# Dimensional Analysis

## Intuition

You can learn a shocking amount about a physical system before solving *any*
equation — just by insisting that the units balance. G. I. Taylor famously estimated
the (classified!) yield of the Trinity nuclear test from a published photograph, using
nothing but dimensions. The method: guess which quantities matter, demand the units
match, and the physics has nowhere to hide.

## The principle

Every physical quantity has dimensions built from a small basis — mass $[M]$, length
$[L]$, time $[T]$, temperature $[\Theta]$, current $[I]$. Any valid physical equation
must be **dimensionally homogeneous**: units on the left = units on the right.

**Recipe:**

1. List the parameters that can plausibly matter: $\{A_1, A_2, \dots\}$
2. Reduce to an independent set $\{B_1, B_2, \dots\}$
3. Write down the dimensions of each
4. Posit a power law: $C \propto B_1^{\alpha} B_2^{\beta}\cdots$
5. Match exponents of $[M], [L], [T], \dots$ and solve

## Worked example: the Trinity blast wave

Assume the fireball radius $R$ depends on released energy $E$, time $t$, and ambient
density $\rho$. Posit $E \propto R^\alpha t^\beta \rho^\gamma$:

$$[E] = ML^2T^{-2} = L^\alpha\, T^\beta\, (ML^{-3})^\gamma$$

Matching: $\gamma = 1$ (mass), $\beta = -2$ (time), $\alpha - 3\gamma = 2 \Rightarrow \alpha = 5$:

$$\boxed{\,E \sim \frac{\rho R^5}{t^2}\,}$$

One photo (radius + timestamp) then yields the yield. The full solution is the
[Sedov–Taylor blast wave](../examples/trinity-blast-wave.md), and the same scaling
reappears in supernova remnants.

## Worked example: boiling eggs

Boiling time $t$ vs egg weight $W$. Heat conduction ($\partial_t \theta = k\nabla^2\theta$,
$[k] = L^2 T^{-1}$) sets the clock: $t \sim L^2/k$, and geometric similarity plus equal
density gives $W \propto L^3$. Hence

$$t \propto W^{2/3}$$

A 60 g chicken egg takes 7 min ⇒ a 10 g quail egg takes
$7\times(10/60)^{2/3} \approx 2.1$ min; a 1.6 kg ostrich egg takes
$7\times(1600/60)^{2/3} \approx 62$ min.

## Worked example: animal locomotion

- **Walking (pendulum law):** legs swing like pendulums, $T = 2\pi\sqrt{L/g}$, so
  stepping frequency $f \propto L^{-1/2}$ — bigger animals stroll slower.
- **Running (strength-limited law, A. V. Hill):** muscle stress $\sigma$ is universal;
  force $\propto L^2$, torque $\propto L^3$, moment of inertia $\propto L^5$ ⇒ angular
  acceleration $\propto L^{-2}$ and $f \propto L^{-1}$.

Log–log plots of real animals show both slopes — physics visible in zoology.

## Scale models

Fluids have no intrinsic length scale: the governing equations are scale-invariant
once expressed in dimensionless groups. Match the groups (chiefly the
[Reynolds number](reynolds-number.md)) between a wind-tunnel model and the full-scale
aircraft, and the flows are *dynamically similar* — same physics, cheaper experiment.

## Common mistakes

- **Omitting a relevant parameter** (the method can't warn you) or including a
  redundant one (you get an undetermined exponent — actually a hint that a
  dimensionless group is free).
- **Expecting the dimensionless prefactor.** Dimensional analysis gives $\sim$, never
  the constant (Sedov's full calculation gives the O(1) factor).
- **Treating angles/counts as dimensional** — they're dimensionless; they ride along
  in the unknown function.

## Related concepts

- [Buckingham Pi theorem](buckingham-pi-theorem.md) — the systematic version
- [Reynolds number](reynolds-number.md) — the most famous dimensionless group
- [Energy cascade](energy-cascade.md) — Kolmogorov's scales are dimensional analysis at its finest
- [Blast wave example](../examples/trinity-blast-wave.md)

## Knowledge graph position

**Prerequisites:** none beyond units — accessible anytime.
**Leads to:** [Buckingham Pi](buckingham-pi-theorem.md), [Reynolds number](reynolds-number.md), [Kolmogorov scaling](energy-cascade.md).

## Quiz

**Q1 (computational).** A pendulum's period may depend on $L$, $m$, $g$. Find the
dependence.

??? success "Answer"
    $T \propto L^a m^b g^c$: time needs $c = -1/2$, mass forces $b = 0$, length gives
    $a = 1/2$. $T \propto \sqrt{L/g}$ — mass drops out automatically.

**Q2 (conceptual).** In the egg problem, why does the boiling time scale as $W^{2/3}$
rather than $W$?

??? success "Answer"
    Heat must *diffuse* to the centre: $t \sim L^2/k$, quadratic in size, while
    $W \sim L^3$. So $t \sim W^{2/3}$ — cooking time is set by conduction depth, not by
    total mass.

**Q3 (multiple choice).** Dimensional analysis alone can determine:

- (a) exact numerical answers  (b) functional forms up to dimensionless factors
- (c) which parameters are physically relevant  (d) boundary conditions

??? success "Answer"
    **(b).** Relevance (c) must be *assumed* going in; constants and boundary effects
    need real analysis or experiment.
