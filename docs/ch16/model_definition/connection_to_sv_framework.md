# Connection to the General Stochastic Volatility Framework

Many stochastic volatility models exist in the quantitative finance literature, each making different assumptions about how instantaneous variance evolves. Before studying the Heston model in depth, it is valuable to place it within the broader SV family. Understanding what is generic (shared by all SV models) and what is specific (unique to Heston) clarifies why certain analytical results are available for Heston but not for alternatives, and guides the practitioner in choosing the right model for a given application.

This section defines the general one-factor stochastic volatility framework, identifies the Heston model as a special case, compares it with other prominent SV models, and highlights the properties that make the Heston specification analytically tractable. We assume familiarity with the Heston SDE and parameters from the [preceding section](heston_sde_and_parameters.md).

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - Write the general one-factor stochastic volatility SDE system
    - Identify the specific coefficient functions that define the Heston model within the general framework
    - Compare the Heston model with SABR, Hull-White, the 3/2 model, and Stein-Stein
    - Explain why the square-root diffusion in Heston leads to affine structure
    - State existence and uniqueness conditions for the Heston variance process

---

## The General One-Factor SV Framework

Recall (see [§ Two-Factor Diffusion Models](../../ch14/general_stochastic_volatility_framework/two_factor_diffusion_models.md)): a generic stochastic volatility model writes

$$
dS_t = (r - q)\,S_t\,dt + \sigma(v_t)\,S_t\,dW_t^{(1)}, \qquad dv_t = \mu_v(v_t)\,dt + \sigma_v(v_t)\,dW_t^{(2)}, \qquad d\langle W^{(1)}, W^{(2)}\rangle_t = \rho\,dt.
$$

The three coefficient functions $\sigma(\cdot)$, $\mu_v(\cdot)$, $\sigma_v(\cdot)$ determine the model completely. Each named SV model corresponds to a particular choice of these functions.

---

## Heston as a Special Case

### Coefficient Identification

The Heston model arises from the general framework with the following specific choices:

!!! info "Definition: Heston Coefficient Functions"
    The Heston (1993) model corresponds to the general SV framework with:

    | Component | General Form | Heston Specification |
    |:---|:---:|:---:|
    | State variable | $v_t$ | $v_t$ = instantaneous variance |
    | Volatility function | $\sigma(v_t)$ | $\sqrt{v_t}$ |
    | Variance drift | $\mu_v(v_t)$ | $\kappa(\theta - v_t)$ |
    | Variance diffusion | $\sigma_v(v_t)$ | $\sigma_v \sqrt{v_t}$ |

    Substituting into the general framework yields:

    $$
    dS_t = (r - q)\,S_t\,dt + \sqrt{v_t}\,S_t\,dW_t^{(1)}
    $$

    $$
    dv_t = \kappa\,(\theta - v_t)\,dt + \sigma_v\,\sqrt{v_t}\,dW_t^{(2)}
    $$

Three properties distinguish the Heston specification from other SV models:

1. **The state variable is variance itself**, not volatility. This means $\sigma(v_t) = \sqrt{v_t}$, a square-root function.
2. **The drift is linear (affine) in $v_t$**: $\mu_v(v_t) = \kappa\theta - \kappa v_t$, which is of the form $a + b\,v_t$.
3. **The diffusion is proportional to $\sqrt{v_t}$**: $\sigma_v(v_t) = \sigma_v\sqrt{v_t}$, so $\sigma_v^2(v_t) = \sigma_v^2\,v_t$, which is also affine in $v_t$.

These three properties make the Heston model an **affine diffusion**, which is the key to its analytical tractability. We develop this in detail in the [Affine Structure and Riccati System](affine_structure_and_riccati.md) section.

---

## Comparison with Other SV Models

The following table catalogs the most important one-factor SV models by their coefficient functions.

### Model Catalog

| Model | State Variable | $\sigma(v_t)$ | $\mu_v(v_t)$ | $\sigma_v(v_t)$ | Affine? |
|:---|:---:|:---:|:---:|:---:|:---:|
| **Heston (1993)** | Variance $v_t$ | $\sqrt{v_t}$ | $\kappa(\theta - v_t)$ | $\sigma_v\sqrt{v_t}$ | Yes |
| **Hull-White (1987)** | Variance $v_t$ | $\sqrt{v_t}$ | $\mu\,v_t$ | $\sigma_v\,v_t$ | No |
| **Stein-Stein (1991)** | Volatility $\sigma_t$ | $\sigma_t$ | $\kappa(\theta - \sigma_t)$ | $\sigma_v$ | No |
| **SABR (2002)** | Volatility $\sigma_t$ | $\sigma_t S_t^{\beta-1}$ | $0$ | $\alpha\,\sigma_t$ | No |
| **3/2 Model** | Variance $v_t$ | $\sqrt{v_t}$ | $\kappa\,v_t(\theta - v_t)$ | $\sigma_v\,v_t^{3/2}$ | No |
| **Scott (1987)** | Log-volatility $y_t$ | $e^{y_t}$ | $\kappa(\theta - y_t)$ | $\sigma_v$ | No |

!!! tip "What Makes Heston Special"
    Among all the models in the table, only the Heston model has the affine property: both the drift and squared diffusion of the variance process are affine (linear plus constant) functions of $v_t$. This is precisely the condition needed for the characteristic function to have an exponential-affine form, which in turn enables semi-analytical Fourier pricing.

### Detailed Comparison

**Heston vs. Hull-White.** The Hull-White (1987) model uses $dv_t = \mu\,v_t\,dt + \sigma_v\,v_t\,dW_t^{(2)}$, making $v_t$ a geometric Brownian motion. This means variance is log-normal rather than chi-squared, and the model is not affine. No closed-form characteristic function exists. The Hull-White model requires Monte Carlo simulation or series expansion approximations for pricing.

**Heston vs. SABR.** The SABR model (Hagan et al., 2002) uses $dF_t = \sigma_t F_t^\beta\,dW_t^{(1)}$ and $d\sigma_t = \alpha\,\sigma_t\,dW_t^{(2)}$, where $F_t$ is the forward price and $\beta \in [0,1]$ controls the backbone. The volatility follows a driftless geometric Brownian motion. SABR has an approximate closed-form implied volatility formula (the Hagan formula) but lacks an exact characteristic function. It is widely used for interpolating the smile at a single maturity but is less suited for consistent pricing across maturities.

**Heston vs. the 3/2 Model.** The 3/2 model uses $dv_t = \kappa\,v_t(\theta - v_t)\,dt + \sigma_v\,v_t^{3/2}\,dW_t^{(2)}$. The drift and diffusion are both nonlinear in $v_t$. While the model is not affine in $v_t$, it is affine in $1/v_t$ (a reciprocal transformation), which gives a different form of tractability. The 3/2 model generates more realistic variance dynamics for extreme events but is harder to calibrate.

**Heston vs. Stein-Stein.** The Stein-Stein (1991) model uses $d\sigma_t = \kappa(\theta - \sigma_t)\,dt + \sigma_v\,dW_t^{(2)}$, an Ornstein-Uhlenbeck process for volatility. The constant diffusion means volatility can become negative, which is unphysical. Schobel and Zhu (1999) showed that if one works with $v_t = \sigma_t^2$ (variance), the characteristic function can be obtained in closed form, but the derivation is more complex than for Heston.

---

## Affine Structure: The Key Distinction

Recall (see [§ Affine Structure and Riccati System](affine_structure_and_riccati.md) and [§ Heston as Affine](../../ch15/examples/heston_as_affine.md)): because the drift and squared diffusion of $v_t$ are affine in $v_t$, the conditional characteristic function admits the exponential-affine form $\phi(u, \tau) = \exp(C(\tau, u) + D(\tau, u)v_t + iu\,x_t)$, with $C$ and $D$ solving Riccati ODEs. The 2D PDE reduces to a pair of ODEs solvable in closed form.

For non-affine models (Hull-White, SABR, 3/2), no such reduction exists in general; the characteristic function either has no closed form or requires special transformations.

!!! note "Affine Models Beyond Heston"
    The Heston model is the most important member of the affine class, but it is not the only one. The Bates (1996) model adds jumps to the Heston price dynamics while preserving affine structure. Multi-factor models (double Heston) stack two independent CIR variance processes. These extensions, discussed in later sections, all share the Riccati ODE structure.

---

## Existence and Uniqueness

Recall (see [§ Feller Condition and Boundary Behavior](feller_condition_and_boundary.md) and [§ CIR Variance Process Solution](../variance_dynamics/cir_variance_process_solution.md)): under $\kappa, \theta, \sigma_v > 0$ and $v_0 > 0$, the CIR variance equation admits a unique strong non-negative solution (via Yamada-Watanabe), strict positivity follows under the Feller condition $2\kappa\theta \geq \sigma_v^2$, and the asset price equation has a unique strong positive solution given any continuous non-negative variance path.

---

## Worked Example: Model Comparison on the Same Data

Consider the following scenario: the current implied volatility smile for 1-year S&P 500 options exhibits a negative skew. We compare the qualitative behavior of several SV models under typical parameters.

??? example "Qualitative Behavior Comparison"
    Fix common parameters where applicable: current volatility $\approx 20\%$, mean-reversion target $\approx 20\%$ vol, correlation $\rho = -0.7$.

    | Feature | Heston | Hull-White | SABR ($\beta = 0.5$) | 3/2 Model |
    |:---|:---:|:---:|:---:|:---:|
    | Short-term smile | Moderate curvature | Similar | Strong curvature (backbone) | Strong curvature |
    | Long-term smile | Flattens (mean-reversion) | Grows (no mean-reversion) | N/A (single maturity) | Flattens |
    | Variance positivity | Guaranteed if Feller holds | Always positive (log-normal) | N/A | Always positive |
    | Closed-form CF | Yes | No | No | Via reciprocal |
    | Calibration speed | Fast (CF + FFT) | Slow (MC required) | Fast (Hagan formula) | Moderate |
    | Term structure fit | Good | Poor | Not designed for it | Good |

    The Heston model offers the best combination of analytical tractability and term structure fitting, which explains its dominance in practice for multi-maturity calibration.

---

## Summary

The Heston model is a special case of the general one-factor stochastic volatility framework, distinguished by its CIR-type variance process with affine drift and affine squared diffusion. This affine structure is the source of the model's analytical tractability: it reduces the characteristic function computation to a pair of Riccati ODEs with closed-form solutions. Among the major SV models -- Hull-White, SABR, 3/2, Stein-Stein -- only Heston (and its extensions) possesses this property, making it the standard choice for Fourier-based pricing and multi-maturity calibration.

The [next section](affine_structure_and_riccati.md) develops the affine structure in full detail, deriving the Riccati system that underlies all Heston pricing.

---

## Exercises

**Exercise 1.** Write the general one-factor SV model $dS_t = rS_t\,dt + \sigma(V_t)S_t\,dW_t^S$ and $dV_t = \mu(V_t)\,dt + \eta(V_t)\,dW_t^V$ with $\operatorname{Corr}(dW^S, dW^V) = \rho\,dt$. Show that the Heston model is the special case $\sigma(V) = \sqrt{V}$, $\mu(V) = \kappa(\theta - V)$, and $\eta(V) = \sigma_v\sqrt{V}$.

??? success "Solution to Exercise 1"
    The general one-factor SV model under the risk-neutral measure is:

    $$
    dS_t = rS_t\,dt + \sigma(V_t)\,S_t\,dW_t^S
    $$

    $$
    dV_t = \mu(V_t)\,dt + \eta(V_t)\,dW_t^V
    $$

    $$
    d\langle W^S, W^V \rangle_t = \rho\,dt
    $$

    where $\sigma(\cdot)$, $\mu(\cdot)$, and $\eta(\cdot)$ are the three coefficient functions that specify the model. The Heston model corresponds to the choices:

    - **Volatility function:** $\sigma(V) = \sqrt{V}$. The state variable $V_t$ represents instantaneous variance directly, so the instantaneous volatility of the asset price is $\sqrt{V_t}$.

    - **Variance drift:** $\mu(V) = \kappa(\theta - V)$. This is a linear (affine) function of $V$, producing mean-reverting dynamics with speed $\kappa$ and target $\theta$.

    - **Variance diffusion:** $\eta(V) = \sigma_v\sqrt{V}$. The diffusion coefficient is proportional to $\sqrt{V}$, making the variance process a CIR (Cox-Ingersoll-Ross) diffusion.

    Substituting these into the general framework:

    $$
    dS_t = rS_t\,dt + \sqrt{V_t}\,S_t\,dW_t^S
    $$

    $$
    dV_t = \kappa(\theta - V_t)\,dt + \sigma_v\sqrt{V_t}\,dW_t^V
    $$

    which is precisely the Heston SDE system. The key structural property is that both $\mu(V) = \kappa\theta - \kappa V$ and $\eta^2(V) = \sigma_v^2 V$ are affine functions of $V$, which is the source of the model's analytical tractability.

---

**Exercise 2.** For the Hull-White SV model where the variance follows a GBM $dV_t = \mu V_t\,dt + \sigma_v V_t\,dW_t^V$, explain why the diffusion coefficient $\sigma_v V_t$ is not affine in $V_t$ (it is linear, but the squared diffusion $\sigma_v^2 V_t^2$ is quadratic). Why does this prevent a closed-form characteristic function?

??? success "Solution to Exercise 2"
    In the Hull-White (1987) SV model, the variance follows a geometric Brownian motion:

    $$
    dV_t = \mu V_t\,dt + \sigma_v V_t\,dW_t^V
    $$

    The diffusion coefficient is $\eta(V) = \sigma_v V$, which is linear in $V$. However, the **squared diffusion** (the instantaneous variance of $V_t$) is:

    $$
    \eta^2(V) = \sigma_v^2 V^2
    $$

    This is **quadratic** in $V$, not affine. For a process to be affine, we need both the drift and the elements of the diffusion matrix $\Sigma\Sigma^\top$ to be affine (linear plus constant) in the state variables. The drift $\mu V$ is linear (hence affine), but $\sigma_v^2 V^2$ is quadratic.

    This prevents the exponential-affine ansatz from working. If one substitutes $\phi = \exp(C + DV + iux)$ into the Feynman-Kac PDE for the Hull-White model, the $\frac{1}{2}\sigma_v^2 V^2 D^2$ term generates a $V^2$ dependence that cannot be absorbed into the $V^0$ and $V^1$ coefficients. The separation of the PDE into ODEs for $C$ and $D$ fails because a $V^2$ term appears with no corresponding degree of freedom in the ansatz.

    Without a closed-form characteristic function, pricing European options requires either Monte Carlo simulation (slow for calibration) or numerical PDE methods (computationally expensive in two spatial dimensions). This is the fundamental computational disadvantage of non-affine SV models.

---

**Exercise 3.** The SABR model has dynamics $dF_t = \sigma_t F_t^\beta\,dW_t^F$. For $\beta = 1$ (log-normal SABR), the forward price is a GBM with stochastic volatility. Compare this to the Heston model and explain why SABR lacks a closed-form characteristic function for general $\beta$.

??? success "Solution to Exercise 3"
    In the log-normal SABR model ($\beta = 1$), the dynamics are:

    $$
    dF_t = \sigma_t F_t\,dW_t^F, \qquad d\sigma_t = \alpha\,\sigma_t\,dW_t^\sigma
    $$

    The volatility $\sigma_t$ follows a driftless geometric Brownian motion. Comparing with Heston:

    - **Heston** models *variance* $V_t$ with a mean-reverting CIR process: the drift is $\kappa(\theta - V_t)$ and the diffusion is $\sigma_v\sqrt{V_t}$.
    - **SABR** models *volatility* $\sigma_t$ with a GBM: the drift is zero and the diffusion is $\alpha\sigma_t$.

    For general $\beta$, the asset dynamics $dF_t = \sigma_t F_t^\beta\,dW_t^F$ introduce a nonlinear dependence on $F_t$ through $F_t^\beta$. The instantaneous variance of the log-price involves $\sigma_t^2 F_t^{2(\beta-1)}$, which depends on both state variables in a non-affine way. This means the joint process $(F_t, \sigma_t)$ is not affine.

    Even rewriting in terms of $\ln F_t$ and $\sigma_t$ (or $\sigma_t^2$), the coefficients of the resulting PDE are not affine in the state variables for $\beta \neq 0$ or $\beta \neq 1$. Therefore, the exponential-affine ansatz for the characteristic function fails, and no closed-form CF exists for general $\beta$. The celebrated Hagan formula for SABR implied volatility is an asymptotic approximation (valid for short maturities), not an exact result derived from a characteristic function.

---

**Exercise 4.** The 3/2 model uses $dV_t = \kappa V_t(\theta - V_t)\,dt + \sigma_v V_t^{3/2}\,dW_t^V$. Show that the substitution $Y_t = 1/V_t$ transforms this into a CIR process for $Y_t$. What does this tell you about the tractability of the 3/2 model?

??? success "Solution to Exercise 4"
    Starting from the 3/2 model:

    $$
    dV_t = \kappa V_t(\theta - V_t)\,dt + \sigma_v V_t^{3/2}\,dW_t^V
    $$

    Apply Ito's lemma to $Y_t = 1/V_t$. With $f(V) = 1/V$, we have $f'(V) = -1/V^2$ and $f''(V) = 2/V^3$:

    $$
    dY_t = f'(V_t)\,dV_t + \tfrac{1}{2}f''(V_t)\,(dV_t)^2
    $$

    $$
    = -\frac{1}{V_t^2}\bigl[\kappa V_t(\theta - V_t)\,dt + \sigma_v V_t^{3/2}\,dW_t\bigr] + \tfrac{1}{2}\cdot\frac{2}{V_t^3}\cdot\sigma_v^2 V_t^3\,dt
    $$

    $$
    = \left[-\frac{\kappa(\theta - V_t)}{V_t} + \sigma_v^2\right]dt - \frac{\sigma_v}{\sqrt{V_t}}\,dW_t
    $$

    Substituting $V_t = 1/Y_t$:

    $$
    dY_t = \left[-\kappa\theta Y_t + \kappa + \sigma_v^2\right]dt - \sigma_v\sqrt{Y_t}\,dW_t
    $$

    $$
    = \bigl[(\kappa + \sigma_v^2) - \kappa\theta\,Y_t\bigr]\,dt - \sigma_v\sqrt{Y_t}\,dW_t
    $$

    This is a CIR process for $Y_t = 1/V_t$ with parameters:

    - Mean-reversion speed: $\kappa\theta$
    - Long-run mean: $(\kappa + \sigma_v^2)/(\kappa\theta)$
    - Vol-of-vol: $\sigma_v$

    The negative sign on the diffusion term is immaterial (it can be absorbed by redefining the Brownian motion). Since $Y_t$ follows a CIR process, it is an affine diffusion in the variable $Y_t = 1/V_t$. This means the characteristic function of $Y_T$ (and hence functionals of $V_T$) can be computed using the same Riccati ODE machinery as the Heston model, albeit with different coefficients and applied to the reciprocal variable. The 3/2 model is therefore tractable -- but through the reciprocal transformation rather than directly.

---

**Exercise 5.** List the key properties that make the Heston model the standard choice for Fourier-based pricing: (i) affine structure, (ii) closed-form CF, (iii) mean-reverting variance, (iv) non-negative variance. Which of these properties does the Stein-Stein model (Gaussian variance) fail to satisfy?

??? success "Solution to Exercise 5"
    The key properties that make Heston the standard for Fourier-based pricing are:

    **(i) Affine structure.** Both the drift $\mu(V) = \kappa(\theta - V)$ and the squared diffusion $\eta^2(V) = \sigma_v^2 V$ are affine in $V$. This allows the exponential-affine ansatz for the characteristic function, reducing a 2D PDE to Riccati ODEs.

    **(ii) Closed-form characteristic function.** The Riccati ODEs for the Heston model can be solved in closed form, giving an explicit expression for $\phi(u, \tau)$. This enables evaluation of the CF at any frequency $u$ without numerical ODE integration.

    **(iii) Mean-reverting variance.** The CIR drift $\kappa(\theta - V_t)$ pulls variance toward $\theta$, producing a stationary distribution and ensuring that the implied volatility term structure is well-behaved at long maturities.

    **(iv) Non-negative variance.** The CIR process guarantees $V_t \geq 0$ for all $t$ (and $V_t > 0$ if the Feller condition holds). Variance is physically non-negative, so the model is economically consistent.

    The **Stein-Stein model** uses an OU process for volatility: $d\sigma_t = \kappa(\theta - \sigma_t)\,dt + \sigma_v\,dW_t$. The constant diffusion $\sigma_v$ means volatility is Gaussian and can become **negative**, violating property (iv). Since variance is $V_t = \sigma_t^2$, negative volatility is unphysical. The Stein-Stein model satisfies (iii) but fails (iv). Properties (i) and (ii) are partially recovered by working with $V_t = \sigma_t^2$ (Schobel-Zhu, 1999), but the derivation is more complex, the resulting CF involves three Riccati equations instead of two, and the model still allows unphysical negative volatility paths.

---

**Exercise 6.** For calibration to a panel of option prices across strikes and maturities, explain why having a closed-form characteristic function (as in Heston) is a decisive computational advantage over models requiring numerical PDE solutions for each parameter evaluation (as in SABR with general $\beta$).

??? success "Solution to Exercise 6"
    In calibration, the model parameters $(\kappa, \theta, \sigma_v, \rho, V_0)$ are adjusted to minimize the distance between model-implied and market-observed option prices (or implied volatilities) across a panel of strikes $K_1, \ldots, K_N$ and maturities $T_1, \ldots, T_M$.

    **With a closed-form CF (Heston):**

    - For each parameter vector proposed by the optimizer, the CF $\phi(u, \tau)$ is evaluated directly from the explicit formula.
    - Option prices for all $N \times M$ instruments are computed via FFT (Fast Fourier Transform) or the COS method in $O(N \log N)$ operations per maturity, with each CF evaluation costing $O(1)$.
    - A single calibration iteration evaluates perhaps $10^2$--$10^3$ options in milliseconds.
    - The optimizer typically requires $10^2$--$10^3$ iterations, giving total calibration time of seconds to minutes.

    **Without a closed-form CF (e.g., SABR with general $\beta$):**

    - For each parameter vector, one must solve a 2D PDE or run Monte Carlo to obtain each option price.
    - A 2D PDE solve with adequate resolution ($100 \times 100$ grid) requires $O(10^4)$ operations per time step and $O(10^2)$ time steps, so $O(10^6)$ per option price.
    - Monte Carlo with $10^5$ paths and $10^2$ time steps requires $O(10^7)$ operations per option price.
    - Evaluating $10^2$--$10^3$ options per calibration iteration becomes extremely expensive.

    The ratio of computational cost is roughly $10^3$--$10^6$ times more expensive per calibration iteration without a CF. Since calibration must be performed frequently (daily or intraday for trading desks), the closed-form CF is not just convenient but practically essential for production use. This is the decisive advantage of the Heston model's affine structure.
