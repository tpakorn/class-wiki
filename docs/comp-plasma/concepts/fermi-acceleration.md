# Fermi Acceleration

## Intuition

Bounce a ping-pong ball between two paddles moving slowly together: every bounce off
an approaching paddle adds speed. Replace paddles with
[magnetic mirrors](magnetic-mirror.md) and the ball with a trapped charged particle,
and you have Fermi's 1949 mechanism for accelerating cosmic rays to fantastic
energies — magnetic clouds in the galaxy acting as drifting mirrors.

## The setup

The course's model: a mirror field whose length slowly shrinks,

$$\psi(r, z, t) = B_\text{min}\pi r^2\left[1 + 2\lambda\frac{\zeta^2}{\zeta^4 + 1}\right],
\qquad \zeta = \frac{z}{L(t)}, \quad L(t) = L_0 - \alpha t$$

A time-varying $\mathbf{B}$ *induces an electric field* (Faraday), computed from the
vector potential:

$$\mathbf{A} = \frac{\psi}{2\pi r}\hat{\boldsymbol\phi}
\quad\Longrightarrow\quad
\mathbf{E} = -\frac{\partial\mathbf{A}}{\partial t}
= -\frac{1}{2\pi r}\frac{\partial \psi}{\partial t}\hat{\boldsymbol\phi}$$

This azimuthal E field is what actually does the work — magnetic fields never do.

## The physics

- Each reflection off an approaching mirror boosts $v_\parallel$ (head-on collision
  with a moving wall: $v \to v + 2u$ in the wall frame).
- The parallel invariant $J = \oint v_\parallel\, dz \approx v_\parallel L$ is
  adiabatically conserved: as $L$ shrinks, $v_\parallel$ *must* grow —
  $v_\parallel \propto 1/L$.
- Meanwhile $\mu = mv_\perp^2/2B$ holds $v_\perp$ tied to $B$. The pitch angle
  therefore *decreases* as $v_\parallel$ grows...
- ...until the particle enters the **loss cone**
  ($\theta < \theta_\text{trap} = \sin^{-1}(\lambda^{-1})$ in the model's notation)
  and escapes — carrying its stolen energy. Acceleration with a built-in exit door:
  exactly what a cosmic-ray source needs.

## Numerical experiment

Integrate the full orbit with the [leapfrog solver](leapfrog-method.md), fields from
the analytic derivatives of $\psi$ (chain rule through $L(t)$):

$$\frac{\partial\psi}{\partial t} = \frac{\partial\psi}{\partial\zeta}\cdot\left(-\frac{z}{L^2}\right)\cdot(-\alpha)$$

Watch $v_\parallel$ ratchet up bounce after bounce, then the escape. Track $\mu$ to
confirm the perpendicular invariant holds while $J$ does the accelerating.

## Where it matters

Cosmic-ray acceleration (Fermi's original 2nd-order mechanism, and the 1st-order
version at [supernova shocks](../../fluids/concepts/shock-waves.md)) · magnetic-pumping
heating schemes · particle energization in shrinking magnetospheric flux tubes.

## Common mistakes

- **Crediting the magnetic field with the energy.** The energy comes from whatever
  moves the mirrors, delivered via the induced E field.
- **Expecting unlimited acceleration.** The loss cone always wins eventually; the
  mechanism accelerates *and releases*.
- **Simulating with a symplectic-but-static-field mindset:** time-dependent fields
  mean energy is *not* conserved — that's the whole point; don't "fix" it.

## Related concepts

- [Magnetic mirror](magnetic-mirror.md) — the static prerequisite
- [Guiding center & drifts](guiding-center-drifts.md) — adiabatic framework
- [Leapfrog method](leapfrog-method.md) — integration engine

## Knowledge graph position

**Prerequisites:** [Magnetic mirror](magnetic-mirror.md).
**Leads to:** astrophysical particle acceleration, wave heating.

## Quiz

**Q1 (computational).** Mirrors shrink from $L_0$ to $L_0/2$. By what factor does a
trapped particle's parallel energy grow (adiabatic $J$)?

??? success "Answer"
    $v_\parallel \propto 1/L$ doubles ⇒ parallel energy ×4.

**Q2 (conceptual).** Why does Fermi acceleration preferentially *increase* energy,
when a particle can also bounce off a *receding* mirror and lose energy?

??? success "Answer"
    Head-on (approaching) encounters are more frequent than overtaking ones —
    approach speed is higher, so collisions are biased toward gains (rate ∝ relative
    velocity). Statistically the gains win — 2nd-order Fermi. With converging mirrors
    (or a shock), *every* bounce gains — 1st-order Fermi.

**Q3 (MCQ).** The work on the accelerated particle is done by:

- (a) the magnetic field directly  (b) the induced electric field
- (c) collisions  (d) gravity

??? success "Answer"
    **(b).** $\partial\mathbf{B}/\partial t \neq 0$ induces $\mathbf{E}$ (Faraday);
    only $\mathbf{E}$ does work on charges.
