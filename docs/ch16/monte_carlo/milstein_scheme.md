# Milstein Scheme for the Heston Model

The Euler-Maruyama scheme achieves strong convergence order $\frac{1}{2}$, which means halving the time step only reduces the pathwise error by a factor of $\sqrt{2}$. The **Milstein scheme** adds a correction term derived from the Ito-Taylor expansion that captures the curvature of the diffusion coefficient, boosting the strong convergence order to 1 for scalar SDEs. Applying Milstein to the Heston model, however, reveals a subtle obstacle: the two-dimensional correlated system requires simulation of the **Levy area**, which is computationally expensive and difficult to implement correctly.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the Milstein correction term from the Ito-Taylor expansion for a scalar SDE
    2. Apply the Milstein scheme to the CIR variance process with its square-root diffusion
    3. Explain the Levy area problem that arises in correlated multi-dimensional SDEs
    4. Assess when Milstein offers a practical advantage over Euler for Heston simulation

!!! tip "Prerequisites"
    This section builds on the [Euler discretization](euler_discretization_and_pitfalls.md) and the [CIR variance process](../variance_dynamics/cir_variance_process_solution.md).

---

## The Ito-Taylor Expansion

To understand the Milstein correction, consider a generic scalar SDE:

$$
dY_t = a(Y_t) \, dt + b(Y_t) \, dW_t
$$

The Euler-Maruyama scheme approximates the increment over $[t_n, t_{n+1}]$ by freezing the coefficients at $t_n$:

$$
Y_{n+1}^{\text{Euler}} = Y_n + a(Y_n) \Delta t + b(Y_n) \Delta W_n
$$

The **Ito-Taylor expansion** of $b(Y_t)$ around $Y_n$ gives the next-order correction. Applying Ito's formula to $b(Y_t)$:

$$
b(Y_t) = b(Y_n) + \int_{t_n}^{t} b'(Y_s) b(Y_s) \, dW_s + \text{higher order terms}
$$

Substituting this into the stochastic integral $\int_{t_n}^{t_{n+1}} b(Y_t) \, dW_t$ and retaining the leading correction yields the **Milstein scheme**:

$$
Y_{n+1} = Y_n + a(Y_n) \Delta t + b(Y_n) \Delta W_n + \frac{1}{2} b(Y_n) b'(Y_n) \left[ (\Delta W_n)^2 - \Delta t \right]
$$

The additional term $\frac{1}{2} b(Y_n) b'(Y_n) [(\Delta W_n)^2 - \Delta t]$ is the **Milstein correction**. It captures the leading nonlinear effect of the diffusion and improves the strong convergence order from $\frac{1}{2}$ to $1$.

---

## Milstein Applied to the CIR Variance Process

The CIR variance process in the Heston model has the form:

$$
dv_t = \kappa(\theta - v_t) \, dt + \xi \sqrt{v_t} \, dW_t^{(2)}
$$

Here the drift is $a(v) = \kappa(\theta - v)$ and the diffusion is $b(v) = \xi\sqrt{v}$. The derivative of the diffusion coefficient is:

$$
b'(v) = \frac{\xi}{2\sqrt{v}}
$$

The Milstein correction term becomes:

$$
\frac{1}{2} b(v_n) b'(v_n) = \frac{1}{2} \cdot \xi\sqrt{v_n} \cdot \frac{\xi}{2\sqrt{v_n}} = \frac{\xi^2}{4}
$$

This is remarkably simple: the correction is a **constant** independent of $v_n$. The full Milstein update for the variance is:

$$
v_{n+1} = v_n + \kappa(\theta - v_n) \Delta t + \xi\sqrt{v_n^+} \, \Delta W_n^{(2)} + \frac{\xi^2}{4}\left[(\Delta W_n^{(2)})^2 - \Delta t\right]
$$

where $v_n^+ = \max(v_n, 0)$ applies the full truncation fix from the Euler section.

!!! note "The Constant Correction"
    The fact that $b(v)b'(v) = \xi^2/2$ is constant for the CIR process is special. For most nonlinear diffusions, the Milstein correction depends on the current state. This simplification makes Milstein particularly easy to implement for CIR-type processes.

---

## Milstein for the Log-Price Process

The log-price process $x_t = \ln S_t$ satisfies:

$$
dx_t = \left(r - q - \tfrac{1}{2} v_t\right) dt + \sqrt{v_t} \, dW_t^{(1)}
$$

Here the diffusion is $b(x, v) = \sqrt{v}$, which depends on $v$ rather than $x$. Since $\partial b / \partial x = 0$, the Milstein correction in the $x$-direction vanishes. The log-price update is:

$$
x_{n+1} = x_n + \left(r - q - \tfrac{1}{2} v_n^+\right) \Delta t + \sqrt{v_n^+} \, \Delta W_n^{(1)}
$$

This is identical to the Euler update. The Milstein improvement for the Heston model concentrates entirely in the variance equation.

---

## The Levy Area Problem

### Why Multi-Dimensional Milstein Is Hard

For a system of SDEs driven by correlated Brownian motions, the full Milstein scheme requires not only the increments $\Delta W^{(1)}$ and $\Delta W^{(2)}$ but also the **Levy area** (or iterated stochastic integral):

$$
A_{n} = \int_{t_n}^{t_{n+1}} \int_{t_n}^{s} dW_u^{(1)} \, dW_s^{(2)} - \int_{t_n}^{t_{n+1}} \int_{t_n}^{s} dW_u^{(2)} \, dW_s^{(1)}
$$

This double integral measures the "area" swept by the two-dimensional Brownian path and captures the cross-interaction between the two noise sources. When $\rho \neq 0$, the Levy area has a non-trivial distribution that cannot be expressed in closed form in terms of $\Delta W^{(1)}$ and $\Delta W^{(2)}$ alone.

### Consequences for Convergence

Without simulating the Levy area, the Milstein scheme for the correlated 2D Heston system does **not** achieve strong order 1 in general. The achievable convergence orders are:

| Component | With Levy Area | Without Levy Area |
|-----------|---------------|-------------------|
| Variance (1D Milstein) | Strong order 1 | Strong order 1 |
| Full 2D system | Strong order 1 | Strong order $\frac{1}{2}$ |

The variance equation alone benefits from the Milstein correction (strong order 1), because it is a scalar SDE in $v$ driven by a single Brownian motion $W^{(2)}$. The cross-coupling through $\rho$ only affects the joint simulation of $(x, v)$.

### Practical Implications

Simulating the Levy area accurately requires either:

1. **Truncated Fourier series** approximations (Wiktorsson, 2001), which add $\mathcal{O}(p)$ operations per step for $p$ Fourier terms
2. **Exact sampling** methods that are computationally expensive

For most practical purposes, the improvement from strong order $\frac{1}{2}$ to strong order 1 in the joint system does not justify the cost of Levy area simulation. This is a key reason why practitioners prefer the [QE scheme](quadratic_exponential_scheme.md) or [exact simulation](exact_simulation_broadie_kaya.md), which achieve near-exact accuracy without Ito-Taylor corrections.

!!! warning "When Milstein Without Levy Area Helps"
    Even without the Levy area, applying the Milstein correction to the variance process alone can reduce pricing bias compared to pure Euler. The variance is the "difficult" component (non-Lipschitz diffusion), and improving its simulation accuracy benefits the overall price estimate. The log-price equation, being linear in $x$, is already well-handled by Euler.

---

## Convergence Comparison

The following table summarizes the convergence properties of Euler and Milstein for the Heston model:

| Property | Euler (Full Truncation) | Milstein (Variance Only) | Milstein (Full 2D + Levy) |
|----------|------------------------|--------------------------|---------------------------|
| Weak order | 1 | 1 | 1 |
| Strong order (variance) | $\frac{1}{2}$ | 1 | 1 |
| Strong order (joint) | $\frac{1}{2}$ | $\frac{1}{2}$ | 1 |
| Cost per step | $\mathcal{O}(1)$ | $\mathcal{O}(1)$ | $\mathcal{O}(p)$ |
| Implementation | Simple | Simple | Complex |

For **weak convergence** (relevant to option pricing), both Euler and Milstein achieve order 1, so the pricing accuracy improvement from Milstein is modest. The main benefit of Milstein is in **strong convergence** for path-dependent payoffs where individual path accuracy matters.

---

## Worked Example

Consider the Heston parameters from the Euler section:

| Parameter | Value |
|-----------|-------|
| $v_0$ | $0.04$ |
| $\kappa$ | $1.5$ |
| $\theta$ | $0.04$ |
| $\xi$ | $0.3$ |
| $\Delta t$ | $1/252$ |

**Single Milstein step for variance**: Suppose $v_n = 0.04$ and draw $Z_2 = -1.5$ (a moderately negative shock). Then $\Delta W^{(2)} = \sqrt{1/252} \cdot (-1.5) \approx -0.0945$.

**Euler update:**

$$
v_{n+1}^{\text{Euler}} = 0.04 + 1.5(0.04 - 0.04)(1/252) + 0.3\sqrt{0.04}(-0.0945) \approx 0.04 - 0.00567 = 0.03433
$$

**Milstein update:**

$$
v_{n+1}^{\text{Milstein}} = 0.03433 + \frac{0.09}{4}\left[(-0.0945)^2 - \frac{1}{252}\right] \approx 0.03433 + 0.0225(0.00893 - 0.00397) \approx 0.03444
$$

The Milstein correction adds approximately $0.00011$ to the variance, partially compensating for the downward shock. Over many steps, these corrections accumulate to reduce the strong error significantly.

??? example "Convergence Rate Verification"
    To verify the convergence orders empirically, simulate $M$ paths with step sizes $\Delta t \in \{1/50, 1/100, 1/200, 1/400\}$:

    1. For each $\Delta t$, compute the variance at $T = 1$ using both Euler and Milstein
    2. Use a very fine grid ($\Delta t = 1/10000$) as the "exact" reference
    3. Compute the strong error: $\varepsilon(\Delta t) = \left(\frac{1}{M}\sum_{m=1}^{M}|v_N^{(m)} - v_{\text{ref}}^{(m)}|^2\right)^{1/2}$
    4. Plot $\log \varepsilon$ vs $\log \Delta t$: Euler gives slope $\approx 0.5$; Milstein (variance only) gives slope $\approx 1.0$

---

## Summary

The Milstein scheme improves the strong convergence order of the CIR variance discretization from $\frac{1}{2}$ to 1 by adding the correction term $\frac{\xi^2}{4}[(\Delta W)^2 - \Delta t]$, which is constant for the square-root diffusion. For the log-price equation, the Milstein correction vanishes because the diffusion does not depend on $x$. The correlated two-dimensional Heston system requires the Levy area for full strong order 1 convergence, which is expensive to simulate. In practice, applying Milstein to the variance process alone (without the Levy area) offers a modest improvement over Euler at negligible additional cost. For substantially better accuracy, the [QE scheme](quadratic_exponential_scheme.md) and [exact simulation](exact_simulation_broadie_kaya.md) are preferred.

---

## Exercises

**Exercise 1.**
The Milstein correction for a general scalar SDE $dY = a(Y)\,dt + b(Y)\,dW$ is $\frac{1}{2}b(Y)b'(Y)[(\Delta W)^2 - \Delta t]$. For the CIR process, $b(v) = \xi\sqrt{v}$ and $b'(v) = \xi/(2\sqrt{v})$, giving $b(v)b'(v) = \xi^2/2$. Now consider the alternative diffusion $b(v) = \xi v^\alpha$ for general $\alpha > 0$. Compute $b(v)b'(v)$ and show that the correction is state-dependent except when $\alpha = 1/2$ (the CIR case). For $\alpha = 1$ (geometric Brownian motion for the variance), what is the Milstein correction?

??? success "Solution to Exercise 1"
    For a general diffusion $b(v) = \xi v^\alpha$, the derivative is:

    $$
    b'(v) = \alpha \xi v^{\alpha - 1}
    $$

    The Milstein product is:

    $$
    b(v)b'(v) = \xi v^\alpha \cdot \alpha \xi v^{\alpha - 1} = \alpha \xi^2 v^{2\alpha - 1}
    $$

    **State dependence:** The correction $\frac{1}{2}b(v)b'(v)[(\Delta W)^2 - \Delta t]$ depends on $v$ through the factor $v^{2\alpha - 1}$. This is state-independent only when $2\alpha - 1 = 0$, i.e., $\alpha = 1/2$. For $\alpha = 1/2$ (the CIR case):

    $$
    b(v)b'(v) = \frac{1}{2}\xi^2 v^0 = \frac{\xi^2}{2}
    $$

    which is constant, as shown in the text.

    **For** $\alpha = 1$ **(geometric Brownian motion for variance):** $b(v) = \xi v$, $b'(v) = \xi$, so:

    $$
    b(v)b'(v) = \xi v \cdot \xi = \xi^2 v
    $$

    The Milstein correction is:

    $$
    \frac{1}{2}\xi^2 v_n [(\Delta W)^2 - \Delta t]
    $$

    This is the well-known Milstein correction for geometric Brownian motion. It is proportional to $v_n$, so it scales with the current variance level. The full Milstein update becomes:

    $$
    v_{n+1} = v_n + \kappa(\theta - v_n)\Delta t + \xi v_n \Delta W + \frac{1}{2}\xi^2 v_n[(\Delta W)^2 - \Delta t]
    $$

    For $\alpha = 1$, the diffusion coefficient is globally Lipschitz (unlike $\alpha = 1/2$), so standard Milstein convergence theory applies directly without the complications of the CIR square-root singularity.

    **General pattern:** For $\alpha < 1/2$, the correction $v^{2\alpha-1} \to \infty$ as $v \to 0$, making Milstein numerically unstable near zero. For $\alpha > 1/2$, the correction $v^{2\alpha-1} \to 0$ as $v \to 0$, which is well-behaved. The CIR case $\alpha = 1/2$ is the unique boundary where the correction is constant.

---

**Exercise 2.**
The worked example computes a single Milstein step with $v_n = 0.04$, $Z_2 = -1.5$, $\Delta t = 1/252$. The Milstein correction adds $0.00011$ to the Euler value. Compute the correction as a percentage of the Euler increment $|v_{n+1}^{\text{Euler}} - v_n|$. For what magnitude of $Z_2$ does the Milstein correction exceed 10% of the Euler increment? Does the correction always have the same sign as $(\Delta W)^2 - \Delta t$?

??? success "Solution to Exercise 2"
    From the worked example: $v_{n+1}^{\text{Euler}} = 0.03433$, so the Euler increment is:

    $$
    |v_{n+1}^{\text{Euler}} - v_n| = |0.03433 - 0.04| = 0.00567
    $$

    The Milstein correction is $0.00011$. As a percentage of the Euler increment:

    $$
    \frac{0.00011}{0.00567} \times 100\% \approx 1.94\%
    $$

    **When does the correction exceed 10% of the Euler increment?** The Milstein correction is:

    $$
    \frac{\xi^2}{4}[(\Delta W)^2 - \Delta t] = \frac{0.09}{4}[\Delta t \cdot Z_2^2 - \Delta t] = \frac{0.09\Delta t}{4}(Z_2^2 - 1) = 0.0225 \cdot \frac{1}{252}(Z_2^2 - 1)
    $$

    The Euler increment (dominated by the diffusion term for large $|Z_2|$) is approximately:

    $$
    |\text{Euler increment}| \approx \xi\sqrt{v_n}\sqrt{\Delta t}|Z_2| = 0.3 \times 0.2 \times \frac{1}{\sqrt{252}}|Z_2| \approx \frac{0.06}{\sqrt{252}}|Z_2|
    $$

    The ratio of correction to Euler increment is approximately:

    $$
    \frac{0.0225(Z_2^2 - 1)/252}{0.06|Z_2|/\sqrt{252}} = \frac{0.0225(Z_2^2 - 1)}{0.06\sqrt{252}|Z_2|} = \frac{0.375(|Z_2| - 1/|Z_2|)}{\sqrt{252}}
    $$

    Setting this $> 0.10$:

    $$
    |Z_2| - \frac{1}{|Z_2|} > \frac{0.10\sqrt{252}}{0.375} \approx 4.23
    $$

    Solving the quadratic $|Z_2|^2 - 4.23|Z_2| - 1 > 0$ gives $|Z_2| > (4.23 + \sqrt{4.23^2 + 4})/2 \approx 4.46$.

    So the Milstein correction exceeds 10% of the Euler increment only for extreme draws $|Z_2| > 4.46$, which occur with probability $\approx 8 \times 10^{-6}$. For typical draws, the correction is a small fraction of the Euler step.

    **Sign of the correction:** The correction is $\frac{\xi^2}{4}[(\Delta W)^2 - \Delta t]$, which has the same sign as $Z_2^2 - 1$. It is positive when $|Z_2| > 1$ (probability $\approx 0.317$) and negative when $|Z_2| < 1$ (probability $\approx 0.683$). So the correction is more often negative than positive, but on average equals zero.

---

**Exercise 3.**
The Milstein correction $\frac{\xi^2}{4}[(\Delta W)^2 - \Delta t]$ has expected value zero (since $\mathbb{E}[(\Delta W)^2] = \Delta t$). Show this directly: $\mathbb{E}[\frac{\xi^2}{4}((\Delta W)^2 - \Delta t)] = \frac{\xi^2}{4}(\Delta t - \Delta t) = 0$. Compute the variance of the correction term and show it equals $\frac{\xi^4}{8}\Delta t^2$. For $\xi = 0.3$ and $\Delta t = 1/252$, is this variance significant compared to the variance of the Euler diffusion term $\xi^2 v_n \Delta t$?

??? success "Solution to Exercise 3"
    The Milstein correction is $\frac{\xi^2}{4}[(\Delta W)^2 - \Delta t]$ where $\Delta W = \sqrt{\Delta t}\,Z$ with $Z \sim N(0,1)$.

    **Expected value:**

    $$
    \mathbb{E}\!\left[\frac{\xi^2}{4}((\Delta W)^2 - \Delta t)\right] = \frac{\xi^2}{4}\left(\mathbb{E}[(\Delta W)^2] - \Delta t\right) = \frac{\xi^2}{4}(\Delta t - \Delta t) = 0
    $$

    since $\mathbb{E}[(\Delta W)^2] = \mathbb{E}[\Delta t \cdot Z^2] = \Delta t$.

    **Variance of the correction:** We need $\text{Var}\!\left(\frac{\xi^2}{4}[(\Delta W)^2 - \Delta t]\right)$:

    $$
    = \frac{\xi^4}{16}\,\text{Var}((\Delta W)^2 - \Delta t) = \frac{\xi^4}{16}\,\text{Var}((\Delta W)^2)
    $$

    Since $\Delta W = \sqrt{\Delta t}\,Z$, we have $(\Delta W)^2 = \Delta t \cdot Z^2$. Thus:

    $$
    \text{Var}((\Delta W)^2) = (\Delta t)^2 \text{Var}(Z^2) = (\Delta t)^2 \cdot 2
    $$

    using $\text{Var}(Z^2) = \mathbb{E}[Z^4] - (\mathbb{E}[Z^2])^2 = 3 - 1 = 2$. Therefore:

    $$
    \text{Var}\!\left(\text{correction}\right) = \frac{\xi^4}{16} \cdot 2(\Delta t)^2 = \frac{\xi^4}{8}(\Delta t)^2
    $$

    **Numerical comparison for** $\xi = 0.3$, $\Delta t = 1/252$, $v_n = 0.04$:

    - Variance of the Milstein correction: $\frac{0.09^2}{8} \cdot (1/252)^2 = \frac{0.0081}{8} \cdot 1.576 \times 10^{-5} \approx 1.59 \times 10^{-8}$
    - Variance of the Euler diffusion term $\xi\sqrt{v_n}\,\Delta W$: $\xi^2 v_n \Delta t = 0.09 \times 0.04 \times (1/252) = 1.43 \times 10^{-5}$

    The ratio is:

    $$
    \frac{1.59 \times 10^{-8}}{1.43 \times 10^{-5}} \approx 0.0011
    $$

    The variance of the Milstein correction is about $0.1\%$ of the variance of the Euler diffusion term. This confirms that the correction is a small perturbation on each individual step. Its cumulative effect on convergence comes from the systematic reduction in strong error over many steps, not from a large contribution at any single step.

---

**Exercise 4.**
The Levy area $A_n = \int_{t_n}^{t_{n+1}}\int_{t_n}^s dW_u^{(1)}\,dW_s^{(2)} - \int_{t_n}^{t_{n+1}}\int_{t_n}^s dW_u^{(2)}\,dW_s^{(1)}$ is needed for full strong order 1 in the 2D Heston system. Show that $\mathbb{E}[A_n] = 0$ and $\text{Var}(A_n) = \frac{1}{3}(\Delta t)^2$. Why can't $A_n$ be expressed as a function of $\Delta W^{(1)}$ and $\Delta W^{(2)}$ alone? Hint: $A_n$ measures the "signed area" enclosed by the 2D Brownian path, which requires path information beyond the endpoints.

??? success "Solution to Exercise 4"
    **Expected value:** Using the Ito isometry and the tower property:

    $$
    \mathbb{E}[A_n] = \mathbb{E}\!\left[\int_{t_n}^{t_{n+1}}\int_{t_n}^s dW_u^{(1)}\,dW_s^{(2)}\right] - \mathbb{E}\!\left[\int_{t_n}^{t_{n+1}}\int_{t_n}^s dW_u^{(2)}\,dW_s^{(1)}\right]
    $$

    For the first term, condition on $\mathcal{F}_s$: $\mathbb{E}\!\left[\int_{t_n}^s dW_u^{(1)}\,dW_s^{(2)}\right]$ involves the product of $\int_{t_n}^s dW_u^{(1)}$ (which is $\mathcal{F}_s$-measurable) and $dW_s^{(2)}$ (which is independent of $\mathcal{F}_s$ when $W^{(1)}$ and $W^{(2)}$ are independent). By iterated expectation, each term vanishes, giving $\mathbb{E}[A_n] = 0$.

    **Variance:** By the Ito isometry applied to double integrals:

    $$
    \text{Var}\!\left(\int_{t_n}^{t_{n+1}}\int_{t_n}^s dW_u^{(1)}\,dW_s^{(2)}\right) = \int_{t_n}^{t_{n+1}} \mathbb{E}\!\left[\left(\int_{t_n}^s dW_u^{(1)}\right)^2\right] ds = \int_{t_n}^{t_{n+1}} (s - t_n)\,ds = \frac{(\Delta t)^2}{2}
    $$

    Similarly for the other term. Since the two double integrals are correlated, a careful computation (see Kloeden and Platen, Chapter 5) yields:

    $$
    \text{Var}(A_n) = 2 \cdot \frac{(\Delta t)^2}{2} - 2\,\text{Cov}(\text{terms}) = \frac{(\Delta t)^2}{3}
    $$

    **Why** $A_n$ **cannot be expressed as a function of** $(\Delta W^{(1)}, \Delta W^{(2)})$ **alone:** The Brownian increments $\Delta W^{(1)} = W_{t_{n+1}}^{(1)} - W_{t_n}^{(1)}$ and $\Delta W^{(2)} = W_{t_{n+1}}^{(2)} - W_{t_n}^{(2)}$ are the endpoints of the two-dimensional Brownian path over $[t_n, t_{n+1}]$. The Levy area $A_n$ measures the signed area enclosed by the path in the $(W^{(1)}, W^{(2)})$ plane. Different Brownian paths can have the same endpoints but enclose different areas---just as a curve in the plane can start and end at the same points but sweep different areas. Formally, $A_n$ is not $\sigma(\Delta W^{(1)}, \Delta W^{(2)})$-measurable: knowing the increments determines the joint distribution of $A_n$ but not its realized value. The conditional distribution $A_n \mid (\Delta W^{(1)}, \Delta W^{(2)})$ is a non-degenerate random variable with variance of order $(\Delta t)^2$, which is precisely why omitting it degrades the strong convergence order.

---

**Exercise 5.**
The convergence comparison table shows that Milstein (variance only, without Levy area) achieves strong order 1 for the variance but only $\frac{1}{2}$ for the joint system. Explain why the variance benefits from the correction independently: the variance SDE is a scalar equation driven by $W^{(2)}$ alone, so no Levy area is needed for its Milstein scheme. The coupling to $W^{(1)}$ enters only through the joint system.

??? success "Solution to Exercise 5"
    The variance SDE is:

    $$
    dv_t = \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
    $$

    This is a **scalar** SDE driven by the single Brownian motion $W^{(2)}$. The Milstein scheme for a scalar SDE requires only the increment $\Delta W^{(2)}$ and the correction $\frac{1}{2}b(v)b'(v)[(\Delta W^{(2)})^2 - \Delta t]$. No iterated or cross integrals involving other Brownian motions are needed.

    The Levy area arises only in **multi-dimensional** systems where cross-diffusion terms couple different Brownian motions. In the Heston model, the coupling between $W^{(1)}$ and $W^{(2)}$ (through the correlation $\rho$) enters the joint simulation of $(x_t, v_t)$, not the variance equation alone.

    Specifically, the full 2D Milstein scheme for the joint system $(x, v)$ requires:

    - The double integral $\int_{t_n}^{t_{n+1}}\int_{t_n}^s dW_u^{(1)}\,dW_s^{(2)}$ for the cross-interaction between the diffusion of $x$ (driven by $W^{(1)}$) and the diffusion of $v$ (driven by $W^{(2)}$)
    - The reverse integral $\int_{t_n}^{t_{n+1}}\int_{t_n}^s dW_u^{(2)}\,dW_s^{(1)}$

    The Levy area $A_n$ is the antisymmetric part of these cross integrals. Without it, the joint system only achieves strong order $1/2$.

    However, the variance process viewed in isolation has strong order 1 under Milstein, and since the log-price equation is linear in $x$ (the diffusion $\sqrt{v}$ does not depend on $x$), improving the accuracy of $v$ directly benefits the accuracy of $x$ through the coupling. This is why applying Milstein to the variance alone (without the Levy area) still provides a practical improvement over pure Euler for the full system, even though the theoretical joint strong order remains $1/2$.

---

**Exercise 6.**
For weak convergence (option pricing), both Euler and Milstein achieve order 1. Explain why the Milstein correction provides little benefit for European option pricing: the weak error depends on the distribution of the terminal values, not on pathwise accuracy. In what setting would the improved strong convergence of Milstein be important? Consider path-dependent options like Asian options where the payoff depends on individual path values.

??? success "Solution to Exercise 6"
    **Weak convergence and European options:** Weak convergence measures the error in expected values of smooth test functions, which is exactly what matters for European option pricing:

    $$
    |\mathbb{E}[g(S_T^{\text{scheme}})] - \mathbb{E}[g(S_T^{\text{true}})]| = \mathcal{O}(\Delta t^p)
    $$

    where $p$ is the weak order. Both Euler and Milstein achieve $p = 1$ for the Heston model. The Milstein correction has zero expectation ($\mathbb{E}[\frac{\xi^2}{4}((\Delta W)^2 - \Delta t)] = 0$), so it does not improve the mean of the transition distribution---only its pathwise accuracy. For European options, where the price depends only on the terminal distribution $S_T$, the weak error is the relevant metric, and Milstein provides no systematic advantage.

    **When strong convergence matters:** Strong convergence measures pathwise accuracy:

    $$
    \left(\mathbb{E}[|Y_N - Y_T|^2]\right)^{1/2} = \mathcal{O}(\Delta t^q)
    $$

    This is important for **path-dependent options** where the payoff depends on the specific realization of the path, not just the terminal value. Examples include:

    - **Asian options:** The payoff depends on $\frac{1}{N}\sum_{k=1}^N S_{t_k}$, which is sensitive to the accuracy of each intermediate $S_{t_k}$. Pathwise errors in the variance process propagate to errors in the running average, and these errors do not cancel out through averaging across paths.
    - **Lookback options:** The payoff depends on $\max_{k} S_{t_k}$ or $\min_{k} S_{t_k}$, which is sensitive to individual path extremes.
    - **Barrier options:** Whether a path crosses the barrier depends on the precise path values, not their distribution.
    - **Hedging simulations:** Computing hedge ratios by finite differences of simulated payoffs requires pathwise accuracy, since the same Brownian draws are used for bumped and un-bumped scenarios.

    In all these cases, improving the strong convergence order from $1/2$ to $1$ (for the variance component) can materially reduce the simulation error, making the Milstein correction worthwhile despite its negligible effect on European option pricing.

---

**Exercise 7.**
Compare the cost-accuracy trade-off of Euler, Milstein, and QE for pricing a European call. Use $M = 100{,}000$ paths with $N = 252$ (daily) steps for Euler and Milstein, and $N = 12$ (monthly) steps for QE. The QE scheme has near-zero discretization bias with 12 steps, while Euler and Milstein have $O(\Delta t)$ weak bias. Estimate the total floating-point operations for each method (Euler/Milstein cost $\sim 10$ operations per step per path; QE costs $\sim 30$ operations per step per path) and the expected bias. Which method achieves the best accuracy per unit of computation?

??? success "Solution to Exercise 7"
    **Total floating-point operations:**

    | Method | Paths ($M$) | Steps ($N$) | Ops/step | Total ops |
    |--------|------------|------------|----------|-----------|
    | Euler | $100{,}000$ | $252$ | $10$ | $2.52 \times 10^8$ |
    | Milstein | $100{,}000$ | $252$ | $10$ | $2.52 \times 10^8$ |
    | QE | $100{,}000$ | $12$ | $30$ | $3.6 \times 10^7$ |

    Milstein costs essentially the same as Euler per step because the correction $\frac{\xi^2}{4}[(\Delta W)^2 - \Delta t]$ requires only 3--4 additional arithmetic operations (squaring $\Delta W$, subtracting $\Delta t$, multiplying by $\xi^2/4$, adding to the update), which is negligible compared to the random number generation and other operations.

    **Expected bias:** All three methods have weak order 1, but the constant differs:

    - **Euler (full truncation):** Bias $\approx \$0.05$ at $N = 252$. The bias comes from the truncation of negative variance, which systematically underestimates the variance.
    - **Milstein:** Bias $\approx \$0.04$ at $N = 252$. Slightly better than Euler because the correction reduces the frequency and severity of negative variance events, leading to less truncation.
    - **QE:** Bias $\approx \$0.01$ at $N = 12$. The moment-matching approach captures the CIR transition distribution far more accurately per step.

    **Accuracy per unit of computation:** Define efficiency as $1 / (\text{Bias}^2 \times \text{Total ops})$:

    | Method | Bias$^2$ | Total ops | Bias$^2 \times$ ops |
    |--------|---------|-----------|---------------------|
    | Euler | $0.0025$ | $2.52 \times 10^8$ | $6.3 \times 10^5$ |
    | Milstein | $0.0016$ | $2.52 \times 10^8$ | $4.0 \times 10^5$ |
    | QE | $0.0001$ | $3.6 \times 10^7$ | $3.6 \times 10^3$ |

    The QE scheme is approximately **$100$--$175$ times more efficient** than Euler or Milstein in terms of accuracy per floating-point operation. This enormous advantage comes from two sources: (1) QE requires far fewer steps ($12$ vs $252$) due to its superior per-step accuracy, and (2) the moment-matching approach produces negligible bias even with large time steps, while Euler and Milstein accumulate truncation-related bias over many small steps. Milstein offers a marginal improvement over Euler but cannot close the gap with QE. For European option pricing under the Heston model, the QE scheme is the clear winner in cost-accuracy trade-off.
