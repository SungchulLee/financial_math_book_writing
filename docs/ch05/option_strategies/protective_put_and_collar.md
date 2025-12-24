# Protective Puts and Collars

**Protective puts and collars** are portfolio hedging strategies where you protect long stock positions against downside risk using options, either by buying puts (insurance) or combining bought puts with sold calls (zero-cost protection).

---

## The Core Insight

**The fundamental idea:**
- You own stock and want to protect it
- Buy put = insurance (pay premium, get protection)
- Collar = put + call (free insurance, cap upside)
- Accept cost or opportunity cost for peace of mind
- Static hedge (set and forget until expiration)

**The key equation:**
$$
\text{Protected Position} = \text{Long Stock} + \text{Long Put} ± \text{Short Call}
$$

**You're essentially saying: "I want to own this stock long-term, but I need downside protection for the next few months."**

---

## What Is a Protective Put?

**The simplest portfolio insurance:**

### The Structure

**Protective Put = Long Stock + Long Put**

**Example:**
- Own 100 shares of AAPL at $150
- Buy 1 put contract, strike $145, expiration 3 months
- Pay $5 premium ($500)

**What you've created:**
- Unlimited upside (stock can rise forever)
- Limited downside (protected below $145)
- Cost: $500 premium

### Why Use a Protective Put?

**Scenarios:**

**1. Holding valuable position:**
- Own stock with large unrealized gains
- Don't want to sell (taxes, conviction)
- But worried about near-term pullback
- **Buy puts for temporary protection**

**2. Volatile period ahead:**
- Earnings season
- Economic uncertainty
- Market turbulence
- **Insurance during storm**

**3. Portfolio protection:**
- Concentrated position (too much one stock)
- Can't diversify yet (lockup, vesting)
- **Hedge the concentration risk**

**4. Lock in gains:**
- Stock ran up significantly
- Want to protect profits
- Not ready to sell
- **"Insure" your gains**

### The Payoff Diagram

```
    Profit
      ↑
      |        /
      |       / (Stock rises)
      |      /
      |     /
  ────┼────/────────────
      |   /|
      |  / |
      | /  | Protected
      |/___|____________→ Stock Price
         $145 (Put Strike)
         
Max Loss = ($150 - $145) + $5 premium = $10 per share
```

**Key feature:** Downside capped at put strike (minus premium paid)

---

## Protective Put: Detailed Example

### Setup

**Your position:**
- Own 100 shares AAPL, bought at $130
- Current price: $150
- Unrealized gain: $2,000
- Worried about pullback

**Market context:**
- Earnings in 6 weeks
- Market volatile
- Want protection

**Available puts (3 months):**

| Strike | Premium | Protection Level | Max Loss if Crash |
|--------|---------|------------------|-------------------|
| $155 | $8.00 | Above current | -$300 + premium = -$1,100 |
| $150 | $5.50 | At current | -$550 |
| $145 | $3.50 | 3.3% below | -$500 + premium = -$850 |
| $140 | $2.00 | 6.7% below | -$1,000 + premium = -$1,200 |

### Decision: Buy $145 Put for $3.50

**The trade:**
- Buy 1 contract $145 put
- Pay $350
- Expiration: 90 days
- Protection: Below $145

**New position:**
- Long 100 AAPL shares (cost basis $130)
- Long 1 AAPL $145 put (cost $3.50)
- Total capital: $13,000 (stock) + $350 (put) = $13,350

### Scenario 1: Stock Crashes to $120 (Protection Works!)

**Without put:**
- Stock value: $12,000
- Loss from $150: -$3,000
- Loss from original cost: -$1,000
- **Disaster!**

**With protective put:**
- Stock value: $12,000
- Put value: $25 ($145 - $120)
- Put profit: $2,500 - $350 = $2,150
- **Net position: $12,000 + $2,500 = $14,500**
- **Loss from $150: only -$850** (protected!)

**Insurance worked:** Put prevented 67% of the downside!

### Scenario 2: Stock Stays at $150 (Insurance Cost)

**At expiration:**
- Stock: $150 (unchanged)
- Put: worthless (OTM)
- Lost premium: -$350

**Result:**
- Stock value: $15,000
- Less put cost: -$350
- Net: $14,650
- **Cost of insurance: $350 (2.3% of position)**

### Scenario 3: Stock Rises to $170 (Insurance + Upside)

**At expiration:**
- Stock: $170
- Put: worthless
- Stock gain: +$2,000
- Put cost: -$350
- **Net gain: +$1,650**

**Key insight:** Full upside participation (minus insurance cost)

### Scenario 4: Stock Drops to $147 (Near Strike)

**At expiration:**
- Stock: $147
- Put: worthless (just OTM)
- Stock loss: -$300
- Put cost: -$350
- **Net loss: -$650**

**Lesson:** If stock stays near strike, you pay premium but don't use insurance (like car insurance - you pay even if no accident)

---

## What Is a Collar?

**Free insurance by giving up upside:**

### The Structure

**Collar = Long Stock + Long Put + Short Call**

**Example:**
- Own 100 shares AAPL at $150
- Buy $145 put for $3.50
- Sell $160 call for $3.50
- **Net cost: $0 (zero-cost collar)**

**What you've created:**
- Protected below $145 (put)
- Capped above $160 (call)
- No premium paid (call premium = put premium)

### Why Use a Collar?

**Want protection but:**
1. **Don't want to pay premium** (reduce cost)
2. **Willing to cap upside** (accept opportunity cost)
3. **Define range** (know max gain and loss)
4. **Preserve capital** (institutional preference)

**Common uses:**

**1. Lock in profits (zero cost):**
- Stock up significantly
- Want to protect gains
- Don't pay premium
- Accept capped upside

**2. Hold through volatility:**
- Uncertain period (earnings, Fed meeting)
- Want to hold long-term
- Free protection for event

**3. Reduce cost of protection:**
- Protective put too expensive
- Sell call to finance it
- Trade-off accepted

**4. Regulatory/institutional:**
- Pension funds, endowments
- Need hedges but minimize cost
- Defined risk acceptable

### Collar Payoff Diagram

```
    Profit
      ↑
      |    _______ (Capped at $160)
      |   /|
      |  / |
      | /  |
  ────┼/───┼────────
      /|   |
     / |   | Protected
    /  |   |
   /   |___|________→ Stock Price
      $145  $160
```

**Range defined:** Max profit at $160, max loss at $145

---

## Collar: Detailed Example

### Setup

**Your position:**
- Own 1,000 shares of NFLX
- Average cost: $300
- Current price: $400
- Unrealized gain: $100,000
- Want to protect but not pay premium

**Goal:** Protect downside, willing to cap upside

**3-month options:**

| Strike | Type | Premium |
|--------|------|---------|
| $380 | Put | $8.00 |
| $420 | Call | $8.00 |

### The Collar Trade

**Execute:**
- Buy 10 contracts $380 put (pay $8,000)
- Sell 10 contracts $420 call (receive $8,000)
- **Net cost: $0**

**New position:**
- Long 1,000 shares NFLX (cost $300, value $400,000)
- Protected below $380
- Capped above $420
- **Zero-cost hedge!**

### Scenario 1: Stock Crashes to $320 (Protection Works)

**Without collar:**
- Stock value: $320,000
- Loss: -$80,000 (-20%)
- **Painful!**

**With collar:**
- Stock value: $320,000
- Put value: $60 × 1,000 = $60,000
- Call value: $0 (OTM)
- **Total: $380,000**
- **Loss: only -$20,000** (-5%)

**Protected:** Collar saved you $60,000!

### Scenario 2: Stock Stays at $400 (Free Insurance)

**At expiration:**
- Stock: $400
- Put: worthless
- Call: worthless
- **No cost, no benefit**

**Like unused insurance:** Didn't need it, but didn't pay for it either

### Scenario 3: Stock Rises to $450 (Capped Upside)

**Without collar:**
- Stock value: $450,000
- Gain: +$50,000
- **Full upside!**

**With collar:**
- Stock value: $450,000
- Put value: $0
- Call value: -$30 × 1,000 = -$30,000 (must deliver shares at $420)
- **Net: $420,000**
- **Gain: only +$20,000** (capped)

**Trade-off:** Gave up $30,000 upside for free protection

### Scenario 4: Stock at $380 (At Put Strike)

**At expiration:**
- Stock: $380
- Put: worthless (ATM)
- Call: worthless
- **Net: $380,000**

**Breakeven at protection level**

### The Cost Analysis

**Opportunity cost:**
- Missed upside if > $420: Real cost
- Protection if < $380: Real benefit
- **Trade-off:** Free insurance but limited upside

**Time value:**
- Locked in for 3 months
- Can't participate fully if stock moons
- **Accept this constraint**

---

## Strike Selection Strategies

### For Protective Puts

**1. Deep ITM (Conservative):**
- Strike above current price
- Example: Stock $150, buy $155 put
- Very expensive
- Maximum protection
- Use when: Very concerned, can afford premium

**2. ATM (Balanced):**
- Strike = current price
- Example: Stock $150, buy $150 put
- Moderate cost
- Full current value protection
- Use when: Standard hedge

**3. OTM (Economical):**
- Strike below current price
- Example: Stock $150, buy $145 put
- Cheaper premium
- Accept some loss
- Use when: **Most common** (like insurance deductible)

**General rule:** 5-10% OTM is typical (balance cost vs. protection)

### For Collars

**Symmetric collar:**
- Put and call equidistant from current
- Example: Stock $150, buy $145 put, sell $155 call
- Balanced range

**Skewed collar (more upside):**
- Call strike farther out
- Example: Stock $150, buy $145 put, sell $165 call
- Keep more upside
- **Pay net debit** (call premium < put premium)

**Skewed collar (more protection):**
- Put strike closer
- Example: Stock $150, buy $148 put, sell $155 call
- More protection
- **Receive net credit** (call premium > put premium)

---

## Time Selection

### Short-Term (1-3 months)

**Protective puts:**
- Cheaper
- Good for specific events (earnings)
- Need to roll frequently

**Collars:**
- Common for quarterly hedges
- Re-evaluate each quarter

### Medium-Term (3-6 months)

**Most common:**
- Balance cost and protection
- Semi-annual hedging
- Let position develop

### Long-Term (LEAPS: > 1 year)

**For long-term holdings:**
- Very expensive (protective puts)
- But full year of protection
- Institutional preference
- Amortize cost over time

**Example:**
- Own stock long-term
- Buy 2-year LEAPS puts
- Cost 8-12% of stock value
- But 2 years of protection

---

## Protective Put vs. Collar Comparison

| Aspect | Protective Put | Collar |
|--------|---------------|--------|
| **Cost** | Pay premium | Zero (or small) |
| **Downside** | Protected at strike | Protected at put strike |
| **Upside** | **Unlimited** | **Capped at call strike** |
| **Complexity** | Simple (2 legs) | Medium (3 legs) |
| **Flexibility** | Keep all upside | Trade upside for free insurance |
| **Best for** | Strong upside expected | Range-bound expected |
| **Typical use** | Event protection | Long-term hedge |

**When to choose:**

**Protective Put:**
- Expect upside (don't want to cap)
- Can afford premium
- Short-term protection
- Strong conviction on stock

**Collar:**
- Uncertain direction
- Want free hedge
- Accept capped upside
- Institutional constraints

---

## Rolling Strategies

**What to do as expiration approaches:**

### Rolling the Protective Put

**If stock still volatile:**
- Close expiring put
- Open new put (same or different strike)
- Continue protection

**Example:**
- Own AAPL at $150
- 3-month $145 put expiring
- Stock now at $155
- Roll: Close $145 put, buy new $150 put for 3 more months

**Cost:** New premium (ongoing insurance cost)

### Rolling the Collar

**If want to maintain hedge:**
- Close both legs
- Open new collar (adjust strikes)

**Example:**
- Stock at $155 (was $150)
- Old collar: $145 put / $160 call expiring
- New collar: $150 put / $165 call for 3 months
- Adjust strikes upward with stock

**Result:** Protection moves with stock price

### Letting It Expire

**If no longer need protection:**
- Let both put and call expire
- Unhedged position again
- Saves closing costs

---

## Tax Considerations

**Important for real-world application:**

### Protective Puts and Holding Periods

**IRS Rule:** Protective put can suspend holding period for tax purposes

**Impact:**
- Own stock 11 months (almost long-term capital gain)
- Buy protective put
- Holding period **may be suspended**
- Can delay long-term treatment

**Avoid:** Don't buy put if close to 1-year holding period

### Collars and Constructive Sales

**IRS Rule:** Tight collars can trigger "constructive sale"

**Definition:**
- If collar too tight (strikes very close)
- IRS treats as if you sold
- Triggers capital gains tax

**Safe harbor:** Strikes at least 10% apart generally OK

**Example:**
- Stock at $100
- Collar: $95 put / $105 call (10% range)
- Generally safe
- But $98 put / $102 call (4% range) risky

**Consult tax advisor!**

### Wash Sale Rules

**If sell stock at loss then buy protective put:**
- May trigger wash sale
- Loss disallowed
- Complex rules

**Safest:** Close positions, wait 30 days before rehedging

---

## Protective Puts vs. Other Strategies

| Strategy | Cost | Downside | Upside | Complexity |
|----------|------|----------|--------|-----------|
| **Protective Put** | Premium | Protected | Unlimited | Low |
| **Collar** | Zero/Low | Protected | Capped | Medium |
| **Stop Loss** | Free | Realized loss | Unlimited | Low |
| **Diversification** | Free | Reduced | Reduced | Low |
| **Selling** | Free (foregone gains) | None (cash) | None | Low |

**Key differences:**

**Protective Put vs. Stop Loss:**
- Put: Insured, can weather volatility
- Stop: Forced exit, can't recover

**Protective Put vs. Selling:**
- Put: Keep position, pay premium
- Sell: No position, no upside

**Collar vs. Selling:**
- Collar: Capped position, no tax
- Sell: No position, taxes due

---

## Common Mistakes

### Mistake 1: Buying Protection After Crash

❌ **Wrong:**
- Stock crashes 20%
- NOW buy protective put
- "Closing barn door after horse left"

**Why it fails:**
- IV is spiked (expensive)
- Already took loss
- Protecting lower value

✅ **Better:**
- Buy protection BEFORE volatility
- When IV is low
- Anticipate risk

### Mistake 2: Over-Hedging

❌ **Wrong:**
- Own 100 shares
- Buy 5 put contracts (500 shares worth)
- Now net short!

**Why it fails:**
- Over-hedged = bearish bet
- If stock rises, puts lose more than stock gains
- Tail wagging dog

✅ **Better:**
- 1:1 ratio (100 shares = 1 put contract)
- Match exactly
- Pure hedge

### Mistake 3: Collar Too Tight

❌ **Wrong:**
- Stock at $100
- Collar: $99 put / $101 call
- 2% range

**Why it fails:**
- Constructive sale (tax issue)
- No room for stock to move
- Locked in completely

✅ **Better:**
- At least 10-15% range
- Example: $95 put / $110 call
- Room to breathe

### Mistake 4: Ignoring Costs

❌ **Wrong:**
- Buy protective puts every month
- Premium: $500/month = $6,000/year
- Stock value: $15,000
- **Spending 40% annually on insurance!**

**Why it fails:**
- Cost overwhelms protection
- Better to just sell stock

✅ **Better:**
- Calculate annualized cost
- Compare to just holding cash
- Use longer-dated options (less frequent)

### Mistake 5: Not Rolling Before Expiration

❌ **Wrong:**
- Put expires Friday
- Wait until Monday to buy new one
- Weekend gap risk!

**Why it fails:**
- Unprotected over weekend
- Bad news can hit
- Gap down before rehedge

✅ **Better:**
- Roll 1-2 weeks before expiration
- Maintain continuous protection
- No gaps

---

## When to Use Each Strategy

### Use Protective Puts When:

**1. Concentrated position**
- Single stock is 20%+ of portfolio
- Can't sell (lockup, taxes, conviction)
- Need insurance

**2. Event risk**
- Earnings coming
- Regulatory decision
- Known catalyst

**3. Strong upside expected**
- Bullish but prudent
- Want full upside
- Can afford premium

**4. Market timing**
- Worried about market
- Don't want to sell
- Temporary protection

**5. Large unrealized gains**
- Stock up 100%+
- Protect profits
- Not ready to realize gains (taxes)

### Use Collars When:

**1. Free protection desired**
- Can't pay premium
- Accept capped upside
- Institutional constraint

**2. Range-bound expected**
- Stock unlikely to moon
- Downside protection more important
- Trade upside for safety

**3. Long-term hedge**
- Holding multi-year
- Quarterly/annual collars
- Systematic hedging

**4. Pre-liquidity event**
- Stock lockup ending soon
- Want protection until can sell
- Free hedge

**5. Regulatory requirements**
- Must hedge (fiduciary duty)
- Minimize cost
- Defined risk acceptable

---

## Advanced: Costless Collar Adjustments

**Making collars work better:**

### 1. Out-of-the-Money Collar

**Structure:**
- Buy OTM put (e.g., 10% below)
- Sell farther OTM call (e.g., 20% above)
- **Receive net credit**

**Benefits:**
- Get paid to hedge
- More upside room
- Accept deductible

**Example:**
- Stock at $100
- Buy $90 put, sell $125 call
- Net credit: $1.50
- Protection below $90, capped at $125

### 2. Ratio Collar

**Structure:**
- Buy puts
- Sell MORE calls (e.g., 2 calls per 1 put)
- Lower net cost or credit

**Risk:**
- Unlimited upside risk beyond 2nd call strike
- Complex

**Use:** Advanced only

### 3. Rolling Collar

**Strategy:**
- Each quarter, roll collar up with stock
- Locks in gains progressively

**Example:**
- Q1: Stock $100, collar $95/$110
- Q2: Stock $108, collar $100/$118
- Q3: Stock $115, collar $107/$125
- **Ratchet protection upward**

---

## Real-World Examples

### Example 1: Tech Executive with RSUs

**Situation:**
- Executive receives 1,000 shares company stock (vesting)
- Value: $200,000 (stock at $200)
- Concentrated position (50% of net worth)
- 1-year lockup remaining

**Solution: 1-Year Collar**
- Buy 10 contracts $180 put (1 year) = $15,000
- Sell 10 contracts $230 call (1 year) = $15,000
- Net cost: $0

**Result:**
- Protected below $180 (worst case: $180,000)
- Capped at $230 (best case: $230,000)
- Free hedge for lockup period

**Outcome (one year later):**
- Stock at $210
- Collar expires: Put worthless, call worthless
- Free protection for volatile period
- Now can sell/diversify

### Example 2: Retiree with Apple Position

**Situation:**
- Retiree owns 500 AAPL, cost basis $50
- Current price: $180
- Unrealized gain: $65,000
- Don't want to sell (taxes + conviction)
- But worried about recession

**Solution: 6-Month Protective Put**
- Buy 5 contracts $170 put (6 months) = $3,000
- Accept 2.5% cost for protection

**Outcome (if crash):**
- Stock crashes to $140
- Puts worth: $30 × 500 = $15,000
- Put profit: $15,000 - $3,000 = $12,000
- **Net position: $140 stock + $30 puts = $170 × 500 = $85,000**
- Saved $15,000 vs. unhedged!

**Outcome (if no crash):**
- Stock at $190 after 6 months
- Puts expire worthless
- Cost: $3,000 (insurance premium)
- Stock value: $95,000
- **Peace of mind cost: 3.2%**

### Example 3: Startup Employee Pre-IPO

**Situation:**
- Employee at pre-IPO startup
- Owns options to buy 10,000 shares at $10
- Private valuation: $100/share
- IPO in 6 months with 6-month lockup
- After lockup: can sell

**Problem:**
- Stock might crash post-lockup
- Need protection from IPO to end of lockup

**Solution: Forward Collar (at IPO)**
- At IPO: Stock at $120
- Buy 12-month collar: $100 put / $150 call
- Cost: Near zero
- Protects through lockup

**Result:**
- Worst case: $100 × 10,000 = $1M locked in
- Best case: $150 × 10,000 = $1.5M capped
- **Range defined for entire lockup**

---

## What to Remember

### Core Concept

**Protective strategies insure long stock positions:**

**Protective Put:**
$$
\text{Protected Position} = \text{Long Stock} + \text{Long Put}
$$
- Cost: Premium
- Downside: Limited
- Upside: Unlimited

**Collar:**
$$
\text{Collar} = \text{Long Stock} + \text{Long Put} + \text{Short Call}
$$
- Cost: Zero (or small)
- Downside: Limited  
- Upside: Capped

### The Trade-offs

**Protective Put:**
- ✓ Keep all upside
- ✗ Pay premium
- Best when: Expect upside but want insurance

**Collar:**
- ✓ Free (or cheap) protection
- ✗ Upside capped
- Best when: Accept capped gains for free protection

### Strike Selection

**Protective Put:**
- ITM: Maximum protection, expensive
- ATM: Full protection, moderate cost
- **OTM: Typical (5-10% below), cheapest**

**Collar:**
- Symmetric: Equal distance both sides
- More upside: Call farther out (pay debit)
- More protection: Put closer (receive credit)

### Time Selection

**Short-term (1-3 months):**
- Event protection
- Cheaper
- Roll frequently

**Medium-term (3-6 months):**
- **Most common**
- Balance cost and time
- Semi-annual hedging

**Long-term (1+ year):**
- Expensive but comprehensive
- Institutional preference
- Amortize cost

### Success Factors

**For protection to work:**
1. Buy BEFORE volatility spike (when cheap)
2. Size correctly (1:1 ratio)
3. Choose appropriate strikes
4. Roll before expiration (maintain coverage)
5. Calculate cost (annualized %)
6. Accept cost as insurance premium

### Common Mistakes

**Avoid:**
1. Buying after crash (expensive)
2. Over-hedging (more puts than stock)
3. Collar too tight (tax issues)
4. Ignoring costs (40% annual = too much)
5. Gaps in protection (roll early)

### When to Use

**Protective Puts:**
- Concentrated position
- Event risk ahead
- Want full upside
- Can afford premium
- Strong conviction on stock

**Collars:**
- Want free hedge
- Accept capped upside
- Range-bound expected
- Institutional requirements
- Long-term holding

### The Math

**Protective Put Cost:**
$$
\text{Annualized Cost} = \frac{\text{Premium}}{\text{Stock Value}} \times \frac{365}{\text{Days to Expiry}}
$$

**Example:**
- Stock: $10,000
- Premium: $300
- Time: 90 days
- Cost: ($300/$10,000) × (365/90) = **12.2% annualized**

**Rule of thumb:** If > 15% annualized, too expensive

### Tax Warning

**Be aware:**
- Protective puts can suspend holding period
- Tight collars can trigger constructive sale
- Wash sale rules apply
- **Consult tax advisor!**

### Your Strategy Arsenal

**Where this fits:**

```
ELEMENTARY HEDGING:
1. Long Calls/Puts (directional)
2. Protective Put ← Portfolio insurance
3. Collar ← Free insurance
   ↓
INCOME:
4. Covered Calls
5. Cash-Secured Puts
   ↓
INTERMEDIATE:
6. Vertical Spreads
7. Straddles
   ↓
ADVANCED:
8. Delta Hedging, Gamma Scalping, etc.
```

**Protective strategies bridge from simple options to hedging!**

### Practical Wisdom

- **Insurance has a cost** (premium or opportunity cost)
- **Buy before you need it** (not after crash)
- **Continuous coverage** (roll before expiration)
- **1:1 ratio** (match stock position exactly)
- **Calculate annualized cost** (is it worth it?)
- **Tax considerations** (consult advisor)
- **Peace of mind has value** (can't be measured in dollars)

### Final Thought

**Protective strategies are real insurance:**

> "Like car or home insurance, you hope you never need it. You pay premiums (protective put) or accept limitations (collar cap) for protection. Most years, nothing bad happens - premium is 'wasted.' But the one year disaster strikes, insurance saves you. The question isn't whether protection costs money - it's whether the cost is acceptable for your risk tolerance and financial situation. For concentrated positions or large unrealized gains, the cost is usually worth it."

**The truth:**
- Most protective puts expire worthless (like most insurance)
- Cost is real (2-5% quarterly typical)
- But prevents catastrophic loss (that one time)
- **Peace of mind is valuable**
- Allows you to hold winners longer (not forced to sell from fear)

**Master protective strategies before attempting complex hedges!** 🛡️📊
