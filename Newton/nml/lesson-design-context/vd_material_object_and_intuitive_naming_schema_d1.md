> **Generic seed copy — nml lesson-design context. Do not edit here.**
> **Home note:** `material_object_naming`, draft `d1` — `Newton-analysis/material_object_naming/vd_material_object_and_intuitive_naming_schema_d1.md`.
> Part of the invariant core for any nml lesson-drafting session: the cognitively-anchored naming method governing terminology decisions. Copy into a new lesson's ai-context-bundle after refreshing from the home note.

---

# From `material-object` to a Cognitively Anchored Naming Schema

**Date:** 2026-07-14  
**Status:** Working argument note  
**Context:** VD Newton terminology and its possible generalisation into an educational naming method

---

## Thesis

The VD Newton concept currently under consideration is not merely a geometrical point following a trajectory. It is the persistent mechanical individual to which a trajectory, an inertial mass, a mechanical composition, and a net force belong. We argued that `material-object` is the best name for this concept.

The argument was not that the English word *object* is a universal word learned in infancy. The evidence supports a subtler claim: humans possess an early, prelinguistic capacity to represent persistent physical individuals, while *object* is a later, highly general word that can reactivate much of that earlier structure. The modifier *material* restricts the word to the intended physical branch and suppresses several competing philosophical, grammatical, and computational senses.

This reasoning suggests a general naming principle:

> A technical concept should, where possible, be named by attaching it to the learner's most structurally appropriate prior concept, and then qualifying that familiar name only as much as is required for formal precision.

The aim is not familiarity by itself. The aim is **maximum cognitive continuity subject to correctness**. A successful name allows the learner to reuse an existing conceptual structure instead of constructing both a new concept and an arbitrary verbal label at the same time.

This note calls that method **cognitively anchored naming**.

---

## Part I — Why `material-object` is the appropriate name

### 1. The distinction that requires a name

There are two importantly different entities in the present Newtonian vocabulary.

The first is a kinematic representation: a point or trajectory through space. It answers questions about where something is and how its position changes. Considered by itself, it need not own inertial mass, mechanical composition, or a net force.

The second is the mechanically qualified individual for which those quantities and structures have addresses. It is:

- re-identifiable through time;
- represented by a trajectory;
- a bearer of inertial mass;
- an owner of a mechanical composition of acting-objects;
- a participant in interactions; and
- the entity for which a net force and inertial acceleration can be evaluated.

The required name should therefore identify more than the presence of mass. It should identify the **persisting bearer and owner** to which changing mechanical attributes belong.

### 2. Why the obvious alternatives are incomplete

| Candidate | What it gets right | What it hides or distorts |
| --- | --- | --- |
| `point-particle` | Standard modelling language; makes the point idealisation visible | Encourages identification of the mechanical individual with its geometrical representation |
| `mass-point` | Historically established; clearly distinguishes dynamics from a bare moving point | Foregrounds one scalar attribute and says little about force, interaction, composition, or ownership |
| `massive-particle` | Explicitly marks the presence of mass | *Massive* can suggest “very heavy”; still defines the entity by one property rather than by its identity-bearing role |
| `body` | Deep history in mechanics; naturally suggests a physical bearer | Can imply extension, shape, or an organism; its relation to a point idealisation must be explained |
| `object` | Activates persistence, individuation, property-bearing, interaction, and whole–part structure | Too broad without qualification; collides with abstract, grammatical, philosophical, and computational uses |
| `material-object` | Retains the intuitive object schema while restricting it to the physical branch | Still requires an explicit technical definition and careful translation across languages |

`material-object` wins because it names the type of unity involved, rather than selecting one of the unity's attributes as though that attribute constituted the whole concept.

### 3. The prelinguistic foundation

Research on infant cognition gives strong evidence that humans represent physical individuals before they possess the word *object*. Infants expect physical individuals to exhibit such properties as cohesion, boundedness, continuity, persistence, solidity, and contact-governed interaction. These expectations are not Newtonian mechanics, but they provide part of the conceptual scaffold upon which a Newtonian account can later be built.

The correspondence is close:

| Early physical expectation | Later mechanical use |
| --- | --- |
| Continuity and persistence | One entity can be tracked through changing positions and times |
| Cohesion and boundedness | There is a whole to which properties and parts belong |
| Re-identification through change | Mass and composition can remain at the same conceptual address while force and position change |
| Solidity and contact | Distinct individuals can constrain or interact with one another |
| Separate trackability | Several entities can have distinct trajectories and mechanical states |

Cross-linguistic studies strengthen the conceptual claim. English- and Japanese-speaking children distinguish complex objects from substances even though the two languages encode countability differently. The evidence therefore favours an early object–substance or individual–non-individual distinction that is not manufactured by the English word *object*.

This establishes the correct direction of dependence:

```text
prelinguistic physical individuation
    -> names for familiar kinds such as ball, cup, dog, and person
    -> general labels such as thing and object
    -> qualified technical concepts such as material-object
    -> further abstractions such as mathematical or abstract object
```

The infant does not first learn the word *object* and then learn that a ball is one. The infant can already treat the ball as one persisting individual. The later word gathers and generalises structure that was already available.

### 4. Trackability as the bridge from infant objecthood to mechanics

The table above mentions trackability, but the connection deserves to be stated as a chain. Trackability is not merely one more property that babies happen to attribute to objects. It is the operational bridge between prelinguistic objecthood and a mechanics written in trajectories.

An infant encounters a changing visual scene rather than a ready-made list of named objects. To treat one changing portion of that scene as *the same thing* requires the infant to maintain identity across changes of position, orientation, illumination, partial occlusion, and temporary disappearance. The infant's expectation that a hidden object continues to exist is therefore also an expectation that the object remains re-identifiable: what disappears behind the screen and what emerges from it belong to one continuing history unless the event supplies evidence of a split, replacement, or destruction.

At this level, objecthood is already temporal:

```text
one object
    = appearances at different times
      treated as belonging to one continuing individual
```

The VD trackability work turns that practical expectation into an explicit precondition:

```text
trackability :=
selected points of the scene can be re-identified through time,
each generating a track.
```

These two statements are not identical. Infant cognition ordinarily tracks cohesive wholes, whereas the VD tracker can begin with selected feature-points before any body has been identified. Infant experiments establish expectations about persistence and continuity; they do not establish the VD's particular tracker, tolerance, or lumping procedure. The relationship is one of **formal refinement**: the VD extracts the re-identification structure implicit in ordinary object cognition and makes its observational commitments inspectable.

This refinement corrects an easy circularity. We should not begin by saying, “an object supplies a family of tracks,” because that assumes the object whose identity the tracks are supposed to establish. The cleaner order is:

```text
changing material scene
    -> re-identifiable feature-tracks
    -> redundant tracks grouped within a working tolerance
    -> one bundle or lump
    -> one material-object/body is licensed
    -> one representative particle carries the bundle's motion
    -> r(t) is the mathematical carrier of that representative track
```

In this order, a body is not primitively handed to the theory. It is an output of successful re-identification and lumping. The infant performs a fast, pre-formal version of this achievement when it treats changing appearances as one continuing thing. The VD slows the achievement down and separates its ingredients: scene, seeds, tracks, tolerance, redundancy, bundle, representative, and possible defeat.

This also shows why a `material-object` is not identical to a `point-particle` or to a trajectory:

| Level | Role |
| --- | --- |
| Material scene | What is presented for observation before individuals have been fixed |
| Track | A time-indexed record produced by re-identifying a selected feature |
| Bundle or lump | A family of tracks judged redundant within tolerance over an interval |
| Material-object/body | The material individual licensed by the lumping judgment |
| Point-particle | The representative track-carrier used in the mechanical model |
| Trajectory `r(t)` | The mathematical representation of that carrier's position through time |

The distinction is educationally important. A trajectory records the motion of an identity; it does not by itself create or explain that identity. A point-particle represents a lump; it is not a miniature material body. The `material-object` is the identity-bearing target for which the representation is being used.

#### Trackability creates the address; dynamics supplies the value

The mass pipeline makes the consequence especially clear. Before “the mass of this object” can receive a numerical answer, *this object* must have a referent. Trackability supplies candidate histories, and lumping judges which histories count together as one target. The result is an identity stable enough to own a ledger entry:

```text
trackability       supplies continuing histories
lumping            fixes WHICH continuing thing is the target
mass address       becomes available for that target
dynamics           binds HOW MUCH mass to the address
no offshoot tracks help certify that the binding still applies
```

Thus trackability does not determine the magnitude of inertial mass. Any observed track can be reconciled with different masses if the force is allowed to vary. Trackability instead performs the logically prior work of fixing and escorting the **bearer** of the mass value.

The same reasoning applies to force and composition. A net-force value can change from moment to moment, and acting-objects can be added, removed, activated, or defeated. Those changes are intelligible only because they are changes *of the same continuing material-object*. Trackability supplies the temporal spine along which those changing mechanical commitments are attached.

#### Defeat reveals what the intuition commits us to

Ordinary object cognition is defeasible. If a ball splatters, a block breaks, or one part develops an offshoot track, the old one-object interpretation may cease to be usable. The VD makes this revisability explicit. Lumping is interval-relative and tolerance-relative; a later event can show retrospectively that what was treated as one target must now be represented as several.

This is not a defect in the bridge. It is part of its fidelity to ordinary cognition. Babies and adults do not merely assume eternal identity; they maintain identity under expected transformations and revise it when continuity, cohesion, or common motion fails. A mechanical identity should behave similarly: stable enough to support prediction, but capable of expiring when the observational evidence for the lump breaks.

The deepest naming argument can therefore be restated:

> `material-object` is appropriate because it names the continuing individual produced by re-identification and lumping—the entity stable enough to own trajectory, mass, composition, and force—whereas `point-particle` names its reduced representative and `trajectory` names the representative's time-indexed motion.

Trackability is what prevents “object” from being a merely warm or familiar word. It identifies the exact inherited intuition that the formal mechanics reuses.

### 5. Why *object* still matters

The fact that *object* is not a universal nursery word does not make it a poor technical name. It changes the justification for using it.

In contemporary English, the ordinary physical sense of *object* commonly evokes a separately identifiable thing that can persist, move, possess properties, have parts, and participate in events. These are precisely the intuitions that a learner should carry into the mechanical concept. The technical definition then enriches this ordinary schema with inertial mass, trajectory, net force, and mechanical composition.

The relation is therefore not:

```text
ordinary word = complete scientific definition
```

It is:

```text
ordinary object schema
    + explicit mechanical qualifications
    = material-object
```

The familiar schema supplies the unity. Newtonian theory supplies the mechanical commitments.

### 6. Why the modifier *material* is essential

The word *object* has travelled through philosophy, grammar, mathematics, psychology, and computing. Its learned history derives from Medieval Latin *objectum*: roughly, something placed before perception, thought, desire, or action. This history explains expressions such as *object of thought*, *object of desire*, and *grammatical object*. It also explains why the word can name physical and non-physical entities.

Bare `object` would consequently be underconstrained in the VD. `material-object` performs a useful act of controlled qualification:

- `object` contributes identity, persistence, property-bearing, and whole–part unity;
- `material` selects the physically situated branch;
- the VD definition adds the specifically Newtonian slots and laws.

This also protects the relation to `abstract-object`. The claim need not be that the historical phrase *abstract object* was literally derived from Newtonian mechanics. The more defensible claim is conceptual: abstract objecthood preserves and generalises such structures as unity, identity, re-identification, property-bearing, and composition while removing or relaxing material embodiment.

The material object is therefore a powerful **cognitive paradigm** of objecthood even if the international word *object* has a more complicated scholarly history.

### 7. Composition completes the argument

The VD composition discovery showed that the particle—or, under the proposed terminology, the material-object—owns its acting-objects. This is not merely a set-membership convenience. It is a whole–part relation:

- the material-object is the persisting whole;
- acting-objects are its force-producing components;
- inertial mass characterises its passive response to force;
- mechanical composition characterises its active contribution to interactions.

An identity-bearing whole is conceptually prior to ownership. Before one can say that something *has* components, one must be able to treat it as the same whole across the relevant description. `material-object` naturally supplies that owner. `massive-particle` does not express this role nearly as well.

### 8. The naming decision

The resulting recommendation is:

> **`material-object`** — A persistent, trackable physical individual represented in Newtonian mechanics as having a trajectory, an inertial mass, a mechanical composition, and a net force.

The exact VD definition may need to distinguish permanent attributes, time-indexed values, and relations to a reference frame. The name does not replace that formal work. Its role is to ensure that, when the definition is given, the learner begins from the right kind of mental unity.

Within an established Newtonian context, *object* may be used as an economical short form. The dictionary headword should remain `material-object` because it carries its own disambiguation.

---

## Part II — Generalising the argument into a naming schema

### 9. The general principle

Every technical name creates a mapping between two structures:

1. the formal structure intended by the theory; and
2. the conceptual structure activated in the learner by the name.

A name is educationally strong when these structures overlap in the relations that matter. A name is weak when it activates no useful prior structure, or when it activates a familiar structure containing misleading relations.

The ideal is therefore not “always use an ordinary word.” It is:

> Choose the most cognitively available name whose inherited structure is substantially isomorphic to the formal concept; then add the smallest qualification needed to remove important false entailments.

This can be represented as a constrained optimisation:

```text
best-name(concept) =
    maximise(
        cognitive availability
      + structural fit
      + explanatory generativity
      + continuity with neighbouring names
    )
    while minimising(
        misleading entailments
      + lexical collision
      + arbitrary novelty
      + translation fragility
    )
    subject to formal correctness.
```

Formal correctness is a constraint, not one desirable factor among others. No increase in familiarity compensates for a name that systematically teaches the wrong structure.

### 10. The cognitively anchored naming procedure

#### Step 1 — Determine the formal invariants

Write down what must remain true of the concept across all its legitimate applications. Do this before choosing a name.

For `material-object`, the relevant invariants include persistent identity, trackability, property-bearing, mechanical ownership, and participation in force evaluation. “Has a nonzero mass” is insufficient because it does not capture the whole role.

#### Step 2 — Identify candidate prior schemas

Ask what learners already know that has the same relational shape. Sources can include:

- early physical cognition;
- bodily and spatial experience;
- ordinary whole–part reasoning;
- familiar artifacts and activities;
- existing concepts learned earlier in the curriculum; and
- structurally equivalent concepts in other disciplines.

This step searches for a reusable conceptual structure, not merely a familiar sound.

#### Step 3 — Compare structures, not dictionary glosses

For each candidate name, map the relations it normally evokes against the formal relations.

Questions include:

- Does the familiar concept have the right kind of identity?
- Does it persist through the right changes?
- Can it bear the relevant properties?
- Does it own parts, or is it itself only a part or representation?
- Does it participate in the right causal relations?
- Which ordinary implications would become misconceptions?

This is the step by which `object` outperformed `massive-particle`: the former activates the bearer-and-owner structure, whereas the latter mostly advertises a single attribute.

#### Step 4 — Choose a familiar root and a precision-bearing modifier

If the best familiar root is too broad, preserve it and qualify it compositionally.

Examples of the pattern are:

```text
object -> material-object
composition -> mechanical-composition
frame -> reference-frame
mass -> inertial-mass
force -> net-force
```

The root provides cognitive continuity. The modifier records the formal restriction. A transparent compound is often preferable to a completely novel word because the learner can recover part of its meaning from its components.

#### Step 5 — State the retained and rejected intuitions

A definition should say not only what the term means, but which ordinary implications survive technicalisation.

For example:

```text
Retain from object:
    one persisting identity;
    a bearer of properties;
    an owner of components;
    a participant in interactions.

Do not automatically retain:
    visible extension;
    rigidity;
    being human-made;
    being directly perceptible;
    being large enough to handle.
```

This makes conceptual change explicit instead of leaving the learner to guess where the ordinary and technical meanings diverge.

#### Step 6 — Build a coherent name family

Names should help reveal the dependency graph. Related terms should display their relationship where possible:

- `object`, `material-object`, and `abstract-object`;
- `force`, `acting-force`, `reaction-force`, and `net-force`;
- `mass`, `inertial-mass`, and any distinct mass concepts introduced later.

A coherent family makes definitions partially visible in the vocabulary. An arbitrary collection of unrelated labels hides the theory's structure and increases memorisation load.

#### Step 7 — Check the name across languages and learner groups

The English word should not be mistaken for the universal concept. Translation must preserve the formal–intuitive mapping rather than the surface word. In another language, the most appropriate equivalent of `material-object` might literally resemble *physical thing*, *body*, or *material individual*.

The schema therefore requires two distinct questions:

1. What is the invariant concept?
2. Which expression in this learner's language best anchors that concept?

The ideal international vocabulary may preserve a stable formal identifier while allowing carefully selected pedagogical display names in different languages.

#### Step 8 — Test rather than merely admire the name

The proposed name should be treated as an educational hypothesis. Candidate names can be compared using:

- initial interpretation before a definition is shown;
- accuracy immediately after instruction;
- ability to distinguish the concept from neighbouring concepts;
- delayed retention;
- transfer to unfamiliar problems;
- frequency and type of misconceptions;
- time required to follow a definition or VD trace; and
- ability to reconstruct the concept from the name and its family.

For the present case, learners could be randomly introduced to `mass-point`, `massive-particle`, `body`, or `material-object`, with identical definitions. Their subsequent explanations would reveal which name best preserves identity, ownership, representation, mass, and force without importing damaging assumptions.

---

### 11. Why this may improve educational success

The proposed schema connects to several established findings in learning science.

#### Prior knowledge determines what new information can attach to

New knowledge is not stored in an empty system. Learners interpret it through prior knowledge, and the quality of that prior knowledge predicts later achievement. A structurally appropriate name can act as a retrieval cue for the right prior schema. An opaque name cannot; a misleading familiar name retrieves the wrong one.

#### Naming can reduce simultaneous processing demands

Before learners can understand a complex causal system, they must identify its parts and know what those parts are. Research on pre-training finds that instruction is more effective when learners first know the names and characteristics of the main components. A well-designed vocabulary performs some of that pre-training continuously: the names themselves remind learners what kind of components they are manipulating.

#### Concrete-to-abstract continuity can support transfer

Research on *concreteness fading* investigates instruction that begins with meaningful concrete representations and progressively moves toward idealised and abstract ones. Cognitively anchored naming applies a related principle to vocabulary. It allows an abstract formal structure to remain connected to a concrete or familiar source schema while its technical restrictions are gradually made explicit.

The sequence becomes:

```text
familiar experience
    -> ordinary concept
    -> qualified technical name
    -> formal definition
    -> symbolic or computational use
```

#### Coherent names externalise part of the theory

If names preserve genuine structural relationships, vocabulary becomes a low-resolution map of the theory. The learner does not have to remember every dependency as an unrelated fact. The distinction between `force`, `net-force`, and `reaction-force`, for example, is partly carried by the names themselves.

#### Better normalisation becomes possible

In the VD, a natural-language question must be normalised to a headword before the dictionary can expand it. A cognitively anchored headword should be easier to select because its name advertises the conceptual role being requested. Better names may therefore improve not only recall but also the accuracy of question normalisation and the legibility of answer traces.

These mechanisms make improved educational success plausible, but they do not make it automatic. The proposal is a research programme: improve names, predict the resulting learning advantages, and test those predictions.

---

### 12. Failure modes and boundary conditions

#### Familiarity without structural fit

An everyday word can be dangerously intuitive. Physics already contains familiar words whose technical meanings diverge from ordinary usage: *work*, *power*, *energy*, *momentum*, and *weight*. Such terms can encourage confident misconceptions precisely because they feel understood.

The schema therefore penalises **misleading entailments**, not unfamiliarity alone. Sometimes a new or visibly technical name is better than a familiar false friend.

#### Excessive qualification

Modifiers can improve precision until they make a term unprocessable. A long name that attempts to encode the entire definition ceases to function as a name. The aim is the smallest modifier that selects the intended branch; the definition and dependency graph carry the remaining detail.

#### Premature abstraction

A name can be formally elegant yet educationally sterile if it is introduced before the learner has any experience to which it can attach. The same name may be excellent for an expert and poor for a novice. Naming should therefore be indexed to curricular order as well as theoretical structure.

#### Prototype exclusion

The prototype activated by a familiar word may be narrower than the formal extension. English *object* often suggests an inanimate, medium-sized, manipulable thing. A Newtonian material-object may represent a planet, grain of dust, person, or other system. Instruction must explicitly extend beyond the prototype without losing the prototype's useful structure.

#### Mistaking English for cognition itself

The infant concept of a physical individual transcends English; the word *object* does not. A translation that preserves the spelling or etymology but loses the intuitive mapping violates the schema. Cross-linguistic implementation must optimise the mapping again in each language.

---

### 13. Implications for the VD

The VD already requires every operative concept to receive a headword. That makes it unusually sensitive to naming quality. In ordinary exposition, a poor name can sometimes be repaired by surrounding prose. In a dictionary-like theory, the headword is repeatedly used for normalisation, lookup, expansion, tracing, and comparison. Its cognitive effects compound.

Cognitively anchored naming could therefore become an explicit VD design criterion:

> A VD headword should expose the deepest reusable intuitive structure compatible with its formal role, while its modifiers and definition should remove the intuitive structure's invalid extensions.

For every proposed headword, an authoring sheet could record:

| Field | Question |
| --- | --- |
| Formal role | What does this concept do in the dependency graph? |
| Prior anchor | What familiar or earlier concept has the same relational structure? |
| Retained intuitions | Which parts of the prior concept remain valid? |
| Rejected intuitions | Which ordinary implications would be false? |
| Required modifier | What is the smallest qualification that selects the intended sense? |
| Neighbouring names | Does the term form a legible family with its dependencies and contrasts? |
| Translation note | Must another language choose a different lexical anchor? |
| Educational prediction | What should learners understand or remember better because of this name? |
| Evaluation | How will that prediction be tested? |

This would turn naming from an aesthetic afterthought into a constrained part of theory engineering.

---

### 14. Compact formulation

The entire argument can be condensed into four claims.

1. A technical concept needs a name for its organising unity, not merely for one conspicuous attribute.
2. The best familiar name is the one whose inherited conceptual relations most closely match the formal relations.
3. A modifier should remove the important mismatches while preserving the useful prior structure.
4. The resulting name is an educational hypothesis whose value should be measured through comprehension, retention, discrimination, and transfer.

Applied to the present case:

```text
organising unity: persistent physical bearer and owner
best prior schema: object
necessary restriction: material
result: material-object
```

Generalised:

```text
formal invariant
    + structurally matched prior schema
    + minimal disambiguating qualification
    = cognitively anchored technical name
```

The educational ambition is not to eliminate abstraction. It is to give abstraction a continuous path from what the learner already knows.

---

## Sources and related project notes

### Project notes

- *Composition: A Newtonian Word* — establishes mechanical composition as an ordinary whole–part structure and the material individual as owner of acting-objects.
- *VD Dictionary — Answering Textbook Questions* — establishes normalisation from natural-language questions to headwords and recursive dictionary expansion.
- *From Scene to Particles: Trackability, Redundancy, and the Lumping Criterion* — establishes trackability as the precondition of trajectory mechanics and bodies as outputs of tracking and lumping.
- *The Point-Particle Bridge: Spine Note* — distinguishes the material target from the representative particle and locates trackability and lumping before mass assignment.
- *The Mass Pipeline: How the Right Mass Enters F = ma* — establishes that lumping fixes which continuing thing owns the mass address, dynamics binds its value, and the absence of offshoot tracks escorts that binding through time.
- *VD Newton v0.5 Dependency Graph* — displays the current dependency structure from which the naming problem emerged.

### Development, language, and cognition

- Elizabeth Spelke, [*Core Knowledge of Objects*](https://www.harvardlds.org/wp-content/uploads/2017/01/spelke2000-1.pdf).
- Mutsumi Imai and Dedre Gentner, [*A cross-linguistic study of early word meaning: universal ontology and linguistic influence*](https://www.sciencedirect.com/science/article/abs/pii/S0010027796007846).
- Lance Rips and Susan Hespos, [*Concepts of objects and substances in language*](https://link.springer.com/article/10.3758/s13423-019-01613-w).
- Marc Bornstein and Martha Arterberry, [*The development of object categorization in young children: hierarchical inclusiveness, age, perceptual attribute, and group versus individual analyses*](https://pmc.ncbi.nlm.nih.gov/articles/PMC2856652/).
- Anna Wierzbicka, [*“Semantic Primitives”, fifty years later*](https://journals.rudn.ru/linguistics/article/view/26795).

### Learning and terminology

- Telle Hailikari, Nina Katajavuori, and Sari Lindblom-Ylänne, [*The relevance of prior knowledge in learning and instructional design*](https://pmc.ncbi.nlm.nih.gov/articles/PMC2630138/).
- Richard Mayer, [*Pre-training Principle*](https://www.cambridge.org/core/books/multimedia-learning/pretraining-principle/01791D57F5D4164251269E6DF56A8BF1).
- Emily Fyfe and colleagues, [*Concreteness fading in mathematics and science instruction: a systematic review*](https://link.springer.com/article/10.1007/s10648-014-9249-3).
- Tiina Kokkonen and colleagues, [*Concreteness fading in learning secondary school physics concepts*](https://www.sciencedirect.com/science/article/pii/S0959475221000839).
- Jennifer Kaplan and colleagues, [*Exploiting lexical ambiguity to help students understand the meaning of random*](https://iase-pub.org/ojs/SERJ/article/view/296/196).
- Jenna Zukswert and colleagues, [*Identifying troublesome jargon in biology*](https://pmc.ncbi.nlm.nih.gov/articles/PMC6757220/).
