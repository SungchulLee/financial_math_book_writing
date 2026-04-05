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

---

## Exercises

**Exercise 1.** Given a smile parametrized by $\sigma(y, T) = \sigma_{\text{ATM}} + \mathcal{S} \cdot y + \frac{1}{2}\mathcal{C} \cdot y^2$ with $\sigma_{\text{ATM}} = 0.20$, $\mathcal{S} = -0.15$, and $\mathcal{C} = 0.80$, compute the implied volatility at log-moneyness $y = -0.10$ (OTM put region) and $y = +0.10$ (OTM call region). Verify that the smile exhibits downward skew with positive curvature.

??? success "Solution to Exercise 1"
    We are given $\sigma_{\text{ATM}} = 0.20$, $\mathcal{S} = -0.15$, $\mathcal{C} = 0.80$, and the smile parametrization

    $$
    \sigma(y, T) = \sigma_{\text{ATM}} + \mathcal{S} \cdot y + \frac{1}{2}\mathcal{C} \cdot y^2
    $$

    **At $y = -0.10$ (OTM put region):**

    $$
    \sigma(-0.10) = 0.20 + (-0.15)(-0.10) + \frac{1}{2}(0.80)(0.01) = 0.20 + 0.015 + 0.004 = 0.219
    $$

    So the implied volatility is $21.9\%$.

    **At $y = +0.10$ (OTM call region):**

    $$
    \sigma(+0.10) = 0.20 + (-0.15)(0.10) + \frac{1}{2}(0.80)(0.01) = 0.20 - 0.015 + 0.004 = 0.189
    $$

    So the implied volatility is $18.9\%$.

    **Verification of downward skew:** The OTM put region ($y < 0$) has IV of 21.9%, which exceeds the ATM IV of 20.0%, which in turn exceeds the OTM call region IV of 18.9%. This confirms $\sigma(-0.10) > \sigma(0) > \sigma(+0.10)$, consistent with downward skew ($\mathcal{S} = -0.15 < 0$).

    **Verification of positive curvature:** Both wings have IV above the linear interpolation. The purely linear component gives $\sigma_{\text{linear}}(-0.10) = 0.215$ and $\sigma_{\text{linear}}(+0.10) = 0.185$. The quadratic term adds $+0.004$ to both, lifting the wings symmetrically. Since $\mathcal{C} = 0.80 > 0$, the smile is convex (U-shaped curvature superimposed on the skew).

---

**Exercise 2.** The risk reversal and butterfly are defined as $\text{RR}_{25} = \sigma_{25\Delta C} - \sigma_{25\Delta P}$ and $\text{BF}_{25} = \frac{1}{2}(\sigma_{25\Delta C} + \sigma_{25\Delta P}) - \sigma_{\text{ATM}}$. If $\sigma_{25\Delta P} = 25\%$, $\sigma_{\text{ATM}} = 18\%$, and $\sigma_{25\Delta C} = 17\%$, compute $\text{RR}_{25}$ and $\text{BF}_{25}$. Interpret the signs in terms of the skew direction and tail behavior of the risk-neutral distribution.

??? success "Solution to Exercise 2"
    We are given $\sigma_{25\Delta P} = 25\%$, $\sigma_{\text{ATM}} = 18\%$, and $\sigma_{25\Delta C} = 17\%$.

    **Risk reversal:**

    $$
    \text{RR}_{25} = \sigma_{25\Delta C} - \sigma_{25\Delta P} = 17\% - 25\% = -8\%
    $$

    **Butterfly:**

    $$
    \text{BF}_{25} = \frac{1}{2}(\sigma_{25\Delta C} + \sigma_{25\Delta P}) - \sigma_{\text{ATM}} = \frac{1}{2}(17\% + 25\%) - 18\% = 21\% - 18\% = 3\%
    $$

    **Interpretation of the risk reversal:** $\text{RR}_{25} = -8\% < 0$ indicates strong downward (negative) skew. The 25-delta put has much higher implied volatility than the 25-delta call, meaning the market prices downside risk more heavily than upside risk. This is characteristic of equity index options where "crashophobia" drives demand for OTM puts.

    **Interpretation of the butterfly:** $\text{BF}_{25} = 3\% > 0$ indicates a smile (wings elevated relative to ATM). The average IV of the two 25-delta options exceeds the ATM IV, reflecting fat tails in the risk-neutral distribution. The positive butterfly implies the market assigns higher probability to extreme moves (both up and down) than a lognormal distribution would predict, indicating excess kurtosis.

---

**Exercise 3.** Explain the relationship between the smile skew parameter $\mathcal{S}$ and the third moment (skewness) of the risk-neutral distribution, and between the curvature $\mathcal{C}$ and the fourth moment (kurtosis). For an equity index with skewness $-1.5$ and kurtosis $6.0$, predict the qualitative shape of the smile.

??? success "Solution to Exercise 3"
    **Skew and third moment:** The smile skew parameter $\mathcal{S} = \frac{\partial \sigma_{\text{IV}}}{\partial y}\big|_{y=0}$ is related to the third moment of the risk-neutral log-return distribution through the approximate relationship

    $$
    \text{Skew}(\ln S_T) \propto -\mathcal{S}(T)
    $$

    A negative $\mathcal{S}$ (downward skew, where OTM puts have higher IV) corresponds to negative skewness in the risk-neutral distribution. This is because higher IV at low strikes means the risk-neutral density assigns more probability to the left tail than a symmetric (lognormal) distribution would. The Breeden-Litzenberger relationship shows that $\frac{\partial^2 C}{\partial K^2}$ gives the risk-neutral density, and a steeper decline of IV with increasing $K$ translates to a left-skewed density.

    **Curvature and fourth moment:** The curvature parameter $\mathcal{C} = \frac{\partial^2 \sigma_{\text{IV}}}{\partial y^2}\big|_{y=0}$ is related to excess kurtosis:

    $$
    \text{Kurt}(\ln S_T) - 3 \propto \mathcal{C}(T)
    $$

    Positive curvature ($\mathcal{C} > 0$) means both wings of the smile are elevated relative to ATM, indicating that extreme outcomes (both tails) are more likely than under a lognormal model. This excess kurtosis reflects fat tails in the risk-neutral distribution.

    **Prediction for equity index with skewness $-1.5$ and kurtosis $6.0$:** Since skewness is strongly negative ($-1.5$), we expect $\mathcal{S} > 0$ in magnitude but negative in sign, producing steep downward skew (OTM puts significantly more expensive). Since kurtosis is $6.0$, the excess kurtosis is $6.0 - 3 = 3.0 > 0$, implying substantial positive curvature. The qualitative shape is a **smirk**: a steeply downward-sloping smile with notable curvature, where the left wing (OTM puts) is much higher than ATM, and the right wing (OTM calls) is only slightly elevated. This is the classic post-1987 equity index pattern.

---

**Exercise 4.** The SVI parametrization is $w(y) = a + b(\rho(y - m) + \sqrt{(y-m)^2 + \sigma^2})$. For parameters $a = 0.04$, $b = 0.10$, $\rho = -0.5$, $m = 0$, $\sigma = 0.2$, and $T = 1$: (a) compute the total variance $w(y)$ at $y = -0.2, 0, 0.2$; (b) convert to implied volatility via $\sigma_{\text{IV}} = \sqrt{w/T}$; (c) verify that the no-arbitrage condition $b(1 + |\rho|) < 4a$ is satisfied.

??? success "Solution to Exercise 4"
    We are given $a = 0.04$, $b = 0.10$, $\rho = -0.5$, $m = 0$, $\sigma = 0.2$, $T = 1$.

    **(a) Total variance at $y = -0.2, 0, 0.2$:**

    The SVI formula is $w(y) = a + b(\rho(y - m) + \sqrt{(y - m)^2 + \sigma^2})$.

    At $y = -0.2$:

    $$
    w(-0.2) = 0.04 + 0.10\left((-0.5)(-0.2) + \sqrt{(-0.2)^2 + 0.04}\right) = 0.04 + 0.10\left(0.1 + \sqrt{0.08}\right)
    $$

    Since $\sqrt{0.08} = 0.2828$:

    $$
    w(-0.2) = 0.04 + 0.10(0.1 + 0.2828) = 0.04 + 0.03828 = 0.07828
    $$

    At $y = 0$:

    $$
    w(0) = 0.04 + 0.10\left(0 + \sqrt{0 + 0.04}\right) = 0.04 + 0.10(0.2) = 0.04 + 0.02 = 0.06
    $$

    At $y = 0.2$:

    $$
    w(0.2) = 0.04 + 0.10\left((-0.5)(0.2) + \sqrt{0.04 + 0.04}\right) = 0.04 + 0.10\left(-0.1 + 0.2828\right) = 0.04 + 0.01828 = 0.05828
    $$

    **(b) Implied volatility:**

    Since $\sigma_{\text{IV}} = \sqrt{w/T}$ and $T = 1$:

    $$
    \sigma_{\text{IV}}(-0.2) = \sqrt{0.07828} = 0.2798 \approx 28.0\%
    $$

    $$
    \sigma_{\text{IV}}(0) = \sqrt{0.06} = 0.2449 \approx 24.5\%
    $$

    $$
    \sigma_{\text{IV}}(0.2) = \sqrt{0.05828} = 0.2414 \approx 24.1\%
    $$

    The OTM put region ($y = -0.2$) has the highest IV, confirming downward skew driven by $\rho = -0.5 < 0$.

    **(c) No-arbitrage condition:** The condition is $b(1 + |\rho|) < 4a$:

    $$
    0.10(1 + 0.5) = 0.10 \times 1.5 = 0.15
    $$

    $$
    4a = 4(0.04) = 0.16
    $$

    Since $0.15 < 0.16$, the no-arbitrage condition is satisfied.

---

**Exercise 5.** Compare the smile shapes across three asset classes: equity indices, major FX pairs, and commodities. For each, describe (a) the typical sign of $\mathcal{S}$ (skew), (b) the typical sign of $\mathcal{C}$ (curvature), (c) the dominant economic driver (leverage effect, jump risk, supply/demand, etc.).

??? success "Solution to Exercise 5"
    **(a) Equity indices:**

    - **Skew $\mathcal{S}$:** Strongly negative. OTM puts have much higher IV than OTM calls.
    - **Curvature $\mathcal{C}$:** Positive but moderate. Both wings are elevated, but the effect is asymmetric (left wing much higher).
    - **Dominant driver:** The leverage effect (as stock prices fall, debt-to-equity rises, increasing equity volatility) combined with crashophobia (institutional demand for portfolio insurance via OTM puts after the 1987 crash). The negative correlation $\rho(dS, d\sigma) < 0$ is the primary mechanism.

    **(b) Major FX pairs (EUR/USD, USD/JPY):**

    - **Skew $\mathcal{S}$:** Near zero. The smile is approximately symmetric around ATM.
    - **Curvature $\mathcal{C}$:** Positive and often larger than equities. Both wings are significantly elevated.
    - **Dominant driver:** Two-sided jump risk. Currencies can experience sharp moves in either direction due to central bank interventions, geopolitical events, or capital flow reversals. There is no structural asymmetry analogous to the leverage effect because a depreciation of one currency is simultaneously an appreciation of the other.

    **(c) Commodities:**

    - **Skew $\mathcal{S}$:** Variable, depends on the specific commodity and market conditions. Energy commodities may show positive skew (supply disruption fears push OTM call IV higher) or negative skew (demand collapse fears). Precious metals often show mild positive skew (safe-haven demand for upside exposure).
    - **Curvature $\mathcal{C}$:** Positive, reflecting jump risk from supply shocks, weather events, and geopolitical disruptions.
    - **Dominant driver:** Supply-demand asymmetries and physical constraints. Unlike financial assets, commodities have storage costs, delivery logistics, and physical supply limitations that create directional asymmetries specific to each market. Seasonal patterns (e.g., winter heating demand for natural gas) also play a role.

---

**Exercise 6.** In a jump-diffusion model $dS = \mu S \, dt + \sigma S \, dW + S \, dJ$ where the jump size has mean $m_J < 0$ (negative jumps), explain how this produces (a) negative skew in the implied volatility smile and (b) positive curvature (excess kurtosis). What happens to the smile shape if jumps are symmetric ($m_J = 0$)?

??? success "Solution to Exercise 6"
    In the jump-diffusion model $dS = \mu S \, dt + \sigma S \, dW + S \, dJ$ with negative mean jump size $m_J < 0$:

    **(a) Negative skew:** Negative jumps ($m_J < 0$) create an asymmetry in the risk-neutral return distribution. The left tail (large declines) is fattened more than the right tail because downward jumps are more likely or larger in magnitude. When the risk-neutral density has a heavier left tail, the Breeden-Litzenberger formula $q(K) = e^{rT} \frac{\partial^2 C}{\partial K^2}$ assigns more probability mass to low values of $S_T$. To match these higher probabilities at low strikes, implied volatility must be elevated for OTM puts (low $K$), producing $\frac{\partial \sigma_{\text{IV}}}{\partial K} < 0$, i.e., negative skew.

    Formally, the risk-neutral distribution under jump-diffusion is a mixture of lognormals (one for each number of jumps $n = 0, 1, 2, \ldots$). When $m_J < 0$, the component distributions with $n \geq 1$ jumps are shifted to the left, creating negative skewness in the mixture.

    **(b) Positive curvature (excess kurtosis):** Jumps, regardless of their direction, add mass to the tails of the distribution beyond what diffusion alone would produce. The compound Poisson component introduces discontinuous moves that create leptokurtosis (excess kurtosis $> 0$). Since kurtosis is related to the smile curvature via $\text{Kurt} - 3 \propto \mathcal{C}$, the curvature $\mathcal{C} > 0$, meaning both wings of the smile are elevated relative to ATM.

    Quantitatively, if the jump size has variance $\sigma_J^2$, the excess kurtosis of the return distribution scales as $\lambda \sigma_J^4 / (\sigma^2 + \lambda \sigma_J^2)^2$, which is always positive.

    **(c) Symmetric jumps ($m_J = 0$):** When the mean jump size is zero, the distribution remains symmetric (no skewness), so $\mathcal{S} \approx 0$. However, jumps still add kurtosis, so $\mathcal{C} > 0$ persists. The resulting smile is a symmetric U-shape, similar to what is observed in FX markets. Both OTM puts and OTM calls have elevated IV relative to ATM, but neither wing dominates the other.

---

**Exercise 7.** An options trader observes the following 3-month SPX implied volatilities: 90% strike = 26%, 95% strike = 22%, 100% (ATM) = 18%, 105% strike = 17%, 110% strike = 16.5%. (a) Compute the smile skew $\mathcal{S}$ as the slope between 95% and 105% strikes in log-moneyness. (b) Compute the smile curvature using the 90%, 100%, and 110% strikes. (c) Is this smile more consistent with equity skew (smirk) or FX smile (symmetric)?

??? success "Solution to Exercise 7"
    The given 3-month SPX implied volatilities are: 90% strike = 26%, 95% = 22%, 100% (ATM) = 18%, 105% = 17%, 110% = 16.5%.

    **(a) Smile skew $\mathcal{S}$:**

    Log-moneyness values (using moneyness $K/F$ where we approximate $F \approx S_0$):

    $$
    y_{95} = \ln(0.95) = -0.05129, \quad y_{105} = \ln(1.05) = 0.04879
    $$

    The slope between 95% and 105% strikes:

    $$
    \mathcal{S} \approx \frac{\sigma(y_{105}) - \sigma(y_{95})}{y_{105} - y_{95}} = \frac{0.17 - 0.22}{0.04879 - (-0.05129)} = \frac{-0.05}{0.10008} = -0.4996
    $$

    The smile skew is approximately $\mathcal{S} \approx -0.50$, indicating a steep downward slope.

    **(b) Smile curvature:**

    Using the 90%, 100%, and 110% strikes with log-moneyness $y_{90} = \ln(0.90) = -0.10536$ and $y_{110} = \ln(1.10) = 0.09531$:

    The second derivative is approximated by:

    $$
    \mathcal{C} \approx \frac{\sigma(y_{110}) - 2\sigma(0) + \sigma(y_{90})}{(\Delta y)^2}
    $$

    where $\Delta y \approx \frac{y_{110} - y_{90}}{2} = \frac{0.09531 + 0.10536}{2} = 0.10034$.

    $$
    \mathcal{C} \approx \frac{0.165 - 2(0.18) + 0.26}{(0.10034)^2} = \frac{0.065}{0.01007} \approx 6.45
    $$

    The curvature is positive and large, indicating a pronounced smile (elevated wings).

    **(c) Equity skew (smirk) vs. FX smile (symmetric):**

    This smile is clearly an **equity skew (smirk)**, not a symmetric FX smile. The evidence is:

    - The left wing is much more elevated than the right wing: IV at 90% strike (26%) is 8 points above ATM, while IV at 110% strike (16.5%) is only 1.5 points below ATM.
    - The skew is strongly negative ($\mathcal{S} \approx -0.50$), characteristic of equity index options.
    - A symmetric FX smile would have $\sigma(y) \approx \sigma(-y)$, but here $\sigma(y_{90}) = 26\%$ while $\sigma(y_{110}) = 16.5\%$, showing extreme asymmetry.
    - The pattern is consistent with post-1987 SPX crashophobia, where OTM puts command a large premium over OTM calls.
