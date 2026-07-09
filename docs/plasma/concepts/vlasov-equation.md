# Vlasov Equation

*Source lecture(s):* [pc368_lec04_vlasov, pc368_lec12_landau_damping](../lectures.md)

## Intuition

In a collisionless plasma, particles stream freely through the electromagnetic
field. The Vlasov equation tells us how the 6-dimensional phase-space density
$f(\mathbf{r}, \mathbf{v}, t)$ evolves without assuming thermodynamic
equilibrium. It is the kinetic theory backbone of plasma physics.

## Formal Definition

The **Vlasov equation** is the collisionless Boltzmann equation:

$$
\frac{\partial f}{\partial t} + \mathbf{v}\cdot\frac{\partial f}{\partial \mathbf{r}}
+ \frac{q}{m}\bigl(\mathbf{E} + \mathbf{v}\times\mathbf{B}\bigr)\cdot
\frac{\partial f}{\partial \mathbf{v}} = 0
$$

It states that $df/dt = 0$ along particle trajectories in phase space.

## Mathematical Formulation

The fields are self-consistently coupled via Maxwell’s equations:

$$
\nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0}, \qquad
\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial \mathbf{E}}{\partial t}
$$

with

$$
\rho = \sum_s q_s \int f_s \, d^3v, \qquad
\mathbf{J} = \sum_s q_s \int \mathbf{v}\, f_s \, d^3v.
$$

## Derivation

Start from Liouville’s theorem: in the absence of collisions, phase-space
density is conserved along Hamiltonian trajectories. Write the Hamiltonian for a
charged particle in EM fields, $H = \frac{1}{2}m v^2 + q\phi - q\mathbf{A}\cdot\mathbf{v}$,
and apply the chain rule:

$$
\frac{df}{dt} = \frac{\partial f}{\partial t} + \dot{\mathbf{r}}\cdot\frac{\partial f}{\partial \mathbf{r}}
+ \dot{\mathbf{p}}\cdot\frac{\partial f}{\partial \mathbf{p}} = 0.
$$

Using Lorentz force $\dot{\mathbf{v}} = (q/m)(\mathbf{E} + \mathbf{v}\times\mathbf{B})$
produces the Vlasov equation.

## Worked Example

> **Landau damping seed:** Consider a one-dimensional electrostatic perturbation
> with potential $\phi(x,t) = \phi_0 e^{i(kx - \omega t)}$. Linearize the
> Vlasov–Poisson system and find the dispersion relation.

Linearize $f = f_0(v) + f_1$ and $\phi$. Fourier transforming yields
$(-i\omega + ikv) f_1 + (e/m_e)\phi_0 \delta f_0/\delta v = 0$. Solving for
$f_1$, inserting into Poisson, and closing with $\varepsilon(\omega,k) =
1 + \chi_e = 0$ gives the dielectric function. The solution is obtained by
integrating along the Landau contour.

## Common Mistakes

- **Vlasov is not the same as fluid equations.** Fluid equations are velocity
  moments; Vlasov retains the full velocity dependence.
- **Collisions are ignored completely.** Resistivity, Landau damping, and wave
  particle interactions arise from microphysics beyond the collisionless
  hypothesis.
- **Fields are not given a priori.** They must be solved self-consistently.

## Related Concepts

- [Landau Damping](landau-damping.md)
- [MHD](mhd.md)
- [Plasma Waves](plasma-waves.md)
- [Streaming Instability](streaming-instability.md)

## Quiz Questions

1. **Conceptual:** Why does $df/dt = 0$ hold even though particles feel forces?
2. **Computational:** Compute the linear Landau damping rate for a Maxwellian
   plasma with $T_e = 1$ keV and $\lambda_D = 10^{-3}$ m.
3. **MCQ:** Which Maxwell equation closes the Vlasov–Maxwell system?
   - A) $\nabla\cdot\mathbf{B} = 0$
   - B) $\nabla\cdot\mathbf{E} = \rho/\varepsilon_0$
   - C) $\nabla\times\mathbf{E} = -\partial \mathbf{B}/\partial t$
   - D) All of the above

## Further Reading

- R. Betti & O. Manz, *Notes on Kinetic Theory of Plasmas*.
- N. A. Krall & A. W. Trivelpiece, *Principles of Plasma Physics*.
