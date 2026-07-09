# Conformal Mapping & the Complex Potential

## Intuition

In two dimensions, [potential flow](potential-flow.md) has a superpower: the potential
$\phi$ and stream function $\psi$ pair up into a single *analytic* complex function.
Anything complex analysis can do — and it can do a lot — becomes a fluid-mechanics
tool. In particular: if you can solve the flow around a *circle*, a clever change of
complex variable hands you the flow around an *airfoil* for free.

## Formal definition

Define the **complex potential** on $z = x + iy$:

$$F(z) = \phi(x, y) + i\,\psi(x, y)$$

Because $\phi, \psi$ satisfy the Cauchy–Riemann equations, $F$ is analytic, and its
derivative packages the velocity:

$$\frac{dF}{dz} = u - iv$$

A **conformal map** is an analytic function $w = f(z)$ carrying one flow domain to
another. It preserves angles (hence "conformal"), and — crucially — it preserves
irrotationality and incompressibility, so *solutions map to solutions*.

## The Joukowski transformation

$$\boxed{\,w = z + \frac{c^2}{z}\,}$$

maps a circle in the $z$-plane into an airfoil-like shape in the $w$-plane (an offset
circle gives a cambered airfoil with a sharp trailing edge). Since the flow past a
cylinder (uniform + doublet + vortex) is known exactly, the flow past a Joukowski
airfoil follows by substitution — including the circulation and hence the **lift**
(Kutta–Joukowski theorem: $L' = \rho U \Gamma$).

## Riemann mapping theorem

> Any simply connected region of the plane (other than the whole plane) can be
> conformally mapped onto the unit disk.

For fluid mechanics this is an existence guarantee: *every* 2-D irrotational
incompressible flow in a simply connected domain is, up to a map, the flow in a disk.
Solving one canonical problem solves them all in principle; the craft is finding the
map.

## Method of images (boundary conditions for free)

Solid boundaries demand zero normal velocity. Instead of solving a boundary-value
problem, place fictitious singularities so symmetry enforces the condition:

- **Wall:** source $Q$ at $(a,0)$ + image source $Q$ at $(-a,0)$ ⇒ the $x$-axis becomes
  a streamline.
- **Cylinder:** the Milne-Thomson circle theorem inserts an image system inside the
  cylinder so its surface is a streamline.

## Common mistakes

- **Using a non-analytic "map".** Only analytic (holomorphic, $f'(z)\neq 0$) functions
  preserve the flow equations; $|z|$ or $\bar z$ tricks break everything.
- **Forgetting the velocity transforms too:** velocities in the mapped plane pick up a
  factor $1/|f'(z)|$; speeds are *not* copied verbatim.
- **Ignoring the trailing-edge (Kutta) condition** when computing airfoil lift — the
  physical flow selects the circulation that leaves the sharp edge smoothly.

## Related concepts

- [Potential flow](potential-flow.md) — the theory this machinery serves
- [Laplace's equation](../equations/laplace-equation.md) — invariant under conformal maps
- [Bernoulli's principle](bernoulli-principle.md) — converts mapped velocities into pressures and lift

## Knowledge graph position

**Prerequisites:** [Potential flow](potential-flow.md), complex analysis (from
[PHY622-level math methods](../../index.md)).
**Leads to:** airfoil theory, advanced hydrodynamics.

## Quiz

**Q1 (conceptual).** Why does the Joukowski map produce a *sharp* trailing edge from a
smooth circle?

??? success "Answer"
    The map $w = z + c^2/z$ has $f'(z) = 1 - c^2/z^2 = 0$ at $z = \pm c$. Conformality
    fails exactly at those critical points — angles are *not* preserved there, and the
    smooth circle acquires a cusp.

**Q2 (multiple choice).** The complex velocity is:

- (a) $u + iv$  (b) $u - iv$  (c) $v + iu$  (d) $|\mathbf{v}|e^{i\theta}$

??? success "Answer"
    **(b).** $dF/dz = \phi_x + i\psi_x = u - iv$ by Cauchy–Riemann.

**Q3 (computational).** A source of strength $Q$ sits at distance $a$ from a rigid
wall. What is the fluid speed at the wall point nearest the source?

??? success "Answer"
    Source + image each contribute $\frac{Q}{2\pi a}$... their normal components cancel,
    tangential components cancel *at the foot point* by symmetry — the nearest wall
    point is a stagnation point with speed $0$. (Maximum wall speed occurs at
    $x = \pm a$ along the wall, $|u| = \frac{Q}{2\pi a}$.)
