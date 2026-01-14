# Covered Yield Notes


**Covered yield notes** are structured products that combine a bond with a short position in equity options, generating enhanced income through option premium collection while accepting the risk of delivering shares at predetermined levels below current market prices, essentially selling downside insurance to earn above-market yields.

---

## The Core Insight


**The fundamental idea:**

- Investors want higher yields than bonds offer
- Willing to take equity downside risk for extra income
- Structure sells puts on stock/index embedded in note
- Premium from sold puts boosts coupon payments
- If stock falls below barrier, receive shares instead of principal
- Trade-off: Higher yield today for conversion risk tomorrow

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/covered_yield_note_payoff.png?raw=true" alt="covered_yield_note_payoff" width="700">
</p>
**Figure 1:** Covered yield note payoff structure showing enhanced coupon payments in stable markets offset by equity conversion risk if underlying stock falls below the knock-in barrier, combining fixed income and short put exposure.

**You're essentially asking: "How much extra yield do I need to sell downside insurance on stocks?"**

---

## What Are Covered Yield Notes?


### 1. Basic Structure


**Components of the note:**

**Definition:** A covered yield note is a debt instrument where the investor receives enhanced coupons in exchange for accepting potential equity conversion if the underlying stock falls below a barrier level.

**When you buy a covered yield note:**

- Invest principal (e.g., $100K at par)
- Receive high coupons (8-15% annually)
- If stock stays above barrier → Receive all coupons + principal back
- If stock breaches barrier → Receive shares instead of cash principal
- Maturity typically 1-3 years

**Example structure:**

- Principal: $100,000
- Underlying: Apple stock at $180
- Knock-in barrier: $144 (80% of initial price)
- Coupon: 12% per year ($12,000 annually)
- Maturity: 2 years

### 2. Payoff at Maturity


**Two scenarios:**

**Scenario 1: Stock never touched barrier ($144)**

- Receive: All coupons ($12K + $12K = $24K)
- Receive: Principal ($100K)
- **Total: $124K (24% total return over 2 years)**

**Scenario 2: Stock touched barrier at any point**

- Receive: All coupons ($12K + $12K = $24K)
- Receive: Apple shares worth current market value
- Number of shares: $100K / $180 = 555.56 shares

**If Apple ends at $150:**
- Share value: 555.56 × $150 = $83,340
- Plus coupons: $24K
- **Total: $107,340 (7.34% total return)**

**If Apple ends at $120:**
- Share value: 555.56 × $120 = $66,667
- Plus coupons: $24K
- **Total: $90,667 (-9.33% loss)**

### 3. Decomposition


**Equivalent portfolio:**

Covered yield note = Zero-coupon bond + Short put option

$$
\text{CYN} = \text{Bond} - \text{Put}(K = \$144)
$$

**Formal payoff:**

$$
V_T = \begin{cases}
\$100K + \sum \text{Coupons} & \text{if } \min_{0 \leq t \leq T} S_t \geq \$144 \\
S_T \times \frac{\$100K}{S_0} + \sum \text{Coupons} & \text{if } \min_{0 \leq t \leq T} S_t < \$144
\end{cases}
$$

**Translation:**
- Upper payoff: Bond with enhanced coupons (from put premium)
- Lower payoff: Physical settlement of short put + coupons

### 4. Risk-Return Profile


**Return decomposition:**

$$
\text{Total Return} = \text{Coupon Income} + \text{Principal Return}
$$

$$
\text{Principal Return} = \begin{cases}
0\% & \text{(barrier not hit)} \\
\frac{S_T - S_0}{S_0} & \text{(barrier hit)}
\end{cases}
$$

**Example returns:**

**No barrier breach:**
- Coupon: 12% × 2 years = 24%
- Principal: 0%
- **Total: 24% (12% annualized)**

**Barrier breached, stock -10%:**
- Coupon: 24%
- Principal: -10%
- **Total: 14% (7% annualized)**

**Barrier breached, stock -30%:**
- Coupon: 24%
- Principal: -30%
- **Total: -6% (-3% annualized)**

### 5. Knock-In Barrier


**Critical feature:**

**Definition:** Price level that, if breached at ANY point during the note's life, triggers equity conversion at maturity (assuming stock still below initial level).

**Barrier types:**

**American barrier (continuous monitoring):**
- Checks every instant (theoretical)
- Higher knock-in probability
- Lower coupon (more risky for investor)
- Rarely used in practice

**European barrier (at maturity only):**
- Checks only at final maturity
- Lower knock-in probability
- Higher coupon (less risky for investor)
- Sometimes used (simplest structure)

**Discrete barrier (common):**
- Checks at specific dates (daily closes, monthly, etc.)
- Most practical for real products
- Daily monitoring most common
- Moderate coupon level

**Example:**

Stock at $100, barrier at $80

**Continuous monitoring:**
- Intraday spike to $79 → Triggered!
- Coupon: 10%

**Daily monitoring:**
- Intraday spike to $79, but closes at $81 → Safe
- Only breaches if daily close ≤ $80
- Coupon: 11% (higher due to lower risk)

**Monthly monitoring:**
- Only checks monthly close
- Even lower trigger probability
- Coupon: 12% (highest)

### 6. Coupon Enhancement


**Where does extra yield come from?**

**Short put premium:**

$$
\text{Enhanced Coupon} = \text{Risk-Free Rate} + \text{Put Premium}
$$

**Example calculation:**

- Risk-free rate: 4%
- Put premium (2-year, 80% strike): 8%
- **Total coupon: 12%**

**Formal pricing:**

$$
\text{Note Value} = B(0,T) \times \$100K + \sum_{i=1}^{N} B(0,t_i) \times C_i - P_{\text{knock-in}}
$$

Where:
- $B(0,T)$ = Discount factor to maturity
- $C_i$ = Coupon payment at time $t_i$
- $P_{\text{knock-in}}$ = Value of knock-in put option

### 7. Volatility Impact


**Higher vol = higher coupon:**

**Put option value increases with volatility:**

$$
\text{Put Value} \propto \sigma
$$

**Example:**

Stock at $100, barrier at $80, 2 years

**Low vol (σ = 15%):**
- Put premium: 5%
- Coupon: 4% + 5% = **9%**

**Medium vol (σ = 25%):**
- Put premium: 9%
- Coupon: 4% + 9% = **13%**

**High vol (σ = 40%):**
- Put premium: 15%
- Coupon: 4% + 15% = **19%**

**Implication:** Covered yield notes on volatile stocks offer higher coupons but higher conversion risk.

---

## Key Terminology


**Knock-In Level:**
- Barrier that triggers conversion feature
- Usually 70-85% of initial stock price
- Once breached, note converts to equity
- Monitoring frequency matters (daily, weekly, etc.)

**Physical Settlement:**
- Delivery of actual shares at maturity
- Number of shares = Principal / Initial Stock Price
- Investor becomes shareholder
- Can hold or sell shares immediately

**Memory Feature:**
- Once barrier breached, conversion is locked
- Even if stock recovers above barrier
- Path-dependent outcome
- Permanent trigger (no "healing")

**Contingent Coupon:**
- Some structures only pay coupon if no breach
- Higher coupon rate than fixed coupons
- Higher risk for investor
- Less common than fixed coupons

**Worst-Of Structure:**
- Multiple underlyings (e.g., 3 stocks)
- Barrier based on worst performer
- Higher coupon (more risk)
- Complex correlation effects

**Issuer Credit:**
- Note is unsecured debt of issuer
- Investor has credit risk to bank/issuer
- Different from owning stock directly
- Check issuer rating (A or better)

---

## Why Investors Buy


### 1. Income Generation


**Seeking yield in low-rate environment:**

**Example:**

Capital: $100,000

**Traditional fixed income:**
- 10-year Treasury: 4.5%
- Corporate bond (A-rated): 5.5%
- **Annual income: $5,500**

**Covered yield note:**
- Stock: S&P 500 at 4,500
- Barrier: 3,600 (80%)
- Coupon: 11%
- **Annual income: $11,000** (double!)

**Trade-off:**
- Get 2× the income
- But risk equity conversion
- Appropriate if bullish or neutral on market

### 2. Bullish Outlook


**Conviction stock won't crash:**

**Investor view:**
- "Apple won't fall 20% in next 2 years"
- Comfortable owning Apple at $144 (vs. $180 today)
- Essentially want to buy Apple at discount with paid waiting time

**Structure fits view:**
- Barrier at $144 (20% cushion)
- If hit, get Apple shares at $180 cost basis
- 12% coupons while waiting
- **Like getting paid to place a limit order**

### 3. Neutral Positioning


**Range-bound market view:**

**Setup:**
- Expect S&P 500 to trade $4,000-$5,000 for 2 years
- Don't expect big crash or big rally
- Want income during sideways period

**Covered yield note:**
- Barrier at $3,200 (20% below)
- Provides income during range-bound period
- Only risk if major bear market
- Fits neutral-to-bullish view perfectly

### 4. Strategic Positioning


**Want to own stock at lower price:**

**Example:**

Want to buy Tesla at $200 (current: $250)

**Traditional approach:**
- Place limit order at $200
- Miss out if never touches $200
- Earn zero while waiting

**Covered yield note approach:**
- Buy CYN with $200 barrier ($250 current)
- Earn 10% coupon while waiting
- If hits $200, get Tesla shares automatically
- If never hits, keep principal + coupons
- **Win-win: Income + potential entry**

### 5. Leveraged Yield


**Boost income on portfolio:**

**Setup:**
- Portfolio: $1M, allocated 60% equity / 40% bonds
- Bond allocation: $400K earning 5% = $20K

**Replace with covered yield notes:**
- Same $400K, but CYNs yielding 12%
- **Income: $48K (2.4× increase)**

**Risk:**
- Bond allocation now has equity risk
- But equity risk is to downside only (70-80% barriers)
- Portfolio becomes 60% equity + 40% equity-linked notes
- Effectively ~70% equity risk for ~80% equity return

### 6. Tax Considerations


**Coupon treatment:**

**US tax (simplified):**
- Coupons taxed as ordinary income
- If converted to shares, capital gain treatment at sale
- Holding period starts at conversion date
- Potential for lower long-term capital gains rate

**Example:**

Investor in 35% tax bracket

**Coupon: $12,000 per year**
- Tax: $4,200 (35%)
- After-tax: $7,800

**vs. dividend from stock: $4,000**
- Tax: $600 (15% qualified dividend rate)
- After-tax: $3,400

**Trade-off:** Higher income but higher tax rate

### 7. Portfolio Diversification


**Uncorrelated income source:**

**Within fixed income:**
- Traditional bonds: Sensitive to rates
- Covered yield notes: Sensitive to equity vol + credit
- Different risk factors
- Can diversify fixed income allocation

**Example portfolio:**
- 20% Treasuries (duration risk)
- 20% Corporate bonds (credit risk)
- 20% Covered yield notes (equity risk + credit risk)
- Different risk sources, potentially lower correlation

---

## Pricing & Valuation


### 1. Put Premium Calculation


**Black-Scholes for the embedded put:**

$$
P = K e^{-rT} N(-d_2) - S_0 N(-d_1)
$$

Where:
$$
\begin{align*}
d_1 &= \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}} \\
d_2 &= d_1 - \sigma\sqrt{T}
\end{align*}
$$

**Knock-in adjustment:**

For down-and-in put:

$$
P_{\text{DI}} = P_{\text{vanilla}} - P_{\text{down-and-out}}
$$

**Example:**

- $S_0 = \$180$ (Apple)
- $K = \$180$ (strike = initial price)
- $H = \$144$ (barrier, 80%)
- $r = 4\%$
- $\sigma = 30\%$
- $T = 2$ years

**Vanilla put:** $P_{\text{vanilla}} = \$24.50$ (13.6%)

**Down-and-out put:** $P_{\text{DO}} = \$10.20$ (5.7%)

**Down-and-in put:** $P_{\text{DI}} = \$14.30$ (7.9%)

**Coupon calculation:**

$$
\text{Annual Coupon} = r + \frac{P_{\text{DI}}}{T} = 4\% + \frac{7.9\%}{2} = 7.95\% \approx 8\%
$$

### 2. Break-Even Analysis


**At what final price do you break even?**

$$
\text{Break-even: } S_T = S_0 \left(1 - \frac{\sum \text{Coupons}}{\text{Principal}}\right)
$$

**Example:**

- Initial price: $180
- Total coupons: 8% × 2 = 16%
- Break-even: $180 × (1 - 0.16) = $151.20

**Interpretation:** Stock can fall 16% and investor still breaks even (coupons offset loss).

### 3. Probability Estimation


**Chance of knock-in:**

Using Black-Scholes framework:

$$
\mathbb{P}(\text{knock-in}) = N\left(\frac{\ln(H/S_0) + (r - \sigma^2/2)T}{\sigma\sqrt{T}}\right) + \left(\frac{H}{S_0}\right)^{2r/\sigma^2} N\left(\frac{\ln(H/S_0) - (r - \sigma^2/2)T}{\sigma\sqrt{T}}\right)
$$

**Example:**

- $S_0 = \$180$, $H = \$144$, $r = 4\%$, $\sigma = 30\%$, $T = 2$
- **P(knock-in) ≈ 22%**

**Interpretation:** Roughly 1-in-5 chance of conversion.

### 4. Expected Return


**Probability-weighted outcomes:**

$$
E[R] = (1 - p) \times R_{\text{no breach}} + p \times E[R_{\text{breach}}]
$$

Where:
- $p$ = Probability of knock-in
- $R_{\text{no breach}}$ = Coupon return (known)
- $E[R_{\text{breach}}]$ = Expected return if breached (depends on final $S_T$)

**Example:**

- P(knock-in) = 22%
- Return if no breach: 16% (2 years of 8% coupons)
- Expected stock return if breach: -10% (conditional on hitting $144)
- Expected total return if breach: 16% - 10% = 6%

$$
E[R] = 0.78 \times 16\% + 0.22 \times 6\% = 12.48\% + 1.32\% = 13.8\%
$$

**vs. expected stock return: ~10%**

### 5. Volatility Surface Impact


**Real markets have volatility skew:**

**Put options are more expensive than Black-Scholes suggests:**
- Implied vol for OTM puts higher than ATM
- Reflects crash risk (fat left tail)
- Covered yield notes benefit (short put = receive higher premium)

**Example:**

Black-Scholes (flat vol = 25%): Put premium = 7%

**Market (skew: OTM put vol = 32%):** Put premium = 10%

**Coupon impact:** 4% + 10%/2 = **9%** (vs. 7.5% with flat vol)

**Implication:** Real-world coupons higher than theory due to skew.

### 6. Credit Spread


**Issuer credit affects pricing:**

$$
\text{Note Value} = \text{Bond Component} + \text{Option Component}
$$

$$
\text{Bond Component} = \sum B(0, t_i; r + s) \times C_i + B(0,T; r+s) \times \text{Principal}
$$

Where $s$ = Credit spread of issuer

**Example:**

Issuer: BBB-rated bank, credit spread = 150 bps

**Risk-free note value:** $100
**With credit risk:** Value drops to $97

**Adjustment:** Increase coupon by 1% to compensate for credit risk.

### 7. Comparison to Stock


**Risk-adjusted return:**

**Buy stock directly:**
- Cost: $180
- Expected return: 10%
- Volatility: 30%
- Sharpe ratio: (10% - 4%) / 30% = 0.20

**Buy covered yield note:**
- Cost: $100K (same exposure via shares if converted)
- Expected return: 13.8% (from earlier calc)
- Volatility: ~20% (lower due to coupon cushion)
- Sharpe ratio: (13.8% - 4%) / 20% = 0.49

**Note appears better risk-adjusted**, but:
- Issuer credit risk not captured in vol
- Liquidity worse (can't sell easily)
- Path-dependent (barrier feature)

---

## Common Mistakes


### 1. Ignoring Issuer Credit


**Treating as risk-free:**

- **Mistake:** Focus only on equity risk, ignore issuer credit
- **Why it fails:** If issuer defaults, lose everything (not just equity conversion)
- **Fix:** Check issuer credit rating, diversify across issuers
- **Real cost:** Lehman-issued notes in 2008 became worthless

**Example:**

2008 Financial Crisis:

**Covered yield note:**
- Issuer: Lehman Brothers
- Underlying: S&P 500 (stayed above barrier!)
- Investor expected: Get principal + coupons back

**Reality:**
- Lehman bankrupt in September 2008
- Note became unsecured claim in bankruptcy
- Investors received ~8¢ on the dollar
- **Lost 92% despite equity never breaching barrier**

**Lesson:** Issuer credit risk can exceed equity risk!

### 2. Misunderstanding Memory


**Thinking barrier "heals":**

- **Mistake:** Believe if stock recovers above barrier, conversion canceled
- **Why it fails:** Knock-in is permanent (path-dependent!)
- **Fix:** Understand once breached, conversion is locked
- **Real cost:** Surprised by equity delivery despite recovery

**Example:**

Stock path: $180 → $140 → $175

**Investor thinking:**
- "Stock briefly dipped to $140, but recovered to $175"
- "Should get principal back, right?"

**Reality:**
- Barrier at $144 was breached at $140
- Conversion locked in (memory)
- At maturity, receive 555 shares worth $175 each = $97,222
- **Lost $2,778** vs. principal (despite stock only -2.8%)

### 3. Dividend Oversight


**Forgetting dividend impact:**

- **Mistake:** Price note ignoring dividend yield
- **Why it fails:** Dividends reduce stock drift, affect put value
- **Fix:** Adjust Black-Scholes for dividend yield $q$
- **Real cost:** Overpay for note if dividends ignored

**Adjusted formula:**

$$
d_1 = \frac{\ln(S_0/K) + (r - q + \sigma^2/2)T}{\sigma\sqrt{T}}
$$

**Example:**

Stock at $180, dividend yield = 2%

**Without dividend adjustment:**
- Put premium: 8%
- Coupon: 8% + 4% = 12%

**With dividend adjustment:**
- Put premium: 6.5%
- Coupon: 6.5% + 4% = 10.5%

**Error:** Note should pay 10.5%, not 12%

**If investor pays par for 12% coupon:** Overpaid by ~1.5% annually

### 4. Liquidity Assumption


**Treating as liquid:**

- **Mistake:** Buy note assuming can sell anytime at fair value
- **Why it fails:** Secondary market is thin, bid-ask spreads wide
- **Fix:** Plan to hold to maturity, or accept 5-10% haircut to exit early
- **Real cost:** Forced sale at 85¢ on the dollar

**Example:**

Investor buys $100K note, needs cash 6 months later

**Attempt to sell:**
- Fair value: $103K (earned 6 months of coupons)
- Bid from dealer: $92K (10% haircut)
- **Liquidity cost: $11K (11%)**

**Alternatives:**
- Hold to maturity (if possible)
- Use note as collateral for loan (if issuer permits)

### 5. Worst-Of Correlation


**Underestimating worst-of risk:**

- **Mistake:** Buy worst-of note thinking diversification helps
- **Why it fails:** In crashes, correlation → 1, all stocks fall together
- **Fix:** Stress test under high-correlation scenarios
- **Real cost:** Multiple underlying doesn't reduce risk as much as expected

**Example:**

**Worst-of note on 3 tech stocks:**
- Apple, Microsoft, Google
- Barrier: 70% for each
- Coupon: 15% (vs. 10% single-stock note)

**Normal times (correlation = 0.6):**
- P(worst breaches) = 18%
- Seems reasonable

**Crisis (correlation = 0.95):**
- P(worst breaches) = 35%
- **Almost double the risk!**

**Lesson:** Extra 5% coupon doesn't compensate for doubling of risk in stress.

### 6. Reinvestment Timing


**Poor timing of reinvestment:**

- **Mistake:** Buy covered yield note at market highs
- **Why it fails:** Barrier is % from initial price (high initial = high barrier = more risk)
- **Fix:** Buy when market is mid-range or after correction
- **Real cost:** Higher knock-in probability, worse risk-reward

**Example:**

**Buy at market high:**
- S&P 500 at 5,000 (peak)
- Barrier at 4,000 (80%)
- If market corrects 25% to 3,750 → Knocked in

**Buy after correction:**
- S&P 500 at 4,000 (after 20% correction)
- Barrier at 3,200 (80%)
- Same 25% decline: 4,000 → 3,000 → Still safe!

**Better entry point = better risk-reward**

---

## Best vs. Worst Case


### 1. Best Case: Success


**Perfect environment:**

**Setup:**
- Investor buys $250K covered yield note
- Underlying: S&P 500 at 4,500
- Barrier: 3,600 (20% down)
- Coupon: 10% annually
- Maturity: 2 years

**Market environment:**
- Low volatility regime (VIX around 12-15)
- Steady bull market
- No major corrections

**Year 1:**
- S&P 500: 4,500 → 4,950 (10% gain)
- Never approached barrier
- Coupon received: $25K

**Year 2:**
- S&P 500: 4,950 → 5,200 (5% gain)
- Still far above barrier
- Coupon received: $25K

**Maturity:**
- Barrier never breached
- Receive: Principal $250K + Coupons $50K
- **Total: $300K**
- **Return: 20% over 2 years (9.5% annualized)**

**vs. alternatives:**

**S&P 500 index:**
- Return: 15.5% (4,500 → 5,200)
- Dividends: ~4% (2% × 2 years)
- **Total: 19.5%**

**2-year Treasury:**
- Yield: 4.5%
- **Total: 9%**

**Covered yield note:**
- **Outperformed Treasury by 11%**
- **Matched equity with less volatility**
- **Success!**

### 2. Worst Case: Disaster


**Crash scenario:**

**Setup:**
- Investor buys $500K covered yield note
- Underlying: Bank stock at $100
- Barrier: $75 (25% down)
- Coupon: 13% annually
- Maturity: 3 years
- Issued: Late 2007 (before crisis!)

**Year 1 (2008): Financial Crisis**

**Q1-Q2 2008:**
- Stock: $100 → $85 (still above $75)
- Market volatility spiking
- Coupon received: $65K

**Q3 2008: Lehman collapse**
- Stock crashes: $85 → $55 (**barrier breached**)
- Conversion locked in
- Market panic

**Year 2 (2009): Bottom**
- Stock falls further: $55 → $25 (75% down from initial!)
- Coupon received: $65K (at least still paying)

**Year 3 (2010): Recovery**
- Stock recovers: $25 → $45 (still 55% below initial)
- Coupon received: $65K

**Maturity:**
- Total coupons: $195K (13% × 3 years = 39%)
- Principal: 5,000 shares (500K / 100) × $45 = $225K
- **Total: $420K** (started with $500K)
- **Loss: -$80K (-16%)**

**vs. alternatives:**

**Held stock directly:**
- Return: $100 → $45 (-55%)
- Dividends: ~9% (suspended in 2009, but some received)
- **Total: -46%**

**Stayed in Treasuries:**
- Yield: ~4% × 3 = 12%
- **Total: +12%**

**Analysis:**
- Note better than stock (-16% vs. -46%)
- But devastated vs. safe Treasuries
- High coupon didn't compensate for equity crash
- **Lesson: Covered yield notes don't protect in crashes**

**Even worse scenario:**
- If issuer was also bank (Lehman, Bear Stearns)
- Note became worthless (issuer bankrupt)
- Lost 100% despite stock recovering
- **Double whammy: equity risk + credit risk**

---

## Risk Management Rules


### 1. Position Sizing


**Maximum allocation:**

$$
\text{Max CYN allocation} = \min(20\% \text{ of fixed income}, 10\% \text{ of total portfolio})
$$

**Example:**

$1M portfolio: 60% equity, 40% bonds

**Maximum covered yield notes:**
- 20% of bonds = 20% × $400K = $80K
- 10% of total = $100K
- **Limit: $80K** (take minimum)

**Rationale:**
- Treats CYN as equity-like risk within bond allocation
- Limits total equity exposure (direct + via notes)

### 2. Diversification


**Spread across issuers and underlyings:**

**Rules:**
- Maximum 25% in single issuer
- Maximum 25% on single underlying
- Minimum 4 different issuers
- Minimum 3 different underlyings

**Example $400K allocation:**
- 4 notes × $100K each
- 4 different banks (A-rated or better)
- Underlyings: S&P 500, Apple, Microsoft, Google
- No concentration risk

### 3. Barrier Cushion


**Require minimum barrier distance:**

$$
\text{Minimum cushion} = \frac{S_0 - H}{S_0} \geq 20\%
$$

**Example:**

Stock at $100

**Acceptable:**
- Barrier at $80 (20% cushion) ✓
- Barrier at $75 (25% cushion) ✓

**Reject:**
- Barrier at $85 (15% cushion) ✗
- Barrier at $90 (10% cushion) ✗

**Rationale:** Need meaningful buffer for normal volatility.

### 4. Credit Quality


**Minimum issuer rating:**

$$
\text{Issuer rating} \geq \text{A-}
$$

**Watch list:**
- Monitor issuer CDS spreads monthly
- If CDS > 200 bps → Review position
- If rating downgraded to BBB+ → Consider exit
- If rating falls to BBB → Mandatory exit

**Example:**

- Bought note from Bank A (A+ rated)
- 6 months later: Rating cut to BBB+
- CDS spreads widen to 180 bps
- **Action: Sell note (even at loss) to avoid credit risk**

### 5. Maturity Ladder


**Stagger maturities:**

**Structure:**
- Year 1: $100K matures
- Year 2: $150K matures
- Year 3: $150K matures

**Benefits:**
- Regular liquidity events
- Reinvestment opportunities
- Reduce interest rate risk
- Can reassess market conditions yearly

### 6. Stress Testing


**Required scenarios:**

1. **-20% equity correction**
   - Does barrier hold?
   - What's expected return?
   - Still acceptable?

2. **-40% equity crash**
   - How much loss including coupons?
   - Can portfolio tolerate this?
   - Credit risk of issuer in stress?

3. **Issuer downgrade**
   - Exit cost if need to sell?
   - Alternative issuers available?
   - Portfolio impact?

**Example:**

$100K note, 10% coupon, 2 years, barrier at 80%

**Stress 1 (-20% equity):**
- Barrier breached (100 → 80)
- Final value: 80% × $100K + $20K = $100K
- **Return: 0% (break-even)**
- Acceptable? Yes

**Stress 2 (-40% equity):**
- Barrier breached
- Final value: 60% × $100K + $20K = $80K
- **Return: -20%**
- Acceptable? Depends on risk tolerance

---

## Real-World Examples


### 1. Bank of America 2010s


**Popular issuance:**

**Program:**
- Issuer: Bank of America (AA- rated)
- Offered dozens of covered yield notes
- Typical underlying: S&P 500, Dow Jones, single stocks
- Coupons: 8-12% annually
- Maturities: 1-3 years

**Example note (2015):**
- Underlying: S&P 500 at 2,100
- Barrier: 1,680 (20% down)
- Coupon: 9% annually
- Maturity: 2 years

**Outcome (2017):**
- S&P 500 at 2,400 (rally!)
- Barrier never approached
- Investors received: Principal + 18% coupons
- **Very successful for investors**

**Why it worked:**
- Bull market 2015-2017
- Low volatility (no big corrections)
- Strong issuer credit
- Appropriate barrier cushion

### 2. Worst-Of Disaster (2008)


**Complex structure gone wrong:**

**Setup:**
- Issuer: Major European bank
- Underlying: Worst of 3 banks (Citi, JPM, WFC)
- Initial: All around $50
- Barrier: $37.50 (25% down)
- Coupon: 15% annually
- Maturity: 3 years
- Issued: January 2008

**Year 1 (2008):**
- All banks crashed in financial crisis
- Citi: $50 → $15 (70% down - **breached**)
- JPM: $50 → $25 (50% down - **breached**)
- WFC: $50 → $20 (60% down - **breached**)
- Coupon paid: $15K

**Maturity (2011):**
- Citi: $45 (recovered, but originally knocked in)
- Conversion: Receive Citi shares at $50 basis
- 2,000 shares × $45 = $90K
- Plus coupons: $45K (15% × 3)
- **Total: $135K (vs. $100K invested)**

**Wait, profit?**

**But many investors:**
- Panicked and sold in 2009 when Citi at $15
- Received 60-70¢ on dollar in secondary market
- **Actually lost 30-40%**

**Lesson:** Need strong hands to hold through crisis, even with high coupons.

### 3. Apple Success (2016-2019)


**Single-stock note:**

**Setup:**
- Underlying: Apple at $100
- Barrier: $70 (30% down)
- Coupon: 8%
- Maturity: 3 years

**Path:**
- Year 1: $100 → $150 (50% rally!)
- Year 2: $150 → $170 (continued rally)
- Year 3: $170 → $200 (another rally)
- Barrier never remotely approached

**Outcome:**
- Coupons: 8% × 3 = 24%
- Principal: Returned 100%
- **Total: 124% (7.4% annualized)**

**vs. owning Apple stock:**
- Return: 100% (doubled)
- Dividends: ~3%
- **Total: 103%**

**Analysis:**
- Note underperformed stock (24% vs. 103%)
- But provided income + principal safety
- Trade-off: Gave up upside for guaranteed income
- Appropriate for conservative investor

### 4. Oil Crash (2014-2016)


**Energy sector note disaster:**

**Setup:**
- Underlying: Exxon at $100
- Barrier: $75 (25% down)
- Coupon: 11%
- Maturity: 2 years
- Issued: Mid-2014

**Oil crash:**
- Oil: $100/barrel → $30/barrel (70% crash)
- Exxon: $100 → $70 (**barrier breached**)

**Maturity (2016):**
- Exxon at $80 (recovered somewhat)
- Shares: 1,000 × $80 = $80K
- Coupons: $22K
- **Total: $102K (+2%)**

**Investor reaction:**
- "Only 2% return over 2 years?"
- "Should have stayed in bonds!"
- Disappointed but not devastated

**Lesson:**
- Sector concentration risk
- Commodity-linked stocks are volatile
- High coupon appropriate (compensated for risk)

---

## Practical Steps


### 1. Initial Assessment


**Is this product right for you?**

**Checklist:**
- [ ] Understand equity downside risk
- [ ] Can hold to maturity (liquidity OK)
- [ ] Bullish/neutral on underlying
- [ ] Comfortable owning stock at barrier price
- [ ] Issuer credit risk acceptable
- [ ] Enhanced yield justifies risks

**If all checked → Proceed**

### 2. Product Selection


**Screening criteria:**

1. **Issuer credit:**
   - Rating ≥ A-
   - CDS < 150 bps
   - Stable outlook

2. **Underlying:**
   - Liquid stock/index
   - Understand business/index
   - Comfortable owning long-term

3. **Barrier:**
   - Cushion ≥ 20%
   - Below major support levels
   - Stress test: OK with 30% drop?

4. **Coupon:**
   - Competitive with market
   - Fair value (use pricing model)
   - Tax treatment understood

5. **Maturity:**
   - Fits investment horizon
   - 1-3 years optimal
   - Not too short (<6 months) or long (>5 years)

### 3. Due Diligence


**Before investing:**

**Read offering documents:**
- Full prospectus (not just term sheet)
- Understand all terms and conditions
- Barrier monitoring frequency
- Settlement procedures
- Early redemption features (if any)

**Model the payoffs:**
- Best case (no breach)
- Base case (breach, moderate loss)
- Worst case (breach, severe loss)
- Break-even price
- Probability analysis

**Compare alternatives:**
- Direct stock purchase
- Traditional bonds
- Covered call strategy
- Other structured products

### 4. Execution


**Placing the order:**

**Primary market:**
- Buy from issuer at launch
- Typically at par (no markup)
- Better pricing than secondary
- Lock in terms at issuance

**Secondary market:**
- Buy from dealer inventory
- Bid-ask spread: 2-5%
- Check fair value (don't overpay)
- Verify issuer credit hasn't deteriorated

**Size appropriately:**
- Start with smaller position (5-10% of allocation)
- Scale up if comfortable and successful
- Don't overconcentrate in single note

### 5. Monitoring


**Ongoing surveillance:**

**Monthly:**
- Stock price vs. barrier (how close?)
- Issuer credit (CDS, rating)
- Market conditions (volatility, rates)
- Accrued coupons

**Quarterly:**
- Full revaluation (mark-to-market)
- Compare to initial projections
- Stress test under current conditions
- Review continued appropriateness

**Event-driven:**
- Barrier approach (within 10%)
- Issuer downgrade
- Major market stress
- Dividend changes (underlying)

### 6. Exit Strategy


**When to exit early:**

**Sell if:**
- Issuer credit deteriorates (downgrade to BBB or worse)
- Stock approaching barrier (within 5-10%)
- Need liquidity urgently
- Better opportunity elsewhere
- Investment thesis invalidated

**Hold if:**
- Issuer credit stable
- Stock well above barrier
- Earning attractive coupons
- No liquidity need
- Still fits portfolio objectives

**At maturity:**
- If no breach: Receive principal + final coupon
- If breach: Receive shares + final coupon
  - Decide: Hold shares or sell immediately?
  - Consider tax implications
  - Evaluate stock outlook

---

## Final Wisdom


> "Covered yield notes are the siren song of structured products—the high coupon beckons, but the rocks of equity risk and credit risk lie beneath. They're not bad products, but they're often misused by investors chasing yield without understanding the risks. The coupon is NOT free money—it's compensation for selling downside insurance on stocks and taking credit risk on the issuer. Use covered yield notes when you have a clear bullish view, when you'd be happy to own the underlying stock at the barrier price, and when you've diversified across multiple issuers and underlyings. Never allocate more than 10-20% of your fixed income to these structures. And always remember: in a real crisis, both the equity risk and credit risk can materialize simultaneously, turning your 'enhanced yield' into an actual loss. The best time to buy covered yield notes is when coupons are high (high volatility) but you have conviction the market won't crash. The worst time is when everyone else is buying them (complacency, peak markets). Be contrarian, be diversified, and always know your exit strategy."

**Key to success:**

- Treat as equity substitute, not bond substitute (despite the coupons)
- Diversify across issuers, underlyings, maturities
- Monitor issuer credit religiously (it matters more than you think)
- Understand barrier is permanent (path-dependent, no healing)
- Size appropriately (10-20% of fixed income maximum)
- Stress test under realistic scenarios (-30% stock, issuer downgrade)
- Have exit plan (don't assume hold-to-maturity)
