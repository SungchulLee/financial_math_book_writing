# Fourier Pricing Methods


Fourier methods convert option pricing into numerical integration problems using characteristic functions. They are widely used for stochastic volatility models because they are fast and accurate for repeated evaluations during calibration.

---

## Basic idea


Let \(X_T = \log S_T\). Many models provide \(\varphi(u) = \mathbb{E}[e^{iuX_T}]\).
Option prices can be expressed via Fourier inversion of:
- the density of \(X_T\),
- or transforms of the payoff function.

---

## Fourier inversion for densities


If \(f_{X_T}(x)\) is the density of \(X_T\), then

\[
f_{X_T}(x) = \frac{1}{2\pi}\int_{\mathbb{R}} e^{-iux}\varphi(u)\,du.
\]



In principle, one could compute prices by integrating payoff \(g(e^x)\) against this density, but direct density inversion can be numerically delicate.

---

## Carr–Madan approach (damped payoff)


A common practical method dampens the call payoff to ensure integrability:

\[
C(K) = e^{-rT}\,\mathbb{E}[(S_T-K)^+].
\]



Define \(k=\log K\). The Carr–Madan method prices calls using a Fourier transform of a damped call price:
- introduce damping factor \(\alpha>0\),
- compute the transform analytically in terms of \(\varphi\),
- invert numerically using FFT.

This yields fast pricing across many strikes in one run.

---

## Numerical integration choices


Common quadrature/inversion methods:
- standard quadrature (Gauss–Legendre, Simpson),
- FFT-based grid inversion,
- fractional FFT (more flexible strike grids).

Key numerical parameters:
- truncation range for integration,
- grid spacing,
- damping parameters.

---

## Practical stability considerations


- ensure the integrand decays sufficiently (choose \(\alpha\) appropriately),
- control oscillatory integrals (step size and truncation),
- validate against known benchmarks (e.g., Black–Scholes limit).

For calibration, consistent numerical settings across maturities matter to avoid optimizer artifacts.

---

## Key takeaways


- Fourier pricing uses characteristic functions to compute option prices efficiently.
- Carr–Madan and FFT methods are standard for stochastic volatility calibration.
- Numerical stability requires careful control of truncation, damping, and grids.

---

## Further reading


- Carr & Madan (1999), FFT pricing.
- Lee (2004), moment formulas and tail behavior.
- Lord & Kahl, Heston calibration and numerical refinements.
