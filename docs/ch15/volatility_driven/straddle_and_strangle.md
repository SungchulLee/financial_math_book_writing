# Straddles and Strangles


<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/long_straddle_pnl.png?raw=true" alt="long_straddle_pnl" width="700">
</p>


<p align="center"><em>Figure 1: Long straddle P&L profile showing V-shaped payoff with unlimited profit potential in both directions and maximum loss equal to premium paid</em></p>



<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/long_strangle_pnl.png?raw=true" alt="long_strangle_pnl" width="700">
</p>


<p align="center"><em>Figure 2: Long strangle P&L profile with wider breakeven range and lower cost compared to straddle</em></p>



<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/long_vs_short_straddle.png?raw=true" alt="long_vs_short_straddle" width="700">
</p>


<p align="center"><em>Figure 3: Long vs. short straddle comparison showing inverse risk/reward profiles</em></p>



<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/straddle_greeks.png?raw=true" alt="straddle_greeks" width="700">
</p>


<p align="center"><em>Figure 4: Greek exposures of straddle position including delta, gamma, vega, and theta</em></p>



<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/straddle_pnl_sources.png?raw=true" alt="straddle_pnl_sources" width="700">
</p>


<p align="center"><em>Figure 5: Decomposition of straddle P&L into movement (gamma), volatility (vega), and time decay (theta) components</em></p>



<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/straddle_scenario_analysis.png?raw=true" alt="straddle_scenario_analysis" width="700">
</p>


<p align="center"><em>Figure 6: Scenario analysis showing P&L outcomes under different market conditions and time horizons</em></p>



<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/straddle_time_decay.png?raw=true" alt="straddle_time_decay" width="700">
</p>


<p align="center"><em>Figure 7: Time decay impact on straddle value showing accelerating theta burn approaching expiration</em></p>



<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/straddle_volatility_impact.png?raw=true" alt="straddle_volatility_impact" width="700">
</p>


<p align="center"><em>Figure 8: Implied volatility impact on straddle value demonstrating vega exposure</em></p>



<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/straddle_vs_strangle.png?raw=true" alt="straddle_vs_strangle" width="700">
</p>


<p align="center"><em>Figure 9: Direct comparison of straddle vs. strangle showing cost/breakeven trade-offs</em></p>



**Straddles and strangles** are the simplest volatility trading strategies where you profit from large price movements in either direction without the complexity of delta hedging or rebalancing.

---

## The Core Insight


**The fundamental idea:**

- You don't know which way the market will move
- But you believe it will move A LOT
- Buy options on both sides (calls AND puts)
- Profit if the move is large enough in EITHER direction
- Accept directional exposure (no hedging)

**The key equation:**
$$
\text{Profit} = \text{Intrinsic Value at Expiry} - \text{Premium Paid}
$$

**You're essentially betting: "This stock will move more than the market expects, but I don't know which direction."**

---

## The Simplest Volatility Trade


**This is THE most basic volatility strategy:**

### 1. Why Start Here?


**Before learning complex strategies (gamma scalping, dispersion, etc.), understand straddles:**

**Progression:**

1. **Straddles/Strangles** ← Start here! (Simple, no hedging)
2. **Delta Hedging** → Add hedging to remove directional risk
3. **Gamma Scalping** → Delta hedge + rebalancing for profit
4. **Vega Trading** → Focus on IV changes
5. **And beyond...**

**Think of it this way:**

- **Straddle** = Raw volatility bet (simple)
- **Gamma scalping** = Refined volatility bet (delta hedged)
- **Variance swap** = Pure volatility bet (no options needed)

**Straddles are the starting point that motivates everything else!**

---

## What Is a Straddle?


**A straddle is buying (or selling) both a call and a put at the SAME strike:**

### 1. Long Straddle Structure


**What you do:**

- Buy 1 ATM call
- Buy 1 ATM put
- Same strike (at-the-money)
- Same expiration

**Example:**

- Stock at $100
- Buy $100 call for $5
- Buy $100 put for $5
- **Total cost: $10**

**Payoff at expiration:**

```
    Profit
      ↑
      |        /
      |       /
      |      /
  ────┼─────/────────
      |    /    \
      |   /      \
      |  /        \
      | /          \
      |/____________\____→ Stock Price
         90  100  110
```

**Key characteristics:**

- **Maximum loss:** Premium paid ($10)
- **Breakeven points:** Strike ± Premium ($90 and $110)
- **Unlimited profit potential:** Both upside and downside
- **Profit if:** Stock moves significantly in EITHER direction

### 2. The Math


**At expiration:**

If stock at $S$:

- Call worth: $\max(S - 100, 0)$
- Put worth: $\max(100 - S, 0)$
- Total value: $|S - 100|$ (absolute value!)

**P&L:**
$$
\text{P\&L} = |S - \text{Strike}| - \text{Premium Paid}
$$

**Profit if:**

- Stock > $110 (call profits)
- Stock < $90 (put profits)
- **Loss if:** Stock stays near $100 (both expire worthless)

---

## What Is a Strangle?


**A strangle is buying (or selling) both a call and put at DIFFERENT strikes:**

### 1. Long Strangle Structure


**What you do:**

- Buy 1 OTM call (higher strike)
- Buy 1 OTM put (lower strike)
- Different strikes
- Same expiration

**Example:**

- Stock at $100
- Buy $110 call for $2
- Buy $90 put for $2
- **Total cost: $4**

**Payoff at expiration:**

```
    Profit
      ↑
      |           /
      |          /
      |         /
  ────┼────────/───────
      |       /      \
      |      /        \
      |_____/__________\___→ Stock Price
         80  90  100  110  120
```

**Key characteristics:**

- **Maximum loss:** Premium paid ($4)
- **Breakeven points:** $90 - $4 = $86 and $110 + $4 = $114
- **Wider breakeven range** than straddle
- **Cheaper** than straddle
- **Need bigger move** to profit

### 2. Straddle vs. Strangle Comparison


| Aspect | Straddle | Strangle |
|--------|----------|----------|
| **Strikes** | Same (ATM) | Different (OTM) |
| **Cost** | Higher ($10) | Lower ($4) |
| **Breakevens** | Closer ($90-$110) | Wider ($86-$114) |
| **Max Loss** | Higher | Lower |
| **Move needed** | Smaller | Larger |
| **Risk/Reward** | Higher premium, easier profit | Lower premium, harder profit |

**When to choose:**

- **Straddle:** Expect large move, willing to pay more
- **Strangle:** Expect VERY large move, want cheaper entry

---

## Long vs. Short


### 1. Long Straddle/Strangle (Buy Volatility)


**Structure:**

- **Buy** call + put
- Pay premium
- Want large movement

**Characteristics:**

- Limited loss (premium paid)
- Unlimited profit potential
- Negative theta (pay time decay daily)
- Long vega (benefit from IV increase)
- Long gamma (profit from movement)

**When to use:**

- Believe stock will move more than market expects
- Before earnings, events, announcements
- When IV is low (options cheap)
- High conviction on movement, not direction

**Your view:** "Realized volatility will exceed implied volatility"

### 2. Short Straddle/Strangle (Sell Volatility)


**Structure:**

- **Sell** call + put
- Receive premium
- Want no movement

**Characteristics:**

- Limited profit (premium received)
- Unlimited loss potential (very risky!)
- Positive theta (collect time decay daily)
- Short vega (hurt by IV increase)
- Short gamma (hurt by movement)

**When to use:**

- Believe stock will stay in range
- After events (vol crush expected)
- When IV is high (options expensive)
- Range-bound market expected

**Your view:** "Realized volatility will be less than implied volatility"

**WARNING:** Short straddles are VERY risky! Unlimited loss potential.

### Margin Requirements for Short Straddles


**Typical broker margin calculation (greater of):**

$$
\text{Margin} = \max\left(\text{Call Margin}, \text{Put Margin}\right) + \text{Other Side Premium}
$$

**For the short side (higher requirement):**

$$
\text{Option Margin} = 20\% \times S + \text{Premium} - \text{OTM Amount}
$$

**Example: Short ATM straddle on $100 stock**
- Sell $100 call for $4
- Sell $100 put for $4
- Total premium received: $8 × 100 = $800

**Margin calculation:**
- Call margin: 20% × $10,000 + $400 - $0 = $2,400
- Put margin: 20% × $10,000 + $400 - $0 = $2,400
- **Total margin required: ~$2,400 + $400 = $2,800**

**Margin as percentage of potential loss:**
- If stock moves to $80: Loss = $20 - $8 = $12/share = $1,200
- If stock moves to $120: Loss = $20 - $8 = $12/share = $1,200
- If stock moves to $60: Loss = $40 - $8 = $32/share = $3,200 (exceeds margin!)

**Key insight:** Margin requirements can change as position moves against you (margin calls).

### Typical IV Crush Magnitudes


**Earnings events (typical IV crush):**

| Stock Type | Pre-Earnings IV | Post-Earnings IV | Crush % |
|------------|-----------------|------------------|---------|
| Large cap tech (AAPL, MSFT) | 35-45% | 20-25% | 40-50% |
| High-growth (TSLA, NFLX) | 55-75% | 35-45% | 35-45% |
| Biotech (FDA events) | 80-150% | 40-60% | 50-60% |
| Stable dividend (JNJ, PG) | 20-30% | 15-20% | 25-35% |

**Binary events:**
- FDA approval/rejection: 60-80% crush
- M&A announcements: 50-70% crush
- Major litigation outcomes: 40-60% crush

**Economic events:**
- FOMC meetings: 10-20% crush (VIX)
- CPI/Jobs reports: 5-15% crush
- Quarterly rebalancing: 5-10% crush

**Example: TSLA earnings play**
- Pre-earnings IV: 65%
- ATM straddle price: $20 (stock at $250)
- Implied move: $20/$250 = 8%

- Post-earnings IV: 40% (38% crush)
- Stock moves +5% to $262.50
- Call intrinsic: $12.50, but time value destroyed
- Put: worthless
- **Straddle now worth ~$15 despite being right on direction**

**Lesson:** IV crush can erase directional gains. Long straddle buyers need movement GREATER than implied move PLUS IV crush impact.

---

## The Portfolio


### 1. Long Straddle Portfolio


$$
\Pi = C(K) + P(K)
$$

where $C(K)$ and $P(K)$ are call and put at strike $K$.

**Greeks:**

- **Delta:** $\Delta \approx 0$ initially (call $+0.5$, put $-0.5$ cancel out)
- **Gamma:** $\Gamma > 0$ positive (both options have positive gamma)
- **Vega:** $\mathcal{V} > 0$ positive (both long options)
- **Theta:** $\Theta < 0$ negative (pay decay on both)

**Portfolio value dynamics:**

$$
d\Pi = \Delta dS + \frac{1}{2}\Gamma(dS)^2 + \mathcal{V}d\sigma + \Theta dt
$$

**What you're exposed to:**

- ✓ Movement (gamma term)
- ✓ Implied volatility increases (vega term)
- ✗ Time decay (theta term)
- ✗ No movement (worst case)

### 2. Long Strangle Portfolio


$$
\Pi = C(K_{\text{call}}) + P(K_{\text{put}})
$$

where $K_{\text{call}} > S_0 > K_{\text{put}}$ (both OTM).

**Greeks comparison to straddle:**

- **Delta:** $\Delta \approx 0$ (similar to straddle)
- **Gamma:** $\Gamma > 0$ (smaller than straddle, options further OTM)
- **Vega:** $\mathcal{V} > 0$ (smaller than straddle)
- **Theta:** $\Theta < 0$ (less negative than straddle, cheaper options)

**Cost-benefit trade-off:**

$$
\text{Premium}_{\text{strangle}} < \text{Premium}_{\text{straddle}}
$$
$$
\text{Breakeven Width}_{\text{strangle}} > \text{Breakeven Width}_{\text{straddle}}
$$

### 3. Short Straddle Portfolio


$$
\Pi = -C(K) - P(K)
$$

**Greeks (opposite signs):**

- **Delta:** $\Delta \approx 0$
- **Gamma:** $\Gamma < 0$ (short gamma = lose on moves!)
- **Vega:** $\mathcal{V} < 0$ (short vega = lose on IV rise!)
- **Theta:** $\Theta > 0$ (collect time decay)

**Risk profile:**

$$
\text{Max Profit} = \text{Premium Received}
$$
$$
\text{Max Loss} = \infty
$$

**Daily P&L decomposition:**

$$
\text{P\&L}_{\text{daily}} = -\frac{1}{2}\Gamma(dS)^2 + \Theta dt - \mathcal{V}d\sigma
$$

First term is gamma loss from movement (quadratic in move size!), second is theta collection, third is vega loss from IV increases.

---

## Economic


**Understanding what this strategy REALLY represents economically:**

### 1. The Core Economic Trade-Off


**For long straddle:**

$$
\text{Straddle Payoff} = |S_T - K| - \text{Premium}
$$

**Economic meaning:**

This is a bet on **realized volatility exceeding implied volatility**. You're:

- Paying $\sigma_{\text{implied}}$ (via premium)
- Receiving $\sigma_{\text{realized}}$ (via |moves|)
- Profitable if $\sigma_{\text{realized}} > \sigma_{\text{implied}}$

**Approximate relationship:**

$$
\text{Premium} \approx S \cdot \sigma_{\text{implied}} \cdot \sqrt{T}
$$
$$
\text{Payoff} \propto S \cdot \sigma_{\text{realized}} \cdot \sqrt{T}
$$

Therefore:
$$
\text{Profit} \propto S \cdot (\sigma_{\text{realized}} - \sigma_{\text{implied}}) \cdot \sqrt{T}
$$

### 2. Why This Structure Exists Economically


Markets create these structures because different participants have different:

**Risk preferences:**

- Hedgers: Want to remove uncertainty (buy straddles)
- Speculators: Want to harvest premium (sell straddles)

**Time horizons:**

- Short-term traders: Buy before events
- Long-term investors: Sell when IV is elevated

**Capital constraints:**

- Limited capital: Use strangles (cheaper)
- Large capital: Use straddles (better risk/reward)

**View on volatility vs. direction:**

- Directional traders: Use calls or puts
- Volatility traders: Use straddles/strangles

### 3. Professional Institutional Perspective


**Institutional traders view straddles as:**

1. **Variance exposure:** 
   $$\text{Straddle} \approx \text{Variance Swap (discrete version)}$$

2. **Optionality value:**
   The convexity (gamma) is worth paying theta for when you expect large moves

3. **Tail risk hedge:**
   Straddles provide protection against both tail events (up or down)

4. **Vol arbitrage vehicle:**
   If your estimate of realized vol differs from market's implied vol

### 4. The Fair Value Perspective


**Break-even analysis:**

For a long straddle to break even at expiration:
$$
|S_T - K| = \text{Premium}
$$

This implies:
$$
\text{Required Move} = \frac{\text{Premium}}{S_0} \times 100\%
$$

For typical ATM straddles:

- Premium ≈ 3-5% of stock price for 1-month options
- Requires >3-5% move in either direction to profit

**Market's expectation:**

The straddle premium reflects:
$$
\text{Premium} = E^Q[|S_T - K|]
$$

where $E^Q$ is risk-neutral expectation. You profit if actual moves exceed this expectation.

### 5. Volatility Risk Premium


**Key concept:** Markets typically overprice options (positive volatility risk premium):

$$
\sigma_{\text{implied}} > E[\sigma_{\text{realized}}]
$$

**Implications:**

- **Long straddles:** Fighting uphill battle (need larger moves than average)
- **Short straddles:** Collecting risk premium (profitable on average, but risky)
- **Strategy choice:** Depends on whether you think current vol premium is justified

**Statistical edge:**

Historical studies show:

- Selling straddles wins ~60-70% of the time
- But losses can be catastrophic (fat tails)
- Long straddles need exceptional timing or events

Understanding the economic foundations helps you recognize when the strategy offers genuine edge versus when market pricing is fair.

---

## Greek Dynamics


### 1. Delta Evolution


**Initial state:**
$$
\Delta_{\text{straddle}} = \Delta_{\text{call}} + \Delta_{\text{put}} \approx 0.5 - 0.5 = 0
$$

**As stock moves up:**
$$
\Delta_{\text{call}} \to 1, \quad \Delta_{\text{put}} \to 0 \quad \Rightarrow \quad \Delta_{\text{straddle}} \to 1
$$

**As stock moves down:**
$$
\Delta_{\text{call}} \to 0, \quad \Delta_{\text{put}} \to -1 \quad \Rightarrow \quad \Delta_{\text{straddle}} \to -1
$$

**Interpretation:** Straddle starts delta-neutral but becomes directional as stock moves. The winning leg dominates.

### 2. Gamma Behavior


**Straddle gamma:**
$$
\Gamma_{\text{straddle}} = \Gamma_{\text{call}} + \Gamma_{\text{put}}
$$

**ATM characteristics:**

- Maximum gamma when $S = K$
- Both options contribute maximum gamma
- Decreases as stock moves away from strike

**Time decay of gamma:**
$$
\Gamma(t) \propto \frac{1}{\sigma\sqrt{T-t}}
$$

As expiration approaches ($T-t \to 0$), gamma explodes near ATM but collapses away from ATM.

### 3. Vega Profile


**Straddle vega:**
$$
\mathcal{V}_{\text{straddle}} = \mathcal{V}_{\text{call}} + \mathcal{V}_{\text{put}}
$$

**ATM vega is maximized:**
$$
\mathcal{V}_{\text{ATM}} = S\sqrt{T-t}\phi\left(\frac{\log(S/K)}{\sigma\sqrt{T-t}}\right)
$$

where $\phi$ is standard normal PDF.

**Key insight:** Straddle benefits from IV increases regardless of direction.

**IV change impact:**
$$
\Delta\Pi \approx \mathcal{V} \cdot \Delta\sigma_{\text{implied}}
$$

Example: If $\mathcal{V} = 100$ and IV increases by 5 points (0.05), profit = $100 \times 0.05 = \$5$.

### 4. Theta Decay


**Straddle theta:**
$$
\Theta_{\text{straddle}} = \Theta_{\text{call}} + \Theta_{\text{put}} < 0
$$

**Daily time decay:**
$$
\Theta_{\text{daily}} \approx -\frac{S\sigma\sqrt{T}}{2\sqrt{\pi T}} \cdot \frac{1}{\sqrt{365}}
$$

**Acceleration pattern:**
$$
|\Theta(T)| \propto \frac{1}{\sqrt{T}}
$$

Theta is most painful in final weeks. Daily dollar loss accelerates as expiration approaches.

**Example calculation:**

30-day ATM straddle on $100 stock with 30% IV:
$$
\text{Premium} \approx 100 \times 0.30 \times \sqrt{30/365} \approx \$8.64
$$
$$
\text{Average daily theta} \approx -\$8.64/30 \approx -\$0.29
$$

But actual theta near expiry can be $-\$0.50$ or more per day!

### 5. Greek Interactions


**P&L attribution over small time interval:**
$$
d\Pi = \underbrace{\Delta dS}_{\text{delta}} + \underbrace{\frac{1}{2}\Gamma(dS)^2}_{\text{gamma}} + \underbrace{\mathcal{V}d\sigma}_{\text{vega}} + \underbrace{\Theta dt}_{\text{theta}}
$$

**Daily trade-off:**

Each day you hold:

- **Lose:** $\Theta dt < 0$ (certain loss)
- **Gain:** $\frac{1}{2}\Gamma(dS)^2$ (if stock moves)
- **Uncertain:** $\mathcal{V}d\sigma$ (depends on IV changes)

**Break-even movement:**

For gamma gains to offset theta losses:
$$
\frac{1}{2}\Gamma(dS)^2 = -\Theta dt
$$
$$
|dS| = \sqrt{\frac{-2\Theta dt}{\Gamma}}
$$

Example: If $\Theta = -0.30$, $\Gamma = 0.05$, $dt = 1$ day:
$$
|dS| = \sqrt{\frac{2 \times 0.30}{0.05}} = \sqrt{12} \approx \$3.46
$$

Stock needs to move $3.46 just to break even on theta that day!

### 6. Greek Changes Over Time


**Gamma evolution near expiry:**

```
Days to Expiry:
30 days:  -------- (low gamma, spread out)
10 days:  -----    (moderate gamma)
3 days:   ---      (high gamma spike at ATM)
1 day:    -|       (massive gamma spike, but worthless if OTM)
```

**Theta evolution near expiry:**

```
Days to Expiry:
30 days:  $0.29/day  (slow burn)
10 days:  $0.50/day  (faster)
3 days:   $0.90/day  (rapid decay)
1 day:    $1.50/day  (extreme)
```

**Strategic implication:** Long straddles are better for medium-term (30-60 days) where theta is manageable. Short straddles are better for final week where theta collection is maximized (but gamma risk is extreme).

---

## Time Evolution


### 1. The Life Cycle of a Straddle


**T-30 days (Entry):**

Position characteristics:

- Premium: $8.64 (example)
- Delta ≈ 0
- Gamma moderate
- Vega high
- Theta: -$0.29/day

**T-20 days:**

If stock unchanged:

- Value: $6.50 (lost $2.14 to theta)
- Theta accelerating: -$0.35/day
- Still have time for move

**T-10 days:**

If stock unchanged:

- Value: $3.80 (lost $4.84 total)
- Theta severe: -$0.50/day
- Getting worried...

**T-3 days:**

If stock unchanged:

- Value: $1.20 (lost $7.44 total)
- Theta extreme: -$0.90/day
- Emergency mode!

**T-0 (Expiration):**

If stock unchanged:

- Value: $0
- Total loss: $8.64 (100%)
- Game over

### 2. Topic 


**T-25 days:** Stock jumps to $108 (+8%)

Immediate effects:

- Intrinsic: $8
- Time value remaining: ~$4
- **Total value: $12**
- **P&L: +$3.36** (+39%)

**Decision point:**

1. **Take profit now:** Lock in 39% gain
2. **Hold:** Hope for more movement, but pay theta

**Calculation:**

Remaining 25 days will cost $0.30/day × 25 = $7.50 in theta. Stock needs to stay above $112 at expiration or drop below $88 to beat taking profit now.

**Professional approach:** Take profit! Don't fight theta.

### 3. Topic 


**T-5 days:** Stock finally moves to $106 (+6%)

Position value:

- Intrinsic: $6
- Time value: ~$1.50
- **Total value: $7.50**
- **P&L: -$1.14** (-13%)

Even with 6% move, you're still losing! Why?

**Theta destruction:**
$$
\text{Lost to theta} = \$8.64 - \$1.50 = \$7.14
$$
$$
\text{Gained from move} = \$6.00
$$
$$
\text{Net} = \$6.00 - \$7.14 = -\$1.14
$$

**Lesson:** Timing matters! Early moves are more valuable than late moves.

### 4. The Theta Race


**Visual representation:**

```
Value over time if stock doesn't move enough:

$10 |●
    |  ●
    |    ●
 $5 |      ●●
    |         ●●
    |            ●●●
  0 |________________●●●●___
    0  10  20  30  Days
```

**Critical insight:** You're in a race against time. Stock must move before theta destroys your position.

### 5. The Optimal Exit Timing


**Framework for deciding when to exit:**

**Exit immediately if:**
$$
\text{Current Profit} > E[\text{Future Profit}] - \text{Future Theta Cost}
$$

**Example calculation:**

Current position worth $12 (profit = $3.36):

- Expected future movement in 25 days: $2
- Expected theta cost: $7.50
- Expected net if hold: $12 + $2 - $7.50 = $6.50

Current value ($12) > Expected future value ($6.50) → **Exit now!**

### 6. Time to Expiration Sweet Spot


**Optimal horizon for long straddles:**

**Too short (<7 days):**

- Theta too brutal
- Need immediate large move
- Small margin for error

**Too long (>90 days):**

- Expensive premium
- Theta compounds over time
- Uncertainty too high

**Sweet spot (30-60 days):**

- Reasonable premium
- Manageable theta
- Time for catalyst to play out

**Empirical data:**

Historical win rates:

- 7-day straddles: 25% profitable
- 30-day straddles: 35% profitable  
- 60-day straddles: 40% profitable
- 90-day straddles: 38% profitable (theta drag)

### 7. The Event-Driven Advantage


**Best setup:** Buy straddle 3-7 days before known event

**Timeline:**

**T-7 days:** Buy straddle

- Premium includes event vol
- But still reasonable cost

**T-0 (Event day):** Event occurs

- Stock moves 10%
- Large profit

**T+1:** Exit immediately

- Capture intrinsic value
- Avoid post-event theta decay

**Why this works:**

You experience only 7 days of theta but capture the full event move. Optimal risk/reward.

---

## P&L Sources Decomposition


### 1. The Three Components


**Every dollar of P&L comes from exactly three sources:**

$$
\text{Total P\&L} = \underbrace{\text{Gamma P\&L}}_{\text{from movement}} + \underbrace{\text{Vega P\&L}}_{\text{from IV changes}} + \underbrace{\text{Theta P\&L}}_{\text{from time}}
$$

**Let's analyze each:**

### 2. Gamma P&L (Movement)


**Formula:**
$$
\text{Gamma P\&L} = \frac{1}{2}\Gamma \times (\Delta S)^2
$$

**Key insight:** Profit is proportional to the SQUARE of the move.

**Examples:**

$2 move: $\text{Gamma P\&L} = 0.5 \times 0.05 \times 2^2 = \$0.10$
$4 move: $\text{Gamma P\&L} = 0.5 \times 0.05 \times 4^2 = \$0.40$
$8 move: $\text{Gamma P\&L} = 0.5 \times 0.05 \times 8^2 = \$1.60$

Doubling the move gives 4× the profit! This is the convexity benefit.

**Directional symmetry:**

Move to $108: Same profit as move to $92 (symmetric)

**Cumulative gamma over multiple days:**

$$
\text{Total Gamma P\&L} = \frac{1}{2}\Gamma \sum_{i=1}^{n} (\Delta S_i)^2
$$

This is why many small moves can add up, even if net price change is small!

### 3. Vega P&L (IV Changes)


**Formula:**
$$
\text{Vega P\&L} = \mathcal{V} \times \Delta \sigma_{\text{implied}}
$$

**Examples:**

IV increases 5 points: $\text{Vega P\&L} = 100 \times 0.05 = \$5.00$ ✓

IV decreases 3 points: $\text{Vega P\&L} = 100 \times (-0.03) = -\$3.00$ ✗

**Common vega scenarios:**

**Pre-event IV expansion:**

- IV: 25% → 35% (+10 points)
- Vega P&L: +$10 (without stock moving!)
- Can exit here for profit

**Post-event vol crush:**

- IV: 35% → 20% (-15 points)  
- Vega P&L: -$15 (even if stock moved!)
- This kills many straddles

**Why vega matters:**

You can be RIGHT about movement but WRONG about timing of IV changes. If IV crushes before stock moves, you lose.

### 4. Theta P&L (Time Decay)


**Formula:**
$$
\text{Theta P\&L} = \Theta \times \Delta t
$$

**This is ALWAYS negative for long straddles:**

$$
\Theta < 0 \quad \Rightarrow \quad \text{Theta P\&L} < 0
$$

**Daily examples:**

30 days out: $-$0.29/day$
10 days out: $-$0.50/day$
3 days out: $-$0.90/day$

**Cumulative theta over 30 days:**
$$
\text{Total Theta P\&L} \approx -\$8.64
$$

This is your maximum loss if stock doesn't move!

### 5. Complete P&L Example


**Day 0:** Buy straddle for $8.64

**Day 10:** Stock moves from $100 to $107

**Component breakdown:**

1. **Gamma P&L:**
   $$\frac{1}{2} \times 0.05 \times 7^2 = \$1.23$$

2. **Vega P&L:**
   IV increased 25% → 30% (+5 points)
   $$100 \times 0.05 = \$5.00$$

3. **Theta P&L:**
   10 days × -$0.30/day $= -\$3.00$

**Total P&L:**
$$
\$1.23 + \$5.00 - \$3.00 = \$3.23
$$

**Position value:**
$$
\$8.64 + \$3.23 = \$11.87
$$

**Return:** +37%

### 6. The Critical Trade-Offs


**Daily decision:**

Every day you hold, you face:

$$
\text{Expected Gain} = E[\text{Gamma P\&L} + \text{Vega P\&L}]
$$
$$
\text{Certain Loss} = \text{Theta P\&L}
$$

**Break-even requirement:**

$$
E[\text{Gamma P\&L} + \text{Vega P\&L}] > |\text{Theta P\&L}|
$$

If this inequality doesn't hold, close the position!

### 7. Why Most Straddles Lose


**Statistical reality:**

On average:

- Gamma P&L: Slightly positive (but small daily moves)
- Vega P&L: Often negative (vol risk premium)
- Theta P&L: Definitely negative (guaranteed loss)

**Net result:** 
$$
\text{Small gains} - \text{Uncertain vega} - \text{Certain theta} < 0
$$

**But exceptions occur:**

When gamma P&L or vega P&L is large enough (events, crashes, rallies), straddles can be very profitable. You're betting on EXCEPTIONAL moves, not average outcomes.

### 8. Professional P&L Attribution


**Traders track each component separately:**

```
Daily P&L Report:
Date: [Today]
Position: Long 100 AAPL Straddles

Gamma P&L:    +$1,234  (Stock moved $3.50)
Vega P&L:     -$567    (IV dropped 2 points)
Theta P&L:    -$890    (Time decay)
─────────────────────
Net P&L:      -$223

Analysis: Stock moved right amount, but IV crush hurt us.
Consider exit if IV expected to drop further.
```

**This attribution helps you understand:**

- What's working
- What's not working
- Whether to hold or exit

### 9. The Vega-Gamma Synergy


**Best case:** Both work in your favor

**Event anticipation:**

- IV rises before event (vega P&L positive)
- Stock moves on event (gamma P&L positive)
- Exit immediately after event (avoid vol crush)

**Example:**

Buy straddle 5 days before earnings:

- Days 1-4: IV rises 25% → 35%, Vega P&L = +$10
- Day 5: Stock moves 8%, Gamma P&L = +$3.20
- Day 5: Exit immediately

**Total profit:** $13.20 - (5 × $0.30) = $11.70 on $8.64 cost = 135% return!

This is the ideal straddle scenario: ride IV expansion, capture movement, exit before vol crush.

---

## Volatility Impact


### 1. The Vega Equation


**Straddle value sensitivity to IV:**
$$
\frac{d\Pi}{d\sigma} = \mathcal{V} = S\sqrt{T-t}\phi(d_1)
$$

where $\phi$ is standard normal PDF and $d_1$ depends on moneyness.

**Key insight:** Straddle value is HIGHLY sensitive to IV changes, often more than to stock movement in short term.

### 2. IV Changes vs. Stock Movement


**Comparison:**

**5-point IV increase:**

- Vega P&L = $100 × 0.05 = $5.00

**$5 stock move:**

- Gamma P&L = $0.5 × 0.05 × 5² = $0.625

**IV change has 8× the impact!**

**Why this matters:**

You can profit from straddle WITHOUT stock moving, just from IV increasing. Conversely, stock can move but you still lose if IV crashes.

### 3. The Volatility Smile Effect


**ATM vs. OTM vega:**

ATM options (straddle strikes):

- Highest vega
- Maximum IV sensitivity

OTM options (strangle strikes):

- Lower vega
- Less IV sensitivity

**Implication:** Straddles benefit more from IV changes than strangles.

**Volatility smile impact:**

During market stress:

- ATM IV: +5 points
- OTM IV: +8 points (smile steepens)
- Strangles can actually outperform straddles!

### 4. Implied vs. Realized Volatility


**The fundamental bet:**

Long straddle bets:
$$
\sigma_{\text{realized}} > \sigma_{\text{implied}}
$$

**Realized volatility definition:**

$$
\sigma_{\text{realized}} = \sqrt{\frac{252}{n}\sum_{i=1}^{n}\left(\log\frac{S_i}{S_{i-1}}\right)^2}
$$

**Annualized** from daily log returns.

**Relationship to P&L:**

Over holding period, your profit is approximately:
$$
\text{Profit} \propto (\sigma_{\text{realized}} - \sigma_{\text{implied}}) \times \text{Vega}
$$

**Examples:**

Implied vol = 25%, Realized vol = 35%:

- **Win:** Realized exceeded implied
- Profit ≈ $(0.35 - 0.25) × 100 = $10$

Implied vol = 35%, Realized vol = 20%:

- **Lose:** Realized fell short of implied  
- Loss ≈ $(0.20 - 0.35) × 100 = -$15$

### 5. The Volatility Risk Premium


**Historical observation:**

$$
E[\sigma_{\text{implied}}] > E[\sigma_{\text{realized}}]
$$

On average, implied vol is 2-4 percentage points higher than subsequently realized vol.

**Why premium exists:**

1. **Risk aversion:** Option buyers pay for protection
2. **Fat tails:** Rare catastrophic moves
3. **Supply/demand:** Natural hedging demand
4. **Jump risk:** Discontinuous moves priced in

**Implication for straddles:**

- **Long straddles:** Fighting uphill battle (negative expected value)
- **Short straddles:** Collecting risk premium (positive expected value, but risky)

**When long straddles work:**

Despite negative expectation, long straddles profit when:

1. Exceptional events occur (earnings surprises)
2. Black swan events (crashes, squeezes)
3. IV expansion before events (sell before move happens)

### 6. IV Term Structure


**IV varies by expiration:**

```
IV by Tenor:
1-week:   28%  (high, near-term uncertainty)
1-month:  25%  (base level)
3-month:  24%  (lower, mean reversion expected)
1-year:   23%  (lowest, long-run average)
```

**Calendar effects:**

- **Earnings proximity:** IV spikes before earnings
- **FOMC meetings:** IV rises before Fed decisions  
- **Expiration weeks:** IV can be elevated or crushed

**Strategy implications:**

**Buy straddles when:**

- IV low relative to historical average
- Near-term IV < longer-term IV (backwardation)
- Before known catalysts

**Sell straddles when:**

- IV high relative to historical average
- Near-term IV > longer-term IV (contango)
- After events (vol crush)

### 7. Event-Driven Volatility Patterns


**Typical earnings pattern:**

```
IV Timeline:
T-30: 25% (base)
T-10: 28% (anticipation)
T-3:  35% (peak)
T-0:  40% (event day)
T+1:  20% (crush!)
```

**Straddle strategies:**

**Strategy 1:** Buy at T-10, sell at T-3

- Capture IV expansion
- Avoid actual event
- Take 30% profit from vega alone

**Strategy 2:** Buy at T-3, hold through event

- Ride peak IV
- Capture movement
- Risk vol crush if move is small

**Strategy 3:** Buy at T-1, sell at T+0 open

- Minimal theta exposure
- Capture overnight move
- Exit before full vol crush

### 8. Volatility Mean Reversion


**Statistical property:**

Volatility tends to revert to long-run average:
$$
\sigma_t = \theta + \phi(\sigma_{t-1} - \theta) + \epsilon_t
$$

**AR(1) model** with mean reversion coefficient $\phi < 1$.

**Trading implications:**

When IV is extremely high:

- Expect reversion to mean
- Short straddles may be profitable
- But timing is difficult!

When IV is extremely low:

- Expect eventual spike
- Long straddles may be profitable
- But can stay low for long time

**Practical rule:**

Compare current IV to:

- 30-day historical average
- 1-year percentile ranking

If current IV > 80th percentile → Consider selling
If current IV < 20th percentile → Consider buying

### 9. Volatility Clustering


**Stylized fact:**

High vol tends to follow high vol. Low vol tends to follow low vol.

$$
\text{Corr}(\sigma_t, \sigma_{t-1}) > 0
$$

**GARCH effect.**

**Trading implication:**

After a volatile day:

- Tomorrow likely to be volatile too
- Straddles may be profitable even after first move
- But be aware IV may have already adjusted

### 10. The IV-HV Spread


**Key metric for straddle traders:**

$$
\text{IV-HV Spread} = \sigma_{\text{implied}} - \sigma_{\text{historical realized}}
$$

**Interpretation:**

Spread > 0: Market pricing more vol than historical
Spread < 0: Market pricing less vol than historical (rare)

**Trading signal:**

Large positive spread → Possible short straddle opportunity (if you think realized will match historical)
Negative spread → Possible long straddle opportunity (market underpricing volatility)

**Example:**

Current IV = 35%
30-day realized = 25%
Spread = +10%

This suggests options are expensive. Short straddle may be attractive IF you believe realized will stay around 25%.

### 11. Professional Vol Trading Perspective


**Volatility traders monitor:**

1. **IV levels** (absolute)
2. **IV percentiles** (relative to history)
3. **IV term structure** (across expirations)
4. **IV skew** (across strikes)
5. **IV vs. HV spread** (richness)

**Decision matrix:**

```
Current IV vs. Historical IV:
High + Rising   → Avoid buying, consider selling
High + Falling  → Wait for better entry
Low + Rising    → Buy straddles now
Low + Falling   → Wait for inflection
```

Understanding volatility dynamics is crucial. Stock movement alone doesn't determine straddle profitability—IV changes can dominate P&L, especially short-term.

---

## Analysis


### 1. 1


**Setup:**

- Buy straddle at $100 strike for $8.64
- Day 1: Stock gaps to $108

**Analysis:**

Position value:

- Call intrinsic: $8
- Call time value: $3.20
- Put worthless: $0
- **Total: $11.20**

**P&L:** +$2.56 (+30%)

**Greeks update:**

- Delta: Now +0.85 (dominated by call)
- Gamma: Lower (further from ATM)
- Vega: Lower (less sensitive)
- Theta: Lower (less premium to decay)

**Decision framework:**

✓ **Take profit:** Already profitable, lock in gain
✗ **Hold:** Exposed to reversal, theta continues

**Professional choice:** Take profit. Don't get greedy.

### 2. 2


**Setup:**

- Buy straddle for $8.64
- Stock drifts up gradually over 30 days

**Timeline:**

Day 10: Stock at $102

- Position value: $6.50
- P&L: -$2.14 (-25%)

Day 20: Stock at $104

- Position value: $5.20
- P&L: -$3.44 (-40%)

Day 30: Stock at $106

- Position value: $6.00 (intrinsic only)
- P&L: -$2.64 (-31%)

**Why you're losing despite 6% move:**

Move happened too slowly! Theta consumed more value than gamma generated.

**Lesson:** Need large, FAST moves for straddles to work.

### 3. 3


**Setup:**

- Buy straddle for $8.64
- Stock stays at $100
- But IV increases 25% → 40%

**Analysis:**

Position value:

- Intrinsic: $0
- Time value with higher IV: $12.40
- **Total: $12.40**

**P&L:** +$3.76 (+44%)

**This is why straddles are volatility trades!**

**Decision framework:**

✓ **Take profit:** IV spike may not last
✗ **Hold:** Hoping for stock movement too

**Professional choice:** Usually take profit from IV expansion. Don't wait for movement.

### 4. 4


**Setup:**

- Buy straddle 1 day before earnings for $10
- Stock moves 5% but IV collapses 40% → 20%

**Component analysis:**

Gamma P&L: +$1.25 (from 5% move)
Vega P&L: -$6.00 (from IV collapse)
Theta P&L: -$0.50 (1 day)

**Net P&L:** +$1.25 - $6.00 - $0.50 = -$5.25

**Position value:** $4.75
**Loss:** -$5.25 (-53%)

**This is the vol crush trap!** Stock moved but you still lost.

**Lesson:** Consider exiting BEFORE event if IV has already expanded enough.

### 5. 5


**Setup:**

- Buy straddle for $8.64
- Stock whipsaws violently

**Timeline:**

Day 1: $100 → $108 (+8%)
Day 2: $108 → $97 (-10%)
Day 3: $97 → $105 (+8%)
Day 5: $105 → $100 (-5%)

**End result:** Stock back at $100!

**But straddle is profitable:**

Each large move generated gamma P&L:

- Move 1: +$1.60
- Move 2: +$2.00
- Move 3: +$1.60
- Move 4: +$0.63

**Total gamma:** +$5.83
**Theta cost:** -$1.50 (5 days)

**Net P&L:** +$4.33 (+50%)

**Key insight:** Direction doesn't matter, VOLATILITY matters. Realized vol exceeded implied vol even though stock ended flat!

### 6. 6


**Setup:**

- Buy straddle for $8.64
- Stock stays between $98-$102 for 30 days

**Timeline:**

Day 10: Value $6.50 (-25%)
Day 20: Value $4.20 (-51%)
Day 30: Value $0 (-100%)

**What happened:**

Stock moved slightly but not enough:

- Daily moves: 0.5-2% (small)
- Gamma generated: $0.50 total
- Theta lost: $8.64
- **Net: -$8.14** (total loss)

**This is the most common outcome.** Theta wins.

**Lesson:** If stock isn't moving enough, exit early. Don't hope for a miracle.

### 7. 7


**Setup:**

- Hold straddle during unexpected crisis
- Stock crashes 30% overnight

**Analysis:**

Position value:

- Call worthless: $0
- Put intrinsic: $30
- **Total: $30**

**P&L:** +$21.36 (+247%)

**This is the lottery ticket scenario.** Rare but massive payoff.

**Why straddles are tail risk hedges:**

During market crashes:

- Portfolios down 20-40%
- Straddles up 200-400%
- Provides crucial hedge

### 8. 8


**Setup:**

- Buy straddle 2 weeks before known event
- Exit 1 day before event

**Timeline:**

T-14: Buy at IV = 25% for $8.64
T-1: IV = 40%, stock moved only 2%

**Position value:**

Gamma contribution: +$0.20
Vega contribution: +$6.00
Theta cost: -$4.20

**Total value:** $10.64
**P&L:** +$2.00 (+23%)

**Exit before event** and avoid vol crush!

**Strategy:** This "IV expansion play" is often more reliable than holding through events. You're trading volatility, not outcome.

### 9. Comparison Matrix


| Scenario | Stock Move | IV Change | Duration | P&L | Key Lesson |
|----------|-----------|-----------|----------|-----|------------|
| Immediate move | +8% | Neutral | 1 day | +30% | Take profit fast |
| Slow drift | +6% | Neutral | 30 days | -31% | Speed matters |
| IV spike | 0% | +15pts | 10 days | +44% | Volatility is king |
| Vol crush | +5% | -20pts | 1 day | -53% | Exit before events |
| Whipsaw | 0% net | Neutral | 5 days | +50% | Realized vol matters |
| Slow death | ±2% | Neutral | 30 days | -100% | Exit losers early |
| Black swan | -30% | +30pts | 1 day | +247% | Lottery ticket |
| IV expansion | +2% | +15pts | 14 days | +23% | Trade the vol, not event |

### 10. Professional Planning


**Before entering straddle, map out:**

1. **Best case:** Large immediate move or IV spike
   - Target: +40-50%
   - Exit trigger: Hit target or 3-5 days elapsed

2. **Base case:** Moderate move over time
   - Target: +15-20%
   - Exit trigger: 50% of time elapsed, adjust based on P&L

3. **Worst case:** No move, theta decay
   - Stop loss: -30-40%
   - Exit trigger: Position down 30% OR 1 week with no meaningful movement

**Example decision tree:**

```
Entry → Day 5 checkpoint:
├─ Up >30% → Exit (take profit)
├─ Down >30% → Exit (stop loss)
└─ Flat → Evaluate:
    ├─ Still bullish on move? → Hold
    └─ Losing conviction? → Exit now
```

**Statistical reality check:**

Based on historical data:

- 30% of straddles: Large profit (>50%)
- 20% of straddles: Small profit (10-50%)
- 50% of straddles: Loss (theta wins)

Your job is to maximize exposure to first category, minimize exposure to third category.

---

## Real-World Trading Examples


### 1. Pension Duration Cut via Futures


**Setup (T-7 days before earnings):**

- TSLA trading at $250
- Implied vol: 65% (elevated)
- 1-week ATM straddle cost: $28 (11.2% of stock price)
- Breakevens: $222 and $278

**Trade thesis:**

"Earnings will cause large move. IV is high but justified."

**Day 1-6:** Hold through week

IV increases: 65% → 75%
Vega P&L: +$7
Theta P&L: -$4

Position value: $31

**T-0 (Earnings):** Stock gaps to $210 (-16%)

**Analysis:**

Position value:

- Put intrinsic: $40
- Remaining time value: $3
- **Total: $43**

**P&L:** +$15 (+54%)

**Post-trade analysis:**

✓ Correctly anticipated large move
✓ Move exceeded breakeven requirement
✓ 54% return in 1 week

**Lessons:**

1. High IV was justified (realized vol even higher)
2. Early exit (T-1 at $31) would have given 11% profit—took risk to wait
3. Directional uncertainty resolved by straddle structure

### 2. Transition Risk Hedge


**Setup (T-2 days before FOMC):**

- SPY at $450
- Implied vol: 18% (high for SPY)
- 2-day ATM straddle cost: $6.50 (1.44% of stock price)
- Breakevens: $443.50 and $456.50

**Trade thesis:**

"FOMC might surprise. Need 1.5% move, seems likely."

**T-0 (FOMC announcement):** 

Fed does exactly what expected. SPY moves to $451 (+0.22%)

IV collapses: 18% → 11%

**Analysis:**

Position value:

- Call intrinsic: $1
- Vega loss from vol crush: -$5
- **Total: $1**

**P&L:** -$5.50 (-85%)

**Post-trade analysis:**

✗ Overestimated probability of surprise
✗ Didn't account for "non-event" scenario  
✗ IV crush was brutal post-announcement

**Lessons:**

1. SPY straddles are expensive (hard to profit)
2. "Priced-in" events are real risk
3. Should have exited when no surprise materialized

### 3. Portable Alpha with Futures


**Setup (T-3 days before FDA decision):**

- Biotech stock at $40
- Binary event: Approval (expected surge) or denial (expected crash)
- Implied vol: 110% (extreme)
- 3-day ATM straddle cost: $10 (25% of stock price!)
- Breakevens: $30 and $50

**Trade thesis:**

"This will be binary and violent. 25% breakeven is steep but move will be larger."

**T-0 (FDA decision):** Approval! Stock surges to $75 (+88%)

**Analysis:**

Position value:

- Call intrinsic: $35
- **Total: $35**

**P&L:** +$25 (+250%)

**Post-trade analysis:**

✓ Correctly anticipated binary nature
✓ Massive move justified high premium
✓ 250% return in 3 days (but high risk!)

**Lessons:**

1. Binary events can justify expensive straddles
2. Small biotech has wider possibility space than mega-cap
3. This was a bet, not a trade (massive uncertainty)

### 4. Tactical Duration Extension


**Setup:**

- Stable large-cap at $100
- No events expected
- IV: 22% (low)
- 30-day straddle cost: $6.30
- Breakevens: $93.70 and $106.30

**Trade thesis:**

"IV is cheap, something could happen."

**Timeline:**

Day 10: Stock at $101, position value $4.80 (-24%)
Day 20: Stock at $99, position value $3.20 (-49%)
Day 30: Stock at $100, position value $0 (-100%)

**Analysis:**

Stock stayed in $98-$102 range entire time:

- Max intraday move: 1.8%
- Realized vol: 15% (below implied 22%)
- Theta destroyed position

**P&L:** -$6.30 (-100%)

**Post-trade analysis:**

✗ No catalyst (why expect move?)
✗ "Cheap IV" not sufficient thesis
✗ Should have exited by day 10 when no movement

**Lessons:**

1. Need REASON to expect movement, not just "cheap" options
2. Exit losers early (would have saved 50% by cutting on day 10)
3. Range-bound stocks stay range-bound

### 5. Duration Hedge Failure in Crisis


**Setup (T-10 before earnings):**

- Stock at $150
- IV: 30% (below historical avg of 45% pre-earnings)
- 10-day straddle cost: $9

**Trade thesis:**

"IV will rise into earnings. Exit before event."

**Timeline:**

Day 1-7: IV gradually rises 30% → 42%
Day 7: Stock at $152

**Analysis at Day 7:**

Position value:

- Intrinsic: $2
- Time value with higher IV: $11
- **Total: $13**

**P&L:** +$4 (+44%)

**Decision:** Exit here (T-3 before earnings)

**What happened next:**

T-0 (Earnings): Stock moved 8% but IV crushed to 25%
Straddle would have been worth $10 (only +$1 from entry)

**Post-trade analysis:**

✓ Captured IV expansion without event risk
✓ Avoided vol crush
✓ 44% return in 7 days by trading vol, not direction

**Lessons:**

1. IV expansion can be more predictable than stock movement
2. Don't have to hold through event to profit
3. Sometimes "IV expansion play" is the real trade

### 6. Example 6


**Setup:**

- Volatile tech stock at $100
- Earnings just passed (IV: 35% → 45% this week after guidance)
- 5-day straddle cost: $4.80

**Trade thesis:**

"Post-earnings volatility often spills into next week."

**Timeline:**

Day 1: $100 → $108 (+8%)
Day 2: $108 → $98 (-9%)
Day 3: $98 → $104 (+6%)
Day 4: $104 → $99 (-5%)
Day 5: $99 → $101 (+2%)

**Net stock move:** +1% from entry

**But realized vol was huge!**

**Analysis:**

Gamma P&L from moves: +$3.80
Vega P&L (IV stayed elevated): +$1.20
Theta P&L: -$1.50

Position value at Day 5: $7.50

**P&L:** +$2.70 (+56%)

**Post-trade analysis:**

✓ Stock ended near entry but straddle profitable
✓ High realized vol exceeded implied vol
✓ This is textbook "path matters more than endpoint"

**Lessons:**

1. Realized vol ≠ directional move
2. Multiple large moves profitable even if they cancel out
3. Post-event volatility continuation can be tradeable

### 7. Key Patterns Across Examples


**Winners had:**

- Specific catalyst for movement
- Correct timing (enter close to event)
- Exit strategy (took profits or cut losses)
- Reasonable cost relative to expected move

**Losers had:**

- Vague thesis ("might move")
- No catalyst or wrong catalyst
- Held too long (theta killed)
- Underestimated vol crush

**Professional checklist before entering:**

1. □ Is there a specific catalyst?
2. □ Is timing optimal (days from catalyst)?
3. □ Is breakeven reasonable (< 1 std dev)?
4. □ Do I have exit plan (profit target AND stop loss)?
5. □ Am I prepared for vol crush (if event trade)?
6. □ Is this position sized properly (2-5% of portfolio)?

If any answer is no, reconsider the trade.

---

## Common Pitfalls


### 1. Pitfall 1


**The mistake:**

Buying straddle and thinking "I'll hold to expiration and see what happens."

**Why it's wrong:**

Theta accelerates near expiration. Last week loses 40% of remaining value. Final day can lose 80% of remaining value.

**Example:**

10 days out: Position worth $5
3 days out: Position worth $2 (lost 60%)
Expiration: Position worth $0 (lost 100%)

**If stock moves 4% on final day:** Now worth $4 (still down 20% from 10 days ago!)

**Lesson:** Exit early, even with profit. Don't fight theta acceleration.

**Professional approach:**

Set calendar-based exit:

- Entered 30-day straddle → Exit by day 20 regardless
- Never hold last week
- Exception: Very specific event on expiration day

### 2. Pitfall 2


**The mistake:**

Seeing high IV and thinking "Big move expected! Buy straddle!"

**Why it's wrong:**

High IV usually means market already pricing in large move. You're buying after expectation is elevated.

**Example:**

Stock normally trades at 25% IV
Before earnings, IV at 55%
Straddle costs $12 instead of usual $6

Stock moves 10% (large move!):

- In normal vol environment: Profit of $4 (breakeven $6)
- In high vol environment: Loss of $2 (breakeven $12)

**Same move, different outcome** due to entry cost.

**Lesson:** Compare current IV to:

1. Historical IV percentile
2. Post-event typical collapse

Buy when IV is LOW relative to expected move, not HIGH.

### 3. Pitfall 3


**The mistake:**

"I'll buy before earnings and hold through. Stock will move!"

**The reality:**

```
Before earnings: IV = 60%, Straddle = $15
After earnings: IV = 30%, Stock moved 8%
Straddle now: $10

Stock moved 8% but you LOST 33%!
```

**Why it happens:**

Vol crush can overwhelm directional profit. The $5 loss from vega > $2 gain from gamma.

**Lesson:** 

For event trades, consider:

1. Buy early (T-10), exit before event (T-1)
2. Accept you're trading IV expansion, not outcome
3. If holding through event, ensure breakeven accounts for vol crush

**Vol crush insurance:**

Calculate required move for breakeven AFTER accounting for typical post-event IV:

$$
\text{Required Move} = \frac{\text{Premium}_{\text{pre-event}}}{\text{Expected Value}_{\text{post-event}}}
$$

### 4. Pitfall 4


**The mistake:**

"Maximum loss is premium paid, so I don't need a stop."

**Why it's wrong:**

While technically true (you can't lose more than premium), you CAN lose 80-90% waiting for miracle.

**Example:**

Entry: $10
After 2 weeks of no movement: $4 (down 60%)
"I'll hold, maybe it moves!"
Expiration: $0 (down 100%)

**Better approach:**

Exit when position down 30-40%:

- Entry: $10
- Exit at $6 (down 40%)
- Saved: $6 to deploy elsewhere

**Lesson:** Capital preservation matters. Losing 40% < losing 100%.

**Stop loss rule:**

If position down 30-40% AND:

- No movement yet
- >50% of time elapsed
- No clear catalyst soon

→ **Exit immediately.**

### 5. Pitfall 5


**The mistake:**

"This straddle can't lose more than premium, so I'll risk 20% of portfolio!"

**The disaster:**

10 straddles at 20% each means:

- All could expire worthless
- Lose 20% of entire portfolio
- Happened in 3 weeks

**Proper sizing:**

Risk only 2-5% per straddle trade:

- $100k portfolio → $2k-5k per trade
- Lose entire premium → Only down 2-5%
- Can survive 20 consecutive losses

**Why this matters:**

Straddles have ~60-70% loss rate. You need MANY attempts to hit the big winners. Proper sizing ensures survival.

**Lesson:** Position size for MULTIPLE losses before a win.

### 6. Pitfall 6


**The mistake:**

Buying 90-day straddles thinking "More time = safer"

**Why it's wrong:**

Longer time = more theta to pay. Unless move happens early, theta compounds.

**Example:**

90-day straddle: $15 (high premium)
After 30 days: Down to $10 (lost $5)
Still 60 days left but already down 33%!

**Better approach:**

30-45 day straddles:

- Lower absolute premium
- Still enough time for catalyst
- Less compounded theta

**Lesson:** Optimal horizon is 30-45 days for most straddles. Longer is not safer.

### 7. Pitfall 7


**The mistake:**

"This stock seems quiet. Options cheap. Maybe it'll move?"

**Why it's wrong:**

Cheap options are cheap for a reason: low probability of movement. No catalyst = no move likely.

**Example:**

Boring utility company at $50
IV: 15% (low)
30-day straddle: $1.80

After 30 days: Stock at $50.20
Straddle expires worthless
100% loss

**Lesson:** Need SPECIFIC catalyst:

- Earnings (✓)
- FDA decision (✓)
- Merger talk (✓)
- "Something might happen" (✗)

**Catalyst checklist:**

□ Specific event identified
□ Event date known  
□ Event is binary or high-impact
□ Market may be underpricing event

### 8. Pitfall 8


**The mistake:**

After losing on straddle, immediately buying another to "make it back"

**The psychology:**

Loss hurts → Emotional need to recover → Take bigger risk → Lose more

**Example:**

Trade 1: Lost $2k on AAPL straddle
Feeling: "I need to make this back NOW"
Trade 2: Buy $5k TSLA straddle (2.5× size!)
Result: Lose $5k more
Total loss: $7k (could have been $2k)

**Lesson:** After losing trade:

1. Take break (at least 1 day)
2. Analyze what went wrong
3. Return with normal position size
4. Never increase size after loss

### 9. Pitfall 9


**The mistake:**

Stock not moving, but "I know it will eventually" → Hold losing position

**The reality:**

If stock hasn't moved in 50% of time elapsed, probability of profitable move in remaining time is LOW.

**Example:**

30-day straddle
Day 15: Stock moved only 1% (need 5% to breakeven)
Holding value: $3 (down 50%)

"It HAS to move soon!" → Hold
Day 30: Expires worthless

**Better approach:**

Day 15: Accept defeat, exit at $3
Saved: $3 to redeploy elsewhere

**Lesson:** If not working by mid-point, unlikely to work. Cut losses.

### 10. Pitfall 10


**The mistake:**

Buying straddles constantly, on every stock, always in market

**Why it's wrong:**

Most straddles lose. Doing too many means death by thousand cuts.

**Example:**

Place 20 straddle trades per month:

- 14 lose (70%): -$70
- 6 win (30%): +$60
- **Net: -$10** despite winning trades!

**Better approach:**

High-quality setups only:

- 2-3 trades per month
- Strong catalysts only
- Better win rate (40-50%)
- Larger average wins

**Lesson:** Quality > Quantity. Be selective.

### 11. Summary


**Risk management:**

1. Always have stop loss (-30-40%)
2. Exit before final week
3. Size positions properly (2-5%)

**Trade selection:**

1. Need specific catalyst
2. Enter when IV reasonable
3. Know event timing precisely

**Emotional control:**

1. No revenge trading
2. Accept losses quickly
3. Don't fight the tape

**Remember:** Most pitfalls come from either:

- Improper risk management (sizing, stops, exits)
- Poor trade selection (no catalyst, expensive IV)
- Emotional errors (revenge, hope, anchoring)

Professional traders avoid these through discipline and checklist adherence.

---

## Position Management


### 1. Entry Checklist


**Before placing any straddle trade, verify:**

**Catalyst & Timing:**

- [ ] Specific catalyst identified (earnings, FDA, FOMC, etc.)
- [ ] Catalyst date confirmed
- [ ] Entry is 3-7 days before catalyst (optimal window)
- [ ] No earlier conflicting events

**Volatility Assessment:**

- [ ] Current IV vs. historical percentile checked
- [ ] Current IV < historical pre-event average (cheaper entry)
- [ ] Expected IV expansion path mapped
- [ ] Post-event vol crush quantified

**Cost-Benefit:**

- [ ] Breakeven calculated as % of stock price
- [ ] Breakeven is achievable (< 1 std dev of expected move)
- [ ] Premium relative to event probability justified
- [ ] Compared to historical similar setups

**Risk Management:**

- [ ] Position size = 2-5% of portfolio
- [ ] Stop loss defined (-30-40% from entry)
- [ ] Profit target defined (+40-50% or higher)
- [ ] Calendar-based exit planned

**Example entry decision:**

```
Trade: AAPL earnings straddle
Stock: $180
Days to event: 5
IV: 32% (below 45% historical pre-earnings avg)
Cost: $8.50 (4.7% of stock)
Breakeven: ±4.7%

✓ Catalyst: Earnings in 5 days
✓ IV: Below historical, room to expand
✓ Breakeven: Achievable (last 4 quarters averaged 6% move)
✓ Size: $5k position on $100k portfolio (5%)
✓ Exit: Take profit at $12 (+41%) or stop at $6 (-29%)

→ APPROVED for entry
```

### 2. Monitoring Framework


**Daily check (5 minutes):**

Track three numbers:

1. Current position value
2. Days to expiration
3. Current IV level

**Example dashboard:**

```
Day 3 of 30-day TSLA straddle:
Current value: $32.50 (entry: $28)
P&L: +$4.50 (+16%)
DTE: 27 days
IV: 68% (entry: 65%)
```

**Action triggers:**

**Green (good):**

- P&L: +16%
- IV: Up 3 points
- → Continue holding, watch for profit target

**Weekly deep dive (30 minutes):**

Decompose P&L:

- Gamma contribution
- Vega contribution  
- Theta cost

**Example analysis:**

```
Week 1 Summary:
Gamma P&L: +$2.20 (stock moved $7)
Vega P&L: +$3.80 (IV up 3 pts)
Theta P&L: -$1.50 (7 days × -$0.21)
────────────────────
Net: +$4.50

Stock move: Good but not enough yet
IV trajectory: Favorable, expanding as expected
Theta burn: On track

Decision: HOLD, thesis intact
```

### 3. Exit Decision Framework


**Exit immediately if ANY of:**

**Profit-taking triggers:**

1. Hit profit target (+40-50%)
2. IV expanded significantly (>10 points) regardless of stock move
3. Large favorable move (stock beyond breakeven)
4. Event happened and captured most value

**Stop-loss triggers:**

1. Position down 30-40%
2. IV collapsed unexpectedly
3. Catalyst cancelled/postponed
4. More than 50% of time elapsed with no significant movement

**Time-based triggers:**

1. Entered last week (never hold through last week except for specific expiry events)
2. Calendar-based exit reached (e.g., day 20 of 30-day straddle)

**Example exit decisions:**

**Scenario A: Take profit**
```
Entry: $10
Current: $14.50 (+45%)
DTE: 23 days
Decision: EXIT

Rationale: 

- Hit profit target
- Still have theta risk
- Don't get greedy
```

**Scenario B: Stop loss**
```
Entry: $10
Current: $6.50 (-35%)
DTE: 18 days
No meaningful stock movement
Decision: EXIT

Rationale:

- Approaching stop loss threshold
- Time elapsed without movement
- Preserve remaining capital
```

**Scenario C: IV expansion exit**
```
Entry: $10 (IV: 30%)
Current: $13.80 (+38%, IV: 45%)
DTE: 25 days
Stock moved only 2%
Decision: EXIT

Rationale:

- IV expanded 15 points (huge)
- Most profit from vega
- Exit before potential vol crush
```

**Scenario D: Hold through**
```
Entry: $10
Current: $11.20 (+12%)
DTE: 26 days
Catalyst in 3 days
Stock positioned well
Decision: HOLD

Rationale:

- Small profit, room for more
- Catalyst still coming
- Thesis intact
- Not at any exit trigger
```

### 4. Adjustment Strategies


**Question:** "Can I adjust a losing straddle?"

**Answer:** Generally NO for directional straddles, but here are rare exceptions:

**Option 1: Roll Forward**

If position down due to theta but thesis still valid:

Action: Close current straddle, open further-dated straddle

Example:

- Current 10-day straddle: $4 (entry: $8, down 50%)
- Close and pay $4
- Open 30-day straddle: $10
- **Total invested: $14** (original $8 + rollforward $6)

**Only if:**

- Strong conviction in catalyst still coming
- Willing to commit more capital
- New breakeven still achievable

**Option 2: Exit One Leg**

If stock moved strongly one direction:

Action: Close losing leg, hold winning leg

Example:

- Stock moved from $100 to $115
- Call now worth $18, put worth $0.50
- Close put, hold call
- **Now just a long call position**

**Transforms straddle → directional bet.** Only do if you now have directional view.

**Option 3: Scale Out**

If profitable, reduce risk:

Action: Close 50-75% of position, let rest ride

Example:

- Position up 40% 
- Close 70% at +40%
- Hold 30% with "house money"
- **Locked in most profit, kept upside exposure**

**Best for:** Event trades where you think there's more to come but want to lock profits.

### 5. Multi-Leg Position Management


**If running multiple straddles simultaneously:**

**Correlation risk:**

Don't buy straddles on highly correlated stocks:

Bad: AAPL + MSFT + GOOGL straddles (tech correlation ~0.7)
Good: AAPL + XLE + GLD straddles (low correlation)

**Portfolio Greeks:**

Track aggregate exposure:

- Total gamma
- Total vega
- Total theta

Example:
```
Portfolio of 3 straddles:

           Delta  Gamma  Vega  Theta
Straddle 1:  0    0.05   100   -30
Straddle 2:  0    0.04    80   -25
Straddle 3:  0    0.06   120   -35
──────────────────────────────────
Total:       0    0.15   300   -90

Daily expected movement break-even:
With combined Gamma = 0.15 and Theta = -90:
|dS| = sqrt(2×90/0.15) = $34.6 move needed across all positions
```

**Concentration limits:**

Never allocate >15% of portfolio to straddles simultaneously:

- Max 3 positions at 5% each
- Total theta manageable
- Diversification maintained

### 6. The Day-Before Decision


**You're holding straddle with earnings tomorrow. What do you do?**

**Decision tree:**

**Is position profitable?**

→ **YES, profitable:** 

- Take profits now (avoid vol crush risk)
- Exception: If profit is small (<20%) and move hasn't happened yet, might hold

→ **NO, losing:**

- Is stock positioned near breakeven?
  - YES → Hold through event (last chance)
  - NO → Exit now, save remaining value

**Example scenarios:**

**Scenario 1:** Position up 35%, stock moved 4%
→ **EXIT.** Lock profit, avoid vol crush.

**Scenario 2:** Position down 20%, stock at $98 (entry $100, breakeven $92)
→ **EXIT.** Stock not close enough to breakeven.

**Scenario 3:** Position down 10%, stock at $93 (breakeven $92)  
→ **HOLD.** Close to breakeven, worth the risk.

**Scenario 4:** Position up 60%, stock moved 10%
→ **EXIT.** Great profit, don't get greedy.

**Professional rule:** Bias toward exiting profitable positions before events. Vol crush often exceeds directional gain.

### 7. Post-Trade Review


**After every straddle trade (win or lose), document:**

1. **Entry conditions:**
   - Stock price, IV, DTE
   - Catalyst and timing
   - Thesis

2. **What happened:**
   - Actual stock move
   - IV path
   - Timing of move

3. **Exit decision:**
   - Why exited when exited
   - P&L at exit
   - Days held

4. **What I learned:**
   - What worked
   - What didn't work
   - What to do differently

**Example post-trade review:**

```
Trade: NFLX Earnings Straddle
Date: Q3 2024

Entry:

- Price: $440, IV: 58%, 7 DTE
- Cost: $31 (7.0% breakeven)
- Thesis: Subscriber growth surprise expected

What happened:

- Held 7 days through earnings
- Stock moved to $465 (+5.7%)
- IV crushed 58% → 35%
- Exit value: $27 (intrinsic $25 + $2 time value)

P&L: -$4 (-13%)

What I learned:
✗ Breakeven too wide (7%) for typical NFLX move (5%)
✗ Didn't exit before event despite profitable IV expansion
✓ Position sizing was appropriate (no portfolio damage)

Next time:

- Exit before event if IV expands >10 points
- Use tighter breakeven requirement (<5%)
```

**Keep a journal.** Patterns emerge. You'll notice:

- Which setups consistently work
- Which consistently fail
- Your behavioral tendencies

### 8. Advanced


**Professional traders monitor real-time Greeks:**

```
Position: AAPL 30-day Straddle ($180 strike)

Current Greeks:
Delta: -0.02 (slightly negative from skew)
Gamma: 0.047 (high)
Vega: 124 (very high)
Theta: -$42/day (ouch)

Break-even movements:
1-day: Need $30 move to offset theta
1-week: Need cumulative realized vol of 42% (implied is 35%)

Risk metrics:
Max loss: $850 (premium paid)
Current loss: $180 (21%)
Days to stop-loss trigger: 3-4 more losing days

Alerts:
⚠ Theta burning $42/day  
✓ Vega exposure favorable (IV low vs. historical)
```

**Having this dashboard helps you:**

- Make rational decisions
- Avoid emotional responses
- Know when to hold vs. fold
- Understand sources of P&L

**Bottom line:** Position management separates professionals from amateurs. Entry is 20% of success. Management is 80%.

---



## Pedagogical Note


**Where this fits in your curriculum:**

**Option A: Chapter 1.5 (Before Gamma Scalping)**
```

1. Delta Hedging (foundation)
1.5. Straddles/Strangles (simple vol bet) ← Insert here!

2. Gamma Scalping (refined vol bet)
3. Vega Trading
... etc.
```

**Why:** Shows the "why" for delta hedging (to remove the directional risk that straddles have)

**Option B: Chapter 2.5 (After Gamma Scalping)**
```

1. Delta Hedging
2. Gamma Scalping
2.5. Straddles/Strangles ← Insert here as "simpler alternative"

3. Vega Trading
... etc.
```

**Why:** Shows straddles as "lazy gamma scalping" for comparison

**Recommendation:** **Option A** (before gamma scalping) is pedagogically stronger. Students learn the simple approach first, then see how to refine it.