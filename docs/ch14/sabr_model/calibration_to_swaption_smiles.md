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
