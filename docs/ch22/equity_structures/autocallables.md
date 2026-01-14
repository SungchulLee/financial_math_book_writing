# Autocallables


**Autocallable notes** are structured products that automatically mature early ("call") if the underlying asset reaches predetermined trigger levels at observation dates, paying accumulated coupons plus principal, while offering downside protection through barriers but exposing investors to significant losses if barriers are breached, creating asymmetric risk-return profiles that favor stable or moderately rising markets.

---

## The Core Insight


**The fundamental idea:**

- Investors want upside with limited downside
- Early maturity = return capital faster if market cooperates
- High coupons accumulate until autocall or maturity
- Barrier provides downside cushion (until breached)
- If breaches, lose like stock (minus coupons)
- Structure works best in sideways-to-up markets

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/autocallable_payoff_profile.png?raw=true" alt="autocallable_payoff_profile" width="700">
</p>
**Figure 1:** Autocallable note payoff structure showing early call trigger levels at observation dates, high coupon accumulation, and barrier protection that converts to equity downside if breached, demonstrating the path-dependent asymmetric payoff.

**You're essentially betting: "Market will stay flat or rise moderately, and I'll get paid well for this bet."**

---

## What Are Autocallables?


### 1. Core Structure


**Essential components:**

**Definition:** An autocallable note pays enhanced coupons and automatically matures early if the underlying asset price is at or above a call level on any observation date, returning principal plus all accumulated coupons; if never called and barrier breached, investors face equity downside at maturity.

**When you buy an autocallable:**

- Invest principal (e.g., $100K)
- Receive high coupons (8-15% annually)
- Quarterly or annual observation dates
- If stock ≥ call level at observation → Note calls early
- If never called and barrier breached → Equity conversion
- Typical maturity: 2-3 years

**Example:**

- Principal: $100,000
- Underlying: S&P 500 at 4,500
- Autocall trigger: 4,500 (100% of initial, at-the-money)
- Observations: Quarterly for 2 years
- Coupon: 12% per year (3% per quarter)
- Barrier: 3,375 (75% of initial)

### 2. Observation Schedule


**When does it check for autocall?**

**Quarterly observations (most common):**
- Dates: Every 3 months (8 chances over 2 years)
- Check: Is $S_t \geq$ Call Level?
- If yes → Autocall immediately
- If no → Continue to next observation

**Annual observations:**
- Dates: Once per year (2 chances over 2 years)
- Fewer opportunities to call
- Slightly higher coupon compensation

**Monthly observations:**
- Dates: Every month (24 chances over 2 years)
- More opportunities to call
- Slightly lower coupon (easier to call)

**Example quarterly schedule:**

- Month 3: Observation #1
- Month 6: Observation #2
- Month 9: Observation #3
- Month 12: Observation #4
- Month 15: Observation #5
- Month 18: Observation #6
- Month 21: Observation #7
- Month 24: Final maturity (Observation #8)

### 3. Autocall Payoff


**What happens when it calls?**

$$
\text{Autocall Payoff} = \text{Principal} + \text{Accumulated Coupons}
$$

**Example:**

Note calls at Month 12 (Observation #4)

**Payoff:**
- Principal: $100,000
- Coupons: 12% × 1 year = $12,000
- **Total: $112,000**
- **Return: 12% in 1 year**
- **Annualized: 12%**

**Early call scenarios:**

**Calls at Month 3:**
- Return: $100K + $3K = $103K (12% annualized)

**Calls at Month 6:**
- Return: $100K + $6K = $106K (12% annualized)

**Calls at Month 12:**
- Return: $100K + $12K = $112K (12% annualized)

**Never calls, no barrier breach:**
- Return: $100K + $24K = $124K (12% annualized over 2 years)

### 4. Barrier Feature


**Downside protection level:**

**European barrier (at maturity only):**
- Checks barrier only at final maturity
- If $S_T < 75\%$ at maturity → Equity conversion
- Simpler, less risk for investor
- Lower coupon

**American barrier (continuous):**
- Monitors barrier every moment
- If ever touches 75% → Locked in for conversion
- Path-dependent, riskier
- Higher coupon (compensates for risk)

**Typical:** Daily barrier monitoring

$$
\text{Barrier Breach} = \begin{cases}
\text{Yes} & \text{if } \min_{0 \leq t \leq T} S_t < H \\
\text{No} & \text{otherwise}
\end{cases}
$$

Where $H$ = Barrier level (e.g., 75% of initial)

### 5. Maturity Scenarios


**If never autocalled, three outcomes:**

**Scenario A: Stock above barrier at maturity**
- S&P 500 ends at 4,000 (88.9% of initial 4,500)
- Above barrier (75%)
- Payoff: $100K + $24K (2 years of coupons) = $124K
- **Return: 24% over 2 years (11.4% annualized)**

**Scenario B: Stock below barrier, never touched**
- European barrier case only
- S&P at 3,200 (71% of initial)
- Below barrier but never touched during life
- Payoff: $100K + $24K = $124K
- **Return: 24%** (principal protected!)

**Scenario C: Barrier breached**
- S&P touched 3,300 (73%) during life or ends below 75%
- Equity conversion: Receive shares
- Number of shares: $100K / 4,500 = 22.22 shares
- If S&P ends at 3,600: 22.22 × 3,600 = $80K
- Plus coupons: $24K
- **Total: $104K (4% gain, not loss!)**

**Scenario D: Barrier breached, severe crash**
- S&P ends at 2,700 (60% of initial)
- Shares: 22.22 × 2,700 = $60K
- Plus coupons: $24K
- **Total: $84K (-16% loss)**

### 6. Step-Down Feature


**Call level decreases over time:**

**Example:**

- Year 1 observations: Call at 100% (4,500)
- Year 2 observations: Call at 95% (4,275)
- Year 3 observations: Call at 90% (4,050)

**Why:**
- Increases chance of autocall as time passes
- Encourages early call (return capital faster)
- More investor-friendly
- Slightly lower coupon (easier to trigger)

**Example path:**

Stock at 4,400 throughout

**Without step-down:**
- Call level fixed at 100% (4,500)
- Never calls (stock at 4,400 < 4,500)
- Hold full 2-3 years

**With step-down:**
- Year 1: No call (4,400 < 4,500)
- Year 2: Calls! (4,400 > 4,275, the 95% level)
- **Returns capital 1 year early**

### 7. Memory Feature


**Accumulated coupons:**

**Memory coupon structure:**

$$
\text{Payoff at call date } t = \text{Principal} + \sum_{i=1}^{t} C_i
$$

Where $C_i$ = Coupon for period $i$

**Non-memory structure (rare):**
- Only pay current period coupon
- Lose accrued coupons if calls early
- Investor-unfriendly
- Higher coupon to compensate

**Example:**

Note with 3% quarterly coupon

**Memory (standard):**
- Calls at Month 12 (Q4)
- Pays: Principal + $3K + $3K + $3K + $3K = $100K + $12K

**Non-memory:**
- Calls at Month 12
- Pays: Principal + $3K (current quarter only) = $103K
- **Lost $9K** in foregone coupons

---

## Key Terminology


**Call Trigger:**
- Price level that causes early maturity
- Usually 100% of initial (at-the-money)
- Step-down versions decrease over time
- Must be reached at observation date (not intraday)

**Observation Date:**
- Specific dates when autocall checked
- Quarterly, annual, or monthly
- Based on official closing price
- Miss by 1¢ = No call, wait till next date

**Memory Coupons:**
- Accumulated coupons paid at autocall
- Standard feature in most autocallables
- Increases early call value
- Fair to investors

**Contingent Coupon:**
- Coupon only paid if condition met
- Example: Pay only if stock ≥ barrier
- Riskier for investor (might receive nothing)
- Higher coupon rate

**Worst-Of:**
- Autocallable on basket of stocks
- All must be ≥ call level to autocall
- Any below barrier = conversion on worst
- Much riskier, much higher coupon

**Issuer Call:**
- Issuer can force early redemption
- Separate from autocall feature
- Typically at par after 1 year
- Protects issuer if interest rates rise

---

## Why Investors Buy


### 1. High Income


**Enhanced coupons in low-yield environment:**

**Example:**

Capital: $100K

**Traditional bonds:**
- 2-year Treasury: 4.5%
- Investment grade corporate: 5.5%
- **Annual income: $5,500**

**Autocallable note:**
- Underlying: S&P 500
- Coupon: 11%
- **Annual income: $11,000** (double!)

**Trade-off:**
- Higher income today
- But risk of equity conversion
- Only appropriate if bullish/neutral on market

### 2. Early Return of Capital


**Fast turnaround if market cooperates:**

**Scenario:**

Buy autocallable, market rallies 5% in first quarter

**Outcome:**
- Autocalls at Month 3
- Receive: $103K ($100K + $3K coupon)
- **Return: 12% annualized** (not bad!)
- **Capital back to reinvest** after just 3 months

**vs. bond:**
- 2-year bond: Capital tied up for 24 months
- Can't reinvest early if opportunities arise

**Benefit:**
- Opportunistic capital allocation
- Flexibility in changing markets
- Reduced duration risk

### 3. Moderate Market View


**Perfect for sideways-to-up markets:**

**View:**
- Don't expect big rally (>20%)
- Don't expect crash (<-25%)
- Expect range-bound or modest gains
- Want income during sideways period

**Autocallable fits perfectly:**
- Captures income in flat markets
- Calls early if moderate rally
- Protected until -25% (barrier)
- **Ideal for neutral investors**

### 4. Downside Cushion


**Barrier provides safety net:**

**Example:**

Stock at $100, barrier at $75

**Market correction scenarios:**

**Down 10%:** Stock at $90 → Still above barrier, safe
**Down 20%:** Stock at $80 → Still above barrier, safe  
**Down 24%:** Stock at $76 → Still above barrier, safe
**Down 26%:** Stock at $74 → **Barrier breached**

**25% cushion** before equity risk kicks in

**vs. owning stock:**
- Any decline = immediate loss
- No buffer zone
- Full downside exposure

### 5. Tax Efficiency


**Coupon deferral strategies:**

In some structures:
- Coupons accrue but not paid until maturity/autocall
- Defers tax liability
- Compound returns (reinvest mentally)
- Pay all taxes at exit

**Example:**

$100K note, 11% coupon, 2 years

**Traditional (pay-as-you-go):**
- Year 1 coupon: $11K → Tax $3,850 (35% bracket)
- Year 2 coupon: $11K → Tax $3,850
- **Total taxes: $7,700**

**Accrual structure:**
- Year 1: No payment → No tax
- Year 2: Receive $22K at maturity → Tax $7,700
- **Same total taxes, but deferred**

**Benefit:** Time value of money on deferred taxes

### 6. Principal Protection Perception


**Psychological appeal:**

**Investor thinking:**
- "Even if market drops 24%, I get my money back"
- "Only lose money if market crashes >25%"
- "That's pretty safe, right?"

**Reality:**
- Still exposed to >25% crashes
- Issuer credit risk (not principal protected!)
- Barrier breach is permanent (no recovery)

**But perception drives demand:**
- Feels safer than stocks
- Feels higher-yielding than bonds
- "Best of both worlds"

### 7. Portfolio Diversification


**Uncorrelated strategy:**

Traditional portfolio: 60/40 stocks/bonds

**Add autocallables:**
- 50% stocks (pure equity exposure)
- 30% bonds (duration + credit)
- 20% autocallables (equity-linked income)

**Different risk profile:**
- Stocks: Full upside/downside
- Bonds: Interest rate risk
- Autocallables: Range-bound strategy
- **Potentially lower correlation** during certain regimes

---

## Pricing & Valuation


### 1. Component Breakdown


**Autocallable = Bond + Options:**

$$
\text{Autocallable} = \text{Bond} + \text{Call on Autocall Feature} - \text{Put on Barrier}
$$

**More precisely:**

$$
V_0 = \sum_{i=1}^{N} P_{\text{autocall at } t_i} \times \text{PV}(\text{Payoff}_i) + P_{\text{no autocall}} \times \text{PV}(\text{Final Payoff})
$$

Where:
- $P_{\text{autocall at } t_i}$ = Probability note calls at observation $i$
- $P_{\text{no autocall}}$ = Probability note held to maturity
- PV = Present value

### 2. Monte Carlo Pricing


**Path-dependent valuation:**

**Algorithm:**

1. Simulate $N$ stock paths (e.g., 100,000)
2. For each path:
   - Check autocall at each observation
   - If autocalls: Calculate payoff, discount to present
   - If never autocalls: Calculate final payoff
   - Track barrier breaches
3. Average all discounted payoffs

**Example simulation:**

Stock $S_0 = \$100$, risk-free rate $r = 4\%$, vol $\sigma = 25\%$

**Path 1:**
- Month 3: $S = \$108$ → **Autocalls!**
- Payoff: $\$100 + \$3 = \$103$
- PV: $\$103 \times e^{-0.04 \times 0.25} = \$101.97$

**Path 2:**
- Never autocalls, $S_T = \$95$ (above barrier)
- Payoff: $\$100 + \$12 = \$112$
- PV: $\$112 \times e^{-0.04 \times 1} = \$107.57$

**Path 3:**
- Barrier breached, $S_T = \$60$
- Shares: 1 × $60 = $60$
- Plus coupons: $12$
- Payoff: $72$
- PV: $\$72 \times e^{-0.04 \times 1} = \$69.18$

**Average across 100,000 paths → Fair value**

### 3. Key Greeks


**Delta:**

$$
\Delta = \frac{\partial V}{\partial S}
$$

**Autocallable delta:**
- Near call level: Very high delta (small move = big value change)
- Near barrier: Negative delta kicks in (like short put)
- Mid-range: Modest positive delta

**Vega:**

$$
\text{Vega} = \frac{\partial V}{\partial \sigma}
$$

**Autocallable vega:**
- Typically **negative** (short volatility position)
- Higher vol = Higher barrier breach probability
- Issuer benefits from selling vol at high levels

**Theta:**

$$
\Theta = \frac{\partial V}{\partial t}
$$

**Autocallable theta:**
- Positive theta (earning carry)
- Coupons accrue over time
- Offset by option time decay

### 4. Autocall Probability


**Chance of early redemption:**

**Historical estimation:**

$$
P(\text{autocall by } t) = P\left(\max_{0 \leq s \leq t} S_s \geq K\right)
$$

For lognormal process:

$$
P(\text{max} \geq K) = N\left(\frac{\ln(S_0/K) + (r - q + \sigma^2/2)t}{\sigma\sqrt{t}}\right) + \left(\frac{S_0}{K}\right)^{2(r-q)/\sigma^2 - 1} N\left(\frac{\ln(K/S_0) + (r - q - \sigma^2/2)t}{\sigma\sqrt{t}}\right)
$$

**Example:**

$S_0 = 4,500$, $K = 4,500$ (ATM), $\sigma = 20\%$, $t = 3$ months

**P(autocall at Month 3):** ~52%

**Cumulative probabilities:**
- Month 3: 52%
- Month 6: 68% (cumulative)
- Month 9: 77%
- Month 12: 83%

**Interpretation:** 83% chance note calls within first year

### 5. Barrier Breach Probability


**Chance of downside conversion:**

$$
P(\text{barrier breach}) = P\left(\min_{0 \leq t \leq T} S_t < H\right)
$$

**For continuous monitoring:**

$$
P(\min < H) = N\left(\frac{\ln(H/S_0) + (r - q - \sigma^2/2)T}{\sigma\sqrt{T}}\right) + \left(\frac{H}{S_0}\right)^{2(r-q)/\sigma^2 - 1} N\left(\frac{\ln(H/S_0) - (r - q - \sigma^2/2)T}{\sigma\sqrt{T}}\right)
$$

**Example:**

$S_0 = 4,500$, $H = 3,375$ (75%), $\sigma = 20\%$, $T = 2$ years

**P(barrier breach) ≈ 15%**

**Interpretation:** ~1-in-7 chance of equity conversion

### 6. Expected Return


**Probability-weighted outcomes:**

$$
E[R] = \sum_{i} P_i \times R_i
$$

**Example:**

- $P(\text{autocall Month 3}) = 40\%$ → $R = 12\%$ annualized
- $P(\text{autocall Month 6-12}) = 35\%$ → $R = 12\%$ annualized
- $P(\text{no autocall, safe}) = 20\%$ → $R = 11\%$ annualized
- $P(\text{barrier breach}) = 5\%$ → $R = -10\%$ (conditional expected)

$$
E[R] = 0.40 \times 12\% + 0.35 \times 12\% + 0.20 \times 11\% + 0.05 \times (-10\%)
$$

$$
E[R] = 4.8\% + 4.2\% + 2.2\% - 0.5\% = 10.7\%
$$

**vs. stock expected return: 8-10%**

### 7. Skew Impact


**Volatility smile matters:**

**Put options (barrier protection) trade at higher implied vol than ATM:**

- ATM vol: 20%
- 75% strike put vol: 28% (skew)

**Impact on pricing:**
- Barrier protection is worth more
- Investor pays more for this protection
- Coupon must be lower to compensate

**Example:**

**Flat vol pricing (20%):**
- Fair coupon: 13%

**With skew (put at 28% vol):**
- Fair coupon: 11%

**Issuer keeps extra 2%** from expensive put they sold

---

## Common Mistakes


### 1. Misunderstanding "Safe"


**Barrier ≠ Principal protection:**

- **Mistake:** Think "75% barrier means I'm protected"
- **Why it fails:** Barrier is just conversion trigger, not stop-loss
- **Fix:** Understand full equity downside if breached
- **Real cost:** Shocked by 40%+ losses in crashes

**Example:**

2008 crash scenario:

**Setup:**
- Autocallable on S&P 500 at 1,500
- Barrier at 1,125 (75%)
- Issued: October 2007

**Outcome:**
- Month 3: S&P at 1,400 (no autocall)
- Month 6: S&P at 1,300 (no autocall)
- Month 9: S&P at 1,200 (no autocall, but safe)
- Month 12 (2008 crash): S&P at 900 (**barrier breached**)

**Maturity:**
- S&P at 800 (46.7% down from initial)
- Shares: 1 unit × 800 = $800 per $1,000 invested
- Coupons: $120 (12% × 1 year before crash)
- **Total: $920 (-8% vs. -46.7% for S&P)**
- But investor expected "protection"!

### 2. Ignoring Autocall Timing


**Early call = reinvestment risk:**

- **Mistake:** Don't plan for early return of capital
- **Why it fails:** Might autocall when yields are low
- **Fix:** Have reinvestment strategy ready
- **Real cost:** Capital sits idle earning 0%

**Example:**

**2021 scenario:**

Buy autocallable at 12% coupon (vol was high)

**Month 3:** Market rallies, note autocalls
- Receive: $103K
- **Now what?**

**Try to reinvest:**
- New autocallables only paying 7% (vol dropped)
- Forced to accept much lower yield
- **Reinvestment risk:** 12% → 7% (5% yield drop)

### 3. Correlation Misjudgment


**Worst-of autocallables:**

- **Mistake:** Buy worst-of thinking "diversification helps"
- **Why it fails:** Correlations spike to 1 in crashes (all fall together)
- **Fix:** Stress test under 0.9+ correlation
- **Real cost:** All stocks breach barrier together

**Example:**

**Worst-of on 3 tech stocks:**
- Apple, Microsoft, Google
- Autocall: All ≥ 100%
- Barrier: 75% for each

**Normal times (ρ = 0.6):**
- P(all ≥ 100% for autocall) = 35%
- P(any < 75% for barrier) = 12%
- Seems reasonable

**Crisis (ρ = 0.95):**
- P(all ≥ 100%) = 48% (actually better for autocall!)
- P(any < 75%) = 28% (**more than doubled!**)

**Result:** Extra coupon (16% vs. 11%) doesn't compensate for 2× barrier risk

### 4. Forgetting Issuer Credit


**Unsecured debt obligation:**

- **Mistake:** Focus only on equity risk, ignore credit risk
- **Why it fails:** Issuer default = total loss regardless of stock
- **Fix:** Check issuer rating, monitor CDS
- **Real cost:** Lehman notes worthless in 2008

**Example:**

**2008 Lehman autocallable:**

- Underlying: S&P 500 (performed well 2010-2012!)
- Barrier: Never breached
- Should have autocalled in 2010

**Reality:**
- Lehman bankrupt September 2008
- Note became unsecured claim
- Investors received ~8¢ on dollar in bankruptcy
- **Lost 92%** despite equity never breaching barrier

**Lesson:** Issuer credit risk can dominate equity risk

### 5. Chasing High Coupons


**High coupon = high risk:**

- **Mistake:** Buy highest-coupon autocallable available
- **Why it fails:** High coupon means market pricing high risk
- **Fix:** Compare coupon to implied volatility, barrier levels
- **Real cost:** "Free" extra 3% comes with 50% more barrier breach risk

**Example:**

**Two autocallables:**

**Note A: 11% coupon**
- Underlying: S&P 500 (20% vol)
- Barrier: 75%
- Call: 100%

**Note B: 16% coupon**
- Underlying: Bitcoin (80% vol!)
- Barrier: 70%
- Call: 100%

**Why Note B pays more:**
- 4× the volatility
- Much higher barrier breach probability (40% vs. 15%)
- Extreme path dependency

**Result:**
- Note A: Expected return 10%
- Note B: Expected return 8% (higher risk-adjusted)

**Extra 5% coupon doesn't compensate for 2.7× higher risk**

### 6. Path Dependence Surprise


**Barrier memory:**

- **Mistake:** Think barrier "resets" if stock recovers
- **Why it fails:** Barrier breach is permanent (American monitoring)
- **Fix:** Understand once breached, conversion locked forever
- **Real cost:** Receive shares despite stock above barrier at maturity

**Example:**

Stock path: $100 → $70 → $110

**Investor thinking:**
- "Stock ended at $110 (10% gain)"
- "Should get principal + coupons, right?"

**Reality:**
- Barrier at $75 breached when stock hit $70
- Conversion locked in (path-dependent)
- Receive: 1 share × $110 = $110
- Plus coupons: $12
- **Total: $122 (22% gain, actually OK)**

**But if stock ended at $90:**
- Receive: 1 share × $90 = $90
- Plus coupons: $12
- **Total: $102 (2% gain vs. "should have" got $112)**

---

## Best vs. Worst Case


### 1. Best Case: Success


**Perfect autocallable environment:**

**Setup:**
- Autocallable on S&P 500 at 4,000
- Call trigger: 4,000 (ATM)
- Barrier: 3,000 (75%)
- Coupon: 11% (quarterly: 2.75%)
- Observations: Quarterly
- Maturity: 3 years

**Market environment:**
- Steady bull market
- Low volatility (VIX 12-15)
- No corrections >10%

**Path:**

**Month 3 (Q1):** S&P at 4,100
- **Autocalls!** (above 4,000 trigger)
- Payoff: $100K + $2.75K = $102.75K
- **Return: 11% annualized over 3 months**

**Analysis:**
- Capital returned after just 3 months
- Can reinvest in next opportunity
- Earned 11% annualized with minimal risk
- Perfect outcome

**What if didn't autocall immediately?**

**Alternative path:**

**Q1-Q3:** S&P sideways at 3,900 (no autocall)
**Q4:** S&P rallies to 4,200
- **Autocalls at Month 12**
- Payoff: $100K + $11K = $111K
- **Return: 11% in 1 year**

**Still excellent** - beat most fixed income

**Maximum outcome (held to maturity):**

Never autocalls, S&P stays 3,900-4,000 range

**Maturity (3 years):**
- S&P at 3,950 (still above barrier)
- Payoff: $100K + $33K (11% × 3 years) = $133K
- **Return: 33% over 3 years (10% annualized)**

**Comparison:**
- S&P total return (3,900 → 3,950): 1.3% + 6% divs = 7.3%
- Autocallable: 33%
- **Outperformed by 25.7%** in sideways market

### 2. Worst Case: Disaster


**2008-style crisis:**

**Setup:**
- Autocallable on financial sector index
- Index at 1,000 (October 2007)
- Call: 1,000
- Barrier: 700 (70%, seemed safe!)
- Coupon: 15% (high vol environment)
- Observations: Quarterly
- Maturity: 2 years
- Principal: $500K

**Path:**

**Q1 (Jan 2008):** Index at 950
- No autocall (below 1,000)
- Coupon accrued: $18.75K

**Q2 (April 2008):** Index at 900
- No autocall
- Getting nervous...
- Coupon accrued: $37.5K

**Q3 (July 2008):** Index at 850
- No autocall
- Still above barrier (barely)
- Coupon accrued: $56.25K

**Q4 (October 2008): Lehman collapse**
- Index crashes to 400 (60% down from initial!)
- **Barrier breached** at 700 in September
- Conversion locked in

**Q1-Q4 2009:** Continued weakness
- Index bottoms at 350

**Maturity (October 2009):**
- Index at 500 (recovered from 350, but still 50% down)
- Conversion: 500 shares (500K / 1,000)
- Share value: 500 × $500 = $250K
- Coupons received: $150K (15% × 2 years)
- **Total: $400K**
- **Loss: -$100K (-20%)**

**But many investors panicked:**

**Sale in March 2009:**
- Index at 350
- Note value: $350 × 500 + $150K = $325K
- Dealer bid: $275K (large haircut in distress)
- **Loss: -$225K (-45%)**

**Comparison to alternatives:**

**Held index directly:**
- Return: (500 / 1,000) - 1 = -50%
- **Autocallable better than stock!** (-20% vs. -50%)

**Held Treasuries:**
- Return: +8% (safe haven rally)
- **Treasuries won** (+8% vs. -20%)

**Lessons:**
1. Autocallables don't protect in severe crashes
2. High coupons can't offset 50% equity decline
3. Barrier "protection" is only moderate (30% cushion ≠ safety)
4. Issuer credit risk can make it even worse

---

## Risk Management Rules


### 1. Position Sizing


**Maximum allocation:**

$$
\text{Max Autocallable} = \min(30\% \text{ of equity}, 15\% \text{ of portfolio})
$$

**Rationale:**
- Treat as equity substitute (not bond!)
- Autocallables are equity-like risk with bond-like return profile
- Limit total equity exposure

**Example:**

$1M portfolio: 60% equity ($600K), 40% bonds ($400K)

**Maximum autocallables:**
- 30% of equity = $180K
- 15% of total = $150K
- **Limit: $150K** (take minimum)

### 2. Diversification


**Spread risk:**

**Rules:**
- Maximum 5 different autocallables
- No more than 25% in single issuer
- No more than 30% on single underlying
- Mix observation frequencies (quarterly + annual)

**Example $300K allocation:**
- Note 1: $75K on S&P 500, Issuer A
- Note 2: $75K on Tech sector, Issuer B
- Note 3: $75K on Apple, Issuer C
- Note 4: $75K on Healthcare, Issuer A

**No concentration:** ✓

### 3. Barrier Requirements


**Minimum cushion:**

$$
\text{Barrier Cushion} = \frac{S_0 - H}{S_0} \geq 25\%
$$

**Example:**

Stock/Index at $100

**Acceptable:**
- Barrier at $75 (25% cushion) ✓
- Barrier at $70 (30% cushion) ✓

**Reject:**
- Barrier at $80 (20% cushion) ✗
- Barrier at $85 (15% cushion) ✗

**Rationale:** Need substantial buffer for normal market volatility (20% corrections are common)

### 4. Coupon Reasonableness


**Sanity check:**

$$
\text{Coupon} \approx r + \text{Put Premium} - \text{Call Premium}
$$

**Rule of thumb:**

$$
6\% \leq \text{Coupon} \leq 18\%
$$

**If coupon > 18%:** Extreme risk priced in

**If coupon < 6%:** Poor deal (just buy bonds)

**Example:**

Offered autocallable with 25% coupon

**Red flag:**
- Market pricing extreme risk
- Either very volatile underlying
- Or very tight barrier
- Or issuer credit concerns
- **Reject**

### 5. Observation Frequency


**Balance autocall chance with complexity:**

**Monthly observations:**
- More autocall chances (good)
- More path points to monitor
- Slightly lower coupon

**Quarterly observations (recommended):**
- Reasonable autocall frequency
- Less monitoring overhead
- Standard market convention

**Annual observations:**
- Fewer chances (only 2-3 shots)
- Higher coupon
- Less attractive

**Prefer: Quarterly**

### 6. Issuer Credit


**Minimum standards:**

$$
\text{Issuer Rating} \geq \text{A-}
$$

**Monitoring:**
- Check CDS spreads monthly
- If CDS > 200 bps → Review
- If downgraded to BBB+ → Consider exit
- If downgraded to BBB → Mandatory exit

**Example:**

- Bought note from Bank X (A rated)
- 6 months later: Bank X downgraded to BBB+
- CDS widens to 250 bps
- **Action:** Exit position (even at 10% loss)

**Rationale:** Issuer default risk > equity risk

### 7. Stress Testing


**Required scenarios:**

**Scenario 1: -25% correction**
- Barrier at 75% → Just breached
- Expected outcome?
- Still acceptable return?

**Scenario 2: -40% crash**
- Well below barrier
- Loss after coupons?
- Can portfolio handle this?

**Scenario 3: Early autocall + reinvestment**
- Calls at Month 3
- Where to reinvest at lower yields?
- Opportunity cost?

**Example:**

$100K autocallable, 11% coupon, barrier 75%

**Stress 1 (-25%):**
- Final value: $75K (shares) + $22K (coupons) = $97K
- **Return: -3%** (tolerable)

**Stress 2 (-40%):**
- Final value: $60K (shares) + $22K (coupons) = $82K
- **Return: -18%** (painful but survivable)

---

## Real-World Examples


### 1. Korean Market Dominance


**Largest autocallable market globally:**

**Why popular in Korea:**
- Conservative investor base
- Desire for income + downside protection
- Familiarity with structured products
- Tax advantages for capital gains

**Typical structure:**
- Underlying: KOSPI 200 index
- Maturity: 3 years
- Observations: Monthly
- Step-down: 100% → 95% → 90%
- Barrier: 60-65% (aggressive!)
- Coupon: 8-12% annually

**Performance (2015-2020):**
- Majority autocalled early (bull market)
- Investors received ~10% annualized
- Better than bonds, comparable to equities
- **Widely successful**

**2020 COVID crash:**
- KOSPI dropped 35% (March 2020)
- Many barriers breached
- Recovery meant investors still made money
- But traumatic experience

### 2. European Reverse Convertible


**Conservative variant:**

**Setup:**
- Issued by Swiss bank (AA rated)
- Underlying: SMI index at 10,000
- Autocall: 10,000 (quarterly obs, 3 years)
- Barrier: 7,000 (70%)
- Coupon: 7% (low vol environment)

**Outcome (2017-2020):**
- Index range-bound 9,800-10,200
- Autocalled at Month 15 (Q5)
- Investors received: Principal + 8.75% (1.25 years × 7%)
- **Return: 7% annualized**

**Success factors:**
- Conservative barrier (70% = 30% cushion)
- Stable market environment
- Strong issuer credit
- Reasonable expectations

### 3. Wall Street Retail Distribution


**Mass market autocallables (2010s):**

**Major issuers:**
- JP Morgan
- Morgan Stanley  
- Barclays
- Bank of America

**Typical offering:**
- Underlying: S&P 500, Dow Jones
- Sold through broker networks
- Target: Retail investors
- Coupons: 9-13%

**Controversy:**
- High fees (1-3% embedded)
- Complexity confusing to retail
- Barrier risks not well understood
- SEC scrutiny increased

**Performance:**
- Bull market 2010-2020: Mostly successful
- High autocall rates (80%+ called early)
- Investors generally satisfied

**Issues:**
- Some sold right before 2015 correction
- Barrier breaches caused confusion
- Secondary market liquidity poor
- Complaints about suitability

### 4. Worst-Of Disaster (2018)


**Complex structure:**

**Setup:**
- Worst-of on 3 stocks: Facebook, Netflix, Tesla
- Autocall: All ≥ 100%
- Barrier: 70% on any stock
- Coupon: 18% (!!)
- Maturity: 2 years
- Issued: January 2018

**Path:**

**2018 (volatile year):**
- Facebook: 100 → 130 → 120 (OK)
- Netflix: 100 → 150 → 110 (OK)
- Tesla: 100 → 70 → 60 (**barrier breached**)

**Q4 2018:** All fell together
- Facebook: 130 → 120 (no autocall, all must be ≥100)
- Conversion locked on Tesla

**Maturity (January 2020):**
- Tesla at 140 (recovered!)
- But conversion already locked
- Receive: Tesla shares at 100 cost basis
- Actual value: 140
- Coupons: 36% (18% × 2)
- **Total: 176%** (wait, profit?)

**But:**
- Many sold during panic at 90-100
- Didn't understand path dependence
- Thought "worst-of" meant average of 3
- **Actual returns: -10% to +76%** (huge dispersion based on behavior)

**Lesson:**
- Complexity breeds misunderstanding
- High coupons signal high risk
- Investor behavior matters as much as structure

---

## Practical Steps


### 1. Suitability Assessment


**Is this product right for you?**

**Checklist:**
- [ ] Understand full equity downside risk
- [ ] Comfortable with 2-3 year lockup
- [ ] Bullish or neutral on underlying
- [ ] Can tolerate 25%+ decline
- [ ] Understand path-dependent features
- [ ] Issuer credit risk acceptable
- [ ] Have reinvestment plan if autocalls early

**If all checked → Proceed**

### 2. Product Screening


**Evaluation criteria:**

**Issuer:**
- Credit rating ≥ A-
- CDS < 150 bps
- Major financial institution
- Check recent news/outlook

**Underlying:**
- Liquid market (>$1M daily volume)
- Understand the index/stock
- Comfortable with fundamentals
- Historical volatility analysis

**Structure:**
- Barrier ≥ 75% (prefer 70-75%)
- Observations: Quarterly (prefer) or monthly
- Coupon: 8-15% range (not too high)
- Maturity: 2-3 years (not too long)
- Step-down: Yes (prefer)
- Memory: Yes (mandatory)

### 3. Valuation Check


**Is it fairly priced?**

**Compare to theoretical value:**

1. **Get market data:**
   - Current stock/index price
   - Implied volatility (ATM)
   - Dividend yield
   - Risk-free rate

2. **Run Monte Carlo:**
   - Simulate 50,000 paths
   - Calculate payoffs
   - Average and discount
   - Compare to offered price

3. **Check vs. alternatives:**
   - Covered call writing return
   - Bond + put spread
   - Expected stock return

**Example:**

Offered autocallable at par

**Your valuation: $98**
**Offered: $100**

**Conclusion:** Overpaying $2 (2%) for convenience
- Acceptable if want packaged solution
- Better to negotiate or walk away

### 4. Execution


**How to invest:**

**Primary market (new issue):**
- Buy at launch from issuer
- No secondary market haircut
- Standard terms
- Easier documentation

**Secondary market:**
- Buy existing notes from dealer
- Bid-ask spread: 2-5%
- Check remaining life
- Verify barrier status (already breached?)

**Documentation:**
- Read full prospectus
- Understand all terms
- Check observation dates
- Verify settlement procedures

### 5. Monitoring


**Ongoing surveillance:**

**Monthly:**
- Stock price vs. autocall level
- Stock price vs. barrier
- Observation dates coming up
- Issuer CDS/rating
- Mark-to-market value

**Before each observation:**
- Check expected closing price
- Anticipate autocall (prepare for reinvestment)
- Update probabilities

**Event-driven:**
- Issuer downgrade
- Major market correction (>10%)
- Barrier approach (within 5-10%)
- News on underlying

### 6. Exit Strategy


**When to exit early:**

**Sell if:**
- Issuer downgraded below A-
- Barrier within 10% (stock falling)
- Need liquidity urgently
- Found better opportunity
- Barrier already breached and stock still falling

**Hold if:**
- Issuer credit stable
- Stock well above barrier
- No liquidity need
- Coupons still attractive
- Structure still appropriate

**At autocall:**
- Receive payment
- Plan reinvestment immediately
- Compare current market conditions
- May need to accept lower yields

**At maturity (no autocall):**
- If no breach: Receive principal + coupons ✓
- If breach: Receive shares
  - Evaluate outlook on stock
  - Hold if bullish
  - Sell immediately if bearish
  - Consider tax implications

---

## Final Wisdom


> "Autocallables are the structured product industry's most successful creation—and for good reason. They offer high income, early call optionality, and downside cushions that appeal to conservative investors. But don't confuse a 75% barrier with 'safety'—it's just the point where you start losing real money. The high coupon is payment for selling equity downside insurance, not free money. These products work beautifully in sideways-to-up markets (which is most of the time), but can devastate portfolios in severe crashes. The 2008 crisis proved that 70-75% barriers offer little protection when markets fall 50%+. Use autocallables when you have conviction the market won't crash (not just 'probably won't crash') and when you truly understand that you're selling earthquake insurance on stocks to collect premium. The best buyers are sophisticated investors who use these tactically, size them appropriately (10-15% of portfolio max), diversify across issuers and underlyings, and monitor religiously. The worst buyers are retail investors chasing yield without understanding that the 13% coupon comes with real equity risk. If it seems too good to be true—high income, principal protection, upside participation—remember: it IS too good to be true. You're making trade-offs, and the market always prices those trade-offs fairly (plus a profit margin for the issuer)."

**Key to success:**

- Understand it's equity risk dressed up as fixed income
- Barrier is not a stop-loss (no protection if breached)
- High coupon = high implicit risk (market is smart)
- Diversify across issuers, underlyings, maturities
- Monitor issuer credit more than equity price
- Size appropriately (10-15% of portfolio maximum)
- Have reinvestment plan for early autocalls
- Stress test under realistic crash scenarios (-40%)
