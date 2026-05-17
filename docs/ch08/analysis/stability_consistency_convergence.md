# Stability, Consistency, and Convergence

Consider what could go wrong with an FDM scheme. Either the *local* equation it solves is wrong (the discrete operator does not match the PDE as $h\to 0$ -- a **consistency** failure), or each step amplifies errors so badly that they swamp the answer (a **stability** failure). Eliminate both and the global error must go to zero -- this is **convergence**. The Lax Equivalence Theorem makes the implication precise: for linear, well-posed problems, consistency plus stability is equivalent to convergence.

---

## The Fundamental Principle

For linear, well-posed problems:

$$
\boxed{
\text{Consistency} + \text{Stability} \Longrightarrow \text{Convergence}
}
$$

This is the **Lax Equivalence Theorem**: a consistent scheme converges if and only if it is stable.

---

## Consistency

### Definition

A scheme is **consistent** if the local truncation error vanishes as the mesh is refined.

For a PDE $\mathcal{L}u = 0$ and discrete approximation $\mathcal{L}_{\Delta}u_{\Delta} = 0$:

$$
\text{Local truncation error} = \mathcal{L}_{\Delta}u - \mathcal{L}u
$$

where $u$ is the exact solution.

**Consistency**: LTE $\to 0$ as $\Delta\tau, \Delta S \to 0$.

### Order of Consistency

If LTE $= O((\Delta\tau)^p + (\Delta S)^q)$, the scheme is:

- $p$-th order in time
- $q$-th order in space

### Example: Crank-Nicolson

For smooth solutions:

$$
\text{LTE} = O((\Delta\tau)^2 + (\Delta S)^2)
$$

Crank-Nicolson is **second-order consistent** in both time and space.

---

## Stability

### Definition

A scheme is **stable** if errors remain bounded as the computation proceeds.

For a linear scheme $\mathbf{u}^{n+1} = B\mathbf{u}^n$, stability requires:

$$
\boxed{
\|B^n\| \leq C \quad \text{for all } n\Delta\tau \leq T
}
$$

for some constant $C$ independent of the mesh.

### Von Neumann (Fourier) Analysis

Recall (see [§ Von Neumann Stability Analysis](von_neumann_stability_analysis.md)): decompose errors into Fourier modes $\varepsilon_j^n = g^n e^{i\xi j}$; the scheme is stable iff the amplification factor $|g(\xi)| \leq 1$ for all $\xi \in [-\pi,\pi]$. The explicit heat scheme has $g = 1 - 4\lambda\sin^2(\xi/2)$ requiring $\lambda \leq 1/2$; implicit and Crank-Nicolson are unconditionally stable.

---

## Convergence

### Definition

A scheme **converges** if the numerical solution approaches the exact solution as the mesh is refined:

$$
\lim_{\Delta\tau, \Delta S \to 0} \max_{n,j} |u_j^n - u(\tau_n, S_j)| = 0
$$

### Convergence Rate

If the error satisfies:

$$
\|u_{\Delta} - u\| = O((\Delta\tau)^p + (\Delta S)^q)
$$

the scheme has convergence rate $(p, q)$.

### The Lax Equivalence Theorem

**Theorem**: For a well-posed linear initial value problem and a consistent finite difference scheme, **stability is equivalent to convergence**.

**Proof sketch**:

1. Let $e^n = u^n - u(\tau_n)$ be the global error
2. Error evolution: $e^{n+1} = Be^n + \text{LTE}$
3. By induction: $e^n = B^n e^0 + \sum_{k=0}^{n-1} B^{n-1-k}\text{LTE}_k$
4. If stable: $\|B^n\| \leq C$, so errors remain bounded
5. If consistent: LTE $\to 0$, so total error $\to 0$

---

## Practical Stability Analysis

### Matrix Criterion

For $\mathbf{u}^{n+1} = B\mathbf{u}^n$, stability requires:

$$
\rho(B) \leq 1 + O(\Delta\tau)
$$

where $\rho(B)$ is the spectral radius (largest eigenvalue magnitude).

### Energy Methods

For some problems, multiply by $u$ and sum to get energy estimates:

$$
\|u^{n+1}\|^2 \leq \|u^n\|^2
$$

This directly proves stability.

### Comparison Principles

**Monotone schemes** preserve the discrete maximum principle:

$$
\min_j u_j^n \leq u_j^{n+1} \leq \max_j u_j^n
$$

This implies $L^\infty$ stability.

---

## Issues with Non-Smooth Data

Option payoffs like $(S-K)^+$ are not smooth at $S = K$: Taylor expansions underlying consistency analysis break down, and observed convergence rates fall below theoretical (typically from 2 down to $0.5$–$1$ near the kink). Standard remedies: Rannacher smoothing, payoff smoothing, grid alignment at $K$, and Richardson extrapolation (see [§ Richardson Extrapolation — When Extrapolation Fails](richardson_extrapolation.md#when-richardson-extrapolation-fails)).

---

## The CFL Condition

Recall (see [§ CFL Condition and Time Step Restrictions](cfl_condition_and_time_step.md)): the CFL condition is the necessary stability constraint for explicit schemes, summarized by

- advection $u_t + cu_x = 0$: $|c|\Delta t/\Delta x \le 1$;
- diffusion $u_\tau = Du_{xx}$: $D\Delta\tau/(\Delta x)^2 \le 1/2$;
- Black-Scholes with variable coefficient $\tfrac{1}{2}\sigma^2 S^2$: $\sigma^2 S_{\max}^2 \Delta\tau / (2(\Delta S)^2) \le 1/2$.

---

## Convergence Study (Practical)

Recall (see [§ Grid Convergence and Error Analysis](grid_convergence_and_error_analysis.md)): refine on $M, 2M, 4M, \ldots$, compare to a reference, and read the order from the log-log slope. A ratio $\approx 4$ between successive errors confirms second-order convergence.

---

## Summary

$$
\boxed{
\text{Consistency} + \text{Stability} \Longleftrightarrow \text{Convergence}
}
$$

| Concept | Definition | Verification |
|---------|------------|--------------|
| **Consistency** | LTE $\to 0$ | Taylor expansion |
| **Stability** | $\|B^n\| \leq C$ | Von Neumann analysis |
| **Convergence** | $u_\Delta \to u$ | Lax theorem + above |

| Scheme | Stability | CFL Restriction |
|--------|-----------|-----------------|
| Explicit | Conditional | $\Delta\tau \leq C(\Delta S)^2$ |
| Implicit | Unconditional | None |
| Crank-Nicolson | Unconditional | None |

**A well-designed finite difference scheme must be both consistent and stable to guarantee convergence to the correct solution.**

---

## Exercises

**Exercise 1.** Consider the explicit scheme for the heat equation $u_\tau = \frac{1}{2}u_{xx}$ with mesh ratio $\lambda = \Delta\tau / (\Delta x)^2$. Show that the amplification factor is $G = 1 - 2\lambda(1 - \cos(k\Delta x))$ and derive the stability condition $\lambda \leq 1/2$ directly from $|G| \leq 1$.

??? success "Solution to Exercise 1"
    The explicit scheme for $u_\tau = \frac{1}{2}u_{xx}$ with mesh ratio $\lambda = \Delta\tau / (\Delta x)^2$ is:

    $$
    u_j^{n+1} = u_j^n + \lambda(u_{j+1}^n - 2u_j^n + u_{j-1}^n)
    $$

    Substitute a single Fourier mode $\varepsilon_j^n = G^n e^{ikj\Delta x}$ into the difference equation:

    $$
    G^{n+1} e^{ikj\Delta x} = G^n e^{ikj\Delta x} + \lambda G^n \bigl(e^{ik(j+1)\Delta x} - 2e^{ikj\Delta x} + e^{ik(j-1)\Delta x}\bigr)
    $$

    Dividing both sides by $G^n e^{ikj\Delta x}$:

    $$
    G = 1 + \lambda(e^{ik\Delta x} + e^{-ik\Delta x} - 2) = 1 + \lambda(2\cos(k\Delta x) - 2)
    $$

    Using the identity $\cos\theta - 1 = -2\sin^2(\theta/2)$:

    $$
    G = 1 - 4\lambda\sin^2\!\left(\frac{k\Delta x}{2}\right) = 1 - 2\lambda(1 - \cos(k\Delta x))
    $$

    This confirms $G = 1 - 2\lambda(1 - \cos(k\Delta x))$.

    For stability we need $|G| \leq 1$. Since $\sin^2(k\Delta x / 2) \in [0, 1]$, the amplification factor ranges from $G = 1$ (when $k\Delta x = 0$) to $G = 1 - 4\lambda$ (when $k\Delta x = \pi$).

    The condition $|G| \leq 1$ requires:

    $$
    -1 \leq 1 - 4\lambda \leq 1
    $$

    The right inequality $1 - 4\lambda \leq 1$ is always satisfied for $\lambda > 0$. The left inequality gives $1 - 4\lambda \geq -1$, i.e., $4\lambda \leq 2$, hence $\lambda \leq 1/2$.

    Note that here the diffusion coefficient is $D = 1/2$, so $\lambda = \Delta\tau / (\Delta x)^2$ and the CFL condition $D\lambda' \leq 1/2$ with $\lambda' = \Delta\tau / (\Delta x)^2$ gives $\Delta\tau \leq (\Delta x)^2 / (2D) = (\Delta x)^2$, consistent with $\lambda \leq 1/2$ under the convention used.

---

**Exercise 2.** Verify the consistency of the Crank-Nicolson scheme by substituting the exact solution into the discrete equation and performing a Taylor expansion. Show that the local truncation error is

$$
\text{LTE} = O((\Delta\tau)^2 + (\Delta S)^2)
$$

Identify the leading-order error terms explicitly.

??? success "Solution to Exercise 2"
    The Crank-Nicolson scheme for $u_\tau = \frac{1}{2}\sigma^2 u_{SS}$ is:

    $$
    \frac{u_j^{n+1} - u_j^n}{\Delta\tau} = \frac{1}{2}\sigma^2 \cdot \frac{1}{2}\left[\frac{u_{j+1}^n - 2u_j^n + u_{j-1}^n}{(\Delta S)^2} + \frac{u_{j+1}^{n+1} - 2u_j^{n+1} + u_{j-1}^{n+1}}{(\Delta S)^2}\right]
    $$

    Substitute the exact solution $u(S_j, \tau_n)$ and expand in Taylor series around $(S_j, \tau_{n+1/2})$, the midpoint in time.

    **Temporal discretization**: With $\tau_{n+1/2} = \tau_n + \Delta\tau/2$:

    $$
    u_j^{n+1} = u_{n+1/2} + \frac{\Delta\tau}{2}u_\tau + \frac{1}{2}\left(\frac{\Delta\tau}{2}\right)^2 u_{\tau\tau} + O((\Delta\tau)^3)
    $$

    $$
    u_j^n = u_{n+1/2} - \frac{\Delta\tau}{2}u_\tau + \frac{1}{2}\left(\frac{\Delta\tau}{2}\right)^2 u_{\tau\tau} + O((\Delta\tau)^3)
    $$

    So $(u_j^{n+1} - u_j^n)/\Delta\tau = u_\tau\big|_{n+1/2} + O((\Delta\tau)^2)$.

    **Spatial discretization**: The central difference $\delta_{SS}^2 u = (u_{j+1} - 2u_j + u_{j-1})/(\Delta S)^2 = u_{SS} + \frac{1}{12}(\Delta S)^2 u_{SSSS} + O((\Delta S)^4)$. The Crank-Nicolson average at levels $n$ and $n+1$ evaluates to $u_{SS}\big|_{n+1/2} + O((\Delta S)^2 + (\Delta\tau)^2)$.

    Combining, the local truncation error is:

    $$
    \text{LTE} = \left[u_\tau - \frac{1}{2}\sigma^2 u_{SS}\right]_{n+1/2} + O((\Delta\tau)^2) + O((\Delta S)^2)
    $$

    The bracketed term vanishes because $u$ satisfies the PDE. The leading-order error terms are:

    - Time: $\frac{1}{24}(\Delta\tau)^2 u_{\tau\tau\tau}$
    - Space: $\frac{1}{12}\sigma^2(\Delta S)^2 u_{SSSS}$

    Therefore LTE $= O((\Delta\tau)^2 + (\Delta S)^2)$, confirming second-order consistency in both time and space.

---

**Exercise 3.** The Lax Equivalence Theorem states that for a consistent, well-posed linear problem, stability is equivalent to convergence. Explain why each of the three hypotheses (linearity, well-posedness, consistency) is necessary by giving a counterexample or argument for what can go wrong when each is removed.

??? success "Solution to Exercise 3"
    **Linearity**: The Lax Equivalence Theorem applies to linear problems. Without linearity, the superposition principle fails: errors cannot be decomposed into independent modes, and the relationship between stability and convergence breaks down. A simple counterexample is the nonlinear ODE $u' = u^2$ discretized with forward Euler. The scheme can be consistent and stable for small perturbations yet fail to converge for large perturbations because the error evolution is inherently nonlinear.

    **Well-posedness**: The PDE must have a unique solution that depends continuously on the data. The backward heat equation $u_t = -u_{xx}$ is ill-posed: arbitrarily small perturbations in the initial data lead to unbounded growth in the exact solution. No consistent, stable numerical scheme can converge to a meaningful solution of an ill-posed problem, because the "exact solution" itself is not well-defined under perturbation.

    **Consistency**: Without consistency, the scheme may be stable (errors do not grow) but converge to the wrong answer. For example, consider the trivial scheme $u_j^{n+1} = u_j^n$ for the heat equation $u_\tau = u_{xx}$. This scheme is perfectly stable ($\|B^n\| = 1$) but has a non-vanishing truncation error as $\Delta\tau, \Delta x \to 0$ (it approximates $u_\tau = 0$, not $u_\tau = u_{xx}$). The numerical solution converges — but to the initial condition, not to the solution of the heat equation.

---

**Exercise 4.** A convergence study on four successively refined grids produces the following maximum errors for a European call priced via Crank-Nicolson:

| Grid ($M$) | Max Error |
|------------|-----------|
| 50         | 0.0820    |
| 100        | 0.0205    |
| 200        | 0.0051    |
| 400        | 0.0013    |

Compute the error ratios and confirm second-order convergence. If the error were instead $O((\Delta S)^{3/2})$, what ratios would you expect?

??? success "Solution to Exercise 4"
    The error ratios between successive grids are:

    $$
    \frac{0.0820}{0.0205} = 4.0, \quad \frac{0.0205}{0.0051} = 4.02, \quad \frac{0.0051}{0.0013} = 3.92
    $$

    All ratios are approximately 4. Since doubling $M$ halves $\Delta S$, and the error decreases by a factor of 4, we have Error $\propto (\Delta S)^2 \propto M^{-2}$, confirming second-order convergence.

    If the error were $O((\Delta S)^{3/2})$ instead, then halving $\Delta S$ would reduce the error by a factor of $2^{3/2} = 2\sqrt{2} \approx 2.83$. The expected ratios would be approximately 2.83 rather than 4.

---

**Exercise 5.** For the Black-Scholes PDE with $\sigma = 0.25$ and $S_{\max} = 400$, compute the CFL restriction on $\Delta\tau$ for the explicit scheme when $\Delta S = 2$. How many time steps are needed for $T = 1$ year? Repeat the calculation in log-price coordinates with $\Delta x = 0.02$ and compare.

??? success "Solution to Exercise 5"
    **In original coordinates** with $\sigma = 0.25$, $S_{\max} = 400$, and $\Delta S = 2$:

    $$
    \Delta\tau \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2} = \frac{(2)^2}{(0.25)^2 \times (400)^2} = \frac{4}{0.0625 \times 160000} = \frac{4}{10000} = 4 \times 10^{-4}
    $$

    For $T = 1$ year:

    $$
    N \geq \frac{T}{\Delta\tau} = \frac{1}{4 \times 10^{-4}} = 2{,}500 \text{ time steps}
    $$

    **In log-price coordinates** with $\Delta x = 0.02$:

    $$
    \Delta\tau \leq \frac{(\Delta x)^2}{\sigma^2} = \frac{(0.02)^2}{(0.25)^2} = \frac{4 \times 10^{-4}}{0.0625} = 6.4 \times 10^{-3}
    $$

    For $T = 1$ year:

    $$
    N \geq \frac{1}{6.4 \times 10^{-3}} \approx 157 \text{ time steps}
    $$

    The log-price formulation requires roughly 16 times fewer time steps (157 vs. 2,500), because the CFL restriction is independent of $S_{\max}$.

---

**Exercise 6.** The payoff $(S - K)^+$ has a kink at $S = K$. Explain, using the concept of local truncation error, why the convergence rate of a second-order scheme may degrade near $S = K$. Describe two remedies and state how each restores the expected convergence order.

??? success "Solution to Exercise 6"
    The local truncation error (LTE) of a second-order finite difference scheme is derived via Taylor expansion of the exact solution. For the central difference approximation of $u_{SS}$:

    $$
    \frac{u(S+\Delta S) - 2u(S) + u(S-\Delta S)}{(\Delta S)^2} = u_{SS} + \frac{(\Delta S)^2}{12}u_{SSSS} + O((\Delta S)^4)
    $$

    This expansion requires $u$ to have at least four continuous derivatives. At $S = K$, the payoff $(S-K)^+$ has a kink: $u_S$ is discontinuous (it jumps from 0 to 1 for a call), and $u_{SS}$ contains a Dirac delta. The higher derivatives $u_{SSS}$, $u_{SSSS}$ do not exist in the classical sense.

    Consequently, the Taylor expansion underlying the LTE analysis is invalid near $S = K$. The actual truncation error at nodes near the kink is $O(1)$ rather than $O((\Delta S)^2)$, and the global error degrades from $O((\Delta S)^2)$ to $O((\Delta S)^{1/2})$ or $O(\Delta S)$ depending on how close grid points are to the kink.

    **Remedy 1: Rannacher smoothing.** Perform 2-4 fully implicit (backward Euler) time steps near maturity before switching to Crank-Nicolson. The implicit scheme has strong damping that smooths out the kink in 1-2 time steps, after which the solution is $C^\infty$ and Crank-Nicolson achieves its full second-order rate.

    **Remedy 2: Payoff smoothing.** Replace the non-smooth payoff with a smooth approximation over a small interval $[K - \epsilon, K + \epsilon]$, for example using a polynomial or Gaussian kernel. With an appropriate choice of $\epsilon = O(\Delta S)$, this restores the full second-order convergence rate.

---

**Exercise 7.** Suppose a numerical scheme has iteration matrix $B$ with spectral radius $\rho(B) = 1 + 2\Delta\tau$. Is this scheme stable in the sense required by the Lax Equivalence Theorem? Justify your answer by relating $\rho(B)$ to the bound $\|B^n\| \leq C$ for $n\Delta\tau \leq T$.

??? success "Solution to Exercise 7"
    Yes, the scheme is stable in the Lax sense. The Lax stability condition requires $\|B^n\| \leq C$ for all $n\Delta\tau \leq T$, where $C$ is independent of the mesh parameters.

    With $\rho(B) = 1 + 2\Delta\tau$, the spectral radius satisfies $\rho(B) \leq 1 + C'\Delta\tau$ with $C' = 2$. For a normal matrix (or using the spectral radius as a bound on the matrix norm), we have:

    $$
    \|B^n\| \leq \rho(B)^n = (1 + 2\Delta\tau)^n
    $$

    Since $n\Delta\tau \leq T$, we have $n \leq T / \Delta\tau$, and:

    $$
    (1 + 2\Delta\tau)^n \leq (1 + 2\Delta\tau)^{T/\Delta\tau} \leq e^{2T}
    $$

    where the last inequality uses $(1 + a/m)^m \leq e^a$. Since $e^{2T}$ is a finite constant depending only on $T$ (not on $\Delta\tau$ or $n$), we have $\|B^n\| \leq e^{2T} = C$ for all $n\Delta\tau \leq T$.

    This is precisely the Lax stability condition. A spectral radius of $1 + O(\Delta\tau)$ is permissible — it is only $\rho(B) > 1 + O(1)$ (growth independent of mesh refinement) that causes instability.
