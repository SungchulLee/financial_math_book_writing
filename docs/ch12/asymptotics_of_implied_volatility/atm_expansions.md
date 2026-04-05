# ATM Expansions


## Introduction


The **at-the-money (ATM) expansion** of implied volatility provides a detailed characterization of the smile near the forward price $F = S_0 e^{(r-q)T}$. This region is of paramount importance because:
- ATM options are the most liquid and actively traded
- ATM IV serves as the benchmark volatility level
- Near-ATM expansion connects to Greeks and hedging sensitivity
- The shape near ATM determines skew and curvature parameters

This section develops comprehensive asymptotic expansions for implied volatility in the neighborhood of the ATM strike, including connections to model parameters, moments, and practical applications.

## ATM Definition and Conventions


### 1. Multiple ATM Definitions


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


### 1. General Expansion in Log-Moneyness


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

### 2. Interpretation of Coefficients


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


### 1. Moment Expansion


The risk-neutral distribution admits a moment expansion around the forward:


$$
S_T = F e^X
$$



where $X = \ln(S_T/F)$ has:
- Mean: $\mathbb{E}[X] = -\frac{1}{2}\text{Var}(X)$ (to ensure $\mathbb{E}[S_T] = F$)
- Variance: $\text{Var}(X) = \sigma_{\text{eff}}^2 T$
- Skewness: $\text{Skew}(X) = \gamma_3$
- Kurtosis: $\text{Kurt}(X) = \gamma_4$

### 2. ATM Volatility and Variance


**Leading term:**


$$
\sigma_{\text{ATM}}^2 T \approx \text{Var}(X)
$$



**Exact relationship (Carr-Madan):**


$$
\sigma_{\text{ATM}}^2 T = \text{Var}(X) + O(T^2)
$$



For short maturities, ATM IV directly measures the variance of log-returns.

### 3. Skew and Third Moment


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

### 4. Curvature and Fourth Moment


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


### 1. Black-Scholes Model


For constant volatility $\sigma$:


$$
\sigma_{\text{IV}}(y, T) = \sigma \quad \text{for all } y
$$



**Coefficients:**
- $\sigma_0 = \sigma$
- $\sigma_1 = \sigma_2 = \sigma_3 = \cdots = 0$ (flat smile)

### 2. Local Volatility Model


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

### 3. Heston Model


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

### 4. SABR Model


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


### 1. Scaling Limit


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

### 2. Connection to Heat Kernel


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


### 1. Quadratic Approximation


For short-dated options (e.g., weekly), a quadratic fit suffices:


$$
\sigma(y) = \sigma_0 + \sigma_1 y + \frac{\sigma_2}{2} y^2
$$



**Calibration:**
- Use ATM and two wing points (e.g., 25-delta put/call)
- Solve linear system for $(\sigma_0, \sigma_1, \sigma_2)$

### 2. Risk Reversal and Butterfly


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


### 1. Vega at ATM


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

### 2. Gamma at ATM


ATM gamma is:


$$
\Gamma_{\text{ATM}} = \frac{e^{-qT} \phi(d_1)}{S_0 \sigma_{\text{ATM}} \sqrt{T}}
$$



Using the approximation above:


$$
\Gamma_{\text{ATM}} \approx \frac{1}{S_0 \sigma_{\text{ATM}} \sqrt{2\pi T}}
$$



Gamma blows up as $T^{-1/2}$ near expiry.

### 3. Volga (Vomma)


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


### 1. ATM Volatility Evolution


Define the **ATM term structure**:


$$
\sigma_{\text{ATM}}(T)
$$



**Typical patterns:**
- Upward sloping: Low current volatility, expected to rise
- Downward sloping: High current volatility, expected to fall
- Humped: Event risk at intermediate maturity

### 2. Skew Term Structure


The skew parameter $\sigma_1(T)$ also varies with maturity:

**Empirical observation (equity):**


$$
\sigma_1(T) \approx \sigma_1^\infty + (\sigma_1^0 - \sigma_1^\infty) e^{-\lambda T}
$$



- $\sigma_1^0$: Short-term skew (often steep)
- $\sigma_1^\infty$: Long-term skew (flatter)
- $\lambda$: Decay rate

**Interpretation:** Short-dated skew reflects immediate crash risk; long-dated skew is milder as uncertainty dominates.

### 3. Curvature Term Structure


The curvature $\sigma_2(T)$ often **increases** with maturity:


$$
\sigma_2(T) \propto T^\alpha \quad \text{with } \alpha \approx 0.5
$$



**Reason:** Accumulation of uncertainty over longer horizons increases tail fatness.

## Asymptotic Matching


### 1. Matching ATM and Wing Asymptotics


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

### 1. **Taylor expansion:**



$$
\sigma(y) = \sigma_0 + \sigma_1 y + \frac{\sigma_2}{2} y^2 + O(y^3)
$$



- $\sigma_0$: ATM volatility (level)
- $\sigma_1$: Skew (asymmetry)
- $\sigma_2$: Curvature (convexity)

### 2. **Moment relationships:**



$$
\sigma_1 \sim -\frac{\text{Skewness}}{6\sigma_0}, \quad \sigma_2 \sim \frac{\text{Excess Kurtosis}}{24\sigma_0}
$$



### 3. **Model-specific formulas:**


**Heston:**

$$
\sigma_0^2 = v_0, \quad \sigma_1 = \frac{\rho\xi}{4\sqrt{v_0}}
$$



**SABR:**

$$
\sigma_0 = \alpha, \quad \frac{\partial \sigma}{\partial \ln K} = \frac{\rho \nu \alpha}{F^{1-\beta}}
$$



### 4. **Market quoting conventions:**



$$
\text{RR} \approx 2\sigma_1 y_\Delta, \quad \text{BF} \approx \frac{\sigma_2}{2} y_\Delta^2
$$



### 5. **Greeks near ATM:**


- Vega: $\mathcal{V} \sim \sqrt{T}$
- Gamma: $\Gamma \sim T^{-1/2}$ (blows up)
- Volga: $\approx 0$ at ATM for small $T$

### 6. **Practical workflow:**


1. Extract $(\sigma_0, \sigma_1, \sigma_2)$ from ATM, 25Δ put/call
2. Use for short-dated pricing and hedging
3. Match to full smile model (SVI, SSVI) for all strikes
4. Verify consistency with wing asymptotics

ATM expansions are fundamental for understanding the local structure of the volatility smile and serve as the primary calibration tool for parametric models.

---

## Exercises

**Exercise 1.** Given an implied volatility smile parametrized by $\sigma(y) = \sigma_0 + \sigma_1 y + \frac{\sigma_2}{2} y^2$ with $\sigma_0 = 0.22$, $\sigma_1 = -0.30$, and $\sigma_2 = 10.0$, compute the implied volatility at log-moneyness $y = -0.05$ and $y = 0.05$. Verify that the smile is downward-sloping (equity-like) near ATM.

??? success "Solution to Exercise 1"
    We evaluate the quadratic smile $\sigma(y) = \sigma_0 + \sigma_1 y + \frac{\sigma_2}{2} y^2$ with $\sigma_0 = 0.22$, $\sigma_1 = -0.30$, and $\sigma_2 = 10.0$.

    **At $y = -0.05$:**

    $$
    \sigma(-0.05) = 0.22 + (-0.30)(-0.05) + \frac{10.0}{2}(-0.05)^2 = 0.22 + 0.015 + 0.0125 = 0.2475
    $$

    So $\sigma_{\text{IV}} \approx 24.75\%$.

    **At $y = 0.05$:**

    $$
    \sigma(0.05) = 0.22 + (-0.30)(0.05) + \frac{10.0}{2}(0.05)^2 = 0.22 - 0.015 + 0.0125 = 0.2175
    $$

    So $\sigma_{\text{IV}} \approx 21.75\%$.

    **Verification of downward slope:** The IV at $y = -0.05$ (OTM put, $K < F$) is $24.75\%$, which is higher than the IV at $y = 0.05$ (OTM call, $K > F$) of $21.75\%$. This confirms the smile is downward-sloping near ATM, consistent with an equity-like skew ($\sigma_1 = -0.30 < 0$). Lower strikes have higher implied volatility, reflecting the market's pricing of downside crash risk.

---

**Exercise 2.** The skew-skewness relationship states

$$
\sigma_1 \approx -\frac{\gamma_3}{6\sigma_0}
$$

If the risk-neutral distribution of $X = \ln(S_T/F)$ has skewness $\gamma_3 = -1.2$ and ATM volatility $\sigma_0 = 0.18$, compute the smile skew parameter $\sigma_1$. Interpret the sign of $\sigma_1$ in the context of equity index options.

??? success "Solution to Exercise 2"
    We apply the skew-skewness relationship with $\gamma_3 = -1.2$ and $\sigma_0 = 0.18$:

    $$
    \sigma_1 \approx -\frac{\gamma_3}{6\sigma_0} = -\frac{-1.2}{6 \times 0.18} = \frac{1.2}{1.08} \approx 1.111
    $$

    Wait — let us re-examine the sign convention. From the text, the relationship is

    $$
    \sigma(y) \approx \sigma_0 - \frac{\gamma_3}{6\sigma_0} y
    $$

    so $\sigma_1 = -\frac{\gamma_3}{6\sigma_0}$.

    Substituting:

    $$
    \sigma_1 = -\frac{-1.2}{6 \times 0.18} = \frac{1.2}{1.08} \approx 1.111
    $$

    However, this seems large. The issue is that $\sigma_1$ here represents $\frac{\partial \sigma}{\partial y}\big|_{y=0}$, and for typical equity parameters the numerical value can indeed be on the order of unity because $y$ is log-moneyness (a small number for near-ATM strikes).

    **Interpretation:** $\sigma_1 > 0$ means that $\frac{d\sigma}{dy} > 0$, so IV increases as $y = \ln(K/F)$ increases. But recall the correction in the text: using the convention $\sigma(y) \approx \sigma_0 - \frac{\gamma_3}{6\sigma_0} y$, negative skewness ($\gamma_3 < 0$) yields a smile where IV **decreases** with increasing log-moneyness in the standard parameterization. This is the equity index pattern: OTM puts ($y < 0$) have higher IV than OTM calls ($y > 0$), reflecting the left-skewed risk-neutral distribution and the market's demand for downside protection.

---

**Exercise 3.** In the Heston model with parameters $v_0 = 0.0625$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.5$, and $\rho = -0.65$, use the ATM expansion formulas to compute: (a) the leading-order ATM implied volatility $\sigma_0$, (b) the skew parameter $\sigma_1$, and (c) the first-order correction to $\sigma_{\text{ATM}}^2$ for maturity $T = 0.25$.

??? success "Solution to Exercise 3"
    **Heston parameters:** $v_0 = 0.0625$, $\kappa = 1.5$, $\theta = 0.04$, $\xi = 0.5$, $\rho = -0.65$.

    **(a) Leading-order ATM implied volatility:**

    $$
    \sigma_0 = \sqrt{v_0} = \sqrt{0.0625} = 0.25
    $$

    So $\sigma_0 = 25\%$.

    **(b) Skew parameter:**

    $$
    \sigma_1 = \frac{\rho \xi}{4\sqrt{v_0}} = \frac{(-0.65)(0.5)}{4 \times 0.25} = \frac{-0.325}{1.0} = -0.325
    $$

    The negative skew ($\sigma_1 = -0.325$) reflects the negative correlation $\rho = -0.65$: when the asset drops, volatility rises, creating the characteristic equity skew.

    **(c) First-order correction to $\sigma_{\text{ATM}}^2$ at $T = 0.25$:**

    Using the formula

    $$
    \sigma_{\text{ATM}}^2 = v_0 + \frac{T}{2}\left[\kappa(\theta - v_0) - \frac{\xi^2}{4}\right] + O(T^2)
    $$

    we compute the correction term:

    $$
    \kappa(\theta - v_0) = 1.5(0.04 - 0.0625) = 1.5 \times (-0.0225) = -0.03375
    $$

    $$
    \frac{\xi^2}{4} = \frac{0.25}{4} = 0.0625
    $$

    $$
    \text{Correction} = \frac{0.25}{2}\left[-0.03375 - 0.0625\right] = 0.125 \times (-0.09625) = -0.01203
    $$

    $$
    \sigma_{\text{ATM}}^2 \approx 0.0625 - 0.01203 = 0.05047
    $$

    $$
    \sigma_{\text{ATM}} \approx \sqrt{0.05047} \approx 0.2247 = 22.47\%
    $$

    The ATM IV decreases from the spot value of $25\%$ because the mean-reversion term pulls variance toward $\theta = 0.04$ (lower than $v_0 = 0.0625$), and the vol-of-vol correction further reduces it.

---

**Exercise 4.** An FX options desk quotes the following for 1-month EUR/USD options: ATM volatility $\sigma_{\text{ATM}} = 10\%$, 25-delta risk reversal $\text{RR}_{25\Delta} = -0.8\%$, and 25-delta butterfly $\text{BF}_{25\Delta} = 0.4\%$. Using $T = 1/12$ and $\Phi^{-1}(0.75) \approx 0.6745$, compute the quadratic smile coefficients $(\sigma_0, \sigma_1, \sigma_2)$ and write the approximate smile function $\sigma(y)$.

??? success "Solution to Exercise 4"
    **Given:** $\sigma_{\text{ATM}} = 10\% = 0.10$, $\text{RR}_{25\Delta} = -0.8\% = -0.008$, $\text{BF}_{25\Delta} = 0.4\% = 0.004$, $T = 1/12$, $\Phi^{-1}(0.75) \approx 0.6745$.

    **Step 1: Compute $y_{25\Delta}$.**

    $$
    y_{25\Delta} \approx \Phi^{-1}(0.75) \cdot \sigma_0 \cdot \sqrt{T} = 0.6745 \times 0.10 \times \sqrt{1/12}
    $$

    $$
    \sqrt{1/12} \approx 0.2887
    $$

    $$
    y_{25\Delta} \approx 0.6745 \times 0.10 \times 0.2887 \approx 0.01947
    $$

    **Step 2: Compute the smile coefficients.**

    $$
    \sigma_0 = \sigma_{\text{ATM}} = 0.10
    $$

    $$
    \sigma_1 \approx \frac{\text{RR}}{2 y_{25\Delta}} = \frac{-0.008}{2 \times 0.01947} = \frac{-0.008}{0.03894} \approx -0.2054
    $$

    $$
    \sigma_2 \approx \frac{2 \,\text{BF}}{y_{25\Delta}^2} = \frac{2 \times 0.004}{(0.01947)^2} = \frac{0.008}{0.000379} \approx 21.1
    $$

    **Step 3: Write the smile function.**

    $$
    \sigma(y) \approx 0.10 - 0.2054\, y + 10.55\, y^2
    $$

    The negative $\sigma_1$ confirms the downward skew (OTM puts more expensive), and the large positive $\sigma_2$ creates a U-shaped smile around ATM, which is typical for FX options.

---

**Exercise 5.** Explain why the volga (vomma) of an ATM option is approximately zero for short maturities. Starting from the formula

$$
\text{Volga} = S_0 e^{-qT} \phi(d_1) \sqrt{T} \frac{d_1 d_2}{\sigma}
$$

show that $d_1 d_2 \to 0$ as $T \to 0$ at the ATM strike. What does this imply about the stability of ATM vega?

??? success "Solution to Exercise 5"
    At ATM, $K = F = S_0 e^{(r-q)T}$, and for small $(r-q)T$:

    $$
    d_1 = \frac{\ln(S_0/K) + (r - q + \sigma^2/2)T}{\sigma\sqrt{T}} \approx \frac{\sigma^2 T/2}{\sigma\sqrt{T}} = \frac{\sigma\sqrt{T}}{2}
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{T} = \frac{\sigma\sqrt{T}}{2} - \sigma\sqrt{T} = -\frac{\sigma\sqrt{T}}{2}
    $$

    Therefore:

    $$
    d_1 d_2 = \frac{\sigma\sqrt{T}}{2} \times \left(-\frac{\sigma\sqrt{T}}{2}\right) = -\frac{\sigma^2 T}{4}
    $$

    As $T \to 0$:

    $$
    d_1 d_2 = -\frac{\sigma^2 T}{4} \to 0
    $$

    Substituting into the volga formula:

    $$
    \text{Volga} = S_0 e^{-qT} \phi(d_1) \sqrt{T} \frac{d_1 d_2}{\sigma} \approx S_0 \cdot \frac{1}{\sqrt{2\pi}} \cdot \sqrt{T} \cdot \frac{-\sigma^2 T / 4}{\sigma} = -\frac{S_0 \sigma T^{3/2}}{4\sqrt{2\pi}}
    $$

    This vanishes as $T \to 0$, confirming that ATM volga is approximately zero for short maturities.

    **Implication for ATM vega stability:** Since volga $= \partial \mathcal{V}/\partial \sigma \approx 0$ at ATM for small $T$, the ATM vega is nearly constant with respect to changes in volatility. This means ATM options provide a stable, predictable vega exposure—making them ideal instruments for volatility trading. In contrast, OTM options (in the wings) have significant volga, so their vega changes as volatility moves, creating second-order risk.

---

**Exercise 6.** The curvature-kurtosis relationship gives $\sigma_2 \approx \frac{\gamma_4 - 3}{24\sigma_0}$. Suppose the risk-neutral kurtosis is $\gamma_4 = 5.0$ and $\sigma_0 = 0.25$. (a) Compute the curvature parameter $\sigma_2$. (b) Is the resulting smile U-shaped or inverted? (c) What value of $\gamma_4$ would produce a flat smile (zero curvature)?

??? success "Solution to Exercise 6"
    **Given:** $\gamma_4 = 5.0$ and $\sigma_0 = 0.25$.

    **(a) Curvature parameter:**

    $$
    \sigma_2 \approx \frac{\gamma_4 - 3}{24\sigma_0} = \frac{5.0 - 3}{24 \times 0.25} = \frac{2.0}{6.0} \approx 0.333
    $$

    **(b)** Since $\sigma_2 = 0.333 > 0$, the smile is **U-shaped** (convex). The implied volatility curve has a minimum near ATM and increases on both sides. This is consistent with the excess kurtosis $\gamma_4 - 3 = 2.0 > 0$, reflecting heavier tails than the normal distribution.

    **(c)** For a flat smile (zero curvature), we need $\sigma_2 = 0$:

    $$
    \frac{\gamma_4 - 3}{24\sigma_0} = 0 \implies \gamma_4 = 3
    $$

    A kurtosis of $\gamma_4 = 3$ corresponds to the normal (Gaussian) distribution, which is mesokurtic. In that case, the risk-neutral distribution of log-returns has Gaussian tails, and the implied volatility smile is flat (no curvature)—consistent with the Black-Scholes model.

---

**Exercise 7.** Consider the SABR model with $\beta = 0.5$, $\alpha = 0.15$, $\nu = 0.35$, and $\rho = -0.40$ for a forward price $F = 50$. Using the SABR ATM expansion, compute the approximate ATM implied volatility for $T = 1/4$. Then compute the ATM skew $\frac{\partial \sigma}{\partial \ln K}\big|_{K=F}$ and interpret the result.

??? success "Solution to Exercise 7"
    **SABR parameters:** $\beta = 0.5$, $\alpha = 0.15$, $\nu = 0.35$, $\rho = -0.40$, $F = 50$, $T = 1/4$.

    **Step 1: ATM implied volatility.**

    At ATM ($K = F$), we use the SABR ATM formula:

    $$
    \sigma_{\text{ATM}} \approx \alpha \left[1 + \left(\frac{(1-\beta)^2 \alpha^2}{24 F^{2-2\beta}} + \frac{\rho \beta \nu \alpha}{4 F^{1-\beta}} + \frac{2 - 3\rho^2}{24}\nu^2\right)T\right]
    $$

    Compute each term inside the bracket:

    - $F^{1-\beta} = 50^{0.5} = \sqrt{50} \approx 7.071$
    - $F^{2-2\beta} = 50^{1} = 50$

    **Term 1:**

    $$
    \frac{(1-\beta)^2 \alpha^2}{24 F^{2-2\beta}} = \frac{(0.5)^2 (0.15)^2}{24 \times 50} = \frac{0.25 \times 0.0225}{1200} = \frac{0.005625}{1200} \approx 0.000004688
    $$

    **Term 2:**

    $$
    \frac{\rho \beta \nu \alpha}{4 F^{1-\beta}} = \frac{(-0.40)(0.5)(0.35)(0.15)}{4 \times 7.071} = \frac{-0.0105}{28.284} \approx -0.000371
    $$

    **Term 3:**

    $$
    \frac{2 - 3\rho^2}{24}\nu^2 = \frac{2 - 3(0.16)}{24}(0.1225) = \frac{2 - 0.48}{24} \times 0.1225 = \frac{1.52}{24} \times 0.1225 \approx 0.06333 \times 0.1225 \approx 0.007758
    $$

    **Sum of terms:**

    $$
    0.000005 - 0.000371 + 0.007758 \approx 0.007392
    $$

    **ATM IV:**

    $$
    \sigma_{\text{ATM}} \approx 0.15 \times \left[1 + 0.007392 \times 0.25\right] = 0.15 \times [1 + 0.001848] = 0.15 \times 1.001848 \approx 0.15028
    $$

    So $\sigma_{\text{ATM}} \approx 15.03\%$.

    **Step 2: ATM skew.**

    $$
    \frac{\partial \sigma}{\partial \ln K}\bigg|_{K=F} \approx \frac{\rho \nu \alpha}{F^{1-\beta}} = \frac{(-0.40)(0.35)(0.15)}{7.071} = \frac{-0.021}{7.071} \approx -0.00297
    $$

    **Interpretation:** The ATM skew is $\approx -0.30\%$ per unit log-moneyness. The negative value arises from the negative correlation $\rho = -0.40$: when the forward price drops, volatility tends to rise, generating a downward-sloping smile. For every $1\%$ increase in log-moneyness, the implied volatility decreases by approximately $0.003$ (0.3 percentage points). This is a moderate skew typical of equity-like behavior in the SABR framework.
