# Calibration of the CIR Model

A short-rate model is only useful if its parameters can be determined from observable market data. The CIR model has three risk-neutral parameters --- $\kappa$, $\theta$, $\sigma$ --- plus the current short rate $r_0$, and calibration means choosing these values so that model prices match market prices as closely as possible. Two fundamentally different approaches exist: **cross-sectional calibration** fits the yield curve or option prices at a single date, while **time-series calibration** (maximum likelihood estimation) uses historical rate observations. This section develops both approaches, analyzes their strengths and limitations, and discusses the practical challenges of CIR calibration.

---

## Cross-sectional calibration to the yield curve

### Objective function

Given observed zero-coupon bond prices $P^{\text{mkt}}(0, T_j)$ for maturities $T_1, \ldots, T_J$, find parameters $(\kappa, \theta, \sigma, r_0)$ minimizing the sum of squared pricing errors:

$$
\min_{\kappa,\,\theta,\,\sigma,\,r_0}\;\sum_{j=1}^{J}\left(P^{\text{CIR}}(0, T_j;\,\kappa,\theta,\sigma,r_0) - P^{\text{mkt}}(0, T_j)\right)^2
$$

Alternatively, calibrate in yield space:

$$
\min_{\kappa,\,\theta,\,\sigma,\,r_0}\;\sum_{j=1}^{J}\left(R^{\text{CIR}}(0, T_j) - R^{\text{mkt}}(0, T_j)\right)^2
$$

where $R(0,T_j) = -\ln P(0,T_j)/T_j$. Yield-space calibration weights short and long maturities more evenly, since bond prices are close to 1 for short maturities and close to 0 for very long maturities.

### Parameter constraints

The optimization must enforce:

- $\kappa > 0$ (mean reversion)
- $\theta > 0$ (positive long-run mean)
- $\sigma > 0$ (positive volatility)
- $r_0 > 0$ (positive initial rate)
- Feller condition: $2\kappa\theta \geq \sigma^2$ (optional but recommended)

!!! warning "CIR cannot fit an arbitrary yield curve"
    With only four parameters, the CIR model generates yield curves from a four-dimensional family. Real yield curves have far more degrees of freedom, so the fit will always be approximate. The residual errors are systematic, not random --- they reflect the model's structural limitations. For exact term structure fitting, time-dependent extensions (CIR++) or the Hull-White model are needed.

### Optimization algorithm

The objective function is nonlinear and potentially multimodal. A practical approach combines:

1. **Grid search** over a coarse parameter grid to find a good starting point
2. **Gradient-based optimizer** (e.g., L-BFGS-B with box constraints) to refine

The gradients $\partial P^{\text{CIR}}/\partial \kappa$, $\partial P^{\text{CIR}}/\partial \theta$, $\partial P^{\text{CIR}}/\partial \sigma$ can be computed analytically from the closed-form bond price formula, which significantly improves convergence compared to finite differences.

---

## Calibration to cap volatilities

### From market quotes to model prices

Interest rate caps are quoted in terms of implied (Black) volatilities. The calibration target is to match these quotes:

$$
\min_{\kappa,\,\theta,\,\sigma,\,r_0}\;\sum_{i=1}^{I}w_i\left(\sigma_{\text{Black},i}^{\text{CIR}}(\kappa,\theta,\sigma,r_0) - \sigma_{\text{Black},i}^{\text{mkt}}\right)^2
$$

where $w_i$ are weights (often inversely proportional to the bid-ask spread) and $\sigma_{\text{Black},i}^{\text{CIR}}$ is the Black implied volatility backed out from the CIR cap price.

### Procedure

For each parameter trial $(\kappa, \theta, \sigma, r_0)$:

1. Compute CIR caplet prices using the bond-put equivalence and the non-central chi-squared formula
2. Sum caplets to get cap prices
3. Invert the Black (1976) formula to extract implied volatilities
4. Compare to market implied volatilities

The inner loop (Black inversion) requires a root-finding step, making the overall calibration computationally intensive. Pre-computing a table of Black prices versus implied volatilities can speed this up.

---

## Joint calibration to yield curve and caps

In practice, calibrating to both the yield curve and cap volatilities simultaneously produces the most informative parameter set:

$$
\min_{\kappa,\,\theta,\,\sigma,\,r_0}\;\alpha\sum_{j=1}^{J}\left(R_j^{\text{CIR}} - R_j^{\text{mkt}}\right)^2 + (1-\alpha)\sum_{i=1}^{I}w_i\left(\sigma_{\text{Black},i}^{\text{CIR}} - \sigma_{\text{Black},i}^{\text{mkt}}\right)^2
$$

The mixing parameter $\alpha \in [0,1]$ balances term structure fit versus volatility fit. Typical choices are $\alpha = 0.5$ (equal weight) or values determined by the relative magnitudes of the two error terms.

---

## Maximum likelihood estimation

### Setup

Given a time series of observed short rates $r_{t_0}, r_{t_1}, \ldots, r_{t_n}$ at equally spaced times $t_k = k\Delta t$, the log-likelihood function is

$$
\ell(\kappa, \theta, \sigma) = \sum_{k=0}^{n-1}\ln p(r_{t_{k+1}}\,|\,r_{t_k};\,\kappa,\theta,\sigma)
$$

where $p(r_{t_{k+1}} | r_{t_k})$ is the CIR transition density, which is a scaled non-central chi-squared density.

### Transition density

The density of $r_{t+\Delta t}$ given $r_t$ is

$$
p(r_{t+\Delta t}\,|\,r_t) = c_e\,f_{\chi^2(d,\lambda)}(c_e\,r_{t+\Delta t})
$$

where $f_{\chi^2(d,\lambda)}$ is the non-central chi-squared PDF and

$$
c_e = \frac{4\kappa}{\sigma^2(1 - e^{-\kappa\Delta t})}, \qquad d = \frac{4\kappa\theta}{\sigma^2}, \qquad \lambda = c_e\,r_t\,e^{-\kappa\Delta t}
$$

The log-likelihood of a single observation is

$$
\ln p(r_{t+\Delta t}\,|\,r_t) = \ln c_e + \ln f_{\chi^2(d,\lambda)}(c_e\,r_{t+\Delta t})
$$

### MLE procedure

1. Choose initial parameter guesses $(\kappa_0, \theta_0, \sigma_0)$
2. For each trial $(\kappa, \theta, \sigma)$, compute the total log-likelihood $\ell(\kappa, \theta, \sigma)$
3. Maximize $\ell$ using a numerical optimizer (e.g., Nelder-Mead or L-BFGS-B)

The MLE estimates physical (real-world) parameters $(\kappa^{\mathbb{P}}, \theta^{\mathbb{P}}, \sigma)$. Risk-neutral parameters for pricing require an additional specification of the market price of risk.

!!! note "Physical vs risk-neutral parameters"
    MLE from historical data estimates the physical parameters. Cross-sectional calibration to market prices estimates risk-neutral parameters. The two sets are related by $\kappa = \kappa^{\mathbb{P}} + \lambda_0$ and $\theta = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/\kappa$, where $\lambda_0$ is the market price of risk parameter. Estimating $\lambda_0$ requires both time-series and cross-sectional data.

---

## Identifiability issues

### Parameter correlation

The parameters $\kappa$ and $\theta$ are highly correlated in the yield curve: different $(\kappa, \theta)$ combinations can produce similar long rates $R_\infty = 2\kappa\theta/(\gamma + \kappa)$. This makes the optimization landscape elongated along a ridge, slowing convergence and creating sensitivity to initial conditions.

### Under-determination

With only four parameters, the CIR model is over-determined when calibrating to a full yield curve (10+ points) but may be under-determined when fitting to only a few cap prices. Adding the Feller condition as a constraint reduces the feasible set and can help regularize the problem.

### Practical recommendations

1. **Start from economically reasonable values**: $\kappa \in [0.1, 2.0]$, $\theta \in [0.01, 0.10]$, $\sigma \in [0.01, 0.30]$
2. **Use multiple starting points**: Run the optimizer from 5--10 random initial conditions
3. **Check the Feller condition**: Verify $2\kappa\theta/\sigma^2$ after calibration
4. **Examine residuals**: Systematic patterns in the residuals indicate model misspecification

---

## Numerical example

Calibrate CIR to five market zero rates: $R^{\text{mkt}}(0, T_j)$ for $T_j \in \{1, 2, 5, 10, 30\}$ years with values $\{3.5\%, 3.8\%, 4.2\%, 4.5\%, 4.7\%\}$.

**Calibrated parameters**: $\kappa = 0.48$, $\theta = 0.062$, $\sigma = 0.095$, $r_0 = 0.032$.

**Feller ratio**: $2\kappa\theta/\sigma^2 = 2(0.48)(0.062)/(0.095)^2 \approx 6.59 > 1$ $\checkmark$

**Long rate**: $\gamma = \sqrt{0.48^2 + 2(0.095)^2} \approx 0.498$, $R_\infty = 2(0.48)(0.062)/(0.498 + 0.48) \approx 6.08\%$

| Maturity | $R^{\text{mkt}}$ | $R^{\text{CIR}}$ | Error (bp) |
|:--------:|:-----------------:|:-----------------:|:----------:|
| 1y | 3.50% | 3.52% | +2 |
| 2y | 3.80% | 3.78% | -2 |
| 5y | 4.20% | 4.18% | -2 |
| 10y | 4.50% | 4.53% | +3 |
| 30y | 4.70% | 4.68% | -2 |

The fit is within 3 basis points across all maturities, which is typical for a three-parameter model against a smooth yield curve.

---

## Summary

CIR calibration proceeds through cross-sectional fitting (to yield curves and/or cap volatilities) or time-series estimation (MLE using the non-central chi-squared transition density). Cross-sectional calibration determines risk-neutral parameters for pricing, while MLE recovers physical parameters for risk measurement. The main challenges are the limited flexibility of the three-parameter family (which cannot perfectly fit arbitrary term structures), parameter correlation between $\kappa$ and $\theta$, and the distinction between physical and risk-neutral parameter sets. Joint calibration to both yield curves and options provides the most robust parameter estimates, and multiple starting points are essential to avoid local optima.

---

## Exercises

**Exercise 1.** Given market zero rates $R^{\text{mkt}}(0, T_j)$ for $T_j \in \{1, 3, 5, 10\}$ years with values $\{2.5\%, 3.0\%, 3.5\%, 4.0\%\}$, write out the yield-space objective function explicitly. How many free parameters does CIR have, and why is the optimization over-determined in this case?

---

**Exercise 2.** Compute the CIR bond price $P^{\text{CIR}}(0, 5)$ for parameters $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.08$, and $r_0 = 0.03$. First compute $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$, then $B(5)$ and $A(5)$, and finally $P(0,5) = A(5)\,e^{-B(5)\,r_0}$.

---

**Exercise 3.** The parameters $\kappa$ and $\theta$ are highly correlated in yield curve fitting. Show that the long rate $R_\infty = 2\kappa\theta/(\gamma + \kappa)$ depends on the product $\kappa\theta$ more strongly than on each parameter individually by computing $\partial R_\infty / \partial \kappa$ and $\partial R_\infty / \partial \theta$. Give two different $(\kappa, \theta)$ pairs that produce approximately the same $R_\infty$ with $\sigma = 0.10$.

---

**Exercise 4.** For MLE calibration, the transition density involves the non-central chi-squared distribution with parameters $c_e$, $d$, and $\lambda$. Given $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.10$, $\Delta t = 1/252$ (daily), and $r_t = 0.05$, compute $c_e$, $d$, and $\lambda$. What is the expected value of $r_{t+\Delta t}$ under this density?

---

**Exercise 5.** Explain the distinction between physical parameters $(\kappa^{\mathbb{P}}, \theta^{\mathbb{P}}, \sigma)$ estimated from historical data and risk-neutral parameters $(\kappa, \theta, \sigma)$ calibrated from market prices. If MLE gives $\kappa^{\mathbb{P}} = 0.3$ and $\theta^{\mathbb{P}} = 0.05$, and cross-sectional calibration gives $\kappa = 0.5$ and $\theta = 0.06$, what is the implied market price of risk parameter $\lambda_0$?

---

**Exercise 6.** In the joint calibration objective

$$
\alpha\sum_{j}\left(R_j^{\text{CIR}} - R_j^{\text{mkt}}\right)^2 + (1-\alpha)\sum_{i}w_i\left(\sigma_{\text{Black},i}^{\text{CIR}} - \sigma_{\text{Black},i}^{\text{mkt}}\right)^2
$$

explain why the mixing parameter $\alpha$ matters. If yield errors are on the order of $10^{-4}$ (in decimal) and volatility errors are on the order of $10^{-2}$, what value of $\alpha$ would approximately equalize the two terms?

---

**Exercise 7.** After calibrating to the five-maturity yield curve in the numerical example, the residuals show a pattern: positive at 1Y, negative at 2Y and 5Y, positive at 10Y, and negative at 30Y. Discuss what this systematic pattern reveals about the CIR model's yield curve shape limitations. What structural feature of a real yield curve might CIR be unable to capture with its three parameters?
