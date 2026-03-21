# Skew and Smile


## Introduction


The **volatility smile** and **volatility skew** describe how implied volatility varies with strike price $K$ for a fixed maturity $T$. These cross-sectional features of the volatility surface are among the most striking empirical violations of the Black-Scholes model, which predicts constant volatility across all strikes. The shape of the smile reveals fundamental information about the risk-neutral distribution, market beliefs about tail risks, and the dynamics of the underlying asset.

## Definitions and Terminology


### 1. Volatility Smile


A **volatility smile** refers to the U-shaped pattern where:


$$
\sigma_{\text{IV}}(K) > \sigma_{\text{IV}}(K_{\text{ATM}}) \quad \text{for } K \text{ far from } K_{\text{ATM}}
$$



Both deep in-the-money (ITM) and out-of-the-money (OTM) options have higher implied volatility than at-the-money (ATM) options.

**Graphically:** Plotting $\sigma_{\text{IV}}$ vs $K$ produces a smile-like curve with minimum at ATM.

**Markets:** Foreign exchange (FX), commodities, interest rates

### 2. Volatility Skew


A **volatility skew** refers to a monotonic pattern where:


$$
\frac{\partial \sigma_{\text{IV}}}{\partial K} \neq 0
$$



**Downward skew (negative skew):**

$$
\frac{\partial \sigma_{\text{IV}}}{\partial K} < 0
$$


OTM puts (low strikes) have higher IV than OTM calls (high strikes).

**Upward skew (positive skew):**

$$
\frac{\partial \sigma_{\text{IV}}}{\partial K} > 0
$$


Less common; sometimes seen in commodity markets.

**Markets:** Equity indices exhibit strong downward skew

### 3. Smirk


A **smirk** combines skew and smile:
- Asymmetric smile
- OTM puts have much higher IV than ATM
- OTM calls have moderately higher IV than ATM
- Net effect: downward sloping with curvature

**Markets:** Post-1987 equity options

## Mathematical Characterization


### 1. Moneyness Coordinates


To compare across different spot levels and maturities, use **moneyness**:

**Log-moneyness:**

$$
y = \ln\left(\frac{K}{F}\right) = \ln K - \ln S_0 - (r - q)T
$$



**Standardized moneyness:**

$$
m = \frac{K - F}{\sigma_{\text{ATM}} F \sqrt{T}}
$$



**Delta-moneyness:** Using Black-Scholes delta:

$$
\Delta_{\text{call}} = e^{-qT} \Phi(d_1)
$$



Common conventions: 25-delta, 10-delta for wings.

### 2. Smile Parametrization


Define the **smile function**:


$$
\sigma(y, T) := \sigma_{\text{IV}}(K = F e^y, T)
$$



where $y$ is log-moneyness and $F = S_0 e^{(r-q)T}$ is the forward.

**Symmetry:** A symmetric smile satisfies:

$$
\sigma(y, T) = \sigma(-y, T)
$$



**Skew:** Measured by the first derivative:

$$
\mathcal{S}(T) := \frac{\partial \sigma}{\partial y}\bigg|_{y=0}
$$



Negative $\mathcal{S}$ indicates downward skew.

**Curvature:** Measured by the second derivative:

$$
\mathcal{C}(T) := \frac{\partial^2 \sigma}{\partial y^2}\bigg|_{y=0}
$$



Positive $\mathcal{C}$ indicates convexity (smile).

### 3. Taylor Expansion Around ATM


For small $y$ (near ATM):


$$
\sigma(y, T) = \sigma_{\text{ATM}}(T) + \mathcal{S}(T) y + \frac{1}{2} \mathcal{C}(T) y^2 + O(y^3)
$$



**Interpretation:**
- $\sigma_{\text{ATM}}$: Volatility level
- $\mathcal{S}$: Linear skew (asymmetry)
- $\mathcal{C}$: Quadratic curvature (smile)

## Connection to Risk-Neutral Distribution


### 1. Moments and Smile Shape


From the Breeden-Litzenberger relationship, the smile encodes distributional properties:

**Variance (second moment):**

$$
\text{Var}(S_T) \leftrightarrow \sigma_{\text{ATM}}^2 T
$$



**Skewness (third moment):**

$$
\text{Skew}(S_T) \propto -\mathcal{S}(T)
$$



Negative skew parameter $\mathcal{S} < 0$ → negative distributional skewness.

**Kurtosis (fourth moment):**

$$
\text{Kurt}(S_T) - 3 \propto \mathcal{C}(T)
$$



Positive curvature $\mathcal{C} > 0$ → excess kurtosis (fat tails).

### 2. Tail Behavior


**Left tail (low strikes, $K \ll F$):**  
High implied volatility indicates the risk-neutral density assigns higher probability to large downward moves than the lognormal distribution.

**Right tail (high strikes, $K \gg F$):**  
High implied volatility indicates higher probability of large upward moves.

**Symmetric smile:** Both tails fatter than lognormal (jump risk, but no directional bias)

**Downward skew:** Left tail much fatter than right tail (crash risk)

## Empirical Patterns Across Asset Classes


### 1. Equity Indices


**Pre-1987:** Relatively flat smile (Black-Scholes appeared adequate)

**Post-1987:** Strong downward skew emerged after October 1987 crash

**Characteristics:**
- OTM puts (e.g., 90% strike) have IV 5-10 points higher than ATM
- OTM calls have IV close to ATM (minimal smile on upside)
- Shape: Downward sloping with slight curvature (smirk)

**Example (S&P 500, typical values):**
- ATM (100%): 18% IV
- 95% strike: 22% IV
- 90% strike: 26% IV
- 105% strike: 17% IV
- 110% strike: 16% IV

**Interpretation:** Market prices downside protection (put insurance) heavily.

### 2. Individual Equities


**Large-cap stocks:** Similar to index (downward skew, less pronounced)

**Small-cap stocks:** More symmetric smile (higher jump risk both directions)

**High-beta stocks:** Steeper skew (leverage to market downturns)

**Earnings announcements:** Temporary symmetric smile around event (binary outcomes)

### 3. Foreign Exchange (FX)


**Major pairs (EUR/USD, USD/JPY):**
- **Symmetric smile:** Both OTM puts and calls have elevated IV
- Reflects two-sided jump risk (currency can move sharply either direction)
- Risk reversals (25-delta) often close to zero

**Emerging market FX:**
- **Asymmetric smile:** Often skewed toward currency depreciation
- Reflects sovereign risk, capital flight fears

**Example (EUR/USD):**
- ATM: 10% IV
- 25-delta put: 11% IV
- 25-delta call: 11% IV
- Symmetric shape

### 4. Commodities


**Energy (crude oil):**
- Variable skew depending on supply/demand
- Sometimes upward skew (supply disruption fears)
- Sometimes downward skew (demand collapse fears)

**Precious metals (gold):**
- Mild upward skew or flat (safe-haven asset)
- OTM calls priced for tail risk hedging

**Agricultural:**
- Seasonal patterns
- Asymmetric based on weather risk direction

### 5. Interest Rates (Swaptions)


**Normal market:**
- Upward skew (rates can spike but rarely crash below zero)
- Post-2008: Negative rates complicate pattern

**High-rate environment:**
- Downward skew (rates expected to fall from high levels)

## Economic Drivers of Smile and Skew


### 1. Leverage Effect (Equity Skew)


**Mechanism:**  
As stock price $S$ falls, debt-to-equity ratio $D/E$ increases, making equity riskier. Volatility $\sigma$ increases.

**Mathematical formulation:**  
If $\sigma = \sigma(S)$ with $\frac{\partial \sigma}{\partial S} < 0$, then:


$$
dS = \mu S dt + \sigma(S) S dW
$$



generates negative correlation between returns and volatility.

**Smile implication:**  
Local volatility $\sigma_{\text{loc}}(K, T)$ is decreasing in $K$, producing downward skew in implied volatility.

**Empirical support:** Observed negative correlation $\rho(dS, d\sigma) < 0$ in equity markets.

### 2. Supply and Demand (Crashophobia)


**Mechanism:**  
Institutional investors buy OTM put options for portfolio insurance, driving up demand and prices.

**Smile implication:**  
Higher prices for OTM puts → higher implied volatility at low strikes.

**Evidence:** Skew steepens during market stress when hedging demand intensifies.

### 3. Jump Risk


**Mechanism:**  
Discontinuous price movements (earnings, geopolitical shocks) add kurtosis to the return distribution.

**Mathematical model:** Jump-diffusion:


$$
dS = \mu S dt + \sigma S dW + S dJ
$$



where $J$ is a compound Poisson process.

**Smile implication:**  
Jumps contribute to smile curvature $\mathcal{C} > 0$ (fat tails).

**Symmetric jumps:** Produce symmetric smile (FX)

**Asymmetric jumps:** Negative jumps more likely → downward skew (equity)

### 4. Volatility Risk Premium


**Mechanism:**  
Investors demand compensation for bearing volatility risk, leading to a wedge between risk-neutral and physical probabilities.

**Mathematical formulation:**  
Risk-neutral density $q(S)$ differs from physical density $p(S)$ by:


$$
q(S) = \frac{p(S) \cdot \xi(S)}{\int p(S') \xi(S') dS'}
$$



where $\xi(S)$ is the pricing kernel (marginal utility).

**Smile implication:**  
If $\xi(S)$ is decreasing and convex, generates both skew and smile.

## Parametric Smile Models


### 1. SVI (Stochastic Volatility Inspired)


The **SVI parametrization** (Gatheral, 2004) models total variance:


$$
w(y) = a + b\left(\rho(y - m) + \sqrt{(y - m)^2 + \sigma^2}\right)
$$



where:
- $y$: Log-moneyness
- $a$: Overall level
- $b$: Slope
- $\rho \in [-1, 1]$: Skew parameter
- $m$: ATM location
- $\sigma$: Smile width

**Implied volatility:**

$$
\sigma_{\text{IV}}(y, T) = \sqrt{\frac{w(y)}{T}}
$$



**Advantages:**
- Explicit formula
- No-arbitrage constraints easily enforced ($b(1 + |\rho|) < 4a$, etc.)
- Flexible enough to fit market data

**Limitations:**
- Single-maturity parametrization (doesn't enforce calendar arbitrage across maturities)

### 2. SSVI (Surface SVI)


The **SSVI parametrization** (Gatheral-Jacquier, 2014) extends SVI to the entire surface:


$$
w(y, T) = \frac{T}{2} \left\{ 1 + \rho \varphi(T) y + \sqrt{(\varphi(T) y + \rho)^2 + (1 - \rho^2)} \right\}
$$



where $\varphi(T)$ controls the ATM curvature as a function of maturity.

**Properties:**
- Arbitrage-free by construction (no butterfly or calendar arbitrage)
- Smooth across both $K$ and $T$
- Fits market data well with few parameters

### 3. SABR Model


The **SABR (Stochastic Alpha Beta Rho)** model:


$$
\begin{align}
dF_t &= \sigma_t F_t^\beta dW_t^1 \\
d\sigma_t &= \nu \sigma_t dW_t^2 \\
d\langle W^1, W^2 \rangle_t &= \rho dt
\end{align}
$$



generates an approximate implied volatility formula:


$$
\sigma_{\text{IV}}(K) \approx \frac{\alpha}{(FK)^{(1-\beta)/2}} \frac{z}{x(z)} \left\{ 1 + \left[ \frac{(1-\beta)^2}{24} \frac{\alpha^2}{(FK)^{1-\beta}} + \frac{\rho \beta \nu \alpha}{4(FK)^{(1-\beta)/2}} + \frac{2 - 3\rho^2}{24} \nu^2 \right] T \right\}
$$



where $z = \frac{\nu}{\alpha}(FK)^{(1-\beta)/2} \ln(F/K)$ and $x(z) = \ln\left(\frac{\sqrt{1 - 2\rho z + z^2} + z - \rho}{1 - \rho}\right)$.

**Parameters:**
- $\alpha$: ATM volatility
- $\beta \in [0, 1]$: CEV exponent (controls backbone)
- $\rho \in [-1, 1]$: Correlation (controls skew)
- $\nu$: Vol-of-vol (controls smile curvature)

**Widely used in:** Interest rate options, FX options

## Delta Conventions and Quotation


### 1. Delta and 10-Delta Options


In FX markets, options are quoted by delta rather than strike:

**25-delta call:** Strike $K$ such that $\Delta_{\text{call}}(K) = 0.25$

**25-delta put:** Strike $K$ such that $|\Delta_{\text{put}}(K)| = 0.25$

### 2. Risk Reversal


The **risk reversal (RR)** measures the skew:


$$
\text{RR}_{25} = \sigma_{\text{IV}}(\text{25-delta call}) - \sigma_{\text{IV}}(\text{25-delta put})
$$



**Interpretation:**
- $\text{RR} < 0$: Downward skew (put IV > call IV)
- $\text{RR} > 0$: Upward skew (call IV > put IV)
- $\text{RR} \approx 0$: Symmetric smile

**Typical values:**
- Equity: RR $\approx -3\%$ to $-5\%$ (negative)
- FX: RR $\approx 0\%$ (near symmetric)

### 3. Butterfly Spread


The **butterfly (BF)** measures the curvature:


$$
\text{BF}_{25} = \frac{\sigma_{\text{IV}}(\text{25-delta call}) + \sigma_{\text{IV}}(\text{25-delta put})}{2} - \sigma_{\text{IV}}(\text{ATM})
$$



**Interpretation:**
- $\text{BF} > 0$: Smile (wings elevated relative to ATM)
- $\text{BF} < 0$: Frown (wings depressed, rare)

**Typical values:**
- Equity: BF $\approx 1\%$ to $2\%$
- FX: BF $\approx 1\%$ to $3\%$
- Higher during crises

### 4. ATM Definition Ambiguity


**ATM conventions:**
1. **ATM forward:** $K = F = S_0 e^{(r-q)T}$
2. **ATM spot:** $K = S_0$
3. **ATM delta-neutral:** $K$ such that $\Delta_{\text{call}} = 0.5$

Different conventions give slightly different strikes and IVs. Market standard varies by product.

## Smile Dynamics


### 1. Sticky Strike


**Definition:** Implied volatility remains constant for each fixed strike as spot moves:


$$
\sigma_{\text{IV}}(K, t) = \sigma_{\text{IV}}(K, 0) \quad \text{independent of } S_t
$$



**Consequence:** As spot moves, the smile shifts in moneyness space.

**Generated by:** Local volatility models (Dupire)

**Implication for hedging:** Vega hedge depends only on the fixed strike structure.

### 2. Sticky Delta


**Definition:** Implied volatility remains constant for each fixed delta as spot moves:


$$
\sigma_{\text{IV}}(\Delta, t) = \sigma_{\text{IV}}(\Delta, 0)
$$



**Consequence:** The smile moves with the spot in strike space, maintaining constant shape in delta coordinates.

**Generated by:** Stochastic volatility models (Heston)

**Implication for hedging:** Vega hedge adjusts dynamically as spot moves.

### 3. Sticky Moneyness


**Definition:** Implied volatility depends only on moneyness $K/S$:


$$
\sigma_{\text{IV}}(K/S, t) = \sigma_{\text{IV}}(K/S, 0)
$$



**Intermediate case:** Smile shifts partially with spot.

**Empirical observation:** Real markets exhibit behavior between sticky-strike and sticky-delta, closer to sticky-delta.

## Asymptotic Analysis


### 1. Small-Maturity Asymptotics


For $T \to 0$, the smile is determined by the local volatility at the initial spot:


$$
\sigma_{\text{IV}}(K, T) \sim \sigma_{\text{loc}}(K, 0) \quad \text{as } T \to 0
$$



**Sharp smile:** If $\sigma_{\text{loc}}(K, 0)$ varies steeply with $K$, the short-dated smile is pronounced.

### 2. Large-Strike Asymptotics (Wings)


For $|y| = |\ln(K/F)| \to \infty$, **Lee's moment formula** gives:


$$
\lim_{y \to -\infty} \frac{\sigma_{\text{IV}}^2(y, T) T}{|y|} = 2 p_-
$$




$$
\lim_{y \to +\infty} \frac{\sigma_{\text{IV}}^2(y, T) T}{|y|} = 2 p_+
$$



where $p_\pm$ are related to the moments of the risk-neutral density.

**Implication:** The wings cannot be too flat; IV must grow at least as $\sqrt{|y|/T}$.

## Summary


The volatility smile and skew reveal:

### 1. **Empirical patterns:**


**Equity:** Downward skew (crashophobia, leverage effect)

$$
\sigma_{\text{IV}}(K) \text{ decreasing in } K
$$



**FX:** Symmetric smile (two-sided jump risk)

$$
\sigma_{\text{IV}}(y) = \sigma_{\text{IV}}(-y)
$$



**Commodities:** Variable (supply/demand asymmetries)

### 2. **Distributional interpretation:**


**Skew** $\mathcal{S} = \frac{\partial \sigma_{\text{IV}}}{\partial y}\big|_{\text{ATM}}$ ↔ **Third moment (skewness)**

**Curvature** $\mathcal{C} = \frac{\partial^2 \sigma_{\text{IV}}}{\partial y^2}\big|_{\text{ATM}}$ ↔ **Fourth moment (kurtosis)**

### 3. **Economic drivers:**

- Leverage effect
- Supply/demand for hedging
- Jump risk
- Volatility risk premium

### 4. **Parametric models:**

- **SVI/SSVI:** Tractable, arbitrage-free parametrization
- **SABR:** Stochastic vol model with closed-form approximation

### 5. **Dynamics:**

- **Sticky strike:** Local volatility behavior
- **Sticky delta:** Stochastic volatility behavior
- **Empirical:** Hybrid, closer to sticky-delta

The smile is not a static feature but encodes rich information about market beliefs, risk premia, and the dynamics of the underlying asset.
