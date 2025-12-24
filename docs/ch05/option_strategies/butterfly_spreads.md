# Butterfly Spreads

**Butterfly spreads** are neutral options strategies that profit from low volatility by combining multiple vertical spreads to create a position with limited risk, limited profit, and maximum gain when the stock stays near a target price.

---

## The Core Insight

**The fundamental idea:**
- You expect stock to stay in a narrow range
- Create a position that profits from stability
- Use 3 strikes (wings + body) in specific ratio
- Limited risk (small debit), limited reward (but high ROI potential)
- Opposite of straddle (which wants movement)

**The key equation:**
$$
\text{Butterfly} = \text{ITM Spread} - \text{OTM Spread}
$$

Or equivalently:
$$
\text{Buy 1 low strike} + \text{Sell 2 middle strikes} + \text{Buy 1 high strike}
$$

**You're essentially betting: "The stock will be at this specific price at expiration, or very close to it."**

---

## What Is a Butterfly Spread?

**The classic neutral strategy:**

### The Structure

**Long Call Butterfly (most common):**
- Buy 1 ITM call (lower strike)
- Sell 2 ATM calls (middle strike)  
- Buy 1 OTM call (upper strike)
- Strikes equally spaced

**Example:**
- Stock at $100
- Buy 1 × $95 call
- Sell 2 × $100 calls
- Buy 1 × $105 call
- Net debit: $2.50 (small cost)

**What you've created:**
- Max profit at $100 (middle strike)
- Max loss = debit paid ($2.50)
- Breakevens: $97.50 and $102.50
- **Profits from stability**

### The Name Origin

**Visual representation of payoff:**

```
    Profit
      ↑
     2.5|      /\
      2 |     /  \
    1.5|    /    \
      1 |   /      \
    0.5|  /        \
  ────0┼─/──────────\──────→ Stock Price
   -2.5|/            \
       95   100   105
```

**Looks like a butterfly!**
- Wings at $95 and $105
- Body at $100
- Maximum "wingspan" = max profit

### Why Use a Butterfly?

**You use butterflies when:**
1. **Neutral to slightly bullish/bearish**
2. **Expect low volatility** (range-bound)
3. **Target specific price** (pin at strike)
4. **Want high ROI potential** (small cost, decent profit)
5. **Define risk** (limited loss)

**Comparison to other strategies:**

| Strategy | View | Cost | Risk | Profit |
|----------|------|------|------|--------|
| **Butterfly** | Neutral at strike | **Very small** | **Limited** | Limited but high ROI |
| Straddle | Volatile either way | Large | Limited | Unlimited |
| Iron Condor | Range-bound | Credit | Limited | Limited |
| Calendar | Stable + time | Moderate | Limited | Limited |

**Unique feature:** Very low cost, very specific target, very high ROI if right

---

## Types of Butterflies

### 1. Long Call Butterfly (Most Common)

**Structure:**
- Buy 1 ITM call
- Sell 2 ATM calls
- Buy 1 OTM call

**Debit strategy (pay to enter)**

**Example:**
- $95/$100/$105 call butterfly
- Cost: $2.50
- Max profit: $2.50 (strikes $5 apart, cost $2.50)
- Max loss: $2.50 (debit paid)
- Breakeven: $97.50, $102.50

**Payoff at expiration:**

| Stock Price | Payoff |
|-------------|--------|
| < $95 | -$2.50 (max loss) |
| $95 | -$2.50 |
| $97.50 | $0 (breakeven) |
| $100 | **+$2.50 (max profit)** |
| $102.50 | $0 (breakeven) |
| $105 | -$2.50 |
| > $105 | -$2.50 (max loss) |

### 2. Long Put Butterfly

**Structure:**
- Buy 1 OTM put (low strike)
- Sell 2 ATM puts (middle)
- Buy 1 ITM put (high strike)

**Debit strategy**

**Example:**
- $95/$100/$105 put butterfly
- Identical payoff to call butterfly
- Just uses puts instead

**When to use:**
- Same as call butterfly
- Sometimes puts have better pricing
- Tax considerations

**Put-call parity:** Call and put butterflies at same strikes have same payoff!

### 3. Iron Butterfly

**Structure:**
- Sell ATM call
- Sell ATM put (same strike)
- Buy OTM call (protection)
- Buy OTM put (protection)

**Credit strategy (receive money)**

**Example:**
- Sell $100 call
- Sell $100 put
- Buy $105 call
- Buy $95 put
- Net credit: $2.50

**Comparison to long butterfly:**
- Iron butterfly: receive credit, same payoff
- Long butterfly: pay debit, same payoff
- **Iron butterfly = short straddle with wings** (protection)

**Why iron butterfly:**
- Receive credit (positive carry)
- Define risk (wings protect)
- Same profit zone as long butterfly
- More capital efficient

### 4. Broken Wing Butterfly

**Structure:**
- Unequal spacing of strikes
- One wing farther than other

**Example (bullish bias):**
- Buy $95 call
- Sell 2 × $100 calls
- Buy $110 call (instead of $105)
- Asymmetric

**Characteristics:**
- Directional bias (more profit one side)
- Can be done for credit or lower debit
- Advanced variation

### 5. Reverse (Short) Butterfly

**Structure:**
- Opposite of long butterfly
- Sell wings, buy body
- **Profit from volatility**

**Example:**
- Sell $95 call
- Buy 2 × $100 calls
- Sell $105 call
- **Opposite payoff: loses if stable, wins if volatile**

**When to use:**
- Rare (just use straddle instead)
- Specific vega/gamma considerations

---

## Concrete Example: Long Call Butterfly Trade

**Complete walkthrough:**

### Setup

**Stock:** SPY at $450
**View:** Market will stay around $450 for next month (consolidation)
**Volatility:** Moderate (VIX at 18)
**Strategy:** 30-day call butterfly

**Available options:**

| Strike | Call Premium | Put Premium |
|--------|--------------|-------------|
| $445 | $7.50 | $2.50 |
| $450 | $4.50 | $4.50 |
| $455 | $2.50 | $7.50 |

### The Trade: $445/$450/$455 Call Butterfly

**Execute:**
- Buy 1 × $445 call @ $7.50
- Sell 2 × $450 calls @ $4.50 each = $9.00 received
- Buy 1 × $455 call @ $2.50
- **Net debit: $7.50 + $2.50 - $9.00 = $1.00**

**Position summary:**
- Cost: $100 (1 contract)
- Max profit: $400 ($5 spread - $1 cost = $4)
- Max loss: $100 (debit)
- ROI potential: 400% (!!!)
- Breakevens: $446, $454

### The Math

**At each strike:**

**Below $445:**
- All calls worthless
- Loss: -$100 (full debit)

**At $445:**
- $445 call: $0
- $450 calls: $0
- $455 call: $0
- Loss: -$100

**At $447:**
- $445 call: $2 ($200 value)
- $450 calls: $0
- $455 call: $0
- P&L: +$200 - $100 = **+$100**

**At $450 (MAX PROFIT):**
- $445 call: $5 ($500 value)
- $450 calls: $0 (ATM, no value)
- $455 call: $0
- P&L: +$500 - $100 = **+$400 (400% ROI!)**

**At $453:**
- $445 call: $8 ($800)
- $450 calls: -$6 ($-600, short 2)
- $455 call: $0
- P&L: $800 - $600 - $100 = **+$100**

**At $455:**
- $445 call: $10 ($1,000)
- $450 calls: -$10 ($-1,000)
- $455 call: $0
- P&L: $0 - $100 = **-$100**

**Above $455:**
- All spreads offset
- Loss: -$100 (full debit)

### Scenario 1: Perfect! SPY at $450 (Max Profit)

**At expiration:**
- SPY exactly at $450
- Butterfly worth $4.00
- Entry: $1.00
- **Profit: $300 (300% return!)**

**Why it worked:** Stock pinned exactly at middle strike (rare but beautiful)

### Scenario 2: Close but Not Perfect - SPY at $448

**At expiration:**
- SPY at $448
- $445 call worth: $3
- $450 calls: $0
- Net value: $3
- Entry: $1
- **Profit: $200 (200% return)**

**Still profitable:** Within the profit zone

### Scenario 3: Outside Range - SPY at $460

**At expiration:**
- SPY at $460 (big move up)
- All options ITM, spreads cancel
- Net value: $0
- Entry: $1
- **Loss: $100 (100% loss)**

**Wrong:** Stock moved too much

### Scenario 4: Outside Range - SPY at $440

**At expiration:**
- SPY at $440 (moved down)
- All calls worthless
- Net value: $0
- Entry: $1
- **Loss: $100 (100% loss)**

**Wrong:** Stock moved too much (other direction)

### Scenario 5: Early Exit on Volatility Spike

**After 15 days:**
- SPY still at $450
- But VIX spikes to 25 (vol up)
- Butterfly loses value (vega negative)
- Now worth: $0.60
- Entry: $1.00
- **Loss: $40 if exit now**

**Decision:** Either exit for small loss, or hold hoping for vol crush

---

## Butterfly Mechanics

### Strike Spacing

**Equal spacing required (for standard butterfly):**

**Good examples:**
- $95/$100/$105 (each $5 apart) ✓
- $145/$150/$155 (each $5 apart) ✓
- $48/$50/$52 (each $2 apart) ✓

**Bad examples:**
- $95/$100/$110 (unequal) ✗
- $145/$150/$160 (unequal) ✗

**Why equal spacing:**
- Ensures payoff symmetry
- Pricing works correctly
- Standard contracts

**Width choice:**
- Wider spreads ($95/$105 instead of $95/$100/$105):
  - Cheaper
  - Lower probability
  - Higher ROI potential
- Tighter spreads:
  - More expensive
  - Higher probability
  - Lower ROI

### The Greeks

**Delta:**
- Near zero (neutral)
- Slightly positive/negative depending on where stock is
- Changes as stock moves

**Gamma:**
- Negative at wings
- Positive at body
- Net gamma typically negative

**Theta:**
- **Positive** (benefits from time decay)
- Accelerates near expiration
- Wants time to pass

**Vega:**
- **Negative** (hurt by volatility increase)
- Wants IV to decrease
- Opposite of straddle

**Key insight:** Butterflies are short volatility + positive theta (like iron condors but more targeted)

---

## Iron Butterfly Example

**The credit version:**

### Setup

**Stock:** AAPL at $180
**Strategy:** 45-day iron butterfly

### The Trade

**Execute:**
- Sell $180 call @ $5.50
- Sell $180 put @ $5.50
- Buy $190 call @ $2.00 (protection)
- Buy $170 put @ $2.00 (protection)

**Net credit: $11 - $4 = $7.00**

**Position summary:**
- Credit received: $700
- Max profit: $700 (if at $180)
- Max loss: $300 ($10 spread - $7 credit)
- Breakevens: $173, $187
- Risk/reward: Risk $300 to make $700

### Payoff Analysis

**At $180 (max profit):**
- Both sold options expire worthless
- Both bought options worthless
- Keep entire credit: **+$700**

**At $175:**
- Short put ITM: -$5 ($-500)
- Long put OTM: $0
- Calls worthless
- P&L: $700 - $500 = **+$200**

**At $170 (breakeven):**
- Short put: -$10 ($-1,000)
- Long put: +$10 ($+1,000)
- P&L: $700 - $1,000 + $1,000 = **+$700 net, but spread lost $300**
- Net: $700 credit - $300 = **$0 (breakeven at $173)**

**Below $170 or above $190:**
- Spreads max out
- Loss: $300 (max loss)

### Iron Butterfly vs. Iron Condor

| Aspect | Iron Butterfly | Iron Condor |
|--------|---------------|-------------|
| **Short strikes** | Same (ATM both) | Different (OTM both) |
| **Profit zone** | Narrow (pinpoint) | Wide (range) |
| **Max profit** | Higher | Lower |
| **Probability** | Lower (specific) | Higher (range) |
| **Risk/reward** | Better (if right) | More conservative |

**Iron butterfly = "pinpoint" iron condor**

---

## When to Use Butterflies

### Favorable Conditions

**1. Low volatility expected:**
- VIX declining
- Post-event (earnings passed)
- Market consolidation
- **Stock should stay put**

**2. Specific target price:**
- Technical level (support/resistance)
- Round number ($100, $150, etc.)
- Option pin expected
- Historical mean

**3. After volatile move:**
- Stock spiked, now settling
- IV crush expected
- Profit from stabilization

**4. Event play (after event):**
- Earnings just reported
- IV will collapse
- Stock likely to drift

**5. Cheap entry:**
- Can establish butterfly for $1-2
- High ROI potential (300-500%)
- Low risk ($1-2 max loss)

### Unfavorable Conditions

**1. High volatility expected:**
- Earnings coming
- Binary events
- Market uncertainty
- **Stock will move**

**2. Trending market:**
- Strong directional bias
- Momentum building
- Will blow through butterfly

**3. Wide bid-ask spreads:**
- Illiquid options
- Give up edge to spread
- Better strategies available

**4. Very short time:**
- < 1 week to expiry
- Gamma risk high
- Hard to manage

---

## Butterfly vs. Straddle (The Opposite)

**The fundamental contrast:**

| Aspect | Butterfly | Straddle |
|--------|-----------|----------|
| **View** | Stable (neutral) | Volatile (either way) |
| **Cost** | Very low ($1-2) | High ($8-10) |
| **Theta** | Positive (earn) | Negative (pay) |
| **Vega** | Negative (hurt by vol) | Positive (benefit from vol) |
| **Profit zone** | Narrow (near strike) | Wide (far from strike) |
| **Max profit** | Limited (but high ROI) | Unlimited |
| **Max loss** | Limited (small) | Limited (large) |
| **Complexity** | Higher (4 legs) | Lower (2 legs) |

**Perfect opposites:**
- Butterfly profits if calm (collect theta, avoid vega)
- Straddle profits if volatile (overcome theta with movement/vega)

**Interesting strategy:**
- Can hedge straddle with butterfly
- Reduce cost, accept capped profit
- Advanced combination

---

## Advanced Variations

### 1. Unbalanced Butterfly

**Structure:**
- Different ratios (not 1-2-1)
- Example: 1-3-2 or 2-4-2

**Use:**
- Fine-tune risk/reward
- Directional bias
- Advanced traders

### 2. Skip-Strike Butterfly

**Structure:**
- Skipped strikes in middle
- Example: Buy $95, sell 2×$100, buy $110 (skipped $105)

**Effect:**
- Wider profit zone
- Lower max profit
- Different shape

### 3. Double Butterfly

**Structure:**
- Two butterflies at different centers
- Example: $95/$100/$105 + $100/$105/$110

**Use:**
- Wider profit zone
- Multiple targets
- Bimodal expectations

### 4. Condor (Related Strategy)

**Structure:**
- Like butterfly but 4 different strikes
- Example: Buy $95, sell $100, sell $105, buy $110
- Wider body

**Difference from butterfly:**
- Butterfly: Pinpoint (one middle strike)
- Condor: Range (two middle strikes)

---

## Common Mistakes

### Mistake 1: Expecting Perfect Pin

❌ **Wrong:**
- Buy butterfly centered at $100
- Expect stock EXACTLY at $100
- Disappointed if at $99 or $101

**Why unrealistic:**
- Exact pin is rare
- Need to profit in range
- Not just one price

✅ **Better:**
- Accept profit anywhere in range
- Take profits at 50% of max
- Don't wait for perfect

### Mistake 2: Entering During High IV

❌ **Wrong:**
- Buy butterfly before earnings
- IV at 60% (very high)
- Expensive to establish

**Why it fails:**
- Overpaying for volatility
- Even if stable, IV crush hurts
- Vega loss

✅ **Better:**
- Enter AFTER event (IV declining)
- Or use iron butterfly (credit)
- Avoid high IV entry

### Mistake 3: Too Many Legs, High Costs

❌ **Wrong:**
- Pay $0.25 spread on each of 4 legs
- Total: $1.00 in bid-ask
- Butterfly only cost $1.50 net
- **Gave away 67% to spread!**

**Why it fails:**
- Transaction costs eat edge
- Need tight markets
- Leakage is real

✅ **Better:**
- Use liquid underlyings (SPY, QQQ)
- Enter as single order (multi-leg)
- Check net debit, not individual legs

### Mistake 4: Wrong Expiration

❌ **Wrong:**
- Too long (60+ days): expensive, theta slow
- Too short (< 1 week): gamma risk, hard to manage

✅ **Better:**
- 30-45 days ideal
- Balance theta and gamma
- Enough time to work

### Mistake 5: Ignoring Assignment Risk

❌ **Wrong:**
- Iron butterfly short legs deep ITM
- Ignore early assignment risk
- Surprised by assignment

**Why it matters:**
- Short ATM options can be assigned
- Especially near dividends or earnings
- Breaks the position

✅ **Better:**
- Close if deep ITM
- Roll if necessary
- Monitor assignment risk

---

## Position Management

### Taking Profits

**Guidelines:**

**At 50% of max profit:**
- Target achieved
- Take profit and redeploy
- Don't be greedy

**At 75% of max profit:**
- Excellent result
- Definitely close
- Diminishing returns

**Example:**
- Butterfly max profit: $4
- Current value: $2 (50% of max)
- Cost: $1
- Profit: $1 (100% return)
- **Close! Don't wait for $4**

### Managing Losers

**If stock moves outside range:**

**Early in trade:**
- Consider closing for small loss
- Redeploy capital
- Don't hope it comes back

**Near expiration:**
- Often worth holding to expiration
- Max loss already defined
- Small chance of recovery

**Stop loss:**
- 50% of debit paid
- Or exit at 7-14 days before expiry

### Rolling

**If stock drifts slightly:**
- Can roll butterfly to follow
- Close current, open new centered at new price
- Costs commissions and spread

**Example:**
- Butterfly at $100, stock now $103
- Roll to $103-centered butterfly
- Continue the trade

---

## What to Remember

### Core Concept

**Butterflies profit from stability at a specific price:**

$$
\text{Butterfly} = \text{Buy Wing} + \text{Sell 2× Body} + \text{Buy Wing}
$$

- Very low cost ($1-2)
- Very high ROI potential (300-500%)
- Very specific target (pinpoint)
- Limited risk (max loss = debit)

### The Structure

**Standard ratios:**
- 1-2-1 (long-short-short-long)
- Equal strike spacing
- Call or put (same payoff)

**Iron butterfly:**
- Credit version
- Short straddle + long strangle
- Same profit zone

### The Greeks

**Characteristics:**
- **Theta:** Positive (time friend)
- **Vega:** Negative (vol enemy)
- **Delta:** Near zero (neutral)
- **Gamma:** Negative net

**Opposite of straddle on theta and vega!**

### When to Use

**Best scenarios:**
- Post-event (IV declining)
- Consolidation expected
- Specific target price
- Low volatility forecast
- High ROI opportunity

**Avoid:**
- Before events (high IV)
- Trending markets
- Very short time
- Illiquid options

### Success Factors

**What you need:**
1. Accurate price target
2. Low volatility
3. Time for theta to work
4. Tight bid-ask spreads
5. Exit discipline (50% profits)

### Risk Profile

**Favorable:**
- Limited risk (small debit)
- High ROI potential
- Defined max loss
- Positive theta

**Unfavorable:**
- Narrow profit zone
- Low probability (specific price)
- Complex (4 legs)
- Negative vega

### Butterfly vs. Similar Strategies

**vs. Straddle:**
- Opposite views (stable vs. volatile)
- Opposite Greeks (theta/vega)

**vs. Iron Condor:**
- Butterflies: Pinpoint
- Iron Condors: Range

**vs. Calendar:**
- Butterflies: Single expiration
- Calendars: Multiple expirations

### The Math

**Max profit:**
$$
\text{Max Profit} = \text{Strike Width} - \text{Net Debit}
$$

**Breakevens:**
$$
\text{Lower BE} = \text{Lower Strike} + \text{Net Debit}
$$
$$
\text{Upper BE} = \text{Upper Strike} - \text{Net Debit}
$$

**Example:**
- $95/$100/$105 butterfly
- Cost: $1
- Max profit: $5 - $1 = $4
- Breakevens: $96, $104

### Common Mistakes

**Avoid:**
1. Expecting perfect pin (unrealistic)
2. Entering during high IV (expensive)
3. Transaction costs eating edge (illiquid)
4. Wrong expiration (too short/long)
5. Holding to max profit (be greedy, lose)

### Your Strategy Arsenal

**Where this fits:**

```
NEUTRAL STRATEGIES:
1. Calendar Spreads (time + neutral)
2. Butterfly Spreads (pinpoint + neutral) ← You are here!
3. Iron Condor (range + neutral)
   ↓
OPPOSITE:
4. Straddles (volatile + neutral)
```

**Butterflies are the "laser-focused" neutral strategy!**

### Practical Wisdom

- **Exact pins are rare** (profit in range, not just one price)
- **Take 50% profits** (don't wait for max)
- **Enter after IV spike** (not before)
- **Use liquid underlyings** (SPY, QQQ, AAPL)
- **30-45 days ideal** (balance theta and gamma)
- **Positive theta works slowly** (be patient)
- **4 legs = complexity** (manage spreads carefully)

### Final Thought

**Butterflies are precision instruments:**

> "A butterfly is like a sniper rifle - you pick a specific target (price) and take your shot (enter position). Most of the time you miss (stock moves away). But when you hit (stock pins at your strike), the payoff is spectacular (300-500% ROI). The cost of ammunition (premium) is low, so you can afford to take many shots. But you need patience, accuracy, and discipline. Don't hold out for the perfect pin - take profits at 50% and live to trade another day."

**The truth:**
- Low probability (10-20% typically)
- But high reward when right (300%+)
- **Acceptable risk/reward for patient traders**
- Complements other strategies (use alongside)
- Not your only strategy (part of toolkit)

**Master butterflies to trade specific price targets with defined risk!** 🦋📊
