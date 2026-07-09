# Lagrange Multipliers (Variational)

*Source lecture(s):* [PHY622 Lec1](../lectures.md)

## Intuition

Constraints turn free variation problems into constrained ones by adding a term that penalizes constraint violations.

## Formal Definition

For constraint $G[y]=0$, extremize $\int (F+\lambda G)\,dx$. The multiplier $\lambda(x)$ enforces the constraint.

## Mathematical Formulation

$$\frac{\partial}{\partial y}(F+\lambda G) - \frac{d}{dx}\frac{\partial}{\partial y'}(F+\lambda G) = 0$$
$$G[y]=0$$

## Derivation

Lagrange undetermined multiplier method: require stationarity of $J+\lambda G$ with respect to both $y$ and $\lambda$.

## Worked Example

Brachistochrone under gravity with fixed endpoints uses $F=\sqrt{(1+y'^2)/2gy}$.

## Common Mistakes

- Treating $\lambda$ as a constant when it can be an arbitrary function of $x$.
- Forgetting natural boundary conditions from fixed endpoints.

## Related Concepts

- [Calculus of Variations](calculus-of-variations.md)
- [Geodesics](geodesics.md)
- [Minimal Surfaces](minimal-surfaces.md)

## Quiz

**Q1.** What does the multiplier $\lambda$ represent physically?

??? success "Answer"
    A generalized force that enforces the constraint.
