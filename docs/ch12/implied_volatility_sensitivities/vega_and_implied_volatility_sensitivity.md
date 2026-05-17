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


Recall (see [§ Greeks in Black-Scholes](../../ch10/greeks/greeks_in_black_scholes_model.md)): the closed-form BS vega is $\mathcal{V}_{\text{BS}} = S_0 e^{-qT} \phi(d_1) \sqrt{T} = K e^{-rT} \phi(d_2)\sqrt{T}$, with $d_1, d_2$ the standard BS quantities. It is positive for both calls and puts, symmetric in $d_1$ (since $\phi(-x)=\phi(x)$), and maximized when $d_1\approx 0$.

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


Recall (see [§ Gamma and Vega Hedging](../../ch11/hedging_strategies/gamma_and_vega_hedging.md) and [§ Portfolio Hedging and Cross-Greeks](../../ch11/hedging_strategies/portfolio_hedging_and_cross_greeks.md)) for the mechanics of single-instrument vega neutralization, $\sqrt{T}$-weighted hedging across maturities, multi-instrument bucket hedges, and the liquidity / transaction-cost / delta-gamma-interaction considerations. The application here is to use **vega buckets across the implied-volatility surface** (by strike and maturity) rather than a single aggregated vega.

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

---

## Exercises

**Exercise 1.** For a European call with $S_0 = 100$, $K = 100$, $T = 0.25$, $r = 5\%$, $q = 0$, and $\sigma = 20\%$, compute the Black-Scholes vega using

$$
\mathcal{V}_{\text{BS}} = S_0 e^{-qT} \phi(d_1) \sqrt{T}
$$

Verify that a 1 percentage point increase in implied volatility (20% to 21%) changes the option price by approximately $\mathcal{V} \times 0.01$.

??? success "Solution to Exercise 1"
    We have $S_0 = 100$, $K = 100$, $T = 0.25$, $r = 0.05$, $q = 0$, and $\sigma = 0.20$.

    First compute $d_1$:

    $$
    d_1 = \frac{\ln(100/100) + (0.05 + 0.02)\times 0.25}{0.20 \times 0.5} = \frac{0 + 0.0175}{0.10} = 0.175
    $$

    The standard normal density at $d_1 = 0.175$ is:

    $$
    \phi(0.175) = \frac{1}{\sqrt{2\pi}} e^{-0.175^2/2} = \frac{1}{\sqrt{2\pi}} e^{-0.0153} \approx 0.3945
    $$

    Since $q = 0$, the vega is:

    $$
    \mathcal{V}_{\text{BS}} = S_0 \,\phi(d_1)\,\sqrt{T} = 100 \times 0.3945 \times 0.5 = 19.73
    $$

    For a 1 percentage point increase ($\Delta\sigma = 0.01$):

    $$
    \Delta P \approx \mathcal{V} \times 0.01 = 19.73 \times 0.01 = 0.1973
    $$

    So the option price increases by approximately $\$0.20$ when implied volatility moves from 20% to 21%, confirming the linear approximation.

---

**Exercise 2.** Using the same parameters as Exercise 1, compute vega at strikes $K = 85, 90, 95, 100, 105, 110, 115$. Plot the results and confirm that vega is maximized at or near ATM. At which strike does vega drop below half of the ATM value?

??? success "Solution to Exercise 2"
    Using $S_0 = 100$, $T = 0.25$, $r = 0.05$, $q = 0$, and $\sigma = 0.20$, we compute $d_1$ and vega at each strike.

    The formula is $d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}$ and $\mathcal{V} = S_0\,\phi(d_1)\sqrt{T}$.

    | $K$ | $d_1$ | $\phi(d_1)$ | $\mathcal{V}$ |
    |-----|-------|-------------|----------------|
    | 85  | 1.80  | 0.079       | 3.95           |
    | 90  | 1.28  | 0.176       | 8.78           |
    | 95  | 0.73  | 0.307       | 15.34          |
    | 100 | 0.175 | 0.394       | 19.73          |
    | 105 | $-0.38$ | 0.370     | 18.50          |
    | 110 | $-0.93$ | 0.258     | 12.91          |
    | 115 | $-1.49$ | 0.131     | 6.56           |

    Vega is maximized at $K = 100$ (ATM). Half of the ATM vega is $19.73/2 \approx 9.87$. From the table, vega drops below this threshold at $K = 90$ ($\mathcal{V} = 8.78$) and $K = 110$ ($\mathcal{V} = 12.91$). On the low side, the strike where vega first drops below half ATM is approximately $K = 90$.

---

**Exercise 3.** Compute the vanna for an ATM call with $S_0 = K = 100$, $T = 0.5$, $r = 3\%$, $q = 0$, and $\sigma = 25\%$ using

$$
\text{Vanna} = -\frac{\mathcal{V} \cdot d_2}{S \cdot \sigma \cdot \sqrt{T}}
$$

Interpret the sign: if the spot increases by \$1 while volatility simultaneously increases by 1%, what is the approximate effect on the option's delta?

??? success "Solution to Exercise 3"
    We have $S_0 = K = 100$, $T = 0.5$, $r = 0.03$, $q = 0$, and $\sigma = 0.25$.

    Compute $d_1$ and $d_2$:

    $$
    d_1 = \frac{\ln(1) + (0.03 + 0.03125)\times 0.5}{0.25\sqrt{0.5}} = \frac{0.030625}{0.17678} \approx 0.1733
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T} = 0.1733 - 0.17678 \approx -0.0035
    $$

    Vega:

    $$
    \mathcal{V} = 100 \times \phi(0.1733) \times \sqrt{0.5} \approx 100 \times 0.3940 \times 0.7071 \approx 27.86
    $$

    Vanna:

    $$
    \text{Vanna} = -\frac{\mathcal{V}\cdot d_2}{S\cdot\sigma\cdot\sqrt{T}} = -\frac{27.86 \times (-0.0035)}{100 \times 0.25 \times 0.7071} = \frac{0.0975}{17.678} \approx 0.0055
    $$

    The vanna is positive (small). If spot increases by $\$1$ ($\Delta S = 1$) while volatility simultaneously increases by 1% ($\Delta\sigma = 0.01$), the approximate effect on delta is:

    $$
    \Delta(\Delta) \approx \text{Vanna}\times\Delta\sigma = 0.0055 \times 0.01 \approx 0.000055
    $$

    The effect is negligible at ATM because $d_2 \approx 0$. For options further from ATM, vanna is larger and the cross-effect is more significant.

---

**Exercise 4.** The volga (vomma) is given by $\text{Volga} = \mathcal{V} \cdot d_1 d_2 / \sigma$. (a) At ATM, show that $d_1 d_2 < 0$ for typical parameter values, so volga is negative. (b) For a deep OTM call with $K = 130$ (same parameters otherwise), show that $d_1 d_2 > 0$ and volga is positive. (c) Explain the economic meaning: why do OTM options benefit from "vol-of-vol"?

??? success "Solution to Exercise 4"
    **(a)** At ATM forward, we have approximately $d_1 \approx \sigma\sqrt{T}/2 > 0$ and $d_2 = d_1 - \sigma\sqrt{T} \approx -\sigma\sqrt{T}/2 < 0$. Therefore:

    $$
    d_1 d_2 \approx \frac{\sigma\sqrt{T}}{2}\times\left(-\frac{\sigma\sqrt{T}}{2}\right) = -\frac{\sigma^2 T}{4} < 0
    $$

    Since $\mathcal{V} > 0$ and $\sigma > 0$, the volga $\mathcal{V}\,d_1 d_2/\sigma < 0$ at ATM.

    **(b)** For a deep OTM call with $K = 130$, using $S_0 = 100$, $T = 0.25$, $r = 0.05$, $\sigma = 0.20$:

    $$
    d_1 = \frac{\ln(100/130) + 0.0175}{0.10} = \frac{-0.2624 + 0.0175}{0.10} = -2.449
    $$

    $$
    d_2 = -2.449 - 0.10 = -2.549
    $$

    Both $d_1 < 0$ and $d_2 < 0$, so $d_1 d_2 = (-2.449)(-2.549) = 6.24 > 0$ and volga is positive.

    **(c)** OTM options benefit from vol-of-vol because their value is convex in volatility. When volatility is low, they are very cheap (near zero). When volatility is high, they gain significant value. This asymmetry means that random fluctuations in volatility (vol-of-vol) raise the expected payoff of OTM options, making their fair value higher than what a constant-volatility model would predict. Positive volga reflects this convexity premium.

---

**Exercise 5.** A trading desk holds a portfolio with vega exposures: +\$200K in 1-month options and $-$\$150K in 6-month options. (a) Compute the parallel vega. (b) Compute the time-weighted vega $\mathcal{V}/\sqrt{T}$ for each bucket. (c) Is the portfolio at risk from a term structure steepening (short-dated vol up, long-dated vol down)? Explain.

??? success "Solution to Exercise 5"
    **(a)** Parallel vega is the sum of all vega exposures:

    $$
    \mathcal{V}_{\parallel} = +200{,}000 + (-150{,}000) = +\$50{,}000
    $$

    **(b)** Time-weighted vega $\mathcal{V}/\sqrt{T}$ for each bucket:

    - 1-month bucket ($T = 1/12$): $\mathcal{V}/\sqrt{T} = 200{,}000/\sqrt{1/12} = 200{,}000 \times \sqrt{12} \approx 200{,}000 \times 3.464 = \$692{,}800$
    - 6-month bucket ($T = 0.5$): $\mathcal{V}/\sqrt{T} = -150{,}000/\sqrt{0.5} = -150{,}000 \times 1.414 = -\$212{,}100$

    **(c)** Yes, the portfolio is significantly at risk from term structure steepening. If short-dated vol rises by $\Delta\sigma_{\text{short}}$ and long-dated vol falls by $\Delta\sigma_{\text{long}}$:

    $$
    \text{P\&L} \approx 200{,}000\times\Delta\sigma_{\text{short}} - 150{,}000\times|\Delta\sigma_{\text{long}}|
    $$

    A steepening (short up, long down) produces gains from the long short-dated position and gains from the short long-dated position, so the portfolio profits from steepening. Conversely, a flattening (short down, long up) would produce losses on both legs.

---

**Exercise 6.** In the Heston stochastic volatility model, identify three distinct "vegas": spot vol vega ($\partial P / \partial v_0$), long-run vol vega ($\partial P / \partial \theta$), and vol-of-vol vega ($\partial P / \partial \xi$). For a 1-year ATM option, which of these three sensitivities do you expect to be largest? Explain your reasoning based on the option's maturity relative to the mean-reversion time scale $1/\kappa$.

??? success "Solution to Exercise 6"
    In the Heston model, the variance follows $dv_t = \kappa(\theta - v_t)dt + \xi\sqrt{v_t}\,dW_t^v$. The three vegas are:

    - **Spot vol vega** ($\partial P/\partial v_0$): Sensitivity to the current instantaneous variance. For a 1-year option, this is the most direct and largest sensitivity because the option's near-term payoff distribution depends immediately on the current variance level.
    - **Long-run vol vega** ($\partial P/\partial \theta$): Sensitivity to the mean-reversion target. Its impact depends on how much time the option has for variance to revert. For a 1-year ATM option, if $1/\kappa$ is comparable to 1 year (e.g., $\kappa \approx 1$), then $\theta$ has moderate influence because variance partially reverts over the option's life.
    - **Vol-of-vol vega** ($\partial P/\partial \xi$): Sensitivity to the volatility of the variance process. This primarily affects the smile shape (convexity/wings) rather than the ATM level, so it tends to be smaller for ATM options.

    For a 1-year ATM option, the **spot vol vega** ($\partial P/\partial v_0$) is expected to be the largest. The current variance $v_0$ directly sets the volatility level over the near term and dominates the total integrated variance experienced by the option. The long-run vega becomes relatively more important only for very long-dated options (when $T \gg 1/\kappa$), and the vol-of-vol vega is more relevant for OTM options where smile curvature matters.

---

**Exercise 7.** An option has price $P = 5.20$, vega $\mathcal{V} = 18.0$, and volga $\text{Volga} = 3.5$. If implied volatility jumps from 22% to 27% (a large 5 percentage point move), compare the first-order approximation $\Delta P \approx \mathcal{V} \cdot \Delta\sigma$ with the second-order approximation $\Delta P \approx \mathcal{V} \cdot \Delta\sigma + \frac{1}{2}\text{Volga} \cdot (\Delta\sigma)^2$. By what percentage does the first-order approximation underestimate the true price change?

??? success "Solution to Exercise 7"
    The volatility move is $\Delta\sigma = 0.27 - 0.22 = 0.05$.

    **First-order approximation:**

    $$
    \Delta P_1 \approx \mathcal{V}\cdot\Delta\sigma = 18.0 \times 0.05 = 0.90
    $$

    **Second-order approximation:**

    $$
    \Delta P_2 \approx \mathcal{V}\cdot\Delta\sigma + \frac{1}{2}\text{Volga}\cdot(\Delta\sigma)^2 = 18.0\times 0.05 + \frac{1}{2}\times 3.5\times 0.05^2
    $$

    $$
    = 0.90 + \frac{1}{2}\times 3.5 \times 0.0025 = 0.90 + 0.004375 = 0.904375
    $$

    The first-order approximation gives $\Delta P_1 = 0.90$ while the second-order gives $\Delta P_2 \approx 0.9044$.

    The percentage underestimation by the first-order approximation (relative to the second-order estimate) is:

    $$
    \frac{0.9044 - 0.90}{0.9044}\times 100\% \approx 0.49\%
    $$

    The first-order approximation underestimates the price change by approximately 0.49%. The volga correction is small here because $(\Delta\sigma)^2 = 0.0025$ is modest, but for even larger vol moves or options with larger volga (e.g., deep OTM), the correction becomes more significant.
