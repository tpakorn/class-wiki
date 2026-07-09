# Diagonalization

*Source lecture(s):* [PHY621 Lec2](../lectures.md)

## Intuition

If a matrix has enough eigenvectors, rotate coordinates so the matrix becomes diagonal.

## Formal Definition

$A$ is diagonalizable if $A=PDP^{-1}$ where $D$ is diagonal and $P$ contains eigenvectors as columns.

## Mathematical Formulation

$$A=P\,\text{diag}(\lambda_1,\ldots,\lambda_N)\,P^{-1}$$

## Derivation

Write $AP=PD$. The $j$-th column gives $A\vec{v}_j=\lambda_j\vec{v}_j$, which is exactly the eigenvalue equation.

## Worked Example

A diagonal matrix is already in the form $D$; its eigenvectors are the standard basis.

## Common Mistakes

- Assuming every matrix is diagonalizable.
- Using the same eigenvector for repeated roots without checking degeneracy.

## Related Concepts

- [Eigenvalues and Eigenvectors](eigenvalues-eigenvectors.md)
- [Hermitian Matrices](hermitian-matrices.md)

## Quiz

**Q1.** What guarantees diagonalizability?

??? success "Answer"
    Distinct eigenvalues or a complete set of linearly independent eigenvectors.
