# Jade Lizard and Big Lizard

**Jade Lizard** is an income strategy combining a short put with a short call spread, creating a credit position with no upside risk (cannot lose if stock rallies) but defined downside risk, popular among traders seeking premium collection with asymmetric risk profiles.









---

## The Core Insight

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_capital_efficiency.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**The fundamental idea:**

- Traditional short put: Collect premium, risk if stock drops
- Traditional short call spread: Collect premium, risk if stock rallies
- **Jade Lizard: Combine both** → Collect more premium, eliminate upside risk
- Key feature: Net credit > call spread width (no upside risk)
- Downside risk only (if stock crashes below short put)
- Popular for bullish-to-neutral income generation

**The key equation:**

$$
\text{Net Credit} > (K_{\text{call high}} - K_{\text{call low}})
$$

This ensures **zero upside risk** (credit collected exceeds max call spread loss).

**You're essentially betting: "Stock won't crash (short put safe) and I'm willing to cap my upside risk (call spread) to collect maximum premium."**

---

## What Is a Jade Lizard?

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_components.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Before trading Jade Lizards, understand the structure:**

### 1. Standard Jade Lizard

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_credit_vs_width.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Definition:** Sell OTM put + Sell OTM call spread (higher strikes).

**Structure:**

- **Sell 1×** OTM put at strike $K_P$ (e.g., $95 put)
- **Sell 1×** OTM call at strike $K_{C1}$ (e.g., $105 call)
- **Buy 1×** higher OTM call at strike $K_{C2}$ (e.g., $110 call)
- Same expiration
- Net: Credit collected

**Example:**

- Stock at $100
- Sell $95 put for $3.50
- Sell $105 call for $2.50
- Buy $110 call for $0.80
- **Net credit: $3.50 + $2.50 - $0.80 = $5.20**
- **Call spread width: $110 - $105 = $5**
- **Credit > Width:** $5.20 > $5 ✓ (no upside risk!)

**Payoff at expiration:**

| Stock Price | Put P&L | Call Spread P&L | Total P&L |
|-------------|---------|-----------------|-----------|
| $80 | -$15 (assigned) | +$1.70 (keep credit) | **-$13.30** |
| $90 | -$5 (assigned) | +$1.70 | **-$3.30** |
| $95 | $0 | +$1.70 | **+$1.70** |
| $100 | $0 | +$1.70 | **+$1.70** |
| $105 | $0 | +$1.70 | **+$1.70** |
| $108 | $0 | -$1.30 ($3 ITM - $1.70 credit) | **-$1.30** |
| $110+ | $0 | -$3.30 (max loss) | **-$3.30** |

**But wait - at $110:**

- Put expires worthless: Keep $3.50
- Call spread max loss: -$5 (width)
- **Net: $3.50 - $5 = -$1.50?**

Let me recalculate:

**At $110 (stock above call spread):**

- Put: Expires worthless (sold for $3.50, keep it)
- Call spread: Max loss = -($110 - $105) = -$5
- **Total: $3.50 - $5 = -$1.50 loss**

**Wait, this violates the "no upside risk" claim!**

Let me reconsider. The net credit collected was $5.20. Let's trace through again:

**Total credit collected upfront:** $5.20

**At expiration, if stock at $110+:**

- Short $105 call: Must pay ($110 - $105) = $5
- Long $110 call: Receive ($110 - $110) = $0
- **Call spread loss: -$5**
- **Net P&L: $5.20 credit - $5 loss = +$0.20**

**Ah! The credit ($5.20) EXCEEDS the spread width ($5), so worst case upside is +$0.20 profit.**

This is the key to Jade Lizard: **Credit must exceed call spread width.**

### 2. Big Lizard (Variation)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_greeks.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Definition:** Jade Lizard with WIDER call spread to collect more premium.

**Structure:**

- Sell OTM put
- Sell OTM call spread with **wider width** (e.g., $10 instead of $5)
- Collect larger credit BUT more upside risk

**Example:**

- Stock at $100
- Sell $95 put for $3.50
- Sell $105 call for $2.50
- Buy $115 call for $0.20 (wider spread)
- **Net credit: $5.80**
- **Call spread width: $10**
- **Credit < Width:** $5.80 < $10 (has upside risk!)

**This is NOT a pure Jade Lizard** (has upside risk), but collects more premium.

**Trade-off:**

- More premium ($5.80 vs $5.20)
- But upside risk exists (if stock rallies hard)

**Figure 1:** Payoff diagram for Jade Lizard showing no upside risk (flat or small profit above call spread), maximum profit in the middle range, and downside risk below short put strike.

---

## Economic

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_lizard_payoff.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Beyond the basic definition, understanding what Jade Lizards REALLY are economically:**

### 1. Decomposition into Components

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_scenarios.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Jade Lizard = Short Put + Short Call Spread**

**Short Put component:**

- Collect premium
- Risk: Stock drops below strike
- Obligation: Buy stock at strike if assigned

**Short Call Spread component:**

- Collect premium (sell $105 call, buy $110 call)
- Risk: Stock rallies above $105
- Max loss: Width of spread ($5)
- Capped upside risk

**Combined effect:**

$$
\text{Jade Lizard} = \underbrace{\text{Short Put}}_{\text{Downside risk}} + \underbrace{\text{Short Call Spread}}_{\text{Capped upside risk}}
$$

**Key insight:** By ensuring **credit > call spread width**, you eliminate upside risk entirely.

### 2. Why Eliminate Upside Risk?

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_vs_big_lizard.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Market bias: Equities have upside drift**

Historical data shows:
- **Long-term equity trend:** UP (~10% annually)
- **Crash risk:** DOWN (fat left tail)
- **Distribution:** Negatively skewed

**Strategic logic:**

- Don't want to lose money if stock rallies (market's natural tendency)
- **Willing to take downside risk** (lower probability in bull market)
- Jade Lizard aligns with market bias

**Comparison to alternatives:**

**Short strangle (sell put + sell call):**

- Risk on BOTH sides (downside AND upside)
- Unlimited risk on both ends

**Jade Lizard (sell put + sell call spread):**

- Risk on downside ONLY
- **No upside risk** (capped by call spread, offset by credit)

**Trade-off:**

- Collect less premium than strangle
- But eliminate upside risk (sleep better)

### 3. The "Lizard" Name Origin

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_vs_strangle.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Why "Jade Lizard"?**

- Coined by options educators (tastytrade community)
- "Jade" = valuable (high premium collection)
- "Lizard" = agile, low risk (eliminates upside risk)
- Contrasts with "Iron Condor" (sells both sides with defined risk)

**Big Lizard:**

- Wider call spread (bigger "lizard")
- More premium but violates no-upside-risk rule

---

## Key Terminology

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_lizard_payoff.png?raw=true" alt="jade_lizard" width="700">
</p>

**Jade Lizard:**

- Short put + short call spread
- Net credit > call spread width (no upside risk)
- Also called: "No-Risk Call Spread Collar" (less common)

**Big Lizard:**

- Jade Lizard with wider call spread
- Credit < call spread width (has upside risk)
- Trade-off: More premium for accepting upside risk

**Short Put:**

- Obligation to buy stock at strike if assigned
- Downside risk (stock drops below strike)
- Collect premium

**Short Call Spread:**

- Sell lower call, buy higher call
- Capped upside risk (width of spread)
- Collect net premium

**Breakeven:**

Lower breakeven only (no upper breakeven due to no upside risk):

$$
\text{BE}_{\text{lower}} = K_{\text{put}} - \text{Net Credit}
$$

**Example:**

- Short $95 put, net credit $5.20
- **BE: $95 - $5.20 = $89.80**

---

## Why Trade Jade Lizards?

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/jade_lizard_theta.png?raw=true" alt="jade_theta" width="700">
</p>

**Use cases:**


---

## Economic

**Understanding what jade lizards REALLY represent economically:**

### 1. The Core Economic Trade-Off

Jade lizards represent a sophisticated economic proposition: **Eliminating upside risk by collecting enough premium to exceed call spread width**. This transforms a traditional short strangle (unlimited risk both sides) into a directionally-optimized income structure with defined upside risk and undefined downside risk.

**Economic equivalence:**

$$
\text{Jade Lizard} = \underbrace{\text{Short Put}}\_{\text{Downside Risk}} + \underbrace{\text{Bear Call Spread}}\_{\text{Capped Upside}}
$$

**The critical constraint:**

$$
\text{Credit} > \text{Call Spread Width} \implies \text{No Upside Risk}
$$

**Example:**
- Collect $6.50 credit
- Call spread: $5 wide
- **$6.50 > $5:** Even if call spread max loss, still profit $1.50 ✓

**Why this matters economically:**
- **Short strangle:** Unlimited risk both directions (terrifying)
- **Iron condor:** Defined risk both sides, but lower credit
- **Jade lizard:** Eliminated upside risk, maximize credit, accept downside risk
- **Trade-off:** Accepted undefined downside in exchange for no upside cap + maximum premium

### 2. Why This Structure Exists Economically

Markets create jade lizards because of **asymmetric risk preferences and directional conviction**:

**1. Bullish bias with income optimization:**

**The common investor problem:**
- Portfolio: Long equities (inherently bullish)
- Want: Generate income from premium
- **Challenge:** How to collect premium without capping upside?

**Traditional solutions fail:**

**Covered call:**
- Caps upside at strike
- **Problem:** Miss rallies (opportunity cost)
- **Example:** Stock rallies 20%, you only get 5% (called away)

**Short put:**
- Collect premium
- Unlimited downside (same as owning stock)
- **Problem:** No upside income

**Cash-secured put:**
- Same as short put
- Ties up cash
- **Problem:** Capital inefficiency

**Jade lizard solves this:**
- Collect premium from BOTH put and call
- Call spread defines upside (but credit > width = no risk!)
- **Result:** Maximum credit + no upside cap + bullish positioning

**Economic truth:** Jade lizards are how bullish investors monetize their conviction while protecting participation in rallies.

**2. Volatility smile exploitation with directional tilt:**

**The skew reality (equity markets):**

$$
\text{IV}_{OTM\;Put} > \text{IV}_{ATM} > \text{IV}_{OTM\;Call}
$$

**Jade lizards exploit TWO skew inefficiencies:**

**Put side:**
- OTM puts have elevated IV (crash fear)
- Sell expensive put premium
- **Collect overpriced insurance**

**Call side:**
- OTM calls have lower IV (rally skepticism)
- Sell call spread (defined risk)
- **Width cheap relative to put**

**Net effect:**
- Put premium (rich) + call spread premium (moderate) > call spread width
- **Credit exceeds max call risk:** Free upside participation!

**Example:**
- Sell $165 put: IV 35%, collect $5.00 (rich)
- Sell $185/$190 call spread: IV 28%/26%, collect $1.80 (cheap)
- **Total credit:** $6.80
- **Call spread width:** $5.00
- **Edge:** $1.80 excess from skew differential

**3. Capital efficiency through margin optimization:**

**Comparing capital requirements:**

**Long 100 shares at $175:**
- Capital: $17,500
- Upside: Unlimited
- Downside: -$17,500 (to zero)

**Jade lizard (same exposure):**
- Short $165 put + $185/$190 call spread
- **Margin requirement:** ~$3,000 (for short put)
- Call spread: No additional margin (defined risk)
- **Total capital:** $3,000 vs $17,500

**ROI comparison:**
- Stock: $5 rally = +2.9% ($5/$175)
- Jade lizard: Collect $6.50 = **+217%** ($6.50/$3 margin)

**Why 72× better ROI?**
- Leveraging margin, not cash
- Collecting premium from two sides
- **Trade-off:** Undefined downside (like owning stock)

### 3. Professional Institutional Perspective

**How institutions use jade lizards:**

**1. Enhanced covered call replacement:**

**Traditional institution problem:**
- Long $50M equity portfolio
- Want income without capping rallies
- Covered calls leave $20M on table annually

**Jade lizard solution:**
- Sell jade lizards against index (SPY)
- Collect $300k monthly ($3.6M annually)
- **No upside cap:** Participate in all rallies
- Risk: Downside (but already have long equity hedge)

**Economic benefit:**
- $3.6M income (covered calls: $2.8M)
- **Extra $800k (29% more)**
- Plus: Full rally participation

**2. Volatility harvesting in trending markets:**

**Professional vol traders know:**
- Trending markets = persistent directional bias
- Volatility premium exists on BOTH sides
- **Jade lizard harvests both**

**Example:**
- Bull market: SPY trending up
- Put IV: 32% (elevated, fear still present)
- Call IV: 25% (lower, rally expected)
- **Sell jade lizard monthly:** Harvest put fear + call premium

**Annual strategy:**
- 12 months × $6 credit = $72 potential
- Win rate: ~70% (market continues up or stable)
- **Expected:** $50.40 per year (70% × $72)
- **vs. long stock:** Adds 5-7% annual return on top of market gains

**3. Post-earnings IV crush capture:**

**Institutional edge:**
- Better earnings models
- Know actual move < implied move
- **Jade lizard captures IV crush + directional bias**

**Example:**
- AAPL earnings tomorrow, IV 65%
- Models predict: 3% move (market prices 5%)
- **Post-earnings jade lizard:**
  - Enter right after announcement
  - IV crushes 65% → 35%
  - Collect rich premium, IV working for you
  - **Close after 1-2 days:** 60-80% of max profit

**Why it works:**
- Volatility overpriced before events
- Institutions sell overpriced vol
- Jade lizard maximizes collection

**4. Portfolio yield enhancement:**

**Hedge fund strategy:**
- Core: Long/short equity
- **Overlay:** Jade lizards for income
- Generate 3-5% additional yield

**Structure:**
- Sell jade lizards on SPY (broad market)
- ~2% OTM on both sides
- 30-45 DTE
- **Roll monthly:** Close at 50% profit, re-enter

**Annual result:**
- 12 opportunities × $6 average × 70% success
- **Income:** $50.40 per lizard per year
- On $500M AUM: $8.4M additional return (1.7% alpha)

### 4. The Behavioral Finance Angle

**Why jade lizards offer edge:**

**1. Fear asymmetry:**
- Investors fear crashes (puts expensive)
- Investors skeptical of rallies (calls cheap)
- **Jade lizard benefits from both:**
  - Sell expensive puts (monetize fear)
  - Sell call spread (cheap insurance)

**2. Covered call mentality:**
- Retail loves covered calls (feels "safe")
- **Problem:** Caps upside, misses 20%+ rallies
- **Jade lizard:**
  - Psychological: "Still bullish" (no stock owned, but same exposure)
  - Economic: Better returns, no cap

**Retail resistance to jade lizards:**
- "Don't own stock feels risky"
- "What if it crashes?"
- **Reality:** Economically identical to covered call + naked put!

**Professional advantage:**
- Understand equivalence
- Overcome psychological barrier
- **Capture edge from retail reluctance**

**3. Trending market bias:**
- After 3-month rally: Everyone bullish
- **Jade lizard perfect:**
  - Bullish structure (matches sentiment)
  - No upside cap (catches continued rally)
  - Collect premium (monetize optimism)

### 5. The Mathematics of Jade Lizard Economics

**Break-even probability:**

For jade lizard to be profitable long-term:

$$
P(\text{Win}) \times \text{Credit} > P(\text{Loss}) \times \text{Avg Loss}
$$

**Example:**
- Credit: $6.50
- Upside max loss: $0 (credit > call width)
- Downside breakeven: $165 - $6.50 = $158.50

**If stock > $158.50:** Profit (any amount from $0.01 to $6.50)

**Probability calculation:**
- Stock at $175, 30 DTE
- Historical vol: 20%
- 30-day move: 20% × √(30/365) = 5.7%
- **1 std dev:** $165-$185

**Breakeven:** $158.50 (1.3 std dev down)
**Probability below $158.50:** ~10%

**Expected value:**
- Win (90%): Avg profit $4.50
- Loss (10%): Avg loss $12 (estimate)

**EV:** 0.90 × $4.50 - 0.10 × $12 = $4.05 - $1.20 = **+$2.85 per trade** (positive edge!)

**Key insight:** High win rate (90%+) overcomes occasional large downside losses.

### 6. Understanding the Economic Foundations

**Key insights from jade lizards:**

**1. Upside risk elimination is valuable:**
- Removing even small probability (10%) of upside loss
- **Enables:** Full rally participation
- **Worth:** Accepting larger downside risk

**2. Credit > width is powerful:**
- Mathematical guarantee: No upside loss
- **Psychological:** Feel protected on upside
- **Economic:** Maximum income extraction

**3. Directional + income combined:**
- Most strategies: Direction OR income
- **Jade lizard:** Direction AND income
- **Edge:** Dual exposure hard to price

**4. Margin efficiency creates leverage:**
- Use $3k margin to control $17.5k exposure
- **6× leverage** (vs buying stock)
- **Risk:** Same as owning stock (downside)
- **Benefit:** Higher ROI on capital

**5. Trending markets = persistent edge:**
- Mean reversion strategies fail in trends
- **Jade lizards benefit from trends:**
  - Bullish markets: Put premium stays elevated (fear lingers)
  - Collect monthly, stock stays above strikes
  - **Compound:** 12× per year

**The economic truth:**
- Jade lizards don't create "free money"
- They **optimize risk allocation** for bullish conviction
- **Edge comes from:**
  - Being right about direction (bullish)
  - Volatility skew exploitation
  - Capital efficiency
  - Eliminating upside cap
- **Success requires:**
  - Correct bullish bias
  - Proper strike selection
  - Accepting downside risk consciously

Understanding economic foundations helps you recognize:
- When jade lizards offer edge (trending up markets + elevated put IV)
- When to avoid (bearish markets, low IV)
- How to size positions (downside risk is REAL)
- Why "no upside risk" doesn't mean "no risk" - downside is unlimited!


### 7. Bullish-to-Neutral Income (Main Use)

**Scenario:** Stock in established uptrend, want income without upside risk

**Setup:**

- AAPL at $175, strong uptrend
- Expect: Consolidation or continued rally (NOT crash)

**Trade (30 DTE):**

- Sell $165 put for $4.20
- Sell $185 call for $3.50
- Buy $190 call for $1.50
- **Net credit: $6.20**
- **Call spread width: $5**
- **No upside risk:** $6.20 > $5 ✓

**Outcomes:**

**AAPL → $180 (slight rally):**

- All expire worthless
- **Profit: $6.20** (full credit, max profit)

**AAPL → $195 (strong rally):**

- Put worthless, call spread loses $5
- **P&L: $6.20 - $5 = +$1.20** (still profit!)

**AAPL → $160 (drops):**

- Put assigned: Buy 100 shares at $165
- Shares worth $160 → Loss $5
- **P&L: $6.20 - $5 = +$1.20** (breakeven zone)

**AAPL → $150 (crashes):**

- Put assigned at $165
- Shares worth $150 → Loss $15
- **P&L: $6.20 - $15 = -$8.80** (max risk zone)

**Why this works:**

- AAPL trending up (upside protected by design)
- Collect $6.20 premium (good income)
- Only risk if crashes (lower probability)

### 8. Post-Earnings Implied Volatility Crush

**Scenario:** Stock reported earnings, IV elevated, expecting IV crush + consolidation

**Setup:**

- TSLA at $240, just reported earnings
- IV at 70% (elevated post-earnings)
- Expect: IV to normalize to 45%, stock to consolidate

**Trade (21 DTE):**

- Sell $230 put for $6
- Sell $255 call for $5
- Buy $265 call for $2
- **Net credit: $9**
- **Call spread width: $10**

**Wait, this violates no-upside-risk rule!**

Let me adjust:

**Better trade:**

- Sell $230 put for $6
- Sell $255 call for $5
- Buy $260 call for $3
- **Net credit: $8**
- **Call spread width: $5**
- **No upside risk: $8 > $5** ✓

**Outcome (one week later):**

- IV crushes: 70% → 45%
- Stock at $245 (consolidating)
- **Position value:** $1.50 (mostly decayed)
- **Can close for:** $8 - $1.50 = $6.50 profit (81% of max)

**Why this works:**

- IV crush benefits ALL short options
- Stock consolidation keeps price in safe zone
- Collected premium during high IV (optimal entry)

### 9. Low-Volatility Range-Bound Markets

**Scenario:** Market in extended low-volatility regime

**Setup:**

- SPY trading $445-$455 for 3 months
- VIX at 12 (very low)
- Expecting continued range

**Trade (45 DTE):**

- Sell $440 put for $4
- Sell $460 call for $3
- Buy $465 call for $1.20
- **Net credit: $5.80**
- **Call spread width: $5**
- **No upside risk: $5.80 > $5** ✓

**Weekly management:**

- **Week 1-3:** SPY stays $445-$455, theta working
- **Week 4:** SPY at $452, position value $1.20
- **Exit:** Close for $4.60 profit (79% of max)

**Why this works:**

- Low VIX = cheaper options (but still collect good premium)
- Range-bound eliminates directional risk
- No upside risk = perfect for slow uptrend

### 10. Replacing Covered Calls (Capital Efficiency)

**Comparison:**

**Traditional covered call:**

- Own 100 shares at $100 = $10,000 capital
- Sell $105 call for $2.50
- **Capital required: $10,000**
- **Max profit: $7.50** (if called away at $105)

**Jade Lizard alternative:**

- Sell $95 put for $3.50
- Sell $105 call for $2.50
- Buy $110 call for $0.80
- **Capital required: ~$3,000** (margin for short put)
- **Max profit: $5.20**

**Comparison:**

| Metric | Covered Call | Jade Lizard |
|--------|--------------|-------------|
| Capital | $10,000 | $3,000 |
| Max profit | $7.50 | $5.20 |
| ROI | 7.5% | 17.3% |
| Upside | Capped at $105 | No cap (above $110) |
| Risk | Own stock (full downside) | Put assignment |

**Why Jade Lizard can be better:**

- **3× capital efficiency** ($3K vs $10K)
- **2× ROI** (17% vs 7.5%)
- **No upside risk** (vs covered call capped)

---

## Greeks Behavior

### 1. Delta

**Delta calculation:**

$$
\Delta_{\text{JL}} = \Delta_{\text{put}} + \Delta_{\text{call spread}}
$$

**Example:**

- Short $95 put: Δ = +0.20 (short put = positive delta)
- Short $105/$110 call spread: Δ = -0.15
- **Net delta: +0.05** (slightly bullish)

**Delta evolution:**

- **Stock drops to $90:** Delta becomes +0.60 (put dominates)
- **Stock at $100:** Delta ≈ 0 (balanced)
- **Stock rallies to $110:** Delta ≈ 0 (call spread capped)

**Key insight:** Jade Lizard is nearly delta-neutral in target zone, slightly bullish overall.

### 2. Gamma

**Gamma:**

$$
\Gamma_{\text{JL}} = \Gamma_{\text{put}} + \Gamma_{\text{call spread}} < 0
$$

**Why negative?**

You SOLD options (short gamma). Small moves around strikes hurt.

**Example:**

- Short put gamma: -0.03
- Short call spread gamma: -0.02
- **Net gamma: -0.05**

**Practical impact:**

- Stock whipsaws around $95 or $105 → Gamma losses
- Best scenario: Stock enters safe zone and STAYS there

### 3. Theta

**Theta:**

$$
\Theta_{\text{JL}} = \Theta_{\text{put}} + \Theta_{\text{call spread}} > 0
$$

**Example:**

- Short put theta: +$0.12/day
- Short call spread theta: +$0.08/day
- **Net theta: +$0.20/day** (collect ~$20/day)

**Theta evolution:**

**Figure 2:** Theta decay collection for Jade Lizard showing positive daily theta from both short put and short call spread components, accelerating in final 2 weeks.

**Strategic timing:**

- Enter 30-45 DTE (optimal theta zone)
- Exit at 7-14 DTE or 50-70% profit (whichever first)

### 4. Vega

**Vega:**

$$
\text{Vega}_{\text{JL}} = \text{Vega}_{\text{put}} + \text{Vega}_{\text{call spread}} < 0
$$

**Example:**

- Short put vega: -0.18
- Short call spread vega: -0.12
- **Net vega: -0.30**

**Practical impact:**

- **IV increases:** Position loses value (even if stock in safe zone)
- **IV decreases:** Position gains value (vega crush helps)

**Best entry: High IV** (>60th percentile) to benefit from mean reversion.

---

## Common Pitfalls

### 1. Violating the "No Upside Risk" Rule

**The mistake:**

"I'll widen the call spread to collect more premium."

**What you missed:**

If credit < call spread width, you have upside risk (no longer a true Jade Lizard).

**Example:**

**Bad trade:**

- Sell $95 put for $3.50
- Sell $105 call for $2.50
- Buy $115 call for $0.50 (wide spread)
- **Net credit: $5.50**
- **Call spread width: $10**
- **Upside risk:** $5.50 - $10 = **-$4.50 max loss if stock rallies**

**The fix:**

- **Always ensure:** Net credit ≥ call spread width
- If violating this, it's a "Big Lizard" (different strategy, has upside risk)

### 2. Ignoring Assignment Risk

**The mistake:**

"I'll just hold to expiration for max profit."

**What you missed:**

Short put can be assigned EARLY (American options), especially if deep ITM near ex-dividend.

**Example:**

**Setup:**

- Jade Lizard on AAPL
- Stock drops from $175 → $155 (below $165 put strike)
- Ex-dividend date tomorrow ($0.25)

**Friday night:**

- Short $165 put is $10 ITM
- **Assigned:** Must buy 100 shares at $165
- Now own shares worth $155 → Immediate -$10 loss
- **Plus:** Stock could gap down Monday

**The fix:**

- **Close or roll short put** if deeply ITM (>$5)
- Avoid holding short puts through ex-dividend dates
- Monitor assignment risk in final week

### 3. Wrong Strike Selection (Too Aggressive)

**The mistake:**

"I'll sell ATM put for maximum premium."

**What you missed:**

ATM put has 50% probability of being ITM. Too risky.

**Example:**

**Aggressive trade:**

- Stock at $100
- Sell $100 put (ATM) for $5
- High probability of assignment!

**Conservative trade:**

- Stock at $100
- Sell $90 put (10% OTM) for $2
- Lower premium BUT lower probability

**The fix:**

- **Target 15-20 delta puts** (~15-20% OTM)
- Balances premium collection with safety
- Example: Stock at $100, sell $85-$87 put

### 4. Entering at Low IV

**The mistake:**

"Jade Lizards work in any volatility environment."

**What you missed:**

Low IV = low premium collected. Not worth the risk.

**Example:**

**Low IV entry (VIX = 12, stock IV 18%):**

- Net credit: $2.50
- Downside risk: Potentially -$15 if stock crashes
- **Risk/reward: Terrible** ($2.50 gain vs $15+ loss)

**High IV entry (VIX = 22, stock IV 35%):**

- Net credit: $6.50
- Same downside risk: -$15
- **Risk/reward: Better** ($6.50 gain vs $15 loss)

**The fix:**

- **Only enter Jade Lizards when IV >50th percentile**
- Higher premium justifies risk
- IV crush works in your favor (short vega)

### 5. No Exit Plan

**The mistake:**

"I'll hold for maximum profit."

**What you missed:**

Last 20% of profit has highest risk (gamma explodes, assignment risk).

**Example:**

**Week 4 (of 6):**

- Collected $6 credit initially
- Position now worth $1.50
- **Unrealized profit: $4.50 (75% of max)**

**Trader holds for last $1.50...**

**Week 5:** Stock whipsaws around strikes
- Gamma losses: -$2
- **Now only +$2.50 profit** (lost $2 by being greedy)

**The fix:**

- **Exit at 50-75% of max profit**
- Example: $6 credit, close at $1.50-$3 remaining value
- Avoid last week (gamma + assignment risk too high)

---

## Risk Management Rules

### 1. Strike Selection

**Short put guidelines:**

$$
\Delta_{\text{put}} = 0.15 \text{ to } 0.25 \quad \text{(15-25% probability ITM)}
$$

**Example:**

- Stock at $100
- Target: 20-delta put
- **Strikes: $85-$90 range**

**Call spread guidelines:**

$$
\Delta_{\text{short call}} = 0.15 \text{ to } 0.25
$$

$$
\text{Width} = 1\text{-}2 \times \text{ATR (Average True Range)}
$$

**Example:**

- Stock at $100, ATR = $3
- Short call: $110-$115 (20-25 delta)
- Width: $5 (about 1.5× ATR)

### 2. Position Sizing

**Rule of thumb:**

$$
\text{Position Size} = \frac{\text{Account} \times 0.05}{\text{Put Strike}}
$$

**Example:**

- $50,000 account
- 5% risk = $2,500
- Short put at $95
- **Max 1 contract** ($95 × 100 = $9,500 assignment value)

**Alternatively, size on margin required:**

- Margin for Jade Lizard: ~$3,000 per contract
- 5% of $50K account = $2,500
- **Max 1 contract**

### 3. Time Frame

**Entry:**

- **30-45 DTE:** Optimal theta decay zone
- Avoid <21 DTE (gamma too high)

**Exit:**

- **Target:** 50-75% of max profit
- **OR:** 7-10 DTE (whichever first)

**Example:**

- Enter 35 DTE for $6 credit
- Exit at $1.50-$3 remaining value (75-50% profit)
- OR exit at Day 25 (10 DTE remaining)

### 4. IV Entry Requirements

**Check IV percentile:**

$$
\text{IV Percentile} = \frac{\text{Current IV} - \text{52-week Low}}{\text{52-week High} - \text{52-week Low}}
$$

**Entry rules:**

- **<40th percentile:** AVOID (options too cheap)
- **40-60th:** Acceptable
- **>60th:** IDEAL (high premium, IV crush potential)

### 5. Adjustment Triggers

**When to adjust:**

1. **Stock threatens put strike:** Within $2 of short put
2. **Stock rockets past call spread:** Above long call strike
3. **IV spike:** Unexpected 30%+ IV increase
4. **Time decay stalling:** Theta not working after 2 weeks

**How to adjust:**

- **Stock drops:** Roll put down and out (lower strike, later expiration)
- **Stock rallies:** Usually no action needed (no upside risk by design)
- **IV spike:** Consider closing for scratch (reenter later)

---

## Real-World Examples

### 1. Pension Duration Cut via Futures

**Setup (March 2024):**

- SPY at $520
- IV at 58th percentile (16% IV)
- Bullish market trend

**Trade (35 DTE):**

- Sell $505 put for $5.20 (18-delta)
- Sell $535 call for $4.10 (20-delta)
- Buy $540 call for $2.50
- **Net credit: $6.80**
- **Call spread width: $5**
- **No upside risk:** $6.80 > $5 ✓

**Week 1:** SPY at $525
- Position value: $5.10
- **Profit so far: $1.70** (theta working)

**Week 2:** SPY at $530
- Position value: $3.80
- **Profit: $3.00** (44% of max)

**Week 3:** SPY at $532
- Position value: $2.50
- **Profit: $4.30** (63% of max)

**Exit (Day 22, 13 DTE remaining):**

- Closed for $2.00
- **Total profit: $4.80 (71% of max)**
- **ROI: 160%** on $3,000 margin

**Lesson:** Clean Jade Lizard execution. Stock stayed in safe zone, theta worked, exited before final week gamma risk. No upside risk protected against late rally.

### 2. Transition Risk Hedge

**Setup (November 2024, post-earnings):**

- NVDA at $140, just reported earnings
- IV at 75th percentile (75% IV post-earnings)
- Expecting IV crush + consolidation

**Trade (30 DTE):**

- Sell $130 put for $7.50
- Sell $150 call for $6.00
- Buy $155 call for $3.20
- **Net credit: $10.30**
- **Call spread width: $5**
- **No upside risk:** $10.30 > $5 ✓

**Next day (IV crush):**

- IV dropped: 75% → 50% (-25%)
- Stock at $143 (slight rally)
- **Position value:** $4.50
- **Unrealized profit: $5.80** (56% in 1 day!)

**Exit (3 days later):**

- Closed for $3.20
- **Total profit: $7.10 (69% of max)**
- **3-day return: 237%**

**Lesson:** High IV entry + IV crush = perfect Jade Lizard setup. Both short put and short call benefited from vega crush.

### 3. Portable Alpha with Futures

**Setup:**

- Stock at $100
- Jade Lizard: Sell $95 put, sell $110/$115 call spread
- Net credit: $6.50

**Week 3:** Stock drops to $92 (below put strike)

- Trader thinks: "It'll bounce back, I'll hold"
- Put now $3 ITM

**Week 4:** Stock at $90

- Put now $5 ITM
- Ex-dividend date approaching
- **Friday:** Assigned on short put (early assignment)
- **Forced to buy 100 shares at $95**

**Monday:** Stock gaps down to $87

- Own shares worth $87, paid $95
- **Loss: -$8 per share = -$800**
- But collected $6.50 credit
- **Net loss: -$150**

**Better outcome if closed Week 3:**

- Week 3 value at $92: $9 (put worth ~$3, call spread ~$0)
- Could have closed for -$2.50 loss
- **Saved: -$2.50 vs -$1.50 = $1.00** (plus avoided overnight gap risk)

**Lesson:** Don't "hope" for recovery when short put is ITM. Close or roll before assignment risk escalates.

### 4. Tactical Duration Extension

**Setup:**

- Stock at $100
- **Big Lizard (not standard Jade):**

  - Sell $90 put for $3
  - Sell $110 call for $3
  - Buy $125 call for $0.50
- **Net credit: $5.50**
- **Call spread width: $15**
- **Upside risk exists:** $5.50 < $15

**Outcome:**

- Stock rallies to $125 (strong bull market)
- Call spread max loss: -$15
- **Net P&L: $5.50 - $15 = -$9.50 loss**

**If used standard Jade Lizard:**

- Buy $115 call instead of $125 call (narrower spread)
- Credit would be $4
- Spread width: $5
- **Would have small profit:** $4 - $5 = -$1 (or close to breakeven)

**Lesson:** "Big Lizard" collects more premium but violates the no-upside-risk rule. If stock rallies hard, you lose. Stick to standard Jade Lizard (credit > width) for true upside protection.

---


---



## Final Wisdom

> "The Jade Lizard is the income trader's answer to covered calls - all the premium, a fraction of the capital, and none of the upside regret. By combining a short put with a short call spread, you're essentially saying 'I don't think the stock will crash, and even if it rallies to the moon, I won't lose.' The magic is in the math: credit > spread width = no upside risk. But discipline matters: sell the put far enough out, enter when IV is rich, and take profits before the last week. The Jade Lizard rewards patience and punishes greed."

**Key to success:**

- ALWAYS ensure: Net credit ≥ call spread width
- Enter when IV >50th percentile (rich premium)
- Sell 15-25 delta puts (not ATM)
- Exit at 50-75% max profit (don't be greedy)
- Monitor short put for assignment risk
- Close or roll if put gets deeply ITM

**Most important:** The "no upside risk" feature is what makes Jade Lizard special. Don't violate this by widening the call spread too much (becomes Big Lizard with upside risk). Stick to the formula! 🦎💚


---

## Practical Guidance

**Step-by-step jade lizard implementation:**

### 1. Critical Pre-Trade Checklist

☐ **Bullish conviction?** (Would you own stock at put strike?)  
☐ **IV 50-75th percentile?** (Elevated for premium collection)  
☐ **Uptrend confirmed?** (Above 50-day MA, higher highs/lows)  
☐ **Calculate credit > call width?** (CRITICAL: No upside risk verification)  
☐ **No earnings within expiration?** (Binary events forbidden)  
☐ **30-45 DTE?** (Optimal theta decay)  
☐ **Liquid strikes?** (OI > 500, spread < 10% per leg)  
☐ **Position size for -20% drop?** (Downside risk is UNLIMITED)

### 2. Step 1

**CRITICAL: Jade lizards are BULLISH strategies**

**Verify trend:**
- Stock above 50-day and 200-day MA
- Higher highs and higher lows for 3+ months
- **If broken:** Don't enter jade lizards

**Bullish catalysts:**
- Sector strength
- Earnings beat (post-earnings entry)
- Macro tailwinds

**If NOT bullish:** Use different strategy (not jade lizard)

### 3. Step 2

**The golden rule:**

$$
\text{Credit Collected} > \text{Call Spread Width}
$$

**This guarantees no upside risk!**

**Strike selection process:**

**1. Choose call spread first:**
- Short call: 20-25 delta (~2 SD OTM)
- Long call: 5-10 delta protection
- **Width:** Typically $5 for stocks, $5-10 for indices

**2. Choose put strike:**
- 15-20 delta (~1.5-2 SD OTM)
- Below technical support
- **Collect enough to exceed call width**

**3. Verify the rule:**
- Call width: $5
- Put premium: $5.50
- Call spread net: $2.00
- **Total credit:** $7.50
- **$7.50 > $5:** ✓ Pass

**If credit < call width:**
- Adjust put strike lower (collect more)
- OR narrow call spread
- OR skip trade (don't violate rule!)

### 4. Step 3

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times 1.5\%}{(\text{Put Strike} \times 0.20) \times 100}
$$

**Example:**
- Portfolio: $50,000
- Put strike: $170
- Assume -20% crash: $170 × 0.20 = $34 loss per share
- **Max contracts:** $50,000 × 0.015 / $3,400 = **0.22 → ZERO contracts!**

**More realistic for smaller accounts:**
For $50k account with $170 put:
- Risk: 1.5% = $750
- Reasonable loss (10% drop): $170 × 0.10 = $17 per share
- Less credit (say $7): $17 - $7 = $10 loss per share
- **Max contracts:** $750 / $1,000 = **0.75 → 1 contract only**

**Why so conservative?**
- Downside is UNLIMITED
- "No upside risk" creates overconfidence
- Need to survive 2-3 crashes
- **85% win rate masks 15% catastrophic loss**

### 5. Step 4

**Order entry:**
1. **3-leg combo order** (all simultaneously)
2. **Limit at mid-price** or better
3. **Verify credit > call width** BEFORE submitting
4. **Double-check put strike** (most common mistake)

**Entry timing:**
- **Best:** Post-earnings (IV elevated)
- **Good:** Post-volatility spike (IV elevated)
- **Avoid:** Low IV environment (<45th percentile)

### 6. Step 5

**Daily monitoring:**
- Stock price relative to put strike
- IV percentile (exit if drops <40th)
- Days to expiration (exit by 7 DTE)

**Exit triggers (ANY trigger → close):**

**Profit targets:**
- **Primary:** +60-70% of max profit
  - Example: Max $8, exit at $4.80-5.60
- **Time:** 75% time elapsed if +50% profit

**Stop losses (CRITICAL):**
- **Primary:** -50% of credit collected
  - Example: Collected $8, exit at -$4 loss
- **Put breach:** Stock within $5 of put strike
- **Technical:** Break of key support level

**Time stops:**
- **Always exit by 7 DTE** (gamma risk)
- Exit by 14 DTE if not +30% profitable

### 7. Step 6

**For jade lizards: Generally CLOSE rather than adjust**

**Why:**
- Downside risk is unlimited
- Adjusting (rolling) often makes it worse
- Better to take loss and re-enter fresh

**Only adjust if:**
- Stock threatening put, but still above support
- Roll put down + out (lower strike, more DTE)
- Collect additional credit
- **Must verify:** Still bullish!

**Example adjustment:**
- Stock at $172, put at $170 (threatened)
- Roll: Close $170 put, sell $165 put next month
- Collect $3 more credit
- **New position:** Lower risk, more time

**When NOT to adjust:**
- Stock breaking support (exit!)
- No longer bullish (exit!)
- Collected credit already spent (exit!)

### 8. Step 7

| Date | Underlying | Put | Call Spread | Credit | Width | Pass? | DTE | Exit | P&L | Win? |
|------|------------|-----|-------------|--------|-------|-------|-----|------|-----|------|
| 1/15 | NVDA | $120 | $140/$145 | $8.70 | $5 | ✓ | 35 | D28 | +$6.20 | ✓ |
| 2/10 | AAPL | $170 | $190/$195 | $7.50 | $5 | ✓ | 30 | D5 | -$7.50 | ✗ |

**Track:**
- **Pass rate:** How often credit > width (should be 100%!)
- **Win rate:** Target 75-80%
- **Avg winner:** +65% of max
- **Avg loser:** -50% of credit (stopped out)
- **Expectancy:** Should be positive

**Calculate expectancy:**
$$
E = (W\% \times \text{Avg Win}) - (L\% \times \text{Avg Loss})
$$

Example: 0.77 × $6.00 - 0.23 × $4.00 = $4.62 - $0.92 = **+$3.70 per trade**

### 9. The Jade Lizard Trading Rules

**Never trade when:**
1. Not bullish (would NOT own stock)
2. Credit < call width (violates golden rule)
3. Earnings or binary events within expiration
4. IV < 45th percentile (too cheap)
5. Downtrend or below 50-day MA
6. < 21 DTE (too short) or > 60 DTE (too long)
7. Can't size properly (unlimited downside!)

**Always:**
1. Verify credit > call width
2. Size for crash scenario (-20%)
3. Exit at +60-70% profit target
4. Exit at -50% credit loss
5. Exit by 7 DTE regardless
6. Close (don't adjust) when in trouble
7. Ask: "Would I own stock here?"

**The iron rule:** If you wouldn't be comfortable owning the stock at the put strike price, DON'T trade the jade lizard. The "no upside risk" is meaningless if downside destroys your account.