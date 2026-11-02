# What Starts the Snowball to Relativity

## Which electromagnetic force laws a Galilean Newtonian theory can hold without paradox

**Date:** 2026-11-02
**Status:** record, written by Claude at the user's request from the 2 November conversation ("put these together in their own record in NM analysis")
**Scope:** the Galilean/relativistic divide stated as a condition on state; which EM force laws sit on the Galilean side; what actually forces the step to relativity; an input to the open Ampère-vs-Grassmann ruling for NM magnetism

---

## 1. The claim and its sharpened form

**His claim (2 November):** if the static forces were the only electromagnetic forces known (Coulomb, current–current, magnet–magnet and the static electric action of a magnetic-moment flow), there would be no paradoxes leading to relativity. Everything beyond them causes subtle problems that snowball into relativity.

**The half that holds.** Every one of those laws depends on relative configuration only. None asks "velocity relative to what?", none mixes $\mathbf E$ and $\mathbf B$ under a change of frame, and none has a magnet–conductor asymmetry. A theory built from them is consistently Galilean (Section 3).

**The half that overreaches.** "Everything else snowballs" is too strong. Weber's electrodynamics is instantaneous, Galilean-invariant and velocity-dependent, and it derives Faraday induction and Ampère's force (Section 4). The class of paradox-free laws is larger than statics.

**Sharpened version:**

> Instantaneous Galilean particle theories whose energy is a function of the present state are paradox-free. The snowball starts the moment an interaction has to propagate.

Induction, $\mathbf E$–$\mathbf B$ mixing and the magnet–conductor asymmetry are symptoms that appear once fields have been accepted. The cause is finite propagation (Section 5).

---

## 2. The framework the claim rests on

Three conditions on a theory of $N$ particles with configuration $Q(t)=(\mathbf x_1(t),\dots,\mathbf x_N(t))$:

- **C1 (current state).** Dynamics is a flow on a state space $\Gamma$, and the conserved energy is a function on $\Gamma$: $E = E(S(t))$. This excludes energies built from integrals along worldline histories (Fokker, Wheeler–Feynman).
- **C2 (configuration only).** $\Gamma$ is particle phase space and the interaction depends on positions alone: $H = \sum_i |\mathbf p_i|^2/2m_i + U(Q)$.
- **C3 (Galilean covariance).** $U$ is invariant under rotations and translations; the equations keep their form under boosts.

**Newtonian mechanics comes out as theorems.** If $U$ depends only on $Q$ and is translation-invariant:

1. Boost invariance is automatic: a boost at fixed $t$ shifts every $\mathbf x_i$ by the same vector, so every separation $r_{ij}$ is unchanged.
2. The third law holds at every instant: $\sum_i \partial U/\partial \mathbf x_i = 0$, so $\sum_i \mathbf F_i(t) = 0$.
3. Particle momentum is conserved on its own; nothing else has to carry momentum.

Newtonian gravity satisfies C1–C3 exactly.

**The divide.** The Currie–Jordan–Sudarshan no-interaction theorem (1963; Leutwyler 1965 for $N$ particles): if the Poincaré group acts canonically on particle-only phase space and the canonical positions transform as worldline points, the particles do not interact. So "current state only, particles only" is not merely compatible with Galilean physics; with interaction, it requires it. Holding C1, relativity forces one of three exits:

1. enlarge the state with free field data, i.e. an independent energy store (Maxwell);
2. give up that canonical positions are the physical positions (Bakamjian–Thomas);
3. give up C1 and accept history-dependent energy (Fokker, Wheeler–Feynman).

**The line between.** Retardation expands in powers of $1/c$, each power trading history for one more time derivative of the present state. At order $c^0$ the interaction depends on $Q$ (Coulomb). At $c^{-1}$ the scalar term vanishes by charge conservation. At $c^{-2}$ it depends on $(Q,\dot Q)$ (Darwin Lagrangian) and still needs no store. At $c^{-3}$ radiation reaction appears, particle energy is no longer conserved, and C1 forces a store.

---

## 3. The paradox-free static set

With currents, magnets and magnetic-moment flows taken as primitives (not as moving charges), every pair law is configuration-only:

| Pair | Energy, configuration only | Status |
| --- | --- | --- |
| Charge–charge | $q_iq_j/4\pi\varepsilon_0 r$ | Coulomb |
| Current–current | Helmholtz family, one free parameter $\kappa$ (Section 6) | Biot–Savart for closed loops, all $\kappa$ |
| Magnet–magnet | $\mu_0[\mathbf m_1\cdot\mathbf m_2 - 3(\mathbf m_1\cdot\hat{\mathbf r})(\mathbf m_2\cdot\hat{\mathbf r})]/4\pi r^3$ | Small-loop limit of current–current |
| Current–magnet | $-\mathbf m\cdot\mathbf B_j$ | Fixed by the loop limit; $\kappa$ drops out |
| Charge–current | $q\,(\mathbf j\cdot\hat{\mathbf r})\,f(r)$ | Parity-allowed; vanishes round any closed loop |
| Charge–magnet | would be a pseudoscalar | Forbidden by parity |
| Magnetic-moment flow on charge | $\mathbf E_K = \frac{\mu_0}{4\pi}\,[3(\mathbf K\cdot\hat{\mathbf R})\hat{\mathbf R}-\mathbf K]/R^3$, with $\mathbf K = \mathbf u_{\mathrm{rel}}\times\mathbf m$, $\mathbf u_{\mathrm{rel}}$ the magnets' velocity relative to the device | The static electric acting object of the 2026-08-19 record |

Static energies contain no velocities, so time reversal constrains nothing here; parity is the only selection rule.

---

## 4. The counterexample: Weber

Weber's electrodynamics (1846) is instantaneous and Galilean-invariant, with forces depending on the relative distance, radial velocity and radial acceleration of the charges. Weber derived Faraday's law of induction from it, and Ampère's force between current elements follows as a special case. So:

- **induction alone does not force relativity** — Weber had it inside a Galilean theory;
- the paradox-free class contains at least the instantaneous, Galilean, relative-velocity laws. That is already the scope NM takes for magnetism (force laws may depend on relative velocity, never absolute velocity).

**Reconciliation owed.** C2 (positions only) is stricter than NM's own relative-velocity scope. C2 picks out Newtonian *statics* inside the Galilean class; it is not the Galilean class itself. The 2 November working doc records this as its parked issue #1.

---

## 5. What actually starts the snowball

Weber's theory did not fail on relativity paradoxes. It failed on:

1. **an energy pathology** — Helmholtz's objection, effective negative mass for speeds below $c$, which permits runaway motion;
2. **light** — the theory has no waves; nothing propagates.

Combine that with the C1 argument. A disturbance that takes time to cross space, together with an energy that is a function of the present state, forces an intermediate store: in the gust experiment, the air; in electromagnetism, the field. A store means a state space with free field data, and with that state the no-interaction theorem points to Lorentz invariance. So the order is:

> finite propagation + C1 → store → fields with free data → Lorentz

Induction as a field law, $\mathbf E$–$\mathbf B$ mixing under boosts and the magnet–conductor asymmetry come after the second arrow.

---

## 6. Input to the open ruling: Ampère or Grassmann

NM's magnetism scope leaves open whether its current-element law is **Ampère's** (central, strong third law) or **Grassmann's** (Biot–Savart form; strong third law fails for isolated elements, recovered for closed circuits).

The two sit in one family. Maxwell's most general element force has a free constant $k$: Ampère took $k=-1$; Gauss, Grassmann and Clausius took $k=+1$; Weber took $k=-1$, Riemann $k=+1$; integrating round a closed circuit eliminates $k$, so closed-circuit experiments cannot decide. Helmholtz's matching potential family is

$$
U_{kl} = -\frac{\mu_0}{8\pi\, r_{kl}}\Big[(1+\kappa)\,\mathbf j_k\cdot\mathbf j_l + (1-\kappa)\,(\mathbf j_k\cdot\hat{\mathbf r}_{kl})(\mathbf j_l\cdot\hat{\mathbf r}_{kl})\Big],
$$

with $\kappa=+1$ Neumann, $\kappa=0$ Maxwell, $\kappa=-1$ Weber. The $\kappa$-dependent part is a mixed derivative $\partial^2 r/\partial s_1\partial s_2$, which integrates to zero round closed loops.

**What C1 and the third law decide (corrected; see W4).** Neither historical element law survives. Grassmann's has no energy and fails even the weak third law. Ampère's is central, so it keeps the strong third law, but its force has nonzero curl at fixed orientations, so it has no configuration energy either. With primitive currents and an energy that is a function of the present state, the element law must be a gradient of the Helmholtz family, and the strong third law then selects **Neumann's** ($\kappa=+1$), whose element torques cancel. Ampère's force belongs to Weber's ontology, where the state includes the carriers' velocities; NM's primitive currents have none. Offered as input; the ruling is his. (The first version of this record named Ampère as the consistent choice; W4 shows why that was wrong.)

---

## 7. Where induction enters: the boundary marker

In C1–C3 statics, moving a magnet past a charge does nothing: there is no charge–magnet coupling (parity forbids it). That absence is exactly why the theory is consistently Galilean. The electric field of moving magnets — physically, induction — enters only as a separately posited primitive: the magnetic-moment-flow static electric acting object of `STATIC_ELECTRIC_ACTING_OBJECT_RESULT_2026-08-19_d1.md` (called a "murrent" in the 2 November conversation). Making that field arise *automatically* from moving magnets is the step that pushes a theory past C2. It is the magnet–conductor asymmetry that opens Einstein's 1905 paper. So the 08-19 acting object marks where Galilean statics meets relativity.

**Dissipation fits the same logic.** Friction and drag break energy conservation at the particle level, so under C1 they signal a hidden store (heat, the air's degrees of freedom). Newtonian mechanics stays coherent if every non-conservative force is read as energy flowing into unmodelled stores.

---

## 8. Relation to the 2026-08-19 records

**Value equivalence is not acting-object reduction.** The 2 November conversation found that every field and force of a magnetic-moment flow equals that of an electric dipole density $\mathbf P = \mathbf u_{\mathrm{rel}}\times\mathbf M/c^2$, and argued from C1 that any new static source of $\mathbf E$ must be curl-free and hence charge-reproducible. That is a statement about *values*. `STATIC_ELECTRIC_ACTING_OBJECT_RESULT` (sec. 7) already argues that exterior force-profile equivalence does not license source reduction: a fictitious charge distribution has no source warrant. Both stand. The 2 November "reduction result" should be read as extensional only, and does not reduce the acting object.

**Open-work items of the 08-19 record that the 2 November work bears on:**

- **Item 1, universal kernel:** $\mathbf E_K = \frac{\mu_0}{4\pi}[3(\mathbf K\cdot\hat{\mathbf R})\hat{\mathbf R}-\mathbf K]/R^3$ per element, $\mathbf K = \mathbf u_{\mathrm{rel}}\times\mathbf m$, perpendicular to the direction of motion. Here $\mathbf u_{\mathrm{rel}}$ is the magnets' velocity relative to the device (in the 2 November derivation, the stationary line of opposite magnets that cancels their $\mathbf B$), which is what keeps the kernel unchanged under Galilean boosts; this matches the 08-19 record's sec. 5, $\mathbf u_{\mathrm{rel}}=\mathbf v_{\mathrm{belt}}-\mathbf v_{\mathrm{tube}}$. (Corrected the same day: the first version wrote the magnets' lab velocity, which is not boost-invariant.)
- **The kernel is certified at element level, with no free parameter.** $\mathbf K=\mathbf u_{\mathrm{rel}}\times\mathbf m$ vanishes wherever the magnets point along their path, so a closed loop of moving magnets aligned with the path everywhere except one short tilted segment carries murrent on that segment only, in a fully stationary configuration. The parent theory therefore fixes the single-element law directly: the plain dipole law with $\mathbf p=\mathbf u_{\mathrm{rel}}\times\mathbf m/c^2$ exactly (W1), with no dependence on the direction of motion (W3). Currents cannot be isolated this way, since stationarity forces $\nabla\cdot\mathbf J=0$, which is why their element law keeps the free $\kappa$ of Section 6 and the murrent's has none.\n- **Couplings to currents and magnets are zero in static configurations.** If the cancelling line cancels the moving magnets' lab magnetization exactly, the pure magnetic-moment flow is a static polarization with $\mathbf B=0$ at all orders, so it exerts nothing on currents or magnets, and neither feels a net force in its static $\mathbf E$ (W2). A nonzero coupling appears only under relative motion, which is velocity-dependent and outside C2. So in value the moment flow differs from a charge distribution nowhere; what separates them is the acting-object identity the 08-19 record argues for. (Added the same day.) The element carries a position plus a full frame (direction of motion, $\hat{\mathbf K}$), so its configuration space is $\mathbb R^3\times SO(3)$.
- **Item 3, exact static domain:** for a train of moving dipoles at spacing $a$, the ripple harmonics decay like $e^{-2\pi k d/\gamma a}$ at distance $d$, so the continuum limit is exactly static. A twisting direction pattern is static only if it is fixed in space, each magnet rotating as it travels.
- **Item 6, Galilean-EM comparison:** the motional field is a $1/c^2$ effect; it vanishes in the electric Galilean limit and survives in the magnetic one.
- **Further results:** a twisted line screens its field like $e^{-q\rho}$ beyond one pitch; on a closed loop the twist is quantised, and on a loop with $q$-fold symmetry the multipole with azimuthal number $M$ survives iff $M \equiv \pm\mathrm{Lk} \pmod q$ (confirmed numerically to $\ell=6$). Full working: the 2 November doc, https://claude.ai/artifact/FxTWLM3hoJXKe44oFTPo31

---

## 9. What this record does not settle

- The static set is paradox-free partly because it is empirically thin. Rowland's spinning charged disc and induction experiments are phenomena it cannot produce; they push toward Weber-type relative-velocity laws, not toward relativity.
- Weber's own energy pathology is not resolved here; a paradox-free class must still survive Helmholtz's objection.
- The C2-versus-relative-velocity reconciliation (Section 4) is owed.

---

## Sources

- Currie, Jordan and Sudarshan, *Relativistic invariance and Hamiltonian theories of interacting particles*, Rev. Mod. Phys. 35, 350 (1963); Leutwyler, Nuovo Cimento 37, 556 (1965). Cited from memory.
- Ampère's force law, Maxwell's general element force and the historical values of $k$: https://en.wikipedia.org/wiki/Amp%C3%A8re%27s_force_law
- Helmholtz's potential family and its parameter: Helmholtz, *On the theory of electrodynamics* (1872), https://isidore.co/misc/Physics%20papers%20and%20books/Zotero/storage/Q79WRJMZ/Helmholtz%20-%201872%20-%20LXIII.%20On%20the%20theory%20of%20electrodynamics.pdf ; and J. D. Jackson and L. B. Okun, *Historical roots of gauge invariance*, https://arxiv.org/pdf/hep-ph/0012061
- Weber's law deriving Faraday induction and Ampère's force: A. K. T. Assis, *Weber's Law and Mach's Principle* (1995), https://www.ifi.unicamp.br/~assis/Weber-Law-Mach-Principle-p159-171(1995).pdf
- Helmholtz's negative-mass objection to Weber: https://www.mdpi.com/2673-8724/3/2/9
- Einstein, *Zur Elektrodynamik bewegter Körper* (1905), opening paragraph on the magnet and conductor.

---

## Appendix: Workings (begun 2026-11-02)

Each item derives a claim made above. What is still unwritten is listed at the end.

### W1. Moving magnets: the motional polarization, exactly

Bound sources form an antisymmetric tensor $\mathcal M^{\mu\nu}$ with $J^\mu=\partial_\nu\mathcal M^{\mu\nu}$, where $\mathcal M^{i0}=cP^i$ and $\mathcal M^{ij}=\epsilon^{ijk}M_k$. Check: $J^0=\partial_i\mathcal M^{0i}=-c\,\nabla\cdot\mathbf P$, so $\rho=-\nabla\cdot\mathbf P$; and $J^i=\partial_0\mathcal M^{i0}+\partial_j\mathcal M^{ij}=\partial_tP^i+(\nabla\times\mathbf M)^i$.

Comparing with the field tensor, $(c^2\mathbf P,\,-\mathbf M)$ transforms exactly like $(\mathbf E,\,\mathbf B)$. The field transformation to a frame moving at $\mathbf v$ is $\mathbf E'_\perp=\gamma(\mathbf E+\mathbf v\times\mathbf B)_\perp$ and $\mathbf B'_\perp=\gamma(\mathbf B-\mathbf v\times\mathbf E/c^2)_\perp$, with parallel parts unchanged. Hence

$$
\mathbf P'_\perp=\gamma\Big(\mathbf P-\frac{\mathbf v\times\mathbf M}{c^2}\Big)_\perp,\qquad
\mathbf M'_\perp=\gamma\,(\mathbf M+\mathbf v\times\mathbf P)_\perp .
$$

Magnets at rest have $\mathbf P_0=0$ and magnetization $\mathbf M_0$. The lab moves at $-\mathbf u$ relative to them, so

$$
\mathbf P_{\rm lab}=\gamma\,\frac{\mathbf u\times\mathbf M_0}{c^2},\qquad
\mathbf M_{{\rm lab},\perp}=\gamma\,\mathbf M_{0\perp},\qquad
\mathbf M_{{\rm lab},\parallel}=\mathbf M_{0\parallel}.
$$

Since $\mathbf u\times\mathbf M$ uses only the perpendicular part, this is, exactly and to all orders,

$$
\boxed{\;\mathbf P=\frac{\mathbf u\times\mathbf M_{\rm lab}}{c^2}\;}
$$

**One point magnet.** With rest-frame moment $\mathbf m$, the dipole's tensor density is $c\int d\tau\,m^{\mu\nu}\,\delta^4(x-z(\tau))$, and $\int c\,d\tau\,\delta(ct-ct(\tau))=1/\gamma$. That $1/\gamma$ cancels the boost's $\gamma$, so $\mathbf p=\mathbf u\times\mathbf m/c^2$ exactly. **Correction:** sec. 8 first wrote $\mathbf p=\gamma\,\mathbf u\times\mathbf m/c^2$, wrong by a factor $\gamma$; it is fixed there. The $\gamma$ belongs to densities compared with rest-frame densities, not to a single dipole.

**Rotating magnets.** The transformation is pointwise along each worldline and contains no time derivative of $\mathbf m$. So a moment pattern fixed in space, with each magnet rotating as it travels, still gives averaged sources $\mathbf P(\mathbf x)=\mathbf u\times\mathbf M_{\rm lab}(\mathbf x)/c^2$.

### W2. The pure moment flow has $\mathbf B=0$ exactly and couples to nothing magnetic

The device: moving magnets with averaged lab magnetization $\mathbf M_{\rm lab}(\mathbf x)$, time-independent because the pattern is fixed in space, plus stationary magnets with magnetization $-\mathbf M_{\rm lab}(\mathbf x)$, which carry no polarization. Totals:

$$
\mathbf M_{\rm tot}=0,\qquad
\mathbf P_{\rm tot}=\frac{\mathbf u\times\mathbf M_{\rm lab}}{c^2},\qquad
\partial_t\mathbf P_{\rm tot}=0 .
$$

So $\mathbf J=\partial_t\mathbf P_{\rm tot}+\nabla\times\mathbf M_{\rm tot}=0$ and $\rho=-\nabla\cdot\mathbf P_{\rm tot}$. The sources are a static polarization with no current: $\mathbf B=0$, and $\mathbf E=-\nabla\phi$ with $\phi$ the potential of $\mathbf P_{\rm tot}$. This is exact at all orders in $u/c$ for the averaged sources.

**Couplings in static configurations, both directions.** The force on any source distribution is $\int(\rho\,\mathbf E+\mathbf J\times\mathbf B)\,d^3x$.

- *Device on a current or a magnet.* A neutral steady current has $\rho=0$. A magnet's sources are $\rho_b=0$ and $\mathbf J_b=\nabla\times\mathbf M$. The device supplies $\mathbf B=0$, so both integrands vanish: zero force.
- *Current or magnet on the device.* Either supplies $\mathbf E=0$ and some static $\mathbf B$. The device has $\mathbf J=0$, so $\mathbf J\times\mathbf B=0$, and $\rho\,\mathbf E=0$: zero force.
- The ripple's fields oscillate in time, and forces linear in them average to zero.
- Momentum bookkeeping: the configuration still holds field momentum $\varepsilon_0\int\mathbf E\times\mathbf B\,d^3x=c^{-2}\int\phi\,\mathbf J\,d^3x$, balanced by hidden momentum in the current. Both stay constant while nothing moves. They produce forces only under relative motion, which is velocity-dependent and outside C2.

### W3. The moment-flow element law is unique (no $\kappa$ analogue)

Two assumptions: **superposition**, i.e. a configuration's field is $\oint\mathbf e(\mathbf K(s),\hat{\mathbf t}(s),\mathbf x-\mathbf y(s))\,ds$ with $\mathbf e$ linear in $\mathbf K$; and **locality**, i.e. $\mathbf e$ depends only on the element's own data.

1. By W1 and W2 the parent theory certifies, for any closed path traversed at speed $u$ and any moment pattern fixed in space, a static field equal to that of $\mathbf P=\mathbf u\times\mathbf M_{\rm lab}/c^2$ on the path. Per length, $\mathbf k(s)=u\,\hat{\mathbf t}(s)\times\boldsymbol\mu(s)$.
2. $\mathbf k=0$ wherever $\boldsymbol\mu\parallel\hat{\mathbf t}$. Align the magnets with the path everywhere except a segment $S$ and tilt them on $S$: the certified field is that of a polarization on $S$ alone.
3. Write $\mathbf e=\mathbf e_{\rm D}+A(\hat{\mathbf t},\mathbf R)\,\mathbf K$, with $\mathbf e_{\rm D}$ the dipole law. Agreement for every such configuration requires $\int_S A(\hat{\mathbf t}(s),\mathbf x-\mathbf y(s))\,\mathbf k(s)\,ds=0$ for every segment and every profile $\mathbf k\perp\hat{\mathbf t}$. Shrinking $S$ gives $A(\hat{\mathbf t},\mathbf R)\,\mathbf k=0$ for all $\mathbf k\perp\hat{\mathbf t}$. Since $\mathbf K$ is always perpendicular to $\hat{\mathbf t}$, the extra term acts on nothing: $\mathbf e=\mathbf e_{\rm D}$.

**Contrast with currents.** Stationarity forces $\nabla\cdot\mathbf J=0$, so the current $I$ is the same all round a circuit and cannot be confined to a segment. An addition $I\,\mathbf A(\hat{\mathbf t},\mathbf R)$ then needs only $\oint\mathbf A\,ds=0$ on every closed curve, which any derivative along the curve satisfies: $\mathbf A=(\hat{\mathbf t}\cdot\nabla_{\mathbf y})\,\mathbf g(\mathbf x-\mathbf y)$. That freedom is the $\kappa$ family of sec. 6.

### W4. Element force laws: which survive C1 and the third law

Units $\mu_0I_1I_2/4\pi=1$. Element $\mathbf a$ sits at the origin, element $\mathbf b$ at $\mathbf R$; $\hat{\mathbf R}$ points from $\mathbf a$ to $\mathbf b$.

**Grassmann.** $\mathbf F_{\mathbf a\to\mathbf b}=\mathbf b\times(\mathbf a\times\hat{\mathbf R})/R^2$ and $\mathbf F_{\mathbf b\to\mathbf a}=-\mathbf a\times(\mathbf b\times\hat{\mathbf R})/R^2$. Expanding both triple products,

$$
\mathbf F_{\mathbf a\to\mathbf b}+\mathbf F_{\mathbf b\to\mathbf a}=\frac{\mathbf a(\mathbf b\cdot\hat{\mathbf R})-\mathbf b(\mathbf a\cdot\hat{\mathbf R})}{R^2}=\frac{\hat{\mathbf R}\times(\mathbf a\times\mathbf b)}{R^2}\neq0 .
$$

Even the weak third law fails. Example: $\mathbf a\perp\hat{\mathbf R}$ and $\mathbf b\parallel\hat{\mathbf R}$ push $\mathbf b$ with force $|\mathbf b|\,\mathbf a/R^2$ while $\mathbf a$ feels nothing. A pair energy $U(\mathbf y_{\mathbf b}-\mathbf y_{\mathbf a},\mathbf a,\mathbf b)$ always gives equal and opposite forces (sec. 2), so Grassmann's law has no energy.

**Ampère.** $\mathbf F_{\mathbf a\to\mathbf b}=-h(\hat{\mathbf R})\,\hat{\mathbf R}/R^2$ with $h=2\,\mathbf a\cdot\mathbf b-3(\mathbf a\cdot\hat{\mathbf R})(\mathbf b\cdot\hat{\mathbf R})$. It is central, so the strong third law holds. But since $\nabla\times(\hat{\mathbf R}/R^2)=0$,

$$
\nabla_{\mathbf R}\times\mathbf F_{\mathbf a\to\mathbf b}=-\frac{\nabla h\times\hat{\mathbf R}}{R^2}\neq0 ,
$$

because $h$ depends on direction and $\nabla h$ has a part perpendicular to $\hat{\mathbf R}$. Carrying element $\mathbf b$ round a closed path at fixed orientations does net work, so **Ampère's element force has no configuration energy either**.

**Helmholtz family.** $U_\kappa$ (sec. 6) is conservative by construction. Its force is central only for $\kappa=+1$ (Neumann), where $U=-(\mathbf a\cdot\mathbf b)/R$ depends on $R$ alone; every other member gets a transverse force from the $(\mathbf a\cdot\hat{\mathbf R})(\mathbf b\cdot\hat{\mathbf R})$ term. Neumann's element torques, $\mathbf a\times\mathbf b/R$ on $\mathbf a$ and $\mathbf b\times\mathbf a/R$ on $\mathbf b$, cancel, so angular momentum closes too.

**Neumann is the only central conservative law.** A conservative force is central only if $U$ does not depend on $\hat{\mathbf R}$ at fixed orientations. With bilinearity, rotation and parity invariance and $1/R$ scaling, the only scalar left is $\mathbf a\cdot\mathbf b$, so $U\propto(\mathbf a\cdot\mathbf b)/R$.

**Numerical check** (three random configurations; script `element_laws_check.py`, in the 2 November conversation, not filed): the curl of the Grassmann and Ampère forces is between $10^{-2}$ and $10^{0}$, so nonzero; Grassmann's force sum is nonzero; the transverse part of the $\kappa=+1$ gradient force is at most $2\times10^{-11}$, while for $\kappa=0$ and $\kappa=-1$ it is of order one.

**Consequence: sec. 6 corrected.** With primitive currents and C1, Ampère's element law is excluded as well as Grassmann's. The law that satisfies C1, the strong third law and angular-momentum balance is **Neumann's** ($\kappa=+1$). Ampère's force belongs to Weber's ontology, where the state includes the carriers' velocities; NM's primitive currents have no carriers.

### Not yet written

- The potential-theory lemma behind the 2 November reduction result: a curl-free exterior field whose sources lie on a path is reproducible by charges on or near it.
- Derivation of the Helmholtz family's two-term form from bilinearity, rotation and parity invariance and $1/R$ scaling.
- The C1–C3 consequences of sec. 2 written out in full.
- The symmetry step of the $\mathrm{Lk} \bmod q$ selection rule (the symmetry turns the framing by $2\pi\,\mathrm{Lk}/q$), currently backed by numerics only.
