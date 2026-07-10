# Potential Energy

*Source lecture(s):* [SC133 Lec 9](../lectures.md)

## Intuition

Lift a book: you do work against gravity, and the motion you "paid for" seems gone.
But drop the book — the motion comes back, in full. The work wasn't lost; it was
**banked**. Potential energy is stored work: energy of *configuration* (how high, how
stretched, how far apart) rather than of motion. Only special forces offer this
banking service — the **conservative** ones.

## Conservative forces & the definition

A force is **conservative** if the work it does between two points is independent of
the path (equivalently: zero work around any closed loop). Gravity and springs
qualify; [friction](friction-and-drag.md) does not — a longer path means more heat.

For a conservative force, define potential energy by the work *against* it:

$$\Delta U = -W_\text{cons} = -\int \vec F\cdot d\vec s$$

and recover the force from the landscape:

$$F_x = -\frac{dU}{dx}$$

— force points *downhill* on the energy landscape, with magnitude equal to the slope.

## The standard catalogue

| System | Potential energy | Reference |
|---|---|---|
| Uniform gravity | $U = mgh$ | any convenient $h=0$ |
| Spring ([Hooke](../equations/hookes-law.md)) | $U = \tfrac12 kx^2$ | natural length |
| Newtonian gravity | $U = -\dfrac{GMm}{r}$ | zero at $r \to \infty$ |

Only *differences* in $U$ matter — the zero point is yours to choose (and for
$-GMm/r$ the conventional choice makes bound orbits have $E < 0$; see
[gravitation](gravitation.md)).

## Reading energy landscapes

On a $U(x)$ graph:

- **Equilibria** sit where $dU/dx = 0$ — valleys are **stable** (restoring force),
  hilltops **unstable**.
- A particle with total energy $E$ moves where $E \geq U(x)$; the boundaries are
  **turning points**.
- Near any valley bottom, $U \approx \tfrac12 k x^2$ — which is why
  [simple harmonic motion](simple-harmonic-motion.md) is everywhere.

This landscape-reading skill scales all the way up to
[stability analysis in fluids](../../fluids/concepts/hydrodynamic-stability.md) and
plasma equilibria.

## Worked example: spring-launched block

A 0.5 kg block compresses a $k = 800\,\text{N/m}$ spring by 10 cm, then is released
on a frictionless track. Launch speed?

$$\tfrac12 kx^2 = \tfrac12 mv^2 \Rightarrow
v = x\sqrt{k/m} = 0.1\sqrt{1600} = 4\,\text{m/s}$$

No forces, no trajectory, no time — just the bank transfer $U \to K$.

## Common mistakes

- **Assigning potential energy to friction.** Non-conservative forces have no $U$;
  their work depends on the path taken.
- **Treating $U$'s zero point as physical.** Negative potential energy is not weird —
  only $\Delta U$ appears in physics.
- **Forgetting whose energy it is.** $U$ belongs to the *system* (Earth + book, spring
  + block), not to one object alone.
- **Sign slips in $F = -dU/dx$** — the minus sign is the whole content: force pushes
  toward lower $U$.

## Related concepts

- [Kinetic energy & work](kinetic-energy-and-work.md) — the other half of the ledger
- [Conservation of energy](conservation-of-energy.md) — the ledger balanced
- [Simple harmonic motion](simple-harmonic-motion.md) — life at the bottom of a valley
- [Gravitation](gravitation.md) — the $-GMm/r$ well

## Knowledge graph position

**Prerequisites:** [Work & kinetic energy](kinetic-energy-and-work.md).
**Leads to:** [Conservation of energy](conservation-of-energy.md), [SHM](simple-harmonic-motion.md), [orbits](keplers-laws.md).

## Quiz

**Q1 (computational).** A 60 kg hiker climbs 500 m of elevation. Change in
gravitational potential energy?

??? success "Answer"
    $\Delta U = mgh = 60\times9.8\times500 = 2.94\times10^5\,\text{J}$ ≈ 0.3 MJ —
    about the energy in 70 food-calories. Bodies are inefficient; the hike costs far
    more.

**Q2 (conceptual).** Why can't we define a potential energy for friction?

??? success "Answer"
    Friction's work depends on path length, not endpoints — around a closed loop it
    does nonzero (negative) work. No single-valued function of position can encode
    that; the energy leaves mechanics as heat.

**Q3 (multiple choice).** At a stable equilibrium point, $U(x)$ has:
(a) maximum, $F=0$ (b) minimum, $F=0$ (c) zero value

??? success "Answer"
    **(b).** Valley bottom: zero slope (no force) and curvature that pushes back when
    displaced.
