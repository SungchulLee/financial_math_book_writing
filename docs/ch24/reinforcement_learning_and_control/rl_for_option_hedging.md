# RL for Option Hedging

Option hedging under realistic market conditions---discrete rebalancing, transaction costs, model uncertainty---is a sequential decision problem naturally suited to reinforcement learning. The RL agent learns a hedging policy that adapts to realized market dynamics, replacing the model-dependent delta hedge with a data-driven strategy that can outperform under frictions and misspecification.

---

## Hedging as a Sequential Decision Problem

### The Classical Delta Hedge and Its Shortcomings

Under Black-Scholes assumptions, a European option with price $V(t, S)$ is perfectly hedged by holding $\Delta_t = \partial V / \partial S$ shares of the underlying. In continuous time with zero transaction costs, the replicating portfolio's P&L is:

$$
\text{P\&L}_{\text{BS}} = V(0, S_0) + \int_0^T \Delta_t \, dS_t - V(T, S_T) = 0
$$

In practice, with discrete rebalancing at times $t_0, t_1, \ldots, t_{N-1}$, the P&L is:

$$
\text{P\&L}_{\text{discrete}} = V(0, S_0) + \sum_{k=0}^{N-1} \Delta_{t_k}(S_{t_{k+1}} - S_{t_k}) - V(T, S_T) \neq 0
$$

The residual has standard deviation proportional to $\sigma^2 \sqrt{\Delta t} \cdot \Gamma$ (the gamma exposure times the square root of the rebalancing interval). Adding proportional transaction costs $\kappa$, each rebalancing incurs cost:

$$
C_k = \kappa \, |S_{t_k}| \cdot |\Delta_{t_k} - \Delta_{t_{k-1}}|
$$

The total cost scales as $\kappa \cdot \sigma \cdot S \cdot \sqrt{N}$ for $N$ rebalancing periods, creating a trade-off: more frequent rebalancing reduces hedging error but increases costs.

---

## MDP Formulation

### State Space

The hedging state at time $t_k$ encodes all relevant information:

$$
s_k = \left(\frac{S_{t_k}}{K}, \; \frac{T - t_k}{T}, \; \delta_{k-1}, \; \hat{\sigma}_k, \; \hat{\Delta}_k^{\text{BS}}\right)
$$

where:

- $S_{t_k}/K$: moneyness (normalized stock price)
- $(T - t_k)/T$: normalized time to maturity
- $\delta_{k-1}$: current hedge position (from previous rebalancing)
- $\hat{\sigma}_k$: estimated or implied volatility
- $\hat{\Delta}_k^{\text{BS}}$: Black-Scholes delta (as a feature, not necessarily the action)

Including the Black-Scholes delta as a state feature allows the RL agent to learn corrections to the analytical hedge.

### Action Space

The action $a_k = \delta_k \in \mathbb{R}$ specifies the new hedge position (number of shares of the underlying held during $[t_k, t_{k+1})$). Alternatively, the action can represent the **change** in position:

$$
a_k = \delta_k - \delta_{k-1} \in \mathbb{R}
$$

### Reward Function

The reward captures the hedging quality. A natural choice is the **negative P&L slippage minus costs**:

$$
r_k = \delta_{k}(S_{t_{k+1}} - S_{t_k}) - \kappa \, |S_{t_k}| \cdot |\delta_k - \delta_{k-1}|
$$

At the terminal step, the option payoff enters:

$$
r_{N} = -H(S_T)
$$

where $H(S_T) = (S_T - K)^+$ for a call. The total return is:

$$
G = \sum_{k=0}^{N} r_k = \sum_{k=0}^{N-1} \delta_k(S_{t_{k+1}} - S_{t_k}) - \sum_k C_k - H(S_T)
$$

### Risk-Sensitive Objectives

Standard RL maximizes $\mathbb{E}[G]$, but hedging requires controlling P&L variability. Risk-sensitive formulations include:

**Mean-variance:**

$$
J(\theta) = \mathbb{E}_{\pi_\theta}[G] - \frac{\lambda}{2}\text{Var}_{\pi_\theta}[G]
$$

**CVaR optimization:**

$$
J(\theta) = \text{CVaR}_\alpha(G) = \mathbb{E}[G \mid G \leq q_\alpha(G)]
$$

**Entropic risk:**

$$
J(\theta) = -\frac{1}{\lambda}\log\mathbb{E}\!\left[e^{-\lambda G}\right]
$$

The entropic formulation connects directly to exponential utility and the deep hedging framework.

---

## Learning Algorithms

### Deep Q-Learning for Hedging

Discretize the hedge ratio into $A$ levels (e.g., $\delta \in \{0, 0.1, 0.2, \ldots, 1.0\}$). The Q-network learns:

$$
Q_\theta(s_k, \delta_k) \approx \mathbb{E}\!\left[\sum_{j=k}^{N} r_j \mid s_k, \delta_k, \pi^*\right]
$$

At each step, the agent selects $\delta_k = \arg\max_\delta Q_\theta(s_k, \delta)$.

### Policy Gradient for Hedging

For continuous hedge ratios, use a Gaussian policy:

$$
\delta_k \sim \pi_\theta(\cdot \mid s_k) = \mathcal{N}\!\left(\mu_\theta(s_k), \sigma_\theta^2(s_k)\right)
$$

The policy gradient with baseline:

$$
\nabla_\theta J = \mathbb{E}\!\left[\sum_{k=0}^{N-1} \nabla_\theta \log \pi_\theta(\delta_k \mid s_k)(G_k - b(s_k))\right]
$$

### Training Protocol

1. **Environment:** Simulate $M$ stock price paths under a chosen model (GBM, Heston, or empirical bootstrap)
2. **Episode:** Each episode is one option hedging task from $t = 0$ to $t = T$
3. **Training:** Run PPO or SAC for $10^5$--$10^6$ episodes
4. **Evaluation:** Test on held-out paths (different random seeds or different model parameters)

---

## Comparison with Delta Hedging

### Theoretical Analysis

**Proposition.** In the Black-Scholes model with zero transaction costs and continuous rebalancing, the optimal RL policy converges to the delta hedge $\delta_k = \partial V / \partial S(t_k, S_{t_k})$.

This follows because the delta hedge perfectly replicates the payoff, achieving $\text{Var}[G] = 0$, which is the global optimum for any risk-averse objective.

**Proposition.** With proportional transaction costs $\kappa > 0$, the optimal policy differs from delta hedging. The RL agent learns a **no-trade band** around the Black-Scholes delta:

$$
\delta_k = \begin{cases} \Delta_k^{\text{BS}} - h_k^- & \text{if } \delta_{k-1} < \Delta_k^{\text{BS}} - h_k^- \\ \delta_{k-1} & \text{if } \Delta_k^{\text{BS}} - h_k^- \leq \delta_{k-1} \leq \Delta_k^{\text{BS}} + h_k^+ \\ \Delta_k^{\text{BS}} + h_k^+ & \text{if } \delta_{k-1} > \Delta_k^{\text{BS}} + h_k^+
\end{cases}
$$

The bandwidth $h_k^\pm$ depends on $\kappa$, $\Gamma$, $\sigma$, and time to maturity. This reproduces the Whalley-Wilmott asymptotic result $h \propto (\kappa \sigma S^2 |\Gamma| / \lambda)^{1/3}$.

### Empirical Performance

Under a Heston model with weekly rebalancing and $\kappa = 0.001$:

| Method | Mean P&L | Std P&L | Sharpe | Total Costs |
|---|---|---|---|---|
| Delta hedge (BS vol) | $-$0.12 | 1.85 | $-$0.065 | 0.42 |
| Delta hedge (true vol) | $-$0.08 | 1.52 | $-$0.053 | 0.48 |
| RL (mean-var) | $-$0.09 | 1.31 | $-$0.069 | 0.35 |
| RL (CVaR) | $-$0.15 | 1.24 | $-$0.121 | 0.31 |

The RL agent achieves lower P&L standard deviation by learning to:

- Trade less frequently (reducing costs)
- Hedge more aggressively near expiry (reducing gamma risk)
- Adapt to realized volatility (unlike the fixed-vol delta hedge)

---

## Model-Free and Model-Agnostic Hedging

### Training Under Model Uncertainty

A key advantage of RL hedging is **model agnosticism**. The agent can be trained under multiple models simultaneously:

1. Generate paths from GBM, Heston, and SABR with random parameters
2. Train the same agent across all model environments
3. The resulting policy is robust to model misspecification

### Historical Data Training

The agent can be trained directly on historical return data using experience replay:

1. Collect historical return sequences of length $N$
2. Compute option payoffs at the end of each sequence
3. Train the RL agent on these historical episodes

This produces a hedging policy that reflects the true (historical) distribution of returns, including jumps, heavy tails, and volatility clustering that parametric models may miss.

!!! tip "Connection to Deep Hedging"
    RL for option hedging and the deep hedging framework of Buehler et al. solve the same optimization problem from different perspectives. Deep hedging treats it as a single supervised optimization over all time steps simultaneously, while RL decomposes it into per-step decisions via Bellman recursion. In practice, the deep hedging approach often converges faster for fixed environments, while RL offers more flexibility for adaptive, multi-objective settings.

---

## Extensions

### Multi-Asset Hedging

For a portfolio of options on multiple underlyings, the state space expands to include all relevant prices, Greeks, and correlations. The RL agent learns cross-hedging strategies---using liquid instruments to hedge illiquid ones---automatically discovering optimal hedge ratios.

### Path-Dependent Options

For path-dependent payoffs (Asian, barrier, lookback options), the state must encode path-dependent features:

$$
s_k = \left(\frac{S_{t_k}}{K}, \; \frac{T - t_k}{T}, \; \delta_{k-1}, \; \bar{S}_k, \; S_k^{\max}, \; \hat{\sigma}_k\right)
$$

where $\bar{S}_k$ is the running average and $S_k^{\max}$ the running maximum. The RL agent learns hedging strategies that classical delta hedging cannot provide without solving a high-dimensional PDE.

---

## Key Takeaways

1. **Option hedging** under discrete rebalancing and transaction costs is naturally a sequential decision problem amenable to RL.

2. In frictionless Black-Scholes, the RL agent **recovers delta hedging**; with frictions, it discovers **no-trade bands** consistent with asymptotic theory.

3. **Risk-sensitive objectives** (mean-variance, CVaR, entropic) produce different hedging behaviors, with CVaR-optimized agents being most conservative in the tails.

4. **Model-free training** on historical data or across multiple models produces robust hedging policies that outperform model-dependent delta hedging under misspecification.

5. RL naturally extends to **multi-asset** and **path-dependent** hedging problems where analytical solutions are unavailable.

---

## Further Reading

- Kolm & Ritter (2019), "Dynamic Replication and Hedging: A Reinforcement Learning Approach"
- Cao, Chen, Hull & Poulos (2021), "Deep Hedging of Derivatives Using Reinforcement Learning"
- Buehler, Gonon, Maystre & Niedermeyer (2019), "Deep Hedging"
- Whalley & Wilmott (1997), "An Asymptotic Analysis of the Davis, Panas & Zariphopoulou Model for Option Pricing with Transaction Costs"
- Halperin (2020), "QLBS: Q-Learner in the Black-Scholes (-Merton) Worlds"
