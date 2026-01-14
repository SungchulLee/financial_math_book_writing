# Pathwise Differentiation


Pathwise differentiation computes Greeks by differentiating sample paths with respect to parameters or initial data.

---

## Delta (Black–Scholes)


Since \(\partial S_T/\partial S = S_T/S\),

\[
\Delta(t,S)=\mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\frac{S_T}{S}\right]
\]


for smooth \(\Phi\).

---

## Vega (Black–Scholes)


Differentiate \(S_T\) with respect to \(\sigma\):

\[
\frac{\partial S_T}{\partial \sigma}
=
S_T\left(Z-\sigma\tau\right),
\qquad Z=W_T-W_t.
\]


Thus, for smooth \(\Phi\),

\[
\boxed{
\nu(t,S)=
\mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\,S_T\left(Z-\sigma\tau\right)\right].
}
\]



---

## Limitation


If \(\Phi\) has kinks, \(\Phi'\) is discontinuous and pathwise differentiation can fail at the kink. Likelihood ratio methods avoid this by moving derivatives to the density.

---

## What to remember


- Pathwise methods are natural for smooth payoffs.
- For kinked payoffs, likelihood ratio/Malliavin weights are often preferable.
