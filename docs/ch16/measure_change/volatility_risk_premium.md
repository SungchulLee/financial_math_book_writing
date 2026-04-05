# Volatility Risk Premium

The volatility risk premium (VRP) is the compensation investors demand for bearing variance risk that cannot be hedged by trading the stock alone. In the Heston model, it manifests as the difference between the physical and risk-neutral variance dynamics: the mean-reversion speed shifts from $\kappa^{\mathbb{P}}$ to $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \xi\lambda$, and the long-run variance shifts from $\theta^{\mathbb{P}}$ to $\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/\kappa^{\mathbb{Q}}$. Understanding and estimating the VRP connects the Heston model's theoretical framework to observable market quantities: the difference between implied and realized variance.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Define the volatility risk premium within the Heston framework
    2. Derive how the VRP transforms the variance process parameters from $\mathbb{P}$ to $\mathbb{Q}$
    3. Relate the VRP to the implied-realized variance spread and the VIX
    4. Describe empirical methods for estimating the VRP from market data

---

## Intuition

Consider an investor who sells variance swaps, collecting a premium that compensates for the risk of realized variance exceeding the swap rate. Empirically, implied variance (priced under $\mathbb{Q}$) consistently exceeds realized variance (observed under $\mathbb{P}$). This spread is the volatility risk premium. It reflects the market's aversion to variance risk: investors are willing to accept a lower expected return on portfolios that protect against high-volatility regimes, effectively paying a premium for variance insurance.

In the Heston model, this premium is encoded by a single parameter $\lambda$ --- the market price of variance risk --- that governs how the physical mean-reversion level and speed transform into their risk-neutral counterparts.

---

## Definition of the Volatility Risk Premium

!!! info "Definition (Volatility Risk Premium)"
    The **volatility risk premium** in the Heston model is the difference between the expected variance under $\mathbb{Q}$ and under $\mathbb{P}$:

    $$
    \text{VRP}(t, T) = \frac{1}{T-t}\left[\mathbb{E}^{\mathbb{Q}}\!\left[\int_t^T v_s \, ds \,\bigg|\, \mathcal{F}_t\right] - \mathbb{E}^{\mathbb{P}}\!\left[\int_t^T v_s \, ds \,\bigg|\, \mathcal{F}_t\right]\right]
    $$

    This is the annualized difference between the risk-neutral expected integrated variance and the physical expected integrated variance.

Using the CIR conditional expectation $\mathbb{E}[v_s | v_t] = \theta + (v_t - \theta)e^{-\kappa(s-t)}$:

$$
\frac{1}{\tau}\mathbb{E}\!\left[\int_t^T v_s \, ds \,\bigg|\, v_t\right] = \theta + (v_t - \theta)\frac{1 - e^{-\kappa\tau}}{\kappa\tau}
$$

where $\tau = T - t$ and $(\kappa, \theta)$ are the measure-specific parameters.

---

## The Parameter Transformation

Recall the Girsanov measure change with $\lambda_v(t) = \lambda\sqrt{v_t}$ gives

$$
\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \xi\lambda, \qquad \theta^{\mathbb{Q}} = \frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{Q}}}
$$

!!! info "Proposition (VRP in Terms of Lambda)"
    The volatility risk premium is

    $$
    \text{VRP}(t, T) = \left(\theta^{\mathbb{Q}} - \theta^{\mathbb{P}}\right) + (v_t - \theta^{\mathbb{Q}})\frac{1 - e^{-\kappa^{\mathbb{Q}}\tau}}{\kappa^{\mathbb{Q}}\tau} - (v_t - \theta^{\mathbb{P}})\frac{1 - e^{-\kappa^{\mathbb{P}}\tau}}{\kappa^{\mathbb{P}}\tau}
    $$

    In the stationary limit ($v_t = \theta^{\mathbb{P}}$ and $\tau \to \infty$):

    $$
    \text{VRP} \approx \theta^{\mathbb{Q}} - \theta^{\mathbb{P}} = \theta^{\mathbb{P}}\left(\frac{\kappa^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \xi\lambda} - 1\right) = -\frac{\xi\lambda\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \xi\lambda}
    $$

**Interpretation.** When $\lambda > 0$ (the empirically dominant case):

- $\text{VRP} < 0$: risk-neutral expected variance is **lower** than physical expected variance in the long run, because $\theta^{\mathbb{Q}} < \theta^{\mathbb{P}}$
- However, the risk-neutral mean-reversion $\kappa^{\mathbb{Q}} > \kappa^{\mathbb{P}}$ means variance reverts faster under $\mathbb{Q}$

!!! warning "Sign Convention"
    The sign of the VRP depends on the convention. Some authors define VRP = implied $-$ realized (positive when implied exceeds realized), while others define it as realized $-$ implied (negative). In the Heston model with $\lambda > 0$, the short-term VRP (measuring $\mathbb{E}^{\mathbb{Q}}[v_t] - \mathbb{E}^{\mathbb{P}}[v_t]$ instantaneously) is zero because both measures share the same current variance $v_t$. The VRP emerges only over a horizon $\tau > 0$ through the different mean-reversion dynamics.

---

## Connection to the VIX and Variance Swaps

The VIX index approximates the square root of the risk-neutral expected integrated variance:

$$
\text{VIX}^2 \approx \frac{1}{\tau}\mathbb{E}^{\mathbb{Q}}\!\left[\int_t^{t+\tau} v_s \, ds \,\bigg|\, \mathcal{F}_t\right] = \theta^{\mathbb{Q}} + (v_t - \theta^{\mathbb{Q}})\frac{1 - e^{-\kappa^{\mathbb{Q}}\tau}}{\kappa^{\mathbb{Q}}\tau}
$$

where $\tau = 30/365$ for the standard 30-day VIX.

The **variance swap rate** for maturity $\tau$ is exactly $\mathbb{E}^{\mathbb{Q}}[\frac{1}{\tau}\int_t^T v_s \, ds]$ in the Heston model (since variance swaps have zero convexity correction in affine models). Therefore:

$$
\text{VRP}(t, T) = \text{Variance swap rate} - \frac{1}{\tau}\mathbb{E}^{\mathbb{P}}\!\left[\int_t^T v_s \, ds\right]
$$

!!! info "Proposition (VRP from VIX and Realized Variance)"
    An empirical estimator of the VRP is

    $$
    \widehat{\text{VRP}}_t = \text{VIX}_t^2 - \text{RV}_{t, t+\tau}
    $$

    where $\text{RV}_{t,t+\tau}$ is the realized variance computed from high-frequency returns over $[t, t+\tau]$. This is an ex-post estimator that becomes an ex-ante estimator when $\text{RV}$ is replaced by a forecast.

---

## Empirical Estimation of Lambda

The variance risk premium parameter $\lambda$ can be estimated from joint time-series and cross-sectional data.

### Method 1: Physical vs Risk-Neutral Mean Reversion

Estimate $\kappa^{\mathbb{P}}$ from a time series of realized variance (e.g., by fitting a discrete CIR model to daily VIX squared or realized variance), then obtain $\kappa^{\mathbb{Q}}$ from calibration to the options cross-section. The VRP parameter follows:

$$
\hat{\lambda} = \frac{\kappa^{\mathbb{Q}} - \kappa^{\mathbb{P}}}{\xi}
$$

### Method 2: Variance Swap Spread

Using the VRP estimator directly:

$$
\hat{\lambda} \approx -\frac{\widehat{\text{VRP}} \cdot \kappa^{\mathbb{Q}}}{\xi \theta^{\mathbb{P}}}
$$

This follows from the stationary VRP formula solved for $\lambda$.

### Method 3: Joint Calibration

Fit the Heston model simultaneously to:

1. Time-series data: estimate $(\kappa^{\mathbb{P}}, \theta^{\mathbb{P}}, \xi, \rho)$ from realized variance and returns
2. Cross-sectional data: calibrate $(\kappa^{\mathbb{Q}}, \theta^{\mathbb{Q}}, \xi, \rho, v_0)$ to the options surface
3. Extract $\lambda$ from the relationship $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \xi\lambda$

!!! tip "Typical Empirical Values"
    For S&P 500 equity index options:

    - $\lambda \in [0.5, 3.0]$: the variance risk premium is significantly positive
    - $\kappa^{\mathbb{P}} \in [1, 5]$, $\kappa^{\mathbb{Q}} \in [2, 8]$: risk-neutral mean reversion is substantially faster
    - $\theta^{\mathbb{P}} \approx 0.04$ (20% annual vol), $\theta^{\mathbb{Q}} \approx 0.02\text{--}0.035$: risk-neutral long-run variance is lower
    - $\text{VRP} \approx -0.01$ to $-0.03$ (annualized): implied variance exceeds realized by 1--3 percentage points

---

## Term Structure of the VRP

The VRP varies with the horizon $\tau$, creating a term structure.

**Short horizons ($\tau \to 0$).** As $\tau \to 0$, both $\mathbb{Q}$ and $\mathbb{P}$ expected integrated variances converge to $v_t$, and the VRP vanishes:

$$
\text{VRP}(t, t+\tau) \to 0 \quad \text{as } \tau \to 0
$$

**Long horizons ($\tau \to \infty$).** The VRP converges to the stationary value:

$$
\text{VRP}(t, \infty) = \theta^{\mathbb{Q}} - \theta^{\mathbb{P}} = -\frac{\xi\lambda\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \xi\lambda}
$$

**Intermediate horizons.** The VRP is a smooth, monotonically increasing (in magnitude) function of $\tau$, with the steepest change occurring around $\tau \sim 1/\kappa^{\mathbb{P}}$ (the physical mean-reversion timescale).

---

## Numerical Example

Consider $v_0 = 0.04$, $\kappa^{\mathbb{P}} = 2.0$, $\theta^{\mathbb{P}} = 0.04$, $\xi = 0.4$, $\lambda = 1.5$.

**Risk-neutral parameters:**

$$
\kappa^{\mathbb{Q}} = 2.0 + 0.4(1.5) = 2.6
$$

$$
\theta^{\mathbb{Q}} = \frac{2.0 \times 0.04}{2.6} = 0.0308
$$

**VRP for $\tau = 1$ year (with $v_0 = \theta^{\mathbb{P}} = 0.04$):**

$$
\mathbb{E}^{\mathbb{Q}}\!\left[\frac{1}{\tau}\int_0^1 v_s \, ds\right] = 0.0308 + (0.04 - 0.0308)\frac{1 - e^{-2.6}}{2.6} = 0.0308 + 0.0092 \times 0.3719 / 1 = 0.0342
$$

$$
\mathbb{E}^{\mathbb{P}}\!\left[\frac{1}{\tau}\int_0^1 v_s \, ds\right] = 0.04 + 0 = 0.04
$$

$$
\text{VRP} = 0.0342 - 0.04 = -0.0058
$$

In annualized volatility terms, this corresponds to implied volatility of $\sqrt{0.0342} = 18.5\%$ versus realized volatility of $\sqrt{0.04} = 20\%$. The risk-neutral world "expects" lower future variance because the faster mean reversion pulls variance down more quickly.

??? example "VRP Term Structure"
    | $\tau$ (years) | $\mathbb{E}^{\mathbb{Q}}[\bar{v}]$ | $\mathbb{E}^{\mathbb{P}}[\bar{v}]$ | VRP |
    |---------|--------------------------------|--------------------------------|-----|
    | 0.1 | 0.0393 | 0.04 | $-0.0007$ |
    | 0.5 | 0.0366 | 0.04 | $-0.0034$ |
    | 1.0 | 0.0342 | 0.04 | $-0.0058$ |
    | 2.0 | 0.0321 | 0.04 | $-0.0079$ |
    | 5.0 | 0.0310 | 0.04 | $-0.0090$ |
    | $\infty$ | 0.0308 | 0.04 | $-0.0092$ |

    The VRP magnitude increases with $\tau$ and converges to $\theta^{\mathbb{Q}} - \theta^{\mathbb{P}} = -0.0092$.

---

## Implications for Option Pricing and Hedging

The VRP has direct consequences for option pricing and risk management.

**Implied volatility bias.** The positive VRP ($\lambda > 0$) makes implied volatilities systematically exceed expected future realized volatility. This is not a mispricing but rather the market price of bearing variance risk.

**Selling variance is profitable on average.** Since implied variance exceeds realized variance on average, strategies that sell variance (short straddles, short variance swaps) earn the VRP as compensation. The expected P&L of a delta-hedged short option position is approximately:

$$
\mathbb{E}^{\mathbb{P}}[\text{P\&L}] \approx -\frac{1}{2}\Gamma S^2 \tau \cdot \text{VRP}
$$

which is positive when VRP $< 0$ (implied exceeds realized).

**Hedging effectiveness.** The VRP implies that hedging with implied volatility will systematically overhedge. For more accurate hedging, adjust the hedge volatility downward by the estimated VRP.

---

## Summary

The volatility risk premium in the Heston model is determined by the parameter $\lambda$ that governs the measure change from $\mathbb{P}$ to $\mathbb{Q}$, transforming $\kappa^{\mathbb{P}} \to \kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \xi\lambda$ and $\theta^{\mathbb{P}} \to \theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/\kappa^{\mathbb{Q}}$. When $\lambda > 0$ (the empirical norm for equity indices), the risk-neutral variance dynamics have faster mean reversion and a lower long-run level than the physical dynamics, producing a negative VRP (implied exceeds realized). The VRP connects to observable quantities through the variance swap rate and VIX, and it can be estimated from the spread between implied and realized variance or from joint time-series and cross-sectional calibration. The VRP has a term structure that ranges from zero at $\tau = 0$ to $\theta^{\mathbb{Q}} - \theta^{\mathbb{P}}$ at $\tau = \infty$, and its sign explains why selling options is profitable on average.

---

## Exercises

**Exercise 1.**
The stationary VRP is $\text{VRP}(\infty) = \theta^{\mathbb{Q}} - \theta^{\mathbb{P}} = -\xi\lambda\theta^{\mathbb{P}}/(\kappa^{\mathbb{P}} + \xi\lambda)$. For the numerical example ($\kappa^{\mathbb{P}} = 2.0$, $\theta^{\mathbb{P}} = 0.04$, $\xi = 0.4$, $\lambda = 1.5$), verify that $\text{VRP}(\infty) = -0.0092$. Convert this to annualized volatility units by computing $\sqrt{\theta^{\mathbb{Q}}} - \sqrt{\theta^{\mathbb{P}}}$ and interpret the result.

??? success "Solution to Exercise 1"
    **Verification of $\text{VRP}(\infty)$.**

    $$
    \text{VRP}(\infty) = \theta^{\mathbb{Q}} - \theta^{\mathbb{P}} = -\frac{\xi\lambda\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \xi\lambda}
    $$

    Substituting $\kappa^{\mathbb{P}} = 2.0$, $\theta^{\mathbb{P}} = 0.04$, $\xi = 0.4$, $\lambda = 1.5$:

    $$
    \text{VRP}(\infty) = -\frac{0.4 \times 1.5 \times 0.04}{2.0 + 0.4 \times 1.5} = -\frac{0.024}{2.6} = -0.00923
    $$

    Rounding to four decimal places: $\text{VRP}(\infty) \approx -0.0092$. Confirmed.

    Equivalently, $\theta^{\mathbb{Q}} = 0.0308$ and $\theta^{\mathbb{P}} = 0.04$, so $\text{VRP}(\infty) = 0.0308 - 0.04 = -0.0092$.

    **Conversion to annualized volatility:**

    $$
    \sqrt{\theta^{\mathbb{Q}}} - \sqrt{\theta^{\mathbb{P}}} = \sqrt{0.0308} - \sqrt{0.04} = 0.1754 - 0.2000 = -0.0246
    $$

    This means the risk-neutral long-run volatility is approximately 17.5%, while the physical long-run volatility is 20%. The difference of $-2.46$ percentage points is the volatility risk premium expressed in volatility units. Investors price options as if long-run volatility is about 2.5 percentage points lower than the physical level, reflecting the compensation they demand for bearing variance risk. Equivalently, variance sellers earn an expected annualized return corresponding to this 2.5 percentage point spread.

---

**Exercise 2.**
The VRP term structure goes from 0 at $\tau = 0$ to $\theta^{\mathbb{Q}} - \theta^{\mathbb{P}}$ at $\tau = \infty$. Using the exact formulas, compute the VRP at $\tau = 0.1, 0.5, 1.0, 2.0$ for the numerical example parameters. At what maturity $\tau^*$ does the VRP reach 90% of its asymptotic value? How does $\tau^*$ relate to the physical mean-reversion timescale $1/\kappa^{\mathbb{P}}$?

??? success "Solution to Exercise 2"
    **VRP formula.** With $v_0 = \theta^{\mathbb{P}} = 0.04$ (stationary case):

    $$
    \text{VRP}(\tau) = \left(\theta^{\mathbb{Q}} - \theta^{\mathbb{P}}\right) + (v_0 - \theta^{\mathbb{Q}})\frac{1 - e^{-\kappa^{\mathbb{Q}}\tau}}{\kappa^{\mathbb{Q}}\tau} - (v_0 - \theta^{\mathbb{P}})\frac{1 - e^{-\kappa^{\mathbb{P}}\tau}}{\kappa^{\mathbb{P}}\tau}
    $$

    Since $v_0 = \theta^{\mathbb{P}} = 0.04$, the last term vanishes. With $\theta^{\mathbb{Q}} = 0.0308$ and $\kappa^{\mathbb{Q}} = 2.6$:

    $$
    \text{VRP}(\tau) = (0.0308 - 0.04) + (0.04 - 0.0308)\frac{1 - e^{-2.6\tau}}{2.6\tau}
    $$

    $$
    = -0.0092 + 0.0092\cdot\frac{1 - e^{-2.6\tau}}{2.6\tau}
    $$

    $$
    = -0.0092\left(1 - \frac{1 - e^{-2.6\tau}}{2.6\tau}\right)
    $$

    **Computing for each $\tau$:**

    For $\tau = 0.1$: $2.6\tau = 0.26$, $e^{-0.26} = 0.7711$, $(1 - 0.7711)/0.26 = 0.8804$.

    $$
    \text{VRP}(0.1) = -0.0092(1 - 0.8804) = -0.0092 \times 0.1196 = -0.0011
    $$

    For $\tau = 0.5$: $2.6\tau = 1.3$, $e^{-1.3} = 0.2725$, $(1 - 0.2725)/1.3 = 0.5596$.

    $$
    \text{VRP}(0.5) = -0.0092(1 - 0.5596) = -0.0092 \times 0.4404 = -0.0041
    $$

    For $\tau = 1.0$: $2.6\tau = 2.6$, $e^{-2.6} = 0.0743$, $(1 - 0.0743)/2.6 = 0.3560$.

    $$
    \text{VRP}(1.0) = -0.0092(1 - 0.3560) = -0.0092 \times 0.6440 = -0.0059
    $$

    For $\tau = 2.0$: $2.6\tau = 5.2$, $e^{-5.2} = 0.0055$, $(1 - 0.0055)/5.2 = 0.1912$.

    $$
    \text{VRP}(2.0) = -0.0092(1 - 0.1912) = -0.0092 \times 0.8088 = -0.0074
    $$

    **Finding $\tau^*$ where VRP reaches 90% of asymptote.** We need

    $$
    1 - \frac{1 - e^{-2.6\tau^*}}{2.6\tau^*} = 0.9
    $$

    $$
    \frac{1 - e^{-2.6\tau^*}}{2.6\tau^*} = 0.1
    $$

    Let $x = 2.6\tau^*$. We need $(1 - e^{-x})/x = 0.1$, i.e., $1 - e^{-x} = 0.1x$. Solving numerically: at $x = 4.0$, LHS $= 0.982$, RHS $= 0.4$ (no); at $x = 6$, LHS $= 0.998$, RHS $= 0.6$ (no); at $x = 9$, LHS $= 0.9999$, RHS $= 0.9$ (close). Refining: at $x = 9.1$, RHS $= 0.91$; at $x \approx 8.7$, RHS $= 0.87$. Solving more carefully, $x \approx 9.0$, giving $\tau^* \approx 9.0/2.6 \approx 3.46$ years.

    The physical mean-reversion timescale is $1/\kappa^{\mathbb{P}} = 1/2.0 = 0.5$ years. The 90% convergence time is about $\tau^* \approx 3.5$ years $\approx 7/\kappa^{\mathbb{P}}$, which is several multiples of the physical timescale. This is because the VRP depends on the risk-neutral mean reversion $\kappa^{\mathbb{Q}} = 2.6$, and convergence to the stationary VRP requires $\tau \gg 1/\kappa^{\mathbb{Q}} \approx 0.38$ years.

---

**Exercise 3.**
Method 1 for estimating $\lambda$ uses $\hat{\lambda} = (\kappa^{\mathbb{Q}} - \kappa^{\mathbb{P}})/\xi$. Suppose $\kappa^{\mathbb{P}} = 2.0$ (estimated from realized variance time series) and $\kappa^{\mathbb{Q}} = 3.5$ (calibrated from the options surface), with $\xi = 0.4$. Compute $\hat{\lambda}$ and the corresponding $\theta^{\mathbb{Q}}$ given $\theta^{\mathbb{P}} = 0.04$. How sensitive is $\hat{\lambda}$ to the estimation error in $\kappa^{\mathbb{P}}$? If $\kappa^{\mathbb{P}}$ has a standard error of $\pm 0.5$, what is the range of $\hat{\lambda}$?

??? success "Solution to Exercise 3"
    **Computing $\hat{\lambda}$ and $\theta^{\mathbb{Q}}$:**

    $$
    \hat{\lambda} = \frac{\kappa^{\mathbb{Q}} - \kappa^{\mathbb{P}}}{\xi} = \frac{3.5 - 2.0}{0.4} = \frac{1.5}{0.4} = 3.75
    $$

    $$
    \theta^{\mathbb{Q}} = \frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{Q}}} = \frac{2.0 \times 0.04}{3.5} = \frac{0.08}{3.5} = 0.0229
    $$

    **Sensitivity to $\kappa^{\mathbb{P}}$ estimation error.** With standard error $\pm 0.5$ on $\kappa^{\mathbb{P}}$:

    If $\kappa^{\mathbb{P}} = 2.5$ (upper bound):

    $$
    \hat{\lambda} = \frac{3.5 - 2.5}{0.4} = \frac{1.0}{0.4} = 2.5
    $$

    If $\kappa^{\mathbb{P}} = 1.5$ (lower bound):

    $$
    \hat{\lambda} = \frac{3.5 - 1.5}{0.4} = \frac{2.0}{0.4} = 5.0
    $$

    **Range of $\hat{\lambda}$: $[2.5, 5.0]$.**

    The point estimate is $\hat{\lambda} = 3.75$, but the uncertainty range $[2.5, 5.0]$ is enormous --- the width is 2.5, which is 67% of the point estimate. The sensitivity is

    $$
    \frac{\partial\hat{\lambda}}{\partial\kappa^{\mathbb{P}}} = -\frac{1}{\xi} = -\frac{1}{0.4} = -2.5
    $$

    A one-unit change in $\kappa^{\mathbb{P}}$ produces a 2.5-unit change in $\hat{\lambda}$ (in the opposite direction). This means that the estimation error in $\hat{\lambda}$ is amplified by the factor $1/\xi$ relative to the estimation error in $\kappa^{\mathbb{P}}$. When $\xi$ is small, this amplification is severe.

    This high sensitivity is a fundamental challenge for Method 1: the physical mean-reversion speed is notoriously difficult to estimate precisely from time-series data (CIR parameter estimation has large finite-sample bias for $\kappa$), and the resulting uncertainty propagates directly into $\hat{\lambda}$ through division by $\xi$.

---

**Exercise 4.**
The expected P&L of a delta-hedged short option position is approximately $\mathbb{E}^{\mathbb{P}}[\text{P\&L}] \approx -\frac{1}{2}\Gamma S^2 \tau \cdot \text{VRP}$. For an ATM call with $\Gamma = 0.02$, $S = 100$, $\tau = 1/12$ (monthly), and $\text{VRP} = -0.006$, compute the expected monthly P&L. Explain why this is positive (profit from selling options) and estimate the annualized Sharpe ratio if the P&L standard deviation is three times the expected P&L.

??? success "Solution to Exercise 4"
    **Expected monthly P&L:**

    $$
    \mathbb{E}^{\mathbb{P}}[\text{P\&L}] \approx -\frac{1}{2}\Gamma S^2 \tau \cdot \text{VRP}
    $$

    $$
    = -\frac{1}{2}(0.02)(100)^2\left(\frac{1}{12}\right)(-0.006)
    $$

    $$
    = -\frac{1}{2}(0.02)(10000)(0.0833)(-0.006)
    $$

    $$
    = -(0.5)(0.02)(10000)(0.0833)(-0.006)
    $$

    $$
    = -(8.333)(-0.006) = 0.05
    $$

    The expected monthly P&L is approximately \$0.05 per option.

    **Why this is positive.** The VRP is negative ($\text{VRP} = -0.006$), meaning implied variance exceeds realized variance. The seller of an option collects a premium based on implied volatility but the actual hedging cost is determined by realized volatility. Since realized volatility is systematically lower than implied, the seller earns the difference as profit. The gamma $\Gamma > 0$ means the option's curvature creates a hedging cost proportional to variance, and the negative VRP makes the expected net profit positive.

    **Annualized Sharpe ratio.** The annualized expected P&L is $0.05 \times 12 = 0.60$. The monthly P&L standard deviation is $3 \times 0.05 = 0.15$. The annualized standard deviation is $0.15\sqrt{12} = 0.5196$. The annualized Sharpe ratio is

    $$
    \text{SR} = \frac{0.60}{0.5196} \approx 1.15
    $$

    A Sharpe ratio above 1 is attractive but relies on the VRP persisting over time. In practice, the variance selling strategy has a negatively skewed return distribution (large losses during volatility spikes), so the Sharpe ratio overstates the risk-adjusted attractiveness compared to strategies with symmetric returns.

---

**Exercise 5.**
The VIX approximates $\sqrt{\mathbb{E}^{\mathbb{Q}}[\frac{1}{\tau}\int_t^{t+\tau} v_s\,ds]}$ with $\tau = 30/365$. Using the Heston formula for the risk-neutral expected integrated variance, compute VIX for $v_0 = 0.04$ and $v_0 = 0.09$ (market stress) using the numerical example parameters. What percentage increase in VIX corresponds to the doubling of $v_0$?

??? success "Solution to Exercise 5"
    The VIX approximation in the Heston model is

    $$
    \text{VIX}^2 \approx \theta^{\mathbb{Q}} + (v_0 - \theta^{\mathbb{Q}})\frac{1 - e^{-\kappa^{\mathbb{Q}}\tau}}{\kappa^{\mathbb{Q}}\tau}
    $$

    with $\tau = 30/365 = 0.0822$, $\kappa^{\mathbb{Q}} = 2.6$, $\theta^{\mathbb{Q}} = 0.0308$.

    First compute the common factor: $\kappa^{\mathbb{Q}}\tau = 2.6 \times 0.0822 = 0.2137$, $e^{-0.2137} = 0.8075$, $(1 - 0.8075)/0.2137 = 0.9005$.

    **Case 1: $v_0 = 0.04$ (normal market).**

    $$
    \text{VIX}^2 = 0.0308 + (0.04 - 0.0308)(0.9005) = 0.0308 + 0.0092 \times 0.9005 = 0.0308 + 0.0083 = 0.0391
    $$

    $$
    \text{VIX} = \sqrt{0.0391} = 0.1977 \approx 19.8\%
    $$

    **Case 2: $v_0 = 0.09$ (market stress).**

    $$
    \text{VIX}^2 = 0.0308 + (0.09 - 0.0308)(0.9005) = 0.0308 + 0.0592 \times 0.9005 = 0.0308 + 0.0533 = 0.0841
    $$

    $$
    \text{VIX} = \sqrt{0.0841} = 0.2900 \approx 29.0\%
    $$

    **Percentage increase in VIX:**

    $$
    \frac{29.0 - 19.8}{19.8} \times 100\% = \frac{9.2}{19.8} \times 100\% \approx 46.5\%
    $$

    A doubling of $v_0$ (from 0.04 to 0.09) produces approximately a 47% increase in VIX, not a doubling. This is because VIX is approximately $\sqrt{v_0}$ for short maturities, and $\sqrt{0.09}/\sqrt{0.04} = 0.3/0.2 = 1.5$ (a 50% increase). The slightly lower figure of 47% reflects the partial mean reversion over the 30-day window, which pulls the stressed $v_0 = 0.09$ back toward $\theta^{\mathbb{Q}} = 0.0308$.

---

**Exercise 6.**
The sign convention warning notes that the VRP can be defined as either implied $-$ realized or realized $-$ implied. In the Heston model with $\lambda > 0$, the long-run VRP is $\theta^{\mathbb{Q}} - \theta^{\mathbb{P}} < 0$. However, empirically the "VIX minus realized vol" spread is typically positive. Reconcile these: show that $\text{VIX}^2 - \mathbb{E}^{\mathbb{P}}[\text{RV}] < 0$ in the Heston model when $\lambda > 0$, but $\text{VIX} - \sqrt{\mathbb{E}^{\mathbb{P}}[\text{RV}]}$ can be either sign due to Jensen's inequality.

??? success "Solution to Exercise 6"
    **Variance-level comparison.** In the Heston model with $\lambda > 0$, the stationary VRP is

    $$
    \text{VIX}^2 - \mathbb{E}^{\mathbb{P}}[\text{RV}] \approx \theta^{\mathbb{Q}} - \theta^{\mathbb{P}} < 0
    $$

    since $\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/(\kappa^{\mathbb{P}} + \xi\lambda) < \theta^{\mathbb{P}}$. This means that at the variance level, implied variance is lower than expected realized variance in the long run, which may seem counterintuitive.

    **Empirical observation.** The commonly cited empirical fact is that VIX (a volatility, not variance, quantity) tends to exceed realized volatility. The apparent contradiction arises from Jensen's inequality.

    **Reconciliation via Jensen's inequality.** Define the risk-neutral expected integrated variance as $V^{\mathbb{Q}} = \mathbb{E}^{\mathbb{Q}}[\bar{v}]$ and the physical expected integrated variance as $V^{\mathbb{P}} = \mathbb{E}^{\mathbb{P}}[\bar{v}]$. We have established $V^{\mathbb{Q}} < V^{\mathbb{P}}$ when $\lambda > 0$.

    Now consider the volatility-level comparison. By Jensen's inequality (since $\sqrt{\cdot}$ is concave):

    $$
    \text{VIX} = \sqrt{V^{\mathbb{Q}}} \leq \sqrt{V^{\mathbb{P}}}
    $$

    However, the empirically observed "realized volatility" is typically computed as $\text{RV}_{\text{vol}} = \sqrt{\text{RV}_{\text{var}}}$, and for a single realization:

    $$
    \mathbb{E}^{\mathbb{P}}[\sqrt{\text{RV}_{\text{var}}}] \leq \sqrt{\mathbb{E}^{\mathbb{P}}[\text{RV}_{\text{var}}]} = \sqrt{V^{\mathbb{P}}}
    $$

    again by Jensen's inequality. So the comparison between $\text{VIX} = \sqrt{V^{\mathbb{Q}}}$ and $\mathbb{E}^{\mathbb{P}}[\sqrt{\text{RV}_{\text{var}}}]$ involves two applications of Jensen's inequality pushing in the same direction.

    The key insight is that even though $V^{\mathbb{Q}} < V^{\mathbb{P}}$ at the variance level, the relationship at the volatility level depends on the variance of realized variance. If $\text{RV}_{\text{var}}$ is highly variable (as it is empirically), the Jensen gap $\sqrt{V^{\mathbb{P}}} - \mathbb{E}^{\mathbb{P}}[\sqrt{\text{RV}_{\text{var}}}]$ can be large, making $\mathbb{E}^{\mathbb{P}}[\sqrt{\text{RV}}]$ substantially below $\sqrt{V^{\mathbb{P}}}$. This can result in

    $$
    \text{VIX} = \sqrt{V^{\mathbb{Q}}} > \mathbb{E}^{\mathbb{P}}[\sqrt{\text{RV}_{\text{var}}}]
    $$

    even though $V^{\mathbb{Q}} < V^{\mathbb{P}}$. In other words, the "VIX premium" (VIX exceeding realized vol) is a volatility-level phenomenon that is consistent with a negative variance-level VRP, reconciled by Jensen's inequality and the high variability of realized variance.

---

**Exercise 7.**
Joint calibration (Method 3) fits both time-series and cross-sectional data simultaneously. Discuss the practical challenges: the time-series estimate of $\kappa^{\mathbb{P}}$ requires long histories of realized variance data, which may not be stationary, while the cross-sectional estimate of $\kappa^{\mathbb{Q}}$ depends on the option surface on a single date. How would you ensure that the estimated $\lambda$ is stable over time?

??? success "Solution to Exercise 7"
    **Practical challenges of joint calibration:**

    **1. Time-series estimation of $\kappa^{\mathbb{P}}$.** The physical mean-reversion speed governs how quickly variance returns to its long-run level. Estimating it requires:

    - **Long data histories**: Mean reversion operates on timescales of months to years ($1/\kappa^{\mathbb{P}} \approx 0.5$ years for typical parameters). Reliable estimation requires multiple mean-reversion cycles, necessitating 5--10+ years of data.
    - **Stationarity assumption**: The CIR model assumes constant $(\kappa^{\mathbb{P}}, \theta^{\mathbb{P}}, \xi)$. Over long horizons, these parameters may shift due to structural changes in market microstructure, monetary policy regimes, or evolving market composition.
    - **Estimation bias**: Discrete-time estimators of CIR parameters exhibit substantial finite-sample bias. The MLE for $\kappa$ is biased upward (overestimating mean-reversion speed), which would bias $\hat{\lambda}$ downward.
    - **Proxy choice**: One must choose a proxy for $v_t$ (VIX squared, realized variance from high-frequency data, GARCH-filtered variance), and different proxies yield different $\hat{\kappa}^{\mathbb{P}}$.

    **2. Cross-sectional estimation of $\kappa^{\mathbb{Q}}$.** The risk-neutral parameters come from calibrating the Heston model to the observed option surface on a single date. Challenges include:

    - **Single-date snapshot**: $\kappa^{\mathbb{Q}}$ is identified from the term structure of implied volatility on one day. Different days yield different $\hat{\kappa}^{\mathbb{Q}}$, introducing time variation.
    - **Identification**: $\kappa^{\mathbb{Q}}$ and $\theta^{\mathbb{Q}}$ are jointly identified from the volatility term structure but can be poorly identified if only short-maturity options are liquid.
    - **Model misspecification**: The Heston model may not fit the observed surface perfectly, introducing calibration error that propagates into $\hat{\kappa}^{\mathbb{Q}}$.

    **3. Ensuring stability of $\hat{\lambda}$ over time.** Several approaches can improve stability:

    - **Rolling estimation**: Estimate $\kappa^{\mathbb{P}}$ from a rolling window (e.g., 5-year) and $\kappa^{\mathbb{Q}}$ daily from the options surface. Average $\hat{\lambda}$ over time to reduce noise.
    - **Bayesian estimation**: Place priors on $\lambda$ (or equivalently on $\kappa^{\mathbb{P}}$) to regularize the estimate and prevent extreme values driven by short-term fluctuations.
    - **Panel methods**: Use a panel of option maturities and multiple observation dates simultaneously, estimating a single $\lambda$ (or a slowly varying $\lambda_t$) that best explains the joint time-series and cross-sectional data.
    - **Structural constraints**: Impose economic constraints such as $\lambda > 0$ (positive variance risk premium) and $\kappa^{\mathbb{Q}} > \kappa^{\mathbb{P}}$ (risk-neutral mean reversion faster than physical), which are well-supported empirically and prevent sign-flipping instabilities.
    - **Filtering approaches**: Use Kalman or particle filters to jointly estimate $v_t$, $\kappa^{\mathbb{P}}$, and $\lambda$ from option prices and returns in a state-space framework, which optimally combines time-series and cross-sectional information.
