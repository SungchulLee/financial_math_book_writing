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

---

## Exercises

**Exercise 1.** Starting from the Ito decomposition $\ln(S_T/S_0) = (r - q)T - \frac{1}{2}\int_0^T \sigma_t^2 \, dt + \int_0^T \sigma_t \, dW_t$, derive the formula for expected integrated variance $\mathbb{E}^{\mathbb{Q}}[\int_0^T \sigma_t^2 \, dt] = 2(r-q)T - 2\mathbb{E}^{\mathbb{Q}}[\ln(S_T/S_0)]$. Explain why this requires no assumptions about the volatility process $\sigma_t$.

??? success "Solution to Exercise 1"
    Starting from the Ito decomposition of $\ln S_t$:

    $$
    \ln \frac{S_T}{S_0} = (r - q)T - \frac{1}{2}\int_0^T \sigma_t^2 \, dt + \int_0^T \sigma_t \, dW_t^{\mathbb{Q}}
    $$

    Take the risk-neutral expectation $\mathbb{E}^{\mathbb{Q}}[\cdot]$ of both sides. The stochastic integral $\int_0^T \sigma_t \, dW_t^{\mathbb{Q}}$ is a martingale (under mild integrability conditions on $\sigma_t$), so its expectation is zero:

    $$
    \mathbb{E}^{\mathbb{Q}}\left[\int_0^T \sigma_t \, dW_t^{\mathbb{Q}}\right] = 0
    $$

    Therefore:

    $$
    \mathbb{E}^{\mathbb{Q}}\left[\ln \frac{S_T}{S_0}\right] = (r - q)T - \frac{1}{2}\mathbb{E}^{\mathbb{Q}}\left[\int_0^T \sigma_t^2 \, dt\right]
    $$

    Solving for the expected integrated variance:

    $$
    \mathbb{E}^{\mathbb{Q}}\left[\int_0^T \sigma_t^2 \, dt\right] = 2(r - q)T - 2\mathbb{E}^{\mathbb{Q}}\left[\ln \frac{S_T}{S_0}\right]
    $$

    **Why no assumptions on $\sigma_t$ are needed:** The derivation uses only Ito's lemma (applied to $\ln S_t$) and the zero-expectation property of the stochastic integral. Ito's lemma is a purely mathematical result that applies to any semimartingale; it does not depend on whether $\sigma_t$ is constant, deterministic, stochastic, or even path-dependent. The volatility process $\sigma_t$ can follow any adapted process (Heston, SABR, local vol, regime-switching, etc.) and the formula remains valid. This is what makes the result **model-free**: it connects expected integrated variance to the expected log return without specifying the dynamics of volatility.

---

**Exercise 2.** The log contract payoff $\ln(S_T/F)$ can be replicated using a portfolio of OTM puts and calls via $\ln(S_T/F) = \frac{S_T - F}{F} - \int_0^F \frac{1}{K^2}\max(K - S_T, 0) \, dK - \int_F^\infty \frac{1}{K^2}\max(S_T - K, 0) \, dK$. Verify this identity for $S_T = 80$ with $F = 100$ by evaluating both sides.

??? success "Solution to Exercise 2"
    We need to verify the identity for $S_T = 80$ and $F = 100$:

    $$
    \ln \frac{S_T}{F} = \frac{S_T - F}{F} - \int_0^F \frac{(K - S_T)^+}{K^2} \, dK - \int_F^\infty \frac{(S_T - K)^+}{K^2} \, dK
    $$

    **Left side:**

    $$
    \ln \frac{80}{100} = \ln 0.8 \approx -0.22314
    $$

    **Right side, term by term:**

    *First term:*

    $$
    \frac{S_T - F}{F} = \frac{80 - 100}{100} = -0.20
    $$

    *Second term:* Since $S_T = 80 < F = 100$, the put payoff $(K - 80)^+$ is positive for $K > 80$:

    $$
    \int_0^{100} \frac{(K - 80)^+}{K^2} \, dK = \int_{80}^{100} \frac{K - 80}{K^2} \, dK
    $$

    Split:

    $$
    = \int_{80}^{100} \frac{1}{K} \, dK - 80\int_{80}^{100} \frac{1}{K^2} \, dK
    $$

    $$
    = \ln\frac{100}{80} - 80\left[-\frac{1}{K}\right]_{80}^{100} = \ln 1.25 - 80\left(-\frac{1}{100} + \frac{1}{80}\right)
    $$

    $$
    = 0.22314 - 80 \times \frac{1}{400} = 0.22314 - 0.20 = 0.02314
    $$

    *Third term:* Since $S_T = 80 < F = 100$, for $K > 100 > 80$, the call payoff $(80 - K)^+ = 0$:

    $$
    \int_{100}^\infty \frac{(80 - K)^+}{K^2} \, dK = 0
    $$

    **Combining:**

    $$
    \text{RHS} = -0.20 - 0.02314 - 0 = -0.22314
    $$

    **Verification:** $\text{LHS} = \ln(0.8) = -0.22314 = \text{RHS}$ $\checkmark$

---

**Exercise 3.** The CBOE VIX formula in continuous form is

$$
\text{VIX}^2 = \frac{2}{T} \left[\int_0^F \frac{P(K)}{K^2} dK + \int_F^\infty \frac{C(K)}{K^2} dK\right]
$$

Explain why only OTM options are used (puts for $K < F$, calls for $K > F$). What would go wrong if ITM options were included instead?

??? success "Solution to Exercise 3"
    **Why only OTM options are used:** The VIX formula uses puts for $K < F$ and calls for $K > F$, i.e., only out-of-the-money options. There are several reasons:

    1. **Liquidity and price discovery:** OTM options are more actively traded than ITM options. The bid-ask spreads are tighter (as a fraction of the option price), and the midquotes are more reliable reflections of fair value.

    2. **Avoiding intrinsic value contamination:** ITM options have a large intrinsic value component ($S_0 - Ke^{-rT}$ for ITM calls) that contributes nothing to the volatility information. The time value (extrinsic value), which contains the volatility signal, is a small fraction of the ITM price. Any error in the intrinsic value (due to incorrect forward price, dividend estimate, or interest rate) would dominate the volatility signal.

    3. **Put-call parity equivalence:** By put-call parity, $C(K) - P(K) = e^{-rT}(F - K)$. The forward contract component $e^{-rT}(F - K)$ contributes nothing to $\frac{\partial^2}{\partial K^2}$, so ITM calls and OTM puts carry identical volatility information. Using OTM options simply selects the more liquid and better-priced version.

    **What would go wrong with ITM options:** If ITM options were included:

    - The option prices would be dominated by intrinsic value, requiring precise knowledge of the forward price to extract the small time-value component
    - Bid-ask spreads on ITM options are wider in absolute terms, introducing more noise
    - Early exercise premia (for American options) would contaminate the European-style pricing assumption
    - Small errors in the forward price estimate would create large biases in the variance calculation

---

**Exercise 4.** The discrete CBOE VIX formula approximates the integral as a Riemann sum: $\text{VIX}^2 = \frac{2}{T}\sum_i \frac{\Delta K_i}{K_i^2} e^{rT} Q(K_i) - \frac{1}{T}(F/K_0 - 1)^2$, where $Q(K_i)$ is the midpoint of the bid-ask spread. Given 5 equally spaced strikes at $K = 90, 95, 100, 105, 110$ with $\Delta K = 5$, $F = 100$, $T = 30/365$, $r = 2\%$, and mid prices $Q = [8.50, 5.20, 3.00, 1.80, 0.90]$, compute $\text{VIX}^2$ and VIX.

??? success "Solution to Exercise 4"
    Given: $K = [90, 95, 100, 105, 110]$, $\Delta K = 5$, $F = 100$, $T = 30/365 \approx 0.08219$, $r = 0.02$, and $Q = [8.50, 5.20, 3.00, 1.80, 0.90]$.

    Since $F = 100$, set $K_0 = 100$ (highest strike below or equal to $F$). Strikes below 100 use puts, above 100 use calls, and at 100 use the average (here the midquote is given directly).

    Compute $e^{rT} = e^{0.02 \times 30/365} \approx e^{0.001644} \approx 1.001645$.

    Compute each term $\frac{\Delta K_i}{K_i^2} e^{rT} Q(K_i)$:

    | $K_i$ | $Q(K_i)$ | $\Delta K / K_i^2$ | Contribution |
    |--------|-----------|---------------------|-------------|
    | 90 | 8.50 | $5 / 8100 = 6.173 \times 10^{-4}$ | $6.173 \times 10^{-4} \times 1.00164 \times 8.50 = 5.250 \times 10^{-3}$ |
    | 95 | 5.20 | $5 / 9025 = 5.540 \times 10^{-4}$ | $5.540 \times 10^{-4} \times 1.00164 \times 5.20 = 2.882 \times 10^{-3}$ |
    | 100 | 3.00 | $5 / 10000 = 5.000 \times 10^{-4}$ | $5.000 \times 10^{-4} \times 1.00164 \times 3.00 = 1.502 \times 10^{-3}$ |
    | 105 | 1.80 | $5 / 11025 = 4.535 \times 10^{-4}$ | $4.535 \times 10^{-4} \times 1.00164 \times 1.80 = 8.168 \times 10^{-4}$ |
    | 110 | 0.90 | $5 / 12100 = 4.132 \times 10^{-4}$ | $4.132 \times 10^{-4} \times 1.00164 \times 0.90 = 3.722 \times 10^{-4}$ |

    Sum of contributions:

    $$
    \Sigma = 5.250 \times 10^{-3} + 2.882 \times 10^{-3} + 1.502 \times 10^{-3} + 8.168 \times 10^{-4} + 3.722 \times 10^{-4} = 0.01082
    $$

    Convexity correction: $F/K_0 - 1 = 100/100 - 1 = 0$, so the correction is zero.

    $$
    \text{VIX}^2 = \frac{2}{T} \times \Sigma = \frac{2}{0.08219} \times 0.01082 = 24.33 \times 0.01082 \approx 0.2633
    $$

    $$
    \text{VIX} = 100 \times \sqrt{0.2633} \approx 100 \times 0.5131 \approx 51.3
    $$

    Note: This high VIX value reflects the fact that the example uses only 5 strikes with relatively high option prices. In practice, the S&P 500 has hundreds of strikes and the individual contributions are much smaller.

---

**Exercise 5.** The VIX measures expected variance under the risk-neutral measure $\mathbb{Q}$, not the physical measure $\mathbb{P}$. The difference is the variance risk premium (VRP). If the VIX is 20 and the expected 30-day realized volatility under $\mathbb{P}$ is 16%, compute the annualized VRP in variance terms. Explain why VRP is typically positive for equity indices.

??? success "Solution to Exercise 5"
    Given VIX $= 20$ and expected 30-day realized volatility under $\mathbb{P}$ is 16%.

    The implied annualized variance under $\mathbb{Q}$ is:

    $$
    \sigma_{\mathbb{Q}}^2 = \left(\frac{\text{VIX}}{100}\right)^2 = 0.20^2 = 0.04
    $$

    The expected annualized realized variance under $\mathbb{P}$ is:

    $$
    \mathbb{E}^{\mathbb{P}}[\text{RV}] = 0.16^2 = 0.0256
    $$

    The annualized variance risk premium is:

    $$
    \text{VRP} = \sigma_{\mathbb{Q}}^2 - \mathbb{E}^{\mathbb{P}}[\text{RV}] = 0.04 - 0.0256 = 0.0144
    $$

    In volatility terms, this corresponds to $\sqrt{0.04} - \sqrt{0.0256} = 20\% - 16\% = 4\%$ volatility points (though VRP is properly defined in variance, not volatility space).

    **Why VRP is typically positive for equity indices:**

    1. **Hedging demand:** Portfolio managers systematically buy options (especially puts) for downside protection. This buying pressure inflates option prices and hence implied variance above the actuarially fair level.

    2. **Risk aversion to volatility:** Investors are averse to volatility itself (not just to losses). High-volatility states coincide with economic downturns, reduced consumption, and wealth destruction. Investors require a premium to bear this volatility risk.

    3. **Leverage effect:** Volatility rises when prices fall, creating a negative correlation between returns and volatility. Since high-volatility states are "bad" states, the risk-neutral measure overweights these scenarios, inflating implied variance.

    4. **Jump risk:** The VIX captures jump risk (via the log-contract replication), and jump events are negatively valued. The risk-neutral expectation of jump variance exceeds the physical expectation.

---

**Exercise 6.** The convexity adjustment between volatility and variance implies that $\mathbb{E}[\sigma] \leq \sqrt{\mathbb{E}[\sigma^2]}$ by Jensen's inequality. If the fair variance swap strike is $K_{\text{var}} = 0.04$ (20% vol), what is the upper bound on the expected volatility? Under what distributional assumptions would equality hold?

??? success "Solution to Exercise 6"
    By Jensen's inequality, for any concave function $f$ (here $f(x) = \sqrt{x}$):

    $$
    \mathbb{E}[\sqrt{X}] \leq \sqrt{\mathbb{E}[X]}
    $$

    Applied to $X = \frac{1}{T}\int_0^T \sigma_t^2 \, dt$ (realized variance):

    $$
    \mathbb{E}^{\mathbb{Q}}\left[\sqrt{\frac{1}{T}\int_0^T \sigma_t^2 \, dt}\right] \leq \sqrt{\mathbb{E}^{\mathbb{Q}}\left[\frac{1}{T}\int_0^T \sigma_t^2 \, dt\right]} = \sqrt{K_{\text{var}}}
    $$

    With $K_{\text{var}} = 0.04$, the upper bound on expected volatility is:

    $$
    \mathbb{E}^{\mathbb{Q}}[\sigma_{\text{realized}}] \leq \sqrt{0.04} = 0.20 = 20\%
    $$

    **When does equality hold?** Jensen's inequality becomes an equality if and only if the random variable inside $f$ is deterministic (i.e., constant with probability 1). This means:

    $$
    \frac{1}{T}\int_0^T \sigma_t^2 \, dt = K_{\text{var}} \quad \text{almost surely}
    $$

    This occurs when realized variance is non-random, which happens when volatility is deterministic (possibly time-varying, but not stochastic). The simplest case is the Black-Scholes model where $\sigma_t = \sigma_0$ is constant. Any model with stochastic volatility (Heston, SABR, etc.) will have $\mathbb{E}[\sigma] < \sqrt{K_{\text{var}}}$, and the gap increases with the vol-of-vol parameter.

---

**Exercise 7.** The VIX formula assumes a continuous strike grid, but in practice only finitely many strikes are traded. Describe how truncation of the integral at the last available OTM strike introduces a downward bias in the VIX calculation. How does the CBOE handle this, and why does the problem worsen during market stress when deep OTM puts become very valuable?

??? success "Solution to Exercise 7"
    **How truncation introduces downward bias:** The VIX formula integrates over all strikes from $0$ to $\infty$:

    $$
    K_{\text{var}} = \frac{2e^{rT}}{T}\int_0^\infty \frac{Q(K)}{K^2} \, dK
    $$

    In practice, the sum runs only from $K_{\min}$ (lowest listed strike with a nonzero bid) to $K_{\max}$ (highest listed strike with a nonzero bid). The missing contributions are:

    $$
    \text{Truncation bias} = \frac{2e^{rT}}{T}\left(\int_0^{K_{\min}} \frac{P(K)}{K^2} \, dK + \int_{K_{\max}}^\infty \frac{C(K)}{K^2} \, dK\right) > 0
    $$

    Since all option prices are non-negative, every omitted contribution is non-negative, so the truncated integral underestimates the true integral. The bias is **always downward**.

    **CBOE handling:** The CBOE mitigates truncation in several ways:

    1. **Bid price filter with stopping rule:** Include all OTM strikes moving outward from $K_0$ until two consecutive zero-bid options are encountered. This captures as much of the wings as the market provides.
    2. **Wide strike listing:** The S&P 500 has options listed at many strikes, extending deep into both wings.
    3. **Acceptance of residual bias:** The CBOE acknowledges that some truncation bias remains and treats it as negligible under normal market conditions (estimated at 0.1--0.5 vol points).

    **Why the problem worsens during market stress:** During a crash or crisis:

    1. **Deep OTM puts become valuable:** Market participants aggressively buy far OTM puts for tail hedging. These options, which normally have near-zero bids, now carry significant value.
    2. **$1/K^2$ amplification:** The puts that gain the most value are at low strikes, where the $1/K^2$ weight is largest. A put at $K = 70\%$ of spot has weight $1/(0.7F)^2 \approx 2\times$ the ATM weight.
    3. **Strike coverage gaps:** Even though more strikes become active during stress, the extreme tail may still be untradeable. The newly active put at (say) $K = 3000$ on the S&P 500 captures some of the tail but options at $K = 2500$ or below may still have no quotes.
    4. **Larger contribution from missing strikes:** In calm markets, the missing tail contributes negligibly. During stress, the risk-neutral density develops a much fatter left tail, and the missing strikes carry meaningful variance contribution.

    The net effect is that the truncation bias increases precisely when accurate VIX measurement matters most — during market stress.
