# Implied Volatility and Risk-Neutral Density

## Introduction

While implied volatility is defined through the Black-Scholes formula (a model-specific construct), it serves as a powerful **coordinate system** for describing the risk-neutral distribution. The shape of the implied volatility surface—its smile, skew, and term structure—directly encodes information about the risk-neutral density's moments, asymmetry, and tail behavior. This section establishes the deep connection between implied volatility and distributional properties.

## Implied Volatility as Distributional Coordinate

### Coordinate Transformation

The map from option prices to implied volatilities:


$$
C(K, T) \xrightarrow{\mathcal{C}^{-1}} \sigma_{\text{IV}}(K, T)
$$



transforms the price surface into the implied volatility surface. Combined with Breeden-Litzenberger:


$$
\text{Prices } C(K, T) \xrightarrow{\text{B-L}} \text{Density } q(K, T) \xrightarrow{\text{encode}} \text{IV Surface } \sigma_{\text{IV}}(K, T)
$$



**Key insight:** The same information is represented in three equivalent ways:
1. **Option prices** $C(K, T)$: Direct market observables
2. **Risk-neutral density** $q(S_T)$: Probabilistic description
3. **Implied volatility** $\sigma_{\text{IV}}(K, T)$: Normalized quoting convention

### Why Use Implied Volatility?

While the density $q(S_T)$ is the fundamental object, implied volatility offers advantages:

1. **Normalization:** IV removes the effect of intrinsic value, making comparisons across strikes/maturities meaningful
2. **Stability:** Small changes in density often correspond to small changes in IV
3. **Market convention:** Traders think in terms of volatility, not probabilities
4. **Parametrization:** IV surfaces are smoother and easier to model than price surfaces

## Relating Implied Volatility to Moments

### Moment-Based Characterization

The risk-neutral density is completely characterized by its moments:


$$
m_n = \mathbb{E}^{\mathbb{Q}}[S_T^n] = \int_0^\infty S^n q(S) dS
$$



The implied volatility surface encodes these moments through option prices.

### First Moment: Forward Price

The first moment is fixed by no-arbitrage:


$$
\mathbb{E}^{\mathbb{Q}}[S_T] = S_0 e^{(r - q)T} = F
$$



This is the forward price and is **independent** of the volatility smile. All arbitrage-free models agree on the first moment.

### Second Moment: Variance

The second moment (variance) is related to the **model-free implied variance**:


$$
\text{Var}^{\mathbb{Q}}(S_T) = \mathbb{E}^{\mathbb{Q}}[S_T^2] - F^2
$$



Carr and Madan show this can be computed from option prices via:


$$
\text{Var}^{\mathbb{Q}}(S_T) = 2 e^{rT} \left( \int_0^F \frac{P(K)}{K^2} dK + \int_F^\infty \frac{C(K)}{K^2} dK \right)
$$



This integral is the **variance swap** payoff, directly observable from the smile.

**Connection to ATM IV:**

For small $T$, the ATM implied volatility approximates the square root of the variance:


$$
\sigma_{\text{IV}}(F, T) \approx \sqrt{\frac{\text{Var}^{\mathbb{Q}}(S_T)}{F^2 T}}
$$



### Third Moment: Skewness

The third central moment measures asymmetry:


$$
\text{Skew}^{\mathbb{Q}} = \frac{\mathbb{E}^{\mathbb{Q}}[(S_T - F)^3]}{(\text{Var}^{\mathbb{Q}}(S_T))^{3/2}}
$$



**Empirical relationship:** Negative skewness (left tail heavier) corresponds to:
- **Downward sloping IV skew:** $\frac{\partial \sigma_{\text{IV}}}{\partial K} < 0$ for $K < F$
- **Equity markets:** Typically exhibit negative skew (crash fear)

**Mathematical connection:** Bakshi, Kapadia, and Madan (2003) show:


$$
\mathbb{E}^{\mathbb{Q}}[(S_T - F)^3] = 6 e^{rT} \left( \int_0^F \frac{(F - K)^2 P(K)}{K^2} dK + \int_F^\infty \frac{(K - F)^2 C(K)}{K^2} dK \right)
$$



This integral weights OTM options, which are directly affected by the skew.

### Fourth Moment: Kurtosis

The fourth moment measures tail heaviness:


$$
\text{Kurt}^{\mathbb{Q}} = \frac{\mathbb{E}^{\mathbb{Q}}[(S_T - F)^4]}{(\text{Var}^{\mathbb{Q}}(S_T))^2}
$$



**Relationship to smile:** Excess kurtosis (fat tails, $\text{Kurt} > 3$) manifests as:
- **Volatility smile:** Both OTM puts and calls have higher IV than ATM
- **Symmetric wings:** $\sigma_{\text{IV}}(K)$ increases as $|K - F|$ increases

**Log contract representation:**


$$
\mathbb{E}^{\mathbb{Q}}[(S_T - F)^4] \propto \int_0^\infty \frac{(K - F)^4 \max(C(K), P(K))}{K^2} dK
$$



Deep OTM options contribute heavily, reflecting tail risk.

## Smile Patterns and Distributional Shapes

### Flat Smile: Lognormal Distribution

If $\sigma_{\text{IV}}(K, T) = \sigma_0$ (constant), the risk-neutral density is lognormal:


$$
q(S) = \frac{1}{S \sigma_0 \sqrt{2\pi T}} \exp\left( -\frac{(\ln S - \ln F - \sigma_0^2 T/2)^2}{2 \sigma_0^2 T} \right)
$$



This is the Black-Scholes assumption. Properties:
- **Symmetric log-returns:** $\ln(S_T/F)$ is normally distributed
- **Skewness:** Zero
- **Kurtosis:** $3$ (mesokurtic, same as normal)

### Downward Skew: Negative Skewness

If $\frac{\partial \sigma_{\text{IV}}}{\partial K} < 0$ (volatility decreases with strike), the density exhibits:
- **Left tail fatter than lognormal:** Higher probability of large drops
- **Right tail thinner:** Lower probability of large rises
- **Negative skewness:** $\mathbb{E}[(S_T - F)^3] < 0$

**Economic interpretation:** Markets price crash protection (OTM puts) higher than upside speculation (OTM calls).

**Typical in:** Equity indices (S&P 500, etc.)

### Smile (U-shape): Excess Kurtosis

If $\sigma_{\text{IV}}(K)$ is convex in $K$ (minimum at ATM, increases in wings), the density has:
- **Fat tails:** Both extreme outcomes more likely than lognormal predicts
- **Excess kurtosis:** $\text{Kurt} > 3$
- **Potential for jumps:** Discontinuous price movements

**Economic interpretation:** Markets price both tail risks (crash and rally) higher than Black-Scholes predicts.

**Typical in:** FX markets, commodities

### Smirk (Asymmetric Smile)

Combination of skew and smile:
- OTM puts have much higher IV than ATM
- OTM calls have moderately higher IV than ATM
- Asymmetric U-shape

Corresponds to:
- Negative skewness (left tail dominates)
- Moderate excess kurtosis (both tails fat, but left more so)

**Typical in:** Equity options post-1987 crash

## Quantitative Relationships

### ATM Implied Volatility and Second Moment

At-the-money implied volatility (forward strike $K = F$):


$$
\sigma_{\text{ATM}}^2 = \sigma_{\text{IV}}^2(F, T)
$$



For short maturity, this relates to instantaneous variance:


$$
\lim_{T \to 0} \sigma_{\text{ATM}}^2(T) = \sigma_{\text{spot}}^2
$$



where $\sigma_{\text{spot}}$ is the instantaneous volatility at the current spot.

### Skew and Third Moment

The **slope of the skew** at ATM:


$$
\mathcal{S} := \frac{\partial \sigma_{\text{IV}}}{\partial K}\bigg|_{K=F}
$$



relates to skewness through:


$$
\text{Skew}^{\mathbb{Q}} \approx -\frac{6 F \mathcal{S} \sqrt{T}}{\sigma_{\text{ATM}}}
$$



for small $T$ (asymptotic expansion).

**Interpretation:** Steeper downward skew → more negative skewness.

### Curvature and Fourth Moment

The **curvature of the smile** at ATM:


$$
\mathcal{C} := \frac{\partial^2 \sigma_{\text{IV}}}{\partial K^2}\bigg|_{K=F}
$$



relates to kurtosis:


$$
\text{Kurt}^{\mathbb{Q}} - 3 \approx 12 F^2 \mathcal{C} T
$$



**Interpretation:** Positive curvature (convex smile) → excess kurtosis → fat tails.

## Asymptotic Expansions

### Small-Time Asymptotics

For $T \to 0$, the implied volatility admits an expansion:


$$
\sigma_{\text{IV}}(K, T) = \sigma_0(K) + \sigma_1(K) T + \sigma_2(K) T^2 + O(T^3)
$$



The leading term $\sigma_0(K)$ is determined by the **initial local volatility**:


$$
\sigma_0(K) = \sigma_{\text{loc}}(K, 0)
$$



Higher-order terms $\sigma_1(K), \sigma_2(K)$ depend on derivatives of $\sigma_{\text{loc}}$.

**Connection to density:** As $T \to 0$, the density concentrates around $S_0$, and the smile encodes information about the local volatility function.

### Large Deviation Principle

For large strikes ($K \gg F$), the implied volatility behaves as:


$$
\sigma_{\text{IV}}^2(K, T) T \sim \frac{2 |\ln(K/F)|}{T} \quad \text{as } K \to \infty
$$



This is **Lee's moment formula**, ensuring that the density has finite variance:


$$
\mathbb{E}^{\mathbb{Q}}[S_T^2] < \infty
$$



**Interpretation:** The wings cannot be too flat; IV must grow with $|K - F|$ to prevent infinite variance.

## Using IV to Infer Market Beliefs

### Risk-Neutral vs Physical Measure

The risk-neutral density $q(S_T)$ differs from the physical (real-world) density $p(S_T)$ due to risk premia. However, $q$ reflects **market-implied** probabilities.

**Interpretation:**
- High IV in OTM puts → Market assigns high probability (or high risk aversion) to crashes
- Steep skew → Strong asymmetry in perceived risks

While not true probabilities, IV reveals market sentiment and hedging demand.

### Extracting Tail Probabilities

Define the **implied tail probability** of large moves:


$$
\mathbb{Q}(S_T < K_{\text{low}}) = \int_0^{K_{\text{low}}} q(S) dS
$$



Using Breeden-Litzenberger:


$$
\mathbb{Q}(S_T < K) = 1 + e^{rT} \frac{\partial C}{\partial K}\bigg|_K
$$



**From IV:** Convert $\sigma_{\text{IV}}(K_{\text{low}}, T)$ to $C(K_{\text{low}})$ via Black-Scholes, then differentiate.

Example: If 1-month 10%-OTM put has $\sigma_{\text{IV}} = 30\%$ vs ATM $\sigma_{\text{IV}} = 20\%$, the market implies higher tail probability than lognormal with $20\%$ vol.

### Implied Density Plots

Construct $q(K)$ by:
1. Collecting IV across strikes for fixed maturity
2. Converting to call prices via BS
3. Applying B-L: $q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}$

**Common findings:**
- **Equity indices:** Left-skewed, fat-tailed (crash risk)
- **FX:** Symmetric smile, fat-tailed (jump risk)
- **Individual stocks:** Varies (event risk, earnings)

## Connection Between IV Surface and Density Evolution

### Static vs Dynamic

The IV surface $\sigma_{\text{IV}}(K, T)$ at a fixed time $t = 0$ encodes the **marginal densities** $q(S_T)$ for various $T$:


$$
\sigma_{\text{IV}}(K, T_1) \leftrightarrow q(S_{T_1}) \quad \text{and} \quad \sigma_{\text{IV}}(K, T_2) \leftrightarrow q(S_{T_2})
$$



However, the surface does **not** uniquely determine the **joint distribution** $q(S_{T_1}, S_{T_2})$ or the path-dependent dynamics.

**Limitation:** Knowing all marginals $q(S_T)$ is insufficient to price path-dependent exotics without additional assumptions (local vol, stochastic vol, etc.).

### Forward Density

The **forward density** (conditional on survival to time $t$):


$$
q(S_T \mid S_t) = \frac{q(S_T, S_t)}{q(S_t)}
$$



can be inferred from **forward-starting options**:


$$
C_{\text{fwd}}(K, t, T) = e^{-r(T - t)} \mathbb{E}^{\mathbb{Q}}[\max(S_T - K, 0) \mid \mathcal{F}_t]
$$



The forward IV surface $\sigma_{\text{IV}}^{\text{fwd}}(K; t, T)$ encodes $q(S_T \mid S_t)$.

## Smile and Distributional Summary Statistics

### Moment Summary Table

| IV Feature | Density Property | Typical Market |
|------------|------------------|----------------|
| $\sigma_{\text{IV}}(F)$ | Variance | All markets |
| $\frac{\partial \sigma_{\text{IV}}}{\partial K} < 0$ | Negative skew | Equity indices |
| $\frac{\partial^2 \sigma_{\text{IV}}}{\partial K^2} > 0$ | Excess kurtosis | FX, commodities |
| $\sigma_{\text{IV}}(K_{\text{low}}) \gg \sigma_{\text{IV}}(F)$ | Fat left tail | Post-crash equity |
| $\sigma_{\text{IV}}(K_{\text{high}}) \approx \sigma_{\text{IV}}(F)$ | Thin right tail | Bounded upside |

### Stylized Patterns

**Black-Scholes (flat IV):**
- Density: Lognormal
- Skew: 0
- Kurtosis: 3

**Equity smile (downward skew):**
- Density: Negatively skewed, left tail fat
- Skew: $< 0$
- Kurtosis: $> 3$

**FX smile (symmetric U-shape):**
- Density: Symmetric, both tails fat
- Skew: $\approx 0$
- Kurtosis: $\gg 3$

**Commodity (volatile):**
- Density: Highly skewed or bimodal
- Skew: Varies
- Kurtosis: Very high

## Model Consistency

### Implied Volatility in Different Models

Different models generate different IV surfaces even with the same marginal density $q(S_T)$:

**Black-Scholes:**

$$
\sigma_{\text{IV}}(K, T) = \sigma \quad \text{(flat)}
$$



**Local Volatility:**

$$
\sigma_{\text{IV}}(K, T) \text{ determined by } \sigma_{\text{loc}}(S, t) \text{ via Dupire}
$$


- Generates sticky-strike smile dynamics

**Heston (Stochastic Volatility):**

$$
\sigma_{\text{IV}}(K, T) \text{ determined by } (\kappa, \theta, \xi, \rho, v_0)
$$


- Generates more realistic smile dynamics (sticky-delta)

**Jump-Diffusion (Merton):**

$$
\sigma_{\text{IV}}(K, T) \text{ exhibits convexity from jumps}
$$


- Smile curvature increases with jump intensity

### Which Model to Use?

The choice depends on:
1. **Vanilla pricing:** All models can fit the smile (Dupire guarantees perfect fit)
2. **Exotic pricing:** Models differ significantly for path-dependent options
3. **Hedging:** Smile dynamics determine rehedging P&L

**Recommendation:** Use model-free results (B-L, Dupire) for understanding the density, then select a dynamic model based on smile evolution and exotic pricing needs.

## Practical Workflow: From Market Data to Density

### Step-by-Step Procedure

**Step 1: Collect IV data**  
Observe implied volatilities $\{\sigma_{\text{IV}}(K_i, T_j)\}$ from market quotes

**Step 2: Convert IV to prices**  
Use Black-Scholes formula:

$$
C(K_i, T_j) = C_{\text{BS}}(S_0, K_i, T_j, r, q, \sigma_{\text{IV}}(K_i, T_j))
$$



**Step 3: Interpolate/Smooth**  
Fit arbitrage-free surface $C(K, T)$ using splines or parametric models

**Step 4: Extract density via B-L**  

$$
q(K, T) = e^{rT} \frac{\partial^2 C}{\partial K^2}\bigg|_{(K, T)}
$$



**Step 5: Compute moments**  

$$
m_n(T) = \int_0^\infty K^n q(K, T) dK
$$



**Step 6: Analyze distributional properties**  
Compute skewness, kurtosis, tail probabilities, VaR, etc.

### Example: S&P 500 Options

**Observed:** Downward-sloping skew with $\sigma_{\text{IV}}(K)$ decreasing approximately linearly for $K < F$

**Implied density:**
- Negative skewness $\approx -1.5$ to $-2.0$
- Excess kurtosis $\approx 5$ to $8$
- Left tail probability (5% OTM puts) $\approx 15\%$ vs lognormal $10\%$

**Interpretation:** Market prices significant crash risk beyond Gaussian assumptions.

## Summary

The implied volatility surface $\sigma_{\text{IV}}(K, T)$ provides a **normalized coordinate system** for the risk-neutral density $q(S_T)$:

### **Key relationships:**

**Variance:**

$$
\text{Var}^{\mathbb{Q}}(S_T) \leftrightarrow \sigma_{\text{IV}}(F, T)
$$



**Skewness:**

$$
\text{Skew}^{\mathbb{Q}} \leftrightarrow \frac{\partial \sigma_{\text{IV}}}{\partial K}
$$



**Kurtosis:**

$$
\text{Kurt}^{\mathbb{Q}} \leftrightarrow \frac{\partial^2 \sigma_{\text{IV}}}{\partial K^2}
$$



### **Practical insights:**

1. **Smile shape encodes tail risk:** U-shaped smile = fat tails, skew = asymmetry
2. **Model-free inference:** Extract moments and probabilities without assuming a model
3. **Market sentiment:** IV reveals hedging demand and risk premia
4. **Complementarity:** B-L + Dupire + IV together fully characterize arbitrage-free surface

The IV surface is not merely a quoting convention—it is a rich source of distributional information, encoding the market's view of future price dynamics under the risk-neutral measure.
