# Gradient, Divergence, and Curl

*Source lecture(s):* [PC604 Lec1-2, PHY621 Lec1](../lectures.md)

## Intuition

Gradient points uphill; divergence measures source strength; curl measures local circulation.

## Formal Definition

For scalar field $\phi$ and vector field $\vec{A}$: $\nabla\phi$, $\nabla\cdot\vec{A}$, $\nabla\times\vec{A}$.

## Mathematical Formulation

$$\nabla\phi=\hat{e}_i\frac{\partial\phi}{\partial x_i}$$
$$\nabla\cdot\vec{A}=\frac{\partial A_i}{\partial x_i}$$
$$\nabla\times\vec{A}=\epsilon_{ijk}\hat{e}_i\frac{\partial A_k}{\partial x_j}$$

## Derivation

In curvilinear coordinates insert scale factors $h_i$. For Cartesian $h_i=1$, this collapses to the familiar forms.

## Worked Example

For $\vec{A}=x\hat{i}+y\hat{j}+z\hat{k}$, $\nabla\cdot\vec{A}=3$. For $\vec{A}=-y\hat{i}+x\hat{j}$, $\nabla\times\vec{A}=2\hat{k}$.

## Common Mistakes

- Treating $\nabla$ as a regular vector when differentiating products.
- Assuming zero divergence means no field variation.

## Related Concepts

- [Coordinate Systems](coordinate-systems.md)
- [Divergence Theorem](divergence-theorem.md)
- [Stokes' Theorem](stokes-theorem.md)

## Quiz

**Q1.** What does $\nabla\cdot\vec{A}=0$ mean physically?

??? success "Answer"
    No net source or sink in the field.

**Q2.** What does $\nabla\times\nabla\phi$ equal?

??? success "Answer"
    Zero.
