# Quizzes · Mathematical Methods II

Integrative questions — each concept page has its own quiz too. Study in
[lecture order](lectures.md).

## Conceptual

**Q1.** Hamilton's principle says the action is *stationary*, not minimal. What's the
difference, and does it matter?

??? success "Answer"
    Stationary means $\delta S = 0$ — minimum, maximum, *or saddle*. Real trajectories
    are often saddle points (e.g. long harmonic-oscillator paths past a conjugate
    point). The equations of motion only need $\delta S = 0$.

**Q2.** What is the geometric meaning of the Cauchy–Riemann equations?

??? success "Answer"
    They force the local map $z \mapsto f(z)$ to be a pure rotation + scaling
    (multiplication by $f'(z)$) — angle-preserving wherever $f' \neq 0$. Analyticity
    *is* local conformality.

**Q3.** Why does SU(2) cover SO(3) *twice*?

??? success "Answer"
    Both $U$ and $-U$ produce the same rotation ($R(U) = R(-U)$): the map
    SU(2) → SO(3) is 2-to-1. Physical consequence: spinors pick up a sign under a
    $360°$ rotation and need $720°$ to return — see [SU(2) ↔ SO(3)](concepts/su2-so3.md).

**Q4.** A soap film and a light ray both "solve variational problems." What functional
does each extremize?

??? success "Answer"
    The film minimizes *area* ([minimal surface](concepts/minimal-surfaces.md),
    $H = 0$); the ray extremizes *optical path length* $\int n\,ds$ (Fermat) — both
    are Euler–Lagrange in different costumes.

## Computational

**Q5.** Find the Euler–Lagrange equation for $F = y'^2 + V(y)$.

??? success "Answer"
    $\frac{\partial F}{\partial y} - \frac{d}{dx}\frac{\partial F}{\partial y'}
    = V'(y) - 2y'' = 0 \Rightarrow 2y'' = V'(y)$.

**Q6.** Residue of $f(z) = \dfrac{1}{z^2+1}$ at $z = i$?

??? success "Answer"
    Simple pole: $\lim_{z\to i}(z - i)f(z) = \dfrac{1}{2i} = -\dfrac{i}{2}$.
    (Bonus: closing $\int_{-\infty}^{\infty}\frac{dx}{1+x^2}$ upstairs gives
    $2\pi i \times(-i/2) = \pi$ ✓.)

**Q7.** Evaluate $\displaystyle\int_0^{2\pi} \frac{d\theta}{2 + \cos\theta}$ by
residues.

??? success "Answer"
    Set $z = e^{i\theta}$: integral becomes
    $\oint \frac{2\,dz}{i(z^2 + 4z + 1)}$ on $|z|=1$. Poles at $z = -2 \pm \sqrt3$;
    only $-2 + \sqrt3$ lies inside. Residue $\frac{2}{i}\cdot\frac{1}{2\sqrt3}$ ⇒
    integral $= 2\pi i \cdot \frac{1}{i\sqrt3} = \frac{2\pi}{\sqrt3}$.

## Multiple choice

**Q8.** The Euler–Lagrange equation for $F = y'^2$:
(a) $y'' = 0$  (b) $y = 0$  (c) $y' = 0$

??? success "Answer"
    **(a)** — extremals are straight lines.

**Q9.** The residue of $\dfrac{1}{(z-2)^2}$ at $z = 2$:
(a) 1  (b) 0  (c) undefined

??? success "Answer"
    **(b)** — a double pole with no $1/(z-2)$ term in its Laurent series; the residue
    (coefficient of the simple-pole term) is zero, so $\oint = 0$ around it.

**Q10.** Which group is non-Abelian?
(a) $C_4$  (b) $S_3$  (c) $\mathbb{Z}_5$

??? success "Answer"
    **(b)** — permutations of 3 objects don't commute (swap-then-cycle ≠
    cycle-then-swap); it's the smallest non-Abelian group (order 6).
