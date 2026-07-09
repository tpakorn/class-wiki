# Dielectrics

*Source lecture(s):* [SC134 Lec6](../lectures.md)

## Intuition

Insulating materials polarize in an electric field, reducing the internal field and increasing capacitance.

## Formal Definition

A dielectric reduces the effective field by factor $\kappa$ (dielectric constant).

## Mathematical Formulation

$$\vec{E} = \frac{\vec{E}_0}{\kappa}$$
$$C = \kappa C_0$$

## Derivation

Polarization $\vec{P}$ produces bound surface charge $\sigma_b = \vec{P}\cdot\hat{n}$. Gauss's law with $D=\varepsilon_0 E + P$ gives $D = \varepsilon_0\kappa E$.

## Worked Example

Inserting dielectric ($\kappa=5$) into isolated charged capacitor reduces $E$ by 5, increases $C$ by 5, and leaves $Q$ unchanged.

## Common Mistakes

- Forgetting $Q$ is fixed when capacitor is isolated.
- Confusing $\kappa$ with resistivity.

## Related Concepts

- [Capacitance](capacitance.md)
- [Gauss's Law](gauss-law.md)

## Quiz

**Q1.** What happens to stored energy when dielectric is inserted with battery connected?

??? success "Answer"
    Energy increases; battery does work.
