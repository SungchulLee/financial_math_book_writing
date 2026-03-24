# Incompleteness of Equity Markets

The Black–Scholes model assumes a **complete market**, where all risks can be perfectly hedged using traded instruments. Empirically and structurally, equity markets are incomplete, which fundamentally limits the model's applicability and introduces risk premia for unhedgeable factors.

---

## Market Completeness in Black–Scholes

In the Black–Scholes framework, a market is **complete** if every contingent claim can be replicated by a self-financing trading strategy in the underlying assets.

**Formal definition:** A market is complete if the replicating portfolio $\Pi_t$ satisfies:

$$
\Pi_T = \Phi(S_T) \quad \text{a.s.}
$$

for any payoff $\Phi$, where $\Pi_t$ is constructed from holdings in $S_t$ and the risk-free bond.

**Black–Scholes completeness requires:**

1. **Single source of randomness:** One Brownian motion drives $S_t$
2. **Continuous trading:** Portfolio can be rebalanced continuously
3. **No frictions:** No transaction costs, no constraints
4. **Constant parameters:** $\sigma$, $r$, $q$ are known constants

Under these conditions, the delta-hedging strategy:

$$
\Delta_t = \frac{\partial C}{\partial S}(t, S_t)
$$

replicates any European payoff exactly.

---

## Sources of Incompleteness

Real markets violate the completeness conditions in multiple ways:

### 1. Stochastic Volatility

When volatility is random:

$$
\begin{aligned}
dS_t &= \mu S_t\,dt + \sqrt{V_t} S_t\,dW_t^S \\
dV_t &= a(V_t)\,dt + b(V_t)\,dW_t^V
\end{aligned}
$$

there are **two sources of randomness** ($W^S$, $W^V$) but only **one traded asset** ($S$). The volatility shock $dW_t^V$ cannot be hedged by trading $S$ alone.

**Dimension count:**
- Risk factors: 2 (price, volatility)
- Traded instruments: 1 (underlying) + 1 (bond) = 2
- But bond provides no volatility exposure → effective instruments for volatility: 0

### 2. Jumps and Discontinuities

If prices can jump:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t + S_{t^-}(e^{J_t} - 1)\,dN_t
$$

where $N_t$ is a Poisson process, then:
- Jump timing is unpredictable
- Jump size may be random
- Continuous hedging cannot eliminate jump risk

Even with deterministic jump sizes, the number of jump states can exceed the number of traded instruments.

### 3. Discrete Trading

In practice, portfolios are rebalanced at discrete times $t_0 < t_1 < \cdots < t_n$. Between rebalancing:

$$
d\Pi_t = \Delta_{t_i}\,dS_t + (r\,dt)\times\text{(cash)}
$$

but $\Delta_{t_i}$ is stale. The **hedging error** accumulates:

$$
\text{Hedging error} = \int_0^T (\Delta_t^{\text{true}} - \Delta_t^{\text{used}})\,dS_t \neq 0
$$

### 4. Transaction Costs

With proportional transaction costs $\epsilon$, frequent rebalancing incurs costs:

$$
\text{Cost} = \epsilon \sum_{i} |S_{t_i}||\Delta_{t_i} - \Delta_{t_{i-1}}|
$$

The trade-off between hedging error and transaction costs introduces irreducible uncertainty.

### 5. Trading Constraints

- Short-selling restrictions
- Position limits
- Margin requirements
- Liquidity constraints

Each constraint reduces the set of feasible hedging strategies.

---

## Consequences for Pricing

In incomplete markets, the fundamental theorem of asset pricing takes a different form:

### Non-Uniqueness of Prices

**Complete market:** Unique no-arbitrage price = replication cost

**Incomplete market:** A range of no-arbitrage prices exists:

$$
\underline{C} \leq C \leq \overline{C}
$$

where:
- $\underline{C}$ = subhedging price (price of cheapest super-replicating portfolio)
- $\overline{C}$ = superhedging price

Any price in $[\underline{C}, \overline{C}]$ is consistent with no-arbitrage.

### Multiple Equivalent Martingale Measures

By the Second Fundamental Theorem of Asset Pricing:

$$
\text{Market complete} \iff \text{Unique EMM } \mathbb{Q}
$$

In incomplete markets, there exists a **family** of equivalent martingale measures $\{\mathbb{Q}_\lambda\}$. Each measure gives a different price:

$$
C_\lambda = e^{-rT}\mathbb{E}^{\mathbb{Q}_\lambda}[\Phi(S_T)]
$$

The selection of $\mathbb{Q}$ requires additional criteria (utility, equilibrium, market price of risk).

### Risk Preferences Matter

In complete markets, prices are preference-free (determined by replication). In incomplete markets:

- Risk-averse agents demand compensation for bearing unhedgeable risk
- Supply and demand equilibrium determines prices
- Different investors may have different valuations

---

## Volatility as a Non-Traded Risk

Volatility occupies a special role in incomplete markets:

### Volatility Cannot Be Directly Traded

While volatility derivatives exist (variance swaps, VIX options), in many markets:
- Volatility is not a directly tradeable asset
- Delta hedging eliminates only price risk, not volatility risk
- Vega exposure remains after delta hedging

### Market Price of Volatility Risk

The change from physical to risk-neutral measure involves a **market price of volatility risk** $\lambda_V$:

$$
dW_t^{V,\mathbb{Q}} = dW_t^{V,\mathbb{P}} - \lambda_V(t, S_t, V_t)\,dt
$$

Under $\mathbb{P}$: volatility dynamics reflect actual evolution
Under $\mathbb{Q}$: volatility dynamics are risk-adjusted for pricing

The difference $\lambda_V$ is not uniquely determined by no-arbitrage—it reflects market equilibrium and risk preferences.

### Volatility Risk Premium

Empirically, volatility risk carries a **negative premium**: sellers of volatility (e.g., variance swap receivers) earn positive expected returns.

$$
\mathbb{E}^{\mathbb{P}}[\text{RV}^2] < \mathbb{E}^{\mathbb{Q}}[\text{RV}^2] = \text{Variance swap rate}
$$

This premium compensates for:
- Jump risk
- Volatility-of-volatility risk
- Correlation with market downturns (volatility spikes when markets crash)

---

## Quantifying Incompleteness

### Variance Optimal Hedge

The mean-variance optimal hedge minimizes:

$$
\min_{\Delta} \mathbb{E}\left[(H - V_T^{\Delta})^2\right]
$$

where $H$ is the claim payoff and $V_T^{\Delta}$ the hedged portfolio value.

The **residual variance** measures incompleteness:

$$
\text{Residual var} = \min_{\Delta} \text{Var}[H - V_T^{\Delta}] > 0
$$

### Minimal Entropy Martingale Measure

Among all EMMs, the **minimal entropy** measure $\mathbb{Q}^*$ minimizes:

$$
\mathbb{Q}^* = \arg\min_{\mathbb{Q}} H(\mathbb{Q} | \mathbb{P}) = \arg\min_{\mathbb{Q}} \mathbb{E}^{\mathbb{Q}}\left[\log\frac{d\mathbb{Q}}{d\mathbb{P}}\right]
$$

This provides a principled way to select among EMMs.

### Utility Indifference Pricing

An agent with utility $U$ values a claim at the **indifference price** $p$:

$$
\sup_{\pi} \mathbb{E}[U(X_T^{\pi})] = \sup_{\pi} \mathbb{E}[U(X_T^{\pi} + H - p)]
$$

where $\pi$ ranges over admissible trading strategies.

---

## Practical Implications

### Hedging in Incomplete Markets

Since perfect replication is impossible:

1. **Partial hedging:** Reduce but don't eliminate risk
2. **Variance swaps:** Trade volatility risk directly when available
3. **Options on options:** Use the smile to hedge smile risk
4. **Robust hedging:** Minimize worst-case loss across models

### Model Selection

Different models imply different:
- Risk-neutral dynamics
- Volatility risk premia
- Hedging strategies
- Price ranges

Model selection is a form of specifying risk preferences.

### P&L Attribution

In incomplete markets, hedging P&L decomposes as:

$$
\text{P\&L} = \underbrace{\text{Gamma P\&L}}_{\text{hedgeable}} + \underbrace{\text{Vega P\&L}}_{\text{partially hedgeable}} + \underbrace{\text{Volga/Vanna P\&L}}_{\text{higher-order}} + \underbrace{\text{Unexplained}}_{\text{model error}}
$$

---

## Key Takeaways

- Equity markets are incomplete: not all risks can be hedged
- Sources include stochastic volatility, jumps, discrete trading, and frictions
- Incompleteness implies non-unique prices and multiple EMMs
- Volatility risk is the primary unhedgeable factor in equity markets
- Risk premia emerge naturally for bearing unhedgeable risks
- Model selection and measure choice reflect risk preferences

---

## Further Reading

- Harrison, J.M. & Kreps, D. (1979). *Martingales and arbitrage in multiperiod securities markets*. Journal of Economic Theory.
- Harrison, J.M. & Pliska, S. (1981). *Martingales and stochastic integrals in the theory of continuous trading*. Stochastic Processes and Applications.
- Duffie, D. (2001). *Dynamic Asset Pricing Theory*, 3rd ed. Princeton University Press.
- Föllmer, H. & Schied, A. (2016). *Stochastic Finance: An Introduction in Discrete Time*, 4th ed. De Gruyter.
- Cont, R. (2006). *Model uncertainty and its impact on the pricing of derivative instruments*. Mathematical Finance.

---

## Exercises

**Exercise 1.** Consider a market with two sources of randomness ($W^S$, $W^V$) but only one risky asset $S$ and a risk-free bond. Using a dimension-counting argument, explain why this market is incomplete. How many additional traded instruments would be needed to restore completeness?

---

**Exercise 2.** In a stochastic volatility model, two equivalent martingale measures $\mathbb{Q}_1$ and $\mathbb{Q}_2$ give call option prices $C_1 = 5.20$ and $C_2 = 5.80$ for the same strike and maturity. What can you conclude about the no-arbitrage bounds $[\underline{C}, \overline{C}]$? Explain why, unlike in the Black–Scholes model, additional economic assumptions are needed to select a unique price.

---

**Exercise 3.** The market price of volatility risk $\lambda_V$ transforms the volatility Brownian motion from $\mathbb{P}$ to $\mathbb{Q}$ via

$$
dW_t^{V,\mathbb{Q}} = dW_t^{V,\mathbb{P}} - \lambda_V\,dt
$$

If the physical-measure volatility dynamics are $dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V$, write the risk-neutral dynamics under $\mathbb{Q}$ explicitly. Identify the risk-neutral mean-reversion speed and long-run variance level in terms of $\kappa$, $\theta$, $\xi$, and $\lambda_V$ (assuming $\lambda_V$ is constant).

---

**Exercise 4.** The variance risk premium is defined as $VRP = \mathbb{E}^{\mathbb{Q}}[\sigma^2] - \mathbb{E}^{\mathbb{P}}[\sigma^2]$. Suppose the variance swap rate (risk-neutral expected variance) for a 1-month horizon is $(18\%)^2$ and the expected realized variance under $\mathbb{P}$ is $(15\%)^2$. Compute the VRP in variance terms and explain why a negative risk premium for variance sellers (positive $VRP$) is economically consistent with the leverage effect.

---

**Exercise 5.** A trader holds a delta-hedged short call position. Decompose the hedging P&L into gamma, vega, and higher-order components:

$$
\text{P\&L} = \text{Gamma P\&L} + \text{Vega P\&L} + \text{Volga/Vanna P\&L} + \text{Unexplained}
$$

Explain which components are hedgeable using only the underlying stock, and which require additional instruments such as options. Why does market incompleteness make it impossible to eliminate all components simultaneously?

---

**Exercise 6.** In utility indifference pricing, an agent with exponential utility $U(x) = -e^{-\gamma x}$ values a claim at the price $p$ satisfying

$$
\sup_{\pi} \mathbb{E}[U(X_T^{\pi})] = \sup_{\pi} \mathbb{E}[U(X_T^{\pi} + H - p)]
$$

Explain intuitively why this price depends on the risk aversion parameter $\gamma$. What happens to the indifference price as $\gamma \to 0$ (risk-neutral agent)? As $\gamma \to \infty$ (infinitely risk-averse agent)?

---

**Exercise 7.** Consider a jump-diffusion model where the stock follows

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t + S_{t^-}(e^J - 1)\,dN_t
$$

with $N_t$ a Poisson process with intensity $\lambda = 2$ per year and $J \sim \mathcal{N}(-0.05, 0.1^2)$. Even if $\sigma$ is constant, explain why the market is still incomplete. What additional instrument(s) could partially complete the market?
