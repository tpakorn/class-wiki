# Orthogonal Transformations

*Source lecture(s):* [PHY621 Lec1-2](../lectures.md)

## Intuition

Rotations and reflections preserve lengths and angles—they are Euclidean symmetries.

## Formal Definition

An orthogonal matrix $R$ satisfies $R^TR=RR^T=I$, so $R^{-1}=R^T$.

## Mathematical Formulation

$$R_z(\theta)=\begin{pmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{pmatrix}$$

## Derivation

The determinant condition preserves volume. In 3D, Rodrigues' formula builds any rotation from axis $\hat{n}$ and angle $\theta$.

## Worked Example

$90^\circ$ rotation about $z$ sends $(1,0,0)\mapsto(0,1,0)$.

## Common Mistakes

- Assuming all orthogonal matrices are pure rotations (det $=-1$ reflects).
- Using Euler angles without checking ranges.

## Related Concepts

- [Matrices and Determinants](matrices-determinants.md)
- [Eigenvalues and Eigenvectors](eigenvalues-eigenvectors.md)

## Quiz

**Q1.** What is $\det R$ for a proper rotation?

??? success "Answer"
    $+1$.
