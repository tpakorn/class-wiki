# Quizzes · Electromagnetism

Integrative questions across the course — every concept page carries its own quiz too.
Follow the [lecture timeline](lectures.md) to study in order.

## Conceptual

**Q1.** Why does a negative charge move opposite to electric field lines?

??? success "Answer"
    Field direction is *defined* by the force on a **positive** test charge
    ($\vec F = q\vec E$); flip the sign of $q$ and the force flips.

**Q2.** Why can two equipotential surfaces never cross?

??? success "Answer"
    A crossing point would have two different potentials at once — contradiction.
    (Equivalently: $\vec E = -\nabla V$ would be undefined there.)

**Q3.** Why does changing magnetic flux induce an EMF, even with no battery anywhere?

??? success "Answer"
    [Faraday's law](concepts/faraday-law.md): $\mathcal{E} = -d\Phi_B/dt$ — a changing
    $\vec B$ creates a circulating $\vec E$ field, which drives charges around the loop.

**Q4.** A capacitor is charged, disconnected, and a dielectric is slid in. What happens
to $Q$, $V$, and the stored energy?

??? success "Answer"
    $Q$ fixed (isolated); $C \to \kappa C$ so $V = Q/C$ *drops* by $\kappa$;
    $U = Q^2/2C$ drops by $\kappa$ too — the missing energy went into pulling the
    dielectric in.

## Computational

**Q5.** Flux through a $0.2\ \text{m}^2$ loop tilted $60°$ from a uniform 0.3 T field?

??? success "Answer"
    $\Phi = BA\cos\theta = 0.3\times0.2\times\cos 60° = 0.03$ Wb.

**Q6.** RC time constant for $R = 5\ \text{k}\Omega$, $C = 2\ \mu\text{F}$ — and how
long to reach 95% charge?

??? success "Answer"
    $\tau = RC = 10$ ms. 95% needs $1 - e^{-t/\tau} = 0.95 \Rightarrow t = 3\tau = 30$ ms.

**Q7.** Two protons are 1 nm apart. Compare the electric repulsion with their
gravitational attraction.

??? success "Answer"
    $F_E = k e^2/r^2 \approx 2.3\times10^{-10}$ N;
    $F_G = G m_p^2/r^2 \approx 1.9\times10^{-46}$ N.
    Ratio $\sim 10^{36}$ — why gravity is irrelevant inside atoms.

## Multiple choice

**Q8.** Unit of electric flux:
(a) N/C  (b) V/m  (c) N·m²/C

??? success "Answer"
    **(c)** — field × area. (Equivalently V·m.)

**Q9.** Inside a long solenoid with $n = 500$ turns/m carrying $i = 2$ A, $B$ equals:
(a) $\mu_0 n i$  (b) $\mu_0 i/(2\pi n)$  (c) $\mu_0 n^2 i$

??? success "Answer"
    **(a)** — from [Ampère's law](concepts/amperes-law.md);
    numerically $B = 4\pi\times10^{-7}\times500\times2 \approx 1.3$ mT.

**Q10.** EMF induced in $N = 50$ turns by $\Phi = 0.1\sin(\pi t)$ Wb:
(a) $-5\pi\cos(\pi t)$ V  (b) $-10\pi\cos(\pi t)$ V  (c) $-50\pi\cos(\pi t)$ V

??? success "Answer"
    **(a)** — $\mathcal{E} = -N\,d\Phi/dt = -50 \times 0.1\pi\cos(\pi t) = -5\pi\cos(\pi t)$ V.
