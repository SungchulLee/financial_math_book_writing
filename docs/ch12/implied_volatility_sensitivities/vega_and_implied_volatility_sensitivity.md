# Vega and Implied Volatility Sensitivity


## Introduction


Implied volatility sensitivities play a central role in option risk management. Among them, **vega** measures how option prices respond to changes in implied volatility and serves as the primary channel through which volatility risk is transmitted. Understanding vega and its extensions is essential for constructing effective hedges, attributing P&L, and managing complex option portfolios.

This section develops a comprehensive treatment of vega, from the basic Black-Scholes definition through model-consistent generalizations, higher-order sensitivities, and practical hedging applications.

## Definition of Vega


### 1. Basic Definition


For an option with price $P$ and implied volatility $\sigma_{\text{IV}}$, **vega** is defined as:

$$
\mathcal{V} := \frac{\partial P}{\partial \sigma_{\text{IV}}}
$$


This measures the first-order sensitivity of the option price to changes in implied volatility.

**Convention:** Vega is typically quoted per 1% (100 basis points) change in implied volatility:

$$
\mathcal{V}_{1\%} = \frac{\partial P}{\partial \sigma_{\text{IV}}} \times 0.01
$$


### 2. Black-Scholes Vega


In the Black-Scholes model, vega has a closed-form expression:

$$
\mathcal{V}_{\text{BS}} = S_0 e^{-qT} \phi(d_1) \sqrt{T}
$$


where $\phi(\cdot)$ is the standard normal density and:

$$
d_1 = \frac{\ln(S_0/K) + (r - q + \sigma^2/2)T}{\sigma\sqrt{T}}
$$


**Key properties:**
- **Positive for all options:** Both calls and puts have $\mathcal{V} > 0$
- **Symmetric in $d_1$:** Since $\phi(-x) = \phi(x)$, vega depends on $|d_1|$
- **Maximum at ATM:** Vega is largest when $d_1 \approx 0$ (at-the-money forward)

**Equivalently:**

$$
\mathcal{V}_{\text{BS}} = K e^{-rT} \phi(d_2) \sqrt{T}
$$


where $d_2 = d_1 - \sigma\sqrt{T}$.

### 3. Vega as Dual Delta


There is a remarkable duality between vega and delta:

$$
\mathcal{V} = S_0 \sqrt{T} \cdot \frac{\partial C}{\partial d_1} \cdot \frac{\partial d_1}{\partial \sigma}
$$


Using the Black-Scholes formula:

$$
\frac{\partial C}{\partial d_1} = S_0 e^{-qT} \phi(d_1)
$$


This shows that vega can be interpreted as the "delta with respect to $d_1$" scaled appropriately.

## Dependence on Strike and Maturity


### 1. Strike Dependence


The dependence of vega on strike (or moneyness) follows directly from the $\phi(d_1)$ term:

$$
\mathcal{V}(K) = S_0 e^{-qT} \sqrt{T} \cdot \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{d_1^2}{2}\right)
$$


**At-the-money forward ($K = F = S_0 e^{(r-q)T}$):**

$$
d_1 = \frac{\sigma\sqrt{T}}{2}, \quad \mathcal{V}_{\text{ATM}} = S_0 e^{-qT} \sqrt{T} \cdot \phi\left(\frac{\sigma\sqrt{T}}{2}\right)
$$


For small $\sigma\sqrt{T}$:

$$
\mathcal{V}_{\text{ATM}} \approx \frac{S_0 e^{-qT} \sqrt{T}}{\sqrt{2\pi}} \left(1 - \frac{\sigma^2 T}{8}\right)
$$


**Deep in-the-money ($K \ll S_0$):**

$$
d_1 \to +\infty, \quad \phi(d_1) \to 0, \quad \mathcal{V} \to 0
$$


**Deep out-of-the-money ($K \gg S_0$):**

$$
d_1 \to -\infty, \quad \phi(d_1) \to 0, \quad \mathcal{V} \to 0
$$


**Interpretation:** Vega is maximized at ATM because the option price is most sensitive to volatility when the payoff is uncertain (near the strike).

### 2. Maturity Dependence


The $\sqrt{T}$ factor in vega produces characteristic maturity behavior:

$$
\mathcal{V}(T) = S_0 e^{-qT} \phi(d_1(T)) \sqrt{T}
$$


**Short maturity ($T \to 0$):**

$$
\sqrt{T} \to 0 \quad \Rightarrow \quad \mathcal{V} \to 0
$$


Short-dated options have small vega because:
- Little time for volatility to affect the outcome
- Price is dominated by intrinsic value (deep ITM/OTM)

**Long maturity ($T \to \infty$):**

For ATM options:

$$
d_1 \to \frac{\sigma\sqrt{T}}{2} \to \infty \quad \Rightarrow \quad \phi(d_1) \to 0
$$


The product $\sqrt{T} \cdot \phi(d_1)$ eventually decreases:

$$
\lim_{T \to \infty} \sqrt{T} \cdot \phi\left(\frac{\sigma\sqrt{T}}{2}\right) = \lim_{T \to \infty} \frac{\sqrt{T}}{\sqrt{2\pi}} e^{-\sigma^2 T/8} = 0
$$


**Peak vega maturity:** For ATM options, vega peaks at an intermediate maturity:

$$
T^* = \frac{4}{\sigma^2}
$$


For $\sigma = 20\%$, $T^* = 100$ years, effectively outside typical option maturities. In practice, ATM vega increases with $T$ for most quoted maturities.

**For OTM options:** Vega may peak at shorter maturities because $d_1$ moves away from zero faster as $T$ increases.

### 3. Vega Surface


The complete vega surface $\mathcal{V}(K, T)$ exhibits:

| Region | Vega Behavior |
|--------|---------------|
| ATM, short-dated | Small (small $\sqrt{T}$) |
| ATM, medium-dated | Maximum |
| ATM, long-dated | Large but eventually declining |
| OTM, any maturity | Smaller than ATM |
| Deep ITM/OTM | Near zero |

## Higher-Order Volatility Sensitivities


### 1. Vanna: Cross-Sensitivity to Spot and Volatility


**Definition:**

$$
\text{Vanna} := \frac{\partial^2 P}{\partial S \partial \sigma} = \frac{\partial \mathcal{V}}{\partial S} = \frac{\partial \Delta}{\partial \sigma}
$$


**Black-Scholes formula:**

$$
\text{Vanna}_{\text{BS}} = -e^{-qT} \phi(d_1) \frac{d_2}{\sigma} = \frac{\mathcal{V}}{S} \left(1 - \frac{d_1}{\sigma\sqrt{T}}\right)
$$


**Equivalently:**

$$
\text{Vanna}_{\text{BS}} = -\frac{\mathcal{V} \cdot d_2}{S \sigma \sqrt{T}}
$$


**Sign and interpretation:**
- **ATM ($d_2 \approx -\sigma\sqrt{T}/2 < 0$):** Vanna > 0 for calls
- **OTM call ($d_2 < 0$):** Vanna > 0
- **ITM call ($d_2 > 0$):** Vanna < 0

**Interpretation:** Vanna measures how delta changes with volatility, or equivalently, how vega changes with spot. It is crucial for understanding P&L when both spot and volatility move together (correlation effects).

### 2. Volga (Vomma): Second-Order Volatility Sensitivity


**Definition:**

$$
\text{Volga} := \frac{\partial^2 P}{\partial \sigma^2} = \frac{\partial \mathcal{V}}{\partial \sigma}
$$


**Black-Scholes formula:**

$$
\text{Volga}_{\text{BS}} = \mathcal{V} \cdot \frac{d_1 d_2}{\sigma}
$$


**Equivalently:**

$$
\text{Volga}_{\text{BS}} = S_0 e^{-qT} \phi(d_1) \sqrt{T} \cdot \frac{d_1 d_2}{\sigma}
$$


**Sign and interpretation:**
- **ATM ($d_1 \approx \sigma\sqrt{T}/2$, $d_2 \approx -\sigma\sqrt{T}/2$):** $d_1 d_2 < 0$, so Volga < 0
- **OTM/ITM (large $|d_1|$):** Volga > 0 (both $d_1, d_2$ same sign)

**Interpretation:** Volga measures the convexity of the option price with respect to volatility. Positive volga means the option benefits from volatility of volatility (vol-of-vol).

### 3. Ultima: Third-Order Volatility Sensitivity


**Definition:**

$$
\text{Ultima} := \frac{\partial^3 P}{\partial \sigma^3} = \frac{\partial \text{Volga}}{\partial \sigma}
$$


**Black-Scholes formula:**

$$
\text{Ultima}_{\text{BS}} = -\frac{\mathcal{V}}{\sigma^2} \left[ d_1 d_2 (1 - d_1 d_2) + d_1^2 + d_2^2 \right]
$$


Ultima is rarely used in practice but becomes relevant for portfolios with large volga exposure.

### 4. Summary Table of Volatility Greeks


| Greek | Definition | BS Formula | At ATM |
|-------|-----------|------------|--------|
| Vega | $\partial P/\partial \sigma$ | $S\phi(d_1)\sqrt{T}$ | Maximum |
| Vanna | $\partial^2 P/\partial S \partial \sigma$ | $-\mathcal{V} d_2/(S\sigma\sqrt{T})$ | Positive |
| Volga | $\partial^2 P/\partial \sigma^2$ | $\mathcal{V} d_1 d_2/\sigma$ | Negative |
| Ultima | $\partial^3 P/\partial \sigma^3$ | (complex) | (varies) |

## Vega as Sensitivity to Market Quotes


### 1. Implied Volatility as the Market Variable


Because traders quote options in terms of implied volatility rather than price, vega measures sensitivity to **observable market moves**:

$$
\Delta P \approx \mathcal{V} \cdot \Delta \sigma_{\text{IV}}
$$


This first-order approximation underlies most day-to-day volatility risk management.

**Example:** An option with $\mathcal{V} = \$0.50$ per 1 vol point will change by approximately $\$0.50$ if implied volatility moves from 20% to 21%.

### 2. Dollar Vega and Percentage Vega


**Dollar vega:** The absolute change in position value for a 1% move in implied volatility:

$$
\mathcal{V}_{\$} = \mathcal{V} \times \text{Position Size}
$$


**Percentage vega:** The percentage change in option price per 1% move in IV:

$$
\mathcal{V}_{\%} = \frac{\mathcal{V}}{P} \times 100
$$


**Out-of-the-money options** have high percentage vega but low dollar vega.

### 3. Model-Free Interpretation


Importantly, when using market-implied volatility, vega has a model-free interpretation:

$$
\Delta P_{\text{market}} \approx \mathcal{V}_{\text{BS}}(\sigma_{\text{IV}}) \cdot \Delta \sigma_{\text{IV}}
$$


The Black-Scholes vega evaluated at the implied volatility approximates the market price change, regardless of the true underlying dynamics.

## Vega Beyond Black-Scholes


### 1. Model-Consistent Vega


In models beyond Black-Scholes (local volatility, stochastic volatility), the concept of vega becomes more nuanced:

**Definition:** Model-consistent vega is the derivative of the model price with respect to a parallel shift in the implied volatility surface:

$$
\mathcal{V}_{\text{model}} = \frac{\partial P_{\text{model}}}{\partial \sigma_{\text{IV}}}
$$


This differs from the Black-Scholes vega because model prices depend on the entire volatility surface, not just a single $\sigma$.

### 2. Local Volatility Vega


In local volatility models:

$$
dS_t = (r - q) S_t dt + \sigma_{\text{loc}}(S_t, t) S_t dW_t
$$


The vega with respect to a bump in the local volatility surface is:

$$
\mathcal{V}_{\text{loc}} = \int_0^T \int_0^\infty \frac{\partial P}{\partial \sigma_{\text{loc}}(S, t)} \cdot \delta\sigma_{\text{loc}}(S, t) \, dS \, dt
$$


For a parallel bump $\delta\sigma_{\text{loc}} = \epsilon$:

$$
\mathcal{V}_{\text{loc}} \neq \mathcal{V}_{\text{BS}}
$$


because the local volatility surface and implied volatility surface are related nonlinearly.

### 3. Stochastic Volatility Vega


In stochastic volatility models (e.g., Heston):

$$
\begin{align}
dS_t &= (r - q) S_t dt + \sqrt{v_t} S_t dW_t^S \\
dv_t &= \kappa(\theta - v_t) dt + \xi \sqrt{v_t} dW_t^v
\end{align}
$$


Multiple "vegas" exist:
- **Spot vol vega:** $\partial P / \partial v_0$ (sensitivity to initial variance)
- **Long-run vol vega:** $\partial P / \partial \theta$ (sensitivity to mean variance)
- **Vol-of-vol vega:** $\partial P / \partial \xi$

Each captures different aspects of volatility risk.

### 4. Market-Quoted vs. Model Vegas


**Market-quoted vega:** Sensitivity to a change in the market-implied volatility at a specific strike and maturity.

**Model vega:** Sensitivity computed from the model's pricing function.

**Discrepancy:** When a model is calibrated to the market, these may differ:
- Market-quoted vega: Changes implied vol, holds model parameters fixed
- Model vega: Changes model parameters consistently with the new implied vol

**Best practice:** Use market-quoted vegas for risk reporting and hedging, model vegas for understanding dynamics.

## Vega Bucketing and Term Structure Hedging


### 1. The Need for Bucketing


A portfolio of options across multiple strikes and maturities has vega exposure distributed across the volatility surface. A single "total vega" number is insufficient for risk management.

**Vega bucketing** decomposes total vega by:
- **Maturity buckets:** 1M, 3M, 6M, 1Y, 2Y, etc.
- **Strike buckets:** OTM puts, ATM, OTM calls
- **Combined:** A grid of (strike, maturity) buckets

### 2. Parallel Vega


**Definition:** Parallel vega is the sensitivity to a uniform shift across all implied volatilities:

$$
\mathcal{V}_{\parallel} = \sum_{i} \mathcal{V}_i
$$


where $\mathcal{V}_i$ is the vega of the $i$-th option.

**Limitation:** Market volatility rarely moves in parallel; short-dated and long-dated vols often move differently.

### 3. Term Structure Vega


**Definition:** Term structure vega decomposes sensitivity by maturity:

$$
\mathcal{V}(T_j) = \sum_{i: T_i \in \text{bucket } j} \mathcal{V}_i
$$


**Hedging implications:**
- To hedge $\mathcal{V}(T_1)$ exposure, trade options expiring around $T_1$
- Different maturities hedge different parts of the term structure

**Example:** A portfolio is:
- Long $\mathcal{V} = \$100K$ in 1-month options
- Short $\mathcal{V} = \$50K$ in 1-year options

The portfolio is net long $\$50K$ vega, but:
- Benefits if short-dated vol rises
- Loses if long-dated vol rises
- A term structure steepening (short up, long down) produces mixed P&L

### 4. Smile Vega


**Definition:** Smile vega decomposes sensitivity by strike:

$$
\mathcal{V}(K_j) = \sum_{i: K_i \in \text{bucket } j} \mathcal{V}_i
$$


**Typical buckets:**
- 25-delta puts
- ATM
- 25-delta calls

**Hedging implications:**
- To hedge skew exposure, trade risk reversals (long OTM put, short OTM call)
- To hedge smile curvature, trade butterflies

## Numerical Examples


### 1. Example: ATM Call Vega


**Parameters:**
- $S_0 = 100$, $K = 100$, $r = 5\%$, $q = 0$
- $\sigma = 20\%$, $T = 0.25$ years

**Calculation:**

$$
d_1 = \frac{\ln(100/100) + (0.05 + 0.04/2) \times 0.25}{0.20 \times 0.5} = \frac{0 + 0.0175}{0.10} = 0.175
$$


$$
\phi(0.175) = \frac{1}{\sqrt{2\pi}} e^{-0.175^2/2} = 0.3945
$$


$$
\mathcal{V} = 100 \times 0.3945 \times 0.5 = 19.73
$$


**Interpretation:** A 1% increase in implied volatility (20% → 21%) increases the option price by approximately $\$0.20$.

### 2. Example: Vega Across Strikes


For the same parameters, vary $K$:

| Strike $K$ | $d_1$ | $\phi(d_1)$ | Vega |
|-----------|-------|-------------|------|
| 90 | 1.28 | 0.176 | 8.78 |
| 95 | 0.73 | 0.307 | 15.34 |
| 100 | 0.175 | 0.394 | 19.73 |
| 105 | -0.38 | 0.370 | 18.50 |
| 110 | -0.93 | 0.258 | 12.91 |

**Observation:** Vega peaks near ATM and declines for both ITM and OTM options.

### 3. Example: Vanna Calculation


Using the same ATM parameters:

$$
d_2 = d_1 - \sigma\sqrt{T} = 0.175 - 0.10 = 0.075
$$


$$
\text{Vanna} = -\frac{\mathcal{V} \cdot d_2}{S \cdot \sigma \cdot \sqrt{T}} = -\frac{19.73 \times 0.075}{100 \times 0.20 \times 0.5} = -0.148
$$


**Interpretation:** If spot increases by $\$1$ and volatility increases by 1%, the combined effect on delta is approximately $-0.148 \times 0.01 = -0.00148$.

### 4. Example: Volga Calculation


$$
\text{Volga} = \mathcal{V} \cdot \frac{d_1 d_2}{\sigma} = 19.73 \times \frac{0.175 \times 0.075}{0.20} = 1.30
$$


**Interpretation:** The ATM option has positive volga (convex in volatility), but this is small. Deep OTM options have much larger volga.

## Vega Hedging in Practice


### 1. Single-Instrument Vega Hedges


**Objective:** Neutralize vega exposure using a liquid hedging instrument.

**Approach:**
1. Compute portfolio vega: $\mathcal{V}_{\text{portfolio}}$
2. Select hedging instrument with vega $\mathcal{V}_{\text{hedge}}$
3. Trade $n = -\mathcal{V}_{\text{portfolio}} / \mathcal{V}_{\text{hedge}}$ units

**Limitation:** Hedge ratio assumes parallel volatility moves. If the portfolio and hedge have different strike/maturity profiles, the hedge is imperfect.

### 2. Vega-Weighted Hedging


When hedging across different maturities, use **time-weighted vega**:

$$
\mathcal{V}_{\sqrt{T}} = \mathcal{V} / \sqrt{T}
$$


This normalizes for the $\sqrt{T}$ dependence:

$$
\text{Hedge ratio} = -\frac{\mathcal{V}_{\text{portfolio}} / \sqrt{T_{\text{portfolio}}}}{\mathcal{V}_{\text{hedge}} / \sqrt{T_{\text{hedge}}}}
$$


### 3. Multi-Instrument Hedging


For complex portfolios, hedge using multiple instruments:

**Objective:** Find hedge ratios $n_1, n_2, \ldots$ such that:

$$
\mathcal{V}_{\text{portfolio}} + \sum_j n_j \mathcal{V}_j^{(\text{hedge})} = 0
$$


**Extended objective (term structure):**

$$
\mathcal{V}_{\text{portfolio}}(T_k) + \sum_j n_j \mathcal{V}_j^{(\text{hedge})}(T_k) = 0 \quad \text{for each bucket } k
$$


This requires at least as many hedging instruments as buckets.

### 4. Practical Considerations


**Liquidity:** Not all strikes/maturities are equally liquid. Concentrate hedges in liquid options.

**Transaction costs:** Frequent rehedging is costly. Balance hedge accuracy against costs.

**Model risk:** Vega calculations depend on model assumptions. Use conservative (larger) hedge ratios in uncertain conditions.

**Gamma/delta interaction:** Vega hedges may introduce delta and gamma exposure. Consider joint optimization.

## P&L Attribution


### 1. Volatility P&L


The P&L from volatility moves is:

$$
\text{P\&L}_{\sigma} = \mathcal{V} \cdot \Delta\sigma + \frac{1}{2} \text{Volga} \cdot (\Delta\sigma)^2 + \text{higher order}
$$


**First-order approximation:**

$$
\text{P\&L}_{\sigma} \approx \mathcal{V} \cdot \Delta\sigma
$$


**Second-order refinement (important for large moves):**

$$
\text{P\&L}_{\sigma} \approx \mathcal{V} \cdot \Delta\sigma + \frac{1}{2} \text{Volga} \cdot (\Delta\sigma)^2
$$


### 2. Cross-Effects: Vanna P&L


When spot and volatility move together:

$$
\text{P\&L}_{\text{cross}} = \text{Vanna} \cdot \Delta S \cdot \Delta\sigma
$$


**Empirical regularity:** For equity indices, spot and volatility are negatively correlated:

$$
\Delta\sigma \approx -\beta \cdot \frac{\Delta S}{S}, \quad \beta > 0
$$


This **leverage effect** means:
- Vanna > 0 portfolios benefit when spot falls and vol rises
- Vanna < 0 portfolios suffer in this scenario

### 3. Full Second-Order P&L


Combining all effects:

$$
\text{P\&L} = \Delta \cdot \Delta S + \frac{1}{2}\Gamma \cdot (\Delta S)^2 + \mathcal{V} \cdot \Delta\sigma + \frac{1}{2}\text{Volga} \cdot (\Delta\sigma)^2 + \text{Vanna} \cdot \Delta S \cdot \Delta\sigma + \Theta \cdot \Delta t
$$


This decomposition is fundamental for trading desk P&L attribution.

## Summary


Vega and implied volatility sensitivities form the foundation of volatility risk management:

### 1. Basic Properties

$$
\mathcal{V}_{\text{BS}} = S_0 e^{-qT} \phi(d_1) \sqrt{T}
$$

- Positive for all options
- Maximum at ATM
- Increases with $\sqrt{T}$ for moderate maturities

### 2. Higher-Order Greeks

| Greek | Formula | Interpretation |
|-------|---------|----------------|
| Vanna | $\partial^2 P/\partial S \partial \sigma$ | Spot-vol cross-sensitivity |
| Volga | $\partial^2 P/\partial \sigma^2$ | Vol convexity |

### 3. Model Considerations

- Black-Scholes vega is model-free when applied to market IV
- Local/stochastic volatility models require model-consistent vegas
- Market-quoted vegas preferred for risk management

### 4. Practical Hedging

- Use vega bucketing by maturity and strike
- Multi-instrument hedges for term structure exposure
- Account for gamma/delta interactions
- Balance accuracy against transaction costs

### 5. P&L Attribution

$$
\text{P\&L}_{\text{vol}} \approx \mathcal{V} \cdot \Delta\sigma + \frac{1}{2}\text{Volga} \cdot (\Delta\sigma)^2 + \text{Vanna} \cdot \Delta S \cdot \Delta\sigma
$$

Understanding these sensitivities enables effective volatility trading and risk management.

---

## Further Reading


- Hull, J.C. *Options, Futures, and Other Derivatives*. Chapter on Greeks.
- Taleb, N.N. *Dynamic Hedging*. Comprehensive treatment of vega and higher-order Greeks.
- Gatheral, J. *The Volatility Surface*. Model-consistent Greeks in stochastic volatility.
- Bergomi, L. *Stochastic Volatility Modeling*. Advanced treatment of volatility sensitivities.
