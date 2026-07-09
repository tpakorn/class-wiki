# Hermitian Matrices

*Source lecture(s):* [PHY621 Lec2](../lectures.md)

## Intuition

Physical observables must have real eigenvalues. Hermitian matrices guarantee exactly that.

## Formal Definition

$A$ is Hermitian if $A=A^\dagger$ (conjugate transpose equals itself).

## Mathematical Formulation

$$A_{ij}=A_{ji}^*$$
$$\langle\psi|A|\psi\rangle\in\mathbb{R}$$

## Derivation

Take $\langle\psi|A|\psi\rangle$. Its conjugate equals itself iff $A=A^\dagger$, forcing $\lambda\in\mathbb{R}$.

## Worked Example

Pauli matrix $\sigma_z=\begin{pmatrix}1&0\\0&-1\end{pmatrix}$ is Hermitian with eigenvalues $\pm1$.

## Common Mistakes

- Confusing Hermitian ($A=A^\dagger$) with symmetric ($A=A^T$).
- Forgetting orthogonality of eigenvectors for distinct eigenvalues.

## Related Concepts

- [Eigenvalues and Eigenvectors](eigenvalues-eigenvectors.md)
- [Diagonalization](diagonalization.md)

## Quiz

**Q1.** Are eigenvalues of a Hermitian matrix always real?

??? success "Answer"
    Yes.
