# RC Circuits

*Source lecture(s):* [SC134 Lec8, Lec9](../lectures.md)

## Intuition

A resistor and capacitor together define an exponential timescale—fast for small $RC$, slow for large.

## Formal Definition

Charging: $q(t) = C\mathcal{E}(1-e^{-t/RC})$
Discharging: $q(t) = Q_0 e^{-t/RC}$

## Mathematical Formulation

Current: $i(t) = \frac{\mathcal{E}}{R}e^{-t/RC}$ (charging)
Voltage across C: $V_C(t) = \mathcal{E}(1-e^{-t/RC})$

## Derivation

Kirchhoff loop rule $\mathcal{E} - iR - q/C = 0$; substitute $i=dq/dt$; solve separable ODE.

## Worked Example

$\tau=RC=2\,\text{ms}$ reaches $63\%$ charge in 2 ms.

## Common Mistakes

- Using $\tau=RC$ for RL circuits by accident (valid there too, but check values).
- Confusing $i$ and $q$ exponential forms.

## Related Concepts

- [DC Circuits](dc-circuits.md)
- [Current, Resistance, and Resistivity](current-resistance.md)

## Quiz

**Q1.** What fraction of final charge does an RC circuit reach at $t=\tau$?

??? success "Answer"
    $1-e^{-1}\approx 63\%$.
