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
