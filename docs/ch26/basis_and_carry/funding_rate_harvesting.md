# Funding-Rate Harvesting

**Funding-rate harvesting** systematically collects periodic payments in cryptocurrency perpetual swap markets by maintaining delta-neutral positions (long spot + short perpetual, or vice versa) to capture the funding rate—typically 0.01-0.10% every 8 hours paid from longs to shorts when positive—generating annualized returns of 11-109% depending on market sentiment, leverage demand, and positioning imbalances, while managing risks including funding reversal (flipping from positive to negative), exchange failure (counterparty risk), liquidation on leveraged legs, and the opportunity cost of capital deployed in what is essentially a carry trade betting that crypto derivatives will persistently trade at a premium to spot.

---

## The Core Insight

**The fundamental idea:**

- Perpetual funding rate = Payment every 8 hours
- Positive funding: Longs pay shorts (typical 80% of time)
- Harvest by being short perp + long spot (delta-neutral)
- Annual yield: 11-30% normal, 50-100%+ in euphoria
- Unlike quarterly futures (converge at expiration), perpetuals never expire
- Funding varies continuously based on supply/demand for leverage
- Higher leverage demand = Higher funding (more to harvest)
- Risk: Funding can flip negative (you pay instead of receive)
- Capital intensive: Requires full notional on both legs

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/funding_rate_harvesting_dynamics.png?raw=true" alt="funding_rate_harvesting_dynamics" width="700">
</p>
**Figure 1:** Funding rate harvesting framework showing entry triggers (funding >0.03%), position structure (long spot + short perp), daily collection mechanics, dynamic adjustment based on funding changes, exit signals (funding <0.015%), and risk controls including exchange diversification and hedge monitoring.

**You're essentially asking: "How do I systematically collect funding rates as income?"**

---

## Understanding Funding Mechanics

### 1. Funding Rate Formula

**Exchange calculation:**

$$
\text{Funding Rate} = \text{Average Premium} + \text{clamp}(\text{Interest Rate} - \text{Premium}, 0.05\%, -0.05\%)
$$

**Premium component:**

$$
\text{Premium} = \frac{\text{Perp TWAP} - \text{Spot Index TWAP}}{\text{Spot Index TWAP}}
$$

Where TWAP = Time-weighted average price over funding period

**Interest component:**

Typically 0.01% per 8 hours (cost of capital baseline)

**Example:**

BTC perpetual: $43,100
BTC spot index: $43,000
- Premium: $(43,100 - 43,000) / 43,000 = 0.233\%$
- Interest: 0.01%
- **Funding rate: 0.01%** per 8 hours

**If premium higher:**

Perpetual: $43,500 (longs aggressive)
- Premium: 1.16%
- Clamped to +0.05% max (on some exchanges)
- **Funding rate: 0.05%** per 8 hours

### 2. Payment Calculation

**Individual position:**

$$
\text{Payment} = \text{Position Size} \times \text{Funding Rate}
$$

**Paid every 8 hours** (typical: 00:00, 08:00, 16:00 UTC)

**Direction:**
- If funding positive (+): Longs pay shorts
- If funding negative (-): Shorts pay longs

**Example:**

Short 10 BTC perpetual at $43,000:
- Notional: $430,000
- Funding: +0.03% per 8 hours
- Payment received: $430,000 × 0.03% = **$129** (every 8 hours)

**Daily:**
- 3 payments × $129 = **$387/day**

**Monthly:**
- $387 × 30 = **$11,610**

**Annualized:**
- $387 × 365 = **$141,255** (32.8% annual yield)

### 3. Annualization Convention

**Converting 8-hour rate to annual:**

$$
\text{Annual Funding} = \text{Rate}_{8h} \times 3 \times 365
$$

**Example rates:**

| 8-hour Rate | Daily | Annual |
|-------------|-------|--------|
| 0.01% | 0.03% | 10.95% |
| 0.02% | 0.06% | 21.90% |
| 0.03% | 0.09% | 32.85% |
| 0.05% | 0.15% | 54.75% |
| 0.10% | 0.30% | 109.50% |

**Interpretation:**
- 0.01%: Normal, sustainable
- 0.03%: Elevated, good harvest
- 0.05%: High, excellent harvest
- 0.10%: Extreme, unsustainable (reversal risk)

### 4. Funding Rate Drivers

**What determines funding:**

**1. Leverage demand:**
- More longs wanting leverage → Higher funding
- Shorts scarce → Longs pay premium

**2. Market sentiment:**
- Bullish: Positive funding (longs dominate)
- Bearish: Can go negative (shorts dominate)
- Neutral: Close to 0.01% (baseline)

**3. Capital availability:**
- Limited short capital → Higher funding
- Abundant arbitrage capital → Lower funding

**4. Volatility:**
- High vol → Lower appetite for leverage → Lower funding
- Low vol → More leverage → Higher funding

**Example—Bull market:**
- BTC rallying $40K → $60K
- Retail FOMO, everyone wants long leverage
- Funding: 0.05-0.10% (54-109% annual)
- Shorts scarce, can collect premium

**Example—Bear market:**
- BTC falling $60K → $30K
- Shorts pile in, longs exit
- Funding: Can go -0.05% (shorts pay longs)
- Harvesting becomes paying!

### 5. Historical Patterns

**Typical funding by market regime:**

**Bull market (2020-2021):**
- Average: 0.02-0.05% (22-55% annual)
- Peak: 0.15% (164% annual, May 2021)
- Duration: Months of elevated funding

**Bear market (2022):**
- Average: 0.00-0.02% (0-22% annual)
- Periods of negative funding
- Lower but still positive most of time

**Sideways (2023-2024):**
- Average: 0.01-0.03% (11-33% annual)
- Stable, predictable
- Good for harvesting

**Volatility events:**
- COVID crash: -0.20% (panic, shorts paying)
- May 2021 crash: Flipped from +0.15% to -0.05%
- Recovery: Back to positive within days

### 6. Cross-Asset Comparison

**Funding varies by asset:**

**BTC (most stable):**
- Typical: 0.01-0.03%
- Extremes: -0.10% to +0.15%
- Most liquid, best for harvesting

**ETH:**
- Typical: 0.02-0.05%
- Higher than BTC (more retail interest)
- Good alpha opportunity

**Altcoins (SOL, AVAX, etc):**
- Typical: 0.03-0.10%
- Much higher variance
- Higher yield but higher risk

**Example snapshot (bull market):**
- BTC funding: 0.03% (33% annual)
- ETH funding: 0.05% (55% annual)
- SOL funding: 0.08% (87.6% annual)

**Strategy:** Diversify to capture higher alts while using BTC as stable base

### 7. Exchange Differences

**Funding varies by platform:**

**Binance (largest):**
- BTC: 0.02% typical
- Liquid, tight spreads
- Most reliable

**Bybit:**
- BTC: 0.025% typical
- Often 10-20% higher than Binance
- Opportunity for cross-exchange arb

**OKX:**
- BTC: 0.018% typical
- Often lower (more arb capital)

**Deribit:**
- BTC: 0.03% typical
- Higher (options-focused platform)

**Cross-exchange strategy:**
- Long spot on Coinbase
- Short perp on highest-funding exchange
- Capture differential

---

## Key Terminology

**Funding Rate:**
- Periodic payment (8-hour)
- Percentage of notional
- Longs pay shorts (typical)
- Measured per period

**Annualized Funding:**
- Rate × 1,095 (3 × 365)
- Comparison to annual yield
- Assumes constant rate (unrealistic)
- Useful for sizing decisions

**Funding Timestamp:**
- Specific times (00:00, 08:00, 16:00 UTC typical)
- Must hold position through timestamp
- Payment automatic
- Can enter/exit between timestamps

**Funding History:**
- Past funding rates
- Reveals patterns
- Identifies extremes
- Informs entry/exit

**Delta-Neutral:**
- Long spot + Short perp (equal notional)
- Or short spot + Long perp (if funding negative)
- Net price exposure = 0
- Only collect funding

**Harvesting Yield:**
- Funding collected / Capital deployed
- Annualized for comparison
- Net of costs
- Risk-adjusted return metric

**Funding Reversal:**
- Switch from positive to negative
- Or negative to positive
- Risk for harvesters
- Requires position flip

---

## Funding Harvesting Strategies

### 1. Basic Long-Short Harvest

**Strategy:**

Long spot, short perpetual, collect positive funding

**Setup:**
- Monitor funding rates
- Enter when >0.03% per 8h (33% annual)
- Hold until <0.015% or target achieved

**Example:**

Funding: 0.04% per 8h (43.8% annual)

**Position:**
- Buy: 10 BTC spot at $43,000 = $430,000 (Coinbase)
- Short: 10 BTC perpetual at $43,000 (Binance)
- Net delta: 0

**Daily collection:**
- 0.04% × 3 = 0.12% daily
- $430,000 × 0.12% = **$516/day**

**Monthly:**
- $516 × 30 = **$15,480** (3.6% monthly)

**Annual projection:**
- $516 × 365 = **$188,340** (43.8% annually)

**Hold duration:** 90 days (collected $46,440)

**Exit trigger:**
- Funding drops to 0.012% (13.14% annual)
- Below threshold, not worth exchange risk

### 2. Dynamic Allocation

**Strategy:**

Adjust position size based on funding level

**Allocation rules:**

$$
\text{Allocation} = \begin{cases}
0\% & \text{if Funding} < 0.015\% \\
15\% & \text{if } 0.015\% \leq \text{Funding} < 0.03\% \\
30\% & \text{if } 0.03\% \leq \text{Funding} < 0.05\% \\
50\% & \text{if Funding} \geq 0.05\%
\end{cases}
$$

**Example:**

$1M portfolio

**Week 1:** Funding 0.02% (22% annual)
- Allocation: 15% = $150K
- Collecting: $150K × 22% = $33K annually

**Week 5:** Funding rises to 0.06% (65.7% annual)
- Increase to: 50% = $500K
- Collecting: $500K × 65.7% = $328.5K annually

**Week 12:** Funding drops to 0.01% (11% annual)
- Reduce to: 0% (exit)
- Collected total: $85K (8.5% on $1M over 12 weeks)

**Advantage:**
- Maximize exposure when funding high
- Minimize when low
- Better risk-adjusted returns

### 3. Multi-Asset Diversification

**Strategy:**

Spread across BTC, ETH, and alts for diversification

**Rationale:**
- Different funding patterns
- Lower correlation
- Reduces concentration risk

**Example allocation:**

$1M portfolio, funding elevated across board

**BTC (40%):** $400K
- Funding: 0.03% (33% annual)
- Expected: $132K annually

**ETH (35%):** $350K
- Funding: 0.05% (54.75% annual)
- Expected: $191.6K annually

**SOL (15%):** $150K
- Funding: 0.08% (87.6% annual)
- Expected: $131.4K annually

**AVAX (10%):** $100K
- Funding: 0.10% (109.5% annual)
- Expected: $109.5K annually

**Total expected:** $564.5K annually (56.45% on $1M)

**Risk reduction:**
- If BTC funding normalizes: Still have ETH/SOL/AVAX
- If Binance fails: Diversified across exchanges
- If one asset funding reverses: Others may stay positive

### 4. Cross-Exchange Optimization

**Strategy:**

Harvest on highest-funding exchange for each asset

**Process:**

1. Check funding across exchanges (Binance, Bybit, OKX, Deribit)
2. Long spot on safest exchange (Coinbase/Kraken)
3. Short perp on highest-funding exchange
4. Capture differential

**Example:**

BTC funding snapshot:
- Binance: 0.03%
- Bybit: 0.035%
- Deribit: 0.04%

**Trade:**
- Long: 10 BTC spot on Coinbase ($430K)
- Short: 10 BTC perp on Deribit at 0.04% funding

**Extra yield:**
- Deribit: 43.8% annual
- vs Binance: 32.85% annual
- **Additional: 10.95%** (47K extra annually)

**Risk:**
- Deribit counterparty risk higher than Binance
- Weigh extra yield vs risk

### 5. Funding Momentum Strategy

**Strategy:**

Follow funding trends (rising/falling)

**Rules:**
- Enter when funding rising (3 days up)
- Increase when continues rising
- Exit when declining (2 days down)

**Example:**

**Day 1-3:** Funding 0.02% → 0.03% → 0.04% (rising)
- Enter: 30% allocation on day 3

**Day 4-7:** Funding 0.04% → 0.05% → 0.06% → 0.07%
- Increase: 50% allocation on day 7

**Day 8-9:** Funding 0.07% → 0.06% → 0.05% (declining)
- Exit: Close position on day 9

**Result:**
- Captured: 5 days at high funding (0.05-0.07%)
- Avoided: Continued decline to 0.02%
- **Better timing than static hold**

### 6. Negative Funding Harvest

**Strategy:**

When funding negative, reverse position (short spot, long perp)

**Rare but occurs in:**
- Extreme fear (COVID crash)
- Bear market capitulation
- Specific asset panic

**Example:**

March 2020, funding: -0.10% (shorts paying longs)

**Reverse position:**
- Short: 10 BTC (via futures or borrow)
- Long: 10 BTC perpetual

**Collect from shorts:**
- $430K × 0.10% × 3 = **$1,290/day**
- Annual: 109.5%

**Hold:** 5-10 days until funding normalizes

**Risk:**
- Borrowing BTC to short (borrow costs)
- Timing (funding can go more negative)
- Execution (harder to short spot)

### 7. Funding Spread Arbitrage

**Strategy:**

Long low-funding perp, short high-funding perp (same asset)

**Example:**

BTC funding:
- Binance: 0.02%
- Deribit: 0.05%
- Spread: 0.03%

**Trade:**
- Long: BTC perp on Binance (pay 0.02%)
- Short: BTC perp on Deribit (collect 0.05%)
- Net: Collect 0.03% per 8h (33% annual)

**Advantage:**
- No spot position needed (both perps)
- Lower capital (margin only, not full notional)
- Pure funding differential

**Disadvantage:**
- Both legs on derivatives (2× exchange risk)
- Spread can narrow (lose opportunity)
- Requires monitoring both exchanges

---

## Common Mistakes

### 1. Projecting Peak Funding

**Assuming constant high funding:**

- **Mistake:** Entry at 0.10% funding, project 109.5% annual for year
- **Why it fails:** Funding mean-reverts to 0.01-0.03%
- **Fix:** Use conservative average (0.02-0.03% for projections)
- **Real cost:** Overestimate returns by 70-80%

**Example:**

Entry when funding 0.10% (109.5% annual):
- Projected: $500K × 109.5% = $547.5K annual

**Reality:**
- Month 1-2: 0.10% (collect $91.25K)
- Month 3-12: Average 0.02% (collect $100K)
- **Total: $191.25K** (38.25% actual vs 109.5% projected)

### 2. Single Exchange Concentration

**All positions on one platform:**

- **Mistake:** Long spot + short perp both on Binance
- **Why it fails:** Exchange failure = both legs lost
- **Fix:** Spot on Exchange A, perp on Exchange B
- **Real cost:** 100% loss (FTX: $8B frozen)

**Correct:**
- Spot: Coinbase (withdraw to cold storage)
- Perp: Binance (margin only, $50K vs $500K notional)
- Risk: Only $50K on Binance, $450K in cold storage

### 3. Ignoring Negative Funding Risk

**Not monitoring for reversal:**

- **Mistake:** Set-and-forget harvesting position
- **Why it fails:** Funding flips negative, now paying instead of collecting
- **Fix:** Daily monitoring, exit if funding <0%
- **Real cost:** Paying 11-30% annually instead of collecting

**Example:**

May 2021, funding +0.12% (harvesting $1,500/day):
- Crash happens
- Funding flips to -0.08% (now paying $1,000/day)
- If don't exit: Lose $30K/month
- **Should have exited immediately**

### 4. Overleveraging

**Using margin to amplify:**

- **Mistake:** Borrow to increase position 3-5×
- **Why it fails:** Funding drops below borrow cost
- **Fix:** No leverage or max 1.5×
- **Real cost:** Negative carry (paying more than collecting)

**Example:**

Own $200K, borrow $800K at 8%:
- Total: $1M harvesting position
- Funding: Starts 0.05% (54.75%), drops to 0.015% (16.4%)
- Funding income: $1M × 16.4% = $164K
- Borrow cost: $800K × 8% = $64K
- **Net: $100K** (50% ROE, but declining)

**If funding drops to 0%:**
- Income: $0
- Borrow: $64K
- **Net: -$64K** (total loss)

### 5. Hedge Ratio Drift

**Not rebalancing:**

- **Mistake:** Initial 10 BTC spot, 10 BTC short, never adjust
- **Why it fails:** Funding payments change notional slightly
- **Fix:** Monthly rebalance (check delta)
- **Real cost:** Directional exposure, losses on price moves

**Example:**

Initial:
- Spot: 10 BTC
- Perp: 10 BTC short

**After 6 months:**
- Spot: Still 10 BTC
- Perp: Effective 9.92 BTC (funding drained margin slightly)
- Unhedged: 0.08 BTC ($3,440 at $43K)

**BTC drops 20%:**
- Unhedged loss: 0.08 × $43K × 20% = **$688**
- Should have been $0 if properly hedged

### 6. Tax Inefficiency

**Short-term treatment:**

- **Mistake:** Close and reopen every month (harvest profits)
- **Why it fails:** Every close = short-term capital gain (37% tax)
- **Fix:** Hold >1 year if possible, minimize turnover
- **Real cost:** 37% tax vs 20% long-term

**Example:**

Monthly closes (12 taxable events):
- Profit: $100K
- Tax (short-term): $100K × 37% = **$37K**

**Annual close (1 event, held >1 year):**
- Profit: $100K
- Tax (long-term): $100K × 20% = **$20K**

**Savings: $17K** (85% more after-tax by holding longer)

### 7. Exit Delay

**Not exiting when funding normalizes:**

- **Mistake:** Funding drops to 0.01% (11% annual), stay in
- **Why it fails:** Tying up capital for low yield
- **Fix:** Exit when funding <0.015%, redeploy elsewhere
- **Real cost:** Opportunity cost (missed better trades)

**Example:**

Funding drops to 0.01% (11% annual):
- Collecting: $500K × 11% = $55K annually
- Opportunity elsewhere: DeFi earning 20%
- **Cost of staying: $45K** (9% opportunity cost)

---

## Risk Management Rules

### 1. Funding Entry Threshold

**Minimum for entry:**

$$
\text{Min Funding} = 0.03\% \text{ per 8h} \quad (32.85\% \text{ annual})
$$

**Rationale:**
- Below this: Barely covers exchange + opportunity risk (5% + 10% = 15%)
- Above this: Meaningful risk premium

**Exception:**
- Can enter at 0.02% if very stable, low-volatility environment

### 2. Exit Threshold

**Exit if funding drops below:**

$$
\text{Exit Funding} = 0.015\% \text{ per 8h} \quad (16.4\% \text{ annual})
$$

**Rationale:**
- 16.4% - 5% opportunity - 10% risk premium = 1.4% net
- Not worth exchange risk for <2% net yield

### 3. Allocation Limits

**Maximum in funding harvesting:**

$$
\text{Max Allocation} = 50\% \text{ of Total Portfolio}
$$

**By asset:**
- BTC: 30% max
- ETH: 20% max
- Alts: 15% combined max

**Example:**

$1M portfolio:
- BTC harvesting: $300K
- ETH harvesting: $200K
- SOL harvesting: $100K
- Other strategies: $400K

### 4. Leverage Prohibition

**No borrowing for harvesting:**

$$
\text{Leverage} = 1.0\times \quad (\text{no borrowed capital})
$$

**Exception:**
- Max 1.5× if funding >0.08% and very stable

**Rationale:**
- Funding too volatile for leveraged carry
- Borrow costs (6-10%) eat into profits
- Risk of negative carry if funding drops

### 5. Daily Monitoring

**Required checks:**

1. **Funding rate:** Changed from yesterday?
2. **Position delta:** Still neutral? (should be ~0)
3. **Exchange news:** Regulatory, solvency, hacks?
4. **Collected funding:** Matches expectation?

**Alert thresholds:**
- Funding drops >50% (e.g., 0.06% → 0.03%)
- Funding goes negative (<0%)
- Delta >2% (hedge broken)

### 6. Exchange Diversification

**Maximum per exchange:**

$$
\text{Per Exchange} \leq 40\% \text{ of Harvesting Capital}
$$

**Example:**

$500K in harvesting:
- Binance perp: $200K (40%)
- Bybit perp: $150K (30%)
- OKX perp: $150K (30%)

**Spot:**
- Coinbase: $250K (withdraw to cold storage)
- Kraken: $250K (withdraw to cold storage)

### 7. Funding History Analysis

**Monthly review:**

Track 30-day average funding:

$$
\text{Avg}_{30d} = \frac{\sum_{i=1}^{90} \text{Funding}_i}{90}
$$

**Decision:**
- If current >1.5 × average: Overextended, reduce exposure
- If current <0.5 × average: Below normal, consider exit
- If current ≈ average: Sustainable, maintain

**Example:**

30-day average: 0.04%
- Current: 0.10% (2.5× average)
- Action: Reduce allocation from 50% to 30% (take profits)

---

## Real-World Examples

### 1. Q1 2021 Bull Market Harvest

**Event:** Sustained high funding during rally

**Setup (January-March 2021):**
- BTC rallying $30K → $60K
- Funding: Consistently 0.05-0.10% per 8h
- Duration: 3 months of elevated rates

**Trade executed:**

January 15, funding 0.08% (87.6% annual):
- Long: 20 BTC spot at $35,000 = $700K
- Short: 20 BTC perp at $35,000

**Daily collection:**
- 0.08% × 3 = 0.24% daily
- $700K × 0.24% = **$1,680/day**

**3-month results (90 days):**
- Total collected: $1,680 × 90 = **$151,200**
- Return: 21.6% in 90 days
- Annualized: 86.4%

**Exit:** April 15, funding dropped to 0.025% (27.4% annual)

**Lesson:** High funding can persist for months in strong bull markets

### 2. May 2021 Crash Reversal

**Event:** Funding flipped from extreme positive to negative

**Pre-crash:**

May 10-18:
- BTC: $55K-$64K
- Funding: 0.10-0.15% (109-164% annual)
- Harvesters collecting aggressively

**May 19 crash:**
- BTC: $64K → $30K (53% in 24 hours)
- Funding: Flipped to -0.08% (-87.6% annual!)
- Harvesters now paying instead of collecting

**Impact on $1M harvesting position:**

**Before crash:**
- Collecting: $1M × 0.15% × 3 = $4,500/day

**After crash:**
- Paying: $1M × 0.08% × 3 = $2,400/day (loss)

**If didn't exit immediately:**
- Week of paying: $2,400 × 7 = $16,800 loss
- vs could have saved if exited on crash

**Lesson:** Extreme funding reverses violently, monitor closely

### 3. 2022 Bear Market Grind

**Event:** Low but stable funding in bear market

**Setup (Most of 2022):**
- BTC range: $16K-$25K (down from $69K ATH)
- Funding: 0.01-0.02% most of year
- Not exciting but consistent

**Trade:**

Conservative harvesting:
- Position: $500K
- Avg funding: 0.015% (16.4% annual)

**Annual collection:**
- $500K × 16.4% = **$82K**
- After costs (5% opportunity): **$57K net**
- Return: 11.4% annual

**Comparison:**
- S&P 500 2022: -18%
- BTC 2022: -64%
- Harvesting: +11.4%

**Lesson:** Harvesting provides steady income even in bear markets

### 4. COVID Negative Funding (March 2020)

**Event:** Extreme negative funding during panic

**March 12-13, 2020:**
- BTC crashed $8,000 → $3,800
- Funding: -0.15% to -0.20% (shorts dominant)
- Shorts paying longs handsomely

**Reverse harvest:**

- Short spot: 10 BTC (via futures short)
- Long perp: 10 BTC

**Collection (from shorts):**
- $43K × 10 BTC × 0.18% × 3 = **$2,322/day**

**Duration:** 3-5 days until funding normalized

**Total collected:** $2,322 × 4 = **$9,288**

**Lesson:** Negative funding offers opportunities if can reverse position quickly

### 5. FTX Collapse (November 2022)

**Event:** Exchange failure mid-harvest

**Traders affected:**

$1M harvesting on FTX:
- Long: 23.26 BTC spot on FTX
- Short: 23.26 BTC perp on FTX
- Collecting: $300/day funding

**November 8:** FTX halts withdrawals
- Both legs frozen
- Bankruptcy filed
- **Total loss: $1M** despite "hedged" position

**If diversified:**

- Long: 23.26 BTC spot on Coinbase (withdrawn to cold storage)
- Short: 23.26 BTC perp on FTX ($100K margin)
- **Loss: $100K** (perp margin only)
- **Spot safe: $900K** (in cold storage)

**Lesson:** Exchange diversification critical for harvesting

### 6. ETH Merge Premium (August-September 2022)

**Event:** ETH funding elevated pre-merge

**Setup:**

August 2022, 1 month before merge:
- ETH funding: 0.08-0.12% (87-131% annual)
- Uncertainty drove longs (bullish) and shorts (uncertainty)
- Net: Longs dominated

**Trade:**

- Long: 500 ETH spot at $1,800 = $900K
- Short: 500 ETH perp at $1,800

**30-day collection:**
- Average funding: 0.10%
- Daily: $900K × 0.30% = $2,700
- **Total: $2,700 × 30 = $81K** (9% in 1 month)

**Post-merge:** Funding normalized to 0.02%

**Lesson:** Event-driven funding spikes create harvesting opportunities

### 7. Altcoin Funding Differential (2023)

**Event:** Alts funding much higher than BTC/ETH

**Setup:**

Snapshot (bull period):
- BTC funding: 0.02% (22% annual)
- ETH funding: 0.04% (44% annual)
- SOL funding: 0.10% (109.5% annual)
- AVAX funding: 0.12% (131.4% annual)

**Trade allocation:**

$1M total:
- BTC: $400K at 22% = $88K annual
- ETH: $300K at 44% = $132K annual
- SOL: $200K at 109.5% = $219K annual
- AVAX: $100K at 131.4% = $131.4K annual

**Total: $570.4K annually** (57% blended yield)

**Risk:**
- Alts more volatile (funding can reverse faster)
- Less liquidity (harder to exit)
- Higher exchange risk (concentrated on offshore)

**Result (6 months):**
- Collected: $285K (28.5% in 6 months)
- One position (AVAX) funding dropped to 0.01%, exited early
- **Net: 25% return in 6 months** (annualized 50%)

---

## Practical Steps

### 1. Monitor Funding Landscape

**Daily routine (10 minutes):**

Check funding across assets and exchanges:

**BTC:**
- Binance: 0.025%
- Bybit: 0.03%
- OKX: 0.02%

**ETH:**
- Binance: 0.04%
- Bybit: 0.045%
- OKX: 0.035%

**Identify opportunities:**
- ETH Bybit: 49.3% annual (attractive)
- BTC OKX: 21.9% annual (marginal)

### 2. Calculate Expected Yield

**Formula:**

$$
\text{Net Yield} = \text{Funding Rate} \times 1095 - \text{Costs}
$$

**Example:**

Funding: 0.04% per 8h
- Gross annual: 0.04% × 1,095 = 43.8%
- Opportunity cost: 5%
- Risk premium required: 10%
- Entry/exit costs: 1%
- **Net expected: 27.8% annually**

### 3. Size Position

**Allocation decision:**

If net yield 27.8%:
- Above 20% threshold: Allocate 30-40%
- $1M portfolio: $300-400K

**Example position:**

$350K allocation:
- Long: 8.14 BTC spot at $43,000 = $350K (Coinbase)
- Short: 8.14 BTC perp at $43,000 (Bybit)

### 4. Execute Simultaneously

**Step-by-step:**

1. **Transfer funds:**
   - $350K USDT to Coinbase
   - $35K USDT to Bybit (10% for perp margin)

2. **Buy spot first:**
   - Limit order: 8.14 BTC at $43,000
   - Wait for fill

3. **Short perp immediately (30 seconds after spot fill):**
   - Limit order: 8.14 BTC at $43,000
   - Leverage: 10× (margin $35K, notional $350K)
   - Wait for fill

4. **Verify hedge:**
   - Spot: Long 8.14 BTC
   - Perp: Short 8.14 BTC notional
   - **Delta: 0** ✓

### 5. Track Daily Collection

**Set up tracking spreadsheet:**

| Date | Funding Rate | Notional | Daily Collection | Cumulative |
|------|-------------|----------|-----------------|------------|
| Day 1 | 0.04% | $350K | $420 | $420 |
| Day 2 | 0.042% | $350K | $441 | $861 |
| Day 3 | 0.038% | $350K | $399 | $1,260 |

**Monthly total:** ~$12,600 (3.6% monthly)

### 6. Rebalance if Needed

**Monthly check:**

Calculate delta:

$$
\Delta = \text{Spot Notional} - \text{Perp Notional}
$$

**Example:**

After 3 months:
- Spot: 8.14 BTC @ $45,000 = $366,300
- Perp: 8.14 BTC notional (still $350K in system)
- Delta: $16,300 (4.7% unhedged)

**Rebalance:**
- Reduce perp short by 0.36 BTC
- Or sell 0.36 BTC spot
- Return to delta = 0

### 7. Exit When Triggered

**Exit rule:** Funding <0.015% for 3 consecutive days

**Example:**

Day 88: Funding drops to 0.018% (still ok)
Day 89: Funding 0.014% (below threshold)
Day 90: Funding 0.012% (confirmed exit signal)

**Exit process:**

1. **Close perp short:**
   - Buy 8.14 BTC perp to close
   - Withdraw margin ($35K)

2. **Decide on spot:**
   - Option A: Sell spot (full exit)
   - Option B: Withdraw to cold storage (hold BTC)

3. **Calculate return:**
   - Collected: 90 days × $420 avg = $37,800
   - Costs: $1,750 (entry fees)
   - **Net profit: $36,050** (10.3% in 90 days, 41.2% annualized)

---

## Final Wisdom

> "Funding-rate harvesting is crypto's version of being the house in a casino—you're systematically collecting small, regular payments from leverage-hungry traders who outnumber the shorts (80% of the time historically), generating 11-30% annually in normal markets and 50-100%+ when euphoria hits and funding reaches 0.10-0.15% per 8 hours. The mechanism is beautiful: perpetual swaps need to track spot but have no expiration to force convergence, so instead they use funding rates—longs pay shorts every 8 hours based on the premium of perpetual over spot, creating a continuous incentive for arbitrageurs to short perpetuals when they're expensive. During bull markets, leverage demand is insatiable (everyone wants to long BTC with 10-20× leverage), so funding stays elevated for months: Q1 2021 averaged 0.05-0.08% per 8 hours (54-87% annually) for THREE MONTHS straight, letting harvesters collect 20%+ quarterly returns with market-neutral positions. The capital efficiency isn't as good as it seems: you need full $430K to buy 10 BTC spot, plus $43K margin to short 10 BTC perp at 10× leverage = $473K deployed for $430K exposure, yielding $141K annually at 0.03% funding = 29.8% ROE, good but not spectacular compared to DeFi's 20-60% yields without counterparty risk. The killer risks: (1) FTX proved exchange failure wipes 'hedged' positions if both legs on same platform—$8B lost by traders who thought long spot + short perp on FTX was safe, (2) funding reverses violently (May 2021: +0.15% to -0.08% in 24 hours, turning $4,500 daily collection into $2,400 daily payment), (3) mean reversion is vicious (funding 0.10% rarely lasts >2-4 weeks, projecting 109% annually is delusional), (4) opportunity cost during bear markets when funding averages 0.01-0.015% (11-16% annual, barely worth exchange risk). The execution is simple but discipline is hard: enter when funding >0.03% (33% annual minimum to justify exchange risk), exit when <0.015% (16% not worth it), diversify exchanges (spot on Coinbase, perp on Binance, never both on same platform), monitor daily (funding changes constantly), no leverage (funding too volatile for borrowed capital, 6-10% borrow costs kill returns). Cross-asset diversification helps: BTC funding averages 0.02-0.03%, ETH typically 0.04-0.05%, alts like SOL/AVAX can hit 0.08-0.12%, so blending across $1M = $400K BTC + $300K ETH + $200K SOL + $100K AVAX yields 40-60% blended vs 20-30% BTC-only. The math is straightforward—0.04% per 8h × 3 per day × 365 days = 43.8% annually—but reality is messy: funding varies daily (project conservatively at 0.02-0.03% average, not peak), costs matter (1% entry/exit fees + 5% opportunity cost = -6% drag), and exchange risk is existential (FTX taught us 10% counterparty risk premium is justified). The deepest truth: funding harvesting is a volatility-selling strategy—you're short gamma (short perp = short volatility), collecting premium while markets are calm, but getting crushed when volatility spikes and funding reverses, exactly like selling options. For disciplined practitioners with $500K-$5M, harvesting provides steady 15-35% annual returns with moderate risk, vastly superior to TradFi fixed income (2-5%) but inferior to DeFi LP farming (30-100%) with higher smart contract risk."

**Key to success:**

- Enter only when funding >0.03% per 8h (33% annually minimum)
- Exit immediately when funding <0.015% per 8h (16% not worth risk)
- Diversify exchanges (spot Coinbase, perp Binance, never both same platform)
- No leverage (funding too volatile, 6-10% borrow costs kill returns)
- Monitor daily (funding changes constantly, reversal is sudden)
- Conservative projections (use 0.02-0.03% average, not peak 0.10%)
- Diversify assets (BTC 40%, ETH 30%, alts 30% for higher blended yield)
- Rebalance monthly (funding payments drift hedge ratio over time)
