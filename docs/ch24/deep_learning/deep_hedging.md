# Deep Hedging

**Deep hedging**, introduced by Buehler, Gonon, Maystre, and Niedermeyer (2019), recasts the hedging problem as an optimization over neural-network-parameterized trading strategies. Unlike classical delta hedging, which relies on a specific model and assumes frictionless markets, deep hedging directly minimizes a risk measure of the hedging profit-and-loss (P&L) while naturally incorporating transaction costs, discrete rebalancing, market impact, and incomplete markets.

---

## Limitations of Classical Delta Hedging

In the Black-Scholes framework, the replicating strategy for a European option with payoff $H(S_T)$ is:

$$
\delta_t = \frac{\partial V}{\partial S}(t, S_t)
$$

This requires:

- A correctly specified model for $S$
- Continuous trading (infinitesimal rebalancing intervals)
- Zero transaction costs
- Complete markets (all risk can be hedged)

In practice, every assumption is violated. Rebalancing is discrete, transaction costs are material, models are misspecified, and markets are incomplete. The resulting P&L residual can be substantial.

---

## The Deep Hedging Framework

### Setup and Notation

Consider a discrete trading schedule $0 = t_0 < t_1 < \cdots < t_N = T$ and a set of tradeable instruments with prices $S_{t_k} \in \mathbb{R}^d$ at each time $t_k$.

**Definition (Hedging Strategy).** A hedging strategy is a sequence of $\mathcal{F}_{t_k}$-measurable functions:

$$
\delta = (\delta_{t_0}, \delta_{t_1}, \ldots, \delta_{t_{N-1}}), \quad \delta_{t_k} : \Omega \to \mathbb{R}^d
$$

where $\delta_{t_k}$ specifies the portfolio holdings in the $d$ tradeable instruments during the interval $[t_k, t_{k+1})$.

**Definition (Hedging P&L).** The profit and loss from hedging a liability $Z$ (e.g., an option payoff) using strategy $\delta$ is:

$$
\text{P\&L}(\delta) = -Z + \sum_{k=0}^{N-1} \delta_{t_k}^\top (S_{t_{k+1}} - S_{t_k}) - \sum_{k=0}^{N-1} c_{t_k}(\delta_{t_k}, \delta_{t_{k-1}})
$$

where $c_{t_k}(\delta_{t_k}, \delta_{t_{k-1}})$ represents transaction costs incurred when rebalancing from $\delta_{t_{k-1}}$ to $\delta_{t_k}$ (with $\delta_{t_{-1}} = 0$).

### Transaction Cost Models

Common cost specifications include:

**Proportional costs:**

$$
c_k(\delta_k, \delta_{k-1}) = \kappa \, |S_{t_k}|^\top |\delta_k - \delta_{k-1}|
$$

where $\kappa > 0$ is the cost rate and operations are componentwise.

**Quadratic (market impact) costs:**

$$
c_k(\delta_k, \delta_{k-1}) = \lambda \, (\delta_k - \delta_{k-1})^\top \Sigma_k \, (\delta_k - \delta_{k-1})
$$

where $\Sigma_k$ captures the price impact matrix.

---

## Optimization Objective

### Risk Measure Minimization

The deep hedging objective is to find the strategy minimizing a convex risk measure of the negative P&L:

$$
\min_{\delta \in \mathcal{H}} \rho\!\left(-\text{P\&L}(\delta)\right)
$$

where $\mathcal{H}$ is the set of admissible strategies and $\rho$ is a **convex risk measure**.

**Definition (Convex Risk Measure).** A functional $\rho : L^p(\Omega) \to \mathbb{R} \cup \{+\infty\}$ is a convex risk measure if it satisfies:

1. **Monotonicity:** $X \leq Y$ a.s. implies $\rho(X) \geq \rho(Y)$
2. **Cash invariance:** $\rho(X + c) = \rho(X) - c$ for $c \in \mathbb{R}$
3. **Convexity:** $\rho(\lambda X + (1-\lambda)Y) \leq \lambda\rho(X) + (1-\lambda)\rho(Y)$

### Common Risk Measures

**Entropic risk measure:**

$$
\rho_\lambda(X) = \frac{1}{\lambda}\log\!\left(\mathbb{E}\!\left[e^{-\lambda X}\right]\right)
$$

This corresponds to exponential utility maximization. The parameter $\lambda > 0$ controls risk aversion.

**Conditional Value-at-Risk (CVaR):**

$$
\text{CVaR}_\alpha(X) = -\frac{1}{\alpha}\mathbb{E}\!\left[X \cdot \mathbf{1}_{\{X \leq q_\alpha(X)\}}\right]
$$

where $q_\alpha(X)$ is the $\alpha$-quantile. CVaR focuses on tail losses and is coherent (subadditive).

**Mean-variance:**

$$
\rho_{\text{MV}}(X) = -\mathbb{E}[X] + \frac{\gamma}{2}\text{Var}(X)
$$

Not cash-invariant, but widely used in practice.

---

## Neural Network Parameterization

### Strategy Networks

Each $\delta_{t_k}$ is parameterized by a neural network:

$$
\delta_{t_k} = \mathcal{N}_{\theta_k}(I_{t_k})
$$

where $I_{t_k}$ is the **information vector** available at time $t_k$, which may include:

- Current prices: $S_{t_k}$
- Current holdings: $\delta_{t_{k-1}}$
- Time to maturity: $T - t_k$
- Additional features: implied volatility, Greeks, realized volatility

The network $\mathcal{N}_{\theta_k} : \mathbb{R}^p \to \mathbb{R}^d$ maps the information state to portfolio holdings.

### Recurrent vs Feedforward Architectures

**Feedforward (per-step networks):** Each time step has its own network $\mathcal{N}_{\theta_k}$. The information vector must encode all relevant history.

**Recurrent (LSTM/GRU):** A single recurrent network processes the sequence of market observations, maintaining an internal state that summarizes history:

$$
h_{k+1}, \delta_{t_k} = \text{LSTM}_\theta(I_{t_k}, h_k)
$$

The recurrent approach uses fewer parameters and can discover relevant features from raw price paths.

### The Full Optimization Problem

$$
\min_\Theta \; \rho\!\left(-\text{P\&L}(\delta^\Theta)\right) = \min_\Theta \; \rho\!\left(Z - \sum_{k=0}^{N-1} \mathcal{N}_{\theta_k}(I_{t_k})^\top (S_{t_{k+1}} - S_{t_k}) + \sum_{k=0}^{N-1} c_k\right)
$$

where $\Theta = (\theta_0, \ldots, \theta_{N-1})$ collects all network parameters.

---

## Training Procedure

### Monte Carlo Optimization

Since the expectation in the risk measure is intractable, we approximate via Monte Carlo:

1. **Simulate** $M$ paths of the underlying process $\{S_{t_k}^{(m)}\}_{k,m}$ under a chosen model (or use historical paths)
2. **Compute** hedging P&L for each path:

$$
\text{P\&L}^{(m)} = -Z^{(m)} + \sum_{k=0}^{N-1} \delta_{t_k}^{(m),\top}(S_{t_{k+1}}^{(m)} - S_{t_k}^{(m)}) - \sum_k c_k^{(m)}
$$

3. **Evaluate** the empirical risk measure:

$$
\hat{\rho}(\Theta) = \hat{\rho}\!\left(\{-\text{P\&L}^{(m)}\}_{m=1}^M\right)
$$

4. **Update** parameters via SGD/Adam: $\Theta \leftarrow \Theta - \eta \nabla_\Theta \hat{\rho}$

For the entropic risk measure, the gradient is:

$$
\nabla_\Theta \hat{\rho}_\lambda = -\frac{\sum_{m=1}^M e^{-\lambda \, \text{P\&L}^{(m)}} \nabla_\Theta \text{P\&L}^{(m)}}{\sum_{m=1}^M e^{-\lambda \, \text{P\&L}^{(m)}}}
$$

This is a reweighted average of P&L gradients, with higher weight on worse outcomes.

---

## Theoretical Properties

### Existence of Optimal Strategies

**Theorem (Buehler et al. 2019).** Under mild conditions on the risk measure $\rho$ (lower semicontinuity, convexity) and the market model (bounded price increments), an optimal hedging strategy exists:

$$
\delta^* = \arg\min_{\delta \in \mathcal{H}} \rho(-\text{P\&L}(\delta))
$$

Moreover, if the neural network class $\mathcal{F}_N$ is sufficiently rich (universal approximation), the deep hedging solution converges to the optimal strategy as the network capacity increases.

### Indifference Pricing

Deep hedging naturally produces **indifference prices**. The indifference price $p$ of the liability $Z$ is defined by:

$$
\min_\delta \rho\!\left(-\text{P\&L}_{\text{hedged}}\right) = \min_\delta \rho\!\left(-\text{P\&L}_{\text{unhedged}}\right)
$$

which gives:

$$
p = \min_\delta \rho\!\left(Z - \sum_k \delta_{t_k}^\top \Delta S_{t_k} + \sum_k c_k\right) - \min_\delta \rho\!\left(-\sum_k \delta_{t_k}^\top \Delta S_{t_k} + \sum_k c_k\right)
$$

This price accounts for transaction costs and risk aversion, and is computed as a byproduct of the optimization.

---

## Example: European Call with Transaction Costs

Consider hedging a European call with payoff $Z = (S_T - K)^+$ under proportional transaction costs $\kappa = 0.001$ (10 basis points per trade), with weekly rebalancing ($N = 52$ for $T = 1$ year).

### Comparison with Delta Hedging

Under the Black-Scholes model with $S_0 = 100$, $K = 100$, $r = 0.02$, $\sigma = 0.2$:

| Strategy | Mean P&L | Std P&L | CVaR$_{5\%}$ P&L | Total Cost |
|---|---|---|---|---|
| No hedge | 0.00 | 12.84 | $-$21.30 | 0.00 |
| Delta hedge (weekly) | $-$0.82 | 1.54 | $-$4.12 | 0.82 |
| Deep hedge (CVaR) | $-$0.65 | 1.38 | $-$3.41 | 0.65 |
| Deep hedge (Entropic) | $-$0.71 | 1.42 | $-$3.52 | 0.71 |

The deep hedging strategy learns to:

- **Trade less frequently** near at-the-money to reduce costs
- **Hedge more aggressively** in the tails where risk is highest
- **Underhedge slightly** when the cost of reducing residual risk exceeds the benefit

These adaptive behaviors emerge naturally from the optimization without being hand-coded.

---

## Incomplete Markets and Model-Free Hedging

### Stochastic Volatility

When the underlying follows a stochastic volatility model (e.g., Heston), the market is incomplete and perfect replication is impossible. Deep hedging naturally handles this:

- The strategy learns to partially hedge Vega risk using the underlying alone
- Adding a variance swap or VIX future to the tradeable set $S$ allows the network to discover the optimal Vega hedge

### Model-Free Training

A distinctive feature of deep hedging is that training can use **real market data** or **model-free scenarios**:

- Train on historical paths: No model assumption needed
- Train on GAN-generated paths: Synthetic data with realistic features
- Train on mixed scenarios: Combine historical and stressed paths

This eliminates model risk in the hedging strategy itself, even though a model may be used for initial pricing.

---

## Key Takeaways

1. **Deep hedging** formulates hedging as minimizing a convex risk measure over neural-network-parameterized strategies, naturally incorporating transaction costs and market frictions.

2. **Risk measure choice** determines the character of the hedge: entropic for utility maximization, CVaR for tail risk control, mean-variance for volatility reduction.

3. The framework produces **indifference prices** as a byproduct, correctly accounting for transaction costs and risk preferences.

4. Deep hedging strategies **outperform classical delta hedging** under realistic conditions with transaction costs, discrete rebalancing, and model uncertainty.

5. The approach extends naturally to **incomplete markets** and **model-free settings**, where classical replication theory does not apply.

---

## Further Reading

- Buehler, Gonon, Maystre & Niedermeyer (2019), "Deep Hedging"
- Buehler, Gonon, Maystre, Mohan & Niedermeyer (2019), "Deep Hedging: Hedging Derivatives Under Generic Market Frictions"
- Carbonneau & Godin (2021), "Equal Risk Pricing of Derivatives with Deep Learning"
- Horvath, Teichmann & Zuric (2021), "Deep Hedging Under Rough Volatility"
- Ruf & Wang (2020), "Neural Networks for Option Pricing and Hedging"

---

## Exercises

**Exercise 1.** Write out the hedging P&L for a strategy $\delta$ hedging a European call with payoff $Z = (S_T - K)^+$ under proportional transaction costs $c_k = \kappa |S_{t_k}||\delta_{t_k} - \delta_{t_{k-1}}|$. For $N = 4$ rebalancing periods, $S_0 = 100$, $K = 100$, and a specific price path $S = (100, 105, 98, 103, 110)$, compute the P&L for the constant strategy $\delta_{t_k} = 0.5$ (holding half a share at all times) with $\kappa = 0.001$. Compare to the P&L of the perfect hedge $\delta_{t_k} = 1$ for $k = 0,\ldots,3$.

??? success "Solution to Exercise 1"
    **Setup.** We have $N = 4$ rebalancing periods, price path $S = (S_0, S_1, S_2, S_3, S_4) = (100, 105, 98, 103, 110)$, strike $K = 100$, and $\kappa = 0.001$.

    The payoff is $Z = (S_T - K)^+ = (110 - 100)^+ = 10$.

    The hedging P&L is:

    $$
    \text{P\&L}(\delta) = -Z + \sum_{k=0}^{3} \delta_{t_k}(S_{t_{k+1}} - S_{t_k}) - \sum_{k=0}^{3} \kappa |S_{t_k}||\delta_{t_k} - \delta_{t_{k-1}}|
    $$

    with $\delta_{t_{-1}} = 0$.

    **Constant strategy $\delta_{t_k} = 0.5$ for all $k$:**

    Hedging gains:

    - $k=0$: $0.5 \times (105 - 100) = 2.5$
    - $k=1$: $0.5 \times (98 - 105) = -3.5$
    - $k=2$: $0.5 \times (103 - 98) = 2.5$
    - $k=3$: $0.5 \times (110 - 103) = 3.5$

    Total hedging gain: $2.5 - 3.5 + 2.5 + 3.5 = 5.0$

    Transaction costs:

    - $k=0$: $\kappa |S_0||\delta_0 - 0| = 0.001 \times 100 \times 0.5 = 0.05$
    - $k=1$: $\kappa |S_1||\delta_1 - \delta_0| = 0.001 \times 105 \times 0 = 0$
    - $k=2$: $\kappa |S_2||\delta_2 - \delta_1| = 0.001 \times 98 \times 0 = 0$
    - $k=3$: $\kappa |S_3||\delta_3 - \delta_2| = 0.001 \times 103 \times 0 = 0$

    Total cost: $0.05$

    $$
    \text{P\&L} = -10 + 5.0 - 0.05 = -5.05
    $$

    The hedge is poor because holding half a share does not fully replicate the call payoff.

    **Full hedge $\delta_{t_k} = 1$ for all $k$:**

    Hedging gains:

    - $k=0$: $1 \times (105 - 100) = 5$
    - $k=1$: $1 \times (98 - 105) = -7$
    - $k=2$: $1 \times (103 - 98) = 5$
    - $k=3$: $1 \times (110 - 103) = 7$

    Total hedging gain: $5 - 7 + 5 + 7 = 10$

    Transaction costs:

    - $k=0$: $0.001 \times 100 \times |1 - 0| = 0.10$
    - $k=1, 2, 3$: $0.001 \times S_{t_k} \times |1 - 1| = 0$ (no rebalancing needed)

    Total cost: $0.10$

    $$
    \text{P\&L} = -10 + 10 - 0.10 = -0.10
    $$

    The full hedge nearly replicates the payoff, losing only the initial transaction cost. This makes sense: holding one share perfectly tracks $S_T - S_0 = 10$, which equals the payoff $(S_T - K)^+ = 10$ on this particular path. The residual $-0.10$ is purely the cost of establishing the position.

---

**Exercise 2.** Explain the deep hedging optimization objective $\min_\delta \rho(-\text{P\&L}(\delta))$ where $\rho$ is a convex risk measure. For the entropic risk measure $\rho_\lambda(X) = \frac{1}{\lambda}\log(\mathbb{E}[e^{-\lambda X}])$, show that as $\lambda \to 0$, $\rho_\lambda(X) \to -\mathbb{E}[X]$ (risk-neutral limit), and as $\lambda \to \infty$, $\rho_\lambda(X) \to \text{ess sup}(-X)$ (worst-case limit). How does the choice of $\lambda$ affect the learned hedging strategy?

??? success "Solution to Exercise 2"
    **The optimization objective** $\min_\delta \rho(-\text{P\&L}(\delta))$ seeks the strategy that minimizes risk (as measured by $\rho$) of the hedge loss. Since $\rho$ is applied to the negative P&L, minimizing $\rho(-\text{P\&L})$ means reducing the risk of losses.

    **Risk-neutral limit ($\lambda \to 0$):**

    The entropic risk measure is $\rho_\lambda(X) = \frac{1}{\lambda}\log(\mathbb{E}[e^{-\lambda X}])$. As $\lambda \to 0$, expand the exponential using a Taylor series:

    $$
    e^{-\lambda X} = 1 - \lambda X + \frac{\lambda^2 X^2}{2} - \cdots
    $$

    $$
    \mathbb{E}[e^{-\lambda X}] = 1 - \lambda \mathbb{E}[X] + \frac{\lambda^2 \mathbb{E}[X^2]}{2} - \cdots
    $$

    Taking the logarithm:

    $$
    \log(\mathbb{E}[e^{-\lambda X}]) = \log\!\left(1 - \lambda\mathbb{E}[X] + O(\lambda^2)\right) = -\lambda\mathbb{E}[X] + O(\lambda^2)
    $$

    Therefore:

    $$
    \rho_\lambda(X) = \frac{1}{\lambda}\left(-\lambda\mathbb{E}[X] + O(\lambda^2)\right) = -\mathbb{E}[X] + O(\lambda)
    $$

    As $\lambda \to 0$: $\rho_\lambda(X) \to -\mathbb{E}[X]$. This is the risk-neutral limit where only the expected value matters, and the hedger is indifferent to variance.

    **Worst-case limit ($\lambda \to \infty$):**

    For large $\lambda$, the exponential $e^{-\lambda X}$ is dominated by the values where $X$ is most negative (i.e., the worst outcomes). Formally, by Varadhan's lemma (or by direct argument):

    $$
    \lim_{\lambda \to \infty} \frac{1}{\lambda}\log(\mathbb{E}[e^{-\lambda X}]) = \text{ess sup}(-X) = -\text{ess inf}(X)
    $$

    So $\rho_\lambda(X) \to \text{ess sup}(-X)$, which is the worst-case loss. In this limit, the hedger is infinitely risk-averse and optimizes against the worst possible outcome.

    **Effect of $\lambda$ on the hedging strategy:**

    - Small $\lambda$: The strategy minimizes expected loss, trading off mean P&L against cost. It may accept some tail risk if reducing it is expensive.
    - Moderate $\lambda$: The strategy balances expected P&L and risk aversion, overweighting bad outcomes. It trades more aggressively in scenarios with large potential losses.
    - Large $\lambda$: The strategy becomes very conservative, hedging against worst-case scenarios. It will incur higher costs to reduce tail exposure, potentially overhedging relative to the risk-neutral optimum.

---

**Exercise 3.** Classical delta hedging under Black-Scholes with weekly rebalancing and transaction costs of 10 bps achieves a P&L standard deviation of \$1.54 (from the example in the text). Deep hedging with CVaR optimization achieves \$1.38. Compute the percentage improvement. Discuss the economic intuition: what specific adaptive behaviors does the deep hedging strategy learn that delta hedging cannot? Why does delta hedging overtrade near the money?

??? success "Solution to Exercise 3"
    **Percentage improvement in P&L standard deviation:**

    $$
    \text{Improvement} = \frac{1.54 - 1.38}{1.54} \times 100\% = \frac{0.16}{1.54} \times 100\% \approx 10.4\%
    $$

    Deep hedging reduces P&L volatility by approximately 10.4%.

    **Adaptive behaviors of deep hedging:**

    1. **Reduced trading near the money.** When $S \approx K$, the Black-Scholes delta $\Delta = \Phi(d_1)$ is approximately 0.5 and its gamma $\Gamma = \phi(d_1)/(S\sigma\sqrt{T-t})$ is at its maximum. Delta hedging rebalances aggressively in this region because small price moves cause large delta changes. Each rebalance incurs transaction costs. Deep hedging recognizes that the marginal reduction in variance from this frequent rebalancing is outweighed by the cost, so it trades less.

    2. **More aggressive hedging in the tails.** When $S$ is far from $K$ (deep in- or out-of-the-money), delta is near 0 or 1 and gamma is small. Classical delta hedging barely trades here. However, deep hedging with a tail-risk measure (CVaR) recognizes that tail scenarios carry disproportionate risk, so it may maintain or adjust positions to protect against extreme moves.

    3. **Asymmetric behavior.** Deep hedging can learn that costs of underhedging and overhedging are asymmetric. For example, a short call position has unlimited upside risk but bounded downside. The optimal strategy may deliberately underhedge on the downside (saving costs) while hedging more tightly on the upside.

    **Why delta hedging overtrades near the money.** Delta hedging follows the rule $\delta_t = \partial V/\partial S$, which changes rapidly when gamma is large (near the money). With weekly rebalancing, each week the delta may shift by $\Delta\delta \approx \Gamma \cdot \Delta S$, which is largest near the money. The resulting transaction cost $\kappa |S||\Delta\delta|$ accumulates. Delta hedging has no mechanism to weigh these costs against risk reduction -- it mechanically tracks the model delta regardless of cost. Deep hedging, by contrast, jointly optimizes over the entire path and can learn to "smooth" its trading around the money, accepting slightly higher hedging variance to substantially reduce costs.

---

**Exercise 4.** Define the indifference price of a liability $Z$ in the deep hedging framework:

$$
p = \min_\delta \rho\left(Z - \sum_k \delta_{t_k}^\top \Delta S_{t_k} + \sum_k c_k\right) - \min_\delta \rho\left(-\sum_k \delta_{t_k}^\top \Delta S_{t_k} + \sum_k c_k\right)
$$

Explain why this price depends on the risk measure $\rho$ and the transaction cost structure. In the limit of zero transaction costs and the mean risk measure ($\rho = -\mathbb{E}$), show that the indifference price recovers the risk-neutral price. Why does the indifference price create a bid-ask spread?

??? success "Solution to Exercise 4"
    **Indifference price interpretation.** The indifference price $p$ is the price at which the hedger is equally well off with or without the liability $Z$. It satisfies:

    $$
    p = \underbrace{\min_\delta \rho\!\left(Z - \sum_k \delta_{t_k}^\top \Delta S_{t_k} + \sum_k c_k\right)}_{\text{Minimum risk with liability}} - \underbrace{\min_\delta \rho\!\left(-\sum_k \delta_{t_k}^\top \Delta S_{t_k} + \sum_k c_k\right)}_{\text{Minimum risk without liability}}
    $$

    The first term is the optimal residual risk when hedging the liability. The second is the optimal risk from trading alone (without liability). The difference is the "risk cost" of taking on $Z$.

    **Dependence on $\rho$.** The indifference price depends on $\rho$ because different risk measures weight outcomes differently. A highly risk-averse agent (large $\lambda$ in the entropic measure) values the liability more negatively (charges a higher price to take it on) because they weight the worst outcomes more heavily. A risk-neutral agent values it at the expected discounted payoff.

    **Dependence on transaction costs.** With costs, the hedger cannot perfectly replicate, so residual risk remains. Higher costs mean worse hedging, larger residual risk, and thus higher indifference prices (for selling) or lower prices (for buying).

    **Recovery of risk-neutral price.** Set $\rho = -\mathbb{E}$ and $c_k = 0$. Then:

    $$
    p = \min_\delta\left(-\mathbb{E}\!\left[-Z + \sum_k \delta_{t_k}^\top \Delta S_{t_k}\right]\right) - \min_\delta\left(-\mathbb{E}\!\left[\sum_k \delta_{t_k}^\top \Delta S_{t_k}\right]\right)
    $$

    $$
    = \min_\delta\left(\mathbb{E}[Z] - \mathbb{E}\!\left[\sum_k \delta_{t_k}^\top \Delta S_{t_k}\right]\right) - \min_\delta\left(-\mathbb{E}\!\left[\sum_k \delta_{t_k}^\top \Delta S_{t_k}\right]\right)
    $$

    Under the risk-neutral measure $\mathbb{Q}$, $\mathbb{E}^{\mathbb{Q}}[\Delta S_{t_k}] = rS_{t_k}\Delta t_k$ (approximately). For the mean-risk measure, the hedging gain does not affect the minimum (since $\mathbb{E}[\delta^\top \Delta S]$ can be any value by choosing $\delta$, but under no-arbitrage, $\mathbb{E}^{\mathbb{Q}}[\Delta \tilde{S}] = 0$ for discounted prices). Thus the minimum in both terms is achieved at any $\delta$, giving:

    $$
    p = \mathbb{E}^{\mathbb{Q}}[Z] = e^{-rT}\mathbb{E}^{\mathbb{Q}}[H(S_T)]
    $$

    which is the standard risk-neutral price.

    **Why indifference pricing creates a bid-ask spread.** The indifference price depends on the direction of the trade (buying vs. selling the liability). The seller's indifference price $p_{\text{ask}}$ uses $+Z$ (the cost of taking on the liability), while the buyer's price $p_{\text{bid}}$ uses $-Z$ (the benefit of receiving the payoff). Due to transaction costs and risk aversion, $p_{\text{ask}} > p_{\text{bid}}$, creating a natural bid-ask spread. This spread increases with transaction costs (less effective hedging) and risk aversion (greater compensation demanded for residual risk).

---

**Exercise 5.** In an incomplete market (e.g., stochastic volatility without a volatility instrument), deep hedging can only partially reduce risk. Suppose the underlying follows a Heston model with stochastic variance $v_t$. The hedger can trade only the stock $S$. Explain what residual risk remains after optimal hedging: is it delta risk, Vega risk, or both? If the hedger is also allowed to trade a variance swap, how does the deep hedging framework automatically discover the optimal Vega hedge?

??? success "Solution to Exercise 5"
    **Residual risk in an incomplete market.**

    Under the Heston model, the stock price $S_t$ and variance $v_t$ are driven by two correlated Brownian motions $W^S$ and $W^v$. If the hedger can only trade the stock $S$, they can control exposure to $W^S$ but not to $W^v$. Specifically:

    - **Delta risk** can be (approximately) hedged by adjusting the stock position. The strategy sets $\delta_t$ to offset the sensitivity $\partial V/\partial S$.

    - **Vega risk** ($\partial V/\partial v$) cannot be directly hedged because there is no tradeable instrument driven purely by $W^v$. The stock has some exposure to $v_t$ through the correlation $\rho$, but this provides only partial Vega hedging. The residual risk is primarily **Vega risk** -- the unhedgeable component corresponding to moves in variance that are orthogonal to stock price moves.

    More precisely, the option's P&L can be decomposed as:

    $$
    dV \approx \Delta \, dS + \frac{1}{2}\Gamma \, (dS)^2 + \mathcal{V} \, dv + \Theta \, dt
    $$

    After delta hedging ($\delta = \Delta$), the residual is:

    $$
    dV - \Delta \, dS \approx \frac{1}{2}\Gamma \, (dS)^2 + \mathcal{V} \, dv + \Theta \, dt
    $$

    The $\mathcal{V} \, dv$ term contains exposure to $W^v$ that cannot be eliminated using the stock alone. Through the correlation, part of $dv$ is hedgeable via $dS$, but the orthogonal component $\sqrt{1 - \rho^2} \, dW^v$ remains.

    **Adding a variance swap.** If the hedger can also trade a variance swap (or VIX future) $P_t$ with exposure to $v_t$, then the strategy becomes $(\delta^S_t, \delta^v_t)$ where $\delta^v_t$ is the position in the variance instrument. The deep hedging framework automatically discovers the optimal allocation:

    $$
    \min_{\delta^S, \delta^v} \rho\!\left(-\text{P\&L}(\delta^S, \delta^v)\right)
    $$

    The network takes both $S_t$ and $P_t$ (or $v_t$) as inputs and outputs positions in both instruments. Through training, the network learns to set $\delta^v_t$ to offset the Vega exposure: the hedging P&L from the variance instrument $\delta^v_t \, dP_t$ cancels the $\mathcal{V} \, dv$ term. The deep hedging framework discovers this Vega hedge without being explicitly told about Greeks -- it simply finds the strategy that minimizes the risk measure, and that strategy turns out to include Vega hedging as an emergent behavior.

---

**Exercise 6.** Describe how deep hedging can be trained on real historical data rather than model-simulated paths. What are the advantages and challenges of this model-free approach? Discuss: (a) limited data and overfitting risk, (b) non-stationarity of market dynamics, (c) inability to generate new stress scenarios, and (d) how GAN-generated synthetic paths could supplement historical data while preserving realistic features.

??? success "Solution to Exercise 6"
    **Training on historical data** means using actual observed price paths $\{S_{t_0}^{(i)}, \ldots, S_{t_N}^{(i)}\}$ rather than model-simulated ones. The network learns the hedging strategy directly from real market dynamics.

    **Advantages:**

    - No model risk: the strategy adapts to whatever dynamics the market actually exhibits, including fat tails, volatility clustering, jumps, and regime changes.
    - Realistic transaction costs, bid-ask spreads, and liquidity effects are naturally captured if the data includes these features.
    - No need to specify or calibrate a stochastic model.

    **Challenges:**

    **(a) Limited data and overfitting.** Historical data is finite. For a daily-rebalanced strategy over 10 years, there are roughly 2,500 trading days. With $N = 52$ weekly rebalancing points per year, there are only about 520 paths of length 52 available (if paths are non-overlapping). With overlapping windows, more paths can be extracted, but they are highly correlated. The neural network, with potentially thousands of parameters, can easily overfit to the specific patterns in the training set. Regularization (dropout, weight decay, early stopping) and careful cross-validation are essential.

    **(b) Non-stationarity.** Financial markets exhibit structural changes: volatility regimes shift, correlations break down, new instruments appear, and regulatory changes alter market microstructure. A strategy trained on 2010--2015 data may perform poorly in 2020 if the dynamics have changed. Solutions include using rolling windows for training, weighting recent data more heavily, and including regime indicators as input features.

    **(c) Inability to generate stress scenarios.** Historical data reflects what *did* happen, not what *could* happen. Rare events (market crashes, flash crashes, liquidity crises) may appear zero or once in the training set, giving the network insufficient information to hedge against them. The strategy may be dangerously exposed to scenarios not represented in the data.

    **(d) GAN-generated synthetic paths.** Generative Adversarial Networks (GANs) can learn the distribution of historical paths and generate new synthetic paths that share the statistical properties (volatility clustering, fat tails, correlation structure) of real data. Benefits include:

    - Unlimited data: generate as many paths as needed, eliminating overfitting from finite samples.
    - Novel scenarios: the GAN can interpolate and (to some extent) extrapolate, producing paths not exactly seen in history but consistent with learned dynamics.
    - Stress testing: the GAN can be conditioned or modified to generate stressed scenarios (e.g., by amplifying tail events).
    - Combination approach: train on a mixture of real paths and GAN-generated paths, with the real paths anchoring the distribution and synthetic paths providing diversity. This mitigates both the data scarcity problem and the non-stationarity issue.

---

**Exercise 7.** For a recurrent (LSTM) deep hedging architecture, the hidden state $h_k$ carries information from previous time steps. Compare this to the feedforward architecture where each $\delta_{t_k} = \mathcal{N}_{\theta_k}(S_{t_k}, \delta_{t_{k-1}}, T - t_k)$. Discuss when each architecture is preferable. For a path-dependent option (e.g., Asian option), argue that the recurrent architecture has a natural advantage because the payoff depends on the entire price path. What information must the feedforward architecture include in its input to match the recurrent architecture's performance?

??? success "Solution to Exercise 7"
    **Recurrent (LSTM) architecture:**

    The LSTM maintains a hidden state $h_k$ that is updated at each time step:

    $$
    h_{k+1}, \delta_{t_k} = \text{LSTM}_\theta(I_{t_k}, h_k)
    $$

    The hidden state $h_k$ serves as a learned summary of the entire price history $(S_{t_0}, \ldots, S_{t_k})$. The network automatically decides which historical features are relevant for the hedging decision.

    **Feedforward architecture:**

    Each $\delta_{t_k} = \mathcal{N}_{\theta_k}(S_{t_k}, \delta_{t_{k-1}}, T - t_k)$ is a function of only the current state, previous holding, and time to maturity. It has no explicit memory of earlier price levels.

    **When feedforward is preferable:**

    - For **path-independent options** (European calls/puts), the optimal hedge depends only on the current state (price, time, possibly implied vol). No history is needed. The feedforward architecture is simpler, has fewer parameters (no recurrent gates), and trains faster.
    - When the Markov property holds: if the information set $I_{t_k}$ contains all relevant state variables, no history is needed.
    - For short-dated options with few rebalancing steps, the overhead of the LSTM gates is unnecessary.

    **When LSTM is preferable:**

    - For **path-dependent options** (Asian, lookback, barrier), the payoff depends on the entire path. The optimal hedge therefore depends on path history.
    - When relevant features are not known in advance: the LSTM can learn to extract features (e.g., realized volatility, trend indicators) from the raw price sequence.
    - When the number of rebalancing steps is large and the optimal hedge has complex path dependencies.

    **Asian option example.** An Asian call pays $(\frac{1}{N}\sum_{k} S_{t_k} - K)^+$. The hedge at time $t_k$ depends on the running average $\bar{S}_k = \frac{1}{k}\sum_{j=0}^{k} S_{t_j}$, because this determines how far the payoff is in- or out-of-the-money. The LSTM naturally tracks this running average in its hidden state. The feedforward architecture cannot access $\bar{S}_k$ unless it is explicitly provided as an input.

    **Information needed by feedforward to match LSTM:**

    To match the LSTM's performance, the feedforward architecture must include sufficient statistics of the price history in its input vector. For common path-dependent options:

    - **Asian option:** Include the running average $\bar{S}_k$ (or equivalently, the running sum $\sum_{j \leq k} S_{t_j}$) as an input feature.
    - **Lookback option:** Include the running maximum $\max_{j \leq k} S_{t_j}$ and/or running minimum.
    - **Barrier option:** Include an indicator for whether the barrier has been breached: $\mathbf{1}\{\max_{j \leq k} S_{t_j} \geq B\}$.
    - **General path dependence:** Include a set of hand-crafted features: realized volatility $\hat{\sigma}_k$, momentum $S_{t_k} - S_{t_{k-m}}$, and other summary statistics.

    The LSTM's advantage is that it discovers these features automatically from data, without manual feature engineering. However, when the relevant features are known (as they often are for standard path-dependent options), explicitly including them in the feedforward input achieves comparable performance with a simpler and more interpretable architecture.
