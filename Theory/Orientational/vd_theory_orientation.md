# Valid Dictionary — Theory Project Orientation

**Document type:** Orientation (stable).
**Internal ID:** vd-theory-orientation.
**Status:** LIVE. Update only if the project's branch structure or publishing strategy changes.
**Project tag:** vd-project.

**Point.** Give any new reader — human collaborator or fresh Claude instance — enough structural context to work productively in the Theory branch of the Valid Dictionary project. Establish what the VD is, what it produces, how the branches of the project relate, and what Theory's specific job within that structure is.

**Target goals.** Fix the stable frame the rest of the Theory artifacts sit inside. Describe the branch architecture and the publishing strategy it supports. Name Theory's role and explain why its deliverables have the shape they do. Make it possible for an incoming instance to orient without re-deriving the framework from the raw documents.

**Non-goals.** This document does not list open theoretical questions (that is the job of other artifacts and working notes). It does not itself derive or justify any VD commitment (those belong in the dedicated commitment artifacts catalogued by the Commitment Ledger). It does not teach the content of the VD — reading a commitment document is still the right way to learn what a specific commitment says.

**Target audience.** Anyone arriving cold into the Theory branch and needing to be productive quickly.

**Dependencies / references.** None as prerequisites. Companion artifact: `vd-theory-commitment-ledger` (the tabular index of what Theory has committed to and where each commitment is documented).

---

## 1. What the VD produces

The deliverable of a Valid Dictionary instance is a *trace*: a record of how a specific prediction gets generated, with every definitional commitment and every point of human input made explicit and attributed. A trace begins with a goal expression — the quantity the practitioner wants to predict — and walks downward through the dependency graph of the VD's entries, demanding values, resolving headwords against their definitions, and landing external inputs at specific attribution points. When the trace runs to completion, it produces the predicted value together with a full audit of everything it took to get there: which recognition judgments the human made, which modelling choices were committed to, which empirical numbers were supplied, and which constraints were forced by closure diagnostics when the evaluator got stuck.

The trace is not a record of the reasoning a physicist *did*; it is a record of the reasoning the physicist *would have to do*, written out completely, with nothing left in the background. The existing theory of physics is, from the VD's perspective, a compressed form of the same procedure — compressed because the practitioner's training allows most of the procedure to happen without deliberation. The VD makes the procedure uncompressed, and then the trace is what you get when you actually run it.

Everything else in the project — the entries, the laws, the engine, the rules — exists so that traces run cleanly and their outputs are trustable.

## 2. The stack that produces traces

A trace is produced by running a *program* over a *theory*, where the theory is a specific VD instance (an append-only log of entries encoding some body of physics) and the program is an evaluator that knows how to walk the dependency graph those entries induce. Four layers have to be in place for this to work, and each is a branch of the project.

At the foundation sits *Theory*: the philosophical and structural commitments that justify why the VD has the shape it does. Why entries are strings. Why the log is append-only. Why laws are three-cycles with a previously-defined anchor and two new winter words. Why raw_meaning is a real object and not a gesture. These commitments are what make the rest of the stack non-arbitrary. Without them, the framework is just one design choice among many; with them, the framework is a forced consequence of specific arguments that can be inspected and contested.

Above Theory sits *Core*: a mathematical and algebraic accounting of the rules the VD obeys. Core translates theoretical commitments into crisp, checkable predicates — *previously-defined*, *supported word*, *meaningfully defined*, *minimal three-cycle*, *unique November*, *grounding closure* — that either hold of a given VD instance or don't. Core is the specification against which any concrete VD instance can be audited.

Above Core sits *Code*: an implementation of Core's rules in a program that can actually read entries, tokenise definitions, build dependency graphs, detect laws and six-entry houses, and run traces. Code makes Core's rules operative; it is what turns a VD instance from a pile of strings into something you can walk.

Above Code sits *Newton* (and, eventually, other case studies): concrete VD instances that encode specific bodies of physics, against which Code can be run to produce traces. Newton is both a product and a test — a complete encoding of Newtonian mechanics as a VD instance, and simultaneously a stress test that surfaces where the other three layers are incomplete or inconsistent.

## 3. The branches and the publishing strategy

The four branches — Theory, Core, Code, Newton — correspond to four future publications, each with its own scope and non-goals. The branch structure is primarily a *publishing* structure: each branch's artifacts are written to fit inside one prospective paper, so that when publication becomes appropriate, the material is already organised for it rather than needing to be extracted from a tangle.

The branches may or may not correspond to separate working contexts at any given time. Whether a given branch has its own dedicated working environment is an operational question that varies with the project's state; the logical separation between branches — Theory justifies, Core specifies, Code implements, Newton instantiates — holds regardless of where the work physically happens. It is entirely possible (and has in practice been the case) that work on one branch happens in the same environment as work on another, because the branches depend on each other too tightly for strict separation to be efficient. What matters is that the *outputs* are correctly attributed to their branches, so that the publishing structure remains clean.

One consequence of this arrangement is that progress is uneven across branches, and unevenly so for structural reasons rather than neglect. Code has had to move ahead of Core in several places, because encoding Newton has forced implementation decisions that Core has not yet formalised. Newton has likewise moved ahead of Core in places, because the pressure of actually encoding mechanics has surfaced patterns (the six-entry house, the dispatch requirement, the role of the zero acting-object) that Core has not yet caught up to. Core is the branch most frequently in catch-up mode, because its job is to write down, in crisp form, what the other branches have been forced to commit to. This is not a defect of the arrangement — it is what the arrangement looks like when it is functioning correctly. Theory's job, correspondingly, is to make sure the commitments Core is catching up to are themselves defensible.

## 4. Theory's job

The most important thing to understand about Theory is that it is not where the ideas of the VD are being *discovered*. The major commitments of the framework — the structural role of definitions versus meanings, the triplet architecture of laws, the distinction between raw definitional identity and mathematical equality, the append-only discipline, the role of residues as the thing that lets different interpreters' vocabularies be compared without a hidden reference — have been stable in the author's head for a long time. They have been tested against case studies, they have survived several rounds of reformulation at the Core level, and the places where they have needed revision (for instance, the move from modelling the dictionary as a function to modelling it as a log) have been minor corrections of pedagogical convenience rather than shifts in the underlying claims. The theoretical spine is solid.

What is *not* solid is the externalisation of that spine. Until a commitment has been written down in a form that another instance — human or Claude — can read and cite without needing to re-derive it from conversation, the commitment functions as a bottleneck: any branch working on a problem that touches it has to route through the author, who is the only place the commitment currently lives. This is the concrete problem Theory exists to solve. Theory's job is to externalise commitments that already exist, one by one, in a form tight enough that Core can specify against them, Code can implement against them, and Newton can encode against them without going back to source.

The shape this takes is a series of dedicated *commitment documents*, each targeting a single forced theoretical claim and presenting its derivation in a form other branches can cite. The two current examples are the residue derivation note (which establishes raw_meaning as a derivable object) and the what-the-VD-is note (which establishes that the VD's target is physics-as-practiced rather than physics-as-formalism). Both of these are short, tightly scoped, and written to be read once and then pointed at. Future commitment documents will follow the same model. The work of the Theory branch is, essentially, to produce these artifacts at a rate that unblocks the other branches.

A secondary job follows from the first: adjudicating practice rules. Encoding Newton has generated a number of practice-level rules (bookkeeping separated from attribution, net quantities not implying causal sources, recognition as the only allowed vagueness, triplets for commitments and meaningfully-defined entries for execution semantics, and so on). Some of these are at root theoretical claims that belong in Core once they are justified; others are style-guide material that belong in a practice document. Theory takes a view on which is which. This work happens either inside a commitment document (when the rule gets justified and promoted) or as a note in the Commitment Ledger (when it is clear where a rule belongs without needing a full artifact).

## 5. Where Theory artifacts live

The two current Theory commitment documents are the residue derivation note and the what-the-VD-is note, both of which are stable and citable. The current state of what Theory has committed to, where each commitment is documented, and which commitments are still unwritten is tracked in the Commitment Ledger (`vd-theory-commitment-ledger.xlsx`), which is the companion artifact to this orientation. The Commitment Ledger is the right place to look when trying to determine whether a particular claim has been externalised yet or is still living in conversation; it is updated as new commitment documents are produced, and it is the honest record of what Theory has so far managed to put down in writing versus what remains in the author's head.

One convention worth naming: a commitment is considered *documented* only when it has a dedicated artifact (or a dedicated section of one) whose job is to establish it. Being mentioned in passing across several working notes does not count as documented — the content is still in motion until it has a settled home. This is deliberately strict; the point of the ledger is to be honest about the state of externalisation, and loose accounting would defeat the purpose.

## 6. Reading order for an incoming instance

An instance arriving in the Theory branch for the first time should, in rough order: read this document to establish the frame; open the Commitment Ledger and look at what has been documented versus what is still in flight; read the commitment documents that correspond to the task at hand (the residue note is essential context for almost any Theory work; the what-the-VD-is note is essential context for understanding why the framework is shaped the way it is); and then look at whichever Core, Code, or Newton artifacts are relevant to the specific question being worked on.

What should *not* happen is treating the older working drafts (the first draft notes, the amendments, and the various design notes) as authoritative statements of current commitments. Those documents are snapshots from the history of the project; some of what they contain has been superseded, some has been refined, and some is still current. The Commitment Ledger is the mechanism for distinguishing these, and it should be consulted before any of those older documents are cited. Working drafts are valuable as *context* for understanding how the project has arrived at its current positions, but they are not the right thing to cite.

The same goes for this document. This orientation is maintained to be stable, but it is stable because its scope is narrow: it covers the frame, not the content. When it becomes outdated, it will be because the project's structure has changed — a new branch has been added, the publishing strategy has shifted, or Theory's job has been reconceived — and those are rare events that warrant deliberate revision. Content-level drift does not invalidate this document, because content-level material is not here.

## 7. Publishing strategy note

A final point worth making explicit: every Theory artifact is written with its eventual publication in mind. This is why the artifacts have the scope/non-goals/dependencies headers they do, why they cite each other by stable IDs, and why they are kept short and tightly focused rather than sprawling. When the time comes to publish, the intention is that the material can be assembled from existing artifacts with minimal rewriting, rather than extracted from conversational notes and restructured. This imposes some discipline on the artifacts — they have to stand alone, they have to survive being read by an audience that does not have the conversational context, and they have to fit cleanly inside whichever prospective publication they belong to. New artifacts should follow the same discipline.

Cross-references between artifacts carry the load that would otherwise force each artifact to reintroduce its context. An artifact that depends on raw_meaning being a derived object cites the residue note; an artifact that depends on the VD's target being physics-as-practiced cites the what-the-VD-is note. The collection of artifacts held together by these cross-references is, in aggregate, the Theory branch. There is no single master document; there is a network of short commitment documents plus this orientation and the ledger that holds them together.
