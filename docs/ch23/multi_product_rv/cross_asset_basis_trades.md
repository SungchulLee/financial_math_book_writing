# Cross-Asset Basis Trades


**Cross-asset basis trades** exploit persistent or temporary mispricings between economically linked instruments across different asset classes—such as equity-credit (CDS vs stock), equity-rates (dividend futures vs bonds), commodity-equity (oil vs energy stocks), and FX-rates (currency forwards vs interest rate differentials)—by simultaneously taking opposite positions in related assets and profiting when the basis (spread) converges to fair value, with typical drivers including liquidity imbalances, regulatory constraints, funding costs, and technical flows that create wedges between theoretically linked prices.

> **Prerequisites:** No-arbitrage fundamentals (Section 23.1.1), covered interest parity, and credit-equity linkages. For the Merton model connecting equity volatility to credit spreads, see credit risk fundamentals in Chapter 12.

---

## The Core Insight


**The fundamental idea:**

- Related assets across classes should maintain relationships
- Basis = Actual spread - Theoretical spread
- Temporary dislocations create opportunities
- Fundamental linkage ensures eventual convergence
- Capital structure arbitrage: Equity vs debt of same firm
- Commodity-equity: Physical vs producer equity
- FX triangulation: Currency crosses and rates
- Regulatory/structural forces can maintain basis for extended periods

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/cross_asset_basis_trades.png?raw=true" alt="cross_asset_basis_trades" width="700">
</p>
**Figure 1:** Cross-asset basis relationship map showing linkages between equity-credit (Merton model), equity-rates (dividend discount), commodity-equity (cost pass-through), FX-rates (covered interest parity), with typical basis ranges, convergence timeframes, and key risk factors for each relationship.

**You're essentially asking: "When do prices across asset classes get out of sync, and how do I profit from their re-alignment?"**

---

## What Are Basis Trades?


### 1. The Basis Concept


**Definition:**

$$
\text{Basis} = \text{Actual Spread} - \text{Theoretical Fair Value Spread}
$$

**Fair value from no-arbitrage:**

Related assets must maintain specific relationships, or arbitrage opportunities exist

**Example—Equity vs Credit:**

**Theoretical link (Merton model):**
- Equity = Call option on firm value
- Debt = Firm value - Put option
- Both tied to same underlying (firm value)

**Basis:**

$$
\text{Basis} = \text{Equity Implied Default Prob} - \text{CDS Implied Default Prob}
$$

**Normal:** Should be equal (same company, same risk)
**Reality:** Often diverge by 50-200 bps

### 2. Equity-Credit Basis


**Relationship:**

**CDS spread reflects credit risk:**
$$
\text{CDS Spread} \approx (1 - \text{Recovery Rate}) \times \text{Default Probability}
$$

**Equity implied default probability:**

From Merton model:
$$
P(\text{Default}) = N\left(\frac{\ln(D/V) - \mu T}{\sigma\sqrt{T}}\right)
$$

Where:
- $D$ = Debt
- $V$ = Firm value (from equity market cap)
- $\mu$ = Drift
- $\sigma$ = Equity volatility

**Example:**

Company XYZ:
- Market cap: $10B
- Debt: $5B
- Equity vol: 30%
- Equity implied default: 5% (from Merton)

**CDS market:**
- 5-year CDS: 200 bps
- Implied default: 3.3% (assuming 40% recovery)

**Basis:** 5% - 3.3% = **+1.7%** (equity implies more risk)

**Interpretation:** Equity cheap relative to credit, or credit expensive relative to equity

### 3. Commodity-Equity Basis


**Relationship:**

**Oil price affects energy stocks:**

$$
\text{Stock Return} \approx \beta_{\text{oil}} \times \text{Oil Return} + \alpha
$$

**Typical beta:** Energy stocks have β ≈ 0.3-0.5 to oil

**Basis trade:**

If correlation breaks down:
- Oil up 10%, energy stocks flat
- Expected: Stocks up 3-5% (0.3-0.5 × 10%)
- Basis: -3% to -5% (stocks underperformed)

**Trade:**
- Long energy stocks
- Short oil futures
- Profit when basis normalizes

### 4. FX-Rates Basis


**Covered Interest Parity:**

$$
F = S \times \frac{1 + r_d}{1 + r_f}
$$

**Basis:**

$$
\text{FX Basis} = F_{\text{market}} - F_{\text{theoretical}}
$$

**Example:**

EUR/USD:
- Spot: 1.0800
- USD rate: 5.5%
- EUR rate: 3.5%
- Theoretical forward (1Y): 1.1009

**Market forward:** 1.1050

**Basis:** 1.1050 - 1.1009 = **+0.0041** (41 pips)

**Interpretation:** EUR forward expensive (or FX hedging demand high)

### 5. Dividend-Rates Basis


**Relationship:**

**Dividend futures should reflect discounted dividends:**

$$
F_{\text{div}} = \sum_{i} \frac{D_i}{(1+r)^{t_i}}
$$

**Basis:**

$$
\text{Div Basis} = F_{\text{div}} - \text{PV(Expected Dividends)}
$$

**Example:**

S&P 500 dividend futures (1Y):
- Expected dividends: $70 (total over year)
- Discount rate: 5%
- PV: $70 / 1.05 = $66.67

**Market future:** $68

**Basis:** $68 - $66.67 = **+$1.33** (2% rich)

**Trade:** Sell dividend future, expect convergence

### 6. Convertible-Equity Basis


**Relationship:**

**Convert bond = Bond + Embedded call:**

$$
\text{Convert} = \text{Straight Bond} + \text{Call Option}
$$

**Basis:**

$$
\text{Basis} = \text{Convert Price} - (\text{Bond Floor} + \text{Option Value})
$$

**Example:**

Convert bond:
- Price: $1,050
- Bond floor: $900 (straight bond value)
- Stock: $45, Conversion ratio: 20
- Conversion value: 20 × $45 = $900
- Option value (from BS): $120

**Fair value:** $900 + $120 = $1,020

**Basis:** $1,050 - $1,020 = **+$30** (3% rich)

### 7. Index-Sector Basis


**Relationship:**

**Index = Weighted sum of sectors:**

$$
\text{SPX} = \sum_{s} w_s \times \text{Sector}_s
$$

**Basis:**

If sectors mispriced relative to index

**Example:**

S&P 500: 4,500
- Tech (XLK) weight: 28%
- Finance (XLF) weight: 13%
- Healthcare (XLV) weight: 13%
- ... (other sectors)

**Synthetic S&P from sectors:** 4,480

**Basis:** 4,500 - 4,480 = **+20 points** (0.44%)

**Trade:** Buy cheap sectors, sell index

---

## Key Terminology


**Basis:**
- Spread between related assets
- Actual vs theoretical
- Positive = expensive, negative = cheap
- Mean-reverting (typically)

**Capital Structure Arbitrage:**
- Equity vs credit same firm
- Exploits Merton model relationship
- Long cheap, short expensive
- Convergence when perception aligns

**Merton Model:**
- Equity as call option on firm
- Structural credit model
- Links equity vol to default risk
- Foundation for equity-credit basis

**Covered Interest Parity:**
- FX forward vs spot + rates
- Should hold by arbitrage
- Basis = CIP violation
- Persistent post-2008 (regulatory)

**Conversion Premium:**
- Convertible bond richness
- Premium over parity
- Reflects optionality value
- Arbitrageable with hedges

**Recovery Rate:**
- Credit loss given default
- Typically 40% (senior unsecured)
- Affects CDS pricing
- Links to equity value

**Beta:**
- Sensitivity to factor
- Oil beta for energy stocks
- Rate beta for banks
- Basis when beta breaks

---

## Cross-Asset Basis Strategies


### 1. Equity-CDS Arbitrage


**Capital structure trade:**

**Setup:**
- Company's equity implies high default risk
- CDS market prices low risk
- Divergence = opportunity

**Example:**

Bank XYZ:
- Stock: $50, down 30% (market cap $5B)
- Equity volatility: 50% (elevated)
- Merton model implied default: 15%

**CDS market:**
- 5Y CDS: 300 bps
- Implied default: 5% (using 40% recovery)

**Basis:** 15% - 5% = **+10%** (equity much more bearish)

**Trade:**
1. Buy stock: $5M (bet on recovery)
2. Buy CDS protection: $10M notional
3. Net: Long equity, protected if default

**Convergence scenarios:**

**Scenario A: Stock recovers**
- Stock: $50 → $65 (+30%)
- Equity implied default: 15% → 8%
- CDS: 300 bps → 200 bps (tightens)
- **Both profitable**

**Scenario B: Company deteriorates**
- Stock: $50 → $30 (-40%)
- CDS: 300 bps → 800 bps (widens)
- Default occurs: CDS pays out
- **CDS profit offsets stock loss**

### 2. Oil-Energy Stock Basis


**Commodity-equity linkage:**

**Setup:**
- Oil rallies +20%
- Energy stocks lag, only +5%
- Historical beta: 0.5 (should be +10%)
- **Underperformance: -5%**

**Trade:**
1. Long energy stocks (XLE ETF): $10M
2. Short oil futures (CL): Hedge ratio 0.5
3. Contracts: $10M × 0.5 / $70K per contract = 71 contracts

**Expected convergence:**

Energy stocks catch up:
- Stocks: +5% → +10% (additional +5%)
- Oil: Stable at +20%
- Net: +5% on $10M = **$500K profit**

**Risk:**
- Oil reverses before stocks catch up
- Beta permanently shifts lower
- Sector-specific issues (not oil-related)

### 3. FX Basis Arbitrage


**Post-2008 persistent basis:**

**Setup:**
- EUR/USD forward expensive (FX basis negative)
- Covered interest parity violated
- Opportunity for dollar-funded investors

**Example:**

1-year EUR/USD:
- Spot: 1.0800
- USD rate: 5.5%, EUR rate: 3.5%
- Theoretical forward: 1.1009

**Market:**
- Forward: 1.1050
- **Basis: +41 pips** (EUR forward expensive)

**Trade (for USD investor):**
1. Borrow USD: $10M at 5.5%
2. Convert to EUR at spot: €9.26M
3. Invest EUR: 3.5% (receive €9.58M)
4. Sell EUR forward: Lock in 1.1050

**One year later:**
- EUR investment: €9.58M
- Convert at forward: €9.58M × 1.1050 = $10.59M
- Repay USD loan: $10.55M (1.055 × $10M)
- **Profit: $40K** (0.4%, the basis)

**Why persistent?**
- Bank balance sheet constraints
- Regulatory capital charges
- Dollar funding premium
- Hedging demand from EUR corporates

### 4. Dividend Future Arbitrage


**Dividend vs index:**

**Setup:**
- Dividend futures expensive relative to expected dividends
- Sell future, hedge with index

**Example:**

S&P 500 dividend future (2025):
- Future: $72
- Expected dividends: $70
- **Premium: $2** (2.9%)

**Trade:**
1. Sell dividend future: $72
2. Buy S&P 500 index: $4,500 (to collect dividends)
3. Short S&P futures: Hedge price risk

**One year later:**
- Dividends collected: $70
- Dividend future settles: $70 (realized)
- Profit from future: $72 - $70 = $2
- Index hedge: Break even (price neutral)
- **Net: $2 profit** (2.9% on $70 notional)

### 5. Convertible Arbitrage


**Convert vs stock + bond:**

**Setup:**
- Convertible bond expensive
- Sell convert, hedge with stock and credit

**Example:**

Company ABC convertible:
- Convert price: $1,100
- Stock: $48
- Conversion ratio: 20
- Bond floor: $950
- Implied vol: 25%

**Fair value breakdown:**
- Bond component: $950
- Equity option (20 calls at $50 strike): $140
- **Total fair: $1,090**

**Basis:** $1,100 - $1,090 = **+$10** (0.9% rich)

**Trade:**
1. Sell convert: $1,100
2. Buy stock: 20 × $48 = $960 (delta hedge)
3. Short CDS or bonds: $950 (credit hedge)

**Convergence:**
- Convert basis narrows to 0
- Profit: $10 per bond

**Ongoing management:**
- Rehedge delta as stock moves
- Collect carry (coupon vs. hedge costs)

### 6. Sector Rotation Basis


**Index vs sector ETFs:**

**Setup:**
- Tech overperforming (expensive)
- Financials underperforming (cheap)
- Spread at extreme

**Example:**

Historical relationship:
- XLK/XLF ratio: Average 2.5
- Current: 3.0 (tech 20% expensive relative)

**Trade:**
1. Short tech (XLK): $5M
2. Long financials (XLF): $5M
3. Dollar-neutral, market-neutral

**Convergence:**
- Tech underperforms: -10%
- Financials outperform: +10%
- Spread: 3.0 → 2.5
- **Profit:** $5M × (0.10 + 0.10) = **$1M** (20%)

### 7. Term Structure Basis


**Front vs back contracts:**

**Setup:**
- VIX futures in extreme contango
- Front month 15, back month 22
- Historical spread: 4 points

**Trade:**
- Long front month: 15
- Short back month: 22
- Spread: -7 (paying 7 points)

**Convergence:**
- Spread normalizes: -7 → -4
- Profit: 3 points × $1,000 = **$3,000 per spread**

---

## Common Mistakes


### 1. Ignoring Funding Costs


**Forgetting cost of carry:**

- **Mistake:** Calculate basis without funding costs
- **Why it fails:** Leverage costs erode profit
- **Fix:** Include all financing in calculation
- **Real cost:** 2-5% annually

**Example:**

Equity-CDS arbitrage:
- Long $10M stock (borrow at 5%)
- Buy CDS: $50K annually
- Basis: 1% = $100K profit expected

**Funding cost:** $10M × 5% = $500K/year

**Net:** $100K - $500K - $50K = **-$450K loss!**

### 2. Wrong Hedge Ratio


**Misestimating beta:**

- **Mistake:** Use historical beta without adjusting
- **Why it fails:** Beta unstable, regime-dependent
- **Fix:** Dynamic hedge ratio, stress test
- **Real cost:** 20-50% of basis captured

**Example:**

Oil-energy stock trade:
- Historical beta: 0.5
- Current regime beta: 0.3 (low oil sensitivity)
- Hedge with 0.5 ratio

**Result:**
- Oil down 10%
- Expected stock impact: -5% (0.5 × -10%)
- Actual: -3% (0.3 × -10%)
- Overhedged: Lost 2% on hedge
- **Basis profit: 5% expected, 3% realized**

### 3. Structural Basis Persistence


**Assuming mean reversion:**

- **Mistake:** Think all basis reverts quickly
- **Why it fails:** Regulatory/structural forces maintain basis
- **Fix:** Understand WHY basis exists
- **Real cost:** Opportunity cost of tied-up capital

**Example:**

FX basis post-2008:
- EUR/USD basis: -30 bps (persistent)
- Trade: Assume reverts in 3 months
- 10 years later: Still -30 bps!
- **Basis never reverted** (regulatory capital constraints)

### 4. Tail Risk Ignorance


**Not hedging credit risk:**

- **Mistake:** Long equity, short credit (double default exposure)
- **Why it fails:** If company defaults, both legs lose
- **Fix:** Size conservatively, use options for tail
- **Real cost:** 100% loss in default

**Example:**

Capital structure arb on weak company:
- Long stock: $1M
- Short CDS: Receive $100K annually

**Company defaults:**
- Stock → $0 (total loss $1M)
- CDS: Pay out $600K (loss on short!)
- **Total loss: $1.6M** (more than stock alone!)

### 5. Correlation Breakdown


**Assuming stable relationship:**

- **Mistake:** Pair trade assuming correlation persists
- **Why it fails:** Crisis → correlations spike to 1 or flip
- **Fix:** Monitor correlation, have stop-loss
- **Real cost:** 30-60% drawdown

**Example:**

Oil-energy stock basis:
- Normal correlation: +0.7
- Trade: Market-neutral (hedged)

**Crisis (March 2020):**
- Correlation → +0.95 (both crashed together)
- Oil: -50%
- Stocks: -45%
- Hedge didn't work
- **Loss despite "hedge"**

### 6. Liquidity Trap


**Can't exit at favorable prices:**

- **Mistake:** Trade illiquid cross-asset pair
- **Why it fails:** Exit costs >> entry profit
- **Fix:** Only liquid markets
- **Real cost:** Trapped in position

**Example:**

EM equity-credit basis:
- Entry: 5 bp edge
- Exit: 15 bp bid-ask widening (crisis)
- **Net: -10 bp loss**

### 7. Dividend Risk


**Unexpected dividend cuts:**

- **Mistake:** Long dividend future, stock cuts dividend
- **Why it fails:** Future settles at realized (lower)
- **Fix:** Monitor dividend sustainability
- **Real cost:** 20-50% of position

**Example:**

Long S&P dividend future: $70
- Expected: $70 dividends realized
- Reality: COVID, dividends cut to $50
- Future settles: $50
- **Loss: $20** (29% of notional)

---

## Best vs. Worst Case


### 1. Best Case: Success


**Equity-credit arbitrage (2016):**

**Setup:**
- Deutsche Bank crisis fears
- Stock crashed, CDS widened massively

**September 2016:**

**Deutsche Bank:**
- Stock: €11 (down 50% YTD)
- 5Y CDS: 250 bps (elevated but not extreme)
- Equity implied default: 25% (Merton model)
- **Basis: 20%** (equity much more bearish)

**Trade:**
1. Buy stock: $10M at €11
2. Buy CDS: $20M notional at 250 bps

**Rationale:**
- If bank survives: Stock recovers
- If bank defaults: CDS pays out
- Basis too wide (market overreacting)

**October-December 2016:**

**News flow improves:**
- DOJ settlement better than feared
- Capital position stabilizes
- Stock: €11 → €16.50 (+50%)
- CDS: 250 bps → 150 bps (-100 bps)

**P&L:**

**Stock position:**
- Profit: $10M × 50% = **+$5M**

**CDS position:**
- Cost: $10M × 2.5% × 3 months / 12 = -$62.5K
- Mark-to-market gain: $20M × 1% × 5 duration = **+$1M**

**Total:** $5M + $1M - $62.5K = **+$5.94M** (59% return in 3 months)

**Success factors:**
1. Identified extreme basis (20%)
2. Fundamental analysis (bank solvent)
3. Hedged tail risk (CDS protection)
4. Sized appropriately (10% of fund)
5. Patient (3-month hold)

### 2. Worst Case: Disaster


**Oil-energy stock basis (2014-2016):**

**Setup:**
- Hedge fund specializing in commodity-equity basis
- Long energy stocks, short oil (beta-neutral)

**June 2014:**

**Trade thesis:**
- Oil at $105
- Energy stocks fair value
- Beta: 0.5 (historical)

**Position:**
- Long energy stocks (XLE): $100M
- Short oil futures (CL): 500 contracts

**July 2014 - January 2015:**

**Oil crash begins:**
- Oil: $105 → $45 (-57%)
- Energy stocks: Down but less
- Expected: Stocks down 28.5% (0.5 × 57%)
- Actual: Stocks down 35%

**Why basis widened?**

1. **Beta shift:** Energy stocks became MORE correlated to oil
   - Beta: 0.5 → 0.7 (increased sensitivity)
   - Structural change (shale, debt concerns)

2. **Credit fears:** Energy company defaults
   - High debt levels
   - Cash flow collapse
   - Bankruptcy risk

3. **Forced selling:** Energy funds liquidating
   - Redemptions in energy funds
   - Indiscriminate selling
   - Downward spiral

**January 2015: Disaster unfolds**

**P&L:**

**Stock position:**
- $100M × -35% = **-$35M**

**Oil hedge:**
- 500 contracts × $60K decline × $1K per point = **+$30M**

**Net:** -$35M + $30M = **-$5M** (5% loss)

**But it gets worse...**

**February-March 2015:**

**Margin calls on oil shorts:**
- Oil rallied from $45 → $60 (+33%!)
- Shorts: -$15M loss
- Stocks: Only +10% (β still broken)

**Forced liquidation:**
- Cover oil shorts: -$15M
- Stuck with long stocks (illiquid)
- Stocks continued falling

**Final P&L (by March):**
- Stock losses: -$40M
- Oil hedge: +$15M ($30M - $15M)
- **Total: -$25M** (25% loss)

**Aftermath:**

- Fund shut down April 2015
- Investors lost 25%
- Thesis was right (basis did eventually narrow)
- But timing killed them (margin calls, redemptions)

**Lessons:**
1. Beta not stable (regime changes)
2. Basis can widen before narrowing (path matters)
3. Leverage amplifies pain (margin calls)
4. Liquidity asymmetry (can't exit)
5. Structural shifts break relationships

---

## Risk Management Rules


### 1. Basis Threshold


**Minimum profitable basis:**

$$
\text{Min Basis} = 3 \times \text{Total Costs}
$$

**Example:**

Transaction costs: 5 bps each leg = 10 bps total

**Minimum basis:** $3 \times 10 = 30$ bps

**Only trade if basis ≥ 30 bps**

### 2. Correlation Monitoring


**Track rolling correlation:**

$$
\rho_t = \text{Corr}_{t-90:t}(\text{Asset A}, \text{Asset B})
$$

**Exit if:**
- $\rho$ drops below 0.5 (from historical 0.7+)
- Or $\rho$ spikes above 0.95 (correlation to 1)

### 3. Position Limits


**Per basis trade:**

$$
\text{Max Position} \leq 15\% \text{ of Capital}
$$

**Diversification:**
- Max 3 equity-credit trades
- Max 3 commodity-equity trades
- Max 2 FX basis trades

### 4. Stop-Loss Discipline


**Exit if basis widens:**

$$
\text{Stop Loss} = -2 \times \text{Expected Basis Profit}
$$

**Example:**

Expected profit: 20 bps

**If basis widens against you by 40 bps:** Exit

### 5. Leverage Limits


**Maximum leverage per strategy:**

- Equity-credit: 2× max
- Commodity-equity: 1.5× max
- FX basis: 3× max (low vol)

### 6. Funding Management


**Ensure positive carry:**

$$
\text{Expected Basis Profit} > \text{Financing Cost} + \text{Hedge Costs}
$$

**Example:**

Basis profit: 50 bps
- Financing: 30 bps
- Hedge cost: 10 bps
- **Net: +10 bps** ✓

### 7. Stress Testing


**Monthly scenarios:**

1. Basis doubles (widens 100%)
2. Correlation breaks (±0.3 change)
3. Liquidity dries up (10× bid-ask)
4. Funding costs spike (2× increase)

**Maximum loss in worst scenario:**

$$
\text{Stress Loss} \leq 20\% \text{ of Position}
$$

---

## Real-World Examples


### 1. GM Bankruptcy (2009)


**Equity-credit disconnect:**

**March 2009:**
- GM stock: $3 (down 95%)
- 5Y CDS: 5,000 bps (50% default probability)
- Equity implied: 99% default probability

**June 2009:** GM filed bankruptcy

**CDS holders:** Received 12.5¢ on dollar (87.5% loss)
**Equity holders:** Wiped out (100% loss)

**Lesson:** Both were right (default), basis reflected bankruptcy proximity

### 2. FX Basis Post-2008


**Persistent CIP violation:**

**2008-present:**
- EUR/USD basis: -20 to -50 bps (persistent)
- JPY/USD basis: -30 to -80 bps
- Never reverted to zero

**Drivers:**
- Bank balance sheet costs
- Basel III capital charges
- Dollar funding premium

**Lesson:** Some basis is structural, not temporary

### 3. Oil-MLP Basis (2015-2016)


**Energy MLPs vs oil:**

**2015:**
- Oil: $105 → $45 (-57%)
- MLPs: Expected down 20% (β = 0.35)
- Actual: Down 40%

**Excess decline:** Credit fears, distribution cuts

**Basis:** -20% (MLPs oversold)

**2016-2017 recovery:**
- Oil: Flat to up slightly
- MLPs: +40-60% (catching up)
- **Basis trade: Very profitable for patient investors**

### 4. Tesla Convertible (2013-2014)


**Convert premium collapse:**

**2013:**
- Convert bond: $1,200 (huge premium)
- Stock: $180
- Conversion ratio: 3.54
- Parity: $637
- **Premium: 88%** (extremely rich)

**2014:**
- Stock: $180 → $250 (+39%)
- Convert: $1,200 → $1,000 (-17%)
- Parity: $885
- **Premium: 13%** (normalized)

**Basis trade:** Short convert, long stock = Very profitable

---

## Practical Steps


### 1. Identify Linkage


**Economic relationship:**

- Equity-credit: Same company
- Commodity-equity: Cost pass-through
- FX-rates: Interest rate parity
- Dividend-rates: Discount cash flows

**Verify with data:**
- Historical correlation
- Regression (beta estimation)
- Cointegration test

### 2. Calculate Fair Value


**Theoretical spread:**

$$
\text{Fair Spread} = f(\text{Model Parameters})
$$

**Examples:**
- Merton model for equity-credit
- Beta for commodity-equity
- CIP for FX-rates

### 3. Measure Basis


**Actual vs theoretical:**

$$
\text{Basis} = \text{Actual Spread} - \text{Fair Value Spread}
$$

**Percentile ranking:**
- Compare to historical distribution
- Trade if in top/bottom 10%

### 4. Assess Costs


**All-in costs:**

- Transaction costs (bid-ask, commissions)
- Financing costs (borrow rates)
- Hedge costs (options, futures)

**Breakeven:**

$$
\text{Basis} > \text{Total Costs} + \text{Risk Premium}
$$

### 5. Size Position


**Risk-based sizing:**

$$
\text{Size} = \frac{\text{Risk Capital}}{\text{Basis Risk (1σ)}}
$$

**Example:**

Risk capital: $1M
Basis std dev: 20 bps

**Position:** $1M / 0.002 = $5M notional (reasonable)

### 6. Execute Hedges


**Simultaneous execution:**

1. Buy cheap asset
2. Sell expensive asset
3. Both legs in single order flow
4. Verify hedge ratios

### 7. Monitor and Rebalance


**Daily:**
- Mark-to-market
- Correlation check
- Funding cost

**Weekly:**
- Rehedge if delta/beta changed >20%
- Update fair value model

**Monthly:**
- Review thesis
- Stress test
- Decide: Hold, add, or exit

---

## Final Wisdom


> "Cross-asset basis trades are the most intellectually satisfying strategies in finance—they require deep understanding of how different asset classes relate, mathematical models to price fair value, and the patience to wait for convergence. The equity-credit basis embodies the Merton model's elegance: equity and debt are both claims on the same firm value, so their implied default probabilities MUST converge, or you can arbitrage the capital structure. But here's the brutal truth: basis can stay irrational longer than you can stay solvent. The FX basis post-2008 taught an entire generation that 'no-arbitrage relationships' can be violated persistently when structural forces (regulatory capital, balance sheet constraints) dominate. Deutsche Bank's equity-credit basis in 2016 was a 20% dislocation that reversed in three months—classic mean reversion. But Energy MLPs' basis in 2015 took two years to normalize, and many funds didn't survive. The deepest insight: basis trades require three things most investors lack: (1) understanding of cross-asset linkages beyond correlations, (2) patience to wait for convergence without margin calls, and (3) dry powder to add when basis widens (the 'widening before narrowing' curse). Every basis trade is a bet on two things: (1) the relationship is real and will reassert, and (2) you have enough time and capital to survive the path. The commodity-equity basis killed funds in 2015 not because the relationship broke permanently, but because beta shifted from 0.5 to 0.7 and margin calls forced liquidation. Risk management is paramount: size at 10-15% per trade, diversify across basis types, use options for tail risk, and always ask 'why is this basis here?'—if you can't answer, it might be structural, not temporary. The greatest basis trades come when markets panic and throw out correlations (2008, 2020)—that's when 20-50% dislocations appear and patient capital wins."

**Key to success:**

- Understand WHY basis exists (temporary vs structural)
- Model fair value rigorously (Merton, beta, CIP)
- Size conservatively (10-15% per trade maximum)
- Monitor correlation continuously (exit if breaks)
- Account for ALL costs (funding critical)
- Use leverage cautiously (2-3× max)
- Have patience for convergence (months to years)
- Diversify across basis types (equity-credit, commodity-equity, FX-rates)
