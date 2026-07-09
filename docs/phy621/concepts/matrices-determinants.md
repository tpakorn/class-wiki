# Matrices and Determinants

*Source lecture(s):* [PHY621 Lec1](../lectures.md)

## Intuition

Matrices compress many simultaneous linear equations into one compact object. The determinant tells you whether the map is invertible.

## Formal Definition

An $N\times N$ matrix $\mathbf{A}$ maps $\vec{x}\mapsto\vec{b}=A\vec{x}$. The determinant $\det\mathbf{A}$ scales volume under this map.

## Mathematical Formulation

$$\det\mathbf{A}=\sum_{\sigma}\text{sgn}(\sigma)\prod_{i=1}^N A_{i,\sigma(i)}$$

## Derivation

The determinant is the unique multilinear, alternating $N$-linear function with $\det\mathbf{I}=1$. Laplace expansion computes it from any row or column.

## Worked Example

$A=\begin{pmatrix}1&2\\3&4\end{pmatrix}$ has $\det A = 1\cdot4-2\cdot3=-2$.

## Common Mistakes

- Multiplying diagonal entries for non-triangular matrices.
- Confusing $\det(AB)$ with $\det A+\det B$.

## Related Concepts

- [Eigenvalues and Eigenvectors](eigenvalues-eigenvectors.md)

## Quiz

**Q1.** When is a matrix singular?

??? success "Answer"
    When its determinant is zero.

**Q2.** Does $\det(A^T)=\det A$?

??? success "Answer"
    Yes.
