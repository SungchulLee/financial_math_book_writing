# Skew Trading Spreads

## Exploiting Put /


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/skew_trading_spreads_mean_reversion.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Skew trading spreads** focus on exploiting relative mispricing between **put and call implied volatilities across strikes**, rather than trading the absolute level of volatility or the direction of the underlying.





---

## The Core Insight


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/skew_trading_spreads_opportunity.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**The fundamental idea:**

- Implied volatility is **not symmetric across strikes**
- Downside puts usually trade at **higher IV** than upside calls
- This asymmetry is called **volatility skew**
- Skew is structural, but **not constant**
- When skew becomes too steep or too flat, **relative-value trades emerge**

> **Skew trading is not about volatility level — it is about volatility *asymmetry*.**

---

## What Is Volatility Surface Arbitrage?
<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/skew_trading_spreads_premium.png?raw=true" alt="long_call_vs_put" width="700">
</p>

### 1. Definition


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/skew_trading_spreads_returns.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Volatility skew** refers to the systematic difference between implied volatilities of options at different strikes for the same maturity.

Typical equity skew:

```
IV
↑
40% |\
35% | \
30% |  \
25% |   \____
    |___________→ Strike
     OTM P  ATM  OTM C
```

- OTM puts → high IV (crash risk, insurance demand)
- ATM options → lower IV
- OTM calls → lower or moderately increasing IV

---

### 2. Why Skew Exists


Skew is driven by:

- Demand for downside protection
- Institutional hedging flows
- Leverage and margin constraints
- Behavioral fear asymmetry

Skew reflects **market-implied asymmetry in future return distributions**.

---

## Why Skew Becomes


Skew is **persistent**, but:

- It changes magnitude
- It mean-reverts
- It overreacts during stress or events

**Trading opportunity arises when:**

- Put IV is *too rich* relative to calls
- Call IV is *too cheap*
- Historical or model-implied skew relationships break

---

## The Structure and Mechanics
### 1. General Skew


Skew trades are typically:

- Same maturity
- Different strikes
- Long cheap volatility
- Short rich volatility
- Often delta-neutral

> **Long relative IV on one wing, short relative IV on the other.**

---

### 2. Common Skew


### 3. Risk Reversal


\[
\text{Risk Reversal} = \text{Long OTM Call} - \text{Short OTM Put}
\]

- Long upside IV
- Short downside IV
- Strong skew exposure

---

### 4. Put vs Call


- Sell expensive put spread
- Buy cheap call spread
- Delta-hedge

---

### 5. Skewed Butterfly


- Sell rich downside wing
- Buy cheap upside wing
- ATM strike anchors payoff

---

## The Portfolio Construction
\[
\Pi_{\text{skew}} = \sum_i n_i \cdot V(K_i, T, \sigma_i)
\]

Target exposures:

\[
\Delta \approx 0, \quad
\text{Vega}_{\text{down}} < 0, \quad
\text{Vega}_{\text{up}} > 0
\]

---


---

## Economic Foundations
**Understanding what this strategy REALLY represents economically:**

### 1. The Core Economic Logic
This IV strategy involves specific economic trade-offs around volatility exposure. The key is understanding what you're giving up versus what you're gaining in terms of implied volatility positioning.

**Economic equivalence:**

$$
\text{Strategy P\&L} = \text{IV Change Component} + \text{Term Structure Component} + \text{Skew Component}
$$

### 2. Why This IV Structure Exists
Markets create these IV structures because different participants have different:
- Volatility expectations (near-term vs. long-term)
- Risk preferences (convexity vs. theta)
- Event views (known catalysts vs. unknown volatility)
- Hedging needs (portfolio protection vs. income generation)

### 3. The Volatility Risk Premium
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


## The P&L Driver


\[
\text{P\&L} = \sum_i \text{Vega}_i (\sigma_i^{\text{fair}} - \sigma_i^{\text{market}})
\]

Profit comes from **skew normalization**, not direction.

---

## Risk Management Framework
- Control tail risk
- Use spreads instead of naked options
- Hedge delta frequently
- Avoid event-heavy periods
- Define max loss upfront

---

## Relationship to


| Strategy | Dimension |
|--------|-----------|
| Vega trades | Vol level |
| Calendars | Term structure |
| Butterflies | Curvature |
| **Skew trades** | **Put–call asymmetry** |
| Surface arb | Full surface |

---


---



## Practical Guidance for Implementation
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

### 2. Entry Timing and Conditions
**Enter this strategy when:**
- Skew deviates significantly from historical norm (>1.5 standard deviations)
- Put IV / Call IV ratio exceeds historical range
- OTM put IV 15%+ higher than OTM call IV (unusually steep)
- Stock not facing imminent binary event
- Sufficient liquidity in both put and call strikes
- Clear skew mean-reversion pattern in past

**Avoid this strategy when:**
- Skew at historical average (no edge)
- Binary events pending (biotech FDA, M&A rumors)
- Extreme market stress (VIX > 40, skew may stay elevated)
- Illiquid strikes (OI < 500, bid-ask > 15%)
- During earnings week (skew distorted by event)
- Trending market (skew may persist with trend)

### 3. Calculate Maximum Position Size
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

### 4. Best Practices for Entry
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

### 5. Active Management Rules
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


## Common Mistakes and How to Avoid Them
### 1. Assuming Skew


**The error:**
- Skew at 15 points (historically 8-10)
- "This must normalize!"
- Sell expensive puts, buy cheap calls
- **Skew stays elevated for 6 months during bear market**

**Fix:**
- Check market regime first
- In downtrends, skew stays steep
- Only trade skew compression in calm/bullish regimes
- **Skew is regime-dependent, not purely mean-reverting**

### 2. Ignoring


**The error:**
- "I'm trading skew, not direction"
- Sell OTM puts, buy OTM calls
- Stock drops 10%
- Puts blow through, skew irrelevant

**Fix:**
- Risk reversals have delta exposure
- Size positions for directional risk too
- Monitor both skew AND stock price
- **Can't ignore delta just because trading skew**

### 3. Wrong Strike


**The error:**
- Using ATM strikes for skew trade
- "Maximum vega sensitivity here"
- But ATM skew is minimal
- **Missing the actual skew differential**

**Fix:**
- Use OTM strikes (10-20 delta)
- That's where skew is steepest
- True skew traders focus on wings
- **Real skew is in the tails**

### 4. Insufficient Skew


**The error:**
- Skew at 11 points, normal is 10
- "1 point edge, I'll trade it"
- After costs, no real edge

**Fix:**
- Need 1.5-2 standard deviations from normal
- Minimum 3-5 point skew deviation
- Factor in bid-ask spreads
- **Only trade significant dislocations**

### 5. Not Checking


**The error:**
- "This skew looks steep to me"
- No historical data
- Turns out it's normal for this stock

**Fix:**
- Calculate 1-year skew average and std dev
- Check skew percentile (like IV percentile)
- Some stocks naturally have steeper skew
- **Know what's normal vs abnormal**

### 6. Holding Too Long


**The error:**
- Skew compresses partially
- Up 50%, want 100%
- Skew re-steepens on market dip
- Give back all gains

**Fix:**
- Take profits at 50-75% of max
- Skew can reverse quickly
- Don't be greedy on relative value trades
- **These are mean-reversion trades, not trends**

### 7. Over-Leveraging


**The error:**
- "Low risk, it's just relative mispricing"
- Put on 20% of account
- Skew persists, directional move
- **Massive loss**

**Fix:**
- Risk 1-3% per skew trade maximum
- These trades can still blow up
- Diversify across multiple skew trades
- **Respect that "relative" doesn't mean safe**



---

## Real-World Examples


### 1. Pension Duration


**Setup (March 2020 Recovery):**
- SPY at $350, recovering from COVID crash
- Market panic subsiding but skew still elevated
- OTM put IV: 45% (extreme fear premium)
- OTM call IV: 22% (no one wants upside)
- **Skew differential: 23 points (3 std dev above normal 10-point average)**
- Historical pattern: Skew compresses as markets stabilize

**The Trade:**
- Sell $330 puts (20 delta) @ $8.50 (IV 45%)
- Buy $370 calls (20 delta) @ $4.20 (IV 22%)
- **Net credit: $4.30 per contract**
- 5 contracts, expecting skew normalization

**Management:**

**Week 1-2:**
- Market continues recovery, SPY $350 → $365
- Fear premium declining
- Put IV: 45% → 38%
- Call IV: 22% → 26%
- **Skew: 23 → 12 points (compressing as expected)**

**Week 3:**
- SPY stabilizes $365-$370
- Put IV: 38% → 32%
- Call IV: 26% → 28%
- **Skew: 12 → 4 points (near normal!)**
- Short puts: Worth $2.50 (far OTM + IV dropped)
- Long calls: Worth $6.00 (slightly ITM + IV rose)
- **Position value: -$2.50 + $6.00 = +$3.50 gain**

**Exit at Day 21:**
- Close entire position
- **P&L:**
  - Credit collected: $4.30
  - Current value: $3.50 profit
  - **Total: $7.80 × 100 × 5 = $3,900 profit**
  - **ROI: 181% on $4,300 credit in 21 days**

**Why it worked:**
- Skew was abnormally steep from panic
- Market regime shifted from crisis to recovery
- Both vega AND delta worked in our favor
- **Perfect skew mean-reversion setup**

### 2. Transition Risk


**Setup (September 2022):**
- QQQ at $300 during Fed tightening
- Skew looks elevated at 14 points (normal 9-10)
- "Should mean-revert"
- Ignored that we're in bear market regime

**The Trade:**
- Sell $285 puts @ $6.00 (IV 35%)
- Buy $315 calls @ $3.50 (IV 21%)
- **Net credit: $2.50 per contract**
- 10 contracts

**What went wrong:**

**Week 1:**
- Fed announces more hikes than expected
- QQQ drops $300 → $285
- Skew STEEPENS instead of normalizing
- Put IV: 35% → 42%
- Call IV: 21% → 18%
- **Skew: 14 → 24 points (went wrong way!)**

**Week 2:**
- Recession fears intensify
- QQQ at $275 (puts breached)
- Put IV: 42% → 48%
- Skew: 24 → 30 points
- **Disaster unfolding**

**Exit forced at Day 12:**
- Short puts: Deep ITM, worth $12.00
- Long calls: Worthless, $0.50
- **Loss:**
  - Credit: $2.50
  - Position cost to close: -$12.00 + $0.50 = -$11.50
  - **Net: ($2.50 - $11.50) × 100 × 10 = -$9,000 loss**
  - **18% of $50,000 account**

**Lessons learned:**
- Don't trade skew compression in bear markets
- Skew stays steep when fear is justified
- Should have had 50% stop loss
- **Market regime > statistical mean reversion**

### 3. Portable Alpha


**Setup (January 2024):**
- AAPL earnings in 5 days
- Earnings skew: Puts bid up for protection
- Put IV: 58%, Call IV: 52%
- Normal AAPL skew: 6-8 points
- Earnings skew: 6 points (actually flatter than normal!)

**The Trade:**
- Buy $175 puts @ IV 58% for $4.50
- Sell $185 calls @ IV 52% for $4.00
- **Net debit: $0.50 per contract**
- 20 contracts (small risk)
- Betting on normal skew re-establishing post-earnings

**Post-earnings:**
- AAPL beats, stock to $182
- IV crush: Puts 58% → 24%, Calls 52% → 22%
- Normal skew re-emerges: 2-point differential
- Put IV still slightly higher (structural)

**Outcome:**
- Puts: Worth $1.00 (some value left)
- Calls: Worth $0.80 (OTM but close)
- **Position worth: $1.00 - $0.80 = $0.20**
- Lost most of $0.50 debit
- **Small loss: -$600 (minor)**

**Why minimal profit:**
- Both puts and calls crushed in IV
- Directional move favored short calls
- **Skew play harder around earnings (IV crush dominates)**

**Lesson:** Skew trades work better in non-event periods. During binary events, absolute IV changes overwhelm relative skew changes.

### 4. Tactical Duration


**Approach:**
- Run skew compression trades systematically
- Monthly positions on SPY
- Only enter when skew > 1.5 std dev from mean
- Always 5% position size maximum

**12-month results:**
```
Month | Skew Entry | Trade P&L | Notes
------|------------|-----------|-------
Jan   | 15 (steep) | +$2,400  | Compressed to 9
Feb   | 11 (normal)| No trade | Skipped
Mar   | 18 (steep) | +$3,100  | Post-bank crisis
Apr   | 12 (normal)| No trade | Skipped
May   | 16 (steep) | -$1,800  | Stayed steep
Jun   | 10 (normal)| No trade | Skipped
Jul   | 14 (steep) | +$1,900  | Normalized
Aug   | 13 (mildly)| No trade | Skipped
Sep   | 19 (steep) | -$2,200  | Bear market
Oct   | 11 (normal)| No trade | Skipped
Nov   | 17 (steep) | +$2,600  | Recovery
Dec   | 12 (normal)| No trade | Skipped

Trades: 6
Winners: 4 (67%)
Losers: 2 (33%)
Total P&L: +$6,000
Average win: +$2,500
Average loss: -$2,000
```

**Key insights:**
- Disciplined entry criteria (>1.5 std dev)
- Skip "normal" skew months
- Win rate 67% on skew compression
- Average win > average loss
- **Patient, systematic approach profitable**


## Key Takeaways and Summary
- Skew trading is **relative-value volatility trading**
- Downside IV is structurally rich
- Delta management is essential
- Skew mean-reverts, but not always quickly

---

## One-Line Summary


> **Skew trading spreads exploit distortions in put–call implied volatility by trading asymmetry rather than volatility level.**