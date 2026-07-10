# Work & Kinetic Energy

*Source lecture(s):* [SC133 Lec 8](../lectures.md)

## Intuition

Newton's laws track forces instant by instant. Energy methods take a shortcut: instead
of following the whole trajectory, compare *before* and *after*. **Work** is the
currency — force succeeding at pushing something through a distance — and **kinetic
energy** is the account balance of motion. The exchange rate is exact: net work in,
kinetic energy up, joule for joule.

## Definitions

**Work** by a constant force $\vec F$ over displacement $\vec d$:

$$W = \vec F\cdot\vec d = Fd\cos\theta$$

Only the force component *along the motion* counts ([dot product](vectors.md)).
Perpendicular forces (the normal force on a sliding block, tension in a circular
swing) do **zero** work. For varying forces:

$$W = \int \vec F\cdot d\vec s \qquad\text{e.g. spring: } W = \int_0^x(-kx')dx' = -\tfrac12 kx^2$$

**Kinetic energy:**

$$K = \tfrac12 m v^2$$

**Power** — rate of doing work:

$$P = \frac{dW}{dt} = \vec F\cdot\vec v \qquad [1\,\text{W} = 1\,\text{J/s}]$$

## The work–energy theorem

$$\boxed{\,W_\text{net} = \Delta K = \tfrac12 mv_f^2 - \tfrac12 mv_i^2\,}$$

**Derivation** (1-D, from Newton II):
$W = \int F\,dx = \int m\frac{dv}{dt}dx = \int m\frac{dv}{dt}v\,dt = \int mv\,dv
= \tfrac12 mv_f^2 - \tfrac12 mv_i^2$. ∎
(Full version on the [equation page](../equations/work-energy-theorem.md).)

The theorem is Newton's second law *integrated over distance* — no new physics, but a
scalar equation that skips all the trajectory details.

## Worked example: braking distance

A car at speed $v$ locks its brakes; kinetic friction $\mu_k mg$ acts over distance
$d$. The theorem: $-\mu_k mg\,d = 0 - \tfrac12 mv^2$, so

$$d = \frac{v^2}{2\mu_k g}$$

Mass cancels; distance grows with the **square** of speed. Doubling your speed
quadruples the skid — the single most life-relevant equation in this course.

## Signs of work

| Situation | Sign of $W$ | Effect on $K$ |
|---|---|---|
| Force along motion (engine) | + | speeds up |
| Force against motion (friction, braking) | − | slows down |
| Force ⊥ motion (normal, centripetal) | 0 | speed unchanged (direction may change!) |

The zero-work case explains why [magnetic forces never change a particle's speed](../../comp-plasma/equations/lorentz-force.md).

## Common mistakes

- **"I pushed hard, so I did work."** Pushing a wall does zero work — no
  displacement. Holding a suitcase stationary: zero work (tiring ≠ work).
- **Forgetting work is signed.** Friction does *negative* work; the theorem needs the
  net, signed total.
- **Confusing power with energy.** A 1000 W kettle running for one hour uses energy
  $= P t = 3.6$ MJ; watts measure the *rate*.
- **Using $W = Fd$ with the total force in circular motion** — the centripetal force
  does no work at all.

## Related concepts

- [Potential energy](potential-energy.md) — work stored for later
- [Conservation of energy](conservation-of-energy.md) — the full budget
- [Work–energy theorem (equation page)](../equations/work-energy-theorem.md)
- [Vectors](vectors.md) — the dot product

## Knowledge graph position

**Prerequisites:** [Newton's laws](newtons-laws.md), [Vectors](vectors.md).
**Leads to:** [Potential energy](potential-energy.md) → [Conservation of energy](conservation-of-energy.md).

## Quiz

**Q1 (computational).** A 2 kg block accelerates from 3 m/s to 7 m/s. Net work done?

??? success "Answer"
    $W = \Delta K = \tfrac12(2)(49 - 9) = 40\,\text{J}$ — regardless of how the
    force varied along the way.

**Q2 (conceptual).** A satellite in circular orbit: how much work does gravity do per
revolution?

??? success "Answer"
    Zero. Gravity is exactly centripetal (⊥ velocity) at every instant, so
    $\vec F\cdot d\vec s = 0$ throughout — consistent with constant orbital speed.

**Q3 (computational).** What steady power must a 1200 kg car deliver to climb a 5%
grade at 20 m/s (ignore drag)?

??? success "Answer"
    Force along slope $\approx mg\times 0.05 = 588\,\text{N}$;
    $P = Fv = 588\times20 \approx 11.8\,\text{kW}$ (≈16 hp) — hills, not flat
    cruising, are what engines are sized for.

**Q4 (multiple choice).** Two objects with equal momentum but different masses: which
has more kinetic energy? (a) heavier (b) lighter (c) equal

??? success "Answer"
    **(b).** $K = p^2/2m$ — at fixed $p$, smaller mass means larger $K$. (A bullet
    beats a truck at equal momentum.)
