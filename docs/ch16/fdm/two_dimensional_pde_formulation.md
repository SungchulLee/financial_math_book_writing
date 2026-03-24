# Two-Dimensional PDE Formulation

Fourier methods price European options efficiently but cannot easily handle American exercise, path-dependent barriers with discrete monitoring, or general payoff nonlinearities. **Finite difference methods (FDM)** solve the Heston PDE directly on a two-dimensional grid in $(S, v)$ or $(\ln S, v)$ space, providing a flexible framework for pricing any derivative whose value depends on the current stock price and variance. The key challenge compared to the one-dimensional Black-Scholes PDE is the **mixed derivative** term $\rho \xi v S \, \partial^2 V / \partial S \partial v$, which couples the stock and variance directions and requires specialized discretization.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the Heston PDE from the risk-neutral dynamics using Ito's lemma
    2. Identify the role of the mixed derivative term arising from correlation
    3. Transform the PDE to log-price coordinates for improved numerical behavior
    4. Construct non-uniform grids and discretize all differential operators including the cross-derivative

!!! tip "Prerequisites"
    This section requires the [Heston SDE](../model_definition/heston_sde_and_parameters.md) and the [Feynman-Kac connection](../../ch05/feynman_kac/feynman_kac_option_pricing.md). The [boundary conditions](boundary_conditions_for_variance.md) and [ADI schemes](adi_schemes.md) build on the PDE formulation developed here.

---

## Deriving the Heston PDE

Under the risk-neutral measure $\mathbb{Q}$, the joint dynamics of the stock price and variance are:

$$
dS_t = (r - q) S_t \, dt + \sqrt{v_t} \, S_t \, dW_t^{(1)}
$$

$$
dv_t = \kappa(\theta - v_t) \, dt + \xi \sqrt{v_t} \, dW_t^{(2)}
$$

with $d\langle W^{(1)}, W^{(2)} \rangle_t = \rho \, dt$.

Let $V(t, S, v)$ denote the price of a European derivative. By the Feynman-Kac theorem, $V$ satisfies a PDE obtained by applying Ito's formula to $V(t, S_t, v_t)$ and requiring that the discounted price process $e^{-rt}V$ be a martingale.

Applying the two-dimensional Ito's lemma:

$$
dV = \frac{\partial V}{\partial t} dt + \frac{\partial V}{\partial S} dS + \frac{\partial V}{\partial v} dv + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}(dS)^2 + \frac{1}{2}\frac{\partial^2 V}{\partial v^2}(dv)^2 + \frac{\partial^2 V}{\partial S \partial v}(dS)(dv)
$$

Computing the quadratic variations:

$$
(dS)^2 = v S^2 \, dt, \qquad (dv)^2 = \xi^2 v \, dt, \qquad (dS)(dv) = \rho \xi v S \, dt
$$

Setting the drift of $e^{-rt}V$ to zero (martingale condition) yields the **Heston PDE**:

$$
\frac{\partial V}{\partial t} + (r-q)S\frac{\partial V}{\partial S} + \kappa(\theta - v)\frac{\partial V}{\partial v} + \frac{1}{2}vS^2\frac{\partial^2 V}{\partial S^2} + \frac{1}{2}\xi^2 v\frac{\partial^2 V}{\partial v^2} + \rho\xi v S\frac{\partial^2 V}{\partial S \partial v} - rV = 0
$$

with terminal condition $V(T, S, v) = g(S)$.

!!! note "The Mixed Derivative Term"
    The term $\rho\xi v S \, \partial^2 V / \partial S \partial v$ is absent in the Black-Scholes PDE and arises solely from the correlation between stock returns and variance innovations. When $\rho = 0$, the Heston PDE separates into independent $S$ and $v$ directions. When $\rho \neq 0$ (typically $\rho \approx -0.7$ for equities), this coupling term is significant and requires careful numerical treatment.

---

## Log-Price Transformation

The Heston PDE in $(S, v)$ has variable coefficients that depend on $S$ (through $S\partial_S$ and $S^2\partial_{SS}$). The substitution $x = \ln S$ simplifies the PDE by removing the $S$-dependence from the diffusion terms.

Under $x = \ln S$, the derivatives transform as:

$$
S\frac{\partial V}{\partial S} = \frac{\partial V}{\partial x}, \qquad S^2\frac{\partial^2 V}{\partial S^2} = \frac{\partial^2 V}{\partial x^2} - \frac{\partial V}{\partial x}
$$

The transformed PDE in $(t, x, v)$ is:

$$
\frac{\partial V}{\partial t} + \left(r - q - \frac{v}{2}\right)\frac{\partial V}{\partial x} + \kappa(\theta - v)\frac{\partial V}{\partial v} + \frac{v}{2}\frac{\partial^2 V}{\partial x^2} + \frac{\xi^2 v}{2}\frac{\partial^2 V}{\partial v^2} + \rho\xi v\frac{\partial^2 V}{\partial x \partial v} - rV = 0
$$

This formulation has two advantages:

1. The diffusion coefficients $v/2$ and $\xi^2 v/2$ do not depend on $x$, simplifying the finite difference stencil
2. The computational domain in $x$ is naturally symmetric around $\ln S_0$, allowing efficient grid placement

---

## Grid Construction

### Computational Domain

The PDE is solved on a bounded rectangular domain:

$$
(x, v) \in [x_{\min}, x_{\max}] \times [0, v_{\max}]
$$

Typical choices:

- $x_{\min} = \ln S_0 - L\sqrt{v_0 T}$ and $x_{\max} = \ln S_0 + L\sqrt{v_0 T}$ with $L \approx 6$--$8$
- $v_{\max} \approx 5\theta$ to $10\theta$, large enough that the solution is insensitive to the upper boundary

### Non-Uniform Grid

Accuracy concentrates where the option value changes most rapidly: near the strike $x \approx \ln K$ and near the current variance $v \approx v_0$. A **sinh-based** stretching provides smooth non-uniform spacing:

$$
x_i = \ln K + c_x \sinh\!\left(\frac{i - i_0}{d_x}\right), \qquad i = 0, 1, \ldots, N_x
$$

where $i_0$ is the index closest to $\ln K$, and $c_x, d_x$ control the concentration. Similarly for the variance direction:

$$
v_j = c_v \sinh\!\left(\frac{j}{d_v}\right), \qquad j = 0, 1, \ldots, N_v
$$

This automatically places $v_0 = 0$ on the grid and concentrates points near $v = 0$ where the PDE degenerates.

---

## Finite Difference Discretization

### Second-Order Central Differences

On a non-uniform grid with spacings $h_i^+ = x_{i+1} - x_i$ and $h_i^- = x_i - x_{i-1}$:

**First derivative:**

$$
\frac{\partial V}{\partial x}\bigg|_i \approx \frac{h_i^-}{h_i^+(h_i^+ + h_i^-)} V_{i+1} + \frac{h_i^+ - h_i^-}{h_i^+ h_i^-} V_i - \frac{h_i^+}{h_i^-(h_i^+ + h_i^-)} V_{i-1}
$$

**Second derivative:**

$$
\frac{\partial^2 V}{\partial x^2}\bigg|_i \approx \frac{2}{h_i^+(h_i^+ + h_i^-)} V_{i+1} - \frac{2}{h_i^+ h_i^-} V_i + \frac{2}{h_i^-(h_i^+ + h_i^-)} V_{i-1}
$$

### The Mixed Derivative

The cross-derivative $\partial^2 V / \partial x \partial v$ at grid point $(i, j)$ uses a **seven-point stencil**:

$$
\frac{\partial^2 V}{\partial x \partial v}\bigg|_{i,j} \approx \frac{1}{(h_i^+ + h_i^-)(k_j^+ + k_j^-)}\left(V_{i+1,j+1} - V_{i+1,j-1} - V_{i-1,j+1} + V_{i-1,j-1}\right)
$$

where $k_j^+ = v_{j+1} - v_j$ and $k_j^- = v_j - v_{j-1}$.

!!! warning "Non-Positive-Definite Stencil"
    The standard central difference for the mixed derivative can produce negative coefficients in the finite difference operator, potentially causing oscillations. When $|\rho|$ is large, an upwind-biased discretization of the mixed derivative may be necessary to maintain stability. Alternatively, ADI schemes treat the mixed derivative explicitly, sidestepping this issue.

---

## Operator Splitting Form

Writing the spatial operator as $\mathcal{L} = \mathcal{L}_x + \mathcal{L}_v + \mathcal{L}_{xv}$:

$$
\mathcal{L}_x V = \frac{v}{2}\frac{\partial^2 V}{\partial x^2} + \left(r - q - \frac{v}{2}\right)\frac{\partial V}{\partial x}
$$

$$
\mathcal{L}_v V = \frac{\xi^2 v}{2}\frac{\partial^2 V}{\partial v^2} + \kappa(\theta - v)\frac{\partial V}{\partial v}
$$

$$
\mathcal{L}_{xv} V = \rho\xi v\frac{\partial^2 V}{\partial x \partial v}
$$

The semi-discrete system in time is:

$$
\frac{\partial V}{\partial t} + (\mathcal{L}_x + \mathcal{L}_v + \mathcal{L}_{xv})V - rV = 0
$$

This splitting is the starting point for **ADI (alternating direction implicit) schemes**, which solve each directional operator implicitly in sequence. The mixed derivative operator $\mathcal{L}_{xv}$ is typically treated explicitly to preserve the tridiagonal structure of each directional solve.

---

## Worked Example: Grid for an ATM Call

Consider pricing a European call with $S_0 = \$100$, $K = \$100$, $T = 1$, $v_0 = 0.04$, $\theta = 0.04$.

**Domain:**

- $x_{\min} = \ln 100 - 6\sqrt{0.04} = 4.605 - 1.2 = 3.405$ (corresponding to $S \approx \$30$)
- $x_{\max} = \ln 100 + 6\sqrt{0.04} = 4.605 + 1.2 = 5.805$ (corresponding to $S \approx \$331$)
- $v_{\max} = 5 \times 0.04 = 0.20$

**Grid sizes:** $N_x = 100$, $N_v = 50$, $N_t = 100$, giving a total of 5,000 spatial grid points per time step.

??? example "Grid Point Distribution"
    With sinh-based stretching:

    - Approximately 40% of the $x$-grid points fall within $[4.2, 5.0]$ (the region $S \in [\$67, \$148]$ containing the strike)
    - Approximately 50% of the $v$-grid points fall within $[0, 0.06]$ (near the initial and long-run variance)
    - The finest $x$-spacing near $\ln K = 4.605$ is approximately $0.01$ (versus $0.024$ for a uniform grid)

    This concentration reduces the total grid size needed for a given accuracy by a factor of 3--5 compared to a uniform grid.

---

## Summary

The Heston PDE is a two-dimensional parabolic equation in $(x, v, t)$ with a mixed derivative coupling the stock and variance directions through correlation $\rho$. The log-price transformation simplifies the coefficients, and non-uniform grids concentrate resolution near the strike and current variance. The spatial operator splits naturally into $x$-direction, $v$-direction, and cross-derivative components, setting the stage for [ADI schemes](adi_schemes.md) that solve each direction implicitly. Proper treatment of the mixed derivative---either through a seven-point central stencil or explicit treatment in the ADI framework---is essential for accuracy and stability.

---

## Exercises

**Exercise 1.**
Starting from the Heston dynamics $dS = (r-q)Sdt + \sqrt{v}SdW^{(1)}$ and $dv = \kappa(\theta - v)dt + \xi\sqrt{v}dW^{(2)}$, derive the Heston PDE for $V(S, v, t)$ using Ito's lemma applied to the two-dimensional process $(S_t, v_t)$. Identify each term in the PDE and its financial interpretation.

---

**Exercise 2.**
Perform the log-price transformation $x = \ln S$ to convert the Heston PDE from $(S, v, t)$ to $(x, v, t)$ coordinates. Show that the $S^2 \partial^2 V / \partial S^2$ term becomes $\partial^2 V / \partial x^2$ (without a multiplicative coefficient), and the drift term gains a $-v/2$ correction.

---

**Exercise 3.**
The mixed derivative $\rho\xi v \partial^2 V / \partial x \partial v$ is discretized using the four-point stencil. Verify that this stencil is second-order accurate on a uniform grid by Taylor-expanding $V_{i\pm 1, j\pm 1}$ around $(x_i, v_j)$ and showing that the leading error term is $\mathcal{O}(\Delta x^2 + \Delta v^2)$.

---

**Exercise 4.**
The operator splitting $\mathcal{A} = \mathcal{A}_0 + \mathcal{A}_1 + \mathcal{A}_2$ distributes the kill term $-rV$ equally between $\mathcal{A}_1$ and $\mathcal{A}_2$. Why is this splitting preferred over placing the entire $-rV$ term in one operator? Hint: consider the eigenvalues of the discrete operators and the stability of the ADI scheme.

---

**Exercise 5.**
A non-uniform grid in $x$ uses a sinh transformation centered at $x_0 = \ln S_0$. With $c_1 = 4$ and $c_2 = 4$, compute the grid points $x_i$ for $i/N_x = 0, 0.25, 0.5, 0.75, 1.0$ with $N_x = 100$. What is the grid spacing $\Delta x$ at the center ($i/N_x = 0.5$) versus at the boundaries?

---

**Exercise 6.**
If $\rho = 0$, the mixed derivative vanishes and the Heston PDE fully decouples into two independent 1D problems. Is this exactly true? Explain why even with $\rho = 0$, the variance process still affects the stock price through the $\frac{1}{2}v\partial^2 V/\partial x^2$ term, so the two directions are not truly independent. What is the role of the mixed derivative in coupling the directions?
