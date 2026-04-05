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

## Exercises

**Exercise 1.** Compute the instantaneous covariance $\operatorname{Cov}(d\log S_t, dV_t) = \rho\sigma_v V_t\,dt$ for $\rho = -0.75$, $\sigma_v = 0.4$, $V_t = 0.04$. Interpret the sign and magnitude.

??? success "Solution to Exercise 1"
    We compute the instantaneous covariance:

    $$
    \operatorname{Cov}(d\log S_t,\, dV_t) = \rho\,\sigma_v\,V_t\,dt
    $$

    Substituting $\rho = -0.75$, $\sigma_v = 0.4$, and $V_t = 0.04$:

    $$
    \operatorname{Cov}(d\log S_t,\, dV_t) = (-0.75)(0.4)(0.04)\,dt = -0.012\,dt
    $$

    **Interpretation of the sign:** The covariance is negative, reflecting the leverage effect. When the log-return $d\log S_t$ is negative (stock price drops), the variance change $dV_t$ tends to be positive (variance increases), and vice versa. This is the fundamental mechanism generating the implied volatility skew in equity markets.

    **Interpretation of the magnitude:** The covariance magnitude is $0.012\,dt$. To assess its strength, consider the instantaneous correlation. We have $d\langle \log S \rangle_t = V_t\,dt = 0.04\,dt$ and $d\langle V \rangle_t = \sigma_v^2 V_t\,dt = 0.16 \times 0.04\,dt = 0.0064\,dt$. The instantaneous correlation is:

    $$
    \frac{-0.012\,dt}{\sqrt{0.04\,dt \times 0.0064\,dt}} = \frac{-0.012}{\sqrt{0.000256}} = \frac{-0.012}{0.016} = -0.75 = \rho
    $$

    This confirms the derivation and shows that $\rho$ is the instantaneous correlation between log-returns and variance changes, independent of the current variance level.

---

**Exercise 2.** The skewness of log-returns over a short period $\Delta t$ is approximately proportional to $\rho\sigma_v\sqrt{V_t}\Delta t$. Explain why $\rho < 0$ produces negative skewness and relate this to the shape of the implied volatility smile.

??? success "Solution to Exercise 2"
    Over a short interval $\Delta t$, the log-return and variance change are approximately:

    $$
    \Delta \log S_t \approx \sqrt{V_t}\,\Delta W_t^{(1)}, \qquad \Delta V_t \approx \sigma_v\sqrt{V_t}\,\Delta W_t^{(2)}
    $$

    where $\operatorname{Corr}(\Delta W_t^{(1)}, \Delta W_t^{(2)}) = \rho$.

    When $\rho < 0$, a negative realization of $\Delta W_t^{(1)}$ (stock drops) is correlated with a positive realization of $\Delta V_t$ (variance rises). This creates an asymmetry in the return distribution:

    - **Left tail amplification:** A large negative return increases variance, which in turn increases the probability of further large (negative or positive) returns. But since returns are currently trending negatively (the shock that caused the variance increase was negative), the net effect is a heavier left tail.
    - **Right tail dampening:** A large positive return decreases variance, which reduces the probability of further large returns, thinning the right tail.

    The skewness is approximately:

    $$
    \text{Skew}(\Delta \log S) \approx \rho\,\sigma_v\,\sqrt{V_t}\,\Delta t
    $$

    For $\rho < 0$, this is negative, confirming negative skewness.

    **Relation to the implied volatility smile:** Negative skewness in the physical return distribution translates to a negatively sloped implied volatility smile under the risk-neutral measure. OTM puts (low strikes) are priced higher than the Black-Scholes model would predict because the left tail is heavier than a lognormal distribution. OTM calls (high strikes) are priced lower because the right tail is thinner. The result is the characteristic "smirk" shape observed in equity index options, where implied volatility decreases as the strike price increases.

---

**Exercise 3.** For the ATM implied volatility skew, the leading-order approximation is $\frac{\partial\sigma_{\text{imp}}}{\partial k}\big|_{k=0} \approx \frac{\rho\sigma_v}{2\sqrt{V_0}}$ where $k = \log(K/F)$. Compute this for $\rho = -0.7$, $\sigma_v = 0.3$, $V_0 = 0.04$. Is the skew negative as expected?

??? success "Solution to Exercise 3"
    The ATM implied volatility skew is:

    $$
    \frac{\partial\sigma_{\text{imp}}}{\partial k}\bigg|_{k=0} \approx \frac{\rho\,\sigma_v}{2\sqrt{V_0}}
    $$

    Substituting $\rho = -0.7$, $\sigma_v = 0.3$, $V_0 = 0.04$ (so $\sqrt{V_0} = 0.2$):

    $$
    \frac{\partial\sigma_{\text{imp}}}{\partial k}\bigg|_{k=0} \approx \frac{(-0.7)(0.3)}{2 \times 0.2} = \frac{-0.21}{0.4} = -0.525
    $$

    **Interpretation:** The skew is $-0.525$, meaning that for each unit increase in log-moneyness $k = \ln(K/F)$, the implied volatility decreases by approximately 52.5 percentage points (in volatility units). In more practical terms, for a 10% change in log-moneyness ($\Delta k = 0.10$), the implied volatility changes by approximately $-0.525 \times 0.10 = -0.0525$, or about $-5.25$ volatility points.

    Yes, the skew is negative as expected, since $\rho < 0$. This means OTM puts (negative $k$) have higher implied volatility than ATM options, and OTM calls (positive $k$) have lower implied volatility, consistent with the equity volatility smirk.

---

**Exercise 4.** If $\rho = 0$, the Heston model produces a symmetric implied volatility smile (no skew). Sketch the smile shape for $\rho = 0$, $\rho = -0.5$, and $\rho = -0.9$, labeling the ATM level and the skew.

??? success "Solution to Exercise 4"
    The three cases produce qualitatively different smile shapes:

    **Case 1: $\rho = 0$ (no leverage).** The implied volatility smile is symmetric about the ATM level. Both OTM puts and OTM calls have elevated implied volatility relative to ATM, forming a "U"-shaped curve. The curvature is controlled by $\sigma_v$: larger $\sigma_v$ means fatter tails in the return distribution, producing higher wings. The smile is centered at the forward price with equal left and right wings.

    **Case 2: $\rho = -0.5$ (moderate leverage).** The smile tilts to the left, creating a "smirk." OTM puts have higher implied volatility than the ATM level, while OTM calls have lower implied volatility. The left wing is elevated relative to the symmetric case, and the right wing is depressed. The overall shape is a decreasing function of strike, with residual curvature from $\sigma_v$.

    **Case 3: $\rho = -0.9$ (strong leverage).** The smirk becomes more pronounced. The implied volatility function is steeply decreasing in strike. OTM puts have significantly elevated implied volatility (reflecting the heavy left tail), while OTM calls have depressed implied volatility. The slope at ATM is approximately $\rho\sigma_v/(2\sqrt{V_0})$, which is $1.8$ times steeper than the $\rho = -0.5$ case.

    In all three cases, the ATM implied volatility level is approximately the same ($\approx \sqrt{V_0}$), since $\rho$ primarily affects the slope and asymmetry, not the overall level. The progression from $\rho = 0$ to $\rho = -0.9$ transforms a symmetric smile into an increasingly steep downward-sloping skew.

---

**Exercise 5.** The leverage effect implies that hedging a short call position requires buying more stock than the Black-Scholes delta suggests. Explain this qualitatively: when $\rho < 0$ and the stock drops, what happens to volatility, and how does this affect the option's delta?

??? success "Solution to Exercise 5"
    Consider a short call position. The Black-Scholes delta for a call is $\Delta_{\text{BS}} \in (0, 1)$, and we hedge by holding $\Delta_{\text{BS}}$ shares of stock.

    When $\rho < 0$ and the stock price drops:

    1. **Volatility increases** (leverage effect): The drop in $S$ is correlated with an increase in $V_t$. Higher volatility increases the value of the call option (via vega), partially offsetting the decrease due to the lower stock price.

    2. **Impact on the call's delta:** The call option loses value because the stock dropped (delta effect) but gains value because volatility increased (vega effect). The net sensitivity of the call to the stock price is larger than what Black-Scholes delta alone predicts, because each unit decrease in $S$ also triggers a volatility increase that further affects the option value.

    3. **Need for a larger hedge ratio:** To properly hedge, we need:

        $$
        \Delta_{\text{Heston}} = \Delta_{\text{BS}} + \frac{\partial V}{\partial v} \cdot \frac{\partial v}{\partial S}
        $$

        The term $\frac{\partial V}{\partial v}$ (vega-like sensitivity) is positive for a call. The term $\frac{\partial v}{\partial S}$ is negative when $\rho < 0$ (stock drops cause variance to rise). For a short call, the hedger needs to buy *more* stock than the Black-Scholes delta prescribes.

    Intuitively, when the stock drops, the short call position loses money not only from the directional move but also from the volatility increase. To offset this additional exposure, the hedger must hold more shares. Ignoring this effect (using Black-Scholes delta alone) leads to systematic under-hedging and losses during market selloffs.

---

**Exercise 6.** Empirical studies find $\rho \in [-0.9, -0.5]$ for equity indices but $\rho \approx 0$ or slightly positive for some commodities and FX pairs. Explain the economic mechanisms behind these differences.

??? success "Solution to Exercise 6"
    **Equity indices ($\rho \in [-0.9, -0.5]$):** The strongly negative correlation arises from multiple reinforcing mechanisms:

    - *Financial leverage:* When equity values drop, the firm's debt-to-equity ratio increases, making equity riskier and more volatile.
    - *Feedback effects:* Market declines trigger margin calls, forced selling, and de-leveraging, which amplify volatility.
    - *Risk aversion:* Investor panic during selloffs increases demand for protective options, driving up implied volatility.
    - *Volatility clustering:* Large moves (typically negative for equities due to the asymmetry of crashes vs. rallies) beget further large moves.

    These mechanisms are strongly directional: equity crashes are abrupt and volatility-increasing, while rallies are gradual and volatility-decreasing.

    **Foreign exchange ($\rho \approx 0$):** FX markets are fundamentally symmetric -- a strengthening of EUR/USD is simultaneously a weakening of USD/EUR. There is no inherent directional bias: a large move in either direction can increase uncertainty. Furthermore, central bank interventions and macroeconomic news can drive both appreciations and depreciations with similar volatility dynamics. The result is a near-symmetric implied volatility smile (the "butterfly" shape) rather than a skew.

    **Commodities ($\rho$ varies):** The sign of $\rho$ depends on the specific supply-demand dynamics:

    - *Oil:* Supply disruptions cause price spikes with increased volatility ($\rho > 0$ in some regimes), while demand drops cause price declines with increased volatility ($\rho < 0$). The net effect can be ambiguous.
    - *Gold:* As a safe-haven asset, gold prices often rise during market stress (when volatility is high), potentially giving $\rho > 0$.
    - *Agricultural commodities:* Weather shocks can cause price spikes with high volatility, suggesting $\rho > 0$.

    The key difference from equities is that commodities lack the systematic leverage mechanism: there is no analog of the debt-to-equity ratio that mechanically links price declines to volatility increases.
