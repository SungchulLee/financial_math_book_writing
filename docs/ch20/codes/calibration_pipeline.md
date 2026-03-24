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

---

**Exercise 2.** Explain why the cap volatility objective function uses implied volatility errors rather than price errors:

$$
f(\sigma, \lambda) = \sum_j w_j\left[\sigma_j^{\text{model}} - \sigma_j^{\text{mkt}}\right]^2
$$

What problems might arise from minimizing price errors instead? How should the weights $w_j$ be chosen?

---

**Exercise 3.** The one-factor Hull-White model has only two free parameters $(\sigma, \lambda)$ for fitting cap volatilities across many maturities. Explain the $\sigma$-$\lambda$ tradeoff: if $\sigma$ increases while $\lambda$ is adjusted appropriately, what happens to short-maturity caplet prices versus long-maturity caplet prices? Why does this create a ridge in the objective function landscape?

---

**Exercise 4.** Describe the three-stage calibration pipeline (market curve, theta fit, volatility calibration) and explain why the stages must be performed in this specific order. What would happen if you attempted to calibrate $(\sigma, \lambda)$ before computing $\theta(t)$?

---

**Exercise 5.** After calibrating to cap implied volatilities, the validation step reveals that the 3Y cap has a repricing error of 25 bps. Propose three possible causes and describe how you would diagnose each: (a) a numerical issue, (b) a model limitation, (c) a market data issue.

---

**Exercise 6.** In joint calibration with weight $\alpha$:

$$
h(\sigma, \lambda) = \alpha\,f(\sigma, \lambda) + (1 - \alpha)\,g(\sigma, \lambda)
$$

explain why $\alpha = 0.5$ does not necessarily give equal importance to caps and swaptions. What determines the effective relative importance? How would you modify the weighting to ensure that a 1 bp repricing error in caps is penalized equally to a 1 bp error in swaptions?

---

**Exercise 7.** Describe how you would assess parameter stability by calibrating to market data on five consecutive business days. What metrics would you compute? If $\hat{\sigma}$ varies by 30\% across the five days while $\hat{\lambda}$ varies by 200\%, what does this suggest about the identifiability of the parameters?
