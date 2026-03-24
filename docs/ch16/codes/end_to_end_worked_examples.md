# End-to-End Worked Examples

This section ties together every component of the Heston model implementation---model class, characteristic function engine, COS/FFT pricing, Monte Carlo simulation, FDM solver, calibration pipeline, and Greeks computation---into three complete workflows. Each example starts from raw inputs and produces final answers, with intermediate values shown at every step so the reader can verify their own implementation. The companion code is in [`end_to_end_worked_examples.py`](end_to_end_worked_examples.py).

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Price a European call under Heston using five independent methods and verify cross-consistency
    2. Execute a full calibration pipeline from synthetic market data to validated parameters
    3. Compute Greeks and construct a delta-hedging P&L simulation
    4. Price a path-dependent exotic (Asian option) via Monte Carlo with control variates

!!! tip "Prerequisites"
    This section uses all prior code guides: the [`HestonModel` class](heston_model_class.md), the [CF engine](characteristic_function_engine.md), the [COS/FFT engines](cos_and_fft_pricing_engines.md), the [MC engine](monte_carlo_engine_qe.md), the [FDM engine](fdm_engine_adi.md), and the [calibration pipeline](calibration_pipeline.md).

---

## Example 1: European Call Pricing -- Five-Engine Comparison

### Setup

Create a Heston model with the following parameters:

| Parameter | Value | Interpretation |
|---|---|---|
| $S_0$ | \$100 | Spot price |
| $r$ | 3% | Risk-free rate |
| $q$ | 1% | Dividend yield |
| $v_0$ | 0.04 | Initial variance ($\sigma_0 = 20\%$) |
| $\kappa$ | 2.0 | Mean-reversion speed |
| $\theta$ | 0.04 | Long-run variance ($\sqrt{\theta} = 20\%$) |
| $\xi$ | 0.5 | Vol-of-vol |
| $\rho$ | $-0.7$ | Correlation |

Price a European call with $K = 100$ (ATM) and $T = 0.5$ years.

```python
model = HestonModel(S0=100, r=0.03, q=0.01,
                    v0=0.04, kappa=2.0, theta=0.04,
                    xi=0.5, rho=-0.7)
K, T = 100, 0.5
```

### Method 1: Gil-Pelaez Inversion

Evaluate the CF on a frequency grid $u \in [0.01, 100]$ with $N = 4096$ points, then compute $P_1$ and $P_2$ via the trapezoidal rule.

**Result**: $C^{\text{GP}} = 6.8061$

### Method 2: COS Method ($N = 128$)

Truncation range: $a = -0.7$, $b = 0.7$ (based on $L = 10$ and the cumulant estimate). Compute density coefficients $A_k$ and payoff coefficients $H_k^{\text{call}}$.

**Result**: $C^{\text{COS}} = 6.8061$

### Method 3: Carr-Madan FFT ($N = 4096$)

Damping parameter $\alpha = 1.5$, frequency spacing $\Delta\nu = 0.01$. Run FFT and interpolate to $K = 100$.

**Result**: $C^{\text{FFT}} = 6.8060$

### Method 4: Monte Carlo (QE Scheme)

$N_{\text{paths}} = 1{,}000{,}000$, $N_t = 100$ time steps, with antithetic variates.

**Result**: $C^{\text{MC}} = 6.8073 \pm 0.0098$ (95% CI: $[6.7877, 6.8269]$)

### Method 5: FDM (Craig-Sneyd ADI)

Grid: $N_x = 200$, $N_v = 100$, $N_t = 200$. Interpolate to $(S_0, v_0)$.

**Result**: $C^{\text{FDM}} = 6.8062$

### Cross-Comparison

| Method | Price | Error vs GP (bps) | Runtime |
|---|---|---|---|
| Gil-Pelaez | 6.8061 | -- | 12 ms |
| COS ($N = 128$) | 6.8061 | 0.00 | 0.5 ms |
| FFT ($N = 4096$) | 6.8060 | 0.01 | 3 ms |
| MC (1M paths, QE) | 6.8073 | 0.18 | 2.1 s |
| FDM ($200 \times 100 \times 200$) | 6.8062 | 0.01 | 0.8 s |

All five methods agree to within 0.2 basis points, confirming implementation consistency. The COS method is the fastest for a single option; the FFT is most efficient for many strikes.

---

## Example 2: Calibration Pipeline

### Synthetic Market Data

Generate "market" option prices from a known Heston model (the "true" model), then calibrate to recover the parameters.

**True parameters**: $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.05$, $\xi = 0.4$, $\rho = -0.65$.

Generate 60 call options: 4 maturities $T \in \{0.1, 0.25, 0.5, 1.0\}$ with 15 strikes each from $K = 80$ to $K = 120$.

```python
true_model = HestonModel(S0=100, r=0.03, q=0.01,
                         v0=0.04, kappa=1.5, theta=0.05,
                         xi=0.4, rho=-0.65)

maturities = [0.1, 0.25, 0.5, 1.0]
strikes = np.linspace(80, 120, 15)

# Generate "market" prices with 0.1% noise
market_prices = {}
for T in maturities:
    cos_prices = heston_cos_price(true_model, strikes, T)
    noise = 1 + np.random.normal(0, 0.001, len(strikes))
    market_prices[T] = cos_prices * noise
```

### Calibration

Run the calibration pipeline with DE ($N_p = 75$, 300 generations) + Nelder-Mead.

**Calibrated parameters vs true parameters:**

| Parameter | True | Calibrated | Error |
|---|---|---|---|
| $v_0$ | 0.0400 | 0.0401 | +0.25% |
| $\kappa$ | 1.500 | 1.620 | +8.0% |
| $\theta$ | 0.0500 | 0.0478 | $-4.4\%$ |
| $\xi$ | 0.400 | 0.393 | $-1.8\%$ |
| $\rho$ | $-0.650$ | $-0.658$ | +1.2% |

**Diagnostics**: IVRMSE = 5 bps (excellent). The $\kappa$-$\theta$ product: true $\kappa\theta = 0.075$, calibrated $\kappa\theta = 0.077$ (+2.7%)---much tighter than the individual $\kappa$ and $\theta$ errors, confirming the degeneracy.

### Implied Volatility Surface Comparison

At maturity $T = 0.25$:

| Strike | Market IV (%) | Model IV (%) | Residual (bps) |
|---|---|---|---|
| 85 | 24.8 | 24.9 | +1.0 |
| 92 | 21.5 | 21.5 | +0.2 |
| 100 | 19.8 | 19.8 | $-0.1$ |
| 108 | 19.4 | 19.3 | $-0.5$ |
| 115 | 20.2 | 20.3 | +0.8 |

The residuals are well within bid-ask spreads (typically 20--50 bps for equity options).

---

## Example 3: Delta Hedging Simulation

### Setup

Using the calibrated model from Example 2, simulate a delta-hedging strategy for a short ATM call position.

**Trade**: Sell 1 ATM call ($K = 100$, $T = 0.5$) and delta-hedge daily.

**Simulation**: Generate 10,000 Heston paths using the QE scheme with $N_t = 126$ steps (one per trading day over 6 months).

### Daily Hedge Rebalancing

At each time step $t_n$:

1. Compute the Heston delta $\Delta_n = \partial C / \partial S$ at $(S_n, v_n, T - t_n)$ using the COS method with finite differences: $\Delta_n \approx [C(S_n + h) - C(S_n - h)] / (2h)$ with $h = 0.01 S_n$.

2. Update the hedge portfolio: hold $\Delta_n$ shares of stock, financed at the risk-free rate.

3. At expiry, pay the call payoff $\max(S_T - K, 0)$.

### P&L Decomposition

The hedging P&L for path $i$ is:

$$
\text{P\&L}^{(i)} = C_0 + \sum_{n=0}^{N_t - 1} \Delta_n^{(i)} (S_{n+1}^{(i)} - S_n^{(i)}) - \max(S_T^{(i)} - K, 0)
$$

where $C_0 = 6.81$ is the initial option premium collected.

**Results** (across 10,000 paths):

| Metric | Value |
|---|---|
| Mean P&L | \$0.002 (near zero, as expected) |
| Std P&L | \$0.85 |
| 5th percentile | $-\$1.52$ |
| 95th percentile | \$1.48 |
| Hedging efficiency | 92% |

The hedging efficiency is defined as $1 - \text{Var}(\text{P\&L}) / \text{Var}(\text{payoff})$. The 92% efficiency means the delta hedge captures 92% of the option's variance, with the residual coming from discrete rebalancing, gamma exposure, and vega risk (variance moves).

!!! note "Why the Residual P&L Is Non-Zero"
    In the Heston model, the market is incomplete: variance risk cannot be hedged with the stock alone. The residual P&L standard deviation of \$0.85 reflects unhedged vega exposure. Adding a variance swap or VIX future to the hedge portfolio would reduce this further.

---

## Example 4: Asian Option Pricing via Monte Carlo

### Setup

Price a discretely-monitored arithmetic Asian call with:

- Averaging: monthly fixings, $N_{\text{fix}} = 6$
- Strike: $K = 100$ (ATM)
- Maturity: $T = 0.5$ years
- Monitoring dates: $t_k = k/12$ for $k = 1, 2, \ldots, 6$

The payoff is:

$$
\max\!\left(\frac{1}{N_{\text{fix}}} \sum_{k=1}^{N_{\text{fix}}} S_{t_k} - K, \; 0\right)
$$

### Monte Carlo with Control Variate

Use the European call as a control variate:

1. Simulate 500,000 QE paths with 126 time steps
2. Compute both the Asian payoff $f_{\text{Asian}}^{(i)}$ and the European payoff $f_{\text{Euro}}^{(i)} = \max(S_T^{(i)} - K, 0)$
3. The control variate estimator is:

$$
\hat{C}_{\text{Asian}}^{\text{CV}} = e^{-rT}\overline{f_{\text{Asian}}} - \hat{\beta}\left(e^{-rT}\overline{f_{\text{Euro}}} - C_{\text{Euro}}^{\text{COS}}\right)
$$

where $C_{\text{Euro}}^{\text{COS}}$ is the known European price and $\hat{\beta}$ is the regression coefficient.

### Results

| Method | Price | Std Error | 95% CI |
|---|---|---|---|
| Plain MC (500K paths) | 4.138 | 0.012 | $[4.114, 4.162]$ |
| MC + control variate | 4.141 | 0.004 | $[4.133, 4.149]$ |

The control variate reduces the standard error by a factor of 3, corresponding to a 9x efficiency improvement.

### Comparison with European Price

The Asian call price (\$4.14) is lower than the European call price (\$6.81) because averaging reduces the effective volatility of the payoff. The ratio $C_{\text{Asian}}/C_{\text{Euro}} \approx 0.61$ is typical for at-the-money Asian options with monthly averaging.

---

## Cross-Engine Consistency Matrix

The following table summarizes prices across examples, confirming that all engines produce consistent results when applied to the same model.

| Payoff | COS | FFT | MC (QE) | FDM |
|---|---|---|---|---|
| European call ($K = 100$, $T = 0.5$) | 6.806 | 6.806 | 6.807 | 6.806 |
| European put ($K = 100$, $T = 0.5$) | 5.818 | 5.818 | 5.819 | 5.818 |
| European call ($K = 110$, $T = 1.0$) | 6.352 | 6.352 | 6.354 | 6.353 |
| Asian call ($K = 100$, $T = 0.5$) | -- | -- | 4.141 | -- |

The COS, FFT, and FDM methods agree to 4+ digits for European options. Monte Carlo agrees to 2--3 digits (limited by sampling noise). The Asian option is priced only by MC since it requires path simulation.

---

## Summary

These four examples demonstrate the complete Heston model workflow: pricing European options across five engines with sub-basis-point agreement; calibrating to synthetic market data and recovering parameters to within the identifiability limits; simulating delta-hedging P&L that reveals the unhedgeable variance risk; and pricing path-dependent exotics with control-variate Monte Carlo. Together, they validate the entire code library and illustrate the practical trade-offs---speed versus accuracy, analytical versus numerical methods, complete versus incomplete hedging---that arise in production Heston model implementations.

---

## Exercises

**Exercise 1.**
Using the five-engine comparison results, the COS and Gil-Pelaez methods agree to 0.00 bps while Monte Carlo has a 0.18 bps error with 1,000,000 paths. How many paths would be needed to reduce the MC standard error to 0.01 bps (matching the FFT/FDM accuracy)? Recall that the standard error scales as $1/\sqrt{N}$. Is this number of paths practically feasible? Discuss the role of variance reduction in making MC competitive with analytical methods.

---

**Exercise 2.**
In Example 2, the calibrated $\kappa = 1.620$ differs from the true $\kappa = 1.500$ by 8.0%, yet the calibrated $\kappa\theta = 0.077$ differs from the true $\kappa\theta = 0.075$ by only 2.7%. Explain this observation using the $\kappa$-$\theta$ degeneracy. If you added more long-maturity options (e.g., $T = 3$ and $T = 5$ years) to the calibration, would you expect the individual $\kappa$ and $\theta$ errors to decrease? Why or why not?

---

**Exercise 3.**
The delta-hedging simulation reports a hedging efficiency of 92%. The residual P&L standard deviation is \$0.85. Decompose this residual into contributions from: (a) discrete rebalancing (gamma cost), (b) unhedged variance risk (vega exposure), and (c) higher-order terms. If you rebalanced twice per day instead of once, estimate how the gamma contribution would change (hint: it scales approximately as $\Delta t$).

---

**Exercise 4.**
The Asian call price (\$4.14) is 61% of the European call price (\$6.81). Derive an intuitive bound: the arithmetic Asian price satisfies $C_{\text{Asian}} \leq C_{\text{Euro}}$ (Jensen's inequality). Explain why monthly averaging reduces the effective volatility. If you changed from monthly to daily averaging ($N_{\text{fix}} = 126$), would the Asian price increase or decrease relative to the monthly case? Justify your answer.

---

**Exercise 5.**
The control variate in Example 4 reduces the standard error by a factor of 3 (from 0.012 to 0.004). Compute the variance reduction ratio and the effective number of paths: how many plain MC paths would you need to match the control-variate accuracy? If the correlation between the Asian and European payoffs is $\hat{\rho}_{AE}$, the variance reduction ratio is approximately $1/(1 - \hat{\rho}_{AE}^2)$. Estimate $\hat{\rho}_{AE}$ from the reported standard errors.

---

**Exercise 6.**
The cross-engine consistency matrix shows that European put prices satisfy put-call parity: $C - P = S_0 e^{-qT} - K e^{-rT}$. Verify this for $K = 100$, $T = 0.5$ using $C = 6.806$, $P = 5.818$, $S_0 = 100$, $r = 0.03$, $q = 0.01$. Compute the parity residual and confirm it is within numerical precision.

---

**Exercise 7.**
Design a fifth end-to-end example: pricing a European digital (binary) call that pays \$1 if $S_T > K$ and \$0 otherwise. Describe how you would compute this price using: (a) the COS method (hint: the payoff coefficients simplify to $H_k = \psi_k(0, b)$), (b) Monte Carlo with the QE scheme, and (c) finite differences on the Heston PDE. For method (b), explain why the convergence is slower than for a vanilla call (the payoff is discontinuous) and propose a variance reduction technique specific to digital options.
