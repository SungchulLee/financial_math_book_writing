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


---

## Economic Interpretation: Advanced Perspectives

**Understanding what butterfly spreads REALLY represent economically:**

### The Core Economic Trade-Off

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

### Why This Structure Exists Economically

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

### Professional Institutional Perspective

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

### The Volatility Smile and Butterfly Pricing

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

### The Behavioral Finance Angle

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

### The Mathematics of Butterfly Economics

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

### Understanding the Economic Foundations

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

<img src="https://github.com/SungchulLee/img/blob/main/long_call_butterfly_pnl.png?raw=true" alt="long_call_butterfly_pnl" width="700">

**Figure 1:** Long call butterfly profit/loss diagram showing the characteristic peaked payoff structure with maximum profit at the middle strike ($100) and limited losses at the wing strikes, illustrating how the position profits from pinpoint price stability.

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

<img src="https://github.com/SungchulLee/img/blob/main/butterfly_types_comparison.png?raw=true" alt="butterfly_types_comparison" width="700">

**Figure 2:** Comprehensive comparison of different butterfly types including long call butterfly, long put butterfly, iron butterfly, broken wing butterfly, and reverse butterfly, showing how each structure creates distinct profit/loss profiles while maintaining the core butterfly shape.

---

## Concrete Example: Long Call Butterfly Trade

**Complete walkthrough:**

### Setup

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

<img src="https://github.com/SungchulLee/img/blob/main/spy_butterfly_scenarios.png?raw=true" alt="spy_butterfly_scenarios" width="700">

**Figure 3:** SPY butterfly trade scenarios showing P&L outcomes across different stock prices at expiration, illustrating the five key scenarios from max profit (stock at $450) to max loss (stock outside wings), with breakeven points clearly marked.

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

<img src="https://github.com/SungchulLee/img/blob/main/strike_width_comparison.png?raw=true" alt="strike_width_comparison" width="700">

**Figure 4:** Strike width comparison showing how narrow spreads (tighter spacing) versus wide spreads (wider spacing) affect the cost, probability of profit, and ROI potential of butterfly positions, illustrating the fundamental trade-off between capital efficiency and success probability.

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

<img src="https://github.com/SungchulLee/img/blob/main/butterfly_greeks_profile.png?raw=true" alt="butterfly_greeks_profile" width="700">

**Figure 5:** Butterfly Greeks profile showing the characteristic behavior of delta (near zero at center), gamma (positive at body, negative at wings), theta (positive throughout), and vega (negative), demonstrating why butterflies profit from stability and time decay while being hurt by volatility increases.

---

## Iron Butterfly Example

**The credit version:**

### Setup

- **Stock:** AAPL at $180

- **Strategy:** 45-day iron butterfly

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

<img src="https://github.com/SungchulLee/img/blob/main/iv_impact_butterfly.png?raw=true" alt="iv_impact_butterfly" width="700">

**Figure 6:** Implied volatility impact on butterfly pricing and profitability, showing how high IV environments make butterflies expensive to enter while IV crush post-event creates ideal entry opportunities, illustrating the critical importance of timing butterfly trades around volatility cycles.

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

### Critical Pre-Trade Checklist

☐ **Consolidation confirmed?** (3+ days range-bound)  
☐ **IV 45-70th percentile?** (Sweet spot)  
☐ **No events within expiration?** (Earnings, Fed, etc.)  
☐ **30-45 DTE?** (Optimal theta/gamma balance)  
☐ **Liquid strikes?** (OI > 1,000, spread < $0.20 per leg)  
☐ **Cost < 60% of width?** ($2.50 cost on $5-wide = 50%, good)  
☐ **Technical support/resistance?** (Wings align with key levels)

### Step 1: IV Environment Check

**Only enter butterflies when:**

- IV 50-70th percentile (elevated, will compress)

- Stock consolidating (not trending)

- **After volatility event** (IV declining)

**Avoid when:**

- IV < 45th (too cheap, no edge)

- IV > 75th (expansion risk)

- Stock trending strongly

### Step 2: Strike Selection

**Center strike:** At current price or expected target  
**Wing width:** $5-$10 for stocks, $5-$25 for indices  
**Target cost:** 40-60% of wing width

**Example:**

- Stock at $180

- Butterfly: $175/$180/$185 ($5-wide)

- **Good cost:** $2.00-3.00 (40-60%)

- **Bad cost:** $3.50+ (70%+, too expensive)

### Step 3: Position Sizing

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times 2\%}{\text{Debit} \times 100}
$$

**Example:** $50k account, $2.50 debit  
**Max:** $1,000 / $250 = **4 contracts**

### Step 4: Entry Execution

1. **Multi-leg order** (all 3-4 legs simultaneously)

2. **Limit at mid or better**

3. **Check slippage:** Total spread < 20% of debit

4. **Set alerts:** Breakevens, 50% profit, 80% loss

### Step 5: Exit Rules

**Profit targets:**

- **Primary:** +40-50% of max profit

- **Time:** 70% time elapsed if +30% profit

**Stop losses:**

- **Primary:** -80% of max loss

- **Wing breach:** Stock breaks wing by 3%+, exit

**Time stops:**

- **Always exit by 7 DTE**

- Exit by 14 DTE if not profitable

### Step 6: Adjustments (Rare)

**Generally:** Close butterflies rather than adjust

**Only adjust if:**

- Deeply profitable (+60%+)

- Want to lock gains

- Convert to safer structure

**Techniques:**

- Close threatened wing

- Roll center strikes

- **Usually better:** Take profit, re-enter fresh

### Step 7: Record Template

| Date | Center | Width | Cost | DTE | IV% | Exit | P&L | Win? |
|------|--------|-------|------|-----|-----|------|-----|------|
| 1/15 | $180 | $5 | $2.50 | 45 | 58% | D30 | +$1.20 | ✓ |

**Target metrics:**

- Win rate: 60-65%

- Avg win: +45% of max

- Avg loss: -85% of max

- **Expectancy:** +$0.30-0.50 per trade

### The Butterfly Trading Rules

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


---

## Worst Case Scenario

**What happens when stability fails:**

### The Nightmare Setup: The "Sure Thing" That Moved

**How it starts (The High-Conviction Trade):**

You enter a long call butterfly on AAPL:

- AAPL at $180 (consolidating for 3 weeks)

- Technical setup: Strong support at $175, resistance at $185

- Thesis: "Stock will stay range-bound, earnings not for 2 months"

- **Structure:** Long call butterfly $175/$180/$185

  - Buy $175 call: -$8.00

  - Sell 2× $180 calls: +$10.00 each = +$20.00

  - Buy $185 call: -$2.50

  - **Net debit: $2.50** ($250 per contract)

- Max profit: $2.50 (if AAPL exactly at $180)

- Max loss: $2.50 (if AAPL outside $175-$185)

- **Probability (estimated):** 55% (stock stays in range)

You trade 20 contracts (feels safe, "only $5k risk").

**But then reality strikes:**

**Day 1 - 10:00 AM (The Surprise):**

- Apple announces surprise product delay

- Stock gaps down: $180 → $170 (-5.6%)

- **Instantly outside your butterfly tent**

- IV spikes: 25% → 35%

**Your position immediately:**

- Below $175 (lower wing): All calls OTM or near-zero

- **Current loss:** Approaching -$2.50 per spread (max loss)

- **20 contracts:** -$2.50 × 20 × 100 = **-$5,000 loss**

- Account: $50,000 → $45,000 (-10%)

**Your emotional response:** "It's just $5k, might bounce back"

**The deterioration:**

**Day 1 - 2:00 PM (False Hope):**

- AAPL bounces to $173 (bargain hunters)

- Position improves slightly: -$4,200

- **You decide:** "I'll hold - still 42 DTE, can recover"

**Day 2-7 (The Grind Lower):**

- More analysts downgrade

- AAPL drifts: $173 → $169 → $167

- **Deep outside tent**

- Position: -$4,800 (96% of max loss)

- Theta decay: Minimal (already near max loss)

**Week 2 (Decision Point):**

- AAPL at $165 (now -8.3% from entry)

- Position: Full max loss -$5,000

- **Critical decision:** Exit for -$5,000 OR hold hoping for bounce?

- **You hold:** "Earnings in 6 weeks, might bounce then"

**Week 3-4 (The Realization):**

- AAPL stays $163-$168

- No bounce materializes

- **Theta becomes enemy:** Time decay actually hurts now

  - Short $180 calls worthless (no more decay)

  - Long $175/$185 calls losing tiny remaining value

- Position: -$5,000 (locked in)

**Week 5 (New Hope):**

- AAPL bounces to $174!

- Back inside tent (barely)

- Position improves: -$2,800

- **You think:** "See! I was right to hold!"

- **Mistake:** Should close here, take -56% loss

**Week 6 (Second Collapse):**

- Supply chain issues announced

- AAPL → $168

- **Back to max loss:** -$5,000

- Only 7 DTE left

**Expiration:**

- AAPL settles at $166

- All calls expire worthless (below $175)

- **Final loss:** -$5,000 (full max loss, 10% of account)

**But the real damage comes next...**

### Maximum Loss Calculation

**Worst case mathematics:**

For long butterflies, max loss is simple:

$$
\text{Max Loss} = \text{Debit Paid}
$$

**Example (our trade):**

- Debit paid: $2.50 per spread

- **Max loss:** $2.50 per spread (100% of debit)

**With 20 contracts:**
$$
\text{Total Max Loss} = \$2.50 \times 100 \times 20 = \$5,000
$$

**For iron butterflies (credit structures):**

$$
\text{Max Loss} = \text{Wing Width} - \text{Credit Received}
$$

**Example:**

- Wing width: $5 (strikes $5 apart)

- Credit received: $2.50

- **Max loss:** $5 - $2.50 = **$2.50** (same as long butterfly!)

**Impact on portfolio:**

- Started: $50,000

- After butterfly disaster: $45,000 (-10%)

- **Recovery needed:** +11.1% just to break even

**The deceptive "small risk":**

- $2.50 seems small per spread

- **But:** 20 contracts = $5,000 total

- One trade = 10% of account (NOT small!)

### What Goes Wrong: Multiple Failure Modes

The worst case for butterflies occurs when:

**1. Move outside tent (most common):**

- **Single biggest risk:** Stock moves beyond wings

- Even 5-7% move = max loss

- **Probability:** Higher than expected (40-50% for OTM butterflies)

**2. Fast violent move (brutal):**

- **Before theta can help:** Stock gaps outside tent

- Day 1: Max loss locked in

- **Can't exit:** Already near max loss, minimal value to salvage

**3. Whipsaw (soul-crushing):**

- Week 1: Stock drops below tent (-$5,000)

- You hold, hoping for recovery

- Week 3: Stock rallies above tent! (-$5,000 again)

- **Lost on BOTH sides sequentially**

**Example:**

- Enter at $180, tent $175-$185

- Week 2: Stock drops to $170 (max loss -$5,000)

- Week 4: Stock rallies to $190 (still max loss -$5,000)

- **Total:** -$5,000 (lost once, no recovery possible)

**4. IV collapse (underestimated risk):**

- Enter butterfly when IV high

- Stock stays in tent (good!)

- But IV collapses (vega negative)

- **Both happen:** Stock stable + IV drops

- Position should profit (stable stock)

- **Reality:** Vega loss offsets theta gain

**Example:**

- Enter with IV at 35% (high)

- Stock stable at $180 (perfect!)

- IV drops to 22% (-13 points)

- **Vega loss:** -$0.80 × 20 = -$1,600

- **Theta gain:** +$1,200

- **Net:** -$400 (should be winning!)

**5. Expiration pin risk (weekend surprise):**

- **Friday close:** Stock at $180.05 (perfect!)

- Should be max profit

- **But:** Uncertain exercise on short $180 calls

- Some assigned, some not (random)

- **Monday:** Find out you're long/short unexpected shares

- Stock gaps down to $177

- **Extra loss:** $300-500 from assignment confusion

### The Cascade Effect: Butterfly Death Spiral

**Month 1: First "high probability" butterfly**

- $2.50 debit × 20 contracts

- Stock moves outside tent

- **Loss:** -$5,000 (10% of account)

- Account: $50,000 → $45,000

- **Emotional state:** Frustration

**Month 2: "Can't be wrong twice"**

- Double size (40 contracts) to recover

- "65% probability this time!"

- Stock moves outside tent again

- **Loss:** -$10,000 (40 contracts)

- Account: $45,000 → $35,000 (-30% cumulative)

- **Emotional state:** Desperation

**Month 3: "All-in recovery"**

- Triple original size (60 contracts)

- "Market maker's favorite strategy, can't lose!"

- Stock whipsaws through tent

- **Loss:** -$15,000

- Account: $35,000 → $20,000 (-60% cumulative)

- **Emotional state:** Capitulation

**Total damage:**

- Started: $50,000

- After 3 butterflies: $20,000

- **Need +150% to recover** (nearly impossible)

- **Time wasted:** 3 months of losses

### Assignment and Pin Risk

**The expiration day surprise:**

**Friday 4:00pm: Stock at $180.02**

- Your structure: Long $175 call, short 2× $180 calls, long $185 call

- **Short $180 calls:** $0.02 ITM (barely!)

- What you think: "Tiny ITM, probably not exercised"

**What actually happens:**

**Friday after-hours:**

- Stock drifts to $179.98 (2 cents below $180)

- OCC settlement process

- **Random assignment:** Some short calls exercised, some not

**Scenarios:**

**Scenario A: Both short calls assigned**

- You're short 200 shares at $180

- Also have long $175 call, long $185 call

- **Monday open:** Stock at $177

- Short shares losing: 200 × ($180 - $177) = **-$600 unexpected**

**Scenario B: One short call assigned, one not**

- Short 100 shares at $180

- Still short 1× $180 call, plus longs

- **Asymmetric exposure:** Delta confusion

- Monday stock at $183: **-$300 on shares, but short call losing too**

**Scenario C: Neither assigned (lucky)**

- All options expire

- You keep whatever tiny profit/loss

- **This is what you wanted**

**The problem:** You don't know until Saturday/Sunday which scenario occurred!

**Monday morning surprise:**

- Check account: Surprise! You're short 100 shares

- Stock gapped to $177

- **Immediate loss:** $300 unplanned

- Plus commissions to close

- **Total:** $350-400 extra loss vs. expected

### Real Examples of Disasters

**Historical Example 1: Post-Earnings "Stability"**

**Setup:**

- Trader: "TSLA always consolidates after earnings"

- TSLA at $250 (day after earnings)

- Thought: "Will stay $245-$255 next 30 days"

- **Butterfly:** $245/$250/$255, cost $2.00

- 50 contracts

**Week 1-2:**

- Elon tweets product delay

- TSLA drops: $250 → $225 (-10%)

- **Max loss hit:** -$2.00 × 50 × 100 = **-$10,000**

**Week 3-4:**

- "Will recover" (doesn't)

- Stays $220-$230

- **Max loss locked in**

**Expiration:**

- TSLA at $228

- All calls expire worthless

- **Final loss:** -$10,000 (20% of $50k account)

**Lesson:** "Post-earnings consolidation" is NOT guaranteed. Butterflies need stability, not hope.

**Historical Example 2: Fed Decision "Certainty"**

**Setup:**

- Fed meeting tomorrow

- SPY at $450

- Consensus: "No rate change, market won't move"

- **Trade:** Iron butterfly $445/$450/$455

  - Collected $2.50 credit

  - Max risk: $2.50

  - 30 contracts

**Fed decision:**

- Surprise hawkish statement

- SPY drops: $450 → $435 (-3.3%)

- **Below lower wing:** Max loss

- **Loss:** -$2.50 × 30 × 100 = **-$7,500**

**Lesson:** "Certainty" about binary events is dangerous. Butterflies should avoid event risk entirely.

### Psychology of Losses

**Emotional stages (butterfly specific):**

**1. Overconfidence: "High probability!"**

- See 55-60% win probability

- Think: "More likely to win than lose"

- **Miss:** 40-45% loss probability × 100% loss = significant risk

**2. Denial: "Just needs small bounce"**

- Stock outside tent at $172

- "Only needs $3 bounce to reduce loss"

- **Reality:** Momentum continues down, no bounce

**3. Hope: "Time decay will help"**

- 35 DTE remaining

- "Theta will reduce loss"

- **Truth:** At max loss, theta is minimal (options near zero value)

**4. Revenge sizing: "I'll recover with bigger position"**

- Lost $5k on 20 contracts

- Next trade: 40 contracts

- **Result:** -$10k on second loser

**5. Paralysis: "Can't close at max loss"**

- Position at -$4,800 (96% of max)

- "Not worth closing, might bounce"

- **Hold to expiration:** Still -$5,000 (should have closed, saved $200)

**Winning trader mindset:**

- **Accept:** Max loss will happen 40-50% of time

- **Exit early:** At -80% of max loss, not worth holding

- **Size appropriately:** Max loss = 2-3% of account (not 10%!)

- **Don't revenge trade:** One loss is data, not personal attack

### Preventing Worst Case

**Risk management strategies:**

**1. Position sizing (CRITICAL for butterflies):**

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times 2\%}{\text{Debit} \times 100}
$$

**Example:**

- Portfolio: $50,000

- Debit: $2.50 ($250 per spread)

- **Max contracts:** $50,000 × 0.02 / $250 = **4 contracts**

**NOT 20, NOT 50 - Just 4 contracts!**

Why 2% (not 5%)?

- Butterflies have 40-50% loss probability (high!)

- Need survive 3-5 sequential losses

- 2% × 5 losses = 10% drawdown (recoverable)

**2. Probability verification BEFORE entry:**

**Use implied volatility to calculate range:**

- Stock at $180, 30 DTE

- IV: 25% annually = 1.44% daily

- 30-day expected move: 1.44% × √30 = **7.9%**

- **1 standard deviation range:** $166-$194

**Your butterfly:** $175/$180/$185

- **Profit zone:** $177.50-$182.50

- **Coverage:** Center ~30% of distribution

- **Estimated probability:** ~30-35% (NOT 55%!)

**Decision:** Don't trade! Probability too low for 1:1 risk/reward.

**Better butterfly:**

- Wait for IV to spike to 35%

- Same strikes, now profit zone covers 40-45% of distribution

- **Entry criteria met**

**3. Stop losses (mandatory for butterflies):**

**Exit triggers:**

- **-80% of max loss:** Exit immediately

  - Example: Max loss $2.50, exit at -$2.00

- **Stock breaks wing by 2%:** Exit same day

  - Example: Lower wing $175, if stock drops to $171.50, exit

- **50% time passed, down >50%:** Exit

  - Example: 30 DTE, at 15 DTE, if down $1.30+, exit

**Why 80% not 50%?**

- Butterflies have narrow profit zone

- By time you're down 50%, usually at/near max loss already

- Save transaction costs by waiting for 80%

**4. Avoid event risk (non-negotiable):**

**Never hold butterflies through:**

- Earnings (even if 30 days away!)

- Fed decisions

- FDA approvals

- Political elections

- Major product launches

- **Any binary event**

**Why so strict?**

- Butterflies profit from stability

- Events = volatility

- **One event can wipe out 10 winning trades**

**5. IV environment screening:**

**Only trade butterflies when:**

- IV > 45th percentile (elevated, room to fall)

- IV < 75th percentile (not extreme)

- **Sweet spot:** 50-65th percentile

**Avoid when:**

- IV < 40th percentile (too cheap, no edge)

- IV > 75th percentile (expansion risk)

### The Ultimate Protection

$$
\text{Survivability} = \frac{\text{Capital Remaining}}{\text{Capital Initial}} > 0.92
$$

**The harsh reality:**

- Butterflies are NOT "safe" because defined risk

- **40-50% of trades will hit max loss**

- **Math:** Need 60%+ win rate to be profitable long-term

- **Achieving 60%:** Requires excellent entry timing + IV selection

**Expected value example:**

- Win rate: 50% (bad)

- Max profit: $2.50

- Max loss: $2.50

- **Expected value:** 0.50 × $2.50 - 0.50 × $2.50 = **$0** (breakeven at best!)

**Need this:**

- Win rate: 62% (good)

- Max profit: $2.50

- Max loss: $2.50

- **Expected value:** 0.62 × $2.50 - 0.38 × $2.50 = **+$0.60 per trade**

**How to achieve 62% win rate:**

1. Enter only when IV elevated (50-70th percentile)

2. Stock in consolidation (not trending)

3. No events within expiration

4. Technical support/resistance define wings

5. Exit at 50% profit (don't wait for max)

**Position sizing is EVERYTHING:**

- Size for 2% max risk per trade

- Even 5 sequential losses = 10% (recoverable)

- **Survive to compound wins**

**Remember:** Butterfly max loss WILL happen 40-50% of time. This is normal. Size so you can survive the statistical reality of the strategy. Professional butterfly traders size SMALLER than other strategies precisely because of high loss frequency.



---

## Best Case Scenario

**When stability delivers:**

### The Perfect Setup: Post-Volatility Consolidation

**Ideal entry conditions:**

- SPY at $450, post-earnings volatility spike (IV 62nd percentile)

- Market consolidating 3 days (range $448-$452)

- Technical: Strong support $447, resistance $453

- No events for 45 days

**Long call butterfly $445/$450/$455:**

- Buy $445 call: -$8.00

- Sell 2× $450 calls: +$10.50 each = +$21.00

- Buy $455 call: -$2.50

- **Net debit: $2.50** ($250 per contract)

- Max profit: $2.50 (if SPY at $450)

- 10 contracts

**Days 1-15: The Drift**

- SPY: $450 → $451.50 → $449.50 (perfect!)

- Theta: +$18/day × 15 = +$270

- IV compression: 62nd → 48th percentile

- Vega: +$120

- **P&L: +$390** (16% gain)

**Days 16-30: Sweet Spot**

- SPY consolidates $449-$451

- Theta accelerating: +$25/day

- **Cumulative: +$765** (31%)

**Exit Day 30:**

- Target: 50% of max = $1,250

- Close for +$765 (31% of max)

- **ROI: 31% in 30 days**

### Maximum Profit Achievement

$$
\text{Max Profit (Long Butterfly)} = \text{Wing Width} - \text{Debit Paid}
$$

**Our trade:**

- Wing width: $5

- Debit: $2.50

- **Max profit:** $5 - $2.50 = **$2.50 per spread**

- **10 contracts:** $2,500 total (100% ROI)

**If held to expiration at $450 (perfect):**

- All options expire at intrinsic value

- **Profit:** $2.50 × 10 × 100 = $2,500 (100% ROI on $2,500 risk)

### Comparison to Straddle

**Long straddle (same strikes):**

- Buy $450 call + $450 put

- Cost: $11.00

- SPY stays $449-$451: Loss $9+ (lost to decay)

**Our butterfly:**

- Cost: $2.50

- SPY stays $449-$451: Profit +$0.75-2.00

- **Butterfly wins when:** Stock stable (exactly what happened)

### Professional Profit-Taking

Exit at 40-50% of max profit:

- Higher win rate (65% vs 40%)

- Faster capital recycling

- Better annual returns

**Typical outcomes (100 trades):**

- 62 winners: +$1.25 avg = +$77.50

- 38 losers: -$2.00 avg = -$76.00

- **Net: +$1.50 per opportunity**

- **Annual (15 trades): +$22.50 (9% return)**

**Remember:** Best case = consistent 50% profit captures, not max profit home runs.


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

**Master butterflies to trade specific price targets with defined risk!** 