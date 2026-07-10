# Center of Mass & Linear Momentum

*Source lecture(s):* [SC133 Lec 10](../lectures.md)

## Intuition

Toss a hammer spinning through the air: every point traces a wild curve — except one.
One special point rides a perfect [projectile parabola](projectile-motion.md) as if
the hammer were a single particle. That point is the **center of mass** (CM): the
mass-weighted average position, the handle by which Newton's laws grab an extended
object.

## Definition

$$\vec r_\text{cm} = \frac{\sum_i m_i \vec r_i}{\sum_i m_i}
\qquad\text{or, for continuous bodies,}\qquad
\vec r_\text{cm} = \frac{1}{M}\int \vec r\, dm$$

For symmetric uniform bodies the CM sits at the geometric center. It need not lie
inside the material at all — a doughnut's CM is in the hole, and a high-jumper's CM
can pass *under* the bar while the body arcs over it (the Fosbury flop).

## Why the CM is special

Differentiate twice and use [Newton's third law](newtons-laws.md): all *internal*
forces cancel in pairs, leaving

$$\boxed{\,M\vec a_\text{cm} = \sum \vec F_\text{ext}\,}$$

The CM of *any* system — hammer, exploding firework, diving cat — obeys the
single-particle Newton's second law under the external forces alone. Internal
rearrangement, however violent, cannot move the CM.

## Linear momentum of a system

Total momentum is the CM in disguise:

$$\vec P = \sum_i m_i\vec v_i = M\vec v_\text{cm}, \qquad
\frac{d\vec P}{dt} = \sum\vec F_\text{ext}$$

**If the net external force is zero, $\vec P$ is constant** — the conservation law
that powers all of [collision physics](collision-and-impulse.md). More on the
momentum concept itself: [linear momentum](linear-momentum.md).

## Worked example: walking on a boat

A 60 kg person walks 3 m toward the shore-end of a 120 kg boat (frictionless water).
How far does the boat move?

No external horizontal force ⇒ the CM stays put. Let the boat shift $d$ backward;
the person moves $3 - d$ forward in the ground frame:

$$60(3 - d) = 120\,d \Rightarrow d = 1\,\text{m}$$

The boat slides a metre backward — and no amount of walking, jumping, or shoving can
carry the *system's* CM ashore.

## Worked example: exploding projectile

A shell following a parabola explodes at its apex into two equal fragments; one drops
straight down. Where does the other land?

The CM continues on the original parabola and would land at range $R$. With one
fragment at $R/2$ (below the apex), symmetry of the CM average puts the other at
$\tfrac{3R}{2}$.

## Common mistakes

- **Thinking internal forces can shift the CM.** Rockets work by *throwing mass
  backward* — the exhaust's momentum is real; the CM of (rocket + exhaust) never
  accelerates without external force.
- **Placing the CM inside the body by reflex** — check the geometry (L-shapes, rings,
  crescents).
- **Forgetting the CM velocity is momentum ÷ total mass** — a useful instant sanity
  check in collision problems.

## Related concepts

- [Linear momentum](linear-momentum.md) — the conserved quantity
- [Collisions & impulse](collision-and-impulse.md) — conservation in action
- [Rotation](rotation.md) — motion *about* the CM, the other half of rigid-body dynamics
- [N-body simulations (PHY653)](../../comp-plasma/concepts/n-body-simulation.md) — the CM frame as a computational tool

## Knowledge graph position

**Prerequisites:** [Newton's laws](newtons-laws.md).
**Leads to:** [Collisions](collision-and-impulse.md), [Rotation](rotation.md).

## Quiz

**Q1 (computational).** Masses 2 kg at $x = 0$ and 6 kg at $x = 4$ m. Where is the CM?

??? success "Answer"
    $x_\text{cm} = (2\cdot0 + 6\cdot4)/8 = 3\,\text{m}$ — three times closer to the
    heavier mass, as the inverse-ratio rule demands.

**Q2 (conceptual).** An astronaut floating at rest in space throws a wrench. Describe
the CM of (astronaut + wrench) afterward.

??? success "Answer"
    Still at rest, forever. The throw is internal; astronaut and wrench carry equal
    and opposite momenta, and the CM stays fixed — which is exactly *why* throwing
    the wrench propels the astronaut.

**Q3 (multiple choice).** A firework explodes mid-flight. Immediately after, the CM
of all fragments: (a) stops (b) continues on the pre-explosion trajectory
(c) scatters unpredictably

??? success "Answer"
    **(b).** The explosion is internal; only gravity (external) acts on the CM, which
    continues its parabola until fragments start landing.
