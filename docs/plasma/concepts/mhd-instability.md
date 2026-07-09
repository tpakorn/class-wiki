# MHD Instability

*Source lecture(s):* [pc368_lec15_dynamics_instability](../lectures.md)

## Intuition

An MHD equilibrium is a delicate balance: magnetic pressure bends inward,
thermal pressure pushes outward. If the plasma “knows” that there is free energy
stored in a non-uniform pressure or current profile, tiny perturbations can grow
exponentially, releasing that energy violently. These modes—kink, ballooning,
tearing—limit the performance of magnetic confinement devices.

## Formal Definition

An MHD configuration is **unstable** if an infinitesimal perturbation $\boldsymbol{\xi}(\mathbf{r}, t)
= \boldsymbol{\xi}_0 e^{\gamma t}$ grows ($\gamma^2 > 0$) in time, converting
magnetic or thermal energy into kinetic energy.

## Mathematical Formulation

The **energy principle** states that the potential energy change due to a
displacement $\boldsymbol{\xi}$ is:

$$\delta W = \frac{1}{2}\int_V \Bigl[ \frac{|\mathbf{B}\cdot\nabla\times(\boldsymbol{\xi}\times\mathbf{B})|^2}{\mu_0} + \gamma p |\nabla\cdot\boldsymbol{\xi}|^2 + \dots \Bigr] dV$$

If $\delta W < 0$ for any admissible $\boldsymbol{\xi}$, the equilibrium is unstable.

## Derivation

1. Perturb the MHD equations: $\mathbf{B} \to \mathbf{B} + \delta\mathbf{B}$,
   $\mathbf{U} \to \delta\mathbf{U}$, etc.
2. Combine perturbed induction and Faraday’s laws to get $\delta\mathbf{B}$.
3. Derive the equation of motion for $\boldsymbol{\xi}$.
4. Multiply by $\boldsymbol{\xi}^*$ and integrate over the volume.
5. After boundary-condition integration by parts, obtain the boundary-value
   problem whose eigenvalues $\gamma^2$ reveal stability.

## Worked Example

> **Current-driven kink:** A Z-pinch with uniform current profile ($\mathbf{J}
= J_0 \hat{z}$) is unstable to the m=1 kink if the safety factor $q < 1$.
> Because $q = (r B_z)/(R B_\theta) < 1$ implies the field line wraps around the
> axis less than once per poloidal circuit, the field lines can open into a
> helical shape that shortens the path, releasing magnetic energy.

## Common Mistakes

- **Stability = existence of equilibrium.** Many solutions of $\mathbf{J}\times\mathbf{B}=\nabla p$
  are unstable to small perturbations.
- **Only ideal MHD matters.** Resistive instabilities (tearing modes) require
  $\eta \neq 0$ and are not captured by ideal energy principle.
- **Large-$n$ modes are always stable.** Ballooning modes at high toroidal
  mode numbers can dominate in high-$\beta$ tokamaks.

## Related Concepts

- [MHD Equilibrium](mhd-equilibrium.md)
- [Magnetic Reconnection](magnetic-reconnection.md)
- [Sweet–Parker Model](sweet-parker-model.md)

## Quiz Questions

1. **Conceptual:** Why does the kink instability grow faster at higher current?
2. **Computational:** For a step-function current profile, compute the linear
   growth rate of the m=1 internal kink.
3. **MCQ:** The energy principle applies to:
   - A) Ideal MHD only
   - B) Resistive MHD only
   - C) Both ideal and resistive
   - D) Neither

## Further Reading

- B. Coppi, *MHD Stability Theory*, review in *Phys. Fluids*.
