# DC Circuits

*Source lecture(s):* [SC134 Lec8](../lectures.md)

## Intuition

Kirchhoff's rules enforce charge and energy conservation around loops and junctions.

## Formal Definition

Loop rule: $\sum \mathcal{E} - \sum IR = 0$.
Junction rule: $\sum I_{\text{in}} = \sum I_{\text{out}}$.

## Mathematical Formulation

Series: $R_{\text{eq}} = \sum R_i$
Parallel: $1/R_{\text{eq}} = \sum 1/R_i$
RC charge: $q(t) = C\mathcal{E}(1-e^{-t/RC})$
Time constant: $\tau = RC$

## Derivation

Apply Kirchhoff's loop rule to the RC circuit; solve first-order linear ODE for $q(t)$.

## Worked Example

$R=2\,\text{k}\Omega$, $C=1\,\mu\text{F}$: $\tau=2\,\text{ms}$.

## Common Mistakes

- Forgetting battery polarity in loop rule.
- Setting $V$ across capacitor to zero immediately after connection.

## Related Concepts

- [Current, Resistance, and Resistivity](current-resistance.md)
- [RC Circuits](rc-circuits.md)

## Quiz

**Q1.** Does current through series resistors differ?

??? success "Answer"
    No—same current everywhere.
