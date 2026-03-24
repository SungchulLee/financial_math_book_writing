# Calibration to the Implied Volatility Surface

Calibrating the Heston model to a full implied volatility surface is the central practical task of this chapter. The previous sections developed the ingredients --- the objective function, the differential evolution optimizer, and the parameter stability analysis --- and this section assembles them into a complete calibration workflow. We walk through the end-to-end process on a realistic equity implied volatility surface, demonstrate the typical fit quality achievable by the five-parameter Heston model, and perform a residual analysis that reveals the model's systematic limitations.

!!! info "Prerequisites"
    - [Objective Function Design](objective_function_design.md) (vega-weighted loss)
    - [Differential Evolution](differential_evolution.md) (global optimization)
    - [Joint Calibration Across Maturities](joint_calibration_across_maturities.md) (multi-maturity fitting)
    - [Parameter Stability](parameter_stability.md) (day-to-day consistency)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Execute a complete Heston calibration from raw implied volatility data to calibrated parameters
    2. Construct the vega-weighted objective function from market data
    3. Run a hybrid DE + local optimization workflow and interpret convergence diagnostics
    4. Assess calibration quality through IVRMSE, maximum error, and residual patterns
    5. Identify systematic model misfit (wing errors, term structure errors) and their parameter-space origins

---

## The Calibration Workflow

### Input Data

The market provides European option implied volatilities $\{\sigma_i^{\text{mkt}}\}_{i=1}^M$ at strikes $K_i$ and maturities $T_i$, together with the spot price $S_0$, risk-free rate curve $r(T)$, and dividend yield curve $q(T)$.

### End-to-End Steps

The calibration proceeds as follows.

**Step 1: Data preparation.**

- Convert all strikes to log-moneyness $m_i = \ln(K_i / F_i)$ where $F_i = S_0 e^{(r_i - q_i)T_i}$ is the forward price
- Compute Black-Scholes vegas $\mathcal{V}_i = S_0 e^{-q_i T_i}\sqrt{T_i}\,\phi(d_{1,i})$ at the market implied volatilities
- Set vega weights $w_i = 1/\mathcal{V}_i^2$
- Filter out options with very small vega ($\mathcal{V}_i < \epsilon$, typically 0.01) to avoid numerical instability from near-zero denominators

**Step 2: Define the objective function.**

$$
\mathcal{L}(\Theta) = \sum_{i=1}^M w_i \left[C_i^{\text{Heston}}(\Theta) - C_i^{\text{mkt}}\right]^2
$$

where $C_i^{\text{Heston}}(\Theta)$ is computed via the COS method or Carr-Madan FFT for all $M$ options simultaneously.

**Step 3: Global search (DE).**

- Bounds: $v_0 \in [0.001, 1]$, $\kappa \in [0.01, 10]$, $\theta \in [0.001, 1]$, $\xi \in [0.01, 3]$, $\rho \in [-0.99, 0.99]$
- Population size $N_p = 50$, mutation $F = 0.8$, crossover $CR = 0.9$
- Run for 200 generations
- Include yesterday's parameters in the initial population (warm start)

**Step 4: Local refinement.**

Starting from $\Theta_{\text{DE}}$, run Nelder-Mead (or Levenberg-Marquardt) to convergence.

**Step 5: Validation.**

- Compute model implied volatilities at all calibration strikes
- Evaluate IVRMSE, maximum error, and residual patterns
- Check parameter constraints (Feller condition, positivity)
- Compare with previous day's calibration for stability

---

## Worked Example: S&P 500 Implied Volatility Surface

### Market Data

Consider a representative S&P 500 implied volatility surface with $S_0 = 4500$, $r = 4.5\%$, $q = 1.5\%$. The surface spans 5 maturities and 9 strikes per maturity (45 options total).

| | 80% | 85% | 90% | 95% | 100% | 105% | 110% | 115% | 120% |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1M** | 28.5 | 25.2 | 22.4 | 20.1 | 18.5 | 17.8 | 17.5 | 17.8 | 18.6 |
| **3M** | 26.8 | 24.1 | 21.8 | 20.0 | 18.8 | 18.1 | 17.8 | 18.0 | 18.5 |
| **6M** | 25.4 | 23.2 | 21.3 | 19.8 | 18.8 | 18.2 | 18.0 | 18.1 | 18.5 |
| **1Y** | 24.2 | 22.4 | 20.9 | 19.7 | 18.9 | 18.4 | 18.2 | 18.3 | 18.6 |
| **2Y** | 23.5 | 22.0 | 20.7 | 19.6 | 19.0 | 18.6 | 18.4 | 18.5 | 18.8 |

All values are in percent. Moneyness is $K/F$ as a percentage.

### Calibration Results

The hybrid DE + Nelder-Mead optimizer converges after approximately 12,000 objective function evaluations (8 seconds on a modern laptop). The calibrated parameters are:

| Parameter | Value | Interpretation |
|---|---|---|
| $v_0$ | 0.0342 | Current variance (18.5% vol) |
| $\kappa$ | 2.15 | Mean-reversion half-life $\approx$ 4 months |
| $\theta$ | 0.0361 | Long-run variance (19.0% vol) |
| $\xi$ | 0.48 | Vol-of-vol |
| $\rho$ | $-0.72$ | Strong negative leverage effect |

**Feller ratio**: $2\kappa\theta / \xi^2 = 2(2.15)(0.0361)/(0.48)^2 = 0.674 < 1$. The Feller condition is violated, meaning the variance process touches zero with positive probability. This is typical for equity-calibrated Heston parameters.

### Fit Quality

The model implied volatilities and residuals (model $-$ market, in basis points) are:

| | 80% | 85% | 90% | 95% | 100% | 105% | 110% | 115% | 120% |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **1M** | $-85$ | $-42$ | $-15$ | $+5$ | $+12$ | $+8$ | $-10$ | $-45$ | $-95$ |
| **3M** | $-55$ | $-25$ | $-8$ | $+3$ | $+8$ | $+5$ | $-5$ | $-22$ | $-50$ |
| **6M** | $-35$ | $-15$ | $-3$ | $+2$ | $+5$ | $+3$ | $-2$ | $-12$ | $-30$ |
| **1Y** | $-20$ | $-8$ | $+1$ | $+3$ | $+3$ | $+2$ | $+1$ | $-5$ | $-15$ |
| **2Y** | $-10$ | $-3$ | $+2$ | $+3$ | $+2$ | $+1$ | $+1$ | $-2$ | $-8$ |

### Calibration Quality Metrics

| Metric | Value |
|---|---|
| IVRMSE | 32 bps |
| Maximum absolute error | 95 bps (1M, 80% moneyness) |
| Mean absolute error | 18 bps |
| ATM average error | 6 bps |
| Number of options | 45 |

---

## Residual Analysis

### Systematic Patterns

The residual table reveals a characteristic pattern that is **universal** to Heston calibration on equity surfaces.

**Wing underpricing at short maturities.** The largest errors (up to 95 bps) occur at extreme moneyness for the shortest maturity (1M). The Heston model, being a pure diffusion model, cannot generate the steep short-maturity smile observed in the market. This is the well-known "short-maturity smile problem" that motivates adding jumps (Bates model).

**Symmetric wing errors.** The errors are approximately symmetric in the wings --- both deep OTM puts and deep OTM calls are underpriced. This indicates that the market distribution has heavier tails than the Heston model produces with a single variance factor.

**Error magnitude decreases with maturity.** The 2Y residuals are 5--10 times smaller than the 1M residuals. Over longer horizons, the diffusive dynamics of Heston better approximate the return distribution, as the central limit theorem smooths out the impact of jumps.

!!! note "Theorem (Short-Maturity Smile Asymptotics)"
    For a pure stochastic volatility model (no jumps), the ATM implied volatility skew satisfies:

    $$
    \frac{\partial\sigma_{\text{imp}}}{\partial m}\bigg|_{m=0} = O(T^{-1/2}) \quad \text{as } T \to 0
    $$

    where $m = \ln(K/F)$ is log-moneyness. Market data typically show skew behavior closer to $O(T^{-0.6})$ to $O(T^{-0.8})$ at very short maturities, indicating the presence of jump risk or rough volatility.

### Parameter Sensitivity of Residual Patterns

| Residual pattern | Heston parameter responsible | Possible fix |
|---|---|---|
| Wing underpricing (short $T$) | Structural (no jumps) | Add jumps (Bates) |
| Asymmetric skew error | $\rho$ too constrained | Double Heston (two $\rho$'s) |
| Term structure misfit | Single $\kappa$ | Double Heston (two $\kappa$'s) |
| Curvature too flat | $\xi$ compromised | Additional variance factor |

---

## Effect of Objective Function Choice

The choice of error metric materially affects which part of the surface is fitted best.

### Comparison of Metrics

| Metric | IVRMSE (bps) | Max ATM error (bps) | Max wing error (bps) |
|---|:---:|:---:|:---:|
| Uniform price weights | 55 | 3 | 180 |
| Vega-weighted price | 32 | 6 | 95 |
| Direct IV minimization | 30 | 8 | 88 |

Uniform price weights produce the worst overall fit because they focus on ITM options (large prices, large vega) at the expense of OTM options. Vega weighting approximates the direct IV minimization at lower computational cost and is the standard choice.

---

## Convergence Diagnostics

### DE Convergence

Monitor the following during the DE run:

| Generation | Best $\mathcal{L}$ | Worst $\mathcal{L}$ | $v_0$ | $\kappa$ | $\theta$ | $\xi$ | $\rho$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 4.2e-2 | 8.1e-1 | 0.028 | 5.2 | 0.052 | 1.8 | $-0.45$ |
| 50 | 1.8e-3 | 2.5e-2 | 0.035 | 2.8 | 0.039 | 0.55 | $-0.68$ |
| 100 | 4.5e-4 | 3.1e-3 | 0.034 | 2.2 | 0.036 | 0.49 | $-0.71$ |
| 200 | 2.8e-4 | 5.2e-4 | 0.034 | 2.15 | 0.036 | 0.48 | $-0.72$ |

The population converges within 100--150 generations. The spread between best and worst narrows by three orders of magnitude, confirming that the population has collapsed to a single basin.

### Local Refinement

Starting from the DE solution, Nelder-Mead reduces $\mathcal{L}$ from $2.8 \times 10^{-4}$ to $2.6 \times 10^{-4}$ in 35 iterations. The parameter changes are in the fourth significant digit, confirming that DE located the correct basin.

---

## Comparison with Extended Models

The residual analysis motivates considering models beyond Heston.

| Model | Parameters | IVRMSE (bps) | Max error (bps) | Calibration time |
|---|:---:|:---:|:---:|---|
| Heston | 5 | 32 | 95 | 8 seconds |
| Bates (Heston + jumps) | 8 | 18 | 45 | 25 seconds |
| Double Heston | 10 | 12 | 28 | 45 seconds |
| Bates + double Heston | 13 | 8 | 18 | 90 seconds |

Each extension reduces the IVRMSE at the cost of more parameters and longer calibration time. The diminishing returns beyond double Heston suggest that 10--13 parameters are sufficient for most practical purposes.

!!! warning "Overfitting Risk"
    With 13 parameters and 45 data points, the ratio of data to parameters is only 3.5:1. Regularization is essential to prevent overfitting and ensure parameter stability. A rule of thumb: the number of options should be at least 5--10 times the number of parameters.

---

## Practical Recommendations

!!! tip "Calibration Best Practices"
    1. **Start with vega-weighted objective**: It provides the best balance between fit quality and computational cost.
    2. **Use hybrid DE + local**: DE escapes local minima; local search achieves full precision.
    3. **Warm-start from yesterday**: Include previous parameters in the DE population.
    4. **Filter extreme wings**: Exclude options with $|m| > 0.5$ (50% OTM) where Heston systematically fails and the data may be stale.
    5. **Monitor residual patterns**: Systematic wing errors indicate model limitations, not calibration failure.
    6. **Check Feller ratio**: Report $2\kappa\theta/\xi^2$ but do not enforce Feller > 1 (most equity calibrations violate it).
    7. **Log everything**: Store parameters, objective value, residuals, and convergence history for audit and stability analysis.

---

## Summary

Heston calibration to a full implied volatility surface follows a systematic workflow: prepare market data with vega weights, run differential evolution for global search, refine with a local optimizer, and validate through residual analysis. On a representative S&P 500 surface, the five-parameter Heston model achieves an IVRMSE of approximately 30--35 bps, with the largest errors concentrated in the short-maturity wings where the absence of jumps limits the model's ability to reproduce steep smiles. The residual pattern is diagnostic: symmetric wing underpricing calls for jumps (Bates), term structure misfit calls for additional variance factors (double Heston), and both can be addressed by extending the model at the cost of more parameters and longer calibration times. The vega-weighted objective function, combined with hybrid global-local optimization and warm-starting, provides the standard industry approach to Heston calibration.

---

## Further Reading

- Christoffersen, P., Heston, S., and Jacobs, K. (2009). "The shape and term structure of the index option smear." *Management Science*, 55(12), 1914--1932.
- Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*. Wiley.
- Cont, R. and Tankov, P. (2004). *Financial Modelling with Jump Processes*. CRC Press.

---

## Exercises

**Exercise 1.**
Consider a market with $S_0 = 5000$, $r = 5\%$, and $q = 2\%$. Compute the forward price $F$ for maturities $T = 0.25$, $T = 0.5$, and $T = 1.0$. Then convert the strikes $K = 4500, 5000, 5500$ to log-moneyness $m = \ln(K/F)$ for each maturity. Explain why the same strike corresponds to different log-moneyness values at different maturities.

---

**Exercise 2.**
A Heston calibration yields parameters $v_0 = 0.04$, $\kappa = 1.5$, $\theta = 0.05$, $\xi = 0.60$, and $\rho = -0.75$. Compute the Feller ratio $2\kappa\theta / \xi^2$. Is the Feller condition satisfied? Discuss why equity-calibrated Heston parameters commonly violate this condition, and explain the practical consequences for the variance process.

---

**Exercise 3.**
Suppose you calibrate the Heston model using uniform price weights and observe that the IVRMSE is 55 bps, with most of the error concentrated in OTM put options. Explain mathematically why uniform price weights bias the fit toward ITM options. Derive the relationship between price errors and implied volatility errors using the vega approximation:

$$
C^{\text{model}} - C^{\text{mkt}} \approx \mathcal{V}\,(\sigma^{\text{model}}_{\text{imp}} - \sigma^{\text{mkt}}_{\text{imp}})
$$

and show that minimizing $\sum_i (C_i^{\text{model}} - C_i^{\text{mkt}})^2$ with uniform weights effectively places weight proportional to $\mathcal{V}_i^2$ on implied volatility errors.

---

**Exercise 4.**
Given the residual table in the worked example, verify the reported IVRMSE of 32 bps. The IVRMSE is defined as:

$$
\text{IVRMSE} = \sqrt{\frac{1}{M}\sum_{i=1}^M (\sigma_i^{\text{model}} - \sigma_i^{\text{mkt}})^2}
$$

Using the residuals (in basis points) for all 45 options, compute the IVRMSE explicitly. Also compute the mean absolute error and confirm that the maximum absolute error is 95 bps.

---

**Exercise 5.**
A differential evolution run with population size $N_p = 50$ and 200 generations requires $50 \times 200 = 10{,}000$ objective function evaluations (plus the initial population). If each evaluation requires pricing 45 options via the COS method with $N = 128$ cosine terms, estimate the total number of characteristic function evaluations performed during the entire calibration. Discuss how vectorization across strikes and maturities reduces the wall-clock time compared to a naive loop implementation.

---

**Exercise 6.**
The residual analysis shows that short-maturity wing errors are much larger than long-maturity errors. Using the short-maturity smile asymptotics result:

$$
\frac{\partial\sigma_{\text{imp}}}{\partial m}\bigg|_{m=0} = O(T^{-1/2}) \quad \text{as } T \to 0
$$

explain why the ATM skew steepens as $T \to 0$ in any pure stochastic volatility model. If the market skew behaves as $O(T^{-0.7})$, argue that no adjustment of the Heston parameters $(\kappa, \theta, \xi, \rho)$ can match the market at very short maturities. What model extension would you recommend?

---

**Exercise 7.**
You are tasked with calibrating the Heston model daily for a trading desk. On day 1, the calibrated parameters are $\Theta_1 = (0.034, 2.15, 0.036, 0.48, -0.72)$. On day 2, without warm-starting, the optimizer finds $\Theta_2 = (0.038, 3.80, 0.034, 0.62, -0.65)$, which achieves a similar objective function value. Compute the relative change in each parameter. Explain why such parameter instability is problematic for a hedging desk that computes Greeks from the model, and describe how warm-starting the DE population with $\Theta_1$ helps mitigate this issue.
