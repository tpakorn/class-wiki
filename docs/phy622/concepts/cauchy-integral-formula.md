# Cauchy's Integral Formula

*Source lecture(s):* [PHY622 Lec4](../lectures.md)

## Intuition

The value of an analytic function inside a contour is determined entirely by its values on the boundary.

## Formal Definition

$$f(z_0) = \frac{1}{2\pi i}\oint_C \frac{f(z)}{z-z_0}\,dz$$

## Mathematical Formulation

Repeated differentiation gives $f^{(n)}(z_0) = \frac{n!}{2\pi i}\oint_C \frac{f(z)}{(z-z_0)^{n+1}}\,dz$.

## Derivation

Apply the residue theorem to $f(z)/(z-z_0)$; the only pole inside $C$ is simple at $z_0$ with residue $f(z_0)$.

## Worked Example

$f(z)=z^2$ gives $f(0)=\frac{1}{2\pi i}\oint z^2/z\,dz = \frac{1}{2\pi i}\oint z\,dz = 0$ (since $z$ is analytic).

## Common Mistakes

- Applying when $f$ is not analytic inside $C$.
- Confusing the pole order in the $n$-th derivative formula.

## Related Concepts

- [Cauchy's Theorem](cauchy-theorem.md)
- [Residue Theorem](residue-theorem.md)

## Quiz

**Q1.** What does Cauchy's integral formula tell you about derivatives?

??? success "Answer"
    They are also given by contour integrals.
