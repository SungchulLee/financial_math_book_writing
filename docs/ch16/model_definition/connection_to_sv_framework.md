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

### Intuition

In any stochastic volatility model, the key idea is the same: the instantaneous variance is not a fixed parameter but a random process with its own dynamics. Different models differ only in how they specify the drift and diffusion of the variance (or volatility) process. Thinking of the variance dynamics as a "plug-in module" within a common framework makes it straightforward to compare models and understand what drives their distinct behaviors.

### Definition

!!! info "Definition: General One-Factor Stochastic Volatility Model"
    Under the risk-neutral measure $\mathbb{Q}$, a one-factor stochastic volatility model specifies:

    $$
    dS_t = (r - q)\,S_t\,dt + \sigma(v_t)\,S_t\,dW_t^{(1)}
    $$

    $$
    dv_t = \mu_v(v_t)\,dt + \sigma_v(v_t)\,dW_t^{(2)}
    $$

    $$
    d\langle W^{(1)}, W^{(2)} \rangle_t = \rho\,dt
    $$

    where:

    - $v_t$ is the state variable driving volatility
    - $\sigma(v_t)$ is the **volatility function** mapping the state variable to the instantaneous volatility of $S_t$
    - $\mu_v(v_t)$ is the **drift function** of the variance/volatility process
    - $\sigma_v(v_t)$ is the **diffusion function** of the variance/volatility process

The three coefficient functions $\sigma(\cdot)$, $\mu_v(\cdot)$, and $\sigma_v(\cdot)$ determine the model completely. Each named SV model corresponds to a particular choice of these three functions.

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

The property that sets the Heston model apart is its **affine structure**. To see why this matters, consider the characteristic function of the log-price:

$$
\phi(u, \tau) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{iu\,x_T} \,\middle|\, x_t, v_t\right]
$$

For the Heston model, the Feynman-Kac theorem links $\phi$ to a PDE. Because the drift and squared diffusion of $v_t$ are both affine in $v_t$, one can guess (and verify) that $\phi$ has the exponential-affine form:

$$
\phi(u, \tau) = \exp\!\bigl(C(\tau, u) + D(\tau, u)\,v_t + iu\,x_t\bigr)
$$

where $C$ and $D$ satisfy Riccati ordinary differential equations. This reduces the pricing problem from solving a PDE in $(x, v, t)$ to solving two ODEs, which can be done in closed form.

For non-affine models (Hull-White, SABR, 3/2), no such reduction exists in general. The characteristic function either has no closed form or requires special transformations.

!!! note "Affine Models Beyond Heston"
    The Heston model is the most important member of the affine class, but it is not the only one. The Bates (1996) model adds jumps to the Heston price dynamics while preserving affine structure. Multi-factor models (double Heston) stack two independent CIR variance processes. These extensions, discussed in later sections, all share the Riccati ODE structure.

---

## Existence and Uniqueness

The Heston SDE system has well-defined solutions under the standard parameter constraints.

!!! success "Theorem: Existence and Pathwise Uniqueness"
    Suppose $\kappa > 0$, $\theta > 0$, $\sigma_v > 0$, $\rho \in [-1, 1]$, and $v_0 > 0$. Then:

    1. The CIR variance equation $dv_t = \kappa(\theta - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t^{(2)}$ has a unique strong solution $v_t \geq 0$ for all $t \geq 0$
    2. If the Feller condition $2\kappa\theta \geq \sigma_v^2$ holds, then $v_t > 0$ a.s. for all $t > 0$
    3. Given any continuous, non-negative variance path $v_t$, the asset price equation has a unique strong solution $S_t > 0$ for all $t \geq 0$

The variance process existence and uniqueness rely on the Yamada-Watanabe theorem, which applies to SDEs with Holder-$\frac{1}{2}$ continuous diffusion coefficients (the $\sqrt{v}$ function). The standard Lipschitz condition for uniqueness fails at $v = 0$, but the Yamada-Watanabe condition $\int_0^\epsilon \sigma_v^{-2}(x)\,dx = \int_0^\epsilon (\sigma_v^2 x)^{-1}\,dx = +\infty$ suffices for pathwise uniqueness.

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
