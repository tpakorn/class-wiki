# Euler-Lagrange Equation

*Source lecture(s):* [PHY622 Lec1](../lectures.md)

## Intuition

The condition for a curve to extremize a functional is a differential equation.

## Formal Definition

For $J[y]=\int F(x,y,y')\,dx$, the Euler-Lagrange equation is $F_y - d/dx(F_{y'}) = 0$.

## Mathematical Formulation

$$\frac{\partial F}{\partial y} - \frac{d}{dx}\frac{\partial F}{\partial y'} = 0$$

## Derivation

Perturb $y\to y+\epsilon\eta$, require $\delta J=0$ for arbitrary $\eta$, integrate $\int (F_y\eta + F_{y'}\eta')\,dx$ by parts.

## Worked Example

Shortest path in a plane has $F=\sqrt{1+y'^2}$, giving $d/dx(y'/\sqrt{1+y'^2})=0$, so $y'=$ const—a straight line.

## Common Mistakes

- Dropping boundary terms incorrectly.
- Using $F$ instead of $F_y$.

## Related Concepts

- [Calculus of Variations](calculus-of-variations.md)
- [Geodesics](geodesics.md)

## Quiz

**Q1.** When does the Euler-Lagrange equation reduce to $F_{y'}=$ const?

??? success "Answer"
    When $F$ is independent of $y$.
