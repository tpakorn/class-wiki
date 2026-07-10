# Gravitation

*Source lecture(s):* [SC133 Lec 16](../lectures.md)

## Intuition

Newton's great unification: the force that drops an apple **is** the force that holds
the Moon. The Moon *is falling* — continuously — it just moves sideways fast enough
to keep missing the Earth. One law, inverse-square in distance, universal in mass,
governs apples, moons, planets, and galaxies.

## The law

$$\boxed{\,F = G\,\frac{m_1 m_2}{r^2}\,}
\qquad G = 6.67\times10^{-11}\ \text{N·m}^2/\text{kg}^2$$

— always attractive, along the line joining the (centers of the) masses. Full
reference: [equation page](../equations/newtons-law-of-gravitation.md).

Two theorems make spheres tractable (Newton's shell theorems): a uniform spherical
shell attracts outside bodies *as if all its mass sat at the center*, and exerts
**zero** net force on a body inside it. Hence planets act like points — and gravity
*decreases* as you tunnel into the Earth.

## Superposition

Gravity adds as [vectors](vectors.md): the field of several masses is the sum of the
individual fields,

$$\vec g(\vec r) = \sum_i \left(-\frac{Gm_i}{r_i^2}\hat r_i\right)$$

Surface gravity: $g = GM_E/R_E^2 = 9.8\,\text{m/s}^2$ — this equation *weighs the
Earth* once $G$ is measured (Cavendish, 1798: "the experiment that weighed the
world").

## Gravitational potential energy

Taking $U(\infty) = 0$ ([why we may choose this](potential-energy.md)):

$$U = -\frac{G M m}{r}$$

Negative everywhere: bound systems sit in an energy hole. Escape requires total
energy $E = K + U \geq 0$:

$$v_\text{esc} = \sqrt{\frac{2GM}{R}}$$

Earth: $11.2\,\text{km/s}$. Moon: $2.4$ (why it kept no atmosphere). Push $R$ small
enough at fixed $M$ that $v_\text{esc} \to c$ and you have sketched a black hole —
[dimensional analysis gets the same radius](../../fluids/concepts/dimensional-analysis.md).

## The apple–Moon check (Newton's own)

Moon distance $\approx 60 R_E$, so lunar gravity should be $g/60^2 = 2.7\times10^{-3}\,\text{m/s}^2$.
Required centripetal acceleration: $\omega^2 r = \left(\frac{2\pi}{27.3\,\text{d}}\right)^2 (3.84\times10^8\,\text{m}) \approx 2.7\times10^{-3}\,\text{m/s}^2$. ✓
The inverse-square law, confirmed with 17th-century data.

## Weight vs weightlessness

Astronauts float not because gravity is absent (at ISS altitude it's still ~90% of
$g$!) but because they and the station **fall together** — orbit is perpetual free
fall. "Weightlessness" = no *contact* force, not no gravity.

## Common mistakes

- **"No gravity in space."** Gravity extends to infinity; orbiting is falling.
- **Using $U = mgh$ far from the surface.** That's the near-surface linearization;
  use $-GMm/r$ for anything orbital.
- **Doubling $r$ halves the force?** Inverse *square*: quarter.
- **Forgetting both masses attract each other equally** ([third law](newtons-laws.md))
  — the Earth accelerates toward the apple too, just imperceptibly.

## Related concepts

- [Kepler's laws & orbits](keplers-laws.md) — the law's consequences in the sky
- [Circular motion](circular-motion.md) — gravity as centripetal force
- [Potential energy](potential-energy.md) — the $-1/r$ well
- [Newton's law of gravitation (equation page)](../equations/newtons-law-of-gravitation.md)

## Knowledge graph position

**Prerequisites:** [Newton's laws](newtons-laws.md), [Circular motion](circular-motion.md), [Potential energy](potential-energy.md).
**Leads to:** [Kepler's laws](keplers-laws.md), astrophysics, [N-body simulation (PHY653)](../../comp-plasma/concepts/n-body-simulation.md).

## Quiz

**Q1 (computational).** How fast must a satellite move in a circular orbit just above
Earth's surface ($R_E = 6.4\times10^6$ m)?

??? success "Answer"
    $\frac{GM}{R^2} = \frac{v^2}{R} \Rightarrow v = \sqrt{gR_E} = \sqrt{9.8\times6.4\times10^6} \approx 7.9\,\text{km/s}$
    — Newton's cannonball; note $v_\text{esc} = \sqrt2\, v_\text{orbit}$.

**Q2 (conceptual).** You tunnel halfway to Earth's center (uniform density). How does
$g$ there compare with the surface?

??? success "Answer"
    Half. Only the mass *inside* your radius pulls (shell theorem):
    $g(r) = \frac{G}{r^2}\cdot M\frac{r^3}{R^3} = g_\text{surf}\,\frac{r}{R}$ —
    gravity is linear in $r$ inside a uniform sphere.

**Q3 (multiple choice).** Two satellites orbit Earth at radii $r$ and $4r$. The outer
one's orbital speed is: (a) half (b) quarter (c) $1/\sqrt2$

??? success "Answer"
    **(a).** $v = \sqrt{GM/r} \propto r^{-1/2}$: four times the radius, half the
    speed — outer planets amble.
