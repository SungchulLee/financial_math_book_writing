# Hedging Under Transaction Costs


## Introduction


In frictionless markets, the Black-Scholes delta-hedging strategy perfectly replicates any European option payoff through continuous rebalancing. In practice, every trade incurs a cost --- brokerage fees, bid-ask spreads, market impact --- and continuous rebalancing generates **infinite transaction costs**. This fundamental tension between hedging accuracy and trading costs is one of the most practically important problems in quantitative finance.

The study of hedging under transaction costs intersects with model uncertainty in a profound way: as Leland (1985) first observed, the presence of proportional transaction costs leads to a **modified volatility** that effectively widens the uncertainty about the true dynamics. Moreover, the super-replication price under transaction costs turns out to be trivially expensive in many settings, motivating the development of asymptotic and approximate hedging strategies that balance replication error against trading costs.

This section develops the theory from the Leland hedging approach through modern results on super-replication, consistent price systems, and the connection to robust finance.

## Proportional Transaction Costs


### 1. Market Model with Costs


**Setup**: Consider a market with:

- A riskless bond with price $B_t = e^{rt}$ (or $B_t = 1$ when $r = 0$)
- A risky asset with mid-price process $(S_t)_{0 \leq t \leq T}$
- Proportional transaction cost rate $\varepsilon > 0$

**Bid-Ask Spread**: When buying or selling, the actual transaction prices are:

$$
\text{Ask price} = (1 + \varepsilon) S_t, \quad \text{Bid price} = (1 - \varepsilon) S_t
$$

so the round-trip cost of buying and immediately selling one share is $2\varepsilon S_t$.

**Portfolio Dynamics**: A self-financing portfolio with $\theta_t$ shares of stock and $\eta_t$ units of bond satisfies:

$$
d\eta_t = -(1 + \varepsilon) S_t \, d\theta_t^+ + (1 - \varepsilon) S_t \, d\theta_t^-
$$

where $\theta_t^+$ and $\theta_t^-$ denote the cumulative purchases and sales, so that $\theta_t = \theta_0 + \theta_t^+ - \theta_t^-$.

### 2. The Hedging Cost Problem


**Infinite Rebalancing Cost**: Under Black-Scholes dynamics $dS_t = \sigma S_t \, dW_t$ (with $r = 0$), a strategy that rebalances $N$ times over $[0,T]$ at equally spaced times incurs expected transaction costs of order:

$$
\mathbb{E}\left[\text{Total cost}\right] \approx \varepsilon \sum_{i=1}^N \mathbb{E}\left[S_{t_i} |\Delta \theta_{t_i}|\right] \sim \varepsilon \sqrt{N}
$$

for a delta-hedging strategy. As $N \to \infty$, the hedging error vanishes at rate $1/\sqrt{N}$ but the transaction costs grow at rate $\sqrt{N}$, leading to an infinite total cost in the continuous limit.

**The Fundamental Tradeoff**: Any practical hedging strategy must balance:

- **Replication error**: Decreases with more frequent rebalancing
- **Transaction costs**: Increases with more frequent rebalancing
- **Total hedging cost** = Replication error + Transaction costs

## The Leland Hedging Strategy


### 1. Leland's Approach


Leland (1985) proposed a modified delta-hedging strategy that accounts for transaction costs by adjusting the volatility parameter.

**Setup**: Consider hedging a European call option with payoff $(S_T - K)^+$ under Black-Scholes dynamics with volatility $\sigma$, proportional cost rate $\varepsilon$, and rebalancing at $N$ equally spaced times with $\delta t = T/N$.

**Modified Volatility**: Define the **Leland-adjusted volatility**:

$$
\hat{\sigma}^2 = \sigma^2\left(1 + \varepsilon \sqrt{\frac{8}{\pi \delta t}} \cdot \frac{1}{\sigma}\right) = \sigma^2 + \varepsilon \sigma \sqrt{\frac{8}{\pi \delta t}}
$$

**Leland Strategy**: At each rebalancing time $t_i$, hold:

$$
\theta_{t_i} = \frac{\partial \hat{C}}{\partial S}(t_i, S_{t_i})
$$

where $\hat{C}(t, S)$ is the Black-Scholes call price computed with the adjusted volatility $\hat{\sigma}$ instead of $\sigma$.

### 2. Intuition for the Adjustment


The adjustment $\hat{\sigma}^2 - \sigma^2 = \varepsilon \sigma \sqrt{8/(\pi \delta t)}$ compensates for the expected transaction costs at each rebalancing step. At each step, the expected cost is:

$$
\mathbb{E}[\varepsilon S_{t_i} |\Delta \theta_{t_i}|] \approx \varepsilon S_{t_i} \left|\frac{\partial^2 C}{\partial S^2}\right| \mathbb{E}[|\Delta S_{t_i}|] \approx \varepsilon S_{t_i}^2 \Gamma_{t_i} \sigma \sqrt{\frac{2 \delta t}{\pi}}
$$

where $\Gamma_{t_i} = \partial^2 C / \partial S^2$ is the option gamma. This matches the additional term in the modified Black-Scholes PDE when $\hat{\sigma}$ replaces $\sigma$.

### 3. The Modified PDE


The Leland-adjusted price $\hat{C}$ satisfies the **modified Black-Scholes equation**:

$$
\frac{\partial \hat{C}}{\partial t} + \frac{1}{2} \hat{\sigma}^2 S^2 \frac{\partial^2 \hat{C}}{\partial S^2} + r S \frac{\partial \hat{C}}{\partial S} - r \hat{C} = 0
$$

with terminal condition $\hat{C}(T, S) = (S - K)^+$.

Since $\hat{\sigma} > \sigma$, the adjusted price satisfies $\hat{C} > C$ for all $(t, S)$ with $t < T$, reflecting the additional cost of hedging. The excess $\hat{C}(0, S_0) - C(0, S_0)$ represents the transaction cost reserve.

### 4. Convergence: The Leland-Lott Theorem


**Theorem** (Leland, 1985; Lott, 1993): Under the Leland strategy with $N$ rebalancing steps, the hedging error (final portfolio value minus option payoff) satisfies:

$$
V_T^N - (S_T - K)^+ \xrightarrow{L^2} 0 \quad \text{as } N \to \infty
$$

provided that $\varepsilon = \varepsilon(N)$ scales appropriately with $N$. Specifically:

- If $\varepsilon \sqrt{N} \to \kappa \in (0, \infty)$ (transaction costs decrease as rebalancing increases), the strategy converges to perfect replication
- If $\varepsilon$ is fixed, the strategy does **not** converge to exact replication; instead, the residual hedging error is of order $O(\varepsilon)$

*Proof sketch*: Write the hedging error as:

$$
V_T^N - (S_T - K)^+ = \sum_{i=0}^{N-1} \left[\hat{C}(t_{i+1}, S_{t_{i+1}}) - \hat{C}(t_i, S_{t_i}) - \theta_{t_i}(S_{t_{i+1}} - S_{t_i}) - \varepsilon S_{t_i}|\Delta\theta_{t_i}|\right]
$$

By the discrete Ito formula and the choice of $\hat{\sigma}$, the terms involving the transaction cost and the second-order correction from the volatility adjustment cancel to leading order. The residual terms are of order $\delta t$ at each step, giving total error of order $N \cdot \delta t = T$ unless the cancellation is exact. A careful analysis using the PDE satisfied by $\hat{C}$ shows that the leading-order terms cancel, leaving $L^2$ convergence. $\square$

### 5. Limitations


The Leland approach has several well-known limitations:

1. **Gamma singularity**: Near expiry, the gamma of the call option becomes singular at the strike, causing the Leland adjustment to blow up. Refined treatments (Pergamenshchikov, 2003) handle this through careful analysis near the strike.

2. **Fixed costs**: When $\varepsilon$ is fixed (not shrinking with $N$), the Leland strategy does not perfectly replicate. The residual error is a genuine hedging cost.

3. **Non-convex payoffs**: For payoffs with negative gamma, the sign of the Leland adjustment must be reversed, leading to a **reduced** effective volatility. The general formula is:

$$
\hat{\sigma}^2 = \sigma^2 + \varepsilon \sigma \sqrt{\frac{8}{\pi \delta t}} \cdot \text{sign}(\Gamma)
$$

## Super-Replication Under Transaction Costs


### 1. The Super-Replication Problem


**Definition**: The **super-replication price** of a contingent claim $\Phi(S_T)$ under proportional transaction costs $\varepsilon$ is:

$$
V_\varepsilon^{\text{super}} = \inf\left\{x \in \mathbb{R} : \exists (\theta_t) \text{ self-financing s.t. } x + \int_0^T \theta_t \, dS_t - \varepsilon \int_0^T S_t \, |d\theta_t| \geq \Phi(S_T) \text{ a.s.}\right\}
$$

This is the smallest initial capital from which one can construct a portfolio that dominates the payoff after accounting for all transaction costs.

### 2. Trivial Super-Replication Bounds


**Theorem** (Soner-Shreve-Cvitanic, 1995): For a European call option under the Black-Scholes model with any proportional transaction cost $\varepsilon > 0$:

$$
V_\varepsilon^{\text{super}} = S_0
$$

That is, the super-replication price equals the current stock price, regardless of the strike, maturity, or cost level.

*Proof*: **Upper bound**: The strategy of buying one share at time 0 (cost $S_0$) and holding it until maturity gives terminal value $S_T \geq (S_T - K)^+$, costing $S_0$ plus one transaction cost. As $\varepsilon \to 0$, this approaches $S_0$.

**Lower bound**: Any super-replicating strategy must, in the worst case, be prepared for $S_T$ to be arbitrarily large. Under transaction costs, the strategy cannot be adjusted without cost, so it must hold at least one share at maturity. The cost of acquiring this share is at least $(1-\varepsilon) S_0$, which approaches $S_0$ as $\varepsilon \to 0$.

The rigorous proof uses the theory of viscosity solutions: the super-replication price satisfies a nonlinear PDE (the Black-Scholes-Barenblatt equation) with infinite effective volatility, whose solution is the stock price itself. $\square$

**Implication**: Super-replication is too expensive to be useful in practice. This motivates approximate hedging strategies that accept some residual risk.

### 3. The Black-Scholes-Barenblatt Equation


The super-replication price under uncertain volatility $\sigma \in [\underline{\sigma}, \overline{\sigma}]$ (a closely related problem) satisfies the **Black-Scholes-Barenblatt (BSB) equation**:

$$
\frac{\partial V}{\partial t} + \frac{1}{2} \Sigma(\Gamma)^2 S^2 \Gamma + rS\frac{\partial V}{\partial S} - rV = 0
$$

where $\Gamma = \partial^2 V / \partial S^2$ and the effective volatility is:

$$
\Sigma(\Gamma) = \begin{cases} \overline{\sigma} & \text{if } \Gamma \geq 0 \\ \underline{\sigma} & \text{if } \Gamma < 0 \end{cases}
$$

Under transaction costs, the effective volatility interval widens, and in the limit of continuous rebalancing, $\overline{\sigma} \to \infty$, recovering the trivial super-replication bound.

## Consistent Price Systems


### 1. No-Arbitrage with Transaction Costs


The fundamental theorem of asset pricing extends to markets with transaction costs, but the notion of equivalent martingale measure is replaced by **consistent price systems**.

**Definition** (Consistent Price System): A pair $(\tilde{S}, \mathbb{Q})$ is a $\varepsilon$-consistent price system (CPS) if:

1. $\mathbb{Q}$ is equivalent to $\mathbb{P}$
2. $\tilde{S}_t$ is a $\mathbb{Q}$-martingale
3. $(1-\varepsilon)S_t \leq \tilde{S}_t \leq (1+\varepsilon)S_t$ for all $t \in [0,T]$

The process $\tilde{S}$ lies within the bid-ask spread and is a martingale under $\mathbb{Q}$.

### 2. Fundamental Theorem with Costs


**Theorem** (Jouini-Kallal, 1995; Guasoni-Rasonyi-Schachermayer, 2008): The following are equivalent:

1. There is no arbitrage strategy with transaction costs (robust no free lunch with vanishing risk)
2. For every $\varepsilon' > \varepsilon$, there exists an $\varepsilon'$-consistent price system

**Significance**: Unlike the frictionless case, the set of consistent price systems forms a continuum parametrized by processes within the bid-ask spread. The super-replication price is:

$$
V_\varepsilon^{\text{super}} = \sup_{(\tilde{S}, \mathbb{Q}) \in \text{CPS}(\varepsilon)} \mathbb{E}_\mathbb{Q}[\Phi(\tilde{S}_T)]
$$

### 3. Connection to Robust Finance


The CPS framework connects directly to model uncertainty: the set of consistent price systems is an **ambiguity set** of models, all consistent with the observed bid-ask prices. The super-replication price is the worst-case expected payoff over this set, exactly paralleling the robust pricing framework.

**Proposition**: Let $\mathcal{Q}_\varepsilon$ denote the set of all risk-neutral measures arising from $\varepsilon$-CPS. Then:

$$
\mathcal{Q}_\varepsilon \subset \mathcal{Q}_{\varepsilon'} \quad \text{for } \varepsilon < \varepsilon'
$$

and

$$
\bigcap_{\varepsilon > 0} \mathcal{Q}_\varepsilon = \{\mathbb{Q}^*\}
$$

in complete markets, recovering the unique risk-neutral measure as transaction costs vanish.

## Asymptotic Hedging


### 1. The Whalley-Wilmott Approach


For small transaction costs, **asymptotic analysis** provides practical hedging strategies that balance replication error and costs.

**Theorem** (Whalley-Wilmott, 1997): For small $\varepsilon$, the optimal rebalancing strategy uses a **no-trade band** around the Black-Scholes delta:

$$
\theta_t \in \left[\Delta_t - H_t, \; \Delta_t + H_t\right]
$$

where $\Delta_t = \partial C / \partial S(t, S_t)$ is the Black-Scholes delta and the half-width of the band is:

$$
H_t = \left(\frac{3\varepsilon S_t^2 \Gamma_t^2 \sigma^2}{2\lambda}\right)^{1/3}
$$

Here $\lambda$ is the risk-aversion parameter trading off hedging error against transaction costs.

**Trading Rule**: Rebalance only when the current holding $\theta_t$ exits the band. When it does, trade the minimum amount to return to the boundary (not the center).

### 2. Utility-Based Asymptotic Hedging


**Setup**: An agent with exponential utility $U(x) = -e^{-\lambda x}$ hedges a short option position. The **utility indifference price** under transaction costs is:

$$
p_\varepsilon = \frac{1}{\lambda} \log \frac{\mathbb{E}[e^{-\lambda W_T^*}]}{\mathbb{E}[e^{-\lambda(W_T^{*,\Phi} - \Phi)}]}
$$

where $W_T^*$ is the optimal terminal wealth without the option and $W_T^{*,\Phi}$ is optimal wealth with the option liability.

**Asymptotic Expansion** (Barles-Soner, 1998): For small $\varepsilon$, the utility indifference price admits the expansion:

$$
p_\varepsilon = C_{\text{BS}} + \varepsilon^{2/3} \cdot p_1(t, S) + O(\varepsilon^{4/3})
$$

where $C_{\text{BS}}$ is the Black-Scholes price and $p_1$ is a correction term solving a nonlinear PDE. The leading correction scales as $\varepsilon^{2/3}$, not $\varepsilon$, reflecting the nonlinear interaction between hedging and costs.

### 3. The Kusuoka Limit


**Theorem** (Kusuoka, 1995): Consider a sequence of discrete-time hedging strategies with $N$ rebalancing points and proportional cost $\varepsilon_N$. If $\varepsilon_N N^{1/2} \to c \in (0, \infty)$, then the hedging error converges in distribution:

$$
\sqrt{N}\left(V_T^N - \Phi(S_T)\right) \xrightarrow{d} \mathcal{N}\left(0, \sigma_c^2\right)
$$

where $\sigma_c^2$ depends on the cost parameter $c$, the option gamma, and the underlying volatility. The limiting variance represents the irreducible cost of hedging with finite transaction costs.

## Hedging with Bid-Ask Spreads


### 1. General Bid-Ask Model


A more general framework replaces proportional costs with a **bid-ask spread model**.

**Definition**: The market is described by bid and ask price processes:

$$
S_t^{\text{bid}} \leq S_t^{\text{ask}}
$$

The **relative spread** is:

$$
\text{spread}_t = \frac{S_t^{\text{ask}} - S_t^{\text{bid}}}{S_t^{\text{mid}}}
$$

where $S_t^{\text{mid}} = (S_t^{\text{ask}} + S_t^{\text{bid}})/2$.

**Self-Financing Condition**: A portfolio $(\eta_t, \theta_t)$ is self-financing if:

$$
d\eta_t = -S_t^{\text{ask}} \, d\theta_t^+ + S_t^{\text{bid}} \, d\theta_t^-
$$

### 2. Shadow Price


**Definition** (Shadow Price): A **shadow price** is a process $\hat{S}_t$ with $S_t^{\text{bid}} \leq \hat{S}_t \leq S_t^{\text{ask}}$ such that the optimal strategy in the market with bid-ask spread equals the optimal strategy in a frictionless market with price $\hat{S}_t$.

**Theorem** (Kallsen-Muhle-Karbe, 2010): Under regularity conditions, a shadow price exists and the original problem with transaction costs reduces to a frictionless problem with the shadow price. The shadow price typically fluctuates between the bid and ask, touching each boundary at the optimal rebalancing times.

**Application to Hedging**: The hedging strategy under transaction costs can be computed by:

1. Finding the shadow price $\hat{S}_t$
2. Computing the frictionless Black-Scholes hedge with respect to $\hat{S}_t$
3. The no-trade band arises naturally from the bid-ask interval

### 3. Numerical Example


**Setup**: European call with $K = 100$, $T = 1$, $\sigma = 0.2$, $S_0 = 100$, $r = 0$.

**Proportional cost** $\varepsilon = 0.5\%$:

- Black-Scholes price: $C_{\text{BS}} \approx \$7.97$
- Leland-adjusted price ($N = 252$ daily rebalancing): $\hat{C} \approx \$9.14$
- Transaction cost reserve: $\hat{C} - C_{\text{BS}} \approx \$1.17$
- Whalley-Wilmott half-bandwidth at $t=0$: $H_0 \approx 0.032$ (about 3.2% of delta)

**Proportional cost** $\varepsilon = 1\%$:

- Leland-adjusted price ($N = 252$): $\hat{C} \approx \$10.31$
- Transaction cost reserve: $\approx \$2.34$ (roughly double, as expected for linear costs)

The super-replication price $V_\varepsilon^{\text{super}} = S_0 = \$100$ is clearly impractical, confirming the need for approximate strategies.

## Optimal Execution and Hedging


### 1. Combined Hedging and Execution


In practice, the hedging problem is intertwined with **optimal execution**: executing the hedge trades themselves incurs market impact costs.

**Model**: The total cost of a hedging strategy $(\theta_t)$ includes:

$$
\text{Total cost} = \underbrace{\int_0^T \theta_t \, dS_t}_{\text{hedging P\&L}} - \underbrace{\int_0^T c(|\dot{\theta}_t|) \, dt}_{\text{transaction costs}} - \underbrace{\int_0^T \eta(|\dot{\theta}_t|) S_t \, dt}_{\text{market impact}}
$$

where $c(\cdot)$ represents proportional costs and $\eta(\cdot)$ represents temporary price impact.

### 2. Connection to Model Uncertainty


**Key Insight**: The Leland volatility adjustment can be interpreted through the lens of model uncertainty. When transaction costs force discrete rebalancing, the hedger effectively faces **uncertain volatility** between rebalancing times:

$$
\sigma_{\text{effective}}^2 \in \left[\sigma^2 - \varepsilon \sigma \sqrt{\frac{8}{\pi \delta t}}, \; \sigma^2 + \varepsilon \sigma \sqrt{\frac{8}{\pi \delta t}}\right]
$$

This interval grows as the rebalancing frequency decreases ($\delta t$ increases), formalizing the intuition that **less frequent hedging corresponds to greater model uncertainty**.

**Proposition**: The Leland hedging strategy is the unique strategy that is optimal against the worst-case volatility realization within the effective uncertainty band, connecting transaction cost hedging to the minimax framework of robust control.

## Summary and Key Takeaways


1. **Continuous hedging is impossible**: Under any positive transaction costs, the Black-Scholes continuous delta-hedge generates infinite costs, necessitating discrete or band-based strategies

2. **Leland adjustment**: Replacing $\sigma^2$ with $\hat{\sigma}^2 = \sigma^2 + \varepsilon \sigma \sqrt{8/(\pi \delta t)}$ in the Black-Scholes formula provides an effective hedging strategy that accounts for proportional costs at leading order

3. **Super-replication is trivial**: The super-replication price of a call under any positive transaction cost equals the stock price, motivating approximate rather than exact hedging approaches

4. **Consistent price systems**: The fundamental theorem of asset pricing extends to markets with transaction costs via CPS, connecting directly to the robust pricing framework through the analogy between bid-ask spreads and ambiguity sets

5. **Asymptotic optimality**: The Whalley-Wilmott no-trade band provides the optimal balance between hedging error and costs for small $\varepsilon$, with bandwidth scaling as $\varepsilon^{1/3}$

6. **Model uncertainty connection**: Transaction costs create an effective volatility uncertainty band, linking hedging under costs to the uncertain volatility framework and robust control theory

7. **Practical relevance**: The transaction cost reserve $\hat{C} - C_{\text{BS}}$ quantifies the true cost of hedging and is essential for accurate P&L attribution and risk management

---

## Exercises

**Exercise 1.** For a European call with $S_0 = K = 100$, $\sigma = 0.20$, $T = 1$, $r = 0$, and proportional transaction cost $\varepsilon = 0.5\%$, compute the Leland adjusted volatility $\hat{\sigma} = \sigma\sqrt{1 + \varepsilon\sqrt{8/(\pi \delta t)}}$ for daily rebalancing ($\delta t = 1/252$). Compare the Leland-adjusted call price with the frictionless Black-Scholes price and interpret the difference as a transaction cost reserve.

---

**Exercise 2.** Prove that the super-replication price of a European call under proportional transaction costs $\varepsilon > 0$ equals the stock price $S_0$. Hint: show that the only portfolio that dominates $(S_T - K)^+$ for all $S_T \geq 0$ under transaction costs is to hold one share of stock. Explain why this result motivates the search for approximate rather than exact hedging strategies.

---

**Exercise 3.** The Whalley-Wilmott no-trade band has half-width $H = \left(\frac{3\varepsilon \Gamma^2 S^2 \sigma^2}{2r}\right)^{1/3}$. For the call option in Exercise 1, compute the no-trade band at $S = 100$ and $t = 0.5$. How does the band width depend on $\varepsilon$, and why does it scale as $\varepsilon^{1/3}$ rather than $\varepsilon$?

---

**Exercise 4.** Explain the concept of a consistent price system (CPS) in a market with proportional transaction costs. For a one-period model with $S_0 = 100$, $S_1 \in \{80, 120\}$, and $\varepsilon = 5\%$, characterize the set of all consistent price systems. How does this set relate to the set of equivalent martingale measures in the frictionless case?

---

**Exercise 5.** Compare the total hedging cost (transaction cost reserve plus expected hedging error) for three rebalancing frequencies: daily ($N = 252$), weekly ($N = 52$), and monthly ($N = 12$), with $\varepsilon = 0.1\%$. The expected transaction cost scales as $\varepsilon \sigma S_0 \sqrt{N/T}$ and the expected hedging error scales as $\sigma^2 S_0^2 \Gamma / (2N)$. Find the optimal rebalancing frequency that minimizes total cost.

---

**Exercise 6.** In the Leland framework, show that the effective volatility band induced by transaction costs is $[\sigma_{\text{eff}}^-, \sigma_{\text{eff}}^+]$ where

$$
\sigma_{\text{eff}}^\pm = \sigma \sqrt{1 \pm \varepsilon\sqrt{\frac{8}{\pi \delta t}}}
$$

Explain how this connects hedging under transaction costs to the uncertain volatility framework. For what values of $\varepsilon$ and $\delta t$ does the lower bound $\sigma_{\text{eff}}^-$ become zero or negative, and what does this mean financially?

---

**Exercise 7.** A trader considers two hedging strategies for a short call position: (a) delta hedging with Leland adjustment, rebalanced daily, and (b) semi-static hedging using a put-call parity relationship plus monthly rebalancing. Given $\varepsilon = 0.2\%$, $\sigma = 0.25$, and $T = 0.5$, analyze which strategy produces lower total cost. Include both the expected hedging error and the expected transaction costs in your comparison.
