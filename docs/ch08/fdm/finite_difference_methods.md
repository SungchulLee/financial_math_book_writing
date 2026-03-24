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

---

**Exercise 2.** Consider the log-price transformation $x = \ln S$. Starting from the Black-Scholes PDE in the original $(t, S)$ variables, carry out the change of variables to derive the transformed PDE

$$
\frac{\partial u}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial u}{\partial x} - ru
$$

Explain why the constant coefficients in this PDE are an advantage for numerical computation.

---

**Exercise 3.** For a European put option with $K = 100$, $r = 0.05$, and $T = 1$, write down the boundary conditions at $S = 0$ and $S = S_{\max} = 300$ in both Dirichlet and Neumann forms. Discuss when each type is appropriate.

---

**Exercise 4.** Set up the tridiagonal matrix $A$ for the explicit scheme with $M = 4$ interior grid points ($j = 1, 2, 3, 4$) on $[0, S_{\max}]$ with $S_{\max} = 200$, $\sigma = 0.2$, $r = 0.05$, and $\Delta\tau = 0.001$. Compute the numerical values of the coefficients $a_j$, $b_j$, $c_j$ for each interior node. Are all coefficients non-negative?

---

**Exercise 5.** A grid for pricing a European call uses $S_{\max} = 3K$. Argue qualitatively why this choice of $S_{\max}$ is appropriate for vanilla options. What happens to the truncation error if $S_{\max}$ is too small? What happens to the stability condition if $S_{\max}$ is too large?

---

**Exercise 6.** The coordinate stretching formula $S_j = K\sinh((j - M/2)\alpha/(M/2))/\sinh(\alpha) + K$ concentrates grid points near the strike. For $K = 100$, $M = 100$, and $\alpha = 3$, compute $S_{45}$, $S_{50}$, and $S_{55}$, and compare the local spacing near $K$ to the uniform spacing $\Delta S = S_{\max}/M$ that would be needed for the same number of grid points on $[0, 300]$.

---

**Exercise 7.** The payoff $(S - K)^+$ has a kink at $S = K$. Explain why placing a grid point exactly at $S = K$ improves accuracy. If $\Delta S = 1.5$ and $K = 100$, does the uniform grid $S_j = j\Delta S$ place a node at the strike? If not, suggest a modified grid spacing that does.
