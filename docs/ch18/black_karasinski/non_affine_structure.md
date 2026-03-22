# Non-Affine Structure and Consequences

The Vasicek, Hull-White, and CIR models all belong to the **affine** class of term structure models, where zero-coupon bond prices take the exponential-affine form $P(t,T) = A(\tau)e^{-B(\tau)r_t}$. This structure enables closed-form pricing of bonds, bond options, caps, and swaptions. The Black-Karasinski model breaks this pattern: the nonlinear dependence of the drift on $\ln r$ prevents the bond pricing PDE from admitting an exponential-affine solution. Understanding precisely why the affine structure fails --- and what consequences follow --- is essential for appreciating both the limitations and the compensating advantages of the BK model.

---

## Definition of affine term structure models

A short-rate model is called **affine** if the drift and squared diffusion coefficient are both affine (linear plus constant) functions of the state variable $r_t$:

$$
\mu(t, r) = \alpha_0(t) + \alpha_1(t)\,r
$$

$$
\sigma^2(t, r) = \beta_0(t) + \beta_1(t)\,r
$$

where $\alpha_0, \alpha_1, \beta_0, \beta_1$ are deterministic functions of time. Under this condition, the bond pricing PDE

$$
f_t + \mu(t,r)\,f_r + \frac{1}{2}\sigma^2(t,r)\,f_{rr} - r\,f = 0
$$

admits a solution of the form $f(t,r) = A(\tau)\,e^{-B(\tau)\,r}$, and the functions $A(\tau)$ and $B(\tau)$ satisfy ordinary differential equations.

### Examples of affine models

| Model | $\mu(t,r)$ | $\sigma^2(t,r)$ | Affine? |
|-------|------------|------------------|:-------:|
| Vasicek | $\kappa(\theta - r)$ | $\sigma^2$ | Yes |
| Hull-White | $\theta(t) - ar$ | $\sigma^2$ | Yes |
| CIR | $\kappa(\theta - r)$ | $\sigma^2 r$ | Yes |
| Black-Karasinski | $r[\theta(t) - a\ln r + \frac{1}{2}\sigma^2]$ | $\sigma^2 r^2$ | **No** |

---

## Why Black-Karasinski is not affine

The BK short rate dynamics (from Ito's lemma applied to $r_t = e^{x_t}$) are

$$
dr_t = r_t\!\left[\theta(t) - a\ln r_t + \frac{1}{2}\sigma^2\right]dt + \sigma\,r_t\,dW_t
$$

Comparing with the affine requirements:

**Drift**: $\mu(t, r) = r\!\left[\theta(t) - a\ln r + \frac{1}{2}\sigma^2\right]$. This contains the term $r\ln r$, which is not affine in $r$. No choice of $\alpha_0(t)$ and $\alpha_1(t)$ can represent $r\ln r$ as $\alpha_0 + \alpha_1 r$.

**Squared diffusion**: $\sigma^2(t,r) = \sigma^2 r^2$. This is quadratic in $r$, not affine. The affine condition requires $\sigma^2(t,r) = \beta_0(t) + \beta_1(t)\,r$, which cannot accommodate $r^2$.

Both conditions fail simultaneously. The BK model is therefore **doubly non-affine**: both the drift and the diffusion violate the affine requirements.

---

## The BK bond pricing PDE

Substituting the BK dynamics into the general bond pricing PDE:

$$
f_t + r\!\left[\theta(t) - a\ln r + \frac{1}{2}\sigma^2\right]f_r + \frac{1}{2}\sigma^2 r^2\,f_{rr} - r\,f = 0
$$

with terminal condition $f(T, r) = 1$.

### Attempting the affine ansatz

Suppose we try $f(t,r) = A(\tau)\,e^{-B(\tau)\,r}$. Then $f_r = -B\,f$ and $f_{rr} = B^2\,f$. Substituting:

$$
\left[-\frac{A'}{A} + B'\,r\right] + r\!\left[\theta(t) - a\ln r + \frac{1}{2}\sigma^2\right](-B) + \frac{1}{2}\sigma^2 r^2\,B^2 - r = 0
$$

This expression contains terms $r\ln r$ (from the drift) and $r^2$ (from the diffusion), neither of which can be absorbed into the coefficient-matching structure that separates powers of $r$. The ansatz fails --- there is no way to split the equation into independent functions of $\tau$ and $r$.

!!! warning "No exponential-affine solution exists"
    The failure of the affine ansatz is not a matter of insufficient cleverness. The $r\ln r$ and $r^2$ terms create a fundamental obstruction: the PDE cannot be reduced to a system of ODEs for any ansatz of the form $A(\tau)\,e^{-B(\tau)\,g(r)}$ with $g$ polynomial in $r$.

---

## Alternative PDE formulation in log-rate

Working in the log-rate variable $x = \ln r$ simplifies the PDE. Setting $g(t, x) = f(t, e^x)$:

$$
g_t + \left[\theta(t) - ax + \frac{1}{2}\sigma^2\right]g_x - \frac{1}{2}\sigma^2\,g_x + \frac{1}{2}\sigma^2\,g_{xx} - e^x\,g = 0
$$

which simplifies to

$$
g_t + \left[\theta(t) - ax\right]g_x + \frac{1}{2}\sigma^2\,g_{xx} - e^x\,g = 0
$$

The obstruction is now concentrated in the single term $e^x g$: the discounting rate $r = e^x$ is a nonlinear function of the state variable $x$. In an affine model (Vasicek or Hull-White), the discounting term would be $x\,g$ (linear in $x$), which is compatible with the exponential-affine ansatz. The exponential $e^x$ prevents separation.

---

## Consequences for derivative pricing

The non-affine structure has cascading consequences.

### No closed-form bond prices

The bond pricing PDE must be solved numerically (by finite differences, trees, or Monte Carlo). There is no formula analogous to $P(t,T) = A(\tau)e^{-B(\tau)r_t}$.

### No closed-form bond options

Since bond prices are not available in closed form, bond option formulas (which require the distribution of bond prices) are also unavailable. The CIR chi-squared formula and the Vasicek/Hull-White Gaussian formula have no BK analogue.

### No closed-form caps or swaptions

Caps and swaptions, which decompose into bond options, inherit the numerical requirement.

### Jamshidian decomposition still applies

Jamshidian's trick requires only that bond prices are monotone in the short rate, which holds for BK. The decomposition of a swaption into bond options remains valid, but each bond option must be priced numerically.

### Calibration is iterative

The time-dependent drift $\theta(t)$ cannot be extracted by a single analytical formula (as in Hull-White). Instead, $\theta(t)$ is calibrated iteratively, typically by forward induction on a trinomial tree.

---

## What the BK model gains

Despite losing analytical tractability, the BK model offers:

1. **Strict positivity**: Rates are always positive, which is essential for certain products and markets
2. **Exact term structure fit**: The time-dependent $\theta(t)$ matches the initial yield curve exactly
3. **Log-normal rate distribution**: The heavy right tail better captures the empirical distribution of rates in high-rate environments
4. **Flexible volatility structure**: The multiplicative noise $\sigma r$ produces rate-level-dependent volatility, matching the empirical observation that rate volatility increases with the level

!!! tip "The affine-tractability tradeoff"
    The choice between affine models (Vasicek, Hull-White, CIR) and non-affine models (Black-Karasinski) reflects a fundamental tradeoff: analytical formulas enable fast pricing and transparent calibration, while non-affine models offer richer distributional properties and positivity constraints. The "right" choice depends on the application: for vanilla products where speed matters, affine models dominate; for portfolios sensitive to the rate distribution (e.g., mortgage-backed securities), BK may be preferred.

---

## Summary

The Black-Karasinski model is non-affine because both its drift (containing $r\ln r$) and its squared diffusion (proportional to $r^2$) violate the affine conditions required for exponential-affine bond prices. The failure is visible in the bond pricing PDE, where the discounting term $e^x g$ (with $x = \ln r$) prevents the separation of variables that underlies all affine model solutions. As a consequence, no closed-form formulas exist for bonds, bond options, caps, or swaptions; all must be computed numerically. The BK model compensates for this loss with guaranteed positive rates, exact term structure calibration, and a log-normal rate distribution that better matches empirical behavior in certain market environments.
