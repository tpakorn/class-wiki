# Quizzes · Mathematical Methods I

Integrative questions — each concept page has its own quiz too. Study in
[lecture order](lectures.md).

## Conceptual

**Q1.** Why does the curl of any gradient field vanish identically?

??? success "Answer"
    $(\nabla\times\nabla\phi)_i = \epsilon_{ijk}\partial_j\partial_k\phi$: mixed
    partials are symmetric in $j,k$ while $\epsilon_{ijk}$ is antisymmetric — the
    contraction is zero.

**Q2.** What property of an operator guarantees real eigenvalues, and why does physics
insist on it?

??? success "Answer"
    Hermiticity ($A = A^\dagger$). Measured quantities are real numbers, and the
    eigenvalues of an observable *are* its possible measurement outcomes — see
    [Hermitian matrices](concepts/hermitian-matrices.md).

**Q3.** When does separation of variables fail for a PDE?

??? success "Answer"
    When the equation (or boundary) couples the variables inseparably — e.g.
    coefficients depending on both variables jointly, or boundaries not aligned with a
    coordinate system in which the PDE separates.

**Q4.** Why do Fourier methods turn ODEs into algebra?

??? success "Answer"
    $e^{ikx}$ are eigenfunctions of $d/dx$: differentiation acts as multiplication by
    $ik$. In the transform domain a linear ODE with constant coefficients becomes a
    polynomial equation — see [Fourier transform](concepts/fourier-transform.md).

## Computational

**Q5.** Eigenvalues of $\begin{pmatrix}4&2\\1&3\end{pmatrix}$?

??? success "Answer"
    $\lambda^2 - 7\lambda + 10 = 0 \Rightarrow \lambda = 5, 2$
    (trace $= 7$ ✓, det $= 10$ ✓).

**Q6.** Fourier sine coefficient $b_3$ for $f(x) = x$ on $[-\pi, \pi]$?

??? success "Answer"
    $b_n = \frac{1}{\pi}\int_{-\pi}^{\pi} x\sin nx\,dx = \frac{2(-1)^{n+1}}{n}$, so
    $b_3 = \frac{2}{3}$.

**Q7.** Solve $y'' + y = \delta(x - \xi)$ on $[0, \pi]$ with $y(0) = y(\pi) = 0$ —
what jump condition does the Green's function satisfy at $x = \xi$?

??? success "Answer"
    $G$ continuous at $\xi$; $G'$ jumps by $+1$:
    $G'(\xi^+) - G'(\xi^-) = 1$ (integrate the equation across the delta). See
    [Green's functions](concepts/greens-functions.md).

## Multiple choice

**Q8.** The theorem converting $\oint_S \vec A\cdot d\vec S$ into
$\int_V \nabla\cdot\vec A\,dV$:
(a) Stokes  (b) Divergence  (c) Fundamental theorem of calculus

??? success "Answer"
    **(b)** — [divergence theorem](concepts/divergence-theorem.md). Stokes converts a
    *line* integral to a surface integral of the curl.

**Q9.** If $A$ is $3\times3$ with $\det A = -4$, then $\det A^{-1}$ is:
(a) $-4$  (b) $-1/4$  (c) $4$

??? success "Answer"
    **(b)** — $\det(A^{-1}) = 1/\det A$.

**Q10.** The Laplace transform of $\sin(\omega t)$:
(a) $\dfrac{\omega}{s^2+\omega^2}$  (b) $\dfrac{s}{s^2+\omega^2}$  (c) $\dfrac{1}{s^2+\omega^2}$

??? success "Answer"
    **(a)** — and (b) is $\cos(\omega t)$; remember by checking $t \to 0$ behavior.
