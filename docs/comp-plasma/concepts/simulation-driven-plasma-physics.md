# Why Simulate Plasmas?

## Intuition

A plasma is a crowd where everyone influences everyone: each charged particle moves in
electromagnetic fields, and the fields are *made by* the moving charges. This
self-consistent loop —

$$\text{particles} \xrightarrow{\ \rho,\ \mathbf{J}\ } \text{fields}
\xrightarrow{\ \mathbf{E},\ \mathbf{B}\ } \text{particles}$$

— produces collective behavior (oscillations, waves, instabilities) that no
pencil-and-paper method can follow far. Computation is not a convenience here; it is
the laboratory.

## The two governing pillars

**Particle motion — the [Lorentz equation](../equations/lorentz-force.md):**

$$m\frac{d\mathbf{v}}{dt} = q(\mathbf{E} + \mathbf{v}\times\mathbf{B})$$

**Field evolution — Maxwell's equations:**

$$\nabla\cdot\mathbf{E} = \frac{\rho}{\varepsilon_0} \qquad \nabla\cdot\mathbf{B} = 0$$

$$\nabla\times\mathbf{E} = -\frac{\partial\mathbf{B}}{\partial t} \qquad
\nabla\times\mathbf{B} = \mu_0\mathbf{J} + \mu_0\varepsilon_0\frac{\partial\mathbf{E}}{\partial t}$$

The course's arc: learn to integrate the first
([Chapters 2–3](ode-integration.md)), discretize the second
([Chapter 4](finite-difference-method.md)), then couple them
([Chapter 5 — PIC](pic-method.md)).

## The toolkit: Python

NumPy (arrays), Matplotlib (plots/animations), SciPy (sparse solvers), Jupyter
(code + math + narrative). Everything in the course fits the same skeleton:

```python
# initialize state arrays
for i in range(1, num_steps):
    # compute forces/fields at state[i-1]
    # advance state to state[i]
# visualize
```

## Warm-up: projectiles as proto-plasmas

The bouncing-ball simulation (gravity + energy loss per bounce) is secretly a charged
particle in a uniform field: $g \leftrightarrow qE/m$. Two classic results fall out:

- **Parabola of safety:** the envelope of all trajectories launched at speed $u$ is
  $y = \frac{u^2}{2g} - \frac{g x^2}{2u^2}$ — no projectile can cross it.
- **[Rutherford scattering](../examples/rutherford-scattering.md):** replace the
  constant field by the Coulomb field $\mathbf{E} = \frac{q}{4\pi\varepsilon_0 r^2}\hat r$
  and the simulation reproduces $\tan(\theta/2) = \frac{q_1q_2}{4\pi\varepsilon_0\mu b v_\infty^2}$
  — numerics validated against theory, the pattern for the whole course.

## Common mistakes

- **Trusting a simulation you haven't benchmarked.** Every solver in this course is
  first run on a problem with a known answer (cycloid, Rutherford, Kepler).
- **Confusing single-particle with self-consistent simulation.** Chapters 2–3
  prescribe the fields; reality (and [PIC](pic-method.md)) computes them from the
  particles.
- **Ignoring units.** Normalized units ($q = m = c = 1$) are standard — know the
  conversion back before quoting numbers.

## Related concepts

- [ODE integration](ode-integration.md) — the first tool
- [PIC method](pic-method.md) — the destination
- [Plasma fundamentals (PC368)](../../plasma/index.md) — the physics this computes

## Knowledge graph position

**Prerequisites:** basic mechanics & electromagnetism, Python.
**Leads to:** [ODE integration](ode-integration.md), [finite differences](finite-difference-method.md).

## Quiz

**Q1 (conceptual).** Why can't single-particle simulations capture plasma
oscillations?

??? success "Answer"
    Plasma oscillations are collective: they exist because displaced *charge density*
    creates a restoring field. With prescribed fields, no feedback from particle to
    field exists — you need the self-consistent [PIC loop](pic-method.md).

**Q2 (computational).** A ball dropped from 10 m loses 20% of its energy per bounce.
What height does it reach after 3 bounces?

??? success "Answer"
    Height ∝ energy: $10 \times 0.8^3 = 5.12$ m.

**Q3 (MCQ).** The analogy between projectile motion and charged-particle motion maps
$g$ onto:

- (a) $qB/m$  (b) $qE/m$  (c) $q/m$  (d) $E/B$

??? success "Answer"
    **(b).** Uniform electric acceleration $qE/m$ plays exactly the role of $g$.
