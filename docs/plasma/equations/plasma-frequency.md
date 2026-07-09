# Plasma Frequency

$$\omega_{pe} = \sqrt{\frac{n_e e^2}{m_e \varepsilon_0}}$$

*Source lecture:* pc368_lec03_frequency, pc368_lec01_intro

## Physical Meaning

The plasma frequency is the natural angular oscillation frequency of electrons
sloshing back and forth against a stationary ion background. It sets the lowest
frequency at which electrostatic oscillations can propagate in an unmagnetized
plasma and determines the cutoff for electromagnetic wave transmission.

## Variable Definitions

| Symbol | Definition | SI Units |
|--------|------------|----------|
| $n_e$ | Electron number density | m$^{-3}$ |
| $e$ | Elementary charge | C |
| $m_e$ | Electron mass | kg |
| $\varepsilon_0$ | Vacuum permittivity | F m$^{-1}$ |

## Assumptions

- Ions are stationary on the electron timescale ($m_i \gg m_e$).
- No background magnetic field.
- Linear, collisionless response.
- Isothermal or adiabatic electrons ($\gamma_e = 1$ or $5/3$).

## Derivation

Combine electron continuity, momentum, and Poisson:

$$\frac{\partial n}{\partial t} + n_0 \nabla\cdot\mathbf{u} = 0$$

$$m_e \frac{\partial \mathbf{u}}{\partial t} = -e \nabla\phi$$

$$\nabla^2\phi = -\frac{e}{\varepsilon_0}(n - n_0)$$

Assume $u \sim e^{i(kx - \omega t)}$ and eliminate $u$ and $n$:

$$\frac{\omega^2}{\omega_{pe}^2} = 1 + \frac{3 k^2 v_{te}^2}{\omega_{pe}^2}$$

Cold limit ($T_e \to 0$) gives $\omega = \omega_{pe}$.

## Applications

- **Radio blackout:** Re-entry plasma sheath density exceeds $n_c = \varepsilon_0 m_e \omega^2/e^2$
  for communication frequencies.
- **Langmuir probes:** Oscillations at $f_{pe}$ appear in IV characteristics.
- **Wave propagation:** Dispersion relations $\omega^2 = \omega_{pe}^2 + c^2 k^2$ govern
  EM waves in plasma.

## Connections to Other Equations

- [Debye Length](../equations/debye-length.md): $\lambda_D = v_{te}/\omega_{pe}$.
- [Langmuir Waves](../concepts/langmuir-waves.md): Cold limit of dispersion.
- [Alfvén Speed](../equations/alfven-velocity.md): Ratio $\omega_{pe}/\Omega_{ce}$ determines
  X-mode cutoff.
