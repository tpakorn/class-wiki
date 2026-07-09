# Coordinate Systems

*Source lecture(s):* [PC604 Lec1-2](../lectures.md)

## Intuition

Symmetry dictates which coordinates simplify a problem.

## Formal Definition

A coordinate system assigns a unique triplet $(q_1,q_2,q_3)$ to each point. The Jacobian converts volume elements.

## Mathematical Formulation

Cartesian: $dV=dx\,dy\,dz$
Cylindrical: $dV=r\,dr\,d\phi\,dz$
Spherical: $dV=r^2\sin\theta\,dr\,d\theta\,d\phi$

## Derivation

In cylindrical coordinates $\vec{r}=r\hat{e}_r+z\hat{e}_z$. The scale factors are $h_r=1$, $h_\phi=r$, $h_z=1$, so $dV=h_r h_\phi h_z\,dr\,d\phi\,dz=r\,dr\,d\phi\,dz$.

## Worked Example

Sphere volume: $V=\int_0^R r^2\,dr\int_0^\pi\sin\theta\,d\theta\int_0^{2\pi}d\phi=\frac{4}{3}\pi R^3$.

## Common Mistakes

- Forgetting the Jacobian when changing variables.
- Swapping $\theta$ and $\phi$ in spherical coordinates.

## Related Concepts

- [Vector Operations](vector-operations.md)
- [Gradient, Divergence, and Curl](gradient-divergence-curl.md)

## Quiz

**Q1.** What is the Jacobian for cylindrical coordinates?

??? success "Answer"
    $r$.

**Q2.** Which coordinate has $\hat{e}_\phi$ depend on position?

??? success "Answer"
    Cylindrical and spherical.
