# Comparison of Fourier Methods

The three Fourier pricing methods developed in this chapter---COS, Carr--Madan FFT, and Lewis integration---all exploit the characteristic function to compute European option prices, but they differ fundamentally in their mathematical approach, computational cost, accuracy profile, and ease of implementation. Choosing the right method depends on whether the goal is pricing a single option, pricing across a strike grid, calibrating a model, computing Greeks, or recovering the risk-neutral density. This section provides a systematic comparison across all relevant dimensions, supported by numerical benchmarks.

!!! info "Prerequisites"
    - [COS Pricing Formula](../cos_method/cos_pricing_formula.md)
    - [Carr--Madan FFT Method](carr_madan_fft.md)
    - [Lewis Integration Formula](lewis_integration_formula.md)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Compare the three methods along dimensions of speed, accuracy, and ease of use
    2. Select the appropriate method for a given application
    3. Understand the parameter sensitivity of each method
    4. Interpret numerical benchmark results
    5. Identify hybrid strategies that combine methods

---

## Mathematical Structure Comparison

The three methods represent different decompositions of the same pricing integral $V = e^{-rT}\int \Phi(x)f(x)\,dx$:

| Method | Representation | Key idea |
|---|---|---|
| COS | $V = e^{-rT}\sum_{k=0}^{N-1}{}' F_k V_k$ | Expand density in cosine series, integrate against payoff analytically |
| Carr--Madan | $C(k) = \frac{e^{-\alpha k}}{\pi}\int_0^\infty e^{-iuk}\psi_T(u)\,du$ via FFT | Fourier transform of damped call, evaluated via FFT |
| Lewis | $C = S_0 - \frac{\sqrt{S_0K}e^{-rT/2}}{\pi}\int_0^\infty \frac{\text{Re}[\cdots]}{u^2+1/4}\,du$ | Contour integral along critical line |

All three require the characteristic function as input. They differ in how many times $\phi$ is evaluated, at what arguments (real vs complex), and how the results are assembled into prices.

---

## Speed Comparison

!!! note "Computational Complexity"

    | Method | Cost for 1 strike | Cost for $M$ strikes | Cost for $N_{\text{grid}}$ strikes |
    |---|---|---|---|
    | COS | $O(N_{\text{cos}})$ CF evals + $O(N_{\text{cos}})$ arithmetic | $O(N_{\text{cos}})$ CF evals + $O(MN_{\text{cos}})$ arithmetic | Same as $M$ strikes |
    | Carr--Madan FFT | $O(N_{\text{fft}}\log N_{\text{fft}})$ | Same (all strikes free) | $O(N_{\text{fft}}\log N_{\text{fft}})$ |
    | Lewis | $O(M_{\text{quad}})$ CF evals | $O(M \cdot M_{\text{quad}})$ CF evals | $O(N_{\text{grid}}\cdot M_{\text{quad}})$ |

Key observations:

1. **Single strike:** COS is fastest ($N \approx 64$--$128$ CF evaluations), Lewis is second ($M \approx 100$--$200$), Carr--Madan is slowest ($N \approx 4096$).

2. **Dense strike grid:** Carr--Madan dominates because all $N$ strikes come from a single FFT. COS must recompute payoff coefficients for each strike (though density coefficients are shared). Lewis must redo the entire integral for each strike.

3. **Calibration (many strikes, many parameter sets):** Carr--Madan is the standard choice because each parameter proposal produces all strike prices simultaneously.

---

## Accuracy Comparison

!!! example "Accuracy Benchmark: Heston Model"
    Parameters: $S_0 = 100$, $K = 100$, $r = 0.05$, $T = 1$, $\kappa = 1.5$, $\theta = 0.04$, $\sigma_v = 0.3$, $\rho = -0.7$, $v_0 = 0.04$.

    Reference price: $V_{\text{ref}} = 10.2351$ (computed by Richardson-extrapolated high-order quadrature).

    | Method | Parameters | Price | Error | Time |
    |---|---|---|---|---|
    | COS | $N = 64$, $L = 10$ | 10.2351 | $\approx 10^{-7}$ | $\approx 0.01$ ms |
    | COS | $N = 128$, $L = 10$ | 10.2351 | $\approx 10^{-11}$ | $\approx 0.02$ ms |
    | Carr--Madan (trap.) | $N = 4096$, $\eta = 0.25$, $\alpha = 1.5$ | 10.2351 | $\approx 10^{-4}$ | $\approx 0.5$ ms |
    | Carr--Madan (Simps.) | $N = 4096$, $\eta = 0.25$, $\alpha = 1.5$ | 10.2351 | $\approx 10^{-6}$ | $\approx 0.5$ ms |
    | Lewis (Gauss) | $M = 100$ | 10.2351 | $\approx 10^{-10}$ | $\approx 0.05$ ms |
    | Lewis (Gauss) | $M = 200$ | 10.2351 | $\approx 10^{-14}$ | $\approx 0.1$ ms |

The COS method achieves the highest accuracy per CF evaluation due to its exponential convergence. The Lewis formula achieves very high accuracy with moderate quadrature points. Carr--Madan has the lowest accuracy per evaluation but compensates by pricing all strikes at once.

---

## Parameter Sensitivity

Each method has parameters that affect accuracy and must be chosen appropriately:

| Method | Parameters | Sensitivity |
|---|---|---|
| COS | $N$ (terms), $[a,b]$ (truncation) | Robust: $N = 128$ and cumulant-based $[a,b]$ work universally |
| Carr--Madan | $\alpha$ (damping), $\eta$ (spacing), $N$ (grid size) | Sensitive: $\alpha$ must satisfy moment condition; $\eta$ and $N$ trade off resolution vs accuracy |
| Lewis | $M$ (quadrature points), $U$ (truncation) | Robust: $M = 200$ works universally; $U$ determined by CF decay |

!!! warning "Carr--Madan Parameter Tuning"
    The Carr--Madan method is the most parameter-sensitive:

    - **$\alpha$ too small:** integrand decays slowly, requiring large $\eta N$
    - **$\alpha$ too large:** CF evaluation near explosion boundary, numerical instability
    - **$\eta$ too large:** discretization error dominates
    - **$N$ too small:** strike grid is coarse, interpolation needed

    The COS and Lewis methods require minimal tuning by comparison.

---

## Ease of Implementation

| Method | Implementation complexity | Key challenge |
|---|---|---|
| COS | Low | Computing payoff coefficients $V_k$ analytically |
| Carr--Madan | Medium | FFT setup, Simpson weights, grid alignment |
| Lewis | Low | Choosing quadrature rule for semi-infinite integral |

The COS method is the simplest to implement: evaluate $\phi$ at $N$ points, compute $V_k$ from closed-form expressions, sum. The Lewis formula requires a good quadrature library for semi-infinite integrals. Carr--Madan requires FFT, careful grid alignment, and Simpson weights.

---

## Greeks Computation

Computing sensitivities (Greeks) is important for hedging and risk management:

| Method | Greeks approach | Efficiency |
|---|---|---|
| COS | Differentiate the pricing formula analytically w.r.t. parameters | Excellent: $F_k$ and $V_k$ differentiate cleanly |
| Carr--Madan | Differentiate $\psi_T(u)$ w.r.t. parameters, apply FFT | Good: single FFT gives Greeks at all strikes |
| Lewis | Finite differences or AD on the quadrature | Good: simple but requires re-evaluation |

The COS method is particularly well-suited for Greeks because the density coefficients $F_k$ depend on the CF (and hence on model parameters) in a differentiable way, while the payoff coefficients $V_k$ depend on the strike in a simple analytic form. Delta, gamma, vega, and theta can all be computed by differentiating $F_k$ or $V_k$.

---

## Application-Specific Recommendations

!!! tip "Method Selection Guide"

    | Application | Recommended method | Reason |
    |---|---|---|
    | Price one option | COS ($N = 128$) | Fastest, most accurate |
    | Price options at 5--20 strikes | COS (reuse $F_k$) or Lewis | COS shares CF evaluations; Lewis is simple |
    | Calibration (100+ strikes) | Carr--Madan FFT | All strikes from one FFT |
    | Density recovery | COS | Natural output of the method |
    | Greeks (single option) | COS or Lewis | COS: analytic differentiation; Lewis: AD-friendly |
    | Greeks (strike grid) | Carr--Madan | FFT gives Greeks at all strikes |
    | Model validation | COS density recovery + Lewis single-point check | Complementary diagnostics |

---

## Hybrid Strategies

In practice, many implementations combine methods:

1. **Calibration with Carr--Madan, pricing with COS.** Use the FFT method to calibrate model parameters against market data (exploiting the strike-grid efficiency), then switch to COS for production pricing and Greeks (exploiting the single-option accuracy).

2. **Lewis for validation, COS for production.** Use the Lewis formula as an independent check on COS prices during development, then deploy COS in production.

3. **COS for short maturities, Carr--Madan for long.** Short-maturity options have concentrated densities requiring many COS terms; long-maturity options have diffuse densities that are well-handled by FFT.

---

## Summary

| Dimension | COS | Carr--Madan FFT | Lewis |
|---|---|---|---|
| Best for | Single option, Greeks | Strike grid, calibration | Single option, validation |
| Convergence | Exponential | Algebraic ($O(\eta^2)$ or $O(\eta^4)$) | High-order quadrature |
| Parameters | $N$, $[a,b]$ (easy) | $\alpha$, $\eta$, $N$ (sensitive) | $M$, $U$ (easy) |
| CF evaluations | $N \approx 64$--$128$ | $N \approx 4096$ | $M \approx 100$--$200$ |
| Strike grid | One at a time | All at once | One at a time |
| Greeks | Analytic differentiation | FFT-based | Finite differences / AD |
| Implementation | Simple | Moderate | Simple |

**The COS method offers the best accuracy-per-cost ratio for individual option pricing and Greeks, Carr--Madan FFT is optimal for calibration over dense strike grids, and the Lewis formula provides the simplest parameter-free approach for single-option pricing and validation.**

---

## Exercises

**Exercise 1.** For pricing a single ATM European call under the Heston model, compare the number of characteristic function evaluations required by each method: COS with $N = 128$, Carr-Madan FFT with $N = 4096$, and Lewis with $M = 200$. Compute the ratio of CF evaluations for Carr-Madan vs COS and explain why COS is preferred for single-option pricing.

---

**Exercise 2.** A calibration problem requires pricing options at 200 strikes for each of 500 parameter proposals. For each method, compute the total number of CF evaluations: (a) COS with $N = 128$ (CF evaluations shared across strikes), (b) Carr-Madan FFT with $N = 4096$ (all strikes from one FFT), (c) Lewis with $M = 200$ (independent integral per strike). Which method minimizes the total CF evaluation cost?

---

**Exercise 3.** The accuracy benchmark shows COS with $N = 128$ achieving $10^{-11}$ error, while Carr-Madan with Simpson's rule achieves $10^{-6}$ error using 4096 CF evaluations. Compute the "accuracy per CF evaluation" for each method (defined as $-\log_{10}(\text{error})/N_{\text{CF}}$). What does this metric tell you about the efficiency of exponential vs algebraic convergence?

---

**Exercise 4.** The Lewis formula has no free parameters to tune, while Carr-Madan requires choosing $\alpha$, $\eta$, and $N$. Describe a practical scenario where poor parameter choices in Carr-Madan lead to significant pricing errors. Specifically, explain what happens when (a) $\alpha$ is too close to the explosion boundary of the Heston CF, and (b) $\eta$ is too large.

---

**Exercise 5.** For computing delta ($\partial V/\partial S$) under the COS method, the density coefficients $F_k$ depend on $S_0$ through $\phi$, while the payoff coefficients $V_k$ depend on $K/S_0$ through the log-moneyness. Explain how to compute delta analytically by differentiating the COS formula. Compare this to the Lewis approach, where delta requires re-evaluating the quadrature with a modified integrand.

---

**Exercise 6.** Design a hybrid pricing workflow for a trading desk that needs: (a) daily model calibration against 500 market options, (b) real-time pricing of individual exotic options, (c) Greeks computation for the top 50 positions. Assign the appropriate Fourier method (COS, Carr-Madan, or Lewis) to each task, justify your choices, and estimate the total computation time assuming each CF evaluation takes 1 microsecond.
