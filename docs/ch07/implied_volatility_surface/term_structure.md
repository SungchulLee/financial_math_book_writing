# Term Structure of Implied Volatility

## Introduction

The **term structure of implied volatility** describes how implied volatility varies with option maturity $T$ while holding the strike $K$ (or moneyness) fixed. This temporal dimension of the volatility surface reveals market expectations about future volatility levels, mean reversion dynamics, and uncertainty about uncertainty. Unlike the smile (cross-sectional variation), the term structure encodes information about the time evolution of volatility.

## Definition and Notation

### ATM Term Structure

The most commonly analyzed term structure is at-the-money (ATM):


$$
\sigma_{\text{ATM}}(T) := \sigma_{\text{IV}}(K_{\text{ATM}}(T), T)
$$



where $K_{\text{ATM}}(T) = F(T) = S_0 e^{(r-q)T}$ is the forward price at maturity $T$.

**Interpretation:** $\sigma_{\text{ATM}}(T)$ represents the market's implied volatility for an option that is currently at-the-money with maturity $T$.

### Constant-Moneyness Term Structure

For fixed moneyness $m = K/F$:


$$
\sigma_{\text{IV}}(m, T) \quad \text{with } K = m \cdot S_0 e^{(r-q)T}
$$



This controls for the fact that "at-the-money" means different strike levels for different maturities.

### Fixed-Strike Term Structure

For a fixed strike $K_0$:


$$
\sigma_{\text{IV}}(K_0, T) \quad \text{as } T \text{ varies}
$$



**Note:** As $T$ increases, $K_0$ moves through different moneyness levels relative to $F(T)$, mixing term structure and smile effects.

**Recommendation:** Use constant-moneyness term structure to isolate pure maturity effects.

## Typical Term Structure Shapes

### Upward Sloping (Normal)

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

### Downward Sloping (Inverted)

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

### Humped (Non-Monotonic)

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

### Flat (Rare)

**Characteristics:**

$$
\sigma_{\text{ATM}}(T) \approx \text{constant}
$$



**Interpretation:**
- No expected change in volatility regime
- Market sees current volatility as persistent
- Rare in practice except as transient configuration

## Mathematical Analysis of Term Structure

### Relationship to Variance Curve

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



### Calendar Spread Constraint

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

### Forward Volatility

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



### Instantaneous Forward Volatility

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

### Constant Volatility (Black-Scholes)

If $\sigma(t) = \sigma_0$ (constant), then:


$$
w(T) = \sigma_0^2 T \quad \Rightarrow \quad \sigma_{\text{ATM}}(T) = \sigma_0
$$



**Flat term structure:** $\sigma_{\text{ATM}}(T)$ is independent of $T$.

### Deterministic Local Volatility

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

### Stochastic Volatility (Heston)

The Heston model:


$$
\begin{align}
dS_t &= (r - q) S_t dt + \sqrt{v_t} S_t dW_t^S \\
dv_t &= \kappa(\theta - v_t) dt + \xi \sqrt{v_t} dW_t^v \\
d\langle W^S, W^v \rangle_t &= \rho dt
\end{align}
$$



ATM term structure for small $T$:


$$
\sigma_{\text{ATM}}^2(T) \approx v_0 + (\theta - v_0)(1 - e^{-\kappa T}) + \frac{\xi^2}{4\kappa}(1 - e^{-2\kappa T})
$$



**Limits:**
- Short maturity: $\sigma_{\text{ATM}}^2(T) \approx v_0$ (spot variance)
- Long maturity: $\sigma_{\text{ATM}}^2(T) \to \theta + \frac{\xi^2}{4\kappa}$ (long-run level + vol-of-vol effect)

**Slope:**

$$
\frac{d\sigma_{\text{ATM}}^2}{dT}\bigg|_{T=0} = \kappa(\theta - v_0)
$$



- If $v_0 < \theta$: Upward sloping (mean reversion from below)
- If $v_0 > \theta$: Downward sloping (mean reversion from above)

### Jump-Diffusion Models

With jumps in the underlying:


$$
dS_t = (r - q - \lambda m_J) S_t dt + \sigma S_t dW_t + S_t dJ_t
$$



where $J_t$ is a compound Poisson process with intensity $\lambda$ and jump size mean $m_J$.

**Effect on term structure:** Jumps contribute a constant to the total variance:


$$
w(T) = \sigma^2 T + \lambda \mathbb{E}[J^2] T
$$



The term structure remains flat (both components scale linearly with $T$), but the **smile** exhibits curvature.

**Implication:** Jumps affect strike dimension (smile shape) more than maturity dimension (term structure).

## Empirical Stylized Facts

### Equity Indices (S&P 500, EURO STOXX)

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

### FX Markets

**G10 currencies (EUR/USD, USD/JPY):**
- Relatively flat term structure
- Less pronounced mean reversion than equities
- Occasional humps around central bank meetings

**Emerging markets:**
- More volatile term structure
- Steeper slopes reflecting sovereign risk, capital controls

### Commodities

**Energy (crude oil, natural gas):**
- Highly seasonal term structure
- Humps corresponding to delivery periods
- Winter natural gas: high IV for winter maturities

**Precious metals (gold, silver):**
- Relatively flat or mildly upward sloping
- Flight-to-safety effects during crises

## Variance Swaps and Term Structure

### Variance Swap Basics

A **variance swap** pays the difference between realized variance and a fixed strike $K_{\text{var}}$:


$$
\text{Payoff} = N_{\text{var}} \left( \frac{1}{T} \sum_{i=1}^n \log^2\frac{S_{t_i}}{S_{t_{i-1}}} - K_{\text{var}} \right)
$$



where $N_{\text{var}}$ is the variance notional.

The fair strike is:


$$
K_{\text{var}} = \frac{2 e^{rT}}{T} \left( \int_0^F \frac{P(K)}{K^2} dK + \int_F^\infty \frac{C(K)}{K^2} dK \right)
$$



This integral of option prices across strikes gives a **model-free implied variance**.

### Variance Term Structure

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

### Forward Variance

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

### Short-Maturity Limit ($T \to 0$)

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



### Large-Maturity Limit ($T \to \infty$)

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

### Hedging and Risk Management

**Vega exposure:**  
A portfolio with options across maturities has **term structure risk**:
- **Parallel shift:** All maturities move together (rare)
- **Steepening:** Long-end rises more than short-end
- **Flattening:** Term structure compresses
- **Inversion:** Short-end rises, long-end falls (crisis scenarios)

**Hedging strategy:** Use variance swaps or options at multiple maturities to hedge term structure risk separately from level risk.

### Volatility Arbitrage

**Carry trades:**  
- If term structure is upward sloping, sell short-dated options, buy long-dated options
- Collect theta from short-dated, benefit from mean reversion

**Event trades:**  
- If term structure shows hump at known event, compare realized volatility around event to implied
- Trade forward variance swaps to isolate event-specific vol

### Model Selection

**Flat term structure:** Suggests constant or slowly varying volatility → Local volatility or simple Heston sufficient

**Steep term structure:** Requires model with strong mean reversion → Two-factor models, regime-switching

**Humped term structure:** Requires deterministic term structure or event-driven jumps → Time-dependent parameters

## Summary

The term structure of implied volatility $\sigma_{\text{ATM}}(T)$ encodes:

### **Market expectations:**
- Upward sloping: Volatility expected to increase (mean reversion from below)
- Downward sloping: Volatility expected to decrease (mean reversion from above)
- Humped: Event risk at intermediate maturity

### **Mathematical relationships:**

$$
w(T) = \sigma_{\text{ATM}}^2(T) \cdot T \quad \text{(total variance)}
$$




$$
\sigma_{\text{fwd}}^2(T_1, T_2) = \frac{w(T_2) - w(T_1)}{T_2 - T_1} \quad \text{(forward volatility)}
$$




$$
\sigma_{\text{inst}}^2(T) = \frac{dw}{dT} \quad \text{(instantaneous forward vol)}
$$



### **No-arbitrage constraints:**

$$
\frac{dw}{dT} \geq 0 \quad \text{(calendar spreads)}
$$



### **Limits:**

$$
\lim_{T \to 0} \sigma_{\text{ATM}}(T) = \sigma_{\text{spot}} \quad (\text{spot vol})
$$




$$
\lim_{T \to \infty} \sigma_{\text{ATM}}(T) = \sigma_\infty \quad (\text{long-run vol})
$$



### **Connections:**
- **Variance swaps:** Provide model-free measure of variance term structure
- **Stochastic vol models:** Generate realistic term structure dynamics via mean reversion
- **Calibration:** Term structure slope constrains model parameters ($\kappa, \theta$ in Heston)

The term structure is a critical dimension of the volatility surface, revealing market beliefs about volatility evolution and serving as a key input for pricing, hedging, and risk management.
