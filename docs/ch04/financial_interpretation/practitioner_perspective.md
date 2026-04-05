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

!!! abstract "Guiding principle"
    Practitioners do not trust models---they use them to **structure risk and
    monitor deviations**. The goal is not to find the "correct" model but to
    choose one that prices liquid instruments consistently, produces stable
    hedge ratios, and makes model risk transparent and manageable.

---

## Calibration vs Estimation

!!! abstract "Core idea"
    Pricing models are fitted to market prices ($\mathbb{Q}$), not historical
    data ($\mathbb{P}$).

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

!!! abstract "Core idea"
    Different models calibrated to the same market data select different
    risk-neutral measures---and can disagree on exotic prices.

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

!!! abstract "Core idea"
    Perfect hedging is a theoretical limit. In practice, discrete rebalancing
    and uncertain volatility generate P&L driven by the gamma exposure.

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

This decomposition shows:

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

!!! abstract "Core idea"
    The volatility surface *is* the market's risk-neutral distribution.

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
risk-neutral measure $\mathbb{Q}$. Each slice of the surface *defines* a
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

The key differences between theory and practice:

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

!!! tip "Trader translation"
    - Price with implied vol ($\mathbb{Q}$).
    - Make money with realized vol ($\mathbb{P}$).

!!! quote "A practitioner's view"
    "All models are wrong, but some are useful." --- George E. P. Box

    Models are not used because they are true---they are used because they are
    **consistent**. The risk-neutral pricing framework is not a description of
    reality. It is a tool that translates the complex problem of derivative
    valuation into a tractable mathematical structure. Its value lies not in its
    literal truth but in the discipline and consistency it brings to pricing and
    risk management.

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

---

## Exercises

**Exercise 1.**
A stock has physical drift $\mu = 0.15$, volatility $\sigma = 0.25$, and the risk-free rate is $r = 0.04$. A desk calibrates a Black-Scholes model to at-the-money implied volatility and obtains $\sigma_{\mathrm{imp}} = 0.22$. Explain why the calibrated volatility differs from the physical volatility, and state which volatility should be used for pricing a European call option under $\mathbb{Q}$.

??? success "Solution to Exercise 1"
    The physical volatility $\sigma = 0.25$ is estimated from historical returns under $\mathbb{P}$ and describes how the stock actually moves over time. The implied volatility $\sigma_{\mathrm{imp}} = 0.22$ is extracted from option market prices and reflects the risk-neutral distribution under $\mathbb{Q}$.

    These differ for several reasons:

    1. **Different measures:** Physical volatility is a $\mathbb{P}$-measure quantity, while implied volatility is a $\mathbb{Q}$-measure quantity. Although Girsanov's theorem preserves the diffusion coefficient (volatility is invariant under measure change for a geometric Brownian motion), the Black-Scholes implied volatility is not literally the diffusion coefficient---it is the constant $\sigma$ that, when plugged into the Black-Scholes formula, reproduces the market price. In more realistic models (stochastic volatility, jumps), the implied volatility surface is a nonlinear transformation of the risk-neutral dynamics and need not equal the physical volatility.

    2. **Variance risk premium:** Empirically, implied volatility tends to exceed realized volatility on average (the "variance risk premium"), meaning option sellers are compensated for bearing volatility risk. The observation that $\sigma_{\mathrm{imp}} = 0.22 < \sigma = 0.25$ here is atypical but can occur in specific market conditions.

    For pricing a European call under $\mathbb{Q}$, the practitioner should use the **implied volatility** $\sigma_{\mathrm{imp}} = 0.22$, because this is the market-consistent $\mathbb{Q}$-measure input. Using the physical volatility $\sigma = 0.25$ would produce a price inconsistent with the market, creating an apparent arbitrage against the desk's own book.

---

**Exercise 2.**
Given the calibration objective

$$
\hat{\boldsymbol{\alpha}} = \arg\min_{\boldsymbol{\alpha}} \sum_{i=1}^{N} w_i\!\left(C_i^{\mathrm{model}}(\boldsymbol{\alpha}) - C_i^{\mathrm{mkt}}\right)^2
$$

suppose two different parameter vectors $\boldsymbol{\alpha}_1$ and $\boldsymbol{\alpha}_2$ both achieve the global minimum of the objective for a set of vanilla options. Explain why the prices of an exotic barrier option may still differ under $\boldsymbol{\alpha}_1$ and $\boldsymbol{\alpha}_2$, and relate this to the concept of market incompleteness.

??? success "Solution to Exercise 2"
    Both $\boldsymbol{\alpha}_1$ and $\boldsymbol{\alpha}_2$ achieve the global minimum of the calibration objective for vanilla options, so they fit the same set of vanilla prices perfectly (or equally well). However, vanilla option prices determine only the **marginal distributions** of $S_T$ at each maturity $T$ (via the Breeden-Litzenberger formula). They do not uniquely determine the **dynamics** of $S_t$ along the path.

    A barrier option's payoff depends on whether the stock price hits the barrier $B$ at any time during the life of the option. This is a path-dependent event that depends on the **joint distribution** of $(S_t)_{0 \leq t \leq T}$, not just on the terminal distribution $S_T$. Two different parameter vectors $\boldsymbol{\alpha}_1$ and $\boldsymbol{\alpha}_2$ can produce the same marginal distributions at each maturity but different path dynamics (e.g., different local volatility surfaces, different correlation structures between spot and volatility, different jump intensities along the path).

    This is directly related to market incompleteness: vanilla options alone do not span all contingent claims. The exotic barrier option lies outside the span of the calibration instruments, so its price is not uniquely determined by no-arbitrage and the vanilla surface. Each parameter vector $\boldsymbol{\alpha}_j$ implicitly selects a different risk-neutral measure from the family of measures consistent with the vanilla prices, and these measures can disagree on the value of path-dependent claims.

---

**Exercise 3.**
A delta-hedged short call position has gamma $\Gamma = 0.04$ and current stock price $S = 100$. Over one day ($\Delta t = 1/252$), the realized stock return produces $(\Delta W)^2 = 0.006$ while the model predicts $\sigma^2 \Delta t = 0.0004$. Compute the approximate P&L from the gamma P&L formula

$$
\text{P\&L} \approx \frac{1}{2}\Gamma\,S^2\left[(\Delta W)^2 - \sigma^2 \Delta t\right]
$$

and determine whether the position gained or lost money.

??? success "Solution to Exercise 3"
    Applying the gamma P&L formula:

    $$
    \text{P\&L} \approx \frac{1}{2}\Gamma\,S^2\left[(\Delta W)^2 - \sigma^2 \Delta t\right]
    $$

    Substituting the given values:

    $$
    \text{P\&L} \approx \frac{1}{2} \times 0.04 \times 100^2 \times (0.006 - 0.0004)
    $$

    $$
    = \frac{1}{2} \times 0.04 \times 10{,}000 \times 0.0056
    $$

    $$
    = 0.5 \times 0.04 \times 10{,}000 \times 0.0056 = 1.12
    $$

    The P&L is approximately $+\$1.12$.

    The formula computes the gamma P&L of the **hedged book** (option plus delta hedge). The positive sign means the combined position gained \$1.12 over this interval. However, the sign must be interpreted carefully relative to the option position:

    - The **short call** has negative gamma ($-\Gamma < 0$). When realized volatility greatly exceeds implied volatility, a short gamma position **loses** money: large moves hurt the short option holder.
    - The **delta hedge** partially offsets this, but the net gamma P&L of $+\$1.12$ here reflects the perspective of a **long gamma** hedger (the formula uses $\Gamma > 0$, corresponding to a long option position).

    For the **short call** holder, the gamma P&L has the opposite sign: $-\$1.12$. The position **lost** money because realized volatility far exceeded implied volatility. This is the standard result: short gamma positions lose when markets move more than the model predicts.

---

**Exercise 4.**
Transaction costs at rate $\kappa$ per dollar traded produce a total hedging cost that scales as $\kappa\,\sigma\,S_0\,\sqrt{T / \Delta t}$, while the hedging error scales as $\Gamma\,\sigma^2\,S_0^2\,\sqrt{\Delta t}$. By minimizing the sum of these two costs with respect to $\Delta t$, derive an expression for the optimal rebalancing interval in terms of $\kappa$, $\sigma$, $\Gamma$, and $S_0$.

??? success "Solution to Exercise 4"
    The total cost to minimize is

    $$
    C(\Delta t) = \underbrace{\kappa\,\sigma\,S_0\,\sqrt{\frac{T}{\Delta t}}}_{\text{transaction costs}} + \underbrace{\Gamma\,\sigma^2\,S_0^2\,\sqrt{\Delta t}}_{\text{hedging error}}
    $$

    Taking the derivative with respect to $\Delta t$ and setting it to zero:

    $$
    \frac{dC}{d(\Delta t)} = -\frac{1}{2}\kappa\,\sigma\,S_0\,\sqrt{T}\,(\Delta t)^{-3/2} + \frac{1}{2}\Gamma\,\sigma^2\,S_0^2\,(\Delta t)^{-1/2} = 0
    $$

    Solving:

    $$
    \frac{1}{2}\Gamma\,\sigma^2\,S_0^2\,(\Delta t)^{-1/2} = \frac{1}{2}\kappa\,\sigma\,S_0\,\sqrt{T}\,(\Delta t)^{-3/2}
    $$

    Multiplying both sides by $2(\Delta t)^{3/2}$:

    $$
    \Gamma\,\sigma^2\,S_0^2\,\Delta t = \kappa\,\sigma\,S_0\,\sqrt{T}
    $$

    $$
    \Delta t^* = \frac{\kappa\,\sqrt{T}}{\Gamma\,\sigma\,S_0}
    $$

    The optimal rebalancing interval increases with transaction costs $\kappa$ (hedge less frequently when trading is expensive) and decreases with gamma $\Gamma$, volatility $\sigma$, and stock price $S_0$ (hedge more frequently when the hedging error is large).

---

**Exercise 5.**
Using the Breeden-Litzenberger formula

$$
\frac{\partial^2 C}{\partial K^2}\bigg|_{K=k} = e^{-rT}\,q(k, T)
$$

explain why the risk-neutral density $q(k, T)$ can be extracted from a sufficiently smooth implied volatility surface. If the implied volatility smile is symmetric around the at-the-money strike, what does this imply about the skewness of the risk-neutral distribution?

??? success "Solution to Exercise 5"
    The Breeden-Litzenberger formula states that the risk-neutral density is the second derivative of call prices with respect to strike:

    $$
    q(k, T) = e^{rT}\frac{\partial^2 C}{\partial K^2}\bigg|_{K=k}
    $$

    To extract $q$ from the implied volatility surface, one needs $C(K, T)$ to be twice differentiable in $K$. Given a smooth implied volatility surface $\sigma_{\mathrm{imp}}(K, T)$, the call price is $C(K, T) = \mathrm{BS}(S_0, K, T, r, \sigma_{\mathrm{imp}}(K, T))$, and the second derivative can be computed via the chain rule (involving $\partial \sigma_{\mathrm{imp}}/\partial K$ and $\partial^2 \sigma_{\mathrm{imp}}/\partial K^2$). As long as the surface is sufficiently smooth and the resulting $q(k, T) \geq 0$ everywhere, the density is well-defined.

    **Symmetric smile and skewness:** If the implied volatility smile is symmetric around the at-the-money strike $K = S_0 e^{rT}$ (i.e., $\sigma_{\mathrm{imp}}(K_0 + \delta, T) = \sigma_{\mathrm{imp}}(K_0 - \delta, T)$ for all $\delta$), then the risk-neutral density $q(k, T)$ is symmetric around its central value. A symmetric density has **zero skewness**.

    In equity markets, the implied volatility smile is typically asymmetric (a "skew" with higher implied volatility for low strikes), reflecting a negatively skewed risk-neutral distribution. The left tail is fatter than the right, consistent with crash risk being priced by the market. A symmetric smile would imply no such asymmetry.

---

**Exercise 6.**
Consider the Dupire local volatility formula

$$
\sigma_{\mathrm{loc}}^2(K, T) = \frac{\frac{\partial C}{\partial T} + rK\frac{\partial C}{\partial K}}{\frac{1}{2}K^2\frac{\partial^2 C}{\partial K^2}}
$$

Suppose call prices $C(K, T)$ are given by the Black-Scholes formula with constant implied volatility $\sigma_0$. Show that the local volatility surface reduces to $\sigma_{\mathrm{loc}}(K, T) = \sigma_0$ for all $K$ and $T$.

??? success "Solution to Exercise 6"
    Under constant implied volatility $\sigma_0$, the Black-Scholes call price is

    $$
    C(K, T) = S_0\,N(d_1) - Ke^{-rT}N(d_2)
    $$

    where $d_1 = \frac{\ln(S_0/K) + (r + \sigma_0^2/2)T}{\sigma_0\sqrt{T}}$ and $d_2 = d_1 - \sigma_0\sqrt{T}$.

    The Dupire formula requires three partial derivatives. For the Black-Scholes formula with constant $\sigma_0$:

    **Numerator:** Using the Black-Scholes PDE from the call price perspective, $\frac{\partial C}{\partial T} + rK\frac{\partial C}{\partial K}$. It is known that for the Black-Scholes price with constant volatility:

    $$
    \frac{\partial C}{\partial T} = S_0\,n(d_1)\frac{\sigma_0}{2\sqrt{T}} + rKe^{-rT}N(d_2)
    $$

    $$
    \frac{\partial C}{\partial K} = -e^{-rT}N(d_2)
    $$

    So the numerator is

    $$
    S_0\,n(d_1)\frac{\sigma_0}{2\sqrt{T}} + rKe^{-rT}N(d_2) - rKe^{-rT}N(d_2) = S_0\,n(d_1)\frac{\sigma_0}{2\sqrt{T}}
    $$

    **Denominator:** The second derivative of the Black-Scholes call with respect to $K$ is

    $$
    \frac{\partial^2 C}{\partial K^2} = e^{-rT}\frac{n(d_2)}{K\sigma_0\sqrt{T}}
    $$

    Using $S_0\,n(d_1) = Ke^{-rT}n(d_2)$ (a standard Black-Scholes identity), the numerator becomes $Ke^{-rT}n(d_2)\frac{\sigma_0}{2\sqrt{T}}$. Therefore:

    $$
    \sigma_{\mathrm{loc}}^2 = \frac{Ke^{-rT}n(d_2)\frac{\sigma_0}{2\sqrt{T}}}{\frac{1}{2}K^2 \cdot e^{-rT}\frac{n(d_2)}{K\sigma_0\sqrt{T}}} = \frac{Ke^{-rT}n(d_2)\frac{\sigma_0}{2\sqrt{T}}}{\frac{1}{2}Ke^{-rT}\frac{n(d_2)}{\sigma_0\sqrt{T}}} = \frac{\sigma_0}{2\sqrt{T}} \cdot \frac{2\sigma_0\sqrt{T}}{1} = \sigma_0^2
    $$

    Therefore $\sigma_{\mathrm{loc}}(K, T) = \sigma_0$ for all $K$ and $T$, confirming that when the implied volatility surface is flat, the local volatility surface is also flat and equal to $\sigma_0$. This is consistent with the fact that Black-Scholes is the special case of the local volatility model with constant local volatility.

---

**Exercise 7.**
A desk calibrates three models (Black-Scholes, local volatility, and Heston stochastic volatility) to the same set of vanilla option prices. For a down-and-out call with barrier $B$, the model prices are $V_{\mathrm{BS}} = 4.82$, $V_{\mathrm{LV}} = 5.41$, and $V_{\mathrm{Heston}} = 5.18$. Compute the model risk as defined by $\sup_{\mathcal{M}} V^{\mathcal{M}} - \inf_{\mathcal{M}} V^{\mathcal{M}}$. Explain why barrier options are particularly sensitive to model choice compared to vanilla options.

??? success "Solution to Exercise 7"
    The model risk is

    $$
    \sup_{\mathcal{M}} V^{\mathcal{M}} - \inf_{\mathcal{M}} V^{\mathcal{M}} = \max(4.82, 5.41, 5.18) - \min(4.82, 5.41, 5.18) = 5.41 - 4.82 = 0.59
    $$

    This represents a spread of \$0.59, or approximately 12% of the Black-Scholes price.

    **Why barrier options are particularly sensitive to model choice:**

    Vanilla option prices depend only on the **marginal distribution** of $S_T$ at maturity. All three models are calibrated to the same vanilla surface, meaning they agree on these marginal distributions. Consequently, vanilla prices are identical across models by construction.

    Barrier options, however, are **path-dependent**: their payoff depends on whether $S_t$ crosses the barrier $B$ at any time during $[0, T]$. This depends on the **transition densities** and **joint distributions** of $(S_{t_1}, S_{t_2}, \ldots, S_{t_n})$ at multiple times, not just the terminal distribution. Different models make fundamentally different assumptions about these dynamics:

    - **Black-Scholes** assumes constant volatility, producing smooth, continuous paths with a specific hitting probability for the barrier.
    - **Local volatility** has state-dependent volatility $\sigma(S, t)$, which changes the diffusion rate near the barrier, altering the hitting probability.
    - **Heston** has stochastic volatility with mean-reversion, producing clustering of high/low volatility periods that affects barrier crossing probabilities differently.

    Since the path dynamics differ across models even when marginal distributions agree, barrier option prices diverge. The closer the barrier is to the current spot price, and the longer the maturity, the more sensitive the price becomes to these dynamic differences.
