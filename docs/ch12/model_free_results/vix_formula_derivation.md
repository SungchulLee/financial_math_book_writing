# VIX Formula Derivation

The CBOE Volatility Index (VIX) provides a model-free measure of the market's expectation of 30-day forward-looking volatility. Unlike implied volatility computed from a single option via the Black-Scholes formula, the VIX aggregates information from the entire strip of out-of-the-money options to produce a single volatility number that requires no parametric model assumption. This section derives the VIX formula from first principles, starting with variance swap replication via the log contract, establishing the continuous-strike integral representation, and arriving at the CBOE's discrete approximation used in practice.

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Derive the fair strike of a variance swap using the log contract replication argument
    - Explain why the integral $\int C(K)/K^2 \, dK$ captures model-free implied variance
    - State and derive the CBOE VIX formula from the continuous variance swap formula
    - Identify the convexity adjustment between volatility and variance
    - Compute VIX from a discrete set of option prices

## Variance Swap Replication

### Motivation

A variance swap is a forward contract on realized variance. The buyer receives the realized variance of an underlying asset over a specified period and pays a fixed strike $K_{\text{var}}$. The central question is: what is the fair value of $K_{\text{var}}$ such that the swap has zero initial value? The answer turns out to be expressible as an integral over option prices — a remarkable model-free result that forms the theoretical backbone of the VIX.

### The Log Contract

The key to variance swap replication is the **log contract**, a derivative with payoff $\ln(S_T / S_0)$ at maturity $T$. Under the risk-neutral measure $\mathbb{Q}$, the stock price follows:

$$
\frac{dS_t}{S_t} = (r - q) \, dt + \sigma_t \, dW_t^{\mathbb{Q}}
$$

where $\sigma_t$ is the (possibly stochastic) instantaneous volatility. Applying Ito's lemma to $\ln S_t$:

$$
d \ln S_t = \left(r - q - \frac{1}{2}\sigma_t^2\right) dt + \sigma_t \, dW_t^{\mathbb{Q}}
$$

Integrating from $0$ to $T$:

$$
\ln \frac{S_T}{S_0} = (r - q)T - \frac{1}{2}\int_0^T \sigma_t^2 \, dt + \int_0^T \sigma_t \, dW_t^{\mathbb{Q}}
$$

Taking the risk-neutral expectation and using the fact that the stochastic integral has zero expectation:

$$
\mathbb{E}^{\mathbb{Q}}\left[\ln \frac{S_T}{S_0}\right] = (r - q)T - \frac{1}{2}\mathbb{E}^{\mathbb{Q}}\left[\int_0^T \sigma_t^2 \, dt\right]
$$

Solving for the expected integrated variance:

$$
\mathbb{E}^{\mathbb{Q}}\left[\int_0^T \sigma_t^2 \, dt\right] = 2(r - q)T - 2\mathbb{E}^{\mathbb{Q}}\left[\ln \frac{S_T}{S_0}\right]
$$

This expresses the fair variance as a function of the risk-neutral expected log return — the price of the log contract.

### Replicating the Log Contract with Options

The log contract payoff can be replicated using a static portfolio of European options. The key identity comes from a second-order Taylor expansion with integral remainder:

$$
\ln \frac{S_T}{F} = \frac{S_T - F}{F} - \int_0^F \frac{(K - S_T)^+}{K^2} \, dK - \int_F^\infty \frac{(S_T - K)^+}{K^2} \, dK
$$

where $F = S_0 e^{(r-q)T}$ is the forward price. This identity decomposes the log payoff into:

1. A forward contract (first term)
2. A continuum of out-of-the-money puts weighted by $1/K^2$ (second term)
3. A continuum of out-of-the-money calls weighted by $1/K^2$ (third term)

**Proof of the replication identity.** Start from the identity for any twice-differentiable function $f$:

$$
f(S_T) = f(F) + f'(F)(S_T - F) + \int_0^F f''(K)(K - S_T)^+ \, dK + \int_F^\infty f''(K)(S_T - K)^+ \, dK
$$

For $f(x) = \ln(x/F)$, we have $f(F) = 0$, $f'(x) = 1/x$, and $f''(x) = -1/x^2$. Substituting:

$$
\ln \frac{S_T}{F} = \frac{S_T - F}{F} - \int_0^F \frac{(K - S_T)^+}{K^2} \, dK - \int_F^\infty \frac{(S_T - K)^+}{K^2} \, dK
$$

$\square$

### Fair Strike of the Variance Swap

Taking the discounted risk-neutral expectation of the replication identity:

$$
e^{-rT}\mathbb{E}^{\mathbb{Q}}\left[\ln \frac{S_T}{F}\right] = 0 - \int_0^F \frac{P(K)}{K^2} \, dK - \int_F^\infty \frac{C(K)}{K^2} \, dK
$$

where $P(K) = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(K - S_T)^+]$ and $C(K) = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+]$ are European put and call prices, and the forward contract term vanishes since $\mathbb{E}^{\mathbb{Q}}[S_T] = F$.

Combining with the variance formula derived above:

$$
\frac{1}{T}\mathbb{E}^{\mathbb{Q}}\left[\int_0^T \sigma_t^2 \, dt\right] = \frac{2e^{rT}}{T}\left(\int_0^F \frac{P(K)}{K^2} \, dK + \int_F^\infty \frac{C(K)}{K^2} \, dK\right)
$$

**Theorem 12.4.1** (Variance Swap Fair Strike)
The fair strike of a variance swap is:

$$
K_{\text{var}} = \frac{2e^{rT}}{T}\left(\int_0^F \frac{P(K)}{K^2} \, dK + \int_F^\infty \frac{C(K)}{K^2} \, dK\right)
$$

This result is **model-free**: it holds for any process with continuous paths (no jumps) and requires only the absence of arbitrage.

!!! note "The $1/K^2$ Weighting"
    The $1/K^2$ weighting arises naturally from the second derivative of $\ln(x)$. Options at lower strikes receive higher weight, reflecting the fact that percentage moves are larger for lower asset values. This weighting also connects to the Breeden-Litzenberger formula: since $\partial^2 C / \partial K^2 = e^{-rT} q(K)$, the integral effectively averages the local variance over the risk-neutral density.

## From Variance Swap to VIX

### The Continuous VIX Formula

The VIX is defined as the square root of the variance swap fair strike (annualized to percentage terms), with a specific adjustment. Starting from the variance swap formula:

$$
\text{VIX}^2 = \frac{2e^{rT}}{T}\int_0^\infty \frac{Q(K)}{K^2} \, dK - \frac{1}{T}\left(\frac{F}{K_0} - 1\right)^2
$$

where $Q(K)$ denotes the OTM option price (put for $K < F$, call for $K > F$), and $K_0$ is the highest strike below the forward price $F$. The second term is a **convexity adjustment** that accounts for the discrete strike grid; in the continuous limit with $K_0 = F$, it vanishes and the formula reduces to the variance swap fair strike.

### The Forward Price Adjustment

In the continuous-strike version, the VIX formula uses the forward price $F$ as the cutoff between puts and calls. Since $F$ may not coincide with any listed strike, the CBOE introduces $K_0 \leq F$ and adds the correction term:

$$
\frac{1}{T}\left(\frac{F}{K_0} - 1\right)^2
$$

This correction arises because shifting the put-call boundary from $F$ to $K_0$ introduces a small bias. Specifically, at strikes between $K_0$ and $F$, using puts instead of calls (or vice versa) changes the integral by an amount proportional to $(F - K_0)^2$.

**Proposition 12.4.1** (Convexity Correction)
For $K_0 \leq F$, the difference between the variance swap integral split at $F$ and the integral split at $K_0$ satisfies:

$$
\frac{2e^{rT}}{T}\left(\int_0^F \frac{P(K)}{K^2} \, dK + \int_F^\infty \frac{C(K)}{K^2} \, dK\right) = \frac{2e^{rT}}{T}\int_0^\infty \frac{Q(K)}{K^2} \, dK - \frac{1}{T}\left(\frac{F}{K_0} - 1\right)^2 + O\!\left(\frac{(F - K_0)^3}{K_0^3}\right)
$$

where $Q(K)$ uses the split at $K_0$.

*Proof sketch.* Apply put-call parity $C(K) - P(K) = e^{-rT}(F - K)$ to the integral between $K_0$ and $F$, expand $\ln(F/K_0)$ as $(F/K_0 - 1) - \frac{1}{2}(F/K_0 - 1)^2 + \cdots$, and collect terms. $\square$

## CBOE VIX Methodology

### Discrete Approximation

In practice, options trade at a finite set of strikes $K_1 < K_2 < \cdots < K_n$. The CBOE approximates the continuous integral using a Riemann sum:

$$
\text{VIX}^2 = \frac{2}{T}\sum_{i=1}^{n} \frac{\Delta K_i}{K_i^2} e^{rT} Q(K_i) - \frac{1}{T}\left(\frac{F}{K_0} - 1\right)^2
$$

where:

- $\Delta K_i = \frac{K_{i+1} - K_{i-1}}{2}$ for interior strikes, with one-sided differences at the endpoints
- $Q(K_i) = \text{put midquote}$ if $K_i < K_0$, $\text{call midquote}$ if $K_i > K_0$, and $\frac{1}{2}(\text{put} + \text{call})$ if $K_i = K_0$
- $K_0$ is the highest listed strike below the forward price $F$
- $T$ is the time to expiration in years (minutes-based: $T = N_{\text{min}} / N_{\text{year}}$)

**Definition 12.4.1** (CBOE VIX Index)
The VIX index is defined as:

$$
\text{VIX} = 100 \times \sqrt{\frac{2}{T}\sum_{i} \frac{\Delta K_i}{K_i^2} e^{rT} Q(K_i) - \frac{1}{T}\left(\frac{F}{K_0} - 1\right)^2}
$$

The factor of 100 converts to percentage points, so VIX = 20 corresponds to 20% annualized volatility.

### Maturity Interpolation

The VIX targets a 30-day forward-looking window. Since listed options rarely expire exactly 30 days out, the CBOE interpolates between two near-term maturities:

$$
\text{VIX}^2 = T_1 \sigma_1^2 \left(\frac{N_{T_2} - N_{30}}{N_{T_2} - N_{T_1}}\right) + T_2 \sigma_2^2 \left(\frac{N_{30} - N_{T_1}}{N_{T_2} - N_{T_1}}\right)
$$

where $\sigma_1^2$ and $\sigma_2^2$ are the variance estimates from the near-term ($T_1$) and next-term ($T_2$) option expirations, and $N_{30}$, $N_{T_1}$, $N_{T_2}$ are expressed in minutes. This is a linear interpolation in variance (not volatility) space, consistent with the additive property of variance over non-overlapping intervals.

### Selection Rules

The CBOE applies specific rules to filter the option data:

1. **Bid price filter:** Exclude any option with a zero bid price. Moving outward from $K_0$, stop including strikes after two consecutive zero-bid options
2. **Near-term expiry:** Use options with at least 23 days and no more than 37 days to expiration
3. **Next-term expiry:** Use options with at least 30 days to expiration
4. **Weekly vs monthly:** The CBOE uses both weekly and standard monthly expirations in the current methodology

!!! warning "Truncation Bias"
    The VIX formula integrates over all strikes from zero to infinity, but listed options cover only a finite range. The missing wing contributions introduce a **truncation bias**, causing the discrete VIX to underestimate the true model-free implied variance. The bias is most significant during periods of high skew, when deep OTM puts carry substantial weight. Empirical estimates suggest the truncation bias is typically 0.1--0.5 vol points for the S&P 500.

## Connection to Implied Variance

### Variance Swap vs Implied Volatility

The VIX squared represents the **model-free implied variance**, which differs from the Black-Scholes ATM implied volatility:

$$
\text{VIX}^2 / 100^2 = \sigma_{\text{MF}}^2 \neq \sigma_{\text{ATM}}^2
$$

The relationship between the two involves contributions from the entire smile:

$$
\sigma_{\text{MF}}^2 = \sigma_{\text{ATM}}^2 + \text{skew contribution} + \text{curvature contribution} + \cdots
$$

**Proposition 12.4.2** (Model-Free vs ATM Variance)
In terms of the implied volatility surface, the model-free variance can be expanded as:

$$
\sigma_{\text{MF}}^2 \approx \sigma_{\text{ATM}}^2 + \frac{1}{3}\sigma_{\text{ATM}}^2 \kappa_4 T + O(T^2)
$$

where $\kappa_4$ is the excess kurtosis of the risk-neutral log-return distribution. The skewness enters at higher order. Thus the VIX exceeds ATM implied volatility when the distribution has fat tails (positive excess kurtosis), as is typical in equity markets.

### Connection to Breeden-Litzenberger

The $1/K^2$ weighting in the VIX formula connects directly to the Breeden-Litzenberger risk-neutral density. Writing $q(K) = e^{rT} \partial^2 C / \partial K^2$:

$$
K_{\text{var}} = \frac{2e^{rT}}{T}\int_0^\infty \frac{C(K)}{K^2} \, dK = \frac{2}{T}\int_0^\infty \frac{\int_K^\infty (S - K) q(S) \, dS}{K^2} \, dK
$$

Changing the order of integration and evaluating:

$$
K_{\text{var}} = \frac{2}{T}\int_0^\infty q(S) \left(\int_0^S \frac{S - K}{K^2} \, dK\right) dS = \frac{2}{T}\int_0^\infty q(S) \left(\frac{S}{K}\bigg|_0^S + \ln K\bigg|_0^S\right) dS
$$

After regularization (subtracting the forward contract contribution), this yields:

$$
K_{\text{var}} = -\frac{2}{T}\mathbb{E}^{\mathbb{Q}}\left[\ln \frac{S_T}{F}\right]
$$

confirming the variance swap interpretation: the fair strike equals (twice) the negative of the expected log return relative to the forward.

## Jump Correction

### Impact of Jumps on Variance Swaps

The derivation above assumes continuous paths. When the underlying can jump, the relationship between the log contract and integrated variance breaks down. Under a jump-diffusion model:

$$
\frac{dS_t}{S_{t^-}} = (r - q - \lambda \bar{J}) \, dt + \sigma_t \, dW_t + J_t \, dN_t
$$

where $N_t$ is a Poisson process with intensity $\lambda$ and $J_t$ is the jump size, the integrated variance and the log contract differ by the jump contribution:

$$
-\frac{2}{T}\mathbb{E}^{\mathbb{Q}}\left[\ln \frac{S_T}{F}\right] = \frac{1}{T}\mathbb{E}^{\mathbb{Q}}\left[\int_0^T \sigma_t^2 \, dt\right] + \frac{2\lambda}{T}\mathbb{E}^{\mathbb{Q}}\left[\int_0^T \left(J_t - \ln(1 + J_t)\right) dt\right]
$$

The second term is always non-negative (since $x - \ln(1+x) \geq 0$ for $x > -1$), so the VIX overestimates the expected integrated variance in the presence of jumps. This jump contribution is sometimes called the **jump risk premium** embedded in VIX.

!!! tip "Practical Implication"
    The jump correction explains why VIX systematically exceeds subsequently realized volatility. Part of the "variance risk premium" commonly observed in the literature reflects not only risk aversion but also the convexity of the log contract under jump risk. Separating these two effects requires additional modeling assumptions about jump intensity and size distribution.

## Numerical Example

### Computing VIX from Market Data

Consider S&P 500 options with the following parameters:

- Current index level: $S_0 = 4500$
- Risk-free rate: $r = 5\%$
- Dividend yield: $q = 1.5\%$
- Time to near-term expiration: $T_1 = 25$ days $= 25/365$ years
- Forward price: $F = S_0 e^{(r-q)T_1} = 4500 \times e^{0.035 \times 25/365} \approx 4503.42$

Suppose the following OTM option midquotes are available:

| Strike $K$ | Type | Midquote $Q(K)$ | $\Delta K$ | $\Delta K / K^2$ | Contribution |
|------------|------|-----------------|------------|-------------------|-------------|
| 4300 | Put | 12.50 | 50 | $2.70 \times 10^{-6}$ | $3.38 \times 10^{-5}$ |
| 4350 | Put | 17.80 | 50 | $2.64 \times 10^{-6}$ | $4.70 \times 10^{-5}$ |
| 4400 | Put | 26.40 | 50 | $2.58 \times 10^{-6}$ | $6.82 \times 10^{-5}$ |
| 4450 | Put | 41.20 | 50 | $2.53 \times 10^{-6}$ | $1.04 \times 10^{-4}$ |
| 4500 | Avg  | 55.30 | 50 | $2.47 \times 10^{-6}$ | $1.37 \times 10^{-4}$ |
| 4550 | Call | 38.60 | 50 | $2.42 \times 10^{-6}$ | $9.33 \times 10^{-5}$ |
| 4600 | Call | 22.10 | 50 | $2.36 \times 10^{-6}$ | $5.22 \times 10^{-5}$ |
| 4650 | Call | 11.40 | 50 | $2.31 \times 10^{-6}$ | $2.64 \times 10^{-5}$ |
| 4700 | Call | 5.20 | 50 | $2.26 \times 10^{-6}$ | $1.18 \times 10^{-5}$ |

Each contribution is $(\Delta K_i / K_i^2) \times e^{rT_1} Q(K_i)$. Summing and applying the formula:

$$
\sigma_1^2 = \frac{2}{T_1} \sum_i \frac{\Delta K_i}{K_i^2} e^{rT_1} Q(K_i) - \frac{1}{T_1}\left(\frac{F}{K_0} - 1\right)^2
$$

With $K_0 = 4500$ and the convexity correction $(F/K_0 - 1)^2 = (4503.42/4500 - 1)^2 \approx 5.78 \times 10^{-7}$, which is negligible. The sum of contributions gives a representative value leading to:

$$
\text{VIX} \approx 100 \times \sqrt{\sigma_1^2} \approx 18.5
$$

corresponding to an annualized model-free implied volatility of approximately 18.5%.

## Variance Swap vs Volatility Swap

### The Convexity Adjustment

A **volatility swap** pays the realized volatility $\sqrt{(1/T)\int_0^T \sigma_t^2 \, dt}$ minus a fixed strike, rather than realized variance minus a fixed strike. By Jensen's inequality:

$$
\mathbb{E}^{\mathbb{Q}}\left[\sqrt{\frac{1}{T}\int_0^T \sigma_t^2 \, dt}\right] \leq \sqrt{\mathbb{E}^{\mathbb{Q}}\left[\frac{1}{T}\int_0^T \sigma_t^2 \, dt\right]} = \sqrt{K_{\text{var}}}
$$

Therefore, the fair strike of a volatility swap is less than or equal to the VIX:

$$
K_{\text{vol}} \leq \text{VIX}/100
$$

The difference depends on the vol-of-vol:

$$
K_{\text{vol}} \approx \sqrt{K_{\text{var}}} - \frac{\text{Var}(\sigma_{\text{realized}})}{8 K_{\text{var}}^{3/2}}
$$

This **convexity adjustment** is larger when vol-of-vol is high (volatile volatility environment).

!!! example "Convexity Gap in Practice"
    If VIX = 20 (so $K_{\text{var}} = 0.04$) and the standard deviation of realized volatility is 4 vol points (vol-of-vol = 0.04), the convexity adjustment is approximately:

    $$
    \frac{0.04^2}{8 \times 0.04^{3/2}} = \frac{0.0016}{0.0640} \approx 0.025
    $$

    So the fair volatility swap strike is approximately $0.20 - 0.025 = 0.175$, or 17.5%. The 2.5 percentage point gap represents the variance-volatility convexity premium.

## Extensions

### Corridor Variance Swaps

A **corridor variance swap** accumulates realized variance only when the underlying trades within a specified corridor $[L, U]$:

$$
K_{\text{corr}} = \frac{2e^{rT}}{T}\left(\int_L^F \frac{P(K)}{K^2} \, dK + \int_F^U \frac{C(K)}{K^2} \, dK\right)
$$

This restricts the integration range and provides exposure to volatility in a specific spot range. The standard VIX corresponds to $L = 0$, $U = \infty$.

### Gamma Swaps

A **gamma swap** has payoff proportional to realized variance weighted by the underlying level:

$$
\text{Payoff} = \sum_i \frac{S_{t_i}}{S_0} \ln^2\left(\frac{S_{t_i}}{S_{t_{i-1}}}\right) - K_{\text{gamma}}
$$

The fair strike involves an integral with $1/K$ weighting instead of $1/K^2$:

$$
K_{\text{gamma}} = \frac{2e^{rT}}{T S_0}\left(\int_0^F \frac{P(K)}{K} \, dK + \int_F^\infty \frac{C(K)}{K} \, dK\right)
$$

Gamma swaps are less sensitive to extreme moves and do not require delta hedging.

## Summary

The VIX formula rests on a chain of model-free results:

1. **Ito's lemma** connects integrated variance to the log contract: $\mathbb{E}^{\mathbb{Q}}[\int_0^T \sigma_t^2 \, dt] = 2(r-q)T - 2\mathbb{E}^{\mathbb{Q}}[\ln(S_T/S_0)]$
2. **Static replication** decomposes the log contract into a portfolio of OTM options weighted by $1/K^2$
3. **Variance swap fair strike** equals the integral of weighted option prices: $K_{\text{var}} = (2e^{rT}/T)\int Q(K)/K^2 \, dK$
4. **CBOE discretization** approximates the integral with a Riemann sum over listed strikes, with a convexity correction for the put-call boundary

The resulting VIX is a model-free measure of implied variance that:

- Requires no parametric model assumption (holds for any continuous-path process)
- Uses the entire option smile, not just a single ATM option
- Overestimates expected realized volatility due to the variance risk premium and jump effects
- Provides the benchmark for volatility derivatives trading
