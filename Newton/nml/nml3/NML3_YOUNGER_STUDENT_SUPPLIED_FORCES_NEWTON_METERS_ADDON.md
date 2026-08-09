# NML3 Younger-Student Add-On: Supplied Force Accounts and Newton Meters

**Status:** mock lesson add-on  
**Project:** VD Newton / NML3  
**Purpose:** extend the younger-student NML3 mock lesson with problem formats that supply force values directly, allowing students to practise force addition without yet opening the later acting-object machinery.

---

## 0. Core Teaching Opportunity

NML3 creates a new kind of classroom problem that was difficult to use safely in NML2.1.

Earlier, a student might be told:

> A newton meter reads 8 N.

But that does **not** by itself establish that the net force on the object is 8 N. The meter supplies the value of one force contribution. Other force contributions may also act on the object.

NML3 gives students enough force-accounting structure to say:

> **A measured or supplied force is one force in the object's force account. The net force is obtained by adding all of the forces in that account.**

This allows introductory problems to skip the difficult question of how a physical interaction is identified and converted into a force contribution.

The problem can simply **supply the forces**.

The student then performs the NML3 operation:

```text
supplied force account
    -> add the force vectors
    -> net force
```

The later acting-object lessons will ask the harder question:

```text
physical scene
    -> identify relevant interactions
    -> establish force contributions
    -> construct the force account
```

NML3 does not need to solve that problem yet.

---

# Part I — Three Useful Ways to Supply Force Information

## 1. Force values supplied directly

The cleanest NML3 problem simply gives the force vectors.

Example:

> Three forces act on a box:
>
> - 10 N right
> - 15 N right
> - 5 N left
>
> What is the net force?

The student is **not** being asked to determine where the forces came from.

The force account has already been supplied:

```text
10 N right
15 N right
5 N left
```

The student's job is:

```text
add the supplied force vectors
```

so:

$$
F_{\text{net}}
=
10 + 15 - 5
=
20\text{ N right}.
$$

### Teaching purpose

This problem isolates the force-sum skill.

It teaches:

```text
several force values
    -> one resultant
```

without requiring:

```text
acting-object identification
activation conditions
force laws
action-reaction classification
```

---

## 2. A story supplies already-identified forces

A second class of problem gives an intuitive physical story but still supplies the force values explicitly.

Example:

> Three students push a box.
>
> - Aisha pushes with 10 N to the right.
> - Ben pushes with 15 N to the right.
> - Carla pushes with 5 N to the left.
>
> What is the net force on the box?

Again, the student does not need to establish whether each student-object interaction really produces a force or calculate the force from another law.

The problem has already supplied three force contributions.

The student writes:

$$
F_{\text{net}}
=
10 + 15 - 5
=
20\text{ N right}.
$$

### Why this format is useful

The story gives each force an intuitive identity.

The learner can point to three different contributions:

```text
Aisha's push
Ben's push
Carla's push
```

while the numerical operation remains simple.

This format also prepares the later idea that two forces may have the same numerical vector without becoming the same physical force.

For example:

> Aisha pushes 5 N right.
>
> Ben pushes 5 N right.

There are still two supplied force contributions even though their vector values are equal.

The force account contains two contributions, and their net contribution is:

$$
5 + 5 = 10\text{ N right}.
$$

---

## 3. A newton meter supplies one force value

A newton meter can now be introduced carefully.

Student-facing meaning:

> **A newton meter measures the force transmitted through the meter.**

It therefore supplies one force value for the force account.

It does **not** automatically supply the net force.

### Clean one-force case

> A newton meter pulls a cart with a reading of 8 N to the right.
>
> In this question, this is the only force in the cart's force account.
>
> What is the net force?

Because the supplied account has one member:

```text
8 N right
```

the net force is:

$$
F_{\text{net}}=8\text{ N right}.
$$

This is the easiest case in which a newton-meter reading equals the net force.

### Two-force case

> A newton meter pulls a cart with 8 N to the right.
>
> A student pushes the cart with 3 N to the left.
>
> What is the net force?

The force account is:

```text
8 N right
3 N left
```

therefore:

$$
F_{\text{net}}
=
8-3
=
5\text{ N right}.
$$

The meter still reads 8 N.

The net force is 5 N right.

The two quantities are not the same.

### Insufficient-information case

> A newton meter attached to a cart reads 8 N to the right.
>
> What is the net force on the cart?

Expected answer:

> **Not enough information has been supplied about the rest of the force account.**

The meter has supplied one force contribution.

It has not established that no other contributions exist.

This is an important NML3 question because refusing to equate the meter reading with net force is itself successful force-accounting.

---

# Part II — A Newton-Meter Progression

## 4. Stage 1 — One meter, one supplied force

Start with problems in which the question explicitly says that the meter force is the only force in the account.

Example:

> The only force acting on a trolley in this simplified model is a 6 N pull measured by a newton meter to the right.
>
> Find the net force.

Answer:

$$
F_{\text{net}}=6\text{ N right}.
$$

Student handle:

```text
one force in the account
-> net force is that force
```

---

## 5. Stage 2 — Meter plus another force

Example:

> A newton meter pulls 10 N right.
>
> Another supplied force is 4 N left.
>
> Find the net force.

Answer:

$$
F_{\text{net}}
=
10-4
=
6\text{ N right}.
$$

Student handle:

```text
meter reading
is one force
not automatically the resultant
```

---

## 6. Stage 3 — Meter reading equals net force by cancellation

Once students understand cancellation, use a more subtle case.

> A newton meter pulls 6 N right.
>
> Two other forces act:
>
> - 3 N right
> - 3 N left
>
> What is the net force?

The total is:

$$
F_{\text{net}}
=
6+3-3
=
6\text{ N right}.
$$

The net force happens to equal the meter reading.

But the meter was **not** the only force in the account.

This gives an important distinction:

```text
meter reading = net-force value
```

does not imply:

```text
meter force = only force present
```

Numerical equality does not reveal the contents of the force account.

This prepares the deeper NML3 ending.

---

# Part III — Core Problem Bank

## 7. Same-direction addition

### Problem A

> Three students push a crate to the right with forces of:
>
> - 10 N
> - 15 N
> - 5 N
>
> Find the net force.

$$
F_{\text{net}}
=
10+15+5
=
30\text{ N right}.
$$

### Problem B

> Four supplied forces act upward:
>
> - 2 N
> - 4 N
> - 3 N
> - 1 N
>
> Find the net force.

$$
F_{\text{net}}
=
10\text{ N upward}.
$$

Teaching target:

```text
forces in the same direction add
```

---

## 8. Opposing forces

### Problem A

> One student pushes a box 12 N right.
>
> Another pushes 5 N left.
>
> Find the net force.

$$
F_{\text{net}}
=
7\text{ N right}.
$$

### Problem B

> A rope pulls 9 N left.
>
> A second supplied force pushes 14 N right.
>
> Find the net force.

$$
F_{\text{net}}
=
5\text{ N right}.
$$

Teaching target:

```text
choose a direction convention
add signed force values
return both magnitude and direction
```

---

## 9. Balanced force accounts

### Problem A

> Two supplied forces act on a box:
>
> - 10 N right
> - 10 N left
>
> Find the net force.

$$
F_{\text{net}}=0.
$$

Then ask:

> How many force contributions were supplied?

Answer:

```text
two
```

Then ask:

> Did the forces disappear because the net force is zero?

Answer:

```text
no
```

### Core lesson

```text
two nonzero forces
can sum to
zero net force
```

Therefore:

```text
zero net force
does not mean
no forces in the account
```

This should be one of the central NML3 examples.

---

## 10. More than two forces cancelling

Example:

> Four supplied forces act on an object:
>
> - 10 N right
> - 5 N right
> - 8 N left
> - 7 N left
>
> Find the net force.

$$
F_{\text{net}}
=
10+5-8-7
=
0.
$$

Ask:

> Is the force account empty?

Expected answer:

> No. Four nonzero force contributions were supplied.

This prepares students for the idea that cancellation may involve several members, not merely one obvious opposing pair.

---

# Part IV — Two-Dimensional Force Addition

## 11. Perpendicular supplied forces

Once students are ready for vector addition in two dimensions:

> A box has two supplied forces:
>
> - 3 N right
> - 4 N upward
>
> Find the net force.

The resultant is:

$$
\mathbf F_{\text{net}}
=
(3,4)\text{ N}.
$$

Its magnitude is:

$$
|\mathbf F_{\text{net}}|
=
5\text{ N}.
$$

The important conceptual point remains unchanged:

```text
the vectors being added
were supplied as members of the force account first
```

The geometric or component method comes second.

---

## 12. Components are not automatically separate forces

This distinction should be introduced carefully once students decompose vectors into components.

Suppose one force is:

$$
\mathbf F=(3,4)\text{ N}.
$$

It can be written:

$$
\mathbf F
=
(3,0)\text{ N}
+
(0,4)\text{ N}.
$$

This does **not** mean that two physical forces have been discovered.

It is one force vector represented using two components.

Student-facing rule:

> **Breaking one force arrow into horizontal and vertical parts is a mathematical decomposition. It does not automatically create two forces in the physical force account.**

This provides an excellent bridge to the end of the lesson.

---

# Part V — The Distinctive NML3 Ending

## 13. One net-force vector can be decomposed many ways

Suppose:

$$
\mathbf F_{\text{net}}
=
10\text{ N right}.
$$

Mathematically, we may write:

$$
10
=
10,
$$

or:

$$
10
=
5+5,
$$

or:

$$
10
=
7+3,
$$

or:

$$
10
=
20-10,
$$

or:

$$
10
=
100-90.
$$

All of these are correct arithmetic decompositions of the same resultant.

But they do not describe the same physical situation.

The equation:

$$
10=5+5
$$

does not prove that two 5 N forces acted.

The equation:

$$
10=20-10
$$

does not prove that one 20 N force and one opposing 10 N force acted.

The resultant alone does not tell us which force contributions belong in the physical account.

---

## 14. The force account represents the interactions being modelled

The younger-student formulation can be:

> **A force account is the collection of force contributions that represents the interactions acting on the object in the physical situation being modelled.**

The important order is:

```text
physical situation
    -> forces belonging to the account
    -> add their vectors
    -> net force
```

not:

```text
net-force vector
    -> invent any convenient decomposition
    -> call those pieces physical forces
```

Short classroom rule:

> **Find the forces first. Add them second.**

Or:

> **The sum tells us the resultant. It does not tell us the story that produced it.**

---

## 15. Same resultant, different physical accounts

Give students several stories that produce the same net force.

### Story A

```text
one supplied force:
10 N right
```

### Story B

```text
two supplied forces:
15 N right
5 N left
```

### Story C

```text
three supplied forces:
6 N right
6 N right
2 N left
```

All produce:

$$
F_{\text{net}}=10\text{ N right}.
$$

Ask:

> Are these the same force account?

Expected answer:

> No.

Ask:

> Do they have the same net force?

Expected answer:

> Yes.

The installed distinction is:

```text
same resultant
does not mean
same force account
```

---

## 16. The inverse question fails

Present:

> The net force on an object is 10 N right.
>
> List all the forces acting on it.

Expected answer:

> **The net-force value alone is not enough information.**

Students may propose possible decompositions, but they must distinguish:

```text
a mathematically possible decomposition
```

from:

```text
the force account of the actual situation
```

Teacher line:

> “You can invent infinitely many sums that give 10 N. That does not tell you which interactions the object is actually experiencing.”

This is the younger-student doorway into the deeper NML3 force-account problem.

---

# Part VI — Question Formats That Deliberately Skip Acting-Object Machinery

## 17. Fully supplied account questions

Use wording such as:

> The following forces act on the object...

or:

> In this model, the object's force account contains...

or, for younger students:

> These are the forces on the object...

Then list the force vectors.

The student is entitled to use the supplied list.

---

## 18. Supplied-story questions

Use wording such as:

> Three students push the box. Their forces are...

> Two ropes pull the sled with...

> A fan pushes with... while a student pushes with...

The identities of the contributors are intuitively visible, but the force values are supplied.

The student is **not** being asked to derive those values or prove that those interactions produce forces.

---

## 19. Measurement-supplied questions

Use wording such as:

> A newton meter measures a 7 N pull to the right.

Then explicitly state the rest of the account, or ask whether enough information has been supplied.

This allows three outcomes:

```text
meter force is the only supplied force
    -> net force follows directly

other supplied forces exist
    -> add them all

rest of force account is unspecified
    -> net force not determined
```

---

# Part VII — Teacher Boundary Notes

## 20. What is being skipped

These problem formats deliberately bypass later questions such as:

```text
Why does this interaction count as a force?
Which acting object produced it?
What activation condition applies?
Which force law determines its magnitude?
Is this the action or reaction member?
How was the force account shown to be complete?
```

Those are not mistakes or omissions inside the exercise.

They are **supplied inputs**.

NML3 can say:

> “For this problem, these are the force contributions to use.”

Later lessons investigate how such a list is earned from the physical scene.

---

## 21. Do not let supplied-force problems silently become universal methodology

Students should not leave with:

> “Whenever I see a physics situation, I can simply guess a list of forces.”

The lesson should explicitly distinguish:

```text
THIS PROBLEM SUPPLIES THE FORCE ACCOUNT
```

from:

```text
THE PHYSICAL WORLD ARRIVES WITH A FORCE ACCOUNT ALREADY LABELLED
```

The first is a classroom convenience.

The second is false.

Suggested teacher sentence:

> “Today many questions will give you the force list so that you can practise adding forces. Later we will learn how physicists decide which forces belong on that list.”

---

## 22. Do not call every meter reading net force

Use:

> “The newton meter measures one force.”

Avoid:

> “The newton meter measures the net force.”

unless the problem has separately established a force account whose other contributions sum to zero or, in the simplest introductory case, that the meter force is the only force in the account.

The clean first-stage teaching case is:

> “The meter force is the only force in this simplified account.”

Later examples can show that other forces may exist while the meter reading still happens numerically to equal the net force because those other contributions cancel.

---

# Part VIII — Suggested Mini-Sequence for the Younger Lesson

## 23. Possible progression

A compact teaching route is:

```text
1. One supplied force
   -> net force is that force

2. Several same-direction supplied forces
   -> add magnitudes

3. Opposing forces
   -> signed addition / subtraction

4. Balanced account
   -> nonzero forces can produce zero net force

5. Newton meter
   -> meter supplies one force value

6. Meter plus another supplied force
   -> meter reading need not equal net force

7. Two-dimensional forces
   -> vector addition

8. Components
   -> decomposing one vector does not create new physical forces

9. Same net force from different supplied accounts
   -> resultant does not identify account

10. Final distinction
    -> the physical force account represents the interactions on the object
    -> find/receive the forces first, then add them
```

---

# Part IX — Exit Questions

## 24. Short exit bank

### Question 1

> Three forces act on a box:
>
> - 10 N right
> - 15 N right
> - 5 N left
>
> What is the net force?

Expected:

```text
20 N right
```

---

### Question 2

> Two forces act:
>
> - 8 N right
> - 8 N left
>
> The net force is zero. Are there no forces acting?

Expected:

```text
No. Two nonzero forces were supplied and they cancel.
```

---

### Question 3

> A newton meter reads 7 N right. No other information about the object's force account is supplied. What is the net force?

Expected:

```text
Not determined from the information supplied.
The meter has supplied one force value, not necessarily the complete force account.
```

---

### Question 4

> A newton meter reads 7 N right and the problem states that this is the only force in the account. What is the net force?

Expected:

```text
7 N right
```

---

### Question 5

> The net force is 10 N right. Does that prove that two 5 N-right forces act on the object?

Expected:

```text
No.
5 N + 5 N is one possible mathematical decomposition.
The net-force value alone does not establish the physical force account.
```

---

### Question 6

> One physical force vector is broken into horizontal and vertical components. Have two physical forces been discovered?

Expected:

```text
No.
The components are a mathematical decomposition of one vector unless the physical account independently contains two separate forces.
```

---

# Part X — Compact Lesson Summary

The younger-student NML3 force-sum lesson can remain close to ordinary introductory mechanics.

Students learn to:

```text
recognise supplied force arrows
add forces in the same direction
combine opposing forces
use vector addition
find the net force
understand cancellation
read a newton meter as a measurement of one force
```

The distinctive NML3 extension comes at the end.

Students are shown that:

```text
one resultant vector
has many mathematical decompositions
```

but:

```text
those decompositions do not automatically describe physical forces
```

The physical model instead contains a particular force account intended to represent the interactions experienced by the object.

The final student-facing rule is:

> **Find or receive the forces first. Add them second. Do not start with the net force and invent the forces afterward.**

And the forward-looking boundary is:

> **In this lesson, many questions give you the force account. Later lessons ask how that account is established from the physical interactions themselves.**
