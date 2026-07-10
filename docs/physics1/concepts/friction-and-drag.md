# Friction & Drag

*Source lecture(s):* [SC133 Lec 7](../lectures.md)

## Intuition

Real surfaces grip and real fluids resist. **Friction** is the sideways force between
touching surfaces — microscopic welds forming and breaking. **Drag** is the fluid's
resistance to a body pushing through it. Both oppose *relative* sliding, both convert
orderly kinetic energy into heat, and both are why perpetual motion looks so
plausible on ice and so absurd in honey.

## Friction: static vs kinetic

**Static friction** holds surfaces still. It is *adjustable*: it matches whatever
force tries to slide the object, up to a ceiling —

$$f_s \leq \mu_s N$$

**Kinetic friction** acts once sliding begins, roughly constant:

$$f_k = \mu_k N$$

with $\mu_k < \mu_s$ (breaking free is harder than keeping going — the reason wheels
lock and ABS exists). Both are proportional to the **normal force** $N$, *not* to
weight and *not* to contact area.

## Worked example: block on an incline

A block rests on a slope of angle $\theta$. When does it slip?

Along the incline: gravity component $mg\sin\theta$ vs static friction
$\leq \mu_s N = \mu_s mg\cos\theta$. Slipping starts when

$$\tan\theta_c = \mu_s$$

— measuring the critical angle *is* measuring $\mu_s$. For $\mu_s = 0.6$:
$\theta_c \approx 31°$.

## Drag and terminal velocity

At everyday speeds in air, drag grows with the *square* of speed:

$$D = \tfrac12 C \rho A v^2$$

($\rho$ air density, $A$ cross-section, $C\sim0.5$–1 drag coefficient). A falling body
accelerates until drag balances weight — **terminal velocity**:

$$v_t = \sqrt{\frac{2mg}{C\rho A}}$$

Skydiver spread-eagle: $\sim 60\,\text{m/s}$; head-down: $\sim 90\,\text{m/s}$;
raindrop: $\sim 7\,\text{m/s}$ (a mercy — pea-sized hail at free-fall-from-cloud
speed would be lethal). Because $v_t \propto \sqrt{m/A}$, small creatures fall
slowly: an ant reaches harmless terminal velocity almost instantly.

## Physical interpretation

Friction converts kinetic energy to thermal energy at rate $f_k v$ — the
[energy bookkeeping](conservation-of-energy.md) still balances, but mechanical energy
alone does not. Drag at high speeds is the first taste of
[fluid mechanics](../../fluids/index.md); the quadratic law comes from the momentum
the body must give the fluid it shoves aside, and the dimensionless story behind $C$
is the [Reynolds number](../../fluids/concepts/reynolds-number.md).

## Common mistakes

- **Using $f_s = \mu_s N$ always.** That's the *maximum*; static friction is usually
  smaller — exactly what's needed to prevent sliding, no more.
- **Friction always opposes motion?** It opposes *relative slipping*. Friction is what
  pushes a car forward (tires grip road) and what makes walking possible.
- **$N = mg$ reflexively** — false on inclines and whenever other vertical forces act.
- **Using constant-acceleration kinematics with drag.** Drag depends on $v$, so $a$
  changes continuously; you need calculus or numerics ([PHY653 knows how](../../comp-plasma/concepts/ode-integration.md)).

## Related concepts

- [Newton's laws](newtons-laws.md) — friction lives on free-body diagrams
- [Kinetic energy & work](kinetic-energy-and-work.md) — friction's negative work
- [Reynolds number (PC316)](../../fluids/concepts/reynolds-number.md) — when drag is linear vs quadratic
- [Terminal-velocity physics in the projectile playground](../simulations/projectile-playground.md)

## Knowledge graph position

**Prerequisites:** [Newton's laws](newtons-laws.md).
**Leads to:** [Work & energy](kinetic-energy-and-work.md) (dissipation), [fluid mechanics (PC316)](../../fluids/index.md).

## Quiz

**Q1 (computational).** A 10 kg crate needs 49 N to start moving and 39 N to keep
moving at constant velocity. Find $\mu_s$ and $\mu_k$.

??? success "Answer"
    $N = mg = 98\,\text{N}$. $\mu_s = 49/98 = 0.5$; $\mu_k = 39/98 = 0.4$ (constant
    velocity ⇒ applied force balances kinetic friction).

**Q2 (conceptual).** Why do heavy and light skydivers *not* fall together, when
Galileo says free fall is universal?

??? success "Answer"
    With drag, terminal velocity $v_t = \sqrt{2mg/C\rho A}$ depends on $m/A$. Free
    fall is universal only in vacuum; drag breaks the equivalence by caring about
    size and mass separately.

**Q3 (multiple choice).** A car brakes hardest without skidding when its wheels:
(a) lock completely (b) keep rolling at the verge of slipping (c) spin freely

??? success "Answer"
    **(b).** Rolling contact uses *static* friction ($\mu_s > \mu_k$); a locked wheel
    slides on smaller kinetic friction. Hence anti-lock brakes.
