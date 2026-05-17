# American Options via PSOR

European options under Heston have semi-analytical prices through Fourier inversion, but **American options** require numerical methods because the early exercise boundary depends on both the stock price $S$ and the variance $v$. The early exercise feature transforms the PDE into a **linear complementarity problem (LCP)**: the option value must satisfy the PDE inequality while remaining above the intrinsic value at every point. **Projected successive over-relaxation (PSOR)** solves this LCP efficiently by combining iterative linear system solving with a projection onto the exercise constraint, integrating naturally with the ADI framework for the two-dimensional Heston PDE.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Formulate the American option pricing problem as a linear complementarity problem in two dimensions
    2. Derive the PSOR algorithm from projected Gauss-Seidel iteration
    3. Integrate PSOR with ADI time stepping for the Heston PDE
    4. Select the relaxation parameter and convergence tolerance

!!! tip "Prerequisites"
    This section builds on the [2D PDE formulation](two_dimensional_pde_formulation.md), [ADI schemes](adi_schemes.md), and [boundary conditions](boundary_conditions_for_variance.md).

---

## The Early Exercise Problem

Recall (see [§ Free-boundary problems](../../ch08/american_options/free_boundary_problems_american_options.md)) that an American option creates a free boundary separating exercise from continuation. Under Heston the boundary is a **surface** $S^*(t, v)$ in $(t, S, v)$ rather than a curve, because variance is an additional state variable. For an American put with $g(S) = (K - S)^+$:

- When $v$ is **small**, volatility is low and the put is less likely to move further in-the-money, so early exercise is more attractive and $S^*(t, v)$ is **higher**
- When $v$ is **large**, high volatility increases the option's time value, delaying exercise and pushing $S^*(t, v)$ **lower**

---

## Linear Complementarity Formulation

Recall (see [§ Linear complementarity formulation](../../ch08/american_options/linear_complementarity_formulation.md)) the LCP triple $V \geq g$, $\partial_t V + \mathcal{L}V - rV \leq 0$, $(V-g)(\partial_t V + \mathcal{L}V - rV)=0$. For Heston the only change is that the spatial operator is the 2D one, $\mathcal{L} = \mathcal{L}_x + \mathcal{L}_v + \mathcal{L}_{xv}$, with $g(e^x) = (K - e^x)^+$ for an American put. After time discretization the matrix LCP is $\mathbf{V}^{n+1} \geq \mathbf{g}$, $A\mathbf{V}^{n+1} \geq \mathbf{b}$, $(\mathbf{V}^{n+1} - \mathbf{g})^T (A\mathbf{V}^{n+1} - \mathbf{b}) = 0$.

---

## The PSOR Algorithm

### From Gauss-Seidel to PSOR

Recall (see [§ PSOR algorithm](../../ch08/american_options/psor_algorithm.md)) that PSOR combines an SOR update with a projection: $\tilde{V}_k^{(\ell+1)} = (1-\omega)V_k^{(\ell)} + (\omega/a_{kk})\bigl(b_k - \sum_{j<k} a_{kj}V_j^{(\ell+1)} - \sum_{j>k} a_{kj}V_j^{(\ell)}\bigr)$, then $V_k^{(\ell+1)} = \max(\tilde{V}_k^{(\ell+1)}, g_k)$, with $g_k = g(e^{x_k})$ and $\omega \in (0,2)$.

### Algorithm

For each time step, given $\mathbf{V}^n$ from the previous step:

1. **Form** the linear system $A\mathbf{V}^{n+1} = \mathbf{b}(\mathbf{V}^n)$
2. **Initialize** $\mathbf{V}^{(0)} = \mathbf{V}^n$ (warm start)
3. **Iterate** for $\ell = 0, 1, 2, \ldots$:
    - For $k = 1, 2, \ldots, N_x N_v$:
        - Compute $\tilde{V}_k^{(\ell+1)}$ using SOR
        - Project: $V_k^{(\ell+1)} = \max(\tilde{V}_k^{(\ell+1)}, g_k)$
4. **Stop** when $\|\mathbf{V}^{(\ell+1)} - \mathbf{V}^{(\ell)}\|_\infty < \epsilon$

!!! note "Convergence of PSOR"
    PSOR converges for any $\omega \in (0, 2)$ when the matrix $A$ is an M-matrix (diagonally dominant with non-positive off-diagonal entries), which is satisfied by standard finite difference discretizations on sufficiently fine grids. The convergence rate depends on $\omega$; the optimal choice is typically $\omega \in [1.2, 1.8]$.

---

## Integration with ADI

The PSOR algorithm can be combined with ADI time stepping in two ways:

### Approach 1: PSOR After Each ADI Step (Operator Splitting Approach)

The simplest approach applies the ADI scheme to advance the PDE solution one time step (ignoring the exercise constraint), then projects:

1. Compute $\hat{\mathbf{V}}^{n+1}$ using the ADI scheme (e.g., Hundsdorfer-Verwer)
2. Project: $V_{i,j}^{n+1} = \max(\hat{V}_{i,j}^{n+1}, g_{i,j})$ for all $(i, j)$

This is sometimes called the **penalty method** or **operator splitting** approach. It is simple but introduces a splitting error: the projection is applied only once per time step, not iteratively.

### Approach 2: PSOR Within Each ADI Sweep

A more accurate approach applies PSOR within each implicit directional sweep of the ADI scheme:

1. In the $x$-direction sweep, solve the tridiagonal system for each $v_j$ line using PSOR (project after each row update)
2. In the $v$-direction sweep, solve the tridiagonal system for each $x_i$ line using PSOR

This produces better results near the exercise boundary but requires more iterations per sweep.

### Practical Recommendation

Approach 1 (projection after each full ADI step) is the standard choice in practice. The splitting error is $\mathcal{O}(\Delta\tau)$, which is compatible with the ADI temporal accuracy. Approach 2 is used when higher accuracy near the free boundary is needed.

---

## Relaxation Parameter Selection

The convergence rate of PSOR depends on the relaxation parameter $\omega$:

| $\omega$ | Behavior |
|-----------|----------|
| $\omega = 1$ | Gauss-Seidel (no over-relaxation) |
| $1 < \omega < \omega^*$ | Under-relaxed, slow but stable |
| $\omega = \omega^*$ | Optimal, fastest convergence |
| $\omega^* < \omega < 2$ | Over-relaxed, may oscillate |
| $\omega \geq 2$ | Divergent |

For the Heston PDE discretization, the **optimal** $\omega^*$ depends on the spectral radius of the Jacobi iteration matrix, which changes with the grid size and the PDE coefficients. In practice:

- Start with $\omega = 1.5$ as a robust default
- For fine grids ($N_x > 200$), increase toward $\omega = 1.7$--$1.8$
- The sensitivity to $\omega$ is modest: any $\omega \in [1.2, 1.8]$ gives acceptable performance

The stopping tolerance $\epsilon$ should be set to $10^{-6}$ to $10^{-8}$ times the notional, ensuring the iteration error is well below the spatial discretization error.

---

## Early Exercise Boundary Extraction

After solving the American option on the grid, the early exercise boundary $S^*(t, v)$ can be extracted by scanning each time slice for the transition from the exercise region to the continuation region:

For each $v_j$ and time $t_n$, find the largest $x_i$ (for a put) such that:

$$
V_{i,j}^n = g(e^{x_i})
$$

The boundary in $S$-space is $S^*_j(t_n) = e^{x_i}$. This produces a surface $S^*(t, v)$ that shows how the exercise boundary varies with both time and variance.

---

## Worked Example

Consider an American put with:

| Parameter | Value |
|-----------|-------|
| $S_0$ | $\$100$ |
| $K$ | $\$100$ |
| $r$ | $0.05$ |
| $q$ | $0$ |
| $v_0$ | $0.04$ |
| $\kappa$ | $1.5$ |
| $\theta$ | $0.04$ |
| $\xi$ | $0.3$ |
| $\rho$ | $-0.7$ |
| $T$ | $1.0$ |

**Grid**: $N_x = 150$, $N_v = 75$, $N_t = 200$, $\omega = 1.5$, $\epsilon = 10^{-7}$.

??? example "American Put Pricing Results"
    | Method | Price | Early Exercise Premium |
    |--------|:-----:|:---------------------:|
    | European put (Fourier) | $\$5.52$ | --- |
    | American put (PSOR + HV ADI) | $\$5.94$ | $\$0.42$ |

    The early exercise premium of $\$0.42$ (approximately 7.6% of the European value) reflects the value of being able to exercise when the stock drops significantly.

    The exercise boundary at $v = v_0 = 0.04$: $S^*(0, 0.04) \approx \$82$ (exercise immediately if $S < \$82$ at $t=0$).

    At $v = 0.01$ (low vol): $S^*(0, 0.01) \approx \$88$ --- higher boundary because low vol reduces time value.

    At $v = 0.10$ (high vol): $S^*(0, 0.10) \approx \$72$ --- lower boundary because high vol increases time value.

    The PSOR iteration converges in 5--15 iterations per time step with $\omega = 1.5$.

---

## Summary

American options under the Heston model are priced by solving a two-dimensional linear complementarity problem that couples the Heston PDE with the early exercise constraint. The PSOR algorithm efficiently solves this LCP by combining SOR iteration with projection onto the intrinsic value bound. Integration with ADI schemes---either through post-step projection (operator splitting) or intra-sweep PSOR---produces accurate American option prices and the two-dimensional free boundary $S^*(t, v)$. The relaxation parameter $\omega \approx 1.5$ and tolerance $\epsilon \approx 10^{-7}$ are robust defaults. The resulting exercise boundary reveals how optimal exercise depends on both moneyness and the current variance level.

---

## Exercises

**Exercise 1.**
State the linear complementarity problem (LCP) for an American put under Heston: $V \geq g(S)$, $\mathcal{L}V \leq 0$, $(V - g)\mathcal{L}V = 0$, where $g(S) = (K - S)^+$ and $\mathcal{L}$ is the Heston PDE operator. Explain each condition in financial terms. Why can the problem not be solved by simply solving the PDE and then clamping the result?

??? success "Solution to Exercise 1"
    **LCP statement.** Let $g(S) = (K - S)^+$ be the intrinsic value of the American put, and let $\mathcal{L}$ denote the Heston spatial operator:

    $$
    \mathcal{L}V = \frac{v}{2}\frac{\partial^2 V}{\partial x^2} + \left(r - q - \frac{v}{2}\right)\frac{\partial V}{\partial x} + \frac{\xi^2 v}{2}\frac{\partial^2 V}{\partial v^2} + \kappa(\theta - v)\frac{\partial V}{\partial v} + \rho\xi v\frac{\partial^2 V}{\partial x \partial v} - rV
    $$

    The LCP consists of three conditions:

    **Condition 1** (Value bound): $V(t, x, v) \geq g(e^x)$ for all $(t, x, v)$. Financially, the holder can always exercise, so the option is worth at least its intrinsic value.

    **Condition 2** (PDE inequality): $\frac{\partial V}{\partial t} + \mathcal{L}V \leq 0$ for all $(t, x, v)$. Financially, the option cannot grow faster than the riskless rate---otherwise arbitrage would be possible.

    **Condition 3** (Complementarity): $(V - g) \cdot \left(\frac{\partial V}{\partial t} + \mathcal{L}V\right) = 0$ for all $(t, x, v)$. At every point, exactly one of the following holds:

    - $V = g$ (exercise region): the holder exercises, and the PDE inequality is strict
    - $V > g$ (continuation region): the holder waits, and the PDE equality holds exactly

    **Why clamping fails.** Simply solving the PDE and then applying $V \leftarrow \max(V, g)$ produces an incorrect answer because the early exercise constraint feeds back into the PDE solution itself. In the continuation region, the PDE must account for the fact that exercise will occur at the free boundary---the boundary condition at the free boundary $S^*(t, v)$ is $V = g(S^*)$ with smooth pasting $\partial V / \partial S = -1$ (for a put). A single clamp ignores this coupling: the PDE solution without the constraint will generally violate $V \geq g$ in a region, and the clamp introduces a discontinuity in the derivatives that propagates as $\mathcal{O}(\Delta\tau)$ error. The PSOR iteration correctly handles this by iteratively enforcing the constraint at every grid point until the complementarity condition is satisfied.

---

**Exercise 2.**
The early exercise boundary $S^*(t, v)$ for an American put under Heston depends on both time to maturity and the current variance. Explain qualitatively why higher variance $v$ leads to a lower exercise boundary (the put should be exercised less readily). Hint: higher variance increases the option's continuation value.

??? success "Solution to Exercise 2"
    **Higher variance raises continuation value.** The early exercise boundary $S^*(t, v)$ for a put is the stock price below which immediate exercise is optimal. The holder exercises when:

    $$
    \underbrace{K - S}_{\text{exercise value}} \geq \underbrace{V_{\text{cont}}(t, S, v)}_{\text{continuation value}}
    $$

    The continuation value depends on the expected future payoff, which increases with volatility because:

    1. **Higher $v$ increases the option's time value.** Variance is the "fuel" for the diffusion in the Heston model. When $v$ is large, the stock price has a wider distribution of future outcomes, making it more likely that the put will become even deeper in-the-money. The holder benefits from waiting.

    2. **Mean reversion amplifies the effect.** If the current $v$ is above $\theta$, mean reversion will pull $v$ down, but the stock still has a period of elevated volatility ahead. The option holder captures this through the continuation value.

    3. **Convexity of the payoff.** The put payoff $(K - S)^+$ is convex. By Jensen's inequality, higher variance in the future stock price distribution raises the expected payoff under continuation:

    $$
    \mathbb{E}[(K - S_T)^+] \geq (K - \mathbb{E}[S_T])^+
    $$

    with the gap increasing in the variance of $S_T$.

    Consequently, at higher $v$, the continuation value exceeds the intrinsic value over a wider range of stock prices, and early exercise becomes optimal only at lower stock prices. This means $S^*(t, v)$ is a **decreasing** function of $v$: the exercise boundary drops as variance increases.

    Numerically, for the parameters in the worked example: $S^*(0, 0.01) \approx \$88$ (low vol, exercise readily) versus $S^*(0, 0.10) \approx \$72$ (high vol, defer exercise).

---

**Exercise 3.**
The PSOR algorithm projects the SOR iterate onto the constraint set: $V_{i,j}^{(k+1)} = \max(V_{i,j}^{(k+1)}, g_{i,j})$. Explain why this projection is applied after each SOR update (not just at the end of the iteration). What happens if you only project at the end?

??? success "Solution to Exercise 3"
    **Why project after each update.** The PSOR algorithm updates the solution components sequentially (Gauss-Seidel style), and each update uses the most recently computed values of neighboring components. The projection $V_{i,j}^{(k+1)} = \max(\tilde{V}_{i,j}^{(k+1)}, g_{i,j})$ is applied immediately after updating each grid point.

    **Projection after each update is essential because:**

    1. **Information propagation.** When point $(i, j)$ is in the exercise region ($V_{i,j} = g_{i,j}$), this constraint immediately influences the update of neighboring points $(i+1, j)$, $(i, j+1)$, etc. If the projection is deferred, these neighbors are computed using an incorrect (too-low) value, and the exercise boundary is not accurately captured until the next full iteration.

    2. **Convergence guarantee.** The PSOR convergence proof relies on the iterates staying feasible ($V^{(k)} \geq g$) at every step. The immediate projection ensures that each intermediate iterate satisfies the constraint. Without this, intermediate iterates can violate $V \geq g$, and the iteration may converge to a solution of the linear system $AV = b$ rather than the LCP.

    3. **Free boundary sharpness.** The exercise boundary in the Heston model is a curve in $(x, v)$ space. The sequential projection accurately identifies which grid points are in the exercise region at each iteration. Deferring the projection to the end of a full sweep would produce a blurred boundary.

    **What happens with end-of-iteration projection only.** If one performs a full SOR sweep (without projection) and then clamps $V^{(k+1)} = \max(V^{(k+1)}, g)$:

    - The iteration effectively solves the unconstrained system $AV = b$ first, then projects. This is the "solve-then-clamp" approach, which produces $\mathcal{O}(\Delta\tau)$ errors near the free boundary.
    - Convergence is slower because the constraint information does not propagate within each sweep.
    - The method may require many more iterations to satisfy the complementarity condition to the desired tolerance, as each iteration only partially incorporates the exercise constraint.

---

**Exercise 4.**
The relaxation parameter $\omega$ in SOR controls convergence speed. For $\omega = 1$ (Gauss-Seidel), convergence is guaranteed but slow. For $\omega = 1.5$, convergence is faster. The optimal $\omega$ depends on the spectral radius of the iteration matrix. Describe a practical procedure to choose $\omega$ for the Heston PSOR: run a few time steps with $\omega = 1.0, 1.2, 1.4, 1.6, 1.8$ and count the iterations to convergence.

??? success "Solution to Exercise 4"
    **Practical procedure for choosing $\omega$.**

    **Step 1: Setup.** Select a representative set of Heston parameters and grid sizes. Use the first 5--10 time steps (not the full computation) since the convergence behavior is similar throughout.

    **Step 2: Test values.** Run the PSOR iteration for $\omega \in \{1.0, 1.2, 1.4, 1.6, 1.8\}$ with a tight convergence tolerance $\epsilon = 10^{-8}$. For each $\omega$ and each time step, record the number of iterations $n_{\text{iter}}(\omega)$ to reach $\|V^{(k+1)} - V^{(k)}\|_\infty < \epsilon$.

    **Step 3: Average and compare.** Compute the average iteration count over the tested time steps:

    $$
    \bar{n}(\omega) = \frac{1}{N_{\text{test}}} \sum_{n=1}^{N_{\text{test}}} n_{\text{iter}}^{(n)}(\omega)
    $$

    **Expected behavior:**

    | $\omega$ | Typical $\bar{n}$ | Behavior |
    |:--------:|:-----------------:|----------|
    | 1.0 | 30--50 | Gauss-Seidel, baseline |
    | 1.2 | 20--35 | Moderate improvement |
    | 1.4 | 12--25 | Good improvement |
    | 1.5 | 10--20 | Near-optimal for many grids |
    | 1.6 | 8--18 | Possibly optimal |
    | 1.8 | 10--30 | May oscillate, grid-dependent |

    **Step 4: Select.** Choose $\omega^*$ as the value minimizing $\bar{n}(\omega)$. In practice, $\omega^* \in [1.4, 1.7]$ for typical Heston grids.

    **Theoretical guidance.** For a model problem (Laplace equation on a uniform grid), the optimal SOR parameter is:

    $$
    \omega^* = \frac{2}{1 + \sqrt{1 - \rho_J^2}}
    $$

    where $\rho_J$ is the spectral radius of the Jacobi iteration matrix. For the Heston discretization, $\rho_J$ depends on the grid size, PDE coefficients, and the non-uniform grid stretching, making the empirical approach above more reliable than the formula. As the grid is refined ($N_x, N_v \to \infty$), $\rho_J \to 1$ and $\omega^* \to 2$, but in practice the grid sizes used (100--300 points per direction) give $\omega^* \approx 1.5$--$1.7$.

---

**Exercise 5.**
The American put premium (American price minus European price) under Heston depends on the Heston parameters. Explain how $v_0$ and $\kappa$ affect the premium. If $v_0$ is very high, is the American premium large or small relative to the European put price?

??? success "Solution to Exercise 5"
    **Effect of $v_0$ on the American premium.**

    The American put premium is defined as $P_{\text{Am}} - P_{\text{Eu}}$, the difference between the American and European put prices. This premium represents the value of the early exercise right.

    **Large $v_0$:** When initial variance is high, the option's continuation value is large (high volatility increases the expected payoff from waiting). This means:

    - The European put price $P_{\text{Eu}}$ is large because high volatility increases option value
    - The early exercise boundary $S^*(t, v_0)$ is low (the holder is less inclined to exercise because waiting is valuable)
    - The American premium $P_{\text{Am}} - P_{\text{Eu}}$ is **small relative to $P_{\text{Eu}}$**

    Intuitively, when volatility is very high, early exercise is rarely optimal because the time value of the option dominates. The American and European prices are close.

    **Small $v_0$:** When initial variance is low:

    - The European put has a lower price
    - The early exercise boundary is higher (exercise is attractive at more stock price levels)
    - The American premium is **larger relative to $P_{\text{Eu}}$**

    With low volatility, the put behaves more like its intrinsic value, and the interest earned on the strike payment from early exercise becomes significant relative to the small time value.

    **Effect of $\kappa$ (mean reversion speed).**

    - **Large $\kappa$:** Variance reverts quickly to $\theta$. If $v_0 > \theta$, high $\kappa$ means the elevated variance is transient, reducing continuation value and slightly increasing the premium. If $v_0 < \theta$, fast reversion to higher $\theta$ increases continuation value and reduces the premium.

    - **Small $\kappa$:** Variance stays near $v_0$ for longer. The premium is more sensitive to $v_0$ itself, and the exercise boundary is relatively stable over time.

    In summary: the American premium relative to the European price is an **increasing** function of the interest rate $r$ (which drives early exercise) and a **decreasing** function of $v_0$ (which increases continuation value).

---

**Exercise 6.**
Compute the early exercise boundary at $t = 0$ (i.e., right now) for an American put with $K = 100$, $T = 1$, $r = 5\%$, under Black-Scholes with $\sigma = 20\%$. The boundary satisfies $K - S^* = \text{Put}_{\text{BS}}(S^*, K, T, r, \sigma)$ approximately. Under Heston, explain why the boundary $S^*(v)$ is a curve in the $(S, v)$ plane rather than a single point.

??? success "Solution to Exercise 6"
    **Black-Scholes exercise boundary.** At $t = 0$ with $T = 1$ remaining, the exercise boundary $S^*$ satisfies the condition that the intrinsic value equals the European put value:

    $$
    K - S^* = P_{\text{BS}}(S^*, K, T, r, \sigma)
    $$

    Using the Black-Scholes put formula $P_{\text{BS}} = Ke^{-rT}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)$ with $K = 100$, $T = 1$, $r = 0.05$, $\sigma = 0.20$:

    $$
    100 - S^* = 100 e^{-0.05}\mathcal{N}(-d_2) - S^*\mathcal{N}(-d_1)
    $$

    where

    $$
    d_1 = \frac{\ln(S^*/100) + (0.05 + 0.02) \cdot 1}{0.20}, \quad d_2 = d_1 - 0.20
    $$

    This is a nonlinear equation in $S^*$ that must be solved numerically (e.g., by Newton's method or bisection). Starting from an initial guess $S^* = 80$:

    - At $S^* = 80$: $d_1 \approx \frac{-0.2231 + 0.07}{0.20} = -0.766$, $d_2 = -0.966$. Then $P_{\text{BS}} \approx 95.12 \times 0.833 - 80 \times 0.778 \approx 79.2 - 62.3 = 16.9$. Intrinsic $= 20$. Since $20 > 16.9$, exercise is optimal: $S^*$ is above 80.
    - At $S^* = 85$: $d_1 \approx \frac{-0.1625 + 0.07}{0.20} = -0.463$, $d_2 = -0.663$. Then $P_{\text{BS}} \approx 95.12 \times 0.746 - 85 \times 0.678 \approx 71.0 - 57.6 = 13.4$. Intrinsic $= 15$. Still exercise: $S^* > 85$.
    - Iterating further yields $S^* \approx \$81$--$\$83$ for these parameters.

    **Why Heston gives a curve, not a point.** Under Black-Scholes, the volatility $\sigma$ is a fixed constant. The exercise boundary at any time $t$ is a single number $S^*(t)$ because the model state is fully characterized by $(t, S)$.

    Under Heston, the model state is $(t, S, v)$---three-dimensional. The variance $v$ is a stochastic state variable that affects the option value. At each time $t$, the exercise boundary is a function $S^*(t, v)$:

    - For each value of $v$, there is a different critical stock price below which exercise is optimal
    - Higher $v$ means higher continuation value, so $S^*(t, v)$ is lower (exercise only at more deeply in-the-money levels)
    - Lower $v$ means lower continuation value, so $S^*(t, v)$ is higher

    The exercise boundary is therefore a **surface** $(t, S^*(t, v), v)$ in three-dimensional space, or equivalently, at each fixed time $t$, a **curve** $S^*(v)$ in the $(S, v)$ plane. This is a fundamental difference from one-factor models and is the reason the Heston American option problem requires a two-dimensional numerical solver.
