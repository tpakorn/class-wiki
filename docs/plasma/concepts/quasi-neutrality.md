# Quasi-neutrality

*Source lecture(s):* [pc368_lec02_debye](../lectures.md)

## Intuition

A plasma is quasi-neutral because electrons and ions rearrange themselves on the
Debye length scale to cancel any large-scale electric field. On scales much
larger than $\\lambda_D$, the net charge density is essentially zero.

## Formal Definition

**Quasi-neutrality** means

$$|n_e - Z n_i| \\ll n_e$$

for macroscopic lengths $L \\gg \\lambda_D$. Exact neutrality holds only in the
limit $L \\to \\infty$.

## Mathematical Formulation

From Poisson’s equation:

$$\\nabla^2\\phi = -\\frac{e}{\\varepsilon_0}(n_i - n_e)$$

With Boltzmann electrons and fixed ions, the restoring electric field is

$$E \\sim \\frac{k_B T_e}{e\\lambda_D} n_1/n_0$$

where $n_1$ is the perturbation. For $L \\gg \\lambda_D$, $n_1/n_0 \\sim
\\exp(-L/\\lambda_D) \\approx 0$.

## Derivation

Assume a small density perturbation $n_e = n_0 + n_1$. Poisson becomes

$$\\nabla^2\\phi_1 = -\\frac{e}{\\varepsilon_0}(Z n_{i1} - n_1)$$

If ions are immobile ($n_{i1}=0$) and electrons obey Boltzmann statistics,
$n_1/n_0 = e\\phi_1/k_B T_e$. Substituting gives the screened Poisson
equation with screening length $\\lambda_D$.

## Worked Example

If a plasma blob has $n_e = 10^{19}\\,\\text{m}^{-3}$ and $T_e = 1$ eV, then
$\\lambda_D \\sim 7\\times 10^{-5}\\,\\text{m}$. A fluctuation of $\\Delta n/n
= 10^{-3}$ on a 1-cm scale generates $E \\sim (k_B T_e/e\\lambda_D) \\cdot
10^{-3} \\approx 0.1\\,\\text{V/m}$, negligible for most applications.

## Common Mistakes

- Believing plasmas are *exactly* neutral. They are only neutral on scales
  $L \\gg \\lambda_D$; sheaths and double layers are strongly non-neutral.
- Applying quasi-neutrality inside the Debye sphere. It breaks down there
  by design.

## Related Concepts

- [Plasma](plasma.md)
- [Debye Shielding](debye-shielding.md)
- [Ideal Plasma](ideal-plasma.md)
- [Poisson’s Equation in Plasma](poisson-equation.md)

## Quiz Questions

1. Why can a plasma sheath be non-neutral while the bulk is quasi-neutral?
2. Does quasi-neutrality hold for a single particle in vacuum?

## Further Reading

- D. A. Gurnett & A. Bhattacharjee, *Introduction to Plasma Physics*.
