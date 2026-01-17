# Regime-Based


**Regime-based strategy design** recognizes that no single options strategy works well in all market conditions. Instead of forcing one approach across all environments, sophisticated traders classify market states (regimes) and systematically adapt their strategy selection to match the dominant risk channels of each regime.

Greeks quantify exposures; regimes determine whether those exposures are rewarded (realized variance, jump risk, liquidity).

---

## The Core Insight


**The fundamental idea:**

- Markets shift between distinct behavioral **regimes**
- Each regime has different **dominant risk channels**
- Strategies that profit in one regime may fail catastrophically in another
- **The key:** Match your strategy to the current regime, not to historical averages
- Greeks tell you what you're exposed to; regimes tell you if that exposure gets paid

**The critical equation:**

$$
\text{Strategy P\&L} = \text{Greek Exposure} \times \text{Regime Dynamics}
$$

**You're essentially betting: "I've correctly identified the current regime, and my strategy's Greek exposures are aligned with how this regime compensates those risks."**

---

## What Are Market Regimes


### 1. Definition of Market Regimes


A **market regime** is a persistent pattern of market behavior characterized by:
- Realized volatility levels
- Correlation structure
- Skew behavior
- Liquidity conditions
- Risk premium dynamics

**Regimes are not static:** Markets transition between regimes based on macro conditions, policy changes, and structural shifts.

### 2. The Three Core Volatility Regimes


**1. Low Volatility Regime (Grinding):**
- RV: 5-15% annualized
- Skew: Moderate (8-12 points)
- IV/RV ratio: 1.2-1.5 (modest premium)
- Correlations: Low
- Character: Slow grind higher, complacency
- Duration: Can persist 6-18 months

**2. Medium Volatility Regime (Normal):**
- RV: 15-25% annualized
- Skew: Normal (10-15 points)
- IV/RV ratio: 1.3-1.7 (fair premium)
- Correlations: Moderate
- Character: Two-way volatility, mean reversion
- Duration: Typical baseline state

**3. High Volatility Regime (Crisis):**
- RV: 25-80%+ annualized
- Skew: Extreme (20-40 points)
- IV/RV ratio: 0.8-1.2 (sometimes inverted!)
- Correlations: High (everything moves together)
- Character: Sharp moves, gaps, illiquidity
- Duration: Days to months (but feels eternal)

---

## Regime Identification


### 1. Quantitative Indicators


**Primary metrics:**

**Realized Volatility (20-day):**
```
RV < 12%:  Low vol regime
RV 12-20%: Normal regime  
RV > 20%:  High vol regime
```

**VIX Level:**
```
VIX < 15:  Grind regime
VIX 15-25: Normal regime
VIX > 25:  Stress regime
VIX > 40:  Crisis regime
```

**IV Rank (30-day):**
```
IVR < 30:  Sell vol unfavorable
IVR 30-70: Neutral
IVR > 70:  Sell vol favorable
```

**Skew Steepness (25-delta put vs call):**
```
Skew < 5:   Complacency
Skew 5-12:  Normal
Skew > 15:  Fear regime
```

### 2. Regime Transition Signals


**Low → Medium:**
- VIX rising through 15
- RV accelerating
- Correlation pickup
- Skew steepening

**Medium → High:**
- VIX spike above 25
- Gap moves increasing
- Bid-ask spreads widening
- Put demand surge

**High → Medium:**
- VIX declining below 25
- Gaps decreasing
- Liquidity returning
- Skew normalizing

**Medium → Low:**
- VIX compressing below 15
- Tight daily ranges
- Correlation collapse
- Complacency signals

---

## Economic Foundations


### 1. The Core Economic Framework


**Each regime rewards different exposures:**

**Low Volatility Regime:**
- Rewards: Short gamma (theta collection), short vega (IV overpriced)
- Punishes: Long gamma (slow bleed), long vega (IV crushes)
- Why: Market overpays for protection in calm times

**Medium Volatility Regime:**
- Rewards: Tactical directional, selective short vol, term structure trades
- Punishes: Mechanical strategies, over-leveraged positions
- Why: Fair pricing, need selectivity

**High Volatility Regime:**
- Rewards: Long gamma (captures moves), tail hedges
- Punishes: Short gamma (gets run over), naked short vol
- Why: Realized vol exceeds implied, gaps destroy short positions

### 2. Why These Regime Categories Work


**1. Volatility clustering:**
- High vol begets high vol
- Low vol persists
- Transitions are usually rapid

**2. Risk premium dynamics:**
- In calm: Market overpays for insurance → sell vol wins
- In crisis: Market underpays for protection → buy vol wins
- Regime determines sign and magnitude of risk premium

**3. Structural flows:**
- Low vol: Systematic vol sellers dominate
- High vol: Panic buying, forced liquidations
- Flow imbalances create tradable dislocations

### 3. Professional Perspective


**Market makers:**
- Low vol: Happy to sell vol (rich premium, low risk)
- High vol: Charge massive skew, widen markets
- Must adapt inventory management to regime

**Hedge funds:**
- Trend followers: Profit from regime transitions
- Vol arb: Exploit IV/RV relationship per regime
- Tail risk: Position for regime shifts

**Retail traders:**
- Often fight regimes (sell vol in crisis, buy vol in calm)
- Success requires regime awareness
- Position sizing must account for regime risk

---

## Strategy Selection by Regime


### 1. Low Volatility Regime Strategies


**Favored strategies:**
1. **Iron condors** - collect theta, range-bound
2. **Short strangles** - sell rich premium
3. **Covered calls** - enhance yield
4. **Credit spreads** - defined risk premium selling

**Avoid:**
- Long options (theta burn excessive)
- Long straddles (IV too high)
- Wide wings (complacency risk)

**Position sizing:** Conservative (3-5% risk) - blow-ups happen here

### 2. Medium Volatility Regime Strategies


**Favored strategies:**
1. **Directional spreads** - vertical spreads with edge
2. **Calendars** - term structure plays
3. **Butterflies** - precision trades
4. **Selective iron condors** - with statistical edge

**Avoid:**
- Mechanical short vol (no edge)
- Over-leveraging (regime can shift)

**Position sizing:** Moderate (2-3% risk)

### 3. High Volatility Regime Strategies


**Favored strategies:**
1. **Long options** - capture gaps
2. **Debit spreads** - defined risk directional
3. **Long straddles/strangles** - if RV > IV
4. **Ratio backspreads** - tail exposure

**Avoid:**
- Short naked options (assignment risk)
- Iron condors (get blown out)
- Theta collection (gamma risk too high)

**Position sizing:** Aggressive (1-2% risk, but can size up long vol)

---

## Practical Guidance


**Step-by-step implementation framework:**

### 1. Daily Regime Assessment


**Daily regime check:**

1. **Calculate current metrics:**
   - 20-day realized volatility
   - VIX level and term structure
   - IV rank (30-day percentile)
   - Skew (25-delta put - call IV)

2. **Classify regime:**
   ```python
   if VIX < 15 and RV < 12:
       regime = "Low Vol Grind"
   elif VIX > 25 or RV > 25:
       regime = "High Vol Crisis"
   else:
       regime = "Medium Vol Normal"
   ```

3. **Check transition signals:**
   - Is VIX rising or falling?
   - Is skew steepening or flattening?
   - Are correlations increasing?
   - Regime stable or transitioning?

### 2. Entry Criteria by Regime


**Enter regime-appropriate strategies:**

**Low Vol Regime:**
- Short premium when IVR > 50
- Target 60-70% probability of profit
- Wide strikes (2-3 SD)
- Exit at 50% profit
- **Stop:** If VIX spikes above 18 (regime change)

**Normal Vol Regime:**
- Directional plays with technical edge
- Calendars if term structure steep
- Mix of strategies for diversification
- Standard risk management
- **Stop:** Per-trade basis (not regime-driven)

**High Vol Regime:**
- Long gamma for gap protection
- Debit spreads for directional conviction
- Scale into long vol if RV stays elevated
- Aggressive profit taking (vol mean-reverts)
- **Stop:** When VIX drops below 20 (regime normalizing)

### 3. Risk Allocation by Regime


**Risk allocation rules:**

$$
\text{Position Size} = \frac{\text{Capital} \times \text{Regime Risk \%}}{\text{Max Loss per Trade}}
$$

**Regime-based risk allocation:**

**Low Vol (Grind):**
- Max 2-3% per trade
- Concentration risk: Max 15% total short vol
- **Danger:** Complacency breeds blow-ups

**Normal Vol:**
- Standard 2-5% per trade
- Diversify across strategy types
- **Balance:** Mix directional and vol trades

**High Vol (Crisis):**
- Conservative 1-2% per defined risk trade
- Can go 5-10% on long vol if RV > IV
- **Opportunity:** Size up when edge clear

### 4. Regime-Specific Position Management


**Regime-specific entry rules:**

**Low Vol:**
- Wait for IVR > 60 (don't sell vol too early)
- Enter 30-45 DTE
- Use limit orders (markets calm)
- Scale in over days/weeks

**Normal Vol:**
- Standard entry timing
- Match liquidity to position size
- Multi-leg orders at mid or better

**High Vol:**
- Accept wider spreads (urgency matters)
- Market orders okay for long gamma
- Enter quickly when opportunity appears
- Don't wait for "perfect" entry

### 5. Active Regime Monitoring


**Active regime monitoring:**

**Track daily:**
- Current regime classification
- Transition probability
- P&L by regime type
- Strategy performance vs regime

**Management rules:**

**If regime stable:**
- Manage positions per original plan
- Take profits per strategy rules
- Adjust as needed for stock moves

**If regime transitioning:**
- Close mismatched positions immediately
- Don't wait for better price
- Accept small loss to avoid regime mismatch
- **Example:** Short strangles in Low → High transition = close NOW

### 6. When Regime Changes: Transition Protocol


**When regime shifts:**

**Low → High transition:**
1. Close ALL short premium positions
2. Cut position size 50%
3. Switch to long gamma/defined risk
4. Accept transition costs (worth it)

**High → Low transition:**
1. Start scaling out of long vol
2. Test short vol in small size
3. Gradually rebuild normal sizing
4. Don't rush (false dawns common)

**Critical rule:** When regime changes, strategy MUST change. No exceptions.

### 7. Track Performance by Regime


**Track by regime:**
- Total trades per regime
- Win rate per regime
- P&L per regime type
- Regime identification accuracy
- Transition timing quality

**Quarterly review:**
- Which regimes traded best?
- Where did regime calls fail?
- Position sizing appropriate?
- Transition timing good?

### 8. Common Execution Errors


1. **Fighting the regime** - Selling vol in high vol regime
2. **Slow regime recognition** - Staying in wrong strategy too long
3. **Over-trading transitions** - Calling regime changes too frequently
4. **Ignoring regime entirely** - Running same strategy always
5. **Oversizing in wrong regime** - Big short vol in high vol
6. **Under-sizing in right regime** - Small long vol in crisis
7. **Not tracking regime performance** - Can't learn without data
8. **Assuming regime will persist** - All regimes end eventually

### 9. Professional Tips


**For systematic traders:**
- Code regime classifier
- Automate strategy selection
- Backtest by regime
- Track regime transition costs

**For discretionary traders:**
- Daily regime checklist
- Strategy decision tree
- Hard rules for regime changes
- Journal regime calls

**For all traders:**
- Regime determines strategy, not opinion
- Trust the framework over gut feel
- Accept transition costs
- Learn from regime misclassifications

---

## Common Mistakes


### 1. Regime Denial


**The error:**
- VIX at 35, crisis mode
- "I'll keep selling iron condors"
- "Vol will mean-revert soon"
- **Regime mismatch destroys account**

**Fix:**
- Respect current regime
- Don't fight it with predictions
- Adapt strategy immediately
- **Regime IS what it IS, not what you want**

### 2. Over-Trading on Regime Signals


**The error:**
- VIX goes 17 → 19 → 16
- "Regime changed! No wait, back to low vol!"
- Constant position flipping
- **Death by transaction costs**

**Fix:**
- Need significant threshold (VIX >20 or <13)
- Require persistence (3-5 days)
- Don't react to noise
- **Regime changes are rare, not daily**

### 3. Mechanical Rule Following


**The error:**
- "I always trade iron condors"
- Same strategy regardless of regime
- **Works in low vol, destroyed in high vol**

**Fix:**
- Build regime-specific playbook
- Have 2-3 strategies per regime
- Rotate as regime changes
- **Strategy must match regime**

### 4. Ignoring Transition Periods


**The error:**
- In transition from low → high vol
- Keep existing short premium positions
- "They'll probably be fine"
- **Blow through strikes in regime shift**

**Fix:**
- Close mismatched positions immediately
- Accept small loss on transition
- Don't hope for regime reversal
- **Transition days are highest risk**

### 5. Wrong Position Sizing for Regime


**The error:**
- High vol regime (VIX 40)
- Put on 10% of account in iron condor
- "It's defined risk"
- **Max loss realized**

**Fix:**
- Conservative sizing in wrong regime
- Aggressive sizing in right regime match
- 1-2% max in unfavorable regimes
- **Regime determines risk appetite**

### 6. Assuming Mean Reversion


**The error:**
- Low vol regime at VIX 12
- "Vol must spike soon, I'll buy straddles"
- 6 months of theta decay
- **Regimes persist longer than expected**

**Fix:**
- Trade current regime, not expected next regime
- Regimes can last 12+ months
- Wait for actual regime change
- **Don't anticipate, react**

### 7. Not Tracking Regime Performance


**The error:**
- No data on which regimes traded well
- Can't learn from mistakes
- Repeat same errors
- **Never improve**

**Fix:**
- Journal every regime call
- Track P&L by regime
- Review monthly
- **Data-driven regime trading**

---

## Real-World Examples


### 1. Case Study: 2017 Low Vol Regime


**Setup:**
- January 2017: VIX at 11-12
- RV at 6-8%
- Market grinding higher daily
- **Classic low volatility regime**

**Strategy Selection:**
- Sell iron condors on SPY weekly
- 2SD-wide strikes
- Collect $2-3 credit per week
- Position size: 5% of account per trade

**Execution:**

**Month 1-3 (Jan-Mar):**
- VIX stays 10-12
- Weekly iron condors
- Win rate: 92% (11/12 weeks)
- Average profit: $250/week
- **Grinding theta collection**

**Month 4-6 (Apr-Jun):**
- VIX still sub-12
- Continue weekly iron condors
- Win rate: 89% (11/12 weeks)
- Cumulative: +$5,800
- **Regime persisting**

**Month 7-12 (Jul-Dec):**
- VIX remains historically low
- Same strategy all year
- Annual win rate: 90% (47/52 weeks)
- Total profit: **+$12,400 from regime match**
- Minimal drawdown

**Key insights:**
- Low vol regime lasted entire year
- Single strategy worked for 12 months
- Perfect regime identification
- **Regime persistence = consistent profits**

### 2. Case Study: February 2018 Volmageddon


**Setup:**
- Late Jan 2018: VIX at 10
- Short vol ETPs popular
- Massive short premium positions market-wide
- **Low vol regime at extreme**

**The Trade (Classic Error):**
- Short naked strangles on SPX
- Collecting $5,000/week in premium
- VIX 10, seemed safe
- Position: 10% of $200k account

**The Transition:**

**Monday Feb 5:**
- VIX spikes 10 → 17
- Market down 4%
- Strangles down -$8,000
- **Regime changing!**
- Should close here, didn't

**Tuesday Feb 6 (Volmageddon):**
- VIX explodes 17 → 50
- Market down another 4%
- Gap through strikes
- **Strangles down -$35,000**
- Margin call

**Wednesday Feb 7:**
- Forced liquidation
- Total loss: **-$42,000 (21% of account)**
- Could have been -$8k if closed Monday
- **Regime transition + denial = disaster**

**What went wrong:**
- Didn't recognize transition
- Stayed in wrong-regime strategy
- Oversized for regime risk
- **Fighting regime change = catastrophic**

**Lesson:**
- Regime transitions happen fast
- Close mismatched positions immediately
- Accept small loss to avoid large loss
- **Respect regime changes**

### 3. Case Study: COVID-19 Regime Shift


**Setup:**
- March 2020: COVID crash
- VIX at 40-80
- RV at 60%+
- Market gapping daily
- **Classic high vol regime**

**Strategy Selection:**
- BUY puts (long gamma)
- Debit spreads for direction
- Small position sizing (2% per trade)
- Aggressive profit-taking

**Execution:**

**Week 1 (March 9-13):**
- VIX at 45
- Buy SPY $280/$260 put spread @ $8
- SPY gaps down to $250
- Close at $18
- **Profit: $1,000 (125% in 3 days)**

**Week 2 (March 16-20):**
- VIX at 80
- Buy QQQ $180/$160 put spread @ $10
- QQQ to $165
- Close at $14
- **Profit: $400 (40% in 2 days)**

**Week 3-4:**
- Continue buying puts
- Quick profit-taking (vol mean-reverts fast)
- Win rate: 75%
- Total profit: **+$8,200**

**Regime transition:**
- Late March: VIX starts declining
- 80 → 60 → 40
- **Stop buying puts when VIX < 30**
- Switch to neutral strategies

**Key insights:**
- High vol regime favors long gamma
- Quick profit-taking essential
- Size up when regime matches strategy
- **Regime match = explosive returns**

### 4. Case Study: 2022 Rate Hiking Regime


**Setup:**
- Trader runs only iron condors
- "It's my strategy, I'm good at it"
- Ignores regime completely
- **No regime awareness**

**Results by Regime:**

**Low Vol (40% of time):**
- Iron condors work perfectly
- Profit: +$15,000
- Win rate: 88%

**Normal Vol (45% of time):**
- Iron condors okay
- Profit: +$3,000
- Win rate: 62%

**High Vol (15% of time):**
- Iron condors destroyed
- Loss: **-$28,000**
- Win rate: 15%
- Multiple max losses

**Annual result:**
- Net: **-$10,000**
- One good strategy applied blindly
- High vol regime wiped out year of gains
- **Regime ignorance = net loss**

**Fix:**
- Add regime classifier
- Only trade iron condors in low/normal vol
- Switch to long gamma in high vol
- **Could have been +$18k year if regime-aware**

---


