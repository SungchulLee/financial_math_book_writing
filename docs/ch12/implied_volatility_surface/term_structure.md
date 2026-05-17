# Term Structure of Implied Volatility


## Introduction


The **term structure of implied volatility** describes how implied volatility varies with option maturity $T$ while holding the strike $K$ (or moneyness) fixed. This temporal dimension of the volatility surface reveals market expectations about future volatility levels, mean reversion dynamics, and uncertainty about uncertainty. Unlike the smile (cross-sectional variation), the term structure encodes information about the time evolution of volatility.

## Definition and Notation


### 1. ATM Term Structure


The most commonly analyzed term structure is at-the-money (ATM):


$$
\sigma_{\text{ATM}}(T) := \sigma_{\text{IV}}(K_{\text{ATM}}(T), T)
$$



where $K_{\text{ATM}}(T) = F(T) = S_0 e^{(r-q)T}$ is the forward price at maturity $T$.

**Interpretation:** $\sigma_{\text{ATM}}(T)$ represents the market's implied volatility for an option that is currently at-the-money with maturity $T$.

### 2. Constant-Moneyness Term Structure


For fixed moneyness $m = K/F$:


$$
\sigma_{\text{IV}}(m, T) \quad \text{with } K = m \cdot S_0 e^{(r-q)T}
$$



This controls for the fact that "at-the-money" means different strike levels for different maturities.

### 3. Fixed-Strike Term Structure


For a fixed strike $K_0$:


$$
\sigma_{\text{IV}}(K_0, T) \quad \text{as } T \text{ varies}
$$



**Note:** As $T$ increases, $K_0$ moves through different moneyness levels relative to $F(T)$, mixing term structure and smile effects.

**Recommendation:** Use constant-moneyness term structure to isolate pure maturity effects.

## Typical Term Structure Shapes


### 1. Upward Sloping (Normal)


**Characteristics:**

$$
\frac{\partial \sigma_{\text{ATM}}}{\partial T} > 0
$$



Short-dated options have lower implied volatility than long-dated options.

**Interpretation:**

- **Low current volatility:** Market expects volatility to increase over time (mean reversion to long-run average)
- **Volatility mean reversion:** Current volatility below long-run mean $\theta$
- **Uncertainty accumulation:** Longer horizons have more uncertain outcomes

**Typical markets:** Stable equity markets, low-volatility regimes

**Mathematical model:** In Heston model with $v_0 < \theta$ (current variance below mean):


$$
\mathbb{E}^{\mathbb{Q}}[v_t] = v_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t}) \to \theta \quad \text{as } t \to \infty
$$



The ATM IV for small $T$ reflects $v_0$, while large $T$ reflects $\theta$.

### 2. Downward Sloping (Inverted)


**Characteristics:**

$$
\frac{\partial \sigma_{\text{ATM}}}{\partial T} < 0
$$



Short-dated options have higher implied volatility than long-dated options.

**Interpretation:**

- **High current volatility:** Market expects volatility to decrease over time
- **Elevated uncertainty:** Recent shock or crisis with expected normalization
- **Mean reversion from above:** Current volatility above long-run mean

**Typical markets:** Post-crash periods, crisis episodes, VIX spikes

**Example:** After the 2008 financial crisis, 1-month IV was 60%+ while 1-year IV was 30-40%, reflecting expected calm-down.

### 3. Humped (Non-Monotonic)


**Characteristics:**

$$
\frac{\partial \sigma_{\text{ATM}}}{\partial T} \begin{cases}
> 0 & \text{for small } T \\
< 0 & \text{for large } T
\end{cases}
$$



Implied volatility peaks at intermediate maturities (e.g., 3-6 months).

**Interpretation:**

- **Event risk at specific horizon:** Earnings announcement, election, Brexit vote, etc.
- **Short-term calm, medium-term uncertainty:** Market expects volatility spike at known future event
- **Long-term mean reversion:** After event, volatility returns to baseline

**Typical markets:** Around scheduled events (FOMC meetings, elections, earnings)

**Example:** Options expiring just after an earnings release have elevated IV compared to shorter and longer maturities.

### 4. Flat (Rare)


**Characteristics:**

$$
\sigma_{\text{ATM}}(T) \approx \text{constant}
$$



**Interpretation:**

- No expected change in volatility regime
- Market sees current volatility as persistent
- Rare in practice except as transient configuration

## Mathematical Analysis of Term Structure


### 1. Relationship to Variance Curve


Define **total variance**:


$$
w(T) := \sigma_{\text{ATM}}^2(T) \cdot T
$$



The term structure is equivalently characterized by how $w(T)$ grows with $T$:

**Upward sloping IV:**

$$
\frac{d w}{d T} = \sigma_{\text{ATM}}^2 + 2T \sigma_{\text{ATM}} \frac{d\sigma_{\text{ATM}}}{dT} > \sigma_{\text{ATM}}^2
$$


If $\frac{d\sigma_{\text{ATM}}}{dT} > 0$, total variance grows **faster than linearly**.

**Downward sloping IV:**

$$
\frac{d w}{d T} < \sigma_{\text{ATM}}^2
$$


Total variance still increases (by no-arbitrage) but **slower than linearly**.

**Constraint:** No-arbitrage requires:

$$
\frac{d w}{d T} \geq 0 \quad \Rightarrow \quad w(T) \text{ is non-decreasing}
$$



### 2. Calendar Spread Constraint


The no-arbitrage condition for calendar spreads:


$$
C(K, T_2) \geq C(K, T_1) \quad \text{for } T_2 > T_1
$$



(assuming no dividends). This implies:


$$
w(T_2) \geq w(T_1)
$$



but does **not** directly constrain $\sigma_{\text{ATM}}(T)$.

**Example:** Both scenarios are arbitrage-free:

1. $\sigma_{\text{ATM}}(T_1) = 20\%$, $\sigma_{\text{ATM}}(T_2) = 25\%$ (upward)
2. $\sigma_{\text{ATM}}(T_1) = 30\%$, $\sigma_{\text{ATM}}(T_2) = 22\%$ (downward, but $w(T_2) = 0.22^2 \cdot T_2 > w(T_1) = 0.30^2 \cdot T_1$ if $T_2$ is large enough)

### 3. Forward Volatility


The **forward implied volatility** between $T_1$ and $T_2$ is defined by:


$$
\sigma_{\text{fwd}}^2(T_1, T_2) := \frac{w(T_2) - w(T_1)}{T_2 - T_1} = \frac{\sigma_{\text{ATM}}^2(T_2) T_2 - \sigma_{\text{ATM}}^2(T_1) T_1}{T_2 - T_1}
$$



**Interpretation:** The implied volatility for the period $[T_1, T_2]$ assuming the model:


$$
\int_0^{T_1} \sigma^2(t) dt = w(T_1), \quad \int_0^{T_2} \sigma^2(t) dt = w(T_2)
$$



Thus:


$$
\int_{T_1}^{T_2} \sigma^2(t) dt = w(T_2) - w(T_1) \quad \Rightarrow \quad \sigma_{\text{fwd}}^2(T_1, T_2) \approx \text{average } \sigma^2(t) \text{ over } [T_1, T_2]
$$



### 4. Instantaneous Forward Volatility


Taking $T_2 \to T_1$:


$$
\sigma_{\text{inst}}^2(T) := \lim_{T_2 \to T_1} \sigma_{\text{fwd}}^2(T_1, T_2) = \frac{d w}{d T}\bigg|_{T=T_1}
$$



Explicitly:


$$
\sigma_{\text{inst}}^2(T) = \sigma_{\text{ATM}}^2(T) + 2T \sigma_{\text{ATM}}(T) \frac{d\sigma_{\text{ATM}}}{dT}
$$



**Interpretation:** The instantaneous volatility the market expects at time $T$ given current information.

**Relationship to term structure slope:**

- Upward sloping: $\frac{d\sigma_{\text{ATM}}}{dT} > 0 \Rightarrow \sigma_{\text{inst}}^2 > \sigma_{\text{ATM}}^2$ (forward vol exceeds spot IV)
- Downward sloping: $\frac{d\sigma_{\text{ATM}}}{dT} < 0 \Rightarrow \sigma_{\text{inst}}^2 < \sigma_{\text{ATM}}^2$ (forward vol below spot IV)

## Connection to Volatility Models


### 1. Constant Volatility (Black-Scholes)


If $\sigma(t) = \sigma_0$ (constant), then:


$$
w(T) = \sigma_0^2 T \quad \Rightarrow \quad \sigma_{\text{ATM}}(T) = \sigma_0
$$



**Flat term structure:** $\sigma_{\text{ATM}}(T)$ is independent of $T$.

### 2. Deterministic Local Volatility


For a time-dependent local volatility $\sigma_{\text{loc}}(t)$:


$$
w(T) = \int_0^T \sigma_{\text{loc}}^2(t) dt
$$




$$
\sigma_{\text{ATM}}(T) = \sqrt{\frac{1}{T} \int_0^T \sigma_{\text{loc}}^2(t) dt}
$$



The term structure reflects the **time-averaged** volatility up to maturity $T$.

**Example:** If $\sigma_{\text{loc}}(t) = \sigma_0 + \alpha t$ (linear ramp):


$$
w(T) = \sigma_0^2 T + \sigma_0 \alpha T^2 + \frac{\alpha^2 T^3}{3}
$$




$$
\sigma_{\text{ATM}}(T) = \sqrt{\sigma_0^2 + \sigma_0 \alpha T + \frac{\alpha^2 T^2}{3}}
$$



For $\alpha > 0$, term structure is upward sloping.

### 3. Stochastic Volatility (Heston)


Recall (see [§ Stochastic Volatility](../../ch14/index.md)): in Heston $dv_t = \kappa(\theta - v_t)dt + \xi\sqrt{v_t}dW^v$, the short-$T$ ATM variance satisfies $\sigma_{\text{ATM}}^2(T) \approx v_0 + (\theta - v_0)(1 - e^{-\kappa T}) + \frac{\xi^2}{4\kappa}(1 - e^{-2\kappa T})$ with initial slope $\kappa(\theta-v_0)$, so $v_0<\theta$ yields an upward-sloping term structure and $v_0>\theta$ a downward-sloping one; long-$T$ limit is $\theta + \xi^2/(4\kappa)$.

### 4. Jump-Diffusion Models


With jumps $dS_t = (r - q - \lambda m_J) S_t dt + \sigma S_t dW_t + S_t dJ_t$, the compound Poisson component adds $\lambda\mathbb{E}[J^2]T$ to total variance — linear in $T$, so the term structure stays flat. Jumps act in the strike dimension (smile curvature, see [§ Skew and Smile](skew_and_smile.md)), not the maturity dimension.

## Empirical Stylized Facts


### 1. Equity Indices (S&P 500, EURO STOXX)


**Normal regime (VIX < 20):**

- Upward sloping term structure
- 1-month ATM IV: 12-15%
- 1-year ATM IV: 18-22%
- Reflects mean reversion to long-run volatility

**Crisis regime (VIX > 30):**

- Downward sloping term structure
- 1-month ATM IV: 30-50%
- 1-year ATM IV: 20-30%
- Reflects expected calm-down

**Event-driven:**

- Humped around known events (FOMC, elections)
- Peak at event maturity

### 2. FX Markets


**G10 currencies (EUR/USD, USD/JPY):**

- Relatively flat term structure
- Less pronounced mean reversion than equities
- Occasional humps around central bank meetings

**Emerging markets:**

- More volatile term structure
- Steeper slopes reflecting sovereign risk, capital controls

### 3. Commodities


**Energy (crude oil, natural gas):**

- Highly seasonal term structure
- Humps corresponding to delivery periods
- Winter natural gas: high IV for winter maturities

**Precious metals (gold, silver):**

- Relatively flat or mildly upward sloping
- Flight-to-safety effects during crises

## Variance Swaps and Term Structure


### 1. Variance Swap Basics


Recall (see [§ Model-Free Results](../model_free_results/breeden_litzenberger_formula.md)): a variance swap pays $N_{\text{var}}(\tfrac{1}{T}\sum_i \log^2(S_{t_i}/S_{t_{i-1}}) - K_{\text{var}})$ with model-free fair strike $K_{\text{var}} = \tfrac{2e^{rT}}{T}(\int_0^F P(K)/K^2\,dK + \int_F^\infty C(K)/K^2\,dK)$ — a strike-weighted integral of OTM option prices.

### 2. Variance Term Structure


Define the variance swap rate for maturity $T$:


$$
\sigma_{\text{var}}^2(T) := K_{\text{var}}(T)
$$



The **variance term structure** $\sigma_{\text{var}}(T)$ is often smoother than the ATM IV term structure because it integrates over the entire smile.

**Relationship:**

$$
\sigma_{\text{var}}^2(T) \approx \frac{1}{T} \int_0^T \mathbb{E}[\sigma^2(t)] dt
$$



In practice:

$$
\sigma_{\text{var}}(T) \gtrsim \sigma_{\text{ATM}}(T)
$$



due to the smile (variance swaps weight OTM options more heavily).

### 3. Forward Variance


The **forward variance** between $T_1$ and $T_2$:


$$
\sigma_{\text{fwd-var}}^2(T_1, T_2) = \frac{\sigma_{\text{var}}^2(T_2) T_2 - \sigma_{\text{var}}^2(T_1) T_1}{T_2 - T_1}
$$



This can be traded via **forward-starting variance swaps**, providing a direct measure of market expectations for future volatility.

**Arbitrage-free condition:**

$$
\sigma_{\text{fwd-var}}^2(T_1, T_2) \geq 0 \quad \text{for all } T_2 > T_1
$$



Equivalently:

$$
\frac{d}{dT}\left(\sigma_{\text{var}}^2(T) \cdot T\right) \geq 0
$$



## Asymptotic Analysis


### 1. Short-Maturity Limit (T → 0)


As $T \to 0$, the ATM implied volatility converges to the **spot instantaneous volatility**:


$$
\lim_{T \to 0} \sigma_{\text{ATM}}(T) = \sigma_{\text{spot}}
$$



where $\sigma_{\text{spot}}$ is the volatility coefficient in the SDE at the current time.

**In local volatility:**

$$
\sigma_{\text{spot}} = \sigma_{\text{loc}}(S_0, 0)
$$



**In stochastic volatility:**

$$
\sigma_{\text{spot}} = \sqrt{v_0}
$$



**Expansion:** For small $T$:


$$
\sigma_{\text{ATM}}^2(T) = v_0 + a_1 T + a_2 T^2 + O(T^3)
$$



The coefficient $a_1$ is related to the drift of volatility:


$$
a_1 = \kappa(\theta - v_0) \quad \text{(Heston)}
$$



### 2. Large-Maturity Limit (T → ∞)


As $T \to \infty$, the ATM implied volatility converges to the **long-run average volatility**:


$$
\lim_{T \to \infty} \sigma_{\text{ATM}}(T) = \sigma_\infty
$$



**In mean-reverting models:**

$$
\sigma_\infty = \sqrt{\theta + \frac{\xi^2}{4\kappa}} \quad \text{(Heston)}
$$



**Ergodic interpretation:** For large $T$, the option "sees" the stationary distribution of the volatility process.

**Convergence rate:** Typically exponential:


$$
\sigma_{\text{ATM}}^2(T) - \sigma_\infty^2 \sim e^{-\lambda T}
$$



where $\lambda$ is the mean-reversion speed (e.g., $\lambda = \kappa$ in Heston).

## Practical Implications


### 1. Hedging and Risk Management


**Vega exposure:**  
A portfolio with options across maturities has **term structure risk**:

- **Parallel shift:** All maturities move together (rare)
- **Steepening:** Long-end rises more than short-end
- **Flattening:** Term structure compresses
- **Inversion:** Short-end rises, long-end falls (crisis scenarios)

**Hedging strategy:** Use variance swaps or options at multiple maturities to hedge term structure risk separately from level risk.

### 2. Volatility Arbitrage


**Carry trades:**  

- If term structure is upward sloping, sell short-dated options, buy long-dated options
- Collect theta from short-dated, benefit from mean reversion

**Event trades:**  

- If term structure shows hump at known event, compare realized volatility around event to implied
- Trade forward variance swaps to isolate event-specific vol

### 3. Model Selection


**Flat term structure:** Suggests constant or slowly varying volatility → Local volatility or simple Heston sufficient

**Steep term structure:** Requires model with strong mean reversion → Two-factor models, regime-switching

**Humped term structure:** Requires deterministic term structure or event-driven jumps → Time-dependent parameters

## Summary


The term structure of implied volatility $\sigma_{\text{ATM}}(T)$ encodes:

### 1. **Market expectations:**

- Upward sloping: Volatility expected to increase (mean reversion from below)
- Downward sloping: Volatility expected to decrease (mean reversion from above)
- Humped: Event risk at intermediate maturity

### 2. **Mathematical relationships:**


$$
w(T) = \sigma_{\text{ATM}}^2(T) \cdot T \quad \text{(total variance)}
$$




$$
\sigma_{\text{fwd}}^2(T_1, T_2) = \frac{w(T_2) - w(T_1)}{T_2 - T_1} \quad \text{(forward volatility)}
$$




$$
\sigma_{\text{inst}}^2(T) = \frac{dw}{dT} \quad \text{(instantaneous forward vol)}
$$



### 3. **No-arbitrage constraints:**


$$
\frac{dw}{dT} \geq 0 \quad \text{(calendar spreads)}
$$



### 4. **Limits:**


$$
\lim_{T \to 0} \sigma_{\text{ATM}}(T) = \sigma_{\text{spot}} \quad (\text{spot vol})
$$




$$
\lim_{T \to \infty} \sigma_{\text{ATM}}(T) = \sigma_\infty \quad (\text{long-run vol})
$$



### 5. **Connections:**

- **Variance swaps:** Provide model-free measure of variance term structure
- **Stochastic vol models:** Generate realistic term structure dynamics via mean reversion
- **Calibration:** Term structure slope constrains model parameters ($\kappa, \theta$ in Heston)

The term structure is a critical dimension of the volatility surface, revealing market beliefs about volatility evolution and serving as a key input for pricing, hedging, and risk management.

---

## Exercises

**Exercise 1.** The ATM implied volatilities for SPX options at various maturities are: 1M = 14%, 3M = 16%, 6M = 18%, 1Y = 20%. (a) Is the term structure upward or downward sloping? (b) Compute the total variance $w(T) = \sigma^2 T$ for each maturity. (c) Verify the no-arbitrage condition $w(T_2) \geq w(T_1)$ for all pairs. (d) Compute the forward volatility $\sigma_{\text{fwd}}$ between 3M and 6M.

??? success "Solution to Exercise 1"
    Given ATM implied volatilities: 1M = 14%, 3M = 16%, 6M = 18%, 1Y = 20%.

    **(a)** The term structure is **upward sloping** since $\sigma_{\text{ATM}}$ increases monotonically with maturity: $14\% < 16\% < 18\% < 20\%$. This is consistent with a low-volatility regime where the market expects volatility to mean-revert upward toward a higher long-run level.

    **(b) Total variance $w(T) = \sigma^2 T$:**

    Using $T$ in years: 1M $= 1/12$, 3M $= 3/12 = 0.25$, 6M $= 0.5$, 1Y $= 1.0$.

    $$
    w(1\text{M}) = (0.14)^2 \times \frac{1}{12} = 0.0196 \times 0.0833 = 0.001633
    $$

    $$
    w(3\text{M}) = (0.16)^2 \times 0.25 = 0.0256 \times 0.25 = 0.006400
    $$

    $$
    w(6\text{M}) = (0.18)^2 \times 0.5 = 0.0324 \times 0.5 = 0.016200
    $$

    $$
    w(1\text{Y}) = (0.20)^2 \times 1.0 = 0.0400 \times 1.0 = 0.040000
    $$

    **(c) No-arbitrage verification:** $w(T)$ must be non-decreasing:

    $$
    0.001633 < 0.006400 < 0.016200 < 0.040000 \quad \checkmark
    $$

    All adjacent pairs satisfy $w(T_2) \geq w(T_1)$, confirming no calendar arbitrage.

    **(d) Forward volatility between 3M and 6M:**

    $$
    \sigma_{\text{fwd}}^2(3\text{M}, 6\text{M}) = \frac{w(6\text{M}) - w(3\text{M})}{T_{6\text{M}} - T_{3\text{M}}} = \frac{0.016200 - 0.006400}{0.5 - 0.25} = \frac{0.009800}{0.25} = 0.039200
    $$

    $$
    \sigma_{\text{fwd}}(3\text{M}, 6\text{M}) = \sqrt{0.039200} = 0.1980 \approx 19.8\%
    $$

    The forward volatility of 19.8% between 3M and 6M exceeds both the 3M (16%) and 6M (18%) spot implied volatilities, which is characteristic of an upward-sloping term structure where the market expects volatility to accelerate in the near future.

---

**Exercise 2.** In the Heston model, the short-maturity ATM variance is $\sigma_{\text{ATM}}^2(T) \approx v_0 + \kappa(\theta - v_0) T$. For parameters $v_0 = 0.09$ (30% vol), $\kappa = 3$, and $\theta = 0.04$ (20% long-run vol): (a) compute the initial slope $\frac{d\sigma_{\text{ATM}}^2}{dT}\big|_{T=0}$; (b) is the term structure upward or downward sloping near $T = 0$? (c) What is the economic interpretation of $v_0 > \theta$?

??? success "Solution to Exercise 2"
    Given Heston parameters: $v_0 = 0.09$ ($\sigma_0 = 30\%$), $\kappa = 3$, $\theta = 0.04$ ($\sigma_\infty = 20\%$).

    **(a) Initial slope:**

    $$
    \frac{d\sigma_{\text{ATM}}^2}{dT}\bigg|_{T=0} = \kappa(\theta - v_0) = 3(0.04 - 0.09) = 3(-0.05) = -0.15
    $$

    **(b)** Since the initial slope is **negative** ($-0.15 < 0$), the term structure is **downward sloping** near $T = 0$. The ATM implied variance decreases with maturity for short-dated options.

    For the implied volatility itself:

    $$
    \frac{d\sigma_{\text{ATM}}}{dT}\bigg|_{T=0} = \frac{1}{2\sqrt{v_0}} \times \kappa(\theta - v_0) = \frac{-0.15}{2 \times 0.30} = -0.25
    $$

    So the ATM implied volatility decreases at a rate of 25 vol points per year near $T = 0$.

    **(c) Economic interpretation of $v_0 > \theta$:** The current instantaneous variance ($v_0 = 0.09$, i.e., 30% vol) exceeds the long-run mean variance ($\theta = 0.04$, i.e., 20% vol). This is a **high-volatility regime**, typically observed after a market shock, crisis, or significant uncertainty event. The market currently experiences elevated volatility but expects it to mean-revert downward toward the long-run level of 20%.

    The mean-reversion speed $\kappa = 3$ implies a half-life of $\ln(2)/\kappa \approx 0.23$ years (about 2.8 months), meaning the market expects volatility to return halfway to its long-run mean within roughly 3 months. This produces the inverted term structure: short-dated options reflect the current high volatility, while longer-dated options reflect the expected convergence to 20%.

---

**Exercise 3.** Define the instantaneous forward variance as $\sigma_{\text{inst}}^2(T) = \frac{dw}{dT}$. Given a total variance function $w(T) = 0.04T + 0.002T^2$, compute: (a) the implied volatility $\sigma_{\text{ATM}}(T) = \sqrt{w(T)/T}$ for $T = 0.25, 0.5, 1.0$; (b) the instantaneous forward variance $\sigma_{\text{inst}}^2(T)$ for the same maturities; (c) verify that $\sigma_{\text{inst}}^2(T) > \sigma_{\text{ATM}}^2(T)$ when the term structure is upward sloping.

??? success "Solution to Exercise 3"
    Given $w(T) = 0.04T + 0.002T^2$.

    **(a) Implied volatility $\sigma_{\text{ATM}}(T) = \sqrt{w(T)/T} = \sqrt{0.04 + 0.002T}$:**

    At $T = 0.25$:

    $$
    \sigma_{\text{ATM}}(0.25) = \sqrt{0.04 + 0.002(0.25)} = \sqrt{0.0405} = 0.20125 \approx 20.1\%
    $$

    At $T = 0.5$:

    $$
    \sigma_{\text{ATM}}(0.5) = \sqrt{0.04 + 0.002(0.5)} = \sqrt{0.041} = 0.20248 \approx 20.2\%
    $$

    At $T = 1.0$:

    $$
    \sigma_{\text{ATM}}(1.0) = \sqrt{0.04 + 0.002(1.0)} = \sqrt{0.042} = 0.20494 \approx 20.5\%
    $$

    The term structure is upward sloping: $20.1\% < 20.2\% < 20.5\%$.

    **(b) Instantaneous forward variance $\sigma_{\text{inst}}^2(T) = \frac{dw}{dT}$:**

    $$
    \frac{dw}{dT} = 0.04 + 0.004T
    $$

    At $T = 0.25$:

    $$
    \sigma_{\text{inst}}^2(0.25) = 0.04 + 0.004(0.25) = 0.041
    $$

    At $T = 0.5$:

    $$
    \sigma_{\text{inst}}^2(0.5) = 0.04 + 0.004(0.5) = 0.042
    $$

    At $T = 1.0$:

    $$
    \sigma_{\text{inst}}^2(1.0) = 0.04 + 0.004(1.0) = 0.044
    $$

    **(c) Verification that $\sigma_{\text{inst}}^2(T) > \sigma_{\text{ATM}}^2(T)$:**

    | $T$ | $\sigma_{\text{ATM}}^2(T) = 0.04 + 0.002T$ | $\sigma_{\text{inst}}^2(T) = 0.04 + 0.004T$ | Difference |
    |---|---|---|---|
    | 0.25 | 0.0405 | 0.041 | +0.0005 |
    | 0.5 | 0.041 | 0.042 | +0.001 |
    | 1.0 | 0.042 | 0.044 | +0.002 |

    At every maturity, $\sigma_{\text{inst}}^2(T) > \sigma_{\text{ATM}}^2(T)$. This is consistent with the general relationship: when the term structure is upward sloping ($\frac{d\sigma_{\text{ATM}}}{dT} > 0$), the instantaneous forward variance exceeds the spot implied variance because the forward rate must be above the average to pull the average upward.

---

**Exercise 4.** During a market crisis, the VIX spikes to 45 and the term structure inverts: 1M ATM IV = 45%, 3M = 35%, 6M = 28%, 1Y = 24%. (a) Compute total variances and verify no-arbitrage. (b) Compute forward volatilities for each adjacent pair. (c) What is the market's implied expectation for volatility between 6M and 1Y? (d) Is this consistent with mean reversion?

??? success "Solution to Exercise 4"
    Given crisis ATM IVs: 1M = 45%, 3M = 35%, 6M = 28%, 1Y = 24%.

    **(a) Total variances:**

    $$
    w(1\text{M}) = (0.45)^2 / 12 = 0.2025 / 12 = 0.016875
    $$

    $$
    w(3\text{M}) = (0.35)^2 \times 0.25 = 0.1225 \times 0.25 = 0.030625
    $$

    $$
    w(6\text{M}) = (0.28)^2 \times 0.5 = 0.0784 \times 0.5 = 0.039200
    $$

    $$
    w(1\text{Y}) = (0.24)^2 \times 1.0 = 0.0576
    $$

    **No-arbitrage verification:**

    $$
    0.016875 < 0.030625 < 0.039200 < 0.057600 \quad \checkmark
    $$

    Despite the inverted term structure in IV, total variance is strictly increasing, so there is no calendar arbitrage.

    **(b) Forward volatilities:**

    **1M to 3M** ($T_1 = 1/12$, $T_2 = 3/12$):

    $$
    \sigma_{\text{fwd}}^2 = \frac{0.030625 - 0.016875}{0.25 - 0.0833} = \frac{0.013750}{0.1667} = 0.082484
    $$

    $$
    \sigma_{\text{fwd}} = \sqrt{0.082484} = 0.2872 \approx 28.7\%
    $$

    **3M to 6M** ($T_1 = 0.25$, $T_2 = 0.5$):

    $$
    \sigma_{\text{fwd}}^2 = \frac{0.039200 - 0.030625}{0.25} = \frac{0.008575}{0.25} = 0.034300
    $$

    $$
    \sigma_{\text{fwd}} = \sqrt{0.034300} = 0.1852 \approx 18.5\%
    $$

    **6M to 1Y** ($T_1 = 0.5$, $T_2 = 1.0$):

    $$
    \sigma_{\text{fwd}}^2 = \frac{0.057600 - 0.039200}{0.5} = \frac{0.018400}{0.5} = 0.036800
    $$

    $$
    \sigma_{\text{fwd}} = \sqrt{0.036800} = 0.1918 \approx 19.2\%
    $$

    **(c)** The market's implied expectation for volatility between 6M and 1Y is approximately **19.2%**. This is close to a typical non-crisis volatility level (normal regime ATM IV of 14-18%), indicating the market expects near-complete normalization by the second half of the year.

    **(d)** This is fully consistent with **mean reversion**. The forward volatilities decline sharply from 28.7% (1M-3M period) to 18.5% (3M-6M) and then stabilize around 19.2% (6M-1Y), approaching the long-run average. The steepest decline occurs in the near term (the market expects the crisis shock to dissipate relatively quickly), while the longer-horizon forward vol settles near the ergodic mean. This pattern is precisely what mean-reverting stochastic volatility models (such as Heston with $v_0 \gg \theta$) produce.

---

**Exercise 5.** A variance swap has fair strike $K_{\text{var}}(T)$ related to the integral of option prices across strikes. Explain why $\sigma_{\text{var}}(T) \geq \sigma_{\text{ATM}}(T)$ in general, and under what conditions would equality hold. Relate this to Jensen's inequality and the convexity of the variance swap payoff.

??? success "Solution to Exercise 5"
    The variance swap rate integrates option prices across all strikes:

    $$
    \sigma_{\text{var}}^2(T) = \frac{2e^{rT}}{T}\left(\int_0^F \frac{P(K)}{K^2}dK + \int_F^\infty \frac{C(K)}{K^2}dK\right)
    $$

    This is a weighted average of implied volatilities across all strikes, with weights proportional to $1/K^2$.

    **Why $\sigma_{\text{var}}(T) \geq \sigma_{\text{ATM}}(T)$:** The variance swap rate can be expressed as:

    $$
    \sigma_{\text{var}}^2(T) = \int_0^\infty \sigma_{\text{IV}}^2(K, T) \cdot \omega(K) \, dK
    $$

    where $\omega(K)$ are positive weights. By Jensen's inequality, since implied volatility is a convex function of strike (the smile has positive curvature), the weighted average of $\sigma_{\text{IV}}^2$ across all strikes exceeds the value at the ATM point.

    More precisely, if the smile is U-shaped with minimum at ATM, then OTM options (which receive positive weight in the variance swap integral) have $\sigma_{\text{IV}}(K) \geq \sigma_{\text{ATM}}$. Therefore the integral over all strikes yields a value at least as large as the ATM implied variance:

    $$
    \sigma_{\text{var}}^2(T) = \sigma_{\text{ATM}}^2(T) + \underbrace{\int [\sigma_{\text{IV}}^2(K) - \sigma_{\text{ATM}}^2] \omega(K) dK}_{\geq 0 \text{ when smile is present}}
    $$

    **Equality holds when** the smile is perfectly flat: $\sigma_{\text{IV}}(K, T) = \sigma_{\text{ATM}}(T)$ for all $K$. In this case, every strike has the same IV, so the weighted average equals the ATM value. This corresponds exactly to the Black-Scholes model with constant volatility. In the real market, the smile is always present (non-flat), so strict inequality $\sigma_{\text{var}}(T) > \sigma_{\text{ATM}}(T)$ always holds.

    **Connection to Jensen's inequality:** The variance swap payoff is $\frac{1}{T}\int_0^T \sigma_t^2 \, dt - K_{\text{var}}$, which is linear in realized variance. However, the replication portfolio involves options whose prices are convex functions of implied volatility. The convexity of the smile means that the integral of option prices (which determines the variance swap rate) exceeds the price of a single ATM option (which determines $\sigma_{\text{ATM}}$), analogous to Jensen's inequality $\mathbb{E}[f(X)] \geq f(\mathbb{E}[X])$ for convex $f$.

---

**Exercise 6.** Compare the term structure behavior of the following models: (a) Black-Scholes (constant volatility), (b) deterministic local volatility $\sigma_{\text{loc}}(t) = 0.15 + 0.01t$, and (c) Heston with $v_0 = 0.0225$, $\theta = 0.04$, $\kappa = 2$. For each, describe the shape of the term structure (flat, upward, downward) and compute $\sigma_{\text{ATM}}(T)$ at $T = 0.5$ and $T = 2.0$.

??? success "Solution to Exercise 6"
    **(a) Black-Scholes (constant volatility $\sigma_0$):**

    $$
    \sigma_{\text{ATM}}(T) = \sigma_0 \quad \text{for all } T
    $$

    The term structure is **flat**. At $T = 0.5$ and $T = 2.0$, $\sigma_{\text{ATM}} = \sigma_0$ (the same constant value).

    **(b) Deterministic local volatility $\sigma_{\text{loc}}(t) = 0.15 + 0.01t$:**

    $$
    \sigma_{\text{ATM}}(T) = \sqrt{\frac{1}{T}\int_0^T (0.15 + 0.01t)^2 dt}
    $$

    Expanding the integrand:

    $$
    \int_0^T (0.0225 + 0.003t + 0.0001t^2) dt = 0.0225T + 0.0015T^2 + \frac{0.0001T^3}{3}
    $$

    At $T = 0.5$:

    $$
    \sigma_{\text{ATM}}^2(0.5) = \frac{0.01125 + 0.000375 + 0.00000417}{0.5} = \frac{0.01163}{0.5} = 0.02326
    $$

    $$
    \sigma_{\text{ATM}}(0.5) = \sqrt{0.02326} = 0.1525 \approx 15.3\%
    $$

    At $T = 2.0$:

    $$
    \sigma_{\text{ATM}}^2(2.0) = \frac{0.0450 + 0.0060 + 0.000267}{2.0} = \frac{0.05127}{2.0} = 0.02563
    $$

    $$
    \sigma_{\text{ATM}}(2.0) = \sqrt{0.02563} = 0.1601 \approx 16.0\%
    $$

    The term structure is **upward sloping** ($15.3\% < 16.0\%$), reflecting the linearly increasing local volatility.

    **(c) Heston model** with $v_0 = 0.0225$ ($\sigma_0 = 15\%$), $\theta = 0.04$ ($\sigma_\infty = 20\%$), $\kappa = 2$:

    Using the approximation $\sigma_{\text{ATM}}^2(T) \approx v_0 + (\theta - v_0)(1 - e^{-\kappa T})$:

    At $T = 0.5$:

    $$
    \sigma_{\text{ATM}}^2(0.5) \approx 0.0225 + (0.04 - 0.0225)(1 - e^{-1.0}) = 0.0225 + 0.0175(1 - 0.3679)
    $$

    $$
    = 0.0225 + 0.0175 \times 0.6321 = 0.0225 + 0.01106 = 0.03356
    $$

    $$
    \sigma_{\text{ATM}}(0.5) = \sqrt{0.03356} = 0.1832 \approx 18.3\%
    $$

    At $T = 2.0$:

    $$
    \sigma_{\text{ATM}}^2(2.0) \approx 0.0225 + 0.0175(1 - e^{-4.0}) = 0.0225 + 0.0175(1 - 0.01832)
    $$

    $$
    = 0.0225 + 0.0175 \times 0.9817 = 0.0225 + 0.01718 = 0.03968
    $$

    $$
    \sigma_{\text{ATM}}(2.0) = \sqrt{0.03968} = 0.1992 \approx 19.9\%
    $$

    The term structure is **upward sloping** ($18.3\% < 19.9\%$), reflecting mean reversion from below ($v_0 = 0.0225 < \theta = 0.04$). The Heston model produces a steeper term structure than the deterministic case because mean reversion pulls the variance toward a significantly higher long-run level.

---

**Exercise 7.** An options trader notices a humped term structure in natural gas options with peak IV at the 6-month maturity corresponding to the upcoming winter heating season. (a) Explain the economic reasoning behind this hump. (b) The trader wants to trade the view that the hump is overpriced. Describe a forward variance swap or calendar spread strategy that isolates the event-specific volatility. (c) What risks does this trade carry?

??? success "Solution to Exercise 7"
    **(a) Economic reasoning behind the hump:** Natural gas demand is highly seasonal. The winter heating season (roughly November through March) drives peak demand, and supply disruptions (cold snaps, pipeline constraints, storage shortfalls) during this period can cause extreme price spikes. The 6-month maturity coincides with the upcoming winter, so options expiring during the heating season command elevated implied volatility because:

    - **Demand uncertainty:** The severity of winter weather is unknown, creating wide uncertainty in consumption levels.
    - **Supply constraints:** Natural gas storage levels may be insufficient for extreme cold, and pipeline capacity limits prevent rapid supply response.
    - **Price spike history:** Natural gas has experienced dramatic winter price spikes (e.g., the February 2021 Texas freeze), and the market prices the possibility of similar events.
    - **Mean reversion after winter:** Once the heating season ends, demand normalizes, so longer-dated options (beyond winter) have lower IV reflecting expected return to baseline volatility.

    The result is a hump: short-dated options reflect current (moderate) volatility, 6-month options reflect winter event risk, and longer-dated options reflect the post-winter calm.

    **(b) Strategy to trade the view that the hump is overpriced:**

    **Forward variance swap approach:** Enter a short forward-starting variance swap that covers the winter period. Specifically:

    - Go long a variance swap with maturity at 3 months (pre-winter, lower variance strike)
    - Go short a variance swap with maturity at 6 months (through winter, higher variance strike)

    The net position is equivalent to selling forward variance for the 3-month to 6-month window, isolating the winter-specific volatility premium.

    **Calendar spread approach:** Sell a straddle (or strangle) expiring at the 6-month maturity (peak of the hump) and buy a straddle expiring at the 3-month maturity and another at the 9-month or 1-year maturity to hedge. This is short the hump: the trade profits if realized volatility during the winter period is lower than the implied level.

    More precisely, the trader could sell the 6-month ATM straddle and buy a weighted combination of the 3-month and 9-month straddles such that the net vega exposure to a parallel shift in the term structure is zero, isolating the curvature (hump) component.

    **(c) Risks:**

    - **Realized volatility exceeds implied:** If the winter is unusually severe (extreme cold, supply disruptions, storage depletion), realized volatility during the heating season could exceed the elevated implied level, causing large losses on the short variance position.
    - **Gap risk:** Natural gas prices can gap sharply (e.g., doubling overnight during a polar vortex), creating losses that exceed what continuous hedging models predict.
    - **Liquidity risk:** Natural gas options and variance swaps may become illiquid during extreme weather events, making it difficult to close or adjust the position.
    - **Model risk:** The term structure hump may reflect genuine event risk rather than overpricing, and the trader's view may simply be wrong about the probability of extreme winter outcomes.
    - **Basis risk:** If using calendar spreads rather than variance swaps, the hedge between different maturities may not perfectly isolate the hump component, leaving residual exposure to parallel shifts in the term structure.
