# MHD Equilibrium

*Source lecture(s):* [pc368_lec14_mhd_equilibrium](../lectures.md)

## Intuition

A magnetic confinement device (tokamak, stellarator, Z-pinch) can only confine
plasma if the outward pressure gradient is balanced by the inward magnetic tension.
This static balance is **MHD equilibrium**. Finding the self-consistent
$\mathbf{B}(\mathbf{r})$ and $p(\mathbf{r})$ that satisfy $\mathbf{J}\times\mathbf{B} = \nabla p$
is a central problem in fusion energy.

## Formal Definition

An equilibrium solution of the MHD force-balance equation satisfies:

$$\frac{\mathbf{J}\times\mathbf{B}}{\mu_0} = \nabla p$$

with $\nabla\cdot\mathbf{B} = 0$ and $\mathbf{J} = (1/\mu_0)\nabla\times\mathbf{B}$.

## Mathematical Formulation

For axisymmetric systems (tokamaks), the **Grad–Shafranov equation** describes
flux surfaces:

$$\Delta^* \psi + \mu_0 R^2 \frac{dp}{d\psi} + F \frac{dF}{d\psi} = 0$$

where $\psi(R,Z)$ is the poloidal flux stream function and $F(R,\psi) = RB_\phi$.

## Derivation

1. Start from $\mathbf{J}\times\mathbf{B} = \nabla p$.
2. Assume static equilibrium ($\partial/\partial t = 0$) and no flow ($\mathbf{U}=0$).
3. Take the curl of both sides and use $\nabla\times\mathbf{B} = \mu_0\mathbf{J}$.
4. Substitute $\nabla\times(\mathbf{J}\times\mathbf{B}) = \nabla(\mathbf{J}\cdot\mathbf{B}) - \mathbf{J}(\nabla\cdot\mathbf{B}) - (\mathbf{B}\cdot\nabla)\mathbf{J} + (\mathbf{J}\cdot\nabla)\mathbf{B}$.
   With $\nabla\cdot\mathbf{B}=0$ and constant $p$-surfaces, simplify.
5. In axisymmetry ($\partial/\partial \phi = 0$), the Grad–Shafranov equation
   follows.

## Worked Example

> **Circular tokamak:** Assume $\psi = \psi(r)$ with $r$ the minor radius.
> The poloidal field is $B_\theta = (1/R)\partial\psi/\partial r$.
> Pressure balance $d p/dr = B_\theta B_\phi/\mu_0$ gives a natural profile
> $p(r) = p_0 (1 - r^2/a^2)^2$ compatible with a parabolic current density.

## Common Mistakes

- **Ignoring the J×B force.** Pressure gradients alone cannot confine a plasma.
- **Treating all equilibria as 1D.** Shafranov shift and triangularity are
  inherently 2D effects.
- **Forgetting the bootstrap current.** Neoclassical physics contributes a
  self-generated current important for steady-state tokamaks.

## Related Concepts

- [MHD](mhd.md)
- [MHD Instability](mhd-instability.md)
- [Frozen-in Theorem](frozen-in-theorem.md)

## Quiz Questions

1. **Conceptual:** Why can’t a straight Z-pinch achieve high-β equilibrium?
2. **Computational:** For a force-free field $\mathbf{J} = \alpha\mathbf{B}$,
   show that $\nabla^2\psi + \alpha^2\psi = 0$ in cylindrical geometry.
3. **MCQ:** The Grad–Shafranov equation requires:
   - A) Time dependence
   - B) Axisymmetry
   - C) $\nabla\cdot\mathbf{J} \neq 0$
   - D) Zero resistivity

## Further Reading

- J. P. Freidberg, *Plasma Physics and Fusion Energy*.
