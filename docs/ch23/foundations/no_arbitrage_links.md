# No-Arbitrage Links Across Markets


**No-arbitrage links across markets** are the fundamental price relationships that must hold between different asset classes—equities, bonds, currencies, commodities—enforced by arbitrageurs who exploit any deviations, creating a web of interconnected valuations where covered interest parity links FX forwards to interest rates, put-call parity connects options across strikes, commodity storage costs determine futures prices, and quanto adjustments tie foreign assets to domestic currency, making cross-asset arbitrage the invisible force that maintains global market consistency.

> **Prerequisites:** This section assumes familiarity with option pricing fundamentals (Chapter 5: Black-Scholes), Greeks and hedging mechanics (Chapter 6), and implied volatility concepts (Chapter 7).

---

## The Core Insight


**The fundamental idea:**

- Markets don't exist in isolation
- Price relationships must be internally consistent
- Arbitrage enforces consistency across markets
- If relationship breaks → Free money (briefly)
- Arbitrageurs rush in → Prices converge
- Links create predictable patterns across assets
- Understanding links = understanding market structure

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/cross_asset_arbitrage_web.png?raw=true" alt="cross_asset_arbitrage_web" width="700">
</p>
**Figure 1:** Web of no-arbitrage relationships connecting equities, bonds, FX, and commodities through covered interest parity (FX-rates), put-call parity (equity-options), cost-of-carry (spot-futures), dividend arbitrage (stock-futures), and quanto relationships (foreign assets), showing how violations in any link create arbitrage opportunities that force convergence.

**You're essentially asking: "What price relationships MUST hold, or free money appears?"**

---

## What Are No-Arbitrage Links?


### 1. The Law of One Price


**Fundamental principle:**

Identical assets must trade at the same price (adjusted for transaction costs)

**Formal statement:**

If asset A and asset B provide identical cash flows in all states, then:

$$
P_A = P_B
$$

Otherwise: Buy cheap, sell expensive, lock in risk-free profit

**Example:**

Apple stock trades on:
- NYSE: $180.00
- London Stock Exchange (LSE): £141.00
- FX rate: USD/GBP = 1.2766

**Check arbitrage:**

LSE price in USD: £141 × 1.2766 = $180.00 ✓

**If LSE quoted £140:**
- Buy in London: £140 = $178.70
- Sell in New York: $180.00
- **Profit: $1.30 per share** (73 bps)

**Arbitrage action:** Buy London, sell NY → Prices converge

### 2. Covered Interest Parity


**FX forward pricing:**

The fundamental link between FX rates and interest rates

$$
F = S_0 \times \frac{1 + r_d}{1 + r_f}
$$

Or in continuous time:
$$
F = S_0 e^{(r_d - r_f)T}
$$

Where:
- $F$ = Forward FX rate
- $S_0$ = Spot FX rate
- $r_d$ = Domestic interest rate
- $r_f$ = Foreign interest rate
- $T$ = Time to maturity

**Economic intuition:**

**Strategy 1: Invest domestically**
- Invest $1 at rate $r_d$
- Get $(1 + r_d)$ after time $T$

**Strategy 2: Invest abroad**
- Convert $1 to foreign currency: $1/S_0$ units
- Invest at $r_f$: $(1/S_0)(1 + r_f)$
- Lock in forward to convert back: $(1/S_0)(1 + r_f) \times F$

**No-arbitrage:** Both strategies must yield same return

$$
1 + r_d = \frac{1}{S_0}(1 + r_f) \times F
$$

Rearranging:
$$
F = S_0 \times \frac{1 + r_d}{1 + r_f}
$$

**Example:**

- EUR/USD spot: $S_0 = 1.0800$
- USD rate: $r_d = 5.5\%$ (1 year)
- EUR rate: $r_f = 3.5\%$

**Forward price:**
$$
F = 1.0800 \times \frac{1.055}{1.035} = 1.0800 \times 1.0193 = 1.1009
$$

**Market quotes forward at 1.1050:**
- Arbitrage! Forward too expensive

**Strategy:**
1. Borrow EUR 1M at 3.5%
2. Convert to USD at 1.0800: Get $1.08M
3. Invest in USD at 5.5%
4. Sell forward at 1.1050

**Cash flows:**

**Today (T=0):**
- Borrow: €1M
- Convert: +$1.08M
- Invest: -$1.08M
- Net: €0, $0

**One year (T=1):**
- EUR investment: €1M × 1.035 = €1.035M
- Sell EUR at forward: €1.035M × 1.1050 = **$1.1437M**
- Repay USD loan: $1.08M × 1.055 = **$1.1394M**
- **Profit: $1.1437M − $1.1394M = $4.3K** (40 bps)

**Why this works:**

The forward rate (1.1050) implies EUR appreciation relative to what CIP predicts. The fair forward under CIP would be:

$$
F_{\text{CIP}} = 1.08 \times \frac{1.035}{1.055} = 1.0598
$$

Since market forward (1.1050) > CIP fair value (1.0598), the EUR is overpriced in the forward market. Arbitrageurs:
- Borrow the currency that's cheap to borrow (USD at 5.5%)
- Invest in the currency with lower rates (EUR at 3.5%)
- Lock in favorable forward sale of EUR

The 40 bps profit represents the mispricing between the forward market and interest rate differential.

### 3. Put-Call Parity


**Link between calls, puts, stock, and bond:**

$$
C - P = S_0 - K e^{-rT}
$$

Or equivalently:
$$
C + K e^{-rT} = P + S_0
$$

**Economic intuition:**

**Portfolio A:** Long call + Cash (PV of strike)
**Portfolio B:** Long put + Stock

Both portfolios have identical payoff at expiration:
- If $S_T > K$: Call worth $S_T - K$, put worthless, stock worth $S_T$, cash worth $K$
  - Portfolio A: $(S_T - K) + K = S_T$
  - Portfolio B: $0 + S_T = S_T$ ✓

- If $S_T < K$: Call worthless, put worth $K - S_T$, stock worth $S_T$, cash worth $K$
  - Portfolio A: $0 + K = K$
  - Portfolio B: $(K - S_T) + S_T = K$ ✓

**No-arbitrage:** Equal payoffs → Equal prices

**Example:**

- Stock: $S_0 = 100$
- Strike: $K = 100$
- Rate: $r = 5\%$
- Time: $T = 1$ year
- Call: $C = 10$
- Put: $P = ?$

**From put-call parity:**
$$
P = C - S_0 + K e^{-rT} = 10 - 100 + 100 \times e^{-0.05} = 10 - 100 + 95.12 = 5.12
$$

**If market quotes put at $P = 6$:**
- Arbitrage! Put too expensive

**Strategy:**
1. Sell put: +$6
2. Buy call: -$10
3. Sell stock: +$100
4. Invest proceeds: +$100 at 5%

**Cash flows:**

**Arbitrage (put overpriced at $6 vs. fair value $5.12):**

The strategy exploits put-call parity by constructing a synthetic put and comparing to the market put.

**Synthetic put:** Short stock + Long call + Lend PV(K) = Put
- Cost: $-100 + 10 + 95.12 = 5.12$

**Market put:** $6

**Strategy:** Sell market put (+$6), buy synthetic put (−$5.12)
- **Riskless profit: $0.88 per share**

**Verification at expiration:**

| Stock Price $S_T$ | Sold Put Payoff | Long Call Payoff | Stock Position | Bond Matures | Net |
|-------------------|-----------------|------------------|----------------|--------------|-----|
| $S_T > 100$ (e.g., 120) | $0$ | $+(S_T - 100)$ | $-S_T$ | $+100$ | $0$ |
| $S_T < 100$ (e.g., 80) | $-(100 - S_T)$ | $0$ | $-S_T$ | $+100$ | $0$ |

In both cases, the portfolio has zero terminal value. Since we collected $0.88 upfront, this is a riskless arbitrage profit.

### 4. Cost of Carry


**Link between spot and futures:**

$$
F = S_0 e^{(r + u - y)T}
$$

Where:
- $r$ = Risk-free rate
- $u$ = Storage cost (for commodities)
- $y$ = Convenience yield or dividend yield

**Economic intuition:**

**Strategy 1: Buy futures**
- Pay $F$ at maturity
- Get commodity

**Strategy 2: Buy spot + carry**
- Buy spot: $S_0$
- Finance at $r$: $S_0 e^{rT}$
- Storage cost: $S_0 e^{uT}$
- Collect dividend/yield: $-S_0 e^{yT}$
- Total: $S_0 e^{(r+u-y)T}$

**No-arbitrage:** $F = S_0 e^{(r+u-y)T}$

**Example—Stock index futures:**

- S&P 500 spot: 4,500
- Dividend yield: 2%
- Interest rate: 5%
- Time: 3 months = 0.25 years

$$
F = 4500 \times e^{(0.05 - 0.02) \times 0.25} = 4500 \times e^{0.0075} = 4500 \times 1.0075 = 4,534
$$

**If futures quoted at 4,550:**
- Arbitrage! Futures too expensive

**Strategy (cash-and-carry):**
1. Short futures at 4,550
2. Buy index portfolio at 4,500
3. Hold for 3 months (collect dividends)

**Cash flows:**

**Today:** -$4,500 (buy index)

**3 months:**
- Dividends: $4,500 × 0.02 × 0.25 = $22.50
- Financing cost: $4,500 × 0.05 × 0.25 = $56.25
- Futures settlement: $4,550 (receive)
- Index value: $S_T$ (sell)

**Net:** $4,550 - 4,500 - 56.25 + 22.50 = 16.25$

**Risk-free profit: $16.25** per contract (after financing and dividends)

### 5. Triangular Arbitrage


**FX cross-rate consistency:**

$$
\frac{\text{EUR}}{\text{USD}} \times \frac{\text{USD}}{\text{GBP}} = \frac{\text{EUR}}{\text{GBP}}
$$

**Or in rate notation:**

$$
S_{\text{EUR/GBP}} = \frac{S_{\text{EUR/USD}}}{S_{\text{GBP/USD}}}
$$

**Example:**

- EUR/USD = 1.0800
- GBP/USD = 1.2700
- Implied EUR/GBP = 1.0800 / 1.2700 = **0.8504**

**Market quotes EUR/GBP = 0.8520:**
- Discrepancy: 0.8520 - 0.8504 = **0.0016** (16 pips)
- Arbitrage opportunity!

**Strategy:**

**Path 1: Via direct market**
- Sell EUR 1M for GBP at 0.8520 → Receive £852,000

**Path 2: Via synthetic (two legs)**
- Sell EUR 1M for USD at 1.0800 → Receive $1,080,000
- Sell $1,080,000 for GBP at 1.2700 → Receive £850,394

**Difference:** £852,000 - £850,394 = **£1,606 profit**

**Arbitrage action:**
1. Buy EUR with GBP in direct market (0.8520)
2. Sell EUR for USD (1.0800)
3. Sell USD for GBP (1.2700)
4. Net: Start with £X, end with £(X + profit)

### 6. Quanto Adjustments


**Link between foreign assets and domestic currency:**

**Quanto call on foreign stock (S) payable in domestic currency:**

$$
C_{\text{quanto}} = S_0 e^{-r_f T} N(d_1) - K e^{-r_d T} N(d_2)
$$

Where:
$$
d_1 = \frac{\ln(S_0/K) + (r_d - r_f + \rho \sigma_S \sigma_{FX})T + \sigma^2 T/2}{\sigma\sqrt{T}}
$$

**Key adjustment:** $\rho \sigma_S \sigma_{FX}$ term

**Economic intuition:**

- Quanto removes FX risk (pays in domestic currency)
- But correlation between asset and FX matters
- If stock rises when domestic currency strengthens: Positive correlation → Higher quanto value
- Vice versa for negative correlation

**Example:**

- Japanese stock at ¥10,000
- Strike: ¥10,000
- Quanto call pays in USD (not JPY)
- Correlation (Nikkei vs. USD/JPY): ρ = -0.6
- Stock vol: σ_S = 25%
- FX vol: σ_FX = 12%

**Quanto adjustment:**
$$
\text{Adjustment} = \rho \sigma_S \sigma_{FX} = -0.6 \times 0.25 \times 0.12 = -0.018 = -1.8\%
$$

**Impact:** Quanto call worth **less** than standard call (negative correlation)

### 7. Commodity Arbitrage


**Storage and convenience yield:**

$$
F = S_0 e^{(r + u - c)T}
$$

Where:
- $u$ = Storage cost
- $c$ = Convenience yield (benefit of holding physical)

**Convenience yield:** Implicit benefit of having commodity on hand
- High when supply tight (backwardation)
- Low when supply ample (contango)

**Example—Crude oil:**

- Spot: $80/barrel
- Storage: $2/barrel/year (2.5%)
- Interest rate: 5%
- 1-year forward: $F = ?$

**No convenience yield:**
$$
F = 80 \times e^{(0.05 + 0.025) \times 1} = 80 \times e^{0.075} = 80 \times 1.0779 = 86.23
$$

**If market quotes $85:**
- Implies convenience yield: $c = 1.5\%$
- Market expects some supply tightness

**Arbitrage limits:**

- Storage capacity constraints (can't store infinite oil)
- Physical delivery costs (basis risk)
- Seasonality (natural gas heating season)

---

## Key Terminology


**Covered Interest Parity:**
- FX forward equals spot adjusted for rate differential
- Core link between FX and rates
- Violation = covered arbitrage opportunity
- Typically holds within transaction costs

**Put-Call Parity:**
- Relationship between call, put, stock, cash
- European options only (American more complex)
- Synthetic positions from parity
- Conversion and reversal arbitrage

**Cost of Carry:**
- Futures price equals spot plus carry costs
- Includes financing, storage, dividends
- Basis = Future - Spot
- Cash-and-carry arbitrage

**Triangular Arbitrage:**
- FX cross-rate consistency
- Three-way exchange must net to starting point
- High-frequency strategy
- Milliseconds execution required

**Quanto:**
- Foreign asset with domestic currency payoff
- Removes FX risk
- Correlation adjustment required
- Common in equity derivatives

**Convenience Yield:**
- Implicit benefit of holding physical
- High when supply tight (backwardation)
- Low when supply ample (contango)
- Cannot be observed directly

---

## Cross-Asset Arbitrage Strategies


### 1. Index Arbitrage


**ETF vs. underlying basket:**

**Strategy:** Exploit temporary mispricing between ETF and constituents

**Example—SPY vs. S&P 500 basket:**

- SPY (ETF): $450.00 per share
- S&P 500 fair value: $450.15 (sum of constituents)
- **Discount: 15¢** (3.3 bps)

**If discount > transaction costs:**

**Action:**
1. Buy SPY shares: $450.00 × 10,000 = $4.5M
2. Short S&P 500 basket: $450.15 equivalent
3. Wait for convergence

**Profit:** $0.15 × 10,000 = **$1,500**

**Timing:** Usually converges within hours (intraday arb)

**Risks:**
- Tracking error (ETF not perfect replica)
- Dividend timing (ETF vs. stocks)
- Borrowing cost (short basket)
- Execution slippage (500 stocks)

### 2. Convertible Arbitrage


**Convert bond vs. stock + bond:**

**Example:**

- Convert bond: $1,050
- Conversion ratio: 10 shares per bond
- Stock price: $95
- Conversion value: 10 × $95 = $950
- Bond floor: $900 (straight bond value)

**Convert trades at premium:** $1,050 - $950 = $100 (10.5%)

**Strategy:**

1. Buy convert: $1,050
2. Short stock: 10 shares at $95 = $950
3. Net investment: $100

**Scenarios:**

**Stock rises to $110:**
- Convert value: 10 × $110 = $1,100
- Short loss: -10 × ($110 - $95) = -$150
- Convert now worth: $1,100
- **Net: $1,100 - $150 - $1,050 = -$100** (break even)

**Stock falls to $80:**
- Convert value: Max($800, $900) = $900 (bond floor)
- Short gain: 10 × ($95 - $80) = +$150
- **Net: $900 + $150 - $1,050 = $0** (break even)

**Profit from:**
- Coupon income (4-5% typically)
- Gamma trading (rehedge as stock moves)
- Credit spread tightening

### 3. Capital Structure Arbitrage


**Equity vs. debt of same company:**

**Example:**

- Company XYZ
- Stock: $50
- 5-year CDS: 300 bps
- Implied default probability: ~15%

**Check consistency:**

If stock worth $50, equity has value → Company unlikely to default
But CDS at 300 bps suggests 15% default risk over 5 years
**Inconsistency!**

**Two possibilities:**

**Scenario A: Stock cheap, CDS rich**
- Buy stock, buy CDS protection
- If stock rallies, CDS tightens: Both profit

**Scenario B: Stock rich, CDS cheap**
- Short stock, sell CDS protection
- If stock falls, CDS widens: Short profits, CDS loses (net depends on magnitude)

**Typical trade (Scenario A):**
- Buy $1M stock
- Buy CDS on $1M notional
- Cost: 300 bps × $1M = $30K per year

**Payoff:**
- If company improves: Stock +20%, CDS tightens 100 bps → Both gain
- If company defaults: Stock → $0, CDS pays $1M → Protected

### 4. Fixed Income Arbitrage


**Treasury vs. futures:**

**CTD (Cheapest-to-Deliver) arbitrage:**

**Example:**

- 10Y Treasury futures: 110-00 ($110,000 per contract)
- CTD bond: 4% coupon, 9.5 years to maturity
- CTD bond price: $97 (for $100 face)
- Conversion factor: 0.88

**Fair futures price:**

$$
F = \frac{\text{CTD Price}}{\text{Conversion Factor}} = \frac{97}{0.88} = 110.23
$$

**Market futures at 110-00 (110.00):**
- Arbitrage: Futures cheap by 0.23

**Strategy:**
1. Buy futures: 110.00
2. Short CTD bond: 97.00
3. Profit at convergence: 0.23 per $100 face

**Risks:**
- CTD may switch (different bond becomes cheapest)
- Basis risk (delivery option value)
- Financing costs

### 5. Volatility Arbitrage


**Options vs. realized volatility:**

**Example:**

- Stock at $100
- 1-month ATM straddle: $8
- Implied vol: 30%
- Your forecast: Realized vol will be 35%

**Strategy:**
1. Buy straddle: $8
2. Delta-hedge daily
3. Profit from realized vol > implied vol

**Expected P&L:**

**If realized vol = 35% vs. 30% implied:**
- Gamma scalping profit: ~$2 per contract
- **Return: 25% on $8 invested**

**Risk:**
- Vol forecast wrong (realized < implied)
- Hedging costs (bid-ask, commissions)
- Gap risk (can't hedge gaps)

### 6. Merger Arbitrage


**Target vs. acquirer spread:**

**Example:**

- Company A to acquire Company B
- Deal terms: 0.5 shares of A for each share of B
- Company A stock: $100
- Company B stock: $48
- Implied B value: 0.5 × $100 = $50
- **Spread: $50 - $48 = $2** (4%)

**Strategy:**
1. Buy B stock: $48
2. Short A stock: 0.5 shares at $100 = $50
3. Wait for deal close

**If deal closes:**
- B converts to 0.5 shares of A
- Net out short position
- Profit: $2 per B share (4%)

**If deal breaks:**
- B stock crashes (maybe to $40)
- A stock rises (maybe to $105)
- **Loss:** $(40 + 0.5 × 105) - 48 = -$3$ (massive!)

**Risk management:**
- Analyze deal probability (regulatory, financing, shareholder vote)
- Size for 10-20% deal break risk
- Typical: 50 deals × 2% each = 100% diversified portfolio

### 7. Statistical Arbitrage


**Pairs trading:**

**Example:**

- Coca-Cola (KO): $60
- PepsiCo (PEP): $180
- Historical ratio: PEP/KO = 3.1
- Current ratio: 180/60 = 3.0
- **Ratio deviation: -3.2%**

**If ratio mean-reverts:**

**Strategy:**
1. Buy $100K KO (undervalued relatively)
2. Short $310K PEP (overvalued relatively)
3. Wait for ratio to return to 3.1

**Convergence scenario:**

For proper pairs trading, use a **dollar-neutral** hedge:

**Setup:**
- Long $100K KO (1,667 shares at $60)
- Short $100K PEP (556 shares at $180)
- Net market exposure: $0

**Scenario 1: Ratio reverts, both rise**
- KO rises 5% to $63 → Position worth $105K → **Gain: +$5K**
- PEP rises 3% to $185.4 → Owe $103K → **Loss: −$3K**
- **Net P&L: +$2K**

**Scenario 2: Ratio reverts, both fall**
- KO falls 2% to $58.8 → Position worth $98K → **Loss: −$2K**
- PEP falls 5% to $171 → Owe $95K → **Gain: +$5K**
- **Net P&L: +$3K**

**Scenario 3: Ratio diverges further (adverse)**
- KO falls 3% to $58.2 → Position worth $97K → **Loss: −$3K**
- PEP rises 2% to $183.6 → Owe $102K → **Loss: −$2K**
- **Net P&L: −$5K**

**Key insight:** Dollar-neutral pairs trading profits from *relative* outperformance regardless of market direction. The hedge ratio ensures approximately equal dollar exposure to each leg, isolating the relative value bet from broad market moves.

---

## Common Mistakes


### 1. Ignoring Transaction Costs


**Thinking small edge is profit:**

- **Mistake:** See 5 bps discrepancy, assume profit
- **Why it fails:** Bid-ask spreads, commissions, slippage eat edge
- **Fix:** Subtract ALL costs before declaring arbitrage
- **Real cost:** "Arbitrage" becomes loss after execution

**Example:**

Index arbitrage opportunity:
- ETF discount: 3 bps
- Commission: 1 bp (ETF) + 2 bps (basket shorting) = 3 bps
- **Net: 0 bps** (not profitable!)

### 2. Execution Risk


**Can't execute all legs simultaneously:**

- **Mistake:** Trade one leg, assume can complete others
- **Why it fails:** Prices move before completion
- **Fix:** Use algorithms for simultaneous execution
- **Real cost:** "Arbitrage" becomes directional bet

**Example:**

Triangular FX arbitrage:
- Leg 1: Buy EUR/USD at 1.0800 ✓
- Leg 2: Try to sell GBP/USD at 1.2700 → Price changed to 1.2695!
- **Execution failure:** Left with unwanted EUR position

### 3. Financing Cost


**Ignoring carry cost:**

- **Mistake:** Calculate arbitrage without financing cost
- **Why it fails:** Most arbitrage requires leverage/borrowing
- **Fix:** Include borrowing rate in calculation
- **Real cost:** 2-5% annual carry erodes edge

**Example:**

Cash-and-carry on index:
- Futures premium: 20 bps
- Finance cost for 3 months: 1.25% (5% annual)
- **Net: 0.20% - 1.25% = -1.05%** (loss!)

### 4. Model Risk


**Using wrong relationship:**

- **Mistake:** Apply Black-Scholes to American options
- **Why it fails:** Early exercise changes valuation
- **Fix:** Use appropriate model for contract type
- **Real cost:** 5-15% mispricing

**Example:**

Put-call parity for American options:
- Early exercise on dividend-paying stock
- Parity doesn't hold exactly
- **Apparent "arbitrage" is actually model error**

### 5. Capacity Constraints


**Assuming infinite size:**

- **Mistake:** Find small arbitrage, try to scale infinitely
- **Why it fails:** Market impact, liquidity limits
- **Fix:** Know your size limits (usually $1-10M)
- **Real cost:** Edge disappears at size

**Example:**

Merger arb spread: 2%
- $1M position: Works fine (earn $20K)
- Try $100M: Can't execute, moves market
- **Actual capacity: $5M** (earn $100K max)

### 6. Regulatory Constraints


**Violating rules unknowingly:**

- **Mistake:** Short sell without locate
- **Why it fails:** Reg SHO violations, fines
- **Fix:** Understand all regulatory constraints
- **Real cost:** Fines, trading suspension

**Example:**

Short selling in ETF arbitrage:
- Need "hard-to-borrow" locate
- Cost: 2% annual (expensive!)
- Naked short: Illegal (Reg SHO)
- **Must factor borrow cost into arbitrage**

### 7. Correlation Breakdown


**Assuming stable relationships:**

- **Mistake:** Pairs trade assuming historical correlation persists
- **Why it fails:** Correlations unstable, especially in crisis
- **Fix:** Monitor correlation, have stop-loss
- **Real cost:** 20-50% drawdown when correlation breaks

**Example:**

Oil stocks pairs trade:
- Historical correlation: 0.85
- Crisis: Correlation → 0.3
- One stock -30%, other -10%
- **Loss despite "hedged" position**

---

## Best vs. Worst Case


### 1. Best Case: Success


**Perfect arbitrage execution:**

**Setup:**
- Quant fund specializing in ETF arbitrage
- High-frequency infrastructure
- Deep knowledge of market structure

**Opportunity:**

SPY (S&P 500 ETF) discount:
- SPY: $450.00
- Fair value: $450.20
- **Discount: 20¢** (4.4 bps)

**Transaction costs:**
- ETF commission: 0.1 bp
- Basket execution: 1.5 bps (using algorithms)
- **Total: 1.6 bps**

**Net edge: 4.4 - 1.6 = 2.8 bps** (profitable!)

**Execution:**

**9:30:15 AM:** Detect opportunity
1. Buy 100,000 SPY shares: $45M at $450.00
2. Short S&P 500 basket: $45.02M equivalent
3. Both executed within 5 seconds

**9:35 AM:** Arbitrage converges
- SPY rises to $450.18
- Basket at $450.20
- Close both positions

**P&L:**
- SPY: +$18,000 (18¢ × 100,000)
- Basket: +$20,000 (20¢ gain from short)
- Wait, that doesn't make sense...

Let me recalculate:
- SPY bought at $450.00, sold at $450.18: +$18K
- Basket shorted at $450.20, covered at $450.20: $0
- **Net: +$18K**

No wait, if SPY rises to fair value:
- SPY profit: $(450.20 - 450.00) × 100K = +$20K
- Basket loss: $(450.20 - 450.20) × equivalent = $0
- **Net: +$20K**

**Return:**
- Profit: $20K
- Capital: $45M (1:1 leverage)
- **Return: 4.4 bps** (over 5 minutes!)
- **Annualized:** Ridiculous (executed 100+ times/day)

**Success factors:**
1. Millisecond detection (HFT infrastructure)
2. Simultaneous execution (both legs filled)
3. Tight risk management (limited size)
4. Diversification (100+ opportunities daily)

**Annual performance:**
- Average 50 trades/day × 252 days = 12,600 trades
- Average profit: 2 bps per trade
- Gross: 12,600 × 2 bps = 252% (!!)
- Costs: Infrastructure $5M, data $1M, salaries $10M = $16M
- On $100M capital: 16% expense ratio
- **Net: 236%** (incredible, but real for top HFT firms)

### 2. Worst Case: Disaster


**Arbitrage gone wrong:**

**Setup:**
- Hedge fund doing convertible arbitrage
- "Market-neutral" strategy
- Leveraged 10:1

**Position (2008):**
- Long $1B convertible bonds
- Short stocks as delta hedge
- Net leverage: 10× on $100M equity

**Strategy breakdown:**

**September 2008: Lehman collapse**

**Day 1:**
- Credit spreads explode (converts crash)
- Stocks also falling (shorts profit)
- Net: Should offset... right?

**Reality:**
- Convert bonds: -20% (illiquid, no bids)
- Stocks: -10% (short profit +10%)
- **Net: -10%**

**But leverage 10×:**
- Portfolio: -10%
- Equity: -10% × 10 = **-100%** (wiped out!)

**What went wrong:**

1. **Liquidity mismatch:**
   - Converts: Illiquid (couldn't sell)
   - Stocks: Liquid (covered shorts)
   - Forced to cover shorts at losses

2. **Credit spread explosion:**
   - Model assumed spreads widen 100 bps
   - Reality: Widened 500 bps
   - 5× unexpected move

3. **Correlation breakdown:**
   - Model: Convert and stock 80% correlated
   - Crisis: Correlation → -0.3 (both fell!)
   - Hedge failed completely

4. **Margin calls:**
   - Prime broker demanded more collateral
   - Forced selling at worst prices
   - Death spiral

**Final losses:**
- Starting equity: $100M
- Final equity: -$20M (negative!)
- **Lost 120%** (investors lost everything plus)

**Aftermath:**
- Fund liquidated
- Lawsuits from investors
- Managers' reputation destroyed
- Example: LTCM, Amaranth, etc.

**Lessons:**
1. Leverage amplifies small errors into catastrophes
2. Models fail in extremes (when you need them most)
3. Liquidity matters more than fair value
4. "Market-neutral" doesn't mean risk-free
5. Correlation → 1 or -1 in crisis (diversification fails)

---

## Risk Management Rules


### 1. Gross vs. Net Exposure


**Track both:**

$$
\text{Gross Exposure} = |\text{Long}| + |\text{Short}|
$$

$$
\text{Net Exposure} = \text{Long} - \text{Short}
$$

**Limits:**

- Gross: < 5× capital (max leverage)
- Net: < 10% of gross (truly market-neutral)

**Example:**

- Capital: $100M
- Long: $250M
- Short: $260M
- Gross: $510M (5.1× leverage) - **At limit**
- Net: -$10M (-2% of gross) - **OK**

### 2. Stop-Loss Discipline


**Exit if arbitrage fails to converge:**

**Rules:**
- Time-based: Exit after 5 days if no convergence
- Loss-based: Exit if loss exceeds 2× expected profit
- Event-based: Exit on liquidity shock

**Example:**

Expected profit: 5 bps
- If loss reaches 10 bps → **Exit**
- Don't wait for convergence

### 3. Liquidity Reserve


**Maintain dry powder:**

$$
\text{Cash Reserve} \geq 30\% \text{ of Capital}
$$

**Purpose:**
- Margin calls
- Unexpected opportunities
- Forced liquidation buffer

### 4. Diversification


**Multiple arbitrage types:**

- Index arb: 30%
- Merger arb: 30%
- Convertible arb: 20%
- Stat arb: 20%

**Never >50% in single strategy** (avoid blow-up risk)

### 5. Stress Testing


**Weekly scenarios:**

1. Spreads widen 3×
2. Liquidity dries up (widen by 5× transaction costs)
3. Correlation → 1 (all positions same direction)
4. Margin call (need to raise 20% cash immediately)

**Maximum loss in worst scenario:**

$$
\text{Stress Loss} \leq 20\% \text{ of Capital}
$$

### 6. Counterparty Limits


**Per prime broker:**

$$
\text{Exposure per PB} \leq 40\% \text{ of Total}
$$

**Minimum: 3 prime brokers** (avoid single point of failure)

### 7. Documentation


**Required records:**

- Entry time and prices (all legs)
- Expected profit and risks
- Exit criteria (time, profit, loss)
- Actual exit and P&L
- Post-trade analysis

**Retention: 7 years**

---

## Real-World Examples


### 1. LTCM (1998)


**The grandaddy of arbitrage disasters:**

**Strategy:**
- Government bond arbitrage (on-the-run vs. off-the-run)
- Volatility arbitrage
- Merger arbitrage
- Total: 100+ strategies

**Leverage: 25:1** (!!!)

**1997: Glory days**
- Return: 43% after fees
- AUM: $126B (including leverage)
- Principals worth billions

**1998: Russian crisis**
- Russia defaults on bonds
- Flight to quality (everyone buys Treasuries)
- LTCM's short Treasury positions crushed
- Spreads widened instead of converging

**Death spiral:**
- Losses mount → Margin calls
- Forced selling → Prices worsen
- More losses → More selling
- **Lost 90% in 4 months**

**Bailout:**
- Federal Reserve orchestrated $3.6B rescue
- Fund liquidated
- Principals lost personal fortunes

**Lesson:** Even "arbitrage" has massive risk with leverage

### 2. Amaranth (2006)


**Natural gas spread arbitrage:**

**Strategy:**
- Calendar spread: March vs. April nat gas futures
- Historical spread: $0.50
- Current spread: $0.30
- Long March, short April (bet on convergence to $0.50)

**Size: $9B position** (on $7.5B capital)

**September 2006:**
- Hurricane season mild (less nat gas demand)
- Spread moved wrong way: $0.30 → $0.10
- **Lost $6.6B in one month** (88% of capital!)

**Collapse:**
- Forced liquidation
- Counterparties smelled blood
- Bought spreads from them at huge discounts
- Fund shut down

**Lesson:** Market can stay irrational longer than you can stay solvent

### 3. VIX ETN Disaster (2018)


**Volatility arbitrage:**

**Product:** XIV (short VIX ETN)

**Strategy:**
- VIX term structure usually in contango
- Roll short VIX futures daily
- Collect "roll yield"
- 2012-2017: Compounded at 50%+ annually

**Investors:** Piled in (became crowded trade)

**February 5, 2018:**
- VIX spike: 17 → 37 (120% in one day)
- XIV: Down 96% (from $108 to $4)
- **Terminated the next day**

**Investors lost billions:**
- Many bought at peak ($140)
- Wiped out in 24 hours

**Lesson:** Short volatility is picking up pennies in front of steamroller

### 4. GameStop (2021)


**The arbitrage that wasn't:**

**Setup:**
- GameStop heavily shorted (>100% of float)
- Hedge funds: Melvin Capital, others
- Thesis: Retail decline, company obsolete

**January 2021:**
- Reddit WallStreetBets organized
- Massive buying pressure (gamma squeeze)
- Price: $20 → $483 (24× in 2 weeks)

**Hedge funds:**
- Forced to cover shorts (buy at any price)
- Melvin lost 53% in January
- Required $2.75B bailout

**Lesson:** "Arbitrage" of fundamentals vs. price can go very wrong when:
- Position crowded
- Liquidity low
- Opponents organized
- Gamma squeezes possible

---

## Practical Steps


### 1. Identify Links


**Map price relationships:**

- Which assets must maintain ratios?
- What are transaction costs?
- Typical spreads between linked assets?
- Historical basis risk?

### 2. Monitor Continuously


**Automated surveillance:**

- Real-time price feeds (all related assets)
- Calculate implied vs. actual prices
- Flag when discrepancy > transaction costs
- Alert system for opportunities

### 3. Calculate True Edge


**Include ALL costs:**

$$
\text{Net Edge} = \text{Gross Spread} - \text{Transaction Costs} - \text{Financing} - \text{Slippage}
$$

**Only proceed if Net Edge > 0**

### 4. Execute Simultaneously


**Best practices:**

- Use algorithms (minimize execution risk)
- All legs in single packet if possible
- IOC orders (immediate or cancel)
- Verify all fills before booking profit

### 5. Monitor Position


**Daily tracking:**

- Mark-to-market both sides
- Check convergence progress
- Set exit triggers (time, profit, loss)
- Be ready to exit quickly

### 6. Analyze Results


**Post-trade:**

- Actual profit vs. expected
- What worked / didn't work?
- Update models with new data
- Document for future

### 7. Scale Carefully


**Gradual increase:**

- Start small (test infrastructure)
- Scale 2× only after 100 successful trades
- Monitor capacity (slippage increases with size)
- Never exceed 10% of market liquidity

---

## Final Wisdom


> "No-arbitrage links are the invisible threads that hold global markets together—covered interest parity connects FX to rates, put-call parity binds options to stocks, and cost-of-carry ties futures to spot. These relationships must hold, or free money appears. But 'must hold' has a big caveat: 'eventually, after transaction costs, if you can execute fast enough, and assuming no liquidity crisis.' The LTCM disaster taught us that leverage transforms 'arbitrage' into 'disaster'—even true relationships take time to converge, and 25:1 leverage means you need them to converge tomorrow, not next month. Modern HFT firms make millions exploiting microsecond violations of these links, proving they exist. But retail traders see the same opportunities in milliseconds, by which time it's gone. The cruel truth: arbitrage is real, but it requires (1) technology (2) speed (3) capital (4) expertise (5) discipline to stay small. Without all five, you're not doing arbitrage—you're doing correlation trades that look like arbitrage until they blow up. The best arbitrage lesson: if it seems obvious and easy, it's not arbitrage—it's a trap. True arbitrage is hard, fast, and requires infrastructure most investors can't access. For the rest of us, understanding these links helps us avoid disasters (like shorting futures below cost-of-carry) and recognize when markets are stressed (when links break). Know the relationships, respect the links, but unless you're Two Sigma or Citadel, don't confuse 'seeing the relationship' with 'being able to arbitrage it.'"

**Key to success:**

- Understand ALL no-arbitrage links (they're real foundations)
- Include every single cost (many "arbitrages" are losses after costs)
- Execute with speed (opportunities vanish in milliseconds for HFT)
- Use minimal leverage (3-5× max, not 25× like LTCM)
- Diversify strategies (never 100% in one arbitrage type)
- Have liquidity reserves (30% cash for margin calls)
- Stress test religiously (assume links temporarily break)
- Know when to exit (discipline beats hope)
