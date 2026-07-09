# Magnetic Mirror

*Source lecture(s):* [pc368_lec08_adiabatic_invariant](../lectures.md)

## Intuition

A magnetic mirror is a region where the magnetic field strength increases along a
field line. Charged particles spiraling into this region slow their parallel
motion and can reflect back, creating a magnetic “bottle.”

## Formal Definition

Reflection occurs when the pitch angle $\\theta$ satisfies

$$\\sin^2\\theta \\geq \\frac{B_{\\text{min}}}{B_{\\text{max}}}$$

Equivalently, the **loss cone** angle is

$$\\theta_{\\text{lc}} = \\arcsin\\sqrt{\\frac{B_{\\text{min}}}{B_{\\text{max}}}}$$

## Mathematical Formulation

The magnetic moment is an adiabatic invariant:

$$\\mu = \\frac{m v_\\perp^2}{2 B} = \\text{const}$$

As $B$ increases, $v_\\perp$ grows and $v_\\parallel$ must decrease to conserve
energy. Reflection happens when $v_\\parallel = 0$.

## Derivation

1. Start from $\\mu = m v_\\perp^2/(2B) =$ const.
2. Total energy $E = m v_\\parallel^2/2 + \\mu B =$ const.
3. At the mirror point $v_\\parallel = 0$, so $E = \\mu B_{\\text{max}}$.
4. At the minimum field, $E = \\mu B_{\\text{min}} + m v_{\\parallel,\\text{min}}^2/2$.
5. Equating gives the loss-cone condition.

## Worked Example

For a magnetic mirror with $B_{\\text{min}} = 0.1$ T and $B_{\\text{max}} = 1$ T:

$$\\theta_{\\text{lc}} = \\arcsin\\sqrt{0.1} \\approx 18°$$

Only particles with $\\theta < 18°$ escape; the rest are trapped.

## Common Mistakes

- Believing mirrors reflect all particles. Only those outside the loss cone are
  trapped.
- Confusing mirror ratio $R_m = B_{\\text{max}}/B_{\\text{min}}$ with field
  strength.

## Related Concepts

- [Adiabatic Invariant](adiabatic-invariant.md)
- [Larmor Radius](larmor-radius.md)
- [Drift Motion](drift-motion.md)

## Quiz Questions

1. Why are magnetic mirrors not perfect traps?
2. How does increasing $B_{\\text{max}}$ affect the loss cone?

## Further Reading

- W. I. van Ruller, *Charged Particle Optics*.
