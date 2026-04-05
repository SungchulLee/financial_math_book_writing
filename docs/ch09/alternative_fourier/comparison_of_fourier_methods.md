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

??? success "Solution to Exercise 1"
    The number of CF evaluations per pricing call for each method:

    - **COS with $N = 128$:** The method evaluates $\phi_T(k\pi/(b-a))$ for $k = 0, 1, \ldots, 127$, giving **128 CF evaluations**.
    - **Carr--Madan FFT with $N = 4096$:** The method evaluates $\phi_T(u_j - (\alpha+1)i)$ for $j = 0, 1, \ldots, 4095$, giving **4096 CF evaluations**.
    - **Lewis with $M = 200$:** The method evaluates $\phi_T(u_j - i/2)$ at 200 quadrature nodes, giving **200 CF evaluations**.

    The ratios:

    $$
    \frac{N_{\text{Carr-Madan}}}{N_{\text{COS}}} = \frac{4096}{128} = 32
    $$

    Carr--Madan requires 32 times more CF evaluations than COS for a single option. The COS method is preferred for single-option pricing because it achieves superior accuracy ($10^{-11}$ vs $10^{-6}$) with 32 times fewer CF evaluations. The Carr--Madan method "wastes" most of its CF evaluations producing prices at thousands of strikes that are not needed when only one price is required. The FFT's strength---simultaneous pricing at all grid points---becomes a liability when only a single strike is of interest.

---

**Exercise 2.** A calibration problem requires pricing options at 200 strikes for each of 500 parameter proposals. For each method, compute the total number of CF evaluations: (a) COS with $N = 128$ (CF evaluations shared across strikes), (b) Carr-Madan FFT with $N = 4096$ (all strikes from one FFT), (c) Lewis with $M = 200$ (independent integral per strike). Which method minimizes the total CF evaluation cost?

??? success "Solution to Exercise 2"
    With 200 strikes and 500 parameter proposals:

    **(a) COS with $N = 128$:** The density coefficients $F_k = \frac{2}{b-a}\text{Re}[\phi_T(k\pi/(b-a)) e^{-ika\pi/(b-a)}]$ are computed once per parameter set (128 CF evaluations) and reused for all 200 strikes. The payoff coefficients $V_k$ depend on the strike but not on $\phi_T$, so they require no CF evaluations. Total CF evaluations:

    $$
    500 \times 128 = 64{,}000
    $$

    **(b) Carr--Madan FFT with $N = 4096$:** Each parameter proposal requires one FFT pass with 4096 CF evaluations, producing prices at all grid strikes simultaneously. Total CF evaluations:

    $$
    500 \times 4096 = 2{,}048{,}000
    $$

    **(c) Lewis with $M = 200$:** Each strike requires an independent quadrature with 200 CF evaluations. The integrals cannot be shared across strikes. Total CF evaluations:

    $$
    500 \times 200 \times 200 = 20{,}000{,}000
    $$

    **Comparison:**

    | Method | Total CF evaluations |
    |---|---|
    | COS | 64,000 |
    | Carr--Madan FFT | 2,048,000 |
    | Lewis | 20,000,000 |

    The COS method minimizes the total CF evaluation cost by a factor of 32 over Carr--Madan and 312 over Lewis. This is because COS shares the CF evaluations across all 200 strikes, while Lewis shares nothing. Carr--Madan also shares across strikes (via the FFT) but evaluates the CF at 4096 points regardless of how many market strikes exist.

---

**Exercise 3.** The accuracy benchmark shows COS with $N = 128$ achieving $10^{-11}$ error, while Carr-Madan with Simpson's rule achieves $10^{-6}$ error using 4096 CF evaluations. Compute the "accuracy per CF evaluation" for each method (defined as $-\log_{10}(\text{error})/N_{\text{CF}}$). What does this metric tell you about the efficiency of exponential vs algebraic convergence?

??? success "Solution to Exercise 3"
    Define the "accuracy per CF evaluation" metric as $\eta = -\log_{10}(\text{error}) / N_{\text{CF}}$.

    **COS with $N = 128$:**

    $$
    \eta_{\text{COS}} = \frac{-\log_{10}(10^{-11})}{128} = \frac{11}{128} \approx 0.0859 \text{ digits per CF evaluation}
    $$

    **Carr--Madan (Simpson) with $N = 4096$:**

    $$
    \eta_{\text{CM}} = \frac{-\log_{10}(10^{-6})}{4096} = \frac{6}{4096} \approx 0.00146 \text{ digits per CF evaluation}
    $$

    The ratio:

    $$
    \frac{\eta_{\text{COS}}}{\eta_{\text{CM}}} = \frac{0.0859}{0.00146} \approx 58.8
    $$

    COS delivers approximately 59 times more accuracy per CF evaluation than Carr--Madan. This dramatic difference reflects the fundamental distinction between exponential and algebraic convergence:

    - **COS (exponential convergence):** Each additional CF evaluation adds a roughly constant number of accurate digits. Doubling $N$ from 64 to 128 improves accuracy from $\sim 10^{-7}$ to $\sim 10^{-11}$, gaining 4 digits with 64 extra evaluations.
    - **Carr--Madan (algebraic convergence $O(\eta^4)$):** Gaining one extra digit of accuracy requires multiplying $N$ by $10^{1/4} \approx 1.78$. The cost per digit grows as the grid is refined.

    This metric confirms that exponential convergence is vastly more efficient per evaluation, but it does not account for the FFT's ability to price multiple strikes simultaneously, which is the Carr--Madan method's true advantage.

---

**Exercise 4.** The Lewis formula has no free parameters to tune, while Carr-Madan requires choosing $\alpha$, $\eta$, and $N$. Describe a practical scenario where poor parameter choices in Carr-Madan lead to significant pricing errors. Specifically, explain what happens when (a) $\alpha$ is too close to the explosion boundary of the Heston CF, and (b) $\eta$ is too large.

??? success "Solution to Exercise 4"
    **(a) $\alpha$ too close to the explosion boundary.** In the Heston model, the CF $\phi_T(u - (\alpha+1)i)$ involves a Riccati ODE solution $D(u, T)$ with a discriminant:

    $$
    d = \sqrt{(\kappa - \rho\sigma_v(\alpha+1))^2 + \sigma_v^2(\alpha+1)((\alpha+1)-1)}
    $$

    As $\alpha + 1$ approaches the critical value $u^*$, $d$ approaches zero and $D(u, T)$ diverges. Numerically, the CF evaluation becomes unstable: small perturbations in $u$ near the explosion boundary cause the CF to oscillate wildly or produce overflow. The resulting FFT output will contain large numerical errors, leading to negative option prices or non-monotone price-strike curves. For example, with typical Heston parameters ($\sigma_v = 0.5$, $\rho = -0.7$), the explosion boundary might be $u^* \approx 4.5$, so choosing $\alpha = 3.0$ (giving $\alpha + 1 = 4.0$, close to $u^*$) would produce visible pricing errors of order $10^{-2}$ or worse.

    **(b) $\eta$ too large.** The frequency spacing $\eta$ determines the quadrature accuracy. With trapezoidal rule, the error is $O(\eta^2)$; with Simpson's rule, $O(\eta^4)$. If $\eta$ is too large (say $\eta = 1.0$ instead of $0.25$), the discretization misses oscillations in the integrand $\psi_T(u)$, leading to aliasing-like errors. Moreover, the log-strike spacing $\Delta k = 2\pi/(N\eta)$ increases: with $N = 4096$ and $\eta = 1.0$, $\Delta k = 2\pi/4096 \approx 0.00153$, which is actually finer in strike space---but the quadrature error is $(\eta/\eta_0)^4 = (1.0/0.25)^4 = 256$ times larger. For options far from ATM where the integrand oscillates more rapidly, the quadrature error can reach $10^{-2}$ or worse, rendering the prices unreliable for calibration.

---

**Exercise 5.** For computing delta ($\partial V/\partial S$) under the COS method, the density coefficients $F_k$ depend on $S_0$ through $\phi$, while the payoff coefficients $V_k$ depend on $K/S_0$ through the log-moneyness. Explain how to compute delta analytically by differentiating the COS formula. Compare this to the Lewis approach, where delta requires re-evaluating the quadrature with a modified integrand.

??? success "Solution to Exercise 5"
    The COS pricing formula is:

    $$
    V = e^{-rT} \sum_{k=0}^{N-1}{}' F_k \cdot V_k
    $$

    where the density coefficients are $F_k = \frac{2}{b-a}\text{Re}\!\left[\phi_T\!\left(\frac{k\pi}{b-a}\right) e^{-i k a\pi/(b-a)}\right]$ and the payoff coefficients for a call are:

    $$
    V_k = \frac{2}{b-a}\int_a^b (S_0 e^x - K)^+ \cos\!\left(\frac{k\pi(x-a)}{b-a}\right) dx
    $$

    To compute delta $\Delta = \partial V / \partial S_0$, note that:

    - The density coefficients $F_k$ depend on $S_0$ through the CF: $\phi_T(u) = e^{iu\ln S_0} \cdot \tilde{\phi}_T(u)$ where $\tilde{\phi}_T$ depends on model parameters but not $S_0$. So $\partial F_k / \partial S_0 = (iu/(S_0)) \cdot (\text{related term})$.
    - The payoff coefficients $V_k$ depend on $S_0$ directly through $S_0 e^x$ in the payoff and through the log-moneyness $k = \ln(K/S_0)$.

    Differentiating the COS formula:

    $$
    \Delta = e^{-rT} \sum_{k=0}^{N-1}{}' \left(\frac{\partial F_k}{\partial S_0} V_k + F_k \frac{\partial V_k}{\partial S_0}\right)
    $$

    In practice, the standard approach is to note that $F_k$ depends on $S_0$ only through the phase $e^{iu\ln S_0}$, so $\partial F_k / \partial S_0 = \frac{ik\pi}{(b-a)S_0} \cdot (\text{imaginary part term})$. The payoff coefficient derivative $\partial V_k / \partial S_0$ has a closed-form expression involving the same trigonometric integrals. Thus delta is computed analytically at the same $O(N)$ cost as the price, with no extra CF evaluations needed.

    **Lewis approach.** For the Lewis formula, delta is:

    $$
    \frac{\partial C}{\partial S_0} = 1 - \frac{e^{-rT/2}}{2\pi\sqrt{S_0 K}} \int_0^{\infty} \text{Re}\!\left[\frac{e^{-iu\ln(K/S_0)} \phi_T(u-i/2)}{u^2+1/4} \left(\frac{iu}{S_0} \cdot \frac{\partial \phi_T}{\partial S_0}\Big|_{u-i/2} \cdot \frac{1}{\phi_T(u-i/2)} + \frac{iu}{S_0}\right)\right] du
    $$

    This requires re-evaluating the quadrature with a modified integrand that includes the derivative of $\phi_T$ with respect to $S_0$. While conceptually simple, it doubles the computational work compared to the COS approach, which computes delta with no additional CF evaluations. Alternatively, finite differences ($\Delta \approx (C(S_0 + h) - C(S_0 - h))/(2h)$) require two full Lewis evaluations but are trivial to implement.

---

**Exercise 6.** Design a hybrid pricing workflow for a trading desk that needs: (a) daily model calibration against 500 market options, (b) real-time pricing of individual exotic options, (c) Greeks computation for the top 50 positions. Assign the appropriate Fourier method (COS, Carr-Madan, or Lewis) to each task, justify your choices, and estimate the total computation time assuming each CF evaluation takes 1 microsecond.

---

??? success "Solution to Exercise 6"
    **Task (a): Daily calibration against 500 market options.**

    **Recommended method: Carr--Madan FFT.**

    Calibration requires evaluating option prices at many strikes for each trial parameter set. With Carr--Madan ($N = 4096$), a single FFT call produces prices at all strikes simultaneously. Assuming 1000 optimizer iterations:

    - CF evaluations per iteration: 4096
    - Total CF evaluations: $1000 \times 4096 = 4{,}096{,}000$
    - Total CF time: $4{,}096{,}000 \times 1\,\mu\text{s} \approx 4.1\,\text{s}$
    - FFT overhead: approximately 50% of CF time $\approx 2\,\text{s}$
    - **Total calibration time: $\approx 6\,\text{s}$**

    (Note: COS with shared $F_k$ would use only $1000 \times 128 = 128{,}000$ CF evaluations ($\approx 0.13\,\text{s}$), but requires $500 \times 128 = 64{,}000$ multiplications per iteration for assembling prices. COS is actually competitive here and could be faster.)

    **Task (b): Real-time pricing of individual exotic options.**

    **Recommended method: COS.**

    For single-option pricing, COS is fastest with $N = 128$:

    - CF evaluations: 128
    - Time: $128 \times 1\,\mu\text{s} = 0.128\,\text{ms}$
    - **Latency: $< 0.2\,\text{ms}$**, well within real-time requirements

    The Lewis formula ($M = 200$, time $\approx 0.2\,\text{ms}$) is a close alternative but slightly slower.

    **Task (c): Greeks for top 50 positions.**

    **Recommended method: COS.**

    COS computes delta, gamma, vega, and theta analytically by differentiating $F_k$ and $V_k$. Each Greek requires the same $N = 128$ CF evaluations (shared with the price). For 50 positions, with 5 Greeks each:

    - CF evaluations: $50 \times 128 = 6{,}400$ (density coefficients computed once per position)
    - Greek assembly: $50 \times 5 \times 128 = 32{,}000$ multiply-add operations
    - Total CF time: $6{,}400 \times 1\,\mu\text{s} = 6.4\,\text{ms}$
    - **Total Greeks time: $< 10\,\text{ms}$**

    **Summary of total computation time:**

    | Task | Method | Time |
    |---|---|---|
    | Calibration (daily) | Carr--Madan FFT | $\approx 6\,\text{s}$ |
    | Real-time pricing (per option) | COS | $\approx 0.2\,\text{ms}$ |
    | Greeks (50 positions) | COS | $\approx 10\,\text{ms}$ |

    The hybrid workflow uses Carr--Madan's strike-grid efficiency for calibration, then switches to COS's per-option efficiency for production pricing and Greeks. The total daily computational budget is dominated by calibration at roughly 6 seconds---easily feasible for a trading desk.
