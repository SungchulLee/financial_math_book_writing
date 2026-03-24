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

---

**Exercise 2.** Given Hagan's ATM formula $\sigma_{\text{ATM}} \approx \alpha_0 / F^{1-\beta} \cdot [1 + (\ldots)T]$, describe the procedure for extracting $\alpha_0$ from the market ATM implied volatility for a given $(\beta, \rho, \nu)$. Why is this step typically performed first before fitting the full smile?

---

**Exercise 3.** A swaption desk observes the 5Y10Y implied volatility smile: ATM vol = 55 bps (normal), 25-delta receiver vol = 62 bps, 25-delta payer vol = 50 bps. The forward swap rate is 3.5%. Using $\beta = 0.5$, outline the calibration steps to determine $(\alpha_0, \rho, \nu)$. Which parameter primarily controls the skew (receiver vs. payer asymmetry)?

---

**Exercise 4.** Hagan's formula is a first-order asymptotic expansion in $T$ and becomes inaccurate for long maturities or far OTM strikes. For a 30-year swaption at 200 bps OTM, discuss the potential magnitude of the approximation error. What alternative pricing methods (PDE, Monte Carlo, higher-order expansions) can be used to validate or replace Hagan's formula?

---

**Exercise 5.** In a negative-rate environment with forward rate $F = -0.5\%$, explain why the standard SABR model with $\beta > 0$ fails. Describe the shifted SABR approach: replace $F$ with $F + s$ where $s > 0$. How should the shift $s$ be chosen? What are the implications for the interpretation of $\alpha_0$ and the smile shape?

---

**Exercise 6.** A SABR calibration for a 2Y5Y swaption on Monday yields $(\alpha_0, \rho, \nu) = (0.025, -0.30, 0.45)$. On Tuesday, with the forward rate unchanged and virtually identical market vols, the calibration yields $(0.028, -0.22, 0.52)$. Compute the percentage change in each parameter. Is this level of instability acceptable? Propose a temporal smoothing formula and discuss how to choose the smoothing parameter $\lambda$.

---

**Exercise 7.** A full swaption surface consists of smiles at (say) 7 expiries and 7 tenors, each requiring a separate SABR calibration. Describe a complete production workflow for calibrating the 49 SABR parameter sets. Address: parallelization strategy, cross-slice consistency checks, storage and versioning of parameters, and integration with a pricing library for swaption risk management.
