# Chapter 5: Partial Differential Equations in Finance

This chapter develops the PDE theory underlying derivative pricing. The central theme is that expected values of diffusion processes satisfy partial differential equations—the infinitesimal generator serves as the bridge. Starting from the classification of second-order PDEs and the heat equation, we study Green's functions and transition densities, derive the Kolmogorov forward and backward equations, and culminate in the Feynman-Kac formula that connects risk-neutral expectations to pricing PDEs.

## Key Concepts

**The SDE-PDE Bridge**
For a diffusion $X_t$ and a function $g$, the conditional expectation $u(t,x) = \mathbb{E}[g(X_T) \mid X_t = x]$ is a deterministic function of the starting point that satisfies a PDE involving the generator $\mathcal{L}$. This correspondence—random processes yield deterministic equations for their expected behavior—is the organizing principle of the chapter. PDEs arise naturally in finance because option prices, as risk-neutral expectations, inherit this structure. Second-order linear PDEs are classified by the sign of the discriminant $B^2 - AC$ into elliptic, parabolic, and hyperbolic types; pricing PDEs in finance are **parabolic**, reflecting the irreversibility of time and the diffusive nature of asset dynamics. Boundary value problems (Dirichlet, Neumann, Robin) encode the specific features of financial contracts—payoffs, barriers, and exercise boundaries.

**The Heat Equation**
The heat equation $u_t = \frac{1}{2} u_{xx}$ is the prototype of all parabolic PDEs. Its **fundamental solution** (heat kernel) is the Gaussian density
$$G(t,x) = \frac{1}{\sqrt{2\pi t}} \exp\!\left(-\frac{x^2}{2t}\right)$$
which is simultaneously the transition density of standard Brownian motion. Solutions are obtained by convolution: $u(t,x) = \int G(t, x-y)\, f(y)\, dy = \mathbb{E}[f(x + B_t)]$. The **parabolic scaling** symmetry $u(\lambda^2 t, \lambda x)$ preserves solutions, reflecting the $\sqrt{t}$ scaling of Brownian motion. The **maximum principle** states that subsolutions attain their maximum on the parabolic boundary—this is the key tool for uniqueness and comparison. Energy methods provide an alternative approach to uniqueness via the monotonicity of $\int u^2\, dx$.

**Green's Functions and Transition Densities**
The Green's function $G(x,t; y,s)$ for a parabolic PDE is the response to a point source: the solution with initial condition $\delta(x - y)$ at time $s$. For diffusion processes, the **transition density** $p(x,t \mid x_0, t_0)$ is precisely the Green's function of the associated Kolmogorov equation. On bounded domains, the Green's function is constructed via **spectral decomposition**—expanding in eigenfunctions of the spatial operator. The distinction between free-space and bounded domains is critical: free-space problems use the heat kernel directly, while bounded domains require eigenfunction series and must account for boundary conditions (absorption at barriers, reflection, etc.).

**Kolmogorov Equations**
The Kolmogorov equations describe two dual perspectives on a diffusion $dX_t = \mu(X_t)\, dt + \sigma(X_t)\, dW_t$:

- *Backward equation*: $\frac{\partial u}{\partial t} + \mathcal{L}u = 0$ where $\mathcal{L} = \mu\, \partial_x + \frac{1}{2}\sigma^2\, \partial_{xx}$ acts on the initial point. The function $u(t,x) = \mathbb{E}_x[g(X_T)]$ satisfies this equation—it tracks how expected payoffs depend on the starting position.
- *Forward equation* (Fokker-Planck): $\frac{\partial p}{\partial t} = -\frac{\partial}{\partial x}[\mu\, p] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2\, p]$ acts on the current state. It describes the evolution of the probability density—tracking where probability mass flows over time.

The two equations are **adjoint**: the forward operator $\mathcal{L}^*$ is the formal adjoint of the backward operator $\mathcal{L}$, reflecting the duality between "where did it come from?" and "where is it going?" For canonical financial models, the Fokker-Planck equation yields known transition densities: log-normal for GBM, non-central chi-square for CIR, and Gaussian for Ornstein-Uhlenbeck.

**The Feynman-Kac Formula**
The Feynman-Kac formula provides a probabilistic representation for solutions of parabolic PDEs with discounting:
$$u(t,x) = \mathbb{E}\!\left[\exp\!\left(-\int_t^T r(X_s)\, ds\right) g(X_T) \;\middle|\; X_t = x\right]$$
solves the PDE $u_t + \mathcal{L}u - r\, u = 0$ with terminal condition $u(T,x) = g(x)$. The proof applies Ito's lemma to the discounted process, identifies the martingale part, and uses the martingale property to equate the expectation. The **running payoff extension** adds a source term:
$$u(t,x) = \mathbb{E}\!\left[\exp\!\left(-\int_t^T r\, ds\right) g(X_T) + \int_t^T \exp\!\left(-\int_t^s r\, d\tau\right) f(X_s)\, ds \;\middle|\; X_t = x\right]$$
solving $u_t + \mathcal{L}u - r\, u + f = 0$. In finance, the Feynman-Kac formula is the mathematical justification for risk-neutral pricing: the Black-Scholes PDE with terminal condition $\Phi(S_T)$ has solution equal to the discounted $\mathbb{Q}$-expectation of the payoff. This duality enables a choice between Monte Carlo simulation (SDE paths) and finite-difference methods (PDE grid) for numerical computation.

!!! note "Role in the Book"
    The PDE framework developed here is applied directly in Chapter 6, where the Black-Scholes PDE is derived and solved via heat equation reduction and the Feynman-Kac representation. The Kolmogorov equations reappear in calibration (Chapter 17) via the Dupire equation.

---
