# Landau Dispersion Relation

$$1 + \frac{1}{k^2 \lambda_D^2} \Bigl[ 1 + \zeta Z(\zeta) \Bigr] = 0$$

*Source lecture:* pc368_lec12_landau_damping

## Physical Meaning

The Landau dispersion relation is the condition for electrostatic normal modes in
a plasma with a given equilibrium distribution $f_0(v)$. It embeds the physics of
resonant wave–particle interactions via the plasma dispersion function $Z(\zeta)$.

## Variable Definitions

| Symbol | Definition | SI Units |
|--------|------------|----------|
| $k$ | Wavenumber | m$^{-1}$ |
| $\lambda_D$ | Debye length | m |
| $\zeta = \omega/(k\sqrt{2}v_{te})$ | Normalized phase speed | dimless |
| $Z(\zeta)$ | Plasma dispersion function | dimless |
| $v_{te} = \sqrt{k_B T_e/m_e}$ | Electron thermal speed | m s$^{-1}$ |

## Assumptions

- One-dimensional electrostatic perturbation.
- Collisionless Vlasov–Poisson system.
- Maxwellian background $f_0(v) = n_0/\sqrt{2\pi}v_{te} \exp(-v^2/v_{te}^2)$.

## Derivation

1. Fourier-transform Vlasov in time and space.
2. Integrate over velocity: $\chi_e = (e^2/\varepsilon_0 k^2) \int \frac{\partial f_{0e}/\partial v}{\omega - k v} dv$.
3. Close with Poisson: $1 + \chi_e = 0$.
4. The pole at $v = \omega/k$ is pushed below the real axis (Landau contour
   $v \to v - i0^+$).
5. Integration yields $Z(\zeta) = \pi^{1/2} \int_{-\infty}^{\infty} \exp(-t^2)/(t-\zeta) dt$.

## Applications

- **Landau damping rate:** Weak-damping limit gives $\gamma/\omega$ formula.
- **Bump-on-tail:** $\partial f_0/\partial v > 0$ gives growth.
- **Dispersion broadening:** $k\lambda_D \sim 1$ regime for satellite plasma
  wave instruments.

## Connections to Other Equations

- [Debye Length](../equations/debye-length.md): Appears in normalization.
- [Landau Damping](../concepts/landau-damping.md): Physical interpretation.
- [Vlasov Equation](../equations/vlasov-equation.md): Starting point.
