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
w(k) = a + b \left( \rho (k - m) + \sqrt{(k - m)^2 + \sigma^2} \right)
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
w(k) = \delta + \frac{\omega}{2} \left( 1 + \zeta \rho (k - \mu) + \sqrt{(\zeta(k - \mu) + \rho)^2 + 1 - \rho^2} \right)
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
\frac{\partial^2 C}{\partial K^2} \ge 0 \quad \Leftrightarrow \quad g(k) \ge 0
$$

where

$$
g(k) = \left( 1 - \frac{k w'(k)}{2w(k)} \right)^2 - \frac{(w'(k))^2}{4} \left( \frac{1}{w(k)} + \frac{1}{4} \right) + \frac{w''(k)}{2}
$$

For SVI, this translates to constraints on the parameters.

### Sufficient conditions for butterfly-free SVI

A simple sufficient condition (Gatheral & Jacquier):

$$
b(1 + |\rho|) \le \frac{4}{T}, \qquad a + b\sigma\sqrt{1 - \rho^2} \ge 0
$$

These ensure non-negative variance and bounded slope.

### Calendar arbitrage

Total variance must be non-decreasing in maturity for fixed log-moneyness:

$$
\frac{\partial w(k, T)}{\partial T} \ge 0 \quad \text{for all } k
$$

This constrains how SVI parameters can evolve across the term structure.

---

## SSVI: Surface SVI

**SSVI (Surface SVI)** extends SVI to the entire $(k, T)$ surface while guaranteeing no calendar arbitrage by construction.

### The SSVI formula

$$
w(k, \theta_T) = \frac{\theta_T}{2} \left( 1 + \rho \phi(\theta_T) k + \sqrt{(\phi(\theta_T) k + \rho)^2 + 1 - \rho^2} \right)
$$

where:

- $\theta_T = \sigma_{\text{ATM}}^2(T) \cdot T$ is ATM total variance.
- $\phi(\theta)$ is a function controlling the smile shape.

### Common choices for φ(θ)

**Power-law:**

$$
\phi(\theta) = \frac{\eta}{\theta^\gamma (1 + \theta)^{1 - \gamma}}, \quad \eta > 0, \; 0 \le \gamma \le 1
$$

**Heston-like:**

$$
\phi(\theta) = \frac{1}{\lambda \theta} \left( 1 - \frac{1 - e^{-\lambda \theta}}{\lambda \theta} \right)
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
   \min_{a, b, \rho, m, \sigma} \sum_i \omega_i \left( w^{\text{SVI}}(k_i; a, b, \rho, m, \sigma) - w_i \right)^2
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
\sigma_{\text{loc}}^2(K, T) = \frac{\partial_T w}{1 - \frac{k}{w} \partial_k w + \frac{1}{4}\left( -\frac{1}{4} - \frac{1}{w} + \frac{k^2}{w^2} \right)(\partial_k w)^2 + \frac{1}{2} \partial_{kk} w}
$$

### Analytic derivatives

SVI admits closed-form derivatives:

$$
\partial_k w = b \left( \rho + \frac{k - m}{\sqrt{(k - m)^2 + \sigma^2}} \right)
$$

$$
\partial_{kk} w = \frac{b \sigma^2}{((k - m)^2 + \sigma^2)^{3/2}}
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

---

## Exercises

**Exercise 1.** For the raw SVI formula $w(k) = a + b(\rho(k-m) + \sqrt{(k-m)^2 + \sigma^2})$, compute the asymptotic slopes of the left and right wings:

$$
\lim_{k \to -\infty} \frac{w(k)}{|k|} \quad \text{and} \quad \lim_{k \to +\infty} \frac{w(k)}{k}
$$

Express your answers in terms of $b$ and $\rho$. Verify that when $\rho < 0$, the left wing is steeper than the right, consistent with equity index skew.

??? success "Solution to Exercise 1"
    For $k \to +\infty$ (right wing), note that $\sqrt{(k-m)^2 + \sigma^2} \approx |k - m| = k - m$ for large $k$, so

    $$
    w(k) \approx a + b\bigl(\rho(k-m) + (k - m)\bigr) = a + b(1 + \rho)(k - m)
    $$

    Thus

    $$
    \lim_{k \to +\infty} \frac{w(k)}{k} = b(1 + \rho)
    $$

    For $k \to -\infty$ (left wing), $\sqrt{(k-m)^2 + \sigma^2} \approx |k - m| = m - k$, so

    $$
    w(k) \approx a + b\bigl(\rho(k-m) + (m - k)\bigr) = a + b(1 - \rho)(m - k)
    $$

    Since $|k| = -k$ for $k \to -\infty$:

    $$
    \lim_{k \to -\infty} \frac{w(k)}{|k|} = b(1 - \rho)
    $$

    **Verification of skew:** When $\rho < 0$:

    - Left wing slope: $b(1 - \rho) = b(1 + |\rho|)$
    - Right wing slope: $b(1 + \rho) = b(1 - |\rho|)$

    Since $|\rho| > 0$, we have $b(1 + |\rho|) > b(1 - |\rho|)$, confirming that the left wing is steeper than the right wing. This is consistent with the equity index volatility skew, where put options (left wing, $k < 0$) have higher implied volatility than calls (right wing, $k > 0$), producing a steeper rise in total variance on the left.

---

**Exercise 2.** Show that the SVI total variance at the center $k = m$ is $w(m) = a + b\sigma$. Use the sufficient no-arbitrage condition $a + b\sigma\sqrt{1-\rho^2} \ge 0$ to derive a lower bound on $a$ in terms of $b$, $\sigma$, and $\rho$. For $b = 0.3$, $\sigma = 0.1$, $\rho = -0.7$, compute this lower bound.

??? success "Solution to Exercise 2"
    At the center $k = m$, we have $(k - m)^2 = 0$, so

    $$
    w(m) = a + b\bigl(\rho \cdot 0 + \sqrt{0 + \sigma^2}\bigr) = a + b\sigma
    $$

    The sufficient no-arbitrage condition requires $a + b\sigma\sqrt{1 - \rho^2} \ge 0$. Rearranging for a lower bound on $a$:

    $$
    a \ge -b\sigma\sqrt{1 - \rho^2}
    $$

    **Numerical computation:** With $b = 0.3$, $\sigma = 0.1$, $\rho = -0.7$:

    $$
    \sqrt{1 - \rho^2} = \sqrt{1 - 0.49} = \sqrt{0.51} \approx 0.7141
    $$

    $$
    a \ge -0.3 \times 0.1 \times 0.7141 = -0.02142
    $$

    So the lower bound on $a$ is approximately $-0.0214$.

    Note that this means $a$ can be slightly negative, which is permissible. The total variance at any point $w(k)$ is not just $a$---it includes the positive contribution $b(\rho(k-m) + \sqrt{(k-m)^2 + \sigma^2})$. The condition ensures that $w(k) \ge 0$ everywhere, which is necessary since total variance must be non-negative.

    With this lower bound, the minimum total variance is $w(m) = a + b\sigma \ge -b\sigma\sqrt{1-\rho^2} + b\sigma = b\sigma(1 - \sqrt{1-\rho^2}) > 0$, confirming positivity.

---

**Exercise 3.** Verify analytically that the SVI second derivative with respect to log-moneyness is

$$
\partial_{kk}w = \frac{b\sigma^2}{((k-m)^2 + \sigma^2)^{3/2}}
$$

Show that $\partial_{kk}w > 0$ for all $k$ when $b > 0$ and $\sigma > 0$. Explain why this property is important for the denominator of the Dupire formula.

??? success "Solution to Exercise 3"
    Let $u = k - m$. The SVI formula is $w(k) = a + b(\rho u + \sqrt{u^2 + \sigma^2})$. The first derivative is

    $$
    \partial_k w = b\left(\rho + \frac{u}{\sqrt{u^2 + \sigma^2}}\right)
    $$

    Taking the second derivative, we differentiate $u/\sqrt{u^2 + \sigma^2}$ with respect to $u$ (equivalently $k$):

    $$
    \frac{d}{du}\left(\frac{u}{\sqrt{u^2 + \sigma^2}}\right) = \frac{\sqrt{u^2 + \sigma^2} - u \cdot \frac{u}{\sqrt{u^2 + \sigma^2}}}{u^2 + \sigma^2}
    $$

    $$
    = \frac{\frac{u^2 + \sigma^2 - u^2}{\sqrt{u^2+\sigma^2}}}{u^2 + \sigma^2} = \frac{\sigma^2}{(u^2 + \sigma^2)^{3/2}}
    $$

    Therefore

    $$
    \partial_{kk}w = \frac{b\sigma^2}{((k-m)^2 + \sigma^2)^{3/2}}
    $$

    **Positivity:** Since $b > 0$ (given), $\sigma^2 > 0$ (given), and $((k-m)^2 + \sigma^2)^{3/2} > 0$ for all $k$ (as a positive number raised to a positive power), we have

    $$
    \partial_{kk}w > 0 \quad \text{for all } k \in \mathbb{R}
    $$

    **Importance for the Dupire formula:** In the Dupire formula expressed in total variance coordinates, the denominator contains the term $\frac{1}{2}\partial_{kk}w$. This term contributes positively to the denominator. The full denominator is

    $$
    1 - \frac{k}{w}\partial_k w + \frac{1}{4}\left(-\frac{1}{4} - \frac{1}{w} + \frac{k^2}{w^2}\right)(\partial_k w)^2 + \frac{1}{2}\partial_{kk}w
    $$

    Having $\partial_{kk}w > 0$ ensures that this positive contribution is always present, helping to keep the overall denominator positive (which is the butterfly no-arbitrage condition expressed in these coordinates). If $\partial_{kk}w$ could be negative or zero, the denominator would be more prone to vanishing or becoming negative, leading to unphysical local variance values. The guaranteed positivity of SVI's second derivative thus provides a structural safeguard against butterfly arbitrage violations.

---

**Exercise 4.** Consider a market with ATM total variance $w_{\text{ATM}} = 0.04$, left-wing slope approximately $0.45$, and right-wing slope approximately $0.15$. Using the asymptotic wing formulas from Exercise 1, set up a system of equations for $b$ and $\rho$. Solve for $b$ and $\rho$, then choose initial values for $a$, $m$, and $\sigma$ to begin a local optimization. Describe your reasoning for each initial value.

??? success "Solution to Exercise 4"
    **Setting up equations from wing slopes:**

    From Exercise 1, the asymptotic wing slopes are:

    - Left wing slope: $b(1 - \rho) \approx 0.45$
    - Right wing slope: $b(1 + \rho) \approx 0.15$

    This gives two equations in two unknowns:

    $$
    b(1 - \rho) = 0.45
    $$

    $$
    b(1 + \rho) = 0.15
    $$

    **Solving for $b$ and $\rho$:** Adding the two equations:

    $$
    2b = 0.45 + 0.15 = 0.60 \implies b = 0.30
    $$

    Subtracting the second from the first:

    $$
    -2b\rho = 0.45 - 0.15 = 0.30 \implies \rho = -\frac{0.30}{0.60} = -0.50
    $$

    **Verification:** $b(1 - \rho) = 0.30 \times 1.50 = 0.45$ and $b(1 + \rho) = 0.30 \times 0.50 = 0.15$. Correct.

    **Choosing initial values for $a$, $m$, $\sigma$:**

    - **$a$ (overall level):** At $k = m$, $w(m) = a + b\sigma$. Since ATM total variance is $w_{\text{ATM}} = 0.04$ and ATM corresponds approximately to $k = 0$, if we start with $m = 0$, then $a + b\sigma \approx 0.04$, giving $a \approx 0.04 - 0.30\sigma$. A reasonable starting guess for $\sigma$ gives $a$. With $\sigma = 0.05$ (see below), $a \approx 0.04 - 0.015 = 0.025$.

    - **$m$ (horizontal shift):** The minimum of the smile typically occurs near the forward, so $m \approx 0$ is a natural starting point. If the market smile minimum is slightly off-center, $m$ can be adjusted, but zero is a robust initialization.

    - **$\sigma$ (ATM curvature):** This parameter controls how quickly the smile transitions from curved (near ATM) to linear (wings). A smaller $\sigma$ makes the transition sharper. A reasonable starting value is $\sigma \approx 0.05$ to $0.10$, based on the observation that the smile curvature is concentrated within one or two standard deviations of $k = m$ in typical equity markets.

    **Summary of initial guess:** $(a, b, \rho, m, \sigma) = (0.025, 0.30, -0.50, 0.0, 0.05)$. This should be refined using a local optimizer (e.g., Levenberg--Marquardt) with bounds $b \ge 0$, $|\rho| < 1$, $\sigma > 0$.

---

**Exercise 5.** For the SSVI parameterization with power-law $\phi(\theta) = \eta/(\theta^\gamma(1+\theta)^{1-\gamma})$, show that the condition for absence of butterfly arbitrage at $k = 0$ imposes an upper bound on $\eta$ that depends on $\rho$. Specifically, show that $\eta(1 + |\rho|) \le 2$ is sufficient. What happens to the smile curvature when $\eta$ approaches this upper bound?

??? success "Solution to Exercise 5"
    The SSVI formula at $k = 0$ (ATM) simplifies because the general formula is

    $$
    w(k, \theta_T) = \frac{\theta_T}{2}\left(1 + \rho\phi(\theta_T)k + \sqrt{(\phi(\theta_T)k + \rho)^2 + 1 - \rho^2}\right)
    $$

    At $k = 0$:

    $$
    w(0, \theta_T) = \frac{\theta_T}{2}\left(1 + \sqrt{\rho^2 + 1 - \rho^2}\right) = \frac{\theta_T}{2}(1 + 1) = \theta_T
    $$

    This confirms $w(0) = \theta_T$ (ATM total variance equals $\theta_T$, as expected).

    **Butterfly arbitrage condition at $k = 0$:** The density function $g(k) \ge 0$ requires (from the general formula for $g$):

    $$
    g(k) = \left(1 - \frac{kw'(k)}{2w(k)}\right)^2 - \frac{(w'(k))^2}{4}\left(\frac{1}{w(k)} + \frac{1}{4}\right) + \frac{w''(k)}{2} \ge 0
    $$

    At $k = 0$, the first term simplifies to $(1 - 0)^2 = 1$ since the $k w'(k)$ term vanishes. We need to compute $w'(0)$ and $w''(0)$.

    For SSVI, $\partial_k w = \frac{\theta_T}{2}\phi(\theta_T)\left(\rho + \frac{\phi(\theta_T)k + \rho}{\sqrt{(\phi(\theta_T)k + \rho)^2 + 1 - \rho^2}}\right)$.

    At $k = 0$:

    $$
    w'(0) = \frac{\theta_T}{2}\phi\left(\rho + \frac{\rho}{\sqrt{\rho^2 + 1 - \rho^2}}\right) = \frac{\theta_T}{2}\phi \cdot 2\rho = \theta_T\phi\rho
    $$

    where $\phi = \phi(\theta_T)$.

    For the condition $g(0) \ge 0$, a sufficient condition (simplifying the full expression and using bounds) leads to

    $$
    \frac{(w'(0))^2}{4}\left(\frac{1}{w(0)} + \frac{1}{4}\right) \le 1 + \frac{w''(0)}{2}
    $$

    The key constraint comes from bounding the wing slopes. The maximum slope of $w(k)/|k|$ as $|k| \to \infty$ is $\frac{\theta_T}{2}\phi(1 + |\rho|)$. Roger Lee's moment formula requires this to be at most 2 (for the variance swap bound). Combined with butterfly considerations, a sufficient condition is

    $$
    \eta(1 + |\rho|) \le 2
    $$

    where $\eta$ appears in $\phi(\theta) = \eta/(\theta^\gamma(1+\theta)^{1-\gamma})$. This ensures that $\theta_T \phi(\theta_T)(1 + |\rho|)/2$ does not exceed 2 for any $\theta_T$, keeping the wing slopes bounded.

    **As $\eta$ approaches the upper bound:** The wing slopes approach the maximum allowed value. The smile curvature (controlled by $w''$) increases, making the smile sharper. The implied density in the wings becomes thinner (closer to zero), and the denominator of Dupire's formula approaches zero in the wings, making local vol extraction increasingly sensitive. At the bound itself, the density just touches zero, which is the limiting case for butterfly arbitrage absence.

---

**Exercise 6.** A practitioner fits SVI independently to 5 maturities ($T = 0.1, 0.25, 0.5, 1.0, 2.0$) and obtains parameters $(a_i, b_i, \rho_i, m_i, \sigma_i)$ for each. To check calendar arbitrage, one must verify $w(k, T_{i+1}) \ge w(k, T_i)$ for all $k$. Show that this is not guaranteed by per-slice SVI fits even if each slice is individually arbitrage-free. Construct a concrete numerical example where two arbitrage-free SVI slices violate calendar monotonicity at some $k$.

??? success "Solution to Exercise 6"
    **Why per-slice fits do not guarantee calendar monotonicity:** Each SVI slice enforces $w(k, T_i) \ge 0$ and $\partial_{kk}w \ge 0$ at maturity $T_i$, but these are conditions on individual slices. The inter-slice condition $w(k, T_{i+1}) \ge w(k, T_i)$ for all $k$ involves the relationship between two separate parameter sets, which is not constrained.

    **Concrete numerical example:** Consider two maturities $T_1 = 0.25$ and $T_2 = 0.50$ with SVI parameters:

    - Slice 1 ($T_1 = 0.25$): $a_1 = 0.01$, $b_1 = 0.25$, $\rho_1 = -0.3$, $m_1 = 0$, $\sigma_1 = 0.1$
    - Slice 2 ($T_2 = 0.50$): $a_2 = 0.02$, $b_2 = 0.15$, $\rho_2 = -0.6$, $m_2 = 0$, $\sigma_2 = 0.1$

    Both slices are individually arbitrage-free (positive total variance, $b_i > 0$, $|\rho_i| < 1$).

    At $k = 0$ (ATM): $w_1(0) = 0.01 + 0.25 \times 0.1 = 0.035$ and $w_2(0) = 0.02 + 0.15 \times 0.1 = 0.035$. These are equal, which is borderline.

    Now check the right wing at $k = 1$:

    $$
    w_1(1) = 0.01 + 0.25(-0.3 \times 1 + \sqrt{1 + 0.01}) = 0.01 + 0.25(-0.3 + 1.005) = 0.01 + 0.25 \times 0.705 = 0.186
    $$

    $$
    w_2(1) = 0.02 + 0.15(-0.6 \times 1 + \sqrt{1 + 0.01}) = 0.02 + 0.15(-0.6 + 1.005) = 0.02 + 0.15 \times 0.405 = 0.081
    $$

    We have $w_2(1) = 0.081 < w_1(1) = 0.186$, so **calendar arbitrage is violated** at $k = 1$. The longer-dated option has less total variance than the shorter-dated one in the right wing, which is impossible under no-arbitrage.

    The violation arises because slice 2 has a smaller $b$ (flatter wings) and more negative $\rho$ (steeper left vs. right asymmetry) than slice 1. These parameter differences cause the right wing of slice 2 to fall below that of slice 1, despite slice 2 having higher ATM variance.

    This demonstrates that independent per-slice fitting requires a post-hoc calendar arbitrage check and adjustment, whereas SSVI avoids this issue by construction.

---

**Exercise 7.** Starting from the SVI analytic derivatives $\partial_k w$ and $\partial_{kk}w$, substitute into the Dupire formula in total variance coordinates to obtain an expression for $\sigma_{\text{loc}}^2(k, T)$ purely in terms of SVI parameters and $\partial_T w$. Assuming $\partial_T w$ is estimated via finite differences between adjacent maturities, discuss which term in the denominator is most sensitive to parameter uncertainty and why.

??? success "Solution to Exercise 7"
    The SVI analytic derivatives are

    $$
    \partial_k w = b\left(\rho + \frac{k - m}{\sqrt{(k-m)^2 + \sigma^2}}\right)
    $$

    $$
    \partial_{kk} w = \frac{b\sigma^2}{((k-m)^2 + \sigma^2)^{3/2}}
    $$

    Substituting into the Dupire formula:

    $$
    \sigma_{\text{loc}}^2(k, T) = \frac{\partial_T w}{1 - \frac{k}{w}\,b\!\left(\rho + \frac{k-m}{\sqrt{(k-m)^2+\sigma^2}}\right) + \frac{1}{4}\!\left(-\frac{1}{4} - \frac{1}{w} + \frac{k^2}{w^2}\right)\!b^2\!\left(\rho + \frac{k-m}{\sqrt{(k-m)^2+\sigma^2}}\right)^{\!2} + \frac{b\sigma^2}{2((k-m)^2+\sigma^2)^{3/2}}}
    $$

    where $w = a + b(\rho(k-m) + \sqrt{(k-m)^2 + \sigma^2})$ and $\partial_T w$ is estimated from adjacent maturities:

    $$
    \partial_T w \approx \frac{w(k, T_{i+1}) - w(k, T_i)}{T_{i+1} - T_i}
    $$

    **Which denominator term is most sensitive to parameter uncertainty:**

    The term $\frac{1}{4}\left(-\frac{1}{4} - \frac{1}{w} + \frac{k^2}{w^2}\right)(\partial_k w)^2$ is the most sensitive, for several reasons:

    1. **Quadratic dependence on $\partial_k w$:** This term involves $(\partial_k w)^2$, so errors in the SVI parameters (especially $b$ and $\rho$, which control the slope) are squared. A 10% error in $b$ produces a roughly 20% error in this term.

    2. **Dependence on $w$ in the denominator:** The factors $1/w$ and $k^2/w^2$ blow up when $w$ is small (near ATM at short maturities, where total variance is low). Small errors in $a$ (which directly shifts $w$) are amplified by this division.

    3. **Wing sensitivity:** In the wings ($|k|$ large), $\partial_k w \to b(1 \pm \rho)$ and $k^2/w^2 \to 1/(1 \pm \rho)^2$. The product $\frac{k^2}{w^2}(\partial_k w)^2 \to b^2$ is bounded, but the coefficient $-1/4 - 1/w$ can be large when $w$ is small. Furthermore, the cross-terms between $b$, $\rho$, and $k$ create a complex error landscape.

    4. **Interaction effects:** This term involves all five SVI parameters ($a$ through $w$, $b$ and $\rho$ through $\partial_k w$, $m$ through the centering), so it is the most "connected" to the full parameter vector.

    By contrast, the $\frac{1}{2}\partial_{kk}w$ term depends only on $b$, $\sigma$, and $m$, with a smooth, bounded dependence. The $-\frac{k}{w}\partial_k w$ term is linear in $\partial_k w$ and thus less sensitive to multiplicative parameter errors.

    In practice, the sensitivity of the $(\partial_k w)^2$ term means that accurate estimation of the SVI skew parameters $b$ and $\rho$ is critical for stable local vol extraction, particularly in the wings and at short maturities.
