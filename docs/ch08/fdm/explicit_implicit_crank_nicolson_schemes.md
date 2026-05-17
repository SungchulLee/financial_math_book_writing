# Explicit, Implicit, and Crank-Nicolson Schemes

After spatial discretization the Black-Scholes PDE becomes a coupled ODE system $d\mathbf{u}/d\tau=A\mathbf{u}$, with $A$ tridiagonal. Stepping that system from $\mathbf{u}^n$ to $\mathbf{u}^{n+1}$ comes down to one choice: where to evaluate $A\mathbf{u}$. At the *known* level $n$ gives **explicit** (cheap, conditionally stable). At the *unknown* level $n+1$ gives **implicit** (one linear solve per step, unconditionally stable). At the *average* of the two gives **Crank-Nicolson** (one linear solve, unconditionally stable, second-order in time). The three schemes are the three points of this trade-off.

---

## The Semi-Discrete System

Recall (see [§ Finite Difference Methods](finite_difference_methods.md)): after spatial discretization of the Black-Scholes PDE one obtains $\dfrac{d\mathbf{u}}{d\tau} = A\mathbf{u}$, with $\mathbf{u} = (u_1, \ldots, u_{M-1})^T$ and $A$ a tridiagonal spatial operator.

**Goal**: Advance from $\mathbf{u}^n$ at time $\tau_n$ to $\mathbf{u}^{n+1}$ at time $\tau_{n+1} = \tau_n + \Delta\tau$.

---

## Explicit Scheme (Forward Euler)

### Formulation

Evaluate the right-hand side at the **known** time level $n$:

$$
\boxed{
\mathbf{u}^{n+1} = \mathbf{u}^n + \Delta\tau \cdot A\mathbf{u}^n = (I + \Delta\tau A)\mathbf{u}^n
}
$$

### Component Form

$$
u_j^{n+1} = a_j u_{j-1}^n + (1 + b_j)u_j^n + c_j u_{j+1}^n
$$

### Properties

| Property | Assessment |
|----------|------------|
| Implementation | Simple, no linear solve |
| Cost per step | $O(M)$ |
| Stability | **Conditional** |
| Accuracy | First-order in time |

### Stability Condition (CFL)

Recall (see [§ CFL Condition and Time Step Restrictions](../analysis/cfl_condition_and_time_step.md)): the explicit scheme is conditionally stable under $\Delta\tau \leq (\Delta S)^2/(\sigma^2 S_{\max}^2)$, often a very restrictive constraint.

---

## Implicit Scheme (Backward Euler)

### Formulation

Evaluate the right-hand side at the **unknown** time level $n+1$:

$$
\mathbf{u}^{n+1} = \mathbf{u}^n + \Delta\tau \cdot A\mathbf{u}^{n+1}
$$

Rearranging:

$$
\boxed{
(I - \Delta\tau A)\mathbf{u}^{n+1} = \mathbf{u}^n
}
$$

### Properties

| Property | Assessment |
|----------|------------|
| Implementation | Requires linear solve |
| Cost per step | $O(M)$ with tridiagonal solver |
| Stability | **Unconditionally stable** |
| Accuracy | First-order in time |

### Linear System

The matrix $(I - \Delta\tau A)$ is tridiagonal. Recall (see [§ Implicit Scheme Implementation](../implementation/implicit_scheme_implementation.md)): the Thomas algorithm solves such systems in $O(M)$ operations.

### Advantages

- No time step restriction for stability
- Can use large $\Delta\tau$ if accuracy permits
- Robust for stiff problems

---

## Crank-Nicolson Scheme (Trapezoidal Rule)

### Formulation

Average of explicit and implicit:

$$
\mathbf{u}^{n+1} = \mathbf{u}^n + \frac{\Delta\tau}{2}(A\mathbf{u}^n + A\mathbf{u}^{n+1})
$$

Rearranging:

$$
\boxed{
\left(I - \frac{\Delta\tau}{2}A\right)\mathbf{u}^{n+1} = \left(I + \frac{\Delta\tau}{2}A\right)\mathbf{u}^n
}
$$

### Properties

| Property | Assessment |
|----------|------------|
| Implementation | Requires linear solve |
| Cost per step | $O(M)$ with tridiagonal solver |
| Stability | **Unconditionally stable** |
| Accuracy | **Second-order** in time |

### Why Second-Order?

Crank-Nicolson is equivalent to the trapezoidal rule for ODEs, which has error $O((\Delta\tau)^2)$.

---

## The Theta-Scheme (Generalization)

The **theta-scheme** parameterizes the family:

$$
\boxed{
(I - \theta\Delta\tau A)\mathbf{u}^{n+1} = (I + (1-\theta)\Delta\tau A)\mathbf{u}^n
}
$$

| $\theta$ | Scheme | Stability | Accuracy |
|----------|--------|-----------|----------|
| 0 | Explicit | Conditional | $O(\Delta\tau)$ |
| 1/2 | Crank-Nicolson | Unconditional | $O((\Delta\tau)^2)$ |
| 1 | Implicit | Unconditional | $O(\Delta\tau)$ |

**Common choice**: $\theta = 0.5$ (Crank-Nicolson) for accuracy, or $\theta = 1$ for robustness.

---

## Oscillation Issues with Crank-Nicolson

### The Problem

For **non-smooth** initial data (e.g., option payoffs with kinks), Crank-Nicolson can produce **oscillations** near $\tau = 0$.

**Example**: European call payoff $(S-K)^+$ has a discontinuous derivative at $S = K$.

### Cause

Crank-Nicolson is not **monotone**—the discrete maximum principle can be violated.

### Solution: Rannacher Time-Stepping

Use a few **implicit** steps initially, then switch to Crank-Nicolson:

```
For n = 0, 1:  (first two steps)
    Use backward Euler (θ = 1)
For n = 2, 3, ..., N-1:
    Use Crank-Nicolson (θ = 0.5)
```

This damps high-frequency oscillations while maintaining overall second-order accuracy.

---

## Comparison of Schemes

### Accuracy vs Stability

| Scheme | Time Accuracy | Space Accuracy | Stability |
|--------|---------------|----------------|-----------|
| Explicit | $O(\Delta\tau)$ | $O((\Delta S)^2)$ | Conditional |
| Implicit | $O(\Delta\tau)$ | $O((\Delta S)^2)$ | Unconditional |
| C-N | $O((\Delta\tau)^2)$ | $O((\Delta S)^2)$ | Unconditional |

### Computational Cost

| Scheme | Cost per Step | Total Cost (fixed accuracy) |
|--------|---------------|---------------------------|
| Explicit | $O(M)$ | High (many steps needed) |
| Implicit | $O(M)$ | Moderate |
| C-N | $O(M)$ | Low (fewer steps needed) |

---

## Practical Recommendations

### For European Options

1. Use **Crank-Nicolson** with **Rannacher smoothing**
2. Grid: $M \approx 200$, $N \approx 100$
3. Center grid around strike $K$

### For American Options

Recall (see [§ American Options Early Exercise Implementation](../american_options/american_options_early_exercise_implementation.md)): the implicit scheme is preferred and the early-exercise constraint is enforced by projection $u_j^{n+1} \leftarrow \max(u_j^{n+1}, \Phi_j)$.

### For Barrier Options

1. Use **implicit** for stability near barriers
2. Place grid points exactly on barriers

---

## Summary

$$
\boxed{
\begin{aligned}
\text{Explicit}: & \quad \mathbf{u}^{n+1} = (I + \Delta\tau A)\mathbf{u}^n \\
\text{Implicit}: & \quad (I - \Delta\tau A)\mathbf{u}^{n+1} = \mathbf{u}^n \\
\text{Crank-Nicolson}: & \quad \left(I - \frac{\Delta\tau}{2}A\right)\mathbf{u}^{n+1} = \left(I + \frac{\Delta\tau}{2}A\right)\mathbf{u}^n
\end{aligned}
}
$$

| Recommendation | Scheme |
|----------------|--------|
| Accuracy priority | Crank-Nicolson |
| Robustness priority | Implicit |
| Simplicity priority | Explicit (with small $\Delta\tau$) |
| Non-smooth data | Rannacher (implicit start, then C-N) |

**The choice of time-stepping scheme balances accuracy, stability, and computational efficiency.**

---

## Exercises

**Exercise 1.** For the explicit scheme with $\sigma = 0.3$, $S_{\max} = 300$, and $\Delta S = 1$, compute the maximum allowable time step $\Delta\tau$ for stability. How many time steps are needed for $T = 1$? Repeat for $\Delta S = 0.5$ and comment on how halving the spatial step affects the computational cost.

??? success "Solution to Exercise 1"
    The CFL stability condition for the explicit scheme applied to the Black-Scholes PDE is:

    $$
    \Delta\tau \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2}
    $$

    **Case 1**: $\sigma = 0.3$, $S_{\max} = 300$, $\Delta S = 1$:

    $$
    \Delta\tau \leq \frac{1^2}{0.09 \times 90000} = \frac{1}{8100} \approx 1.235 \times 10^{-4}
    $$

    For $T = 1$, the number of time steps required is:

    $$
    N \geq \frac{T}{\Delta\tau} = \frac{1}{1.235 \times 10^{-4}} \approx 8100
    $$

    **Case 2**: $\Delta S = 0.5$:

    $$
    \Delta\tau \leq \frac{0.25}{8100} = \frac{1}{32400} \approx 3.086 \times 10^{-5}
    $$

    $$
    N \geq \frac{1}{3.086 \times 10^{-5}} \approx 32400
    $$

    Halving $\Delta S$ reduces $(\Delta S)^2$ by a factor of $4$, so the maximum allowable $\Delta\tau$ also decreases by a factor of $4$, and the number of time steps increases by a factor of $4$. Meanwhile, the number of spatial points doubles from $M = 300$ to $M = 600$. The total computational cost (proportional to $M \times N$) increases by a factor of $2 \times 4 = 8$. This illustrates the severe computational burden of the explicit scheme: halving the spatial resolution increases the total cost eightfold.

---

**Exercise 2.** The theta-scheme is given by $(I - \theta\Delta\tau A)\mathbf{u}^{n+1} = (I + (1-\theta)\Delta\tau A)\mathbf{u}^n$. Show that for $\theta = 0$ this reduces to the explicit scheme and for $\theta = 1$ it reduces to the implicit scheme. What value of $\theta$ gives the Crank-Nicolson scheme, and why is it second-order accurate in time?

??? success "Solution to Exercise 2"
    The theta-scheme is:

    $$
    (I - \theta\Delta\tau A)\mathbf{u}^{n+1} = (I + (1-\theta)\Delta\tau A)\mathbf{u}^n
    $$

    **$\theta = 0$ (explicit scheme)**: The left side becomes $I\mathbf{u}^{n+1} = \mathbf{u}^{n+1}$ and the right side becomes $(I + \Delta\tau A)\mathbf{u}^n$, giving:

    $$
    \mathbf{u}^{n+1} = (I + \Delta\tau A)\mathbf{u}^n
    $$

    This is exactly the forward Euler (explicit) scheme.

    **$\theta = 1$ (implicit scheme)**: The left side becomes $(I - \Delta\tau A)\mathbf{u}^{n+1}$ and the right side becomes $I\mathbf{u}^n = \mathbf{u}^n$, giving:

    $$
    (I - \Delta\tau A)\mathbf{u}^{n+1} = \mathbf{u}^n
    $$

    This is exactly the backward Euler (implicit) scheme.

    **$\theta = 1/2$ (Crank-Nicolson)**: The scheme becomes:

    $$
    \left(I - \frac{\Delta\tau}{2}A\right)\mathbf{u}^{n+1} = \left(I + \frac{\Delta\tau}{2}A\right)\mathbf{u}^n
    $$

    This is the Crank-Nicolson scheme. It is second-order accurate in time because it is equivalent to the trapezoidal rule for the ODE system $d\mathbf{u}/d\tau = A\mathbf{u}$. The trapezoidal rule approximates:

    $$
    \mathbf{u}^{n+1} = \mathbf{u}^n + \frac{\Delta\tau}{2}\left(A\mathbf{u}^n + A\mathbf{u}^{n+1}\right)
    $$

    To see the order of accuracy, consider the scalar ODE $du/d\tau = \lambda u$. The exact solution satisfies $u(\tau + \Delta\tau) = e^{\lambda\Delta\tau}u(\tau)$. The trapezoidal rule gives amplification factor:

    $$
    R(z) = \frac{1 + z/2}{1 - z/2}
    $$

    where $z = \lambda\Delta\tau$. The Taylor expansion is $R(z) = 1 + z + z^2/2 + z^3/4 + \cdots$ while $e^z = 1 + z + z^2/2 + z^3/6 + \cdots$, so $R(z) - e^z = O(z^3)$, confirming second-order accuracy (the local truncation error is $O((\Delta\tau)^3)$, giving global error $O((\Delta\tau)^2)$).

---

**Exercise 3.** Write out the Thomas algorithm (forward sweep and back substitution) for solving a tridiagonal system of size $M - 1 = 4$. Count the total number of multiplications and divisions and confirm the $O(M)$ cost.

??? success "Solution to Exercise 3"
    For a tridiagonal system of size $4$:

    $$
    \begin{pmatrix} \beta_1 & \gamma_1 & 0 & 0 \\ \alpha_2 & \beta_2 & \gamma_2 & 0 \\ 0 & \alpha_3 & \beta_3 & \gamma_3 \\ 0 & 0 & \alpha_4 & \beta_4 \end{pmatrix} \begin{pmatrix} u_1 \\ u_2 \\ u_3 \\ u_4 \end{pmatrix} = \begin{pmatrix} d_1 \\ d_2 \\ d_3 \\ d_4 \end{pmatrix}
    $$

    **Forward sweep**:

    Step 1 ($j=1$): $c'_1 = \gamma_1/\beta_1$ (1 division), $d'_1 = d_1/\beta_1$ (1 division).

    Step 2 ($j=2$): $w_2 = \beta_2 - \alpha_2 c'_1$ (1 multiply, 1 subtract), $c'_2 = \gamma_2/w_2$ (1 division), $d'_2 = (d_2 - \alpha_2 d'_1)/w_2$ (1 multiply, 1 subtract, 1 division).

    Step 3 ($j=3$): Same as step 2: 2 multiplications, 2 subtractions, 2 divisions.

    Step 4 ($j=4$): $w_4 = \beta_4 - \alpha_4 c'_3$ (1 multiply, 1 subtract), $d'_4 = (d_4 - \alpha_4 d'_3)/w_4$ (1 multiply, 1 subtract, 1 division). No $c'_4$ needed.

    **Back substitution**:

    Step 1: $u_4 = d'_4$ (0 operations).

    Step 2 ($j=3$): $u_3 = d'_3 - c'_3 u_4$ (1 multiply, 1 subtract).

    Step 3 ($j=2$): $u_2 = d'_2 - c'_2 u_3$ (1 multiply, 1 subtract).

    Step 4 ($j=1$): $u_1 = d'_1 - c'_1 u_2$ (1 multiply, 1 subtract).

    **Operation count**: Counting multiplications and divisions:

    - Forward sweep: $j=1$: 2; $j=2$: 4; $j=3$: 4; $j=4$: 3. Total: 13.
    - Back substitution: 3 multiplications. Total: 3.
    - Grand total: 16 multiplications/divisions.

    For general size $M-1$: the forward sweep uses $2$ operations for $j=1$ and $4$ for each subsequent row except the last which uses $3$, and back substitution uses $M-2$ operations. The total is $O(M)$, confirming linear cost. Specifically, the Thomas algorithm requires approximately $8(M-1)$ floating-point operations, which is $O(M)$.

---

**Exercise 4.** Explain the Rannacher time-stepping strategy. Why does the Crank-Nicolson scheme produce oscillations near $\tau = 0$ when the initial data has a kink? How do a few initial implicit steps suppress these oscillations while maintaining overall second-order accuracy?

??? success "Solution to Exercise 4"
    **Rannacher time-stepping** uses a few fully implicit (backward Euler) steps at the start of the time integration, then switches to Crank-Nicolson for the remaining steps.

    **Why Crank-Nicolson oscillates**: When the initial data $u(0, S) = (S - K)^+$ has a kink at $S = K$, the initial condition contains high-frequency Fourier components. The Crank-Nicolson amplification factor for a mode with eigenvalue $\lambda$ is:

    $$
    R(\lambda\Delta\tau) = \frac{1 + \lambda\Delta\tau/2}{1 - \lambda\Delta\tau/2}
    $$

    For large negative $\lambda$ (high-frequency spatial modes), $R \to -1$. This means high-frequency components are not damped but instead oscillate in sign at each time step, producing spurious oscillations in the solution near the kink.

    **How implicit steps help**: The backward Euler amplification factor is:

    $$
    R(\lambda\Delta\tau) = \frac{1}{1 - \lambda\Delta\tau}
    $$

    For large negative $\lambda$, $R \to 0$. Thus the implicit scheme is $L$-stable and strongly damps high-frequency modes. After 2-4 implicit steps, the high-frequency content of the initial kink has been sufficiently smoothed, and the solution is regular enough for Crank-Nicolson to proceed without oscillation.

    **Why overall second-order accuracy is maintained**: Suppose we take $p$ implicit steps (each of size $\Delta\tau$) followed by $(N - p)$ Crank-Nicolson steps. The implicit steps introduce local error $O((\Delta\tau)^2)$ per step, accumulating to $O(p(\Delta\tau)^2)$ over $p$ steps. Since $p$ is a fixed constant (independent of $N$), this contributes $O((\Delta\tau)^2)$ to the global error. The Crank-Nicolson steps contribute $O((\Delta\tau)^2)$ globally as well. The combined global error remains $O((\Delta\tau)^2)$, preserving second-order convergence.

---

**Exercise 5.** Consider a European call with $K = 100$ priced using both the explicit and implicit schemes with $M = 100$ spatial points. If the explicit scheme requires $N = 5000$ time steps (due to the CFL condition) while the implicit scheme uses $N = 100$, compare the total computational costs. Which scheme is more efficient, and by what factor?

??? success "Solution to Exercise 5"
    Both schemes have the same spatial discretization with $M = 100$ points, so the cost per time step is $O(M) = O(100)$ for both (the implicit scheme uses the Thomas algorithm, which is also $O(M)$).

    **Explicit scheme**: $N = 5000$ time steps, each costing $O(M)$ operations.

    $$
    \text{Total cost (explicit)} = 5000 \times O(100) = O(500{,}000)
    $$

    **Implicit scheme**: $N = 100$ time steps, each costing $O(M)$ operations.

    $$
    \text{Total cost (implicit)} = 100 \times O(100) = O(10{,}000)
    $$

    The implicit scheme is more efficient by a factor of:

    $$
    \frac{500{,}000}{10{,}000} = 50
    $$

    The implicit scheme is **50 times** more efficient. This dramatic difference arises because the explicit scheme's CFL condition forces $\Delta\tau = O((\Delta S)^2)$, requiring $N = O(1/(\Delta S)^2)$ steps, while the implicit scheme is unconditionally stable and can use $N = O(1/\Delta\tau_{\text{accuracy}})$ steps based purely on accuracy requirements. For this example, the accuracy-driven step count ($N = 100$) is far smaller than the stability-driven count ($N = 5000$).

---

**Exercise 6.** For the implicit scheme, the linear system $(I - \Delta\tau A)\mathbf{u}^{n+1} = \mathbf{u}^n$ involves a tridiagonal matrix. Explain why this matrix is an M-matrix (positive diagonal, non-positive off-diagonal, non-singular with non-negative inverse). Why does the M-matrix property guarantee that the numerical solution preserves the non-negativity of option prices?

??? success "Solution to Exercise 6"
    The matrix $B = I - \Delta\tau A$ arises from the implicit scheme. Recall that $A$ is the tridiagonal spatial operator with entries arising from the finite difference discretization. For the Black-Scholes PDE, the entries of $A$ at row $j$ are:

    - Sub-diagonal: $\alpha_j = \frac{1}{2}\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} - \frac{rS_j}{\Delta S}\right)$
    - Diagonal: $\delta_j = -\frac{\sigma^2 S_j^2}{(\Delta S)^2} - r$
    - Super-diagonal: $\gamma_j = \frac{1}{2}\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} + \frac{rS_j}{\Delta S}\right)$

    The matrix $B = I - \Delta\tau A$ has entries:

    - Diagonal: $1 - \Delta\tau\,\delta_j = 1 + \Delta\tau\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} + r\right) > 0$
    - Off-diagonal: $-\Delta\tau\,\alpha_j$ and $-\Delta\tau\,\gamma_j$

    Since $\gamma_j > 0$ for all $j$ (both terms in $\gamma_j$ are positive), we have $-\Delta\tau\,\gamma_j < 0$. The sub-diagonal term $-\Delta\tau\,\alpha_j$ is non-positive when $\alpha_j \geq 0$, which holds when $\sigma^2 S_j/(\Delta S) \geq r$ (typically satisfied for reasonable grid sizes). Under this condition, $B$ has positive diagonal and non-positive off-diagonal entries.

    **Diagonal dominance**: The diagonal entry satisfies:

    $$
    1 + \Delta\tau\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} + r\right) > \Delta\tau\left(\alpha_j + \gamma_j\right) = \Delta\tau\cdot\frac{\sigma^2 S_j^2}{(\Delta S)^2}
    $$

    since $1 + r\Delta\tau > 0$. This gives strict diagonal dominance, which implies $B$ is non-singular. A matrix that has positive diagonal, non-positive off-diagonal, and is diagonally dominant is a (non-singular) M-matrix with $B^{-1} \geq 0$ (all entries of the inverse are non-negative).

    **Preservation of non-negativity**: Since $B^{-1} \geq 0$ entry-wise, the update

    $$
    \mathbf{u}^{n+1} = B^{-1}\mathbf{u}^n
    $$

    maps non-negative vectors to non-negative vectors. If $\mathbf{u}^0 \geq 0$ (which holds since the payoff is non-negative), then $\mathbf{u}^n \geq 0$ for all $n$ by induction. This guarantees that the numerical option price remains non-negative at every grid point and every time step, which is physically required since option prices cannot be negative.
