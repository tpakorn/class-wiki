# Leapfrog Update for the Lorentz Force

## Equation

Discretizing $\dot{\mathbf{v}} = \boldsymbol\Sigma + \mathbf{v}\times\boldsymbol\Omega$
(with $\boldsymbol\Omega = q\mathbf{B}/m$, $\boldsymbol\Sigma = q\mathbf{E}/m$) by the
centered [leapfrog rule](../concepts/leapfrog-method.md) gives an implicit equation
$\mathbf{v}_\text{new} + \mathbf{A}\times\mathbf{v}_\text{new} = \mathbf{C}$ with the
**closed-form solution**:

$$\boxed{\;\mathbf{v}_\text{new} = \frac{\mathbf{C} + \mathbf{A}(\mathbf{A}\cdot\mathbf{C}) - \mathbf{A}\times\mathbf{C}}{1 + A^2}\;}$$

$$\mathbf{A} = \frac{\boldsymbol\Omega\,\Delta t}{2}, \qquad
\mathbf{C} = \mathbf{v}_\text{old} + \Delta t\left(\boldsymbol\Sigma + \frac{\mathbf{v}_\text{old}\times\boldsymbol\Omega}{2}\right),
\qquad \mathbf{x}_\text{new} = \mathbf{x}_\text{old} + \mathbf{v}_\text{new}\Delta t$$

Cross-field special case ($\mathbf{E} = E\hat\jmath$, $\mathbf{B} = B\hat k$), with
$a = \Omega\Delta t/2$:

$$v_x' = \frac{(1 - a^2)\,v_x + 2a\,v_y + a\,\Sigma\Delta t}{1 + a^2}, \qquad
v_y' = \frac{(1 - a^2)\,v_y - 2a\,v_x + \Sigma\Delta t}{1 + a^2}$$

!!! warning "Check the $(1-a^2)$ factor"
    For $\Sigma = 0$ this map is an *exact rotation* — $|\mathbf{v}'| = |\mathbf{v}|$
    identically, which is the whole point of the scheme. A tempting "simplification"
    that replaces $(1-a^2)v_x \to v_x$ (as appears in some course materials) has
    per-step gain $\sqrt{(1 + 4a^2)}/(1+a^2) > 1$: the orbit slowly spirals outward,
    exactly the pathology leapfrog exists to avoid. Reduce the general vector formula
    carefully.

## Physical meaning

An *implicit* scheme solved *explicitly*: because the magnetic force is linear in
$\mathbf{v}$, the implicit equation is just a small linear system, invertible by the
vector identity above. You get implicit-grade stability and symplectic energy behavior
at explicit-method cost — one field evaluation per step, no iteration.

## Variables

$\mathbf{A}$ — half-step rotation vector (dimensionless) · $\mathbf{C}$ — predictor
velocity · $\Omega = qB/m$ — [cyclotron frequency](cyclotron-motion.md) ·
$\Sigma = qE/m$ — electric acceleration.

## Properties

- **2nd order**, symplectic, time-reversible
- **Exact gyration radius** for uniform $\mathbf{B}$ (phase error only)
- Works for arbitrary $\mathbf{E}(\mathbf{x},t)$, $\mathbf{B}(\mathbf{x},t)$ — the
  3-D solver behind every [Chapter 3 orbit exercise](../concepts/guiding-center-drifts.md)
- The **Boris pusher** — the standard mover in production
  [PIC codes](../concepts/pic-method.md) — is this same rotate-and-kick idea

```python
def update_velocity(v_old, E, B, dt):
    Omega, Sigma = q_m*B, q_m*E
    A = Omega * dt / 2
    C = v_old + dt*(Sigma + np.cross(v_old, Omega)/2)
    return (C + A*np.dot(A, C) - np.cross(A, C)) / (1 + np.linalg.norm(A)**2)
```

## Derivation sketch

Leapfrog demands
$\frac{\mathbf{v}_\text{new} - \mathbf{v}_\text{old}}{\Delta t} = \boldsymbol\Sigma + \frac{\mathbf{v}_\text{new} + \mathbf{v}_\text{old}}{2}\times\boldsymbol\Omega$.
Collect the unknown: $\mathbf{v}_\text{new} + \mathbf{A}\times\mathbf{v}_\text{new} = \mathbf{C}$.
For any such equation, dotting and crossing with $\mathbf{A}$ lets you solve:
$\mathbf{v} = \frac{\mathbf{C} + \mathbf{A}(\mathbf{A}\cdot\mathbf{C}) - \mathbf{A}\times\mathbf{C}}{1+A^2}$
(check: substitute back and use the BAC–CAB identity).

## Related equations

- [Lorentz force](lorentz-force.md) — the continuous law
- [Cyclotron motion](cyclotron-motion.md) — the benchmark it must reproduce
- [RK4 scheme](rk4-scheme.md) — the accuracy-first alternative

## Quiz

**Q1 (conceptual).** Why does the denominator $1 + A^2$ guarantee the update never
blows up, at any $\Delta t$?

??? success "Answer"
    The update is (kick + exact rotation-like map); its "gain" is bounded by
    $\sim 1/(1+A^2) \times$ rotation factors of unit norm. Large $\Delta t$ degrades
    *accuracy* (wrong gyration phase) but never *stability* — contrast forward Euler's
    unconditional energy growth.

**Q2 (computational).** With $\Omega\Delta t = 2$, how many steps per gyration period
is that, and would you trust the orbit's phase?

??? success "Answer"
    $T = 2\pi/\Omega$ ⇒ $\pi \approx 3$ steps per period. The radius stays right
    (symplectic), but with ~3 samples per circle the *phase* error is enormous —
    resolve at least ~20 steps/period for meaningful trajectories.
