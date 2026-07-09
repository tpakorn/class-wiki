# Langmuir Waves

*Source lecture:* pc368_lec09_wave1, pc368_lec10_wave2

## Intuition

Langmuir waves are the natural electrostatic oscillations of electrons against a
stationary ion background. They are the “sound” of a plasma’s electron fluid.

## Formal Definition

Langmuir waves are electrostatic normal modes with dispersion relation

$$\\omega^2 = \\omega_{pe}^2 + 3 k^2 v_{te}^2$$

in the warm-fluid limit, where $\\omega_{pe}$ is the plasma frequency and
$v_{te}$ is the electron thermal speed.

## Mathematical Formulation

From the linearized Vlasov–Poisson system with a Maxwellian background, the
dielectric function is

$$\\varepsilon(k,\\omega) = 1 + \\frac{1}{k^2\\lambda_D^2}\\Bigl[1 + \\zeta Z(\\zeta)\\Bigr] = 0$$

with $\\zeta = \\omega/(k\\sqrt{2}v_{te})$. For $k\\lambda_D \\ll 1$, this
reduces to the fluid Langmuir dispersion above.

## Derivation

1. Linearize electron continuity and momentum equations with $p = n k_B T$.
2. Assume isothermal or adiabatic electrons ($\\gamma_e = 1$ or $5/3$).
3. Combine with Poisson’s equation to eliminate density and potential.
4. The resulting wave equation gives $\\omega^2 = \\omega_{pe}^2 + 3 k^2 v_{te}^2$.

## Worked Example

For $n_e = 10^{18}\\,\\text{m}^{-3}$ and $T_e = 1$ eV:
- $f_{pe} \\approx 9$ GHz.
- For $k\\lambda_D = 0.1$, $\\omega \\approx \\omega_{pe}\\sqrt{1 + 0.03}
  \\approx 1.015\\,\\omega_{pe}$.

## Common Mistakes

- Calling Langmuir waves “electromagnetic.” They are electrostatic; $\\mathbf{E}$
  is parallel to $\\mathbf{k}$.
- Forgetting the thermal correction $3k^2 v_{te}^2$. At $k\\lambda_D \\sim 1$,
  it dominates.

## Related Concepts

- [Plasma Frequency](../equations/plasma-frequency.md)
- [Debye Length](../equations/debye-length.md)
- [Plasma Waves](plasma-waves.md)
- [Landau Damping](landau-damping.md)

## Quiz Questions

1. What is the phase velocity of a cold Langmuir wave?
2. Why does Landau damping vanish in the cold-fluid limit?

## Further Reading

- T. H. Stix, *Waves in Plasmas*.
