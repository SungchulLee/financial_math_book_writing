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

### Different Choices of λ

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

---

## Exercises

**Exercise 1.** In the Black-Scholes model, the market is complete because there is one source of randomness and one traded asset (plus the bond). In the Heston model, there are two sources of randomness but still only one traded risky asset. (a) Explain why this leads to incompleteness. (b) If variance swaps were liquidly traded, would the Heston market become complete? Justify your answer.

---

**Exercise 2.** The superhedging price $\overline{\pi}(H) = \inf\{x : \exists \theta \text{ s.t. } x + \int_0^T \theta_t\,dS_t \geq H \text{ a.s.}\}$ is the cost of the cheapest portfolio that dominates the payoff. (a) Explain why the superhedging price is always at least as large as any arbitrage-free price. (b) Why is the superhedging price often impractically large for insurance products? (c) How does the subhedging price provide a lower bound?

---

**Exercise 3.** The utility indifference price $\pi^U(H)$ satisfies $\sup_\theta \mathbb{E}[U(X_T^{x-\pi^U}+H)] = \sup_\theta \mathbb{E}[U(X_T^x)]$. For exponential utility $U(x) = -e^{-\gamma x}$: (a) Show that the indifference price is independent of the investor's initial wealth $x$. (b) Explain why the indifference price lies in the no-arbitrage interval $[\underline{\pi}, \overline{\pi}]$. (c) What happens to $\pi^U$ as $\gamma \to 0$ (risk-neutral investor) and as $\gamma \to \infty$ (infinitely risk-averse)?

---

**Exercise 4.** For the Heston model, the market price of volatility risk $\lambda(t, v_t)$ is not determined by no-arbitrage. (a) Describe how calibration to market option prices implicitly selects a specific $\lambda$. (b) Explain why two different calibrated Heston models (with different parameters but identical vanilla fits) can give different prices for exotic options. (c) How does this relate to the concept of "model risk"?

---

**Exercise 5.** List the four pricing measure selection criteria discussed: minimal martingale, variance-optimal, utility indifference, and entropy minimization. For each, (a) state the defining principle, (b) give one advantage, and (c) describe a situation where that criterion would be preferred.

---

**Exercise 6.** The FTAP (Fundamental Theorem of Asset Pricing) states that the market is complete if and only if there exists exactly one equivalent martingale measure. Using this theorem, prove that adding a liquidly traded variance swap to the Heston model makes the market complete. How many equivalent martingale measures exist before and after adding this instrument?

---

## Solutions

??? success "Solution to Exercise 1"
    **(a)** In the Heston model, the dynamics under the risk-neutral measure are

    $$
    \begin{aligned}
    dS_t &= rS_t\,dt + \sqrt{v_t}S_t\,dW_t^{(1)} \\
    dv_t &= \kappa(\theta - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2)}
    \end{aligned}
    $$

    with $\text{Corr}(dW^{(1)}, dW^{(2)}) = \rho$. There are two independent sources of randomness ($W^{(1)}$ and $W^{(2)}$) but only one traded risky asset $S$ (plus the risk-free bond). To replicate an arbitrary contingent claim, we need as many tradeable assets as independent risk factors. Since we have 2 risk factors but only 1 risky asset, we cannot span the full space of contingent claims. Specifically, the volatility risk driven by $W^{(2)}$ cannot be hedged using $S$ alone, making the market incomplete.

    **(b)** Yes, adding a liquidly traded variance swap would make the Heston market complete. A variance swap pays the realized variance $\int_0^T v_t\,dt$ and is directly sensitive to the variance process $v_t$. With $S$ and the variance swap, we now have two traded instruments whose prices are driven by the two independent Brownian motions $W^{(1)}$ and $W^{(2)}$. The stock $S$ is primarily exposed to $W^{(1)}$ (and partially to $W^{(2)}$ through correlation), while the variance swap is exposed to $W^{(2)}$. Together, they span the full risk space: any contingent claim can be replicated by dynamically trading $S$, the variance swap, and the bond. With two independent risk factors and two independent traded instruments, the market becomes complete, and the equivalent martingale measure becomes unique.

??? success "Solution to Exercise 2"
    **(a)** The superhedging price satisfies $x + \int_0^T \theta_t\,dS_t \geq H$ almost surely for some strategy $\theta$. For any equivalent martingale measure $\mathbb{Q} \in \mathcal{Q}$, taking expectations under $\mathbb{Q}$:

    $$
    x + \mathbb{E}^{\mathbb{Q}}\left[\int_0^T \theta_t\,dS_t\right] \geq \mathbb{E}^{\mathbb{Q}}[H]
    $$

    Since $S$ is a $\mathbb{Q}$-martingale (after discounting), the stochastic integral has zero expectation (under appropriate integrability conditions), so $x \geq \mathbb{E}^{\mathbb{Q}}[e^{-rT}H]$. This holds for every $\mathbb{Q} \in \mathcal{Q}$, so

    $$
    \overline{\pi}(H) \geq \sup_{\mathbb{Q} \in \mathcal{Q}} \mathbb{E}^{\mathbb{Q}}[e^{-rT}H]
    $$

    The duality theorem states that equality holds under technical conditions. Therefore, the superhedging price is at least as large as any arbitrage-free price (which lies in the interval).

    **(b)** For insurance products, the payoff $H$ can take extreme values (e.g., catastrophic losses), and the superhedging strategy must cover the worst-case scenario with probability one. This requires enough capital to cover even the most extreme realizations of $H$, making the superhedging price very conservative and impractically expensive. For example, superhedging a put option in a jump-diffusion model requires hedging against arbitrarily large downward jumps, leading to a superhedging price close to the strike price itself.

    **(c)** The subhedging price is $\underline{\pi}(H) = \sup\{x : \exists \theta \text{ s.t. } x + \int_0^T \theta_t\,dS_t \leq H \text{ a.s.}\}$. By an analogous argument, for any $\mathbb{Q} \in \mathcal{Q}$, taking expectations yields $x \leq \mathbb{E}^{\mathbb{Q}}[e^{-rT}H]$, so $\underline{\pi}(H) \leq \inf_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}[e^{-rT}H]$. With duality, equality holds and $\underline{\pi}(H)$ equals the lower bound of the no-arbitrage interval, providing the minimum price a seller should accept.

??? success "Solution to Exercise 3"
    **(a)** For exponential utility $U(x) = -e^{-\gamma x}$, the indifference price $\pi^U$ satisfies

    $$
    \sup_\theta \mathbb{E}[-e^{-\gamma(X_T^{x-\pi^U} + H)}] = \sup_\theta \mathbb{E}[-e^{-\gamma X_T^x}]
    $$

    Since the wealth process is $X_T^{x} = x + \int_0^T \theta_t\,dS_t$, we can write

    $$
    \sup_\theta \mathbb{E}[-e^{-\gamma(x - \pi^U + G + H)}] = \sup_\theta \mathbb{E}[-e^{-\gamma(x + G)}]
    $$

    where $G = \int_0^T \theta_t\,dS_t$ is the trading gain. Factoring out the constant $e^{-\gamma x}$ from both sides:

    $$
    e^{-\gamma(x-\pi^U)} \sup_\theta \mathbb{E}[-e^{-\gamma(G+H)}] = e^{-\gamma x} \sup_\theta \mathbb{E}[-e^{-\gamma G}]
    $$

    Dividing both sides by $-e^{-\gamma x}$:

    $$
    e^{\gamma \pi^U} \inf_\theta \mathbb{E}[e^{-\gamma(G+H)}] = \inf_\theta \mathbb{E}[e^{-\gamma G}]
    $$

    The factor $e^{-\gamma x}$ cancels completely, so $\pi^U$ does not depend on $x$. This is the **translation invariance** property of exponential utility.

    **(b)** If $\pi^U > \overline{\pi}(H)$, then an investor would overpay relative to the superhedging price, and a seller could superhedge the claim with a sure profit, creating an arbitrage for the seller. If $\pi^U < \underline{\pi}(H)$, then the seller would accept less than the subhedging price, and the buyer could create an arbitrage. Therefore, the indifference price must satisfy $\underline{\pi}(H) \leq \pi^U(H) \leq \overline{\pi}(H)$.

    **(c)** As $\gamma \to 0$ (risk-neutral investor), the investor becomes indifferent to risk. The indifference price converges to the expected discounted payoff under the minimal martingale measure, i.e., $\pi^U \to \mathbb{E}^{\mathbb{Q}^{\min}}[e^{-rT}H]$.

    As $\gamma \to \infty$ (infinitely risk-averse investor), the investor demands full protection against the worst case. The indifference price for a buyer converges to the superhedging price: $\pi^U \to \overline{\pi}(H)$. This is because an infinitely risk-averse agent only accepts positions that are hedged with certainty.

??? success "Solution to Exercise 4"
    **(a)** Calibrating the Heston model to market option prices means choosing parameters $(\kappa, \theta, \xi, \rho, v_0)$ so that model prices match observed vanilla option prices across strikes and maturities. Once these parameters are fixed, the dynamics under $\mathbb{Q}$ are fully specified, including the drift of the variance process. Since the drift under $\mathbb{Q}$ incorporates the market price of volatility risk $\lambda$, calibration implicitly determines $\lambda$ through the relationship between the $\mathbb{P}$-drift and the $\mathbb{Q}$-drift. Specifically, if under $\mathbb{P}$ we have $dv_t = [\kappa(\theta - v_t) - \lambda(t,v_t)]\,dt + \xi\sqrt{v_t}\,dW_t^{(2),\mathbb{P}}$, then matching market prices fixes the $\mathbb{Q}$-drift $\kappa(\theta - v_t)$ and hence implicitly determines $\lambda$.

    **(b)** Two Heston models with different parameters $(\kappa_1, \theta_1, \xi_1, \rho_1, v_{0,1})$ and $(\kappa_2, \theta_2, \xi_2, \rho_2, v_{0,2})$ can produce identical prices for all vanilla options (European calls and puts across all strikes and maturities). However, exotic options depend on the full joint distribution of $(S_t, v_t)$ over the path, not just marginal distributions at fixed times. Different parameter sets imply different dynamics for the variance process, leading to different path-dependent behaviors. For example, a barrier option or a cliquet depends on the joint evolution, which differs between the two calibrated models.

    **(c)** This is a manifestation of **model risk**: the risk that the chosen model, even when calibrated to liquid instruments, gives incorrect prices for illiquid or exotic products. In incomplete markets, multiple martingale measures are consistent with observed vanilla prices, and each gives a different exotic price. The spread between these prices quantifies model risk.

??? success "Solution to Exercise 5"
    **1. Minimal Martingale Measure**

    - **(a) Principle**: Choose $\mathbb{Q}^{\min}$ so that only the traded risk (the component driving $S$) is adjusted, while the orthogonal (unhedgeable) component retains its $\mathbb{P}$-distribution.
    - **(b) Advantage**: Preserves the structure of unhedgeable risk, making minimal assumptions about unobservable risk premia.
    - **(c) Preferred when**: Pricing in stochastic volatility models where one wants a "neutral" baseline that does not impose any view on the volatility risk premium.

    **2. Variance-Optimal Measure**

    - **(a) Principle**: Choose $\mathbb{Q}^{\text{var}}$ to minimize $\text{Var}^{\mathbb{P}}[d\mathbb{Q}/d\mathbb{P}]$, i.e., the variance of the Radon-Nikodym derivative under the physical measure.
    - **(b) Advantage**: Leads to the best mean-variance hedging strategy; the resulting hedge minimizes the $L^2$ hedging error.
    - **(c) Preferred when**: Constructing optimal hedging portfolios in a mean-variance framework, for example when a trader wants to minimize the variance of their P&L.

    **3. Utility Indifference Pricing**

    - **(a) Principle**: Price $\pi^U(H)$ makes the investor indifferent between holding the claim (with hedging) and not holding it, given utility function $U$.
    - **(b) Advantage**: Incorporates the investor's specific risk preferences and provides economically meaningful prices that account for risk aversion.
    - **(c) Preferred when**: Pricing illiquid or non-tradeable risks (e.g., insurance liabilities, weather derivatives) where an investor's risk appetite directly influences the acceptable price.

    **4. Entropy Minimization**

    - **(a) Principle**: Choose $\mathbb{Q}^{\text{ent}}$ to minimize the relative entropy (Kullback-Leibler divergence) $H(\mathbb{Q}|\mathbb{P}) = \mathbb{E}^{\mathbb{Q}}[\log(d\mathbb{Q}/d\mathbb{P})]$.
    - **(b) Advantage**: Stays as close as possible to the physical measure in an information-theoretic sense, making the least distortion to the real-world probabilities.
    - **(c) Preferred when**: Pricing in models where one wants to remain close to historical/statistical estimates, such as in credit derivatives or emerging market products where the physical measure is estimated from data.

??? success "Solution to Exercise 6"
    **Before adding the variance swap**: The Heston model has two sources of randomness ($W^{(1)}$ and $W^{(2)}$) but only one traded risky asset $S$. By the Second Fundamental Theorem of Asset Pricing, the market is complete if and only if $|\mathcal{Q}| = 1$. Since there is one "free" parameter (the market price of volatility risk $\lambda$), there are infinitely many equivalent martingale measures $\mathbb{Q} \in \mathcal{Q}$.

    **After adding the variance swap**: Consider the market with two traded instruments: the stock $S$ (driven primarily by $W^{(1)}$) and the variance swap $V^{\text{var}}$ (driven primarily by $W^{(2)}$ through the variance process). The dynamics under any $\mathbb{Q} \in \mathcal{Q}$ are:

    $$
    \begin{aligned}
    dS_t &= rS_t\,dt + \sqrt{v_t}S_t\,dW_t^{(1),\mathbb{Q}} \\
    dv_t &= \kappa^{\mathbb{Q}}(\theta^{\mathbb{Q}} - v_t)\,dt + \xi\sqrt{v_t}\,dW_t^{(2),\mathbb{Q}}
    \end{aligned}
    $$

    The no-arbitrage condition for $S$ determines the drift adjustment for $W^{(1)}$. The no-arbitrage condition for the variance swap determines the drift of $v_t$ under $\mathbb{Q}$, which fixes the market price of volatility risk $\lambda$. With both drifts determined, there are no remaining free parameters in the measure change, so $|\mathcal{Q}| = 1$.

    Formally, we now have 2 traded instruments and 2 risk factors. The volatility matrix (the matrix of diffusion coefficients relating the 2 asset returns to the 2 Brownian motions) is $2 \times 2$. If this matrix is invertible (which it is, since $S$ and $V^{\text{var}}$ have independent exposures to the two Brownian motions), the market price of risk vector $\theta = (\theta^{(1)}, \theta^{(2)})$ is uniquely determined. By the FTAP, uniqueness of $\mathbb{Q}$ implies completeness.

    **Summary**: Before adding the variance swap, $|\mathcal{Q}| = \infty$. After adding it, $|\mathcal{Q}| = 1$, and the market is complete.
