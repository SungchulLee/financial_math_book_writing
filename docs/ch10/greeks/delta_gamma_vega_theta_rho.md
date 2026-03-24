# Delta, Gamma, Vega, Theta, Rho


Let an option price be written as a function


\[
V = V(t,S;\sigma,r,\dots)
\]



where \(t\in[0,T]\) is time, \(S>0\) is the underlying price, \(\sigma>0\) is volatility, and \(r\in\mathbb{R}\) is the short rate (constant in Black–Scholes).

The **Greeks** are partial derivatives of the pricing map \(V\) with respect to state variables and model parameters. They quantify first- and second-order sensitivities and form the basis of risk measurement and hedging, independently of any particular pricing model.


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
\boxed{\Theta(t,S) := \frac{\partial V}{\partial t}(t,S)}
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
+\frac{1}{2}\Gamma\,(\delta S)^2
\]



This is the conceptual basis for “Greek-based” risk decomposition and hedging heuristics.

---

## What to remember


- Greeks are derivatives of a pricing map \(V(t,S;\theta)\) with respect to state and parameters.
- Gamma is the curvature term that dominates short-time hedging error.
- Theta conventions vary; define yours explicitly.
- In the next section, these abstract definitions are specialized to the
**Black–Scholes model**, where the Greeks can be computed explicitly in
closed form.

---

## Exercises

**Exercise 1.** A European call option has price $V = 12.50$, with $\Delta = 0.62$, $\Gamma = 0.035$, and $\nu = 18.5$. If the underlying moves from $S = 100$ to $S = 103$ while volatility increases from $\sigma = 0.20$ to $\sigma = 0.22$, estimate the new option price using the second-order Taylor expansion.

---

**Exercise 2.** Explain why gamma is the same for a European call and a European put with the same strike and maturity, while delta and rho differ. Use put-call parity to justify your answer.

---

**Exercise 3.** Consider a portfolio consisting of $n_1$ calls and $n_2$ puts on the same underlying, all with the same strike and maturity. Write the portfolio Greeks $\Delta_\pi$, $\Gamma_\pi$, $\nu_\pi$, $\Theta_\pi$, $\rho_\pi$ in terms of $n_1$, $n_2$, and the individual option Greeks. Under what conditions is the portfolio delta-neutral?

---

**Exercise 4.** Show that the second-order Taylor expansion for the option price can be written in vector-matrix form as

$$
\delta V \approx \mathbf{g}^T \delta \mathbf{x} + \frac{1}{2} \delta \mathbf{x}^T \mathbf{H} \, \delta \mathbf{x}
$$

where $\mathbf{g}$ is the gradient vector of first-order Greeks and $\mathbf{H}$ is the Hessian of second-order Greeks. Identify the entries of $\mathbf{g}$ and $\mathbf{H}$ for variables $(S, \sigma, r)$.

---

**Exercise 5.** Why does theta have ambiguous sign conventions in the literature? If one defines $\Theta_1 = \partial V / \partial t$ and $\Theta_2 = -\partial V / \partial t$, explain which is negative for a long call position and why. How does the convention affect the P&L decomposition formula?

---

**Exercise 6.** Suppose a trader holds a delta-neutral portfolio with $\Gamma = 0.04$ and $\nu = 15$. She observes a simultaneous move $\delta S = +2$ and $\delta \sigma = -0.01$. Compute the approximate change in portfolio value. Which effect dominates, and under what conditions would the other dominate instead?

