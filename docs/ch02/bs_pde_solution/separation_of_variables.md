# Separation of Variables: Complete Mathematical Treatment

Separation of variables is a **classical technique** for solving PDEs by reducing them to ordinary differential equations. While powerful, its application to Black-Scholes reveals both the **elegance and limitations** of this method.

---

## **1. General Theory of Separation of Variables**

### **The Method**

For a PDE in two variables, assume the solution has the **product form**:
$$\boxed{u(x,t) = X(x)T(t)}$$

Substitute into the PDE and separate variables to obtain:
$$\frac{\text{function of } t \text{ only}}{\text{function of } x \text{ only}} = \text{constant}$$

This yields **two ODEs** that can be solved independently.

### **The Separation Constant**

The constant $\lambda$ (separation constant) is determined by:
1. **Boundary conditions** in space
2. **Self-adjoint operators** → real eigenvalues
3. **Sturm-Liouville theory** → orthogonal eigenfunctions

### **General Solution**

The general solution is a **superposition** of separated solutions:
$$\boxed{u(x,t) = \sum_{n=0}^{\infty} c_n X_n(x)T_n(t)}$$

where coefficients $c_n$ are determined by initial/terminal conditions.

---

## **2. Black-Scholes PDE Setup**

### **The Equation**

$$\boxed{\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV = 0}$$

Terminal condition: $V(S,T) = \Phi(S)$

### **Obstacle: Infinite Domain**

The stock price domain is $S \in (0, \infty)$ — **semi-infinite**.

Standard separation of variables works best on **finite intervals** $[a,b]$ where boundary conditions at both ends provide:
- Discrete eigenvalues $\lambda_n$
- Orthogonal eigenfunctions
- Fourier series expansions

For infinite domains, we get:
- **Continuous spectrum** instead of discrete
- **Fourier transforms** instead of Fourier series
- More complex analysis required

---

## **3. Logarithmic Transformation**

### **Change to Log-Price**

Define $x = \ln S$ and $\tau = T - t$. The PDE becomes:
$$\boxed{\frac{\partial V}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 V}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial V}{\partial x} - rV}$$

Domain: $x \in (-\infty, \infty)$ with initial condition $V(x,0) = \Phi(e^x)$.

### **Separation Ansatz**

Try:
$$V(x,\tau) = X(x)T(\tau)$$

Substituting:
$$X(x)T'(\tau) = \frac{\sigma^2}{2}X''(x)T(\tau) + \left(r - \frac{\sigma^2}{2}\right)X'(x)T(\tau) - rX(x)T(\tau)$$

Divide by $X(x)T(\tau)$:
$$\boxed{\frac{T'(\tau)}{T(\tau)} = \frac{\frac{\sigma^2}{2}X''(x) + (r-\frac{\sigma^2}{2})X'(x) - rX(x)}{X(x)} = -\lambda}$$

### **Two ODEs**

**Time equation**:
$$\boxed{T'(\tau) + \lambda T(\tau) = 0}$$

Solution: $T(\tau) = C e^{-\lambda\tau}$

**Space equation** (Sturm-Liouville form):
$$\boxed{\frac{\sigma^2}{2}X''(x) + \left(r - \frac{\sigma^2}{2}\right)X'(x) + (\lambda - r)X(x) = 0}$$

---

## **4. The Spatial Eigenvalue Problem**

### **Standard Form**

Rewrite as:
$$\frac{\sigma^2}{2}X''(x) + \left(r - \frac{\sigma^2}{2}\right)X'(x) + (\lambda - r)X(x) = 0$$

This is a **second-order linear ODE with constant coefficients**.

### **Characteristic Equation**

Try $X(x) = e^{\mu x}$:
$$\frac{\sigma^2}{2}\mu^2 + \left(r - \frac{\sigma^2}{2}\right)\mu + (\lambda - r) = 0$$

Solve for $\mu$:
$$\mu = \frac{-\left(r - \frac{\sigma^2}{2}\right) \pm \sqrt{\left(r-\frac{\sigma^2}{2}\right)^2 - 2\sigma^2(\lambda-r)}}{\sigma^2}$$

$$\boxed{\mu_{\pm} = \frac{1}{\sigma^2}\left[-\left(r - \frac{\sigma^2}{2}\right) \pm \sqrt{\left(r-\frac{\sigma^2}{2}\right)^2 - 2\sigma^2(\lambda-r)}\right]}$$

### **Simplification**

Let $k = \frac{2r}{\sigma^2}$ (as before). Then:
$$\mu_{\pm} = \frac{1}{2}\left[-(k-1) \pm \sqrt{(k-1)^2 + 4(\lambda/\frac{\sigma^2}{2} - k)}\right]$$

$$= \frac{1}{2}\left[-(k-1) \pm \sqrt{(k-1)^2 - 4k + 4\lambda/\frac{\sigma^2}{2}}\right]$$

$$= \frac{1}{2}\left[-(k-1) \pm \sqrt{(k+1)^2 - 4(k+1) + 4\lambda/\frac{\sigma^2}{2}}\right]$$

This is getting messy. Let's denote:
$$\boxed{\Delta^2 = \left(r-\frac{\sigma^2}{2}\right)^2 - 2\sigma^2(\lambda-r)}$$

Then:
$$\mu_{\pm} = \frac{-\left(r-\frac{\sigma^2}{2}\right) \pm \Delta}{\sigma^2}$$

---

## **5. The Problem: Continuous Spectrum**

### **Boundary Conditions**

For $x \in (-\infty, \infty)$, we need:
- $V$ bounded as $x \to -\infty$ (as $S \to 0$)
- $V$ bounded as $x \to \infty$ (as $S \to \infty$)

### **Issue with Exponential Solutions**

If $\lambda$ is such that $\Delta$ is **real**:
$$X(x) = A e^{\mu_+ x} + B e^{\mu_- x}$$

For boundedness:
- If $\mu_+ > 0$: need $A = 0$ to avoid explosion as $x \to \infty$
- If $\mu_- < 0$: need $B = 0$ to avoid explosion as $x \to -\infty$

But this leaves only trivial solutions unless we're very careful about $\lambda$.

### **Continuous Spectrum**

For an infinite domain, there are **no discrete eigenvalues** in general. Instead:
- $\lambda$ ranges over a **continuous set** (the spectrum)
- "Eigenfunctions" are **generalized functions** (distributions)
- The sum $\sum_n$ becomes an **integral** (Fourier transform)

This is why **Fourier transform** is more natural than separation of variables for Black-Scholes!

---

## **6. Case with Barriers: Finite Domain**

### **Down-and-Out Option**

Consider a barrier option with $S \in [B, S_{\max}]$ where $B$ is a knock-out barrier.

In log-space: $x \in [x_B, x_{\max}]$ where $x_B = \ln B$.

**Boundary conditions**:
- $V(x_B, \tau) = 0$ (knocked out)
- $V(x_{\max}, \tau) = $ something appropriate (e.g., $\sim S - K$)

### **Discrete Eigenvalues**

Now the spatial ODE:
$$\frac{\sigma^2}{2}X''(x) + \left(r - \frac{\sigma^2}{2}\right)X'(x) + (\lambda - r)X(x) = 0$$

with $X(x_B) = X(x_{\max}) = 0$ has **discrete eigenvalues** $\lambda_n$.

### **Sturm-Liouville Problem**

This is a **Sturm-Liouville problem**:
$$\mathcal{L}X = \lambda X$$

with the operator:
$$\mathcal{L} = -\frac{\sigma^2}{2}\frac{d^2}{dx^2} - \left(r - \frac{\sigma^2}{2}\right)\frac{d}{dx} + r$$

### **Self-Adjoint Form**

To make it self-adjoint, use the weight function:
$$w(x) = \exp\left[\frac{2(r-\frac{\sigma^2}{2})}{\sigma^2}x\right] = \exp\left[\frac{2r - \sigma^2}{\sigma^2}x\right]$$

The weighted inner product:
$$\langle f, g \rangle = \int_{x_B}^{x_{\max}} f(x)g(x)w(x)dx$$

makes $\mathcal{L}$ self-adjoint.

---

## **7. Eigenfunction Expansion (Bounded Domain)**

### **Complete Orthogonal System**

For the Sturm-Liouville problem with boundary conditions, we get:
- Eigenvalues: $0 < \lambda_1 < \lambda_2 < \lambda_3 < \cdots$
- Eigenfunctions: $X_n(x)$ satisfying $\mathcal{L}X_n = \lambda_n X_n$
- **Orthogonality**: $\langle X_m, X_n \rangle = 0$ for $m \neq n$

### **General Solution**

$$\boxed{V(x,\tau) = \sum_{n=1}^{\infty} c_n X_n(x)e^{-\lambda_n\tau}}$$

### **Determining Coefficients**

At $\tau = 0$ (terminal condition):
$$V(x,0) = \Phi(e^x) = \sum_{n=1}^{\infty} c_n X_n(x)$$

By orthogonality:
$$\boxed{c_n = \frac{\langle \Phi(e^x), X_n(x) \rangle}{\langle X_n, X_n \rangle} = \frac{\int_{x_B}^{x_{\max}} \Phi(e^x)X_n(x)w(x)dx}{\int_{x_B}^{x_{\max}} X_n^2(x)w(x)dx}}$$

### **Example: Symmetric Case**

For $x \in [-L, L]$ with symmetric boundary conditions, eigenfunctions might be:
$$X_n(x) \propto \sin\left(\frac{n\pi(x+L)}{2L}\right) \cdot \text{(weight factor)}$$

or more complex depending on drift and boundary conditions.

---

## **8. Explicit Example: Simplified Case**

### **No Drift, No Discount**

Consider the simplified equation (for illustration):
$$\frac{\partial V}{\partial \tau} = \frac{\sigma^2}{2}\frac{\partial^2 V}{\partial x^2}$$

on $x \in [0, L]$ with $V(0,\tau) = V(L,\tau) = 0$.

### **Separation**

$$V(x,\tau) = X(x)T(\tau)$$

gives:
$$\frac{T'}{\frac{\sigma^2}{2}T} = \frac{X''}{X} = -\lambda$$

### **Spatial Problem**

$$X'' + \lambda X = 0, \quad X(0) = X(L) = 0$$

Eigenvalues:
$$\boxed{\lambda_n = \left(\frac{n\pi}{L}\right)^2, \quad n = 1,2,3,\ldots}$$

Eigenfunctions:
$$\boxed{X_n(x) = \sin\left(\frac{n\pi x}{L}\right)}$$

### **Temporal Solution**

$$T_n(\tau) = e^{-\frac{\sigma^2}{2}\lambda_n\tau} = e^{-\frac{\sigma^2}{2}\left(\frac{n\pi}{L}\right)^2\tau}$$

### **General Solution**

$$\boxed{V(x,\tau) = \sum_{n=1}^{\infty} c_n \sin\left(\frac{n\pi x}{L}\right)e^{-\frac{\sigma^2}{2}\left(\frac{n\pi}{L}\right)^2\tau}}$$

with:
$$c_n = \frac{2}{L}\int_0^L \Phi(e^x)\sin\left(\frac{n\pi x}{L}\right)dx$$

---

## **9. Connection to Fourier Transform**

### **Limit as Domain → ∞**

As $L \to \infty$, the discrete spectrum becomes continuous:
$$\lambda_n = \left(\frac{n\pi}{L}\right)^2 \to \omega^2 \quad (\text{continuous } \omega)$$

The sum becomes an integral:
$$\sum_{n=1}^{\infty} \to \int_{-\infty}^{\infty} d\omega$$

The eigenfunctions become:
$$\sin\left(\frac{n\pi x}{L}\right) \to e^{i\omega x} \quad \text{(complex exponentials)}$$

### **Fourier Transform Representation**

$$\boxed{V(x,\tau) = \frac{1}{2\pi}\int_{-\infty}^{\infty}\hat{V}(\omega,0)e^{-\frac{\sigma^2\omega^2\tau}{2}}e^{i\omega x}d\omega}$$

This is exactly the **Fourier transform solution** we discussed earlier!

### **Philosophical Point**

Separation of variables on **finite domains** → Fourier series (discrete)
Separation of variables on **infinite domains** → Fourier transform (continuous)

---

## **10. Why Separation of Variables is Less Used**

### **Limitations**

1. **Infinite domain**: Requires moving to continuous spectrum → Fourier transforms
2. **Non-constant coefficients**: If $\sigma = \sigma(S,t)$, separation fails
3. **Path-dependent options**: Asian, lookback → need more state variables
4. **Boundary complexity**: Non-homogeneous or time-dependent boundaries complicate analysis

### **When It Works Well**

1. **Bounded domains**: Options with barriers on both sides
2. **Simple geometries**: Rectangular domains in multi-dimensional problems
3. **Homogeneous boundary conditions**: Zero at boundaries
4. **Pedagogical purposes**: Teaching the structure of solutions

### **Alternative Methods**

For most practical problems:
- **Fourier/Laplace transforms**: Handle infinite domains naturally
- **Green's functions**: Direct integral representation
- **Feynman-Kac**: Probabilistic approach
- **Numerical methods**: Finite differences, finite elements

---

## **11. Multi-Dimensional Separation**

### **Two-Asset Option**

For $V(S_1, S_2, t)$ satisfying:
$$\frac{\partial V}{\partial t} + \mathcal{L}_1 V + \mathcal{L}_2 V + \rho\sigma_1\sigma_2 S_1 S_2\frac{\partial^2 V}{\partial S_1 \partial S_2} - rV = 0$$

### **Separation Ansatz**

Try:
$$V(S_1, S_2, t) = V_1(S_1)V_2(S_2)T(t)$$

The **mixed derivative term** $\frac{\partial^2 V}{\partial S_1 \partial S_2}$ prevents simple separation unless $\rho = 0$ (uncorrelated assets).

### **Uncorrelated Case ($\rho = 0$)**

With $\rho = 0$:
$$\frac{T'}{T} + \frac{\mathcal{L}_1 V_1}{V_1} + \frac{\mathcal{L}_2 V_2}{V_2} - r = 0$$

Can separate:
$$\frac{\mathcal{L}_1 V_1}{V_1} = -\lambda_1, \quad \frac{\mathcal{L}_2 V_2}{V_2} = -\lambda_2, \quad \frac{T'}{T} = -(\lambda_1 + \lambda_2 - r)$$

This gives:
$$\boxed{V(S_1,S_2,t) = \sum_{m,n}c_{mn}X_m(S_1)Y_n(S_2)e^{-(\lambda_m + \lambda_n - r)(T-t)}}$$

### **Correlated Case ($\rho \neq 0$)**

Need to **diagonalize** the covariance matrix first via rotation/principal components, then separate in the new coordinates.

---

## **12. Time-Dependent Separation**

### **Modified Ansatz**

For time-dependent coefficients $r(t), \sigma(t)$, standard separation $V = X(S)T(t)$ fails.

Try **generalized separation**:
$$V(S,t) = \sum_{n=0}^{\infty}T_n(t)X_n(S)$$

where $X_n$ are **fixed eigenfunctions** but $T_n(t)$ satisfy **coupled ODEs**.

### **WKB Approximation**

For slowly varying coefficients, use **WKB (Wentzel-Kramers-Brillouin) method**:
$$V(S,t) \sim e^{i\theta(S,t)/\epsilon}A(S,t)$$

where $\theta$ satisfies the **eikonal equation** and $A$ satisfies a transport equation.

This is beyond standard separation but related in spirit.

---

## **13. Relationship to Spectral Methods**

### **Spectral Expansion**

The separation of variables solution:
$$V(x,\tau) = \sum_{n=1}^{\infty}c_n X_n(x)e^{-\lambda_n\tau}$$

is a **spectral expansion** in the eigenfunctions of the spatial operator.

### **Numerical Spectral Methods**

**Galerkin Method**:
1. Choose basis functions $\{\phi_n\}$ (eigenfunctions or other complete set)
2. Approximate: $V_N(x,\tau) = \sum_{n=1}^N c_n(\tau)\phi_n(x)$
3. Project PDE onto finite-dimensional space
4. Solve system of ODEs for $c_n(\tau)$

**Advantage**: Exponential convergence for smooth solutions

**Disadvantage**: Requires smooth payoffs; boundary treatment is delicate

### **Chebyshev/Legendre Polynomials**

For bounded domains $[a,b]$, use:
- **Chebyshev polynomials** $T_n(x)$ on $[-1,1]$
- **Legendre polynomials** $P_n(x)$ on $[-1,1]$
- Transform domain via $x = \frac{2S - (a+b)}{b-a}$

Excellent for **smooth problems** with **spectral accuracy** ($O(e^{-cN})$ error).

---

## **14. Similarity Solutions**

### **Self-Similar Ansatz**

For scale-invariant problems, try:
$$V(S,t) = S^\alpha f(\xi), \quad \xi = \frac{\ln(S/K)}{\sigma\sqrt{T-t}}$$

This reduces the PDE to an **ODE** in $\xi$.

### **Connection to Separation**

Similarity solutions are a **special case** of separation where the separation constant is chosen to match the scale invariance.

### **Heat Equation Example**

For $u_t = u_{xx}$:
$$u(x,t) = t^{-1/2}f\left(\frac{x}{\sqrt{t}}\right)$$

reduces to:
$$f'' + \frac{\xi}{2}f' + \frac{1}{2}f = 0$$

Solution: $f(\xi) = e^{-\xi^2/4}$ (Gaussian!)

### **Black-Scholes Similarity**

The Black-Scholes formula has the similarity structure:
$$C(S,K,T,r,\sigma) = S \cdot \Pi_1(d_1) - Ke^{-rT}\Pi_2(d_2)$$

where $d_1, d_2$ depend only on:
$$\frac{\ln(S/K)}{\sigma\sqrt{T}}, \quad r\sqrt{T}, \quad \sigma\sqrt{T}$$

These are **dimensionless combinations** (similarity variables).

---

## **15. Operator Theory Perspective**

### **The Black-Scholes Operator**

Define:
$$\boxed{\mathcal{L} = \frac{\sigma^2}{2}\frac{\partial^2}{\partial x^2} + \left(r-\frac{\sigma^2}{2}\right)\frac{\partial}{\partial x} - r}$$

The PDE is:
$$\frac{\partial V}{\partial \tau} = \mathcal{L}V$$

### **Spectral Decomposition**

The operator $\mathcal{L}$ has:
- **Spectrum**: $\sigma(\mathcal{L})$ (set of eigenvalues)
- **Eigenfunctions**: $\mathcal{L}\phi_\lambda = \lambda\phi_\lambda$
- **Semigroup**: $e^{\tau\mathcal{L}}$ is the solution operator

### **Functional Calculus**

The solution is:
$$\boxed{V(\cdot, \tau) = e^{\tau\mathcal{L}}V(\cdot, 0)}$$

For discrete spectrum:
$$e^{\tau\mathcal{L}} = \sum_{n=1}^{\infty}e^{\tau\lambda_n}P_n$$

where $P_n$ projects onto the $n$-th eigenspace.

For continuous spectrum:
$$e^{\tau\mathcal{L}} = \int_{\sigma(\mathcal{L})}e^{\tau\lambda}dE(\lambda)$$

where $E(\lambda)$ is the **spectral measure** (Fourier transform).

---

## **16. Practical Example: Box Spread**

### **Setup**

Consider a bounded domain $S \in [S_L, S_U]$ (box spread: long call spread + short put spread).

**Boundary conditions**:
- $V(S_L, t) = A$ (constant)
- $V(S_U, t) = B$ (constant)

### **Modified Problem**

Define $W(S,t) = V(S,t) - A - \frac{B-A}{S_U - S_L}(S - S_L)$ so:
- $W(S_L,t) = 0$
- $W(S_U,t) = 0$

Now $W$ satisfies a **homogeneous** boundary value problem.

### **Eigenfunction Expansion**

$$W(S,t) = \sum_{n=1}^{\infty}c_n(t)\phi_n(S)$$

where $\phi_n$ are eigenfunctions of:
$$\mathcal{L}\phi_n = \lambda_n\phi_n$$

with $\phi_n(S_L) = \phi_n(S_U) = 0$.

### **Time Evolution**

$$c_n(t) = c_n(T)e^{-\lambda_n(T-t)}$$

where $c_n(T)$ comes from projecting the payoff:
$$c_n(T) = \frac{\int_{S_L}^{S_U}[\Phi(S) - A - \frac{B-A}{S_U-S_L}(S-S_L)]\phi_n(S)w(S)dS}{\int_{S_L}^{S_U}\phi_n^2(S)w(S)dS}$$

---

## **17. Computational Aspects**

### **Computing Eigenvalues**

For the Sturm-Liouville problem:
$$-\frac{\sigma^2}{2}X'' - (r-\frac{\sigma^2}{2})X' + rX = \lambda X$$

with boundary conditions, use:

**Shooting method**:
1. Guess $\lambda$
2. Integrate ODE from $x_L$ to $x_R$
3. Check if boundary condition at $x_R$ is satisfied
4. Iterate to find $\lambda$ where it is

**Finite differences**:
1. Discretize: $X_j \approx X(x_j)$
2. Matrix eigenvalue problem: $\mathbf{A}\mathbf{X} = \lambda\mathbf{X}$
3. Use standard eigenvalue solvers (QR algorithm, etc.)

### **Computing Coefficients**

The projection:
$$c_n = \frac{\langle \Phi, \phi_n \rangle}{\langle \phi_n, \phi_n \rangle}$$

requires **numerical integration** (Gaussian quadrature).

### **Series Truncation**

In practice, truncate:
$$V(x,\tau) \approx \sum_{n=1}^{N}c_n\phi_n(x)e^{-\lambda_n\tau}$$

**Error estimate**:
$$\left|V - V_N\right| \leq \sum_{n=N+1}^{\infty}|c_n|e^{-\lambda_n\tau} \leq Ce^{-\lambda_{N+1}\tau}$$

The exponential decay in $\tau$ means **rapid convergence** away from $\tau = 0$.

---

## **18. Barrier Options via Separation**

### **Down-and-Out Call**

Domain: $S \in [B, \infty)$ with $V(B,t) = 0$.

**Problem**: Semi-infinite domain, but with one boundary condition.

### **Truncation**

Approximate by $S \in [B, S_{\max}]$ for large $S_{\max}$, with:
- $V(B,t) = 0$ (knock-out)
- $V(S_{\max}, t) = S_{\max} - K$ (deep ITM)

Now standard separation applies.

### **Comparison with Method of Images**

The **method of images** gives:
$$V(S,t) = C_{\text{BS}}(S,t) - \left(\frac{B}{S}\right)^{2r/\sigma^2}C_{\text{BS}}\left(\frac{B^2}{S}, t\right)$$

This is **exact** and more elegant than truncated eigenfunction expansion.

**Lesson**: For problems with analytical solutions via other methods, separation of variables is often less efficient.

---

## **19. Advanced Topics**

### **Non-Self-Adjoint Operators**

If the operator is not self-adjoint, we need:
- **Bi-orthogonal systems**: left and right eigenfunctions
- **Generalized eigenfunctions**: in the sense of distributions
- **Resolvent theory**: $(L - \lambda I)^{-1}$ analysis

### **Degenerate Operators**

Near $S = 0$, the Black-Scholes operator degenerates ($\sigma^2 S^2 \to 0$).

This changes the **type** of the equation (parabolic → first-order) and affects:
- Boundary conditions needed
- Regularity of eigenfunctions
- Completeness of the eigenfunction system

### **Fractional Laplacian**

For **Lévy processes** (jumps), the spatial operator is:
$$\mathcal{L} = \int_{\mathbb{R}}[f(x+y) - f(x) - yf'(x)\mathbb{1}_{|y|<1}]\nu(dy)$$

This is **non-local** (integral operator), so standard separation of variables doesn't directly apply.

Eigenfunctions exist but are more exotic (related to special functions).

---

## **20. Summary: When to Use Separation of Variables**

### **Advantages**

| **Situation** | **Why It Works** |
|---------------|------------------|
| Bounded domains | Discrete spectrum, Fourier series |
| Homogeneous BCs | Simplifies eigenvalue problem |
| Pedagogical | Reveals structure of solution |
| Theoretical | Connects to spectral theory |

### **Disadvantages**

| **Situation** | **Why It Fails/Struggles** |
|---------------|----------------------------|
| Infinite domains | Continuous spectrum → Fourier transform better |
| Non-separable operators | Mixed derivatives with $\rho \neq 0$ |
| Time-dependent coefficients | Standard separation doesn't work |
| Complex boundaries | Non-homogeneous or time-dependent BCs |
| Path-dependent options | Need more state variables |

### **The Verdict**

For **Black-Scholes** specifically:
- **Infinite domain** ($S \in (0,\infty)$) makes discrete separation impractical
- **Fourier/Laplace transforms** are the natural extension
- **Green's function** method is more direct
- **Feynman-Kac** is most elegant probabilistically

For **bounded domains** (barriers):
- Separation works but **method of images** is often simpler
- **Numerical methods** (FD, FEM) are more flexible

### **Historical Role**

Separation of variables was crucial **historically**:
1. **19th century**: Fourier, Sturm-Liouville theory
2. **Early 20th century**: Heat/wave equations in physics
3. **Modern era**: Absorbed into spectral theory, functional analysis

For **modern quantitative finance**:
- Transform methods (Fourier, Laplace, Mellin)
- Probabilistic methods (Feynman-Kac, martingales)
- Numerical PDE solvers

dominate practical applications.

---

## **21. The Deep Structure**

### **Unified View**

All these methods are **related**:

$$\begin{align}
&\text{Separation (finite)} \longleftrightarrow \text{Fourier series} \\
&\quad\downarrow \text{(limit } L \to \infty) \\
&\text{Separation (infinite)} \longleftrightarrow \text{Fourier transform} \\
&\quad\downarrow \text{(Green's function)} \\
&\text{Fundamental solution} \longleftrightarrow \text{Heat kernel} \\
&\quad\downarrow \text{(probabilistic)} \\
&\text{Transition density} \longleftrightarrow \text{Feynman-Kac}
\end{align}$$

They're all **different manifestations** of the spectral decomposition of the heat operator.

### **The Fundamental Insight**

$$\boxed{e^{\tau\mathcal{L}}V_0 = \begin{cases}
\sum_{n}e^{\tau\lambda_n}\langle V_0, \phi_n\rangle\phi_n & \text{(discrete)} \\
\int e^{\tau\lambda}\langle V_0, \phi_\lambda\rangle\phi_\lambda d\lambda & \text{(continuous)} \\
\int G(x,y,\tau)V_0(y)dy & \text{(Green's function)} \\
\mathbb{E}[V_0(X_\tau)] & \text{(probabilistic)}
\end{cases}}$$

These are **four representations** of the **same solution operator**!

### **Choosing the Right Tool**

- **Discrete spectrum** (barriers) → Separation/Fourier series
- **Continuous spectrum** (no barriers) → Fourier transform
- **Non-smooth payoffs** → Green's function
- **Exotic options** → Feynman-Kac/Monte Carlo
- **American options** → Free boundary/viscosity solutions

The art is knowing which representation to use for each problem.

---

Would you like me to explore:
- Detailed eigenvalue computation for specific barrier configurations
- Multi-dimensional separation with correlation
- Connection to spherical harmonics for multi-asset options
- WKB methods for time-dependent coefficients
- Spectral methods for numerical solution
- The relationship between separation and method of images in detail?