# Finite Difference Methods

Finite difference methods approximate the Black-Scholes PDE by replacing continuous derivatives with discrete differences on a computational grid. This transforms the PDE into a system of algebraic equations that can be solved numerically.

---

## The Black-Scholes PDE

For an option price $V(t,S)$ with no dividends:

$$
\boxed{
\frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
}
$$

with terminal condition $V(T,S) = \Phi(S)$ and appropriate boundary conditions.

---

## Time-to-Maturity Formulation

Define $\tau = T - t$ (time to maturity) and $u(\tau, S) = V(T-\tau, S)$.

The PDE becomes a **forward** problem:

$$
\boxed{
\frac{\partial u}{\partial \tau} = \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2} + rS\frac{\partial u}{\partial S} - ru
}
$$

with **initial** condition $u(0,S) = \Phi(S)$.

This is the standard form for numerical solution: march forward from $\tau = 0$.

---

## Grid Construction

### Spatial Grid

Truncate the infinite domain $(0, \infty)$ to $[0, S_{\max}]$ and discretize:

$$
S_j = j \cdot \Delta S, \quad j = 0, 1, \ldots, M
$$

where $\Delta S = S_{\max}/M$.

### Temporal Grid

$$
\tau_n = n \cdot \Delta\tau, \quad n = 0, 1, \ldots, N
$$

where $\Delta\tau = T/N$.

### Grid Notation

Let $u_j^n \approx u(\tau_n, S_j)$ denote the numerical approximation.

---

## Derivative Approximations

### First Derivative (Central Difference)

$$
\boxed{
\frac{\partial u}{\partial S}\bigg|_{S_j} \approx \frac{u_{j+1} - u_{j-1}}{2\Delta S}
}
$$

**Accuracy**: $O((\Delta S)^2)$

### First Derivative (One-Sided)

Forward: $\frac{u_{j+1} - u_j}{\Delta S}$, Backward: $\frac{u_j - u_{j-1}}{\Delta S}$

**Accuracy**: $O(\Delta S)$

### Second Derivative

$$
\boxed{
\frac{\partial^2 u}{\partial S^2}\bigg|_{S_j} \approx \frac{u_{j+1} - 2u_j + u_{j-1}}{(\Delta S)^2}
}
$$

**Accuracy**: $O((\Delta S)^2)$

### Time Derivative

$$
\frac{\partial u}{\partial \tau}\bigg|_{\tau_n} \approx \frac{u^{n+1} - u^n}{\Delta\tau}
$$

---

## The Semi-Discrete System

Substituting finite differences into the PDE at node $(n, j)$:

$$
\frac{u_j^{n+1} - u_j^n}{\Delta\tau} = \frac{1}{2}\sigma^2 S_j^2 \frac{u_{j+1}^n - 2u_j^n + u_{j-1}^n}{(\Delta S)^2} + rS_j\frac{u_{j+1}^n - u_{j-1}^n}{2\Delta S} - ru_j^n
$$

### Coefficient Form

Define coefficients:

$$
a_j = \frac{\Delta\tau}{2}\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} - \frac{rS_j}{\Delta S}\right)
$$

$$
b_j = -\Delta\tau\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} + r\right)
$$

$$
c_j = \frac{\Delta\tau}{2}\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} + \frac{rS_j}{\Delta S}\right)
$$

The explicit scheme becomes:

$$
u_j^{n+1} = a_j u_{j-1}^n + (1 + b_j)u_j^n + c_j u_{j+1}^n
$$

---

## Matrix Formulation

Let $\mathbf{u}^n = (u_1^n, u_2^n, \ldots, u_{M-1}^n)^T$ (excluding boundary nodes).

The scheme can be written as:

$$
\mathbf{u}^{n+1} = A\mathbf{u}^n + \mathbf{b}^n
$$

where $A$ is a **tridiagonal matrix** and $\mathbf{b}^n$ incorporates boundary conditions.

$$
A = \begin{pmatrix}
1+b_1 & c_1 & 0 & \cdots \\
a_2 & 1+b_2 & c_2 & \cdots \\
0 & a_3 & 1+b_3 & \cdots \\
\vdots & & \ddots & \ddots
\end{pmatrix}
$$

---

## Log-Price Transformation

Using $x = \log S$ often improves numerical behavior.

### Transformed PDE

$$
\frac{\partial u}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial u}{\partial x} - ru
$$

### Advantages

1. **Constant diffusion coefficient**: $\frac{\sigma^2}{2}$ instead of $\frac{\sigma^2 S^2}{2}$
2. **Uniform grid in $x$** corresponds to geometric spacing in $S$
3. Better resolution for small $S$ (important for puts)
4. Removes one source of spatial variation in coefficients

### Grid in Log-Space

$$
x_j = x_{\min} + j\Delta x, \quad S_j = e^{x_j}
$$

---

## Boundary Conditions

### At S = 0 (or x → -∞)

**Call**: $V(t, 0) = 0$

**Put**: $V(t, 0) = Ke^{-r(T-t)}$

### At S = S_max (or x = x_max)

**Call**: $V(t, S_{\max}) \approx S_{\max} - Ke^{-r(T-t)}$

**Put**: $V(t, S_{\max}) \approx 0$

### Neumann (Derivative) Conditions

For large $S$, call delta approaches 1:

$$
\frac{\partial V}{\partial S}(t, S_{\max}) = 1
$$

Implemented using one-sided differences or ghost points.

---

## Implementation Considerations

### Grid Sizing

**Rule of thumb**:

- $S_{\max} \approx 3K$ to $5K$ for vanilla options
- $\Delta S$ small enough to resolve payoff kink at $K$
- Place grid point exactly at strike $K$

### Payoff Smoothing

The payoff $(S-K)^+$ has a kink at $S = K$, causing accuracy issues.

**Remedies**:

1. Use fine grid near $K$
2. Apply payoff smoothing
3. Use Rannacher time-stepping

### Coordinate Stretching

Non-uniform grids concentrate points where needed:

$$
S_j = K \sinh\left(\frac{j - M/2}{M/2} \cdot \alpha\right) / \sinh(\alpha) + K
$$

---

## Algorithm Summary

```
1. Set up grid: S_j, τ_n
2. Initialize: u_j^0 = Φ(S_j)  (payoff)
3. For n = 0, 1, ..., N-1:
   a. Apply time-stepping scheme
   b. Enforce boundary conditions
4. Return: V(0, S) = u^N
```

---

## Summary

| Aspect | Choice |
|--------|--------|
| Coordinates | $S$ (direct) or $x = \log S$ (transformed) |
| Derivatives | Central differences (2nd order) |
| Time stepping | Explicit, implicit, or Crank-Nicolson |
| Boundary | Dirichlet or Neumann |
| Grid | Uniform or stretched |

$$
\boxed{
\frac{u_j^{n+1} - u_j^n}{\Delta\tau} = \frac{\sigma^2 S_j^2}{2}\frac{u_{j+1} - 2u_j + u_{j-1}}{(\Delta S)^2} + rS_j\frac{u_{j+1} - u_{j-1}}{2\Delta S} - ru_j
}
$$

**Finite differences convert the PDE into a structured linear algebra problem amenable to efficient numerical solution.**

---

## Exercises

**Exercise 1.** Starting from the Black-Scholes PDE in the time-to-maturity formulation, derive the explicit scheme coefficients $a_j$, $b_j$, $c_j$ by substituting central difference approximations for $\partial u/\partial S$ and $\partial^2 u/\partial S^2$, and a forward difference for $\partial u/\partial\tau$. Verify that $a_j + (1 + b_j) + c_j = 1$ and interpret this condition.

??? success "Solution to Exercise 1"
    Starting from the time-to-maturity PDE:

    $$
    \frac{\partial u}{\partial \tau} = \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 u}{\partial S^2} + rS\frac{\partial u}{\partial S} - ru
    $$

    Substitute the forward difference for the time derivative:

    $$
    \frac{u_j^{n+1} - u_j^n}{\Delta\tau}
    $$

    the central difference for the first spatial derivative:

    $$
    \frac{\partial u}{\partial S}\bigg|_{S_j} \approx \frac{u_{j+1}^n - u_{j-1}^n}{2\Delta S}
    $$

    and the central second difference:

    $$
    \frac{\partial^2 u}{\partial S^2}\bigg|_{S_j} \approx \frac{u_{j+1}^n - 2u_j^n + u_{j-1}^n}{(\Delta S)^2}
    $$

    Substituting into the PDE and solving for $u_j^{n+1}$:

    $$
    u_j^{n+1} = u_j^n + \Delta\tau\left[\frac{\sigma^2 S_j^2}{2}\frac{u_{j+1}^n - 2u_j^n + u_{j-1}^n}{(\Delta S)^2} + rS_j\frac{u_{j+1}^n - u_{j-1}^n}{2\Delta S} - ru_j^n\right]
    $$

    Collecting terms by $u_{j-1}^n$, $u_j^n$, and $u_{j+1}^n$:

    $$
    a_j = \frac{\Delta\tau}{2}\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} - \frac{rS_j}{\Delta S}\right)
    $$

    $$
    b_j = -\Delta\tau\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} + r\right)
    $$

    $$
    c_j = \frac{\Delta\tau}{2}\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} + \frac{rS_j}{\Delta S}\right)
    $$

    Now verify $a_j + (1 + b_j) + c_j$:

    $$
    a_j + c_j = \frac{\Delta\tau}{2}\cdot\frac{\sigma^2 S_j^2}{(\Delta S)^2} - \frac{\Delta\tau}{2}\cdot\frac{rS_j}{\Delta S} + \frac{\Delta\tau}{2}\cdot\frac{\sigma^2 S_j^2}{(\Delta S)^2} + \frac{\Delta\tau}{2}\cdot\frac{rS_j}{\Delta S} = \Delta\tau\cdot\frac{\sigma^2 S_j^2}{(\Delta S)^2}
    $$

    $$
    a_j + (1 + b_j) + c_j = \Delta\tau\cdot\frac{\sigma^2 S_j^2}{(\Delta S)^2} + 1 - \Delta\tau\cdot\frac{\sigma^2 S_j^2}{(\Delta S)^2} - \Delta\tau\cdot r = 1 - r\Delta\tau
    $$

    Wait — re-examining, note that $a_j + (1+b_j) + c_j = 1 + (a_j + b_j + c_j)$. Computing $a_j + b_j + c_j$:

    $$
    a_j + b_j + c_j = \Delta\tau\cdot\frac{\sigma^2 S_j^2}{(\Delta S)^2} - \Delta\tau\cdot\frac{\sigma^2 S_j^2}{(\Delta S)^2} - \Delta\tau r = -r\Delta\tau
    $$

    Hence $a_j + (1+b_j) + c_j = 1 - r\Delta\tau$.

    **Interpretation**: The row sums equal $1 - r\Delta\tau$ rather than $1$. This reflects the discounting inherent in the Black-Scholes PDE: the term $-rV$ causes the solution to be discounted at rate $r$. If $r = 0$, the row sums are exactly $1$, which corresponds to a probability-preserving scheme. The condition $a_j + (1+b_j) + c_j = 1 - r\Delta\tau$ ensures consistency with the PDE.

---

**Exercise 2.** Consider the log-price transformation $x = \ln S$. Starting from the Black-Scholes PDE in the original $(t, S)$ variables, carry out the change of variables to derive the transformed PDE

$$
\frac{\partial u}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial u}{\partial x} - ru
$$

Explain why the constant coefficients in this PDE are an advantage for numerical computation.

??? success "Solution to Exercise 2"
    Starting from the Black-Scholes PDE in original variables:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} + rS\frac{\partial V}{\partial S} - rV = 0
    $$

    Let $x = \ln S$, so $S = e^x$. By the chain rule:

    $$
    \frac{\partial V}{\partial S} = \frac{\partial V}{\partial x}\cdot\frac{dx}{dS} = \frac{1}{S}\frac{\partial V}{\partial x}
    $$

    For the second derivative:

    $$
    \frac{\partial^2 V}{\partial S^2} = \frac{\partial}{\partial S}\left(\frac{1}{S}\frac{\partial V}{\partial x}\right) = -\frac{1}{S^2}\frac{\partial V}{\partial x} + \frac{1}{S^2}\frac{\partial^2 V}{\partial x^2}
    $$

    Substituting into the PDE:

    $$
    \frac{\partial V}{\partial t} + \frac{\sigma^2 S^2}{2}\left(\frac{1}{S^2}\frac{\partial^2 V}{\partial x^2} - \frac{1}{S^2}\frac{\partial V}{\partial x}\right) + rS\cdot\frac{1}{S}\frac{\partial V}{\partial x} - rV = 0
    $$

    Simplifying:

    $$
    \frac{\partial V}{\partial t} + \frac{\sigma^2}{2}\frac{\partial^2 V}{\partial x^2} - \frac{\sigma^2}{2}\frac{\partial V}{\partial x} + r\frac{\partial V}{\partial x} - rV = 0
    $$

    $$
    \frac{\partial V}{\partial t} + \frac{\sigma^2}{2}\frac{\partial^2 V}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial V}{\partial x} - rV = 0
    $$

    Switching to $\tau = T - t$ and $u(\tau, x) = V(T - \tau, e^x)$, so $\frac{\partial u}{\partial \tau} = -\frac{\partial V}{\partial t}$:

    $$
    \frac{\partial u}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial u}{\partial x} - ru
    $$

    **Advantages of constant coefficients**: In the original PDE, the diffusion coefficient $\frac{1}{2}\sigma^2 S^2$ and the convection coefficient $rS$ both depend on $S$, so the finite difference coefficients $a_j$, $b_j$, $c_j$ vary with the spatial index $j$. After the log transformation, all coefficients are constants ($\frac{\sigma^2}{2}$, $r - \frac{\sigma^2}{2}$, and $r$), so the tridiagonal matrix $A$ has the same entries along each diagonal. This simplifies implementation, improves conditioning, and allows a uniform grid in $x$ that provides better resolution near $S = 0$ (since equal steps in $\ln S$ correspond to geometric spacing in $S$).

---

**Exercise 3.** For a European put option with $K = 100$, $r = 0.05$, and $T = 1$, write down the boundary conditions at $S = 0$ and $S = S_{\max} = 300$ in both Dirichlet and Neumann forms. Discuss when each type is appropriate.

??? success "Solution to Exercise 3"
    For a European put with $K = 100$, $r = 0.05$, $T = 1$:

    **Dirichlet boundary conditions at $S = 0$**:

    $$
    V(t, 0) = Ke^{-r(T-t)} = 100\,e^{-0.05(1-t)}
    $$

    At $t = 0$: $V(0, 0) = 100\,e^{-0.05} \approx 95.12$.

    At $t = 0.5$: $V(0.5, 0) = 100\,e^{-0.025} \approx 97.53$.

    At $t = 1$: $V(1, 0) = 100\,e^{0} = 100$.

    **Dirichlet boundary conditions at $S_{\max} = 300$**:

    $$
    V(t, 300) \approx 0
    $$

    for all $t$, since the put is deep out of the money when $S = 300 \gg K = 100$.

    **Neumann boundary conditions at $S = 0$**: For a put, $\Delta \to -1$ as $S \to 0$, so

    $$
    \frac{\partial V}{\partial S}(t, 0) = -1
    $$

    However, the Dirichlet condition at $S = 0$ is exact for a put (the asset becomes worthless, and the put pays $K$ at maturity discounted to time $t$), so it is preferred.

    **Neumann boundary conditions at $S_{\max} = 300$**: For a put, $\Delta \to 0$ as $S \to \infty$, so

    $$
    \frac{\partial V}{\partial S}(t, S_{\max}) \approx 0
    $$

    **When each type is appropriate**: Dirichlet conditions are preferred when the boundary value is known exactly (e.g., put at $S = 0$). Neumann conditions are useful at the far boundary when the exact value is uncertain or when the truncation domain may not be large enough — specifying the derivative is more robust than guessing the function value. For the put at $S_{\max} = 300$, both $V \approx 0$ and $V_S \approx 0$ are reasonable. For a call at $S_{\max}$, the Neumann condition $V_S = 1$ may be more robust than the Dirichlet approximation $V \approx S_{\max} - Ke^{-r(T-t)}$.

---

**Exercise 4.** Set up the tridiagonal matrix $A$ for the explicit scheme with $M = 4$ interior grid points ($j = 1, 2, 3, 4$) on $[0, S_{\max}]$ with $S_{\max} = 200$, $\sigma = 0.2$, $r = 0.05$, and $\Delta\tau = 0.001$. Compute the numerical values of the coefficients $a_j$, $b_j$, $c_j$ for each interior node. Are all coefficients non-negative?

??? success "Solution to Exercise 4"
    Given: $M = 4$ interior points on $[0, S_{\max}]$ with $S_{\max} = 200$, $\sigma = 0.2$, $r = 0.05$, $\Delta\tau = 0.001$.

    The grid has $M + 1 = 5$ intervals, so $\Delta S = 200/5 = 40$ and the nodes are $S_0 = 0$, $S_1 = 40$, $S_2 = 80$, $S_3 = 120$, $S_4 = 160$, $S_5 = 200$.

    The coefficients are:

    $$
    a_j = \frac{\Delta\tau}{2}\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} - \frac{rS_j}{\Delta S}\right), \quad
    b_j = -\Delta\tau\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} + r\right), \quad
    c_j = \frac{\Delta\tau}{2}\left(\frac{\sigma^2 S_j^2}{(\Delta S)^2} + \frac{rS_j}{\Delta S}\right)
    $$

    For $j = 1$ ($S_1 = 40$): $\frac{\sigma^2 S_1^2}{(\Delta S)^2} = \frac{0.04 \times 1600}{1600} = 0.04$, $\frac{rS_1}{\Delta S} = \frac{0.05 \times 40}{40} = 0.05$.

    $$
    a_1 = \frac{0.001}{2}(0.04 - 0.05) = -0.000005
    $$

    $$
    b_1 = -0.001(0.04 + 0.05) = -0.00009
    $$

    $$
    c_1 = \frac{0.001}{2}(0.04 + 0.05) = 0.000045
    $$

    For $j = 2$ ($S_2 = 80$): $\frac{\sigma^2 S_2^2}{(\Delta S)^2} = \frac{0.04 \times 6400}{1600} = 0.16$, $\frac{rS_2}{\Delta S} = \frac{0.05 \times 80}{40} = 0.10$.

    $$
    a_2 = \frac{0.001}{2}(0.16 - 0.10) = 0.00003
    $$

    $$
    b_2 = -0.001(0.16 + 0.05) = -0.00021
    $$

    $$
    c_2 = \frac{0.001}{2}(0.16 + 0.10) = 0.00013
    $$

    For $j = 3$ ($S_3 = 120$): $\frac{\sigma^2 S_3^2}{(\Delta S)^2} = \frac{0.04 \times 14400}{1600} = 0.36$, $\frac{rS_3}{\Delta S} = \frac{0.05 \times 120}{40} = 0.15$.

    $$
    a_3 = \frac{0.001}{2}(0.36 - 0.15) = 0.000105
    $$

    $$
    b_3 = -0.001(0.36 + 0.05) = -0.00041
    $$

    $$
    c_3 = \frac{0.001}{2}(0.36 + 0.15) = 0.000255
    $$

    For $j = 4$ ($S_4 = 160$): $\frac{\sigma^2 S_4^2}{(\Delta S)^2} = \frac{0.04 \times 25600}{1600} = 0.64$, $\frac{rS_4}{\Delta S} = \frac{0.05 \times 160}{40} = 0.20$.

    $$
    a_4 = \frac{0.001}{2}(0.64 - 0.20) = 0.00022
    $$

    $$
    b_4 = -0.001(0.64 + 0.05) = -0.00069
    $$

    $$
    c_4 = \frac{0.001}{2}(0.64 + 0.20) = 0.00042
    $$

    The tridiagonal matrix $A$ is:

    $$
    A = \begin{pmatrix}
    1 + b_1 & c_1 & 0 & 0 \\
    a_2 & 1 + b_2 & c_2 & 0 \\
    0 & a_3 & 1 + b_3 & c_3 \\
    0 & 0 & a_4 & 1 + b_4
    \end{pmatrix}
    $$

    $$
    = \begin{pmatrix}
    0.99991 & 0.000045 & 0 & 0 \\
    0.00003 & 0.99979 & 0.00013 & 0 \\
    0 & 0.000105 & 0.99959 & 0.000255 \\
    0 & 0 & 0.00022 & 0.99931
    \end{pmatrix}
    $$

    **Are all coefficients non-negative?** No. The coefficient $a_1 = -0.000005 < 0$. This occurs because the convection term $rS_j/\Delta S$ exceeds the diffusion term $\sigma^2 S_j^2/(\Delta S)^2$ at $j = 1$. When coefficients are negative, the scheme may fail to satisfy the discrete maximum principle, potentially producing spurious oscillations or negative option prices. Using the log-price transformation or an upwind scheme would remedy this.

---

**Exercise 5.** A grid for pricing a European call uses $S_{\max} = 3K$. Argue qualitatively why this choice of $S_{\max}$ is appropriate for vanilla options. What happens to the truncation error if $S_{\max}$ is too small? What happens to the stability condition if $S_{\max}$ is too large?

??? success "Solution to Exercise 5"
    **Why $S_{\max} = 3K$ is appropriate**: For a vanilla European option, the region of economic interest is near the strike $K$. Far from the strike, the option value is dominated by its intrinsic value. For a call, as $S \to \infty$, $V \approx S - Ke^{-rT}$ (linear growth), and the Black-Scholes price converges rapidly to this asymptotic form. At $S = 3K$, the option is deep in the money and the pricing error from the boundary approximation $V(t, S_{\max}) \approx S_{\max} - Ke^{-r(T-t)}$ is extremely small. Similarly, for a put, the value is negligible for $S \gg K$.

    **Truncation error if $S_{\max}$ is too small**: The artificial boundary condition imposes an approximate value at $S_{\max}$ that may differ significantly from the true solution. This error propagates inward and contaminates the solution in the region of interest near $S = K$. For a call option, if $S_{\max}$ is only slightly above $K$, the boundary approximation $V \approx S_{\max} - Ke^{-rT}$ ignores the time value, introducing a significant systematic error.

    **Stability impact if $S_{\max}$ is too large**: For the explicit scheme, the CFL stability condition is

    $$
    \Delta\tau \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2}
    $$

    If $S_{\max}$ increases while keeping the number of grid points $M$ fixed, then $\Delta S = S_{\max}/M$ increases, but $S_{\max}^2$ grows faster than $(\Delta S)^2$. Specifically, the bound becomes $\Delta\tau \leq \frac{S_{\max}^2/M^2}{\sigma^2 S_{\max}^2} = \frac{1}{\sigma^2 M^2}$, which is independent of $S_{\max}$. However, if one keeps $\Delta S$ fixed and increases $S_{\max}$, then $M = S_{\max}/\Delta S$ increases, and more importantly the maximum eigenvalue of the spatial operator grows with $S_{\max}^2$, making the stability constraint much more restrictive. Additionally, a larger domain with fixed grid resolution reduces accuracy near the strike. The choice $S_{\max} = 3K$ to $5K$ balances accuracy and computational efficiency.

---

**Exercise 6.** The coordinate stretching formula $S_j = K\sinh((j - M/2)\alpha/(M/2))/\sinh(\alpha) + K$ concentrates grid points near the strike. For $K = 100$, $M = 100$, and $\alpha = 3$, compute $S_{45}$, $S_{50}$, and $S_{55}$, and compare the local spacing near $K$ to the uniform spacing $\Delta S = S_{\max}/M$ that would be needed for the same number of grid points on $[0, 300]$.

??? success "Solution to Exercise 6"
    The formula is $S_j = K\sinh\!\bigl((j - M/2)\alpha/(M/2)\bigr)/\sinh(\alpha) + K$ with $K = 100$, $M = 100$, $\alpha = 3$.

    For $j = 50$: $(j - M/2) = 0$, so $\sinh(0) = 0$ and

    $$
    S_{50} = 100 \cdot \frac{0}{\sinh(3)} + 100 = 100
    $$

    For $j = 45$: $(j - M/2) = -5$, and $(j - M/2)\alpha/(M/2) = -5 \cdot 3/50 = -0.3$.

    $$
    \sinh(-0.3) = -0.30452, \quad \sinh(3) = 10.01787
    $$

    $$
    S_{45} = 100 \cdot \frac{-0.30452}{10.01787} + 100 = 100 - 3.040 = 96.96
    $$

    For $j = 55$: $(j - M/2) = 5$, and $(j - M/2)\alpha/(M/2) = 0.3$.

    $$
    S_{55} = 100 \cdot \frac{0.30452}{10.01787} + 100 = 100 + 3.040 = 103.04
    $$

    The local spacing near the strike is approximately $S_{55} - S_{45} = 6.08$ over 10 grid intervals, giving an average local spacing of about $0.608$.

    For a uniform grid on $[0, 300]$ with $M = 100$ intervals, $\Delta S = 300/100 = 3.0$.

    The stretched grid achieves a spacing of approximately $0.608$ near the strike, which is about $5\times$ finer than the uniform spacing of $3.0$, without increasing the total number of grid points. This concentration of resolution near $K$ is critical for accurately resolving the payoff kink and option greeks.

---

**Exercise 7.** The payoff $(S - K)^+$ has a kink at $S = K$. Explain why placing a grid point exactly at $S = K$ improves accuracy. If $\Delta S = 1.5$ and $K = 100$, does the uniform grid $S_j = j\Delta S$ place a node at the strike? If not, suggest a modified grid spacing that does.

??? success "Solution to Exercise 7"
    The payoff $(S - K)^+$ has a discontinuous first derivative at $S = K$: the slope jumps from $0$ to $1$. Finite difference approximations of derivatives are based on polynomial interpolation, which assumes smoothness. Near a kink, the interpolation polynomial oscillates or converges slowly, degrading the accuracy of derivative estimates.

    If a grid point sits exactly at $S = K$, the kink is resolved nodally — the payoff values at adjacent nodes lie on one of the two linear pieces, so the finite difference approximation on each side is exact. In contrast, if the kink falls between grid points, the stencil straddles the discontinuity in slope, and the second-derivative approximation

    $$
    \frac{u_{j+1} - 2u_j + u_{j-1}}{(\Delta S)^2}
    $$

    contains an $O(1)$ error rather than the expected $O((\Delta S)^2)$ error.

    For $\Delta S = 1.5$ and $K = 100$: a grid point at $S_j = j \cdot 1.5$ lies at $K$ when $j = 100/1.5 = 66.67$, which is not an integer. Therefore the uniform grid with $\Delta S = 1.5$ does **not** place a node at the strike.

    **Modified grid spacing**: Choose $\Delta S$ so that $K/\Delta S$ is an integer. For instance, $\Delta S = 100/67 \approx 1.4925$ gives $S_{67} = 100$ exactly. Alternatively, use $\Delta S = 2.0$ with $S_{50} = 100$, or $\Delta S = 1.0$ with $S_{100} = 100$. More generally, any $\Delta S = K/m$ for a positive integer $m$ ensures a node at $S = K$. A practical choice close to $1.5$ is $\Delta S = 100/67 \approx 1.4925$ or simply $\Delta S = 1.25 = 100/80$.
