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
