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

### Constant volatility (σ scalar)

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

### Piecewise-constant volatility (σ(t))

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

### a--σ correlation

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

??? success "Solution to Exercise 1"
    **RMSE (Root Mean Squared Error):**

    $$
    \text{RMSE} = \sqrt{\frac{1}{M}\sum_{j=1}^M (\sigma^{\text{model}}_j - \sigma^{\text{mkt}}_j)^2}
    $$

    RMSE penalizes large errors disproportionately because it squares deviations before averaging. It is the standard metric when the loss function is quadratic (e.g., least-squares calibration). RMSE is most useful when all instruments are equally important and outlier errors are costly.

    **MAE (Mean Absolute Error):**

    $$
    \text{MAE} = \frac{1}{M}\sum_{j=1}^M |\sigma^{\text{model}}_j - \sigma^{\text{mkt}}_j|
    $$

    MAE treats all errors linearly and is less sensitive to outliers than RMSE. **Prefer MAE over RMSE when:** (i) a few instruments are known to be less liquid or have wider bid-ask spreads (so large errors on those instruments are expected and should not dominate the metric), or (ii) the calibration target is median accuracy across the instrument set rather than minimizing worst-case squared error.

    **MaxErr (Maximum Absolute Error):**

    $$
    \text{MaxErr} = \max_j |\sigma^{\text{model}}_j - \sigma^{\text{mkt}}_j|
    $$

    MaxErr identifies the single worst-fitting instrument. **MaxErr is most informative when:** (i) any mispriced instrument could create an arbitrage opportunity or a visible mark-to-market discrepancy, (ii) regulatory or audit constraints require that no single instrument exceed a threshold error, or (iii) diagnosing systematic model biases (a large MaxErr at a specific maturity reveals a structural limitation).

    The three metrics are related by the inequality $\text{MAE} \le \text{RMSE} \le \text{MaxErr}$, and they are equal only when all errors are identical.

---

**Exercise 2.** A Hull-White model with constant $\sigma$ produces ATM cap volatility RMSE of 20 bps. After switching to piecewise-constant $\sigma(t)$ with one level per cap maturity, the RMSE drops to $< 0.1$ bps. Explain why this dramatic improvement occurs. How many free volatility parameters does the piecewise-constant model have if there are 10 cap maturities?

??? success "Solution to Exercise 2"
    With constant $\sigma$, the Hull-White model has only two free parameters ($a$ and $\sigma$) to fit 10 cap volatilities. The model generates a specific term structure shape for cap implied volatilities determined by the interplay of mean reversion and volatility. With 10 data points and 2 free parameters, the system is heavily over-determined (8 excess constraints), so the best-fit RMSE of 20 bps reflects a structural inability to match the market's volatility term structure.

    With piecewise-constant $\sigma(t)$, one assigns a separate volatility level $\sigma_i$ to each caplet interval $[T_{i-1}, T_i]$. For 10 cap maturities, the model has **10 free volatility parameters** (one per cap maturity bucket), plus the mean reversion $a$. Since each cap price depends primarily on the corresponding $\sigma_i$ (the caplet volatility in that interval), the system becomes (approximately) exactly determined. The Hull-White cap pricing formula provides an analytical relationship between $\sigma_i$ and the $i$-th cap price, enabling a sequential bootstrap:

    1. Calibrate $\sigma_1$ to the 1Y cap
    2. Calibrate $\sigma_2$ to the 2Y cap (with $\sigma_1$ already fixed)
    3. Continue sequentially through all 10 maturities

    Each step involves solving a one-dimensional equation analytically (or near-analytically), so the fit is exact to machine precision ($< 0.1$ bps). The dramatic improvement occurs because the number of free parameters matches the number of constraints, eliminating the over-determination that caused the 20 bps RMSE with constant $\sigma$.

---

**Exercise 3.** The CIR model with constant parameters shows higher cap volatility RMSE (20--35 bps) than Hull-White (15--25 bps). Identify the structural reason: the CIR cap implied volatility depends on the rate level through $\sqrt{r}$, while Hull-White cap implied volatility is level-independent. How does this affect the fit quality when the current rate is far from $\theta$?

??? success "Solution to Exercise 3"
    In the Hull-White model, the caplet implied volatility depends on the bond price volatility

    $$
    \sigma_P = \frac{\sigma}{a}(1 - e^{-a\delta})\sqrt{\frac{1 - e^{-2aT}}{2a}}
    $$

    which is independent of the current rate level $r_t$. This means the HW cap implied volatility is purely a function of the parameters $(a, \sigma)$ and the maturity structure, not of where rates currently stand.

    In the CIR model, the instantaneous volatility is $\sigma\sqrt{r_t}$, so the effective volatility of rate changes depends on the rate level. When pricing caps, the caplet volatility is influenced by the expected path of $r_t$, which depends on the relationship between the current rate $r_0$ and the long-run mean $\theta$:

    - **If $r_0 \gg \theta$**: The rate is expected to mean-revert downward. Since CIR volatility $\propto \sqrt{r}$, the volatility will decrease along the expected path, making short-maturity caplets relatively more volatile than long-maturity ones (compared to the case $r_0 = \theta$).
    - **If $r_0 \ll \theta$**: The rate is expected to mean-revert upward, increasing the volatility over time. Long-maturity caplets become relatively more volatile.

    This level dependence introduces a coupling between the yield curve level and the volatility term structure that does not exist in Hull-White. When the current rate is far from $\theta$, the CIR model's cap volatility term structure is distorted by the expected rate path, making it harder to simultaneously fit short-end and long-end cap volatilities with constant parameters. Hull-White, being level-independent, separates the curve fit (via $\theta(t)$) from the volatility fit (via $a$ and $\sigma$), allowing each to be calibrated independently.

    This structural difference accounts for the higher RMSE range of CIR (20--35 bps) versus Hull-White (15--25 bps) with constant parameters.

---

**Exercise 4.** Explain why the one-factor structure is the dominant source of swaption calibration error, regardless of whether Hull-White or Black-Karasinski is used. What specific property of the swaption volatility matrix cannot be reproduced by any one-factor model?

??? success "Solution to Exercise 4"
    A one-factor model implies that all rates are driven by a single Brownian motion, which forces **perfect instantaneous correlation** between rates at all tenors. Specifically, if $r(t)$ is the single factor, then the forward rate $f(t,T)$ at any tenor $T$ is a deterministic function of $r(t)$, and

    $$
    \text{Corr}\bigl(df(t,T_1),\; df(t,T_2)\bigr) = \pm 1
    $$

    for all tenors $T_1$, $T_2$.

    The swaption volatility matrix (expiry $\times$ tenor) encodes the market's view of how rate volatility varies across both the time dimension (expiry) and the tenor dimension (swap length). A one-factor model can match the **diagonal** of this matrix (by varying $\sigma(t)$), but it cannot independently control the volatilities at different tenors for the same expiry. Specifically:

    - The ratio of swaption volatilities at the same expiry but different tenors is determined by the $B(\tau)$ function, which is fixed by $a$.
    - The market swaption matrix shows that this ratio varies with expiry, reflecting time-varying correlations that a single factor cannot produce.

    **The specific property that cannot be reproduced:** the decorrelation between rates at different tenors. Market data shows that short-term and long-term rates are imperfectly correlated (typically 0.7--0.9), and this correlation varies with the horizon. A one-factor model imposes correlation $\equiv 1$, forcing all off-diagonal swaption volatilities to be mechanically determined once the diagonal is fitted. This is why both Hull-White and Black-Karasinski produce similar swaption RMSE (30--60 bps with constant $\sigma$): the error is dominated by the single-factor constraint, not by the distributional assumption.

    To improve the swaption matrix fit, one must move to a **two-factor** (or multi-factor) model, which introduces a second source of randomness that allows imperfect correlation between rate tenors.

---

**Exercise 5.** BK with piecewise-constant $\sigma(t)$ shows higher parameter instability (2--5% daily change per bucket) than HW (1--3%). Explain why tree-based calibration introduces discretization noise that contributes to this instability. How would increasing the number of tree steps affect stability?

??? success "Solution to Exercise 5"
    Black-Karasinski calibration uses a trinomial tree where the $\theta(t)$ function is determined numerically to match market discount factors. At each time step $t_i$, the algorithm:

    1. Proposes a value of $\theta(t_i)$
    2. Builds the tree out to maturity
    3. Computes model bond prices by backward induction
    4. Adjusts $\theta(t_i)$ until the model bond price matches the market bond price

    **Sources of discretization noise:**

    - The tree has a finite number of nodes $J$ per time slice and a finite time step $\Delta t$. The rate at each node is $r_{ij} = e^{x_j}$ where $x_j$ lies on a discrete grid.
    - Small changes in the yield curve shift the required $\theta(t_i)$ values, but the tree nodes remain on the same discrete grid. The mapping from continuous $\theta(t)$ to discrete tree probabilities introduces quantization error.
    - When $\sigma(t)$ is piecewise-constant, each bucket's calibrated value depends on the tree's representation of the rate distribution within that bucket's time interval. The tree's discrete branching approximates a continuous log-normal distribution, and this approximation error varies with the yield curve level.

    **Effect of increasing tree steps:**

    More tree steps ($N_t \uparrow$) reduce the time step $\Delta t$ and increase the number of nodes, which:

    - Reduces discretization error in $\theta(t)$ calibration (finer resolution of the yield curve)
    - Reduces quantization noise in transition probabilities
    - Smooths the relationship between market data changes and parameter changes

    This directly reduces the day-over-day parameter instability. However, the improvement comes at computational cost: doubling $N_t$ roughly quadruples the tree computation time (since the number of nodes grows as $O(N_t^2)$ for a trinomial tree). In practice, BK trees use 50--200 steps per year, balancing stability against speed.

    Hull-White avoids this issue entirely because $\theta(t)$ is calibrated analytically via the market forward rate curve $f^M(0,t)$, with no tree discretization involved. The analytical bootstrap is immune to discretization noise, explaining the lower parameter instability.

---

**Exercise 6.** The $a$--$\sigma$ correlation creates a ridge in the calibration objective function. For Hull-White, sketch the level curves of the cap volatility RMSE in the $(a, \sigma)$ plane and indicate the ridge direction. Explain the practical recommendation to fix $a$ from historical estimation.

??? success "Solution to Exercise 6"
    The cap volatility RMSE as a function of $(a, \sigma)$ has the following structure:

    - **Ridge direction**: The level curves form elongated ellipses along a direction where increasing $a$ is compensated by increasing $\sigma$. Higher $a$ means faster mean reversion, which reduces the effective volatility of long-term rates. To compensate and maintain the same cap prices, $\sigma$ must increase. The ridge runs approximately along the line $\sigma \propto a^{1/2}$ (for long-dated caps, the cap volatility scales as $\sigma / \sqrt{2a}$, so holding $\sigma/\sqrt{a}$ constant maintains similar prices).
    - **Across the ridge**: The objective function changes rapidly. A small perturbation perpendicular to the ridge produces a large RMSE change.
    - **Along the ridge**: The objective function is nearly flat. Many $(a, \sigma)$ combinations along the ridge produce similar RMSE, making the optimizer's job difficult.

    The level curves in the $(a, \sigma)$ plane look like narrow ellipses tilted at approximately $45°$ in log-coordinates (since $\log\sigma \approx \frac{1}{2}\log a + \text{const}$ along the ridge).

    **Practical recommendation to fix $a$:** By fixing $a$ from historical estimation (e.g., regressing $\Delta r_t$ on $r_t$ to estimate the physical mean reversion, then adjusting for the market price of risk), the calibration reduces to a one-dimensional optimization over $\sigma$ alone. This eliminates the ridge because:

    - With $a$ fixed, the objective function $\text{RMSE}(\sigma)$ is a smooth, convex function of $\sigma$ with a unique minimum.
    - The optimizer converges quickly and reliably.
    - Day-over-day stability improves because only $\sigma$ adjusts to reflect changing market conditions, while $a$ (which is poorly identified from option data alone) remains anchored.

    This approach separates the estimation of the mean reversion structure (from historical data or from the swaption matrix diagonal) from the calibration of the volatility level (from cap prices).

---

**Exercise 7.** A portfolio contains both ATM caps and deep OTM receiver swaptions. Based on the summary table, propose a calibration strategy that uses Hull-White for the ATM caps and Black-Karasinski for the OTM swaptions. What challenges arise from using two models for the same portfolio, particularly for hedging and risk aggregation?

??? success "Solution to Exercise 7"
    **Proposed dual-model calibration strategy:**

    1. **Hull-White for ATM caps**: Calibrate $a$ and $\sigma(t)$ (piecewise-constant) to ATM cap volatilities using the analytical bootstrap. This gives an exact fit to ATM caps with machine precision and sub-millisecond computation.

    2. **Black-Karasinski for OTM receiver swaptions**: Calibrate $a_{\text{BK}}$ and $\sigma_{\text{BK}}(t)$ to the OTM receiver swaption prices using a trinomial tree. The log-normal rate distribution produces a smile that better matches the market prices of deep OTM receiver swaptions (which depend on the left tail of the rate distribution, where the difference between normal and log-normal is largest).

    **Challenges of using two models:**

    1. **Inconsistent hedging**: A cap hedged using Hull-White Greeks will have different sensitivities than the same position valued under Black-Karasinski. If the portfolio contains both ATM caps and OTM swaptions, the hedge ratios from the two models will not aggregate consistently. For example, the portfolio delta under HW differs from the portfolio delta under BK, and there is no principled way to combine them.

    2. **Risk aggregation**: VaR and P&L attribution require a single model to revalue the entire portfolio under stressed scenarios. With two models, the total portfolio P&L is the sum of two model-specific P&Ls, but the interaction terms (how a rate move affects both the HW-priced caps and BK-priced swaptions) are inconsistent. The correlation structure between instruments is implicitly different under each model.

    3. **Arbitrage between models**: The two models imply different rate distributions. If the HW-implied forward rate distribution disagrees with the BK-implied distribution, there may exist portfolios of caps and swaptions that appear to have positive expected value under one model but not the other. This internal inconsistency can be exploited (inadvertently or deliberately), creating hidden risk.

    4. **Operational complexity**: Maintaining two calibration pipelines, two pricing engines, and two sets of Greeks doubles the infrastructure cost and increases the risk of errors.

    **A better alternative** is to use a single model that captures the smile, such as shifted Hull-White (which adds a displacement parameter to produce a non-trivial smile while retaining analytical tractability) or a two-factor Hull-White model that can better fit both the swaption matrix and the cap smile simultaneously.
