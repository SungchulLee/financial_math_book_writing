# Calibration to Yield Curve and Caps

Calibration is the process of determining model parameters so that the model reproduces observed market prices. For the Vasicek model with three parameters $(\kappa, \theta, \sigma)$, calibration targets fall into two categories: the **yield curve** (bond prices or equivalently zero rates) and **volatility instruments** (cap and swaption prices). This section develops both calibration approaches, presents maximum likelihood estimation for historical data, and discusses the fundamental tension between fitting the initial curve and fitting option prices with a time-homogeneous model.

---

## Calibration to the yield curve

### Objective function

Given observed zero-coupon bond prices $P^{\text{mkt}}(0, T_i)$ for maturities $T_1, \ldots, T_n$, the calibration minimizes the weighted sum of squared errors:

$$
\min_{\kappa, \theta, \sigma} \sum_{i=1}^n w_i \left(P^{\text{model}}(0, T_i; \kappa, \theta, \sigma, r_0) - P^{\text{mkt}}(0, T_i)\right)^2
$$

where $P^{\text{model}}(0, T_i) = A(T_i)\,e^{-B(T_i)\,r_0}$ is the Vasicek bond price and $w_i > 0$ are weights (often $w_i = 1$ or $w_i = 1/P^{\text{mkt}}(0,T_i)^2$ for relative pricing errors).

### Equivalent yield-based formulation

Equivalently, one can minimize yield errors:

$$
\min_{\kappa, \theta, \sigma} \sum_{i=1}^n w_i \left(R^{\text{model}}(0, T_i) - R^{\text{mkt}}(0, T_i)\right)^2
$$

where $R^{\text{model}}(0, T_i) = -\ln P^{\text{model}}(0, T_i)/T_i$. The yield formulation has the advantage that errors are on a comparable scale across maturities.

### The initial rate

The current short rate $r_0$ can be treated as:

1. **Observable**: Set $r_0$ equal to the overnight rate (e.g., the Fed Funds rate or SOFR). Then only $(\kappa, \theta, \sigma)$ are free parameters.
2. **Free parameter**: Include $r_0$ in the optimization, giving four parameters. This provides a better fit but may produce $r_0$ inconsistent with the observed overnight rate.

### Fundamental limitation

The Vasicek model with constant parameters $(\kappa, \theta, \sigma)$ produces a yield curve that is a specific functional form---a weighted average of $r_0$ and $R_\infty$ plus a convexity term. This family of curves cannot match an arbitrary observed yield curve exactly. The calibration finds the best fit within this restricted family.

The mismatch is typically largest at intermediate maturities (2--5 years), where the observed curve may have features (kinks, local humps) that the smooth Vasicek curve cannot reproduce.

!!! note "Exact fit via Hull-White"
    The Hull-White extension $dr_t = (\theta(t) - \kappa\,r_t)\,dt + \sigma\,dW_t$ replaces the constant $\theta$ with a time-dependent function $\theta(t)$ chosen to match the initial yield curve exactly. This eliminates the yield curve fitting error at the cost of a non-stationary model.

---

## Calibration to cap volatilities

### Cap prices in the Vasicek model

A cap with strike $\kappa_{\text{cap}}$ consists of caplets, each priced as a ZCB put (as derived in the caplet section):

$$
\text{Cap}^{\text{model}} = \sum_{k=1}^n (1 + \delta_k\,\kappa_{\text{cap}})\,\text{Put}_{\text{ZCB}}(0;\, K_k,\, T_{k-1},\, T_k)
$$

### Implied volatility matching

Market cap prices are often quoted in terms of Black implied volatilities $\sigma_{\text{Black},k}^{\text{mkt}}$. The calibration objective is

$$
\min_{\kappa, \theta, \sigma} \sum_{k=1}^n w_k \left(\sigma_{\text{Black},k}^{\text{model}}(\kappa, \theta, \sigma) - \sigma_{\text{Black},k}^{\text{mkt}}\right)^2
$$

where $\sigma_{\text{Black},k}^{\text{model}}$ is obtained by inverting the Black formula applied to the Vasicek caplet price.

### Joint calibration

In practice, one calibrates to both yields and volatilities simultaneously:

$$
\min_{\kappa, \theta, \sigma} \left[\lambda_1 \sum_i w_i^{\text{yield}}\!\left(R_i^{\text{model}} - R_i^{\text{mkt}}\right)^2 + \lambda_2 \sum_k w_k^{\text{vol}}\!\left(\sigma_k^{\text{model}} - \sigma_k^{\text{mkt}}\right)^2\right]
$$

where $\lambda_1, \lambda_2 > 0$ control the relative importance of yield fit versus volatility fit.

The three parameters $(\kappa, \theta, \sigma)$ play different roles:

- $\theta$ and $r_0$ primarily control the **level** of the yield curve
- $\kappa$ controls the **slope** (how fast yields converge to $R_\infty$)
- $\sigma$ controls **cap volatilities** and the convexity correction

---

## Maximum likelihood estimation

### Setting

Given discrete observations $r_{t_0}, r_{t_1}, \ldots, r_{t_N}$ at equally spaced times $\Delta t = t_{i+1} - t_i$, the Vasicek transition density is

$$
r_{t_{i+1}} \mid r_{t_i} \sim \mathcal{N}\!\left(\mu_i,\, v^2\right)
$$

where $\mu_i = \theta + (r_{t_i} - \theta)\,e^{-\kappa\Delta t}$ and $v^2 = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\Delta t})$.

### Log-likelihood function

The log-likelihood is

$$
\ell(\kappa, \theta, \sigma) = -\frac{N}{2}\ln(2\pi v^2) - \frac{1}{2v^2}\sum_{i=0}^{N-1}\left(r_{t_{i+1}} - \mu_i\right)^2
$$

Defining $\phi = e^{-\kappa\Delta t}$, this can be written as

$$
\ell = -\frac{N}{2}\ln(2\pi v^2) - \frac{1}{2v^2}\sum_{i=0}^{N-1}\left(r_{t_{i+1}} - \theta(1-\phi) - \phi\,r_{t_i}\right)^2
$$

### Closed-form MLE

The log-likelihood is that of a linear regression $r_{t_{i+1}} = a + b\,r_{t_i} + \varepsilon_i$ with $a = \theta(1-\phi)$, $b = \phi$, $\varepsilon_i \sim \mathcal{N}(0, v^2)$. The MLEs are obtained by ordinary least squares:

$$
\hat{b} = \frac{\sum_{i=0}^{N-1}(r_{t_i} - \bar{r}_{\text{lag}})(r_{t_{i+1}} - \bar{r}_{\text{lead}})}{\sum_{i=0}^{N-1}(r_{t_i} - \bar{r}_{\text{lag}})^2}
$$

$$
\hat{a} = \bar{r}_{\text{lead}} - \hat{b}\,\bar{r}_{\text{lag}}
$$

$$
\hat{v}^2 = \frac{1}{N}\sum_{i=0}^{N-1}\left(r_{t_{i+1}} - \hat{a} - \hat{b}\,r_{t_i}\right)^2
$$

where $\bar{r}_{\text{lag}} = \frac{1}{N}\sum r_{t_i}$ and $\bar{r}_{\text{lead}} = \frac{1}{N}\sum r_{t_{i+1}}$.

The Vasicek parameters are recovered via

$$
\hat{\kappa} = -\frac{\ln \hat{b}}{\Delta t}, \qquad \hat{\theta} = \frac{\hat{a}}{1 - \hat{b}}, \qquad \hat{\sigma} = \hat{v}\,\sqrt{\frac{2\hat{\kappa}}{1 - e^{-2\hat{\kappa}\Delta t}}}
$$

???+ note "Asymptotic standard errors"
    The Fisher information matrix for the OU regression is available in closed form. The standard errors of $\hat{\kappa}$, $\hat{\theta}$, $\hat{\sigma}$ can be obtained by the delta method applied to the transformation $(a, b, v^2) \to (\kappa, \theta, \sigma)$. For typical weekly data over 10 years ($N \approx 520$), the standard error of $\hat{\kappa}$ is often large, reflecting the difficulty of estimating mean-reversion speed from short time series.

---

## Parameter identifiability

### The kappa estimation problem

Mean-reversion speed $\kappa$ is notoriously difficult to estimate reliably. The key issue is that $e^{-\kappa\Delta t}$ is close to $1$ for typical values of $\kappa$ and $\Delta t$:

- Weekly data: $e^{-\kappa/52} \approx 1 - \kappa/52$
- For $\kappa = 0.3$: $e^{-0.3/52} = 0.9942$

The regression coefficient $b$ is close to $1$, making it hard to distinguish from a unit root ($b = 1$, no mean reversion). This is the classic **near-unit-root** problem in econometrics.

### Risk-neutral vs physical parameters

MLE estimates the **physical measure** parameters $(\kappa^{\mathbb{P}}, \theta^{\mathbb{P}}, \sigma)$. The risk-neutral parameters $(\kappa^{\mathbb{Q}}, \theta^{\mathbb{Q}}, \sigma)$ that enter bond pricing are related by the market price of risk $\lambda$:

$$
\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda, \qquad \theta^{\mathbb{Q}} = \frac{\kappa^{\mathbb{P}}\,\theta^{\mathbb{P}}}{\kappa^{\mathbb{P}} + \lambda}
$$

Cross-sectional calibration to bond prices identifies $(\kappa^{\mathbb{Q}}, \theta^{\mathbb{Q}})$, while time-series estimation identifies $(\kappa^{\mathbb{P}}, \theta^{\mathbb{P}})$. The market price of risk $\lambda$ connects the two and is identified by combining both data sources.

---

## Practical calibration workflow

A typical calibration proceeds as follows:

1. **Collect market data**: Zero rates $R^{\text{mkt}}(0, T_i)$ for $T_i \in \{0.25, 0.5, 1, 2, 3, 5, 7, 10, 20, 30\}$ years, and ATM cap volatilities $\sigma^{\text{Black}}_k$ for maturities $\{1, 2, 3, 5, 7, 10\}$ years.

2. **Set initial guess**: $\kappa_0 = 0.3$, $\theta_0 = R^{\text{mkt}}(0, 10)$, $\sigma_0 = 0.01$.

3. **Optimize**: Use Nelder-Mead or Levenberg-Marquardt to minimize the joint objective.

4. **Validate**: Compare model yields and cap vols against market values. Check that the residuals are within bid-ask spreads.

5. **Stability check**: Perturb the initial guess and verify convergence to the same minimum. Compute parameter standard errors from the Hessian.

---

## Numerical example

**Market data** (stylized):

| Maturity | Market Yield |
|:-:|:-:|
| 1Y | 3.50% |
| 2Y | 3.80% |
| 5Y | 4.10% |
| 10Y | 4.30% |
| 30Y | 4.40% |

**Calibration result**: $\hat{\kappa} = 0.25$, $\hat{\theta} = 0.0455$, $\hat{\sigma} = 0.018$, $r_0 = 0.034$.

| Maturity | Market Yield | Model Yield | Error (bp) |
|:-:|:-:|:-:|:-:|
| 1Y | 3.50% | 3.52% | 2 |
| 2Y | 3.80% | 3.76% | $-4$ |
| 5Y | 4.10% | 4.12% | 2 |
| 10Y | 4.30% | 4.32% | 2 |
| 30Y | 4.40% | 4.43% | 3 |

The fit is within 5 basis points across all maturities---acceptable for a three-parameter model, though not as precise as the exact fit achievable with Hull-White.

---

## Summary

Calibration of the Vasicek model involves fitting three parameters $(\kappa, \theta, \sigma)$ to market yields and/or cap volatilities. Yield curve calibration minimizes pricing errors across observed maturities, with the fundamental constraint that a three-parameter model cannot match an arbitrary curve exactly. Cap volatility calibration targets the single parameter $\sigma$ that drives option prices. Maximum likelihood estimation on historical rate data provides an alternative (physical measure) calibration via the AR(1) regression structure of the OU process, with the caveat that the mean-reversion speed is poorly identified from short time series. The distinction between physical and risk-neutral parameters requires combining cross-sectional and time-series information.

---

## Exercises

**Exercise 1.** Write the yield-space objective function for calibrating Vasicek to 5 market zero rates. How many free parameters are there, and why is the problem over-determined?

---

**Exercise 2.** Using the calibrated parameters $\hat{\kappa} = 0.25$, $\hat{\theta} = 0.0455$, $\hat{\sigma} = 0.018$, compute the Vasicek long-run yield $R_\infty = \theta - \sigma^2/(2\kappa^2)$. Compare this with the 30Y market yield of 4.40%.

---

**Exercise 3.** In MLE for the Vasicek model, the discretized OU process gives the AR(1) regression $r_{t+\Delta t} = \alpha + \beta r_t + \epsilon_t$. Express $\kappa$, $\theta$, and $\sigma$ in terms of $\alpha$, $\beta$, and $\text{Var}(\epsilon)$ and $\Delta t$.

---

**Exercise 4.** Explain why the mean-reversion speed $\kappa$ is poorly identified from short time series. If a 2-year daily sample gives $\hat{\kappa}^{\mathbb{P}} = 0.05$ with standard error 0.04, what does this imply about the reliability of $\hat{\kappa}$?

---

**Exercise 5.** A cap volatility calibration requires matching the Vasicek implied cap volatility $\sigma_{\text{cap}}$ to the market Black volatility. Since the Vasicek cap price depends only on $\sigma$ (with $\kappa$ and $\theta$ fixed from the yield curve), this is a one-dimensional root-finding problem. Describe the procedure using Newton's method and the cap vega.

---

**Exercise 6.** The calibrated model has residual yield errors of $\{+2, -4, +2, +2, +3\}$ basis points across maturities $\{1, 2, 5, 10, 30\}$Y. Is this pattern random or systematic? What does a systematic pattern tell you about the model's yield curve shape limitations?

---

**Exercise 7.** Distinguish physical measure parameters $(\kappa^{\mathbb{P}}, \theta^{\mathbb{P}}, \sigma)$ from risk-neutral parameters $(\kappa, \theta, \sigma)$. If historical estimation gives $\kappa^{\mathbb{P}} = 0.10$, $\theta^{\mathbb{P}} = 0.04$, and market calibration gives $\kappa = 0.25$, $\theta = 0.0455$, compute the market price of risk $\lambda$ using $\kappa = \kappa^{\mathbb{P}} + \lambda$.
