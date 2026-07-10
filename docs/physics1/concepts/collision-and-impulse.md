# Collisions & Impulse

*Source lecture(s):* [SC133 Lec 11](../lectures.md)

## Intuition

A collision is physics compressed into milliseconds: forces too large and too brief
to track directly. The escape is to integrate over the mess. **Impulse** — force
accumulated over time — equals the momentum change, no matter how wild the force
profile. And for the colliding *system*, total [momentum](linear-momentum.md) simply
passes through unchanged. From car crashes to particle physics, this is the same
calculation.

## Impulse–momentum theorem

$$\boxed{\,\vec J = \int \vec F\,dt = \Delta\vec p\,}
\qquad\text{(} \vec J \approx \vec F_\text{avg}\,\Delta t \text{)}$$

The same $\Delta p$ can come from a huge force over a short time or a gentle force
over a long one. **Every safety device exploits this**: airbags, crumple zones,
bending your knees on landing — all stretch $\Delta t$ to shrink $F_\text{avg}$.

## The collision taxonomy

Momentum is conserved in *all* of them (isolated system); kinetic energy
distinguishes:

| Type | Momentum | Kinetic energy | Signature |
|---|---|---|---|
| **Elastic** | conserved | conserved | bodies bounce apart cleanly |
| **Inelastic** | conserved | partly lost | some heat/deformation |
| **Perfectly inelastic** | conserved | maximum loss | bodies stick together |

**Perfectly inelastic** (stick): $v' = \dfrac{m_1v_1 + m_2v_2}{m_1 + m_2}$ — the
[center-of-mass](center-of-mass.md) velocity; the KE of relative motion is destroyed.

**Elastic 1-D** (the exam classic):

$$v_1' = \frac{m_1 - m_2}{m_1 + m_2}v_1 + \frac{2m_2}{m_1+m_2}v_2
\qquad
v_2' = \frac{2m_1}{m_1+m_2}v_1 + \frac{m_2 - m_1}{m_1+m_2}v_2$$

Limiting cases to memorize: equal masses **exchange velocities** (Newton's cradle); a
ball off a wall reverses; a heavy ball barely notices a light one but sends it off at
nearly $2v_1$.

## Worked example: ballistic pendulum

A 10 g bullet embeds in a 2 kg block, which swings up 5 cm. Bullet speed?

Two stages, two laws — never mix them:

1. **Collision** (momentum only, KE destroyed):
   $m_b v = (m_b + M)V$.
2. **Swing** ([energy](conservation-of-energy.md)):
   $V = \sqrt{2gh} = \sqrt{2(9.8)(0.05)} = 0.99\,\text{m/s}$.

$$v = \frac{2.01}{0.01}(0.99) \approx 199\,\text{m/s}$$

Using energy conservation *across the embedding* would be wrong by a factor of
$\sim 200$ — the classic trap.

## Try it live

The **[collision lab](../simulations/collision-lab.md)** lets you set masses,
velocities and elasticity, then watch momentum and kinetic-energy bars during the
impact.

## Common mistakes

- **Conserving kinetic energy in inelastic collisions.** Momentum: always (isolated).
  KE: only if stated elastic.
- **Dropping signs in 1-D.** Velocities are signed; head-on means opposite signs.
- **Two-stage problems solved in one stage** (ballistic pendulum above).
- **Forgetting impulse is a vector.** A ball bouncing straight back off a wall has
  $|\Delta p| = 2mv$, not zero and not $mv$.

## Related concepts

- [Linear momentum](linear-momentum.md) — the conserved quantity
- [Center of mass](center-of-mass.md) — collisions look simplest in the CM frame
- [Conservation of energy](conservation-of-energy.md) — the elastic special case
- [Collision lab (live demo)](../simulations/collision-lab.md)
- [N-body gravitational encounters (PHY653)](../../comp-plasma/concepts/n-body-simulation.md)

## Knowledge graph position

**Prerequisites:** [Linear momentum](linear-momentum.md), [Newton's laws](newtons-laws.md).
**Leads to:** [Rotation](rotation.md) (angular analogues), kinetic theory of [gases](ideal-gas.md) — pressure *is* molecular impulse.

## Quiz

**Q1 (computational).** A 1000 kg car at 20 m/s rear-ends a stationary 1500 kg van;
they lock together. Final speed, and fraction of KE lost?

??? success "Answer"
    $v' = 1000(20)/2500 = 8\,\text{m/s}$.
    $K_i = 200\,\text{kJ}$, $K_f = \tfrac12(2500)(64) = 80\,\text{kJ}$ — 60% of the
    kinetic energy went into crumpled metal. (Loss fraction $= m_2/(m_1+m_2)$.)

**Q2 (conceptual).** Why does an egg survive being dropped onto a pillow but not onto
concrete, when $\Delta p$ is identical?

??? success "Answer"
    Impulse $F\Delta t = \Delta p$ is fixed, but the pillow stretches $\Delta t$ by
    ~100×, cutting the peak force by the same factor — below the shell's breaking
    strength.

**Q3 (multiple choice).** In an elastic collision between equal masses, one initially
at rest, after impact: (a) both move at $v/2$ (b) they exchange velocities
(c) the first bounces back

??? success "Answer"
    **(b).** The mover stops dead; the target leaves with $v$ — watch any Newton's
    cradle or billiards shot.

**Q4 (conceptual).** A superball and a clay ball of equal mass hit a door at the same
speed. Which is more likely to slam it shut?

??? success "Answer"
    The superball: it bounces back, delivering impulse up to $2mv$ versus the clay's
    $mv$. Elastic rebound *doubles* the momentum transfer.
