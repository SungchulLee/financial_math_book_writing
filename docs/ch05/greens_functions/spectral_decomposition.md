# Spectral Decomposition

The **spectral decomposition** expresses the Green's function as a sum over **eigenfunctions** of the spatial operator. Each eigenfunction represents an independent mode of the system, vibrating or decaying at its own characteristic rate. This decomposition is the PDE analog of diagonalization in linear algebra: it reduces a complicated operator into a collection of independent, one-dimensional problems.

---

## Intuition

Consider a vibrating string or a cooling rod. The motion can be decomposed into **fundamental modes** -- sine waves of different frequencies. Each mode evolves independently: in the heat equation, each mode decays exponentially at a rate proportional to its eigenvalue (higher frequencies decay faster). The full solution is the superposition of all modes.

In finance, the spectral decomposition of a pricing operator reveals the **term structure of decay rates** -- how different components of the option price decay as maturity increases.

---

## The Eigenvalue Problem

### Setting

Consider the generator $\mathcal{L}$ on a bounded domain $[a, b]$ with homogeneous boundary conditions (Dirichlet, Neumann, or Robin). The **eigenvalue problem** is:

$$
\boxed{
\mathcal{L}\phi_n = -\lambda_n\,\phi_n, \quad \text{with boundary conditions on } [a, b]
}
$$

where $\lambda_n$ are the **eigenvalues** and $\phi_n$ are the **eigenfunctions**.

**Convention**: The minus sign ensures $\lambda_n > 0$ for dissipative operators (the generator has non-positive eigenvalues).

### Properties (Self-Adjoint Case)

When $\mathcal{L}$ is self-adjoint with respect to the appropriate inner product (e.g., the heat operator $\frac{1}{2}\partial_{xx}$), the spectral theory guarantees:

1. **Real eigenvalues**: $0 < \lambda_1 \leq \lambda_2 \leq \cdots \to \infty$
2. **Orthogonal eigenfunctions**: $\int_a^b \phi_m(x)\,\phi_n(x)\,dx = \delta_{mn}$ (after normalization)
3. **Completeness**: Every square-integrable function $f$ on $[a, b]$ can be expanded as:

$$
f(x) = \sum_{n=1}^{\infty} c_n\,\phi_n(x), \quad c_n = \int_a^b f(y)\,\phi_n(y)\,dy
$$

---

## Spectral Expansion of the Green's Function

### Theorem

The Green's function of the parabolic equation $\partial_t u = \mathcal{L}u$ on $[a,b]$ with homogeneous boundary conditions has the expansion:

$$
\boxed{
G(t, x; s, y) = \sum_{n=1}^{\infty} e^{-\lambda_n(t-s)}\,\phi_n(x)\,\phi_n(y)
}
$$

**Derivation**: Expand the delta function initial condition in eigenfunctions:

$$
\delta(x - y) = \sum_{n=1}^{\infty} \phi_n(y)\,\phi_n(x)
$$

Since each mode evolves independently as $\phi_n(x)\,e^{-\lambda_n t}$ (because $\mathcal{L}\phi_n = -\lambda_n\phi_n$), the solution with delta initial data is:

$$
G(t, x; 0, y) = \sum_{n=1}^{\infty} e^{-\lambda_n t}\,\phi_n(x)\,\phi_n(y)
$$

### Structure of the Expansion

Each term $e^{-\lambda_n(t-s)}\phi_n(x)\phi_n(y)$ has a clear interpretation:

- $\phi_n(x)$: the spatial shape of the $n$-th mode at the observation point
- $\phi_n(y)$: the coupling of the source point to the $n$-th mode
- $e^{-\lambda_n(t-s)}$: the temporal decay of the $n$-th mode

**Key insight**: Higher modes (larger $\lambda_n$) decay faster. For large times, only the lowest mode survives:

$$
G(t, x; 0, y) \approx e^{-\lambda_1 t}\,\phi_1(x)\,\phi_1(y) \quad \text{as } t \to \infty
$$

---

## Example: Heat Equation on $[0, L]$ with Dirichlet Conditions

### Eigenvalue Problem

$$
\frac{1}{2}\phi''(x) = -\lambda\,\phi(x), \quad \phi(0) = \phi(L) = 0
$$

**Eigenfunctions**:

$$
\phi_n(x) = \sqrt{\frac{2}{L}}\sin\!\left(\frac{n\pi x}{L}\right), \quad n = 1, 2, 3, \ldots
$$

**Eigenvalues**:

$$
\lambda_n = \frac{n^2\pi^2}{2L^2}
$$

### Green's Function

$$
G(t, x; 0, y) = \frac{2}{L}\sum_{n=1}^{\infty} \exp\!\left(-\frac{n^2\pi^2 t}{2L^2}\right) \sin\!\left(\frac{n\pi x}{L}\right)\sin\!\left(\frac{n\pi y}{L}\right)
$$

### Solution for General Initial Data

For $u(0, x) = f(x)$:

$$
u(t, x) = \sum_{n=1}^{\infty} c_n\,e^{-\lambda_n t}\,\phi_n(x)
$$

where the **Fourier sine coefficients** are:

$$
c_n = \int_0^L f(y)\,\phi_n(y)\,dy = \sqrt{\frac{2}{L}}\int_0^L f(y)\sin\!\left(\frac{n\pi y}{L}\right)dy
$$

**Long-time behavior**: $u(t, x) \approx c_1\,e^{-\pi^2 t/2L^2}\,\phi_1(x)$ -- only the fundamental mode survives.

---

## Example: Heat Equation on $[0, L]$ with Neumann Conditions

### Eigenvalue Problem

$$
\frac{1}{2}\phi''(x) = -\lambda\,\phi(x), \quad \phi'(0) = \phi'(L) = 0
$$

**Eigenfunctions**:

$$
\phi_0(x) = \frac{1}{\sqrt{L}}, \quad \phi_n(x) = \sqrt{\frac{2}{L}}\cos\!\left(\frac{n\pi x}{L}\right), \quad n = 1, 2, \ldots
$$

**Eigenvalues**:

$$
\lambda_0 = 0, \quad \lambda_n = \frac{n^2\pi^2}{2L^2}, \quad n \geq 1
$$

The zero eigenvalue corresponds to the constant eigenfunction: with Neumann conditions, the average value of $u$ is conserved.

**Long-time behavior**:

$$
u(t, x) \to \frac{1}{L}\int_0^L f(y)\,dy \quad \text{as } t \to \infty
$$

The solution converges to its spatial average -- probability equilibrates to the uniform distribution.

---

## Non-Self-Adjoint Operators

For generators with drift, $\mathcal{L} = \mu(x)\partial_x + \frac{1}{2}\sigma^2(x)\partial_{xx}$, the operator is **not self-adjoint** in the standard $L^2$ inner product. Two approaches handle this.

### Approach 1: Biorthogonal Expansion

Define the adjoint eigenfunctions $\psi_n$ by $\mathcal{L}^*\psi_n = -\lambda_n\psi_n$. The Green's function expands as:

$$
G(t, x; s, y) = \sum_{n=1}^{\infty} e^{-\lambda_n(t-s)}\,\phi_n(x)\,\psi_n(y)
$$

where $\{\phi_n\}$ and $\{\psi_n\}$ form a **biorthogonal system**: $\int \phi_m\,\psi_n\,dx = \delta_{mn}$.

### Approach 2: Weighted Inner Product

If $\mathcal{L}$ has a **speed measure** $m(x)$ such that $\mathcal{L}$ is self-adjoint in the weighted space $L^2(m\,dx)$, use the weighted expansion:

$$
G(t, x; s, y) = \sum_{n=1}^{\infty} e^{-\lambda_n(t-s)}\,\phi_n(x)\,\phi_n(y)\,m(y)^{-1}
$$

where $\phi_n$ are orthonormal in $L^2(m\,dx)$.

!!! example "Ornstein-Uhlenbeck"
    For $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ on $\mathbb{R}$ with the stationary measure $m(x) = \frac{\sqrt{\kappa}}{\sigma\sqrt{\pi}}\,e^{-\kappa x^2/\sigma^2}$, the eigenfunctions are **Hermite polynomials** and the eigenvalues are $\lambda_n = n\kappa$. The spectral gap is $\kappa$, which is the rate of mean reversion.

---

## Convergence and Regularity

### Short-Time Behavior

For small $t - s$, the spectral series converges slowly (many modes contribute). The Green's function approaches the delta function, and the series needs many terms.

### Long-Time Behavior

For large $t - s$, the series converges rapidly. Only the first few terms matter:

$$
G(t, x; s, y) = e^{-\lambda_1(t-s)}\phi_1(x)\phi_1(y) + O(e^{-\lambda_2(t-s)})
$$

The **spectral gap** $\lambda_2 - \lambda_1$ determines the rate of convergence to the dominant mode.

### Pointwise vs $L^2$ Convergence

- **$L^2$ convergence**: Always guaranteed by the spectral theorem
- **Pointwise convergence**: Requires additional smoothness of the eigenfunctions and the initial data
- **Uniform convergence**: For $t > 0$, the exponential decay factors ensure uniform convergence of the series

---

## Financial Application: Bond Pricing

In short-rate models, the zero-coupon bond price is:

$$
P(t, r; T) = \mathbb{E}\left[e^{-\int_t^T r_s\,ds} \,\Big|\, r_t = r\right]
$$

For models where the generator of $r_t$ has a discrete spectrum (e.g., CIR on a bounded domain), the bond price admits a spectral expansion:

$$
P(t, r; T) = \sum_{n=0}^{\infty} a_n(r)\,e^{-\lambda_n(T-t)}
$$

where $a_n(r)$ involves the eigenfunctions and the eigenvalues incorporate both the generator and the discounting.

**Yield curve**: The yield $Y(T-t) = -\frac{\log P}{T-t}$ for large maturities is dominated by the smallest eigenvalue:

$$
Y(\tau) \to \lambda_0 \quad \text{as } \tau \to \infty
$$

This gives the **long rate** of the term structure.

---

## Connection to Separation of Variables

The spectral decomposition is the rigorous version of the classical **separation of variables** technique:

1. **Ansatz**: Seek solutions of the form $u(t,x) = T(t)\,X(x)$
2. **Substitution**: $T'(t)\,X(x) = T(t)\,\mathcal{L}X(x)$ implies $\frac{T'}{T} = \frac{\mathcal{L}X}{X} = -\lambda$
3. **Spatial equation**: $\mathcal{L}X = -\lambda X$ with boundary conditions -- this is the eigenvalue problem
4. **Temporal equation**: $T'(t) = -\lambda T(t)$, giving $T(t) = e^{-\lambda t}$
5. **General solution**: Superposition $u(t,x) = \sum c_n\,e^{-\lambda_n t}\,\phi_n(x)$

The spectral theorem guarantees that this construction is complete -- every solution can be represented this way.

---

## Summary

$$
\boxed{
G(t, x; s, y) = \sum_{n=1}^{\infty} e^{-\lambda_n(t-s)}\,\phi_n(x)\,\phi_n(y)
}
$$

| Aspect | Description |
|---|---|
| **Eigenvalue problem** | $\mathcal{L}\phi_n = -\lambda_n\phi_n$ with boundary conditions |
| **Green's function** | Sum of exponentially decaying modes |
| **Long-time limit** | Dominated by smallest eigenvalue $\lambda_1$ |
| **Spectral gap** | $\lambda_2 - \lambda_1$ controls rate of convergence to equilibrium |
| **Non-self-adjoint** | Use biorthogonal or weighted expansion |

**The spectral decomposition reveals the modal structure of parabolic PDEs: each eigenfunction is an independent channel of decay, and the eigenvalues determine the timescales. In finance, this connects the generator's spectrum to the term structure of interest rates and the long-time behavior of option prices.**

---

## See Also

- [Green's Function for Parabolic PDEs](greens_function_parabolic.md) -- the object being decomposed
- [Uniqueness via Energy Methods](../heat_equation/uniqueness_via_energy_methods.md) -- energy decay and the Poincare inequality
- [Free vs Bounded Domains](free_vs_bounded_domains.md) -- discrete vs continuous spectrum
- [Fundamental Solution](../heat_equation/fundamental_solution.md) -- the free-space case (continuous spectrum)

---

## Exercises

**Exercise 1.**
For the operator $\mathcal{L} = \frac{1}{2}\partial_{xx}$ on $[0, \pi]$ with Dirichlet conditions, verify that $\phi_n(x) = \sqrt{2/\pi}\sin(nx)$ are eigenfunctions with eigenvalues $\lambda_n = n^2/2$. Check orthonormality: $\int_0^{\pi}\phi_m(x)\phi_n(x)\,dx = \delta_{mn}$.

---

**Exercise 2.**
Using the spectral decomposition, write the Green's function for the heat equation on $[0, L]$ with Dirichlet conditions as $G(t,x;0,y) = \sum_{n=1}^{\infty}e^{-\lambda_n t}\phi_n(x)\phi_n(y)$. For $L = 1$, compute the first three terms and discuss how quickly the series converges for large $t$.

---

**Exercise 3.**
Explain why the smallest eigenvalue $\lambda_1$ determines the long-time decay rate of the Green's function. In a double-barrier option context, relate $\lambda_1$ to the rate at which the option price decays toward zero as maturity $T \to \infty$.

---

**Exercise 4.**
For the free domain $\mathbb{R}$, the eigenvalue problem has a continuous spectrum rather than a discrete one. The Fourier transform replaces the eigenfunction expansion: $G(t,x;0,y) = \frac{1}{2\pi}\int_{-\infty}^{\infty}e^{i\xi(x-y)}e^{-\xi^2 t/2}\,d\xi$. Verify this gives the Gaussian kernel by evaluating the integral.

---

**Exercise 5.**
Consider the Sturm-Liouville problem $-\frac{1}{2}\phi'' = \lambda\phi$ on $[0, 1]$ with Neumann conditions $\phi'(0) = \phi'(1) = 0$. Find the eigenfunctions and eigenvalues. Why does $\lambda_0 = 0$ appear, and what does it mean for the long-time behavior of the Green's function?

---

**Exercise 6.**
A barrier option on $[0, L]$ has its price given by the spectral expansion. Explain why truncating the series after $N$ terms gives exponentially good approximation for large $T - t$, but poor approximation near maturity. What alternative method is better for short maturities?

---

**Exercise 7.**
For a non-self-adjoint operator $\mathcal{L} = \mu\partial_x + \frac{1}{2}\sigma^2\partial_{xx}$ with $\mu \neq 0$, the eigenfunctions are no longer orthogonal in the standard $L^2$ inner product. Explain how a change of variables (the "speed measure" or Liouville transformation) can symmetrize the operator, and why this is important for obtaining a well-behaved spectral decomposition.
