# Volatility Swaps


**Volatility swaps** are forward contracts on realized volatility where you exchange a fixed strike (agreed upfront) for the realized volatility of an underlying asset over a specified period, providing convex exposure to volatility movements.

---

## The Core Insight


**The fundamental idea:**

- You want exposure to volatility, not variance
- Variance swaps payoff linear in variance (vol squared)
- Volatility swaps payoff linear in volatility itself
- Convexity makes vol swaps more expensive than variance swaps
- Pay/receive difference between realized and strike volatility
- Better for directional vol views (up or down)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/volatility_swap_payoff.png?raw=true" alt="volatility_swap_payoff" width="700">
</p>
**Figure 1:** Volatility swap payoff diagram showing linear exposure to realized volatility minus strike volatility, with notional measured in vega units (currency per percentage point).

**You're essentially betting: "Realized volatility will differ from strike volatility, and I want exposure to that difference directly."**

---

## What Are Vol Swaps?


### 1. Pure Vol Exposure


**Linear in volatility:**

**Definition:** A forward contract where at maturity you receive:

$$
\text{Payoff} = N_{\text{vega}} \times (\sigma_{\text{realized}} - K_{\text{vol}})
$$

Where:
- $N_{\text{vega}}$ = Vega notional (currency per 1% volatility)
- $\sigma_{\text{realized}}$ = Realized volatility over the period (annualized %)
- $K_{\text{vol}}$ = Strike volatility (agreed at inception, in %)

**Key properties:**

- Payoff linear in volatility (not variance!)
- More intuitive for traders
- Convex payoff in variance terms
- More expensive than variance swaps
- Settlement based on square root of realized variance

### 2. Vol vs Variance Swaps


**Critical comparison:**

**Variance swap payoff:**

$$
\text{Payoff}_{\text{var}} = N_{\text{var}} \times (\sigma_{\text{realized}}^2 - K_{\text{var}})
$$

**Volatility swap payoff:**

$$
\text{Payoff}_{\text{vol}} = N_{\text{vega}} \times (\sigma_{\text{realized}} - K_{\text{vol}})
$$

**Relationship between strikes:**

$$
K_{\text{vol}} > \sqrt{K_{\text{var}}}
$$

**Why?** Convexity adjustment (Jensen's inequality)

**Example:**

- Variance strike: $K_{\text{var}} = 400$ (20% vol)
- Volatility strike: $K_{\text{vol}} \neq 20\%$, actually $\approx 20.5\%$

**The convexity premium makes vol swaps more expensive.**

### 3. Realized Vol Calculation


**How realized volatility is computed:**

Given realized variance:

$$
\sigma_{\text{realized}}^2 = \frac{252}{n} \sum_{i=1}^{n} r_i^2
$$

Take the square root:

$$
\sigma_{\text{realized}} = \sqrt{\frac{252}{n} \sum_{i=1}^{n} r_i^2}
$$

Where:
- $r_i = \ln(S_i/S_{i-1})$ = Log return on day $i$
- $n$ = Number of observations
- $252$ = Annualization factor

**Key points:**

- Same variance calculation as variance swaps
- Then take square root for volatility
- Result is in percentage points (e.g., 22.5%)
- Always positive by construction

**Example:**

- 3-month swap, 63 trading days
- Realized variance = 506
- **Realized volatility:** $\sigma_{\text{realized}} = \sqrt{506} = 22.5\%$

### 4. Strike Determination


**How volatility strike is set:**

At inception, strike set so swap has zero value:

$$
K_{\text{vol}} = \mathbb{E}^Q[\sigma_{\text{realized}}] + \text{Convexity Adjustment}
$$

**The convexity adjustment:**

$$
\text{Convexity} \approx \frac{\mathbb{E}^Q[\sigma_{\text{realized}}^2] - (\mathbb{E}^Q[\sigma_{\text{realized}}])^2}{2\mathbb{E}^Q[\sigma_{\text{realized}}]}
$$

**Practical approximation:**

$$
K_{\text{vol}} \approx \sqrt{K_{\text{var}}} + \frac{\text{Var}(\sigma^2)}{8K_{\text{var}}^{3/2}}
$$

**Example:**

- Variance strike: $K_{\text{var}} = 400$ (20% vol)
- Variance of variance: $\text{Var}(\sigma^2) = 1,600$

**Volatility strike:**

$$
K_{\text{vol}} \approx \sqrt{400} + \frac{1,600}{8 \times 400^{3/2}} = 20\% + 0.5\% = 20.5\%
$$

**Vol swaps always more expensive than $\sqrt{\text{variance strike}}$**

### 5. Vega Notional


**Converting between notionals:**

For volatility swaps, vega notional is direct:

$$
N_{\text{vega}} = \text{Currency per 1\% volatility change}
$$

**Example:**

- Want $\$100,000$ vega exposure
- Strike volatility: $K_{\text{vol}} = 20\%$
- Vega notional: $N_{\text{vega}} = \$100,000$ per 1% vol

**If realized vol = 25%:**

$$
\text{Payoff} = \$100,000 \times (25\% - 20\%) = \$500,000
$$

**Compare to variance swap:**

- Same $\$100,000$ vega desired
- Variance notional: $N_{\text{var}} = \$100,000/(2 \times 20\%) = \$2,500$
- Realized variance: $625$ (25% vol)
- Payoff: $\$2,500 \times (625 - 400) = \$562,500$

**Volatility swap pays less due to square root transformation!**

### 6. Mark-to-Market


**Daily P&L before settlement:**

Volatility swaps marked based on forward volatility:

$$
\text{MTM} = N_{\text{vega}} \times \left(K_{\text{vol}}^{\text{forward}} - K_{\text{vol}}\right) \times e^{-r(T-t)}
$$

Where:
- $K_{\text{vol}}^{\text{forward}}$ = Current forward volatility strike
- Derived from option prices at time $t$
- Requires convexity adjustment from variance

**P&L sources:**

1. **Realized volatility accrual:**
   - As days pass, realized vol materializes
   - Contributes to final payoff

2. **Forward volatility changes:**
   - If implied vol rises → long position gains
   - If implied vol falls → long position loses
   - Reflects expected future volatility

**Example:**

- Long vol swap, strike = 20%
- After 1 month, forward vol = 23%
- Vega notional = $\$100,000$
- Time to maturity = 2 months, $r = 5\%$

**MTM gain:**

$$
\text{MTM} = \$100,000 \times (23\% - 20\%) \times e^{-0.05 \times 2/12} = \$298,760
$$

### 7. Replication Portfolio


**How dealers hedge volatility swaps:**

Volatility swaps harder to replicate than variance swaps:

**Approximate replication:**

- Start with variance swap replication
- Add dynamic hedge for convexity
- Or use variance swap + options on variance

**Static replication (imperfect):**

$$
\text{Vol Swap} \approx \frac{1}{2\sigma_{\text{ATM}}} \times \text{Variance Swap} + \text{Correction Term}
$$

**Challenges:**

- No perfect static hedge
- Requires continuous rebalancing
- More expensive to hedge (dealers charge more)
- Convexity harder to capture

**Dealer perspective:**

- Sell volatility swap to client
- Approximate hedge with variance swap
- Dynamic overlay for convexity
- Profit from bid-ask and convexity premium

---

## Why Trade Vol Swaps?


**Use cases for volatility exposure:**

### 1. Intuitive Vol Bets


**Think in volatility terms:**

Traders naturally think in volatility (%), not variance:

- "Vol will go from 20% to 25%" (makes sense)
- "Variance will go from 400 to 625" (less intuitive)

**Volatility swaps allow:**

- Direct betting on vol levels
- Easier P&L calculation
- More natural for risk management
- Better for explaining to clients

**Example:**

- Expect vol to rise 5%
- Long vol swap with $\$100,000$ vega

**If right:**

$$
\text{Profit} = \$100,000 \times 5\% = \$500,000
$$

**Simple, intuitive calculation!**

### 2. Convexity Preference


**Long volatility benefits from convexity:**

Volatility swaps have built-in convexity vs. variance swaps:

**Scenario:** Vol moves from 20% to 30% (+10%)

**Variance swap payoff:**

- Variance: $400 \to 900$ (+500 points)
- With $\$2,500$ notional: $\$2,500 \times 500 = \$1,250,000$

**Volatility swap payoff:**

- Vol: $20\% \to 30\%$ (+10%)
- With $\$100,000$ vega: $\$100,000 \times 10\% = \$1,000,000$

**Vol swap pays less due to concavity in variance terms, but if you're betting on vol doubling:**

**Vol: 20% → 40%**

- Variance swap: $400 \to 1,600$ (+1,200) = $\$3,000,000$
- Vol swap: $\$100,000 \times 20\% = \$2,000,000$

**Trade-off:** Vol swaps more expensive upfront (higher strike), but simpler payoff structure

### 3. Downside Protection


**Long vol swaps for hedging:**

When buying volatility for protection:

- Vol swaps pay linearly in vol
- Easier to size hedge (think in vol terms)
- Better for extreme moves (convexity helps)

**Example hedge:**

- $\$10M$ portfolio, want vol hedge
- Expect vol to spike from 15% to 40% in crisis
- Buy vol swap: $\$40,000$ vega per 1%

**In crash scenario (vol to 40%):**

$$
\text{Hedge gain} = \$40,000 \times (40\% - 15\%) = \$1,000,000
$$

**Offsets 10% portfolio drawdown.**

### 4. Vol Spread Trades


**Bet on vol differentials:**

Volatility swaps easier for relative value:

**Example:** Short-term vs. long-term vol

- Long 1-month vol swap (expect spike)
- Short 6-month vol swap (expect normalization)
- P&L in intuitive vol units

**Trade setup:**

- 1M vol strike: 18%
- 6M vol strike: 22%
- Long 1M, short 6M (calendar spread)

**If term structure inverts:**

- 1M realized: 25% (+7%)
- 6M realized: 20% (-2%)
- **Net P&L:** $(+7\%) + (-(-2\%)) = +9\%$ of vega notional

### 5. Cross-Asset Vol Trades


**Trade relative volatility:**

**Example:** Equity vol vs. FX vol

- Long equity vol swap (expect spike)
- Short FX vol swap (stable)
- Bet on correlation structure

**When it works:**

- Risk-off events (equity vol ↑, FX stable)
- Asset-specific shocks
- Divergence in vol regimes

### 6. Tail Risk Hedging


**Pure tail protection:**

Vol swaps provide clean tail hedge:

- Linear payoff in vol (unlimited upside)
- No theta decay (mark-to-market instrument)
- Set and forget until maturity
- Better than rolling options

**Advantage over variance swaps:**

- Easier to explain to risk committee
- More intuitive sizing
- Natural language: "vol spikes to X%"

### 7. Vol Arbitrage


**Exploit vol mispricing:**

**Vol swap vs. straddle:**

- If vol swap cheap vs. ATM straddle
- Buy vol swap, sell delta-hedged straddle
- Profit from basis

**Vol swap vs. variance swap:**

- If convexity premium too large/small
- Trade the spread
- Capture relative value

---

## Mathematical Framework


### 1. Payoff Structure


**At maturity $T$:**

$$
\text{Payoff}_{\text{long}} = N_{\text{vega}} \times \left(\sigma_{\text{realized}} - K_{\text{vol}}\right)
$$

**For short volatility:**

$$
\text{Payoff}_{\text{short}} = N_{\text{vega}} \times \left(K_{\text{vol}} - \sigma_{\text{realized}}\right)
$$

**Key properties:**

- Linear in volatility (not variance!)
- Simpler P&L calculation
- More expensive strike than variance swaps
- Concave in variance terms

### 2. Fair Value Pricing


**Volatility swap fair value:**

Under risk-neutral measure:

$$
K_{\text{vol}} = \mathbb{E}^Q[\sigma_{\text{realized}}]
$$

**But realized vol is:**

$$
\sigma_{\text{realized}} = \sqrt{\frac{1}{T}\int_0^T \sigma_t^2 dt}
$$

**Jensen's inequality gives:**

$$
\mathbb{E}^Q[\sigma_{\text{realized}}] > \sqrt{\mathbb{E}^Q[\sigma_{\text{realized}}^2]}
$$

**Therefore:**

$$
K_{\text{vol}} > \sqrt{K_{\text{var}}}
$$

**The difference is the convexity adjustment.**

### 3. Convexity Adjustment


**Relationship to variance:**

Using Taylor expansion around $\mathbb{E}[\sigma^2]$:

$$
\mathbb{E}[\sigma] \approx \sqrt{\mathbb{E}[\sigma^2]} - \frac{\text{Var}(\sigma^2)}{8(\mathbb{E}[\sigma^2])^{3/2}}
$$

**Convexity premium:**

$$
\text{Convexity} = K_{\text{vol}} - \sqrt{K_{\text{var}}} \approx \frac{\text{Var}(\sigma^2)}{8K_{\text{var}}^{3/2}}
$$

**Typical values:**

- For $K_{\text{var}} = 400$ (20% vol)
- Var(variance) ≈ 1,600
- **Convexity ≈ 0.4-0.6% vol**

**Higher variance of variance → larger convexity adjustment**

### 4. Greeks


**Volatility vega:**

$$
\text{Vega} = N_{\text{vega}}
$$

**Simple: $1 per 1% volatility change by construction!**

**Gamma (in variance terms):**

$$
\text{Gamma}_{\text{var}} = \frac{N_{\text{vega}}}{2\sigma}
$$

**Delta:**

$$
\text{Delta} = 0 \quad \text{(by construction)}
$$

**Theta:**

As time passes, volatility accrues:

$$
\theta = N_{\text{vega}} \times \frac{\partial \sigma_{\text{realized}}}{\partial t}
$$

Where the partial derivative depends on new returns added.

### 5. Vol of Vol Exposure


**Sensitivity to vol changes:**

Volatility swaps have exposure to volatility of volatility:

$$
\text{Volvol Sensitivity} = N_{\text{vega}} \times \frac{\partial K_{\text{vol}}}{\partial \text{Volvol}}
$$

**Higher vol-of-vol → higher convexity adjustment → higher strike**

**This means:**

- Long vol swap benefits from stable vol path
- Short vol swap hurt by high vol-of-vol
- Convexity is priced into initial strike

### 6. Relationship to Variance


**Converting between instruments:**

Given variance swap with notional $N_{\text{var}}$:

Equivalent vega exposure:

$$
N_{\text{vega}} = N_{\text{var}} \times 2\sigma_{\text{ATM}}
$$

Given vol swap with notional $N_{\text{vega}}$:

Equivalent variance exposure:

$$
N_{\text{var}} = \frac{N_{\text{vega}}}{2\sigma_{\text{ATM}}}
$$

**But payoffs differ due to convexity!**

### 7. Skew Impact


**Option smile affects pricing:**

Volatility swaps more sensitive to skew:

- Deep OTM puts have higher implied vol
- Jump risk priced into wings
- Convexity adjustment captures this

**Skew-adjusted pricing:**

$$
K_{\text{vol}} \approx \sigma_{\text{ATM}} + \text{Skew Adjustment} + \text{Convexity}
$$

**Higher skew → higher vol swap strike**

---

## Common Mistakes


**Pitfalls to avoid:**

### 1. Confusing Vol/Variance


**Mistake:** Treat vol and variance swaps identically

**Why it fails:** Different payoff structures

**Example:**

- Vol moves 20% → 25% (+5%)
- Variance moves 400 → 625 (+225 points)

**Vol swap payoff (per $\$100k vega):**

$$
\$100,000 \times 5\% = \$500,000
$$

**Variance swap payoff (equivalent exposure):**

$$
\$2,500 \times 225 = \$562,500
$$

**Different amounts!**

**Fix:** Understand the instruments are different, choose based on preference

### 2. Ignoring Convexity Cost


**Mistake:** Don't account for higher strike

**Why it fails:** Vol swaps more expensive than $\sqrt{\text{variance strike}}$

**Example:**

- Variance strike: 400 (20% vol)
- Expect vol swap strike = 20%
- Actual vol swap strike = 20.5%

**If realized = 22%:**

**Expected P&L:** $\$100,000 \times (22\% - 20\%) = \$200,000$

**Actual P&L:** $\$100,000 \times (22\% - 20.5\%) = \$150,000$

**Fix:** Always check actual vol strike, don't assume $\sqrt{K_{\text{var}}}$

### 3. Wrong Notional Comparison


**Mistake:** Use same dollar notional for var and vol swaps

**Why it fails:** Different exposures

**Example:**

- $\$100,000$ in variance notional
- $\$100,000$ in vega notional
- **NOT equivalent exposures!**

**At 20% vol:**

- Variance exposure: $\$100,000$ per variance point
- Vega equivalent: $\$100,000 \times 2 \times 20\% = \$4,000,000$ vega!

**Fix:** Convert properly using $N_{\text{vega}} = N_{\text{var}} \times 2\sigma$

### 4. Mispricing Convexity


**Mistake:** Underestimate convexity value

**Why it fails:** Large moves benefit variance more than vol

**Scenario:** Vol spikes 20% → 50%

**Variance swap:**

- Variance: $400 \to 2,500$ (+2,100 points)
- With $\$1,000$ notional: $\$2,100,000$ profit

**Vol swap:**

- Vol: $20\% \to 50\%$ (+30%)
- With $\$70,000$ vega: $\$2,100,000$ profit

**But vol strike was higher! (20.5% vs. 20%)**

**Net: Variance swap more profitable in extreme moves**

**Fix:** If betting on tail events, consider variance swaps for convexity

### 5. Neglecting Vol-of-Vol


**Mistake:** Ignore volatility path dependence

**Why it fails:** Realized vol depends on path

**Example:**

- Case 1: Steady 20% vol for 3 months → realized = 20%
- Case 2: Alternating 10% and 30% vol → realized ≈ 21% (higher!)

**Higher vol-of-vol → higher realized vol (on average)**

**Fix:**

- Account for vol regime changes
- Consider vol-of-vol when pricing
- Long vol benefits from stable paths

### 6. Ignoring Settlement


**Mistake:** Confuse interim MTM with final payoff

**Why it fails:** Final payoff based on cumulative realized vol

**Example:**

- 6-month vol swap, strike = 20%
- After 3 months, realized vol = 30%
- MTM shows large profit

**But if next 3 months realize 10% vol:**

**Average realized vol:**

$$
\sqrt{\frac{30\%^2 + 10\%^2}{2}} \approx 22.4\%
$$

**Final payoff:** $N_{\text{vega}} \times (22.4\% - 20\%) = 2.4\% \times N_{\text{vega}}$

**Much less than MTM suggested!**

**Fix:** Remember settlement based on full-period realized vol

### 7. Overpaying for Hedges


**Mistake:** Buy vol swaps without checking basis

**Why it fails:** Vol swaps expensive vs. alternatives

**Example:**

- Vol swap strike: 20.5% (with convexity)
- Variance swap equivalent: 20%
- ATM straddle implied: 20%

**Vol swap is most expensive hedge!**

**Fix:**

- Compare to variance swaps
- Compare to straddles
- Only use vol swaps if simplicity worth premium

### 8. Wrong Time Horizon


**Mistake:** Trade long-dated vol swaps

**Why it fails:** Convexity adjustment grows with maturity

**For 1-year vol swap:**

- Convexity can be 1-2% vol points
- Makes vol swaps very expensive
- Variance swaps better for long-dated

**Fix:**

- Use vol swaps for short-dated (< 6 months)
- Use variance swaps for long-dated
- Consider cost-benefit of simplicity

---

## Risk Management Rules


### 1. Position Sizing


**Conservative guideline:**

$$
N_{\text{vega}} = \frac{\text{Max Acceptable Loss}}{\text{Max Expected Vol Move}}
$$

**Example:**

- Max loss: $\$100,000$ (1% of portfolio)
- Worst case: Vol moves 20% → 35% (+15%)

**Vega notional:**

$$
N_{\text{vega}} = \frac{\$100,000}{15\%} = \$6,667 \text{ per 1% vol}
$$

**Rule of thumb:** Max 2-3% of portfolio in vega terms

### 2. Comparing Instruments


**Before trading, compare costs:**

1. **Vol swap strike:** $K_{\text{vol}}$ (quoted)
2. **Variance swap strike:** $\sqrt{K_{\text{var}}}$
3. **ATM straddle implied vol:** $\sigma_{\text{ATM}}$

**Typical ranking (most to least expensive):**

$$
K_{\text{vol}} > \sigma_{\text{ATM}} > \sqrt{K_{\text{var}}}
$$

**Choose instrument based on:**

- Simplicity need (vol swap easiest)
- Cost sensitivity (variance swap cheapest)
- Convexity preference (variance for tail events)

### 3. Hedging Tail Risk


**For short vol positions:**

- Buy OTM puts for crash protection
- Cost: 0.5-1% of notional
- Caps downside
- Example: Short vol + long 3-SD OTM put

**For long vol positions:**

- Less critical (upside unlimited)
- Set profit targets (100-200% gain)
- Consider taking profits if implied vol spikes

### 4. Monitoring


**Daily checklist:**

- MTM P&L (from forward vol changes)
- Accrued realized volatility
- Remaining days to settlement
- Implied volatility level
- Vol-of-vol indicators

**Action triggers:**

- MTM loss > 50% → Review thesis
- Implied vol +10% → Consider exit/taking profit
- Realized vol diverging far from strike → Adjust

### 5. Diversification


**Spread risk across:**

- Multiple underlyings (indices, stocks)
- Multiple maturities (1M, 3M, 6M)
- Mix vol and variance swaps
- Combine with other strategies (straddles, VIX)

**Never:**

- More than 25% of vol exposure in single swap
- Short vol without tail hedge
- Ignore cost of convexity

---

## Real-World Examples


### 1. Brexit Vote (June 2016)


**Setup:**

- GBP/USD at 1.50
- Pre-Brexit vol low: 10%
- Bought 1-month vol swap, strike = 11%
- Vega notional: $\$50,000$

**Outcome:**

- Brexit passed, GBP crashed
- Realized vol = 35% over the month
- **Payoff:** $\$50,000 \times (35\% - 11\%) = \$1,200,000$

**Lesson:** Vol swaps perfect for event-driven binary outcomes

### 2. VIX Spike (Feb 2018)


**Setup:**

- SPX at highs, VIX at 9%
- 3-month vol swap, strike = 10%
- Vega notional: $\$100,000$

**Outcome:**

- VIXplosion to 50
- Realized vol = 28% over 3 months
- **Payoff:** $\$100,000 \times (28\% - 10\%) = \$1,800,000$

**Lesson:** Cheap vol before crisis extremely profitable

### 3. Vol Spread Trade (2019)


**Setup:**

- Short 1-month vol: strike = 12%
- Long 6-month vol: strike = 15%
- Bet on term structure normalization
- Vega: $\$50,000$ per leg

**Outcome:**

- 1M realized: 11% (+1% profit)
- 6M realized: 17% (+2% profit)
- **Net:** $(+1\%) + (+2\%) = +3\%$ × $\$50,000 = $\$150,000$

**Lesson:** Vol curve trades work in stable environments

### 4. Tail Hedge (COVID 2020)


**Setup:**

- Jan 2020: SPX at 3,300
- Bought 6-month vol swap as hedge
- Strike: 14%, Vega: $\$30,000$

**Outcome:**

- March crash: vol spiked to 60%+
- Realized vol over 6M = 42%
- **Payoff:** $\$30,000 \times (42\% - 14\%) = \$840,000$

**Lesson:** Vol swaps effective tail hedge, easy to explain to risk committee

---

## Practical Steps


### 1. Pre-Trade Analysis


**Evaluate before entering:**

1. **Current levels:**
   - Implied volatility (VIX percentile)
   - Historical realized volatility
   - Vol swap strike vs. variance strike

2. **View formation:**
   - Directional view on volatility
   - Expected magnitude
   - Time horizon

3. **Cost-benefit:**
   - Vol swap strike
   - vs. $\sqrt{\text{variance strike}}$
   - vs. ATM straddle
   - Convexity premium justified?

### 2. Instrument Selection


**Choose between alternatives:**

**Vol swap when:**

- Simplicity critical (explain to non-quants)
- Think naturally in vol terms
- Short-dated (< 3 months)
- Moderate moves expected

**Variance swap when:**

- Cost-sensitive
- Expect extreme moves (benefit from convexity)
- Long-dated (lower relative cost)
- Comfortable with variance math

**Straddle when:**

- Very short-dated
- Want optionality to exit
- Theta acceptable

### 3. Execution


**Best practices:**

- Get quotes from multiple dealers
- Compare to theoretical (variance + convexity)
- Check bid-ask spread (1-2% vol typical)
- Negotiate vega notional
- Confirm settlement methodology

**Typical pricing:**

- SPX vol swap: 0.5-1% vol above $\sqrt{K_{\text{var}}}$
- Single stock: 1-2% vol above
- Emerging markets: 2-4% vol above

### 4. Monitoring


**Daily tracking:**

- Realized volatility accrued
- Forward volatility (from options)
- MTM P&L
- Vol-of-vol indicators
- Days to settlement

**Tools:**

- Bloomberg: VOLS, VCURVE
- Realized vol calculators
- Custom spreadsheets

### 5. Exit Discipline


**Exit rules for long vol:**

- Take profit at 100% gain
- Stop loss at -50% (if view invalidated)
- Time stop: exit at 50% DTE if flat

**Exit rules for short vol:**

- Take profit at 50% gain
- **Hard stop at -50% loss**
- Exit if implied vol spikes >20%
- Exit if jump risk increases

### 6. Post-Trade Review


**Document for learning:**

- Entry/exit levels
- Realized vs. expected vol
- MTM path vs. final payoff
- What worked/didn't work
- Would variance swap have been better?

---

## Final Wisdom


> "Volatility swaps offer the most intuitive way to trade volatility - linear payoffs in the vol units you naturally think in. But this simplicity comes at a cost: the convexity adjustment makes vol swaps more expensive than variance swaps, sometimes significantly. For short-dated trades and directional vol views, this premium is worth paying for clarity and ease of communication. For tail hedging or long-dated positions, variance swaps are more economical. Master the vol-variance relationship, understand the convexity cost, and choose your instrument wisely."

**Key to success:**

- Understand convexity adjustment (vol swaps always more expensive)
- Compare costs across instruments before trading
- Use vol swaps for simplicity and intuition
- Use variance swaps for cost efficiency and extreme moves
- Monitor mark-to-market, but remember final settlement matters
- Size conservatively - volatility can explode
- Combine with complementary strategies for robust portfolio
