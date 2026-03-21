# Chapter 8: Numerical Solutions of the Black-Scholes PDE

This chapter develops finite difference methods (FDM) for solving the Black-Scholes PDE numerically, covering the complete pipeline from grid discretization and scheme construction through stability analysis, convergence theory, and practical implementation. Starting from the parabolic structure of the pricing PDE, we implement explicit, implicit, and Crank-Nicolson schemes in both original and log-price coordinates, analyze their stability via von Neumann analysis and the CFL condition, establish grid convergence and Richardson extrapolation for error improvement, extract Greeks directly from the solution grid, extend to American options through free boundary formulations with projection, PSOR, and penalty methods, and establish the rigorous convergence framework of viscosity solutions and the Barles-Souganidis theorem.

## Key Concepts

### **Finite Difference Discretization**
The Black-Scholes PDE 

$$\partial_t V + \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S - rV = 0$$ 

is solved on a rectangular grid $(S_j, t_n) = (j\Delta S, n\Delta t)$ for $j = 0,\ldots,M$ and $n = 0,\ldots,N$, with $\Delta S = S_{\max}/M$ and $\Delta t = T/N$. Using the time-to-maturity transformation $\tau = T - t$, the PDE becomes a forward problem 

$$\partial_\tau u = \frac{1}{2}\sigma^2 S^2 u_{SS} + rSu_S - ru$$ 

with initial condition $u(0,S) = \Phi(S)$. Derivatives are replaced by finite differences: the central difference 

$$V_S \approx \frac{V_{j+1}^n - V_{j-1}^n}{2\Delta S}$$

with $O((\Delta S)^2)$ accuracy, the second central difference 

$$V_{SS} \approx \frac{V_{j+1}^n - 2V_j^n + V_{j-1}^n}{(\Delta S)^2}$$ 

and the backward time difference 

$$V_t \approx \frac{V_j^{n+1} - V_j^n}{\Delta t}$$ 

The semi-discrete system yields tridiagonal coefficient matrices with entries $a_j = \frac{\Delta t}{2}(\sigma^2 j^2 - rj)$, $b_j = -({\Delta t})(\sigma^2 j^2 + r)$, $c_j = \frac{\Delta t}{2}(\sigma^2 j^2 + rj)$. The **log-price transformation** $x = \ln S$ produces constant diffusion coefficient $\sigma^2/2$, yielding a uniform grid in log-space with better resolution for small $S$ and removing spatial variation in coefficients. Boundary conditions for calls are $V(t,0) = 0$ and $V(t,S_{\max}) \approx S_{\max} - Ke^{-r(T-t)}$; for puts, $V(t,0) \approx Ke^{-r(T-t)}$ and $V(t,S_{\max}) \approx 0$. Neumann conditions ($V_S(t,S_{\max}) = 1$ for calls) provide alternatives. Grid sizing guidelines include $S_{\max} \approx 3K$ to $5K$, placing a grid point exactly at strike $K$, and applying payoff smoothing or Rannacher time-stepping to handle the kink in $(S-K)^+$.

### **Three Core Schemes**
The **explicit scheme** (forward Euler) evaluates spatial derivatives at the known time level: 

$$\mathbf{u}^{n+1} = (I + \Delta\tau A)\mathbf{u}^n$$

giving $u_j^{n+1} = a_j u_{j-1}^n + (1+b_j)u_j^n + c_j u_{j+1}^n$. This requires no linear solve ($O(M)$ per step) but is conditionally stable, requiring $\Delta t \leq (\Delta S)^2/(\sigma^2 S_{\max}^2)$---for typical parameters this demands thousands of time steps. The **implicit scheme** (backward Euler) evaluates at the unknown time level: 

$$(I - \Delta\tau A)\mathbf{u}^{n+1} = \mathbf{u}^n$$
 
producing a tridiagonal system solved by the Thomas algorithm in $O(M)$ operations. This is unconditionally stable but only first-order in time. The **Crank-Nicolson scheme** averages explicit and implicit: 

$$(I - \frac{\Delta\tau}{2}A)\mathbf{u}^{n+1} = (I + \frac{\Delta\tau}{2}A)\mathbf{u}^n$$

achieving $\mathcal{O}((\Delta t)^2 + (\Delta S)^2)$ accuracy while maintaining unconditional stability. The general **theta-scheme** 
$(I - \theta\Delta\tau A)\mathbf{u}^{n+1} = (I + (1-\theta)\Delta\tau A)\mathbf{u}^n$
unifies all three ($\theta = 0$: explicit, $\theta = 1/2$: Crank-Nicolson, $\theta = 1$: implicit). Crank-Nicolson can produce oscillations near non-smooth payoffs; **Rannacher time-stepping** uses two implicit steps initially then switches to Crank-Nicolson, damping high-frequency modes while preserving overall second-order accuracy. All three schemes are implemented in both original and log-price coordinates for European calls, European puts, American calls, and American puts, with comparison against the analytical Black-Scholes formula.

### **Stability, Consistency, and Convergence**
The **Lax equivalence theorem** states that for a consistent finite difference scheme applied to a well-posed linear problem, stability is equivalent to convergence: 

$$\text{consistency + stability}\quad \Longleftrightarrow\quad \text{convergence}$$

### **Consistency** requires the local truncation error to vanish as the mesh is refined; Crank-Nicolson has 

$$\text{LTE}= O((\Delta t)^2 + (\Delta S)^2)$$

### **Stability** requires bounded error growth: for all nΔ t ≤ T 

$$\|B^n\| \leq C$$ 

### **Von Neumann stability analysis** inserts a Fourier mode V_jⁿ = gⁿ eⁱkjΔ S and requires the amplification factor |g(ξ)| ≤ 1 for all frequencies. For the explicit scheme on the heat equation, g = 1 - 2λ(1-cos kΔ x) with λ = Δ t/(Δ x)², yielding the **CFL condition** λ ≤ 1/2. For the implicit scheme, g = 1/(1 + 2λ(1-cos kΔ x)) < 1 unconditionally. For Crank-Nicolson, g = (1-λ(1-cos kΔ x))/(1+λ(1-cos kΔ x)), also unconditionally stable. The CFL condition for Black-Scholes with variable coefficients is σ² S_max² Δ t/(2(Δ S)²) ≤ 1/2. **Monotone schemes** preserve the discrete maximum principle, implying L^∞ stability. Non-smooth payoffs reduce observed convergence order (from 2 to 0.5--1 for Crank-Nicolson near kinks), motivating Rannacher smoothing, payoff smoothing, grid adaptation, and Richardson extrapolation. **Grid convergence** is verified by refining Δ S and Δ t and plotting error on log-log scales; a ratio of ≈ 4 in successive errors confirms second-order convergence. **Richardson extrapolation** combines solutions at two grid spacings to cancel leading error terms, boosting accuracy by one order: V_ext = 2V(2M) - V(M).

### **Greeks via Finite Differences**
Greeks are extracted directly from the solution grid without requiring additional PDE solves (for spatial Greeks). **Delta** uses central differences: $\Delta \approx (V_{j+1}^0 - V_{j-1}^0)/(2\Delta S)$, with forward/backward differences at boundaries. **Gamma** uses the second central difference: $\Gamma \approx (V_{j+1}^0 - 2V_j^0 + V_{j-1}^0)/(\Delta S)^2$. High gamma near the strike indicates rapid delta changes. **Theta** is read from the time-stepping: $\Theta \approx -(V_j^{n+1} - V_j^n)/\Delta t$, using the final two time levels. **Vega** and **rho** require the **bumping approach**: solve the PDE twice with perturbed parameters $\sigma \pm \delta\sigma$ or $r \pm \delta r$ and take finite differences of the resulting prices. Grid placement relative to the strike critically affects accuracy---staggering the grid so $K$ falls on a node avoids interpolation error. The **theta-gamma relation** $\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma = rV$ serves as a consistency check. Accuracy and grid sensitivity analysis examines how Greek estimates depend on grid resolution, with finer grids improving estimates at higher computational cost.

### **American Options and Free Boundaries**
American option pricing requires enforcing the early exercise constraint $V \geq \Phi$ at every grid point and time step. The **variational inequality** $\min(-\partial_t V - \mathcal{L}V + rV,\; V - \Phi) = 0$ creates a free boundary $S^*(t)$ separating the continuation region (PDE holds) from the exercise region ($V = \Phi$). The **smooth pasting conditions** $V(t,S^*) = \Phi(S^*)$ and $V_S(t,S^*) = \Phi'(S^*)$ provide the extra equation to determine $S^*$. The early exercise premium $V_{\text{Am}} = V_{\text{Eu}} + \text{EEP} \geq 0$ quantifies the value of early exercise flexibility. The simplest numerical approach is **projection**: after each implicit/Crank-Nicolson time step, enforce $u_j^{n+1} \leftarrow \max(u_j^{n+1}, \Phi_j)$. This is easy to implement but may lose accuracy near the free boundary. The **linear complementarity problem** (LCP) formulation $L\mathbf{u} \geq \mathbf{f}$, $\mathbf{u} \geq \boldsymbol{\Phi}$, $(L\mathbf{u} - \mathbf{f})^T(\mathbf{u} - \boldsymbol{\Phi}) = 0$ provides the rigorous discrete framework. The **projected successive over-relaxation** (PSOR) algorithm iterates the SOR update $\tilde{u}_j^{(k+1)} = (1-\omega)u_j^{(k)} + \frac{\omega}{l_{jj}}(f_j - \sum_{i<j}l_{ji}u_i^{(k+1)} - \sum_{i>j}l_{ji}u_i^{(k)})$ followed by the projection $u_j^{(k+1)} = \max(\tilde{u}_j^{(k+1)}, \Phi_j)$, with $\omega \in (1,2)$ for over-relaxation (typically 5--20 iterations per time step). The **penalty method** adds $\rho\max(\Phi - V, 0)$ to the PDE, converting the free boundary to a nonlinear PDE on a fixed domain with error $O(1/\rho)$; combined with discretization error: $\|V_{h,\Delta t}^\rho - V\| \leq C_1 h^2 + C_2 \Delta t^p + C_3/\rho$, with $\rho = 10^6$--$10^8$ balancing accuracy and conditioning. The **Brennan-Schwartz algorithm** exploits the monotonicity of the exercise boundary for American puts, providing a direct non-iterative solve. **Front-fixing methods** transform coordinates to fix the boundary at a known location, achieving higher accuracy near $S^*$ at the cost of implementation complexity.

### **Viscosity Solutions and Convergence Theory**
When payoffs have kinks or the PDE degenerates (at $S = 0$), classical solutions may not exist. **Viscosity solutions** replace pointwise PDE satisfaction with inequalities tested against smooth test functions touching the solution from above (supersolution) or below (subsolution). The **comparison principle** guarantees uniqueness: if a viscosity subsolution lies below a supersolution at the boundary, the ordering holds everywhere. The **Barles-Souganidis theorem** provides the rigorous convergence framework: a finite difference scheme converges to the viscosity solution if and only if it is *monotone* (preserves the comparison principle discretely, tied to nonnegative stencil coefficients), *stable* (uniformly bounded), and *consistent* (recovers the PDE in the limit). This theorem justifies the use of upwind schemes and monotone discretizations for degenerate PDEs, and explains why naive high-order schemes can converge to wrong solutions when monotonicity is violated. For American options, the obstacle problem requires monotone discretizations and constraint enforcement (projection/LCP) to ensure convergence to the correct viscosity solution.

!!! note "Role in the Book"
    Finite difference methods provide the computational backbone for pricing problems throughout the book. The schemes developed here extend directly to local volatility PDEs (Chapter 13), two-dimensional ADI methods for Heston (Chapter 16), and tree-based implementations for Hull-White (Chapter 20). The viscosity solution framework connects to the PDE theory of Chapter 5 and provides rigorous foundations for American option pricing introduced in Chapter 7. Greeks estimation techniques underpin the hedging strategies discussed throughout the later chapters.

---
