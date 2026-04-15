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

!!! warning "Model Limits"
    Perfect replication assumed in Black-Scholes assumes zero transaction costs. Under realistic spreads:
    - Perfect replication is impossible (hedging costs accumulate to significant levels)
    - Safe pricing requires markup that exceeds model price by a spread-dependent premium
    - Dynamic hedging becomes an optimal control problem, not a replication strategy

---

## Exercises

**Exercise 1.** A trader delta-hedges a short ATM call with $S = K = 100$, $\sigma = 0.20$, $\tau = 0.25$, and $\Gamma = 0.032$. The bid-ask spread is $\$0.10$ (so the half-spread is $\$0.05$ per share). If the trader rebalances daily and the expected daily delta change is $|\Delta\Gamma| \cdot \sigma S \sqrt{\Delta t} \cdot \sqrt{2/\pi}$ shares, compute the expected daily spread cost and the total spread cost over the option's life. Compare this to the option premium (approximately $\$4.50$).

??? success "Solution to Exercise 1"
    First, compute the expected daily delta change. The expected absolute delta change per day is

    $$
    |\Delta\Gamma| = \Gamma \cdot \sigma S \sqrt{\Delta t} \cdot \sqrt{2/\pi}
    $$

    With $\Gamma = 0.032$, $\sigma = 0.20$, $S = 100$, $\Delta t = 1/252$:

    $$
    \sigma S \sqrt{\Delta t} = 0.20 \times 100 \times \sqrt{1/252} = 20 \times 0.0630 = 1.260
    $$

    $$
    |\Delta\Gamma| = 0.032 \times 1.260 \times \sqrt{2/\pi} = 0.032 \times 1.260 \times 0.7979 = 0.03218 \text{ shares}
    $$

    The expected daily spread cost is the half-spread times the number of shares traded:

    $$
    \text{Daily cost} = 2 \times \$0.05 \times 0.03218 \times 100 = \$0.322
    $$

    Here we multiply by 100 because the option controls 100 shares (one contract). Actually, let us reconsider: the expected delta change of $0.03218$ means we must trade $0.03218 \times 100 = 3.218$ shares per contract. Each share incurs a round-trip cost of $\$0.10$ (the full spread):

    $$
    \text{Daily cost} = 3.218 \times \$0.10 = \$0.322
    $$

    The option has $\tau = 0.25$ years $= 63$ trading days. Total spread cost over the life:

    $$
    \text{Total cost} = 63 \times \$0.322 = \$20.27
    $$

    The option premium is approximately $\$4.50$ per share, or $\$450$ per contract. The spread cost of $\$20.27$ is about $4.5\%$ of the premium. This is a significant drag on the hedge, though still a fraction of the premium collected.

---

**Exercise 2.** The optimal rehedging frequency balances spread costs ($\sim N \cdot S_{\text{spread}} \cdot |\delta\Delta|$) against gamma losses between rehedges ($\sim \frac{1}{2}\Gamma \sigma^2 S^2 \delta t$ per step). For $\Gamma = 0.04$, $\sigma = 0.25$, $S = 100$, and a bid-ask spread of $\$0.08$, estimate the optimal rebalancing interval by equating marginal spread cost to marginal gamma loss reduction. Express your answer in trading days.

??? success "Solution to Exercise 2"
    The marginal spread cost per rebalancing event is approximately $S_{\text{spread}} \cdot |\delta\Delta|$, where $|\delta\Delta| \approx \Gamma \sigma S \sqrt{\delta t} \sqrt{2/\pi}$. Over a time step $\delta t$, the spread cost is

    $$
    C_{\text{spread}} = S_{\text{spread}} \cdot \Gamma \sigma S \sqrt{\delta t} \cdot \sqrt{2/\pi}
    $$

    The gamma loss (variance of hedging error) per step from not hedging continuously is

    $$
    C_{\text{gamma}} = \frac{1}{2}\Gamma \sigma^2 S^2 \delta t
    $$

    Equating marginal costs:

    $$
    S_{\text{spread}} \cdot \Gamma \sigma S \sqrt{\delta t} \cdot \sqrt{2/\pi} = \frac{1}{2}\Gamma \sigma^2 S^2 \delta t
    $$

    Dividing both sides by $\Gamma \sigma S \sqrt{\delta t}$:

    $$
    S_{\text{spread}} \cdot \sqrt{2/\pi} = \frac{1}{2}\sigma S \sqrt{\delta t}
    $$

    Solving for $\delta t$:

    $$
    \sqrt{\delta t} = \frac{2 S_{\text{spread}} \sqrt{2/\pi}}{\sigma S}
    $$

    $$
    \delta t = \frac{4 S_{\text{spread}}^2 \cdot (2/\pi)}{\sigma^2 S^2} = \frac{8 S_{\text{spread}}^2}{\pi \sigma^2 S^2}
    $$

    Substituting $S_{\text{spread}} = \$0.08$, $\sigma = 0.25$, $S = 100$:

    $$
    \delta t = \frac{8 \times (0.08)^2}{\pi \times (0.25)^2 \times (100)^2} = \frac{8 \times 0.0064}{\pi \times 0.0625 \times 10000} = \frac{0.0512}{1963.5} = 2.608 \times 10^{-5} \text{ years}
    $$

    Converting to trading days ($\times 252$):

    $$
    \delta t = 2.608 \times 10^{-5} \times 252 \approx 0.0066 \text{ trading days}
    $$

    This suggests rebalancing roughly every $0.007$ days, or about every few minutes. In practice, this means the marginal analysis indicates very frequent rebalancing for these parameters. The result is driven by the relatively small spread relative to the gamma exposure. For larger spreads, the optimal interval increases: with $S_{\text{spread}} = \$0.50$, the interval would be $\sim 0.25$ days.

---

**Exercise 3.** The effective spread, realized spread, and market impact decompose the total transaction cost. If a trader buys 500 shares at an execution price of $\$100.06$ when the mid-quote is $\$100.00$, the next mid-quote is $\$100.03$, and the permanent price impact is $\$100.02$, compute: (a) the effective half-spread; (b) the realized spread; (c) the temporary market impact; (d) the permanent impact. Which component dominates?

??? success "Solution to Exercise 3"
    Given: execution price $= \$100.06$, mid-quote at execution $= \$100.00$, next mid-quote $= \$100.03$, permanent impact $= \$100.02$.

    **(a) Effective half-spread:**

    $$
    \text{Effective half-spread} = \text{Execution price} - \text{Mid-quote} = \$100.06 - \$100.00 = \$0.06
    $$

    **(b) Realized spread:** The realized spread measures the market maker's revenue after the price moves:

    $$
    \text{Realized spread} = \text{Execution price} - \text{Next mid-quote} = \$100.06 - \$100.03 = \$0.03
    $$

    **(c) Temporary market impact:** The temporary impact is the portion of the price move that reverts:

    $$
    \text{Temporary impact} = \text{Next mid-quote} - \text{Permanent price} = \$100.03 - \$100.02 = \$0.01
    $$

    **(d) Permanent impact:**

    $$
    \text{Permanent impact} = \text{Permanent price} - \text{Original mid-quote} = \$100.02 - \$100.00 = \$0.02
    $$

    **Verification:** The effective half-spread decomposes as: realized spread ($\$0.03$) = temporary impact ($\$0.01$) + permanent impact ($\$0.02$). And total cost to the trader = effective half-spread ($\$0.06$) per share, which equals realized spread ($\$0.03$) + next mid movement ($\$0.03$). The dominant component is the effective half-spread of $\$0.06$, with the realized spread ($\$0.03$) being the largest single decomposition component. The permanent impact ($\$0.02$) represents information content of the trade.

---

**Exercise 4.** Bid-ask spreads create a no-arbitrage band around the model price. If the Black-Scholes price of a call is $\$5.20$ and the spread on the option is $\$0.30$, what are the effective bid and ask prices? A trader believes the "true" value is $\$5.40$. Is there an opportunity to profit after accounting for the spread? What minimum mispricing (relative to the model) is needed to overcome the spread?

??? success "Solution to Exercise 4"
    The Black-Scholes price is $\$5.20$ and the option spread is $\$0.30$. The effective bid and ask prices are:

    $$
    \text{Bid} = \$5.20 - \$0.30/2 = \$5.20 - \$0.15 = \$5.05
    $$

    $$
    \text{Ask} = \$5.20 + \$0.30/2 = \$5.20 + \$0.15 = \$5.35
    $$

    The trader believes the true value is $\$5.40$. To profit by buying the option, the trader pays the ask price of $\$5.35$ and holds an asset believed to be worth $\$5.40$, yielding an expected profit of

    $$
    \$5.40 - \$5.35 = \$0.05
    $$

    So yes, there is a small potential profit of $\$0.05$ per option after accounting for the spread.

    The minimum mispricing needed to overcome the spread is the half-spread:

    $$
    \text{Minimum mispricing} = \$0.15
    $$

    For a buyer, the "true" value must exceed the ask ($\$5.35$), i.e., the mispricing relative to the model price must be at least $\$0.15$ (the half-spread). For a seller, the "true" value must be below the bid ($\$5.05$). In general, any profitable trade requires the perceived mispricing to exceed the half-spread of $\$0.15$.

---

**Exercise 5.** Spreads typically widen during periods of high volatility. Suppose the half-spread is $\kappa = 0.001$ under normal conditions ($\sigma = 0.20$) and widens to $\kappa = 0.003$ during a volatility spike ($\sigma = 0.40$). For a delta-hedged short call with $\Gamma = 0.03$ and $S = 100$, compute the expected daily rehedging cost under both regimes. How does the cost-to-gamma-benefit ratio change between regimes?

??? success "Solution to Exercise 5"
    **Normal conditions** ($\sigma = 0.20$, $\kappa = 0.001$): The expected daily rehedging cost for a delta hedge is approximately

    $$
    \text{Daily cost} = 2\kappa S \cdot \Gamma \sigma S \sqrt{\Delta t} \cdot \sqrt{2/\pi}
    $$

    where $\Delta t = 1/252$. Computing:

    $$
    \Gamma \sigma S \sqrt{\Delta t} = 0.03 \times 0.20 \times 100 \times \sqrt{1/252} = 0.6 \times 0.0630 = 0.0378
    $$

    $$
    \text{Daily cost} = 2 \times 0.001 \times 100 \times 0.0378 \times 0.7979 = 0.200 \times 0.0302 = \$0.00603
    $$

    The daily gamma benefit (expected gamma P&L from correctly hedged convexity) is

    $$
    \text{Gamma benefit} = \frac{1}{2}\Gamma \sigma^2 S^2 \Delta t = \frac{1}{2} \times 0.03 \times 0.04 \times 10000 \times \frac{1}{252} = \frac{6.0}{252} = \$0.0238
    $$

    Cost-to-benefit ratio: $0.00603 / 0.0238 = 0.253$, or about $25\%$.

    **High volatility regime** ($\sigma = 0.40$, $\kappa = 0.003$):

    $$
    \Gamma \sigma S \sqrt{\Delta t} = 0.03 \times 0.40 \times 100 \times 0.0630 = 0.0756
    $$

    $$
    \text{Daily cost} = 2 \times 0.003 \times 100 \times 0.0756 \times 0.7979 = 0.600 \times 0.0603 = \$0.0362
    $$

    The daily gamma benefit is

    $$
    \frac{1}{2} \times 0.03 \times 0.16 \times 10000 \times \frac{1}{252} = \frac{24.0}{252} = \$0.0952
    $$

    Cost-to-benefit ratio: $0.0362 / 0.0952 = 0.380$, or about $38\%$.

    The cost-to-benefit ratio increases from $25\%$ to $38\%$ in the high-vol regime. Although both costs and benefits rise, the tripling of $\kappa$ (from $0.001$ to $0.003$) outpaces the doubling of $\sigma$, making hedging proportionally more expensive during volatility spikes.

---

**Exercise 6.** A market maker quotes a bid-ask spread of $\$0.20$ on an option worth $\$8.00$ (model price). The option has $\Gamma = 0.05$, $\Theta = -0.03$ per day, and the underlying spread is $\$0.05$. If the market maker delta-hedges and the expected daily move is consistent with $\sigma = 0.25$, compute: (a) the daily spread revenue from market making; (b) the daily hedging cost (spread on underlying times expected turnover); (c) the net daily P&L before gamma/theta effects. Is the spread sufficient to cover hedging costs?

??? success "Solution to Exercise 6"
    **(a) Daily spread revenue from market making:** If the market maker captures the full option spread on each trade, the revenue per option traded is $\$0.20$. Assuming the market maker trades an average of 1 contract per day (buying at bid, selling at ask), the daily spread revenue is $\$0.20$ per contract per round trip, or $\$0.10$ per side.

    **(b) Daily hedging cost:** The expected daily delta change requires trading $|\delta\Delta| \cdot S$ dollars of the underlying. The expected share turnover is

    $$
    \text{Turnover} = \Gamma \cdot \sigma S \sqrt{\Delta t} \cdot \sqrt{2/\pi} = 0.05 \times 0.25 \times 100 \times \sqrt{1/252} \times 0.7979
    $$

    $$
    = 1.25 \times 0.0630 \times 0.7979 = 0.0629 \text{ shares}
    $$

    The hedging cost per day is the underlying spread times turnover:

    $$
    \text{Hedging cost} = \$0.05 \times 0.0629 = \$0.00314
    $$

    **(c) Net daily P&L before gamma/theta:** The net P&L from spread capture minus hedging costs is

    $$
    \text{Net} = \$0.10 - \$0.00314 = \$0.097
    $$

    (using $\$0.10$ for one side of market making).

    Yes, the spread is more than sufficient to cover hedging costs. The hedging cost ($\$0.003$) is a small fraction of the spread revenue ($\$0.10$). The real risk to the market maker comes from gamma/theta effects: the theta decay earns $\$0.03$/day, while gamma risk (from adverse moves) and inventory risk are the main concerns. The spread provides a substantial buffer over pure hedging costs.
