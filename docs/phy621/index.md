# PHY621 · Mathematical Methods in Physics I

**A knowledge wiki for PHY621** — Thammasat University graduate course, semester 1.
The working mathematics of a physicist: linear algebra, transforms, and the
differential equations they conquer.

## The course in one paragraph

Physics problems keep asking the same mathematical questions. *What are the natural
modes?* — [eigenvalues and eigenvectors](concepts/eigenvalues-eigenvectors.md), with
[Hermitian operators](concepts/hermitian-matrices.md) guaranteeing real, measurable
answers. *How do I unravel derivatives?* —
[Fourier](concepts/fourier-transform.md) and
[Laplace transforms](concepts/laplace-transform.md), which turn calculus into algebra
(and multiplication into [convolution](concepts/convolution.md)). *How do I solve the
equations of physics?* — [ODEs](concepts/ordinary-differential-equations.md) with
their [special functions](concepts/special-functions.md),
[PDEs](concepts/partial-differential-equations.md) by separation, and the master key:
[Green's functions](concepts/greens-functions.md), which build any response from the
response to a single kick.

## Start here

- **[Lecture timeline](lectures.md)** — teaching order, review Lec 0 → Green's functions
- **[Concept graph](concept-graph.md)** — the dependency map
- **[Fourier series builder](simulations/fourier-builder.md)** — watch harmonics assemble a square wave
- **[Quizzes](quizzes.md)** · **[Glossary](glossary.md)**

!!! tip "Where this mathematics gets used"
    The eigenmode language powers quantum mechanics; transforms power every signal and
    wave problem; Green's functions reappear in electrodynamics and field theory. In
    this wiki family: [FDTD and Poisson solvers](../comp-plasma/index.md) are these
    methods gone numerical, and [PHY622](../phy622/index.md) continues with
    variations, complex analysis and groups.
