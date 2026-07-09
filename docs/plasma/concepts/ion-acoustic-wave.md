# Ion Acoustic Wave

*Source lecture(s):* [pc368_lec09_wave1, pc368_lec10_wave2, pc368_lec11_streaming_ins](../lectures.md)

## Intuition

Ion acoustic waves are the ion-scale analog of sound waves in a plasma. Ions
provide the inertia, while pressure gradients and electron Boltzmann response
provide the restoring force.

## Formal Definition

The ion acoustic dispersion relation is

$$\\omega^2 = \\frac{k^2 c_s^2}{1 + k^2\\lambda_{De}^2}$$

where $c_s = \\sqrt{(\\gamma_e k_B T_e + \\gamma_i k_B T_i)/m_i}$ is the ion
sound speed.

## Mathematical Formulation

From two-fluid equations with Boltzmann electrons ($n_e = n_0 \\exp(e\\phi/k_B T_e)$)
and cold ions ($T_i \\ll T_e$), linearizing gives

$$\\omega^2 = \\frac{k^2 k_B T_e/m_i}{1 + k^2\\lambda_{De}^2}$$

## Derivation

1. Linearize ion continuity and momentum.
2. Use Boltzmann response for electrons to close Poisson.
3. Eliminate density and potential.
4. The ion inertial term $m_i$ in the denominator makes these waves slow
   compared to Langmuir waves.

## Worked Example

For $T_e = 10$ eV, $T_i = 1$ eV, $m_i = m_p$:
- $c_s \\approx \\sqrt{k_B T_e/m_i} \\approx 2.5\\times 10^3\\,\\text{m/s}$
- At $k\\lambda_{De} \\ll 1$, $\\omega \\approx k c_s$.

## Common Mistakes

- Assuming $T_i = T_e$. Strong ion acoustic waves require $T_e \\gg T_i$.
- Ignoring electron inertia. It is negligible because $m_e \\ll m_i$.

## Related Concepts

- [Plasma Waves](plasma-waves.md)
- [Langmuir Waves](langmuir-waves.md)
- [Plasma Sheath](plasma-sheath.md)
- [Sound Speed](sound-speed.md)

## Quiz Questions

1. Why does the ion acoustic speed depend on electron temperature, not ion temperature?
2. What happens when $k\\lambda_{De} \\gg 1$?

## Further Reading

- D. A. Gurnett & A. Bhattacharjee, *Introduction to Plasma Physics*.
