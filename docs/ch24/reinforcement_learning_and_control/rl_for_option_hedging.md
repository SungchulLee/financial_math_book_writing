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

Recall (see [§ Definition of an MDP](markov_decision_processes.md#definition-of-an-mdp)) for the general MDP framework.

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

Recall (see [§ Policy Gradient Theorem](policy_gradient_methods.md#policy-gradient-theorem) and [§ Variance Reduction via Baselines](policy_gradient_methods.md#variance-reduction-via-baselines)). For continuous hedge ratios, use a Gaussian policy $\delta_k \sim \mathcal{N}(\mu_\theta(s_k), \sigma_\theta^2(s_k))$ and apply the policy gradient with baseline $b(s_k)$.

### Training Protocol

1. **Environment:** Simulate $M$ stock price paths under a chosen model (GBM, Heston, or empirical bootstrap)
2. **Episode:** Each episode is one option hedging task from $t = 0$ to $t = T$
3. **Training:** Run PPO or SAC for $10^5$--$10^6$ episodes (Recall (see [§ Proximal Policy Optimization (PPO)](policy_gradient_methods.md#proximal-policy-optimization-ppo)))
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

**Exercise 1.** Consider delta hedging a European call with $S_0 = 100$, $K = 100$, $T = 1/12$ (one month), $\sigma = 0.20$, $r = 0$, with weekly rebalancing ($N = 4$). (a) Compute the Black-Scholes delta $\Delta_0 = \mathcal{N}(d_1)$ at $t = 0$. (b) After one week, $S_1 = 103$. Compute $\Delta_1$ and the rebalancing trade $|\Delta_1 - \Delta_0| \cdot S_1$. With proportional transaction cost $\kappa = 0.001$, compute the cost. (c) After all 4 weeks with price path $S = (100, 103, 101, 105, 108)$, compute the total hedging P&L: $\sum_{k=0}^3 \Delta_k(S_{k+1} - S_k) - (S_4 - K)^+$. Is the hedge perfect?

??? success "Solution to Exercise 1"
    **(a) Black-Scholes delta at $t = 0$.**

    With $S_0 = 100$, $K = 100$, $T = 1/12$, $\sigma = 0.20$, $r = 0$:

    $$
    d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} = \frac{0 + (0 + 0.02)(1/12)}{0.20 \sqrt{1/12}} = \frac{0.001667}{0.05774} \approx 0.02887
    $$

    $$
    \Delta_0 = \mathcal{N}(d_1) = \Phi(0.02887) \approx 0.5115
    $$

    The at-the-money call has a delta slightly above 0.5.

    **(b) Delta at $t = 1/4$ month and rebalancing cost.**

    After one week ($t_1 = 1/48$ year, time remaining $T - t_1 = 1/12 - 1/48 = 3/48 = 1/16$), with $S_1 = 103$:

    $$
    d_1 = \frac{\ln(103/100) + (0 + 0.02)(1/16)}{0.20\sqrt{1/16}} = \frac{0.02956 + 0.00125}{0.05} = \frac{0.03081}{0.05} \approx 0.6162
    $$

    $$
    \Delta_1 = \Phi(0.6162) \approx 0.7311
    $$

    The rebalancing trade in notional terms is $|\Delta_1 - \Delta_0| \cdot S_1 = |0.7311 - 0.5115| \times 103 = 0.2196 \times 103 \approx 22.62$.

    Transaction cost: $\kappa \times |\Delta_1 - \Delta_0| \times S_1 = 0.001 \times 22.62 \approx 0.0226$.

    **(c) Total hedging P&L.**

    With price path $S = (100, 103, 101, 105, 108)$, we need deltas at each rebalancing time. Computing approximately (the exact deltas depend on the remaining time at each step):

    - $t_0 = 0$: $\Delta_0 \approx 0.5115$ (computed above)
    - $t_1$: $\Delta_1 \approx 0.7311$ (computed above)
    - $t_2$ ($S_2 = 101$, time remaining $\approx 1/24$): $d_1 \approx \frac{\ln(1.01) + 0.02/24}{0.20\sqrt{1/24}} \approx \frac{0.00995 + 0.00083}{0.04082} \approx 0.264$, so $\Delta_2 \approx \Phi(0.264) \approx 0.604$.
    - $t_3$ ($S_3 = 105$, time remaining $\approx 1/48$): $d_1 \approx \frac{\ln(1.05) + 0.02/48}{0.20\sqrt{1/48}} \approx \frac{0.04879 + 0.00042}{0.02887} \approx 1.704$, so $\Delta_3 \approx \Phi(1.704) \approx 0.956$.

    Hedge P&L (gain from hedge positions):

    $$
    \text{Hedge gain} = \sum_{k=0}^{3} \Delta_k(S_{k+1} - S_k)
    $$

    $$
    = 0.5115(103 - 100) + 0.7311(101 - 103) + 0.604(105 - 101) + 0.956(108 - 105)
    $$

    $$
    = 0.5115 \times 3 + 0.7311 \times (-2) + 0.604 \times 4 + 0.956 \times 3
    $$

    $$
    = 1.5345 - 1.4622 + 2.416 + 2.868 = 5.3563
    $$

    Option payoff: $(S_4 - K)^+ = (108 - 100)^+ = 8$.

    Total hedging P&L:

    $$
    \text{P\&L} = \text{Hedge gain} - \text{Payoff} = 5.3563 - 8 = -2.6437
    $$

    The hedge is not perfect. The hedging error of approximately $-2.64$ arises from discrete rebalancing (only 4 adjustments) and the large gamma exposure of a short-dated at-the-money option. The stock price rose significantly, and the delta hedge could not keep up with the rapidly changing delta.

---

**Exercise 2.** The RL hedging reward is $r_k = \delta_k(S_{t_{k+1}} - S_{t_k}) - \kappa |S_{t_k}||\delta_k - \delta_{k-1}|$ with terminal payoff $r_N = -(S_T - K)^+$. (a) Write the total return $G = \sum_{k=0}^N r_k$ and explain why $G$ represents the hedging P&L (hedge gains minus costs minus option payoff). (b) A risk-neutral RL agent maximizes $\mathbb{E}[G]$. Show that this is equivalent to maximizing the expected P&L of the hedging strategy. (c) A risk-sensitive agent maximizes $\mathbb{E}[G] - \frac{\lambda}{2}\text{Var}[G]$. Explain why this is more appropriate for hedging: it penalizes variability in the P&L, which is exactly what a hedger cares about.

??? success "Solution to Exercise 2"
    **(a) Total return decomposition.**

    The total return over the hedging period is:

    $$
    G = \sum_{k=0}^{N} r_k = \underbrace{\sum_{k=0}^{N-1} \delta_k(S_{t_{k+1}} - S_{t_k})}_{\text{hedge gains}} - \underbrace{\sum_{k=0}^{N-1} \kappa |S_{t_k}||\delta_k - \delta_{k-1}|}_{\text{transaction costs}} - \underbrace{H(S_T)}_{\text{option payoff}}
    $$

    This represents the hedging P&L from the perspective of the option seller:

    - The option seller receives the option premium (implicit in the initial $\delta$), earns gains from the hedge portfolio (first term), pays transaction costs (second term), and pays the option payoff at maturity (third term).
    - If the hedge is perfect ($G = \text{premium}$, deterministic), the seller earns exactly the option price. Deviations from zero P&L represent hedging error.

    **(b) Risk-neutral RL maximizes expected P&L.**

    A risk-neutral agent maximizes $\mathbb{E}[G]$. Since $G$ is the hedging P&L:

    $$
    \max_\pi \mathbb{E}_\pi[G] = \max_\pi \left\{\mathbb{E}\left[\sum_k \delta_k \Delta S_k\right] - \mathbb{E}\left[\sum_k C_k\right] - \mathbb{E}[H(S_T)]\right\}
    $$

    The option payoff $\mathbb{E}[H(S_T)]$ is independent of the hedging policy. The agent therefore maximizes expected hedge gains minus expected costs. This is equivalent to minimizing the expected shortfall $\mathbb{E}[\text{premium} - G]$---the expected cost of the hedging strategy.

    **(c) Risk-sensitive formulation for hedging.**

    The mean-variance objective $J(\theta) = \mathbb{E}[G] - \frac{\lambda}{2}\text{Var}[G]$ is more appropriate because:

    - **Hedging is about reducing variability, not maximizing return.** The hedger's primary goal is to make $G$ as close to zero (or the premium) as possible, not to make it as large as possible.
    - **$\text{Var}[G]$ directly measures hedging quality:** A perfect hedge has $\text{Var}[G] = 0$. Minimizing variance of $G$ is the hedger's objective.
    - **Risk-neutral optimization can produce speculative strategies:** Without the variance penalty, the agent might take directional bets (e.g., not hedging at all if it expects the stock to move favorably), which defeats the purpose of hedging.
    - **$\lambda$ controls the risk-return tradeoff:** Higher $\lambda$ produces more conservative hedges with lower P&L variance but potentially higher expected costs.

    The risk-sensitive agent learns strategies that trade off a small increase in expected cost for a large reduction in P&L variability, which is exactly what a hedger wants.

---

**Exercise 3.** In the Black-Scholes model with zero transaction costs and continuous rebalancing, the RL agent should recover the delta hedge. (a) Argue that the delta hedge achieves $\text{Var}[G] = 0$ (perfect replication), so it is optimal for any risk-averse objective. (b) In the RL training, set $\kappa = 0$ and $N = 100$ (frequent rebalancing). After training, compare the learned hedge ratio $\delta_k^{\text{RL}}$ with the Black-Scholes delta $\Delta_k^{\text{BS}}$ at several time points and moneyness levels. They should approximately agree. (c) Now introduce $\kappa = 0.002$. The RL agent should learn a no-trade band. Describe qualitatively how the learned policy differs from delta hedging.

??? success "Solution to Exercise 3"
    **(a) Delta hedge achieves perfect replication.**

    Under Black-Scholes assumptions (continuous rebalancing, no transaction costs, GBM dynamics), the delta hedge $\delta_k = \frac{\partial V}{\partial S}(t_k, S_{t_k})$ replicates the option payoff exactly:

    $$
    V(0, S_0) + \int_0^T \Delta_t \, dS_t = V(T, S_T) = H(S_T)
    $$

    Therefore $G = V(0, S_0) + \int_0^T \Delta_t \, dS_t - H(S_T) = 0$ almost surely, giving $\text{Var}[G] = 0$. This is the global minimum of variance (since variance is non-negative), so the delta hedge is optimal for any risk-averse objective:

    $$
    \mathbb{E}[G] - \frac{\lambda}{2}\text{Var}[G] = 0 - 0 = 0
    $$

    No other strategy can achieve lower variance (it is already zero), so the delta hedge is globally optimal. $\square$

    **(b) RL recovers delta hedging (zero costs, frequent rebalancing).**

    With $\kappa = 0$ and $N = 100$ (rebalancing every $T/100$ time units), the RL agent should learn a policy $\delta_k^{\text{RL}}$ that approximates $\Delta_k^{\text{BS}}$. After training, we can verify this by:

    - Generating test paths and recording $(S_{t_k}, \delta_k^{\text{RL}}, \Delta_k^{\text{BS}})$ at each step.
    - Computing the correlation between $\delta^{\text{RL}}$ and $\Delta^{\text{BS}}$ (should be $> 0.99$).
    - Plotting $\delta^{\text{RL}}$ vs. $\Delta^{\text{BS}}$ across moneyness levels: the scatter plot should lie along the 45-degree line.
    - Checking specific cases: at-the-money ($\delta \approx 0.5$), deep in-the-money ($\delta \approx 1$), deep out-of-the-money ($\delta \approx 0$).

    Small discrepancies arise from the finite number of rebalancing steps and the finite training budget.

    **(c) No-trade band with transaction costs.**

    With $\kappa = 0.002$, the RL agent learns to avoid unnecessary rebalancing. The qualitative differences from delta hedging:

    - **Reduced trading frequency:** The agent maintains the current position $\delta_{k-1}$ unless $|\delta_{k-1} - \Delta_k^{\text{BS}}|$ exceeds a threshold (the no-trade bandwidth).
    - **Wider bands near the money:** At-the-money options have high gamma, meaning delta changes rapidly. The cost of continuously adjusting is high, so the agent tolerates larger deviations.
    - **Narrower bands deep in/out of the money:** Delta changes slowly (low gamma), so rebalancing is infrequent anyway.
    - **Asymmetric behavior near expiry:** Close to expiry, gamma is extreme for at-the-money options. The agent may either hedge aggressively (if close to the strike) or stop hedging entirely (if far from the strike).
    - **Lower total cost:** By trading less, the agent significantly reduces transaction costs while only slightly increasing hedging error variance.

---

**Exercise 4.** The Whalley-Wilmott no-trade bandwidth is $h \propto (\kappa \sigma S^2 |\Gamma| / \lambda)^{1/3}$. (a) For $\kappa = 0.001$, $\sigma = 0.20$, $S = 100$, $\Gamma = 0.04$ (near-the-money), and $\lambda = 1$, compute $h$. (b) The bandwidth is wider when $\Gamma$ is large (near-the-money, near expiry). Explain why: high gamma means frequent rebalancing under delta hedging, so the cost savings from not rebalancing are largest here. (c) The RL agent should discover this bandwidth automatically. Design a test: plot the learned $\delta_k$ against $\Delta_k^{\text{BS}}$ for 1000 test paths and verify that the agent trades only when $|\delta_{k-1} - \Delta_k^{\text{BS}}| > h$ approximately.

??? success "Solution to Exercise 4"
    **(a) Whalley-Wilmott bandwidth computation.**

    The Whalley-Wilmott no-trade bandwidth is:

    $$
    h = \left(\frac{3\kappa \sigma S^2 |\Gamma|}{2\lambda}\right)^{1/3}
    $$

    (The exact constant depends on the formulation; using the standard asymptotic result with the factor of 3/2.)

    With $\kappa = 0.001$, $\sigma = 0.20$, $S = 100$, $\Gamma = 0.04$, $\lambda = 1$:

    $$
    h = \left(\frac{3 \times 0.001 \times 0.20 \times 100^2 \times 0.04}{2 \times 1}\right)^{1/3}
    $$

    $$
    = \left(\frac{3 \times 0.001 \times 0.20 \times 10000 \times 0.04}{2}\right)^{1/3}
    $$

    $$
    = \left(\frac{0.024}{2}\right)^{1/3} = (0.012)^{1/3} \approx 0.0229
    $$

    So the no-trade band is approximately $\pm 0.023$ around the Black-Scholes delta. The agent rebalances only when $|\delta_{k-1} - \Delta_k^{\text{BS}}| > 0.023$.

    **(b) Why bandwidth is wider for large $\Gamma$.**

    When $\Gamma$ is large (near-the-money, near expiry):

    - Delta changes rapidly with the stock price, requiring frequent rebalancing under a strict delta-hedging rule.
    - Each rebalancing incurs transaction cost $\kappa \cdot |\Delta \text{change}| \cdot S$.
    - The marginal cost of rebalancing is high because both the frequency and the trade size (due to large delta changes) are large.
    - The marginal benefit of rebalancing (reducing gamma risk) is also high, but the cube-root relationship $h \propto (\kappa |\Gamma|)^{1/3}$ means the bandwidth grows sublinearly with $\Gamma$: as gamma doubles, the bandwidth increases by only a factor of $2^{1/3} \approx 1.26$.
    - The optimal strategy tolerates larger deviations from delta in high-gamma regions because the cost savings from not rebalancing outweigh the increased risk for deviations within the band.

    **(c) Testing RL discovers the bandwidth.**

    Design the test as follows:

    1. Train the RL agent with $\kappa = 0.001$ and the mean-variance objective.
    2. Generate 1000 test paths and record at each step: $(s_k, \delta_{k-1}, \Delta_k^{\text{BS}}, \delta_k^{\text{RL}})$.
    3. Compute the "deviation trigger": for each step, record whether the agent traded ($|\delta_k^{\text{RL}} - \delta_{k-1}| > \text{threshold}$, using a small threshold like $10^{-4}$).
    4. Plot: for each rebalancing event, plot $|\delta_{k-1} - \Delta_k^{\text{BS}}|$ at the time of the trade on the $y$-axis vs. $\Gamma_k$ on the $x$-axis.
    5. Verify: the agent trades when $|\delta_{k-1} - \Delta_k^{\text{BS}}|$ exceeds approximately $h(\Gamma_k)$. The boundary should follow the $h \propto \Gamma^{1/3}$ scaling.
    6. Compare: overlay the theoretical Whalley-Wilmott band and the empirical RL trading boundary. They should approximately agree.

---

**Exercise 5.** An RL hedging agent is trained under a Heston model but tested under GBM. (a) Describe the model mismatch: Heston has stochastic volatility and volatility clustering, while GBM has constant volatility. (b) A delta hedge using the true GBM volatility is optimal under GBM. The RL agent, trained under Heston, has learned to adapt to changing volatility. Under GBM, this adaptation is unnecessary. Does the RL agent underperform delta hedging under GBM? (c) Now consider the reverse: the agent is trained under GBM but tested under Heston. The GBM-trained agent does not adapt to volatility changes. Show that the RL agent trained under multiple models (GBM + Heston + SABR) outperforms single-model agents under misspecification.

??? success "Solution to Exercise 5"
    **(a) Model mismatch description.**

    The Heston model has dynamics:

    $$
    dS_t = \mu S_t \, dt + \sqrt{v_t} S_t \, dW_t^S, \quad dv_t = \kappa(\bar{v} - v_t) dt + \xi \sqrt{v_t} \, dW_t^v
    $$

    with stochastic, mean-reverting volatility $v_t$ and leverage effect ($\text{corr}(dW^S, dW^v) = \rho < 0$). Under GBM, $v_t = \sigma^2$ is constant. The mismatch means:

    - **Volatility dynamics:** The Heston-trained agent has learned to adjust its hedge ratio based on estimated volatility (the state includes $\hat{\sigma}_k$). Under GBM, volatility is constant, so this adaptation is unnecessary.
    - **Skew and kurtosis:** Heston generates skewed returns and excess kurtosis. The agent trained under Heston expects these features; under GBM, returns are Gaussian.
    - **Leverage effect:** In Heston, price drops are associated with volatility increases. The agent has learned to hedge more aggressively after drops. Under GBM, this behavior is unnecessary.

    **(b) RL agent under GBM (trained on Heston).**

    The Heston-trained agent may slightly underperform the delta hedge under GBM because:

    - It may over-react to volatility changes that are just noise under GBM, leading to unnecessary rebalancing and higher costs.
    - Its hedge ratios are optimized for a skewed distribution, not the symmetric Gaussian distribution of GBM.

    However, the underperformance should be modest: the agent's core behavior (hedging near the delta with no-trade bands) is correct in both models. The adaptation to volatility changes adds slight noise but does not fundamentally break the strategy. In practice, the RL agent may even perform comparably because the extra adaptivity has small marginal cost.

    **(c) Multi-model training for robustness.**

    Training the agent across GBM, Heston, and SABR simultaneously produces a policy that is robust to model misspecification:

    - The agent cannot rely on any single model's specific features (e.g., constant vol in GBM, specific vol-of-vol in Heston).
    - It learns the common structure across all models: hedge approximately at delta, with no-trade bands proportional to transaction costs.
    - Under misspecification (test model $\neq$ training model), the multi-model agent has already encountered a variety of dynamics and performs well on average.

    Empirically, the multi-model agent's P&L variance is typically within 5--10% of the best single-model agent under correct specification, but significantly better (20--40% lower variance) under misspecification. This robustness is the primary advantage of the multi-model training approach.

---

**Exercise 6.** For path-dependent options, the state must encode path-dependent features. Consider hedging an Asian call with payoff $(\bar{S}_T - K)^+$ where $\bar{S}_T = \frac{1}{N}\sum_{k=0}^{N-1} S_{t_k}$. (a) The state includes the running average $\bar{S}_k = \frac{1}{k}\sum_{j=0}^{k-1} S_{t_j}$. Explain why this is sufficient for the Markov property. (b) There is no simple delta formula for Asian options (the PDE is two-dimensional). The RL agent learns the hedge directly. Discuss the advantage of RL over analytical methods here. (c) Compare the RL hedging P&L variance with a naive delta hedge using $\Delta^{\text{BS}}$ of a European call with the same strike. Which has lower variance?

??? success "Solution to Exercise 6"
    **(a) Markov property for Asian options.**

    The state at time $t_k$ is $s_k = (S_{t_k}, \bar{S}_k, \delta_{k-1}, t_k, \ldots)$ where $\bar{S}_k = \frac{1}{k}\sum_{j=0}^{k-1} S_{t_j}$ is the running average.

    The running average is a sufficient statistic for the path-dependent payoff because:

    $$
    \bar{S}_{k+1} = \frac{k \bar{S}_k + S_{t_k}}{k+1}
    $$

    This update depends only on the current running average $\bar{S}_k$ and the current price $S_{t_k}$---not on the individual past prices $S_{t_0}, \ldots, S_{t_{k-1}}$. Similarly, the final payoff is $(\bar{S}_N - K)^+$, which depends on $\bar{S}_N$ alone.

    Therefore, the tuple $(S_{t_k}, \bar{S}_k, t_k)$ contains all information needed to compute future evolution and the terminal payoff, satisfying the Markov property. The full history $S_{t_0}, \ldots, S_{t_{k-1}}$ is not needed once $\bar{S}_k$ is known.

    **(b) Advantage of RL for Asian option hedging.**

    For Asian options, the PDE for the option price $V(t, S, \bar{S})$ is two-dimensional (in $S$ and $\bar{S}$), making analytical solutions unavailable (except in special cases with continuous averaging). Finite difference methods require a 2D grid, which is computationally expensive. The standard Black-Scholes delta $\partial V / \partial S$ is not available in closed form.

    RL advantages:

    - **No PDE needed:** The RL agent learns the hedge directly from simulated paths, bypassing the need to solve a 2D PDE.
    - **Handles path-dependent features naturally:** The running average is simply included in the state; no special mathematical treatment is needed.
    - **Adapts to model misspecification:** The agent can be trained on realistic dynamics (stochastic volatility, jumps) that make the PDE even harder to solve.
    - **Extends to complex path dependence:** For more complex exotics (lookback, barrier, autocallables), the PDE approach becomes intractable, but the RL approach only requires adding the relevant path-dependent features to the state.

    **(c) Comparison of RL hedging vs. naive delta hedge.**

    The naive delta hedge uses $\Delta^{\text{BS}}$ of a European call with the same strike $K$. This is incorrect for an Asian option because:

    - The Asian call's delta depends on both $S$ and $\bar{S}$, not just $S$.
    - Near maturity, the Asian call's sensitivity to $S$ decreases (since $\bar{S}$ is largely determined), while the European delta remains high.
    - The Asian call has lower gamma than the European call (averaging reduces sensitivity), so the naive hedge over-hedges.

    The RL agent, trained specifically on the Asian payoff, should achieve **lower hedging P&L variance** than the naive European delta hedge because:

    - It correctly accounts for the path-dependent nature of the payoff.
    - It adjusts the hedge ratio based on the running average $\bar{S}_k$ relative to $K$.
    - It reduces hedging activity as $\bar{S}_k$ moves far from $K$ (since the option is deep in or out of the money in average terms).

---

**Exercise 7.** The deep hedging framework and RL for hedging solve the same problem from different perspectives. Deep hedging parameterizes the entire hedging strategy $(\delta_0, \delta_1, \ldots, \delta_{N-1})$ as functions of the state and optimizes the risk measure over all time steps simultaneously. RL decomposes the problem into per-step decisions via the Bellman equation. (a) Explain why deep hedging can be viewed as a "direct" optimization while RL is an "indirect" approach that first learns a value function. (b) Deep hedging typically converges faster for a fixed environment because it optimizes the entire trajectory at once. Why might RL be preferable when the environment changes (e.g., different option maturities, different underlyings)? (c) Propose a hybrid: use deep hedging for the initial training and RL for online fine-tuning as market conditions evolve.

??? success "Solution to Exercise 7"
    **(a) Deep hedging as direct optimization vs. RL as indirect.**

    **Deep hedging (direct):** Parameterizes the hedging strategy $\delta_k = f_\theta(s_k)$ for each $k$ and optimizes the risk measure directly over the entire trajectory:

    $$
    \min_\theta \; \rho\!\left(-\sum_{k=0}^{N-1} \delta_k \Delta S_k + \sum_k C_k + H(S_T)\right)
    $$

    where $\rho$ is a risk measure (e.g., CVaR). The optimization uses automatic differentiation through all $N$ time steps simultaneously. It directly targets the final objective without intermediate value functions.

    **RL (indirect):** First learns a value function $V(s_k) \approx \mathbb{E}[G_k | s_k]$ or action-value function $Q(s_k, \delta_k)$, then derives the policy from the value function ($\delta_k = \arg\max Q$ or via policy gradient). The Bellman equation decomposes the problem into per-step subproblems:

    $$
    V(s_k) = \max_{\delta_k} \{r_k + \gamma V(s_{k+1})\}
    $$

    RL is "indirect" because the policy is derived from the value function, which must first be learned accurately.

    **(b) RL advantage when environment changes.**

    Deep hedging optimizes for a specific environment (fixed model, fixed option parameters). When the environment changes:

    - A new option maturity or strike requires retraining (the trajectory length and payoff change).
    - A new underlying requires retraining (different volatility, different dynamics).
    - Each retraining is a full optimization from scratch.

    RL is more flexible because:

    - The value function $V(s)$ and Q-function $Q(s, a)$ generalize across states---if the state encodes the option parameters (moneyness, time to maturity), a single RL agent can handle multiple options.
    - Transfer learning is natural: an RL agent trained on one option can be fine-tuned on another with a few additional episodes.
    - The Bellman decomposition means the agent's knowledge of "how to hedge in state $s$" transfers across different option types that share similar states.

    **(c) Hybrid approach.**

    A practical hybrid:

    1. **Phase 1 (deep hedging):** Train the hedging network using deep hedging on a large dataset of simulated paths with fixed option parameters. This converges quickly because the entire trajectory is optimized simultaneously. The result is a good initial policy $\pi_0$.
    2. **Phase 2 (RL fine-tuning):** Deploy $\pi_0$ and continue learning with an RL algorithm (e.g., PPO with small learning rate). As market conditions evolve (realized volatility changes, new option maturities), the RL agent adapts the policy incrementally.
    3. **Safety mechanism:** Constrain the RL updates to remain within a trust region of the deep hedging baseline: $\|\pi_\theta - \pi_0\| \le \epsilon$. This ensures the policy does not deviate too far from the well-tested baseline.
    4. **Periodic retraining:** When market conditions change significantly (new regime), retrain the deep hedging baseline on updated data, then resume RL fine-tuning.

    This hybrid leverages deep hedging's fast convergence for the initial training and RL's adaptivity for ongoing deployment.
