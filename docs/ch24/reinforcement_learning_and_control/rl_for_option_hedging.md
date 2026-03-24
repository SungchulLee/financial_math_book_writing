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

---

## Exercises

**Exercise 1.** Consider delta hedging a European call with $S_0 = 100$, $K = 100$, $T = 1/12$ (one month), $\sigma = 0.20$, $r = 0$, with weekly rebalancing ($N = 4$). (a) Compute the Black-Scholes delta $\Delta_0 = \Phi(d_1)$ at $t = 0$. (b) After one week, $S_1 = 103$. Compute $\Delta_1$ and the rebalancing trade $|\Delta_1 - \Delta_0| \cdot S_1$. With proportional transaction cost $\kappa = 0.001$, compute the cost. (c) After all 4 weeks with price path $S = (100, 103, 101, 105, 108)$, compute the total hedging P&L: $\sum_{k=0}^3 \Delta_k(S_{k+1} - S_k) - (S_4 - K)^+$. Is the hedge perfect?

---

**Exercise 2.** The RL hedging reward is $r_k = \delta_k(S_{t_{k+1}} - S_{t_k}) - \kappa |S_{t_k}||\delta_k - \delta_{k-1}|$ with terminal payoff $r_N = -(S_T - K)^+$. (a) Write the total return $G = \sum_{k=0}^N r_k$ and explain why $G$ represents the hedging P&L (hedge gains minus costs minus option payoff). (b) A risk-neutral RL agent maximizes $\mathbb{E}[G]$. Show that this is equivalent to maximizing the expected P&L of the hedging strategy. (c) A risk-sensitive agent maximizes $\mathbb{E}[G] - \frac{\lambda}{2}\text{Var}[G]$. Explain why this is more appropriate for hedging: it penalizes variability in the P&L, which is exactly what a hedger cares about.

---

**Exercise 3.** In the Black-Scholes model with zero transaction costs and continuous rebalancing, the RL agent should recover the delta hedge. (a) Argue that the delta hedge achieves $\text{Var}[G] = 0$ (perfect replication), so it is optimal for any risk-averse objective. (b) In the RL training, set $\kappa = 0$ and $N = 100$ (frequent rebalancing). After training, compare the learned hedge ratio $\delta_k^{\text{RL}}$ with the Black-Scholes delta $\Delta_k^{\text{BS}}$ at several time points and moneyness levels. They should approximately agree. (c) Now introduce $\kappa = 0.002$. The RL agent should learn a no-trade band. Describe qualitatively how the learned policy differs from delta hedging.

---

**Exercise 4.** The Whalley-Wilmott no-trade bandwidth is $h \propto (\kappa \sigma S^2 |\Gamma| / \lambda)^{1/3}$. (a) For $\kappa = 0.001$, $\sigma = 0.20$, $S = 100$, $\Gamma = 0.04$ (near-the-money), and $\lambda = 1$, compute $h$. (b) The bandwidth is wider when $\Gamma$ is large (near-the-money, near expiry). Explain why: high gamma means frequent rebalancing under delta hedging, so the cost savings from not rebalancing are largest here. (c) The RL agent should discover this bandwidth automatically. Design a test: plot the learned $\delta_k$ against $\Delta_k^{\text{BS}}$ for 1000 test paths and verify that the agent trades only when $|\delta_{k-1} - \Delta_k^{\text{BS}}| > h$ approximately.

---

**Exercise 5.** An RL hedging agent is trained under a Heston model but tested under GBM. (a) Describe the model mismatch: Heston has stochastic volatility and volatility clustering, while GBM has constant volatility. (b) A delta hedge using the true GBM volatility is optimal under GBM. The RL agent, trained under Heston, has learned to adapt to changing volatility. Under GBM, this adaptation is unnecessary. Does the RL agent underperform delta hedging under GBM? (c) Now consider the reverse: the agent is trained under GBM but tested under Heston. The GBM-trained agent does not adapt to volatility changes. Show that the RL agent trained under multiple models (GBM + Heston + SABR) outperforms single-model agents under misspecification.

---

**Exercise 6.** For path-dependent options, the state must encode path-dependent features. Consider hedging an Asian call with payoff $(\bar{S}_T - K)^+$ where $\bar{S}_T = \frac{1}{N}\sum_{k=0}^{N-1} S_{t_k}$. (a) The state includes the running average $\bar{S}_k = \frac{1}{k}\sum_{j=0}^{k-1} S_{t_j}$. Explain why this is sufficient for the Markov property. (b) There is no simple delta formula for Asian options (the PDE is two-dimensional). The RL agent learns the hedge directly. Discuss the advantage of RL over analytical methods here. (c) Compare the RL hedging P&L variance with a naive delta hedge using $\Delta^{\text{BS}}$ of a European call with the same strike. Which has lower variance?

---

**Exercise 7.** The deep hedging framework and RL for hedging solve the same problem from different perspectives. Deep hedging parameterizes the entire hedging strategy $(\delta_0, \delta_1, \ldots, \delta_{N-1})$ as functions of the state and optimizes the risk measure over all time steps simultaneously. RL decomposes the problem into per-step decisions via the Bellman equation. (a) Explain why deep hedging can be viewed as a "direct" optimization while RL is an "indirect" approach that first learns a value function. (b) Deep hedging typically converges faster for a fixed environment because it optimizes the entire trajectory at once. Why might RL be preferable when the environment changes (e.g., different option maturities, different underlyings)? (c) Propose a hybrid: use deep hedging for the initial training and RL for online fine-tuning as market conditions evolve.
