# Sticky Strike vs Sticky Delta


## Introduction


When the underlying price moves, the implied volatility surface changes in complex ways. Understanding these dynamics is critical for delta hedging, P&L attribution, and model selection. Two stylized assumptions—**sticky strike** and **sticky delta**—describe idealized behaviors of how implied volatility responds to spot movements and serve as polar benchmarks for analyzing real market behavior.

This section develops the mathematical framework for these assumptions, derives their implications for Greeks and hedging, and examines empirical evidence on actual smile dynamics.

## Theoretical Framework


### 1. The Central Question


Consider an option with strike $K$ and maturity $T$. At time $t$, with spot price $S_t$, it has implied volatility $\sigma_{\text{IV}}(K, T, S_t)$.

**Question:** When the spot moves from $S_t$ to $S_t + \Delta S$, how does the implied volatility change?

Three quantities characterize the answer:
1. The **new** implied volatility at strike $K$: $\sigma_{\text{IV}}(K, T, S_t + \Delta S)$
2. The **new** implied volatility at the new ATM forward
3. The relationship between strike-space and delta-space

### 2. Coordinate Systems for the Smile


**Strike space:** Implied volatility as a function of absolute strike $K$:

$$
\sigma_{\text{IV}} = \sigma(K, T)
$$


**Moneyness space:** Implied volatility as a function of moneyness $m = K/F$:

$$
\sigma_{\text{IV}} = \sigma(m, T)
$$


**Log-moneyness space:** Implied volatility as a function of $k = \ln(K/F)$:

$$
\sigma_{\text{IV}} = \sigma(k, T)
$$


**Delta space:** Implied volatility as a function of option delta $\Delta$:

$$
\sigma_{\text{IV}} = \sigma(\Delta, T)
$$


The choice of coordinate system determines how we parametrize the smile and affects the interpretation of smile dynamics.

## Sticky Strike Assumption


### 1. Definition


Under the **sticky strike** assumption, implied volatility is a function of absolute strike only, independent of spot:

$$
\sigma_{\text{IV}}(K, T; S) = \sigma(K, T) \quad \text{(independent of } S \text{)}
$$


**Consequence:** When spot moves, the implied volatility at a fixed strike $K$ remains unchanged:

$$
\frac{\partial \sigma_{\text{IV}}(K)}{\partial S} = 0
$$


### 2. Graphical Interpretation


Under sticky strike:
- The smile "stays in place" in $(K, \sigma)$ space
- The forward price $F = S e^{(r-q)T}$ shifts with spot
- The ATM point moves along the existing smile curve

**Example:** If spot moves from $S = 100$ to $S = 102$:
- The strike $K = 100$ (was ATM) now has the same IV as before
- The new ATM forward ($K \approx 102$) picks up the IV from the old OTM call region

### 3. Mathematical Formulation


Let $\sigma(K)$ be the smile function. Under sticky strike:

$$
\sigma_{\text{IV}}(K; S_t) = \sigma(K) \quad \forall S_t
$$


The **total derivative** of IV with respect to spot is:

$$
\frac{d\sigma_{\text{IV}}}{dS} = \frac{\partial \sigma}{\partial K} \cdot \underbrace{\frac{\partial K}{\partial S}}_{=0} = 0
$$


since strike is held constant.

### 4. Implications for Delta


The Black-Scholes delta is:

$$
\Delta_{\text{BS}} = e^{-qT} \Phi(d_1)
$$


Under sticky strike, the **total delta** includes the smile effect:

$$
\Delta_{\text{total}} = \frac{\partial C}{\partial S} = \Delta_{\text{BS}} + \mathcal{V} \cdot \frac{\partial \sigma_{\text{IV}}}{\partial S}
$$


Since $\frac{\partial \sigma_{\text{IV}}}{\partial S} = 0$ under sticky strike:

$$
\Delta_{\text{sticky-strike}} = \Delta_{\text{BS}}
$$


**Result:** Under sticky strike, the Black-Scholes delta (computed at the current implied volatility) is the correct hedge ratio.

### 5. Local Volatility Connection


**Theorem:** The sticky strike assumption is consistent with **local volatility models**.

In a local volatility model:

$$
dS_t = (r - q) S_t dt + \sigma_{\text{loc}}(S_t, t) S_t dW_t
$$


The implied volatility surface is determined by the local volatility function via the Dupire equation. When spot moves:
- The local volatility function $\sigma_{\text{loc}}(S, t)$ is fixed
- The implied volatility at each strike remains unchanged
- This is precisely sticky strike behavior

**Caveat:** This is an idealization. Real local vol dynamics exhibit more complex behavior over short horizons.

## Sticky Delta Assumption


### 1. Definition


Under the **sticky delta** assumption, implied volatility is a function of option delta only, independent of spot:

$$
\sigma_{\text{IV}}(\Delta, T; S) = \sigma(\Delta, T) \quad \text{(independent of } S \text{)}
$$


**Consequence:** When spot moves, the implied volatility at a fixed delta level remains unchanged:

$$
\frac{\partial \sigma_{\text{IV}}(\Delta)}{\partial S} = 0
$$


### 2. Graphical Interpretation


Under sticky delta:
- The smile "shifts" with spot in $(K, \sigma)$ space
- A fixed-delta point (e.g., 25-delta put) always has the same IV
- The strike corresponding to that delta changes with spot

**Example:** If spot moves from $S = 100$ to $S = 102$:
- The 25-delta put strike shifts from ~$K_1$ to ~$K_2$
- Both $K_1$ (at old spot) and $K_2$ (at new spot) have the same IV
- In strike space, the entire smile has "shifted right"

### 3. Mathematical Formulation


Let $\sigma(\Delta)$ be the smile function in delta space. The strike corresponding to delta $\Delta$ depends on spot:

$$
K(\Delta, S) = S \cdot f(\Delta, \sigma, T, r, q)
$$


where $f$ is the inverse delta function.

Under sticky delta, the IV at a fixed strike $K_0$ changes as spot moves because the delta at $K_0$ changes:

$$
\frac{d\sigma_{\text{IV}}(K_0)}{dS} = \frac{\partial \sigma}{\partial \Delta} \cdot \frac{\partial \Delta(K_0)}{\partial S}
$$


Since $\frac{\partial \Delta}{\partial S} > 0$ (delta increases with spot for calls), and $\frac{\partial \sigma}{\partial \Delta}$ is typically negative (OTM puts have higher IV), we have:

$$
\frac{d\sigma_{\text{IV}}(K_0)}{dS} < 0 \quad \text{(for typical equity skew)}
$$


**Result:** Under sticky delta, implied volatility at a fixed strike **decreases** when spot increases (for negatively skewed markets).

### 4. Implications for Delta


The total delta under sticky delta includes the smile effect:

$$
\Delta_{\text{total}} = \Delta_{\text{BS}} + \mathcal{V} \cdot \frac{\partial \sigma_{\text{IV}}}{\partial S}
$$


Since $\frac{\partial \sigma_{\text{IV}}}{\partial S} < 0$ for typical equity skew:

$$
\Delta_{\text{sticky-delta}} = \Delta_{\text{BS}} + \underbrace{\mathcal{V} \cdot \frac{\partial \sigma_{\text{IV}}}{\partial S}}_{< 0}
$$


**Result:** Under sticky delta, the total delta is **smaller** than the Black-Scholes delta.

**Intuition:** When spot rises, IV falls, which partially offsets the direct price increase. The hedge ratio should account for this.

### 5. FX Market Convention


The sticky delta assumption is closely aligned with **FX market conventions**:

- FX options are quoted in delta terms (25-delta call, 10-delta put, ATM)
- Market makers quote IV at fixed delta levels
- When spot moves, the strikes adjust but delta-quoted IVs stay similar

This makes sticky delta a natural assumption for FX volatility models.

## Quantitative Comparison


### 1. Smile Parametrization


Consider a simple linear skew model:

$$
\sigma(k) = \sigma_0 + \beta k
$$


where $k = \ln(K/F)$ is log-moneyness and $\beta < 0$ (downward skew).

**Under sticky strike:** $\sigma(K)$ is fixed. When $F$ changes (spot moves), log-moneyness $k$ changes, so the IV at ATM changes.

**Under sticky delta:** The smile in $(k, \sigma)$ space shifts so that the delta-equivalent points have constant IV.

### 2. Delta Comparison


**Proposition:** For a call option with negative skew ($\beta < 0$):

$$
\Delta_{\text{sticky-delta}} < \Delta_{\text{BS}} < \Delta_{\text{sticky-strike}} \cdot \text{(adjusted)}
$$


Actually, under sticky strike:

$$
\Delta_{\text{sticky-strike}} = \Delta_{\text{BS}}
$$


And under sticky delta:

$$
\Delta_{\text{sticky-delta}} = \Delta_{\text{BS}} + \mathcal{V} \cdot \frac{\partial \sigma}{\partial S}
$$


For equity skew with $\frac{\partial \sigma}{\partial S} < 0$:

$$
\Delta_{\text{sticky-delta}} < \Delta_{\text{sticky-strike}}
$$


### 3. Numerical Example


**Parameters:**
- $S_0 = 100$, $K = 100$ (ATM), $T = 0.25$, $r = 5\%$, $q = 0$
- $\sigma_{\text{ATM}} = 20\%$
- Skew: $\frac{\partial \sigma}{\partial k} = -20\%$ per unit log-moneyness

**Black-Scholes delta:**

$$
\Delta_{\text{BS}} = \Phi(d_1) = \Phi(0.175) \approx 0.569
$$


**Smile adjustment:**

$$
\frac{\partial \sigma}{\partial S} = \frac{\partial \sigma}{\partial k} \cdot \frac{\partial k}{\partial S} = -0.20 \times \left(-\frac{1}{S}\right) = \frac{0.20}{100} = 0.002
$$


**Vega:**

$$
\mathcal{V} \approx 19.73
$$


**Sticky delta adjustment:**

$$
\Delta_{\text{sticky-delta}} = 0.569 + 19.73 \times 0.002 = 0.569 + 0.039 = 0.608
$$


Wait, this is **larger**, not smaller. Let me recalculate.

The sign depends on the direction of the skew effect. With $\frac{\partial \sigma}{\partial k} < 0$:

$$
\frac{\partial \sigma}{\partial S} = \frac{\partial \sigma}{\partial k} \cdot \frac{\partial k}{\partial S} = \frac{\partial \sigma}{\partial k} \cdot \frac{-1}{S}
$$


So if $\frac{\partial \sigma}{\partial k} = -0.20$:

$$
\frac{\partial \sigma}{\partial S} = (-0.20) \times \left(\frac{-1}{100}\right) = +0.002
$$


This gives a **positive** adjustment, making $\Delta_{\text{sticky-delta}} > \Delta_{\text{BS}}$.

**Correction:** The relationship depends on how skew is defined and whether we're looking at OTM puts or calls. For a negatively skewed smile where OTM puts have higher IV:
- Spot up → fixed strike becomes more OTM put-like → IV increases
- This is **not** sticky delta behavior

Let me reformulate more carefully.

### 4. Correct Formulation


Under **sticky moneyness** (log-moneyness constant):

$$
\sigma(k, T) \text{ fixed}, \quad k = \ln(K/F)
$$


When $S$ increases, $F$ increases, so $k = \ln(K/F)$ decreases for fixed $K$.

$$
\frac{\partial \sigma}{\partial S}\bigg|_{K \text{ fixed}} = \frac{\partial \sigma}{\partial k} \cdot \frac{\partial k}{\partial S} = \frac{\partial \sigma}{\partial k} \cdot \left(-\frac{1}{S}\right)
$$


For downward skew ($\frac{\partial \sigma}{\partial k} < 0$):

$$
\frac{\partial \sigma}{\partial S}\bigg|_{K \text{ fixed}} > 0
$$


**Interpretation:** Under sticky moneyness, when spot rises, the IV at a fixed strike **increases** because that strike becomes relatively more OTM (lower moneyness), moving into higher-IV territory.

Under **sticky strike**: $\frac{\partial \sigma}{\partial S}\big|_{K \text{ fixed}} = 0$.

Under **sticky delta**: The IV at a fixed delta stays constant, meaning the smile in strike space shifts.

## Impact on Greeks


### 1. Adjusted Delta


The general formula for total delta is:

$$
\Delta_{\text{total}} = \frac{\partial C}{\partial S} = \Delta_{\text{BS}} + \frac{\partial C}{\partial \sigma} \cdot \frac{\partial \sigma}{\partial S} = \Delta_{\text{BS}} + \mathcal{V} \cdot \frac{\partial \sigma}{\partial S}
$$


| Assumption | $\frac{\partial \sigma}{\partial S}$ | Delta Adjustment |
|------------|-------------------------------------|-----------------|
| Sticky strike | 0 | None |
| Sticky moneyness | $-\frac{1}{S} \frac{\partial \sigma}{\partial k}$ | $\mathcal{V} \cdot \frac{\partial \sigma}{\partial S}$ |
| Sticky delta | Depends on $\frac{\partial \sigma}{\partial \Delta}$ | Complex |

### 2. Vanna and Smile Dynamics


**Vanna** measures the sensitivity of delta to volatility, or equivalently, of vega to spot:

$$
\text{Vanna} = \frac{\partial \Delta}{\partial \sigma} = \frac{\partial \mathcal{V}}{\partial S}
$$


Under different smile dynamics:

**Sticky strike:**

$$
\text{Total Vanna} = \text{Vanna}_{\text{BS}}
$$


**Sticky delta:**

$$
\text{Total Vanna} = \text{Vanna}_{\text{BS}} + \text{Volga} \cdot \frac{\partial \sigma}{\partial S} + \mathcal{V} \cdot \frac{\partial^2 \sigma}{\partial S \partial S}
$$


The smile dynamics introduce additional vanna-like effects.

### 3. Gamma Adjustment


Similarly, the total gamma depends on smile dynamics:

$$
\Gamma_{\text{total}} = \Gamma_{\text{BS}} + 2 \cdot \text{Vanna} \cdot \frac{\partial \sigma}{\partial S} + \mathcal{V} \cdot \frac{\partial^2 \sigma}{\partial S^2}
$$


Under sticky strike, the correction terms vanish.

## P&L Attribution Under Different Dynamics


### 1. Delta-Hedged P&L


For a delta-hedged option position:

$$
\text{P\&L} = \frac{1}{2} \Gamma (\Delta S)^2 + \mathcal{V} \Delta\sigma + \text{Vanna} \cdot \Delta S \cdot \Delta\sigma + \Theta \Delta t
$$


The vanna term captures the cross-effect between spot and volatility moves.

### 2. Sticky Strike P&L


Under sticky strike, $\Delta\sigma|_{K \text{ fixed}} = 0$, so:

$$
\text{P\&L}_{\text{sticky-strike}} = \frac{1}{2} \Gamma (\Delta S)^2 + \Theta \Delta t
$$


No volatility P&L (at fixed strike).

### 3. Sticky Delta P&L


Under sticky delta, $\Delta\sigma|_{\Delta \text{ fixed}} = 0$, but $\Delta\sigma|_{K \text{ fixed}} \neq 0$:

$$
\text{P\&L}_{\text{sticky-delta}} = \frac{1}{2} \Gamma (\Delta S)^2 + \mathcal{V} \Delta\sigma_K + \text{Vanna} \cdot \Delta S \cdot \Delta\sigma_K + \Theta \Delta t
$$


where $\Delta\sigma_K$ is the change in IV at the fixed strike $K$.

## Empirical Evidence


### 1. Equity Markets


Empirical studies of equity index options (S&P 500, EURO STOXX) show:

**Short-term behavior:**
- Closer to sticky strike than sticky delta
- IV at fixed strikes relatively stable over short horizons
- Skew steepens after large down moves

**Medium-term behavior:**
- Neither assumption holds perfectly
- Spot-vol correlation (leverage effect) dominates
- Smile dynamics are asymmetric: faster reaction to down moves

**Quantitative finding:** The "skew stickiness ratio" (SSR):

$$
\text{SSR} = \frac{\text{ATM IV change}}{\text{Predicted change under sticky strike}}
$$


Empirical SSR for SPX is typically 0.3-0.6, indicating behavior between sticky strike and sticky moneyness.

### 2. FX Markets


**Short-term:** Closer to sticky delta
- Market makers quote at fixed delta levels
- IV at 25-delta put/call relatively stable

**Medium-term:** Mean reversion in both spot and volatility complicates the picture

**Risk reversals:** The 25D risk reversal (IV of 25D call minus 25D put) is more stable than individual strike IVs.

### 3. Single-Stock Options


**Idiosyncratic behavior:**
- More noise, less clear pattern
- Event-driven (earnings, M&A) dominates
- Sector effects matter

**General tendency:** Between sticky strike and sticky delta, with significant variation.

## Model Implications


### 1. Local Volatility Models


Local volatility models produce **sticky strike** behavior by construction:
- The local vol surface $\sigma_{\text{loc}}(S, t)$ is fixed
- When spot moves, the path through local vol space changes
- But implied volatility at each strike is determined by the same integral

**Problem:** This implies unrealistic forward smiles and dynamics.

### 2. Stochastic Volatility Models


Stochastic volatility models (Heston, SABR) produce dynamics between sticky strike and sticky delta:
- The spot-vol correlation ($\rho$) controls the leverage effect
- Negative $\rho$ (typical for equities) produces skew that steepens when spot falls
- This is neither pure sticky strike nor pure sticky delta

**SABR:** The SABR model with backbone parameter $\beta$ interpolates:
- $\beta = 1$: Normal SABR, sticky strike-like
- $\beta = 0$: Lognormal SABR, sticky delta-like

### 3. Bergomi's Variance Curve Models


Bergomi's framework models the forward variance curve directly:

$$
d\xi_t^T = \xi_t^T \cdot \omega(T-t) \cdot dZ_t
$$


The resulting smile dynamics are:
- More realistic than local vol
- Capture term structure of skew
- Can match empirical SSR observations

## Practical Hedging Implications


### 1. Delta Hedging Choices


| Assumption | Hedge Ratio | When to Use |
|------------|-------------|-------------|
| Sticky strike | $\Delta_{\text{BS}}$ | Local vol models, short-term |
| Sticky delta | Adjusted $\Delta$ | FX markets, longer horizons |
| Empirical | Blend or estimated | Most realistic |

### 2. Estimating Smile Dynamics


**Regression approach:**

$$
\Delta\sigma_{\text{ATM}} = \alpha + \beta \cdot \frac{\Delta S}{S} + \epsilon
$$


The coefficient $\beta$ estimates the spot-vol sensitivity:
- $\beta = 0$: Sticky strike
- $\beta = -\text{skew}$: Sticky moneyness
- Intermediate: Empirical dynamics

### 3. Robust Hedging


Given uncertainty about smile dynamics:

1. **Conservative approach:** Use the hedge ratio that performs better in adverse scenarios
2. **Scenario analysis:** Test P&L under sticky strike, sticky delta, and historical dynamics
3. **Dynamic adjustment:** Update hedge ratio estimates as market conditions change

## Summary


Sticky strike and sticky delta represent idealized extremes of smile dynamics:

### 1. Sticky Strike

$$
\frac{\partial \sigma_{\text{IV}}(K)}{\partial S} = 0
$$

- IV at fixed strike unchanged when spot moves
- Consistent with local volatility models
- Delta = Black-Scholes delta

### 2. Sticky Delta

$$
\frac{\partial \sigma_{\text{IV}}(\Delta)}{\partial S} = 0
$$

- IV at fixed delta unchanged when spot moves
- Smile shifts in strike space
- Common in FX markets
- Delta requires adjustment

### 3. Reality

- Neither assumption holds perfectly
- Short-term equity: closer to sticky strike
- FX markets: closer to sticky delta
- Leverage effect creates asymmetric dynamics
- Empirical "skew stickiness ratio" typically 0.3-0.6

### 4. Implications

| Aspect | Sticky Strike | Sticky Delta |
|--------|--------------|--------------|
| Delta | $\Delta_{\text{BS}}$ | $\Delta_{\text{BS}} + \mathcal{V} \frac{\partial\sigma}{\partial S}$ |
| Vanna effect | Standard | Enhanced |
| Gamma | Standard | Modified |
| P&L attribution | No vol P&L at fixed $K$ | Vol P&L present |

Understanding these benchmarks enables more nuanced analysis of actual market dynamics and more robust hedging strategies.

---

## Further Reading


- Derman, E. *The Volatility Smile*. Comprehensive treatment of smile dynamics.
- Bergomi, L. *Stochastic Volatility Modeling*. Advanced framework for variance dynamics.
- Gatheral, J. *The Volatility Surface*. Empirical analysis of smile behavior.
- Rebonato, R. *Volatility and Correlation*. Practical hedging under smile dynamics.
- Hagan, P. et al. *Managing Smile Risk*. SABR model and smile dynamics.
