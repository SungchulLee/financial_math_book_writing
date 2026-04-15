# Practitioner Perspective

Every derivatives desk operates in the gap between theory and reality.
The risk-neutral formula $V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-rT}X_T]$ assumes
continuous trading, zero frictions, and known parameters---none of which hold.
This section examines the compensating mechanisms that practitioners have
built around the theoretical framework: calibration, model risk management,
the gamma P&L decomposition, and the implied volatility surface.

!!! abstract "Guiding principle"
    Practitioners do not trust models---they use them to **structure risk and
    monitor deviations**. The goal is not to find the "correct" model but to
    choose one that prices liquid instruments consistently, produces stable
    hedge ratios, and makes model risk transparent.

!!! note "Scope"
    This section treats the pricing framework as an applied tool. It
    assumes familiarity with the core material in
    [Physical vs Risk-Neutral World](physical_vs_risk_neutral.md) and
    [Pricing vs Hedging](pricing_vs_hedging.md). For the conditions
    under which the framework fails entirely, see
    [When Measure Change Fails](when_measure_change_fails.md).

---

## Calibration vs Estimation

Pricing models are fitted to market prices, not to history. A desk that
estimates volatility from past returns and plugs it into the Black-Scholes
formula will misprice every liquid option on the screen---and create apparent
arbitrage against its own book.

!!! abstract "Core idea"
    Pricing parameters come from calibration to market prices ($\mathbb{Q}$),
    not from statistical estimation on historical data ($\mathbb{P}$).

### The Two Approaches

| | Estimation | Calibration |
|---|---|---|
| **Measure** | $\mathbb{P}$ | $\mathbb{Q}$ |
| **Data source** | Historical time series | Current option prices |
| **Method** | MLE, GMM, Bayesian | Least squares on prices |
| **Output** | Physical dynamics | Risk-neutral dynamics |
| **Used for** | Risk management, VaR | Derivative pricing |

### Why Calibration Dominates

Three reasons make calibration the standard for pricing:

1. **Market consistency.** A model that disagrees with observable option
   prices would create arbitrage against the desk's own book.
2. **Information content.** Implied volatilities encode the market's
   collective assessment of jump risk, stochastic volatility, and tail
   events that historical data may underrepresent.
3. **Drift irrelevance.** Derivative prices under $\mathbb{Q}$ depend on
   $r$ and $\sigma$ but not on $\mu$. Estimating the physical drift is
   unnecessary for pricing.

!!! note "Calibration does not determine the physical measure"
    A model calibrated to $\mathbb{Q}$ cannot be used for risk management
    tasks (VaR, expected shortfall) that require $\mathbb{P}$-measure
    forecasts.

### The Calibration Problem

Given a model with parameter vector $\boldsymbol{\alpha}$ and $N$ liquid
instruments with market prices $C_1^{\mathrm{mkt}}, \ldots, C_N^{\mathrm{mkt}}$,
calibration solves

$$
\hat{\boldsymbol{\alpha}} = \arg\min_{\boldsymbol{\alpha}} \sum_{i=1}^{N} w_i\!\left(C_i^{\mathrm{model}}(\boldsymbol{\alpha}) - C_i^{\mathrm{mkt}}\right)^2
$$

where $w_i$ are weights (often inversely proportional to bid-ask spreads) and
each model price is computed via risk-neutral valuation:

$$
C_i^{\mathrm{model}}(\boldsymbol{\alpha}) = \mathbb{E}^{\mathbb{Q}_{\boldsymbol{\alpha}}}\!\left[e^{-\int_0^{T_i} r_s\,ds}\,\Phi_i(S_{T_i})\right]
$$

!!! warning "Non-uniqueness of calibration"
    In incomplete markets, different parameter vectors may fit market prices
    equally well yet produce different exotic prices. This is a manifestation
    of measure non-uniqueness; see
    [When Measure Change Fails](when_measure_change_fails.md).

---

## Model Risk

When two models calibrate perfectly to the same vanilla surface yet disagree
on the price of an exotic, the difference is model risk. It is not a bug---it
is an unavoidable consequence of market incompleteness.

!!! abstract "Core idea"
    Different models calibrated to the same data select different risk-neutral
    measures and can disagree on exotic prices.

### Sources

Model risk arises at three layers:

1. **Specification risk.** The choice of dynamics (Black-Scholes vs Heston
   vs local volatility) determines the set of available risk-neutral measures.
2. **Calibration risk.** Within a given model, different calibration sets or
   objective functions lead to different parameter estimates.
3. **Extrapolation risk.** Exotic prices require extrapolation beyond the
   liquid calibration instruments.

### Quantification

A natural measure of model risk is the pricing interval:

$$
\text{Model risk} = \sup_{\mathcal{M}} V^{\mathcal{M}}(\Phi) - \inf_{\mathcal{M}} V^{\mathcal{M}}(\Phi)
$$

where the supremum and infimum range over all models $\mathcal{M}$ that
calibrate to the same liquid instruments.

??? example "Model risk in barrier option pricing"
    A down-and-out call calibrated to the same vanilla surface under three
    models:

    | Model | Barrier option price | Difference from BS |
    |---|---|---|
    | Black-Scholes (flat vol) | \$4.82 | baseline |
    | Local volatility (Dupire) | \$5.41 | +12% |
    | Stochastic volatility (Heston) | \$5.18 | +7% |

    Barrier options depend on the **joint distribution of path and terminal
    value**, which vanilla prices (marginal distributions) do not uniquely
    determine.

---

## Hedging in Practice: The Gamma P&L

Perfect replication is a theoretical limit. In practice, discrete rebalancing
and uncertain volatility produce a residual P&L that is driven entirely by
gamma exposure.

!!! abstract "Core idea"
    Discrete hedging generates P&L proportional to gamma times the gap between
    realized and implied variance.

### Discrete Hedging Error

Between rebalance times $t_k$ and $t_{k+1}$, the P&L of a delta-hedged
position is approximately

$$
\text{P\&L}_{k} \approx \frac{1}{2}\Gamma_{t_k}\,S_{t_k}^2\left[(\Delta W_k)^2 - \sigma^2\Delta t\right]
$$

where $\Gamma_{t_k} = \partial^2 V / \partial S^2$ and
$\Delta W_k = W_{t_{k+1}} - W_{t_k}$. Three consequences follow immediately:

1. **P&L scales with gamma.** Near-the-money, near-expiry positions have the
   largest hedging errors.
2. **Realized vs implied variance drives the sign.** The term
   $(\Delta W_k)^2 - \sigma^2\Delta t$ compares actual squared moves to the
   model's prediction.
3. **The expectation is zero only when the model is correct.** Under
   $\mathbb{P}$, the expected P&L per step vanishes only if $\sigma$ equals
   realized volatility.

### Aggregate Gamma P&L

Summing over the option's life:

$$
\text{Total P\&L} \approx \frac{1}{2}\sum_{k=0}^{N-1}\Gamma_{t_k}\,S_{t_k}^2\left(\sigma_{\mathrm{realized},k}^2 - \sigma_{\mathrm{implied}}^2\right)\Delta t
$$

Long gamma profits when realized volatility exceeds implied; short gamma
profits in the opposite regime.

!!! tip "The trader's rule of thumb"
    "Buy options when you think realized vol will exceed implied; sell when
    you think the opposite." This connects the $\mathbb{P}$-measure forecast
    of future volatility to the $\mathbb{Q}$-measure implied volatility.

---

## Transaction Costs and Hedging Frequency

Transaction costs create a tradeoff: more frequent rebalancing reduces hedging
error but increases trading costs. For proportional costs at rate $\kappa$
per dollar traded:

$$
\text{Transaction costs} \sim \kappa\,\sigma\,S_0\,\sqrt{\frac{T}{\Delta t}}
$$

$$
\text{Hedging error} \sim \Gamma\,\sigma^2\,S_0^2\,\sqrt{\Delta t}
$$

The total cost is minimized at an optimal $\Delta t$ that depends on
$\kappa$, $\sigma$, and $\Gamma$. Common strategies include:

- **Time-based rebalancing**: hedge at fixed intervals (e.g., daily).
- **Threshold-based rebalancing**: hedge when the delta deviation exceeds a
  tolerance band.
- **Utility-based hedging**: minimize expected utility loss inclusive of
  transaction costs.

---

## The Implied Volatility Surface

The Black-Scholes model predicts a flat implied volatility surface. Markets
produce a rich two-dimensional surface $\sigma_{\mathrm{imp}}(K, T)$ that
varies with both strike and maturity---and this surface *is* the market's
risk-neutral distribution.

!!! abstract "Core idea"
    The implied volatility surface encodes all risk-neutral marginal
    distributions via the Breeden-Litzenberger formula.

### Empirical Features

- **Volatility skew**: out-of-the-money puts carry higher implied volatility,
  reflecting crash risk and leverage effects.
- **Term structure**: short-dated implied volatility spikes during stress and
  compresses in calm markets.
- **Surface dynamics**: the surface moves stochastically, and no single
  parametric model captures its full dynamics.

### Breeden-Litzenberger Formula

Each maturity slice of the surface defines a risk-neutral density:

$$
\frac{\partial^2 C}{\partial K^2}\bigg|_{K=k} = e^{-rT}\,q(k, T)
$$

where $q(k, T)$ is the risk-neutral density of $S_T$ at level $k$.
Calibrating a model to the surface is equivalent to fitting its risk-neutral
marginal distributions to those implied by the market.

---

## Calibration in Practice: Local Volatility

The **Dupire local volatility model** uses a state-dependent volatility
$\sigma_{\mathrm{loc}}(S, t)$ chosen to reproduce all vanilla prices exactly:

$$
dS_t = rS_t\,dt + \sigma_{\mathrm{loc}}(S_t, t)\,S_t\,dW_t^{\mathbb{Q}}
$$

Dupire's formula extracts $\sigma_{\mathrm{loc}}$ directly from the surface:

$$
\sigma_{\mathrm{loc}}^2(K, T) = \frac{\frac{\partial C}{\partial T} + rK\frac{\partial C}{\partial K}}{\frac{1}{2}K^2\frac{\partial^2 C}{\partial K^2}}
$$

Local volatility provides a complete model (unique $\mathbb{Q}$) that fits
all vanillas. However, its forward volatility dynamics are unrealistic,
leading to poor performance for path-dependent and forward-starting options.

---

## Theory vs Practice: Summary

| Theoretical Assumption | Practical Reality |
|---|---|
| Continuous trading | Discrete rebalancing |
| Zero transaction costs | Bid-ask spreads, commissions, market impact |
| Known volatility $\sigma$ | Stochastic, estimated or implied |
| Unique risk-neutral measure | Multiple models, multiple calibrations |
| Complete markets | Most markets are incomplete |
| Infinite liquidity | Limited depth, especially in stress |

Despite these gaps, the framework provides a consistent pricing language,
a starting point for hedging, and a benchmark against which model risk can
be measured.

!!! tip "Trader translation"
    - Price with implied vol ($\mathbb{Q}$).
    - Make money with realized vol ($\mathbb{P}$).

!!! quote "A practitioner's view"
    "All models are wrong, but some are useful." --- George E. P. Box

    The risk-neutral framework is not a description of reality. It is a tool
    that translates derivative valuation into a tractable mathematical
    structure whose value lies in the discipline and consistency it brings
    to pricing and risk management.

---

## Exercises

**Exercise 1.**
A stock has physical drift $\mu = 0.15$, volatility $\sigma = 0.25$, and risk-free rate $r = 0.04$. A desk calibrates Black-Scholes to at-the-money options and obtains $\sigma_{\mathrm{imp}} = 0.22$. Explain why the calibrated volatility differs from the physical volatility. Which should be used for pricing a European call under $\mathbb{Q}$?

??? success "Solution to Exercise 1"
    The physical volatility $\sigma = 0.25$ is estimated from historical returns under $\mathbb{P}$. The implied volatility $\sigma_{\mathrm{imp}} = 0.22$ is extracted from option prices and reflects the risk-neutral distribution under $\mathbb{Q}$.

    They differ because:

    1. **Different measures.** Physical volatility is a $\mathbb{P}$-quantity; implied volatility is a $\mathbb{Q}$-quantity. In models richer than Black-Scholes (stochastic volatility, jumps), implied volatility is a nonlinear transformation of the risk-neutral dynamics and need not equal physical volatility.

    2. **Variance risk premium.** Empirically, implied volatility tends to exceed realized volatility on average. The observation $\sigma_{\mathrm{imp}} < \sigma$ here is atypical but can occur in specific market conditions.

    For pricing under $\mathbb{Q}$, the desk should use $\sigma_{\mathrm{imp}} = 0.22$. Using $\sigma = 0.25$ would produce a price inconsistent with the market, creating apparent arbitrage against the desk's book.

---

**Exercise 2.**
Suppose two parameter vectors $\boldsymbol{\alpha}_1$ and $\boldsymbol{\alpha}_2$ both achieve the global minimum of the calibration objective for vanilla options. Explain why an exotic barrier option may still have different prices under $\boldsymbol{\alpha}_1$ and $\boldsymbol{\alpha}_2$, and relate this to market incompleteness.

??? success "Solution to Exercise 2"
    Both parameter vectors fit vanillas perfectly. However, vanilla prices determine only the **marginal distributions** of $S_T$ at each maturity (via Breeden-Litzenberger). They do not determine the path dynamics.

    A barrier option's payoff depends on whether $S_t$ hits the barrier during the option's life---a path-dependent event governed by the **joint distribution** of $(S_t)_{0 \leq t \leq T}$, not just the terminal marginal. Two parameter vectors can produce identical marginals but different path dynamics (different local volatility surfaces, different spot-vol correlations, different jump structures).

    This is market incompleteness: vanilla options do not span all contingent claims. Each $\boldsymbol{\alpha}_j$ implicitly selects a different risk-neutral measure from the family consistent with the vanilla surface, and these measures can disagree on path-dependent claims.

---

**Exercise 3.**
A delta-hedged short call has $\Gamma = 0.04$, $S = 100$, $\Delta t = 1/252$, $(\Delta W)^2 = 0.006$, and $\sigma^2 \Delta t = 0.0004$. Compute the gamma P&L and determine the sign for the short call holder.

??? success "Solution to Exercise 3"
    Applying the gamma P&L formula:

    $$
    \text{P\&L} \approx \frac{1}{2}\Gamma\,S^2\left[(\Delta W)^2 - \sigma^2 \Delta t\right]
    $$

    Substituting:

    $$
    \text{P\&L} \approx \frac{1}{2} \times 0.04 \times 10{,}000 \times (0.006 - 0.0004) = 200 \times 0.0056 = 1.12
    $$

    This gives $+\$1.12$ for a **long gamma** position. The short call has **negative gamma**, so the short call holder's P&L is $-\$1.12$. The position lost money because realized volatility far exceeded implied---the standard result for short gamma positions.

---

**Exercise 4.**
Transaction costs scale as $\kappa\,\sigma\,S_0\,\sqrt{T/\Delta t}$ and hedging error scales as $\Gamma\,\sigma^2\,S_0^2\,\sqrt{\Delta t}$. Minimize the total cost with respect to $\Delta t$ to derive the optimal rebalancing interval.

??? success "Solution to Exercise 4"
    The total cost is

    $$
    C(\Delta t) = \kappa\,\sigma\,S_0\,\sqrt{\frac{T}{\Delta t}} + \Gamma\,\sigma^2\,S_0^2\,\sqrt{\Delta t}
    $$

    Taking the derivative and setting it to zero:

    $$
    \frac{dC}{d(\Delta t)} = -\frac{1}{2}\kappa\,\sigma\,S_0\,\sqrt{T}\,(\Delta t)^{-3/2} + \frac{1}{2}\Gamma\,\sigma^2\,S_0^2\,(\Delta t)^{-1/2} = 0
    $$

    Multiplying both sides by $2(\Delta t)^{3/2}$:

    $$
    \Gamma\,\sigma^2\,S_0^2\,\Delta t = \kappa\,\sigma\,S_0\,\sqrt{T}
    $$

    $$
    \Delta t^* = \frac{\kappa\,\sqrt{T}}{\Gamma\,\sigma\,S_0}
    $$

    The optimal interval increases with $\kappa$ (trade less when costs are high) and decreases with $\Gamma$, $\sigma$, and $S_0$ (trade more when hedging error is large).

---

**Exercise 5.**
Using the Breeden-Litzenberger formula, explain why a symmetric implied volatility smile implies zero skewness in the risk-neutral distribution. What does the typical equity skew (higher implied vol for low strikes) say about the risk-neutral density?

??? success "Solution to Exercise 5"
    The Breeden-Litzenberger formula

    $$
    q(k, T) = e^{rT}\frac{\partial^2 C}{\partial K^2}\bigg|_{K=k}
    $$

    extracts the risk-neutral density from the call price surface. Given a smooth implied volatility surface $\sigma_{\mathrm{imp}}(K, T)$, the call price $C(K,T) = \mathrm{BS}(S_0, K, T, r, \sigma_{\mathrm{imp}}(K,T))$ is twice differentiable in $K$, and $q(k,T)$ can be computed via the chain rule.

    If the smile is symmetric around the at-the-money strike ($\sigma_{\mathrm{imp}}(K_0 + \delta) = \sigma_{\mathrm{imp}}(K_0 - \delta)$ for all $\delta$), the resulting density $q(k,T)$ is symmetric, giving **zero skewness**.

    In equity markets the smile is asymmetric: out-of-the-money puts (low $K$) carry higher implied vol than out-of-the-money calls (high $K$). This produces a risk-neutral density with a fatter left tail---**negative skewness**---reflecting crash risk priced by the market.

---

**Exercise 6.**
Suppose call prices are given by Black-Scholes with constant implied volatility $\sigma_0$. Show that Dupire's formula reduces to $\sigma_{\mathrm{loc}}(K, T) = \sigma_0$ for all $K$ and $T$.

??? success "Solution to Exercise 6"
    Under constant $\sigma_0$ the Black-Scholes call price is $C = S_0 N(d_1) - Ke^{-rT}N(d_2)$ with standard $d_1, d_2$. The required partial derivatives are:

    $$
    \frac{\partial C}{\partial T} = S_0\,n(d_1)\frac{\sigma_0}{2\sqrt{T}} + rKe^{-rT}N(d_2)
    $$

    $$
    \frac{\partial C}{\partial K} = -e^{-rT}N(d_2)
    $$

    $$
    \frac{\partial^2 C}{\partial K^2} = e^{-rT}\frac{n(d_2)}{K\sigma_0\sqrt{T}}
    $$

    **Numerator** of Dupire's formula:

    $$
    \frac{\partial C}{\partial T} + rK\frac{\partial C}{\partial K} = S_0\,n(d_1)\frac{\sigma_0}{2\sqrt{T}} + rKe^{-rT}N(d_2) - rKe^{-rT}N(d_2) = S_0\,n(d_1)\frac{\sigma_0}{2\sqrt{T}}
    $$

    Using the Black-Scholes identity $S_0\,n(d_1) = Ke^{-rT}n(d_2)$, the numerator becomes $Ke^{-rT}n(d_2)\frac{\sigma_0}{2\sqrt{T}}$.

    **Denominator:**

    $$
    \frac{1}{2}K^2 \cdot e^{-rT}\frac{n(d_2)}{K\sigma_0\sqrt{T}} = \frac{Ke^{-rT}n(d_2)}{2\sigma_0\sqrt{T}}
    $$

    Dividing:

    $$
    \sigma_{\mathrm{loc}}^2 = \frac{Ke^{-rT}n(d_2)\frac{\sigma_0}{2\sqrt{T}}}{\frac{Ke^{-rT}n(d_2)}{2\sigma_0\sqrt{T}}} = \sigma_0^2
    $$

    Therefore $\sigma_{\mathrm{loc}}(K,T) = \sigma_0$ for all $K, T$. A flat implied volatility surface produces a flat local volatility surface, confirming that Black-Scholes is the constant-local-volatility special case.
