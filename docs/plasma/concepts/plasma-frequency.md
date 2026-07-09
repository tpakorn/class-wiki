# Plasma Frequency

*Source lecture:* pc368_lec03_frequency

## Intuition

Pluck an electron cloud away from the ion background and it will oscillate. The
natural frequency of this sloshing is the **electron plasma frequency** $\omega_{pe}$.
It sets the timescale for virtually every electrostatic process in a plasma,
from Langmuir waves to Landau damping.

## Formal Definition

For a cold electron–ion plasma with stationary ions:

$$\omega_{pe} = \sqrt{\frac{n_e e^2}{m_e \varepsilon_0}}$$

where $n_e$ is the electron number density.

## Mathematical Formulation

Displace electrons by a small distance $x$ relative to the fixed ion background.
The charge imbalance creates an electric field $E = n_e e x / \varepsilon_0$
(from Gauss’s law). Newton’s second law for the electron fluid gives:

$$m_e \ddot{x} = -e E = -\frac{n_e e^2}{\varepsilon_0} x$$

This is simple harmonic motion with frequency $\omega = \sqrt{n_e e^2/(m_e \varepsilon_0)}$.

## Derivation

1. Linearize continuity, momentum, and Poisson equations about a uniform
   equilibrium with stationary ions.
2. For isothermal electrons ($T_e$ constant), momentum equation gives
   $m_e \partial v_e / \partial t = -e E$.
3. Combining with $\partial n_1 / \partial t + n_0 \nabla \cdot v_e = 0$
   and $\nabla \cdot E = e n_1 / \varepsilon_0$, eliminate $v_e$ and $n_1$.
4. The result is the wave equation $\nabla^2 E = (\omega_{pe}^2 / c^2) E$, or
   more precisely, $\omega^2 = \omega_{pe}^2 + c^2 k^2$ for electromagnetic
   disturbances.

## Worked Example

> **Problem:** What is $\omega_{pe}$ in the solar corona ($n_e \sim 10^{15}\,\text{m}^{-3}$)?

$\omega_{pe} = \sqrt{10^{15} \times (1.6\times 10^{-19})^2 / (9.11\times 10^{-31} \times 8.85\times 10^{-12})} \approx 5.6\times 10^8\,\text{rad/s}$
($f_{pe} \approx 89$ MHz).

## Common Mistakes

- **$\omega_{pe}$ depends only on density.** Confirm before using.
- **The ion plasma frequency matters for high-frequency electromagnetic waves.**
- **Plasma oscillation is not a sound wave.** It is an electrostatic Langmuir mode.

## Related Concepts

- [Plasma](plasma.md)
- [Debye Length](../equations/debye-length.md)
- [Langmuir Waves](langmuir-waves.md)
- [Ion Acoustic Wave](ion-acoustic-wave.md)

## Quiz Questions

1. **Conceptual:** If you suddenly removed all ions from a plasma, what would
   the electron frequency become?
2. **Computational:** Compute $\omega_{pe}$ for a dusty plasma with
   $n_e = 10^{12}\,\text{m}^{-3}$.
3. **MCQ:** For which of these parameters does $\omega_{pe}$ increase?
   - A) Lowering $n_e$
   - B) Increasing $m_e$
   - C) Increasing $T_e$
   - D) Increasing $n_e$

## Further Reading

- T. J. M. Boyd & J. J. Sanderson, *Plasma Dynamics via Atoms*.
