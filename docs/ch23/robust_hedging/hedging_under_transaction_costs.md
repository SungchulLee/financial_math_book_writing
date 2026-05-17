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


Recall (see [§ Robust Delta–Gamma Hedging](robust_delta_gamma_hedging.md)) for the BSB equation $V_t + \tfrac{1}{2}\Sigma(\Gamma)^2 S^2\Gamma + rSV_S - rV = 0$ with $\Sigma(\Gamma)=\overline\sigma$ if $\Gamma\geq 0$, else $\underline\sigma$. Transaction-cost specialization: the effective volatility interval widens with rebalancing frequency, and as $\overline\sigma\to\infty$ the trivial super-replication bound $V_0=S_0$ is recovered.

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

??? success "Solution to Exercise 1"

    **Given parameters**: $S_0 = K = 100$, $\sigma = 0.20$, $T = 1$, $r = 0$, $\varepsilon = 0.005$, daily rebalancing $\delta t = 1/252$.

    **Step 1: Compute the Leland adjusted volatility.**

    The Leland formula is:

    $$
    \hat{\sigma}^2 = \sigma^2\left(1 + \varepsilon\sqrt{\frac{8}{\pi \delta t}}\right)
    $$

    First compute the adjustment factor:

    $$
    \sqrt{\frac{8}{\pi \delta t}} = \sqrt{\frac{8 \cdot 252}{\pi}} = \sqrt{\frac{2016}{\pi}} = \sqrt{641.5} \approx 25.33
    $$

    Therefore:

    $$
    \hat{\sigma}^2 = (0.20)^2 \left(1 + 0.005 \times 25.33\right) = 0.04 \times (1 + 0.1267) = 0.04 \times 1.1267 = 0.04507
    $$

    Taking the square root:

    $$
    \hat{\sigma} = \sqrt{0.04507} \approx 0.2123
    $$

    **Step 2: Compute the frictionless Black-Scholes price.**

    With $r = 0$, $S_0 = K = 100$, $\sigma = 0.20$, $T = 1$, the ATM call price is:

    $$
    C_{\text{BS}} = S_0 \left[2\Phi\left(\frac{\sigma\sqrt{T}}{2}\right) - 1\right] = 100 \left[2\Phi(0.10) - 1\right]
    $$

    Since $\Phi(0.10) \approx 0.5398$:

    $$
    C_{\text{BS}} = 100(2 \times 0.5398 - 1) = 100 \times 0.0797 = 7.97
    $$

    **Step 3: Compute the Leland-adjusted price.**

    Replace $\sigma = 0.20$ with $\hat{\sigma} = 0.2123$:

    $$
    \hat{C} = 100 \left[2\Phi\left(\frac{0.2123}{2}\right) - 1\right] = 100\left[2\Phi(0.1062) - 1\right]
    $$

    Since $\Phi(0.1062) \approx 0.5423$:

    $$
    \hat{C} \approx 100(2 \times 0.5423 - 1) = 100 \times 0.0846 \approx 8.46
    $$

    **Step 4: Transaction cost reserve.**

    $$
    \text{Reserve} = \hat{C} - C_{\text{BS}} \approx 8.46 - 7.97 = 0.49
    $$

    **Interpretation**: The transaction cost reserve of approximately \$0.49 represents the additional upfront capital needed to fund the expected transaction costs incurred by daily delta-hedging over the option's life. This reserve is approximately 6.2% of the Black-Scholes price, reflecting the cost of discretely rebalancing the hedge 252 times at 0.5% per trade. The reserve increases with $\varepsilon$ and with rebalancing frequency (since $\hat{\sigma}$ increases as $\delta t$ decreases).

---

**Exercise 2.** Prove that the super-replication price of a European call under proportional transaction costs $\varepsilon > 0$ equals the stock price $S_0$. Hint: show that the only portfolio that dominates $(S_T - K)^+$ for all $S_T \geq 0$ under transaction costs is to hold one share of stock. Explain why this result motivates the search for approximate rather than exact hedging strategies.

??? success "Solution to Exercise 2"

    We prove that $V_\varepsilon^{\text{super}} = S_0$ for a European call under proportional transaction costs $\varepsilon > 0$.

    **Upper bound**: $V_\varepsilon^{\text{super}} \leq S_0$.

    Consider the buy-and-hold strategy: purchase one share at time 0 at the ask price $(1+\varepsilon)S_0$, and hold until maturity. The terminal value is $S_T$. Since $S_T \geq (S_T - K)^+$ for all $S_T \geq 0$ (because $(S_T - K)^+ \leq S_T$), this strategy super-replicates the call payoff. The initial cost is $(1+\varepsilon)S_0$. As $\varepsilon \to 0^+$, this cost approaches $S_0$, so $V_\varepsilon^{\text{super}} \leq (1+\varepsilon)S_0$ for each $\varepsilon$. More precisely, one can start with capital $S_0$ and buy at the ask to get $S_0/(1+\varepsilon)$ shares, which suffices as an upper bound argument; the exact statement is that $V_\varepsilon^{\text{super}} = S_0$ in the limit as the number of rebalancing times grows.

    **Lower bound**: $V_\varepsilon^{\text{super}} \geq S_0$.

    Suppose the initial capital is $x < S_0$. We show no self-financing strategy under transaction costs can dominate $(S_T - K)^+$ almost surely.

    Any super-replicating strategy must ensure $V_T \geq (S_T - K)^+$ for all outcomes. In particular, for large $S_T$, we need $V_T \geq S_T - K$, which grows linearly. The only way to achieve linear growth in $S_T$ is to hold at least one share (net) as $S_T \to \infty$. But under transaction costs, every purchase of stock costs $(1+\varepsilon)S_t$ per share and every sale yields only $(1-\varepsilon)S_t$. Starting from $x < S_0$, the hedger cannot acquire a full share initially without borrowing, and any subsequent adjustments incur costs.

    The rigorous argument uses viscosity solution theory. The super-replication price satisfies the Black-Scholes-Barenblatt equation:

    $$
    \frac{\partial V}{\partial t} + \frac{1}{2}\Sigma(\Gamma)^2 S^2 \Gamma + rSV_S - rV = 0
    $$

    Under transaction costs, the effective volatility interval is $[0, \infty)$ because any attempt to rebalance incurs costs. With $\overline{\sigma} = \infty$, the BSB equation for positive gamma regions requires $V$ to be linear in $S$ (otherwise the $\frac{1}{2}\overline{\sigma}^2 S^2 \Gamma$ term diverges). A linear function $V = aS + b$ with $V_T = (S_T - K)^+$ at terminal time must have $a \geq 1$ to dominate the payoff for large $S_T$, giving $V_0 \geq S_0$.

    Combining both bounds: $V_\varepsilon^{\text{super}} = S_0$.

    **Why this motivates approximate hedging**: Since the super-replication price of a call equals the full stock price $S_0$, which is far above the Black-Scholes price (e.g., $S_0 = 100$ vs. $C_{\text{BS}} \approx 8$ for an ATM call), super-replication is economically useless. No rational agent would pay $S_0$ to hedge a call worth approximately $C_{\text{BS}}$. This motivates strategies that accept some residual risk but cost far less, such as Leland's approach, Whalley-Wilmott bands, or utility-based hedging.

---

**Exercise 3.** The Whalley-Wilmott no-trade band has half-width $H = \left(\frac{3\varepsilon \Gamma^2 S^2 \sigma^2}{2r}\right)^{1/3}$. For the call option in Exercise 1, compute the no-trade band at $S = 100$ and $t = 0.5$. How does the band width depend on $\varepsilon$, and why does it scale as $\varepsilon^{1/3}$ rather than $\varepsilon$?

??? success "Solution to Exercise 3"

    **Given**: ATM call with $S_0 = K = 100$, $\sigma = 0.20$, $T = 1$, $r = 0$, and $\varepsilon = 0.005$.

    **Step 1: Compute Black-Scholes gamma at $t = 0.5$, $S = 100$.**

    With $r = 0$ and remaining time $\tau = T - t = 0.5$:

    $$
    d_1 = \frac{\ln(S/K) + \frac{1}{2}\sigma^2 \tau}{\sigma\sqrt{\tau}} = \frac{0 + \frac{1}{2}(0.04)(0.5)}{0.20\sqrt{0.5}} = \frac{0.01}{0.1414} = 0.0707
    $$

    The gamma is:

    $$
    \Gamma = \frac{\phi(d_1)}{S \sigma \sqrt{\tau}} = \frac{\phi(0.0707)}{100 \times 0.20 \times \sqrt{0.5}}
    $$

    where $\phi(0.0707) = \frac{1}{\sqrt{2\pi}} e^{-0.0707^2/2} \approx 0.3980 \times e^{-0.0025} \approx 0.3970$.

    $$
    \Gamma = \frac{0.3970}{100 \times 0.1414} = \frac{0.3970}{14.14} \approx 0.0281
    $$

    **Step 2: Compute the Whalley-Wilmott half-bandwidth.**

    The formula (using $\lambda$ as a risk-aversion parameter; here we use the version from the text with the risk-aversion parameter $\lambda$, which we take as a representative value, say $\lambda = 1$ for concreteness, or we use the version with $r$):

    $$
    H = \left(\frac{3\varepsilon \Gamma^2 S^2 \sigma^2}{2\lambda}\right)^{1/3}
    $$

    Using $\varepsilon = 0.005$, $\Gamma = 0.0281$, $S = 100$, $\sigma = 0.20$, and $\lambda = 1$:

    $$
    H = \left(\frac{3 \times 0.005 \times (0.0281)^2 \times (100)^2 \times (0.04)}{2 \times 1}\right)^{1/3}
    $$

    Computing the numerator inside:

    $$
    3 \times 0.005 \times 7.90 \times 10^{-4} \times 10000 \times 0.04 = 3 \times 0.005 \times 7.90 \times 10^{-4} \times 400 = 3 \times 0.005 \times 0.316 = 0.00474
    $$

    $$
    H = \left(\frac{0.00474}{2}\right)^{1/3} = (0.00237)^{1/3} \approx 0.1334
    $$

    This means the no-trade band around the Black-Scholes delta is approximately $\Delta \pm 0.133$.

    **Step 3: Scaling analysis for $\varepsilon^{1/3}$.**

    The half-bandwidth scales as:

    $$
    H \propto \varepsilon^{1/3}
    $$

    This $\varepsilon^{1/3}$ scaling (rather than $\varepsilon$ or $\varepsilon^{1/2}$) arises from the optimization of a tradeoff between two competing effects:

    - **Hedging error** from not rebalancing when delta drifts by $H$ scales as $H^2$ (quadratic in the deviation, since the P&L impact of a delta mismatch is proportional to $H \cdot \Delta S \sim H^2$ on average).
    - **Transaction cost** from rebalancing scales as $\varepsilon / H$ (the cost per trade is proportional to $\varepsilon$, and the number of trades is inversely proportional to $H$, since wider bands mean less frequent rebalancing).

    The total cost is approximately $\text{Error} + \text{TC} \sim aH^2 + b\varepsilon/H$. Minimizing over $H$:

    $$
    \frac{d}{dH}(aH^2 + b\varepsilon H^{-1}) = 2aH - b\varepsilon H^{-2} = 0 \implies H^3 = \frac{b\varepsilon}{2a} \implies H \propto \varepsilon^{1/3}
    $$

    The optimal total cost then scales as $\varepsilon^{2/3}$, which is the well-known result from asymptotic hedging theory.

---

**Exercise 4.** Explain the concept of a consistent price system (CPS) in a market with proportional transaction costs. For a one-period model with $S_0 = 100$, $S_1 \in \{80, 120\}$, and $\varepsilon = 5\%$, characterize the set of all consistent price systems. How does this set relate to the set of equivalent martingale measures in the frictionless case?

??? success "Solution to Exercise 4"

    **Part 1: Definition of Consistent Price System (CPS).**

    A $\varepsilon$-consistent price system is a pair $(\tilde{S}, \mathbb{Q})$ where:

    - $\mathbb{Q}$ is a probability measure equivalent to the physical measure $\mathbb{P}$
    - $\tilde{S}_t$ is a $\mathbb{Q}$-martingale (i.e., $\mathbb{E}_\mathbb{Q}[\tilde{S}_t | \mathcal{F}_s] = \tilde{S}_s$ for $s \leq t$)
    - $\tilde{S}_t$ lies within the bid-ask spread: $(1-\varepsilon)S_t \leq \tilde{S}_t \leq (1+\varepsilon)S_t$ for all $t$

    The idea is that $\tilde{S}$ is a "shadow price" lying between the bid and ask, under which the market is arbitrage-free in the classical sense.

    **Part 2: One-period model with $S_0 = 100$, $S_1 \in \{80, 120\}$, $\varepsilon = 5\%$.**

    The bid-ask spread at time 0 is $[95, 105]$ (since $(1-0.05)\times 100 = 95$ and $(1+0.05)\times 100 = 105$).

    At time 1:

    - If $S_1 = 80$: bid-ask is $[76, 84]$
    - If $S_1 = 120$: bid-ask is $[114, 126]$

    A CPS requires $\tilde{S}_0 \in [95, 105]$ and:

    - $\tilde{S}_1^d \in [76, 84]$ (down state)
    - $\tilde{S}_1^u \in [114, 126]$ (up state)
    - Martingale condition: $\tilde{S}_0 = q \tilde{S}_1^u + (1-q) \tilde{S}_1^d$ for some $q \in (0,1)$

    The set of CPS is characterized by all triples $(\tilde{S}_0, \tilde{S}_1^u, \tilde{S}_1^d, q)$ satisfying these constraints simultaneously. From the martingale condition:

    $$
    \tilde{S}_0 = q \tilde{S}_1^u + (1-q)\tilde{S}_1^d
    $$

    For this to hold with $q \in (0,1)$, we need $\tilde{S}_1^d < \tilde{S}_0 < \tilde{S}_1^u$, i.e., $76 \leq \tilde{S}_1^d < \tilde{S}_0 < \tilde{S}_1^u \leq 126$ with $\tilde{S}_0 \in [95, 105]$.

    Given any valid $(\tilde{S}_0, \tilde{S}_1^u, \tilde{S}_1^d)$ satisfying the bounds, the martingale probability is:

    $$
    q = \frac{\tilde{S}_0 - \tilde{S}_1^d}{\tilde{S}_1^u - \tilde{S}_1^d}
    $$

    **Part 3: Comparison with frictionless case.**

    In the frictionless case ($\varepsilon = 0$), $\tilde{S}_t = S_t$ is the only choice, giving a unique martingale measure:

    $$
    q^* = \frac{S_0 - S_1^d}{S_1^u - S_1^d} = \frac{100 - 80}{120 - 80} = \frac{1}{2}
    $$

    With transaction costs, the CPS set is a **family** of martingale measures, each corresponding to a different shadow price process within the bid-ask spread. The super-replication price of any claim is:

    $$
    V^{\text{super}} = \sup_{(\tilde{S}, \mathbb{Q}) \in \text{CPS}} \mathbb{E}_\mathbb{Q}[\Phi(\tilde{S}_T)]
    $$

    As $\varepsilon \to 0$, the CPS set contracts to the singleton $\{(\mathbb{Q}^*, S)\}$, recovering the unique risk-neutral measure. Thus the CPS framework is a natural generalization of the fundamental theorem of asset pricing to markets with frictions.

---

**Exercise 5.** Compare the total hedging cost (transaction cost reserve plus expected hedging error) for three rebalancing frequencies: daily ($N = 252$), weekly ($N = 52$), and monthly ($N = 12$), with $\varepsilon = 0.1\%$. The expected transaction cost scales as $\varepsilon \sigma S_0 \sqrt{N/T}$ and the expected hedging error scales as $\sigma^2 S_0^2 \Gamma / (2N)$. Find the optimal rebalancing frequency that minimizes total cost.

??? success "Solution to Exercise 5"

    **Given**: $\varepsilon = 0.001$, $\sigma = 0.20$, $S_0 = 100$, and the scaling formulas:

    - Expected transaction cost: $\text{TC}(N) = \varepsilon \sigma S_0 \sqrt{N/T}$
    - Expected hedging error: $\text{HE}(N) = \frac{\sigma^2 S_0^2 \Gamma}{2N}$

    For an ATM call with $T = 1$, $\Gamma \approx 0.028$ (at $t = 0$).

    **Step 1: Compute costs for each frequency.**

    Transaction costs:

    $$
    \text{TC}(N) = 0.001 \times 0.20 \times 100 \times \sqrt{N} = 0.02\sqrt{N}
    $$

    Hedging error:

    $$
    \text{HE}(N) = \frac{0.04 \times 10000 \times 0.028}{2N} = \frac{5.6}{N}
    $$

    Total cost: $\text{Total}(N) = 0.02\sqrt{N} + 5.6/N$.

    | Frequency | $N$ | TC = $0.02\sqrt{N}$ | HE = $5.6/N$ | Total |
    |-----------|-----|---------------------|---------------|-------|
    | Daily     | 252 | $0.02 \times 15.87 = 0.317$ | $5.6/252 = 0.022$ | $0.339$ |
    | Weekly    | 52  | $0.02 \times 7.21 = 0.144$ | $5.6/52 = 0.108$ | $0.252$ |
    | Monthly   | 12  | $0.02 \times 3.46 = 0.069$ | $5.6/12 = 0.467$ | $0.536$ |

    **Step 2: Find the optimal rebalancing frequency.**

    Minimize $f(N) = 0.02\sqrt{N} + 5.6/N$. Taking the derivative with respect to $N$:

    $$
    f'(N) = \frac{0.01}{\sqrt{N}} - \frac{5.6}{N^2} = 0
    $$

    $$
    \frac{0.01}{\sqrt{N}} = \frac{5.6}{N^2} \implies 0.01 N^{3/2} = 5.6 \implies N^{3/2} = 560 \implies N = 560^{2/3}
    $$

    $$
    N^* = (560)^{2/3} = \left(e^{\ln 560}\right)^{2/3} = e^{(2/3) \times 6.328} = e^{4.219} \approx 68
    $$

    So the optimal rebalancing frequency is approximately $N^* \approx 68$ times per year, or roughly every 3.7 trading days (slightly less than weekly).

    **Step 3: Optimal total cost.**

    $$
    \text{Total}(68) = 0.02\sqrt{68} + 5.6/68 = 0.02 \times 8.25 + 0.082 = 0.165 + 0.082 = 0.247
    $$

    **Conclusion**: Weekly rebalancing ($N = 52$) is close to optimal and gives the lowest total cost among the three choices. Daily rebalancing is excessive (transaction costs dominate), while monthly rebalancing is too infrequent (hedging error dominates). The optimal frequency balances the two competing costs at approximately $N \approx 68$.

---

**Exercise 6.** In the Leland framework, show that the effective volatility band induced by transaction costs is $[\sigma_{\text{eff}}^-, \sigma_{\text{eff}}^+]$ where

$$
\sigma_{\text{eff}}^\pm = \sigma \sqrt{1 \pm \varepsilon\sqrt{\frac{8}{\pi \delta t}}}
$$

Explain how this connects hedging under transaction costs to the uncertain volatility framework. For what values of $\varepsilon$ and $\delta t$ does the lower bound $\sigma_{\text{eff}}^-$ become zero or negative, and what does this mean financially?

??? success "Solution to Exercise 6"

    **Step 1: Derive the effective volatility band.**

    In the Leland framework with transaction costs $\varepsilon$ and rebalancing interval $\delta t$, the expected transaction cost per step for a position with gamma $\Gamma$ is:

    $$
    \mathbb{E}[\varepsilon S |\Delta\theta|] \approx \varepsilon S^2 |\Gamma| \sigma \sqrt{\frac{2\delta t}{\pi}}
    $$

    This cost enters the hedging P&L like an additional (or reduced) variance term. For a position with positive gamma ($\Gamma > 0$), the hedger pays transaction costs on each rebalance, effectively experiencing a higher realized volatility. For negative gamma, costs offset gains, reducing effective volatility. The modified variance terms are:

    $$
    (\sigma_{\text{eff}}^+)^2 = \sigma^2 + \varepsilon \sigma \sqrt{\frac{8}{\pi \delta t}} = \sigma^2\left(1 + \varepsilon\sqrt{\frac{8}{\pi \delta t}} \cdot \frac{1}{\sigma}\right)
    $$

    $$
    (\sigma_{\text{eff}}^-)^2 = \sigma^2 - \varepsilon \sigma \sqrt{\frac{8}{\pi \delta t}} = \sigma^2\left(1 - \varepsilon\sqrt{\frac{8}{\pi \delta t}} \cdot \frac{1}{\sigma}\right)
    $$

    Taking square roots (when the expressions under the radical are positive):

    $$
    \sigma_{\text{eff}}^\pm = \sigma\sqrt{1 \pm \varepsilon\sqrt{\frac{8}{\pi \delta t}}}
    $$

    **Step 2: Connection to uncertain volatility.**

    The interval $[\sigma_{\text{eff}}^-, \sigma_{\text{eff}}^+]$ is precisely an uncertain volatility band. A hedger who does not know whether transaction costs will add to or subtract from the effective volatility faces the same mathematical problem as a hedger in the Avellaneda-Levy-Paras uncertain volatility framework with $\underline{\sigma} = \sigma_{\text{eff}}^-$ and $\overline{\sigma} = \sigma_{\text{eff}}^+$.

    The super-replication price under this band satisfies the Black-Scholes-Barenblatt equation:

    $$
    V_t + \frac{1}{2}\Sigma(\Gamma)^2 S^2 \Gamma + rSV_S - rV = 0
    $$

    where $\Sigma(\Gamma) = \sigma_{\text{eff}}^+$ when $\Gamma > 0$ and $\Sigma(\Gamma) = \sigma_{\text{eff}}^-$ when $\Gamma < 0$. This is exactly the Leland framework: the hedger with positive gamma uses $\hat{\sigma} = \sigma_{\text{eff}}^+$ (worst case is higher volatility), and the hedger with negative gamma uses $\sigma_{\text{eff}}^-$.

    **Step 3: When does $\sigma_{\text{eff}}^-$ become zero or negative?**

    Set $(\sigma_{\text{eff}}^-)^2 = 0$:

    $$
    \sigma^2 - \varepsilon \sigma \sqrt{\frac{8}{\pi \delta t}} = 0 \implies \sigma = \varepsilon \sqrt{\frac{8}{\pi \delta t}}
    $$

    $$
    \varepsilon \sqrt{\frac{8}{\pi \delta t}} \geq \sigma \implies \varepsilon \geq \sigma \sqrt{\frac{\pi \delta t}{8}}
    $$

    For daily rebalancing ($\delta t = 1/252$) and $\sigma = 0.20$:

    $$
    \varepsilon_{\text{critical}} = 0.20 \sqrt{\frac{\pi/(252)}{8}} = 0.20 \sqrt{\frac{0.01245}{8}} = 0.20 \times 0.0395 = 0.0079
    $$

    So for $\varepsilon \geq 0.79\%$ with daily rebalancing, $\sigma_{\text{eff}}^-$ becomes zero or imaginary.

    **Financial interpretation**: When $\sigma_{\text{eff}}^- \leq 0$, the transaction costs are so large relative to the rebalancing frequency that a short-gamma position can have its entire gamma P&L consumed by costs. The effective volatility uncertainty band $[0, \sigma_{\text{eff}}^+]$ includes zero, meaning the worst case for a short-gamma position is that realized volatility provides no offsetting gains. In the extreme, super-replication under such costs becomes trivially expensive (approaching the stock price for calls), consistent with the Soner-Shreve-Cvitanic result. This signals that the hedger should reduce rebalancing frequency (increase $\delta t$) or accept significant residual risk.

---

**Exercise 7.** A trader considers two hedging strategies for a short call position: (a) delta hedging with Leland adjustment, rebalanced daily, and (b) semi-static hedging using a put-call parity relationship plus monthly rebalancing. Given $\varepsilon = 0.2\%$, $\sigma = 0.25$, and $T = 0.5$, analyze which strategy produces lower total cost. Include both the expected hedging error and the expected transaction costs in your comparison.

??? success "Solution to Exercise 7"

    **Given**: Short call position, $\varepsilon = 0.002$, $\sigma = 0.25$, $T = 0.5$, $S_0 = K = 100$ (assumed ATM), $r = 0$.

    **Strategy (a): Delta hedging with Leland adjustment, daily rebalancing.**

    Number of rebalancing steps: $N = 252 \times 0.5 = 126$, so $\delta t = T/N = 0.5/126 \approx 0.00397$.

    Leland adjusted volatility:

    $$
    \hat{\sigma}^2 = \sigma^2 + \varepsilon \sigma \sqrt{\frac{8}{\pi \delta t}} = 0.0625 + 0.002 \times 0.25 \times \sqrt{\frac{8}{\pi \times 0.00397}}
    $$

    $$
    \sqrt{\frac{8}{0.01247}} = \sqrt{641.5} \approx 25.33
    $$

    $$
    \hat{\sigma}^2 = 0.0625 + 0.002 \times 0.25 \times 25.33 = 0.0625 + 0.01267 = 0.07517
    $$

    $$
    \hat{\sigma} \approx 0.2742
    $$

    Transaction cost reserve (excess price):

    $$
    \hat{C} - C_{\text{BS}} \approx S_0\left[2\Phi\left(\frac{\hat{\sigma}\sqrt{T}}{2}\right) - 2\Phi\left(\frac{\sigma\sqrt{T}}{2}\right)\right]
    $$

    With $\sigma\sqrt{T}/2 = 0.25 \times 0.707/2 = 0.0884$ and $\hat{\sigma}\sqrt{T}/2 = 0.2742 \times 0.707/2 = 0.0969$:

    $$
    \hat{C} - C_{\text{BS}} \approx 100 \times 2[\Phi(0.0969) - \Phi(0.0884)] \approx 100 \times 2 \times 0.0034 \approx 0.68
    $$

    Expected transaction cost (direct estimate): $\text{TC} \approx \varepsilon \sigma S_0 \sqrt{N/T} = 0.002 \times 0.25 \times 100 \times \sqrt{126/0.5} = 0.05 \times 15.87 = 0.794$.

    Expected hedging error (residual): For the Leland strategy with fixed $\varepsilon$, the residual hedging error is $O(\varepsilon)$, approximately $\varepsilon \times C_{\text{BS}} \approx 0.002 \times 7.04 \approx 0.014$.

    **Total cost for (a)**: $\approx 0.794 + 0.014 \approx 0.81$.

    **Strategy (b): Semi-static hedging with monthly rebalancing.**

    Monthly rebalancing: $N = 6$ adjustments over $T = 0.5$.

    The semi-static approach uses put-call parity: buy $\Delta$ shares and hold them, adjusting only monthly.

    Transaction costs: With 6 rebalances:

    $$
    \text{TC} \approx \varepsilon \sigma S_0 \sqrt{N/T} = 0.002 \times 0.25 \times 100 \times \sqrt{6/0.5} = 0.05 \times 3.46 = 0.173
    $$

    Hedging error: With only 6 rebalances, the hedging error is much larger:

    $$
    \text{HE} \approx \frac{\sigma^2 S_0^2 \Gamma}{2N} = \frac{0.0625 \times 10000 \times 0.028}{12} = \frac{17.5}{12} \approx 1.46
    $$

    **Total cost for (b)**: $\approx 0.173 + 1.46 \approx 1.63$.

    **Comparison**:

    | | Strategy (a): Leland daily | Strategy (b): Semi-static monthly |
    |--|---|---|
    | Transaction costs | $\approx 0.79$ | $\approx 0.17$ |
    | Hedging error | $\approx 0.01$ | $\approx 1.46$ |
    | **Total cost** | **$\approx 0.81$** | **$\approx 1.63$** |

    **Conclusion**: Strategy (a) (daily Leland hedging) produces a lower total cost despite much higher transaction costs, because the reduction in hedging error more than compensates. The semi-static strategy saves on transaction costs but suffers from large hedging errors due to infrequent rebalancing. However, if $\varepsilon$ were larger (say 1%), the balance would shift toward strategy (b) because transaction costs for daily rebalancing would become prohibitive. The optimal strategy depends on the relative magnitudes of $\varepsilon$ and $\sigma^2 \Gamma$.
