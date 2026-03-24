# Forward Rate Dynamics


The Heath–Jarrow–Morton (HJM) framework models the **entire forward rate curve** directly. Instead of specifying a short rate, HJM postulates dynamics for instantaneous forward rates.

---

## Instantaneous forward rates


Recall the instantaneous forward rate

\[
f(t,T) := -\partial_T \log P(t,T),
\]


so that

\[
P(t,T) = \exp\left(-\int_t^T f(t,u)\,du\right).
\]



In HJM, \(f(t,T)\) for all maturities \(T\ge t\) is the state variable.

---

## Stochastic dynamics


Under the risk-neutral measure, HJM postulates

\[
df(t,T) = \alpha(t,T)\,dt + \sum_{i=1}^n \sigma_i(t,T)\,dW_t^i,
\]


where:
- \(\sigma_i(t,T)\) are volatility functions,
- \(W^i\) are Brownian motions,
- \(\alpha(t,T)\) is the drift.

Crucially, the drift is *not arbitrary*.

---

## QuantPie Derivation: From Forward Rates to Bond Prices

### Forward Rate Definition

For $t < S < T$, the forward rate is defined as:

$$
P(t,T) = P(t,S) \cdot P(t,S,T) := P(t,S) \cdot e^{-R(t,S,T)(T-S)}
$$

where the forward rate is:

$$
R(t,S,T) = -\frac{\log P(t,T) - \log P(t,S)}{T-S}
$$

### Instantaneous Forward Rate

Taking the limit as $S \to T$:

$$
f(t,T) = \lim_{S \to T} R(t,S,T) = -\lim_{S \to T} \frac{\log P(t,T) - \log P(t,S)}{T-S} = -\frac{\partial}{\partial T}\log P(t,T)
$$

This shows the fundamental relationship between instantaneous forward rates and the log of bond prices.

### Forward Rate Dynamics

The instantaneous forward rate follows the stochastic differential equation:

$$
df(t,T) = \mu^{\mathbb{Q}}(t,T)dt + \sigma(t,T)dW^{\mathbb{Q}}(t)
$$

where:
- $\mu^{\mathbb{Q}}(t,T)$ is the drift under the risk-neutral measure
- $\sigma(t,T)$ is the volatility of the forward rate
- $dW^{\mathbb{Q}}(t)$ is a standard Brownian motion increment

---

## Interpretation


- Volatility structures determine how different maturities move together.
- The model is **infinite-dimensional** because \(T\) is continuous.
- Short-rate and market models arise as special cases.

---

## Advantages of forward modeling


- Exact fit to the initial yield curve by construction.
- Transparent no-arbitrage conditions.
- Direct modeling of curve dynamics.

---

## Key takeaways


- HJM models forward rates directly.
- The entire yield curve is the state variable.
- Drift restrictions ensure no-arbitrage.

---

## Further reading


- Heath, Jarrow & Morton (1992).
- Filipović, *Term-Structure Models*.

---

## Exercises

**Exercise 1.** Given the initial forward rate curve $f(0, T) = 0.04 + 0.005\,T - 0.0002\,T^2$ for $T \in [0, 30]$, compute the initial zero-coupon bond prices $P(0, 5)$, $P(0, 10)$, and $P(0, 20)$ using the relation

$$
P(0, T) = \exp\!\left(-\int_0^T f(0, u)\,du\right)
$$

Verify that $P(0, T)$ is a decreasing function of $T$.

---

**Exercise 2.** In the one-factor HJM framework with constant volatility $\sigma(t, T) = \sigma_0$, write down the explicit dynamics $df(t, T)$ under the risk-neutral measure (including the drift determined by the no-arbitrage condition). Integrate the SDE to obtain $f(t, T)$ as a function of $f(0, T)$, $\sigma_0$, and the Brownian motion. Identify the resulting short-rate model.

---

**Exercise 3.** Consider the forward rate volatility $\sigma(t, T) = \sigma_0\,e^{-\kappa(T-t)}$. Show that the short rate $r_t = f(t, t)$ satisfies a mean-reverting SDE and identify the mean-reversion speed $\kappa$. What well-known short-rate model does this volatility specification correspond to?

---

**Exercise 4.** Explain why the HJM framework is said to be "infinite-dimensional," whereas short-rate models like Vasicek or CIR are finite-dimensional. In practical terms, what does infinite-dimensionality mean for the computational complexity of Monte Carlo simulation in HJM?

---

**Exercise 5.** Starting from $P(t, T) = \exp\bigl(-\int_t^T f(t, u)\,du\bigr)$, verify that

$$
f(t, T) = -\frac{\partial}{\partial T}\log P(t, T)
$$

and that the short rate satisfies $r_t = f(t, t)$. If $P(t, T) = \exp(-a(T-t) - b(T-t)\,r_t)$ for some functions $a(\cdot)$ and $b(\cdot)$, express $f(t, T)$ in terms of $a'$, $b'$, and $r_t$.

---

**Exercise 6.** A two-factor HJM model has volatilities $\sigma_1(t, T) = 0.01$ and $\sigma_2(t, T) = 0.008\,e^{-0.3(T-t)}$. The first factor represents parallel shifts and the second represents slope changes. Compute the instantaneous variance of the forward rate $f(t, T)$ as a function of $T - t$ and sketch its term structure. At what time-to-maturity is the variance maximized?

---

**Exercise 7.** The forward rate $R(t, S, T)$ for the period $[S, T]$ is defined by $P(t, T) = P(t, S)\,e^{-R(t,S,T)(T-S)}$. Show that in the limit $S \to T$, $R(t, S, T)$ converges to the instantaneous forward rate $f(t, T)$. For finite $T - S$, express $R(t, S, T)$ as an average of instantaneous forward rates and discuss how a parallel shift in $f(t, \cdot)$ affects $R(t, S, T)$.
