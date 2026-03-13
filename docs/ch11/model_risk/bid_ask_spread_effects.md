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
