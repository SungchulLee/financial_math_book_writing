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

---

**Exercise 2.** Explain the deep hedging optimization objective $\min_\delta \rho(-\text{P\&L}(\delta))$ where $\rho$ is a convex risk measure. For the entropic risk measure $\rho_\lambda(X) = \frac{1}{\lambda}\log(\mathbb{E}[e^{-\lambda X}])$, show that as $\lambda \to 0$, $\rho_\lambda(X) \to -\mathbb{E}[X]$ (risk-neutral limit), and as $\lambda \to \infty$, $\rho_\lambda(X) \to \text{ess sup}(-X)$ (worst-case limit). How does the choice of $\lambda$ affect the learned hedging strategy?

---

**Exercise 3.** Classical delta hedging under Black-Scholes with weekly rebalancing and transaction costs of 10 bps achieves a P&L standard deviation of \$1.54 (from the example in the text). Deep hedging with CVaR optimization achieves \$1.38. Compute the percentage improvement. Discuss the economic intuition: what specific adaptive behaviors does the deep hedging strategy learn that delta hedging cannot? Why does delta hedging overtrade near the money?

---

**Exercise 4.** Define the indifference price of a liability $Z$ in the deep hedging framework:

$$
p = \min_\delta \rho\left(Z - \sum_k \delta_{t_k}^\top \Delta S_{t_k} + \sum_k c_k\right) - \min_\delta \rho\left(-\sum_k \delta_{t_k}^\top \Delta S_{t_k} + \sum_k c_k\right)
$$

Explain why this price depends on the risk measure $\rho$ and the transaction cost structure. In the limit of zero transaction costs and the mean risk measure ($\rho = -\mathbb{E}$), show that the indifference price recovers the risk-neutral price. Why does the indifference price create a bid-ask spread?

---

**Exercise 5.** In an incomplete market (e.g., stochastic volatility without a volatility instrument), deep hedging can only partially reduce risk. Suppose the underlying follows a Heston model with stochastic variance $v_t$. The hedger can trade only the stock $S$. Explain what residual risk remains after optimal hedging: is it delta risk, Vega risk, or both? If the hedger is also allowed to trade a variance swap, how does the deep hedging framework automatically discover the optimal Vega hedge?

---

**Exercise 6.** Describe how deep hedging can be trained on real historical data rather than model-simulated paths. What are the advantages and challenges of this model-free approach? Discuss: (a) limited data and overfitting risk, (b) non-stationarity of market dynamics, (c) inability to generate new stress scenarios, and (d) how GAN-generated synthetic paths could supplement historical data while preserving realistic features.

---

**Exercise 7.** For a recurrent (LSTM) deep hedging architecture, the hidden state $h_k$ carries information from previous time steps. Compare this to the feedforward architecture where each $\delta_{t_k} = \mathcal{N}_{\theta_k}(S_{t_k}, \delta_{t_{k-1}}, T - t_k)$. Discuss when each architecture is preferable. For a path-dependent option (e.g., Asian option), argue that the recurrent architecture has a natural advantage because the payoff depends on the entire price path. What information must the feedforward architecture include in its input to match the recurrent architecture's performance?
