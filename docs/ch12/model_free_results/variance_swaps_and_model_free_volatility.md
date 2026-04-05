# Variance Swaps and Model-Free Volatility

Variance swaps provide direct exposure to realized volatility and enable model-free pricing of volatility. These instruments reveal the market's volatility expectations independent of any specific pricing model and form the foundation for variance curve construction and volatility derivatives trading.

## Key Concepts

**Variance Swap Definition**
A variance swap exchanges realized variance for a fixed strike:

$$\text{Payoff} = N \times \left(\sum_i \ln^2\left(\frac{S_{t_i}}{S_{t_{i-1}}}\right) - K_{\text{var}}^2\right) \times \Delta t$$

Key features:
- Long variance position: profits when realized volatility exceeds strike
- Cash settlement: no need to hold underlying asset
- Fair strike $K_{\text{var}}^*$ determined by replication arguments

**Model-Free Replication**
Under risk-neutral measure, realized variance can be replicated using:
1. A log contract (payoff = $\ln S_T / S_0$) for the mean term
2. A continuum of out-of-the-money options across all strikes for the variance term

The replication formula:

$$\text{Var}(S) = 2 \int_0^{\infty} \frac{C(K)}{K^2} dK - \frac{1}{T}\ln^2(F/S_0)$$

where $C(K)$ are European call prices and $F$ is the forward.

**Relating Variance to Volatility**
Realized variance: $\text{RV} = \frac{1}{T}\sum_i r_i^2$

Implied variance from options: $\sigma_{\text{IV}}^2 = E^Q[\text{RV}]$ (risk-neutral expectation)

The variance risk premium: $\text{VRP} = \sigma_{\text{IV}}^2 - E^P[\text{RV}]$
where the superscript denotes risk-neutral (Q) vs physical (P) measure.

**Model-Free Implied Volatility**
The VIX index computes model-free implied volatility from options:

$$\text{VIX}^2 = \frac{2}{T}\int_0^{\infty} \frac{C(K)}{K^2} dK - \frac{1}{T}\ln^2(F/K_0)$$

This is model-independent and directly observable from market option prices.

**Volatility Curve Construction**
Variance swaps at different maturities trace out the variance curve:
- Short-dated: influenced by near-term uncertainty and momentum
- Long-dated: approach long-run volatility forecast
- Term structure shape: upward sloping (near trough) or downward sloping (elevated stress)

!!! note "Market Applications"
    Variance swaps enable:
    - Pure volatility trading without directional bet
    - Volatility curve construction from traded instruments
    - Hedging volatility exposure (vega neutral portfolio construction)
    - Arbitrage between realized and implied volatility
    - Model-free calibration targets for stochastic vol models

---

## Exercises

**Exercise 1.** A variance swap has notional $N = \$100{,}000$ per variance point, maturity $T = 0.25$ years, and strike $K_{\text{var}} = 0.04$ (corresponding to 20% volatility). If the realized variance over the period is $\text{RV} = 0.0625$ (25% volatility), compute the payoff to the long variance position.

??? success "Solution to Exercise 1"
    Given: $N = \$100{,}000$ per variance point, $T = 0.25$ years, $K_{\text{var}} = 0.04$ (strike in variance terms, corresponding to $\sqrt{0.04} = 20\%$ volatility), and realized variance $\text{RV} = 0.0625$ (corresponding to $\sqrt{0.0625} = 25\%$ volatility).

    The payoff to the long variance position is:

    $$
    \text{Payoff} = N \times (\text{RV} - K_{\text{var}}) = 100{,}000 \times (0.0625 - 0.04)
    $$

    $$
    = 100{,}000 \times 0.0225 = \$2{,}250
    $$

    The long variance position profits because realized volatility (25%) exceeded the strike volatility (20%). The payoff is linear in variance (not volatility), so the \$2,250 gain reflects the difference in variance terms: $0.0625 - 0.04 = 0.0225$.

    Note: If the realized variance had been $0.04$ (exactly at strike), the payoff would be zero. If realized variance had been $0.0256$ (16% vol), the payoff would be $100{,}000 \times (0.0256 - 0.04) = -\$1{,}440$, a loss to the long position.

---

**Exercise 2.** The model-free replication formula for variance swap fair strike involves the integral $\frac{2}{T}\int_0^\infty \frac{C(K)}{K^2} dK$, split at the forward $F$ into put and call components. Explain why the $1/K^2$ weighting gives more weight to low-strike (OTM put) options. What does this imply about the sensitivity of variance swap pricing to left-tail events?

??? success "Solution to Exercise 2"
    The model-free replication formula splits at the forward $F$:

    $$
    K_{\text{var}} = \frac{2e^{rT}}{T}\left(\int_0^F \frac{P(K)}{K^2} \, dK + \int_F^\infty \frac{C(K)}{K^2} \, dK\right)
    $$

    The $1/K^2$ weighting assigns disproportionately more weight to low-strike options:

    - At $K = 50$: weight is $1/2500 = 0.0004$
    - At $K = 100$: weight is $1/10000 = 0.0001$
    - At $K = 200$: weight is $1/40000 = 0.000025$

    An option at half the forward strike receives 4 times the weight of an ATM option. This occurs because the $1/K^2$ weighting arises from the second derivative of $\ln(x)$, i.e., $f''(K) = -1/K^2$. The log function has more curvature at lower values, meaning a given absolute price change at lower levels corresponds to a larger percentage move.

    **Sensitivity to left-tail events:** Since the low-strike OTM puts receive the highest weight, the variance swap fair strike (and the VIX) is heavily influenced by the left tail of the return distribution. This has several implications:

    1. **Crash sensitivity:** Deep OTM puts, which protect against large downside moves, dominate the integral. A spike in put prices due to crash fear significantly increases the variance swap fair strike.

    2. **Skew dependence:** The steeper the implied volatility skew (higher put vol relative to call vol), the higher the variance swap strike, because the heavily-weighted low-strike puts are more expensive.

    3. **Asymmetric exposure:** A long variance swap position has more exposure to downside moves than upside moves of the same magnitude, because the $1/K^2$ weighting amplifies the contribution of downside events.

---

**Exercise 3.** The variance risk premium is defined as $\text{VRP} = \sigma_{\text{IV}}^2 - \mathbb{E}^P[\text{RV}]$. Empirical studies find that VRP is typically positive for equity indices (implied variance exceeds expected realized variance). (a) What economic explanation accounts for this premium? (b) How can a trader profit from a consistently positive VRP? (c) What are the risks of such a strategy?

??? success "Solution to Exercise 3"
    **(a) Economic explanation for positive VRP:** The variance risk premium reflects investor risk aversion toward volatility itself. Several mechanisms contribute:

    - **Crash insurance demand:** Institutional investors (pension funds, mutual funds) systematically buy OTM puts for portfolio protection, driving up put prices and implied variance above the actuarially fair level.
    - **Volatility as a risk factor:** High volatility coincides with poor economic states (recessions, crises). Investors require compensation for bearing this risk, creating a premium in implied variance.
    - **Loss aversion:** Investors dislike variance more in down markets than they benefit from it in up markets, leading them to overpay for variance reduction.

    **(b) Trading strategy to profit from positive VRP:** Systematically **sell variance swaps** (or sell straddles/strangles, or sell VIX futures):

    - Enter short variance swap positions at the implied strike $K_{\text{var}} = \sigma_{\text{IV}}^2$
    - At maturity, pay realized variance $\text{RV}$
    - Expected profit per swap: $\text{VRP} = \sigma_{\text{IV}}^2 - \mathbb{E}^P[\text{RV}] > 0$

    This is sometimes called "harvesting the variance risk premium."

    **(c) Risks of the strategy:**

    - **Tail risk:** Selling variance has unlimited downside. A market crash (e.g., 2008, 2020) can produce realized variance far exceeding implied variance, generating catastrophic losses.
    - **Negative skewness of returns:** The strategy profits frequently but modestly, then loses infrequently but massively — the payoff distribution is negatively skewed.
    - **Margin/capital requirements:** Spikes in implied volatility require additional margin, potentially forcing liquidation at the worst time.
    - **Regime changes:** The VRP can turn negative during sustained stress periods, invalidating the strategy premise.

---

**Exercise 4.** Given the variance swap formula, explain why the VIX index can be interpreted as the square root of the fair variance swap strike (with a small adjustment). If VIX = 22, what is the implied annualized variance? What is the market's expectation for 30-day realized volatility (ignoring the variance risk premium)?

??? success "Solution to Exercise 4"
    If VIX $= 22$, then:

    $$
    \text{VIX}^2 = 22^2 = 484
    $$

    The implied annualized variance is:

    $$
    \sigma_{\text{MF}}^2 = \frac{\text{VIX}^2}{100^2} = \frac{484}{10000} = 0.0484
    $$

    This is the annualized variance, corresponding to an annualized volatility of $\sqrt{0.0484} = 0.22 = 22\%$.

    For the market's expectation of 30-day realized volatility (ignoring VRP): VIX measures the expected variance over a 30-day horizon. The 30-day variance is:

    $$
    \sigma_{30d}^2 = \sigma_{\text{MF}}^2 \times \frac{30}{365} = 0.0484 \times 0.0822 = 0.00398
    $$

    The expected 30-day realized volatility (annualized) is simply:

    $$
    \sigma_{30d, \text{ann}} = \text{VIX}/100 = 22\%
    $$

    since VIX is already quoted in annualized terms. Ignoring the variance risk premium, the market expects realized volatility over the next 30 days to be approximately 22% (annualized). In practice, VRP is positive, so the actual expected realized volatility is lower, typically around 16--18% when VIX is at 22.

---

**Exercise 5.** The variance curve plots $K_{\text{var}}(T)$ versus maturity $T$. During a market crisis, the variance curve typically inverts (short-dated variance higher than long-dated). (a) What does this imply about the market's expectation for near-term versus long-term volatility? (b) How does this relate to the mean-reversion property of volatility?

??? success "Solution to Exercise 5"
    **(a)** An inverted variance curve means $K_{\text{var}}(T_1) > K_{\text{var}}(T_2)$ for $T_1 < T_2$. This implies:

    - **Near-term:** The market expects high volatility in the immediate future (due to a crisis, major event, or elevated uncertainty).
    - **Long-term:** The market expects volatility to decline over time and return to more normal levels.

    The inversion reflects the belief that the current elevated volatility is temporary — the market is pricing a transient shock, not a permanent regime change.

    **(b) Relation to mean-reversion:** The inverted variance curve is a direct manifestation of **volatility mean-reversion**. Under most stochastic volatility models (e.g., Heston), variance reverts to a long-run mean $\theta$:

    $$
    dv_t = \kappa(\theta - v_t) \, dt + \xi \sqrt{v_t} \, dW_t
    $$

    When current variance $v_0 > \theta$ (elevated stress), the drift pulls variance downward, so:

    - Short-dated expected variance $\approx v_0$ (high, near current level)
    - Long-dated expected variance $\approx \theta$ (lower, near the long-run mean)

    This creates a downward-sloping (inverted) variance term structure. Conversely, when $v_0 < \theta$ (calm period), the drift pulls variance upward, creating an upward-sloping term structure. The speed of mean-reversion $\kappa$ determines how quickly the curve flattens toward $\theta$.

---

**Exercise 6.** A forward-starting variance swap covers the period $[T_1, T_2]$ with fair strike $\sigma_{\text{fwd}}^2 = \frac{K_{\text{var}}(T_2) T_2 - K_{\text{var}}(T_1) T_1}{T_2 - T_1}$. Given $K_{\text{var}}(0.25) = 0.04$ and $K_{\text{var}}(0.50) = 0.036$, compute the forward variance for the period $[0.25, 0.50]$. Is the forward variance higher or lower than the spot variance?

??? success "Solution to Exercise 6"
    Given: $K_{\text{var}}(0.25) = 0.04$ and $K_{\text{var}}(0.50) = 0.036$.

    The forward variance for $[T_1, T_2] = [0.25, 0.50]$ is:

    $$
    \sigma_{\text{fwd}}^2 = \frac{K_{\text{var}}(T_2) \cdot T_2 - K_{\text{var}}(T_1) \cdot T_1}{T_2 - T_1}
    $$

    Substituting:

    $$
    \sigma_{\text{fwd}}^2 = \frac{0.036 \times 0.50 - 0.04 \times 0.25}{0.50 - 0.25} = \frac{0.018 - 0.010}{0.25} = \frac{0.008}{0.25} = 0.032
    $$

    The forward variance is $0.032$, corresponding to a forward volatility of $\sqrt{0.032} \approx 17.9\%$.

    **Comparison:** The spot variance (for the period $[0, 0.25]$) is $K_{\text{var}}(0.25) = 0.04$ (20% vol), while the forward variance for $[0.25, 0.50]$ is $0.032$ (17.9% vol). The forward variance is **lower** than the spot variance.

    This indicates a downward-sloping (inverted) variance term structure: the market expects volatility to decline from the current elevated level. The total variance to 6 months ($0.036 \times 0.50 = 0.018$) is a weighted average of the higher near-term variance and the lower forward variance.

---

**Exercise 7.** In practice, the variance swap replication integral is approximated by a discrete sum over traded strikes. Describe the discretization procedure and identify two sources of error: (a) truncation error from the finite strike range and (b) interpolation error between observed strikes. How does each error affect the accuracy of the VIX calculation?

??? success "Solution to Exercise 7"
    **Discretization procedure:** The continuous integral $\frac{2e^{rT}}{T}\int_0^\infty \frac{Q(K)}{K^2} \, dK$ is approximated by a Riemann sum over available strikes $K_1 < K_2 < \cdots < K_n$:

    $$
    \frac{2e^{rT}}{T}\sum_{i=1}^{n} \frac{\Delta K_i}{K_i^2} Q(K_i)
    $$

    where $\Delta K_i = (K_{i+1} - K_{i-1})/2$ for interior strikes and one-sided differences at the endpoints. Only OTM options are used: puts for $K_i < K_0$ and calls for $K_i > K_0$, where $K_0$ is the highest strike below the forward.

    **(a) Truncation error:** The integral runs from $0$ to $\infty$, but listed options cover only a finite range $[K_{\min}, K_{\max}]$. The missing contributions are:

    - **Left tail** ($K < K_{\min}$): Deep OTM puts that are not listed or have zero bids. Since $1/K^2$ is large for small $K$, even small put prices here contribute meaningfully.
    - **Right tail** ($K > K_{\max}$): Deep OTM calls that are unlisted. The $1/K^2$ weight diminishes, so this truncation is less severe.

    The truncation error causes the discrete VIX to **underestimate** the true model-free variance. The bias is most significant during periods of high skew or market stress, when deep OTM puts (which carry the heaviest $1/K^2$ weight) become valuable but may be beyond the listed strike range.

    **(b) Interpolation error:** Between listed strikes, the Riemann sum uses a step-function approximation rather than the true continuous integrand. Two sub-issues arise:

    - **Wide strike spacing:** If $\Delta K$ is large relative to the curvature of $Q(K)/K^2$, the Riemann sum is inaccurate. This is especially problematic near ATM where option prices change rapidly.
    - **Missing strikes:** If certain strikes have no active quotes (illiquid), the effective $\Delta K$ at those points is much larger, degrading accuracy.

    Interpolation error can cause either over- or under-estimation depending on the local curvature of the integrand. The error is approximately $O((\Delta K)^2)$ for smooth integrands.

    **Impact on VIX accuracy:** Truncation bias dominates during market stress (estimated at 0.1--0.5 vol points for S&P 500 under normal conditions, potentially larger during crises). Interpolation error is typically smaller but can be significant for options with wide strike spacing. The CBOE mitigates these by using all available strikes with nonzero bids and selecting two maturities that bracket 30 days.
