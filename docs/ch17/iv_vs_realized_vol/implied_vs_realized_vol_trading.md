# Implied vs Realized

## Trading the


**Implied vs realized volatility trading** focuses on exploiting the systematic difference between **implied volatility (what the market prices)** and **realized volatility (what actually occurs)**.

This is one of the most fundamental and persistent edges in volatility trading.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/implied_vs_realized_vol_trading_comparison.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/implied_vs_realized_vol_trading_risk_premium.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/implied_vs_realized_vol_trading_strategy_returns.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/implied_vs_realized_vol_trading_win_rate.png?raw=true" alt="long_call_vs_put" width="700">
</p>

---

## The Core Insight


**The fundamental idea:**

- Implied volatility (IV) reflects **expected + risk premium**

- Realized volatility (RV) reflects **actual price movement**

- On average:
  \[
  \text{IV} > \text{RV}
  \]

- The difference is called the **volatility risk premium**

- Traders can systematically **sell or buy volatility** to capture this spread

> **You are trading the price of uncertainty versus the realized uncertainty.**

---

## What Are Implied and


### 1. Implied


- Backed out from option prices

- Forward-looking

- Includes:

  - Expected volatility

  - Risk aversion

  - Tail-risk premium

  - Supply/demand effects

\[
\text{Option Price} = f(S, K, T, r, \sigma_{\text{implied}})
\]

---

### 2. Realized


- Measured from historical price returns

- Backward-looking

- Computed as:

\[
\sigma_{\text{realized}} = \sqrt{\frac{252}{N} \sum_{i=1}^N (\log S_i - \log S_{i-1})^2}
\]

- What actually happens in the market

---

## Why IV Is Usually


IV embeds compensation for:

- Crash risk

- Jump risk

- Model uncertainty

- Hedging demand

- Margin and capital constraints

This creates a **structural premium** paid by option buyers to option sellers.

> **Selling volatility is selling insurance.**

---

## Why the IV–RV Spread


The IV–RV gap is:

- Persistent

- Mean-reverting

- Observable

- Tradeable via options and variance instruments

**Trading opportunity arises when:**

- IV is unusually high relative to expected RV

- IV is unusually low relative to expected RV

- Market overprices or underprices future uncertainty

---

## The Structure


### 1. General IV–RV


IV–RV trades typically involve:

- Selling or buying options (IV)

- Hedging directional exposure

- Letting realized volatility determine P&L

> **You are betting on realized volatility relative to what the option market implies.**

---

### 2. Common IV–RV


### 3. Short Straddle /


\[
\text{Short Straddle} = -C(K) - P(K)
\]

- Sell implied volatility

- Delta-hedge

- Profit if realized volatility < implied

---

### 4. Long Straddle


\[
\text{Long Straddle} = +C(K) + P(K)
\]

- Buy implied volatility

- Profit if realized volatility > implied

- Used around events or regime shifts

---

### 5. Gamma Scalping


- Long gamma via options

- Actively delta-hedge

- Profit from realized volatility exceeding implied

---

### 6. Variance Swaps


\[
\text{Payoff} = (\sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2)
\]

- Cleanest expression of IV–RV trade

- No vega smile or skew effects

- Not usually accessible to retail traders

---

## The Portfolio


### 1. Generic IV–RV


\[
\Pi_{\text{IV-RV}} = \sum_i n_i \cdot V(K_i, T, \sigma_{\text{implied}})
\]

Managed so that:

\[
\Delta \approx 0
\]

The portfolio’s P&L depends primarily on **realized volatility**.

---


---

## Economic


**Understanding what this strategy REALLY represents economically:**

### 1. The Core Economic


This IV strategy involves specific economic trade-offs around volatility exposure. The key is understanding what you're giving up versus what you're gaining in terms of implied volatility positioning.

**Economic equivalence:**

$$
\text{Strategy P\&L} = \text{IV Change Component} + \text{Term Structure Component} + \text{Skew Component}
$$

### 2. Why This IV


Markets create these IV structures because different participants have different:

- Volatility expectations (near-term vs. long-term)

- Risk preferences (convexity vs. theta)

- Event views (known catalysts vs. unknown volatility)

- Hedging needs (portfolio protection vs. income generation)

### 3. The Volatility


Most IV strategies exploit the **volatility risk premium** - the empirical observation that:

$$
\text{Implied Volatility} > \text{Realized Volatility} \quad \text{(on average)}
$$

**Why this exists:**

1. **Insurance value:** Investors pay premium for protection

2. **Crash insurance:** Fear of tail events inflates IV

3. **Supply/demand:** More vol buyers than sellers

4. **Behavioral biases:** Overestimation of future volatility

### 4. Professional


Institutional traders view IV strategies as tools for:

1. **Volatility arbitrage:** Extracting the vol risk premium

2. **Term structure trading:** Exploiting mispricings across time

3. **Skew trading:** Capturing mispricing across strikes

4. **Surface arbitrage:** Finding no-arbitrage violations

Understanding the economic foundations helps you recognize when IV offers genuine edge versus when market pricing is fair.


## The P&L Formula


### 1. Core P&L Driver


\[
\text{P\&L} \approx \text{Vega} \cdot (\sigma_{\text{implied}} - \sigma_{\text{realized}})
\]

- Short volatility:

  - Profit if RV < IV

- Long volatility:

  - Profit if RV > IV

---

### 2. Decomposition


\[
\text{P\&L} =
\underbrace{\text{Theta}}_{\text{Vol premium}}
+
\underbrace{\text{Gamma P\&L}}_{\text{Realized vol}}

-
\underbrace{\text{Hedging costs}}_{\text{Slippage}}
\]

---

## Concrete Example


### 1. Short Volatility


**Underlying:** SPY  

**Spot:** 450  

**Maturity:** 30 days  

**ATM IV:** 22%

**Trade:**

- Sell ATM straddle

- Delta-hedge daily

**Outcome scenarios:**

1. **Realized vol = 15%**

   - Options decay faster than price moves

   - Theta dominates

   - Profit

2. **Realized vol = 22%**

   - Break-even (before costs)

3. **Realized vol = 30%**

   - Large price swings

   - Gamma losses dominate

   - Loss

---

## Risk Management


### 1. Key Risks


- Tail risk (large jumps)

- Volatility clustering

- Regime shifts

- Gap risk

- Model error

---

### 2. Risk Controls


- Position sizing

- Stop-loss rules

- Use spreads instead of naked options

- Diversify across time and assets

- Avoid known event risk (earnings, macro)

---

## Relationship to


| Strategy | What It Trades |
|--------|---------------|
| Directional options | Price |
| Skew trading | Strike asymmetry |
| Term structure trades | Time dimension |
| **IV–RV trading** | **Volatility premium** |
| Surface arbitrage | Full surface |

> **IV–RV trading is the foundation of most option-selling strategies.**

---

## When IV–RV Trading


✅ Normal markets  
✅ High implied volatility environments  
✅ Diversified portfolios  
✅ Systematic execution  

❌ Crisis regimes  
❌ Structural regime shifts  
❌ Illiquid options  
❌ Poor risk controls  

---


---



## Practical Guidance


**Step-by-step implementation framework:**

### 1. Before entering,


**Before entering, evaluate:**

1. **IV level analysis:**

   - Current IV percentile (IVP) or IV rank (IVR)

   - Is IV historically high or low?

   - IV vs. realized volatility spread

2. **Term structure analysis:**

   - Shape of vol term structure (contango/backwardation)

   - Front month vs. back month IV relationship

   - Event-driven distortions in term structure

3. **Skew analysis:**

   - Put vs. call IV differential

   - Shape of vol smile/smirk

   - Unusual skew steepness

4. **Upcoming events:**

   - Earnings announcements

   - Fed meetings, economic data

   - Product launches, regulatory decisions

### 2. Enter this


**Enter this strategy when:**

- [Specific IV conditions]

- [Term structure requirements]

- [Skew positioning]

- [Time to event/expiration]

**Avoid this strategy when:**

- [Unfavorable IV environment]

- [Wrong term structure shape]

- [Insufficient IV edge]

- [Event risk too high]

### 3. Calculate maximum


**Calculate maximum position size:**

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times \text{Risk\%}}{\text{Max Loss Per Contract}}
$$

**For IV strategies, consider:**

- Vega exposure limits ($ per 1% IV move)

- Theta collection goals ($ per day target)

- Gamma risk near expiration

- Capital at risk for defined-risk strategies

**Conservative sizing:**

- Max vega: $100-200 per 1% IV move per $10k capital

- Max theta: $20-50 per day per $10k capital

- Risk 1-2% on undefined risk strategies

- Risk 2-5% on defined risk strategies

### 4. Best practices: 1


**Best practices:**

1. **IV analysis first:** Check IV percentile before entry

2. **Liquidity check:** Ensure tight bid-ask spreads

3. **Multi-leg orders:** Enter complete structure as one order

4. **Timing considerations:** 

   - Sell vol when IV elevated (IVR > 50)

   - Buy vol when IV depressed (IVR < 30)

   - Avoid entering right before events (IV usually elevated)

**Entry checklist:**

- [ ] IV percentile checked

- [ ] Term structure analyzed

- [ ] Liquidity verified (bid-ask < 10%)

- [ ] Position sized appropriately

- [ ] Greeks calculated (delta, vega, theta, gamma)

- [ ] Max loss understood

- [ ] Exit plan defined

### 5. Active management


**Active management rules:**

**IV monitoring:**

- Track IV daily (minimum)

- Monitor IV percentile changes

- Watch term structure shifts

- Alert on IV expansion/contraction

**Profit targets:**

- **For short vol:** Close at 50-75% of max profit

- **For long vol:** Take profit at 100-200% gain

- **For term structure:** Close when term structure normalizes

**Loss limits:**

- **For short vol:** Close at 2-3x credit received

- **For long vol:** Cut at 50% loss

- **Time stop:** Exit if 50% of time passed with no favorable IV move

**Adjustment triggers:**

- IV percentile moves 20+ points

- Term structure inverts unexpectedly

- Underlying makes large move (>2 SD)

- Event announced/cancelled

### 6. When to adjust:


**When to adjust:**

**For short vol strategies:**

- Stock moves significantly against position

- IV expanding beyond entry level

- Risk of max loss approaching

**How to adjust:**

- Roll out in time (collect more theta)

- Roll strikes (move to new delta)

- Convert to different structure (spread to iron condor)

- Close and reenter at better strikes

**For long vol strategies:**

- IV not expanding as expected

- Theta burn exceeding plan

- Realized vol lower than expected

**How to adjust:**

- Scale into more contracts if IV crashes

- Roll to longer dated (reduce theta)

- Take partial profits on IV spikes

- Convert to calendar (neutralize theta)

### 7. Track every


**Track every trade:**

- Entry IV level and percentile

- Term structure shape at entry

- Vega, theta, gamma at entry

- Days to expiration

- P&L by component (vega, theta, gamma)

- Actual IV vs. entry IV

- Lessons learned

**Quarterly review:**

- Win rate by IV percentile

- P&L by term structure shape

- Best entry IV conditions

- Common mistakes

### 8. Common Execution


1. **Selling vol at low IV** - IVR < 30 usually poor for short vol

2. **Buying vol at high IV** - IVR > 70 often too expensive for long vol

3. **Ignoring term structure** - Don't sell front month if in backwardation

4. **Over-leveraging vega** - Too much vega exposure can blow up account

5. **Holding through earnings** - IV crush destroys long vol positions

6. **Not taking profits** - Greed kills short vol profits

7. **Fighting IV trends** - IV regimes can persist

8. **Ignoring skew** - Put skew can make bearish trades expensive

### 9. Professional


**For volatility selling (short vega):**

- Enter when IVR > 50, ideally > 70

- Target 60-70% probability of profit

- Close at 50% of max profit

- Use mechanical stops (2x credit)

**For volatility buying (long vega):**

- Enter when IVR < 30

- Need catalyst for IV expansion

- Take profits quickly on IV spikes

- Cut losses at 50% if IV doesn't cooperate

**For term structure trades:**

- Understand event calendar

- Check historical term structure patterns

- Monitor roll dynamics

- Scale positions gradually

**For skew trades:**

- Understand why skew exists in that stock

- Check historical skew patterns

- Combine with directional view

- Monitor skew changes daily


## Common Mistakes


**Critical errors that destroy IV-RV traders:**

### 1. The error: "VIX


**The error:**
"VIX is at 11. It can't go lower. Time to buy volatility!"

**Example:**

- Date: Mid-2017

- VIX: 11 (30-year lows)

- Trader: "This is unsustainable. Buying VIX calls!"

- Position: 50× VIX $15 calls @ $0.50 = $2,500

**What happened:**

- Month 1: VIX stays 10-11, calls → $0.20 **(-60%)**

- Month 2: VIX at 9.5! (even lower!), calls → $0.05 **(-90%)**

- Month 3: Expires worthless **(-100%)**

**Why it's wrong:**

**"Low VIX" ≠ "Must spike soon"**

**Historical:**

- VIX can stay low for YEARS (2004-2007, 2012-2017)

- VIX went to 9.14 in 2017 (record low!)

- Stayed <12 for 9+ months

**The fix:**

**Don't fight low vol:**

- Low VIX → Market calm (can persist)

- Don't buy vol just because "it's low"

- Wait for catalyst

- Or: Accept it's a secular shift

**When to buy vol:**

- NOT: "VIX is low"

- YES: "Catalyst emerging" (geopolitics, Fed, etc.)

- YES: "Event risk" (election, crisis)

---

### 2. The error: "VIX


**The error:**
"VIX at 12! Free theta! I'll sell straddles all day!"

**Example:**

- January 2018

- VIX: 12 (calm market)

- Trader: Short 20× SPX straddles

- Credit: $100,000

- "VIX can't spike much from here"

**February 5, 2018:**

- **VIX: 12 → 37** (in ONE DAY!)

- Loss: **-$200,000+**

- Margin call

- Account wiped out

**Why it's DEADLY:**

**VIX 12 → 37 = 3× increase!**

**Low VIX = HIGHEST risk for sellers!**

**Historical VIX spikes from low levels:**

- 2015: VIX 12 → 40 (August flash crash)

- 2018: VIX 11 → 50 (February Volmageddon)

- 2020: VIX 13 → 85 (COVID crash)

**Spikes are BIGGER from low VIX!**

**The fix:**

**Never short vol at VIX <13:**

- Below 13 = Danger zone

- Risk/reward terrible (small credit, huge risk)

- Wait for VIX 20+ to short

**Safe shorting:**

- VIX >25 (elevated, will normalize)

- Post-event (earnings, FOMC passed)

- IV percentile >70th

---

### 3. The error: "Stock


**The error:**
"Stock moving a lot (high realized vol). Perfect for selling options (high IV)!"

**Example:**

- Stock: TSLA

- Recent moves: $10/day (40% realized vol)

- Trader: "Volatility is high! Sell straddles!"

- Sells $240 straddle for $30

**Reality:**

- IV: 80% (market pricing in CONTINUED high movement)

- RV: 40% currently

- **But:** RV can go to 80%+ (matching IV!)

**What happened:**

- Week 1: TSLA moves $15/day (RV increases!)

- RV: 40% → 60%

- Still below IV (80%)

- Straddle: $30 → $45 **(-$1,500 loss)**

**Why it's wrong:**

**High RV ≠ Expensive IV!**

**IV prices EXPECTED volatility:**

- If RV = 40%, IV = 80%

- Market expects: RV will INCREASE to 80%!

- Not: RV is high so IV is expensive

**The fix:**

**Compare IV to future RV (forecast):**

- Current RV: 40%

- IV: 80%

- Question: Will RV go to 80%+?

**If YES:** IV is fair (don't short!)  

**If NO:** IV is expensive (short vol!)

**Tool: IV percentile**

- Compare IV to its own history

- 80th percentile IV → Likely to fall

- 30th percentile IV → Not expensive!

---

### 4. The error: "IV is


**The error:**
"IV is 30%, but RV is only 25%. IV is overpriced! Short it!"

**Example:**

- IV: 30%

- Historical RV: 25%

- Spread: 5 points

- Trader: "Free money! Short vol!"

**Reality:**

- **This is the risk premium** (not mispricing!)

- IV SHOULD be higher than RV

- The 5 points = Insurance premium

**What happened:**

- Year 1: RV stays 25%, trader makes money (+5 points)

- Year 2: RV stays 23%, makes money (+7 points)

- Year 3: RV stays 26%, makes money (+4 points)

- **Year 4: BLACK SWAN** RV = 70%!

- **Loss: -40 points** (wipes out 3 years of gains!)

**Why it's wrong:**

**Risk premium exists for a reason:**

$$
\text{Expected: IV} > \text{RV most of the time}
$$

But:
$$
\text{Occasionally: RV} >> \text{IV} \text{ (tail events)}
$$

**The premium compensates for tail risk!**

**The fix:**

**Accept the risk premium:**

- 5-point spread is NORMAL

- Don't short vol just because IV > RV

- Only short when spread is ABNORMALLY large (10-15 points)

**Or:**

- Understand: You're selling insurance

- Sometimes the house burns down

- Size accordingly!

---

### 5. The error:


**The error:**
"Selling vol has high win rate (80%+). I'll use 50% of my account!"

**Example:**

- Account: $100,000

- Strategy: Short vol (iron condors)

- Allocation: $50,000 (50%)

- "Win rate is 85%, I'll compound fast!"

**First 10 months:**

- 8 wins, 2 losses (80% win rate!)

- Average win: $2,500

- Average loss: $5,000

- **Net: 8 × $2,500 - 2 × $5,000 = +$10,000**

- "This works!"

**Month 11 (Black swan):**

- Market crashes

- VIX spikes 12 → 50

- **All positions max loss**

- Loss: **-$50,000**

**Net after 11 months:** -$40,000 (down 40%!)

**Why it's wrong:**

**High win rate ≠ Low risk!**

**Short vol characteristics:**

- Win rate: 70-85%

- Avg win: Small

- Avg loss: LARGE (10× avg win)

**Math:**
$$
E[Return] = 0.8 \times \$2,500 - 0.2 \times \$25,000 = -\$3,000
$$

**Negative expected value with fat tails!**

**The fix:**

**Size for WORST loss, not avg win:**

$$
\text{Max Allocation} = \frac{\text{Account}}{20} \text{ (5% max)}
$$

**Example:**

- $100,000 account

- Max short vol: $5,000

- If wipeout: Only -5%

- **Survivable!**

---

### 6. The error: "I'll


**The error:**
"I'll just sell vol naked. Hedging reduces profits!"

**Example:**

- Strategy: Short 10× iron condors/month

- Monthly credit: $5,000

- Annual: $60,000

- No hedges

**Years 1-3:**

- Average P&L: +$45,000/year (after losses)

- Total: +$135,000

**Year 4 (Black swan):**

- February crash

- VIX 12 → 50

- All positions max loss

- **Loss: -$200,000**

**Net after 4 years:** -$65,000 (negative!)

**With hedge (example):**

**Strategy:**

- Same short vol positions

- BUT: Buy 5% in VIX calls (tail hedge)

- Cost: $3,000/year

**Years 1-3:**

- P&L: +$42,000/year (after hedge cost)

- Total: +$126,000

**Year 4 (Black swan):**

- Short vol losses: -$200,000

- **VIX calls profit: +$180,000** (VIX spiked!)

- Net: -$20,000

**Net after 4 years:** +$106,000 (POSITIVE!)

**The fix:**

**Always hedge tail risk:**

**Hedge options:**

1. **Buy OTM puts** (5% of capital)

2. **Buy VIX calls** (small allocation)

3. **Long vol spreads** (calendar spreads)

**Cost:** 5-10% of expected profits

**Benefit:** Survival in black swans!

---

### 7. The error: "Lost


**The error:**
"Lost $10,000 on short vol. I'll double position size to make it back!"

**Example:**

- Month 1: Short vol, lose $10,000 (VIX spike)

- Trader: "That was unlucky. I'll sell MORE next month!"

- Month 2: Doubles position (20 contracts vs. 10)

**Month 2 outcome:**

- VIX spikes AGAIN (continued volatility)

- **Loss: -$20,000** (double the size = double the loss!)

- Total: -$30,000 (30% of account)

**Why it's wrong:**

**Volatility clusters:**

- High vol → More high vol (not immediate reversion)

- VIX spike → Often followed by continued elevated vol

- Doubling down = Catching falling knife

**The fix:**

**After loss, REDUCE size:**

- Lost $10k → Reduce position 50%

- Wait for vol to normalize

- Then gradually scale back up

**Rule:**
$$
\text{New Size} = \text{Old Size} \times (1 - \text{Loss\%})
$$

Lost 20%? → Reduce size 20%!

---

### 8. The error:


**The error:**
"Earnings are tomorrow. IV is 60%! I'll sell straddles for huge credit!"

**Example:**

- AAPL earnings tomorrow

- IV: 60% (elevated pre-earnings)

- Sell straddle: $35 credit ($3,500)

- "After earnings, IV will crush. Easy money!"

**Earnings night:**

- AAPL beats, but guides lower

- Stock gaps from $180 → $165 **(-8%!)**

- IV doesn't crush (uncertainty remains on guidance)

**Next day:**

- Straddle value: $50

- **Loss: -$1,500** (from $3,500 credit)

- Plus: Assignment risk

**Why it's wrong:**

**Binary events = Unpredictable:**

- Stock can gap beyond strikes

- IV crush not guaranteed

- One wrong earnings wipes out months

**The fix:**

**Never sell vol through events:**

- Exit 1 day before earnings

- Or: Enter AFTER earnings (IV crush)

- Avoid the binary risk

---

### 9. The error: "I'll


**The error:**
"I'll diversify: Short vol on 10 different stocks!"

**Example:**

- Positions: Short vol on AAPL, MSFT, GOOGL, AMZN, TSLA, NVDA, META, NFLX, SHOP, ROKU

- Total: 10 positions

- "Diversified!"

**Market crash:**

- All tech stocks drop together

- **ALL 10 positions: Max loss simultaneously**

- Not diversified at all!

**Why it's wrong:**

**Correlation = 1 in crashes:**

- All stocks drop together

- "Diversification" illusion

- Short vol correlates to MARKET, not stocks

**The fix:**

**True diversification:**

- Different asset classes (stocks, bonds, commodities)

- Different geographies (US, Europe, Asia)

- Different strategies (long vol + short vol)

**Or: Acknowledge**

- Short vol = Short market beta

- Not diversifiable

- Accept concentration risk

---

### 10. The error: "I


**The error:**
"I made 5% last month shorting vol. Too slow! I'll use margin to make 10%!"

**Example:**

- Account: $100,000

- Normal strategy: $5,000/month (+5%)

- With 2× margin: $10,000/month (+10%)

- "Doubling returns!"

**Month 1-5:**

- Working great!

- +$50,000 (50%!)

**Month 6 (Crash):**

- Market crashes

- Positions: 2× size (margin)

- **Loss: -$100,000** (2× the normal max loss)

- **Margin call: Owe broker $20,000**

- Account: Wiped out + debt!

**Why it's wrong:**

**Leverage magnifies BOTH ways:**

- Good times: 2× returns

- Bad times: **2× losses** (wipeout!)

**The fix:**

**NEVER leverage short vol:**

- Already risky enough

- No margin

- Cash-secured only

- Sleep at night!

---

### 11. | | Mistake |


| # | Mistake | Fix |
|---|---------|-----|
| 1 | Buy vol because VIX low | Wait for catalyst, not "low VIX" |
| 2 | Sell vol at VIX <13 | Only short at VIX >20 |
| 3 | Confuse IV with RV | Use IV percentile, not RV level |
| 4 | Ignore risk premium | Accept 5-point spread is normal |
| 5 | Over-size (>10%) | Max 5% of portfolio in short vol |
| 6 | No tail hedge | Spend 5% on VIX calls/OTM puts |
| 7 | Revenge trade after loss | Reduce size after losses |
| 8 | Sell into events | Exit before, enter after |
| 9 | Ignore correlation | True diversification across assets |
| 10 | Use leverage | Cash only, no margin |

**Remember:** IV-RV trading is unforgiving. One mistake can wipe out years of gains. Follow the rules or don't play!

---

## Real-World Examples


**Concrete scenarios showing IV-RV trading in practice:**

### 1. Pension Duration


**Trader profile:**

- Conservative professional

- $500,000 portfolio

- Strategy: Systematic short vol (iron condors)

- Allocation: 10% max ($50,000)

**The rules:**

1. Only short vol when VIX >20

2. Only sell iron condors (defined risk)

3. Exit at 50% profit or -100% loss

4. 5% tail hedge (VIX calls)

5. Max 5 positions simultaneously

**Results by year:**

**2012:** +$22,000 (+4.4% portfolio)  

**2013:** +$28,000 (+5.6%)  

**2014:** +$18,000 (+3.6%) - August flash crash hit  

**2015:** +$15,000 (+3.0%) - Managed Aug/Dec vol spikes  

**2016:** +$32,000 (+6.4%) - Brexit recovered  

**2017:** +$12,000 (+2.4%) - VIX too low, fewer trades  

**5-year total:** +$127,000 (+25.4% total return)  

**Annualized:** ~4.6%/year (conservative but steady)

**February 2018:**

- VIX spike 12 → 37

- Losses: -$15,000 (iron condors hit max loss)

- **BUT:** VIX calls (hedge) +$12,000

- Net: -$3,000 (survived!)

**Lesson:** Conservative sizing + tail hedge = Survival

---

### 2. Transition Risk


**Trader profile:**

- Retail trader, 2 years experience

- $250,000 account (life savings)

- Strategy: Naked short strangles (undefined risk)

- Allocation: 80% (way too much!)

**The thesis:**
"VIX has been 9-12 for months. This is the new normal. Free theta forever!"

**January 2018:**

- Positions: Short 40× SPX strangles

- VIX: 11

- Credit collected: $160,000

- Monthly theta: $12,000

- "Making $12k/month risk-free!"

**Jan 1-Feb 4:**

- Collected: $17,000 theta

- Positions: All profitable

- Account: $250k → $267k

**February 5, 2018 (Volmageddon):**

**12:00 PM:** S&P starts dropping  

**2:00 PM:** VIX 17 → 22, getting nervous  

**3:00 PM:** VIX 22 → 28, **MARGIN CALL!**  

**3:30 PM:** VIX 28 → 37, **LIQUIDATION FORCED**

**Final outcome:**

- Entry credit: $160,000

- Exit cost: $320,000

- **Loss: -$160,000**

- Account: $267k → $107k **(-60%!)**

- Plus: Owed broker $15k for margin

**Post-mortem:**

- Allocation too high (80%)

- No tail hedge

- Undefined risk (naked)

- VIX too low (<13)

- **Perfect recipe for disaster**

**Trader aftermath:**

- Devastated financially

- Quit trading for 2 years

- Eventually returned with 5% allocation rule

---

### 3. Portable Alpha


**Institution profile:**

- Hedge fund, $1 billion AUM

- Strategy: Tail hedge (long VIX futures)

- Allocation: 5% ($50 million)

**Thesis:**
"Market is overextended after 8-year bull run. Protect downside."

**2017 execution:**

**Jan-Dec positions:**

- Rolling long VIX futures (front + 2nd month)

- Average VIX: 10-12 (record lows!)

- Contango cost: Brutal

**Monthly P&L:**

- Jan: -$600k (contango roll)

- Feb: -$550k

- Mar: -$580k

- Apr-Dec: Similar (-$500-600k/month)

**Annual cost: -$6.5 million** (13% of allocation!)

**S&P 500:** +19.4% (no crash, protection useless)

**Investor reactions:**
"We paid $6.5M for zero protection!"

**2018 decision:**

- Reduce tail hedge to 2% ($20M)

- Accept more risk

**February 2018:**

- Volmageddon hits

- Remaining hedge: +$8 million (saved!)

- "If we'd cut all hedges, would've lost on downside"

**Lesson:** Hedges cost money, but prevent disaster. Finding right size is art.

---

### 4. Tactical Duration


**Trader profile:**

- Quantitative analyst

- $200,000 account

- Strategy: Statistical IV vs. RV trading

- Systematic rules

**The strategy:**

1. Calculate IV - RV spread daily

2. If spread >7 points: Short vol (IV overpriced)

3. If spread <2 points: Long vol (IV underpriced)

4. Delta hedge daily

5. Exit when spread normalizes to 5 points

**2015-2017 results:**

**2015:**

- 12 trades

- 9 winners (+$18,000)

- 3 losers (-$6,000)

- **Net: +$12,000 (+6%)**

**2016:**

- 15 trades

- 11 winners (+$24,000)

- 4 losers (-$8,000)

- **Net: +$16,000 (+8%)**

**2017:**

- 18 trades

- 14 winners (+$28,000)

- 4 losers (-$7,000)

- **Net: +$21,000 (+10.5%)**

**3-year total: +$49,000 (+24.5%)**

Annualized: ~7.5%/year (excellent risk-adjusted!)

**February 2018:**

**Feb 1:** Spread = 8 points (IV 20%, RV 12%)  

**Signal:** Short vol

**Feb 5:** Market crashes

- RV spikes to 70%!

- Spread: -50 points (IV underpriced now!)

- **Loss: -$15,000** (position blown up)

**But:**

- Position size: Only 10% of capital

- Stop loss: Triggered at -$15k

- **Account: $249k → $234k** (-6%, survived!)

**Lesson:** Good strategy can still lose. Position sizing saved him.

---

### 5. Duration Hedge


**Retail trader:**

- Strategy: Sell vol AFTER earnings (IV crush trade)

- Stock: NFLX

- Account: $50,000

**Setup:**

- NFLX reports earnings today (after close)

- Current IV: 70% (elevated pre-earnings)

- Thesis: "After earnings, IV will crush to 35-40%"

**Position (WAIT until after earnings):**

- Earnings announced: 8 PM ET

- NFLX beats, stock up 5% after hours

- Next morning: IV 70% → 38% (crushed!)

**Trade (next morning):**

- Sell 5× NFLX iron condors

- IV: 38% (still elevated vs. normal 30%)

- Credit: $2,500

**Week 1:**

- IV: 38% → 33% (normalizing)

- Theta: +$400

- Vega: +$500 (IV drop)

- **P&L: +$900**

**Week 2:**

- IV: 33% → 30% (back to normal)

- **Exit at 75% profit**

- **Total: +$1,875** (75% in 2 weeks!)

**Why it worked:**
✅ Waited AFTER earnings (no binary risk)  
✅ IV still elevated post-earnings (37% vs. 30% normal)  
✅ Defined risk (iron condors, not naked)  
✅ Exited early (75% profit)  
✅ IV continued normalizing

**Annualized (if repeatable):**

- 2 weeks per trade

- 26 trades/year possible

- Average: +$1,500/trade

- Annual: **+$39,000 (+78%!)**

**Reality:** Only ~12 good setups/year = $18,000 (+36%)

**Still excellent!**

---

### 6. Sophisticated


**Sophisticated trader:**

- Strategy: VIX futures term structure arbitrage

- Capital: $500,000

**Setup (Normal markets):**

- VIX spot: 15

- Front month VIX future: 17

- 2nd month: 19

- 3rd month: 21

- **Steep contango** (normal)

**Trade:**

- Short front month VIX futures

- Long 2nd month (or 3rd month)

- Capture roll yield (contango decay)

**Normal month P&L:**

- Front month rolls down: 17 → 15 (converges to spot)

- Profit: 2 points = +$10,000

- Repeat monthly

**2016-2017 results:**

- Average: +$8,000/month (some variation)

- Annual: +$96,000 (19.2% return!)

**February 2018 disaster:**

**Feb 1-4:** Normal

- Contango intact

- Position: Short front (17), Long 2nd (19)

**Feb 5:**

- VIX spot: 15 → 37 (massive spike!)

- Front month: 17 → 40 (explosive move!)

- 2nd month: 19 → 32 (less move)

**P&L:**

- Short front: -23 points = **-$115,000**

- Long 2nd: +13 points = +$65,000

- **Net: -$50,000** (10% of account!)

**Plus:** Curve inverted (backwardation)

- Can't continue strategy

- Forced to close all positions

**Lesson:** Term structure can invert violently. Size for worst case.

---

### 7. Contrarian


**Contrarian trader:**

- 2019-early 2020

- Strategy: Long vol in calm markets

- Thesis: "Market too complacent, protection cheap"

**Setup (Jan 2020):**

- VIX: 13 (calm)

- SPY ATM straddles: Cheap

- IV: 15% (low)

- Buys: 10× SPY straddles @ $15 = $15,000

**Jan-Feb 2020:**

- Market calm, position bleeding

- Loss: -$2,000 (theta decay)

**Late Feb 2020:**

- COVID news emerging

- Market starting to worry

- VIX: 13 → 20

- Position: $13,000 → $24,000 (+$11,000!)

**Early March 2020:**

- Full panic

- VIX: 20 → 85 (historic!)

- Position: $24,000 → $115,000!

**Exit:**

- Sells at $115,000

- **Profit: +$100,000** (+667%!)

**Why it worked:**
✅ Bought when VIX low + cheap  
✅ Catalyst emerged (COVID)  
✅ Held through initial losses  
✅ Exited during panic (not at absolute peak)  
✅ Lucky timing (can't predict black swans)

**Note:** This is RARE. Most long vol bleeds to zero!

---

### 8. Successful IV-RV


**Successful IV-RV trading requires:**

1. **Conservative sizing** (5-10% max)

2. **Defined risk** (iron condors > naked)

3. **Tail hedges** (5% in protection)

4. **Know when NOT to trade** (VIX <13 for shorts)

5. **Discipline** (follow rules, no revenge)

6. **Patience** (wait for setups)

7. **Accept costs** (hedges, theta on long vol)

**Fatal mistakes:**

1. Oversizing (>20%)

2. Undefined risk (naked shorts)

3. No hedges

4. Trading at wrong VIX levels

5. Revenge trading

6. Leverage

**The pattern:**
$$
\text{Success} = \text{Right Sizing} + \text{Right Setup} + \text{Discipline}
$$

**Miss any one → Disaster!**

---

## Real-World Examples


[Concrete IV strategy examples]


## Key Takeaways


- IV usually exceeds RV due to risk premium

- The IV–RV spread is persistent but risky

- Selling volatility earns premium but carries tail risk

- Buying volatility is expensive but convex

- Risk management is essential

---

## One-Line Summary


> **Implied vs realized volatility trading captures the volatility risk premium by betting on how much uncertainty actually materializes versus what the market prices.**