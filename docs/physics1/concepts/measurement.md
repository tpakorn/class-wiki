# Measurement & Units

*Source lecture(s):* [SC133 Lec 1](../lectures.md)

## Intuition

Physics is a quantitative science: every statement must survive a comparison with a
number read off an instrument. Before we can say *how* the world moves, we agree on
*what we measure it against* — a system of units — and *how well* we know it —
significant figures and uncertainty. A result without units is meaningless; a result
without an error bar is a guess wearing a lab coat.

## Why it matters

Getting units right catches most first-year mistakes for free (a velocity had better
come out in m/s), and **dimensional analysis** lets you reconstruct half-forgotten
formulas and sanity-check every answer in this course — from
[projectile range](projectile-motion.md) to the [pendulum period](pendulum.md).

## The SI base units

| Quantity | Unit | Symbol |
|---|---|---|
| length | metre | m |
| mass | kilogram | kg |
| time | second | s |
| electric current | ampere | A |
| temperature | kelvin | K |
| amount | mole | mol |
| luminous intensity | candela | cd |

Every mechanical quantity is a product of powers of **m, kg, s**. Force, for example,
has dimensions $[\text{M L T}^{-2}]$ and the derived unit newton, $1\,\text{N} = 1\,\text{kg·m/s}^2$.

## Dimensional analysis

Write each quantity's dimensions in $[\text{M}^a \text{L}^b \text{T}^c]$ and demand
both sides of any equation match. A valid physical equation is **dimensionally
homogeneous**.

$$[\text{speed}] = \frac{\text{L}}{\text{T}}, \qquad
[\text{acceleration}] = \frac{\text{L}}{\text{T}^2}, \qquad
[\text{energy}] = \frac{\text{M L}^2}{\text{T}^2}$$

This single tool reappears, in full force, in
[PC316 fluid mechanics](../../fluids/concepts/dimensional-analysis.md) where
G. I. Taylor estimated a nuclear yield from a photograph with nothing else.

## Worked example: is $v = \sqrt{2gh}$ dimensionally sound?

$$[\sqrt{gh}] = \sqrt{\frac{\text{L}}{\text{T}^2}\cdot \text{L}} = \sqrt{\frac{\text{L}^2}{\text{T}^2}} = \frac{\text{L}}{\text{T}} = [v]\ \checkmark$$

Both sides are a speed, so the formula *could* be right — dimensional analysis can't
supply the factor of 2, but it can reject anything with the wrong units.

## Significant figures & orders of magnitude

- **Significant figures** track precision: $9.8\,\text{m/s}^2$ (2 s.f.) vs
  $9.81\,\text{m/s}^2$ (3 s.f.). A result is only as precise as its *least* precise input.
- **Fermi estimates** (order-of-magnitude reasoning) get you within a factor of ten
  with almost no data — a physicist's superpower.

## Common mistakes

- **Dropping units mid-calculation**, then guessing them at the end. Carry units
  through every line; they self-check the algebra.
- **Reporting 8 digits** from 2-digit data. Significant figures are honesty about what
  you actually know.
- **Confusing mass and weight.** Mass (kg) is intrinsic; weight ($mg$, in newtons) is
  a force that depends on where you are.

## Related concepts

- [Kinematics](kinematics.md) — the first quantities we measure: position, velocity, acceleration
- [Vectors](vectors.md) — many measured quantities carry direction
- [Dimensional analysis in fluids (PC316)](../../fluids/concepts/dimensional-analysis.md)

## Knowledge graph position

**Prerequisites:** none — this is the entry point of the course.
**Leads to:** [kinematics](kinematics.md), [vectors](vectors.md), and every quantitative page that follows.

## Quiz

**Q1 (conceptual).** Why can dimensional analysis rule a formula *out* but never fully
confirm it?

??? success "Answer"
    It checks units, not dimensionless factors. $v=\sqrt{2gh}$ and $v=\sqrt{gh}$ are
    both dimensionally valid; only a derivation or experiment fixes the factor of 2.

**Q2 (computational).** The period of a pendulum might depend on length $L$, mass $m$,
and gravity $g$. Use dimensions to find the only possible combination.

??? success "Answer"
    $T \propto L^a m^b g^c$. Matching $[\text{T}]$: mass can't appear ($b=0$), and
    $\sqrt{L/g}$ is the only length/gravity combination with units of time. So
    $T \propto \sqrt{L/g}$ — mass drops out, as observed. See [pendulum](pendulum.md).

**Q3 (multiple choice).** $1\,\text{N}$ in base units is:
(a) $\text{kg·m/s}$ (b) $\text{kg·m/s}^2$ (c) $\text{kg·m}^2/\text{s}^2$

??? success "Answer"
    **(b)** — force = mass × acceleration.
