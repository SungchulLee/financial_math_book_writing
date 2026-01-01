# Variance Swaps

**Variance swaps** are derivatives that provide pure, direct exposure to realized variance, allowing you to bet on volatility without the complications of delta hedging, gamma scalping, or theta decay.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/variance_swaps_calculation.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 1:** Variance Swaps Calculation visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/variance_swaps_convexity.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 2:** Variance Swaps Convexity visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/variance_swaps_payoff.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 3:** Variance Swaps Payoff visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/variance_swaps_vol_variance.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 4:** Variance Swaps Vol Variance visualization.

---

## The Core Insight

**The fundamental idea:**

- All previous strategies (gamma scalping, vega trading) trade volatility indirectly through options
- They require constant delta hedging, have theta decay, transaction costs
- Variance swaps trade volatility DIRECTLY
- You simply bet: "Realized variance will be X"
- Clean, pure, elegant exposure

**The key equation:**

$$
\text{Payoff} = \text{Notional} \times (\sigma_{\text{realized}}^2 - K_{\text{var}})
$$

**You're essentially betting: "The stock will realize more (or less) variance than the strike."**

---

## What Is Variance?

**Before understanding variance swaps, we need to understand variance:**

### Variance vs. Volatility

**Volatility** is what we usually talk about:

- Standard deviation of returns
- Measured in % (e.g., "30% volatility")
- Square root of variance

**Variance** is volatility squared:

$$
\text{Variance} = \text{Volatility}^2
$$

**Example:**

- Volatility = 30% = 0.30
- Variance = (0.30)² = 0.09 = 9%

**Why trade variance instead of volatility?**

- **Mathematical convenience:** Variance is additive, volatility is not
- **Cleaner replication:** Options naturally replicate variance
- **No square root:** Easier to work with mathematically

### Realized Variance

**How to calculate realized variance:**

For a period with $n$ daily returns $r_1, r_2, ..., r_n$:

$$
\sigma_{\text{realized}}^2 = \frac{252}{n} \sum_{i=1}^{n} r_i^2
$$

**In plain English:**

1. Calculate daily returns
2. Square each return
3. Add them up
4. Annualize (multiply by 252 trading days)

**Example:**

Day 1: Stock moves +2% → $r_1^2 = (0.02)^2 = 0.0004$
Day 2: Stock moves -1.5% → $r_2^2 = (0.015)^2 = 0.000225$
Day 3: Stock moves +1% → $r_3^2 = (0.01)^2 = 0.0001$
...
Sum over 60 days, multiply by 252/60 = 4.2

**Key insight:** Variance is always positive (you square the returns). Big moves contribute more (quadratically).

---

## What Is a Variance Swap?

**A variance swap is a forward contract on realized variance:**

### The Contract Terms

**Buyer agrees to:**

- Pay a fixed amount: **Variance Strike** ($K_{\text{var}}$)
- Receive a variable amount: **Realized Variance** ($\sigma_{\text{realized}}^2$)

**At maturity (typically 1-3 months):**

$$
\boxed{\text{Payoff} = \text{Notional} \times (\sigma_{\text{realized}}^2 - K_{\text{var}})}
$$

**Example Contract:**

- Notional: $1,000,000
- Variance Strike: 0.09 (equivalent to 30% volatility)
- Maturity: 3 months

**Scenario 1: High Realized Variance**

- Realized variance: 0.16 (40% volatility)
- Payoff: $1,000,000 × (0.16 - 0.09) = **+$70,000**
- You profit! Stock was more volatile than expected

**Scenario 2: Low Realized Variance**

- Realized variance: 0.04 (20% volatility)
- Payoff: $1,000,000 × (0.04 - 0.09) = **-$50,000**
- You lose! Stock was less volatile than expected

**Simple, clean, direct.**

---

## Variance Swaps vs. Volatility Swaps

**There's also a related instrument: volatility swaps**

### Variance Swap Payoff

$$
\text{Payoff} = \text{Notional}_{\text{var}} \times (\sigma_{\text{realized}}^2 - K_{\text{var}})
$$

- Linear in variance
- Direct measurement
- More common in the market

### Volatility Swap Payoff

$$
\text{Payoff} = \text{Notional}_{\text{vol}} \times (\sigma_{\text{realized}} - K_{\text{vol}})
$$

- Linear in volatility
- Need to take square root
- Less common (harder to hedge)

**In this document, we focus on variance swaps as they are more standard.**

### Why Variance Instead of Volatility?

**Mathematical reasons:**

1. **Variance is additive:**

         - Daily variances add up to total variance
         - Makes replication clean
   
2. **Options replicate variance naturally:**

         - Portfolio of options = variance exposure
         - No square root complications

3. **Convexity:**

         - Variance swap is naturally long convexity
         - Large moves contribute disproportionately

**Practical reason:**

- Variance swaps are more liquid
- Market standard
- Easier to price and hedge

---

## The Beautiful Simplicity

**Compare variance swaps to gamma scalping:**

### Gamma Scalping (Complex)

**What you do:**

1. Buy options (pay premium)
2. Delta hedge (short stock)
3. Rebalance constantly (transaction costs)
4. Track gamma P&L: $\frac{1}{2}\Gamma(\delta S)^2$
5. Pay theta decay every day
6. Hope realized variance > implied variance (after costs)

**Complications:**

- Discrete rebalancing → tracking error
- Transaction costs → eat into profits
- Theta decay → constant cost
- Need to actively manage
- Model-dependent

**P&L:**

$$
\delta \Pi \approx \frac{1}{2}\Gamma(\delta S)^2 - \theta\,\delta t - \text{transaction costs}
$$

### Variance Swap (Simple)

**What you do:**

1. Enter variance swap contract
2. Wait
3. Realized variance is calculated
4. Receive payoff

**That's it!**

**Complications:**

- None
- No hedging
- No transaction costs
- No theta
- No rebalancing

**P&L:**

$$
\text{Payoff} = \text{Notional} \times (\sigma_{\text{realized}}^2 - K_{\text{var}})
$$

**This is the theoretical limit of gamma scalping - pure variance exposure without all the friction!**

---

## The Connection to Gamma Scalping

**This is profound:**

### Gamma Scalping Converges to Variance Swap

**In the theoretical limit:**

- Continuous rebalancing (no discrete tracking error)
- Zero transaction costs
- Infinite liquidity

**The gamma scalping P&L becomes:**

$$
\lim_{\delta t \to 0} \sum \frac{1}{2}\Gamma(\delta S)^2 = \text{Notional} \times \sigma_{\text{realized}}^2
$$

**This is exactly the variance swap payoff!**

**So:**

- **Variance swap** = What gamma scalping wants to be
- **Gamma scalping** = Imperfect replication of variance swap

**The relationship:**

```
Gamma Scalping          Variance Swap
(Imperfect, Costly)  →  (Perfect, Clean)
     ↓                       ↓
Actual realized var    Pure realized var
minus costs            exposure
```

### Why This Matters

**Understanding:**

- Variance swaps are the "Platonic ideal" of volatility trading
- Gamma scalping is the practical implementation
- The difference is friction (costs, theta, tracking error)

**In practice:**

- If variance swaps available → cleaner exposure
- If not → gamma scalping is approximation
- Market makers hedge variance swaps via gamma scalping!

---

## How Variance Swaps Are Priced

**The variance strike is set at inception to make the contract fair value (zero cost to enter):**

### Pricing Formula

$$
K_{\text{var}} = \text{Expected Realized Variance under risk-neutral measure}
$$

**In practice:**

$$
K_{\text{var}} \approx \frac{2}{T} \int_0^{\infty} \frac{C(K) + P(K)}{K^2} dK
$$

where:

- $T$ = Time to maturity
- $C(K)$ = Call option price at strike $K$
- $P(K)$ = Put option price at strike $K$

**In plain English:**

- Take all call and put options (across all strikes)
- Weight by $1/K^2$
- Integrate (sum) them up
- This portfolio replicates realized variance!

**Key insight:** A portfolio of options across all strikes perfectly replicates variance.

### Practical Pricing

**Market makers use:**

1. Liquid option prices (nearby strikes)
2. Implied volatility surface
3. Approximate the integral with a sum

**Example:**

- Stock at $100
- Options imply 30% volatility
- Variance strike ≈ (0.30)² = 0.09

**The strike is set at "fair value" based on current option prices.**

---

## Replication: How Market Makers Hedge

**When a market maker sells you a variance swap, how do they hedge?**

### The Log Contract

**Theoretical replication:**

A portfolio of options weighted by $1/K^2$ replicates variance:

$$
\text{Variance Payoff} = \frac{2}{T} \left[\int_0^S \frac{P(K)}{K^2}dK + \int_S^{\infty} \frac{C(K)}{K^2}dK\right]
$$

**In practice:**

1. Buy a strip of out-of-the-money puts (strikes below spot)
2. Buy a strip of out-of-the-money calls (strikes above spot)
3. Weight each by $1/K^2$
4. Delta hedge the portfolio

**This creates a "log contract" that replicates variance.**

### Dynamic Hedging

**Alternative (used by most dealers):**

- Gamma scalping!
- Continuously delta hedge a dynamically-adjusted option portfolio
- Accumulate realized variance through rebalancing

**So market makers hedge variance swaps via gamma scalping:**

- You want clean variance exposure → buy variance swap
- Dealer provides it → hedges with gamma scalping
- You avoid the complexity → dealer takes it on (for a spread)

**Circle complete:**

- Variance swap = clean exposure
- Gamma scalping = replication method
- Market maker bridges the gap

---

## Long Variance vs. Short Variance

### Long Variance (Buy Variance Swap)

**Position:**

- Pay fixed variance strike
- Receive realized variance

**Payoff:**

$$
\text{Payoff} = \text{Notional} \times (\sigma_{\text{realized}}^2 - K_{\text{var}})
$$

**You profit when:**

- Realized variance > Strike
- Stock moves around more than expected
- "Long volatility"

**When to use:**

- Believe market is complacent
- Expect volatility spike
- Before events (earnings, elections)
- Similar motivation to buying options/gamma scalping

**Example:**

- VIX at 12 (historically low)
- You expect volatility to spike
- Buy variance swap at strike 0.0144 (12% vol)
- Market realizes 20% vol = 0.04 variance
- Profit: Notional × (0.04 - 0.0144)

### Short Variance (Sell Variance Swap)

**Position:**

- Receive fixed variance strike
- Pay realized variance

**Payoff:**

$$
\text{Payoff} = \text{Notional} \times (K_{\text{var}} - \sigma_{\text{realized}}^2)
$$

**You profit when:**

- Realized variance < Strike
- Stock is calmer than expected
- "Short volatility"

**When to use:**

- Believe market is too fearful
- Expect volatility to decline
- After crises (vol crush)
- Similar motivation to selling options

**Example:**

- VIX at 40 (crisis levels)
- You expect volatility to calm
- Sell variance swap at strike 0.16 (40% vol)
- Market realizes 25% vol = 0.0625 variance
- Profit: Notional × (0.16 - 0.0625)

---

## Concrete Example: Full Trade Lifecycle

**Let's walk through a complete variance swap trade:**

### Setup

- **Date:** January 1
- **Stock:** SPY (S&P 500 ETF)
- **Current price:** $400
- **Implied volatility:** 20%

**Your view:** "The market is too complacent. Volatility will be higher than 20%."

**The trade:**

- Buy 3-month variance swap
- Variance strike: 0.04 (20% volatility squared)
- Notional: $1,000,000
- Maturity: April 1 (60 trading days)

### During the Contract

**The stock moves over 60 days:**

- Some days up 2%, some days down 1.5%
- Some big moves: +3%, -2.5%
- Some quiet days: +0.1%, -0.2%

**You don't do anything:**

- No trading
- No hedging  
- No rebalancing
- Just wait

**Daily variance accumulates automatically:**

$$
\text{Daily contribution} = r_i^2
$$

### At Maturity (April 1)

**Calculation of realized variance:**

$$
\sigma_{\text{realized}}^2 = \frac{252}{60} \sum_{i=1}^{60} r_i^2
$$

**Example calculation:**

- Sum of squared returns: 0.015
- Annualized: 0.015 × (252/60) = 0.063

**Realized volatility:**

$$
\sigma_{\text{realized}} = \sqrt{0.063} = 25.1\%
$$

**Your payoff:**

$$
\text{Payoff} = 1,000,000 \times (0.063 - 0.04) = 1,000,000 \times 0.023 = \$23,000
$$

**You made $23,000 because:**

- Strike: 20% vol (0.04 variance)
- Realized: 25.1% vol (0.063 variance)
- Difference: 5.1% vol (0.023 variance)
- **You were right! Volatility was higher than market expected.**

### What If You Were Wrong?

**If realized volatility was 15%:**

- Realized variance: 0.0225
- Payoff: $1,000,000 × (0.0225 - 0.04) = **-$17,500**
- You lose because volatility was lower than expected

**Simple, clean, transparent.**

---

## Variance Swaps vs. All Other Strategies

**Let's put variance swaps in context:**

| Strategy | Instrument | Primary Exposure | Need Hedging? | Transaction Costs | Theta | Complexity |
|----------|-----------|------------------|---------------|-------------------|-------|------------|
| **Delta Hedging** | Options | None (hedged) | Yes (constant) | High | Yes | Medium |
| **Gamma Scalping** | Options | Realized vol | Yes (constant) | High | Yes | Medium |
| **Vega Trading** | Options | Implied vol | Yes (periodic) | Medium | Yes | Medium |
| **Dispersion** | Options (many) | Correlation | Yes (all assets) | Very High | Yes | Very High |
| **Convertible Arb** | Converts + Stock | Multi-factor | Yes (constant) | High | Some | Very High |
| **Variance Swaps** | Variance swap | Realized variance | NO | None | None | **Low** |

**The key differences:**

### Variance Swaps vs. Gamma Scalping

| Aspect | Gamma Scalping | Variance Swap |
|--------|---------------|---------------|
| **Instrument** | Options | OTC derivative |
| **Hedging** | Required constantly | Not required |
| **Transaction costs** | Significant | Zero |
| **Theta** | Pay every day | None |
| **Rebalancing** | Manual/automated | Automatic |
| **Tracking error** | Yes (discrete hedging) | No (perfect) |
| **P&L formula** | $\frac{1}{2}\Gamma(\delta S)^2 - \theta - \text{costs}$ | $\text{Notional} \times (\sigma_r^2 - K)$ |
| **Complexity** | High | Low |
| **Accessibility** | Retail possible | Institutional only |
| **Result** | Approximate variance | Pure variance |

**Variance swap is what gamma scalping wants to be - pure, frictionless variance exposure!**

### Variance Swaps vs. Vega Trading

| Aspect | Vega Trading | Variance Swap |
|--------|-------------|---------------|
| **What you trade** | IMPLIED volatility changes | REALIZED variance |
| **P&L source** | Market expectation changes | Actual stock movement |
| **Time horizon** | Can be days | Must wait to maturity |
| **Early exit** | Can close position | Must hold or exit at market price |
| **Theta** | Yes (costs or earns) | No |

**Different bets:**

- Vega: "Market's expectation will change"
- Variance swap: "Actual variance will be X"

---

## The Variance Risk Premium

**Important empirical fact:**

### Historical Observation

**Over long periods:**

$$
\text{Implied Variance} > \text{Realized Variance}
$$

**In other words:**

- Variance strikes (implied variance) are typically higher than realized variance
- Short variance swaps have positive expected return on average
- This is the "variance risk premium"

**Why does this exist?**

1. **Risk aversion:**

         - Investors pay premium for volatility protection
         - Willing to overpay for hedges
         - Similar to insurance premium

2. **Crash fear:**

         - Market fears left-tail events
         - Prices in more volatility than usually occurs
         - Premium for jump risk

3. **Hedging demand:**

         - Institutions need volatility hedges
         - Buy variance swaps/options for protection
         - Demand drives up price

4. **Behavioral bias:**

         - People overestimate volatility
         - Loss aversion
         - Recency bias

**The result:**

- Short variance swaps earn premium on average
- Like selling insurance
- But with tail risk (crashes)

**Historical data:**

- S&P 500 variance risk premium: ~3-5% annualized
- Varies by market conditions
- Higher in bull markets, lower in crises

---

## Pros and Cons

### Advantages ✓

**1. Pure variance exposure**

- Direct bet on realized variance
- No gamma, theta, delta complications
- Exactly what you want

**2. No transaction costs**

- No rebalancing needed
- No bid-ask spreads on hedges
- No borrow costs
- Pure P&L

**3. No theta decay**

- Options lose value daily (theta)
- Variance swaps have no time decay
- No carrying cost

**4. No hedging required**

- Set it and forget it
- No constant monitoring
- No execution risk

**5. Perfect replication of variance**

- No tracking error
- Continuous equivalent (no discretization)
- Mathematical purity

**6. Structural edge (variance risk premium)**

- Short variance historically profitable
- Similar to selling insurance
- Quantifiable expected return

**7. Operationally simple**

- Enter contract
- Wait
- Settle
- That's it

**8. Theoretical elegance**

- Clean mathematical properties
- Variance is additive
- Easy to understand payoff

### Disadvantages ✗

**1. Institutional access only**

- OTC market
- Need large capital
- Prime broker relationships
- Not for retail investors
- Minimum notionals (typically $1M+)

**2. Counterparty risk**

- Bilateral contract
- Dealer might default
- Need credit management
- Not exchange-cleared (usually)

**3. Illiquid**

- Can't easily exit mid-trade
- Wide bid-ask spreads if you want out
- Stuck until maturity
- Market price can be adverse

**4. Mark-to-market volatility**

- Value fluctuates with implied variance
- Can show large unrealized losses
- Need to manage margin
- Accounting issues

**5. No optionality**

- Linear payoff (unlike options)
- Unlimited loss potential (if short)
- No protection from extremes

**6. Convexity risk (short variance)**

- Large moves hurt disproportionately
- Variance is squared (convex)
- Tail risk significant
- Can lose multiples of premium

**7. Jump risk**

- Single large jump can dominate P&L
- Gap risk (overnight, weekends)
- Flash crashes
- Hard to hedge

**8. Less flexible than options**

- Can't customize strikes
- Can't do spreads
- Binary: long or short variance
- Limited structures

**9. Vega vs. variance basis risk**

- Variance swap ≠ vega swap
- Non-linear relationship
- Hedging one with other imperfect

---

## When Variance Swaps Work Best

### For Long Variance

**Favorable conditions:**

- **Low implied volatility** (VIX < 15)
- **Market complacency** (extended bull market)
- **Before known events** (elections, Fed meetings)
- **Building tensions** (geopolitical, economic)
- **Historical vol percentile low** (< 20th percentile)

**Catalysts:**

- Upcoming binary events
- Structural changes expected
- Market fragility increasing
- Low realized vol but high potential

**Example environments:**

- Late 2019 (pre-COVID)
- Mid-2007 (pre-financial crisis)
- Any "calm before the storm"

### For Short Variance

**Favorable conditions:**

- **High implied volatility** (VIX > 30)
- **Post-crisis environment** (fear elevated)
- **Volatility spike just occurred**
- **Mean reversion likely**
- **Historical vol percentile high** (> 80th percentile)

**Catalysts:**

- Crisis peaked
- Central bank intervention
- Worst-case scenarios priced in
- Volatility unsustainable at current levels

**Example environments:**

- April 2020 (post-COVID crash)
- Early 2009 (post-financial crisis trough)
- After any panic spike

### General Favorable Conditions

**For both directions:**

- Strong view on realized volatility
- Long time horizon (can wait out fluctuations)
- Sufficient capital
- Access to dealers
- Conviction in variance risk premium (for short)

**Unfavorable conditions:**

- Mid-range volatility (no strong view)
- Need liquidity (might have to exit early)
- Counterparty concerns
- Regulatory changes
- Market structure breaks

---

## Advanced: Variance Dispersion

**You can also trade dispersion with variance swaps!**

### The Structure

**Just like option dispersion, but with variance swaps:**

**Long Variance Dispersion:**

- Short index variance swap
- Long individual stock variance swaps (weighted)
- Bet: Stocks will move independently (low correlation)

**Short Variance Dispersion:**

- Long index variance swap
- Short individual stock variance swaps
- Bet: Stocks will move together (high correlation)

### Why It's Cleaner

**Advantages over option dispersion:**

- No gamma hedging required
- No theta decay
- No transaction costs
- Pure correlation exposure

**Same mathematical relationship:**

$$
\text{Index Variance} = \sum w_i^2 \cdot \text{Individual Variances} + \text{Correlation Terms}
$$

**But cleaner execution!**

---

## Practical Considerations

### Notional Selection

**Vega-notional conversion:**

A variance swap with notional $N_{\text{var}}$ has vega approximately:

$$
\text{Vega} \approx \frac{N_{\text{var}}}{2 \sigma_{\text{implied}}}
$$

**Example:**

- Want $10,000 vega (per 1% vol move)
- Implied vol = 20%
- Need notional: $N_{\text{var}} = 2 \times 0.20 \times 10,000 = $4,000,000

### Strike Setting

**Variance strike is typically set at:**

- Fair value based on option prices
- Slightly above realized vol (variance risk premium)
- Negotiated with dealer

**Example:**

- Implied vol: 22%
- Historical realized vol: 18%
- Variance strike might be set at 20% → 0.04

### Settlement

**Most variance swaps cash settle:**

- Calculate realized variance
- Compare to strike
- Cash payment exchanges hands
- No physical delivery

**Some have caps:**

- Maximum variance level (e.g., 2.5× strike)
- Protects seller from extreme moves
- Reduces premium for buyer

---

## Real-World Usage

### Hedge Funds

**Volatility arbitrage funds:**

- Core strategy: sell variance swaps
- Harvest variance risk premium
- Hedge with dynamic gamma scalping
- Systematic volatility strategies

**Examples:**

- Many "vol arb" funds
- Managed futures
- Relative value strategies

### Market Makers

**Dealers use for:**

- Hedge option positions
- Manage variance exposure
- Warehouse risk
- Provide liquidity

### Institutional Investors

**Uses:**

- Portfolio hedging (buy variance)
- Yield enhancement (sell variance)
- Volatility overlay strategies
- Tail risk hedging

**Example:**

- Pension fund worried about crash
- Buy variance swap as tail hedge
- Pays off if volatility spikes
- Cheaper than buying puts (no theta)

---

## Historical Examples

### 2008 Financial Crisis

**Pre-crisis (2007):**

- VIX at 15-20
- Short variance was popular
- "Great Moderation" mentality

**During crisis (late 2008):**

- VIX spiked to 80+
- Realized variance went to 0.64+ (80% vol)
- Short variance positions devastated
- Many funds blew up

**Lesson:** Tail risk in short variance is real and severe

### COVID-19 Crash (March 2020)

**Pre-crash (February 2020):**

- VIX at 15
- Market complacent

**During crash (March 2020):**

- VIX spiked to 80+
- Realized variance exploded
- Long variance highly profitable
- Short variance catastrophic

**Recovery (April-May 2020):**

- VIX declined to 30
- Short variance from high levels profitable
- Mean reversion

**Lesson:** Timing matters, volatility is cyclical

### Brexit (June 2016)

**Before vote:**

- Implied vol elevated (uncertainty)
- Realized vol moderate

**Vote result:**

- Large one-day move
- But then stabilization
- Realized variance lower than implied

**After:**

- Short variance profitable
- One-time event didn't sustain high vol

**Lesson:** Events can elevate implied vol beyond realized

---


---

## Worst Case Scenario

**What happens when everything goes wrong:**

### The Nightmare Setup

**How it starts:**
- [Unfavorable Greeks behavior]
- [Market moves against position]
- [Rebalancing losses mount]

**The deterioration:**

**Week 1:**
- [Early warning signs in Greeks]
- [Position losing value]
- [Rebalancing creating losses]
- [Critical decision point]

**Through expiration:**
- [Continued adverse Greeks dynamics]
- [Mounting hedge costs]
- [Maximum loss approached/realized]
- [Final outcome]

### Maximum Loss Calculation

**Worst case mathematics:**

$$
\text{Max Loss} = \text{Option Premium} + \text{Hedging Costs} + \text{Slippage}
$$

**Or for leveraged Greeks:**

$$
\text{Max Loss} = \text{Greeks Exposure} \times \text{Adverse Move} + \text{Transaction Costs}
$$

**Example calculation:**
- Position: [Specific position]
- Greeks exposure: [Delta, gamma, vega, theta]
- Adverse scenario: [What went wrong]
- Rebalancing costs: [Excessive]
- **Loss: [Calculation]**

### What Goes Wrong

The worst case occurs when:
1. **Wrong Greeks exposure:** Market behavior opposite to position
2. **Wrong volatility:** Realized vol doesn't materialize (or too much)
3. **Wrong timing:** Adverse moves happen quickly
4. **Wrong costs:** Transaction costs explode
5. **Wrong liquidity:** Cannot rebalance efficiently

### The Cascade Effect

**Multiple compounding failures:**

**Trade 1: Initial loss**
- [Setup and expectation]
- [What went wrong]
- [Loss amount]

**Trade 2: Revenge trading**
- [Doubling down]
- [Further losses]
- [Psychological damage]

**Trade 3: Account damage**
- [Desperation]
- [Major loss]
- [Recovery difficulty]

**Total damage:**
- Cumulative loss: [Amount]
- Portfolio impact: [Percentage]
- Time to recover: [Estimate]

### Greeks Blow-Up Scenarios

**Gamma blow-up:**
- [Large gap move]
- [Cannot rebalance]
- [Massive slippage]
- [Assignment risk]

**Vega collapse:**
- [IV crush]
- [Long vega position destroyed]
- [No recovery possible]

**Theta burn:**
- [No volatility materialized]
- [Time decay relentless]
- [Position expires worthless]

### Real Disasters

**Historical example 1:**
- [Specific event/strategy]
- [What happened to Greeks]
- [Final loss]
- [Lesson learned]

**Historical example 2:**
- [Specific event/strategy]
- [What happened to Greeks]
- [Final loss]
- [Lesson learned]

### Transaction Cost Death Spiral

**The problem:**
- Over-hedging/rebalancing
- Small price moves triggering rebalances
- Bid-ask spread eating profits
- Commission accumulation

**The math:**
- Expected Greeks P&L: $X
- Actual transaction costs: $Y > $X
- Net loss despite correct directional view

**Prevention:** Optimal rebalancing frequency, delta bands

### Psychology of Greeks Losses

**Emotional stages:**
1. **Confusion:** "My Greeks model says this should work"
2. **Denial:** "Just need volatility to pick up"
3. **Frustration:** "Transaction costs are killing me"
4. **Capitulation:** "Close everything"
5. **Learning:** "What did my Greeks analysis miss?"

**Winning trader mindset:**
- Greeks models are imperfect
- Accept losses in adverse scenarios
- Learn from Greeks attribution
- Improve risk management

### Preventing Worst Case

**Risk management strategies:**

1. **Position sizing by Greeks:**
   - Limit max delta exposure
   - Cap gamma concentration
   - Control vega risk
   - Monitor theta bleed

2. **Rebalancing discipline:**
   - Set delta bands
   - Consider transaction costs
   - Don't over-rebalance
   - Use algorithms if possible

3. **Diversification:**
   - Multiple Greeks exposures
   - Different underlyings
   - Various timeframes
   - Offsetting positions

4. **Liquidity requirements:**
   - Only trade liquid options
   - Ensure can exit/rebalance
   - Monitor volume and spreads
   - Have contingency plans

5. **Scenario analysis:**
   - Stress test all Greeks
   - Model extreme moves
   - Calculate worst-case costs
   - Plan exit strategies

### The Ultimate Protection

**Greeks risk limits:**

$$
\text{Max Delta} < \text{Limit}_\Delta
$$
$$
\text{Max Gamma} < \text{Limit}_\Gamma  
$$
$$
\text{Max Vega} < \text{Limit}_\nu
$$
$$
\text{Max Theta} < \text{Limit}_\theta
$$

Respect these limits religiously. A single Greeks blow-up can destroy months or years of careful P&L accumulation.

**Remember:** Greeks strategies amplify both gains and losses. The market WILL test your risk management. Proper position sizing and discipline determine survival.



---

## Best Case Scenario

**What happens when everything goes right:**

### The Perfect Setup

**Ideal entry conditions:**
- [Greeks favorably positioned]
- [Volatility at optimal level]
- [Market conditions supporting strategy]
- [Liquidity abundant]

**The optimal sequence:**

**Week 1:**
- [Initial Greeks behavior]
- [Favorable market moves]
- [Successful rebalancing]
- [P&L accumulation begins]

**Through position:**
- [Continued favorable Greeks dynamics]
- [Optimal rebalancing opportunities]
- [Greeks P&L exceeding costs]
- [Final profitable exit]

### Maximum Profit Achievement

**Best case mathematics:**

$$
\text{Max Profit} = \text{Greeks P\&L} - \text{Hedging Costs} - \text{Theta Decay}
$$

**Example calculation:**
- Position: [Specific position]
- Greeks exposure: [Delta, gamma, vega, theta]
- Market move: [Favorable scenario]
- Rebalancing: [Optimal frequency]
- **Profit: [Calculation]**

### What Makes It Perfect

The best case requires:
1. **Right Greeks setup:** Exposure matches market behavior
2. **Right volatility:** Realized matches expectations
3. **Right timing:** Greeks P&L accumulates quickly
4. **Right costs:** Transaction costs remain low
5. **Right liquidity:** Can rebalance efficiently

### Greeks P&L Breakdown

**Component analysis:**

**Delta P&L:**
- [How delta contributed]
- [Directional component]

**Gamma P&L:**
- [Rebalancing profits]
- [Convexity capture]

**Vega P&L:**
- [Volatility change impact]
- [IV expansion/contraction]

**Theta P&L:**
- [Time decay cost/benefit]
- [Carry component]

**Net P&L:** Sum of all Greeks components minus costs

### Comparison to Alternatives

**This strategy vs. [Alternative approach]:**
- [Greeks exposure comparison]
- [Cost-benefit analysis]
- [When this strategy wins]
- [Trade-offs involved]

### Professional Profit-Taking

**When to exit:**
- Greeks P&L target achieved
- Market conditions changing
- Transaction costs increasing
- Better opportunity elsewhere

**The compounding advantage:**

By taking profits and redeploying into new favorable Greeks setups, you can achieve better risk-adjusted returns than holding positions hoping for maximum theoretical profit.

### The Dream Scenario

**Extreme best case:**
- [Exceptional Greeks alignment]
- [Massive realized vol vs. low costs]
- [Multiple profitable rebalances]
- [Outsized P&L]

**Probability:** Rare but illustrates potential

**Key insight:** Best case demonstrates the strategy's maximum potential, but realistic expectations should be more modest. Position sizing should assume median outcomes, not best case.



---


---


---

## Economic Interpretation

**Understanding what variance swaps REALLY represent economically:**

### The Fundamental Economic Insight

Variance swaps exist because of a critical market insight:

$$
\text{Variance Swap} = \text{Pure Volatility Bet} - \text{All the Complications}
$$

**Traditional volatility trading (options):**
- Delta risk (must hedge)
- Gamma risk (must rebalance)
- Theta decay (time cost)
- Transaction costs (continuous)
- Path-dependent (how you get there matters)

**Variance swap:**
- Zero delta (market-neutral)
- No rebalancing needed
- No theta decay
- Zero transaction costs
- Path-independent (only endpoint matters)

$$
\boxed{\text{Variance Swap Payoff} = \text{Vega Notional} \times (\sigma_{\text{realized}}^2 - K_{\text{var}})}
$$

**Economic meaning:** You're buying/selling variance at a fixed strike, settling at realized variance. Pure volatility exposure.

### Why Variance Instead of Volatility?

**The mathematical economics:**

**Variance is additive:**

$$
\sigma_{T}^2 = \sigma_{T_1}^2 + \sigma_{T_2}^2 \quad \text{(can sum variances)}
$$

**Volatility is NOT additive:**

$$
\sigma_T \neq \sigma_{T_1} + \sigma_{T_2} \quad \text{(cannot sum volatilities)}
$$

**Economic implication:**
- Can decompose variance across time periods
- Can create variance strips (different maturities)
- Can build variance curves
- **Enables variance trading market**

**Variance has linear payoff in itself:**

$$
\text{Variance Swap P\&L} = \text{Notional} \times (\text{Realized Var} - \text{Strike Var})
$$

**Clean, linear, hedgeable.**

**Volatility swap would have nonlinear payoff:**

$$
\text{Vol Swap P\&L} = \text{Notional} \times (\sigma_{\text{realized}} - \sigma_{\text{strike}})
$$

But $\sigma = \sqrt{\text{Variance}}$ → **Nonlinear in underlying variance!**

**Harder to hedge, more complex pricing.**

### The Variance Risk Premium

**Critical market phenomenon:**

$$
\text{Variance Risk Premium (VRP)} = \text{Implied Variance} - \text{Realized Variance}
$$

**Empirical fact:** VRP is **persistently positive** (10-20% annually).

**Economic explanation:**

**Investors are willing to PAY for volatility protection:**
- Insurance against tail events
- Portfolio hedging demand
- Crisis aversion
- Fear of crashes

**Sellers (variance swap dealers) get compensated:**
- Negative skewness risk (crashes)
- Liquidity provision
- Balance sheet usage
- Model risk

**Historical data (S&P 500, 1990-2024):**

$$
\text{Average Implied Variance} = 0.045 \text{ (21.2\% vol)}
$$

$$
\text{Average Realized Variance} = 0.032 \text{ (17.9\% vol)}
$$

$$
\text{VRP} = 0.013 \text{ (3.3\% vol points annually)}
$$

**Economic insight:** Selling variance swaps harvests this premium (but takes crash risk).

### Variance Convexity and Jensen's Inequality

**Critical difference from vol swaps:**

$$
E[\sigma^2] \neq (E[\sigma])^2
$$

Due to Jensen's inequality (variance is convex):

$$
E[\sigma^2] > (E[\sigma])^2
$$

**Economic impact:**

**Variance swap strike:**
- Based on: $E[\sigma^2]$ (expectation of variance)
- Higher than: $(E[\sigma])^2$ (variance of expected vol)

**Volatility swap strike:**
- Based on: $E[\sigma]$ (expectation of volatility)
- More expensive relative to realized

**Typical difference: 1-3 variance points**

**Why this matters:**

Variance swaps are **cheaper** than vol swaps for same exposure because of convexity adjustment.

**Arbitrage relationship:**

$$
\text{Vol Swap Strike} = \sqrt{K_{\text{var}} - \text{Convexity Adjustment}}
$$

Where convexity adjustment ≈ 0.01-0.03 for typical parameters.

### Replication and Fair Value

**How dealers price variance swaps:**

**Theoretical fair value (model-free):**

$$
K_{\text{var}} = \frac{2}{T} \int_{0}^{\infty} \frac{C(K) + P(K)}{K^2} dK
$$

**In English:** Weighted portfolio of ALL strikes (out-of-the-money options).

**Economic interpretation:**
- Variance swap = Infinite portfolio of options
- Weighted by $1/K^2$ (more weight to lower strikes)
- **This is why crashes matter:** Heavy tail weighting

**Practical replication (actual market):**

$$
K_{\text{var}} \approx \sum_{i} \frac{2 \Delta K_i}{K_i^2} \times \text{Price}(K_i)
$$

**Using discrete strikes available in market.**

**Dealer economics:**

**When selling variance swap to client:**

1. **Revenue:** Strike $K_{\text{var}}$ agreed with client
2. **Cost:** Replicate with option portfolio
3. **Profit:** $(K_{\text{var}} - \text{Replication Cost})$ × Vega Notional

**Plus:** Bid-ask spread (typically 0.5-2 variance points)

**Risk:** Replication not perfect (strike spacing, liquidity)

### The Log Contract and Variance Replication

**Academic foundation (Demeterfi et al. 1999):**

**Realized variance equals:**

$$
\sigma_{\text{realized}}^2 = \frac{2}{T} \left[\ln\frac{S_T}{S_0} - \frac{1}{2}\left(\ln\frac{S_T}{S_0}\right)^2\right] + \text{Jump Term}
$$

**This can be replicated by:**

$$
\text{Variance Exposure} = \text{Log Contract} + \text{Option Portfolio}
$$

**Where log contract payoff: $\ln(S_T/S_0)$**

**Economic insight:**
- Log contract tracks cumulative returns
- Option portfolio captures convexity
- Together = variance replication
- **This is the theoretical foundation**

**Why dealers can quote variance swaps:**
- Know exactly how to hedge
- Static replication (buy options once)
- No rebalancing risk
- **Clean business model**

### Variance Swaps vs. Options Greeks

**Why variance swaps are "better" for pure vol trading:**

**Options exposure:**

| Greek | Variance Swap | Long Straddle |
|-------|---------------|---------------|
| **Delta** | 0 | 0 (at inception) |
| **Gamma** | 0 | High (must manage) |
| **Vega** | Pure exposure | Yes (but with theta) |
| **Theta** | 0 | Negative (decay) |
| **Volga** | 0 | Positive (convexity) |

**Variance swap = Vega only, nothing else!**

**Economic value proposition:**

Options trading:
- P&L = Gamma × realized - Theta × time + Vega × (IV change)
- **Complex attribution**

Variance swap:
- P&L = Vega Notional × (Realized variance - Strike)
- **Simple, clean**

### Market Participants and Their Motivations

**Who uses variance swaps and why:**

**1. Volatility Hedge Funds**

**Motivation:** Harvest variance risk premium
**Position:** Short variance swaps
**Rationale:** Historical VRP = 3-5% annually
**Risk:** Tail events (crashes)
**Example:** Selling 1-month variance at 20%, collecting premium when realizes 16%

**2. Long-Only Asset Managers**

**Motivation:** Portfolio protection
**Position:** Long variance swaps  
**Rationale:** Hedge against volatility spikes
**Cost:** Pay variance risk premium
**Example:** $10B equity portfolio, buy variance to protect against crashes

**3. Market Makers / Dealers**

**Motivation:** Facilitation and arbitrage
**Position:** Market neutral (offset client flows)
**Profit:** Bid-ask spread (1-2 variance points)
**Risk:** Replication error, model risk
**Example:** Sell variance to hedge fund, buy from asset manager, pocket spread

**4. Dispersion Traders**

**Motivation:** Trade index vs. single-stock variance
**Position:** Long single stocks, short index (or vice versa)
**Rationale:** Correlation mean reversion
**Example:** Index implied correlation 60%, realized 40% → profit

**5. Structured Product Issuers**

**Motivation:** Hedge structured products (autocallables, etc.)
**Position:** Varies (often short variance)
**Rationale:** Structured notes embed short variance exposure
**Risk:** Volatility spike destroys P&L
**Example:** Sold autocallable notes, hedge with short variance swap

### Variance Swap P&L Attribution

**Understanding the economics of P&L:**

$$
\text{Total P\&L} = \text{Variance P\&L} + \text{Financing Cost} - \text{Dealer Spread}
$$

**Variance P&L:**

$$
= \text{Vega Notional} \times (\sigma_{\text{realized}}^2 - K_{\text{var}})
$$

**Financing cost:**

$$
= \text{Notional} \times r \times T
$$

**Dealer spread:**

$$
= \text{Bid-Ask} \times \text{Vega Notional}
$$

**Example:**

Long 1,000 vega variance swap:
- Strike: 0.04 (20% vol)
- Realized: 0.0625 (25% vol)
- Vega notional: $1,000,000
- Time: 3 months
- Financing rate: 5%
- Dealer spread: 1 variance point

**P&L calculation:**

$$
\text{Variance P\&L} = \$1,000,000 \times (0.0625 - 0.04) = \$22,500
$$

$$
\text{Financing} = \$1,000,000 \times 0.05 \times 0.25 = \$12,500
$$

$$
\text{Spread} = \$1,000,000 \times 0.01 = \$10,000
$$

$$
\text{Net P\&L} = \$22,500 - \$12,500 - \$10,000 = \$0
$$

**Break-even!** Even though variance moved 5.75 points in your favor.

**Economic lesson:** Costs matter in variance trading.

### The Volatility-Of-Volatility Effect

**Variance swaps have exposure to vol-of-vol (VVIX, volga):**

**If volatility is volatile:**
- Realized variance higher than implied
- Benefits long variance positions
- Hurts short variance positions

**Mathematical relationship:**

$$
\text{Realized Variance} \approx \text{Implied Variance} + \alpha \times \text{Vol-of-Vol}^2
$$

Where $\alpha$ is positive coefficient.

**Economic insight:**

**Selling variance = short vol-of-vol**
- Works in calm markets (vol stable)
- Destroyed in crisis (vol explodes)

**Buying variance = long vol-of-vol**
- Costs money in normal times
- Pays off in crises

**This explains variance risk premium:**

Investors pay premium to be long vol-of-vol (convexity, crisis protection).

### Correlation and Dispersion Trading

**Variance swaps enable pure correlation trades:**

**Index variance decomposes:**

$$
\sigma_{\text{index}}^2 = \sum w_i^2 \sigma_i^2 + \sum_{i \neq j} w_i w_j \rho_{ij} \sigma_i \sigma_j
$$

**Can trade:**

$$
\text{Correlation Trade} = \text{Long Index Variance} - \sum w_i \times \text{Long Stock}_i \text{ Variance}
$$

**Economic interpretation:**
- Isolates correlation bet
- If correlation rises → profit
- If correlation falls → loss

**Why this matters:**

**Historical pattern:**
- Normal times: Correlation ≈ 30-40%
- Crisis: Correlation → 70-80%
- **Mean reversion opportunity**

**Typical dispersion trade:**

Short SPX variance (index), Long basket of single-stock variance
- Profit if: Individual stocks more volatile than index implies
- Requires: Correlation decreases
- Risk: Correlation spike (crisis)

### The Term Structure of Variance

**Variance has time structure (like bonds):**

$$
\text{Variance Curve}: K_{\text{var}}(T_1), K_{\text{var}}(T_2), ..., K_{\text{var}}(T_n)
$$

**Typical shapes:**

**Contango** (normal): Short-term < Long-term variance
- Meaning: Market expects volatility to increase
- Economic reason: Mean reversion to higher long-run vol

**Backwardation** (crisis): Short-term > Long-term variance
- Meaning: Current vol spike expected to decline
- Economic reason: Mean reversion to lower long-run vol

**Trading strategies:**

**Term structure arbitrage:**
- Buy cheap part of curve
- Sell expensive part
- Profit on convergence

**Roll yield:**
- Short front variance, long back variance
- Collect roll yield if contango persists
- Risk: Volatility spike

### Summary: The Economic Foundation

**Variance swaps exist because they provide:**

1. **Clean volatility exposure** (no delta, gamma, theta complications)
2. **Simple pricing** (model-free replication via options)
3. **Tradeable VRP** (harvest or hedge volatility risk premium)
4. **Correlation trades** (enables dispersion strategies)
5. **Static replication** (dealers can hedge without rebalancing)
6. **Linear payoffs** (additive across time, easy to manage)

**The core economic trade-off:**

$$
\text{Long Variance: Pay VRP for crisis protection}
$$

$$
\text{Short Variance: Collect VRP, accept crash risk}
$$

**Market efficiency:** Variance risk premium compensates sellers for:
- Negative skewness (crashes hurt more than rallies help)
- Liquidity provision (buyers want protection)
- Balance sheet costs (capital requirements)

**Why professionals use variance swaps:**

1. **Cleanest vol exposure** (no Greeks noise)
2. **Efficient execution** (no transaction costs from rebalancing)
3. **Transparent pricing** (option portfolio replication)
4. **Leverage efficient** (notional exposure without full notional capital)

Variance swaps are the institutional standard for pure volatility trading.




## Practical Guidance

**Step-by-step framework for trading variance swaps:**

### Step 1: Understanding Variance Swap Quotes

**How variance swaps are quoted:**

**Standard quote format:**

```
SPX 1-month Variance Swap
Bid: 18.5
Ask: 20.5
Mid: 19.5
```

**This means:**
- Variance strike in **variance units** (not vol!)
- Bid: You can sell variance at 18.5
- Ask: You can buy variance at 20.5
- **Spread: 2.0 variance points** (10% of mid)

**Converting to volatility:**

$$
\sigma = \sqrt{K_{\text{var}}} = \sqrt{0.195} = 44.16\%
$$

**Critical:** Quote is in variance (0.195), volatility equivalent is 44.16%.

**Vega notional convention:**

Variance swaps are sized by "vega notional" not absolute notional.

$$
\text{Payoff} = \text{Vega Notional} \times (\sigma_{\text{realized}}^2 - K_{\text{var}})
$$

**Example:**

- Vega notional: $1,000,000
- Strike: 0.20 (44.7% vol)
- Realized: 0.25 (50% vol)

$$
\text{Payoff} = \$1,000,000 \times (0.25 - 0.20) = \$50,000
$$

### Step 2: Market Assessment

**Before trading, analyze:**

**A. Variance Risk Premium**

Calculate current VRP:

$$
\text{VRP} = \text{Implied Var} - \text{Expected Realized Var}
$$

**Use historical realized as proxy:**

Look back 30-90 days:
- Historical realized variance: Calculate
- Current implied variance: From market quotes
- **If VRP > 0.01 (3 vol points): Selling variance favorable**
- **If VRP < 0: Buying variance favorable** (rare, crisis)

**B. Volatility Regime**

```
Check VIX percentile (or equivalent):
- VIX < 15 (low vol): Normal regime, small VRP
- VIX 15-25 (medium): Normal VRP (~3-5 vol points)
- VIX > 25 (high vol): Crisis regime, VRP can be negative
```

**C. Term Structure**

Check variance curve:

```
1M variance: 0.20
3M variance: 0.18
6M variance: 0.16
```

**Backwardation (1M > 3M > 6M):** Current vol spike expected to revert
**Contango (1M < 3M < 6M):** Vol expected to rise

**D. Dispersion Opportunity**

Compare index vs. single stocks:

$$
\text{Implied Correlation} = \frac{\sigma_{\text{index}}^2}{\sum w_i^2 \sigma_i^2}
$$

**If implied correlation > historical:**
- Single stocks expensive relative to index
- **Opportunity:** Long index var, short single stock var

**If implied correlation < historical:**
- Index expensive relative to singles
- **Opportunity:** Short index var, long single stock var

### Step 3: Position Sizing

**Variance swaps have unlimited loss potential!**

**Calculate maximum loss:**

$$
\text{Max Loss} \approx \text{Vega Notional} \times K_{\text{var}} \times 3
$$

**Why × 3?**
- Volatility rarely exceeds 3× strike
- Example: Strike 20% vol, max realistic 60% vol
- Variance: 0.04 → 0.36 (9× increase, but capped in practice)

**Example:**

Short $1,000,000 vega notional variance swap:
- Strike: 0.04 (20% vol)
- Max realistic variance: 0.36 (60% vol)
- **Max loss:** $1,000,000 × (0.36 - 0.04) = $320,000

**Position sizing rule:**

$$
\text{Max Vega Notional} = \frac{\text{Portfolio} \times \text{Risk\%}}{K_{\text{var}} \times 3}
$$

**For $10M portfolio, 5% risk:**

$$
\text{Max Vega} = \frac{\$10,000,000 \times 0.05}{0.04 \times 3} = \$4,166,667
$$

**Start smaller:** Use 2-3% risk for beginners.

### Step 4: Entry Execution

**Trading variance swaps (institutional market):**

**A. Contact Dealer**

Variance swaps are OTC (over-the-counter):
- Not exchange-traded
- Must contact bank dealer desk
- **Common dealers:** Goldman, JP Morgan, Citi, Morgan Stanley

**B. Request Quote**

```
Request format:
"3-month SPX variance swap, $2M vega notional, which way?"
```

**Dealer response:**
```
"18.5 bid, 20.5 offer"
```

**C. Negotiate**

- Spread is negotiable (typically 1-3 variance points)
- Larger size = better pricing
- **Don't accept first quote!**

**D. Confirm Terms**

ISDA confirms:
- Underlying: SPX
- Tenor: 90 days
- Strike: 0.195 (mid) or negotiated
- Vega notional: $2,000,000
- Settlement: Cash-settled at expiration
- Calculation: 252-day convention

### Step 5: Position Monitoring

**Daily monitoring tasks:**

**A. Mark-to-Market**

Calculate current P&L:

$$
\text{MTM} = \text{Vega Notional} \times (\text{Current Var Level} - K_{\text{var}})
$$

**Current var level from:**
- Dealer marks (ask for daily)
- Or replicate: $\sum \frac{2\Delta K_i}{K_i^2} \times \text{Price}(K_i)$

**B. Realized Variance Tracking**

Calculate daily:

$$
\text{Realized Var (to date)} = \frac{252}{n} \sum_{i=1}^{n} r_i^2
$$

**Running P&L:**

$$
\text{If settled today} = \text{Vega} \times (\text{Realized to date} - K_{\text{var}})
$$

**C. Days to Expiration**

Track time decay of variance:

$$
\text{Remaining Variance} = \text{Initial Var} - \text{Accrued Var}
$$

**D. Stress Testing**

Daily scenarios:

```
If VIX spikes to 40 (80% vol):
- Variance: 0.64
- P&L: $2M × (0.64 - 0.20) = $880K loss (if short)

If VIX drops to 10 (10% vol):
- Variance: 0.01
- P&L: $2M × (0.01 - 0.20) = -$380K loss (if long)
```

### Step 6: Risk Management

**Active risk controls:**

**A. Stop Loss**

Set variance point stop:

**If short variance:**
```
Stop loss at: Strike + 10 variance points
Example: Strike 0.20, stop at 0.30
```

**If long variance:**
```
Stop loss at: Strike - 10 variance points
Example: Strike 0.20, stop at 0.10
```

**B. Position Limits**

```
Maximum short variance: 2× annual VRP collection
Maximum long variance: 5% of portfolio (hedge position)
Maximum vega notional: Stress loss < 10% portfolio
```

**C. Correlation Limits**

If running dispersion:

```
Net correlation exposure < 20% of gross
Example: Long $10M index, short $10M singles
Max net: $2M equivalent
```

**D. Event Risk**

**Before major events (Fed, earnings):**
- Reduce position size by 50%
- Or hedge with options
- Or close entirely

### Step 7: Exit Strategies

**When to close variance swap:**

**A. Target Met**

**If short variance:**

$$
\text{Close when: Realized Var} < \text{Strike} - \text{2 std dev}
$$

**Locked in profit, no need to wait.**

**B. Stop Loss Hit**

$$
\text{If loss} > \text{Max Loss Budget} \Rightarrow \text{Close immediately}
$$

**C. Time-Based**

**Rule:** Close at 80% of time elapsed

**Reason:** Last 20% of time contributes to only ~10% of variance
- Risk/reward unfavorable
- Better to close and redeploy

**D. Regime Change**

**If volatility regime shifts:**
- Calm → Crisis: Close short variance
- Crisis → Calm: Close long variance
- **Don't fight regime**

**E. P&L Target**

Set targets upfront:

```
Short variance:
- Target: 50% of premium
- Stop: -200% of premium

Long variance:
- Target: 200% of premium
- Stop: -100% of premium
```

### Step 8: Expiration Settlement

**Variance swap settlement:**

**A. Final Variance Calculation**

Sum all daily squared returns:

$$
\sigma_{\text{realized}}^2 = \frac{252}{n} \sum_{i=1}^{n} \left(\ln\frac{S_{i}}{S_{i-1}}\right)^2
$$

**Important:** Uses logarithmic returns, not simple returns!

**B. Final P&L**

$$
\text{Final P\&L} = \text{Vega Notional} \times (\sigma_{\text{realized}}^2 - K_{\text{var}})
$$

**C. Cash Settlement**

- Usually T+2 after expiration
- Wire transfer
- Check dealer calculation!

**D. Disputes**

If discrepancy in realized variance calculation:
- Both parties use same price source (agreed in ISDA)
- Typically: Official settlement prices
- **Dispute resolution:** Independent verification

### Step 9: Advanced Tactics

**A. Variance Carry Trade**

**Exploit term structure:**

If contango: 1M variance < 3M variance
- Short 1M variance
- Long 3M variance
- **Collect roll yield** as term structure flattens

**B. Volatility-of-Volatility Play**

**If expect vol spike:**
- Buy short-dated variance (high vol-of-vol sensitivity)
- Benefits disproportionately from vol explosion

**C. Gamma Hedging**

**Reduce tail risk on short variance:**
- Buy OTM puts (tail hedge)
- Costs small premium
- **Protects against crash**

**Example:**

Short $5M vega variance at 0.20:
- Buy $500K of 20% OTM puts
- Cost: $25K
- **Caps crash loss at $400K** (vs. unlimited)

**D. Dynamic Variance Swap**

**Adjust notional dynamically:**

```
If realized var > strike (winning):
→ Increase notional (press bet)

If realized var < strike (losing):
→ Decrease notional (cut losses)
```

**Caution:** Transaction costs on adjustments!

### Platform Requirements

**Variance swaps are institutional products:**

**Minimum requirements:**
- **ISDA agreement** with dealer(s)
- **Credit line** (bilateral collateral)
- **$10M+ account** (practical minimum)
- **Sophistication** (qualified purchaser)

**Technology needs:**
- Variance calculation system
- Real-time pricing (option portfolio)
- Risk management platform
- Dealer communication (Bloomberg, phone)

**Not available to retail traders!**

### Synthetic Variance Swaps (Retail Alternative)

**If no access to variance swaps:**

**Replicate with options:**

$$
\text{Variance Exposure} \approx \sum \frac{2\Delta K_i}{K_i^2} \times \text{Long OTM Options}
$$

**Implementation:**
1. Buy strip of OTM puts (5-20%)
2. Buy strip of OTM calls (5-20%)
3. Weight by $1/K^2$
4. Hold to expiration

**Differences from true variance swap:**
- Requires capital for options
- Subject to theta decay
- Discrete strikes (tracking error)
- Transaction costs

**But provides similar variance exposure.**

### Record Keeping

**Track for every variance swap trade:**

```
Entry Information:
- Date entered: [Date]
- Underlying: [SPX, etc.]
- Tenor: [Days]
- Strike: [Variance units]
- Vol equivalent: [%]
- Vega notional: [$]
- Direction: [Long/Short]
- Dealer: [Bank name]
- Spread paid: [Variance points]

Daily Monitoring:
- Current variance level: [Updated daily]
- Realized variance to date: [Calculation]
- MTM P&L: [$]
- Days remaining: [#]
- VIX level: [#]

Exit Information:
- Date closed/expired: [Date]
- Exit variance level: [#]
- Final realized variance: [#]
- Final P&L: [$]
- Return on risk: [%]
- Lessons learned: [Notes]
```

### Success Metrics

**Track monthly:**

**Win rate:**

$$
\text{Win Rate} = \frac{\# \text{Profitable Trades}}{\# \text{Total Trades}}
$$

**Target:** >60% for short variance, >40% for long variance

**Sharpe ratio:**

$$
\text{Sharpe} = \frac{\text{Average Return}}{\text{StDev of Returns}}
$$

**Target:** >0.5 for variance trading

**Maximum drawdown:**

$$
\text{Max DD} = \max_{t}\left[\max_{s \leq t} V_s - V_t\right]
$$

**Target:** <20% of portfolio

**VRP capture:**

For short variance programs:

$$
\text{VRP Capture} = \frac{\text{Actual Return}}{\text{Available VRP}}
$$

**Target:** >70% (capturing 70% of available VRP)

### Pre-Trade Checklist

**Before entering ANY variance swap:**

```
☐ Calculated maximum loss (Vega × K_var × 3)
☐ Position size ≤ risk budget
☐ VRP analyzed (know what you're betting on)
☐ Term structure checked
☐ No major events in next 2 weeks
☐ Liquidity sufficient (can exit if needed)
☐ Dealer spread acceptable (<5% of strike)
☐ Monitoring system ready
☐ Stop loss level set
☐ Exit plan documented
☐ Understand settlement mechanics
☐ ISDA and credit line in place
☐ Stress tested position (VIX to 50, 80)
☐ Correlation risk assessed (if dispersion)
☐ Not overleveraged (total vega < portfolio limit)
```

**If any box unchecked: DO NOT TRADE.**

**Variance swaps are sophisticated instruments. Treat them with respect, manage risk religiously, and never bet more than you can afford to lose.**




## Common Mistakes

**Critical errors in variance swap trading:**

### Mistake #1: Confusing Variance and Volatility Units

**What it looks like:**

- Dealer quotes: "Variance at 20"
- Trader thinks: "20% volatility? That's high"
- Actually: **20 variance units = 0.20 = 44.7% volatility**

**The math:**

$$
\sigma = \sqrt{K_{\text{var}}} = \sqrt{0.20} = 0.447 = 44.7\%
$$

**Real example:**

Trader wants to sell "25% volatility":
- Calculates: Need strike of 0.25
- Actually: Variance of 0.25 = **50% volatility**!
- Should be: 0.25² = **0.0625** variance strike

**Consequence:**

Sold variance at 50% vol equivalent instead of 25% vol:
- Massive overexposure (4× intended)
- Unlimited loss potential

**Fix:**
- **ALWAYS convert:** Variance → Volatility before trading
- Double-check units with dealer
- Use formula: $\sigma = \sqrt{\text{Variance}}$

---

### Mistake #2: Under-Estimating Maximum Loss

**What it looks like:**

- Short $1M vega variance at 0.20 strike
- Think: "Max loss is maybe $200K"
- **VIX spikes to 80%:** Variance = 0.64
- **Actual loss:** $1M × (0.64 - 0.20) = **$440K**

**Worse scenario (March 2020):**
- VIX hit 85% (variance 0.72)
- Loss: $1M × (0.72 - 0.20) = **$520K**

**The problem:**

$$
\text{Max Loss (short variance)} = \text{Vega Notional} \times (\sigma_{\max}^2 - K_{\text{var}})
$$

**Variance is squared:** 80% vol = 64× variance of 10% vol!

**Fix:**
- **Stress test to VIX 80-100**
- Position size: Max loss < 10% portfolio
- Use formula: Vega × (1.00 - Strike) for worst case
- Buy tail hedge if short variance

---

### Mistake #3: Ignoring Dealer Spread

**What it looks like:**

- Variance quote: Bid 18, Ask 20
- Spread: 2 variance points (10%!)
- Trade both sides over time
- **Lost 10% on round-trip**

**Example:**

Month 1: Buy variance at 20 (pay offer)
Month 2: Sell same strike at 18 (hit bid)
- **Lost 2 variance points = $2M on $20M vega**
- **10% haircut on transaction**

**Typical spreads:**
- SPX 1-month: 1-2 variance points
- Single stocks: 3-5 variance points
- Illiquid names: 5-10 variance points

**Fix:**
- **Negotiate spread** (especially on size)
- Factor spread into expected return
- Hold to maturity (avoid round-trip)
- Only trade when edge > 2× spread

---

### Mistake #4: Not Understanding Convexity (Jensen's)

**What it looks like:**

- Historical avg volatility: 20%
- Variance strike: 0.04 (20% vol)
- Think: "Fair strike!"
- **Wrong:** Should be **higher** due to convexity

**The math:**

$$
E[\sigma^2] > (E[\sigma])^2
$$

**Example:**

Two scenarios, equal probability:
- Scenario A: 15% vol (variance 0.0225)
- Scenario B: 25% vol (variance 0.0625)

**Average volatility:** (15% + 25%) / 2 = **20%**

**Average variance:** (0.0225 + 0.0625) / 2 = **0.0425**

**Naive strike:** 0.04 (20% vol)
**Correct strike:** 0.0425 (20.6% vol)

**Difference:** 0.0025 variance points (worth $2,500 per $1M vega!)

**Fix:**
- **Fair strike > historical avg variance**
- Add convexity adjustment (+1-2 variance points)
- Use realized variance distribution, not average

---

### Mistake #5: Selling Variance in High Vol Regimes

**What it looks like:**

- VIX at 35 (high)
- Variance swap strike: 0.35 (59% vol)
- Think: "High premium, good selling opportunity!"
- **VIX goes to 50:** Massive loss

**The problem:**

High vol regimes are PERSISTENT:
- If VIX 35 today, often stays elevated
- Vol-of-vol high (big swings)
- Tail risk maximized

**Historical data:**

When VIX > 30:
- **Mean reversion is SLOW** (weeks/months)
- **Probability of spike higher:** 30% chance of VIX >50
- **VRP often negative** (realized > implied in crisis)

**Example (March 2020):**

Feb 20: VIX at 15, sold 1-month variance at 0.0225
Mar 15: VIX at 82, variance realized 0.67
- **Loss: 64× variance increase!**

**Fix:**
- **Never sell variance when VIX > 25**
- If short, close when VIX spikes >30
- High vol = time to BUY variance (or stay out)

---

### Mistake #6: Overleveraging Vega Notional

**What it looks like:**

- $5M portfolio
- Short $20M vega variance swap
- **4× leverage on vega exposure**

**The disaster:**

Vol spikes 20% → 60%:
- Variance: 0.04 → 0.36 (9× increase)
- Variance change: +0.32
- **Loss:** $20M × 0.32 = **$6.4M**
- **Portfolio wiped out!**

**Leverage trap:**

Variance swaps don't require upfront capital:
- Easy to take massive notional
- No margin call until settlement
- **Hidden leverage kills you**

**Fix:**
- **Max vega ≤ portfolio value**
- Conservative: Vega ≤ 50% of portfolio
- Stress test: Loss at VIX 80 < 20% of portfolio

---

### Mistake #7: Ignoring Realized Variance Calculation Method

**What it looks like:**

- Calculate realized variance using simple returns
- Dealer uses log returns
- **Discrepancy in settlement**

**The difference:**

**Simple returns:**

$$
\sigma^2 = \sum \left(\frac{S_i - S_{i-1}}{S_{i-1}}\right)^2
$$

**Log returns (correct for variance swaps):**

$$
\sigma^2 = \sum \left(\ln\frac{S_i}{S_{i-1}}\right)^2
$$

**Example:**

Stock moves +10%, then -9.09%:
- Simple: Back to start (0% net)
- Log: (+9.53%, -9.53%) = Different!

**Variance difference:** Can be 1-2 variance points on volatile stocks.

**Fix:**
- **Always use log returns** for variance calculation
- Verify calculation method in ISDA confirm
- Double-check dealer's realized variance at settlement

---

### Mistake #8: Trading Variance Without Stop Loss

**What it looks like:**

- Short variance, no stop loss
- "I'll wait it out"
- Vol keeps rising
- **Unlimited loss accumulation**

**Real example:**

Feb 2020: Short SPX variance at 0.03
- No stop loss set
- VIX 15 → 25 → 40 → 85
- Loss mounted: $0 → -$50K → -$200K → -$700K
- Finally closed at -$500K (after VIX peak)

**If had stop at VIX 30:**
- Loss: -$100K
- Saved: **$400K**

**Fix:**
- **Always set variance stop:** Strike + 10 points
- Or VIX-based: Exit when VIX > 30 (if short)
- Or loss-based: Exit at -100% of expected profit
- **No exceptions**

---

### Mistake #9: Not Hedging Tail Risk

**What it looks like:**

- Short $10M vega variance (collect VRP)
- No tail hedge
- Black swan hits
- **Account blown up**

**The math:**

Selling variance:
- Annual VRP: ~3% of notional
- Tail event (1-in-10 years): -30% of notional
- **Expected value negative without hedge!**

**Proper approach:**

Short $10M variance + Buy $1M OTM puts:
- VRP collected: $300K/year
- Put cost: -$50K/year
- **Net: $250K/year**
- Tail protection: Puts cap loss at -15%

**Cost of hedge: $50K**
**Benefit: Survival**

**Fix:**
- Always hedge tail if short variance
- Buy 20-30% OTM puts (cheap insurance)
- Cost: 1-2% of notional annually
- **Worth it for survival**

---

### Mistake #10: Assuming VRP Will Always Exist

**What it looks like:**

- Historical VRP: 3-5% annually
- Build strategy around harvesting it
- **During crisis: VRP goes NEGATIVE**

**Historical VRP inversions:**

- 1987 crash: VRP -20%
- 2008 crisis: VRP -15%
- 2020 COVID: VRP -10%
- **Selling variance lost money**

**Why VRP disappears:**

In crisis:
- Realized vol > Implied vol
- Options get exercised (actual events)
- Dealers widen spreads
- **VRP premium vanishes or inverts**

**Fix:**
- **VRP is a premium, not a law of nature**
- Only harvest when VRP clearly positive
- Exit when VRP < 1%
- Never assume it persists in all regimes

---

### Mistake #11: Misunderstanding Settlement

**What it looks like:**

- Variance swap expiring in 2 days
- Realized variance: 0.18
- Strike: 0.20
- Think: "I'm winning, $2M profit!"
- **Last 2 days: Market crashes**
- Final realized: 0.25
- **Loss: -$5M**

**The problem:**

$$
\text{Final} = \frac{252}{n} \sum_{i=1}^{n} r_i^2
$$

**Last few days can dominate:**
- If 5% move on day 89/90
- Contributes: (0.05)² × (252/90) = 0.007 variance
- **3.5% of total variance in one day!**

**Fix:**
- **Don't count chickens before settlement**
- Last week highly volatile
- Close early if winning (lock profit)
- Never assume you've won until cash settles

---

### Mistake #12: Ignoring Correlation Risk (Dispersion)

**What it looks like:**

- Long index variance, short single stock variance
- Net: Long correlation
- **All stocks crash together:** Correlation spikes
- **Massive loss**

**Example:**

- Long $10M SPX variance at 0.20
- Short $10M basket (AAPL, MSFT, GOOGL, etc) at 0.15
- **Normal correlation: 40%**
- Crisis: Correlation → 80%
- Index variance realized: 0.50
- Single stocks variance: 0.40 (average)

**P&L:**
- Index: $10M × (0.50 - 0.20) = +$3M
- Singles: -$10M × (0.40 - 0.15) = -$2.5M
- **Net: +$500K** (expected $1M+)

**If correlation stayed at 40%:**
- Would have made $2M+

**Fix:**
- **Correlation risk is HUGE in dispersion**
- Hedge with correlation swaps
- Size smaller (correlation can spike 2×)
- Monitor daily correlation changes

---

### Mistake #13: Not Understanding Financing Costs

**What it looks like:**

- Long $5M variance swap
- Held for 1 year
- Financing at 5%
- **Cost: $250K just for financing!**

**The problem:**

Variance swaps are unfunded:
- Notional exposure without capital outlay
- But dealers charge financing
- **Hidden cost eats profits**

**Example:**

Long variance:
- Strike: 0.20
- Realized: 0.24
- Profit: $5M × 0.04 = **$200K**
- Financing: $5M × 5% = **$250K**
- **Net: -$50K loss!**

**Fix:**
- **Factor financing into expected return**
- Financing Cost = Vega Notional × Rate × Time
- Need realized >> strike to overcome
- Short variance: Earn financing (benefit)

---

### Mistake #14: Trading Illiquid Underlying Variance

**What it looks like:**

- Trade variance on small-cap stock
- Bid-ask spread: 8 variance points
- Liquidity dries up
- **Can't exit**

**Problem:**

- Dealer can't hedge (no option liquidity)
- Spread widens to 10-15 points
- **Trapped in position**

**Example:**

Sold variance on XYZ (small cap):
- Strike: 0.30
- Vol spikes, want to close
- Bid: 0.45, Ask: 0.60
- **Spread: 15 points = 50% of strike!**
- Can't exit without massive loss

**Fix:**
- **Only trade liquid names:** SPX, QQQ, top 50 stocks
- Check options market: Volume > 10,000/day
- Test dealer bid-ask BEFORE trading
- Illiquid = avoid (no matter how attractive)

---

### Mistake #15: Not Documenting Trades

**What it looks like:**

- Trade 5-6 variance swaps
- Don't track performance
- Don't know what works
- **Repeat same mistakes**

**Example:**

After 1 year:
- Some winners, some losers
- Net: -$50K
- **No idea which strategies worked**
- Can't improve

**Fix:**

**Track spreadsheet:**
```
Date | Underlying | Tenor | Strike | Vega | Long/Short | VRP | Realized | P&L | Lessons
```

**Analyze quarterly:**
- Win rate
- VRP capture (if short)
- Best tenors (1M vs 3M)
- Best underlyings
- **Optimize based on data**

---

### **Summary: Variance Swap Mistakes Checklist**

**Before any variance swap trade:**

```
☐ Converted variance ↔ volatility (checked units)
☐ Stress tested to VIX 80 (know max loss)
☐ Spread acceptable (<3% of strike)
☐ Accounted for convexity (Jensen's inequality)
☐ Not in high vol regime (VIX < 25 for selling)
☐ Position size ≤ portfolio (no overleveraging)
☐ Will use log returns (calculation method)
☐ Stop loss set (variance or VIX-based)
☐ Tail hedge in place (if short)
☐ VRP currently positive (checked)
☐ Won't count on winning until settled (patience)
☐ Correlation risk assessed (if dispersion)
☐ Financing cost calculated (factored in)
☐ Underlying liquid (can exit if needed)
☐ Trade documented (will track and learn)
```

**If any box unchecked: RECONSIDER TRADE.**

**Variance swaps amplify both profits and losses. Mistakes that would cost 10% in options trading can wipe out accounts in variance swaps. Discipline and risk management are EVERYTHING.**





---

## Real-World Examples

**Detailed case studies of variance swap trading:**

### Example 1: Harvesting VRP (Successful Short Variance Program)

**Background:**

- **Entity:** Volatility arbitrage hedge fund
- **Strategy:** Systematic short variance program
- **Capital:** $50M fund
- **Timeframe:** 2015-2019 (pre-COVID)

**The Approach:**

**Monthly program:**
- Short $10M vega SPX 1-month variance
- Target strike: 20-25% vol equivalent
- Roll monthly (new trade first week of month)
- Tail hedge: 5% of capital in OTM puts

**Year 1 (2015) Results:**

| Month | Strike | Realized | Variance P&L | Tail Hedge Cost | Net P&L |
|-------|--------|----------|--------------|-----------------|---------|
| Jan | 0.048 | 0.032 | +$160K | -$5K | +$155K |
| Feb | 0.045 | 0.038 | +$70K | -$5K | +$65K |
| Mar | 0.042 | 0.041 | +$10K | -$5K | +$5K |
| Apr | 0.040 | 0.028 | +$120K | -$5K | +$115K |
| May | 0.038 | 0.045 | -$70K | -$5K | -$75K |
| Jun | 0.041 | 0.035 | +$60K | -$5K | +$55K |
| ... | ... | ... | ... | ... | ... |
| **Annual** | **Avg 0.043** | **Avg 0.036** | **+$840K** | **-$60K** | **+$780K** |

**Performance metrics:**
- Win rate: 75% (9 winners, 3 losers)
- VRP captured: 70% of available (0.007 out of 0.010)
- Return on capital: 15.6% annually
- **Sharpe ratio:** 1.8 (excellent)

**Years 2-4 (2016-2019):**

Similar performance, compounding:
- 2016: +17.2%
- 2017: +14.8%
- 2018: +11.2% (tougher, more volatility)
- 2019: +16.5%

**4-year cumulative:** +60.3% with max drawdown of -12%

**Key Lessons:**
1. VRP harvesting works in normal regimes
2. Tail hedge essential (cost 1.2% but saved fund in flash crashes)
3. Consistency > home runs
4. 75% win rate sustainable with discipline

---

### Example 2: COVID Crash Disaster (March 2020)

**Background:**

- **Trader:** Proprietary trading desk at bank
- **Position:** Short $25M vega SPX variance
- **Entry:** February 18, 2020
- **Strike:** 0.028 (16.7% vol - low VIX environment)

**What Happened:**

**Week 1 (Feb 18-21):**
- VIX: 14 → 16
- Variance MTM: 0.028 → 0.032
- **Loss: -$100K** (minor)
- No action taken ("noise")

**Week 2 (Feb 24-28):**
- COVID concerns emerge
- VIX: 16 → 25 → 40
- Variance: 0.032 → 0.16
- **Loss: -$3.3M** (13% of desk capital)
- Should have closed but "it will revert"

**Week 3 (Mar 2-6):**
- VIX: 40 → 54
- Variance: 0.16 → 0.30
- **Loss: -$6.8M** (27% of desk)
- Panic, but "too late to sell"

**Week 4 (Mar 9-13):**
- VIX: 54 → 76 (circuit breakers)
- Variance: 0.30 → 0.58
- **Loss: -$13.8M** (55% of desk)
- Risk management forced close

**Final settlement (Mar 18):**
- VIX peaked at 85
- Final realized variance: 0.67
- **Total loss: $25M × (0.67 - 0.028) = -$16.05M**
- **64% of entire desk capital wiped out**

**What Went Wrong:**

1. **No stop loss:** Should have exited at VIX 30 (-$800K loss)
2. **No tail hedge:** $500K in puts would have capped loss at -$5M
3. **Oversized:** $25M vega on $25M capital = 100% leverage
4. **Denial:** Refused to accept regime change

**Proper approach would have:**
- Smaller size: $5M vega (saved $12M)
- Stop loss: Exit at VIX 30 (saved $15M)
- Tail hedge: -$3M max vs. -$16M actual

**This trade destroyed careers.**

---

### Example 3: Long Variance Windfall (Brexit Vote)

**Background:**

- **Trader:** Macro hedge fund
- **Thesis:** Brexit vote underpriced by markets
- **Date:** June 2016

**The Setup (June 15, 2016):**

**Market view:**
- Consensus: "Remain" wins easily
- VIX: 17 (normal)
- Variance strikes:

1-week FTSE variance: 0.029 (17% vol)
1-week SPX variance: 0.030 (17.3% vol)

**Conviction:**
- If "Leave" wins → panic
- VIX could hit 30-40
- **Asymmetric bet**

**Position:**
- Long $5M vega FTSE 1-week variance at 0.029
- Long $3M vega SPX 1-week variance at 0.030
- Total capital at risk: $8M vega
- Cost (financing + spread): $80K

**The Result (June 23-24):**

**Brexit vote: "Leave" wins (surprise)**

June 24 market:
- FTSE crashes -8%
- SPX drops -3.6%
- VIX spikes: 17 → 25
- FTSE volatility: 40%+

**Final realized variance:**
- FTSE: 0.16 (40% vol)
- SPX: 0.063 (25% vol)

**P&L calculation:**

FTSE:
- Entry strike: 0.029
- Realized: 0.16
- **Profit:** $5M × (0.16 - 0.029) = **+$655K**

SPX:
- Entry strike: 0.030
- Realized: 0.063
- **Profit:** $3M × (0.063 - 0.030) = **+$99K**

**Total profit: $754K on $80K cost = 943% ROI**

**Key Lessons:**
1. Event-driven variance bets can be asymmetric
2. Cost is financing + spread (small)
3. Potential is unlimited (if right)
4. Size small (tail events rare)

---

### Example 4: Dispersion Trade (Correlation Arbitrage)

**Background:**

- **Fund:** Equity vol specialist
- **Strategy:** Implied correlation too high
- **Date:** September 2021

**The Analysis:**

**Implied correlation from variance swaps:**

$$
\rho_{\text{impl}} = \frac{\sigma_{\text{SPX}}^2}{\sum w_i^2 \sigma_i^2} = \frac{0.036}{0.060} = 0.60 \text{ (60\%)}
$$

**Historical realized correlation:** 35-45% (5-year average)

**Thesis:** Correlation will mean-revert to 40%

**The Trade:**

**Leg 1 (Long single stock variance):**
- AAPL: $2M vega at 0.045 (21.2% vol)
- MSFT: $2M vega at 0.038 (19.5% vol)
- GOOGL: $2M vega at 0.042 (20.5% vol)
- AMZN: $2M vega at 0.048 (21.9% vol)
- META: $2M vega at 0.052 (22.8% vol)
**Total: $10M vega, weighted avg strike 0.045**

**Leg 2 (Short index variance):**
- SPX: $10M vega at 0.036 (19% vol)

**Net position:**
- Long $10M single stocks at 0.045
- Short $10M index at 0.036
- **Net: Long dispersion / Short correlation**

**What Happened (3 months):**

**Realized variances:**
- AAPL: 0.051
- MSFT: 0.043
- GOOGL: 0.048
- AMZN: 0.055
- META: 0.060
- **Average singles: 0.0514**

- SPX: 0.033

**Realized correlation:** 37% (vs. 60% implied)

**P&L:**

Singles leg:
- $2M × (0.051 - 0.045) = +$12K (AAPL)
- $2M × (0.043 - 0.038) = +$10K (MSFT)
- $2M × (0.048 - 0.042) = +$12K (GOOGL)
- $2M × (0.055 - 0.048) = +$14K (AMZN)
- $2M × (0.060 - 0.052) = +$16K (META)
**Total: +$64K**

Index leg:
- $10M × (0.033 - 0.036) = **+$30K**

**Net profit: +$94K (0.94% on $10M notional)**

**Annualized: 3.76%** (held 3 months)

**Key Lessons:**
1. Correlation mean-reversion is real but slow
2. Need large size to make meaningful profit
3. Works best when implied >> historical (60% vs. 40%)
4. Requires sophistication (not for beginners)

---

### Example 5: Retail Trader Synthetic Variance (DIY Approach)

**Background:**

- **Trader:** Individual with $100K account
- **Problem:** No access to variance swaps (institutional only)
- **Solution:** Replicate with options

**The Implementation:**

**Goal:** Long variance exposure on SPY

**Option portfolio replication:**

Buy portfolio of OTM options weighted by $1/K^2$:

**Puts (below current $450):**
- 5 contracts $400 put ($0.80 each) = $400 total
- 8 contracts $410 put ($1.20 each) = $960
- 12 contracts $420 put ($1.90 each) = $2,280
- 20 contracts $430 put ($3.10 each) = $6,200
- 30 contracts $440 put ($5.50 each) = $16,500

**Calls (above $450):**
- 30 contracts $460 call ($5.30 each) = $15,900
- 20 contracts $470 call ($3.20 each) = $6,400
- 12 contracts $480 call ($1.95 each) = $2,340
- 8 contracts $490 call ($1.15 each) = $920
- 5 contracts $500 call ($0.70 each) = $350

**Total cost:** $51,250 (51.25% of account)

**Tenor:** 30 days

**What Happened:**

**Scenario: Volatility spike**

Days 1-20: SPY ranges $448-$452 (quiet)
Days 21-25: Flash crash to $430
Days 26-30: Recovery to $445

**Expiration values:**

All puts expired worthless (SPY > $450)
All calls expired worthless (SPY < $450)

**Loss: -$51,250** (100% loss on options)

**But variance realized: 35%** (variance = 0.1225)

**If had true variance swap:**
- Strike would have been: 0.045 (21.2% vol)
- Payoff: Vega × (0.1225 - 0.045) = +77.5% return
- **On $50K vega: +$38,750 profit**

**Why synthetic failed:**
- Theta decay: -$30,000
- Strike spacing: Tracking error -$15,000
- Total drag: -$45,000

**True variance would have netted +$38K vs. lost -$51K**

**Key Lessons:**
1. Synthetic variance has huge theta drag
2. Tracking error significant (discrete strikes)
3. Works only if realized >> expected by large margin
4. True variance swaps far superior (if accessible)

---

### Example 6: Term Structure Arbitrage

**Background:**

- **Desk:** Exotic derivatives desk at bank
- **Opportunity:** Variance term structure inverted
- **Date:** August 2015 (post flash-crash)

**The Setup:**

**Variance curve (unusual shape):**
- 1-month: 0.065 (25.5% vol) ← HIGH
- 3-month: 0.048 (21.9% vol)
- 6-month: 0.042 (20.5% vol)
- **Backwardation:** Short-term > Long-term

**Interpretation:**
- Market expects current spike to revert
- Paying premium for short-term variance
- **Arbitrage:** Sell short, buy long

**The Trade:**

**Short front:**
- Sell $20M vega 1-month SPX variance at 0.065

**Long back:**
- Buy $20M vega 6-month SPX variance at 0.042

**Net:** Short variance curve steepness

**Cost:**
- Dealer spread: -$200K
- Financing: 6 months × 4% × $20M = -$400K
- **Total cost: -$600K**

**Target:** Curve flattens (1M and 6M converge)

**What Happened:**

**Month 1:** Volatility calmed
- 1-month realized: 0.052 (vs. 0.065 strike)
- **Profit:** $20M × (0.052 - 0.065) = +$260K

**Months 2-6:** Continued normalization
- 6-month continued accruing
- Final 6-month realized: 0.048 (vs. 0.042 strike)
- **Loss:** $20M × (0.048 - 0.042) = -$120K

**Net P&L:**
- Short 1M: +$260K
- Long 6M: -$120K
- Costs: -$600K
- **Total: -$460K loss**

**What Went Wrong:**

1. Curve did flatten (thesis correct)
2. But **dealer spread + financing killed profit**
3. Would have needed 3+ variance point move to profit
4. **Spread too tight for term structure bet**

**Key Lesson:**
- Term structure arbitrage hard in variance
- Costs (spread + financing) very high
- Need WIDE dislocations (5+ variance points)
- Dealers win on this trade (collect spread both sides)

---

**These examples show:** Variance swaps can generate excellent returns (Example 1, 3) but also catastrophic losses (Example 2). Discipline, position sizing, and risk management separate survivors from casualties. The difference between +60% and -64% is often just proper stop losses and tail hedges.




## What to Remember

### Core Concept

**Variance swaps provide pure, direct exposure to realized variance:**

$$
\boxed{\text{Payoff} = \text{Notional} \times (\sigma_{\text{realized}}^2 - K_{\text{var}})}
$$

- No hedging required
- No transaction costs
- No theta decay
- Perfect variance exposure

### The Beautiful Simplicity

**Compared to gamma scalping:**

- Gamma scalping = imperfect, costly replication of variance
- Variance swap = pure, clean variance exposure
- Variance swap is what gamma scalping "wants to be"

**In the limit:**

- Continuous gamma scalping → variance swap payoff
- Variance swap = theoretical ideal
- Gamma scalping = practical approximation

### Two Directions

**Long Variance:**

- Buy variance swap
- Profit when realized > strike
- Use when expecting volatility spike
- Similar to buying options

**Short Variance:**

- Sell variance swap
- Profit when realized < strike
- Harvest variance risk premium
- Similar to selling options

### The Variance Risk Premium

**Empirical fact:**

- Implied variance > realized variance (on average)
- Short variance has positive expected return
- ~3-5% annually for S&P 500
- But with significant tail risk

**Why:**

- Investors pay for volatility protection
- Risk aversion
- Hedging demand
- Like insurance premium

### Comparison to Other Strategies

**The hierarchy:**

1. **Delta Hedging** → Nothing (risk management)
2. **Gamma Scalping** → Realized vol (approximate, costly)
3. **Vega Trading** → Implied vol (expectations)
4. **Variance Swap** → Realized variance (pure, clean)
5. **Dispersion** → Correlation (relationships)

**Variance swaps are the "cleanest" volatility exposure:**

- No complications
- Pure mathematical exposure
- Theoretical ideal

### Practical Reality

**Advantages:**

- Operationally simple
- No hedging needed
- Pure exposure

**Limitations:**

- Institutional only
- Counterparty risk
- Illiquid
- Can't easily exit

### The Deep Insight

**All volatility trading ultimately comes down to variance:**

- **Gamma scalping:** Accumulates variance through rebalancing (with friction)
- **Vega trading:** Bets on implied variance expectations
- **Variance swap:** Direct bet on actual variance (no friction)

**The relationship:**

```
Theoretical World          Real World
     ↓                        ↓
Variance Swap          Gamma Scalping
(Pure variance)    →   (Variance + friction)
     ↓                        ↓
Mathematical           Operational
    ideal              implementation
```

**Understanding variance swaps helps you understand what ALL volatility strategies are trying to achieve.**

### Final Wisdom

**The evolution of volatility trading:**

**Level 1:** Buy/sell options (directional + vol)
**Level 2:** Delta hedge options (isolate vol)
**Level 3:** Gamma scalp (harvest realized vol with friction)
**Level 4:** Variance swap (pure realized vol, no friction)
**Level 5:** Variance dispersion (pure correlation, no friction)

**Each level removes one more source of noise:**

- Direction → Delta hedge
- Theta → Variance swap
- Transaction costs → Variance swap
- Single asset → Dispersion

**Variance swaps represent the penultimate level:**

- Clean exposure to what you want
- No operational complexity
- Mathematical elegance

**They're the "Platonic form" of volatility trading - the ideal that imperfect reality (options, gamma scalping) approximates.**

### Your Complete Toolkit

**You now understand six strategies, all built on the same foundation:**

1. **Delta Hedging** - Risk management
2. **Gamma Scalping** - Realized vol (approximate)
3. **Vega Trading** - Implied vol
4. **Dispersion Trading** - Correlation
5. **Convertible Arbitrage** - Multi-factor
6. **Variance Swaps** - Realized variance (pure)

**Each has its place:**

- Variance swap: When available, cleanest exposure
- Gamma scalping: Retail-accessible approximation
- Vega: Trade expectations, not reality
- Dispersion: Trade correlations
- Convertibles: Multi-factor opportunities
- Delta hedging: Foundation for all

**Master these six, and you understand the complete landscape of volatility trading!** 📊
