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

??? success "Solution to Exercise 1"
    **Euler-Maruyama discretization:**

    $$
    X_{t_{k+1}} \approx X_{t_k} + \mu_\theta(t_k, X_{t_k}) \, \Delta t + \sigma_\phi(t_k, X_{t_k}) \, \Delta W_k
    $$

    where $\Delta W_k \sim \mathcal{N}(0, \Delta t)$.

    **Gaussian transition density:**

    $$
    p_{\theta,\phi}^{\text{EM}}(x' \mid x) = \frac{1}{\sqrt{2\pi \sigma_\phi^2 \Delta t}} \exp\!\left(-\frac{(x' - x - \mu_\theta \Delta t)^2}{2\sigma_\phi^2 \Delta t}\right)
    $$

    **Log-likelihood computation.** Given $X_0 = 100$, $X_{\Delta t} = 102$, $\Delta t = 1/252$, $\mu_\theta = 0.05$, and $\sigma_\phi = 0.20$:

    The increment is $\Delta X = 102 - 100 = 2$.

    The predicted mean of the increment is $\mu_\theta \Delta t = 0.05 / 252 \approx 0.000198$.

    The variance of the increment is $\sigma_\phi^2 \Delta t = 0.04 / 252 \approx 0.0001587$.

    The log-likelihood of this single transition is:

    $$
    \ell = -\frac{1}{2}\log(2\pi \sigma_\phi^2 \Delta t) - \frac{(\Delta X - \mu_\theta \Delta t)^2}{2\sigma_\phi^2 \Delta t}
    $$

    Computing term by term:

    $$
    \sigma_\phi^2 \Delta t = 0.04 \times \frac{1}{252} = 1.587 \times 10^{-4}
    $$

    $$
    -\frac{1}{2}\log(2\pi \times 1.587 \times 10^{-4}) = -\frac{1}{2}\log(9.974 \times 10^{-4}) \approx -\frac{1}{2}(-6.911) \approx 3.456
    $$

    $$
    \frac{(\Delta X - \mu_\theta \Delta t)^2}{2\sigma_\phi^2 \Delta t} = \frac{(2 - 0.000198)^2}{2 \times 1.587 \times 10^{-4}} = \frac{3.999}{3.175 \times 10^{-4}} \approx 12{,}597
    $$

    $$
    \ell \approx 3.456 - 12{,}597 \approx -12{,}594
    $$

    This is an extremely negative log-likelihood, reflecting that a 2-point move in one day is extremely unlikely under $\sigma = 0.20$ (the daily standard deviation is $\sigma\sqrt{\Delta t} \approx 0.20/\sqrt{252} \approx 0.0126$, so a move of 2 is roughly $2/0.0126 \approx 159$ standard deviations).

    **With $\sigma_\phi = 0.40$:**

    $$
    \sigma_\phi^2 \Delta t = 0.16/252 = 6.349 \times 10^{-4}
    $$

    $$
    -\frac{1}{2}\log(2\pi \times 6.349 \times 10^{-4}) \approx -\frac{1}{2}\log(3.989 \times 10^{-3}) \approx 2.763
    $$

    $$
    \frac{(2 - 0.000198)^2}{2 \times 6.349 \times 10^{-4}} = \frac{3.999}{1.270 \times 10^{-3}} \approx 3{,}149
    $$

    $$
    \ell \approx 2.763 - 3{,}149 \approx -3{,}147
    $$

    Doubling $\sigma_\phi$ greatly increases the log-likelihood (from $-12{,}594$ to $-3{,}147$) because the wider variance makes the large observed move less improbable. However, the likelihood is still very low, indicating that even $\sigma = 0.40$ is insufficient to explain a 2-point daily move in a level-100 asset (the daily standard deviation is $0.40/\sqrt{252} \approx 0.0252$, so the move is still about $2/0.0252 \approx 79$ standard deviations). This illustrates that the Euler-Maruyama approximation applied to price levels (rather than log-prices) can produce misleading likelihoods.

---

**Exercise 2.** Explain why neural networks with Lipschitz activations (e.g., ReLU with $|\text{ReLU}(x) - \text{ReLU}(y)| \le |x - y|$) and bounded weights produce Lipschitz drift and diffusion functions. If the weight matrices satisfy $\|W^{(\ell)}\|_2 \le B$ for all layers, derive an upper bound on the Lipschitz constant of the neural network in terms of $B$ and the depth $L$. Discuss how weight clipping during training ensures well-posedness of the neural SDE.

??? success "Solution to Exercise 2"
    **Lipschitz property of neural networks.**

    Consider a feedforward network $\mathcal{N}_\theta(x) = W^{(L+1)} \sigma(W^{(L)} \cdots \sigma(W^{(1)} x + b^{(1)}) \cdots + b^{(L)}) + b^{(L+1)}$.

    For ReLU activation, $|\sigma(a) - \sigma(b)| \leq |a - b|$ for all $a, b \in \mathbb{R}$ (Lipschitz constant 1). For tanh, $|\tanh(a) - \tanh(b)| \leq |a - b|$ (since $|\tanh'(z)| = 1 - \tanh^2(z) \leq 1$).

    **Deriving the Lipschitz bound.** Consider the mapping at each layer:

    $$
    h^{(\ell)}(x) = \sigma(W^{(\ell)} h^{(\ell-1)}(x) + b^{(\ell)})
    $$

    For two inputs $x, y$:

    $$
    |h^{(\ell)}(x) - h^{(\ell)}(y)| \leq |W^{(\ell)}(h^{(\ell-1)}(x) - h^{(\ell-1)}(y))| \leq \|W^{(\ell)}\|_2 \cdot |h^{(\ell-1)}(x) - h^{(\ell-1)}(y)|
    $$

    where we used the Lipschitz property of $\sigma$ (Lipschitz constant 1) and the operator norm of $W^{(\ell)}$.

    Iterating from layer 1 to layer $L+1$:

    $$
    |\mathcal{N}_\theta(x) - \mathcal{N}_\theta(y)| \leq \prod_{\ell=1}^{L+1} \|W^{(\ell)}\|_2 \cdot |x - y|
    $$

    If $\|W^{(\ell)}\|_2 \leq B$ for all layers, the Lipschitz constant of the network is:

    $$
    \text{Lip}(\mathcal{N}_\theta) \leq B^{L+1}
    $$

    This grows exponentially with depth $L$ for $B > 1$, but remains controlled for $B \leq 1$.

    **Weight clipping for well-posedness.** During training, if we clip weights so that $\|W^{(\ell)}\|_2 \leq B$ after each gradient step, we guarantee:

    - Lipschitz continuity of $\mu_\theta$ and $\sigma_\phi$ with constant $\leq B^{L+1}$, satisfying the first existence/uniqueness condition.
    - Linear growth: since the bias terms are bounded and the network is Lipschitz, $|\mathcal{N}_\theta(t,x)| \leq |\mathcal{N}_\theta(t,0)| + B^{L+1}|x| \leq C + B^{L+1}|x|$, which gives the required linear growth bound with $K = \max(C, B^{L+1})$.

    Alternative techniques include spectral normalization (dividing $W^{(\ell)}$ by $\|W^{(\ell)}\|_2$ after each update) and gradient penalty regularization. These provide the same theoretical guarantee while being less restrictive during training.

---

**Exercise 3.** A neural SDE is used to model stock price dynamics: $d\log S_t = \mu_\theta(t, \log S_t)dt + \sigma_\phi(t, \log S_t)dW_t$. Explain why modeling $\log S$ rather than $S$ naturally ensures positivity of prices. If the neural diffusion uses softplus activation $\sigma_\phi = \log(1 + e^{\mathcal{N}_\phi})$, show that $\sigma_\phi > 0$ always. What would happen if $\sigma_\phi$ could become zero or negative?

??? success "Solution to Exercise 3"
    **Positivity from log-price modeling.**

    If we model $\log S_t$ rather than $S_t$ directly, then $S_t = e^{\log S_t}$, which is strictly positive for any value of $\log S_t \in \mathbb{R}$. The neural SDE for $Y_t = \log S_t$ is:

    $$
    dY_t = \mu_\theta(t, Y_t) \, dt + \sigma_\phi(t, Y_t) \, dW_t
    $$

    Since $Y_t$ can take any real value, no boundary constraints are needed. The stock price $S_t = e^{Y_t}$ is automatically positive.

    **Softplus ensures $\sigma_\phi > 0$.**

    The softplus function is $\text{softplus}(z) = \log(1 + e^z)$. We need to show this is strictly positive for all $z \in \mathbb{R}$:

    - For all $z$, $e^z > 0$, so $1 + e^z > 1$, thus $\log(1 + e^z) > \log(1) = 0$.

    Therefore $\sigma_\phi = \text{softplus}(\mathcal{N}_\phi(t, Y_t)) > 0$ for any network output $\mathcal{N}_\phi \in \mathbb{R}$.

    Additionally, softplus is smooth and monotonically increasing, with $\text{softplus}(z) \to 0^+$ as $z \to -\infty$ and $\text{softplus}(z) \approx z$ as $z \to +\infty$. This means the network can represent both very small and very large volatilities.

    **If $\sigma_\phi$ could become zero or negative:**

    - *Zero diffusion ($\sigma_\phi = 0$):* The SDE degenerates to an ODE at that point, $dY_t = \mu_\theta \, dt$. This causes the transition density to become singular (a Dirac delta), making the likelihood ill-defined. The Euler-Maruyama Gaussian approximation has zero variance, and the log-likelihood $-\frac{(\Delta Y)^2}{2\sigma^2 \Delta t}$ diverges to $-\infty$ for any nonzero increment. This creates numerical instability during training.

    - *Negative diffusion ($\sigma_\phi < 0$):* The SDE $dY_t = \mu_\theta \, dt + \sigma_\phi \, dW_t$ is still well-defined since multiplying Brownian motion by a negative constant simply reverses the sign (which is a valid Brownian motion by symmetry). However, the diffusion matrix $\sigma\sigma^\top = \sigma_\phi^2 \geq 0$ is still non-negative, so the SDE itself does not break. The real issue is that the *sign ambiguity* creates non-identifiability: $(\mu, \sigma)$ and $(\mu, -\sigma)$ produce the same dynamics. This can cause training instability as the optimizer oscillates between the two solutions. Enforcing $\sigma_\phi > 0$ via softplus resolves this identifiability issue.

---

**Exercise 4.** The adjoint method computes gradients with $O(1)$ memory instead of $O(N)$. Explain the memory bottleneck in standard backpropagation through the Euler-Maruyama scheme: why must all $N$ intermediate states $\{X_{t_k}\}$ be stored? For a neural SDE with 252 daily time steps over 1 year and state dimension $d = 5$, estimate the memory savings of the adjoint method. What is the computational tradeoff (i.e., what additional computation does the adjoint method require)?

??? success "Solution to Exercise 4"
    **Memory bottleneck in standard backpropagation.**

    The Euler-Maruyama scheme computes:

    $$
    X_{t_{k+1}} = X_{t_k} + \mu_\theta(t_k, X_{t_k}) \, \Delta t + \sigma_\phi(t_k, X_{t_k}) \, \Delta W_k, \quad k = 0, 1, \ldots, N-1
    $$

    Standard backpropagation (reverse-mode autodiff) computes gradients by traversing the computation graph backward. At step $k$, the gradient $\partial \mathcal{L}/\partial \theta$ depends on $X_{t_k}$ (because $\mu_\theta$ and $\sigma_\phi$ were evaluated at $X_{t_k}$). To compute the backward pass, all intermediate states $\{X_{t_0}, X_{t_1}, \ldots, X_{t_N}\}$ must be stored during the forward pass. This is because the chain rule at step $k$ requires both the local Jacobians $\partial \mu_\theta / \partial \theta$ and $\partial \mu_\theta / \partial x$ evaluated at $X_{t_k}$.

    Total memory: $O(N \times d)$ for the states, plus $O(N)$ for the Brownian increments.

    **Memory savings for the specific problem.** With $N = 252$ daily steps and $d = 5$:

    - Standard backprop: stores $N \times d = 252 \times 5 = 1{,}260$ floating-point values for states, plus $N \times d = 1{,}260$ for Brownian increments, plus network activations at each step. Total: $O(N) = O(252)$ memory blocks.

    - Adjoint method: stores only the current state $X_t$ ($d = 5$ values), the current adjoint $a_t$ ($d = 5$ values), and accumulated gradients. Total: $O(1)$ memory blocks (constant in $N$).

    The memory reduction factor is $O(N) = O(252)$, approximately 250x savings. For longer simulations (e.g., 10 years daily $= 2{,}520$ steps), the savings are even more dramatic.

    **Computational tradeoff.** The adjoint method requires solving the backward SDE:

    $$
    da_t = -\left(\frac{\partial \mu_\theta}{\partial x}\right)^\top a_t \, dt - \left(\frac{\partial \sigma_\phi}{\partial x}\right)^\top a_t \, dW_t
    $$

    This means:

    1. The forward SDE must be solved again during the backward pass (since $X_t$ is not stored and is needed to evaluate the Jacobians). Alternatively, the forward SDE can be solved backward (using the stored terminal value $X_T$ and the same Brownian increments), but this introduces additional discretization error.

    2. The backward SDE solver requires evaluating Jacobians $\partial \mu_\theta / \partial x$ and $\partial \sigma_\phi / \partial x$ at each backward step, which involves additional autodiff computations.

    3. The overall wall-clock time is roughly doubled (one forward pass + one backward pass), compared to the standard approach which has one forward pass and one (cheaper) backward pass using stored states.

    The tradeoff is: **$O(1)$ memory at the cost of roughly $2\times$ computation time.** For problems where memory is the binding constraint (large $N$, large $d$, or limited GPU memory), the adjoint method is essential.

---

**Exercise 5.** Describe how a latent neural SDE with variational inference extends classical stochastic volatility models. In the Heston model, the latent state is the variance $v_t$. In the latent neural SDE, the latent state $Z_t \in \mathbb{R}^p$ is learned from data. The KL divergence between the posterior and prior SDEs takes the Girsanov form

$$
D_{\text{KL}}(q \| p) = \frac{1}{2}\mathbb{E}_q\left[\int_0^T \left\|\sigma^{-1}(\tilde{\mu}_\lambda - \mu_\theta)\right\|^2 dt\right]
$$

Explain why this penalizes the posterior drift $\tilde{\mu}_\lambda$ for deviating from the prior drift $\mu_\theta$, acting as a regularizer on the latent dynamics.

??? success "Solution to Exercise 5"
    **Connection to classical stochastic volatility.**

    In the Heston model, the latent state is the variance $v_t$ satisfying $dv_t = \kappa(\bar{v} - v_t)dt + \xi\sqrt{v_t} \, dW_t^v$. This has a fixed parametric form: mean-reverting, square-root diffusion, with 3 parameters $(\kappa, \bar{v}, \xi)$.

    In the latent neural SDE, the latent state $Z_t \in \mathbb{R}^p$ (with $p$ possibly greater than 1) satisfies:

    $$
    dZ_t = \mu_\theta(t, Z_t) \, dt + \sigma_\phi(t, Z_t) \, dW_t
    $$

    where the drift and diffusion are neural networks. This is a nonparametric generalization:

    - The dimension $p$ of the latent space is a hyperparameter (Heston uses $p = 1$).
    - The drift $\mu_\theta$ can capture any mean-reversion structure (not just linear).
    - The diffusion $\sigma_\phi$ can be any positive function (not restricted to square-root).
    - Multiple latent factors can interact nonlinearly.

    **KL divergence as regularizer.**

    The training uses variational inference with the ELBO:

    $$
    \text{ELBO} = \mathbb{E}_q[\log p_\psi(X_{0:T} \mid Z_{0:T})] - D_{\text{KL}}(q_\lambda \| p_{\theta,\phi})
    $$

    The KL divergence between two SDEs with the same diffusion $\sigma_\phi$ is:

    $$
    D_{\text{KL}}(q \| p) = \frac{1}{2}\mathbb{E}_q\!\left[\int_0^T \|\sigma^{-1}(\tilde{\mu}_\lambda - \mu_\theta)\|^2 \, dt\right]
    $$

    This penalizes the posterior drift $\tilde{\mu}_\lambda$ for deviating from the prior drift $\mu_\theta$. The interpretation is:

    - The prior SDE (with drift $\mu_\theta$) represents the model's unconditional belief about how the latent state evolves.
    - The posterior SDE (with drift $\tilde{\mu}_\lambda$) represents the latent dynamics conditioned on observed data.
    - The KL term measures how much the data-informed dynamics differ from the prior. A large deviation means the posterior is "surprised" by the data.

    **Regularization effect:** Without the KL term, the posterior could fit any latent trajectory, leading to overfitting. The KL penalty forces the posterior to stay close to the prior, acting as Occam's razor: it prefers latent dynamics that are explained by the prior model, only allowing deviations when strongly supported by data.

    The factor $\sigma^{-1}$ means that drift deviations are penalized more strongly in directions where diffusion is small (low noise). When noise is large, the prior and posterior naturally differ more (there is more room for the drift to vary without affecting the path distribution), so less penalty is imposed. This is the natural information-theoretic weighting from Girsanov's theorem.

---

**Exercise 6.** A neural SDE is calibrated to fit the implied volatility surface by minimizing $\sum_i w_i|V_{\text{market}}^{(i)} - V_{\theta,\phi}^{(i)}|^2$. The model prices $V_{\theta,\phi}^{(i)}$ are computed by Monte Carlo simulation of the neural SDE. Discuss the computational challenges: (a) the loss gradient requires differentiating through the Monte Carlo simulation, (b) the variance of the Monte Carlo estimator affects gradient quality. How do techniques like reparameterization (pathwise gradients) and variance reduction help?

??? success "Solution to Exercise 6"
    **(a) Differentiating through Monte Carlo.**

    The model prices are:

    $$
    V_{\theta,\phi}^{(i)} = e^{-rT} \frac{1}{M}\sum_{m=1}^M h^{(i)}(S_T^{(m)})
    $$

    where $S_T^{(m)}$ depends on $(\theta, \phi)$ through the neural SDE simulation. To compute $\partial V / \partial \theta$, we must differentiate through the entire simulation path:

    $$
    \frac{\partial V}{\partial \theta} = e^{-rT} \frac{1}{M}\sum_m \frac{\partial h}{\partial S_T^{(m)}} \cdot \frac{\partial S_T^{(m)}}{\partial \theta}
    $$

    The term $\partial S_T^{(m)}/\partial \theta$ involves backpropagation through $N$ Euler-Maruyama steps, each containing a neural network evaluation. This is computationally expensive (cost proportional to $N \times \text{network cost}$) and memory-intensive (must store all intermediate states or use adjoint methods).

    **(b) Variance of Monte Carlo gradient.**

    The gradient $\nabla_\theta V$ is estimated by averaging over $M$ paths. The variance of this estimator is $O(1/M)$, but the *variance of the gradient estimator* (not just the price estimator) can be much higher because:

    - The payoff function $h$ may have discontinuities (e.g., digital options) or kinks (vanilla options at the strike), causing high gradient variance.
    - The gradient $\partial S_T^{(m)}/\partial \theta$ accumulates over $N$ time steps and can have high variance due to the multiplicative structure of the SDE.

    **Reparameterization (pathwise gradients):**

    The key technique is to separate the randomness from the parameters. Instead of sampling $S_T \sim p_{\theta,\phi}$, write:

    $$
    S_T = F_{\theta,\phi}(\epsilon), \quad \epsilon \sim \mathcal{N}(0, I)
    $$

    where $F$ is the deterministic transformation of the noise through the Euler scheme. Then:

    $$
    \frac{\partial}{\partial \theta} \mathbb{E}[h(S_T)] = \mathbb{E}\!\left[\frac{\partial h}{\partial S_T} \cdot \frac{\partial F_{\theta,\phi}}{\partial \theta}(\epsilon)\right]
    $$

    This pathwise gradient estimator has lower variance than the score function (REINFORCE) estimator because it uses the sensitivity of the path to the parameters rather than the score of the density.

    **Variance reduction techniques:**

    - *Antithetic variates:* For each noise sample $\epsilon$, also simulate with $-\epsilon$. The two paths are negatively correlated, reducing variance.
    - *Control variates:* Use a known baseline (e.g., Black-Scholes price with constant $\sigma$) to reduce variance: $V - V_{\text{BS}} + V_{\text{BS}}^{\text{exact}}$.
    - *Importance sampling:* Shift the simulation measure to concentrate paths near the important region (e.g., near the money).
    - *Gradient clipping:* Clip large gradient values to reduce the impact of outlier paths, at the cost of introducing small bias.

---

**Exercise 7.** Compare neural SDEs to classical parametric models (Black-Scholes, Heston, SABR) on three criteria: (a) flexibility to fit the volatility surface, (b) interpretability of model parameters, and (c) out-of-sample stability. Argue that neural SDEs offer superior fit but potentially worse interpretability and stability. Propose a hybrid approach that combines parametric structure with neural network corrections, and explain how this might achieve the benefits of both.

??? success "Solution to Exercise 7"
    **(a) Flexibility to fit the volatility surface.**

    - *Black-Scholes:* Constant volatility -- cannot fit any smile or skew. One parameter ($\sigma$) for the entire surface. Fails immediately for real market data.
    - *Heston:* Five parameters ($v_0, \kappa, \bar{v}, \xi, \rho$). Can produce a reasonable skew and term structure, but often struggles to fit short-maturity smiles and wings simultaneously.
    - *SABR:* Four parameters ($\alpha, \beta, \rho, \nu$) per maturity. Fits individual smiles well but requires separate calibration for each expiry, with no guaranteed consistency across maturities.
    - *Neural SDE:* The drift and diffusion have thousands of parameters. Can fit the entire implied volatility surface to machine precision, including complex term structures, steep skews, and wing behavior. **Superior flexibility.**

    **(b) Interpretability.**

    - *Black-Scholes:* $\sigma$ directly represents volatility. Fully interpretable.
    - *Heston:* Each parameter has clear meaning: $\kappa$ = mean reversion speed, $\bar{v}$ = long-run variance, $\xi$ = vol-of-vol, $\rho$ = leverage. Traders and risk managers can reason about parameter changes.
    - *SABR:* $\alpha$ = ATM vol, $\beta$ = backbone, $\rho$ = skew, $\nu$ = smile curvature. Well-understood by practitioners.
    - *Neural SDE:* Parameters are weights and biases of neural networks. No individual parameter has financial meaning. The drift and diffusion functions can be evaluated and plotted, but understanding *why* the model produces a particular feature requires post-hoc analysis. **Worst interpretability.**

    **(c) Out-of-sample stability.**

    - *Parametric models:* Few parameters provide strong regularization. Calibrated parameters are relatively stable across days. Extrapolation behavior is determined by the functional form, which is designed with financial constraints in mind (e.g., Heston produces a term structure of skew that flattens with maturity, consistent with theory).
    - *Neural SDE:* Many parameters can lead to overfitting the current day's surface. Small changes in input data can cause large changes in the learned dynamics. Extrapolation outside the training domain is unreliable because neural networks have no built-in financial structure. Recalibrating daily may produce unstable hedging strategies. **Potentially worst stability.**

    **Hybrid approach: parametric backbone with neural corrections.**

    Define:

    $$
    dS_t = \mu_{\text{Heston}}(t, S_t, v_t) \, dt + \sigma_{\text{Heston}}(t, S_t, v_t) \, dW_t^S + \epsilon_\theta(t, S_t, v_t) \, dt + \eta_\phi(t, S_t, v_t) \, dW_t^S
    $$

    $$
    dv_t = \kappa(\bar{v} - v_t) \, dt + \xi\sqrt{v_t} \, dW_t^v + \alpha_\theta(t, v_t) \, dt + \beta_\phi(t, v_t) \, dW_t^v
    $$

    where $\epsilon_\theta, \eta_\phi, \alpha_\theta, \beta_\phi$ are small neural network corrections.

    **Benefits:**

    - The Heston backbone provides structure, interpretability, and stability. The 5 Heston parameters retain their financial meaning.
    - The neural corrections capture residual misspecification: features of the volatility surface that Heston cannot match (e.g., short-maturity smile shape, steep wing behavior).
    - Regularize the corrections (e.g., $L^2$ penalty on $\epsilon, \eta, \alpha, \beta$) so that they remain small perturbations. This ensures that the model stays close to Heston, with stability guarantees.
    - Out-of-sample: in regions without data, the corrections shrink to zero (via regularization), and the model reverts to the well-understood Heston dynamics.
    - Calibration: first calibrate the Heston parameters to get a good initial fit, then train the neural corrections on the residuals. This staged approach is more stable than end-to-end neural SDE training.
