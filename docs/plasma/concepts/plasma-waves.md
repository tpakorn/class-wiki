# Plasma Waves

*Source lecture(s):* [pc368_lec09_wave1, pc368_lec10_wave2](../lectures.md)

## Intuition

A plasma can sustain self-reproducing oscillations because inertia (electron mass)
and restoring force (space charge) are both built in. The simplest example is the
Langmuir wave: electrons slosh back and forth through the stationary ion sea.
More complicated geometries (magnetized, multi-species) give rise to a zoo of
modes, each with its own polarization and dispersion relation.

## Formal Definition

A **plasma wave** is a self-sustaining disturbance in which the plasma variables
($n$, $\mathbf{E}$, $\mathbf{B}$, $T$, etc.) oscillate in space and time
according to the linearized Vlasov–Maxwell or MHD equations.

## Mathematical Formulation

From linearized Vlasov–Poisson for a cold, unmagnetized plasma:

$$1 + \chi_e = 1 - \frac{\omega_{pe}^2}{\omega^2} = 0$$

This yields the **Langmuir mode**:

$$\omega^2 = \omega_{pe}^2 + 3 k^2 v_{te}^2$$

where $v_{te} = \sqrt{k_B T_e/m_e}$ is the electron thermal speed (Bohm–Gross
correction).

For warm ions, the **ion acoustic wave** appears:

$$\omega^2 = \frac{k^2 c_s^2}{1 + (k\lambda_D)^2}, \qquad c_s^2 = \frac{\gamma_e k_B T_e + \gamma_i k_B T_i}{m_i}$$

## Derivation (Langmuir)

1. Write continuity, momentum, and Poisson for a perturbed electron fluid.
2. Assume $n_e = n_0 + n_1$, $u_e = u_1$, $\phi \propto e^{i(kx - \omega t)}$.
3. Neglect pressure to get cold Langmuir: $\omega^2 = \omega_{pe}^2$.
4. Add isothermal pressure $p_e = n_e k_B T_e$ to get Bohm–Gross.
5. Verify that $\omega \gg \omega_{pi}$ justifies the frozen-ion assumption.

## Worked Example

> **Cutoff condition:** A radio wave encounters an overdense plasma ($n_e > n_c$).
> The critical density is $n_c = \varepsilon_0 m_e \omega^2 / e^2$.
> For $f = 1$ GHz, $n_c \approx 1.24\times 10^{16}\,\text{m}^{-3}$.
> If $n_e > n_c$, the wave reflects before entering.

## Common Mistakes

- **Langmuir waves are not sound waves.** They are electrostatic; ions are
  considered immobile on the electron timescale.
- **Ion acoustic needs $T_e \gg T_i$.** Otherwise Landau damping extinguishes
  the wave.
- **Dispersion = dissipation.** Dispersion changes wave shape; dissipation damps
  amplitude. They are distinct.

## Related Concepts

- [Landau Damping](landau-damping.md)
- [Streaming Instability](streaming-instability.md)
- [Magnetized Waves](magnetized-waves.md)

## Quiz Questions

1. **Conceptual:** If electrons and ions both sloshed equally, would you still
   have a Langmuir wave?
2. **Computational:** Show that for $n_e = 10^{18}\,\text{m}^{-3}$, the cold
   Langmuir frequency is $f_{pe} \approx 9$ GHz.
3. **MCQ:** Landau damping is strongest when:
   - A) $k\lambda_D \ll 1$
   - B) $k\lambda_D \approx 1$
   - C) $k\lambda_D \gg 1$
   - D) Temperature is zero

## Further Reading

- D. J. Stix, *Waves in Plasmas*.
