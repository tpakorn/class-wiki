# Special Functions

*Source lecture(s):* [PHY621 Lec5](../lectures.md)

## Intuition

Bessel, Legendre, and other named functions recur so often in physics that they deserve catalog entries.

## Formal Definition

Bessel $J_n(x)$ solves $x^2y''+xy'+(x^2-n^2)y=0$. Legendre $P_l(x)$ solves $(1-x^2)y''-2xy'+l(l+1)y=0$.

## Mathematical Formulation

$$J_n(x)=\sum_{m=0}^\infty \frac{(-1)^m}{m!(m+n)!}\left(\frac{x}{2}\right)^{2m+n}$$

## Derivation

Use Frobenius series $y=\sum a_m x^{m+r}$; equate lowest-power terms to find $r$ and recurrences.

## Worked Example

Small-$x$ behavior: $J_0(x)\approx1-\frac{x^2}{4}$.

## Common Mistakes

- Using Bessel $Y_n$ without checking singular behavior at $x=0$.
- Using a weight function for Legendre orthogonality — $P_l$ are orthogonal on $[-1,1]$ with weight $1$ (the weight $(1-x^2)^{-1/2}$ belongs to Chebyshev polynomials).

## Related Concepts

- [Ordinary Differential Equations](ordinary-differential-equations.md)
- [Fourier Series](fourier-series.md)

## Quiz

**Q1.** What ODE defines Bessel functions of order $n$?

??? success "Answer"
    $x^2y''+xy'+(x^2-n^2)y=0$.
