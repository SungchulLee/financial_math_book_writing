# Reverse Convertibles

**Reverse convertible notes** are short-term structured products that pay enhanced coupons in exchange for investors selling put options on underlying stocks, where investors receive either cash principal (if stock stays above strike) or physical shares (if stock falls below strike), converting from bond to equity in the downside scenario—the "reverse" of traditional convertible bonds that give investors upside equity participation.

---

## The Core Insight

**The fundamental idea:**

- Traditional convertible: Bond converts to equity if stock RISES (upside)
- Reverse convertible: Bond converts to equity if stock FALLS (downside)
- Investor is short a put option embedded in the note
- Premium from put sold creates enhanced coupon
- Keep premium regardless of outcome
- But risk receiving shares below current market

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/reverse_convertible_structure.png?raw=true" alt="reverse_convertible_structure" width="700">
</p>
**Figure 1:** Reverse convertible structure showing the inverse relationship to traditional convertibles, where downside equity conversion replaces fixed principal repayment, with enhanced coupons compensating for embedded short put exposure.

**You're essentially asking: "How much income do I need to accept shares if stock falls X%?"**

---

## What Are Reverse Convertibles?

### 1. Basic Structure

**Core components:**

**Definition:** A reverse convertible is a debt instrument that pays high coupons but may repay principal in the form of depreciated shares if the underlying stock falls below the strike price, effectively embedding a cash-secured short put position within a bond structure.

**When you buy a reverse convertible:**

- Invest principal (e.g., $100K)
- Receive enhanced coupons (10-25% annually)
- Short maturity (3-12 months typical)
- At maturity, ONE of two outcomes:
  - Stock ≥ Strike → Get 100% cash principal
  - Stock < Strike → Get shares worth less than principal
- Always receive all coupons regardless

**Example:**

- Principal: $100,000
- Underlying: Apple at $180
- Strike: $180 (at-the-money)
- Coupon: 15% annually
- Maturity: 6 months

### 2. Payoff at Maturity

**Two scenarios:**

**Scenario A: Stock finishes ≥ Strike**

Apple at $200 at maturity (above $180 strike)

**Payoff:**
- Principal: $100,000 (cash)
- Coupon: $7,500 (15% × 6 months)
- **Total: $107,500**
- **Return: 15% annualized**

**Scenario B: Stock finishes < Strike**

Apple at $150 at maturity (below $180 strike)

**Payoff:**
- Principal: 555.56 shares ($100K / $180)
- Share value: 555.56 × $150 = $83,333
- Coupon: $7,500
- **Total: $90,833**
- **Loss: -9.2%** (despite earning 15% coupon)

**Effective put sale:**

Investor has sold put option:
- Strike: $180
- Premium received: $7,500 (embedded in coupon)
- If stock < $180: Must buy at $180 (via share delivery)

### 3. Strike Selection

**Three standard variations:**

**At-the-money (ATM):**
- Strike = Current stock price
- Example: Stock $100, Strike $100
- Highest risk, highest coupon
- Most common structure

**Out-of-the-money (OTM):**
- Strike < Current stock price
- Example: Stock $100, Strike $90 (10% cushion)
- Lower risk, lower coupon
- More conservative

**In-the-money (ITM):**
- Strike > Current stock price
- Example: Stock $100, Strike $110
- Even higher coupon
- Almost certain to convert
- Rarely offered (too risky)

**Coupon comparison:**

Stock at $100:

- Strike $90 (OTM): Coupon 12%
- Strike $100 (ATM): Coupon 18%
- Strike $110 (ITM): Coupon 25%

### 4. Maturity Timing

**Short-term nature:**

**Typical maturities:**
- 3 months: Very short, high annualized coupons
- 6 months: Most common
- 9 months: Less common
- 12 months: Maximum

**Why short-term?**
- Easier to forecast (less uncertainty)
- Higher investor comfort
- Better liquidity (faster turnaround)
- Market timing plays

**Example:**

Same 15% coupon on Apple:

**3-month note:**
- Coupon payment: $3,750 (15% × 3/12)
- Time at risk: Only 3 months
- Higher probability of staying above strike

**12-month note:**
- Coupon payment: $15,000 (15% × 12/12)
- Time at risk: Full year
- Higher probability of dropping below strike

**Trade-off:** Shorter = Less time premium but less risk

### 5. Worst-Of Structure

**Multiple underlying stocks:**

**Definition:** Reverse convertible where conversion depends on the WORST performer among a basket of stocks, all must stay above their strikes to avoid conversion.

**Example:**

- Principal: $100K
- Underlyings: Apple, Microsoft, Google (each at $200)
- Strikes: $200 for each
- Coupon: 25% annually (6 months = $12,500)
- Maturity: 6 months

**Scenario A: All above strikes**

All three at $210+

**Payoff:** $100K cash + $12.5K = $112.5K ✓

**Scenario B: One below strike**

- Apple: $180 (worst, -10%)
- Microsoft: $220
- Google: $215

**Payoff:**
- Receive: 500 Apple shares ($100K / $200)
- Value: 500 × $180 = $90K
- Coupon: $12.5K
- **Total: $102.5K** (+2.5%, but own falling stock)

**Why higher coupon?**

- Probability of any ONE falling is much higher than single stock
- Correlation matters (diversification benefit questionable)
- Typically 5-10% higher coupon than single-stock

### 6. Digital vs. Proportional

**How conversion amount is determined:**

**Proportional (standard):**

$$
\text{Shares} = \frac{\text{Principal}}{\text{Strike}}
$$

If stock ends at $S_T < K$:

$$
\text{Value} = \text{Shares} \times S_T = \frac{\text{Principal}}{K} \times S_T
$$

**Example:**
- Principal: $100K, Strike: $180, Final: $150
- Shares: 555.56
- Value: $83,333

**Digital (rare):**

Fixed share amount regardless of final price

- Below strike → Receive fixed number of shares
- Creates discontinuous payoff
- Harder to hedge, uncommon

### 7. Protection Features

**Enhanced structures:**

**Knock-in barrier:**
- Conversion only if stock ever touches barrier
- Barrier < Strike (e.g., 80% of initial)
- More expensive, lower coupon
- Memory effect (barrier breach is permanent)

**Example:**

- Stock: $100
- Strike: $100
- Barrier: $80
- If stock drops to $90 at maturity → No conversion (never hit $80)
- If stock drops to $75 at maturity → Conversion (hit barrier)

**Coupon impact:**

- Standard RCN: 18% coupon
- Knock-in RCN: 12% coupon (barrier reduces risk)

**Partial protection:**
- Receive some cash + some shares
- Example: 50% cash + 50% shares if converted
- Reduces downside impact
- Lower coupon

---

## Key Terminology

**Strike Price:**
- Price at which conversion determined
- Usually set at-the-money (ATM)
- Determines share quantity if converted
- Key risk parameter

**Participation:**
- Percentage of downside accepted
- 100% = full downside (standard)
- 80% = cushioned (partial protection)
- Lower participation = lower coupon

**Observation Date:**
- Single date at maturity (European)
- Used to determine final settlement
- Based on official close
- No path dependency (except barriers)

**Physical Settlement:**
- Delivery of actual shares
- Must be accepted by investor
- Can sell immediately after receipt
- Tax implications (capital gains start)

**Automatic Exercise:**
- No decision needed by investor
- Conversion automatic if stock < strike
- Unlike put options (which require decision)
- Simplifies process

**Yield Enhancement:**
- Extra return from embedded put premium
- Typically 5-15% above bond yields
- Compensation for equity risk
- Main selling point

---

## Why Investors Buy

### 1. Income Generation

**High coupons in short timeframe:**

**Example:**

Capital: $100K

**Alternatives:**

**6-month CD:**
- Yield: 5% annually = $2,500 for 6 months

**6-month Treasury:**
- Yield: 5.5% annually = $2,750 for 6 months

**Reverse convertible:**
- Coupon: 16% annually = $8,000 for 6 months
- **3× the income of CD!**

**Trade-off:**
- Get much higher income
- But risk equity conversion
- Appropriate if bullish on underlying

### 2. Strategic Stock Entry

**Want to buy stock at lower price:**

**Example:**

Want to own Tesla at $200 (current: $250)

**Traditional approach:**
- Place limit order at $200
- Earn $0 while waiting
- Might never fill

**Reverse convertible approach:**
- Buy RCN: Strike $250, Principal $100K
- Coupon: 20% × 6 months = $10K
- **If Tesla falls to $200:**
  - Receive 400 shares ($100K / $250)
  - Paid $10K while waiting
  - Effective cost basis: $250 - $10K/400 = $225 per share
- **If Tesla stays at $250:**
  - Keep $100K + $10K
  - Can try again

**Better than limit order:**
- Earn income while waiting
- Reduce effective cost basis
- Still get shares if drops

### 3. Market View

**Neutral-to-bullish outlook:**

**View:**
- Stock won't crash >15-20%
- Comfortable owning at current price
- Want income during sideways period
- Don't expect massive rally (willing to miss upside)

**RCN fits perfectly:**
- Earn high coupon if flat
- Earn high coupon if moderate rise
- Only lose if significant drop
- Match view to structure

### 4. Portfolio Yield

**Enhance fixed income returns:**

**Setup:**
- Portfolio: $1M
- Bond allocation: $400K earning 5% = $20K/year

**Replace with RCNs:**
- Same $400K in RCNs
- Average coupon: 15%
- **Income: $60K/year** (3× increase!)

**Risk:**
- Bond allocation now has equity risk
- But only if stocks fall significantly
- During bull/sideways markets, massively outperform

### 5. Short-Term Speculation

**Tactical bets:**

**Before earnings:**
- Buy RCN on stock 2 weeks before earnings
- If earnings good → Keep principal + coupon
- If earnings bad → Get shares (wanted to buy anyway)
- High coupon for short period

**Example:**

Apple earnings in 2 weeks

**Strategy:**
- Buy 1-month RCN
- Strike: $180 (current price)
- Coupon: 20% annualized = 1.67% for 1 month = $1,667
- **Two outcomes:**
  1. Earnings good, stock at $185 → Keep $100K + $1,667
  2. Earnings bad, stock at $170 → Get shares + $1,667
- Either way, earn $1,667 in 1 month

### 6. Tax Harvesting

**Losses for tax purposes:**

If converted to shares that fell:
- Establish cost basis at strike price
- Immediate unrealized loss
- Can sell and harvest tax loss
- Offset capital gains elsewhere

**Example:**

- Converted to Apple shares at $180 strike
- Current market: $150
- Unrealized loss: $30 per share × 555.56 = $16,667
- Sell immediately → Realize loss
- Offset against $16,667 of capital gains
- Tax savings: $16,667 × 20% = $3,333

**Net outcome:**
- Loss: $16,667
- Coupon: $7,500
- Tax savings: $3,333
- **Net loss: $5,834** (much better than -$16,667)

### 7. Covered Call Alternative

**Achieve similar risk-return:**

**Covered call:**
- Buy stock at $180
- Sell call at $180
- Collect premium

**Reverse convertible:**
- Implicit short put at $180
- Collect premium (via coupon)
- Less capital intensive

**Comparison:**

**Covered call (own stock):**
- Capital: $180K (buy 1,000 shares)
- Premium: $5K (selling calls)
- Return if flat: 2.8%

**Reverse convertible:**
- Capital: $100K (note)
- Premium: $7.5K (coupon)
- Return if flat: 7.5%

**RCN advantages:**
- Less capital needed
- Higher yield on capital
- No dividends (simplicity)

**Covered call advantages:**
- Own stock (diversification)
- Can adjust dynamically
- More liquid

---

## Pricing & Valuation

### 1. Put Premium Extraction

**Core pricing formula:**

$$
\text{Note Value} = \text{Bond} + \text{Short Put}
$$

Or equivalently:

$$
\text{Enhanced Coupon} = \text{Risk-Free Rate} + \frac{\text{Put Premium}}{\text{Notional}}
$$

**Example:**

6-month note on stock at $180

**Risk-free rate:** 5% annually = 2.5% for 6 months

**Put premium** (ATM, 6 months, 30% vol):
- Using Black-Scholes: $12.50 per share = 6.9%
- Annualized: 13.8%

**Total coupon:**
$$
\text{Coupon} = 5\% + 13.8\% = 18.8\% \approx 19\%
$$

### 2. Black-Scholes Valuation

**Put option pricing:**

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

**Example:**

- $S_0 = \$180$
- $K = \$180$ (ATM)
- $r = 5\%$
- $\sigma = 30\%$
- $T = 0.5$ years

**Calculation:**
$$
d_1 = \frac{\ln(180/180) + (0.05 + 0.09/2) \times 0.5}{0.3\sqrt{0.5}} = 0.2209
$$

$$
d_2 = 0.2209 - 0.3\sqrt{0.5} = 0.0089
$$

$$
P = 180 e^{-0.05 \times 0.5} N(-0.0089) - 180 N(-0.2209)
$$

$$
P = 180 \times 0.9753 \times 0.4965 - 180 \times 0.4126 = \$12.55
$$

**Put premium: 6.97%** (12.55 / 180)
**Annualized: 13.94%**
**Total coupon: 5% + 13.94% = 18.94%**

### 3. Break-Even Analysis

**At what stock price do you break even?**

$$
\text{Break-even: } S_T = K \times \left(1 - \frac{\text{Coupon}}{\text{Principal}}\right)
$$

**Example:**

- Strike: $180
- Coupon: 15% annually × 6 months = 7.5%

$$
S_T = 180 \times (1 - 0.075) = 180 \times 0.925 = \$166.50
$$

**Interpretation:** Stock can fall to $166.50 (7.5% drop) and investor breaks even.

### 4. Probability of Conversion

**Chance of receiving shares:**

Using risk-neutral framework:

$$
\mathbb{P}(S_T < K) = N\left(\frac{\ln(K/S_0) + (r - \sigma^2/2)T}{\sigma\sqrt{T}}\right)
$$

**Example:**

$S_0 = K = \$180$, $\sigma = 30\%$, $T = 0.5$

$$
\mathbb{P}(S_T < 180) = N\left(\frac{0 + (0.05 - 0.045) \times 0.5}{0.3\sqrt{0.5}}\right) = N(0.0118) = 50.47\%
$$

**Interpretation:** Roughly 50% chance of conversion (makes sense for ATM)

### 5. Expected Return

**Probability-weighted outcomes:**

$$
E[R] = P(\text{no conversion}) \times R_{\text{success}} + P(\text{conversion}) \times E[R_{\text{conversion}}]
$$

**Example:**

- P(no conversion) = 50%
- Return if no conversion: 15% annualized
- P(conversion) = 50%
- Expected stock return conditional on being ITM: -12% (on average)
- Coupon offsets some loss: 15% - 12% = 3%

$$
E[R] = 0.50 \times 15\% + 0.50 \times 3\% = 7.5\% + 1.5\% = 9\%
$$

**vs. expected stock return: ~8-10%**

**Roughly fair** (market efficiently prices risk)

### 6. Volatility Sensitivity

**Higher vol = higher coupon:**

Stock at $180, 6-month maturity

**Vol = 20% (low):**
- Put premium: 5.5%
- Coupon: 5% + 5.5% × 2 = 16%

**Vol = 30% (medium):**
- Put premium: 7%
- Coupon: 5% + 7% × 2 = 19%

**Vol = 40% (high):**
- Put premium: 9.5%
- Coupon: 5% + 9.5% × 2 = 24%

**Implication:**
- High-vol stocks offer higher coupons
- But higher chance of conversion
- Trade-off: Income vs. risk

### 7. Dividend Adjustment

**Dividends reduce put value:**

$$
P_{\text{with div}} < P_{\text{no div}}
$$

**Impact on coupon:**
- Higher dividend yield → Lower put premium
- Lower put premium → Lower coupon
- But dividend cushions conversion risk

**Example:**

Stock at $180, no dividend vs. 3% dividend yield

**No dividend:**
- Put premium: 7%
- Coupon: 19%

**3% dividend:**
- Put premium: 5.5%
- Coupon: 16%

**Trade-off:**
- Lower coupon (16% vs. 19%)
- But dividend provides 1.5% return if hold shares
- Somewhat compensates

---

## Common Mistakes

### 1. Treating as "Safe" Income

**High coupon ≠ low risk:**

- **Mistake:** View RCN as "bond with better yield"
- **Why it fails:** It's actually "short put with coupon"
- **Fix:** Recognize full equity downside risk
- **Real cost:** Shocked by 30-50% losses in crashes

**Example:**

Investor buys RCN thinking "guaranteed 20% in 6 months"

**Market crashes 40%:**
- Receive shares down 40%
- Coupon: +10% (6 months × 20%)
- **Net: -30%** (not the "safe" 20% expected)

**Lesson:** High coupon is compensation for risk, not free money

### 2. Ignoring Forced Conversion

**Can't choose to walk away:**

- **Mistake:** Think "I can just not take the shares"
- **Why it fails:** Conversion is automatic (not optional)
- **Fix:** Understand you WILL receive shares if ITM
- **Real cost:** Forced to own falling stock

**Example:**

- RCN on biotech stock at $100
- Stock drops to $50 after FDA rejection
- Investor thinking: "I don't want these shares!"

**Reality:**
- Must receive 1,000 shares worth $50K
- No choice (automatic conversion)
- Must hold or sell at $50 (realizing loss)

**Contrast with put options:**
- Put buyer can choose not to exercise
- RCN holder has no choice

### 3. Worst-Of Correlation

**Underestimating joint probability:**

- **Mistake:** "Three stocks, diversified, lower risk"
- **Why it fails:** Stocks correlate in crashes (→ 1)
- **Fix:** Stress test under 0.9+ correlation
- **Real cost:** All stocks convert together

**Example:**

Worst-of on 3 banks (2007):

**Normal times (ρ = 0.5):**
- P(any one < strike) = 18%

**Crisis (ρ = 0.95):**
- P(any one < strike) = 40%

**Result:**
- Extra 8% coupon for worst-of structure
- But risk more than doubled (18% → 40%)
- Compensation insufficient

### 4. Maturity Mismatch

**Duration vs. conviction:**

- **Mistake:** Buy 12-month RCN with 3-month view
- **Why it fails:** View changes, but locked in for 12 months
- **Fix:** Match maturity to conviction timeframe
- **Real cost:** Hold wrong position for 9 months

**Example:**

Bullish on tech for next quarter

**Buy 12-month RCN:**
- Collect 20% coupon
- Tech rallies first 3 months (view correct)
- Then corrects -25% over next 9 months

**Outcome:**
- Converted to shares (now underwater)
- **Should have used 3-month RCN** (would have exited at peak)

### 5. Strike Selection Errors

**Optimizing wrong parameter:**

- **Mistake:** Choose OTM strike (lower risk) but too low coupon
- **Why it fails:** Opportunity cost vs. alternatives
- **Fix:** Compare risk-adjusted returns across strikes
- **Real cost:** Suboptimal risk-return trade-off

**Example:**

Stock at $100

**Option A: ATM strike ($100), 20% coupon**
- P(conversion) = 50%
- Expected return = 10%

**Option B: OTM strike ($90), 12% coupon**
- P(conversion) = 20%
- Expected return = 9.6%

**Analysis:**
- Option A: Higher expected return
- Option B: Lower risk but insufficient compensation
- **Choose A** (better risk-adjusted)

### 6. Issuer Credit Ignorance

**Focus only on equity, ignore credit:**

- **Mistake:** Only analyze stock, ignore issuer rating
- **Why it fails:** Issuer default = lose everything
- **Fix:** Check issuer credit, diversify issuers
- **Real cost:** Lehman RCNs worthless in 2008

**Example:**

2008 crisis:

- RCN issued by Lehman Brothers
- Underlying: S&P 500 (stayed above strike!)
- Should have received $100K + coupons

**Reality:**
- Lehman bankrupt
- Note became unsecured claim
- Recovery: ~8¢ on dollar
- **Lost 92%** despite stock above strike

---

## Best vs. Worst Case

### 1. Best Case: Success

**Ideal scenario:**

**Setup:**
- RCN on Apple at $180
- Strike: $180 (ATM)
- Coupon: 18% annually
- Maturity: 6 months
- Principal: $100,000

**Market environment:**
- Steady bull market
- Tech sector strong
- Apple has positive catalyst (new product launch)

**Path:**

**Month 1-3:**
- Apple steady at $185-190
- No concerns

**Month 4-6:**
- Apple rallies to $210 (new iPhone sales strong)
- Well above strike

**Maturity:**
- Apple at $210 (16.7% gain from initial)
- **Payoff: $100K cash + $9K coupon = $109K**
- **Return: 18% annualized**

**Comparison:**

**Owned Apple stock:**
- Return: 16.7% + 1% dividend = 17.7%

**RCN:**
- Return: 18%
- **Slightly better!**

**But more importantly:**
- No equity risk taken (got cash back)
- Can redeploy $100K immediately
- Earned income during 6-month period

**Multiple iterations:**

Repeat strategy 4 times over 2 years:
- Each RCN: 18% annualized × 6 months = 9% per period
- Compound: (1.09)^4 = 1.41
- **Total: 41% over 2 years** (18.7% annualized)

**vs. holding Apple:**
- Assume 10% annual return
- Total: 21% over 2 years

**RCN strategy dominated** (in this ideal scenario)

### 2. Worst Case: Disaster

**2008-style crash:**

**Setup:**
- RCN on Citigroup at $50 (October 2007)
- Strike: $50
- Coupon: 22% annually
- Maturity: 12 months
- Principal: $100,000

**Path:**

**Q1 2008:**
- Citi falls to $45 (concerns about subprime exposure)
- Still close to strike

**Q2 2008:**
- Citi falls to $40 (write-downs accelerating)
- Below strike, will convert

**Q3 2008:**
- Citi at $30 (crisis deepening)
- Far below strike

**Q4 2008: Lehman collapse**
- Citi crashes to $10 (80% down from initial!)
- Government intervention prevents bankruptcy

**Maturity (October 2008):**
- Citi at $15 (recovered from $10 low)
- **Conversion: 2,000 shares** ($100K / $50)
- Share value: 2,000 × $15 = $30K
- Coupon received: $22K (22% × 1 year)
- **Total: $52K**
- **Loss: -48%** (-$48,000)

**Comparison:**

**Held Citi stock:**
- Loss: 70% ($50 → $15)
- Dividend: ~0% (suspended)
- **Total: -70%**

**RCN:**
- Loss: -48%
- **Better than stock** (coupon cushioned)
- But still devastated

**Investor perspective:**

"I thought 22% coupon meant it was safe!"

**Reality:**
- High coupon signaled high risk
- Market correctly priced extreme downside
- Banking sector systemic risk
- No "safe" place to hide

**Post-crisis:**

Sold shares at $15:
- Realized loss: -48%
- Tax loss: Offset $48K in gains
- Small consolation

**5 years later (2013):**
- Citi recovered to $45
- But investor already sold at $15
- Missed recovery (opportunity cost)

---

## Risk Management Rules

### 1. Position Sizing

**Maximum allocation:**

$$
\text{Max RCN} = \min(20\% \text{ of equity allocation}, 10\% \text{ of total portfolio})
$$

**Example:**

$500K portfolio: 60% equity ($300K), 40% bonds ($200K)

**Maximum RCN:**
- 20% of equity = $60K
- 10% of total = $50K
- **Limit: $50K** (take minimum)

**Rationale:** Treat as equity substitute, not bond

### 2. Diversification

**Spread risk across dimensions:**

**Rules:**
- Maximum 4 different RCNs
- No more than 30% in single issuer
- No more than 30% on single stock
- No more than 50% on single sector

**Example $200K allocation:**
- Note 1: $50K on Apple, Issuer A
- Note 2: $50K on S&P 500, Issuer B
- Note 3: $50K on Healthcare sector, Issuer A
- Note 4: $50K on Amazon, Issuer C

**Diversified:** ✓

### 3. Strike Cushion

**Minimum downside buffer:**

$$
\frac{S_0 - K}{S_0} \geq 5\%
$$

**Example:**

Stock at $100

**Acceptable:**
- Strike $95 (5% cushion) ✓
- Strike $90 (10% cushion) ✓

**Marginal:**
- Strike $100 (0% cushion) - only if high conviction

**Reject:**
- Strike $105 (negative cushion!) ✗

**Rationale:** Need buffer for normal volatility

### 4. Coupon Reasonableness

**Fair value check:**

$$
\text{Coupon} \approx r + 2 \times \sigma \times \sqrt{T}
$$

**Example:**

6-month RCN, vol = 30%

$$
\text{Fair coupon} \approx 5\% + 2 \times 30\% \times \sqrt{0.5} = 5\% + 42.4\% = 47.4\% \text{ annually}
$$

But with P(conversion) adjustment: ~18-22% is fair

**If offered 30%:** Check why (very high vol? ITM strike?)
**If offered 12%:** Poor deal (just buy bonds)

### 5. Maturity Matching

**Conviction horizon:**

$$
\text{Maturity} \leq \text{Conviction Period}
$$

**Example:**

Bullish on Tesla for next 3 months (product launch)

**Choose:**
- 3-month RCN ✓
- 6-month RCN ✗ (view may change after 3 months)
- 12-month RCN ✗✗ (way too long)

### 6. Issuer Credit

**Minimum standards:**

$$
\text{Issuer Rating} \geq \text{BBB+}
$$

**Prefer: A- or better**

**Monitoring:**
- Check CDS spreads before each new RCN
- If CDS > 300 bps → Avoid that issuer
- Diversify across 3+ issuers

**Example:**

Offered RCN from Regional Bank (BBB rated, CDS 280 bps)

**Analysis:**
- Rating: Marginal (BBB)
- CDS: High (280 bps)
- **Action: Reject**

Better to wait for A-rated issuer offer

### 7. Break-Even Discipline

**Minimum break-even cushion:**

$$
\text{Break-even decline} = \frac{\text{Coupon}}{\text{Principal}} \geq 8\%
$$

**Example:**

Stock at $100, strike $100, coupon 15% for 6 months

**Break-even:** Stock can fall to $92.50 (7.5% drop)

**Too tight!** (Want at least 8% cushion)

**Better structure:**
- Extend to 9 months: 15% × 9/12 = 11.25% coupon
- Break-even: $88.75 (11.25% drop) ✓

---

## Real-World Examples

### 1. Classic Apple RCN (2015-2016)

**Popular retail product:**

**Setup:**
- Issuer: Morgan Stanley (A+ rated)
- Underlying: Apple at $120
- Strike: $120 (ATM)
- Coupon: 18% annually
- Maturity: 6 months
- Sold to retail investors

**Path:**
- Apple steady $115-125 for 5 months
- Month 6: Earnings beat, rallies to $130

**Outcome:**
- Stock above strike ($130 > $120)
- Investors received: $100K + $9K = $109K
- **Return: 18% annualized**
- Very satisfied customers

**Why successful:**
- Apple stable, high-quality company
- Reasonable 6-month timeframe
- Fair coupon for risk
- Strong issuer credit

**Multiple issuances:**
- Morgan Stanley issued dozens of similar notes
- High take-up from retail
- Generally positive outcomes (2010-2016 bull market)

### 2. Energy Sector Disaster (2014-2016)

**Oil crash impact:**

**Setup:**
- Underlying: Exxon at $100 (mid-2014)
- Strike: $100
- Coupon: 14%
- Maturity: 12 months

**Oil crash:**
- Oil: $100/barrel → $30/barrel (70% drop)
- Exxon: $100 → $70 (30% drop)

**Maturity (mid-2015):**
- Exxon at $75 (25% down)
- Conversion: 1,000 shares
- Value: $75K
- Coupon: $14K
- **Total: $89K (-11%)**

**Investor reaction:**
- "Only 14% coupon for 11% loss?"
- "Should have just held bonds"
- Disappointed but understood risk

**Lesson:**
- Sector risk matters
- Commodity-linked stocks volatile
- 14% coupon insufficient for energy risk
- Should have been 18-20%

### 3. Tesla Volatility Play (2020)

**High-vol structure:**

**Setup:**
- Tesla at $500 (pre-split equivalent)
- Strike: $500
- Coupon: 28% annually (!!)
- Maturity: 3 months
- Issuer: Major bank

**Why 28% coupon?**
- Tesla implied vol: 80%+
- Put option expensive
- High risk = high reward

**Scenario A (happened):**
- Tesla rallied to $700 (40% gain in 3 months)
- No conversion
- **Return: 7% in 3 months** (28% annualized)

**But if Scenario B:**
- Tesla fell to $350 (30% drop)
- Conversion to shares
- Value: $350 per share
- Coupon: $35 (28% × 3/12)
- **Loss: 16%** (30% - 14% coupon)

**High risk, high reward**
- Appropriate for sophisticated investors
- Retail might not understand 80% vol
- Need strong conviction

### 4. Worst-Of Tech (2018)

**FAANG basket:**

**Setup:**
- Worst of: Facebook, Amazon, Apple, Netflix, Google
- All at $100 (normalized)
- Strike: $100 for each
- Coupon: 22%
- Maturity: 6 months

**Q4 2018 correction:**
- All fell together (high correlation)
- Facebook: $100 → $75 (worst)
- Amazon: $100 → $80
- Apple: $100 → $82
- Netflix: $100 → $78
- Google: $100 → $85

**Conversion:** Facebook (worst performer)

**Maturity:**
- Facebook at $80 (recovered from $75)
- Conversion: 1,000 shares
- Value: $80K
- Coupon: $11K
- **Total: $91K (-9%)**

**If single-stock on S&P 500:**
- Coupon would be 15% (lower risk)
- S&P stayed above strike (no conversion)
- **Return: +15%**

**Lesson:**
- Extra 7% coupon for worst-of not enough
- Correlation risk underestimated
- Single-stock structure would have been better

---

## Practical Steps

### 1. Suitability Assessment

**Is RCN right for you?**

**Checklist:**
- [ ] Understand it's short put (not bond)
- [ ] Comfortable owning underlying at strike
- [ ] Can tolerate 20-30% loss
- [ ] Time horizon matches maturity
- [ ] Bullish or neutral on stock
- [ ] Don't need liquidity before maturity
- [ ] Understand forced conversion

**If all checked → Proceed**

### 2. Product Evaluation

**Screening criteria:**

**Issuer:**
- Rating ≥ A-
- CDS < 200 bps
- Major financial institution

**Underlying:**
- Liquid stock (>$1M daily volume)
- Understand business fundamentals
- Check recent volatility
- Review analyst ratings

**Terms:**
- Strike: ATM or slightly OTM preferred
- Coupon: 15-25% range (not too low/high)
- Maturity: 3-9 months (not too long)
- Break-even: ≥8% decline cushion

### 3. Pricing Verification

**Is it fair value?**

**Steps:**

1. **Get Black-Scholes inputs:**
   - Current stock price
   - Implied volatility (ATM)
   - Dividend yield
   - Risk-free rate
   - Time to maturity

2. **Calculate put value:**
   - Use online calculator or Excel
   - Check put premium %

3. **Derive fair coupon:**
   - Fair coupon = Risk-free + Put premium / maturity

4. **Compare to offered:**
   - Offered ≥ Fair value → Good deal
   - Offered < Fair value → Walk away

**Example:**

Offered 18% coupon

**Your calculation:**
- Risk-free: 5%
- Put premium: 7% (6-month)
- Fair: 5% + 7% × 2 = 19%

**Conclusion:** Offered 18% vs. Fair 19%
- Slightly low (1% underpriced)
- Negotiate or look elsewhere

### 4. Execution

**How to invest:**

**Primary market:**
- Buy at issuance from broker
- No secondary market spread
- Standard documentation
- Easier process

**Check:**
- Final terms match initial offer
- All fees disclosed
- Settlement procedures clear
- Tax documentation provided

**Size appropriately:**
- Start with 5% of allocation
- Scale up if successful
- Don't overconcentrate

### 5. Monitoring

**Ongoing surveillance:**

**Weekly:**
- Stock price vs. strike (how close?)
- Issuer credit (CDS, news)
- Implied volatility (changes?)
- Mark-to-market value

**Monthly:**
- Review thesis (still valid?)
- Check break-even distance
- Prepare for conversion scenario
- Plan for maturity reinvestment

**Event-driven:**
- Earnings announcements
- Major news on underlying
- Issuer credit events
- Market corrections (>5%)

### 6. Maturity Management

**At expiration:**

**Scenario A: No conversion**
- Receive cash principal
- Receive final coupon
- Plan reinvestment immediately
- Evaluate new RCN opportunities

**Scenario B: Conversion to shares**
- Receive physical shares
- Evaluate outlook:
  - Bullish → Hold shares
  - Neutral → Sell 50%, hold 50%
  - Bearish → Sell immediately
- Consider tax implications:
  - Holding period starts now
  - Can harvest loss if needed
- Update portfolio allocation (now own equity)

**Documentation:**
- Confirm share delivery
- Verify cost basis
- Update tax records
- Calculate realized return

---

## Final Wisdom

> "Reverse convertibles are Wall Street's most straightforward structured product—which is both their strength and their danger. Unlike autocallables with their complex path dependencies, or principal-protected notes with their binary outcomes, RCNs have a simple premise: You're selling a put option and collecting the premium as a coupon. That's it. But simplicity doesn't mean safety. That 18% coupon is the market's fair price for the risk you're taking, not free money. If it seems like an easy 18% return, you're not understanding the risk—the market is smarter than you. RCNs work beautifully when you have genuine conviction on a stock and would be happy to own it at current prices. They work terribly when you're chasing yield without understanding you're selling equity downside insurance. The 'reverse' in reverse convertible doesn't just mean the opposite of traditional convertibles—it means you're on the OTHER SIDE of the trade, taking the risk that option buyers are paying to avoid. Use them when you'd buy the stock anyway, when you'd sell cash-secured puts anyway, when you truly understand you're an equity investor dressed up as a bond investor. Never buy them thinking 'I'll just take the coupon and never get converted'—because the moment you think that, you will get converted, the stock will be down 40%, and you'll realize that 18% coupon didn't compensate for 40% equity loss. Be the house, not the gambler. The house knows the odds and sizes positions accordingly."

**Key to success:**

- Treat as short put, not bond (honest risk assessment)
- Only sell puts on stocks you'd happily own
- Strike = price you'd pay to buy stock today
- Diversify across issuers, stocks, maturities
- Size for total loss (coupon won't save you in crashes)
- Match maturity to conviction period (don't overstay)
- Monitor issuer credit as much as stock price
- Have plan for both outcomes (cash back or shares)
