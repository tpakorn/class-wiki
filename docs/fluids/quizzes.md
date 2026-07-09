# Quizzes · Fluid Mechanics

Question bank organized by difficulty. Every concept page also carries its own quiz —
these are integrative questions spanning multiple topics.

## Easy

**E1 (conceptual).** Why does pressure in a lake depend on depth but not on the lake's
width?

??? success "Answer"
    [Hydrostatic equilibrium](concepts/hydrostatic-equilibrium.md) is a *local* balance:
    $dP/dy = \rho g$ integrates over depth only. Each column of fluid supports its own
    weight — neighboring columns push sideways equally and cancel.

**E2 (computational).** A hydraulic lift has pistons of area 0.01 m² and 1 m². What
force on the small piston supports a 1000 kg car on the large one?

??? success "Answer"
    Equal pressure ([Pascal](concepts/pressure.md)):
    $F_1 = F_2 A_1/A_2 = 9800 \times 0.01 = 98$ N — about 10 kg-force.

**E3 (MCQ).** Water flows through a pipe that doubles in diameter. The speed:

- (a) doubles  (b) halves  (c) quarters  (d) quadruples

??? success "Answer"
    **(c).** [Continuity](equations/continuity-equation.md): $A \propto d^2$ quadruples,
    so $v$ drops 4×.

**E4 (conceptual).** A ship made of steel floats, but a steel ball sinks. Reconcile.

??? success "Answer"
    Floating depends on *average* density of the displaced-volume envelope
    ([buoyancy](concepts/buoyancy.md)). The hull encloses mostly air, so the ship
    displaces its weight in water long before submerging.

**E5 (MCQ).** The no-slip condition says that at a stationary solid wall:

- (a) pressure vanishes  (b) fluid velocity is zero  (c) shear stress is zero  (d) vorticity is zero

??? success "Answer"
    **(b)** — see [viscosity](concepts/viscosity.md). Consequently shear stress and
    vorticity are typically *largest* at walls.

## Medium

**M1 (computational).** A wind of 15 m/s blows over a flat warehouse roof of 500 m²
($\rho_\text{air} = 1.2\ \text{kg/m}^3$). Estimate the net upward force if the interior
is at rest.

??? success "Answer"
    [Bernoulli](equations/bernoulli-equation.md):
    $\Delta p = \frac12\rho v^2 = 135$ Pa; $F = 135 \times 500 = 67.5$ kN — about
    6.9 tonnes of lift.

**M2 (computational).** Oil ($\mu = 0.1$ Pa·s, $\rho = 900\ \text{kg/m}^3$) flows at
$Q = 10^{-4}\ \text{m}^3/\text{s}$ through a 2 cm-diameter, 10 m pipe. Find the
pressure drop and verify the flow is laminar.

??? success "Answer"
    [Hagen–Poiseuille](examples/hagen-poiseuille-flow.md):
    $\Delta P = \frac{8\mu L Q}{\pi R^4} = \frac{8\times0.1\times10\times10^{-4}}{\pi\times(0.01)^4} \approx 25.5$ kPa.
    Mean speed $v = Q/A = 0.318$ m/s;
    $Re = \rho v d/\mu = 900\times0.318\times0.02/0.1 \approx 57 \ll 2300$. Laminar.

**M3 (conceptual).** Explain why a spinning bucket of water makes a *parabolic*
surface, not a conical or spherical one.

??? success "Answer"
    [Rigid-body rotation](concepts/fluid-in-rigid-body-motion.md): the isobar condition
    gives $dz/dr = r\omega^2/g$ — slope growing *linearly* with $r$ integrates to
    $z \propto r^2$. Centripetal demand grows linearly outward; only a parabola's tilt
    keeps pace.

**M4 (computational).** Use the [Buckingham Pi theorem](concepts/buckingham-pi-theorem.md)
to show the drag on a submarine depends on only two dimensionless groups, and name
them.

??? success "Answer"
    $F = \phi(\rho, v, L, \mu)$: $n = 5$, $k = 3$ ⇒ 2 groups:
    $C_D = F/(\rho v^2 L^2)$ and $Re = \rho v L/\mu$. Hence $C_D = f(Re)$.

**M5 (MCQ).** Across a stationary normal shock, which quantity *decreases*?

- (a) pressure  (b) temperature  (c) density  (d) flow speed

??? success "Answer"
    **(d)** — see [Rankine–Hugoniot](equations/rankine-hugoniot-conditions.md);
    entropy demands compression and deceleration.

## Hard

**H1 (computational).** A 2 mm-wavelength ripple and a 2 m-wavelength wave both travel
on deep water. Which is faster and why? ($\gamma = 0.074$ N/m)

??? success "Answer"
    Gravity–capillary dispersion
    ([interface relation](equations/interface-dispersion-relation.md)):
    $c^2 = g/k + \gamma k/\rho$. For $\lambda = 2$ m: $c \approx 1.77$ m/s
    (gravity-dominated). For $\lambda = 2$ mm: $k = 3142$, $c^2 = 0.0031 + 0.233$,
    $c \approx 0.49$ m/s. The long wave is faster; capillary waves are slow but their
    speed *rises* again at even shorter wavelengths (minimum ≈ 0.23 m/s at
    $\lambda \approx 1.7$ cm).

**H2 (computational).** Kolmogorov: a kitchen mixer dissipates 50 W in 0.5 kg of water
($\nu = 10^{-6}\ \text{m}^2/\text{s}$). Estimate the smallest eddy size.

??? success "Answer"
    $\varepsilon = 50/0.5 = 100\ \text{W/kg} = 100\ \text{m}^2/\text{s}^3$;
    $\eta = (\nu^3/\varepsilon)^{1/4} = (10^{-18}/100)^{1/4} = 10^{-5}$ m — ten
    microns. See [energy cascade](concepts/energy-cascade.md).

**H3 (conceptual).** The linear [Kelvin–Helmholtz](concepts/kelvin-helmholtz-instability.md)
growth rate increases without bound as $k \to \infty$ for an ideal vortex sheet. Give
two physical effects that regularize this, and the scaling of each.

??? success "Answer"
    (1) Surface tension: adds $-\gamma k^3/(\rho_1+\rho_2)$ under the radicand —
    stabilizes $k$ above a cutoff. (2) Finite shear-layer thickness $\delta$ (or
    viscosity $\sim \mu k^2$): modes with $k\delta \gtrsim 1$ see a smooth profile, not
    a jump, capping growth near $k \sim 1/\delta$.

**H4 (computational).** A supernova releases $10^{44}$ J into interstellar gas of
density $2\times10^{-21}\ \text{kg/m}^3$. Using
[Sedov–Taylor](examples/trinity-blast-wave.md), estimate the remnant radius after
1000 years.

??? success "Answer"
    $t = 3.15\times10^{10}$ s;
    $R \sim (Et^2/\rho)^{1/5} = \left(\frac{10^{44}\times9.9\times10^{20}}{2\times10^{-21}}\right)^{1/5}
    = (5\times10^{85})^{1/5} \approx 2\times10^{17}$ m ≈ 6 pc — the right order for
    young remnants like Tycho's.

**H5 (conceptual).** Why does the [RANS](concepts/reynolds-averaging.md) approach
never close, no matter how many moment equations you derive? What does every practical
model therefore do?

??? success "Answer"
    The Navier–Stokes nonlinearity is quadratic: the equation for the $n$-th moment
    always contains the $(n{+}1)$-th ($\overline{u'u'}$ needs $\overline{u'u'u'}$,
    etc.) — an infinite hierarchy. Practical models truncate it by *modeling* some
    moment in terms of lower ones (e.g. Boussinesq eddy viscosity for
    $\overline{u_i'u_j'}$), importing empirical constants.
