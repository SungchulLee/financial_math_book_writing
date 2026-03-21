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
