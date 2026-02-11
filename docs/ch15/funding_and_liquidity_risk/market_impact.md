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

## Almgren-Chriss Model

### Setup

Liquidate $X$ shares over time horizon $T$ with strategy $x(t)$:

$$
\int_0^T \dot{x}(t) \, dt = X, \quad x(0) = X, \quad x(T) = 0
$$

### Price Dynamics

$$
S_t = S_0 - g(v_t) - h(v_t) + \sigma W_t
$$

where:
- $v_t = -\dot{x}(t)$ is the trading rate
- $g(v)$ = permanent impact function
- $h(v)$ = temporary impact function
- $\sigma W_t$ = price volatility

### Linear Impact Model

Common specification:
$$
g(v) = \gamma v, \quad h(v) = \eta v
$$

where $\gamma$ is permanent impact coefficient and $\eta$ is temporary impact coefficient.

### Cost Functional

Total cost of execution:

$$
C[x(\cdot)] = \gamma X^2 + \int_0^T \eta v_t^2 \, dt + \text{Risk Cost}
$$

The first term is permanent impact (unavoidable), the second is temporary impact (depends on speed).

---

## Optimal Execution

### Mean-Variance Objective

Minimize expected cost plus risk penalty:

$$
\min_{x(\cdot)} \mathbb{E}[C] + \lambda \cdot \text{Var}[C]
$$

where $\lambda$ is risk aversion.

### Optimal Strategy (Linear Impact)

The optimal trading trajectory is:

$$
x(t) = X \cdot \frac{\sinh(\kappa(T-t))}{\sinh(\kappa T)}
$$

where $\kappa = \sqrt{\lambda \sigma^2 / \eta}$ depends on risk aversion and market parameters.

### Limiting Cases

**Risk-neutral ($\lambda = 0$):** Trade at constant rate (TWAP)
$$
x(t) = X \cdot \left(1 - \frac{t}{T}\right)
$$

**Highly risk-averse ($\lambda \to \infty$):** Trade immediately
$$
x(t) = 0 \text{ for } t > 0
$$

### Implementation Shortfall

Expected cost of the optimal strategy:

$$
\mathbb{E}[C^*] = \gamma X^2 + \eta X^2 \cdot \frac{\kappa}{\tanh(\kappa T)}
$$

Decomposed into permanent impact and temporary impact terms.

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

$$
\text{LVaR} = \text{VaR} + \text{Liquidation Cost}
$$

where liquidation cost depends on position size and impact model.

### Stressed Impact

During crises, impact increases:
- Wider spreads
- Lower depth
- Higher volatility
- Fewer counterparties

**Stress multiplier:** Impact may be 2-5× normal during severe stress.

---

## Hedging with Market Impact

### Impact-Adjusted Delta

Optimal hedge with impact costs:

$$
\Delta^* = \Delta^{\text{BS}} \cdot \frac{1}{1 + \text{Impact Cost Factor}}
$$

Under-hedge when impact is costly.

### Rebalancing Frequency

Trade-off between:
- Tracking error (favor frequent rebalancing)
- Impact costs (favor infrequent rebalancing)

**Optimal frequency** balances these costs.

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
