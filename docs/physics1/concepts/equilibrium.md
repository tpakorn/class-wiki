# Equilibrium & Elasticity

*Source lecture(s):* [SC133 Lec 15](../lectures.md)

## Intuition

Bridges, cranes, bookshelves, ladders against walls: most of engineering is things
that *don't move*. Statics is [Newton's laws](newtons-laws.md) in the special case
$\vec a = 0$ and $\alpha = 0$ — but with a twist: for extended bodies you must
balance not just forces but **torques**, or your bookshelf rotates off the wall. And
because nothing is perfectly rigid, "not moving" really means "deforming slightly
and pushing back" — **elasticity**.

## The two conditions of static equilibrium

$$\boxed{\;\sum \vec F = 0 \qquad\text{and}\qquad \sum \vec\tau = 0\;\text{(about any axis)}\;}$$

The freedom to choose the torque axis is the problem-solver's best weapon: **put the
axis where the most annoying unknown force acts**, and that force vanishes from the
torque equation.

## Worked example: the leaning ladder

A uniform ladder (mass $m$, length $L$) leans at angle $\theta$ against a
frictionless wall; floor friction coefficient $\mu_s$. When does it slip?

Forces: weight $mg$ at the center, wall normal $N_w$ (horizontal), floor normal $N_f$
and friction $f$.

- $\sum F_y = 0$: $N_f = mg$
- $\sum F_x = 0$: $f = N_w$
- Torque about the **floor contact** (killing $N_f$ and $f$):
  $N_w L\sin\theta = mg\frac{L}{2}\cos\theta \Rightarrow N_w = \frac{mg}{2\tan\theta}$

Slipping when $f > \mu_s N_f$:

$$\tan\theta_\text{min} = \frac{1}{2\mu_s}$$

Steeper is safer; a slick floor ($\mu_s \to 0$) makes *every* angle unsafe — exactly
as intuition (and ladder-safety posters) insist.

## Elasticity: stress and strain

Real "rigid" bodies are stiff springs. Define

$$\text{stress} = \frac{F}{A}\ \text{(Pa)} \qquad
\text{strain} = \frac{\Delta L}{L}\ \text{(dimensionless)}$$

For modest loads they are proportional — [Hooke's law](../equations/hookes-law.md)
in grown-up units:

$$\frac{F}{A} = E\,\frac{\Delta L}{L}$$

with **Young's modulus** $E$ a material property (steel $\approx 200$ GPa, bone
$\approx 15$ GPa, rubber $\approx 0.01$ GPa). Analogous moduli handle shear (shear
modulus $G$) and squeezing (bulk modulus $B$). Push past the **elastic limit** and
deformation becomes permanent; past **ultimate strength**, it becomes news.

## Worked example: stretching a cable

A 2 m steel cable, cross-section $1\,\text{cm}^2$, hangs a 500 kg load. Stretch?

$$\Delta L = \frac{FL}{AE} = \frac{4900 \times 2}{10^{-4}\times 2\times10^{11}}
\approx 0.5\,\text{mm}$$

Stiff — but not zero. Skyscrapers, bridges and bones all live on this small-but-finite
give; the [stress–strain language](../../fluids/concepts/what-is-a-fluid.md)
also marks the exact boundary between solids (sustain shear) and fluids (don't).

## Stability of equilibrium

Balanced is not the same as *stable*: displace slightly and ask what gravity does.
Center of mass above the support polygon = balanced; CM falling when tipped = stable.
Lower CM and wider base ⇒ harder to topple — why racing cars are low and wide, and
why you widen your stance on a bus. (The energy view — valleys vs hilltops of
$U$ — is on the [potential energy page](potential-energy.md), and the full dynamical
treatment awaits in [hydrodynamic stability](../../fluids/concepts/hydrodynamic-stability.md).)

## Common mistakes

- **Balancing forces but not torques.** Both conditions are mandatory; a couple
  (equal, opposite, offset forces) has zero net force yet spins the body.
- **Choosing a torque axis and then forgetting forces at that axis still exist** —
  they're absent from the *torque* equation only.
- **Confusing stress with force and strain with stretch** — both are normalized, so
  material properties don't depend on specimen size.
- **Treating the elastic limit as failure.** Permanent bending comes first; fracture
  later — different design margins.

## Related concepts

- [Torque](torque.md) — the second condition
- [Newton's laws](newtons-laws.md) — the first condition
- [Potential energy](potential-energy.md) — stability as energy landscape
- [Fluid statics (PC316)](../../fluids/concepts/hydrostatic-equilibrium.md) — equilibrium of things that *can't* hold shear

## Knowledge graph position

**Prerequisites:** [Newton's laws](newtons-laws.md), [Torque](torque.md).
**Leads to:** [Fluids](fluids.md) (the no-shear limit), structural mechanics beyond this course.

## Quiz

**Q1 (computational).** A 60 kg person stands 1.5 m from the left end of a uniform
4 m, 20 kg plank supported at both ends. Force on each support?

??? success "Answer"
    Torque about the left support:
    $N_R(4) = 20g(2) + 60g(1.5) \Rightarrow N_R = \frac{40g + 90g}{4} = 32.5g \approx 319\,\text{N}$.
    Then $N_L = 80g - N_R = 47.5g \approx 466\,\text{N}$ — the nearer support carries
    more, as it must.

**Q2 (conceptual).** Why does a crane need a massive counterweight?

??? success "Answer"
    The load creates a huge torque about the tower; the counterweight supplies an
    opposing torque so the *net* torque at the base stays small. Force balance alone
    would be satisfied by the tower pushing up — it's the torque condition that
    demands the counterweight.

**Q3 (multiple choice).** Two wires of the same material and length; wire B has twice
the diameter. Under the same load, B stretches:
(a) half as much (b) a quarter as much (c) the same

??? success "Answer"
    **(b).** $\Delta L \propto 1/A \propto 1/d^2$ — doubling diameter quadruples the
    area.
