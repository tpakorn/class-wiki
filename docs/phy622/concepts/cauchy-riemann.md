# Cauchy-Riemann Equations

*Source lecture(s):* [PHY622 Lec3](../lectures.md)

## Intuition

Differentiability in the complex plane imposes two coupled real equations, far stricter than real differentiability.

## Formal Definition

For $f=u+iv$, $\partial u/\partial x = \partial v/\partial y$ and $\partial u/\partial y = -\partial v/\partial x$.

## Mathematical Formulation

$$\frac{\partial u}{\partial x}=\frac{\partial v}{\partial y}, \quad \frac{\partial u}{\partial y}=-\frac{\partial v}{\partial x}$$

## Derivation

Write $\Delta z$ along real ($\Delta x$) and imaginary ($i\Delta y$) axes. The limit must be unique, giving two equations.

## Worked Example

For $f(z)=e^z=e^x(\cos y+i\sin y)$, CR gives $u_x=v_y=e^x\cos y$ and $u_y=-v_x=-e^x\sin y$.

## Common Mistakes

- Checking only one of the two equations.
- Assuming CR guarantees analyticity everywhere (need continuous partials).

## Related Concepts

- [Analytic Functions](analytic-functions.md)
- [Complex Numbers and Functions](complex-numbers.md)

## Quiz

**Q1.** Are the Cauchy-Riemann equations sufficient alone?

??? success "Answer"
    No—need continuous partial derivatives.
