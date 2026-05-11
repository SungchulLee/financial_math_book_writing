# Calibration to the Implied Volatility Surface


In practice, *static* calibration to vanilla options is often performed not directly on prices, but on the **implied volatility surface**. The surface representation improves interpretability, makes quotes comparable across strikes/maturities, and helps expose arbitrage issues.

---

## From prices to implied volatility


For a given maturity $T$ and strike $K$, a market quote is typically a bid/ask or mid option price

$$
C^{\text{mkt}}(K,T)
$$



The **Black–Scholes implied volatility** $\sigma_{\text{impl}}(K,T)$ is defined as the unique $\sigma\ge 0$ such that

$$
C^{\text{BS}}(K,T;\sigma) = C^{\text{mkt}}(K,T)
$$


where $C^{\text{BS}}$ is the Black–Scholes call price (with the appropriate forward/discounting conventions).

### 1. Why implied vols?


- **Scale normalization:** prices vary strongly with level, discounting, and maturity; implied vol is closer to a normalized “shape”.
- **Market quoting conventions:** many markets quote vol (or delta-vol) directly.
- **Diagnostics:** skew/smile and term structure become visually clear.

---

## Parameterizing the surface


A volatility “surface” is really a function of strike and maturity. Common coordinates include:

- $(K,T)$ (strike, maturity),
- $(k,T)$ where $k=\log(K/F_T)$ is **log-moneyness**,
- $(\Delta,T)$ where $\Delta$ is option delta (FX-style quoting).

A robust workflow typically:

1. converts raw quotes into a consistent coordinate system (often log-moneyness),
2. performs filtering (liquidity, stale quotes, outliers),
3. fits an interpolant or parametric form.

### 1. Common surface representations


- **Parametric smiles per maturity** (e.g., SVI, polynomial in $k$)
- **Spline / kernel smoothing** across $(k,T)$
- **Local volatility / total variance surface** $w(k,T)=T\sigma_{\text{impl}}^2(k,T)$

---

## No-arbitrage considerations (static)


A “good” implied vol surface should not generate static arbitrage.

Typical constraints (informally):

- **Calendar arbitrage:** total variance should be non-decreasing in $T$ for fixed moneyness.
- **Butterfly arbitrage:** call prices convex in strike; in implied vol coordinates this imposes shape constraints.

In practice, calibration is often done after (or together with) an **arbitrage-cleaning** step: remove obvious violations, widen bid/ask, or fit a surface constrained to be arbitrage-free.

---

## Calibrating a model to the surface


Let the model depend on parameters $\theta$. For each grid point $(K_i,T_i)$, we can compute model prices $C^{\text{model}}(K_i,T_i;\theta)$ and then compute the corresponding implied vol

$$
\sigma^{\text{model}}_{\text{impl}}(K_i,T_i;\theta)
$$



Calibration “to the surface” means selecting $\theta$ such that

$$
\sigma^{\text{model}}_{\text{impl}}(K_i,T_i;\theta)
\approx
\sigma^{\text{mkt}}_{\text{impl}}(K_i,T_i)
$$



This is usually posed as a weighted optimization problem (see next sections).

---

## Practical pitfalls


- **Implied vol inversion noise:** deep OTM options or short maturities can make the implied-vol map ill-conditioned.
- **Data sparsity:** some maturities/strikes are illiquid; interpolation can dominate true information.
- **Smile parameterization bias:** a flexible surface can overfit noise; a rigid surface can distort the fit.
- **Numerical cost:** if model pricing is expensive, calibrating at many grid points may be slow.

---

## Key takeaways


- Calibrating to the implied vol surface aligns with market conventions and improves interpretability.
- Surface construction and arbitrage filtering are part of the calibration pipeline.
- The choice of **objective function** and **weights** largely determines calibration stability (next files).

---

## Further reading


- Gatheral, *The Volatility Surface* (implied vol geometry and SVI).
- Fengler, *Semiparametric Modeling of Implied Volatility*.
- Andersen & Piterbarg, *Interest Rate Modeling* (practitioner calibration details).

---

## Exercises

**Exercise 1.** Define the Black--Scholes implied volatility $\sigma_{\text{impl}}(K,T)$ precisely. For a call option with $S_0 = 100$, $K = 100$, $T = 0.25$, $r = 0.02$, $q = 0$, and market price $C^{\text{mkt}} = 5.50$, describe how you would numerically solve for $\sigma_{\text{impl}}$ using Newton's method. Write down the iteration formula and explain why Vega appears in the denominator.

??? success "Solution to Exercise 1"
    The Black--Scholes implied volatility $\sigma_{\text{impl}}(K,T)$ is defined as the unique non-negative value $\sigma$ such that

    $$
    C^{\text{BS}}(S_0, K, T, r, q; \sigma) = C^{\text{mkt}}(K,T)
    $$

    where $C^{\text{BS}}$ denotes the Black--Scholes call price formula:

    $$
    C^{\text{BS}} = S_0 e^{-qT} \mathcal{N}(d_1) - K e^{-rT} \mathcal{N}(d_2)
    $$

    with $d_1 = \frac{\ln(S_0/K) + (r - q + \sigma^2/2)T}{\sigma\sqrt{T}}$ and $d_2 = d_1 - \sigma\sqrt{T}$.

    Existence and uniqueness follow from the fact that $C^{\text{BS}}$ is strictly increasing in $\sigma$ on $(0,\infty)$, ranging continuously from the intrinsic value $(S_0 e^{-qT} - Ke^{-rT})^+$ at $\sigma = 0$ to $S_0 e^{-qT}$ as $\sigma \to \infty$.

    To solve numerically using Newton's method, define the root-finding problem $g(\sigma) = C^{\text{BS}}(\sigma) - C^{\text{mkt}} = 0$. Newton's iteration is:

    $$
    \sigma_{n+1} = \sigma_n - \frac{C^{\text{BS}}(\sigma_n) - C^{\text{mkt}}}{\frac{\partial C^{\text{BS}}}{\partial \sigma}(\sigma_n)} = \sigma_n - \frac{C^{\text{BS}}(\sigma_n) - C^{\text{mkt}}}{\text{Vega}(\sigma_n)}
    $$

    The Black--Scholes Vega is

    $$
    \text{Vega} = S_0 e^{-qT} \sqrt{T}\, \phi(d_1)
    $$

    where $\phi$ is the standard normal density. Vega appears in the denominator because Newton's method requires the derivative of the function being zeroed. Since $C^{\text{BS}}$ is a smooth, strictly increasing function of $\sigma$ with positive Vega everywhere (for $T > 0$ and finite strike), the iteration is well-defined and converges quadratically near the solution.

    For the given numerical example ($S_0 = 100$, $K = 100$, $T = 0.25$, $r = 0.02$, $q = 0$, $C^{\text{mkt}} = 5.50$), one would start with an initial guess such as $\sigma_0 = 0.20$, compute $C^{\text{BS}}(\sigma_0)$ and the corresponding Vega, then iterate. Convergence is typically achieved in 3--5 iterations to machine precision.

---

**Exercise 2.** Explain why implied volatility is more convenient than raw prices for visualizing the volatility surface. Given the following data: $\sigma_{\text{impl}}(90, 0.25) = 0.28$, $\sigma_{\text{impl}}(100, 0.25) = 0.22$, $\sigma_{\text{impl}}(110, 0.25) = 0.20$, sketch the smile at $T = 0.25$ and identify the skew. What market phenomenon typically produces this pattern for equity index options?

??? success "Solution to Exercise 2"
    Implied volatility is more convenient than raw prices for several reasons:

    1. **Scale normalization.** Raw option prices vary enormously with the level of the underlying, the strike, the maturity, and the discount factor. A 1-year ATM call on a \$100 stock might be worth \$10, while a 1-week 10%-OTM call might be worth \$0.05. Comparing these prices directly is not informative about relative richness or cheapness. Implied volatility normalizes out these effects, placing all options on a comparable scale (typically 10--50% for equities).

    2. **Market conventions.** Many markets (especially FX) quote options directly in volatility terms. Even in equity markets, traders think in "vol" when assessing relative value.

    3. **Shape diagnostics.** In the implied volatility surface, the skew and smile become immediately visible, whereas in price space these features are obscured by the monotonic dependence on strike and maturity.

    For the given data at $T = 0.25$:

    | Strike $K$ | $\sigma_{\text{impl}}$ |
    |:---:|:---:|
    | 90 | 0.28 |
    | 100 | 0.22 |
    | 110 | 0.20 |

    The smile at $T = 0.25$ is a decreasing function of strike: implied volatility is highest for low strikes (OTM puts / ITM calls) and lowest for high strikes (OTM calls / ITM puts). This is a **volatility skew** (also called a "smirk"), not a symmetric smile.

    This pattern is characteristic of **equity index options** and is driven by several reinforcing phenomena: (i) the leverage effect---when stock prices drop, firm leverage increases, raising equity volatility; (ii) crash risk---investors demand protection against large downside moves, bidding up OTM put prices and hence their implied vols; (iii) supply-demand imbalances---institutional hedging creates persistent demand for downside protection. The skew became particularly pronounced after the 1987 crash and has been a persistent feature of equity index markets since then.

---

**Exercise 3.** Define the total variance surface $w(k,T) = T\sigma_{\text{impl}}^2(k,T)$ where $k = \ln(K/F_T)$. State the calendar arbitrage condition in terms of $w$ and explain why it is easier to check in total variance coordinates than in implied volatility coordinates.

??? success "Solution to Exercise 3"
    The **total variance surface** is defined as

    $$
    w(k, T) = T \, \sigma_{\text{impl}}^2(k, T)
    $$

    where $k = \ln(K / F_T)$ is the log-moneyness relative to the forward price $F_T$.

    The **calendar arbitrage condition** in total variance coordinates states that for fixed log-moneyness $k$, the total variance must be non-decreasing in maturity:

    $$
    \frac{\partial w}{\partial T}(k, T) \ge 0 \quad \text{for all } k \text{ and } T > 0
    $$

    or equivalently, for $T_1 < T_2$:

    $$
    w(k, T_1) \le w(k, T_2)
    $$

    This condition is easier to check in total variance coordinates than in implied volatility coordinates for the following reason. In implied volatility coordinates, the analogous condition is

    $$
    T_2 \, \sigma_{\text{impl}}^2(k, T_2) \ge T_1 \, \sigma_{\text{impl}}^2(k, T_1)
    $$

    which does **not** require $\sigma_{\text{impl}}$ itself to be increasing in $T$. The implied volatility can decrease with maturity (as term structures often do for long dates) without violating no-arbitrage, provided it does not decrease fast enough to make the total variance decrease. In total variance space, the condition reduces to a simple monotonicity check: $w$ must be non-decreasing in $T$ for each fixed $k$. This is a straightforward pointwise comparison, whereas in implied volatility space one must jointly reason about the level of $\sigma_{\text{impl}}$ and the factor $T$, making violations less visually obvious.

    The financial intuition is that total variance represents the cumulative "amount of randomness" up to time $T$. Since randomness cannot be un-accumulated, total variance must grow (or at least not shrink) with the horizon. A violation would allow a calendar spread arbitrage: sell the shorter-dated option and buy the longer-dated option to lock in a riskless profit.

---

**Exercise 4.** A practitioner constructs an implied volatility surface from 50 market quotes using cubic spline interpolation in log-moneyness for each of 5 maturities. After interpolation, they discover that the butterfly spread $C(K-h) - 2C(K) + C(K+h) < 0$ at a specific point. What type of arbitrage does this violate? Propose two methods to repair the surface.

??? success "Solution to Exercise 4"
    The condition $C(K - h) - 2C(K) + C(K + h) < 0$ means that the call price function is **concave** in strike at the point $K$. This violates the **butterfly arbitrage** (also called **strike convexity**) condition.

    The no-arbitrage requirement is that the call price $C(K)$ must be a convex function of $K$. Equivalently, the second derivative $\partial^2 C / \partial K^2 \ge 0$, which is proportional to the risk-neutral density of the underlying at $K$. A negative second difference implies a negative risk-neutral density in that region, which is impossible for a probability distribution.

    Concretely, a butterfly spread with strikes $K - h$, $K$, $K + h$ (buy the wings, sell the body) has a non-negative payoff at expiry. If its price is negative, one can buy it for a profit with no risk---a static arbitrage.

    **Two methods to repair the surface:**

    1. **Constrained spline fitting.** Replace the unconstrained cubic spline with a shape-constrained interpolation method. One approach is to fit a spline (or piecewise polynomial) subject to the constraint that $\partial^2 C / \partial K^2 \ge 0$ at all grid points. This can be formulated as a quadratic program (minimize squared deviations from data subject to linear inequality constraints on second differences). Alternatively, one can use monotone-convexity-preserving splines (e.g., Fritsch--Carlson or Schumaker shape-preserving interpolants applied to the call price curve). In the SVI framework, the parametric form automatically guarantees convexity under certain parameter restrictions.

    2. **Arbitrage filtering via total variance adjustment.** Convert the implied volatility surface to total variance $w(k) = T \sigma^2(k)$. In total variance space, butterfly arbitrage corresponds to a violation of the condition $1 - \frac{k}{w}\frac{\partial w}{\partial k} + \frac{1}{4}\left(-\frac{1}{4} - \frac{1}{w} + \frac{k^2}{w^2}\right)\left(\frac{\partial w}{\partial k}\right)^2 + \frac{1}{2}\frac{\partial^2 w}{\partial k^2} \ge 0$. One can smooth the total variance curve by local averaging or by fitting a parameterization (such as SVI) that is known to satisfy this density condition under appropriate parameter constraints. Where violations are detected, locally adjust the interpolated values by the minimal perturbation needed to restore convexity, or widen the bid-ask tolerance at those points and re-interpolate.

---

**Exercise 5.** When computing model implied volatilities $\sigma_{\text{impl}}^{\text{model}}(K_i, T_i; \theta)$ for calibration, one must numerically invert the Black--Scholes formula for each model price. Discuss the computational cost of this nested inversion when calibrating a Heston model to 200 vanilla options. How does this compare to calibrating directly in price space?

??? success "Solution to Exercise 5"
    When calibrating a model (such as Heston) to 200 vanilla options in **implied volatility space**, the procedure at each optimizer iteration is:

    1. For current parameters $\theta$, compute the model price $C_j^{\text{model}}(\theta)$ for each of the 200 options.
    2. For each model price, numerically invert the Black--Scholes formula to obtain $\sigma_j^{\text{model}}(\theta)$.
    3. Compute the objective $\mathcal{L}_{\text{iv}}(\theta) = \frac{1}{2}\sum_{j=1}^{200} w_j (\sigma_j^{\text{model}} - \sigma_j^{\text{mkt}})^2$.

    Step 2 requires solving $C^{\text{BS}}(\sigma) = C_j^{\text{model}}$ for each of the 200 options at every iteration. Each inversion typically requires 3--8 Newton iterations, each involving one evaluation of $\Phi(\cdot)$ (the normal CDF) and $\phi(\cdot)$ (the normal PDF). If the optimizer requires $N_{\text{iter}}$ iterations (say 50--500 for a gradient-based method), the total number of implied vol inversions is $200 \times N_{\text{iter}}$, each costing several function evaluations.

    For the Heston model specifically, semi-analytic pricing via the characteristic function and numerical integration (e.g., using the Carr--Madan FFT or the Lewis formula) already involves significant computation per option. A single FFT call can price many strikes at once for a given maturity, but one still needs separate FFT calls for each maturity. The nested implied-vol inversion adds an overhead factor.

    **Comparison to price-space calibration.** In price space, the objective is $\mathcal{L}_{\text{price}}(\theta) = \frac{1}{2}\sum_{j=1}^{200} w_j (C_j^{\text{model}} - C_j^{\text{mkt}})^2$, which eliminates step 2 entirely. The cost saving is the elimination of all 200 Newton inversions per optimizer step. For 200 options and 200 optimizer iterations, this saves on the order of $200 \times 200 \times 5 = 200{,}000$ Black--Scholes evaluations. While each Black--Scholes evaluation is cheap individually, this overhead can be 10--30% of total calibration time when model pricing itself is fast (as with FFT-based Heston pricing).

    However, if gradient-based optimization is used and the Jacobian $\partial \sigma_j^{\text{model}} / \partial \theta$ is needed, the implicit function theorem gives

    $$
    \frac{\partial \sigma_j^{\text{model}}}{\partial \theta} = \frac{1}{\text{Vega}_j} \frac{\partial C_j^{\text{model}}}{\partial \theta}
    $$

    so once the implied vol inversion is done, the gradient computation is only marginally more expensive than in price space. The main cost difference is therefore the inversion itself, not the gradient.

    In practice, many implementations cache implied vol inversions and use efficient initial guesses (rational approximations such as Jäckel's method), reducing the inversion cost to near-trivial levels. The choice between price-space and vol-space calibration is then driven more by statistical and stability considerations than by computational cost.

---

**Exercise 6.** Compare calibrating in log-moneyness coordinates $k = \ln(K/F_T)$ versus delta-parameterized coordinates $\Delta$. For which market (equity vs. FX) is each convention more natural? How does the choice of coordinates affect the interpolation quality in the wings?

??? success "Solution to Exercise 6"
    **Log-moneyness coordinates** $k = \ln(K/F_T)$:

    - **Natural for equity markets**, where options are listed at fixed strikes $K$ (e.g., \$90, \$95, \$100, ...) and the forward $F_T$ is readily computed from the spot, interest rate, and dividend yield.
    - Log-moneyness centers the smile at $k = 0$ (ATM forward) and is symmetric in the sense that $k$ and $-k$ correspond to equally "far" strikes on opposite sides.
    - Common parametric forms (SVI, polynomial smiles) are naturally expressed in $k$.

    **Delta-parameterized coordinates** $\Delta$:

    - **Natural for FX markets**, where the quoting convention is in terms of delta (e.g., 25-delta put, ATM, 25-delta call). FX volatility quotes are given as ATM vol, risk reversal (25$\Delta$ and 10$\Delta$), and butterfly (25$\Delta$ and 10$\Delta$), which directly correspond to delta buckets.
    - Delta compresses the far wings: as $K \to 0$ or $K \to \infty$, delta approaches 1 or 0 respectively, so the entire strike range maps into $[0, 1]$.

    **Effect on wing interpolation quality:**

    In log-moneyness space, the wings extend to $k \to \pm\infty$, and interpolation/extrapolation in the wings can be poorly constrained by sparse data. A polynomial or spline in $k$ may oscillate or diverge for large $|k|$.

    In delta space, the wings are compressed into the regions near $\Delta = 0$ and $\Delta = 1$. This compression can improve interpolation stability in the wings because the coordinate transformation effectively "stretches" the well-observed near-ATM region and "compresses" the poorly observed wings. However, delta is itself a function of implied volatility (since $\Delta = \mathcal{N}(d_1)$ involves $\sigma$), creating a circular dependence: to parameterize in delta, one needs the volatility, but the volatility is what one is trying to determine. This is typically handled iteratively or by using a "sticky delta" convention.

    For equity markets, log-moneyness is preferred because listed strikes are fixed and the delta parameterization adds unnecessary complexity. For FX markets, delta is preferred because it aligns with market conventions and naturally handles the fact that FX option strikes are quoted relative to delta rather than absolute levels.

---

**Exercise 7.** Data sparsity can make surface construction unreliable. Suppose you have 3 strikes at $T = 0.1$, 8 strikes at $T = 0.5$, and 5 strikes at $T = 2.0$. Describe how you would handle this uneven data density when constructing a smooth surface. What risks arise from over-interpolating in sparse regions, and how do these propagate to calibrated model parameters?

??? success "Solution to Exercise 7"
    The uneven data density---3 strikes at $T = 0.1$, 8 strikes at $T = 0.5$, 5 strikes at $T = 2.0$---requires careful treatment in surface construction.

    **Handling the uneven density:**

    1. **Per-maturity smile fitting.** Fit a separate smile model (e.g., SVI or a low-order polynomial in log-moneyness) at each maturity independently. At $T = 0.1$ with only 3 strikes, use a parsimonious parameterization (e.g., a quadratic or a 3-parameter SVI) to avoid overfitting. At $T = 0.5$ with 8 strikes, a richer parameterization (full 5-parameter SVI or cubic spline) is justified. Then interpolate across maturities in total variance space to ensure calendar spread arbitrage-freeness.

    2. **Regularization in sparse regions.** Apply stronger regularization (smoothness penalties) at $T = 0.1$ where data is sparse, and lighter regularization at $T = 0.5$ where data is dense. A Bayesian approach would use a prior that shrinks the smile toward a simple shape (e.g., flat or linear in $k$) when data is scarce.

    3. **Maturity-balanced weighting.** In a global surface fit, normalize weights per maturity so that each maturity contributes equally to the objective function. Without this, the 8 strikes at $T = 0.5$ would dominate and the surface at $T = 0.1$ would be poorly determined.

    4. **Confidence bands.** Report uncertainty estimates (e.g., bootstrap standard errors) for the interpolated surface. In sparse regions, the confidence bands will be wide, signaling that the surface is driven more by the interpolation model than by data.

    **Risks from over-interpolating in sparse regions:**

    - **Spurious smile features.** With only 3 data points at $T = 0.1$, a flexible interpolant (e.g., a cubic spline passing exactly through the points) can introduce oscillations and artificial convexity/concavity that do not reflect the true market smile.
    - **Arbitrage violations.** A poorly constrained short-maturity smile may violate butterfly or calendar arbitrage conditions. Since $T = 0.1$ is the shortest maturity, calendar arbitrage violations relative to $T = 0.5$ are particularly dangerous.
    - **Instability.** Small perturbations to any of the 3 data points at $T = 0.1$ can cause large changes in the interpolated surface, leading to unstable calibrated parameters.

    **Propagation to calibrated model parameters:**

    The surface at short maturities is particularly influential for certain model parameters. For instance, in the Heston model, the short-maturity smile constrains the initial variance $v_0$ and the vol-of-vol $\xi$. If the short-maturity surface is unreliable, these parameters will be poorly identified, leading to (i) instability across recalibration dates, (ii) poor pricing of short-dated exotics, and (iii) unreliable risk sensitivities. Long-maturity parameters (e.g., long-run variance $\bar{v}$ and mean-reversion speed $\kappa$) are similarly affected by sparsity at $T = 2.0$ but are typically more stable because the smile shape is smoother at long horizons.
