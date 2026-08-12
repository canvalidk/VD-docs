# Authority Documents and the Name-Free Structure of Language

**Status:** Working derivation note  
**Project:** Valid Dictionary / VD foundations  
**Date:** 11 August 2026  
**Scope:** This note captures the current argument only. It records what has been earned, what remains provisional, and how the route begins to resemble the VD without yet deriving the whole VD.

---

## 0. Central idea

Words are arbitrary, but locally changing a word changes what a sentence does.

The resolution is that a word can be changed without substantive consequence only under a **complete substitution**: every causally relevant use of the word must be changed together. A local edit changes which already-installed linguistic handle is being used. A complete substitution changes the handle assignment while preserving the underlying language structure.

This leads to a new question:

> If the surface names are arbitrary, what stores the choice of one naming arrangement rather than another?

The proposed answer is a new mathematical object:

> An **authority document** represents the arbitrary naming choices of a language.

“Represents” is meant in the mathematical sense in which a matrix represents a linear transformation. A mistaken matrix still represents a transformation—just not the transformation the writer intended. Likewise, a mistaken authority document still represents a naming arrangement, even if that arrangement was never realised by any linguistic community.

The route then asks what a language must look like when its names are removed. The current answer is not a simple graph of words and pairwise references. It is a recursively structured collection of whole linguistic contexts. Surface names are added afterward by an authority document, understood as a gauge choice.

---

## 1. The starting puzzle: arbitrary names, non-arbitrary effects

Consider:

> Cat likes to eat fish.

Replace only `Cat` with `Dog`:

> Dog likes to eat fish.

The sentence now affects a trained interpreter differently. This does not show that the name `Cat` was intrinsically tied to cats. It shows that the rest of the language—and the interpreter’s training in that language—was held fixed while one local stimulant was changed.

Now imagine a stronger operation. Every causally relevant occurrence of `Cat` and `Dog` is exchanged:

- every spoken sentence;
- every written sentence;
- every dictionary;
- every lesson;
- every correction given to a learner;
- every memory and installed response that depended on those uses;
- every future use made under the same convention.

In the resulting world, cats are called “dogs” and dogs are called “cats”, but the substantive organisation of the language has not changed.

This gives the first principle:

> **A name is arbitrary under complete substitution, not under isolated substitution.**

Or more compactly:

> **Labels are globally arbitrary but locally load-bearing.**

A complete renaming may be written as a permutation \(\pi\) of the surface vocabulary. If the whole language is transformed consistently, then the original and renamed languages are structurally equivalent:

\[
L \sim \pi(L).
\]

The surface forms have changed. The pattern of use has not.

---

## 2. Why the language does not store its own naming choice

If a language remains structurally equivalent under a complete permutation of its names, then the language structure by itself does not determine which of those names must occupy which roles.

The sentences of the language cannot uniquely store the choice because the entire body of sentences can be transformed along with the choice.

The naming arrangement is therefore additional information.

This motivates an authority document.

### Working definition

> **An authority document is a mathematical object that represents a particular assignment of surface names to the underlying objects or slots of a language.**

At this stage, “authority” does not mean that the document magically makes the represented assignment true. The document may be ignored, miscopied, obsolete, or never implemented. Its representational content remains well defined.

---

## 3. Representation is not realisation

The matrix analogy is important because it prevents several confusions.

Suppose a writer intends to represent the identity transformation but writes

\[
\begin{pmatrix}
1 & 0\\
0 & 2
\end{pmatrix}.
\]

The matrix does not fail to represent anything. It represents a different linear transformation from the intended one. That transformation may never have been physically realised or deliberately used. It is nevertheless the transformation represented by the matrix.

The same distinction should hold for authority documents.

Let \(D\) be an authority document and let

\[
\operatorname{Rep}(D)=g_D
\]

be the naming assignment represented by it.

Let \(g_*\) be the naming assignment actually realised in some linguistic community. Then correctness is a separate relation:

\[
D\text{ is accurate with respect to the realised language}
\iff
g_D=g_*.
\]

If \(g_D\neq g_*\), the document still represents a coherent alternative naming arrangement. It simply represents the wrong one relative to that community.

This yields two separate questions:

1. **Representational question:** What naming assignment does this authority document represent?
2. **Realisation question:** Is that naming assignment the one actually installed or used?

The present derivation begins with the first.

---

## 4. Authority documents as gauge choices

The underlying language may admit many surface naming assignments related by complete renaming. These assignments can be treated as different representatives of one underlying structure.

Let \(\mathcal W\) be the collection of underlying language objects and let \(\mathcal N\) be a collection of available surface names. A strict naming gauge may be written schematically as

\[
g:\mathcal W\to\mathcal N.
\]

A permutation \(\pi\) of the names produces a new gauge:

\[
g' = \pi\circ g.
\]

The underlying language object \(\mathcal W\) has not changed. Only its rendered names have changed.

In this sense:

> **An authority document represents a gauge choice for the language.**

This does not yet mean that an authority document is a rule that selects a gauge uniquely from every possible equivalence class. It means only that the document represents one particular named representative.

A canonical authority document might choose one displayed name for each underlying object. A richer linguistic system might allow several surface handles to be attached to the same object. That distinction can remain open for now.

---

## 5. The name-free substitution test

To understand what information an authority document must contain, ask:

> Can a specific renaming be specified without using the names that are being renamed?

Saying “swap `Cat` and `Dog`” presupposes the current naming arrangement. It does not reveal how the authority document identifies the things that receive those names.

A first response is to introduce distinct underlying slots:

\[
S=\{1,2,3,\ldots\}.
\]

A naming assignment might then contain

\[
(1,\texttt{Cat}),
\qquad
(2,\texttt{Dog}),
\qquad
(3,\texttt{Fish}).
\]

A substitution can now be described without naming the occupants:

> Exchange the names assigned to slots 1 and 2.

This correctly distinguishes two operations that are often conflated:

### Renaming the occupants of fixed slots

\[
(1,A),(2,B),(3,C)
\longrightarrow
(1,C),(2,A),(3,B).
\]

The slots remain fixed; the names move.

### Permuting the slots themselves

\[
1\mapsto2,
\qquad
2\mapsto3,
\qquad
3\mapsto1.
\]

This is a transformation of the underlying carrier structure.

The authority-document problem concerns the first operation. However, the slot-ID picture is only temporary. The next objection shows that the underlying object is richer than a set of numbered nodes connected by simple arrows.

---

## 6. Why a simple dependency graph is too lossy

Suppose the language contains two definition-like structures:

\[
A := \operatorname{Res}_1(B,C),
\]

\[
A := \operatorname{Res}_2(D,E).
\]

A simple graph would flatten this into

\[
A\to B,
\quad
A\to C,
\quad
A\to D,
\quad
A\to E.
\]

That representation loses essential information.

It does not preserve that:

- \(B\) and \(C\) occur together in one definition;
- \(D\) and \(E\) occur together in another definition;
- there are two distinct structured contexts involving \(A\);
- the two contexts may use different residual operations \(\operatorname{Res}_1\) and \(\operatorname{Res}_2\);
- argument order or position may matter within each context.

The pairing is not an optional annotation. It is part of the linguistic information.

Therefore the name-free language object cannot be merely

\[
\text{words} + \text{pairwise edges}.
\]

It needs something closer to

\[
\text{language objects}
+
\text{whole structured contexts}
+
\text{positional/residual formers}.
\]

The ordinary dependency graph is then a **lossy projection** of this richer object.

---

## 7. Entry numbers are not part of the ontology

The next simplification is that entry numbers are unnecessary in the underlying object.

Instead of treating \(E_1\) and \(E_2\) as permanent entities, collect the structured contexts together as members of the object currently named \(A\):

\[
W_A
=
\left\{
((W_B,W_C);R_1),
((W_D,W_E);R_2)
\right\}.
\]

A second object might be

\[
W_B
=
\left\{
((W_A);R_3),
((W_J,W_K);R_1)
\right\}.
\]

The whole language is then schematically

\[
\mathcal W
=
\{W_A,W_B,W_C,\ldots\}.
\]

The letters \(A,B,C,\ldots\) are temporary gauge labels used for readability. They are not intrinsic parts of the objects.

An “entry number” is therefore only a temporary conversational coordinate:

> Call this member of \(W_A\) “entry 1” while we discuss it.

The numbering helps serialisation and audit. It need not belong to the underlying mathematical object.

This is an important shift:

> **A headword-object is represented by the collection of its structured linguistic contexts, not by a numbered list of definitions.**

The list and its numbers are one possible printout of the set.

---

## 8. The role of sets and the treatment of synonyms

The discussion deliberately refuses to manufacture distinctions that the language itself never uses.

Suppose `fast`, `quick`, and `rapid` are perfectly interchangeable throughout all relevant linguistic contexts. Replacing every instance of all three by `rapid` loses nothing the present theory cares about.

Then we are content to treat them as one underlying language object.

This gives a quotient principle:

> **If no relevant structured use distinguishes two alleged language objects, treat them as one object.**

Sets are attractive here because extensional identity gives the desired behaviour:

\[
X=Y
\iff
\forall z\,(z\in X\leftrightarrow z\in Y).
\]

If two alleged word-objects contain exactly the same complete collection of structured contexts, then they are the same set-object. Giving the same object several surface names does not multiply the underlying object.

Thus one may have

\[
\texttt{fast}\mapsto W_7,
\qquad
\texttt{quick}\mapsto W_7,
\qquad
\texttt{rapid}\mapsto W_7.
\]

Or a canonical authority document may choose only

\[
W_7\mapsto\texttt{rapid}.
\]

The inability to distinguish perfect synonyms is not treated as a defect. It is taken as evidence that no distinction needs to be represented.

This is not yet a complete theory of ordinary synonymy. Real words often differ in register, frequency, collocation, emotional effect, grammatical behaviour, or historical distribution. Any such difference would appear as a difference in their structured-context sets. The collapse applies only to distinctions that truly disappear at the chosen level of description.

---

## 9. Concrete example: “Cat likes to eat fish”

Take the sentence:

> Cat likes to eat fish.

The naive graph representation would record pairwise connections between `Cat` and the other words. That loses order and sentence-level composition.

Instead, store the whole ordered context in the object currently named `Cat`:

\[
W_{\text{Cat}}
\ni
R_1
\bigl(
W_{\text{likes}},
W_{\text{to}},
W_{\text{eat}},
W_{\text{fish}}
\bigr),
\]

where

\[
R_1
=
(\square,
\operatorname{slot}_1,
\operatorname{slot}_2,
\operatorname{slot}_3,
\operatorname{slot}_4).
\]

The blank \(\square\) marks the position occupied by the object whose set is being defined. The residual/context former \(R_1\) records that the target occurs first, followed in order by four supplied language objects.

In the shorter notation used during the discussion:

\[
\text{Cat}
:=
R_1(\text{likes},\text{to},\text{eat},\text{fish}).
\]

This statement should not be read as saying that the surface string `Cat` intrinsically contains those words. It says that the underlying object currently named `Cat` has this structured occurrence as one member of its total language record.

The same sentence can contribute corresponding members to the other participating word-objects. For example, the object currently named `fish` may contain a context former whose blank lies in the final position:

\[
W_{\text{fish}}
\ni
R_5
\bigl(
W_{\text{Cat}},
W_{\text{likes}},
W_{\text{to}},
W_{\text{eat}}
\bigr),
\]

with

\[
R_5
=
(
\operatorname{slot}_1,
\operatorname{slot}_2,
\operatorname{slot}_3,
\operatorname{slot}_4,
\square
).
\]

As more sentences are uttered, each language object accumulates more structured contexts:

\[
W_i
=
\{
R_\alpha(\ldots),
R_\beta(\ldots),
R_\gamma(\ldots),
\ldots
\}.
\]

The language as a whole becomes a mutually recursive system because the structured contexts contained in one word-object refer to other word-objects, whose own context sets refer back in turn.

---

## 10. How the substitution now works

Let \(g\) be the authority document’s current naming gauge:

\[
g(W_{\text{Cat}})=\texttt{Cat},
\]

\[
g(W_{\text{likes}})=\texttt{likes},
\]

\[
g(W_{\text{fish}})=\texttt{fish},
\]

and so on.

The underlying context is stored as

\[
R_1
\bigl(
W_{\text{likes}},
W_{\text{to}},
W_{\text{eat}},
W_{\text{fish}}
\bigr)
\in
W_{\text{Cat}}.
\]

When rendered under \(g\), it appears as:

> Cat likes to eat fish.

Now define a new gauge \(g'\) such that

\[
g'(W_{\text{Cat}})=\texttt{Dog},
\]

while the underlying structured language object remains unchanged.

When the same recursive object is rendered under \(g'\), every occurrence of \(W_{\text{Cat}}\) is displayed as `Dog`:

> Dog likes to eat fish.

No search through the corpus for the character string `Cat` is fundamentally required. Every occurrence already points to the same underlying object. Changing the gauge-name of that object changes all rendered occurrences together.

This is the desired complete substitution.

More generally, a name permutation \(\pi\) changes the gauge:

\[
g' = \pi\circ g.
\]

The linguistic structure remains fixed. Only its authority-document representation changes.

---

## 11. Why this is richer than search-and-replace

Ordinary text search treats each occurrence of `Cat` as an independent string match. It then tries to update all matching strings consistently.

The current construction reverses that picture:

1. There is one underlying object \(W_{\text{Cat}}\).
2. Every linguistic context refers to that object.
3. The authority document assigns a surface name to it.
4. Rendering produces the repeated visible strings.

So the repeated word tokens are outputs of one naming assignment rather than independent objects that must later be coordinated.

The substitution is therefore not fundamentally:

\[
\text{find all strings and replace them}.
\]

It is:

\[
\text{change the name assigned to one underlying object and re-render}.
\]

This is exactly the sort of information the authority document was introduced to store.

---

## 12. Cycles are expected, but triplets are not yet selected

Because language objects contain contexts that refer to other language objects, the system will naturally contain recursive dependence.

For example:

\[
W_A
=
\{((W_B,W_C);R_1),\ldots\},
\]

while

\[
W_B
=
\{((W_A);R_3),\ldots\}.
\]

Following the structure may therefore return to an earlier object. Cycles are not an accidental defect in this picture. They are a natural possibility in a recursively defined language.

This aligns with one existing VD observation:

> Cycles are structurally special because recursive expansion does not escape them.

However, this route has **not** yet selected \(N=3\) as the privileged cycle size.

That is acceptable because the VD’s preference for triplets arises from a second and independent idea. The two steps are:

1. **Cyclicity is special.** Some mutual dependencies do not reduce into an acyclic chain.
2. **Triangles are primitive.** Larger apparent polygons are analysed as compositions of overlapping triangles, just as polygons can be triangulated.

The current route may plausibly recover the first step before the second. It should not be criticised for failing to derive triplets at the stage where it has only begun to expose recursive cycles.

The VD’s geometrical stance can be stated provocatively as:

> “That is not a fundamental pentagon. It is several triangles with some internal sides or intermediate terms not yet made explicit.”

The triangulation constraint remains a later problem.

---

## 13. Emerging correspondence with the VD

The new route begins outside the VD, from the arbitrariness of names. Nevertheless, several VD-shaped structures are already appearing.

### 13.1 Headwords become gauge labels

A headword is the current surface name assigned to an underlying recursively structured language object.

The object survives a complete renaming. The headword does not.

### 13.2 Definitions become structured-context members

A word-object is not assigned one privileged definition. It is associated with a collection of structured contexts:

\[
W_A
=
\{d_1,d_2,d_3,\ldots\}.
\]

This naturally accommodates the VD fact that one headword may have several entries doing different work.

### 13.3 Entry numbers become serialisation coordinates

The permanent object is the set of structured contexts. `E1`, `E2`, and so on are temporary labels used to discuss, order, or audit members when the object is printed linearly.

This suggests that the append-only VD log may be a particular serialised presentation of a more fundamental unordered or partially ordered object. That possibility has not yet been derived.

### 13.4 Residuals begin as context/composition formers

The symbols \(R_1,R_2,\ldots\) currently preserve:

- the position of the target;
- the order of the other participants;
- which participants occur together;
- potentially grammatical, operational, or inferential structure not captured by bare co-occurrence.

This already resembles the VD insistence that a residual is not mere leftover prose. However, the present route has not yet excavated the full operational nature of residuals, handles, dossiers, or disciplined interpreter effects.

### 13.5 The dependency graph is a projection

A VD dependency graph that draws arrows from a headword to every headword appearing in its entry records useful information, but it forgets the internal grouping of those mentions.

The richer object is entry- or context-level. The graph is derived from it by flattening each structured member into pairwise references.

### 13.6 Synonym collapse becomes extensional identity

If two alleged language objects have no distinct structured contexts at the chosen level, they collapse into one set-object. Several surface names may point to it, or one canonical gauge-name may replace all of them.

---

## 14. What has been earned so far

The discussion supports the following provisional conclusions.

### 14.1 Complete renaming symmetry

A language may be transformed by a globally consistent permutation of its surface names without changing its underlying organisation.

### 14.2 Naming information is additional

The underlying language structure does not uniquely determine which arbitrary surface name occupies which role.

### 14.3 Authority documents represent naming choices

An authority document represents one naming assignment in the same broad sense that a matrix represents a linear transformation.

### 14.4 Representation and realisation are distinct

A document may coherently represent a naming arrangement that was never implemented or that differs from the realised language.

### 14.5 A simple graph is insufficient

Pairwise dependency edges lose co-occurrence grouping, argument order, residual form, and the distinction between multiple structured contexts involving the same target.

### 14.6 Entry IDs are not fundamental

Structured contexts can be collected directly as members of a word-object. Numbers are temporary labels introduced for discussion or serialisation.

### 14.7 Perfectly indistinguishable synonyms may be collapsed

The theory is permitted to identify surface names whose complete relevant use is indistinguishable.

### 14.8 Concrete substitution is now possible

A sentence can be stored as a structured context involving underlying language objects. A gauge change then renames every occurrence of one object simultaneously.

---

## 15. What has not yet been earned

The current construction remains a working direction, not a finished foundation.

It has not yet established:

- the exact mathematical nature of the underlying language objects;
- whether ordinary well-founded sets are sufficient for the recursive system;
- the correct identity criterion for recursively presented set-objects;
- whether every utterance-event, every sentence-type, or some selected corpus belongs in the object;
- how repeated identical utterances and their frequencies are represented;
- how time, speaker, context, tone, gesture, and non-verbal conditions enter;
- how morphology and inflection are represented;
- what information is contained in a residual/context former \(R\);
- whether word order alone is sufficient even for the simplest language fragment;
- how an authority document is itself written without circularly relying on the language it names;
- how the represented gauge becomes causally or socially realised;
- the VD append-only rule;
- the November/winter distinction;
- the six-entry chimney/triplet/wall structure;
- the principle that decomposes larger cycles into triplets;
- lazy evaluation and answer-producing traces;
- the full handle/dossier account of raw meaning.

These are not objections to the route. They are the next objects to excavate.

---

## 16. Technical cautions

### 16.1 Sentence types versus utterance events

If the object stores only sentence types, repeating the exact same sentence adds no new member to an ordinary set. That may be acceptable if only structural possibility matters.

If frequency, training, or historical installation matters, then individual utterance-events must remain distinguishable. A member may need to include a time, speaker, event identity, or other contextual record:

\[
U_k
=
(
\text{structured sentence},
\text{speaker},
\text{time},
\text{context},
\ldots
).
\]

Two verbally identical utterances can then be different members because they are different events.

### 16.2 The blank is a real structural position

In

\[
R_1=(\square,s_1,s_2,s_3,s_4),
\]

the blank is not decorative. It records where the target object occurs in the context. A corresponding context for a different target requires a different placement of the blank.

### 16.3 Order is only one part of composition

The example currently lets \(R_1\) encode order. Real linguistic composition may also require:

- grammatical role;
- scope;
- binding;
- tense;
- number;
- modality;
- dependency type;
- pragmatic context;
- prosody;
- non-verbal situation.

The notation \(R\) is therefore deliberately open. It stands for whatever structured remainder is needed once the participating language objects are supplied.

### 16.4 Extensional collapse depends on the chosen description level

Two words may collapse at one coarse level and separate at a finer one. `fast` and `quick` may be interchangeable in a simplified corpus but differ once register, collocation, rhythm, or emotional reaction is included.

Synonymy is therefore relative to the information admitted into the structured-context sets.

---

## 17. Compact working model

The current proposal can be compressed into four layers.

### Layer 1: underlying language objects

\[
\mathcal W=\{W_1,W_2,W_3,\ldots\}.
\]

### Layer 2: structured contexts

Each object is given by the set of contexts in which it occurs:

\[
W_i
=
\{
R_{i1}(W_{a_1},\ldots,W_{a_n}),
R_{i2}(W_{b_1},\ldots,W_{b_m}),
\ldots
\}.
\]

Each \(R\) records at least the target position, grouping, and order of participants.

### Layer 3: authority document / naming gauge

\[
g_D:\mathcal W\to\mathcal N.
\]

The authority document \(D\) represents \(g_D\).

### Layer 4: rendering

A renderer replaces each underlying object in a structured context with its gauge-name under \(g_D\), producing ordinary sentences.

A complete substitution changes \(g_D\), not the underlying contexts.

---

## 18. The concrete substitution trace

Start with the underlying context:

\[
R_1
\bigl(
W_{\text{likes}},
W_{\text{to}},
W_{\text{eat}},
W_{\text{fish}}
\bigr)
\in
W_{\text{Cat}}.
\]

Authority document \(D\) represents:

\[
g_D(W_{\text{Cat}})=\texttt{Cat}.
\]

Rendering gives:

> Cat likes to eat fish.

A second authority document \(D'\) represents:

\[
g_{D'}(W_{\text{Cat}})=\texttt{Dog}.
\]

The underlying context is unchanged. Rendering gives:

> Dog likes to eat fish.

Every other context containing \(W_{\text{Cat}}\) changes at the same time.

This is the first explicit demonstration that the proposed storage form is sufficient to perform the complete name substitution that motivated the investigation.

---

## 19. Research correspondences to investigate later

Several established areas appear likely to provide useful comparison machinery, without yet being identified with the present construction:

- gauge choices and quotient structures;
- nominal sets and finite permutations of names;
- alpha-equivalence and name-free variable representations;
- structuralist accounts of linguistic arbitrariness;
- permutation and model-theoretic arguments about reference;
- recursive and non-well-founded set presentations;
- hypergraphs, incidence structures, and operadic or compositional representations.

These are comparison targets. The present derivation should continue to be judged by whether each piece is forced by the naming problem, not by whether it can be made to resemble an existing formalism.

---

## 20. Working summary

The route now runs as follows:

```text
A local word replacement changes a sentence.

A complete replacement of every causally relevant occurrence does not change
what the language does.

Therefore surface names are arbitrary gauge labels.

The language itself does not uniquely store which gauge was selected.

An authority document represents that naming choice.

To understand the document, specify substitutions without using the names.

Temporary slot IDs make this possible, but a simple graph of slots is too
lossy: it destroys whole-context grouping, order, and multiple definitions.

So store each underlying language object as a set of structured contexts in
which it occurs.

Entry numbers are temporary names for members of those sets, not fundamental
parts of the object.

Perfectly indistinguishable synonyms collapse into one underlying object.

The sentence “Cat likes to eat fish” becomes one ordered context in the object
currently named Cat.

A gauge change renames that object and thereby changes all of its rendered
occurrences simultaneously.
```

The most important achievement is that the original complete-substitution operation is no longer merely imagined. The proposed object now contains enough information to perform it.

The next foundational pressure point is the nature of the residual/context formers \(R\): what exactly must they preserve, and what kind of object is left when all replaceable language objects have been removed from an utterance?
