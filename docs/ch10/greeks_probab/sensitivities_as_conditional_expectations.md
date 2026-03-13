# Sensitivities as Conditional Expectations


Many Greeks can be expressed as conditional expectations, clarifying their hedging interpretation and providing a bridge between probabilistic pricing theory and practical risk management.

---

## Discounted martingale


For a European payoff \(H = \Phi(S_T)\) in a complete market under the risk-neutral measure \(\mathbb{Q}\),

\[
\widetilde{V}_t
=
\mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}H \mid \mathcal{F}_t]
\]

is a \(\mathbb{Q}\)-martingale, where \(\widetilde{V}_t = e^{-rt}V(t,S_t)\) is the discounted option value.

---

## Martingale representation and delta


By the martingale representation theorem (applicable in complete markets driven by a single Brownian motion), there exists a unique predictable process \(Z_t\) such that

\[
\widetilde{V}_t = \widetilde{V}_0 + \int_0^t Z_s\,\mathrm{d}W_s^{\mathbb{Q}}
\]

In the Black–Scholes model, one can identify this integrand explicitly. Since \(V(t,S_t)\) is a function of the Markov state \(S_t\) and Itô's formula gives

\[
d\widetilde{V}_t = e^{-rt}\left(\frac{\partial V}{\partial S}\right)\sigma S_t\,dW_t^{\mathbb{Q}} + \text{(dt terms that vanish by the PDE)}
\]

we obtain

\[
\boxed{Z_t = e^{-rt}\sigma S_t\,\Delta(t, S_t)}
\]

---

## Interpretation


Delta is the predictable coefficient multiplying the tradable Brownian risk factor in a complete market. This is the precise mathematical foundation for the statement that "delta is the hedge ratio."

The self-financing replicating portfolio holds \(\Delta(t, S_t)\) shares at time \(t\). The stochastic integral \(\int_0^t \Delta(s, S_s)\,dS_s\) tracks the gains from trading, and the martingale representation guarantees this replication is exact under continuous trading.

---

## Delta as a conditional expectation


In the risk-neutral framework, delta can itself be written as a conditional expectation. For a European call with payoff \(\Phi(S_T) = (S_T - K)^+\):

\[
\Delta(t, S_t) = \frac{\partial}{\partial S}\mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}(S_T - K)^+ \mid S_t = S]
\]

Under regularity conditions allowing interchange of differentiation and expectation (see *Pathwise Differentiation*):

\[
\Delta(t, S_t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}\!\left[\frac{\partial S_T}{\partial S_t}\mathbf{1}_{S_T > K}\,\Big|\, S_t\right]
\]

In Black–Scholes, \(\frac{\partial S_T}{\partial S_t} = \frac{S_T}{S_t}\) (by log-linearity), so

\[
\Delta = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}\!\left[\frac{S_T}{S_t}\mathbf{1}_{S_T > K}\,\Big|\, S_t\right]
\]

which evaluates to \(N(d_1)\) — the Black–Scholes call delta.

---

## Gamma as a conditional expectation


Gamma can also be expressed probabilistically. Differentiating delta once more:

\[
\Gamma = \frac{\partial \Delta}{\partial S} = \frac{\partial^2 V}{\partial S^2}
\]

Using the likelihood ratio method (see *Likelihood Ratio and Malliavin Methods*), gamma can be written without requiring payoff differentiability:

\[
\Gamma = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}\!\left[\Phi(S_T)\cdot w(S_T, S_t)\,\Big|\, S_t\right]
\]

where \(w\) is a weight function derived from the score of the transition density. In Black–Scholes:

\[
\Gamma = \frac{e^{-r\tau}}{S_t^2 \sigma^2 \tau}\mathbb{E}^{\mathbb{Q}}\!\left[\Phi(S_T)\left(\frac{(\log(S_T/S_t) - \mu\tau)^2}{\sigma^2\tau} - 1\right)\,\Big|\, S_t\right]
\]

with \(\mu = r - \sigma^2/2\).

---

## Vega and theta as expectations


Similarly:

**Vega.** Using the chain rule through the transition density:

\[
\nu = \frac{\partial V}{\partial \sigma} = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}\!\left[\Phi(S_T)\cdot\frac{\partial \log p(S_T|S_t)}{\partial \sigma}\,\Big|\,S_t\right]
\]

In Black–Scholes, this simplifies to \(\nu = S\sqrt{\tau}\,N'(d_1)\).

**Theta.** From the Black–Scholes PDE:

\[
\Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma
\]

So theta is determined by the other Greeks and does not require a separate conditional expectation representation — it is the "residual" needed for the PDE to hold.

---

## Incomplete markets


In incomplete markets (e.g., stochastic volatility without trading the variance), the martingale representation theorem still applies to the \(\mathbb{Q}\)-martingale \(\widetilde{V}_t\), but now \(W^{\mathbb{Q}}\) may be multi-dimensional:

\[
\widetilde{V}_t = \widetilde{V}_0 + \int_0^t Z_s^{(1)}\,dW_s^{(1)} + \int_0^t Z_s^{(2)}\,dW_s^{(2)}
\]

Only \(Z^{(1)}\) (the component driven by the tradable asset) corresponds to a hedge ratio. The coefficient \(Z^{(2)}\) represents **unhedgeable risk** — the portion of option value change that cannot be replicated by trading the underlying alone.

This means:

- Delta still gives the optimal hedge ratio for the tradable asset.
- Vega exposure (driven by \(Z^{(2)}\)) can only be hedged by trading other options or volatility instruments.
- Not every sensitivity corresponds to a tradable hedge in incomplete markets.

---

## Practical significance


The conditional expectation representation of Greeks has several practical applications:

**Monte Carlo Greeks.** Computing Greeks via their expectation representations is the foundation of Monte Carlo Greek estimation. Pathwise derivatives and likelihood ratio methods provide unbiased estimators that can be computed alongside option price simulation.

**Model-free hedging arguments.** The martingale representation shows that delta hedging is optimal (in a mean-square sense) regardless of the specific dynamics, as long as the market is complete and the model is correct.

**Intuition for hedging.** The representation \(Z_t = e^{-rt}\sigma S_t \Delta\) shows that the hedge ratio is the sensitivity of the discounted claim to the fundamental source of randomness, scaled by the asset's own exposure to that randomness.

---

## What to remember


- Delta arises as the predictable integrand in the martingale representation of the discounted option price.
- In complete markets, this gives a rigorous foundation for "delta is the hedge ratio."
- Greeks can be expressed as conditional expectations, enabling Monte Carlo computation and extending to complex models.
- In incomplete markets, not every sensitivity corresponds to a tradable hedge — only the components aligned with traded risk factors.
