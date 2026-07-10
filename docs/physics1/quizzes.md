# Quizzes · Physics I

Integrative questions spanning the course — every concept page carries its own quiz
too. Work in [lecture order](lectures.md) the first time; before the exam, start here
and chase wrong answers back through the links.

## Easy

**E1 (conceptual).** A block slides across a floor at constant velocity. What is the
net horizontal force on it?

??? success "Answer"
    Zero — constant velocity means zero acceleration
    ([Newton's first law](concepts/newtons-laws.md)). The push and friction balance
    exactly.

**E2 (conceptual).** Why does a steel ship float when a steel ball sinks?

??? success "Answer"
    [Buoyancy](concepts/fluids.md) compares the *average* density of the hull-plus-air
    envelope with water; the ship displaces its weight in water long before
    submerging.

**E3 (computational).** What force parallel to a frictionless 30° incline holds a
0.5 kg block in place?

??? success "Answer"
    $F = mg\sin 30° = 0.5\times9.8\times0.5 = 2.45\,\text{N}$.

**E4 (MCQ).** Which increases a projectile's level-ground range?
(a) higher launch speed (b) lower angle, always (c) heavier ball

??? success "Answer"
    **(a)** — $R = v_0^2\sin 2\theta/g$ grows with $v_0^2$; the best angle is 45°,
    and mass never appears. [Projectile motion](concepts/projectile-motion.md).

## Medium

**M1 (conceptual).** If the net external torque on a system is zero, what is
conserved — and give two examples exploiting it.

??? success "Answer"
    [Angular momentum](concepts/rolling-torque-angular-momentum.md) $L = I\omega$.
    A skater pulling in her arms spins faster; a planet
    [sweeps equal areas](concepts/keplers-laws.md) as it orbits.

**M2 (computational).** Wave speed on a string with $\mu = 0.02$ kg/m under 200 N of
tension — and the fundamental frequency if the string is 0.5 m long, fixed at both
ends?

??? success "Answer"
    $v = \sqrt{T/\mu} = \sqrt{10^4} = 100\,\text{m/s}$;
    $f_1 = v/2L = 100\,\text{Hz}$ — see [standing waves](concepts/superposition.md).

**M3 (computational).** A 3 kg block at 4 m/s hits a stationary 1 kg block; they stick.
Final speed, and kinetic energy lost?

??? success "Answer"
    $v' = 3(4)/4 = 3\,\text{m/s}$;
    $K_i = 24\,\text{J}$, $K_f = 18\,\text{J}$: 6 J (25%) became heat and deformation —
    momentum conserved, [KE not](concepts/collision-and-impulse.md).

**M4 (conceptual).** A raw egg and a hard-boiled egg spin on a table. Which stops
wobbling when briefly touched — and why?

??? success "Answer"
    The hard-boiled one. Its rigid interior stops with the shell; the raw egg's liquid
    keeps its [angular momentum](concepts/rolling-torque-angular-momentum.md) and
    re-spins the shell after your finger lifts. (Also the standard kitchen test.)

**M5 (MCQ).** Doubling the absolute temperature of an ideal gas multiplies the rms
molecular speed by: (a) 2 (b) $\sqrt2$ (c) 4

??? success "Answer"
    **(b)** — $v_\text{rms} \propto \sqrt{T}$;
    see [molecular speeds](concepts/molecular-speed.md).

## Hard

**H1 (computational).** A solid sphere and a hoop roll (no slipping) from rest down
the same ramp of height 2 m. Find both bottom speeds.

??? success "Answer"
    $v = \sqrt{2gh/(1 + I/MR^2)}$
    ([rolling](concepts/rolling-torque-angular-momentum.md)):
    sphere ($2/5$): $v = \sqrt{2(9.8)(2)/1.4} \approx 5.3\,\text{m/s}$;
    hoop ($1$): $v = \sqrt{19.6} \approx 4.4\,\text{m/s}$ — geometry decides the race,
    not mass.

**H2 (computational).** A 10 g bullet at 300 m/s embeds in a 2 kg pendulum block.
How high does the block swing?

??? success "Answer"
    Two stages ([never one](concepts/collision-and-impulse.md)):
    collision — $V = \frac{0.01\times300}{2.01} \approx 1.49\,\text{m/s}$;
    swing — $h = V^2/2g \approx 11\,\text{cm}$. Energy "conservation" across the
    embedding would overestimate wildly.

**H3 (conceptual).** Two identical pendulum clocks: one at sea level, one atop a
mountain. Over a week, which is behind, and roughly why?

??? success "Answer"
    The mountain clock: $g$ is smaller up high
    ([gravitation](concepts/gravitation.md)), so $T = 2\pi\sqrt{L/g}$ is longer —
    it ticks slower and falls behind. (Historically how gravity surveys were done —
    [pendulum](concepts/pendulum.md).)

**H4 (computational).** A Carnot engine operates between 600 K and 300 K, producing
200 W of useful power. At what rate does it exhaust heat?

??? success "Answer"
    $e = 1 - 300/600 = 0.5$, so heat intake $= 400\,\text{W}$ and exhaust
    $= 200\,\text{W}$ — half the fuel's heat is the
    [second law's](concepts/second-law-of-thermodynamics.md) non-negotiable tax.

**H5 (conceptual).** A satellite experiences slight atmospheric drag. Explain why it
ends up moving *faster*.

??? success "Answer"
    Drag lowers the orbit's total energy $E = -GMm/2a$, shrinking $a$; but orbital
    speed $v = \sqrt{GM/r}$ *rises* as $r$ falls — the lost energy comes out of
    potential energy twice over ([virial logic](concepts/keplers-laws.md)). In
    orbits, brakes are accelerators.
