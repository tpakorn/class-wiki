# Faraday's Law of Induction

*Source lecture(s):* [SC134 Lec11-13](../lectures.md)

## Intuition

A changing magnetic flux through a loop induces an EMF—generators and transformers run on this.

## Formal Definition

$$\mathcal{E} = -\frac{d\Phi_B}{dt}$$
Magnetic flux: $\Phi_B = \int \vec{B}\cdot d\vec{A}$

## Mathematical Formulation

For $N$ turns: $\mathcal{E} = -N\,d\Phi_B/dt$
Inductance: $\mathcal{E} = -L\,di/dt$
Energy: $U = \frac{1}{2}Li^2$

## Derivation

Empirical law from Faraday's experiments; Maxwell added displacement current term $\varepsilon_0 d\Phi_E/dt$ to Ampere's law.

## Worked Example

Sinusoidal flux $\Phi = \Phi_0\sin\omega t$ gives $\mathcal{E} = -\omega\Phi_0\cos\omega t$.

## Common Mistakes

- Dropping the minus sign (Lenz's law).
- Confusing flux linkage $N\Phi$ with single-loop flux.

## Related Concepts

- [Magnetic Flux](magnetic-flux.md)
- [Maxwell's Equations](maxwell-equations.md)

## Quiz

**Q1.** What does the minus sign represent physically?

??? success "Answer"
    Lenz's law: induced EMF opposes the change.
