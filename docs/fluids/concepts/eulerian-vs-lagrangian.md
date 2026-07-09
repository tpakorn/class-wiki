# Eulerian vs Lagrangian Descriptions

## Intuition

Two ways to study traffic: stand on a bridge and count cars passing below
(**Eulerian** — fixed point, watch the field), or ride inside one car and log its
journey (**Lagrangian** — follow the particle). Fluid mechanics constantly switches
between these views, and the dictionary between them is the
[material derivative](material-derivative.md).

## Formal definitions

| Characteristic | Eulerian | Lagrangian |
|---|---|---|
| Focus | fixed spatial points | individual fluid particles |
| Tracks | properties at locations | trajectory of each particle |
| Variables | fields $f(\mathbf{x}, t)$ | particle functions $f_P(t)$ |
| Frame | fixed (watching flow) | moving (riding the flow) |

**Eulerian:** the velocity *field* $\mathbf{v} = \mathbf{v}(\mathbf{x}, t)$. The local
rate of change at a fixed point is $\partial f/\partial t$. This is the natural
language of measurement (anemometer on a mast) and of CFD grids.

**Lagrangian:** each particle's position $\mathbf{X}(t)$, with velocity
$\mathbf{v}_L = d\mathbf{X}/dt$. This is the natural language of Newton's laws — force
acts on *matter*, not on points of space.

## Flow visualization: three kinds of lines

- **Streamlines** — curves tangent to $\mathbf{v}$ everywhere *at one instant*:
  $\frac{dx}{u} = \frac{dy}{v} = \frac{dz}{w}$. Snapshots; can't cross in steady flow.
- **Pathlines** — actual particle trajectories over time: integrate
  $\frac{d\mathbf{r}}{dt} = \mathbf{v}(\mathbf{r}(t), t)$. Pure Lagrangian objects.
- **Streaklines** — the locus of all particles that ever passed a fixed point (what a
  dye injector shows). History-dependent.

In **steady flow** all three coincide; in unsteady flow they differ, and confusing them
is a classic exam trap.

## Four motions of a fluid element

A velocity field generically does four things to a small blob of fluid:

1. **Translation** ($\mathbf{v}$) — carries it along
2. **Rotation** ($\boldsymbol{\omega} = \nabla\times\mathbf{v}$) — spins it
3. **Linear strain** ($\varepsilon_{xx}$…) — stretches it
4. **Shear strain** ($\varepsilon_{xy}$…) — skews it

[Potential flow](potential-flow.md) is the special case with zero rotation;
[viscosity](viscosity.md) generates stresses from the strain rates.

## Common mistakes

- **Thinking $\partial \mathbf{v}/\partial t = 0$ means particles don't accelerate.**
  A steady converging nozzle has $\partial \mathbf{v}/\partial t = 0$ everywhere, yet
  every particle speeds up as it moves — the acceleration is *convective*. See
  [material derivative](material-derivative.md).
- **Reading dye photos as streamlines.** Dye shows *streaklines*; they only match
  streamlines when the flow is steady.

## Related concepts

- [Material derivative](material-derivative.md) — the bridge between the two views
- [Reynolds transport theorem](reynolds-transport-theorem.md) — the same bridge for finite volumes
- [Potential flow](potential-flow.md) — irrotational special case

## Knowledge graph position

**Prerequisites:** [What is a fluid?](what-is-a-fluid.md)
**Leads to:** [Material derivative](material-derivative.md), [Reynolds transport theorem](reynolds-transport-theorem.md).

## Quiz

**Q1 (conceptual).** A weather station reports temperature falling at 2 °C/h. A balloon
drifting with the wind reports temperature *rising* at 1 °C/h. Are these contradictory?

??? success "Answer"
    No. The station measures the Eulerian rate $\partial T/\partial t$ at a fixed
    point; the balloon measures the Lagrangian rate $DT/Dt$. They differ by advection
    $\mathbf{v}\cdot\nabla T$ — the wind is blowing the balloon into warmer air.

**Q2 (multiple choice).** In an unsteady flow, the line traced by continuous dye
injection at a point is a:

- (a) streamline  (b) pathline  (c) streakline  (d) isobar

??? success "Answer"
    **(c).** Streaklines connect all particles that passed the injection point.

**Q3 (conceptual).** Why do computational fluid dynamics codes usually favor the
Eulerian description?

??? success "Answer"
    Fields on a fixed grid are easy to discretize and the mesh never tangles. Tracking
    billions of individual particles (Lagrangian) is costly and the particles cluster,
    leaving regions unresolved. (Particle methods do exist — e.g. SPH, and the
    [PIC method](../../comp-plasma/concepts/pic-method.md) in plasma physics is a hybrid.)
