# Crypto Vol Regimes

**Crypto volatility regimes** represent distinct statistical environments characterized by dramatically different realized and implied volatility levels—ranging from low-vol "grind" periods (20-40% annual volatility, tight trading ranges, declining open interest) to medium-vol "trend" phases (40-80% annual volatility, directional momentum, rising open interest) to extreme-vol "crisis" events (100-200%+ annualized volatility, >20% daily moves, liquidation cascades)—each requiring fundamentally different risk management approaches, position sizing rules, leverage constraints, and trading strategies, with regime transitions often occurring abruptly (within hours) and persisting for weeks to months, making regime identification and adaptive positioning critical for survival and alpha generation in cryptocurrency markets.

---

## The Core Insight

**The fundamental idea:**

- Crypto volatility is not constant (violates Black-Scholes assumption)
- Distinct regimes with persistent characteristics
- Low-vol: 20-40% annual (boring, range-bound, opportunity elsewhere)
- Medium-vol: 40-80% annual (tradeable trends, optimal for strategies)
- High-vol: 80-150% annual (dangerous, reduce exposure)
- Extreme-vol: 150%+ annual (crisis, survival mode)
- Regime persistence: Days to months (not random walk)
- Transitions: Often sudden (hours), triggered by events
- Trading implications: Same strategy fails across regimes
- Risk management: Adapt position size to regime (10× in low-vol, 1× in extreme-vol)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/crypto_volatility_regimes.png?raw=true" alt="crypto_volatility_regimes" width="700">
</p>
**Figure 1:** Crypto volatility regime framework showing four distinct environments (low 20-40%, medium 40-80%, high 80-150%, extreme 150%+), characteristic behaviors (open interest patterns, funding rates, price action), transition triggers, appropriate strategies per regime, and position sizing rules for risk management.

**You're essentially asking: "What volatility environment are we in, and how should I trade it?"**

---

## Defining Volatility Regimes

### 1. Realized Volatility Calculation

**Standard definition:**

$$
\sigma_{\text{realized}} = \sqrt{\frac{252}{N} \sum_{i=1}^N r_i^2}
$$

Where:
- $r_i = \ln(P_i / P_{i-1})$ (log returns)
- $N$ = Number of observations (typically 21 or 30 days)
- $252$ = Trading days per year (crypto: 365)

**Crypto adjustment:**

$$
\sigma_{\text{crypto}} = \sqrt{\frac{365}{N} \sum_{i=1}^N r_i^2}
$$

**Example calculation (30-day realized vol):**

BTC daily returns (sample):
- Day 1: +2.3%
- Day 2: -1.8%
- Day 3: +0.5%
- ...
- Day 30: -1.2%

**Sum of squared returns:** 0.0421
**Realized vol:** $\sqrt{365/30 \times 0.0421} = \sqrt{0.513} = 71.6\%$

### 2. Regime Classification

**Four primary regimes:**

**Low Volatility (Grind):**
- Realized vol: 20-40% annually
- Daily moves: <2% typical
- Price action: Range-bound, choppy
- Duration: Weeks to months
- Example: December 2023, BTC $40K-$45K range

**Medium Volatility (Trend):**
- Realized vol: 40-80% annually
- Daily moves: 2-5% typical
- Price action: Directional trends, momentum
- Duration: Weeks to quarters
- Example: Q1 2021, BTC $30K→$60K steady climb

**High Volatility (Volatile):**
- Realized vol: 80-150% annually
- Daily moves: 5-10% typical
- Price action: Whipsaws, sharp reversals
- Duration: Days to weeks
- Example: May 2021, BTC $64K→$30K→$40K

**Extreme Volatility (Crisis):**
- Realized vol: 150%+ annually
- Daily moves: 10-30%+ possible
- Price action: Crashes, liquidation cascades
- Duration: Hours to days
- Example: COVID crash March 2020, BTC -50% in 24 hours

### 3. Regime Indicators

**Primary metrics:**

**1. Realized volatility (30-day):**
- Most direct measure
- Lags regime changes by ~1 week
- Stable, not manipulable

**2. ATR (Average True Range):**

$$
\text{ATR} = \frac{1}{N} \sum_{i=1}^N \max(H_i - L_i, |H_i - C_{i-1}|, |L_i - C_{i-1}|)
$$

**Example:**

30-day ATR: $1,200
Current price: $43,000
**ATR %:** $1,200 / $43,000 = 2.79\%$

**Interpretation:**
- <2%: Low volatility
- 2-4%: Medium volatility
- 4-6%: High volatility
- >6%: Extreme volatility

**3. Bollinger Band Width:**

$$
\text{BB Width} = \frac{\text{Upper Band} - \text{Lower Band}}{\text{Middle Band}}
$$

**Example:**

- Upper (43,000 + 2σ): $46,500
- Lower (43,000 - 2σ): $39,500
- Middle: $43,000

**Width:** $(46,500 - 39,500) / 43,000 = 16.3\%$

**Interpretation:**
- <10%: Low volatility (squeeze)
- 10-20%: Medium volatility
- 20-30%: High volatility
- >30%: Extreme volatility

**4. VIX-style index (if available):**

DVOL (Deribit BTC volatility index):
- Implied volatility from options
- Forward-looking (predictive)
- Typically 10-20% above realized

### 4. Regime Persistence

**Statistical properties:**

**Low-vol regime:**
- Mean duration: 45 days
- Median: 30 days
- Longest observed: 120+ days (2019)

**Medium-vol regime:**
- Mean duration: 60 days
- Median: 45 days
- Typical of bull markets

**High-vol regime:**
- Mean duration: 15 days
- Median: 10 days
- Usually precedes regime change

**Extreme-vol regime:**
- Mean duration: 3 days
- Median: 1-2 days
- Black swan events, brief but violent

**Autocorrelation:**

Volatility is autocorrelated (today's vol predicts tomorrow's):
- 1-day lag correlation: 0.65
- 7-day lag correlation: 0.45
- 30-day lag correlation: 0.25

**Implication:** Regimes persist (not random)

### 5. Transition Patterns

**Common transitions:**

**Low → Medium:**
- Catalyst: Breakout from range
- Speed: Gradual (1-2 weeks)
- Warning signs: Rising volume, tight BB squeeze
- Frequency: Most common transition

**Medium → High:**
- Catalyst: Parabolic price acceleration
- Speed: Fast (days)
- Warning signs: Extreme funding rates, peak OI
- Frequency: Regular in bull markets

**High → Extreme:**
- Catalyst: Crash/liquidation cascade
- Speed: Instantaneous (hours)
- Warning signs: None (black swan)
- Frequency: Rare (2-3× per year)

**Extreme → Medium:**
- Catalyst: Stabilization after crisis
- Speed: Fast (1-3 days)
- Behavior: V-shape recovery typical

**Medium → Low:**
- Catalyst: Trend exhaustion, consolidation
- Speed: Gradual (weeks)
- Behavior: Declining volume, narrowing range

### 6. Implied vs Realized Vol

**Relationship:**

Implied vol (from options) typically leads realized vol by 5-10 days

**Normal relationship:**

$$
\text{IV} \approx 1.1 \times \text{RV} + 5\%
$$

**Example:**

Realized vol: 60%
Expected implied: 1.1 × 60% + 5% = **71%**

**Regime signals:**

**IV >> RV:** Fear, uncertainty
- Interpretation: Market expects vol to rise
- Action: Reduce leverage, defensive

**IV ≈ RV:** Normal market
- Interpretation: Expectations match reality
- Action: Standard strategies

**IV < RV:** Complacency
- Interpretation: Market underpricing risk
- Action: Cautious (potential surprise ahead)

### 7. Historical Regime Distribution

**BTC 2017-2024 statistics:**

**Time in each regime:**
- Low-vol: 35% of days
- Medium-vol: 45% of days
- High-vol: 15% of days
- Extreme-vol: 5% of days

**Returns by regime:**

**Low-vol periods:**
- Median return: +0.5% monthly (boring!)
- Best: +8% monthly (breakout setup)
- Worst: -3% monthly (failed breakout)

**Medium-vol periods:**
- Median return: +12% monthly (trends!)
- Best: +40% monthly (Q1 2021)
- Worst: -25% monthly (reversal)

**High-vol periods:**
- Median return: -5% monthly (dangerous)
- Best: +30% monthly (V-recovery)
- Worst: -50% monthly (May 2021)

**Extreme-vol periods:**
- Median return: -15% monthly (survivability)
- Best: +20% monthly (March 2020 bottom)
- Worst: -70% monthly (crashes)

---

## Key Terminology

**Realized Volatility:**
- Historical price variation
- Calculated from returns
- Backward-looking
- Typically 30 or 90 days

**Implied Volatility:**
- Market's expectation
- From option prices
- Forward-looking
- Leads realized vol

**Volatility Regime:**
- Persistent vol environment
- Low/Medium/High/Extreme
- Lasts days to months
- Requires different strategies

**ATR (Average True Range):**
- Daily range measure
- Accounts for gaps
- Normalized to price
- Regime indicator

**Bollinger Band Width:**
- Volatility expansion/contraction
- Squeeze = Low vol
- Wide bands = High vol
- Mean-reverting

**Vol Clustering:**
- High vol begets high vol
- Low vol begets low vol
- Autocorrelation property
- GARCH modeling

**Volatility Smile:**
- IV varies by strike
- Skew in crypto (put premium)
- Regime-dependent shape
- Risk reversal measure

---

## Trading by Regime

### 1. Low-Vol Regime Strategies

**Characteristics:**
- 20-40% annual volatility
- Range-bound price action
- Declining open interest
- Low funding rates (0.01-0.02%)

**Optimal strategies:**

**Range trading:**
- Buy support, sell resistance
- Target 2-3% range
- Stop if breaks out

**Example:**

BTC ranging $42K-$44K for 30 days:
- Buy: $42,200 (near support)
- Sell: $43,800 (near resistance)
- Stop: Below $41,800 (range break)
- **Profit per cycle: 3.8%**

**Repeat:** 5 cycles in 30 days = 19% monthly return

**Volatility selling:**
- Short straddles/strangles
- Collect premium from low IV
- Exit if vol expands

**Mean reversion:**
- Fade extremes within range
- 2σ Bollinger Band touches
- Quick scalps (hours to days)

**Position sizing:**
- Can use 5-10× leverage (low risk)
- Tight stops (1-2% from entry)
- Max 50% of capital

### 2. Medium-Vol Regime Strategies

**Characteristics:**
- 40-80% annual volatility
- Trending price action
- Rising open interest
- Moderate funding (0.02-0.05%)

**Optimal strategies:**

**Trend following:**
- Moving average crossovers
- Breakout continuation
- Ride trends for weeks

**Example:**

BTC uptrend, 50-day MA crossing 200-day:
- Entry: $44,000 (crossover confirmed)
- Trend target: $52,000 (+18%)
- Stop: Below 50-day MA (2% trailing)

**Hold:** 6 weeks, exit at $51,500

**Momentum trading:**
- Buy strength, short weakness
- Use RSI/MACD confirmation
- Hold 3-7 days

**Volatility buying:**
- Long straddles pre-event
- Expect vol expansion
- Benefit from trend acceleration

**Position sizing:**
- Moderate leverage (3-5×)
- Wider stops (5-8% from entry)
- Max 40% of capital

### 3. High-Vol Regime Strategies

**Characteristics:**
- 80-150% annual volatility
- Whipsaw price action
- Elevated open interest (liquidation risk)
- High funding (>0.05%, unstable)

**Optimal strategies:**

**Scalping:**
- Ultra-short duration (minutes to hours)
- Profit from 1-3% moves
- Exit immediately if wrong

**Example:**

BTC volatile, 5% intraday swings:
- Entry: $43,000 on dip
- Target: $43,800 (1.9%)
- Stop: $42,600 (0.9%)
- **Hold time: 45 minutes**

**Volatility trading:**
- Long gamma (long options)
- Profit from swings
- Manage theta decay carefully

**Contrarian positioning:**
- Fade extremes (RSI >80 or <20)
- Mean reversion on steroids
- Very tight stops

**Position sizing:**
- Low leverage (1-2× max)
- Very wide stops (10-15%) or tight stops (2-3%)
- Max 20% of capital

### 4. Extreme-Vol Regime Strategies

**Characteristics:**
- 150%+ annual volatility
- Crashes/liquidation cascades
- Collapsing open interest
- Funding can flip violently

**Optimal strategies:**

**Capital preservation:**
- Reduce to 0-5% exposure
- Cash is a position
- Survive to trade another day

**Example:**

March 2020 crash:
- BTC $8,000 → $3,800 (52% in 24 hours)
- Volatility: 300%+ annualized
- **Action: Flat or minimal exposure**

**Opportunistic buying (advanced only):**
- Small positions at extreme lows
- 1-2× max leverage
- Expect violent reversal

**Crisis alpha:**
- Long volatility (VIX-style products)
- Short liquidation-prone altcoins
- Basis trades (funding often extreme)

**Position sizing:**
- No leverage
- Max 10% of capital total
- Accept potential total loss of position

### 5. Regime Transition Trading

**Strategy:**

Anticipate and trade regime changes

**Low → Medium transition:**

**Signal:** Bollinger squeeze + volume spike + breakout

**Trade:**
- Enter: On breakout confirmation
- Direction: Momentum direction
- **Expected: Trend develops, vol rises to medium**

**Example:**

BTC squeezing in $42-44K for 45 days:
- Bollinger width: 8% (very tight)
- Breakout: $44,500 on volume
- **Entry long:** $44,500
- Result: Trend to $52,000 over 6 weeks

**Medium → High transition:**

**Signal:** Parabolic acceleration + extreme funding + OI peak

**Trade:**
- Reduce: Cut longs by 50-75%
- Hedge: Buy puts or short futures
- **Expected: Volatility spike incoming**

**Example:**

May 2021, BTC $58K → $64K in 10 days:
- Funding: 0.15% (extreme)
- OI: All-time high
- **Action: Reduce from 40% to 10% exposure**
- Result: Crash to $30K (avoided 53% loss)

### 6. Dynamic Position Sizing

**Leverage adjustment by regime:**

$$
\text{Leverage} = \begin{cases}
10\times & \text{Low-vol (20-40\%)} \\
5\times & \text{Medium-vol (40-80\%)} \\
2\times & \text{High-vol (80-150\%)} \\
1\times & \text{Extreme-vol (>150\%)}
\end{cases}
$$

**Position size formula:**

$$
\text{Position Size} = \frac{\text{Capital} \times \text{Risk \%}}{\text{Volatility Factor}}
$$

Where volatility factor = Realized vol / 40% (normalized)

**Example:**

$1M capital, 2% risk per trade

**Low-vol (30% realized):**
- Vol factor: 30% / 40% = 0.75
- Position: $1M × 2% / 0.75 = $26,667
- With 10× leverage: $266,667 notional

**Extreme-vol (180% realized):**
- Vol factor: 180% / 40% = 4.5
- Position: $1M × 2% / 4.5 = $4,444
- No leverage: $4,444 notional

**Result:** 60× smaller position in extreme-vol vs low-vol!

### 7. Multi-Timeframe Analysis

**Regime on different horizons:**

**Intraday (1-hour):**
- Can be high-vol while daily is medium
- Use for entry timing only

**Daily (30-day realized):**
- Primary regime classification
- Drive strategy selection

**Weekly (90-day realized):**
- Structural regime
- Context for daily regime

**Example:**

**Daily regime:** Medium-vol (55%)
**Weekly regime:** Low-vol (35%)
**Interpretation:** Recent volatility pickup, but structurally calm
**Strategy:** Medium-vol tactics, but cautious (could revert to low-vol)

---

## Common Mistakes

### 1. Ignoring Regime Changes

**Using same strategy across regimes:**

- **Mistake:** Range trading in high-vol regime
- **Why it fails:** Stops hit constantly on whipsaws
- **Fix:** Adapt strategy to regime
- **Real cost:** 20-30% drawdown

**Example:**

May 2021, volatility 120% (high regime):
- Trader: Range trading $55K-$60K
- Reality: BTC $64K → $30K in days
- All range positions stopped out
- **Loss: 30%** (should have been flat)

### 2. Overleveraging in High-Vol

**Using 10-20× leverage when vol elevated:**

- **Mistake:** 20× leverage, vol 100%
- **Why it fails:** 5% adverse move = liquidation
- **Fix:** Reduce leverage as vol rises
- **Real cost:** Total liquidation

**Formula for max leverage:**

$$
\text{Max Leverage} = \frac{40\%}{\text{Realized Vol}}
$$

**Example:**

Vol 100%:
- Max leverage: 40% / 100% = **0.4× (no leverage!)**
- Using 20×: Liquidated on 0.5% move
- **Loss: 100%**

### 3. Fighting the Regime

**Expecting vol to normalize immediately:**

- **Mistake:** Vol spikes to 150%, assume temporary, stay leveraged
- **Why it fails:** Extreme-vol persists for days
- **Fix:** React immediately, reduce exposure
- **Real cost:** Caught in liquidation cascade

**Example:**

COVID crash March 2020:
- Day 1: Vol 100% (halve leverage)
- Day 2: Vol 200% (quarter leverage again)
- Day 3: Vol 300% (flat)

**If stayed leveraged:**
- BTC -50% × 10× leverage = **-500% (total loss + margin call)**

### 4. Regime Misclassification

**Using wrong lookback period:**

- **Mistake:** Calculate vol over 7 days (too short, noisy)
- **Why it fails:** Misidentify regime
- **Fix:** Use 21-30 day minimum
- **Real cost:** Wrong strategy, losses

**Example:**

BTC drops 15% in 2 days (news event):
- 7-day vol: 120% (extreme!)
- 30-day vol: 55% (medium)
- True regime: Medium (temporary spike)

**Wrong action:** Reduce to 5% exposure (extreme-vol protocol)
**Correct action:** Maintain 30% exposure (medium-vol)
**Cost:** Missed recovery rally +20%

### 5. Confusing Vol Levels Across Assets

**Comparing BTC vol to altcoin vol:**

- **Mistake:** "BTC vol is 60%, so ETH 80% is high"
- **Why it fails:** ETH structurally more volatile
- **Fix:** Compare to asset's own historical range
- **Real cost:** Underestimate altcoin risk

**Typical vol by asset:**

- BTC: 40-80% normal
- ETH: 60-100% normal
- Mid-cap alts: 100-150% normal
- Micro-cap: 200%+ normal

**Example:**

SOL vol: 120%
- Absolute: Sounds extreme
- Relative: Normal for SOL (avg 110%)
- **Action: Medium-vol strategies (not extreme-vol)**

### 6. Ignoring Implied Vol

**Only looking at realized:**

- **Mistake:** RV = 50%, IV = 90%, ignore IV
- **Why it fails:** Market expects vol explosion
- **Fix:** Monitor IV/RV ratio
- **Real cost:** Caught in vol spike

**Example:**

Pre-crash:
- Realized vol: 45% (medium)
- Implied vol: 95% (high)
- IV/RV ratio: 2.1 (extreme warning!)

**Correct action:** Reduce leverage despite "normal" realized vol
**If ignored:** Caught in crash, vol spikes to 150%

### 7. Overtrading in Low-Vol

**High turnover in boring markets:**

- **Mistake:** Force trades during 25% vol regime
- **Why it fails:** Fees exceed profit potential
- **Fix:** Accept cash, wait for better regime
- **Real cost:** Death by a thousand cuts

**Example:**

Low-vol regime, 100 trades per month:
- Avg profit per trade: 0.5%
- Fees: 0.1% × 2 (entry + exit) = 0.2%
- **Net per trade: 0.3%**
- Total: 30% gross - 20% fees = **10% net**

**If patient (10 high-conviction trades):**
- Avg profit: 2%
- Fees: 0.2%
- **Net: 1.8% × 10 = 18%** (80% better!)

---

## Risk Management Rules

### 1. Regime Identification

**Daily protocol:**

Calculate 30-day realized volatility:

$$
\sigma_{30} = \sqrt{\frac{365}{30} \sum_{i=1}^{30} r_i^2}
$$

**Classify regime:**
- <40%: Low
- 40-80%: Medium
- 80-150%: High
- >150%: Extreme

**Adjust immediately** (don't wait)

### 2. Leverage Constraints

**Maximum leverage by regime:**

$$
L_{\max} = \min\left(\frac{40\%}{\sigma_{\text{realized}}}, 10\right)
$$

**Example calculations:**

| Realized Vol | Max Leverage | Rationale |
|--------------|-------------|-----------|
| 25% | 10× (cap applied) | Low-vol, safe |
| 50% | 0.8× ≈ 1× | Medium-vol |
| 100% | 0.4× (no leverage) | High-vol |
| 200% | 0.2× (reduce exposure) | Extreme-vol |

### 3. Stop-Loss Scaling

**Stop distance by regime:**

$$
\text{Stop Distance} = \max(2\%, \sigma_{\text{daily}} \times 2)
$$

Where $\sigma_{\text{daily}} = \sigma_{\text{annual}} / \sqrt{365}$

**Example:**

**Low-vol (30% annual):**
- Daily vol: 30% / √365 = 1.57%
- Stop: max(2%, 3.14%) = **3.14%**

**High-vol (120% annual):**
- Daily vol: 120% / √365 = 6.28%
- Stop: max(2%, 12.56%) = **12.56%**

**Implication:** Stops 4× wider in high-vol vs low-vol

### 4. Position Sizing Formula

**Kelly Criterion adaptation:**

$$
f^* = \frac{p \times (b+1) - 1}{b} \times \frac{40\%}{\sigma_{\text{realized}}}
$$

Where:
- $p$ = Win probability
- $b$ = Win/loss ratio
- Vol factor = Scales for regime

**Example:**

Win rate 60%, Win/loss 2:1

**Low-vol (30%):**
- Kelly: (0.6 × 3 - 1) / 2 = 0.4 (40%)
- Vol-adjusted: 0.4 × 40% / 30% = **53%** (use 25-30% in practice)

**Extreme-vol (180%):**
- Kelly: 0.4 (same)
- Vol-adjusted: 0.4 × 40% / 180% = **8.9%** (use 5% in practice)

### 5. Portfolio Heat Limits

**Maximum risk exposure:**

$$
\text{Portfolio Heat} = \sum_{i=1}^N (\text{Position}_i \times \text{Stop Distance}_i)
$$

**Limits by regime:**
- Low-vol: Max 10% portfolio heat
- Medium-vol: Max 6% portfolio heat
- High-vol: Max 3% portfolio heat
- Extreme-vol: Max 1% portfolio heat

**Example:**

$1M portfolio, medium-vol regime (6% max heat)

**Position 1:** $200K, stop 8% away
- Heat: $200K × 8% = $16K (1.6%)

**Position 2:** $150K, stop 10% away
- Heat: $150K × 10% = $15K (1.5%)

**Position 3:** $100K, stop 12% away
- Heat: $100K × 12% = $12K (1.2%)

**Total heat:** $43K (4.3%)

**Remaining budget:** 6% - 4.3% = 1.7% ($17K max for new positions)

### 6. Correlation Adjustment

**In high-vol regimes, correlations → 1:**

During stress:
- BTC/ETH correlation: 0.95+ (vs 0.80 normal)
- BTC/Alts correlation: 0.90+ (vs 0.60 normal)

**Implication:** Diversification fails

**Adjustment:**

$$
\text{Effective Positions} = \frac{\text{Nominal Positions}}{1 + (\rho - 0.5) \times 2}
$$

**Example:**

3 positions (BTC, ETH, SOL), high-vol regime (ρ = 0.95)
- Effective: 3 / (1 + 0.45 × 2) = 3 / 1.9 = **1.58 positions**

**Action:** Reduce by 47% (from 3 to 1.58 effective)

### 7. Regime Change Alerts

**Set alerts for:**

$$
\text{Alert if } \sigma_{7\text{day}} > 1.5 \times \sigma_{30\text{day}}
$$

**Example:**

30-day vol: 50%
- Alert threshold: 75%
- If 7-day vol >75%: Regime change incoming

**Action protocol:**
1. Recalculate 30-day vol
2. Reclassify regime
3. Adjust leverage immediately (same day)
4. Close positions exceeding new limits

---

## Real-World Examples

### 1. Low-Vol Grind (December 2023)

**Regime characteristics:**

December 1-31, 2023:
- BTC range: $40,000 - $45,000
- Realized vol: 32% (low regime)
- ATR: 1.8%
- Funding: 0.015% (17% annual, low)

**Optimal strategies:**

**Range trading:**
- Buy: $40,500
- Sell: $44,500
- Repeated: 4× in month
- **Profit: 4 × 9.9% = 39.6%** (monthly!)

**Volatility selling:**
- Short 30-day ATM straddle
- Collected: $2,500 premium (6.25% yield)
- Vol stayed low, expired worthless
- **Profit: 6.25%** (effectively risk-free)

**Lesson:** Low-vol = boring but profitable for range traders

### 2. Medium-Vol Bull Trend (Q1 2021)

**Regime characteristics:**

January-March 2021:
- BTC: $30,000 → $60,000 (+100%)
- Realized vol: 55-70% (medium regime)
- Steady uptrend, healthy pullbacks
- Rising OI, moderate funding (0.03-0.05%)

**Optimal strategies:**

**Trend following:**
- Entry: $32,000 (breakout above $30K)
- Exit: $58,000 (overbought RSI + extreme funding)
- **Profit: 81%** over 10 weeks

**Momentum:**
- Multiple swing trades, 5-15% each
- Win rate: 70%
- **Total: 45%** over quarter

**Lesson:** Medium-vol = optimal for directional strategies

### 3. High-Vol Euphoria (Late April 2021)

**Regime characteristics:**

April 20-30, 2021:
- BTC: $54,000 → $64,000 (parabolic)
- Realized vol: 95% (high regime)
- Funding: 0.10-0.15% (109-164% annual, extreme)
- OI: All-time high (danger signal)

**Correct action:**

**Risk-off:**
- Reduce from 40% exposure to 10%
- Take profits on longs
- Buy put protection

**Example portfolio:**

- Closed: $400K long positions (took profits)
- Kept: $100K core position
- Bought: $50K ATM puts (insurance)

**May 19 crash:**
- BTC $64K → $30K (-53%)
- **Core position loss: $53K** (53% on $100K)
- **Put profit: $45K** (90% on $50K)
- **Net loss: $8K** (0.8% of $1M portfolio)

**If stayed fully invested:**
- Loss: $400K × 53% = **$212K** (21.2% portfolio loss!)

**Lesson:** High-vol + extreme signals = reduce aggressively

### 4. Extreme-Vol Crash (May 19, 2021)

**Event:** $64K → $30K in 24 hours

**Realized vol:** 280% (extreme regime)

**Liquidations:**
- Total: $9B+ in 24 hours
- OI collapse: 50%+ in hours

**Survival strategies:**

**Flat portfolio:**
- Action: 100% cash before crash
- Result: 0% loss
- **Opportunity: Bought $32K dip (+25% rebound)**

**Opportunistic (advanced):**
- Bought: $35K with 5% of portfolio ($50K)
- Stop: $32K (tight)
- Result: Rebound to $40K
- **Profit: $7,150** (14.3% on $50K)

**Lesson:** Extreme-vol = survival first, opportunism second

### 5. COVID Crash (March 12-13, 2020)

**Event:** BTC $8,000 → $3,800 → $6,500 in 48 hours

**Characteristics:**

- Realized vol: 350%+ (extreme)
- 50% drop in single day
- Liquidation cascade (cross-asset, not just crypto)
- Funding: -0.20% (shorts dominating)

**Regime response:**

**Day 1 (crash):**
- Action: Flat (0% exposure)
- Missed: Bottom ($3,800)

**Day 2 (stabilization):**
- Vol declining: 180%
- Action: Small long $4,200 (2% of portfolio)

**Week 1 (recovery):**
- BTC → $6,500
- Profit: $4,600 on $20K = **23%**

**Month 1:**
- BTC → $9,000
- Cumulative: **114%** (from $4,200)

**Lesson:** Extreme-vol → medium-vol transition = opportunity

### 6. 2022 Bear Grind (March-November)

**Regime characteristics:**

- BTC: $48,000 → $15,500 (slow bleed)
- Realized vol: 45-65% (medium regime throughout)
- No extreme spikes (just steady decline)
- Funding: 0.01-0.02% (low, bearish)

**Strategies:**

**Short perpetuals:**
- Multiple short positions in downtrend
- Avg holding: 2-3 weeks each
- **Returns: 5-12% per trade**

**Basis trades:**
- Long spot, short perpetual (collected funding despite bear)
- Annual yield: 15-25%
- **Total: 18%** despite BTC -68%!

**Lesson:** Medium-vol bear markets still tradeable (just short instead of long)

### 7. Post-FTX Recovery (December 2022-January 2023)

**Transition:** Extreme → High → Medium

**Timeline:**

**Nov 8-15:** FTX collapse
- Vol: 250% (extreme)
- BTC: $21K → $16K
- Action: Flat

**Nov 16-30:** Stabilization
- Vol: 120% (high)
- BTC: $16K-$17K range
- Action: 5% long at $16.5K

**Dec 1-31:** Recovery
- Vol: 75% (medium)
- BTC: $16.5K → $18K
- Action: Increase to 20% exposure

**Jan 1-31:** New trend
- Vol: 60% (medium)
- BTC: $18K → $23K
- **Profit: 39%** (from $16.5K entry)

**Lesson:** Patience through regime transitions pays off

---

## Practical Steps

### 1. Daily Regime Check

**Morning routine (10 minutes):**

**Calculate 30-day realized vol:**

```python
returns = np.log(prices[1:] / prices[:-1])
vol_30d = np.sqrt(365 / 30 * np.sum(returns**2))
```

**Output:** 67% (example)

**Classify:** Medium-vol regime

**Set rules for day:**
- Max leverage: 5×
- Stop distance: 7-10%
- Max position: 30% of capital

### 2. Measure Current Vol

**Tools:**

- **CoinGecko:** Historical price data
- **TradingView:** Built-in volatility indicators (ATR, Bollinger Width)
- **Glassnode:** Realized volatility charts
- **Deribit:** DVOL index (implied vol)

**Manual calculation:**

Download 30 days of daily close prices → Calculate log returns → Square and sum → Multiply by 365/30 → Square root

### 3. Compare to Historical Range

**Percentile analysis:**

Where is current vol in historical distribution?

**Example:**

BTC 5-year vol data:
- 10th percentile: 30%
- 25th percentile: 45%
- 50th percentile: 65%
- 75th percentile: 90%
- 90th percentile: 120%

**Current:** 67%

**Interpretation:** 50th percentile (median), medium regime confirmed

### 4. Adjust Position Sizes

**Recalculate max position:**

$$
\text{Max Position} = \frac{\text{Capital} \times 40\%}{\sigma_{\text{realized}}}
$$

**Example:**

$1M capital, vol 67%
- Max position: $1M × 40% / 67% = **$597K**
- Current exposure: $800K
- **Action: Reduce by $203K**

### 5. Set Alerts

**Volatility spike alert:**

If 7-day vol >1.5 × 30-day vol → Notify

**Example:**

30-day vol: 50%
- Alert threshold: 75%

**Triggers:**
- Immediate: Review regime
- If confirmed: Reduce leverage same day

### 6. Review Open Positions

**Check each position:**

- Is leverage appropriate for regime?
- Is stop distance adequate?
- Is position size too large?

**Example position:**

- Long BTC: $200K notional
- Leverage: 10×
- Stop: 5% away

**If regime changed to high-vol:**
- Leverage: Too high (should be 2×)
- Stop: Too tight (should be 10-12%)
- **Action: Reduce to $40K notional, widen stop to 10%**

### 7. Document Regime

**Trading journal entry:**

```
Date: January 10, 2026
30-day realized vol: 67%
Regime: Medium-vol
ATR %: 3.2%
Bollinger Width: 16%
Funding: 0.03%
OI: Rising (+8% weekly)

Strategy: Trend following
Max leverage: 5×
Position sizing: 30% max per trade
Stop distance: 7-10%

Current positions:
- Long BTC $200K (4× leverage)
- Long ETH $150K (3× leverage)
Total heat: 4.8% (within 6% limit)
```

---

## Final Wisdom

> "Crypto volatility regimes are the single most important concept for risk management—the same 10× leverage that generates 50% returns in low-vol regimes (20-40% annual volatility) will liquidate your entire account in extreme-vol regimes (150%+ volatility) within hours. The statistics are brutal: BTC spent 35% of 2017-2024 in low-vol regimes (boring 2-3% weekly ranges, perfect for range trading with high leverage), 45% in medium-vol regimes (40-80% volatility, optimal for trend following with moderate leverage), 15% in high-vol (80-150%, whipsaw hell where most traders die), and 5% in extreme-vol (COVID crash's 350% realized volatility, May 2021's $64K→$30K in 24 hours, liquidating $9B in positions). The deepest mathematical truth: volatility is NOT constant (Black-Scholes assumption fails catastrophically in crypto), and it clusters—high vol begets high vol (GARCH effects), meaning a 5% daily move predicts more 5% daily moves, not mean reversion to calm. The regime persistence is what kills traders: extreme-vol doesn't last forever (mean 3 days), but you can't survive those 3 days at 20× leverage when 30% daily moves are occurring. The correct framework is dynamic position sizing: leverage = 40% / realized_vol, which means 10× in low-vol (40%/30% = 1.33, capped at 10×), 1× in medium-vol (40%/50% = 0.8×), and 0× in extreme-vol (40%/180% = 0.22×, i.e., flat). Q1 2021 exemplifies perfect medium-vol trend following: BTC $30K→$60K over 10 weeks with 55-70% realized volatility, enabling 5× leveraged positions that 2× returned 162% (81% price move × 2× leverage), but late April transitioned to high-vol (95% realized) with funding 0.15% (164% annual, screaming danger), and May 19 erupted into extreme-vol (280% realized) crashing -53% in 24 hours—those who stayed 10× leveraged lost 530% (impossible, liquidated at -100%). The transition patterns are predictable: low→medium happens on range breakouts (Bollinger squeeze, volume spike), medium→high happens on parabolic price acceleration (late-stage bull runs, extreme funding rates, OI peaks), high→extreme is instantaneous black swans (usually liquidation cascades or external shocks like FTX). Implied volatility leads realized by 5-10 days, so IV/RV ratio >1.5 is early warning system (pre-COVID: RV 45%, IV 95%, ratio 2.1 = extreme warning, correct). The tactical implementation: (1) Calculate 30-day realized vol DAILY (not weekly, regimes change fast), (2) Classify regime honestly (don't wishful-think low-vol when it's 75%), (3) Adjust leverage IMMEDIATELY (same day, not tomorrow), (4) Scale stops proportionally (tight 3% in low-vol, wide 12% in high-vol), (5) Accept cash positions (50%+ cash in extreme-vol is correct, opportunity cost doesn't matter when survival at stake), (6) Don't fight the regime (range trading in high-vol = death, trend following in low-vol = chop-fest). The final truth: crypto volatility regimes are like weather—you can't control them, you can't wish them away, you can only dress appropriately. Wearing shorts in a blizzard (10× leverage in 150% vol) gets you killed; wearing a parka in summer (100% cash in 30% vol) is uncomfortable but survivable. Most traders fail because they REKT in extreme-vol episodes (5% of time) that wipe out gains from the other 95%. Surviving the 5% is the entire game."

**Key to success:**

- Calculate 30-day realized vol DAILY (not weekly, regimes change fast)
- Classify regime honestly (don't wishful-think low-vol when medium/high)
- Adjust leverage IMMEDIATELY when regime changes (same day, not tomorrow)
- Formula: Max leverage = 40% / realized_vol (10× at 30%, 1× at 50%, 0× at 150%+)
- Scale stops proportionally (tight 3% in low-vol, wide 12% in high-vol)
- Accept cash positions (50%+ cash in extreme-vol is correct, survival > opportunity)
- Don't fight regime (range trade low-vol, trend follow medium-vol, survive extreme-vol)
- Monitor IV/RV ratio (>1.5 = early warning, market expects vol explosion)
