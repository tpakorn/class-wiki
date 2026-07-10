# Kepler's Laws & Orbits

*Source lecture(s):* [SC133 Lec 17](../lectures.md)

## Intuition

Kepler spent a decade wrestling Tycho Brahe's planetary data into three empirical
rules — and half a century later Newton showed all three tumble out of one
inverse-square law. This is the template of theoretical physics: patterns first, then
the single principle underneath. Bonus: Einstein's turn came when Mercury's orbit
refused to follow Newton exactly.

## The three laws

**K1 — Ellipses.** Planets move on ellipses with the Sun at one focus. (The circle is
the special case of zero eccentricity; comets ride extreme ellipses.)

**K2 — Equal areas.** The Sun–planet line sweeps equal areas in equal times: planets
move *fastest at perihelion*, slowest at aphelion.

This is nothing but [conservation of angular momentum](rolling-torque-angular-momentum.md):
gravity is central, exerts no torque about the Sun, so
$L = mvr_\perp$ is constant — and the swept-area rate is $\frac{dA}{dt} = \frac{L}{2m}$.

**K3 — Harmonic law.** Period² ∝ semi-major-axis³:

$$\boxed{\,T^2 = \frac{4\pi^2}{GM}\,a^3\,}$$

**Derivation for circular orbits** (two lines): gravity supplies the
[centripetal force](circular-motion.md),

$$\frac{GMm}{r^2} = \frac{mv^2}{r} = m\omega^2 r
\;\Rightarrow\; \omega^2 = \frac{GM}{r^3}
\;\Rightarrow\; T^2 = \frac{4\pi^2}{GM}r^3.$$

Measure $T$ and $r$ for *any* satellite and you have weighed the central body — this
is literally how we know the masses of the Sun, the planets, and the black hole at
the galactic center.

## Orbital energetics

Total energy of an orbit of semi-major axis $a$:

$$E = K + U = -\frac{GMm}{2a}$$

- $E < 0$: bound (ellipse) · $E = 0$: parabola (escape, exactly) · $E > 0$: hyperbola (flyby)
- For circular orbits $K = -E = |U|/2$ — the **virial relation**, the same
  $2\langle K\rangle = -\langle U\rangle$ that governs
  [star-cluster simulations](../../comp-plasma/concepts/n-body-simulation.md).
- Counterintuitive gem: drag on a satellite makes it **speed up** (it falls to a
  lower, faster orbit — energy drops, kinetic energy rises).

## Worked example: geostationary orbit

What radius keeps a satellite over one spot ($T = 24$ h = 86 400 s)?

$$r = \left(\frac{GM_E T^2}{4\pi^2}\right)^{1/3}
= \left(\frac{(6.67\times10^{-11})(5.97\times10^{24})(86400)^2}{4\pi^2}\right)^{1/3}
\approx 4.2\times10^7\,\text{m}$$

— about $6.6\,R_E$, the crowded ring where communication satellites live.

## Einstein's postscript

Mercury's perihelion drifts 43″/century beyond Newtonian prediction. General
relativity — gravity as spacetime curvature — accounts for it exactly, plus light
bending and GPS clock corrections. Newton remains the working approximation
everywhere weaker than these extremes.

## Common mistakes

- **Sun at the center.** It's at a *focus*; the ellipse's center is empty.
- **Constant orbital speed on an ellipse.** K2 forbids it — speed varies, only the
  areal rate is constant.
- **Applying K3 across different central bodies.** The constant contains $M$: moons
  of Jupiter and planets of the Sun follow *different* $T^2/a^3$ lines.
- **Confusing $r$ with $a$** for ellipses — K3 uses the semi-major axis.

## Related concepts

- [Gravitation](gravitation.md) — the underlying force law
- [Angular momentum](rolling-torque-angular-momentum.md) — K2's real identity
- [Circular motion](circular-motion.md) — the two-line derivation of K3
- [Rutherford scattering (PHY653)](../../comp-plasma/examples/rutherford-scattering.md) — the same math with repulsion: hyperbolas

## Knowledge graph position

**Prerequisites:** [Gravitation](gravitation.md), [Angular momentum](rolling-torque-angular-momentum.md).
**Leads to:** astrophysics, orbital mechanics, [N-body simulation](../../comp-plasma/concepts/n-body-simulation.md).

## Quiz

**Q1 (computational).** Mars orbits at $a = 1.52$ AU. Its year, in Earth years?

??? success "Answer"
    $T = a^{3/2} = 1.52^{1.5} \approx 1.87$ years — K3 with Sun-units, where
    $T^2/a^3 = 1$ by construction.

**Q2 (conceptual).** A comet's speed at perihelion (0.5 AU) vs aphelion (50 AU)?

??? success "Answer"
    K2 / angular momentum: $v_p r_p = v_a r_a$ (velocity ⊥ radius at both extremes),
    so $v_p = 100\,v_a$ — a two-order-of-magnitude sprint past the Sun.

**Q3 (multiple choice).** To catch up with a space station *ahead* of you in the same
orbit, you should briefly fire your engines:
(a) forward (speed up) (b) backward (slow down) (c) toward Earth

??? success "Answer"
    **(b).** Slowing drops you to a lower, *faster* orbit; you overtake below, then
    re-raise. Orbital mechanics runs on energy logic, not car logic.
