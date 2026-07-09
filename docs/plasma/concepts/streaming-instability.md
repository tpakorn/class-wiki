# Streaming Instability

*Source lecture(s):* [pc368_lec11_streaming_ins](../lectures.md)

## Intuition

A fast beam of electrons streaming through a background plasma can transfer
energy to plasma waves when the beam speed exceeds the phase velocity of certain
modes. This is the **two-stream instability** (often called the Buneman instability
when $v_0 \gg v_{te}$). Instead of damping, the wave grows exponentially,
creating holes and vortices in velocity space.

## Formal Definition

The **streaming instability** is a kinetic instability that arises when a
drifted Maxwellian beam co-exists with a background plasma, satisfying the
resonance condition $v_\phi \approx v_0$.

## Mathematical Formulation

The dispersion relation for a cold beam of density $n_b$ and drift $v_0$ through
a cold background plasma ($n_0$) is:

$$1 + \chi_0 + \chi_b = 0$$

with

$$\chi_{0,b} = -\frac{\omega_{p,0/b}^2}{(\omega - k v_{0/b})^2}$$

For $m_b = m_e$, the electrostatic solution yields the **Buneman instability**
growth rate:

$$\gamma_{\max} \approx \frac{(\pi/8)^{1/3}}{2^{7/6}} \frac{\omega_{pe}}{S^{1/3}}$$

where $S = n_b / n_0$ is the density ratio.

## Derivation

1. Linearize the Vlasov–Poisson system for two cold species.
2. Fourier transform: $(-i\omega + ikv) f_{1s} + (q_s/m_s) E \partial f_{0s}/\partial v = 0$.
3. For cold beams $f_{0s} = n_{0s} \delta(v - v_{0s})$, so $\partial f_{0s}/\partial v$ is singular.
4. Apply the Landau prescription to push the pole off the real axis.
5. Solve the quartic polynomial in $\omega$; unstable roots appear when $v_0 > c_s$.

## Worked Example

> **Threshold:** For an electron beam ($v_0 = 2\times 10^6$ m/s) through
> hydrogen plasma ($n_0 = 10^{18}$ m$^{-3}$), determine if the Buneman instability
> is active.
> $v_0 > c_s = \sqrt{k_B T_e/m_i}$? With $T_e = 1$ eV, $c_s \sim 3\times 10^3$ m/s.
> Since $v_0 \gg c_s$, the beam is super-sonic and the instability is strong.

## Common Mistakes

- **Beam is the only driver.** The background plasma provides the reactive inertia.
- **Ion acoustic instability is the same thing.** It occurs for $v_0 \sim c_s$ in two-species plasmas; Buneman is for $v_0 \gg c_s$ and $m_b \ll m_i$.
- **Landau damping always quenches instabilities.** Near the resonance ($\omega/k \approx v_0$), the sign of $\partial f_0/\partial v$ determines growth.

## Related Concepts

- [Landau Damping](landau-damping.md)
- [Vlasov Equation](../equations/vlasov-equation.md)
- [Plasma Waves](plasma-waves.md)

## Quiz Questions

1. **Conceptual:** Why does a beam–plasma system “prefer” to grow a wave rather
   than simply pass through undisturbed?
2. **Computational:** Derive the threshold condition $v_0 > c_s$ for Buneman.
3. **MCQ:** Which feature distinguishes the streaming instability from pure
   Landau damping?
   - A) Growth rate sign
   - B) Frequency value
   - C) Wavelength
   - D) Magnetic field presence

## Further Reading

- O. Buneman, *Dissipation of Currents in Ionized Media*.
