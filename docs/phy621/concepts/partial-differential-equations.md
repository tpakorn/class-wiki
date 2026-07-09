# Partial Differential Equations

*Source lecture(s):* [PHY621 Lec6](../lectures.md)

## Intuition

PDEs describe fields varying in space and time. Classification tells you how information propagates.

## Formal Definition

Second-order linear PDE: $Au_{xx}+2Bu_{xy}+Cu_{yy}+\text{lower order}=0$. Discriminant $B^2-AC$ determines the type.

## Mathematical Formulation

Elliptic ($B^2-AC<0$): Laplace $\nabla^2 u=0$.
Parabolic ($B^2-AC=0$): Heat $u_t=\kappa\nabla^2 u$.
Hyperbolic ($B^2-AC>0$): Wave $u_{tt}=c^2\nabla^2 u$.

## Derivation

Try $u=X(x)Y(y)$; separation yields $X''/X + Y''/Y = 0$ for Laplace, so each equals a separation constant.

## Worked Example

Rectangle Laplace problem gives $\sinh$ and $\sin$ eigenfunctions matched to boundary temperatures.

## Common Mistakes

- Treating hyperbolic PDEs like parabolic (diffusion vs wave).
- Forgetting boundary conditions.

## Related Concepts

- [Ordinary Differential Equations](ordinary-differential-equations.md)
- [Green's Functions](greens-functions.md)

## Quiz

**Q1.** Which PDE class has no time evolution?

??? success "Answer"
    Elliptic.
