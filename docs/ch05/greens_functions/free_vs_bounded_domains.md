# Free vs Bounded Domains

The behavior of a Green's function depends fundamentally on whether the domain is **free** (unbounded, typically all of $\mathbb{R}$) or **bounded** (a finite interval or region with explicit boundary conditions). On free domains, heat diffuses away to infinity and the Green's function is a single Gaussian. On bounded domains, heat reflects off or is absorbed by the boundaries, producing a richer structure involving image sources or spectral expansions. In finance, this distinction maps to the difference between **standard options** (free domain) and **barrier options** (bounded domain).

---

## Free-Space Green's Function

### The Gaussian Kernel

On $\mathbb{R}$ (no boundaries), the Green's function for $\partial_t u = \frac{1}{2}\partial_{xx} u$ is:

$$
\boxed{
G_{\text{free}}(t, x; s, y) = \frac{1}{\sqrt{2\pi(t-s)}} \exp\!\left(-\frac{(x-y)^2}{2(t-s)}\right)
}
$$

**Properties:**

- Defined for all $x, y \in \mathbb{R}$ and $t > s$
- $\int_{-\infty}^{\infty} G_{\text{free}}\,dx = 1$ -- probability is conserved
- As $t \to \infty$, $G_{\text{free}} \to 0$ pointwise -- heat dissipates to infinity
- **Continuous spectrum**: The Fourier transform diagonalizes the operator, with spectral parameter $\xi \in \mathbb{R}$:

$$
G_{\text{free}}(t, x; 0, y) = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{i\xi(x-y)}\,e^{-\xi^2 t/2}\,d\xi
$$

**Financial interpretation**: The free-space Green's function is the transition density of geometric Brownian motion (after a log-transformation), which gives the standard Black-Scholes pricing framework with no barriers.

---

## Bounded-Domain Green's Function: Dirichlet Conditions

### Setting

On $[0, L]$ with **absorbing boundaries** $u(t, 0) = u(t, L) = 0$, the Green's function must vanish at both endpoints.

### Method of Images

The Dirichlet Green's function can be constructed by **superposing image sources** -- fictitious sources placed outside the domain to enforce the boundary conditions.

For a single absorbing boundary at $x = 0$:

$$
G_{\text{half}}(t, x; 0, y) = G_{\text{free}}(t, x; 0, y) - G_{\text{free}}(t, x; 0, -y)
$$

The negative image at $-y$ cancels the Green's function at $x = 0$.

For the interval $[0, L]$ with two absorbing boundaries, an infinite sequence of images is needed:

$$
G_{\text{Dir}}(t, x; 0, y) = \sum_{k=-\infty}^{\infty} \left[G_{\text{free}}(t, x; 0, y + 2kL) - G_{\text{free}}(t, x; 0, -y + 2kL)\right]
$$

Each pair of images enforces the zero condition at $x = 0$ and $x = L$ simultaneously.

!!! note "Convergence"
    The image series converges rapidly for large $t$ (because the Gaussians from distant images have negligible contribution) but slowly for small $t$. The spectral expansion (below) has the opposite behavior: fast for large $t$, slow for small $t$.

### Spectral Expansion

The same Green's function has the eigenfunction representation:

$$
\boxed{
G_{\text{Dir}}(t, x; 0, y) = \frac{2}{L}\sum_{n=1}^{\infty} \exp\!\left(-\frac{n^2\pi^2 t}{2L^2}\right)\sin\!\left(\frac{n\pi x}{L}\right)\sin\!\left(\frac{n\pi y}{L}\right)
}
$$

**Properties:**

- $G_{\text{Dir}}(t, 0; 0, y) = G_{\text{Dir}}(t, L; 0, y) = 0$ -- boundary conditions satisfied
- $\int_0^L G_{\text{Dir}}(t, x; 0, y)\,dx < 1$ for $t > 0$ -- probability is **not** conserved (it leaks through the absorbing boundaries)
- **Discrete spectrum**: Eigenvalues $\lambda_n = n^2\pi^2 / 2L^2$ are isolated
- **Long-time decay**: $G_{\text{Dir}} \sim e^{-\pi^2 t/2L^2}\sin(\pi x/L)\sin(\pi y/L)$ -- exponential decay at the rate of the first eigenvalue

---

## Bounded-Domain Green's Function: Neumann Conditions

### Setting

On $[0, L]$ with **reflecting boundaries** $u_x(t, 0) = u_x(t, L) = 0$:

### Method of Images

The Neumann condition requires a **positive** image (same sign):

$$
G_{\text{Neu}}(t, x; 0, y) = \sum_{k=-\infty}^{\infty} \left[G_{\text{free}}(t, x; 0, y + 2kL) + G_{\text{free}}(t, x; 0, -y + 2kL)\right]
$$

### Spectral Expansion

$$
G_{\text{Neu}}(t, x; 0, y) = \frac{1}{L} + \frac{2}{L}\sum_{n=1}^{\infty}\exp\!\left(-\frac{n^2\pi^2 t}{2L^2}\right)\cos\!\left(\frac{n\pi x}{L}\right)\cos\!\left(\frac{n\pi y}{L}\right)
$$

**Properties:**

- $\int_0^L G_{\text{Neu}}\,dx = 1$ for all $t$ -- probability is conserved (reflecting boundaries keep mass in)
- **Long-time limit**: $G_{\text{Neu}}(t, x; 0, y) \to \frac{1}{L}$ -- the uniform distribution (equilibrium)
- The zero eigenvalue $\lambda_0 = 0$ corresponds to the constant eigenfunction and represents the conservation of total probability

---

## Comparison: Free vs Bounded

| Aspect | Free Domain ($\mathbb{R}$) | Bounded (Dirichlet) | Bounded (Neumann) |
|---|---|---|---|
| **Green's function** | Single Gaussian | Image series or sine expansion | Image series or cosine expansion |
| **Spectrum** | Continuous ($\xi \in \mathbb{R}$) | Discrete ($\lambda_n = n^2\pi^2/2L^2$) | Discrete ($\lambda_0 = 0, \lambda_n > 0$) |
| **Probability conservation** | Yes ($\int G = 1$) | No ($\int G < 1$, leaks out) | Yes ($\int G = 1$) |
| **Long-time limit** | $G \to 0$ (disperses) | $G \to 0$ (absorbed) | $G \to 1/L$ (equilibrium) |
| **Financial analog** | Standard option | Barrier option (knockout) | Reflecting boundaries |

!!! tip "Which Representation to Use?"
    - **Short times** ($t \ll L^2$): The image series converges fast (few images needed because the process hasn't reached the boundary yet)
    - **Long times** ($t \gg L^2$): The spectral series converges fast (only the first few eigenmodes survive)
    - **Intermediate times**: Both converge at similar rates; either works

---

## Financial Interpretation

### Standard Options (Free Domain)

For a European call under Black-Scholes, the log-price $X_t = \log S_t$ lives on all of $\mathbb{R}$. The free-space Green's function gives the standard pricing formula:

$$
V(t, S) = e^{-r(T-t)}\int_0^{\infty} g(S_T)\,p_{\text{free}}(T, S_T \mid t, S)\,dS_T
$$

where $p_{\text{free}}$ is the lognormal transition density.

### Barrier Options (Bounded Domain)

For a **down-and-out call** with barrier at $B < K$, the log-price is restricted to $(\log B, \infty)$. The Dirichlet condition $V(t, B) = 0$ is imposed:

$$
V_{\text{DO}}(t, S) = e^{-r(T-t)}\int_B^{\infty} g(S_T)\,p_{\text{Dir}}(T, S_T \mid t, S)\,dS_T
$$

where $p_{\text{Dir}}$ is the transition density with absorption at $\log B$.

**Relationship to the free-domain price**:

$$
V_{\text{DO}}(t, S) < V_{\text{vanilla}}(t, S)
$$

The barrier option is always worth less than the vanilla option because some paths are killed at the barrier.

### Double Barrier Options

For a **double knock-out option** with barriers at $B_l < S < B_u$, the domain is bounded on both sides. The Green's function is the full spectral expansion on $[\log B_l, \log B_u]$.

---

## The Method of Images in Detail

### Single Absorbing Barrier

For the half-line $[0, \infty)$ with $u(t, 0) = 0$:

$$
G(t, x; 0, y) = \frac{1}{\sqrt{2\pi t}}\left[\exp\!\left(-\frac{(x-y)^2}{2t}\right) - \exp\!\left(-\frac{(x+y)^2}{2t}\right)\right]
$$

**Probabilistic interpretation**: This is the density of Brownian motion at $x$ conditional on not hitting zero before time $t$:

$$
G(t, x; 0, y) = p(B_t \in dx, \tau_0 > t \mid B_0 = y) / dx
$$

where $\tau_0 = \inf\{t : B_t = 0\}$.

The **survival probability** is:

$$
\mathbb{P}(\tau_0 > t \mid B_0 = y) = \int_0^{\infty} G(t, x; 0, y)\,dx = \text{erf}\!\left(\frac{y}{\sqrt{2t}}\right)
$$

### Reflection Principle

The method of images is the PDE version of the **reflection principle** for Brownian motion:

$$
\mathbb{P}(B_t \geq x,\, \min_{s \leq t} B_s \leq 0 \mid B_0 = y) = \mathbb{P}(B_t \geq x \mid B_0 = -y)
$$

Each image source corresponds to a reflected path that has crossed the barrier.

---

## Domain Truncation for Numerical Methods

In practice, the free-space domain $\mathbb{R}$ must be truncated to a bounded domain for finite difference methods. This introduces artificial boundaries.

**Common strategies:**

1. **Large domain**: Set $[x_{\min}, x_{\max}]$ with $x_{\min}, x_{\max}$ far from the region of interest. Impose Dirichlet conditions based on asymptotic behavior
2. **Absorbing boundaries**: Use $u = 0$ at truncation points (conservative -- slightly underprices)
3. **Linear boundary conditions**: $\partial_{xx} u = 0$ at truncation (extrapolate linearly)

!!! warning "Truncation Error"
    The truncation introduces error of order $O(e^{-(x_{\max} - x_0)^2/2T})$ -- exponentially small if the truncation is sufficiently far. For Black-Scholes with $\sigma = 0.2$ and $T = 1$, setting $x_{\max} = x_0 + 5\sigma\sqrt{T}$ gives negligible error.

---

## Summary

| Domain | Green's Function | Spectrum | Conservation | Long-Time |
|---|---|---|---|---|
| **Free** ($\mathbb{R}$) | Gaussian kernel | Continuous | $\int G = 1$ | Disperses |
| **Dirichlet** ($[0,L]$) | Images or sines | Discrete, $\lambda_n > 0$ | $\int G < 1$ | Decays to 0 |
| **Neumann** ($[0,L]$) | Images or cosines | Discrete, $\lambda_0 = 0$ | $\int G = 1$ | Equilibrium |

$$
\boxed{
\text{Free domain: dispersion} \qquad \text{Absorbing boundary: decay} \qquad \text{Reflecting boundary: equilibrium}
}
$$

**The choice of domain and boundary conditions determines the qualitative behavior of the Green's function. In finance, free domains correspond to standard options, absorbing boundaries to barrier options, and reflecting boundaries to constrained portfolios. The method of images and spectral decomposition provide complementary representations, each optimal in different time regimes.**

---

## See Also

- [Green's Function for Parabolic PDEs](greens_function_parabolic.md) -- general construction
- [Spectral Decomposition](spectral_decomposition.md) -- eigenfunction expansion on bounded domains
- [Boundary Value Problems](../overview/boundary_value_problems.md) -- types of boundary conditions
- [Fundamental Solution](../heat_equation/fundamental_solution.md) -- the free-space heat kernel

---

## Exercises

**Exercise 1.**
Write the free-space Green's function $G_{\text{free}}(t, x; 0, y)$ for the heat equation $\partial_t u = \frac{1}{2}\partial_{xx}u$. Verify that $\int_{-\infty}^{\infty}G_{\text{free}}\,dx = 1$ for all $t > 0$ by recognizing the integrand as a Gaussian density.

---

**Exercise 2.**
For the bounded domain $[0, L]$ with absorbing (Dirichlet) boundary conditions, the Green's function can be constructed via the method of images. Write the first image correction to the free-space kernel and explain geometrically why image sources are placed at $y' = -y$ and $y' = 2L - y$.

---

**Exercise 3.**
A down-and-out barrier option on a log-price process $X_t = \ln S_t$ corresponds to solving the heat equation on $[B, \infty)$ with absorbing condition at $X = B$. Explain why the Green's function on this half-line is $G_{\text{free}}(t, x; 0, y) - G_{\text{free}}(t, x; 0, 2B - y)$. What is the financial interpretation of the subtracted term?

---

**Exercise 4.**
Compare the long-time behavior of the free-space Green's function (pointwise decay to zero, conservation of total mass) with the bounded-domain Dirichlet Green's function (exponential decay in total mass). Explain the probabilistic reason for this difference in terms of absorption at the boundary.

---

**Exercise 5.**
On $[0, L]$ with Dirichlet conditions, the spectral expansion of the Green's function involves eigenvalues $\lambda_n = n^2\pi^2/(2L^2)$. Explain why the smallest eigenvalue $\lambda_1$ dominates for large times and compute the decay rate of $G$ for $L = 1$.

---

**Exercise 6.**
For Neumann boundary conditions $\partial_x u(t, 0) = \partial_x u(t, L) = 0$, the Green's function conserves total mass. Explain why, in financial terms, this corresponds to a reflecting barrier. Give an example of a financial model where reflecting barriers are appropriate.

---

**Exercise 7.**
Consider a double-barrier option with $B_l = 80$ and $B_u = 120$ on a stock with $S_0 = 100$. In log-space, this corresponds to a bounded domain $[\ln 80, \ln 120]$. Explain qualitatively how the spectral decomposition of the Green's function on this interval determines the option price, and why shorter-maturity options are more sensitive to higher-order eigenmodes.
