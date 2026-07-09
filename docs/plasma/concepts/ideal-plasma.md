# Ideal Plasma

*Source lecture(s):* [pc368_lec01_intro](../lectures.md)

## Intuition

An ideal plasma is a “perfect” plasma where collective effects dominate over
binary collisions. In this regime, particles interact primarily through the
long-range electromagnetic field, not through short-range collisions.

## Formal Definition

A plasma is **ideal** when three conditions hold:

1. **Plasma approximation:** $\\lambda_D \\ll L$
2. **Quasi-neutrality:** $n_e \\approx Z n_i$ on scales $L \\gg \\lambda_D$
3. **Collective parameter:** $\\Lambda = 4\\pi n \\lambda_D^3 \\gg 1$

## Mathematical Formulation

The **coupling parameter** $\\Gamma$ compares mean kinetic energy to mean
potential energy:

$$\\Gamma = \\frac{e^2}{4\\pi\\varepsilon_0 \\lambda_D k_B T} = \\frac{1}{3\\Lambda^{2/3}}$$

Weak coupling requires $\\Gamma \\ll 1$, equivalent to $\\Lambda \\gg 1$.

## Derivation

Inside a Debye sphere of radius $\\lambda_D$, there are

$$N_D = \\frac{4\\pi}{3} \\lambda_D^3 n = \\frac{4\\pi}{3} \\Bigl(\\frac{\\varepsilon_0 k_B T_e}{n_e e^2}\\Bigr)^{3/2} n_e = \\Lambda$$

particles. If $N_D \\gg 1$, each particle feels the smoothed, collective
potential rather than discrete collisions.

## Worked Example

For a tokamak edge plasma with $n_e = 10^{18}\\,\\text{m}^{-3}$ and $T_e = 10$ eV:

$$\\lambda_D \\approx 7\\times 10^{-5}\\,\\text{m}, \\quad \\Lambda \\approx 3\\times 10^6 \\gg 1$$

So the plasma is ideal.

## Common Mistakes

- Assuming high temperature alone guarantees an ideal plasma. Low density can
  make $\\lambda_D$ large and $\\Lambda$ small.
- Confusing $\\lambda_D \\ll L$ with $\\lambda_D \\ll \\rho$ (Larmor radius).
  Both matter for different reasons.

## Related Concepts

- [Plasma](plasma.md)
- [Debye Shielding](debye-shielding.md)
- [Quasi-neutrality](quasi-neutrality.md)

## Quiz Questions

1. Why does $\\Lambda \\gg 1$ imply collective behavior?
2. Is a dense, cold plasma more or less ideal than a tenuous, hot one?

## Further Reading

- F. F. Chen, *Introduction to Plasma Physics and Controlled Fusion*.
