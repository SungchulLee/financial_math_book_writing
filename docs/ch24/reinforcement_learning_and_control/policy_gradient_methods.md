# Policy Gradient Methods

**Policy gradient methods** directly parameterize the policy $\pi_\theta(a \mid s)$ and optimize it by gradient ascent on expected cumulative reward. Unlike value-based methods (Q-learning, dynamic programming) that first estimate value functions and derive policies indirectly, policy gradient methods search the policy space directly. This is particularly advantageous for financial applications with continuous action spaces---portfolio weights, trade sizes, hedge ratios---where discretizing the action space is impractical.

---

## Policy Gradient Theorem

### Setup

Consider a Markov decision process with state space $\mathcal{S}$, action space $\mathcal{A}$, transition kernel $P(s' \mid s, a)$, reward function $r(s, a)$, and discount factor $\gamma \in (0,1]$. A **stochastic policy** $\pi_\theta(a \mid s)$ is parameterized by $\theta \in \mathbb{R}^p$.

The objective is to maximize the expected discounted return:

$$
J(\theta) = \mathbb{E}_{\pi_\theta}\!\left[\sum_{t=0}^{\infty} \gamma^t r(s_t, a_t)\right] = \mathbb{E}_{s_0 \sim d_0}\!\left[V^{\pi_\theta}(s_0)\right]
$$

where $d_0$ is the initial state distribution and $V^{\pi}(s) = \mathbb{E}_\pi[\sum_{t=0}^\infty \gamma^t r(s_t, a_t) \mid s_0 = s]$.

### The Theorem

**Theorem (Policy Gradient Theorem -- Sutton et al. 1999).** Under standard regularity conditions, the gradient of $J(\theta)$ with respect to $\theta$ is:

$$
\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta}\!\left[\sum_{t=0}^{\infty} \gamma^t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \, Q^{\pi_\theta}(s_t, a_t)\right]
$$

Equivalently, using the discounted state visitation distribution $d^{\pi_\theta}(s) = (1 - \gamma)\sum_{t=0}^\infty \gamma^t P(s_t = s \mid \pi_\theta)$:

$$
\nabla_\theta J(\theta) = \frac{1}{1 - \gamma}\mathbb{E}_{s \sim d^{\pi_\theta}, \, a \sim \pi_\theta(\cdot|s)}\!\left[\nabla_\theta \log \pi_\theta(a \mid s) \, Q^{\pi_\theta}(s, a)\right]
$$

### Proof

We prove the result for the finite-horizon case. Starting from:

$$
\nabla_\theta V^{\pi_\theta}(s) = \nabla_\theta \left[\sum_a \pi_\theta(a \mid s) \, Q^{\pi_\theta}(s, a)\right]
$$

By the product rule:

$$
= \sum_a \left[\nabla_\theta \pi_\theta(a \mid s) \, Q^{\pi_\theta}(s, a) + \pi_\theta(a \mid s) \, \nabla_\theta Q^{\pi_\theta}(s, a)\right]
$$

Now expand $Q^{\pi_\theta}(s,a) = r(s,a) + \gamma \sum_{s'} P(s' \mid s,a) V^{\pi_\theta}(s')$, so:

$$
\nabla_\theta Q^{\pi_\theta}(s, a) = \gamma \sum_{s'} P(s' \mid s, a) \nabla_\theta V^{\pi_\theta}(s')
$$

Substituting back and unrolling the recursion over $t = 0, 1, 2, \ldots$ yields:

$$
\nabla_\theta J(\theta) = \sum_{t=0}^{\infty} \gamma^t \sum_s P(s_t = s \mid \pi_\theta) \sum_a \nabla_\theta \pi_\theta(a \mid s) \, Q^{\pi_\theta}(s, a)
$$

Using the log-derivative trick $\nabla_\theta \pi_\theta = \pi_\theta \nabla_\theta \log \pi_\theta$:

$$
= \mathbb{E}_{\pi_\theta}\!\left[\sum_{t=0}^{\infty} \gamma^t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \, Q^{\pi_\theta}(s_t, a_t)\right]
$$

$\square$

!!! note "The Log-Derivative Trick"
    The identity $\nabla_\theta \pi_\theta(a \mid s) = \pi_\theta(a \mid s) \nabla_\theta \log \pi_\theta(a \mid s)$ converts the gradient of an expectation into an expectation of a gradient, enabling Monte Carlo estimation without knowing the transition dynamics.

---

## REINFORCE Algorithm

The simplest policy gradient method estimates $\nabla_\theta J$ using a single trajectory.

**Algorithm (REINFORCE -- Williams 1992).**

1. Sample trajectory $\tau = (s_0, a_0, r_0, s_1, a_1, r_1, \ldots)$ under $\pi_\theta$
2. Compute returns $G_t = \sum_{k=0}^{T-t-1} \gamma^k r_{t+k}$
3. Update: $\theta \leftarrow \theta + \alpha \sum_{t=0}^{T-1} \gamma^t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \, G_t$

The estimator $\hat{g} = \sum_t \gamma^t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \, G_t$ is an unbiased estimate of $\nabla_\theta J(\theta)$.

**Proposition (Unbiasedness).** $\mathbb{E}_{\pi_\theta}[\hat{g}] = \nabla_\theta J(\theta)$.

This follows from the policy gradient theorem and the fact that $\mathbb{E}[G_t \mid s_t, a_t] = Q^{\pi_\theta}(s_t, a_t)$.

### Variance Reduction via Baselines

**Theorem (Baseline Invariance).** For any function $b(s)$ independent of action $a$:

$$
\mathbb{E}_{a \sim \pi_\theta}\!\left[\nabla_\theta \log \pi_\theta(a \mid s) \, b(s)\right] = b(s) \, \nabla_\theta \underbrace{\sum_a \pi_\theta(a \mid s)}_{= 1} = 0
$$

Therefore, subtracting a **baseline** $b(s_t)$ from $G_t$ does not introduce bias:

$$
\hat{g}_b = \sum_{t=0}^{T-1} \gamma^t \nabla_\theta \log \pi_\theta(a_t \mid s_t)(G_t - b(s_t))
$$

The optimal baseline (minimizing variance) is approximately $b^*(s) \approx V^{\pi_\theta}(s)$, the value function.

---

## Actor-Critic Methods

Actor-critic methods combine policy gradient updates (the **actor**) with value function estimation (the **critic**), using the estimated value function as the baseline.

### Architecture

- **Actor:** Policy network $\pi_\theta(a \mid s)$ with parameters $\theta$
- **Critic:** Value network $\hat{V}_w(s)$ with parameters $w$

### The Advantage Function

**Definition (Advantage Function).**

$$
A^{\pi}(s, a) = Q^{\pi}(s, a) - V^{\pi}(s)
$$

The advantage measures how much better action $a$ is compared to the average action under $\pi$. Using the advantage in the policy gradient:

$$
\nabla_\theta J(\theta) = \mathbb{E}_{\pi_\theta}\!\left[\sum_{t=0}^{\infty} \gamma^t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \, A^{\pi_\theta}(s_t, a_t)\right]
$$

reduces variance since $\mathbb{E}_a[A^{\pi}(s,a)] = 0$.

### Temporal Difference Estimation

The advantage can be estimated using the **TD error**:

$$
\hat{A}_t = r_t + \gamma \hat{V}_w(s_{t+1}) - \hat{V}_w(s_t)
$$

This is a one-step estimate. Multi-step estimates and their combination lead to **Generalized Advantage Estimation**.

### Generalized Advantage Estimation (GAE)

**Definition (GAE -- Schulman et al. 2016).** The GAE with parameter $\lambda \in [0,1]$ is:

$$
\hat{A}_t^{\text{GAE}(\gamma,\lambda)} = \sum_{k=0}^{\infty} (\gamma\lambda)^k \delta_{t+k}
$$

where $\delta_t = r_t + \gamma \hat{V}_w(s_{t+1}) - \hat{V}_w(s_t)$ is the TD error.

This interpolates between:

- $\lambda = 0$: One-step TD estimate $\hat{A}_t = \delta_t$ (low variance, high bias)
- $\lambda = 1$: Monte Carlo estimate (high variance, low bias)

---

## Continuous Action Spaces for Finance

### Gaussian Policies

For continuous actions (e.g., portfolio weights $a \in \mathbb{R}^d$), a common choice is a Gaussian policy:

$$
\pi_\theta(a \mid s) = \mathcal{N}\!\left(a \;\middle|\; \mu_\theta(s), \Sigma_\theta(s)\right)
$$

where $\mu_\theta(s)$ and $\Sigma_\theta(s)$ are neural network outputs. The log-probability gradient is:

$$
\nabla_\theta \log \pi_\theta(a \mid s) = \nabla_\theta \mu_\theta^\top \Sigma_\theta^{-1}(a - \mu_\theta) + \text{terms from } \nabla_\theta \Sigma_\theta
$$

### Portfolio Allocation Policy

For portfolio allocation with $d$ assets and a constraint $\sum_i a_i = 1$, $a_i \geq 0$, the policy outputs a softmax:

$$
a_i = \frac{e^{z_i(\theta, s)}}{\sum_j e^{z_j(\theta, s)}}
$$

where $z(\theta, s) \in \mathbb{R}^d$ is the network output. This naturally satisfies the simplex constraint.

### Deterministic Policy Gradient

**Theorem (Deterministic Policy Gradient -- Silver et al. 2014).** For deterministic policies $a = \mu_\theta(s)$:

$$
\nabla_\theta J(\theta) = \mathbb{E}_{s \sim d^{\mu_\theta}}\!\left[\nabla_\theta \mu_\theta(s) \, \nabla_a Q^{\mu_\theta}(s, a)\big|_{a = \mu_\theta(s)}\right]
$$

This requires a differentiable Q-function estimate (the critic). The **Deep Deterministic Policy Gradient (DDPG)** algorithm implements this using neural network function approximation for both the actor and critic.

---

## Proximal Policy Optimization (PPO)

Large policy updates can destabilize training. PPO constrains the update size.

**Definition (PPO Objective -- Schulman et al. 2017).** Define the probability ratio:

$$
r_t(\theta) = \frac{\pi_\theta(a_t \mid s_t)}{\pi_{\theta_{\text{old}}}(a_t \mid s_t)}
$$

The clipped surrogate objective is:

$$
\mathcal{L}^{\text{CLIP}}(\theta) = \mathbb{E}_t\!\left[\min\!\left(r_t(\theta)\hat{A}_t, \; \operatorname{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t\right)\right]
$$

where $\epsilon \approx 0.2$. The clipping prevents the ratio from moving too far from 1, ensuring small policy updates.

PPO is widely used in financial RL due to its stability and ease of implementation.

---

## Financial Applications

### Risk-Sensitive Policy Gradient

Standard policy gradients maximize expected return. For finance, **risk-sensitive** objectives are essential:

$$
J_{\text{risk}}(\theta) = \mathbb{E}_{\pi_\theta}\!\left[\sum_t \gamma^t r_t\right] - \lambda \, \text{Var}_{\pi_\theta}\!\left[\sum_t \gamma^t r_t\right]
$$

The gradient involves additional terms from the variance:

$$
\nabla_\theta J_{\text{risk}} = \nabla_\theta J - 2\lambda \, \text{Cov}_{\pi_\theta}\!\left[\sum_t \gamma^t r_t, \; \sum_t \gamma^t \nabla_\theta \log \pi_\theta(a_t \mid s_t) \sum_{k \geq t} \gamma^{k-t} r_k\right]
$$

### Convergence Considerations

**Theorem (Policy Gradient Convergence).** Under standard assumptions (bounded rewards, Lipschitz policy gradients), REINFORCE with appropriate step sizes $\alpha_k$ satisfying $\sum \alpha_k = \infty$, $\sum \alpha_k^2 < \infty$ converges to a stationary point of $J(\theta)$.

For the actor-critic with compatible function approximation (the critic's feature vector equals $\nabla_\theta \log \pi_\theta$), convergence to a local optimum is guaranteed under additional regularity conditions.

!!! warning "Local Optima"
    Policy gradient methods converge to **local** optima, not global ones. The policy landscape in financial problems (portfolio optimization, hedging) can have many local optima. Multiple random restarts and careful initialization are essential.

---

## Key Takeaways

1. The **policy gradient theorem** provides a model-free formula for the gradient of expected return with respect to policy parameters.

2. **REINFORCE** is unbiased but high-variance; **baselines** and **actor-critic** methods reduce variance at the cost of some bias.

3. **Generalized Advantage Estimation** interpolates between bias and variance via the parameter $\lambda$.

4. **Continuous action spaces** for portfolio allocation and trade sizing are handled naturally through Gaussian or softmax policies.

5. **PPO** stabilizes training through clipped surrogate objectives, making it practical for financial RL applications.

---

## Further Reading

- Sutton, McAllester, Singh & Mansour (1999), "Policy Gradient Methods for RL with Function Approximation"
- Williams (1992), "Simple Statistical Gradient-Following Algorithms for Connectionist RL"
- Schulman, Moritz, Levine, Jordan & Abbeel (2016), "High-Dimensional Continuous Control Using GAE"
- Schulman, Wolski, Dhariwal, Radford & Klimov (2017), "Proximal Policy Optimization Algorithms"
- Silver, Lever, Heess et al. (2014), "Deterministic Policy Gradient Algorithms"

---

## Exercises

**Exercise 1.** For a Gaussian policy $\pi_\theta(a|s) = \mathcal{N}(a; \mu_\theta(s), \sigma^2)$ with fixed variance $\sigma^2$, compute the score function $\nabla_\theta \log \pi_\theta(a|s) = \frac{a - \mu_\theta(s)}{\sigma^2} \nabla_\theta \mu_\theta(s)$. (a) If $\mu_\theta(s) = \theta^\top s$ is linear with $s = (1, S_t/K, (T-t)/T)^\top \in \mathbb{R}^3$ and $\theta \in \mathbb{R}^3$, compute $\nabla_\theta \log \pi_\theta(a|s)$ explicitly. (b) For a single trajectory with $s_0 = (1, 1.05, 0.9)$, $a_0 = 0.6$ (hedge ratio), $G_0 = -0.03$ (P&L), and $\sigma = 0.1$, compute the REINFORCE gradient estimate. (c) Explain why the gradient pushes $\mu_\theta$ toward $a_0$ when $G_0 > 0$ and away when $G_0 < 0$.

---

**Exercise 2.** The baseline invariance theorem states that subtracting any state-dependent baseline $b(s)$ from the return does not introduce bias: $\mathbb{E}_{a \sim \pi_\theta}[\nabla_\theta \log \pi_\theta(a|s) \cdot b(s)] = 0$. (a) Prove this by showing that $\sum_a \nabla_\theta \pi_\theta(a|s) = \nabla_\theta 1 = 0$. (b) The optimal baseline is $b^*(s) = \frac{\mathbb{E}[(\nabla_\theta \log \pi)^2 G]}{\mathbb{E}[(\nabla_\theta \log \pi)^2]}$. Explain why this is approximately $V^\pi(s)$. (c) In a hedging application, the value function baseline reduces gradient variance dramatically. Numerically, if REINFORCE without baseline has gradient variance 100 and with baseline it has variance 5, how many more trajectories would be needed without the baseline to achieve the same estimation accuracy?

---

**Exercise 3.** Generalized Advantage Estimation (GAE) with parameter $\lambda$ computes $\hat{A}_t^{\text{GAE}} = \sum_{k=0}^\infty (\gamma\lambda)^k \delta_{t+k}$ where $\delta_t = r_t + \gamma \hat{V}(s_{t+1}) - \hat{V}(s_t)$. Consider a 3-step hedging episode with $r_0 = -0.01$, $r_1 = 0.02$, $r_2 = -0.03$, $\hat{V}(s_0) = 0.05$, $\hat{V}(s_1) = 0.04$, $\hat{V}(s_2) = 0.06$, $\hat{V}(s_3) = 0$ (terminal), $\gamma = 1$. (a) Compute $\delta_0, \delta_1, \delta_2$. (b) Compute $\hat{A}_0^{\text{GAE}}$ for $\lambda = 0$ (one-step TD) and $\lambda = 1$ (Monte Carlo). (c) For $\lambda = 0.95$, compute $\hat{A}_0^{\text{GAE}}$ and explain why this intermediate value balances bias and variance.

---

**Exercise 4.** The PPO clipped objective is $\mathcal{L}^{\text{CLIP}} = \mathbb{E}_t[\min(r_t(\theta)\hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t)]$ where $r_t(\theta) = \pi_\theta(a_t|s_t) / \pi_{\theta_{\text{old}}}(a_t|s_t)$. (a) If $\hat{A}_t > 0$ (the action was better than average), show that the objective encourages increasing $\pi_\theta(a_t|s_t)$ but clips the increase at $r_t = 1 + \epsilon$. (b) If $\hat{A}_t < 0$, show that the objective encourages decreasing $\pi_\theta(a_t|s_t)$ but clips at $r_t = 1 - \epsilon$. (c) For $\epsilon = 0.2$, the probability ratio is constrained to $[0.8, 1.2]$. Explain why this prevents catastrophic policy updates that are particularly dangerous in financial applications.

---

**Exercise 5.** A portfolio allocation agent uses a softmax policy: $a_i = e^{z_i(\theta, s)} / \sum_j e^{z_j(\theta, s)}$ for $d = 5$ assets, where $z(\theta, s)$ is a neural network output. (a) Verify that $\sum_i a_i = 1$ and $a_i > 0$, satisfying the simplex constraint for long-only portfolios. (b) Compute $\partial a_i / \partial z_j = a_i(\mathbf{1}_{i=j} - a_j)$ (the softmax Jacobian). (c) If the risk-sensitive objective is $J = \mathbb{E}[R_p] - \frac{\lambda}{2}\text{Var}[R_p]$ where $R_p = \sum_i a_i R_i$, describe how the policy gradient $\nabla_\theta J$ involves both the mean and variance of the portfolio return. (d) Discuss why the softmax parameterization prevents short-selling, and how you would modify it to allow short positions.

---

**Exercise 6.** The deterministic policy gradient theorem states $\nabla_\theta J = \mathbb{E}_s[\nabla_\theta \mu_\theta(s) \nabla_a Q^{\mu_\theta}(s,a)|_{a=\mu_\theta(s)}]$. (a) Explain why this requires a differentiable Q-function (the critic) but not a stochastic policy. (b) In DDPG for optimal execution, the actor outputs the trade size $a = \mu_\theta(s)$ and the critic estimates $Q_w(s,a)$. The actor is updated by backpropagating through the critic: $\nabla_\theta J \approx \nabla_\theta \mu_\theta \cdot \nabla_a Q_w$. Explain this chain rule. (c) Discuss the advantage of deterministic policies for financial applications: they produce the same action in the same state, which is important for reproducibility and risk management.

---

**Exercise 7.** Policy gradient methods converge to local optima, not global ones. (a) For a portfolio optimization problem with 10 assets, the policy landscape may have many local optima. Propose strategies to find good solutions: multiple random restarts, curriculum learning (start with simpler problems), warm-starting from known heuristics (e.g., initialize near the minimum-variance portfolio). (b) Discuss validation: how do you assess whether the learned policy is close to the global optimum? Compare with known analytical solutions when available (e.g., Merton portfolio for simple cases). (c) In practice, a policy that achieves 90% of the theoretically optimal Sharpe ratio may be acceptable if it is robust and stable. Argue that robustness (small policy changes $\to$ small performance changes) is more important than optimality in financial deployment.
