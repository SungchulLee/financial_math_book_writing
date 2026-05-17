# Market Impact

**Market impact** refers to the price movement caused by executing trades. It is a key component of transaction costs and liquidity risk, particularly for large positions.

---

## Types of Market Impact

### Temporary Impact

Short-lived price pressure during execution:

- Prices move against the trade during execution
- Prices partially revert after execution completes
- Duration: minutes to hours

### Permanent Impact

Lasting price change due to information revelation:

- Market infers information from the trade
- Price adjusts to incorporate new information
- Persists indefinitely

### Total Impact

$$
\text{Total Impact} = \text{Temporary Impact} + \text{Permanent Impact}
$$

---

## The Square-Root Law

### Empirical Observation

Market impact scales approximately as the square root of trade size:

$$
\Delta P \approx \sigma \cdot \sqrt{\frac{Q}{V}}
$$

where:

- $\Delta P$ = price impact (as return)
- $\sigma$ = daily volatility
- $Q$ = order size (shares)
- $V$ = daily volume (shares)

### Interpretation

**Participation rate:** $Q/V$ measures trade size relative to market.

**Square-root scaling:** Doubling trade size increases impact by $\sqrt{2} \approx 1.41$, not 2×.

**Volatility scaling:** More volatile assets have larger impact.

### Refined Formula

Including a constant term:

$$
\Delta P = \eta \cdot \text{sign}(Q) + \gamma \cdot \sigma \cdot \sqrt{\frac{|Q|}{V}}
$$

where $\eta$ captures fixed costs (bid-ask spread) and $\gamma$ is a market-specific constant.

---

## Almgren-Chriss Model and Optimal Execution

Recall (see [§ Optimal Execution](optimal_execution.md)) for the full Almgren-Chriss setup, mean-variance objective, the optimal $\sinh$-trajectory $x^*(t) = X \sinh(\kappa(T-t))/\sinh(\kappa T)$ with urgency $\kappa = \sqrt{\lambda \sigma^2/\eta}$, TWAP and immediate-execution limits, and the optimal expected cost.

---

## Market Impact Models

### Linear Models

$$
\Delta P = \lambda \cdot Q
$$

Simple but unrealistic for large trades.

### Square-Root Models

$$
\Delta P = \lambda \cdot \text{sign}(Q) \cdot \sqrt{|Q|}
$$

Empirically supported; widely used.

### Power-Law Models

$$
\Delta P = \lambda \cdot \text{sign}(Q) \cdot |Q|^\delta
$$

where $\delta \approx 0.5$ empirically.

### Kyle Lambda

From Kyle (1985) model:

$$
\Delta P = \lambda \cdot Q
$$

where $\lambda$ is the market depth parameter, related to:

$$
\lambda = \frac{\sigma_v}{\sigma_u}
$$

(ratio of informed trading volatility to noise trading volatility).

---

## Determinants of Market Impact

### Trade Characteristics

| Factor | Effect on Impact |
|--------|-----------------|
| Order size | Larger → More impact |
| Execution speed | Faster → More impact |
| Order type | Market > Limit |
| Timing | Open/close → More impact |

### Market Characteristics

| Factor | Effect on Impact |
|--------|-----------------|
| Volatility | Higher → More impact |
| Volume | Higher → Less impact |
| Spread | Wider → More impact |
| Depth | Deeper → Less impact |

### Information Content

Trades perceived as informed have larger permanent impact.

---

## Measuring Market Impact

### Event Study Approach

Compare execution price to benchmark:

$$
\text{Impact} = P_{\text{exec}} - P_{\text{benchmark}}
$$

**Benchmarks:**

- Arrival price (decision time)
- VWAP (volume-weighted average)
- TWAP (time-weighted average)
- Close price

### Regression Approach

Estimate impact function from execution data:

$$
r_t = \alpha + \beta \cdot \text{OrderFlow}_t + \epsilon_t
$$

where $\beta$ estimates price sensitivity to order flow.

### Transaction Cost Analysis (TCA)

Comprehensive analysis decomposing costs:

- Market impact
- Timing cost
- Opportunity cost
- Commission/fees

---

## Risk Management Implications

### Liquidation Risk

Ignoring market impact **understates liquidation losses**:

$$
\text{True Liquidation Loss} = \text{Mark-to-Market Loss} + \text{Market Impact}
$$

### Liquidity-Adjusted VaR (LVaR)

Recall (see [§ Liquidity Premia](liquidity_premia.md)) for LVaR construction, holding-period extensions, and stress adjustments.

### Stressed Impact

During crises, impact increases:

- Wider spreads
- Lower depth
- Higher volatility
- Fewer counterparties

**Stress multiplier:** Impact may be 2-5× normal during severe stress.

---

## Hedging with Market Impact

Recall (see [§ Transaction Costs and Liquidity Effects](../../ch11/model_risk/transaction_costs_and_liquidity_effects.md)) for impact-adjusted delta, rebalancing-frequency trade-offs (tracking error vs. impact costs), and Whalley-Wilmott hedging bands.

---

## Practical Applications

### Algorithmic Trading

Execution algorithms designed to minimize impact:

- **TWAP:** Time-weighted average price
- **VWAP:** Volume-weighted average price
- **Implementation Shortfall:** Minimize expected cost
- **Adaptive:** Adjust to real-time conditions

### Pre-Trade Analysis

Before large trades:

1. Estimate expected impact
2. Choose execution horizon
3. Select algorithm
4. Set participation rate limits

### Post-Trade Analysis

After execution:

1. Compare to benchmark
2. Decompose costs
3. Assess algorithm performance
4. Refine future estimates

---

## Key Takeaways

- Market impact is the price movement caused by trading
- Impact has temporary and permanent components
- The square-root law: impact scales as $\sqrt{Q/V}$
- Almgren-Chriss provides optimal execution framework
- Optimal execution trades off impact cost against timing risk
- Market impact must be included in risk measures (LVaR)
- Impact increases during stress—liquidation risk is underestimated

---

## Further Reading

- Almgren, R. & Chriss, N. (2001), "Optimal Execution of Portfolio Transactions"
- Kyle, A. (1985), "Continuous Auctions and Insider Trading"
- Bouchaud, J.-P., Farmer, J.D., & Lillo, F. (2009), "How Markets Slowly Digest Changes in Supply and Demand"
- Gatheral, J. (2010), "No-Dynamic-Arbitrage and Market Impact"
- Cartea, Á., Jaimungal, S., & Penalva, J. (2015), *Algorithmic and High-Frequency Trading*

---

## Exercises

**Exercise 1.** A trader executes a market order to buy 100,000 shares of a stock with average daily volume of 1,000,000 shares and a bid-ask spread of \$0.05. Estimate the immediate (temporary) market impact using the "square-root law": $\Delta P \approx \sigma \cdot \sqrt{Q/V}$, where $\sigma$ is the daily volatility (2%), $Q = 100{,}000$, and $V = 1{,}000{,}000$.

??? success "Solution to Exercise 1"
    **Estimating temporary market impact using the square-root law.**

    The square-root law states:

    $$
    \Delta P \approx \sigma \cdot \sqrt{\frac{Q}{V}}
    $$

    Substituting the given values:

    - Daily volatility: $\sigma = 2\% = 0.02$
    - Order size: $Q = 100{,}000$ shares
    - Daily volume: $V = 1{,}000{,}000$ shares

    $$
    \Delta P \approx 0.02 \times \sqrt{\frac{100{,}000}{1{,}000{,}000}} = 0.02 \times \sqrt{0.1} = 0.02 \times 0.3162 \approx 0.00632
    $$

    This is a return of approximately 0.632%, or **63.2 basis points**.

    To express this in dollar terms, if the stock price is (say) \$50:

    $$
    \Delta P_{\$} \approx 0.00632 \times \$50 = \$0.316 \text{ per share}
    $$

    The total market impact cost for the full order is:

    $$
    \text{Total Impact Cost} = \Delta P_{\$} \times Q = \$0.316 \times 100{,}000 = \$31{,}600
    $$

    **Comparison with the bid-ask spread cost:**

    The half-spread cost (crossing the spread) is:

    $$
    \text{Spread Cost} = \frac{1}{2} \times \$0.05 \times 100{,}000 = \$2{,}500
    $$

    The market impact cost (\$31,600) is roughly **12.6 times** the half-spread cost (\$2,500), illustrating that for large orders, market impact dominates the bid-ask spread as a component of transaction costs.

    **Note:** The participation rate is $Q/V = 10\%$, which is considered significant. At this participation level, the square-root law estimate is reasonable but actual impact could vary depending on execution strategy, market conditions, and the information content of the order.

---

**Exercise 2.** Distinguish between temporary and permanent market impact. A trade of size $Q$ causes a temporary impact of $\eta\,Q$ (which decays) and a permanent impact of $\gamma\,Q$ (which persists). If $\eta = 0.001$ \$/share and $\gamma = 0.0003$ \$/share for a 50,000-share order, compute each component and the total execution cost.

??? success "Solution to Exercise 2"
    **Temporary versus permanent market impact.**

    **Definitions:**

    - **Temporary impact** ($\eta Q$): The price concession required to execute the trade. This reflects the cost of demanding immediacy from the market. It decays after execution as the order book replenishes and liquidity returns to normal.

    - **Permanent impact** ($\gamma Q$): The lasting shift in the equilibrium price caused by the trade. This reflects the market's inference that the trade contains information about the asset's fundamental value. It does not decay.

    **Computation for a 50,000-share order:**

    With $\eta = 0.001$ \$/share and $\gamma = 0.0003$ \$/share:

    **Temporary impact:**

    $$
    \text{Temporary Impact} = \eta \times Q = 0.001 \times 50{,}000 = \$50 \text{ per share (during execution)}
    $$

    **Permanent impact:**

    $$
    \text{Permanent Impact} = \gamma \times Q = 0.0003 \times 50{,}000 = \$15 \text{ per share (persists)}
    $$

    **Total execution cost:**

    The execution cost depends on how the impacts affect the average execution price. The permanent impact accumulates linearly as the order executes, so the average permanent impact paid is half the full amount. The temporary impact applies to each unit traded:

    $$
    \text{Permanent Impact Cost} = \frac{1}{2} \gamma Q^2 = \frac{1}{2} \times 0.0003 \times 50{,}000^2 = \frac{1}{2} \times 0.0003 \times 2.5 \times 10^9 = \$375{,}000
    $$

    $$
    \text{Temporary Impact Cost} = \eta Q^2 / T = 0.001 \times 50{,}000^2 / T
    $$

    For the temporary impact cost in the simplest (single-trade) case:

    $$
    \text{Temporary Impact Cost} = \eta \times Q \times Q = 0.001 \times 50{,}000 \times 50{,}000 = \$2{,}500{,}000
    $$

    However, if we interpret the linear model in per-share terms, the average cost per share is:

    - Temporary: \$50 per share $\times$ 50,000 shares = **\$2,500,000** (for immediate execution)
    - Permanent: \$15 per share $\times$ 50,000 shares $\times$ $\frac{1}{2}$ = **\$375,000** (average over the execution)

    **Total execution cost:**

    $$
    \text{Total Cost} = \$2{,}500{,}000 + \$375{,}000 = \$2{,}875{,}000
    $$

    The temporary impact dominates because $\eta \gg \gamma$. This is typical: temporary impact is the larger but controllable component (it can be reduced by slowing execution), while permanent impact is smaller but unavoidable (it does not depend on execution speed).

---

**Exercise 3.** Explain why market impact is nonlinear: doubling the trade size more than doubles the impact. The empirical square-root law states impact $\propto \sigma \sqrt{Q/V}$. Provide an intuitive explanation based on order book structure and adverse selection.

??? success "Solution to Exercise 3"
    **Why market impact is nonlinear (concave) in order size.**

    The empirical square-root law states:

    $$
    \Delta P \propto \sigma \sqrt{\frac{Q}{V}}
    $$

    Doubling the trade size from $Q$ to $2Q$ increases impact by a factor of $\sqrt{2} \approx 1.41$, not 2. This concavity is surprising at first glance but has deep microstructural explanations:

    **Explanation 1 -- Order book structure:**

    The limit order book has a characteristic shape: there are many limit orders near the best bid/ask (high density) and progressively fewer at more distant prices (lower density). For a small buy order, only the nearby ask-side liquidity is consumed, and the price moves little. For a larger order, the trader must "walk up the book," consuming increasingly sparse liquidity at progressively worse prices.

    However, the order book is not static. As the trader's order walks through the book, new limit orders are submitted by other participants who observe the activity. This **replenishment** effect means that the effective depth encountered by a large order is greater than the instantaneous snapshot of the book would suggest. The replenishment rate scales with time and participation, leading to a sub-linear relationship between order size and impact.

    **Explanation 2 -- Adverse selection and information:**

    In the Kyle (1985) framework, market makers adjust prices based on their inference about the trader's information. A key insight is that informed traders **optimally split their orders** over time to minimize their impact. As a result, the information revealed by an order of size $Q$ is not proportional to $Q$ -- a large order from a single trader may reflect the same information as a smaller one.

    The market maker's optimal pricing rule leads to impact that scales as:

    $$
    \Delta P \propto \sqrt{\text{variance of informed trading}}
    $$

    Since the informed trader submits orders proportional to their signal (which has finite variance), the aggregate impact inherits a square-root scaling.

    **Explanation 3 -- Dimensional analysis and universality:**

    Consider the natural scales of the problem. The only dimensionless ratio involving order size is $Q/V$ (participation rate). The impact must scale with $\sigma$ (volatility, the natural price scale). The simplest functional form consistent with concavity is:

    $$
    \Delta P = \sigma \cdot f\left(\frac{Q}{V}\right)
    $$

    Empirically, $f(x) \sim \sqrt{x}$ is remarkably universal across markets, asset classes, and time periods (Bouchaud et al., 2009). This universality suggests that the square-root law arises from fundamental properties of how markets aggregate information and supply liquidity, rather than from the specific institutional details of any particular market.

    **Implication for execution:** The concavity of impact is good news for large traders: splitting an order reduces total impact. If impact were linear, splitting would not help (total impact would be the same). The square-root law implies that patient, gradual execution achieves meaningfully lower costs than aggressive execution.

---

**Exercise 4.** A fund manager needs to liquidate a \$500M equity position. The stock has average daily volume of \$50M and daily volatility of 1.5%. Estimate the market impact cost if the position is liquidated over (a) 1 day, (b) 5 days, and (c) 10 days. Discuss the trade-off between impact cost and timing risk.

??? success "Solution to Exercise 4"
    **Estimating market impact for different liquidation horizons.**

    **Given parameters:**

    - Position value: \$500M
    - Average daily volume (ADV): \$50M per day
    - Daily volatility: $\sigma = 1.5\%$
    - Position as a fraction of daily volume: $Q/V_{\text{day}} = 500/50 = 10$ days of volume

    Using the square-root impact law for a multi-day execution of $T_{\text{liq}}$ days, the participation rate per day is $Q/(V \cdot T_{\text{liq}})$, and the impact per day's trading is approximately:

    $$
    \Delta P \approx \sigma \cdot \sqrt{\frac{Q/T_{\text{liq}}}{V}} = \sigma \cdot \sqrt{\frac{Q}{V \cdot T_{\text{liq}}}}
    $$

    The total impact cost (in dollar terms) is the impact per share times total shares sold. Using the aggregated square-root law for the full meta-order:

    $$
    \text{Impact Cost} \approx \sigma \cdot \sqrt{\frac{Q}{V \cdot T_{\text{liq}}}} \times \text{Position Value}
    $$

    where $Q/(V \cdot T_{\text{liq}})$ is the daily participation rate.

    **(a) Liquidation over 1 day ($T_{\text{liq}} = 1$):**

    Daily participation rate: $500/50 = 10$ (i.e., 1000% of daily volume -- effectively impossible in a single day, but computing for illustration):

    $$
    \text{Impact} \approx 0.015 \times \sqrt{10} \approx 0.015 \times 3.162 = 4.74\%
    $$

    $$
    \text{Impact Cost} \approx 4.74\% \times \$500\text{M} = \$23.7\text{M}
    $$

    This is enormous and practically infeasible. A single-day liquidation would destroy roughly \$24M in value.

    **(b) Liquidation over 5 days ($T_{\text{liq}} = 5$):**

    Daily participation rate: $500/(50 \times 5) = 2$ (200% per day -- still very aggressive):

    $$
    \text{Impact} \approx 0.015 \times \sqrt{2} \approx 0.015 \times 1.414 = 2.12\%
    $$

    $$
    \text{Impact Cost} \approx 2.12\% \times \$500\text{M} = \$10.6\text{M}
    $$

    **(c) Liquidation over 10 days ($T_{\text{liq}} = 10$):**

    Daily participation rate: $500/(50 \times 10) = 1$ (100% per day -- still significant):

    $$
    \text{Impact} \approx 0.015 \times \sqrt{1} = 1.5\%
    $$

    $$
    \text{Impact Cost} \approx 1.5\% \times \$500\text{M} = \$7.5\text{M}
    $$

    **Summary table:**

    | Liquidation Period | Daily Participation | Impact (%) | Impact Cost |
    |---|---|---|---|
    | 1 day | 1000% | 4.74% | \$23.7M |
    | 5 days | 200% | 2.12% | \$10.6M |
    | 10 days | 100% | 1.50% | \$7.5M |

    **Trade-off between impact cost and timing risk:**

    Slower execution reduces impact cost (as shown above) but increases **timing risk**: the risk that the stock price moves adversely during the liquidation period. The timing risk over $T_{\text{liq}}$ days is:

    $$
    \text{Timing Risk} = \sigma_{\text{daily}} \times \sqrt{T_{\text{liq}}} \times \text{Average Position}
    $$

    For $T_{\text{liq}} = 10$ days with average position $\approx \$250\text{M}$ (half the starting position):

    $$
    \text{Timing Risk (1 std dev)} \approx 0.015 \times \sqrt{10} \times \$250\text{M} \approx \$11.9\text{M}
    $$

    The fund manager must balance: faster execution minimizes timing risk but maximizes impact cost, while slower execution minimizes impact cost but exposes the position to adverse market movements. The Almgren-Chriss framework provides the optimal balance through the urgency parameter $\kappa$.

---

**Exercise 5.** In the Almgren-Chriss framework, market impact has a permanent component $g(v) = \gamma\,v$ and a temporary component $h(v) = \eta\,v + \epsilon\,\text{sgn}(v)$, where $v$ is the trading rate. Explain the economic interpretation of each parameter. Why is the bid-ask spread captured by $\epsilon$?

??? success "Solution to Exercise 5"
    **Economic interpretation of Almgren-Chriss impact parameters.**

    In the Almgren-Chriss model, the price dynamics during execution are:

    $$
    S_t^{\text{exec}} = S_0 + \gamma \int_0^t v(s)\,ds - \eta\,v(t) - \epsilon\,\text{sgn}(v(t)) + \sigma W_t
    $$

    where $v(t) = -\dot{x}(t)$ is the trading rate.

    **Parameter $\gamma$ (permanent impact coefficient):**

    - **Units:** \$/share per (share/time)
    - **Interpretation:** Each unit traded permanently shifts the equilibrium price by $\gamma$ dollars. This reflects the **information content** of the trade. The market infers that a seller may have negative private information and permanently adjusts the price downward.
    - **Key property:** The permanent impact $\gamma \int_0^t v(s)\,ds = \gamma(X - x(t))$ depends only on the cumulative quantity traded, not on the speed of execution. It is therefore unavoidable -- no matter how cleverly the trader executes, the total permanent impact is $\gamma X$.

    **Parameter $\eta$ (temporary impact coefficient):**

    - **Units:** \$/share per (share/time)
    - **Interpretation:** Trading at rate $v$ causes an additional temporary price concession of $\eta v$ per share. This reflects the **liquidity cost of demanding immediacy**: trading faster requires walking further up the order book, paying higher prices. Temporary impact decays immediately -- it only affects the instantaneous execution price.
    - **Key property:** Temporary impact depends on trading speed, not cumulative quantity. It can be reduced by slowing down execution. The total temporary impact cost is $\eta \int_0^T v(t)^2\,dt$, which is minimized by trading at a constant rate (TWAP).

    **Parameter $\epsilon$ (fixed transaction cost / half-spread):**

    - **Units:** \$/share
    - **Interpretation:** This is the **half bid-ask spread** -- the minimum cost of executing any trade, regardless of size or speed. It captures the fixed per-share cost of crossing the spread.
    - **Why the bid-ask spread is captured by $\epsilon$:** When a trader submits a market buy order, they pay the ask price; when selling, they receive the bid price. The cost per share is the half-spread:

        $$
        \text{Cost per share} = \frac{P^{\text{ask}} - P^{\text{bid}}}{2} = \epsilon
        $$

        The $\text{sgn}(v)$ term ensures this cost is always incurred in the adverse direction: buyers pay above mid-price, sellers receive below mid-price. The total spread cost is $\epsilon \cdot X$ (independent of execution strategy), making it an unavoidable fixed cost like permanent impact.

    **Complete cost decomposition:**

    $$
    \text{Total Cost} = \underbrace{\epsilon X}_{\text{spread}} + \underbrace{\frac{1}{2}\gamma X^2}_{\text{permanent impact}} + \underbrace{\eta \int_0^T v(t)^2\,dt}_{\text{temporary impact}} + \underbrace{\sigma \int_0^T x(t)\,dW_t}_{\text{timing risk}}
    $$

    Only the temporary impact term is controllable through the execution strategy. The spread and permanent impact are fixed costs, and timing risk is a zero-mean random variable.

---

**Exercise 6.** How does market impact affect derivative hedging? A delta-hedging strategy requires frequent rebalancing. If each rebalance incurs market impact costs, describe how the total hedging cost depends on rebalancing frequency. What is the optimal trade-off between hedging accuracy and transaction costs?

??? success "Solution to Exercise 6"
    **Market impact and derivative hedging.**

    **Setup: Delta hedging with market impact.**

    A delta-hedging strategy for an option position requires rebalancing the hedge portfolio to maintain $\Delta_t$ shares of the underlying at each time step. If the option's delta changes by $\Delta_{t+1} - \Delta_t$ between rebalancing times, the hedger must trade:

    $$
    Q_{\text{rebalance}} = \Delta_{t+1} - \Delta_t \approx \Gamma \cdot \delta S
    $$

    where $\Gamma$ is the option's gamma and $\delta S$ is the price change. Each rebalance incurs market impact costs.

    **Total hedging cost as a function of rebalancing frequency:**

    Suppose the hedger rebalances every $\delta t$ time units, for a total of $N = T/\delta t$ rebalancing events.

    **Impact cost per rebalance:** Each rebalance trades $|Q_k| \approx |\Gamma| \cdot |\delta S_k|$ shares. Using the square-root impact model:

    $$
    \text{Impact per rebalance} \approx c \cdot \sigma \sqrt{\frac{|\Gamma \cdot \delta S_k|}{V \cdot \delta t}}
    $$

    The expected total impact cost over $N$ rebalances scales as:

    $$
    \text{Total Impact Cost} \propto N \times \mathbb{E}[\text{impact per rebalance}]
    $$

    Since $|\delta S_k| \approx \sigma \sqrt{\delta t}$ and $N = T/\delta t$:

    $$
    \text{Total Impact Cost} \propto \frac{T}{\delta t} \times f(\Gamma \sigma \sqrt{\delta t})
    $$

    For a linear impact model ($f(x) = \eta x$):

    $$
    \text{Total Impact Cost} \propto \eta \Gamma^2 \sigma^2 \times \frac{T}{\delta t} \times \delta t = \eta \Gamma^2 \sigma^2 T
    $$

    This is independent of $\delta t$! However, for the more realistic square-root model:

    $$
    \text{Total Impact Cost} \propto \frac{T}{\delta t} \times \sqrt{\delta t} = T \times (\delta t)^{-1/2}
    $$

    which **increases** as $\delta t \to 0$ (more frequent rebalancing).

    **Hedging error (tracking error):**

    The discrete hedging error arises from gamma exposure between rebalancing times:

    $$
    \text{Hedging Error} \approx \frac{1}{2} \Gamma (\delta S)^2 - \Theta \cdot \delta t
    $$

    The variance of the total hedging error over $T$ scales as:

    $$
    \text{Var}[\text{Total Hedging Error}] \propto \Gamma^2 \sigma^4 \cdot \delta t \cdot T
    $$

    This **decreases** as $\delta t \to 0$ (more frequent rebalancing reduces tracking error).

    **Optimal trade-off:**

    The total cost of hedging combines impact costs and hedging error risk:

    $$
    \text{Total Cost} = \underbrace{A \cdot (\delta t)^{-1/2}}_{\text{impact cost}} + \underbrace{\lambda \cdot B \cdot \delta t}_{\text{risk penalty from hedging error}}
    $$

    where $A$ and $B$ are constants depending on $\Gamma$, $\sigma$, $T$, and market parameters, and $\lambda$ is risk aversion.

    Minimizing with respect to $\delta t$:

    $$
    \frac{d}{d(\delta t)}\left[A(\delta t)^{-1/2} + \lambda B \cdot \delta t\right] = -\frac{A}{2}(\delta t)^{-3/2} + \lambda B = 0
    $$

    $$
    \delta t^* = \left(\frac{A}{2\lambda B}\right)^{2/3}
    $$

    **Key insights:**

    - The optimal rebalancing frequency is **finite** -- neither continuous nor zero.
    - Higher market impact costs (larger $A$) favor **less frequent** rebalancing.
    - Higher risk aversion or larger gamma (larger $\lambda B$) favor **more frequent** rebalancing.
    - Higher volatility increases both the impact cost per rebalance (more shares to trade) and the hedging error (larger price moves), making the trade-off sharper.
    - In practice, hedgers also use "hedging bands" (rebalance only when delta deviates by more than a threshold), which further reduces unnecessary trades while controlling tracking error. The Whalley-Wilmott (1997) asymptotic result gives the optimal bandwidth as proportional to $(\text{transaction cost})^{1/3}$.
