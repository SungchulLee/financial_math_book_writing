# Stability Issues


Even with smoothing, local volatility calibration can be unstable. Instability can appear as jagged $\sigma_{\text{loc}}$ surfaces, extreme values near wings, or strong sensitivity to small quote changes. This section summarizes where instability comes from and how it is managed.

---

## Structural instability in the Dupire formula


The Dupire expression

$$
\sigma_{\text{loc}}^2(T,K)
= \frac{2\left(\partial_T C + (r-q)K\partial_K C - q C\right)}
{K^2\,\partial_{KK} C}
$$


has two built-in amplifiers:

1. **Differentiation amplifies noise** (numerator and denominator).
2. **Division by curvature**: if $\partial_{KK}C$ is small, errors explode.

The curvature is typically smallest in:
- far wings (deep OTM),
- regions with sparse data,
- maturities with wide bid/ask spreads.

---

## Boundary and extrapolation effects


Local vol requires a surface over a domain in $(K,T)$, but data are finite:

- strikes are available only in a range,
- maturities are discrete.

Thus extrapolation is unavoidable, and instability often concentrates near:

- smallest maturity $T\to 0$,
- largest maturity (scarce quotes),
- extreme strikes where extrapolation dominates.

Common mitigation:
- enforce reasonable asymptotic wing behavior (e.g., SVI-inspired),
- freeze or damp local vol outside liquid regions.

---

## Short-maturity pathologies


As $T\to 0$, option prices become very sensitive to microstructure, discrete dividends, and jump risk.
Even a small mismatch in forward/dividend handling can distort $\partial_T C$ significantly.

Practitioner rules of thumb:
- exclude ultra-short maturities from the Dupire inversion,
- treat dividend modeling carefully (forward curve consistency),
- apply stronger smoothing in time near $T=0$.

---

## Numerical differentiation stability


Even with a smooth fitted surface, numerical differentiation choices matter:

- finite difference step sizes,
- derivative schemes (central vs one-sided),
- interpolation grid spacing.

Stability improves when:
- derivatives are computed analytically from the fitted functional form (e.g., splines/SVI),
- differentiation is done in well-scaled coordinates (log-moneyness),
- the grid avoids extreme clustering where finite differences become tiny.

---

## Regularized local vol (post-processing)


A common practical approach is to compute a “raw” local vol estimate and then solve a *regularized reconstruction* problem:

$$
\min_{\sigma_{\text{loc}}} \; \|\text{Price}(\sigma_{\text{loc}}) - C^{\text{mkt}}\|^2
+ \lambda\,\mathcal{R}(\sigma_{\text{loc}})
$$


where $\mathcal{R}$ penalizes roughness in $t$ and/or $S$.

This shifts the problem from direct differentiation (very unstable) to a PDE-constrained optimization (more stable but computationally heavier).

---

## Validation for stability


You should validate local vol surfaces by:

- **re-calibration under perturbations** within bid/ask,
- checking for unreasonable spikes or negative local variance (should not occur),
- pricing simple exotics (barriers) and checking sensitivity,
- monitoring day-to-day surface movement.

---

## Key takeaways


- Local volatility calibration is intrinsically ill-posed; smoothing is necessary but not sufficient.
- Instability concentrates in wings, sparse maturities, and near expiry.
- Numerical differentiation and extrapolation are major sources of error.
- Regularized PDE-constrained approaches can improve stability at higher cost.

---

## Further reading


- Dupire (1994), “Pricing with a Smile”.
- Gatheral, *The Volatility Surface*.
- Rebonato, *Volatility and Correlation* (practitioner view on local vol pitfalls).

---

## Exercises

**Exercise 1.** The Dupire formula involves the ratio of a numerator $N = 2(\partial_T C + (r-q)K\partial_K C - qC)$ to a denominator $D = K^2 \partial_{KK}C$. Suppose both $N$ and $D$ are estimated with relative errors $\delta_N$ and $\delta_D$ respectively. Using first-order error propagation, show that the relative error in $\sigma_{\text{loc}}^2 = N/D$ satisfies

$$
\frac{\delta(\sigma_{\text{loc}}^2)}{\sigma_{\text{loc}}^2} \approx \sqrt{\delta_N^2 + \delta_D^2}
$$

Explain why the instability is worst when $|D|$ is small, even if $\delta_D$ is moderate.

??? success "Solution to Exercise 1"
    Let $\sigma_{\text{loc}}^2 = N/D$ where $N$ and $D$ are estimated with errors $\hat{N} = N(1 + \delta_N)$ and $\hat{D} = D(1 + \delta_D)$, with $\delta_N$ and $\delta_D$ being small relative errors.

    The estimated local variance is

    $$
    \widehat{\sigma_{\text{loc}}^2} = \frac{\hat{N}}{\hat{D}} = \frac{N(1+\delta_N)}{D(1+\delta_D)} = \frac{N}{D}(1+\delta_N)(1+\delta_D)^{-1}
    $$

    For small $\delta_D$, $(1+\delta_D)^{-1} \approx 1 - \delta_D$, so

    $$
    \widehat{\sigma_{\text{loc}}^2} \approx \frac{N}{D}(1 + \delta_N)(1 - \delta_D) \approx \frac{N}{D}(1 + \delta_N - \delta_D)
    $$

    to first order. The relative error in $\sigma_{\text{loc}}^2$ is therefore

    $$
    \frac{\widehat{\sigma_{\text{loc}}^2} - \sigma_{\text{loc}}^2}{\sigma_{\text{loc}}^2} \approx \delta_N - \delta_D
    $$

    If $\delta_N$ and $\delta_D$ are independent with zero mean, the variance of the relative error is

    $$
    \operatorname{Var}\left(\frac{\delta(\sigma_{\text{loc}}^2)}{\sigma_{\text{loc}}^2}\right) = \operatorname{Var}(\delta_N) + \operatorname{Var}(\delta_D) = \delta_N^2 + \delta_D^2
    $$

    (interpreting $\delta_N^2$ and $\delta_D^2$ as variances), giving

    $$
    \frac{\delta(\sigma_{\text{loc}}^2)}{\sigma_{\text{loc}}^2} \approx \sqrt{\delta_N^2 + \delta_D^2}
    $$

    **Why small $|D|$ is problematic:** The relative error $\delta_D$ in $D$ is defined as $\delta_D = \Delta D / D$, where $\Delta D$ is the absolute error. Even if $\Delta D$ is moderate, when $|D|$ is small, the relative error $\delta_D = \Delta D / D$ becomes large. Specifically:

    $$
    \delta_D = \frac{\Delta D}{D} \to \infty \quad \text{as } D \to 0
    $$

    This means the relative error in $\sigma_{\text{loc}}^2$ is dominated by $\delta_D$ whenever $|D| = |K^2\partial_{KK}C|$ is small. Geometrically, this happens in the wings where the risk-neutral density is small, or wherever the smile has low curvature. In such regions, the Dupire inversion becomes extremely sensitive to perturbations, which is the fundamental source of instability.

---

**Exercise 2.** Consider a deep out-of-the-money call with $K = 150$, $S_0 = 100$, $T = 0.5$, and observed price $C^{\text{obs}} = 0.12$. The butterfly spread value $\partial_{KK}C$ estimated from neighboring strikes is $0.0003$. Estimate $\sigma_{\text{loc}}^2$ using a simplified Dupire formula with $r = q = 0$ and numerator $\partial_T C = 0.25$. Now perturb the butterfly spread by $\pm 0.0001$ and recompute. What is the relative change in $\sigma_{\text{loc}}^2$?

??? success "Solution to Exercise 2"
    **Estimating $\sigma_{\text{loc}}^2$:** With $r = q = 0$, the simplified Dupire formula is

    $$
    \sigma_{\text{loc}}^2 = \frac{2\,\partial_T C}{K^2\,\partial_{KK}C}
    $$

    Given $\partial_T C = 0.25$, $K = 150$, and $\partial_{KK}C = 0.0003$:

    $$
    \sigma_{\text{loc}}^2 = \frac{2 \times 0.25}{150^2 \times 0.0003} = \frac{0.50}{22500 \times 0.0003} = \frac{0.50}{6.75} \approx 0.0741
    $$

    **Perturbation $\partial_{KK}C = 0.0004$ (increased by $0.0001$):**

    $$
    \sigma_{\text{loc}}^2 = \frac{0.50}{150^2 \times 0.0004} = \frac{0.50}{9.00} \approx 0.0556
    $$

    **Perturbation $\partial_{KK}C = 0.0002$ (decreased by $0.0001$):**

    $$
    \sigma_{\text{loc}}^2 = \frac{0.50}{150^2 \times 0.0002} = \frac{0.50}{4.50} \approx 0.1111
    $$

    **Relative changes:**

    - Upward perturbation: $(0.0556 - 0.0741)/0.0741 \approx -25\%$
    - Downward perturbation: $(0.1111 - 0.0741)/0.0741 \approx +50\%$

    A perturbation of $\pm 0.0001$ in the butterfly spread (about $\pm 33\%$ relative to its base value of $0.0003$) produces local variance changes of $-25\%$ and $+50\%$ respectively. The asymmetry arises because $\sigma_{\text{loc}}^2 \propto 1/\partial_{KK}C$, which is a convex function---downward perturbations are amplified more than upward ones.

    This extreme sensitivity at deep OTM strikes ($K/S_0 = 1.5$) illustrates why local volatility surfaces are notoriously unstable in the wings.

---

**Exercise 3.** A practitioner observes that the local volatility surface extracted on Monday and Tuesday (with very similar market data) differs by up to 30% in the short-maturity wings. List at least four specific sources of this instability, ordered from most to least impactful. For each source, propose a concrete mitigation strategy.

??? success "Solution to Exercise 3"
    **Four sources of instability, ordered from most to least impactful:**

    1. **Small denominator $\partial_{KK}C$ in the short-maturity wings:** Near expiry, the risk-neutral density becomes sharply peaked near the forward. In the wings, $\partial_{KK}C$ is extremely small, so any noise in the numerator is amplified by division. Between Monday and Tuesday, even tiny changes in wing quotes (within bid-ask) can produce large percentage changes in local vol.
        - *Mitigation:* Apply a floor to $\partial_{KK}C$ or freeze local vol beyond the last liquid strike. Use SVI/SSVI parameterization that regularizes the wings.

    2. **Noisy estimation of $\partial_T C$ at short maturities:** With few short-dated maturities available, $\partial_T C$ is estimated via forward differences with large time steps, producing significant truncation error. Day-to-day changes in the shortest maturity quote (and changes in time-to-expiry itself) directly shift the estimated $\partial_T C$.
        - *Mitigation:* Exclude maturities shorter than a threshold (e.g., $T < 0.05$). Use parametric interpolation in the time direction (e.g., linear interpolation in total variance) to stabilize the time derivative.

    3. **Different bid-ask realizations:** Even if the "true" surface is unchanged, the mid-market prices observed on Monday and Tuesday are different realizations of bid-ask noise. Since differentiation amplifies this noise by $1/h^2$ or $1/h^4$, the calibrated surface jitters.
        - *Mitigation:* Smooth the input surface using penalized splines or SVI before applying Dupire. Average quotes over a time window rather than using a single snapshot.

    4. **Forward and discount curve changes:** Small changes in interest rates, dividends, or the forward price between Monday and Tuesday shift the entire surface in $(K, T)$ coordinates. If these shifts are not consistently reflected in the inputs, they introduce apparent changes in $\partial_K C$ and $\partial_T C$.
        - *Mitigation:* Work in forward-moneyness and total-variance coordinates, which factor out forward and discounting effects. Re-derive the forward curve daily from liquid instruments.

---

**Exercise 4.** In the regularized local volatility reconstruction

$$
\min_{\sigma_{\text{loc}}} \|\text{Price}(\sigma_{\text{loc}}) - C^{\text{mkt}}\|^2 + \lambda\,\mathcal{R}(\sigma_{\text{loc}})
$$

suppose $\mathcal{R}(\sigma_{\text{loc}}) = \int\int [(\partial_T \sigma_{\text{loc}})^2 + (\partial_K \sigma_{\text{loc}})^2]\,dK\,dT$. Explain the trade-off controlled by $\lambda$. What happens to the vanilla repricing error as $\lambda \to \infty$? How would you choose $\lambda$ in practice using an L-curve or cross-validation approach?

??? success "Solution to Exercise 4"
    In the regularized reconstruction

    $$
    \min_{\sigma_{\text{loc}}} \|\text{Price}(\sigma_{\text{loc}}) - C^{\text{mkt}}\|^2 + \lambda\,\mathcal{R}(\sigma_{\text{loc}})
    $$

    with $\mathcal{R}(\sigma_{\text{loc}}) = \iint [(\partial_T \sigma_{\text{loc}})^2 + (\partial_K \sigma_{\text{loc}})^2]\,dK\,dT$:

    **Trade-off controlled by $\lambda$:**

    - The first term (data fidelity) measures how well the model reprices vanilla options. Minimizing it alone would perfectly fit all market quotes.
    - The second term (regularization) penalizes roughness in $\sigma_{\text{loc}}$. Minimizing it alone would produce a constant (flat) local vol surface.
    - $\lambda$ interpolates between these extremes: small $\lambda$ favors fit quality; large $\lambda$ favors smoothness.

    **As $\lambda \to \infty$:** The regularization term dominates, forcing $\partial_T\sigma_{\text{loc}} \to 0$ and $\partial_K\sigma_{\text{loc}} \to 0$ everywhere. The solution converges to a flat local volatility surface $\sigma_{\text{loc}}(T, K) = \text{const}$. This constant is chosen to minimize the vanilla repricing error among all flat surfaces---essentially, it becomes the best-fit Black--Scholes implied vol (a single number). The vanilla repricing error becomes large because a flat local vol cannot reproduce a non-trivial smile.

    **Choosing $\lambda$ via the L-curve method:**

    1. Solve the optimization for a range of $\lambda$ values (e.g., $\lambda \in \{10^{-4}, 10^{-3}, \ldots, 10^2\}$).
    2. For each $\lambda$, record the data misfit $\|\text{Price}(\sigma_{\text{loc}}) - C^{\text{mkt}}\|^2$ and the roughness $\mathcal{R}(\sigma_{\text{loc}})$.
    3. Plot $\log(\text{misfit})$ vs. $\log(\text{roughness})$. The resulting curve is typically L-shaped.
    4. Choose $\lambda$ at the "corner" of the L, where both quantities are moderate. This is the point of maximum curvature of the L-curve.

    **Choosing $\lambda$ via cross-validation:**

    1. Hold out a subset of vanilla options (e.g., 20% of quotes).
    2. Calibrate using the remaining 80% for various $\lambda$.
    3. For each $\lambda$, price the held-out options and compute the out-of-sample error.
    4. Choose $\lambda$ minimizing the out-of-sample error.

    This approach is more data-driven and automatically adapts to the noise level in the market data.

---

**Exercise 5.** At very short maturities ($T < 0.05$), discrete dividends introduce jumps in the forward price. Explain why ignoring discrete dividends leads to errors in $\partial_T C$ and hence in the extracted local volatility. Describe how using a proportional dividend model versus a cash dividend model affects the stability of the Dupire inversion near ex-dividend dates.

??? success "Solution to Exercise 5"
    **Discrete dividends and $\partial_T C$:** A discrete cash dividend $D_{\text{div}}$ paid at time $t_d$ causes the stock price to jump down by $D_{\text{div}}$ at $t_d$. Consequently, the forward price has a discontinuity:

    $$
    F_{t_d^+} = F_{t_d^-} - D_{\text{div}}
    $$

    This creates a kink in the call price surface $C(K, T)$ as a function of $T$ when $T$ crosses $t_d$. The time derivative $\partial_T C$ becomes discontinuous at $t_d$, and finite-difference estimates of $\partial_T C$ that straddle the ex-dividend date are contaminated by the jump.

    If discrete dividends are ignored (i.e., a continuous dividend yield is used instead), the forward price is smooth, but it disagrees with the actual forward implied by the market. This mismatch means the estimated $\partial_T C$ includes a spurious component from the forward mispricing, which propagates into $\sigma_{\text{loc}}^2$ through the numerator of Dupire's formula.

    **Proportional dividend model ($S \to S(1-\delta)$):**

    - The stock price drops by a fraction $\delta$, so $F_T = S_0(1 - \delta)e^{(r-q)T}$ for $T > t_d$.
    - In log-moneyness coordinates $k = \ln(K/F_T)$, the surface is continuous because the forward adjustment absorbs the dividend effect.
    - The Dupire inversion is stable near $t_d$ because $\partial_T w$ in total variance coordinates does not exhibit a jump.

    **Cash dividend model ($S \to S - D_{\text{div}}$):**

    - The forward price has an additive jump, which cannot be absorbed by a multiplicative rescaling.
    - In any coordinates, the call price surface has a kink at $T = t_d$, making $\partial_T C$ discontinuous.
    - The Dupire inversion near ex-dividend dates produces artifacts: local vol can spike or dip sharply.
    - *Mitigation:* Model the cash dividend explicitly by splitting the Dupire PDE at $t_d$ with a jump condition, or use a piecewise forward curve and compute $\partial_T C$ separately on each interval.

    In practice, for equity indices with multiple dividend dates, the proportional model is preferred for Dupire calibration because it avoids the repeated kinks and yields a smoother local vol surface.

---

**Exercise 6.** As a stability check, a practitioner perturbs each market quote within its bid-ask spread (say $\pm 0.5$ vols) and re-calibrates the local volatility surface 100 times. The resulting distribution of $\sigma_{\text{loc}}(T_0, K_0)$ at a specific point has mean $0.22$ and standard deviation $0.08$. Is this level of uncertainty acceptable for hedging purposes? How would you use this bootstrap analysis to define confidence bands on the local volatility surface?

??? success "Solution to Exercise 6"
    **Assessment of uncertainty:** A standard deviation of $0.08$ on a mean of $0.22$ represents a relative uncertainty of $0.08/0.22 \approx 36\%$. For most hedging purposes, this is quite large and is likely **not acceptable**, particularly for:

    - **Delta hedging:** Local vol affects the delta through the relationship $\Delta = \partial_S C$. A 36% uncertainty in local vol translates (roughly) to significant uncertainty in delta, leading to unreliable hedge ratios.
    - **Exotic pricing:** Barrier options, autocallables, and other path-dependent products are very sensitive to the local vol surface. A 36% uncertainty band would produce a wide range of exotic prices, making risk management difficult.
    - **Greeks computation:** Vega, gamma, and other sensitivities depend on the local vol surface and its derivatives. Unstable local vol produces unstable Greeks.

    However, for **vanillas repricing**, this uncertainty may be acceptable since the vanilla prices themselves are inputs to the calibration and are reproduced by construction.

    **Defining confidence bands using bootstrap analysis:**

    1. **Pointwise confidence intervals:** At each grid point $(T_j, K_i)$, use the 100 bootstrap samples to construct a confidence interval. For example, the 90% confidence interval at $(T_0, K_0)$ is $[0.22 - 1.645 \times 0.08, 0.22 + 1.645 \times 0.08] = [0.088, 0.352]$ (assuming normality), or more robustly, use the 5th and 95th percentiles of the 100 samples.

    2. **Spatial structure of uncertainty:** The bootstrap analysis reveals where the surface is stable (small spread) and where it is unstable (large spread). Typically, ATM short-dated regions are more stable than wings and long-dated regions.

    3. **Use for risk management:**
        - Quote exotic prices as a range: price the exotic under the mean local vol surface and under the upper/lower confidence bounds.
        - Use the confidence bands to identify regions where the model is unreliable and hedge conservatively.
        - Weight hedging positions more heavily in stable regions and use model reserves for unstable regions.

    4. **Improving stability:** If the confidence bands are too wide, this indicates the need for stronger smoothing, more liquid quotes, or a more parsimonious parameterization (e.g., SSVI instead of per-slice splines).

---

**Exercise 7.** Compare the stability properties of two approaches to local volatility calibration: (a) direct Dupire inversion from a smoothed implied volatility surface, and (b) PDE-constrained optimization that minimizes pricing errors subject to a smoothness penalty on $\sigma_{\text{loc}}$. Discuss computational cost, accuracy of vanilla repricing, and robustness to data noise for each approach. Under what conditions does method (b) justify its additional cost?

??? success "Solution to Exercise 7"
    **(a) Direct Dupire inversion from a smoothed implied volatility surface:**

    - **Computational cost:** Low. Requires (i) fitting a smooth surface (SVI, splines, etc.) and (ii) computing derivatives analytically or via finite differences. This is essentially a closed-form calculation once the surface is built---no PDE solves needed. Wall-clock time is typically seconds.

    - **Vanilla repricing accuracy:** Depends on the quality of the smoothed surface. If the implied vol surface is well-fitted, vanillas are repriced well because the Dupire local vol is derived directly from the fitted surface. However, the extracted local vol may not exactly reprice vanillas due to discretization and differentiation errors.

    - **Robustness to noise:** Moderate to poor. The method inherits the noise properties of the smoothed surface. Differentiation amplifies residual noise, especially in regions where the surface is less constrained (wings, sparse maturities). The denominator $\partial_{KK}C$ can be small, amplifying errors.

    **(b) PDE-constrained optimization with smoothness penalty:**

    - **Computational cost:** High. Each evaluation of the objective function requires solving a forward PDE (Dupire's equation) to price vanillas given a candidate $\sigma_{\text{loc}}$. The optimization requires many such PDE solves (gradient-based methods also need adjoint PDE solves for the gradient). Wall-clock time ranges from minutes to hours depending on grid resolution and number of instruments.

    - **Vanilla repricing accuracy:** Excellent by construction. The objective directly minimizes pricing errors, so vanillas are repriced to within the specified tolerance. The smoothness penalty prevents overfitting to noisy quotes.

    - **Robustness to noise:** Good. The smoothness penalty $\lambda\mathcal{R}(\sigma_{\text{loc}})$ acts as a regularizer, preventing the local vol surface from developing spikes or oscillations in response to noisy data. The method finds the smoothest surface compatible with the data, which is precisely the well-posed formulation of the inverse problem.

    **When does method (b) justify its cost?**

    1. **Exotic pricing and hedging:** When local vol is used to price path-dependent exotics (barriers, autocallables, cliquets), the quality of the local vol surface directly impacts P&L. Method (b) produces a smoother, more stable surface, reducing exotic pricing noise and improving hedge ratios.

    2. **Noisy or sparse data:** When market data are illiquid, have wide bid-ask spreads, or are available at few maturities, method (a) struggles due to amplified noise. Method (b) handles this gracefully through the regularization penalty.

    3. **Day-to-day stability:** Method (b) typically produces surfaces that are more stable from one day to the next, which is critical for risk management and P&L attribution.

    4. **Regulatory and model validation:** Method (b) provides a principled, well-posed formulation of the calibration problem that is easier to validate and explain to regulators.

    Method (a) is preferred when speed is paramount (e.g., intraday recalibration), data quality is high, and the surface is used only for vanilla analytics.
