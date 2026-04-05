# Penalty and Finite Difference Methods

## Introduction

When pricing American options via finite difference methods, the early-exercise constraint transforms the Black–Scholes PDE into a **variational inequality**. Two main approaches enforce this constraint numerically: the **projection method** (applied after each time step) and the **penalty method** (which embeds the constraint into the PDE itself).

This section focuses on penalty methods and their integration with standard finite difference schemes (explicit, implicit, Crank–Nicolson), as well as the **Projected Successive Over-Relaxation (PSOR)** algorithm for solving the resulting linear complementarity problem.

!!! info "Prerequisites"
    - [Finite Difference Methods](../../ch08/fdm/finite_difference_methods.md) (FDM basics)
    - [Free Boundary Problems](../../ch08/american_options/free_boundary_problems_american_options.md) (variational inequality)
    - [American Options Implementation](../../ch08/american_options/american_options_early_exercise_implementation.md) (projection approach)

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Formulate the penalty method for American option PDEs
    2. Implement PSOR for solving the linear complementarity problem
    3. Compare projection, penalty, and PSOR approaches
    4. Analyze the accuracy–efficiency trade-offs

---

## The Variational Inequality

The American option price satisfies:

$$
\max\left(\frac{\partial V}{\partial t} + \mathcal{L}V - rV, \; \Phi(S) - V\right) = 0
$$

where $\mathcal{L}V = \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S$ and $\Phi$ is the payoff function.

Equivalently, at each time step the discrete solution must satisfy:

$$
\begin{aligned}
L\mathbf{u} &\geq \mathbf{f} \\
\mathbf{u} &\geq \boldsymbol{\Phi} \\
(L\mathbf{u} - \mathbf{f})^T (\mathbf{u} - \boldsymbol{\Phi}) &= 0
\end{aligned}
$$

This is the **linear complementarity problem (LCP)**.

---

## Penalty Methods

### Core Idea

Instead of enforcing the constraint $V \geq \Phi$ exactly, add a **penalty term** that becomes large when the constraint is violated:

$$
\boxed{
\frac{\partial V}{\partial t} + \mathcal{L}V - rV + \lambda \max(\Phi(S) - V, 0) = 0
}
$$

where $\lambda \gg 1$ is the **penalty parameter**.

### How It Works

- When $V > \Phi$: the penalty term is zero, and the standard Black–Scholes PDE holds
- When $V < \Phi$: the penalty term $\lambda(\Phi - V)$ is large and positive, pushing $V$ back up toward $\Phi$
- As $\lambda \to \infty$: the penalized solution converges to the true American option price

### Discrete Formulation

After discretization with an implicit or Crank–Nicolson scheme, the system at each time step becomes:

$$
(L + \lambda P)\mathbf{u}^{n+1} = \mathbf{f} + \lambda P\boldsymbol{\Phi}
$$

where $P = \operatorname{diag}(p_1, \ldots, p_M)$ with:

$$
p_j = \begin{cases}
1 & \text{if } u_j^{n+1} < \Phi_j \\
0 & \text{otherwise}
\end{cases}
$$

Since $P$ depends on the solution, the system is **nonlinear** and requires iteration.

### Iterative Solution

```
Initialize: u⁰ = previous time step solution
For k = 0, 1, 2, ... until convergence:
    1. Compute P^k from u^k (identify violated constraints)
    2. Solve (L + λP^k) u^{k+1} = f + λP^k Φ
    3. Check convergence: ||u^{k+1} - u^k|| < ε
```

### Choice of λ

| $\lambda$ | Behavior |
|---|---|
| Too small ($10^2$–$10^4$) | Poor approximation, $V$ can dip below $\Phi$ |
| Moderate ($10^6$–$10^8$) | Good accuracy, well-conditioned |
| Too large ($> 10^{10}$) | Accurate but ill-conditioned, slow convergence |

!!! tip "Practical Guideline"
    $\lambda = 10^6$ to $10^8$ typically provides a good balance between accuracy ($O(1/\lambda)$ error from penalty approximation) and numerical conditioning.

---

## Projected Successive Over-Relaxation (PSOR)

### Motivation

PSOR directly solves the LCP without introducing a penalty approximation. It combines the **SOR iterative method** for linear systems with a **projection step** to enforce the constraint.

### Algorithm

At each time step, solve the LCP: $L\mathbf{u} \geq \mathbf{f}$, $\mathbf{u} \geq \boldsymbol{\Phi}$, complementarity.

For iteration $k+1$:

$$
\boxed{
\begin{aligned}
\tilde{u}_j^{(k+1)} &= (1 - \omega) u_j^{(k)} + \frac{\omega}{l_{jj}} \left(f_j - \sum_{i < j} l_{ji} u_i^{(k+1)} - \sum_{i > j} l_{ji} u_i^{(k)}\right) \\[6pt]
u_j^{(k+1)} &= \max\left(\tilde{u}_j^{(k+1)}, \; \Phi_j\right)
\end{aligned}
}
$$

The first line is the standard SOR update; the second is the **projection** onto the constraint.

### Parameters

- **Relaxation parameter** $\omega \in (1, 2)$: over-relaxation accelerates convergence. Typically $\omega \approx 1.2$–$1.5$.
- **Convergence criterion**: $\|\mathbf{u}^{(k+1)} - \mathbf{u}^{(k)}\|_\infty < \varepsilon$

### Convergence Properties

| Property | PSOR |
|---|---|
| Convergence type | Linear |
| Iterations per time step | 5–20 (typical) |
| Total cost | $O(MN \times \text{iterations})$ |
| Accuracy | Exact LCP solution (no penalty error) |

---

## Python Implementation: Penalty Method

```python
import numpy as np

def american_put_penalty(S_max, K, T, r, sigma, M, N, lam=1e7):
    """
    American put via Crank-Nicolson with penalty method.

    Parameters
    ----------
    S_max : float — Maximum stock price on grid
    K : float — Strike price
    T : float — Maturity
    r, sigma : float — Risk-free rate, volatility
    M : int — Number of spatial grid points
    N : int — Number of time steps
    lam : float — Penalty parameter

    Returns
    -------
    S : array — Stock price grid
    V : array — Option values
    """
    dS = S_max / M
    dt = T / N
    S = np.linspace(0, S_max, M + 1)
    payoff = np.maximum(K - S, 0)

    V = payoff.copy()

    for n in range(N):
        V_old = V.copy()

        # Iterate penalty
        for _ in range(50):  # max penalty iterations
            V_prev = V.copy()

            for i in range(1, M):
                Si = i * dS
                a = 0.5 * dt * (sigma**2 * Si**2 / dS**2 - r * Si / dS)
                b = 1 + dt * (sigma**2 * Si**2 / dS**2 + r)
                c = 0.5 * dt * (sigma**2 * Si**2 / dS**2 + r * Si / dS)

                # Penalty indicator
                penalty = lam * dt if V[i] < payoff[i] else 0.0

                rhs = V_old[i] + a * (V[i-1] - V_old[i-1]) + c * (V[i+1] - V_old[i+1])
                rhs += penalty * payoff[i]

                V[i] = rhs / (b + penalty)

            # Boundary conditions
            V[0] = K * np.exp(-r * (n + 1) * dt)
            V[M] = 0

            if np.max(np.abs(V - V_prev)) < 1e-10:
                break

    return S, V
```

---

## Comparison of Methods

| Method | Accuracy | Implementation | Conditioning | Free Boundary |
|---|---|---|---|---|
| **Projection** | First-order near boundary | Very simple | Good | Approximate |
| **PSOR** | Exact LCP solution | Moderate | Good | Exact |
| **Penalty** | $O(1/\lambda)$ error | Simple | Degrades with large $\lambda$ | Approximate |

### When to Use Each

!!! tip "Method Selection Guide"
    - **Projection**: Quick prototyping, educational implementations
    - **PSOR**: Production-quality pricing where accuracy matters
    - **Penalty**: When integrating with existing PDE solvers; good for nonlinear extensions

---

## Advanced: Penalty Method Convergence Theory

The penalized solution $V^\lambda$ satisfies:

$$
\|V^\lambda - V\|_\infty \leq \frac{C}{\lambda}
$$

where $C$ depends on the PDE coefficients and the payoff. Combined with the finite difference discretization error:

$$
\|V^\lambda_{h,\Delta t} - V\|_\infty \leq C_1 h^2 + C_2 \Delta t^p + \frac{C_3}{\lambda}
$$

where $p = 1$ for implicit and $p = 2$ for Crank–Nicolson. The penalty parameter should be chosen so that $1/\lambda$ is smaller than the discretization error.

---

## Summary

$$
\boxed{
\frac{\partial V}{\partial t} + \mathcal{L}V - rV + \lambda(\Phi - V)^+ = 0 \quad \xrightarrow{\lambda \to \infty} \quad \text{American price}
}
$$

| Aspect | Description |
|---|---|
| Penalty method | Soft enforcement of exercise constraint |
| PSOR | Iterative LCP solver with projection |
| Penalty parameter | $\lambda \sim 10^6$–$10^8$ balances accuracy and conditioning |
| Error | $O(1/\lambda)$ from penalty + $O(h^2, \Delta t^p)$ from discretization |

**Penalty methods and PSOR provide complementary approaches to the American option LCP: penalty methods offer simplicity and compatibility with existing solvers, while PSOR delivers exact constraint satisfaction without penalty approximation error.**

---

## Exercises

**Exercise 1.** Write down the linear complementarity problem (LCP) for an American put: state the PDE inequality, the exercise constraint, and the complementarity condition. Explain why the three conditions together uniquely determine the American put price and the free boundary.

??? success "Solution to Exercise 1"
    The linear complementarity problem (LCP) for an American put with payoff $g(S) = (K - S)^+$ consists of three conditions that must hold simultaneously for all $(S, t) \in (0, \infty) \times [0, T)$:

    **1. PDE inequality (the option value satisfies or exceeds the Black-Scholes PDE):**

    $$
    -\frac{\partial V}{\partial t} - \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rS\frac{\partial V}{\partial S} + rV \geq 0
    $$

    This states that the Black-Scholes operator applied to $V$ is non-negative. In the continuation region, this holds as an equality (the standard PDE). In the exercise region, the PDE residual is strictly positive because the option is being "held down" at the intrinsic value.

    **2. Exercise constraint (the option value is at least the intrinsic value):**

    $$
    V(S, t) \geq (K - S)^+
    $$

    This is the no-arbitrage constraint: the American put can always be exercised for $(K - S)^+$, so its value cannot be less.

    **3. Complementarity condition (at each point, at least one inequality binds):**

    $$
    \left(-\frac{\partial V}{\partial t} - \mathcal{L}V + rV\right) \cdot \left(V - (K-S)^+\right) = 0
    $$

    This states that the product of the two "slacks" is zero. At every point, either the PDE holds as an equality (continuation region) or the option value equals the payoff (exercise region), or both (at the free boundary).

    **Why uniqueness:** The three conditions together specify the problem completely. The exercise constraint partitions the domain into two regions. In the continuation region ($V > g$), the complementarity condition forces the PDE to hold exactly, giving a well-posed boundary-value problem. In the exercise region ($V = g$), the value is determined. The free boundary $S^*(t)$ is determined by the requirement that both conditions transition smoothly (smooth pasting). Standard results from the theory of variational inequalities guarantee existence and uniqueness of the solution.

---


**Exercise 2.** In the penalty method, the variational inequality is approximated by $\frac{\partial V}{\partial t} + \mathcal{L}V + \lambda \max(g(S) - V, 0) = 0$ where $g(S) = (K-S)^+$ is the payoff. Explain the role of the penalty parameter $\lambda$: what happens as $\lambda \to \infty$, and what is the trade-off between large $\lambda$ (accuracy) and numerical conditioning?

??? success "Solution to Exercise 2"
    The penalty method replaces the variational inequality with the penalized PDE:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S - rV + \lambda \max\left((K-S)^+ - V, \, 0\right) = 0
    $$

    **Role of $\lambda$:** The penalty parameter $\lambda > 0$ controls how strongly the constraint $V \geq (K-S)^+$ is enforced:

    - When $V > (K-S)^+$: the $\max$ term is zero, and the standard Black-Scholes PDE holds. The penalty has no effect in the continuation region.
    - When $V < (K-S)^+$: the penalty term $\lambda((K-S)^+ - V) > 0$ is activated. This large positive term forces $V$ upward toward the payoff. The larger $\lambda$ is, the stronger the restoring force.

    **As $\lambda \to \infty$:** The penalized solution $V^\lambda$ converges to the true American price $V$. The constraint violation $\max((K-S)^+ - V^\lambda, 0)$ shrinks to zero. In the limit, $V^\lambda \geq (K-S)^+$ holds exactly, and the penalized PDE reduces to the variational inequality. The convergence rate is:

    $$
    \|V^\lambda - V\|_\infty = O(1/\lambda)
    $$

    **Trade-off between accuracy and conditioning:**

    - **Large $\lambda$ (accuracy):** The penalty approximation error $O(1/\lambda)$ is small, so $V^\lambda$ closely approximates $V$. The free boundary is accurately located.
    - **Large $\lambda$ (poor conditioning):** The penalized system becomes stiff. The penalty term introduces coefficients of order $\lambda$ into the discrete equations, leading to large condition numbers. Iterative solvers converge slowly, and direct solvers may suffer from round-off errors. The system $(L + \lambda P)\mathbf{u} = \mathbf{f}$ has eigenvalues of order $\lambda$ in the exercise region and $O(1)$ in the continuation region.

    The practical recommendation is $\lambda \sim 10^6$--$10^8$, which gives $O(1/\lambda) \sim 10^{-6}$--$10^{-8}$ penalty error, well below typical discretization errors of $O(h^2 + \Delta t^2)$ for Crank-Nicolson with mesh sizes $h, \Delta t \sim 10^{-2}$--$10^{-3}$.

---


**Exercise 3.** Describe the PSOR (projected successive over-relaxation) algorithm for solving the discretized American option LCP. At each grid point, what is the projection step, and how does it enforce the early-exercise constraint?

??? success "Solution to Exercise 3"
    The PSOR algorithm solves the LCP: $L\mathbf{u} \geq \mathbf{f}$, $\mathbf{u} \geq \boldsymbol{\Phi}$, with complementarity $(L\mathbf{u} - \mathbf{f})^T(\mathbf{u} - \boldsymbol{\Phi}) = 0$.

    At each time step, given the right-hand side from the previous time step, iterate:

    **For each grid point $j = 1, 2, \ldots, M-1$ (sweep through the grid):**

    **Step 1 (SOR update):** Compute the tentative new value using the SOR formula:

    $$
    \tilde{u}_j^{(k+1)} = (1 - \omega) u_j^{(k)} + \frac{\omega}{l_{jj}}\left(f_j - \sum_{i < j} l_{ji} u_i^{(k+1)} - \sum_{i > j} l_{ji} u_i^{(k)}\right)
    $$

    where $\omega \in (1, 2)$ is the over-relaxation parameter, $l_{ji}$ are elements of the matrix $L$, and the sum uses the most recent values (Gauss-Seidel style: already-updated values for $i < j$, old values for $i > j$).

    **Step 2 (Projection):** Enforce the exercise constraint:

    $$
    u_j^{(k+1)} = \max\left(\tilde{u}_j^{(k+1)}, \, \Phi_j\right)
    $$

    where $\Phi_j = (K - S_j)^+$ is the payoff at grid point $j$.

    **How the projection enforces early exercise:** If the SOR update produces $\tilde{u}_j < \Phi_j$, the projection raises $u_j$ to the payoff value. This corresponds to the exercise region where $V = \Phi$. If $\tilde{u}_j \geq \Phi_j$, the projection has no effect, corresponding to the continuation region where $V > \Phi$.

    The iterations continue until $\|\mathbf{u}^{(k+1)} - \mathbf{u}^{(k)}\|_\infty < \varepsilon$ (convergence). Typically 5--20 iterations per time step suffice with $\omega \approx 1.2$--$1.5$.

---


**Exercise 4.** For the Crank-Nicolson scheme applied to the American put PDE, explain why the standard time-stepping must be modified to handle the early-exercise constraint. Describe how the projection is applied after each implicit solve.

??? success "Solution to Exercise 4"
    The Crank-Nicolson scheme for the Black-Scholes PDE is:

    $$
    \frac{V_j^{n+1} - V_j^n}{\Delta t} = \frac{1}{2}\left(\mathcal{L}_h V_j^{n+1} + \mathcal{L}_h V_j^n\right) - rV_j^{n+1/2}
    $$

    where $\mathcal{L}_h$ is the discrete spatial operator. This leads to a tridiagonal system $A\mathbf{V}^{n+1} = B\mathbf{V}^n + \mathbf{b}$ at each time step.

    **Why modification is needed:** The standard Crank-Nicolson solve produces values $\mathbf{V}^{n+1}$ that satisfy the PDE exactly but may violate the constraint $V_j^{n+1} \geq \Phi_j$. In the exercise region, the option value should equal the intrinsic value, but the unconstrained PDE solve can push it below.

    **How the projection is applied:** After each implicit solve (or half-step), the constraint is enforced by:

    $$
    V_j^{n+1} \leftarrow \max\left(V_j^{n+1}, \, \Phi_j\right) \quad \text{for all } j
    $$

    This is the simplest approach, called the **explicit projection** or **operator-splitting** method. It proceeds as:

    1. Solve the unconstrained Crank-Nicolson system: $A\tilde{\mathbf{V}}^{n+1} = B\mathbf{V}^n + \mathbf{b}$
    2. Project: $V_j^{n+1} = \max(\tilde{V}_j^{n+1}, \Phi_j)$ for all $j$

    **Limitation of simple projection:** Applying the projection after the full Crank-Nicolson step can introduce a splitting error of $O(\Delta t)$, reducing the overall scheme from second-order to first-order accuracy near the free boundary. This is because the PDE and the constraint are solved separately rather than simultaneously.

    **Better approach:** Use PSOR or the penalty method to solve the constrained system directly within each implicit step. This maintains the full accuracy of the Crank-Nicolson discretization by treating the PDE and the constraint as a coupled system.

---


**Exercise 5.** Compare the penalty method and PSOR in terms of: (a) accuracy of the free boundary approximation, (b) computational cost per time step, (c) ease of implementation, and (d) sensitivity to parameter choices. Which method would you recommend for a production pricing system, and why?

??? success "Solution to Exercise 5"
    **(a) Accuracy of free boundary approximation:**

    - **Penalty method:** The free boundary location has an error of $O(1/\lambda)$ from the penalty approximation, plus the discretization error. With $\lambda = 10^7$ and mesh size $h = 0.01$, the penalty error ($10^{-7}$) is negligible compared to $O(h^2) = 10^{-4}$. However, the penalty introduces a smooth transition zone of width $O(1/\lambda)$ around the true free boundary, rather than a sharp interface.
    - **PSOR:** Solves the LCP exactly (up to the iteration tolerance $\varepsilon$), so the free boundary is determined to the accuracy of the finite difference grid with no additional penalty error. The boundary is identified sharply at the grid scale.

    **(b) Computational cost per time step:**

    - **Penalty method:** Requires solving a modified tridiagonal system (with penalty terms on the diagonal) iteratively. Typically 3--10 iterations per time step, each involving a tridiagonal solve at $O(M)$ cost. Total: $O(3\text{--}10 \times M)$ per time step.
    - **PSOR:** Requires 5--20 SOR iterations per time step, each sweeping through $M$ grid points at $O(M)$ cost. Total: $O(5\text{--}20 \times M)$ per time step. Generally slightly more expensive than penalty.

    **(c) Ease of implementation:**

    - **Penalty method:** Simple to implement. Take an existing Black-Scholes PDE solver and add a penalty term to the diagonal of the matrix. The modification is localized and minimal.
    - **PSOR:** Requires implementing the SOR iteration with the projection step. More involved than penalty, but still straightforward for tridiagonal systems. Requires choosing $\omega$ and a convergence criterion.

    **(d) Sensitivity to parameter choices:**

    - **Penalty method:** Sensitive to $\lambda$. Too small gives inaccurate prices; too large causes ill-conditioning. The "sweet spot" ($10^6$--$10^8$) is well-established but problem-dependent.
    - **PSOR:** Sensitive to $\omega$. Optimal $\omega$ depends on the matrix properties and is not known a priori. Suboptimal $\omega$ leads to slow convergence but does not affect accuracy. The convergence criterion $\varepsilon$ is easy to set.

    **Recommendation for production:** PSOR is generally preferred for a production pricing system because it solves the LCP exactly without introducing the additional approximation error of the penalty method. The slightly higher implementation effort is justified by the guaranteed accuracy and the absence of a penalty parameter to tune. For systems where the PDE solver is already built and cannot be easily modified, the penalty method is a pragmatic alternative.
