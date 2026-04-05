# SABR Calibration to Swaption Smiles

Calibration --- the process of determining model parameters from observed market prices --- is the step that transforms the SABR model from a theoretical framework into a practical pricing tool. In the swaption market, SABR is calibrated **independently for each expiry-tenor pair**, producing a separate set of parameters $(\alpha, \rho, \nu)$ for each point in the swaption cube. This section describes the standard calibration procedure, the conventions for choosing $\beta$, the role of the ATM quote in determining $\alpha$, and the optimization techniques used to fit $\rho$ and $\nu$ to the smile. Throughout, emphasis is placed on the practical considerations --- stability, robustness, and market conventions --- that determine calibration quality.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Describe the structure of swaption market data (the swaption cube)
    2. Fix $\beta$ by market convention and explain why it should not be calibrated
    3. Determine $\alpha$ from the ATM implied volatility quote
    4. Calibrate $\rho$ and $\nu$ by fitting the smile using least-squares optimization
    5. Validate calibration quality and assess parameter stability

---

## Swaption Market Data

### The Swaption Cube

The swaption market quotes implied volatilities across three dimensions:

- **Expiry**: Time until the option expires (e.g., 1M, 3M, 6M, 1Y, 2Y, ..., 30Y)
- **Tenor**: Length of the underlying swap (e.g., 1Y, 2Y, 5Y, 10Y, 20Y, 30Y)
- **Strike**: Expressed as an offset from the ATM forward swap rate (e.g., ATM$\pm$50, ATM$\pm$100, ATM$\pm$200 bps)

A typical swaption cube contains quotes for 10--15 expiries, 5--10 tenors, and 5--11 strikes, producing several hundred implied volatilities that must each be fitted by a SABR model.

### Quoting Conventions

| Market | Vol Type | $\beta$ Convention | Strike Convention |
|--------|----------|-------------------|-------------------|
| USD (pre-SOFR) | Black | $\beta = 0.5$ | ATM $\pm$ bps |
| EUR | Normal | $\beta = 0$ | ATM $\pm$ bps |
| JPY | Normal | $\beta = 0$ | ATM $\pm$ bps |
| GBP | Black | $\beta = 0.5$ | ATM $\pm$ bps |

!!! tip "Market Convention Drives Beta"
    The choice of $\beta$ is a **convention**, not a calibration result. It is fixed by the market or by the trading desk and should remain constant across all expiries and tenors. Fixing $\beta$ eliminates the degeneracy between $\alpha$ and $\beta$ that would otherwise make calibration unstable. Common choices are $\beta = 0$ (for normal vol markets) and $\beta = 0.5$ (for Black vol markets).

---

## The Calibration Procedure

### Step 1: Fix Beta

Choose $\beta$ according to market convention. This reduces the free parameters from four to three: $(\alpha, \rho, \nu)$.

### Step 2: Determine Alpha from ATM

The ATM implied volatility $\sigma_{\text{ATM}}^{\text{mkt}}$ is typically the most liquid and reliable quote. Use it to determine $\alpha$ by solving the ATM Hagan formula:

$$
\sigma_{\text{ATM}}^{\text{mkt}} = \frac{\alpha}{F^{1-\beta}}\left[1 + \left(\frac{(1-\beta)^2\alpha^2}{24 F^{2(1-\beta)}} + \frac{\rho\beta\nu\alpha}{4 F^{1-\beta}} + \frac{2-3\rho^2}{24}\nu^2\right)T\right]
$$

This is a cubic equation in $\alpha$ (the terms involving $\rho$ and $\nu$ are treated as known from initial guesses or from the previous day's calibration). The leading-order solution is:

$$
\alpha_0 = \sigma_{\text{ATM}}^{\text{mkt}} \cdot F^{1-\beta}
$$

A Newton step refines this:

$$
\alpha_{n+1} = \alpha_n - \frac{\sigma_B^{\text{ATM}}(\alpha_n) - \sigma_{\text{ATM}}^{\text{mkt}}}{\partial\sigma_B^{\text{ATM}}/\partial\alpha\big|_{\alpha_n}}
$$

Typically, 2--3 Newton iterations suffice for convergence to machine precision.

### Step 3: Calibrate Rho and Nu to the Smile

With $\alpha$ determined from the ATM quote (as a function of $\rho$ and $\nu$), the remaining task is to fit $\rho$ and $\nu$ to the OTM implied volatilities. The objective function is:

$$
\min_{\rho, \nu} \sum_{i=1}^{N_K} w_i\left[\sigma_B^{\text{Hagan}}(K_i; \alpha(\rho, \nu), \beta, \rho, \nu) - \sigma_B^{\text{mkt}}(K_i)\right]^2
$$

subject to the constraints $\rho \in (-1, 1)$ and $\nu > 0$.

**Key points:**

- $\alpha$ is **re-solved** from the ATM condition at each $(\rho, \nu)$ evaluation, ensuring the model always matches the ATM quote exactly
- The weights $w_i$ can be uniform or proportional to the inverse bid-ask spread (giving more weight to liquid strikes)
- The number of OTM quotes $N_K$ is typically 4--10

### Step 4: Validate

After calibration, check:

1. **ATM fit**: $\sigma_B^{\text{model}}(F) = \sigma_{\text{ATM}}^{\text{mkt}}$ (should be exact by construction)
2. **Smile fit**: $|\sigma_B^{\text{model}}(K_i) - \sigma_B^{\text{mkt}}(K_i)| < \epsilon$ for all calibration strikes
3. **Arbitrage-free**: Verify $C''(K) \geq 0$ across all strikes (non-negative density)
4. **Parameter ranges**: $\alpha > 0$, $|\rho| < 1$, $\nu > 0$, and parameters are in reasonable ranges

---

## Optimization Methods

### Levenberg--Marquardt

The standard algorithm for nonlinear least-squares problems. It interpolates between gradient descent (when far from the minimum) and Gauss--Newton (when close), providing robust convergence:

$$
(\mathbf{J}^{\top}\mathbf{J} + \lambda\,\mathbf{I})\,\delta\boldsymbol{\theta} = -\mathbf{J}^{\top}\mathbf{r}
$$

where $\mathbf{J}$ is the Jacobian of residuals with respect to $(\rho, \nu)$, $\mathbf{r}$ is the residual vector, and $\lambda$ is the damping parameter.

**Advantage**: Converges in 5--20 iterations for well-posed problems. The Jacobian can be computed analytically from the Hagan formula derivatives.

### Nelder--Mead

A derivative-free simplex method that is robust for noisy or discontinuous objectives. It is slower (50--200 evaluations) but requires no Jacobian computation.

### Bounds and Constraints

The constraints $\rho \in (-1, 1)$ and $\nu > 0$ are handled by:

- **Transformation**: $\rho = \tanh(\tilde{\rho})$ and $\nu = \exp(\tilde{\nu})$ map the constrained problem to unconstrained optimization
- **Penalty**: Add a barrier $+\lambda(1-\rho^2)^{-1}$ to the objective near the boundary

!!! warning "Multiple Local Minima"
    For expiry-tenor pairs with few OTM quotes (e.g., only 3 strikes), the objective function may have multiple local minima. Strategies to mitigate this:

    - Initialize from the previous day's parameters (warm start)
    - Run from multiple random starting points
    - Impose prior constraints (e.g., $\rho \in [-0.8, 0.2]$ for rates)

---

## Identifiability and Stability

### Parameter Roles

Each SABR parameter has a primary calibration role:

| Parameter | Calibrated From | Identifiability |
|-----------|-----------------|-----------------|
| $\alpha$ | ATM vol | Excellent (1 equation, 1 unknown) |
| $\rho$ | Skew (difference between OTM put and call vols) | Good (if OTM quotes available) |
| $\nu$ | Curvature (wings relative to ATM) | Good (if wide strike range available) |
| $\beta$ | Fixed by convention | Not calibrated |

### Degeneracy Between Parameters

When only a narrow range of strikes is available, $\rho$ and $\nu$ can become **degenerate**: different $(\rho, \nu)$ pairs produce similar smiles within the calibration range but diverge in the wings. This is mitigated by:

- Using strikes at least $\pm$200 bps from ATM
- Fixing $\beta$ (eliminates the $\alpha$-$\beta$ degeneracy)
- Adding regularization terms to the objective function

### Day-to-Day Stability

For risk management, smooth day-to-day parameter evolution is more important than achieving the tightest possible fit on any single day. Techniques for promoting stability:

- **Warm starting**: Initialize today's calibration from yesterday's parameters
- **Regularization**: Add $\lambda_{\text{reg}}[(\rho - \rho_{\text{prev}})^2 + (\nu - \nu_{\text{prev}})^2]$ to the objective
- **Outlier rejection**: Exclude quotes that are clearly stale or erroneous

---

## Worked Calibration Example

!!! example "Calibrating 5Y10Y USD Swaption"
    **Market data** (as of a representative date):

    | Strike (bps from ATM) | $-200$ | $-100$ | $-50$ | ATM | $+50$ | $+100$ | $+200$ |
    |-----------------------|--------|--------|-------|-----|-------|--------|--------|
    | Black vol (%) | 24.8 | 22.1 | 21.0 | 20.2 | 19.6 | 19.2 | 18.7 |

    Forward swap rate: $F = 3.50\%$, expiry $T = 5$Y, convention $\beta = 0.5$.

    **Step 1**: $\beta = 0.5$ (USD convention).

    **Step 2**: From ATM, $\alpha_0 = 0.202 \times 0.035^{0.5} = 0.0378$. After Newton refinement: $\alpha = 0.0382$.

    **Step 3**: Least-squares fit to the 6 OTM quotes yields $\rho = -0.32$, $\nu = 0.41$.

    **Validation**: Maximum error across calibration strikes is 0.15% (15 bps), within the bid-ask spread of approximately 20--40 bps. Parameters are in expected ranges.

    **Result**: $(\alpha, \beta, \rho, \nu) = (0.0382, 0.5, -0.32, 0.41)$.

---

## Summary

SABR calibration to swaption smiles follows a structured two-step procedure: fix $\beta$ by convention, determine $\alpha$ from the ATM quote, and fit $\rho$ and $\nu$ to the OTM smile by least-squares optimization. The ATM-first approach guarantees exact ATM fit and reduces the optimization to two parameters. The Levenberg--Marquardt algorithm with analytic Jacobians provides fast convergence. Calibration stability is promoted by warm starting, regularization, and fixing $\beta$. The resulting SABR parameters provide a compact, interpretable representation of each swaption smile that supports real-time pricing, interpolation, and Greek computation.

---

## Further Reading

- Hagan, P. et al. (2002). *Managing smile risk*. Wilmott Magazine, 1, 84--108.
- West, G. (2005). *Calibration of the SABR model in illiquid markets*. Applied Mathematical Finance, 12(4), 371--385.
- Rebonato, R., McKay, K., & White, R. (2009). *The SABR/LIBOR Market Model*. Wiley, Chapters 6--8.
- Le Floc'h, F. (2014). *Fast and accurate analytic basis point SABR*. SSRN preprint.

---

## Exercises

**Exercise 1.** The SABR calibration procedure has two steps: (a) determine $\alpha$ from the ATM quote; (b) fit $\rho$ and $\nu$ to the OTM smile. Explain why the ATM-first approach guarantees an exact ATM fit. For a market ATM implied vol of 18% with $F = 3\%$, $\beta = 0.5$, $T = 5$, and initial guesses $\rho = 0$, $\nu = 0.3$, solve for $\alpha$ approximately from $\sigma_{\text{ATM}} \approx \alpha/F^{1-\beta}$.

??? success "Solution to Exercise 1"
    **Why ATM-first guarantees an exact ATM fit.** In the SABR calibration procedure, $\alpha$ is determined by inverting the Hagan formula at $K = F$ (the ATM point):

    $$
    \sigma_{\text{ATM}}^{\text{mkt}} = \frac{\alpha}{F^{1-\beta}}\left[1 + \left(\frac{(1-\beta)^2\alpha^2}{24 F^{2(1-\beta)}} + \frac{\rho\beta\nu\alpha}{4 F^{1-\beta}} + \frac{2-3\rho^2}{24}\nu^2\right)T\right]
    $$

    For any given values of $(\rho, \nu)$, this equation is solved for $\alpha$ using Newton's method. Because $\alpha$ is **re-solved** from this equation at every evaluation of the objective function during the $(\rho, \nu)$ optimization, the model implied volatility at ATM always equals the market ATM volatility by construction. The ATM fit is not part of the least-squares residual; it is enforced as an exact constraint. This eliminates one degree of freedom from the optimization and ensures the most liquid, most reliable quote is matched perfectly.

    **Computing $\alpha$ for the given data.** With $F = 0.03$, $\beta = 0.5$, $T = 5$, $\sigma_{\text{ATM}}^{\text{mkt}} = 0.18$, and initial guesses $\rho = 0$, $\nu = 0.3$, the leading-order approximation sets the correction bracket to zero:

    $$
    \sigma_{\text{ATM}} \approx \frac{\alpha}{F^{1-\beta}} = \frac{\alpha}{F^{0.5}}
    $$

    Solving for $\alpha$:

    $$
    \alpha \approx \sigma_{\text{ATM}} \cdot F^{0.5} = 0.18 \times (0.03)^{0.5} = 0.18 \times 0.17321 = 0.03118
    $$

    This leading-order estimate would then be refined by 2--3 Newton iterations to account for the correction term, but the approximate value $\alpha \approx 0.031$ provides an excellent starting point.

---

**Exercise 2.** The OTM fit minimizes $\sum_i (\sigma^{\text{SABR}}(K_i) - \sigma^{\text{mkt}}(K_i))^2$ over $(\rho, \nu)$. Suppose the market smile has 5 quotes at strikes 1.5%, 2%, 2.5% (ATM), 3%, 3.5%. Explain why two parameters ($\rho$, $\nu$) are well-determined by 4 OTM quotes (5 total minus 1 ATM). What happens if only 2 quotes are available?

??? success "Solution to Exercise 2"
    **Degrees of freedom analysis.** With 5 market quotes and 3 SABR parameters ($\alpha$, $\rho$, $\nu$), and with $\alpha$ exactly determined by the ATM condition, we are left with 2 free parameters ($\rho$, $\nu$) to fit 4 non-ATM (OTM) quotes. This gives an **over-determined** system: 4 equations for 2 unknowns, with 2 excess degrees of freedom. The system is solved in the least-squares sense, minimizing the sum of squared residuals.

    The 4 OTM quotes provide enough information to identify both parameters because $\rho$ and $\nu$ control different features of the smile:

    - **$\rho$ controls the skew**: the asymmetry between OTM put volatilities and OTM call volatilities. With strikes on both sides of ATM, the difference $\sigma_B(K_{\text{low}}) - \sigma_B(K_{\text{high}})$ primarily determines $\rho$.
    - **$\nu$ controls the curvature**: the degree to which the smile is "U-shaped." The average elevation of both wings relative to ATM primarily determines $\nu$.

    With 4 OTM quotes spanning both sides of ATM, these two effects are distinguishable, and the system is well-identified.

    **If only 2 quotes are available** (e.g., ATM $\pm$ 50 bps), the system becomes **exactly determined**: 2 equations for 2 unknowns. While a unique solution may exist, the calibration suffers from:

    1. **No redundancy**: There is no way to assess goodness of fit or detect outliers in the market data
    2. **Sensitivity to noise**: Small errors in either quote translate directly into large parameter swings
    3. **Potential degeneracy**: With only two narrow strikes, different $(\rho, \nu)$ pairs may produce nearly identical implied volatilities within the narrow range, leading to ill-conditioning of the Jacobian
    4. **Unreliable extrapolation**: The calibrated smile may behave erratically outside the narrow calibration range

    In practice, at least 4 OTM quotes (2 below and 2 above ATM) are recommended for robust calibration.

---

**Exercise 3.** Warm starting uses yesterday's calibrated parameters as today's initial guess. Explain why this improves both speed and stability. If yesterday's parameters were $\rho = -0.25$, $\nu = 0.42$, and today's ATM vol shifted by 1 bp, would you expect the new $\rho$ and $\nu$ to change significantly? Why or why not?

??? success "Solution to Exercise 3"
    **Speed improvement.** The SABR calibration objective function $\sum_i [\sigma_B^{\text{SABR}}(K_i) - \sigma_B^{\text{mkt}}(K_i)]^2$ is a nonlinear least-squares problem that typically has a single basin of attraction (for well-posed problems), but the optimizer may take many iterations to reach it from a poor starting point. Warm starting places the initial guess in the neighborhood of the solution, so Levenberg--Marquardt or Nelder--Mead converges in fewer iterations (typically 3--5 with warm start vs. 10--20 with a cold start). Since each iteration requires evaluating the Hagan formula at all calibration strikes and solving for $\alpha$, the savings are roughly proportional to the ratio of iteration counts.

    **Stability improvement.** Day-to-day, the underlying market conditions (forward rates, volatility levels, and skew) change incrementally. The SABR parameters that describe these conditions should also change incrementally. Without warm starting, the optimizer may converge to different local minima on consecutive days (especially when the objective has a flat valley), producing parameter jumps that create artificial P&L volatility and unstable Greeks. Warm starting biases the solution toward continuity with the previous day, acting as an implicit regularizer.

    **Impact of a 1 bp ATM shift.** If the ATM vol shifts by 1 bp (e.g., from 20.20% to 20.21%), $\alpha$ adjusts through the ATM inversion:

    $$
    \Delta\alpha \approx \frac{\Delta\sigma_{\text{ATM}}}{\partial\sigma_B/\partial\alpha} \approx \frac{0.0001}{5.32} \approx 0.00002
    $$

    This is a relative change of approximately 0.05% in $\alpha$. The parameters $\rho$ and $\nu$ would change by even less, since the OTM smile shape is largely unaffected by a parallel 1 bp shift. We would expect $\Delta\rho < 0.001$ and $\Delta\nu < 0.001$. The fundamental reason is that $\rho$ and $\nu$ are determined by the **shape** of the smile (skew and curvature), not its **level**, and a 1 bp parallel shift barely changes the shape.

---

**Exercise 4.** A swaption trader calibrates SABR independently for each expiry-tenor pair in the swaption cube. For a 5Y expiry with tenors 5Y, 10Y, 20Y, 30Y, she obtains $\rho = -0.28, -0.35, -0.42, -0.48$ respectively. Is the trend in $\rho$ across tenors economically sensible? Explain why longer-tenor swaps might have more negative $\rho$ values.

??? success "Solution to Exercise 4"
    The trend of increasingly negative $\rho$ with longer swap tenor ($\rho = -0.28, -0.35, -0.42, -0.48$ for 5Y, 10Y, 20Y, 30Y tenors) is **economically sensible** for the following reasons.

    **Negative correlation between rates and volatility.** The parameter $\rho$ measures the correlation between innovations in the forward swap rate and innovations in its volatility. A negative $\rho$ means that when rates fall, volatility rises, and vice versa. This is the interest rate analogue of the "leverage effect" in equity markets.

    **Why longer tenors have more negative $\rho$:**

    1. **Flight-to-quality dynamics**: When the economy weakens, long-term rates fall as the market prices in lower growth and potential central bank easing. Simultaneously, uncertainty about the long-term economic outlook rises, increasing rate volatility. This negative rate-vol correlation is stronger for longer-maturity instruments because they are more sensitive to macroeconomic uncertainty.

    2. **Duration and convexity effects**: Longer-tenor swaps have higher duration, so a given change in yield produces larger price moves. Market participants who are long duration (e.g., pension funds, insurance companies) become more active hedgers when rates move, and this hedging activity amplifies volatility precisely when rates are falling, strengthening the negative $\rho$.

    3. **Central bank policy**: Short-term rates are more directly anchored by central bank policy, which limits both rate moves and vol moves. Long-term rates are less constrained, allowing the negative rate-vol correlation to manifest more strongly.

    4. **Empirical smile steepness**: In swaption markets, longer-tenor smiles tend to exhibit steeper skew (higher OTM payer vol relative to OTM receiver vol), which is captured by a more negative $\rho$.

    The monotonic trend is consistent with these economic forces and is observed robustly across currencies and dates.

---

**Exercise 5.** The Levenberg-Marquardt algorithm requires the Jacobian $\partial\sigma^{\text{SABR}}(K_i)/\partial\rho$ and $\partial\sigma^{\text{SABR}}(K_i)/\partial\nu$. These can be computed analytically by differentiating the Hagan formula. Explain why analytic Jacobians are preferred over finite-difference Jacobians for calibration. What numerical issues might arise with finite differences when $\nu$ is small?

??? success "Solution to Exercise 5"
    **Why analytic Jacobians are preferred.** The Levenberg--Marquardt algorithm uses the Jacobian $\mathbf{J}$ with entries $J_{ij} = \partial\sigma_B^{\text{SABR}}(K_i)/\partial\theta_j$ where $\theta = (\rho, \nu)$. Analytic Jacobians, obtained by differentiating the Hagan formula symbolically, offer several advantages over finite-difference approximations:

    1. **Exact derivatives**: Analytic Jacobians compute the true partial derivatives without approximation error. Finite differences introduce truncation error ($O(h)$ for forward differences, $O(h^2)$ for central differences) that can distort the Gauss--Newton direction.

    2. **No step-size selection**: Finite differences require choosing a perturbation $h$ for each parameter. Too large $h$ gives poor approximation; too small $h$ causes catastrophic cancellation in floating-point arithmetic. The optimal $h \sim \sqrt{\epsilon_{\text{mach}}} \approx 10^{-8}$ for double precision is parameter-dependent and difficult to tune automatically.

    3. **Computational cost**: Finite-difference Jacobians require $2p$ additional function evaluations for central differences ($p = 2$ parameters), each involving evaluation of the Hagan formula at all $N_K$ strikes. Analytic derivatives are computed alongside the function evaluation with minimal additional cost.

    4. **Convergence rate**: Inaccurate Jacobians degrade the quadratic convergence of Gauss--Newton to linear convergence (or worse), requiring more iterations to reach the minimum.

    **Numerical issues when $\nu$ is small.** When $\nu \to 0$, the SABR model degenerates to a CEV model, and the Hagan formula terms involving $\nu$ vanish. The finite-difference approximation $\partial\sigma_B/\partial\nu \approx [\sigma_B(\nu + h) - \sigma_B(\nu - h)]/(2h)$ suffers because:

    - For $\nu$ near zero, a negative perturbation $\nu - h < 0$ violates the constraint $\nu > 0$, forcing the use of one-sided differences with larger truncation error
    - The sensitivity $\partial\sigma_B/\partial\nu$ itself is small when $\nu \approx 0$ (the smile is nearly flat), so the signal-to-noise ratio in the finite difference is poor
    - Catastrophic cancellation occurs because $\sigma_B(\nu + h) \approx \sigma_B(\nu - h)$ when $\nu$ is small, making the numerator the difference of nearly equal numbers

    Analytic Jacobians avoid all of these issues by providing the exact derivative regardless of the parameter magnitude.

---

**Exercise 6.** After calibration, the SABR parameters provide a compact representation of the smile that can be used for interpolation. Explain how to compute the implied vol at an arbitrary strike $K^*$ not in the original calibration set. Compare this SABR-based interpolation with linear interpolation in strike space. Which produces smoother and more financially sensible results?

??? success "Solution to Exercise 6"
    **SABR-based interpolation.** Once the SABR parameters $(\alpha, \beta, \rho, \nu)$ have been calibrated to the market smile, the implied volatility at any arbitrary strike $K^*$ is computed by simply evaluating the Hagan formula:

    $$
    \sigma_B(K^*) = \frac{\alpha}{(FK^*)^{(1-\beta)/2}\left[1 + \frac{(1-\beta)^2}{24}\ln^2\frac{F}{K^*} + \frac{(1-\beta)^4}{1920}\ln^4\frac{F}{K^*}\right]} \cdot \frac{z}{x(z)} \cdot \left[1 + \left(\frac{(1-\beta)^2\alpha^2}{24(FK^*)^{1-\beta}} + \frac{\rho\beta\nu\alpha}{4(FK^*)^{(1-\beta)/2}} + \frac{2-3\rho^2}{24}\nu^2\right)T\right]
    $$

    where $z = (\nu/\alpha)(FK^*)^{(1-\beta)/2}\ln(F/K^*)$ and $x(z) = \ln[(\sqrt{1 - 2\rho z + z^2} + z - \rho)/(1 - \rho)]$. This produces a smooth, continuous smile for all $K^* > 0$.

    **Comparison with linear interpolation.** Linear interpolation in strike space computes the implied volatility at $K^*$ between two calibration strikes $K_j < K^* < K_{j+1}$ as:

    $$
    \sigma_B^{\text{lin}}(K^*) = \sigma_B(K_j) + \frac{K^* - K_j}{K_{j+1} - K_j}\left[\sigma_B(K_{j+1}) - \sigma_B(K_j)\right]
    $$

    This approach has several deficiencies:

    1. **Non-smooth smile**: The implied volatility curve has kinks at each calibration strike (the first derivative is discontinuous), producing unrealistic spikes in the implied density $f(K)$.
    2. **Non-convex call prices**: Linear interpolation in implied volatility does not guarantee convexity of the call price function $C(K)$, potentially creating butterfly arbitrage.
    3. **No extrapolation**: Beyond the range of calibration strikes, linear interpolation requires ad hoc rules (flat, linear, etc.), whereas the SABR formula provides a principled extrapolation based on the stochastic volatility model dynamics.
    4. **Inconsistent Greeks**: Delta and vega computed from linearly interpolated smiles have discontinuities at calibration strikes, leading to unstable hedges.

    **SABR produces smoother and more financially sensible results.** The Hagan formula is derived from a continuous stochastic volatility model, so the resulting smile is infinitely differentiable (analytic) in $K$. This ensures smooth call prices, non-negative densities (at least near ATM), and well-behaved Greeks. The three parameters $(\alpha, \rho, \nu)$ encode the economically meaningful features of the smile --- level, skew, and curvature --- and interpolate between calibration strikes in a way that is consistent with these features. For these reasons, SABR-based interpolation is the industry standard for swaption smiles.
