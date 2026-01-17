# Incomplete Markets and Pricing Bounds

In **incomplete markets**, not all risks can be perfectly hedged, leading to **non-uniqueness** of equivalent martingale measures. Arbitrage-free prices form an **interval** rather than a single value, and additional criteria are needed to select a specific price.

---

## Complete vs Incomplete Markets

### Complete Markets

- Every contingent claim can be replicated by trading
- Unique equivalent martingale measure (EMM)
- Unique arbitrage-free price
- **Example**: Black-Scholes model

### Incomplete Markets

- Some claims cannot be perfectly replicated
- Multiple equivalent martingale measures exist
- Arbitrage-free prices form an interval
- **Examples**: Stochastic volatility, jump-diffusion, transaction costs

### Sources of Incompleteness

| Source | Description |
|--------|-------------|
| **Extra risk factors** | More randomness than tradeable assets |
| **Trading constraints** | Short-selling restrictions, discrete trading |
| **Transaction costs** | Bid-ask spreads, market impact |
| **Model uncertainty** | Unknown true probability measure |

---

## Pricing Bounds

### The No-Arbitrage Interval

Let $\mathcal{Q}$ be the set of all equivalent martingale measures. For a claim with payoff $H$:

$$
\boxed{
\underline{\pi}(H) = \inf_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[e^{-rT}H] \leq \pi(H) \leq \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[e^{-rT}H] = \overline{\pi}(H)
}
$$

Any price in $[\underline{\pi}(H), \overline{\pi}(H)]$ is **arbitrage-free**.

### Interpretation

- $\overline{\pi}(H)$: Maximum price a buyer should pay
- $\underline{\pi}(H)$: Minimum price a seller should accept
- $\overline{\pi}(H) - \underline{\pi}(H)$: Measure of market incompleteness

---

## Superhedging and Subhedging

### Superhedging Price

The **superhedging price** is the minimum initial capital needed to dominate the payoff:

$$
\boxed{
\overline{\pi}(H) = \inf\left\{x : \exists \theta \text{ s.t. } x + \int_0^T \theta_t\,dS_t \geq H \text{ a.s.}\right\}
}
$$

**Duality theorem**: Under technical conditions, the superhedging price equals the upper bound.

### Subhedging Price

The **subhedging price** is the maximum initial capital that can be extracted while covering the payoff:

$$
\underline{\pi}(H) = \sup\left\{x : \exists \theta \text{ s.t. } x + \int_0^T \theta_t\,dS_t \leq H \text{ a.s.}\right\}
$$

---

## Selecting a Price

When prices are not unique, additional criteria select a specific price.

### 1. Minimal Martingale Measure

Choose $\mathbb{Q}^{\min}$ that preserves the structure of the orthogonal martingale component:

$$
\frac{d\mathbb{Q}^{\min}}{d\mathbb{P}} = \mathcal{E}\left(-\int_0^T \theta^{(1)}_t\,dW_t^{(1)}\right)
$$

where only the traded risk is adjusted.

**Properties**:
- Minimal entropy distance from $\mathbb{P}$
- Preserves "unhedgeable" risk distribution
- Popular in stochastic volatility models

### 2. Variance-Optimal Measure

Choose $\mathbb{Q}$ to minimize the variance of the pricing error:

$$
\mathbb{Q}^{\text{var}} = \arg\min_{\mathbb{Q} \in \mathcal{Q}} \text{Var}^{\mathbb{P}}\left[\frac{d\mathbb{Q}}{d\mathbb{P}}\right]
$$

### 3. Utility Indifference Pricing

Price based on an investor's utility function $U$:

$$
\boxed{
\pi^U(H) = x \text{ such that } \sup_\theta \mathbb{E}[U(X_T^x)] = \sup_\theta \mathbb{E}[U(X_T^0 + H)]
}
$$

The price makes the investor indifferent between buying the claim or not.

**Popular choices**: Exponential utility $U(x) = -e^{-\gamma x}$

### 4. Entropy Minimization

Choose $\mathbb{Q}$ closest to $\mathbb{P}$ in relative entropy:

$$
\mathbb{Q}^{\text{ent}} = \arg\min_{\mathbb{Q} \in \mathcal{Q}} H(\mathbb{Q} | \mathbb{P}) = \arg\min_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}\left[\log\frac{d\mathbb{Q}}{d\mathbb{P}}\right]
$$

---

## Example: Stochastic Volatility

### Setup

$$
\begin{aligned}
dS_t &= rS_t\,dt + \sqrt{v_t}S_t\,dW_t^{(1)} \\
dv_t &= \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
\end{aligned}
$$

with $\text{Corr}(dW^{(1)}, dW^{(2)}) = \rho$.

### Incompleteness

- 2 sources of randomness ($W^{(1)}, W^{(2)}$)
- Only 1 tradeable asset ($S$)
- Cannot hedge variance risk with the stock alone

### Market Price of Volatility Risk

The measure change involves:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}} = \mathcal{E}\left(-\int_0^T \theta_t^{(1)}\,dW_t^{(1)} - \int_0^T \theta_t^{(2)}\,dW_t^{(2)}\right)
$$

- $\theta_t^{(1)} = (\mu - r)/\sqrt{v_t}$ is determined by no-arbitrage
- $\theta_t^{(2)} = \lambda(t, v_t)$ is **free** (volatility risk premium)

### Different Choices of $\lambda$

| Choice | Measure | Effect |
|--------|---------|--------|
| $\lambda = 0$ | Minimal | No volatility risk premium |
| $\lambda = \lambda_0\sqrt{v}$ | Proportional | Common parameterization |
| Calibrated | Market-implied | Matches option prices |

---

## Practical Implications

### Pricing

1. **Model calibration**: Implicitly selects a martingale measure
2. **Different models**: May give different prices even with same vanilla fit
3. **Exotic pricing**: Sensitive to measure choice

### Hedging

1. **Perfect replication impossible**: Some residual risk remains
2. **Optimal hedging**: Minimize variance/utility of hedging error
3. **Super-replication**: Conservative but expensive

### Risk Management

1. **Pricing bounds**: Quantify model uncertainty
2. **Stress testing**: Explore range of possible prices
3. **Reserve setting**: May use worst-case prices

---

## Mathematical Framework

### The Set of Martingale Measures

For a market with price process $S$ under $\mathbb{P}$:

$$
\mathcal{Q} = \{\mathbb{Q} \sim \mathbb{P} : S/B \text{ is a } \mathbb{Q}\text{-local martingale}\}
$$

### Characterization (for diffusions)

Each $\mathbb{Q} \in \mathcal{Q}$ corresponds to a market price of risk $\theta$ satisfying:

1. $\theta$ removes the excess drift of $S$
2. $\theta$ satisfies integrability conditions (Novikov)

The remaining degrees of freedom parameterize $\mathcal{Q}$.

### FTAP for Incomplete Markets

**Theorem**: The market is arbitrage-free if and only if $\mathcal{Q} \neq \emptyset$.

**Corollary**: The market is complete if and only if $|\mathcal{Q}| = 1$.

---

## Width of the Pricing Interval

### Factors Affecting Width

| Factor | Effect on Width |
|--------|-----------------|
| **Degree of incompleteness** | More unhedgeable risk → wider |
| **Claim payoff structure** | Path-dependent → wider |
| **Time to maturity** | Longer → wider |
| **Leverage of claim** | Higher → wider |

### Example: Variance Swap

In stochastic volatility, variance swap prices span a wide interval because variance is directly exposed to the unhedgeable volatility risk.

---

## Summary

$$
\boxed{
\underline{\pi}(H) = \inf_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[e^{-rT}H] \leq \pi(H) \leq \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[e^{-rT}H] = \overline{\pi}(H)
}
$$

| Concept | Description |
|---------|-------------|
| **Incomplete market** | More risks than tradeable assets |
| **Multiple EMMs** | Non-unique risk-neutral measure |
| **Pricing bounds** | Arbitrage-free interval $[\underline{\pi}, \overline{\pi}]$ |
| **Superhedging** | Upper bound = cost of dominating strategy |

| Selection Criterion | Principle |
|---------------------|-----------|
| Minimal martingale | Preserve orthogonal risk |
| Variance-optimal | Minimize density variance |
| Utility indifference | Investor's risk preferences |
| Entropy minimization | Stay close to physical measure |

**In incomplete markets, arbitrage-free pricing provides bounds rather than unique prices, requiring additional economic or mathematical criteria to pin down specific values.**
