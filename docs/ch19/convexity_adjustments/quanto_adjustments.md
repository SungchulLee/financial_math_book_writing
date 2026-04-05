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

??? success "Solution to Exercise 1"

    **Given:** $L^f(0) = 0.048$, $\sigma^f = 0.19$, $\sigma_X = 0.08$, $\rho_{L,X} = 0.25$, $T = 3$ years.

    **Quanto-adjusted forward rate:**

    $$
    L^{f,\text{quanto}}(0) = L^f(0) \, \exp\!\left(-\rho_{L,X} \, \sigma^f \, \sigma_X \, T\right)
    $$

    Computing the exponent:

    $$
    -\rho_{L,X} \, \sigma^f \, \sigma_X \, T = -0.25 \times 0.19 \times 0.08 \times 3 = -0.25 \times 0.0456 = -0.01140
    $$

    $$
    L^{f,\text{quanto}}(0) = 0.048 \times e^{-0.01140} = 0.048 \times 0.98867 = 0.047456
    $$

    Equivalently, $L^{f,\text{quanto}}(0) = 4.746\%$.

    **Quanto adjustment in basis points:**

    $$
    \text{Quanto Adj} = L^{f,\text{quanto}}(0) - L^f(0) = 4.746\% - 4.800\% = -0.054\% = -5.4 \text{ bp}
    $$

    Alternatively, using the first-order formula:

    $$
    \text{Quanto Adj} \approx -\rho_{L,X} \, \sigma^f \, \sigma_X \, T \cdot L^f(0) = -0.01140 \times 0.048 = -0.000547 = -5.5 \text{ bp}
    $$

    (The slight difference is due to the first-order approximation.)

    **Interpretation:** The adjustment is **negative** ($-5.4$ bp) because $\rho_{L,X} = 0.25 > 0$. Positive correlation means that when GBP rates are high, the GBP tends to strengthen against the USD. A standard (non-quanto) product would benefit from this correlation (high rates + strong GBP = double benefit), but the quanto product settles at a fixed exchange rate and misses the FX gain. The quanto-adjusted rate is therefore lower, reflecting the loss of this favorable correlation.

---

**Exercise 2.** Starting from the dynamics of the foreign forward rate under $\mathbb{Q}^{f,T_{i+1}}$ and the exchange rate under $\mathbb{Q}^d$, derive the quanto drift

$$
\mu_{\text{quanto}}(t) = -\rho_{L,X} \, \sigma_i^f \, \sigma_X
$$

using Girsanov's theorem for the composite measure change $\mathbb{Q}^{f,T_{i+1}} \to \mathbb{Q}^d \to \mathbb{Q}^{d,T_{i+1}}$. State all assumptions and identify where the correlation enters.

??? success "Solution to Exercise 2"

    **Step 1: Foreign forward rate under $\mathbb{Q}^{f,T_{i+1}}$.**

    Under the foreign $T_{i+1}$-forward measure, with numéraire $P^f(t, T_{i+1})$:

    $$
    \frac{dL_i^f(t)}{L_i^f(t)} = \sigma_i^f \, dW_L^{f,T_{i+1}}(t)
    $$

    where $W_L^{f,T_{i+1}}$ is a Brownian motion under $\mathbb{Q}^{f,T_{i+1}}$.

    **Step 2: Exchange rate under $\mathbb{Q}^d$.**

    Under the domestic risk-neutral measure:

    $$
    \frac{dX(t)}{X(t)} = (r^d - r^f) \, dt + \sigma_X \, dW_X^d(t)
    $$

    **Assumption:** $dW_L^{f,T_{i+1}} \cdot dW_X^d = \rho_{L,X} \, dt$ (constant correlation).

    **Step 3: Measure change $\mathbb{Q}^{f,T_{i+1}} \to \mathbb{Q}^d$.**

    The relationship between the domestic and foreign risk-neutral measures involves the exchange rate. The numéraire for $\mathbb{Q}^d$ expressed in foreign terms is $B^d(t)/X(t)$. The Girsanov kernel for the change $\mathbb{Q}^f \to \mathbb{Q}^d$ is $\sigma_X$, applied to the Brownian motion $W_X$.

    Under $\mathbb{Q}^d$, the foreign Brownian motion $W_L^{f}$ shifts:

    $$
    dW_L^{f}(t) = dW_L^{d}(t) - \rho_{L,X} \, \sigma_X \, dt
    $$

    This is because the Girsanov theorem for the measure change from $\mathbb{Q}^f$ to $\mathbb{Q}^d$ involves the volatility of the exchange rate, projected onto the direction of $W_L$.

    **Step 4: Measure change $\mathbb{Q}^d \to \mathbb{Q}^{d,T_{i+1}}$.**

    Changing from $\mathbb{Q}^d$ to $\mathbb{Q}^{d,T_{i+1}}$ introduces an additional drift from the domestic bond volatility $\sigma_P^d(t, T_{i+1})$. However, we also need to account for the change from $\mathbb{Q}^{f,T_{i+1}}$ to $\mathbb{Q}^f$ (forward to spot measure in the foreign economy), which introduces a drift involving the foreign bond volatility.

    **Step 5: Combining the measure changes.**

    The composite measure change $\mathbb{Q}^{f,T_{i+1}} \to \mathbb{Q}^{d,T_{i+1}}$ introduces a total drift in $L_i^f$. The key observation is that the drift terms from the forward-measure changes (foreign and domestic) involve bond volatilities that approximately cancel for the forward rate $L_i^f$, leaving only the FX-related drift.

    Under $\mathbb{Q}^{d,T_{i+1}}$:

    $$
    \frac{dL_i^f(t)}{L_i^f(t)} = -\rho_{L,X} \, \sigma_i^f \, \sigma_X \, dt + \sigma_i^f \, dW_L^{d,T_{i+1}}(t)
    $$

    The quanto drift is:

    $$
    \mu_{\text{quanto}} = -\rho_{L,X} \, \sigma_i^f \, \sigma_X
    $$

    **Where correlation enters:** The correlation appears in Step 3 when projecting the Girsanov kernel (which is $\sigma_X$, the FX volatility vector) onto the direction of the foreign rate's Brownian motion $W_L$. The projection is $\rho_{L,X} \sigma_X$, giving the drift correction $-\rho_{L,X} \sigma_i^f \sigma_X$.

    **Assumptions used:** (1) Lognormal dynamics for both $L_i^f$ and $X$. (2) Constant volatilities $\sigma_i^f$, $\sigma_X$ and constant correlation $\rho_{L,X}$. (3) Deterministic interest rates for the forward-measure changes (or that the additional drifts from stochastic rates cancel to leading order). $\blacksquare$

---

**Exercise 3.** Consider a differential (diff) swap that pays $(L_i^f(T_i) - L_i^d(T_i))$ at $T_{i+1}$ in domestic currency. Show that the fair diff-swap spread is

$$
L_i^{f,\text{quanto}}(0) - L_i^d(0)
$$

where only the foreign rate requires a quanto adjustment. Explain why the domestic rate does not need an adjustment.

??? success "Solution to Exercise 3"

    **Present value of the diff swap coupon:**

    $$
    V_0 = P^d(0, T_{i+1}) \, \mathbb{E}^{\mathbb{Q}^{d,T_{i+1}}}\!\left[\delta_i (L_i^f(T_i) - L_i^d(T_i))\right]
    $$

    By linearity of expectation:

    $$
    V_0 = P^d(0, T_{i+1}) \, \delta_i \left(\mathbb{E}^{\mathbb{Q}^{d,T_{i+1}}}[L_i^f(T_i)] - \mathbb{E}^{\mathbb{Q}^{d,T_{i+1}}}[L_i^d(T_i)]\right)
    $$

    **Foreign rate:** $L_i^f$ is a martingale under $\mathbb{Q}^{f,T_{i+1}}$, not under $\mathbb{Q}^{d,T_{i+1}}$. Therefore:

    $$
    \mathbb{E}^{\mathbb{Q}^{d,T_{i+1}}}[L_i^f(T_i)] = L_i^{f,\text{quanto}}(0) = L_i^f(0) \, e^{-\rho_{L,X}\sigma_i^f\sigma_X T_i}
    $$

    The foreign rate requires the quanto adjustment.

    **Domestic rate:** $L_i^d$ is a martingale under $\mathbb{Q}^{d,T_{i+1}}$ (the domestic $T_{i+1}$-forward measure) because $T_{i+1}$ is precisely its natural payment date, and $P^d(t, T_{i+1})$ is the natural numéraire. Therefore:

    $$
    \mathbb{E}^{\mathbb{Q}^{d,T_{i+1}}}[L_i^d(T_i)] = L_i^d(0)
    $$

    No adjustment is needed for the domestic rate.

    **Why the domestic rate needs no adjustment:** The domestic forward rate $L_i^d$ for period $[T_i, T_{i+1}]$ is defined as a function of $P^d(t, T_i)/P^d(t, T_{i+1})$, and when both the pricing numéraire and the payment currency are domestic, no measure change is required. The payoff $(L_i^f - L_i^d)$ is paid in domestic currency at $T_{i+1}$, and $\mathbb{Q}^{d,T_{i+1}}$ is the correct pricing measure. The domestic rate is already a martingale under this measure, while the foreign rate requires the cross-currency measure change.

    **Fair diff-swap spread:**

    $$
    V_0 = P^d(0, T_{i+1}) \, \delta_i \left(L_i^{f,\text{quanto}}(0) - L_i^d(0)\right)
    $$

    The fair spread (the fixed rate that makes $V_0 = 0$) is $L_i^{f,\text{quanto}}(0) - L_i^d(0)$. $\blacksquare$

---

**Exercise 4.** A trader estimates the GBP rate / GBP-USD FX correlation to be $\rho_{L,X} = 0.35$ using a 1-year rolling window, but $\rho_{L,X} = 0.15$ using a 5-year window. For a 10-year quanto cap on GBP LIBOR with $\sigma^f = 20\%$, $\sigma_X = 10\%$, and $L^f(0) = 5\%$, compute the quanto adjustment under each correlation estimate and express the difference in basis points. Discuss how this correlation uncertainty affects the risk management of a quanto book.

??? success "Solution to Exercise 4"

    **Given:** $\sigma^f = 0.20$, $\sigma_X = 0.10$, $L^f(0) = 0.05$, $T = 10$ years.

    **With $\rho_{L,X} = 0.35$ (1-year window):**

    $$
    \text{Quanto Adj}_1 = -\rho_{L,X} \, \sigma^f \, \sigma_X \, T \cdot L^f(0) = -0.35 \times 0.20 \times 0.10 \times 10 \times 0.05
    $$

    $$
    = -0.35 \times 0.01 \times 0.05 = -0.000350 = -3.50 \text{ bp}
    $$

    Using the exact formula: $L^{f,q}_1 = 0.05 \times e^{-0.35 \times 0.20 \times 0.10 \times 10} = 0.05 \times e^{-0.07} = 0.05 \times 0.9324 = 0.04662$. Adjustment $= -3.38$ bp.

    **With $\rho_{L,X} = 0.15$ (5-year window):**

    $$
    \text{Quanto Adj}_2 = -0.15 \times 0.20 \times 0.10 \times 10 \times 0.05 = -0.000150 = -1.50 \text{ bp}
    $$

    Using the exact formula: $L^{f,q}_2 = 0.05 \times e^{-0.15 \times 0.20 \times 0.10 \times 10} = 0.05 \times e^{-0.03} = 0.05 \times 0.9704 = 0.04852$. Adjustment $= -1.48$ bp.

    **Difference between the two estimates:**

    $$
    |\text{Adj}_1 - \text{Adj}_2| = |{-3.38} - ({-1.48})| = 1.90 \text{ bp}
    $$

    On the forward rate level, the difference is approximately **1.9 basis points**.

    **Impact on risk management:**

    1. **Valuation uncertainty:** A 1.9 bp difference in the forward rate translates directly to P&L uncertainty. For a \$1 billion notional 10-year quanto cap, this could represent millions of dollars in mark-to-market difference.

    2. **Correlation hedging:** The rate-FX correlation $\rho_{L,X}$ cannot be hedged directly with liquid instruments, making it an unhedgeable risk factor. This is a key source of **model risk** in quanto books.

    3. **Reserve requirements:** Prudent risk management requires holding reserves for correlation uncertainty. A common approach is to compute the quanto adjustment under multiple correlation scenarios (e.g., $\pm 1$ standard deviation of the historical estimate) and reserve the range.

    4. **Estimation methodology:** The choice of estimation window (1-year vs 5-year) reflects a trade-off between responsiveness to recent market conditions and statistical stability. Neither is objectively correct, suggesting that quanto pricing inherently carries irreducible model risk of the order computed above.

---

**Exercise 5.** Show that the quanto adjustment formula $L^{f,\text{quanto}} = L^f \exp(-\rho_{L,X}\sigma^f\sigma_X T)$ can be rewritten as a shift in the drift of the lognormal process. Specifically, verify that if $L_i^f(T_i)$ is lognormal under $\mathbb{Q}^{f,T_{i+1}}$ with zero drift, then under $\mathbb{Q}^{d,T_{i+1}}$ it remains lognormal but with drift $\mu_{\text{quanto}} = -\rho_{L,X}\sigma^f\sigma_X$, and that the volatility $\sigma^f$ is unchanged.

??? success "Solution to Exercise 5"

    Under $\mathbb{Q}^{f,T_{i+1}}$, the foreign forward rate is a driftless lognormal martingale:

    $$
    dL_i^f(t) = \sigma^f L_i^f(t) \, dW^{f,T_{i+1}}(t)
    $$

    In integrated form:

    $$
    L_i^f(T_i) = L_i^f(0) \exp\!\left(-\frac{1}{2}(\sigma^f)^2 T_i + \sigma^f W^{f,T_{i+1}}(T_i)\right)
    $$

    Under $\mathbb{Q}^{d,T_{i+1}}$, the quanto drift $\mu_{\text{quanto}} = -\rho_{L,X}\sigma^f\sigma_X$ shifts the dynamics to:

    $$
    dL_i^f(t) = \mu_{\text{quanto}} \, L_i^f(t) \, dt + \sigma^f L_i^f(t) \, dW^{d,T_{i+1}}(t)
    $$

    In integrated form:

    $$
    L_i^f(T_i) = L_i^f(0) \exp\!\left(\left(\mu_{\text{quanto}} - \frac{1}{2}(\sigma^f)^2\right) T_i + \sigma^f W^{d,T_{i+1}}(T_i)\right)
    $$

    This is lognormal with:

    - **Drift:** $\mu_{\text{quanto}} = -\rho_{L,X}\sigma^f\sigma_X$ (nonzero)
    - **Volatility:** $\sigma^f$ (unchanged)

    **Verification of the expectation:**

    $$
    \mathbb{E}^{\mathbb{Q}^{d,T_{i+1}}}[L_i^f(T_i)] = L_i^f(0) \exp\!\left(\mu_{\text{quanto}} \, T_i\right) = L_i^f(0) \exp\!\left(-\rho_{L,X}\sigma^f\sigma_X T_i\right) = L_i^{f,\text{quanto}}(0)
    $$

    This confirms the quanto-adjusted forward rate formula.

    **Why the volatility is unchanged:** The Girsanov theorem changes the drift of the Brownian motion but not its quadratic variation. Specifically, $W^{d,T_{i+1}}(t) = W^{f,T_{i+1}}(t) + \int_0^t \rho_{L,X}\sigma_X \, ds$ is still a Brownian motion under $\mathbb{Q}^{d,T_{i+1}}$ (by Girsanov's theorem), so the diffusion coefficient $\sigma^f$ multiplying $dW$ is the same under both measures. The quanto adjustment affects only the mean of $\ln L_i^f(T_i)$, not its variance. $\blacksquare$

---

**Exercise 6.** Price a quanto floorlet on EUR EURIBOR with strike $K = 3.0\%$, settled in JPY. The parameters are: $L^f(0) = 2.8\%$ (EUR forward rate), $\sigma^f = 25\%$, $\sigma_X = 12\%$ (EUR/JPY vol), $\rho_{L,X} = -0.15$, $T = 2$ years, $\delta = 0.5$, and $P^d(0, T_{i+1}) = 0.990$ (JPY discount factor). First compute the quanto-adjusted forward rate, then apply Black's formula for the floorlet.

??? success "Solution to Exercise 6"

    **Given:** $L^f(0) = 0.028$ (EUR), $\sigma^f = 0.25$, $\sigma_X = 0.12$ (EUR/JPY), $\rho_{L,X} = -0.15$, $T = 2$, $\delta = 0.5$, $P^d(0, T_{i+1}) = 0.990$, $K = 0.03$.

    **Step 1: Quanto-adjusted forward rate.**

    $$
    L^{f,\text{quanto}}(0) = L^f(0) \, \exp\!\left(-\rho_{L,X} \, \sigma^f \, \sigma_X \, T\right)
    $$

    $$
    = 0.028 \times \exp\!\left(-(-0.15) \times 0.25 \times 0.12 \times 2\right) = 0.028 \times \exp(0.0090)
    $$

    $$
    = 0.028 \times 1.00904 = 0.028253
    $$

    The quanto-adjusted forward rate is $2.825\%$. The adjustment is **positive** ($+2.5$ bp) because $\rho_{L,X} < 0$: when EUR rates rise, the EUR tends to weaken against JPY. The quanto product does not suffer from this FX loss, so the effective forward rate is higher.

    **Step 2: Black's formula for the quanto floorlet.**

    $$
    \text{Quanto Floorlet} = \delta \, P^d(0, T_{i+1}) \left[K \, N(-d_2) - L^{f,q}(0) \, N(-d_1)\right]
    $$

    Computing $d_1$ and $d_2$:

    $$
    d_1 = \frac{\ln(L^{f,q}(0)/K) + \frac{1}{2}(\sigma^f)^2 T}{\sigma^f \sqrt{T}} = \frac{\ln(0.028253/0.030) + \frac{1}{2}(0.0625)(2)}{0.25\sqrt{2}}
    $$

    $$
    = \frac{\ln(0.94177) + 0.0625}{0.3536} = \frac{-0.05997 + 0.0625}{0.3536} = \frac{0.00253}{0.3536} = 0.00716
    $$

    $$
    d_2 = d_1 - \sigma^f\sqrt{T} = 0.00716 - 0.3536 = -0.3464
    $$

    Now:

    - $N(-d_1) = N(-0.00716) = 0.4971$
    - $N(-d_2) = N(0.3464) = 0.6355$

    **Quanto floorlet price:**

    $$
    = 0.5 \times 0.990 \times \left[0.030 \times 0.6355 - 0.028253 \times 0.4971\right]
    $$

    $$
    = 0.495 \times \left[0.019065 - 0.014045\right] = 0.495 \times 0.005020 = 0.002485
    $$

    The quanto floorlet price is approximately $0.2485\%$ of notional, or $24.85$ bp.

    **Note:** The floorlet is relatively valuable because the quanto-adjusted forward rate ($2.825\%$) is below the strike ($3.0\%$), so the floor is in-the-money, making $N(-d_1) \approx 0.50$ and $N(-d_2) \approx 0.64$.

---

**Exercise 7.** In a stochastic volatility extension, both $\sigma^f(t)$ and $\sigma_X(t)$ follow their own diffusion processes and $\rho_{L,X}(t)$ is state-dependent. Explain qualitatively why the constant-parameter quanto formula $\exp(-\rho\sigma^f\sigma_X T)$ becomes inadequate for long-dated quanto products. Describe two modeling approaches that can handle time-varying or stochastic correlation and discuss their calibration requirements.

??? success "Solution to Exercise 7"

    **Why the constant-parameter formula becomes inadequate:**

    The quanto adjustment formula $\exp(-\rho\sigma^f\sigma_X T)$ assumes that $\rho$, $\sigma^f$, and $\sigma_X$ are **constant** over the life of the product. For long-dated quanto products (e.g., 10--30 years), this assumption breaks down for several reasons:

    1. **Volatility mean-reversion and regime changes:** Interest rate volatilities and FX volatilities exhibit mean-reversion and can undergo regime shifts. Using today's spot volatility for a 20-year projection overstates or understates the cumulative adjustment. The correct integral is $\int_0^T \rho(t)\sigma^f(t)\sigma_X(t) \, dt$, which can differ significantly from $\rho\sigma^f\sigma_X T$.

    2. **Correlation instability:** The rate-FX correlation $\rho_{L,X}$ is empirically unstable, varying with macroeconomic regimes (e.g., risk-on vs risk-off), monetary policy cycles, and market stress. A constant $\rho$ fails to capture the time-varying nature of this dependence.

    3. **Stochastic volatility effects:** When volatilities are stochastic, the quanto adjustment depends on the **joint distribution** of $(\sigma^f(t), \sigma_X(t), \rho(t))$, not just their initial values. The convexity of the exponential function means that $\mathbb{E}[\exp(-\int_0^T \rho\sigma^f\sigma_X dt)] \neq \exp(-\mathbb{E}[\int_0^T \rho\sigma^f\sigma_X dt])$ (Jensen's inequality), introducing a higher-order correction.

    4. **Correlation between correlation and rates:** If correlation increases during stress periods when rates are volatile, the average $\rho\sigma^f\sigma_X$ product differs from the product of averages.

    **Two modeling approaches:**

    **Approach 1: Multi-factor stochastic volatility with local correlation.**

    Model the foreign rate, exchange rate, and their volatilities jointly:

    - $dL^f/L^f = \sigma^f(v_1(t)) \, dW_1$, where $v_1$ follows a CIR or Heston process
    - $dX/X = \ldots + \sigma_X(v_2(t)) \, dW_2$, where $v_2$ follows its own stochastic process
    - $\rho_{L,X}(t) = \rho(v_1(t), v_2(t))$, a deterministic function of the variance states

    **Calibration requirements:** Joint calibration to (1) the foreign interest rate swaption surface, (2) the FX option smile across maturities, and (3) cross-asset products such as quanto swaptions or power reverse dual currency notes (PRDCs) that are sensitive to rate-FX correlation. Correlation is typically backed out from quanto product prices or estimated from historical data with appropriate filtering.

    **Approach 2: Time-dependent (piecewise constant) parameters.**

    Use a simpler framework where $\sigma^f(t)$, $\sigma_X(t)$, and $\rho(t)$ are deterministic but time-varying (e.g., piecewise constant on annual intervals):

    $$
    L^{f,\text{quanto}}(0) = L^f(0) \exp\!\left(-\sum_{k} \rho_k \, \sigma^f_k \, \sigma_{X,k} \, \Delta t_k\right)
    $$

    **Calibration requirements:** Calibrate each time bucket's volatilities to the respective term structure of option prices (caplet vols for rates, FX option vols for FX). The time-dependent correlation can be estimated from forward-starting quanto products or from historical rolling-window estimates mapped to future periods.

    This approach is simpler to implement than full stochastic volatility but captures the most important effect: the term structure of the adjustment parameters. It is widely used in practice for pricing long-dated quanto products.
