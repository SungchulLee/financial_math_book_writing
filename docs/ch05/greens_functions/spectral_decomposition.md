# Spectral Decomposition

The spectral decomposition expresses the [Green's function](greens_function_parabolic.md) as a sum over **eigenfunctions** of the spatial operator. Each eigenfunction is an independent mode that decays at its own characteristic rate, turning a single parabolic PDE into a family of uncoupled ODEs. This is the PDE analog of diagonalizing a matrix, and in finance it produces the term-structure modes that organize long-maturity pricing.

This page is the **eigenstructure lens** on Green's functions; the operator/PDE lens is in [Green's Function for Parabolic PDEs](greens_function_parabolic.md), the probability lens in [Transition Density as Green's Function](transition_density_as_greens_function.md), and the geometry lens in [Free vs Bounded Domains](free_vs_bounded_domains.md).

---

## The Eigenvalue Problem

On a bounded domain $[a, b]$ with homogeneous boundary conditions, the generator $\mathcal{L}$ has an eigenvalue problem

$$
\mathcal{L}\phi_n = -\lambda_n\,\phi_n, \qquad \text{boundary conditions on } [a,b].
$$

The minus sign makes $\lambda_n > 0$ for dissipative operators. When $\mathcal{L}$ is self-adjoint in the relevant inner product, spectral theory guarantees:

1. **Real, ordered eigenvalues**: $0 \leq \lambda_1 \leq \lambda_2 \leq \cdots \to \infty$.
2. **Orthonormal eigenfunctions**: $\int_a^b \phi_m\,\phi_n\,dx = \delta_{mn}$.
3. **Completeness**: any $f \in L^2([a,b])$ expands as $f(x) = \sum_n c_n\,\phi_n(x)$ with $c_n = \int f\phi_n\,dy$.

---

## Spectral Expansion of the Green's Function

Expanding the delta initial condition $\delta(x-y) = \sum_n \phi_n(y)\phi_n(x)$ and evolving each mode by $e^{-\lambda_n t}$ gives the central formula:

$$
\boxed{\,G(t, x; s, y) = \sum_{n=1}^{\infty} e^{-\lambda_n(t-s)}\,\phi_n(x)\,\phi_n(y)\,}
$$

Each term has three factors:

- $\phi_n(x)$ -- spatial shape of mode $n$ at the observation point,
- $\phi_n(y)$ -- coupling of the source to mode $n$,
- $e^{-\lambda_n(t-s)}$ -- temporal decay of mode $n$.

Higher modes decay faster, so for large $t-s$ only the lowest mode survives:

$$
G(t, x; 0, y) \sim e^{-\lambda_1 t}\,\phi_1(x)\,\phi_1(y).
$$

!!! note "Relation to separation of variables"
    The ansatz $u(t,x) = T(t)X(x)$ in $\partial_t u = \mathcal{L}u$ gives $T'/T = \mathcal{L}X/X = -\lambda$, so the eigenvalue problem is exactly the spatial half of separation of variables. The spectral theorem guarantees the construction is complete.

---

## Modal Interpretation and Convergence

Think of each eigenfunction as an independent channel. Mode $n$ has its own amplitude (set by the initial data), its own shape $\phi_n$, and its own lifetime $1/\lambda_n$. Evolution is just exponential decay applied mode-by-mode.

Two convergence regimes matter:

- **Long time, $t - s$ large**: $e^{-\lambda_n(t-s)}$ suppresses high modes strongly, and a handful of terms give extreme accuracy. The error after truncating at $N$ terms is $O(e^{-\lambda_{N+1}(t-s)})$.
- **Short time, $t - s$ small**: the series must reproduce a near-delta function, all high frequencies contribute, and convergence is slow. The short-time regime is better served by the method-of-images representation (see [Free vs Bounded Domains](free_vs_bounded_domains.md)).

The **spectral gap** $\lambda_2 - \lambda_1$ controls how quickly the solution collapses onto the first mode.

---

## Example: Heat Equation on [0, L]

For $\mathcal{L} = \tfrac12\partial_{xx}$ on $[0,L]$ with Dirichlet conditions $\phi(0)=\phi(L)=0$:

$$
\phi_n(x) = \sqrt{\tfrac{2}{L}}\sin\!\left(\tfrac{n\pi x}{L}\right), \qquad \lambda_n = \tfrac{n^2\pi^2}{2L^2},
$$

so

$$
G(t,x;0,y) = \frac{2}{L}\sum_{n=1}^{\infty} e^{-n^2\pi^2 t/(2L^2)}\sin\!\left(\tfrac{n\pi x}{L}\right)\sin\!\left(\tfrac{n\pi y}{L}\right).
$$

With Neumann conditions $\phi'(0)=\phi'(L)=0$, the same $\lambda_n$ appear for $n\geq 1$, plus a zero eigenvalue $\lambda_0 = 0$ with constant eigenfunction $\phi_0 = 1/\sqrt{L}$. The zero mode does not decay, reflecting conservation of total probability with reflecting boundaries.

---

## Non-Self-Adjoint Operators

For generators with drift, $\mathcal{L} = \mu(x)\partial_x + \tfrac12\sigma^2(x)\partial_{xx}$, the operator is not self-adjoint in $L^2$. Two standard remedies.

**Biorthogonal expansion**: introduce adjoint eigenfunctions $\psi_n$ with $\mathcal{L}^*\psi_n = -\lambda_n\psi_n$, normalized so $\int \phi_m\psi_n\,dx = \delta_{mn}$. Then

$$
G(t,x;s,y) = \sum_n e^{-\lambda_n(t-s)}\,\phi_n(x)\,\psi_n(y).
$$

**Weighted inner product**: if $\mathcal{L}$ is self-adjoint in $L^2(m\,dx)$ for some speed measure $m$, the expansion uses $\phi_n$ orthonormal under that weight. This is the preferred route whenever a natural stationary measure exists.

!!! example "Ornstein-Uhlenbeck: Hermite modes"
    Recall (see [§ Transition Density as Green's Function](transition_density_as_greens_function.md)): the Ornstein-Uhlenbeck transition density is explicitly Gaussian. Here we focus on the eigenstructure. For $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ on $\mathbb{R}$, the stationary density $m(x) \propto e^{-\kappa x^2/\sigma^2}$ makes $\mathcal{L}$ self-adjoint in $L^2(m\,dx)$. The eigenfunctions are the **Hermite polynomials** $H_n$ with eigenvalues $\lambda_n = n\kappa$. The spectral gap is exactly the mean-reversion rate $\kappa$, and higher Hermite modes decay in integer multiples of it.

---

## Finance Application: Term Structure Modes

In a short-rate model with generator $\mathcal{L}$ and discrete spectrum, the zero-coupon bond price admits a spectral representation

$$
P(t, r; T) = \sum_{n=0}^{\infty} a_n(r)\,e^{-\lambda_n (T-t)},
$$

where the $\lambda_n$ combine the generator's eigenvalues with the discounting. Each $a_n(r)\,e^{-\lambda_n(T-t)}$ is a **yield-curve mode**: a fixed spatial shape in $r$ whose contribution decays at a maturity-specific rate.

The **yield** $Y(\tau) = -\log P / \tau$ for long $\tau$ is dominated by the smallest eigenvalue:

$$
Y(\tau) \to \lambda_0 \quad \text{as } \tau \to \infty.
$$

This is the **long rate** of the term structure -- a direct spectral quantity. In empirical studies, the first few eigenmodes give the standard "level, slope, curvature" decomposition of yield-curve movements, with spectral gaps controlling how quickly curvature shocks revert relative to slope shocks.

---

## Summary

| Aspect | Description |
|---|---|
| Eigenvalue problem | $\mathcal{L}\phi_n = -\lambda_n\phi_n$ with BCs |
| Green's function | $\sum_n e^{-\lambda_n(t-s)}\phi_n(x)\phi_n(y)$ |
| Long-time limit | Dominated by smallest $\lambda_1$ |
| Spectral gap | $\lambda_2 - \lambda_1$ sets approach-to-equilibrium rate |
| Non-self-adjoint | Biorthogonal or weighted expansion |
| Finance | Yield-curve modes, long rate = smallest eigenvalue |

---

## See Also

- [Green's Function for Parabolic PDEs](greens_function_parabolic.md)
- [Transition Density as Green's Function](transition_density_as_greens_function.md)
- [Free vs Bounded Domains](free_vs_bounded_domains.md)

---

## Exercises

**Exercise 1.**
For $\mathcal{L} = \tfrac12\partial_{xx}$ on $[0,\pi]$ with Dirichlet conditions, verify that $\phi_n(x) = \sqrt{2/\pi}\sin(nx)$ are eigenfunctions with eigenvalues $\lambda_n = n^2/2$, and check orthonormality.

??? success "Solution to Exercise 1"
    Solve $\phi'' = -2\lambda\phi$ with $\phi(0)=\phi(\pi)=0$: the general solution $A\sin(\sqrt{2\lambda}x) + B\cos(\sqrt{2\lambda}x)$ reduces to $A\sin(\sqrt{2\lambda}x)$ via $\phi(0)=0$, and $\phi(\pi)=0$ forces $\sqrt{2\lambda} = n$, giving $\lambda_n = n^2/2$.

    Normalization: $\int_0^\pi \sin^2(nx)\,dx = \pi/2$, so $\phi_n(x) = \sqrt{2/\pi}\sin(nx)$. For $m\neq n$, $\int_0^\pi \sin(mx)\sin(nx)\,dx = \tfrac12\int_0^\pi[\cos((m-n)x) - \cos((m+n)x)]\,dx = 0$. Combined with the normalization, $\int \phi_m\phi_n\,dx = \delta_{mn}$.

---

**Exercise 2.**
For the heat equation on $[0,1]$ with Dirichlet conditions, write the spectral Green's function and compute the first three terms at $t=1$. Estimate how many terms are needed for $10^{-6}$ accuracy at $t=1$ versus $t=0.01$.

??? success "Solution to Exercise 2"
    With $L=1$, $\lambda_n = n^2\pi^2/2$ and $\phi_n = \sqrt{2}\sin(n\pi x)$, so

    $$
    G(t,x;0,y) = 2\sum_{n=1}^\infty e^{-n^2\pi^2 t/2}\sin(n\pi x)\sin(n\pi y).
    $$

    At $t=1$: $e^{-\pi^2/2}\approx 7.2\times 10^{-3}$, $e^{-2\pi^2}\approx 2.7\times 10^{-9}$, $e^{-9\pi^2/2}\approx 5.2\times 10^{-20}$. Two terms already give $\sim 10^{-9}$ accuracy; one term beats $10^{-6}$.

    At $t=0.01$: $e^{-n^2\pi^2/200}\approx e^{-0.0493 n^2}$, decaying much more slowly in $n$. Roughly $e^{-0.0493 n^2} < 10^{-6}$ requires $n^2 > 280$, i.e. about $n\geq 17$. Short time needs many more modes -- the image series is better there.

---

**Exercise 3.**
Explain why $\lambda_1$ controls the long-time decay rate of the Dirichlet Green's function, and relate $\lambda_1$ to the maturity decay of a double-barrier knock-out option on a corridor of log-width $L$.

??? success "Solution to Exercise 3"
    For large $t$ every term in $\sum_n e^{-\lambda_n t}\phi_n(x)\phi_n(y)$ is dominated by the slowest decay, $e^{-\lambda_1 t}$, with subleading terms suppressed by $e^{-(\lambda_2-\lambda_1)t}$. Thus

    $$
    G(t,x;0,y) \sim e^{-\lambda_1 t}\phi_1(x)\phi_1(y).
    $$

    **Double-barrier option**: the log-price lives on a corridor of width $L = \log(B_u/B_l)$, with Dirichlet Green's function on that interval. The principal eigenvalue is $\lambda_1 = \pi^2/(2L^2)$. For large maturity $T$, the knock-out price decays like $e^{-(\lambda_1 + r)T}$: the factor $\lambda_1$ is the probabilistic leakage rate through the barriers, and $r$ is discounting. Narrower corridors mean larger $\lambda_1$ and faster decay.

---

**Exercise 4.**
For the Sturm-Liouville problem $-\tfrac12\phi'' = \lambda\phi$ on $[0,1]$ with Neumann conditions, find all eigenpairs. Why does a $\lambda_0 = 0$ mode appear, and what does it imply about the long-time limit of the Green's function?

??? success "Solution to Exercise 4"
    The general solution $A\cos(\sqrt{2\lambda}x) + B\sin(\sqrt{2\lambda}x)$ subject to $\phi'(0)=0$ forces $B=0$, and $\phi'(1)=0$ requires $\sin(\sqrt{2\lambda})=0$, giving $\sqrt{2\lambda} = n\pi$ for $n = 0,1,2,\dots$. Hence $\lambda_n = n^2\pi^2/2$ with $\phi_0 = 1$ and $\phi_n = \sqrt{2}\cos(n\pi x)$ for $n\geq 1$.

    $\lambda_0 = 0$ arises because the constant function satisfies both $\phi''=0$ and the Neumann conditions -- Neumann boundaries do not pin the value anywhere, so a nonzero constant mode is admissible.

    As $t\to\infty$, all $n\geq 1$ modes decay exponentially and $G \to 1$ (uniform density on $[0,1]$). Total probability is conserved because the zero mode does not decay: reflecting boundaries keep mass inside, and the limit is the equilibrium distribution.

---

**Exercise 5.**
A short-rate model has generator with discrete spectrum $\{\lambda_n\}_{n\geq 0}$. Starting from the spectral expansion of bond prices $P(t,r;T) = \sum_n a_n(r)e^{-\lambda_n(T-t)}$, show that the long-maturity yield $Y(\tau) = -\log P/\tau$ converges to $\lambda_0$ as $\tau\to\infty$. What financial quantity is this?

??? success "Solution to Exercise 5"
    For large $\tau = T-t$, the term with smallest $\lambda_n$ dominates:

    $$
    P(t,r;T) \sim a_0(r)\,e^{-\lambda_0\tau}\left[1 + \tfrac{a_1(r)}{a_0(r)}e^{-(\lambda_1-\lambda_0)\tau} + \cdots\right].
    $$

    Taking logs and dividing by $\tau$,

    $$
    Y(\tau) = -\frac{\log P}{\tau} = \lambda_0 - \frac{\log a_0(r)}{\tau} + O(e^{-(\lambda_1-\lambda_0)\tau}/\tau) \to \lambda_0.
    $$

    Financially this is the **long rate** of the term structure: the asymptotic yield common to all starting states $r$. The spectral gap $\lambda_1 - \lambda_0$ sets how quickly the yield curve flattens to this long rate.

---

**Exercise 6.**
For an Ornstein-Uhlenbeck process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$, state the eigenfunctions and eigenvalues in the weighted space $L^2(m\,dx)$ with Gaussian stationary weight. Using only this eigenstructure (no explicit Gaussian formula), argue that the spectral gap equals the mean-reversion rate.

??? success "Solution to Exercise 6"
    With stationary density $m(x) = \sqrt{\kappa/\pi\sigma^2}\,\exp(-\kappa x^2/\sigma^2)$, the generator $\mathcal{L} = -\kappa x\partial_x + \tfrac12\sigma^2\partial_{xx}$ is self-adjoint in $L^2(m\,dx)$. The eigenfunctions are the Hermite polynomials $H_n$ (orthonormalized against $m$), with eigenvalues $\lambda_n = n\kappa$ for $n = 0,1,2,\dots$. The $n=0$ mode is the constant function (the stationary density itself under the weight).

    The spectral gap is $\lambda_1 - \lambda_0 = \kappa - 0 = \kappa$. Any mean-zero perturbation of the stationary density lives in the span of $H_n$ for $n\geq 1$, and the slowest such mode decays as $e^{-\kappa t}$. So any deviation from equilibrium relaxes at rate $\kappa$ -- exactly the mean-reversion rate. The eigenstructure alone reproduces the familiar OU relaxation timescale without computing any densities.
