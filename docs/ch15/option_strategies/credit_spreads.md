# Credit Spreads (Bull Put & Bear Call)

**Credit spreads** are defined-risk option strategies where you sell a higher-premium option and buy a lower-premium option at a different strike, collecting net premium upfront. They offer high probability of profit with limited, predefined risk - making them the workhorse strategy for income-focused options traders.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/credit_spread_greeks.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/credit_spreads_bear_call_spread.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/credit_spreads_bull_put_spread.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/credit_spreads_bull_put_vs_bear_call.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/credit_spreads_fifty_percent_rule.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/credit_spreads_strike_selection.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/credit_spreads_theta_decay_curve.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/credit_spreads_time_management.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/iv_impact_credit_spread.png?raw=true" alt="long_call_vs_put" width="700">
</p>

---

## The Core Insight

**The fundamental idea:**

- Markets often trade sideways or trend slowly
- Most options expire worthless (time decay favors sellers)
- But naked selling has unlimited risk
- Spreads cap your risk while letting you sell premium
- You collect premium upfront and profit if stock doesn't move too much
- High probability trades with defined risk/reward

**The key equation:**

$$
\text{Max Profit} = \text{Net Credit Received} \quad (\text{collected upfront})
$$

$$
\text{Max Loss} = \text{Spread Width} - \text{Net Credit} \quad (\text{defined, limited})
$$

**You're essentially betting: "The stock won't move beyond my short strike by expiration, so I keep the premium."**

---

## What Are Credit Spreads?

**Before trading spreads, understand the two main types:**

### Bull Put Spread (Bullish Credit Spread)

**Definition:** Sell a higher-strike put, buy a lower-strike put for protection, collecting net credit.

**Structure:**

- **Sell:** $95 put for $3 (obligation to buy at $95)
- **Buy:** $90 put for $1 (right to sell at $90)
- **Net Credit:** $3 - $1 = $2 = $200 per spread

**The bet:** Stock stays above $95 (short strike) → keep $200

**Max Risk:** ($95 - $90) - $2 = $3 per share = $300 per spread

**Characteristics:**

- Bullish strategy (want stock flat or up)
- Profit if stock stays above short strike
- Defined risk (long put protects downside)
- High probability, small reward
- Best in low IV environments

### Bear Call Spread (Bearish Credit Spread)

**Definition:** Sell a lower-strike call, buy a higher-strike call for protection, collecting net credit.

**Structure:**

- **Sell:** $105 call for $3 (obligation to sell at $105)
- **Buy:** $110 call for $1 (right to buy at $110)
- **Net Credit:** $3 - $1 = $2 = $200 per spread

**The bet:** Stock stays below $105 (short strike) → keep $200

**Max Risk:** ($110 - $105) - $2 = $3 per share = $300 per spread

**Characteristics:**

- Bearish/neutral strategy (want stock flat or down)
- Profit if stock stays below short strike
- Defined risk (long call protects upside)
- High probability, small reward
- Best in low IV environments

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/bull_put_bear_call_spreads.png?raw=true" alt="credit_spreads" width="700">
</p>
**Figure 1:** Profit/loss diagrams for bull put spread (left) and bear call spread (right), showing identical risk/reward profiles but different directional biases. Both have defined maximum profit (credit received) and defined maximum loss (spread width minus credit).

---

## Economic Interpretation: Selling Insurance with a Hedge

**Beyond the basic definition, understanding what credit spreads REALLY are economically:**

### Credit Spreads as Insurance Underwriting

**The deep insight:**

A credit spread is economically equivalent to **selling insurance with automatic reinsurance protection**. When you put on a credit spread, you're essentially:

1. **Selling insurance** (short option collects premium)
2. **Buying reinsurance** (long option caps your loss)
3. **Keeping the premium spread** if nothing bad happens
4. **Limited liability** if disaster strikes

**Formal decomposition:**

$$
\underbrace{\text{Bull Put Spread}}_{\text{Net Credit}} \equiv \underbrace{\text{Short Put}}_{\text{Sell Insurance}} - \underbrace{\text{Long Put}}_{\text{Buy Reinsurance}}
$$

**Why this matters:**

**Traditional naked put selling:**

- Sell $95 put for $3
- Collect $300 premium
- If stock → $50, you lose $4,200 ($95 - $50 - $3)
- **Potential for catastrophic loss**

**Bull put spread (insurance with reinsurance):**

- Sell $95 put for $3
- Buy $90 put for $1
- Collect $200 net
- If stock → $50, you lose only $300 (spread width - credit)
- **Maximum loss: $300 (predefined)**

**The $1 you pay for the $90 put is your "reinsurance premium" - the cost of capping your tail risk.**

### Example: Breaking Down the SPY Bull Put Spread

**Setup:**

- SPY at $450
- Sell $445 put for $4
- Buy $440 put for $2
- Net credit: $2 = $200 per spread

**What you're really doing:**

$$
\begin{align}
\text{Economic Position} &= \text{Sell put insurance at \$445} \\
&+ \text{Buy reinsurance at \$440} \\
&+ \text{Keep \$200 if SPY > \$445 at expiry} \\
&+ \text{Max loss \$300 if SPY < \$440}
\end{align}
$$

**Scenarios:**

| SPY at Expiry | Naked Short Put | Bull Put Spread |
|--------------|----------------|-----------------|
| $460 | Gain: $400 (keep full premium) | Gain: $200 (keep net credit) |
| $445 | Gain: $400 (keep full premium) | Gain: $200 (keep net credit) |
| $442 | Loss: $100 ($3 intrinsic - $4) | Loss: $100 ($3 intrinsic - $2) |
| $440 | Loss: $100 ($5 intrinsic - $4) | Loss: $300 (max loss) |
| $420 | **Loss: $2,100 ($25 intrinsic - $4)** | **Loss: $300 (capped by long put)** |

**This "automatic reinsurance" is the key difference!**

### The Insurance Analogy

**Think like an insurance company:**

**When you sell a credit spread:**

- You're the insurance company
- Premium collected = your revenue
- Short strike = policy deductible
- Spread width = your maximum payout
- Long option = your reinsurance policy

**Insurance companies profit when:**

- Claims (stock moves) are rare
- Premiums (credits) exceed payouts
- Losses are capped by reinsurance

**Same with credit spreads:**

- Most expire worthless (high probability)
- You keep credit most of the time
- Occasional losses are limited by long option

### Credit Spreads vs. Debit Spreads: The Economic Tradeoff

**The fundamental options financing theorem:**

$$
\text{Credit Spread (sell insurance)} \leftrightarrow \text{Debit Spread (buy insurance)}
$$

**Credit spread trader:**

- Collects premium upfront
- High probability of small win
- Occasional large loss (but defined)
- Time decay works FOR you
- Needs high win rate

**Debit spread trader:**

- Pays premium upfront
- Low probability of large win
- Frequent small losses
- Time decay works AGAINST you
- Needs occasional big win

**Neither is "better" - they're inverse positions:**

$$
\text{Bull Put Spread} + \text{Bear Put Spread (same strikes)} = \text{Zero Sum Game}
$$

### Why This Perspective Matters

**Understanding credit spreads as insurance underwriting helps you:**

1. **Think probabilistically:**

   - What's probability stock stays above short strike?
   - Am I being paid enough for the risk?
   - Is my premium/risk ratio attractive?

2. **Understand premium pricing:**

   - Premium = probability × payout + time value
   - Higher IV = higher premiums (better for sellers)
   - Lower IV = lower premiums (better for buyers)

3. **Size positions correctly:**

   - Insurance companies diversify policies
   - You should diversify credit spreads
   - Never risk >5% on single spread

4. **Recognize when to stop selling:**

   - Insurance companies refuse policies in disasters
   - Don't sell credit spreads in high IV spikes
   - Wait for IV to normalize before selling

### The Strategic Advantage of Defined Risk Selling

**Why traders prefer credit spreads over naked selling:**

**Scenario: Neutral on SPY at $450, want to sell premium**

**Option A: Naked Put Selling**
- Sell $445 put for $4
- Collect $400 premium
- Margin requirement: ~$9,000
- **Risk: Stock to $0 = -$44,100 loss**

**Option B: Bull Put Spread**
- Sell $445 put for $4
- Buy $440 put for $2
- Collect $200 net credit
- Margin requirement: $300 (spread width - credit)
- **Risk: Maximum -$300 loss (defined)**

**The spread gives you:**

- 9x lower capital requirement ($300 vs. $9,000)
- Defined, manageable risk
- Sleep-at-night comfort
- **Controlled downside in black swan events**

**This is why credit spreads are called "the thinking trader's premium collection strategy."**

---

## Key Terminology

**Spread Width:**

- Distance between strikes
- $10 wide, $5 wide, $2 wide
- Determines max risk (width - credit)
- Wider = more risk, more credit

**Net Credit:**

- Premium collected after buying protection
- Your max profit
- Received upfront in your account
- Short premium - long premium

**Break-Even Point (BEP):**

- **Bull Put:** Short strike - net credit
- **Bear Call:** Short strike + net credit
- Stock must move beyond BEP for loss

**Probability of Profit (POP):**

- Typically 60-80% for credit spreads
- Based on delta of short strike
- Higher POP = lower credit
- Sweet spot: 65-75% POP

**Win Rate:**

- Percentage of trades that expire worthless
- Credit spreads typically 65-80% win rate
- Need high win rate since profit < risk

**Risk/Reward Ratio:**

- Max risk ÷ max profit
- Typical: 2:1 to 4:1 (risk more than profit)
- Must win frequently to overcome ratio

---

## Why Use Credit Spreads?

**Use cases for bull put and bear call spreads:**

### Bull Put Spread (Bullish/Neutral)

**When to use:**

1. **Moderately bullish:**

   - Stock in uptrend, expect continuation
   - Want to profit from range-bound trading
   - Don't expect huge rally, just no collapse

2. **High IV environment:**

   - Premiums rich from elevated volatility
   - Good credit collection opportunity
   - Sell expensive options before IV contracts

3. **Earnings aftermath:**

   - Stock already moved, IV crushed
   - Sell the high remaining premium
   - Expect stabilization/consolidation

4. **Support levels:**

   - Stock near strong support
   - Technical setup suggests floor
   - Sell puts below support

5. **Income generation:**

   - Want consistent premium collection
   - Accept moderate risk for regular income
   - Building theta-positive portfolio

**Example scenario:**

- AAPL at $180, strong uptrend
- IV at 30% (elevated)
- Resistance at $185, support at $175
- **Action:** Sell $175/$170 bull put spread
- Collect $150 credit, risk $350
- Profit if AAPL stays above $175 (high probability)

### Bear Call Spread (Bearish/Neutral)

**When to use:**

1. **Moderately bearish:**

   - Stock in downtrend, expect continuation
   - Want to profit from capped upside
   - Don't expect crash, just no rally

2. **Resistance overhead:**

   - Stock near major resistance
   - Technical setup suggests ceiling
   - Sell calls above resistance

3. **Post-rally exhaustion:**

   - Stock had big run, looking toppy
   - Momentum fading
   - Expect pullback or consolidation

4. **Elevated IV:**

   - Premiums inflated from fear/uncertainty
   - Good opportunity to sell expensive calls
   - Especially on meme stocks with high IV

5. **Hedging long positions:**

   - Own stock, want to collect premium
   - Bear call spread as partial hedge
   - Reduces cost basis while capping upside

**Example scenario:**

- TSLA at $220, parabolic move to $240
- IV at 70% (very elevated)
- RSI overbought, divergence forming
- **Action:** Sell $250/$255 bear call spread
- Collect $200 credit, risk $300
- Profit if TSLA stays below $250 (likely consolidation)

---

## The Greeks: Understanding Credit Spread Dynamics

**How Greeks affect your position:**

### Delta (Directional Risk)

**Bull Put Spread:**

$$
\Delta_{\text{spread}} = \Delta_{\text{short put}} - \Delta_{\text{long put}} \approx +0.20 \text{ to } +0.40
$$

**What this means:**

- Positive delta (bullish)
- If stock up $1, spread gains ~$0.20-$0.40
- If stock down $1, spread loses ~$0.20-$0.40
- Acts like owning 20-40 shares per spread

**Bear Call Spread:**

$$
\Delta_{\text{spread}} = \Delta_{\text{short call}} - \Delta_{\text{long call}} \approx -0.20 \text{ to } -0.40
$$

**What this means:**

- Negative delta (bearish)
- If stock down $1, spread gains ~$0.20-$0.40
- If stock up $1, spread loses ~$0.20-$0.40
- Acts like shorting 20-40 shares per spread

**Delta evolution:**

- As stock approaches short strike → delta increases (danger zone)
- As stock moves away from short strike → delta decreases (safe zone)

### Theta (Time Decay) - Your Best Friend

**The magic of credit spreads:**

$$
\Theta_{\text{spread}} \approx +0.02 \text{ to } +0.08 \text{ per day}
$$

**What this means:**

- **Positive theta** (time decay helps you!)
- Every day that passes, spread value declines
- Decline in spread value = profit for you
- Maximum theta when stock near short strike

**Theta acceleration:**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/theta_decay_curve.png?raw=true" alt="theta_decay" width="600">
</p>

**Time to expiration vs. theta:**

- 60+ DTE: Slow decay (~$0.02/day)
- 30-45 DTE: Sweet spot (~$0.05/day)
- 15-21 DTE: Accelerating (~$0.08/day)
- <7 DTE: Exponential decay (risky zone)

**The 30-45 DTE sweet spot:**

- Optimal theta/gamma ratio
- Good credit collection
- Time for position management
- Most professional traders sell here

### Gamma (Delta Risk)

**Credit spreads have negative gamma:**

$$
\Gamma_{\text{spread}} = \Gamma_{\text{short}} - \Gamma_{\text{long}} < 0
$$

**What this means:**

- Delta accelerates against you as stock approaches short strike
- Small moves become big moves quickly near expiration
- Maximum gamma risk at short strike
- This is why we manage winners early!

**Gamma evolution:**

| Stock Position | Gamma | Delta Change | What to Do |
|---------------|-------|--------------|------------|
| Far from short strike | Low | Slow | Let theta work |
| Near short strike | Medium | Moderate | Monitor closely |
| At short strike | **High** | **Rapid** | Manage/close |
| Past short strike | Extreme | Explosive | Emergency exit |

**The gamma squeeze:**

- As expiration nears + stock at short strike = gamma explosion
- Delta can go from -0.30 to -0.80 in one day
- This is why we close at 50% profit or roll out

### Vega (Volatility Risk) - Beware the Spike

**Credit spreads have negative vega:**

$$
\text{Vega}_{\text{spread}} \approx -0.15 \text{ to } -0.30
$$

**What this means:**

- IV increase hurts your position
- IV spike of 10% → lose $150-$300 per spread
- IV contraction helps your position
- Best to sell when IV elevated

**IV scenarios:**

**Good entry (high IV):**

- VIX at 25, stock IV at 40%
- Collect $200 credit on $5-wide spread
- IV drops to 30% → spread value drops → you profit

**Bad entry (low IV):**

- VIX at 12, stock IV at 20%
- Collect $80 credit on $5-wide spread
- IV spikes to 35% → spread value rises → you lose

**The vega trap:**

Many beginners sell credit spreads in low IV, then:
1. Black swan event → IV spikes
2. Spread mark-to-market explodes against you
3. Forced to close at huge loss
4. **Always check IV percentile before selling!**

**IV percentile guideline:**

- >50%: Good environment to sell
- >70%: Great environment to sell
- <30%: Avoid selling, consider buying
- <20%: Dangerous for premium sellers

### Rho (Interest Rate Risk) - Usually Negligible

**Impact:** ~$0.01 per 1% rate change

**Why it doesn't matter much:**

- Rates don't change daily
- Effect minimal on short-term spreads
- More relevant for LEAPS or rate-sensitive stocks
- Can ignore for most trading

---

## Strike Selection Strategy

**Where you place your strikes determines everything:**

### The Probability-Premium Tradeoff

**The fundamental choice:**

| Short Strike | Delta | POP | Credit | Risk/Reward | Use Case |
|-------------|-------|-----|--------|-------------|----------|
| **16-delta** | 0.16 | 84% | Low | 5:1 | Conservative |
| **20-delta** | 0.20 | 80% | Medium | 4:1 | Balanced |
| **30-delta** | 0.30 | 70% | Good | 3:1 | Aggressive |
| **40-delta** | 0.40 | 60% | High | 2:1 | Very aggressive |

**The pattern:** Higher probability = lower credit = need more wins

### The 20-30 Delta Sweet Spot (Recommended)

**Why this range works:**

**20-delta short strike:**

- 80% probability of profit
- Reasonable credit (10-20% of spread width)
- Stock needs to move ~1 standard deviation to lose
- Good balance of risk/reward

**Example:**

- Stock at $100, 30 days to expiration
- Sell $95 put (20-delta) for $1.20
- Buy $90 put for $0.40
- Net credit: $0.80 on $5-wide = 16% return on risk
- POP: 80%

**Math behind it:**

If 20-delta option expires worthless 80% of time:
- Win 8 out of 10 trades: +$80 × 8 = +$640
- Lose 2 out of 10 trades: -$420 × 2 = -$840
- **Expected value: -$200**

**Wait, negative EV?! Why trade these?**

Because real trading includes:
1. **Management:** Close at 50% profit (reduces risk)
2. **Adjustments:** Roll threatened positions
3. **Filtering:** Only trade in favorable conditions
4. **Diversification:** Multiple uncorrelated positions

**With proper management, 20-delta spreads can achieve:**

- 75-80% win rate
- Average win: $0.60 (from $0.80 credit, close at 50%)
- Average loss: $3.00 (from $4.20 max, good management)
- **Positive expectancy!**

### Spread Width Selection

**How wide should your spread be?**

**Narrow spreads ($1-$2 wide):**

- **Pros:** Less capital required, smaller max loss
- **Cons:** Terrible credit (low premium), not worth risk
- **Use:** Never - avoid these

**Medium spreads ($5 wide):**

- **Pros:** Decent credit/risk ratio (15-20%), liquid
- **Cons:** Standard choice, nothing special
- **Use:** Default choice for most stocks

**Wide spreads ($10+ wide):**

- **Pros:** Excellent credit collection, better ratios
- **Cons:** Large capital requirement, larger max loss
- **Use:** High-priced stocks (AMZN, GOOGL), when you have capital

**The optimal width formula:**

$$
\text{Optimal Width} = \frac{\text{Stock Price}}{20} \text{ to } \frac{\text{Stock Price}}{10}
$$

**Examples:**

- $100 stock: $5-$10 wide spreads
- $200 stock: $10-$20 wide spreads
- $50 stock: $2.50-$5 wide spreads

**Why this matters:**

$$
\text{Credit/Risk Ratio} = \frac{\text{Net Credit}}{\text{Spread Width - Credit}}
$$

**Target:** 1:4 to 1:3 ratio (collect 20-25% of spread width)

**Example:**

- $5-wide spread, collect $1.25 credit
- Max risk: $5 - $1.25 = $3.75
- Ratio: $1.25/$3.75 = 1:3 ✓

---

## Time Selection: When to Enter and Exit

### Entry Timing: The 30-45 DTE Rule

**The professional standard:**

**Sell credit spreads 30-45 days to expiration:**

**Why this timeframe?**

1. **Optimal theta/gamma ratio:**

   - Good time decay without gamma risk explosion
   - Theta decay accelerating but not frantic
   - Time to manage if trade goes wrong

2. **Liquidity:**

   - Most liquid expiration cycle
   - Tight bid-ask spreads
   - Easy to adjust or close

3. **Premium collection:**

   - Capture ~30-40% of option's total value
   - Better than weekly (too risky) or quarterly (too slow)

4. **Probability works in your favor:**

   - More time for mean reversion
   - Stock unlikely to sustain big move for 30 days
   - Gives you management flexibility

**Comparison:**

| DTE | Theta/Day | Gamma Risk | Credit | Management Time | Verdict |
|-----|-----------|------------|--------|----------------|---------|
| 60+ | Low | Low | High | Too much | Too slow |
| 30-45 | **Optimal** | **Low** | **Good** | **Ideal** | **✓ Best** |
| 15-21 | High | Medium | Medium | Rushed | Risky |
| 0-7 | Extreme | **Extreme** | Low | None | Avoid |

### Exit Timing: The 50% Rule

**The data-driven exit strategy:**

**Close credit spreads when you've captured 50% of max profit:**

**Why 50%?**

Research from tastytrade (analyzed 1 million+ trades):
- Closing at 50% profit optimizes risk/reward
- Remaining 50% not worth the increased risk
- Frees capital for new opportunities
- Dramatically improves long-term expectancy

**The math:**

**Scenario:** Sold $5-wide spread for $1 credit

**Option A: Hold to expiration**
- Max profit: $1 (if successful)
- Max loss: $4 (if it goes against you)
- Risk/reward: 4:1
- Gamma explodes near expiration

**Option B: Close at 50% profit**
- Take profit at: $0.50
- Remaining risk: ~$2.50 (much lower)
- Risk/reward: 5:1 (better!)
- Exit with 20+ DTE (before gamma risk)

**Expected value comparison:**

Assume 70% win rate at expiration:

**Hold to expiration:**

- Win: $1 × 70% = $0.70
- Lose: -$4 × 30% = -$1.20
- **EV: -$0.50 (negative!)**

**Close at 50%:**

- Win: $0.50 × 75% = $0.375 (higher win rate)
- Lose: -$2.50 × 25% = -$0.625 (lower loss)
- **EV: -$0.25 (less negative, close to breakeven with management)**

**The 50% rule transforms credit spreads from negative to positive EV!**

### The 21-Day Management Rule

**Alternative exit timing:**

**Close spreads at 21 DTE regardless of profit/loss:**

**Rationale:**

- Gamma risk accelerates dramatically <21 DTE
- Theta benefit diminishes in final 3 weeks
- Risk of overnight gap exceeds reward of holding
- Institutional traders follow this rule religiously

**Comparison:**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/credit_spread_exit_timing.png?raw=true" alt="exit_timing" width="700">
</p>

**Combined rule:**

- Close at 50% profit, OR
- Close at 21 DTE, whichever comes first
- This maximizes long-term expectancy

### Rolling Positions

**When your spread is threatened (stock approaching short strike):**

**Rolling out (same strikes, later expiration):**

**When to roll:**

- Stock approaching short strike (delta >0.50)
- Still 14+ DTE left
- Credit collected > max loss
- Thesis still intact (still bullish/bearish)

**How to roll:**

1. Buy back current spread
2. Sell new spread same strikes, next month
3. Collect net credit for the roll
4. Extends time for stock to move favorably

**Example - Bull Put Spread Roll:**

**Original position:**

- Sold SPY $440/$435 spread for $1.25
- SPY dropped to $437 (danger!)
- Spread now worth $2.50 (losing $1.25)
- 14 DTE remaining

**Roll out:**

- Buy back $440/$435 for $2.50
- Sell next month $440/$435 for $1.75
- Net debit: -$0.75
- Total collected: $1.25 - $0.75 = $0.50
- New max loss: $5.00 - $0.50 = $4.50

**The bet:** SPY will recover above $440 in next 30 days

**When NOT to roll:**

- Thesis broken (momentum shifted)
- Stock blasting through short strike
- Already rolled once (don't chase)
- Better to take loss and move on

**Rolling down/up (adjust strikes):**

**Only in specific scenarios:**

- Turn loser into different trade (usually bad idea)
- Converting to wider spread (increases risk)
- Generally avoid - accept loss or close

---

## Maximum Profit and Loss Analysis

### Mathematical Formulas

**Bull Put Spread:**

$$
\text{Max Profit} = \text{Credit Received}
$$

$$
\text{Max Loss} = (\text{Short Strike} - \text{Long Strike}) - \text{Credit Received}
$$

$$
\text{Break-Even} = \text{Short Strike} - \text{Credit Received}
$$

**Example:**

- Stock at $100
- Sell $95 put for $2
- Buy $90 put for $0.50
- Net credit: $1.50

**Calculations:**

- Max profit: $1.50 × 100 = $150
- Max loss: ($95 - $90) - $1.50 = $3.50 × 100 = $350
- Break-even: $95 - $1.50 = $93.50

**Profit/loss at expiration:**

| Stock Price | Short Put | Long Put | Spread Value | P/L |
|------------|-----------|----------|--------------|-----|
| $100+ | Worthless | Worthless | $0 | **+$150** |
| $95 (BE + credit) | Worthless | Worthless | $0 | **+$150** |
| $93.50 (BE) | -$1.50 | Worthless | -$1.50 | $0 |
| $92 | -$3.00 | Worthless | -$3.00 | -$150 |
| $90 | -$5.00 | +$0 | -$5.00 | **-$350** |
| <$90 | -$5.00 | +$0 | -$5.00 | **-$350** |

**Bear Call Spread:**

$$
\text{Max Profit} = \text{Credit Received}
$$

$$
\text{Max Loss} = (\text{Long Strike} - \text{Short Strike}) - \text{Credit Received}
$$

$$
\text{Break-Even} = \text{Short Strike} + \text{Credit Received}
$$

**Example:**

- Stock at $100
- Sell $105 call for $2
- Buy $110 call for $0.50
- Net credit: $1.50

**Calculations:**

- Max profit: $1.50 × 100 = $150
- Max loss: ($110 - $105) - $1.50 = $3.50 × 100 = $350
- Break-even: $105 + $1.50 = $106.50

### Return on Risk Analysis

**The critical metric for credit spreads:**

$$
\text{Return on Risk} = \frac{\text{Credit Received}}{\text{Max Risk}} \times 100\%
$$

**Example:**

- Collect $1.50 credit
- Max risk $3.50
- ROR = $1.50/$3.50 = 43%

**ROR targets by timeframe:**

| DTE | Target ROR | Interpretation |
|-----|-----------|----------------|
| 30-45 | 20-33% | Ideal sweet spot |
| 15-21 | 33-50% | Aggressive but acceptable |
| 7-14 | 50%+ | Too risky (avoid) |

**Why this matters:**

**High ROR (>40%):**

- Usually means strike too close (high risk)
- Or very short DTE (gamma risk)
- Tempting but dangerous
- Lower win rate needed

**Low ROR (<15%):**

- Safe strikes but poor reward
- Need very high win rate
- Not worth capital commitment
- Better opportunities exist

**Optimal ROR (20-33%):**

- Balanced risk/reward
- Achievable with 30-45 DTE
- Sustainable long-term
- Professional standard

### Probability-Adjusted Returns

**Expected value calculation:**

$$
\text{EV} = (P_{\text{win}} \times \text{Profit}) - (P_{\text{loss}} \times \text{Loss})
$$

**Example spread:**

- Collect $150, risk $350
- Win probability: 75%
- Loss probability: 25%

**Without management:**
$$
\text{EV} = (0.75 \times \$150) - (0.25 \times \$350) = \$112.50 - \$87.50 = \$25
$$

**With 50% profit management:**

- Average win: $75 (close at 50%)
- Average loss: $250 (good management)
- Win rate increases to 80%

$$
\text{EV} = (0.80 \times \$75) - (0.20 \times \$250) = \$60 - \$50 = \$10
$$

**Why management matters:**

- Improves win rate (75% → 80%)
- Reduces average loss ($350 → $250)
- Lowers average win but increases frequency
- **Net result: More consistent profits**

---

## When to Enter Credit Spreads

### Market Conditions

**Best environments for selling credit spreads:**

#### 1. High IV Environments

**The premium seller's paradise:**

- VIX > 20
- Individual stock IV > 50th percentile
- Fat premiums available
- IV likely to contract (helping your position)

**How to check:**

1. Check VIX (market-wide volatility)
2. Check IV Rank (stock-specific volatility)
3. Only sell when IV Rank > 50%

**IV Rank formula:**

$$
\text{IV Rank} = \frac{\text{Current IV} - \text{52-week Low IV}}{\text{52-week High IV} - \text{52-week Low IV}} \times 100
$$

**Example:**

- Current IV: 35%
- 52-week range: 20% to 60%
- IV Rank = (35-20)/(60-20) = 37.5%

**Not great for selling (below 50%)**

#### 2. Post-Event IV Crush

**Perfect timing for credit spreads:**

**After earnings announcement:**

- IV drops 30-50% overnight
- Stock stabilizes in range
- Elevated premium still available
- Lower probability of big moves

**Example:**

- NFLX earnings tonight
- Pre-earnings IV: 80%
- Post-earnings IV: 45%
- Stock settles at $380 (moved on news)
- **Action:** Sell $370/$365 bull put spread
- Collect premium from still-elevated IV
- Profit from continued IV contraction

**Other events:**

- FDA decisions (biotech)
- Product launches
- Merger announcements
- Political events (elections)

**Pattern:** Sell AFTER event, when IV still elevated but uncertainty resolved

#### 3. Range-Bound Markets

**The credit spread trader's dream:**

**Characteristics:**

- Stock trading in defined range for weeks
- Low beta, predictable moves
- Technical support/resistance clear
- Boring, sideways action

**Example:**

- KO trading $58-$62 for 3 months
- Sell $57/$52 bull put spreads (below support)
- Sell $63/$68 bear call spreads (above resistance)
- Collect premium from both sides (iron condor)
- **Profit from time decay in range**

### Technical Setups

**Combine credit spreads with technical analysis:**

#### Bull Put Spreads - Technical Entry Signals

**1. Support level bounces:**

- Stock pulls back to strong support
- Bullish reversal pattern forming
- **Sell puts below support**

**2. Uptrend continuation:**

- Stock in clear uptrend (higher lows)
- Pullback to rising trendline
- **Sell puts at/below trendline**

**3. Moving average support:**

- Stock above rising 50/200 EMA
- Price tests EMA and holds
- **Sell puts below EMA**

**4. Bullish chart patterns:**

- Bull flag/pennant forming
- After consolidation near highs
- **Sell puts below pattern low**

#### Bear Call Spreads - Technical Entry Signals

**1. Resistance rejection:**

- Stock rallies to resistance, fails
- Bearish reversal pattern forming
- **Sell calls above resistance**

**2. Downtrend continuation:**

- Stock in clear downtrend (lower highs)
- Bounce to falling trendline
- **Sell calls at/above trendline**

**3. Moving average resistance:**

- Stock below declining 50/200 EMA
- Price tests EMA from below, rejects
- **Sell calls above EMA**

**4. Bearish chart patterns:**

- Bear flag/head and shoulders
- After rally in downtrend
- **Sell calls above pattern high**

### Fundamental/News-Based Entries

**Using catalysts and news flow:**

#### Positive Scenarios (Bull Put Spreads)

**1. Better-than-expected earnings:**

- Company beats estimates
- Stock gaps up
- Sell puts below new support (gap fill level)

**2. Positive analyst upgrades:**

- Major firm upgrades stock
- Price target raised significantly
- Sell puts below previous resistance (now support)

**3. Sector rotation into stock:**

- Money flowing into sector
- Stock showing relative strength
- Sell puts on pullbacks

#### Negative Scenarios (Bear Call Spreads)

**1. Worse-than-expected earnings:**

- Company misses badly
- Stock gaps down
- Sell calls above new resistance (gap fill level)

**2. Negative analyst downgrades:**

- Major firm downgrades
- Price target slashed
- Sell calls above previous support (now resistance)

**3. Regulatory headwinds:**

- New regulations threaten business
- Legal issues arise
- Sell calls on rallies (dead cat bounces)

---

## When to Avoid Credit Spreads

**Situations where credit spreads are dangerous:**

### 1. Low IV Environments

**The premium desert:**

- VIX < 15
- Stock IV < 30th percentile
- Premiums anemic
- Not worth the risk

**Example:**

- Want to sell SPY $440/$435 bull put spread
- IV Rank: 25% (low)
- Credit available: $0.40
- Max risk: $4.60
- **ROR: 8.7% (terrible!)**

**Why it fails:**

- Tiny credit for substantial risk
- If IV spikes, you're crushed
- Better to buy options in low IV

**Rule:** Never sell credit spreads when IV Rank < 30%

### 2. Binary Events Approaching

**The known-unknown trap:**

**Events that create massive uncertainty:**

- Earnings in 0-3 days
- FDA decisions pending
- Merger votes
- Patent litigation verdicts
- Political elections

**Why avoid:**

- IV will spike (hurts your position)
- Stock can gap huge (blow through your spread)
- Probability models break down
- One event can wipe out months of gains

**Example - The Earnings Mistake:**

**Setup:**

- NVDA at $450
- Earnings tomorrow
- IV at 60% (elevated)
- Sell $440/$435 bull put spread for $2

**What happens:**

- Earnings: Miss revenue by 5%
- Stock gaps to $400 overnight
- Spread worth $5 (max loss)
- **Lost $3 per share instantly**

**The lesson:** That $2 premium wasn't worth the gap risk

### 3. Parabolic Moves

**Don't fight momentum:**

**When stock is ripping/crashing:**

- Vertical price action
- 20+ IV percentile spike
- RSI >80 or <20
- Clear momentum/mania

**Example:**

- GME at $40, squeezing to $100
- "It has to come down, I'll sell $120 calls!"
- Stock goes to $480
- **Destroyed**

**Rule:** Never sell premium against parabolic moves, wait for consolidation

### 4. Around Ex-Dividend Dates

**The early assignment trap:**

**For put spreads specifically:**

- Stock goes ex-dividend in 0-5 days
- Short put ITM
- You can be assigned early (forced to buy stock)
- Unexpected capital requirement
- Lose defined-risk protection

**Example:**

- Sold $95 put on $100 stock
- Ex-dividend: $2 tomorrow
- Put becomes ITM after dividend
- Assigned early, now own 100 shares at $95
- Stock drops to $90
- **Lost more than max spread loss**

**Rule:** Close put spreads 3-5 days before ex-dividend if ITM

---

## Common Mistakes Beginners Make

### 1. Chasing Premium (Selling Too Close to Price)

**The temptation:**

- See $3 credit on tight spread
- "Wow, 60% return on risk!"
- Stock only needs to stay above...
- **Stock moves $2, you're destroyed**

**The mistake:**

- Selling 40-50 delta options (low probability)
- Chasing high ROR without understanding risk
- Ignoring probability of profit

**Example:**

- AAPL at $180
- Sell $178/$173 bull put spread for $3
- Stock drops to $175 (normal pullback)
- **Max loss: -$2 per share**

**The fix:**

- Stick to 20-30 delta short strikes
- Accept lower premium for higher probability
- 20% ROR at 75% win rate > 50% ROR at 50% win rate

### 2. Holding Until Expiration

**The greed:**

- Spread at $0.20, collected $1
- "Just 5 more days for last $0.20..."
- Stock gaps through short strike
- **Turn $0.80 winner into -$3 loser**

**The mistake:**

- Squeezing last penny of time value
- Exposing position to gamma risk
- Ignoring data (50% rule optimizes returns)

**The fix:**

- Close at 50% profit religiously
- Exit at 21 DTE regardless
- Free up capital for new opportunities

### 3. Selling in Low IV

**The trap:**

- "I'll just sell every week for income"
- Market calm, VIX at 12
- Collect $0.30 on $5 spread
- IV spikes, lose $2
- **Months of gains wiped out**

**The mistake:**

- Not checking IV environment
- Mechanical selling without selectivity
- Ignoring volatility cycles

**The fix:**

- Only sell when IV Rank > 50%
- Be patient, wait for opportunities
- When IV low, buy options instead (debit spreads)

### 4. Over-Leveraging

**The ruin:**

- $10,000 account
- Sell 20 credit spreads (max risk $10,000)
- "I'll just manage them..."
- Market crashes, all hit max loss
- **Account to $0**

**The mistake:**

- Using all buying power
- Not leaving room for losses
- Treating high probability as certainty

**The fix:**

- Max 30-40% of portfolio in credit spreads
- Max 5-10% per underlying
- Max 2-5% per trade
- **Always have cash reserve for adjustments**

### 5. Not Using Stop Losses

**The hope:**

- Spread goes against you
- "It's a high probability trade, just wait"
- Holding through -100%, -200% loss
- "It HAS to come back..."
- **Nope, max loss**

**The mistake:**

- Confusing probability with certainty
- No exit plan for losers
- Emotional attachment to "being right"

**The fix:**

- Set stop loss at 2x credit (losing trade)
- If spread doubles in value against you, exit
- Accept losses quickly
- Move on to next trade

### 6. Ignoring Correlation

**The disaster:**

- Sell bull put spreads on:
  - AAPL, MSFT, AMZN, GOOGL, META
- "Diversified across 5 stocks!"
- Market correction
- **All 5 hit max loss simultaneously**

**The mistake:**

- False diversification (all tech)
- Ignoring sector/market correlation
- Compounding risk instead of spreading it

**The fix:**

- Diversify across sectors
- Mix bull and bear spreads
- Vary expiration dates
- Consider index hedges

### 7. The Addiction to Premium

**The psychological trap:**

- Credit spreads feel good (collect money upfront)
- Dopamine hit from seeing credit
- Start selling more and more
- "I'm a premium collection machine!"
- **One bad month wipes out 6 good months**

**The mistake:**

- Treating trading like gambling
- Focusing on wins, ignoring tail risk
- Not respecting negative skew

**The reality:**

Credit spreads have **negative skew:**

- Many small wins
- Occasional large losses
- One bad loss can erase months of gains
- **Need discipline to survive long-term**

**The fix:**

- Track overall P/L, not win rate
- Calculate expectancy (not just probability)
- Use stop losses religiously
- Take breaks after losing trades (avoid revenge trading)

---

## Advanced Concepts

### 1. Credit Spread Arbitrage

**Identifying mispricings in the options chain:**

**Put-Call Parity Violations:**

In theory:
$$
\text{Bull Put Spread} + \text{Bear Put Spread} = \text{Spread Width}
$$

**Example:**

- $5-wide spread should total $5 in credits

**Reality:**

- Bull put spread (sell $95/90): Collect $1.20
- Bear put spread (sell $100/95): Collect $4.10
- Total: $5.30 (>$5.00)

**Arbitrage opportunity:**

- Sell both spreads
- Collect $5.30 total
- Max risk: $5.00
- **Guaranteed $0.30 profit**

**Why it exists:**

- Market inefficiency
- Skew in put prices
- Temporary supply/demand imbalance

**How to find:**

- Compare bull put vs. bear put at same strikes
- Look for total credit > spread width
- Act fast (arb disappears quickly)

### 2. Diagonal Credit Spreads

**Variation: Different expiration dates**

**Structure:**

- Sell near-term option (high theta)
- Buy later-term option (protection)
- Collect net credit (usually)
- Benefits from theta and calendar effects

**Example - Diagonal Bull Put:**

- Stock at $100
- Sell $95 put, 30 DTE for $2
- Buy $90 put, 60 DTE for $1.50
- Net credit: $0.50

**Advantages:**

- Long option doesn't decay as fast
- Can roll short option monthly
- Reduced capital requirement vs. vertical

**Disadvantages:**

- More complex to manage
- Vega risk from long option
- Can lose on both legs in extreme moves

**When to use:**

- Expect gradual move in your favor
- Want to leg into calendar spread
- Bullish long-term, neutral short-term

### 3. Credit Spread Legs vs. Iron Condors

**Combining bull put + bear call = Iron Condor**

**Iron Condor structure:**

- Sell OTM put spread (bull put)
- Sell OTM call spread (bear call)
- Collect credit from both sides
- Profit if stock stays in range

**Comparison:**

| Strategy | Directional Bias | Premium | Management |
|----------|-----------------|---------|------------|
| Bull Put Spread | Bullish/neutral | Moderate | Simple |
| Bear Call Spread | Bearish/neutral | Moderate | Simple |
| Iron Condor | Neutral | High | Complex |

**When to use Iron Condor:**

- Stock in tight range
- Expect consolidation
- High IV environment
- Willing to manage 4 legs

**When to use single spread:**

- Have directional bias
- Simpler management
- Lower capital requirement
- Clearer risk definition

### 4. Ratio Credit Spreads

**Variation: Unequal number of contracts**

**Structure:**

- Sell 2 near-ATM options
- Buy 1 far-OTM option
- Collect larger credit
- Undefined risk if stock moves far

**Example:**

- Sell 2 × $95 puts for $4 total
- Buy 1 × $90 put for $1.50
- Net credit: $2.50
- **Risky if stock crashes hard**

**Advantages:**

- Much higher credit
- Better return on capital
- Works well in low IV

**Disadvantages:**

- Undefined risk beyond long strike
- Requires more management
- Can blow up in tail events

**When to use:**

- Very high conviction on range
- Low probability of extreme move
- Experienced traders only
- **Never in high IV or before events**

### 5. The Implied Probability Arbitrage

**Using theoretical vs. market probabilities:**

**Theory:**

- Option delta ≈ probability of finishing ITM
- 30-delta option ≈ 30% chance of ITM

**Reality:**

- Market prices don't always match theoretical probabilities
- Skew creates opportunities

**Example:**

- Stock at $100
- $95 put has 25-delta (25% ITM probability)
- But historical data shows: stock only drops below $95 15% of time
- **Market overpricing downside protection**

**Opportunity:**

- Sell $95 put (collect inflated premium)
- Market paying for 25% probability
- Reality is 15% probability
- **Statistical edge over time**

**How to identify:**

- Compare implied volatility to realized volatility
- Check historical move probabilities
- Find where IV > realized vol consistently
- Sell those overpriced options

### 6. Volatility Surface Trading

**Exploiting skew in the volatility smile:**

**The pattern:**

- OTM puts have higher IV than ATM (put skew)
- Downside protection is expensive
- Upside calls have lower IV

**Strategy:**

- Sell the expensive OTM puts (high IV)
- Use that premium to buy ATM options
- Capture the skew premium

**Example:**

- ATM put (Strike $100): IV = 30%, costs $4
- OTM put (Strike $90): IV = 40%, costs $2

**Bull put spread:**

- Sell $90 put (IV = 40%) for $2
- Buy $85 put (IV = 45%) for $1.25
- Net credit: $0.75
- **Selling higher IV than buying (good)**

**The edge:**

- Volatility smile tends to flatten
- OTM puts' elevated IV often contracts
- Spread value decreases faster than theta alone
- **Vega contraction + theta decay working together**

---

## Risk Management Rules

**Essential guidelines for credit spread trading:**

### Position Sizing

**The Kelly Criterion adapted for credit spreads:**

$$
\text{Position Size} = \frac{p \times W - (1-p) \times L}{W \times L} \times \text{Capital}
$$

Where:
- $p$ = Probability of winning
- $W$ = Win amount (credit)
- $L$ = Loss amount (max risk)

**Example:**

- Win probability: 75%
- Average win: $150
- Average loss: $350

$$
\text{Position Size} = \frac{0.75 \times 150 - 0.25 \times 350}{150 \times 350} \times \text{Capital}
$$

**Result: ~1-2% of capital per trade**

**Practical sizing rules:**

1. **Per-trade limit:** Max 2-5% of account per credit spread
2. **Per-underlying limit:** Max 10% of account in one stock
3. **Total exposure:** Max 30-40% of account in credit spreads
4. **Correlation adjustment:** Reduce size when positions correlated

**Example for $50,000 account:**

- Max per spread: $2,500 (5%)
- Max per stock: $5,000 (10%)
- Max total credit spreads: $20,000 (40%)
- Cash reserve: $30,000 (for adjustments)

### Diversification

**Never put all eggs in one basket:**

**Sector diversification:**

- Max 20% in any sector
- Mix cyclical and defensive
- Include index spreads for broad exposure

**Time diversification:**

- Vary expiration dates
- Don't have everything expiring same week
- Stagger entries over time

**Strategy diversification:**

- Mix bull puts and bear calls
- Some in high IV, some in medium IV
- Different underlying volatilities

**Example portfolio:**

- 3 bull put spreads (different sectors, different DTE)
- 2 bear call spreads (different sectors)
- 1 iron condor on index
- All with 30-45 DTE
- Max $1,000 risk per position

### Exit Rules

**Set upfront, execute mechanically:**

#### Profit Taking

**1. The 50% profit rule:**

- Close when captured 50% of max credit
- Example: Sold for $1, close at $0.50
- Optimal risk/reward balance

**2. The 21-DTE exit:**

- Close all spreads at 21 DTE
- Avoid gamma explosion risk
- Frees capital for new trades

**3. The delta trigger:**

- If short option delta reaches 0.70, close immediately
- Position too risky regardless of P/L
- Gamma risk too high

#### Loss Cutting

**1. The 2x credit stop loss:**

- If spread value doubles, exit
- Example: Sold for $1, exit at $2 (losing $1)
- Prevents holding through max loss

**2. The 50% max loss stop:**

- Never lose more than 50% of max risk
- Example: Max risk $400, stop at -$200
- Preserves capital for next trade

**3. The thesis break:**

- If fundamental reason for trade invalidated, exit
- Don't wait for technical stop
- Example: Bullish spread, company issues profit warning → exit

#### Time Stops

**1. Theta decay insufficient:**

- If 50% of time passed and only 25% profit → exit
- Theta not working as expected
- Free capital for better opportunity

**2. Stuck in the mud:**

- Position unchanged for 10+ days
- No progress toward profit
- Opportunity cost too high → exit

### The Adjustment Framework

**When position threatened but not dead:**

#### Scenario 1: Stock Approaching Short Strike

**Diagnosis:**

- 14+ DTE remaining
- Short strike delta 0.50-0.60
- Thesis still intact
- Overall market supportive

**Action: Roll out**
1. Buy back current spread
2. Sell same strikes, next monthly expiration
3. Collect net credit
4. Reset probability in your favor

#### Scenario 2: Stock Blasted Through Short Strike

**Diagnosis:**

- Short strike now ATM or ITM
- Delta >0.70
- Time running out

**Action: Exit immediately**
- Don't try to adjust
- Accept loss
- Move on

#### Scenario 3: IV Spike

**Diagnosis:**

- Spread value increased due to IV
- Stock position unchanged
- IV rank jumped 20+ points

**Action: Consider closing**
- If near profit target, take it early
- If losing, might worsen before improving
- Evaluate if IV spike justified (event coming?)

#### Scenario 4: Slow Bleed

**Diagnosis:**

- Position slowly losing
- No catalyst for reversal
- Time decay not helping enough

**Action: Exit at 50% max loss**
- Cut losses before they become full losses
- Preserve capital
- Find better setup

### Avoid These

**Never commit these capital-destroying errors:**

1. **Never go full portfolio:** Always keep 50%+ cash
2. **Never average down:** Adding to losers compounds mistakes
3. **Never trade illiquid options:** Bid-ask > $0.20 = avoid
4. **Never sell before events:** Earnings, FDA, etc. = stay away
5. **Never ignore IV rank:** Selling in low IV = long-term failure
6. **Never over-concentrate:** One stock, one sector = recipe for disaster
7. **Never hold to expiration:** Last week gamma risk = account killer
8. **Never trade without stops:** Hope is not a strategy

### The Emergency Exit Plan

**When everything goes wrong:**

**Market crash scenario:**

- VIX spikes to 40+
- All positions threatened
- What do you do?

**Action plan:**

1. **Assess damage:** Which positions salvageable?
2. **Triage:** Close worst positions first (deepest ITM)
3. **Keep winners:** Don't panic close profitable spreads
4. **Free up capital:** Need cash for recovery plays
5. **Wait for IV to stabilize:** Don't immediately re-enter

**Example:**

- Portfolio has 5 bull put spreads
- Market crashes, 3 spreads threatened
- Action:
  - Close 1 worst spread (accept max loss)
  - Roll 1 medium spread (buy time)
  - Keep 1 far OTM spread (still profitable)
  - Exit other 2 safe spreads at profit
  - Sit in cash until VIX drops

---

## Real-World Examples

### Example 1: SPY Bull Put Spread (Successful Trade)

**Setup (September 2024):**

- SPY at $560 (uptrend intact)
- Market consolidating after rally
- Support at $550 holding firm
- IV Rank: 45% (moderate)
- VIX: 18

**Technical analysis:**

- 50-day EMA at $555 (rising)
- RSI: 55 (neutral, not overbought)
- Volume declining (healthy consolidation)

**Trade:** Bull Put Spread

- **Sell:** $545 put (20-delta) for $3.50
- **Buy:** $540 put for $1.50
- **Net credit:** $2.00 = $200 per spread
- **Max risk:** ($5 - $2) = $3.00 = $300 per spread
- **Break-even:** $543
- **DTE:** 35 days
- **POP:** ~80%

**Position sizing:**

- $50,000 account
- Max risk per trade: $2,500 (5%)
- Number of spreads: 8 contracts
- Total credit collected: $1,600
- Total risk: $2,400

**Management plan:**

- Close at 50% profit ($100 per spread)
- Stop loss at -100% (spread worth $4)
- Exit at 21 DTE regardless

**Outcome:**

Day 1-10:
- SPY consolidates $557-$563
- Spread value: $1.80 (slight profit)
- No action needed

Day 11-20:
- SPY rallies to $572
- Spread value: $0.80
- **60% profit! Close position**

**Final results:**

- Entry: $2.00 credit ($1,600 total)
- Exit: $0.80 ($640 buy-back cost)
- **Profit: $1.20 per spread = $960 total**
- **ROI: 40% in 20 days**
- **Annualized: ~730%**

**Lessons:**

- Proper strike selection (20-delta)
- Closed at 60% (exceeded 50% rule)
- Exited with 15 DTE remaining (avoided gamma risk)
- Position sizing allowed comfortable hold

### Example 2: TSLA Bear Call Spread (Loss Example)

**Setup (October 2024):**

- TSLA at $240 (parabolic rally)
- Stock up 40% in 2 months
- Resistance at $250 (previous high)
- IV Rank: 65% (elevated)
- Elon Musk bullish on Twitter

**Technical analysis:**

- RSI: 78 (overbought)
- Momentum divergence (price up, RSI declining)
- Volume decreasing on rally (warning sign)

**The mistake:** Fighting the trend

**Trade:** Bear Call Spread

- **Sell:** $255 call (25-delta) for $5.00
- **Buy:** $265 call for $2.00
- **Net credit:** $3.00 = $300 per spread
- **Max risk:** ($10 - $3) = $7.00 = $700 per spread
- **Break-even:** $258
- **DTE:** 30 days
- **POP:** ~75%

**What went wrong:**

Day 1-5:
- TSLA continued rally to $255
- Short strike now ATM
- Spread value: $5.50 (losing $2.50)
- **Should have exited here (2x credit rule)**
- **Mistake: Held, thinking "it's overbought"**

Day 6-10:
- TSLA gaps to $270 on positive news
- Spread now at max loss
- Value: $10.00
- **Total loss: $700 per spread**

**If traded 3 contracts:**

- Collected: $900 total
- Final loss: -$2,100
- **Net: -$1,200 loss**

**Lessons learned:**

1. **Don't fight parabolic moves** (biggest mistake)
2. **Follow stop loss rules** (should have exited at $6)
3. **Respect momentum** (trend is friend)
4. **IV rank not enough** (other factors matter)
5. **Don't bet against Elon** (cult stocks are different)

**What should have been done:**

- Wait for TSLA to consolidate
- Or sell bear call much higher ($280/$290)
- Or simply avoid - too much momentum
- **Better to miss opportunity than force bad trade**

### Example 3: AAPL IV Crush Trade (Post-Earnings)

**Setup (November 2024):**

- AAPL earnings released yesterday
- Stock at $190 (moved up $5 on earnings)
- Pre-earnings IV: 55%
- Post-earnings IV: 30%
- IV Rank: 40% → 25% (crushed)

**The opportunity:**

- Event risk gone (earnings passed)
- IV still elevated but declining
- Stock found new range
- Technical support at $185

**Trade:** Bull Put Spread (IV crush play)

- **Sell:** $185 put (18-delta) for $2.20
- **Buy:** $180 put for $0.90
- **Net credit:** $1.30 = $130 per spread
- **Max risk:** ($5 - $1.30) = $3.70 = $370 per spread
- **DTE:** 28 days (next monthly)
- **POP:** ~82%

**Why this works:**

- Selling after IV spike (better premium)
- Event uncertainty removed
- Stock unlikely to move big in next month
- IV continues to contract → spread value drops
- **Double benefit: theta + vega contraction**

**Outcome:**

Week 1:
- AAPL consolidates $188-$192
- IV drops to 25%
- Spread value: $0.90 (30% profit)

Week 2:
- AAPL drifts to $193
- IV drops to 23%
- Spread value: $0.60 (53% profit)
- **Close position!**

**Final results:**

- Entry: $1.30 credit
- Exit: $0.60 ($70 buy-back)
- **Profit: $0.70 per spread**
- **ROI: 19% in 14 days**
- **Key advantage: Vega contraction added to theta decay**

**Lessons:**

- Post-event timing crucial (IV still elevated)
- Double benefit: time decay + IV contraction
- Closed at 50%+ profit (followed rules)
- Avoided holding through potential news

### Example 4: Portfolio Approach (Iron Condor on SPY)

**Setup (December 2024):**

- SPY at $575 (holiday season, low volume)
- Market range-bound for 2 weeks
- $565-$585 range established
- IV Rank: 35% (below average but acceptable)
- No major catalysts upcoming

**Strategy:** Iron Condor (bull put + bear call)

**Bull Put Spread:**

- Sell $560 put for $2.50
- Buy $555 put for $1.00
- Credit: $1.50

**Bear Call Spread:**

- Sell $590 call for $2.00
- Buy $595 call for $0.80
- Credit: $1.20

**Combined Iron Condor:**

- Total credit: $2.70 = $270 per IC
- Max risk: $2.30 = $230 per IC (on either side)
- Break-evens: $557.30 (downside), $592.70 (upside)
- DTE: 35 days
- **Profit zone: $557-$593 (36-point range)**

**Management:**

Week 1-2:
- SPY trades $570-$580 (perfect)
- Both spreads decaying nicely
- IC value: $1.80 (33% profit)

Week 3:
- SPY rallies to $587
- Call spread threatened (getting close)
- Put spread safe
- IC value: $2.00 (26% profit)

**Decision:** Close early
- Target was 50% but risk increasing
- Take 26% profit with 12 DTE left
- Avoid late gamma risk

**Final results:**

- Entry: $2.70 credit
- Exit: $2.00
- **Profit: $0.70 = $70 per IC**
- **ROI: 30% in 23 days**

**If traded 5 ICs:**

- Collected: $1,350
- Profit: $350
- **Return on risk: 30% in 3 weeks**

**Lessons:**

- Range-bound strategy worked
- Didn't wait for 50% (risk management)
- Exited before gamma risk period
- Diversification within one structure (bull + bear)

---

## What to Remember

### Core Concept

**Credit spreads are probability-based, defined-risk premium collection strategies:**

$$
\text{Credit Spread} = \text{Sell insurance, buy reinsurance, keep the spread}
$$

- Collect premium upfront
- Max profit = credit (limited)
- Max loss = spread width - credit (defined)
- Need high win rate (60-80%) to overcome risk/reward ratio
- Time decay works FOR you

### The Setup

**Bull Put Spread (Bullish):**

- Sell higher strike put
- Buy lower strike put (protection)
- Collect net credit
- Profit if stock stays flat or rises
- Max loss if stock crashes below long put

**Bear Call Spread (Bearish):**

- Sell lower strike call
- Buy higher strike call (protection)
- Collect net credit
- Profit if stock stays flat or falls
- Max loss if stock rallies above long call

### The Greeks

**Critical to understand:**

- **Delta:** ±0.20 to ±0.40 (moderate directional exposure)
- **Theta:** +$0.02 to +$0.08/day (time decay helps you!)
- **Gamma:** Negative (accelerates against you near expiration)
- **Vega:** Negative (IV increase hurts, IV decrease helps)

### Strike Selection

**The 20-30 delta rule:**

- Sell 20-30 delta short strike (80-70% POP)
- Spread width: 5-10 points (depending on stock price)
- Target credit: 20-33% of spread width
- Sweet spot for risk/reward balance

### Time Selection

**The 30-45 DTE standard:**

- Enter 30-45 days to expiration
- Exit at 50% profit OR 21 DTE
- Optimal theta decay zone
- Avoid last 3 weeks (gamma explosion)

### Maximum Profit/Loss

**Bull Put Spread:**

- Max profit: Net credit collected
- Max loss: Spread width - credit
- Breakeven: Short strike - credit

**Bear Call Spread:**

- Max profit: Net credit collected
- Max loss: Spread width - credit
- Breakeven: Short strike + credit

### When to Use

**Sell credit spreads when:**

- IV Rank > 50% (elevated volatility)
- High conviction on direction
- Post-event (earnings, FDA, etc.)
- Range-bound market expected
- Want defined risk (vs. naked selling)

**Don't use when:**

- IV Rank < 30% (low volatility)
- Major event coming (0-3 days)
- Parabolic move happening
- Unclear market direction
- Low liquidity (wide spreads)

### Common Mistakes to Avoid

1. Don't chase premium (selling too close to price)
2. Don't hold to expiration (gamma risk)
3. Don't sell in low IV (poor risk/reward)
4. Don't over-leverage (max 30-40% of portfolio)
5. Don't ignore stop losses (hope is not a strategy)
6. Don't fight parabolic moves (trend is friend)
7. Don't ignore correlation (false diversification)
8. Don't get addicted to premium collection (respect tail risk)

### Risk Management

**Essential rules:**

- Position size: Max 2-5% of portfolio per trade
- Exit at 50% profit (optimal risk/reward)
- Stop loss at 2x credit or 50% max loss
- Close at 21 DTE (avoid gamma)
- Diversify: sectors, timeframes, strategies
- Check IV Rank before every trade
- Keep 50%+ cash reserve

### Comparison to Debit Spreads

**Advantages over debit spreads:**

- Collect money upfront (positive cash flow)
- Time decay works FOR you
- Higher probability of profit (60-80%)
- Better for range-bound markets

**Disadvantages vs. debit spreads:**

- Limited profit potential (just credit)
- Negative skew (rare big losses)
- Need high win rate to profit
- Gamma works against you

### Your Learning Path

**Start here (credit spreads), then:**

1. Master basic bull puts and bear calls
2. Combine into iron condors (neutral strategy)
3. Learn calendar spreads (time dimension)
4. Progress to diagonals (time + strike)
5. Eventually: volatility surface trading

**Credit spreads are THE WORKHORSE for income traders!**

### Final Wisdom

> "Credit spreads are the thinking trader's strategy - they require patience, discipline, and respect for probability. You'll win most of the time, but the losses can sting. The key is proper position sizing, timely exits, and never fighting momentum. Master the 50% profit rule, the 21 DTE exit, and the IV Rank filter - these three rules alone will transform your results. Remember: you're selling insurance. Insurance companies profit not by avoiding all claims, but by pricing risk correctly and diversifying."

**Key to success:**

- High-probability setups only (IV Rank > 50%)
- Proper position sizing (2-5% max per trade)
- Exit discipline (50% profit, 21 DTE, 2x stop)
- Diversification (sectors, timeframes, directions)
- Check IV before entering (never sell in low IV)
- Respect momentum (don't fight parabolic moves)
- Manage winners early (greed kills)

**Most important:** Credit spreads offer defined risk with consistent income potential - but only if you follow the rules religiously! 🎯📊
