# Magnetohydrodynamics (MHD)

*Source lectures:* pc368_lec05_mhd

## Intuition

When a plasma is dense and cool enough that particle collisions are frequent,
we can forget individual particle orbits and treat the plasma as a single
conducting fluid. This is **magnetohydrodynamics** (MHD). It is the workhorse
theory for fusion reactors, solar flares, and interstellar dynamics.

## Formal Definition

MHD is the one-fluid theory obtained by taking the first few velocity moments of
the Vlasov equation and imposing a **scalar** pressure and Ohm’s law closure.

## Mathematical Formulation

**Continuity:**

$$\frac{\partial \rho}{\partial t} + \nabla\cdot(\rho \mathbf{U}) = 0$$

**Momentum (Navier–Stokes):**

$$\rho\frac{D\mathbf{U}}{Dt} = \mathbf{J}\times\mathbf{B} - \nabla p + \mu \nabla^2 \mathbf{U}$$

**Induction:**

$$\frac{\partial \mathbf{B}}{\partial t} = \nabla\times(\mathbf{U}\times\mathbf{B}) + \eta \nabla^2 \mathbf{B}$$

**Ohm’s law:**

$$\mathbf{E} + \mathbf{U}\times\mathbf{B} = \eta \mathbf{J}$$

## Derivation

1. **Continuity:** Integrate the zeroth velocity moment of the Boltzmann equation.
   The collisionless form becomes the fluid continuity equation.
2. **Momentum:** Multiply Boltzmann by $m\mathbf{v}$ and integrate. The pressure
   tensor is closed by $P_{ij} \to p \delta_{ij}$ (isotropic pressure).
3. **Induction:** Use $\mathbf{E} + \mathbf{U}\times\mathbf{B} = \eta\mathbf{J}$
   and Faraday’s law $\partial \mathbf{B}/\partial t = -\nabla\times\mathbf{E}$.
4. **Closure:** Assume the equation of state $p = n k_B T$ and an isentropic or
   isothermal relation.

## Worked Example

> **Z-pinch equilibrium:** A cylindrical plasma column carries current $I$ along
> $\hat{z}$. The azimuthal magnetic field is $B_\theta = \mu_0 I/(2\pi r)$.
> The Lorentz force is inward: $\mathbf{J}\times\mathbf{B} = -(B_\theta^2/\mu_0)\hat{r}$.
> For force balance with pressure gradient $dp/dr = -B_\theta^2/\mu_0$:
> Integrate to find $p(r) = p_0 - (\mu_0 I^2/8\pi^2)\ln(r)$. This profile shows
> that peak pressure is at the axis and falls off logarithmically.

## Common Mistakes

- **Treating MHD as always valid.** MHD breaks down when $\rho \to 0$, when
  kinetic effects matter, or when the Hall term is important.
- **Neglecting energy equation.** Stating $p$ without its evolution equation loses
  information about heating and cooling.
- **Assuming ideal MHD in reconnection.** Ideal MHD forbids reconnection;
  resistivity $\eta$ is essential.

## Related Concepts

- [Frozen-in Theorem](frozen-in-theorem.md)
- [Plasma](plasma.md)
- [MHD Equilibrium](mhd-equilibrium.md)
- [Magnetic Reconnection](magnetic-reconnection.md)

## Quiz Questions

1. **Conceptual:** Why does the induction equation look like the advection of
   a passive scalar?
2. **Computational:** For a tokamak with $n = 10^{20}\,\text{m}^{-3}$, $T = 1$ keV,
   and $B = 2$ T, estimate $v_A$.
3. **MCQ:** In ideal MHD ($\eta=0$), what happens to magnetic field lines?
   - A) Diffuse through the plasma
   - B) Move with the fluid (frozen-in)
   - C) Decay exponentially
   - D) Become parallel to velocity

## Further Reading

- J. P. Freidberg, *Ideal MHD*.
- P. A. Davidson, *An Introduction to Magnetohydrodynamics*.
