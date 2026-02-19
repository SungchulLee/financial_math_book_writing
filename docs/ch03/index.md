# Chapter 3: Stochastic Differential Equations

This chapter develops the theory of stochastic differential equations from empirical motivation through rigorous construction. Beginning with the statistical properties of real financial returns and the failure of deterministic models, we build the Ito integral, derive Ito's formula, define and solve SDEs for canonical financial models, establish existence and uniqueness theory, and study the structural properties of diffusion processes and their infinitesimal generators.

## Key Concepts

**Empirical Motivation**
Real stock returns exhibit **stylized facts** that deterministic models cannot capture: heavy tails (excess kurtosis), volatility clustering, the leverage effect (asymmetric volatility response), absence of return autocorrelation, and aggregational Gaussianity. The exponential growth ODE $dS/dt = \mu S$ produces smooth, deterministic paths with zero variance—fundamentally incompatible with observed data. Adding a noise term $\sigma S\, dW_t$ to the ODE bridges the gap from deterministic to stochastic models and motivates the SDE framework.

**Ito Integration**
Classical Riemann-Stieltjes integration fails for Brownian motion because its paths have unbounded variation. The Ito integral $\int_0^t H_s\, dW_s$ is constructed via $L^2$-approximation: first for simple (step-function) integrands, then extended by continuity using the **Ito isometry**

$$\mathbb{E}\!\left[\left(\int_0^t H_s\, dW_s\right)^{\!2}\right] = \mathbb{E}\!\left[\int_0^t H_s^2\, ds\right]$$

The resulting integral is a continuous martingale with zero expectation. The general **Ito process** $X_t = X_0 + \int_0^t b_s\, ds + \int_0^t \sigma_s\, dW_s$ decomposes into drift and martingale parts. The **Stratonovich integral** $\int_0^t H_s \circ dW_s$ uses midpoint evaluation, satisfies the classical chain rule, but loses the martingale property; the two conventions are related by $\int H_s \circ dW_s = \int H_s\, dW_s + \frac{1}{2}\langle H, W \rangle_t$.

**Ito's Formula**
Ito's formula is the stochastic chain rule. For $f \in C^{1,2}$ and an Ito process $X_t$:

$$df(t, X_t) = \frac{\partial f}{\partial t}\, dt + \frac{\partial f}{\partial x}\, dX_t + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}\, (dX_t)^2$$

The second-order term 

$$(dX_t)^2 = \sigma^2\, dt$$ 

arises from the non-zero quadratic variation of Brownian motion and is the hallmark of stochastic calculus. The derivation proceeds via Taylor expansion: the linear approximation leaves a non-vanishing residual of order $dt$, forcing retention of the quadratic term. Extensions include the **Ito product rule** $d(XY) = X\, dY + Y\, dX + d\langle X, Y \rangle$, the **quotient rule**, **integration by parts**, and the **multidimensional version** for vector-valued processes driven by $m$-dimensional Brownian motion.

**Stochastic Differential Equations**
An SDE 

$$dX_t = b(t, X_t)\, dt + \sigma(t, X_t)\, dW_t$$
 
defines a diffusion process through its drift $b$ and diffusion coefficient $\sigma$. Canonical examples include geometric Brownian motion 

$$dS = \mu S\, dt + \sigma S\, dW$$ 

solved by 

$$S_t = S_0 \exp((\mu - \sigma^2/2)t + \sigma W_t)$)$ 

the Ornstein-Uhlenbeck process (mean-reverting dynamics), and the square-root (CIR) process. Solving techniques include the **Ito-formula ansatz**, exponential transformations, and variation of constants. Verification of candidate solutions uses Ito's formula to confirm the SDE is satisfied. Moment analysis derives $\mathbb{E}[X_t]$ and $\text{Var}(X_t)$ without requiring closed-form solutions. Numerical simulation via Euler-Maruyama discretization $X_{i+1} = X_i + b\,\Delta t + \sigma\,\sqrt{\Delta t}\, Z_i$ enables Monte Carlo pricing when analytic solutions are unavailable.

**Existence and Uniqueness**
The fundamental theorem for SDEs guarantees a unique **strong solution** under the **Lipschitz condition** 

$$|b(t,x) - b(t,y)| + |\sigma(t,x) - \sigma(t,y)| \leq K|x-y|$$ 

and the **linear growth condition** 

$$|b(t,x)| + |\sigma(t,x)| \leq K(1 + |x|)$$ 

The constructive proof uses **Picard iteration**: successive approximations 

$$X^{(n+1)}_t = x + \int_0^t b(s, X^{(n)}_s)\, ds + \int_0^t \sigma(s, X^{(n)}_s)\, dW_s$$ 

converge in $L^2$. The distinction between **strong solutions** (adapted to the given Brownian motion) and **weak solutions** (where the probability space may be constructed as part of the solution) is essential: strong uniqueness implies weak uniqueness but not conversely.

**Diffusion Processes**
Solutions to SDEs are diffusion processes—continuous-path Markov processes completely characterized by drift and diffusion coefficients. The **strong Markov property** extends the memoryless property to stopping times: $\mathbb{E}[\varphi(X_{\tau+t}) \mid \mathcal{F}_\tau] = \mathbb{E}^{X_\tau}[\varphi(X_t)]$. The **Stroock-Varadhan martingale problem** provides an alternative characterization: a diffusion is defined by requiring $f(X_t) - \int_0^t \mathcal{L}f(X_s)\, ds$ to be a local martingale for all test functions $f$. **Invariant measures** $\pi$ satisfying $\int P_t f\, d\pi = \int f\, d\pi$ describe long-run stationary behavior. **Time reversal** reveals how the reversed process $\widetilde{X}_t = X_{T-t}$ satisfies an SDE with modified drift. **Large deviations** (Freidlin-Wentzell theory) quantify how the small-noise diffusion $dX^\varepsilon = b\, dt + \sqrt{\varepsilon}\,\sigma\, dW$ concentrates near the deterministic ODE solution as $\varepsilon \to 0$.

**Infinitesimal Generators**
The generator $\mathcal{L}f(x) = b^i(x)\, \partial_i f + \frac{1}{2} a^{ij}(x)\, \partial_{ij} f$ (where $a = \sigma\sigma^\top$) captures the instantaneous rate of change of conditional expectations. **Dynkin's formula** $\mathbb{E}_x[f(X_\tau)] = f(x) + \mathbb{E}_x[\int_0^\tau \mathcal{L}f(X_s)\, ds]$ is the stochastic fundamental theorem of calculus, connecting expected values at stopping times to the generator. The **Dynkin martingale** $M_t = f(X_t) - f(X_0) - \int_0^t \mathcal{L}f(X_s)\, ds$ provides a martingale characterization of the generator. Applications include computing expected exit times ($\mathcal{L}u = -1$), hitting probabilities ($\mathcal{L}f = 0$ with boundary conditions), and Laplace transforms of stopping times ($\mathcal{L}f = \lambda f$).

!!! warning "Ito vs. Stratonovich"
    The Ito convention is standard in finance due to its martingale properties and non-anticipating evaluation. The Stratonovich convention preserves the classical chain rule and is natural in physics. The two are related by a drift correction involving the quadratic covariation.

---
