# RL for Optimal Execution

Optimal execution---liquidating or acquiring a large position while minimizing market impact and timing risk---is a natural application of reinforcement learning. The classical Almgren-Chriss framework provides an analytical benchmark under restrictive assumptions, but RL agents can adapt to real-time market conditions, nonlinear impact, and stochastic liquidity without requiring a closed-form model.

---

## The Optimal Execution Problem

### Classical Formulation

An investor must liquidate $Q$ shares over a time horizon $[0, T]$. At each decision point $t_k$, the investor sells $n_k$ shares, subject to the constraint:

$$
\sum_{k=0}^{N-1} n_k = Q, \quad n_k \geq 0
$$

The remaining inventory is $q_k = Q - \sum_{j=0}^{k-1} n_j$, with $q_0 = Q$ and $q_N = 0$.

### Market Impact

Each trade $n_k$ moves the price:

**Temporary impact** (affects only the execution price of the current trade):

$$
S_k^{\text{exec}} = S_k - \eta \cdot n_k
$$

**Permanent impact** (shifts the fundamental price for all future trades):

$$
S_{k+1} = S_k - \gamma \cdot n_k + \sigma \varepsilon_{k+1}, \quad \varepsilon_{k+1} \sim \mathcal{N}(0, \Delta t)
$$

The implementation shortfall (cost relative to the initial price) is:

$$
\text{IS} = Q \cdot S_0 - \sum_{k=0}^{N-1} n_k \cdot S_k^{\text{exec}} = \sum_{k=0}^{N-1} n_k(\gamma \cdot n_k + \eta \cdot n_k) + \text{volatility terms}
$$

---

## The Almgren-Chriss Benchmark

### Mean-Variance Objective

The Almgren-Chriss model minimizes a mean-variance criterion:

$$
\min_{\{n_k\}} \; \mathbb{E}[\text{IS}] + \lambda \, \text{Var}[\text{IS}]
$$

**Theorem (Almgren-Chriss Optimal Strategy).** Under linear temporary and permanent impact, the optimal deterministic schedule is:

$$
n_k^* = Q \cdot \frac{\sinh\!\left(\kappa(N - k)\Delta t\right) - \sinh\!\left(\kappa(N - k - 1)\Delta t\right)}{\sinh(\kappa N \Delta t)}
$$

where $\kappa = \cosh^{-1}\!\left(\frac{\gamma \Delta t}{2\eta} + 1 + \frac{\lambda\sigma^2 \Delta t}{2\eta}\right) / \Delta t$ balances urgency (risk aversion $\lambda$) against impact.

**Key properties:**

- Higher risk aversion $\lambda$ leads to faster, more front-loaded execution
- The strategy is deterministic and state-independent (does not adapt to price movements)
- The efficient frontier traces out $\text{Var}[\text{IS}]$ vs $\mathbb{E}[\text{IS}]$

### Limitations

The Almgren-Chriss solution is optimal only under:

1. Linear and time-invariant impact functions
2. Arithmetic Brownian motion for the price
3. No stochastic liquidity or volume patterns
4. No information arrival or alpha signals

In practice, all of these assumptions are violated.

---

## MDP Formulation for Execution

### State Space

The RL state captures all information relevant to the execution decision:

$$
s_k = (q_k, S_k, t_k, \mathbf{m}_k)
$$

where:

- $q_k$: remaining inventory (shares left to sell)
- $S_k$: current mid-price
- $t_k$: elapsed time (or time remaining $T - t_k$)
- $\mathbf{m}_k$: market microstructure features (spread, volume, volatility, order-book imbalance)

The inventory $q_k$ and time $t_k$ create urgency; the market features $\mathbf{m}_k$ capture the current trading environment.

### Action Space

The action $a_k$ specifies the trade size at time $t_k$:

$$
a_k \in [0, q_k]
$$

Alternatively, use a normalized action $\tilde{a}_k \in [0, 1]$ representing the fraction of remaining inventory to trade: $n_k = \tilde{a}_k \cdot q_k$.

### Reward Design

The reward function encodes the execution objective. Common designs:

**Implementation shortfall reward:**

$$
r_k = -n_k \cdot \text{slippage}_k = -n_k \cdot (S_0 - S_k^{\text{exec}})
$$

**Per-step revenue with penalty:**

$$
r_k = n_k \cdot S_k^{\text{exec}} - \lambda_{\text{risk}} \cdot q_k^2 \cdot \hat{\sigma}_k^2 \cdot \Delta t
$$

The first term rewards selling at high prices; the second penalizes holding inventory (timing risk).

**Terminal penalty for incomplete execution:**

$$
r_N = -\Lambda \cdot q_N^2
$$

with large $\Lambda > 0$ to enforce the full liquidation constraint.

!!! warning "Reward Shaping Pitfalls"
    Poorly designed rewards can lead to pathological strategies:

    - Without urgency penalty, the agent may delay trading indefinitely
    - Without completion incentive, the agent may leave inventory unsold
    - Over-penalizing holding creates strategies indistinguishable from TWAP

    The reward must balance execution quality against risk and completion requirements.

---

## RL Algorithms for Execution

### Deep Q-Network Approach

Discretize the action space into $A$ bins (e.g., trade 0%, 5%, 10%, ..., 100% of remaining inventory). Learn the Q-function:

$$
Q_\theta(s, a) \approx Q^*(s, a) = \max_\pi \mathbb{E}_\pi\!\left[\sum_{k'=k}^{N-1} \gamma^{k'-k} r_{k'} \mid s_k = s, a_k = a\right]
$$

using a neural network $Q_\theta$ trained via the Bellman loss:

$$
\mathcal{L}(\theta) = \mathbb{E}\!\left[\left(r_k + \gamma \max_{a'} Q_{\bar{\theta}}(s_{k+1}, a') - Q_\theta(s_k, a_k)\right)^2\right]
$$

where $\bar{\theta}$ is a target network updated periodically.

### Actor-Critic Approach

For continuous action spaces, use an actor-critic method:

- **Actor** $\pi_\theta(a \mid s)$: Gaussian policy outputting trade size
- **Critic** $V_w(s)$ or $Q_w(s,a)$: Estimates value function

The policy gradient with advantage estimation:

$$
\nabla_\theta J = \mathbb{E}\!\left[\nabla_\theta \log \pi_\theta(a_k \mid s_k) \hat{A}_k\right]
$$

where $\hat{A}_k = r_k + \gamma V_w(s_{k+1}) - V_w(s_k)$.

### Training Environment

RL execution agents are trained in simulation:

1. **Market simulator:** Generates price paths with realistic dynamics (stochastic volatility, intraday patterns, order-book mechanics)
2. **Impact model:** Simulates temporary and permanent price impact
3. **Episode structure:** Each episode is one liquidation task ($Q$ shares over $T$)

Typical training requires $10^5$--$10^6$ episodes for convergence.

---

## Comparison with Classical Strategies

### TWAP and VWAP

**TWAP (Time-Weighted Average Price):** Sell $Q/N$ shares at each period. Simple, deterministic, ignores market conditions.

**VWAP (Volume-Weighted Average Price):** Sell proportional to predicted volume profile. Better than TWAP but still deterministic.

### Adaptive Advantages of RL

The RL agent can learn to:

1. **Speed up** when spread is tight and volume is high
2. **Slow down** when spread widens or volatility spikes
3. **Exploit momentum:** Sell more aggressively after price increases (mean-reversion) or less aggressively (momentum)
4. **Respond to inventory risk:** Become more aggressive as the deadline approaches with large remaining inventory

**Proposition (Adaptivity Benefit).** Consider a market with two regimes: high liquidity ($\eta_H$, probability $p$) and low liquidity ($\eta_L > \eta_H$, probability $1-p$). The optimal adaptive strategy has expected cost:

$$
C_{\text{adaptive}} = p \cdot C^*(\eta_H) + (1-p) \cdot C^*(\eta_L)
$$

while the optimal static strategy has:

$$
C_{\text{static}} = C^*(p\eta_H + (1-p)\eta_L) > C_{\text{adaptive}}
$$

by Jensen's inequality (since $C^*$ is concave in $\eta$). The gap increases with the dispersion of liquidity states.

---

## Practical Considerations

### Sim-to-Real Transfer

A critical challenge is that the RL agent is trained in simulation but deployed in live markets. The **sim-to-real gap** arises from:

- Imperfect market impact models
- Missing microstructure features
- Latency and execution uncertainty
- Regime changes not represented in training data

Mitigation strategies include:

- **Domain randomization:** Train across a distribution of simulator parameters
- **Conservative policies:** Use PPO with small update steps
- **Online fine-tuning:** Continue learning (carefully) in live markets with small exploration

### Regulatory and Operational Constraints

Execution algorithms must satisfy constraints not easily captured in the standard MDP:

- Maximum participation rate (e.g., no more than 20% of volume)
- Minimum/maximum order sizes
- Exchange-specific rules (tick size, lot size)
- Market-on-close obligations

These are handled via action masking or constrained policy optimization.

---

## Key Takeaways

1. **Optimal execution** is naturally formulated as an MDP where the state includes inventory, price, time, and market conditions.

2. The **Almgren-Chriss** benchmark provides an analytical solution under linear impact, but RL can learn adaptive strategies for nonlinear, stochastic environments.

3. **Reward design** is critical: it must balance execution quality, risk aversion, and completion requirements.

4. **RL agents adapt** to real-time market conditions (liquidity, volatility, volume), providing systematic improvement over static TWAP/VWAP.

5. **Sim-to-real transfer** remains the primary practical challenge, addressed through domain randomization and conservative policies.

---

## Further Reading

- Almgren & Chriss (2001), "Optimal Execution of Portfolio Transactions"
- Nevmyvaka, Feng & Kearns (2006), "Reinforcement Learning for Optimized Trade Execution"
- Ning, Ling & Jaimungal (2021), "Double Deep Q-Learning for Optimal Execution"
- Fang, Oosterlee & Schoenmakers (2021), "Deep RL for Optimal Execution"
- Cartea, Jaimungal & Penalva (2015), *Algorithmic and High-Frequency Trading*, Chapter 6

---

## Exercises

**Exercise 1.** In the Almgren-Chriss framework, a trader liquidates $Q = 10{,}000$ shares over $N = 10$ periods with $\Delta t = 1$, temporary impact $\eta = 0.001$, permanent impact $\gamma = 0.0005$, volatility $\sigma = 0.02$, and risk aversion $\lambda = 10^{-5}$. (a) Compute $\kappa = \cosh^{-1}(\frac{\gamma \Delta t}{2\eta} + 1 + \frac{\lambda \sigma^2 \Delta t}{2\eta})/\Delta t$ and the optimal trade sizes $n_k^*$ for $k = 0, 1, \ldots, 9$. (b) Verify that $\sum_k n_k^* = Q$. (c) Compute the expected implementation shortfall $\mathbb{E}[\text{IS}] = \eta \sum_k (n_k^*)^2 + \gamma \sum_k n_k^* q_k$. (d) Compare with the TWAP strategy $n_k = 1{,}000$ for all $k$.

---

**Exercise 2.** An RL agent for optimal execution uses the state $s_k = (q_k, S_k, t_k)$ and the reward $r_k = n_k S_k^{\text{exec}} - \lambda_{\text{risk}} q_k^2 \hat{\sigma}^2 \Delta t$ with terminal penalty $r_N = -\Lambda q_N^2$. (a) Explain why the risk penalty $\lambda_{\text{risk}} q_k^2 \hat{\sigma}^2 \Delta t$ encourages the agent to reduce inventory: the cost of holding is quadratic in remaining inventory. (b) What happens if $\Lambda$ is too small? The agent may not fully liquidate. What if $\Lambda$ is too large? The agent may dump everything at the end regardless of impact. (c) Propose a reward modification that explicitly enforces $q_N = 0$ as a hard constraint rather than a soft penalty.

---

**Exercise 3.** Compare the RL execution agent with TWAP in a market with stochastic liquidity. The bid-ask spread alternates between $s_{\text{tight}} = 0.01$ and $s_{\text{wide}} = 0.05$ with equal probability at each step. (a) TWAP sells $Q/N$ shares regardless of the spread. Compute the expected total spread cost over $N = 10$ periods for $Q = 10{,}000$. (b) An adaptive RL agent learns to sell more when the spread is tight and less when wide. If the agent sells 1.5 times the TWAP amount when spread is tight and 0.5 times when wide (still totaling $Q$), recompute the expected spread cost. (c) Show that the adaptive strategy reduces expected costs by exploiting the concavity of the cost function. This illustrates the adaptivity benefit formalized in the proposition on $C_{\text{adaptive}} < C_{\text{static}}$.

---

**Exercise 4.** A Deep Q-Network for execution discretizes the action space into 11 levels: sell 0%, 10%, 20%, ..., 100% of remaining inventory. (a) For state $s = (q = 5000, S = 100, t = 5/10)$, the Q-values are $Q(s, 0\%) = -50$, $Q(s, 10\%) = -42$, $Q(s, 20\%) = -38$, $Q(s, 30\%) = -35$, $Q(s, 40\%) = -34$, $Q(s, 50\%) = -36$, ..., $Q(s, 100\%) = -65$. What action does the greedy policy select? (b) With $\epsilon = 0.05$ exploration, what is the probability of selecting each action? (c) The Bellman loss for one transition is $(r + \gamma \max_{a'} Q_{\bar{\theta}}(s', a') - Q_\theta(s, a))^2$. If $r = 3800$, $\gamma = 1$, $\max_{a'} Q_{\bar{\theta}}(s', a') = -30$, and $Q_\theta(s, a) = -34$, compute the loss and the gradient direction for updating $\theta$.

---

**Exercise 5.** The sim-to-real gap is a critical challenge for deploying RL execution agents. (a) A simulator uses linear permanent impact $\gamma = 0.0005$, but the real market has concave impact $\gamma_{\text{real}}(n) = 0.001 \sqrt{n}$. For $n = 1{,}000$ shares, compare the simulated and real permanent impacts. (b) Domain randomization trains the agent across a distribution of simulator parameters: $\gamma \sim \text{Uniform}(0.0003, 0.0008)$, $\eta \sim \text{Uniform}(0.0005, 0.002)$, $\sigma \sim \text{Uniform}(0.01, 0.04)$. Explain why the resulting policy is more robust than one trained on fixed parameters. (c) Propose a safe deployment protocol: start with small order sizes, monitor execution quality (implementation shortfall relative to TWAP benchmark), and gradually increase the agent's autonomy.

---

**Exercise 6.** An actor-critic agent for execution uses a Gaussian policy $\pi_\theta(a|s) = \mathcal{N}(\mu_\theta(s), \sigma_\theta^2(s))$ where $a$ is the trade size. (a) The mean network $\mu_\theta(s)$ has input $(q/Q, S/S_0, (T-t)/T, \text{spread}, \text{volume})$ and outputs a scalar. Why is it important to normalize the inputs? (b) The variance $\sigma_\theta^2(s)$ controls exploration: high variance during training for exploration, low variance during deployment for consistent execution. Describe a schedule for $\sigma$ during training. (c) The advantage estimate is $\hat{A}_k = r_k + \gamma V_w(s_{k+1}) - V_w(s_k)$. If the agent sells aggressively and $r_k$ is high but $V_w(s_{k+1})$ is low (because remaining inventory is small and time is ample), is $\hat{A}_k$ positive or negative? Explain the interpretation.

---

**Exercise 7.** Regulatory constraints require that an execution algorithm not exceed 20% of market volume in any 5-minute interval. (a) Formalize this as a constraint on the action space: $n_k \le 0.20 \cdot V_k$ where $V_k$ is the predicted volume in interval $k$. (b) Action masking sets $Q(s, a) = -\infty$ for infeasible actions. Describe how this is implemented in a DQN. (c) For a continuous-action actor-critic, the policy must be constrained. Propose using a projected Gaussian: sample $a \sim \mathcal{N}(\mu, \sigma^2)$ and clip to $[0, \min(q_k, 0.20 V_k)]$. What are the implications of this clipping for the policy gradient computation?
