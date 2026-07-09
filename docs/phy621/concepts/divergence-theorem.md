# Divergence Theorem

*Source lecture(s):* [PC604 Lec1-2](../lectures.md)

## Intuition

Sources inside a volume push flux out through its surface.

## Formal Definition

$$\oint_S \vec{A}\cdot d\vec{S}=\int_V (\nabla\cdot\vec{A})\,dV$$

## Mathematical Formulation

$$\oint_S \vec{A}\cdot d\vec{S}=\int_V (\nabla\cdot\vec{A})\,dV$$

## Derivation

Apply the fundamental theorem in each Cartesian direction and sum.

## Worked Example

For $\vec{A}=x\hat{i}$ through the unit cube, flux is $1$, matching $\int_V 1\,dV=1$.

## Common Mistakes

- Forgetting the outward normal on $d\vec{S}$.
- Applying to non-closed surfaces.

## Related Concepts

- [Gradient, Divergence, and Curl](gradient-divergence-curl.md)
- [Stokes' Theorem](stokes-theorem.md)

## Quiz

**Q1.** Can the divergence theorem be applied to a hollow sphere?

??? success "Answer"
    Yes—include both inner and outer surfaces.
