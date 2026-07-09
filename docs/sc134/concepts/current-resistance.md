# Current, Resistance, and Resistivity

*Source lecture(s):* [SC134 Lec8](../lectures.md)

## Intuition

Materials impede charge flow; resistivity is an intrinsic property, resistance depends on geometry.

## Formal Definition

Ohm's law: $V = IR$.
Resistivity: $\rho = RA/L$
Conductivity: $\sigma = 1/\rho$

## Mathematical Formulation

$$R = \rho\frac{L}{A}$$
Power: $$P = IV = I^2R = V^2/R$$

## Derivation

Drude model: $v_d = \mu E$, $J = \sigma E$, so $V = EL = (\rho L/A)I$.

## Worked Example

1 km of 1 mm$^2$ copper ($\rho=1.7\times10^{-8}\,\Omega\cdot\text{m}$): $R = \rho L/A = 1.7\times10^{-8}\times 10^3/10^{-6} = 17\,\Omega$ — why long, thin cables need thick copper.

## Common Mistakes

- Confusing series vs parallel combination rules.
- Using copper resistivity for nichrome.

## Related Concepts

- [Electric Current](electric-current.md)
- [DC Circuits](dc-circuits.md)

## Quiz

**Q1.** If length doubles and area halves, what happens to R?

??? success "Answer"
    It quadruples.
