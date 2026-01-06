# Event Calendar Spreads
## Trading Event-Driven Volatility Dislocations

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/event_calendar_spreads_by_event.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Event calendar spreads** exploit differences in implied volatility **before and after discrete events** such as earnings, economic releases, or policy announcements.

These strategies trade **when volatility occurs**, not whether price goes up or down.





---

## The Core Insight

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/event_calendar_spreads_exit_timing.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**The fundamental idea:**

- Certain events create **localized volatility**
- Options expiring before an event embed **event risk**
- Options expiring after the event embed **less or diluted event risk**
- This creates **term-structure distortions** around the event
- Calendar spreads can isolate and trade this mismatch

> **You are trading the market’s pricing of *when* volatility will occur.**

---

## What Is Event Volatility?

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/event_calendar_spreads_payoff.png?raw=true" alt="long_call_vs_put" width="700">
</p>

### 1. Discrete Events

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/event_calendar_spreads_timing.png?raw=true" alt="long_call_vs_put" width="700">
</p>

Events that materially affect prices over short horizons:

- Earnings announcements
- CPI / inflation releases
- FOMC decisions
- Product launches
- Court rulings or regulatory decisions

These events create:
- Sudden jumps
- Volatility clustering
- Sharp implied volatility differences across maturities

---

### 2. Event vs Non-Event Volatility

For a known event at time $t_E$:

- Options expiring **before** $t_E$: no event risk
- Options expiring **just after** $t_E$: full event risk
- Longer-dated options: event risk **averaged out**

This creates a **kink** in the term structure.

```
IV
↑
50% |        ●  (post-event)
40% |      ●
30% |   ●
20% | ●
    |________________→ Time
        pre     post
        event   event
```

---

## Why Event Volatility Is Tradable

Event-related IV is often:

- Overestimated (fear premium)
- Poorly distributed across maturities
- Mean-reverting immediately after the event

**Opportunities arise when:**

- Front-month IV is excessively inflated
- Back-month IV underprices event impact
- The market misprices event magnitude or timing

---

## The Structure

### 1. General Event Calendar Construction

Event calendar spreads typically:

- Use **same strike**
- Use **different expirations**
- Sell event-rich volatility
- Buy event-diluted volatility

> **Sell concentrated uncertainty, buy diversified uncertainty.**

---

### 2. Common Event Calendar Structures

### 3. Classic Earnings Calendar Spread

\[
\text{Calendar} = +C(K, T_{\text{after}}) - C(K, T_{\text{before}})
\]

(or puts)

- Sell option expiring right after earnings
- Buy longer-dated option
- Delta-neutral near strike

---

### 4. Double Calendar Around Events

- Calendar spreads at multiple strikes
- Covers a price range
- Reduces directional sensitivity

---

### 5. Reverse Calendar (Event Underpricing)

- Buy near-term event volatility
- Sell longer-dated volatility
- Used when market underestimates event risk

---

## The Portfolio

\[
\Pi_{\text{event}} = V(K, T_{\text{after}}, \sigma_{\text{after}})
- V(K, T_{\text{before}}, \sigma_{\text{before}})
\]

Managed such that:

\[
\Delta \approx 0
\]

Primary exposure is to **relative IV across maturities**.

---


---

## Economic Interpretation

**Understanding what event calendar spreads REALLY represent economically:**

### 1. The Core Economic Insight

Event calendar spreads trade a fundamental market phenomenon:

$$
\boxed{\text{Event-Driven Volatility} > \text{Background Volatility}}
$$

**The economic reality:**

Options expiring right after earnings/events are priced for:
- **Binary outcome risk** (beat or miss)
- **Gap risk** (overnight jumps)
- **Uncertainty premium** (fear of unknown)

Options expiring later dilute this risk over time:
- Event risk **averaged** with normal market noise
- Lower volatility per day remaining
- **Less expensive** per unit of variance

**The arbitrage:**

$$
\text{Calendar Spread Profit} = \text{Event IV Premium} - \text{Diluted Event IV}
$$

### 2. Why Event IV Premiums Exist

**Economic foundation - The Insurance Market for Binary Events:**

**Hedgers (buyers) pay for event protection:**
- Earnings holders: Long stock, can't sell before earnings
- Market makers: Short options, need protection
- Institutional portfolios: Can't react instantly

**Sellers collect premium for taking event risk:**
- Accept gap risk
- Accept binary outcome
- Accept volatility of volatility

**Empirical fact:** Event IV overprices realized moves by 20-40% on average.

**Example data (Earnings):**

$$
\text{Implied Move} = \sigma_{\text{event}} \times \sqrt{T} \times S
$$

For typical earnings:
- Implied move: 8-12% (priced in options)
- Actual average move: 6-8% (realized)
- **Overprice: 25-40%**

**Why the persistent overprice:**

1. **Negative skewness:** Big misses hurt more than beats help
2. **Outliers:** Occasional 20-30% moves justify premium
3. **Liquidity premium:** Hard to exit near event
4. **Model risk:** Dealers charge extra for event risk

### 3. The Term Structure Distortion

**Normal volatility term structure:**

$$
\sigma_{\text{1M}} \approx \sigma_{\text{3M}} \approx \sigma_{\text{6M}}
$$

**Around events (earnings):**

```
IV
↑
80% |           ●  (week after earnings)
    |          ╱
60% |        ●   ← Event premium
    |      ╱
40% |    ●      ● ● ● ● (months later, normalized)
20% |  ●
    |___________________________→ Time to Expiration
      Pre-   Post-  +2wk  +1mo  +2mo
      Event  Event
```

**Economic interpretation:**

$$
\text{Post-Event IV} = \text{Event Risk} + \text{Normal Volatility}
$$

$$
\text{Later IV} = \frac{\text{Event Risk}}{\sqrt{n}} + \text{Normal Volatility}
$$

Where $n$ = days between now and event.

**Event risk gets diluted by square root of time.**

**The kink:** 

Sharp IV jump right at event expiration:
- 1 day before earnings: IV 30% (no event risk)
- 1 day after earnings: IV 80% (full event risk)
- **Kink: 50 percentage point jump** in term structure

**Calendar spread captures this kink.**

### 4. The Post-Event IV Collapse Economics

**What happens after event:**

**T-1:** Uncertainty maximum, IV 80%
**T+1:** Event known, uncertainty resolved

$$
\text{IV Collapse} = \sigma_{\text{pre-event}} - \sigma_{\text{post-event}}
$$

**Typical earnings example:**

Pre-earnings (1 day before): IV = 85%
Post-earnings (1 day after): IV = 32%
**Collapse: 53 percentage points in 24 hours**

**Economic driver:** Information revelation

Before: Market doesn't know earnings
- Wide range of possible outcomes
- Option value = weighted average of scenarios
- **High uncertainty = high IV**

After: Market knows earnings
- Specific outcome realized
- Only residual uncertainty remains
- **Certainty = low IV**

**This collapse is predictable and tradable.**

### 5. Calendar Spread as Volatility Timing Arbitrage

**Economic structure:**

**Position:**
- Short front-month (high IV, event risk)
- Long back-month (lower IV, diluted event)

**Bet:**
- Front IV collapses after event
- Back IV stays stable (has more time)
- **Net profit from convergence**

**P&L decomposition:**

$$
\text{P&L} = \underbrace{\text{Vega}_{\text{short}} \times \Delta IV_{\text{short}}}_{\text{Event collapse (profit)}} + \underbrace{\text{Vega}_{\text{long}} \times \Delta IV_{\text{long}}}_{\text{Stable (neutral)}} + \underbrace{\Theta \times \Delta t}_{\text{Time decay}}
$$

**Typical magnitudes:**

Short front (sell 1-week 60 IV call):
- Event happens, IV → 30
- Vega P&L: +$4,000 per contract

Long back (buy 4-week 38 IV call):
- IV changes 38 → 36 (modest)
- Vega P&L: -$500 per contract

Theta (time decay): +$200
**Net: +$3,700 per spread**

### 6. The Market-Making Perspective

**Why dealers quote wide spreads on event calendars:**

**Risk for dealer selling event calendar to customer:**

1. **Gamma risk near event:** Stock gaps, can't hedge
2. **Vega risk:** IV changes unpredictably
3. **Model risk:** Don't know how IV will collapse
4. **Inventory risk:** Hard to offset with other customers

**Dealer compensation:**

- Bid-ask spread: 10-20% of mid price (wide!)
- Plus: Charge extra on event dates
- Result: **Customer pays significant entry/exit cost**

**Economic implication:** 

You need event IV to collapse by **more than spread** to profit.

Example:
- Spread cost: $200 (bid-ask)
- Need IV collapse: >10 points
- **Only profitable if actual collapse >10 points**

### 7. The Volatility Risk Premium in Events

**Decomposing total volatility:**

$$
\sigma_{\text{total}}^2 = \sigma_{\text{baseline}}^2 + \sigma_{\text{event}}^2
$$

**Baseline:** Normal market variance (15-20% for stocks)
**Event:** Incremental variance from earnings/news

**Historical analysis (earnings):**

Implied event variance: 0.04 (20% event vol)
Realized event variance: 0.025 (15.8% event vol)
**Event VRP: 0.015 (4.2% vol points)**

**Annualized:**

4 earnings/year × 4.2% event VRP = **16.8% annual VRP** from events alone!

**Economic interpretation:**

Earnings options sellers collect massive premium:
- Higher than regular volatility premium
- Concentrated in 4 days/year
- **But take binary risk**

Calendar spreads harvest this premium with **less binary risk** (have back-month protection).

### 8. Behavioral Economics of Event Trading

**Why investors overpay for event protection:**

**1. Ambiguity aversion:**
- Known unknowns (earnings time) > unknown unknowns
- Paradox: More certain about timing → Pay MORE for protection
- Ellsberg paradox in action

**2. Recency bias:**
- Last earnings: Stock dropped 15%
- Investors: "Could happen again!"
- Overpay for protection
- **Most earnings: Normal 6-8% move**

**3. Prospect theory:**
- Losses hurt 2× more than gains
- Willing to pay extra to avoid loss
- **Creates event premium**

**4. Salience:**
- Earnings dates marked on calendar
- Everyone knows it's coming
- Attention → Higher demand → Higher IV
- **Behavioral premium**

**Economic result:**

Event options priced by fear, not fundamentals.
- Rational pricing: Match realized distribution
- Actual pricing: 20-40% too high
- **Opportunity for calendar spread traders**

### 9. Dispersion Around Events

**Index vs. Single Stock dynamics:**

**Single stock earnings:**
- Idiosyncratic news (company-specific)
- High dispersion (winners and losers)
- **Large IV premium**

**Index events (FOMC, CPI):**
- Systematic risk (affects all stocks)
- Correlation spikes
- **Lower relative premium** (everyone moves together)

**Economic opportunity:**

$$
\text{Single Stock Event Premium} > \text{Index Event Premium}
$$

**Reason:** Idiosyncratic risk not diversifiable
- Index: Can hedge with futures
- Single stock: Must hold through event
- **Single stock event calendars more profitable**

### 10. The Timing Value of Information

**Economic value of knowing WHEN:**

**Uncertain timing:** Volatility spreads across days
**Known timing:** Volatility concentrated on specific day

**Example - FDA approval:**

Unknown timing: Decision "sometime in Q2"
- Volatility: 50% for entire quarter
- Value: Averaged over 60 days

Known timing: Decision announced June 15
- Volatility: 120% for June 15 expiry
- Value: Concentrated in 1 day

**Calendar spread captures:**

$$
\text{Value} = \text{Concentrated Vol} - \text{Averaged Vol}
$$

**This is pure timing value** - you profit from knowing when information arrives.

### 11. Professional Institutional Use Cases

**1. Earnings Trading Desks**

**Strategy:** Systematic event calendar program
- Trade 50-100 stocks per quarter
- Short pre-earnings calendars
- Collect event premium systematically

**Economics:**
- Win rate: 65-70%
- Average profit: $2-3K per spread
- Volume: 200 spreads/quarter
- **Annual profit: $400-600K** (on $5M capital)

**2. Volatility Arbitrage Funds**

**Strategy:** Relative value across term structure
- Long event calendars when IV kink excessive
- Short event calendars when IV kink insufficient
- Market-neutral across stocks

**3. Market Makers**

**Usage:** Event risk management
- Customers want event protection
- Dealer sells front-month puts
- **Hedges with calendar spreads**
- Transfers event risk to back month

**4. Corporate Insiders**

**Problem:** Know good/bad news, can't trade stock
**Solution:** Trade calendar spreads (legal!)
- Don't express directional view
- Just trade volatility timing
- **Harvest event premium while compliant**

### 12. Economic Comparison to Alternatives

**Calendar spread vs. Outright short:**

| Metric | Short Front Only | Calendar Spread |
|--------|------------------|-----------------|
| **Premium collected** | $6/contract | $3/contract |
| **Gap risk** | Unlimited | Limited (have back month) |
| **Margin requirement** | High | Low |
| **Event risk** | 100% exposed | 40% exposed |
| **Theta** | High (+$0.20/day) | Medium (+$0.08/day) |
| **Risk/Reward** | High/High | Medium/Medium |

**Economic choice:** Calendar spread = **insurance on your insurance selling.**

### 13. The Zero-Sum Game Dynamics

**Who's on other side of event calendar trades?**

**You (short calendar):** Bet event IV overpriced
**Counterparty (long calendar):** Hedgers, speculators, volatility buyers

**Economic transfer:**

If realized move < implied move:
- You win: Collected overpriced premium
- They lose: Paid too much for protection

If realized move > implied move:
- You lose: Underpriced the risk
- They win: Protection paid off

**Historical edge:** 

65-70% of time, realized < implied
**Long-run:** Sellers win through VRP collection

### 14. Summary

**Event calendar spreads exist because:**

1. **Event uncertainty creates IV premiums** (fear of binary outcomes)
2. **Premiums decline with time** (square root dilution)
3. **Information revelation collapses IV** (post-event certainty)
4. **Behavioral biases amplify premiums** (ambiguity aversion, recency)
5. **Term structure kinks are tradable** (capture timing value)
6. **Dealers need hedging tools** (transfer event risk across time)

**The core economic bet:**

$$
\boxed{\text{Market overprices WHEN volatility happens more than HOW MUCH}}
$$

**Calendar spreads isolate timing premium and harvest it systematically.**

**Professional traders view event calendars as:**
- High Sharpe ratio strategy (win rate 65-70%)
- Capital efficient (defined risk)
- Scalable (many events per quarter)
- Orthogonal to direction (market-neutral)

**The edge comes from:** Being willing to take event risk with back-month protection, while behavioral investors overpay for front-month event protection.




## The P&L Formula

### 1. Primary P&L Driver

\[
\text{P\&L}_{\text{event}} =
\text{Vega}_{\text{near}} \cdot \Delta\sigma_{\text{near}}
+
\text{Vega}_{\text{far}} \cdot \Delta\sigma_{\text{far}}
\]

Typical pattern:

- Near-term IV collapses after event
- Far-term IV changes modestly
- Net profit from **front-month IV crush**

---

### 2. Secondary Effects

- **Theta:** Usually positive
- **Gamma:** Concentrated near event
- **Delta:** Must be actively managed

---

## Concrete Example

### 1. Earnings Calendar Spread

**Stock:** XYZ  
**Spot:** $100  
**Earnings:** In 12 days

**IVs:**

- 2-week ATM call: 65%
- 6-week ATM call: 38%

---

### 2. Trade Construction

- Sell 2-week ATM call
- Buy 6-week ATM call
- Delta hedge

---

## Risk Management

### 1. Key Risks

- Gap risk at the event
- Incorrect event magnitude
- Liquidity near expiration
- Assignment risk
- Volatility regime shifts

---

### 2. Risk Controls

- Use defined-risk calendars
- Avoid extremely short-dated options
- Size conservatively
- Close before expiration if needed
- Diversify across events

---

## Relationship to Other Volatility Strategies

| Strategy | Primary Dimension |
|--------|-------------------|
| IV–RV trading | Volatility premium |
| Mean reversion | Volatility level |
| Skew trading | Strike asymmetry |
| **Event calendars** | **Timing of volatility** |
| Surface arbitrage | Full surface |

> **Event calendar spreads trade *when* volatility happens, not how much.**

---

## When Event Calendars Work Best

✅ Known, scheduled events  
✅ Liquid single-name options  
✅ Moderately elevated IV  
✅ Stable macro backdrop  

❌ Surprise events  
❌ Extreme crisis regimes  
❌ Illiquid names  
❌ Very short expirations  

---


---

## Worst Case Scenario

**What happens when everything goes wrong:**

### 1. The Nightmare Setup

**How it starts:**
- [IV moves against position]
- [Term structure inverts unexpectedly]
- [Unexpected catalyst emerges]
- [Position deteriorating rapidly]

**The deterioration:**

**Week 1:**
- [Early warning signs in IV]
- [Position losing value]
- [IV percentile moving adversely]
- [Critical decision point: hold or fold?]

**Through expiration:**
- [Continued adverse IV dynamics]
- [Maximum loss approached/realized]
- [Final devastating outcome]

### 2. Maximum Loss Calculation

**Worst case mathematics:**

For defined risk IV strategies:

$$
\text{Max Loss} = \text{Debit Paid} \quad \text{(for debit strategies)}
$$

$$
\text{Max Loss} = \text{Spread Width} - \text{Credit} \quad \text{(for credit strategies)}
$$

For undefined risk IV strategies:

$$
\text{Max Loss} = \text{Unlimited} \quad \text{(naked short positions)}
$$

**Example calculation:**
- Position: [Specific IV structure]
- Entry IV: [Level and percentile]
- Adverse scenario: [What went wrong]
- **Loss: [Calculation]**
- **Impact: [% of portfolio]**

### 3. What Goes Wrong

The worst case occurs when:

**For short volatility strategies:**
1. **Wrong IV direction:** IV explodes instead of contracting
2. **Wrong timing:** IV spike happens immediately
3. **Wrong magnitude:** IV move much larger than expected
4. **Black swan:** Unpredicted major event (crash, war, etc.)

**For long volatility strategies:**
1. **Wrong IV direction:** IV crushes instead of expanding
2. **Wrong timing:** Theta decay faster than IV gain
3. **Wrong catalyst:** Expected catalyst doesn't materialize
4. **IV collapse:** Sudden IV crush (post-earnings, resolution of uncertainty)

**For term structure strategies:**
1. **Term structure inversion:** Front month IV explodes relative to back
2. **Event surprise:** Unexpected event distorts normal term structure
3. **Roll dynamics:** Unfavorable roll yield
4. **Gamma explosion:** Front month gamma blows up

### 4. The Cascade Effect

**Multiple compounding failures:**

**Trade 1: Initial short vol loss**
- Sold premium at IVR 60 (thought it was high enough)
- Market crashes, IV explodes to IVR 100
- Loss: $2,000 (max loss on position)

**Trade 2: Panic adjustment**
- Roll position out and down
- Pay $500 to roll
- Market continues lower
- Loss: Another $1,500

**Trade 3: Desperation**
- Double position size to "average down"
- IV continues high
- Assignment risk at expiration
- Loss: $3,000

**Total damage:**
- Cumulative loss: $7,000
- Portfolio impact: 14% of $50k account
- Emotional damage: Severe
- Time to recover: Months

### 5. Real Disaster Scenarios

**Short volatility blow-up (February 2018 Volmageddon):**
- VIX inverse products imploded
- XIV (short vol ETN) lost 90%+ in one day
- Selling vol when VIX at 10-12
- VIX spiked to 50+
- Traders who sold naked vol destroyed
- **Many accounts wiped out entirely**

**Long volatility decay (2017):**
- Bought VIX calls expecting volatility
- VIX stayed suppressed entire year (8-12 range)
- Theta decay relentless month after month
- Traders lost 50-80% waiting for vol spike
- **Death by a thousand theta cuts**

**Term structure inversion (COVID March 2020):**
- Calendar spreads assumed normal term structure
- Front month IV exploded relative to back month
- Term structure inverted violently
- Calendar spreads lost 200-300%
- **"Safe" calendar spreads destroyed**

**Earnings IV crush disaster:**
- Bought straddle into earnings at IVR 90
- IV was 80% before earnings
- Earnings came, stock moved 5% (decent move)
- But IV crushed to 30%
- Straddle lost 40% despite stock moving
- **Directionally right, still lost big**

### 6. The Gamma Blow-Up

**Worst case for short vol at expiration:**

**Friday 3:00pm:**
- Stock at $100.00
- Short $100 straddle (naked)
- Thought it would expire worthless
- **Net delta: 0, everything looks safe**

**Friday 3:59pm:**
- Stock drops to $99.50
- Puts now ITM
- **Net delta: -10,000 shares (100 contracts)**

**Monday morning:**
- Gap down to $95
- Must cover 10,000 shares at market
- Slippage on assignment
- **Loss: $45,000 on what was $2,000 credit**

**This is pin risk + gamma explosion at expiration**

### 7. IV Regime Persistence

**The long grind:**

**Month 1:** Sold vol at IVR 50, expecting mean reversion
- IV stays elevated, position down 30%

**Month 2:** Rolled position, paid debit
- IV still elevated, position down 50%

**Month 3:** Rolled again, more debit
- IV finally normalizing but already lost 60%

**Month 4:** Position finally profitable
- Net result: -40% over 4 months

**The lesson:** IV regimes can persist much longer than you can stay solvent. Mean reversion is real but timing is impossible.

### 8. Psychology of IV Losses

**Emotional stages:**
1. **Confidence:** "IV is too high, easy short"
2. **Concern:** "IV going up but it'll revert"
3. **Denial:** "This is temporary, just need to wait"
4. **Panic:** "Close everything NOW!"
5. **Capitulation:** "I'll never trade vol again"
6. **Learning:** "What did I miss about IV regimes?"

**Winning trader mindset:**
- Respect IV percentile religiously
- Accept that IV can stay irrational
- Cut losses mechanically
- Don't fight IV regime changes
- Learn and adapt

### 9. Preventing Worst Case

**Risk management strategies:**

**1. Position sizing by vega exposure:**
```
Max vega = $100-200 per 1% IV move per $10k capital
If position has $500 vega → 2.5-5% of $50k account max
```

**2. IV percentile discipline:**
```
Only sell vol when IVR > 50 (preferably > 70)
Only buy vol when IVR < 30
No exceptions
```

**3. Mechanical stops:**
```
Short vol: Close at 2-3x credit received
Long vol: Close at 50% loss
Calendar: Close at 50% loss
```

**4. Diversification:**
```
Multiple underlyings
Different expiration cycles
Mix of IV strategies
Never all-in on one IV bet
```

**5. Defined risk structures:**
```
Prefer spreads to naked options
Iron condors > short strangles
Butterflies > naked shorts
Accept lower profit for capped risk
```

**6. Event awareness:**
```
Know earnings dates
Monitor VIX levels
Track macro events
Avoid vol selling before major events
```

### 10. The Ultimate Protection

**Hard rules for IV trading:**

$$
\text{Position Vega} < \frac{\text{Portfolio} \times 0.02}{\text{1\% IV Move}}
$$

$$
\text{If IVR} < 30: \text{No short vol positions}
$$

$$
\text{If IVR} > 70: \text{Be cautious with long vol}
$$

$$
\text{Max Loss} < 5\% \text{ of portfolio}
$$

**Remember:** The market can remain irrational (high/low IV) longer than you can remain solvent. One bad IV trade can wipe out months of profits. Proper position sizing and discipline determine survival.

**The iron law of volatility trading:** You will experience worst case. It's not "if" but "when." Your survival depends on position sizing and mechanical risk management, not on being right about IV direction.



---

## Best Case Scenario

**What happens when everything goes right:**

### 1. The Perfect Setup

**Ideal entry conditions:**
- [IV at optimal level for strategy]
- [Term structure favorably positioned]
- [Skew supporting the trade]
- [Timing aligned with catalyst/events]

**The optimal sequence:**

**Week 1:**
- [IV moves as anticipated]
- [Term structure behaves favorably]
- [Position accumulating profit]
- [Greeks performing as expected]

**Through expiration:**
- [Continued favorable IV dynamics]
- [Optimal IV/RV relationship]
- [Maximum profit zone reached]
- [Exit at optimal timing]

### 2. Maximum Profit Achievement

**Best case mathematics:**

$$
\text{Max Profit} = \text{Vega P\&L} + \text{Theta P\&L} - \text{Gamma Loss}
$$

**Example calculation:**
- Position: [Specific IV structure]
- Entry IV: [Level and percentile]
- Vega exposure: [$ per 1% IV]
- Theta collection: [$ per day]
- **Scenario:**
  - IV moves from [X]% to [Y]%
  - Time passes: [N] days
  - Stock movement: [Favorable/minimal]
- **Profit: [Calculation]**
- **ROI: [Percentage]**

### 3. What Makes It Perfect

The best case requires:
1. **Right IV direction:** IV moves as anticipated (up for long vol, down for short vol)
2. **Right timing:** IV move happens in time frame expected
3. **Right term structure:** Front/back relationship evolves favorably
4. **Right underlying movement:** Stock moves (or doesn't move) as needed
5. **Right skew:** Put/call differential behaves as expected

### 4. IV Component Breakdown

**Vega P&L:**
- Entry IV: [Level]
- Exit IV: [Level]
- Vega position: [$ per 1%]
- **Vega profit: [Calculation]**

**Theta P&L:**
- Days passed: [N]
- Daily theta: [$ per day]
- **Theta profit/cost: [Calculation]**

**Gamma P&L:**
- Stock moves: [Minimal/favorable]
- Rebalancing: [Minimal/profitable]
- **Gamma impact: [Calculation]**

**Net P&L:** Sum of all components

### 5. Comparison to Alternatives

**This strategy vs. [Alternative IV approach]:**
- [IV exposure comparison]
- [Risk-reward analysis]
- [When this strategy wins]
- [Capital efficiency]

### 6. Professional Profit-Taking

**For short volatility:**
- Close at 50-75% of max profit
- Don't wait for 100% (last 20% most risky)
- Free up capital for next trade
- Example: $3 credit → close at $1.50 debit (50%)

**For long volatility:**
- Take profits on IV spikes (100-200% gains)
- Don't wait for perfect scenario
- IV mean-reverts quickly
- Example: Paid $5, worth $10 → sell

**The compounding advantage:**

Short vol example:
- Strategy 1: Hold to expiration (30 days, $300 profit)
- Strategy 2: Close at 50% (15 days, $150), redeploy for another 15 days ($150)
- **Same profit, half the time, quarter the risk**

### 7. The Dream Scenario

**Extreme best case:**

**For short volatility:**
- Enter at IVR 80 (IV very high)
- IV immediately crushes to IVR 20
- Capture 80% of max profit in first week
- **100%+ annualized return with minimal risk**

**For long volatility:**
- Enter at IVR 10 (IV very low)
- Unexpected catalyst hits
- IV spikes to IVR 90
- **300-500% return in days**

**For term structure:**
- Perfect term structure reversion
- Front month IV collapses relative to back month
- Calendar spread worth max value
- **200-300% return on capital**

**Probability:** Rare but illustrates potential when timing perfect

**Key insight:** Best case demonstrates the asymmetric payoff potential of IV strategies. However, realistic expectations should assume median outcomes. Position sizing must account for frequent small wins (short vol) or rare large wins (long vol).



---


---

## Practical Guidance

**Step-by-step framework for trading event calendar spreads:**

### 1. Step 1

**High-probability event calendar opportunities:**

**A. Earnings Announcements (Best)**

Why best:
- Scheduled (known timing)
- Quarterly (4× per year per stock)
- High IV premium (20-40% overpricing)
- Predictable collapse pattern

**Check:**
- Earnings date confirmed (not estimated)
- Options liquid (volume >1,000/day)
- IV percentile >50 (elevated)

**B. Fed Meetings / CPI / NFP (Good)**

Why good:
- Known timing
- Affects entire market
- High IV premium on indices

**Check:**
- SPX/SPY options (very liquid)
- IV spike before event
- VIX >20 (fear premium exists)

**C. FDA Approvals / Court Rulings (Moderate)**

Why moderate:
- Sometimes uncertain timing
- Binary outcomes (high risk)
- Can be illiquid

**Avoid unless:**
- Confirmed date
- Liquid options
- Not first trade (experienced only)

**D. Product Launches (Avoid for beginners)**

Why avoid:
- Uncertain impact
- Hard to price
- Often disappointing (IV doesn't collapse much)

### 2. Step 2

**Critical:** The calendar spread only works if front-month IV elevated relative to back-month.

**Calculate the IV spread:**

$$
\text{IV Spread} = IV_{\text{front}} - IV_{\text{back}}
$$

**Decision criteria:**

```
IV Spread < 10 points: NO TRADE (not enough edge)
IV Spread 10-20 points: MARGINAL (small position)
IV Spread 20-40 points: GOOD (standard position)
IV Spread > 40 points: EXCELLENT (larger position)
```

**Example:**

Stock XYZ earnings in 8 days:
- 1-week options (expiring after earnings): IV = 75%
- 4-week options: IV = 42%
- **IV Spread: 33 points → GOOD TRADE**

**Also check IV percentile:**

$$
\text{IVP} = \frac{\text{Current IV} - \text{52-week Low IV}}{\text{52-week High IV} - \text{52-week Low IV}} \times 100
$$

**Decision:**
- IVP < 30: Front-month IV too low (no event premium)
- IVP 30-50: Marginal (event premium exists but small)
- IVP > 50: **Good** (elevated event premium)
- IVP > 70: **Excellent** (very elevated, likely to collapse)

### 3. Step 3

**Front-month (sell):**

**Expiration:** 1-3 days after event
- Not same-day (pin risk)
- Not too far out (want event premium, not extra time)
- **Optimal: Weekly expiry 1-2 days post-event**

**Strike:**
- ATM (at-the-money): Highest vega, most sensitive
- Slightly OTM: Lower risk if wrong on direction
- **Recommended: ATM or 2-3% OTM**

**Back-month (buy):**

**Expiration:** 2-4 weeks after front-month
- Far enough to be stable
- Not too far (pay less premium)
- **Optimal: Next monthly expiry or 4-week out**

**Strike:** Same as front-month
- Keeps it pure volatility trade
- Delta-neutral at inception

**Example structure:**

Today: March 10
Earnings: March 15 (5 days)
Front: Sell March 17 $100 call (2 days post-earnings)
Back: Buy April 7 $100 call (3 weeks later)

### 4. Step 4

**Calculate maximum loss:**

**For call calendar:**

$$
\text{Max Loss} = \text{Debit Paid} + \text{Assignment Risk}
$$

Assignment risk: If stock gaps way above strike, short call exercised, long call worth less.

**Conservative max loss estimate:**

$$
\text{Max Loss} \approx 2 \times \text{Debit Paid}
$$

**Position sizing formula:**

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times \text{Risk\%}}{2 \times \text{Debit Per Spread}}
$$

**Example:**

Portfolio: $50,000
Risk per trade: 3% = $1,500
Debit per calendar: $2.50
Max loss per spread: $2.50 × 2 = $5.00

$$
\text{Contracts} = \frac{\$1,500}{\$5.00 \times 100} = 3 \text{ contracts}
$$

**Risk management sizing:**
- Beginners: 1-2% risk per trade
- Experienced: 2-4% risk per trade  
- Never: >5% risk on single event

### 5. Step 5

**Timing of entry:**

**Optimal window: 3-7 days before event**

Too early (>10 days):
- Front IV hasn't spiked yet
- Pay more time premium on back month

Too late (<2 days):
- Front IV already elevated (late to trade)
- Risk of event happening early (earnings leak)

**Entry checklist:**

```
□ Event date confirmed (not estimated)
□ IV spread >15 points (sufficient edge)
□ IVP >50 (front-month elevated)
□ Options liquid (bid-ask <10%)
□ Calculated max loss ($XXX)
□ Position sized (X contracts)
□ Delta checked (near zero)
□ Exit plan ready (profit target, stop loss)
```

**Order execution:**

**Use spread order (single order for both legs):**

- Don't leg into it (market might move)
- **Set limit price at natural mid or slightly worse**
- Be patient (don't chase)

**Example order:**

```
Buy 3 XYZ Mar17/Apr7 $100 Call Calendar
Limit: $2.45 (if mid is $2.50)
```

**If no fill in 2 minutes:** Improve by $0.05, try again

### 6. Step 6

**Daily monitoring routine:**

**Before event (days 1-5):**

Check once daily:
- Front IV (should increase as event nears)
- Back IV (should be stable)
- Position P&L (track unrealized)
- Stock price (manage if moves >5%)

**Day of event:**

Check multiple times:
- Event announcement timing
- Immediate stock reaction
- IV levels (front should collapse post-event)

**After event:**

Most important period!
- **If front IV collapses >20 points: Close for profit**
- If front IV collapses <10 points: Hold 1 more day
- If front IV doesn't collapse: Close for loss

### 7. Step 7

**Primary exit: Front-month IV collapse**

**Close when either:**

A. **Target hit:** Front IV collapsed ≥50% from entry
B. **Time:** Day after event (usually)
C. **Profit:** 40-60% of max profit

**Example:**

Entry: Front IV 75%, paid $2.50 debit
Day after earnings: Front IV 32%
- **IV collapse: 43 points (57%)**
- Calendar now worth: $4.20
- **Profit: $1.70 (68% gain)**
- **ACTION: CLOSE**

**Secondary exits:**

**Stop loss triggers:**

1. **Event postponed/cancelled:**
   - Close immediately (IV will drop)
   - Loss: 20-40% typical

2. **Stock gaps >10% through strike:**
   - High assignment risk
   - Close at market (accept loss)

3. **Front IV increases further:**
   - Rare but possible (more uncertainty)
   - If up >20% from entry: Close (wrong trade)

4. **Time stop:** 
   - If 2 days post-event and no IV collapse
   - IV collapse failed to materialize
   - Close for 30-50% loss

### 8. Step 8

**A. Delta Management**

Calendar spreads start delta-neutral but stock movement creates delta.

**If stock moves >5%:**

**Stock up significantly:**
- Short call (front) becomes ITM
- Long call (back) also ITM
- Net: Slightly short delta

**Action:** Buy shares or calls to neutralize (optional)

**Stock down significantly:**
- Both calls OTM
- Net: No delta

**Action:** No adjustment needed

**B. Double Calendar**

For extra premium:

**Structure:**
- Sell ATM call calendar (as normal)
- Sell ATM put calendar (same expirations)
- **Double the premium, double the risk**

**When to use:**
- Very high IV (>80th percentile)
- Confident event won't gap >10%
- More experienced traders

**C. Ratio Calendar**

Adjust risk/reward:

**Structure:**
- Sell 2× front-month calls
- Buy 1× back-month call
- Collect more premium (less debit or credit)
- But higher risk if stock rallies

**When to use:**
- Bearish/neutral bias
- Very high front IV
- Advanced traders only

**D. Iron Calendar (Advanced)**

Combine calendars with verticals:

Too complex for beginners; skip until mastered basic calendar.

### 9. Step 9

**Don't rely on single event - diversify:**

**Calendar spread portfolio approach:**

**Per quarter:**
- Trade 10-15 different stocks
- 3-4 events per week
- **Diversification reduces binary risk**

**Weekly schedule:**

Week 1: Enter 3-4 positions (earnings cycle starts)
Week 2: Monitor positions
Week 3: Close profitable, exit losers
Week 4: Prepare for next month

**Expected results:**

- Win rate: 60-70%
- Average winner: +50% per spread
- Average loser: -40% per spread
- **Net: +15-25% quarterly on capital deployed**

### 10. Step 10

**Required:**
- **Options analytics:** ThinkorSwim, Tastyworks, Interactive Brokers
- **IV tracking:** optionistics.com, marketchameleon.com
- **Earnings calendar:** earningswhispers.com, marketbeat.com
- **Greeks calculator:** Built into platform

**Pre-trade analysis:**

1. **Check IV percentile** (platform or website)
2. **Compare front vs. back IV** (options chain)
3. **Verify event date** (earnings calendar)
4. **Check bid-ask spread** (<10% = good liquidity)
5. **Calculate max loss** (manual or platform)

### 11. Performance Tracking

**Track for every trade:**

```
Entry Log:
- Date: [MM/DD]
- Stock: [TICKER]
- Event: [Earnings/FOMC/etc.]
- Event date: [MM/DD]
- Front expiry: [MM/DD]
- Back expiry: [MM/DD]
- Strike: [$XXX]
- Entry debit: [$X.XX]
- Front IV at entry: [XX%]
- Back IV at entry: [XX%]
- IV spread: [XX points]
- Max loss: [$XXX]
- Contracts: [X]

Exit Log:
- Exit date: [MM/DD]
- Exit credit: [$X.XX]
- Profit/Loss: [$XXX]
- Front IV at exit: [XX%]
- IV collapse: [XX points]
- Hold time: [X days]
- Outcome: [Win/Loss]
- Lessons: [Notes]
```

**Monthly review:**

- Win rate: % profitable trades
- Average profit per winner: $
- Average loss per loser: $
- Expectancy: (Win% × AvgWin) - (Loss% × AvgLoss)
- **Target expectancy: >$50 per trade**

### 12. Pre-Trade Checklist

**Before entering ANY event calendar spread:**

```
□ Event date confirmed (check multiple sources)
□ Front IV >back IV by 15+ points
□ IVP >50 (front-month elevated)
□ Options liquid (volume >500/day, bid-ask <10%)
□ 3-7 days before event (optimal window)
□ Position sized to 2-4% portfolio risk max
□ Strike selected (ATM or slightly OTM)
□ Expirations chosen (1-2 days post-event front, 3-4 weeks back)
□ Calculated max loss and max profit
□ Delta checked (should be near zero)
□ Exit plan ready (profit target, stop loss)
□ Earnings/event time confirmed (AM or PM)
□ Not overlapping with other major events (Fed day, etc.)
□ Account has sufficient capital for max loss
□ Emotionally prepared to take loss if wrong
```

**If any box unchecked: RECONSIDER TRADE**

**Remember:** Event calendar spreads require:
- **Timing** (enter 3-7 days before)
- **Selection** (only trade elevated IV spreads >15 points)
- **Patience** (wait for IV collapse)
- **Discipline** (close after event, don't get greedy)

**Success comes from consistency, not home runs. Trade 10-15 events, win 60-70%, compound returns over quarters.**



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

### 13. Step 7

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

### 14. Common Execution Mistakes to Avoid

1. **Selling vol at low IV** - IVR < 30 usually poor for short vol
2. **Buying vol at high IV** - IVR > 70 often too expensive for long vol
3. **Ignoring term structure** - Don't sell front month if in backwardation
4. **Over-leveraging vega** - Too much vega exposure can blow up account
5. **Holding through earnings** - IV crush destroys long vol positions
6. **Not taking profits** - Greed kills short vol profits
7. **Fighting IV trends** - IV regimes can persist
8. **Ignoring skew** - Put skew can make bearish trades expensive

### 15. Professional Implementation Tips

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

**Critical errors in event calendar spread trading:**

### 1. Mistake #1

**What it looks like:**

- Earnings tomorrow
- See high IV, think "easy money!"
- Enter calendar spread day before event
- **Too late - IV already elevated, little upside**

**The problem:**

Front IV trajectory:
- 7 days before earnings: IV 45%
- 5 days before: IV 60% ← Optimal entry
- 2 days before: IV 72%
- 1 day before: IV 80% ← **TOO LATE**

**If enter at IV 80:**
- Max possible collapse: 80 → 30 = 50 points
- But already paid high price for calendar
- **Risk/reward unfavorable**

**Fix:** Enter 3-7 days before event when IV just starting to elevate.

---

### 2. Mistake #2

**What it looks like:**

- Enter calendar spread
- Think: "Earnings in 5 days"
- Check: "March 15 after-hours"
- Front-month options expire: March 17
- **Event happens after front-month expiry!**

**The disaster:**

Earnings released March 15 4:30 PM (after close)
- Stock gaps 12% overnight
- Front-month options (Mar 17) now deep ITM/OTM
- **No IV collapse benefit** (event already passed)

**Real example:**

Sold NVDA Mar17 $800 call calendar
- Entered Mar 10
- Earnings: Mar 13 after hours
- Mar 14: Stock at $835, short call deep ITM
- Mar 17 expiration: **Assigned, lost $3,500**
- Should have used Mar 15 or Mar 10 expiry

**Fix:** 
- **Check EXACT earnings time** (before or after market hours)
- Front expiry must be AFTER earnings release
- Use earningswhispers.com (shows time)

---

### 3. Mistake #3

**What it looks like:**

- Front IV: 42%
- Back IV: 38%
- **Spread: 4 points** (not enough!)
- Enter anyway

**Why it fails:**

Entry cost: $1.50 debit
Need IV collapse: 4+ points just to break even
- If front drops 42 → 35 (7 points, good collapse)
- Profit: Only $0.50
- **Risk $3 to make $0.50 = terrible**

**Minimum viable spreads:**
- Small cap: 20+ points
- Mid cap: 15+ points
- Large cap: 10+ points

**Fix:** Only trade when IV spread >15 points (>20 preferably).

---

### 4. Mistake #4

**What it looks like:**

- $50K account
- See "perfect" earnings setup
- Risk $5K (10%) on one calendar spread
- **Event goes wrong, lose $4K**

**The problem:**

Even "perfect" setups have 30-40% loss rate:
- Stock gaps through strike
- IV doesn't collapse as expected
- Earnings postponed

**Fix:**
- Max 2-4% per event
- Diversify across 10-15 events
- Law of large numbers works in your favor

---

### 5. Mistake #5

**What it looks like:**

- Earnings passed, IV collapsed
- Front-month has 2 days left
- Think: "Let it expire worthless for max profit"
- **Stock near strike = pin risk**

**The disaster:**

Friday 3:55 PM (expiration):
- Stock at $99.85
- Your $100 short call
- **Exercise uncertain**

Saturday morning:
- Assigned 1,000 shares short at $100
- Stock opens Monday at $102
- **Loss: $2,000 from assignment**

**Fix:**
- **Close day after event** (when IV collapses)
- Take 60-80% of max profit
- Never hold to expiration day

---

### 6. Mistake #6

**What it looks like:**

- Apple product launch in 5 days
- Front IV: 35%, Back IV: 28%
- Enter calendar spread

**What happens:**

Product launched:
- "As expected" announcement
- **Front IV drops 35 → 32** (only 3 points!)
- Calendar loses money

**The problem:**

Product launches rarely move stocks significantly:
- Usually leaked/anticipated
- No surprise
- **IV doesn't collapse much**

**Best events (IV collapse reliable):**
- Earnings (70-80% collapse rate)
- Fed meetings (60-70%)
- CPI releases (65-75%)

**Avoid:**
- Product launches
- Conferences
- "General" news days

**Fix:** Stick to earnings and macro events.

---

### 7. Mistake #7

**What it looks like:**

- Enter calendar: $2.50 debit
- Event happens, worth $3.80
- Think: "Made $1.30!"
- **Close: Net $1.10 after commissions**

**The hidden costs:**

Entry commissions: $1.30 (2 legs × $0.65)
Exit commissions: $1.30 (2 legs × $0.65)
Slippage: $0.20
**Total cost: $2.80**

**Reality:**
- Gross profit: $1.30
- Net profit: **-$1.50 loss!**

**Fix:**
- Use broker with low option fees ($0.50 or less)
- Factor in $2-3 round-trip cost
- Need bigger IV collapse to overcome

---

### 8. Mistake #8

**What it looks like:**

- Enter calendar spread
- No profit target or stop loss
- "I'll see how it goes"
- **Event passes, don't close**
- **Gains evaporate**

**The path:**

Day after earnings:
- Front IV collapsed 60%
- Calendar worth $4.20 (paid $2.50)
- **Profit: $1.70** ← Should close here!
- Think: "Maybe more upside"

3 days later:
- IV continues compressing
- Calendar worth $3.10
- Profit now: $0.60

5 days later (expiration week):
- Front-month theta huge
- Calendar worth $2.30
- **Loss: -$0.20**

**Fix:**
- **Pre-define exit:** "Close when front IV drops 50%"
- OR: "Close day after event regardless"
- Greed kills profits in calendar spreads

---

### 9. Mistake #9

**What it looks like:**

- Enter $100 calendar spread
- Stock moves to $90 (-10%)
- "It's a volatility trade, doesn't matter"
- **Wrong - assignment risk!**

**If stock rallies:**

Front call: Deep ITM
Back call: Also ITM but less
- Net: Short delta
- Risk: Early assignment on short call

**If stock drops:**

Both calls OTM
- Front vega drops
- Less benefit from IV collapse

**Fix:**
- Monitor stock daily
- If >7% move: Consider closing
- Or hedge delta (buy/sell stock)

---

### 10. Mistake #10

**What it looks like:**

- See small-cap earnings
- Front IV: 90%, Back IV: 45%
- **Huge spread!** Enter trade
- Bid-ask: $1.60-$2.40 ← **WIDE**

**The problem:**

Entry: Pay ask $2.40
Exit: Hit bid $1.60
- **$0.80 lost to spread** (33%!)
- Need huge IV collapse to overcome

**Example:**

Enter: $2.40
Earnings happens, IV collapses
Exit: Calendar worth $3.40 (fair value)
Bid-ask: $3.00-$3.80
Sell at bid: $3.00
**Net: $0.60 profit vs. $1.00 if liquid**

**Fix:**
- **Only trade liquid options**
- Volume >1,000/day minimum
- Bid-ask <10% of mid
- Stick to large caps or popular names

---

### 11. Mistake #11

**What it looks like:**

- Earnings morning (before market)
- Use options expiring TODAY
- Think: "Max premium decay!"
- **Gamma risk destroys position**

**What happens:**

9:30 AM: Earnings released (beat)
- Stock gaps $95 → $103 (+8%)
- Your short $100 call: Deep ITM
- **Gamma explodes, delta → 1.00**

9:45 AM: Try to close
- Bid-ask spread widened
- Panic, market order
- **Lost $4/contract**

**Fix:**
- Front expiry: 1-2 days AFTER event minimum
- Never same-day (0DTE too risky)
- Need time for IV collapse to work

---

### 12. Mistake #12

**What it looks like:**

- Stock drops -8% on earnings
- Think: "Calendar should profit!"
- Check position: **Lost money**

**The misunderstanding:**

Calendar spread profits from:
- **IV collapse** (volatility decrease)
- NOT stock price movement

**Example:**

Stock drops -8% but:
- Front IV: 75% → 70% (only 5 point drop!)
- Market still uncertain about future
- **IV didn't collapse enough**
- Calendar loses money despite stock drop

**Fix:**
- Focus on IV, not stock price
- Profit = IV collapse magnitude
- Stock direction is secondary

---

### 13. Mistake #13

**What it looks like:**

- Monday: Enter AAPL calendar (earnings Wed)
- Tuesday: Enter MSFT calendar (earnings Thu)
- Wednesday: Enter GOOGL calendar (earnings Fri)
- **3 events same week**

**The risk:**

All tech stocks:
- Correlated earnings
- If one misses badly, all tech drops
- **All 3 calendars at risk**

**Example (real):**

META reports bad earnings Thu night
- Entire tech sector sells off Friday
- AAPL, MSFT, GOOGL calendars all lose
- **Lost on 3 positions same day**

**Fix:**
- Diversify across sectors
- Max 1-2 events same week
- Spread across calendar month

---

### 14. Mistake #14

**What it looks like:**

- New to stock, see high IV
- Enter calendar blind
- Check history after: Stock always gaps 15%+ on earnings
- **Wrong stock for strategy**

**Volatility stocks to avoid:**

- TSLA (crazy gaps)
- Small biotech (binary outcomes)
- Chinese ADRs (geopolitical risk)

**Better candidates:**

- Large cap stable (JNJ, PG, KO)
- Moderate IV stocks
- Historical gaps <8%

**Fix:**
- **Check past 4-8 earnings**
- Average gap <10%
- Avoid "meme" stocks

---

### 15. Mistake #15

**What it looks like:**

- Trade 20 calendars over quarter
- Some win, some lose
- Don't track which worked
- **Repeat same mistakes**

**Without tracking:**

Can't answer:
- Which stocks worked best?
- Optimal entry timing (5 days vs. 3 days)?
- Better with ATM or OTM?
- Win rate by sector?

**Fix:**

Track spreadsheet:
```
Stock | Entry Date | Event Date | Front IV | Back IV | Entry $ | Exit $ | P/L | Notes
AAPL  | 3/10      | 3/15      | 65%     | 38%    | $2.50  | $3.80 | +$1.30 | Good
TSLA  | 3/12      | 3/17      | 95%     | 52%    | $4.20  | $2.10 | -$2.10 | Too volatile
```

**Quarterly review:**
- What worked (repeat)
- What failed (avoid)
- Continuous improvement

---

### 16. **Summary Checklist

```
□ Don't enter day before event (too late)
□ Don't forget to check event timing (before/after hours)
□ Don't trade <15 point IV spreads (insufficient edge)
□ Don't risk >4% on single event (over-sizing)
□ Don't hold through expiration (pin risk)
□ Don't trade product launches (unreliable IV collapse)
□ Don't forget transaction costs (commissions kill small edges)
□ Don't trade without exit plan (define beforehand)
□ Don't ignore stock movement (>7% creates risk)
□ Don't trade illiquid options (wide spreads eat profit)
□ Don't use 0DTE expirations (gamma risk)
□ Don't confuse IV collapse with price drop (not the same)
□ Don't hold multiple same-sector events (correlation risk)
□ Don't skip earnings history check (avoid volatile stocks)
□ Don't skip post-trade review (can't improve without data)
```

**The difference between profitable event calendar trading and losing money is avoiding these mistakes. Master these lessons and your win rate will jump from 50% to 65-70%.**





---

## Real-World Examples

**Detailed case studies of event calendar spread trades:**

### 1. Example 1: Textbook Earnings Calendar (AAPL

**Background:**

- Date: January 20, 2024
- Stock: AAPL trading at $185
- Earnings: January 25 after market close
- Front expiry: January 26 (weekly)
- Back expiry: February 16 (monthly)

**Setup Analysis:**

**IV Environment:**
- Front-month (Jan 26) IV: 48%
- Back-month (Feb 16) IV: 31%
- **IV Spread: 17 points** ← Good setup
- IV percentile: 62% (elevated)

**Historical context:**
- AAPL last 4 earnings: Average move 4.2%
- Average IV collapse: 22 points
- Win rate: 3 of 4 profitable

**The Trade:**

- **Sell** 5 contracts AAPL Jan 26 $185 call @ $7.50
- **Buy** 5 contracts AAPL Feb 16 $185 call @ $10.20
- **Net debit:** $2.70 per spread
- **Capital at risk:** $2.70 × 100 × 5 = **$1,350**

**Max loss:** ~$5 per spread = $2,500
**Position size:** 2.7% of $50K account ✓

**What Happened:**

**January 25 (Earnings Day):**
- 4:30 PM: AAPL reports (beat expectations)
- AH trading: Stock $185 → $188 (+1.6%)
- Moderate beat, no surprise

**January 26 (Day After Earnings):**
- 9:30 AM open: Stock stable at $187.50
- **Front IV:** 48% → 26% (collapsed 22 points!)
- **Back IV:** 31% → 29% (stable, -2 points)

**Position value:**
- Jan 26 call: $7.50 → $3.20 (IV crush + time decay)
- Feb 16 call: $10.20 → $10.80 (slight gain from stock move)
- **Calendar value: $10.80 - $3.20 = $7.60**

**Exit:**
- Closed at $7.50 (bid-ask)
- **Entry:** $2.70
- **Exit:** $7.50
- **Profit: $4.80 per spread**

**Total P&L:** $4.80 × 100 × 5 = **+$2,400 (178% return)**

**Key Lessons:**
1. Proper IV spread (17 points) provided edge
2. Closed day after earnings (took profit)
3. Normal earnings result = reliable IV collapse
4. Held less than 1 week, capital-efficient

---

### 2. Example 2: Fed Meeting Disaster (SPX

**Background:**

- Date: March 15, 2024
- Underlying: SPX at 5,200
- Event: FOMC meeting March 20, 2 PM
- Front expiry: March 22 (weekly)
- Back expiry: April 19 (monthly)

**Setup (Seemed Good):**

**IV Environment:**
- Front (Mar 22) IV: 18%
- Back (Apr 19) IV: 14%
- **IV Spread: 4 points** ← **MISTAKE #1: Too narrow**
- VIX: 14 (below average)

**The Trade:**

- **Sell** 2 contracts SPX Mar 22 $5200 call @ $85
- **Buy** 2 contracts SPX Apr 19 $5200 call @ $105
- **Net debit:** $20 per spread ($2,000 × 2 = $4,000)

**What Went Wrong:**

**March 20 (FOMC Day):**
- 2:00 PM: Fed announces (hawkish surprise!)
- Powell: "Not cutting rates soon"
- SPX drops 5,200 → 5,020 (-3.5%)

**Position immediately:**
- Both calls now OTM (stock dropped)
- But front vega collapsed (some benefit)
- **Net: Breaking even** (IV collapse offsetting stock drop)

**Mistake: Held position**
- Thought: "Wait for more IV collapse"
- Should have closed here

**March 21:**
- Market continues down: SPX 5,020 → 4,980
- **Front IV: 18% → 14%** (only 4 point collapse)
- **Back IV: 14% → 13%** (also dropped)

**Both calls deep OTM:**
- Mar 22 call: $85 → $2 (intrinsic = 0, IV collapsed)
- Apr 19 call: $105 → $12 (still has time)

**Position value: $12 - $2 = $10**

**Exit (March 21):**
- Entry: $20
- Exit: $10
- **Loss: -$10 per spread**

**Total P&L:** -$10 × 100 × 2 = **-$2,000 loss (-50%)**

**What Went Wrong:**

1. **IV spread too narrow** (4 points insufficient)
2. **Unexpected market direction** (SPX down 3.5%)
3. **Held too long** (should have closed day of event)
4. **Fed meetings trickier** than earnings (policy uncertainty)

**Lessons:**
1. Need >10 point IV spread minimum
2. Fed events more unpredictable than earnings
3. Close on event day if not working
4. Stop loss: If position -40% and event not helped, exit

---

### 3. Example 3

**Background:**

- Trader: Systematic event calendar trader
- Capital: $100,000
- Strategy: Trade 15 earnings events per quarter
- Risk: 2% per trade = $2,000 max

**Q1 2024 Results:**

| Stock | Entry IV Spread | Result | P&L |
|-------|----------------|--------|-----|
| AAPL | 18 pts | Win | +$2,100 |
| MSFT | 21 pts | Win | +$2,400 |
| GOOGL | 15 pts | Win | +$1,200 |
| AMZN | 24 pts | Win | +$2,800 |
| META | 19 pts | Win | +$1,900 |
| TSLA | 32 pts | **Loss** | -$1,800 |
| NVDA | 28 pts | Win | +$3,100 |
| NFLX | 22 pts | Win | +$2,200 |
| DIS | 16 pts | **Loss** | -$1,400 |
| BA | 14 pts | **Small loss** | -$600 |
| JPM | 17 pts | Win | +$1,500 |
| GS | 19 pts | Win | +$1,700 |
| WMT | 12 pts | **Tiny loss** | -$300 |
| TGT | 15 pts | Win | +$1,300 |
| HD | 18 pts | Win | +$1,600 |

**Summary:**
- Trades: 15
- Winners: 11 (73% win rate)
- Losers: 4 (27%)
- Total profit: +$16,100
- Total loss: -$4,100
- **Net: +$12,000 (+12% quarterly return)**

**Analysis:**

Average winner: +$1,827
Average loser: -$1,025
Expectancy: (0.73 × $1,827) - (0.27 × $1,025) = **+$1,057 per trade**

**Sharpe ratio:** 2.1 (excellent)

**Key Insights:**
1. Diversification works (15 events smooths variance)
2. Win rate 70%+ achievable with discipline
3. Lost on TSLA (too volatile, should avoid)
4. Lost on low IV spread trades (WMT 12 pts, BA 14 pts)
5. **Consistency beats home runs**

---

### 4. Example 4: Late Entry Mistake (NFLX

**Background:**

- Stock: NFLX at $620
- Earnings: April 18 after close
- **Entry:** April 17 (day before!) ← **MISTAKE**
- Front expiry: April 19
- Back expiry: May 17

**Setup:**

**IV at entry (April 17):**
- Front: 72% (already elevated!)
- Back: 38%
- IV Spread: 34 points (looks good)

**The Trade:**

- Sell NFLX Apr 19 $620 call @ $32
- Buy NFLX May 17 $620 call @ $41
- **Debit: $9**

**What Happened:**

**April 18 Earnings:**
- Reported after close
- Beat estimates
- Stock +6% to $658 in after-hours

**April 19 (Expiration Day):**
- Stock opens $656
- **Front IV:** 72% → 35% (collapsed 37 points - good!)
- But short call now ITM

**Position value:**
- Apr 19 call: $32 → $38 (ITM + some time value left)
- May 17 call: $41 → $52 (stock up + IV still elevated)
- **Calendar: $52 - $38 = $14**

**Exit:**
- Entry: $9
- Exit: $14
- **Profit: +$5 (56% gain)**

**But compare to optimal entry:**

If entered April 12 (5 days earlier):
- Front IV would have been: 52% (not 72%)
- Entry cost: ~$5-6 (not $9)
- Same exit: $14
- **Profit would have been: +$8-9 (140%+ gain)**

**Lesson:**

Late entry still profitable BUT:
- Lower ROI (56% vs. 140%)
- Higher risk (paid inflated price)
- Less margin of safety

**Optimal window: 3-7 days before event, not 1 day.**

---

### 5. Example 5

**Background:**

- Stock: XYZ (small cap) at $45
- Earnings: May 10
- Option volume: 200/day ← **RED FLAG**

**Setup (Looked Amazing):**

- Front IV: 85%
- Back IV: 42%
- **IV Spread: 43 points!** (Huge)
- Entry date: May 5

**The Trade:**

- Sell May 12 $45 call @ $4.50
- Buy June 16 $45 call @ $5.80
- Natural price (mid): $1.30

**But bid-ask:**
- Bid: $0.90
- Ask: $1.70
- **Spread: $0.80** (62% of mid!)

**Entry:**
- Tried to get filled at $1.40
- No fill after 10 minutes
- Paid ask: **$1.70** (desperation)

**Earnings (May 10):**
- Stock beats, up to $48
- Front IV collapsed: 85% → 38%

**Position value:**
- May 12 call: $4.50 → $4.00 (ITM)
- June 16 call: $5.80 → $7.20
- Calendar mid: $3.20
- **Should be up $1.50!**

**Exit attempt:**
- Bid: $2.80
- Ask: $3.60
- Hit bid: **$2.80**

**P&L:**
- Entry: $1.70
- Exit: $2.80
- **Profit: +$1.10**

**vs. If liquid:**
- Entry at mid: $1.30
- Exit at mid: $3.20
- **Profit would be: +$1.90**

**Cost of illiquidity:** $0.80 per spread = **42% of potential profit lost!**

**Lesson:** 

Stick to liquid options:
- Volume >1,000/day
- Bid-ask <10% of mid
- Illiquidity eats 30-50% of edge

---

### 6. Example 6

**Background:**

- Stock: SPY at $520
- CPI Release: June 12, 8:30 AM
- Front expiry: June 14
- Back expiry: July 19

**Setup:**

- Front IV: 24% (elevated before CPI)
- Back IV: 16%
- IV Spread: 8 points

**The Trade (Double Calendar):**

**Sell June 14 straddle:**
- Sell $520 call @ $8
- Sell $520 put @ $7.80
- **Credit: $15.80**

**Buy July 19 straddle:**
- Buy $520 call @ $13
- Buy $520 put @ $12.50
- **Debit: $25.50**

**Net double calendar debit: $9.70**

**What Happened:**

**June 12 (CPI Day):**
- 8:30 AM: CPI released (in-line)
- SPY: $520 → $522 (small move)
- **Front IV:** 24% → 14% (collapsed 10 points)
- **Back IV:** 16% → 15% (stable)

**June 14 (Expiration):**
- SPY stable at $521
- June 14 straddle: Both legs near ATM, IV crushed
  - $520 call: $8 → $1.50
  - $520 put: $7.80 → $0.40
  - **Total: $1.90**

- July 19 straddle: Still has value
  - $520 call: $13 → $13.80
  - $520 put: $12.50 → $11.20
  - **Total: $25**

**Calendar value: $25 - $1.90 = $23.10**

**P&L:**
- Entry: $9.70
- Exit: $23.10
- **Profit: +$13.40 (138% gain)**

**Why it worked so well:**

1. Double calendar (both call and put side)
2. SPY stayed near $520 (perfect for straddle)
3. Front IV collapsed significantly (10 points)
4. Back IV stable (didn't decay much)

**Risk:** If SPY moved >$10, would have lost money

**Lesson:** Double calendars magnify both profits and losses. Use only when:
- Very high confidence in IV collapse
- Expect small price movement (<2%)
- Experienced traders only




## Key Takeaways

- Event calendars exploit volatility concentration
- Front-month IV often overprices events
- Profit comes from IV collapse, not direction
- Gap risk is real and must be managed
- Best used systematically across many events

---

## One-Line Summary

> **Event calendar spreads profit from mispricing in the timing of volatility around discrete market events.**