# Neural SDE Models

**Neural SDE models** parameterize the drift and diffusion coefficients of stochastic differential equations with neural networks, learning the dynamics directly from observed paths. This approach preserves the continuous-time SDE structure required for consistent pricing and hedging, while providing the flexibility of deep learning to capture complex, nonparametric dynamics that traditional parametric models (Black-Scholes, Heston, SABR) cannot represent.

---

## From Parametric to Neural SDEs

### Classical Parametric SDEs

Traditional financial models specify drift and diffusion through parametric families. For example, the Heston model:

$$
dS_t = \mu S_t \, dt + \sqrt{v_t} \, S_t \, dW_t^S
$$

$$
dv_t = \kappa(\bar{v} - v_t) \, dt + \xi\sqrt{v_t} \, dW_t^v
$$

has 5 parameters $(\mu, \kappa, \bar{v}, \xi, \rho)$. The functional forms are fixed by modeling assumptions, which may be misspecified.

### The Neural SDE Idea

Replace parametric functional forms with neural networks:

**Definition (Neural SDE).** A neural SDE is a stochastic differential equation:

$$
dX_t = \mu_\theta(t, X_t) \, dt + \sigma_\phi(t, X_t) \, dW_t
$$

where $\mu_\theta : [0,T] \times \mathbb{R}^d \to \mathbb{R}^d$ and $\sigma_\phi : [0,T] \times \mathbb{R}^d \to \mathbb{R}^{d \times m}$ are neural networks with parameters $\theta$ and $\phi$ respectively, and $W_t$ is an $m$-dimensional Brownian motion.

The state $X_t$ may represent log-prices, factor values, latent states, or any combination thereof.

---

## Well-Posedness

For the neural SDE to define a valid stochastic process, we need existence and uniqueness of solutions.

**Theorem (Existence and Uniqueness).** If the neural drift $\mu_\theta$ and diffusion $\sigma_\phi$ satisfy:

1. **Lipschitz continuity in $x$:** There exists $L > 0$ such that for all $t \in [0,T]$ and $x, y \in \mathbb{R}^d$:

$$
|\mu_\theta(t,x) - \mu_\theta(t,y)| + |\sigma_\phi(t,x) - \sigma_\phi(t,y)| \leq L|x - y|
$$

2. **Linear growth:** There exists $K > 0$ such that for all $t, x$:

$$
|\mu_\theta(t,x)|^2 + |\sigma_\phi(t,x)|^2 \leq K^2(1 + |x|^2)
$$

then for any initial condition $X_0$ with $\mathbb{E}[|X_0|^2] < \infty$, there exists a unique strong solution.

**Remark.** Neural networks with Lipschitz activations (e.g., ReLU, tanh) and bounded weights automatically satisfy the Lipschitz condition. The linear growth condition can be enforced through architectural constraints or weight clipping.

!!! warning "Positivity and Financial Constraints"
    Unlike classical models where positivity of stock prices can be guaranteed by construction (e.g., geometric Brownian motion), neural SDEs require explicit constraints. Common approaches include:

    - Modeling $\log S_t$ instead of $S_t$
    - Using softplus activation for diffusion: $\sigma_\phi(t,x) = \log(1 + e^{\mathcal{N}_\phi(t,x)})$
    - Adding penalty terms for negativity in the loss function

---

## Training via Maximum Likelihood

### The Likelihood Problem

Given discretely observed paths $\{X_{t_0}^{(i)}, X_{t_1}^{(i)}, \ldots, X_{t_N}^{(i)}\}_{i=1}^M$ at times $0 = t_0 < t_1 < \cdots < t_N = T$, the log-likelihood is:

$$
\ell(\theta, \phi) = \sum_{i=1}^M \sum_{k=0}^{N-1} \log p_{\theta,\phi}(X_{t_{k+1}}^{(i)} \mid X_{t_k}^{(i)})
$$

where $p_{\theta,\phi}(x' \mid x)$ is the transition density of the neural SDE.

**Challenge:** The exact transition density is generally intractable for nonlinear SDEs. We must approximate it.

### Euler-Maruyama Approximation

The simplest approach uses the Euler-Maruyama discretization:

$$
X_{t_{k+1}} \approx X_{t_k} + \mu_\theta(t_k, X_{t_k})\,\Delta t_k + \sigma_\phi(t_k, X_{t_k})\,\Delta W_k
$$

This gives a Gaussian transition density:

$$
p_{\theta,\phi}^{\text{EM}}(x' \mid x) = \mathcal{N}\!\left(x' \;\middle|\; x + \mu_\theta(t,x)\,\Delta t, \; \sigma_\phi(t,x)\sigma_\phi(t,x)^\top \Delta t\right)
$$

The approximate log-likelihood becomes:

$$
\ell^{\text{EM}}(\theta, \phi) = -\frac{1}{2}\sum_{i,k}\left[\log\det(\Sigma_{ik}) + (\Delta X_{ik} - \mu_{ik}\Delta t)^\top \Sigma_{ik}^{-1}(\Delta X_{ik} - \mu_{ik}\Delta t)\right]
$$

where $\Delta X_{ik} = X_{t_{k+1}}^{(i)} - X_{t_k}^{(i)}$, $\mu_{ik} = \mu_\theta(t_k, X_{t_k}^{(i)})$, and $\Sigma_{ik} = \sigma_\phi(t_k, X_{t_k}^{(i)})\sigma_\phi(t_k, X_{t_k}^{(i)})^\top \Delta t_k$.

---

## Training via Adjoint Methods

### The Continuous Adjoint

For neural SDEs with many time steps, backpropagation through the Euler-Maruyama scheme requires storing all intermediate states (memory cost $O(N)$). The **adjoint method** reduces memory to $O(1)$ by solving a backward SDE.

**Theorem (Stochastic Adjoint -- Li et al. 2020).** Define the loss $\mathcal{L} = \mathbb{E}[\ell(X_T)]$ where $X_T$ solves the neural SDE. The gradient with respect to parameters $\theta$ is:

$$
\frac{d\mathcal{L}}{d\theta} = \mathbb{E}\!\left[\int_0^T a_t^\top \frac{\partial \mu_\theta}{\partial \theta}(t, X_t) \, dt + \int_0^T \operatorname{tr}\!\left(\frac{\partial \sigma_\phi}{\partial \theta}(t, X_t)^\top a_t \, dW_t\right)\right]
$$

where the adjoint process $a_t \in \mathbb{R}^d$ satisfies the backward SDE:

$$
da_t = -\left(\frac{\partial \mu_\theta}{\partial x}\right)^\top a_t \, dt - \left(\frac{\partial \sigma_\phi}{\partial x}\right)^\top a_t \, dW_t, \quad a_T = \nabla_x \ell(X_T)
$$

The adjoint SDE is integrated backward from $T$ to $0$ alongside the forward SDE, requiring only $O(1)$ memory instead of $O(N)$.

### Practical Implementation

The training procedure is:

1. **Forward pass:** Solve the neural SDE forward from $t = 0$ to $t = T$ using an SDE solver (Euler-Maruyama, Milstein, or adaptive)
2. **Backward pass:** Solve the adjoint SDE backward from $T$ to $0$, accumulating parameter gradients
3. **Update:** Apply Adam or SGD to update $\theta, \phi$

!!! note "SDE Solvers"
    Higher-order SDE solvers (Milstein, stochastic Runge-Kutta) improve the accuracy of the forward simulation. The Milstein scheme for scalar noise adds the correction:

    $$
    X_{t_{k+1}} = X_{t_k} + \mu \, \Delta t + \sigma \, \Delta W + \frac{1}{2}\sigma \frac{\partial \sigma}{\partial x}((\Delta W)^2 - \Delta t)
    $$

    where the correction term involves $\partial\sigma/\partial x$, readily available via autodiff for neural diffusion coefficients.

---

## Latent Neural SDEs

### Motivation

Often the observed data (e.g., asset prices) does not directly evolve as an SDE. A **latent neural SDE** introduces a hidden state:

$$
dZ_t = \mu_\theta(t, Z_t) \, dt + \sigma_\phi(t, Z_t) \, dW_t
$$

$$
X_t = g_\psi(Z_t)
$$

where $Z_t \in \mathbb{R}^p$ is a latent process (possibly higher-dimensional than the observations) and $g_\psi$ is an observation network.

### Variational Inference

Since the latent process is unobserved, we use variational inference. Introduce an approximate posterior $q_\lambda(Z_{0:T} \mid X_{0:T})$, itself parameterized as a neural SDE:

$$
dZ_t = \tilde{\mu}_\lambda(t, Z_t, X_{0:T}) \, dt + \sigma_\phi(t, Z_t) \, dW_t
$$

The training objective is the **evidence lower bound (ELBO)**:

$$
\text{ELBO} = \mathbb{E}_q\!\left[\log p_\psi(X_{0:T} \mid Z_{0:T})\right] - D_{\text{KL}}\!\left(q_\lambda(Z_{0:T} \mid X_{0:T}) \| p_{\theta,\phi}(Z_{0:T})\right)
$$

The KL divergence between two SDEs with the same diffusion takes the Girsanov form:

$$
D_{\text{KL}}(q \| p) = \frac{1}{2}\mathbb{E}_q\!\left[\int_0^T \left\|\sigma^{-1}(\tilde{\mu}_\lambda - \mu_\theta)\right\|^2 dt\right]
$$

---

## Neural SDEs for Financial Modeling

### Stochastic Volatility Discovery

A neural SDE can learn stochastic volatility dynamics directly from option prices or underlying returns:

$$
d\log S_t = \left(r - \frac{1}{2}v_\theta(t, \log S_t, Z_t)\right)dt + \sqrt{v_\theta(t, \log S_t, Z_t)} \, dW_t^S
$$

$$
dZ_t = \alpha_\theta(t, Z_t) \, dt + \beta_\theta(t, Z_t) \, dW_t^Z
$$

where $v_\theta, \alpha_\theta, \beta_\theta$ are neural networks and $Z_t$ is a latent volatility factor. The model discovers the volatility dynamics from data rather than imposing Heston, SABR, or other parametric forms.

### Calibration to Market Data

Neural SDEs can be calibrated to fit market observables:

$$
\min_{\theta,\phi} \sum_{i} w_i \left|V_{\text{market}}^{(i)} - V_{\theta,\phi}^{(i)}\right|^2
$$

where $V_{\theta,\phi}^{(i)}$ are model prices computed via Monte Carlo simulation of the neural SDE. The neural coefficients provide enough flexibility to fit the entire volatility surface simultaneously, unlike parametric models that trade off different regions.

### Generative Modeling for Scenario Analysis

Trained neural SDEs serve as generative models for risk management:

1. Calibrate the neural SDE to historical data
2. Simulate many future paths from the learned dynamics
3. Compute risk measures (VaR, ES) under the learned distribution

The advantage over historical simulation is that the neural SDE can generate paths beyond the historical record, capturing learned dynamics and correlations.

---

## Connection to Diffusion Models and Score Matching

Neural SDEs are closely connected to **score-based generative models** (diffusion models):

**Forward process:** Gradually add noise to data via a fixed SDE:

$$
dX_t = f(t, X_t) \, dt + g(t) \, dW_t
$$

**Reverse process:** Denoise by reversing the SDE:

$$
dX_t = \left[f(t, X_t) - g(t)^2 \nabla_x \log p_t(X_t)\right]dt + g(t) \, d\bar{W}_t
$$

The **score function** $\nabla_x \log p_t(x)$ is learned by a neural network via score matching:

$$
\min_\theta \mathbb{E}_{t, X_t}\!\left[\left\|s_\theta(t, X_t) - \nabla_x \log p_t(X_t)\right\|^2\right]
$$

In finance, diffusion models can generate realistic return distributions, implied volatility surfaces, and yield curve scenarios.

---

## Key Takeaways

1. **Neural SDEs** replace parametric drift and diffusion with neural networks, learning continuous-time dynamics from discrete observations while preserving SDE structure.

2. **Well-posedness** is guaranteed under Lipschitz and linear growth conditions, which neural networks with bounded weights satisfy.

3. **Adjoint methods** enable memory-efficient training by solving a backward SDE for gradients, avoiding storage of all forward states.

4. **Latent neural SDEs** with variational inference can model complex dynamics with unobserved state variables, naturally extending classical stochastic volatility models.

5. **Financial applications** include volatility surface calibration, generative scenario modeling, and learning pricing dynamics directly from market data.

---

## Further Reading

- Li, Wong, Chen & Duvenaud (2020), "Scalable Gradients for Stochastic Differential Equations"
- Kidger, Foster, Li & Lyons (2021), "Neural SDEs as Infinite-Dimensional GANs"
- Gierjatowicz, Sabate-Vidales, Siska & Szpruch (2022), "Robust Pricing and Hedging via Neural SDEs"
- Tzen & Raginsky (2019), "Neural Stochastic Differential Equations"
- Song, Sohl-Dickstein, Kingma et al. (2021), "Score-Based Generative Modeling through SDEs"

---

## Exercises

**Exercise 1.** Write the Euler-Maruyama discretization for the neural SDE $dX_t = \mu_\theta(t, X_t)dt + \sigma_\phi(t, X_t)dW_t$ and the associated Gaussian transition density. Given observations $X_0 = 100$ and $X_{\Delta t} = 102$ with $\Delta t = 1/252$ (one trading day), and neural network outputs $\mu_\theta = 0.05$ and $\sigma_\phi = 0.20$, compute the log-likelihood of this single transition. How does the likelihood change if $\sigma_\phi = 0.40$?

---

**Exercise 2.** Explain why neural networks with Lipschitz activations (e.g., ReLU with $|\text{ReLU}(x) - \text{ReLU}(y)| \le |x - y|$) and bounded weights produce Lipschitz drift and diffusion functions. If the weight matrices satisfy $\|W^{(\ell)}\|_2 \le B$ for all layers, derive an upper bound on the Lipschitz constant of the neural network in terms of $B$ and the depth $L$. Discuss how weight clipping during training ensures well-posedness of the neural SDE.

---

**Exercise 3.** A neural SDE is used to model stock price dynamics: $d\log S_t = \mu_\theta(t, \log S_t)dt + \sigma_\phi(t, \log S_t)dW_t$. Explain why modeling $\log S$ rather than $S$ naturally ensures positivity of prices. If the neural diffusion uses softplus activation $\sigma_\phi = \log(1 + e^{\mathcal{N}_\phi})$, show that $\sigma_\phi > 0$ always. What would happen if $\sigma_\phi$ could become zero or negative?

---

**Exercise 4.** The adjoint method computes gradients with $O(1)$ memory instead of $O(N)$. Explain the memory bottleneck in standard backpropagation through the Euler-Maruyama scheme: why must all $N$ intermediate states $\{X_{t_k}\}$ be stored? For a neural SDE with 252 daily time steps over 1 year and state dimension $d = 5$, estimate the memory savings of the adjoint method. What is the computational tradeoff (i.e., what additional computation does the adjoint method require)?

---

**Exercise 5.** Describe how a latent neural SDE with variational inference extends classical stochastic volatility models. In the Heston model, the latent state is the variance $v_t$. In the latent neural SDE, the latent state $Z_t \in \mathbb{R}^p$ is learned from data. The KL divergence between the posterior and prior SDEs takes the Girsanov form

$$
D_{\text{KL}}(q \| p) = \frac{1}{2}\mathbb{E}_q\left[\int_0^T \left\|\sigma^{-1}(\tilde{\mu}_\lambda - \mu_\theta)\right\|^2 dt\right]
$$

Explain why this penalizes the posterior drift $\tilde{\mu}_\lambda$ for deviating from the prior drift $\mu_\theta$, acting as a regularizer on the latent dynamics.

---

**Exercise 6.** A neural SDE is calibrated to fit the implied volatility surface by minimizing $\sum_i w_i|V_{\text{market}}^{(i)} - V_{\theta,\phi}^{(i)}|^2$. The model prices $V_{\theta,\phi}^{(i)}$ are computed by Monte Carlo simulation of the neural SDE. Discuss the computational challenges: (a) the loss gradient requires differentiating through the Monte Carlo simulation, (b) the variance of the Monte Carlo estimator affects gradient quality. How do techniques like reparameterization (pathwise gradients) and variance reduction help?

---

**Exercise 7.** Compare neural SDEs to classical parametric models (Black-Scholes, Heston, SABR) on three criteria: (a) flexibility to fit the volatility surface, (b) interpretability of model parameters, and (c) out-of-sample stability. Argue that neural SDEs offer superior fit but potentially worse interpretability and stability. Propose a hybrid approach that combines parametric structure with neural network corrections, and explain how this might achieve the benefits of both.
