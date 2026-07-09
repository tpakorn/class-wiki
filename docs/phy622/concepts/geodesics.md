# Geodesics

*Source lecture(s):* [PHY622 Lec1](../lectures.md)

## Intuition

A geodesic is the shortest path between two points on a curved surface.

## Formal Definition

A curve that locally extremizes arc length on a manifold.

## Mathematical Formulation

Arc length: $L=\int\sqrt{g_{ij}\dot{x}^i\dot{x}^j}\,dt$. Geodesic equation: $\ddot{x}^k + \Gamma^k_{ij}\dot{x}^i\dot{x}^j = 0$.

## Derivation

Apply Euler-Lagrange to the arc-length functional in generalized coordinates; Christoffel symbols $\Gamma$ encode the metric derivatives.

## Worked Example

On a sphere of radius $R$, great circles are geodesics.

## Common Mistakes

- Assuming geodesics are unique between any two points.
- Ignoring conjugate points.

## Related Concepts

- [Euler-Lagrange Equation](euler-lagrange-equation.md)
- [Lagrange Multipliers (Variational)](lagrange-multipliers.md)

## Quiz

**Q1.** Are great circles on Earth geodesics?

??? success "Answer"
    Yes—locally shortest paths.
