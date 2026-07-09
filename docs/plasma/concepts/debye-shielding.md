# Debye Shielding

*Source lectures:* pc368_lec01_intro, pc368_lec02_debye

## Intuition

Drop a charged test particle into a plasma, and the mobile electrons and ions
will rearrange themselves so that outside a small radius the electric potential
is almost zero. This is the plasma analog of electrostatic screening in metals,
except that the “perfect conductor” is collective motion rather than conduction
electrons.

## Formal Definition

Debye shielding is the exponential attenuation of the electric potential produced
by an external charge embedded in a Maxwellian plasma. The shielding length is the
Debye length:

$$\lambda_D = \sqrt{\frac{\varepsilon_0 k_B T_e}{n_e e^2}}$$

## Mathematical Formulation

Start from Poisson’s equation:

$$\nabla^2 \phi = -\frac{\rho_{\text{ext}}}{\varepsilon_0} - \frac{e(n_i - n_e)}{\varepsilon_0}$$

For a singly charged, stationary source $\rho_{\text{ext}} = Ze \delta(\mathbf{r})$:

$$\nabla^2 \phi - \frac{\phi}{\lambda_D^2} = -\frac{Ze}{\varepsilon_0} \delta(\mathbf{r})$$

The Green’s function gives the shielded Coulomb potential:

$$\phi(r) = \frac{Ze}{4\pi\varepsilon_0 r} e^{-r/\lambda_D}$$

## Derivation

1. Assume the external charge $Ze$ is fixed.
2. Electrons respond via Boltzmann distribution: $n_e = n_0 \exp(e\phi/k_B T_e)$.
3. Ions remain essentially immobile because $m_i \gg m_e$.
4. Linearize for $|e\phi| \ll k_B T_e$: $n_e \approx n_0(1 + e\phi/k_B T_e)$.
5. Insert into Poisson: $\nabla^2 \phi - \phi/\lambda_D^2 = -Ze\delta/\varepsilon_0$.
6. Fourier transform or use spherical symmetry to obtain the Yukawa potential.

## Worked Example

> A dust grain of charge $Q = 10^4 e$ sits in a plasma with $n_e = 10^{16}\,\text{m}^{-3}$
> and $T_e = 1$ eV. Find the potential at $r = 10 \lambda_D$.

1. $\lambda_D \approx 2.3\times 10^{-5}\,\text{m}$.
2. At $r = 10\lambda_D$, shielding factor is $e^{-10} \approx 4.5\times 10^{-5}$.
3. Hence the external charge is effectively invisible to distant plasma particles.

## Common Mistakes

- **Debye ≪ L is not a micro-scale phenomenon.** It is a *global* condition; the
  system must be many Debye lengths across.
- **Singularities survive at $r=0$.** Per real charge is singular inside a Debye
  sphere; shielding only works outside.
- **Debye length depends on $T_e$.** Hotter plasma elects a stronger shield.

## Related Concepts

- [Plasma](plasma.md)
- [Quasi-neutrality](quasi-neutrality.md)
- [Ideal Plasma](ideal-plasma.md)
- [Poisson’s Equation in Plasma](poisson-equation.md)

## Quiz Questions

1. **Conceptual:** What is the physical reason that a test charge cannot polarize
   a plasma beyond $\sim \lambda_D$?
2. **Computational:** Derive $\lambda_D$ for argon plasma with $n=10^{18}\,\text{m}^{-3}$
   and $T=0.5$ eV.
3. **MCQ:** In Debye shielding, which species dominates the restoring force?
   - A) Ions
   - B) Electrons
   - C) Both equally
   - D) Neither; it is magnetic

## Further Reading

- Francis F. Chen, *Introduction to Plasma Physics*, Chapter 1.
