# Electric Dipole

*Source lecture(s):* [SC134 Lec3, Lec5](../lectures.md)

## Intuition

A positive and negative charge separated by a tiny distance create a directional field that behaves differently at close vs far range.

## Formal Definition

Dipole moment $\vec{p} = q\vec{d}$ from negative to positive charge.

## Mathematical Formulation

$$V = \frac{1}{4\pi\varepsilon_0}\frac{\vec{p}\cdot\hat{r}}{r^2}$$
$$\vec{E} = \frac{1}{4\pi\varepsilon_0}\frac{1}{r^3}[3(\vec{p}\cdot\hat{r})\hat{r} - \vec{p}]$$

## Derivation

Superpose fields of $+q$ and $-q$ at distance $r\gg d$; keep leading $1/r^2$ and $1/r^3$ terms.

## Worked Example

In a uniform field, a dipole aligns with the field ($U=-pE\cos\theta$).

## Common Mistakes

- Confusing $p=qd$ with $p=q/2d$.
- Using point-dipole formula at $r\sim d$.

## Related Concepts

- [Electric Field](electric-field.md)
- [Electric Potential](electric-potential.md)
- [Electric Force on Charges](electric-force.md)

## Quiz

**Q1.** What is the far-field behavior of a dipole?

??? success "Answer"
    Falls as $1/r^3$.
