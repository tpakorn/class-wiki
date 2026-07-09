# Plasma

*Source lecture(s):* [pc368_lec01_intro](../lectures.md)

## Intuition

More than 99% of the visible universe is plasma. It is not merely a hot gas; it
is an ionized soup of electrons and ions in which long-range Coulomb forces
produce collective behavior. A plasma can sustain oscillations, support waves,
and self-organize into structures that no neutral gas ever could.

## Formal Definition

A **plasma** is an ensemble of charged particles satisfying:

1. The **plasma approximation**: $\lambda_D \ll L$
2. **Quasi-neutrality** on macroscopic scales: $n_e \approx Z n_i$
3. **Collective parameter** $\Lambda = 4\pi n \lambda_D^3 \gg 1$

## Mathematical Formulation

The **Debye length** sets the shielding scale:

$$\lambda_D = \sqrt{\frac{\varepsilon_0 k_B T_e}{n_e e^2}}$$

For a Maxwellian plasma, the **plasma parameter** $\Lambda$ counts the average
number of electrons inside a Debye sphere.

## Derivation

Start from Poisson’s equation for a displaced electron fluid:

$$\nabla^2 \phi = -\frac{e(n_i - n_e)}{\varepsilon_0}$$

With Boltzmann response $n_e = n_0 \exp(e\phi/k_B T_e)$ and linearizing for
$|e\phi| \ll k_B T_e$:

$$\nabla^2 \phi \approx \frac{n_0}{\varepsilon_0} \frac{e\phi}{k_B T_e}$$

The solution is $\phi \propto \exp(-r/\lambda_D)/r$, where $\lambda_D$ is
the Debye length defined above. This exponential screening confirms that
potential disturbances decay on the scale $\lambda_D$.

## Worked Example

> **Problem:** Calculate $\lambda_D$ for a fusion-relevant plasma with
> $n_e = 10^{20}\,\text{m}^{-3}$ and $T_e = 10$ keV.

Steps:
1. Convert $T_e = 10\,\text{keV} = 1.6\times 10^{-15}\,\text{J}$.
2. Insert into $\lambda_D = \sqrt{\varepsilon_0 k_B T_e / (n_e e^2)}$.
3. Result: $\lambda_D \approx 2.3\times 10^{-5}\,\text{m} = 23\,\mu\text{m}$.
4. $\Lambda \approx 4\pi (10^{20}) (2.3\times 10^{-5})^3 \sim 10^{10} \gg 1$.

The plasma is weakly coupled and strongly collective.

## Common Mistakes

- **Confusing temperature with “heat.”** In plasma physics, $T$ refers to the
  average kinetic energy per degree of freedom, not the thermodynamic temperature
  of a neutral gas.
- **Ignoring quasi-neutrality.** On scales $L \gg \lambda_D$, the electric field
  is too weak to separate charges macroscopically.
- **Using the wrong species.** Debye shielding is dominated by the most mobile
  species: usually the electrons.

## Related Concepts

- [Debye Shielding](debye-shielding.md)
- [Plasma Frequency](../equations/plasma-frequency.md)
- [Ideal Plasma](ideal-plasma.md)
- [Quasi-neutrality](quasi-neutrality.md)

## Quiz Questions

1. **Conceptual:** Why does a plasma support longitudinal oscillations (plasma
   waves) while an ordinary collisional gas does not?
2. **Computational:** The solar wind at 1 AU has $n \sim 5\times 10^6\,\text{m}^{-3}$
   and $T \sim 10^5$ K. Estimate the Debye length.
3. **MCQ:** Which condition is NOT part of the definition of an ideal plasma?
   - A) $\lambda_D \ll L$
   - B) $\omega_{pe} \gg \omega_{pi}$
   - C) $\Lambda \ll 1$
   - D) Quasi-neutrality

## Further Reading

- F. F. Chen, *Introduction to Plasma Physics and Controlled Fusion* (Springer).
- R. O. Dendy, *Plasma Dynamics* (Oxford).
