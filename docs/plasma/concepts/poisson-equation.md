# Poisson’s Equation in Plasma

*Source lecture:* pc368_lec02_debye

## Intuition

Poisson’s equation links charge density to electric potential. In plasma physics,
it closes the fluid/kinetic description by relating particle densities to the
self-consistent electrostatic field.

## Formal Definition

$$\\nabla^2 \\phi = -\\frac{\\rho}{\\varepsilon_0}$$

where $\\rho = e\\Bigl(\\sum_s Z_s n_{is} - n_{es}\\Bigr)$ is the net charge
density.

## Mathematical Formulation

For a single species with Boltzmann response:

$$\\nabla^2 \\phi - \\frac{1}{\\lambda_D^2}\\phi = -\\frac{e}{\\varepsilon_0}\\bigl(Z n_{i0} - n_{e0}\\bigr)$$

The homogeneous solution decays as $\\exp(-r/\\lambda_D)/r$.

## Derivation

Start from Gauss’s law $\\nabla\\cdot\\mathbf{E} = \\rho/\\varepsilon_0$ and
$\\mathbf{E} = -\\nabla\\phi$. The screened Poisson equation follows by
substituting the linearized Boltzmann relation for electrons.

## Worked Example

For a point charge $+Ze$ in an electron-ion plasma with fixed ions, the screened
potential is

$$\\phi(r) = \\frac{Ze}{4\\pi\\varepsilon_0 r} e^{-r/\\lambda_D}$$

At $r = \\lambda_D$, the potential has dropped to $1/e$ of its vacuum value.

## Common Mistakes

- Forgetting the sign: positive charge gives $\\nabla^2\\phi < 0$.
- Using vacuum Green’s function when $\\lambda_D$ is finite.

## Related Concepts

- [Debye Shielding](debye-shielding.md)
- [Quasi-neutrality](quasi-neutrality.md)
- [Ideal Plasma](ideal-plasma.md)

## Quiz Questions

1. What happens to Poisson’s equation when $\\lambda_D \\to 0$?
2. Why does the Yukawa potential reduce to the Coulomb potential at $r \\ll \\lambda_D$?

## Further Reading

- J. D. Jackson, *Classical Electrodynamics*.
