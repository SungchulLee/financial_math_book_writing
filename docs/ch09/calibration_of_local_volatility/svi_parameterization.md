# SVI Parameterization for Volatility Surfaces

The **Stochastic Volatility Inspired (SVI)** parameterization is an industry-standard method for fitting implied volatility smiles. It provides a parsimonious, arbitrage-aware representation that serves as input for local volatility calibration and exotic pricing.

---

## Motivation

Fitting implied volatility surfaces requires balancing:

- **Flexibility:** Capture observed smile shapes.
- **Parsimony:** Few parameters for stability.
- **Arbitrage-freedom:** Avoid butterfly and calendar arbitrage.
- **Smoothness:** Enable stable differentiation for local vol.

SVI achieves a good trade-off, fitting market smiles with only 5 parameters per maturity while admitting simple arbitrage constraints.

---

## The raw SVI formula

The **raw SVI** parameterization expresses total implied variance $w(k) = T \sigma_{\text{impl}}^2(k)$ as a function of log-moneyness $k = \log(K/F_T)$:

$$
w(k) = a + b \left( \rho (k - m) + \sqrt{(k - m)^2 + \sigma^2} \right).
$$

### Parameter interpretation

| Parameter | Range | Interpretation |
|-----------|-------|----------------|
| $a$ | $a > 0$ | Overall variance level (vertical shift) |
| $b$ | $b \ge 0$ | Slope of the wings (controls steepness) |
| $\rho$ | $-1 < \rho < 1$ | Rotation/skew (negative = downward-sloping left wing) |
| $m$ | $\mathbb{R}$ | Horizontal translation (shift of smile center) |
| $\sigma$ | $\sigma > 0$ | Smoothness at ATM (controls curvature at $k = m$) |

### Geometric interpretation

- At $k = m$: the smile has its minimum curvature.
- As $|k - m| \to \infty$: the wings become linear with slopes $b(1 + \rho)$ (right) and $b(1 - \rho)$ (left).
- The parameter $\sigma$ controls how quickly the transition from curved (near ATM) to linear (wings) occurs.

---

## Alternative parameterizations

### Natural SVI

A reparameterization that decouples ATM behavior:

$$
w(k) = \delta + \frac{\omega}{2} \left( 1 + \zeta \rho (k - \mu) + \sqrt{(\zeta(k - \mu) + \rho)^2 + 1 - \rho^2} \right),
$$

where $\delta$ is ATM variance, $\omega$ is ATM curvature, and $\zeta$ controls wing steepness.

### Jump-wings SVI

Parameterized directly in terms of observable quantities:

- $v_T$: ATM variance
- $\psi_T$: ATM skew
- $p_T$: slope of left wing
- $c_T$: slope of right wing
- $\tilde{v}_T$: minimum variance

This form is useful for interpolating across maturities.

---

## No-arbitrage conditions

### Butterfly arbitrage

The call price must be convex in strike, which requires

$$
\frac{\partial^2 C}{\partial K^2} \ge 0 \quad \Leftrightarrow \quad g(k) \ge 0,
$$

where

$$
g(k) = \left( 1 - \frac{k w'(k)}{2w(k)} \right)^2 - \frac{(w'(k))^2}{4} \left( \frac{1}{w(k)} + \frac{1}{4} \right) + \frac{w''(k)}{2}.
$$

For SVI, this translates to constraints on the parameters.

### Sufficient conditions for butterfly-free SVI

A simple sufficient condition (Gatheral & Jacquier):

$$
b(1 + |\rho|) \le \frac{4}{T}, \qquad a + b\sigma\sqrt{1 - \rho^2} \ge 0.
$$

These ensure non-negative variance and bounded slope.

### Calendar arbitrage

Total variance must be non-decreasing in maturity for fixed log-moneyness:

$$
\frac{\partial w(k, T)}{\partial T} \ge 0 \quad \text{for all } k.
$$

This constrains how SVI parameters can evolve across the term structure.

---

## SSVI: Surface SVI

**SSVI (Surface SVI)** extends SVI to the entire $(k, T)$ surface while guaranteeing no calendar arbitrage by construction.

### The SSVI formula

$$
w(k, \theta_T) = \frac{\theta_T}{2} \left( 1 + \rho \phi(\theta_T) k + \sqrt{(\phi(\theta_T) k + \rho)^2 + 1 - \rho^2} \right),
$$

where:

- $\theta_T = \sigma_{\text{ATM}}^2(T) \cdot T$ is ATM total variance.
- $\phi(\theta)$ is a function controlling the smile shape.

### Common choices for $\phi(\theta)$

**Power-law:**
$$
\phi(\theta) = \frac{\eta}{\theta^\gamma (1 + \theta)^{1 - \gamma}}, \quad \eta > 0, \; 0 \le \gamma \le 1.
$$

**Heston-like:**
$$
\phi(\theta) = \frac{1}{\lambda \theta} \left( 1 - \frac{1 - e^{-\lambda \theta}}{\lambda \theta} \right).
$$

### Arbitrage-free by design

SSVI is constructed so that:

- Calendar arbitrage is automatically excluded (monotonicity in $\theta_T$).
- Butterfly arbitrage can be checked via simple parameter bounds.

This makes SSVI the preferred choice for building arbitrage-free volatility surfaces.

---

## Calibration of SVI

### Per-slice calibration

For each maturity $T$:

1. Extract market implied vols $\{\sigma_{\text{impl}}(K_i, T)\}$.
2. Convert to total variance: $w_i = T \sigma_{\text{impl}}^2(K_i, T)$.
3. Convert strikes to log-moneyness: $k_i = \log(K_i / F_T)$.
4. Minimize:
   $$
   \min_{a, b, \rho, m, \sigma} \sum_i \omega_i \left( w^{\text{SVI}}(k_i; a, b, \rho, m, \sigma) - w_i \right)^2.
   $$
5. Enforce constraints (e.g., $b \ge 0$, $|\rho| < 1$, arbitrage conditions).

### Initialization strategies

Good initialization is critical due to non-convexity:

1. **Moment matching:** Set $a \approx w_{\text{ATM}}$, estimate $b$ from wing slopes, $\rho$ from skew.
2. **Grid search:** Evaluate on a coarse grid, refine with local optimization.
3. **Quasi-explicit formulas:** Zeliade's method provides closed-form approximations.

### Global calibration (SSVI)

For SSVI, calibrate across all maturities simultaneously:

1. Fit ATM variance term structure $\theta_T$.
2. Calibrate $(\rho, \eta, \gamma)$ or $(\rho, \lambda)$ globally.
3. Check arbitrage conditions; adjust if violated.

---

## From SVI to local volatility

Once an arbitrage-free implied variance surface $w(k, T)$ is obtained, Dupire's formula yields local variance:

$$
\sigma_{\text{loc}}^2(K, T) = \frac{\partial_T w}{1 - \frac{k}{w} \partial_k w + \frac{1}{4}\left( -\frac{1}{4} - \frac{1}{w} + \frac{k^2}{w^2} \right)(\partial_k w)^2 + \frac{1}{2} \partial_{kk} w}.
$$

### Analytic derivatives

SVI admits closed-form derivatives:

$$
\partial_k w = b \left( \rho + \frac{k - m}{\sqrt{(k - m)^2 + \sigma^2}} \right),
$$

$$
\partial_{kk} w = \frac{b \sigma^2}{((k - m)^2 + \sigma^2)^{3/2}},
$$

$$
\partial_T w = \frac{\partial a}{\partial T} + \frac{\partial b}{\partial T} \left( \cdots \right) + \cdots
$$

For SSVI, derivatives with respect to $T$ come from the dependence on $\theta_T$.

### Stability advantages

Using SVI/SSVI rather than raw interpolation:

- Provides smooth, analytic derivatives.
- Avoids numerical differentiation noise.
- Guarantees arbitrage-free inputs to Dupire.

---

## Practical workflow

A robust local volatility calibration pipeline:

1. **Data preparation:**
   - Filter illiquid quotes.
   - Convert to forward moneyness and total variance.

2. **Per-slice SVI fit:**
   - Calibrate SVI to each maturity.
   - Check butterfly conditions; re-fit or widen constraints if violated.

3. **Term structure interpolation:**
   - Fit SSVI or interpolate SVI parameters across maturities.
   - Ensure calendar arbitrage freedom.

4. **Local vol extraction:**
   - Apply Dupire using analytic SVI derivatives.
   - Smooth mildly if residual noise remains.

5. **Validation:**
   - Reprice vanillas; check fit quality.
   - Price simple exotics (barriers); check for spikes.

---

## Limitations of SVI

- **Wing behavior:** SVI wings are asymptotically linear, which may not match all markets (e.g., equity index with steeper put wings).
- **Short maturities:** Near expiry, smiles can be sharper than SVI accommodates.
- **Extreme strikes:** Extrapolation beyond observed data requires care.

Extensions (eSSVI, extended SSVI) address some limitations by allowing more flexible wing shapes.

---

## Key takeaways

- SVI provides a parsimonious, interpretable smile parameterization.
- SSVI extends SVI to a full surface with built-in calendar arbitrage freedom.
- Analytic derivatives make SVI ideal for local volatility calibration.
- Proper initialization and constraint handling are essential for robust fits.
- SVI is not perfect for all markets; know its limitations.

---

## Further reading

- Gatheral, *The Volatility Surface* (original SVI exposition).
- Gatheral & Jacquier, "Arbitrage-Free SVI Volatility Surfaces" (2014).
- De Marco & Martini, "Quasi-Explicit Calibration of SVI" (Zeliade white paper).
- Hendriks & Martini, "Extended SSVI" (2019).
