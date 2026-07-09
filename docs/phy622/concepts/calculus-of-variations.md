# Calculus of Variations

*Source lecture(s):* [PHY622 Lec1-2](../lectures.md)

## Intuition

Instead of finding maxima/minima of a function, we find curves that make a functional stationary.

## Formal Definition

Given a functional $J[y]=\int_{x_0}^{x_1} F(x,y,y')\,dx$, the extremal satisfies the Euler-Lagrange equation.

## Mathematical Formulation

$$\frac{\partial F}{\partial y} - \frac{d}{dx}\frac{\partial F}{\partial y'} = 0$$

## Derivation

Consider a variation $y(x)\to y(x)+\epsilon\eta(x)$ with fixed endpoints. First-order change $\delta J=0$ for arbitrary $\eta$ yields the EL equation after integration by parts.

## Worked Example

For $F=y'^2$, EL gives $y''=0$, so the extremal is a straight line.

## Common Mistakes

- Forgetting the $d/dx$ acting on $\partial F/\partial y'$.
- Applying EL when $F$ depends on higher derivatives ($y''$) without modification.

## Related Concepts

- [Euler-Lagrange Equation](euler-lagrange-equation.md)
- [Lagrange Multipliers (Variational)](lagrange-multipliers.md)
- [Hamilton's Principle](hamilton-principle.md)

## Quiz

**Q1.** What does 'stationary' mean in calculus of variations?

??? success "Answer"
    $\delta J=0$; it could be minimum, maximum, or saddle.
