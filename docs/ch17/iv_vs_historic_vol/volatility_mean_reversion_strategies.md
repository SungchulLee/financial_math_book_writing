# Volatility Mean Reversion Strategies
## Trading the Cyclical Nature of Volatility

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/volatility_mean_reversion_strategies_half_life.png?raw=true" alt="volatility_mean_reversion_strategies_half_life" width="700">
</p>
<p align="center"><em>Figure 1: Half-life analysis showing mean reversion speed across different volatility regimes and asset classes</em></p>

**Volatility mean reversion strategies** exploit the empirical fact that volatility tends to **revert toward a long-term average** after periods of unusually high or low levels.

Rather than predicting direction, these strategies trade the **dynamics of uncertainty itself**.





---

## The Core Insight

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/volatility_mean_reversion_strategies_pattern.png?raw=true" alt="volatility_mean_reversion_strategies_pattern" width="700">
</p>
<p align="center"><em>Figure 2: Volatility mean reversion pattern demonstrating clustering, spikes, and decay toward long-term average</em></p>

**The fundamental idea:**

- Volatility is **not a random walk**

- It exhibits **clustering** and **mean reversion**

- Periods of high volatility are usually followed by lower volatility

- Periods of low volatility are usually followed by higher volatility

- This behavior is observable across asset classes and time scales

$$
\mathbb{E}[\sigma_{t+h} \mid \sigma_t] \rightarrow \bar{\sigma}
$$

> **Volatility spikes are temporary; calm does not last forever.**

---

## Why Volatility Mean-Reverts

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/volatility_mean_reversion_strategies_performance.png?raw=true" alt="volatility_mean_reversion_strategies_performance" width="700">
</p>
<p align="center"><em>Figure 3: Performance comparison of mean reversion strategies across bull, bear, and crisis market conditions</em></p>

Volatility mean reversion arises from:

- Market microstructure

- Leverage constraints

- Risk targeting and deleveraging

- Option hedging flows

- Behavioral overreaction and normalization

High volatility triggers:

- Risk reduction

- Lower leverage

- Reduced trading activity

Low volatility triggers:

- Increased leverage

- Risk-taking

- Crowded positioning

---

## What Mean Reversion Means in Practice

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/volatility_mean_reversion_strategies_zones.png?raw=true" alt="volatility_mean_reversion_strategies_zones" width="700">
</p>
<p align="center"><em>Figure 4: Trading zones showing optimal entry points for selling volatility (extremes) vs buying volatility (compression)</em></p>

### 1. Volatility Regimes

Volatility tends to oscillate between regimes:

- **Low-vol regime:** complacency, carry trades

- **Normal regime:** balanced risk-taking

- **High-vol regime:** stress, deleveraging

Each regime is unstable.

```
Vol
↑
40% |     ●
30% |   ●   ●
20% | ●       ●
10% |     ●
    |________________→ Time
```

Mean reversion strategies attempt to **fade extremes**, not predict exact turning points.

---

## The Structure

### 1. General Mean Reversion

Mean reversion trades typically:

- Sell volatility after **large spikes**

- Buy volatility after **unusually calm periods**

- Are expressed via options, variance, or volatility indices

- Are often combined with **time diversification**

> **You trade volatility when it is extreme relative to its own history.**

---

### 2. Common Mean Reversion Structures

### 3. Short Volatility After Spikes

- Sell ATM straddles or strangles

- Sell variance exposure

- Collect elevated implied volatility

Used when:

- IV is far above historical norms

- Market stress is subsiding

---

### 4. Long Volatility After Compression

- Buy straddles or strangles

- Long gamma positions

- Prepare for volatility expansion

Used when:

- Volatility is unusually low

- Markets are complacent

- Leverage is elevated

---

### 5. VIX Mean Reversion Trades

- Short VIX futures after spikes

- Long VIX after deep compression

- Trade volatility directly

---

### 6. Calendar-Based Mean Reversion

- Sell near-term volatility spikes

- Buy longer-dated volatility

- Exploit normalization of term structure

---

## The Portfolio

$$
\Pi_{\text{MR}} = \sum_i n_i \cdot V(T_i, \sigma_i)
$$

Typically managed so that:

$$
\Delta \approx 0
$$

with exposure concentrated in **volatility level**, not direction.

---

## Economic

**Understanding what mean reversion strategies REALLY represent economically:**

### 1. The Core Economic Trade-Off

**Mean reversion strategies are fundamentally trading volatility overshoots:**

$$
\text{P\&L}_{\text{MR}} = \underbrace{\mathcal{V} \cdot (\sigma_t - \bar{\sigma})}_{\text{Distance from mean}} \times \underbrace{e^{-\lambda t}}_{\text{Reversion speed}}
$$

where $\lambda$ is the mean reversion coefficient.

**Economic meaning:**

When you sell volatility after a spike, you're betting:

- Current volatility > long-run equilibrium

- Market overreacted to temporary shock

- Natural forces will restore normal levels

When you buy volatility after compression, you're betting:

- Current volatility < long-run equilibrium

- Market complacency unsustainable

- Uncertainty will re-emerge

### 2. The Ornstein-Uhlenbeck Process

**Theoretical foundation:**

Volatility follows a mean-reverting process:

$$
d\sigma_t = \kappa(\theta - \sigma_t)dt + \xi\sqrt{\sigma_t}dW_t
$$

where:

- $\kappa$ = speed of mean reversion

- $\theta$ = long-run mean volatility

- $\xi$ = volatility of volatility

- $dW_t$ = Wiener process

**Key parameters:**

**Mean reversion speed ($\kappa$):**

- SPX: $\kappa \approx 2\text{-}3$ (half-life ~90-120 days)

- Individual stocks: $\kappa \approx 4\text{-}6$ (half-life ~40-60 days)

- VIX: $\kappa \approx 8\text{-}10$ (half-life ~25-35 days)

**Long-run mean ($\theta$):**

- SPX: $\theta \approx 16\text{-}18\%$

- Tech stocks: $\theta \approx 25\text{-}30\%$

- Defensive stocks: $\theta \approx 12\text{-}15\%$

**Half-life formula:**

$$
t_{1/2} = \frac{\ln(2)}{\kappa}
$$

Example: $\kappa = 3$ → $t_{1/2} = 84$ days

**Trading implication:** If volatility spikes 20% above mean, expect ~50% reversion in 84 days.

### 3. Why Mean Reversion Exists Economically

**1. Leverage cycling:**

$$
\text{Leverage}_t = \frac{\text{Assets}}{\text{Capital}}
$$

High volatility → Losses → Deleveraging → Less volatility
Low volatility → Gains → Relevering → More volatility

**Self-correcting mechanism.**

**2. Risk targeting:**

Institutional investors target constant risk:

$$
\text{Position Size} = \frac{\text{Target Vol}}{\text{Asset Vol}}
$$

High asset vol → Reduce position → Less price impact → Lower vol
Low asset vol → Increase position → More price impact → Higher vol

**3. Option hedging feedback:**

Market makers dynamically hedge:

- High vol → More rebalancing → Dampens moves → Vol decreases

- Low vol → Less rebalancing → Amplifies moves → Vol increases

**4. Behavioral overcorrection:**

$$
\sigma_{\text{implied}} = \sigma_{\text{rational}} + \beta \cdot \text{Fear/Greed}
$$

Fear spikes during crises (IV overshoot), then normalizes
Greed peaks during calm (IV undershoot), then reality hits

### 4. The Volatility Risk Premium in Mean Reversion

**Standard vol risk premium:**

$$
\mathbb{E}[\sigma_{\text{implied}} - \sigma_{\text{realized}}] > 0
$$

Typically 3-5% annualized.

**Mean reversion premium (additional):**

When selling volatility after spikes:

$$
\text{Total Premium} = \underbrace{3\text{-}5\%}_{\text{Base VRP}} + \underbrace{5\text{-}10\%}_{\text{Mean reversion premium}}
$$

**Why so large after spikes?**

1. **Peak fear pricing:** IV overstates true risk

2. **Forced selling over:** Deleveraging complete

3. **Technical support:** Volatility stabilizing mechanisms activate

4. **Time diversification:** Spikes don't persist

**Example:**

Normal times: IV = 18%, RV = 15% → VRP = 3%
After spike: IV = 35%, RV normalizes to 20% → VRP = 15%

**Mean reversion captures that extra 12%.**

### 5. The Term Structure of Mean Reversion

**Near-term volatility mean-reverts faster than long-term:**

$$
\text{Reversion Speed} \propto \frac{1}{\sqrt{T}}
$$

```
Mean Reversion Half-Life:
1-month options:  30-40 days
3-month options:  60-90 days
1-year options:   180-240 days
```

**Trading implication:**

Sell near-term vol after spikes (fast reversion)
Buy long-term vol after compression (slow reversion, more convexity)

### 6. Professional Institutional Perspective

**Institutional mean reversion strategies:**

**1. Systematic vol sellers:**

- Run continuous short volatility programs

- Size inversely to IV percentile

- Harvest vol risk premium + mean reversion premium

**Typical sizing:**

$$
\text{Position Size} = \frac{\text{Base Size}}{\text{IVR}} \times \frac{100}{100}
$$

At IVR 20%: 5× base size
At IVR 80%: 1.25× base size

**2. Crisis alpha funds:**

- Buy volatility in extended low-vol regimes

- Wait for mean reversion spike

- Target 200-500% returns

**Entry criteria:**

- VIX < 12 for 3+ months

- Implied correlation < 20%

- Leveraged loan issuance elevated

- Put/call skew compressed

**3. Volatility arbitrage:**

- Trade mispricings in mean reversion speed

- Exploit differences across assets

- Statistical arbitrage approach

**4. Risk parity funds:**

- Use mean reversion for portfolio rebalancing

- High vol → Reduce equity → Sell vol

- Low vol → Increase equity → Buy vol

### 7. The Empirical Evidence

**Historical mean reversion statistics:**

**SPX Implied Volatility (1990-2024):**
```
Long-run mean: 17.2%
Standard deviation: 8.4%
Half-life: 92 days
Auto-correlation (30-day): 0.78
```

**Mean reversion trades (backtested):**

**Short vol after spikes (IVR > 80):**

- Win rate: 82%

- Average return: +24% in 60 days

- Average loss: -45% (tail events)

- Sharpe ratio: 0.85 (with proper sizing)

**Long vol after compression (IVR < 20):**

- Win rate: 45%

- Average return: +180% (when wins)

- Average loss: -30% (theta decay)

- Sharpe ratio: 0.45 (asymmetric payoff)

**Key insight:** Short vol mean reversion has higher win rate but catastrophic tail risk. Long vol mean reversion has lower win rate but convex payoffs.

### 8. When Mean Reversion Offers Edge

**Genuine edge exists when:**

**For short volatility (after spikes):**

1. **IVR > 70%:** Volatility at extreme levels

2. **Trigger event resolved:** Crisis/event passed

3. **Deleveraging complete:** Forced selling exhausted

4. **Term structure inverted:** Front >> Back (normalizes)

5. **Skew elevated:** Put skew will compress

**Expected edge:** 10-20% premium over 30-60 days

**For long volatility (after compression):**

1. **IVR < 20%:** Volatility unusually suppressed

2. **Complacency indicators:** Low put/call ratio, tight credit spreads

3. **Leverage elevated:** Record margin debt, covenant-lite loans

4. **Duration extended:** Low VIX for 3+ months

5. **Macro tensions building:** Unreflected risks

**Expected edge:** Convex payoff with 200%+ upside

**Fair pricing (no edge) when:**

- IVR 30-60% (normal range)

- No recent spike or compression

- Term structure normal

- No macro stress or complacency

Understanding these economic foundations helps recognize when mean reversion strategies offer genuine edge versus when you're just taking on risk without adequate compensation.

---

## The P&L Formula

### 1. Primary P&L Driver — Volatility Normalization

$$
\text{P\&L}_{\text{MR}} =
\mathcal{V} \cdot (\sigma_{\text{entry}} - \sigma_{\text{exit}})
$$

- Short vol: profit if volatility declines

- Long vol: profit if volatility rises

**Incorporating mean reversion explicitly:**

$$
\text{P\&L}_{\text{MR}} = \mathcal{V} \cdot \left[(\sigma_0 - \bar{\sigma}) \cdot (1 - e^{-\kappa t})\right]
$$

where:

- $\sigma_0$ = entry volatility

- $\bar{\sigma}$ = long-run mean

- $\kappa$ = mean reversion speed

- $t$ = time held

**Example:**

Entry: IV = 35%, Long-run mean = 18%, $\kappa = 3$
After 30 days: Expected reversion = $(35-18) \times (1-e^{-3 \times 30/365}) = 3.8\%$

If vega = $100/\%, then Expected P&L = $100 × 3.8 = $380

---

### 2. Secondary Effects

- **Theta:** Often positive when selling vol

- **Gamma:** Negative for short vol, positive for long vol

- **Delta:** Hedged or minimized

---

## Concrete Example

### 1. Short Volatility After a Spike

**Underlying:** SPX  

**Spot:** 4400  

**VIX:** 38 (historical avg ≈ 20)

**Trade:**

- Sell 30-day ATM straddle

- Delta hedge

**Thesis:**

- Volatility spike caused by temporary shock

- Expect normalization

**Entry:**

- Sell straddle for $160 (IV = 38%)

- Vega: -$200 per 1% IV

- Theta: +$8/day

- Gamma: -0.03

**Scenario: Mean reversion works**

**Week 1:** VIX drops to 30

- Straddle now worth $120

- **P&L: +$40** (25%)

**Week 2:** VIX to 25

- Straddle worth $90

- **P&L: +$70** (44%)

**Week 3:** VIX to 22

- Straddle worth $70

- **P&L: +$90** (56%)

**Exit at day 21:** Close at $70

- **Total profit: $90 on $160 position** = 56% in 3 weeks

**Return annualized:** ~430%

---

## Risk Management

### 1. Key Risks

- Volatility can stay elevated longer than expected

- Regime shifts (new normal)

- Gap risk

- Correlation breakdown

- Model overconfidence

---

### 2. Risk Controls

- Trade smaller size at extremes

- Scale in gradually

- Use defined-risk structures

- Diversify across maturities

- Hard stop-loss rules

**Position sizing for mean reversion:**

$$
\text{Position Size} = \frac{\text{Base Size}}{1 + |\text{IVR} - 50|/100}
$$

At IVR 80%: Position = Base / 1.30 = 77% of normal
At IVR 20%: Position = Base / 1.30 = 77% of normal

**Smaller positions at extremes** (where you want to trade!) because:

- Higher risk of regime shift

- Larger adverse moves possible

- More uncertainty about timing

---

## Relationship to Other Volatility Strategies

| Strategy | Primary Focus |
|--------|---------------|
| IV–RV trading | Volatility risk premium |
| Skew trading | Asymmetry |
| Term structure trading | Time dimension |
| **Mean reversion** | **Volatility level dynamics** |
| Surface arbitrage | Full surface |

> **Mean reversion is the backbone of volatility trading.**

---



## Practical Guidance

[Continue with existing practical guidance sections...]


**Step-by-step implementation framework:**

### 1. Step 1

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

### 2. Step 2

**Enter SHORT volatility when:**

- IVR > 70% (extreme high volatility)

- Trigger event resolved or resolving

- Credit markets functioning normally

- Term structure inverted (front > back)

- Historical analogs suggest mean reversion

**Avoid SHORT volatility when:**

- IVR < 50% (not enough edge)

- Ongoing systemic crisis

- Financial system stress

- Unknown/mysterious volatility source

- Potential regime shift

**Enter LONG volatility when:**

- IVR < 20% (extreme compression)

- Complacency indicators elevated

- Leverage metrics at extremes

- Low volatility persisted 3+ months

- Building macro tensions

**Avoid LONG volatility when:**

- IVR > 40% (too expensive)

- Recent vol spike (theta decay high)

- No clear catalyst

- Markets trending calmly

### 3. Step 3

**Calculate maximum position size:**

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times \text{Risk\%}}{\text{Max Loss Per Contract}}
$$

**For mean reversion strategies specifically:**

$$
\text{Position Size} = \frac{\text{Base Size}}{1 + \frac{|\text{IVR} - 50|}{100}} \times \text{Regime Factor}
$$

where:

- Base Size = normal position (1-2% of portfolio)

- Regime Factor = 0.5 (crisis), 1.0 (normal), 1.5 (stable)

**Example:**

Portfolio: $100k
IVR: 80% (selling vol after spike)
Regime: Post-crisis stabilizing (Factor = 0.7)

$$
\text{Size} = \frac{$2,000}{1 + 0.30} \times 0.7 = \$1,077
$$

**Conservative maximum vega exposure:**

- $100-200 per 1% IV move per $10k capital

- At extremes (IVR > 80 or < 20): Reduce to $50-100

### 4. Step 4

**Best practices:**

1. **IV percentile confirmation:** Check 252-day IVR

2. **Regime check:** Crisis vs. normal vs. complacent

3. **Liquidity verification:** Bid-ask < 10% of mid

4. **Scale in:** Enter 1/3 immediately, 1/3 after 3 days, 1/3 after week

**Entry checklist:**

- [ ] IV percentile checked and extreme (>70% or <20%)

- [ ] Regime identified (spike vs. shift)

- [ ] Trigger event known or resolved

- [ ] Position sized for worst case

- [ ] Greeks calculated

- [ ] Stop loss defined

- [ ] Profit target set

### 5. Step 5

**Active monitoring:**

**Daily:**

- IV percentile changes

- VIX level and direction

- Underlying price vs. strikes

- Greeks (especially gamma near expiry)

**Weekly:**

- IV term structure evolution

- Realized vol vs. implied

- Profit/loss attribution

- Risk metrics

**Profit targets:**

**For short vol (mean reversion from spike):**

- Take 25% off at 30% of max profit

- Take 50% off at 50% of max profit  

- Take remaining at 75% of max profit

- **Never hold for last 20%** (gamma risk)

**For long vol (mean reversion from compression):**

- Take 50% off at 100% gain

- Take remaining at 200% gain or on vol spike

- Cut at -50% if no spike within expected timeframe

**Loss limits:**

**Short vol stop loss:**
$$
\text{Stop} = \text{Premium Received} \times 2.5
$$

**Long vol stop loss:**

- -50% of premium paid, or

- 50% of expected holding period passed with no favorable move

### 6. Step 6

**When to adjust (short vol):**

**Trigger 1: Stock move**

- Stock moves >2 standard deviations

- Delta exposure exceeds threshold

**Action:** 

- Rehedge delta

- Or roll strikes to new ATM

- Or close and reenter

**Trigger 2: IV re-expansion**

- IV increases back above entry level

- IVR moves 20+ points higher

**Action:**

- Close 50% immediately

- Evaluate regime (spike or shift?)

- Tighten stops on remaining

**Trigger 3: Time decay insufficient**

- Not collecting expected theta

- Position not improving

**Action:**

- Close and redeploy elsewhere

- Accept small loss

### 7. Step 7

**For each trade, record:**

```
Trade Journal Template:

Date: [Entry date]
Underlying: [Asset]
Strategy: Short/Long Vol Mean Reversion

Entry Conditions:

- IV: [Level] (IVR: [%])

- VIX: [Level]

- Regime: [Spike/Compression/Normal]

- Trigger: [What caused extreme]

Position:

- Structure: [Straddle/Strangle/etc]

- Size: [Contracts]

- Premium: [Collected/Paid]

- Greeks: Δ=[X], Γ=[X], 𝒱=[X], Θ=[X]

Exit Conditions:

- Date: [Exit date]

- IV: [Level] (IVR: [%])

- Reason: [Profit target/Stop/Time]

P&L Attribution:

- Vega: $[X]

- Theta: $[X]  

- Gamma: $[X]

- Total: $[X] ([%])

Lessons:

- What worked: [...]

- What didn't: [...]

- Next time: [...]
```

**Quarterly review:**

- Win rate by IVR entry level

- Average hold time by regime

- Profit factor by strategy variant

- Worst trades (what went wrong)

- Best trades (what went right)

### 8. Common Execution Mistakes to Avoid

1. **Selling vol at low IV** - IVR < 30 usually poor for short vol

2. **Buying vol at high IV** - IVR > 70 often too expensive for long vol

3. **Confusing spike with regime shift** - Critical distinction!

4. **Over-leveraging at extremes** - Reduce size when most confident

5. **Holding through last week** - Gamma explosion destroys positions

6. **Not taking profits early** - Greed kills mean reversion trades

7. **Fighting the regime** - If wrong about spike vs. shift, exit fast

8. **Ignoring credit markets** - Credit stress = regime shift signal

### 9. Professional Implementation Tips

**For mean reversion selling (after spikes):**

**Entry criteria:**

- IVR > 70%

- Clear trigger event (resolved or resolving)

- Credit spreads stable or tightening

- Deleveraging appears complete

- Historical analog exists

**Exit criteria:**

- Take 50% at 50% of max profit

- Full exit at 75% of max profit

- Stop loss: 2.5× premium received

- Time stop: 7-10 days before expiry

**Expected metrics:**

- Win rate: 75-80%

- Average winner: +30-45%

- Average loser: -50% (cut quickly!)

- Hold time: 15-30 days

**For mean reversion buying (after compression):**

**Entry criteria:**

- IVR < 20%

- Low volatility persisted 3+ months

- Complacency indicators (low put/call, tight spreads)

- Leverage metrics elevated

- Building but unreflected risks

**Exit criteria:**

- Take 50% at 100% gain

- Full exit at 200% gain or vol spike

- Stop loss: -50% of premium

- Time stop: 50% of expected time with no movement

**Expected metrics:**

- Win rate: 40-50%

- Average winner: +150-250%

- Average loser: -40%

- Hold time: 30-90 days (patience required!)

---

## Real-World Examples

### 1. Pension Duration Cut via Futures

**Setup:**

- Date: August 24, 2015

- Event: China devalued yuan, flash crash in US

- VIX: Spiked from 12 → 40 in 3 days

- SPX: Dropped from 2100 → 1970 (-6%)

**Analysis:**

- IVR: 95% (extreme)

- Trigger: Known event (China devaluation)

- Credit markets: Functioning normally

- Regime: Clear spike, not systemic crisis

**Trade (August 26):**

- Sold 5x SPX 1970 straddles @ $105

- Collected: $52,500

- Vega: -$650 per 1% IV

**Outcome:**

- 28 days later: VIX declined 39 → 16

- Closed at $52.50 (50% profit)

- **Return: +52% in 28 days**

**Why it worked:**

- Correctly identified temporary spike

- No systemic risk

- Fast mean reversion (as predicted)

- Took profits early

### 2. Transition Risk Hedge

**Setup:**

- Date: February 5, 2018

- VIX: At 12, thought to be "too low"

- XIV (short vol ETN) very popular

**Analysis (WRONG):**

- Traders thought: "VIX 12 is compressed, sell vol for income"

- Actually: VIX could spike from low base

**What happened:**

- VIX exploded from 12 → 50+ in ONE day

- XIV lost 96% and was terminated

- Short vol positions destroyed

**Lesson:**

- This wasn't mean reversion FROM spike

- This was spike FROM compression

- **Wrong direction for mean reversion!**

- Many confused "low VIX" with "spike to fade"

### 3. Portable Alpha with Futures

**Setup:**

- Date: Mid-March 2020

- VIX: Spiked to 60+

- Many traders thought: "Fade the spike"

**Analysis (WRONG):**

- This wasn't temporary spike

- This was regime shift (pandemic)

- Uncertainty was RISING, not resolving

**What happened:**

- VIX stayed 40+ for months

- "Mean reversion" trades blown up

- Volatility didn't normalize until summer

**Lesson:**

- Distinguish spike (temporary) from regime shift (persistent)

- When trigger ongoing and unknown, it's NOT a spike to fade

- Wait for resolution signals before selling vol

### 4. Tactical Duration Extension

**Setup:**

- Year: 2017

- VIX: Stayed 8-12 entire year (extreme compression)

- Many bought vol expecting mean reversion

**Analysis:**

- IVR: < 10% for months

- Seemed like perfect long vol setup

- Expected reversion to 16-18

**What happened:**

- VIX stayed suppressed all year

- Long vol positions bled theta

- Losses of 50-80% common

**Lesson:**

- Mean reversion can take VERY long

- Low vol regimes can persist

- Need catalyst, not just "it's too low"

- Position sizing must allow for 6-12 month holds

### 5. Duration Hedge Failure in Crisis

**Setup:**

- Date: October 4, 2011

- Event: European debt crisis panic

- VIX: Spiked to 48

**Analysis:**

- IVR: 98%

- Trigger: European sovereign debt (known issue)

- Governments working on solution

**Trade (October 5):**

- Sold straddles at elevated IV

- Expected normalization as Europe resolved

**Outcome:**

- VIX declined 48 → 22 in 6 weeks

- **Return: +65% in 45 days**

**Why it worked:**

- Clear trigger

- Government action forthcoming

- Historical analog (2008 had similar resolution)

---

## Key Takeaways

### 1. Core Principles

1. **Volatility mean reverts** - but timing is uncertain

2. **Spikes are temporary** - but regime shifts are not

3. **Extremes offer edge** - but also maximum risk

4. **Size inversely to conviction** - most confident = smallest position

5. **Take profits early** - don't wait for perfection

### 2. Critical Distinctions

**Spike vs. Regime Shift:**

| Spike | Regime Shift |
|-------|--------------|
| Known trigger | Unknown/ongoing trigger |
| Temporary event | Structural change |
| Fast reversion (weeks) | Slow reversion (months/years) |
| Trade it! | Wait it out |

**Mean Reversion Speed:**

- Normal markets: 90-120 day half-life

- Crisis markets: 180-365 day half-life

- Can't use normal assumptions in crisis!

### 3. Position Sizing Rules

**Iron laws:**

1. **Max vega exposure:** $100-200 per 1% IV per $10k capital

2. **Reduce at extremes:** When IVR > 80 or < 20, cut size in half

3. **Regime adjustment:** In crisis, cut size to 1/3 of normal

4. **Stop losses:** Always defined before entry

5. **Profit targets:** Take 50% off at 50% of max profit

### 4. Success Metrics

**For short vol mean reversion:**

- Win rate: 75-80% (if selective)

- Average winner: +30-45%

- Average loser: -40-60%

- Requires: Small size, fast stops, early profits

**For long vol mean reversion:**

- Win rate: 40-50%

- Average winner: +150-250%

- Average loser: -40-50%

- Requires: Patience, catalysts, asymmetric sizing

### 5. The Mental Model

**Think of volatility like a rubber band:**

- Stretched high (IVR > 70): Will snap back, but how fast?

- Compressed low (IVR < 20): Will expand, but when?

- Normal range (IVR 30-60): No edge

**Your job:** Identify extremes, size for uncertainty, take profits early.

**Not your job:** Predict exact turning point, hold for maximum profit, fight regime shifts.

---

## Final Wisdom

> **"Sell fear, buy complacency—but size for the possibility you're wrong about which one it is."**

**Mean reversion is the most reliable phenomenon in volatility markets, yet the hardest to time. Trade it with humility, not hubris.**

---

## One-Line Summary

> **Volatility mean reversion strategies trade extremes in uncertainty, betting that fear and complacency are temporary—but only when you can distinguish a spike from a regime shift.**