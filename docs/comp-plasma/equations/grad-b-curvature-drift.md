# Grad-B & Curvature Drifts

## Equations

**Grad-B drift** (field strength varies in space):

$$\boxed{\,\mathbf{v}_{\nabla B} = -\frac{m v_{\perp}^2}{2qB^3}\,\nabla B\times\mathbf{B}\,}$$

**Curvature drift** (field lines bend, curvature vector $\hat{\mathbf{R}}/R = \hat{\mathbf{B}}\cdot\nabla\hat{\mathbf{B}}$):

$$\boxed{\,\mathbf{v}_c = \frac{m v_{\parallel}^2}{qB^2}\,\frac{\hat{\mathbf{R}}}{R}\times\mathbf{B}\,}$$

**Combined** (vacuum-like fields, the tokamak workhorse):

$$\mathbf{v}_{\nabla B} + \mathbf{v}_c = \frac{m}{qB^2}\left(\frac{v_\perp^2}{2} + v_\parallel^2\right)\frac{\hat{\mathbf{R}}}{R}\times\mathbf{B}$$

## Physical meaning

- **Grad-B:** gyration circles are fatter where $B$ is weak, tighter where strong; the
  orbit fails to close and creeps sideways, perpendicular to both $\nabla B$ and
  $\mathbf{B}$.
- **Curvature:** streaming along a bent field line costs centripetal force
  $mv_\parallel^2/R$; the particle supplies it by drifting so the magnetic force
  provides the turn.

## Variables

$v_\perp$ — gyration speed · $v_\parallel$ — speed along $\mathbf{B}$ ·
$\nabla B$ — gradient of field *magnitude* · $R$ — field-line curvature radius ·
$q$ — signed charge.

## The crucial property: charge dependence

Both drifts flip direction with the sign of $q$ (and scale with energy): ions and
electrons separate → **currents** and **space charge**. In a purely toroidal field
($B \propto 1/r$, both drifts vertical) the resulting charge separation creates a
vertical E field whose [E×B drift](exb-drift.md) pushes the *whole* plasma outward —
the reason tokamaks need poloidal field (rotational transform) to survive. This
failure is beautifully visible in the course's
[toroidal-field orbit exercise](../concepts/guiding-center-drifts.md).

## Assumptions

Guiding-center ordering: $r_L \ll L_B$, $R$; drifts slow compared to gyration.
Both are first-order corrections in $r_L/L$ — see
[guiding-center theory](../concepts/guiding-center-drifts.md).

## Related equations

- [E×B drift](exb-drift.md) — the charge-independent sibling
- [Lorentz force](lorentz-force.md) — parent
- [Cyclotron motion](cyclotron-motion.md) — the zeroth-order motion being averaged

## Quiz

**Q1 (conceptual).** In a tokamak, grad-B and curvature drifts point the same way for
a given particle. Why?

??? success "Answer"
    For a toroidal field $B \propto 1/r$: $\nabla B$ points inward (−R̂) and the
    curvature vector also points inward, so $\nabla B\times\mathbf{B}$ and
    $\hat{\mathbf{R}}\times\mathbf{B}$ are parallel (both vertical, sign set by
    charge) — hence the neat combined formula.

**Q2 (computational).** A 1 keV proton ($v_\parallel^2 = v_\perp^2 = v^2/2$) in a
$B = 1$ T field with $R = 1$ m. Estimate the combined drift speed.

??? success "Answer"
    $v^2 = 2E/m \approx 1.9\times10^{11}\ \text{m}^2/\text{s}^2$;
    $v_d = \frac{m}{qBR}\left(\frac{v_\perp^2}{2} + v_\parallel^2\right)
    = \frac{1.67\times10^{-27}}{1.6\times10^{-19}\times1\times1}\times1.43\times10^{11}
    \approx 1.5\times10^{3}$ m/s — a slow creep beside the ~$4\times10^5$ m/s thermal
    speed, but relentless.

**Q3 (MCQ).** Which particle has the larger grad-B drift at equal *energy*?

- (a) electron  (b) proton  (c) equal  (d) depends on B

??? success "Answer"
    **(c).** The drift is $\frac{mv_\perp^2}{2qB^3}|\nabla B \times \mathbf B|$ — at equal
    perpendicular *energy* ($\frac12 mv_\perp^2$), mass cancels; magnitudes match
    (directions oppose).
