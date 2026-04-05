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

---

## Exercises

**Exercise 1.** For the explicit scheme applied to the heat equation $u_\tau = Du_{xx}$ with $D = 1$ and $\Delta x = 0.05$, compute the amplification factor $g(\xi)$ at $\xi = \pi$ (the highest-frequency mode) for $\lambda = 0.4$ and $\lambda = 0.6$. In which case is the scheme stable?

??? success "Solution to Exercise 1"
    The amplification factor for the explicit scheme is $g = 1 - 4\lambda\sin^2(\xi/2)$.

    At $\xi = \pi$ (the highest-frequency mode), $\sin^2(\pi/2) = 1$, so $g(\pi) = 1 - 4\lambda$.

    **For $\lambda = 0.4$**:

    $$
    g(\pi) = 1 - 4(0.4) = 1 - 1.6 = -0.6
    $$

    Since $|g(\pi)| = 0.6 \leq 1$, the scheme is **stable**.

    **For $\lambda = 0.6$**:

    $$
    g(\pi) = 1 - 4(0.6) = 1 - 2.4 = -1.4
    $$

    Since $|g(\pi)| = 1.4 > 1$, the scheme is **unstable**. The highest-frequency mode grows by a factor of 1.4 at each time step, leading to exponential blow-up.

    Note: With $D = 1$ and $\Delta x = 0.05$, we have $\lambda = D\Delta\tau / (\Delta x)^2 = \Delta\tau / 0.0025$. So $\lambda = 0.4$ corresponds to $\Delta\tau = 10^{-3}$ and $\lambda = 0.6$ corresponds to $\Delta\tau = 1.5 \times 10^{-3}$. The stability threshold is $\lambda = 0.5$, i.e., $\Delta\tau = 1.25 \times 10^{-3}$.

---

**Exercise 2.** Derive the amplification factor for the implicit scheme: starting from $g = 1 - 4\lambda g \sin^2(\xi/2)$, solve for $g$ to obtain $g = 1/(1 + 4\lambda\sin^2(\xi/2))$. Verify that $|g| \leq 1$ for all $\lambda > 0$ and all $\xi$.

??? success "Solution to Exercise 2"
    Starting from the implicit scheme's Fourier mode substitution, we have:

    $$
    g = 1 + \lambda g(2\cos\xi - 2) = 1 - 4\lambda g \sin^2\!\left(\frac{\xi}{2}\right)
    $$

    Collecting terms with $g$ on the left side:

    $$
    g + 4\lambda g \sin^2\!\left(\frac{\xi}{2}\right) = 1
    $$

    $$
    g\left(1 + 4\lambda\sin^2\!\left(\frac{\xi}{2}\right)\right) = 1
    $$

    Solving for $g$:

    $$
    g = \frac{1}{1 + 4\lambda\sin^2(\xi/2)}
    $$

    **Verification that $|g| \leq 1$**: For any $\lambda > 0$ and any $\xi \in [-\pi, \pi]$:

    - $\sin^2(\xi/2) \geq 0$, so $4\lambda\sin^2(\xi/2) \geq 0$
    - Therefore the denominator satisfies $1 + 4\lambda\sin^2(\xi/2) \geq 1 > 0$
    - Consequently $0 < g \leq 1$, which gives $|g| \leq 1$

    Since $|g| \leq 1$ for all $\lambda > 0$ and all $\xi$, the implicit scheme is unconditionally stable.

---

**Exercise 3.** The Crank-Nicolson amplification factor $g = (1 - 2\lambda\sin^2(\xi/2))/(1 + 2\lambda\sin^2(\xi/2))$ can become negative for large $\lambda$. Find the critical value of $\lambda$ at which $g(\pi) = 0$, and determine for what values of $\lambda$ the highest-frequency mode $g(\pi) < -0.5$. Explain why negative $g$ leads to oscillatory behavior.

??? success "Solution to Exercise 3"
    The Crank-Nicolson amplification factor at $\xi = \pi$ is:

    $$
    g(\pi) = \frac{1 - 2\lambda\sin^2(\pi/2)}{1 + 2\lambda\sin^2(\pi/2)} = \frac{1 - 2\lambda}{1 + 2\lambda}
    $$

    **Finding $g(\pi) = 0$**: Setting $g(\pi) = 0$:

    $$
    1 - 2\lambda = 0 \implies \lambda = \frac{1}{2}
    $$

    **Finding $g(\pi) < -0.5$**: Setting $g(\pi) = -0.5$:

    $$
    \frac{1 - 2\lambda}{1 + 2\lambda} = -\frac{1}{2}
    $$

    $$
    2(1 - 2\lambda) = -(1 + 2\lambda) \implies 2 - 4\lambda = -1 - 2\lambda \implies 3 = 2\lambda \implies \lambda = \frac{3}{2}
    $$

    Since $g(\pi)$ is a decreasing function of $\lambda$, we have $g(\pi) < -0.5$ when $\lambda > 3/2$.

    **Why negative $g$ causes oscillations**: When $g < 0$, the Fourier mode $\varepsilon_j^n = g^n e^{i\xi j}$ alternates sign at successive time steps: $g^n$ is positive for even $n$ and negative for odd $n$. This means the high-frequency error component flips its sign every time step, producing a sawtooth oscillation in time. The oscillation does not grow (since $|g| \leq 1$), but it can produce visually noisy solutions, especially near non-smooth features. This is a well-known issue with Crank-Nicolson for large time steps.

---

**Exercise 4.** For the general theta-scheme with amplification factor $g = (1 - (1-\theta)\mu)/(1 + \theta\mu)$ where $\mu = 4\lambda\sin^2(\xi/2)$, prove that the scheme is unconditionally stable when $\theta \geq 1/2$. What is the stability restriction when $\theta = 1/4$?

??? success "Solution to Exercise 4"
    For the theta-scheme, $g = (1 - (1-\theta)\mu)/(1 + \theta\mu)$ where $\mu = 4\lambda\sin^2(\xi/2) \geq 0$.

    **Proving unconditional stability for $\theta \geq 1/2$**: We need $|g|^2 \leq 1$, i.e.:

    $$
    (1 - (1-\theta)\mu)^2 \leq (1 + \theta\mu)^2
    $$

    Expanding both sides:

    $$
    1 - 2(1-\theta)\mu + (1-\theta)^2\mu^2 \leq 1 + 2\theta\mu + \theta^2\mu^2
    $$

    Simplifying:

    $$
    -2(1-\theta)\mu + (1-\theta)^2\mu^2 \leq 2\theta\mu + \theta^2\mu^2
    $$

    $$
    0 \leq 2\mu[\theta + (1-\theta)] + \mu^2[\theta^2 - (1-\theta)^2]
    $$

    $$
    0 \leq 2\mu + \mu^2(2\theta - 1)
    $$

    $$
    0 \leq \mu[2 + \mu(2\theta - 1)]
    $$

    Since $\mu \geq 0$, we need $2 + \mu(2\theta - 1) \geq 0$. When $\theta \geq 1/2$, the term $\mu(2\theta - 1) \geq 0$, so $2 + \mu(2\theta - 1) \geq 2 > 0$. Thus the inequality holds for all $\mu \geq 0$ and all $\lambda > 0$, proving unconditional stability.

    **Stability restriction for $\theta = 1/4$**: When $\theta < 1/2$, instability occurs when $g = -1$, i.e., $1 - (1-\theta)\mu = -(1 + \theta\mu)$:

    $$
    1 - (1-\theta)\mu = -1 - \theta\mu \implies 2 = \mu(1 - 2\theta)
    $$

    $$
    \mu = \frac{2}{1 - 2\theta}
    $$

    The worst case is $\xi = \pi$ where $\mu = 4\lambda$, so:

    $$
    4\lambda \leq \frac{2}{1 - 2\theta} \implies \lambda \leq \frac{1}{2(1 - 2\theta)}
    $$

    For $\theta = 1/4$:

    $$
    \lambda \leq \frac{1}{2(1 - 1/2)} = \frac{1}{2 \times 1/2} = 1
    $$

---

**Exercise 5.** The mesh Peclet number $\text{Pe}_h = |c|\Delta x/D$ governs oscillations in convection-diffusion problems. For the Black-Scholes PDE in log-price coordinates with $r = 0.05$, $\sigma = 0.3$, and $\Delta x = 0.05$, compute $\text{Pe}_h$ and determine whether central differences are oscillation-free. What $\Delta x$ would ensure $\text{Pe}_h \leq 2$?

??? success "Solution to Exercise 5"
    For the Black-Scholes PDE in log-price coordinates, the convection coefficient is $c = r - \sigma^2/2$ and the diffusion coefficient is $D = \sigma^2/2$.

    With $r = 0.05$, $\sigma = 0.3$:

    $$
    c = 0.05 - \frac{(0.3)^2}{2} = 0.05 - 0.045 = 0.005
    $$

    $$
    D = \frac{(0.3)^2}{2} = 0.045
    $$

    The mesh Peclet number with $\Delta x = 0.05$:

    $$
    \text{Pe}_h = \frac{|c|\Delta x}{D} = \frac{0.005 \times 0.05}{0.045} = \frac{2.5 \times 10^{-4}}{0.045} \approx 0.0056
    $$

    Since $\text{Pe}_h \approx 0.0056 \ll 2$, central differences are oscillation-free. The problem is diffusion-dominated at this grid scale.

    To find the maximum $\Delta x$ ensuring $\text{Pe}_h \leq 2$:

    $$
    \frac{|c|\Delta x}{D} \leq 2 \implies \Delta x \leq \frac{2D}{|c|} = \frac{2 \times 0.045}{0.005} = 18
    $$

    Since $\Delta x \leq 18$ is an extremely generous bound, oscillation from the convection term is not a concern for any practically reasonable grid spacing. This is because the drift $r - \sigma^2/2$ is very small compared to the diffusion $\sigma^2/2$ for typical financial parameters.

---

**Exercise 6.** Von Neumann analysis strictly applies only to constant-coefficient problems on periodic domains. Explain why a "frozen-coefficient" analysis at each grid node provides useful (though not rigorous) stability information for the Black-Scholes PDE in the original $S$-coordinates, where the diffusion coefficient $\frac{1}{2}\sigma^2 S_j^2$ varies with $j$.

??? success "Solution to Exercise 6"
    In the Black-Scholes PDE in original $S$-coordinates, the diffusion coefficient $\frac{1}{2}\sigma^2 S_j^2$ varies with the spatial node $j$. Von Neumann analysis formally requires constant coefficients because it decomposes errors into Fourier modes, which are eigenfunctions of constant-coefficient difference operators. With variable coefficients, Fourier modes are no longer eigenfunctions, and the analysis is not rigorous.

    However, the frozen-coefficient approach is useful for the following reasons:

    1. **Local behavior**: At any fixed node $j$, the coefficients vary slowly relative to the grid spacing (assuming a sufficiently fine grid). Over a small neighborhood of a few grid points, the coefficients are approximately constant. The local error growth is therefore well-approximated by the constant-coefficient analysis with the local value of the coefficient.

    2. **Necessary condition**: The frozen-coefficient von Neumann condition is a necessary condition for stability of the variable-coefficient problem. If any local amplification factor exceeds 1, that local mode will grow and eventually contaminate the global solution. Thus, requiring $|g_j(\xi)| \leq 1$ at every node $j$ is a minimum requirement.

    3. **Worst-case node**: For the explicit scheme, the local mesh ratio is $\lambda_j = \sigma^2 S_j^2 \Delta\tau / (2(\Delta S)^2)$, and the CFL condition $\lambda_j \leq 1/2$ must hold at every node. The binding constraint occurs at the node with the largest $S_j$ (i.e., $j = M$), giving $\Delta\tau \leq (\Delta S)^2 / (\sigma^2 S_{\max}^2)$. This worst-case analysis is conservative but reliable.

    4. **Practical validation**: Experience shows that the frozen-coefficient CFL condition, applied at the worst-case node, is an accurate predictor of the actual stability boundary for the Black-Scholes PDE. Numerical experiments consistently confirm that violating this condition at any node leads to blow-up.
