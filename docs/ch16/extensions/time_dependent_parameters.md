# Time-Dependent Parameters

Recall standard Heston with constant $(\kappa, \theta, \xi, \rho)$ (see [§ Heston SDE and Parameters](../model_definition/heston_sde_and_parameters.md)): a single parameter set cannot simultaneously match steep short-maturity skews and flatter long-maturity smiles. Allowing parameters to vary with time --- typically as piecewise-constant functions on a maturity grid --- gives enough flexibility to fit the full term structure while preserving the affine structure (see [§ Affine Structure and Riccati](../model_definition/affine_structure_and_riccati.md)).

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

On interval $[T_{i-1}, T_i]$ of length $\tau_i$, the Riccati ODE for $D$ with constant coefficients $(\kappa_i, \xi_i, \rho_i)$ admits the standard Heston solution in terms of $\gamma_i, g_i$ (see [§ Closed-Form Characteristic Function](../heston_cf/closed_form_characteristic_function.md)). For the rightmost interval ($D_{\text{in}}=0$), the standard formula applies directly; for interior intervals where $D_{\text{in}} \neq 0$, a numerical ODE solver (e.g., fourth-order Runge-Kutta) is typically used.

---

## Calibration with Time-Dependent Parameters

### Objective Function

Recall the standard Heston calibration objective (see [§ Calibration](../calibration/calibration_to_iv_surface.md)): minimize the weighted squared implied-volatility error across strikes and maturities, now over the extended parameter set $\Theta = \{v_0, \kappa_i, \theta_i, \xi_i, \rho_i\}_{i=1}^N$.

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

---

## Exercises

**Exercise 1.**
A piecewise-constant Heston model uses two intervals: $[0, T_1]$ with parameters $(\kappa_1, \theta_1, \xi_1, \rho_1)$ and $[T_1, T_2]$ with $(\kappa_2, \theta_2, \xi_2, \rho_2)$. If $T_1 = 0.25$ and $T_2 = 1.0$, how many total parameters are there (including $v_0$)? If the market provides 5 maturities with 9 strikes each (45 options), what is the data-to-parameter ratio?

??? success "Solution to Exercise 1"
    With two intervals $[0, T_1]$ and $[T_1, T_2]$, each interval has 4 parameters: $(\kappa_i, \theta_i, \xi_i, \rho_i)$ for $i = 1, 2$. Including the initial variance $v_0$:

    $$
    \text{Total parameters} = 4 \times 2 + 1 = 9
    $$

    With 5 maturities and 9 strikes per maturity, the market provides $5 \times 9 = 45$ option prices.

    $$
    \text{Data-to-parameter ratio} = \frac{45}{9} = 5.0
    $$

    A ratio of 5:1 is at the lower end of what is considered adequate for stable calibration. While the model has enough data points to formally constrain all parameters, several considerations suggest that care is needed:

    - Not all 45 options are equally informative: ATM options primarily constrain $v_0$ and $\theta_i$, while wing options constrain $\xi_i$ and $\rho_i$
    - Options at maturities between $T_1$ and $T_2$ are influenced by **both** parameter sets, creating correlation in the parameter estimates
    - A ratio of at least 10:1 is preferable for robust calibration

    In practice, one would typically reduce the effective parameter count by fixing $\kappa$ globally (it is poorly identified from European options alone) or imposing continuity constraints, bringing the effective ratio closer to $45/7 \approx 6.4$.

---

**Exercise 2.**
The CF for piecewise-constant parameters is computed by chaining: first solve the Riccati system on $[T_1, T_2]$ with parameters $(\kappa_2, \theta_2, \xi_2, \rho_2)$ and terminal condition $C(0) = D(0) = 0$, then use $C(T_2 - T_1)$ and $D(T_2 - T_1)$ as initial conditions for the next interval. Describe this sequential integration procedure. Why does the order of integration matter?

??? success "Solution to Exercise 2"
    The sequential integration procedure for piecewise-constant parameters works backward from the option maturity $T_2$ to the pricing time $t = 0$.

    **Step 1: Rightmost interval $[T_1, T_2]$.**

    On this interval, the parameters are constant at $(\kappa_2, \theta_2, \xi_2, \rho_2)$. Solve the Riccati ODE backward from the terminal condition:

    $$
    D(T_2, T_2; u) = 0, \qquad C(T_2, T_2; u) = 0
    $$

    Using the standard Heston closed-form Riccati solution with parameters $(\kappa_2, \theta_2, \xi_2, \rho_2)$ and interval length $\tau_2 = T_2 - T_1$, compute $D(T_1, T_2; u)$ and $C(T_1, T_2; u)$.

    **Step 2: Left interval $[0, T_1]$.**

    On this interval, the parameters change to $(\kappa_1, \theta_1, \xi_1, \rho_1)$. The Riccati ODE for $D$ is now solved with initial condition $D(T_1) = D(T_1, T_2; u)$ from Step 1 (not zero). The function $C$ accumulates additively:

    $$
    C(0, T_2; u) = C(T_1, T_2; u) + \int_0^{T_1} \kappa_1 \theta_1 D(s, T_2; u) \, ds + iu(r-q)T_1
    $$

    When $D(T_1) \neq 0$, the standard closed-form Riccati solution (which assumes $D(0) = 0$) cannot be applied directly. Instead, one must either:

    - Use a numerical ODE solver (e.g., Runge-Kutta) for the $D$-equation on $[0, T_1]$ with the non-zero initial condition
    - Apply a change of variables that transforms the non-zero initial condition problem into a zero initial condition problem with modified parameters

    **Why the order of integration matters:**

    The backward integration order (from $T_2$ to $0$) is essential because the **terminal** condition for the characteristic function is known ($D = 0, C = 0$ at maturity), while the initial condition at $t = 0$ is what we seek. If we attempted forward integration starting from $t = 0$, we would not know the correct initial conditions for $C$ and $D$, since these depend on the full parameter path from $0$ to $T_2$.

    Furthermore, the $D$-function at each interval boundary serves as the "boundary condition" for the next (earlier) interval. Integrating in the wrong direction would require iterative methods to satisfy the terminal conditions, destroying the sequential (non-iterative) nature of the algorithm.

---

**Exercise 3.**
Allowing $\rho$ to vary between intervals means the leverage effect can be different at short and long horizons. If $\rho_1 = -0.85$ (steep short-maturity skew) and $\rho_2 = -0.50$ (flatter long-maturity skew), explain how this matches the empirical observation that equity skews flatten with maturity. What constraint ensures continuity of the implied volatility surface at the interval boundary $T_1$?

??? success "Solution to Exercise 3"
    **Matching empirical skew flattening:**

    The equity implied volatility skew $\partial\sigma_{\text{imp}}/\partial\ln K |_{K=F}$ is empirically observed to be steep at short maturities and to flatten with increasing maturity. This is a robust stylized fact across equity indices.

    With $\rho_1 = -0.85$ on $[0, T_1]$ and $\rho_2 = -0.50$ on $[T_1, T_2]$:

    - **Short-maturity options** ($T \leq T_1$): The skew is governed entirely by $\rho_1 = -0.85$, producing a steep negative skew. The strong negative correlation means that when the stock drops, variance increases sharply, driving OTM put implied volatilities up and creating a pronounced skew.

    - **Long-maturity options** ($T_1 < T \leq T_2$): The skew receives contributions from both intervals. On $[0, T_1]$, the strong leverage $\rho_1 = -0.85$ operates, but on $[T_1, T_2]$, the weaker $\rho_2 = -0.50$ applies. The net effect is a weighted average that produces a flatter skew than at short maturities.

    This directly matches the empirical observation: the skew flattens because the leverage effect (as captured by $\rho$) is allowed to weaken at longer horizons.

    **Continuity of the implied volatility surface at $T_1$:**

    The implied volatility surface is automatically continuous at $T_1$ because:

    1. The characteristic function is continuous in $T$: the functions $C(0, T; u)$ and $D(0, T; u)$ are continuous at $T = T_1$ by construction. As $T \to T_1^+$ from above, the interval $[T_1, T]$ shrinks to zero length, and the Riccati solution on that interval approaches the identity ($D \to 0$, $C \to 0$), so the CF approaches the CF for maturity $T_1$ from below.

    2. No explicit constraint is needed. The continuity is a consequence of the affine structure: the CF is an analytic function of $T$, and the piecewise-constant parameter change occurs smoothly because the Riccati integration chains continuously.

    However, while the surface is continuous, the **derivative** $\partial\sigma_{\text{imp}}/\partial T$ may exhibit a kink at $T_1$ due to the abrupt parameter change. If smoothness of the term structure is desired, one can impose regularization such as $|\rho_2 - \rho_1| \leq \delta$ for some bound $\delta$.

---

**Exercise 4.**
The calibration of piecewise-constant parameters is typically done sequentially: first calibrate $(\kappa_1, \theta_1, \xi_1, \rho_1)$ to options with $T \leq T_1$, then calibrate $(\kappa_2, \theta_2, \xi_2, \rho_2)$ to options with $T_1 < T \leq T_2$ (holding the first interval's parameters fixed). Discuss the advantages and disadvantages of this sequential approach compared to simultaneous calibration of all parameters.

??? success "Solution to Exercise 4"
    **Sequential calibration:**

    *Advantages:*

    1. **Reduced dimensionality:** Each stage is a low-dimensional optimization (4--5 parameters), which is much easier to solve than a joint optimization over 9+ parameters. Local optimizers (Levenberg-Marquardt, Nelder-Mead) converge reliably in low dimensions.

    2. **Speed:** Each stage uses only the options at one maturity, so the objective function is cheap to evaluate. The total calibration time is approximately the sum of two fast calibrations, rather than one slow high-dimensional calibration.

    3. **Interpretability:** Parameters at each maturity have a clear economic meaning. If the fit at $T_2$ is poor, the issue is localized to the second interval's parameters.

    4. **Stability:** Fixing earlier parameters eliminates cross-maturity parameter interactions, reducing the likelihood of parameter degeneracies.

    *Disadvantages:*

    1. **Error propagation:** Any error in the Stage 1 parameters $(\kappa_1, \theta_1, \xi_1, \rho_1)$ is permanently baked in and cannot be corrected by Stage 2. If Stage 1 produces a slightly biased $v_0$ (which affects all maturities), the subsequent stages must compensate, potentially leading to unphysical parameter values.

    2. **Sub-optimality:** The sequential approach does not minimize the global objective function. The total error $\sum_j \sum_k w_{jk}[\sigma^{\text{model}} - \sigma^{\text{mkt}}]^2$ across all maturities is not necessarily at its minimum, because the Stage 1 parameters were chosen without regard to the Stage 2 data.

    3. **Ordering dependence:** The result depends on calibrating short maturities first. If one instead calibrated long maturities first and worked backward, different parameters would result.

    4. **Cross-maturity information lost:** Options at intermediate maturities contain information about both parameter sets simultaneously. The sequential approach ignores this cross-maturity information.

    **Simultaneous calibration** avoids these issues by minimizing the global objective, but at the cost of solving a 9-dimensional optimization problem that may have multiple local minima and requires good initialization. The standard practical approach is to use sequential calibration for initialization, followed by a global refinement step.

---

**Exercise 5.**
Adding more intervals improves the fit but increases the risk of overfitting and parameter instability. Propose a regularization strategy that penalizes large jumps between consecutive intervals: $\sum_k \lambda (\Theta_{k+1} - \Theta_k)^2$. For $\lambda = 1.0$ and intervals with $(\rho_1, \rho_2, \rho_3) = (-0.85, -0.65, -0.50)$, compute the regularization penalty. How does this compare to a typical fit improvement of $10^{-4}$ in the objective function?

??? success "Solution to Exercise 5"
    The regularization penalty for parameter jumps between consecutive intervals is:

    $$
    R(\Theta) = \sum_{k=1}^{N-1} \lambda \, (\Theta_{k+1} - \Theta_k)^2
    $$

    Applied to $\rho$ only, with $(\rho_1, \rho_2, \rho_3) = (-0.85, -0.65, -0.50)$ and $\lambda = 1.0$:

    $$
    R_\rho = 1.0 \times \left[(\rho_2 - \rho_1)^2 + (\rho_3 - \rho_2)^2\right]
    $$

    $$
    = 1.0 \times \left[(-0.65 - (-0.85))^2 + (-0.50 - (-0.65))^2\right]
    $$

    $$
    = 1.0 \times \left[(0.20)^2 + (0.15)^2\right] = 1.0 \times [0.04 + 0.0225] = 0.0625
    $$

    **Comparison with fit improvement:** A typical fit improvement (reduction in the sum of squared implied volatility errors) when adding more intervals is on the order of $10^{-4}$ (in units of implied volatility squared, e.g., $(0.01)^2 = 10^{-4}$ corresponds to a 1 vol-point improvement in RMSE).

    The regularization penalty of $0.0625$ is **625 times larger** than the typical fit improvement of $10^{-4}$. This means the regularization heavily penalizes the parameter jumps and would dominate the objective function.

    **Practical implications:**

    - With $\lambda = 1.0$, the optimizer would strongly prefer keeping $\rho$ nearly constant across intervals, effectively defeating the purpose of time-dependent parameters
    - A more appropriate $\lambda$ would balance regularization and fit quality. Setting $\lambda$ so that $R_\rho \approx 10^{-4}$ gives $\lambda \approx 10^{-4}/0.0625 = 1.6 \times 10^{-3}$
    - The optimal $\lambda$ can be chosen by cross-validation: hold out a subset of options, calibrate with various $\lambda$ values on the remaining options, and select $\lambda$ that minimizes the prediction error on the held-out set
    - Alternatively, scale the regularization relative to the data term: $\lambda = \alpha / M$ where $M$ is the number of options and $\alpha$ is a tuning parameter of order 1

    The key insight is that regularization should be calibrated relative to the scale of the fitting objective, not chosen arbitrarily.

---

**Exercise 6.**
The time-dependent Heston model with $N$ intervals has $4N + 1$ parameters (4 per interval plus $v_0$). For $N = 5$, this gives 21 parameters. If the calibration surface has 60 options, the ratio is approximately 3:1. Design a strategy to keep the effective parameter count manageable: for example, fix $\kappa$ and $\xi$ across all intervals (they are poorly identified) and vary only $\theta$ and $\rho$. How many parameters does this reduced model have?

??? success "Solution to Exercise 6"
    **Full time-dependent model with $N = 5$ intervals:**

    $$
    \text{Parameters} = 4N + 1 = 4(5) + 1 = 21
    $$

    With 60 options, the ratio is $60/21 \approx 2.9$, which is dangerously close to overfitting.

    **Reduced model: fix $\kappa$ and $\xi$ globally, vary $\theta_i$ and $\rho_i$:**

    - Global parameters: $\kappa$, $\xi$, $v_0$ (3 parameters)
    - Per-interval parameters: $\theta_i$, $\rho_i$ for $i = 1, \ldots, 5$ ($2 \times 5 = 10$ parameters)

    $$
    \text{Total parameters} = 3 + 10 = 13
    $$

    The data-to-parameter ratio improves to $60/13 \approx 4.6$.

    **Justification for fixing $\kappa$ and $\xi$:**

    1. **$\kappa$ (mean-reversion speed):** This parameter is notoriously poorly identified from European option prices. It primarily affects the rate of convergence of the variance toward $\theta$, which is a second-order effect on the implied volatility surface. Different values of $\kappa$ can be compensated by adjusting $\theta$ and $v_0$. Fixing $\kappa$ globally at a reasonable value (e.g., $\kappa = 2$) has minimal impact on calibration quality.

    2. **$\xi$ (vol-of-vol):** While $\xi$ significantly affects smile curvature, its effect is partially degenerate with $\rho$ in determining the skew. Fixing $\xi$ globally is more restrictive than fixing $\kappa$, but it prevents the instability that arises from letting both $\xi_i$ and $\rho_i$ vary simultaneously (since their product $\rho_i \xi_i$ is what primarily drives the skew).

    **Alternative reduced models:**

    | Configuration | Parameters | Ratio (60 options) |
    |:---|:---:|:---:|
    | Full: all vary | 21 | 2.9 |
    | Fix $\kappa$; vary $\theta_i, \xi_i, \rho_i$ | 16 | 3.8 |
    | Fix $\kappa, \xi$; vary $\theta_i, \rho_i$ | 13 | 4.6 |
    | Fix $\kappa, \xi, \rho$; vary $\theta_i$ | 8 | 7.5 |

    The configuration with $\theta_i$ and $\rho_i$ varying (13 parameters) represents a good trade-off: $\theta_i$ controls the ATM term structure and $\rho_i$ controls the skew term structure, which are the two most important features that time-dependent parameters should capture. Adding per-interval $\xi_i$ (16 parameters) provides curvature term structure control but at the cost of a worse data-to-parameter ratio and potential instability.
