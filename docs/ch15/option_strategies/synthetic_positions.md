# Synthetic Positions

**Synthetic positions** use combinations of options (calls and puts) to **replicate the payoff of other assets or strategies**, most commonly **stock-like exposure**, without directly trading the underlying. They rely on **put–call parity** and are fundamental to understanding how options encode forward prices, leverage, and financing.

---

## The Core Insight

**The fundamental idea:**

- Calls and puts are not independent
- Their prices are linked by **put–call parity**
- By combining options, you can **recreate stock, short stock, or forward contracts**
- These positions often behave almost identically to the underlying
- Differences come from financing, dividends, and early-exercise features

**The key equation (put–call parity):**

\[
C - P = S - K e^{-rT}
\]

Rearranged:

\[
S = C - P + K e^{-rT}
\]

This identity is the mathematical foundation of all synthetic positions.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/put_call_parity_synthetic_positions.png?raw=true" alt="put_call_parity_synthetic_positions" width="700">
</p>
**Figure 1:** Put-call parity relationship diagram showing the fundamental no-arbitrage equation C - P = S - K×e^(-rT) that links call prices, put prices, stock price, and the present value of the strike, forming the theoretical foundation for all synthetic position construction and ensuring price consistency across options markets.

---

## What Is a Synthetic Position?

A **synthetic** is a position constructed from options that **replicates the payoff** of another position at expiration (and often approximately before expiration).

**Key idea:**
> If two portfolios have the same payoff in all states, they must have the same price (no-arbitrage).

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/synthetic_components_breakdown.png?raw=true" alt="synthetic_components_breakdown" width="700">
</p>
**Figure 2:** Synthetic components breakdown showing how various option combinations decompose into equivalent positions, illustrating the building blocks (long/short calls and puts) that create synthetic stock, synthetic forwards, and other replicated exposures through different combinations.

---

## Why Synthetics Exist

### 1. Capital Efficiency
You may want stock exposure without:

- paying full share price
- tying up capital
- triggering taxes or restrictions

Synthetics can replicate exposure with **less upfront cash**.

### 2. Structural Constraints

- Shorting stock may be impossible or expensive
- Certain accounts may restrict stock transactions
- Options may be more liquid than shares

### 3. Hedging and Risk Transfer

Institutions frequently use synthetics to:
- hedge large positions
- convert exposure without trading the underlying
- neutralize dividends or financing effects

---

## Core Synthetic Positions

### 1) Synthetic Long Stock

**Replicates:** owning the stock

#### Structure

- **Buy 1 call**
- **Sell 1 put**
- Same strike \(K\), same expiration \(T\)

\[
\text{Synthetic Long Stock} = +C(K,T) - P(K,T)
\]

#### Payoff at Expiration

\[
\max(S-K,0) - \max(K-S,0) = S - K
\]

Linear, stock-like payoff.

#### Interpretation

- Delta ≈ +1
- Unlimited upside
- Downside similar to owning stock (below strike)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/synthetic_long_stock.png?raw=true" alt="synthetic_long_stock" width="700">
</p>
**Figure 3:** Synthetic long stock profit/loss diagram showing how buying a call and selling a put at the same strike creates a linear payoff identical to owning stock, with unlimited upside and full downside exposure, demonstrating the fundamental replication of equity exposure using only options.

---

### 2) Synthetic Short Stock

**Replicates:** shorting the stock

#### Structure

- **Sell 1 call**
- **Buy 1 put**
- Same strike and expiration

\[
\text{Synthetic Short Stock} = -C(K,T) + P(K,T)
\]

#### Payoff at Expiration

\[
-(S-K) = K - S
\]

#### Interpretation

- Delta ≈ −1
- Unlimited downside risk (like short stock)
- Profits if stock falls

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/synthetic_short_stock.png?raw=true" alt="synthetic_short_stock" width="700">
</p>
**Figure 4:** Synthetic short stock profit/loss diagram demonstrating how selling a call and buying a put at the same strike creates a linear payoff identical to shorting stock, with profits when stock falls and unlimited risk on the upside, showing the mirror image of synthetic long stock.

---

### 3) Synthetic Forward Contract

From parity:

\[
C - P = S - K e^{-rT}
\]

So:
- Long call + short put ≈ **long forward**
- Strike-adjusted cash position completes equivalence

This is heavily used in institutional pricing.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/conversion_relationships_synthetic_positions.png?raw=true" alt="conversion_relationships_synthetic_positions" width="700">
</p>
**Figure 5:** Conversion and reversal relationships showing how to transform between equivalent positions—conversions combine long stock with protective collars (long put + short call), while reversals use short stock with synthetic longs, illustrating advanced arbitrage strategies that exploit deviations from put-call parity.

---

## The Portfolio View


---

## Economic Interpretation

**Understanding what this strategy REALLY represents economically:**

### The Core Economic Trade-Off

This strategy involves specific economic trade-offs that determine when it's most valuable. The key is understanding what you're giving up versus what you're gaining in economic terms.

**Economic equivalence:**

$$
\text{Strategy Payoff} = \text{Component 1} + \text{Component 2} - \text{Cost/Benefit}
$$

### Why This Structure Exists Economically

Markets create these structures because different participants have different:
- Risk preferences
- Time horizons
- Capital constraints
- View on volatility vs. direction

### Professional Institutional Perspective

Institutional traders view this strategy as a tool for:
1. **Risk management:** Precise control over exposure
2. **Capital efficiency:** Optimal use of buying power
3. **Probability engineering:** Trading win rate for win size
4. **Volatility positioning:** Specific exposure to implied volatility changes

Understanding the economic foundations helps you recognize when the strategy offers genuine edge versus when market pricing is fair.


### Synthetic Long Stock

\[
\Pi = C(K,T) - P(K,T)
\]

**Greeks (approximate):**

- Delta: ≈ +1
- Gamma: near 0 (away from ATM)
- Theta: small (call theta − put theta)
- Vega: small (call vega − put vega)

### Synthetic Short Stock

\[
\Pi = -C(K,T) + P(K,T)
\]

Greeks mirror synthetic long stock with opposite signs.

---

## Concrete Example 1: Synthetic Long Stock

**Setup:**

- Stock at \(S = 100\)
- 3-month options
- Strike \(K = 100\)

**Trade:**

- Buy $100 call for $5
- Sell $100 put for $5

**Net cost:** ~$0 (ignoring interest/dividends)

### Outcomes at Expiration

| Stock Price | Call | Put | Net Payoff |
|------------|------|-----|------------|
| 80 | 0 | -20 | -20 |
| 100 | 0 | 0 | 0 |
| 120 | 20 | 0 | +20 |

**Identical to owning stock from $100.**

---

## Concrete Example 2: Synthetic Short Stock

**Setup:**

- Stock at \(S = 100\)
- Same options

**Trade:**

- Sell $100 call for $5
- Buy $100 put for $5

### Outcomes

| Stock Price | Call | Put | Net Payoff |
|------------|------|-----|------------|
| 80 | 0 | +20 | +20 |
| 100 | 0 | 0 | 0 |
| 120 | -20 | 0 | -20 |

Identical to shorting stock from $100.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/concrete_example_synthetic_positions.png?raw=true" alt="concrete_example_synthetic_positions" width="700">
</p>
**Figure 6:** Concrete examples of synthetic long and short stock positions showing detailed P&L tables and payoff diagrams at various stock prices, illustrating how the option combinations exactly replicate stock exposure with identical profit/loss outcomes at expiration across all price scenarios.

---

## Strike Selection

### ATM Synthetics (Most Common)

- Best replication of stock
- Delta ≈ ±1
- Most liquid options
- Most accurate parity behavior

### ITM / OTM Synthetics

- Still work mathematically
- Different capital requirements
- Delta deviates slightly from ±1
- Used for fine-tuning exposure

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/strike_selection_synthetics.png?raw=true" alt="strike_selection_synthetics" width="700">
</p>
**Figure 7:** Strike selection for synthetic positions showing how ATM synthetics (strike equals stock price) replicate stock most accurately with delta ≈ ±1, while ITM and OTM synthetics create leverage or deductibles with different capital requirements and delta profiles, demonstrating strategic strike choices for customized exposure.

---

## Time Selection

### Short-Dated

- Tracks stock closely
- Higher gamma near expiration
- More sensitive to price moves

### Longer-Dated

- Smoother behavior
- Less gamma
- Often preferred for long-term exposure

---

## Synthetics vs. Stock

| Aspect | Synthetic | Stock |
|------|-----------|-------|
| Capital | Lower upfront | Full share price |
| Dividends | Indirect (priced in) | Received directly |
| Voting rights | None | Yes |
| Margin | Often required | None (cash account) |
| Flexibility | High | Lower |

**Key insight:** synthetics replicate **price exposure**, not ownership benefits.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/synthetic_vs_stock_comparison.png?raw=true" alt="synthetic_vs_stock_comparison" width="700">
</p>
**Figure 8:** Comprehensive comparison of synthetic positions versus actual stock holdings showing key differences in capital requirements, dividend treatment, voting rights, margin obligations, and operational flexibility, illustrating when synthetics offer advantages (capital efficiency, shorting) versus when stock is preferable (dividends, voting, simplicity).

---

## Practical Applications

### 1) Replacing Stock Exposure

- Want delta ≈ 1
- Less capital tied up
- Easy to adjust or close

### 2) Avoiding Short-Sale Constraints

- Hard-to-borrow stock
- Use synthetic short instead

### 3) Transition Trades

- Convert stock → options exposure (or vice versa)
- Maintain risk while restructuring portfolio

---

## Risks and Caveats

### 1) Assignment Risk

- Short option leg can be assigned
- Leads to temporary stock position
- Must be managed proactively

### 2) Dividend Effects

- Dividends affect put–call parity
- Early assignment risk increases near ex-dividend dates

### 3) Financing Differences

- Interest rates embedded in option prices
- Synthetic may not be exactly free

### 4) Margin Requirements

- Brokers may require margin similar to stock exposure
- Not “free leverage” in practice

---


---

## Practical Guidance

**Step-by-step implementation framework:**

### Step 1: Market Assessment

**Before entering, evaluate:**

1. **Market environment:**
   - Trend direction and strength
   - Volatility level (IV percentile)
   - Upcoming events or catalysts

2. **Technical analysis:**
   - Support/resistance levels
   - Volume and liquidity
   - Recent price action

3. **Fundamental backdrop:**
   - Company-specific news
   - Sector dynamics
   - Macro environment

### Step 2: Strategy Selection Criteria

**Enter this strategy when:**
- [Specific market conditions]
- [Volatility requirements]
- [Time horizon matches]
- [Risk tolerance appropriate]

**Avoid this strategy when:**
- [Unfavorable conditions]
- [Wrong volatility environment]
- [Insufficient time or liquidity]

### Step 3: Position Sizing

**Calculate maximum position size:**

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times \text{Risk\%}}{\text{Max Loss Per Contract}}
$$

**Conservative guidelines:**
- Risk 1-2% per trade when learning
- Max 5 uncorrelated positions
- Never more than 20% of portfolio in options

### Step 4: Entry Execution

**Best practices:**

1. **Use limit orders:** Never use market orders
2. **Check liquidity:** Bid-ask spread < 10% of mid-price
3. **Time entry:** Avoid first/last 30 minutes of trading day
4. **Single order:** Enter as complete strategy, don't leg in

### Step 5: Position Management

**Active management rules:**

**Profit targets:**
- Take profit at [X]% of max profit
- Scale out if appropriate
- Don't be greedy

**Loss limits:**
- Cut losses at [Y]% of max loss
- Don't hope for recovery
- Preserve capital

**Time-based exits:**
- Monitor theta decay
- Exit if [time-based trigger]

### Step 6: Adjustment Protocols

**When to adjust:**
- Position threatened
- Market environment changes  
- New information emerges

**How to adjust:**
- [Adjustment technique 1]
- [Adjustment technique 2]
- [When to take loss instead]

### Step 7: Record Keeping

Track every trade:
- Entry/exit dates and prices
- Rationale for trade
- Market conditions (IV, trend, etc.)
- P&L and lessons learned

### Common Execution Mistakes to Avoid

1. **Entering at wrong volatility level**
2. **Ignoring liquidity**
3. **Over-sizing positions**
4. **Failing to set exit rules upfront**
5. **Emotional decision-making**


## Common Mistakes

### 1) Forgetting Dividends

- Parity assumes known dividends.
- Ignoring them causes mispricing expectations.

### 2) Treating Synthetics as Limited Risk

- Synthetic long stock has **full downside risk**.
- Synthetic short stock has **unlimited risk**.

### 3) Ignoring Early Exercise

- American options break exact parity before expiration.

---

## When to Use Synthetics

### Best Use Cases

- You want stock-like exposure without stock
- You need flexibility and fast adjustments
- You understand assignment and margin mechanics

### Avoid When

- You want dividends or voting rights
- You cannot manage assignment risk
- Liquidity is poor

---

## Summary

Synthetic positions reveal the **true structure of options markets**:

- Calls, puts, and stock are tightly linked
- Options are not “side bets” — they encode forwards and financing
- Understanding synthetics is essential for:

      - advanced spreads
      - arbitrage intuition
      - professional options trading

Master synthetics, and the rest of options theory becomes much clearer.


---

## Worst Case Scenario

**What happens when everything goes wrong:**

### The Nightmare Setup

**How it starts:**
- [Initial adverse move]
- [Market condition deterioration]
- [Position response]

**The deterioration:**

**Days 1-7:**
- [Early warning signs]
- [Position losing value]
- [Critical decision point]

**Through expiration:**
- [Continued adverse movement]
- [Max loss approached/realized]
- [Final outcome]

### Maximum Loss Calculation

**Worst case mathematics:**

$$
\text{Max Loss} = [\text{Formula}]
$$

**Example calculation:**
- [Specific example with numbers]
- [Loss breakdown]
- [Impact on portfolio]

### What Goes Wrong

The worst case occurs when:
1. **Wrong direction:** Market moves against you
2. **Wrong magnitude:** Move is severe
3. **Wrong timing:** Happens quickly, no time to adjust
4. **Wrong volatility:** IV moves unfavorably

### The Cascade Effect

**Multiple losing positions:**
- [Scenario 1: First loss]
- [Scenario 2: Revenge trading]
- [Scenario 3: Account damage]

**Total damage:**
- [Cumulative loss calculation]
- [Portfolio impact percentage]
- [Recovery difficulty]

### Assignment and Pin Risk

**Complexity at expiration:**
- [Assignment scenario]
- [Pin risk explanation]
- [Weekend risk]
- [Cleanup process]

### Real Examples of Disasters

**Historical example 1:**
- [Setup and expectation]
- [What happened]
- [Final loss]

**Historical example 2:**
- [Setup and expectation]
- [What happened]
- [Final loss]

### Psychology of Losses

**Emotional stages:**
1. **Denial:** "It will recover"
2. **Hope:** "Just need a small bounce"
3. **Anger:** "Market is rigged"
4. **Capitulation:** "Just close it"
5. **Learning:** "What went wrong?"

**Winning trader mindset:**
- Accept losses quickly
- Analyze dispassionately
- Learn and adapt
- Move forward

### Preventing Worst Case

**Risk management strategies:**

1. **Position sizing:**
   - Never risk more than [X]% per trade
   - Respect maximum loss calculations

2. **Stop losses:**
   - Exit at [trigger level]
   - Don't hope for recovery

3. **Diversification:**
   - Multiple uncorrelated positions
   - Different timeframes
   - Different strategies

4. **Avoid high-risk scenarios:**
   - [Scenario to avoid 1]
   - [Scenario to avoid 2]

### The Ultimate Protection

$$
\text{Survivability} = \frac{\text{Capital Remaining}}{\text{Capital Initial}} > 0.85
$$

Even in worst case, proper position sizing ensures you survive to trade again. The market will test you - preparation determines whether you survive or blow up.

**Remember:** Worst case WILL happen eventually. Position accordingly.



---

## Best Case Scenario

**What happens when everything goes right:**

### The Perfect Setup

**Ideal entry conditions:**
- [Market condition 1]
- [Volatility at optimal level]
- [Catalyst working in your favor]

**The optimal sequence:**

**Days 1-7:**
- [What happens initially]
- [Position response]
- [Decision point]

**Through expiration:**
- [Continuation of favorable move]
- [Profit realization]
- [Final outcome]

### Maximum Profit Achievement

**Best case mathematics:**

$$
\text{Max Profit} = [\text{Formula}]
$$

$$
\text{ROI} = \frac{\text{Max Profit}}{\text{Capital At Risk}} \times 100\%
$$

**Example calculation:**
- [Specific example with numbers]
- [Profit breakdown]
- [ROI calculation]

### What Makes It Perfect

The best case requires:
1. **Right direction:** Market moves as anticipated
2. **Right magnitude:** Move is sufficient for profit
3. **Right timing:** Move happens within time frame
4. **Right volatility:** IV behaves favorably

### Comparison to Alternatives

**This strategy vs. [Alternative]:**
- [How best case compares]
- [When this strategy wins]
- [Trade-offs involved]

### Professional Profit-Taking

**When to take profits:**
- At [X]% of max profit
- [Time-based consideration]
- [Volatility-based trigger]

**The compounding advantage:**

Taking profits early and redeploying can yield better annual returns than holding for maximum profit due to reduced risk and faster capital recycling.

### The Dream Scenario

**Extreme best case:**
- [Exceptional circumstance]
- [Outsized gain]
- [Probability and why it's rare]

**Key insight:** Best case is not guaranteed and should not be expected. Position sizing should assume realistic outcomes, not best case scenarios.

