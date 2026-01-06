# Iron Condors

**Iron condors** are neutral, defined-risk option strategies that combine a bull put spread and a bear call spread, profiting from low volatility and time decay with capped maximum loss.









---

## The Core Insight

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/iron_condor_body_width_comparison.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**The fundamental idea:**

- Stocks often trade sideways within a range
- You want to profit from this lack of movement
- Sell premium with DEFINED risk (unlike short strangles)
- Profit if stock stays between your short strikes
- Maximum loss is known upfront
- Best for risk-averse traders who want premium income

**The key equation:**

$$
\text{Max Profit} = \text{Net Credit Received} \quad (\text{collected upfront})
$$

$$
\text{Max Loss} = \text{Width of Spread} - \text{Net Credit} \quad (\text{defined and capped})
$$

**You're essentially betting: "The stock will stay within a range, but I want to sleep at night knowing my maximum loss."**

---

## What Is an Iron Condor?

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/iron_condor_decomposition.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Before trading iron condors, understand the structure:**

### 1. Structure

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/iron_condor_greeks.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Definition:** An iron condor combines two credit spreads with the same expiration:
1. Bull put spread (below current price)
2. Bear call spread (above current price)

**Four legs (from lowest to highest strike):**

1. **Buy OTM Put** at strike $K_1$ (protection)
2. **Sell OTM Put** at strike $K_2$ (income, higher than $K_1$)
3. **Sell OTM Call** at strike $K_3$ (income, above current price)
4. **Buy OTM Call** at strike $K_4$ (protection, higher than $K_3$)

**All same expiration, creating:**
$$
\text{Iron Condor} = \underbrace{\text{Long } K_1 \text{ Put}}_{\text{Protection}} + \underbrace{\text{Short } K_2 \text{ Put}}_{\text{Income}} + \underbrace{\text{Short } K_3 \text{ Call}}_{\text{Income}} + \underbrace{\text{Long } K_4 \text{ Call}}_{\text{Protection}}
$$

**Example:**

- Stock at $100
- Buy $90 put for $1
- Sell $95 put for $3
- Sell $105 call for $3
- Buy $110 call for $1
- **Net credit: ($3 + $3) - ($1 + $1) = $4 = $400 per contract**

**At expiration:**

- Stock between $95-$105 → All options expire worthless → Keep $400
- Stock at $85 → Put spread maxed out → Lose $100 (500 - 400 credit)
- Stock at $115 → Call spread maxed out → Lose $100 (500 - 400 credit)

### 2. Key Characteristics

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/iron_condor_management_zones.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Defined risk neutral strategy:**

- Maximum loss is known upfront
- Cannot lose more than defined amount
- Profit from stock staying in range
- Win from time decay and volatility decrease

**Risk profile:**

- **Max profit:** Net credit received (limited)
- **Max loss:** Width of spread - Net credit (capped!)
- **Breakeven points:** Two of them
  - Lower: Short put strike - Net credit
  - Upper: Short call strike + Net credit

**Probability of Profit:**

- Typically 60-70% (similar to short strangle)
- But max loss much smaller
- Risk-reward ratio better defined
- **Key advantage: Sleep at night knowing max loss**

**Figure 1:** Iron condor payoff diagram showing the defined-risk profit zone between breakeven points. Unlike short strangles, losses are capped at the width of the spreads minus credit received.

---

## Economic Interpretation

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/iron_condor_payoff.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Beyond the basic definition, understanding what iron condors REALLY are economically:**

### 1. The Reinsurance Analogy

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/iron_condor_time_decay.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**The deep insight:**

An iron condor is economically equivalent to **selling insurance while simultaneously buying reinsurance**. When you sell an iron condor, you're essentially:

1. **Selling crash insurance** (short put) to bearish traders
2. **Buying catastrophe reinsurance** (long put) to cap your losses
3. **Selling rally insurance** (short call) to bullish traders  
4. **Buying breakout reinsurance** (long call) to cap your losses
5. **Keeping the premium spread** as your profit

**Formal decomposition:**

$$
\underbrace{\text{Iron Condor}}_{\text{Net Credit}} \equiv \underbrace{\text{Bull Put Spread}}_{\text{Downside Income}} + \underbrace{\text{Bear Call Spread}}_{\text{Upside Income}}
$$

**Why this matters:**

**Short Strangle (no reinsurance):**

- Collect $6 premium
- Risk: UNLIMITED if stock crashes or moons
- Potential loss: $10,000+ if catastrophic move
- **Can't sleep at night**

**Iron Condor (with reinsurance):**

- Collect $4 premium (less than strangle)
- Risk: Capped at $600 max
- You paid $2 for reinsurance ($6 - $4)
- **Sleep soundly knowing worst case**

**The $2 you "sacrifice" compared to a strangle is the cost of capping your tail risk - buying peace of mind.**

### 2. Example

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/iron_condor_vs_strangle.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Setup:**

- SPY at $450
- Buy $440 put for $1
- Sell $445 put for $3.50
- Sell $455 call for $3.50
- Buy $460 call for $1
- Net credit: $5

**What you're really doing:**

$$
\begin{align}
\text{Economic Position} &= \text{Sell crash protection at \$445} \\
&+ \text{Buy catastrophe reinsurance at \$440} \\
&+ \text{Sell rally protection at \$455} \\
&+ \text{Buy breakout reinsurance at \$460} \\
&+ \text{Net income: \$500}
\end{align}
$$

**Scenarios:**

| SPY at Expiry | Spreads Value | Your P&L | vs. Short Strangle |
|--------------|---------------|----------|-------------------|
| $450 (unchanged) | All worthless | **+$500** | +$700 (strangle better) |
| $448 (small move) | All OTM | **+$500** | +$700 (strangle better) |
| $442 (tested) | Put spread -$300 | **+$200** | +$400 (strangle better) |
| $435 (crash) | Put spread maxed | **-$0** | -$800 (CONDOR SAVED YOU!) |
| $465 (rally) | Call spread maxed | **-$0** | -$1,300 (CONDOR SAVED YOU!) |
| $420 (disaster) | Put spread maxed | **-$0** | -$2,300 (HUGE DIFFERENCE!) |

**Key insight: You sacrifice profit in calm markets to avoid catastrophic loss in turbulent markets!**

### 3. The Risk-Reward Trade-off

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/iron_condor_wing_width_comparison.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Iron condor vs. short strangle:**

$$
\text{Strangle Premium} - \text{Condor Premium} = \text{Cost of Insurance}
$$

**Example comparison:**

| Metric | Short Strangle | Iron Condor | Difference |
|--------|---------------|-------------|------------|
| Credit collected | $7 | $5 | $2 (insurance cost) |
| Max profit | $700 | $500 | $200 less |
| Max loss | Unlimited | $500 | HUGE difference |
| Margin required | $10,000 | $500 | Much less |
| Sleep quality | Poor | Good | Priceless |

**This is the fundamental trade-off: Less upside in exchange for defined downside.**

### 4. Why Professional Traders Prefer Iron Condors

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/iron_condor_payoff.png?raw=true" alt="iron_condor_payoff" width="700">
</p>

**Understanding the institutional perspective:**

**Retail traders often think:**

- "Why accept less premium?"
- "I'll just manage the strangle if it goes wrong"
- "I want maximum income"

**Professional traders know:**

- Blowups happen when you can't manage (gap moves, black swans)
- Career risk from unlimited loss unacceptable
- Consistent small wins > occasional catastrophic loss
- **Can size positions larger with defined risk**

**Example sizing:**

**With $100,000 account:**

**Short Strangles:**

- Margin: $10,000 per position
- Max positions: 5 (to be safe)
- One blowup: Could lose $20,000+ (20% of account)

**Iron Condors:**

- Margin: $500 per position  
- Max positions: 20 (with proper diversification)
- One blowup: Lose $500 max (0.5% of account)
- **Can trade more contracts safely!**

**This is why institutions and professionals favor defined-risk strategies: Better risk management allows larger scale.**

---

## Key Terminology

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/iron_condor_greeks.png?raw=true" alt="iron_condor_greeks" width="700">
</p>

**Strike Width:**

- Width of put spread (typically $5)
- Width of call spread (typically $5)
- Determines max loss and margin requirement
- Wider = larger max loss but more premium

**Wing Width:**

- Distance from short strike to long strike on each side
- Narrower: Less max loss, less premium collected
- Wider: More max loss, more premium collected
- Standard: $5 wings ($5 wide spreads)

**Body Width:**

- Distance between short put and short call
- Where you want stock to stay
- Wider: Higher POP, less premium
- Narrower: Lower POP, more premium

**Risk-Reward Ratio:**

$$
\text{Risk/Reward} = \frac{\text{Max Loss}}{\text{Max Profit}} = \frac{\text{Wing Width} - \text{Credit}}{\text{Credit}}
$$

**Example:**

- Credit: $4
- Wing width: $5
- Max loss: $5 - $4 = $1
- Ratio: $1/$4 = 0.25 (risk $1 to make $4)
- **Excellent ratio!**

**Delta Selection:**

- Short strikes typically -0.15 to -0.25 delta
- Further OTM: Higher POP, less premium
- Closer to ATM: Lower POP, more premium
- Standard: -0.20 delta on short strikes

**Breakeven Points:**

- Lower BE = Short put strike - Net credit
- Upper BE = Short call strike + Net credit  
- Must be wider than short strikes due to credit
- Stock must stay between these to profit

---

## Why Trade Iron Condors?

**Use cases for iron condors:**


---

## Economic Interpretation

**Understanding what this strategy REALLY represents economically:**

### 1. The Core Economic Trade-Off

This strategy involves specific economic trade-offs that determine when it's most valuable. The key is understanding what you're giving up versus what you're gaining in economic terms.

**Economic equivalence:**

$$
\text{Strategy Payoff} = \text{Component 1} + \text{Component 2} - \text{Cost/Benefit}
$$

### 2. Why This Structure Exists Economically

Markets create these structures because different participants have different:
- Risk preferences
- Time horizons
- Capital constraints
- View on volatility vs. direction

### 3. Professional Institutional Perspective

Institutional traders view this strategy as a tool for:
1. **Risk management:** Precise control over exposure
2. **Capital efficiency:** Optimal use of buying power
3. **Probability engineering:** Trading win rate for win size
4. **Volatility positioning:** Specific exposure to implied volatility changes

Understanding the economic foundations helps you recognize when the strategy offers genuine edge versus when market pricing is fair.


### 4. Risk-Defined Premium Selling

**When you want income but can't accept unlimited risk:**

- Want to sell premium for income
- But have strict risk limits (firm rules, personal comfort)
- Need defined max loss for position sizing
- Can't accept gap risk of naked options

**Example:** Trading in IRA account

- Cannot have undefined risk positions
- Want option income
- Iron condors are IRA-legal
- **Perfect for retirement accounts**

### 5. Range-Bound Markets with Safety Net

**Stock consolidating but you want protection:**

- Clear range established
- Want to profit from sideways movement
- But market could break out (earnings, Fed, etc.)
- **Willing to sacrifice some premium for safety**

**Example:** SPY trading $445-$455 for weeks

- Historical range visible
- But FOMC meeting in 2 weeks (uncertainty)
- Sell iron condor instead of strangle
- **If Fed surprises, loss capped**

### 6. High Volatility Environments

**When IV elevated but market dangerous:**

- VIX at 25-30 (elevated)
- Options expensive (high premium)
- But large moves possible (dangerous for naked)
- **Defined risk essential in turbulent markets**

**Example:** Geopolitical crisis

- Options pricing in big moves
- Want to collect inflated premium
- But war/crisis could cause gap
- **Iron condor limits catastrophic loss**

### 7. Around Earnings (Post-Event)

**After IV crush, transitioning to calm:**

- Earnings just passed
- IV crushed from 80% to 30%
- Stock found new range
- No catalysts for 30-45 days

**Example:** AAPL post-earnings

- Was $175, now $178
- IV dropped 60% → 25%
- Sell $170/$175/$180/$185 iron condor
- **Profit from continued theta with safety**

### 8. Portfolio Management

**Part of balanced options portfolio:**

- Can't have all undefined risk
- Need mix of strategies
- Iron condors provide steady income
- Complement other positions

**Example:** Diversified options portfolio

- 30% Iron condors (steady income)
- 30% Spreads (directional)
- 20% Long options (asymmetric bets)
- 20% Cash (dry powder)

---

## Strike Selection Strategy

**How to construct your iron condor:**

### 1. Standard Approach

**Most common construction:**

$$
\text{Wing Width} = K_2 - K_1 = K_4 - K_3
$$

**Example: $5 wings on both sides**

- Stock at $100
- Buy $90 put / Sell $95 put (5-wide put spread)
- Sell $105 call / Buy $110 call (5-wide call spread)
- Symmetric structure, balanced risk

**Advantages:**

- Easy to manage
- Symmetric risk
- Standard margin calculations
- Easy to roll or adjust

### 2. Delta-Based Selection

**Choose short strikes by delta:**

$$
\text{Short strikes} \approx -0.15 \text{ to } -0.20 \text{ delta}
$$

**Why this works:**

- -0.20 delta ≈ 80% probability OTM
- Balances POP vs. premium
- Standard professional approach
- Adjustable based on risk tolerance

**Example:** Stock at $100, targeting -0.20 delta

- Short $95 put (-0.20 delta)
- Short $105 call (+0.20 delta)
- Buy $90 put (protection)
- Buy $110 call (protection)

### 3. Width Optimization

**Trade-off: Premium vs. Max Loss**

**Narrow wings ($2-3 wide):**

- Less max loss ($150-$250)
- Less premium collected ($0.50-$1.00)
- Better risk/reward ratio
- Lower margin requirement

**Standard wings ($5 wide):**

- Moderate max loss ($400-$500)
- Moderate premium ($3-$5)
- Balanced approach
- Industry standard

**Wide wings ($10+ wide):**

- Large max loss ($800-$1,000)
- More premium collected ($6-$8)
- Worse risk/reward
- Only if very confident

**Example comparison:**

| Wing Width | Credit | Max Loss | Risk/Reward | Margin |
|-----------|--------|----------|-------------|---------|
| $2 | $0.75 | $125 | 1.67:1 | $200 |
| $5 | $4.00 | $100 | 0.25:1 | $500 |
| $10 | $7.00 | $300 | 0.43:1 | $1,000 |

**Sweet spot: $5 wide wings for most traders**

### 4. Body Width Selection

**Distance between short strikes:**

**Narrow body (short strikes close):**

- Example: $95/$100 or $100/$105
- More premium collected
- Lower POP (50-60%)
- More active management needed

**Standard body:**

- Example: $95/$105 (stock at $100)
- Balanced premium/POP
- 60-70% POP
- Most common approach

**Wide body:**

- Example: $90/$110 (stock at $100)
- Less premium
- Higher POP (70-80%)
- More conservative

**Formula for body width:**

$$
\text{Body Width} \approx 0.10 \times S_0 \text{ to } 0.15 \times S_0
$$

Where $S_0$ is current stock price.

### 5. Expiration Selection

**Optimal timeframes for iron condors:**

**30-45 DTE (Sweet Spot):**

- Good theta decay
- Manageable gamma risk
- Industry standard
- Best balance

**45-60 DTE:**

- Higher premium
- Slower theta
- More time for adjustments
- If very patient

**21-30 DTE:**

- Fast theta
- Higher gamma risk
- For experienced traders
- Quick profits or losses

**Never < 21 DTE:**

- Gamma too high
- Whipsaw risk
- Hard to manage
- Not worth it

---

## The Greeks

**Understanding the forces affecting your position:**

### 1. Delta

**Iron condor delta dynamics:**

$$
\Delta_{\text{condor}} = \Delta_{\text{put spread}} + \Delta_{\text{call spread}} \approx 0
$$

**Key characteristics:**

- Initially delta-neutral (~0)
- Stays near zero within short strikes
- Becomes positive if approaching short call
- Becomes negative if approaching short put
- **Much less delta risk than naked strangles**

**Example:** Stock at $100

- Put spread delta: +0.10
- Call spread delta: -0.10
- **Net delta ≈ 0**

**Comparison to short strangle:**

| Price Move | Strangle Delta | Condor Delta |
|-----------|---------------|--------------|
| Stock at $100 | 0 | 0 |
| Stock at $95 | +0.40 | +0.20 |
| Stock at $90 | +0.80 | +0.50 |
| Stock at $85 | +1.00 | +1.00 (maxed) |

**Long wings limit delta exposure!**

### 2. Theta

**The primary profit source:**

$$
\Theta_{\text{condor}} = \Theta_{\text{put spread}} + \Theta_{\text{call spread}} > 0
$$

**Key characteristics:**

- Always positive (you profit daily)
- Maximized when stock between short strikes
- Accelerates final 30 days
- But LESS than short strangle (you bought wings)

**Comparison:**

| Strategy | Daily Theta | Monthly Income |
|----------|-------------|----------------|
| Short Strangle | $15 | $450 |
| Iron Condor | $10 | $300 |

**You sacrifice $150/month for defined risk!**

**Theta acceleration:**

| Days to Exp | Daily Theta | Weekly Theta |
|------------|-------------|--------------|
| 45 | $8 | $56 |
| 30 | $10 | $70 |
| 21 | $12 | $84 |
| 14 | $15 | $105 |
| 7 | $20 | $140 |

**Optimal zone: 21-45 DTE for theta/gamma balance**

### 3. Gamma

**The hidden benefit:**

$$
\Gamma_{\text{condor}} = \Gamma_{\text{short options}} + \Gamma_{\text{long options}}
$$

**Key characteristics:**

- Negative gamma, but LIMITED
- Long wings cap gamma explosion
- Much safer than naked short options
- **This is the MAIN reason to trade condors!**

**Comparison near expiration:**

| Stock Move | Strangle Loss | Condor Loss |
|-----------|---------------|-------------|
| +$5 | -$500 | -$300 |
| +$10 | -$2,000 | -$500 (capped!) |
| +$20 | -$8,000 | -$500 (capped!) |
| +$50 | -$48,000 | -$500 (CAPPED!) |

**The long wings prevent catastrophe!**

### 4. Vega

**Volatility exposure:**

$$
\nu_{\text{condor}} = \nu_{\text{short options}} + \nu_{\text{long options}} < 0
$$

**Key characteristics:**

- Still negative vega (short volatility)
- Slightly less than strangle (long wings offset)
- Still lose if IV spikes
- **Need to manage this risk**

**Example:**

- Enter with IV = 25%
- IV spikes to 45% (earnings, crisis)
- Position down even if stock unchanged
- **Condor: -$300, Strangle: -$500**

**Mitigations:**

- Enter when IVR high (50%+)
- Exit if IV spikes unexpectedly
- Use VIX as market volatility gauge
- Diversify expirations

**Figure 2:** Greeks comparison between iron condor and short strangle, showing how the long wings reduce gamma and vega risk while maintaining positive theta. The iron condor has less extreme Greeks across all dimensions.

---

## Management and Adjustments

**What to do when positions move against you:**

### 1. Taking Profits Early

**When winning: Exit before expiration**

**50% Rule (Standard):**

- Position showing 50% of max profit
- Example: $400 credit, now worth $200
- **Close for $200 profit, redeploy**
- Captures most edge, avoids late gamma

**21 DTE Rule:**

- Exit at 21 DTE regardless of profit
- Even if only 30% profit
- Gamma acceleration not worth risk
- **Professional standard**

**Example:**

Day 1: Sell condor for $400 credit
Day 15: Worth $180 (55% profit)
Action: **Close immediately, bank $220**

### 2. Managing Tested Sides

**When stock approaches a short strike:**

**Option 1: Do Nothing (If slight breach)**
- Stock just touched short strike
- Still time left (>21 DTE)
- Other side profitable
- **Sometimes best to wait**

**Option 2: Roll Tested Side**
- Stock at $106, short call at $105
- Roll $105 call to $110 for credit
- Extends duration, gives more room
- **Cost: Increases max loss**

**Option 3: Close Entire Position**
- Take loss at predetermined level
- Usually 2x credit or max loss
- Move on to better opportunities
- **Discipline > Hope**

**Option 4: Adjust to Iron Butterfly**
- Stock moved to one short strike
- Move other side to same strike
- Now have iron butterfly
- **Different risk/reward profile**

**Decision matrix:**

| Days Left | Stock Location | Action |
|-----------|----------------|---------|
| 35+ | Just touched short | Wait |
| 35+ | Broke through | Roll or close |
| 21-35 | Near short | Consider rolling |
| <21 | Anywhere tested | Close immediately |

### 3. Rolling Strategies

**Extending duration when needed:**

**Vertical Roll:**

- Same expiration, different strikes
- Roll tested side further OTM
- Collect additional credit
- Increases max loss

**Horizontal Roll:**

- Keep strikes, extend expiration
- Roll entire condor to next month
- Usually near zero cost
- Gives more time

**Diagonal Roll:**

- Change both strikes and expiration
- Most flexible
- Can improve position significantly
- Requires more skill

**Example roll:**

```
Original: 30 DTE, $95/$100/$105/$110 for $4 credit
Stock now at $106
Roll: Close current, open:
New: 45 DTE, $95/$100/$110/$115 for $2 more credit
Result: Total $6 credit, new max loss $4
```

### 4. Managing Winners

**Don't be greedy:**

**Example scenario:**

- Sold condor for $400 credit
- After 20 days, worth $150 (62% profit)
- Stock still in middle of range
- Tempting to hold for full $400

**But consider:**

- Only $150 more potential profit
- 25 days of gamma/vega risk
- Could use capital for new trade
- **Take the $250, move on!**

**Math:**

- Remaining profit: $150
- Remaining risk: $500 (max loss)
- Remaining time: 25 days
- **Risk/reward worsening, exit!**

---

## Advanced Concepts

### 1. Optimal Wing Width Selection

**Mathematical approach:**

$$
\text{Optimal Width} = \arg\max_w \left(\frac{\text{Credit}(w)}{\text{MaxLoss}(w)}\right) \times \text{POP}(w)
$$

**In practice:**

Test different widths:

| Width | Credit | Max Loss | Ratio | POP | Score |
|-------|--------|----------|-------|-----|-------|
| $2 | $0.75 | $1.25 | 0.60 | 75% | 0.45 |
| $5 | $4.00 | $1.00 | 4.00 | 65% | 2.60 |
| $10 | $7.00 | $3.00 | 2.33 | 60% | 1.40 |

**$5 wings optimize risk/reward × probability!**

### 2. Unbalanced Iron Condors

**Adjusting for bias:**

**Bullish bias:**

- Wider put spread ($7-10 wide)
- Narrower call spread ($3-5 wide)
- Collect asymmetric premium
- More upside room

**Bearish bias:**

- Wider call spread
- Narrower put spread
- More downside room
- Directional tilt

**Example:**

Stock at $100, slightly bullish:
- $85/$95 put spread (10-wide)
- $105/$110 call spread (5-wide)
- More room for upward drift
- Still defined risk

### 3. Win Rate Analysis

**Expected value calculation:**

$$
EV = (P_{win} \times \text{Avg Win}) - (P_{loss} \times \text{Avg Loss})
$$

**Typical iron condor:**

- Win rate: 65%
- Average win: $350
- Average loss: $200
- EV = (0.65 × $350) - (0.35 × $200) = $227.50 - $70 = **+$157.50**

**Key insight:**

- Positive expected value
- Win rate high enough
- Losses controlled by wings
- **Sustainable over many trades**

### 4. Kelly Criterion for Sizing

**Optimal position size:**

$$
f^* = \frac{p(b+1) - 1}{b}
$$

Where:
- $p$ = Win probability (0.65)
- $b$ = Win/loss ratio ($350/$200 = 1.75)

$$
f^* = \frac{0.65(1.75+1) - 1}{1.75} = \frac{0.79}{1.75} = 0.45
$$

**Interpretation:**

- Kelly suggests 45% of capital
- WAY too aggressive for options!
- Use fractional Kelly: 10-25%
- **Conservative sizing crucial**

---


---

## Practical Guidance

**Step-by-step implementation framework:**

### 1. Step 1

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

### 2. Step 2

**Enter this strategy when:**
- IV rank > 40% (options expensive enough)
- Stock in established range (no strong trend)
- 30-45 days to expiration available
- Risk tolerance for neutral strategy
- Post-earnings IV crush opportunity
- Market consolidating after big move

**Avoid this strategy when:**
- IV rank < 30% (options too cheap)
- Earnings announcement within 7 days
- Strong trending market (up or down)
- VIX > 30 (too volatile)
- < 21 days to expiration (gamma risk)
- Insufficient liquidity (bid-ask > 10% of mid)

### 3. Step 3

**Calculate maximum position size:**

$$
\text{Max Contracts} = \frac{\text{Portfolio} \times \text{Risk\%}}{\text{Max Loss Per Contract}}
$$

**Conservative guidelines:**
- Risk 1-2% per trade when learning
- Max 5 uncorrelated positions
- Never more than 20% of portfolio in options

### 4. Step 4

**Best practices:**

1. **Use limit orders:** Never use market orders
2. **Check liquidity:** Bid-ask spread < 10% of mid-price
3. **Time entry:** Avoid first/last 30 minutes of trading day
4. **Single order:** Enter as complete strategy, don't leg in

### 5. Step 5

**Active management rules:**

**Profit targets:**
- Take profit at 50% of max profit (non-negotiable)
- Exit at 21 DTE regardless of profit
- Scale out at 40% if nervous about holding
- Don't be greedy - last 50% has highest risk

**Loss limits:**
- Cut losses at 2x credit received (hard stop)
- Exit if stock breaches long strike
- Don't hope for recovery past max loss
- Preserve capital for next opportunity

**Time-based exits:**
- Monitor daily theta decay
- Exit if < 21 DTE (gamma explosion risk)
- Consider early exit if theta gain minimal

### 6. Step 6

**When to adjust:**
- Stock approaches short strike (delta becomes significant)
- Position down more than credit received
- IV spike hurts all legs simultaneously
- Strong directional move threatens one side

**How to adjust:**
- **Vertical roll:** Move tested spread further OTM, increase credit
- **Close untested side:** Remove risk, reduce loss on tested side
- **Time roll:** Extend expiration, collect more premium
- **Take loss and re-enter:** Often better than adjusting
- **Close entire position:** When 2x credit loss or max loss approached

**When to take loss instead:**
- Cost to adjust > original credit
- Stock momentum too strong  
- Adjustment increases max loss significantly
- Less than 21 DTE remaining
- Better opportunity elsewhere

### 7. Step 7

Track every trade:
- Entry/exit dates and prices
- Rationale for trade
- Market conditions (IV, trend, etc.)
- P&L and lessons learned

### 8. Common Execution Mistakes to Avoid

1. **Entering at wrong volatility level**
2. **Ignoring liquidity**
3. **Over-sizing positions**
4. **Failing to set exit rules upfront**
5. **Emotional decision-making**


## Common Mistakes and How to Avoid Them

### 1. Mistake 1

**The error:**

- Use $2-3 wings to "maximize premium"
- Think "I'll just manage it"
- Max loss too large relative to credit

**Why it fails:**

- Max loss = $200-$300
- Credit = $50-$100  
- Risk/reward ratio terrible (3:1 or worse)
- **One loss wipes out multiple wins**

**Fix:**

- Use $5+ wings minimum
- Target 2:1 to 4:1 reward/risk
- Don't optimize for premium alone
- **Optimize for expected value**

### 2. Mistake 2

**The error:**

- "Just 10 more days for full profit"
- Gamma explodes, whipsaw kills position
- $300 profit → $500 loss in one day

**Why it fails:**

- Gamma accelerates exponentially
- Pin risk emerges
- Assignment complications
- **Last 10% profit has 90% of risk**

**Fix:**

- Hard exit at 21 DTE
- Or take 50% profit
- Whichever comes first
- **No exceptions to this rule!**

### 3. Mistake 3

**The error:**

- All condors at same delta
- All tested if market moves
- Correlated losses

**Why it fails:**

- One market move hits all positions
- No diversification benefit
- **Cluster risk**

**Fix:**

- Vary delta selection (-0.15 to -0.25)
- Different underlyings
- Different expirations
- **Spread out breakevens**

### 4. Mistake 4

**The error:**

- Stock breaches short strike
- "I'll roll and collect more premium"
- Keep rolling, keep losing
- Turn $200 loss into $1,000 loss

**Why it fails:**

- Stock has momentum
- Rolling increases max loss
- Chasing bad position
- **Throwing good money after bad**

**Fix:**

- Accept loss at 2x credit
- Close and move on
- Don't marry losing trades
- **Cut losses quickly**

### 5. Mistake 5

**The error:**

- Sell condors when IVR = 10%
- Premium is $1-2 (tiny)
- IV likely to increase
- Negative expected value

**Why it fails:**

- Premium too small vs. risk
- IV mean reversion hurts
- Negative vega hits hard
- **Wrong time to sell vol**

**Fix:**

- Only enter when IVR > 40%
- Ideal when IVR > 60%
- Check IV percentile first
- **Timing matters!**

---

## Real-World Examples

### 1. Example 1

**Setup:**

- SPY at $450, range-bound $445-$455 for 6 weeks
- IV rank at 55% (moderate)
- No major catalysts
- VIX at 16

**Trade:** 35 DTE iron condor

- Buy $435 put / Sell $440 put
- Sell $460 call / Buy $465 call
- Net credit: $4.50 = $450 per contract
- Max loss: $50

**Management:**

- Day 15: Position worth $2.00 (56% profit)
- Took profit, closed for $250 gain
- **Return: 500% on capital (max loss $50) in 15 days**

**Outcome:**

- SPY stayed at $450
- Perfect execution
- Exited early per 50% rule
- **Banked profit, avoided risk**

**Lesson:** Discipline wins. Took profit early instead of being greedy. Used high IV rank for entry timing.

### 2. Example 2

**Setup:**

- AAPL at $175 post-earnings
- IV crushed from 65% to 30%
- Sold iron condor immediately after

**Trade:** 42 DTE post-earnings

- Buy $165 put / Sell $170 put
- Sell $180 call / Buy $185 call
- Net credit: $3.50 = $350
- Max loss: $150

**Event:**

- Unexpected analyst downgrade 2 weeks later
- AAPL dropped to $168 (tested put spread)
- Position down to $175 (-$175 loss)

**Outcome:**

- **Max loss capped at $150**
- vs. naked strangle would be -$500+
- Took the defined loss
- **Moved on to next trade**

**Lesson:** Wings protected from worse loss. Defined risk allowed clean exit. Short strangle would have been disaster.

### 3. Example 3

**Setup:**

- QQQ at $370
- Sold iron condor for $500 credit
- Max loss: $500

**Good start:**

- Day 22: Worth $200 (60% profit)
- Should have closed per rules
- **Got greedy, wanted full $500**

**Disaster:**

- Day 28: Market whipsaw
- QQQ spiked to $378
- Call spread breached
- Position now -$300 loss

**Outcome:**

- **Turned $300 profit → $300 loss**
- Lost $600 in opportunity/reality
- All because didn't exit at 50%

**Lesson:** Rules exist for a reason. 50% profit rule is not optional. Greed destroys accounts. The last $200 of profit cost $600 total.

### 4. Example 4

**Setup:**

- IWM at $200
- Sold iron condor for $400 credit
- IV = 22% at entry (IVR = 50%)

**Event:**

- Day 8: Fed surprise hawkish
- VIX jumped 18 → 28
- IWM unchanged but condor now -$200

**Action:**

- Recognized vega risk
- Exited for -$200 loss
- Avoided potential -$600+ if held

**Later:**

- Day 12: VIX settled at 20
- IWM back at $200
- Re-entered fresh condor
- **Second trade profitable**

**Lesson:** Negative vega is real. Sometimes best action is exit and re-enter. Don't marry positions. Manage risk, not price.

---

## Risk Management Rules

**Essential guidelines for iron condors:**

### 1. Position Sizing

**Capital allocation:**

$$
\text{Max Contracts} = \frac{\text{Account Size} \times 0.05}{\text{Max Loss per Contract}}
$$

**Example:**

- $50,000 account
- 5% risk per trade = $2,500
- Max loss per condor: $500
- **Max size: 5 contracts maximum**

**Professional sizing:**

- 2-5% risk per position
- Max 10 total positions
- Max 50% of account in condors
- Rest in cash or other strategies

### 2. Stop Loss Discipline

**Exit rules (choose before entry):**

**Rule 1: Max loss reached**
- Position hits max defined loss
- Exit immediately, no questions
- This is WHY you bought wings!

**Rule 2: 2x credit loss**
- Collected $400 credit
- Down -$800 total
- **Exit, don't hope**

**Rule 3: Time-based stop**
- Exit at 21 DTE regardless
- Even if down
- Gamma risk too high

**Rule 4: Tested side breached**
- Stock breaks through long strike
- Max loss imminent
- Close entire position

### 3. Profit Taking Discipline

**Exit rules when winning:**

**50% Rule (Primary):**

- Position showing 50% max profit
- Close immediately
- Don't debate, just exit
- **This is the edge!**

**21 DTE Rule (Secondary):**

- If not hit 50%, close at 21 DTE
- Take whatever profit exists
- Redeploy to fresh position

**Example:**

```
Scenario A: 50% profit at Day 18
Action: Close immediately (50% rule triggered)

Scenario B: 30% profit at Day 21
Action: Close (21 DTE rule triggered)

Scenario C: 80% profit at Day 10
Action: Close (50% rule exceeded!)
```

### 4. Diversification Strategy

**Spread risk across:**

**Underlyings:**

- 5-10 different stocks/ETFs
- Different sectors
- Different market caps
- Low correlation

**Expirations:**

- Ladder maturities (30, 35, 40, 45 DTE)
- Not all same week
- Smooth theta income
- Reduce concentration

**Strikes:**

- Vary delta (-0.15 to -0.25)
- Different wing widths
- Different body widths
- Don't cluster breakevens

**Example portfolio:**

| Symbol | Expiry | Strikes | Credit | Max Loss |
|--------|--------|---------|--------|----------|
| SPY | 35 DTE | 440/445/455/460 | $400 | $100 |
| QQQ | 38 DTE | 360/365/375/380 | $450 | $50 |
| IWM | 42 DTE | 195/200/210/215 | $350 | $150 |
| DIA | 33 DTE | 340/345/355/360 | $300 | $200 |

### 5. IV Timing Rules

**Only enter when:**

- IVR > 40% (minimum)
- IVR > 60% (ideal)
- IV not depressed
- Options "expensive"

**Check before every trade:**

$$
\text{IVR} = \frac{\text{Current IV} - \text{52-week Low}}{\text{52-week High} - \text{52-week Low}} \times 100
$$

**Example:**

- Current IV: 28%
- 52-week range: 15% to 50%
- IVR = (28-15)/(50-15) = 37%
- **Borderline, probably wait**

---


---

## Worst Case Scenario

**What happens when everything goes wrong:**

### 1. The Nightmare Setup

**How it starts:**
- Enter iron condor with SPY at $450
- Collect $4 credit, max loss $6 per spread
- Stock trading calmly, IV at 18%
- VIX at comfortable 15

**The deterioration:**

**Days 1-7:**
- Geopolitical crisis announced over weekend
- Gap down Monday: SPY opens at $442 (-$8)
- VIX spikes to 32 (IV explosion hurts)
- Put spread immediately tested
- Position down -$400 (4x credit)

**Through expiration:**
- Fed emergency meeting announced
- SPY continues falling: $438, $435, $432
- Put spread fully breached
- Long $440 put now only protection
- Call spread worthless (far OTM)
- Final expiration: SPY at $428
- **Full max loss realized: -$600 per contract**

### 2. Maximum Loss Calculation

**Worst case mathematics:**

$$
\text{Max Loss} = (\text{Spread Width} - \text{Credit Received}) \times 100
$$

**Example calculation:**
- Sold iron condor: $440/$445/$455/$460 for $4 credit
- Spread width: $5 on each side
- Max loss per side: $5 - $4 = $1 per share
- Max loss per contract: $1 × 100 = $100
- Sold 10 contracts: **Total max loss = $1,000**

**Loss breakdown:**
- Credit collected upfront: $4,000 (10 contracts × $400)
- Put spread maxed out: -$5,000 (10 contracts × $500)
- Net loss: $5,000 - $4,000 = -$1,000
- **Impact on $50,000 account: 2% loss**

**With proper sizing (5% risk rule), this hurts but doesn't destroy the account.**

### 3. What Goes Wrong

The worst case occurs when:
1. **Wrong direction:** Market moves against you
2. **Wrong magnitude:** Move is severe
3. **Wrong timing:** Happens quickly, no time to adjust
4. **Wrong volatility:** IV moves unfavorably

### 4. The Cascade Effect

**Multiple losing positions:**
- **Position 1:** SPY iron condor, -$1,000 from crash
- **Position 2:** QQQ iron condor (high correlation!), -$800 same crash
- **Position 3:** Revenge trade in IWM trying to recover, -$600 more
- **Position 4:** Panic close TLT condor at loss, -$400 unnecessary exit

**Total damage:**
- Cumulative loss: -$2,800
- Started with $50,000 account
- **Now at $47,200 (5.6% drawdown)**
- Recovery needed: 5.9% just to break even

**The mistakes compounded:**
1. Over-correlated positions (SPY + QQQ)
2. Revenge trading after first loss
3. Panic selling profitable position
4. Violated 2% per trade risk rule
5. **Emotional decisions destroyed discipline**

### 5. Assignment and Pin Risk

**Complexity at expiration:**

**Assignment scenario:**
- Stock closes at $104.95 (just below short $105 call)
- You think you're safe, position expires worthless
- After hours: Stock jumps to $105.50 on news
- **Short call assigned: -100 shares at $105**
- Monday open: Stock at $107
- Forced to buy back at $107 = -$200 loss
- Plus your long $110 call worthless = another -$100
- **Total damage: -$300 vs expected $0**

**Pin risk explanation:**
- Stock "pinned" at strike price near expiration
- Uncertain if options ITM or OTM
- Assignment risk on short options
- Long protection may not trigger
- Creates undefined position over weekend

**Weekend risk:**
- Friday close: SPY at $444.50 (near short $445 put)
- Unsure if will be assigned
- Weekend news could gap market
- **Position in limbo until Monday**

**Cleanup process:**
- Monday: Discover assignment occurred
- Now own +100 shares SPY at $445
- Market at $442 = immediate -$300 loss
- Must sell shares and close long put
- Transaction costs eat into profits
- **Complexity = Additional losses**

**Solution: Always close before expiration (21 DTE rule prevents this!)**

### 6. Real Examples of Disasters

**Historical example 1: COVID-19 Crash (March 2020)**
- Setup: Sold SPY iron condors in February 2020
- SPY at $338, collected $5 credit on $10 wide spreads
- Expected max loss: $500 per contract
- What happened: COVID panic, SPY crashed from $338 to $218 in 4 weeks
- VIX exploded from 15 to 82
- Put spreads maxed out instantly
- **Final loss: Full $500 per contract**
- Trader with 20 contracts: **-$10,000 loss (if properly sized)**
- Trader without wings (naked strangle): **-$80,000+ (account wipeout)**

**Lesson: Wings saved accounts. Defined risk prevented total destruction.**

**Historical example 2: August 2015 Flash Crash**
- Setup: Sold iron condors on SPY at $208
- Collected $4 credit, $5 wide spreads
- Expected max loss: $100 per contract
- What happened: China devaluation panic, overnight gap down 5%
- SPY opened at $189 (beyond all strikes)
- No chance to adjust or exit
- Put spreads maxed out at open
- **Final loss: Full $100 per contract plus slippage**
- 50 contracts = -$5,000 to -$6,000
- Short strangle traders: **-$50,000+ losses**

**Lesson: Gap risk is real. Wings limit catastrophic losses even when you can't exit.**

### 7. Psychology of Losses

**Emotional stages:**
1. **Denial:** "It will recover"
2. **Hope:** "Just need a small bounce"
3. **Anger:** "Market is rigged"
4. **Capitulation:** "Just close it"
5. **Learning:** "What went wrong?"

**Winning trader mindset:**
- Accept losses quickly
- Analyze dispassionately
- Learn and adapt
- Move forward

### 8. Preventing Worst Case

**Risk management strategies:**

1. **Position sizing:**
   - Never risk more than 2-5% per trade
   - Respect maximum loss calculations religiously
   - Size for worst case, not best case
   - Calculate: Max contracts = (Account × 0.05) / Max loss

2. **Stop losses:**
   - Exit at 2x credit received (hard stop)
   - Exit when max loss reached (don't hope)
   - Exit at 21 DTE regardless of P&L
   - Use alerts for tested strikes

3. **Diversification:**
   - 5-10 uncorrelated underlyings (avoid SPY + QQQ together)
   - Different expiration dates (ladder 30-45 DTE)
   - Mix strategies (not only iron condors)
   - Different sectors (tech, healthcare, energy, etc.)

4. **Avoid high-risk scenarios:**
   - No positions through earnings (gap risk)
   - No trading when VIX > 30 (too volatile)
   - No entry when IVR < 30% (options too cheap)
   - No holding past 21 DTE (gamma/pin risk)
   - No overnight positions before Fed announcements

### 9. The Ultimate Protection

$$
\text{Survivability} = \frac{\text{Capital Remaining}}{\text{Capital Initial}} > 0.85
$$

Even in worst case, proper position sizing ensures you survive to trade again. The market will test you - preparation determines whether you survive or blow up.

**Remember:** Worst case WILL happen eventually. Position accordingly.



---

## Best Case Scenario

**What happens when everything goes right:**

### 1. The Perfect Setup

**Ideal entry conditions:**
- Post-earnings IV crush (IV rank drops from 80% to 45%)
- Stock establishing clear range ($95-$105 for 4 weeks)
- VIX declining from 22 to 16 (volatility compression)
- 35 DTE available for optimal time decay
- High liquidity (tight bid-ask spreads)
- No major catalysts for next month

**The optimal sequence:**

**Days 1-7:**
- Enter iron condor at $100 stock price
- Sell $95 put / $105 call, buy $90 put / $110 call
- Collect $4 credit ($400 per contract)
- Stock stays at $100 perfectly (no delta movement)
- IV continues declining (positive for short options)
- Theta decay working steadily ($15-20 per day)

**Days 8-20:**
- Stock oscillates between $98-$102 (ideal!)
- Position gaining $20-30 per day from theta
- By day 18: Position worth $2.00 (down from $4.00)
- **50% profit achieved: +$200 per contract**
- **Time to exit per 50% rule!**

**Through expiration (if held):**
- Stock finishes at $100 (center of range)
- All four options expire worthless
- Keep entire $400 credit
- **Maximum profit achieved**
- But this is greedy - should exit at 50%!

### 2. Maximum Profit Achievement

**Best case mathematics:**

$$
\text{Max Profit} = \text{Net Credit Received} = P_{\text{put sold}} + P_{\text{call sold}} - P_{\text{put bought}} - P_{\text{call bought}}
$$

$$
\text{ROI} = \frac{\text{Max Profit}}{\text{Capital At Risk}} \times 100\% = \frac{\text{Credit}}{\text{Max Loss}} \times 100\%
$$

**Example calculation:**
- Stock at $450 (SPY)
- Buy $440 put for $1.50, Sell $445 put for $4.00
- Sell $455 call for $4.00, Buy $460 call for $1.50
- **Net credit: ($4 + $4) - ($1.50 + $1.50) = $5.00 = $500 per contract**

**Profit breakdown:**
- Maximum profit: $500 (keep entire credit)
- Maximum loss: $5 - $5 = $0 (wait, that's wrong)
- Actually max loss: ($5 spread - $5 credit) × 100 = $0
- Real calculation: Max loss = $500 - $500 = $0 (break even worst case)
- Better example: Credit $4, Spread $5 wide
- Max profit: $400
- Max loss: ($5 - $4) × 100 = $100
- **ROI: $400 / $100 = 400% return on capital at risk**

**ROI calculation:**
- Invested: $100 (max loss)
- Returned: $400 (max profit)
- Return: 400% on capital at risk
- If held 35 days: **4,200% annualized** (unrealistic but illustrates leverage)

### 3. What Makes It Perfect

The best case requires:
1. **Right direction:** Market moves as anticipated
2. **Right magnitude:** Move is sufficient for profit
3. **Right timing:** Move happens within time frame
4. **Right volatility:** IV behaves favorably

### 4. Comparison to Alternatives

**This strategy vs. Short Strangle:**

**In best case (stock stays put):**
- Iron Condor: Collects $4, keeps $4 = **$400 profit**
- Short Strangle: Collects $7, keeps $7 = **$700 profit**
- **Strangle wins by $300 (75% more profit)**

**But consider the risk:**
- Iron Condor: Max loss $100 (defined)
- Short Strangle: Max loss unlimited (could be $5,000+)
- **Condor risk: 4:1 reward/risk**
- **Strangle risk: Potentially catastrophic**

**This strategy vs. Iron Butterfly:**
- Iron Condor: Wider profit zone ($95-$105 = $10 range)
- Iron Butterfly: Narrower zone ($98-$102 = $4 range)
- Condor collects less but wins more often
- **When this strategy wins: Stock moves moderately**
- **Butterfly wins: Stock stays very still**

**Trade-offs involved:**
- Give up $300 of potential profit (vs strangle)
- Get peace of mind with defined risk
- Sleep well knowing worst case capped
- Can size larger due to lower margin
- **Professional traders prefer defined risk**

### 5. Professional Profit-Taking

**When to take profits:**
- At 50% of max profit (primary rule, non-negotiable)
- At 21 DTE if not yet reached 50%
- At 40% if nervous about holding (acceptable)
- Immediately if IV spikes significantly (vega risk)

**Why 50% works:**
- Studies show 50% profit in ~50% of time
- Last 50% profit takes ~80% of remaining time
- Risk increases exponentially after 50%
- Capital recycling beats holding for max

**The compounding advantage:**

**Scenario A: Hold for 100%**
- Enter condor for $400 credit
- Hold 35 days for full profit
- Win rate: 65%
- Monthly return: 65% × $400 = $260

**Scenario B: Exit at 50%**
- Exit after 18 days with $200 profit
- Win rate: 75% (higher because less time)
- Can do 2 trades per month
- Monthly return: 75% × $200 × 2 = $300

**Result: Taking 50% profits yields 15% better returns with less risk!**

**Time-based consideration:**
- If 50% reached before 15 DTE: Take it
- If 50% not reached by 21 DTE: Exit anyway
- Never hold past 21 DTE for any reason

**Volatility-based trigger:**
- If IV increases 20%+ (vega spike)
- Exit immediately even at 30% profit
- Re-enter when IV settles
- Protect against vol expansion risk

**The compounding advantage:**

Taking profits early and redeploying can yield better annual returns than holding for maximum profit due to reduced risk and faster capital recycling.

### 6. The Dream Scenario

**Extreme best case:**

**The setup:** 
- Enter 10 iron condors across different stocks after market-wide IV spike
- Each for $5 credit, $5 wide spreads
- Total credit collected: $5,000
- Total capital at risk: $0 (break-even spreads!)

**What happens:**
- All 10 stocks stay perfectly range-bound
- IV crushes harder than expected (-50%)
- After just 12 days, all positions worth $2 (60% profit)
- Close all for $3,000 profit in under 2 weeks
- **ROI: Infinite (zero risk), actual return: 60% in 12 days**

**Why it's rare:**
- Perfect IV timing (happens 2-3 times per year)
- All positions winning simultaneously (requires broad consolidation)
- Fast profit realization (usually takes longer)
- **Probability: ~5% of trades**

**More realistic dream:**
- 7 out of 10 positions hit 50% profit
- 2 positions scratch (small loss)
- 1 position max loss
- Net: (7 × $250) - (1 × $100) = +$1,650
- **Portfolio return: 33% with only 1 loser**

**Key insight:** Best case is not guaranteed and should not be expected. Even professionals average 50-60% profit per winning trade, not 100%. Position sizing should assume realistic outcomes (50% profit, 65% win rate), not dream scenarios. Plan for average results, be pleasantly surprised by exceptional ones.


## What to Remember

### 1. Core Concept

**Iron condors combine bull put spread and bear call spread for defined-risk income:**

$$
\text{Iron Condor} = \text{Bull Put Spread} + \text{Bear Call Spread}
$$

- Four-legged strategy with two spreads
- Maximum profit = Net credit received
- Maximum loss = Width of spread - Credit (CAPPED!)
- High probability neutral strategy
- Best for range-bound markets with defined risk

### 2. The Setup

**Construction:**

1. Buy OTM put (protection, lowest strike)
2. Sell OTM put (income, higher strike)
3. Sell OTM call (income, above price)
4. Buy OTM call (protection, highest strike)

**Example:** Stock at $100
- Buy $90 put / Sell $95 put ($5 wide)
- Sell $105 call / Buy $110 call ($5 wide)
- Net credit: $4 = $400
- Max loss: $5 - $4 = $100

### 3. The Greeks

**Greek profile:**

- **Delta:** ~0 initially (neutral), limited by wings
- **Theta:** Positive (profit from time), less than strangle
- **Gamma:** Negative but CAPPED by long options (key advantage!)
- **Vega:** Negative (short vol), slightly less than strangle

**You win from:** Time decay and volatility decrease
**You lose from:** Large moves and volatility increase
**You're protected from:** Catastrophic losses (defined risk!)

### 4. Strike Selection

**Standard approach:**

- $5 wide spreads most common
- Short strikes at -0.15 to -0.20 delta
- Body width: 5-10% of stock price
- Symmetric wings (balanced risk)

**Example deltas:**

- Long put: -0.05
- Short put: -0.20
- Short call: +0.20
- Long call: +0.05

### 5. Expiration Selection

**Optimal timeframes:**

- **Enter: 30-45 DTE** (sweet spot)
- **Exit: 21 DTE or 50% profit** (whichever first)
- **Never: <21 DTE** (gamma too high)
- **Never: >60 DTE** (theta too slow)

### 6. Maximum Profit/Loss

**Profit/Loss profile:**

- **Max profit:** Net credit received (limited, kept if all expire worthless)
- **Max loss:** Wing width - Net credit (DEFINED and CAPPED!)
- **Breakevens:**

  - Lower: Short put - Credit
  - Upper: Short call + Credit

**Example:**

- Credit: $4
- Spreads: $5 wide
- Max profit: $400
- Max loss: $100
- Risk/reward: 0.25:1 (excellent!)

### 7. When to Use

**Trade iron condors when:**

- IV rank > 40% (options somewhat expensive)
- Stock in established range
- Want income with defined risk
- Cannot accept unlimited loss
- Post-earnings IV crush
- Need IRA-legal strategy

**Don't use when:**

- IV rank < 30% (options cheap)
- Earnings approaching
- Strong trending market
- Need unlimited profit potential
- Market highly volatile (VIX > 30)

### 8. Common Mistakes to Avoid

1. Wings too narrow (<$3 wide)
2. Holding past 21 DTE (gamma explosion)
3. Not taking 50% profits (greed)
4. Over-sizing positions (blow-up risk)
5. Ignoring IV rank (selling cheap options)
6. Not diversifying underlyings
7. Fighting tested sides (rolling endlessly)
8. Entry before earnings (gap risk)

### 9. Risk Management

**Essential rules:**

- **Position size:** Max 5% account per position, max 10 total positions
- **Stop loss:** Exit at max loss or 2x credit
- **Profit target:** Close at 50% profit or 21 DTE
- **IV timing:** Only enter when IVR > 40%
- **Diversification:** 5-10 positions across different underlyings/expirations
- **Wing width:** Minimum $5, optimize for risk/reward

### 10. Comparison to Other Strategies

**vs. Short Strangle:**

- Condor: Less premium, DEFINED risk
- Strangle: More premium, unlimited risk
- **Condor = Strangle + Insurance (long wings)**

**vs. Iron Butterfly:**

- Condor: Wider profit zone, less premium
- Butterfly: Narrower zone, more premium
- Condor more conservative

**vs. Credit Spreads:**

- Condor: Neutral, two spreads
- Single spread: Directional, one spread
- Condor combines both directions

### 11. Your Learning Path

**Progression:**

1. Master credit spreads first (simpler)
2. Understand short strangles (unlimited risk)
3. Graduate to iron condors (defined risk strangles)
4. Combine with other strategies

**Iron condors are INTERMEDIATE level - perfect for risk-conscious traders!**

### 12. Final Wisdom

> "Iron condors are the thinking trader's premium selling strategy. You sacrifice some upside (compared to short strangles) to buy peace of mind through defined risk. The long wings mean you can sleep at night knowing exactly your maximum loss. Success requires: entering when IV elevated, taking 50% profits religiously, exiting at 21 DTE, and maintaining strict position sizing. This is not maximum income - it's maximum risk-adjusted income. Done right, iron condors can generate consistent returns without the career-ending blow-ups that plague naked option sellers."

**Key to success:**

- Only enter when IVR > 40%
- Take 50% profits (non-negotiable)
- Exit at 21 DTE (gamma protection)
- Position size: max 5% per trade
- Diversify across 5-10 positions
- $5+ wing width minimum
- Never hold past 21 DTE

**Most important:** Iron condors are the defined-risk version of short strangles. If you can't stomach unlimited loss or need IRA-legal strategies, this is your tool. The wings cost premium but buy discipline and longevity! 🎯📈
