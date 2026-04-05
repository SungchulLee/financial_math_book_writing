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

??? success "Solution to Exercise 1"
    **Derivation of the Heston PDE.** Let $V(t, S, v)$ be the price of a European derivative with payoff $g(S_T)$ at maturity $T$. By the two-dimensional Ito lemma applied to the process $(S_t, v_t)$:

    $$
    dV = \frac{\partial V}{\partial t} dt + \frac{\partial V}{\partial S} dS + \frac{\partial V}{\partial v} dv + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}(dS)^2 + \frac{1}{2}\frac{\partial^2 V}{\partial v^2}(dv)^2 + \frac{\partial^2 V}{\partial S \partial v}(dS)(dv)
    $$

    Substituting the risk-neutral dynamics $dS = (r-q)S\,dt + \sqrt{v}S\,dW^{(1)}$ and $dv = \kappa(\theta - v)\,dt + \xi\sqrt{v}\,dW^{(2)}$:

    **Quadratic variations:**

    $$
    (dS)^2 = v S^2 \, dt
    $$

    $$
    (dv)^2 = \xi^2 v \, dt
    $$

    $$
    (dS)(dv) = \rho \xi v S \, dt
    $$

    where we used $dW^{(1)} dW^{(2)} = \rho \, dt$.

    **Collecting terms:**

    $$
    dV = \left[\frac{\partial V}{\partial t} + (r-q)S\frac{\partial V}{\partial S} + \kappa(\theta - v)\frac{\partial V}{\partial v} + \frac{1}{2}vS^2\frac{\partial^2 V}{\partial S^2} + \frac{1}{2}\xi^2 v\frac{\partial^2 V}{\partial v^2} + \rho\xi v S\frac{\partial^2 V}{\partial S \partial v}\right]dt + \text{martingale terms}
    $$

    The discounted price $e^{-rt}V$ must be a $\mathbb{Q}$-martingale (Feynman-Kac), so its drift is zero:

    $$
    \frac{\partial V}{\partial t} + (r-q)S\frac{\partial V}{\partial S} + \kappa(\theta - v)\frac{\partial V}{\partial v} + \frac{1}{2}vS^2\frac{\partial^2 V}{\partial S^2} + \frac{1}{2}\xi^2 v\frac{\partial^2 V}{\partial v^2} + \rho\xi v S\frac{\partial^2 V}{\partial S \partial v} - rV = 0
    $$

    **Financial interpretation of each term:**

    - $\partial V / \partial t$: time decay (theta)
    - $(r-q)S \, \partial V / \partial S$: drift of stock under risk-neutral measure (risk-free growth minus dividends)
    - $\kappa(\theta - v) \partial V / \partial v$: mean-reverting drift of variance toward $\theta$
    - $\frac{1}{2}vS^2 \, \partial^2 V / \partial S^2$: diffusion in stock direction (gamma effect, scaled by $v$)
    - $\frac{1}{2}\xi^2 v \, \partial^2 V / \partial v^2$: diffusion in variance direction (vol-of-vol effect)
    - $\rho\xi v S \, \partial^2 V / \partial S \partial v$: cross-diffusion from correlation (leverage effect)
    - $-rV$: discounting at the risk-free rate

---

**Exercise 2.**
Perform the log-price transformation $x = \ln S$ to convert the Heston PDE from $(S, v, t)$ to $(x, v, t)$ coordinates. Show that the $S^2 \partial^2 V / \partial S^2$ term becomes $\partial^2 V / \partial x^2$ (without a multiplicative coefficient), and the drift term gains a $-v/2$ correction.

??? success "Solution to Exercise 2"
    **Log-price transformation.** Let $x = \ln S$, so $S = e^x$. We need to express the derivatives with respect to $S$ in terms of derivatives with respect to $x$.

    **First derivative.** By the chain rule:

    $$
    \frac{\partial V}{\partial S} = \frac{\partial V}{\partial x} \cdot \frac{dx}{dS} = \frac{1}{S}\frac{\partial V}{\partial x}
    $$

    Therefore $S \frac{\partial V}{\partial S} = \frac{\partial V}{\partial x}$.

    **Second derivative.** Applying the chain rule again:

    $$
    \frac{\partial^2 V}{\partial S^2} = \frac{\partial}{\partial S}\left(\frac{1}{S}\frac{\partial V}{\partial x}\right) = -\frac{1}{S^2}\frac{\partial V}{\partial x} + \frac{1}{S} \cdot \frac{1}{S}\frac{\partial^2 V}{\partial x^2} = \frac{1}{S^2}\left(\frac{\partial^2 V}{\partial x^2} - \frac{\partial V}{\partial x}\right)
    $$

    Therefore $S^2 \frac{\partial^2 V}{\partial S^2} = \frac{\partial^2 V}{\partial x^2} - \frac{\partial V}{\partial x}$.

    **Mixed derivative.** Similarly:

    $$
    S\frac{\partial^2 V}{\partial S \partial v} = S \cdot \frac{\partial}{\partial v}\left(\frac{1}{S}\frac{\partial V}{\partial x}\right) = \frac{\partial^2 V}{\partial x \partial v}
    $$

    **Substituting into the Heston PDE:**

    $$
    \frac{\partial V}{\partial t} + (r-q)\frac{\partial V}{\partial x} + \kappa(\theta - v)\frac{\partial V}{\partial v} + \frac{v}{2}\left(\frac{\partial^2 V}{\partial x^2} - \frac{\partial V}{\partial x}\right) + \frac{\xi^2 v}{2}\frac{\partial^2 V}{\partial v^2} + \rho\xi v\frac{\partial^2 V}{\partial x \partial v} - rV = 0
    $$

    Combining the first-order $x$-terms:

    $$
    (r - q)\frac{\partial V}{\partial x} - \frac{v}{2}\frac{\partial V}{\partial x} = \left(r - q - \frac{v}{2}\right)\frac{\partial V}{\partial x}
    $$

    The final transformed PDE is:

    $$
    \frac{\partial V}{\partial t} + \left(r - q - \frac{v}{2}\right)\frac{\partial V}{\partial x} + \kappa(\theta - v)\frac{\partial V}{\partial v} + \frac{v}{2}\frac{\partial^2 V}{\partial x^2} + \frac{\xi^2 v}{2}\frac{\partial^2 V}{\partial v^2} + \rho\xi v\frac{\partial^2 V}{\partial x \partial v} - rV = 0
    $$

    As claimed, the $S^2 \partial^2 V / \partial S^2$ term becomes $\frac{v}{2}\partial^2 V / \partial x^2$ (with no $x$-dependent coefficient---just a factor of $v$), and the drift acquires the convexity correction $-v/2$, which is the familiar Ito correction from the log transformation.

---

**Exercise 3.**
The mixed derivative $\rho\xi v \partial^2 V / \partial x \partial v$ is discretized using the four-point stencil. Verify that this stencil is second-order accurate on a uniform grid by Taylor-expanding $V_{i\pm 1, j\pm 1}$ around $(x_i, v_j)$ and showing that the leading error term is $\mathcal{O}(\Delta x^2 + \Delta v^2)$.

??? success "Solution to Exercise 3"
    **Taylor expansion verification.** On a uniform grid with $\Delta x$ and $\Delta v$, the four-point stencil for the mixed derivative at $(x_i, v_j)$ is:

    $$
    \frac{\partial^2 V}{\partial x \partial v}\bigg|_{i,j} \approx \frac{V_{i+1,j+1} - V_{i+1,j-1} - V_{i-1,j+1} + V_{i-1,j-1}}{4\Delta x \, \Delta v}
    $$

    Taylor-expand each corner term around $(x_i, v_j)$:

    $$
    V_{i+1,j+1} = V + V_x \Delta x + V_v \Delta v + \frac{1}{2}V_{xx}\Delta x^2 + V_{xv}\Delta x\Delta v + \frac{1}{2}V_{vv}\Delta v^2 + \frac{1}{6}V_{xxx}\Delta x^3 + \frac{1}{2}V_{xxv}\Delta x^2\Delta v + \frac{1}{2}V_{xvv}\Delta x\Delta v^2 + \frac{1}{6}V_{vvv}\Delta v^3 + \cdots
    $$

    $$
    V_{i+1,j-1} = V + V_x \Delta x - V_v \Delta v + \frac{1}{2}V_{xx}\Delta x^2 - V_{xv}\Delta x\Delta v + \frac{1}{2}V_{vv}\Delta v^2 + \frac{1}{6}V_{xxx}\Delta x^3 - \frac{1}{2}V_{xxv}\Delta x^2\Delta v + \frac{1}{2}V_{xvv}\Delta x\Delta v^2 - \frac{1}{6}V_{vvv}\Delta v^3 + \cdots
    $$

    $$
    V_{i-1,j+1} = V - V_x \Delta x + V_v \Delta v + \frac{1}{2}V_{xx}\Delta x^2 - V_{xv}\Delta x\Delta v + \frac{1}{2}V_{vv}\Delta v^2 - \frac{1}{6}V_{xxx}\Delta x^3 + \frac{1}{2}V_{xxv}\Delta x^2\Delta v - \frac{1}{2}V_{xvv}\Delta x\Delta v^2 + \frac{1}{6}V_{vvv}\Delta v^3 + \cdots
    $$

    $$
    V_{i-1,j-1} = V - V_x \Delta x - V_v \Delta v + \frac{1}{2}V_{xx}\Delta x^2 + V_{xv}\Delta x\Delta v + \frac{1}{2}V_{vv}\Delta v^2 - \frac{1}{6}V_{xxx}\Delta x^3 - \frac{1}{2}V_{xxv}\Delta x^2\Delta v - \frac{1}{2}V_{xvv}\Delta x\Delta v^2 - \frac{1}{6}V_{vvv}\Delta v^3 + \cdots
    $$

    **Computing the numerator** $V_{i+1,j+1} - V_{i+1,j-1} - V_{i-1,j+1} + V_{i-1,j-1}$:

    The terms $V$, $V_x\Delta x$, $V_v\Delta v$, $\frac{1}{2}V_{xx}\Delta x^2$, $\frac{1}{2}V_{vv}\Delta v^2$ all cancel. What remains:

    $$
    = 4 V_{xv} \Delta x \Delta v + \frac{4}{6}V_{xxxv}\Delta x^3\Delta v + \frac{4}{6}V_{xvvv}\Delta x\Delta v^3 + \cdots
    $$

    (The odd-order pure terms like $V_{xxx}\Delta x^3$ also cancel by symmetry.)

    Dividing by $4\Delta x \Delta v$:

    $$
    \frac{V_{i+1,j+1} - V_{i+1,j-1} - V_{i-1,j+1} + V_{i-1,j-1}}{4\Delta x\Delta v} = V_{xv} + \frac{1}{6}V_{xxxv}\Delta x^2 + \frac{1}{6}V_{xvvv}\Delta v^2 + \cdots
    $$

    The leading error term is $\mathcal{O}(\Delta x^2 + \Delta v^2)$, confirming second-order accuracy.

---

**Exercise 4.**
The operator splitting $\mathcal{A} = \mathcal{A}_0 + \mathcal{A}_1 + \mathcal{A}_2$ distributes the kill term $-rV$ equally between $\mathcal{A}_1$ and $\mathcal{A}_2$. Why is this splitting preferred over placing the entire $-rV$ term in one operator? Hint: consider the eigenvalues of the discrete operators and the stability of the ADI scheme.

??? success "Solution to Exercise 4"
    **Why distribute the kill term $-rV$ between operators.** The operator splitting writes $\mathcal{A} = \mathcal{A}_0 + \mathcal{A}_1 + \mathcal{A}_2$ where $\mathcal{A}_0$ handles the cross-derivative and $\mathcal{A}_1$, $\mathcal{A}_2$ handle the $x$- and $v$-directions respectively. The kill term $-rV$ must be assigned to one or more of these operators.

    **Option 1: Place $-rV$ entirely in $\mathcal{A}_1$.**

    $$
    \mathcal{A}_1 = \frac{v}{2}\frac{\partial^2}{\partial x^2} + \left(r - q - \frac{v}{2}\right)\frac{\partial}{\partial x} - rI
    $$

    $$
    \mathcal{A}_2 = \frac{\xi^2 v}{2}\frac{\partial^2}{\partial v^2} + \kappa(\theta - v)\frac{\partial}{\partial v}
    $$

    **Option 2: Split $-rV$ equally, $-\frac{r}{2}V$ in each.**

    $$
    \mathcal{A}_1 = \frac{v}{2}\frac{\partial^2}{\partial x^2} + \left(r - q - \frac{v}{2}\right)\frac{\partial}{\partial x} - \frac{r}{2}I
    $$

    $$
    \mathcal{A}_2 = \frac{\xi^2 v}{2}\frac{\partial^2}{\partial v^2} + \kappa(\theta - v)\frac{\partial}{\partial v} - \frac{r}{2}I
    $$

    **Why Option 2 is preferred:**

    1. **Balanced eigenvalues.** The discrete matrices $A_1$ and $A_2$ should have eigenvalues of comparable magnitude for optimal ADI stability. The kill term $-rI$ shifts all eigenvalues by $-r$. Placing the entire shift in one operator makes that operator's eigenvalues more negative while leaving the other operator's eigenvalues near zero. This imbalance can cause the ADI splitting error to grow.

    2. **Stability of the implicit solves.** Each ADI stage solves $(I - \theta\Delta\tau A_k)Y = \text{RHS}$. The matrix $(I - \theta\Delta\tau A_k)$ is better conditioned when $A_k$ has eigenvalues of moderate magnitude. If $A_1$ carries the full $-rI$ term, the eigenvalues of $A_1$ are shifted significantly negative, potentially making the tridiagonal system closer to singular for certain parameter regimes.

    3. **Symmetry of the splitting error.** The ADI splitting introduces a temporal error proportional to $\Delta\tau^2 [A_1, A_2]$ (the commutator). When the operators are balanced (similar spectral properties), the commutator is smaller, and the splitting error is reduced.

    4. **Diagonal dominance.** Adding $-r/(2)$ to each diagonal ensures both tridiagonal matrices remain diagonally dominant (a sufficient condition for the Thomas algorithm to be stable and for PSOR convergence in the American case).

---

**Exercise 5.**
A non-uniform grid in $x$ uses a sinh transformation centered at $x_0 = \ln S_0$. With $c_1 = 4$ and $c_2 = 4$, compute the grid points $x_i$ for $i/N_x = 0, 0.25, 0.5, 0.75, 1.0$ with $N_x = 100$. What is the grid spacing $\Delta x$ at the center ($i/N_x = 0.5$) versus at the boundaries?

??? success "Solution to Exercise 5"
    **Sinh grid computation.** The sinh transformation centered at $x_0 = \ln S_0$ is:

    $$
    x_i = x_0 + c_1 \sinh\!\left(c_2\left(\frac{i}{N_x} - \frac{1}{2}\right)\right) / \sinh\!\left(\frac{c_2}{2}\right)
    $$

    where $c_1$ controls the domain half-width and $c_2$ controls the concentration. With $c_1 = 4$ (so the domain is $[x_0 - 4, x_0 + 4]$) and $c_2 = 4$:

    Let $\eta = i/N_x$ and define $f(\eta) = \sinh(c_2(\eta - 1/2)) / \sinh(c_2/2)$. Then $x_i = x_0 + c_1 f(\eta_i)$.

    Precompute $\sinh(c_2/2) = \sinh(2) \approx 3.6269$.

    **At $\eta = 0$:** $f(0) = \sinh(-2)/\sinh(2) = -1$, so $x = x_0 - 4$.

    **At $\eta = 0.25$:** $f(0.25) = \sinh(4 \cdot (-0.25))/3.6269 = \sinh(-1)/3.6269 = -1.1752/3.6269 \approx -0.3241$, so $x = x_0 - 1.2963$.

    **At $\eta = 0.5$:** $f(0.5) = \sinh(0)/3.6269 = 0$, so $x = x_0$.

    **At $\eta = 0.75$:** $f(0.75) = \sinh(1)/3.6269 \approx 1.1752/3.6269 \approx 0.3241$, so $x = x_0 + 1.2963$.

    **At $\eta = 1$:** $f(1) = \sinh(2)/3.6269 = 1$, so $x = x_0 + 4$.

    **Grid spacing at the center ($\eta = 0.5$).** Differentiating:

    $$
    \frac{dx}{d\eta} = c_1 \cdot \frac{c_2 \cosh(c_2(\eta - 1/2))}{\sinh(c_2/2)}
    $$

    At $\eta = 0.5$: $\cosh(0) = 1$, so

    $$
    \frac{dx}{d\eta}\bigg|_{\eta=0.5} = \frac{4 \times 4 \times 1}{3.6269} \approx 4.411
    $$

    The local grid spacing at the center is:

    $$
    \Delta x_{\text{center}} \approx \frac{dx}{d\eta} \cdot \frac{1}{N_x} = \frac{4.411}{100} \approx 0.0441
    $$

    **Grid spacing at the boundary ($\eta = 0$ or $\eta = 1$).** At $\eta = 1$: $\cosh(c_2/2) = \cosh(2) \approx 3.7622$, so

    $$
    \frac{dx}{d\eta}\bigg|_{\eta=1} = \frac{4 \times 4 \times 3.7622}{3.6269} \approx 16.597
    $$

    $$
    \Delta x_{\text{boundary}} \approx \frac{16.597}{100} \approx 0.166
    $$

    **Concentration ratio:** $\Delta x_{\text{boundary}} / \Delta x_{\text{center}} \approx 0.166 / 0.0441 \approx 3.76$. The grid is about 3.8 times coarser at the boundaries than at the center, which is the desired concentration near the strike.

---

**Exercise 6.**
If $\rho = 0$, the mixed derivative vanishes and the Heston PDE fully decouples into two independent 1D problems. Is this exactly true? Explain why even with $\rho = 0$, the variance process still affects the stock price through the $\frac{1}{2}v\partial^2 V/\partial x^2$ term, so the two directions are not truly independent. What is the role of the mixed derivative in coupling the directions?

??? success "Solution to Exercise 6"
    **The PDE does not decouple when $\rho = 0$.** Setting $\rho = 0$ in the transformed Heston PDE eliminates only the mixed derivative term:

    $$
    \frac{\partial V}{\partial t} + \underbrace{\left(r - q - \frac{v}{2}\right)\frac{\partial V}{\partial x} + \frac{v}{2}\frac{\partial^2 V}{\partial x^2}}_{\mathcal{L}_x \text{ (depends on } v\text{)}} + \underbrace{\kappa(\theta - v)\frac{\partial V}{\partial v} + \frac{\xi^2 v}{2}\frac{\partial^2 V}{\partial v^2}}_{\mathcal{L}_v \text{ (depends on } v \text{ only)}} - rV = 0
    $$

    The operator $\mathcal{L}_x$ contains $v$ as a coefficient: the diffusion coefficient $v/2$ and the drift coefficient $(r - q - v/2)$ both depend on $v$. This means the $x$-direction operator changes at every variance level $v_j$, so the $x$- and $v$-directions are coupled through the **state-dependent coefficients**, not through the mixed derivative.

    **Why the directions are not independent.** For the PDE to decompose into two independent 1D problems, one would need $V(t, x, v) = f(t, x) \cdot g(t, v)$ (separation of variables). Substituting this product form:

    $$
    f_t g + g_t f + \left(r - q - \frac{v}{2}\right)f_x g + \frac{v}{2}f_{xx} g + \kappa(\theta - v) f g_v + \frac{\xi^2 v}{2} f g_{vv} - r f g = 0
    $$

    Dividing by $fg$:

    $$
    \frac{f_t}{f} + \frac{g_t}{g} + \left(r - q - \frac{v}{2}\right)\frac{f_x}{f} + \frac{v}{2}\frac{f_{xx}}{f} + \kappa(\theta - v)\frac{g_v}{g} + \frac{\xi^2 v}{2}\frac{g_{vv}}{g} - r = 0
    $$

    The terms $\frac{v}{2}\frac{f_{xx}}{f}$ and $-\frac{v}{2}\frac{f_x}{f}$ mix $v$ with functions of $x$ alone, so no separation into "$x$-only" and "$v$-only" parts is possible. The equation cannot be split into the sum of a function of $x$ alone and a function of $v$ alone.

    **The role of the mixed derivative.** The mixed derivative $\rho\xi v \, \partial^2 V / \partial x \partial v$ introduces an additional, qualitatively different type of coupling: it creates a **direct interaction** between the gradients in $x$ and $v$. Specifically:

    1. **Without the mixed derivative** ($\rho = 0$): the directions are coupled only through the coefficients. The $x$-diffusion depends on $v$, but the $v$-diffusion does not depend on $x$. This is a "one-way" coupling: variance affects stock dynamics, but not vice versa.

    2. **With the mixed derivative** ($\rho \neq 0$): the coupling is "two-way." A change in $V$ along the $x$-direction instantaneously affects the $v$-direction and vice versa, through the $V_{xv}$ term. This is what produces the leverage effect and the skew in implied volatility.

    In the finite difference context, the practical consequence is that even when $\rho = 0$, the ADI scheme must still solve the $x$-direction sweep with $v$-dependent coefficients (a different tridiagonal system for each $v_j$). The mixed derivative's absence simply means the ADI splitting is exact (no splitting error from the cross-term), improving accuracy without simplifying the computational structure.
