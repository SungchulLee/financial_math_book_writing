# Yield Curve Dynamics


Pricing interest-rate derivatives requires understanding not only today’s yield curve but also how the **entire curve evolves over time**. Yield curve dynamics are central to term-structure modeling.

---

## From static curves to dynamics


A static yield curve specifies \(P(0,T)\) or \(f(0,T)\).
A dynamic model specifies how these quantities evolve:

\[
T \mapsto P(t,T), \quad t>0.
\]



Short-rate models induce dynamics for the full curve through the evolution of \(r_t\).

---

## Curve dynamics under short-rate models


Given \(r_t\), bond prices evolve as

\[
P(t,T) = P(t,T,r_t).
\]



Consequences:
- the curve moves in a low-dimensional way,
- all maturities are driven by the same state variable(s),
- this limits flexibility but ensures consistency.

---

## Drift restrictions and no-arbitrage


No-arbitrage imposes strong constraints on curve dynamics:
- drifts of bond prices are determined by volatility,
- arbitrage-free evolution ties together different maturities.

These ideas are formalized in HJM theory.

---

## Implications for derivative pricing


Yield curve dynamics determine:
- swap and FRA pricing,
- cap/floor and swaption dynamics,
- hedging behavior across maturities.

Model choice affects which curve moves are possible.

---

## Key takeaways


- Yield curve dynamics are essential for IR derivative pricing.
- Short-rate models generate low-dimensional curve movements.
- No-arbitrage tightly constrains curve evolution.

---

## Further reading


- Heath, Jarrow & Morton (HJM).
- Filipovic, *Term-Structure Models*.

---

## Exercises

**Exercise 1.** In the Vasicek model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$, the bond price is $P(t, T) = e^{A(T-t) + B(T-t)\,r_t}$. Show that all bond prices are driven by the single state variable $r_t$, and explain why the yield curve can only undergo "parallel-like" shifts (up to the $B(\tau)$ weighting). What types of yield curve movements are impossible in this model?

---

**Exercise 2.** Starting from a flat yield curve $P(0, T) = e^{-r_0 T}$ with $r_0 = 5\%$, suppose the Vasicek parameters are $\kappa = 0.1$, $\theta = 5\%$, $\sigma = 1\%$. Compute $P(0, T)$ for $T = 1, 5, 10, 30$ years using the Vasicek formula. Plot the initial yield curve $y(0, T) = -\ln P(0, T)/T$ and discuss its shape.

---

**Exercise 3.** Explain the difference between a **static** yield curve $\{P(0, T)\}_{T \geq 0}$ and **dynamic** yield curve evolution $\{P(t, T)\}_{t \leq T}$. Why is the static curve insufficient for pricing interest rate derivatives such as caps and swaptions?

---

**Exercise 4.** In HJM theory, the drift of the instantaneous forward rate $f(t, T)$ under the risk-neutral measure is fully determined by the volatility function $\sigma_f(t, T)$. State the HJM drift condition without proof. Explain why this condition implies that specifying the yield curve dynamics is equivalent to specifying the volatility structure.

---

**Exercise 5.** Consider a two-factor short-rate model where $r_t = x_t + y_t + \varphi(t)$, with $x_t$ and $y_t$ independent OU processes with different mean-reversion speeds. Explain how this model generates richer yield curve dynamics than a one-factor model. What additional yield curve movements (beyond level shifts) become possible?

---

**Exercise 6.** Suppose the yield curve at time $t$ is described by a Nelson-Siegel parameterization:

$$
y(t, T) = \beta_0(t) + \beta_1(t)\frac{1 - e^{-\alpha(T-t)}}{\alpha(T-t)} + \beta_2(t)\left(\frac{1 - e^{-\alpha(T-t)}}{\alpha(T-t)} - e^{-\alpha(T-t)}\right)
$$

Identify $\beta_0$, $\beta_1$, $\beta_2$ as level, slope, and curvature factors. Discuss whether making $\beta_0(t)$, $\beta_1(t)$, $\beta_2(t)$ stochastic necessarily produces an arbitrage-free model.
