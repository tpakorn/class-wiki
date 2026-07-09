# Guiding Center & Drift Theory

## Intuition

A charged particle in a magnetic field is a fast circle glued to a slow wanderer.
Squint past the rapid gyration and you see the circle's *center* drifting smoothly —
that center is the **guiding center**, and drift theory is the physics of where it
goes. It converts an impossible-to-follow spiral into four clean drift formulas.

## The decomposition

$$\mathbf{x}(t) = \underbrace{\mathbf{X}_\text{gc}(t)}_{\text{guiding center (slow)}}
+ \underbrace{\boldsymbol{\rho}(t)}_{\text{gyration (fast)}}$$

**Validity conditions:** the Larmor radius is small compared to field-variation scales
($\rho_L \ll L_B$), and the gyration period is short compared to field time scales
($2\pi/\omega_c \ll \tau_\text{field}$). Averaging over the gyration then yields:

$$\boxed{\,\mathbf{v}_{\perp,\text{gc}} = \mathbf{v}_E + \mathbf{v}_{\nabla B} + \mathbf{v}_c + \mathbf{v}_P\,}$$

## The four drifts

| Drift | Formula | Cause | Charge-dependent? |
|---|---|---|---|
| [E×B](../equations/exb-drift.md) | $\mathbf{v}_E = \dfrac{\mathbf{E}\times\mathbf{B}}{B^2}$ | electric field | **No** |
| [Grad-B](../equations/grad-b-curvature-drift.md) | $\mathbf{v}_{\nabla B} = -\dfrac{m v_{\perp}^2}{2qB^3}\nabla B\times\mathbf{B}$ | $\lvert\mathbf{B}\rvert$ gradient | Yes |
| [Curvature](../equations/grad-b-curvature-drift.md) | $\mathbf{v}_c = \dfrac{m v_{\parallel}^2}{qB^2}\dfrac{\hat{\mathbf{R}}}{R}\times\mathbf{B}$ | curved field lines | Yes |
| Polarization | $\mathbf{v}_P \approx \dfrac{m}{qB^2}\dfrac{d\mathbf{E}_\perp}{dt}$ | time-varying $\mathbf{E}$ | Yes (and mass-dep.) |

Charge dependence matters enormously: charge-dependent drifts separate ions from
electrons → **currents** and **charge separation** → new electric fields → new E×B
drifts. That chain is the engine of tokamak vertical drift, of the
[polarization current in waves](../../plasma/index.md), and of much plasma
misbehavior.

## Physical pictures

- **E×B:** during the half-gyration where the particle moves with $\mathbf{E}$ it
  speeds up (bigger Larmor radius); against, it slows (smaller). Fat half + thin half
  = net sideways march — *independent of charge and mass* (both flip together).
- **Grad-B:** larger circles where $B$ is weak, tighter where strong; the orbit
  doesn't close and inches sideways.
- **Curvature:** a particle streaming along a bent field line feels a centrifugal
  push $mv_\parallel^2/R$ outward; crossed with $\mathbf{B}$, that force drifts it.
- **Polarization:** when $\mathbf{E}$ changes, the E×B drift must change too; the
  inertia-limited catch-up appears as a drift along $d\mathbf{E}/dt$ — heavy ions lag
  more, carrying most of the polarization current.

## Numerical verification (the course's approach)

Rather than trust the averaging, integrate the full
[Lorentz force](../equations/lorentz-force.md) with the
[3-D leapfrog solver](leapfrog-method.md) and *watch* each drift emerge:

1. **Uniform E, B** → helical cycloid drifting at exactly $E/B$
2. **Line charge + axial B** → azimuthal E×B orbit around the wire
3. **Toroidal field** ($B \propto 1/r$) → vertical grad-B + curvature drift, the
   reason a pure toroidal trap fails ([tokamaks](../../plasma/index.md) add poloidal
   field to short it out)
4. **[Magnetic mirror](magnetic-mirror.md)** → trapping and reflection
5. **Wave fields** → drift-theory regime $\alpha \ll 1$ through stochastic
   $\alpha \gtrsim 1$, where $\alpha = mk^2\phi/qB^2$

## Common mistakes

- **Applying drift formulas where gyration isn't fast.** If $\rho_L \sim L_B$ the
  decomposition fails; only the full orbit integration is trustworthy (that's why the
  course teaches both).
- **Expecting E×B to create current.** It moves ions and electrons *together* — flow,
  not current. The charge-dependent drifts make the currents.
- **Dropping the parallel dynamics.** Drifts describe motion ⊥ to $\mathbf{B}$; along
  the field, particles stream freely (or mirror — see
  [magnetic mirror](magnetic-mirror.md)).

## Related concepts

- [E×B drift](../equations/exb-drift.md) · [Grad-B & curvature drifts](../equations/grad-b-curvature-drift.md)
- [Magnetic mirror](magnetic-mirror.md) — parallel-motion counterpart
- [Leapfrog method](leapfrog-method.md) — the verification engine
- [PC368 drift-motion page](../../plasma/concepts/drift-motion.md) — the theory course's treatment

## Knowledge graph position

**Prerequisites:** [Lorentz force](../equations/lorentz-force.md), [Leapfrog](leapfrog-method.md), [cyclotron motion](../equations/cyclotron-motion.md).
**Leads to:** [Magnetic mirror](magnetic-mirror.md), [Fermi acceleration](fermi-acceleration.md).

## Quiz

**Q1 (computational).** $E = 100$ V/m ⊥ $B = 0.1$ T. Find the E×B drift speed for an
electron and for a proton.

??? success "Answer"
    $v_E = E/B = 1000$ m/s — identical for both. Charge and mass cancel in
    $\mathbf{E}\times\mathbf{B}/B^2$.

**Q2 (conceptual).** In a purely toroidal field, why do particles escape even though
field lines close on themselves?

??? success "Answer"
    $B \propto 1/r$ gives both grad-B and curvature drifts, which are *vertical* and
    charge-dependent. Charges separate vertically, the resulting E field drives an
    outward E×B drift for everyone — the plasma expels itself.

**Q3 (MCQ).** Which drift survives even when $q \to -q$ and $m \to m_e$?

- (a) grad-B  (b) curvature  (c) E×B  (d) polarization

??? success "Answer"
    **(c).** E×B is charge- and mass-independent — it is really the velocity of the
    frame in which $\mathbf{E}_\perp$ vanishes.
