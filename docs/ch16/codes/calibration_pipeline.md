# Calibration Pipeline

Calibrating the Heston model in practice involves much more than calling an optimizer. Raw market data must be cleaned, filtered for arbitrage violations, and organized by maturity. The pricing engine must be configured for speed (FFT for the full surface sweep) rather than precision. The optimizer must be initialized with sensible bounds, run through a global search stage, and refined locally. After calibration, the results must be validated against market data and checked for parameter stability. This guide assembles all these components into a production-quality **end-to-end calibration pipeline**, referencing the implementation in [`calibration_pipeline.py`](calibration_pipeline.py).

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Design a complete calibration pipeline from raw market data to validated Heston parameters
    2. Implement market data preprocessing with arbitrage filtering and IV extraction
    3. Configure the two-stage optimizer (DE global + local refinement) with appropriate bounds and tolerances
    4. Validate calibration results through fit diagnostics and parameter stability checks

!!! tip "Prerequisites"
    This section integrates all prior calibration components: the [objective function design](../calibration/objective_function_design.md), [differential evolution](../calibration/differential_evolution.md), [parameter stability](../calibration/parameter_stability.md), [joint calibration](../calibration/joint_calibration_across_maturities.md), and the [characteristic function engine](characteristic_function_engine.md) or [COS/FFT engines](cos_and_fft_pricing_engines.md) for pricing.

---

## Pipeline Overview

The calibration pipeline consists of five stages, each of which can fail independently and must be monitored.

```
Raw Market Data → [Stage 1: Preprocess] → Clean IV Surface
                  → [Stage 2: Configure] → Objective + Bounds
                  → [Stage 3: Optimize]  → Calibrated Θ*
                  → [Stage 4: Validate]  → Diagnostics
                  → [Stage 5: Store]     → Parameters + Metadata
```

---

## Stage 1: Market Data Preprocessing

### Input Format

Market data arrives as a table of option quotes with columns: strike $K$, maturity $T$, bid price $C^{\text{bid}}$, ask price $C^{\text{ask}}$, option type (call/put), plus market context: spot $S_0$, risk-free rate $r(T)$ (a term structure), and dividend yield $q(T)$.

### Mid-Price and IV Extraction

Compute the mid-price $C^{\text{mid}} = (C^{\text{bid}} + C^{\text{ask}}) / 2$ and extract the implied volatility $\sigma^{\text{mkt}}$ by inverting the Black-Scholes formula via Newton-Raphson. Options where Newton-Raphson fails to converge (typically deep OTM options with mid-prices near zero) are flagged and excluded.

### Arbitrage Filtering

Apply the following static arbitrage checks and remove violations:

1. **Non-negative price**: $C^{\text{mid}} > 0$
2. **Call spread**: $C(K_1, T) \geq C(K_2, T)$ for $K_1 < K_2$ (calls are decreasing in strike)
3. **Butterfly spread**: $C(K - \delta, T) + C(K + \delta, T) \geq 2C(K, T)$ (convexity in strike)
4. **Calendar spread**: $C(K, T_1) \leq C(K, T_2)$ for $T_1 < T_2$ (calls are increasing in maturity)
5. **Intrinsic value bound**: $C(K, T) \geq \max(S_0 e^{-qT} - K e^{-rT}, 0)$

```python
def filter_arbitrage(options_df, S0, r_curve, q_curve):
    """Remove options violating static no-arbitrage conditions."""
    df = options_df.copy()

    # Non-negative prices
    df = df[df['mid_price'] > 0]

    # Intrinsic value
    for _, row in df.iterrows():
        K, T = row['strike'], row['maturity']
        r_T, q_T = r_curve(T), q_curve(T)
        intrinsic = max(S0 * np.exp(-q_T * T) - K * np.exp(-r_T * T), 0)
        if row['mid_price'] < intrinsic:
            df.drop(row.name, inplace=True)

    # Butterfly (convexity) per maturity
    for T, group in df.groupby('maturity'):
        group = group.sort_values('strike')
        # Check second differences of price w.r.t. strike
        # Remove options that violate convexity

    return df
```

### Maturity Grouping

Organize the cleaned options by maturity. Each maturity group provides a slice of the IV smile that the calibration will fit simultaneously.

---

## Stage 2: Objective Function Configuration

### Pricing Engine Selection

For calibration, the **Carr-Madan FFT** is the preferred pricing engine because it produces prices for all strikes at a given maturity in a single $\mathcal{O}(N\log N)$ call. The alternative is the COS method, which is per-strike but with very small $N$.

### Vega Weights

Compute the Black-Scholes vega for each option at its market implied volatility:

$$
\mathcal{V}_i = S_0 e^{-q_i T_i} \sqrt{T_i} \, \phi(d_{1,i})
$$

Set $w_i = 1 / \mathcal{V}_i^2$. These weights are constants computed once before optimization.

### Parameter Bounds

| Parameter | Lower | Upper | Notes |
|---|---|---|---|
| $v_0$ | $0.5 \cdot (\sigma_{\text{ATM}}^{\text{short}})^2$ | $2.0 \cdot (\sigma_{\text{ATM}}^{\text{short}})^2$ | Centered on short-maturity ATM level |
| $\kappa$ | $0.01$ | $10.0$ | Allows slow to fast mean-reversion |
| $\theta$ | $0.5 \cdot (\sigma_{\text{ATM}}^{\text{long}})^2$ | $2.0 \cdot (\sigma_{\text{ATM}}^{\text{long}})^2$ | Centered on long-maturity ATM level |
| $\xi$ | $0.01$ | $3.0$ | Wide range for vol-of-vol |
| $\rho$ | $-0.99$ | $-0.01$ | Equities: $\rho < 0$ (leverage effect) |

The $v_0$ and $\theta$ bounds are data-informed: use the ATM implied volatilities at the shortest and longest maturities as initial estimates. For equity indices, $\rho$ is always negative; restricting the upper bound to $-0.01$ (instead of $+0.99$) halves the search space.

### Regularization

Add the Tikhonov penalty if yesterday's calibrated parameters $\Theta_{\text{prev}}$ are available:

$$
\mathcal{L}_{\text{total}}(\Theta) = \mathcal{L}_{\text{vega}}(\Theta) + \sum_{j=1}^{5} \lambda_j (\Theta_j - \Theta_{\text{prev},j})^2
$$

---

## Stage 3: Optimization

### Global Search (Differential Evolution)

Run DE with the following settings:

```python
from scipy.optimize import differential_evolution

result_de = differential_evolution(
    objective,
    bounds=param_bounds,
    strategy='best1bin',
    maxiter=300,
    popsize=15,       # population = 15 * 5 = 75
    tol=1e-8,
    atol=1e-8,
    seed=42,
    workers=-1,       # parallelize across CPU cores
    updating='deferred'  # required for parallel workers
)
```

Typical runtime: 5--30 seconds depending on the number of options and CPU cores.

### Local Refinement

Starting from the DE solution, run a local optimizer:

```python
from scipy.optimize import minimize

result_local = minimize(
    objective,
    x0=result_de.x,
    method='Nelder-Mead',
    options={'xatol': 1e-10, 'fatol': 1e-10, 'maxiter': 5000}
)
```

The local refinement typically reduces the objective by a further 10--50% and takes 1--5 seconds.

### Assembling the Result

```python
calibrated = {
    'v0': result_local.x[0],
    'kappa': result_local.x[1],
    'theta': result_local.x[2],
    'xi': result_local.x[3],
    'rho': result_local.x[4],
    'objective': result_local.fun,
    'n_options': M,
    'timestamp': datetime.now(),
    'de_iterations': result_de.nit,
    'local_iterations': result_local.nit
}
```

---

## Stage 4: Validation

After calibration, run the following diagnostics to assess fit quality and parameter reasonableness.

### Fit Quality Metrics

Compute per-maturity and aggregate metrics:

$$
\text{IVRMSE}(T_j) = \sqrt{\frac{1}{N_j}\sum_{k=1}^{N_j}\left(\sigma_{jk}^{\text{mod}} - \sigma_{jk}^{\text{mkt}}\right)^2}
$$

$$
\text{IVRMSE}_{\text{total}} = \sqrt{\frac{1}{M}\sum_{i=1}^{M}\left(\sigma_i^{\text{mod}} - \sigma_i^{\text{mkt}}\right)^2}
$$

Acceptable thresholds depend on the application:

| Application | IVRMSE Threshold |
|---|---|
| Exotic pricing | < 50 bps |
| Vanilla hedging | < 30 bps |
| Market making | < 15 bps |

### Residual Analysis

Plot the residuals $\sigma_i^{\text{mod}} - \sigma_i^{\text{mkt}}$ as a function of moneyness $K/S_0$ for each maturity. Look for:

- **Random scatter**: Good calibration, residuals are noise.
- **Systematic pattern** (e.g., positive residuals on the put wing, negative on the call wing): The model's smile shape is wrong, suggesting a structural limitation.
- **Maturity dependence** (e.g., short maturities fit well, long maturities poorly): The $\kappa$-$\theta$ identification is weak, or the model's term structure is inadequate.

### Parameter Reasonableness

Check that calibrated parameters are economically sensible:

- $v_0 \approx (\sigma_{\text{ATM}}^{\text{short}})^2$
- $\theta \approx (\sigma_{\text{ATM}}^{\text{long}})^2$
- $\kappa \in [0.5, 5.0]$ (half-life between 0.14 and 1.4 years)
- $\xi \in [0.1, 1.5]$ for equity indices
- $\rho \in [-0.9, -0.3]$ for equity indices

!!! warning "Red Flags"
    Parameters hitting their bounds (e.g., $\kappa = 10.0$ or $\rho = -0.99$) indicate that the optimizer is struggling. Widen the bounds or investigate the market data for anomalies.

---

## Stage 5: Storage and Logging

Store the calibrated parameters along with metadata:

```python
calibration_record = {
    'date': '2026-03-22',
    'underlying': 'SPX',
    'parameters': calibrated,
    'fit_quality': {
        'ivrmse_total': ivrmse,
        'ivrmse_per_maturity': ivrmse_per_T,
        'max_abs_residual': max_residual
    },
    'diagnostics': {
        'feller_ratio': 2 * kappa * theta / xi**2,
        'half_life': np.log(2) / kappa,
        'de_converged': result_de.success,
        'local_converged': result_local.success
    },
    'market_data': {
        'n_options': M,
        'n_maturities': N_T,
        'maturities': maturities.tolist()
    }
}
```

This record enables parameter history tracking, stability monitoring, and reproducibility.

---

## Worked Example

Calibrate to SPX options with $S_0 = 4500$, 5 maturities (1M to 2Y), 135 total options.

**Stage 1**: After arbitrage filtering, 128 options remain (7 removed for butterfly violations).

**Stage 2**: Vega weights computed. Bounds: $v_0 \in [0.010, 0.050]$, $\kappa \in [0.01, 10]$, $\theta \in [0.015, 0.080]$, $\xi \in [0.01, 3.0]$, $\rho \in [-0.99, -0.01]$.

**Stage 3**: DE converges in 187 generations (14,025 objective evaluations, 8.2 seconds). Nelder-Mead converges in 203 iterations (1.1 seconds). Total: 9.3 seconds.

**Stage 4**: IVRMSE = 22 bps. Per-maturity breakdown: 1M: 31 bps, 3M: 18 bps, 6M: 15 bps, 1Y: 20 bps, 2Y: 28 bps. No parameters hit bounds.

**Calibrated parameters**: $v_0 = 0.0263$, $\kappa = 2.35$, $\theta = 0.0438$, $\xi = 0.42$, $\rho = -0.72$. Feller ratio: $2(2.35)(0.0438)/0.42^2 = 1.17$ (Feller satisfied).

---

## Summary

The calibration pipeline transforms raw market option data into validated Heston parameters through five stages: preprocessing (arbitrage filtering, IV extraction), configuration (pricing engine, vega weights, bounds, regularization), optimization (DE global + local refinement), validation (IVRMSE, residual patterns, parameter reasonableness), and storage (parameters + metadata). Each stage has failure modes that must be monitored: arbitrage violations in the input data, optimizer convergence failures, parameters hitting bounds, and systematic residual patterns indicating model limitations. The pipeline in [`calibration_pipeline.py`](calibration_pipeline.py) implements this workflow with the `HestonCalibrator` class.

---

## Exercises

**Exercise 1.**
A market data set contains 150 European call options across 6 maturities. After applying static arbitrage filters, 12 options are removed: 5 for butterfly violations, 4 for negative mid-prices, and 3 for calendar spread violations. Explain each type of arbitrage violation in financial terms. If you observe that most butterfly violations occur at the shortest maturity, what does this suggest about the quality of the short-dated market quotes?

---

**Exercise 2.**
The pipeline uses data-informed bounds for $v_0$ and $\theta$. If the shortest-maturity ATM implied volatility is $\sigma_{\text{ATM}}^{\text{short}} = 18\%$ and the longest-maturity ATM is $\sigma_{\text{ATM}}^{\text{long}} = 22\%$, compute the bounds for $v_0$ and $\theta$ using the rule $[0.5\sigma^2, 2.0\sigma^2]$. Why is it advantageous to use data-informed bounds rather than fixed bounds like $[0.001, 1.0]$?

---

**Exercise 3.**
The pipeline uses `scipy.optimize.differential_evolution` with `popsize=15` (so population $= 15 \times 5 = 75$) and `maxiter=300`. Compute the maximum number of objective function evaluations. If each evaluation prices $M = 128$ options using the Carr-Madan FFT with $N = 4096$ points, estimate the total number of FFT calls (one per maturity per evaluation, assuming 5 maturities). Compare the cost if the COS method ($N = 128$) were used per-strike instead.

---

**Exercise 4.**
After calibration, the pipeline reports per-maturity IVRMSE as: 1M: 31 bps, 3M: 18 bps, 6M: 15 bps, 1Y: 20 bps, 2Y: 28 bps. The total IVRMSE is 22 bps. Verify that the total IVRMSE is consistent with the per-maturity values by computing:

$$
\text{IVRMSE}_{\text{total}} = \sqrt{\frac{1}{M}\sum_{j=1}^{N_T} N_j \cdot [\text{IVRMSE}(T_j)]^2}
$$

assuming the strike counts are $N_1 = 35$, $N_2 = 30$, $N_3 = 25$, $N_4 = 22$, $N_5 = 16$ with $M = 128$. Discuss whether a market-making desk would find these error levels acceptable.

---

**Exercise 5.**
The calibrated parameters are $v_0 = 0.0263$, $\kappa = 2.35$, $\theta = 0.0438$, $\xi = 0.42$, $\rho = -0.72$, with a Feller ratio of 1.17. Suppose next day's calibration (without regularization) yields $v_0 = 0.0270$, $\kappa = 4.10$, $\theta = 0.0250$, $\xi = 0.50$, $\rho = -0.70$. Verify the Feller ratio for both parameter sets. Discuss whether the day-to-day parameter change is acceptable for a production system and propose specific regularization weights $\lambda_j$ to stabilize the calibration.

---

**Exercise 6.**
The validation stage checks for "red flags" such as parameters hitting their bounds. Suppose $\rho$ calibrates to $-0.99$ (the lower bound). List three possible root causes and the diagnostic steps you would take for each. Would widening the bound to $\rho \in [-0.999, -0.01]$ solve the problem? Why or why not?

---

**Exercise 7.**
Design a monitoring dashboard for a production calibration pipeline. Specify the metrics, thresholds, and alert conditions for each of the five pipeline stages. For example, Stage 4 (Validation) might alert if IVRMSE exceeds 50 bps or if any parameter changes by more than 50% day-over-day. Write the alert conditions as mathematical inequalities and justify each threshold based on typical market conditions and hedging requirements.
