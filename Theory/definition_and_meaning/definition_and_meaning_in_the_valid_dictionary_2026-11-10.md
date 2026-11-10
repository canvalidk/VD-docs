# Definition and meaning in the Valid Dictionary

Status: first version, 10 November 2026. Assembled by Claude with Can Valid from the December 2025 first-draft notes and the worked examples of 10 November 2026. Not yet tested on a cold reader. Open points are listed in the catalog note for this file.

## The rule

A person who wants to leave sees an exit sign and walks toward it.

The meaning of the sign is that: it makes people think the exit is that way, and it makes people who want to leave go that way. The meaning is not the sentence "the exit is that way", and it does not depend on whether the exit is there.

So every utterance has two arrows.

- **Meaning** runs from the utterance to the people who notice it. It is what the utterance makes them do and think.
- **Accuracy** runs from the utterance to the world. It is whether things are as the utterance says.

The two are separate. Bolt the door shut and the sign's meaning is unchanged. The Valid Dictionary is built on keeping them apart.

## The terms

Three terms are used below. Each shares a name with an ordinary word. Each is a technical term, not a claim about what the ordinary word really means.

- **Authority Dictionary.** A named list of entries that can be written out exactly. Each entry is a pair, a headword and a string, with nothing ambiguous in it. Entries are added and never changed. Nobody has to have written the list down. Convention is one, and its name is "convention". Every statement made with the dictionary carries "according to this dictionary".
- **valid_definition.** According to a named Authority Dictionary, the valid_definition of a word is the string that dictionary returns for it. Two valid_definitions are the same only if every character matches.
- **valid_meaning.** The total change in the relevant state of the world caused by the utterance of a word in a given context. It is an effect, not a string, and it is never stored in the dictionary.

From here on, "definition" is short for valid_definition according to a named Authority Dictionary, and "meaning" is short for valid_meaning. This document is the authority for both.

A definition can be looked up. A meaning has to be observed.

## The square

Cross the two terms with themselves and you get four questions. The square is a table of contents. It says where each example below belongs.

| Cell | The question it holds | Examples |
| --- | --- | --- |
| DoD (Definition of Definition) | What is a valid_definition? | 3, 5, 6 |
| DoM (Definition of Meaning) | What does a string do when it is uttered? | 1, 2, 4 |
| MoM (Meaning of Meaning) | When do two utterances do the same thing? | 3, 5 |
| MoD (Meaning of Definition) | When may a short string stand in for a meaning? | 5, 6 |

Read the cells in that order.

## Worked examples

### 1. An exit sign (DoM)

A person who wants to leave sees the sign and walks toward it. Nobody looks anything up. The sign works on people who never learned a definition of "exit". Part of its effect comes from context: the same sign in a shop window, for sale, sends nobody anywhere. Strangers leave by the same door because the sign has much the same effect on each of them. The world reaches the meaning only through readers. If the door is bolted, the meaning changes only when people find out.

### 2. "Don't think about elephants" (DoM)

The string says to refrain. The utterance makes people think of elephants. Reading the word "elephants" is already the thought, so the effect has happened before the instruction can be followed. "Don't" changes what the string says. It does not change what "elephants" does. The only hearer who complies is the one who did not notice the utterance. A speaker who wants a result picks the sentence by its effect, and someone writing a dictionary entry should do the same.

### 3. "5 + 3" (DoD, MoM)

Shown to a trained person, "5 + 3" makes them produce "8". The strings "5 + 3" and "8" differ character by character, so by the dictionary's test they are not the same. What they share is an effect. An adult recalls the answer, a child counts on fingers, a calculator runs a circuit, and all three end at "8". Here the two arrows agree, and they agree because people were trained until they did. A person who produces "9" shows what the string did to them. Calling it wrong is a separate judgement, made against an authority.

### 4. "35 × 78" (DoM)

Most people have no stored response to this string. It starts a chain: a run of small utterances to yourself, with paper holding the state between steps. Asked what multiplication is, people say repeated addition, yet nobody adds 35 seventy-eight times. What they say multiplication is, and the procedure they run, are different things. The string triggers a trained procedure, and longer chains misfire more often. Writing the chain down is what lets someone else find the step that failed.

### 5. "35 × 78 = 2730" (MoM, MoD, DoD)

The meaning of "35 × 78" is not 2730. It is the computing the string sets off. The equation offers a swap. A reader who trusts it stops computing and carries "2730" forward. A reader who checks it runs the left side and compares the result with the right side, character by character. So "=" makes a claim: a trained reader who runs both sides ends at the same string. A false equation makes a trusting reader swap just the same. Only the check tells the two apart.

### 6. "a" for acceleration (MoD, DoD)

Alone, the mark "a" does nothing fixed. In "a cat" it is an article. Under "F = ma", beside the line "where a is the acceleration", it makes the reader produce "acceleration". That line is an entry: headword "a", string "acceleration", authority this page. With no such line the reader still expands it, according to convention, and the convention of another field gives another string. Shorthand keeps chains short, and short chains misfire less. The cost is that a short mark is always vague. The writer hopes it triggers the entry they have in mind. The reader guesses from context which entry that is, and the guess can be wrong. Copied to another board, "a" gets whatever expansion the reader's training supplies. The entry is exact. Getting to it is not.

## Misreadings to expect

1. **Reading valid_definition as a statement of what a thing is.** It is only the string a named dictionary returns. The question "But is that what a definition really is?" has no target, because no definition of "definition" was offered.
2. **Stating a meaning as a sentence.** "The sign means the exit is that way" is the mistake. Say what the utterance makes people do and think.
3. **Taking a formula for the law.** "F = ma" is a string. It can carry Newton's second law for a reader trained to expand it. Teaching the string as the law hands over the mark without the training.

## Where it goes next

This document stops before physical law. The two terms are the groundwork for the Valid Dictionary's definition of a law, which is argued elsewhere. The paths below are in the VD-docs repository.

- Why a law is three mutually defined entries: `Theory/triplet_as_admission_event/why_the_triplet_rule_is_needed_d2.md` and `Core/VD_LAW_HOUSE_FOUNDATION.md`
- How the training is installed, and what survives across readers: `Theory/handle_residue_derivation/handle_derivation_note_rewritten.md`
- Why every swap is a hypothesis: `Theory/nobody_made_a_mistake/nobody_made_a_mistake_meaningful_substitutions.md`
- How a dictionary answers a question by expanding entries: `Core/vd_dictionary_question_answering.md`
- Source for this document: `Core/Current development/VD__how_to draft1.1.pdf`, sections 1 to 7

## Two exercises

Analyse each one as the examples were analysed. What string was uttered? What does it make people do and think? According to which authority? Where do the two arrows come apart?

1. "He is such a sssssalesman."
2. "E = mc²", printed on a T-shirt.
