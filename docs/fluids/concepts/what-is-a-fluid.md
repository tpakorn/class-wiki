# What Is a Fluid?

## Intuition

Push sideways on a brick and it pushes back; it deforms a little and stops. Push
sideways on water — even infinitesimally gently — and it *never stops deforming*. That
is the whole distinction. A **fluid** is a substance that continuously deforms under
any shear stress, no matter how small. Liquids, gases, plasmas: all fluids. Jelly,
rubber, and (on short timescales) even cats behave elastically instead — they hold a
shear and spring back.

## Why it matters

Everything in this course — [pressure](pressure.md), [Bernoulli](bernoulli-principle.md),
[Navier–Stokes](../equations/navier-stokes-equation.md) — rests on two assumptions made
here: (1) the material cannot support static shear, and (2) it can be treated as a
*continuum*, so that fields like $\rho(\mathbf{r})$ and $\mathbf{v}(\mathbf{r})$ are
smooth functions of position.

## Formal definition

**Fluid.** A substance that deforms continuously under an applied shear stress, however
small. At rest, a fluid can sustain only *normal* stresses (pressure), never shear.

**Continuum hypothesis.** A material may be treated as continuous when its properties
$f(\mathbf{r})$ (density, velocity, pressure…) vary smoothly with position:

$$\forall \epsilon > 0,\ \exists \delta > 0:\ \|\delta\mathbf{r}\| < \delta \implies |f(\mathbf{r}+\delta\mathbf{r}) - f(\mathbf{r})| < \epsilon.$$

Practically, the continuum picture holds when the system's characteristic length $L$
vastly exceeds the molecular mean free path $\lambda$:

$$L \gg \lambda.$$

## Physical interpretation

- In a **solid**, molecules sit in a fixed lattice; shear strain is stored elastically
  and released when the force is removed.
- In a **liquid**, molecules stay close but slide freely — shear cannot be stored.
- In a **gas**, molecules are far apart and fill any container.
- In a **plasma**, the gas is ionized; free electrons and ions move independently, but
  the continuum description still applies when $L \gg \lambda$.

The ratio $\lambda/L$ (the *Knudsen number*) tells you when the continuum picture
breaks: rarefied upper-atmosphere flow and micro-channel gas flow are classic failures.

## Common mistakes

- **"Fluid = liquid."** Gases and plasmas are fluids too. The category is about shear
  response, not density.
- **Confusing slow creep with fluidity.** Some materials (glaciers, silly putty, cats)
  act solid on short timescales and fluid on long ones; this course sticks to clear-cut
  fluids.
- **Applying continuum results at molecular scales.** A "fluid particle" is *large*
  compared to $\lambda$ but *small* compared to $L$.

## Related concepts

- [Pressure](pressure.md) — the only stress a static fluid can exert
- [Viscosity](viscosity.md) — how a moving fluid resists *rate* of shear
- [Shock waves](shock-waves.md) — where gradients get so steep the continuum almost breaks ($\ell_s \sim \lambda$)

## Knowledge graph position

**Prerequisites:** none — this is the root of the course.
**Leads to:** [Pressure](pressure.md), [Eulerian vs Lagrangian descriptions](eulerian-vs-lagrangian.md), [Viscosity](viscosity.md).

## Quiz

**Q1 (conceptual).** A rubber block between two plates is sheared and holds its
deformed shape while the force is applied. Is rubber a fluid?

??? success "Answer"
    No. It sustains a static shear stress (finite deformation ∝ force, recovered on
    release). A fluid would deform *without bound* under the same load.

**Q2 (conceptual).** Why can't we use fluid mechanics to describe air flow in a channel
just 10 molecular mean-free-paths wide?

??? success "Answer"
    The continuum hypothesis needs $L \gg \lambda$. With $L \sim 10\lambda$, individual
    molecular collisions matter, fields like $\rho(\mathbf{r})$ are no longer smooth, and
    kinetic theory (not continuum mechanics) is required.

**Q3 (multiple choice).** Which statement is true of a fluid *at rest*?

- (a) It supports small shear stresses only.
- (b) It supports normal stresses only.
- (c) It supports no stresses at all.
- (d) It supports shear only along boundaries.

??? success "Answer"
    **(b).** A static fluid exerts and sustains only normal stress — that is precisely
    [pressure](pressure.md).
