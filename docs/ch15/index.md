# Chapter 15: Affine Processes

This chapter develops the theory of affine processes—Markov processes whose characteristic function is exponential-affine in the state variable—and their central role in mathematical finance. Starting from the definition and the log-affine expectation property, we derive the Riccati ODE system that governs the characteristic function, study the infinitesimal generator and measure changes within the affine class, build the affine term structure framework for bond pricing, extend to discounted transforms for option pricing, and classify the multidimensional affine family including its jump-diffusion extensions.

## Key Concepts

**Definition and the Exponential-Affine Property**
An $\mathbb{R}^d$-valued Markov process $X_t$ is **affine** if its conditional characteristic function has the exponential-affine form

$$\mathbb{E}\!\left[e^{u^\top X_T} \mid X_t = x\right] = \exp\!\left(\phi(\tau, u) + \psi(\tau, u)^\top x\right)$$

for $\tau = T - t$, where $\phi : \mathbb{R}_+ \times \mathbb{C}^d \to \mathbb{C}$ and $\psi : \mathbb{R}_+ \times \mathbb{C}^d \to \mathbb{C}^d$ satisfy the initial conditions $\phi(0, u) = 0$ and $\psi(0, u) = u$. This log-affine structure means that the log-characteristic function is linear in the current state $x$—an extraordinary simplification that reduces option pricing from solving PDEs to solving ordinary differential equations. The key examples—geometric Brownian motion, the Vasicek and CIR short-rate models, and the Heston stochastic volatility model—are all affine, explaining their analytical tractability.

**Riccati ODE System**
Substituting the exponential-affine ansatz into the backward Kolmogorov equation yields the **generalized Riccati system**:

$$\frac{d\psi}{d\tau} = R(\psi), \qquad \frac{d\phi}{d\tau} = F(\psi)$$

where $R$ and $F$ are determined by the drift, diffusion, and jump coefficients of $X_t$. For a scalar affine diffusion $dX_t = (\kappa_0 + \kappa_1 X_t)\,dt + \sqrt{\sigma_0 + \sigma_1 X_t}\,dW_t$, the Riccati equation becomes $\psi' = \frac{1}{2}\sigma_1\psi^2 + \kappa_1\psi$ and $\phi' = \frac{1}{2}\sigma_0\psi^2 + \kappa_0\psi$. **Existence and uniqueness** of solutions follows from the regularity of $R$ and $F$ in the admissible parameter domain. Explicit closed-form solutions exist for the CIR process (involving $\gamma = \sqrt{\kappa^2 + 2\sigma_1 u}$ and exponential functions) and the Vasicek process (quadratic in $\tau$). When closed-form solutions are unavailable—as in multi-factor or jump-diffusion affine models—the Riccati ODEs are solved numerically, typically with Runge-Kutta methods, requiring care with branch cuts and complex-plane continuity.

**Infinitesimal Generator and Measure Change**
The infinitesimal generator of an affine process has the form $\mathcal{A}f(x) = (b_0 + b_1 x)f'(x) + \frac{1}{2}(a_0 + a_1 x)f''(x) + \int [f(x+z) - f(x) - zf'(x)]\,m(x, dz)$ where the drift $b_0 + b_1 x$, diffusion $a_0 + a_1 x$, and jump measure $m(x, dz)$ are all affine in $x$. **Exponential martingales** $M_t = \exp(\phi(T-t, u) + \psi(T-t, u)^\top X_t)$ are constructed directly from the Riccati solutions and serve as Radon-Nikodym derivatives for measure changes. The crucial **closure property**: measure changes via exponential-affine Radon-Nikodym derivatives preserve the affine class, modifying only the parameters $(b_0, b_1, a_0, a_1, m)$. This means the risk-neutral measure $\mathbb{Q}$ of an affine model is itself affine, with different drift and jump parameters but the same structural form—enabling consistent pricing and calibration across measures.

**Affine Term Structure Models**
A short-rate model $r_t = \rho_0 + \rho_1^\top X_t$ with affine state dynamics yields the **exponential-affine bond price**:

$$P(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds} \mid X_t\right] = \exp\!\left(A(\tau) + B(\tau)^\top X_t\right)$$

where $A(\tau)$ and $B(\tau)$ satisfy the **extended Riccati system** with $B' = R(B) - \rho_1$ and $A' = F(B) - \rho_0$. This is the **affine term structure** (ATS) framework of Duffie and Kan (1996). The Vasicek model ($X_t = r_t$ with Gaussian dynamics) gives $B(\tau) = (1-e^{-\kappa\tau})/\kappa$ and yields are linear in $r_t$. The CIR model gives $B(\tau) = 2(e^{\gamma\tau}-1)/((\gamma+\kappa)(e^{\gamma\tau}-1)+2\gamma)$ with $\gamma = \sqrt{\kappa^2+2\sigma^2}$ and guarantees non-negative yields. The **classification** of ATS models (Dai-Singleton, 2000) organizes multi-factor affine models by the number of state variables driving the volatility, denoted $A_m(d)$ for $m$ volatility factors among $d$ total.

**Discounted Transform and Option Pricing**
For derivative pricing, we need the **discounted characteristic function**:

$$\mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_t^T r_s\,ds + u^\top X_T} \mid X_t = x\right] = \exp\!\left(\tilde{\phi}(\tau, u) + \tilde{\psi}(\tau, u)^\top x\right)$$

where $\tilde{\phi}$ and $\tilde{\psi}$ satisfy the extended Riccati system incorporating the discounting rate. This connects directly to the **Feynman-Kac** representation and enables option pricing via Fourier inversion: the European call price is $C = \frac{1}{\pi}\int_0^{\infty}\text{Re}[\cdots]\,du$ with the integrand built from the discounted transform. For the Heston model, the discounted transform gives the semi-closed-form option price that is the foundation of Fourier pricing (Chapter 9) and calibration (Chapter 17).

**Multidimensional Affine Processes**
The $d$-dimensional affine process $X_t \in \mathbb{R}^d$ has drift $\mu(x) = b + Bx$, diffusion matrix $\Sigma(x) = a_0 + \sum_{i=1}^d a_i x_i$, and jump compensator $m(x, dz) = m_0(dz) + \sum_i x_i m_i(dz)$, all affine in $x$. The **canonical representation** (Duffie, Filipovic, Schachermayer, 2003) identifies the state space as $\mathbb{R}^m_+ \times \mathbb{R}^{d-m}$ with the first $m$ components non-negative (driving stochastic volatility) and the remaining $d-m$ components unconstrained. **Admissibility conditions** ensure the process remains in its state space: the diffusion must vanish at the boundary of $\mathbb{R}^m_+$ and the drift must point inward, generalizing the Feller condition. The **correlation structure** between components is encoded in the off-diagonal elements of $B$ and the cross-terms in $\Sigma$, constrained by admissibility.

**Jump-Diffusion Extensions and Limitations**
Adding jumps to affine processes preserves the exponential-affine structure provided the jump compensator is itself affine. The Bates model (Heston + Merton jumps in the stock) and the double-exponential jump-diffusion (Kou) are affine, with jump contributions adding $\lambda(\mathbb{E}[e^{uJ}] - 1)$ terms to the Riccati equations. The affine framework breaks down when: volatility depends non-linearly on the state (e.g., $\sigma(S) = S^{\beta}$ with $\beta \neq 0, 1/2, 1$), when mean reversion targets are stochastic but non-affine, or when path-dependent features (lookbacks, barriers) are present. **Rough volatility** models with fractional kernels $v_t = \int_0^t K(t-s)\,dW_s$ break the Markov and semi-group properties that affine theory requires, demanding entirely different analytical tools.

!!! note "Role in the Book"
    Affine processes provide the unifying mathematical framework connecting interest rate models (Vasicek, CIR in Chapter 18), the Heston stochastic volatility model (Chapter 16), and Fourier pricing methods (Chapter 9). The Riccati ODE system is the computational engine behind characteristic function pricing, and the closure under measure change ensures consistent calibration (Chapter 17). The bond pricing formula underpins the affine term structure theory developed in Chapter 18.

---
