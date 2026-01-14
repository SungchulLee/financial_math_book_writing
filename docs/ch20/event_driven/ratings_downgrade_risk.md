# Ratings and Downgrade Risk


**Credit ratings** are standardized assessments of default probability issued by rating agencies (S&P, Moody's, Fitch), and **downgrade risk** is the potential for these ratings to be lowered, triggering forced selling, index exclusion, spread widening, and significant losses, creating both catastrophic risks for the unprepared and extraordinary opportunities for those who can anticipate rating changes before the agencies act.

---

## The Core Insight


**The fundamental idea:**

- Credit ratings categorize default risk (AAA/Aaa = safest, D = default)
- Investment grade (BBB-/Baa3 and above) vs. High yield (BB+/Ba1 and below)
- Rating changes trigger mechanical flows (forced selling/buying)
- Downgrades cause spreads to widen (prices fall), upgrades tighten (prices rise)
- **Fallen angels** (IG → HY) face catastrophic forced selling
- **Rising stars** (HY → IG) benefit from forced buying
- Market anticipates rating changes (spreads move before announcement)
- Skillful investors front-run agencies by analyzing fundamentals
- Widest opportunities at IG/HY boundary (BBB/BB ratings)

**The key equations:**

**Rating transition probability matrix:**

$$
P_{ij}(t) = \text{Probability of moving from rating } i \text{ to } j \text{ over time } t
$$

**Impact of downgrade on spread:**

$$
\Delta S = S_{\text{new rating}} - S_{\text{old rating}} + \text{Technical Premium}
$$

Where **Technical Premium** = forced selling impact.

**Fallen angel spread widening:**

$$
\Delta S_{\text{fallen angel}} \approx 200-400 \text{ bp (immediate)} + 100-200 \text{ bp (index rebalancing)}
$$

**Expected loss from downgrade:**

$$
\text{Loss} = -\Delta S \times \text{Duration} \times \text{Notional}
$$

**You're essentially asking: "Which companies are on the verge of being downgraded (or upgraded), how much will spreads move when the rating change occurs, and how do I position ahead of the announcement to capture the spread move while avoiding the forced selling tsunami that accompanies fallen angels?"**

---

## What Are Credit Ratings?


**Before trading around ratings, understand the framework:**

### 1. The Rating Scales


**Major rating agencies:**

1. **S&P Global Ratings**
2. **Moody's Investors Service**
3. **Fitch Ratings**

**Rating scale comparison:**

| Category | S&P | Moody's | Fitch | Default Probability (5-year) |
|----------|-----|---------|-------|------------------------------|
| **Investment Grade** | | | | |
| Highest quality | AAA | Aaa | AAA | 0.1% |
| High quality | AA+, AA, AA- | Aa1, Aa2, Aa3 | AA+, AA, AA- | 0.3% |
| Upper medium | A+, A, A- | A1, A2, A3 | A+, A, A- | 0.5% |
| Lower medium | BBB+, BBB, BBB- | Baa1, Baa2, Baa3 | BBB+, BBB, BBB- | 2.0% |
| **High Yield** | | | | |
| Non-IG speculative | BB+, BB, BB- | Ba1, Ba2, Ba3 | BB+, BB, BB- | 5.0% |
| Highly speculative | B+, B, B- | B1, B2, B3 | B+, B, B- | 12.0% |
| Substantial risk | CCC+, CCC, CCC- | Caa1, Caa2, Caa3 | CCC+, CCC, CCC- | 30.0% |
| Extremely speculative | CC, C | Ca | CC, C | 50%+ |
| Default | D | C | D | 100% |

**The critical boundary:**

$$
\boxed{\text{BBB-/Baa3 (Investment Grade)} \leftrightarrow \text{BB+/Ba1 (High Yield)}}
$$

**This is the most important rating transition!**

### 2. Rating Outlooks and Watches


**Rating agencies provide forward guidance:**

**1. Rating Outlook:**
- **Positive:** Possible upgrade within 6-24 months
- **Stable:** No change expected
- **Negative:** Possible downgrade within 6-24 months
- **Developing:** Uncertain direction

**Probability of change:**
- Positive outlook → Upgrade: 50%
- Negative outlook → Downgrade: 50%

**2. Credit Watch (Watchlist):**
- More imminent than outlook (0-90 days)
- **Watch Positive:** Upgrade likely
- **Watch Negative:** Downgrade likely
- **Watch Developing:** Direction unclear

**Probability of change:**
- Watch Negative → Downgrade: 75-85%
- Watch Positive → Upgrade: 75-85%

**Example progression:**

```
Stable → Negative Outlook → Watch Negative → Downgrade
  ↓           ↓                    ↓              ↓
(normal)  (6-12 months)        (0-90 days)    (occurs)
```

### 3. What Ratings Actually Measure


**Ratings assess:**

1. **Default probability** (primary)
2. **Loss severity** (secondary - recovery)

**Rating methodology factors:**

**Business risk (50% weight):**
- Industry outlook
- Competitive position
- Operating efficiency
- Management quality

**Financial risk (50% weight):**
- Leverage ratios (Debt/EBITDA)
- Interest coverage (EBITDA/Interest)
- Cash flow adequacy
- Financial flexibility

**Key ratios by rating:**

| Rating | Debt/EBITDA | EBITDA/Interest | Free Cash Flow/Debt |
|--------|-------------|-----------------|---------------------|
| AAA/Aaa | <1.0x | >10x | >30% |
| A/A2 | 1.5-2.0x | 7-10x | 20-30% |
| BBB/Baa2 | 2.5-3.5x | 4-6x | 10-20% |
| BB/Ba2 | 4.0-5.0x | 2.5-4x | 5-10% |
| B/B2 | 5.5-7.0x | 1.5-2.5x | 0-5% |
| CCC/Caa | >8.0x | <1.5x | Negative |

**Ratings are NOT:**
- Price targets
- Buy/sell recommendations
- Timing signals (often lag market)

**Ratings ARE:**
- Relative ranking of default risk
- Through-the-cycle assessment
- Triggers for investment mandates

---

## Economic Interpretation: Why Ratings Matter


**Understanding the structural importance:**

### 1. Investment Mandates and Forced Flows


**Many investors have rating-based mandates:**

**Investment grade only:**
- Pension funds (often restricted to IG)
- Insurance companies (regulatory capital)
- Money market funds (AAA/AA only)
- **~$9 trillion in IG-only mandates**

**When a bond is downgraded IG → HY:**
- **Must sell** (regardless of price or fundamentals)
- **Forced selling** within 30-90 days
- **Price impact severe** (supply >> demand)

**High yield funds:**
- Can buy fallen angels
- But often wait for price to stabilize
- **Don't catch the falling knife**

**The forced selling cascade:**

```
BBB bond announced → HY (BB+)
        ↓
Day 1-7: Market anticipates, spread widens 100-200 bp
        ↓
Day 8-30: Rating change effective, index exclusion
        ↓
Day 31-60: Forced IG selling, spreads widen another 200-300 bp
        ↓
Day 61-90: HY buyers emerge, spreads stabilize/tighten
        ↓
Day 90+: Spreads normalize to HY level (if fundamentals stable)
```

**Example:**

**Company XYZ downgraded BBB- → BB+**

| Date | Event | Spread | Price | Change |
|------|-------|--------|-------|--------|
| Day 0 | Rating BBB-, stable | 150 bp | $100 | - |
| Day -30 | Outlook → Negative | 180 bp | $98.5 | -1.5% |
| Day -7 | Watch Negative | 220 bp | $96.5 | -3.5% |
| Day 0 | Downgrade to BB+ | 350 bp | $90 | -10% |
| Day 30 | Index exclusion | 450 bp | $84 | -16% |
| Day 60 | Forced selling peak | 500 bp | $80 | -20% |
| Day 90 | HY buyers step in | 420 bp | $84 | -16% |

**Total loss from BBB- rating: -16% at stabilization**

**But market moved BEFORE downgrade:** -3.5% before announcement.

### 2. Index Rebalancing Mechanics


**Major bond indices:**

**Investment Grade:**
- Bloomberg Barclays US Corporate IG Index
- iShares iBoxx $ Investment Grade Corporate Bond ETF (LQD)
- ~$10 trillion tracking IG indices

**High Yield:**
- Bloomberg Barclays US Corporate High Yield Index
- iShares iBoxx $ High Yield Corporate Bond ETF (HYG)
- ~$1.5 trillion tracking HY indices

**Rebalancing process:**

**When company downgraded IG → HY:**

1. **Announcement date:** Rating agency announces
2. **Effective date:** Typically 5-10 business days later
3. **Index removal:** End of month following effective date
4. **Forced selling:** 30-60 days after index removal

**Example timeline:**

- June 15: S&P downgrades Ford BBB- → BB+
- June 20: Effective date
- June 30: Ford removed from IG index, added to HY index
- July 1-31: IG funds sell, HY funds buy
- **Net flow: IG holders 5x larger than HY → Net selling pressure**

**The asymmetry:**

$$
\text{IG Index AUM} \approx 7x \times \text{HY Index AUM}
$$

**When $10B bond falls from IG to HY:**
- IG funds sell: $10B
- HY funds buy: $1.4B (14% weight due to smaller index)
- **Net selling: $8.6B** → Price crashes

### 3. Rating Agency Lag


**Agencies are backward-looking:**

**Market vs. Agencies:**

| Metric | Market | Rating Agencies |
|--------|--------|-----------------|
| Speed | Real-time | Lag 6-18 months |
| Information | Forward-looking | Historical |
| Flexibility | High | Low (stable ratings) |
| Incentive | Profit | Accuracy |

**Example progression:**

| Date | Event | Market Reaction | Agency Action |
|------|-------|-----------------|---------------|
| Jan 2023 | Weak earnings | Spreads +50 bp | No action |
| Apr 2023 | Guide down | Spreads +100 bp | No action |
| Jul 2023 | Missed debt payment | Spreads +200 bp | Outlook → Negative |
| Oct 2023 | Restructuring | Spreads +300 bp | Watch Negative |
| Jan 2024 | More bad news | Spreads +400 bp | Downgrade! |

**Market moved 400 bp BEFORE agency downgraded!**

**This creates opportunity:**
- Anticipate downgrades by monitoring fundamentals
- Trade BEFORE agency acts
- Exit before forced selling

---

## Key Terminology


**Credit Rating:**

- Standardized assessment of default probability
- Issued by S&P, Moody's, Fitch (Nationally Recognized Statistical Rating Organizations - NRSROs)
- Scale: AAA/Aaa (best) to D/C (default)
- Investment grade vs. High yield threshold: BBB-/Baa3

**Investment Grade (IG):**

- Rated BBB-/Baa3 or higher
- "Low" default risk (historical: <2% over 5 years)
- Regulatory preferred (banks, insurance, pensions)
- Lower yields, higher prices

**High Yield (HY) / Junk Bonds:**

- Rated BB+/Ba1 or lower
- "High" default risk (historical: 5-30% over 5 years depending on rating)
- Higher yields, lower prices
- Smaller investor base

**Fallen Angel:**

- Bond downgraded from IG to HY
- Faces forced selling from IG-only investors
- Spreads widen 200-500 bp on average
- Often oversold (value opportunity after stabilization)

**Rising Star:**

- Bond upgraded from HY to IG
- Benefits from forced buying by IG investors
- Spreads tighten 100-300 bp on average
- Often overbought (short opportunity after stabilization)

**Rating Outlook:**

- Forward guidance: Positive, Stable, Negative, Developing
- Timeframe: 6-24 months
- Downgrade probability (Negative outlook): ~50%

**Credit Watch / Watchlist:**

- More imminent rating change expected
- Timeframe: 0-90 days
- Downgrade probability (Watch Negative): 75-85%

**Notching:**

- Different ratings for different securities of same issuer
- Senior secured > Senior unsecured > Subordinated
- Typically 1-2 notches difference

**Rating Migration:**

- Movement from one rating to another over time
- Measured by transition matrices
- Example: BBB bonds have 5% annual probability of downgrade to BB

**Split Rating:**

- Different agencies give different ratings
- Example: S&P BBB+, Moody's Baa3
- Creates uncertainty, often trades to lower rating

**Crossover Credits:**

- Companies at IG/HY boundary (BBB/BB)
- Highest downgrade risk
- Most volatile spreads

**Catalyst:**

- Event that triggers rating review
- Examples: M&A, dividend increase, debt issuance, weak earnings
- Agencies respond to catalysts

---

## Basic Downgrade Risk Strategies


### 1. Strategy 1: Short BBB Credits on Negative Watch


**Setup:**

**Screening criteria for downgrade candidates:**

1. **Rating: BBB/Baa (crossover)**
2. **Outlook: Negative or Watch Negative**
3. **Fundamentals deteriorating:**
   - Leverage rising (Debt/EBITDA > 3.5x)
   - Coverage declining (EBITDA/Interest < 3x)
   - Free cash flow negative

**Identified company:**

**ABC Corp:**
- Rating: BBB (S&P), Baa2 (Moody's)
- Outlook: Negative (S&P), Watch Negative (Moody's)
- 5-year bond: Spread 180 bp
- Debt/EBITDA: 3.8x (high for BBB)
- Interest coverage: 2.8x (low for BBB)
- **Downgrade to BB+ likely within 3 months**

**Trade:**

**Buy CDS protection (short credit):**
- Notional: $10M
- Spread: 180 bp
- Running: 100 bp
- Upfront: -3.6%

**Expected outcome:**

**Scenario 1: Downgraded to BB+ (base case)**

**Spread moves:**
- Current (BBB): 180 bp
- Post-downgrade (BB+): 350 bp (immediate)
- Post-forced selling: 450 bp (30-60 days)

**P/L (3 months):**

| Phase | Spread | Change | MTM | Cumulative |
|-------|--------|--------|-----|------------|
| Entry | 180 bp | - | -3.6% | -3.6% |
| Announcement | 350 bp | +170 bp | +7.1% | +3.5% |
| Forced selling | 450 bp | +100 bp | +4.2% | +7.7% |
| **Total** | | **+270 bp** | | **+7.7%** |

**Return on capital (~10% margin): 77% in 3 months**

**Scenario 2: Outlook revised to Stable (upside surprise)**

**Spread moves:**
- 180 bp → 140 bp (-40 bp)
- Loss: -40 bp × 4.5 DV01 = -1.8%
- Plus upfront: -3.6%
- **Total loss: -5.4%**

**Scenario 3: No change for 6 months (carry bleed)**

- Running cost: 100 bp × 0.5 years = -0.5%
- Upfront: -3.6%
- **Total cost: -4.1%**

**Risk/reward:**
- Downside: -5.4% (if upgraded)
- Upside: +7.7% (if downgraded)
- **Ratio: 1.4:1 (acceptable)**

### 2. Strategy 2: Long Fallen Angels Post-Stabilization


**Setup:**

**Recently downgraded company:**

**DEF Corp:**
- Downgraded BBB- → BB+ (2 months ago)
- Current spread: 480 bp (very wide)
- Pre-downgrade spread: 160 bp (BBB-)
- Fair value BB+ spread: 320 bp (based on peers)
- **Spread 160 bp too wide due to forced selling**

**Fundamentals:**
- Business stable (downgrade due to leverage, not operations)
- Debt/EBITDA: 4.2x (normal for BB+)
- Coverage: 3.0x (adequate)
- No further downgrade risk

**Trade:**

**Buy bonds at 480 bp spread:**
- Face value: $10M
- Price: $92
- YTM: 8.80%
- Duration: 5.5 years

**Expected spread normalization:**

**6-month forward:**
- Target spread: 350 bp (still wide of 320 bp fair, but normalized)
- Spread tightening: 480 - 350 = 130 bp
- Price gain: 130 bp × 5.3 duration = 6.9%
- Carry: 8.80% × 0.5 = 4.4%
- **Total return: 11.3%** (23% annualized)

**Catalysts for normalization:**
1. **Time:** Forced selling ends (30-60 days post-downgrade)
2. **HY buyers emerge:** Natural buyers at 450+ bp
3. **Technical stabilization:** Supply/demand balance

**Scenario analysis:**

**Scenario 1: Normalizes to 350 bp (base case)**
- Return: +11.3% (6 months)

**Scenario 2: Normalizes to 320 bp (fair value)**
- Tightening: 160 bp
- Return: 160 × 5.3 + 4.4% = 12.9%

**Scenario 3: Further deterioration → downgrade to B+**
- Spread: 480 → 700 bp (+220 bp)
- Loss: -220 × 5.5 = -12.1%
- Plus carry: +4.4%
- **Net: -7.7%**

**Risk management:**
- Set stop loss: Spread > 600 bp (exit)
- Monitor fundamentals weekly
- Exit if further downgrade likely

### 3. Strategy 3: Relative Value - BBB vs. BB Spread Compression


**Setup:**

**Post fallen angel environment:**

When multiple BBB issuers downgraded to BB, the BB market becomes crowded.

**Market conditions:**

| Rating | Avg Spread | Historical Avg | Z-score |
|--------|-----------|----------------|---------|
| BBB | 160 bp | 150 bp | +0.5 (normal) |
| BB | 420 bp | 340 bp | +2.0 (very wide) |
| **Differential** | **260 bp** | **190 bp** | **+2.5** |

**Analysis:**
- BB spreads 70 bp wider than normal differential
- Due to supply (many fallen angels)
- Should compress over time

**Trade:**

**Long BB bonds (buy supply, cheap):**
- $10M BB-rated bonds at 420 bp

**Short BBB bonds (expensive, relative):**
- Short $10M BBB-rated bonds at 160 bp
- Or sell CDS protection on BBB at 160 bp

**Expected convergence:**
- BB: 420 → 360 bp (-60 bp)
- BBB: 160 → 175 bp (+15 bp)
- Differential: 260 → 185 bp (normalized)

**P/L (12 months):**

| Position | Change | Duration | P/L |
|----------|--------|----------|-----|
| Long BB | -60 bp | 5.0 | +3.0% |
| Short BBB | +15 bp | 6.0 | -0.9% |
| **Net** | | | **+2.1%** |

**Plus carry differential:**
- Earn: BB yield 9.2%
- Pay: BBB yield 6.6%
- **Net carry: +2.6%**

**Total return: 2.1% + 2.6% = 4.7%**

**This is market-neutral to credit (long and short credit), betting only on spread differential.**

### 4. Strategy 4: Rising Star Arbitrage (Short Post-Upgrade)


**Setup:**

**Recently upgraded company:**

**GHI Corp:**
- Upgraded BB+ → BBB- (1 week ago)
- Current spread: 140 bp (very tight for BBB-)
- Pre-upgrade spread: 300 bp (BB+)
- Fair BBB- spread: 180 bp (based on peers)
- **Spread 40 bp too tight due to forced buying**

**Forced buying mechanics:**
- IG funds must buy (added to index)
- Buy within 30-60 days
- **Demand > Supply → Spread tightens excessively**

**Trade:**

**Sell CDS protection at 140 bp (too tight):**
- Notional: $10M
- Expect widening to 180 bp (fair value)

**Or short bonds:**
- Borrow and sell $10M bonds at tight spread

**Expected spread normalization:**

**3-month forward:**
- Forced buying ends
- Spread: 140 → 180 bp (+40 bp widening)
- Gain: 40 bp × 5.5 DV01 = +2.2%

**Scenario analysis:**

**Scenario 1: Normalizes to 180 bp**
- Gain: +2.2%
- Carry (sold protection): +0.35% (3 months)
- **Total: +2.55%** (10% annualized)

**Scenario 2: Further upgrade to BBB**
- Spread: 140 → 110 bp (-30 bp)
- Loss: -30 × 5.5 = -1.65%
- **Stop loss triggered**

**Scenario 3: Downgrade back to BB+ (rare)**
- Spread: 140 → 300 bp (+160 bp)
- Loss: -160 × 5.5 = -8.8%
- **Catastrophic but unlikely (<5% probability)**

**Risk management:**
- Exit if spread < 120 bp (too tight, more upside risk)
- Stop loss: Spread < 100 bp or upgrade announced

---

## Greeks in Rating Transition Strategies


**Understanding sensitivities:**

### 1. Duration Risk (Spread DV01)


**When bonds downgraded, duration changes:**

**Before downgrade (BBB):**
- Spread: 150 bp
- Duration: 6.5 years
- Spread risk: 150 × 6.5 = 975

**After downgrade (BB+):**
- Spread: 350 bp
- Duration: 5.8 years (lower due to higher yield)
- Spread risk: 350 × 5.8 = 2,030

**Spread risk more than DOUBLED!**

**Implication:**
- Spreads more volatile post-downgrade
- Need to reduce position size or hedge

**Position sizing adjustment:**

$$
\text{Post-downgrade size} = \text{Pre-downgrade size} \times \frac{D_{\text{old}}}{D_{\text{new}}}
$$

**Example:**
- Held $10M BBB (duration 6.5)
- After downgrade to BB (duration 5.8)
- **Reduce to:** $10M × (6.5/5.8) = **$11.2M to maintain same DV01**

But risk is higher, so actually reduce absolute size.

### 2. Convexity (Gamma)


**Rating transitions create discontinuous jumps:**

**Normal credit spread changes:**
- Gradual, smooth
- Positive convexity (bonds benefit from volatility)

**Rating changes:**
- Discrete jumps (150 bp → 350 bp overnight)
- **Negative gamma** (option sellers lose)

**Example:**

**Before downgrade announcement:**
- Expected spread widening: 200 bp
- Actual: 270 bp (worse than expected)
- **Loss 35% worse than modeled**

**Gamma exposure:**

$$
\text{Gamma Loss} = \frac{1}{2} \Gamma \times (\Delta S)^2
$$

**This explains why fallen angels overshoot:**
- Model says: 200 bp widening
- Reality: 300 bp widening (forced selling)
- **Extra 100 bp is gamma/forced flow**

### 3. Correlation Risk


**Multiple downgrades often cluster:**

**Sector downgrades:**
- Energy sector (2015-2016): 20+ fallen angels
- Retail sector (2017-2018): 10+ fallen angels
- Autos (2020): Ford, GM distress

**When one company downgraded, others follow:**

$$
\rho_{\text{downgrade}} \approx 0.6-0.8 \text{ (within sector)}
$$

**Portfolio impact:**

If short 10 BBB credits in same sector:
- Expected: 2-3 downgrades
- Reality in stress: 7-8 downgrades
- **Correlation underestimated = losses amplified**

**Risk management:**
- Diversify across sectors (max 20% any sector)
- Monitor peer group stress
- Exit all positions if 2+ downgrades in sector

---

## Rating Transition Payoff Analysis


### 1. Fallen Angel Expected Return Distribution


**Setup:**
- BBB- bond on Watch Negative
- Current spread: 200 bp
- Holding period: 6 months

**Probability distribution:**

| Outcome | Probability | Spread | Return | Notes |
|---------|-------------|--------|--------|-------|
| Upgrade to A | 5% | 120 bp | +3.5% | Surprise positive |
| Affirmed BBB- | 15% | 180 bp | +1.2% | Removed from watch |
| Stays BBB- | 20% | 200 bp | +0% | No change |
| Downgrade to BB+ | 50% | 380 bp | -10.8% | Forced selling |
| Downgrade to BB | 10% | 480 bp | -17.0% | Severe |

**Expected value:**

$$
E[R] = 0.05(3.5\%) + 0.15(1.2\%) + 0.20(0\%) + 0.50(-10.8\%) + 0.10(-17.0\%)
$$

$$
= 0.175\% + 0.18\% + 0\% - 5.4\% - 1.7\% = -6.765\%
$$

**Negative expected return!**

**Why? Because:**
- High probability of downgrade (60%)
- Downgrade losses large (-10 to -17%)
- Upgrade gains small (+1 to +3.5%)

**Asymmetric payoff: Large losses, small gains**

**This is why you SHORT these credits (buy protection), not own them!**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/ratings_downgrade_payoff_distribution.png?raw=true" alt="ratings_downgrade_payoff_distribution" width="700">
</p>
**Figure 1:** Expected return distribution for BBB- bond on negative watch showing negative skew with high probability of large losses from downgrade vs. small probability of moderate gains from affirmation.

### 2. Rising Star Expected Return Distribution


**Setup:**
- BB+ bond on Watch Positive
- Current spread: 320 bp
- Holding period: 6 months

**Probability distribution:**

| Outcome | Probability | Spread | Return | Notes |
|---------|-------------|--------|--------|-------|
| Upgrade to BBB- | 60% | 180 bp | +8.4% | Forced buying |
| Upgrade to BBB | 10% | 140 bp | +10.8% | Strong |
| Affirmed BB+ | 25% | 300 bp | +1.2% | Watch removed |
| Downgrade to BB | 5% | 400 bp | -4.8% | Surprise negative |

**Expected value:**

$$
E[R] = 0.60(8.4\%) + 0.10(10.8\%) + 0.25(1.2\%) + 0.05(-4.8\%)
$$

$$
= 5.04\% + 1.08\% + 0.30\% - 0.24\% = 6.18\%
$$

**Positive expected return! (12.4% annualized)**

**Why? Because:**
- High probability of upgrade (70%)
- Upgrade gains large (+8 to +11%)
- Downgrade losses small (low probability)

**Asymmetric payoff: Large gains, small losses**

**This is why you BUY rising stars!**

---

## Real-World Rating Change Examples


### 1. Example 1: Ford Downgrade to Junk (2020) - Loser for Holders


**Setup:**

- **Date:** March 2020 (COVID crisis)
- **Company:** Ford Motor Company
- **Rating:** BBB- (S&P), Baa3 (Moody's) - lowest IG

**Market environment:**
- Auto sales collapsed (COVID lockdowns)
- Production halted
- Cash burn accelerating
- **Downgrade to HY imminent**

**Pre-downgrade position:**

**Institutional investor (pension fund):**
- Held $50M Ford 10-year bonds
- Bought at: $98 (spread 180 bp)
- Rating: BBB-
- **Required to hold only IG bonds**

**March 2020: Warning signs**

**March 1:**
- S&P places Ford on Watch Negative
- Spread: 180 bp → 280 bp (+100 bp)
- Price: $98 → $93.5

**Investor reaction:** "We're required to hold IG, can't sell yet, hoping upgrade doesn't happen..."

**March 20:**
- Ford draws down $15B credit line (sign of distress)
- Moody's downgrades: Baa3 → Ba1 (HY!)
- Spread: 280 bp → 520 bp (+240 bp)
- Price: $93.5 → $83

**Forced selling begins:**

**March 24:**
- S&P downgrades: BBB- → BB+ (HY)
- **Both agencies now HY → Must sell!**
- Spread: 520 bp → 650 bp (+130 bp)
- Price: $83 → $78.5

**March 25-31: Panic selling**
- Pension fund must liquidate $50M Ford
- Market has no bids (everyone selling, no buyers)
- Finally sells at: **$72** (spread ~800 bp)

**Total loss:**

| Component | Change |
|-----------|--------|
| Purchase price | $98 |
| Sale price | $72 |
| **Loss** | **-$26 per $100 face** |

**On $50M position: -$13M (-26.5%)**

**Plus missed carry:** Would have earned ~$2.5M in coupon over holding period.

**Total damage: -$13M**

**What if sold earlier?**

**Sell on Watch Negative (March 1):**
- Sold at: $93.5
- Loss: $4.5 per $100 = -$2.25M
- **Saved $10.75M by acting early!**

**Why investor didn't sell:**
- "We're required to hold IG, can't sell until downgrade"
- **Wrong! Mandate is guideline, not law**
- Should have sold when deterioration clear

**The aftermath:**

**6 months later (September 2020):**
- Ford stabilized (government aid, cost cuts)
- Spread: 800 bp → 450 bp
- Price: $72 → $83
- **If held, would have recovered $11 per bond**

**But couldn't hold - forced to sell at bottom.**

**Lesson: Don't wait for rating agencies. Sell when fundamentals deteriorate!**

### 2. Example 2: Sprint Rising Star (2018) - Winner


**Setup:**

- **Date:** July 2018
- **Company:** Sprint Corporation
- **Rating:** BB+ (S&P), Ba1 (Moody's) - top of HY
- **Event:** T-Mobile merger announced, upgrade expected

**Hedge fund strategy:**

**Identified rising star candidate:**

**Screening criteria (met):**
- [ ] BB+ rating (1 notch below IG)
- [ ] Positive outlook or watch positive
- [ ] Fundamentals improving (merger synergies)
- [ ] Catalyst (merger approval)

**Sprint analysis:**
- Standalone: BB+ (marginal)
- Post-merger: BBB- likely (combined entity stronger)
- **Upgrade to IG expected within 6-12 months**

**Trade (July 2018):**

**Buy Sprint 8-year bonds:**
- Notional: $20M
- Spread: 380 bp (BB+ level)
- Price: $95
- YTM: 8.0%

**Expected IG spread:** 160 bp (BBB-)

**Evolution:**

**August-December 2018:**
- Merger regulatory review progressing
- Sprint standalone improving
- Spread: 380 bp → 320 bp (-60 bp)
- Price: $95 → $98.50

**Interim P/L (5 months):**
- Price gain: +3.7%
- Carry: +3.3%
- **Total: +7.0%**

**January-March 2019:**
- Merger approval uncertainty
- Spread volatile: 320-360 bp
- Held position (conviction on upgrade)

**April 2019: Upgrade Announced**

**S&P upgrades Sprint: BB+ → BBB- (!)** 

**Market reaction:**

- Spread: 340 bp → 180 bp (-160 bp immediate!)
- Price: $97 → $106
- **One-day gain: +9.3%**

**Forced buying begins:**

**April-May 2019:**
- IG index adds Sprint
- IG-only funds must buy
- Spread continues tightening: 180 bp → 140 bp
- Price: $106 → $108.50

**Total P/L (10 months):**

| Component | Return |
|-----------|--------|
| Spread tightening | 380 → 140 bp = 240 bp × 5.5 = 13.2% |
| Carry | 8.0% × 10/12 = 6.7% |
| **Total** | **19.9%** |

**Annualized: 23.9%**

**Decision: Sell at $108.50**
- Locked in gains
- Spread now too tight (140 bp)
- Forced buying complete

**Why it worked:**

1. **Correct catalyst identification:** Merger = upgrade path
2. **Early entry:** Bought before upgrade (at 380 bp)
3. **Patience:** Held through volatility
4. **Captured forced buying:** Sold into IG demand
5. **Disciplined exit:** Didn't get greedy

**Compare to entering after upgrade:**

**If bought post-upgrade at 180 bp:**
- Tightening: 180 → 140 bp = 40 bp
- Return: 40 × 5.4 = 2.2%
- **Much smaller gain!**

**Early entry captured 240 bp vs. 40 bp.**

### 3. Example 3: Kraft Heinz False Alarm (2019) - Winner by Avoiding


**Setup:**

- **Date:** February 2019
- **Company:** Kraft Heinz
- **Rating:** BBB (S&P), Baa2 (Moody's) - solid IG

**Event:**

**February 21, 2019: Earnings disaster**
- $15B goodwill writedown
- Dividend cut 36%
- SEC investigation disclosed
- Stock: -27% in one day

**Market panic:**
- "This is the next fallen angel!"
- BBB bonds: Spread 120 bp → 240 bp (+120 bp)
- Price: $100 → $94

**Many investors:** "Obvious downgrade coming, sell now!"

**Contrarian fund analysis:**

**Rating agency perspective:**

**S&P/Moody's criteria:**
- Current leverage: 3.2x (within BBB range)
- Coverage: 4.5x (adequate)
- Dividend cut = deleveraging (positive)
- Writedown = non-cash (doesn't affect cash flow)

**Agency statement (Feb 22):**
- "Rating affirmed at BBB, outlook stable"
- "Writedown doesn't change credit fundamentals"
- **No downgrade!**

**Trade (contrarian):**

**Buy Kraft bonds at panic spread:**
- Spread: 240 bp (very wide for BBB)
- Price: $94
- Fair value spread: 140 bp (BBB average)

**Thesis:** False alarm, spreads will normalize.

**Evolution:**

**March 2019:**
- Market realizes no downgrade coming
- Spread: 240 bp → 180 bp (-60 bp)
- Price: $94 → $97.50

**April-May 2019:**
- Fundamentals stable
- Spread: 180 bp → 150 bp (-30 bp)
- Price: $97.50 → $99

**6-month P/L:**

| Component | Return |
|-----------|--------|
| Spread tightening | 240 → 150 bp = 90 bp × 5.5 = 4.95% |
| Carry | 6.2% × 0.5 = 3.1% |
| **Total** | **8.05%** (16.1% annualized) |

**Why it worked:**

1. **Understood rating criteria:** Agencies look at cash flow, not writedowns
2. **Identified panic:** Market overreacted
3. **Read agency statements:** "Affirmed" = no downgrade
4. **Quick entry:** Bought during panic (first week)

**Contrast to those who sold:**

**Panicked sellers:**
- Sold at: $94 (240 bp)
- Bought originally: $100 (120 bp)
- **Loss: -6%**

**Should have:**
- Analyzed rating agency criteria
- Realized writedown non-cash
- **Held or bought more**

**Lesson: Not all bad news = downgrade. Understand what agencies care about!**

### 4. Example 4: Energy Sector Massacre (2015-2016) - Loser


**Setup:**

- **Date:** June 2015 - December 2016
- **Sector:** Energy (E&P and oil services)
- **Catalyst:** Oil price collapse ($100 → $28/barrel)

**Rating environment:**

**June 2015 - Energy sector BBB credits:**
- 15 major E&P companies rated BBB
- 8 oil services companies rated BBB
- **Total $180B BBB energy bonds outstanding**

**Fund strategy (misguided):**

**IG bond fund (passive, index tracking):**
- Held $2B energy sector bonds (10% of fund)
- All BBB-rated
- **Mandate: Must track IG index**

**The cascade:**

**Q3 2015 (Sep):**
- Oil: $60 → $45
- S&P downgrades 5 energy companies: BBB → BB
- **$40B fallen angels**

**Impact on fund:**
- Held 3 of the 5 downgraded ($600M)
- Must sell within 60 days
- Market flooded with sellers
- Spreads: 180 bp → 420 bp

**Forced sale losses:**
- Bought at: $100 (180 bp)
- Sold at: $85 (420 bp)
- **Loss: -15% on $600M = -$90M**

**Q4 2015 (Dec):**
- Oil: $45 → $37
- S&P downgrades another 4: BBB → BB
- Moody's downgrades 6: Baa → Ba
- **Another $60B fallen angels**

**Impact on fund:**
- Held 5 of the newly downgraded ($800M)
- Must sell
- Spreads: 200 bp → 550 bp (worse than Q3!)
- **Loss: -20% on $800M = -$160M**

**Q1 2016 (Mar):**
- Oil: $37 → $28 (crash!)
- Another wave: 6 more BBBs → BB
- **Total: 21 fallen angels in 9 months**

**Impact on fund:**
- Held 4 ($700M)
- Spreads: 220 bp → 650 bp
- **Loss: -24% on $700M = -$168M**

**Cumulative damage:**

| Quarter | Downgrades | Position | Loss |
|---------|-----------|----------|------|
| Q3 2015 | 5 | $600M | -$90M |
| Q4 2015 | 10 | $800M | -$160M |
| Q1 2016 | 6 | $700M | -$168M |
| **Total** | **21** | **$2.1B** | **-$418M** |

**On $20B fund: -2.1% just from energy downgrades**

**Plus:** Energy bonds not downgraded still fell 10-15%.

**Total fund energy impact: -$800M (-4% of fund)**

**What should have been done:**

**Early warning (June 2015):**
- Oil falling from $100 → $60
- E&P companies levered at $80-90 oil
- **Clear downgrade risk**

**Correct action:**
- Sell ALL energy BBBs (June 2015)
- Exit at: -5% loss
- **Save $350M+**

**But passive fund couldn't:**
- "We must track index"
- "Can't sell until downgrade"
- **Dogma = disaster**

**The aftermath:**

**2017-2018: Oil recovery**
- Oil: $28 → $70
- Many fallen angels upgraded back: BB → BBB
- Spreads: 650 bp → 280 bp
- **If held, would have recovered**

**But forced selling at bottom locked in losses.**

**Lesson: Sector concentration risk in passive IG funds is catastrophic during downgrade waves.**

---

## Best Case Scenario


### 1. The Perfect Downgrade Anticipation - AT&T Divestiture (2022)


**Setup:**

- **Date:** March 2022
- **Sophisticated Credit Hedge Fund**
- **Capital:** $500M
- **Strategy:** Anticipate rating changes using fundamental analysis

**Market opportunity:**

**AT&T situation:**
- Rating: BBB+ (S&P), Baa1 (Moody's) - mid IG
- Announced WarnerMedia spin-off (May 2021)
- Post-spin: AT&T will have less cash flow, same debt
- **Leverage will increase significantly**

**Fund analysis (March 2022):**

**Current metrics:**
- Debt: $180B
- EBITDA (with WarnerMedia): $60B
- **Leverage: 3.0x** (acceptable for BBB+)

**Post-spin metrics (estimated):**
- Debt: $180B (unchanged)
- EBITDA (without WarnerMedia): $42B
- **Leverage: 4.3x** (too high for BBB+)

**Rating agency thresholds:**
- BBB+: Leverage <3.5x
- BBB: Leverage 3.5-4.0x
- BBB-: Leverage 4.0-4.5x

**Conclusion: AT&T will be downgraded BBB+ → BBB- (2 notches)**

**But market not pricing this yet!**

**Market pricing (March 2022):**
- AT&T 10-year bonds: Spread 130 bp (BBB+ level)
- BBB- bonds trade at: 180 bp
- **50 bp mispricing!**

**The perfect trade:**

**Buy CDS protection (short AT&T credit):**

1. Buy $200M CDS protection
2. Spread: 130 bp
3. Running: 100 bp
4. Target: 180 bp (post-downgrade)

**Also:**
5. Short $100M AT&T bonds (borrow and sell)

**Total position: $300M notional**
**Capital: $30M (10% margin)**

**Timeline - The Perfect Execution:**

**April 2022: Spin-off closes**
- WarnerMedia separated
- AT&T leverage: 3.0x → 4.2x (confirmed)
- Market begins pricing downgrade
- Spread: 130 bp → 155 bp (+25 bp)

**P/L (1 month):**
- CDS: +25 bp × $800k DV01 = +$20M
- Short bonds: +25 bp × $400k DV01 = +$10M
- **Total: +$30M (+100% on $30M capital!)**

**May 2022: Agencies announce review**

**May 15:**
- S&P places AT&T on Watch Negative
- Moody's places on review for downgrade
- **Market front-runs downgrade**
- Spread: 155 bp → 175 bp (+20 bp)

**Cumulative P/L:**
- CDS: +45 bp = +$36M
- Short bonds: +45 bp = +$18M
- Costs (2 months): -$2M
- **Net: +$52M (+173%)**

**June 2022: Double downgrade announced**

**June 30:**
- S&P: BBB+ → BBB- (2 notches!)
- Moody's: Baa1 → Baa3 (2 notches!)
- **Bigger than expected!**

**Market reaction:**
- Spread: 175 bp → 210 bp (+35 bp)
- Forced selling begins (some BBB+ only mandates)

**Cumulative P/L:**
- CDS: +80 bp = +$64M
- Short bonds: +80 bp = +$32M
- Costs (3 months): -$3M
- **Net: +$93M (+310%!)**

**July-August 2022: Forced selling**

**Peak spread:**
- 210 bp → 230 bp (+20 bp more)
- Technical selling (index rebalancing)

**Decision: Close 75% of position**
- Locked in profits: $85M (on 75% position)
- Kept 25% for final stabilization

**September 2022: Stabilization**

- Spread: 230 bp → 195 bp (-35 bp)
- Forced selling ends
- Closed remaining 25%

**Final P/L:**

| Phase | CDS Gain | Bond Short Gain | Total |
|-------|----------|-----------------|-------|
| Anticipation (Apr-May) | +$36M | +$18M | +$54M |
| Announcement (Jun) | +$28M | +$14M | +$42M |
| Forced selling (Jul-Aug) | +$16M | +$8M | +$24M |
| **Total (gross)** | **+$80M** | **+$40M** | **+$120M** |
| Costs | -$6M | -$4M | -$10M |
| **Net** | **+$74M** | **+$36M** | **+$110M** |

**Return on $30M capital: 367% in 6 months**

**Attribution:**

| Source | Amount | % |
|--------|--------|---|
| Fundamental mispricing | $54M | 49% |
| Agency announcement | $42M | 38% |
| Technical selling | $24M | 22% |
| Costs | -$10M | -9% |
| **Total** | **$110M** | **100%** |

**Why this was best case:**

1. **Perfect fundamental analysis:**
   - Identified leverage increase from spin-off
   - Calculated exact post-spin metrics (4.2x)
   - Predicted 2-notch downgrade (correct!)

2. **Early entry:**
   - Positioned 3 months before announcement
   - Entered at 130 bp (full mispricing)
   - **vs. entering after announcement at 175 bp**

3. **Catalysts clear:**
   - Spin-off date known (April)
   - Agency reviews predictable (May-June)
   - Timeline tight (6 months total)

4. **Multiple profit sources:**
   - Phase 1: Market anticipation (+54M)
   - Phase 2: Announcement (+42M)
   - Phase 3: Forced selling (+24M)

5. **Disciplined exit:**
   - Closed 75% at peak (locked in $85M)
   - Avoided full reversal
   - Kept 25% for final move

6. **Optimal structure:**
   - CDS (2/3 position): No borrow costs
   - Short bonds (1/3): Extra convexity
   - Combined: Maximum alpha

**Comparison to alternatives:**

| Strategy | Return | Notes |
|----------|--------|-------|
| **Actual (CDS + short bonds)** | **+367%** | **Perfect execution** |
| Just CDS | +247% | Good but less than actual |
| Just short bonds | +120% | Borrow costs hurt |
| Wait for announcement | +80% | Missed 49% of gain |
| Buy after downgrade | +10% | Only stabilization |

**This exemplifies the power of:**
1. Fundamental credit analysis
2. Anticipating rating agencies
3. Early positioning
4. Multiple profit phases
5. Disciplined execution

---

## Worst Case Scenario


### 1. The Downgrade Wave Trap - Retail Apocalypse (2017-2018)


**Setup:**

- **Date:** January 2017
- **Investor:** Multi-strategy credit fund
- **Capital:** $1B
- **Strategy:** Overweight retail sector BBB credits

**Market environment:**

**Retail sector (early 2017):**
- Brick-and-mortar retail under pressure (Amazon)
- But still generating cash flow
- Many BBB-rated issuers
- **Spreads tight: 140-180 bp**

**Fund's thesis (wrong):**

"Retail headwinds are overblown. These are strong brands with loyal customers. Amazon threat is priced in. BBB ratings are safe. Spreads will tighten as fears prove unfounded."

**Position:**

**$300M retail BBB bonds (30% of fund):**
- Macy's: $60M (BBB)
- Nordstrom: $50M (BBB)
- Gap: $40M (BBB+)
- L Brands: $40M (BBB-)
- Kohl's: $30M (BBB+)
- J.C. Penney: $30M (BBB-)
- Bon-Ton: $20M (BBB-)
- Sears: $30M (BBB-)

**Average spread: 165 bp**

**The cascade - Month by month disaster:**

**February 2017: First cracks**

**Macy's:**
- Announces store closures
- Weak Q4 earnings
- S&P: Outlook → Negative
- Spread: 150 bp → 200 bp

**Fund reaction:** "Temporary weakness, hold."

**March-April 2017: Deterioration spreads**

**Multiple retailers:**
- Weak earnings across sector
- Same-store sales negative
- Amazon eating market share

**Spreads:**
- Macy's: 200 bp → 280 bp
- Nordstrom: 160 bp → 220 bp
- Gap: 140 bp → 190 bp

**Portfolio: -$18M (-6%)**

**Fund reaction:** "Oversold, buying opportunity!"

**Fatal mistake #1: Averaged down**
- Added $100M more retail bonds
- **Total position now: $400M (40% of fund!)**

**May-August 2017: The downgrade wave begins**

**June 1: S&P downgrades Macy's: BBB → BB+**

- Spread: 280 bp → 550 bp (+270 bp)
- Price: $95 → $83
- **Loss on $60M: -$7.2M**

**Forced to sell (index exclusion):**
- Sold at: $83 (realized loss)

**June 15: Fitch downgrades Nordstrom: BBB → BB+**

- Spread: 220 bp → 480 bp
- **Loss: -$6.5M on $50M**
- Sold at forced sale

**July: J.C. Penney and Bon-Ton Watch Negative**

- Spreads gap wider in anticipation
- J.C. Penney: 240 bp → 420 bp
- Bon-Ton: 280 bp → 550 bp

**August 1: Both downgraded BBB- → BB**

- J.C. Penney sold at: -18% loss = -$5.4M
- Bon-Ton sold at: -22% loss = -$4.4M

**Cumulative losses (8 months): -$41.5M**

**Fund manager:** "Worst is over, these downgrades are priced in now."

**September-December 2017: Second wave**

**Sears accelerating decline:**
- Same-store sales -13%
- Burning $1B+ cash annually
- Bankruptcy rumors

**October: Moody's downgrades Sears: Baa3 → B1 (3 notches!)**

- Spread: 350 bp → 1,200 bp (distressed)
- Price: $88 → $45
- **Loss on $30M: -$12.9M** (43% loss!)

**November: Gap downgraded BBB+ → BBB-**

- Not to HY yet, but 1 notch from fallen angel
- Spread: 190 bp → 320 bp
- **Mark-to-market loss: -$5.2M**

**December: L Brands to Watch Negative**

- Spread: 210 bp → 300 bp
- **MTM loss: -$3.6M**

**Year-end 2017 damage:**

| Position | Entry | Exit/Mark | Loss | Status |
|----------|-------|-----------|------|--------|
| Macy's | $60M | Sold | -$7.2M | Downgraded |
| Nordstrom | $50M | Sold | -$6.5M | Downgraded |
| J.C. Penney | $30M | Sold | -$5.4M | Downgraded |
| Bon-Ton | $20M | Sold | -$4.4M | Downgraded |
| Sears | $30M | Sold | -$12.9M | Downgraded |
| Gap | $40M | Held | -$5.2M | Still BBB- |
| L Brands | $40M | Held | -$3.6M | Still BBB- |
| Kohl's | $30M | Held | -$2.8M | Still BBB+ |
| **Total** | **$400M** | | **-$48M** | **-12%** |

**2018: The final destruction**

**February 2018: Gap downgraded BBB- → BB+**

- Forced sale at: -18%
- **Loss: -$7.2M** (total on Gap)

**March: L Brands downgraded BBB- → BB**

- Forced sale at: -20%
- **Loss: -$8.0M** (total on L Brands)

**April: Kohl's outlook → Negative**

- Spread: 170 bp → 240 bp
- **MTM: -$2.1M**

**October 2018: Sears bankruptcy**

- Bond recovery: 15 cents
- Additional loss from mark: -$3.0M
- **Total Sears loss: -$15.9M** (53% wipeout)

**Final tally (22 months):**

| Component | Loss |
|-----------|------|
| Realized losses (sales) | -$46.5M |
| MTM losses (remaining) | -$8.9M |
| Sears bankruptcy | -$15.9M |
| Carry collected | +$12.0M |
| **Net** | **-$59.3M** |

**On $300M original (later $400M): -19.8% loss**
**Fund overall: -5.9% (devastating)**

**What went catastrophically wrong:**

1. **Sector concentration:**
   - 30% in one sector (retail)
   - When sector collapsed, all fell together
   - **Correlation → 1.0 in stress**

2. **Ignored secular trend:**
   - "Amazon is priced in" (WRONG!)
   - Brick-and-mortar dying, not just weak
   - **Structural decline, not cyclical**

3. **Averaged down (fatal):**
   - $300M → $400M (added to losers)
   - Turned bad into catastrophic
   - **Never average down on secular decline**

4. **Downgrade wave dynamics:**
   - One downgrade triggered others
   - Rating agencies herd
   - **Cascade effect**

5. **Forced selling amplified:**
   - 5 fallen angels in 12 months
   - Each forced sale crashed price
   - **Technical > fundamental**

6. **No stop loss:**
   - Held through -6%, -10%, -15%
   - "Long-term investors"
   - **Should have exited at -10%**

7. **Ignored credit metrics:**
   - Leverage rising (sales falling, debt constant)
   - Coverage declining (EBITDA down)
   - Free cash flow negative
   - **All downgrade signals, ignored**

8. **Confirmation bias:**
   - "Retail will recover"
   - "Amazon fears overdone"
   - **Refused to update thesis**

**What should have been done:**

**January 2017: Early warning signs**

- Amazon sales growth 25%
- Retail same-store sales negative
- **Clear sector headwinds**

**Correct action:**
- Exit ALL retail BBB exposure
- Loss: -2% to -3%
- **Save $56M+**

**Or at minimum:**

**June 2017: After first downgrade (Macy's)**

- "When one falls, others follow"
- Exit all retail
- Loss at that point: -$18M
- **Save $41M+**

**The aftermath:**

**2019-2020:**
- Some survivors (Kohl's, Nordstrom) stabilized
- Never recovered to pre-2017 levels
- Many bankruptcies (Sears, Bon-Ton, J.C. Penney eventually)

**If held everything:**
- Some recovered 30-40%
- Others went to zero (Sears, Bon-Ton)
- **Net: Still -40% to -50% from peak**

**Lesson: Sector downgrade waves are catastrophic. When secular decline starts, EXIT ALL EXPOSURE immediately. Don't average down. Don't hope for recovery. The retail apocalypse proved: fallen angels in declining sectors don't recover—they die.**

---

## What to Remember


### 1. Core Concept


**Credit ratings assess default probability, and rating changes trigger mechanical flows:**

$$
\text{IG} \leftrightarrow \text{HY boundary (BBB-/BB+)} = \text{Maximum forced flow impact}
$$

- Downgrades cause forced selling → Spreads widen → Prices fall
- Upgrades cause forced buying → Spreads tighten → Prices rise
- **Market anticipates rating changes** (spreads move before announcement)
- Skillful investors front-run agencies by 3-12 months

### 2. Rating Scales


**Investment Grade (IG):**
- AAA/Aaa → AA → A → BBB/Baa
- Can be held by pension funds, insurance
- ~$15 trillion market

**High Yield (HY):**
- BB/Ba → B → CCC/Caa → D/C
- Limited investor base
- ~$2 trillion market

**Critical boundary: BBB-/Baa3 ↔ BB+/Ba1**

### 3. Forced Flow Dynamics


**Fallen angel (IG → HY):**

$$
\text{Spread widening} = 200-300 \text{ bp (immediate)} + 100-200 \text{ bp (forced selling)}
$$

**Typical price impact: -15% to -25%**

**Rising star (HY → IG):**

$$
\text{Spread tightening} = 100-200 \text{ bp (immediate)} + 50-100 \text{ bp (forced buying)}
$$

**Typical price gain: +8% to +15%**

### 4. Entry Checklist - Short Downgrade Candidates


**For buying CDS protection (betting on downgrade):**

1. **Rating characteristics:**
   - [ ] BBB/Baa rating (crossover zone)
   - [ ] Negative outlook or Watch Negative
   - [ ] Split rating (one agency already lower)

2. **Fundamentals:**
   - [ ] Leverage >3.5x (high for BBB)
   - [ ] Coverage <3.5x (low for BBB)
   - [ ] Free cash flow negative or declining
   - [ ] Sector under stress

3. **Catalyst:**
   - [ ] Identified event (M&A, div increase, weak earnings)
   - [ ] Timeframe <6 months
   - [ ] Agency review announced or likely

4. **Position:**
   - [ ] CDS liquid (bid-ask <10 bp)
   - [ ] Size <5% of fund
   - [ ] Stop loss defined (spread tightens 50 bp)

### 5. Entry Checklist - Long Fallen Angels


**For buying bonds post-downgrade:**

1. **Timing:**
   - [ ] 30-90 days post-downgrade (forced selling period)
   - [ ] Spread at 75th+ percentile vs. new rating
   - [ ] Spread >100 bp wider than pre-downgrade

2. **Fundamentals:**
   - [ ] Business stable (downgrade due to leverage, not operations)
   - [ ] No further downgrade risk
   - [ ] Management deleveraging plan

3. **Technical:**
   - [ ] Forced selling volume visible (high turnover)
   - [ ] HY buyers starting to emerge
   - [ ] Spread volatility declining

4. **Valuation:**
   - [ ] Spread vs. peers: >50 bp wide
   - [ ] Expected normalization: +15%+ return potential
   - [ ] Breakeven: <6 months to fair value

### 6. Common Strategies Summary


| Strategy | Entry | Target | Expected Return | Risk |
|----------|-------|--------|-----------------|------|
| Short downgrade candidates | BBB Watch Neg | Downgrade to BB+ | 15-30% | -10% if affirmed |
| Long fallen angels | Post-downgrade | Normalization | 10-20% | -15% if further downgrade |
| BBB vs. BB spread trade | Differential wide | Mean reversion | 5-10% | -5% if widens |
| Short rising stars | Post-upgrade | Normalization | 5-10% | -5% if further upgrade |

### 7. Exit Rules


**Short positions (CDS protection):**

1. **Profit targets:**
   - Downgrade announced: Close 50-75%
   - Forced selling peak: Close remainder

2. **Stop losses:**
   - Outlook revised to Stable: Exit
   - Spread tightens 50 bp: Exit
   - Loss > -10%: Exit

**Long positions (bonds):**

1. **Profit targets:**
   - Spread normalizes to fair value: Close
   - Return > +15%: Take profits

2. **Stop losses:**
   - Further downgrade announced: Exit
   - Spread >100 bp wider: Exit
   - Loss > -10%: Exit

### 8. Position Sizing


$$
\text{Position Size} = \min\left(5\% \text{ of fund}, \frac{2\%}{\text{Expected Vol}}\right)
$$

**Examples:**
- BBB Watch Negative (high vol): 2-3% max
- Fallen angel (post-stabilization): 5% max
- Sector exposure: <15% any sector

### 9. Rating Transition Probabilities


**Historical 1-year transition matrix (S&P):**

| From | To AAA | AA | A | BBB | BB | B | CCC | D |
|------|--------|----|----|-----|----|----|-----|---|
| AAA | 90% | 8% | 0.5% | 0.1% | 0% | 0% | 0% | 0% |
| AA | 1% | 91% | 7% | 0.5% | 0.1% | 0% | 0% | 0% |
| A | 0.1% | 2% | 91% | 5% | 0.5% | 0.1% | 0% | 0.1% |
| BBB | 0% | 0.5% | 5% | 87% | 5% | 1% | 0.3% | 0.2% |
| BB | 0% | 0% | 0.5% | 7% | 80% | 8% | 2% | 1% |
| B | 0% | 0% | 0% | 0.5% | 6% | 83% | 5% | 4% |

**Key observations:**
- BBB → BB: 5% annually
- BB → BBB: 7% annually
- Default rates: BBB 0.2%, BB 1%, B 4%

### 10. Common Mistakes


1. **Waiting for rating agency**
   - Market moves 3-12 months before
   - By announcement, 50-70% of move done

2. **Averaging down in downgrade wave**
   - Sector stress clusters
   - First downgrade often signals more

3. **Ignoring fundamental deterioration**
   - "Rating is still BBB, I'm safe"
   - Agencies lag by 6-18 months

4. **No catalyst**
   - Just "weak fundamentals" insufficient
   - Need specific event/timeline

5. **Buying too early post-downgrade**
   - Forced selling takes 30-90 days
   - Wait for stabilization

6. **Sector concentration**
   - One downgrade triggers others
   - Max 15% any sector

7. **No exit discipline**
   - Holding fallen angels to zero
   - "It's a good company" ≠ good bond

8. **Underestimating technical impact**
   - Forced flows > fundamentals
   - $10B IG selling vs. $1.5B HY buying

### 11. Performance Expectations


**Short downgrade candidates:**

| Outcome | Probability | Return | Notes |
|---------|-------------|--------|-------|
| Downgrade 2 notches | 20% | +25% | Fallen angel |
| Downgrade 1 notch | 30% | +12% | Within IG |
| Affirmed | 40% | -5% | Outlook removed |
| Upgrade | 10% | -12% | Wrong direction |

**Expected return: 4-8% (trade, not annualized)**

**Long fallen angels:**

| Outcome | Probability | Return |
|---------|-------------|--------|
| Normalizes | 60% | +15% |
| Partial recovery | 25% | +5% |
| Further downgrade | 10% | -15% |
| Default | 5% | -60% |

**Expected return: 8-12% over 6-12 months**

### 12. Your Learning Path


**Phase 1 (Months 1-3): Fundamentals**
- Study rating methodologies
- Build downgrade screening model
- Track agency actions (outlooks, watches)
- Paper trade

**Phase 2 (Months 4-6): Analysis**
- Identify crossover credits (BBB/BB)
- Calculate leverage/coverage ratios
- Predict rating changes
- Small real-money positions

**Phase 3 (Months 7-12): Active trading**
- Short downgrade candidates
- Buy fallen angels post-stabilization
- Portfolio of 5-10 positions
- Track performance attribution

**Phase 4 (Year 2+): Systematic**
- Automated screening
- Systematic entry/exit rules
- Risk management framework
- Scale capital

### 13. Final Wisdom


> "Rating agencies are historians, not forecasters. They tell you what already happened to credit quality, not what will happen. The skilled credit investor is the agency's worst nightmare—someone who analyzes fundamentals in real-time, anticipates rating changes 6-12 months early, and profits from the mechanical forced flows that occur when the agency finally catches up. But the downgrade game is treacherous. Fallen angels can fall further (BBB → BB → B → CCC → Default). Sector waves cluster (retail 2017, energy 2015, autos 2020). Forced selling creates 20-30% drawdowns that test conviction. The winners anticipate early, size conservatively, take profits at announcement, and avoid sector concentration. The losers wait for agencies, average down, hold through forced selling, and blow up in downgrade cascades. Choose wisely."

**Keys to success:**

1. **Analyze fundamentals, don't wait for agencies** (6-12 month edge)
2. **Focus on BBB/BB boundary** (largest forced flows)
3. **Short downgrade candidates early** (before Watch Negative)
4. **Buy fallen angels late** (after forced selling)
5. **Diversify across sectors** (<15% any sector)
6. **Set hard stop losses** (-10% maximum)
7. **Take profits at announcement** (don't get greedy)
8. **Avoid sector downgrade waves** (exit ALL at first sign)

**Most critical rule:**

$$
\text{First fallen angel in sector} = \text{Exit ALL sector BBB exposure immediately}
$$

Downgrade waves cluster. Retail 2017 proved this: Macy's fell, then Nordstrom, then J.C. Penney, Bon-Ton, Gap, L Brands, and eventually Sears bankruptcy. The first fallen angel is your warning. Exit everyone. The retail fund that lost -19.8% should have exited after Macy's downgrade and saved $41M. Learn from their mistake. 🎯📊
