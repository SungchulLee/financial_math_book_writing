# Calibration Pipeline Guide

Calibrating the Hull-White model requires two distinct steps: fitting the time-dependent drift $\theta(t)$ to the market yield curve (exact by construction), and then fitting the constant parameters $\sigma$ and $\lambda$ to derivative prices (caps, swaptions, or both). This guide describes the calibration pipeline implemented in the companion `calibration_pipeline.py`, explaining how the steps are sequenced, what objective functions are used, and how to assess the quality of the calibrated model.

!!! info "Prerequisites"
    - [Hull-White Model Class Guide](hull_white_model_class.md) (model class and $\theta$ computation)
    - [Bond and Derivative Pricing Classes Guide](bond_derivative_pricing_classes.md) (caplet and swaption formulas)
    - [Named Functions Implementation Guide](named_functions_implementation.md) ($A$, $B$, $\theta$ numerical details)

!!! abstract "Learning Objectives"
    By the end of this guide, you will be able to:

    1. Describe the two-stage calibration procedure (yield curve, then volatility instruments)
    2. Implement the cap-based objective function for $(\sigma, \lambda)$ calibration
    3. Implement the swaption-based objective function
    4. Run the optimizer and interpret the calibrated parameters
    5. Validate the calibration via repricing and stability checks

---

## Pipeline Overview

The calibration proceeds in three stages:

1. **Market data input**: Yield curve (discount factors or zero rates), cap implied volatilities, swaption implied volatilities
2. **Yield curve fit**: Compute $\theta(t)$ from the market curve --- this is automatic (no optimization) once $\sigma$ and $\lambda$ are given
3. **Volatility calibration**: Find $(\sigma, \lambda)$ minimizing the distance between model and market derivative prices

```python
class CalibrationPipeline:
    def __init__(self, market_curve, cap_vols=None, swaption_vols=None):
        self.P = market_curve       # callable: P^M(0, T)
        self.cap_vols = cap_vols    # dict: {maturity: implied_vol}
        self.swn_vols = swaption_vols  # dict: {(expiry, tenor): implied_vol}
```

---

## Stage 1: Market Curve

The market discount curve $P^M(0, T)$ is provided as a callable. Common sources:

- **Bootstrapped curve**: From deposit rates, futures, and swap rates
- **Parametric fit**: Nelson-Siegel or Svensson parameterization
- **Spline interpolation**: Cubic spline through market discount factors

The pipeline does not perform bootstrapping itself --- it takes the curve as input and uses it to compute $\theta(t)$ via numerical differentiation of $\ln P^M(0, t)$.

---

## Stage 2: Cap Volatility Calibration

### Objective function

Given trial parameters $(\sigma, \lambda)$, the pipeline:

1. Constructs a `HullWhite(sigma, lambd, P)` model instance
2. Prices each ATM caplet using the closed-form formula
3. Sums caplet prices to get cap prices
4. Inverts Black's formula to get model cap implied volatilities
5. Computes the weighted sum of squared errors:

$$
f(\sigma, \lambda) = \sum_{j=1}^{M} w_j\left[\sigma^{\text{model}}_j(\sigma, \lambda) - \sigma^{\text{mkt}}_j\right]^2
$$

### Implementation

```python
def _cap_objective(self, params):
    sigma, lambd = params
    hw = HullWhite(sigma, lambd, self.P)
    pricer = BondPricer(hw)
    total_error = 0.0
    for maturity, mkt_vol in self.cap_vols.items():
        model_price = pricer.cap(self._reset_dates(maturity), self.delta, self.atm_strike, self.r0)
        model_vol = self._invert_black_cap(model_price, maturity)
        total_error += (model_vol - mkt_vol) ** 2
    return total_error
```

### Optimizer

The default optimizer is `scipy.optimize.minimize` with the Nelder-Mead method (derivative-free, robust to the noisy landscape). For better convergence, Levenberg-Marquardt via `scipy.optimize.least_squares` can be used when Jacobian information is available.

```python
def calibrate_to_caps(self, sigma0=0.01, lambd0=0.05):
    result = minimize(self._cap_objective, [sigma0, lambd0],
                      method='Nelder-Mead', options={'xatol': 1e-6, 'fatol': 1e-10})
    self.sigma_cal, self.lambd_cal = result.x
    return result
```

---

## Stage 3: Swaption Calibration

### Objective function

For swaption calibration, the objective uses the Jamshidian swaption formula:

$$
g(\sigma, \lambda) = \sum_{(T_0, T_n)} w_{T_0, T_n}\left[\sigma^{\text{swn,model}}_{T_0, T_n} - \sigma^{\text{swn,mkt}}_{T_0, T_n}\right]^2
$$

### Joint calibration

When both cap and swaption data are available, the joint objective is a weighted combination:

$$
h(\sigma, \lambda) = \alpha\,f(\sigma, \lambda) + (1 - \alpha)\,g(\sigma, \lambda)
$$

where $\alpha \in [0, 1]$ controls the relative importance. Typical choices: $\alpha = 0.5$ for equal weight, $\alpha = 1$ for cap-only, $\alpha = 0$ for swaption-only.

!!! warning "One-Factor Limitations"
    The one-factor Hull-White model cannot simultaneously fit the full swaption matrix. If the cap fit is good, off-diagonal swaptions (short expiry, long tenor) will typically show errors of 20--60 bps. Joint calibration compromises on both. Two-factor models (see [Two-Factor Model](../two_factor/two_factor_model_definition.md)) resolve this.

---

## Validation

### Repricing check

After calibration, reprice all calibration instruments and report errors:

```python
def validate(self):
    hw = HullWhite(self.sigma_cal, self.lambd_cal, self.P)
    pricer = BondPricer(hw)
    for maturity, mkt_vol in self.cap_vols.items():
        model_vol = ...
        print(f"Cap {maturity}Y: mkt={mkt_vol:.2%} model={model_vol:.2%} err={model_vol-mkt_vol:.2%}")
```

### Parameter sensitivity

Compute the Hessian of the objective at the optimum to assess parameter uncertainty:

$$
\text{Var}(\hat{\theta}) \approx H^{-1} \cdot \hat{\sigma}_{\text{res}}^2
$$

A flat Hessian eigenvalue indicates a poorly identified parameter (typically the $\sigma$-$\lambda$ ridge).

### Cross-validation

Calibrate to a subset of instruments and test on the held-out instruments to detect overfitting.

---

## Summary

| Stage | Input | Output | Method |
|-------|-------|--------|--------|
| Market curve | Discount factors | $P^M(0, T)$ callable | Interpolation / parametric fit |
| $\theta(t)$ | $P^M$, $\sigma$, $\lambda$ | Time-dependent drift | Automatic (numerical differentiation) |
| Cap calibration | Cap implied vols | $\hat{\sigma}$, $\hat{\lambda}$ | Nelder-Mead / LM optimization |
| Swaption calibration | Swaption implied vols | $\hat{\sigma}$, $\hat{\lambda}$ | Same, different objective |
| Validation | Calibrated model | Repricing errors | Analytical repricing |

For the end-to-end workflow combining all stages with market data, see [End-to-End Worked Examples Guide](end_to_end_worked_examples.md).

---

## Exercises

**Exercise 1.** The calibration pipeline computes $\theta(t)$ from the market curve $P^M(0, T)$ using numerical differentiation of $\ln P^M(0, t)$. For a flat curve at rate $r$, show analytically that $\theta(t) = r + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})$. Verify this by plugging $P^M(0, t) = e^{-rt}$ into the numerical formula and comparing with the analytical result for $\sigma = 0.01$, $\lambda = 0.05$, $r = 0.03$.

??? success "Solution to Exercise 1"
    For a flat curve $P^M(0, t) = e^{-rt}$, the instantaneous forward rate is:

    $$
    f(0, t) = -\frac{\partial}{\partial t}\ln P^M(0, t) = -\frac{\partial}{\partial t}(-rt) = r
    $$

    The derivative is $\frac{\partial f}{\partial t}(0, t) = 0$. Substituting into the $\theta(t)$ formula:

    $$
    \theta(t) = r + \frac{0}{\lambda} + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t}) = r + \frac{\sigma^2}{2\lambda^2}(1 - e^{-2\lambda t})
    $$

    With $r = 0.03$, $\sigma = 0.01$, $\lambda = 0.05$:

    $$
    \theta(t) = 0.03 + \frac{(0.01)^2}{2(0.05)^2}(1 - e^{-0.1t}) = 0.03 + 0.02(1 - e^{-0.1t})
    $$

    The numerical formula uses central differences to compute $f(0, t)$ and $\partial f/\partial t$ from $P^M$. For the flat curve:

    $$
    f_{\text{num}}(0, t) = -\frac{\ln e^{-r(t+dt)} - \ln e^{-r(t-dt)}}{2\,dt} = -\frac{-r(t+dt) + r(t-dt)}{2\,dt} = r
    $$

    This is exact (no truncation error) because $\ln P^M$ is linear in $t$. Similarly, $\partial f/\partial t$ computed by finite differences of $f$ gives exactly zero. Therefore, the numerical $\theta(t)$ matches the analytical formula to machine precision.

    Sample values:

    - $\theta(0) = 0.03 + 0 = 0.03$
    - $\theta(1) = 0.03 + 0.02(1 - e^{-0.1}) = 0.03 + 0.02 \times 0.09516 = 0.03190$
    - $\theta(5) = 0.03 + 0.02(1 - e^{-0.5}) = 0.03 + 0.02 \times 0.39347 = 0.03787$
    - $\theta(10) = 0.03 + 0.02(1 - e^{-1.0}) = 0.03 + 0.02 \times 0.63212 = 0.04264$

---

**Exercise 2.** Explain why the cap volatility objective function uses implied volatility errors rather than price errors:

$$
f(\sigma, \lambda) = \sum_j w_j\left[\sigma_j^{\text{model}} - \sigma_j^{\text{mkt}}\right]^2
$$

What problems might arise from minimizing price errors instead? How should the weights $w_j$ be chosen?

??? success "Solution to Exercise 2"
    **Why implied volatility errors are preferred over price errors:**

    1. **Scale invariance:** Cap prices vary enormously across maturities (a 1Y cap costs much less than a 10Y cap in absolute terms). Minimizing price errors would overweight long-dated caps simply because they have larger prices, regardless of the fit quality. Implied volatility errors are dimensionless and comparable across maturities.

    2. **Market convention:** Caps are quoted in implied volatility, so fitting in vol space corresponds to matching the quantities traders actually observe and hedge against.

    3. **Numerical conditioning:** The mapping from $(\sigma, \lambda)$ to cap prices is highly nonlinear, with prices spanning several orders of magnitude. The mapping to implied volatilities is more nearly linear, giving a better-conditioned optimization landscape.

    **Problems with price errors:** If the objective minimizes $\sum_j (P_j^{\text{model}} - P_j^{\text{mkt}})^2$, a single long-dated cap with a large absolute price can dominate the fit, causing poor calibration to short-dated caps that may be more liquid and important for hedging.

    **Weight selection:** The weights $w_j$ should reflect:

    - **Liquidity:** More liquid instruments (typically 2Y--5Y caps) should receive higher weight because their market quotes are more reliable.
    - **Vega normalization:** Setting $w_j = 1/\text{vega}_j^2$ normalizes each instrument's contribution so that a 1 bp implied vol error contributes equally regardless of maturity.
    - **Hedging importance:** If the portfolio being hedged has specific maturity exposures, upweight those maturities.

---

**Exercise 3.** The one-factor Hull-White model has only two free parameters $(\sigma, \lambda)$ for fitting cap volatilities across many maturities. Explain the $\sigma$-$\lambda$ tradeoff: if $\sigma$ increases while $\lambda$ is adjusted appropriately, what happens to short-maturity caplet prices versus long-maturity caplet prices? Why does this create a ridge in the objective function landscape?

??? success "Solution to Exercise 3"
    The Hull-White model generates caplet volatilities through the bond price volatility:

    $$
    \sigma_{P,i} = \frac{\sigma}{\lambda}(1 - e^{-\lambda\delta})\sqrt{\frac{1 - e^{-2\lambda T_i}}{2\lambda}}
    $$

    **The $\sigma$-$\lambda$ tradeoff:**

    - **Short-maturity caplets** ($T_i$ small): The factor $\sqrt{(1 - e^{-2\lambda T_i})/(2\lambda)} \approx \sqrt{T_i}$ is approximately independent of $\lambda$. The caplet volatility is roughly $\sigma_{P,i} \propto \sigma \cdot (1 - e^{-\lambda\delta})/\lambda \approx \sigma\delta$ for small $\lambda\delta$. Short-maturity caplets are primarily sensitive to $\sigma$.

    - **Long-maturity caplets** ($T_i$ large): The factor saturates at $\sqrt{1/(2\lambda)}$. The caplet volatility behaves as $\sigma_{P,i} \propto \sigma/\lambda^{3/2}$. Long-maturity caplets are sensitive to the ratio $\sigma/\lambda^{3/2}$.

    If $\sigma$ increases and $\lambda$ increases proportionally to keep $\sigma/\lambda^{3/2}$ constant, then long-maturity caplet prices are approximately unchanged but short-maturity caplet prices increase (because the $\sigma$ sensitivity dominates for small $T_i$).

    **Why this creates a ridge:** The two parameters are partially redundant: many $(\sigma, \lambda)$ combinations produce similar long-maturity cap prices. The objective function contours form an elongated valley (ridge) in the $(\sigma, \lambda)$ plane. Moving along the ridge changes neither the objective function value significantly nor the model's overall fit, making the optimization ill-conditioned. The Hessian of the objective has one large eigenvalue (perpendicular to the ridge) and one small eigenvalue (along the ridge).

---

**Exercise 4.** Describe the three-stage calibration pipeline (market curve, theta fit, volatility calibration) and explain why the stages must be performed in this specific order. What would happen if you attempted to calibrate $(\sigma, \lambda)$ before computing $\theta(t)$?

??? success "Solution to Exercise 4"
    **Three-stage pipeline:**

    1. **Market curve:** Obtain the discount curve $P^M(0, T)$ from market data (bootstrapping, interpolation, or parametric fit).
    2. **Theta fit:** Given trial $(\sigma, \lambda)$ and the market curve, compute $\theta(t)$ via numerical differentiation of $\ln P^M(0, t)$. This is automatic --- $\theta$ is uniquely determined by $(\sigma, \lambda, P^M)$.
    3. **Volatility calibration:** Search over $(\sigma, \lambda)$ to minimize the distance between model and market derivative prices (caps or swaptions).

    **Why this order is mandatory:**

    - $\theta(t)$ depends on $(\sigma, \lambda)$ and $P^M$, so the market curve must be available first.
    - Derivative prices depend on $\theta(t)$ (through the bond price formula $P = e^{A + Br}$ where $A$ involves $\theta$). If $\theta$ is not computed before pricing, the model bond prices will not match the market curve, and all derivative prices will be inconsistent.

    **If you calibrate $(\sigma, \lambda)$ before computing $\theta(t)$:** The bond prices generated by the model would be arbitrary (not matching the market curve), so the caplet and swaption prices would be meaningless. The optimizer would try to fit derivative prices with a model that cannot even reproduce the yield curve, leading to nonsensical parameter estimates. The $\theta(t)$ calibration is what ensures arbitrage-free consistency between the model and the observed yield curve.

---

**Exercise 5.** After calibrating to cap implied volatilities, the validation step reveals that the 3Y cap has a repricing error of 25 bps. Propose three possible causes and describe how you would diagnose each: (a) a numerical issue, (b) a model limitation, (c) a market data issue.

??? success "Solution to Exercise 5"
    A 25 bps repricing error on the 3Y cap could stem from:

    **(a) Numerical issue:** The trapezoidal integration in $A(\tau)$ may have insufficient grid points for the 3Y maturity range, or the numerical differentiation step $dt$ may be poorly chosen for the specific curve shape around $t = 3$.

    - **Diagnosis:** Increase the number of quadrature points from 250 to 1000 and decrease the differentiation step to $10^{-5}$. If the repricing error shrinks, it was a numerical resolution issue. Also run the bond price recovery test $P^{\text{HW}}(0, 3) = P^M(0, 3)$ to check that the named functions are computed correctly.

    **(b) Model limitation:** The one-factor Hull-White model with constant $(\sigma, \lambda)$ cannot simultaneously match all cap maturities when the market cap volatility term structure is non-monotone (humped). The 3Y cap may sit at the hump where the model struggles most.

    - **Diagnosis:** Plot the model vs. market implied volatility term structure. If the model curve is systematically above or below the market at 3Y while fitting well at other maturities, the constant-parameter model lacks the flexibility to match the hump. Try piecewise-constant $\sigma(t)$ and see if the 3Y error disappears.

    **(c) Market data issue:** The 3Y cap implied volatility may be stale, interpolated from sparse quotes, or contaminated by a bid-ask bounce.

    - **Diagnosis:** Check the timestamp and source of the 3Y quote. Compare with 2.5Y and 3.5Y quotes (if available) for consistency. Verify against a second data provider. If the 3Y quote is an outlier relative to neighboring maturities, flag it as suspect and consider excluding it or reducing its weight in the objective function.

---

**Exercise 6.** In joint calibration with weight $\alpha$:

$$
h(\sigma, \lambda) = \alpha\,f(\sigma, \lambda) + (1 - \alpha)\,g(\sigma, \lambda)
$$

explain why $\alpha = 0.5$ does not necessarily give equal importance to caps and swaptions. What determines the effective relative importance? How would you modify the weighting to ensure that a 1 bp repricing error in caps is penalized equally to a 1 bp error in swaptions?

??? success "Solution to Exercise 6"
    The joint objective is:

    $$
    h(\sigma, \lambda) = \alpha\,f(\sigma, \lambda) + (1 - \alpha)\,g(\sigma, \lambda)
    $$

    Setting $\alpha = 0.5$ gives equal *weight* to the two objective functions, but not necessarily equal *importance*. The effective importance depends on:

    1. **Number of instruments:** If there are 6 cap maturities and 15 swaption expiry-tenor pairs, the swaption objective $g$ involves more terms, so each individual swaption's influence is diluted compared to each cap's influence.

    2. **Magnitude of errors:** If cap implied volatilities are around 15--20% and swaption implied volatilities are around 10--15%, a 1 bp error in cap vol contributes differently to $f$ than a 1 bp error in swaption vol contributes to $g$ (because the errors are squared).

    3. **Sensitivity to parameters:** If swaption prices are more sensitive to $\lambda$ than cap prices, the swaption objective will pull $\lambda$ more strongly, regardless of $\alpha$.

    **Ensuring equal penalization of 1 bp errors:** Normalize each objective by the number of instruments:

    $$
    h(\sigma, \lambda) = \alpha \cdot \frac{1}{M_{\text{cap}}}\sum_{j=1}^{M_{\text{cap}}} (\sigma_j^{\text{cap,model}} - \sigma_j^{\text{cap,mkt}})^2 + (1 - \alpha) \cdot \frac{1}{M_{\text{swn}}}\sum_{k=1}^{M_{\text{swn}}} (\sigma_k^{\text{swn,model}} - \sigma_k^{\text{swn,mkt}})^2
    $$

    With this per-instrument normalization and $\alpha = 0.5$, a 1 bp error in any single cap vol is penalized equally to a 1 bp error in any single swaption vol.

---

**Exercise 7.** Describe how you would assess parameter stability by calibrating to market data on five consecutive business days. What metrics would you compute? If $\hat{\sigma}$ varies by 30\% across the five days while $\hat{\lambda}$ varies by 200\%, what does this suggest about the identifiability of the parameters?

??? success "Solution to Exercise 7"
    **Stability assessment procedure:**

    1. Calibrate the model to market data on each of the five consecutive business days $d_1, \ldots, d_5$, obtaining $(\hat{\sigma}^{(d)}, \hat{\lambda}^{(d)})$ for each day.
    2. Compute the following metrics:

    **Metrics:**

    - **Mean and standard deviation** of each parameter across the five days: $\bar{\sigma}, s_\sigma, \bar{\lambda}, s_\lambda$.
    - **Coefficient of variation** (CV): $\text{CV}_\sigma = s_\sigma / \bar{\sigma}$ and $\text{CV}_\lambda = s_\lambda / \bar{\lambda}$.
    - **Day-to-day changes**: $\Delta\hat{\sigma}^{(d)} = \hat{\sigma}^{(d+1)} - \hat{\sigma}^{(d)}$ and similarly for $\lambda$.
    - **Repricing errors**: For each day's calibration, compute the root-mean-square repricing error across all instruments.
    - **Parameter correlation**: Compute $\text{Corr}(\hat{\sigma}, \hat{\lambda})$ across the five days (a high negative correlation indicates a ridge).

    **Interpretation of 30% variation in $\hat{\sigma}$ and 200% in $\hat{\lambda}$:**

    - $\hat{\lambda}$ is poorly identified: its estimates are unreliable and dominated by noise in the market data. The 200% variation means that $\hat{\lambda}$ could plausibly take almost any value in its range.
    - $\hat{\sigma}$ is moderately identified: 30% day-to-day variation is still large for a "constant" parameter, suggesting that $\sigma$ also has some identification problems, though less severe.
    - The likely explanation is the $\sigma$-$\lambda$ ridge: the objective function has a shallow valley, and small changes in market data shift the minimum along the ridge, causing large swings in $\hat{\lambda}$ with correlated (but smaller) changes in $\hat{\sigma}$.
    - **Remedies:** (i) Fix $\lambda$ to a reasonable value (e.g., from historical estimation) and calibrate $\sigma$ only. (ii) Add a regularization penalty $\mu(\lambda - \lambda_0)^2$ to the objective. (iii) Use a time series of calibrations to compute a smoothed $\hat{\lambda}$ with a Kalman filter.
