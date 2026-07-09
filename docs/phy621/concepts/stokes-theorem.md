# Stokes' Theorem

*Source lecture(s):* [PC604 Lec1-2](../lectures.md)

## Intuition

Circulation around a loop equals the integral of curl over any surface it bounds.

## Formal Definition

$$\oint_C \vec{A}\cdot d\vec{r}=\int_S (\nabla\times\vec{A})\cdot d\vec{S}$$

## Mathematical Formulation

$$\oint_C \vec{A}\cdot d\vec{r}=\int_S (\nabla\times\vec{A})\cdot d\vec{S}$$

## Derivation

Divide the surface into small loops; interior edges cancel, leaving only the outer boundary.

## Worked Example

For $\vec{A}=-y\hat{i}+x\hat{j}$ around the unit circle, $\oint \vec{A}\cdot d\vec{r}=2\pi$, matching $\int_S 2\hat{k}\cdot d\vec{S}=2\pi$.

## Common Mistakes

- Using the wrong orientation between loop and surface normal.
- Applying to surfaces with holes.

## Related Concepts

- [Gradient, Divergence, and Curl](gradient-divergence-curl.md)
- [Divergence Theorem](divergence-theorem.md)

## Quiz

**Q1.** Does Stokes' theorem apply to an open curve?

??? success "Answer"
    No—the curve must be closed.
