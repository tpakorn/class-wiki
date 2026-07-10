# The First Law of Thermodynamics

*Source lecture(s):* [SC133 Lec 27](../lectures.md)

## Intuition

[Energy conservation](conservation-of-energy.md), finally with the books complete.
Mechanics kept losing energy to "heat" — the first law brings it home: a system's
**internal energy** (the microscopic KE + PE of its molecules) changes only through
two currencies, **heat in** and **work out**. Track both and nothing is ever lost.
Every engine, refrigerator, and living cell is an entry in this ledger.

## The law

$$\boxed{\,\Delta E_\text{int} = Q - W\,}$$

- $Q$: heat **added to** the system (positive in)
- $W$: work done **by** the system (positive out) — watch conventions; some texts
  flip the sign of $W$
- $E_\text{int}$: internal energy — a **state function** (depends only on the current
  state), while $Q$ and $W$ are *path* functions (depend on how you got there)

For an [ideal gas](ideal-gas.md), $E_\text{int}$ depends on temperature alone:
$E_\text{int} = \tfrac{f}{2}nRT$ (with $f$ degrees of freedom; $f = 3$ monatomic).

## Work by a gas

A gas expanding against a piston does work

$$W = \int_{V_i}^{V_f} P\,dV \quad = \text{area under the curve on a } P\text{–}V \text{ diagram}$$

Different paths between the same endpoints enclose different areas — hence work (and
heat) are path-dependent while $\Delta E_\text{int}$ is not. This is why engines run
in *cycles*: loop area = net work per cycle.

## The standard processes (ideal gas)

| Process | Constant | First law becomes | Work |
|---|---|---|---|
| Isochoric | $V$ | $\Delta E = Q$ | $W = 0$ |
| Isobaric | $P$ | $\Delta E = Q - P\Delta V$ | $W = P\Delta V$ |
| Isothermal | $T$ | $Q = W$ ($\Delta E = 0$) | $W = nRT\ln(V_f/V_i)$ |
| Adiabatic | $Q = 0$ | $\Delta E = -W$ | gas cools as it expands |

Adiabatic (fast or insulated) processes obey $PV^\gamma = \text{const}$ — the physics
of diesel ignition (compress → hot), cloud formation (rising air expands → cools),
and [the adiabatic atmosphere in PC316](../../fluids/concepts/hydrostatic-equilibrium.md).

## Worked example: three ways between two states

One mole of monatomic gas goes from (P₀, V₀) to (P₀, 2V₀) isobarically.

Work: $W = P_0V_0$. Temperature doubles ($PV = nRT$), so
$\Delta E = \tfrac32 nR\,\Delta T = \tfrac32 P_0V_0$.
Heat: $Q = \Delta E + W = \tfrac52 P_0V_0$.

The same $\Delta E$ via a different path (isochoric heat then isothermal expansion)
would need *different* $Q$ and $W$ — but always the same difference. State vs path,
in numbers.

## Common mistakes

- **Sign chaos.** Decide the convention ($W$ = work *by* the system) and audit every
  term. An expanding gas does positive work; compressing it, negative.
- **"Adiabatic" ≠ "isothermal".** Adiabatic means no *heat* flow — the temperature
  usually changes precisely because $Q = 0$.
- **Treating $Q$ or $W$ as state functions** — "the heat in a gas" is as meaningless
  as "the work in a gas".
- **Forgetting $\Delta E_\text{int} = 0$ around any complete cycle** — so per cycle,
  net heat in = net work out: the engine's whole business model.

## Related concepts

- [Temperature & heat](temperature.md) — the players
- [Ideal gas](ideal-gas.md) — the model system for every process above
- [Second law](second-law-of-thermodynamics.md) — which processes *actually happen*
- [Conservation of energy](conservation-of-energy.md) — the mechanical prequel

## Knowledge graph position

**Prerequisites:** [Temperature & heat](temperature.md), [Conservation of energy](conservation-of-energy.md).
**Leads to:** [Ideal gas](ideal-gas.md), [Second law](second-law-of-thermodynamics.md), engines & refrigerators.

## Quiz

**Q1 (computational).** A gas absorbs 800 J of heat while doing 300 J of work. Change
in internal energy?

??? success "Answer"
    $\Delta E = Q - W = 800 - 300 = 500\,\text{J}$.

**Q2 (conceptual).** Why does a bicycle pump grow hot at the bottom even before
friction matters?

??? success "Answer"
    Rapid compression is nearly adiabatic: $Q \approx 0$, work is done *on* the gas
    ($W < 0$), so $\Delta E > 0$ — the air heats. The reverse (adiabatic cooling on
    expansion) frosts CO₂ fire extinguishers and spray-can nozzles.

**Q3 (multiple choice).** In an isothermal expansion of an ideal gas:
(a) $Q = 0$ (b) $W = 0$ (c) $Q = W$

??? success "Answer"
    **(c).** Constant $T$ ⇒ constant $E_\text{int}$ ⇒ every joule of work done by the
    gas is imported as heat.
