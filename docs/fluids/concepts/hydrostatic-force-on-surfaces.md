# Hydrostatic Force on Submerged Surfaces

## Intuition

A dam wall doesn't feel one number — it feels a *distribution*: gentle pressure near
the waterline, crushing pressure at the base. Two questions matter for engineering:
what is the **total force**, and **where** does it effectively act? The answers turn
out to involve two old friends from mechanics: the centroid and the moment of inertia
of the wetted area.

## Mathematical formulation

A plane surface of area $A$ is submerged, inclined at angle $\theta$ to the horizontal.
Measuring $y$ along the plate from the fluid surface, the local pressure is

$$P = P_0 + \rho g y \sin\theta.$$

**Total (resultant) force** — integrate over the plate:

$$F_R = \int_A P\, dA = P_0 A + \rho g \sin\theta \int_A y\, dA$$

Defining the centroid $y_C = \frac{1}{A}\int_A y\, dA$:

$$\boxed{\,F_R = (P_0 + \rho g\, y_C \sin\theta)\,A = P_C\, A\,}$$

*The resultant force equals the pressure at the centroid times the area.*

**Center of pressure** — the point $y_P$ where $F_R$ effectively acts, found by moment
balance $y_P F_R = \int_A y P\, dA$:

$$y_P = y_C + \frac{I_{xx,C}}{\left[y_C + P_0/(\rho g \sin\theta)\right] A}
\quad\xrightarrow{\,P_0 = 0\,}\quad
\boxed{\,y_P = y_C + \frac{I_{xx,C}}{y_C\, A}\,}$$

where $I_{xx,C}$ is the second moment of the area about a horizontal axis through its
centroid (via the parallel-axis theorem $I_{xx,O} = I_{xx,C} + y_C^2 A$).

**Reference table** (area and centroidal moment of inertia):

| Shape | $A$ | $I_{xx,C}$ |
|---|---|---|
| Rectangle $a \times b$ | $ab$ | $ab^3/12$ |
| Circle radius $R$ | $\pi R^2$ | $\pi R^4/4$ |
| Ellipse $a, b$ | $\pi ab$ | $\pi a b^3/4$ |
| Triangle base $a$, height $b$ | $ab/2$ | $ab^3/36$ |
| Semicircle radius $R$ | $\pi R^2/2$ | $0.1098\,R^4$ |

## Worked example: vertical rectangular gate

A vertical gate of width $w = 2$ m and height $b = 3$ m has its top edge at the water
surface ($P_0$ ignored — gauge pressure). Find $F_R$ and $y_P$.

Centroid depth: $y_C = b/2 = 1.5$ m, with $\theta = 90°$.

$$F_R = \rho g y_C A = 1000 \times 9.8 \times 1.5 \times 6 \approx 88\ \text{kN}$$

$$y_P = y_C + \frac{I_{xx,C}}{y_C A} = 1.5 + \frac{2\times 3^3/12}{1.5 \times 6} = 1.5 + 0.5 = 2.0\ \text{m}$$

The force acts at **two-thirds depth** — the classic result for a triangular pressure
distribution.

## Physical interpretation

- $F_R = P_C A$ works because pressure varies *linearly*: the mean of a linear
  distribution over the area is its value at the centroid.
- $y_P$ always lies **below** $y_C$ ($I_{xx,C} > 0$): deeper parts of the plate carry
  more load, dragging the effective point of action downward. As the plate goes very
  deep, $y_P \to y_C$ (pressure becomes nearly uniform).

## Common mistakes

- **Placing the resultant at the centroid.** The *magnitude* uses centroid pressure;
  the *location* is deeper.
- **Forgetting $\sin\theta$** for inclined surfaces — depth is $y\sin\theta$, not $y$.
- **Mixing up $I_{xx,C}$ and $I_{xx,O}$** — the compact formula uses the *centroidal*
  moment.

## Related concepts

- [Pressure](pressure.md) and [Hydrostatic equilibrium](hydrostatic-equilibrium.md) — the field being integrated
- [Buoyancy](buoyancy.md) — the same integral wrapped around a closed body

## Knowledge graph position

**Prerequisites:** [Hydrostatic equilibrium](hydrostatic-equilibrium.md).
**Leads to:** engineering statics of gates, dams, tanks.

## Quiz

**Q1 (conceptual).** For a fully submerged plate, does doubling the depth of submergence
change (i) the resultant force, (ii) the gap $y_P - y_C$?

??? success "Answer"
    (i) Yes — $F_R = \rho g y_C \sin\theta\, A$ grows linearly with centroid depth.
    (ii) It shrinks: $y_P - y_C = I_{xx,C}/(y_C A) \propto 1/y_C$. Deep plates feel
    nearly uniform pressure.

**Q2 (computational).** A circular porthole of radius 0.5 m has its center 10 m below
the surface. Total force?

??? success "Answer"
    $F_R = \rho g y_C A = 1000\times 9.8 \times 10 \times \pi(0.5)^2 \approx 77\ \text{kN}$
    — pressure at the center times area.

**Q3 (multiple choice).** The center of pressure coincides with the centroid when:

- (a) the plate is vertical  (b) the plate is horizontal  (c) never  (d) the fluid is a gas

??? success "Answer"
    **(b).** A horizontal plate sits at one depth — uniform pressure, so the resultant
    acts at the centroid. ((d) is nearly true in practice but not exactly.)
