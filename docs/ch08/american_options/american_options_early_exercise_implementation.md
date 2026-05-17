# American Options and Early Exercise: Implementation

At every time step an American option must satisfy two things at once: the Black-Scholes PDE in the continuation region and the floor $V(S,t)\ge\Phi(S)$ everywhere. The cheapest implementation enforces this by alternation -- solve the unconstrained linear system for one step, then snap each node up to the payoff $\Phi$ if it dipped below. That single line of code, the **projection step**, is the splitting-error approximation to the underlying linear complementarity problem and the practical heart of every American-option scheme in this section. Recall (see [§ Free Boundary Problems](free_boundary_problems_american_options.md)): $\Phi(S)=(S-K)^+$ for a call and $\Phi(S)=(K-S)^+$ for a put.

---

## Modifying the FDM Approach

The simplest treatment is the **projection method**: solve the unconstrained linear system at each time step, then enforce

```python
V_new[i] = max(V_new[i], payoff[i])
```

Recall (see [§ Linear Complementarity Formulation](linear_complementarity_formulation.md)): the underlying discrete problem is an **LCP**, and the projection step here is the easy-to-implement (splitting-error) approximation to it.

---

## Algorithm: Crank-Nicolson with Projection

1. Discretize space and time.
2. Set the terminal payoff as usual.
3. At each time step:
   - Solve the Crank-Nicolson (or implicit) system.
   - For each node, apply: $V_i^{n+1} = \max(V_i^{n+1}, \Phi(S_i))$.

---

## Python Sketch: American Put Option (CN + Projection)

```python
import numpy as np

def american_put_cn(S_max=200, K=100, T=1.0, r=0.05, sigma=0.2, M=100):
    dS = S_max / M
    S = np.linspace(0, S_max, M + 1)
    dt = 0.4 * dS**2 / (sigma**2 * S_max**2)
    N = int(T / dt)
    dt = T / N

    V = np.maximum(K - S, 0)  # American PUT payoff

    a = np.zeros(M - 1)
    b = np.zeros(M - 1)
    c = np.zeros(M - 1)
    payoff = V.copy()

    for i in range(1, M):
        Si = i * dS
        a[i - 1] = -0.25 * dt * ((sigma**2 * Si**2 - r * Si) / dS**2)
        b[i - 1] = 1 + 0.5 * dt * ((sigma**2 * Si**2 + r) / dS**2)
        c[i - 1] = -0.25 * dt * ((sigma**2 * Si**2 + r * Si) / dS**2)

    for n in range(N):
        rhs = np.zeros(M - 1)
        for i in range(1, M):
            Si = i * dS
            alpha = 0.25 * dt * ((sigma**2 * Si**2 - r * Si) / dS**2)
            beta  = -0.5 * dt * ((sigma**2 * Si**2 + r) / dS**2)
            gamma = 0.25 * dt * ((sigma**2 * Si**2 + r * Si) / dS**2)

            rhs[i - 1] = (
                alpha * V[i - 1] +
                (1 - beta) * V[i] +
                gamma * V[i + 1]
            )

        V[1:M] = solve_tridiagonal(a, b, c, rhs)

        # Early exercise projection
        for i in range(1, M):
            V[i] = max(V[i], payoff[i])

        V[0] = K * np.exp(-r * (T - (n + 1) * dt))  # lower bound
        V[M] = 0  # out of the money

    return S, V
```

---

## Visualizing American vs. European Option Value

```python
import matplotlib.pyplot as plt

S, V_am = american_put_cn()
V_eu = np.maximum(K - S, 0)  # Use BS formula for put if desired

plt.figure(figsize=(10, 6))
plt.plot(S, V_am, label='American Put (CN + Projection)')
plt.plot(S, V_eu, '--', label='European Put (Payoff)')
plt.xlabel("Stock Price")
plt.ylabel("Option Value")
plt.title("American vs. European Put Option")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
```

The **American put value is always above** the European counterpart due to the early exercise option.

---

## Summary

- American options require solving a **free boundary problem**.
- The solution must satisfy the **early exercise constraint** at all times.
- Simple projection methods are effective when combined with Crank-Nicolson or implicit schemes.
- The **difference between American and European values** represents the **early exercise premium**.

---

## Exercises

**Exercise 1.** In the Crank-Nicolson with projection algorithm, the projection step $V_i^{n+1} = \max(V_i^{n+1}, \Phi(S_i))$ is applied after solving the linear system. Explain why this sequential approach (solve then project) can introduce a splitting error near the free boundary. How does the LCP formulation avoid this issue?

??? success "Solution to Exercise 1"
    **Splitting error from sequential solve-then-project:**

    In the projection approach, the time step is split into two sub-steps:

    1. **Solve:** Compute $\tilde{V}^{n+1}$ from the unconstrained linear system (the PDE step).
    2. **Project:** Set $V_i^{n+1} = \max(\tilde{V}_i^{n+1}, \Phi(S_i))$.

    The PDE and the constraint are enforced *sequentially*, not *simultaneously*. Near the free boundary, grid points may switch between continuation and exercise from one step to the next. When a point transitions:

    - The PDE solve does not "know" that the constraint will bind at nearby points.
    - The projection modifies the solution locally but does not propagate this modification back through the PDE.

    This introduces a **splitting error** of order $O(\Delta\tau)$ near the free boundary, even if the underlying PDE scheme (e.g., Crank-Nicolson) is second-order. The overall time accuracy degrades to first-order in the vicinity of the boundary.

    **How the LCP avoids this:**

    The LCP formulation enforces the PDE and the constraint *simultaneously*. At each grid point, the solution satisfies either the PDE (in the continuation region) or the constraint (in the exercise region), with the complementarity condition coupling the two. Solvers like PSOR iterate until both conditions are mutually consistent, avoiding the splitting error. The LCP solution is the correct discrete analog of the variational inequality, preserving the full accuracy of the underlying time-stepping scheme.

---

**Exercise 2.** For an American put with $K = 100$, $r = 0.05$, $\sigma = 0.20$, $T = 1$, set up the payoff vector $\Phi$ on the grid $S = (0, 50, 100, 150, 200)$. What are the appropriate boundary conditions at $S = 0$ and $S = S_{\max} = 200$?

??? success "Solution to Exercise 2"
    On the grid $S = (0, 50, 100, 150, 200)$ with $K = 100$, the put payoff $\Phi(S) = (K - S)^+$ gives:

    $$
    \boldsymbol{\Phi} = \begin{pmatrix} \max(100 - 0, 0) \\ \max(100 - 50, 0) \\ \max(100 - 100, 0) \\ \max(100 - 150, 0) \\ \max(100 - 200, 0) \end{pmatrix} = \begin{pmatrix} 100 \\ 50 \\ 0 \\ 0 \\ 0 \end{pmatrix}
    $$

    **Boundary conditions:**

    - **At $S = 0$:** The stock price cannot become negative. With $S = 0$, the put is maximally in the money. For the American put, immediate exercise at $S = 0$ gives $K = 100$. The boundary condition is:

    $$
    V(0, t) = Ke^{-r(T-t)} = 100\,e^{-0.05(T-t)}
    $$

    This represents the present value of the exercise proceeds at the remaining time to maturity. (In practice, for an American put, the holder at $S = 0$ would exercise immediately, so $V(0, t) = K = 100$ is also used.)

    - **At $S = S_{\max} = 200$:** The put is deep out of the money. For sufficiently large $S_{\max}$, the probability of the stock falling below $K = 100$ is negligible:

    $$
    V(S_{\max}, t) = 0
    $$

---

**Exercise 3.** The boundary condition at $S = 0$ for an American put is $V(0, t) = Ke^{-r(T-t)}$. Derive this by arguing that at $S = 0$, immediate exercise yields $K$, but the present value of the exercise proceeds at a future time $T$ is $Ke^{-r(T-t)}$. Under what circumstances might immediate exercise at $S = 0$ be more valuable?

??? success "Solution to Exercise 3"
    At $S = 0$, the stock price is absorbed (it stays at zero under geometric Brownian motion since $dS = rS\,dt + \sigma S\,dW$ gives $dS = 0$ when $S = 0$). The put payoff at exercise is $K - 0 = K$.

    If the holder exercises immediately at time $t$, they receive $K$ right away and can invest it at rate $r$, growing to $Ke^{r(T-t)}$ by time $T$.

    If instead the holder waits until some future time $t' > t$ to exercise (still at $S = 0$), they receive $K$ at time $t'$. The present value at time $t$ is $Ke^{-r(t'-t)}$. Since $e^{-r(t'-t)} < 1$ for $t' > t$, waiting is strictly worse.

    Therefore at $S = 0$, **immediate exercise is always optimal** for the American put, and $V(0, t) = K$.

    The boundary condition $V(0,t) = Ke^{-r(T-t)}$ is used for the *European* put (where immediate exercise is not possible). For the American put, the correct boundary condition is $V(0, t) = K$.

    **When might immediate exercise at $S = 0$ be more valuable?** It is *always* more valuable to exercise immediately at $S = 0$ for an American put, since waiting only delays receipt of $K$ and $S$ will never rise above zero. The condition $V(0,t) = K > Ke^{-r(T-t)}$ holds strictly for $t < T$, confirming immediate exercise dominates.

---

**Exercise 4.** Explain why the American put value is always greater than or equal to the European put value. Sketch both as functions of $S$ on the same axes and identify the region where the two coincide.

??? success "Solution to Exercise 4"
    **Why $V_{\text{American}} \geq V_{\text{European}}$:**

    The American option grants all the same rights as the European option (exercise at $T$) *plus* the additional right to exercise at any time $t \leq T$. Since optimizing over a larger set of strategies (all stopping times in $[0, T]$) cannot yield a lower value than optimizing over a single time ($T$ only):

    $$
    V_{\text{American}} = \sup_{\tau \in \mathcal{T}_{0,T}} \mathbb{E}^{\mathbb{Q}}[e^{-r\tau}\Phi(S_\tau)] \geq \mathbb{E}^{\mathbb{Q}}[e^{-rT}\Phi(S_T)] = V_{\text{European}}
    $$

    **Sketch of both as functions of $S$:**

    - Both curves start at the same terminal condition at $T$: $V(S, T) = (K - S)^+$.
    - For $t < T$, the American put curve lies on or above the European put curve for all $S$.
    - The payoff line $\Phi(S) = (K - S)^+$ lies below both curves in the continuation region ($S > S^*(t)$).
    - In the exercise region ($S < S^*(t)$), the American put equals the payoff: $V_{\text{Am}}(S, t) = K - S$.
    - The European put lies below the payoff in this region (since the European holder cannot exercise early).

    **Region where the two coincide:**

    For large $S$ (deep out-of-the-money), both options have very small value, and the early exercise premium is negligible. The two values nearly coincide for $S \gg K$. They also coincide at $S = \infty$ (both are zero) and at the terminal time $T$ (both equal the payoff).

---

**Exercise 5.** Consider implementing the early exercise projection in log-price coordinates $x = \ln S$. Rewrite the put payoff $\Phi(S) = (K - S)^+$ in terms of $x$. At which value of $x$ does the payoff kink occur?

??? success "Solution to Exercise 5"
    In log-price coordinates $x = \ln S$, the stock price is $S = e^x$. The put payoff transforms as:

    $$
    \Phi(S) = (K - S)^+ = (K - e^x)^+
    $$

    This can be written as:

    $$
    \Phi(x) = \begin{cases} K - e^x & \text{if } x < \ln K \\ 0 & \text{if } x \geq \ln K \end{cases}
    $$

    The **payoff kink** (the point of non-differentiability) occurs at:

    $$
    x^* = \ln K
    $$

    For $K = 100$, this is $x^* = \ln 100 \approx 4.605$.

    Note that in $x$-coordinates, the payoff $K - e^x$ is a smooth, convex function for $x < \ln K$ (not a straight line as in $S$-coordinates). The kink at $x = \ln K$ is still present since the payoff transitions from $K - e^x > 0$ to $0$, with a slope discontinuity: the left derivative is $-e^{\ln K} = -K$ and the right derivative is $0$.

---

**Exercise 6.** A simple convergence test for American option pricing is to refine the grid and check that the price changes decrease. If the American put price is $\$6.10$ with $M = 100$, $\$6.06$ with $M = 200$, and $\$6.05$ with $M = 400$, estimate the convergence order using the Richardson ratio. Is the observed order consistent with the expected first-order convergence near the free boundary?

??? success "Solution to Exercise 6"
    The Richardson ratio is used to estimate the convergence order $p$ from three successively refined solutions. Let $V_h$ denote the price on a grid with spacing $h \propto 1/M$. With halving the grid spacing:

    - $V_{100} = 6.10$ (coarse)
    - $V_{200} = 6.06$ (medium)
    - $V_{400} = 6.05$ (fine)

    The successive differences are:

    $$
    \delta_1 = V_{100} - V_{200} = 6.10 - 6.06 = 0.04
    $$

    $$
    \delta_2 = V_{200} - V_{400} = 6.06 - 6.05 = 0.01
    $$

    The Richardson ratio is:

    $$
    R = \frac{\delta_1}{\delta_2} = \frac{0.04}{0.01} = 4
    $$

    For a scheme with convergence order $p$ and grid refinement ratio $r = 2$ (doubling $M$ halves $h$), the expected ratio is $R = r^p = 2^p$. So:

    $$
    2^p = 4 \implies p = 2
    $$

    **Is this consistent with expected first-order convergence?**

    The observed order $p = 2$ is *higher* than the expected first-order convergence near the free boundary. This can occur because:

    1. The price is evaluated at a grid point away from the free boundary (e.g., at-the-money), where the solution is smooth and the full second-order spatial accuracy is realized.
    2. The free boundary non-smoothness primarily affects convergence near the boundary itself, not globally.
    3. If Crank-Nicolson is used with sufficient time steps, second-order convergence may be observed away from the free boundary region.

    However, if we measured the convergence at or near the exercise boundary, we would typically see first-order convergence due to the non-smoothness. The global convergence order observed here ($p \approx 2$) is optimistic and may degrade on finer grids where the free boundary effects become more pronounced.
