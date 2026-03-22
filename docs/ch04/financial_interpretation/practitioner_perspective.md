# Practitioner Perspective


The mathematical framework of measure change, Girsanov's theorem, and
risk-neutral pricing provides a logically complete theory. In practice,
however, traders and risk managers face a fundamental gap: the theory assumes
continuous trading, perfect liquidity, known model parameters, and frictionless
markets, while reality offers none of these. This section examines how
practitioners actually use risk-neutral pricing, where the theory breaks down,
and what compensating mechanisms have evolved to bridge the gap.

Understanding the practitioner perspective is essential for any quantitative
finance student, because the mathematical framework is a **tool**, not an
end in itself. Its value lies in the practical decisions it informs.

---

## Calibration vs Estimation

### The Two Approaches

Practitioners face a fundamental choice when specifying model dynamics: they
can **estimate** parameters from historical data (the $\mathbb{P}$-measure
approach) or **calibrate** parameters to current market prices (the
$\mathbb{Q}$-measure approach). These are mathematically distinct operations.

| | Estimation | Calibration |
|---|---|---|
| **Measure** | $\mathbb{P}$ | $\mathbb{Q}$ |
| **Data source** | Historical time series | Current option prices |
| **Method** | MLE, GMM, Bayesian | Least squares on prices |
| **Output** | Physical dynamics | Risk-neutral dynamics |
| **Used for** | Risk management, VaR | Derivative pricing |

### Why Calibration Dominates in Practice

For derivative pricing, calibration to market prices is strongly preferred
over historical estimation. The reasons are both practical and theoretical:

1. **Consistency with liquid markets.** A pricing model that disagrees with
   observable option prices would create arbitrage against the desk's own
   book.
2. **Risk-neutral parameters absorb information.** Implied volatilities
   encode the market's collective assessment of future uncertainty, including
   jump risk, stochastic volatility, and tail events that historical data
   may underrepresent.
3. **The physical drift is irrelevant.** As established in the
   [Risk Premium Decomposition](risk_premium_decomposition.md), derivative
   prices under $\mathbb{Q}$ depend on $r$ and $\sigma$ but not on $\mu$.
   Estimating $\mu$ from historical data is unnecessary for pricing.

!!! note "Calibration does not determine the physical measure"
    Calibrating to option prices determines the risk-neutral dynamics but
    says nothing about the physical dynamics. A model calibrated to
    $\mathbb{Q}$ cannot be used directly for risk management tasks (VaR,
    expected shortfall) that require $\mathbb{P}$-measure forecasts. See
    [Physical vs Risk-Neutral World](physical_vs_risk_neutral_world.md)
    for the distinction.

### The Calibration Problem

Formally, given a model with parameter vector $\boldsymbol{\alpha}$ and
a set of $N$ liquid instruments with market prices $C_1^{\mathrm{mkt}}, \ldots, C_N^{\mathrm{mkt}}$,
calibration solves

$$
\hat{\boldsymbol{\alpha}} = \arg\min_{\boldsymbol{\alpha}} \sum_{i=1}^{N} w_i\!\left(C_i^{\mathrm{model}}(\boldsymbol{\alpha}) - C_i^{\mathrm{mkt}}\right)^2
$$

where $w_i$ are weights (often inversely proportional to bid-ask spreads) and
$C_i^{\mathrm{model}}(\boldsymbol{\alpha})$ is the model price of instrument
$i$ computed via risk-neutral valuation:

$$
C_i^{\mathrm{model}}(\boldsymbol{\alpha}) = \mathbb{E}^{\mathbb{Q}_{\boldsymbol{\alpha}}}\!\left[e^{-\int_0^{T_i} r_s\,ds}\,\Phi_i(S_{T_i})\right]
$$

!!! warning "Non-uniqueness of calibration"
    In incomplete markets, the calibration problem may have multiple
    solutions---different parameter vectors that fit market prices equally
    well but produce different prices for exotic derivatives. This is a
    manifestation of measure non-uniqueness discussed in
    [When Measure Change Fails](when_measure_change_fails.md).

---

## Model Risk

### What Is Model Risk

**Model risk** is the risk of financial loss arising from using an incorrect
or inadequately specified model. In the context of measure change, model risk
has a precise interpretation: different models, or different calibrations of
the same model, select different risk-neutral measures from the family of
measures consistent with no-arbitrage.

### Sources of Model Risk

Model risk in derivative pricing arises from three layers:

1. **Model specification risk.** The choice of dynamics (e.g., Black-Scholes
   vs Heston vs local volatility) affects the set of available risk-neutral
   measures.
2. **Calibration risk.** Even within a given model, different calibration
   sets (which strikes, which maturities) or different objective functions
   can lead to different parameter estimates.
3. **Extrapolation risk.** Models are calibrated to liquid instruments
   (typically vanilla options with standard strikes and maturities). Exotic
   derivative prices require extrapolation beyond the calibration set.

### Quantifying Model Risk

One practical approach quantifies model risk as the spread across models:

$$
\text{Model risk} = \sup_{\mathcal{M}} V^{\mathcal{M}}(\Phi) - \inf_{\mathcal{M}} V^{\mathcal{M}}(\Phi)
$$

where the supremum and infimum range over all models $\mathcal{M}$ that
calibrate to the same set of liquid instruments. This is the **pricing
interval** induced by calibration constraints, analogous to the no-arbitrage
bounds in incomplete markets.

??? example "Model risk in barrier option pricing"
    Consider a down-and-out call option with barrier $B < S_0$ and strike $K$.
    Three models calibrated to the same vanilla option surface can produce
    significantly different barrier option prices:

    | Model | Barrier option price | Difference from BS |
    |---|---|---|
    | Black-Scholes (flat vol) | \$4.82 | baseline |
    | Local volatility (Dupire) | \$5.41 | +12% |
    | Stochastic volatility (Heston) | \$5.18 | +7% |

    The differences arise because barrier options depend on the **joint
    distribution of the path and terminal value**, which is not uniquely
    determined by marginal distributions (vanilla prices). Each model makes
    different assumptions about the dynamics along the path, leading to
    different prices for path-dependent claims.

---

## Hedging in Practice vs Theory

### The Theoretical Ideal

In the Black-Scholes framework, perfect hedging requires:

- **Continuous rebalancing** of the delta hedge $\Delta_t = \partial V / \partial S$.
- **Zero transaction costs** for each trade.
- **Known and constant volatility** $\sigma$.
- **Unlimited liquidity** at the mid-price.

Under these conditions, the hedging portfolio replicates the derivative payoff
exactly, and the P&L from the hedged position is identically zero.

### The Reality of Discrete Hedging

In practice, traders rebalance at discrete intervals $\Delta t$. The
**hedging error** from discrete rebalancing has a well-known decomposition.

Consider a delta-hedged short position in a European option. Between rebalance
times $t_k$ and $t_{k+1}$, the P&L from the hedged position is approximately

$$
\text{P\&L}_{k} \approx \frac{1}{2}\Gamma_{t_k}\,S_{t_k}^2\left[(\Delta W_k)^2 - \sigma^2\Delta t\right]
$$

where $\Gamma_{t_k} = \partial^2 V / \partial S^2$ is the gamma and
$\Delta W_k = W_{t_{k+1}} - W_{t_k}$.

This expression reveals several important facts:

1. **The P&L is proportional to gamma.** Positions with high gamma (near
   the money, near expiry) have the largest hedging errors.
2. **The P&L depends on realized vs implied volatility.** The term
   $(\Delta W_k)^2 - \sigma^2\Delta t$ compares the squared Brownian
   increment (realized variance over the interval) to the model's expected
   variance $\sigma^2\Delta t$.
3. **The expectation under $\mathbb{P}$ is not zero.** Under the physical
   measure, $\mathbb{E}^{\mathbb{P}}[(\Delta W_k)^2] = \Delta t$, so the
   expected P&L per step is zero only if $\sigma$ in the model equals the
   realized volatility.

### The Aggregate P&L Decomposition

Over the life of the option, summing the per-period P&L gives

$$
\text{Total P\&L} \approx \frac{1}{2}\sum_{k=0}^{N-1}\Gamma_{t_k}\,S_{t_k}^2\left(\sigma_{\mathrm{realized},k}^2 - \sigma_{\mathrm{implied}}^2\right)\Delta t
$$

This is the **gamma P&L** formula, which shows that:

- If realized volatility exceeds implied volatility, a long gamma position
  profits and a short gamma position loses.
- The converse holds if realized volatility is below implied.

!!! tip "The trader's rule of thumb"
    "Buy options when you think realized vol will exceed implied; sell
    when you think the opposite." This rule is a direct consequence of
    the gamma P&L decomposition and connects the $\mathbb{P}$-measure
    forecast of future volatility to the $\mathbb{Q}$-measure implied
    volatility embedded in option prices.

---

## Transaction Costs and Hedging Frequency

### The Hedging Tradeoff

Transaction costs create a fundamental tradeoff: more frequent rebalancing
reduces hedging error but increases trading costs. The optimal rebalancing
frequency balances these two effects.

For proportional transaction costs at rate $\kappa$ per dollar traded, the
total cost of delta hedging scales as

$$
\text{Transaction costs} \sim \kappa\,\sigma\,S_0\,\sqrt{\frac{T}{\Delta t}}
$$

The hedging error from discrete rebalancing scales as

$$
\text{Hedging error} \sim \Gamma\,\sigma^2\,S_0^2\,\sqrt{\Delta t}
$$

The total cost (hedging error plus transaction costs) is minimized at an
optimal rebalancing interval that depends on $\kappa$, $\sigma$, and $\Gamma$.

### Practical Hedging Strategies

Practitioners use several approaches to manage the hedging tradeoff:

- **Time-based rebalancing**: Hedge at fixed intervals (e.g., daily).
  Simple but ignores market conditions.
- **Threshold-based rebalancing**: Hedge when the delta deviation exceeds
  a tolerance band. More efficient but requires continuous monitoring.
- **Utility-based hedging**: Minimize expected utility loss accounting for
  transaction costs. Theoretically optimal but computationally expensive.

---

## The Implied Volatility Surface

### From Theory to Market Reality

The Black-Scholes model assumes constant volatility, predicting a flat implied
volatility surface. In reality, implied volatility varies systematically with
both strike and maturity, forming a surface $\sigma_{\mathrm{imp}}(K, T)$.

Key features of the empirical surface include:

- **Volatility skew** (or smile): For equity options, out-of-the-money puts
  have higher implied volatility than at-the-money options, reflecting
  crash risk and leverage effects.
- **Term structure**: Short-dated options often have higher implied
  volatility than long-dated options during stress periods, and vice versa
  in calm markets.
- **Surface dynamics**: The surface moves stochastically over time, and
  its dynamics are not captured by any single parametric model.

### What the Surface Tells the Practitioner

The implied volatility surface is the market's representation of the
risk-neutral measure $\mathbb{Q}$. Each point on the surface encodes a
marginal distribution:

$$
\frac{\partial^2 C}{\partial K^2}\bigg|_{K=k} = e^{-rT}\,q(k, T)
$$

where $q(k, T)$ is the risk-neutral density of $S_T$ at level $k$. This
is the **Breeden-Litzenberger formula**: the second derivative of call prices
with respect to strike recovers the risk-neutral probability density.

The implied volatility surface thus summarizes the entire risk-neutral
distribution at each maturity. Calibrating a model to the surface is
equivalent to fitting the model's risk-neutral marginal distributions to
those implied by the market.

---

## Calibration in Practice

### The Workflow

A typical calibration workflow for an equity derivatives desk:

1. **Collect data.** Gather mid-prices (or implied volatilities) for liquid
   vanilla options across strikes and maturities.
2. **Choose a model.** Select a model class (e.g., local volatility,
   stochastic volatility, or a combination).
3. **Solve the calibration problem.** Minimize the distance between model
   prices and market prices by adjusting model parameters.
4. **Validate.** Check that the calibrated model reproduces liquid prices
   within bid-ask spreads and produces sensible prices for exotics.
5. **Re-calibrate.** Repeat daily (or intraday) as market conditions
   change.

### Local Volatility

The **Dupire local volatility model** uses a state-dependent volatility
function $\sigma_{\mathrm{loc}}(S, t)$ chosen so that the model exactly
reproduces all vanilla option prices:

$$
dS_t = rS_t\,dt + \sigma_{\mathrm{loc}}(S_t, t)\,S_t\,dW_t^{\mathbb{Q}}
$$

Dupire's formula determines $\sigma_{\mathrm{loc}}$ directly from the
implied volatility surface:

$$
\sigma_{\mathrm{loc}}^2(K, T) = \frac{\frac{\partial C}{\partial T} + rK\frac{\partial C}{\partial K}}{\frac{1}{2}K^2\frac{\partial^2 C}{\partial K^2}}
$$

Local volatility provides a **complete** model (unique risk-neutral measure)
that fits all vanilla prices. However, its dynamics for forward volatility
are unrealistic, leading to poor performance for path-dependent and forward-
starting options.

---

## The Gap Between Theory and Practice

The following table summarizes the key differences between the theoretical
framework and practical implementation:

| Theoretical Assumption | Practical Reality |
|---|---|
| Continuous trading | Discrete rebalancing (daily or less) |
| Zero transaction costs | Bid-ask spreads, commissions, market impact |
| Known volatility $\sigma$ | Volatility is stochastic and must be estimated or implied |
| Single risk-neutral measure | Multiple models, multiple calibrations |
| Complete markets | Most markets are incomplete |
| Infinite liquidity | Limited depth, especially in stress |
| No model risk | Model choice affects prices and hedges |

Despite these gaps, the theoretical framework remains indispensable because
it provides:

- A **consistent pricing language** across instruments and desks.
- A **starting point** for hedging that can be adjusted for frictions.
- A **benchmark** against which model risk can be measured.
- A **conceptual framework** for understanding what drives derivative prices.

!!! quote "A practitioner's view"
    "All models are wrong, but some are useful." --- George E. P. Box

    The risk-neutral pricing framework is not a description of reality. It is a
    tool that translates the complex problem of derivative valuation into a
    tractable mathematical structure. Its value lies not in its literal truth
    but in the discipline and consistency it brings to pricing and risk
    management.

---

## Summary

Practitioners use the measure-change framework as a **pricing tool**, not as a
literal description of how markets work:

- **Calibration**, not estimation, determines the risk-neutral measure from
  current market prices.
- **Model risk** arises because calibration does not uniquely determine
  prices for exotic derivatives.
- **Hedging** in practice involves discrete rebalancing, transaction costs,
  and uncertain volatility, producing P&L that the theory predicts should
  be zero.
- The **implied volatility surface** encodes the market's risk-neutral
  distributions and serves as the central input for calibration.

The gap between theory and practice is bridged by judgment, experience, and
a clear understanding of what the mathematical framework can and cannot
guarantee. For the mathematical foundations, see
[Pricing vs Hedging](pricing_vs_hedging.md) and
[Physical vs Risk-Neutral World](physical_vs_risk_neutral_world.md). For the
conditions under which the framework breaks down entirely, see
[When Measure Change Fails](when_measure_change_fails.md).
