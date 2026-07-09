# Vector Operations

*Source lecture(s):* [PC604 Lec1-2, PHY621 Lec1](../lectures.md)

## Intuition

Vectors carry magnitude and direction. Every oriented physical quantity—force, velocity, torque—needs vector algebra.

## Formal Definition

A vector $\vec{A}\in\mathbb{R}^3$ has components $A_x,A_y,A_z$. Dot product yields a scalar; cross product yields a vector perpendicular to both.

## Mathematical Formulation

$$\vec{A}\cdot\vec{B}=A_xB_x+A_yB_y+A_zB_z$$
$$\vec{A}\times\vec{B}=\begin{vmatrix}\hat{i}&\hat{j}&\hat{k}\\ A_x&A_y&A_z\\ B_x&B_y&B_z\end{vmatrix}$$

## Derivation

The dot product follows from projecting one vector onto the other. The cross product magnitude equals the area of the parallelogram formed by $\vec{A}$ and $\vec{B}$.

## Worked Example

For $\vec{A}=3\hat{i}+4\hat{j}$ and $\vec{B}=\hat{i}+2\hat{j}+2\hat{k}$, $\vec{A}\cdot\vec{B}=11$ and $|\vec{A}|=5$.

## Common Mistakes

- Using $|\vec{A}||\vec{B}|$ for non-parallel vectors in the dot product.
- Forgetting anti-commutativity $\vec{A}\times\vec{B}=-\vec{B}\times\vec{A}$.

## Related Concepts

- [Vector Triple Product](vector-triple-product.md)
- [Coordinate Systems](coordinate-systems.md)

## Quiz

**Q1.** When is $\vec{A}\times\vec{B}$ parallel to $\vec{A}$?

??? success "Answer"
    When $\vec{B}$ has no component perpendicular to $\vec{A}$.

**Q2.** What does $\vec{A}\cdot\vec{B}=0$ imply?

??? success "Answer"
    The vectors are perpendicular.
