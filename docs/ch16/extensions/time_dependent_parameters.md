# Time-Dependent Parameters

In the standard Heston model, the parameters $\kappa$, $\theta$, $\xi$, and $\rho$ are constants. This produces a single implied volatility surface shape that cannot simultaneously match market smiles at both short and long maturities. In practice, the short-maturity smile is steep and driven by jump-like behavior, while the long-maturity smile flattens as mean reversion dominates. Allowing parameters to vary with time --- typically as piecewise-constant functions --- gives the model enough flexibility to fit the entire term structure of implied volatilities while preserving the affine structure that enables semi-analytic pricing.

!!! info "Prerequisites"
    - [Heston SDE and Parameters](../model_definition/heston_sde_and_parameters.md) (constant-parameter Heston)
    - [Closed-Form Characteristic Function](../heston_cf/closed_form_characteristic_function.md) (Riccati ODE system)
    - [Affine Structure and Riccati](../model_definition/affine_structure_and_riccati.md) (affine framework)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Write down the Heston SDE with time-dependent parameters
    2. Formulate the piecewise-constant parameter specification used in calibration
    3. Derive the characteristic function via sequential Riccati integration over time intervals
    4. Explain why the affine structure is preserved under piecewise-constant parameters
    5. Describe how the extended parameter set improves term-structure calibration

---

## Motivation

### Limitations of Constant Parameters

With constant parameters, the Heston model generates implied volatility surfaces where the skew scales approximately as

$$
\text{skew} \approx \frac{\rho\,\xi}{\sqrt{\theta}} \cdot f(\kappa, T)
$$

for some function $f$ that depends on mean reversion and maturity. A single set $(\kappa, \theta, \xi, \rho)$ cannot reproduce a steep short-maturity skew and a flat long-maturity skew simultaneously. Similarly, the at-the-money term structure of implied volatility is controlled by $\theta$ and the initial variance $v_0$, and a single $\theta$ may not match market levels across all tenors.

### The Piecewise-Constant Solution

Practitioners address this by defining a maturity grid $0 = T_0 < T_1 < \cdots < T_N$ (matching the expiry dates of liquid options) and assigning independent parameter values on each interval $[T_{i-1}, T_i)$. The model retains its affine structure on each interval, and the characteristic function is computed by chaining Riccati solutions across intervals.

---

## Model Specification

### SDE with Time-Dependent Coefficients

Under $\mathbb{Q}$, the time-dependent Heston model specifies:

$$
\frac{dS_t}{S_t} = (r - q)\,dt + \sqrt{v_t}\,dW_t^{(1)}
$$

$$
dv_t = \kappa(t)\bigl[\theta(t) - v_t\bigr]\,dt + \xi(t)\sqrt{v_t}\,dW_t^{(2)}
$$

with $d\langle W^{(1)}, W^{(2)}\rangle_t = \rho(t)\,dt$, where $\kappa(t)$, $\theta(t)$, $\xi(t)$, and $\rho(t)$ are deterministic functions of time.

### Piecewise-Constant Parameterization

Given a maturity grid $0 = T_0 < T_1 < \cdots < T_N$, define:

$$
\kappa(t) = \kappa_i, \quad \theta(t) = \theta_i, \quad \xi(t) = \xi_i, \quad \rho(t) = \rho_i \quad \text{for } t \in [T_{i-1}, T_i)
$$

This gives $4N$ free parameters (plus the initial variance $v_0$). In practice, not all parameters need vary: a common choice is to fix $\kappa$ and $\rho$ globally and let only $\theta_i$ and $\xi_i$ vary by interval, reducing the count to $2N + 2$.

| Configuration | Free parameters | Use case |
|---------------|----------------|----------|
| All vary | $4N + 1$ | Maximum flexibility, risk of overfitting |
| $\theta_i$, $\xi_i$ vary; $\kappa$, $\rho$ fixed | $2N + 3$ | Standard practice |
| $\xi_i$ varies; rest fixed | $N + 4$ | Minimal extension for vol-of-vol term structure |

---

## Characteristic Function via Sequential Riccati Integration

### Affine Structure on Each Interval

On each interval $[T_{i-1}, T_i)$, the parameters are constant, so the log-characteristic function retains the standard affine form:

$$
\ln\mathbb{E}\!\left[e^{iu\ln S_T}\,\Big|\,\mathcal{F}_t\right] = iu\ln S_t + C(t, T; u) + D(t, T; u)\,v_t
$$

where $C$ and $D$ satisfy the Riccati system with parameters $(\kappa_i, \theta_i, \xi_i, \rho_i)$.

### Sequential Integration

For a maturity $T \in (T_{n-1}, T_n]$, the functions $C$ and $D$ are computed by integrating backward from $T$:

**Step 1.** On the interval $[T_{n-1}, T]$, solve the Riccati ODE with parameters $(\kappa_n, \theta_n, \xi_n, \rho_n)$ and terminal condition $D(T, T) = 0$, $C(T, T) = 0$. Obtain $D(T_{n-1}, T)$ and $C(T_{n-1}, T)$.

**Step 2.** On the interval $[T_{n-2}, T_{n-1}]$, solve the Riccati ODE with parameters $(\kappa_{n-1}, \theta_{n-1}, \xi_{n-1}, \rho_{n-1})$. The terminal condition is now $D(T_{n-1}) = D(T_{n-1}, T)$ from Step 1. The function $C$ accumulates additively:

$$
C(T_{n-2}, T) = C(T_{n-1}, T) + \int_{T_{n-2}}^{T_{n-1}} \kappa_{n-1}\,\theta_{n-1}\,D(s, T)\,ds
$$

**Step $k$.** Repeat backward through each interval until reaching $t = 0$.

!!! tip "Why This Works"
    The affine structure means $C$ depends on $v_t$ only through the integral of $D$, and $D$ satisfies the same Riccati ODE on each interval (with different coefficients). At each boundary $T_i$, continuity of $C$ and $D$ is enforced by using the output of interval $i+1$ as the input for interval $i$.

### Closed-Form Solution on Each Interval

On interval $[T_{i-1}, T_i]$ of length $\tau_i = T_i - T_{i-1}$, the Riccati ODE for $D$ with constant coefficients $(\kappa_i, \xi_i, \rho_i)$ has the standard Heston solution:

$$
\gamma_i = \sqrt{(\kappa_i - i\rho_i\xi_i u)^2 + \xi_i^2(iu + u^2)}
$$

$$
g_i = \frac{\kappa_i - i\rho_i\xi_i u - \gamma_i}{\kappa_i - i\rho_i\xi_i u + \gamma_i}
$$

The $D$-function increment on interval $i$ starting from terminal value $D_{\text{in}}$ is obtained by substituting into the general Riccati solution with initial condition $D_{\text{in}}$ rather than zero. When $D_{\text{in}} = 0$ (the rightmost interval), the standard formula applies:

$$
D_i(\tau_i) = \frac{\kappa_i - i\rho_i\xi_i u - \gamma_i}{\xi_i^2}\cdot\frac{1 - e^{-\gamma_i\tau_i}}{1 - g_i e^{-\gamma_i\tau_i}}
$$

For interior intervals where $D_{\text{in}} \neq 0$, a numerical ODE solver (e.g., fourth-order Runge-Kutta) is typically used.

---

## Calibration with Time-Dependent Parameters

### Objective Function

Calibration proceeds by minimizing the distance between model and market implied volatilities across all strikes and maturities:

$$
\min_{\Theta}\;\sum_{j=1}^{M}\sum_{k=1}^{K_j} w_{jk}\left[\sigma^{\text{model}}(K_k, T_j; \Theta) - \sigma^{\text{mkt}}(K_k, T_j)\right]^2
$$

where $\Theta = \{v_0, \kappa_i, \theta_i, \xi_i, \rho_i\}_{i=1}^N$ and $w_{jk}$ are liquidity-based weights.

### Sequential Calibration Strategy

A key practical advantage of the piecewise-constant structure is that calibration can proceed **sequentially by maturity**:

1. **Calibrate to $T_1$**: Find $(\kappa_1, \theta_1, \xi_1, \rho_1, v_0)$ fitting all strikes at the shortest maturity
2. **Calibrate to $T_2$**: Fix interval-1 parameters; find $(\kappa_2, \theta_2, \xi_2, \rho_2)$ fitting $T_2$ strikes
3. **Continue** through each subsequent maturity

This reduces a high-dimensional global optimization to a sequence of low-dimensional problems.

!!! warning "Overfitting and Stability"
    With $4N$ parameters and $N$ maturities, the model can interpolate market prices exactly but may produce unstable parameter estimates. Regularization is essential:

    - Penalize large changes $|\theta_{i+1} - \theta_i|$ between adjacent intervals
    - Constrain $\kappa_i$ and $\rho_i$ to be constant or slowly varying
    - Ensure the Feller condition $2\kappa_i\theta_i > \xi_i^2$ holds on each interval to avoid boundary issues

---

## Comparison with Constant-Parameter Heston

| Aspect | Constant parameters | Piecewise-constant parameters |
|--------|--------------------|-----------------------------|
| **Free parameters** | 5 | $\leq 4N + 1$ |
| **Term structure fit** | Limited | Exact at grid maturities |
| **Characteristic function** | Single closed-form evaluation | $N$ sequential evaluations |
| **Calibration** | Global optimization (5-dim) | Sequential low-dim problems |
| **Exotic pricing** | Consistent but biased | Better fit but path-dependent pricing requires care |
| **Feller condition** | One check | Must hold on each interval |

!!! example "Typical Calibration Grid"
    For SPX options, a common choice is $N = 6$ intervals matching liquid expiries: 1M, 3M, 6M, 1Y, 2Y, 5Y. With $\theta_i$ and $\xi_i$ varying and $\kappa$, $\rho$ fixed, this gives 14 free parameters fitting approximately 100--200 market prices.

---

## Summary

| Concept | Key formula or idea |
|---------|-------------------|
| SDE extension | $\kappa(t), \theta(t), \xi(t), \rho(t)$ deterministic functions |
| Piecewise-constant | Parameters constant on $[T_{i-1}, T_i)$, matching option expiries |
| Characteristic function | Sequential backward Riccati integration |
| Affine preservation | Affine on each interval; chain via continuity of $C, D$ |
| Calibration | Sequential by maturity; regularize inter-interval jumps |

The piecewise-constant extension connects to the [Bates model](bates_model.md) (adding jumps for short-maturity fit) and the [Double Heston model](double_heston_model.md) (adding a second factor for richer dynamics). All three extensions address the same fundamental limitation: constant-parameter Heston cannot simultaneously reproduce the entire term structure of market smiles.
