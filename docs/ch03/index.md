# Chapter 3: Stochastic Differential Equations

This chapter develops the theory of stochastic differential equations from empirical motivation through rigorous construction. Beginning with the statistical properties of real financial returns and the failure of deterministic models, we build the Ito integral, derive Ito's formula, define and solve SDEs for canonical financial models, establish existence and uniqueness theory, and study the structural properties of diffusion processes and their infinitesimal generators.

## Key Concepts

### **Empirical Motivation**
Real stock returns exhibit **stylized facts** that deterministic models cannot capture: heavy tails (excess kurtosis of 7--10 for daily S&P 500 returns versus 3 for the Gaussian), volatility clustering (GARCH effects where large moves beget large moves), the leverage effect (asymmetric volatility response to positive vs. negative returns), absence of return autocorrelation, and aggregational Gaussianity (returns become more Gaussian at lower frequencies). Proper empirical analysis begins with adjusted close prices that correct for dividends, splits, and corporate actions to ensure return continuity. The exponential growth ODE $dS/dt = \mu S$ produces smooth, infinitely differentiable, perfectly predictable paths with zero variance---fundamentally incompatible with observed data. The deterministic model cannot generate randomness, heavy tails, volatility clustering, or any of the documented stylized facts. Adding a multiplicative noise term $\sigma S\, dW_t$ bridges the gap from deterministic to stochastic models and motivates the SDE framework, transitioning from discrete-time observations to continuous-time theory.

### **Ito Integration**
Classical Riemann-Stieltjes integration fails for Brownian motion because its paths have unbounded (infinite) first variation: $\text{Var}_{[0,t]}(B) = \infty$ almost surely. The Ito integral $\int_0^t H_s\, dW_s$ is constructed via $L^2$-approximation: first for simple (step-function) integrands as finite sums $\sum_i H_{t_i}(W_{t_{i+1}} - W_{t_i})$ evaluated at left endpoints, then extended by continuity using the **Ito isometry**

$$\mathbb{E}\!\left[\left(\int_0^t H_s\, dW_s\right)^{\!2}\right] = \mathbb{E}\!\left[\int_0^t H_s^2\, ds\right]$$

The Ito isometry arises because cross terms $\mathbb{E}[\beta_i \beta_j \Delta W_i \Delta W_j] = 0$ for $i < j$ vanish by the independence of Brownian increments from adapted integrands. The resulting integral is a **continuous martingale** with zero expectation, is linear in the integrand, and has **quadratic variation** $\langle \int H\, dW \rangle_t = \int_0^t H_s^2\, ds$. Financial interpretation: the Ito integral represents cumulative profit/loss from holding $H_s$ shares of a stock whose price follows $dB_s$, with the key distinction from ordinary integration being that the increments $dB_s$ are random.

### **Ito Processes and Stratonovich Integration**
The general **Ito process** $X_t = X_0 + \int_0^t b_s\, ds + \int_0^t \sigma_s\, dW_s$ (written $dX_t = b_t\, dt + \sigma_t\, dW_t$) decomposes into a drift term (deterministic, predictable, finite variation) and a martingale term (stochastic integral, zero-mean fluctuations). This decomposition makes Ito processes the natural class of semimartingales for stochastic calculus. The **Stratonovich integral** $\int_0^t H_s \circ dW_s$ uses midpoint evaluation instead of left-endpoint evaluation, satisfies the classical chain rule, but loses the martingale property; the two conventions are related by

$$\int H_s \circ dW_s = \int H_s\, dW_s + \frac{1}{2}\langle H, W \rangle_t$$

The Ito convention is standard in finance due to its martingale properties and non-anticipating evaluation, while the Stratonovich convention is natural in physics where classical transformation rules are preferred.

### **Ito's Formula**
Ito's formula is the stochastic chain rule---the **fundamental theorem of stochastic calculus**. Just as the classical Fundamental Theorem of Calculus turns painful Riemann sums into antiderivative evaluations, Ito's lemma turns painful stochastic integral computations into systematic applications of a chain rule. The derivation proceeds via Taylor expansion: the linear approximation $df \approx f'(x)\, dx$ leaves a non-vanishing residual because $(dW_t)^2 = dt$ (quadratic variation), forcing retention of the second-order term. The **Ito rules** (box calculus) are $(dt)^2 = 0$, $dt \cdot dW_t = 0$, $(dW_t)^2 = dt$. For $f \in C^{1,2}$ and an Ito process $X_t$:

$$df(t, X_t) = \frac{\partial f}{\partial t}\, dt + \frac{\partial f}{\partial x}\, dX_t + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}\, (dX_t)^2$$

where $(dX_t)^2 = \sigma^2\, dt$. Extensions include:

- **Ito product rule**: $d(X_t Y_t) = X_t\, dY_t + Y_t\, dX_t + d\langle X, Y \rangle_t$, where the quadratic covariation $d\langle X,Y\rangle_t = b_t^\alpha d_t^\alpha\, dt$ (Einstein summation) captures the extra term absent in classical calculus
- **Ito quotient rule**: $d(X_t/Y_t)$ derived via the product rule applied to $X_t \cdot Y_t^{-1}$
- **Integration by parts**: $\int_0^t X_s\, dY_s = X_t Y_t - X_0 Y_0 - \int_0^t Y_s\, dX_s - \langle X, Y \rangle_t$
- **Multidimensional version**: for $X_t \in \mathbb{R}^d$ driven by $m$-dimensional Brownian motion with $dX_t^i = b^i\, dt + \sigma^{i\alpha}\, dW_t^\alpha$, the formula becomes $df = \partial_t f\, dt + \partial_i f\, dX^i + \frac{1}{2} a^{ij} \partial_{ij} f\, dt$ where $a^{ij} = \sigma^{i\alpha}\sigma^{j\alpha}$

### **Stochastic Differential Equations**
An SDE

$$dX_t = b(t, X_t)\, dt + \sigma(t, X_t)\, dW_t$$

defines a diffusion process through its drift $b$ and diffusion coefficient $\sigma$. The $dX_t$ notation is shorthand for the integral equation $X_t = X_0 + \int_0^t b(s,X_s)\, ds + \int_0^t \sigma(s,X_s)\, dW_s$. Canonical examples include:

- **Geometric Brownian motion** $dS = \mu S\, dt + \sigma S\, dW$, solved via Ito's lemma applied to $\ln S$ to obtain $S_t = S_0 \exp((\mu - \sigma^2/2)t + \sigma W_t)$
- **Ornstein-Uhlenbeck process** (mean-reverting dynamics) $dX_t = \theta(\mu - X_t)\, dt + \sigma\, dW_t$, solved via integrating factor
- **Square-root (CIR) process** $dX_t = \kappa(\theta - X_t)\, dt + \sigma\sqrt{X_t}\, dW_t$, ensuring non-negativity under the Feller condition

Solving techniques include the **Ito-formula ansatz** (guessing $f(W_t, t)$ and matching coefficients), exponential transformations, and variation of constants. **Verification** of candidate solutions uses Ito's formula to confirm the SDE is satisfied: compute $dX_t$ from the proposed solution and check it matches the original SDE's drift and diffusion. **Moment analysis** derives $\mathbb{E}[X_t]$ and $\text{Var}(X_t)$ via Ito's lemma and moment ODEs without requiring closed-form solutions. **Numerical simulation** via Euler-Maruyama discretization

$$X_{i+1} = X_i + b(t_i, X_i)\,\Delta t + \sigma(t_i, X_i)\,\sqrt{\Delta t}\, Z_i, \quad Z_i \sim \mathcal{N}(0,1)$$

enables Monte Carlo pricing when analytic solutions are unavailable, with the discrete random walk serving as the conceptual foundation.

### **Existence and Uniqueness**
The fundamental theorem for SDEs guarantees a unique **strong solution** under two conditions. The **Lipschitz condition**

$$|b(t,x) - b(t,y)| + |\sigma(t,x) - \sigma(t,y)| \leq K|x-y|$$

ensures that nearby initial conditions produce nearby solutions (uniqueness), while the **linear growth condition**

$$|b(t,x)| + |\sigma(t,x)| \leq K(1 + |x|)$$

prevents finite-time explosion (global existence). The constructive proof uses **Picard iteration**: starting from $X_t^{(0)} = x_0$, successive approximations

$$X^{(n+1)}_t = x_0 + \int_0^t b(s, X^{(n)}_s)\, ds + \int_0^t \sigma(s, X^{(n)}_s)\, dW_s$$

converge in $L^2$ under the Lipschitz condition, analogous to the classical Picard-Lindelof theorem for ODEs. The distinction between **strong solutions** (adapted to the given Brownian motion, i.e., $X_t = F(W_s : 0 \leq s \leq t)$ is a functional of the given noise) and **weak solutions** (where the probability space and Brownian motion may be constructed as part of the solution, requiring only the correct joint distribution) is essential: strong uniqueness implies weak uniqueness (Yamada-Watanabe theorem) but not conversely.

### **Diffusion Processes**
Solutions to SDEs with Markov coefficients are **diffusion processes**---continuous-path Markov processes completely characterized by their drift and diffusion coefficients. They are formally defined as Ito diffusions $dX_t^i = b^i(t,X_t)\, dt + \sigma^{i\alpha}(t,X_t)\, dW_t^\alpha$ on a filtered probability space satisfying the usual conditions. The **strong Markov property** extends the memoryless property from deterministic times to stopping times: for any stopping time $\tau$,

$$\mathbb{E}[\varphi(X_{\tau+t}) \mid \mathcal{F}_\tau] = \mathbb{E}^{X_\tau}[\varphi(X_t)]$$

meaning that conditionally on $X_\tau$, the post-$\tau$ evolution is independent of the past and distributed like a fresh copy started from $X_\tau$. The **Stroock-Varadhan martingale problem** provides an alternative characterization: a diffusion with generator $\mathcal{L}$ is defined by requiring $f(X_t) - \int_0^t \mathcal{L}f(X_s)\, ds$ to be a local martingale for all test functions $f \in C_c^\infty$, which is fundamental for uniqueness in law and weak convergence arguments. **Invariant measures** $\pi$ satisfying $\int P_t f\, d\pi = \int f\, d\pi$ (equivalently, $X_0 \sim \pi$ implies $X_t \sim \pi$) describe long-run stationary behavior. **Time reversal** reveals how the reversed process $\widetilde{X}_t = X_{T-t}$ satisfies an SDE with modified drift involving the **score function** $\nabla \log p(t,x)$ of the forward density. **Large deviations** (Freidlin-Wentzell theory) quantify how the small-noise diffusion $dX^\varepsilon = b\, dt + \sqrt{\varepsilon}\,\sigma\, dW$ concentrates near the deterministic ODE solution $\dot{\bar{x}} = b(\bar{x})$ as $\varepsilon \to 0$, with exponentially small probabilities of atypical paths governed by the rate function $I_{0,T}(\phi) = \frac{1}{2}\int_0^T |\sigma^{-1}(\dot{\phi} - b(\phi))|^2\, dt$.

### **Infinitesimal Generators**
The generator of a diffusion captures the instantaneous rate of change of conditional expectations:

$$\mathcal{L}f(x) = \lim_{h \downarrow 0} \frac{\mathbb{E}^x[f(X_h)] - f(x)}{h} = b^i(x)\, \partial_i f + \frac{1}{2} a^{ij}(x)\, \partial_{ij} f$$

where $a = \sigma\sigma^\top$ is the diffusion matrix. For geometric Brownian motion, $\mathcal{L} = \mu S\, \partial_S + \frac{1}{2}\sigma^2 S^2\, \partial_{SS}$, and the Black-Scholes PDE is precisely $\partial_t V + \mathcal{L}^{(r)}V - rV = 0$---the generator is the bridge connecting stochastic models to pricing PDEs. **Dynkin's formula**

$$\mathbb{E}_x[f(X_\tau)] = f(x) + \mathbb{E}_x\!\left[\int_0^\tau \mathcal{L}f(X_s)\, ds\right]$$

is the stochastic fundamental theorem of calculus, connecting expected values at stopping times to the generator (analogous to $g(b) - g(a) = \int_a^b g'(x)\, dx$). The **Dynkin martingale** $M_t = f(X_t) - f(X_0) - \int_0^t \mathcal{L}f(X_s)\, ds$ provides a martingale characterization of the generator: via Ito's lemma, $M_t = \int_0^t f'(X_s)\sigma(X_s)\, dW_s$, separating the process into predictable drift (captured by $\mathcal{L}$) and unpredictable martingale fluctuations. Functions satisfying $\mathcal{L}f = 0$ are **harmonic** and give rise to martingales $f(X_t)$. Applications of Dynkin's formula include computing expected exit times ($\mathcal{L}u = -1$ with $u = 0$ on $\partial D$), hitting probabilities ($\mathcal{L}f = 0$ with boundary conditions $f = g$ on $\partial D$), and Laplace transforms of stopping times ($\mathcal{L}f = \lambda f$ with $f = 1$ on the target).

!!! warning "Ito vs. Stratonovich"
    The Ito convention is standard in finance due to its martingale properties and non-anticipating evaluation. The Stratonovich convention preserves the classical chain rule and is natural in physics. The two are related by a drift correction involving the quadratic covariation.

---
