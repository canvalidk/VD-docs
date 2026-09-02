# An Editable Scratchpad for LLM Reasoning

## Summary

This document proposes a reasoning tool for large language models: a scratchpad that behaves like a piece of paper the model can write on, edit, and — crucially — *present* to itself. The defining feature is the `present` operation, which renders the current state of the paper into the model's context for a bounded window and then removes it again, collapsing the model's accumulated drafts into a single canonical view. The first half of this document describes the tool as proposed in enough detail that the mechanism is unambiguous. The second half derives the computational cost of using it, and shows that the cost is not a tax the tool pays *despite* helping — it is the very place where the help happens.

---

## Part 1 — The Proposed Tool

### The core idea

Today, when a model wants to revise its own earlier reasoning, it must re-emit the whole thing. There is no cheap way to make a small change to a long passage you wrote three steps ago; you rewrite it from scratch, and every intermediate version stays piled up in the context behind you. This makes incremental editing expensive and pushes models toward getting things right in a few large passes rather than many small corrective ones.

The scratchpad removes that tax. It is an external document — a "piece of paper" — that the model manipulates through commands rather than by reproducing its contents in its own output. The tool holds the canonical state of the document. The model sends edits. This alone makes small changes cheap: the model issues a diff, not a rewrite.

### The editing commands

The model interacts with the paper through a small set of verbs:

- **`write`** — append text to the paper.
- **`edit`** — modify a specified portion of the paper in place.
- **`delete`** — remove a portion of the paper.

These are deliberately few and simple. The goal is a tool the model can learn to use *naturally* — the way a person becomes fluent with an abacus through repeated use, until the instrument becomes an extension of thought rather than something consciously operated. A clean, minimal interface is a precondition for that fluency.

### The `present` command — the heart of the proposal

The novel element is `present`. When the model issues it, the tool renders the *current* state of the paper — however long — into the conversation, so the model can reason against the latest version directly. But `present` carries three further behaviours that distinguish it from a simple "show me the document" call:

**1. A bounded exposure window.** The call takes the form `present(for w tokens)`. The full paper is rendered into context and a counter starts. The model is allowed to reason over the paper's contents for `w` tokens. When the counter expires, the rendering is **automatically deleted** from the context. The paper appears, is available for a defined window of reasoning, and then evaporates.

**2. Supersession of all prior renderings.** Whenever `present` is called, it first **removes every previous rendering** and **resets all counters**. A new `present` supersedes all earlier ones. The consequence is structural and important: *at most one rendering of the paper is ever resident in context at a time.* The act of presenting a fresh view destroys the stale one. There is no accumulation of past presentations.

**3. A clean reasoning checkpoint.** Because `present` clears prior renderings and their counters, each call acts as a reset point for the model's live working state. The model is not reasoning over a sediment of every draft it has produced; it is reasoning over one current artifact.

The effect is that the scratchpad behaves the way physical paper behaves under erasure: you keep working on the *current* state of the page, not a stack of photocopies of every previous state.

### What survives: the operation log

Collapsing the renderings does **not** erase the model's reasoning trail. The sequence of commands — `write`, `edit`, `delete`, `present` — remains visible in the transcript as an append-only log. What gets removed is the *rendered document states*, not the *record of operations*. The model still sees that it wrote X, then edited Y, then presented; it simply does not see five full re-renderings of a growing document.

This is the right information ratio. The command log is a faithful, compact summary of the path taken. The single current rendering is the ground truth of the present state. Together they give the model the shape of its own journey without paying tokens for every frame of it. Nothing is amputated — the verbose intermediate artifacts are replaced by a lightweight trace plus one canonical view.

### Two properties that make the tool safe to add

**It is optional and model-controlled.** The model decides when to `present` and for how long. A capability the model can simply decline to use cannot, in the worst case, do worse than not having it — the model ignores it and behaviour reverts to baseline. So the only question that matters is whether there exists any task on which it helps. The answer is yes: long iterative construction — proofs, specifications, code, structured arguments — where an object passes through many revisions and only the latest matters for the next decision.

**It preserves the trace.** Because the operation log stays, using `present` does not blind the model to how it arrived where it is. This is what lets the tool be aggressive about collapsing renderings without losing the reasoning scaffold.

### Where the document lives in context

For the tool to be cheap to use repeatedly, the rendered paper must sit **late in context** — as close as possible to the point where the model generates its next token, and as far as possible from the system prompt.

The reason is how attention caching works. The context is processed front to back, and the system caches the computed state for a *prefix*. That cache is valid only up to the first token that changed. Everything from a change onward must be recomputed; everything before it is reused for free. So a document that is repeatedly rewritten should be placed at the very end of the context: then each `present` invalidates only the document itself, not the long, stable conversation history in front of it.

Concretely, the context is ordered by how often each region changes — most stable first, most volatile last:

```
[ system prompt ][ settled history ][ append-only operation log ][ current rendering ][ → model generates ]
\______________________ cached, reused _____________________/   \__ recomputed on present __/
            "early"                                                          "late"
```

The append-only log only ever grows at its tail, which is cache-friendly. The single rendered paper is the one block whose *contents* are rewritten in place, so it goes dead last.

---

## Part 2 — The Computational Cost

### Why there is a cost at all

It is tempting to view the recomputation triggered by `present` as pure overhead. It is not — and seeing why is the conceptual key to the whole proposal.

When the paper changes and the model reasons over the new version, the content the model is attending to has *genuinely changed*. The model is now thinking *from* a revised, cleaner artifact rather than from the wreckage of its own drafts. The forward pass over that new content — the **fresh-view calculation** — is the physical substrate on which the improved reasoning actually occurs. The recomputation and the added cognition are *the same event*. You cannot have the model reason over an improved representation without computing over that representation.

This yields a clean principle: **there is no free lunch in which the model reasons over a new representation without computing over it.** A version of this tool with zero recomputation cost would necessarily be a version in which `present` changed nothing the model actually attends to — that is, a no-op. So the cost is not the price paid for the benefit; it *is* the benefit, viewed from the hardware side. A tool that improved the model's reasoning for free would be getting cognition without computation, which cannot exist.

With that established, the question is not *whether* `present` costs anything, but *how the cost scales* — and whether the design keeps it bounded.

### The variables

| Symbol | Meaning |
|---|---|
| **P** | The cached, stable prefix — system prompt, settled history, and the append-only operation log up to the live region. Does not change between presents. |
| **l** | The length of the paper — the full rendering that `present` brings into context. |
| **w** | The exposure window — how many tokens a rendering stays visible before auto-deletion. |
| **r** | The re-presentation time — the average number of tokens between one `present` and the next. |
| **m** | The live (uncached) suffix at a given moment: the span of context since the last cache-valid point. *This is "tokens since the last collapse," not the document size.* |
| **n** | Total resident context at a given moment, $n = P + m$. |

The single most important conceptual correction baked into these definitions: **`m` is not the paper's length.** `m` is the volatile tail that has accumulated since the most recent `present`. The paper's length `l` is only *one* contributor to it, and only while the paper is resident.

### The cost primitive

Attention is quadratic in sequence length: every position attends to every prior position, so a full forward pass over a context of length $n$ costs on the order of $n^2$. But a `present` does **not** recompute the whole context — it recomputes only the live suffix $m$, and each of those $m$ positions attends back over the full resident context $n$. So the cost of one fresh-view calculation is:

$$
C \;\approx\; m \cdot n \;=\; m \,(P + m)
$$

This is the payoff of positioning the paper late in context. By keeping most of $n$ in the cached prefix $P$, the design converts what could have been an $n^2$ recomputation into an $m \cdot n$ one. The entire cost analysis now reduces to a single question: **how large is $m$ when the model reasons, and does the paper persist into the next cycle or not?** That is governed entirely by the relationship between `w` and `r`.

A rendering can end in exactly one of two ways. It can **time out** — `w` tokens elapse and auto-deletion fires — which happens when $w < r$. Or it can be **superseded** — the next `present` fires first and wipes it — which happens when $w \ge r$. Because of the supersession rule, $m$ never contains more than one copy of the paper. These two terminations define the two cases.

### Case 1 — $w < r$ (the window closes before the next present)

The paper times out and goes off-screen before the model presents again. Each cycle of length $r$ has two phases:

- **Exposure phase** (duration $w$, paper resident): the live suffix is $m \approx l + w$, so the cost is $w\,(P + l + w)$.
- **Post-deletion phase** (duration $r - w$, paper gone): the live suffix is only the reasoning since deletion, $m \approx r - w$, so the cost is $(r - w)\,(P + r - w)$.

Per cycle:

$$
C_{\text{cycle}} \;\approx\; \underbrace{w\,(P + l + w)}_{\text{paper resident}} \;+\; \underbrace{(r - w)\,(P + r - w)}_{\text{paper deleted}}
$$

The decisive feature: **the paper's length $l$ appears only in the first term, multiplied by $w$ — not by $r$.** The expensive $l$-sized block is paid for only during its exposure window, then it is gone. It does not carry forward. The paper can be large; it is merely transient.

Amortized over the $r$ tokens of a cycle, the paper's contribution to the per-token cost is:

$$
\frac{w}{r} \cdot l
$$

The ratio $w/r$ is a **duty cycle** — the fraction of time the paper is on-screen. A small $w/r$ means the expensive paper is rarely resident, so it is cheap. This is the dial. The cognitive reading of this regime: *show me the paper, let me extract what I need, then get it out of my way so I reason against my own compressed takeaways.* The paper as **intermittent reference**.

### Case 2 — $w \ge r$ (the next present fires before the window closes)

Here the model presents again before the current rendering would have timed out. Under the supersession rule, the new call wipes the current rendering and immediately lays down a fresh one. The paper is therefore **continuously resident, but only ever as a single copy** — every present refreshes it before the window would have cleared it, and destroys the previous copy in the same act. There is no off-screen phase.

At steady state the live suffix is one paper plus the reasoning since the last present:

$$
m \approx l + r
$$

and the per-event cost is:

$$
C \;\approx\; (l + r)\,(P + l + r)
$$

This is **sustainable, not pathological.** The $l$ term is linear and singly-resident. The cognitive reading: *keep the paper in front of me the whole time — I am actively working on it.* The paper as **persistent workspace**. It costs a steady $l$, but the paper is never absent.

### The supersession guarantee

It is worth being explicit about what the "a new `present` wipes all prior renderings" rule buys, because it is the structural safety property of the design.

*Without* supersession, Case 2 would be a disaster. Renderings would accumulate: a new paper arriving every $r$ tokens, each living for $w$ tokens, would leave roughly $\lceil w/r \rceil$ copies resident simultaneously. The resident paper mass would be $\approx (w/r)\, l$, permanently in the suffix, and the cost would go quadratic in that mass — $\big((w/r)\,l\big)^2$ — a genuine blow-up.

*With* supersession, that case cannot occur. The resident paper mass is capped at **exactly one $l$, in every regime**:

| | **Without supersession, $w \ge r$** | **With supersession, $w \ge r$** |
|---|---|---|
| Resident paper mass | $(w/r)\, l$ — stacked | $l$ — single copy |
| Cost | quadratic in $(w/r)\,l$ — catastrophic | $(l + r)(P + l + r)$ — linear in $l$ |

So the auto-deletion (`w`) and the supersession (a new `present`) are **two independent mechanisms that bound residency** — `w` bounds it by *time*, supersession bounds it by *count*. Together they guarantee that $m$ never holds more than one rendering of the paper, no matter how `w` and `r` relate.

### The resulting design picture

The $w < r$ versus $w \ge r$ boundary does **not** separate a safe mode from a dangerous one — the supersession rule makes both modes safe. It separates two legitimate operating styles:

| | **$w < r$** (timeout wins) | **$w \ge r$** (supersession wins) |
|---|---|---|
| Renderings resident | $\le 1$, with off-screen gaps | exactly $1$, continuously |
| Paper duty cycle | $w/r$ — sometimes off-screen | $1$ — always on-screen |
| Steady-state $m$ | oscillates: peak $l + w$, trough $r - w$ | roughly constant, $l + r$ |
| Amortized paper cost | $(w/r)\cdot l$ — discounted by duty cycle | $l$ — full, always paid |
| Role of the paper | intermittent reference | persistent workspace |

Because supersession guarantees safety from the *count* side, the window `w` is no longer a safety constraint — it is purely a **duty-cycle dial**. Choosing $w < r$ does not avert catastrophe (nothing needs averting); it buys *economy*, letting the paper go off-screen for $r - w$ tokens per cycle so the model pays only $(w/r)\,l$ instead of the full $l$. The choice between the two modes is therefore cognitive rather than defensive: reference-then-internalize when the paper is something to consult, persistent-workspace when it is something to actively build.

### The bottom line

The per-event fresh-view calculation cost is $m\,(P + m)$, where $m$ — the volatile tail since the last `present`, never the paper size itself — is held in check by two independent bounds. With the paper positioned late in context, the cost is linear in the conversation length $P$ for a fixed live suffix, and the supersession rule caps resident paper mass at a single $l$ in every regime, eliminating the only path to quadratic blow-up. The window `w`, relative to the re-presentation cadence `r`, then tunes the duty cycle — and with it the trade between cheap intermittent reference and continuous workspace.

And the cost that remains is exactly the cost that *should* remain: the fresh-view calculation is the forward pass over the model's deliberately improved working state. It is not overhead grudgingly tolerated for the sake of a benefit elsewhere. It is the benefit itself, measured in compute.

---

## Part 3 — Comparison with Existing Context Cleanup

The analysis so far treated the scratchpad in isolation. In practice it would run on a platform that *already* manages context — clearing old tool results and compacting history once resident context grows too large. This part asks how the tool compares against that backdrop, and shows that the existing cleanup machinery does not merely coexist with the tool; it makes the tool nearly free to implement and exposes two further savings.

### What cleanup actually is

The existing cleanup is **threshold-triggered, not periodic.** It does not fire on a clock every fixed number of tokens. It fires when resident context crosses a ceiling, evicts the oldest material to get back under, and resumes. So the "average cleanup frequency" is not a free-standing constant — it is *emergent*, determined by how fast context grows toward the ceiling.

Let **T** be the cleanup threshold (the context ceiling). Then cleanup fires once every:

$$
q \;\approx\; \frac{T}{\text{net context growth per token of reasoning}}
$$

This is the pivot for everything below. The tool does not change the ceiling $T$. It changes the *growth rate*, which changes $q$. Slower growth means a larger $q$, which means cleanup fires *less often*. That second-order effect is invisible if one treats $q$ as fixed, and it is one of the two benefits derived here.

### The premise: existing cleanup makes the tool nearly free

Suppose cleanup is already firing often enough that $q$ is comparable to or smaller than $r$ or $w$. Then the platform is already paying to evict context at roughly the cadence the tool wants to collapse it. The tool's supersession-collapse is, mechanically, the *same operation* the platform already performs as eviction — invalidating the cache from some point and dropping resident tokens. The tool is not adding a new cost category; it is **redirecting eviction the platform already does toward a smarter target** (the stale paper renderings specifically, rather than whatever is oldest). Under this premise the tool's own collapse cost is close to free, and we can focus on what it saves.

### Benefit 1 — Saving computation by shortening context length

*Without the tool*, the model revises by re-emitting, so every revision leaves its predecessor resident. After $k$ versions of an $l$-sized object, the resident draft sediment is:

$$
\text{baseline draft mass} \;\approx\; \sum_{i=1}^{k} l_i \;\approx\; k \bar{l}
$$

— $k$ stale copies accumulating until cleanup evicts them.

*With the tool*, supersession caps resident paper mass at a single $l$. The $k-1$ stale copies never exist:

$$
\text{tool draft mass} \;\approx\; l \quad (\text{versus } k\bar{l})
$$

The eliminated sediment is $\Delta m \approx (k-1)\bar{l}$. But the value of removing it is not those tokens counted once — it is those tokens multiplied by everything that attends over them on every subsequent forward pass. Through the cost primitive $C \approx m(P+m)$, removing $\Delta m$ tokens from a resident context of size $n$ saves, per forward pass:

$$
\Delta C_{\text{length}} \;\approx\; \big[\, n^2 - (n - \Delta m)^2 \,\big] \;=\; 2n\,\Delta m - (\Delta m)^2
$$

The saving is **quadratic in context size**: you not only stop computing the stale tokens, you stop every other resident token from attending over them. The longer the conversation (larger $n$), the more each eliminated stale draft is worth. This is the first benefit — the tool keeps $n$ smaller, and the returns on a smaller $n$ compound quadratically.

### Benefit 2 — Saving computation by decreasing q

Cleanup itself costs compute: eviction invalidates the cache from the eviction point and forces recomputation of the suffix — the same $m(P+m)$ structure, now paid by the platform on every cleanup. If cleanup fires every $q$ tokens, its amortized cost per token of reasoning is $C_{\text{cleanup}} / q$.

The tool slows the growth rate, because draft sediment no longer accumulates. Split the growth into two parts: $g_0$, the irreducible growth from genuine new reasoning (which any approach keeps), and the draft-sediment growth the tool eliminates (a paper-sized chunk every $r$ tokens):

$$
\text{growth}_{\text{baseline}} \approx g_0 + \frac{\bar{l}}{r}, \qquad \text{growth}_{\text{tool}} \approx g_0
$$

Therefore:

$$
q_{\text{baseline}} \approx \frac{T}{g_0 + \bar{l}/r}, \qquad q_{\text{tool}} \approx \frac{T}{g_0}
$$

$$
\frac{q_{\text{tool}}}{q_{\text{baseline}}} \;\approx\; \frac{g_0 + \bar{l}/r}{g_0} \;=\; 1 + \frac{\bar{l}}{g_0\, r}
$$

Cleanup fires **less often by a factor of $1 + \bar{l}/(g_0 r)$.** When draft sediment was a large share of growth — small $g_0$, or large papers presented frequently (small $r$) — this factor is large, and the tool multiplies the cleanup interval several-fold. Each averted cleanup saves a full $C_{\text{cleanup}}$. The amortized saving is:

$$
\Delta C_{\text{cleanup}} \;\approx\; C_{\text{cleanup}}\!\left(\frac{1}{q_{\text{baseline}}} - \frac{1}{q_{\text{tool}}}\right) \;=\; \frac{C_{\text{cleanup}}}{T}\cdot\frac{\bar{l}}{r}
$$

The cleanup-frequency saving scales directly with the draft growth rate $\bar{l}/r$ the tool removes. The faster you were generating sediment, the more cleanups the tool averts.

### Why the regimes align

The premise and the benefits reinforce each other. Frequent existing cleanup (small $q$) means a high growth rate, which means the draft-sediment term $\bar{l}/r$ is a large fraction of growth — and that is exactly the condition under which both benefits are largest:

- **Benefit 1** (shorter $n$) is large because the eliminated sediment was large.
- **Benefit 2** (rarer cleanup) is large because $\bar{l}/(g_0 r)$ is large.
- The tool's **added cost** is small because supersession-collapse is the eviction the platform was already performing, retargeted.

So the conditions that make the tool cheap to run are the same conditions that make its savings largest. The tool is most worth having precisely when context pressure is already high — which is when one would want it anyway.

### Two caveats

**The two benefits are not independent.** Benefit 1 is partly the *cause* of Benefit 2: a smaller resident context grows toward $T$ more slowly. Summing them naively double-counts the shared mechanism. The clean decomposition is to read them as two effects of one cause — eliminated draft sediment — where Benefit 1 is the per-forward-pass saving at a fixed cleanup schedule and Benefit 2 is the saving from the schedule itself stretching out.

**The $g_0$-invariance assumption is load-bearing.** The $q$-improvement assumes $g_0$ — the rate of genuine reasoning output — is unchanged by the tool. But if cheap editing causes the model to reason *more* (the same open question of whether cheap revision unlocks a more iterative reasoning mode), then $g_0$ rises and the $q$-benefit shrinks accordingly. The cleanup-frequency saving is therefore contingent on the tool not inducing a compensating increase in genuine output. This is the empirical crux of the whole comparison, and it cannot be settled by the cost model alone — only by building the tool and measuring.
