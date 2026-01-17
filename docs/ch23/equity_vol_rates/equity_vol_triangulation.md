# Equity vs Volatility Triangulation


**Equity vs volatility triangulation** exploits the asymmetric inverse relationship where equity declines strongly predict volatility spikes (correlation ≈ -0.7) but equity rallies only weakly predict volatility declines (correlation ≈ -0.3), creating structural opportunities through VIX futures, variance swaps, volatility ETPs, and dispersion trades that profit from the volatility risk premium, mean reversion patterns, and the leverage effect where falling stock prices mechanically increase equity volatility through higher debt-to-equity ratios.

> **Prerequisites:** This section builds on implied volatility and VIX construction (Chapter 7), variance swaps (Chapter 24), and stochastic volatility models (Chapter 9: Heston). See Chapter 6 for Greeks mechanics used in hedging strategies.

---

## The Core Insight


**The fundamental idea:**

- Equity and volatility inversely correlated (not perfectly)
- Relationship asymmetric: Crashes spike vol more than rallies crush it
- VIX = "fear gauge" (market's expectation of 30-day S&P 500 volatility)
- Triangulation: Trade relative value between equity, vol, and derivatives
- Structural risk premium: Implied vol > Realized vol (on average)
- Mean reversion: Both equity and vol revert to long-term averages
- Leverage effect: Falling equity → Rising vol (mechanical)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/equity_vol_relationship.png?raw=true" alt="equity_vol_relationship" width="700">
</p>
**Figure 1:** Scatter plot of S&P 500 daily returns vs. VIX changes showing asymmetric inverse relationship where down days exhibit tight negative correlation (-0.7) with large VIX spikes, while up days show weaker positive correlation with modest VIX declines, illustrating the leverage effect and fear-driven volatility dynamics.

**You're essentially asking: "How do I trade the relationship between stock prices and their volatility?"**

---

## What Is the Equity-Vol Relationship?


### 1. The VIX Definition


**Chicago Board Options Exchange Volatility Index:**

$$
\text{VIX} = 100 \times \sqrt{\frac{252}{T} \sum_{i} \frac{\Delta K_i}{K_i^2} e^{rT} Q(K_i)}
$$

Where:
- $T$ = Time to expiration (30 days)
- $K_i$ = Strike prices
- $Q(K_i)$ = Option mid-quote (puts below forward, calls above)
- $\Delta K_i$ = Strike spacing

**Economic interpretation:**

VIX represents the 30-day expected volatility of S&P 500 implied by option prices

**Units:** Annualized percentage (e.g., VIX = 20 means expected 20% annual volatility)

**Example:**

- VIX = 15: Low volatility (calm market)
- VIX = 25: Elevated volatility (uncertain)
- VIX = 40: High volatility (crisis)
- VIX = 80: Extreme volatility (2008, 2020)

**Historical averages:**
- Long-term average: ~19
- 25th percentile: ~14
- 75th percentile: ~23
- Max (2008): 89.5

### 2. Correlation Structure


**Asymmetric relationship:**

**Downside correlation (S&P down):**

$$
\rho_{\text{down}} = \text{Corr}(\Delta \text{SPX}, \Delta \text{VIX} \,|\, \Delta \text{SPX} < 0) \approx -0.7
$$

**Upside correlation (S&P up):**

$$
\rho_{\text{up}} = \text{Corr}(\Delta \text{SPX}, \Delta \text{VIX} \,|\, \Delta \text{SPX} > 0) \approx -0.3
$$

**Why asymmetric?**

1. **Fear asymmetry:** Losses hurt more than gains feel good (prospect theory)
2. **Leverage effect:** Falling equity → Higher debt/equity → More volatile
3. **Put demand:** Downside protection demand spikes in crashes
4. **Convexity:** Volatility has floor (can't go negative) but no ceiling

**Example:**

- S&P falls 3% → VIX rises 15% (5:1 ratio)
- S&P rises 3% → VIX falls 6% (2:1 ratio)

**Implication:** Long vol has positive skew (captures crashes)

### 3. Realized vs Implied


**Realized volatility (what actually happens):**

$$
\sigma_{\text{realized}} = \sqrt{\frac{252}{n} \sum_{i=1}^{n} r_i^2}
$$

Using daily returns over period

**Implied volatility (what market expects):**

$$
\sigma_{\text{implied}} = \text{VIX} / 100
$$

From option prices

**Volatility risk premium:**

$$
\text{VRP} = \sigma_{\text{implied}} - \sigma_{\text{realized}}
$$

**Historical:** VRP ≈ 3-5% (implied > realized)

**Example:**

- VIX: 20% (implied)
- Realized vol: 16% (actual)
- **VRP: 4%** (premium for selling volatility)

**Economic interpretation:**
- Investors overpay for volatility protection
- Structural excess demand for puts
- Compensation for tail risk
- Basis for vol selling strategies

### 4. VIX Futures


**Cash-settled futures on VIX:**

**Pricing relationship:**

$$
F_{\text{VIX}} = E[\text{VIX}_T] + \text{Risk Premium}
$$

**Contango (normal):**
- VIX futures > VIX spot
- Front month: 18, 2nd month: 20, 3rd month: 21
- Upward sloping term structure

**Backwardation (crisis):**
- VIX futures < VIX spot  
- Front month: 35, 2nd month: 32, 3rd month: 28
- Downward sloping term structure

**Roll yield:**

**In contango:**
- Short front month, long back month
- Collect premium as futures converge
- **Positive roll yield**

**In backwardation:**
- Long front month, short back month
- Pay premium as futures diverge
- **Negative roll yield**

**Example:**

VIX spot: 15, front month future: 17

**One month later:**
- VIX spot still: 15
- Front month (now expiring): 15
- Convergence: 17 → 15
- **Roll decay: 2 points** (11.8% loss if long)

### 5. Variance Swaps


**Pure volatility exposure:**

**Payoff:**

$$
\text{Payoff} = N \times (\sigma_{\text{realized}}^2 - \sigma_{\text{strike}}^2)
$$

Where:
- $N$ = Notional (typically $1M variance)
- $\sigma_{\text{realized}}$ = Actual realized volatility
- $\sigma_{\text{strike}}$ = Strike (agreed variance level)

**Example:**

- Strike: 20% (variance = 400)
- Notional: $100 per variance point ($40K notional)
- Realized: 25% (variance = 625)
- **Payoff:** $(625 - 400) \times 100 = $22,500$

**Advantages:**
- Linear in variance (no path dependency)
- No gamma bleed (unlike options)
- Pure volatility exposure

**Disadvantages:**
- OTC (illiquid, counterparty risk)
- Convexity (squared relationship)
- Gap risk (jumps hurt sellers badly)

### 6. Leverage Effect


**Mechanical relationship:**

**Equity value:**
$$
E = V - D
$$

Where $V$ = Firm value, $D$ = Debt

**Equity volatility (Merton model):**

$$
\sigma_E = \frac{V}{E} N(d_1) \sigma_V
$$

**As equity falls:** $E$ decreases → $V/E$ increases → $\sigma_E$ increases

**Example:**

- Firm value: $V = 100$, Debt: $D = 40$, Equity: $E = 60$
- Firm vol: $\sigma_V = 20\%$
- Equity vol: $\sigma_E = (100/60) \times 0.7 \times 20\% = 23.3\%$

**Equity drops to 40:**
- Leverage: $100/40 = 2.5$ (increased!)
- Equity vol: $(100/40) \times 0.85 \times 20\% = 42.5\%$ (spiked!)

**Mechanical volatility increase from leverage change**

### 7. Term Structure


**VIX futures curve:**

**Normal (contango):**

$$
F_1 < F_2 < F_3 < ... < \text{Long-term mean}
$$

**Example:**
- VIX spot: 14
- 1M future: 16
- 2M future: 17.5
- 3M future: 18.5
- Long-term: 20

**Inverted (backwardation):**

$$
F_1 > F_2 > F_3 > ... > \text{Long-term mean}
$$

**Example (crisis):**
- VIX spot: 45
- 1M future: 38
- 2M future: 33
- 3M future: 30
- Long-term: 20

**Trading implication:**
- Contango: Sell front, buy back (collect roll)
- Backwardation: Buy front, sell back (lose roll)

---

## Key Terminology


**VIX:**
- S&P 500 implied 30-day volatility
- Calculated from option prices
- "Fear gauge" of market
- Mean: ~19, Range: 10-90

**Variance Swap:**
- OTC derivative on realized variance
- Linear payoff in variance
- Pure volatility exposure
- No gamma bleed

**Contango:**
- Futures > Spot
- Normal market state
- Positive roll yield for shorts
- 80% of time historically

**Backwardation:**
- Futures < Spot
- Crisis/fear state
- Negative roll yield for longs
- 20% of time historically

**Volatility Risk Premium:**
- Implied vol > Realized vol
- ~3-5% historically
- Compensation for tail risk
- Basis for vol selling

**Leverage Effect:**
- Falling equity → Rising volatility
- Mechanical from debt/equity
- Amplifies asymmetry
- Discovered by Black (1976)

**Dispersion Trading:**
- Long single-stock vol
- Short index vol
- Exploits correlation
- Mean-reverting

---

## Equity-Vol Strategies


### 1. VIX Call Spreads


**Tail risk protection:**

**Structure:**
- Buy VIX call at 25
- Sell VIX call at 40
- Cost: $2.50 per spread

**Payoff:**

- If VIX < 25: Lose $2.50 (premium)
- If VIX = 30: Profit $(30-25) - 2.50 = 2.50$
- If VIX > 40: Profit $(40-25) - 2.50 = 12.50$ (capped)

**Use case:** Portfolio insurance

**Example:**

- $10M equity portfolio
- Beta = 1.0, so move ~1:1 with S&P
- Buy 100 VIX call spreads (25/40) at $2.50 = $25K

**Crisis scenario: S&P -20%, VIX → 45**
- Portfolio loss: -$2M
- VIX spreads: 100 × $12.50K = $1.25M
- **Net loss: -$775K** (62% hedged)

**Cost:** $25K per quarter (1% annual insurance)

### 2. Short VIX Futures


**Collect roll yield:**

**Strategy:**
- Short front-month VIX futures
- Roll monthly to maintain exposure
- Collect contango decay

**Example:**

VIX at 15, front month at 17

**Each month:**
- Short at 17
- Cover at ~15 (convergence)
- **Profit: 2 points** = $1,000 per contract

**Annual:** 12 months × 2 points = 24 points
- On $1M position: $24K profit (2.4% return)

**Risk:**
- VIX spike (2020: 15 → 85 in 1 month)
- Unlimited losses
- Margin calls

**2018 VIX ETN disaster (XIV):**
- Short VIX strategy
- February 5: VIX doubled (17 → 37)
- XIV: -96% in one day
- **Terminated**

### 3. Equity Protective Puts + Short Vol


**"Collar with yield":**

**Structure:**
1. Own S&P 500 index
2. Buy 10% OTM puts (protection)
3. Sell VIX call spreads (income)

**Example:**

- Portfolio: $10M S&P 500
- Buy puts (90% strike): Cost $100K
- Sell VIX 25/40 call spreads: Collect $80K
- **Net cost: $20K** (0.2% vs. 1% for puts alone)

**Rationale:**
- When equity crashes, VIX spikes
- VIX calls partially offset put cost
- Cheap insurance

### 4. Long Variance Swaps


**Pure volatility bet:**

**Position:** Long 1-year variance swap
- Strike: 18% (variance 324)
- Notional: $100 per variance point

**Scenarios:**

**Low vol year (realized 15%):**
- Variance: 225
- Loss: $(225 - 324) \times 100 = -$9,900$

**Normal year (realized 18%):**
- Variance: 324
- **Break even**

**High vol year (realized 25%):**
- Variance: 625
- Profit: $(625 - 324) \times 100 = +$30,100$

**Skewed payoff:** Small losses most years, large gains in crisis

### 5. Dispersion Trading


**Index vol vs. component vol:**

**Relationship:**

$$
\sigma_{\text{index}}^2 = \sum_{i} w_i^2 \sigma_i^2 + \sum_{i \neq j} w_i w_j \rho_{ij} \sigma_i \sigma_j
$$

**Key insight:** If $\rho \to 0$, index vol << average stock vol

**Strategy:**
- Sell index variance (cheap)
- Buy single-stock variance (expensive)
- Net: Long dispersion

**Example:**

- Sell SPX variance at 18%: Collect $324 per variance point
- Buy AAPL, MSFT, GOOGL, AMZN, META variance at average 25%
- Weighted average: Pay $625 per variance point

**Net:** Pay $301 upfront

**Payoff if correlation drops:**
- Crisis → Correlation spikes → Index vol rises more than expected
- **Dispersion trade loses**

**Payoff if correlation normal:**
- Normal → Stocks diverge → Single-stock vol > index vol
- **Dispersion trade wins**

**Historical:** Long dispersion profitable 60% of years

### 6. VIX ETPs


**Exchange-traded products:**

**Long volatility:**
- VXX (short-term futures)
- VIXY (short-term futures)
- Contango decay: -40% to -70% annually

**Short volatility (now rare after XIV):**
- SVXY (inverse short-term)
- Risk: Unlimited losses in spikes

**Mid-term:**
- VXZ (mid-term futures)
- Less decay (flatter curve)
- Lower sensitivity

**Example—Long VXX:**

**Year 1:** VIX average 15, contango 10%
- Roll loss: -40% (aggressive contango)
- VIX changes: +5%
- **Net: -35%**

**Held 10 years:**
- Decay compounds: $100 → $1 (99% loss!)
- Only profitable in sustained spikes

### 7. Equity Index Options


**Trading vol through options:**

**Strategy: Straddles/Strangles**

Buy 1-month ATM straddle:
- S&P at 4,500
- Call + Put: $180 (4% of spot)
- Breakeven: $180 move (4%)

**Profit if:**
- Realized vol > implied vol
- VIX spikes
- Large unexpected move

**Loss if:**
- Realized vol < implied vol
- Market stays calm
- Theta decay

**Delta-hedge to isolate vol:**
- Hedge delta daily
- Pure volatility P&L
- Gamma scalping strategy

---

## Common Mistakes


### 1. Ignoring Roll Costs


**VIX futures are not VIX:**

- **Mistake:** Buy VXX thinking it tracks VIX
- **Why it fails:** Futures in contango, massive roll decay
- **Fix:** Understand term structure before trading
- **Real cost:** -40% to -70% annually in contango

**Example:**

- VIX stays at 15 entire year (flat)
- VXX: -55% (roll decay)
- Investor: "How did I lose money if VIX didn't move?!"

### 2. Leverage on Short Vol


**Amplifying tail risk:**

- **Mistake:** Lever short VIX 3× thinking "easy money"
- **Why it fails:** One spike wipes out years of gains
- **Fix:** Never lever short volatility
- **Real cost:** Total loss (see XIV 2018)

**Example:**

2017: VIX low, short VIX earning 20% monthly
- Lever 3×: Earning 60% monthly (!)
- February 2018: VIX doubles
- 3× loss: -180% (wipeout + debt)

### 3. Correlation Timing


**Dispersion trade gone wrong:**

- **Mistake:** Long dispersion assuming correlation will drop
- **Why it fails:** Correlation spikes in crisis
- **Fix:** Size conservatively, hedge tail risk
- **Real cost:** -30% to -50% in crisis months

**Example:**

2008: Dispersion trade popular
- Long single-stock vol, short index vol
- October 2008: Correlation → 0.95
- All stocks fell together
- Single-stock vol < index vol (opposite of expected)
- **Massive losses**

### 4. Convexity Confusion


**Linear vs. squared:**

- **Mistake:** Think variance swap like volatility
- **Why it fails:** Variance is squared (convex)
- **Fix:** Understand convexity risk
- **Real cost:** Gap losses 2-3× expected

**Example:**

Variance swap strike: 20% (variance 400)
- Small move (realized 22%): Variance 484, gain $84
- Large move (realized 30%): Variance 900, gain $500

**Convexity:** 10% vol move gives 6× the payoff of 2% move

### 5. Ignoring Gamma


**Buying vol without hedging:**

- **Mistake:** Buy options for vol exposure, don't hedge delta
- **Why it fails:** Directional risk swamps vol P&L
- **Fix:** Delta-hedge to isolate volatility
- **Real cost:** "Volatility" bet becomes stock bet

**Example:**

Buy straddle for vol exposure
- S&P rallies 10%
- Realized vol = 18% (as expected)
- But call gains > put losses (directional)
- **Made money from direction, not vol**

### 6. Term Structure Misread


**Wrong tenor hedges:**

- **Mistake:** Buy 1-month VIX futures to hedge 12-month equity risk
- **Why it fails:** Short-term vol mean-reverts fast
- **Fix:** Match hedge tenor to risk horizon
- **Real cost:** Hedge expires before risk materializes

**Example:**

Worried about 2024 election (12 months away)
- Buy 1-month VIX futures
- Expire before election
- Election spike: Unhedged
- **Wasted hedge cost**

### 7. Dividend Ignorance


**Forgetting dividend drag:**

- **Mistake:** Compare VIX (price vol) to equity returns (total return)
- **Why it fails:** S&P dividends ~2%, lowers price volatility
- **Fix:** Adjust for dividends in calculations
- **Real cost:** 2-3% underestimate of effective hedge

---

## Best vs. Worst Case


### 1. Best Case: Success


**VIX call spreads hedge 2020:**

**Setup (December 2019):**
- Portfolio: $50M equity (beta = 1.0)
- Concerned about China virus rumors
- Buy VIX call spreads (20/35) for Q1 2020
- Cost: $5 per spread × 1,000 = $500K (1% of portfolio)

**January-February 2020:**
- Market uneasy but holding up
- S&P: 3,200-3,400 (range-bound)
- VIX: 12-18 (elevated but not crisis)

**March 2020: COVID crash**

**Week 1 (March 9-13):**
- S&P: 3,000 → 2,700 (-10%)
- VIX: 20 → 55 (275% spike!)

**Week 2 (March 16-20):**
- S&P: 2,700 → 2,300 (-15% more)
- VIX: 55 → 82 (peak)

**Portfolio impact:**

**Without hedge:**
- Equity: $50M × -30% = **-$15M**

**With hedge:**
- Equity loss: -$15M
- VIX spreads: 1,000 × $(35-20) \times 1000 = $15M
- Spread cost: -$500K
- **Net: -$500K** (just the premium!)

**Hedge effectiveness: 97%**

**Q2-Q4 2020: Recovery**
- S&P recovered to 3,600 (new high)
- Portfolio: Back to $50M
- **Total return: -1%** (vs. -30% unhedged then +43% = +0% net)

**Success factors:**
1. Bought hedge before crisis (timing)
2. Correct tenor (quarterly, matched risk)
3. Reasonable strikes (20/35, not 30/45)
4. Sized appropriately (1% cost)
5. Held through panic (didn't sell at bottom)

### 2. Worst Case: Disaster


**Short VIX catastrophe (XIV 2018):**

**Setup:**
- XIV: Short VIX ETN (2× leveraged)
- Strategy: Short front-month VIX futures
- 2012-2017: Compounded at 80%+ annually
- Peak AUM: $2B

**Investor profile:**
- Retail investors chasing performance
- Algorithmic traders (momentum)
- Leverage: Built-in 2×

**2017: Glory year**
- VIX: 9-15 (historic lows)
- Contango: Steep (futures 20-30% above spot)
- XIV: +187% (incredible!)
- Investors euphoric

**January 2018:**
- Market complacent (VIX ~10)
- XIV at all-time high: $146
- Investors fully levered

**February 5, 2018: Volmageddon**

**Intraday timeline:**

**9:30 AM:** Normal open
- S&P: 2,700
- VIX: 17 (slightly elevated)
- XIV: $99 (down from $146 but still high)

**2:00 PM:** Selling accelerates
- S&P: -2%
- VIX: 25 (spike!)
- XIV: $70 (down 30%)

**3:00 PM:** Panic
- S&P: -3.5%
- VIX: 35 (doubled!)
- XIV: $30 (down 70%)

**After hours:** Liquidation spiral
- VIX futures: Short covering by XIV
- VIX: 37 peak
- XIV: $5.50 (down 96% in one day!)

**Next day:** Termination event
- Credit Suisse invoked termination clause
- XIV settled at $4.22
- **Investors lost 96-99%** (depending on entry)

**Losses:**
- Peak AUM: $2B
- Final value: $100M
- **Investor losses: $1.9B**

**Individual disasters:**

**Case 1: Retirement account**
- Invested $500K at $140 (thought "safe" after 6 years)
- Final value: $15K
- **Lost 97%** of life savings

**Case 2: Leveraged long**
- Bought $200K on margin (2× personal leverage)
- Total exposure: $400K on $200K capital
- Loss: $388K
- **Owed broker $188K** (more than original capital)

**Case 3: Algorithmic fund**
- $50M in XIV (momentum strategy)
- Losses: $48M
- **Fund shut down**

**Root causes:**
1. Leverage (2× built-in)
2. Tail risk ignored (worked for 6 years)
3. Crowd trade (forced unwinding)
4. Mechanical (no circuit breakers)
5. Termination clause (not understood by retail)

---

## Risk Management Rules


### 1. VIX Position Limits


**Maximum short VIX:**

$$
\text{Short VIX Notional} \leq 5\% \text{ of Capital}
$$

**Never lever short volatility** (no 2×, 3×, etc.)

### 2. Stress Testing


**Required scenarios:**

1. VIX doubles (e.g., 15 → 30)
2. VIX triples (e.g., 15 → 45)
3. VIX to 80 (2008/2020 level)

**Maximum loss in worst scenario:**

$$
\text{Stress Loss} \leq 20\% \text{ of Capital}
$$

### 3. Contango Monitoring


**Exit if term structure inverts:**

$$
\text{If } F_1 < \text{VIX Spot}, \text{ then exit short vol}
$$

**Example:**

Short VIX futures, front month at 17, spot at 15 (contango = okay)

**One week later:** Front month 22, spot 25 (backwardation!)
- **Exit immediately** (warning signal)

### 4. Correlation Limits


**For dispersion trades:**

$$
\text{Max Position Size} = f(\rho)
$$

**If $\rho < 0.5$:** Max 10% of capital
**If $\rho > 0.7$:** Max 2% of capital
**If $\rho > 0.85$:** Exit trade

### 5. Roll Schedule


**VIX futures:**

- Roll 5-7 days before expiration
- Never hold to delivery
- Monitor convergence daily

**VIX ETPs:**

- Understand roll schedule (daily for VXX)
- Calculate expected decay
- Set maximum hold period (1-3 months)

### 6. Hedge Ratios


**For equity portfolios:**

**VIX call notional:**

$$
N_{\text{VIX}} = \frac{\text{Equity Notional} \times \beta}{3000}
$$

**Example:**

- $10M equity portfolio, beta = 1.2
- VIX calls: $(10M \times 1.2) / 3000 = 4,000$ contracts

**Rationale:** $3000 hedge ratio is empirical (VIX vs. S&P move ratio)

### 7. Variance Swap Limits


**Maximum variance notional:**

$$
\text{Variance Notional} \leq 2\% \text{ of Capital}
$$

**Example:**

$100M fund

**Maximum:** $2M variance notional
- If strike 20% (variance 400): Max 5,000 variance points ($400 each)

---

## Real-World Examples


### 1. Volmageddon (February 5, 2018)


Described in detail in Worst Case above.

**Key lesson:** Short volatility works until it doesn't (tail risk)

### 2. COVID Crash (March 2020)


**VIX spike:**
- January: VIX ~13 (complacent)
- March 16: VIX 82.7 (record close)
- Move: 6.3× in 6 weeks

**Winners:**
- VIX call buyers: 10-50× returns
- Variance swap longs: 5-10× returns
- Tail hedge funds: +200-400%

**Losers:**
- Short vol strategies: -90%+
- Unhedged equity: -35%
- VXX buyers (late): -60% (bought at 80, rolled down)

### 3. Low Vol Environment


**VIX record lows:**
- Average 2017: VIX ~11
- 52 days below 10 (record)
- Contango: Persistent, steep

**Short vol strategies:**
- XIV: +187%
- Selling VIX futures: +40-60%
- Short variance swaps: +30-50%

**Lulled investors into false security:**
- "VIX can't spike anymore"
- "New regime" (wrong!)
- Set up for 2018 disaster

### 4. Flash Crash / Debt Ceiling


**August 2011:**
- S&P downgrade of US debt
- VIX: 15 → 48 in 10 days
- S&P: -18% peak-to-trough

**Dispersion trades:**
- Index vol spiked more than single-stock
- Correlation: 0.5 → 0.9
- Long dispersion: -20 to -30%

**Recovery:**
- September: VIX back to 30
- October: VIX back to 25
- Mean reversion

---

## Practical Steps


### 1. Measure Relationship


**Historical correlation:**

$$
\rho = \text{Corr}(\Delta \text{SPX}, \Delta \text{VIX})
$$

**Compute over:**
- 1 month (recent)
- 1 year (medium-term)
- 5 years (long-term)

**Current (2025):** $\rho \approx -0.65$ (1-year)

### 2. Evaluate Risk Premium


**Implied vs. realized:**

$$
\text{VRP} = \text{VIX} - \sigma_{\text{realized, 30-day forward}}
$$

**If VRP > 4%:** Vol expensive (favor selling)
**If VRP < 2%:** Vol cheap (favor buying)

### 3. Check Term Structure


**VIX futures curve:**

**Contango %:**

$$
\text{Contango} = \frac{F_2 - F_1}{F_1} \times 100\%
$$

**If > 10%:** Steep contango (sell front, buy back)
**If < 0%:** Backwardation (avoid short vol)

### 4. Size Position


**For tail hedges:**

$$
\text{Notional} = \text{Portfolio} \times \text{Beta} \times \text{Desired Hedge \%} / 30
$$

**Example:**

- $20M portfolio, beta 1.1, want 50% hedge
- Notional: $20M × 1.1 × 0.5 / 30 = $367K in VIX calls

### 5. Monitor Greeks


**For options:**

- Delta: Hedge daily if isolating vol
- Vega: Track exposure (1% VIX = X P&L)
- Theta: Decay cost per day
- Gamma: Rehedge needs

### 6. Rebalance


**Frequency:**
- VIX futures: Monthly (roll schedule)
- Options: Weekly (theta/gamma)
- Variance swaps: Quarterly (mark-to-market)

### 7. Attribution


**Decompose P&L:**

$$
\text{P&L} = \text{Equity P&L} + \text{Vol P&L} + \text{Interaction}
$$

**Example:**

Monthly return: +2%

**Attribution:**
- Equity: +3%
- Vol (short): -0.5% (VIX rose)
- Interaction: -0.5% (negative correlation helped)
- **Total: 2%**

---

## Final Wisdom


> "The equity-volatility relationship is Wall Street's most reliable pattern and most dangerous trap. Reliable: equity crashes predict VIX spikes with -0.7 correlation, creating the structural foundation for tail hedging and volatility trading. Dangerous: the asymmetry and convexity mean 'selling volatility' earns steady profits until one catastrophic loss wipes out years of gains—the financial equivalent of picking up pennies in front of a steamroller. The VIX is not tradeable directly (it's an index), so you're always trading futures (with roll costs), options (with Greeks), or variance swaps (with convexity). Each vehicle has different exposures, different decay rates, and different tail risks. The 2018 XIV disaster crystallized the core lesson: short volatility works 95% of the time, producing steady 20-40% annual returns, then loses 90%+ in a single day during the other 5% (February 5, 2018). Leverage amplifies this pattern: 2× leverage turns a 50% VIX spike into a 100% loss, triggering termination clauses and forced liquidation spirals. The structural volatility risk premium (implied > realized) is real—about 3-5% annually—but it's compensation for bearing tail risk, not free money. Triangulation means understanding: (1) equity direction sets volatility level, (2) volatility level affects option prices, (3) option prices determine hedge costs, (4) hedge costs affect equity returns. It's a closed loop where each affects the others. Best practices: never lever short vol, size tail hedges at 1-2% of portfolio, match hedge tenor to risk horizon, understand roll costs before trading VIX futures, and remember that 'works until it doesn't' is not a risk management plan—it's a recipe for disaster."

**Key to success:**

- Understand asymmetry (crashes spike vol more than rallies crush it)
- Never lever short volatility (1× max, preferably 0.5×)
- Match hedge tenor to risk horizon (3-month risk = 3-month hedge)
- Account for roll costs (VXX loses 40-70% annually in contango)
- Size for tail events (stress test to VIX = 80)
- Monitor term structure (backwardation = warning signal)
- Use spread strategies (cap tail risk with VIX call spreads)
- Remember convexity (variance is squared, not linear)
