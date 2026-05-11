# Calibration to Implied Volatility Smile

A model is only as useful as its ability to match observed market prices. **Calibration** determines the Merton jump-diffusion parameters $(\sigma, \lambda, \mu_J, \sigma_J)$ by fitting model prices to the implied volatility surface extracted from traded options. This section develops the calibration methodology, discusses the role of each parameter in shaping the smile, identifies common pitfalls, and presents typical calibrated values for equity index options.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Formulate the calibration problem as a nonlinear least-squares optimization
    2. Explain how each Merton parameter controls a specific feature of the implied volatility smile
    3. Implement a calibration procedure using the Merton series formula
    4. Interpret calibrated parameters and assess the quality of the fit

---

## The Implied Volatility Smile

### From Prices to Implied Volatility

Market option prices are quoted in terms of implied volatility: the constant $\sigma_{\text{imp}}$ that, when plugged into the Black-Scholes formula, reproduces the observed price. For a given maturity $T$, plotting $\sigma_{\text{imp}}$ against the strike $K$ (or log-moneyness $k = \ln(K/F)$ where $F = S_0 e^{rT}$ is the forward price) reveals the **smile** or **skew**.

### Features the Merton Model Must Capture

Equity index options typically display:

- **Negative skew**: OTM puts have higher implied volatility than OTM calls
- **Steeper skew at short maturities**: The smile flattens as $T$ increases
- **Moderate convexity**: Both deep OTM puts and calls have elevated implied volatility relative to ATM

The Merton model generates all three features through its jump parameters.

---

## Parameter-to-Smile Mapping

### How Each Parameter Affects the Smile

Understanding the role of each parameter is essential for efficient calibration.

!!! info "Proposition: Parameter Sensitivities"
    | Parameter | Primary effect on IV smile |
    |-----------|---------------------------|
    | $\sigma$ | ATM level (parallel shift) |
    | $\lambda$ | Overall smile amplitude (more jumps = more smile) |
    | $\mu_J$ | Skew direction and magnitude ($\mu_J < 0$ gives negative skew) |
    | $\sigma_J$ | Smile convexity (curvature around ATM) |

**Diffusion volatility $\sigma$:** Controls the baseline ATM implied volatility. Increasing $\sigma$ shifts the entire smile upward approximately in parallel.

**Jump intensity $\lambda$:** Controls how much the smile deviates from the flat Black-Scholes line. With $\lambda = 0$, the smile is perfectly flat. Increasing $\lambda$ amplifies both the skew and the curvature, with the effect strongest at short maturities.

**Jump mean $\mu_J$:** Controls the **asymmetry** (skew) of the smile. When $\mu_J < 0$, downward jumps are more likely, producing a steeper left wing (OTM puts are more expensive). When $\mu_J = 0$, the smile is approximately symmetric around ATM.

**Jump volatility $\sigma_J$:** Controls the **curvature** of the smile. Larger $\sigma_J$ means more dispersed jump sizes, lifting both wings of the smile (deep OTM puts and calls both become more expensive).

### Term Structure of the Smile

The jump contribution to implied volatility decays with maturity. The approximate implied variance is:

$$
\sigma_{\text{imp}}^2(T) \approx \sigma^2 + \frac{\lambda(\sigma_J^2 + \mu_J^2)}{1}
$$

for ATM options, while the skew contribution scales as:

$$
\text{skew} \propto \frac{\lambda\mu_J}{\sqrt{T}}
$$

This $1/\sqrt{T}$ decay matches the empirical observation that short-maturity smiles are much steeper than long-maturity smiles.

---

## Calibration Formulation

### The Objective Function

Given $N_{\text{obs}}$ observed market implied volatilities $\{\sigma_{\text{mkt}}^{(i)}\}$ at strikes $\{K_i\}$ and maturities $\{T_i\}$, the calibration problem is:

$$
\min_{\boldsymbol{\theta}} \sum_{i=1}^{N_{\text{obs}}} w_i \left(\sigma_{\text{model}}^{(i)}(\boldsymbol{\theta}) - \sigma_{\text{mkt}}^{(i)}\right)^2
$$

where $\boldsymbol{\theta} = (\sigma, \lambda, \mu_J, \sigma_J)$ and $w_i$ are weights (often proportional to the inverse bid-ask spread or vega).

!!! tip "Calibrating in IV Space vs Price Space"
    Calibrating in implied volatility space (rather than price space) is preferred because:

    - IVs are on a comparable scale across strikes and maturities
    - Deep OTM options have small prices but meaningful IVs
    - The objective function landscape is smoother in IV space

### Computing Model Implied Volatility

For each trial $\boldsymbol{\theta}$:

1. Compute the Merton price $C_{\text{Merton}}(K_i, T_i; \boldsymbol{\theta})$ using the series formula
2. Invert the Black-Scholes formula numerically to find $\sigma_{\text{model}}^{(i)}$ such that $C_{\text{BS}}(K_i, T_i, \sigma_{\text{model}}^{(i)}) = C_{\text{Merton}}(K_i, T_i; \boldsymbol{\theta})$

The inversion is fast (Newton's method converges in 3--5 iterations using vega as the derivative).

### Constraints

The parameters must satisfy physical constraints:

$$
\sigma > 0, \quad \lambda \geq 0, \quad \sigma_J > 0
$$

The jump mean $\mu_J$ is unconstrained. Additionally, the total variance must be positive:

$$
\sigma^2 + \lambda(\sigma_J^2 + \mu_J^2) > 0
$$

which is automatically satisfied when $\sigma > 0$.

---

## Optimization Methods

### Gradient-Based Methods

The Levenberg-Marquardt algorithm is well-suited for the nonlinear least-squares structure. It requires the Jacobian $\partial\sigma_{\text{model}}^{(i)}/\partial\theta_j$, which can be computed analytically through the chain rule:

$$
\frac{\partial\sigma_{\text{model}}^{(i)}}{\partial\theta_j} = \frac{\partial C_{\text{Merton}}^{(i)}/\partial\theta_j}{\text{vega}_{\text{BS}}^{(i)}}
$$

where $\text{vega}_{\text{BS}}^{(i)} = \partial C_{\text{BS}}/\partial\sigma_{\text{imp}}$ is the Black-Scholes vega.

### Global Optimization

The objective function typically has multiple local minima due to parameter redundancies (e.g., increasing $\lambda$ and decreasing $\sigma_J$ can produce similar smiles). Strategies to find the global minimum include:

- **Multi-start**: Run Levenberg-Marquardt from many random initial points
- **Differential evolution**: A population-based global optimizer that is derivative-free
- **Sequential approach**: First fit $\sigma$ to ATM options, then fit $(\lambda, \mu_J, \sigma_J)$ to the smile shape

### Regularization

To improve stability and avoid overfitting to noisy market data:

$$
\min_{\boldsymbol{\theta}} \sum_i w_i(\sigma_{\text{model}}^{(i)} - \sigma_{\text{mkt}}^{(i)})^2 + \alpha\|\boldsymbol{\theta} - \boldsymbol{\theta}_0\|^2
$$

where $\boldsymbol{\theta}_0$ is a prior estimate and $\alpha > 0$ is the regularization strength.

---

## Typical Calibrated Values

### Equity Index Options (S&P 500)

!!! example "Typical Parameters"
    | Parameter | Typical range | Interpretation |
    |-----------|--------------|----------------|
    | $\sigma$ | 0.10 -- 0.18 | Diffusion vol (lower than total IV) |
    | $\lambda$ | 0.5 -- 3.0 | 0.5 to 3 jumps per year |
    | $\mu_J$ | $-0.15$ to $-0.05$ | 5% to 15% average downward jump |
    | $\sigma_J$ | 0.10 -- 0.40 | Jump size dispersion |

    The total ATM implied volatility is approximately:

    $$
    \sigma_{\text{ATM}} \approx \sqrt{\sigma^2 + \lambda(\sigma_J^2 + \mu_J^2)} \approx 0.20 \text{ to } 0.30
    $$

### Quality of Fit

The Merton model typically achieves:

- **Good fit** at short maturities (1--3 months): jumps dominate and the model has enough flexibility
- **Moderate fit** at medium maturities (6--12 months): the smile flattens faster than the model predicts
- **Poor fit** at long maturities (1+ years): the model cannot reproduce the persistent smile/skew because the jump contribution diminishes as $1/\sqrt{T}$

This limitation motivates the Bates model (Heston + jumps), which uses stochastic volatility to sustain the smile at long maturities.

---

## Identifiability and Pitfalls

### Parameter Correlations

The four parameters are not fully identifiable from ATM options alone:

- $\sigma^2$ and $\lambda\sigma_J^2$ both contribute to ATM variance: you need OTM options to separate them
- $\lambda$ and $\sigma_J$ are partially interchangeable: more frequent small jumps can mimic fewer large jumps

!!! warning "Common Calibration Pitfalls"

    1. **Fitting ATM only**: Produces many equivalent parameter sets. Always include OTM strikes.
    2. **Ignoring maturity structure**: Calibrating to a single maturity leaves the $1/\sqrt{T}$ decay unconstrained.
    3. **Negative $\sigma^2$**: Can occur if the optimizer pushes all variance into the jump component. Use $\sigma > 0$ as a hard constraint.
    4. **Unstable day-to-day parameters**: High sensitivity to market noise. Regularization or Bayesian priors help stabilize.

### Goodness-of-Fit Metrics

| Metric | Definition | Target |
|--------|-----------|--------|
| RMSE (IV) | $\sqrt{\frac{1}{N}\sum(\sigma_{\text{model}} - \sigma_{\text{mkt}})^2}$ | $< 0.5\%$ |
| Max error | $\max_i |\sigma_{\text{model}}^{(i)} - \sigma_{\text{mkt}}^{(i)}|$ | $< 1.5\%$ |
| Weighted RMSE | $\sqrt{\frac{\sum w_i(\sigma_{\text{model}} - \sigma_{\text{mkt}})^2}{\sum w_i}}$ | $< 0.3\%$ |

---

## Summary

Calibration of the Merton jump-diffusion model fits the four parameters $(\sigma, \lambda, \mu_J, \sigma_J)$ to the observed implied volatility surface by minimizing a nonlinear least-squares objective. Each parameter controls a specific feature of the smile: $\sigma$ sets the ATM level, $\lambda$ scales the overall smile amplitude, $\mu_J$ determines the skew, and $\sigma_J$ governs the curvature. The model fits short-maturity smiles well but struggles at longer maturities because the jump contribution decays as $1/\sqrt{T}$, motivating extensions such as the Bates model that add stochastic volatility for persistent smile dynamics.

## Exercises

**Exercise 1.** Formulate the Merton calibration problem as a nonlinear least-squares optimization. Write the objective function explicitly, identify the four parameters being optimized, and state the constraints each parameter must satisfy.

??? success "Solution to Exercise 1"
    The Merton calibration problem is formulated as follows. Given $N_{\text{obs}}$ observed market implied volatilities $\{\sigma_{\text{mkt}}^{(i)}\}$ at strikes $\{K_i\}$ and maturities $\{T_i\}$, the objective function is

    $$
    \min_{\boldsymbol{\theta}} \sum_{i=1}^{N_{\text{obs}}} w_i \left(\sigma_{\text{model}}^{(i)}(\boldsymbol{\theta}) - \sigma_{\text{mkt}}^{(i)}\right)^2
    $$

    where $\boldsymbol{\theta} = (\sigma, \lambda, \mu_J, \sigma_J)$ is the parameter vector and $w_i$ are weights (e.g., proportional to inverse bid-ask spread or vega).

    The four parameters and their constraints are:

    - $\sigma > 0$: diffusion volatility, must be strictly positive
    - $\lambda \geq 0$: jump intensity, must be non-negative
    - $\mu_J \in \mathbb{R}$: mean log-jump size, unconstrained
    - $\sigma_J > 0$: jump size dispersion, must be strictly positive

    For each trial $\boldsymbol{\theta}$, the model implied volatility $\sigma_{\text{model}}^{(i)}$ is obtained by computing the Merton price $C_{\text{Merton}}(K_i, T_i; \boldsymbol{\theta})$ using the series formula and then numerically inverting the Black-Scholes formula. The total variance must also satisfy $\sigma^2 + \lambda(\sigma_J^2 + \mu_J^2) > 0$, which is automatically satisfied when $\sigma > 0$.

---


**Exercise 2.** Explain how each of the four Merton parameters $(\sigma, \lambda, \mu_J, \sigma_J)$ controls a different feature of the implied volatility smile. Given a market smile that is steeply skewed with moderate curvature, which parameters would you expect to have large absolute values?

??? success "Solution to Exercise 2"
    Each of the four Merton parameters controls a distinct feature of the implied volatility smile:

    - **$\sigma$ (diffusion volatility):** Controls the ATM implied volatility level. Increasing $\sigma$ shifts the entire smile upward approximately in parallel.
    - **$\lambda$ (jump intensity):** Controls the overall amplitude of the smile. With $\lambda = 0$ the smile is flat (Black-Scholes). Increasing $\lambda$ amplifies both skew and curvature, with the strongest effect at short maturities.
    - **$\mu_J$ (mean log-jump):** Controls the asymmetry (skew) of the smile. When $\mu_J < 0$, downward jumps are more likely, producing a steeper left wing (higher IV for OTM puts). When $\mu_J = 0$, the smile is approximately symmetric.
    - **$\sigma_J$ (jump size dispersion):** Controls the curvature (convexity) of the smile. Larger $\sigma_J$ lifts both wings, making deep OTM puts and calls more expensive.

    For a market smile that is steeply skewed with moderate curvature, we would expect $|\mu_J|$ to be large (e.g., $\mu_J \approx -0.10$ to $-0.15$), indicating strong downward jump bias, and $\lambda$ to be moderate to large (e.g., $\lambda \geq 1$) to amplify the skew effect. The parameter $\sigma_J$ would be moderate since the curvature is not extreme.

---


**Exercise 3.** The skew contribution to implied volatility decays as $\lambda\mu_J/\sqrt{T}$. For $\lambda = 1.0$ and $\mu_J = -0.10$: (a) Compute the skew contribution at $T = 1$ month, $T = 6$ months, and $T = 2$ years. (b) Explain why this decay means the Merton model fits short-maturity smiles better than long-maturity smiles.

??? success "Solution to Exercise 3"
    **(a)** The skew contribution is proportional to $\lambda\mu_J/\sqrt{T}$. With $\lambda = 1.0$ and $\mu_J = -0.10$:

    At $T = 1/12$ (1 month):

    $$
    \frac{\lambda\mu_J}{\sqrt{T}} = \frac{(1.0)(-0.10)}{\sqrt{1/12}} = \frac{-0.10}{0.2887} \approx -0.346
    $$

    At $T = 0.5$ (6 months):

    $$
    \frac{\lambda\mu_J}{\sqrt{T}} = \frac{-0.10}{\sqrt{0.5}} = \frac{-0.10}{0.7071} \approx -0.141
    $$

    At $T = 2$ (2 years):

    $$
    \frac{\lambda\mu_J}{\sqrt{T}} = \frac{-0.10}{\sqrt{2}} = \frac{-0.10}{1.414} \approx -0.0707
    $$

    **(b)** The skew contribution at 1 month ($-0.346$) is about 4.9 times larger than at 2 years ($-0.0707$). This $1/\sqrt{T}$ decay means that jumps dominate the smile shape at short maturities, where the Merton model has enough flexibility to match the steep observed skew. At longer maturities, the jump contribution becomes negligible relative to the diffusion component, so the smile flattens. Since real markets retain a persistent (though flattening) smile even at long maturities, the Merton model cannot fit those maturities well. This motivates extensions such as the Bates model that add stochastic volatility for persistent smile dynamics.

---


**Exercise 4.** The calibration gradient involves the chain rule $\partial\sigma_{\text{model}}^{(i)}/\partial\theta_j = (\partial C_{\text{Merton}}^{(i)}/\partial\theta_j)/\text{vega}_{\text{BS}}^{(i)}$. Explain why dividing by the Black-Scholes vega converts a price sensitivity into an implied volatility sensitivity. Why is calibration in IV space preferred over price space?

??? success "Solution to Exercise 4"
    The chain rule $\partial\sigma_{\text{model}}^{(i)}/\partial\theta_j = (\partial C_{\text{Merton}}^{(i)}/\partial\theta_j)/\text{vega}_{\text{BS}}^{(i)}$ works because the implied volatility $\sigma_{\text{model}}^{(i)}$ is defined implicitly by

    $$
    C_{\text{BS}}(K_i, T_i, \sigma_{\text{model}}^{(i)}) = C_{\text{Merton}}(K_i, T_i; \boldsymbol{\theta})
    $$

    Differentiating both sides with respect to $\theta_j$ using the implicit function theorem:

    $$
    \frac{\partial C_{\text{BS}}}{\partial \sigma_{\text{imp}}} \cdot \frac{\partial \sigma_{\text{model}}^{(i)}}{\partial \theta_j} = \frac{\partial C_{\text{Merton}}^{(i)}}{\partial \theta_j}
    $$

    Since $\partial C_{\text{BS}}/\partial \sigma_{\text{imp}} = \text{vega}_{\text{BS}}^{(i)}$, solving gives the stated formula. Dividing by vega converts a price sensitivity (dollars per unit parameter change) into an implied volatility sensitivity (vol points per unit parameter change).

    Calibration in IV space is preferred because:

    - Implied volatilities are on a comparable scale across strikes and maturities (typically 15--40%), while option prices vary by orders of magnitude (from cents for deep OTM to tens of dollars for ITM)
    - Deep OTM options have small prices but meaningful IVs, so price-space calibration would underweight them
    - The objective function landscape is smoother in IV space, leading to better optimizer convergence

---


**Exercise 5.** Discuss two common pitfalls in Merton model calibration: (a) fitting only to ATM options, and (b) parameter instability across days. For each pitfall, describe the symptom and a practical remedy (e.g., including OTM strikes, regularization).

??? success "Solution to Exercise 5"
    **(a) Fitting only to ATM options.** The symptom is that many different parameter sets produce equally good fits, because the four parameters are not identifiable from ATM data alone. In particular, $\sigma^2$ and $\lambda(\sigma_J^2 + \mu_J^2)$ both contribute to ATM variance and cannot be separated. The optimizer may converge to parameter sets with unrealistically large $\lambda$ and small $\sigma$, or vice versa. The remedy is to include a range of OTM strikes in the calibration, since the skew (controlled by $\mu_J$) and curvature (controlled by $\sigma_J$) are only visible in OTM options. Including both OTM puts and calls across several maturities pins down all four parameters.

    **(b) Parameter instability across days.** The symptom is that calibrated parameters fluctuate significantly from one day to the next, even when the market smile has changed only slightly. This occurs because the objective function has a relatively flat valley in parameter space, making the minimum sensitive to small perturbations in input data. The remedy is regularization: add a penalty term $\alpha\|\boldsymbol{\theta} - \boldsymbol{\theta}_0\|^2$ to the objective function, where $\boldsymbol{\theta}_0$ is the previous day's calibrated parameters (or a prior estimate) and $\alpha > 0$ controls the regularization strength. This anchors the parameters to a stable reference, smoothing day-to-day fluctuations while still allowing the calibration to track genuine market movements.

---
