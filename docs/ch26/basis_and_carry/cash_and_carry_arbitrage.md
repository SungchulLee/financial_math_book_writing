# Cash-and-Carry Arbitrage

**Cash-and-carry arbitrage** in cryptocurrency markets exploits the basis (price difference) between spot and futures/perpetual contracts by simultaneously buying the underlying asset (BTC, ETH) and shorting an equivalent futures position, locking in the spread as risk-free profit when the derivative converges to spot at expiration or through funding rate payments, with typical annual returns of 5-30% in traditional crypto futures and 20-100%+ during periods of elevated perpetual funding, though constrained by counterparty risk (exchange failure), funding cost volatility, regulatory uncertainty, and the capital intensity of maintaining fully hedged delta-neutral positions across platforms.

---

## The Core Insight

**The fundamental idea:**

- Futures/perpetuals trade at premium to spot (usually)
- Premium = Basis = Future price - Spot price
- Cash-and-carry: Buy spot + Short future = Lock in basis
- Profit when convergence occurs (expiration or funding)
- "Risk-free" in theory, but exchange/regulatory risk in practice
- Perpetuals use funding rate instead of expiration convergence
- Quarterly futures converge at expiration (guaranteed)
- Returns: 5-30% normal, 50-100%+ during euphoria
- Capital intensive: Requires full notional on both legs

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/crypto_cash_and_carry.png?raw=true" alt="crypto_cash_and_carry" width="700">
</p>
**Figure 1:** Cash-and-carry arbitrage mechanism showing spot purchase, futures/perpetual short, basis convergence paths (quarterly expiration vs continuous funding), profit calculation including costs, and exchange risk management through platform diversification.

**You're essentially asking: "How do I lock in the crypto basis as guaranteed profit?"**

---

## What Is Cash-and-Carry?

### 1. The Basic Mechanism

**Trade structure:**

**Long leg:** Buy spot cryptocurrency
**Short leg:** Sell futures or perpetual contract
**Net position:** Market-neutral (delta = 0)

**Profit source:**

$$
\text{Profit} = \text{Basis} - \text{Costs}
$$

Where:
- Basis = Future price - Spot price (at entry)
- Costs = Fees + Funding + Opportunity cost

**Example—Quarterly futures:**

BTC spot: $43,000
BTC March futures: $43,500
Basis: $500 (1.16%)

**Trade:**
- Buy: 10 BTC spot at $43,000 = $430,000
- Sell: 10 BTC March futures at $43,500

**At March expiration:**
- Spot = Futures (converge)
- Lock in: $500 per BTC × 10 = **$5,000**
- Return: $5,000 / $430,000 = 1.16%

**If 3 months to expiration:**
- Annualized: 1.16% × 4 = **4.64%**

### 2. Perpetual Funding Version

**Instead of quarterly expiration:**

**Long leg:** Buy spot BTC
**Short leg:** Sell perpetual contract
**Profit source:** Funding rate payments (continuous)

**Funding collection:**

$$
\text{Daily Funding} = \text{Position Size} \times \text{Funding Rate} \times 3
$$

**Example:**

Funding rate: 0.03% per 8 hours

**Position:**
- Long: 10 BTC spot at $43,000 = $430,000
- Short: 10 BTC perpetual at $43,000

**Daily collection:**
- $430,000 × 0.03% × 3 = **$387/day**

**Annual projection:**
- $387 × 365 = **$141,255**
- Return: $141,255 / $430,000 = **32.8% annually**

**Reality check:**
- Funding varies daily (not constant 0.03%)
- Average funding 0.01-0.02% more realistic
- Realistic annual: 11-22%

### 3. Fair Value vs Market Price

**Theoretical fair value:**

$$
F = S \times e^{(r-y)T}
$$

Where:
- $F$ = Fair futures price
- $S$ = Spot price
- $r$ = Risk-free rate
- $y$ = Yield/dividend (0 for crypto)
- $T$ = Time to expiration

**Simplified (small T):**

$$
F \approx S \times \left(1 + r \times T\right)
$$

**Example:**

BTC spot: $43,000
Risk-free rate: 5% annually
Time: 90 days (0.25 years)

$$
F = 43,000 \times e^{0.05 \times 0.25} = 43,000 \times 1.0126 = 43,542
$$

**Fair value:** $43,542

**If market futures:** $44,000
**Arbitrage basis:** $44,000 - $43,542 = **$458** (excess premium)

### 4. Basis Decomposition

**Total basis has components:**

$$
\text{Total Basis} = \text{Interest Cost} + \text{Risk Premium} + \text{Sentiment Premium}
$$

**Interest cost:**
- Cost to finance spot purchase
- Typically 3-5% in crypto (USDT/USDC borrow)

**Risk premium:**
- Exchange risk compensation
- Regulatory risk compensation
- Typically 5-15% in crypto (vs 0.5-2% TradFi)

**Sentiment premium:**
- Bullish/bearish positioning
- Can be -10% to +50%
- Highly variable

**Example breakdown:**

Total basis: 25% annually

**Decomposition:**
- Interest: 5%
- Risk premium: 10%
- Sentiment: 10%

**Arbitrageur captures:** All 25% (but bears risks)

### 5. Convergence Mechanisms

**Quarterly futures:**

**Forced convergence at expiration:**
- Futures settle to spot index
- Cash-settled (no physical delivery)
- Guaranteed convergence

**Timeline:**
- Entry: 90 days before expiration
- Hold: Until expiration
- Exit: Automatic settlement

**Example:**

December futures, entered September 1:
- Entry: BTC $43,000 spot, $43,800 futures
- Basis: $800
- Hold 90 days
- December expiration: Futures settle to spot (whatever it is)
- **Profit: $800 locked in**

**Perpetuals:**

**Continuous convergence via funding:**
- No expiration
- Funding rate incentivizes convergence
- Can exit anytime

**Timeline:**
- Entry: Anytime
- Hold: Days to months
- Exit: When funding normalizes or target met

**Example:**

Entered with funding 0.05% per 8h:
- Collect: 0.15% daily
- Hold 60 days
- Total collected: 9%
- Exit when funding drops to 0.01%

### 6. Execution Mechanics

**Simultaneous execution critical:**

**Process:**
1. Calculate position size
2. Prepare both orders (spot buy + futures sell)
3. Execute simultaneously (or spot first, futures 30 sec later)
4. Verify hedge ratio (1:1 typically)
5. Monitor positions

**Example execution:**

$500,000 allocation

**Step 1:** Calculate
- 10 BTC at $43,000 = $430,000 spot
- 10 BTC futures short

**Step 2:** Prepare orders
- Spot: Limit buy 10 BTC at $43,000 (Coinbase)
- Futures: Limit sell 10 BTC at $43,500 (CME or Binance)

**Step 3:** Execute
- 10:00:00 - Submit spot buy
- 10:00:02 - Submit futures sell
- Both fill within 10 seconds

**Step 4:** Verify
- Spot: Long 10 BTC
- Futures: Short 10 BTC
- Net delta: 0 ✓

**Execution risk:**
- Price moves between legs
- Slippage on large size
- One leg fills, other doesn't

### 7. Platform Selection

**Exchange pairing:**

**Option 1:** Spot on regulated exchange + Futures on CME
- Spot: Coinbase, Kraken
- Futures: CME (institutional, regulated)
- Advantage: Regulatory clarity
- Disadvantage: Lower basis (5-10% typical)

**Option 2:** Spot on one exchange + Perp on another
- Spot: Coinbase
- Perp: Binance, Bybit
- Advantage: Higher basis (20-50%+)
- Disadvantage: Offshore exchange risk

**Option 3:** Both on same exchange (not recommended)
- Both: Binance spot + Binance perp
- Advantage: Easy execution
- Disadvantage: Not true hedge (same counterparty)

**Risk ranking:**
1. Option 1 (safest): Regulated + regulated
2. Option 2 (moderate): Regulated + offshore
3. Option 3 (risky): Single exchange (FTX lesson)

---

## Key Terminology

**Basis:**
- Futures - Spot price
- Positive (contango): Futures expensive
- Negative (backwardation): Futures cheap
- Measured in $ or %

**Contango:**
- Futures > Spot
- Normal in crypto (usually)
- Longs willing to pay premium
- Positive carry for cash-and-carry

**Backwardation:**
- Futures < Spot
- Rare in crypto
- Shorts dominating (panic)
- Negative carry (loss on c&c)

**Convergence:**
- Futures → Spot over time
- Guaranteed at expiration
- Via funding for perpetuals
- Source of arbitrage profit

**Funding Rate:**
- Perpetual swap payment
- Longs pay shorts (typical)
- Replaces expiration convergence
- Measured per 8 hours

**Notional:**
- Total position size
- Both legs equal
- Example: $500K long, $500K short
- Gross exposure: $1M

**Delta-Neutral:**
- Net directional exposure = 0
- Price moves don't affect P&L (ideally)
- Long spot + short futures
- Immune to price changes

**Roll:**
- Close expiring futures
- Open next quarter futures
- Incurs costs (bid-ask spread)
- Not needed for perpetuals

---

## Cash-and-Carry Strategies

### 1. Classic Quarterly Futures

**Strategy:**

Buy spot, short quarterly futures, hold to expiration

**Setup:**
- Identify futures trading at premium
- Calculate annualized basis
- Execute if basis > costs + risk premium

**Example:**

March BTC futures (90 days out):
- Spot: $43,000
- Futures: $43,800
- Basis: $800 (1.86% for 90 days)
- Annualized: 7.44%

**Trade:**
- Buy: 10 BTC spot at $43,000 = $430,000 (Coinbase)
- Sell: 10 BTC March futures at $43,800 (CME)

**Costs:**
- Spot fee: 0.5% = $2,150
- Futures fee: $2.50/contract × 10 = $25
- Opportunity cost: 5% × 90/365 = 1.23% = $5,289
- **Total costs: $7,464** (1.74%)

**Net profit:**
- Basis: $8,000 (1.86%)
- Costs: $7,464 (1.74%)
- **Net: $536** (0.12% for 90 days, 0.5% annualized)

**Hold period:** 90 days (until March expiration)

**At expiration:**
- Futures settle to spot index
- Close spot position
- Realize $536 profit

### 2. Perpetual Funding Harvest

**Strategy:**

Buy spot, short perpetual, collect funding continuously

**Setup:**
- Monitor funding rate
- Enter when funding >0.03% per 8h (>33% annual)
- Exit when funding <0.01% or target achieved

**Example:**

Funding: 0.05% per 8h (54.75% annualized)

**Trade:**
- Buy: 10 BTC spot at $43,000 = $430,000
- Short: 10 BTC perpetual at $43,000

**Daily collection:**
- 0.05% × 3 per day = 0.15% daily
- $430,000 × 0.15% = **$645/day**

**30-day hold:**
- Total: $645 × 30 = **$19,350**
- Return: 4.5% (monthly), **54.75% annualized**

**Costs:**
- Entry fees: 0.5% spot + 0.02% perp = $2,236
- Opportunity cost: 5% × 30/365 = $1,767
- **Total: $4,003**

**Net profit:**
- Funding: $19,350
- Costs: $4,003
- **Net: $15,347** (3.57% monthly, 42.8% annualized)

**Exit trigger:**
- Funding drops to 0.01% (11% annual, below threshold)

### 3. Cross-Platform Arbitrage

**Strategy:**

Exploit funding/basis differences across exchanges

**Setup:**
- Spot on Exchange A
- Perpetual on Exchange B (higher funding)

**Example:**

Binance funding: 0.03%
Deribit funding: 0.06%
Spread: 0.03% per 8h (33% annual)

**Trade:**
- Buy: 10 BTC spot on Coinbase at $43,000
- Short: 10 BTC perp on Deribit at $43,000

**Additional profit:**
- Standard funding: 0.03% (33% annual)
- Deribit premium: 0.03% (33% annual)
- **Total: 0.06% per 8h (65.7% annualized)**

**Risk:**
- Deribit counterparty risk (vs Binance)
- Cross-exchange execution risk
- Regulatory (Deribit offshore)

### 4. Leveraged Carry (Advanced)

**Strategy:**

Use margin to amplify cash-and-carry returns

**Setup:**
- Borrow USDT at 5-8%
- Invest in cash-and-carry
- Amplify returns (but also risks)

**Example:**

Own $200K, borrow $300K USDT at 6%

**Total capital:** $500K

**Trade:**
- Buy: 11.63 BTC spot at $43,000 = $500K
- Short: 11.63 BTC perp
- Funding: 0.04% per 8h (43.8% annual)

**Annual income:**
- $500K × 43.8% = $219,000

**Annual costs:**
- Borrow: $300K × 6% = $18,000
- Opportunity: $200K × 5% = $10,000
- **Total: $28,000**

**Net profit:**
- Income: $219,000
- Costs: $28,000
- **Net: $191,000** (95.5% return on $200K equity!)

**Risk:**
- Exchange failure (lose $500K)
- Funding drops (income disappears, still pay borrow)
- Liquidation if perp side moves against

**Leverage calculation:**

$$
\text{Leverage} = \frac{\text{Total Notional}}{\text{Own Capital}} = \frac{500K}{200K} = 2.5\times
$$

### 5. Roll-Optimized Futures

**Strategy:**

Minimize roll costs by timing and platform selection

**Setup:**
- Trade quarterly futures
- Roll 7-10 days before expiration (avoid crunch)
- Use limit orders (not market)

**Example:**

December futures expiring Dec 29:
- Dec 19: Roll to March futures
- Avoid Dec 27-29 (expensive, everyone rolling)

**Roll cost:**
- Normal (7 days early): 0.05% in slippage
- Expensive (1 day before): 0.20% in slippage

**Annual roll cost:**
- 4 rolls per year × 0.05% = **0.20%**
- vs 4 × 0.20% = 0.80% if wait until last minute

**Savings:** 0.60% annually on $500K = **$3,000/year**

### 6. Dynamic Rebalancing

**Strategy:**

Adjust positions based on funding rate changes

**Rules:**
- If funding >0.08%: Increase allocation (25% → 40%)
- If funding 0.03-0.08%: Maintain (25%)
- If funding <0.03%: Reduce (25% → 10%)
- If funding negative: Exit completely

**Example:**

Portfolio: $1M

**Month 1:** Funding 0.03% (33% annual)
- Allocation: 25% = $250K in cash-and-carry

**Month 2:** Funding rises to 0.10% (109% annual)
- Increase allocation: 40% = $400K
- New position: +$150K

**Month 3:** Funding drops to 0.02% (22% annual)
- Reduce allocation: 10% = $100K
- Close: $300K

**Result:**
- Month 1: 25% × 33% = 8.25% annual contribution
- Month 2: 40% × 109% = 43.6% annual contribution
- Month 3: 10% × 22% = 2.2% annual contribution
- **Average: 18% blended return** (vs 11% if static 25%)

### 7. Multi-Asset Diversification

**Strategy:**

Spread across BTC, ETH, and other crypto basis trades

**Allocation:**
- BTC: 50% ($250K)
- ETH: 30% ($150K)
- SOL/Other: 20% ($100K)

**Rationale:**
- Diversify exchange risk
- Different funding rate patterns
- Lower correlation of basis

**Example:**

**BTC:**
- Funding: 0.03% (33% annual)
- Contribution: $250K × 33% = $82,500

**ETH:**
- Funding: 0.05% (54.75% annual)
- Contribution: $150K × 54.75% = $82,125

**SOL:**
- Funding: 0.07% (76.65% annual)
- Contribution: $100K × 76.65% = $76,650

**Total annual income:** $241,275 (48.3% on $500K)

**Risk reduction:**
- If Binance (BTC perp) fails: Lose $250K, not $500K
- If funding normalizes on BTC: Still collect on ETH/SOL

---

## Common Mistakes

### 1. Single Exchange Risk

**Both legs on same platform:**

- **Mistake:** Long spot + short perp both on Binance
- **Why it fails:** Exchange failure = both legs gone
- **Fix:** Spot on Exchange A, perp on Exchange B
- **Real cost:** 100% loss (FTX: $8B)

**Example:**

$500K cash-and-carry on FTX (Nov 2022):
- Long: 11.63 BTC spot on FTX
- Short: 11.63 BTC perp on FTX
- FTX bankrupts
- Both legs frozen
- **Total loss: $500K** despite "hedged"

### 2. Ignoring Funding Volatility

**Assuming constant funding:**

- **Mistake:** Project 0.05% funding for year
- **Why it fails:** Funding drops to 0.01% after 2 months
- **Fix:** Use conservative average (0.02-0.03%)
- **Real cost:** Overestimate returns by 50-70%

**Example:**

Entry with funding 0.08% (87.6% annual):
- Projected annual: $500K × 87.6% = $438K

**Reality:**
- Month 1-2: 0.08% (collect $73K)
- Month 3-12: 0.02% (collect $100K)
- **Total: $173K** (34.6% actual vs 87.6% projected)

### 3. Overleveraging

**Using borrowed funds:**

- **Mistake:** Borrow 5× to do cash-and-carry
- **Why it fails:** Funding drops, still owe interest
- **Fix:** Max 2× leverage, preferably none
- **Real cost:** Negative carry if funding < borrow rate

**Example:**

Own $100K, borrow $400K at 8%:
- Total: $500K in cash-and-carry
- Funding: Starts 0.05% (54.75%), drops to 0.015% (16.4%)
- Funding income: $500K × 16.4% = $82K
- Borrow cost: $400K × 8% = $32K
- **Net: $50K** (50% ROE, but risky)

**If funding drops to 0.01% (11%):**
- Income: $500K × 11% = $55K
- Borrow: $32K
- **Net: $23K** (23% ROE, declining)

**If funding goes negative -0.01%:**
- Income: -$55K (paying!)
- Borrow: $32K
- **Net: -$87K** (total loss in one year)

### 4. Neglecting Roll Costs

**For quarterly futures:**

- **Mistake:** Ignore bid-ask on rolls (4× per year)
- **Why it fails:** 0.1-0.3% per roll × 4 = 0.4-1.2% annual drag
- **Fix:** Account for roll costs in return calculation
- **Real cost:** 20-40% of net profit

**Example:**

Basis: 8% annually
- Quarterly roll cost: 0.2% × 4 = 0.8%
- Fees: 0.5%
- Opportunity: 5%
- **Net: 8% - 6.3% = 1.7%** (not 8%!)

### 5. Wrong Hedge Ratio

**Not matching notional:**

- **Mistake:** Long $500K spot, short $480K perp (forgot fees)
- **Why it fails:** Unhedged $20K exposure
- **Fix:** Ensure 1:1 notional match
- **Real cost:** Directional risk

**Example:**

BTC drops 20%:
- Spot loss: $500K × 20% = -$100K
- Perp gain: $480K × 20% = +$96K
- **Net loss: -$4K** (should be $0 if hedged)

### 6. Tax Inefficiency

**Frequent rebalancing:**

- **Mistake:** Close and reopen positions monthly
- **Why it fails:** Each close = taxable event
- **Fix:** Minimize turnover, hold >1 year if possible
- **Real cost:** 37% vs 20% tax rate

**Example:**

Monthly rebalancing (12 taxable events):
- Gains: $50K total
- Tax (short-term): $50K × 37% = **$18,500**

**Annual rebalancing (1 taxable event >1 year):**
- Gains: $50K
- Tax (long-term): $50K × 20% = **$10,000**

**Savings: $8,500** (85% more after-tax)

### 7. Ignoring Withdrawal Limits

**Can't withdraw spot in crisis:**

- **Mistake:** All $500K spot on one exchange
- **Why it fails:** Withdrawal limits ($100K/day)
- **Fix:** Diversify spot holdings, self-custody portion
- **Real cost:** Trapped capital during exit

**Example:**

Need to exit $500K position:
- Exchange limit: $100K/day
- **Takes 5 days to withdraw spot**
- Meanwhile: Funding flips negative, losing $500/day
- **Extra cost: $2,500** (plus opportunity cost)

---

## Risk Management Rules

### 1. Platform Diversification

**Never >50% on one exchange:**

$$
\text{Per Exchange Limit} = 0.5 \times \text{Total Allocation}
$$

**Example:**

$1M cash-and-carry portfolio:
- Coinbase spot: $250K (25%)
- Kraken spot: $250K (25%)
- Binance perp: $300K (30%)
- Bybit perp: $200K (20%)

**No single point of failure**

### 2. Minimum Funding Threshold

**Entry rule:**

$$
\text{Min Funding for Entry} \geq 0.03\% \text{ per 8h} \quad (33\% \text{ annual})
$$

**Exit rule:**

$$
\text{Exit if Funding} < 0.015\% \text{ per 8h} \quad (16.4\% \text{ annual})
$$

**Rationale:** 16.4% barely covers exchange + opportunity risk

### 3. Leverage Limits

**Maximum leverage:**

$$
\text{Max Leverage} = \frac{\text{Total Position}}{\text{Own Capital}} \leq 2\times
$$

**Calculation:**

Own $500K, can borrow up to $500K:
- Total position: $1M max
- Leverage: 2×

**Never exceed 2× for cash-and-carry**

### 4. Position Sizing by Funding

**Allocation based on funding level:**

$$
\text{Allocation} = \begin{cases}
10\% & \text{if Funding} < 0.03\% \\
25\% & \text{if } 0.03\% \leq \text{Funding} < 0.05\% \\
40\% & \text{if } 0.05\% \leq \text{Funding} < 0.08\% \\
50\% & \text{if Funding} \geq 0.08\%
\end{cases}
$$

**Example:**

$1M portfolio, funding 0.06%:
- Allocation: 40%
- Position: $400K in cash-and-carry
- Remaining: $600K in other strategies

### 5. Daily Monitoring

**Check daily:**
- Funding rate (has it changed?)
- Collateral ratio (perp side)
- Exchange health (news, proof of reserves)
- Position P&L (should be flat if delta-neutral)

**Alert thresholds:**
- Funding drops >50% (e.g., 0.06% → 0.03%)
- Position P&L >2% (hedge broken)
- Exchange news (regulatory, hack, insolvency)

### 6. Hedging Breakdown Detection

**Monitor delta:**

$$
\Delta = \frac{\partial \text{P&L}}{\partial \text{BTC Price}}
$$

**Should be ~0 if properly hedged**

**Test:**
- BTC moves 1%
- Position P&L should be <0.1%
- If P&L >0.5%: Hedge broken, rebalance

**Causes of breakdown:**
- Different contract sizes (1 BTC vs 5 BTC futures)
- Fees/funding changed notional
- Liquidation on one leg (catastrophic)

### 7. Exit Planning

**Predetermined exit triggers:**

1. Funding < 0.015% (not worth risk)
2. Exchange concerns (regulatory, solvency)
3. Better opportunity elsewhere (reallocation)
4. Target return achieved (e.g., 20% in 6 months)

**Exit process:**
1. Close perp/futures first (faster)
2. Withdraw spot immediately (before limit changes)
3. Document for taxes

---

## Real-World Examples

### 1. Q1 2021 Funding Boom

**Event:** Extreme funding rates during bull market

**Setup (January-March 2021):**
- BTC rallying $30K → $60K
- Perpetual funding: 0.05-0.10% per 8h
- Annualized: 54.75-109.5%

**Arbitrageurs:**
- Entered cash-and-carry
- Capital deployed: Billions across industry

**Example trade:**

February 2021, funding 0.08% (87.6% annual):
- Long: $1M BTC spot
- Short: $1M BTC perp

**3-month return:**
- Funding collected: $219K (87.6% annual / 4)
- Costs: $10K (fees + opportunity)
- **Net profit: $209K** (20.9% in 3 months)

**Exit:** April 2021, funding dropped to 0.02% (22%)

### 2. FTX Collapse Impact (November 2022)

**Event:** Exchange bankruptcy

**Traders affected:**
- Cash-and-carry positions on FTX
- Both spot and perp on same exchange

**Example:**

Trader with $5M on FTX:
- Long: 116.3 BTC spot
- Short: 116.3 BTC perp
- "Hedged" position (delta-neutral)

**November 8:** FTX halts withdrawals
- Both legs frozen
- Bankruptcy filed
- **Total loss: $5M**

**If diversified:**
- Spot on Coinbase: Safe, withdrew to cold storage
- Perp on FTX: Lost
- **Loss: $2.5M** (50% instead of 100%)

**Lesson:** Never both legs on same exchange

### 3. COVID March 2020 Basis Spike

**Event:** Extreme volatility, basis widened

**March 12-13, 2020:**
- BTC crashed $8,000 → $3,800 (52%)
- Quarterly futures basis: Blew out to 10-15% (annualized 40-60%!)
- Perpetual funding: -0.10% (shorts paying, panic)

**Opportunity:**
- Buy spot $3,800
- Sell June futures $4,200
- Lock in $400 (10.5%) for 3 months (42% annual)

**Trade executed:**
- Buy: 100 BTC spot at $3,800 = $380K
- Sell: 100 BTC June futures at $4,200

**June expiration:**
- BTC spot: $9,500 (rallied 150%!)
- Futures: Settled at $9,500
- Spot P&L: +$5.7M (!!)
- Futures P&L: -$5.3M
- **Basis profit: $40K** (locked in, as planned)

**Return:** $40K / $380K = 10.5% (42% annualized)

### 4. CME vs Offshore Basis Differential (2023)

**Event:** Regulatory premium on offshore exchanges

**Setup:**
- CME BTC futures: 5% annual basis
- Binance perp funding: 25% annual
- Differential: 20%

**Strategy:**
- Buy BTC spot (Coinbase)
- Short Binance perp (higher funding)
- vs short CME (lower basis but safer)

**Example:**

$1M allocation

**Option A (CME):**
- Spot + CME short
- Return: 5% annual = $50K
- Risk: Low (both regulated)

**Option B (Binance):**
- Spot + Binance short
- Return: 25% annual = $250K
- Risk: Higher (Binance offshore)

**Many chose Option B** (extra 20% worth risk)

### 5. Ethereum Merge Arbitrage (September 2022)

**Event:** ETH transition to proof-of-stake

**Pre-merge:**
- Uncertainty about chain split
- Futures trading at discount (rare!)
- Backwardation: -5% to spot

**Trade:**
- Short spot ETH (or hold synthetic short)
- Long ETH futures (at discount)
- **Reverse cash-and-carry**

**September 15 merge:**
- No chain split (POW chain died)
- Futures converged to spot
- **Captured 5% basis**

**Example:**

$500K position:
- Short spot: 400 ETH at $1,500
- Long futures: 400 ETH at $1,425

**Post-merge:**
- Futures → Spot
- Profit: ($1,500 - $1,425) × 400 = **$30K**
- Return: 6% in 2 weeks

### 6. Grayscale GBTC Premium (2020-2021)

**Event:** GBTC trading at 20-40% premium to NAV

**Structure:**
- Buy BTC spot
- Deposit to Grayscale (6-month lock)
- Receive GBTC shares
- Sell GBTC shares at premium

**Example (2020):**

- Buy: 100 BTC at $10,000 = $1M
- Deposit: Creates 106.5 GBTC shares (after fees)
- Wait: 6 months
- GBTC premium: 30%
- Sell: 106.5 shares × $13,000 = $1.38M
- **Profit: $380K** (38% in 6 months)

**2021:** Premium collapsed, then went negative (discount)
- Arbitrage trade unwound painfully
- Those locked in: Couldn't exit

**Lesson:** Lockup risk can backfire if premium disappears

### 7. Kimchi Premium Arbitrage Attempt (2017-2018)

**Event:** Korean exchanges at 20-50% premium

**Setup:**
- BTC in Korea: $12,000
- BTC globally: $10,000
- Premium: 20%

**Attempted arbitrage:**
- Buy BTC globally: $10,000
- Transfer to Korean exchange
- Sell for $12,000
- **Expected profit: $2,000 (20%)**

**Reality:**
- Capital controls (hard to get USD out of Korea)
- KYC restrictions (need Korean residency)
- Withdrawal limits
- **Arbitrage impossible for non-residents**

**Lesson:** Geographic arbitrage has regulatory barriers

---

## Practical Steps

### 1. Evaluate Basis Opportunity

**Daily routine:**

Check basis/funding across exchanges:
- CME BTC futures: 5% annual
- Binance funding: 0.02% per 8h (22% annual)
- Bybit funding: 0.03% per 8h (33% annual)

**Decision:**
- If max basis >30% annual: Attractive
- If <20% annual: Marginal (barely worth exchange risk)

### 2. Calculate Expected Return

**Formula:**

$$
\text{Expected Return} = \text{Basis/Funding} - \text{All Costs}
$$

**Components:**

**Basis/Funding:** 0.05% per 8h = 54.75% annual

**Costs:**
- Entry fees: 0.5% (one-time)
- Opportunity cost: 5% annual
- Exit fees: 0.5% (one-time)
- Total annual costs: ~6%

**Net expected:** 54.75% - 6% = **48.75% annual**

### 3. Size Position

**Risk-based sizing:**

$$
\text{Position Size} = \text{Portfolio} \times \text{Allocation\%}
$$

**Example:**

$1M portfolio, 30% allocation:
- Position: $300K
- Long: $300K BTC spot
- Short: $300K BTC perp

### 4. Execute Trade

**Step-by-step:**

1. **Prepare capital:**
   - $300K USDT on spot exchange
   - $30K USDT on perp exchange (margin)

2. **Buy spot first:**
   - Limit order: 6.98 BTC at $43,000
   - Fill confirmed

3. **Short perp immediately (within 30 sec):**
   - Limit order: 6.98 BTC at $43,000
   - Leverage: 10× (margin $30K, notional $300K)
   - Fill confirmed

4. **Verify hedge:**
   - Spot: Long 6.98 BTC
   - Perp: Short 6.98 BTC (notional $300K)
   - **Net delta: 0** ✓

### 5. Monitor Position

**Daily checks:**

- Funding collected (should be ~$410/day at 0.05%)
- Perp margin ratio (should be >50%, alert if <30%)
- Spot safe in custody
- Net P&L (should be ~$0 if delta-neutral)

**Weekly:**
- Total funding collected vs expected
- Adjust if funding changed significantly

### 6. Rebalance if Needed

**Trigger:** Hedge breakdown (delta ≠ 0)

**Cause:** Fees/funding changed notional slightly

**Fix:**

Original:
- Spot: 6.98 BTC
- Perp: 6.98 BTC short

**After 3 months:**
- Spot: Still 6.98 BTC
- Perp notional (after funding): Effectively 6.93 BTC

**Rebalance:**
- Reduce perp short by 0.05 BTC
- Or buy 0.05 BTC spot

### 7. Exit Strategy

**When to exit:**

- Funding drops <0.015% per 8h (16.4% annual)
- Better opportunity elsewhere
- Exchange concerns
- Target achieved (e.g., 6 months, 25% return)

**Exit process:**

1. **Close perp first:**
   - Buy 6.98 BTC perp to close short
   - Withdraw margin

2. **Sell/hold spot:**
   - Sell if exiting completely
   - Hold if redeploying elsewhere
   - Withdraw to self-custody if holding

3. **Calculate realized return:**
   - Funding collected: $37,000
   - Costs: $4,000
   - **Net profit: $33,000** (11% return)

---

## Final Wisdom

> "Cash-and-carry arbitrage in crypto is the closest thing to 'risk-free' that exists in this Wild West market—you're simultaneously long and short the same asset, market-neutral (theoretically), collecting the basis as the derivative converges to spot, with annualized returns of 5-30% in normal markets and 50-100%+ during euphoric periods when perpetual funding hits 0.10-0.15% per 8 hours. This strategy works because crypto derivatives structurally trade at a premium: longs outnumber shorts (everyone's bullish), leverage is expensive (10-30% annually), and regulatory uncertainty commands a risk premium (5-15%). The quarterly futures version guarantees convergence at expiration—BTC spot is $43,000 and June futures are $44,000, you lock in that $1,000 by buying spot and shorting futures, and on June 28th the futures settle to spot, period, end of story. Perpetuals are messier: no expiration, so convergence happens via funding rate (longs pay shorts every 8 hours), but funding is volatile—it can be 0.08% today (87% annualized) and 0.01% tomorrow (11% annualized), making return projections uncertain. The killer insight: this is NOT risk-free despite being market-neutral. FTX proved it catastrophically—traders with 'hedged' positions (long spot + short perp, both on FTX) lost 100% when the exchange failed, because both legs were with the same counterparty. The correct execution is spot on Coinbase (regulated, self-custody possible) and perp on Binance/Bybit (offshore, higher yields), diversifying counterparty risk. Overleveraging this strategy is suicide: if you borrow 5× to amplify returns and funding flips negative (shorts paying longs), you're paying funding PLUS borrow costs, easily -20% annually. The math works beautifully until it doesn't: funding 0.05% × 3 per day × 365 days = 54.75% annually minus 5% opportunity cost minus 1% fees = 48.75% net, but only if (1) funding stays elevated (it won't), (2) exchange survives (FTX didn't), (3) you sized conservatively (most don't). Historical examples validate both the opportunity and the risk: Q1 2021 delivered 20%+ quarterly returns to arbitrageurs, COVID March 2020 offered 40-60% annualized basis on quarterly futures, and November 2022 FTX collapse wiped out $5M+ 'hedged' positions. The golden rules: (1) Never both legs on same exchange (FTX lesson), (2) Size at 25-40% of portfolio max (not 100%), (3) Minimum 0.03% funding to enter (33% annual), exit at 0.015% (16.4% annual, not worth risk below this), (4) No leverage or max 2× (borrow costs kill if funding normalizes), (5) Diversify across BTC/ETH/alts (different funding patterns), (6) Daily monitoring (funding changes, exchange health, hedge ratio), (7) Self-custody spot where possible (reduces counterparty risk 50%). The deepest truth: cash-and-carry's high returns compensate for exchange risk, regulatory risk, and opportunity cost—it's NOT free money, it's being paid 20-50% annually to bear risks that traditional finance won't touch. For institutions with compliance departments and regulatory clarity (CME futures only), returns are 5-10% (still attractive vs bonds). For retail willing to use offshore exchanges, returns can be 30-60%, but you're one FTX away from total loss."

**Key to success:**

- Different exchanges for spot and perp (never both on same platform)
- Enter only when funding >0.03% per 8h (33% annually minimum)
- Exit when funding <0.015% per 8h (16.4% annual, not worth risk)
- Size conservatively (25-40% of portfolio maximum)
- No leverage or max 2× (borrow costs destroy returns if funding normalizes)
- Daily monitoring (funding rate, exchange health, hedge ratio verification)
- Self-custody spot where possible (withdraw immediately after purchase)
- Realistic projections (use 0.02-0.03% average funding, not peak rates)
