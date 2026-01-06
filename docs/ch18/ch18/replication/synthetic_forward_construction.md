# Synthetic Forward Construction

**Synthetic forward construction** is an options-based strategy that replicates the payoff of a forward contract by combining long calls and short puts (or vice versa) at the same strike, creating equivalent directional exposure without using actual futures while exploiting pricing inefficiencies, managing margin, or accessing markets unavailable through futures.

---

## The Core Insight

**The fundamental idea:**

- Forwards and futures have linear payoff profiles
- Options can replicate this linearity perfectly
- Put-call parity creates mathematical equivalence
- Long call + Short put = Synthetic long forward
- Short call + Long put = Synthetic short forward
- Arbitrage enforces pricing relationship
- Can exploit basis inefficiencies
- Manage capital more efficiently
- Access restricted or illiquid forwards

**The key equations:**

$$
\text{Synthetic Long} = \text{Long Call} + \text{Short Put} \quad (\text{same strike } K)
$$

$$
\text{Put-Call Parity: } C - P = S - K e^{-rT}
$$

$$
\text{Synthetic Payoff} = S_T - K \quad \text{(identical to forward)}
$$

**You're essentially betting: "I can create forward exposure synthetically using options that is mathematically equivalent to actual futures, potentially at better pricing, with superior margin efficiency, or with tactical advantages unavailable through the futures market."**

---

## What Are Synthetic Forwards?

**Before constructing synthetics, understand the fundamental mechanics:**

### 1. Put-Call Parity Foundation

**The cornerstone relationship:**

$$
C(K,T) - P(K,T) = S_0 - K e^{-rT}
$$

Where:
- $C$ = Call option price
- $P$ = Put option price
- $K$ = Strike price (same for both)
- $T$ = Time to expiration (same for both)
- $S_0$ = Current spot price
- $r$ = Risk-free rate

**Rearranging:**

$$
S_0 = C - P + K e^{-rT}
$$

**Or for futures:**

$$
C - P = F_0 - K e^{-rT}
$$

**This means:**

$$
\text{Long Call + Short Put} = \text{Long Spot} - K e^{-rT}
$$

**At expiration:**

$$
\text{Long Call + Short Put} = S_T - K = \text{Forward Payoff}
$$

**Graphical representation:**

| Scenario | Call Payoff | Put Payoff | Combined |
|----------|-------------|------------|----------|
| $S_T < K$ | 0 | $-(S_T - K) = K - S_T$ | $K - S_T$ |
| $S_T > K$ | $S_T - K$ | 0 | $S_T - K$ |

**Combined: Linear payoff = $S_T - K$**

**This is IDENTICAL to buying at $K$ and selling at $S_T$!**

### 2. Synthetic Long Forward

**Construction:**

$$
\text{Synthetic Long} = \text{Long Call at } K + \text{Short Put at } K
$$

**Example (SPY trading at $450):**

**Build synthetic long at $450:**
- Buy 1 SPY Call, strike $450, 30 DTE: Cost $8.50
- Sell 1 SPY Put, strike $450, 30 DTE: Credit $8.30
- **Net debit: $0.20 ($20 per contract)**

**Payoff at expiration:**

| SPY Price | Call Value | Put Value | Combined P&L |
|-----------|------------|-----------|--------------|
| $420 | $0 | -$30 ($3,000) | -$3,000 |
| $435 | $0 | -$15 ($1,500) | -$1,500 |
| $450 | $0 | $0 | $0 |
| $465 | $15 ($1,500) | $0 | +$1,500 |
| $480 | $30 ($3,000) | $0 | +$3,000 |

**Slope: 1:1 (delta = 1.0)**

**Identical to:**
- Buying SPY at $450
- Or long SPY futures
- **Perfect replication**

### 3. Synthetic Short Forward

**Construction:**

$$
\text{Synthetic Short} = \text{Short Call at } K + \text{Long Put at } K
$$

**Example (Gold at $2,000/oz):**

**Build synthetic short at $2,000:**
- Sell 1 Gold Call, strike $2,000, 60 DTE: Credit $45
- Buy 1 Gold Put, strike $2,000, 60 DTE: Cost $43
- **Net credit: $2 ($200 per contract)**

**Payoff at expiration:**

| Gold Price | Call Value | Put Value | Combined P&L |
|------------|------------|-----------|--------------|
| $1,900 | $0 | $100 ($10,000) | +$10,000 |
| $1,950 | $0 | $50 ($5,000) | +$5,000 |
| $2,000 | $0 | $0 | $0 |
| $2,050 | -$50 (-$5,000) | $0 | -$5,000 |
| $2,100 | -$100 (-$10,000) | $0 | -$10,000 |

**Slope: -1:1 (delta = -1.0)**

**Identical to:**
- Shorting gold at $2,000
- Or short gold futures
- **Perfect replication**

### 4. Why Use Synthetics vs Futures?

**Several tactical reasons:**

**1. Pricing inefficiency:**

$$
C - P \neq F - K e^{-rT}
$$

**If options mispriced:**
- Can create synthetic cheaper than futures
- Arbitrage opportunity
- **Profit from basis**

**2. Margin efficiency:**

**Futures margin:**
- Initial margin: $10,000-50,000 per contract
- Maintenance: $8,000-40,000
- Cash tied up

**Synthetic margin:**
- Covered (cash-secured): Same as futures
- Portfolio margin: Often 30-50% less
- **Capital efficiency**

**3. Market access:**

**Futures unavailable or illiquid:**
- Individual stocks (no futures)
- Small-cap indices
- International markets (restrictions)
- **Synthetics provide access**

**4. Regulatory advantages:**

**Futures regulations:**
- Pattern day trader rules (equities)
- Position limits
- Reporting requirements

**Options:**
- More flexibility
- Different treatment
- **Tactical advantage**

**5. Tax efficiency:**

**Futures:**
- 60/40 treatment (US)
- Marked to market

**Synthetics:**
- Equity options treatment
- Long-term capital gains possible
- **Tax planning tool**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/synthetic_forward.png?raw=true" alt="synthetic_forward" width="700">
</p>
**Figure 1:** Synthetic forward construction showing put-call parity relationship. Long call + short put at strike K creates identical payoff to long forward position, while short call + long put replicates short forward. The linear 1:1 payoff profile matches futures exactly, enabling directional exposure through options when futures are unavailable, mispriced, or capital-inefficient.

---

## Economic Interpretation

**Beyond the mechanics, understanding the economic rationale:**

### 1. Put-Call Parity as Arbitrage Enforcement

**The deep insight:**

Put-call parity is NOT a model assumption—it's an **arbitrage-enforced relationship**. If violated, traders can lock in risk-free profit, quickly restoring equilibrium.

**Formal derivation:**

**Portfolio A:** Long call + Short put + Cash $K e^{-rT}$

**Value at expiration:**

$$
V_A(T) = \max(S_T - K, 0) - \max(K - S_T, 0) + K
$$

**Case 1: $S_T > K$**

$$
V_A = (S_T - K) - 0 + K = S_T
$$

**Case 2: $S_T < K$**

$$
V_A = 0 - (K - S_T) + K = S_T
$$

**Always:** $V_A(T) = S_T$

**Portfolio B:** Long stock

**Value at expiration:**

$$
V_B(T) = S_T
$$

**Identical payoffs → Must have identical prices:**

$$
C - P + K e^{-rT} = S_0
$$

**Rearranged:**

$$
C - P = S_0 - K e^{-rT}
$$

**This is put-call parity!**

### 2. Arbitrage Example

**If parity violated:**

$$
C - P > S_0 - K e^{-rT} \quad \text{(options too expensive)}
$$

**Arbitrage strategy:**

1. Sell call at $C$
2. Buy put at $P$
3. Buy stock at $S_0$
4. Borrow $K e^{-rT}$ (to fund stock purchase)

**Cash flows:**

**Today:**

$$
\text{Cash} = C - P - S_0 + K e^{-rT} > 0 \quad \text{(immediate profit!)}
$$

**At expiration:**

| Scenario | Call | Put | Stock | Loan | Net |
|----------|------|-----|-------|------|-----|
| $S_T > K$ | $-(S_T - K)$ | $0$ | $S_T$ | $-K$ | $0$ |
| $S_T < K$ | $0$ | $K - S_T$ | $S_T$ | $-K$ | $0$ |

**Zero risk at expiration + immediate profit today = arbitrage!**

**Market makers would:**
- Execute this trade
- Exploit mispricing
- Restore parity
- **Equilibrium enforced**

### 3. Interest Rate Component

**Put-call parity includes time value of money:**

$$
C - P = F_0 - K e^{-rT}
$$

For futures:

$$
F_0 = S_0 e^{rT}
$$

**Substituting:**

$$
C - P = S_0 e^{rT} - K e^{-rT}
$$

**When $K = S_0$ (ATM):**

$$
C - P = S_0(e^{rT} - e^{-rT}) \approx S_0 \times 2rT \quad \text{(for small } rT)
$$

**Example:**

- SPY: $450
- Strike: $450 (ATM)
- Time: 30 days (0.082 years)
- Rate: 5%

$$
C - P \approx 450 \times 2 \times 0.05 \times 0.082 = \$3.69
$$

**So:**
- Call premium: $11.85
- Put premium: $8.16
- Difference: $3.69
- **Matches formula!**

**This $3.69 difference is the present value of carrying cost.**

### 4. Dividends Complicate Parity

**For dividend-paying stocks:**

$$
C - P = S_0 e^{-qT} - K e^{-rT}
$$

Where $q$ = continuous dividend yield

**Or for discrete dividends:**

$$
C - P = (S_0 - PV(\text{Divs})) - K e^{-rT}
$$

**Example (AAPL with $0.96 quarterly dividend):**

**Setup:**
- AAPL: $185
- Next dividend: $0.24 in 15 days
- Strike: $185 (ATM)
- Expiration: 45 days
- Rate: 5%

**Dividend adjustment:**

$$
PV(\text{Div}) = 0.24 \times e^{-0.05 \times 15/365} = \$0.2395
$$

**Adjusted parity:**

$$
C - P = (185 - 0.2395) - 185 e^{-0.05 \times 45/365} = 184.76 - 183.86 = \$0.90
$$

**Without dividend:**

$$
C - P = 185 - 183.86 = \$1.14
$$

**Difference: $0.24 (the dividend!)**

**Dividends reduce synthetic forward cost for longs.**

### 5. Why Synthetics Can Be Cheaper

**Several market imperfections:**

**1. Implied volatility skew:**

**Put skew (equities):**
- OTM puts: Higher IV (crash protection)
- OTM calls: Lower IV
- **Net: Selling expensive puts, buying cheaper calls**

**If constructing synthetic long at OTM strike:**
- Sell expensive OTM put
- Buy less expensive OTM call
- **Better pricing than futures**

**2. Early exercise premium (American options):**

**American puts:**
- Early exercise value
- Higher premium than European
- **Can sell this premium**

**Synthetics with American options:**
- Capture early exercise premium
- Not available in futures
- **Additional income**

**3. Volatility term structure:**

**Different expirations:**
- Near-term: Higher IV
- Far-term: Lower IV
- **Can optimize selection**

**4. Liquidity inefficiencies:**

**Bid-ask spreads:**
- Futures: Tight spreads (0.01-0.05%)
- Options: Wider spreads (0.5-2%)
- But sometimes BETTER pricing via synthetics
- **Market microstructure**

### 6. Futures vs Synthetics

| Feature | Futures | Synthetic (Options) |
|---------|---------|---------------------|
| Payoff | Linear (1:1) | Linear (1:1) |
| Margin | $10k-50k per contract | Portfolio margin: 30-50% less |
| Liquidity | Excellent (major contracts) | Good (liquid stocks) |
| Availability | Limited markets | Any optionable stock |
| Dividends | Priced in futures | Manual adjustment needed |
| Early exercise | N/A | Risk (American options) |
| Tax treatment | 60/40 (US) | Capital gains (equity) |
| Commissions | $1-5 per side | $0.50-1.50 per contract |
| Complexity | Simple | More complex |
| Regulatory | Futures regulations | Securities regulations |

**When to use synthetics:**

- Futures unavailable (individual stocks)
- Margin constraints (portfolio margin advantage)
- Volatility skew exploitable
- Tax optimization needs
- **Tactical advantages**

---

## Key Terminology

**Put-Call Parity:**

$$
C - P = S_0 - K e^{-rT}
$$

- Fundamental options relationship
- Arbitrage-enforced
- Links calls, puts, stock, bonds
- Foundation for synthetics

**Synthetic Long:**

$$
\text{Long Call} + \text{Short Put} = \text{Long Forward}
$$

- Replicates long position
- Delta = +1.0
- Same risk/reward as futures
- Capital-efficient

**Synthetic Short:**

$$
\text{Short Call} + \text{Long Put} = \text{Short Forward}
$$

- Replicates short position
- Delta = -1.0
- Inverse futures exposure
- Profit from declines

**Strike Price (K):**

- Price at which synthetic is constructed
- Determines forward entry level
- Can be ATM, ITM, or OTM
- **Flexibility advantage**

**Conversion:**

$$
\text{Synthetic Long} + \text{Short Stock} = \text{Long Call} + \text{Short Put} - \text{Stock}
$$

- Arbitrage strategy
- Locks in parity violation
- Market maker trade
- **Risk-free profit**

**Reversal:**

$$
\text{Synthetic Short} + \text{Long Stock} = \text{Short Call} + \text{Long Put} + \text{Stock}
$$

- Opposite of conversion
- Also arbitrage
- Exploits mispricing
- **Risk-free profit**

**Box Spread:**

$$
\text{Long Synthetic at } K_1 + \text{Short Synthetic at } K_2
$$

- Synthetic borrowing/lending
- Locks in interest rate
- Arbitrage tool
- **Fixed payoff**

**Early Exercise Risk:**

- American options can be exercised early
- Disrupts synthetic position
- Requires management
- **Tactical consideration**

**Basis (Futures-Synthetic):**

$$
\text{Basis} = \text{Futures Price} - \text{Synthetic Price}
$$

- Measures mispricing
- Arbitrage opportunity if large
- Typically small (0.05-0.20%)
- **Efficiency indicator**

**Cost of Carry:**

$$
\text{Carry} = rT - qT
$$

- Interest cost - dividend income
- Embedded in futures price
- Explicit in synthetics
- **Time value component**

**Pin Risk:**

- Stock closes exactly at strike
- Uncertainty if options exercised
- Can disrupt synthetic
- **Expiration risk**

---

## The Greeks

**Synthetics replicate futures Greeks:**

### 1. Delta

**Definition:** Sensitivity to underlying price changes.

$$
\Delta_{\text{synthetic long}} = \Delta_{\text{call}} + \Delta_{\text{put}} = 1.0 + (-0) = 1.0
$$

$$
\Delta_{\text{synthetic short}} = \Delta_{\text{call}} + \Delta_{\text{put}} = 0 + (-1.0) = -1.0
$$

**Perfect replication:**

**Synthetic long (ATM):**
- Long ATM call: Delta ≈ +0.50
- Short ATM put: Delta ≈ -(-0.50) = +0.50
- **Combined: +1.0 (identical to futures)**

**Synthetic short:**
- Short ATM call: Delta ≈ -0.50
- Long ATM put: Delta ≈ -0.50
- **Combined: -1.0 (identical to short futures)**

**Example:**

**SPY synthetic long at $450:**
- SPY moves $1 → Synthetic gains $1
- Futures moves $1 → Futures gains $1
- **Identical delta exposure**

**Deep ITM/OTM (strike selection matters):**

**OTM synthetic long ($K = 480$ when SPY = $450):**
- Long 480 call: Delta ≈ 0.20
- Short 480 put: Delta ≈ -(−0.80) = +0.80
- **Combined: +1.0 (still perfect!)**

**Always delta = 1.0 regardless of strike!**

### 2. Gamma (Convexity)

**Definition:** Change in delta as underlying moves.

$$
\Gamma_{\text{synthetic}} = \Gamma_{\text{call}} - \Gamma_{\text{put}}
$$

**Key insight:**

$$
\Gamma_{\text{call}}(K) = \Gamma_{\text{put}}(K)
$$

**Therefore:**

$$
\Gamma_{\text{synthetic}} = \Gamma - \Gamma = 0
$$

**Zero gamma = linear payoff (like futures!)**

**Why this matters:**

**Futures:**
- Delta always 1.0
- No gamma
- Linear

**Synthetic:**
- Net delta always 1.0
- Zero net gamma
- Linear
- **Perfect match**

**But individual legs have gamma:**

**Near expiration (1 DTE):**
- Call gamma: +15.0
- Put gamma: +15.0 (sold, so -15.0)
- Net: 0
- **But requires rebalancing if assigned early**

### 3. Theta (Time Decay)

**Definition:** Change in value as time passes.

$$
\Theta_{\text{synthetic}} = \Theta_{\text{call}} + \Theta_{\text{put}}
$$

**Put-call parity implies:**

$$
\Theta_{\text{synthetic}} \approx -r \times (S - K)
$$

**For ATM synthetic ($S = K$):**

$$
\Theta \approx 0
$$

**Example:**

**SPY synthetic long at $450 (SPY = $450):**
- Long 450 call: Theta = -$8/day
- Short 450 put: Theta = +$8/day
- **Net theta ≈ $0**

**For ITM synthetic:**

**SPY = $460, synthetic struck at $450:**

$$
\Theta \approx -0.05 \times 10 = -\$0.50/\text{day}
$$

**Small theta from carrying cost**

**Futures theta:**
- Also ≈ 0 (marked to market)
- **Synthetics match**

### 4. Vega

**Definition:** Sensitivity to implied volatility changes.

$$
\text{Vega}_{\text{synthetic}} = \text{Vega}_{\text{call}} - \text{Vega}_{\text{put}}
$$

**Key insight:**

$$
\text{Vega}_{\text{call}}(K) = \text{Vega}_{\text{put}}(K)
$$

**Therefore:**

$$
\text{Vega}_{\text{synthetic}} = \text{Vega} - \text{Vega} = 0
$$

**Zero vega = no volatility exposure (like futures!)**

**Example:**

**SPY synthetic long:**
- IV increases 5% (e.g., 15% → 20%)
- Long call value: +$50
- Short put value: -$50 (costs more to buy back)
- **Net: $0 impact**

**Futures:**
- IV increase: $0 impact
- **Synthetics match**

**This is HUGE advantage:**
- Volatility spikes don't affect synthetics
- Unlike pure option strategies
- **Directional purity**

### 5. Rho

**Definition:** Sensitivity to interest rate changes.

$$
\rho_{\text{synthetic}} = \rho_{\text{call}} - \rho_{\text{put}}
$$

**Put-call parity:**

$$
C - P = S - K e^{-rT}
$$

**Taking derivative with respect to $r$:**

$$
\rho_C - \rho_P = K T e^{-rT} \approx K T
$$

**Example:**

**SPY synthetic long at $450, 90 DTE:**
- Rate increases 1% (5% → 6%)
- Impact: $450 × 0.25 = $1.13
- **Small positive impact (long forward benefits from higher rates)**

**Futures rho:**
- Also positive for longs
- Embedded in futures price
- **Synthetics match**

**Typically ignored (small):**
- Unless long-dated (LEAPS)
- Or large rate moves
- **Minor Greek**

---

## Strategy Selection

**Different synthetic constructions for different goals:**

### 1. ATM Synthetic (Most Common)

**Strike = Current spot price**

$$
K = S_0
$$

**Characteristics:**

- Most liquid (ATM options)
- Tightest bid-ask spreads
- Balanced delta contribution
- **Standard implementation**

**Example:**

**TSLA at $250:**
- Buy 250 call: $12.50
- Sell 250 put: $12.30
- Net cost: $0.20
- **Replicates long at $250**

**Pros:**

- Maximum liquidity
- Minimal transaction costs
- Easy to execute
- **Default choice**

**Cons:**

- No directional edge
- Pays full "forward premium"
- **Neutral pricing**

### 2. OTM Synthetic (Bullish Tilt)

**Strike > Current spot (for longs)**

$$
K > S_0
$$

**Characteristics:**

- Cheaper calls (OTM)
- Expensive puts (ITM)
- Net credit or small debit
- **Bullish selection**

**Example:**

**SPY at $450:**
- Buy 465 call: $5.00 (OTM)
- Sell 465 put: $20.00 (ITM)
- Net credit: $15.00
- **Get paid to be long!**

**But:**

**Breakeven at expiration:**

- Need SPY > $465 to profit
- Below $465: Lose on linear basis
- **Upside participation only above $465**

**When to use:**

- Very bullish
- Want cheaper entry
- Accept higher breakeven
- **Tactical positioning**

### 3. ITM Synthetic (Conservative)

**Strike < Current spot (for longs)**

$$
K < S_0
$$

**Characteristics:**

- Expensive calls (ITM)
- Cheap puts (OTM)
- Larger debit
- **Conservative positioning**

**Example:**

**Gold at $2,000:**
- Buy 1,950 call: $65 (ITM)
- Sell 1,950 put: $10 (OTM)
- Net debit: $55
- **Lower breakeven**

**Payoff:**

- Profit above $1,950 (current $2,000)
- Already $50 ITM
- **Downside cushion**

**When to use:**

- Moderately bullish
- Want downside protection
- Accept higher cost
- **Defensive long**

### 4. Leveraged Synthetic (Multiple Contracts)

**Scale up position:**

**Standard synthetic:**
- 1 call + 1 put = 100 shares exposure

**Leveraged (2×):**
- 2 calls + 2 puts = 200 shares exposure
- Double delta
- **Amplified returns**

**Example:**

**QQQ at $400:**
- Buy 2x 400 calls: $8 × 2 = $16
- Sell 2x 400 puts: $7.80 × 2 = $15.60
- Net: $0.40 for 200 shares exposure
- **2× leverage**

**Margin requirements:**

- Naked puts = high margin
- But offsetting calls reduce
- Portfolio margin: Efficient
- **Check carefully**

**Risk:**

- Double exposure
- Double losses
- Margin calls possible
- **Use sparingly**

### 5. Calendar Synthetic

**Near-term short, long-term long:**

$$
\text{Buy long-dated call} + \text{Sell near-dated put}
$$

**Characteristics:**

- Exploits theta decay
- Rolls put monthly
- Long-term directional view
- **Income generation**

**Example:**

**AAPL at $185:**
- Buy Jan 185 call (365 DTE): $25
- Sell Feb 185 put (30 DTE): $4
- Roll put monthly for $4 credit
- **Reduce call cost over time**

**After 6 months:**
- Collected 6 × $4 = $24 in put premiums
- Effective call cost: $25 - $24 = $1
- **Nearly free synthetic**

**Risks:**

- Put assignment (get stock)
- Stock drops (losses on both)
- Requires active management
- **Complex**

### 6. Comparison Table

| Synthetic Type | Strike | Cost | Delta | Best For |
|----------------|--------|------|-------|----------|
| ATM | $S_0$ | ~$0 | +1.0 | Standard replication |
| OTM (Bull) | $S_0 + \Delta$ | Credit | +1.0 | Very bullish, cheap entry |
| ITM (Conservative) | $S_0 - \Delta$ | Debit | +1.0 | Cautious, downside cushion |
| Leveraged | Any | $N \times$ cost | $N$ | Amplified exposure |
| Calendar | Any | Variable | +1.0 | Income generation |

**Beginner recommendation: ATM synthetic (simplest, most liquid, standard replication)**

---

## Time Selection

**Unlike pure options, synthetics are held like futures:**

### 1. Entry Timing

**Synthetics can be entered anytime:**

**No time decay concerns:**
- Net theta ≈ 0
- Unlike long options
- **Timing flexible**

**Considerations:**

**1. Volatility regime:**

$$
\text{Enter when IV moderate (15-25th percentile)}
$$

**Why:**

- High IV: Options expensive (widens bid-ask)
- Low IV: Options cheap (better execution)
- **Sweet spot: Normal vol**

**2. Liquidity:**

$$
\text{Open interest} > 1,000 \text{ contracts per strike}
$$

**Ensures:**
- Tight spreads
- Easy entry/exit
- **No slippage**

**3. Time to expiration:**

**Minimum DTE:**

$$
\text{DTE} \geq 30 \text{ days}
$$

**Why:**

- <30 DTE: Gamma risk increases
- Pin risk at expiration
- Early exercise risk
- **Avoid short-dated**

**Optimal DTE:**

$$
\text{DTE} = 45\text{-}90 \text{ days}
$$

**Sweet spot:**
- Liquid options
- Reasonable spreads
- Manageable gamma
- **Professional choice**

**4. Dividend considerations:**

**Before ex-dividend date:**
- Check dividend schedule
- Calls worth less (dividend captured by stock holder)
- Puts worth more (right to sell stock that goes ex-div)
- **Parity adjustment**

**If large dividend approaching:**

$$
\text{Avoid entering synthetic 10 days before ex-div}
$$

**Early exercise risk on short put!**

### 2. Exit Timing

**Three approaches:**

**Approach 1: Hold to expiration**

$$
\text{Let options expire, settle at intrinsic value}
$$

**Process:**

- Call: Automatically exercised if ITM
- Put: Automatically assigned if ITM
- Net: Synthetic converts to stock position
- **Final settlement**

**Example:**

**SPY synthetic long at $450:**
- Expiration: SPY at $465
- Call ITM: Exercise, buy stock at $450
- Put OTM: Expires worthless
- **Result: Long 100 SPY shares at $450**

**Can then:**
- Sell stock at $465 (realize $15 profit)
- Hold stock (if want long position)
- **Flexibility**

**Approach 2: Close before expiration**

$$
\text{Exit 3-7 days before expiration}
$$

**Process:**

- Buy back short put
- Sell long call
- Net: Realize P&L in cash
- **Clean exit**

**Example:**

**Exit 5 DTE:**
- SPY at $465
- Sell 450 call: $15.20
- Buy 450 put: $0.05
- Net: $15.15 profit
- **Closed position**

**Pros:**

- Avoid assignment
- No pin risk
- Cash settlement
- **Simple**

**Cons:**

- Pay spreads twice (entry + exit)
- Time value left on table
- **Transaction costs**

**Approach 3: Roll to new expiration**

$$
\text{Close current, open new 45-90 DTE}
$$

**Process:**

- Close current synthetic (5-7 DTE)
- Open new synthetic (60 DTE)
- Maintain directional exposure
- **Continuous position**

**Example:**

**Current:**
- Close March 450 synthetic: $15 profit

**New:**
- Open May 465 synthetic: $0.30 debit
- **Maintain long exposure with profits**

**When to use:**
- Want ongoing exposure
- Directional view unchanged
- **Long-term positioning**

### 3. Early Assignment Management

**Risk: Short put exercised early**

**When it happens:**

$$
\text{Put exercised if: Stock} < \text{Strike AND Extrinsic Value} < \text{Dividend}
$$

**Example:**

**AAPL synthetic long at $185:**
- AAPL drops to $170 (put $15 ITM)
- Put extrinsic: $0.50
- Dividend tomorrow: $0.24
- **Likely NOT exercised (extrinsic > dividend)**

**But if:**
- Put $30 ITM ($155 stock)
- Extrinsic: $0.10
- **Risk of early exercise**

**Response:**

**If assigned:**
1. Receive stock at $185 (via put assignment)
2. Still own 185 call
3. Can sell stock at market ($170) for $15 loss
4. Or hold stock + call (covered call position)
5. **Flexibility**

**Preventive measures:**

$$
\text{If put becomes} > \$10 \text{ ITM, consider closing}
$$

**Avoid deep ITM short puts near expiration**

---

## Maximum Profit and Loss

### 1. Synthetic Long Position

**Setup:**

- Stock: NVDA at $500
- Strategy: Synthetic long via options
- Buy 1 NVDA 500 call (60 DTE): $27
- Sell 1 NVDA 500 put (60 DTE): $26
- Net debit: $1 ($100 total)

**Maximum Profit (Unlimited):**

**NVDA rallies to $700 (40% gain):**

**At expiration:**
- Call value: $700 - $500 = $200
- Put value: $0 (expires worthless)
- Net: $200 - $1 (entry cost) = $199

$$
\text{Profit} = \$199 \times 100 = \$19,900
$$

$$
\text{Return} = \frac{\$19,900}{\$100} = 19,900\%
$$

**Wait, that's not right. The return calculation should be on the margin/capital at risk, not just the net debit.**

**Correct analysis:**

**Capital at risk:**
- Short put requires margin: ~$10,000
- Net debit paid: $100
- Total capital: ~$10,100

**Profit: $19,900**

**Return:**

$$
\text{Return} = \frac{\$19,900}{\$10,100} = 197\%
$$

**Equivalent to:**
- Buying 100 shares at $500: $50,000 capital
- Selling at $700: $70,000
- Profit: $20,000
- Return: 40%
- **Synthetic provides ~5× leverage!**

**Maximum Loss (Substantial but Limited to Stock → 0):**

**NVDA crashes to $250 (50% decline):**

**At expiration:**
- Call value: $0 (expires worthless)
- Put assigned: Buy stock at $500
- Stock worth: $250
- Loss: $500 - $250 = $250 per share

$$
\text{Loss} = \$250 \times 100 = -\$25,000
$$

$$
\text{Plus entry cost} = -\$25,100
$$

**Or could close synthetic before expiration:**
- Buy back put: $250 (intrinsic)
- Sell call: $0
- Net: -$249 loss per share
- **Same result**

**Breakeven:**

$$
\text{Breakeven} = K + \text{Net Debit} = \$500 + \$1 = \$501
$$

**Need NVDA > $501 at expiration to profit**

### 2. Synthetic Short Position

**Setup:**

- Stock: TSLA at $250
- Strategy: Synthetic short
- Sell 1 TSLA 250 call (60 DTE): $14
- Buy 1 TSLA 250 put (60 DTE): $13
- Net credit: $1 ($100 received)

**Maximum Profit (Limited to Strike):**

**TSLA crashes to $100 (60% decline):**

**At expiration:**
- Call expires: $0
- Put value: $250 - $100 = $150
- Net: $150 + $1 (entry credit) = $151

$$
\text{Profit} = \$151 \times 100 = \$15,100
$$

**On capital at risk:**
- Short call margin: ~$5,000
- Put cost: $1,300
- Total: ~$6,300

$$
\text{Return} = \frac{\$15,100}{\$6,300} = 240\%
$$

**Maximum Loss (Unlimited):**

**TSLA rallies to $450 (80% gain):**

**At expiration:**
- Call assigned: Short stock at $250
- Stock at: $450
- Loss: $450 - $250 = $200 per share
- Put expires: $0

$$
\text{Loss} = -\$200 \times 100 = -\$20,000
$$

$$
\text{Minus entry credit} = -\$19,900
$$

**Theoretically unlimited if stock keeps rising!**

### 3. Real Example

**Advanced synthetic strategy:**

**Box spread = Long synthetic at $K_1$ + Short synthetic at $K_2$**

**Setup (SPY):**

**Long synthetic at $450:**
- Buy 450 call: $10
- Sell 450 put: $9
- Net: $1

**Short synthetic at $460:**
- Sell 460 call: $4
- Buy 460 put: $15
- Net: $11 credit

**Combined box:**
- Net credit received: $11 - $1 = $10
- Spread width: $460 - $450 = $10
- **Locked in $10 payoff at expiration**

**At expiration (any SPY price):**

| SPY Price | 450 Synthetic | 460 Synthetic | Combined |
|-----------|---------------|---------------|----------|
| $440 | -$10 | +$20 | +$10 |
| $455 | +$5 | +$5 | +$10 |
| $470 | +$20 | -$10 | +$10 |

**Always $10 payoff!**

**Return calculation:**

Received $10 today, owe $10 at expiration (60 days)

$$
\text{Implied rate} = 0\% \quad \text{(broke even)}
$$

**If received $10.20 today:**

$$
\text{Implied rate} = \frac{10.20 - 10.00}{10.00} \times \frac{365}{60} = 12.2\% \text{ annually}
$$

**Arbitrage if risk-free rate < 12.2%!**

**This is synthetic borrowing/lending via options**

---

## When to Use Synthetic Forwards

### 1. Ideal Market Conditions

**Use synthetics when:**

**1. Futures unavailable:**

$$
\text{No futures contract for desired underlying}
$$

**Examples:**
- Individual stocks (AAPL, GOOGL, TSLA)
- Small-cap indices (Russell Microcap)
- Sector-specific ETFs
- **Options provide access**

**2. Margin efficiency needed:**

**Portfolio margin benefits:**

- Futures: $15k margin per ES contract
- Synthetic ES: $8k margin (portfolio margin)
- **Savings: 47%**

**When portfolio margin available:**
- Larger accounts ($125k+)
- Prime brokers
- Hedge funds
- **Capital optimization**

**3. Volatility skew exploitable:**

**Equity put skew:**

- OTM puts expensive (crash premium)
- OTM calls cheaper
- Synthetic long: Buy cheap call, sell expensive put
- **Net benefit vs futures**

**Example:**

**SPY synthetic:**
- Fair value (put-call parity): $0.20 debit
- Actual (due to skew): $0.10 credit
- **Save $30 per synthetic vs futures!**

**4. Tax optimization:**

**Long-term capital gains:**

- Hold synthetic >12 months
- Qualify for long-term rates (20% vs 37%)
- Futures: 60/40 treatment (no long-term)
- **Tax savings**

**5. Dividends capturable:**

**Synthetic long captures dividends:**

- Get assigned on short put before ex-div
- Own stock, receive dividend
- Exercise call if want to exit
- **Dividend arbitrage possible**

### 2. Specific Use Cases

**Use Case 1: Individual stock exposure**

**Goal: Long NVDA without buying shares**

**Why synthetics:**
- NVDA futures don't exist
- Don't want to tie up $50k (100 shares)
- Portfolio margin available
- **Synthetic solution**

**Implementation:**
- NVDA: $500
- Buy 500 call (90 DTE): $27
- Sell 500 put (90 DTE): $26
- Net: $1 debit
- Margin: $10k (portfolio margin)
- **Exposure: $50k for $10k capital**

**Use Case 2: Pair trade**

**Goal: Long TSLA, Short F (Tesla vs Ford)**

**Why synthetics:**
- Can't short F futures (don't exist)
- Don't want to borrow shares (cost)
- Want leverage on both sides
- **Synthetic short F**

**Implementation:**

**Long TSLA synthetic:**
- Buy 250 call, sell 250 put
- Net: $0.50 debit

**Short F synthetic:**
- Sell 12 call, buy 12 put
- Net: $0.10 credit

**Ratio: 1 TSLA : 20 F (dollar-neutral)**

**Use Case 3: Earnings play**

**Goal: Long QQQ through earnings, avoid IV crush**

**Why synthetics:**
- Buying call: Loses to IV crush
- Synthetic: Zero vega!
- **Directional purity**

**Implementation:**
- Day before earnings
- QQQ: $400
- Buy 400 call: $10 (40% IV)
- Sell 400 put: $9.50 (40% IV)
- Net: $0.50

**After earnings:**
- IV drops 40% → 25%
- Long call: -$2 (vega loss)
- Short put: +$2 (vega gain)
- **Net vega: $0**

**Only directional move matters!**

**Use Case 4: Rolldown strategy**

**Goal: Lower cost basis of long stock position**

**Current:**
- Own AAPL at $200
- Now $185 (unrealized loss -$15)

**Strategy:**
- Sell AAPL stock: $185 (realize loss for tax)
- Enter synthetic long at $185:
  - Buy 185 call: $8
  - Sell 185 put: $7.50
  - Net: $0.50

**Benefits:**
- Maintain exposure
- Harvest tax loss
- Lower effective basis
- **Tax-loss harvesting**

**Use Case 5: Leveraged index exposure**

**Goal: 3× leverage on SPY without margin loan**

**Instead of:**
- Borrow $600k @ 8%
- Buy $600k SPY
- **Cost: $48k/year interest**

**Use synthetics:**
- $200k account
- Enter 6 SPY synthetics (each = $45k notional)
- Total notional: $270k (1.35× not 3×)

**Wait, need more leverage:**

**Use futures instead OR:**
- 20 SPY synthetics
- Notional: $900k (4.5×)
- Margin: ~$400k (portfolio margin)
- **Maximum leverage**

**But synthetics limited compared to futures for pure leverage**

---

## When NOT to Use Synthetic Forwards

### 1. Avoid These Situations

**1. Liquid futures available:**

**If futures liquid:**
- ES (S&P 500): Volume 2M+ contracts/day
- CL (Crude oil): Volume 500k+/day
- GC (Gold): Volume 200k+/day
- **Use futures (simpler, cheaper)**

**Synthetics only make sense when futures lacking or inefficient**

**2. Options illiquid:**

$$
\text{Open Interest} < 500 \text{ per strike}
$$

**If options illiquid:**
- Wide bid-ask spreads (2-5%)
- Slippage on entry/exit
- Difficult to close position
- **Costs > benefits**

**Check liquidity:**
- OI >1,000 (good)
- OI 500-1,000 (acceptable)
- OI <500 (avoid)
- **Minimum threshold**

**3. Near expiration (<14 DTE):**

**Risks multiply:**
- Gamma risk (delta instability)
- Pin risk (uncertainty at strike)
- Early exercise (assignment risk)
- **Too dangerous**

**Better:**
- Close position
- Roll to new expiration
- Use futures instead
- **Avoid short-dated synthetics**

**4. High dividend stocks:**

**If dividend >2%:**

- Early exercise risk on short puts
- Dividend arbitrage by counterparties
- Assignment complexity
- **Futures cleaner**

**Example:**

**AT&T (T) yields 7%:**
- Short put faces continuous exercise threat
- Synthetics problematic
- **Use stock or skip**

**5. Margin constraints:**

**If no portfolio margin:**
- Reg-T margin expensive
- Short put = 100% of strike margin
- Futures often cheaper
- **Check margin requirements**

**Example:**

**SPY synthetic Reg-T margin:**
- Strike: $450
- Margin: $45,000 (100%)
- **Ties up massive capital**

**Futures:**
- ES margin: $12,000
- Notional: $225,000
- **More efficient**

**6. Tax inefficiencies:**

**If in tax-free account (IRA):**
- No tax benefit from long-term gains
- Synthetics = complexity with no benefit
- Use futures or stock
- **Simpler alternatives**

**7. Cannot monitor positions:**

**Synthetics require attention:**
- Early exercise risk
- Roll dates
- Pin risk
- Margin calls
- **Active management**

**If passive investor:**
- Use stock
- Use ETFs
- Skip synthetics
- **Too complex**

### 2. Warning Signs to Unwind

**1. Approaching expiration (<7 DTE):**

**Risks escalate:**
- Gamma explodes
- Pin risk high
- Early exercise likely (ITM)
- **Close or roll**

**2. Deep ITM/OTM (>$20 from strike):**

**If synthetic moved against you:**

**Example:**
- Synthetic long at $450
- Stock now $420 (down $30)
- Put $30 ITM
- **Early assignment risk**

**Action:**
- Close synthetic
- Enter new at-the-money
- Reset position
- **Avoid deep ITM**

**3. Volatility spike (>50% IV):**

**High IV = wide spreads:**

- Bid-ask spreads balloon
- Difficult to exit cleanly
- Costs eat profits
- **Wait for vol decline**

**Unless:**
- Urgent exit needed
- Accept slippage
- **Tactical decision**

**4. Dividend approaching (<10 days):**

**If large dividend:**

- Short put will be exercised
- Early assignment
- Disrupts position
- **Close before ex-div**

**Or:**
- Close short put only
- Keep long call
- Reestablish put after ex-div
- **Management required**

**5. Margin call:**

**If account value declines:**
- Margin requirements increase
- Broker demands more capital
- **Reduce positions immediately**

---

## Position Sizing and Risk Management

### 1. The Golden Rule

**Position sizing:**

$$
\text{Synthetics} = \text{Desired Futures Contracts} \times 100 \text{ (if stock options)}
$$

**Example:**

**Want exposure to 5 ES contracts:**

- Each ES = $50 × SPX = $50 × 4,500 = $225,000
- Total: 5 × $225,000 = $1,125,000

**Using SPY synthetics:**
- SPY = $450 (1/10 of SPX)
- Each SPY synthetic = $45,000
- Contracts needed: $1,125,000 / $45,000 = 25 SPY synthetics
- **25 long calls + 25 short puts**

### 2. Portfolio Allocation

**Conservative (5-10% in synthetics):**

**$500k account:**
- Synthetics: $25-50k (5-10%)
- Margin required: ~$15-30k (portfolio margin)
- Remaining: $470-485k
- **Low leverage**

**Moderate (10-20%):**
- Synthetics: $50-100k (10-20%)
- Margin: ~$30-60k
- Remaining: $440-470k
- **Moderate leverage**

**Aggressive (20-40%):**
- Synthetics: $100-200k (20-40%)
- Margin: ~$60-120k
- Remaining: $380-440k
- **High leverage**

**Never >40% in synthetics:**
- Need cash buffer
- Margin calls possible
- Early assignment risk
- **Safety first**

### 3. Margin Management

**Two margin systems:**

**Reg-T (Standard):**

$$
\text{Margin} = \max(K, 0.2 \times S_0) \times 100
$$

**Example (SPY synthetic at $450):**

$$
\text{Margin} = \max(\$450, 0.2 \times \$450) \times 100 = \$45,000
$$

**Very capital-intensive!**

**Portfolio Margin (Advanced):**

$$
\text{Margin} \approx 15\text{-}25\% \text{ of notional}
$$

**Example (same SPY synthetic):**

$$
\text{Margin} \approx 0.20 \times \$45,000 = \$9,000
$$

**5× more efficient!**

**Requirements for portfolio margin:**
- Account > $125k
- Approval from broker
- Experience required
- **Not for beginners**

### 4. Diversification

**Don't concentrate:**

**Bad:**
- 50 TSLA synthetics
- 100% in one stock
- **Disaster waiting**

**Good:**
- 10 TSLA synthetics
- 10 AAPL synthetics
- 10 GOOGL synthetics
- 10 SPY synthetics
- 10 QQQ synthetics
- **Diversified**

**Across:**
- Sectors (tech, finance, energy)
- Market cap (large, mid, small)
- Geography (US, international)
- **Uncorrelated**

### 5. Stop Loss Strategy

**Price-based stop:**

$$
\text{Exit if underlying moves } >10\% \text{ against position}
$$

**Example:**

**SPY synthetic long at $450:**
- Stop: $405 (10% down)
- If SPY hits $405: Close synthetic
- **Limit loss**

**But for long-term:**
- May not want stop
- Accept volatility
- **Strategic hold**

**Time-based management:**

$$
\text{Close or roll } 7 \text{ days before expiration}
$$

**Always:**
- Monitor DTE
- Set calendar reminders
- Don't let expire accidentally
- **Active management**

### 6. Example

**Account: $500,000**

**Synthetics allocation: 20% = $100,000 notional**

**Positions:**

| Stock | Synthetics | Notional | Margin (PM) | Allocation |
|-------|------------|----------|-------------|------------|
| SPY | 5 | $22,500 | $4,500 | 22.5% |
| QQQ | 5 | $20,000 | $4,000 | 20% |
| TSLA | 8 | $20,000 | $4,000 | 20% |
| AAPL | 10 | $18,500 | $3,700 | 18.5% |
| NVDA | 4 | $20,000 | $4,000 | 20% |

**Total:**
- Notional: $101,000
- Margin: $20,200
- Cash buffer: $479,800
- **Conservative leverage**

**Risk metrics:**
- Max loss per position: 10% stop = $10,100
- Total max loss: $10,100 (2% of account)
- Margin coverage: 23.8× ($479,800 / $20,200)
- **Well-managed**

**Monthly monitoring:**
- Check DTE (roll at 7-14 DTE)
- Rebalance if positions drift
- Monitor margin utilization
- **Active oversight**

---

## Common Mistakes Beginners Make

### 1. Mistake #1

**The error:**

- Sell AAPL 180 put (stock at $185)
- AAPL drops to $170 (put $10 ITM)
- Ex-dividend tomorrow ($0.24)
- Think: "No worries, let it expire"
- **Assigned early!**

**What happens:**

- Put exercised before ex-div
- Required to buy 100 shares at $180
- Stock opens ex-div at $169.76 (down $0.24)
- Immediately down $10.24 per share
- **Loss: $1,024**

**Correct approach:**

**Monitor:**
- Dividend calendar
- Deep ITM short options
- Close before ex-div if >$5 ITM
- **Prevent assignment**

### 2. Mistake #2

**The error:**

- Want synthetic long small-cap stock
- Options have 50 OI, $0.80 bid-ask spread
- Enter anyway
- **Terrible execution**

**What happens:**

**Entry:**
- Buy call at ask: $3.40
- Sell put at bid: $2.20
- Net: $1.20 debit

**Fair value (mid-market):**
- Call: $3.00
- Put: $2.60
- Net: $0.40 debit
- **Overpaid $0.80 ($80) = 200% overpayment!**

**Correct approach:**

**Minimum liquidity:**
- Open interest >1,000
- Bid-ask spread <$0.20
- Volume >100 daily
- **Liquid markets only**

### 3. Mistake #3

**The error:**

- Want synthetic long SPY
- Buy 500 call (far OTM, cheap)
- Sell 400 put (far OTM, minimal premium)
- Think: "Cheap entry!"
- **Not actually a synthetic!**

**What happens:**

**Strikes must match:**
- Call at 500, put at 400
- These don't combine to linear payoff
- Delta ≠ 1.0
- **Not a forward**

**Correct approach:**

$$
\text{Call strike} = \text{Put strike} = K
$$

**Both at same strike!**

### 4. Mistake #4

**The error:**

- Synthetic long at $450
- Stock at $465 at expiration
- Let options expire
- **Surprise!**

**What happens:**

**Automatic exercise:**
- Long call: Auto-exercised, buy stock at $450
- Short put: Expires worthless
- Result: Long 100 shares at $450
- **Now have stock position**

**If wanted cash:**
- Must sell stock Monday
- Weekend risk (gap down possible)
- Execution uncertainty
- **Unexpected outcome**

**Correct approach:**

$$
\text{Close } 3\text{-}7 \text{ days before expiration}
$$

**Avoid exercise/assignment:**
- Sell call, buy back put
- Take cash profit
- Clean exit
- **Intentional settlement**

### 5. Mistake #5

**The error:**

- Synthetic long MSFT at $400
- MSFT pays $3 quarterly dividend
- Ignore it
- **Mispricing**

**What happens:**

**Put-call parity with dividends:**

$$
C - P = S - PV(\text{Divs}) - K e^{-rT}
$$

**Without adjustment:**
- Pay too much for call
- Receive too little for put
- **Overpay for synthetic**

**Correct approach:**

**Adjust for dividends:**

$$
\text{Synthetic Cost} = C - P \approx S - PV(\text{Divs}) - K e^{-rT}
$$

**Check:**
- Dividend amount
- Ex-dividend date
- Adjust pricing expectations
- **Fair value**

### 6. Mistake #6

**The error:**

- $100k account
- Enter 50 SPY synthetics
- Notional: 50 × $45k = $2.25M
- Leverage: 22.5×
- **Insane leverage!**

**What happens:**

**SPY drops 5%:**
- Loss: $2.25M × 0.05 = $112,500
- Account: Wiped out
- Margin call: $12,500
- **Bankruptcy**

**Correct approach:**

**Maximum leverage:**

$$
\text{Notional} \leq 3\times \text{ Account Size}
$$

For $100k:
- Max notional: $300k
- SPY synthetics: 6-7 max
- **Manageable risk**

### 7. Mistake #7

**The error:**

- Backtest synthetic strategy
- Assume $0 costs
- "I can make 20% annually!"
- **Unrealistic**

**Reality:**

**Per synthetic (entry):**
- Buy call: $0.65 commission
- Sell put: $0.65 commission
- Slippage: $10-20
- Total: ~$12

**Per synthetic (exit):**
- Same costs: ~$12

**Round-trip: $24**

**Annual (rolling 4×):**
- 4 × $24 = $96 per synthetic
- 10 synthetics: $960
- On $100k: 0.96% annual drag
- **Returns: 20% → 19.04%**

**Correct approach:**

**Model costs in backtest:**
- Commissions
- Slippage estimate
- Realistic net returns
- **Conservative projections**

### 8. Mistake #8

**The error:**

- Synthetic at $450
- SPY closes exactly at $450.00 Friday
- Walk away for weekend
- **Uncertainty**

**What happens:**

**Pin risk:**
- Stock exactly at strike
- Call: Borderline ITM/OTM
- Put: Borderline ITM/OTM
- Auto-exercise threshold: $0.01
- **Uncertain outcome**

**Possible scenarios:**
1. Both expire worthless (if $449.99)
2. Call exercises only (if $450.01)
3. Put assigned only (unlikely)
4. Both happen (if $450.00)
- **Unknown until Monday**

**Monday surprise:**
- May have stock position
- May have nothing
- Weekend gap risk
- **Uncontrolled**

**Correct approach:**

$$
\text{If within } \$1 \text{ of strike at 3:00 PM Friday} \Rightarrow \text{Close position}
$$

**Avoid pin risk entirely**

### 9. Mistake #9

**The error:**

- Approved for portfolio margin
- Think: "Infinite leverage!"
- Overuse it
- **Disaster risk**

**What happens:**

**Portfolio margin is dynamic:**
- Based on market risk
- Increases during volatility
- Can spike unexpectedly
- **Margin call risk**

**Example:**

**Normal times:**
- 20 SPY synthetics
- Margin: $60k

**VIX spikes to 40:**
- Same 20 synthetics
- Margin: $150k (2.5× higher!)
- Account value: $90k
- **Margin call: $60k**

**Correct approach:**

**Use portfolio margin conservatively:**
- Keep 50% cash buffer
- Monitor margin usage daily
- Reduce positions proactively in vol
- **Safety margin**

### 10. Mistake #10

**The error:**

- Own TSLA stock at $300
- TSLA now $250
- Sell stock (realize $5k tax loss)
- Immediately enter TSLA synthetic
- **Wash sale!**

**What happens:**

**Wash sale rule:**
- Can't claim loss if buy "substantially identical" within 30 days
- Synthetic = substantially identical
- Loss disallowed
- **Tax benefit lost**

**Correct approach:**

**Wait 31 days:**
- Sell stock today
- Wait 31 days
- Then enter synthetic
- **Loss allowed**

**Or use correlated security:**
- Sell TSLA
- Buy TSLA synthetic using DIFFERENT strikes
- Arguable not "substantially identical"
- **Consult tax advisor**

---

## Best Case Scenario

### 1. The Perfect Arbitrage (Box Spread)

**Trader profile:**

- Experience: 15 years options
- Account: $2,000,000
- Strategy: Box spread arbitrage
- Skills: Mispricing detection
- Tools: Real-time pricing scanners

**Setup (October 2023):**

**SPY pricing anomaly detected:**

**Box spread (450-460):**

**Long synthetic at 450:**
- Buy 450 call (30 DTE): $15.40
- Sell 450 put (30 DTE): $5.20
- Net: $10.20 debit

**Short synthetic at 460:**
- Sell 460 call: $7.50
- Buy 460 put: $16.90
- Net: $9.40 credit

**Combined:**
- Net credit received: $9.40 - $10.20 = -$0.80 debit
- Spread width: $10.00
- **Locked in $10.00 payoff at expiration**

**Implied return:**

$$
\text{Return} = \frac{10.00 - 0.80}{0.80} = 11.50
$$

**Over 30 days:**

$$
\text{Annualized} = 11.50 \times \frac{365}{30} = 140\%
$$

**Wait, this seems like an arbitrage! Let me recalculate more carefully.**

**Actually, the box spread should be:**

Received: $10 - $0.80 = $9.20 today
Owe: $10 at expiration

**Implied borrowing rate:**

$$
\text{Rate} = \frac{10.00 - 9.20}{9.20} \times \frac{365}{30} = 10.6\% \text{ annually}
$$

**If risk-free rate = 5%:**

**Arbitrage:**
- Execute box spread (borrow at 10.6%)
- Lend at risk-free (5%)
- **Wait... that's backwards!**

**Let me reconsider. If PAYING $0.80 and receiving $10 later:**

**Lending rate:**

$$
\text{Rate} = \frac{10.00 - 0.80}{0.80} \times \frac{365}{30} = 140\% \text{ (impossible!)}
$$

**More realistic scenario:**

**Received $9.85 today (net credit):**
- Long 450 synthetic: -$10.10
- Short 460 synthetic: +$9.95
- Net: -$0.15 debit

Hmm, let me construct a realistic arbitrage example:

**Realistic box spread arbitrage:**

**Market mispricing:**
- Box should trade at: $10.00 - PV($10)
- PV($10, 30 days, 5%) = $10 × e^(-0.05 × 30/365) = $9.959
- Fair cost: $0.041

**But market prices:**
- Actual cost: -$0.10 (net credit!)
- **Arbitrage: Receive $0.10 now, pay $10 later**

**Execution:**

**Entered 200 box spreads:**
- Received: 200 × $0.10 × 100 = $2,000 credit
- Locked liability: $10 × 100 × 200 = $200,000 in 30 days
- **Implied borrowing rate: negative!**

**30 days later:**

**Settlement:**
- Owe $200,000
- Had $2,000 + invested @ 5% for month
- Interest earned: $2,000 × (1 + 0.05/12) = $2,008
- Net cost: $200,000 - $2,008 = $197,992
- **Effectively borrowed $200k for $197,992 = profit $8**

**Wait, that's tiny. Let me recalculate the actual arbitrage:**

**If box gives NET CREDIT of $100 per spread:**
- Receive: $100 × 200 = $20,000 today
- Owe: $10 spread × 100 × 200 = $200,000 in 30 days

**Can invest $20k @ 5%:**
- Month later: $20,000 × (1.0041) = $20,082

**But owe $200k:**
- Need to come up with: $179,918
- **Not pure arbitrage, needs capital**

**True arbitrage would be if net credit ≥ PV(spread width):**

This is getting complex. Let me use a simpler, realistic scenario:

**Perfect synthetic construction (non-arbitrage but optimal):**

The trader instead uses synthetics for leveraged long exposure during a bull run, perfectly managing positions.

### 2. The Perfect Bull Run Trade (Realistic)

**Setup (January 2023):**

**Bullish on SPY recovery:**
- SPY: $380 (after 2022 bear market)
- View: Rally to $450 by year-end
- Strategy: Synthetic longs for leverage

**Position:**
- 50 SPY synthetics at $380
- Buy 380 calls (12-month LEAPS): $35
- Sell 380 puts (12-month): $33
- Net: $2 debit per synthetic
- Total: $2 × 50 × 100 = $10,000
- Margin (portfolio): $380 × 50 × 100 × 0.15 = $285,000
- **Notional exposure: $1.9M on $295k capital (6.4× leverage)**

**One-year progression:**

**Q1 2023: Rally begins**
- SPY: $380 → $410 (+7.9%)
- Synthetics: $10k cost basis + $30 gain = $40 profit/synthetic
- Portfolio: +$200,000
- **Unrealized: +68% on capital**

**Q2-Q3: Continued strength**
- SPY: $410 → $440 (+7.3%)
- Additional gain: $30/synthetic
- Portfolio: +$350,000 cumulative
- **Unrealized: +119%**

**Q4: Year-end rally**
- SPY: $440 → $465 (+5.7%)
- Final gain: $25/synthetic
- Total: $85/synthetic

**Final P&L:**

$$
\text{Profit} = (\$465 - \$380 - \$2) \times 50 \times 100 = \$415,000
$$

$$
\text{Return} = \frac{\$415,000}{\$295,000} = 141\%
$$

**vs buying stock:**
- $295k in SPY @ $380
- Sold @ $465
- Profit: $295k × (465/380 - 1) = $66,000
- Return: 22.4%
- **Synthetic provided 6.3× leverage advantage**

**Why this worked perfectly:**

1. ✅ Correct directional call (bull market)
2. ✅ 12-month timeframe (avoided rolls)
3. ✅ Portfolio margin efficiency
4. ✅ Closed before expiration (avoided assignment)
5. ✅ No early exercise (OTM throughout)
6. ✅ Low volatility (tight spreads)
7. ✅ Patient execution
8. **Professional implementation**

---

## Worst Case Scenario

### 1. The Margin Call Disaster

**Trader profile:**

- Experience: 2 years
- Account: $300,000
- Strategy: Over-leveraged synthetics
- Margin: Reg-T (not portfolio margin)
- Discipline: Poor

**Setup (September 2024):**

**Aggressively bullish:**
- SPY: $550
- View: "Markets only go up"
- Strategy: Maximum leverage
- **Overconfident**

**Position (reckless):**

**100 SPY synthetics at $550:**
- Buy 550 calls: $18
- Sell 550 puts: $17
- Net: $1 debit
- Cost: $1 × 100 × 100 = $10,000

**Margin (Reg-T):**
- Per put: $550 × 100 = $55,000
- Total: 100 × $55,000 = $5.5M
- **WAIT, can't have $5.5M margin on $300k account!**

**Let me recalculate realistically:**

With $300k and Reg-T margin of $55k per synthetic:
- Max synthetics: $300k / $55k = 5.45 ≈ 5 synthetics
- **Way overleveraged even at 5**

**Actually entered: 5 synthetics (used full account as margin)**

**Better calculation with portfolio margin:**

If had portfolio margin (15%):
- Margin per synthetic: $550 × 100 × 0.15 = $8,250
- Max with $300k: $300k / $8,250 = 36 synthetics
- **Trader entered 30 (83% of max)**

**Position:**
- 30 SPY synthetics @ $550
- Margin: $247,500 (portfolio margin)
- Remaining cash: $52,500
- Notional: $1.65M (5.5× leverage)
- **Extremely leveraged**

**The crash (October 2024):**

**Week 1:**
- Surprise recession warning
- SPY gaps down: $550 → $520 (-5.5%)
- Synthetics: -$30 each
- Loss: 30 × $30 × 100 = -$90,000
- Account: $300k → $210k
- **Down 30%**

**Week 2:**
- Panic selling continues
- SPY: $520 → $480 (-7.7%)
- Additional loss: $40 each
- Total: 30 × $70 × 100 = -$210,000
- Account: Would be $90k but margin call hits
- **Margin call: $60k**

**Forced liquidation:**

**Can't meet margin call:**
- Needs $60k immediately
- Only has $52k cash
- Broker liquidates positions
- **Worst possible timing**

**Liquidation pricing (bid-ask crisis):**
- Normal: Buy back 550 puts @ mid
- Crisis: Buy back @ ask (inflated)
- Slippage: $3-5 per contract
- **Exit at 30 × $75 loss = $225k**

**Final account:**

$$
\text{Remaining} = \$300,000 - \$225,000 = \$75,000
$$

**Loss: -75% in 2 weeks**

**What went catastrophically wrong:**

1. ❌ Over-leveraged (used 83% of max margin)
2. ❌ No cash buffer (only $52k reserve)
3. ❌ Concentrated (all SPY, no diversification)
4. ❌ Ignored market signals (recession warning)
5. ❌ No stop loss
6. ❌ Portfolio margin risk misunderstood
7. ❌ Couldn't meet margin call
8. ❌ Forced liquidation at worst prices
9. **Complete discipline failure**

**If had been conservative:**

**Better approach:**
- 10 synthetics (not 30)
- Margin: $82,500
- Cash buffer: $217,500
- Same decline: -$70k
- **Account: $230k (still painful but survivable)**

---

## What to Remember

### 1. Core Concept

**Synthetic forwards replicate futures using options:**

$$
\text{Long Call} + \text{Short Put} = \text{Long Forward}
$$

$$
\text{Short Call} + \text{Long Put} = \text{Short Forward}
$$

- Put-call parity ensures equivalence
- Delta = ±1.0 (identical to futures)
- Gamma = 0, Vega = 0, Theta ≈ 0
- **Perfect mathematical replication**

### 2. Put-Call Parity

**Foundation:**

$$
C - P = S_0 - K e^{-rT}
$$

- Arbitrage-enforced relationship
- Links calls, puts, stock, bonds
- Violations = arbitrage opportunities
- **No-arbitrage condition**

### 3. Construction Methods

**Synthetic long:**
- Buy call at K
- Sell put at K
- Net ≈ $0 (near ATM)
- **Bullish exposure**

**Synthetic short:**
- Sell call at K
- Buy put at K
- Net ≈ $0
- **Bearish exposure**

### 4. When to Use

**Ideal conditions:**
- Futures unavailable (individual stocks)
- Portfolio margin available (capital efficiency)
- Volatility skew exploitable (pricing advantage)
- Tax optimization needs (long-term gains)
- Dividend capture opportunities

### 5. When NOT to Use

**Avoid:**
- Liquid futures available (simpler)
- Options illiquid (OI < 500)
- Near expiration (< 14 DTE)
- High dividend stocks (assignment risk)
- Reg-T margin only (capital inefficient)
- Cannot monitor positions

### 6. Risk Management

**Position sizing:**

$$
\text{Max Notional} = 3\times \text{ Account Size}
$$

**Margin:**
- Portfolio margin: 15-25% of notional
- Reg-T: 100% of strike (inefficient)
- Keep 50% cash buffer

**Diversification:**
- Spread across 5+ underlyings
- Different sectors
- Uncorrelated positions

**Stops:**
- Price stop: 10% adverse move
- Time stop: Roll 7 days before expiry
- Dividend stop: Close before ex-div if deep ITM

### 7. Common Mistakes

1. Ignoring early exercise risk
2. Using illiquid options (OI < 500)
3. Wrong strike selection (must match!)
4. Holding through expiration
5. Ignoring dividends
6. Over-leveraging (>3× account)
7. Forgetting transaction costs
8. Pin risk ignorance
9. Portfolio margin misunderstanding
10. Tax wash sale violations

### 8. Maximum Profit and Loss

**Synthetic long:**
- Max profit: Unlimited (stock → ∞)
- Max loss: Strike price (stock → 0)
- Breakeven: K + net debit

**Synthetic short:**
- Max profit: Strike price (stock → 0)
- Max loss: Unlimited (stock → ∞)
- Breakeven: K - net credit

**Returns:**
- Leverage: 3-6× typical
- Risk identical to futures
- Capital efficiency advantage

### 9. Success Factors

**Three pillars:**

1. **Liquidity** (OI > 1,000, tight spreads)
2. **Margin management** (portfolio margin, 50% buffer)
3. **Timing** (roll 7 days before expiry)

**Formula:**

$$
\text{Success} = \text{Liquidity} \times \text{Capital Efficiency} \times \text{Risk Management}
$$

### 10. Final Wisdom

> "Synthetic forwards are the purest expression of put-call parity in action—mathematically equivalent to futures but constructed from options, offering tactical advantages in capital efficiency, market access, and arbitrage exploitation. The beauty is in the simplicity: long call + short put = perfect directional exposure with zero gamma, zero vega, and near-zero theta. But simplicity requires discipline: match strikes exactly, maintain adequate margin buffers, roll before expiration, monitor early exercise risk, and respect the leverage you're deploying. Synthetics excel when futures are unavailable (individual stocks), when portfolio margin creates capital efficiency (15% vs 100% Reg-T), or when volatility skew provides pricing advantages. But they're unnecessary complexity when liquid futures exist. Use synthetics as a precision tool for specific situations, not as a default approach. Master put-call parity, understand margin dynamics, and manage the operational details—early exercise, pin risk, dividend adjustments. The strategy is mathematically perfect; execution determines success."

**Most important principles:**

- Synthetics = futures via put-call parity (mathematically identical)
- Delta ±1.0, Gamma 0, Vega 0, Theta ≈0 (linear replication)
- Portfolio margin provides capital efficiency (15-25% vs 100%)
- Strikes must match (call K = put K)
- Roll 7 days before expiry (avoid assignment/pin risk)
- Monitor early exercise (deep ITM + dividends)
- Maximum leverage 3× account size (safety)
- Use when futures unavailable or margin advantage

**Why this works:**

- Put-call parity arbitrage-enforced (violations corrected)
- Options combine to eliminate gamma/vega
- Portfolio margin recognizes offsetting risk
- Tax efficiency for long-term positions
- **Mathematical equivalence guaranteed**

**But remember:**

- Early exercise disrupts position
- Pin risk at expiration (close early)
- Dividends complicate pricing
- Transaction costs add up
- Margin can spike in volatility
- Operational complexity vs futures
- **Precision tool, not default approach**

**Use synthetics when they provide clear advantages, avoid when futures are simpler. Respect the leverage, manage the details, master the math. 🔄⚖️**
