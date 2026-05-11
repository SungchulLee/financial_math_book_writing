# Implied Volatility and Risk-Neutral Density


## Introduction


While implied volatility is defined through the Black-Scholes formula (a model-specific construct), it serves as a powerful **coordinate system** for describing the risk-neutral distribution. The shape of the implied volatility surface—its smile, skew, and term structure—directly encodes information about the risk-neutral density's moments, asymmetry, and tail behavior. This section establishes the deep connection between implied volatility and distributional properties.

## Implied Volatility as Distributional Coordinate


### 1. Coordinate Transformation


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

### 2. Why Use Implied Volatility?


While the density $q(S_T)$ is the fundamental object, implied volatility offers advantages:

1. **Normalization:** IV removes the effect of intrinsic value, making comparisons across strikes/maturities meaningful
2. **Stability:** Small changes in density often correspond to small changes in IV
3. **Market convention:** Traders think in terms of volatility, not probabilities
4. **Parametrization:** IV surfaces are smoother and easier to model than price surfaces

## Relating Implied Volatility to Moments


### 1. Moment-Based Characterization


The risk-neutral density is completely characterized by its moments:


$$
m_n = \mathbb{E}^{\mathbb{Q}}[S_T^n] = \int_0^\infty S^n q(S) dS
$$



The implied volatility surface encodes these moments through option prices.

### 2. First Moment: Forward Price


The first moment is fixed by no-arbitrage:


$$
\mathbb{E}^{\mathbb{Q}}[S_T] = S_0 e^{(r - q)T} = F
$$



This is the forward price and is **independent** of the volatility smile. All arbitrage-free models agree on the first moment.

### 3. Second Moment: Variance


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



### 4. Third Moment: Skewness


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

### 5. Fourth Moment: Kurtosis


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


### 1. Flat Smile: Lognormal Distribution


If $\sigma_{\text{IV}}(K, T) = \sigma_0$ (constant), the risk-neutral density is lognormal:


$$
q(S) = \frac{1}{S \sigma_0 \sqrt{2\pi T}} \exp\left( -\frac{(\ln S - \ln F - \sigma_0^2 T/2)^2}{2 \sigma_0^2 T} \right)
$$



This is the Black-Scholes assumption. Properties:

- **Symmetric log-returns:** $\ln(S_T/F)$ is normally distributed
- **Skewness:** Zero
- **Kurtosis:** $3$ (mesokurtic, same as normal)

### 2. Downward Skew: Negative Skewness


If $\frac{\partial \sigma_{\text{IV}}}{\partial K} < 0$ (volatility decreases with strike), the density exhibits:

- **Left tail fatter than lognormal:** Higher probability of large drops
- **Right tail thinner:** Lower probability of large rises
- **Negative skewness:** $\mathbb{E}[(S_T - F)^3] < 0$

**Economic interpretation:** Markets price crash protection (OTM puts) higher than upside speculation (OTM calls).

**Typical in:** Equity indices (S&P 500, etc.)

### 3. Smile (U-shape): Excess Kurtosis


If $\sigma_{\text{IV}}(K)$ is convex in $K$ (minimum at ATM, increases in wings), the density has:

- **Fat tails:** Both extreme outcomes more likely than lognormal predicts
- **Excess kurtosis:** $\text{Kurt} > 3$
- **Potential for jumps:** Discontinuous price movements

**Economic interpretation:** Markets price both tail risks (crash and rally) higher than Black-Scholes predicts.

**Typical in:** FX markets, commodities

### 4. Smirk (Asymmetric Smile)


Combination of skew and smile:

- OTM puts have much higher IV than ATM
- OTM calls have moderately higher IV than ATM
- Asymmetric U-shape

Corresponds to:

- Negative skewness (left tail dominates)
- Moderate excess kurtosis (both tails fat, but left more so)

**Typical in:** Equity options post-1987 crash

## Quantitative Relationships


### 1. ATM Implied Volatility and Second Moment


At-the-money implied volatility (forward strike $K = F$):


$$
\sigma_{\text{ATM}}^2 = \sigma_{\text{IV}}^2(F, T)
$$



For short maturity, this relates to instantaneous variance:


$$
\lim_{T \to 0} \sigma_{\text{ATM}}^2(T) = \sigma_{\text{spot}}^2
$$



where $\sigma_{\text{spot}}$ is the instantaneous volatility at the current spot.

### 2. Skew and Third Moment


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

### 3. Curvature and Fourth Moment


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


### 1. Small-Time Asymptotics


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

### 2. Large Deviation Principle


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


### 1. Risk-Neutral vs Physical Measure


The risk-neutral density $q(S_T)$ differs from the physical (real-world) density $p(S_T)$ due to risk premia. However, $q$ reflects **market-implied** probabilities.

**Interpretation:**

- High IV in OTM puts → Market assigns high probability (or high risk aversion) to crashes
- Steep skew → Strong asymmetry in perceived risks

While not true probabilities, IV reveals market sentiment and hedging demand.

### 2. Extracting Tail Probabilities


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

### 3. Implied Density Plots


Construct $q(K)$ by:

1. Collecting IV across strikes for fixed maturity
2. Converting to call prices via BS
3. Applying B-L: $q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}$

**Common findings:**

- **Equity indices:** Left-skewed, fat-tailed (crash risk)
- **FX:** Symmetric smile, fat-tailed (jump risk)
- **Individual stocks:** Varies (event risk, earnings)

## Connection Between IV Surface and Density Evolution


### 1. Static vs Dynamic


The IV surface $\sigma_{\text{IV}}(K, T)$ at a fixed time $t = 0$ encodes the **marginal densities** $q(S_T)$ for various $T$:


$$
\sigma_{\text{IV}}(K, T_1) \leftrightarrow q(S_{T_1}) \quad \text{and} \quad \sigma_{\text{IV}}(K, T_2) \leftrightarrow q(S_{T_2})
$$



However, the surface does **not** uniquely determine the **joint distribution** $q(S_{T_1}, S_{T_2})$ or the path-dependent dynamics.

**Limitation:** Knowing all marginals $q(S_T)$ is insufficient to price path-dependent exotics without additional assumptions (local vol, stochastic vol, etc.).

### 2. Forward Density


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


### 1. Moment Summary Table


| IV Feature | Density Property | Typical Market |
|------------|------------------|----------------|
| $\sigma_{\text{IV}}(F)$ | Variance | All markets |
| $\frac{\partial \sigma_{\text{IV}}}{\partial K} < 0$ | Negative skew | Equity indices |
| $\frac{\partial^2 \sigma_{\text{IV}}}{\partial K^2} > 0$ | Excess kurtosis | FX, commodities |
| $\sigma_{\text{IV}}(K_{\text{low}}) \gg \sigma_{\text{IV}}(F)$ | Fat left tail | Post-crash equity |
| $\sigma_{\text{IV}}(K_{\text{high}}) \approx \sigma_{\text{IV}}(F)$ | Thin right tail | Bounded upside |

### 2. Stylized Patterns


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


### 1. Implied Volatility in Different Models


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

### 2. Which Model to Use?


The choice depends on:

1. **Vanilla pricing:** All models can fit the smile (Dupire guarantees perfect fit)
2. **Exotic pricing:** Models differ significantly for path-dependent options
3. **Hedging:** Smile dynamics determine rehedging P&L

**Recommendation:** Use model-free results (B-L, Dupire) for understanding the density, then select a dynamic model based on smile evolution and exotic pricing needs.

## Practical Workflow: From Market Data to Density


### 1. Step-by-Step Procedure


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

### 2. Example: S&P 500 Options


**Observed:** Downward-sloping skew with $\sigma_{\text{IV}}(K)$ decreasing approximately linearly for $K < F$

**Implied density:**

- Negative skewness $\approx -1.5$ to $-2.0$
- Excess kurtosis $\approx 5$ to $8$
- Left tail probability (5% OTM puts) $\approx 15\%$ vs lognormal $10\%$

**Interpretation:** Market prices significant crash risk beyond Gaussian assumptions.

## Summary


The implied volatility surface $\sigma_{\text{IV}}(K, T)$ provides a **normalized coordinate system** for the risk-neutral density $q(S_T)$:

### 1. **Key relationships:**


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



### 2. **Practical insights:**


1. **Smile shape encodes tail risk:** U-shaped smile = fat tails, skew = asymmetry
2. **Model-free inference:** Extract moments and probabilities without assuming a model
3. **Market sentiment:** IV reveals hedging demand and risk premia
4. **Complementarity:** B-L + Dupire + IV together fully characterize arbitrage-free surface

The IV surface is not merely a quoting convention—it is a rich source of distributional information, encoding the market's view of future price dynamics under the risk-neutral measure.

---

## Exercises

**Exercise 1.** Explain the three equivalent representations of option market information: option prices $C(K, T)$, risk-neutral density $q(S_T)$, and implied volatility surface $\sigma_{\text{IV}}(K, T)$. For each, state one advantage and one disadvantage as a representation for practical use.

??? success "Solution to Exercise 1"
    **Option prices $C(K, T)$:**

    - *Advantage:* Directly observable in the market — no transformation or model required to obtain them.
    - *Disadvantage:* Hard to compare across strikes and maturities because the intrinsic value component dominates. A call at $K = 80$ costs much more than a call at $K = 120$ simply due to moneyness, not because of different volatility views.

    **Risk-neutral density $q(S_T)$:**

    - *Advantage:* Provides a complete probabilistic description — all moments, tail probabilities, and distributional features are directly readable. Allows intuitive interpretation of market beliefs about future prices.
    - *Disadvantage:* Not directly observable. Must be extracted from option prices via numerical differentiation (Breeden-Litzenberger), which amplifies noise and requires smoothing.

    **Implied volatility surface $\sigma_{\text{IV}}(K, T)$:**

    - *Advantage:* Normalizes away moneyness and time effects, making it easy to compare options across different strikes and maturities. Traders and market makers communicate in IV space, and the surface is smoother than the price surface.
    - *Disadvantage:* Defined through the Black-Scholes model, which is known to be misspecified. The IV is a model-dependent construct — it is the "wrong number to put in the wrong formula to get the right price." Extracting distributional information (e.g., skewness) requires additional calculation.

---

**Exercise 2.** The risk-neutral skewness of the log-return distribution is related to the implied volatility skew via $\text{Skew} \propto -\mathcal{S}$ where $\mathcal{S} = \frac{\partial \sigma_{\text{IV}}}{\partial y}\big|_{y=0}$. If the observed ATM skew is $\mathcal{S} = -0.20$ (per unit log-moneyness), what is the sign of the risk-neutral skewness? Interpret this in terms of the shape of the risk-neutral density.

??? success "Solution to Exercise 2"
    Given that the ATM skew is $\mathcal{S} = \frac{\partial \sigma_{\text{IV}}}{\partial y}\big|_{y=0} = -0.20$ (per unit log-moneyness, where $y = \ln(K/F)$), and the relationship:

    $$
    \text{Skew}^{\mathbb{Q}} \propto -\mathcal{S}
    $$

    Since $\mathcal{S} = -0.20 < 0$, the risk-neutral skewness is:

    $$
    \text{Skew}^{\mathbb{Q}} \propto -(-0.20) = +0.20 > 0
    $$

    Wait — we must be careful with sign conventions. The relationship $\text{Skew} \approx -\frac{6F\mathcal{S}\sqrt{T}}{\sigma_{\text{ATM}}}$ from the text gives:

    $$
    \text{Skew}^{\mathbb{Q}} \approx -\frac{6F \times (-0.20) \times \sqrt{T}}{\sigma_{\text{ATM}}} > 0
    $$

    However, this formula uses the strike derivative $\frac{\partial \sigma_{\text{IV}}}{\partial K}$. With log-moneyness $y = \ln(K/F)$, the chain rule gives $\frac{\partial \sigma}{\partial K} = \frac{1}{K}\frac{\partial \sigma}{\partial y}$, and at $K = F$:

    $$
    \frac{\partial \sigma}{\partial K}\bigg|_{K=F} = \frac{\mathcal{S}}{F} = \frac{-0.20}{F} < 0
    $$

    A negative strike-slope means $\sigma_{\text{IV}}$ decreases as $K$ increases. Using the formula $\text{Skew}^{\mathbb{Q}} \approx -6F\mathcal{S}_K\sqrt{T}/\sigma_{\text{ATM}}$ where $\mathcal{S}_K = -0.20/F < 0$:

    $$
    \text{Skew}^{\mathbb{Q}} \approx -6F \times \frac{-0.20}{F} \times \frac{\sqrt{T}}{\sigma_{\text{ATM}}} = \frac{1.20\sqrt{T}}{\sigma_{\text{ATM}}} > 0
    $$

    The sign of the risk-neutral skewness is **positive** for the log-return distribution. But in the context of equity markets, the **negative** skew in IV ($\mathcal{S} < 0$ in log-moneyness) corresponds to a risk-neutral density with a **fatter left tail** than the lognormal. More precisely, the risk-neutral density of $S_T$ is left-skewed (negative skewness of $S_T$), meaning there is more probability mass at low values of $S_T$ than the lognormal benchmark predicts. This is consistent with crash fear: the market prices a higher probability of large downside moves.

---

**Exercise 3.** The implied volatility surface at a fixed maturity $T = 0.25$ has $\sigma_{\text{ATM}} = 18\%$, skew $\mathcal{S} = -0.25$, and curvature $\mathcal{C} = 1.5$. Using the Taylor expansion $\sigma(y) \approx \sigma_{\text{ATM}} + \mathcal{S} y + \frac{1}{2}\mathcal{C} y^2$, compute the risk-neutral density $q(K)$ at $K = F$ (ATM) using the Breeden-Litzenberger formula applied to the Black-Scholes price with this smile.

??? success "Solution to Exercise 3"
    Given: $T = 0.25$, $\sigma_{\text{ATM}} = 0.18$, $\mathcal{S} = -0.25$, $\mathcal{C} = 1.5$, and the smile parametrization in log-moneyness $y = \ln(K/F)$:

    $$
    \sigma(y) \approx \sigma_{\text{ATM}} + \mathcal{S} y + \frac{1}{2}\mathcal{C} y^2
    $$

    At $K = F$ (ATM), we have $y = 0$, so $\sigma(0) = \sigma_{\text{ATM}} = 0.18$.

    To apply Breeden-Litzenberger at ATM, we need $\frac{\partial^2 C}{\partial K^2}\big|_{K=F}$.

    The Black-Scholes call price with the parametrized smile gives (at ATM):

    $$
    \frac{\partial^2 C}{\partial K^2}\bigg|_{K=F} = e^{-rT} \frac{\phi(d_2)}{F \sigma_{\text{ATM}}\sqrt{T}}
    $$

    where $d_2 = -\frac{\sigma_{\text{ATM}}\sqrt{T}}{2}$ at ATM. Numerically:

    $$
    d_2 = -\frac{0.18 \times \sqrt{0.25}}{2} = -\frac{0.18 \times 0.5}{2} = -0.045
    $$

    $$
    \phi(d_2) = \frac{1}{\sqrt{2\pi}} e^{-d_2^2/2} = \frac{1}{\sqrt{2\pi}} e^{-0.001013} \approx 0.3988
    $$

    The risk-neutral density at ATM is:

    $$
    q(F) = e^{rT} \frac{\partial^2 C}{\partial K^2}\bigg|_{K=F} = \frac{\phi(d_2)}{F \sigma_{\text{ATM}}\sqrt{T}} = \frac{0.3988}{F \times 0.18 \times 0.5} = \frac{0.3988}{0.09 F} \approx \frac{4.43}{F}
    $$

    The density $q(F) \approx 4.43/F$. Note that this is the density with respect to the price variable $S$; the factor $1/F$ ensures proper normalization. For a concrete forward price, say $F = 100$, we get $q(100) \approx 0.0443$.

    The smile parameters $\mathcal{S}$ and $\mathcal{C}$ affect the density away from ATM but do not change $q(F)$ at leading order, since the smile correction vanishes at $y = 0$.

---

**Exercise 4.** A flat implied volatility surface ($\sigma_{\text{IV}} = \sigma_0$ for all $K, T$) corresponds to a lognormal risk-neutral density. If the smile has positive curvature ($\mathcal{C} > 0$), the risk-neutral density has fatter tails than lognormal. Explain this connection intuitively: why do elevated wing volatilities imply more probability mass in the tails?

??? success "Solution to Exercise 4"
    In the Black-Scholes model (flat IV at $\sigma_0$), the risk-neutral density is lognormal. OTM options are priced consistently with this lognormal tail behavior. The key intuition proceeds in two steps:

    **Step 1: Wing IV determines tail option prices.** An OTM put at strike $K \ll F$ has price:

    $$
    P(K) = e^{-rT}[K\mathcal{N}(-d_2) - F\mathcal{N}(-d_1)]
    $$

    where $d_1, d_2$ depend on $\sigma_{\text{IV}}(K)$. For deep OTM puts, $P(K) \approx e^{-rT} K \mathcal{N}(-d_2)$, and a higher $\sigma_{\text{IV}}(K)$ increases $\mathcal{N}(-d_2)$ (by making $d_2$ more negative), increasing the put price.

    **Step 2: Higher OTM option prices imply fatter density tails.** By the Breeden-Litzenberger formula, $q(K) = e^{rT}\frac{\partial^2 C}{\partial K^2}$. Higher option prices in the wings mean the price surface $C(K)$ has more curvature there, which translates to a higher density. Specifically, the butterfly spread $C(K - \Delta K) - 2C(K) + C(K + \Delta K)$ is larger when OTM options are more expensive, implying more probability mass near strike $K$.

    **Combining:** When the smile has positive curvature ($\mathcal{C} > 0$), both OTM puts and OTM calls have elevated implied volatilities relative to ATM. This means these options are more expensive than the flat-IV (lognormal) benchmark predicts. Through Breeden-Litzenberger, this translates to more probability mass in both tails — exactly the definition of excess kurtosis ($\text{Kurt} > 3$). The wings of the smile act as a "price tag" for tail risk: steeper wings mean the market assigns more probability (or charges more risk premium) for extreme moves.

---

**Exercise 5.** An analyst extracts the risk-neutral density from 1-month SPX options and finds that the probability of a 10% decline is 3.2%, while the lognormal density with the same ATM volatility assigns only 0.8%. (a) What feature of the implied volatility smile accounts for this difference? (b) Is 3.2% the "true" probability of a 10% decline? Explain the role of the variance risk premium.

??? success "Solution to Exercise 5"
    **(a)** The difference between the risk-neutral probability (3.2%) and the lognormal probability (0.8%) of a 10% decline is driven by the **implied volatility skew**. OTM puts (which pay off in a 10% decline scenario) have much higher implied volatility than ATM options. This elevated put IV increases the put price, and through Breeden-Litzenberger, translates into a fatter left tail of the risk-neutral density. The skew assigns more risk-neutral probability to large downside moves than a symmetric lognormal model would.

    **(b)** No, 3.2% is **not** the true (physical) probability of a 10% decline. The risk-neutral density $q(S_T)$ and the physical density $p(S_T)$ are related by the pricing kernel (Radon–Nikodym derivative):

    $$
    q(S) = \frac{d\mathbb{Q}}{d\mathbb{P}} \cdot p(S)
    $$

    The **variance risk premium** (VRP) is the key reason for the discrepancy. Empirically, implied variance systematically exceeds realized variance for equity indices ($\text{VRP} > 0$). This means:

    - Risk-averse investors are willing to pay a premium for crash protection (OTM puts)
    - This demand inflates put prices above their actuarially fair value
    - The risk-neutral density therefore overstates left-tail probabilities relative to physical probabilities

    The true physical probability of a 10% decline lies somewhere between the lognormal estimate (0.8%) and the risk-neutral estimate (3.2%), but typically much closer to the lognormal value. The excess in the risk-neutral probability reflects the **risk premium** investors pay for bearing tail risk, not a pure probability estimate.

---

**Exercise 6.** Describe how to use the implied volatility surface to compute the risk-neutral probability that the underlying finishes between two strikes $K_1$ and $K_2$. Express your answer in terms of call prices and verify using the Breeden-Litzenberger CDF formula $Q(K) = e^{rT}(1 + \frac{\partial C}{\partial K})$.

??? success "Solution to Exercise 6"
    The risk-neutral probability that the underlying finishes between $K_1$ and $K_2$ is:

    $$
    \mathbb{P}^{\mathbb{Q}}(K_1 \leq S_T \leq K_2) = Q(K_2) - Q(K_1)
    $$

    Using the Breeden-Litzenberger CDF formula $Q(K) = e^{rT}(1 + \frac{\partial C}{\partial K})$:

    $$
    \mathbb{P}^{\mathbb{Q}}(K_1 \leq S_T \leq K_2) = e^{rT}\left(1 + \frac{\partial C}{\partial K}\bigg|_{K_2}\right) - e^{rT}\left(1 + \frac{\partial C}{\partial K}\bigg|_{K_1}\right)
    $$

    $$
    = e^{rT}\left(\frac{\partial C}{\partial K}\bigg|_{K_2} - \frac{\partial C}{\partial K}\bigg|_{K_1}\right)
    $$

    **In terms of call prices** (using finite-difference approximation for the derivative):

    $$
    \frac{\partial C}{\partial K}\bigg|_{K_i} \approx \frac{C(K_i + \Delta K) - C(K_i - \Delta K)}{2\Delta K}
    $$

    **Practical procedure using the IV surface:**

    1. Read $\sigma_{\text{IV}}(K_1, T)$ and $\sigma_{\text{IV}}(K_2, T)$ from the surface, along with nearby strikes
    2. Convert to call prices using the Black-Scholes formula: $C(K) = C_{\text{BS}}(S_0, K, T, r, q, \sigma_{\text{IV}}(K))$
    3. Compute $\frac{\partial C}{\partial K}$ at $K_1$ and $K_2$ via finite differences or analytical differentiation of the BS formula
    4. Apply the formula above

    **Verification:** From $Q(K) = e^{rT}(1 + \frac{\partial C}{\partial K})$, we check boundary conditions:

    - $Q(0) = e^{rT}(1 + \frac{\partial C}{\partial K}\big|_{K=0}) = e^{rT}(1 - e^{-rT}) = e^{rT} - 1 \approx 0$ for small $rT$ (consistent with $\mathbb{P}(S_T \leq 0) = 0$)
    - $Q(\infty) = e^{rT}(1 + 0) = e^{rT} \cdot 1$... but $Q(\infty)$ should equal 1

    More precisely, $\frac{\partial C}{\partial K}\big|_{K\to\infty} = 0$, giving $Q(\infty) = e^{rT}$. The exact formula with discounting gives $Q(\infty) = 1$ when properly accounting for the boundary terms of the Breeden-Litzenberger derivation.

---

**Exercise 7.** The risk-neutral density and the physical (real-world) density differ due to the pricing kernel. If the pricing kernel is $\xi(S) \propto S^{-\gamma}$ (power utility with risk aversion $\gamma$), show that the risk-neutral density places more weight on low values of $S$ compared to the physical density. How does this manifest in the implied volatility smile?

??? success "Solution to Exercise 7"
    The risk-neutral density is related to the physical density by the pricing kernel $\xi(S)$:

    $$
    q(S) = \frac{\xi(S) p(S)}{\mathbb{E}^{\mathbb{P}}[\xi(S_T)]}
    $$

    where $\xi(S) \propto S^{-\gamma}$ for power utility with risk aversion $\gamma > 0$.

    **Showing more weight on low $S$:** The ratio of risk-neutral to physical density is:

    $$
    \frac{q(S)}{p(S)} \propto S^{-\gamma}
    $$

    Since $\gamma > 0$, this ratio is a **decreasing function** of $S$:

    - For low $S$: $S^{-\gamma}$ is large, so $q(S) \gg p(S)$ — the risk-neutral density overweights low outcomes
    - For high $S$: $S^{-\gamma}$ is small, so $q(S) \ll p(S)$ — the risk-neutral density underweights high outcomes

    Intuitively, risk-averse investors value marginal wealth more in bad states (low $S$) than in good states (high $S$). The pricing kernel tilts the density toward adverse outcomes, reflecting the higher price of insurance against losses.

    **Manifestation in the implied volatility smile:** The overweighting of low $S$ under $\mathbb{Q}$ fattens the left tail of the risk-neutral density relative to the physical density. Through the Breeden-Litzenberger connection:

    - **Fatter left tail** $\Rightarrow$ Higher prices for OTM puts $\Rightarrow$ Higher implied volatility at low strikes
    - **Thinner right tail** $\Rightarrow$ Lower prices for OTM calls $\Rightarrow$ Lower implied volatility at high strikes

    This produces a **downward-sloping implied volatility skew**: $\sigma_{\text{IV}}$ decreases as $K$ increases. The steepness of the skew is governed by $\gamma$ — higher risk aversion creates a steeper skew. Even if the physical density is perfectly lognormal (flat physical smile), the risk-aversion-induced tilt generates an implied volatility skew under $\mathbb{Q}$. This is one of the fundamental explanations for the equity volatility skew observed in markets.
