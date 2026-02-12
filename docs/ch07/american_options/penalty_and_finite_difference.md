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

### Choice of $\lambda$

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
