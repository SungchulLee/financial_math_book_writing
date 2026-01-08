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

### 1. The Structure

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

### 2. The Name Origin

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

### 3. Why Use a Butterfly?

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


---

## Economic

**Understanding what butterfly spreads REALLY represent economically:**

### 1. The Core Economic Trade-Off

Butterfly spreads represent a fundamental economic proposition: **trading probability of profit for magnitude of profit**. Unlike directional strategies (high risk, high reward) or credit spreads (high probability, small reward), butterflies occupy a unique middle ground.

**Economic equivalence:**

$$
\text{Butterfly} = \underbrace{\text{Bull Spread}}\_{\text{Lower Half}} + \underbrace{\text{Bear Spread}}\_{\text{Upper Half}}
$$

Or alternatively:

$$
\text{Butterfly} = \underbrace{\text{Long Strike at Wings}}\_{\text{Insurance}} - \underbrace{2 \times \text{Short Strike at Body}}\_{\text{Premium Sale}}
$$

**Why this matters economically:**

- **Bull spread alone:** Profits if up, loses if down (directional)

- **Bear spread alone:** Profits if down, loses if up (directional)

- **Butterfly (combination):** Profits ONLY if stays stable (neutral)

- **Trade-off:** Gave up probability (must land in narrow range) for lower cost and defined risk

### 2. Why This Structure Exists Economically

Markets create butterflies because of **fundamental disagreements about future volatility**:

**1. Volatility trading without infinite risk:**

**The basic problem:**

- Want to bet on LOW volatility (stock stays stable)

- **Short straddle:** Unlimited risk if wrong

- **Butterfly:** Defined risk, same thesis

**Butterfly as insurance-wrapped straddle:**

$$
\text{Butterfly} = \text{Short Straddle at Center} + \text{Long Strangle Protection at Wings}
$$

**Example:**

- Short straddle at $100: Collect $8, unlimited risk

- Add wings at $95/$105: Pay $3 for protection

- **Net butterfly:** Profit $5 if stable, max loss $5 if volatile

- **Key:** Converted unlimited risk to defined risk for cost of $3

**Economic truth:** Butterflies are how you express "low volatility" view without risking account destruction.

**2. Mean reversion with precise timing:**

Most traders believe in mean reversion, but timing is everything:

- "Stock will revert to $100" 

- **When?** This week, next month, next year?

**Butterfly expresses:** "Stock will be AT $100 in exactly 45 days"

This precision creates three economic scenarios:

**Scenario A: Right about price AND timing** → Max profit  
**Scenario B: Right about price, wrong about timing** → Partial profit or loss  
**Scenario C: Wrong about price** → Max loss (but defined!)

**The economic edge:** If you can predict BOTH price AND timing better than market expects, butterflies offer asymmetric risk/reward.

**3. Time decay harvesting with lottery protection:**

**The time decay opportunity:**

- ATM options decay fastest

- OTM/ITM options decay slower

- **Butterfly exploits this differential**

**Structure breakdown:**

- **Sell 2× ATM** (body): Maximum theta decay

- **Buy 1× ITM + 1× OTM** (wings): Less theta decay

- **Net:** Positive theta if price stable

**Economic equation:**

$$
\text{Butterfly P&L} = \underbrace{\text{Theta Decay}}\_{\text{+Daily}} - \underbrace{\text{Gamma Loss}}\_{\text{-If Moves}} - \underbrace{\text{Vega Loss}}\_{\text{-If IV Drops}}
$$

**If stock stable:** Theta overwhelms gamma/vega → Profit  
**If stock moves:** Gamma/vega overwhelm theta → Loss (but capped!)

### 3. Professional Institutional Perspective

**How institutions actually use butterflies:**

**1. Volatility arbitrage:**

**Market-makers' bread and butter:**

- Sell inflated IV (rich ATM options)

- Buy cheaper IV (wings)

- **Lock in skew differential**

**Example:**

- ATM $100 options: IV 35% (overpriced by 3%)

- Wing options: IV 32% (fairly priced)

- **Butterfly captures 3% IV edge**

- If realized volatility is 32% (as expected), butterfly profits from overpriced ATM

**Why it works:**

- Retail overbuys ATM options (lottery tickets)

- Professionals sell butterflies to them

- Profit from IV mean reversion

**2. Earnings precision betting:**

**Sophisticated earnings trades:**

- Most traders: Buy straddles (bet on big move)

- **Professionals:** Sell butterflies centered at expected move

**Example:**

- AAPL at $180, earnings tomorrow

- Historical moves: Average 3% = $5.40

- Market prices: Expecting 4% = $7.20 move

- **Your analysis:** Will be exactly 3%

**Trade:**

- Butterfly centered at $185.40 (3% up, most likely)

- Width: $5 ($183/$185/$188)

- **Thesis:** Stock will land in $183-$188 range

- **Edge:** Market overpricing move, you have better estimate

**Institutional advantage:**

- Access to better earnings models

- Order flow data (see what big players do)

- **Butterflies express precise view**

**3. Index arbitrage and dispersion:**

**Advanced index trading:**

- Trade volatility differential between index and components

- **Index butterflies vs. single-stock butterflies**

**Example:**

- SPX realized vol: 15%

- Average component vol: 22%

- **Correlation drops during stress** (dispersion increases)

**Strategy:**

- Sell SPX butterfly (bet on low vol)

- Buy component butterflies (protection if dispersion increases)

- **Profit from vol differential**

**Why institutions do this:**

- Diversification benefit

- Correlation breakdowns = profit

- Hedged exposure

**4. Calendar spread management:**

**Professional vol term structure trading:**

- Butterflies isolate specific expiration

- Trade time decay differentials

**Example:**

- Front-month butterfly (30 DTE): High theta

- Back-month butterfly (60 DTE): Lower theta

- **Ratio trade:** Long front-month, short back-month

- **Profit from:** Theta differential if stock stable

### 4. The Volatility Smile and Butterfly Pricing

**Key insight:** Butterfly pricing depends heavily on volatility skew.

**In equity markets (put skew):**

$$
\text{IV}_{OTM\;Put} > \text{IV}_{ATM} > \text{IV}_{OTM\;Call}
$$

**Impact on call butterfly pricing:**

- Lower strike (ITM call): Higher IV → More expensive

- Middle strike (ATM): Highest IV → Most expensive

- Upper strike (OTM call): Lower IV → Cheapest

**Net effect on call butterfly:**

$$
\text{Cost} = \underbrace{\text{Buy ITM}}\_{\text{Expensive}} - \underbrace{2 \times \text{Sell ATM}}\_{\text{Most Exp}} + \underbrace{\text{Buy OTM}}\_{\text{Cheap}}
$$

**Result:** ATM being most expensive **reduces butterfly cost** (selling richest IV)

**Put butterfly (opposite):**

- Lower OTM put: Highest IV (expensive)

- Middle ATM put: Medium IV

- Upper ITM put: Lower IV

**Cost:** Higher than call butterfly (buying expensive OTM put, selling cheaper ATM)

**Put-call parity reconciliation:**

- Call and put butterflies SHOULD cost same (arbitrage-free)

- Small differences = **arbitrage opportunity** for professionals

- Retail traders: Just use cheaper structure

### 5. The Behavioral Finance Angle

**Why butterflies offer edge:**

**1. Volatility overestimation:**

- Humans overestimate likelihood of big moves

- Buy expensive straddles (expecting excitement)

- **Reality:** Most days are boring

- **Butterflies profit from boring**

**2. Recency bias:**

- After big move: Everyone expects more volatility

- IV spikes (options expensive)

- **Best time for butterflies:** Sell inflated ATM IV

- Market calms down → butterfly profits

**3. Probability illusion:**

- Narrow profit zone makes butterflies look "low probability"

- **Truth:** Probability depends on volatility regime

- In low-vol environment: 40-50% probability (decent!)

- In high-vol environment: 20-30% probability (poor)

**Professional edge:** Know WHEN butterflies have genuine edge (post-spike, in mean-reversion regimes).

### 6. The Mathematics of Butterfly Economics

**Break-even probability calculation:**

For butterfly to be profitable on average:

$$
P(\text{Win}) \times \text{Max Profit} > P(\text{Loss}) \times \text{Avg Loss}
$$

**Example:**

- Debit: $2.50

- Max profit: $2.50

- Max loss: $2.50

- **Need:** > 50% probability of landing in profit zone

**How to estimate probability:**

- Use realized volatility to model distribution

- Check if profit zone falls within 1 standard deviation

- **If yes:** Good probability (> 50%)

- **If no:** Poor probability (< 30%)

**Real calculation:**

- Stock at $100, 30 DTE

- Historical vol: 20% annually = 1.15% daily

- 30-day move: 1.15% × √30 = 6.3%

- **1 std dev range:** $94-$106

**Butterfly strikes:** $95/$100/$105

- **Profit zone:** $97.50-$102.50

- **Coverage:** Covers center 50% of distribution

- **Estimated probability:** ~40-45%

**Trade-off analysis:**

- Cost $2.50, max profit $2.50 → 1:1 risk/reward

- Probability ~42%

- **Expected value:** 0.42 × $2.50 - 0.58 × $2.50 = $1.05 - $1.45 = **-$0.40** (negative edge!)

**Conclusion:** This butterfly is NOT a good trade (negative EV).

**Better butterfly:**

- Cost $2.00, max profit $3.00

- Same probability ~42%

- **Expected value:** 0.42 × $3.00 - 0.58 × $2.00 = $1.26 - $1.16 = **+$0.10** (positive edge!)

### 7. Understanding the Economic Foundations

**Key insights from butterflies:**

**1. Volatility is mispriced predictably:**

- Post-shock: IV too high (sell butterflies)

- During grind: IV too low (buy straddles, not butterflies)

- **Edge exists in timing entry**

**2. Precision matters:**

- "Stock will stay stable" = too vague

- "Stock will be $100 ± $2.50 in 30 days" = precise

- **Butterflies reward precision**

**3. Cost structure is everything:**

- Cheap butterfly ($1.50 cost, $3.50 profit potential) = good

- Expensive butterfly ($3.50 cost, $1.50 profit potential) = terrible

- **Must model fair value before entering**

**4. Theta decay is non-linear:**

- First 50% of time: 30% of total decay

- Last 50% of time: 70% of total decay

- **Butterflies benefit from holding closer to expiration**

- But gamma risk increases!

**5. Butterflies are NOT neutral:**

- "Neutral strategy" is misnomer

- **Really:** "Low volatility strategy"

- If realized vol > implied vol → Lose money

- If realized vol < implied vol → Make money

**The economic truth:**

- Butterflies don't create "free money"

- They **express specific view:** Low volatility + precise price target

- **Edge comes from:** Being right about volatility AND price more often than market expects

- **Success requires:** Entering when IV overpriced + stock in consolidation regime

Understanding economic foundations helps you recognize:

- When butterflies offer genuine edge (post-IV spike, consolidation patterns)

- When to avoid (low IV environment, trending markets)

- How to calculate fair value (probability × payoff analysis)

- Why timing entry around volatility cycles is crucial


### 8. Long Call Butterfly (Most Common)

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

<img src="https://github.com/SungchulLee/img/blob/main/long_call_butterfly_pnl.png?raw=true" alt="long_call_butterfly_pnl" width="700">

**Figure 1:** Long call butterfly profit/loss diagram showing the characteristic peaked payoff structure with maximum profit at the middle strike ($100) and limited losses at the wing strikes, illustrating how the position profits from pinpoint price stability.

### 9. Long Put Butterfly

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

### 10. Iron Butterfly

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

### 11. Broken Wing Butterfly

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

### 12. Reverse (Short) Butterfly

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

<img src="https://github.com/SungchulLee/img/blob/main/butterfly_types_comparison.png?raw=true" alt="butterfly_types_comparison" width="700">

**Figure 2:** Comprehensive comparison of different butterfly types including long call butterfly, long put butterfly, iron butterfly, broken wing butterfly, and reverse butterfly, showing how each structure creates distinct profit/loss profiles while maintaining the core butterfly shape.

---

## Concrete Example

**Complete walkthrough:**

### 1. Setup

- **Stock:** SPY at $450

- **View:** Market will stay around $450 for next month (consolidation)

- **Volatility:** Moderate (VIX at 18)

- **Strategy:** 30-day call butterfly

**Available options:**

| Strike | Call Premium | Put Premium |
|--------|--------------|-------------|
| $445 | $7.50 | $2.50 |
| $450 | $4.50 | $4.50 |
| $455 | $2.50 | $7.50 |

### 2. The Trade

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

### 3. The Math

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

### 4. 1

**At expiration:**

- SPY exactly at $450

- Butterfly worth $4.00

- Entry: $1.00

- **Profit: $300 (300% return!)**

**Why it worked:** Stock pinned exactly at middle strike (rare but beautiful)

### 5. 2

**At expiration:**

- SPY at $448

- $445 call worth: $3

- $450 calls: $0

- Net value: $3

- Entry: $1

- **Profit: $200 (200% return)**

**Still profitable:** Within the profit zone

### 6. 3

**At expiration:**

- SPY at $460 (big move up)

- All options ITM, spreads cancel

- Net value: $0

- Entry: $1

- **Loss: $100 (100% loss)**

**Wrong:** Stock moved too much

### 7. 4

**At expiration:**

- SPY at $440 (moved down)

- All calls worthless

- Net value: $0

- Entry: $1

- **Loss: $100 (100% loss)**

**Wrong:** Stock moved too much (other direction)

### 8. 5

**After 15 days:**

- SPY still at $450

- But VIX spikes to 25 (vol up)

- Butterfly loses value (vega negative)

- Now worth: $0.60

- Entry: $1.00

- **Loss: $40 if exit now**

**Decision:** Either exit for small loss, or hold hoping for vol crush

<img src="https://github.com/SungchulLee/img/blob/main/spy_butterfly_scenarios.png?raw=true" alt="spy_butterfly_scenarios" width="700">

**Figure 3:** SPY butterfly trade scenarios showing P&L outcomes across different stock prices at expiration, illustrating the five key scenarios from max profit (stock at $450) to max loss (stock outside wings), with breakeven points clearly marked.

---

## Butterfly Mechanics

### 1. Strike Spacing

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

<img src="https://github.com/SungchulLee/img/blob/main/strike_width_comparison.png?raw=true" alt="strike_width_comparison" width="700">

**Figure 4:** Strike width comparison showing how narrow spreads (tighter spacing) versus wide spreads (wider spacing) affect the cost, probability of profit, and ROI potential of butterfly positions, illustrating the fundamental trade-off between capital efficiency and success probability.

### 2. The Greeks

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

<img src="https://github.com/SungchulLee/img/blob/main/butterfly_greeks_profile.png?raw=true" alt="butterfly_greeks_profile" width="700">

**Figure 5:** Butterfly Greeks profile showing the characteristic behavior of delta (near zero at center), gamma (positive at body, negative at wings), theta (positive throughout), and vega (negative), demonstrating why butterflies profit from stability and time decay while being hurt by volatility increases.

---

## Iron Butterfly Example

**The credit version:**

### 1. Setup

- **Stock:** AAPL at $180

- **Strategy:** 45-day iron butterfly

### 2. The Trade

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

### 3. Payoff Analysis

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

### 4. Iron Butterfly vs. Iron Condor

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

### 1. Favorable Conditions

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

<img src="https://github.com/SungchulLee/img/blob/main/iv_impact_butterfly.png?raw=true" alt="iv_impact_butterfly" width="700">

**Figure 6:** Implied volatility impact on butterfly pricing and profitability, showing how high IV environments make butterflies expensive to enter while IV crush post-event creates ideal entry opportunities, illustrating the critical importance of timing butterfly trades around volatility cycles.

### 2. Unfavorable Conditions

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

<img src="https://github.com/SungchulLee/img/blob/main/profit_probability.png?raw=true" alt="profit_probability" width="700">

**Figure 7:** Profit probability distribution for butterfly spreads showing the relationship between strike positioning, profit zone width, and win rate, illustrating why tighter butterflies have lower probability of profit (10-20%) but higher ROI when successful, while wider butterflies offer higher probability but lower percentage returns.

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

<img src="https://github.com/SungchulLee/img/blob/main/butterfly_vs_straddle.png?raw=true" alt="butterfly_vs_straddle" width="700">

**Figure 8:** Butterfly versus straddle profit/loss comparison showing the fundamental opposition: butterflies profit from stability with positive theta and negative vega, while straddles profit from volatility with negative theta and positive vega, illustrating how these strategies represent opposite market views.

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

<img src="https://github.com/SungchulLee/img/blob/main/broken_wing_butterfly.png?raw=true" alt="broken_wing_butterfly" width="700">

**Figure 9:** Broken wing butterfly structure showing unequal strike spacing that creates directional bias, allowing traders to collect credit or reduce debit while maintaining defined risk, illustrating how asymmetric butterflies can be tailored for specific risk-reward preferences and market outlooks.

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


---

## Practical Guidance

**Step-by-step butterfly implementation:**

### 1. Critical Pre-Trade Checklist

☐ **Consolidation confirmed?** (3+ days range-bound)  
☐ **IV 45-70th percentile?** (Sweet spot)  
☐ **No events within expiration?** (Earnings, Fed, etc.)  
☐ **30-45 DTE?** (Optimal theta/gamma balance)  
☐ **Liquid strikes?** (OI > 1,000, spread < $0.20 per leg)  
☐ **Cost < 60% of width?** ($2.50 cost on $5-wide = 50%, good)  
☐ **Technical support/resistance?** (Wings align with key levels)

### 2. Step 1

**Only enter butterflies when:**

- IV 50-70th percentile (elevated, will compress)

- Stock consolidating (not trending)

- **After volatility event** (IV declining)

**Avoid when:**

- IV < 45th (too cheap, no edge)

- IV > 75th (expansion risk)

- Stock trending strongly

### 3. Step 2

**Center strike:** At current price or expected target  
**Wing width:** $5-$10 for stocks, $5-$25 for indices  
**Target cost:** 40-60% of wing width

**Example:**

- Stock at $180

- Butterfly: $175/$180/$185 ($5-wide)

- **Good cost:** $2.00-3.00 (40-60%)

- **Bad cost:** $3.50+ (70%+, too expensive)

### 4. Step 3

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times 2\%}{\text{Debit} \times 100}
$$

**Example:** $50k account, $2.50 debit  
**Max:** $1,000 / $250 = **4 contracts**

### 5. Step 4

1. **Multi-leg order** (all 3-4 legs simultaneously)

2. **Limit at mid or better**

3. **Check slippage:** Total spread < 20% of debit

4. **Set alerts:** Breakevens, 50% profit, 80% loss

### 6. Step 5

**Profit targets:**

- **Primary:** +40-50% of max profit

- **Time:** 70% time elapsed if +30% profit

**Stop losses:**

- **Primary:** -80% of max loss

- **Wing breach:** Stock breaks wing by 3%+, exit

**Time stops:**

- **Always exit by 7 DTE**

- Exit by 14 DTE if not profitable

### 7. Step 6

**Generally:** Close butterflies rather than adjust

**Only adjust if:**

- Deeply profitable (+60%+)

- Want to lock gains

- Convert to safer structure

**Techniques:**

- Close threatened wing

- Roll center strikes

- **Usually better:** Take profit, re-enter fresh

### 8. Step 7

| Date | Center | Width | Cost | DTE | IV% | Exit | P&L | Win? |
|------|--------|-------|------|-----|-----|------|-----|------|
| 1/15 | $180 | $5 | $2.50 | 45 | 58% | D30 | +$1.20 | ✓ |

**Target metrics:**

- Win rate: 60-65%

- Avg win: +45% of max

- Avg loss: -85% of max

- **Expectancy:** +$0.30-0.50 per trade

### 9. The Butterfly Trading Rules

**Never trade when:**

1. No consolidation pattern

2. Events within expiration

3. IV extremes (< 40th or > 75th)

4. Trending market

5. < 21 DTE or > 60 DTE

6. Cost > 65% of width

**Always:**

1. Enter post-volatility spike

2. Exit at 50% profit target

3. Exit by 7 DTE

4. Size for 2% risk

5. Check probability before entry

**Success formula:** 60%+ win rate requires excellent entry timing (IV + consolidation + no events).


## Common Mistakes

### 1. Mistake 1

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

### 2. Mistake 2

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

### 3. Mistake 3

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

### 4. Mistake 4

❌ **Wrong:**

- Too long (60+ days): expensive, theta slow

- Too short (< 1 week): gamma risk, hard to manage

✅ **Better:**

- 30-45 days ideal

- Balance theta and gamma

- Enough time to work

### 5. Mistake 5

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

### 1. Taking Profits

**Guidelines:**

**At 50% of max profit:**

- Target achieved

- Take profit and redeploy

- Don't be greedy

<img src="https://github.com/SungchulLee/img/blob/main/time_decay_butterfly.png?raw=true" alt="time_decay_butterfly" width="700">

**Figure 10:** Time decay evolution of butterfly spread value showing how positive theta works over time, with value appreciation accelerating as expiration approaches (assuming stock stays near the target strike), illustrating optimal entry timing and profit-taking windows for maximum theta capture.

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

### 2. Managing Losers

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

### 3. Rolling

**If stock drifts slightly:**

- Can roll butterfly to follow

- Close current, open new centered at new price

- Costs commissions and spread

**Example:**

- Butterfly at $100, stock now $103

- Roll to $103-centered butterfly

- Continue the trade

---


---


