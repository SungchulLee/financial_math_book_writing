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
