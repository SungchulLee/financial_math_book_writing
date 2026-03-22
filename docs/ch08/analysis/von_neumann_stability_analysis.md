# Von Neumann Stability Analysis

Von Neumann (Fourier) stability analysis determines whether a finite difference scheme amplifies or damps numerical errors over time. By decomposing the error into Fourier modes, we derive precise conditions under which explicit, implicit, and Crank-Nicolson schemes remain stable.

---

## Motivation

Numerical errors are introduced at every time step through truncation and rounding. A scheme is **stable** if these errors do not grow without bound as the computation proceeds. Without stability, even a consistent scheme produces meaningless results.

The key question is: given an error at time level $n$, how large is that error at time level $n+1$?

---

## The Fourier Mode Approach

### Setup

Consider a constant-coefficient PDE on a uniform grid with spacing $\Delta x$. The numerical error $\varepsilon_j^n$ at node $j$ and time level $n$ satisfies the same difference equation as the solution (by linearity).

**Core idea**: Expand the error in a discrete Fourier series:

$$
\varepsilon_j^n = \sum_k \hat{\varepsilon}_k^n \, e^{i k j \Delta x}
$$

where $k$ ranges over the discrete wavenumbers. By linearity, it suffices to analyze a single Fourier mode:

$$
\varepsilon_j^n = g^n \, e^{i \xi j}
$$

where $\xi = k \Delta x \in [-\pi, \pi]$ is the scaled wavenumber and $g = g(\xi)$ is the **amplification factor**.

### Stability Criterion

!!! info "Von Neumann Stability Condition"
    A scheme is stable if and only if the amplification factor satisfies

    $$
    |g(\xi)| \leq 1 + C\Delta\tau
    $$

    for all $\xi \in [-\pi, \pi]$ and some constant $C$ independent of the mesh.

In practice, for the schemes we consider, the condition simplifies to:

$$
\boxed{|g(\xi)| \leq 1 \quad \text{for all } \xi \in [-\pi, \pi]}
$$

If $|g| > 1$ for any mode, that mode grows exponentially, and the scheme is **unstable**.

---

## Application to the Heat Equation

The model problem for stability analysis is the heat equation:

$$
\frac{\partial u}{\partial \tau} = D \frac{\partial^2 u}{\partial x^2}
$$

where $D > 0$ is the diffusion coefficient. After spatial discretization with central differences, the semi-discrete form at node $j$ is:

$$
\frac{du_j}{d\tau} = D \frac{u_{j+1} - 2u_j + u_{j-1}}{(\Delta x)^2}
$$

Define the **mesh ratio**:

$$
\lambda = \frac{D \Delta\tau}{(\Delta x)^2}
$$

This dimensionless parameter governs stability.

---

## Explicit Scheme (Forward Euler)

### Difference Equation

$$
u_j^{n+1} = u_j^n + \lambda \bigl(u_{j+1}^n - 2u_j^n + u_{j-1}^n\bigr)
$$

### Deriving the Amplification Factor

Substitute the single Fourier mode $\varepsilon_j^n = g^n e^{i\xi j}$:

$$
g^{n+1} e^{i\xi j} = g^n e^{i\xi j} + \lambda g^n \bigl(e^{i\xi(j+1)} - 2e^{i\xi j} + e^{i\xi(j-1)}\bigr)
$$

Dividing both sides by $g^n e^{i\xi j}$:

$$
g = 1 + \lambda \bigl(e^{i\xi} - 2 + e^{-i\xi}\bigr) = 1 + \lambda \bigl(2\cos\xi - 2\bigr)
$$

Using $\cos\xi - 1 = -2\sin^2(\xi/2)$:

$$
\boxed{g = 1 - 4\lambda \sin^2\!\left(\frac{\xi}{2}\right)}
$$

### Stability Analysis

Since $\sin^2(\xi/2) \in [0, 1]$, the amplification factor satisfies:

- **Maximum**: $g = 1$ when $\xi = 0$ (constant mode, always preserved)
- **Minimum**: $g = 1 - 4\lambda$ when $\xi = \pi$ (highest frequency mode)

The condition $|g| \leq 1$ requires:

$$
-1 \leq 1 - 4\lambda \leq 1
$$

The right inequality is always satisfied for $\lambda > 0$. The left inequality gives:

$$
\boxed{\lambda \leq \frac{1}{2} \quad \Longleftrightarrow \quad \Delta\tau \leq \frac{(\Delta x)^2}{2D}}
$$

!!! warning "Conditional Stability"
    The explicit scheme is **conditionally stable**. Violating $\lambda \leq 1/2$ causes the highest-frequency mode ($\xi = \pi$) to grow exponentially, producing oscillatory blow-up.

### Numerical Example

Consider $D = 1$, $\Delta x = 0.01$:

- **Stable**: $\Delta\tau \leq 0.5 \times (0.01)^2 = 5 \times 10^{-5}$
- For $T = 1$, this requires $N \geq 20{,}000$ time steps

---

## Implicit Scheme (Backward Euler)

### Difference Equation

$$
u_j^{n+1} = u_j^n + \lambda \bigl(u_{j+1}^{n+1} - 2u_j^{n+1} + u_{j-1}^{n+1}\bigr)
$$

### Deriving the Amplification Factor

Substitute $\varepsilon_j^n = g^n e^{i\xi j}$:

$$
g^{n+1} e^{i\xi j} = g^n e^{i\xi j} + \lambda g^{n+1} \bigl(e^{i\xi(j+1)} - 2e^{i\xi j} + e^{i\xi(j-1)}\bigr)
$$

Dividing by $g^n e^{i\xi j}$:

$$
g = 1 + \lambda g \bigl(2\cos\xi - 2\bigr) = 1 - 4\lambda g \sin^2\!\left(\frac{\xi}{2}\right)
$$

Solving for $g$:

$$
\boxed{g = \frac{1}{1 + 4\lambda\sin^2(\xi/2)}}
$$

### Stability Analysis

For any $\lambda > 0$ and any $\xi$:

- The denominator satisfies $1 + 4\lambda\sin^2(\xi/2) \geq 1$
- Therefore $0 < g \leq 1$

!!! tip "Unconditional Stability"
    The implicit scheme is **unconditionally stable**: $|g(\xi)| \leq 1$ for all $\lambda > 0$ and all frequencies $\xi$.

The implicit scheme damps all modes. High-frequency modes ($\xi$ near $\pm\pi$) are damped most aggressively:

$$
g(\pi) = \frac{1}{1 + 4\lambda}
$$

For large $\lambda$, this approaches zero, which provides strong smoothing but also introduces excessive numerical dissipation.

---

## Crank-Nicolson Scheme

### Difference Equation

$$
u_j^{n+1} = u_j^n + \frac{\lambda}{2}\bigl(u_{j+1}^n - 2u_j^n + u_{j-1}^n\bigr) + \frac{\lambda}{2}\bigl(u_{j+1}^{n+1} - 2u_j^{n+1} + u_{j-1}^{n+1}\bigr)
$$

### Deriving the Amplification Factor

Substituting the Fourier mode and simplifying:

$$
g = 1 - 2\lambda\sin^2\!\left(\frac{\xi}{2}\right)\bigl(1 + g\bigr)
$$

Let $\mu = 4\lambda\sin^2(\xi/2)$ for brevity. Then $g = 1 - \frac{\mu}{2}(1 + g)$, which gives:

$$
g\left(1 + \frac{\mu}{2}\right) = 1 - \frac{\mu}{2}
$$

$$
\boxed{g = \frac{1 - 2\lambda\sin^2(\xi/2)}{1 + 2\lambda\sin^2(\xi/2)}}
$$

### Stability Analysis

The amplification factor has the form $g = (1 - \alpha)/(1 + \alpha)$ where $\alpha = 2\lambda\sin^2(\xi/2) \geq 0$.

Since $(1-\alpha)/(1+\alpha)$ is a decreasing function with:

- $g = 1$ when $\alpha = 0$
- $g \to -1$ as $\alpha \to \infty$
- $|g| \leq 1$ for all $\alpha \geq 0$

!!! tip "Unconditional Stability"
    The Crank-Nicolson scheme is **unconditionally stable**: $|g(\xi)| \leq 1$ for all $\lambda > 0$.

However, unlike the implicit scheme, $g$ can be **negative** for large $\lambda$. When $\alpha > 1$ (i.e., $2\lambda\sin^2(\xi/2) > 1$), the amplification factor $g < 0$. This means high-frequency modes alternate in sign at successive time steps, producing **oscillatory behavior** without blow-up.

---

## The General Theta-Scheme

The theta-scheme interpolates between explicit ($\theta = 0$), Crank-Nicolson ($\theta = 1/2$), and implicit ($\theta = 1$):

$$
u_j^{n+1} = u_j^n + \lambda\bigl[(1-\theta)(u_{j+1}^n - 2u_j^n + u_{j-1}^n) + \theta(u_{j+1}^{n+1} - 2u_j^{n+1} + u_{j-1}^{n+1})\bigr]
$$

### Amplification Factor

Let $\mu = 4\lambda\sin^2(\xi/2)$:

$$
\boxed{g = \frac{1 - (1-\theta)\mu}{1 + \theta\mu}}
$$

### Stability Conditions

**Case $\theta \geq 1/2$**: The scheme is unconditionally stable. To verify, note:

$$
|g|^2 = \frac{(1 - (1-\theta)\mu)^2}{(1 + \theta\mu)^2} \leq 1
$$

requires $(1 - (1-\theta)\mu)^2 \leq (1 + \theta\mu)^2$. Expanding and simplifying:

$$
\mu(2\theta - 1)(2 + \mu) \geq 0
$$

which holds for all $\mu \geq 0$ when $\theta \geq 1/2$.

**Case $\theta < 1/2$**: The scheme is conditionally stable, requiring:

$$
\lambda \leq \frac{1}{2(1 - 2\theta)}
$$

| $\theta$ | Scheme | Stability | Condition |
|-----------|--------|-----------|-----------|
| $0$ | Explicit | Conditional | $\lambda \leq 1/2$ |
| $1/4$ | --- | Conditional | $\lambda \leq 1$ |
| $1/2$ | Crank-Nicolson | Unconditional | None |
| $1$ | Implicit | Unconditional | None |

---

## Extension to Convection-Diffusion Equations

The Black-Scholes PDE in log-price coordinates takes the form of a convection-diffusion equation:

$$
\frac{\partial u}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 u}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial u}{\partial x} - ru
$$

With central differences for both first and second derivatives, the amplification factor for the explicit scheme becomes:

$$
g = 1 - 4\lambda_D \sin^2\!\left(\frac{\xi}{2}\right) - i \lambda_C \sin\xi
$$

where $\lambda_D = \sigma^2 \Delta\tau / (2(\Delta x)^2)$ is the diffusion mesh ratio and $\lambda_C = (r - \sigma^2/2)\Delta\tau / \Delta x$ is the convection mesh ratio.

### The Mesh Peclet Number

The **mesh Peclet number** measures the relative importance of convection to diffusion at the grid scale:

$$
\text{Pe}_h = \frac{|c|\Delta x}{D} = \frac{|r - \sigma^2/2| \cdot \Delta x}{\sigma^2/2}
$$

When $\text{Pe}_h > 2$, central differences for the first derivative can produce oscillations. Remedies include:

1. **Refining the grid** until $\text{Pe}_h \leq 2$
2. **Upwind differencing**: replace central differences with one-sided differences in the direction of convection
3. **Exponential fitting**: modify coefficients to build the exact solution of a local constant-coefficient problem into the scheme

---

## Black-Scholes in Original Coordinates

For the Black-Scholes PDE written directly in terms of $S$:

$$
\frac{\partial u}{\partial \tau} = \frac{1}{2}\sigma^2 S_j^2 \frac{u_{j+1} - 2u_j + u_{j-1}}{(\Delta S)^2} + rS_j \frac{u_{j+1} - u_{j-1}}{2\Delta S} - ru_j
$$

the coefficients vary with $j$, so **strictly speaking**, von Neumann analysis does not apply globally. However, a **local (frozen-coefficient)** analysis at each node gives insight. At node $j$, define:

$$
\lambda_j = \frac{\sigma^2 S_j^2 \Delta\tau}{2(\Delta S)^2}
$$

The stability condition for the explicit scheme requires $\lambda_j \leq 1/2$ at **every** node, so the binding constraint comes from the node with the largest $S_j$:

$$
\boxed{\Delta\tau \leq \frac{(\Delta S)^2}{\sigma^2 S_{\max}^2}}
$$

This explains why explicit schemes become impractical for large grids when $S_{\max}$ is large.

---

## Relationship to Matrix Stability

Von Neumann analysis and matrix stability analysis are closely related. For the explicit scheme $\mathbf{u}^{n+1} = B\mathbf{u}^n$, stability requires $\rho(B) \leq 1$, where $\rho(B)$ is the spectral radius.

For constant-coefficient problems on periodic domains, the eigenvalues of $B$ are precisely the amplification factors $g(\xi_k)$ evaluated at the discrete wavenumbers:

$$
\xi_k = \frac{2\pi k}{M}, \quad k = 0, 1, \ldots, M-1
$$

Thus:

$$
\rho(B) = \max_k |g(\xi_k)|
$$

Von Neumann analysis computes $\max_\xi |g(\xi)|$ over the continuous range, which bounds the spectral radius. This is why the von Neumann condition is **necessary** for stability and, for constant-coefficient problems, also **sufficient**.

---

## Limitations of Von Neumann Analysis

Von Neumann analysis has important restrictions:

1. **Constant coefficients**: The method assumes frozen coefficients. For variable-coefficient PDEs (Black-Scholes in $S$ coordinates), it provides only a necessary condition
2. **Periodic boundaries**: The Fourier decomposition assumes periodicity. Real problems with Dirichlet or Neumann boundary conditions require additional analysis (e.g., energy methods, GKS theory)
3. **Linear schemes**: The analysis does not apply directly to nonlinear problems such as American option pricing with projection
4. **Single-step methods**: Multi-step methods require a more general analysis involving the root condition

Despite these limitations, von Neumann analysis remains the primary tool for assessing scheme stability in practice. For the Black-Scholes PDE, it provides reliable guidance on time-step restrictions and scheme selection.

---

## Summary

| Scheme | Amplification Factor $g(\xi)$ | Stability |
|--------|-------------------------------|-----------|
| Explicit | $1 - 4\lambda\sin^2(\xi/2)$ | $\lambda \leq 1/2$ |
| Implicit | $\dfrac{1}{1 + 4\lambda\sin^2(\xi/2)}$ | Unconditional |
| Crank-Nicolson | $\dfrac{1 - 2\lambda\sin^2(\xi/2)}{1 + 2\lambda\sin^2(\xi/2)}$ | Unconditional |
| Theta-scheme | $\dfrac{1 - (1-\theta)\mu}{1 + \theta\mu}$ | $\theta \geq 1/2$: unconditional |

$$
\boxed{
\text{Von Neumann criterion: } |g(\xi)| \leq 1 \text{ for all } \xi \in [-\pi, \pi]
}
$$

The explicit scheme's conditional stability ($\lambda \leq 1/2$) imposes a severe time-step restriction for the Black-Scholes PDE: $\Delta\tau \leq (\Delta S)^2 / (\sigma^2 S_{\max}^2)$. The implicit and Crank-Nicolson schemes avoid this restriction entirely, making them the preferred choices for practical option pricing.
