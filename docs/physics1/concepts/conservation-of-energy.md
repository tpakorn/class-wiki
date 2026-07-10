# Conservation of Energy

*Source lecture(s):* [SC133 Lec 9](../lectures.md)

## Intuition

Energy is the universe's strictest accountant. It changes form constantly — motion to
height, height to spring compression, everything eventually to heat — but the total
never budges. In mechanics this gives a superpower: compare any two moments of a
process without solving for anything in between. Roller coaster, pendulum, planet —
if you know the energy budget, you know the speeds.

## The statement

For a system where only **conservative forces** do work:

$$\boxed{\,E = K + U = \text{constant}\,}
\qquad
\tfrac12 mv_i^2 + U_i = \tfrac12 mv_f^2 + U_f$$

With non-conservative forces (friction, drag) the mechanical energy leaks into
thermal energy, but the *total* still balances:

$$K_i + U_i = K_f + U_f + E_\text{thermal}, \qquad E_\text{thermal} = f_k\, d$$

Energy conservation isn't broken by friction — mechanical energy just stops being the
whole story.

## Where it comes from

Mechanical energy conservation is the
[work–energy theorem](../equations/work-energy-theorem.md) plus the definition of
[potential energy](potential-energy.md): $W_\text{cons} = -\Delta U$ and
$W_\text{net} = \Delta K$ combine into $\Delta(K + U) = W_\text{non-cons}$. Deeper
still (Noether's theorem, for later courses): energy conservation is the consequence
of physics being the same today as tomorrow — time-translation symmetry.

## Worked example: roller coaster loop

A cart starts from rest at height $h$ and must maintain contact at the top of a loop
of radius $R$. Minimum $h$?

At the loop top, gravity alone must supply the
[centripetal force](circular-motion.md): $mg = mv^2/R \Rightarrow v^2 = gR$.
Energy from start to loop top (height $2R$):

$$mgh = \tfrac12 mv^2 + mg(2R) = \tfrac12 mgR + 2mgR
\;\Rightarrow\; \boxed{h = \tfrac52 R}$$

No forces along the track ever entered the calculation — that's the power of the
method.

## Worked example: friction included

A 2 kg block slides from rest down a ramp of height 1.5 m, arriving at the bottom at
4 m/s. How much energy went to heat?

$E_\text{thermal} = mgh - \tfrac12 mv^2 = 2(9.8)(1.5) - \tfrac12(2)(16)
= 29.4 - 16 = 13.4\,\text{J}$ — the books always balance.

## When to use energy vs Newton

| Question asks about... | Best tool |
|---|---|
| speed at a position | **energy** (path-independent) |
| time, or force at an instant | Newton / [kinematics](kinematics.md) |
| direction of motion at a point | Newton (energy is a scalar — it forgot direction) |
| systems with friction over known distance | energy with $f_k d$ term |

## Common mistakes

- **Using $E$ conservation across friction without the heat term.** Check for
  non-conservative forces *before* writing $K_i + U_i = K_f + U_f$.
- **Expecting energy methods to give direction or time.** Energy is a scalar; it
  yields speeds, not velocity vectors or durations.
- **Double counting**: if you include a force via potential energy, don't also add
  its work.
- **Mixing zero-points mid-problem.** Choose where $U = 0$ once.

## Related concepts

- [Potential energy](potential-energy.md) & [work–KE theorem](kinetic-energy-and-work.md) — the ingredients
- [Collisions](collision-and-impulse.md) — where kinetic energy may vanish but [momentum](linear-momentum.md) survives
- [First law of thermodynamics](first-law-of-thermodynamics.md) — energy conservation with heat promoted to a first-class citizen
- [Bernoulli's equation (fluids)](bernoulli.md) — energy conservation per unit volume of fluid

## Knowledge graph position

**Prerequisites:** [Work & kinetic energy](kinetic-energy-and-work.md), [Potential energy](potential-energy.md).
**Leads to:** [Collisions](collision-and-impulse.md), [SHM](simple-harmonic-motion.md), [thermodynamics](first-law-of-thermodynamics.md), [Bernoulli](bernoulli.md).

## Quiz

**Q1 (computational).** A pendulum is released from rest with the string horizontal
(length $L$). Speed at the bottom?

??? success "Answer"
    Drop height $= L$: $v = \sqrt{2gL}$. The string tension does no work
    (⊥ motion), so pure energy conservation applies.

**Q2 (conceptual).** A ball bounces, each bounce reaching 80% of the previous height.
Where does the energy go?

??? success "Answer"
    Into thermal energy and sound during each inelastic contact (deforming the ball
    and floor). Mechanical energy shrinks by 20% per bounce; total energy is
    conserved throughout.

**Q3 (multiple choice).** Two ramps, one steep and one gentle, connect the same two
heights (frictionless). A block slides down each. At the bottom:
(a) steep ramp gives higher speed (b) equal speeds, different times (c) equal speeds
and equal times

??? success "Answer"
    **(b).** Same $\Delta U$ ⇒ same speed. The steep ramp is *quicker*, though —
    time is Newton's department, not energy's.

**Q4 (conceptual).** Why does the loop-the-loop answer $h = \frac52 R$ not depend on
the cart's mass?

??? success "Answer"
    Every term in the budget ($mgh$, $\frac12 mv^2$, $mgR$) is proportional to $m$ —
    gravity accelerates all masses alike, so $m$ cancels. The same cancellation
    behind Galileo's tower experiment.
