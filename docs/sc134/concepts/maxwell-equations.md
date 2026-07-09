# Maxwell's Equations

*Source lecture(s):* [SC134 Lec13-14](../lectures.md)

## Intuition

Four equations summarize all of classical electromagnetism, unifying electricity, magnetism, and light.

## Formal Definition

Gauss E: $\oint E\cdot dA = q_{\text{enc}}/\varepsilon_0$
Gauss B: $\oint B\cdot dA = 0$
Faraday: $\oint E\cdot dl = -d\Phi_B/dt$
Ampere-Maxwell: $\oint B\cdot dl = \mu_0 i_{\text{enc}} + \mu_0\varepsilon_0 d\Phi_E/dt$

## Mathematical Formulation

Differential form:
$\nabla\cdot E = \rho/\varepsilon_0$
$\nabla\cdot B = 0$
$\nabla\times E = -\partial B/\partial t$
$\nabla\times B = \mu_0 J + \mu_0\varepsilon_0\partial E/\partial t$

## Derivation

Maxwell added displacement current $\mu_0\varepsilon_0 d\Phi_E/dt$ to Ampere's law to restore continuity; combined with Faraday's law they predict EM waves.

## Worked Example

Electromagnetic wave in vacuum: $E = cB$, $c = 1/\sqrt{\mu_0\varepsilon_0} \approx 3\times10^8\,\text{m/s}$.

## Common Mistakes

- Forgetting displacement current in Ampere's law.
- Treating Maxwell's equations as independent rather than coupled PDEs.

## Related Concepts

- [Faraday's Law of Induction](faraday-law.md)
- [Gauss's Law for Magnetism](gauss-law-magnetism.md)
- [Electromagnetic Waves](electromagnetic-waves.md)

## Quiz

**Q1.** Which term makes Maxwell's equations predict EM waves?

??? success "Answer"
    Displacement current.
