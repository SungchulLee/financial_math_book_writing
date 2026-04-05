# SABR Calibration Workflow

The SABR model is the market standard for quoting and interpolating implied volatility smiles in interest rate derivatives. Its four-parameter structure and Hagan's closed-form approximation enable rapid calibration to individual smile slices, making it the workhorse for swaption and cap/floor markets. This section develops the complete calibration workflow, from ATM vol matching through smile fitting to swaption surface calibration.

---

## The SABR model

### Model dynamics

The SABR (Stochastic Alpha, Beta, Rho) model specifies the forward rate $F_t$ and its stochastic volatility $\alpha_t$ under the forward measure $\mathbb{Q}^T$:

$$
dF_t = \alpha_t \, F_t^{\beta} \, dW_t^F
$$

$$
d\alpha_t = \nu \, \alpha_t \, dW_t^{\alpha}
$$

where $dW_t^F \, dW_t^{\alpha} = \rho \, dt$. The four parameters are:

| Parameter | Symbol | Role | Typical range |
|-----------|--------|------|---------------|
| Initial volatility | $\alpha_0$ | Overall volatility level | $(0, \infty)$ |
| CEV exponent | $\beta$ | Backbone slope | $[0, 1]$ |
| Correlation | $\rho$ | Skew of the smile | $(-1, 1)$ |
| Vol-of-vol | $\nu$ | Curvature of the smile | $(0, \infty)$ |

The parameter $\beta$ governs the local volatility structure: $\beta = 0$ gives a normal model (absolute volatility), $\beta = 1$ gives a log-normal model (proportional volatility), and intermediate values interpolate between these extremes.

!!! tip "Role of beta"
    In practice, $\beta$ is often fixed rather than calibrated. Common choices are $\beta = 0$ (normal SABR, preferred for low or negative rate environments), $\beta = 0.5$ (CIR-like square-root backbone), or $\beta = 1$ (log-normal SABR). Fixing $\beta$ reduces the calibration to three free parameters $(\alpha_0, \rho, \nu)$, improving stability and identifiability.

### Financial interpretation

Each parameter controls a distinct feature of the implied volatility smile:

- **$\alpha_0$** sets the overall level of implied volatility. Increasing $\alpha_0$ shifts the entire smile upward.
- **$\beta$** determines the slope of the ATM volatility backbone as a function of the forward rate. For $\beta < 1$, ATM volatility increases as rates decrease (normal-like behavior).
- **$\rho$** controls the asymmetry (skew) of the smile. Negative $\rho$ makes the smile left-skewed; positive $\rho$ makes it right-skewed.
- **$\nu$** controls the curvature (convexity) of the smile. Larger $\nu$ produces a more pronounced smile with higher wings.

---

## Hagan's implied volatility approximation

The key to rapid SABR calibration is the closed-form approximation of Hagan, Kumar, Lesniewski, and Woodward (2002) for the Black implied volatility.

### General strike formula

For a European option on the forward $F_0$ with strike $K$ and expiry $T$, the SABR implied volatility is approximately

$$
\sigma_B(K, F_0) = \frac{\alpha_0}{(F_0 K)^{(1-\beta)/2} \left[ 1 + \frac{(1-\beta)^2}{24} \ln^2\!\frac{F_0}{K} + \frac{(1-\beta)^4}{1920} \ln^4\!\frac{F_0}{K} \right]} \cdot \frac{z}{x(z)} \cdot \left[ 1 + \epsilon \, T \right]
$$

where

$$
z = \frac{\nu}{\alpha_0} (F_0 K)^{(1-\beta)/2} \ln \frac{F_0}{K}
$$

$$
x(z) = \ln\!\left( \frac{\sqrt{1 - 2\rho z + z^2} + z - \rho}{1 - \rho} \right)
$$

and the correction term is

$$
\epsilon = \frac{(1-\beta)^2 \alpha_0^2}{24 (F_0 K)^{1-\beta}} + \frac{\rho \beta \nu \alpha_0}{4 (F_0 K)^{(1-\beta)/2}} + \frac{(2 - 3\rho^2) \nu^2}{24}
$$

!!! warning "Limitations of Hagan's formula"
    The Hagan approximation is a second-order perturbation expansion in $T$. It becomes inaccurate for: (1) long maturities ($T > 10$--$15$ years), (2) far out-of-the-money strikes ($|k| > 2$--$3$ in log-moneyness), and (3) large vol-of-vol ($\nu > 1$). For these regimes, the approximation may produce negative implied volatilities or arbitrage violations. Alternative approaches include the Obloj (2008) correction, the Antonov-Konikov-Spector exact formula, and PDE-based pricing.

### ATM formula

At the money ($K = F_0$), the formula simplifies considerably. Setting $z = 0$ and using $\lim_{z \to 0} z / x(z) = 1$:

$$
\sigma_{\mathrm{ATM}} = \frac{\alpha_0}{F_0^{1-\beta}} \left[ 1 + \left( \frac{(1-\beta)^2 \alpha_0^2}{24 F_0^{2(1-\beta)}} + \frac{\rho \beta \nu \alpha_0}{4 F_0^{1-\beta}} + \frac{(2 - 3\rho^2) \nu^2}{24} \right) T \right]
$$

This expression is central to the calibration workflow: it provides a direct relationship between $\alpha_0$ and the observed ATM implied volatility.

### Normal SABR formula

For $\beta = 0$, the Hagan formula for the normal (Bachelier) implied volatility takes a simpler form:

$$
\sigma_N(K, F_0) = \alpha_0 \cdot \frac{z}{x(z)} \cdot \left[ 1 + \left( \frac{-\alpha_0^2}{24(F_0 - K)^2} \cdot \frac{(F_0 - K)^2}{(F_0 K)} + \frac{(2 - 3\rho^2)\nu^2}{24} \right) T \right]
$$

with $z = \nu(F_0 - K)/\alpha_0$. The normal SABR is preferred in low-rate environments where the forward can be near zero or negative, as it avoids the singularity of the log-normal model at $F = 0$.

---

## Calibration workflow

The SABR calibration proceeds in two stages: first determine $\alpha_0$ from the ATM volatility, then fit $\rho$ and $\nu$ to the smile shape.

### Stage 1 -- ATM vol matching

Given $\beta$ (fixed), the observed ATM implied volatility $\sigma_{\mathrm{ATM}}^{\mathrm{mkt}}$, and preliminary guesses for $\rho$ and $\nu$, solve the ATM formula for $\alpha_0$:

$$
\sigma_{\mathrm{ATM}}^{\mathrm{mkt}} = \frac{\alpha_0}{F_0^{1-\beta}} \left[ 1 + \epsilon_{\mathrm{ATM}}(\alpha_0, \rho, \nu) \, T \right]
$$

This is a cubic equation in $\alpha_0$. The leading-order approximation provides an excellent starting point:

$$
\alpha_0^{(0)} = \sigma_{\mathrm{ATM}}^{\mathrm{mkt}} \cdot F_0^{1-\beta}
$$

A few Newton-Raphson iterations refine $\alpha_0^{(0)}$ to the exact solution of the cubic.

### Stage 2 -- Smile fitting

With $\alpha_0$ determined (as a function of $\rho$ and $\nu$), minimize the misfit over the remaining parameters:

$$
\min_{\rho, \nu} \sum_{j=1}^{m} w_j \left( \sigma_j^{\mathrm{SABR}}(\alpha_0(\rho, \nu), \beta, \rho, \nu) - \sigma_j^{\mathrm{mkt}} \right)^2
$$

Since only two parameters remain, this is a well-conditioned optimization problem that converges rapidly. Standard algorithms include:

- **Levenberg-Marquardt** with analytic Jacobian (computed from the Hagan formula derivatives)
- **Nelder-Mead simplex** when analytic derivatives are inconvenient
- **Grid search** over a coarse $(\rho, \nu)$ grid followed by local refinement

### Parameter constraints

The optimizer must enforce:

$$
-1 < \rho < 1, \qquad \nu > 0, \qquad \alpha_0 > 0
$$

In practice, tighter bounds improve stability: $|\rho| < 0.999$ and $\nu < 2.0$. For swaption markets, typical calibrated values are $\rho \in (-0.5, 0.3)$ and $\nu \in (0.2, 0.8)$.

---

## Swaption surface calibration

In the interest rate market, SABR is calibrated independently to each swaption expiry-tenor slice.

### Swaption market structure

The swaption market quotes implied volatilities on a two-dimensional grid:

- **Expiry** $T_{\mathrm{exp}}$: the option expiry (e.g., 1M, 3M, 6M, 1Y, 2Y, 5Y, 10Y, 20Y, 30Y)
- **Tenor** $T_{\mathrm{swap}}$: the underlying swap tenor (e.g., 1Y, 2Y, 5Y, 10Y, 20Y, 30Y)

For each $(T_{\mathrm{exp}}, T_{\mathrm{swap}})$ pair, the market provides implied volatilities at several strikes, typically quoted as offsets from the ATM forward swap rate (e.g., ATM $\pm$ 25bp, $\pm$ 50bp, $\pm$ 100bp, $\pm$ 200bp).

### Per-slice calibration

For each swaption slice $(T_{\mathrm{exp}}, T_{\mathrm{swap}})$:

1. Determine the forward swap rate $F_0 = S_{m,n}(0)$ from the yield curve.
2. Fix $\beta$ (common choices: $\beta = 0.5$ for rates, $\beta = 0$ for low-rate regimes).
3. Run the two-stage calibration (ATM matching + smile fitting) on the quoted strikes.
4. Store the calibrated $(\alpha_0, \rho, \nu)$ for this slice.

The result is a parameter surface: $\alpha_0(T_{\mathrm{exp}}, T_{\mathrm{swap}})$, $\rho(T_{\mathrm{exp}}, T_{\mathrm{swap}})$, $\nu(T_{\mathrm{exp}}, T_{\mathrm{swap}})$.

### Interpolation and extrapolation

Between calibrated slices, SABR parameters must be interpolated to price non-standard swaptions. Two approaches are common:

1. **Parameter interpolation.** Interpolate $\alpha_0$, $\rho$, $\nu$ directly across the $(T_{\mathrm{exp}}, T_{\mathrm{swap}})$ grid. Simple but may produce arbitrage.
2. **Smile interpolation.** Interpolate implied volatilities at each strike, then recalibrate SABR to the interpolated smile. More robust but computationally heavier.

For extrapolation beyond the quoted grid, the SABR parameters are typically held constant (flat extrapolation) or extrapolated with care to avoid extreme values.

!!! warning "Arbitrage in SABR"
    The Hagan formula does not guarantee absence of arbitrage, especially for far OTM strikes or long maturities. Butterfly arbitrage (negative probability density) can occur when the implied volatility function is insufficiently convex. Remedies include: (1) checking the density $p(K) = e^{rT} \partial^2 C / \partial K^2 \geq 0$, (2) using arbitrage-free alternatives such as the SABR model with exact solutions, and (3) applying post-hoc corrections to enforce density positivity.

---

## Comparison with Heston calibration

The SABR and Heston calibration pipelines differ in several important respects:

| Aspect | SABR | Heston |
|--------|------|--------|
| Pricing engine | Closed-form (Hagan) | Fourier inversion (FFT/COS) |
| Calibration unit | Per-slice (one expiry) | Full surface (all expiries) |
| Number of parameters | 3 (with $\beta$ fixed) | 5 |
| Speed | Very fast (milliseconds per slice) | Moderate (seconds for full surface) |
| Dynamics | No term structure dynamics | Mean-reversion provides dynamics |
| Best suited for | Rate derivatives, quoting | Equity derivatives, exotics |

SABR excels at capturing the smile shape within a single maturity slice but does not constrain the relationship between slices. Heston provides a globally consistent model with inter-maturity dynamics governed by mean-reversion.

---

## Practical considerations

### Beta selection

The choice of $\beta$ affects both the quality of fit and the behavior of the model in stress scenarios:

- **$\beta = 1$ (log-normal):** Natural for equity-like dynamics; ATM vol scales as $\sigma \propto 1/F^{1-\beta} = 1$ (flat backbone).
- **$\beta = 0.5$:** Intermediate; ATM vol scales as $\sigma \propto 1/\sqrt{F}$.
- **$\beta = 0$ (normal):** ATM vol scales as $\sigma \propto F^0 = 1$ in normal vol terms; preferred for negative rates.

A common approach is to calibrate $\beta$ from a time series of ATM volatilities across different rate levels, regressing $\ln \sigma_{\mathrm{ATM}}$ against $\ln F$ to estimate the backbone exponent.

### Low-rate and negative-rate environments

When forward rates are near zero or negative, the standard SABR model ($\beta > 0$) breaks down because $F^{\beta}$ is undefined for $F < 0$. Solutions include:

- **Normal SABR** ($\beta = 0$): Works for any sign of $F$.
- **Shifted SABR**: Replace $F$ with $F + s$ where $s > 0$ is a shift parameter chosen so that $F + s > 0$ for all relevant forwards.
- **Free-boundary SABR** (Antonov et al.): Extends the model to handle absorption at zero without an ad hoc shift.

### Recalibration frequency

SABR parameters are typically recalibrated daily (or intraday for active desks). The fast calibration speed---milliseconds per slice---makes this feasible even for large swaption grids. Temporal smoothing via $\alpha_0^{\mathrm{smooth}} = \lambda \hat{\alpha}_0 + (1 - \lambda) \alpha_0^{\mathrm{prev}}$ (and similarly for $\rho$ and $\nu$) helps stabilize Greeks.

---

## Exercises

**Exercise 1.** In the SABR model, $\beta$ controls the backbone dynamics. For $\beta = 1$ (log-normal), ATM implied volatility is roughly constant as the forward moves. For $\beta = 0$ (normal), ATM normal volatility is constant. Explain qualitatively what happens for $\beta = 0.5$. How would you estimate $\beta$ empirically from a time series of ATM vols and forward rates?

??? success "Solution to Exercise 1"
    **Behavior for $\beta = 0.5$.**
    The SABR dynamics are $dF_t = \alpha_t F_t^{\beta} dW_t^F$. The local volatility is $\alpha_t F_t^{\beta}$, so the "backbone" relationship between ATM volatility and the forward level is

    $$
    \sigma_{\text{ATM}} \approx \frac{\alpha_0}{F_0^{1-\beta}}
    $$

    to leading order. For different $\beta$ values:

    - $\beta = 1$: $\sigma_{\text{ATM}} \approx \alpha_0$, constant (log-normal backbone). ATM Black vol does not depend on $F_0$.
    - $\beta = 0$: $\sigma_{\text{ATM}} \approx \alpha_0 / F_0$, so $\sigma_{\text{ATM}} \propto 1/F_0$. ATM Black vol increases as $F_0$ decreases. Equivalently, normal vol $\sigma_N \approx \alpha_0$ is constant.
    - $\beta = 0.5$: $\sigma_{\text{ATM}} \approx \alpha_0 / F_0^{0.5} = \alpha_0 / \sqrt{F_0}$. This is intermediate -- ATM Black vol increases as the forward decreases, but less steeply than for $\beta = 0$. The implied volatility scales as $\sigma \propto F_0^{-1/2}$, similar to a CIR (square-root) process.

    Qualitatively, $\beta = 0.5$ captures a moderate negative relationship between rate levels and volatility: when rates fall, volatility rises, but not as dramatically as in the normal model. This is appropriate for rate environments where the volatility response to rate changes is neither purely proportional (log-normal) nor purely additive (normal).

    **Empirical estimation of $\beta$.**
    Given a time series of ATM implied volatilities $\{\sigma_t\}$ and corresponding forward rates $\{F_t\}$, the backbone exponent can be estimated by regressing log-volatility on log-forward:

    $$
    \ln \sigma_{\text{ATM},t} = a + (-(1-\beta)) \ln F_t + \varepsilon_t
    $$

    Since $\sigma_{\text{ATM}} \propto F^{-(1-\beta)}$, the slope of $\ln \sigma$ versus $\ln F$ is $-(1-\beta)$, so

    $$
    \beta = 1 + \text{slope}
    $$

    For example, if the regression yields a slope of $-0.5$, then $\beta = 0.5$. In practice, this regression should use changes (rather than levels) to avoid spurious correlation, and should be estimated over a period with sufficient variation in forward rates. Rolling-window estimation captures time-varying $\beta$, which may shift across monetary policy regimes.

---

**Exercise 2.** Given Hagan's ATM formula $\sigma_{\text{ATM}} \approx \alpha_0 / F^{1-\beta} \cdot [1 + (\ldots)T]$, describe the procedure for extracting $\alpha_0$ from the market ATM implied volatility for a given $(\beta, \rho, \nu)$. Why is this step typically performed first before fitting the full smile?

??? success "Solution to Exercise 2"
    **Procedure for extracting $\alpha_0$.**
    Given fixed values of $\beta$, $\rho$, and $\nu$, and the observed ATM implied volatility $\sigma_{\text{ATM}}^{\text{mkt}}$, the ATM formula provides a single equation in the single unknown $\alpha_0$:

    $$
    \sigma_{\text{ATM}}^{\text{mkt}} = \frac{\alpha_0}{F_0^{1-\beta}} \left[ 1 + \left( \frac{(1-\beta)^2 \alpha_0^2}{24 F_0^{2(1-\beta)}} + \frac{\rho \beta \nu \alpha_0}{4 F_0^{1-\beta}} + \frac{(2 - 3\rho^2)\nu^2}{24} \right) T \right]
    $$

    Let $\hat{\sigma} = \sigma_{\text{ATM}}^{\text{mkt}}$ and $\hat{F} = F_0^{1-\beta}$. Multiplying through:

    $$
    \hat{\sigma} = \frac{\alpha_0}{\hat{F}} + \frac{(1-\beta)^2 T}{24 \hat{F}^3} \alpha_0^3 + \frac{\rho \beta \nu T}{4 \hat{F}^2} \alpha_0^2 + \frac{(2-3\rho^2)\nu^2 T}{24 \hat{F}} \alpha_0
    $$

    This is a **cubic equation** in $\alpha_0$. The leading-order approximation (setting $T = 0$ or dropping higher-order terms) gives

    $$
    \alpha_0^{(0)} = \sigma_{\text{ATM}}^{\text{mkt}} \cdot F_0^{1-\beta}
    $$

    This is then refined by Newton-Raphson iteration on the full cubic. Define

    $$
    g(\alpha_0) = \frac{\alpha_0}{\hat{F}} \left[ 1 + \epsilon(\alpha_0) T \right] - \hat{\sigma}
    $$

    and iterate $\alpha_0^{(n+1)} = \alpha_0^{(n)} - g(\alpha_0^{(n)}) / g'(\alpha_0^{(n)})$. Convergence is typically achieved in 2--3 iterations since the leading-order estimate is already very close.

    **Why this step is performed first.** Extracting $\alpha_0$ first is beneficial because:

    1. **Dimension reduction.** The ATM vol provides one strong constraint that essentially eliminates $\alpha_0$ as a free parameter. The remaining optimization over $(\rho, \nu)$ is only 2-dimensional, which is fast, well-conditioned, and easy to visualize.
    2. **Stability.** $\alpha_0$ is the most directly observable parameter -- it is essentially the overall level of volatility. Fixing it from the ATM constraint prevents the optimizer from trading off level ($\alpha_0$) against shape ($\rho, \nu$) in unphysical ways.
    3. **Speed.** The Newton-Raphson solve for $\alpha_0$ takes microseconds. Embedding $\alpha_0 = \alpha_0(\rho, \nu)$ as a function of the remaining parameters converts a 3D optimization into a 2D one, dramatically reducing the iteration count.

---

**Exercise 3.** A swaption desk observes the 5Y10Y implied volatility smile: ATM vol = 55 bps (normal), 25-delta receiver vol = 62 bps, 25-delta payer vol = 50 bps. The forward swap rate is 3.5%. Using $\beta = 0.5$, outline the calibration steps to determine $(\alpha_0, \rho, \nu)$. Which parameter primarily controls the skew (receiver vs. payer asymmetry)?

??? success "Solution to Exercise 3"
    **Calibration outline for the 5Y10Y swaption smile.**

    *Given data:*

    - Forward swap rate: $F_0 = 3.5\% = 0.035$
    - ATM normal vol: 55 bps
    - 25-delta receiver vol: 62 bps (higher vol for lower strikes)
    - 25-delta payer vol: 50 bps (lower vol for higher strikes)
    - $\beta = 0.5$

    *Step 1: Determine $\alpha_0$ from ATM vol.*
    Using the leading-order ATM formula:

    $$
    \alpha_0^{(0)} \approx \sigma_{\text{ATM}}^{\text{mkt}} \cdot F_0^{1-\beta} = 0.0055 \times (0.035)^{0.5} = 0.0055 \times 0.1871 = 0.001029
    $$

    Note: Since the quoted vols are in normal (Bachelier) terms (bps), we need to convert to Black vol or use the normal SABR formula. For $\beta = 0.5$ with Hagan's Black vol formula, the conversion is embedded in the formula. The leading-order Black vol estimate is $\sigma_B \approx \alpha_0 / F_0^{0.5}$, so $\alpha_0 \approx \sigma_B \times F_0^{0.5}$.

    Refine $\alpha_0$ by Newton-Raphson on the full ATM formula with initial guesses for $\rho$ and $\nu$.

    *Step 2: Identify $\rho$ from the skew.*
    The risk reversal is

    $$
    \text{RR} = \sigma_{25\Delta R} - \sigma_{25\Delta P} = 62 - 50 = 12 \text{ bps}
    $$

    The receiver vol (lower strike) is higher, indicating a left-skewed smile (negative $\rho$). The parameter $\rho$ is the **primary controller of skew**. A negative $\rho$ tilts the smile so that lower strikes have higher volatility, matching the observation.

    Initial estimate: $\rho \approx -0.3$ (based on the magnitude of the risk reversal relative to ATM vol).

    *Step 3: Identify $\nu$ from the curvature.*
    The butterfly is

    $$
    \text{BF} = \frac{\sigma_{25\Delta R} + \sigma_{25\Delta P}}{2} - \sigma_{\text{ATM}} = \frac{62 + 50}{2} - 55 = 56 - 55 = 1 \text{ bp}
    $$

    The butterfly of 1 bp (relative to ATM vol of 55 bps) indicates mild curvature. The parameter $\nu$ controls the curvature (convexity) of the smile. Initial estimate: $\nu \approx 0.3$--$0.4$.

    *Step 4: Joint optimization.*
    Minimize

    $$
    \min_{\rho, \nu} \sum_{j} w_j (\sigma_j^{\text{SABR}}(\alpha_0(\rho, \nu), 0.5, \rho, \nu) - \sigma_j^{\text{mkt}})^2
    $$

    using Levenberg-Marquardt or Nelder-Mead, starting from $(\rho, \nu) = (-0.3, 0.35)$. At each $(\rho, \nu)$ evaluation, recompute $\alpha_0$ from the ATM constraint. The 2D optimization converges in 5--15 iterations.

    **Which parameter primarily controls the skew:** $\rho$ is the primary skew parameter. In Hagan's formula, the $z/x(z)$ term introduces asymmetry through the function $x(z) = \ln[(\sqrt{1-2\rho z + z^2} + z - \rho)/(1-\rho)]$, which depends directly on $\rho$. For $\rho < 0$, the function $z/x(z)$ is larger for negative $z$ (lower strikes) than for positive $z$ (higher strikes), producing left-skew.

---

**Exercise 4.** Hagan's formula is a first-order asymptotic expansion in $T$ and becomes inaccurate for long maturities or far OTM strikes. For a 30-year swaption at 200 bps OTM, discuss the potential magnitude of the approximation error. What alternative pricing methods (PDE, Monte Carlo, higher-order expansions) can be used to validate or replace Hagan's formula?

??? success "Solution to Exercise 4"
    **Magnitude of approximation error for 30Y swaption at 200 bps OTM.**

    Hagan's formula is a perturbation expansion of the form $\sigma_B = \sigma_0 (1 + \epsilon \, T)$ where $\epsilon$ involves terms of order $\alpha_0^2$, $\rho \nu \alpha_0$, and $\nu^2$. For a 30-year swaption, the correction term $\epsilon \, T$ can be substantial:

    With typical swaption parameters $\nu \approx 0.4$ and $T = 30$:

    $$
    \frac{(2 - 3\rho^2)\nu^2}{24} \times T \approx \frac{(2 - 3 \times 0.09) \times 0.16}{24} \times 30 = \frac{1.73 \times 0.16}{24} \times 30 \approx 0.35
    $$

    A 35% correction to the leading-order term indicates the perturbation expansion is far outside its range of validity (the expansion assumes $\epsilon \, T \ll 1$). The error can be 5--20% of the true implied volatility.

    At 200 bps OTM, the log-moneyness $\ln(F_0/K) \approx \pm 0.55$ for $F_0 = 3.5\%$, and the higher-order terms in the denominator of Hagan's formula (the $\ln^2(F_0/K)$ and $\ln^4(F_0/K)$ corrections) become non-negligible. Combined with the large $T$ correction, the total error can produce:

    1. **Negative implied volatilities** at extreme strikes (the formula returns $\sigma_B < 0$, which is unphysical).
    2. **Butterfly arbitrage** (the second derivative $\partial^2 C / \partial K^2 < 0$, implying negative probability density).
    3. **Overestimated wing volatilities** that do not match the true SABR model dynamics.

    **Alternative pricing methods:**

    1. **PDE solution.** Solve the SABR Fokker-Planck PDE numerically using finite differences or finite elements. This provides the exact risk-neutral density and option prices without approximation. Computational cost: seconds per slice (much slower than Hagan's microseconds, but necessary for long maturities).
    2. **Monte Carlo simulation.** Simulate the SABR SDE paths directly and compute option prices by averaging discounted payoffs. Suitable for very long maturities and path-dependent products. Requires careful discretization of the CEV component to handle $F^{\beta}$ near zero.
    3. **Higher-order asymptotic expansions.** Paulot (2015) and others have derived higher-order corrections to Hagan's formula that extend the range of validity. Including $\mathcal{O}(T^2)$ terms reduces the error for moderate $T$ but still breaks down for $T > 15$--$20$ years.
    4. **Exact SABR solutions.** Antonov, Konikov, and Spector derived exact formulas for the SABR model using heat kernel expansions. These are more accurate than Hagan's for all maturities and strikes, at a modest computational premium.
    5. **Arbitrage-free SABR (Hagan-Woodward).** Post-hoc corrections that enforce density positivity and absence of arbitrage, applied on top of the standard formula.

    For a production system handling 30-year swaptions, the recommended approach is to use the Antonov-Konikov-Spector exact formula as the primary pricer, with Hagan's formula retained only for quick indicative pricing and as a benchmark for short-maturity slices ($T < 10$ years).

---

**Exercise 5.** In a negative-rate environment with forward rate $F = -0.5\%$, explain why the standard SABR model with $\beta > 0$ fails. Describe the shifted SABR approach: replace $F$ with $F + s$ where $s > 0$. How should the shift $s$ be chosen? What are the implications for the interpretation of $\alpha_0$ and the smile shape?

??? success "Solution to Exercise 5"
    **Why standard SABR fails for $F < 0$.**
    The SABR dynamics are $dF_t = \alpha_t F_t^{\beta} dW_t^F$. For $\beta > 0$, the term $F_t^{\beta}$ is undefined (or complex) when $F_t < 0$. With $F = -0.5\%$, we have $F^{\beta} = (-0.005)^{\beta}$, which is not a real number for non-integer $\beta$. Even for $\beta = 1$, the process $dF_t = \alpha_t F_t dW_t$ has $F = 0$ as an absorbing barrier (geometric Brownian motion cannot go negative), so the forward can never reach $-0.5\%$ starting from a positive value.

    **Shifted SABR approach.**
    Replace $F_t$ with $\tilde{F}_t = F_t + s$ where $s > 0$ is chosen so that $\tilde{F}_t > 0$ for all relevant forwards. The shifted SABR dynamics are:

    $$
    d\tilde{F}_t = \alpha_t \tilde{F}_t^{\beta} \, dW_t^F, \qquad d\alpha_t = \nu \alpha_t \, dW_t^{\alpha}
    $$

    with $\tilde{F}_0 = F_0 + s$ and strikes shifted accordingly: $\tilde{K} = K + s$. Hagan's formula is applied to the shifted quantities $(\tilde{F}_0, \tilde{K})$.

    **Choosing the shift $s$.**
    The shift must satisfy $F_0 + s > 0$ for all forward rates in the calibration set. Common choices:

    1. **Fixed shift:** $s = 3\%$ or $s = 5\%$, which works for moderately negative rates (down to $-3\%$ or $-5\%$). Simple but ad hoc.
    2. **Market-implied shift:** Choose $s$ equal to the absolute value of the most negative forward rate in the curve, plus a buffer: $s = |F_{\min}| + \delta$ where $\delta \approx 0.5\%$--$1\%$.
    3. **Calibrated shift:** Include $s$ as an additional parameter and calibrate it alongside $(\alpha_0, \rho, \nu)$. This is less common because it adds a degree of freedom and can destabilize calibration.

    For $F_0 = -0.5\%$, a shift of $s = 3\%$ gives $\tilde{F}_0 = 2.5\%$, comfortably positive.

    **Implications for parameter interpretation.**

    - $\alpha_0$ in the shifted model represents the volatility of the shifted forward $\tilde{F} = F + s$, not the original forward $F$. Since $\tilde{F}_0 = F_0 + s$ is larger than $F_0$ (which may be near zero), the calibrated $\alpha_0$ will be different from what it would be without the shift. Comparisons of $\alpha_0$ across different shift values are not meaningful.
    - The smile shape changes with $s$: a larger shift makes the model more log-normal-like (since $\tilde{F}$ is farther from zero), producing a more symmetric smile. A smaller shift keeps the model closer to normal behavior with more pronounced skew.
    - The backbone dynamics (how ATM vol responds to forward movements) also depend on $s$. The effective local volatility is $\alpha_t (F_t + s)^{\beta}$, so the sensitivity of ATM vol to the forward is $\beta (F_0 + s)^{\beta - 1}$, which depends on $s$.

    The key trade-off is: larger $s$ ensures robustness against further rate decreases but changes the model's behavior; smaller $s$ preserves the model's interpretation but may fail if rates decline further.

---

**Exercise 6.** A SABR calibration for a 2Y5Y swaption on Monday yields $(\alpha_0, \rho, \nu) = (0.025, -0.30, 0.45)$. On Tuesday, with the forward rate unchanged and virtually identical market vols, the calibration yields $(0.028, -0.22, 0.52)$. Compute the percentage change in each parameter. Is this level of instability acceptable? Propose a temporal smoothing formula and discuss how to choose the smoothing parameter $\lambda$.

??? success "Solution to Exercise 6"
    **Percentage changes in each parameter.**

    $$
    \Delta \alpha_0 / \alpha_0 = \frac{0.028 - 0.025}{0.025} = \frac{0.003}{0.025} = 12\%
    $$

    $$
    \Delta \rho / \rho = \frac{-0.22 - (-0.30)}{-0.30} = \frac{0.08}{-0.30} = -26.7\%
    $$

    $$
    \Delta \nu / \nu = \frac{0.52 - 0.45}{0.45} = \frac{0.07}{0.45} = 15.6\%
    $$

    **Assessment of instability.**
    These parameter changes (12%, 27%, 16%) are large given that the forward rate is unchanged and market vols are "virtually identical." This level of instability is **not acceptable** for production use because:

    1. **Greeks instability.** The delta, gamma, and vega of swaptions depend on the SABR parameters. A 27% change in $\rho$ produces a significant change in the model delta, leading to spurious hedging activity (unnecessary rebalancing that incurs transaction costs).
    2. **P\&L noise.** Day-over-day P\&L attribution will show large "model risk" or "parameter risk" components that are artifacts of calibration instability rather than genuine market moves.
    3. **Root cause.** The instability likely arises from a flat objective function near the minimum: multiple $(\rho, \nu)$ combinations (with corresponding $\alpha_0$ adjustments) produce nearly identical smile fits. The optimizer lands at different points in this flat region on consecutive days due to numerical noise or tiny changes in the input data.

    **Proposed temporal smoothing formula.**

    $$
    \alpha_0^{\text{smooth}} = \lambda \hat{\alpha}_0 + (1 - \lambda) \alpha_0^{\text{prev}}
    $$

    $$
    \rho^{\text{smooth}} = \lambda \hat{\rho} + (1 - \lambda) \rho^{\text{prev}}
    $$

    $$
    \nu^{\text{smooth}} = \lambda \hat{\nu} + (1 - \lambda) \nu^{\text{prev}}
    $$

    where $\hat{\cdot}$ denotes today's raw calibration and $\cdot^{\text{prev}}$ denotes yesterday's smoothed value.

    **Choosing $\lambda$.**
    The smoothing parameter $\lambda \in (0, 1]$ controls the tradeoff between responsiveness (tracking genuine market changes) and stability (filtering noise):

    - $\lambda = 1$: no smoothing, fully responsive (current unstable behavior).
    - $\lambda = 0.5$: equal weight on today and yesterday.
    - $\lambda = 0.2$: heavy smoothing, slow to react.

    A principled choice uses the signal-to-noise ratio. If the calibration residual (RMSE) is $\epsilon$ and the market change is $\Delta\sigma^{\text{mkt}}$, then:

    - If $\Delta\sigma^{\text{mkt}} \gg \epsilon$: the market has genuinely moved, use large $\lambda$ (e.g., $\lambda = 0.8$).
    - If $\Delta\sigma^{\text{mkt}} \ll \epsilon$: the change is noise, use small $\lambda$ (e.g., $\lambda = 0.2$).

    An adaptive rule: $\lambda = \min(1, c \cdot \|\sigma^{\text{mkt}}_{\text{today}} - \sigma^{\text{mkt}}_{\text{yesterday}}\| / \epsilon)$ where $c$ is calibrated from historical data (typical: $c = 5$--$10$).

    For the given example where market vols are virtually identical, the adaptive $\lambda$ would be close to 0, and the smoothed parameters would barely change from yesterday -- which is the desired behavior.

---

**Exercise 7.** A full swaption surface consists of smiles at (say) 7 expiries and 7 tenors, each requiring a separate SABR calibration. Describe a complete production workflow for calibrating the 49 SABR parameter sets. Address: parallelization strategy, cross-slice consistency checks, storage and versioning of parameters, and integration with a pricing library for swaption risk management.

??? success "Solution to Exercise 7"
    **Production workflow for 49 SABR calibrations (7 expiries $\times$ 7 tenors).**

    **1. Parallelization strategy.**
    Each $(T_{\text{exp}}, T_{\text{swap}})$ slice is calibrated independently (SABR is a per-slice model). This makes the problem embarrassingly parallel.

    - *Architecture:* Assign each slice to a separate thread or process. With 49 slices and a modern multi-core server (16--32 cores), all calibrations complete in 2--4 batches.
    - *Timing:* Each SABR calibration takes $\sim 1$--$5$ ms (Hagan formula evaluation is microseconds; the 2D optimization over $(\rho, \nu)$ converges in 5--15 iterations). Total wall time with parallelization: $\sim 10$--$20$ ms for all 49 slices.
    - *Implementation:* Use a thread pool (e.g., `concurrent.futures.ThreadPoolExecutor` in Python, or OpenMP in C++) with 49 tasks submitted simultaneously. Avoid process-level parallelism for such short tasks (overhead exceeds computation time).

    **2. Cross-slice consistency checks.**
    After all 49 calibrations complete, validate cross-slice consistency:

    - *$\alpha_0$ surface smoothness:* The calibrated $\alpha_0(T_{\text{exp}}, T_{\text{swap}})$ should vary smoothly across the grid. Compute the discrete Laplacian $\Delta \alpha_0$ at each interior grid point. Flag slices where $|\Delta \alpha_0|$ exceeds a threshold (e.g., 3 standard deviations from the mean Laplacian).
    - *$\rho$ monotonicity:* For fixed tenor, $\rho$ typically varies smoothly with expiry. Large jumps (e.g., $\rho$ changing sign between adjacent expiries) suggest a calibration error.
    - *$\nu$ positivity and boundedness:* Verify $\nu > 0$ and $\nu < 2.0$ for all slices. Extreme $\nu$ values indicate that Hagan's formula is being stretched beyond its validity.
    - *Arbitrage checks:* Verify that the interpolated surface (between calibrated slices) does not produce calendar spread arbitrage. Compute total implied variance $w = T \sigma^2(T, K)$ for each strike and verify $w$ is non-decreasing in $T$.
    - *Fallback procedure:* If a slice fails validation, replace its parameters with interpolated values from neighboring slices and flag for manual review.

    **3. Storage and versioning of parameters.**

    - *Data model:* Store each calibration as a record: `(date, timestamp, expiry, tenor, beta, alpha0, rho, nu, rmse, status)`.
    - *Database:* Use a time-series database (e.g., kdb+, InfluxDB) or a relational database with a date-partitioned table. Each end-of-day calibration produces 49 rows.
    - *Versioning:* Maintain an immutable audit trail. Each calibration run gets a unique run ID. If parameters are manually overridden (e.g., after a validation failure), the override is stored as a new version with a flag indicating manual intervention.
    - *Historical access:* Support queries such as "retrieve the SABR parameters for 5Y10Y as of 2024-03-15" for backtesting and regulatory reporting.

    **4. Integration with the pricing library.**

    - *Parameter retrieval:* The pricing library queries the parameter store for the latest validated SABR parameters given $(T_{\text{exp}}, T_{\text{swap}})$.
    - *Interpolation:* For non-standard expiry-tenor pairs, the library interpolates parameters from the calibrated grid. Bilinear interpolation in $(\alpha_0, \rho, \nu)$ is simplest; smile interpolation (interpolate vols, then recalibrate) is more robust.
    - *Pricing:* Given parameters, price swaptions using Hagan's formula for standard maturities ($T < 10$Y) and the Antonov-Konikov-Spector formula for long-dated ($T > 10$Y).
    - *Greeks:* Compute delta, gamma, vega, and cross-Greeks by differentiating through the SABR formula (analytic derivatives are available). Alternatively, bump-and-reprice with the calibrated parameters.
    - *Risk reporting:* Aggregate swaption risk across the portfolio by tenor bucket and expiry bucket, using the SABR-implied deltas and vegas as the risk measures. Monitor the P\&L explained by parameter changes versus market changes to detect model degradation.
