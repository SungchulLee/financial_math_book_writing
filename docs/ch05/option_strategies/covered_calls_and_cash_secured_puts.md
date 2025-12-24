# Covered Calls and Cash-Secured Puts

**Covered calls and cash-secured puts** are income-generating strategies where you sell options against existing positions (stock or cash) to collect premium, accepting the obligation to potentially sell your stock or buy more stock.

---

## The Core Insight

**The fundamental idea:**
- You own stock or have cash sitting idle
- Other people will PAY you for options
- You can "rent out" your stock or cash
- Collect premium income regularly
- Accept obligation (sell stock or buy stock)
- Lower risk than naked options (you're covered)

**The key equation:**
$$
\text{Income} = \text{Premium Collected} - \text{Opportunity Cost}
$$

**You're essentially betting: "I'm willing to sell my stock at this price (or buy at this price) in exchange for immediate income."**

---

## What Is a Covered Call?

**Definition:** Sell call options against stock you already own.

### The Structure

**What you have:**
- Own 100 shares of stock (per contract)
- Stock sitting in portfolio

**What you do:**
- Sell 1 call option at strike $K$ (typically OTM)
- Collect premium upfront
- Keep premium regardless of outcome

**Your obligation:**
- If stock > strike at expiration → sell stock at strike
- If stock < strike → keep stock and premium
- "Rent out" the upside above strike

### Example

**Position:**
- Own 100 shares AAPL at $150
- Current price: $150

**Trade:**
- Sell $160 call, 1 month expiration
- Collect $2 premium
- Receive $200 immediately

**Outcomes:**

**1. Stock stays below $160:**
- Keep stock
- Keep $200 premium
- Can sell another call next month
- **"Rent collected"**

**2. Stock goes above $160 (e.g., $170):**
- Obligated to sell at $160
- Miss gains above $160
- But still made $10/share capital gain + $2 premium = $12 total
- **Capped upside**

**Payoff diagram:**
```
Profit
   ↑
   |      ‾‾‾‾‾‾
   |     /
   |    /
───┼───/────────→ Stock Price
   | /
   |/
   Stock at $150
   Cap at $162 ($160 + $2 premium)
```

---

## What Is a Cash-Secured Put?

**Definition:** Sell put options while holding cash to buy the stock if assigned.

### The Structure

**What you have:**
- Cash in account (enough to buy 100 shares)
- Want to own stock but at lower price

**What you do:**
- Sell 1 put option at strike $K$ (typically ATM or OTM)
- Collect premium upfront
- Set aside cash to cover assignment

**Your obligation:**
- If stock < strike at expiration → buy stock at strike
- If stock > strike → keep premium, repeat
- "Get paid to place limit order"

### Example

**Position:**
- Have $14,500 cash
- Want to own AAPL but only at $145 or below
- Current price: $150

**Trade:**
- Sell $145 put, 1 month expiration
- Collect $3 premium
- Receive $300 immediately
- Reserve $14,500 for potential purchase

**Outcomes:**

**1. Stock stays above $145:**
- Don't buy stock (not assigned)
- Keep $300 premium
- Can sell another put next month
- **"Payment for willingness to buy"**

**2. Stock drops below $145 (e.g., $140):**
- Obligated to buy at $145
- Net cost: $145 - $3 = $142/share
- Better than $150 original price!
- **Acquired stock at discount**

**Payoff diagram:**
```
Profit
   ↑
   |\
   | \‾‾‾‾‾‾‾
   |  \
───┼───\────────→ Stock Price
   |    \
   |     \
   Floor at $142 ($145 - $3 premium)
```

---

## Why These Strategies Exist

### For Covered Calls

**1. Generate Income on Existing Holdings**
- Own stock long-term (won't sell)
- Stock paying dividends, but want more income
- Covered calls add 1-3% monthly income
- **"Extra yield"**

**2. Willing to Sell at Target Price**
- Bought at $100, stock at $150
- Happy to sell at $160
- Get paid $2 to set limit sell order
- **"Paid to exit"**

**3. Lower Cost Basis**
- Stock purchased at $150
- Sell calls repeatedly, collect $2/month
- After 6 months: effective cost $138
- **Reduce downside risk**

**4. Sideways Market Income**
- Stock range-bound $145-$155
- Sell $160 calls monthly
- Collect premium every month
- **Profit from stagnation**

### For Cash-Secured Puts

**1. Get Paid to Buy Stock**
- Want AAPL but at $140, not $150
- Sell $140 put for $2
- Either: collect $2 and wait, OR buy at $138 net
- **Win either way**

**2. Generate Income on Cash**
- Have $50,000 cash earning 0.5% in savings
- Sell puts, earn 1-2% monthly on cash
- Still have buying power
- **Better cash yield**

**3. Dollar-Cost Averaging**
- Want to accumulate stock over time
- Sell puts monthly at different strikes
- Get assigned periodically
- **Paid to build position**

**4. Bullish But Patient**
- Believe stock will rise long-term
- Don't mind buying dips
- Get paid while waiting
- **Premium + potential ownership**

---

## The Portfolio Structures

### Covered Call

$$
\Pi = \text{Long Stock} - \text{Short Call}
$$

**Position:**
- Long 100 shares at price $S_0$
- Short 1 call at strike $K$
- Received premium $P$

**At expiration:**
$$
\text{P\&L} = \begin{cases}
(S - S_0) + P & \text{if } S \leq K \\
(K - S_0) + P & \text{if } S > K
\end{cases}
$$

**Key insight:** Upside capped at $K + P$, downside still exists (stock can drop)

**Greeks:**
- Delta: Positive but reduced (0.50-0.70 typical)
- Theta: Positive (collect decay from short call)
- Vega: Slightly negative (short call)
- Gamma: Negative (from short call)

### Cash-Secured Put

$$
\Pi = - \text{Short Put} + \text{Cash Reserve}
$$

**Position:**
- Short 1 put at strike $K$
- Received premium $P$
- Hold $K \times 100$ cash in account

**At expiration:**
$$
\text{P\&L} = \begin{cases}
P & \text{if } S \geq K \\
P - (K - S) & \text{if } S < K
\end{cases}
$$

**If assigned:** Buy stock at $K$, net cost = $K - P$

**Greeks:**
- Delta: Positive (bullish position, ~0.30-0.50)
- Theta: Positive (collect decay)
- Vega: Negative (short put)
- Gamma: Negative

---

## Strike Selection

### For Covered Calls

**OTM (Stock < Strike) - Most Common:**
- Strike 5-10% above current price
- Lower premium, but keep stock more likely
- Example: Stock $100, sell $105 call for $1

**ATM (Stock ≈ Strike):**
- Maximum premium
- High probability of assignment
- Use when willing to sell

**ITM (Stock > Strike) - Aggressive:**
- Very high premium
- Almost certainly assigned
- Basically selling stock with extra premium

**Example:**
- Stock at $150

| Strike | Type | Premium | Prob. Keep Stock | Income | Best When |
|--------|------|---------|------------------|--------|-----------|
| $160 | OTM | $1.50 | High | 1% | Want to keep stock |
| $150 | ATM | $4.00 | Medium | 2.7% | Neutral |
| $140 | ITM | $11.00 | Low | 7.3% | Want to sell |

### For Cash-Secured Puts

**OTM (Stock > Strike):**
- Strike below current price
- Lower premium, less likely assigned
- Example: Stock $150, sell $145 put for $2

**ATM (Stock ≈ Strike) - Most Common:**
- Strike at current price
- Balanced premium/probability
- Standard approach

**ITM (Stock < Strike):**
- Strike above current price
- High premium, very likely assigned
- Use when very bullish

---

## Time Frame Selection

**Both strategies:**

**Weekly Options:**
- High premium rate (annualized)
- More management required
- Can collect 52 times/year
- Good for active traders

**Monthly Options (Most Common):**
- Standard 30-45 days
- Balanced premium/management
- Most liquid
- Collect 12 times/year

**Quarterly Options:**
- Less management
- Lower premium rate
- More set-and-forget
- 4 times/year

**Recommendation:** Start with monthly, transition to weekly once experienced

---

## Concrete Example 1: Covered Call Income

**Setup:**

**Position:**
- Own 500 shares of MSFT
- Purchase price: $300/share
- Current price: $350
- Happy with gains, don't want to sell yet
- Want extra income

**Strategy:** Monthly covered calls

**Month 1:**
- Sell 5 contracts of $360 calls (3% OTM)
- 30 days to expiration
- Premium: $5/share = $500/contract
- Total collected: $2,500

**Outcome (Stock ends at $355):**
- Stock didn't reach $360
- Keep stock
- Keep $2,500 premium
- **Return: 0.71% for the month (8.5% annualized)**

**Month 2:**
- Repeat: Sell $365 calls
- Premium: $4.50/share
- Collected: $2,250

**Outcome (Stock ends at $370):**
- Stock above $365 → Assigned
- Sell stock at $365
- Total gain per share: ($365 - $300) + $5 + $4.50 = $74.50
- **Total profit: $37,250 on $150,000 investment (24.8%)**

**If never assigned (full year):**
- Collect average $4/share × 12 months = $48/share
- Stock gains + premiums
- Plus dividends
- **Enhanced returns**

---

## Concrete Example 2: Cash-Secured Put Entry

**Setup:**

**Goal:** Want to own NVDA at $450 or below
**Current price:** $480
**Cash available:** $50,000

**Strategy:** Sell cash-secured puts until assigned

**Month 1:**
- Sell 1 contract $450 put
- 30 days to expiration
- Premium: $12/share = $1,200
- Reserve $45,000 for potential purchase

**Outcome (Stock ends at $470):**
- Not assigned (stock above $450)
- Keep $1,200
- **Return: 2.7% on reserved capital**

**Month 2:**
- Sell $450 put again
- Premium: $10/share = $1,000

**Outcome (Stock ends at $440):**
- **Assigned** - buy 100 shares at $450
- Net cost: $450 - $12 - $10 = $428/share
- Market price: $440
- Already up $12/share (2.8%)
- Now own stock at good entry
- **Can now sell covered calls!**

---

## The "Wheel Strategy"

**Combining both strategies in a cycle:**

### The Complete Cycle

**Step 1: Sell Cash-Secured Puts**
- Target stock you want to own
- Collect premium
- Wait for assignment

**Step 2: Get Assigned**
- Buy stock at strike
- Net cost reduced by premiums collected

**Step 3: Sell Covered Calls**
- Now own stock
- Sell OTM calls
- Collect premium

**Step 4: Get Called Away**
- Stock rises above strike
- Sell stock at strike
- Profit = (strike - original put strike) + all premiums

**Step 5: Repeat**
- Back to cash
- Sell puts again
- Cycle continues

### Example: Full Wheel on AAPL

**Starting capital:** $15,000

**Round 1:**
- Sell $145 put, collect $3 → $300
- Assigned at $145 (net: $142)

**Round 2:**
- Own 100 shares at $142
- Sell $155 call, collect $2 → $200
- Called away at $155

**Profit:** 
- Capital gain: ($155 - $142) × 100 = $1,300
- Premiums: $300 + $200 = $500
- **Total: $1,800 on $14,200 at risk (12.7%)**

**Round 3:**
- Back to cash
- Sell $150 put, collect $3 → $300
- Not assigned, keep premium

**Cumulative:**
- $1,800 + $300 = $2,100
- Time: 3 months
- **Return: ~56% annualized**

**This is why the Wheel is popular!**

---

## Covered Calls vs. Other Strategies

| Strategy | Position | Income | Upside | Downside | Best For |
|----------|----------|--------|--------|----------|----------|
| **Buy & Hold** | Long stock | Dividends only | Unlimited | Unprotected | Long-term bulls |
| **Covered Call** | Stock + short call | Premium + dividends | Capped | Unprotected | Income + modest gains |
| **Protective Put** | Stock + long put | Dividends | Unlimited | Protected | Hedging |
| **Collar** | Stock + short call + long put | Low/none | Capped | Protected | Conservative |
| **Cash-Secured Put** | Cash + short put | Premium | N/A | Obligation to buy | Want to own stock |

---

## Pros and Cons

### Covered Calls - Advantages ✓

**1. Generate income**
- 1-3% monthly common
- 12-36% annualized potential
- Regular cash flow

**2. Reduce cost basis**
- Premium lowers effective purchase price
- Downside cushion
- Break-even improves

**3. Outperform in flat/down markets**
- Collect premium even if stock flat
- Small losses offset by premium

**4. Disciplined exits**
- Forces sell at target price
- Removes emotion
- Can't "bag hold" forever

**5. Lower risk than naked calls**
- Covered by stock ownership
- No margin required
- Defined risk (stock can drop)

### Covered Calls - Disadvantages ✗

**1. Cap upside**
- Miss big runs above strike
- Opportunity cost if stock moons

**2. Downside still exists**
- Premium only small cushion ($2-5 typical)
- Stock can still drop 20-50%
- Not true protection

**3. Tax implications**
- May trigger short-term capital gains
- Complicated tax treatment
- Consult tax advisor

**4. Assignment risk**
- Might be assigned early (dividends)
- Forced to sell at inopportune time
- Administrative hassle

**5. Requires stock ownership**
- Need capital for 100 shares
- Concentrated position risk
- No diversification

### Cash-Secured Puts - Advantages ✓

**1. Get paid to wait**
- Income while waiting for entry
- Better than limit orders
- Win-win outcomes

**2. Acquire at discount**
- Net cost = strike - premiums collected
- Often better than market buying
- Dollar-cost average with premiums

**3. Generate income on cash**
- Better than savings accounts
- 1-3% monthly potential
- Active use of idle cash

**4. No directional bet needed**
- Don't need stock to go up NOW
- Patient approach
- Collect while waiting

### Cash-Secured Puts - Disadvantages ✗

**1. Tie up capital**
- Cash reserved, can't use elsewhere
- Opportunity cost
- Less flexibility

**2. Can be assigned in crash**
- Buy stock as it's falling
- Might continue dropping
- Catch falling knife

**3. Max profit limited**
- Only keep premium
- Miss big moves if not assigned
- No leverage

**4. Obligation to buy**
- MUST have cash available
- Can't change mind
- Forced to deploy capital

---

## When to Use Each

### Covered Calls Work Best When:

**1. Moderately bullish**
- Expect slow grind up
- Not explosive growth
- Steady appreciation

**2. Income priority**
- Already have capital gains
- Want regular income
- Don't need maximum upside

**3. Willing to sell**
- Have profit target
- Not married to stock
- Happy to exit at strike

**4. Flat/range-bound market**
- Consolidation expected
- No clear trend
- Theta decay helps

**5. After big run**
- Stock up 50-100%
- Taking some chips off table
- But want to stay invested

**Avoid when:**
- Expecting huge breakout
- News catalyst pending (earnings, FDA, etc.)
- Stock at critical support (might drop hard)
- Very low IV (premium not worth it)

### Cash-Secured Puts Work Best When:

**1. Want to own stock**
- Identified good company
- Waiting for better entry
- Patient approach

**2. After pullback**
- Stock dropped 10-20%
- Finding support
- Looks oversold

**3. Building position**
- Dollar-cost averaging
- Long-term accumulation
- Not worried about timing

**4. Cash sitting idle**
- Have excess cash
- Want better yield than savings
- Willing to deploy for stock

**5. Moderately bullish market**
- Not crashing
- But not expensive
- Normal conditions

**Avoid when:**
- Bearish overall (don't want to own stock)
- Stock fundamentals deteriorating
- Catching falling knife
- Need cash liquidity soon

---

## Common Mistakes

### For Covered Calls

**1. Selling too far OTM**
- Collect $0.20 premium
- Not worth the cap
- Better to not sell at all

**2. Rolling down and out forever**
- Stock drops, never recover
- Keep selling lower strikes
- End up selling at loss

**3. Ignoring dividends**
- Ex-dividend dates trigger assignment
- Lose dividend
- Assignment surprise

**4. Selling before earnings**
- IV high (tempting)
- But stock could gap up
- Miss huge move

### For Cash-Secured Puts

**1. Not having cash secured**
- Sell put without cash
- Assignment forces margin
- Can't fulfill obligation

**2. Selling on falling knife**
- Stock in free fall
- Keep getting assigned
- Catch bottom of crash

**3. Too aggressive on strikes**
- Sell at current price (ATM)
- Assigned too often
- Buy at tops

**4. Ignoring fundamentals**
- Sell puts on bad company
- "Looks cheap"
- Assigned and stock keeps dropping

---

## Risk Management

### For Covered Calls

**Position sizing:**
- Sell calls on max 50% of holdings
- Keep some shares uncapped
- Don't sell calls on every position

**Strike selection:**
- 5-10% OTM for balance
- ATM only if ready to sell
- Check technical resistance

**Exit discipline:**
- Roll up and out if stock runs
- Or accept assignment
- Don't fight the tape

**Tax planning:**
- Be aware of holding periods
- Consider timing for long-term gains
- Don't let tax tail wag investment dog

### For Cash-Secured Puts

**Position sizing:**
- Max 20-30% of cash in puts
- Keep dry powder
- Don't sell puts on all cash

**Stock selection:**
- Only stocks you WANT to own
- Check fundamentals
- Technical support levels

**Strike selection:**
- 5-10% below current price
- Check support levels
- Not too aggressive

**Assignment planning:**
- Know what you'll do if assigned
- Have follow-up strategy (covered calls?)
- Don't panic if assigned

---

## Real-World Examples

### Example 1: Tesla Covered Calls (2023)

**Setup:**
- Own 200 shares TSLA at $180 (from 2022)
- Stock now at $240 (nice gain)
- Want income but keep exposure

**Trade:** Sell $260 calls monthly
- Month 1: Collect $8 → $1,600
- Stock ends at $245 → Keep stock

- Month 2: Sell $265 calls, collect $7 → $1,400
- Stock ends at $258 → Keep stock

- Month 3: Sell $270 calls, collect $6 → $1,200
- Stock rallies to $280 → **Assigned**

**Result:**
- Sold at $270 (cost $180)
- Capital gain: $90 × 200 = $18,000
- Premiums: $1,600 + $1,400 + $1,200 = $4,200
- **Total: $22,200 profit (61% return)**

**Trade-off:**
- Stock went to $280, missed $10/share = $2,000
- But $4,200 premium more than compensated

### Example 2: Microsoft Cash-Secured Puts (2024)

**Setup:**
- Want to own MSFT
- Trading at $380
- Too expensive, wait for dip

**Month 1:** Sell $360 put
- Collect $8 → $800
- Stock ends at $375 → Not assigned

**Month 2:** Sell $365 put
- Collect $7 → $700
- Stock ends at $370 → Not assigned

**Month 3:** Sell $360 put
- Collect $9 → $900
- Stock drops to $350 → **Assigned**

**Result:**
- Bought at $360
- Net cost: $360 - ($8 + $7 + $9) = $336
- Market price: $350
- Up $14/share already
- Collected $2,400 total in 3 months
- **Now selling covered calls**

**Win-win:**
- Got paid $2,400 while waiting
- Acquired at $336 vs. $380 originally
- $44/share discount (11.6%)

---

## What to Remember

### Core Concepts

**Covered Call:**
- Own stock + sell call = income
- Collect premium, cap upside
- Reduce downside slightly
- Win in flat/small-up markets

**Cash-Secured Put:**
- Hold cash + sell put = income
- Collect premium, obligated to buy
- Net cost = strike - premiums
- Get paid to place limit order

### When to Use

**Covered Calls:**
- Own stock long-term
- Want extra income
- Willing to sell at target
- Flat or slow-rising market

**Cash-Secured Puts:**
- Want to own stock
- Patient for entry
- Cash sitting idle
- Bullish but not urgently

### The Wheel

**Complete strategy cycle:**
1. Sell puts → collect premium
2. Get assigned → buy stock
3. Sell calls → collect premium
4. Get called away → sell stock
5. Repeat → continuous income

**Can generate 20-40% annualized returns**

### Risk Management

**Both strategies:**
- Start with 1-2 positions
- Use liquid, quality stocks
- Check IV before selling
- Have assignment plan
- Don't overtrade

### Comparison

| Aspect | Covered Call | Cash-Secured Put |
|--------|--------------|------------------|
| **Requirement** | Own stock | Have cash |
| **Income** | Premium | Premium |
| **Risk** | Stock can drop | Must buy stock |
| **Goal** | Enhance returns | Acquire at discount |
| **Bias** | Neutral/slightly bullish | Bullish |
| **Assignment** | Sell stock | Buy stock |

### Final Wisdom

> "Covered calls and cash-secured puts are the most conservative options strategies besides protective puts. They generate income from assets you already have (stock or cash) and have defined risks. Many retail investors use these exclusively and never touch complex strategies. Master these before attempting anything riskier. The wheel strategy can be an entire trading system by itself."

**Keys to success:**
- Quality stocks only (you might own them!)
- Conservative strikes (5-10% OTM)
- Monthly timeframe (balance income/management)
- Accept assignment gracefully
- Think long-term (income compounds)
- Use wheel strategy for complete system

**Most important:** These are INCOME strategies, not get-rich-quick schemes. Consistent 1-2% monthly adds up over time. 20-30% annual returns are excellent and achievable with discipline. 🎯💰
