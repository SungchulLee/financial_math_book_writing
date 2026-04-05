# Separation of Variables

The heat equation derivation solved the Black-Scholes PDE by transforming it into a known equation with a known Green's function. Separation of variables takes a different classical approach: instead of transforming the PDE, it **decomposes the solution** into a product of functions, each depending on a single variable. For the Black--Scholes equation on unbounded domains, this decomposition leads naturally to the Fourier integral rather than a discrete eigenfunction series. For vanilla options on unbounded domains, the method reduces to the Fourier transform --- the discrete eigenvalues become a continuous spectrum and the series becomes an integral. The method is therefore most effective on **bounded domains** (barrier options), where it yields genuine spectral expansions, and provides valuable **spectral intuition** for understanding solution structure more broadly.

---

## 1. General Theory of Separation of Variables

### 1.1 The Method

For a PDE in two variables, assume the solution has the **product form**:

$$
u(x,t) = X(x) T(t)
$$

Substitute into the PDE and separate variables to obtain:

$$
\frac{\text{function of } t \text{ only}}{\text{function of } x \text{ only}} = \text{constant}
$$

This yields **two ODEs** that can be solved independently.

### 1.2 The Separation Constant

The constant $\lambda$ (separation constant) is determined by:

1. **Boundary conditions** in space
2. **Self-adjoint operators** giving real eigenvalues
3. **Sturm--Liouville theory** giving orthogonal eigenfunctions

### 1.3 General Solution

The general solution is a **superposition** of separated solutions:

$$
u(x,t) = \sum_{n=0}^{\infty} c_n X_n(x) T_n(t)
$$

where coefficients $c_n$ are determined by initial or terminal conditions.

---

## 2. Black--Scholes PDE Setup

### 2.1 The Equation

$$
\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV = 0
$$

Terminal condition: $V(S,T) = \Phi(S)$.

### 2.2 Domain Considerations

The stock price domain is $S \in (0, \infty)$, which is semi-infinite. Standard separation of variables requires a **finite interval** $[a,b]$ where boundary conditions at both ends provide discrete eigenvalues and orthogonal eigenfunctions.

On infinite domains, the discrete spectrum is replaced by a continuous spectrum, and Fourier series give way to Fourier transforms. Separation of variables is therefore **most naturally suited to bounded-domain problems** such as barrier options.

---

## 3. Logarithmic Transformation

### 3.1 Change to Log-Price

Define $x = \ln S$ and $\tau = T - t$. The PDE becomes:

$$
\frac{\partial V}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 V}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial V}{\partial x} - rV
$$

Domain: $x \in (-\infty, \infty)$ with initial condition $V(x,0) = \Phi(e^x)$.

### 3.2 Separation Ansatz

Try $V(x,\tau) = X(x)T(\tau)$. Substituting and dividing by $X(x)T(\tau)$:

$$
\frac{T'(\tau)}{T(\tau)} = \frac{\frac{\sigma^2}{2}X''(x) + \left(r-\frac{\sigma^2}{2}\right)X'(x) - rX(x)}{X(x)} = -\lambda
$$

### 3.3 Two ODEs

**Time equation**:

$$
T'(\tau) + \lambda T(\tau) = 0
$$

Solution: $T(\tau) = C e^{-\lambda\tau}$.

**Space equation**:

$$
\frac{\sigma^2}{2}X''(x) + \left(r - \frac{\sigma^2}{2}\right)X'(x) + (\lambda - r)X(x) = 0
$$

---

## 4. The Spatial Eigenvalue Problem

### 4.1 Characteristic Equation

The space equation is a second-order linear ODE with constant coefficients. Substituting $X(x) = e^{\mu x}$:

$$
\frac{\sigma^2}{2}\mu^2 + \left(r - \frac{\sigma^2}{2}\right)\mu + (\lambda - r) = 0
$$

Define the discriminant:

$$
\Delta^2 = \left(r - \frac{\sigma^2}{2}\right)^2 - 2\sigma^2(\lambda - r)
$$

Then the characteristic roots are:

$$
\mu_{\pm} = \frac{-\left(r-\frac{\sigma^2}{2}\right) \pm \Delta}{\sigma^2}
$$

### 4.2 Nature of Solutions

If $\Delta^2 > 0$ (real roots), the solutions are exponentials $X(x) = Ae^{\mu_+ x} + Be^{\mu_- x}$.

If $\Delta^2 < 0$ (complex roots), the solutions are oscillatory, involving sine and cosine functions modulated by an exponential envelope.

### 4.3 Continuous Spectrum on Unbounded Domains

For $x \in (-\infty, \infty)$, boundedness requirements leave no nontrivial solutions for discrete $\lambda$ values. The eigenvalue parameter ranges over a continuous set, and the discrete sum $\sum_n$ is replaced by a Fourier integral. This is precisely why the **Fourier transform** is the natural tool for vanilla Black--Scholes on the full real line.

---

## 5. Bounded Domains: Barrier Options

Separation of variables becomes fully effective when the domain is finite, as occurs naturally for barrier options.

### 5.1 Down-and-Out Option

Consider a barrier option with $S \in [B, S_{\max}]$ where $B$ is a knock-out barrier.

In log-space: $x \in [x_B, x_{\max}]$ where $x_B = \ln B$.

**Boundary conditions**:

- $V(x_B, \tau) = 0$ (knocked out)
- $V(x_{\max}, \tau) = $ appropriate asymptotic value

### 5.2 Discrete Eigenvalues

The spatial ODE

$$
\frac{\sigma^2}{2}X''(x) + \left(r - \frac{\sigma^2}{2}\right)X'(x) + (\lambda - r)X(x) = 0
$$

with $X(x_B) = X(x_{\max}) = 0$ now has **discrete eigenvalues** $\lambda_n$.

### 5.3 Sturm--Liouville Problem

This is a Sturm--Liouville eigenvalue problem $\mathcal{L}X = \lambda X$ with the operator:

$$
\mathcal{L} = -\frac{\sigma^2}{2}\frac{d^2}{dx^2} - \left(r - \frac{\sigma^2}{2}\right)\frac{d}{dx} + r
$$

### 5.4 Self-Adjoint Form

To obtain a self-adjoint formulation, introduce the weight function:

$$
w(x) = \exp\left[\frac{2r - \sigma^2}{\sigma^2}x\right]
$$

The weighted inner product

$$
\langle f, g \rangle = \int_{x_B}^{x_{\max}} f(x) g(x) w(x)\,dx
$$

makes $\mathcal{L}$ self-adjoint, guaranteeing real eigenvalues and orthogonal eigenfunctions.

---

## 6. Eigenfunction Expansion on Bounded Domains

### 6.1 Complete Orthogonal System

For the Sturm--Liouville problem with homogeneous boundary conditions:

- Eigenvalues: $0 < \lambda_1 < \lambda_2 < \lambda_3 < \cdots$
- Eigenfunctions: $X_n(x)$ satisfying $\mathcal{L}X_n = \lambda_n X_n$
- **Orthogonality**: $\langle X_m, X_n \rangle = 0$ for $m \neq n$

### 6.2 General Solution

$$
V(x,\tau) = \sum_{n=1}^{\infty} c_n X_n(x) e^{-\lambda_n \tau}
$$

### 6.3 Determining Coefficients

At $\tau = 0$ (terminal condition):

$$
V(x,0) = \Phi(e^x) = \sum_{n=1}^{\infty} c_n X_n(x)
$$

By orthogonality:

$$
c_n = \frac{\langle \Phi(e^x), X_n(x) \rangle}{\langle X_n, X_n \rangle} = \frac{\int_{x_B}^{x_{\max}} \Phi(e^x) X_n(x) w(x)\,dx}{\int_{x_B}^{x_{\max}} X_n^2(x) w(x)\,dx}
$$

---

## 7. Explicit Example: Heat Equation on a Bounded Interval

### 7.1 Setup

Consider the simplified equation:

$$
\frac{\partial V}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 V}{\partial x^2}
$$

on $x \in [0, L]$ with $V(0,\tau) = V(L,\tau) = 0$.

### 7.2 Separation

Setting $V(x,\tau) = X(x)T(\tau)$ gives:

$$
\frac{T'}{\frac{\sigma^2}{2}T} = \frac{X''}{X} = -\lambda
$$

### 7.3 Spatial Problem

$$
X'' + \lambda X = 0, \quad X(0) = X(L) = 0
$$

Eigenvalues:

$$
\lambda_n = \left(\frac{n\pi}{L}\right)^2, \quad n = 1, 2, 3, \ldots
$$

Eigenfunctions:

$$
X_n(x) = \sin\left(\frac{n\pi x}{L}\right)
$$

### 7.4 Temporal Solution

$$
T_n(\tau) = e^{-\frac{\sigma^2}{2}\left(\frac{n\pi}{L}\right)^2 \tau}
$$

### 7.5 General Solution

$$
V(x,\tau) = \sum_{n=1}^{\infty} c_n \sin\left(\frac{n\pi x}{L}\right) e^{-\frac{\sigma^2}{2}\left(\frac{n\pi}{L}\right)^2 \tau}
$$

with:

$$
c_n = \frac{2}{L}\int_0^L \Phi(e^x) \sin\left(\frac{n\pi x}{L}\right) dx
$$

---

## 8. Connection to Fourier Transform

### 8.1 Limit as the Domain Grows

As $L \to \infty$, the discrete spectrum becomes continuous:

$$
\lambda_n = \left(\frac{n\pi}{L}\right)^2 \to \omega^2 \quad (\text{continuous } \omega)
$$

The sum becomes an integral:

$$
\sum_{n=1}^{\infty} \to \int_{-\infty}^{\infty} d\omega
$$

The eigenfunctions become complex exponentials:

$$
\sin\left(\frac{n\pi x}{L}\right) \to e^{i\omega x}
$$

### 8.2 Fourier Transform Representation

$$
V(x,\tau) = \frac{1}{2\pi}\int_{-\infty}^{\infty} \hat{V}(\omega, 0)\, e^{-\frac{\sigma^2 \omega^2 \tau}{2}}\, e^{i\omega x}\, d\omega
$$

This recovers the Fourier transform solution.

### 8.3 Unified Perspective

Separation of variables on **finite domains** yields Fourier series (discrete).
Separation of variables on **infinite domains** yields Fourier transforms (continuous).

The two are related by a limiting process, and the Fourier transform solution of Black--Scholes is, in this sense, the continuous-spectrum version of separation of variables.

---

## 9. Multi-Dimensional Separation

### 9.1 Two-Asset Option

For $V(S_1, S_2, t)$ satisfying:

$$
\frac{\partial V}{\partial t} + \mathcal{L}_1 V + \mathcal{L}_2 V + \rho\sigma_1\sigma_2 S_1 S_2\frac{\partial^2 V}{\partial S_1 \partial S_2} - rV = 0
$$

the **mixed derivative term** prevents simple separation unless $\rho = 0$.

### 9.2 Uncorrelated Case

With $\rho = 0$, one can separate:

$$
\frac{\mathcal{L}_1 V_1}{V_1} = -\lambda_1, \quad \frac{\mathcal{L}_2 V_2}{V_2} = -\lambda_2, \quad \frac{T'}{T} = -(\lambda_1 + \lambda_2 - r)
$$

giving:

$$
V(S_1, S_2, t) = \sum_{m,n} c_{mn} X_m(S_1) Y_n(S_2)\, e^{-(\lambda_m + \lambda_n - r)(T-t)}
$$

### 9.3 Correlated Case

When $\rho \neq 0$, diagonalize the covariance matrix via rotation (principal components) to decouple the variables, then apply separation in the transformed coordinates.

---

## 10. Barrier Options via Separation

### 10.1 Down-and-Out Call

Domain: $S \in [B, \infty)$ with $V(B,t) = 0$.

Since the domain is semi-infinite, approximate by $S \in [B, S_{\max}]$ for large $S_{\max}$, with:

- $V(B,t) = 0$ (knock-out)
- $V(S_{\max}, t) = S_{\max} - K$ (deep in-the-money)

Standard eigenfunction expansion then applies on the truncated domain.

### 10.2 Comparison with Method of Images

The **method of images** gives the exact price:

$$
V(S,t) = C_{\text{BS}}(S,t) - \left(\frac{B}{S}\right)^{2r/\sigma^2} C_{\text{BS}}\left(\frac{B^2}{S}, t\right)
$$

This closed-form result is simpler than a truncated eigenfunction series, illustrating that for problems admitting analytical solutions via other techniques, separation of variables may not be the most efficient route.

---

## 11. Practical Example: Box Spread

### 11.1 Setup

Consider a bounded domain $S \in [S_L, S_U]$ with constant boundary conditions:

- $V(S_L, t) = A$
- $V(S_U, t) = B$

### 11.2 Reduction to Homogeneous Boundaries

Define $W(S,t) = V(S,t) - A - \frac{B-A}{S_U - S_L}(S - S_L)$ so that $W(S_L,t) = W(S_U,t) = 0$.

Now $W$ satisfies a homogeneous boundary value problem amenable to eigenfunction expansion.

### 11.3 Eigenfunction Expansion

$$
W(S,t) = \sum_{n=1}^{\infty} c_n(t) \phi_n(S)
$$

where $\phi_n$ are eigenfunctions of $\mathcal{L}\phi_n = \lambda_n \phi_n$ with $\phi_n(S_L) = \phi_n(S_U) = 0$, and:

$$
c_n(t) = c_n(T) e^{-\lambda_n(T-t)}
$$

The terminal coefficients $c_n(T)$ are obtained by projecting the payoff onto the eigenbasis.

---

## 12. Computational Aspects

### 12.1 Computing Eigenvalues

For the Sturm--Liouville problem with boundary conditions, two standard numerical approaches are available.

**Shooting method**:

1. Guess $\lambda$
2. Integrate the ODE from $x_L$ to $x_R$
3. Check whether the boundary condition at $x_R$ is satisfied
4. Iterate to find $\lambda$ values for which it is

**Finite difference discretization**:

1. Discretize: $X_j \approx X(x_j)$
2. Obtain a matrix eigenvalue problem: $\mathbf{A}\mathbf{X} = \lambda\mathbf{X}$
3. Solve with standard eigenvalue algorithms

### 12.2 Computing Coefficients

The projection $c_n = \frac{\langle \Phi, \phi_n \rangle}{\langle \phi_n, \phi_n \rangle}$ requires numerical integration (e.g., Gaussian quadrature).

### 12.3 Series Truncation

In practice, truncate the expansion:

$$
V(x,\tau) \approx \sum_{n=1}^{N} c_n \phi_n(x) e^{-\lambda_n \tau}
$$

**Error estimate**:

$$
\left|V - V_N\right| \leq \sum_{n=N+1}^{\infty} |c_n| e^{-\lambda_n \tau} \leq C e^{-\lambda_{N+1} \tau}
$$

The exponential decay in $\tau$ ensures **rapid convergence** away from $\tau = 0$.

---

## 13. Four Representations of the Solution Operator

The various solution methods for linear parabolic PDEs are different representations of the same object:

$$
\begin{align}
&\text{Separation (finite domain)} \longleftrightarrow \text{Fourier series} \\
&\quad\downarrow \text{(limit } L \to \infty) \\
&\text{Separation (infinite domain)} \longleftrightarrow \text{Fourier transform} \\
&\quad\downarrow \text{(Green's function)} \\
&\text{Fundamental solution} \longleftrightarrow \text{Heat kernel} \\
&\quad\downarrow \text{(probabilistic)} \\
&\text{Transition density} \longleftrightarrow \text{Feynman--Kac}
\end{align}
$$

For the solution operator $e^{\tau\mathcal{L}}$ applied to initial data $V_0$:

$$
e^{\tau\mathcal{L}} V_0 = \begin{cases}
\displaystyle\sum_{n} e^{\tau\lambda_n} \langle V_0, \phi_n \rangle \phi_n & \text{(discrete spectrum)} \\[6pt]
\displaystyle\int e^{\tau\lambda} \langle V_0, \phi_\lambda \rangle \phi_\lambda\, d\lambda & \text{(continuous spectrum)} \\[6pt]
\displaystyle\int G(x, y, \tau) V_0(y)\, dy & \text{(Green's function)} \\[6pt]
\mathbb{E}[V_0(X_\tau)] & \text{(probabilistic)}
\end{cases}
$$

These are four representations of the **same solution operator**. The choice among them depends on the problem:

- **Discrete spectrum** (barrier options) --- eigenfunction expansion / Fourier series
- **Continuous spectrum** (vanilla options) --- Fourier transform
- **Non-smooth payoffs** --- Green's function convolution
- **Exotic / path-dependent options** --- Feynman--Kac / Monte Carlo

---

## 14. Summary

Separation of variables for the Black--Scholes PDE is **most effective on bounded domains** with homogeneous boundary conditions, where it yields a discrete eigenfunction expansion with exponentially convergent series. For vanilla options on unbounded domains, the method leads naturally to continuous-spectrum representations (Fourier transforms), which are handled more directly by transform techniques.

| Situation | Method of choice |
|-----------|-----------------|
| Bounded domain, homogeneous BCs | Eigenfunction expansion |
| Unbounded domain | Fourier / Laplace transform |
| Non-constant or time-dependent coefficients | Numerical PDE methods |
| Path-dependent options | Feynman--Kac / Monte Carlo |

For barrier options specifically, the eigenfunction approach competes with the method of images (when available) and numerical PDE solvers. Its main value lies in providing **structural insight**: it reveals how the spectrum of the spatial operator governs the time decay of each mode, and it connects finite-domain Fourier series to infinite-domain Fourier transforms through a single limiting process. In the operator framework of the introduction, the eigenfunction expansion represents the pricing semigroup $\mathcal{P}_\tau = e^{\tau\mathcal{L}}$ through its **spectral decomposition** on bounded domains.

---

## Exercises

**Exercise 1.** For the heat equation $\frac{\partial F}{\partial \tau} = \frac{1}{2}\sigma^2 \frac{\partial^2 F}{\partial x^2}$ on the domain $x \in (a, b)$ with $F(a, \tau) = F(b, \tau) = 0$ (a double-barrier knock-out option), apply separation of variables to show that the eigenvalues are $\lambda_n = -\frac{1}{2}\sigma^2 \left(\frac{n\pi}{b-a}\right)^2$ for $n = 1, 2, \ldots$ and the eigenfunctions are $\sin\left(\frac{n\pi(x-a)}{b-a}\right)$.

??? success "Solution to Exercise 1"
    On $x \in (a,b)$ with $F(a,\tau) = F(b,\tau) = 0$, substitute $F(x,\tau) = X(x)T(\tau)$:

    $$
    X(x)T'(\tau) = \frac{1}{2}\sigma^2 X''(x)T(\tau)
    $$

    Divide by $X(x)T(\tau)$:

    $$
    \frac{T'(\tau)}{T(\tau)} = \frac{\frac{1}{2}\sigma^2 X''(x)}{X(x)} = -\mu
    $$

    for some separation constant $\mu$.

    **Spatial ODE:** $X'' + \frac{2\mu}{\sigma^2}X = 0$ with $X(a) = X(b) = 0$.

    Let $k^2 = \frac{2\mu}{\sigma^2}$. The general solution is $X(x) = A\sin(k(x-a)) + B\cos(k(x-a))$.

    Boundary condition $X(a) = 0$ gives $B = 0$. Boundary condition $X(b) = 0$ gives $\sin(k(b-a)) = 0$, so:

    $$
    k_n = \frac{n\pi}{b-a}, \quad n = 1, 2, 3, \ldots
    $$

    The eigenvalues are $\mu_n = \frac{\sigma^2 k_n^2}{2} = \frac{\sigma^2}{2}\left(\frac{n\pi}{b-a}\right)^2$, and since the time equation is $T' = -\mu T$:

    $$
    \lambda_n = -\mu_n = -\frac{1}{2}\sigma^2\left(\frac{n\pi}{b-a}\right)^2
    $$

    The eigenfunctions are:

    $$
    X_n(x) = \sin\left(\frac{n\pi(x-a)}{b-a}\right)
    $$

---
**Exercise 2.** Using the eigenvalue decomposition from Exercise 1, write the solution for a European call option knocked out at barriers $S = B_l$ and $S = B_u$ (with $B_l < K < B_u$) as a Fourier sine series. Discuss the convergence rate of this series for smooth vs. non-smooth initial conditions.

??? success "Solution to Exercise 2"
    Using the eigenvalue decomposition, the solution for a double-barrier knock-out call in log-price space $x = \ln S$, with barriers at $x_l = \ln B_l$ and $x_u = \ln B_u$:

    $$
    F(x,\tau) = \sum_{n=1}^{\infty}c_n \sin\left(\frac{n\pi(x - x_l)}{x_u - x_l}\right)\exp\left(-\frac{\sigma^2}{2}\left(\frac{n\pi}{x_u - x_l}\right)^2\tau\right)
    $$

    The coefficients are determined by the initial condition $F(x,0) = (e^x - K)^+$ (after accounting for the drift removal and discounting transformations):

    $$
    c_n = \frac{2}{x_u - x_l}\int_{x_l}^{x_u}(e^z - K)^+\sin\left(\frac{n\pi(z-x_l)}{x_u - x_l}\right)dz
    $$

    Since the payoff is non-zero only for $z > \ln K$:

    $$
    c_n = \frac{2}{x_u - x_l}\int_{\ln K}^{x_u}(e^z - K)\sin\left(\frac{n\pi(z - x_l)}{x_u - x_l}\right)dz
    $$

    **Convergence rate:** For a smooth initial condition (e.g., the payoff is $C^{\infty}$), the Fourier sine coefficients $c_n$ decay as $O(n^{-k})$ for any $k$, giving spectral (super-polynomial) convergence. For the call payoff, which has a kink at $S = K$ (i.e., $\Phi''$ has a delta function), $c_n \sim O(n^{-2})$. This means the series converges as $O(1/N^2)$ for $N$ terms when $\tau = 0$, but for $\tau > 0$, the exponential decay $e^{-cn^2\tau}$ dramatically accelerates convergence.

---
**Exercise 3.** Explain why separation of variables with a discrete spectrum arises naturally for barrier options (bounded domain) but not for vanilla European options (unbounded domain). What replaces the discrete eigenvalue sum in the unbounded case?

??? success "Solution to Exercise 3"
    **Bounded domain (barrier options).** When barriers at $B_l$ and $B_u$ bound the stock price, the log-price domain $[\ln B_l, \ln B_u]$ is finite. The spatial operator with homogeneous Dirichlet boundary conditions has a **discrete spectrum**: eigenvalues $\lambda_1 < \lambda_2 < \cdots$ accumulating at $-\infty$, with corresponding eigenfunctions forming a complete orthonormal basis. The solution is a Fourier sine series (discrete sum).

    **Unbounded domain (vanilla options).** For vanilla European options, $S \in (0,\infty)$ so $x = \ln S \in (-\infty, \infty)$. There are no boundary conditions to constrain the eigenvalues, so the spectrum is **continuous**: every $\lambda \leq 0$ is in the spectrum. The eigenfunctions $e^{i\omega x}$ are not square-integrable (they are generalized eigenfunctions).

    **What replaces the discrete sum.** The discrete eigenvalue sum $\sum_{n=1}^{\infty}c_n X_n(x)e^{-\lambda_n\tau}$ is replaced by the continuous Fourier integral:

    $$
    V(x,\tau) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{V}(\omega,0)e^{\psi(\omega)\tau}e^{i\omega x}d\omega
    $$

    This is the Fourier transform solution. The discrete-to-continuous transition is a manifestation of the general principle in spectral theory: as the domain $[a,b] \to (-\infty,\infty)$, the eigenvalue spacing $\Delta\lambda \sim \pi^2/(b-a)^2 \to 0$ and the sum becomes an integral.

---
**Exercise 4.** Consider the Black--Scholes PDE after the change of variables to the heat equation. Substitute $F(x,\tau) = X(x)T(\tau)$ and derive the two ODEs. Solve each ODE explicitly, identifying the separation constant $\lambda$.

??? success "Solution to Exercise 4"
    Starting from the heat equation $\frac{\partial F}{\partial \tau} = \frac{1}{2}\sigma^2\frac{\partial^2 F}{\partial x^2}$, substitute $F(x,\tau) = X(x)T(\tau)$:

    $$
    X(x)T'(\tau) = \frac{1}{2}\sigma^2 X''(x)T(\tau)
    $$

    Divide by $XT$:

    $$
    \frac{T'(\tau)}{T(\tau)} = \frac{\sigma^2}{2}\frac{X''(x)}{X(x)} = -\lambda
    $$

    **Time ODE:** $T' + \lambda T = 0$, with solution:

    $$
    T(\tau) = Ce^{-\lambda\tau}
    $$

    **Spatial ODE:** $\frac{\sigma^2}{2}X'' + \lambda X = 0$, or equivalently $X'' + \frac{2\lambda}{\sigma^2}X = 0$.

    For $\lambda > 0$: Let $k^2 = 2\lambda/\sigma^2$. Then $X(x) = A\cos(kx) + B\sin(kx)$, or equivalently $X(x) = Ce^{ikx} + De^{-ikx}$.

    For $\lambda < 0$: Let $\kappa^2 = -2\lambda/\sigma^2$. Then $X(x) = Ae^{\kappa x} + Be^{-\kappa x}$ (exponential solutions, not bounded on $\mathbb{R}$).

    For $\lambda = 0$: $X(x) = Ax + B$.

    On the infinite domain, boundedness requires $\lambda \geq 0$, and $k$ ranges continuously over $\mathbb{R}$, recovering the Fourier transform representation. The separation constant $\lambda = \frac{\sigma^2 k^2}{2}$ parametrizes the continuous spectrum.

---
**Exercise 5.** The four equivalent representations of the solution operator -- eigenfunction expansion, Fourier integral, Green's function, and probabilistic expectation -- are listed in the summary. For a European call on the domain $x \in (-\infty, \infty)$, verify that the Green's function representation (convolution with Gaussian) and the Fourier transform representation yield the same answer.

??? success "Solution to Exercise 5"
    **Green's function representation.** The solution is:

    $$
    V(x,\tau) = \int_{-\infty}^{\infty}\Phi(y)G(x-y,\tau)dy
    $$

    where $G(x,\tau) = \frac{1}{\sqrt{2\pi\sigma^2\tau}}e^{-x^2/(2\sigma^2\tau)}$.

    **Fourier transform representation.** The solution is:

    $$
    V(x,\tau) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{\Phi}(\omega)e^{-\sigma^2\omega^2\tau/2}e^{i\omega x}d\omega
    $$

    **Equivalence.** By the convolution theorem, $V = \Phi * G$ in real space corresponds to $\hat{V} = \hat{\Phi} \cdot \hat{G}$ in Fourier space. The Fourier transform of the Gaussian kernel is:

    $$
    \hat{G}(\omega,\tau) = \int_{-\infty}^{\infty}\frac{1}{\sqrt{2\pi\sigma^2\tau}}e^{-x^2/(2\sigma^2\tau)}e^{-i\omega x}dx = e^{-\sigma^2\omega^2\tau/2}
    $$

    Therefore:

    $$
    V(x,\tau) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{\Phi}(\omega)\hat{G}(\omega,\tau)e^{i\omega x}d\omega = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{\Phi}(\omega)e^{-\sigma^2\omega^2\tau/2}e^{i\omega x}d\omega
    $$

    Applying the inverse Fourier transform of the product $\hat{\Phi}\cdot\hat{G}$ gives the convolution $\Phi * G$, confirming both representations are identical.

---
**Exercise 6.** For a down-and-out call with barrier at $S = B$ (where $B < K$), describe how the method of images can be used instead of separation of variables to satisfy the boundary condition $V(B, t) = 0$. What is the "image" solution, and how does the final formula relate to the standard Black--Scholes price?

??? success "Solution to Exercise 6"
    **Method of images.** The idea is to construct a solution that automatically satisfies $V(B,t) = 0$ by adding an "image" solution that cancels the original at $S = B$.

    Start with the standard Black--Scholes call price $C_{\text{BS}}(S,K,\tau)$. The "image" of a point source at $S$ reflected in the barrier $B$ is $B^2/S$ (in the stock price domain). The image solution is:

    $$
    V_{\text{image}}(S,t) = \left(\frac{B}{S}\right)^{2r/\sigma^2 - 1}C_{\text{BS}}\left(\frac{B^2}{S}, K, \tau\right)
    $$

    The power $\left(\frac{B}{S}\right)^{2r/\sigma^2 - 1}$ is chosen so that $V_{\text{image}}$ also satisfies the Black--Scholes PDE (this exponent arises from the drift term in the PDE).

    **Down-and-out call price:**

    $$
    V_{\text{DO}}(S,t) = C_{\text{BS}}(S,K,\tau) - \left(\frac{B}{S}\right)^{2r/\sigma^2 - 1}C_{\text{BS}}\left(\frac{B^2}{S}, K, \tau\right)
    $$

    **Verification at $S = B$:** When $S = B$:

    $$
    V_{\text{DO}}(B,t) = C_{\text{BS}}(B,K,\tau) - (1)^{2r/\sigma^2 - 1}C_{\text{BS}}(B,K,\tau) = 0
    $$

    The boundary condition is satisfied. The formula gives the exact price of a continuously-monitored down-and-out call option under GBM, and it is simpler than the eigenfunction expansion approach since it requires no series truncation or computation of eigenvalues.
