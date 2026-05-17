# Sensitivities as Conditional Expectations


Many Greeks can be expressed as conditional expectations, clarifying their hedging interpretation and providing a bridge between probabilistic pricing theory and practical risk management.

---

## Discounted martingale


For a European payoff $H = \Phi(S_T)$ in a complete market under the risk-neutral measure $\mathbb{Q}$,

$$
\widetilde{V}_t
=
\mathbb{E}^{\mathbb{Q}}[e^{-r(T-t)}H \mid \mathcal{F}_t]
$$

is a $\mathbb{Q}$-martingale, where $\widetilde{V}_t = e^{-rt}V(t,S_t)$ is the discounted option value.

---

## Martingale representation and delta

Recall (see [§ Martingale Representation Theorem](../../ch04/martingale/martingale_representation_theorem.md)): in a complete one-Brownian market there is a unique predictable $Z_t$ with $\widetilde{V}_t = \widetilde{V}_0 + \int_0^t Z_s\,dW_s^{\mathbb{Q}}$.

In the Black–Scholes model, one can identify this integrand explicitly. Since $V(t,S_t)$ is a function of the Markov state $S_t$ and Itô's formula gives

$$
d\widetilde{V}_t = e^{-rt}\left(\frac{\partial V}{\partial S}\right)\sigma S_t\,dW_t^{\mathbb{Q}} + \text{(dt terms that vanish by the PDE)}
$$

we obtain

$$
\boxed{Z_t = e^{-rt}\sigma S_t\,\Delta(t, S_t)}
$$

---

## Interpretation


Delta is the predictable coefficient multiplying the tradable Brownian risk factor in a complete market. This is the precise mathematical foundation for the statement that "delta is the hedge ratio."

The self-financing replicating portfolio holds $\Delta(t, S_t)$ shares at time $t$. The stochastic integral $\int_0^t \Delta(s, S_s)\,dS_s$ tracks the gains from trading, and the martingale representation guarantees this replication is exact under continuous trading.

---

## Delta as a conditional expectation

**Recall** (see [§ Greeks via Feynman–Kac](greeks_via_feynman_kac.md) and [§ Pathwise Differentiation](pathwise_differentiation.md)): for a European call,

$$
\Delta(t, S_t) = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}\!\left[\frac{S_T}{S_t}\mathbf{1}_{S_T > K}\,\Big|\, S_t\right],
$$

which evaluates to $N(d_1)$ in the Black–Scholes model. This is the conditional-expectation form of the pathwise delta and is the bridge between probabilistic and PDE pricing of delta.

---

## Gamma as a conditional expectation


Gamma can also be expressed probabilistically. Differentiating delta once more:

$$
\Gamma = \frac{\partial \Delta}{\partial S} = \frac{\partial^2 V}{\partial S^2}
$$

Using the likelihood ratio method (see *Likelihood Ratio and Malliavin Methods*), gamma can be written without requiring payoff differentiability:

$$
\Gamma = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}\!\left[\Phi(S_T)\cdot w(S_T, S_t)\,\Big|\, S_t\right]
$$

where $w$ is a weight function derived from the score of the transition density. In Black–Scholes:

$$
\Gamma = \frac{e^{-r\tau}}{S_t^2 \sigma^2 \tau}\mathbb{E}^{\mathbb{Q}}\!\left[\Phi(S_T)\left(\frac{(\log(S_T/S_t) - \mu\tau)^2}{\sigma^2\tau} - 1\right)\,\Big|\, S_t\right]
$$

with $\mu = r - \sigma^2/2$.

---

## Vega and theta as expectations

**Vega** has the score-function representation $\nu = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T)\,\partial_\sigma\log p(S_T|S_t)\mid S_t]$ (see [§ Likelihood Ratio and Malliavin Methods](likelihood_ratio_malliavin_methods.md)).

**Theta** is not an independent expectation: from the PDE, $\Theta = rV - rS\Delta - \tfrac12\sigma^2 S^2\Gamma$ — the residual fixed by the other Greeks.

Recall (see [§ Greeks in the Black–Scholes Model](../greeks/greeks_in_black_scholes_model.md)): BS closed forms $\nu_{\text{call}}=S\sqrt{\tau}N'(d_1)$ and the call/put theta formulas.

---

## Incomplete markets


In incomplete markets (e.g., stochastic volatility without trading the variance), the martingale representation theorem still applies to the $\mathbb{Q}$-martingale $\widetilde{V}_t$, but now $W^{\mathbb{Q}}$ may be multi-dimensional:

$$
\widetilde{V}_t = \widetilde{V}_0 + \int_0^t Z_s^{(1)}\,dW_s^{(1)} + \int_0^t Z_s^{(2)}\,dW_s^{(2)}
$$

Only $Z^{(1)}$ (the component driven by the tradable asset) corresponds to a hedge ratio. The coefficient $Z^{(2)}$ represents **unhedgeable risk** — the portion of option value change that cannot be replicated by trading the underlying alone.

This means:

- Delta still gives the optimal hedge ratio for the tradable asset.
- Vega exposure (driven by $Z^{(2)}$) can only be hedged by trading other options or volatility instruments.
- Not every sensitivity corresponds to a tradable hedge in incomplete markets.

---

## Practical significance


The conditional expectation representation of Greeks has several practical applications:

**Monte Carlo Greeks.** Computing Greeks via their expectation representations is the foundation of Monte Carlo Greek estimation. Pathwise derivatives and likelihood ratio methods provide unbiased estimators that can be computed alongside option price simulation.

**Model-free hedging arguments.** The martingale representation shows that delta hedging is optimal (in a mean-square sense) regardless of the specific dynamics, as long as the market is complete and the model is correct.

**Intuition for hedging.** The representation $Z_t = e^{-rt}\sigma S_t \Delta$ shows that the hedge ratio is the sensitivity of the discounted claim to the fundamental source of randomness, scaled by the asset's own exposure to that randomness.

---

## What to remember


- Delta arises as the predictable integrand in the martingale representation of the discounted option price.
- In complete markets, this gives a rigorous foundation for "delta is the hedge ratio."
- Greeks can be expressed as conditional expectations, enabling Monte Carlo computation and extending to complex models.
- In incomplete markets, not every sensitivity corresponds to a tradable hedge --- only the components aligned with traded risk factors.

---

## Exercises

**Exercise 1.** Starting from the martingale representation $\widetilde{V}_t = \widetilde{V}_0 + \int_0^t Z_s \, \mathrm{d}W_s^{\mathbb{Q}}$, verify that $Z_t = e^{-rt}\sigma S_t \Delta(t, S_t)$ by applying Ito's formula to $\widetilde{V}_t = e^{-rt}V(t, S_t)$ and using the Black--Scholes PDE to cancel the $\mathrm{d}t$ terms.

??? success "Solution to Exercise 1"
    Apply Ito's formula to $\widetilde{V}_t = e^{-rt}V(t, S_t)$ where $V(t, S)$ satisfies the Black--Scholes PDE and $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$:

    $$
    d\widetilde{V}_t = -r e^{-rt}V\,dt + e^{-rt}\left(\frac{\partial V}{\partial t}\,dt + \frac{\partial V}{\partial S}\,dS_t + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}(dS_t)^2\right)
    $$

    Substituting $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$ and $(dS_t)^2 = \sigma^2 S_t^2\,dt$:

    $$
    d\widetilde{V}_t = e^{-rt}\!\left(-rV + \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2}\right)dt + e^{-rt}\sigma S_t \frac{\partial V}{\partial S}\,dW_t^{\mathbb{Q}}
    $$

    The Black--Scholes PDE states $\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = rV$. Therefore the $dt$ coefficient vanishes:

    $$
    d\widetilde{V}_t = e^{-rt}\sigma S_t \frac{\partial V}{\partial S}(t,S_t)\,dW_t^{\mathbb{Q}} = e^{-rt}\sigma S_t \Delta(t,S_t)\,dW_t^{\mathbb{Q}}
    $$

    Comparing with $d\widetilde{V}_t = Z_t\,dW_t^{\mathbb{Q}}$, we identify $Z_t = e^{-rt}\sigma S_t \Delta(t, S_t)$.

---

**Exercise 2.** The delta of a European call can be written as $\Delta = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[(S_T/S_t)\mathbf{1}_{S_T > K} \mid S_t]$. Evaluate this expectation explicitly under the log-normal distribution to recover $\Delta = N(d_1)$.

??? success "Solution to Exercise 2"
    Write $S_T = S_t \exp\!\left((r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z\right)$ with $Z \sim \mathcal{N}(0,1)$ and $\tau = T - t$. The condition $S_T > K$ is equivalent to $Z > -d_2$ where

    $$
    d_2 = \frac{\ln(S_t/K) + (r - \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}
    $$

    Then:

    $$
    \Delta = e^{-r\tau}\mathbb{E}\!\left[\frac{S_T}{S_t}\mathbf{1}_{Z > -d_2}\right] = e^{-r\tau}\int_{-d_2}^{\infty} e^{(r-\frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}z}\,\frac{e^{-z^2/2}}{\sqrt{2\pi}}\,dz
    $$

    Combine the exponents:

    $$
    (r - \tfrac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}z - \tfrac{1}{2}z^2 = r\tau - \tfrac{1}{2}(z - \sigma\sqrt{\tau})^2
    $$

    Substituting $u = z - \sigma\sqrt{\tau}$ (so $z = u + \sigma\sqrt{\tau}$ and the lower limit becomes $-d_2 - \sigma\sqrt{\tau} = -d_1$):

    $$
    \Delta = e^{-r\tau} \cdot e^{r\tau} \int_{-d_1}^{\infty} \frac{e^{-u^2/2}}{\sqrt{2\pi}}\,du = \int_{-d_1}^{\infty} \frac{e^{-u^2/2}}{\sqrt{2\pi}}\,du = N(d_1)
    $$

---

**Exercise 3.** In the gamma formula $\Gamma = \frac{e^{-r\tau}}{S_t^2 \sigma^2 \tau}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T)((\log(S_T/S_t) - \mu\tau)^2/(\sigma^2\tau) - 1) \mid S_t]$ with $\mu = r - \sigma^2/2$, explain why this expression does not require $\Phi$ to be differentiable. What class of payoffs can this formula handle that pathwise gamma cannot?

??? success "Solution to Exercise 3"
    The gamma formula

    $$
    \Gamma = \frac{e^{-r\tau}}{S_t^2\sigma^2\tau}\mathbb{E}^{\mathbb{Q}}\!\left[\Phi(S_T)\!\left(\frac{(\log(S_T/S_t) - \mu\tau)^2}{\sigma^2\tau} - 1\right)\,\Big|\, S_t\right]
    $$

    does not require $\Phi$ to be differentiable because it is a **likelihood ratio** (score function) representation. The derivatives have been transferred from the payoff to the transition density via the identity:

    $$
    \frac{\partial^2}{\partial S^2}\int \Phi(y)p(y|S)\,dy = \int \Phi(y)\frac{\partial^2}{\partial S^2}p(y|S)\,dy
    $$

    The weight function $w(S_T, S_t) = \frac{1}{S_t^2\sigma^2\tau}\!\left(\frac{(\log(S_T/S_t)-\mu\tau)^2}{\sigma^2\tau} - 1\right)$ comes from the second derivative of $\log p(S_T|S_t)$ with respect to $S_t$, and involves only the transition density --- not the payoff.

    This formula can handle payoffs that pathwise gamma cannot:

    - **Vanilla calls/puts**: $\Phi(x) = (x-K)^+$ has $\Phi'' = \delta(x-K)$, so pathwise gamma fails
    - **Digital options**: $\Phi(x) = \mathbf{1}_{x>K}$ is discontinuous, so even pathwise delta fails
    - **Piecewise constant payoffs**: Barrier-type payoffs with discontinuities
    - **Any $L^2$ payoff**: The formula requires only that $\mathbb{E}[\Phi(S_T)^2 \cdot w^2] < \infty$, not smoothness of $\Phi$

---

**Exercise 4.** Theta is determined by other Greeks via the Black--Scholes PDE: $\Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma$. Explain why theta does not have an independent conditional expectation representation. Is this a limitation or a simplification?

??? success "Solution to Exercise 4"
    Theta is determined by the Black--Scholes PDE:

    $$
    \Theta = rV - rS\Delta - \frac{1}{2}\sigma^2 S^2 \Gamma
    $$

    This means theta is **not an independent quantity** --- it is completely determined by the current option price $V$, delta $\Delta$, and gamma $\Gamma$. There is no need for a separate conditional expectation representation because:

    1. **The PDE is a constraint.** The Black--Scholes PDE $\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2\Gamma = rV$ holds at every point $(t, S)$. This is an algebraic identity between the Greeks, not a statistical relationship.

    2. **Time is deterministic.** Unlike $S$, which is stochastic, time is a deterministic parameter. The risk-neutral expectation representation is designed for sensitivities with respect to random quantities or parameters affecting the distribution. Time sensitivity is already captured by how the conditional expectation $V(t,S) = \mathbb{E}^{t,S}[e^{-r\tau}\Phi(S_T)]$ changes as the conditioning time $t$ advances.

    This is a **simplification**, not a limitation. It means:

    - Theta can be computed for free once delta, gamma, and the price are known
    - No additional Monte Carlo estimation or expectation evaluation is needed
    - The PDE provides a useful consistency check: if independently computed Greeks do not satisfy $\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2\Gamma = rV$, there is a numerical error

---

**Exercise 5.** In a two-factor stochastic volatility model, the martingale representation has two integrands: $Z^{(1)}$ (tradable) and $Z^{(2)}$ (untradable). If $Z^{(2)}$ represents volatility risk, explain why delta hedging alone cannot eliminate vega exposure. What instruments would be needed to hedge the $Z^{(2)}$ component?

??? success "Solution to Exercise 5"
    In a two-factor stochastic volatility model, the discounted option price has the representation

    $$
    d\widetilde{V}_t = Z_t^{(1)}\,dW_t^{(1)} + Z_t^{(2)}\,dW_t^{(2)}
    $$

    where $W^{(1)}$ drives the stock price and $W^{(2)}$ drives the volatility. Delta hedging means holding $\Delta = Z_t^{(1)} / (\sigma_S S_t e^{-rt})$ shares of the stock, which replicates only the $dW^{(1)}$ component.

    **Why delta hedging cannot eliminate vega exposure:**

    The P&L of a delta-hedged portfolio over $[t, t+dt]$ is

    $$
    d\widetilde{V}_t - \Delta\,d\widetilde{S}_t = Z_t^{(2)}\,dW_t^{(2)}
    $$

    The stock $S$ has zero loading on $W^{(2)}$ (or at most a correlated component), so no position in $S$ alone can offset the $Z_t^{(2)}\,dW_t^{(2)}$ term. This residual is precisely the **vega risk** --- the option's exposure to volatility shocks.

    **Instruments needed to hedge $Z^{(2)}$:**

    To hedge the volatility-driven component, one needs instruments with nonzero exposure to $W^{(2)}$:

    - **Other options** (e.g., a vanilla option with different strike or maturity) whose price loads on $W^{(2)}$
    - **Variance swaps** or **volatility swaps** that are directly exposed to realized or implied volatility
    - **VIX futures/options** in equity markets
    - **Straddles/strangles** that have large vega exposure

    With one such additional instrument, the two-dimensional risk $(W^{(1)}, W^{(2)})$ can be fully hedged, restoring market completeness in the expanded tradable universe.

---

**Exercise 6.** The statement "delta is the hedge ratio" relies on the completeness of the market. In an incomplete market (e.g., with jumps), the martingale representation may involve a jump martingale term. Discuss how the hedging interpretation of delta changes when the market is incomplete, and whether delta hedging is still useful despite not being perfect.

??? success "Solution to Exercise 6"
    In an incomplete market (e.g., one with jumps), the martingale representation takes the form

    $$
    d\widetilde{V}_t = Z_t\,dW_t^{\mathbb{Q}} + \int_{\mathbb{R}} U_t(x)\,\widetilde{N}(dt, dx)
    $$

    where $\widetilde{N}$ is a compensated jump measure. The jump term $\int U_t(x)\,\widetilde{N}(dt,dx)$ cannot be replicated by continuous trading in the stock alone.

    **How the hedging interpretation changes:**

    - Delta ($\partial V / \partial S$) still describes the instantaneous sensitivity of the option to the stock price, and it still determines the optimal hedge ratio for the diffusive component.
    - However, delta hedging only eliminates the **continuous (diffusive) risk**. The **jump risk** remains unhedged: if the stock jumps by $\Delta S$, the option value changes by approximately $\Delta \cdot \Delta S + \frac{1}{2}\Gamma (\Delta S)^2 + \text{higher-order terms}$, but the actual change is $V(S + \Delta S) - V(S)$, which can differ significantly from the linear approximation for large jumps.
    - The hedge is no longer perfect: there is a **hedging residual** whose variance depends on the jump intensity and size distribution.

    **Delta hedging is still useful despite imperfection:**

    - It eliminates the dominant source of risk (small continuous moves) and reduces overall portfolio variance substantially.
    - It is the **minimum-variance hedge** in the mean-square sense among strategies trading only the stock.
    - In practice, jumps are rare events, so the delta hedge works well most of the time.
    - The residual jump risk can be partially managed by holding a portfolio of options with different strikes (to match the jump exposure across different stock price levels) or by using instruments that are sensitive to jump risk (e.g., deep OTM options).
    - Quantitative risk management treats the unhedged jump component as a tail risk, addressed through position limits, stress testing, and capital reserves rather than continuous hedging.
