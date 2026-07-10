# Moment of Inertia

*Source lecture(s):* [SC133 Lec 12](../lectures.md)

## Intuition

Spin a pencil about its long axis: trivial. Spin the same pencil end-over-end: harder.
Same mass — different *distribution* of mass around the axis. The moment of inertia
$I$ is rotation's version of mass, but with a twist: **distance from the axis counts
squared**. Mass far from the axis resists spinning ferociously; mass on the axis
doesn't resist at all.

## Definition

$$\boxed{\,I = \sum_i m_i r_i^2 \;\;\longrightarrow\;\; I = \int r^2\, dm\,}$$

where $r$ is each element's perpendicular distance from the **rotation axis** —
$I$ is meaningless until you name the axis.

## The standard catalogue (mass $M$, about the center unless noted)

| Body | Axis | $I$ |
|---|---|---|
| Hoop / thin ring | center, ⊥ plane | $MR^2$ |
| Solid disk / cylinder | central axis | $\tfrac12 MR^2$ |
| Solid sphere | diameter | $\tfrac25 MR^2$ |
| Hollow sphere | diameter | $\tfrac23 MR^2$ |
| Thin rod, length $L$ | center, ⊥ rod | $\tfrac1{12} ML^2$ |
| Thin rod, length $L$ | end, ⊥ rod | $\tfrac13 ML^2$ |

The pattern: the more mass lives near the rim, the closer the prefactor is to 1.
Ranking objects by $I/MR^2$ predicts the classic race —
[rolling downhill](rolling-torque-angular-momentum.md), the solid sphere beats the
disk beats the hoop, regardless of mass or radius.

## Parallel-axis theorem

Know $I_\text{cm}$ about the center of mass? Any parallel axis a distance $d$ away:

$$I = I_\text{cm} + Md^2$$

Check with the rod: $\tfrac1{12}ML^2 + M(L/2)^2 = \tfrac13 ML^2$ ✓. The theorem also
proves the CM axis is always the *easiest* axis of a given direction to spin about.

## Sample derivation: solid disk

Slice into rings of radius $r$, width $dr$: $dm = \dfrac{M}{\pi R^2}\,2\pi r\,dr$.

$$I = \int_0^R r^2\,dm = \frac{2M}{R^2}\int_0^R r^3\,dr = \frac{2M}{R^2}\cdot\frac{R^4}{4} = \tfrac12 MR^2$$

Every entry in the catalogue is this integral with different geometry — and this same
$\int r^2 dm$ resurfaces as the *area* moment $I_{xx}$ in
[hydrostatic forces on surfaces (PC316)](../../fluids/concepts/hydrostatic-force-on-surfaces.md).

## Common mistakes

- **Quoting $I$ without an axis.** The rod's $I$ changes by a factor of 4 between
  center and end.
- **Treating $I$ like mass in every formula without checking the axis** — the
  parallel-axis theorem exists precisely because axes matter.
- **Adding $Md^2$ to a non-CM value.** The theorem only jumps *from* the CM axis.
- **Assuming heavier means harder to spin.** A heavy solid sphere can out-accelerate
  a light hoop of equal radius under equal torque.

## Related concepts

- [Rotation](rotation.md) — where $I$ plays mass
- [Torque](torque.md) — $\sum\tau = I\alpha$
- [Rolling & angular momentum](rolling-torque-angular-momentum.md) — the catalogue in action
- [Center of mass](center-of-mass.md) — the reference point of the parallel-axis theorem

## Knowledge graph position

**Prerequisites:** [Rotation](rotation.md), [Center of mass](center-of-mass.md).
**Leads to:** [Rolling, torque & angular momentum](rolling-torque-angular-momentum.md), [pendulum](pendulum.md) (physical pendulum).

## Quiz

**Q1 (computational).** Four 1 kg point masses sit at the corners of a square of side
2 m. Find $I$ about the axis through the center, ⊥ to the plane.

??? success "Answer"
    Each mass is $r = \sqrt2$ m from the center:
    $I = 4\times1\times2 = 8\,\text{kg·m}^2$.

**Q2 (conceptual).** A figure skater pulls in her arms and spins faster. What changed,
and what stayed constant?

??? success "Answer"
    Pulling mass toward the axis reduces $I$; with no external torque, angular
    momentum $L = I\omega$ is constant, so $\omega$ rises. (Her kinetic energy
    $\tfrac12 I\omega^2 = L^2/2I$ *increases* — her muscles supply it.)

**Q3 (multiple choice).** Which reaches the bottom of a ramp first (rolling without
slipping): (a) hoop (b) solid disk (c) solid sphere

??? success "Answer"
    **(c).** Acceleration $a = g\sin\theta/(1 + I/MR^2)$: smallest $I/MR^2$
    ($2/5$) wins. Mass and radius cancel — only the *shape* races.
