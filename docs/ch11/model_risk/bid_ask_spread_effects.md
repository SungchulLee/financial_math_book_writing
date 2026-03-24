# Bid-Ask Spread Effects

Bid-ask spreads represent the cost of immediate liquidity in financial markets. These microstructure features have profound impacts on hedging costs, execution strategies, and the practical feasibility of theoretical pricing models. Understanding spread effects is essential for realistic risk management.

## Key Concepts

**Spread Definition and Components**
The bid-ask spread $S = A - B$ (ask price minus bid price) includes:
- **Inventory cost**: compensation for holding positions
- **Information asymmetry**: protection against informed traders
- **Order processing costs**: labor, technology, clearing fees

For liquid assets, spreads scale with:
- Volatility: higher volatility increases spreads due to inventory risk
- Volume: higher volume reduces spreads through increased competition
- Time of day: spreads typically widen during low-volume periods

**Impact on Hedging Costs**
Delta hedging requires frequent rebalancing:
- Each rebalance incurs a round-trip cost of approximately $2S$ per unit
- Continuous rehedging would incur infinite cost; practical strategies use discrete rehedging
- Higher volatility increases rehedging frequency and costs
- Spread width directly reduces the effective hedge ratio

**Optimal Rehedging Frequency**
The cost of hedging includes:
- Spread costs: $\sum_{i} 2S_i |\Delta \gamma_i|$ for rehedging events
- Gamma loss between rehedges: $\frac{1}{2}\gamma (P/\sigma)^2$ for price moves of size P

Optimal intervals balance these competing costs, typically ranging from daily to weekly for standard products.

**Execution and Transaction Costs**
Multi-level spread effects:
1. **Effective spread**: actual cost in basis points
2. **Realized spread**: difference between execution price and next mid-quote
3. **Market impact**: temporary price movement due to order flow
4. **Permanent impact**: lasting price change from information revelation

**Practical Implications for Model Risk**
Spreads create a pricing band:
- Bid price ≈ Model price - $S/2$
- Ask price ≈ Model price + $S/2$
- Traders should be profitable when expected P&L > spread costs
- Models underestimate costs if ignoring spread impact

!!! caution "Model Limits"
    Perfect replication assumed in Black-Scholes assumes zero transaction costs. Under realistic spreads:
    - Perfect replication is impossible (hedging costs accumulate to significant levels)
    - Safe pricing requires markup that exceeds model price by a spread-dependent premium
    - Dynamic hedging becomes an optimal control problem, not a replication strategy

---

## Exercises

**Exercise 1.** A trader delta-hedges a short ATM call with $S = K = 100$, $\sigma = 0.20$, $\tau = 0.25$, and $\Gamma = 0.032$. The bid-ask spread is $\$0.10$ (so the half-spread is $\$0.05$ per share). If the trader rebalances daily and the expected daily delta change is $|\Delta\Gamma| \cdot \sigma S \sqrt{\Delta t} \cdot \sqrt{2/\pi}$ shares, compute the expected daily spread cost and the total spread cost over the option's life. Compare this to the option premium (approximately $\$4.50$).

---

**Exercise 2.** The optimal rehedging frequency balances spread costs ($\sim N \cdot S_{\text{spread}} \cdot |\delta\Delta|$) against gamma losses between rehedges ($\sim \frac{1}{2}\Gamma \sigma^2 S^2 \delta t$ per step). For $\Gamma = 0.04$, $\sigma = 0.25$, $S = 100$, and a bid-ask spread of $\$0.08$, estimate the optimal rebalancing interval by equating marginal spread cost to marginal gamma loss reduction. Express your answer in trading days.

---

**Exercise 3.** The effective spread, realized spread, and market impact decompose the total transaction cost. If a trader buys 500 shares at an execution price of $\$100.06$ when the mid-quote is $\$100.00$, the next mid-quote is $\$100.03$, and the permanent price impact is $\$100.02$, compute: (a) the effective half-spread; (b) the realized spread; (c) the temporary market impact; (d) the permanent impact. Which component dominates?

---

**Exercise 4.** Bid-ask spreads create a no-arbitrage band around the model price. If the Black-Scholes price of a call is $\$5.20$ and the spread on the option is $\$0.30$, what are the effective bid and ask prices? A trader believes the "true" value is $\$5.40$. Is there an opportunity to profit after accounting for the spread? What minimum mispricing (relative to the model) is needed to overcome the spread?

---

**Exercise 5.** Spreads typically widen during periods of high volatility. Suppose the half-spread is $\kappa = 0.001$ under normal conditions ($\sigma = 0.20$) and widens to $\kappa = 0.003$ during a volatility spike ($\sigma = 0.40$). For a delta-hedged short call with $\Gamma = 0.03$ and $S = 100$, compute the expected daily rehedging cost under both regimes. How does the cost-to-gamma-benefit ratio change between regimes?

---

**Exercise 6.** A market maker quotes a bid-ask spread of $\$0.20$ on an option worth $\$8.00$ (model price). The option has $\Gamma = 0.05$, $\Theta = -0.03$ per day, and the underlying spread is $\$0.05$. If the market maker delta-hedges and the expected daily move is consistent with $\sigma = 0.25$, compute: (a) the daily spread revenue from market making; (b) the daily hedging cost (spread on underlying times expected turnover); (c) the net daily P&L before gamma/theta effects. Is the spread sufficient to cover hedging costs?
