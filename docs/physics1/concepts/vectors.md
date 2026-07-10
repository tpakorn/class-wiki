# Vectors

*Source lecture(s):* [SC133 Lec 3](../lectures.md)

## Intuition

"Walk 5 km" is incomplete; "walk 5 km north-east" is an instruction. Quantities that
carry both **magnitude and direction** — displacement, velocity, force — are vectors.
Quantities fully specified by one number — mass, temperature, speed — are **scalars**.
The entire machinery of 2-D and 3-D physics is bookkeeping for arrows.

## Components: the master move

Any vector resolves into perpendicular components:

$$\vec A = A_x\,\hat\imath + A_y\,\hat\jmath, \qquad
A_x = A\cos\theta,\quad A_y = A\sin\theta$$

$$A = |\vec A| = \sqrt{A_x^2 + A_y^2}, \qquad \tan\theta = \frac{A_y}{A_x}$$

Components turn geometry into arithmetic: to add vectors, add their components.
$\vec C = \vec A + \vec B \iff C_x = A_x + B_x,\ C_y = A_y + B_y$. Physics problems in
2-D are just two 1-D problems glued together — the insight behind
[projectile motion](projectile-motion.md).

## The two products

**Dot product** (scalar result) — measures alignment:

$$\vec A\cdot\vec B = AB\cos\theta = A_xB_x + A_yB_y + A_zB_z$$

Zero for perpendicular vectors. Physics use: [work](kinetic-energy-and-work.md)
$W = \vec F\cdot\vec d$ — only the force component *along* the motion counts.

**Cross product** (vector result) — measures perpendicularity, points normal to both
(right-hand rule):

$$|\vec A\times\vec B| = AB\sin\theta, \qquad
\vec A\times\vec B = (A_yB_z - A_zB_y)\,\hat\imath + (A_zB_x - A_xB_z)\,\hat\jmath + (A_xB_y - A_yB_x)\,\hat k$$

Physics use: [torque](torque.md) $\vec\tau = \vec r\times\vec F$,
[angular momentum](rolling-torque-angular-momentum.md) $\vec L = \vec r\times\vec p$,
magnetic force (SC134).

## Worked example: river crossing

A boat moves at $4\,\text{m/s}$ relative to water, pointed straight across a river
flowing at $3\,\text{m/s}$. What is the boat's speed over the ground?

The velocities add as vectors at right angles:
$v = \sqrt{4^2 + 3^2} = 5\,\text{m/s}$, at $\theta = \tan^{-1}(3/4) \approx 37°$
downstream of straight across. (This is [relative motion](relative-motion.md) in one
picture.)

## Common mistakes

- **Adding magnitudes instead of components.** $|\vec A + \vec B| \ne A + B$ unless
  the vectors are parallel.
- **Dropping direction from an answer.** "The force is 10 N" is half an answer.
- **Using degrees in one place and radians in another.** Pick one; check your
  calculator mode.
- **Right-hand-rule with the left hand.** It happens to everyone once. Only once,
  ideally.

## Related concepts

- [Kinematics](kinematics.md) — velocities and accelerations are vectors
- [Projectile motion](projectile-motion.md) — component thinking in action
- [Torque](torque.md) — the cross product at work
- [Vector operations at graduate depth (PHY621)](../../phy621/concepts/vector-operations.md)

## Knowledge graph position

**Prerequisites:** [Measurement](measurement.md).
**Leads to:** [Projectile motion](projectile-motion.md), [relative motion](relative-motion.md), [Newton's laws](newtons-laws.md), [torque](torque.md).

## Quiz

**Q1 (computational).** $\vec A = 3\hat\imath + 4\hat\jmath$,
$\vec B = -2\hat\imath + \hat\jmath$. Find $\vec A\cdot\vec B$ and
$|\vec A\times\vec B|$.

??? success "Answer"
    $\vec A\cdot\vec B = -6 + 4 = -2$.
    $\vec A\times\vec B = (3\cdot1 - 4\cdot(-2))\hat k = 11\hat k$, magnitude 11.

**Q2 (conceptual).** Can the magnitude of $\vec A + \vec B$ be smaller than both $A$
and $B$?

??? success "Answer"
    Yes — nearly antiparallel vectors almost cancel: $|\vec A + \vec B|$ ranges from
    $|A - B|$ to $A + B$.

**Q3 (multiple choice).** $\vec A\cdot(\vec A\times\vec B)$ equals:
(a) $A^2B$ (b) 0 (c) $AB\cos\theta$

??? success "Answer"
    **(b).** The cross product is perpendicular to $\vec A$, and dotting perpendicular
    vectors gives zero — always.
