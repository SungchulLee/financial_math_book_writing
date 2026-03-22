# End-to-End Worked Examples

The previous sections developed the SABR model piece by piece: SDE and parameters, Hagan formula, calibration procedure, Greeks, and arbitrage corrections. This section assembles those pieces into complete workflows that mirror what a practitioner executes every day. We calibrate the SABR model to representative swaption market data, price a swaption from the calibrated parameters, compute Greeks suitable for hedging, and critically compare the model output with the market. Each step is presented with explicit numerical calculations that the reader can reproduce.

!!! info "Prerequisites"
    - [SABR SDE and Parameters](sabr_sde_and_parameters.md) (model definition)
    - [Hagan Implied Volatility Approximation](hagan_implied_volatility_approximation.md) (Hagan formula)
    - [Calibration to Swaption Smiles](calibration_to_swaption_smiles.md) (calibration procedure)
    - [SABR Greeks (Analytical)](sabr_greeks_analytical.md) (delta, vega, Bartlett correction)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Execute a full SABR calibration to swaption market data with explicit numerical steps
    2. Price a European payer swaption using the calibrated SABR implied volatility and the Black formula
    3. Compute SABR delta, vega, and the Bartlett correction numerically
    4. Assess calibration quality by comparing model and market implied volatilities
    5. Interpret the calibrated parameters in terms of market features

---

## Example 1: Calibrating a 5Y into 10Y USD Swaption Smile

### Market Data

Consider a USD payer swaption with 5-year expiry into a 10-year swap, observed on a representative date. The forward swap rate is $F = 3.50\%$ and the annuity factor is $A = 7.82$. The market quotes Black implied volatilities at seven strikes relative to ATM.

| Strike offset (bps) | $-200$ | $-100$ | $-50$ | ATM | $+50$ | $+100$ | $+200$ |
|---|---|---|---|---|---|---|---|
| Strike ($K$, %) | 1.50 | 2.50 | 3.00 | 3.50 | 4.00 | 4.50 | 5.50 |
| Black IV (%) | 24.80 | 22.10 | 21.00 | 20.20 | 19.60 | 19.20 | 18.70 |

The expiry is $T = 5$ years. USD convention sets $\beta = 0.5$.

### Step 1: Fix Beta

By USD swaption convention, $\beta = 0.5$. This is not calibrated.

### Step 2: Determine Alpha from the ATM Quote

The ATM Hagan formula at $K = F = 0.035$ is:

$$
\sigma_B^{\text{ATM}} = \frac{\alpha}{F^{1-\beta}}\left[1 + \left(\frac{(1-\beta)^2\alpha^2}{24 F^{2(1-\beta)}} + \frac{\rho\beta\nu\alpha}{4 F^{1-\beta}} + \frac{2-3\rho^2}{24}\nu^2\right)T\right]
$$

**Leading-order estimate.** Setting the correction term to zero:

$$
\alpha_0 = \sigma_B^{\text{ATM}} \cdot F^{1-\beta} = 0.2020 \times 0.035^{0.5} = 0.2020 \times 0.18708 = 0.03779
$$

**Newton refinement.** With initial guesses $\rho = -0.3$ and $\nu = 0.4$ (from the previous day or a rough estimate), one Newton iteration gives:

$$
\alpha_1 = \alpha_0 - \frac{\sigma_B^{\text{Hagan}}(\alpha_0, \rho, \nu) - 0.2020}{\partial \sigma_B^{\text{Hagan}} / \partial\alpha\big|_{\alpha_0}}
$$

Computing: $\sigma_B^{\text{Hagan}}(\alpha_0) \approx 0.1985$, and $\partial\sigma_B/\partial\alpha \approx 5.32$, so:

$$
\alpha_1 = 0.03779 - \frac{0.1985 - 0.2020}{5.32} = 0.03779 + 0.00066 = 0.03845
$$

After a second Newton iteration: $\alpha = 0.03821$.

### Step 3: Calibrate Rho and Nu

With $\alpha(\rho, \nu)$ determined by the ATM condition at each evaluation, minimize:

$$
\min_{\rho, \nu} \sum_{i=1}^{6} \left[\sigma_B^{\text{Hagan}}(K_i; \alpha(\rho, \nu), 0.5, \rho, \nu) - \sigma_B^{\text{mkt}}(K_i)\right]^2
$$

Using Levenberg-Marquardt with starting point $(\rho_0, \nu_0) = (-0.3, 0.4)$:

**Iteration 1.** Evaluate the residual vector at the 6 OTM strikes. The Jacobian $\mathbf{J}$ is $6 \times 2$ with entries $\partial\sigma_B^{\text{Hagan}}(K_i)/\partial\rho$ and $\partial\sigma_B^{\text{Hagan}}(K_i)/\partial\nu$ (including the implicit dependence through $\alpha(\rho, \nu)$). Solve the normal equations to get the parameter update $\delta(\rho, \nu)$.

**Convergence.** After 8 iterations, the optimizer converges to:

$$
\rho^* = -0.3185, \qquad \nu^* = 0.4073
$$

and the ATM-consistent alpha is $\alpha^* = 0.03821$.

### Step 4: Validate the Calibration

Compute model implied volatilities at all strikes and compare with market:

| Strike (%) | Market IV (%) | Model IV (%) | Error (bps) |
|:---:|:---:|:---:|:---:|
| 1.50 | 24.80 | 24.68 | $-12$ |
| 2.50 | 22.10 | 22.16 | $+6$ |
| 3.00 | 21.00 | 20.98 | $-2$ |
| 3.50 | 20.20 | 20.20 | $0$ (exact by construction) |
| 4.00 | 19.60 | 19.57 | $-3$ |
| 4.50 | 19.20 | 19.12 | $-8$ |
| 5.50 | 18.70 | 18.55 | $-15$ |

The maximum error is 15 bps at the $K = 5.50\%$ wing. This is within the typical bid-ask spread of 20--40 bps for OTM swaptions.

!!! tip "Calibration Quality Assessment"
    An RMSE below 10 bps across the calibration strikes indicates an excellent fit. Here the RMSE is approximately 8.5 bps. The largest errors occur at the extreme wings, where the Hagan formula's asymptotic approximation is least accurate.

### Calibrated Parameters Summary

| Parameter | Value | Interpretation |
|---|---|---|
| $\alpha$ | 0.03821 | ATM vol level: $\sigma_{\text{ATM}} \approx \alpha / F^{0.5} = 20.2\%$ |
| $\beta$ | 0.50 | CIR-type backbone (USD convention) |
| $\rho$ | $-0.3185$ | Moderate negative skew |
| $\nu$ | 0.4073 | Moderate vol-of-vol (smile curvature) |

---

## Example 2: Pricing a European Payer Swaption

### Setup

Using the calibrated parameters from Example 1, price a 5Y into 10Y payer swaption with strike $K = 4.00\%$ (50 bps OTM).

### Step 1: Compute the SABR Implied Volatility

From the calibrated model:

$$
\sigma_B(K = 0.04) = 19.57\%
$$

This was already computed in the validation step above.

### Step 2: Apply the Black Formula

The Black formula for a payer swaption with annuity $A$, forward rate $F$, strike $K$, expiry $T$, and implied volatility $\sigma_B$ is:

$$
V_{\text{payer}} = A \left[F\,\Phi(d_1) - K\,\Phi(d_2)\right]
$$

where:

$$
d_1 = \frac{\ln(F/K) + \frac{1}{2}\sigma_B^2 T}{\sigma_B\sqrt{T}}, \qquad d_2 = d_1 - \sigma_B\sqrt{T}
$$

**Numerical computation:**

$$
d_1 = \frac{\ln(0.035/0.040) + \frac{1}{2}(0.1957)^2 \times 5}{0.1957 \times \sqrt{5}} = \frac{-0.13353 + 0.09581}{0.43756} = \frac{-0.03772}{0.43756} = -0.08621
$$

$$
d_2 = -0.08621 - 0.43756 = -0.52377
$$

$$
\Phi(d_1) = \Phi(-0.08621) = 0.46565
$$

$$
\Phi(d_2) = \Phi(-0.52377) = 0.30024
$$

$$
V_{\text{payer}} = 7.82 \times [0.035 \times 0.46565 - 0.040 \times 0.30024]
$$

$$
= 7.82 \times [0.01630 - 0.01201] = 7.82 \times 0.00429 = 0.03355
$$

The payer swaption price is **3.355%** of notional, or **335.5 bps**. On a \$100 million notional, this is approximately \$3.355 million.

---

## Example 3: Computing SABR Greeks

### Delta (Sensitivity to Forward Rate)

The SABR delta for the $K = 4.00\%$ payer swaption is:

$$
\Delta_{\text{SABR}} = A\left[\Delta_{\text{Black}}(\sigma_B) + \mathcal{V}_{\text{Black}}(\sigma_B) \cdot \frac{\partial\sigma_B}{\partial F}\right]
$$

**Black delta:**

$$
\Delta_{\text{Black}} = \Phi(d_1) = 0.46565
$$

**Black vega (per unit annuity):**

$$
\mathcal{V}_{\text{Black}} = F\sqrt{T}\,\phi(d_1) = 0.035 \times 2.2361 \times \phi(-0.08621)
$$

$$
= 0.07826 \times 0.39656 = 0.03103
$$

**Smile sensitivity $\partial\sigma_B/\partial F$:** From the Hagan formula, the numerical sensitivity at $K = 0.04$ is approximately $\partial\sigma_B/\partial F \approx -1.42$ (the backbone effect: as $F$ rises, $\sigma_B$ falls).

$$
\text{Smile correction} = 0.03103 \times (-1.42) = -0.04406
$$

$$
\Delta_{\text{SABR}} = A \times (0.46565 - 0.04406) = 7.82 \times 0.42159 = 3.297
$$

**Bartlett correction.** The additional term accounts for the forward-volatility correlation:

$$
\Delta_{\text{Bartlett}} = \Delta_{\text{SABR}} + A \cdot \mathcal{V}_{\text{Black}} \cdot \frac{\partial\sigma_B}{\partial\alpha} \cdot \frac{\rho\nu}{F^{\beta}}
$$

Computing: $\partial\sigma_B/\partial\alpha \approx 5.32$, and $\rho\nu/F^{\beta} = (-0.3185)(0.4073)/0.18708 = -0.6932$.

$$
\text{Bartlett term} = 7.82 \times 0.03103 \times 5.32 \times (-0.6932) = -0.8945
$$

$$
\Delta_{\text{Bartlett}} = 3.297 - 0.895 = 2.402
$$

| Delta measure | Value | Per \$100M notional |
|---|:---:|:---:|
| Black delta | $A \times 0.466 = 3.643$ | \$3.643M per 1% move |
| SABR delta | $3.297$ | \$3.297M per 1% move |
| Bartlett delta | $2.402$ | \$2.402M per 1% move |

The Bartlett correction reduces the hedge ratio by approximately 27% relative to the Black delta, reflecting the strong negative correlation ($\rho = -0.32$) between the forward and volatility.

### Vega (Sensitivity to Alpha)

$$
\mathcal{V}_{\text{SABR}} = A \cdot \mathcal{V}_{\text{Black}} \cdot \frac{\partial\sigma_B}{\partial\alpha} = 7.82 \times 0.03103 \times 5.32 = 1.290
$$

A 1% increase in $\alpha$ (from 0.03821 to 0.03859) changes the swaption price by approximately 1.290% of notional, or \$1.290M on \$100M.

### Sensitivity to Rho

$$
\frac{\partial V}{\partial\rho} = A \cdot \mathcal{V}_{\text{Black}} \cdot \frac{\partial\sigma_B}{\partial\rho}
$$

From the Hagan formula, $\partial\sigma_B/\partial\rho \approx 0.0445$ at $K = 4.00\%$. Thus:

$$
\frac{\partial V}{\partial\rho} = 7.82 \times 0.03103 \times 0.0445 = 0.01079
$$

A shift of $\Delta\rho = 0.01$ changes the price by approximately 0.011% of notional.

### Sensitivity to Nu

$$
\frac{\partial V}{\partial\nu} = A \cdot \mathcal{V}_{\text{Black}} \cdot \frac{\partial\sigma_B}{\partial\nu}
$$

From the Hagan formula, $\partial\sigma_B/\partial\nu \approx 0.0253$ at $K = 4.00\%$. Thus:

$$
\frac{\partial V}{\partial\nu} = 7.82 \times 0.03103 \times 0.0253 = 0.00614
$$

---

## Example 4: Comparing Model and Market Across the Smile

### Implied Volatility Comparison

The following table extends the calibration validation to include normal (basis-point) implied volatilities, which are the primary quoting convention in EUR markets.

| Strike (%) | Black IV (%) | Normal IV (bps) | Model Black IV (%) | Residual (bps) |
|:---:|:---:|:---:|:---:|:---:|
| 1.50 | 24.80 | 37.2 | 24.68 | $-12$ |
| 2.50 | 22.10 | 55.3 | 22.16 | $+6$ |
| 3.00 | 21.00 | 63.0 | 20.98 | $-2$ |
| 3.50 | 20.20 | 70.7 | 20.20 | $0$ |
| 4.00 | 19.60 | 78.4 | 19.57 | $-3$ |
| 4.50 | 19.20 | 86.4 | 19.12 | $-8$ |
| 5.50 | 18.70 | 102.8 | 18.55 | $-15$ |

!!! note "Residual Analysis"
    The residuals show a systematic pattern: the model slightly underprices the far wings. This is a known limitation of the Hagan formula, which is a second-order perturbation expansion around the ATM point. Possible remedies:

    - Use the arbitrage-free SABR formula (Hagan et al., 2014), which corrects the wing behavior
    - Include the third-order correction terms in the Hagan expansion
    - Use a finite-difference or Monte Carlo solution to the SABR PDE

### Calibration Quality Metrics

| Metric | Value |
|---|---|
| Maximum absolute error | 15 bps |
| Root-mean-square error (RMSE) | 8.5 bps |
| Mean absolute error (MAE) | 6.6 bps |
| ATM error | 0 bps (exact by construction) |
| Number of calibration strikes | 7 (including ATM) |
| Degrees of freedom | 2 ($\rho$, $\nu$; $\alpha$ fixed by ATM) |

---

## Example 5: Recalibration After a 50bp Rate Move

Suppose the forward swap rate moves from $F = 3.50\%$ to $F = 4.00\%$ over one week. How does the SABR model predict the new smile?

### SABR Smile Dynamics

The SABR model's key strength is that it predicts how the smile moves with the forward. With the same parameters $(\alpha, \beta, \rho, \nu) = (0.03821, 0.5, -0.3185, 0.4073)$, the model implied volatilities at the new forward are:

| Strike (%) | IV at $F = 3.50\%$ | IV at $F = 4.00\%$ | Change (bps) |
|:---:|:---:|:---:|:---:|
| 3.00 | 20.98 | 22.41 | $+143$ |
| 3.50 | 20.20 | 21.12 | $+92$ |
| 4.00 | 19.57 | 20.06 | $+49$ |
| 4.50 | 19.12 | 19.22 | $+10$ |
| 5.00 | 18.79 | 18.54 | $-25$ |

The model predicts that when rates rise by 50 bps, the ATM implied volatility increases by approximately 92 bps (from 20.20% to 21.12%). This is the **backbone effect**: with $\beta = 0.5$, the ATM vol scales as $\alpha/F^{0.5}$, so higher $F$ means higher percentage vol (since $\alpha$ is in absolute terms).

!!! warning "Recalibration Is Still Necessary"
    The SABR smile dynamics provide a first-order prediction, but market microstructure, flow dynamics, and regime changes mean that the actual new smile will differ from the SABR prediction. In practice, desks recalibrate SABR parameters daily (or intraday), using yesterday's parameters as the starting point for today's optimization.

---

## Summary

| Example | Key result |
|---|---|
| Calibration | $(\alpha, \rho, \nu) = (0.0382, -0.32, 0.41)$; RMSE = 8.5 bps |
| Swaption pricing | 5Y10Y payer at $K = 4\%$: 335.5 bps of notional |
| Delta | Bartlett delta = 2.40, substantially below Black delta of 3.64 |
| Vega | 1.29% of notional per 1% alpha shift |
| Smile dynamics | 50 bp rate increase raises ATM vol by 92 bps (backbone effect) |

The end-to-end workflow --- calibrate from ATM out, price via Black formula at the SABR implied volatility, hedge using Bartlett-corrected Greeks --- forms the standard SABR pipeline in interest rate trading. Each step relies on the Hagan formula for speed, with the understanding that wing accuracy degrades and arbitrage-free corrections may be needed for precision applications.

---

## Further Reading

- Hagan, P., Kumar, D., Lesniewski, A., and Woodward, D. (2002). "Managing smile risk." *Wilmott Magazine*, 1, 84--108.
- Bartlett, B. (2006). "Hedging under SABR model." *Wilmott Magazine*, July.
- Rebonato, R., McKay, K., and White, R. (2009). *The SABR/LIBOR Market Model*. Wiley.
- Hagan, P., Lesniewski, A., and Woodward, D. (2014). "Probability distribution in the SABR model of stochastic volatility." In *Large Deviations and Asymptotic Methods in Finance*, Springer.
