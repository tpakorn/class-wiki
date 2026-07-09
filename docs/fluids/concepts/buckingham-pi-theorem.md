# Buckingham Pi Theorem

## Intuition

[Dimensional analysis](dimensional-analysis.md) by guess-a-power-law works, but how do
you know how many independent dimensionless combinations exist, and whether you found
them all? Buckingham's theorem answers with linear algebra: count variables, subtract
the number of independent dimensions, and that's exactly how many dimensionless
$\pi$-groups describe the problem.

## Theorem

If a physical relationship involves $n$ variables built from $k$ independent
fundamental dimensions, then it can be rewritten as a relationship among

$$\boxed{\,n - k\ \text{dimensionless groups}\,}$$

$$f(q_1, \dots, q_n) = 0 \quad\Longleftrightarrow\quad F(\pi_1, \dots, \pi_{n-k}) = 0$$

where each $\pi_i = q_1^{a_1} q_2^{a_2}\cdots q_n^{a_n}$ is dimensionless. The
exponent vectors span the **null space of the dimensional matrix** — hence the count.

## Procedure

1. **List variables** (this is the physics step — everything after is mechanical)
2. **Write dimensions** of each in $[M], [L], [T], \dots$
3. **Build the dimensional matrix** (rows = dimensions, columns = variables)
4. **Find the null space** — each basis vector is one $\pi$-group
5. **Interpret** the groups (they usually have names!)

Practical shortcut: pick $k$ "repeating variables" that span the dimensions (commonly a
length, a velocity, a density), then combine each remaining variable with them.

## Worked example: wind turbine force

Force $F$ on a turbine tower given wind speed $v$, air density $\rho$, viscosity
$\mu$, rotor diameter $d$, spin rate $N$. Here $n = 6$, $k = 3$ ⇒ **3 groups**.
Choosing $d, v, \rho$ as repeaters:

$$0 = \phi\left(\underbrace{\frac{F}{\rho v^2 d^2}}_{\pi_1:\ \text{force coefficient}},\;
\underbrace{\frac{\rho v d}{\mu}}_{\pi_2:\ \text{Reynolds number}},\;
\underbrace{\frac{dN}{v}}_{\pi_3:\ \text{tip-speed ratio}}\right)$$

Six dimensional variables collapse to a surface in 3-D dimensionless space — this is
why one wind-tunnel campaign can characterize every geometrically similar turbine.

## Worked example: pipe flow rate

$Q = \phi(D, L, \Delta P, \mu)$: $n = 5$, $k = 3$ ⇒ 2 groups:

$$\pi_1 = \frac{Q\mu}{\Delta P D^3} \quad (\text{flow characteristic}), \qquad
\pi_2 = \frac{D}{L} \quad (\text{aspect ratio})$$

Adding the physical insight that $Q$ depends on the *gradient* $\Delta P/L$ forces the
combination $\pi_1 \propto \pi_2$, i.e.

$$Q \sim \frac{\Delta P\, D^4}{\mu L}$$

— the [Hagen–Poiseuille law](../examples/hagen-poiseuille-flow.md) up to the exact
prefactor $\pi/128$ (for diameter) that only the full solution supplies.

## Common mistakes

- **Miscounting $k$.** It is the number of *independent* dimensions actually present —
  check the rank of the dimensional matrix, not just "3".
- **Choosing repeating variables that cannot span the dimensions** (e.g. two lengths) —
  the algebra will fail.
- **Treating the $\pi$-groups as unique.** Any product of powers of groups is another
  valid set; pick the conventional, physically named ones.

## Related concepts

- [Dimensional analysis](dimensional-analysis.md) — the informal parent
- [Reynolds number](reynolds-number.md) — $\pi_2$ in nearly every fluids problem
- [Hagen–Poiseuille flow](../examples/hagen-poiseuille-flow.md) — exact counterpart

## Knowledge graph position

**Prerequisites:** [Dimensional analysis](dimensional-analysis.md), linear algebra (null space).
**Leads to:** [Reynolds number](reynolds-number.md), dynamic similarity, turbomachinery scaling.

## Quiz

**Q1 (computational).** Drag $F$ on a sphere depends on $\rho, v, D, \mu$. How many
$\pi$-groups, and what are they?

??? success "Answer"
    $n = 5$, $k = 3$ ⇒ 2 groups: drag coefficient $C_D = \frac{F}{\rho v^2 D^2}$
    and Reynolds number $Re = \frac{\rho v D}{\mu}$. Hence $C_D = f(Re)$ — the entire
    sphere-drag literature is one curve.

**Q2 (conceptual).** For the simple pendulum with $T, L, m, g$ ($n=4$, $k=3$) the
theorem promises one group. What does the single group tell you?

??? success "Answer"
    $\pi = T^2 g/L$ = const ⇒ $T \propto \sqrt{L/g}$, and since no dimensionless
    combination can include $m$ alone, the period **cannot depend on mass**.

**Q3 (multiple choice).** Two flows are dynamically similar when:

- (a) they have the same fluid  (b) all their $\pi$-groups match
- (c) their velocities match  (d) their forces match

??? success "Answer"
    **(b).** Geometric similarity plus equality of every relevant dimensionless group
    (in practice often just $Re$, plus Mach/Froude/Weber as relevant).
