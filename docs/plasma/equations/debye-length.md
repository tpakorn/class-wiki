# Debye Length

$$\lambda_D = \sqrt{\frac{\varepsilon_0 k_B T_e}{n_e e^2}}$$

*Source lecture(s):* [pc368_lec01_intro, pc368_lec02_debye](../lectures.md)

## Physical Meaning

The Debye length is the distance over which a charge disturbance in a plasma is
screened by the rearrangement of electrons and ions. It is the plasma analog of
the Thomas–Fermi screening length in metals, but here the “screening” is
collective and thermal.

## Variable Definitions

| Symbol | Definition | SI Units |
|--------|------------|----------|
| $\varepsilon_0$ | Vacuum permittivity | F m$^{-1}$ |
| $k_B$ | Boltzmann constant | J K$^{-1}$ |
| $T_e$ | Electron temperature | K (or eV × 11605) |
| $n_e$ | Electron number density | m$^{-3}$ |
| $e$ | Elementary charge | C |

## Assumptions

- Plasma is **quasi-neutral** on scales $L \gg \lambda_D$.
- Electrons obey a Boltzmann distribution; ions are immobile.
- The perturbation is small: $|e\phi| \ll k_B T_e$.
- The medium is **unmagnetized** (or B-fields do not affect radial shielding).

## Derivation

Start from Poisson’s equation for a purely electrostatic potential $\phi(r)$ in
spherical symmetry:

$$\frac{1}{r^2} \frac{d}{dr}\Bigl(r^2 \frac{d\phi}{dr}\Bigr) = -\frac{\rho}{\varepsilon_0}$$

For a pure electron plasma responding to a positive test charge $+Ze$:

$$\rho = e\bigl(Z\delta(\mathbf{r}) - n_e\bigr)$$

with Boltzmann response $n_e = n_0 \exp(e\phi/k_B T_e)$. Linearizing:

$$n_e \approx n_0\Bigl(1 + \frac{e\phi}{k_B T_e}\Bigr)$$

Insert into Poisson and assume $r > 0$ (outside the singular source):

$$\frac{1}{r^2} \frac{d}{dr}\Bigl(r^2 \frac{d\phi}{dr}\Bigr) - \frac{\phi}{\lambda_D^2} = 0$$

The Green’s function is the Yukawa potential:

$$\phi(r) = \frac{Ze}{4\pi\varepsilon_0 r} e^{-r/\lambda_D}$$

## Applications

- **Quasi-neutrality:** Any macroscopic plasma region $L \gg \lambda_D$ is
  effectively neutral.
- **RF shielding:** High-frequency electromagnetic waves reflect at critical
  densities $n_c > \varepsilon_0 m_e \omega^2/e^2$ inside $\sim \lambda_D$.
- **Collisionless damping:** The Landau length scale is $k\lambda_D \sim 1$.

## Connections to Other Equations

- [Plasma Frequency](../equations/plasma-frequency.md): $\omega_{pe}^2 = n_e e^2/(m_e \varepsilon_0)$,
  and $\lambda_D = v_{te}/\omega_{pe}$.
- [Vlasov Equation](../equations/vlasov-equation.md): Linearization uses $\lambda_D$ as the
  small parameter.
- [Langmuir Waves](../concepts/langmuir-waves.md): $\omega^2 = \omega_{pe}^2 + 3 k^2 v_{te}^2$.
