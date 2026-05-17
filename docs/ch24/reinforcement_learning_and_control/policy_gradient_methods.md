# Policy Gradient Methods

**Policy gradient methods** directly parameterize the policy $\pi_\theta(a \mid s)$ and optimize it by gradient ascent on expected cumulative reward. Unlike value-based methods (Q-learning, dynamic programming) that first estimate value functions and derive policies indirectly, policy gradient methods search the policy space directly. This is particularly advantageous for financial applications with continuous action spaces---portfolio weights, trade sizes, hedge ratios---where discretizing the action space is impractical.

---

## Policy Gradient Theorem

### Setup

Recall (see [§ Definition of an MDP](markov_decision_processes.md#definition-of-an-mdp)) the MDP tuple $(\mathcal{S}, \mathcal{A}, P, r, \gamma)$. A **stochastic policy** $\pi_\theta(a \mid s)$ is parameterized by $\theta \in \mathbb{R}^p$.

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

??? success "Solution to Exercise 1"
    **(a) Score function for linear Gaussian policy.**

    For $\pi_\theta(a|s) = \mathcal{N}(a; \mu_\theta(s), \sigma^2)$ with $\mu_\theta(s) = \theta^\top s$ and $s = (1, S_t/K, (T-t)/T)^\top$:

    $$
    \log \pi_\theta(a|s) = -\frac{1}{2}\log(2\pi\sigma^2) - \frac{(a - \theta^\top s)^2}{2\sigma^2}
    $$

    The score function is:

    $$
    \nabla_\theta \log \pi_\theta(a|s) = \frac{a - \theta^\top s}{\sigma^2} \nabla_\theta(\theta^\top s) = \frac{a - \theta^\top s}{\sigma^2} \, s
    $$

    Explicitly, with $s = (1, S_t/K, (T-t)/T)^\top \in \mathbb{R}^3$:

    $$
    \nabla_\theta \log \pi_\theta(a|s) = \frac{a - \theta^\top s}{\sigma^2} \begin{pmatrix} 1 \\ S_t/K \\ (T-t)/T \end{pmatrix}
    $$

    This is a vector in $\mathbb{R}^3$, proportional to the state vector $s$ and scaled by the "action surprise" $(a - \mu_\theta(s))/\sigma^2$.

    **(b) REINFORCE gradient estimate.**

    Given $s_0 = (1, 1.05, 0.9)^\top$, $a_0 = 0.6$, $G_0 = -0.03$, $\sigma = 0.1$, and $\sigma^2 = 0.01$.

    First, compute $\mu_\theta(s_0) = \theta^\top s_0$. We need $\theta$; assuming an initial $\theta = (0, 0, 0)^\top$ (or any given value). For a concrete computation, let us assume $\theta$ is such that $\mu_\theta(s_0) = 0.5$ (a plausible initial hedge ratio).

    The score at $(s_0, a_0)$:

    $$
    \nabla_\theta \log \pi_\theta(a_0|s_0) = \frac{0.6 - 0.5}{0.01} \begin{pmatrix} 1 \\ 1.05 \\ 0.9 \end{pmatrix} = 10 \begin{pmatrix} 1 \\ 1.05 \\ 0.9 \end{pmatrix} = \begin{pmatrix} 10 \\ 10.5 \\ 9.0 \end{pmatrix}
    $$

    The REINFORCE gradient estimate (single trajectory, single time step):

    $$
    \hat{g} = \nabla_\theta \log \pi_\theta(a_0|s_0) \cdot G_0 = (-0.03) \begin{pmatrix} 10 \\ 10.5 \\ 9.0 \end{pmatrix} = \begin{pmatrix} -0.30 \\ -0.315 \\ -0.27 \end{pmatrix}
    $$

    The update direction is $\theta \leftarrow \theta + \alpha \hat{g}$, which would decrease $\theta$ (and hence decrease $\mu_\theta(s_0)$, moving the mean away from $a_0 = 0.6$).

    **(c) Gradient direction interpretation.**

    The REINFORCE gradient is $\hat{g} = G_0 \cdot \frac{a_0 - \mu_\theta(s_0)}{\sigma^2} \, s_0$. The update $\theta \leftarrow \theta + \alpha \hat{g}$ changes $\mu_\theta(s)$ in the direction of $s^\top s_0 \cdot (a_0 - \mu_\theta) \cdot G_0$:

    - **If $G_0 > 0$** (positive return, good outcome): The gradient pushes $\mu_\theta(s_0)$ toward $a_0$. The agent learned that this action led to a good outcome, so the policy should make this action more likely.
    - **If $G_0 < 0$** (negative return, bad outcome): The gradient pushes $\mu_\theta(s_0)$ away from $a_0$. The agent learned that this action led to a bad outcome, so the policy should make this action less likely.

    In our example, $G_0 = -0.03 < 0$ and $a_0 > \mu_\theta$, so the gradient decreases $\theta$, which decreases $\mu_\theta$ and moves it further from $a_0 = 0.6$. The agent is learning that hedging with ratio 0.6 in this state led to a loss, so it should reduce the hedge ratio.

---

**Exercise 2.** The baseline invariance theorem states that subtracting any state-dependent baseline $b(s)$ from the return does not introduce bias: $\mathbb{E}_{a \sim \pi_\theta}[\nabla_\theta \log \pi_\theta(a|s) \cdot b(s)] = 0$. (a) Prove this by showing that $\sum_a \nabla_\theta \pi_\theta(a|s) = \nabla_\theta 1 = 0$. (b) The optimal baseline is $b^*(s) = \frac{\mathbb{E}[(\nabla_\theta \log \pi)^2 G]}{\mathbb{E}[(\nabla_\theta \log \pi)^2]}$. Explain why this is approximately $V^\pi(s)$. (c) In a hedging application, the value function baseline reduces gradient variance dramatically. Numerically, if REINFORCE without baseline has gradient variance 100 and with baseline it has variance 5, how many more trajectories would be needed without the baseline to achieve the same estimation accuracy?

??? success "Solution to Exercise 2"
    **(a) Proof of baseline invariance.**

    For any function $b(s)$ independent of $a$:

    $$
    \mathbb{E}_{a \sim \pi_\theta(\cdot|s)}\!\left[\nabla_\theta \log \pi_\theta(a|s) \cdot b(s)\right] = b(s) \sum_a \nabla_\theta \pi_\theta(a|s)
    $$

    where we used the log-derivative trick: $\nabla_\theta \log \pi_\theta(a|s) \cdot \pi_\theta(a|s) = \nabla_\theta \pi_\theta(a|s)$.

    Now:

    $$
    \sum_a \nabla_\theta \pi_\theta(a|s) = \nabla_\theta \sum_a \pi_\theta(a|s) = \nabla_\theta 1 = 0
    $$

    since $\pi_\theta(\cdot|s)$ is a probability distribution that sums to 1 for all $\theta$. Therefore:

    $$
    \mathbb{E}_{a \sim \pi_\theta}\!\left[\nabla_\theta \log \pi_\theta(a|s) \cdot b(s)\right] = b(s) \cdot 0 = 0 \quad \square
    $$

    For continuous actions, replace $\sum_a$ with $\int da$ and the same argument holds since $\int \pi_\theta(a|s) da = 1$ for all $\theta$.

    **(b) Optimal baseline approximation.**

    The optimal baseline minimizes the variance of the gradient estimator $\hat{g} = \nabla_\theta \log \pi_\theta(a|s)(G - b(s))$. For a scalar parameter, the variance-minimizing baseline is:

    $$
    b^*(s) = \frac{\mathbb{E}_{a}\!\left[(\nabla_\theta \log \pi_\theta)^2 \cdot G \mid s\right]}{\mathbb{E}_{a}\!\left[(\nabla_\theta \log \pi_\theta)^2 \mid s\right]}
    $$

    This is a weighted average of $G$ where the weights are $(\nabla_\theta \log \pi_\theta)^2$. Since the weights are always positive and $\mathbb{E}[G | s, a] = Q^\pi(s, a)$:

    $$
    b^*(s) \approx \frac{\mathbb{E}[(\nabla_\theta \log \pi)^2 Q^\pi(s,a)]}{\mathbb{E}[(\nabla_\theta \log \pi)^2]} \approx \mathbb{E}_a[Q^\pi(s,a)] = V^\pi(s)
    $$

    The approximation is exact when $(\nabla_\theta \log \pi_\theta)^2$ is independent of $a$ (which holds approximately when the policy is nearly uniform) or when $Q^\pi(s,a) \approx V^\pi(s)$ for all $a$ (small advantage). In practice, $b(s) = V^\pi(s)$ is a near-optimal baseline.

    **(c) Trajectory requirement ratio.**

    The accuracy of a Monte Carlo estimate scales as $\text{standard error} \propto \sigma / \sqrt{M}$ where $\sigma$ is the standard deviation and $M$ is the number of samples (trajectories). To achieve the same standard error with different variances:

    $$
    \frac{\sigma_{\text{no baseline}}}{\sqrt{M_{\text{no baseline}}}} = \frac{\sigma_{\text{baseline}}}{\sqrt{M_{\text{baseline}}}}
    $$

    $$
    \frac{M_{\text{no baseline}}}{M_{\text{baseline}}} = \frac{\sigma_{\text{no baseline}}^2}{\sigma_{\text{baseline}}^2} = \frac{100}{5} = 20
    $$

    Without the baseline, **20 times more trajectories** are needed to achieve the same gradient estimation accuracy. This is a dramatic efficiency gain. In a hedging application where each trajectory requires simulating an entire option lifetime, reducing the sample requirement by a factor of 20 can mean the difference between a training run taking 1 hour versus 20 hours.

---

**Exercise 3.** Generalized Advantage Estimation (GAE) with parameter $\lambda$ computes $\hat{A}_t^{\text{GAE}} = \sum_{k=0}^\infty (\gamma\lambda)^k \delta_{t+k}$ where $\delta_t = r_t + \gamma \hat{V}(s_{t+1}) - \hat{V}(s_t)$. Consider a 3-step hedging episode with $r_0 = -0.01$, $r_1 = 0.02$, $r_2 = -0.03$, $\hat{V}(s_0) = 0.05$, $\hat{V}(s_1) = 0.04$, $\hat{V}(s_2) = 0.06$, $\hat{V}(s_3) = 0$ (terminal), $\gamma = 1$. (a) Compute $\delta_0, \delta_1, \delta_2$. (b) Compute $\hat{A}_0^{\text{GAE}}$ for $\lambda = 0$ (one-step TD) and $\lambda = 1$ (Monte Carlo). (c) For $\lambda = 0.95$, compute $\hat{A}_0^{\text{GAE}}$ and explain why this intermediate value balances bias and variance.

??? success "Solution to Exercise 3"
    **(a) TD errors.**

    With $\gamma = 1$:

    $$
    \delta_0 = r_0 + \gamma \hat{V}(s_1) - \hat{V}(s_0) = -0.01 + 1 \times 0.04 - 0.05 = -0.02
    $$

    $$
    \delta_1 = r_1 + \gamma \hat{V}(s_2) - \hat{V}(s_1) = 0.02 + 1 \times 0.06 - 0.04 = 0.04
    $$

    $$
    \delta_2 = r_2 + \gamma \hat{V}(s_3) - \hat{V}(s_2) = -0.03 + 1 \times 0 - 0.06 = -0.09
    $$

    **(b) GAE for $\lambda = 0$ and $\lambda = 1$.**

    **$\lambda = 0$ (one-step TD):**

    $$
    \hat{A}_0^{\text{GAE}(\gamma=1, \lambda=0)} = \delta_0 = -0.02
    $$

    This uses only the immediate TD error---low variance but potentially biased if $\hat{V}$ is inaccurate.

    **$\lambda = 1$ (Monte Carlo):**

    $$
    \hat{A}_0^{\text{GAE}(\gamma=1, \lambda=1)} = \delta_0 + \gamma\lambda \cdot \delta_1 + (\gamma\lambda)^2 \cdot \delta_2
    $$

    $$
    = -0.02 + 1 \times 0.04 + 1 \times (-0.09) = -0.07
    $$

    Verification: this should equal $G_0 - \hat{V}(s_0)$ where $G_0 = r_0 + r_1 + r_2 = -0.01 + 0.02 - 0.03 = -0.02$:

    $$
    G_0 - \hat{V}(s_0) = -0.02 - 0.05 = -0.07 \checkmark
    $$

    This is the full Monte Carlo advantage---no bias from $\hat{V}$ (except in the baseline), but higher variance since it depends on the entire trajectory.

    **(c) GAE for $\lambda = 0.95$.**

    $$
    \hat{A}_0^{\text{GAE}(\gamma=1, \lambda=0.95)} = \delta_0 + (0.95)\delta_1 + (0.95)^2 \delta_2
    $$

    $$
    = -0.02 + 0.95 \times 0.04 + 0.9025 \times (-0.09)
    $$

    $$
    = -0.02 + 0.038 - 0.08123 = -0.06323
    $$

    This intermediate value ($-0.0632$) lies between the one-step estimate ($-0.02$) and the Monte Carlo estimate ($-0.07$). The GAE with $\lambda = 0.95$ places most weight on nearby TD errors (which are less noisy due to bootstrapping from $\hat{V}$) while still incorporating information from later steps. The exponential decay $(\gamma\lambda)^k = 0.95^k$ means that $\delta_2$ receives weight $0.9025$ (only 10% less than $\delta_1$'s weight of $0.95$), so with $\lambda$ close to 1 the estimate is close to Monte Carlo. Reducing $\lambda$ would place more weight on $\delta_0$ and less on later (noisier) terms, trading off bias for variance.

---

**Exercise 4.** The PPO clipped objective is $\mathcal{L}^{\text{CLIP}} = \mathbb{E}_t[\min(r_t(\theta)\hat{A}_t, \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon)\hat{A}_t)]$ where $r_t(\theta) = \pi_\theta(a_t|s_t) / \pi_{\theta_{\text{old}}}(a_t|s_t)$. (a) If $\hat{A}_t > 0$ (the action was better than average), show that the objective encourages increasing $\pi_\theta(a_t|s_t)$ but clips the increase at $r_t = 1 + \epsilon$. (b) If $\hat{A}_t < 0$, show that the objective encourages decreasing $\pi_\theta(a_t|s_t)$ but clips at $r_t = 1 - \epsilon$. (c) For $\epsilon = 0.2$, the probability ratio is constrained to $[0.8, 1.2]$. Explain why this prevents catastrophic policy updates that are particularly dangerous in financial applications.

??? success "Solution to Exercise 4"
    **(a) Case $\hat{A}_t > 0$ (good action).**

    When $\hat{A}_t > 0$, the action was better than average. The unclipped objective for this sample is $r_t(\theta) \hat{A}_t$, which increases linearly with $r_t(\theta) = \pi_\theta(a_t|s_t)/\pi_{\theta_{\text{old}}}(a_t|s_t)$. The gradient encourages increasing $\pi_\theta(a_t|s_t)$.

    The clipped objective is:

    $$
    \mathcal{L}_t = \min\!\left(r_t(\theta) \hat{A}_t, \; \text{clip}(r_t(\theta), 1-\epsilon, 1+\epsilon) \hat{A}_t\right)
    $$

    Since $\hat{A}_t > 0$, both terms are increasing in $r_t$ (up to the clip). The clipped term caps at $(1+\epsilon)\hat{A}_t$ when $r_t \ge 1+\epsilon$. The minimum of the two is:

    - For $r_t \le 1+\epsilon$: $\mathcal{L}_t = r_t \hat{A}_t$ (both terms agree, gradient active)
    - For $r_t > 1+\epsilon$: $\mathcal{L}_t = (1+\epsilon)\hat{A}_t$ (flat, gradient is zero)

    Thus, the objective encourages increasing $\pi_\theta(a_t|s_t)$ but stops providing gradient once $r_t$ exceeds $1+\epsilon$, preventing overly large probability increases. $\square$

    **(b) Case $\hat{A}_t < 0$ (bad action).**

    When $\hat{A}_t < 0$, the action was worse than average. The unclipped objective $r_t \hat{A}_t$ is now decreasing in $r_t$ (since $\hat{A}_t < 0$), so the gradient encourages decreasing $r_t$ (i.e., decreasing $\pi_\theta(a_t|s_t)$).

    The clipped term: when $r_t < 1-\epsilon$, $\text{clip}(r_t, 1-\epsilon, 1+\epsilon) = 1-\epsilon$, so the clipped term is $(1-\epsilon)\hat{A}_t$ (constant). The minimum:

    - For $r_t \ge 1-\epsilon$: $\mathcal{L}_t = r_t \hat{A}_t$ (since $r_t \hat{A}_t \le (1-\epsilon)\hat{A}_t$ when $\hat{A}_t < 0$). Actually, since $\hat{A}_t < 0$ and $r_t \ge 1-\epsilon$: $r_t \hat{A}_t \le (1-\epsilon)\hat{A}_t$, so $\min = r_t \hat{A}_t$ (gradient active).
    - For $r_t < 1-\epsilon$: $r_t \hat{A}_t > (1-\epsilon)\hat{A}_t$ (since $\hat{A}_t < 0$), so $\min = (1-\epsilon)\hat{A}_t$ (flat, gradient zero).

    The objective encourages decreasing $\pi_\theta(a_t|s_t)$ but stops at $r_t = 1-\epsilon$. $\square$

    **(c) Financial safety implications.**

    With $\epsilon = 0.2$, the probability ratio $r_t \in [0.8, 1.2]$ means the new policy assigns each action a probability within $\pm 20\%$ of the old policy. This prevents:

    - **Sudden strategy shifts:** A hedging agent cannot suddenly change its hedge ratio dramatically in one update. Without clipping, a single bad batch could cause the agent to switch from hedging to speculating.
    - **Catastrophic drawdowns:** Large policy changes can lead to extreme positions and large losses. Clipping ensures gradual policy evolution.
    - **Instability spirals:** Without clipping, large gradient steps can move the policy to a region where the advantage estimates are inaccurate, leading to further bad updates (a destabilizing feedback loop).

    In financial applications, stability is paramount. A policy that changes gradually is easier to monitor, audit, and risk-manage than one that can change dramatically between updates.

---

**Exercise 5.** A portfolio allocation agent uses a softmax policy: $a_i = e^{z_i(\theta, s)} / \sum_j e^{z_j(\theta, s)}$ for $d = 5$ assets, where $z(\theta, s)$ is a neural network output. (a) Verify that $\sum_i a_i = 1$ and $a_i > 0$, satisfying the simplex constraint for long-only portfolios. (b) Compute $\partial a_i / \partial z_j = a_i(\mathbf{1}_{i=j} - a_j)$ (the softmax Jacobian). (c) If the risk-sensitive objective is $J = \mathbb{E}[R_p] - \frac{\lambda}{2}\text{Var}[R_p]$ where $R_p = \sum_i a_i R_i$, describe how the policy gradient $\nabla_\theta J$ involves both the mean and variance of the portfolio return. (d) Discuss why the softmax parameterization prevents short-selling, and how you would modify it to allow short positions.

??? success "Solution to Exercise 5"
    **(a) Simplex constraint verification.**

    By construction of the softmax function:

    $$
    a_i = \frac{e^{z_i}}{\sum_{j=1}^d e^{z_j}} > 0 \quad \text{for all } i
    $$

    since the exponential function is always positive. Furthermore:

    $$
    \sum_{i=1}^d a_i = \sum_{i=1}^d \frac{e^{z_i}}{\sum_{j=1}^d e^{z_j}} = \frac{\sum_{i=1}^d e^{z_i}}{\sum_{j=1}^d e^{z_j}} = 1
    $$

    Therefore $a \in \{x \in \mathbb{R}^d : x_i > 0, \sum_i x_i = 1\}$, the open probability simplex, satisfying the long-only portfolio constraint. $\square$

    **(b) Softmax Jacobian.**

    For $a_i = e^{z_i} / \sum_j e^{z_j}$:

    $$
    \frac{\partial a_i}{\partial z_j} = \frac{\partial}{\partial z_j}\!\left(\frac{e^{z_i}}{\sum_k e^{z_k}}\right)
    $$

    **Case $i = j$:** Using the quotient rule:

    $$
    \frac{\partial a_i}{\partial z_i} = \frac{e^{z_i} \sum_k e^{z_k} - e^{z_i} e^{z_i}}{(\sum_k e^{z_k})^2} = a_i - a_i^2 = a_i(1 - a_i)
    $$

    **Case $i \neq j$:**

    $$
    \frac{\partial a_i}{\partial z_j} = \frac{0 - e^{z_i} e^{z_j}}{(\sum_k e^{z_k})^2} = -a_i a_j
    $$

    Combining: $\frac{\partial a_i}{\partial z_j} = a_i(\mathbf{1}_{i=j} - a_j)$. In matrix form: $\frac{\partial a}{\partial z} = \text{diag}(a) - a a^\top$. $\square$

    **(c) Risk-sensitive policy gradient.**

    With $J = \mathbb{E}[R_p] - \frac{\lambda}{2}\text{Var}[R_p]$ and $R_p = \sum_i a_i R_i = a^\top R$:

    $$
    \mathbb{E}[R_p] = a^\top \mu, \quad \text{Var}[R_p] = a^\top \Sigma a
    $$

    where $\mu = \mathbb{E}[R]$ and $\Sigma = \text{Cov}(R)$. The gradient with respect to $z$ (the network output):

    $$
    \nabla_z J = \frac{\partial a^\top}{\partial z} \mu - \frac{\lambda}{2} \frac{\partial}{\partial z}(a^\top \Sigma a) = \frac{\partial a^\top}{\partial z}(\mu - \lambda \Sigma a)
    $$

    Using the chain rule: $\nabla_\theta J = \nabla_\theta z \cdot \nabla_z J$. The gradient involves both the mean return vector $\mu$ (encouraging allocation to high-return assets) and the covariance penalty $\lambda \Sigma a$ (discouraging concentrated or correlated positions). The tradeoff between mean and variance is controlled by $\lambda$.

    **(d) Allowing short positions.**

    The softmax constraint $a_i > 0$ prevents short-selling. To allow short positions:

    - **Shifted softmax:** Output $a_i = \frac{e^{z_i}}{\sum_j e^{z_j}} - \frac{1}{d}$. This allows both positive and negative weights while maintaining $\sum_i a_i = 0$ (a dollar-neutral portfolio). Add a parameter for the overall exposure.
    - **Unconstrained output:** Use $a = z / \|z\|_1$ (L1 normalization) which allows negative weights but preserves $\sum |a_i| = 1$.
    - **Two-softmax approach:** Output long weights $a^+$ and short weights $a^-$ separately via two softmax layers, then set $a = w^+ a^+ - w^- a^-$ where $w^+, w^-$ control the long and short exposure.
    - **Direct parameterization:** Output unconstrained $a \in \mathbb{R}^d$ and only enforce $\sum_i a_i = 1$ via a Lagrange multiplier or projection.

---

**Exercise 6.** The deterministic policy gradient theorem states $\nabla_\theta J = \mathbb{E}_s[\nabla_\theta \mu_\theta(s) \nabla_a Q^{\mu_\theta}(s,a)|_{a=\mu_\theta(s)}]$. (a) Explain why this requires a differentiable Q-function (the critic) but not a stochastic policy. (b) In DDPG for optimal execution, the actor outputs the trade size $a = \mu_\theta(s)$ and the critic estimates $Q_w(s,a)$. The actor is updated by backpropagating through the critic: $\nabla_\theta J \approx \nabla_\theta \mu_\theta \cdot \nabla_a Q_w$. Explain this chain rule. (c) Discuss the advantage of deterministic policies for financial applications: they produce the same action in the same state, which is important for reproducibility and risk management.

??? success "Solution to Exercise 6"
    **(a) Differentiable critic requirement.**

    The deterministic policy gradient $\nabla_\theta J = \mathbb{E}_s[\nabla_\theta \mu_\theta(s) \nabla_a Q^{\mu}(s,a)|_{a=\mu_\theta(s)}]$ requires computing $\nabla_a Q(s,a)$---the gradient of the Q-function with respect to the action. This requires a differentiable Q-function approximation (the critic).

    It does **not** require a stochastic policy because the gradient is computed via the chain rule through the Q-function, not via the log-derivative trick. The log-derivative trick $\nabla_\theta \log \pi_\theta(a|s)$ is undefined for a deterministic policy (which assigns probability 1 to a single action). Instead, the deterministic policy gradient bypasses this issue entirely by differentiating through the deterministic action selection $a = \mu_\theta(s)$.

    **(b) Chain rule in DDPG.**

    In DDPG, the actor outputs $a = \mu_\theta(s)$ and the critic estimates $Q_w(s, a)$. The actor update maximizes $Q_w(s, \mu_\theta(s))$ with respect to $\theta$:

    $$
    \nabla_\theta J \approx \nabla_\theta Q_w(s, \mu_\theta(s)) = \underbrace{\nabla_a Q_w(s, a)\big|_{a=\mu_\theta(s)}}_{\text{how Q changes with action}} \cdot \underbrace{\nabla_\theta \mu_\theta(s)}_{\text{how action changes with } \theta}
    $$

    This is the standard chain rule: the gradient flows backward from the Q-value through the action to the policy parameters. The critic tells the actor "how the action should change to increase Q," and the actor adjusts its parameters accordingly. In an optimal execution context, $\nabla_a Q_w$ indicates whether selling more or fewer shares would improve expected execution quality, and $\nabla_\theta \mu_\theta$ maps this into parameter space.

    **(c) Advantages of deterministic policies for finance.**

    Deterministic policies have several advantages for financial applications:

    - **Reproducibility:** Given the same state, the policy always produces the same action. This is critical for audit trails, compliance, and risk management. A stochastic policy might produce a hedge ratio of 0.5 in one run and 0.7 in another for the same market conditions, which is unacceptable for institutional deployment.
    - **No execution noise:** Stochastic exploration noise in live trading introduces unnecessary P&L variability. Deterministic policies produce clean, predictable trades.
    - **Easier risk monitoring:** Risk managers can predict the agent's behavior by evaluating $\mu_\theta(s)$ for any hypothetical state, enabling stress testing and scenario analysis.
    - **Consistency:** Clients and regulators expect consistent behavior. A deterministic policy provides this naturally.

    The exploration needed for training is provided by adding noise externally (e.g., Ornstein-Uhlenbeck process in DDPG) during training only, and removed during deployment.

---

**Exercise 7.** Policy gradient methods converge to local optima, not global ones. (a) For a portfolio optimization problem with 10 assets, the policy landscape may have many local optima. Propose strategies to find good solutions: multiple random restarts, curriculum learning (start with simpler problems), warm-starting from known heuristics (e.g., initialize near the minimum-variance portfolio). (b) Discuss validation: how do you assess whether the learned policy is close to the global optimum? Compare with known analytical solutions when available (e.g., Merton portfolio for simple cases). (c) In practice, a policy that achieves 90% of the theoretically optimal Sharpe ratio may be acceptable if it is robust and stable. Argue that robustness (small policy changes $\to$ small performance changes) is more important than optimality in financial deployment.

??? success "Solution to Exercise 7"
    **(a) Strategies for escaping local optima.**

    For a portfolio optimization problem with 10 assets, the policy landscape $J(\theta)$ is non-convex and may have many local optima. Strategies include:

    - **Multiple random restarts:** Run the policy gradient algorithm $M$ times (e.g., $M = 20$) with different random initializations. Select the best final policy by $J(\theta)$. This is the simplest and most robust approach.
    - **Curriculum learning:** Start with a simpler problem (e.g., 2 assets, no transaction costs) and progressively increase complexity (more assets, add costs, add constraints). Each stage warm-starts from the previous solution. The simple problem has fewer local optima, and the warm-start biases the search toward good regions.
    - **Warm-starting from heuristics:** Initialize $\theta$ near known good policies:
        - Minimum-variance portfolio: $a \propto \Sigma^{-1} \mathbf{1}$
        - Equal-weight portfolio: $a_i = 1/d$
        - Mean-variance optimal (Markowitz): $a \propto \Sigma^{-1} \mu$

        These provide starting points in regions of policy space known to have good properties.
    - **Population-based training:** Maintain a population of policies, share information between them, and periodically replace poor performers with mutations of good ones.

    **(b) Validation against known solutions.**

    To assess proximity to the global optimum:

    - **Analytical benchmarks:** For simplified versions of the problem (e.g., Merton portfolio with CRRA utility, single risky asset, no constraints), the analytical solution is known: $\pi^* = (\mu - r)/(\gamma\sigma^2)$. Train the RL agent on this simplified problem and verify it recovers the analytical solution within a few percent.
    - **Relaxation bounds:** Solve a convex relaxation of the problem (e.g., drop non-convex constraints) to obtain an upper bound on $J^*$. If the learned policy achieves $J(\theta)$ close to this bound, it is near-optimal.
    - **Cross-validation:** Compare the learned policy's out-of-sample performance with multiple baselines (equal-weight, minimum-variance, risk-parity). If the RL policy consistently outperforms all baselines, it is likely in a good region.
    - **Sensitivity analysis:** Perturb $\theta$ locally and check that $J(\theta)$ does not improve significantly, confirming the policy is at least at a local optimum.

    **(c) Robustness over optimality.**

    In financial deployment, robustness is more important than optimality for several reasons:

    - **Parameter uncertainty:** The true $\mu$ and $\Sigma$ are estimated with error. A policy $\theta^*$ that is globally optimal for estimated parameters may be far from optimal for the true parameters. A robust policy that performs well across a range of parameter values is preferable.
    - **Stability under perturbation:** If small changes in market conditions (or small errors in state observation) cause large changes in the policy's behavior, the strategy is fragile. A robust policy satisfies $|J(\theta + \delta\theta) - J(\theta)| \le L\|\delta\theta\|$ with small Lipschitz constant $L$.
    - **Operational risk:** Extreme positions arising from an "optimal" but brittle policy can trigger margin calls, regulatory scrutiny, or forced liquidation. A slightly suboptimal but stable policy avoids these risks.
    - **Model risk:** The true environment differs from the training environment. A policy achieving 90% of the theoretical Sharpe ratio but robust to model misspecification will outperform a 100%-optimal policy that breaks under misspecification.

    Formally, the robust objective is $\max_\theta \min_{\text{model}} J_{\text{model}}(\theta)$, which prioritizes worst-case performance over average-case optimality.
