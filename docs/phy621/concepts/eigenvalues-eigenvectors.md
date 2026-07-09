# Eigenvalues and Eigenvectors

*Source lecture(s):* [PHY621 Lec2](../lectures.md)

## Intuition

Some directions survive linear transformation unchanged except for a scale factor—those are eigenvectors.

## Formal Definition

Non-zero $\vec{v}$ with $A\vec{v}=\lambda\vec{v}$ is an eigenvector; $\lambda$ is the eigenvalue.

## Mathematical Formulation

$$\det(A-\lambda I)=0$$
$$A\vec{v}=\lambda\vec{v}$$

## Derivation

Subtract $\lambda I$: $(A-\lambda I)\vec{v}=0$. Non-trivial $\vec{v}$ exists iff $\det(A-\lambda I)=0$.

## Worked Example

$A=\begin{pmatrix}2&0\\0&3\end{pmatrix}$ has eigenvectors $\hat{i},\hat{j}$ with eigenvalues $2,3$.

## Common Mistakes

- Normalizing when computing eigenvalues.
- Confusing eigenvalues with eigenvectors.

## Related Concepts

- [Matrices and Determinants](matrices-determinants.md)
- [Diagonalization](diagonalization.md)

## Quiz

**Q1.** If $A\vec{v}=\lambda\vec{v}$, what is $A^2\vec{v}$?

??? success "Answer"
    $\lambda^2\vec{v}$.
