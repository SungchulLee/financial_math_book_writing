# Instantaneous Correlation and Leverage Effect

The correlation parameter $\rho$ between the asset price and variance Brownian motions is one of the most important features of the Heston model. When $\rho < 0$ -- the empirically dominant case for equity markets -- a drop in the stock price tends to coincide with an increase in variance, and vice versa. This phenomenon, known as the **leverage effect**, is the primary mechanism by which the Heston model generates the negative implied volatility skew observed in equity options. Understanding $\rho$ is essential for interpreting the shape of the implied volatility surface, for hedging volatility exposure, and for calibrating the model to market data.

This section defines the leverage effect, derives its mathematical consequences for the joint dynamics of returns and variance, shows how $\rho$ shapes the implied volatility smile, and connects the model to empirical observations. We build on the Heston SDE and Cholesky decomposition from the [model definition section](../model_definition/heston_sde_and_parameters.md) and the moment formulas from the [variance moments section](variance_process_moments.md).

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Define the leverage effect and explain its financial origin
    - Derive the covariance between log-returns and variance changes in the Heston model
    - Explain how $\rho < 0$ generates negative implied volatility skew
    - Describe the effect of $\rho$ on the skewness of the log-return distribution
    - Distinguish the roles of $\rho$ (skew) and $\sigma_v$ (curvature) in shaping the smile

---

## The Leverage Effect

### Intuition

The term "leverage effect" has its origin in corporate finance: when a firm's equity value drops, its debt-to-equity ratio (financial leverage) increases, making the equity riskier and hence more volatile. While the corporate finance explanation is debated, the statistical phenomenon is robust: negative equity returns are strongly correlated with increases in realized volatility. The VIX index, which measures the implied volatility of S&P 500 options, typically spikes during market selloffs and declines during rallies.

In the Heston model, this effect is captured by the correlation $\rho < 0$ between the Brownian motions driving the stock price and the variance process. When $dW_t^{(1)}$ is negative (stock drops), the correlation makes it likely that $dW_t^{(2)}$ is also negative in a suitable direction, pushing variance upward.

### Mathematical Formulation

!!! info "Definition: Leverage Effect in the Heston Model"
    The **leverage effect** is the negative instantaneous correlation between asset returns and variance changes:

    $$
    \text{Corr}\!\left(\frac{dS_t}{S_t},\; dv_t\right) = \rho < 0
    $$

    More precisely, using the Heston SDEs and the Cholesky decomposition $W_t^{(2)} = \rho W_t^{(1)} + \sqrt{1-\rho^2}\,Z_t^{(2)}$:

    $$
    d\langle \ln S, v \rangle_t = \rho\,\sigma_v\,v_t\,dt
    $$

**Proof.** The instantaneous quadratic covariation between $x_t = \ln S_t$ and $v_t$ is:

$$
d\langle x, v \rangle_t = \left(\sqrt{v_t}\right)\left(\sigma_v\sqrt{v_t}\right)\,d\langle W^{(1)}, W^{(2)} \rangle_t = \sigma_v\,v_t\,\rho\,dt
$$

Since $d\langle x \rangle_t = v_t\,dt$ and $d\langle v \rangle_t = \sigma_v^2\,v_t\,dt$, the instantaneous correlation is:

$$
\frac{d\langle x, v \rangle_t}{\sqrt{d\langle x \rangle_t \cdot d\langle v \rangle_t}} = \frac{\sigma_v\,v_t\,\rho\,dt}{\sqrt{v_t\,dt \cdot \sigma_v^2\,v_t\,dt}} = \frac{\sigma_v\,v_t\,\rho}{\sigma_v\,v_t} = \rho
$$

$\square$

---

## Effect on the Return Distribution

### Skewness Generation

The leverage effect ($\rho < 0$) generates negative skewness in the log-return distribution. The mechanism is as follows:

1. A negative stock return ($dW_t^{(1)} < 0$) tends to increase variance ($dv_t > 0$ because $\rho < 0$)
2. Higher variance increases the magnitude of subsequent returns (in both directions)
3. This creates an asymmetry: large negative returns are followed by high volatility, amplifying further negative returns; large positive returns are followed by declining volatility, damping further positive returns

The net effect is that the left tail of the return distribution is heavier than the right tail, producing negative skewness.

### Quantitative Skewness Formula

!!! success "Proposition: Short-Maturity Skewness Approximation"
    For small $\tau$, the skewness of $x_T = \ln S_T$ conditional on $(x_t, v_t)$ is approximately:

    $$
    \text{Skew}(x_T | v_t) \approx \frac{\rho\,\sigma_v}{\sqrt{v_t}}\,\sqrt{\tau}
    $$

    For $\rho < 0$, this gives negative skewness that grows (in magnitude) with $\sigma_v$ and $\sqrt{\tau}$, and decreases with $\sqrt{v_t}$.

This approximation shows that the skewness is proportional to $\rho\sigma_v$, the product of correlation and vol-of-vol. This product is the key quantity controlling the slope of the implied volatility skew.

---

## Effect on the Implied Volatility Surface

### Skew vs. Curvature

The two parameters $\rho$ and $\sigma_v$ control different aspects of the implied volatility smile:

| Parameter | Effect on Smile | Mathematical Mechanism |
|:---|:---|:---|
| $\rho$ | **Skew** (tilt/slope) | Asymmetry in return distribution |
| $\sigma_v$ | **Curvature** (convexity/wings) | Fat tails in return distribution |

!!! tip "Decomposition of the Smile"
    At a qualitative level:

    - **$\rho = 0$, $\sigma_v > 0$**: symmetric smile (both wings elevated equally, like a "U")
    - **$\rho < 0$, $\sigma_v > 0$**: negatively skewed smile (left wing higher than right, like a smirk)
    - **$\rho = 0$, $\sigma_v = 0$**: flat smile (Black-Scholes)
    - **$\rho < 0$, $\sigma_v = 0$**: impossible ($\sigma_v = 0$ means deterministic volatility, so $\rho$ is irrelevant)

### The Skew Approximation

For short maturities, the implied volatility skew (slope with respect to log-moneyness $k = \ln(K/F)$ where $F$ is the forward price) is approximately:

$$
\frac{\partial \sigma_{\text{imp}}}{\partial k}\bigg|_{k=0} \approx \frac{\rho\,\sigma_v}{2\sqrt{v_0}}
$$

This formula shows that:

- The ATM skew is proportional to $\rho\sigma_v$ (negative for equity indices)
- The skew is inversely proportional to $\sqrt{v_0}$ (the skew is steeper when volatility is low)
- The skew does not depend on $\kappa$ or $\theta$ to first order (these affect the term structure of the skew)

!!! warning "Short-Maturity Limitation"
    The approximation above is valid for short maturities only. For longer maturities, the mean reversion of variance dampens the skew, and the dependence on $\kappa$ and $\theta$ becomes significant. The full implied volatility surface requires numerical evaluation of the Heston characteristic function.

---

## The Three Roles of Correlation

The parameter $\rho$ plays three distinct roles in the Heston model:

### 1. Smile Skew

As discussed above, $\rho$ controls the slope of the implied volatility smile. Typical calibrated values for equity indices are $\rho \in [-0.9, -0.5]$.

### 2. Spot-Vol Dynamics

The correlation $\rho$ determines how the spot price and implied volatility move together in real time. With $\rho < 0$:

- When $S$ drops, $v$ increases, so implied volatilities rise
- When $S$ rises, $v$ decreases, so implied volatilities fall
- This creates the empirical observation that implied volatility and spot price are negatively correlated

### 3. Hedging

The correlation affects the delta and vega of options. In the Heston model, the delta of an option is:

$$
\Delta_{\text{Heston}} = \Delta_{\text{BS}} + \frac{\partial V}{\partial v}\cdot\frac{\partial v}{\partial S}
$$

where the $\partial v / \partial S$ term depends on $\rho$. With $\rho < 0$, a stock price drop increases variance, which increases option values (for both calls and puts). This makes Heston deltas for puts more negative (and for calls, less positive) than Black-Scholes deltas.

---

## Empirical Calibration of Correlation

??? example "Typical Calibrated Correlation Values"
    | Asset Class | Typical $\rho$ | Explanation |
    |:---|:---:|:---|
    | Equity indices (SPX, EUROSTOXX) | $-0.60$ to $-0.85$ | Strong leverage effect; crashes increase volatility |
    | Single stocks | $-0.40$ to $-0.70$ | Moderate leverage effect; idiosyncratic noise dilutes it |
    | FX (EURUSD, USDJPY) | $-0.20$ to $+0.20$ | Weak or no systematic leverage; symmetric smile |
    | Commodities (Gold, Oil) | $-0.30$ to $+0.30$ | Depends on supply/demand dynamics |
    | Interest rates | $-0.30$ to $+0.30$ | Varies with the rate environment |

    The strong negative correlation for equity indices is the most robust empirical finding and the primary reason the Heston model (with $\rho < 0$) is the standard stochastic volatility model for equity derivatives.

---

## Worked Example: Effect of Correlation on Log-Returns

??? example "Simulating the Leverage Effect"
    Consider two Heston models with identical parameters except for $\rho$:

    - **Model A**: $\rho = -0.7$ (strong leverage)
    - **Model B**: $\rho = 0$ (no leverage)

    Common parameters: $v_0 = 0.04$, $\kappa = 2$, $\theta = 0.04$, $\sigma_v = 0.5$, $r = 0.03$, $q = 0$, $T = 1$.

    | Statistic | Model A ($\rho = -0.7$) | Model B ($\rho = 0$) |
    |:---|:---:|:---:|
    | $\mathbb{E}[\ln(S_T/S_0)]$ | $0.01$ | $0.01$ |
    | $\text{Std}(\ln(S_T/S_0))$ | $0.214$ | $0.213$ |
    | Skewness | $-0.62$ | $\approx 0$ |
    | Excess kurtosis | $1.8$ | $1.2$ |
    | 25-delta put IV - ATM IV | $+4.2$ vol pts | $\approx 0$ |
    | 25-delta call IV - ATM IV | $-1.8$ vol pts | $\approx 0$ |

    The mean and standard deviation are nearly identical (variance is driven by $v_0$, $\kappa$, $\theta$, and $\sigma_v$, not by $\rho$). The skewness and the implied volatility skew, however, are dramatically different. The negative $\rho$ in Model A generates a 6 vol-point differential between OTM puts and OTM calls, which is the hallmark of the equity volatility skew.

---

## Correlation and the Forward Smile

The parameter $\rho$ also affects how the implied volatility smile evolves with maturity.

For short maturities, the skew is steep (proportional to $1/\sqrt{T}$ in the moneyness dimension). For longer maturities, mean reversion dampens variance excursions, reducing the skew. The rate of this dampening depends on the interplay between $\rho$, $\sigma_v$, and $\kappa$:

- **Large $|\rho|$ with small $\kappa$**: persistent skew across maturities (variance shocks are long-lived)
- **Large $|\rho|$ with large $\kappa$**: steep short-maturity skew that flattens quickly
- **Small $|\rho|$**: weak skew at all maturities

This maturity-dependent behavior is one reason the full Heston characteristic function (not just the short-maturity approximation) is needed for calibration across the term structure.

---

## Summary

The correlation parameter $\rho$ in the Heston model generates the leverage effect: negative $\rho$ causes stock price drops to coincide with variance increases, producing negative skewness in the return distribution and a downward-sloping implied volatility skew. The product $\rho\sigma_v$ is the primary determinant of the ATM skew slope, while $\sigma_v$ alone controls the smile curvature. Typical calibrated values for equity indices are $\rho \in [-0.9, -0.5]$, reflecting the strong empirical correlation between negative returns and volatility spikes. The correlation also affects delta hedging (through the spot-vol covariance) and the term structure of the skew (through interaction with mean reversion).

The characteristic function derivation in the [next section](../heston_cf/heston_sde_and_affine_recap.md) incorporates $\rho$ through the mixed partial derivative term in the Feynman-Kac PDE, completing the mathematical picture.

---
