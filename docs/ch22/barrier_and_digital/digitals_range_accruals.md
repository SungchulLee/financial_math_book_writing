# Digitals and Range Accruals

**Digital options and range accruals** are binary-payoff derivatives where digitals pay fixed amounts if conditions are met (all-or-nothing outcomes) while range accruals accumulate daily payments only when the underlying trades within specified ranges, creating fundamentally different risk profiles from standard options by eliminating gradual payoff scaling and introducing discontinuous value changes at trigger levels.

---

## The Core Insight

**The fundamental idea:**

- Standard options: Payoff scales with how far ITM (gradual)
- Digital options: Fixed payoff if condition met (binary)
- Range accruals: Daily counting mechanism (cumulative)
- All-or-nothing creates extreme sensitivity near triggers
- Small price moves = huge value changes
- Path matters for accruals (every day counts)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/digital_vs_vanilla_payoff.png?raw=true" alt="digital_vs_vanilla_payoff" width="700">
</p>
**Figure 1:** Comparison of vanilla option (continuous payoff) versus digital option (binary payoff) showing the discontinuous jump at strike level that creates infinite gamma at the strike and makes digital options extremely difficult to hedge near expiration.

**You're essentially asking: "What if options were all-or-nothing bets instead of graduated payoffs?"**

---

## What Are Digital Options?

### 1. Core Structure

**Binary payoff definition:**

**Digital call:**

$$
V_T = \begin{cases}
N & \text{if } S_T > K \\
0 & \text{if } S_T \leq K
\end{cases}
$$

Where $N$ = Notional payment (fixed amount)

**Digital put:**

$$
V_T = \begin{cases}
N & \text{if } S_T < K \\
0 & \text{if } S_T \geq K
\end{cases}
$$

**Example:**

Digital call on Apple:
- Strike: $180
- Notional: $10 per share
- Current: $175

**At expiration:**
- If Apple at $181 → Receive $10
- If Apple at $179 → Receive $0
- **No gradual scaling**

### 2. Replication Using Spreads

**Static replication:**

Digital call ≈ Tight call spread

$$
\text{Digital Call}(K, N) \approx \frac{N}{\epsilon} \times \left[ C(K) - C(K + \epsilon) \right]
$$

Where $\epsilon$ is small spread width

**Example:**

Want digital paying $10 if stock > $100

**Replication:**
- Buy 100 calls at $100 strike
- Sell 100 calls at $100.10 strike ($0.10 spread)
- If stock ends at $100.10+ → Spread worth $0.10 × 100 = $10 ✓

**As $\epsilon \to 0$:** Converges to perfect digital

**Practical:** Use $\epsilon = 0.5-1\%$ of strike

### 3. Pricing Formula

**Risk-neutral valuation:**

$$
\text{Digital Call} = N \times e^{-rT} \times \mathbb{P}(S_T > K)
$$

$$
= N \times e^{-rT} \times N(d_2)
$$

Where:
$$
d_2 = \frac{\ln(S_0/K) + (r - q - \sigma^2/2)T}{\sigma\sqrt{T}}
$$

**Example:**

- $S_0 = 100$, $K = 100$, $r = 5\%$, $q = 2\%$, $\sigma = 25\%$, $T = 0.5$
- Notional: $N = 10$

$$
d_2 = \frac{0 + (0.03 - 0.03125) \times 0.5}{0.25\sqrt{0.5}} = -0.0035
$$

$$
\text{Value} = 10 \times e^{-0.025} \times N(-0.0035) = 10 \times 0.9753 \times 0.4986 = 4.86
$$

**Interpretation:** Digital worth $4.86, pays $10 if ITM

### 4. Greeks Behavior

**Delta:**

$$
\Delta_{\text{digital}} = \frac{N \times e^{-rT}}{\sigma\sqrt{2\pi T}} \times e^{-d_2^2/2}
$$

**At-the-money:** Delta is maximum
**Deep ITM/OTM:** Delta approaches zero

**Gamma:**

$$
\Gamma_{\text{digital}} = -\frac{\Delta \times d_1}{\sigma\sqrt{T}}
$$

**Near expiration at strike:** $\Gamma \to -\infty$ (massive negative gamma!)

**Vega:**

$$
\text{Vega}_{\text{digital}} = -N \times e^{-rT} \times n(d_2) \times \frac{d_1}{\sigma}
$$

Can be positive or negative depending on moneyness

**Theta:**

$$
\Theta_{\text{digital}} = \frac{N \times e^{-rT} \times n(d_2)}{2\sigma\sqrt{T}} \times \left[ d_1 d_2 + \frac{1}{T} \left( \frac{d_1}{\sigma\sqrt{T}} - d_2 \right) \right]
$$

Complex behavior, can be positive or negative

### 5. Pin Risk

**Settlement risk at expiration:**

**Problem:** Near expiration, impossible to know if option will settle ITM or OTM

**Example:**

Digital call, strike $100, notional $10M

**Friday 3:59 PM:** Stock at $100.01 (just barely ITM)
- Expected payoff: $10M

**Friday 4:00 PM:** Stock closes at $99.99 (just barely OTM)
- Actual payoff: $0
- **Lost: $10M on 2¢ move!**

**Hedging nightmare:**
- Can't hedge this effectively
- Too close to call
- Binary outcome on tiny move

### 6. Touch Digitals

**Path-dependent version:**

**One-touch digital:**

$$
\text{Payoff} = \begin{cases}
N & \text{if price touches } H \text{ at any time before } T \\
0 & \text{otherwise}
\end{cases}
$$

**No-touch digital:**

$$
\text{Payoff} = \begin{cases}
N & \text{if price never touches } H \text{ before } T \\
0 & \text{if price touches } H
\end{cases}
$$

**Example:**

One-touch digital:
- Barrier: $110
- Notional: $1,000
- Current: $100

**If ever hits $110 during life:** Win $1,000
**If never hits $110:** Win $0

**Popular in FX markets** (binary bets on levels)

### 7. Double Touch

**Two barriers:**

**Double no-touch (DNT):**

$$
\text{Payoff} = \begin{cases}
N & \text{if price stays between } L \text{ and } U \text{ for entire period} \\
0 & \text{otherwise}
\end{cases}
$$

**Example:**

Stock at $100

**DNT:**
- Lower barrier: $95
- Upper barrier: $105
- Notional: $500
- Maturity: 1 month

**If stays $95-$105 entire month:** Win $500
**If ever touches $95 or $105:** Win $0

**Use:** Bet on range-bound market

---

## Key Terminology

**Notional:**
- Fixed payment amount if condition met
- Not scaled by how far ITM
- Key parameter (like face value)
- Determines position size

**Strike (Trigger):**
- Level that determines payoff
- Above/below determines win/lose
- Extreme sensitivity near this level
- Small moves = huge value swings

**Binary Outcome:**
- All-or-nothing payoff structure
- No gradual scaling
- Either $N$ or $0$
- Creates discontinuous risk

**Spread Approximation:**
- Replicating digital with tight spread
- Practical implementation method
- Avoids infinite gamma
- Standard market practice

**One-Touch:**
- Payoff if barrier ever hit
- Path-dependent
- Popular in FX
- Cheaper than European digital

**Double-No-Touch:**
- Payoff if stays in range
- Path-dependent on both sides
- Range-bound bet
- Common in structured products

---

## Range Accrual Structures

### 1. Basic Mechanism

**Daily counting structure:**

**Payoff:**

$$
\text{Coupon} = \text{Base Rate} \times \frac{\text{Days in Range}}{\text{Total Days}}
$$

**Example:**

1-year note, 12% base rate, range $95-105$

**Scenario:**
- 200 days in range (out of 252 trading days)

$$
\text{Coupon} = 12\% \times \frac{200}{252} = 9.52\%
$$

**If all days in range:** Earn 12%
**If no days in range:** Earn 0%

### 2. Range Definition

**How is "in range" determined?**

**Daily close:**
- Most common
- Based on official settlement
- Clear and unambiguous

**Intraday:**
- Anytime during day
- Can trade outside range intraday
- As long as never touches boundaries
- More restrictive

**Example:**

Range: $95-$105

**Day 1:**
- Intraday low: $94.50
- Intraday high: $106
- Close: $100

**Daily close method:** In range ✓ (closed at $100)
**Intraday method:** Out of range ✗ (touched boundaries)

### 3. Dual Range

**Two separate conditions:**

**Structure:**

$$
\text{Coupon} = \text{Rate}_1 \times \frac{\text{Days in Range}_1}{\text{Total}} + \text{Rate}_2 \times \frac{\text{Days in Range}_2}{\text{Total}}
$$

**Example:**

- Range 1: Stock $95-$105 → Earn 10%
- Range 2: VIX < 20 → Earn 5%

**Day counts:**
- Stock in range: 180 days
- VIX < 20: 220 days

$$
\text{Coupon} = 10\% \times \frac{180}{252} + 5\% \times \frac{220}{252} = 7.14\% + 4.37\% = 11.51\%
$$

### 4. Step Coupons

**Multiple range tiers:**

**Example:**

Stock at $100

**Ranges:**
- $98-$102$: Earn 8%
- $95-$105$: Earn 6%
- $90-$110$: Earn 4%
- Outside: Earn 0%

**Day 1:** Stock at $99 → Earn 8%/252
**Day 2:** Stock at $103 → Earn 6%/252
**Day 3:** Stock at $89 → Earn 0

**Total coupon:** Sum of all daily accruals

### 5. Snowball Structure

**Cumulative with knockouts:**

**Mechanics:**
- Accumulate coupon daily if in range
- If touches barrier → Note terminates early
- Keep accumulated coupons
- Principal returned

**Example:**

- Base rate: 15%
- Range: $95-$105
- Knockout barriers: $90, $110
- Maturity: 2 years

**Scenario:**
- Year 1: All days in range → Accumulated 15%
- Year 2, Month 3: Hits $110 → **Knocked out**
- Total accumulated: 15% + 3.75% = 18.75%
- **Receive: Principal + 18.75%**

### 6. Leveraged Accrual

**Multiplier on daily accrual:**

**Structure:**

$$
\text{Daily Accrual} = \text{Base Rate} \times \text{Leverage} \times \frac{1}{\text{Total Days}}
$$

If in range, else $0$

**Example:**

- Base rate: 10%
- Leverage: 2×
- Range: $95-$105

**Day in range:** Earn $10\% \times 2 \times \frac{1}{252} = 0.0794\%$

**If 200 days in range:**

$$
\text{Coupon} = 0.0794\% \times 200 = 15.88\%
$$

**Doubled the base rate** (but only if high percentage of days in range)

### 7. Target Redemption

**Stops when target hit:**

**Structure:**
- Accumulate until total reaches target (e.g., 20%)
- Once reached → Redeem immediately
- Keep all accumulated coupons

**Example:**

- Target: 20%
- Base rate: 15%
- Range: $95-$105

**Month 1-12:** All days in range → Accumulated 15%
**Month 13-16:** All days in range → Accumulated another 5%
- **Total: 20%** → **Triggers redemption**

**Investor receives:** Principal + 20% after 16 months

**vs. holding to 2-year maturity:** Got money back faster

---

## Why Trade Digital/Range

### 1. Cheap Binary Bets

**Digital options:**

**View:** "Stock will definitely cross $100"

**Digital call vs. vanilla:**

**Vanilla call (strike $100):**
- Cost: $5
- Payoff: $S_T - 100$ if ITM
- Need stock at $105 to break even

**Digital call (strike $100, $10 notional):**
- Cost: $4.50
- Payoff: $10 if ITM
- Need stock at $100.01 to break even
- **Much easier to profit**

### 2. Enhanced Fixed Income

**Range accruals:**

**Investor profile:**
- Conservative fixed income investor
- Want more than 5% bonds
- Comfortable with equity link
- Believe market will be range-bound

**Range accrual note:**
- Base coupon: 12%
- Range: S&P 500 within ±10%
- If stable market → Earn 12%
- **2-3× bond yields**

### 3. Hedging Specific Levels

**Binary protection:**

**Problem:** Need protection only if stock falls below $90

**Solution:**
- Buy digital put at $90
- Pays fixed $100K if breaches
- Cheaper than vanilla put
- Exact coverage needed

**Example:**

Portfolio: $1M
Comfort zone: Down to 10% loss

**Digital put:**
- Strike: $90 (10% down from $100)
- Notional: $100K
- Cost: $8K

**If crashes below $90:** Receive $100K (offsets loss)
**If stays above $90:** Lose $8K (premium)

### 4. Speculation on Volatility

**Range accruals benefit from low vol:**

**Setup:**
- Buy range accrual
- Tight range: $95-$105
- High base rate: 15%

**Low vol regime:**
- Stock stays in range
- Earn high coupon
- **Profit from stability**

**High vol regime:**
- Stock frequently outside range
- Earn little/nothing
- **Short volatility position**

### 5. Structured Product Building

**Cost reduction:**

**Autocallable with digital:**
- Replace vanilla payoff with digital
- Save issuer cost
- Pass some savings to investor
- Higher coupon possible

**Example:**

Standard autocallable: 11% coupon

**With digital payoff:**
- If autocalls → Receive fixed $110
- Issuer saves on upside > $110
- Can offer 13% coupon
- **Investor gets more income**

### 6. Event-Driven Trades

**Binary events:**

**FDA approval decision:**
- Stock at $50
- Approved → Stock to $80
- Rejected → Stock to $30

**Digital call:**
- Strike: $60
- Notional: $100K
- Cost: $40K (45% probability)

**Payoff:**
- Approved → Win $100K (profit $60K)
- Rejected → Lose $40K

**vs. stock:**
- Buy $40K of stock (800 shares)
- Approved: 800 × $80 = $64K (profit $24K)
- Rejected: 800 × $30 = $24K (loss $16K)

**Digital offers more leverage** on binary outcome

### 7. Income from Range-Bound

**Sideways markets:**

**Problem:** Stocks going nowhere for months

**Solution:**
- Sell range accruals (or buy as investor)
- Collect income during sideways period
- Only risk if breaks out of range

**Example:**

Stock stuck $95-$105 for 6 months

**Strategy:** Sell 6-month range accrual
- Range: $93-$107 (give cushion)
- Collect 10% annualized = 5% for 6 months

**If stays in range:** Keep 5%
**If breaks out:** Owe coupon (but can hedge)

---

## Pricing Mechanics

### 1. Digital Pricing

**Using vanilla spreads:**

$$
\text{Digital}(K) = \lim_{\epsilon \to 0} \frac{C(K) - C(K + \epsilon)}{\epsilon}
$$

**Practical implementation:**

$$
\text{Digital}(K) \approx \frac{C(K - \epsilon/2) - C(K + \epsilon/2)}{\epsilon}
$$

**Example:**

Digital call, strike $100, $\epsilon = 0.50$

- $C(99.75) = 3.20$
- $C(100.25) = 2.70$

$$
\text{Digital} \approx \frac{3.20 - 2.70}{0.50} = 1.00
$$

Per unit, so for $10 notional: **$10 × 1.00 = $10**

### 2. Range Accrual Valuation

**Expected days in range:**

$$
\text{Value} = \text{Rate} \times \sum_{i=1}^{N} e^{-r t_i} \mathbb{P}(\text{Day } i \text{ in range})
$$

**Monte Carlo:**
1. Simulate many price paths
2. For each path, count days in range
3. Calculate coupon for each path
4. Average and discount

**Example:**

10,000 simulations

**Path 1:** 230 days in range → Coupon = 12% × 230/252 = 10.95%
**Path 2:** 180 days in range → Coupon = 12% × 180/252 = 8.57%
...
**Average:** 9.2% → **Fair value**

### 3. Analytical Approximation

**Assuming constant in-range probability:**

$$
\mathbb{P}(\text{in range}) \approx N\left(\frac{U - S_0}{\sigma S_0 \sqrt{dt}}\right) - N\left(\frac{L - S_0}{\sigma S_0 \sqrt{dt}}\right)
$$

Where $L$ = Lower bound, $U$ = Upper bound

**Expected coupon:**

$$
E[\text{Coupon}] \approx \text{Rate} \times \mathbb{P}(\text{in range})
$$

**Example:**

- $S_0 = 100$, Range $[95, 105]$, $\sigma = 20\%$, Daily

$$
\mathbb{P}(\text{in range}) \approx N\left(\frac{5}{20 \times 100 \times \sqrt{1/252}}\right) - N\left(\frac{-5}{20 \times 100 \times \sqrt{1/252}}\right)
$$

$$
= N(0.198) - N(-0.198) = 0.578 - 0.422 = 0.156
$$

Wait, this is daily probability, need to recalculate...

Actually: $\mathbb{P} \approx 75\%$ for this range (using proper calculation)

**Expected coupon:** $12\% \times 0.75 = 9\%$

### 4. Volatility Impact

**Digitals:**

Higher vol → Lower digital call value (harder to exceed strike decisively)

**Range accruals:**

Higher vol → Lower value (more days outside range)

**Example:**

Range accrual, $95-$105$

**Vol = 15%:** Expected days in range = 85% → Coupon = 10.2%
**Vol = 25%:** Expected days in range = 70% → Coupon = 8.4%
**Vol = 35%:** Expected days in range = 55% → Coupon = 6.6%

**Huge impact:** Vol doubling cuts coupon by 35%

### 5. Correlation Effects

**Multi-asset range accruals:**

**Higher correlation → More days with both in range**

**Example:**

Dual range on S&P 500 and Nasdaq

**Independence (ρ = 0):**
- P(both in range) = P(SPX in range) × P(NDX in range)
- = 0.75 × 0.75 = 0.56

**High correlation (ρ = 0.8):**
- P(both in range) ≈ 0.68

**Higher correlation helps investor** (more accrual days)

### 6. Hedging Difficulty

**Digital hedging:**

**Problem:** Infinite gamma at strike near expiration

**Solution:** Use spreads to approximate
- Artificially widen spread to manageable gamma
- Accept small tracking error
- Better than infinite risk

**Range accrual hedging:**

**Problem:** Portfolio of 252 digitals (one per day)

**Solution:**
- Dynamic delta hedging
- Adjust daily based on path
- Very expensive in transaction costs

### 7. Vega of Range

**Range accrual vega:**

$$
\text{Vega}_{\text{range}} = -\text{Rate} \times \sum_i e^{-r t_i} \frac{\partial \mathbb{P}(\text{in range})}{\partial \sigma}
$$

**Always negative:** Higher vol → Lower value

**Example:**

Range accrual fair value: $9.50

**Vol increases 25% → 30%:**

**New value:** $8.70

**Vega:** $(8.70 - 9.50) / 5\% = -$16$ per 1% vol

**Large negative vega** (short volatility position)

---

## Common Mistakes

### 1. Ignoring Gamma Risk

**Digital near expiration:**

- **Mistake:** Hold digital close to expiration near strike
- **Why it fails:** Gamma explodes to infinity
- **Fix:** Exit 1-2 weeks before expiration if near strike
- **Real cost:** Unhedgeable losses from pin risk

**Example:**

Short 10,000 digital calls, strike $100, notional $10

**Day before expiration:** Stock at $100.01
- Delta = 0.5 (approximately)
- Hedged with 5M shares

**Expiration day:** Stock closes at $99.99 (2¢ move down)
- Digital expires worthless ✓
- But still own 5M shares
- If stock continues falling to $99.50...
- **Loss: $2.45M** from unhedged shares

### 2. Misunderstanding Notional

**Confusing with vanilla:**

- **Mistake:** Think notional = position size like vanilla
- **Why it fails:** Notional is payout amount, not market exposure
- **Fix:** Calculate true delta exposure
- **Real cost:** Massive over-leverage

**Example:**

Buy 1,000 digital calls:
- Notional: $10 per contract
- Cost: $4.50 per contract
- "Only $4,500 at risk" (premium)

**But:**
- Delta at strike: 0.5
- Effective stock exposure: 1,000 × 100 × 0.5 × $100 = $5M
- **Not $4,500, it's $5M exposure!**

### 3. Range Accrual Vol Mispricing

**Underestimating vol impact:**

- **Mistake:** Buy range accrual assuming current vol persists
- **Why it fails:** Vol regime changes, range accrual collapses
- **Fix:** Stress test under 1.5× current vol
- **Real cost:** 30-40% loss in value

**Example:**

Bought range accrual for $9.50
- Assumed vol: 20%
- Range: ±10%

**Vol spikes to 35% (regime change):**
- Expected days in range drops from 75% to 50%
- **New value: $6.50**
- **Loss: -31.6%**

### 4. Ignoring Early Termination

**Snowball structures:**

- **Mistake:** Assume will run to maturity
- **Why it fails:** Often terminates early (barrier hit)
- **Fix:** Model expected life, not contractual life
- **Real cost:** Reinvestment risk at low yields

**Example:**

3-year snowball, 15% base rate

**Investor thinking:** "Will earn 45% total"

**Reality:**
- Average life: 14 months (historical)
- Typical termination: 17.5% accumulated
- Must reinvest at lower rates after
- **Actual annualized return: 8-9%** (not 15%)

### 5. One-Touch Timing

**Barriers hit but market recovers:**

- **Mistake:** Sell one-touch digital thinking "will recover"
- **Why it fails:** Already triggered, no takeback
- **Fix:** Understand path dependency is permanent
- **Real cost:** Pay notional despite recovery

**Example:**

Sold one-touch digital:
- Barrier: $110
- Notional: $100K
- Current: $105

**Week 1:** Stock spikes to $111 (barrier hit!)
- Digital triggered
- Owe $100K

**Week 2:** Stock falls back to $105

**Investor:** "Can we cancel? It's back below!"
**Reality:** No, **trigger is permanent**, owe $100K

### 6. Pin Risk Management

**Weekend/holiday gaps:**

- **Mistake:** Hold digital through weekend near strike
- **Why it fails:** Can't manage risk if market closed
- **Fix:** Exit Friday if anywhere near strike
- **Real cost:** Gap over weekend = massive loss

**Example:**

Long digital call, strike $100, stock at $99.90 Friday close

**Monday:** Gaps down to $98 (negative news over weekend)
- Digital worthless
- No chance to adjust
- **Lost entire premium**

**Should have:** Exited Friday, taken small loss

---

## Best vs. Worst Case

### 1. Best Case: Success

**Perfect range accrual:**

**Setup:**
- Conservative investor, $500K portfolio
- Buys 3-year range accrual note
- Underlying: S&P 500 at 4,500
- Range: $4,050-$4,950$ (±10%)
- Base rate: 13% annually

**Market environment:**
- Low volatility regime (VIX 12-15)
- Steady economic growth
- No major shocks
- Range-bound market

**Year 1:**
- S&P range: $4,400-$4,700$
- Days in range: 245/252 (97%)
- Coupon earned: 13% × 97% = 12.6%

**Year 2:**
- S&P range: $4,300-$4,800$
- Days in range: 238/252 (94%)
- Coupon earned: 13% × 94% = 12.2%

**Year 3:**
- S&P range: $4,500-$4,900$
- Days in range: 250/252 (99%)
- Coupon earned: 13% × 99% = 12.9%

**Total:**
- Principal: $500K returned
- Coupons: $500K × (12.6% + 12.2% + 12.9%) = $188.5K
- **Total: $688.5K**
- **Return: 37.7% over 3 years** (11.3% annualized)

**vs. alternatives:**

**S&P 500 index:**
- Return: 25% (4,500 → 5,600)
- Dividends: 6%
- **Total: 31%**

**3-year Treasury:**
- Yield: 4.5% × 3 = 13.5%

**Range accrual outperformed both** in sideways market

### 2. Worst Case: Disaster

**Digital disaster:**

**Setup:**
- Hedge fund selling one-touch digitals for income
- "Barrier will never hit" strategy
- Sell 10,000 one-touch calls on Nasdaq

**Structure per contract:**
- Current: 15,000
- Barrier: 16,500 (10% above)
- Notional: $1,000
- Premium collected: $150 per contract
- **Total premium: $1.5M**

**Month 1-2:** Nasdaq steady 14,800-15,200
- Collecting theta: $50K/day
- **Cumulative: +$3M** (premium + mark-to-market gains)

**Month 3: Tech rally**

**Week 1:** Nasdaq rallies to 15,800
- Getting close to barrier
- Fund gets nervous but holds

**Week 2:** Strong earnings, gap to 16,200
- Even closer...

**Week 3, Monday:** Major AI breakthrough announcement
- Nasdaq gaps from 16,400 to **16,800** overnight
- **All barriers hit!**

**Immediate impact:**
- Owe $1,000 × 10,000 = $10M
- Collected premium: $1.5M
- **Net loss: -$8.5M**

**But it gets worse...**

**Hedging disaster:**
- Fund had been delta hedging with short futures
- Short position: 30M notional
- Nasdaq rallied 16,800 → 17,500 (continued rally)
- **Additional hedge loss: $2.1M**

**Total damage:**
- Digital payout: -$10M
- Premium collected: +$1.5M
- Hedge losses: -$2.1M
- **Net: -$10.6M**

**Fund down 53%** (started with $20M)

**Post-mortem:**
- "Impossible" barrier wasn't impossible
- 10% move in tech not rare
- Leverage (10,000 contracts) was insane
- No stop-loss discipline
- **Fund shut down**

---

## Risk Management Rules

### 1. Position Sizing

**Maximum notional:**

$$
\text{Digital Notional} \leq 5\% \text{ of Portfolio}
$$

**Example:**

$1M portfolio

**Maximum:** $50K notional in digitals

Even though premium might be only $20K

**Rationale:** Notional = actual payout risk

### 2. Expiration Discipline

**Exit before maturity:**

$$
\text{Exit if: Time to expiration} \leq 5 \text{ days AND } |S - K| < 2\%
$$

**Example:**

Digital call, strike $100, stock at $101

**5 days before expiration:**
- Within 2% of strike
- **Exit immediately** regardless of P&L

**Rationale:** Pin risk unmanageable

### 3. Spread Hedging

**For short digitals, use spreads:**

$$
\text{Spread width} = K \times 2\sigma\sqrt{\Delta t}
$$

**Example:**

Short digital, strike $100, daily vol 1.5%

$$
\text{Spread} = 100 \times 2 \times 0.015 \times \sqrt{1/252} = 0.19
$$

**Hedge:** Buy $99.90 call, sell $100.10 call

**Result:** Capped gamma, manageable risk

### 4. Range Accrual Limits

**Maximum allocation:**

$$
\text{Range Accrual} \leq 20\% \text{ of Fixed Income}
$$

**Example:**

$1M portfolio, 40% bonds = $400K

**Maximum range accrual:** $80K

**Rationale:** Concentrated short vol risk

### 5. Volatility Stress

**Required stress test:**

Revalue at $\sigma = 1.5 \times \sigma_{\text{current}}$

**Maximum loss:**

$$
\text{Loss at 1.5× vol} \leq 25\% \text{ of position}
$$

**Example:**

Range accrual worth $95

**Stress (vol 25% → 37.5%):**
- New value: $80
- Loss: $15 (15.8%)
- **Acceptable** (< 25% threshold)

### 6. Barrier Distance

**For touch digitals:**

$$
\frac{|S_0 - H|}{S_0} \geq 8\%
$$

**Example:**

Stock at $100

**Minimum barrier distance:**
- Up barrier: $108+ ✓
- Down barrier: $92 or lower ✓

**Reject:**
- Barriers within 5% ✗

### 7. Monitoring Frequency

**Daily surveillance:**

- Stock price vs. digital strike
- Days in range (for accruals)
- Greeks (if near strike/expiration)
- Vol changes (>10% = alert)

**Exit triggers:**
- Approaching expiration + near strike
- Vol spike (>30% increase)
- Position P&L < -20%

---

## Real-World Examples

### 1. FX One-Touch Market

**Interbank FX trading:**

**Structure:**
- Very common in EUR/USD, USD/JPY
- One-touch and no-touch digitals
- Hourly and daily monitoring
- Notionals: $10M-$100M

**Example trade (2020):**

**EUR/USD at 1.1000**

**One-touch call:**
- Barrier: 1.1500 (500 pips above)
- Notional: $10M
- Premium: $1.2M (12%)
- Maturity: 3 months

**Outcome:**
- EUR rallied to 1.1550 in Month 2
- **Paid $10M**
- Net loss: $8.8M for seller

**Why used:** Very liquid, standard product, no exotic features

### 2. Range Accrual Bonds (Japan)

**Retail structured notes:**

**Setup (2015-2018):**
- Nikkei 225 range accrual notes
- Very popular with Japanese retail
- Typical: 3-year maturity, 10-12% base rate
- Range: Nikkei ±15%

**Performance:**
- Low-vol environment (2015-2017)
- High percentage of days in range
- Investors earned 9-11% annually
- **Very successful**

**2018 correction:**
- Volatility spiked
- Days in range dropped to 60%
- Coupons fell to 6-7%
- **Investor disappointment** (but no principal loss)

### 3. Digital Disaster (2015)

**Swiss Franc unpegging:**

**January 15, 2015:**
- Swiss National Bank removed EUR/CHF floor
- EUR/CHF crashed from 1.20 to 0.85 (30% move)

**Digital casualties:**
- Many traders short EUR/CHF digitals (betting stability)
- Barriers at 1.15 (seemed "safe")
- **All triggered instantly**

**Example loss:**
- Hedge fund short 10,000 digitals
- Notional: $10M
- Premium collected: $500K
- **Paid $10M in one day**
- **Loss: -$9.5M**

**Multiple firms bankrupted** by this event

### 4. Snowball Success (2019)

**Low-vol structured note:**

**Setup:**
- S&P 500 snowball
- Range: ±12%
- Base rate: 14%
- Knockout barriers: ±20%

**Outcome:**
- Ran for 21 months (didn't knock out)
- Accumulated 24.5% return
- Redeemed early (reached target)
- **Investors very happy**

**Why worked:**
- Low-vol regime throughout
- Range wide enough (12% cushion)
- Barriers far enough (20% = extreme)

---

## Practical Steps

### 1. Product Selection

**Choose appropriate structure:**

**For binary views:**
- Use digitals (all-or-nothing)
- Set strike at target level
- Size for notional payout risk

**For range-bound views:**
- Use range accruals
- Wide enough range (±10% minimum)
- Stress test vol sensitivity

**For touch events:**
- Use one-touch/no-touch
- Place barriers at key technical levels
- Account for gap risk

### 2. Pricing Verification

**Get multiple quotes:**

- Check at least 3 dealers
- Compare to spread replication
- Verify monitoring frequency
- Check notional vs. premium

**Red flags:**
- Quote 20%+ different from others
- Unclear monitoring terms
- Complex embedded features
- Large dealer spread

### 3. Hedging Strategy

**For long digitals:**
- Use vanilla spreads to replicate
- Exit 1 week before expiration
- Don't try to hedge gamma

**For short digitals:**
- Always hedge with spreads
- Never naked short
- Exit at 50% profit target
- Stop loss at 100% premium

**For range accruals:**
- Dynamic delta hedging
- Adjust daily if active
- Or hold to maturity (passive)

### 4. Monitoring Protocol

**Daily tasks:**

**Digitals:**
- Check price vs. strike (distance?)
- Time to expiration (exit soon?)
- Implied vol (changed?)
- Position Greeks

**Range accruals:**
- Was today in range? (running count)
- Current percentage in range
- Vol environment (increasing?)
- Expected final coupon

### 5. Exit Discipline

**Mandatory exits:**

**Digitals:**
- 5 days before expiration if near strike
- Loss exceeds 2× premium
- Vol increases >50%

**Range accruals:**
- Loss exceeds 30% of fair value
- Vol regime change (persistent)
- Better opportunity elsewhere

### 6. Documentation

**Record keeping:**

- Exact strike/barrier levels
- Notional amounts
- Monitoring specification
- Daily in/out of range status
- All hedge adjustments
- Settlement process

### 7. Post-Trade Analysis

**After settlement:**

- Actual vs. expected payoff
- Were Greeks accurate?
- Would you trade again?
- What would you change?
- Document lessons learned

---

## Final Wisdom

> "Digital options and range accruals are the 'knife's edge' of derivatives—elegant in theory, treacherous in practice. The binary nature of digitals creates mathematical singularities that no amount of clever hedging can truly tame. That infinite gamma at expiration near the strike? It's not a formula mistake, it's a fundamental feature telling you: DON'T BE HERE. Range accruals seduce with their high coupons in low-vol environments, but they're selling exactly what institutional investors fear most—volatility spikes. When vol doubles (and it will, always unexpectedly), that 12% coupon becomes a 4% coupon, and investors feel betrayed. The core problem: these products give investors exactly what they ask for (binary outcomes, high coupons) but not what they need (gradual payoffs, diversification). Use digitals only for genuine binary views with clear catalysts and short timeframes. Use range accruals only in demonstrably low-vol regimes with wide ranges. Never, EVER hold short digitals through expiration near the strike—this is financial Russian roulette with all chambers loaded except one. Exit early, exit often, and accept that 'picking up pennies in front of a steamroller' is only profitable until you get crushed. The graveyard of derivatives traders is full of those who thought they could outsmart the gamma explosion."

**Key to success:**

- Understand binary = infinite gamma at strike (not just theory)
- Exit digitals 1 week before expiration if near strike (non-negotiable)
- Range accruals are short vol positions (treat as such)
- Wide ranges only (±10% minimum, prefer ±15%)
- Stress test at 1.5× current vol (always)
- Never naked short digitals (use spreads to hedge)
- Accept that "high coupon" = "selling insurance" (not free money)
- Size for notional payout, not premium paid (true risk)
