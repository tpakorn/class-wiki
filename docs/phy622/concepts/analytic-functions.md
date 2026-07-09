# Analytic Functions

*Source lecture(s):* [PHY622 Lec3](../lectures.md)

## Intuition

A function is analytic if it is differentiable everywhere in a neighborhood—this forces it to be smooth and conformal.

## Formal Definition

$f(z)$ is analytic at $z_0$ if $\lim_{z\to z_0}(f(z)-f(z_0))/(z-z_0)$ exists and is unique.

## Mathematical Formulation

Cauchy-Riemann: $u_x=v_y$ and $u_y=-v_x$ for $f=u+iv$.
Analytic $\implies$ $u_{xx}+u_{yy}=0$ (harmonic).

## Derivation

Write $f(z+\Delta z)-f(z)=\Delta z f'(z)+o(\Delta z)$. Separate real and imaginary axes; equating the two limits gives the CR equations.

## Worked Example

$f(z)=z^2$ has $u=x^2-y^2$, $v=2xy$, so $u_x=v_y=2x$ and $u_y=-v_x=-2y$.

## Common Mistakes

- Checking differentiability only along one path.
- Confusing 'analytic' with 'entire'.

## Related Concepts

- [Complex Numbers and Functions](complex-numbers.md)
- [Cauchy-Riemann Equations](cauchy-riemann.md)
- [Conformal Mapping](conformal-mapping.md)

## Quiz

**Q1.** If $f$ is analytic and $|f|$ is constant, what is $f$?

??? success "Answer"
    $f$ is constant.
