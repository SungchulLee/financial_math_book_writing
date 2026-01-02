# Skew Trading Spreads  
## Exploiting Put / Call Implied Volatility Differences

**Skew trading spreads** focus on exploiting relative mispricing between **put and call implied volatilities across strikes**, rather than trading the absolute level of volatility or the direction of the underlying.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/skew_trading_spreads_mean_reversion.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/skew_trading_spreads_opportunity.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/skew_trading_spreads_premium.png?raw=true" alt="long_call_vs_put" width="700">
</p>

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/skew_trading_spreads_returns.png?raw=true" alt="long_call_vs_put" width="700">
</p>

---

## The Core Insight

**The fundamental idea:**

- Implied volatility is **not symmetric across strikes**
- Downside puts usually trade at **higher IV** than upside calls
- This asymmetry is called **volatility skew**
- Skew is structural, but **not constant**
- When skew becomes too steep or too flat, **relative-value trades emerge**

> **Skew trading is not about volatility level — it is about volatility *asymmetry*.**

---

## What Is Volatility Skew?

### Definition

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

### Why Skew Exists

Skew is driven by:

- Demand for downside protection
- Institutional hedging flows
- Leverage and margin constraints
- Behavioral fear asymmetry

Skew reflects **market-implied asymmetry in future return distributions**.

---

## Why Skew Becomes Tradable

Skew is **persistent**, but:

- It changes magnitude
- It mean-reverts
- It overreacts during stress or events

**Trading opportunity arises when:**

- Put IV is *too rich* relative to calls
- Call IV is *too cheap*
- Historical or model-implied skew relationships break

---

## The Structure

### General Skew Trading Construction

Skew trades are typically:

- Same maturity
- Different strikes
- Long cheap volatility
- Short rich volatility
- Often delta-neutral

> **Long relative IV on one wing, short relative IV on the other.**

---

### Common Skew Trading Structures

#### 1. Risk Reversal

\[
\text{Risk Reversal} = \text{Long OTM Call} - \text{Short OTM Put}
\]

- Long upside IV
- Short downside IV
- Strong skew exposure

---

#### 2. Put vs Call Vertical Spread

- Sell expensive put spread
- Buy cheap call spread
- Delta-hedge

---

#### 3. Skewed Butterfly

- Sell rich downside wing
- Buy cheap upside wing
- ATM strike anchors payoff

---

## The Portfolio

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

## Economic Interpretation

**Understanding what this strategy REALLY represents economically:**

### The Core Economic Trade-Off

This IV strategy involves specific economic trade-offs around volatility exposure. The key is understanding what you're giving up versus what you're gaining in terms of implied volatility positioning.

**Economic equivalence:**

$$
\text{Strategy P\&L} = \text{IV Change Component} + \text{Term Structure Component} + \text{Skew Component}
$$

### Why This IV Structure Exists Economically

Markets create these IV structures because different participants have different:
- Volatility expectations (near-term vs. long-term)
- Risk preferences (convexity vs. theta)
- Event views (known catalysts vs. unknown volatility)
- Hedging needs (portfolio protection vs. income generation)

### The Volatility Risk Premium

Most IV strategies exploit the **volatility risk premium** - the empirical observation that:

$$
\text{Implied Volatility} > \text{Realized Volatility} \quad \text{(on average)}
$$

**Why this exists:**
1. **Insurance value:** Investors pay premium for protection
2. **Crash insurance:** Fear of tail events inflates IV
3. **Supply/demand:** More vol buyers than sellers
4. **Behavioral biases:** Overestimation of future volatility

### Professional Institutional Perspective

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

## Risk Management

- Control tail risk
- Use spreads instead of naked options
- Hedge delta frequently
- Avoid event-heavy periods
- Define max loss upfront

---

## Relationship to Other Strategies

| Strategy | Dimension |
|--------|-----------|
| Vega trades | Vol level |
| Calendars | Term structure |
| Butterflies | Curvature |
| **Skew trades** | **Put–call asymmetry** |
| Surface arb | Full surface |

---


---

## Worst Case Scenario

**What happens when everything goes wrong:**

### The Nightmare Setup

**How it starts:**
- Enter risk reversal on SPY at $450
- Skew looks steep: OTM puts trading at IV 28%, OTM calls at IV 18%
- Sell $440 puts @ IV 28% for $4.50
- Buy $460 calls @ IV 18% for $2.20
- Net credit: $2.30 ($230 per contract)
- 10 contracts, delta-neutral structure
- Expecting skew to normalize (puts cheaper, calls more expensive)

**The deterioration:**

**Week 1:**
- Market sells off: SPY drops from $450 to $440
- Short puts now ATM (danger!)
- Skew STEEPENS further (opposite of expectation)
- Put IV: 28% → 35% (+7 points)
- Call IV: 18% → 15% (-3 points)
- **Skew widened from 10 points to 20 points!**
- Position down $3,000 (short puts losing value)
- Critical decision: Close at loss or wait for mean reversion?

**Week 2:**
- Flight to safety continues
- SPY at $435 (puts now ITM)
- Put IV: 35% → 42% (crash protection premium)
- Call IV: 15% → 14% (nobody wants calls in selloff)
- **Skew now 28 points (nearly 3x normal)**
- Short puts: Bought at $4.50, now worth $9.00
- Long calls: Paid $2.20, now worth $0.50
- **Position value: -$9.00 + $0.50 = -$8.50 loss**
- Total loss: ($2.30 credit - $8.50 loss) × 100 × 10 = -$6,200

**Through expiration:**
- Week 3: SPY stabilizes at $432
- Put IV remains elevated at 38% (crisis premium persists)
- Call IV at 13% (nobody wants upside)
- **Skew stays abnormally steep at 25 points**
- Short puts deep ITM: Worth $8.00
- Long calls worthless: $0.10
- Must close position
- **Final loss:**
  - Collected $2.30 credit initially
  - Pay $8.00 to buy back puts
  - Calls nearly worthless
  - Net: ($2.30 - $8.00) × 100 × 10 = **-$5,700**
  - Plus slippage and commissions: **-$5,850 total**
  - **11.7% of $50,000 account destroyed**

**Why skew didn't normalize:**
- Market stress persisted
- Institutional hedging demand elevated
- Skew can stay steep for months during bearish regimes
- **Mean reversion bet failed catastrophically**
- Assumed normal distribution, got fat left tail

### Maximum Loss Calculation

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
- Position: 10 risk reversals on SPY, short $440 puts / long $460 calls
- Entry skew: Put IV 28%, Call IV 18% (10-point differential)
- Entry P&L: +$2.30 credit per contract
- Adverse scenario: Market selloff + skew steepening
  - SPY: $450 → $432 (-4%)
  - Put IV: 28% → 38% (+10 points)
  - Call IV: 18% → 13% (-5 points)
  - **Skew: 10 points → 25 points (150% increase)**
- **Loss breakdown:**
  - Short puts: Sold $4.50, worth $8.00 = -$3.50 per contract
  - Long calls: Paid $2.20, worth $0.10 = -$2.10 per contract
  - Net option loss: -$5.60 per contract
  - Minus credit collected: +$2.30
  - **Loss per contract: -$3.30**
  - 10 contracts × 100 × $3.30 = **-$3,300**
  - But actual worse due to assignment/slippage = **-$5,850**
- **Impact: 11.7% of $50,000 portfolio (severe single trade)**

### What Goes Wrong

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

### The Cascade Effect

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

### Real Disaster Scenarios

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

### The Gamma Blow-Up

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

### IV Regime Persistence

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

### Psychology of IV Losses

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

### Preventing Worst Case

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

### The Ultimate Protection

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

### The Perfect Setup

**Ideal entry conditions:**
- SPY at $450, post-selloff recovery phase
- Skew abnormally steep from recent volatility
- OTM put IV: 32% (elevated from fear)
- OTM call IV: 18% (depressed from pessimism)
- **Skew differential: 14 points (2 std dev above normal)**
- Historical normal skew: 8-10 points
- Market stabilizing, VIX declining
- No major catalysts for 30-45 days

**The optimal sequence:**

**Week 1-2 (Skew normalization begins):**
- Enter position targeting skew compression
- Sell $440 puts @ IV 32% for $5.00
- Buy $460 calls @ IV 18% for $2.50
- **Net credit: $2.50 ($250 per contract)**
- 10 contracts, targeting skew mean reversion
- Market stability returns
- Put IV: 32% → 28% (fear premium declining)
- Call IV: 18% → 20% (optimism returning)
- **Skew: 14 points → 8 points (normalizing!)**
- Position gaining value

**Week 3-4 (Perfect skew compression):**
- Continued market calm, SPY range $448-$452
- Put IV: 28% → 24% (hedging demand eases)
- Call IV: 20% → 22% (buyers return)
- **Skew: 8 points → 2 points (compressed!)**
- Short puts: Worth $2.00 (IV dropped + OTM)
- Long calls: Worth $3.50 (IV rose + slightly ITM)
- **Position value change: -$2.00 + $3.50 = +$1.50 gain**
- Combined with $2.50 credit = **$4.00 total profit**
- **Time to close at Day 28**

**Final outcome:**
- Close position for $4.00 profit per contract
- 10 contracts × $4.00 × 100 = **$4,000 profit**
- **ROI: 160% on $2,500 credit in 28 days**
- **Annualized: 2,086%**

### Maximum Profit Achievement

**Best case mathematics:**

$$
\text{Max Profit} = \text{Vega P\&L} + \text{Theta P\&L} - \text{Gamma Loss}
$$

**Example calculation:**
- Position: 10 risk reversals on SPY, short $440 puts / long $460 calls
- Entry skew: Put IV 32%, Call IV 18% (14-point differential, abnormally steep)
- Entry credit: $2.50 per contract
- Vega exposure: Short puts -$200, Long calls +$250 = Net +$50 per 1% IV
- **Scenario:**
  - Skew normalizes from 14 points to 2 points over 28 days
  - Put IV: 32% → 24% (-8 points)
  - Call IV: 18% → 22% (+4 points)
  - SPY: $450 → $451 (minimal directional move)
- **Profit breakdown:**
  - Put vega P&L: -$200 × (-8%) = +$1,600 (puts got cheaper)
  - Call vega P&L: +$250 × (+4%) = +$1,000 (calls got more expensive)
  - Theta P&L: -$100 (net time decay cost, minor)
  - **Gross P&L: $1,600 + $1,000 - $100 = +$2,500**
  - Plus credit: +$2,500
  - **Total profit: $2,500 + $2,500 = $5,000**
  - Wait, let me recalculate more simply:
  - Short puts: Sold $5.00, buy back $2.00 = +$3.00
  - Long calls: Paid $2.50, sell $3.50 = +$1.00
  - Net: $3.00 + $1.00 = **$4.00 profit per contract**
  - 10 contracts × 100 × $4.00 = **$4,000 total**
- **ROI: $4,000 / $2,500 credit = 160% in 28 days**

### What Makes It Perfect

The best case requires:
1. **Right IV direction:** IV moves as anticipated (up for long vol, down for short vol)
2. **Right timing:** IV move happens in time frame expected
3. **Right term structure:** Front/back relationship evolves favorably
4. **Right underlying movement:** Stock moves (or doesn't move) as needed
5. **Right skew:** Put/call differential behaves as expected

### IV Component Breakdown

**Vega P&L:**
- Entry put IV: 32%, Exit put IV: 24%
- Entry call IV: 18%, Exit call IV: 22%
- Vega position: Short puts -$200, Long calls +$250 per 1% IV
- Put vega: -$200 × (-8%) = **+$1,600**
- Call vega: +$250 × (+4%) = **+$1,000**
- **Total vega profit: $2,600**

**Theta P&L:**
- Days passed: 28 days
- Short put theta: -$15/day (we collect)
- Long call theta: -$20/day (we pay)
- Net daily theta: -$5/day (small cost)
- **Theta cost: -$5 × 28 = -$140 (minor drag)**

**Gamma P&L:**
- Stock moves: $450 → $451 (+0.2%, minimal)
- Gamma neutral structure (risk reversal)
- No rebalancing needed
- **Gamma impact: ~$0 (negligible)**

**Delta P&L:**
- Position delta: ~+20 (long bias from structure)
- Stock move: +$1
- **Delta profit: +$200**

**Net P&L:** $2,600 (vega) - $140 (theta) + $0 (gamma) + $200 (delta) = **+$2,660**

Simplified: Short puts gained $3.00, long calls gained $1.00 = **$4.00 × 1,000 shares × 10 contracts = $4,000**

### Comparison to Alternatives

**This strategy vs. Iron Condor (absolute IV trade):**

**Skew Trade (Risk Reversal):**
- Position: Short rich puts, long cheap calls
- Exposure: Relative value (skew compression)
- Directional: Has delta bias (bullish tilt)
- Profit driver: Skew normalization
- Capital: $2,500 credit collected
- Max profit: Unlimited (calls can run)
- Max loss: Large if stock crashes
- **Best when:** Skew abnormally steep, stable/bullish market

**Iron Condor (Absolute IV):**
- Position: Sell both put and call spreads
- Exposure: Absolute volatility level
- Directional: Delta neutral
- Profit driver: IV crush + theta decay
- Capital: ~$4,000 max risk (defined)
- Max profit: $3.60 typical credit
- Max loss: Defined ($1.40 spread - credit)
- **Best when:** High absolute IV, range-bound market

**When skew trade wins:**
- Skew is distorted but absolute IV normal
- Market trending up (delta helps)
- Want unlimited upside (long calls)
- Comfortable with undefined risk
- **Profit: $4,000 on skew compression**

**When iron condor wins:**
- Absolute IV very high (>70 IVR)
- Market directionless
- Want defined risk
- Prefer theta collection to skew bet
- **Profit: $3,600 on range-bound + IV crush**

**Capital efficiency:**
- Skew trade: $4,000 profit on ~$5,000 margin
- Iron condor: $3,600 profit on $11,000 max risk
- **Skew trade higher ROC but higher risk**

### Professional Profit-Taking

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

### The Dream Scenario

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

**Step-by-step implementation framework:**

### Step 1: Volatility Environment Assessment

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

### Step 2: Strategy Selection Criteria

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

### Step 3: Position Sizing

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

### Step 4: Entry Execution

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

### Step 5: Position Management

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

### Step 6: Adjustment Protocols

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

### Step 7: Record Keeping

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

### Common Execution Mistakes to Avoid

1. **Selling vol at low IV** - IVR < 30 usually poor for short vol
2. **Buying vol at high IV** - IVR > 70 often too expensive for long vol
3. **Ignoring term structure** - Don't sell front month if in backwardation
4. **Over-leveraging vega** - Too much vega exposure can blow up account
5. **Holding through earnings** - IV crush destroys long vol positions
6. **Not taking profits** - Greed kills short vol profits
7. **Fighting IV trends** - IV regimes can persist
8. **Ignoring skew** - Put skew can make bearish trades expensive

### Professional Implementation Tips

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

### 1. Assuming Skew Always Mean-Reverts

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

### 2. Ignoring Directional Risk

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

### 3. Wrong Strike Selection

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

### 4. Insufficient Skew Deviation

**The error:**
- Skew at 11 points, normal is 10
- "1 point edge, I'll trade it"
- After costs, no real edge

**Fix:**
- Need 1.5-2 standard deviations from normal
- Minimum 3-5 point skew deviation
- Factor in bid-ask spreads
- **Only trade significant dislocations**

### 5. Not Checking Historical Patterns

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

### Example 1: Post-Crisis Skew Compression (Winning Trade)

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

### Example 2: Failed Skew Trade (Learning Experience)

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

### Example 3: Earnings Skew Play (Moderate Win)

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

### Example 4: Professional Systematic Skew Strategy

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


## Key Takeaways

- Skew trading is **relative-value volatility trading**
- Downside IV is structurally rich
- Delta management is essential
- Skew mean-reverts, but not always quickly

---

## One-Line Summary

> **Skew trading spreads exploit distortions in put–call implied volatility by trading asymmetry rather than volatility level.**