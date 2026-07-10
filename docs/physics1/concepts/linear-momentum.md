# Linear Momentum

*Source lecture(s):* [SC133 Lec 10](../lectures.md)

## Intuition

Which is harder to stop: a bicycle at 30 km/h or a truck at 30 km/h? Same velocity,
very different "quantity of motion." Momentum $\vec p = m\vec v$ is that quantity —
mass times velocity, the measure of how much *oomph* a moving body carries and how
much force-time it takes to change it. Newton wrote his second law in terms of it,
and unlike velocity or kinetic energy, total momentum survives even the most violent
collisions.

## Definition and Newton's second law, properly

$$\vec p = m\vec v \qquad\qquad \boxed{\;\sum\vec F = \frac{d\vec p}{dt}\;}$$

For constant mass this reduces to $\sum\vec F = m\vec a$; the momentum form is more
general (rockets shed mass; relativity redefines $p$ but keeps this law).

## Conservation of momentum

For a system with **zero net external force**:

$$\vec P_\text{total} = \sum_i m_i \vec v_i = \text{constant}$$

The proof is [Newton's third law](newtons-laws.md): internal forces come in canceling
pairs, so they can redistribute momentum among parts but never change the total.
This is the workhorse of [collision analysis](collision-and-impulse.md) — during the
brief violence of impact, external forces (gravity, friction) are negligible next to
the enormous internal ones, so momentum passes through the collision *unchanged* even
when kinetic energy does not.

Deeper view (for later courses): momentum conservation follows from the homogeneity
of space — physics doesn't care *where* the experiment happens.

## Momentum vs kinetic energy

| | Momentum $\vec p$ | Kinetic energy $K$ |
|---|---|---|
| Type | vector | scalar |
| Formula | $mv$ | $\tfrac12 mv^2 = p^2/2m$ |
| In collisions | always conserved (isolated) | conserved only if elastic |
| Can cancel between bodies? | yes (opposite directions) | never (always ≥ 0) |

Two identical cars in a head-on crash: total momentum zero *before and after*; total
kinetic energy large before, mangled metal after.

## Worked example: recoil

A 4 kg rifle fires a 10 g bullet at 500 m/s. Recoil speed?

$$0 = m_b v_b + m_r v_r \Rightarrow v_r = -\frac{0.01 \times 500}{4} = -1.25\,\text{m/s}$$

Momenta are equal and opposite; kinetic energies are *not* — the bullet carries
$K_b/K_r = m_r/m_b = 400$ times more. (Same split powers rockets and explains why
[the lighter fragment always gets the energy](collision-and-impulse.md).)

## Common mistakes

- **Conserving momentum with external forces present.** A ball bouncing off the floor
  does *not* conserve its momentum — Earth intervenes. Choose the system so external
  forces vanish (or act negligibly during the event).
- **Treating momentum as a scalar.** Head-on momenta subtract; perpendicular momenta
  combine as [vectors](vectors.md), component by component.
- **Assuming KE conservation because momentum is conserved.** Independent claims —
  see [collisions](collision-and-impulse.md).

## Related concepts

- [Center of mass](center-of-mass.md) — $\vec P = M\vec v_\text{cm}$
- [Collisions & impulse](collision-and-impulse.md) — the applications
- [Kinetic energy](kinetic-energy-and-work.md) — the contrasting scalar
- [Momentum of fluids (PC316)](../../fluids/concepts/reynolds-transport-theorem.md) — the same conservation, control-volume style

## Knowledge graph position

**Prerequisites:** [Newton's laws](newtons-laws.md).
**Leads to:** [Collisions & impulse](collision-and-impulse.md), [rocket propulsion], [angular momentum](rolling-torque-angular-momentum.md) (the rotational analogue).

## Quiz

**Q1 (computational).** A 0.15 kg ball at 40 m/s is caught and stopped. Magnitude of
the momentum change?

??? success "Answer"
    $|\Delta p| = 0.15 \times 40 = 6\,\text{kg·m/s}$ — delivered to the catcher's
    hand over the stopping time (see [impulse](collision-and-impulse.md)).

**Q2 (conceptual).** Can a system have zero total momentum but large kinetic energy?

??? success "Answer"
    Yes — two equal masses moving oppositely, a spinning object, a hot gas. Momenta
    cancel as vectors; kinetic energies add as positive scalars.

**Q3 (multiple choice).** A heavy truck and light car have equal kinetic energy.
Which has more momentum? (a) truck (b) car (c) equal

??? success "Answer"
    **(a).** $p = \sqrt{2mK}$: at fixed $K$, momentum grows with mass — the mirror
    image of the equal-momentum quiz on the [work–energy page](kinetic-energy-and-work.md).
