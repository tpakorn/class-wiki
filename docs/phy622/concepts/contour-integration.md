# Contour Integration

*Source lecture(s):* [PHY622 Lec4](../lectures.md)

## Intuition

By closing the integration path in the complex plane, real integrals become contour integrals whose values come from residues.

## Formal Definition

The technique of evaluating real integrals by integrating an analytic function over a closed contour in the complex plane.

## Mathematical Formulation

Key contour: real axis + large semicircle in the upper half-plane (Jordan's lemma).

## Derivation

Choose a contour that simplifies the integral (semicircle, keyhole, wedge). Show the arc contribution vanishes as radius $\to\infty$; the real integral equals $2\pi i$ times enclosed residues.

## Worked Example

$\int_{-\infty}^\infty \frac{dx}{1+x^2}=\pi$ via semicircle enclosing $z=i$.

## Common Mistakes

- Forgetting to check arc contributions vanish.
- Choosing the wrong half-plane for oscillatory integrals.

## Related Concepts

- [Residue Theorem](residue-theorem.md)
- [Conformal Mapping](conformal-mapping.md)

## Quiz

**Q1.** When does Jordan's lemma apply?

??? success "Answer"
    For integrals of $e^{ikz}f(z)$ with $k>0$ and $f\to0$ on a large semicircle.
