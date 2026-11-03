# Möbius Murrents

## What a half twist does to the field of a magnetic-moment flow

**Date:** 2026-11-03
**Status:** record, written by Claude at the user's request ("add it to the repo please"), from the 3 November conversation
**Builds on:** `what_starts_the_snowball_to_relativity_2026-11-02.md` (W8–W10: the selection rule and the thin-tube count)

---

## 1. Result

A half twist never selects a single azimuthal number. It splits the field between the two integers either side of a half-integer: $M=0$ and $M=1$ tie. Real magnets cannot carry an antiperiodic pattern, so this split, not a selection rule, is how a Möbius band shows up.

## 2. Why there is no antiperiodic pattern

A magnet's moment must return to itself after one circuit, so the moment pattern of a moment flow is single-valued. In a Möbius resonator a mode can come back with a minus sign; here it cannot. That leaves two physical placements on a Möbius band: on the centre line with a wall, or on the edge, which goes round twice.

## 3. Centre line, following the band, with a wall

**Setting.** Centre line: a circle of radius $R$. Moments follow the band's width direction, which turns by $\pi$ about the tangent per circuit: $\theta(\phi)=\phi/2$ in the plane spanned by $\hat{\boldsymbol\rho}$ and $\hat{\mathbf z}$. Single-valuedness forces a wall that catches up the missing $\pi$. The source per length is $\mathbf K\propto\hat{\mathbf t}\times\mathbf m=(\sin\theta,\,-\cos\theta)$ in $(\hat{\boldsymbol\rho},\hat{\mathbf z})$. For a ring, the scalar multipole with azimuthal number $M$ is fed by the $M$-th Fourier component of $K_\rho$ and $K_z$.

**Sharp wall, exactly.** Write $\mathbf K$ in its two circular components, proportional to $e^{\pm i\phi/2}$ on $[0,2\pi)$. Their Fourier coefficients involve

$$
\frac{1}{2\pi}\int_0^{2\pi}e^{i(\pm\frac12-M)\phi}\,d\phi=\frac{e^{2\pi i(\pm\frac12-M)}-1}{2\pi i(\pm\frac12-M)}=\frac{i}{\pi(\pm\frac12-M)},
$$

since $e^{2\pi i(\pm\frac12-M)}=-1$. So each circular component has weight $1/(\pi\,|M\mp\tfrac12|)$.

- The spectrum is centred on $\pm\tfrac12$, and $M=0$, $M=\pm1$ tie.
- The tail falls as $1/|M|$; fitted power $-1.003$. The numerical spectrum matches the exact coefficients to four figures at $M=-2,0,1,3$.
- Compare an integer framing on the same ring: $\mathrm{Lk}=0$ gives $M=0$ only, and $\mathrm{Lk}=1$ gives $M=\pm1$ only.

**Finite wall.** A wall of angular width $\delta$ cuts the tail off beyond $M\sim1/\delta$. At $M=32$: sharp about $0.02$, width $0.3$ about $5\times10^{-3}$, width $1.0$ about $7\times10^{-5}$.

**Wall sense barely matters.** A wall turning by $+\pi$ makes $\mathrm{Lk}=1$; one turning by $-\pi$ makes $\mathrm{Lk}=0$. Their spectra differ by under 10% in every component (width 0.3: $M=0$ gives 0.613 against 0.660; $M=\pm1$ gives 0.485 against 0.464). The half twist sets the spectrum, not the integer the wall happens to complete.

## 4. Edge, pointing across the band, no wall

**Setting.** Parameter $\psi\in[0,2\pi)$. Centre $\mathbf c=R(\cos2\psi,\sin2\psi,0)$, band direction $\mathbf b=\cos\psi\,\hat{\boldsymbol\rho}(2\psi)+\sin\psi\,\hat{\mathbf z}$, edge $\mathbf r=\mathbf c+w\,\mathbf b$, moment $\mathbf m=-\mathbf b$ (projected normal to the edge). The edge goes round the axis twice and closes, so the pattern is a smooth integer framing.

**Numbers.** $\mathrm{Lk}=-2$ and $\mathrm{Lk}_0=-1$ (the edge is a $T(2,1)$ torus curve, and $\mathrm{Lk}_0=-q(a-1)$), so $n=\mathrm{Lk}-\mathrm{Lk}_0=-1$: half a turn per circuit of the axis.

**Thin-band count.** The edge has no rotational symmetry ($q=1$), but the thin-tube count of the snowball record's W10 applies with $a=2$:

$$
2M=\pm n+j,\qquad |Q_{\ell M}|\sim w^{|j|}.
$$

With $n$ odd, $M=0$ and $M=1$ both need $|j|=1$, so they enter at the same order. $M=2$ needs $|j|=3$ and $M=3$ needs $|j|=5$: relative suppressions $w^2$ and $w^4$.

| Band half-width $w$ | $M=0$ | $M=1$ | $M=2$ | $M=3$ |
| --- | --- | --- | --- | --- |
| 0.1 | 0.15 | 1 | 0.027 | $4.7\times10^{-5}$ |
| 0.2 | 0.15 | 1 | 0.11 | $7.3\times10^{-4}$ |
| 0.3 | 0.14 | 1 | 0.23 | $3.5\times10^{-3}$ |

Largest multipole per $M$ up to $\ell=6$, relative to $M=1$. The $M=0:M=1$ ratio stays fixed, as equal order requires. $M=2$ grows like $w^2$ (factor 3.95 from $w=0.1$ to $0.2$) and $M=3$ like $w^4$ (factor 15.6). $M=4$ is at the numerical floor ($10^{-11}$ to $10^{-9}$) and was not used.

## 5. Reading

A half-integer winding splits rather than selects. With a wall, the split is exact and broad: $1/|M-\tfrac12|$, with a tail set by the wall's width. On the edge, it is a tie in order between $M=0$ and $M=1$. In both cases the Möbius structure is visible in the field only through which integers share the weight, never through a forbidden one.

Scripts: `mobius.py`, `mobius_edge.py` (3 November conversation, not filed).
