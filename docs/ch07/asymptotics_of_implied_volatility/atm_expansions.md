# ATM Expansions

## Introduction

The **at-the-money (ATM) expansion** of implied volatility provides a detailed characterization of the smile near the forward price $F = S_0 e^{(r-q)T}$. This region is of paramount importance because:
- ATM options are the most liquid and actively traded
- ATM IV serves as the benchmark volatility level
- Near-ATM expansion connects to Greeks and hedging sensitivity
- The shape near ATM determines skew and curvature parameters

This section develops comprehensive asymptotic expansions for implied volatility in the neighborhood of the ATM strike, including connections to model parameters, moments, and practical applications.

## ATM Definition and Conventions

### Multiple ATM Definitions

**ATM Forward (Delta-Neutral):**

$$
K_{\text{ATM}} = F = S_0 e^{(r-q)T}
$$



This is the strike where the forward delta is zero: $\Delta_{\text{fwd}} = 0$.

**ATM Spot:**

$$
K_{\text{ATM}} = S_0
$$



Simply the current spot price.

**ATM Delta:**

$$
K_{\text{ATM}} = K \quad \text{such that } |\Delta(K)| = 0.5
$$



For Black-Scholes, this gives:


$$
K_{\text{ATM}} = S_0 e^{(r - q + \sigma^2/2)T}
$$



**Market convention:** ATM forward is most common for derivatives pricing; ATM delta for quoting.

Throughout this section, we use **ATM forward** ($K = F$) unless stated otherwise.

## Taylor Expansion Around ATM

### General Expansion in Log-Moneyness

Define log-moneyness relative to the forward:


$$
y = \ln(K/F)
$$



The implied volatility admits a Taylor expansion:


$$
\sigma_{\text{IV}}(y, T) = \sigma_{\text{ATM}}(T) + \frac{\partial \sigma}{\partial y}\bigg|_{y=0} y + \frac{1}{2} \frac{\partial^2 \sigma}{\partial y^2}\bigg|_{y=0} y^2 + \frac{1}{6} \frac{\partial^3 \sigma}{\partial y^3}\bigg|_{y=0} y^3 + O(y^4)
$$



**Notation:**


$$
\sigma(y) = \sigma_0 + \sigma_1 y + \frac{\sigma_2}{2} y^2 + \frac{\sigma_3}{6} y^3 + \cdots
$$



where:
- $\sigma_0 = \sigma_{\text{ATM}}$: ATM volatility level
- $\sigma_1 = \frac{\partial \sigma}{\partial y}\big|_{y=0}$: Skew parameter
- $\sigma_2 = \frac{\partial^2 \sigma}{\partial y^2}\big|_{y=0}$: Curvature parameter
- $\sigma_3 = \frac{\partial^3 \sigma}{\partial y^3}\big|_{y=0}$: Asymmetry of curvature

### Interpretation of Coefficients

**$\sigma_0$ (Level):**  
The baseline volatility for an ATM option. Reflects the overall uncertainty about the asset return.

**$\sigma_1$ (Skew):**  
The linear slope of the smile:
- $\sigma_1 < 0$: Downward skew (equity-like)
- $\sigma_1 > 0$: Upward skew (rare)
- $\sigma_1 = 0$: Symmetric smile

**$\sigma_2$ (Curvature):**  
The quadratic term controlling smile convexity:
- $\sigma_2 > 0$: U-shaped smile (FX-like)
- $\sigma_2 < 0$: Inverted smile (frown, rare)

**$\sigma_3$ (Skewness of Curvature):**  
Asymmetry in how the smile curves:
- $\sigma_3 \neq 0$: Different curvature on left vs right wing
- Typically small in practice

## Connection to Risk-Neutral Moments

### Moment Expansion

The risk-neutral distribution admits a moment expansion around the forward:


$$
S_T = F e^X
$$



where $X = \ln(S_T/F)$ has:
- Mean: $\mathbb{E}[X] = -\frac{1}{2}\text{Var}(X)$ (to ensure $\mathbb{E}[S_T] = F$)
- Variance: $\text{Var}(X) = \sigma_{\text{eff}}^2 T$
- Skewness: $\text{Skew}(X) = \gamma_3$
- Kurtosis: $\text{Kurt}(X) = \gamma_4$

### ATM Volatility and Variance

**Leading term:**


$$
\sigma_{\text{ATM}}^2 T \approx \text{Var}(X)
$$



**Exact relationship (Carr-Madan):**


$$
\sigma_{\text{ATM}}^2 T = \text{Var}(X) + O(T^2)
$$



For short maturities, ATM IV directly measures the variance of log-returns.

### Skew and Third Moment

**Theorem 4.4.10** (Skew-Skewness Relationship)  
For small $T$, the smile skew is related to distributional skewness by:


$$
\sigma_1 \approx -\frac{\gamma_3}{6 \sigma_{\text{ATM}}}
$$



where $\gamma_3 = \mathbb{E}[(X - \mathbb{E}[X])^3] / (\text{Var}(X))^{3/2}$ is the skewness coefficient.

**Proof sketch:** Expand the Black-Scholes call price in powers of $y$ and match to the cumulant-generating function. The cubic term in $y$ introduces the third cumulant (skewness). □

**Interpretation:**
- Negative skewness ($\gamma_3 < 0$) → Positive skew parameter ($\sigma_1 > 0$... wait, this is backwards)

**Correction:** The sign convention depends on definition. Using:


$$
\sigma(y) \approx \sigma_0 - \frac{\gamma_3}{6\sigma_0} y
$$



we have:
- Negative skewness ($\gamma_3 < 0$) → Negative smile skew ($\frac{d\sigma}{dy} < 0$)

This matches equity markets: left-skewed distribution → downward-sloping IV.

### Curvature and Fourth Moment

**Theorem 4.4.11** (Curvature-Kurtosis Relationship)  
The smile curvature relates to excess kurtosis:


$$
\sigma_2 \approx \frac{\gamma_4 - 3}{24 \sigma_{\text{ATM}}}
$$



where $\gamma_4 = \mathbb{E}[(X - \mathbb{E}[X])^4] / (\text{Var}(X))^2$ is the kurtosis.

**Interpretation:**
- Excess kurtosis ($\gamma_4 > 3$) → Positive curvature ($\sigma_2 > 0$) → U-shaped smile
- Leptokurtic (fat tails) → Convex smile

**Example (Student-t distribution):**  
Student-t with $\nu$ degrees of freedom has $\gamma_4 = 3 + \frac{6}{\nu - 4}$ for $\nu > 4$.

For $\nu = 5$: $\gamma_4 = 9$, giving:


$$
\sigma_2 \approx \frac{6}{24 \sigma_{\text{ATM}}} = \frac{0.25}{\sigma_{\text{ATM}}}
$$



Significant curvature even for moderately fat tails.

## Model-Specific ATM Expansions

### Black-Scholes Model

For constant volatility $\sigma$:


$$
\sigma_{\text{IV}}(y, T) = \sigma \quad \text{for all } y
$$



**Coefficients:**
- $\sigma_0 = \sigma$
- $\sigma_1 = \sigma_2 = \sigma_3 = \cdots = 0$ (flat smile)

### Local Volatility Model

For $dS_t = (r-q) S_t dt + \sigma_{\text{loc}}(S_t, t) S_t dW_t$:

**Small-time expansion:**


$$
\sigma_{\text{ATM}}(T) = \sigma_{\text{loc}}(F, 0) + O(T)
$$




$$
\sigma_1 = \frac{1}{F} \frac{\partial \sigma_{\text{loc}}}{\partial S}(F, 0) + O(T)
$$




$$
\sigma_2 = \frac{1}{F^2} \frac{\partial^2 \sigma_{\text{loc}}}{\partial S^2}(F, 0) + O(T)
$$



**Interpretation:** The smile parameters directly reflect the spatial derivatives of local volatility near the forward.

### Heston Model

For the Heston stochastic volatility model:


$$
\begin{align}
dS_t &= (r-q) S_t dt + \sqrt{v_t} S_t dW_t^S \\
dv_t &= \kappa(\theta - v_t) dt + \xi \sqrt{v_t} dW_t^v \\
\rho &= d\langle W^S, W^v \rangle_t / dt
\end{align}
$$



**ATM expansion (Hagan-Woodward):**


$$
\sigma_{\text{ATM}}^2 = v_0 + \frac{T}{2} \left[\kappa(\theta - v_0) - \frac{\xi^2}{4}\right] + O(T^2)
$$



**Skew:**


$$
\sigma_1 = \frac{\rho \xi}{4 \sqrt{v_0}} + O(T)
$$



**Curvature:**


$$
\sigma_2 = \frac{1}{24 v_0}\left[\xi^2 - 2\rho^2 \xi^2\right] + O(T)
$$



**Key insights:**
- ATM level determined by spot variance $v_0$
- Skew proportional to correlation $\rho$ and vol-of-vol $\xi$
- Curvature from vol-of-vol $\xi$ (always positive for Heston)

**Empirical calibration:**
- Fit $\sigma_{\text{ATM}} \to v_0$
- Fit skew $\sigma_1 \to \rho, \xi$
- Term structure constrains $\kappa, \theta$

### SABR Model

For SABR with $\beta$ fixed:


$$
\sigma_{\text{ATM}} \approx \alpha \left[1 + \left(\frac{(1-\beta)^2 \alpha^2}{24 F^{2-2\beta}} + \frac{\rho \beta \nu \alpha}{4 F^{1-\beta}} + \frac{2 - 3\rho^2}{24}\nu^2\right)T\right]
$$



**Skew (near ATM):**


$$
\frac{\partial \sigma}{\partial \ln K}\bigg|_{K=F} \approx \frac{\rho \nu \alpha}{F^{1-\beta}}
$$



**Parameters:**
- $\alpha$: ATM volatility level
- $\beta$: Backbone slope (determines mean-reversion of local vol)
- $\rho$: Correlation (controls skew)
- $\nu$: Vol-of-vol (controls curvature)

## Small-Moneyness Regime

### Scaling Limit

Consider strikes in the regime:


$$
K = F + x F \sigma_{\text{ATM}} \sqrt{T}
$$



where $x = O(1)$ as $T \to 0$ with $K$ scaling appropriately.

**Rescaled log-moneyness:**


$$
\tilde{y} = \frac{\ln(K/F)}{\sigma_{\text{ATM}} \sqrt{T}} \approx \frac{K - F}{F \sigma_{\text{ATM}} \sqrt{T}} = x
$$



**Expansion in this regime:**


$$
\sigma_{\text{IV}}(\tilde{y}, T) = \sigma_{\text{ATM}} \left[1 + \frac{\tilde{\sigma}_1}{\sqrt{T}} \tilde{y} + \frac{\tilde{\sigma}_2}{2T} \tilde{y}^2 + O(T^{-3/2})\right]
$$



**Result:** The smile is **parabolic** in the scaling variable $\tilde{y}$, with coefficients that blow up as $T \to 0$.

### Connection to Heat Kernel

For local volatility models, the transition density:


$$
p(S_T | S_0) \approx \frac{1}{\sigma(S_0, 0) S_0 \sqrt{2\pi T}} \exp\left(-\frac{(S_T - S_0)^2}{2\sigma^2(S_0, 0) S_0^2 T}\right)
$$



is approximately Gaussian (heat kernel) for small $T$.

**Implication:** Near ATM, the smile is determined by the local volatility at the spot, with parabolic shape:


$$
\sigma_{\text{IV}}^2(K, T) T \approx \sigma^2(S_0, 0) \left[1 + \frac{(K - S_0)^2}{2\sigma^2 S_0^2 T}\right]
$$



## Practical ATM Parametrizations

### Quadratic Approximation

For short-dated options (e.g., weekly), a quadratic fit suffices:


$$
\sigma(y) = \sigma_0 + \sigma_1 y + \frac{\sigma_2}{2} y^2
$$



**Calibration:**
- Use ATM and two wing points (e.g., 25-delta put/call)
- Solve linear system for $(\sigma_0, \sigma_1, \sigma_2)$

### Risk Reversal and Butterfly

Market quotes in terms of:
- **ATM:** $\sigma_{\text{ATM}}$
- **Risk Reversal (RR):** $\text{RR}_{25\Delta} = \sigma_{25\Delta \text{ call}} - \sigma_{25\Delta \text{ put}}$
- **Butterfly (BF):** $\text{BF}_{25\Delta} = \frac{\sigma_{25\Delta \text{ call}} + \sigma_{25\Delta \text{ put}}}{2} - \sigma_{\text{ATM}}$

**Relationship to coefficients:**

For small deviations from ATM ($y_{25\Delta} \approx \pm \Phi^{-1}(0.25) \sigma_0 \sqrt{T}$):


$$
\text{RR} \approx 2 \sigma_1 y_{25\Delta}
$$




$$
\text{BF} \approx \frac{\sigma_2}{2} y_{25\Delta}^2
$$



**Inversion:**


$$
\sigma_1 \approx \frac{\text{RR}}{2 y_{25\Delta}}
$$




$$
\sigma_2 \approx \frac{2 \text{BF}}{y_{25\Delta}^2}
$$



**Example:**
- ATM = 20%
- RR = $-2\%$ (downward skew)
- BF = $1\%$ (positive curvature)
- $T = 1/12$ (1 month)

Compute:


$$
y_{25\Delta} \approx \Phi^{-1}(0.75) \cdot 0.20 \cdot \sqrt{1/12} \approx 0.0387
$$




$$
\sigma_1 \approx \frac{-0.02}{2 \times 0.0387} \approx -0.26
$$




$$
\sigma_2 \approx \frac{2 \times 0.01}{0.0387^2} \approx 13.3
$$



Quadratic smile:


$$
\sigma(y) \approx 0.20 - 0.26 y + 6.65 y^2
$$



## ATM Greeks and Sensitivities

### Vega at ATM

ATM vega is:


$$
\mathcal{V}_{\text{ATM}} = S_0 e^{-qT} \phi(d_1) \sqrt{T}
$$



where $d_1 = \frac{(r-q)T + \sigma_{\text{ATM}}^2 T/2}{\sigma_{\text{ATM}} \sqrt{T}} \approx \frac{\sigma_{\text{ATM}} \sqrt{T}}{2}$ for small $(r-q)T$.

Thus:


$$
\phi(d_1) \approx \frac{1}{\sqrt{2\pi}} \exp\left(-\frac{\sigma_{\text{ATM}}^2 T}{8}\right) \approx \frac{1}{\sqrt{2\pi}}
$$



for small $T$.

**Approximation:**


$$
\mathcal{V}_{\text{ATM}} \approx \frac{S_0}{\sqrt{2\pi}} \sqrt{T}
$$



Vega grows as $\sqrt{T}$ for short maturities.

### Gamma at ATM

ATM gamma is:


$$
\Gamma_{\text{ATM}} = \frac{e^{-qT} \phi(d_1)}{S_0 \sigma_{\text{ATM}} \sqrt{T}}
$$



Using the approximation above:


$$
\Gamma_{\text{ATM}} \approx \frac{1}{S_0 \sigma_{\text{ATM}} \sqrt{2\pi T}}
$$



Gamma blows up as $T^{-1/2}$ near expiry.

### Volga (Vomma)

The sensitivity of vega to volatility:


$$
\text{Volga} = \frac{\partial \mathcal{V}}{\partial \sigma} = S_0 e^{-qT} \phi(d_1) \sqrt{T} \frac{d_1 d_2}{\sigma}
$$



At ATM with small $T$:


$$
d_1 d_2 \approx \frac{\sigma^2 T}{4} - \frac{\sigma^2 T}{4} = 0
$$



**Result:** Volga is approximately **zero** at ATM for short maturities.

**Implication:** ATM options have stable vega (insensitive to volatility changes), while wings have higher volga.

## Term Structure of ATM Smile

### ATM Volatility Evolution

Define the **ATM term structure**:


$$
\sigma_{\text{ATM}}(T)
$$



**Typical patterns:**
- Upward sloping: Low current volatility, expected to rise
- Downward sloping: High current volatility, expected to fall
- Humped: Event risk at intermediate maturity

### Skew Term Structure

The skew parameter $\sigma_1(T)$ also varies with maturity:

**Empirical observation (equity):**


$$
\sigma_1(T) \approx \sigma_1^\infty + (\sigma_1^0 - \sigma_1^\infty) e^{-\lambda T}
$$



- $\sigma_1^0$: Short-term skew (often steep)
- $\sigma_1^\infty$: Long-term skew (flatter)
- $\lambda$: Decay rate

**Interpretation:** Short-dated skew reflects immediate crash risk; long-dated skew is milder as uncertainty dominates.

### Curvature Term Structure

The curvature $\sigma_2(T)$ often **increases** with maturity:


$$
\sigma_2(T) \propto T^\alpha \quad \text{with } \alpha \approx 0.5
$$



**Reason:** Accumulation of uncertainty over longer horizons increases tail fatness.

## Asymptotic Matching

### Matching ATM and Wing Asymptotics

A complete smile model must consistently match:

1. **ATM expansion:** $\sigma(y) = \sigma_0 + \sigma_1 y + \frac{\sigma_2}{2} y^2 + \cdots$ for $|y| \ll 1$
2. **Wing asymptotics:** $\sigma^2(y) T \sim p_{\pm} |y|$ for $|y| \gg 1$

**Transition region:** Intermediate moneyness where both expansions fail—requires full model.

**Example (SVI):**

SVI smoothly interpolates:
- Near $y = m$: Quadratic behavior (ATM-like)
- Large $|y - m|$: Linear growth (wing-like)

Parameters $(a, b, \rho, m, \sigma)$ control the transition.

## Summary

ATM expansions provide:

### **Taylor expansion:**


$$
\sigma(y) = \sigma_0 + \sigma_1 y + \frac{\sigma_2}{2} y^2 + O(y^3)
$$



- $\sigma_0$: ATM volatility (level)
- $\sigma_1$: Skew (asymmetry)
- $\sigma_2$: Curvature (convexity)

### **Moment relationships:**


$$
\sigma_1 \sim -\frac{\text{Skewness}}{6\sigma_0}, \quad \sigma_2 \sim \frac{\text{Excess Kurtosis}}{24\sigma_0}
$$



### **Model-specific formulas:**

**Heston:**

$$
\sigma_0^2 = v_0, \quad \sigma_1 = \frac{\rho\xi}{4\sqrt{v_0}}
$$



**SABR:**

$$
\sigma_0 = \alpha, \quad \frac{\partial \sigma}{\partial \ln K} = \frac{\rho \nu \alpha}{F^{1-\beta}}
$$



### **Market quoting conventions:**


$$
\text{RR} \approx 2\sigma_1 y_\Delta, \quad \text{BF} \approx \frac{\sigma_2}{2} y_\Delta^2
$$



### **Greeks near ATM:**

- Vega: $\mathcal{V} \sim \sqrt{T}$
- Gamma: $\Gamma \sim T^{-1/2}$ (blows up)
- Volga: $\approx 0$ at ATM for small $T$

### **Practical workflow:**

1. Extract $(\sigma_0, \sigma_1, \sigma_2)$ from ATM, 25Δ put/call
2. Use for short-dated pricing and hedging
3. Match to full smile model (SVI, SSVI) for all strikes
4. Verify consistency with wing asymptotics

ATM expansions are fundamental for understanding the local structure of the volatility smile and serve as the primary calibration tool for parametric models.
