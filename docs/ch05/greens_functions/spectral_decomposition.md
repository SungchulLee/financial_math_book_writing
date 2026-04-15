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

## Example: Heat Equation on [0, L] with Dirichlet Conditions

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

## Example: Heat Equation on [0, L] with Neumann Conditions

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

### Pointwise vs L² Convergence

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

??? success "Solution to Exercise 1"
    The eigenvalue problem is $\frac{1}{2}\phi''(x) = -\lambda\,\phi(x)$ with $\phi(0) = \phi(\pi) = 0$.

    The general solution of $\phi'' = -2\lambda\,\phi$ is $\phi(x) = A\sin(\sqrt{2\lambda}\,x) + B\cos(\sqrt{2\lambda}\,x)$. The boundary condition $\phi(0) = 0$ forces $B = 0$. The condition $\phi(\pi) = 0$ requires $\sin(\sqrt{2\lambda}\,\pi) = 0$, so $\sqrt{2\lambda}\,\pi = n\pi$ for $n = 1, 2, 3, \ldots$, giving

    $$
    \lambda_n = \frac{n^2}{2}
    $$

    The unnormalized eigenfunctions are $\sin(nx)$. To normalize, compute

    $$
    \int_0^{\pi} \sin^2(nx)\,dx = \frac{\pi}{2}
    $$

    so the normalized eigenfunctions are $\phi_n(x) = \sqrt{2/\pi}\,\sin(nx)$.

    **Orthonormality check**: For $m \neq n$:

    $$
    \int_0^{\pi} \phi_m(x)\,\phi_n(x)\,dx = \frac{2}{\pi}\int_0^{\pi} \sin(mx)\sin(nx)\,dx = \frac{1}{\pi}\int_0^{\pi}[\cos((m-n)x) - \cos((m+n)x)]\,dx = 0
    $$

    since both $\sin((m-n)\pi)/(m-n)$ and $\sin((m+n)\pi)/(m+n)$ vanish for integer $m \neq n$. For $m = n$, we already computed $\int_0^{\pi}\phi_n^2\,dx = 1$. Therefore $\int_0^{\pi}\phi_m\,\phi_n\,dx = \delta_{mn}$.

---

**Exercise 2.**
Using the spectral decomposition, write the Green's function for the heat equation on $[0, L]$ with Dirichlet conditions as $G(t,x;0,y) = \sum_{n=1}^{\infty}e^{-\lambda_n t}\phi_n(x)\phi_n(y)$. For $L = 1$, compute the first three terms and discuss how quickly the series converges for large $t$.

??? success "Solution to Exercise 2"
    For $L = 1$ with Dirichlet conditions, the eigenvalues are $\lambda_n = n^2\pi^2/2$ and the normalized eigenfunctions are $\phi_n(x) = \sqrt{2}\sin(n\pi x)$. The Green's function is

    $$
    G(t, x; 0, y) = 2\sum_{n=1}^{\infty} e^{-n^2\pi^2 t/2}\sin(n\pi x)\sin(n\pi y)
    $$

    The first three terms are:

    - $n = 1$: $2\,e^{-\pi^2 t/2}\sin(\pi x)\sin(\pi y)$, with decay rate $\pi^2/2 \approx 4.93$
    - $n = 2$: $2\,e^{-2\pi^2 t}\sin(2\pi x)\sin(2\pi y)$, with decay rate $2\pi^2 \approx 19.74$
    - $n = 3$: $2\,e^{-9\pi^2 t/2}\sin(3\pi x)\sin(3\pi y)$, with decay rate $9\pi^2/2 \approx 44.41$

    **Convergence for large $t$**: The ratio of the $n$-th term to the first term is $e^{-(n^2-1)\pi^2 t/2}$. For example, at $t = 1$, the $n = 2$ term is smaller than the $n = 1$ term by a factor of $e^{-3\pi^2/2} \approx e^{-14.8} \approx 3.7 \times 10^{-7}$, and the $n = 3$ term by $e^{-4\cdot\pi^2} \approx 5.2 \times 10^{-18}$. The series converges extremely rapidly for $t \geq 1$, and a single term suffices to many decimal places.

---

**Exercise 3.**
Explain why the smallest eigenvalue $\lambda_1$ determines the long-time decay rate of the Green's function. In a double-barrier option context, relate $\lambda_1$ to the rate at which the option price decays toward zero as maturity $T \to \infty$.

??? success "Solution to Exercise 3"
    The spectral expansion $G(t, x; 0, y) = \sum_{n=1}^{\infty} e^{-\lambda_n t}\phi_n(x)\phi_n(y)$ shows that each mode decays as $e^{-\lambda_n t}$, with $0 < \lambda_1 < \lambda_2 < \cdots$. For large $t$, the exponentials with larger $\lambda_n$ are negligible, and

    $$
    G(t, x; 0, y) \approx e^{-\lambda_1 t}\,\phi_1(x)\,\phi_1(y)
    $$

    The smallest eigenvalue $\lambda_1$ determines the long-time decay rate because it is the slowest-decaying mode. All other modes are suppressed by at least a factor of $e^{-(\lambda_2 - \lambda_1)t}$ relative to the first.

    **Double-barrier option context**: The price of a double-barrier (knock-out) option with barriers at $B_l$ and $B_u$ involves the Dirichlet Green's function on $[\log B_l, \log B_u]$. For large maturity $T$, the option price decays as

    $$
    V \sim C \cdot e^{-(\lambda_1 + r)T}
    $$

    where $\lambda_1 = \pi^2/(2L^2)$ with $L = \log(B_u/B_l)$, and $r$ is the discount rate. The principal eigenvalue $\lambda_1$ represents the rate at which the surviving probability leaks out through the barriers. As $T \to \infty$, essentially all paths have hit a barrier and been knocked out, so the option price decays to zero at rate $\lambda_1 + r$. A narrower barrier corridor (smaller $L$) gives a larger $\lambda_1$ and faster decay.

---

**Exercise 4.**
For the free domain $\mathbb{R}$, the eigenvalue problem has a continuous spectrum rather than a discrete one. The Fourier transform replaces the eigenfunction expansion: $G(t,x;0,y) = \frac{1}{2\pi}\int_{-\infty}^{\infty}e^{i\xi(x-y)}e^{-\xi^2 t/2}\,d\xi$. Verify this gives the Gaussian kernel by evaluating the integral.

??? success "Solution to Exercise 4"
    On the free domain $\mathbb{R}$, the eigenvalue problem $\frac{1}{2}\phi'' = -\lambda\,\phi$ has no boundary conditions to impose, so all values $\lambda = \xi^2/2$ for $\xi \in \mathbb{R}$ are admissible. The "eigenfunctions" are $e^{i\xi x}$, which are not square-integrable (they don't belong to $L^2(\mathbb{R})$), but they form a complete set via the Fourier transform. The spectral expansion becomes an integral:

    $$
    G(t, x; 0, y) = \frac{1}{2\pi}\int_{-\infty}^{\infty} e^{i\xi(x-y)}\,e^{-\xi^2 t/2}\,d\xi
    $$

    To evaluate, complete the square in the exponent. Let $w = x - y$. The integral is

    $$
    \frac{1}{2\pi}\int_{-\infty}^{\infty} \exp\!\left(i\xi w - \frac{\xi^2 t}{2}\right)d\xi = \frac{1}{2\pi}\int_{-\infty}^{\infty} \exp\!\left(-\frac{t}{2}\!\left(\xi - \frac{iw}{t}\right)^2 - \frac{w^2}{2t}\right)d\xi
    $$

    The shift $\xi \to \xi + iw/t$ in the Gaussian integral (justified by contour deformation in the complex plane) gives

    $$
    \frac{1}{2\pi}\,e^{-w^2/(2t)}\int_{-\infty}^{\infty} e^{-t\xi^2/2}\,d\xi = \frac{1}{2\pi}\,e^{-w^2/(2t)} \cdot \sqrt{\frac{2\pi}{t}} = \frac{1}{\sqrt{2\pi t}}\,e^{-(x-y)^2/(2t)}
    $$

    This is the standard Gaussian heat kernel, confirming the consistency of the continuous spectral representation with the known free-space Green's function.

---

**Exercise 5.**
Consider the Sturm-Liouville problem $-\frac{1}{2}\phi'' = \lambda\phi$ on $[0, 1]$ with Neumann conditions $\phi'(0) = \phi'(1) = 0$. Find the eigenfunctions and eigenvalues. Why does $\lambda_0 = 0$ appear, and what does it mean for the long-time behavior of the Green's function?

??? success "Solution to Exercise 5"
    The Sturm-Liouville problem is $-\frac{1}{2}\phi'' = \lambda\phi$ on $[0, 1]$ with $\phi'(0) = \phi'(1) = 0$.

    The general solution is $\phi(x) = A\cos(\sqrt{2\lambda}\,x) + B\sin(\sqrt{2\lambda}\,x)$. The condition $\phi'(0) = 0$ gives $B\sqrt{2\lambda} = 0$, so $B = 0$ (assuming we also check $\lambda = 0$ separately). Then $\phi(x) = A\cos(\sqrt{2\lambda}\,x)$ and $\phi'(1) = -A\sqrt{2\lambda}\sin(\sqrt{2\lambda}) = 0$.

    This requires $\sin(\sqrt{2\lambda}) = 0$, so $\sqrt{2\lambda} = n\pi$ for $n = 0, 1, 2, \ldots$

    **Eigenvalues**:

    $$
    \lambda_n = \frac{n^2\pi^2}{2}, \quad n = 0, 1, 2, \ldots
    $$

    **Eigenfunctions** (normalized on $[0, 1]$):

    $$
    \phi_0(x) = 1, \quad \phi_n(x) = \sqrt{2}\cos(n\pi x) \text{ for } n \geq 1
    $$

    **Why $\lambda_0 = 0$ appears**: The constant function $\phi_0 = 1$ satisfies both the equation ($\phi_0'' = 0 = -2\lambda_0\,\phi_0$) and the Neumann conditions ($\phi_0' = 0$ everywhere). It exists because Neumann conditions do not pin the function value at any point, allowing a nonzero constant solution.

    **Long-time behavior**: The Green's function is $G(t, x; 0, y) = 1 + 2\sum_{n=1}^{\infty} e^{-n^2\pi^2 t/2}\cos(n\pi x)\cos(n\pi y)$. As $t \to \infty$, all terms with $n \geq 1$ decay to zero, leaving $G \to 1$ (or $1/L$ on $[0, L]$). This means the distribution converges to the uniform distribution -- the system reaches thermal equilibrium. Total probability is conserved because the $\lambda_0 = 0$ mode does not decay.

---

**Exercise 6.**
A barrier option on $[0, L]$ has its price given by the spectral expansion. Explain why truncating the series after $N$ terms gives exponentially good approximation for large $T - t$, but poor approximation near maturity. What alternative method is better for short maturities?

??? success "Solution to Exercise 6"
    The barrier option price on $[0, L]$ has the spectral expansion

    $$
    V = e^{-r(T-t)}\sum_{n=1}^{\infty} a_n\,e^{-\lambda_n(T-t)}
    $$

    where $a_n$ are the Fourier coefficients of the payoff and $\lambda_n = n^2\pi^2/(2L^2)$.

    **Large $T - t$ (long maturity)**: The exponential factors $e^{-\lambda_n(T-t)}$ decay rapidly for large $n$. The ratio of the $n$-th term to the first is $O(e^{-(n^2 - 1)\pi^2(T-t)/(2L^2)})$, which is exponentially small. Truncating after $N$ terms introduces an error of order $e^{-\lambda_{N+1}(T-t)}$, which is exponentially small in $T - t$. For example, keeping $N = 3$ terms with $T - t = 1$ and $L = 1$ gives errors below $10^{-20}$.

    **Near maturity ($T - t$ small)**: When $T - t \to 0$, $e^{-\lambda_n(T-t)} \to 1$ for all $n$, so all modes contribute equally. The series converges slowly because the initial condition $\delta(x - y)$ (or the payoff function) has significant high-frequency content. Many terms are needed to resolve the sharp features of the payoff near maturity.

    **Alternative for short maturities**: The **method of images** is much more efficient for short times. The image series converges rapidly because the Gaussian kernels from distant images have negligible overlap with the domain when $t$ is small (the process hasn't had time to reach the boundary). Typically, only 1-2 image pairs suffice for short maturities, whereas the spectral series may need hundreds of terms.

---

**Exercise 7.**
For a non-self-adjoint operator $\mathcal{L} = \mu\partial_x + \frac{1}{2}\sigma^2\partial_{xx}$ with $\mu \neq 0$, the eigenfunctions are no longer orthogonal in the standard $L^2$ inner product. Explain how a change of variables (the "speed measure" or Liouville transformation) can symmetrize the operator, and why this is important for obtaining a well-behaved spectral decomposition.

??? success "Solution to Exercise 7"
    The operator $\mathcal{L} = \mu\partial_x + \frac{1}{2}\sigma^2\partial_{xx}$ is not self-adjoint in the standard $L^2$ inner product because $\langle \mathcal{L}u, v \rangle \neq \langle u, \mathcal{L}v \rangle$ when $\mu \neq 0$. The eigenfunctions are not orthogonal in $L^2$, complicating the spectral expansion.

    **The Liouville transformation**: Define the scale function $s(x) = \exp\!\left(-\int^x \frac{2\mu(z)}{\sigma^2(z)}\,dz\right)$ and the speed measure density $m(x) = \frac{2}{\sigma^2(x)\,s(x)}$. The substitution $\phi(x) = s(x)^{1/2}\,\psi(x)$ (or equivalently, working in the weighted space $L^2(m\,dx)$) transforms $\mathcal{L}$ into a self-adjoint Sturm-Liouville operator.

    Concretely, in the weighted inner product $\langle f, g \rangle_m = \int f(x)\,g(x)\,m(x)\,dx$, the generator $\mathcal{L}$ becomes self-adjoint:

    $$
    \langle \mathcal{L}f, g \rangle_m = \langle f, \mathcal{L}g \rangle_m
    $$

    **Why this matters**: Self-adjointness guarantees:

    1. **Real eigenvalues** -- essential for the exponential decay interpretation ($e^{-\lambda_n t}$ with real $\lambda_n$).
    2. **Orthogonal eigenfunctions** (in $L^2(m\,dx)$) -- enabling clean decomposition of arbitrary functions and the completeness theorem.
    3. **Spectral theorem** -- ensuring the eigenfunctions form a complete basis, so the Green's function expansion $G = \sum e^{-\lambda_n t}\phi_n(x)\phi_n(y)/m(y)$ converges and represents the full solution.

    Without this symmetrization, one must use biorthogonal expansions (eigenfunctions of $\mathcal{L}$ and $\mathcal{L}^*$), which are technically more complex and may have poorer convergence properties.
