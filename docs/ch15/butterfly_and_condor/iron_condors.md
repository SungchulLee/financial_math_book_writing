# Iron Condors

[메르 - 어렵다고 아우성인 글에 재도전을 하다 (feat 아이언콘도어)](https://blog.naver.com/ranto28/224152797786)


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

## Economic


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

## Why Trade Iron Condors? (Defined-Risk Neutral Strategy)


**Use cases for iron condors:**


---

## Economic


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


### 1. Pension Duration Cut via Futures


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

### 2. Transition Risk Hedge


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

### 3. Portable Alpha with Futures


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

### 4. Tactical Duration Extension


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



## Final Wisdom


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