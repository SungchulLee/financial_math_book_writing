# Ratio Spreads


**Ratio spreads** are unbalanced option strategies where you buy and sell different numbers of options at different strikes, creating positions with directional bias, limited cost, but potential unlimited risk on one side.

---

## The Core Insight


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/concrete_example_ratio_spreads.png?raw=true" alt="concrete_example_ratio_spreads" width="700">
</p>

**The fundamental idea:**

- You have a directional view (bullish or bearish)

- But want to reduce cost (or receive credit)

- Sell MORE options than you buy

- Unbalanced position (not 1:1 ratio)

- Accept unlimited risk beyond a point for cheaper entry

**The key equation:**

$$
\text{Ratio Spread} = \text{Buy N options} + \text{Sell M options (where M > N)}
$$

Typical ratios: 1:2, 1:3, 2:3

**You're essentially betting: "The stock will move moderately in my direction, but NOT too far - I'll profit from the move while collecting premium to reduce cost."**

---

## What Is a Ratio


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/synthetic_long_stock_ratio_spreads.png?raw=true" alt="synthetic_long_stock_ratio_spreads" width="700">
</p>

**The unbalanced strategy:**

### 1. The Basic


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/synthetic_short_stock_ratio_spreads.png?raw=true" alt="synthetic_short_stock_ratio_spreads" width="700">
</p>

**Call Ratio Spread (Bullish with cap):**

- Buy 1 ITM or ATM call

- Sell 2 (or more) OTM calls

- Net debit or credit depending on strikes/ratio

**Example:**

- Stock at $100

- Buy 1 × $100 call for $5

- Sell 2 × $110 calls for $2 each (receive $4)

- Net cost: $1 debit (or could be credit with different strikes)

**What you've created:**

- Profit if stock rises moderately (to $110)

- Max profit at upper short strike ($110)

- **Unlimited risk if stock goes way above** ($110+)

- Cheaper than buying call alone

**Put Ratio Spread (Bearish with cap):**

- Buy 1 OTM or ATM put

- Sell 2 (or more) OTM puts (lower strikes)

- Net debit or credit

**Example:**

- Stock at $100

- Buy 1 × $100 put for $5

- Sell 2 × $90 puts for $2 each (receive $4)

- Net cost: $1 debit

- **Unlimited risk if stock crashes below $90**

### 2. The Key


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/synthetic_components_breakdown_ratio_spreads.png?raw=true" alt="synthetic_components_breakdown_ratio_spreads" width="700">
</p>

**Unbalanced = Unlimited Risk:**

Unlike vertical spreads (1:1 ratio):

- Vertical: Buy 1, sell 1 → defined risk both sides

- Ratio: Buy 1, sell 2 → **UNCOVERED short options beyond a point**

**This is the danger and opportunity:**

- Cheaper entry (collect extra premium)

- But naked short exposure at extremes

- **Must manage actively**

---

## Call Ratio Spread


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/synthetic_vs_stock_comparison_ratio_spreads.png?raw=true" alt="synthetic_vs_stock_comparison_ratio_spreads" width="700">
</p>

### 1. The Structure


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/put_call_parity_ratio_spreads.png?raw=true" alt="put_call_parity_ratio_spreads" width="700">
</p>

**Standard 1:2 call ratio spread:**

**Position:**

- Long 1 call at $K_1$ (lower strike)

- Short 2 calls at $K_2$ (higher strike, where $K_2 > K_1$)

**Example:**

- Long 1 × $100 call @ $6

- Short 2 × $110 calls @ $2.50 each

- Net: $6 - $5 = **$1 debit**

### 2. Payoff Analysis


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/conversion_relationships_ratio_spreads.png?raw=true" alt="conversion_relationships_ratio_spreads" width="700">
</p>

**Below $100:**

- All calls worthless

- Loss: $1 (net debit)

**At $105:**

- Long call: $5 value

- Short calls: $0

- P&L: $5 - $1 = **+$4 profit**

**At $110 (MAX PROFIT):**

- Long call: $10 value

- Short calls: $0 (ATM, expire worthless)

- P&L: $10 - $1 = **+$9 profit (900% ROI!)**

**At $115:**

- Long call: $15 value

- Short calls: -$10 ($5 each × 2 = -$10)

- P&L: $15 - $10 - $1 = **+$4 profit**

**At $120 (Breakeven point):**

- Long call: $20

- Short calls: -$20 ($10 each × 2)

- P&L: $20 - $20 - $1 = **-$1 (breakeven)**

**Above $120:**

- **UNLIMITED LOSS**

- For every $1 stock rises, lose $1

- No protection!

### 3. Payoff Diagram


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/strike_selection_synthetics_ratio_spreads.png?raw=true" alt="strike_selection_synthetics_ratio_spreads" width="700">
</p>

```
    Profit
      ↑
     9 |      /\
     8 |     /  \
     6 |    /    \
     4 |   /      \___
     2 |  /          \
  ────0┼─/────────────\────→ Stock Price

    -1 |/              \
       100  110  120   \
                        ↓
                   (Unlimited loss)
```

**Sweet spot:** Stock at $110 (upper short strike)

**Danger zone:** Stock above $120 (upper breakeven)

### 4. The Math


**Maximum profit:**

$$
\text{Max Profit} = (K_2 - K_1) - \text{Net Debit}
$$

Or if credit:

$$
\text{Max Profit} = (K_2 - K_1) + \text{Net Credit}
$$

**Upper breakeven:**

$$
\text{Upper BE} = K_2 + \frac{(K_2 - K_1) - \text{Net Debit}}{\text{Ratio} - 1}
$$

For 1:2 ratio:

$$
\text{Upper BE} = K_2 + (K_2 - K_1) - \text{Net Debit}
$$

**Example:**

- Long $100, short 2 × $110, cost $1

- Max profit: $10 - $1 = $9 (at $110)

- Upper BE: $110 + $10 - $1 = $119

---

## Put Ratio Spread


### 1. The Structure


**Standard 1:2 put ratio spread:**

**Position:**

- Long 1 put at $K_1$ (higher strike)

- Short 2 puts at $K_2$ (lower strike, where $K_2 < K_1$)

**Example:**

- Long 1 × $100 put @ $6

- Short 2 × $90 puts @ $2.50 each

- Net: $6 - $5 = **$1 debit**

### 2. Payoff Analysis


**Above $100:**

- All puts worthless

- Loss: $1 (net debit)

**At $95:**

- Long put: $5 value

- Short puts: $0

- P&L: $5 - $1 = **+$4 profit**

**At $90 (MAX PROFIT):**

- Long put: $10 value

- Short puts: $0 (ATM)

- P&L: $10 - $1 = **+$9 profit**

**At $85:**

- Long put: $15 value

- Short puts: -$10 ($5 each × 2)

- P&L: $15 - $10 - $1 = **+$4 profit**

**At $80 (Breakeven):**

- Long put: $20

- Short puts: -$20 ($10 each × 2)

- P&L: $20 - $20 - $1 = **-$1 (breakeven)**

**Below $80:**

- **UNLIMITED LOSS** (stock can go to $0)

- Very dangerous!

### 3. Payoff Diagram


```
    Profit
      ↑
     9 |      /\
     8 |     /  \
     6 |    /    \
     4 |   /      \___
     2 |  /          \
  ────0┼─/────────────\────→ Stock Price

    -1 |/              \
       80   90  100    ↓
      ↓               (Calls continue)
   (Puts: unlimited loss to $0)
```

**Sweet spot:** Stock at $90 (lower short strike)

**Danger zone:** Stock below $80 (lower breakeven)

---

## Types of Ratio



---

## Economic Foundations
**Understanding what this strategy REALLY represents economically:**

### 1. The Core Economic Logic
**What you're trading:**

Ratio spreads represent a fundamental bargain with the market:

$$
\text{Ratio Spread} = \text{Directional Exposure} + \text{Premium Collection} - \text{Tail Risk}
$$

**The economic exchange:**

- **You give up:** Safety from extreme moves (uncovered short options)

- **You receive:** Cheaper directional exposure (premium from extra shorts)

- **You bet on:** Moderate move, not extreme move

This is fundamentally different from vertical spreads where you PAY for defined risk. Here you ACCEPT unlimited risk to reduce cost.

---

### 2. The Premium


**Why selling extra options makes this cheaper:**

When you buy 1 call and sell 2 calls, the premium dynamics:

**Long 1 × $100 call:** Pay $6 (establish long position)

**Short 2 × $110 calls:** Collect $5 (2 × $2.50)

**Net:** Pay only $1 instead of $6!

**The economic insight:**

You're not getting free money - you're selling insurance on extreme upside. Those 2 short calls represent:

- Obligations to deliver stock at $110

- 1 is "covered" by your long $100 call

- 1 is NAKED (unlimited risk)

**Market makers price these shorts based on:**

- Probability of stock exceeding $110

- Volatility expectations

- Supply/demand for upside exposure

When IV is high, you collect more premium (better entry point).

---

### 3. The Probability


**What you're actually betting on:**

Stock returns follow (approximately) normal distribution. Ratio spreads are bets on WHERE in the distribution stock lands:

```
        Probability Density
              ↑
              |    /‾‾‾\
              |   /     \
              |  /       \
              | /         \___
          ────|/──|────|─────|\────→ Price
           Loss  Profit Zone  | Loss
           Zone  (Sweet Spot)  |(Danger!)
                   ↑
              Max profit here
```

**Economic interpretation:**

**Zone 1 (Stock < $100):** Small loss (debit paid)

- You were wrong on direction

- Limited loss (max = debit)

**Zone 2 (Stock $100-$110):** PROFIT

- You were right on direction

- Move was moderate (perfect!)

- Max profit at $110

**Zone 3 (Stock $110-$120):** Declining profit

- You were right but it's moving too far

- Naked short starting to hurt

**Zone 4 (Stock > $120):** UNLIMITED LOSS

- You were "too right" (paradox!)

- Naked short explodes

- Every $1 up = $1 loss

**The economic irony:** Being MORE correct can cost you MORE money!

---

### 4. Why This


**Market participants with different needs:**

**You (Ratio Spread Trader):**

- Want directional exposure cheap

- Confident about moderate move

- Willing to accept tail risk

**Option Buyers (Buying your shorts):**

- Want lottery ticket upside

- Paying premium for extreme scenarios

- Hedging or speculating on breakout

**Market makers:**

- Facilitate both sides

- Collect bid-ask spread

- Hedge their net exposure

**The economic equilibrium:**

Ratio spreads exist because:

1. Some traders want cheap directional plays

2. Others are willing to pay for extreme upside protection

3. This creates a natural market

**When are they economically attractive?**

- IV elevated (collect more premium)

- Stock in trading range (lower extreme move probability)

- Post-earnings (IV crush expected)

---

### 5. Professional


**How institutions use ratio spreads:**

**Rarely!** Most institutions avoid them because:

1. **Risk management:** Unlimited risk hard to justify

2. **Regulation:** Many funds prohibited from undefined risk

3. **Alternatives:** Verticals offer similar exposure, defined risk

**When they DO use them:**

- **Portfolio hedging:** Sell ratio spreads against long stock positions

- **Premium harvesting:** In very high IV, collect premium systematically  

- **Relative value:** Paired with other strategies to create synthetic positions

**Example: Covered call ratio spread:**

- Own 200 shares at $100

- Sell 3 × $110 calls

- Net: 100 shares covered, 1 call "naked" but effectively covered by shares

- Collect premium, participate in upside to $110

---

### 6. The Capital


**Why "cheap" can be expensive:**

**Scenario A: Buy $100 call for $6**

- Capital at risk: $600 per contract

- Max loss: $600

- Defined risk

**Scenario B: Ratio spread (1:2) for $1 debit**

- Capital at risk: $100 per contract (apparent)

- Max loss: **UNLIMITED** (actual)

- Undefined risk

**The trap:**

Ratio spread LOOKS 6× cheaper ($1 vs $6). But the REAL cost is potentially infinite!

**Economic truth:**
$$
\text{True Cost} = \text{Debit Paid} + \text{Expected Value of Tail Loss}
$$

If tail loss probability is 5% and average tail loss is $2,000:
$$
\text{True Cost} = \$100 + (0.05 \times \$2,000) = \$200
$$

Suddenly not so cheap!

---

### 7. When The


**Optimal conditions:**

1. **High IV (>60th percentile)**

   - Collect substantial premium from shorts

   - Economic value: $2-3 extra per short call

2. **Range-bound stock**

   - Low probability of extreme move

   - Historical volatility < Implied volatility (IV > HV)

3. **Post-event setup**

   - After earnings, IV elevated but event risk gone

   - Can capture IV crush + theta decay

4. **Large-cap, stable stocks**

   - KO, PG, JNJ type stocks (not TSLA, GME!)

   - Lower gap/extreme move risk

**Economic calculation:**

For a fair ratio spread, you want:
$$
\text{Premium Collected} > \text{Expected Tail Loss} + \text{Risk Premium}
$$

If expected tail loss (probability × magnitude) is $50, and you want 3:1 risk premium:
$$
\text{Premium Needed} > \$50 + 3 \times \$50 = \$200
$$

Most ratio spreads DON'T meet this threshold!

---

### 8. The Hidden Costs


**Beyond the obvious debit/credit:**

1. **Margin requirements:**

   - Naked short requires margin

   - Can be 20-30% of stock value

   - Ties up capital

2. **Assignment risk:**

   - Short calls can be assigned early

   - Especially near ex-dividend

   - Creates unwanted stock position

3. **Adjustment costs:**

   - When threatened, must adjust

   - Transaction costs, slippage

   - $50-100 per adjustment

4. **Opportunity cost:**

   - Capital tied up in margin

   - Could be deployed elsewhere

   - Mental energy monitoring position

5. **Black swan risk:**

   - Buyout announcements

   - Surprise FDA approvals

   - Geopolitical events

   - Can gap stock 30%+ overnight

**True economic cost:**
$$
\text{Total Cost} = \text{Debit} + \text{Margin} + \text{Adjustments} + \text{Opportunity} + \text{Black Swan Risk}
$$

Often makes defined-risk strategies cheaper in reality!

---

### 9. Economic


**Ratio spread vs. Vertical spread:**

**Ratio (1:2): Buy $100, Sell 2 × $110 for $1 debit**

- Economic cost: $100 + tail risk

- Max profit: $900 (at $110)

- ROI: 900% (apparent), but with unlimited downside

**Vertical: Buy $100, Sell 1 × $110 for $4 debit**

- Economic cost: $400 (defined)

- Max profit: $600 (at $110+)

- ROI: 150% (defined risk)

**Economic truth:** Vertical is often CHEAPER when you factor in:

- No margin requirement

- No tail risk

- No adjustment costs

- Sleep-at-night value

**Break-even analysis:**

Ratio spread is economically superior ONLY if:
$$
P(\text{Stock in profit zone}) \times \$900 > P(\text{Tail event}) \times \$2000 + \$400
$$

If P(profit zone) = 40%, P(tail) = 10%:
$$
0.40 \times \$900 = \$360 < 0.10 \times \$2000 + \$400 = \$600
$$

**Vertical is economically superior in this case!**

---

### 10. The Volatility


**Why IV matters for ratio spreads:**

Options at different strikes have different IVs (volatility smile/skew):

**Typical call option skew:**

- ATM calls: 30% IV

- OTM calls (+$10): 28% IV  

- Further OTM (+$20): 26% IV

**Economic impact on ratio spreads:**

When you sell OTM calls, you're selling at LOWER IV than you're buying. This is economically unfavorable!

**Example:**

- Buy $100 call at 30% IV: $6.00

- Sell $110 calls at 28% IV: $2.30 each (not $2.50!)

- Net debit: $1.40 (not $1.00)

**Economic insight:** Volatility skew makes ratio spreads LESS attractive than naive pricing suggests.

**When is skew favorable?**

- After earnings (skew flattens)

- High IV environment (all strikes elevated)

- When selling near-ATM (less skew effect)

---

### 11. Final Economic


**The fundamental equation:**

$$
\text{Ratio Spread Value} = \text{Directional Edge} + \text{Volatility Edge} - \text{Tail Risk} - \text{Hidden Costs}
$$

**For ratio spreads to be economically rational:**

1. You must have STRONG directional conviction (not just "sorta bullish")

2. You must believe extreme moves are VERY unlikely (<5% probability)

3. IV must be elevated (collect meaningful premium)

4. Hidden costs must be acceptable

5. You must SIZE appropriately (tail risk manageable)

**Economic reality:** Most traders overestimate (1) and (2), underestimate (5).

**The harsh economic truth:**

> "Ratio spreads are economically attractive in theory - you get paid to take on tail risk that seems unlikely. But in practice, tail events happen MORE often than pricing suggests (fat tails), hidden costs accumulate, and one black swan wipes out 20 winning trades. The economic value is often illusory - you're picking up pennies in front of a steamroller, and the steamroller is faster than you think."

**Bottom line:** From a pure economic perspective, most traders are better off paying the higher premium for defined-risk strategies. The "savings" from ratio spreads are usually false economy.

---


**Understanding what this strategy REALLY represents economically:**

### 12. The Core


This strategy involves specific economic trade-offs that determine when it's most valuable. The key is understanding what you're giving up versus what you're gaining in economic terms.

**Economic equivalence:**

$$
\text{Strategy Payoff} = \text{Component 1} + \text{Component 2} - \text{Cost/Benefit}
$$

### 13. Why This


Markets create these structures because different participants have different:

- Risk preferences

- Time horizons

- Capital constraints

- View on volatility vs. direction

### 14. Professional


Institutional traders view this strategy as a tool for:

1. **Risk management:** Precise control over exposure

2. **Capital efficiency:** Optimal use of buying power

3. **Probability engineering:** Trading win rate for win size

4. **Volatility positioning:** Specific exposure to implied volatility changes

Understanding the economic foundations helps you recognize when the strategy offers genuine edge versus when market pricing is fair.


### 15. Standard Ratio


**Most common:**

- Buy 1, sell 2

- Moderate risk/reward

- Typical use

### 16. Aggressive Ratio


**Higher risk:**

- Buy 1, sell 3 or more

- **More naked exposure**

- Cheaper or larger credit

- Higher max profit

- Much riskier

**Example:**

- Buy 1 × $100 call

- Sell 3 × $110 calls

- **Very dangerous if stock moons**

### 17. Conservative


**Lower risk:**

- Buy 2, sell 3

- Less naked exposure (only 1 uncovered)

- More expensive

- Safer

**Example:**

- Buy 2 × $100 calls

- Sell 3 × $110 calls

- Only 1 call uncovered

### 18. Ratio Call


**Receive money upfront:**

- Strikes chosen so net credit

- Example: Buy $105, sell 2 × $115

- Receive $1 credit

- Free trade (profit if in range)

**Danger:** Still unlimited risk above breakeven!

### 19. Ratio Put Spread


**Receive money upfront:**

- Buy $95 put, sell 2 × $85 puts

- Receive credit

- Free trade

- **Still unlimited risk below breakeven**

---

## Concrete Example


**Complete walkthrough:**

### 1. Setup


- **Stock:** TSLA at $250

- **View:** Moderately bullish - expect rise to $270-280, but not $300+

- **Strategy:** 45-day call ratio spread

- **Implied Vol:** 50% (moderate)

### 2. Available Options


| Strike | Call Premium |
|--------|--------------|
| $250 | $15.00 |
| $270 | $7.00 |
| $280 | $4.00 |

### 3. The Trade


**Execute:**

- Buy 1 × $250 call @ $15.00

- Sell 2 × $270 calls @ $7.00 each = $14.00 received

- **Net debit: $1.00** ($100 total)

**Position summary:**

- Cost: $100

- Max profit: $1,900 (at $270)

- Max loss (downside): $100

- Max loss (upside): UNLIMITED (above $289)

- Upper breakeven: $289

### 4. At expiration:


**At expiration:**

- TSLA exactly at $270

- $250 call worth: $20 ($2,000)

- $270 calls worth: $0 (ATM, expire worthless)

- **P&L: $2,000 - $100 = +$1,900 (1,900% ROI!)**

**Perfect outcome:** Stock at upper short strike

### 5. At expiration:


**At expiration:**

- TSLA at $265

- $250 call worth: $15 ($1,500)

- $270 calls worth: $0

- **P&L: $1,500 - $100 = +$1,400**

**Still very profitable**

### 6. At expiration:


**At expiration:**

- TSLA at $260

- $250 call worth: $10 ($1,000)

- $270 calls worth: $0

- **P&L: $1,000 - $100 = +$900**

**Decent profit**

### 7. At expiration:


**At expiration:**

- TSLA at $300 (big rally)

- $250 call worth: $50 ($5,000)

- $270 calls worth: -$60 ($30 × 2 = -$6,000)

- **P&L: $5,000 - $6,000 - $100 = -$1,100**

**Loss! Stock moved TOO MUCH**

### 8. At expiration:


**At expiration:**

- TSLA at $350 (massive rally)

- $250 call worth: $100 ($10,000)

- $270 calls worth: -$160 ($80 × 2 = -$16,000)

- **P&L: $10,000 - $16,000 - $100 = -$6,100**

**Catastrophic loss from being right on direction!**

**This is the ratio spread paradox: Can lose money from being "too right"**

### 9. Management


**After 20 days:**

- TSLA now at $280 (moving up quickly)

- Near danger zone

- **Decision: Close the spread**

- Exit for small profit/loss rather than risk unlimited loss

**This is why active management is critical!**

**Figure 1:** TSLA call ratio spread example showing all five scenarios from perfect (stock at $270) to disaster (stock at $350), illustrating the critical paradox of ratio spreads where being "too right" on direction leads to unlimited losses, demonstrating why strict risk management and active monitoring are essential.

---


## Real-World Examples


**Concrete scenarios showing ratio spreads in practice:**

### 1. Pension Duration


**Setup:**

- AAPL at $170 after iPhone earnings

- IV: 45% (60th percentile - elevated)

- Expectation: Modest drift to $175-180, then consolidate

- 45 DTE

**Trade: 1:2 call ratio spread**

- Buy 1 × $170 call @ $7.50

- Sell 2 × $180 calls @ $3.00 each

- **Net debit: $1.50 ($150 per contract)**

**Position metrics:**

- Max profit: $8.50 at $180 (567% ROI!)

- Breakeven: $161.50 (downside), $188.50 (upside)

- Danger zone: > $188.50 (unlimited loss)

- Margin required: ~$3,400 per contract

**Week-by-week:**

**Week 1:** AAPL at $172

- Position value: $3.20

- P&L: +$170 (113% gain)

- Looking good!

**Week 2:** AAPL at $176

- Position value: $5.80

- P&L: +$430 (287% gain)

- Approaching target

**Week 3:** AAPL at $178

- Position value: $7.50

- P&L: +$600 (400% gain)

- Near max profit zone

**Week 4 (30 DTE):** AAPL at $179

- Position value: $8.20

- P&L: +$670 (447% gain)

- **Decision: CLOSE** (96% of max profit)

**Why close at 96%?**

- Remaining upside: $30

- Remaining risk: UNLIMITED if AAPL gaps above $188.50

- Risk/reward: Terrible (risk thousands for $30)

**Final result:**

- Return: +447% in 15 days

- Annualized: >10,000% (meaningless, but impressive)

**Why this worked:**

1. ✅ High IV entry (volatility crushed after)

2. ✅ Stock moved exactly to target ($180)

3. ✅ Closed before extreme upside risk

4. ✅ No surprises (no buyouts, no black swans)

5. ✅ Disciplined exit (didn't chase last 4%)

**Key lesson:** This is the dream scenario. Happens maybe 20-30% of the time. Enjoy it when it does!

---

### 2. Transition Risk


**Setup:**

- NVDA at $400 in AI boom

- Trader thinks: "It'll go to $450 max"

- IV: 55% (elevated from AI hype)

- 60 DTE

**Trade: 1:2 call ratio spread**

- Buy 1 × $400 call @ $32

- Sell 2 × $450 calls @ $12 each

- **Net debit: $8 ($800 per contract)**

- **Size: 10 contracts = $8,000 risk**

**Position metrics:**

- Max profit: $42 at $450 = **$4,200 per contract**

- Upper breakeven: $492

- Trader thinks: "NVDA won't hit $492, that's 23% up!"

**Week 1:** NVDA rallies to $420

- Position: +$1,500 total (19% gain)

- Trader: "Perfect! As planned!"

**Week 2:** NVDA at $440

- Position: +$2,800 (35% gain)  

- Trader: "Even better! Close to max profit zone!"

**Week 3:** NVDA at $460

- **Above target, but still below breakeven**

- Position: +$2,200 (declining from max)

- Trader: "Hmm, it went a bit far. But still profitable!"

- **Critical mistake: Didn't exit**

**Week 4:** AI hype intensifies

- NVDA gaps to $490 on massive volume (AI chip shortage news)

- **Now at upper breakeven!**

- Position: +$200 (went from +$2,800 to near break-even)

- Trader: "Oh no... should I close?"

- **Waits, hoping for pullback**

**Week 5:** NVDA continues to $520

- **$28 past breakeven = $2,800 loss per contract**

- Total position: -$28,000 (10 contracts)

- **From +$2,800 profit to -$28,000 loss!**

- Trader finally panics and closes

**The "too right" effect:**

- Was CORRECT: NVDA did rally (bullish thesis right!)

- But was TOO correct: 30% rally vs. expected 12.5%

- Result: Massive loss from being "too right"

**What went wrong:**

1. ❌ **No stop loss at upper breakeven** ($492)

2. ❌ **Didn't exit when above target** (should've closed at $460)

3. ❌ **Over-sized** (10 contracts = $8,000 initial risk, but INFINITE actual risk)

4. ❌ **Didn't respect unlimited risk** (hoped for pullback)

5. ❌ **Wrong stock choice** (NVDA in AI boom = extreme mover)

**Key lesson:** Being right on direction means NOTHING if stock goes too far. Always have hard stop at upper breakeven!

---

### 3. Portable Alpha


**Setup:**

- TSLA at $245 before earnings

- Trader thinks: "Earnings will be okay, stock goes to $260"

- IV: 75% (very high pre-earnings)

- 30 DTE (earnings in 5 days)

**Trade: 1:2 call ratio spread**

- Buy 1 × $245 call @ $18

- Sell 2 × $260 calls @ $8 each

- **Net debit: $2 ($200 per contract)**

**The mistake:** Holding through earnings!

**Earnings night:**

- TSLA reports massive beat

- **Stock gaps to $295 overnight** (+20%!)

- Market opens, trader checks position...

**Position value:**

- Long $245 call: Worth $50 (+$32 from entry)

- Short 2 × $260 calls: Worth -$70 (-$35 each)

- **Net: $50 - $70 = -$20 per share**

- **Loss: -$2,000 per contract!**

**But wait, it gets worse:**

- Trader had 5 contracts

- **Total loss: -$10,000**

- This was 20% of their $50,000 account

**The cascade:**

- Account now at $40,000

- Margin call triggered

- Forced to liquidate other positions

- Psychological damage: Won't trade for months

**What went wrong:**

1. ❌ **CARDINAL SIN: Held through earnings**

2. ❌ **Underestimated gap risk** (TSLA routinely gaps 15-20% on earnings)

3. ❌ **Over-sized** (20% of account in ONE position)

4. ❌ **Wrong stock** (TSLA = highest volatility)

5. ❌ **Ignored warnings** (75% IV should've been red flag)

**What should've happened:**

- Close position 2 days before earnings

- Take whatever profit/loss exists

- Avoid the gap risk entirely

**Key lesson:** NEVER, EVER hold ratio spreads through earnings. The gap risk is exactly what destroys these positions!

---

### 4. Tactical Duration


**Setup:**

- SPY at $450 post-FOMC meeting

- IV: 22% (68th percentile - elevated after Fed uncertainty)

- Expectation: Market stabilizes, IV crushes, modest drift

- 40 DTE

**Trade: 1:2 call ratio spread**

- Buy 1 × $450 call @ $8.50

- Sell 2 × $460 calls @ $3.00 each

- **Net debit: $2.50 ($250 per contract)**

**Position:** 4 contracts = $1,000 risk

**Why this trade was smart:**

- High IV (collect good premium)

- Post-event (no binary catalysts ahead)

- SPY (stable, liquid, unlikely to gap 10%)

- Wide strikes ($10 apart = room to work)

**Week 1:** SPY drifts to $452

- IV drops to 19% (vega profit!)

- Position: +$180 (18% gain)

**Week 2:** SPY at $454

- IV: 17%

- Position: +$420 (42% gain)

- Theta accelerating

**Week 3:** SPY at $456

- IV: 16%

- Position: +$720 (72% gain)

**Week 4 (26 DTE):** SPY at $458

- IV: 15%

- Position: +$960 (96% gain)

- **Decision: CLOSE** (close to max profit of $1,000)

**Why close here?**

- 96% of max profit captured

- Still 26 DTE (theta working, but gamma risk rising)

- SPY at $458 getting close to $460 (danger starts at $470 breakeven)

- Take the win!

**Final result:**

- Return: +96% in 14 days

- No stress (SPY never threatened upper breakeven)

- Clean trade

**Why this worked:**

1. ✅ High IV entry → IV crush profit

2. ✅ Stable underlying (SPY not TSLA)

3. ✅ Post-catalyst timing (Fed done)

4. ✅ Proper sizing (4 contracts, $1,000 risk)

5. ✅ Wide strikes ($10 buffer)

6. ✅ Disciplined exit (96% is close enough!)

**Key lesson:** This is the IDEAL ratio spread setup. High IV, stable underlying, post-event, wide strikes, small size!

---

### 5. Duration Hedge


**Setup:**

- DIS at $95 in Q2

- Expectation: Theme parks boost, stock to $100-105

- IV: 38% (52nd percentile)

- 50 DTE

**Trade: 1:2 call ratio spread**

- Buy 1 × $95 call @ $6.00

- Sell 2 × $105 calls @ $2.20 each

- **Net debit: $1.60 ($160 per contract)**

- Size: 3 contracts

**Week 1-2:** DIS drifts to $98

- Position: +$120 (25% gain)

- On track!

**Week 3:** Streaming subscriber miss announced

- DIS drops to $93

- Position: -$90 (-19% loss)

- Trader: "I'll wait, earnings coming up..."

**Week 4:** DIS continues weak to $91

- Position: -$130 (-27% loss)

- **Decision point: Exit or hold?**

**Trader decides to ADJUST:**

**Adjustment: Roll down**

- Close original 1:2 ($95/$105)

- Open new 1:2 ($90/$100)

- Additional cost: $120

**New position:**

- Total invested: $280 per contract

- New max profit: $880 at $100

- New upper BE: $108.80

**Week 5-6:** DIS recovers to $97

- Position: +$240 (86% gain on total capital)

- Looking better!

**Week 7 (18 DTE):** DIS at $99

- Position: +$340 (121% gain)

- **Decision: CLOSE**

**Why close?**

- Made back losses + profit

- Getting close to expiration (18 DTE = gamma risk)

- Target ($100) nearly hit

- Don't be greedy

**Final result:**

- Return: +121% accounting for adjustment cost

- Time: 7 weeks (held through adversity)

- Lesson: Smart adjustment saved the trade

**What made this work:**

1. ✅ Adjusted when thesis broken (DIS weak)

2. ✅ Didn't panic at first loss

3. ✅ Rolled down to new profit zone

4. ✅ Closed when target hit post-adjustment

5. ✅ Didn't hold too long (exited 18 DTE)

**Key lesson:** Sometimes adjustments work! But only if you:

- Act early (don't wait for disaster)

- Reset to realistic target

- Exit when recovered (don't get greedy)

---

### 6. Setup: BAC at $28


**Setup:**

- BAC at $28 in banking sector  

- Trader sets 1:2 ratio spread

- Buy $28 call, sell 2 × $32 calls for $0.80 debit

- **Then FORGETS about it** (set and forget mentality)

**Week 1-3:** BAC drifts $28-30

- Position profitable

- Trader not monitoring

**Week 4:** Banking crisis news

- BAC rallies sharply to $34 (flight to quality)

- **Position now losing**

- Trader still not watching!

**Week 5:** BAC continues to $36

- **$4 past upper breakeven**

- Loss: ~$400 per contract

- **Trader has 20 contracts** (over-sized!)

- **Total loss: -$8,000!**

**Trader finally checks account:**

- Sees the damage

- Panics, closes position

- Account destroyed

**What went catastrophically wrong:**

1. ❌ **"Set and forget"** (ratio spreads need ACTIVE monitoring)

2. ❌ **No alerts set** (should've had alert at $32 breakeven)

3. ❌ **Massive over-sizing** (20 contracts = insane)

4. ❌ **No stop loss** (would've auto-closed at breakeven)

**Key lesson:** Ratio spreads are NOT passive strategies. Check daily, set alerts, have stops. Or don't trade them!

---

### 7. Setup: Trader


**Setup:**

- Trader owns 200 shares of JNJ at $160

- Wants income but willing to sell at $170

- Also willing to take on SLIGHT additional upside risk

- 45 DTE

**Trade: Covered ratio spread**

- Own 200 JNJ shares

- Sell 3 × $170 calls @ $2.50 each

- Collect: $750 premium

**Structure:**

- 2 calls "covered" by 200 shares

- 1 call "naked" (but still relatively safe)

**Why this is reasonable:**

- Already own the stock (reduces risk)

- Would sell at $170 anyway

- Extra call adds some risk but manageable

- JNJ is stable (unlikely to gap)

**Outcome (6 weeks later):** JNJ at $168

- All 3 calls expire worthless

- Keep $750 premium

- Still own shares

- **Repeat next month**

**Annual result:**

- Collect ~$750/month = $9,000/year

- On $32,000 position (200 × $160)

- **Extra yield: 28%!**

**Risk managed:**

- If JNJ goes to $180: Lose $10/share on 1 naked call = -$1,000

- But already made $9,000 over year

- Net: Still way ahead

**Key lesson:** Ratio spreads CAN work if:

- Part of broader position (covered)

- On stable, boring stocks

- Small extra risk (not 1:3, just 2:3 ratio)

- Consistent income strategy

This is probably the ONLY good long-term use of ratio spread concepts!

---

### 8. Winning scenarios


**Winning scenarios (20-30% of trades):**

- High IV entry → IV crush

- Stable stock (SPY, JNJ, KO)

- Post-event setup

- Wide strikes

- Disciplined exit (80-90% profit)

- Small size

**Losing scenarios (70-80% of trades):**

- Low IV entry

- Volatile stock (TSLA, NVDA, meme stocks)

- Through earnings or events

- Narrow strikes

- No stop loss

- Over-sized

- "Set and forget"

**The math is brutal:**

- Win rate: 25%

- Avg win: +200% ($500 profit)

- Loss rate: 10% (disasters)

- Avg disaster: -1000% ($2,500 loss)

- Other 65%: Small wins/losses

**Expected value:**
$$
EV = 0.25 \times \$500 + 0.65 \times \$50 - 0.10 \times \$2,500 = \$125 + \$32.50 - \$250 = -\$92.50
$$

**Negative expected value!** This is why most traders should avoid ratio spreads.

---

## When to Use Ratio


### 1. Favorable


**1. Moderately directional view:**

- Think stock will move, but not too far

- Have target in mind

- Confident it won't go past breakeven

**2. High implied volatility:**

- Expensive options

- Collect more premium on shorts

- Can establish for credit

**3. Reduce cost of directional bet:**

- Want long call/put exposure

- Can't afford full premium

- Accept risk for cheaper entry

**4. Range-bound conviction:**

- Stock will rise/fall to certain level

- Then stop or reverse

- Sweet spot at your target

### 2. Unfavorable


**1. Uncertain direction:**

- If unsure, naked shorts are dangerous

- Use defined-risk spreads instead

**2. Potential for big moves:**

- Earnings ahead

- Binary events (FDA, etc.)

- High chance of exceeding breakeven

- **Very dangerous!**

**3. Low volatility:**

- Cheap options anyway

- Not much premium to collect

- Better to use straight call/put

**4. Cannot monitor:**

- Need active management

- Can't set and forget

- If busy, use defined-risk strategies

---

## Risk Management Framework
**Ratio spreads require strict discipline:**

### 1. Rule 1


**Never more than 2-3% of account:**

- Unlimited loss potential

- One bad trade can destroy account

- **Size very small**

**Example:**

- $50,000 account

- Max risk per ratio spread: $1,000-1,500

- Even though "max loss on downside" is $100, upside is unlimited!

### 2. Rule 2


**MUST have hard stop:**

- If stock approaches upper breakeven → close!

- Don't hope it comes back

- Unlimited loss awaits

**Example:**

- Upper BE at $289

- Stock hits $285 → **close immediately**

- Accept small loss rather than catastrophe

### 3. Rule 3


**Never hold ratio spreads through:**

- Earnings

- FDA decisions

- Acquisitions

- FOMC meetings (if relevant)

- **Gap risk is existential threat**

### 4. Rule 4


**Active management required:**

- Check position daily

- Watch for moves toward danger

- Be ready to close

- **Not passive strategy**

### 5. Rule 5


**Don't be greedy:**

- If at 50% max profit → consider closing

- Max profit at upper strike is rare

- Take profits, redeploy

**Example:**

- Max profit: $1,900 at $270

- Current profit: $1,000 at $265

- **Close! Don't wait for $270**

### 6. Rule 6


**Don't use ratio spreads on:**

- Meme stocks (AMC, GME)

- Biotech before FDA

- Small caps with wild swings

- **Stick to stable, large caps**

---

## Ratio Spreads vs.


| Strategy | Cost | Downside Risk | Upside Risk | Complexity |
|----------|------|---------------|-------------|-----------|
| **Call Ratio Spread** | Low/Credit | Limited (debit) | **UNLIMITED** | High |
| **Put Ratio Spread** | Low/Credit | **UNLIMITED** | Limited (debit) | High |
| Long Call | Medium | Limited (premium) | Unlimited | Low |
| Bull Call Spread | Low | Limited | Limited | Medium |
| Calendar Spread | Medium | Limited | Limited | Medium |
| Iron Condor | Credit | Limited | Limited | Medium |

**Key difference:**

**Ratio spreads are ONLY strategy with:**

- Unlimited risk on ONE side (not both)

- Can be established for credit

- Profit from moderate move but lose from large move

**This is unique and dangerous!**

---

## Advanced Variations


### 1. Synthetic


**Advanced traders may combine ratio spreads with synthetic positions to create complex risk-reward profiles:**

**Figure 2:** Synthetic long stock construction showing how long call plus short put at the same strike replicates long stock position, illustrating put-call parity and how synthetics can be combined with ratio spread strategies for capital efficiency.

**Figure 3:** Synthetic short stock construction demonstrating how short call plus long put creates a position equivalent to short stock, showing the mirror relationship to synthetic long positions and applications in ratio spread hedging.

**Figure 4:** Synthetic components breakdown showing how various option combinations decompose into equivalent positions, illustrating the building blocks used in advanced ratio spread variations and conversion strategies.

**Figure 5:** Comparison of synthetic positions versus actual stock holdings showing capital requirements, margin differences, and dividend considerations, demonstrating when synthetics offer advantages in ratio spread construction.

**Figure 6:** Put-call parity relationship diagram showing the fundamental equation C - P = S - K×e^(-rT) that ensures no arbitrage between calls, puts, and stock, forming the theoretical foundation for synthetic position equivalence.

**Figure 7:** Conversion and reversal relationships showing how to transform between equivalent positions (conversions: long stock + long put + short call, reversals: short stock + long call + short put), illustrating advanced arbitrage strategies that can be combined with ratio spreads.

**Figure 8:** Strike selection for synthetic positions and ratio spreads showing how ATM synthetics replicate stock exactly while OTM synthetics create leverage or deductibles, demonstrating strategic strike choices when combining synthetics with ratio spread structures.

### 2. Ratio Backspread


**Opposite structure:**

- Sell fewer, buy more

- Example: Sell 1 × $100 call, buy 2 × $110 calls

- **Profit from big moves** (like straddle but cheaper)

- Usually credit

- Unlimited profit one direction

**Use when:**

- Expect volatility

- Want cheaper than straddle

- Accept risk on one side

### 3. Christmas Tree


**Multiple ratios:**

- Buy 1 low

- Sell 2 middle

- Sell 1 high

- Like ratio + vertical

**More complex, more defined risk**

### 4. Ladder Spread


**Progressive strikes:**

- Buy 1 ATM

- Sell 1 OTM

- Sell 1 farther OTM

- Graduated profit zones

### 5. Ratio Diagonal


**Different expirations:**

- Buy longer-dated

- Sell 2 shorter-dated (different strikes)

- Combines ratio + calendar

**Very complex, professional use**

---


---

## Practical Guidance for Implementation
**Step-by-step implementation framework:**

### 1. Before entering,


**Before entering, evaluate:**

1. **Market environment:**

   - Trend direction and strength

   - Volatility level (IV percentile)

   - Upcoming events or catalysts

2. **Technical analysis:**

   - Support/resistance levels

   - Volume and liquidity

   - Recent price action

3. **Fundamental backdrop:**

   - Company-specific news

   - Sector dynamics

   - Macro environment

### 2. Entry Timing and Conditions
**Enter this strategy when:**

- IV is elevated (IV Rank > 40%) making sold options relatively rich

- You have a directional view but expect limited move magnitude

- 30-60 days to expiration for optimal theta collection

- Underlying has sufficient liquidity (tight bid-ask spreads)

**Avoid this strategy when:**

- IV is very low (IV Rank < 20%) – premium not worth the risk

- Expecting large directional moves (backspreads better)

- Less than 14 days to expiration (gamma risk too high)

- Major events pending that could cause gap moves

### 3. Calculate Maximum Position Size
**Calculate maximum position size:**

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times \text{Risk\%}}{\text{Max Loss Per Contract}}
$$

**Conservative guidelines:**

- Risk 1-2% per trade when learning

- Max 5 uncorrelated positions

- Never more than 20% of portfolio in options

### 4. Best Practices for Entry
**Best practices:**

1. **Use limit orders:** Never use market orders

2. **Check liquidity:** Bid-ask spread < 10% of mid-price

3. **Time entry:** Avoid first/last 30 minutes of trading day

4. **Single order:** Enter as complete strategy, don't leg in

### 5. Active Management Rules
**Active management rules:**

**Profit targets:**

- Take profit at 50-75% of max profit

- Scale out if appropriate

- Don't be greedy

**Loss limits:**

- Cut losses at [Y]% of max loss

- Don't hope for recovery

- Preserve capital

**Time-based exits:**

- Monitor theta decay

- Exit if [time-based trigger]

### 6. When to adjust:


**When to adjust:**

- Position threatened

- Market environment changes  

- New information emerges

**How to adjust:**

- [Adjustment technique 1]

- [Adjustment technique 2]

- [When to take loss instead]

### 7. Track every


Track every trade:

- Entry/exit dates and prices

- Rationale for trade

- Market conditions (IV, trend, etc.)

- P&L and lessons learned

### 8. Common Execution


1. **Entering at wrong volatility level**

2. **Ignoring liquidity**

3. **Over-sizing positions**

4. **Failing to set exit rules upfront**

5. **Emotional decision-making**


## Common Mistakes and How to Avoid Them
### 1. ❌ Wrong: "Stock


❌ **Wrong:**

- "Stock at $250, won't go past $300"

- Set up ratio spread

- Stock gaps to $320 on news

- **Catastrophic loss**

**Why it fails:**

- Stocks can always surprise

- News happens

- Gap risk is real

- Unlimited loss is unlimited

✅ **Better:**

- Always have stop at upper BE

- Size tiny (2% max)

- Never hold through events

- Accept you can't predict extremes

### 2. ❌ Wrong: Set up


❌ **Wrong:**

- Set up ratio spread before earnings

- "Stock won't move more than 10%"

- Stock moves 20% (common!)

- **Disaster**

**Why it fails:**

- Earnings create gaps

- 20-30% moves happen

- Ratio spreads can't handle this

- Unlimited loss triggered

✅ **Better:**

- Close before earnings

- Never hold through binary events

- Use defined-risk strategies for events

### 3. ❌ Wrong: Set up


❌ **Wrong:**

- Set up ratio spread, forget about it

- Stock drifts toward danger

- "It'll come back"

- Blows past upper BE

- **Account destroyed**

**Why it fails:**

- Unlimited loss doesn't care about hope

- Need mechanical stops

- Emotions kill you

✅ **Better:**

- Hard stop at upper BE minus buffer

- No exceptions

- Mechanical exit

### 4. ❌ Wrong: $25,000


❌ **Wrong:**

- $25,000 account

- Risk $5,000 on ratio spread (20%)

- "Max loss is just my debit!"

- Forgets about unlimited upside risk

**Why it fails:**

- One bad ratio spread = account blown

- Max loss isn't really max (upside unlimited)

- Overconfidence

✅ **Better:**

- 2% max sizing

- Assume worst case (loss thousands)

- Never more than few contracts

### 5. ❌ Wrong: Strikes


❌ **Wrong:**

- Strikes too close (short at $105, long at $100)

- Very small profit zone

- High chance of blowing through

**Why it fails:**

- Narrow sweet spot

- Easy to overshoot

- Risk >> reward

✅ **Better:**

- Strikes at least $10 apart (for $100 stock)

- Give room to work

- Better risk/reward

---


---




