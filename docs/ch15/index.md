# Chapter 15: Affine Processes


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

This chapter develops the theory of affine processes---Markov processes whose characteristic function is exponential-affine in the state variable---and their central role in mathematical finance. Starting from a review of Markov processes and the formal definition of affine processes with their log-affine expectation property and state space regularity, we derive the generalized Riccati ODE system that governs the characteristic function and establish existence and uniqueness of its solutions with explicit closed-form expressions for common cases. We then study the infinitesimal generator, construct exponential martingales, and prove the crucial closure property under measure change. The affine term structure framework for bond pricing is developed with exponential-affine bond price formulas, yield curve dynamics, and the Dai-Singleton classification. We extend to discounted transforms for option pricing via Fourier inversion with connections to the Feynman-Kac theorem. The multidimensional affine family is presented in canonical form with admissibility conditions and correlation structures, and key examples---geometric Brownian motion, Vasicek, CIR, Heston, and multi-factor affine models---are analyzed in detail. Finally, jump-diffusion extensions, boundary behavior via Feller classification, and the limitations of the affine framework are discussed.

## Key Concepts

### **Markov Processes Review and State Space**
Affine processes are built on the Markov property: given the current state $X_t$, the future evolution is independent of the past. The state space and regularity conditions ensure well-posedness of the process. For affine diffusions, the state space is typically $\mathbb{R}^m_+ \times \mathbb{R}^{d-m}$ with the first $m$ components non-negative (driving stochastic volatility and ensuring positivity of variance or interest rates) and the remaining $d-m$ components unconstrained. Regularity conditions on the drift, diffusion, and jump coefficients guarantee existence and uniqueness of solutions to the associated SDEs and ensure the process remains within its prescribed state space.

### **Definition of Affine Process and the Log-Affine Expectation Property**
An $\mathbb{R}^d$-valued Markov process $X_t$ is **affine** if its conditional characteristic function has the exponential-affine form

$$\mathbb{E}\!\left[e^{u^\top X_T} \mid X_t = x\right] = \exp\!\left(\phi(\tau, u) + \psi(\tau, u)^\top x\right)$$

for $\tau = T - t$, where $\phi : \mathbb{R}_+ \times \mathbb{C}^d \to \mathbb{C}$ and $\psi : \mathbb{R}_+ \times \mathbb{C}^d \to \mathbb{C}^d$ satisfy the initial conditions $\phi(0, u) = 0$ and $\psi(0, u) = u$. This log-affine structure means that the log-characteristic function is **linear in the current state** $x$---an extraordinary simplification that reduces option pricing from solving PDEs to solving ordinary differential equations. The defining feature of the affine class is that drift, diffusion matrix, and short rate are all **linear** (affine) in the state: $\bar{\mu}(X_t) = a_0 + a_1 X_t$, $\bar{\sigma}(X_t)\bar{\sigma}(X_t)^T = c_0 + c_1^T X_t$, and $r(X_t) = r_0 + r_1^T X_t$.

### **Characteristic Function and Generalized Riccati ODEs**
Substituting the exponential-affine ansatz into the backward Kolmogorov equation yields the **generalized Riccati system**:

$$\frac{d\psi}{d\tau} = R(\psi), \qquad \frac{d\phi}{d\tau} = F(\psi)$$

where $R$ and $F$ are determined by the drift, diffusion, and jump coefficients of $X_t$. For the general affine framework (Duffie-Pan-Singleton), the system takes the form $dA/d\tau = -r_0 + B^T a_0 + \frac{1}{2}B^T c_0 B$ and $dB/d\tau = -r_1 + a_1^T B + \frac{1}{2}B^T c_1 B$ with initial conditions $A(0,u) = 0$ and $B(0,u) = iu^T$. For a scalar affine diffusion $dX_t = (\kappa_0 + \kappa_1 X_t)\,dt + \sqrt{\sigma_0 + \sigma_1 X_t}\,dW_t$, the Riccati equation becomes $\psi' = \frac{1}{2}\sigma_1\psi^2 + \kappa_1\psi$ and $\phi' = \frac{1}{2}\sigma_0\psi^2 + \kappa_0\psi$.

### **Existence, Uniqueness, and Explicit Riccati Solutions**
**Existence and uniqueness** of solutions to the Riccati system follows from the regularity of $R$ and $F$ in the admissible parameter domain. Explicit closed-form solutions exist for important special cases: the CIR process yields $B(\tau) = 2(e^{\gamma\tau}-1)/((\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma)$ with $\gamma = \sqrt{\kappa^2+2\sigma^2}$ involving exponential functions, and the Vasicek process gives solutions that are quadratic in $\tau$. When closed-form solutions are unavailable---as in multi-factor or jump-diffusion affine models---the Riccati ODEs are solved numerically, typically with Runge-Kutta methods, requiring care with branch cuts and complex-plane continuity.

### **Infinitesimal Generator and Exponential Martingales**
The infinitesimal generator of an affine process has the form $\mathcal{A}f(x) = (b_0 + b_1 x)f'(x) + \frac{1}{2}(a_0 + a_1 x)f''(x) + \int [f(x+z) - f(x) - zf'(x)]\,m(x, dz)$ where the drift $b_0 + b_1 x$, diffusion $a_0 + a_1 x$, and jump measure $m(x, dz)$ are all affine in $x$. **Exponential martingales** $M_t = \exp(\phi(T-t, u) + \psi(T-t, u)^\top X_t)$ are constructed directly from the Riccati solutions and serve as Radon-Nikodym derivatives for measure changes.

### **Measure Change and Closure Property**
The crucial **closure property**: measure changes via exponential-affine Radon-Nikodym derivatives preserve the affine class, modifying only the parameters $(b_0, b_1, a_0, a_1, m)$. This means the risk-neutral measure $\mathbb{Q}$ of an affine model is itself affine, with different drift and jump parameters but the same structural form---enabling consistent pricing and calibration across measures. The Girsanov transformation changes drifts while leaving diffusion coefficients unchanged, and for affine processes this modification preserves the linearity of all coefficients in the state variable.

### **Affine Term Structure Models and Bond Pricing**
A short-rate model $r_t = \rho_0 + \rho_1^\top X_t$ with affine state dynamics yields the **exponential-affine bond price**:

$$P(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds} \mid X_t\right] = \exp\!\left(A(\tau) + B(\tau)^\top X_t\right)$$

where $A(\tau)$ and $B(\tau)$ satisfy the **extended Riccati system** with $B' = R(B) - \rho_1$ and $A' = F(B) - \rho_0$. This is the **affine term structure** (ATS) framework of Duffie and Kan (1996). The Vasicek model gives $B(\tau) = (1-e^{-\kappa\tau})/\kappa$ and yields are linear in $r_t$. The CIR model gives $B(\tau) = 2(e^{\gamma\tau}-1)/((\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma)$ with $\gamma = \sqrt{\kappa^2+2\sigma^2}$ and guarantees non-negative yields. **Yield curve dynamics** are fully determined by the affine state variables through the bond price formula, producing tractable expressions for spot rates, forward rates, and the entire yield curve as functions of the state $X_t$.

### **Classification of ATS Models**
The **Dai-Singleton classification** (2000) organizes multi-factor affine models by the number of state variables driving the volatility, denoted $A_m(d)$ for $m$ volatility factors among $d$ total. This taxonomy provides a systematic framework for understanding the trade-offs between model complexity, the ability to fit yield curve shapes, and the degree of stochastic volatility in interest rate dynamics.

### **Discounted Transform and Option Pricing**
For derivative pricing, we need the **discounted characteristic function**:

$$\mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds + u^\top X_T} \mid X_t = x\right] = \exp\!\left(\tilde{\phi}(\tau, u) + \tilde{\psi}(\tau, u)^\top x\right)$$

where $\tilde{\phi}$ and $\tilde{\psi}$ satisfy the extended Riccati system incorporating the discounting rate. This connects directly to the **Feynman-Kac** representation: if $U(X,t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[e^{iuX_T}|\mathcal{F}_t]$, then $U$ satisfies the associated PDE, and the affine ansatz $U = e^{A(\tau) + B(\tau)X}$ reduces the PDE to the Riccati system. For the Black-Scholes model, this yields explicitly $B = iu$ (constant) and $A = [-r + (r - \sigma^2/2)iu - \frac{1}{2}\sigma^2 u^2]\tau$. **Option pricing via Fourier inversion** expresses the European call price as $C = \frac{1}{\pi}\int_0^{\infty}\text{Re}[\cdots]\,du$ with the integrand built from the discounted transform. The **extended Riccati system with discounting** modifies the standard Riccati equations by incorporating the short-rate coefficients $r_0$ and $r_1$ into the ODEs for $A$ and $B$.

### **Multidimensional Affine Processes**
The $d$-dimensional affine process $X_t \in \mathbb{R}^d$ has drift $\mu(x) = b + Bx$, diffusion matrix $\Sigma(x) = a_0 + \sum_{i=1}^d a_i x_i$, and jump compensator $m(x, dz) = m_0(dz) + \sum_i x_i m_i(dz)$, all affine in $x$. The **vector state affine process** framework extends the scalar theory to multiple interacting factors. The **canonical representation** (Duffie, Filipovic, Schachermayer, 2003) identifies the state space as $\mathbb{R}^m_+ \times \mathbb{R}^{d-m}$ with the first $m$ components non-negative (driving stochastic volatility) and the remaining $d-m$ components unconstrained. **Admissibility conditions** ensure the process remains in its state space: the diffusion must vanish at the boundary of $\mathbb{R}^m_+$ and the drift must point inward, generalizing the Feller condition to the multidimensional setting. The **correlation structure** between components is encoded in the off-diagonal elements of $B$ and the cross-terms in $\Sigma$, constrained by admissibility.

### **Key Examples**
**Geometric Brownian motion** illustrates a fundamental subtlety: the stock price $S_t$ itself is **not** affine (the diffusion $\sigma^2 S_t^2$ is quadratic), but the log stock price $X_t = \log S_t$ is affine with constant drift $a_0 = r - \sigma^2/2$, constant diffusion $c_0 = \sigma^2$, and $a_1 = c_1 = 0$, yielding the trivial Riccati solution $B(\tau) = iu$ and $A(\tau) = [-r + (r-\sigma^2/2)iu + \frac{1}{2}\sigma^2(iu)^2]\tau$. The **Vasicek and CIR models** are the canonical one-factor affine short-rate models: Vasicek with Gaussian dynamics ($c_1 = 0$) and CIR with square-root diffusion ($c_1 \neq 0$), both yielding explicit Riccati solutions for bond prices. The **Heston model** is a two-dimensional affine process in $(\log S_t, V_t)$, whose affine structure is the foundation of semi-closed-form option pricing via characteristic functions and Fourier methods. **Multi-factor affine models** combine multiple state variables to capture richer dynamics---for example, two-factor CIR+Vasicek models for interest rates with stochastic long-rate factors.

### **Jump-Diffusion Extensions and Boundary Behavior**
Adding jumps to affine processes preserves the exponential-affine structure provided the jump compensator is itself affine. The Bates model (Heston + Merton jumps in the stock) and the double-exponential jump-diffusion (Kou) are affine, with jump contributions adding $\lambda(\mathbb{E}[e^{uJ}] - 1)$ terms to the Riccati equations. **Boundary behavior** is governed by the **Feller classification**: for CIR-type components, the boundary $V = 0$ is unattainable when $2\kappa\theta \geq \xi^2$ (Feller satisfied) and attainable with instant reflection when violated, with implications for both mathematical well-posedness and numerical simulation.

### **Limits of the Affine Framework**
The affine framework breaks down when: volatility depends non-linearly on the state (e.g., $\sigma(S) = S^{\beta}$ with $\beta \neq 0, 1/2, 1$), when mean reversion targets are stochastic but non-affine, or when path-dependent features (lookbacks, barriers) are present. **Rough volatility** models with fractional kernels $v_t = \int_0^t K(t-s)\,dW_s$ break the Markov and semi-group properties that affine theory requires, demanding entirely different analytical tools. These limitations motivate the development of non-affine models, local-stochastic volatility hybrids, and numerical methods that do not rely on characteristic function tractability.

!!! note "Role in the Book"
    Affine processes provide the unifying mathematical framework connecting interest rate models (Vasicek, CIR in Chapter 18), the Heston stochastic volatility model (Chapter 16), and Fourier pricing methods (Chapter 9). The Riccati ODE system is the computational engine behind characteristic function pricing, and the closure under measure change ensures consistent calibration (Chapter 17). The bond pricing formula underpins the affine term structure theory developed in Chapter 18. The Duffie-Pan-Singleton framework and the Dai-Singleton classification organize the full taxonomy of affine models used throughout quantitative finance. The GBM example demonstrates how simple transformations render familiar models affine, while the Heston example shows how the affine structure enables the semi-closed-form pricing that makes stochastic volatility models practical.

---
