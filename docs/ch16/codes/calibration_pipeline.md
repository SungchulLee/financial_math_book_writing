# Calibration Pipeline

Calibrating the Heston model in practice involves much more than calling an optimizer. Raw market data must be cleaned, filtered for arbitrage violations, and organized by maturity. The pricing engine must be configured for speed (FFT for the full surface sweep) rather than precision. The optimizer must be initialized with sensible bounds, run through a global search stage, and refined locally. After calibration, the results must be validated against market data and checked for parameter stability. This guide assembles all these components into a production-quality **end-to-end calibration pipeline**, referencing the implementation in [`calibration_pipeline.py`](calibration_pipeline.md).

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

The calibration pipeline transforms raw market option data into validated Heston parameters through five stages: preprocessing (arbitrage filtering, IV extraction), configuration (pricing engine, vega weights, bounds, regularization), optimization (DE global + local refinement), validation (IVRMSE, residual patterns, parameter reasonableness), and storage (parameters + metadata). Each stage has failure modes that must be monitored: arbitrage violations in the input data, optimizer convergence failures, parameters hitting bounds, and systematic residual patterns indicating model limitations. The pipeline in [`calibration_pipeline.py`](calibration_pipeline.md) implements this workflow with the `HestonCalibrator` class.

---

## Exercises

**Exercise 1.**
A market data set contains 150 European call options across 6 maturities. After applying static arbitrage filters, 12 options are removed: 5 for butterfly violations, 4 for negative mid-prices, and 3 for calendar spread violations. Explain each type of arbitrage violation in financial terms. If you observe that most butterfly violations occur at the shortest maturity, what does this suggest about the quality of the short-dated market quotes?

??? success "Solution to Exercise 1"
    Each arbitrage violation type has a specific financial interpretation:

    **Butterfly violations** (5 removed): A butterfly spread with strikes $K - \delta$, $K$, $K + \delta$ has a non-negative payoff. The condition $C(K - \delta) + C(K + \delta) \geq 2C(K)$ is equivalent to requiring the call price function to be **convex** in $K$, which is equivalent to the risk-neutral density being non-negative. A violation means the mid-price implies a locally negative probability density, which is economically impossible and indicates a quote anomaly.

    **Negative mid-prices** (4 removed): A European call has non-negative payoff $\max(S_T - K, 0) \geq 0$, so its price must satisfy $C \geq 0$. A negative mid-price typically arises from stale bid quotes or illiquid markets where the bid is zero and the ask is very small, and rounding or data errors push the mid below zero.

    **Calendar spread violations** (3 removed): Since a longer-dated call can be exercised at the same strike as a shorter-dated call (plus you have the additional optionality of the remaining time), we need $C(K, T_1) \leq C(K, T_2)$ for $T_1 < T_2$. Violations indicate temporal inconsistency in the quotes, often caused by different market-making desks or asynchronous quote timestamps.

    If most butterfly violations occur at the **shortest maturity**, this suggests that short-dated option quotes are of lower quality. Short-dated options have high gamma, meaning their prices are highly sensitive to small movements in the underlying. Market makers widen bid-ask spreads for short-dated options, and the mid-price is less reliable as an estimator of fair value. Additionally, short-dated smiles are steeper (more curvature in the IV smile), making convexity violations more likely when quotes are slightly off. The remedy is to use tighter filters for short-dated options or increase the bid-ask tolerance before computing mid-prices.

---

**Exercise 2.**
The pipeline uses data-informed bounds for $v_0$ and $\theta$. If the shortest-maturity ATM implied volatility is $\sigma_{\text{ATM}}^{\text{short}} = 18\%$ and the longest-maturity ATM is $\sigma_{\text{ATM}}^{\text{long}} = 22\%$, compute the bounds for $v_0$ and $\theta$ using the rule $[0.5\sigma^2, 2.0\sigma^2]$. Why is it advantageous to use data-informed bounds rather than fixed bounds like $[0.001, 1.0]$?

??? success "Solution to Exercise 2"
    Given $\sigma_{\text{ATM}}^{\text{short}} = 0.18$ and $\sigma_{\text{ATM}}^{\text{long}} = 0.22$, the data-informed bounds are:

    **For $v_0$** (centered on the short-maturity ATM variance):

    $$
    v_0 \in [0.5 \cdot (0.18)^2, \; 2.0 \cdot (0.18)^2] = [0.5 \cdot 0.0324, \; 2.0 \cdot 0.0324] = [0.0162, \; 0.0648]
    $$

    **For $\theta$** (centered on the long-maturity ATM variance):

    $$
    \theta \in [0.5 \cdot (0.22)^2, \; 2.0 \cdot (0.22)^2] = [0.5 \cdot 0.0484, \; 2.0 \cdot 0.0484] = [0.0242, \; 0.0968]
    $$

    Data-informed bounds are advantageous for several reasons:

    1. **Reduced search space**: The interval $[0.0162, 0.0648]$ is far narrower than $[0.001, 1.0]$, reducing the volume of the 5D search space by orders of magnitude. Since DE's convergence rate depends on the hypervolume of the bounds, tighter bounds mean fewer generations to convergence.

    2. **Better initialization**: The DE population is seeded uniformly within the bounds. With $[0.001, 1.0]$, most initial candidates have $v_0 \gg 0.04$ (the typical range), wasting many generations on implausible regions.

    3. **Avoids numerical issues**: Very large values of $v_0$ or $\theta$ (e.g., $v_0 = 0.9$, corresponding to 95% instantaneous volatility) can cause overflow in the characteristic function evaluation, particularly in the exponential $e^{-\gamma\tau}$.

    4. **Economic grounding**: The relationship $v_0 \approx (\sigma_{\text{ATM}}^{\text{short}})^2$ and $\theta \approx (\sigma_{\text{ATM}}^{\text{long}})^2$ follows directly from the Heston ATM approximation, so the bounds are centered on the most likely parameter values.

---

**Exercise 3.**
The pipeline uses `scipy.optimize.differential_evolution` with `popsize=15` (so population $= 15 \times 5 = 75$) and `maxiter=300`. Compute the maximum number of objective function evaluations. If each evaluation prices $M = 128$ options using the Carr-Madan FFT with $N = 4096$ points, estimate the total number of FFT calls (one per maturity per evaluation, assuming 5 maturities). Compare the cost if the COS method ($N = 128$) were used per-strike instead.

??? success "Solution to Exercise 3"
    **Maximum objective function evaluations for DE:**

    With `popsize=15` and 5 parameters, the population size is $N_p = 15 \times 5 = 75$. With `maxiter=300`, the maximum number of evaluations is:

    $$
    N_{\text{eval}}^{\text{DE}} = N_p \times (\texttt{maxiter} + 1) = 75 \times 301 = 22{,}575
    $$

    (The +1 accounts for the initial population evaluation. In practice, DE may terminate earlier if the tolerance is met.)

    **Total FFT calls with Carr-Madan:**

    Each evaluation prices all strikes at each maturity with one FFT call per maturity. With 5 maturities:

    $$
    N_{\text{FFT}} = N_{\text{eval}} \times 5 = 22{,}575 \times 5 = 112{,}875
    $$

    Each FFT call processes $N = 4096$ points but prices **all** strikes at that maturity simultaneously. So the total number of CF evaluations is $112{,}875 \times 4{,}096 \approx 4.62 \times 10^8$.

    **Cost comparison with COS method ($N = 128$) per-strike:**

    With the COS method, each strike requires $N = 128$ CF evaluations. With $M = 128$ options spread across 5 maturities (approximately 25--26 strikes per maturity), each evaluation requires:

    $$
    N_{\text{CF}}^{\text{COS}} = M \times N_{\text{COS}} = 128 \times 128 = 16{,}384 \text{ CF evaluations per objective call}
    $$

    Total CF evaluations: $22{,}575 \times 16{,}384 \approx 3.70 \times 10^8$.

    However, the FFT has the advantage that $N = 4096$ CF evaluations per maturity are performed as a single vectorized array operation, whereas the COS method requires $N_{\text{COS}} = 128$ CF evaluations per strike, looped over strikes (or batched). In practice, the FFT is faster because:

    - The FFT produces all strike prices from a single CF evaluation batch (one per maturity)
    - The COS per-strike loop has Python overhead unless carefully vectorized
    - The FFT's $\mathcal{O}(N \log N)$ DFT step is negligible compared to CF evaluation

    For a fair comparison: FFT does $5 \times 4{,}096 = 20{,}480$ CF evaluations per objective call, while COS does $128 \times 128 = 16{,}384$. The COS method evaluates fewer CF values per objective call, but the FFT is typically faster in wall-clock time due to vectorization efficiency.

---

**Exercise 4.**
After calibration, the pipeline reports per-maturity IVRMSE as: 1M: 31 bps, 3M: 18 bps, 6M: 15 bps, 1Y: 20 bps, 2Y: 28 bps. The total IVRMSE is 22 bps. Verify that the total IVRMSE is consistent with the per-maturity values by computing:

$$
\text{IVRMSE}_{\text{total}} = \sqrt{\frac{1}{M}\sum_{j=1}^{N_T} N_j \cdot [\text{IVRMSE}(T_j)]^2}
$$

assuming the strike counts are $N_1 = 35$, $N_2 = 30$, $N_3 = 25$, $N_4 = 22$, $N_5 = 16$ with $M = 128$. Discuss whether a market-making desk would find these error levels acceptable.

??? success "Solution to Exercise 4"
    The aggregate IVRMSE from per-maturity values is:

    $$
    \text{IVRMSE}_{\text{total}} = \sqrt{\frac{1}{M}\sum_{j=1}^{N_T} N_j \cdot [\text{IVRMSE}(T_j)]^2}
    $$

    Substituting the given values with $M = 128$:

    $$
    \sum_{j=1}^{5} N_j \cdot [\text{IVRMSE}(T_j)]^2 = 35 \cdot (0.0031)^2 + 30 \cdot (0.0018)^2 + 25 \cdot (0.0015)^2 + 22 \cdot (0.0020)^2 + 16 \cdot (0.0028)^2
    $$

    Computing each term (in units of $10^{-6}$):

    - $35 \times 9.61 \times 10^{-6} = 336.35 \times 10^{-6}$
    - $30 \times 3.24 \times 10^{-6} = 97.20 \times 10^{-6}$
    - $25 \times 2.25 \times 10^{-6} = 56.25 \times 10^{-6}$
    - $22 \times 4.00 \times 10^{-6} = 88.00 \times 10^{-6}$
    - $16 \times 7.84 \times 10^{-6} = 125.44 \times 10^{-6}$

    $$
    \text{Sum} = 703.24 \times 10^{-6}
    $$

    $$
    \text{IVRMSE}_{\text{total}} = \sqrt{\frac{703.24 \times 10^{-6}}{128}} = \sqrt{5.494 \times 10^{-6}} = 0.002344 \approx 23.4 \text{ bps}
    $$

    This is close to the reported 22 bps, with the small discrepancy likely due to rounding in the per-maturity IVRMSE values.

    **Acceptability for market making:**

    A market-making desk requires IVRMSE below 15 bps. The total IVRMSE of 22 bps exceeds this threshold. However, the per-maturity breakdown reveals that the 3M (18 bps) and 6M (15 bps) maturities are within tolerance, while the 1M (31 bps) and 2Y (28 bps) are not. This is a known limitation of the single-parameter-set Heston model: short maturities have steep smiles that the model struggles to fit, and long maturities probe the term structure of volatility dynamics beyond what a constant $\kappa$, $\theta$ can capture.

    For vanilla hedging (threshold 30 bps), the total IVRMSE of 22 bps is acceptable. For exotic pricing (threshold 50 bps), it is comfortably within bounds. A market-making desk would need either a richer model (e.g., double Heston, or local-stochastic volatility) or maturity-dependent calibration weights.

---

**Exercise 5.**
The calibrated parameters are $v_0 = 0.0263$, $\kappa = 2.35$, $\theta = 0.0438$, $\xi = 0.42$, $\rho = -0.72$, with a Feller ratio of 1.17. Suppose next day's calibration (without regularization) yields $v_0 = 0.0270$, $\kappa = 4.10$, $\theta = 0.0250$, $\xi = 0.50$, $\rho = -0.70$. Verify the Feller ratio for both parameter sets. Discuss whether the day-to-day parameter change is acceptable for a production system and propose specific regularization weights $\lambda_j$ to stabilize the calibration.

??? success "Solution to Exercise 5"
    **Feller ratio for Day 1 parameters** ($v_0 = 0.0263$, $\kappa = 2.35$, $\theta = 0.0438$, $\xi = 0.42$):

    $$
    \mathcal{F}_1 = \frac{2\kappa\theta}{\xi^2} = \frac{2 \times 2.35 \times 0.0438}{0.42^2} = \frac{0.20586}{0.1764} = 1.167
    $$

    Feller condition is satisfied ($\mathcal{F}_1 > 1$).

    **Feller ratio for Day 2 parameters** ($v_0 = 0.0270$, $\kappa = 4.10$, $\theta = 0.0250$, $\xi = 0.50$):

    $$
    \mathcal{F}_2 = \frac{2 \times 4.10 \times 0.0250}{0.50^2} = \frac{0.205}{0.25} = 0.820
    $$

    Feller condition is **violated** ($\mathcal{F}_2 < 1$).

    **Day-over-day stability analysis:**

    | Parameter | Day 1 | Day 2 | Change | Relative Change |
    |---|---|---|---|---|
    | $v_0$ | 0.0263 | 0.0270 | +0.0007 | +2.7% |
    | $\kappa$ | 2.35 | 4.10 | +1.75 | +74.5% |
    | $\theta$ | 0.0438 | 0.0250 | $-0.0188$ | $-42.9$% |
    | $\xi$ | 0.42 | 0.50 | +0.08 | +19.0% |
    | $\rho$ | $-0.72$ | $-0.70$ | +0.02 | $-2.8$% |
    | $\kappa\theta$ | 0.1024 | 0.1025 | +0.0001 | +0.1% |

    The $\kappa$ and $\theta$ changes are **unacceptable** for production: a 74.5% change in $\kappa$ and 42.9% change in $\theta$ would cause large day-over-day jumps in Greeks and hedging positions, even though $\kappa\theta$ is essentially unchanged. This is a classic manifestation of the $\kappa$-$\theta$ degeneracy.

    **Proposed regularization weights:**

    The Tikhonov penalty is $\sum_j \lambda_j (\Theta_j - \Theta_{\text{prev},j})^2$. The weights should be scaled inversely with the parameter's typical range:

    - $\lambda_\kappa = 0.5$: Strong penalty on $\kappa$ changes, since $\kappa$ has the worst identifiability
    - $\lambda_\theta = 100$: Strong penalty on $\theta$ changes (scaled for the small magnitude of $\theta$)
    - $\lambda_\xi = 2.0$: Moderate penalty on vol-of-vol
    - $\lambda_{v_0} = 50$: Moderate penalty (scaled for small magnitude); $v_0$ should track the market's short-dated ATM level
    - $\lambda_\rho = 1.0$: Light penalty; $\rho$ is well-identified from the skew

    A practical heuristic is $\lambda_j \propto 1/\sigma_j^2$ where $\sigma_j$ is the typical day-over-day parameter change observed in a stable calibration history. With these weights, the regularized objective would penalize large $\kappa$ and $\theta$ moves, effectively stabilizing the degenerate $\kappa$-$\theta$ pair while allowing $v_0$ and $\rho$ to track the market.

---

**Exercise 6.**
The validation stage checks for "red flags" such as parameters hitting their bounds. Suppose $\rho$ calibrates to $-0.99$ (the lower bound). List three possible root causes and the diagnostic steps you would take for each. Would widening the bound to $\rho \in [-0.999, -0.01]$ solve the problem? Why or why not?

??? success "Solution to Exercise 6"
    If $\rho$ calibrates to $-0.99$ (the lower bound), three possible root causes and their diagnostics are:

    **Root Cause 1: Insufficient skew in the model.**

    The Heston model generates skew primarily through $\rho$. If the market's skew is steeper than what Heston can produce at moderate $\rho$ values, the optimizer pushes $\rho$ to its extreme. **Diagnostic**: Plot the calibrated model's IV smile against the market data. If the model underestimates skew even at $\rho = -0.99$, this confirms a structural model limitation. **Fix**: Use a richer model (e.g., add jumps via Bates, or use a double-Heston model) rather than widening the bound.

    **Root Cause 2: Market data anomalies in the put wing.**

    Stale or mispriced deep OTM puts inflate the apparent skew. **Diagnostic**: Check bid-ask spreads on the deep OTM puts. If the spread is wider than 50% of the mid-price, the quotes are unreliable. Also check whether the butterfly condition holds for the put-wing options. **Fix**: Remove or down-weight options with wide bid-ask spreads, particularly deep OTM puts with moneyness $K/S_0 < 0.85$.

    **Root Cause 3: Poor initialization or local minimum.**

    If DE converges to a local minimum near the $\rho$ boundary, the true global minimum may have a more moderate $\rho$ but different $\kappa$, $\theta$, $\xi$. **Diagnostic**: Run the calibration multiple times with different seeds and check if $\rho = -0.99$ is persistent. Also inspect $\xi$: if $\xi$ is very small alongside extreme $\rho$, the optimizer may be trading off skew (via $\rho$) against smile curvature (via $\xi$). **Fix**: Increase DE population size and generations. Try different starting regions.

    **Would widening to $\rho \in [-0.999, -0.01]$ help?**

    No, widening the bound would not solve the underlying problem and could make it worse. If $\rho = -0.99$ is already at the bound, allowing $\rho = -0.999$ would simply move the boundary-hitting to a more extreme value. The closer $\rho$ gets to $-1$, the more numerically unstable the model becomes: the correlation matrix $\begin{pmatrix} 1 & \rho \\ \rho & 1 \end{pmatrix}$ becomes nearly singular, the Cholesky factor $\sqrt{1 - \rho^2}$ becomes very small, and Monte Carlo paths degenerate. Additionally, $\rho$ near $-1$ makes the price surface nearly flat in the $\rho$ direction (diminishing sensitivity), so the optimizer's convergence degrades. The correct response is to diagnose the root cause and either fix the data or upgrade the model.

---

**Exercise 7.**
Design a monitoring dashboard for a production calibration pipeline. Specify the metrics, thresholds, and alert conditions for each of the five pipeline stages. For example, Stage 4 (Validation) might alert if IVRMSE exceeds 50 bps or if any parameter changes by more than 50% day-over-day. Write the alert conditions as mathematical inequalities and justify each threshold based on typical market conditions and hedging requirements.

??? success "Solution to Exercise 7"
    A production monitoring dashboard should track metrics, thresholds, and alerts for each pipeline stage:

    **Stage 1: Market Data Preprocessing**

    | Metric | Threshold | Alert Condition |
    |---|---|---|
    | Fraction of options removed | $> 15\%$ | $N_{\text{removed}} / N_{\text{input}} > 0.15$ |
    | Butterfly violations | $> 5\%$ of a single maturity | $N_{\text{butterfly}}(T_j) / N(T_j) > 0.05$ |
    | Newton-Raphson IV failures | $> 3\%$ | $N_{\text{NR fail}} / N_{\text{input}} > 0.03$ |
    | IV range | Unreasonable values | $\sigma^{\text{mkt}}_i > 1.0$ or $\sigma^{\text{mkt}}_i < 0.02$ |

    Justification: If more than 15% of options fail arbitrage checks, the market data feed is likely corrupted (e.g., stale quotes, exchange outage). The 5% per-maturity butterfly threshold catches localized quote anomalies.

    **Stage 2: Objective Configuration**

    | Metric | Threshold | Alert Condition |
    |---|---|---|
    | Bound width ratio | Too narrow or too wide | $v_0^{\text{upper}} / v_0^{\text{lower}} > 10$ or $< 2$ |
    | Number of options per maturity | Insufficient | $\min_j N(T_j) < 5$ |
    | Vega weight outliers | Extreme weights | $\max(w_i) / \text{median}(w_i) > 50$ |

    Justification: Extremely wide bounds indicate ATM levels are far apart (unusual market). Fewer than 5 options per maturity provides insufficient smile information.

    **Stage 3: Optimization**

    | Metric | Threshold | Alert Condition |
    |---|---|---|
    | DE convergence | Not converged | `result_de.success == False` |
    | DE iterations | Hit max | $N_{\text{iter}} = \texttt{maxiter}$ |
    | Local optimizer convergence | Not converged | `result_local.success == False` |
    | Objective improvement | Insufficient local gain | $(f_{\text{DE}} - f_{\text{local}}) / f_{\text{DE}} < 0.01$ |
    | Runtime | Excessive | $t_{\text{total}} > 120$ seconds |

    Justification: If DE uses all 300 generations without meeting the tolerance, the search space may be too large or the objective landscape is flat. Runtime above 2 minutes suggests a pricing engine bottleneck.

    **Stage 4: Validation**

    | Metric | Threshold | Alert Condition |
    |---|---|---|
    | Total IVRMSE | Application-dependent | $\text{IVRMSE}_{\text{total}} > 50$ bps |
    | Per-maturity IVRMSE | Short-maturity outlier | $\max_j \text{IVRMSE}(T_j) > 80$ bps |
    | Parameter boundary | Hitting bounds | $|\Theta_j - \Theta_j^{\text{bound}}| / |\Theta_j^{\text{bound}}| < 0.01$ |
    | Feller ratio | Severe violation | $\mathcal{F} < 0.3$ |
    | Day-over-day $\kappa$ change | Instability | $|\kappa_t - \kappa_{t-1}| / \kappa_{t-1} > 0.50$ |
    | Day-over-day $\rho$ change | Instability | $|\rho_t - \rho_{t-1}| > 0.10$ |
    | Systematic residuals | Pattern detected | $|\text{mean residual}(T_j)| > 20$ bps for any $j$ |

    Justification: IVRMSE above 50 bps is unacceptable even for exotic pricing. Day-over-day $\kappa$ changes above 50% cause hedging instability. Systematic residuals indicate model misspecification.

    **Stage 5: Storage and Logging**

    | Metric | Threshold | Alert Condition |
    |---|---|---|
    | Storage write failure | Any failure | I/O exception on write |
    | Missing fields | Incomplete record | Any required field is `None` or `NaN` |
    | Timestamp consistency | Clock skew | $|t_{\text{record}} - t_{\text{market}}| > 5$ minutes |

    Justification: Storage failures silently break the parameter history, preventing stability monitoring. Clock skew can cause parameter lookups to retrieve wrong-day calibrations.
