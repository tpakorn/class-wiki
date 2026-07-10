# Torque

*Source lecture(s):* [SC133 Lec 13](../lectures.md)

## Intuition

Why do door handles live far from the hinges? Because turning effectiveness isn't
just force — it's force **times leverage**. Push near the hinge and the door ignores
you; the same push at the handle swings it easily. Torque is the turning power of a
force: how hard, how far from the axis, and how perpendicular.

## Definition

$$\boxed{\,\vec\tau = \vec r\times\vec F\,}
\qquad
\tau = rF\sin\phi = F\cdot\underbrace{r\sin\phi}_{\text{moment arm}}$$

- $\vec r$: from the axis (or pivot) to the point where the force acts
- $\phi$: angle between $\vec r$ and $\vec F$
- **Moment arm** $r_\perp = r\sin\phi$: the perpendicular distance from the axis to
  the force's line of action — often the fastest way to compute $\tau$
- Direction by the right-hand rule ([cross product](vectors.md)); in 2-D problems,
  just call counterclockwise positive

Maximum torque: push perpendicular to the lever ($\phi = 90°$). Zero torque: push
along the lever, however hard.

## Newton's second law for rotation

$$\sum \tau = I\alpha$$

Torque is to [angular acceleration](rotation.md) what force is to acceleration, with
[moment of inertia](moment-of-inertia.md) as the stubbornness. Torque also does work
($W = \tau\,\theta$) and delivers power ($P = \tau\omega$) — the reason engine specs
quote both torque and rpm.

## Worked example: the falling rod

A uniform rod (mass $M$, length $L$) pivots at one end and is released horizontal.
Initial angular acceleration?

Gravity acts at the CM, moment arm $L/2$:
$\tau = Mg\frac{L}{2}$; with $I_\text{end} = \tfrac13 ML^2$,

$$\alpha = \frac{\tau}{I} = \frac{MgL/2}{ML^2/3} = \frac{3g}{2L}$$

The *tip* then accelerates at $a = L\alpha = \tfrac32 g$ — faster than free fall!
(Stack a coin on the tip of a falling ruler: the ruler drops out from under it.)

## Worked example: the wrench and the pipe

A 20 N·m bolt, a 25 cm wrench: minimum force
$F = \tau / r = 20/0.25 = 80$ N applied perpendicular. Slip a pipe over the wrench to
double $r$ and the required force halves — leverage is free torque (the reason
"cheater bars" both work and snap bolts).

## Static equilibrium preview

A body at rest needs **both** $\sum\vec F = 0$ *and* $\sum\tau = 0$ (about any
point) — the twin conditions that power every ladder, bridge, and seesaw problem in
[equilibrium & elasticity](equilibrium.md).

## Common mistakes

- **Using the full distance instead of the moment arm.** Only the perpendicular
  component of $\vec r$ (or of $\vec F$ — your choice) contributes.
- **Forgetting torque depends on the chosen axis.** State the pivot; in equilibrium
  problems, choose the axis that kills the most unknowns.
- **Sign chaos.** Fix a positive rotation sense first and audit each torque against it.
- **Confusing torque (N·m) with energy (J).** Same units, different beasts — torque is
  a vector, and its "metre" is a lever arm, not a displacement.

## Related concepts

- [Rotation](rotation.md) & [Moment of inertia](moment-of-inertia.md) — the law $\tau = I\alpha$
- [Equilibrium & elasticity](equilibrium.md) — the $\sum\tau = 0$ applications
- [Rolling, torque & angular momentum](rolling-torque-angular-momentum.md) — $\tau = dL/dt$
- [Vectors](vectors.md) — the cross product

## Knowledge graph position

**Prerequisites:** [Vectors](vectors.md), [Newton's laws](newtons-laws.md), [Rotation](rotation.md).
**Leads to:** [Equilibrium](equilibrium.md), [Angular momentum](rolling-torque-angular-momentum.md).

## Quiz

**Q1 (computational).** A 3 N force acts at $(2\,\text{m}, 0)$ pointing in the $+y$
direction. Torque about the origin?

??? success "Answer"
    $\vec\tau = \vec r\times\vec F = (2\hat\imath)\times(3\hat\jmath) = 6\hat k$ —
    6 N·m counterclockwise.

**Q2 (conceptual).** Why does a tightrope walker carry a long pole?

??? success "Answer"
    The pole hugely increases the system's [moment of inertia](moment-of-inertia.md)
    about the wire, so a given gravitational torque produces a much smaller
    $\alpha = \tau/I$ — the tip starts slowly, buying time to correct. (Drooping ends
    even lower the CM.)

**Q3 (multiple choice).** You push on a door with fixed force. Torque about the hinges
is greatest when you push: (a) near the hinge, ⊥ door (b) at the handle, ⊥ door
(c) at the handle, along the door's plane

??? success "Answer"
    **(b).** Maximize both the distance and the perpendicularity; (c) has zero moment
    arm no matter the distance.
