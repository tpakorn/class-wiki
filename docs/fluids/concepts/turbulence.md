# Turbulence

> *"Big whirls have little whirls that feed on their velocity,
> and little whirls have lesser whirls and so on to viscosity."*
> — Lewis Fry Richardson (1922)

## Intuition

Watch smoke rise from an incense stick: a smooth laminar thread, then a wobble, then
sudden glorious chaos. That transition — orderly flow surrendering to a tangle of
eddies across every size — is turbulence. It has no tidy definition; it is recognized
by its symptoms: chaotic, multi-scale, dissipative, and ferociously good at mixing.

## When: the Reynolds number

The laminar/turbulent divide is governed by the
[Reynolds number](reynolds-number.md) $Re = UL/\nu$:

- $Re \ll 1$: viscosity wins — smooth, laminar, reversible.
- $Re \gg 1$: inertia wins — the nonlinear term $(\mathbf{v}\cdot\nabla)\mathbf{v}$
  dominates the [Navier–Stokes equation](../equations/navier-stokes-equation.md), and
  since the viscous term scales as $1/Re$, nothing linear is left to keep order.

## The three signatures

**Eddies.** Turbulence is organized (if that's the word) into vortices —
$\boldsymbol{\omega} = \nabla\times\mathbf{u}$ — spanning a huge range of sizes,
constantly stretching and breaking into smaller ones. 3-D vortex stretching is
essential; 2-D "turbulence" behaves qualitatively differently.

**Chaos.** Sensitive dependence on initial conditions: two indistinguishable initial
states diverge exponentially. Deterministic equations, unpredictable details — hence
the statistical viewpoint of [Reynolds averaging](reynolds-averaging.md).

**Enhanced diffusion.** Eddies transport momentum, heat and tracers orders of magnitude
faster than molecular diffusion: cream stirs into coffee in seconds, drag on pipes and
wings jumps, pollutant plumes spread.

## Where the energy goes

Energy enters at large scales (stirring, shear, convection), cascades through an
inertial range, and dies as heat at the Kolmogorov microscale — the celebrated picture
quantified on the [energy cascade page](energy-cascade.md), with the $-5/3$ spectrum as
its fingerprint.

## Why it's hard

- The convective nonlinearity couples *all* scales — no superposition.
- Whether smooth 3-D Navier–Stokes solutions always exist is a Clay Millennium Prize
  problem ($1M, still unclaimed).
- Direct numerical simulation must resolve scales from $L$ down to the Kolmogorov
  length $\eta$, costing roughly $Re^{9/4}$ grid points — hopeless for an airliner at
  $Re \sim 10^8$. Hence [RANS modeling](reynolds-averaging.md) and the closure problem.

## Examples in the wild

Airplane wakes · smoke plumes · blood flow at high rates and in pathologies · rivers
around bridge piers · planetary atmospheres · solar convection ·
[plasma turbulence in fusion devices](../../plasma/index.md).

## Common mistakes

- **"Turbulent" ≠ "fast".** A glacier-slow flow of low-viscosity fluid at large scale
  can be turbulent; a fast microfluidic jet can be laminar. Only $Re$ (not $U$ alone)
  decides.
- **Expecting exact prediction of instantaneous fields.** Only *statistics* (means,
  spectra, fluxes) are reproducible.
- **Treating turbulence as small-scale noise on the mean flow.** The fluctuations carry
  the momentum transport — see the [Reynolds stress](reynolds-averaging.md).

## Related concepts

- [Reynolds number](reynolds-number.md) — the control parameter
- [Energy cascade](energy-cascade.md) — the K41 picture
- [Reynolds averaging / RANS](reynolds-averaging.md) — the engineering response
- [Hydrodynamic stability](hydrodynamic-stability.md) — how laminar flow loses

## Knowledge graph position

**Prerequisites:** [Navier–Stokes](../equations/navier-stokes-equation.md), [Reynolds number](reynolds-number.md), [Hydrodynamic stability](hydrodynamic-stability.md).
**Leads to:** [Energy cascade](energy-cascade.md), [Reynolds averaging](reynolds-averaging.md).

## Quiz

**Q1 (conceptual).** Why does turbulence require the Reynolds number to be large,
in terms of the Navier–Stokes equation?

??? success "Answer"
    Nondimensionalized, the viscous term carries a $1/Re$ prefactor. At large $Re$ it
    can't damp the quadratic convective term, whose mode-coupling continually excites
    new scales; at small $Re$ diffusion smooths perturbations faster than they grow.

**Q2 (multiple choice).** Which is *not* a defining feature of turbulence?

- (a) sensitivity to initial conditions  (b) broad range of eddy sizes
- (c) enhanced mixing  (d) periodicity in time

??? success "Answer"
    **(d).** Periodic vortex shedding (e.g. a Kármán street) is unsteady laminar flow,
    not turbulence.

**Q3 (conceptual).** Blood flow in arteries is normally laminar ($Re \sim 10^3$ at
peak). Why do doctors listen for *sounds* (bruits) to detect a narrowed artery?

??? success "Answer"
    A stenosis raises the local velocity (continuity) and thus the local $Re$; the jet
    beyond it becomes turbulent, and turbulent pressure fluctuations radiate audible
    noise. Laminar flow is silent.
