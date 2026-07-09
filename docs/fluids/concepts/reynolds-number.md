# Reynolds Number

## Intuition

Every flow is a contest between *inertia* (the tendency of moving fluid to keep going,
amplifying disturbances) and *viscosity* (internal friction smoothing them out). The
Reynolds number is the scoreboard. Small $Re$: honey-like, orderly, reversible motion.
Large $Re$: eddies, wakes, chaos — [turbulence](turbulence.md).

## Definition

$$\boxed{\,Re = \frac{UL}{\nu} = \frac{\rho U L}{\mu}\,}$$

- $U$ — characteristic velocity
- $L$ — characteristic length (pipe diameter, chord, body size)
- $\nu = \mu/\rho$ — kinematic [viscosity](viscosity.md)

It is the ratio of the convective term to the viscous term in the
[Navier–Stokes equation](../equations/navier-stokes-equation.md):

$$\frac{|(\mathbf{v}\cdot\nabla)\mathbf{v}|}{|\nu\nabla^2\mathbf{v}|}
\sim \frac{U^2/L}{\nu U/L^2} = \frac{UL}{\nu}$$

## Regimes

| $Re$ | Character |
|---|---|
| $\ll 1$ | creeping (Stokes) flow — viscosity rules; bacteria, microfluidics |
| $\sim 1$–$10^3$ | smooth laminar flow; steady wakes appear |
| $\sim 2300$ | classic transition threshold in pipes |
| $\gg 10^4$ | turbulent — inertia rules; aircraft, rivers, atmosphere |

Since $\nu \propto 1/Re$ in nondimensional form, high-$Re$ flow behaves *almost*
inviscidly — except in boundary layers and in the smallest eddies of the
[energy cascade](energy-cascade.md), where viscosity always collects its due.

## Why it matters

- **Dynamic similarity:** matching $Re$ (and geometry) between model and full scale
  makes wind-tunnel testing valid — see
  [Buckingham Pi](buckingham-pi-theorem.md).
- **Regime prediction:** whether a design sees laminar or turbulent flow changes drag,
  heat transfer, and mixing by orders of magnitude.
- **The turbulence switch:** $Re$ is the control parameter in most
  [stability analyses](hydrodynamic-stability.md).

## Worked example

A car ($L \approx 4$ m) at 100 km/h in air ($\nu \approx 1.5\times10^{-5}\ \text{m}^2/\text{s}$):

$$Re = \frac{27.8 \times 4}{1.5\times10^{-5}} \approx 7\times10^6$$

Deeply turbulent. A paramecium ($L\sim 10^{-4}$ m, $U\sim 10^{-3}$ m/s, water
$\nu = 10^{-6}$): $Re \sim 0.1$ — it lives in your honey-world, where coasting is
impossible and swimming strategies must be non-reciprocal (the "scallop theorem").

## Common mistakes

- **Ambiguous $L$.** State your length scale; $Re$ based on radius vs diameter differs
  by 2. Conventions matter when quoting thresholds.
- **Treating 2300 as universal.** It's the *pipe-flow* transition under ordinary
  disturbance levels; carefully quiet experiments stay laminar far higher.
- **Assuming high $Re$ = inviscid everywhere.** Boundary layers, separation and
  dissipation are viscous phenomena that persist at any $Re$.

## Related concepts

- [Viscosity](viscosity.md) — the denominator
- [Navier–Stokes equation](../equations/navier-stokes-equation.md) — where the ratio comes from
- [Turbulence](turbulence.md) — the high-$Re$ fate
- [Buckingham Pi theorem](buckingham-pi-theorem.md) — why one number characterizes so much

## Knowledge graph position

**Prerequisites:** [Viscosity](viscosity.md), [Dimensional analysis](dimensional-analysis.md).
**Leads to:** [Turbulence](turbulence.md), [Hydrodynamic stability](hydrodynamic-stability.md).

## Quiz

**Q1 (computational).** Water ($\nu = 10^{-6}\ \text{m}^2/\text{s}$) flows at 2 m/s
through a 5 cm pipe. Laminar or turbulent?

??? success "Answer"
    $Re = 2\times0.05/10^{-6} = 10^5 \gg 2300$ — turbulent, comfortably.

**Q2 (conceptual).** Why is it impossible to test a full-scale-Reynolds airliner with a
1:50 model in the same wind tunnel air at the same speed?

??? success "Answer"
    $Re \propto UL$: shrinking $L$ by 50 drops $Re$ by 50. You'd need 50× the speed
    (compressibility ruins it), a pressurized/cryogenic tunnel (raising $\rho$,
    lowering $\nu$), or acceptance of scale effects.

**Q3 (multiple choice).** The Reynolds number compares:

- (a) pressure to gravity  (b) inertia to viscosity  (c) velocity to sound speed  (d) kinetic to potential energy

??? success "Answer"
    **(b).** (a) is Froude-like, (c) is the Mach number.
