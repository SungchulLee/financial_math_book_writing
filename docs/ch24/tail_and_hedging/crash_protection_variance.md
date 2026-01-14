# Crash Protection with Variance


**Crash protection with variance** uses variance swaps and related derivatives to hedge portfolio tail risk, providing linear payoffs during volatility spikes without the theta decay of traditional options.

---

## The Core Insight


**The fundamental idea:**

- Market crashes = volatility explosions
- Traditional puts decay (theta) and need rolling
- Variance swaps provide pure vol exposure
- No decay (mark-to-market instrument)
- Payoff linear in variance (squared volatility)
- Single trade covers entire horizon

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/variance_crash_protection.png?raw=true" alt="variance_crash_protection" width="700">
</p>
**Figure 1:** Portfolio protection payoff comparing variance swaps vs. puts, showing variance swaps' linear payoff in volatility without theta decay, ideal for tail risk hedging over extended periods.

**You're essentially asking: "How do I protect my portfolio from crashes without paying massive theta decay?"**

---

## Why Variance for Crashes?


### 1. Crash Mechanics


**What happens in crashes:**

**Volatility explosion:**
- Normal market: VIX ≈ 15 (σ ≈ 15%)
- Crash: VIX → 60-80 (σ → 60-80%)
- Variance: 225 → 3,600-6,400 (16x-28x increase!)

**Price cascade:**
- Stocks fall 30-50%
- Portfolio drawdown severe
- Diversification fails (correlation → 1)

**Timing unpredictable:**
- No warning signals
- Days or hours to unfold
- Need protection in place

### 2. Traditional Put Problems


**Why puts are suboptimal:**

**Theta decay:**
- OTM puts lose value daily
- 30-day puts: ~3-5% decay per month
- Annual cost: 30-50% of premium
- **Expensive insurance**

**Strike selection dilemma:**
- ATM puts: Expensive, high theta
- OTM puts: Cheaper but less protection
- Far OTM: Very cheap but only pays in crashes

**Rolling complexity:**
- Need to roll monthly/quarterly
- Transaction costs compound
- Timing risk (when to roll?)

**Skew premium:**
- Put skew makes OTM puts expensive
- Paying for crash insurance premium
- 30-50% markup over ATM

### 3. Variance Swap Advantages


**Why variance swaps are better:**

**No theta decay:**
- Mark-to-market instrument (no premium upfront)
- Daily P&L from realized variance
- No time decay eating returns

**Single trade:**
- Buy 3-6 month variance swap
- Hold to maturity
- No rolling needed

**Linear payoff in variance:**

$$
\text{Payoff} = N_{\text{var}} \times (\sigma_{\text{realized}}^2 - K_{\text{var}})
$$

**In crash (vol 15% → 60%):**

$$
\text{Payoff} = N_{\text{var}} \times (3,600 - 225) = 3,375 \times N_{\text{var}}
$$

**Massive payoff when you need it!**

**Unlimited upside:**
- No cap on payoff
- Bigger crash = bigger payout
- Perfect tail hedge

### 4. Cost Comparison


**Example: $10M portfolio, 6-month protection**

**Option A: Rolling puts**
- Buy 10% OTM puts monthly
- Premium: ~1.5% per month
- Annual cost: 18% of portfolio
- **Cost: $\$1,800,000/year**

**Option B: Variance swap**
- Buy 6-month variance, strike = 225 (15% vol)
- Vega notional: $\$50,000$ per 1% vol
- Initial MTM: $0 (mark-to-market)
- **Cost: $\$0 upfront**

**If no crash:**
- Puts: Lost $\$1,800,000$ (full premium)
- Variance: Lost $\sim \$200,000$ (variance risk premium)

**If crash (vol 15% → 50%):**
- Puts: +$\$3,000,000$ (30% portfolio decline hedged)
- Variance: +$\$1,750,000$ (50% - 15%) × $\$50,000

**Variance cheaper and effective!**

### 5. Convexity Benefits


**Variance swaps super-convex in crashes:**

**Small crash (vol 15% → 25%):**
- Variance: 225 → 625 (+400 points)
- Payoff: 400 × $N_{\text{var}}$

**Large crash (vol 15% → 50%):**
- Variance: 225 → 2,500 (+2,275 points)
- Payoff: 2,275 × $N_{\text{var}}$ (5.7× larger!)

**Mega crash (vol 15% → 80%):**
- Variance: 225 → 6,400 (+6,175 points)
- Payoff: 6,175 × $N_{\text{var}}$ (15.4× larger!)

**Payoff grows quadratically with volatility increase!**

### 6. Historical Performance


**Empirical evidence (crashes):**

**1987 Black Monday:**
- Vol: 20% → 150% (peak)
- Variance: 400 → 22,500
- Variance hedge payoff: 22,100 × $N_{\text{var}}$ (55x strike!)

**2008 Financial Crisis:**
- Vol: 25% → 80%
- Variance: 625 → 6,400
- Payoff: 5,775 × $N_{\text{var}}$ (9.2x strike)

**2020 COVID:**
- Vol: 15% → 85%
- Variance: 225 → 7,225
- Payoff: 7,000 × $N_{\text{var}}$ (31x strike!)

**Variance swaps delivered exactly when needed**

### 7. Portfolio Integration


**Sizing variance hedge:**

Target: Offset 50% of 30% portfolio drawdown = 15% protection

**Example:**
- $\$10M$ portfolio
- Want $\$1.5M$ protection in crash

**If crash = vol 15% → 50%:**
- Variance move: 2,500 - 225 = 2,275 points

**Required variance notional:**

$$
N_{\text{var}} = \frac{\$1,500,000}{2,275} \approx \$660 \text{ per variance point}
$$

**Vega equivalent:**

$$
N_{\text{vega}} = N_{\text{var}} \times 2 \times 15\% = \$660 \times 0.30 = \$198 \text{ per 1\% vol}
$$

**Small notional, huge crash payoff!**

---

## Variance Hedge Structures


**Different ways to implement:**

### 1. Plain Vanilla Hedge


**Structure:**

- Buy long-dated variance swap (6-12 months)
- Strike at current implied variance
- Hold to maturity
- No adjustments

**Example:**
- Buy 6M variance, strike = 225 (15% vol)
- Vega: $\$20,000$ per 1% vol
- Cost: $0 upfront (MTM)

**Payoff scenarios:**

**Normal year (realized 12%):**
- Realized variance: 144
- Loss: $(225 - 144) \times \$667 = -\$54,000$
- **Cost of insurance**

**Crash (realized 40%):**
- Realized variance: 1,600
- Gain: $(1,600 - 225) \times \$667 = +\$917,000$
- **Offset portfolio losses**

### 2. Tiered Protection


**Structure:**

- Buy multiple variance swaps at different strikes
- Lower strikes (ATM): Smaller notional
- Higher strikes (OTM-equivalent): Larger notional
- Ramp up protection for tail events

**Example:**
- $\$300/point at strike 225 (15% vol)
- $\$500/point at strike 400 (20% vol, synthetic)
- $\$1,000/point at strike 900 (30% vol, synthetic)

**In mega crash (vol → 60%):**
- Strike 225: $(3,600 - 225) \times \$300 = +\$1,012,500$
- Strike 400: $(3,600 - 400) \times \$500 = +\$1,600,000$
- Strike 900: $(3,600 - 900) \times \$1,000 = +\$2,700,000$
- **Total: $\$5,312,500$ (massive tail protection!)**

**Cost lower than single large notional**

### 3. Calendar Spread Hedge


**Structure:**

- Buy long-dated variance (6-12M)
- Sell short-dated variance (1-3M) partially
- Reduce near-term VRP cost
- Keep long-term crash protection

**Example:**
- Buy 12M variance, $\$1,000/point
- Sell 3M variance, $\$400/point (40% offset)

**Benefits:**
- Harvest short-term VRP (reduce cost)
- Maintain long-term tail hedge
- Net cost: 60% of long-only

**Risk:**
- Near-term crash hurts (short variance loss)
- Better for "slow build" crash scenarios

### 4. Dispersion-Funded Hedge


**Structure:**

- Buy index variance (protection)
- Sell single-stock variances (funding)
- Correlation collapse in crashes = both legs win!

**Example:**
- Buy SPX variance: $\$1,000/point
- Sell 10 stocks: $\$100/point each (net $\$1,000)

**In crash:**
- SPX variance explodes (long wins big)
- Stock variances rise less (short loses)
- But correlation spikes → index outperforms stocks
- **Net positive in crashes**

**Normal markets:**
- Harvest VRP from stock shorts
- Pay VRP on index long
- Net cost reduced (50-70% of pure index long)

### 5. Strike Spread Hedge


**Structure:**

- Buy ATM variance
- Sell deep OTM variance (synthetic)
- Defined maximum payoff
- Cheaper than pure long

**Example:**
- Buy variance strike 225
- Sell variance strike 2,500 (50% vol, synthetic)
- Max payoff capped at 2,275 points

**In moderate crash (vol → 40%):**
- Realized variance: 1,600
- Payoff: $1,600 - 225 = 1,375$ points (full)

**In mega crash (vol → 60%):**
- Realized variance: 3,600
- Payoff: $\min(3,600 - 225, 2,275) = 2,275$ points (capped)

**Cost: 40-60% of unlimited upside hedge**

### 6. Dynamic Variance Hedge


**Structure:**

- Start with baseline variance hedge
- Scale up when VIX rises (vol clustering)
- Scale down when VIX falls
- Adaptive protection

**Rule:**

$$
N_{\text{var}}(t) = N_{\text{base}} \times \left(1 + \alpha \times \frac{\text{VIX}_t - 15}{15}\right)
$$

**Example:**
- Base: $\$500/point
- $\alpha = 0.5$
- VIX = 25

**Current notional:**
$$
N(t) = \$500 \times \left(1 + 0.5 \times \frac{25-15}{15}\right) = \$500 \times 1.33 = \$667/\text{point}
$$

**Benefits:**
- More protection when crash likely (high VIX)
- Less cost when calm (low VIX)

### 7. Conditional Variance Hedge


**Structure:**

- Start unhedged
- Activate hedge when VIX > threshold (e.g., 25)
- Avoid paying VRP in normal times
- Buy protection when risks rise

**Implementation:**

```
IF VIX > 25:
    Buy variance swap, notional = $1,000/point
ELSE:
    No hedge
```

**Trade-off:**
- Saves cost in low-vol regimes (80% of time)
- Catches most crashes (VIX spikes before crashes)
- Risk: Flash crash (no time to hedge)

---

## Mathematical Framework


### 1. Hedge Sizing Formula


**Target: Offset portfolio loss in crash**

Given:
- Portfolio value: $V$
- Crash scenario: $\sigma_{\text{crash}}$
- Current vol: $\sigma_0$
- Target offset: $\beta$ (e.g., 0.5 for 50%)
- Portfolio drawdown in crash: $\delta$ (e.g., 0.3 for 30%)

**Required variance notional:**

$$
N_{\text{var}} = \frac{\beta \times \delta \times V}{\sigma_{\text{crash}}^2 - \sigma_0^2}
$$

**Example:**
- $V = \$10M$
- $\beta = 0.5$ (hedge 50%)
- $\delta = 0.3$ (30% drawdown)
- $\sigma_0 = 15\%$, $\sigma_{\text{crash}} = 50\%$

**Required notional:**

$$
N_{\text{var}} = \frac{0.5 \times 0.3 \times \$10M}{2,500 - 225} = \frac{\$1.5M}{2,275} = \$660/\text{point}
$$

### 2. Cost-Benefit Analysis


**Expected cost of hedge:**

$$
\text{Cost} = \mathbb{E}[K_{\text{var}} - \text{RV}] \times N_{\text{var}}
$$

**Empirically:**
- VRP ≈ 100 variance points annually
- Annual cost: $100 \times \$660 = \$66,000$
- **0.66% of portfolio**

**Benefit in crash:**
- Offset: $\$1,500,000$ (15% of portfolio)
- Cost: $\$66,000$ annually

**Crash frequency: ~5-10 years**
- Total cost over 10 years: $\$660,000$
- Crash benefit: $\$1,500,000$
- **Net benefit: $\$840,000$ (positive expected value!)**

### 3. Optimal Hedge Ratio


**Minimize portfolio variance:**

$$
\beta^* = \frac{\text{Cov}(\text{Portfolio}, \text{Variance})}{\text{Var}(\text{Variance})}
$$

**Empirically:**
- Stock portfolio: $\beta^* \approx 0.4\text{-}0.6$
- Don't fully hedge (diminishing returns)

**Practical:**
- Hedge 40-60% of expected crash loss
- Full hedge too expensive
- Tail events have low probability (overhedging costly)

### 4. Greeks Analysis


**For long variance hedge:**

**Delta:**

$$
\Delta = 0 \quad \text{(variance insensitive to price)}
$$

**Vega:**

$$
\text{Vega} = N_{\text{var}} \times 2\sigma_0
$$

**Gamma (in variance terms):**

$$
\Gamma = N_{\text{var}} \times 2
$$

**Theta:**

$$
\Theta \approx -N_{\text{var}} \times \text{VRP}
$$

**Negative theta from paying variance risk premium**

### 5. Convexity Measure


**Variance payoff convexity:**

$$
\frac{\partial^2 \text{Payoff}}{\partial \sigma^2} = N_{\text{var}} \times 2 > 0
$$

**Positive convexity: Payoff accelerates with volatility**

**Example:**
- Vol 15% → 25%: Gain = 400 × $N$
- Vol 25% → 35%: Gain = 600 × $N$ (50% more!)
- Vol 35% → 45%: Gain = 800 × $N$ (100% more!)

### 6. Portfolio Risk Reduction


**Portfolio variance with hedge:**

$$
\text{Var}(\text{Portfolio + Hedge}) = \text{Var}(\text{Portfolio}) + \text{Var}(\text{Hedge}) + 2\text{Cov}(\text{Portfolio}, \text{Hedge})
$$

**In crashes:**
- $\text{Cov}(\text{Portfolio}, \text{Hedge}) < 0$ (large negative)
- Portfolio risk reduced dramatically

**Empirical reduction:**
- Unhedged portfolio CVaR (95%): -35%
- Hedged portfolio CVaR (95%): -20%
- **Tail risk reduced 43%!**

### 7. Multi-Period Hedging


**Rolling hedges strategy:**

$$
N_{\text{var}}^{(i)} = N_{\text{base}} \times e^{-\lambda \times t_i}
$$

Where:
- $\lambda$ = Decay rate (0 for static, > 0 for decreasing)
- $t_i$ = Time since inception

**Example:**
- Year 1: $\$1,000/point
- Year 2: $\$1,000 × e^{-0.2 \times 1} = \$819/point
- Year 3: $\$1,000 × e^{-0.2 \times 2} = \$670/point

**Rationale:**
- Long without crash → Portfolio grown → Need more protection
- But diminishing returns → Reduce hedge intensity

---

## Common Mistakes


**Pitfalls to avoid:**

### 1. Undersizing the Hedge


**Mistake:** Tiny variance hedge won't help

**Why it fails:** Crashes cause huge losses

**Example:**
- $\$10M$ portfolio
- Buy $\$100/point variance
- Crash: vol 15% → 50% (variance +2,275)
- Hedge gain: $2,275 × \$100 = \$227,500$
- Portfolio loss: $\$3,000,000$ (30% drawdown)
- **Hedge covers only 7.6% of loss!**

**Fix:**
- Size for meaningful offset (40-60% of crash loss)
- Use hedge sizing formula
- Back-test against historical crashes

### 2. Overhedging


**Mistake:** Massive variance notional

**Why it fails:** Expensive drag in normal years

**Example:**
- Buy $\$5,000/point variance
- Annual VRP cost: $100 × \$5,000 = \$500,000$
- **5% annual drag!**
- Even with crash, total cost high

**Fix:**
- Optimal hedge ratio: 40-60%
- Don't try to eliminate all risk
- Balance cost vs. benefit

### 3. Wrong Strike Selection


**Mistake:** Buy variance at wrong strike

**Why it fails:** Overpay or underprotect

**Example:**
- Current vol: 15%
- Buy variance strike at 25% (OTM-equivalent)
- In crash to 40%, payoff starts from 25%
- Miss first 10% of vol spike!

**Fix:**
- Buy at-the-money variance (current vol)
- Maximize crash protection
- Don't try to save on strike

### 4. Ignoring VRP


**Mistake:** Forget variance risk premium cost

**Why it fails:** Continuous bleed

**Example:**
- Hold variance hedge 10 years
- Annual VRP: $\$100,000$
- No crashes occur
- **Total cost: $\$1,000,000$**

**Fix:**
- Accept VRP as insurance cost
- Model expected cost before entering
- Diversify hedge (dispersion-funded)

### 5. Too Short Maturity


**Mistake:** Buy 1-3 month variance

**Why it fails:** Need to roll frequently

**Example:**
- Buy 1M variance
- Roll 12 times/year
- Transaction cost: 10 variance points/roll
- Annual cost: $10 × 12 = 120$ points (exceeds VRP!)

**Fix:**
- Buy 6-12 month variance
- Roll less frequently (annually)
- Reduce transaction costs

### 6. No Rebalancing


**Mistake:** Set and forget forever

**Why it fails:** Portfolio size changes

**Example:**
- Start: $\$10M$ portfolio, $\$1,000/point hedge
- 5 years later: $\$25M$ portfolio (grown), same hedge
- Hedge now covers only 1.5% of losses
- **Underhedged!**

**Fix:**
- Rebalance hedge annually
- Scale with portfolio size
- Or use % of portfolio rule

### 7. Forgetting Correlation Spike


**Mistake:** Assume hedge uncorrelated in crashes

**Why it fails:** Correlation matters for offset

**Example:**
- Portfolio: 50% stocks, 50% bonds
- Bonds rally in crashes (negative correlation)
- Hedge only needs to offset stock half
- **But sized for full portfolio**

**Fix:**
- Adjust hedge for portfolio composition
- Only hedge equity portion (mostly)
- Bonds provide natural hedge

### 8. Single Variance Only


**Mistake:** Only one variance hedge

**Why it fails:** Concentration risk

**Example:**
- Only long SPX variance
- Single-stock blowup (not systemic)
- SPX barely moves
- **Hedge doesn't pay**

**Fix:**
- Diversify: SPX + sector variances
- Or: Multiple country indices
- Capture broader crash scenarios

---

## Risk Management Rules


### 1. Sizing Guideline


**Maximum hedge cost:**

$$
\text{Max Annual Cost} = \min\left(2\% \times \text{Portfolio}, \, \frac{\text{Expected Crash Loss}}{5}\right)
$$

**Example:**
- $\$10M$ portfolio
- Expected crash: 30% loss = $\$3M$
- Max cost: $\min(2\% × \$10M, \$3M/5) = \min(\$200,000, \$600,000) = \$200,000$

**This implies:**

$$
N_{\text{var}} = \frac{\$200,000}{\text{Annual VRP}} = \frac{\$200,000}{100} = \$2,000/\text{point}
$$

### 2. Rebalancing Schedule


**Annual rebalancing:**

- Check portfolio size (grown or shrunk?)
- Recalculate hedge notional
- Adjust variance position (buy more or reduce)

**Example:**
- Year 1: $\$10M$ portfolio → $\$1,000/point
- Year 2: $\$12M$ portfolio → $\$1,200/point
- Buy additional $\$200/point variance

### 3. Strike Selection


**Always use ATM:**

- Current implied variance = Strike
- Maximizes crash payoff
- No "gap risk" (missing first part of spike)

**Avoid:**
- OTM-equivalent strikes (vol > current)
- Save on cost but lose protection

### 4. Maturity Choice


**Optimal: 6-12 months**

- Long enough to avoid frequent rolling
- Short enough to reset if portfolio changes
- Balance transaction costs vs. flexibility

**Avoid:**
- < 3 months (too frequent rolling)
- > 2 years (too inflexible)

### 5. Monitoring


**Quarterly review:**

- Check MTM P&L (variance hedge)
- Confirm portfolio size
- Verify hedge still appropriate
- Adjust if needed

**Annual rebalance:**

- Roll expiring variance
- Size new hedge to current portfolio
- Review crash scenarios

### 6. Diversification


**Spread variance hedge across:**

- Multiple maturities (6M, 9M, 12M)
- Multiple indices (SPX, NDX, Russell)
- Mix with other hedges (OTM puts for single-stock crashes)

**Don't:**
- Put all hedge in single variance swap
- Ignore idiosyncratic risks

### 7. Cost Tracking


**Monitor ongoing costs:**

- MTM variance hedge daily
- Compute annual VRP paid
- Track cumulative cost vs. benefit

**Action triggers:**

- If cost > 3% annually → Reduce hedge
- If no crash in 10 years → Reevaluate need
- If portfolio composition changes → Adjust

---

## Real-World Examples


### 1. Pre-COVID Hedge (2019)


**Setup:**
- Dec 2019: $\$50M$ portfolio
- Bought 6M variance: $\$5,000/point
- Strike: 225 (15% vol)

**Cost:**
- Jan-Feb 2020: -$\$25,000/month (VRP bleed)
- Total cost through Feb: -$\$50,000$

**Outcome:**
- March crash: Vol spiked 15% → 70%
- Realized variance: 4,900
- Payoff: $(4,900 - 225) × \$5,000 = \$23,375,000$
- Portfolio loss: -$\$15,000,000$ (30% drawdown)
- **Net: +$\$8,375,000$ (gain after offsetting loss!)**

**Lesson:** Variance hedge paid off massively in crash

### 2. Long-Term Hedge (2010-2020)


**Setup:**
- Continuous variance hedge, 10 years
- $\$20M$ portfolio
- $\$1,500/point hedge maintained

**Costs:**
- Annual VRP: ~$\$150,000$
- Total 10 years: $\$1,500,000$

**Crashes captured:**
- 2011 Euro crisis: +$\$450,000$
- 2015 Flash crash: +$\$300,000$
- 2018 Volmageddon: +$\$200,000$
- 2020 COVID: +$\$7,000,000$
- **Total gains: $\$7,950,000$**

**Net over 10 years:**
- Gains: $\$7,950,000$
- Costs: $\$1,500,000$
- **Net: +$\$6,450,000$ (positive!)

**Lesson:** Long-term hedge can be profitable

### 3. Under-Hedged Portfolio (2008)


**Setup:**
- $\$100M$ portfolio
- Variance hedge: $\$2,000/point (too small!)
- Strike: 625 (25% vol, elevated already)

**Outcome:**
- Financial crisis: Vol → 80%
- Realized variance: 6,400
- Payoff: $(6,400 - 625) × \$2,000 = \$11,550,000$
- Portfolio loss: -$\$50,000,000$ (50% drawdown)
- **Hedge covered only 23% of loss**

**Lesson:** Size matters! Don't underhedge.

### 4. Dispersion-Funded Hedge (2014-2016)


**Setup:**
- Buy SPX variance: $\$3,000/point
- Sell 20 stock variances: $\$150/point each (net -$\$3,000)
- Funded hedge (net zero vega)

**Outcome:**
- Normal years (2014-2015):
  - SPX realized < strike: -$\$90,000/year
  - Stocks realized < strike: +$\$120,000/year
  - **Net: +$\$30,000/year (positive carry!)**

- 2015-2016 volatility spikes:
  - Multiple mini-spikes
  - Correlation rose → SPX outperformed
  - **Net: +$\$200,000$ over period**

**Lesson:** Funding via dispersion reduces/eliminates cost

---

## Practical Steps


### 1. Assess Portfolio Risk


**Before hedging, analyze:**

1. **Crash sensitivity:**
   - Historical beta to VIX
   - Drawdown in 2008, 2020
   - Expected loss in 30% market crash

2. **Current vol regime:**
   - VIX level (low < 15, high > 25)
   - Term structure (contango or backwardation)
   - Implied variance strike

3. **Portfolio composition:**
   - Equity allocation (needs hedge)
   - Bond allocation (natural hedge)
   - Alternatives (diversification)

### 2. Size the Hedge


**Calculate notional:**

$$
N_{\text{var}} = \frac{\beta \times \delta \times V}{\sigma_{\text{crash}}^2 - \sigma_0^2}
$$

**Example:**
- Portfolio: $\$10M$
- Target offset ($\beta$): 50%
- Expected crash drawdown ($\delta$): 30%
- Current vol ($\sigma_0$): 15%
- Crash vol ($\sigma_{\text{crash}}$): 50%

**Required notional:**

$$
N_{\text{var}} = \frac{0.5 × 0.3 × \$10M}{2,500 - 225} = \$660/\text{point}
$$

### 3. Choose Structure


**Decide on hedge type:**

- **Plain vanilla:** Simplest, most transparent
- **Calendar spread:** If want to reduce cost
- **Dispersion-funded:** If willing to manage actively
- **Tiered:** If want more tail protection

**Example decision:**
- Retail investor → Plain vanilla
- Institutional → Dispersion-funded
- Ultra-conservative → Tiered

### 4. Execute


**Enter the hedge:**

- Get quotes from multiple dealers
- Check strike (should be ATM)
- Verify notional calculation
- Confirm maturity (6-12 months)

**Example:**
- Request quotes for 6M SPX variance
- Strike: 225 (current implied)
- Notional: $\$660/point
- Compare 3 dealers, pick best

### 5. Monitor


**Ongoing management:**

**Daily:**
- Check MTM P&L (variance hedge)
- Note realized variance accrual
- Monitor VIX/vol regime

**Monthly:**
- Compute cumulative cost (VRP paid)
- Track portfolio value changes
- Verify hedge still sized appropriately

**Quarterly:**
- Full performance review
- Compare cost vs. benefit
- Adjust if portfolio changed >10%

### 6. Rebalance


**Annual rebalancing:**

- Roll expiring variance swap
- Recalculate notional for new portfolio size
- Adjust hedge accordingly

**Example:**
- Original: $\$10M$ portfolio, $\$660/point
- Now: $\$12M$ portfolio
- New hedge: $\$660 × 12/10 = \$792/point$
- Buy additional $\$132/point variance

---

## Final Wisdom


> "Variance swaps are the ultimate crash protection tool - they provide unlimited upside in volatility with no theta decay, covering your portfolio for 6-12 months with a single trade. The cost is the variance risk premium, essentially an insurance fee of 1-2% annually. This is dramatically cheaper than rolling OTM puts and far more effective during tail events when variance explodes quadratically. Size the hedge to offset 40-60% of expected crash losses, not 100% (diminishing returns and too expensive). Monitor annually, rebalance as your portfolio grows, and accept the VRP cost as the price of sleeping well at night. The math is simple: one major crash every 10 years will more than pay for a decade of hedging."

**Key to success:**

- Size hedge using the formula: $N_{\text{var}} = (\beta × \delta × V) / (\sigma_{\text{crash}}^2 - \sigma_0^2)$
- Target 40-60% crash loss offset (not 100%)
- Use 6-12 month maturities (minimize rolling costs)
- Buy at-the-money variance (maximize protection)
- Rebalance annually as portfolio grows
- Accept 1-2% annual VRP cost as insurance premium
- Consider dispersion-funded structure to reduce cost
- Remember: Variance payoff is quadratic in volatility - perfect for tail hedging
