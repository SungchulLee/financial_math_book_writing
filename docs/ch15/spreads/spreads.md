# Options Spreads

**Options spreads** are multi-leg strategies that combine buying and selling options at different strikes or expirations, creating defined risk/reward profiles that are more capital-efficient than single options while offering strategic flexibility for any market view.








---

## The Core Insight

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/spreads_overview.png?raw=true" alt="spreads_overview" width="700">
</p>

**The fundamental idea:**

- Single options: Unlimited risk (short) or expensive (long)

- **Spreads: Defined risk AND defined reward** (the goldilocks solution)

- Combine buying and selling to offset costs

- More capital efficient than single legs

- Reduce exposure to Greeks (vega, gamma)

- Create custom risk/reward profiles for any market view

**The key classifications:**

$$
\text{By Strike: } \begin{cases}
\text{Vertical spreads} & \text{(same expiration, different strikes)} \\
\text{Horizontal spreads} & \text{(different expiration, same strike)} \\
\text{Diagonal spreads} & \text{(different expiration AND strikes)}
\end{cases}
$$

$$
\text{By Direction: } \begin{cases}
\text{Debit spreads} & \text{(pay to enter, limited risk)} \\
\text{Credit spreads} & \text{(collect to enter, limited risk)} \\
\end{cases}
$$

$$
\text{By Type: } \begin{cases}
\text{Call spreads} & \text{(both legs are calls)} \\
\text{Put spreads} & \text{(both legs are puts)} \\
\end{cases}
$$

**You're essentially saying: "I want exposure to a specific price range, time period, or volatility scenario, but I want to limit my risk and reduce my cost."**

---

## What Are Spreads?

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/vertical_spreads_comparison.png?raw=true" alt="vertical_spreads" width="700">
</p>

**Before trading spreads, understand the landscape:**

### 1. The Spread Universe

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/spread_types_matrix.png?raw=true" alt="spread_types" width="700">
</p>

**Spreads can be classified along three dimensions:**

1. **Strike dimension (spatial):**

   - Same strike → Horizontal (calendar)

   - Different strikes, same expiration → Vertical

   - Different strikes, different expiration → Diagonal

2. **Cash flow dimension:**

   - Pay premium → Debit spread

   - Collect premium → Credit spread

3. **Options type:**

   - Call spreads (both calls)

   - Put spreads (both puts)

**This creates a 3D matrix of spread types:**

| Spread Type | Strikes | Expiration | Cash Flow | Example |
|-------------|---------|------------|-----------|---------|
| Vertical debit call | Different | Same | Debit | Bull call spread |
| Vertical credit call | Different | Same | Credit | Bear call spread |
| Vertical debit put | Different | Same | Debit | Bear put spread |
| Vertical credit put | Different | Same | Credit | Bull put spread |
| Horizontal call | Same | Different | Debit | Call calendar |
| Horizontal put | Same | Different | Debit | Put calendar |
| Diagonal call | Different | Different | Debit/Credit | Diagonal call |
| Diagonal put | Different | Different | Debit/Credit | Diagonal put |

### 2. Vertical Spreads

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/spread_risk_profiles.png?raw=true" alt="spread_risk" width="700">
</p>

**Definition:** Buy and sell options at different strikes, same expiration.

**Four main types:**

### 3. Long Call Spread

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/spread_greeks_comparison.png?raw=true" alt="spread_greeks" width="700">
</p>

**Structure:**

- **Buy** lower strike call ($K_1$)

- **Sell** higher strike call ($K_2$)

- Same expiration

- **Pay debit** (cost to enter)

**Example:**

- Stock at $100

- Buy $100 call for $5

- Sell $105 call for $2

- **Net cost: $5 - $2 = $3 debit**

**Payoff at expiration:**

| Stock Price | Long $100 Call | Short $105 Call | Total P&L |
|-------------|----------------|-----------------|-----------|
| $95 | $0 | $0 | **-$3** (max loss) |
| $100 | $0 | $0 | **-$3** (max loss) |
| $103 | $3 | $0 | **$0** (breakeven) |
| $105 | $5 | $0 | **+$2** (max profit) |
| $110 | $10 | -$5 | **+$2** (max profit) |
| $115 | $15 | -$10 | **+$2** (max profit) |

**Characteristics:**

- **Max loss:** Debit paid ($3)

- **Max profit:** $(K_2 - K_1) - \text{debit} = $5 - $3 = $2$

- **Breakeven:** $K_1 + \text{debit} = $100 + $3 = $103$

- **Bias:** Bullish (profit from stock rising)

- **Delta:** Positive (around +0.25 to +0.50)

- **Theta:** Negative (time decay hurts)

- **Vega:** Positive near money (IV rise helps)

### 4. Short Call Spread

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/calendar_spread_dynamics.png?raw=true" alt="calendar_spreads" width="700">
</p>

**Structure:**

- **Sell** lower strike call ($K_1$)

- **Buy** higher strike call ($K_2$)

- Same expiration

- **Collect credit** (receive premium)

**Example:**

- Stock at $100

- Sell $105 call for $3

- Buy $110 call for $1

- **Net credit: $3 - $1 = $2 collected**

**Payoff at expiration:**

| Stock Price | Short $105 Call | Long $110 Call | Total P&L |
|-------------|-----------------|----------------|-----------|
| $95 | $0 | $0 | **+$2** (max profit) |
| $100 | $0 | $0 | **+$2** (max profit) |
| $105 | $0 | $0 | **+$2** (max profit) |
| $107 | -$2 | $0 | **$0** (breakeven) |
| $110 | -$5 | $0 | **-$3** (max loss) |
| $115 | -$10 | $5 | **-$3** (max loss) |

**Characteristics:**

- **Max profit:** Credit received ($2)

- **Max loss:** $(K_2 - K_1) - \text{credit} = $5 - $2 = $3$

- **Breakeven:** $K_1 + \text{credit} = $105 + $2 = $107$

- **Bias:** Bearish-neutral (profit from stock flat/down)

- **Delta:** Negative (around -0.25 to -0.40)

- **Theta:** Positive (time decay helps)

- **Vega:** Negative (IV drop helps)

### 5. Short Put Spread

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/diagonal_spread_flexibility.png?raw=true" alt="diagonal_spreads" width="700">
</p>

**Structure:**

- **Sell** higher strike put ($K_2$)

- **Buy** lower strike put ($K_1$)

- Same expiration

- **Collect credit** (receive premium)

**Example:**

- Stock at $100

- Sell $100 put for $4

- Buy $95 put for $1.50

- **Net credit: $4 - $1.50 = $2.50 collected**

**Payoff at expiration:**

| Stock Price | Short $100 Put | Long $95 Put | Total P&L |
|-------------|----------------|--------------|-----------|
| $110 | $0 | $0 | **+$2.50** (max profit) |
| $105 | $0 | $0 | **+$2.50** (max profit) |
| $100 | $0 | $0 | **+$2.50** (max profit) |
| $97.50 | -$2.50 | $0 | **$0** (breakeven) |
| $95 | -$5 | $0 | **-$2.50** (max loss) |
| $90 | -$10 | $5 | **-$2.50** (max loss) |

**Characteristics:**

- **Max profit:** Credit received ($2.50)

- **Max loss:** $(K_2 - K_1) - \text{credit} = $5 - $2.50 = $2.50$

- **Breakeven:** $K_2 - \text{credit} = $100 - $2.50 = $97.50$

- **Bias:** Bullish-neutral (profit from stock flat/up)

- **Delta:** Positive (around +0.25 to +0.40)

- **Theta:** Positive (time decay helps)

- **Vega:** Negative (IV drop helps)

### 6. Long Put Spread

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/vertical_spreads_payoff.png?raw=true" alt="vertical_spreads_payoff" width="700">
</p>

**Structure:**

- **Buy** higher strike put ($K_2$)

- **Sell** lower strike put ($K_1$)

- Same expiration

- **Pay debit** (cost to enter)

**Example:**

- Stock at $100

- Buy $100 put for $4

- Sell $95 put for $1.50

- **Net cost: $4 - $1.50 = $2.50 debit**

**Payoff at expiration:**

| Stock Price | Long $100 Put | Short $95 Put | Total P&L |
|-------------|---------------|---------------|-----------|
| $110 | $0 | $0 | **-$2.50** (max loss) |
| $105 | $0 | $0 | **-$2.50** (max loss) |
| $100 | $0 | $0 | **-$2.50** (max loss) |
| $97.50 | $2.50 | $0 | **$0** (breakeven) |
| $95 | $5 | $0 | **+$2.50** (max profit) |
| $90 | $10 | -$5 | **+$2.50** (max profit) |

**Characteristics:**

- **Max loss:** Debit paid ($2.50)

- **Max profit:** $(K_2 - K_1) - \text{debit} = $5 - $2.50 = $2.50$

- **Breakeven:** $K_2 - \text{debit} = $100 - $2.50 = $97.50$

- **Bias:** Bearish (profit from stock declining)

- **Delta:** Negative (around -0.25 to -0.50)

- **Theta:** Negative (time decay hurts)

- **Vega:** Positive near money (IV rise helps)

**Figure 1:** Payoff diagrams for all four vertical spreads showing defined risk/reward profiles: bull call (bullish debit), bear call (bearish credit), bull put (bullish credit), bear put (bearish debit).

### 7. Calendar Spreads

**Definition:** Buy and sell options at same strike, different expirations.

**Also called:** Time spreads, calendar spreads

### 8. Diagonal Spreads

**Definition:** Buy and sell options at different strikes AND different expirations.

**Structure:** Hybrid of vertical and horizontal spreads.

## Economic

**Beyond the basic definitions, understanding the ECONOMIC purpose of spreads:**

### 1. Cost Reduction

**Buying single option:**

- Buy $100 call for $5

- **Cost:** High (if far OTM, low probability)

- **Risk:** Lose entire premium if wrong

- **Issue:** Expensive for directional bet

**Solution: Vertical debit spread**

- Buy $100 call for $5, sell $105 call for $2

- **Cost:** $3 (40% cheaper!)

- **Risk:** Still limited to $3

- **Trade-off:** Cap upside at $105 (but upside > $105 is low probability anyway)

**Key insight:** Selling the OTM option funds most of your long option purchase.

### 2. Risk Limitation

**Selling single option:**

- Sell $100 call for $5

- **Premium:** Collect $5

- **Risk:** UNLIMITED (if stock rallies to $200, lose $95 per share!)

- **Margin:** High (broker requires large margin)

**Solution: Vertical credit spread**

- Sell $100 call for $5, buy $105 call for $2

- **Premium:** Collect $3 (less than naked, but...)

- **Risk:** LIMITED to $2 (max loss = spread width - credit)

- **Margin:** Low (only max loss required)

**Key insight:** Buying the further OTM option as "insurance" caps your risk.

### 3. Vega Control

**Long single option:**

- Buy $100 call for $5 (IV = 30%)

- Stock stays at $100, but IV drops to 20%

- **Result:** Option worth $3 (lost $2 from vega alone!)

**Solution: Spread reduces vega exposure**

- Buy $100 call, sell $105 call (net $3 debit)

- IV drops from 30% to 20%

- Long option: $5 → $3 (-$2)

- Short option: $2 → $1.20 (-$0.80)

- **Net:** -$2 + $0.80 = -$1.20 (40% less vega pain)

**Key insight:** Both legs lose from vega, but NET vega exposure is reduced.

### 4. Theta Capture

**Long single call:**

- Buy $105 call for $3 (stock at $100)

- 30 days pass, stock at $102

- **Result:** Option worth $1.50 (lost $1.50 from theta decay)

**Solution: Calendar spread monetizes time decay**

- Sell 30 DTE $100 call for $3

- Buy 60 DTE $100 call for $5

- After 30 days: Short expires worthless (+$3), long worth ~$4

- **Result:** Net +$2 profit from theta differential

**Key insight:** Near-term options decay faster than far-term → Capture this differential.

### 5. Spread Economics

**All spreads can be understood as:**

$$
\text{Spread} = \text{Long option (exposure)} + \text{Short option (financing/risk reduction)}
$$

**The short option serves two purposes:**

1. **Financing:** Reduces cost of long option (debit spreads)

2. **Risk management:** Caps risk of short option (credit spreads)

**The trade-off:** You give up unlimited profit (debit spreads) or unlimited premium collection (credit spreads) in exchange for defined risk and lower cost.

---

## Key Terminology

### 1. Spread Classifications

**Vertical spread:**

- Same expiration, different strikes

- "Vertical" because strikes are arranged vertically on option chain

- Most common spread type

- Includes: Bull call, bear call, bull put, bear put

**Horizontal spread:**

- Same strike, different expirations

- "Horizontal" because expirations are arranged horizontally

- Also called: Calendar spread, time spread

- Includes: Calendar calls, calendar puts

**Diagonal spread:**

- Different strikes AND different expirations

- Combines vertical and horizontal elements

- Most flexible, most complex

- Can be bullish, bearish, or neutral

### 2. Cash Flow Types

**Debit spread:**

- Pay premium to enter

- Net: Buy more expensive option, sell cheaper option

- Max loss: Premium paid

- Max profit: $(K_2 - K_1) - \text{premium paid}$

- Examples: Bull call spread, bear put spread

**Credit spread:**

- Collect premium to enter

- Net: Sell more expensive option, buy cheaper option

- Max profit: Premium collected

- Max loss: $(K_2 - K_1) - \text{premium collected}$

- Examples: Bear call spread, bull put spread

### 3. Directional Classifications

**Bullish spreads:**

- Profit from stock rising

- Positive delta

- Examples: Bull call spread, bull put spread

**Bearish spreads:**

- Profit from stock declining

- Negative delta

- Examples: Bear call spread, bear put spread

**Neutral spreads:**

- Profit from stock staying in range

- Near-zero delta (can be slightly positive or negative)

- Examples: Calendar spreads (at-the-money)

### 4. Spread Width & Strike Terms

**Width (spread width):**

- Distance between strikes: $K_2 - K_1$

- Narrow: $1-2 wide (less risk, less profit)

- Standard: $5 wide (balanced)

- Wide: $10+ wide (more risk, more profit potential)

**Strikes terminology:**

For vertical spreads:

- **Long strike:** The strike you buy

- **Short strike:** The strike you sell

- **Spread width:** Difference between strikes

For credit spreads (short spreads):

- **Short strike:** Usually closer to current price

- **Long strike:** Further OTM (protection)

For debit spreads (long spreads):

- **Long strike:** Usually closer to current price

- **Short strike:** Further OTM (financing)

### 5. Greek Terminology

**Net Greeks:**

All spreads have NET Greeks = sum of individual option Greeks.

$$
\Delta_{\text{spread}} = \Delta_{\text{long option}} + \Delta_{\text{short option}}
$$

**Greek reduction:**

Spreads REDUCE exposure to certain Greeks:

- **Vega reduction:** Long and short vega partially offset

- **Gamma reduction:** Long and short gamma partially offset

- **Theta:** Can be positive (credit spreads) or negative (debit spreads)

- **Delta:** Can be positive (bullish), negative (bearish), or near-zero (neutral)

---

## The Greeks in Detail

### 1. Delta (Δ)

**What delta tells you for spreads:**

$$
\Delta_{\text{spread}} = \Delta_{\text{leg 1}} + \Delta_{\text{leg 2}}
$$

**Vertical spread deltas:**

| Spread Type | Delta | Interpretation |
|-------------|-------|----------------|
| Bull call spread | +0.25 to +0.50 | Moderately bullish |
| Bear call spread | -0.25 to -0.40 | Moderately bearish |
| Bull put spread | +0.25 to +0.40 | Moderately bullish |
| Bear put spread | -0.25 to -0.50 | Moderately bearish |

**Example: Bull call spread**

- Long $100 call: Delta = +0.60

- Short $105 call: Delta = -0.30

- **Net spread delta:** +0.60 - 0.30 = +0.30

**Interpretation:** For every $1 stock rises, spread gains ~$0.30 in value.

**Calendar spread deltas:**

Near-zero delta if strike = current stock price:

- Short near-term: Delta ≈ -0.50

- Long far-term: Delta ≈ +0.50

- **Net:** ≈ 0 (neutral position)

**Key insight:** Vertical spreads have DIRECTIONAL exposure (delta), while ATM calendar spreads are NEUTRAL (near-zero delta).

### 2. Theta (Θ)

**What theta tells you for spreads:**

$$
\Theta_{\text{spread}} = \Theta_{\text{leg 1}} + \Theta_{\text{leg 2}}
$$

**Vertical spread theta:**

**Credit spreads (short spreads):**

- Short option theta: Positive (collecting decay)

- Long option theta: Negative (paying decay)

- **Net theta:** POSITIVE (short option closer to ATM, higher theta magnitude)

- **Earning:** ~$0.05-$0.15 per day

**Debit spreads (long spreads):**

- Long option theta: Negative (paying decay)

- Short option theta: Positive (collecting decay)

- **Net theta:** NEGATIVE (long option closer to ATM, higher theta magnitude)

- **Losing:** ~$0.05-$0.15 per day

**Example: Bear call spread (credit spread)**

- Short $105 call: Theta = +$0.12/day

- Long $110 call: Theta = -$0.05/day

- **Net theta:** +$0.07/day (earning money from time decay)

**Calendar spread theta:**

**POSITIVE theta (this is why you trade calendars!):**

- Short near-term: High theta (e.g., -$0.20/day on your side)

- Long far-term: Low theta (e.g., -$0.08/day against you)

- **Net theta:** +$0.12/day (earning from differential decay)

**Key insight:** 

- Credit spreads earn from theta (main profit driver)

- Debit spreads pay theta (must overcome this to profit)

- Calendar spreads earn from DIFFERENTIAL theta (near-term decays faster)

### 3. Vega (ν)

**What vega tells you for spreads:**

$$
\nu_{\text{spread}} = \nu_{\text{leg 1}} + \nu_{\text{leg 2}}
$$

**Vertical spread vega:**

**Credit spreads (short spreads):**

- Short option vega: Negative (lose if IV rises)

- Long option vega: Positive (gain if IV rises)

- **Net vega:** NEGATIVE (short option closer to ATM, higher vega magnitude)

- **Sensitivity:** -0.04 to -0.08 per 1% IV change

**Debit spreads (long spreads):**

- Long option vega: Positive (gain if IV rises)

- Short option vega: Negative (lose if IV rises)

- **Net vega:** POSITIVE (long option closer to ATM, higher vega magnitude)

- **Sensitivity:** +0.04 to +0.08 per 1% IV change

**Example: Bull call spread (debit spread)**

- Long $100 call: Vega = +0.12

- Short $105 call: Vega = -0.08

- **Net vega:** +0.04 (profit $4 if IV rises 1%)

**Calendar spread vega:**

**POSITIVE vega (significant):**

- Short near-term: Vega ≈ -0.10 (low vega due to short DTE)

- Long far-term: Vega ≈ +0.18 (high vega due to long DTE)

- **Net vega:** +0.08 (profit if IV rises)

**Key insight:**

- Credit spreads: SHORT vega (profit from IV drop)

- Debit spreads: LONG vega (profit from IV rise)

- Calendar spreads: LONG vega (profit from IV rise, especially if near expiration)

**Vega reduction vs. single options:**

**Single long call:**

- Vega = +0.15 (high exposure to IV)

**Bull call spread:**

- Net vega = +0.04 (73% reduction in vega exposure!)

**Benefit:** Less sensitive to IV changes, more controlled risk.

### 4. Gamma (Γ)

**What gamma tells you for spreads:**

$$
\Gamma_{\text{spread}} = \Gamma_{\text{leg 1}} + \Gamma_{\text{leg 2}}
$$

**Vertical spread gamma:**

**Credit spreads (short spreads):**

- Short option gamma: Negative (bad - losses accelerate)

- Long option gamma: Positive (good - limits acceleration)

- **Net gamma:** NEGATIVE but LIMITED (long option caps it)

- **Risk zone:** When stock near short strike

**Debit spreads (long spreads):**

- Long option gamma: Positive (good - gains accelerate)

- Short option gamma: Negative (bad - limits acceleration)

- **Net gamma:** POSITIVE but LIMITED (short option caps it)

- **Sweet spot:** When stock near long strike

**Example: Bear call spread (credit spread)**

- Short $105 call: Gamma = -0.05 (stock at $105 = danger!)

- Long $110 call: Gamma = +0.02 (protection kicks in)

- **Net gamma:** -0.03 (moderate gamma risk)

**Calendar spread gamma:**

**Complicated (changes with time):**

- Near expiration: Short near-term has HIGH gamma (risky if stock near strike)

- Far from expiration: Gamma is manageable

- **Management:** Exit calendar before near-term gets too close to expiration

**Key insight:**

- Gamma is the "acceleration" risk

- Spreads LIMIT gamma exposure vs. naked options

- Credit spreads have gamma RISK (losses accelerate near short strike)

- Debit spreads have gamma BENEFIT (gains accelerate near long strike)

### 5. Greek Comparison Table

**Summary of spread Greeks:**

| Spread Type | Delta | Theta | Vega | Gamma | Best Use |
|-------------|-------|-------|------|-------|----------|
| Bull call spread | +0.30 | -0.10 | +0.04 | +0.02 | Bullish, expect moderate rise |
| Bear call spread | -0.30 | +0.07 | -0.04 | -0.03 | Bearish, expect flat/down |
| Bull put spread | +0.30 | +0.07 | -0.04 | -0.03 | Bullish, expect flat/up |
| Bear put spread | -0.30 | -0.10 | +0.04 | +0.02 | Bearish, expect moderate decline |
| Calendar spread | ≈0 | +0.12 | +0.08 | Variable | Neutral, expect stability |
| Diagonal spread | Variable | Variable | Variable | Variable | Flexible, adjustable |

---


## Strike Selection Strategies

### 1. Vertical Spreads

**The strike selection determines everything:**

- Probability of profit

- Premium collected/paid

- Risk/reward ratio

- Delta exposure

**Framework: Three decisions**

1. **How far OTM for directional strike?**

2. **How wide should the spread be?**

3. **What DTE?**

### 2. Strike Distance

**For credit spreads (bear call, bull put):**

| Short Strike Distance | Delta | Win Prob | Premium | Use When |
|-----------------------|-------|----------|---------|----------|
| 10% OTM | 15 delta | ~75% | Low | Very confident, want safety |
| 5-7% OTM | 25-30 delta | ~65-70% | Moderate | Balanced approach |
| 3-5% OTM | 35-40 delta | ~60-65% | Good | Moderate confidence |
| 1-2% OTM | 45-50 delta | ~55-60% | High | Aggressive, high IV |

**For debit spreads (bull call, bear put):**

| Long Strike Distance | Delta | Win Prob | Cost | Use When |
|----------------------|-------|----------|------|----------|
| ATM | 50 delta | ~50% | High | Strong directional view |
| 1-2% OTM | 40-45 delta | ~45-50% | Moderate | Confident in direction |
| 3-5% OTM | 30-35 delta | ~40-45% | Lower | Less confident, cheaper |

**Key insight:**

- Credit spreads: Further OTM = higher win rate, lower premium

- Debit spreads: Closer to ATM = higher cost, better delta, need less movement

### 3. Spread Width

**Width determines risk/reward:**

$$
\text{Credit spread: } \begin{cases}
\text{Max profit} = \text{Credit} \\
\text{Max loss} = \text{Width} - \text{Credit}
\end{cases}
$$

$$
\text{Debit spread: } \begin{cases}
\text{Max profit} = \text{Width} - \text{Debit} \\
\text{Max loss} = \text{Debit}
\end{cases}
$$

**Width options:**

| Width | Risk/Reward | Capital | Liquidity | Use When |
|-------|-------------|---------|-----------|----------|
| $1-2 | Balanced | Low | May be thin | Small account |
| $5 | Standard | Moderate | Best | Most situations |
| $10 | More risk | Higher | Good | Need room to move |
| $15+ | High risk | High | May be thin | Avoid (usually) |

**Example comparison:**

**Bear call spread on stock at $100:**

| Width | Short/Long Strikes | Credit | Max Loss | R/R | ROC |
|-------|-------------------|--------|----------|-----|-----|
| $2 | $105/$107 | $0.80 | $1.20 | 1.5:1 | 67% |
| $5 | $105/$110 | $2.00 | $3.00 | 1.5:1 | 67% |
| $10 | $105/$115 | $3.00 | $7.00 | 2.3:1 | 43% |

**Key insight:** ROC is similar, but $5 wide is the liquidity sweet spot.

### 4. Expiration

**DTE affects premium and theta:**

| DTE | Theta/Day | Premium | Use For |
|-----|-----------|---------|---------|
| 7-14 | High | Low | Very short-term credit spreads (risky) |
| 21-30 | Good | Moderate | Standard credit spreads |
| 45-60 | Moderate | Higher | Debit spreads, calendars |
| 60-90 | Lower | High | Long-term positions, diagonals |

**Credit spreads optimal DTE: 30-45 days**

- Theta strong but not explosive

- Gamma risk manageable

- Good premium collection

**Debit spreads optimal DTE: 45-60 days**

- Give position time to work

- Theta not too harsh yet

- Can ride for 30-45 days

**Calendar spreads:**

- Sell: 21-30 DTE (near-term)

- Buy: 60-90 DTE (far-term)

- Ratio: Typically 2:1 or 3:1 time ratio

### 5. Volatility Skew

**Volatility skew impacts strike selection:**

**Put skew (equity markets):**

- OTM puts: Higher IV than ATM

- ATM: Middle IV

- OTM calls: Lower IV than ATM

**Impact on spreads:**

**Bull put spread (sell high IV put, buy lower IV put):**

- **Favorable skew** (selling expensive, buying cheap)

- Can collect better premium

**Bear call spread (sell low IV call, buy even lower IV call):**

- **Less favorable skew** (selling cheap, buying cheaper)

- Collect less premium

**Strategy:** 

- Prefer bull put spreads over bull call spreads (better skew)

- Bear call spreads still viable but less skew advantage

---

## Risk Management

### 1. Principles

**Universal rule: Manage risk at trade and portfolio level.**

### 2. Trade Risk

**Maximum risk per trade:**

$$
\text{Max risk per trade} = \begin{cases}
1\% \text{ of account} & \text{if learning} \\
2\% \text{ of account} & \text{if experienced} \\
3-5\% \text{ of account} & \text{if very experienced (rare)}
\end{cases}
$$

**Position sizing calculation:**

$$
\text{Number of spreads} = \frac{\text{Account size} \times \text{Risk \%}}{\text{Max loss per spread}}
$$

**Example:**

- Account: $50,000

- Risk tolerance: 2%

- Max risk: $50,000 × 0.02 = $1,000

- Bear call spread max loss: $300 per spread

- **Position size:** $1,000 / $300 = 3.33 → **3 spreads**

### 3. Spread Risk

**Credit spreads:**

- Max loss = (Width - Credit) × 100

- Example: $5 wide, $2 credit → Max loss = $300

- Easy to calculate

**Debit spreads:**

- Max loss = Debit paid × 100

- Example: $3 debit → Max loss = $300

- Also easy

**Calendar spreads:**

- Max loss = Premium paid (if stock moves far away)

- But typically manage before max loss

- **Sizing:** Use premium paid as "max loss" for conservative sizing

**Diagonal spreads:**

- More complex (can adjust)

- **Sizing:** Use initial debit as approximate max risk

### 4. Portfolio Risk

**Maximum total risk:**

$$
\text{Total risk across all positions} \leq 20\% \text{ of account}
$$

**Diversification rules:**

**By underlying:**

- Don't put all spreads on same stock

- Max 5% of account on any single underlying

- **Example:** With $50k account, max $2,500 risk on SPY trades

**By expiration:**

- Don't have all positions expire same week

- Stagger expirations (some 30 DTE, some 45 DTE, some 60 DTE)

- **Reason:** Avoid "expiration week disaster" (all positions stressed simultaneously)

**By sector:**

- Don't have all tech call spreads

- Diversify: Some SPY, some individual stocks, different sectors

- **Reason:** Sector rotation can kill correlated positions

**Example portfolio ($50k account):**

| Position | Underlying | Type | Contracts | Max Loss | % Account |
|----------|-----------|------|-----------|----------|-----------|
| Bear call spread | SPY | Credit | 4 | $1,200 | 2.4% |
| Bull put spread | AAPL | Credit | 3 | $900 | 1.8% |
| Bull call spread | XLE | Debit | 5 | $1,000 | 2.0% |
| Calendar spread | QQQ | Debit | 2 | $600 | 1.2% |
| **Total** | | | | **$3,700** | **7.4%** |

**Portfolio Greeks:**

- Net delta: +500 (mildly bullish)

- Net theta: +$35/day (positive time decay)

- Net vega: -$80 (short volatility)

### 5. Stops

**Credit spreads (bear call, bull put):**

**Stop loss triggers:**

1. **Stock through short strike:** Close immediately

2. **Loss reaches 50% of max risk:** Close position

3. **Time-based:** If not profitable by 50% of DTE, close

**Example:**

- Bear call spread: $105/$110, collected $2

- Max loss: $3

- **Stop loss:** Close if loss reaches $1.50 OR stock > $105

**Debit spreads (bull call, bear put):**

**Stop loss triggers:**

1. **Loss reaches 50% of premium paid:** Close position

2. **Time-based:** If not up by 50% of DTE, consider closing

3. **Thesis invalidated:** If directional view wrong, close

**Example:**

- Bull call spread: $100/$105, paid $3

- Max loss: $3

- **Stop loss:** Close if loss reaches $1.50 OR if bearish signal emerges

**Calendar spreads:**

**Stop loss triggers:**

1. **Stock moves >5% away from strike:** Close position

2. **Loss reaches 50% of premium paid:** Close

3. **Near-term within 7 DTE:** Close to avoid gamma risk

**Example:**

- Calendar spread at $100 strike, paid $2

- Stock at $100

- **Stop loss:** Close if stock moves to $95 or $105 OR loss > $1

### 6. Exits

**Universal profit target: 50% of max profit**

**Why 50%?**

**Mathematical expectation:**

| Strategy | Hold to 100% | Close at 50% |
|----------|--------------|--------------|
| Win rate | 65% | 75% |
| Avg win | $200 | $100 |
| Avg loss | -$300 | -$100 |
| Expected value | $65 - $105 = -$40 | $75 - $25 = +$50 |

**Key insight:** Taking 50% profit increases win rate AND improves expected value.

**Spread-specific targets:**

**Credit spreads:**

- Target: 50% of credit collected

- Example: Collected $2, close at $1

- **Or:** 21 DTE, whichever comes first

**Debit spreads:**

- Target: 50% of max profit potential

- Example: Max profit $2, close when up $1

- **Or:** Stock reaches midpoint between strikes

**Calendar spreads:**

- Target: 30-50% of max profit (harder to calculate)

- **Rule of thumb:** If up 30%+, close by 14 DTE

### 7. Adjustments

**When to adjust vs. close:**

**Adjust if:**

- Thesis still valid

- Early in trade (<50% time elapsed)

- Adjustment cost reasonable (<30% of max risk)

**Close if:**

- Thesis invalidated

- Late in trade (>50% time elapsed)

- Adjustment too expensive

**Vertical spread adjustments:**

**Roll out (extend time):**

- Close current position

- Open same strikes, later expiration

- **Cost:** Additional premium (usually debit)

- **When:** Need more time, thesis intact

**Roll up/down (change strikes):**

- Close current position

- Open new strikes in favorable direction

- **Cost:** May be credit or debit depending on direction

- **When:** Stock moved, need to reset

**Example adjustment:**

**Bear call spread in trouble:**

- Original: Short $105/$110 call spread

- Stock rallied to $104 (approaching short strike)

- **Adjustment:** Roll to $110/$115 call spread

- **Effect:** Reset higher, give more room

**Calendar spread adjustments:**

**Roll short leg:**

- Near-term expires or getting close

- **Action:** Sell new near-term at same strike

- **Effect:** Collect more premium, extend trade

- **Can repeat:** Multiple times (this is the power of calendars!)

**Example:**

- Month 1: Sell 30 DTE $100 call

- Month 1 end: Cover for profit, sell new 30 DTE $100 call

- Month 2 end: Repeat

- **Result:** Multiple premium collections on single long call

---



## Practical Guidance

**Step-by-step implementation framework for spread trading:**

### 1. Market Context

**Before entering any spread, evaluate:**

1. **Market environment:**

   - Overall trend (bull, bear, sideways)

   - Volatility level (VIX, IV rank)

   - Market cycle phase

   - Economic backdrop

2. **Stock-specific factors:**

   - Price trend and momentum

   - Support/resistance levels

   - Upcoming catalysts (earnings, FDA, product launch)

   - Volume and liquidity (>5,000 daily option volume)

3. **Volatility assessment:**

   - IV rank or percentile (IVR)

   - Historical vs. implied volatility

   - IV skew across strikes

   - Approaching or past earnings

### 2. Strategy Choice

**Choose vertical debit spreads when:**

- Strong directional conviction (bull call or bear put)

- IV rank < 40% (options cheap)

- Expect significant move (>5% in 30-60 days)

- Want limited capital at risk

- Clear catalyst within timeframe

**Choose vertical credit spreads when:**

- Mild directional or neutral view

- IV rank > 50% (options expensive)

- Expect stock to stay in range or move slightly

- Want theta to work for you

- High probability of profit preferred

**Choose calendar spreads when:**

- Neutral to slightly directional

- IV rank < 50% and expecting expansion

- Time horizon 30-60 days

- Can actively manage position

- Expect low short-term movement, volatility later

**Choose diagonal spreads when:**

- Mildly directional (bullish or bearish)

- Want calendar spread benefits with directional bias

- Flexible time horizon

- Can roll and manage actively

**Avoid spreads when:**

- Earnings in next 3-7 days (unless specifically trading earnings)

- Extremely illiquid options (OI < 500)

- No clear thesis or catalyst

- Too many correlated positions already

### 3. Risk Sizing

**Calculate maximum position size:**

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times \text{Risk\%}}{\text{Max Loss Per Spread}}
$$

**Conservative guidelines:**

- Risk 1-2% per trade when learning

- Risk 2-5% per trade with experience

- Never more than 20% total portfolio in options

- Spread risk across 5-10 positions minimum

**Example:**

- $50,000 portfolio

- 2% risk = $1,000

- Bull call spread max loss: $250/contract

- **Max size: 4 contracts**

### 4. Spread Design

**For vertical debit spreads:**

- **Strike width:** 

  - Narrow ($2-3 wide): Lower cost, lower profit, needs smaller move

  - Medium ($5 wide): Balanced risk/reward

  - Wide ($7-10 wide): Higher cost, higher profit, needs larger move

- **Time:** 45-90 DTE for enough time to work

- **Long strike:** ATM or slightly ITM (delta 0.60-0.70)

- **Short strike:** OTM (delta 0.30-0.40)

**For vertical credit spreads:**

- **Strike width:** $5-10 wide (optimize reward/risk)

- **Time:** 30-45 DTE (theta sweet spot)

- **Short strike:** Delta 0.15-0.30 (high probability OTM)

- **Long strike:** 1-2 strikes further OTM (protection)

**For calendar spreads:**

- **Time spread:** 

  - Short leg: 30-45 DTE (front month)

  - Long leg: 60-90 DTE (back month)

  - Minimum 30-day gap

- **Strike:** ATM or slightly OTM in direction of bias

### 5. Execution

**Best practices:**

1. **Order type:** Always enter as single spread order

   - Use "vertical spread" or "calendar spread" order type

   - NEVER leg in (enter one leg at a time)

2. **Pricing:**

   - Start with mid-price limit order

   - Adjust by $0.05 increments if not filled within 5 minutes

   - Check bid-ask spread < 10% of mid-price

   - Be patient - let order work

3. **Timing:**

   - Avoid first 30 minutes (market opening volatility)

   - Avoid last 30 minutes (closing imbalances)

   - Best: 10am-3pm EST

4. **Liquidity check:**

   - Open interest > 500 per strike minimum

   - Daily option volume > 5,000

   - Bid-ask spread tight (<10% of mid)

### 6. Management

**Active management rules:**

**For credit spreads:**

- **Profit target:** Close at 50% of max profit (non-negotiable)

- **Time exit:** Exit at 21 DTE regardless of P&L

- **Stop loss:** Exit if loss = 2x credit received

- **Tested side:** Exit if stock breaches short strike

**For debit spreads:**

- **Profit target:** Close at 50-100% of max profit

- **Time exit:** Exit at 14-21 DTE if not profitable

- **Stop loss:** Exit at -50% of debit paid

- **Trend break:** Exit if stock breaks key support/resistance

**For calendar spreads:**

- **Profit target:** Close when front month has minimal value (<$0.20)

- **IV change:** Exit if IV drops significantly (vega risk)

- **Roll opportunity:** Consider rolling front month out

- **Direction change:** Exit if stock moves far from strike

### 7. Adjustments

**When to adjust:**

- Stock approaching short strike (tested)

- Position down 30-40% but thesis still valid

- Time remaining but direction needs correction

- Volatility shift changes landscape

**How to adjust:**

**Vertical roll (tested side):**

- Close current spread

- Open new spread further OTM

- Collect additional credit (for credit spreads)

- Extend DTE if needed

**Time roll:**

- Keep strikes, extend expiration

- Roll entire spread to next month

- Add premium or small debit

- Gives more time for thesis

**Close untested side:**

- If one side threatened

- Close profitable side

- Reduce exposure

- Lock in partial profit

**When to take loss instead:**

- Already adjusted once (don't keep hoping)

- Thesis invalidated (catalyst failed)

- Cost to adjust > potential profit

- Better opportunity elsewhere

### 8. Review

**Track every trade:**

- Entry date, strikes, expiration, cost/credit

- Rationale: Why this spread? What's the thesis?

- Market conditions: IV rank, trend, technical setup

- Exit date and P&L

- What worked and what didn't

- Mistakes made and lessons learned

**Maintain statistics:**

- Win rate by spread type

- Average ROC (return on capital)

- Average time held

- Best performing setups

- Losing trade patterns

## Common Mistakes 

### 1. No Exit Plan

**The mistake:**

- Expect rally, sell bull put spread (instead of buying bull call spread)

- **Problem:** Limited upside if big move happens

**Example:**

- Stock at $100, expect rally to $120

- Trade: Bull put spread $95/$90 (collect $2)

- Stock rallies to $120: Keep $2 (made only $200)

- **Better:** Bull call spread $100/$110 (pay $4, make $6 = $600)

**How to avoid:**

- **Debit spreads for directional moves** (bull call, bear put)

- **Credit spreads for neutral/income** (bear call, bull put)

- Match strategy to conviction level

### 2. No Rules

**The mistake:**

- Plan to do bull call spread

- Buy $100 call for $5

- Wait to sell $105 call

- Market moves, now $105 call only $1.80 (was $2)

- **Lost $0.20 by not entering as spread**

**Why it's wrong:**

- Market can move against you between legs

- Bid-ask slippage on both legs separately

- Not guaranteed to get desired credit/debit

**How to avoid:**

- **Always enter spreads as single order** (use "vertical spread" order type)

- Set limit price for the SPREAD (not individual legs)

- Let market make both sides simultaneously

### 3. Undefined Risk

**The mistake:**

- Plan credit spread with $2 mid-price

- Bid/ask: $1.80/$2.20

- Enter market order, get filled at $1.80

- **Lost $0.20 immediately** (10% of trade!)

**How to avoid:**

- **Always use limit orders**

- Start at mid-price, adjust by $0.05 if not filled

- Check bid-ask width before entering:

  - < 5% of mid: Good

  - 5-10% of mid: Acceptable

  - >10% of mid: Avoid (illiquid)

### 4. Emotional Trading

**The mistake:**

- Risk 10% of account on one spread

- Spread goes to max loss

- Account down 10% in one trade

- **Psychological damage** leads to revenge trading

**How to avoid:**

- **Strict rule:** Never risk more than 2-5% per trade (1% if learning)

- Calculate max loss BEFORE entering

- Track total portfolio risk (< 20% across all positions)

### 5. Reactive Decisions

**The mistake:**

- Credit spread at 60% of max profit

- "I'll hold for 100%"

- Stock reverses, profit turns to loss

**Why it's wrong:**

- Last 40% of profit takes 70%+ of time

- Last 40% has most gamma risk

- Often not worth the risk

**How to avoid:**

- **Rule:** Close at 50% of max profit

- For credit spreads: If collected $2, close at $1

- For debit spreads: If max profit $5, close at $2.50

- **Exception:** Calendar spreads may hold longer (but manage actively)

### 6. No Stop Loss

**The mistake:**

- Have credit spread, earnings in 3 days

- "Stock probably won't move much"

- Stock gaps 10% on earnings, blow through your strikes

- **Max loss instantly**

**Why it's wrong:**

- Earnings are binary events (stock gaps)

- IV crush can help or hurt (unpredictable)

- Not worth the risk

**How to avoid:**

- **Exit ALL spreads 2-3 days before earnings**

- If want to trade earnings: Use strategies designed for earnings (iron condor, butterfly)

- Check earnings calendar before entering

### 7. No Time Stop

**The mistake:**

- Stock in strong uptrend (+30% in 3 months)

- "Must pull back soon"

- Sell bear call spreads repeatedly

- **Lose on every one as trend continues**

**Why it's wrong:**

- Trends last longer than expected

- "The trend is your friend"

- Low probability bet

**How to avoid:**

- **Check trend FIRST** before entering spread

- If clear uptrend: Don't sell call spreads (use put spreads instead)

- If clear downtrend: Don't sell put spreads (use call spreads instead)

- **Trade WITH trend, not against it**

### 8. Trading on Hope

**The mistake:**

- VIX at 10 (very low), sell credit spreads

- Collect $1 credit on $5 wide spread

- VIX spikes to 25 next week

- Position loses $2 from vega alone (lost 2× the credit!)

**How to avoid:**

- **Check VIX percentile** before trading

- VIX < 40th percentile: Avoid credit spreads (prefer debit spreads or calendars)

- VIX > 60th percentile: Ideal for credit spreads

- **Use IV rank/percentile** for individual stocks too

### 9. Late Exits

**The mistake:**

- Trade spreads on small-cap stock

- Open interest: 50 per strike

- Enter at "fair price," get filled

- Try to exit: Bid-ask is $0.50 wide on $2 spread

- **Lose 25% to slippage on exit**

**How to avoid:**

- **Only trade liquid underlyings:**

  - SPY, QQQ, IWM (index ETFs) ✓

  - AAPL, MSFT, TSLA (large-cap stocks) ✓

  - Avoid small-cap stocks ✗

- **Check open interest:** Need >1,000 per strike

- **Check volume:** Need >5,000 daily volume

### 10. Unplanned Trades

**The mistake:**

- Enter spread

- "I'll figure out exit later"

- Position underwater, panic, make emotional decision

- **Exit at worst possible time**

**How to avoid:**

- **BEFORE entering, write down:**

  - Profit target (usually 50% of max profit)

  - Stop loss (usually 50% of max risk or thesis invalidation)

  - Time stop (usually 21 DTE for 45 DTE entries)

- Follow the rules, don't improvise

- **No emotions, just execution**

---


## Psychological Aspects

### 1. Patience for Spreads

**The mental game:**

**Credit spreads:**

- Collect $2 premium

- Day 1-10: Position barely moves (only +$0.20)

- **Feeling:** "This is too slow"

- **Reality:** Theta accelerates, be patient

**Solution:**

- Understand theta curve (slow early, fast late)

- Don't check position daily (check every 3-5 days)

- Trust the process (if stock cooperates, theta will work)

**Debit spreads:**

- Pay $3 for spread, max profit $2

- Stock needs to MOVE to make money

- Day 1-20: Stock flat, losing to theta

- **Feeling:** "This trade is going nowhere"

- **Reality:** Directional trades need time

**Solution:**

- Accept that directional trades are more binary

- Cut losses quickly if stock doesn't move as expected (don't hold and hope)

- Be selective (only trade with strong conviction)

### 2. Managing Expectations

**Realistic returns:**

**Credit spreads (bear call, bull put):**

- Win rate: 65-70%

- Average ROC per win: 30-50% (in 20-30 days)

- Average loss per loss: 50-100% of risk

- **Net expectation:** ~20-30% ROC over many trades

**Debit spreads (bull call, bear put):**

- Win rate: 50-60%

- Average ROC per win: 50-100% (if move happens)

- Average loss per loss: 50-100% of premium

- **Net expectation:** ~20-40% ROC (but more volatile)

**Calendar spreads:**

- Win rate: 60-70% (if managed well)

- Average ROC: 30-60% (if rolled properly)

- More work (active management)

- **Net expectation:** ~30-50% ROC

**Annual returns:**

- Conservative (2% risk/trade, high win rate): 20-40% annual

- Moderate (3% risk/trade, balanced): 40-80% annual

- Aggressive (5% risk/trade, selective): 80-150% annual (with higher volatility)

**Key reality check:**

- These are NOT get-rich-quick

- Require consistency over 50-100 trades

- One bad trade can set you back 5 good trades

- **Success = risk management + patience + discipline**

### 3. Handling Losing Streaks

**With 65% win rate, expect 3-4 losses in a row occasionally:**

**After 3 losses:**

- Total: ~6% account drawdown (with 2% risk/trade)

- **Feeling:** "This strategy doesn't work"

- **Reality:** This is NORMAL variance

**How to handle:**

1. **Review each loss:** Was it process error or bad luck?

2. **If process error:** Fix the process

3. **If bad luck:** Keep trading (edge will show over time)

4. **Don't change strategy** after 3 losses (need 50+ trades to evaluate)

**After 5+ losses:**

- **Rare but possible** (2% probability with 65% win rate)

- **Action:** Take 1-2 week break, deeply review strategy

- **Consider:** Is market environment changed? Adjust if needed

### 4. The 50% Profit Rule

**Hardest part: Taking profit at 50%**

**Scenario:**

- Credit spread at 50% profit (up $1 on $2 credit)

- "Just 10 more days to expiration, I can get full $2"

- **Temptation is strong**

**Why you must close:**

- Last $1 is 10 more days = $0.10/day

- But gamma risk increases exponentially

- One bad day can erase weeks of theta

- **Math:** 50% rule INCREASES expected value (shown earlier)

**How to build discipline:**

1. **Automate:** Set GTC order to close at 50% profit

2. **Track results:** Keep spreadsheet showing 50% rule performance

3. **Accept:** You're giving up some profit for much less risk

4. **Remember:** Compounding many 50% wins > occasional 100% wins with losses

---

## Trade Execution Checklist

### 1. Pre-Trade Analysis

**Step 1: Market view**

- [ ] Direction: Bullish, bearish, or neutral?

- [ ] Conviction: Strong, moderate, or weak?

- [ ] Timeframe: Days, weeks, or months?

- [ ] Catalyst: What will move the stock?

**Step 2: Strategy selection**

- [ ] Spread type chosen: ______

- [ ] Reasoning: Why this spread for this view?

- [ ] Alternative considered: ______

**Step 3: Underlying selection**

- [ ] Ticker: ______

- [ ] Current price: ______

- [ ] Liquidity check:

  - [ ] Daily volume > 1M shares (stock) or 100K (ETF)?

  - [ ] Option volume > 10,000 contracts/day?

  - [ ] Open interest > 1,000 per strike?

**Step 4: Volatility check**

- [ ] Current VIX: ______ (Percentile: ______)

- [ ] Stock IV rank: ______ (Percentile: ______)

- [ ] Assessment:

  - [ ] High IV → Favor credit spreads

  - [ ] Low IV → Favor debit spreads or calendars

  - [ ] Moderate IV → Either works

**Step 5: Technical setup**

- [ ] Support levels: ______

- [ ] Resistance levels: ______

- [ ] Trend: Uptrend / Downtrend / Sideways

- [ ] Indicators: RSI ______, Moving averages ______

**Step 6: Events calendar**

- [ ] Earnings date: ______ (Plan exit before if within DTE)

- [ ] Ex-dividend date: ______

- [ ] Major events: Fed, economic data, etc.

### 2. Trade Structure

**Step 7: Strike selection**

- [ ] Long strike (if applicable): ______ (Delta: ______)

- [ ] Short strike: ______ (Delta: ______)

- [ ] Spread width: ______

- [ ] Reasoning for strikes: ______

**Step 8: Expiration selection**

- [ ] DTE for near-term (if applicable): ______

- [ ] DTE for far-term (if applicable): ______

- [ ] Expiration date: ______

**Step 9: Pricing**

- [ ] Long leg: Bid ______ / Ask ______

- [ ] Short leg: Bid ______ / Ask ______

- [ ] Spread mid-price: ______

- [ ] Bid-ask width: ______ (< 5% of mid?)

**Step 10: Risk/reward calculation**

- [ ] Debit paid or credit collected: ______

- [ ] Max profit: ______

- [ ] Max loss: ______

- [ ] Risk/reward ratio: ______

- [ ] Breakeven: ______

- [ ] Probability of profit (estimate): ______%

### 3. Position Sizing

**Step 11: Account risk**

- [ ] Account size: $______

- [ ] Risk per trade: ______% = $______

- [ ] Max loss per spread: $______

- [ ] Number of contracts: ______

- [ ] Total capital at risk: $______

- [ ] % of account: ______%

**Step 12: Portfolio check**

- [ ] Current positions: ______ (list)

- [ ] Total portfolio risk: ______% (< 20%?)

- [ ] Correlation check: Diversified by underlying, expiration, sector?

### 4. Exit Rules

**Step 13: Profit target**

- [ ] Profit target: ______ (typically 50% of max profit)

- [ ] Target price to close spread: ______

- [ ] Or: Days until profit target evaluation: ______

**Step 14: Stop loss**

- [ ] Stop loss condition 1: Stock crosses ______ (short strike)

- [ ] Stop loss condition 2: Loss reaches ______ (typically 50% of max)

- [ ] Stop loss condition 3: Thesis invalidated (describe): ______

**Step 15: Time stop**

- [ ] Exit by DTE: ______ (typically 21 DTE for credit spreads, 14 DTE for debit spreads)

- [ ] Calendar date: ______

**Step 16: Adjustment trigger**

- [ ] Adjustment condition: If stock reaches ______ by ______ DTE

- [ ] Planned adjustment: ______ (roll up/down/out, or close)

- [ ] Max adjustment cost: ______ (typically 30% of original risk)

### 5. Trade Entry

**Step 17: Order entry**

- [ ] Order type: Vertical spread / Calendar / Diagonal

- [ ] Buy/Sell: Specify exact order (example: "Sell 5 SPY Feb 450/455 call spreads")

- [ ] Limit price: ______ (start at mid-price)

- [ ] Number of contracts: ______

- [ ] Time in force: Day / GTC

**Step 18: Pre-submission check**

- [ ] Correct strikes? ______

- [ ] Correct expiration(s)? ______

- [ ] Correct number of contracts? ______

- [ ] Correct direction (buy or sell spread)? ______

- [ ] Is this a credit or debit? ______ (matches expectation?)

**Step 19: Order placement**

- [ ] Order submitted at: ______ (time)

- [ ] Fill status: Pending / Filled / Adjusted

**Step 20: Fill confirmation**

- [ ] Filled at: ______ (price)

- [ ] Total credit/debit: $______

- [ ] Actual max profit: $______

- [ ] Actual max loss: $______

- [ ] Commission/fees: $______

### 6. Trade Management

**Daily check (2-3 minutes):**

- [ ] Current stock price: ______

- [ ] Current position P&L: $______

- [ ] Days to expiration: ______

- [ ] Any news/events: ______

- [ ] Action needed: Yes / No

**Weekly review (10-15 minutes):**

- [ ] Time elapsed: ______% of original DTE

- [ ] Profit/loss: ______% of max profit

- [ ] Assessment: On track / Concerning / Need action

- [ ] Check exit triggers:

  - [ ] Profit target hit?

  - [ ] Stop loss triggered?

  - [ ] Time stop reached?

  - [ ] Adjustment needed?

### 7. Trade Exit

**Step 21: Exit decision**

- [ ] Exit trigger: ______ (profit target / stop loss / time / adjustment)

- [ ] Exit planned for: ______ (date/time)

- [ ] Exit price target: ______

**Step 22: Exit order**

- [ ] Order type: Buy/Sell spread to close

- [ ] Limit price: ______ (aim for mid-price)

- [ ] Time of order: ______

**Step 23: Exit confirmation**

- [ ] Filled at: ______

- [ ] Exit cost/credit: $______

- [ ] Final P&L: $______

- [ ] ROC: ______%

- [ ] Days held: ______

- [ ] Annualized ROC: ______%

### 8. Post-Trade Review

**Step 24: Trade analysis**

- [ ] Win or loss: ______

- [ ] Why: ______

- [ ] Did I follow entry rules? Yes / No (explain)

- [ ] Did I follow exit rules? Yes / No (explain)

- [ ] What worked well: ______

- [ ] What could improve: ______

- [ ] Was position sizing appropriate? Yes / No

- [ ] Lessons learned: ______

**Step 25: Record keeping**

- [ ] Trade recorded in journal/spreadsheet

- [ ] Screenshots saved (entry, exit, chart)

- [ ] Updated running stats (win rate, avg ROC, etc.)

---

## Final Thoughts

Spreads are not magic. They are:

- **Tools** for implementing your market view with defined risk

- **Strategies** that profit from directional moves, time decay, or volatility changes

- **Frameworks** for consistent, repeatable trading

**Success comes from:**

- Understanding WHY each spread profits (Greeks, market dynamics)

- Selecting the RIGHT spread for your view (don't force it)

- Managing risk RUTHLESSLY (small losses, let winners run to 50%)

- Being PATIENT (theta and edge take time to show)

- Staying DISCIPLINED (follow rules, ignore emotions)

**If you do these things consistently over 100+ trades, spreads can become a reliable income strategy.**

**Remember:**

- No strategy wins 100% of time

- Losses are part of the game (embrace them)

- Edge shows over 50-100 trades (not 5)

- Risk management is everything

- **Discipline separates winners from losers**

**Good luck, and may the Greeks be ever in your favor!**

---

*This guide is for educational purposes only and does not constitute financial advice. Options trading involves risk of loss and is not suitable for all investors. Options spreads can result in the loss of the entire investment. Always consult with a qualified financial professional before making investment decisions.*