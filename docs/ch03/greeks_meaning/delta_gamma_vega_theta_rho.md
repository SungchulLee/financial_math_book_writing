# Delta, Gamma, Vega, Theta, Rho

Let an option price be written as a function


\[
V = V(t,S;\sigma,r,\dots),
\]



where \(t\in[0,T]\) is time, \(S>0\) is the underlying price, \(\sigma>0\) is volatility, and \(r\in\mathbb{R}\) is the short rate (constant in Black–Scholes).

The **Greeks** are partial derivatives of \(V\) with respect to model inputs.

---

## Delta


\[
\boxed{\Delta(t,S) := \frac{\partial V}{\partial S}(t,S)}
\]



Delta measures first-order sensitivity of the option value to small changes in \(S\).

---

## Gamma


\[
\boxed{\Gamma(t,S) := \frac{\partial^2 V}{\partial S^2}(t,S)}
\]



Gamma measures convexity with respect to \(S\). It controls second-order error in delta hedging and is central for hedging error asymptotics.

---

## Vega


\[
\boxed{\nu(t,S) := \frac{\partial V}{\partial \sigma}(t,S)}
\]



Vega measures sensitivity to volatility. In Black–Scholes, \(\nu\) is typically largest near-the-money and for moderate maturities.

---

## Theta

There are multiple sign conventions. Here we define **calendar-time theta**


\[
\boxed{\Theta(t,S) := \frac{\partial V}{\partial t}(t,S).}
\]



Since many PDEs are written backward in time, some texts define \(-\partial_t V\) as theta. Be explicit about convention whenever using theta in P\&L decompositions.

---

## Rho


\[
\boxed{\rho(t,S) := \frac{\partial V}{\partial r}(t,S)}
\]



Rho measures sensitivity to changes in interest rates.

---

## A second-order Taylor expansion viewpoint

For a small perturbation \((\delta S,\delta\sigma,\delta r)\) (ignoring cross-terms for clarity),


\[
V(t,S+\delta S;\sigma+\delta\sigma,r+\delta r)
\approx
V(t,S;\sigma,r)
+\Delta\,\delta S
+\nu\,\delta\sigma
+\rho\,\delta r
+\frac{1}{2}\Gamma\,(\delta S)^2.
\]



This is the conceptual basis for “Greek-based” risk decomposition and hedging heuristics.

---

## What to remember

- Greeks are derivatives of a pricing map \(V(t,S;\theta)\) with respect to state and parameters.
- Gamma is the curvature term that dominates short-time hedging error.
- Theta conventions vary; define yours explicitly.
