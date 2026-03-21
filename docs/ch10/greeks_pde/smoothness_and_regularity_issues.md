# Smoothness and Regularity Issues


Regularity of \(V\) and Greeks depends on:
- regularity of payoff \(\Phi\),
- ellipticity/smoothness of coefficients,
- time distance to maturity.

---

## Diffusion smoothing: precise statement


Parabolic equations smooth initial/terminal data for \(t<T\). Even if \(\Phi\) is not \(C^1\), \(V(t,\cdot)\) is often smooth for \(t<T\) (away from degeneracies such as \(S=0\)).

**Schauder estimates.** For the Black–Scholes equation with bounded, measurable terminal data \(\Phi\), the solution satisfies:

\[
V \in C^{\infty}((0,T) \times (0,\infty))
\]

More precisely, for any \(\alpha \in (0,1)\) and compact \(K \subset (0,T) \times (0,\infty)\), we have interior Hölder estimates:

\[
\|V\|_{C^{2+\alpha, 1+\alpha/2}(K)} \leq C_K \|\Phi\|_{L^\infty}
\]

where the parabolic Hölder space \(C^{2+\alpha, 1+\alpha/2}\) captures two spatial derivatives and one time derivative with Hölder continuity.

**Heat kernel interpretation.** The fundamental solution (heat kernel) of the log-transformed Black–Scholes equation is Gaussian:

\[
G(t,x;T,y) = \frac{1}{\sqrt{2\pi\sigma^2(T-t)}} \exp\!\left(-\frac{(y-x-(r-\frac12\sigma^2)(T-t))^2}{2\sigma^2(T-t)}\right)
\]

Convolution with any \(L^1\) terminal data produces a \(C^\infty\) function for \(t < T\).

---

## Kinks and gamma concentration


For \(\Phi(S)=(S-K)^+\), the second derivative at maturity is distributional:

\[
\Phi''(S) = \delta(S-K) \quad \text{(Dirac mass)}
\]

For \(t<T\), diffusion replaces this by a narrow bump of width \(\mathcal{O}(\sqrt{T-t})\).

**Quantitative smoothing.** The gamma at time \(t < T\) satisfies:

\[
\Gamma(t,S) = \frac{1}{S\sigma\sqrt{\tau}} N'(d_1) \leq \frac{1}{S\sigma\sqrt{2\pi\tau}}
\]

The maximum gamma occurs at \(S = K e^{-(r-\frac12\sigma^2)\tau} \approx K\) and equals:

\[
\Gamma_{\max}(t) = \frac{1}{K\sigma\sqrt{2\pi\tau}} = \mathcal{O}(\tau^{-1/2})
\]

This shows how the Dirac mass "regularizes" into a smooth bump with:
- **Height**: \(\mathcal{O}(\tau^{-1/2})\)
- **Width**: \(\mathcal{O}(\sqrt{\tau})\)
- **Area** (integral of \(\Gamma\)): \(\mathcal{O}(1)\), independent of \(\tau\)

---

## Degenerate coefficients


The Black–Scholes operator

\[
\mathcal{L} = \frac{1}{2}\sigma^2 S^2 \partial_{SS} + rS\partial_S
\]

degenerates at \(S = 0\) (the coefficient of \(\partial_{SS}\) vanishes). This creates:

- **Boundary layer effects** near \(S = 0\)
- **Reduced regularity** compared to uniformly elliptic equations
- **Need for weighted Sobolev spaces** for rigorous analysis

The standard approach is to work in log-coordinates \(x = \ln S\), where the operator becomes uniformly elliptic:

\[
\widetilde{\mathcal{L}} = \frac{1}{2}\sigma^2 \partial_{xx} + (r - \frac{1}{2}\sigma^2)\partial_x
\]

---

## American options and free boundaries


Free boundaries reduce regularity; viscosity solutions provide the right weak framework.

**Free boundary regularity.** For the American put, the optimal exercise boundary \(S^*(t)\) satisfies:
- \(S^* \in C^{0,1/2}\) (Lipschitz in \(\sqrt{T-t}\)) near maturity
- \(S^*\) is smooth away from maturity

**Greeks across the boundary.** At the exercise boundary:
- \(V\) is \(C^1\) (smooth pasting): \(\Delta\) is continuous
- \(V\) is generally not \(C^2\): \(\Gamma\) has a jump discontinuity
- The jump in \(\Gamma\) relates to the local time of \(S\) at the boundary

---

## Function space classification


| Domain | Price regularity | Greek regularity |
|:-------|:-----------------|:-----------------|
| \(t < T\), European | \(C^\infty\) in \((t,S)\) | All Greeks smooth |
| \(t = T\), kinked payoff | \(C^0\) only | \(\Delta\) discontinuous, \(\Gamma\) distributional |
| American, continuation region | \(C^\infty\) | All Greeks smooth |
| American, at exercise boundary | \(C^1\) | \(\Delta\) continuous, \(\Gamma\) may jump |

---

## What to remember


- Smoothness improves for \(t<T\) but deteriorates as \(t\uparrow T\).
- Interior regularity follows from Schauder estimates; \(V \in C^\infty\) for \(t < T\).
- Payoff kinks create large gamma near maturity: height \(\sim \tau^{-1/2}\), width \(\sim \sqrt{\tau}\).
- The Black–Scholes operator degenerates at \(S=0\); log-transform restores uniform ellipticity.
- Early exercise introduces weaker regularity and free boundary effects; \(\Gamma\) may be discontinuous.
