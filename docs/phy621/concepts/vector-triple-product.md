# Vector Triple Product

*Source lecture(s):* [PC604 Lec1-2](../lectures.md)

## Intuition

Three vectors multiplied in succession introduce extra terms from expanding determinants.

## Formal Definition

The vector triple product identities rearrange products of three vectors.

## Mathematical Formulation

$$\vec{A}\times(\vec{B}\times\vec{C})=\vec{B}(\vec{A}\cdot\vec{C})-\vec{C}(\vec{A}\cdot\vec{B})$$

## Derivation

Expand component-wise using Levi-Civita symbols $\epsilon_{ijk}$ and the identity $\epsilon_{ijk}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$.

## Worked Example

If $\vec{A},\vec{C}$ are orthogonal, $\vec{A}\times(\vec{B}\times\vec{C})\approx -\vec{C}(\vec{A}\cdot\vec{B})$.

## Common Mistakes

- Treating triple product as associative.
- Dropping the $-(\vec{A}\cdot\vec{B})\vec{C}$ term.

## Related Concepts

- [Vector Operations](vector-operations.md)

## Quiz

**Q1.** What is $\hat{i}\times(\hat{j}\times\hat{k})$?

??? success "Answer"
    $\hat{j}(\hat{i}\cdot\hat{k})-\hat{k}(\hat{i}\cdot\hat{j})=0$.
