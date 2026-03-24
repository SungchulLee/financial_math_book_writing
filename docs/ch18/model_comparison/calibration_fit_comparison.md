# Calibration Fit Comparison

All one-factor short-rate models with time-dependent drift --- Vasicek, CIR, Hull-White, and Black-Karasinski --- can fit the initial yield curve exactly by construction. The real test is how well they reproduce the prices of interest rate derivatives, particularly caps, floors, and swaptions, which depend on the volatility structure. This section compares the calibration quality of these four models against market cap volatilities and swaption volatilities, using consistent data and methodology to isolate the effect of model choice from calibration technique.

!!! info "Prerequisites"
    - [Vasicek vs CIR vs Hull-White](vasicek_vs_cir_vs_hull_white.md) (structural differences)
    - [Analytical Tractability](analytical_tractability.md) (computational methods available to each model)
    - [Calibration to Cap Volatilities](../black_karasinski/calibration_to_cap_volatilities.md) (BK calibration details)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Define standard calibration error metrics (RMSE, MAE, max error) for implied volatilities
    2. Compare cap volatility fits across Vasicek, CIR, Hull-White, and Black-Karasinski
    3. Compare swaption volatility matrix fits across the four models
    4. Assess parameter stability by examining calibration results on different dates
    5. Identify systematic biases in each model's fit

---

## Calibration Setup

### Common inputs

All models are calibrated to the same market data:

- **Yield curve**: Bootstrapped from deposit rates, futures, and swaps (e.g., USD SOFR curve)
- **Cap volatilities**: ATM cap implied volatilities for maturities 1Y through 10Y
- **Swaption volatilities**: ATM swaption implied volatilities on a grid of option expiries (1Y--10Y) and swap tenors (1Y--10Y)

### Model parameters

Each model has a small number of free parameters after the yield-curve-fitting drift $\theta(t)$ is determined:

| Model | Free parameters | Calibration method |
|-------|----------------|-------------------|
| Vasicek | $a$, $\sigma$ | Analytical cap formula, least squares |
| CIR | $a$, $b$, $\sigma$ | Semi-analytical, least squares |
| Hull-White | $a$, $\sigma$ (or $\sigma(t)$) | Analytical cap formula, least squares |
| Black-Karasinski | $a$, $\sigma$ (or $\sigma(t)$) | Tree-based, numerical optimization |

### Error metrics

For $M$ market instruments with implied volatilities $\sigma^{\text{mkt}}_j$:

$$
\text{RMSE} = \sqrt{\frac{1}{M}\sum_{j=1}^M (\sigma^{\text{model}}_j - \sigma^{\text{mkt}}_j)^2}
$$

$$
\text{MAE} = \frac{1}{M}\sum_{j=1}^M |\sigma^{\text{model}}_j - \sigma^{\text{mkt}}_j|
$$

$$
\text{MaxErr} = \max_j |\sigma^{\text{model}}_j - \sigma^{\text{mkt}}_j|
$$

---

## Cap Volatility Fit

### Constant volatility ($\sigma$ scalar)

With a single volatility parameter, each model generates a specific term structure shape for cap implied volatilities. The typical pattern:

| Model | Short-end fit | Long-end fit | Systematic bias |
|-------|:------------:|:------------:|----------------|
| Vasicek / Hull-White | Good | Good | Slight over-estimation at intermediate maturities |
| CIR | Moderate | Good | Under-estimates short-end due to $\sqrt{r}$ vol |
| Black-Karasinski | Good | Good | Slight under-estimation at the long end |

!!! example "Typical RMSE (constant $\sigma$, ATM caps)"
    | Model | RMSE (bps) | MAE (bps) | MaxErr (bps) |
    |-------|:----------:|:---------:|:------------:|
    | Vasicek | 15--25 | 12--20 | 30--50 |
    | CIR | 20--35 | 15--28 | 40--60 |
    | Hull-White | 15--25 | 12--20 | 30--50 |
    | Black-Karasinski | 15--30 | 12--25 | 30--55 |

### Piecewise-constant volatility ($\sigma(t)$)

With one volatility level per cap maturity, all models fit ATM cap volatilities to within numerical precision (tree discretization error for BK, machine precision for HW):

| Model | RMSE (bps) | Notes |
|-------|:----------:|-------|
| Hull-White | $< 0.1$ | Analytical bootstrap |
| Black-Karasinski | $< 1.0$ | Limited by tree resolution |

The advantage of BK over HW appears only when fitting **OTM caps** (skew), where the log-normal rate distribution provides a better match to the market smile than the normal distribution of HW.

---

## Swaption Volatility Fit

### The swaption matrix challenge

The swaption volatility matrix (expiry $\times$ tenor) contains far more information than the cap curve. A one-factor model with constant $\sigma$ typically cannot reproduce the full matrix:

- **Correlation structure**: One factor implies perfect correlation between rates at all tenors. Market swaption prices embed imperfect correlations.
- **Volatility hump**: Market swaption volatilities often show a hump shape (peak at 2Y--5Y expiry), which requires time-dependent $\sigma(t)$ to reproduce.

### Fit quality

| Model | ATM swaption RMSE (bps) | Diagonal fit | Off-diagonal fit |
|-------|:-----------------------:|:------------:|:----------------:|
| Hull-White ($\sigma$ const) | 30--60 | Moderate | Poor |
| Hull-White ($\sigma(t)$) | 10--25 | Good | Moderate |
| Black-Karasinski ($\sigma$ const) | 30--60 | Moderate | Poor |
| Black-Karasinski ($\sigma(t)$) | 10--25 | Good | Moderate |

!!! warning "One-Factor Limitation"
    The dominant source of calibration error for swaptions is the one-factor structure, not the choice between normal (HW) and log-normal (BK) rates. Both models produce similar RMSE for ATM swaptions. The rate distribution matters primarily for OTM swaptions (receiver swaptions deep out of the money, where the probability of negative rates differs).

---

## Parameter Stability

### Cross-date stability

A well-behaved model should produce smoothly varying parameters when recalibrated daily to updated market data. Stability is measured by the day-over-day parameter change:

$$
\Delta_k = |\hat{\sigma}_{k} - \hat{\sigma}_{k-1}|
$$

| Model | Median $\Delta_k / \hat{\sigma}$ | Max $\Delta_k / \hat{\sigma}$ |
|-------|:-------------------------------:|:-----------------------------:|
| Hull-White (constant $\sigma$) | 0.5--1% | 3--5% |
| Hull-White ($\sigma(t)$) | 1--3% per bucket | 5--15% per bucket |
| Black-Karasinski (constant $\sigma$) | 0.5--1% | 3--5% |
| Black-Karasinski ($\sigma(t)$) | 2--5% per bucket | 10--25% per bucket |

BK shows higher parameter instability with piecewise-constant $\sigma(t)$ because the tree-based calibration introduces discretization noise that varies with the yield curve level.

### $a$--$\sigma$ correlation

In all models, the mean-reversion speed $a$ and the volatility $\sigma$ are partially correlated: higher $a$ flattens the rate distribution, which can be compensated by higher $\sigma$. This creates a ridge in the objective function landscape, leading to:

- Slow convergence of global optimizers
- Sensitivity to initial guesses
- Instability when both $a$ and $\sigma$ are calibrated jointly

!!! tip "Practical Recommendation"
    Fix $a$ from historical estimation or from swaption calibration, then calibrate $\sigma$ (or $\sigma(t)$) to caps. This eliminates the ridge and stabilizes the calibration.

---

## Summary

| Criterion | Best model |
|-----------|-----------|
| ATM cap fit (constant $\sigma$) | Hull-White $\approx$ BK |
| ATM cap fit ($\sigma(t)$) | Hull-White (analytical bootstrap) |
| OTM cap smile | Black-Karasinski |
| ATM swaption fit | Hull-White $\approx$ BK (one-factor limitation dominates) |
| Parameter stability | Hull-White |
| Calibration speed | Hull-White (100$\times$ faster than BK) |

The overall conclusion: Hull-White dominates for ATM calibration due to speed and stability. Black-Karasinski adds value primarily for OTM products where the log-normal smile is empirically closer to market prices. For a structural comparison of the two models, see [Vasicek vs CIR vs Hull-White](vasicek_vs_cir_vs_hull_white.md). For when to choose which model in practice, see [When to Use Which](when_to_use_which.md).

---

## Exercises

**Exercise 1.** Define the three calibration error metrics (RMSE, MAE, MaxErr) and explain their relative merits. Under what circumstances would you prefer MAE over RMSE? When is MaxErr the most informative metric?

---

**Exercise 2.** A Hull-White model with constant $\sigma$ produces ATM cap volatility RMSE of 20 bps. After switching to piecewise-constant $\sigma(t)$ with one level per cap maturity, the RMSE drops to $< 0.1$ bps. Explain why this dramatic improvement occurs. How many free volatility parameters does the piecewise-constant model have if there are 10 cap maturities?

---

**Exercise 3.** The CIR model with constant parameters shows higher cap volatility RMSE (20--35 bps) than Hull-White (15--25 bps). Identify the structural reason: the CIR cap implied volatility depends on the rate level through $\sqrt{r}$, while Hull-White cap implied volatility is level-independent. How does this affect the fit quality when the current rate is far from $\theta$?

---

**Exercise 4.** Explain why the one-factor structure is the dominant source of swaption calibration error, regardless of whether Hull-White or Black-Karasinski is used. What specific property of the swaption volatility matrix cannot be reproduced by any one-factor model?

---

**Exercise 5.** BK with piecewise-constant $\sigma(t)$ shows higher parameter instability (2--5% daily change per bucket) than HW (1--3%). Explain why tree-based calibration introduces discretization noise that contributes to this instability. How would increasing the number of tree steps affect stability?

---

**Exercise 6.** The $a$--$\sigma$ correlation creates a ridge in the calibration objective function. For Hull-White, sketch the level curves of the cap volatility RMSE in the $(a, \sigma)$ plane and indicate the ridge direction. Explain the practical recommendation to fix $a$ from historical estimation.

---

**Exercise 7.** A portfolio contains both ATM caps and deep OTM receiver swaptions. Based on the summary table, propose a calibration strategy that uses Hull-White for the ATM caps and Black-Karasinski for the OTM swaptions. What challenges arise from using two models for the same portfolio, particularly for hedging and risk aggregation?
