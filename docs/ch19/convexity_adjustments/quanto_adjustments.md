# Quanto Adjustments

A **quanto** (quantity-adjusted) derivative pays the holder a rate or price denominated in one currency but settled in a different currency at a fixed exchange rate. For example, a quanto cap might pay the EUR EURIBOR rate but settle in USD. Because the payoff depends on a foreign rate while the settlement currency differs, the pricing measure must account for the correlation between the foreign rate and the exchange rate. This correlation-driven correction is the **quanto adjustment**. This section derives the adjustment from a cross-currency measure change, presents the quanto correction formula, and applies it to caps and floors.

---

## Quanto Products

### Standard vs. Quanto Payoff

**Standard caplet** (domestic currency, domestic rate):

$$
\delta_i \max(L_i^d(T_i) - K, 0)
$$

paid in the domestic currency at $T_{i+1}$. No cross-currency issues arise.

**Quanto caplet** (foreign rate, domestic settlement):

$$
\delta_i \max(L_i^f(T_i) - K, 0) \quad \text{paid in domestic currency at } T_{i+1}
$$

The payoff depends on the **foreign** LIBOR rate $L_i^f$ but is paid in the **domestic** currency at a predetermined exchange rate (typically 1:1 or a contractual rate). No actual FX conversion takes place at maturity.

### Why a Quanto Adjustment Is Needed

The foreign forward rate $L_i^f(t)$ is a martingale under the **foreign** $T_{i+1}$-forward measure $\mathbb{Q}^{f,T_{i+1}}$ (with numéraire $P^f(t, T_{i+1})$). Pricing the quanto caplet requires computing the expectation under the **domestic** $T_{i+1}$-forward measure $\mathbb{Q}^{d,T_{i+1}}$ (with numéraire $P^d(t, T_{i+1})$). Since these measures differ, the foreign rate acquires a drift adjustment under the domestic measure. This drift is the quanto adjustment.

---

## Cross-Currency Measure Change

### Setup

Let:

- $P^d(t, T)$, $P^f(t, T)$: domestic and foreign zero-coupon bond prices
- $X(t)$: spot exchange rate (units of domestic currency per unit of foreign currency)
- $L_i^f(t)$: foreign forward LIBOR rate for period $[T_i, T_{i+1}]$

### The Exchange Rate Process

Under the domestic risk-neutral measure $\mathbb{Q}^d$, the exchange rate follows:

$$
\frac{dX(t)}{X(t)} = (r^d(t) - r^f(t)) \, dt + \sigma_X(t) \, dW_X^d(t)
$$

where $\sigma_X(t)$ is the exchange rate volatility and $W_X^d$ is a Brownian motion under $\mathbb{Q}^d$.

### Radon--Nikodym Derivative

The measure change from $\mathbb{Q}^{f,T_{i+1}}$ to $\mathbb{Q}^{d,T_{i+1}}$ involves two steps:

**Step 1:** Change from foreign risk-neutral $\mathbb{Q}^f$ to domestic risk-neutral $\mathbb{Q}^d$. The Radon--Nikodym derivative is:

$$
\frac{d\mathbb{Q}^d}{d\mathbb{Q}^f}\bigg|_{\mathcal{F}_t} = \frac{X(t) \, B^d(t)^{-1}}{X(0) \, B^f(t)^{-1} \cdot (B^d(0)/B^f(0))}
$$

where $B^d$, $B^f$ are the domestic and foreign money market accounts.

**Step 2:** Change from $\mathbb{Q}^d$ to $\mathbb{Q}^{d,T_{i+1}}$ via the standard forward measure change:

$$
\frac{d\mathbb{Q}^{d,T_{i+1}}}{d\mathbb{Q}^d}\bigg|_{\mathcal{F}_t} = \frac{P^d(t, T_{i+1})}{B^d(t) \, P^d(0, T_{i+1})}
$$

### Girsanov Drift Adjustment

Under $\mathbb{Q}^{f,T_{i+1}}$, the foreign forward rate is a driftless martingale:

$$
\frac{dL_i^f(t)}{L_i^f(t)} = \sigma_i^f(t) \, dW_i^{f,T_{i+1}}(t)
$$

Under $\mathbb{Q}^{d,T_{i+1}}$, applying Girsanov's theorem for the combined measure change, a drift correction appears:

$$
\frac{dL_i^f(t)}{L_i^f(t)} = \mu_{\text{quanto}}(t) \, dt + \sigma_i^f(t) \, dW_i^{d,T_{i+1}}(t)
$$

where the **quanto drift** is:

$$
\mu_{\text{quanto}}(t) = -\rho_{L,X}(t) \, \sigma_i^f(t) \, \sigma_X(t)
$$

Here $\rho_{L,X}(t)$ is the instantaneous correlation between the foreign forward rate $L_i^f$ and the exchange rate $X$.

---

## The Quanto Correction Formula

### Derivation

Since $L_i^f(t)$ is lognormal under $\mathbb{Q}^{f,T_{i+1}}$ and acquires a constant drift $\mu_{\text{quanto}}$ under $\mathbb{Q}^{d,T_{i+1}}$, the terminal distribution under the domestic measure is:

$$
L_i^f(T_i) = L_i^f(0) \exp\!\left(\mu_{\text{quanto}} T_i - \frac{1}{2}(\sigma_i^f)^2 T_i + \sigma_i^f W_i^{d,T_{i+1}}(T_i)\right)
$$

The expectation under the domestic forward measure is:

$$
\mathbb{E}^{\mathbb{Q}^{d,T_{i+1}}}[L_i^f(T_i)] = L_i^f(0) \, e^{\mu_{\text{quanto}} T_i}
$$

### The Quanto-Adjusted Forward Rate

!!! info "Theorem (Quanto Forward Rate Adjustment)"
    Under the domestic $T_{i+1}$-forward measure, the quanto-adjusted foreign forward rate is:

    $$
    L_i^{f,\text{quanto}}(0) = L_i^f(0) \, \exp\!\left(-\rho_{L,X} \, \sigma_i^f \, \sigma_X \, T_i\right)
    $$

    For small corrections, the first-order approximation gives:

    $$
    L_i^{f,\text{quanto}}(0) \approx L_i^f(0) \left(1 - \rho_{L,X} \, \sigma_i^f \, \sigma_X \, T_i\right)
    $$

The quanto correction is:

$$
\boxed{\text{Quanto Adj} = -\rho_{L,X} \, \sigma_i^f \, \sigma_X \, T_i \cdot L_i^f(0)}
$$

### Sign and Interpretation

- If $\rho_{L,X} > 0$ (foreign rates and the exchange rate are positively correlated, meaning when foreign rates rise, the foreign currency strengthens), the quanto adjustment is **negative**: the quanto forward rate is lower than the standard foreign forward rate
- If $\rho_{L,X} < 0$, the adjustment is **positive**
- If $\rho_{L,X} = 0$, there is no quanto effect

**Financial intuition:** When $\rho_{L,X} > 0$, high foreign rates coincide with a strong foreign currency. A quanto product does not benefit from this FX effect (settlement is at a fixed rate), so the effective forward rate is lower. The adjustment compensates for the missing FX gain.

---

## Quanto Cap and Floor Pricing

### Quanto Caplet via Black's Formula

The quanto caplet is priced using Black's formula with the **quanto-adjusted forward rate** as the underlying:

$$
\text{Quanto Caplet}_i = \delta_i \, P^d(0, T_{i+1}) \left[L_i^{f,\text{quanto}}(0) \, N(d_1) - K \, N(d_2)\right]
$$

where:

$$
d_1 = \frac{\ln(L_i^{f,\text{quanto}}(0)/K) + \frac{1}{2}(\sigma_i^f)^2 T_i}{\sigma_i^f \sqrt{T_i}}
$$

$$
d_2 = d_1 - \sigma_i^f \sqrt{T_i}
$$

Note that:

- The **discounting** uses the domestic zero-coupon bond $P^d(0, T_{i+1})$ (settlement in domestic currency)
- The **forward rate** is the quanto-adjusted foreign rate $L_i^{f,\text{quanto}}(0)$
- The **volatility** is the foreign rate volatility $\sigma_i^f$ (unchanged by the quanto adjustment)

### Quanto Floorlet

$$
\text{Quanto Floorlet}_i = \delta_i \, P^d(0, T_{i+1}) \left[K \, N(-d_2) - L_i^{f,\text{quanto}}(0) \, N(-d_1)\right]
$$

### Quanto Cap

$$
\text{Quanto Cap} = \sum_{i=0}^{n-1} \text{Quanto Caplet}_i
$$

Each caplet uses its own quanto-adjusted forward rate with the appropriate fixing time $T_i$.

---

## Worked Example

??? example "Quanto Cap Pricing"

    **Setup:** A USD-settled cap on 6-month EUR EURIBOR with strike 3.0%, notional EUR 10 million (settled in USD at 1:1 rate), 2-year maturity with semiannual caplets.

    **Parameters:**

    - EUR forward rates: $L_1^f(0) = 3.2\%$, $L_2^f(0) = 3.4\%$, $L_3^f(0) = 3.5\%$
    - EUR caplet vols: $\sigma_1^f = 20\%$, $\sigma_2^f = 21\%$, $\sigma_3^f = 22\%$
    - EUR/USD FX vol: $\sigma_X = 10\%$
    - Correlation (EUR rates, EUR/USD): $\rho_{L,X} = 0.30$
    - Fixing times: $T_1 = 0.5$, $T_2 = 1.0$, $T_3 = 1.5$
    - Day count fraction: $\delta = 0.5$
    - USD discount factors: $P^d(0, 1.0) = 0.960$, $P^d(0, 1.5) = 0.941$, $P^d(0, 2.0) = 0.922$

    **Step 1: Compute quanto-adjusted forward rates**

    For caplet 1 ($T_1 = 0.5$):

    $L_1^{f,q} = 0.032 \times \exp(-0.30 \times 0.20 \times 0.10 \times 0.5) = 0.032 \times e^{-0.003} \approx 0.032 \times 0.9970 = 3.190\%$

    For caplet 2 ($T_2 = 1.0$):

    $L_2^{f,q} = 0.034 \times \exp(-0.30 \times 0.21 \times 0.10 \times 1.0) = 0.034 \times e^{-0.0063} \approx 0.034 \times 0.9937 = 3.379\%$

    For caplet 3 ($T_3 = 1.5$):

    $L_3^{f,q} = 0.035 \times \exp(-0.30 \times 0.22 \times 0.10 \times 1.5) = 0.035 \times e^{-0.0099} \approx 0.035 \times 0.9901 = 3.465\%$

    **Step 2: Price each quanto caplet using Black's formula**

    For caplet 1: $F = 3.190\%$, $K = 3.0\%$, $\sigma = 20\%$, $T = 0.5$

    $d_1 = \frac{\ln(3.190/3.0) + 0.5 \times 0.04 \times 0.5}{0.20\sqrt{0.5}} = \frac{0.0615 + 0.01}{0.1414} = 0.506$

    $d_2 = 0.506 - 0.1414 = 0.365$

    $\text{Caplet}_1 = 0.5 \times 0.960 \times [0.03190 \times 0.694 - 0.030 \times 0.643] = 0.480 \times [0.02214 - 0.01928] = 0.480 \times 0.00286 = 0.001373$

    **Step 3: Compare with non-quanto caplet**

    Without quanto adjustment: $F = 3.200\%$, giving a slightly higher caplet value. The quanto adjustment reduces the forward rate by about 1 bp, translating to a price reduction of approximately 0.5--1% of the caplet value.

    **Observation:** The quanto adjustment is small (less than 1 bp on the forward rate) for this 6-month fixing horizon but grows linearly with time, reaching about 3 bp for a 5-year quanto cap.

---

## Sensitivity Analysis

### Dependence on Parameters

The quanto correction $\Delta L = -\rho_{L,X} \sigma_i^f \sigma_X T_i L_i^f(0)$ is:

- **Linear in correlation** $\rho_{L,X}$: the most important parameter
- **Linear in FX volatility** $\sigma_X$: higher FX vol means larger adjustment
- **Linear in rate volatility** $\sigma_i^f$: higher rate vol amplifies the effect
- **Linear in time** $T_i$: grows with the fixing horizon
- **Linear in the rate level** $L_i^f(0)$: proportional correction

### Typical Magnitudes

| Fixing Horizon | Rate Vol | FX Vol | Correlation | Quanto Adj (bps) |
|---|---|---|---|---|
| 1Y | 20% | 10% | 0.30 | $-0.6$ |
| 3Y | 20% | 10% | 0.30 | $-1.8$ |
| 5Y | 20% | 10% | 0.30 | $-3.0$ |
| 5Y | 20% | 10% | 0.50 | $-5.0$ |
| 10Y | 25% | 12% | 0.40 | $-12.0$ |

For long-dated quanto products, the adjustment can be substantial.

### Correlation Uncertainty

!!! warning "Correlation Risk"
    The quanto adjustment depends critically on the rate-FX correlation $\rho_{L,X}$, which is notoriously difficult to estimate and unstable over time. Historical estimates can vary significantly depending on the estimation window. A 10-percentage-point change in correlation changes the 5-year quanto adjustment by about 1 bp in the forward rate. For large quanto portfolios, this uncertainty is a material source of model risk.

---

## Extensions

### Quanto Swaptions

A quanto swaption pays the foreign swap rate settled in domestic currency. The adjustment follows the same principle: the foreign swap rate $S^f(t)$ acquires a drift under the domestic annuity measure:

$$
S^{f,\text{quanto}}(0) \approx S^f(0) \left(1 - \rho_{S,X} \, \sigma_S^f \, \sigma_X \, T_0\right)
$$

where $\rho_{S,X}$ is the correlation between the foreign swap rate and the exchange rate.

### Differential Swaps (Diff Swaps)

A **differential swap** (or diff swap) pays the difference between a foreign and domestic floating rate, settled in domestic currency:

$$
\text{Payoff} = \delta_i (L_i^f(T_i) - L_i^d(T_i))
$$

paid at $T_{i+1}$ in domestic currency. The foreign rate requires the quanto adjustment while the domestic rate does not. The fair value involves the quanto-adjusted foreign forward minus the domestic forward.

### Stochastic Correlation and Volatility

In practice, the correlation $\rho_{L,X}$ and the volatilities $\sigma_i^f$, $\sigma_X$ are not constant. More sophisticated models use:

- **Stochastic volatility** for the exchange rate (e.g., Heston or SABR)
- **Local correlation** models where $\rho_{L,X}(t)$ depends on the state
- **Multi-factor HJM** models for the joint dynamics of domestic and foreign rates with stochastic FX

These extensions increase calibration complexity but can be important for long-dated quanto products.

---

## Key Takeaways

- A **quanto adjustment** arises when a derivative pays a rate in one currency but settles in another at a fixed exchange rate
- The adjustment comes from a **cross-currency measure change**, which introduces a drift in the foreign rate under the domestic pricing measure
- The quanto-adjusted forward rate is $L^{f,\text{quanto}} = L^f \exp(-\rho_{L,X}\sigma^f\sigma_X T)$, and the correction is proportional to the **rate-FX correlation**
- **Positive correlation** (foreign rate up when foreign currency strengthens) produces a **negative** quanto adjustment
- Quanto caps and floors are priced using Black's formula with the adjusted forward rate and domestic discounting
- The adjustment is typically small for short-dated products but grows linearly with the fixing horizon and can reach 10+ bps for long-dated quanto products
- **Correlation uncertainty** is the dominant source of model risk in quanto pricing

---

## Further Reading

- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapter 14 (Quanto Products)
- Andersen & Piterbarg (2010), *Interest Rate Modeling*, Volume III, Chapter 17
- Hull (2018), *Options, Futures, and Other Derivatives*, Chapter 30 (Quantos)
- Wystup (2006), *FX Options and Structured Products*, Chapter 1

---

## Exercises

**Exercise 1.** A quanto cap on 3-month GBP LIBOR is settled in USD at a 1:1 exchange rate. The GBP forward rate is $L^f(0) = 4.8\%$, the GBP rate volatility is $\sigma^f = 19\%$, the GBP/USD exchange rate volatility is $\sigma_X = 8\%$, and the rate-FX correlation is $\rho_{L,X} = 0.25$. For a caplet fixing in $T = 3$ years, compute the quanto-adjusted forward rate and the quanto adjustment in basis points. Interpret the sign of the adjustment.

---

**Exercise 2.** Starting from the dynamics of the foreign forward rate under $\mathbb{Q}^{f,T_{i+1}}$ and the exchange rate under $\mathbb{Q}^d$, derive the quanto drift

$$
\mu_{\text{quanto}}(t) = -\rho_{L,X} \, \sigma_i^f \, \sigma_X
$$

using Girsanov's theorem for the composite measure change $\mathbb{Q}^{f,T_{i+1}} \to \mathbb{Q}^d \to \mathbb{Q}^{d,T_{i+1}}$. State all assumptions and identify where the correlation enters.

---

**Exercise 3.** Consider a differential (diff) swap that pays $(L_i^f(T_i) - L_i^d(T_i))$ at $T_{i+1}$ in domestic currency. Show that the fair diff-swap spread is

$$
L_i^{f,\text{quanto}}(0) - L_i^d(0)
$$

where only the foreign rate requires a quanto adjustment. Explain why the domestic rate does not need an adjustment.

---

**Exercise 4.** A trader estimates the GBP rate / GBP-USD FX correlation to be $\rho_{L,X} = 0.35$ using a 1-year rolling window, but $\rho_{L,X} = 0.15$ using a 5-year window. For a 10-year quanto cap on GBP LIBOR with $\sigma^f = 20\%$, $\sigma_X = 10\%$, and $L^f(0) = 5\%$, compute the quanto adjustment under each correlation estimate and express the difference in basis points. Discuss how this correlation uncertainty affects the risk management of a quanto book.

---

**Exercise 5.** Show that the quanto adjustment formula $L^{f,\text{quanto}} = L^f \exp(-\rho_{L,X}\sigma^f\sigma_X T)$ can be rewritten as a shift in the drift of the lognormal process. Specifically, verify that if $L_i^f(T_i)$ is lognormal under $\mathbb{Q}^{f,T_{i+1}}$ with zero drift, then under $\mathbb{Q}^{d,T_{i+1}}$ it remains lognormal but with drift $\mu_{\text{quanto}} = -\rho_{L,X}\sigma^f\sigma_X$, and that the volatility $\sigma^f$ is unchanged.

---

**Exercise 6.** Price a quanto floorlet on EUR EURIBOR with strike $K = 3.0\%$, settled in JPY. The parameters are: $L^f(0) = 2.8\%$ (EUR forward rate), $\sigma^f = 25\%$, $\sigma_X = 12\%$ (EUR/JPY vol), $\rho_{L,X} = -0.15$, $T = 2$ years, $\delta = 0.5$, and $P^d(0, T_{i+1}) = 0.990$ (JPY discount factor). First compute the quanto-adjusted forward rate, then apply Black's formula for the floorlet.

---

**Exercise 7.** In a stochastic volatility extension, both $\sigma^f(t)$ and $\sigma_X(t)$ follow their own diffusion processes and $\rho_{L,X}(t)$ is state-dependent. Explain qualitatively why the constant-parameter quanto formula $\exp(-\rho\sigma^f\sigma_X T)$ becomes inadequate for long-dated quanto products. Describe two modeling approaches that can handle time-varying or stochastic correlation and discuss their calibration requirements.
