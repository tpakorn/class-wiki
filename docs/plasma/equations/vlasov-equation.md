# Vlasov Equation

$$\frac{\partial f}{\partial t} + \mathbf{v}\cdot\frac{\partial f}{\partial \mathbf{r}}
+ \frac{q}{m}\bigl(\mathbf{E} + \mathbf{v}\times\mathbf{B}\bigr)\cdot\frac{\partial f}{\partial \mathbf{v}} = 0$$

*Source lecture:* pc368_lec04_vlasov

## Physical Meaning

The Vlasov equation describes the evolution of the phase-space distribution
function $f(\mathbf{r}, \mathbf{v}, t)$ in a collisionless plasma. It states
that the density of representative points in phase space is conserved along
Hamiltonian trajectories.

## Variable Definitions

| Symbol | Definition | SI Units |
|--------|------------|----------|
| $f$ | Phase-space density | s$^3$ m$^{-6}$ |
| $\mathbf{r}, \mathbf{v}$ | Position and velocity vectors | m, m s$^{-1}$ |
| $q, m$ | Particle charge and mass | C, kg |
| $\mathbf{E}, \mathbf{B}$ | Self-consistent EM fields | V m$^{-1}$, T |
| $t$ | Time | s |

## Assumptions

- **Collisionless:** No binary Coulomb collisions.
- **Kinetic:** Full 6-D phase space; no fluid-closure assumption.
- **Self-consistent:** Fields obey Maxwell’s equations with
  $\rho = \int q f d^3v$, $\mathbf{J} = \int q\mathbf{v} f d^3v$.

## Derivation

Start from Liouville’s theorem: in Hamiltonian dynamics with Hamiltonian $H$,
phase-space density is conserved:

$$\frac{df}{dt} = \frac{\partial f}{\partial t} + \dot{\mathbf{r}}\cdot\frac{\partial f}{\partial \mathbf{r}} + \dot{\mathbf{p}}\cdot\frac{\partial f}{\partial \mathbf{p}} = 0$$

The equations of motion are:

$$\dot{\mathbf{r}} = \frac{\partial H}{\partial \mathbf{p}} = \frac{\mathbf{p}}{m}, \qquad
\dot{\mathbf{p}} = -\frac{\partial H}{\partial \mathbf{r}} = q\bigl(\mathbf{E} + \dot{\mathbf{r}}\times\mathbf{B}\bigr)$$

Since $\dot{\mathbf{r}} = \mathbf{v}$, substituting yields:

$$\frac{Df}{Dt} = \frac{\partial f}{\partial t} + \mathbf{v}\cdot\nabla f + \frac{q}{m}\bigl(\mathbf{E} + \mathbf{v}\times\mathbf{B}\bigr)\cdot\frac{\partial f}{\partial \mathbf{v}} = 0$$

## Applications

- **Linear wave theory:** Langmuir, ion acoustic, and Alfvén waves.
- **Collisionless damping:** Landau damping, two-stream instability.
- **Turbulence:** Gyrokinetic and kinetic simulations.

## Connections to Other Equations

- [Landau Damping](../concepts/landau-damping.md): Solves Vlasov–Poisson eigenfunctions.
- [MHD](../concepts/mhd.md): First moments of Vlasov give fluid equations.
- [Streaming Instability](../concepts/streaming-instability.md): Beam-plasma dispersion from Vlasov.
