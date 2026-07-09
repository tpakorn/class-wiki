# Glossary

## A

**Adiabatic invariant** — A quantity that remains constant when a parameter of a
system changes slowly. In plasma physics, the magnetic moment
$\\mu = m v_\\perp^2/(2B)$ is an adiabatic invariant for a particle gyrating in a
slowly varying magnetic field. See [Adiabatic Invariant](concepts/adiabatic-invariant.md).

**Alfvén speed** — The characteristic speed at which transverse MHD disturbances
propagate along magnetic field lines:
$v_A = B/\\sqrt{\\mu_0 \\rho}$.
See [Alfvén Speed](equations/alfven-velocity.md).

## B

**Boltzmann response** — The relation $n_{e1}/n_0 = e\\phi_1/(k_B T_e)$
describing how electrons redistribute in response to a small electrostatic
potential.

**Bohm criterion** — The condition $v_i \\ge c_s$ at the sheath edge, required
for a stable plasma–wall transition.
See [Plasma Sheath](concepts/plasma-sheath.md).

**Buneman instability** — A two-stream instability that occurs when the electron
drift speed exceeds the ion thermal speed. See [Streaming Instability](concepts/streaming-instability.md).

## C

**Collective parameter** — $\\Lambda = 4\\pi n \\lambda_D^3$, the average number
of electrons inside a Debye sphere. $\\Lambda \\gg 1$ defines an ideal plasma.

**Continuity equation** — $\\partial \\rho/\\partial t + \\nabla\\cdot(\\rho \\mathbf{U}) = 0$,
expressing mass/particle conservation.
See [Continuity Equation](equations/continuity-equation.md).

**Cold plasma** — A plasma model where finite temperature effects are neglected;
only fluid motion and fields are retained.

## D

**Debye length** — The screening length in a plasma:
$\\lambda_D = \\sqrt{\\varepsilon_0 k_B T_e / (n_e e^2)}$.
See [Debye Length](equations/debye-length.md).

**Drift motion** — Particle motion perpendicular to $\\mathbf{B}$ caused by
inhomogeneities or forces: $\\mathbf{E}\\times\\mathbf{B}$ drift, grad-B drift,
curvature drift.
See [Drift Motion](concepts/drift-motion.md).

## E

**Equation of state** — Relation between pressure and density. For isothermal
electrons: $p_e = n_e k_B T_e$; for adiabatic ions: $p_i \\propto n_i^{\\gamma_i}$.

## F

**Frozen-in theorem** — In ideal MHD ($\\eta = 0$), magnetic field lines are
“frozen” into the plasma and move with the fluid velocity $\\mathbf{U}$.
See [Frozen-in Theorem](concepts/frozen-in-theorem.md).

## G

**Grad–Shafranov equation** — The fundamental PDE of axisymmetric MHD
equilibrium: $\\Delta^*\\psi + \\mu_0 R^2 dp/d\\psi + F dF/d\\psi = 0$.
See [Grad–Shafranov Equation](equations/grad-shafranov.md).

## I

**Ideal plasma** — A plasma satisfying $\\lambda_D \\ll L$,
$\\Lambda \\gg 1$, and quasi-neutrality.
See [Ideal Plasma](concepts/ideal-plasma.md).

**Induction equation** — $\\partial \\mathbf{B}/\\partial t =
\\nabla\\times(\\mathbf{U}\\times\\mathbf{B}) + \\eta\\nabla^2\\mathbf{B}$,
describing magnetic field evolution in MHD.
See [Induction Equation](equations/induction-equation.md).

**Ion acoustic wave** — A low-frequency electrostatic wave with dispersion
$\\omega^2 = k^2 c_s^2/(1 + k^2\\lambda_{De}^2)$.
See [Ion Acoustic Wave](concepts/ion-acoustic-wave.md).

## L

**Landau damping** — Collisionless damping of plasma waves due to resonant
wave–particle interaction, governed by $\\partial f_0/\\partial v$ at
$v = \\omega/k$.
See [Landau Damping](concepts/landau-damping.md).

**Langmuir waves** — High-frequency electrostatic electron oscillations with
dispersion $\\omega^2 = \\omega_{pe}^2 + 3k^2 v_{te}^2$.
See [Langmuir Waves](concepts/langmuir-waves.md).

**Larmor radius** — The gyroradius of a charged particle in a magnetic field:
$\\rho_s = m_s v_{\\perp}/(|q_s| B)$.
See [Larmor Radius](concepts/larmor-radius.md).

**Loss cone** — The range of pitch angles for which particles can escape a
magnetic mirror. Particles with $\\sin^2\\theta < B_{\\text{min}}/B_{\\text{max}}$
are lost.
See [Magnetic Mirror](concepts/magnetic-mirror.md).

**Lundquist number** — The magnetic Reynolds number in MHD:
$S = \\mu_0 v_A L/\\eta$.
See [Lundquist Number](equations/lundquist-number.md).

## M

**Magnetic island** — A closed flux region formed during magnetic reconnection,
bounded by separatrices.
See [Magnetic Islands](concepts/magnetic-islands.md).

**Magnetic mirror** — A magnetic configuration where increasing field strength
reflects charged particles, trapping them between two high-field regions.
See [Magnetic Mirror](concepts/magnetic-mirror.md).

**Magnetohydrodynamics (MHD)** — Fluid description of a plasma as a single
conducting fluid coupled to electromagnetic fields.
See [MHD](concepts/mhd.md).

**Magnetized wave** — Electromagnetic wave in a magnetized plasma, classified as
R, L, O, or X mode.
See [Magnetized Waves](concepts/magnetized-waves.md).

## P

**Plasma** — An ionized gas in which collective electromagnetic effects dominate
over binary collisions.
See [Plasma](concepts/plasma.md).

**Plasma approximation** — The condition $\\lambda_D \\ll L$ that allows a plasma
to be treated as a continuous medium.

**Plasma frequency** — The natural electron oscillation frequency:
$\\omega_{pe} = \\sqrt{n_e e^2/(m_e \\varepsilon_0)}$.
See [Plasma Frequency](equations/plasma-frequency.md).

**Plasma parameter** — $\\Lambda = 4\\pi n \\lambda_D^3$; measures the number of
particles in a Debye sphere.

**Plasma wave** — Collective oscillation of a plasma: Langmuir, ion acoustic,
Alfvén, magnetosonic, etc.
See [Plasma Waves](concepts/plasma-waves.md).

**Poisson’s equation** — $\\nabla^2 \\phi = -\\rho/\\varepsilon_0$; relates
charge density to electrostatic potential.
See [Poisson’s Equation](concepts/poisson-equation.md).

## Q

**Quasi-neutrality** — The condition $|n_e - Z n_i| \\ll n_e$ on macroscopic
scales $L \\gg \\lambda_D$.
See [Quasi-neutrality](concepts/quasi-neutrality.md).

## S

**Sound speed** — The characteristic speed of pressure propagation in a plasma:
$c_s = \\sqrt{(\\gamma_e k_B T_e + \\gamma_i k_B T_i)/m_i}$.
See [Sound Speed](concepts/sound-speed.md).

**Sweet–Parker model** — A steady-state MHD reconnection model predicting
$M_A \\sim S^{-1/2}$ for a long thin current sheet.
See [Sweet–Parker Model](concepts/sweet-parker-model.md).

## V

**Vlasov equation** — The collisionless Boltzmann equation for the phase-space
distribution function $f(\\mathbf{r}, \\mathbf{v}, t)$.
See [Vlasov Equation](equations/vlasov-equation.md).

## W

**Waves in plasmas** — See [Plasma Waves](concepts/plasma-waves.md) and
[Magnetized Waves](concepts/magnetized-waves.md).
