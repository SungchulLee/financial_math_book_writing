# RL for Optimal Execution

Optimal execution---liquidating or acquiring a large position while minimizing market impact and timing risk---is a natural application of reinforcement learning. The classical Almgren-Chriss framework provides an analytical benchmark under restrictive assumptions, but RL agents can adapt to real-time market conditions, nonlinear impact, and stochastic liquidity without requiring a closed-form model. Recall (see [§ Connection to Stochastic Control](connection_to_stochastic_control.md)) for the HJB perspective.

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

Recall (see [§ Definition of an MDP](markov_decision_processes.md#definition-of-an-mdp)) for the general MDP framework.

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

using a neural network $Q_\theta$ trained via the Bellman loss (Recall (see [§ Bellman equations](markov_decision_processes.md#bellman-equations))):

$$
\mathcal{L}(\theta) = \mathbb{E}\!\left[\left(r_k + \gamma \max_{a'} Q_{\bar{\theta}}(s_{k+1}, a') - Q_\theta(s_k, a_k)\right)^2\right]
$$

where $\bar{\theta}$ is a target network updated periodically.

### Actor-Critic Approach

Recall (see [§ Actor-Critic Methods](policy_gradient_methods.md#actor-critic-methods)). For continuous action spaces, the actor $\pi_\theta(a \mid s)$ is a Gaussian policy outputting trade size and the critic $V_w(s)$ estimates the value function, with advantage estimate $\hat{A}_k = r_k + \gamma V_w(s_{k+1}) - V_w(s_k)$.

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

??? success "Solution to Exercise 1"
    **(a) Computing $\kappa$ and optimal trade sizes.**

    With $Q = 10{,}000$, $N = 10$, $\Delta t = 1$, $\eta = 0.001$, $\gamma = 0.0005$, $\sigma = 0.02$, $\lambda = 10^{-5}$:

    $$
    \kappa = \frac{1}{\Delta t}\cosh^{-1}\!\left(\frac{\gamma \Delta t}{2\eta} + 1 + \frac{\lambda \sigma^2 \Delta t}{2\eta}\right)
    $$

    $$
    = \cosh^{-1}\!\left(\frac{0.0005 \times 1}{2 \times 0.001} + 1 + \frac{10^{-5} \times 0.0004 \times 1}{2 \times 0.001}\right)
    $$

    $$
    = \cosh^{-1}\!\left(0.25 + 1 + 0.002\right) = \cosh^{-1}(1.252)
    $$

    Since $\cosh^{-1}(x) = \ln(x + \sqrt{x^2 - 1})$:

    $$
    \kappa = \ln(1.252 + \sqrt{1.252^2 - 1}) = \ln(1.252 + \sqrt{0.567504}) = \ln(1.252 + 0.7533)
    $$

    $$
    = \ln(2.0053) \approx 0.6963
    $$

    The optimal trade sizes are:

    $$
    n_k^* = Q \cdot \frac{\sinh(\kappa(N-k)\Delta t) - \sinh(\kappa(N-k-1)\Delta t)}{\sinh(\kappa N \Delta t)}
    $$

    Computing $\sinh(\kappa j)$ for $j = 0, 1, \ldots, 10$:

    | $j$ | $\kappa j$ | $\sinh(\kappa j)$ |
    |---|---|---|
    | 0 | 0 | 0 |
    | 1 | 0.6963 | 0.7553 |
    | 2 | 1.3926 | 1.8795 |
    | 3 | 2.0889 | 3.8019 |
    | 4 | 2.7852 | 7.2088 |
    | 5 | 3.4815 | 13.231 |
    | 6 | 4.1778 | 23.99 |
    | 7 | 4.8741 | 43.22 |
    | 8 | 5.5704 | 77.79 |
    | 9 | 6.2667 | 139.9 |
    | 10 | 6.963 | 251.8 |

    Denominator: $\sinh(6.963) \approx 251.8$.

    Trade sizes $n_k^* = 10{,}000 \times [\sinh(\kappa(10-k)) - \sinh(\kappa(9-k))] / 251.8$:

    | $k$ | $n_k^*$ (approx) |
    |---|---|
    | 0 | $10000 \times (251.8 - 139.9)/251.8 = 10000 \times 0.4442 = 4442$ |
    | 1 | $10000 \times (139.9 - 77.79)/251.8 = 10000 \times 0.2468 = 2468$ |
    | 2 | $10000 \times (77.79 - 43.22)/251.8 = 10000 \times 0.1373 = 1373$ |
    | 3 | $10000 \times (43.22 - 23.99)/251.8 = 10000 \times 0.0764 = 764$ |
    | 4 | $10000 \times (23.99 - 13.231)/251.8 = 10000 \times 0.0427 = 427$ |
    | 5 | $10000 \times (13.231 - 7.209)/251.8 = 10000 \times 0.0239 = 239$ |
    | 6 | $10000 \times (7.209 - 3.802)/251.8 = 10000 \times 0.01353 = 135$ |
    | 7 | $10000 \times (3.802 - 1.880)/251.8 = 10000 \times 0.00764 = 76$ |
    | 8 | $10000 \times (1.880 - 0.755)/251.8 = 10000 \times 0.00447 = 45$ |
    | 9 | $10000 \times (0.755 - 0)/251.8 = 10000 \times 0.00300 = 30$ |

    The strategy is heavily front-loaded: approximately 44% of shares are sold in the first period, reflecting the high risk aversion that creates urgency to reduce inventory quickly.

    **(b) Verification that $\sum_k n_k^* = Q$.**

    $$
    \sum_{k=0}^{9} n_k^* = Q \cdot \frac{\sinh(\kappa N) - \sinh(0)}{\sinh(\kappa N)} = Q \cdot \frac{\sinh(\kappa N)}{\sinh(\kappa N)} = Q = 10{,}000 \checkmark
    $$

    This is guaranteed by the telescoping structure of the numerator: $\sum_k [\sinh(\kappa(N-k)) - \sinh(\kappa(N-k-1))] = \sinh(\kappa N) - \sinh(0) = \sinh(\kappa N)$.

    **(c) Expected implementation shortfall.**

    $$
    \mathbb{E}[\text{IS}] = \eta \sum_{k=0}^{9} (n_k^*)^2 + \gamma \sum_{k=0}^{9} n_k^* q_k
    $$

    where $q_k = Q - \sum_{j=0}^{k-1} n_j^*$. Computing the key sums approximately:

    Temporary impact: $\eta \sum (n_k^*)^2 = 0.001 \times (4442^2 + 2468^2 + \ldots + 30^2)$. The dominant terms are the first few: $4442^2 \approx 19.73 \times 10^6$, $2468^2 \approx 6.09 \times 10^6$, $1373^2 \approx 1.89 \times 10^6$. Total $\approx 0.001 \times 28.6 \times 10^6 \approx 28{,}600$.

    Permanent impact: $\gamma \sum n_k^* q_k$, where the first term is $0.0005 \times 4442 \times 10000 = 22{,}210$. Total permanent impact $\approx 0.0005 \times 48 \times 10^6 \approx 24{,}000$.

    Total $\mathbb{E}[\text{IS}] \approx 28{,}600 + 24{,}000 = 52{,}600$ (in price units times shares).

    **(d) Comparison with TWAP.**

    TWAP: $n_k = 1{,}000$ for all $k$.

    $$
    \mathbb{E}[\text{IS}]_{\text{TWAP}} = \eta \sum_{k=0}^{9} 1000^2 + \gamma \sum_{k=0}^{9} 1000 \cdot q_k = 0.001 \times 10 \times 10^6 + 0.0005 \times 1000 \times 55000
    $$

    $$
    = 10{,}000 + 27{,}500 = 37{,}500
    $$

    where $\sum q_k = 10000 + 9000 + \ldots + 1000 = 55{,}000$.

    TWAP has lower expected cost ($37{,}500$ vs. $52{,}600$) because the front-loaded optimal strategy incurs higher temporary impact from large initial trades. However, the optimal strategy has lower **variance** of IS (since it reduces inventory quickly, reducing exposure to price volatility). The mean-variance objective trades off higher expected cost for lower risk, and for $\lambda = 10^{-5}$, the risk reduction justifies the additional cost.

---

**Exercise 2.** An RL agent for optimal execution uses the state $s_k = (q_k, S_k, t_k)$ and the reward $r_k = n_k S_k^{\text{exec}} - \lambda_{\text{risk}} q_k^2 \hat{\sigma}^2 \Delta t$ with terminal penalty $r_N = -\Lambda q_N^2$. (a) Explain why the risk penalty $\lambda_{\text{risk}} q_k^2 \hat{\sigma}^2 \Delta t$ encourages the agent to reduce inventory: the cost of holding is quadratic in remaining inventory. (b) What happens if $\Lambda$ is too small? The agent may not fully liquidate. What if $\Lambda$ is too large? The agent may dump everything at the end regardless of impact. (c) Propose a reward modification that explicitly enforces $q_N = 0$ as a hard constraint rather than a soft penalty.

??? success "Solution to Exercise 2"
    **(a) Risk penalty encourages inventory reduction.**

    The per-step risk penalty is $\lambda_{\text{risk}} q_k^2 \hat{\sigma}^2 \Delta t$. This is the variance of the inventory's mark-to-market change over one period:

    $$
    \text{Var}[q_k \Delta S_k] = q_k^2 \hat{\sigma}^2 \Delta t
    $$

    The penalty is **quadratic** in $q_k$: holding 2000 shares costs 4 times as much as holding 1000. This strongly incentivizes the agent to reduce inventory quickly. Large positions create large per-step penalties, pushing the agent to sell. The penalty also scales with estimated volatility $\hat{\sigma}$: in high-volatility environments, the urgency to reduce inventory increases.

    **(b) Effect of terminal penalty magnitude $\Lambda$.**

    **$\Lambda$ too small:** The terminal penalty $-\Lambda q_N^2$ is weak. If the agent finds it costly to sell all shares (due to impact), it may choose to leave some inventory unsold, accepting a small terminal penalty rather than incurring large impact costs. The resulting policy violates the full-liquidation constraint $q_N = 0$.

    **$\Lambda$ too large:** The terminal penalty dominates all other considerations. The agent is so afraid of the terminal penalty that it may dump all remaining inventory in the last few periods regardless of market conditions, accepting enormous temporary impact. This produces a strategy that hoards inventory early (to avoid intermediate impact) and then sells everything at the end---essentially the opposite of a good execution strategy.

    The optimal $\Lambda$ is large enough to ensure $q_N \approx 0$ in almost all episodes but not so large that it distorts the intermediate trading behavior.

    **(c) Hard constraint enforcement.**

    To enforce $q_N = 0$ as a hard constraint:

    - **Action masking at the final step:** At the last period $k = N-1$, force $n_{N-1} = q_{N-1}$ (sell everything remaining). This removes the terminal penalty entirely and guarantees full liquidation. The reward modification is:

    $$
    r_k = \begin{cases} n_k S_k^{\text{exec}} - \lambda_{\text{risk}} q_k^2 \hat{\sigma}^2 \Delta t & k < N-1 \\ q_{N-1} S_{N-1}^{\text{exec}} & k = N-1 \end{cases}
    $$

    - **Progressive forcing:** In the last $m$ periods, require $n_k \ge q_k / (N - k)$ (at least a TWAP-like minimum). This ensures the agent cannot postpone excessively.
    - **Constrained optimization:** Use a Lagrangian approach where the constraint $q_N = 0$ is enforced via a multiplier $\mu$: $r_N = -\mu \cdot q_N$, with $\mu$ adapted during training to satisfy the constraint on average.

---

**Exercise 3.** Compare the RL execution agent with TWAP in a market with stochastic liquidity. The bid-ask spread alternates between $s_{\text{tight}} = 0.01$ and $s_{\text{wide}} = 0.05$ with equal probability at each step. (a) TWAP sells $Q/N$ shares regardless of the spread. Compute the expected total spread cost over $N = 10$ periods for $Q = 10{,}000$. (b) An adaptive RL agent learns to sell more when the spread is tight and less when wide. If the agent sells 1.5 times the TWAP amount when spread is tight and 0.5 times when wide (still totaling $Q$), recompute the expected spread cost. (c) Show that the adaptive strategy reduces expected costs by exploiting the concavity of the cost function. This illustrates the adaptivity benefit formalized in the proposition on $C_{\text{adaptive}} < C_{\text{static}}$.

??? success "Solution to Exercise 3"
    **(a) TWAP expected spread cost.**

    TWAP sells $n = Q/N = 10{,}000/10 = 1{,}000$ shares per period. The spread cost per share is half the bid-ask spread: $s_k/2$. The expected spread per period is $(0.01 + 0.05)/2 = 0.03$ (since each regime has equal probability). Total expected spread cost:

    $$
    C_{\text{TWAP}} = \sum_{k=0}^{9} n \cdot \frac{\mathbb{E}[s_k]}{2} = 10 \times 1000 \times \frac{0.03}{2} = 10 \times 15 = 150
    $$

    Alternatively, the total expected spread cost is $Q \cdot \mathbb{E}[s]/2 = 10{,}000 \times 0.015 = 150$.

    **(b) Adaptive strategy expected spread cost.**

    The adaptive agent sells $n_{\text{tight}} = 1.5 \times 1000 = 1500$ when spread is tight and $n_{\text{wide}} = 0.5 \times 1000 = 500$ when spread is wide. Expected shares sold per period: $0.5 \times 1500 + 0.5 \times 500 = 1000$, so $\sum n_k = 10{,}000$ in expectation. The spread cost per period:

    $$
    \mathbb{E}[n_k \cdot s_k/2] = 0.5 \times 1500 \times \frac{0.01}{2} + 0.5 \times 500 \times \frac{0.05}{2}
    $$

    $$
    = 0.5 \times 7.5 + 0.5 \times 12.5 = 3.75 + 6.25 = 10
    $$

    Total over 10 periods:

    $$
    C_{\text{adaptive}} = 10 \times 10 = 100
    $$

    The adaptive strategy saves $150 - 100 = 50$ in spread costs, a **33% reduction**.

    **(c) Jensen's inequality argument.**

    The expected cost of the adaptive strategy is:

    $$
    C_{\text{adaptive}} = \sum_k \mathbb{E}\!\left[n_k(s_k) \cdot s_k/2\right]
    $$

    where $n_k$ depends on $s_k$. The static strategy uses $n_k = \bar{n}$ regardless of $s_k$:

    $$
    C_{\text{static}} = \bar{n} \sum_k \mathbb{E}[s_k/2]
    $$

    The adaptive strategy solves a concave optimization problem at each step: maximize $n_k \cdot (P - s_k/2)$ subject to $\mathbb{E}[n_k] = \bar{n}$. By Jensen's inequality, for a concave cost function $C(\eta)$ (where $\eta$ is the effective impact):

    $$
    \mathbb{E}[C^*(\eta_k)] \le C^*(\mathbb{E}[\eta_k])
    $$

    (This is the opposite direction of Jensen for concave functions: the agent allocates more volume to low-cost states and less to high-cost states, exploiting the curvature of the cost function.) The static strategy's cost $C^*(p\eta_H + (1-p)\eta_L)$ is higher than the adaptive cost $pC^*(\eta_H) + (1-p)C^*(\eta_L)$ because the cost function is concave in the impact parameter. The gap increases with the dispersion of liquidity conditions $|\eta_H - \eta_L|$.

---

**Exercise 4.** A Deep Q-Network for execution discretizes the action space into 11 levels: sell 0%, 10%, 20%, ..., 100% of remaining inventory. (a) For state $s = (q = 5000, S = 100, t = 5/10)$, the Q-values are $Q(s, 0\%) = -50$, $Q(s, 10\%) = -42$, $Q(s, 20\%) = -38$, $Q(s, 30\%) = -35$, $Q(s, 40\%) = -34$, $Q(s, 50\%) = -36$, ..., $Q(s, 100\%) = -65$. What action does the greedy policy select? (b) With $\epsilon = 0.05$ exploration, what is the probability of selecting each action? (c) The Bellman loss for one transition is $(r + \gamma \max_{a'} Q_{\bar{\theta}}(s', a') - Q_\theta(s, a))^2$. If $r = 3800$, $\gamma = 1$, $\max_{a'} Q_{\bar{\theta}}(s', a') = -30$, and $Q_\theta(s, a) = -34$, compute the loss and the gradient direction for updating $\theta$.

??? success "Solution to Exercise 4"
    **(a) Greedy action selection.**

    The greedy policy selects $a^* = \arg\max_a Q(s, a)$. From the given Q-values:

    | Action | Q-value |
    |---|---|
    | 0% | $-50$ |
    | 10% | $-42$ |
    | 20% | $-38$ |
    | 30% | $-35$ |
    | **40%** | **$-34$** |
    | 50% | $-36$ |
    | ... | ... |
    | 100% | $-65$ |

    The maximum Q-value is $-34$ at action $40\%$. The greedy policy sells $40\% \times 5000 = 2000$ shares.

    This is intuitive: with $q = 5000$ shares and half the time remaining, selling 40% balances the urgency to liquidate against the impact of a large trade.

    **(b) $\epsilon$-greedy probabilities.**

    With $\epsilon = 0.05$ and $|\mathcal{A}| = 11$ actions:

    $$
    P(a = 40\%) = 1 - \epsilon + \frac{\epsilon}{|\mathcal{A}|} = 0.95 + \frac{0.05}{11} \approx 0.9545
    $$

    $$
    P(a \neq 40\%) = \frac{\epsilon}{|\mathcal{A}|} = \frac{0.05}{11} \approx 0.00455 \quad \text{(each non-greedy action)}
    $$

    The agent exploits (selects 40%) with 95.45% probability and explores uniformly among all 11 actions with 4.55% total probability.

    **(c) Bellman loss and gradient direction.**

    The Bellman loss for the transition is:

    $$
    L = (r + \gamma \max_{a'} Q_{\bar{\theta}}(s', a') - Q_\theta(s, a))^2
    $$

    $$
    = (3800 + 1 \times (-30) - (-34))^2 = (3800 - 30 + 34)^2 = (3804)^2 = 14{,}470{,}416
    $$

    The TD target is $r + \gamma \max_{a'} Q_{\bar{\theta}}(s', a') = 3800 - 30 = 3770$. The current Q-value is $Q_\theta(s, a) = -34$. The TD error is $\delta = 3770 - (-34) = 3804$.

    The gradient of the loss with respect to $\theta$:

    $$
    \nabla_\theta L = -2\delta \cdot \nabla_\theta Q_\theta(s, a) = -2 \times 3804 \times \nabla_\theta Q_\theta(s, a)
    $$

    Since $\delta > 0$, the gradient update $\theta \leftarrow \theta - \alpha \nabla_\theta L$ increases $Q_\theta(s, a)$ toward the TD target. The large TD error ($3804$) indicates that the current Q-value ($-34$) severely underestimates the actual value of selling 40% in this state, and the update will correct this.

    Note: The large magnitude of $\delta$ suggests the Q-network is early in training and has not yet converged. The per-step revenue $r = 3800$ (selling 2000 shares at roughly $\$1.90$ each) dwarfs the continuation value, which is typical for near-terminal states.

---

**Exercise 5.** The sim-to-real gap is a critical challenge for deploying RL execution agents. (a) A simulator uses linear permanent impact $\gamma = 0.0005$, but the real market has concave impact $\gamma_{\text{real}}(n) = 0.001 \sqrt{n}$. For $n = 1{,}000$ shares, compare the simulated and real permanent impacts. (b) Domain randomization trains the agent across a distribution of simulator parameters: $\gamma \sim \text{Uniform}(0.0003, 0.0008)$, $\eta \sim \text{Uniform}(0.0005, 0.002)$, $\sigma \sim \text{Uniform}(0.01, 0.04)$. Explain why the resulting policy is more robust than one trained on fixed parameters. (c) Propose a safe deployment protocol: start with small order sizes, monitor execution quality (implementation shortfall relative to TWAP benchmark), and gradually increase the agent's autonomy.

??? success "Solution to Exercise 5"
    **(a) Simulated vs. real permanent impact.**

    For $n = 1{,}000$ shares:

    $$
    \text{Simulated impact} = \gamma \cdot n = 0.0005 \times 1000 = 0.5
    $$

    $$
    \text{Real impact} = \gamma_{\text{real}}(n) = 0.001 \sqrt{1000} = 0.001 \times 31.62 = 0.03162
    $$

    The simulated linear impact ($0.5$) is **16 times larger** than the real concave impact ($0.032$). The linear model severely overestimates the impact of large trades. Conversely, for very small trades ($n = 1$): simulated $= 0.0005$, real $= 0.001$, so the linear model underestimates small-trade impact.

    This mismatch means an agent trained on linear impact will be overly cautious about large trades (overestimating their cost) and insufficiently cautious about small trades (underestimating their cost). The resulting execution schedule will be more uniform than optimal.

    **(b) Domain randomization for robustness.**

    Training across randomized parameters $\gamma \sim U(0.0003, 0.0008)$, $\eta \sim U(0.0005, 0.002)$, $\sigma \sim U(0.01, 0.04)$:

    - The agent encounters a variety of market conditions during training, each representing a different "world."
    - It cannot memorize the optimal strategy for a single parameter set; instead, it must learn a **robust policy** that works well on average across all parameter combinations.
    - The learned policy is smooth in the parameter space: it adapts to high-impact environments (sell slowly) and low-impact environments (sell more aggressively) based on observed state features.
    - When deployed in the real market (which may have parameters outside the training range), the robust policy generalizes better than a fixed-parameter policy because it has learned the general principle "sell less when impact is high" rather than a specific schedule.

    The key insight is that domain randomization implicitly creates a minimax policy: $\max_\theta \mathbb{E}_{\text{params}}[J(\theta; \text{params})]$, which is robust to parameter uncertainty.

    **(c) Safe deployment protocol.**

    1. **Phase 1 (shadow mode):** Run the RL agent alongside the existing TWAP algorithm. Record what the RL agent would have done, but execute TWAP. Compare implementation shortfall: $\text{IS}_{\text{RL}} - \text{IS}_{\text{TWAP}}$ for each order.
    2. **Phase 2 (small orders):** Deploy the RL agent on small orders (e.g., orders less than 1% of daily volume). Monitor: (i) implementation shortfall relative to TWAP, (ii) maximum participation rate, (iii) any constraint violations.
    3. **Phase 3 (gradual scaling):** If Phase 2 shows consistent improvement ($> 1$ bps savings with no constraint violations over 1 month), increase to medium orders. Continue monitoring.
    4. **Phase 4 (full deployment):** After 3+ months of successful medium-order deployment, allow large orders with additional safeguards.

    Safeguards throughout:

    - **Kill switch:** If $\text{IS}_{\text{RL}} - \text{IS}_{\text{TWAP}} > \text{threshold}$ for any order, immediately revert to TWAP.
    - **Participation limits:** Hard cap at 20% of volume regardless of agent's desired trade size.
    - **Daily P&L monitoring:** If aggregate RL execution cost exceeds TWAP by more than $X$ bps over a day, disable RL for the rest of the day.

---

**Exercise 6.** An actor-critic agent for execution uses a Gaussian policy $\pi_\theta(a|s) = \mathcal{N}(\mu_\theta(s), \sigma_\theta^2(s))$ where $a$ is the trade size. (a) The mean network $\mu_\theta(s)$ has input $(q/Q, S/S_0, (T-t)/T, \text{spread}, \text{volume})$ and outputs a scalar. Why is it important to normalize the inputs? (b) The variance $\sigma_\theta^2(s)$ controls exploration: high variance during training for exploration, low variance during deployment for consistent execution. Describe a schedule for $\sigma$ during training. (c) The advantage estimate is $\hat{A}_k = r_k + \gamma V_w(s_{k+1}) - V_w(s_k)$. If the agent sells aggressively and $r_k$ is high but $V_w(s_{k+1})$ is low (because remaining inventory is small and time is ample), is $\hat{A}_k$ positive or negative? Explain the interpretation.

??? success "Solution to Exercise 6"
    **(a) Input normalization.**

    The inputs to the network $\mu_\theta(s)$ are $(q/Q, S/S_0, (T-t)/T, \text{spread}, \text{volume})$. Normalization is important because:

    - **Scale differences:** $q$ ranges from 0 to $Q$ (e.g., 10,000), $S$ is around 100, spread is around 0.01, and volume may be in millions. Without normalization, the network's weights would need to span orders of magnitude, making training unstable.
    - **Gradient flow:** Neural networks with BatchNorm or similar techniques rely on inputs being roughly in $[-1, 1]$ or $[0, 1]$. Large inputs cause large activations, saturated gradients, and slow convergence.
    - **Generalization:** Normalized inputs ($q/Q \in [0, 1]$, $(T-t)/T \in [0, 1]$) allow the network to generalize across different order sizes $Q$ and horizons $T$. A network trained with $Q = 10{,}000$ can potentially be applied to $Q = 50{,}000$ if the inputs are normalized.
    - **Interpretability:** Normalized inputs have clear interpretations: $q/Q$ is "fraction of inventory remaining," $(T-t)/T$ is "fraction of time remaining."

    **(b) Variance schedule during training.**

    A practical schedule for $\sigma_\theta(s)$:

    - **Early training** (episodes 0--$10^4$): High variance $\sigma = 0.3 \cdot q/Q$ (proportional to remaining inventory). This ensures broad exploration of different trade sizes.
    - **Mid training** (episodes $10^4$--$10^5$): Decay $\sigma$ linearly or exponentially: $\sigma = 0.3 \cdot q/Q \cdot \max(0.1, 1 - \text{episode}/10^5)$. The agent gradually shifts from exploration to exploitation.
    - **Late training** (episodes $> 10^5$): Small $\sigma = 0.03 \cdot q/Q$. Minimal exploration, fine-tuning the policy.
    - **Deployment:** $\sigma \to 0$ (deterministic policy $a = \mu_\theta(s)$). No exploration noise in live trading.

    Alternatively, use learned variance: the network outputs both $\mu$ and $\log \sigma$, and the entropy bonus in PPO/SAC naturally controls exploration.

    **(c) Advantage interpretation.**

    The advantage is $\hat{A}_k = r_k + \gamma V_w(s_{k+1}) - V_w(s_k)$.

    If the agent sells aggressively:

    - $r_k$ is high (large $n_k \times S_k^{\text{exec}}$, substantial revenue this period).
    - $V_w(s_{k+1})$ is low because after selling aggressively, $q_{k+1}$ is small and $T - t_{k+1}$ is still ample---the "easy" part of the execution is already done, and the remaining value is small.
    - $V_w(s_k)$ was high before the trade (large inventory remaining, significant future value).

    The sign of $\hat{A}_k$ depends on the balance:

    $$
    \hat{A}_k = \underbrace{r_k}_{\text{high}} + \underbrace{\gamma V_w(s_{k+1})}_{\text{low}} - \underbrace{V_w(s_k)}_{\text{high}}
    $$

    If $r_k$ is sufficiently high to compensate for the drop in value ($V_w(s_k) - \gamma V_w(s_{k+1})$), then $\hat{A}_k > 0$: the aggressive sell was better than average. If the agent sold too aggressively (high impact cost reducing $r_k$ significantly), then $\hat{A}_k < 0$: selling this much was worse than the critic expected. The advantage directly tells the actor whether to sell more or less aggressively in similar states.

---

**Exercise 7.** Regulatory constraints require that an execution algorithm not exceed 20% of market volume in any 5-minute interval. (a) Formalize this as a constraint on the action space: $n_k \le 0.20 \cdot V_k$ where $V_k$ is the predicted volume in interval $k$. (b) Action masking sets $Q(s, a) = -\infty$ for infeasible actions. Describe how this is implemented in a DQN. (c) For a continuous-action actor-critic, the policy must be constrained. Propose using a projected Gaussian: sample $a \sim \mathcal{N}(\mu, \sigma^2)$ and clip to $[0, \min(q_k, 0.20 V_k)]$. What are the implications of this clipping for the policy gradient computation?

??? success "Solution to Exercise 7"
    **(a) Participation rate constraint formalization.**

    At each decision period $k$, the agent's trade size $n_k$ is subject to:

    $$
    0 \le n_k \le \min(q_k, \, 0.20 \cdot V_k)
    $$

    where $q_k$ is remaining inventory and $V_k$ is the predicted (or realized) market volume in the interval. The first constraint ($n_k \le q_k$) ensures the agent does not sell more than it holds. The second ($n_k \le 0.20 V_k$) enforces the regulatory participation rate limit.

    In the MDP formulation, the feasible action set is state-dependent:

    $$
    \mathcal{A}(s_k) = \{a : 0 \le a \le \bar{a}_k\}, \quad \bar{a}_k = \min(q_k, 0.20 V_k)
    $$

    This constraint tightens in low-volume periods (early morning, lunch hour) and relaxes in high-volume periods (open, close), forcing the agent to align its trading with market activity.

    **(b) Action masking in DQN.**

    In a DQN with discrete actions $a \in \{0\%, 10\%, \ldots, 100\%\}$ of remaining inventory, action masking works as follows:

    1. Compute the maximum feasible fraction: $\bar{f}_k = \min(1.0, 0.20 V_k / q_k)$.
    2. Define the feasible action set: $\mathcal{A}_{\text{feasible}} = \{a : a \le \bar{f}_k\}$.
    3. Before the argmax, set $Q(s_k, a) = -\infty$ for all $a \notin \mathcal{A}_{\text{feasible}}$.
    4. Select $a^* = \arg\max_{a \in \mathcal{A}_{\text{feasible}}} Q(s_k, a)$.

    Implementation: apply a mask vector $\mathbf{m} \in \{0, 1\}^{|\mathcal{A}|}$ where $m_a = 1$ if $a$ is feasible:

    $$
    Q_{\text{masked}}(s, a) = Q_\theta(s, a) + (1 - m_a) \times (-10^{10})
    $$

    The large negative value ensures infeasible actions are never selected. During training, the Bellman target also uses the masked Q-values: $y = r + \gamma \max_{a' \in \mathcal{A}_{\text{feasible}}} Q_{\bar{\theta}}(s', a')$.

    **(c) Projected Gaussian and policy gradient implications.**

    The projected Gaussian policy:

    1. Sample $\tilde{a} \sim \mathcal{N}(\mu_\theta(s), \sigma_\theta^2(s))$.
    2. Clip: $a = \text{clip}(\tilde{a}, 0, \bar{a}_k)$ where $\bar{a}_k = \min(q_k, 0.20 V_k)$.

    **Implications for policy gradient:**

    - **Probability mass accumulation at boundaries:** The clipping maps all samples below 0 to 0 and all above $\bar{a}_k$ to $\bar{a}_k$. The effective distribution of $a$ has point masses at the boundaries:

    $$
    P(a = 0) = \Phi\!\left(\frac{0 - \mu}{\sigma}\right), \quad P(a = \bar{a}_k) = 1 - \Phi\!\left(\frac{\bar{a}_k - \mu}{\sigma}\right)
    $$

    - **Biased gradients:** The standard REINFORCE gradient $\nabla_\theta \log \pi_\theta(a|s) \cdot G$ assumes the log-probability is differentiable. At the boundaries, the density is a delta function and $\log \pi$ is not well-defined. Naively using $\nabla_\theta \log \mathcal{N}(\tilde{a}|\mu, \sigma^2)$ with the pre-clipped sample $\tilde{a}$ introduces bias because the executed action $a$ differs from $\tilde{a}$.
    - **Practical workaround:** Use the **squashed Gaussian** (as in SAC): apply a sigmoid or tanh transformation instead of hard clipping: $a = \bar{a}_k \cdot \text{sigmoid}(z)$ where $z \sim \mathcal{N}(\mu, \sigma^2)$. The log-probability is well-defined and differentiable:

    $$
    \log \pi(a|s) = \log \mathcal{N}(z|\mu, \sigma^2) - \log\!\left|\frac{da}{dz}\right|
    $$

    This avoids the boundary issues while ensuring $a \in (0, \bar{a}_k)$ always.

    - **Alternative:** Use constrained policy optimization (CPO or Lagrangian methods) where the constraint $n_k \le 0.20 V_k$ is enforced via a penalty term rather than hard clipping, keeping the policy gradient well-defined.
