# Ordinary Differential Equations

*Source lecture(s):* [PHY621 Lec5](../lectures.md)

## Intuition

ODE rules tell us how a quantity changes continuously. Solutions respond to boundary and initial conditions.

## Formal Definition

An ODE of order $n$ involves derivatives up to $f^{(n)}(x)$. Linear form: $a_n(x)y^{(n)}+\cdots+a_0(x)y=g(x)$.

## Mathematical Formulation

Second-order linear ODE: $y''+p(x)y'+q(x)y=r(x)$. Homogeneous when $r=0$.

## Derivation

For constant coefficients, substitute $y=e^{rx}$ to get the characteristic polynomial $a_n r^n+\cdots+a_0=0$.

## Worked Example

$y''-3y'+2y=0$ gives $r^2-3r+2=0$, so $r=1,2$ and $y=C_1e^x+C_2e^{2x}$.

## Common Mistakes

- Forgetting linearly independent solutions for repeated roots.
- Adding $\ln|x|$ for Cauchy-Euler without verifying $x>0$.

## Related Concepts

- [Special Functions](special-functions.md)
- [Partial Differential Equations](partial-differential-equations.md)

## Quiz

**Q1.** What is the general solution of $y''+k^2y=0$?

??? success "Answer"
    $y=A\cos(kx)+B\sin(kx)$.
