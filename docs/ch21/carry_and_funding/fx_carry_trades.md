# FX Carry Trades

**FX carry trades** systematically exploit interest rate differentials across currencies by borrowing low-yielding currencies (JPY at 0-0.5%, CHF at 0-1%, historically) and investing in high-yielding currencies (BRL at 10-13%, TRY at 15-45%, MXN at 10-11%), capturing the carry (interest differential, typically 5-15% annually) while exposed to currency appreciation/depreciation risk, with historical Sharpe ratios of 0.4-0.8 making it attractive despite catastrophic drawdowns during risk-off episodes (2008: -20% in months, 2015 CHF un-peg: -30% overnight), requiring careful risk management through position sizing (volatility targeting at 10-15% annual vol), diversification across currency pairs (8-12 positions), stop-losses during regime changes (VIX >30 = exit), and recognition that carry strategies are effectively short volatility (collect premium in calm periods, crash in panics).

---

## The Core Insight

**The fundamental idea:**

- Interest rate differentials create opportunity
- Borrow low-rate currency (funding currency)
- Invest in high-rate currency (target currency)
- Collect interest differential (carry)
- Risk: Currency moves against you (depreciation)
- Return: Carry + Currency appreciation
- Historical return: 5-10% annually (before crashes)
- Sharpe: 0.4-0.8 (good, but tail risk)
- Nature: Short volatility, short disaster insurance
- Crashes in risk-off environments (predictable pattern)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/fx_carry_trade_mechanics.png?raw=true" alt="fx_carry_trade_mechanics" width="700">
</p>
**Figure 1:** FX carry trade mechanics showing funding currencies (JPY, CHF, USD in low-rate environments), target currencies (BRL, TRY, MXN, ZAR), carry calculation (interest differential minus currency movement), risk-off crash patterns (VIX spikes trigger unwinding), and diversification strategies across currency pairs to reduce correlation in tail events.

**You're essentially asking: "How do I profit from interest rate gaps between countries?"**

---

## Carry Trade Fundamentals

### 1. Basic Mechanics

**The trade:**

**Borrow (short):** Low interest rate currency
**Invest (long):** High interest rate currency
**Profit:** Interest differential

**Formula:**

$$
\text{Carry Return} = (r_{\text{high}} - r_{\text{low}}) + \Delta S
$$

Where:
- $r_{\text{high}}$ = Interest rate of target currency
- $r_{\text{low}}$ = Interest rate of funding currency
- $\Delta S$ = Spot FX appreciation/depreciation

**Example:**

**Short JPY, Long BRL:**

- JPY rate: 0.1% (near zero)
- BRL rate: 12.0%
- **Carry: 11.9% annually**

**Scenario A (stable FX):**
- BRL/JPY: Unchanged
- **Return: +11.9%** (pure carry)

**Scenario B (BRL appreciates 5%):**
- BRL/JPY: +5%
- **Return: +11.9% + 5% = +16.9%**

**Scenario C (BRL depreciates 15%):**
- BRL/JPY: -15%
- **Return: +11.9% - 15% = -3.1%**

### 2. Interest Rate Parity

**Theoretical relationship:**

Covered Interest Parity (CIP):

$$
\frac{F}{S} = \frac{1 + r_{\text{domestic}}}{1 + r_{\text{foreign}}}
$$

Where:
- $F$ = Forward exchange rate
- $S$ = Spot exchange rate
- $r$ = Interest rates

**Implication:**

If CIP holds, forward rate already reflects interest differential (no free lunch)

**Reality:**

CIP often violated (transaction costs, credit risk, capital controls)
→ Carry opportunities exist

**Uncovered Interest Parity (UIP):**

$$
E[\Delta S] = r_{\text{domestic}} - r_{\text{foreign}}
$$

**Expected spot change equals interest differential**

**Empirical reality:**

UIP fails systematically (forward rate poor predictor)
→ High interest currencies don't depreciate as much as predicted
→ Carry trades profitable on average

### 3. Carry as Risk Premium

**Why does carry exist?**

**Theory 1—Crash risk premium:**
- High-rate currencies crash in risk-off
- Carry = Compensation for tail risk
- Investors demand premium

**Theory 2—Liquidity premium:**
- Low-rate currencies (JPY, CHF) are liquid safe havens
- High-rate currencies (EM) are less liquid
- Premium for holding less liquid assets

**Theory 3—Political/economic risk:**
- High rates reflect inflation, instability
- Currency depreciation risk
- Carry compensates

**Evidence:**

Carry works most of time (80% of periods profitable)
But crashes violently (20% of time, -20 to -50%)
→ Negative skewness (picking up pennies in front of steamroller)

### 4. Historical Performance

**1990-2023 average annual returns:**

**G10 Carry (developed):**
- Average: 5-7% annually
- Sharpe: 0.5-0.6
- Max drawdown: -25% (2008)

**EM Carry (emerging markets):**
- Average: 8-12% annually
- Sharpe: 0.4-0.5
- Max drawdown: -35% (1998, 2008)

**Specific pairs:**

**USD/JPY carry (short JPY):**
- 1990-2023: +4.5% annually
- Volatility: 10%
- Sharpe: 0.45

**AUD/JPY carry:**
- 1990-2023: +6.8% annually
- Volatility: 13%
- Sharpe: 0.52

**BRL/USD carry:**
- 2000-2023: +9.5% annually
- Volatility: 18%
- Sharpe: 0.53

### 5. Carry vs Spot Return Decomposition

**Total return:**

$$
\text{Total} = \text{Carry} + \text{Spot Return}
$$

**Historical correlation:**

Carry and spot weakly correlated (-0.1 to +0.2)
→ Independent sources of return

**Example (AUD/JPY 2010-2020):**

**Carry contribution:**
- Avg interest differential: 3.5%
- **Carry: +3.5% annually**

**Spot contribution:**
- AUD/JPY: 75 → 72 (−4% over decade)
- **Spot: -0.4% annually**

**Total: +3.1% annually**

**Interpretation:**
- Carry provided all positive return
- Spot was slight drag
- Still profitable overall

### 6. Leverage and Returns

**Typical leverage:**

- Retail: 10-20× (dangerous!)
- Institutional: 2-5×
- Conservative: 1-2×

**Example (10× leverage):**

**USD/BRL carry:**
- Unleveraged carry: 11%
- Leverage: 10×
- **Leveraged carry: 110%** (before spot moves)

**Risk:**
- 10% adverse BRL move: -100% (wipeout)
- Volatility: 15% annual
- **Margin call likely within year**

**Better approach (2× leverage):**
- Leveraged carry: 22%
- Drawdown tolerance: 50% adverse move
- **Sustainable**

### 7. Correlation Structure

**Within carry basket:**

**Normal times:**
- Correlation: 0.3-0.5 (moderate diversification)

**Crisis times:**
- Correlation: 0.8-0.95 (diversification fails!)

**Example (2008 crisis):**

**Normally uncorrelated pairs:**
- AUD/JPY: -0.35 correlation with BRL/JPY (normal)
- 2008: +0.92 correlation
- **All carry trades crashed together**

**Implication:**
- Diversification works in calm periods
- Fails when needed most (tail events)

---

## Key Terminology

**Carry:**
- Interest rate differential
- Earned over time
- Measured annually (%)
- Independent of spot FX moves

**Funding Currency:**
- Low interest rate currency
- Borrowed (short position)
- Typically: JPY, CHF, USD (when low)

**Target Currency:**
- High interest rate currency
- Invested (long position)
- Typically: BRL, TRY, MXN, ZAR, AUD, NZD

**Covered Interest Parity:**
- Forward rate = Spot × (1 + r_diff)
- Arbitrage relationship
- Should eliminate carry profits
- Often violated in practice

**Uncovered Interest Parity:**
- Expected spot change = Interest differential
- Theoretical equilibrium
- Empirically fails (carry profitable)

**Risk-Off:**
- Market stress, risk aversion
- Carry unwinds (crash)
- Flight to safe havens (JPY, CHF)
- VIX spikes, correlations → 1

**Dollar Smile:**
- USD strong in extremes (very good or very bad economies)
- USD weak in middle (moderate growth)
- Affects carry dynamics

---

## Popular Carry Pairs

### 1. AUD/JPY (Classic)

**Characteristics:**

**Funding (JPY):**
- BoJ rate: 0-0.5% (historically near zero)
- Safe haven, appreciation in crises
- Most liquid funding currency

**Target (AUD):**
- RBA rate: 2-4% (recently), historically 4-6%
- Commodity currency (iron ore, coal)
- Pro-cyclical (appreciates in growth)

**Carry:**
- Historical: 3-5% annually
- Recent: 2-3% (both rates low)

**Volatility:**
- 12-15% annually (moderate)

**Performance:**
- 1990-2023: +6.8% annually
- Sharpe: 0.52
- Max drawdown: -45% (2008)

**When it works:**
- Global growth strong
- Commodities rising
- Risk-on environment

**When it fails:**
- Risk-off (2008, 2020 COVID)
- China slowdown (AUD weakness)
- Commodity crash

### 2. NZD/JPY

**Similar to AUD/JPY:**

**Target (NZD):**
- RBNZ rate: Historically 3-6%
- Commodity (dairy, agriculture)
- Small liquid market

**Carry:**
- Historical: 4-6% annually

**Correlation with AUD/JPY:**
- 0.85+ (very similar trade)
- Little diversification benefit

### 3. USD/BRL

**Characteristics:**

**Funding (USD):**
- When Fed low (2008-2015, 2020-2021): 0-0.25%

**Target (BRL):**
- BCB rate: 10-13% (typical), peaked 14.25% (2022)
- EM risk, political uncertainty
- Inflation-linked

**Carry:**
- 10-13% when USD at zero
- 8-10% recent (USD higher)

**Volatility:**
- 18-22% annually (high!)

**Performance:**
- 2000-2023: +9.5% annually
- Sharpe: 0.53
- Max drawdown: -40% (2015-2016)

**Risks:**
- Political instability (Lula vs Bolsonaro)
- Fiscal concerns
- EM contagion

### 4. USD/MXN

**Characteristics:**

**Target (MXN):**
- Banxico rate: 10-11% (2023-2024)
- US-linked economy (NAFTA/USMCA)
- More stable than BRL

**Carry:**
- 10-11% (when USD at zero)

**Volatility:**
- 12-15% (lower than BRL)

**Advantage:**
- Less volatile than other EM
- Liquid market

### 5. EUR/TRY

**Characteristics:**

**Target (TRY):**
- TCMB rate: 15-45% (varies wildly!)
- Extremely high carry
- Erdogan political risk

**Carry:**
- 15-25% typical (but TRY depreciates!)

**Reality:**
- TRY depreciates faster than carry
- 2018-2024: TRY lost -70% vs EUR
- Carry +100% over period
- **Net: -50%** (carry didn't compensate!)

**Lesson:**
- Ultra-high rates = warning sign
- Reflects currency collapse risk

### 6. CHF/JPY (Low-Carry)

**Both low-rate safe havens:**

**Carry:**
- Near zero (both ~0%)

**Why trade?**
- Diversification in multi-pair basket
- Trend following (not carry)

**Typically avoided** in pure carry strategies

### 7. G10 Carry Basket

**Diversified approach:**

**Funding (short):**
- JPY: -33%
- CHF: -33%
- EUR: -34% (when ECB low)

**Target (long):**
- AUD: +25%
- NZD: +25%
- NOK: +25%
- SEK: +25%

**Carry:**
- Blended: 3-5% annually
- Volatility: 8-10%
- Sharpe: 0.5-0.7

**Advantage:**
- Diversification
- Lower vol than single pairs
- More stable

---

## Risk Factors

### 1. Currency Depreciation

**Primary risk:**

High-rate currency depreciates, offsetting carry

**Example:**

**TRY/USD (2018):**
- Carry: +20% (TRY rates high)
- TRY depreciation: -35%
- **Net: -15%**

**Why it happens:**
- High rates reflect inflation expectation
- Purchasing Power Parity (PPP) adjusts
- Currency weakens over time

### 2. Risk-Off Events

**Sudden unwinding:**

**Trigger events:**
- Financial crisis (2008)
- Pandemic (COVID March 2020)
- Geopolitical shock (Russia-Ukraine)
- Central bank surprises

**Mechanism:**
1. Stress → Risk aversion
2. Investors unwind carry trades (sell high-rate, buy low-rate)
3. Funding currencies appreciate (JPY, CHF surge)
4. Target currencies collapse
5. **Carry positions crash -20 to -50%**

**Example—2008 crisis:**

**AUD/JPY:**
- July 2008: 105
- October 2008: 60
- **Decline: -43% in 3 months**

**EUR/JPY:**
- July 2008: 170
- October 2008: 115
- **Decline: -32%**

**All carry trades crashed simultaneously**

### 3. Interest Rate Convergence

**Carry narrows:**

**Scenario:**
- Fed hikes (funding currency rate rises)
- RBA cuts (target currency rate falls)
- Carry shrinks from 5% to 1%

**Example (2015-2018):**

**AUD/JPY carry:**
- 2015: 5.5% (AUD 2.5%, JPY -0.1%)
- 2018: 1.5% (AUD 1.5%, JPY -0.1%)
- **Carry collapsed -73%**

**Impact:**
- Lower return
- Less attractive vs alternatives
- Capital exits carry trades

### 4. Volatility Spikes

**Carry = Short volatility:**

When volatility surges:
- Funding currencies (safe havens) appreciate sharply
- Target currencies crash
- Correlation → 1 (diversification fails)

**VIX relationship:**

Empirical:
- VIX <15: Carry works (75% win rate)
- VIX 15-25: Mixed (50% win rate)
- VIX >25: Carry fails (30% win rate)
- VIX >40: Carry crashes (-80% win rate)

**Implication:**
- Monitor VIX
- Exit when VIX >30
- Re-enter when VIX <20

### 5. Liquidity Crises

**Forced unwinding:**

**Mechanism:**
- Carry funded with leverage
- Market stress → Margin calls
- Forced selling of target currencies
- Self-reinforcing spiral

**Example—2008:**

Hedge funds:
- 10× leverage on carry
- Market crashes 10%
- Margin calls → Forced unwind
- **Amplified decline to -40%**

### 6. Political/Policy Shocks

**Unexpected changes:**

**Swiss franc un-peg (January 2015):**
- SNB held EUR/CHF at 1.20
- Abandoned peg suddenly
- CHF appreciated 30% in minutes
- **EUR/CHF carry: -30% overnight**
- Many levered traders wiped out

**Brexit (June 2016):**
- GBP/USD: -10% overnight
- Carry trades in GBP: Massive losses

### 7. Correlation Breakdown

**Diversification fails in tails:**

**Normal correlation (calm):**
- AUD/JPY vs BRL/USD: 0.3-0.4
- 10 pairs: Effective diversification

**Crisis correlation:**
- All pairs: 0.85-0.95
- Effective positions: 1-2 (not 10)

**Impact:**
- Portfolio crashes despite "diversification"
- Expected -10% becomes -25%

---

## Carry Trade Strategies

### 1. Simple Pair Strategy

**Single pair carry:**

**Example:**

Short JPY, Long AUD (AUD/JPY)

**Position:**
- $1M notional
- Leverage: 1× (no leverage)
- Carry: 3.5% annually

**Expected return:**
- Carry: +$35K annually
- Spot (assume flat): $0
- **Total: +$35K** (3.5%)

**Risk:**
- AUD depreciates 10%: -$100K
- Net: -$65K (-6.5%)

**Probability:**
- Historical: 70% years profitable
- 30% years: -5 to -20%

### 2. Diversified G10 Basket

**Multiple pairs:**

**Portfolio (equal weight):**
1. AUD/JPY: 20%
2. NZD/JPY: 20%
3. GBP/JPY: 20%
4. CAD/JPY: 20%
5. NOK/SEK: 20%

**Carry:**
- Blended: 4.2% annually

**Volatility:**
- Single pair: 12%
- Diversified: 8% (diversification benefit)

**Sharpe:**
- 4.2% / 8% = 0.53

**Advantage:**
- Smoother returns
- Lower max drawdown

### 3. EM High-Carry Strategy

**Focus on emerging markets:**

**Portfolio:**
1. USD/BRL: 25%
2. USD/MXN: 25%
3. USD/ZAR: 25%
4. USD/RUB: 25%

**Carry:**
- Blended: 10-12% annually

**Volatility:**
- 15-18%

**Sharpe:**
- 0.6-0.7 (better than G10, but higher risk)

**Risk:**
- EM contagion (all crash together in crisis)
- Political risk
- Higher individual volatility

### 4. Risk-Adjusted Carry

**Vol targeting:**

**Method:**
- Target: 10% annual volatility
- Adjust leverage based on realized vol

**Formula:**

$$
\text{Leverage} = \frac{\text{Target Vol}}{\text{Realized Vol}}
$$

**Example:**

**AUD/JPY:**
- Target vol: 10%
- Realized vol (recent): 15%
- Leverage: 10% / 15% = 0.67×
- **Position: 67% of capital** (de-lever in high vol)

**When vol drops to 8%:**
- Leverage: 10% / 8% = 1.25×
- **Position: 125%** (lever up in low vol)

**Benefit:**
- Consistent risk exposure
- Higher Sharpe ratio
- Smoother returns

### 5. Momentum-Enhanced Carry

**Combine carry + trend:**

**Rules:**
1. Rank pairs by carry (high to low)
2. Filter: Only long if 3-month trend positive
3. Portfolio: Top 5 pairs meeting both criteria

**Example:**

**January 2023:**

**Rank by carry:**
1. USD/TRY: 20% (but TRY downtrend -12%)
2. USD/BRL: 12% (BRL uptrend +5%)
3. AUD/JPY: 3% (AUD uptrend +3%)

**Selected:**
- USD/BRL: ✓ (carry + momentum)
- AUD/JPY: ✓ (carry + momentum)
- USD/TRY: ✗ (negative momentum)

**Result:**
- Avoided TRY collapse
- Captured BRL/AUD gains

**Historical improvement:**
- Pure carry: Sharpe 0.5
- Carry + momentum: Sharpe 0.7-0.8

### 6. Conditional Carry (VIX Filter)

**Risk-on/off regime:**

**Rules:**
- VIX <20: Full carry positions
- VIX 20-30: 50% carry positions
- VIX >30: 0% carry (cash)

**Example:**

**2020:**
- Jan-Feb: VIX 15 → 100% carry
- March: VIX 85 → 0% carry (avoided -30% crash)
- May: VIX 30 → 50% carry
- June-Dec: VIX 20-25 → 50-100% carry

**Result:**
- Avoided worst of COVID crash
- Participated in recovery
- **Annual: +8%** (vs -15% for unconditional carry)

### 7. Barbell Strategy

**Split between safe and risky:**

**Portfolio:**
- 50%: Low-carry, low-vol (CHF/EUR, JPY/EUR)
- 50%: High-carry, high-vol (BRL, TRY, ZAR)

**Rationale:**
- Safe side: Preserves capital in crisis
- Risky side: Generates high carry in calm periods

**Example:**

**Calm period:**
- Safe: +1% (low carry)
- Risky: +15% (high carry)
- **Blended: +8%**

**Crisis:**
- Safe: +5% (safe haven appreciation)
- Risky: -25%
- **Blended: -10%** (better than -25% all-risky)

---

## Common Mistakes

### 1. Overleveraging

**Using excessive leverage:**

- **Mistake:** 20× leverage on carry (chase high returns)
- **Why it fails:** 5% adverse move = total loss
- **Fix:** Max 2-3× leverage, preferably 1×
- **Real cost:** Wipeout in single crisis

**Example:**

**$100K account, 20× leverage:**
- Position: $2M AUD/JPY
- Carry: 3.5% × 20 = 70% annually
- **Risk:** AUD -5% = -100% (margin call)

**2008 crisis:**
- AUD/JPY: -43%
- **Wiped out at -5%**, missed -38% more

### 2. Ignoring Risk-Off Signals

**Holding through VIX spikes:**

- **Mistake:** VIX hits 40, stay in carry
- **Why it fails:** Historical -80% loss rate when VIX >40
- **Fix:** Exit when VIX >30, re-enter <20
- **Real cost:** -20 to -40% drawdown

**Example:**

**March 2020 COVID:**
- VIX: 15 → 85 in 2 weeks
- Carry trades: -30% average
- **Exit at VIX 30:** -8% loss
- **Stayed in:** -30% loss
- **Cost of ignoring: -22%**

### 3. Chasing Ultra-High Carry

**TRY, ARG, other extreme carries:**

- **Mistake:** 40% carry on TRY, must be good!
- **Why it fails:** High rate = currency collapse signal
- **Fix:** Cap carry at 15%, avoid >20%
- **Real cost:** -30 to -70% despite high carry

**Example:**

**TRY 2018-2023:**
- Cumulative carry: +150% (massive!)
- TRY depreciation: -75%
- **Net: -37.5%** (carry didn't compensate)

### 4. No Diversification

**Single pair concentration:**

- **Mistake:** 100% in AUD/JPY
- **Why it fails:** Single pair can crash -40%
- **Fix:** 8-12 pairs, max 15% each
- **Real cost:** Unrewarded concentration risk

**Example:**

**2008, AUD/JPY only:**
- Drawdown: -43%

**Diversified G10 basket:**
- Drawdown: -25% (better by 18%)

### 5. Forgetting Correlation in Tails

**Assuming diversification always works:**

- **Mistake:** "10 pairs, I'm diversified"
- **Why it fails:** Crisis correlation → 0.95
- **Fix:** Recognize diversification fails in tails, use VIX filter
- **Real cost:** -25% when expecting -10%

**Example:**

**2008, 10-pair basket:**
- Expected (0.3 correlation): -12% max
- Actual (0.92 correlation): -28%
- **Cost: -16% surprise**

### 6. Not Adjusting for Vol Regime

**Same leverage in all volatility:**

- **Mistake:** Constant 100% exposure
- **Why it fails:** High-vol periods more dangerous
- **Fix:** Vol targeting (lower leverage in high vol)
- **Real cost:** 30-50% higher drawdowns

**Example:**

**Constant exposure:**
- Low vol (8%): Fine (Sharpe 0.6)
- High vol (18%): Painful (Sharpe 0.2, drawdown -35%)

**Vol-targeted:**
- Low vol: 1.25× leverage (Sharpe 0.7)
- High vol: 0.55× leverage (Sharpe 0.5, drawdown -18%)
- **Better Sharpe, lower drawdown**

### 7. Ignoring Funding Currency Dynamics

**Only looking at target currency:**

- **Mistake:** Focus on BRL, ignore JPY dynamics
- **Why it fails:** JPY can surge +15% in crisis (BoJ intervention)
- **Fix:** Monitor both sides of pair
- **Real cost:** Unexpected losses from funding side

**Example:**

**2011 Japan earthquake:**
- JPY surged +12% in days (repatriation)
- AUD/JPY carry: -12% from JPY side alone
- **Surprised traders who only watched AUD**

---

## Risk Management Rules

### 1. Maximum Leverage

**Conservative limit:**

$$
\text{Max Leverage} = \frac{15\%}{\text{Historical Vol}}
$$

**Example:**

**AUD/JPY (vol 12%):**
- Max leverage: 15% / 12% = 1.25×

**BRL/USD (vol 18%):**
- Max leverage: 15% / 18% = 0.83× (no leverage!)

### 2. VIX-Based Exposure

**Dynamic allocation:**

$$
\text{Exposure} = \begin{cases}
100\% & \text{if VIX} < 15 \\
75\% & \text{if } 15 \leq \text{VIX} < 20 \\
50\% & \text{if } 20 \leq \text{VIX} < 25 \\
25\% & \text{if } 25 \leq \text{VIX} < 30 \\
0\% & \text{if VIX} \geq 30
\end{cases}
$$

**Example:**

$1M portfolio:
- VIX 12: $1M in carry
- VIX 22: $500K in carry, $500K cash
- VIX 35: $0 in carry, $1M cash

### 3. Position Limits per Pair

**Diversification rule:**

$$
\text{Max per Pair} = \frac{100\%}{\max(8, N)}
$$

Where $N$ = number of pairs

**Example:**

10 pairs:
- Max per pair: 100% / 10 = 10%

5 pairs:
- Max per pair: 100% / 8 = 12.5% (use 8 as minimum)

### 4. Carry Threshold

**Minimum carry to enter:**

$$
\text{Min Carry} \geq 2\% + \text{Expected Depreciation}
$$

**Example:**

BRL expected depreciation: 4% annually (PPP)
- Min carry: 2% + 4% = 6%
- Actual carry: 10%
- **Acceptable** (6% margin)

TRY expected depreciation: 20% annually
- Min carry: 2% + 20% = 22%
- Actual carry: 25%
- **Marginal** (only 3% margin, risky)

### 5. Stop-Loss Rules

**Pair-level stops:**

$$
\text{Stop} = -15\% \text{ (individual pair)}
$$

**Portfolio-level stop:**

$$
\text{Portfolio Stop} = -10\% \text{ (entire carry book)}
$$

**Example:**

AUD/JPY position:
- Entry: 85
- Stop: 72.25 (−15%)
- **Exit if triggered**

**Portfolio:**
- Start: $1M
- Drawdown to: $900K (−10%)
- **Close all positions, reassess**

### 6. Rebalancing Frequency

**Monthly rebalancing:**

1. Recalculate carry for each pair
2. Rank pairs
3. Adjust weights (equal weight or carry-weighted)
4. Rebalance to targets

**Avoid:**
- Daily (too frequent, costs high)
- Annual (too infrequent, miss changes)

### 7. Correlation Monitoring

**Quarterly review:**

Calculate pairwise correlations:
- If avg correlation >0.7: Too concentrated
- Action: Add uncorrelated pairs or reduce exposure

**Example:**

**4-pair basket:**
- AUD/JPY vs NZD/JPY: 0.88 (too high!)
- Action: Replace NZD/JPY with EUR/NOK (corr 0.30)

---

## Real-World Examples

### 1. 2008 Financial Crisis

**Carry crash:**

**Setup (2007):**
- AUD/JPY: ~105, carry 5%
- Popular crowded trade
- Leverage: 5-10× typical

**Crash (Aug-Oct 2008):**
- AUD/JPY: 105 → 60 (−43%)
- NZD/JPY: 95 → 52 (−45%)
- GBP/JPY: 215 → 120 (−44%)

**Leveraged impact:**
- 5× leverage: -215% (total wipeout + owe money)
- 1× leverage: -43% (painful but survivable)

**Recovery:**
- 2009-2010: Partial recovery
- Many traders wiped out, missed recovery

**Lesson:** Leverage kills in carry crashes

### 2. Swiss Franc Un-Peg (January 2015)

**Event:** SNB removes EUR/CHF floor

**Background:**
- SNB held EUR/CHF ≥ 1.20 (since 2011)
- Carry trade: Short CHF (safe haven), long EUR

**January 15, 2015:**
- SNB announces removal (no warning)
- EUR/CHF: 1.20 → 0.85 in minutes (−29%)

**Impact:**
- EUR/CHF carry: −29% instantly
- Leveraged traders: Total wipeout
- Some brokers bankrupted (FXCM lost $225M)

**Lesson:** Central bank policy risk catastrophic

### 3. EM Crisis 1998

**Russian default + LTCM:**

**Carry trades (typical):**
- Short USD (funding)
- Long RUB, BRL, MXN, ZAR (targets)

**August 1998:**
- Russia defaults
- RUB collapses −70%
- Contagion: BRL −35%, MXN −25%, ZAR −30%

**USD/BRL:**
- Carry: +20% (YTD before crisis)
- August crash: −35%
- **Net: −15% YTD**

**LTCM collapse:**
- Massive carry unwind
- Amplified moves

**Lesson:** EM contagion, all crash together

### 4. COVID Crash (March 2020)

**Risk-off extreme:**

**February 2020:**
- VIX: 15 (calm)
- Carry trades: +2% YTD

**March 2020:**
- VIX: 15 → 85 (record)
- Flight to safe havens

**Carry performance:**
- AUD/JPY: −18%
- NZD/JPY: −20%
- BRL/USD: −32%
- MXN/USD: −28%

**Recovery (April-June):**
- VIX: 85 → 30
- Carry rebounded +15-25%

**Full year 2020:**
- Carry: −5 to +2% (depending on exit timing)

**Lesson:** Fast unwinding, fast recovery (VIX timing critical)

### 5. Taper Tantrum (2013)

**Fed policy shift:**

**May 2013:**
- Bernanke mentions tapering QE
- USD expected to strengthen

**EM carry impact:**
- BRL/USD: −15%
- TRY/USD: −18%
- INR/USD: −12%
- ZAR/USD: −14%

**Mechanism:**
- USD strengthens (funding currency)
- EM currencies weaken (risk-off)
- Carry unwinds

**Duration:** 3 months of pain

**Lesson:** Fed policy major driver

### 6. Japan Intervention (2022-2024)

**JPY weakness then reversal:**

**2022:**
- USD/JPY: 115 → 152 (+32%)
- Carry: +32% from spot + carry
- Best carry year in decade

**October 2022:**
- BoJ intervenes (first time since 1998)
- USD/JPY: 152 → 145 in hours (−4.6%)

**2023-2024:**
- USD/JPY: Volatile 125-152 range
- Intervention risk limits carry

**Lesson:** Central bank actions unpredictable, can reverse years of gains quickly

### 7. AUD/JPY Bull Run (2001-2007)

**Sustained carry success:**

**2001:**
- AUD/JPY: 55
- Carry: 5-6% annually

**2007:**
- AUD/JPY: 105 (+91%)
- Cumulative carry: +35%
- **Total: +126%** over 6 years

**Then 2008:**
- Crash to 60 (−43%)
- **Gave back half the gains in 3 months**

**Lesson:** Carry works for long periods, then crashes violently (negative skew)

---

## Practical Steps

### 1. Calculate Carry

**For each pair:**

$$
\text{Carry} = r_{\text{target}} - r_{\text{funding}}
$$

**Example:**

**USD/BRL:**
- BCB rate (BRL): 11.75%
- Fed rate (USD): 5.50%
- **Carry: 6.25% annually**

**AUD/JPY:**
- RBA rate (AUD): 4.35%
- BoJ rate (JPY): 0.25%
- **Carry: 4.10% annually**

### 2. Rank Pairs by Carry

**Create ranking:**

| Pair | Carry | Rank |
|------|-------|------|
| USD/TRY | 35.0% | 1 |
| USD/BRL | 6.25% | 2 |
| AUD/JPY | 4.10% | 3 |
| EUR/NOK | 2.50% | 4 |
| GBP/CHF | 1.75% | 5 |

**Select top 5-8 for diversified basket**

### 3. Check VIX Level

**Current VIX:**
- VIX: 18
- **Allocation: 75%** (per VIX rule)

**Adjust positions:**
- Target: $1M
- VIX-adjusted: $750K in carry
- $250K in cash

### 4. Size Positions

**Equal weight approach:**

8 pairs, $750K allocation:
- Per pair: $750K / 8 = $93,750

**Example positions:**
1. USD/BRL: $93,750
2. AUD/JPY: $93,750
3. NZD/JPY: $93,750
... (8 total)

**Carry-weighted approach:**

Weight by carry (higher carry = larger position):

$$
\text{Weight}_i = \frac{\text{Carry}_i}{\sum \text{Carry}}
$$

**Example:**

Total carry: 40%
- USD/BRL (6.25%): $750K × 6.25% / 40% = $117K
- AUD/JPY (4.10%): $750K × 4.10% / 40% = $77K
- Etc.

### 5. Execute Trades

**For each pair:**

**USD/BRL (long BRL):**
- Spot: 5.00
- Notional: $93,750
- BRL: 468,750

**Trade:**
- Buy: 468,750 BRL
- Sell: $93,750 USD
- Hold position (earn carry daily)

**Daily carry accrual:**
- Annual: 6.25%
- Daily: 6.25% / 365 = 0.017%
- Dollar amount: $93,750 × 0.017% = **$16/day**

### 6. Monitor Daily

**Check each position:**

**P&L components:**

$$
\text{P&L} = \text{Carry Accrued} + \text{Spot Move}
$$

**Example (USD/BRL after 30 days):**

**Carry:**
- 30 days × $16 = $480

**Spot:**
- Entry: 5.00
- Current: 4.95 (BRL appreciated 1%)
- Spot gain: $93,750 × 1% = $938

**Total P&L: +$1,418** (1.5% in 30 days)

### 7. Rebalance Monthly

**End of month:**

1. **Recalculate carry** (rates may have changed)
2. **Check VIX** (adjust overall exposure)
3. **Rerank pairs** (remove pairs with carry <2%)
4. **Rebalance to equal weights** (or carry-weighted)

**Example:**

**Changes:**
- TRY rate increased: 35% → 42% (risky, exclude)
- Fed cut: USD rate 5.5% → 5.0% (carry increased on USD/BRL)
- VIX: 18 → 22 (reduce exposure 75% → 50%)

**Actions:**
- Remove TRY positions
- Increase USD/BRL weight
- Reduce overall exposure to $500K

---

## Final Wisdom

> "FX carry trades are the ultimate 'pick up pennies in front of a steamroller' strategy—they work beautifully 80% of the time (historical win rate), generating 5-10% annually with Sharpe ratios of 0.4-0.8, but crash catastrophically the other 20% (2008: -43% in three months, 2015 CHF un-peg: -29% overnight, 2020 COVID: -30%), exhibiting severe negative skewness where the 95th percentile loss is 5-10× the median gain. The fundamental mechanism is simple: borrow low-rate currencies (JPY at 0.1%, CHF at 0.5%, USD when Fed at zero) and invest in high-rate currencies (BRL at 11%, TRY at 35%, MXN at 10%), pocketing the interest differential (carry) which compounds daily at the rate differential—for example, USD/BRL at 11% carry accrues $30/day on $100K notional, $11K annually, seemingly 'risk-free' money. The catch is currency risk: if BRL depreciates 15%, the 11% carry becomes -4% net, and this depreciation risk is NOT random—it's systematically correlated with global risk appetite, creating the portfolio's Achilles heel. Uncovered Interest Parity (UIP) theory says expected spot change should equal interest differential (high-rate currencies should depreciate by exactly the carry amount, eliminating profit), but empirically UIP fails: high-rate currencies depreciate less than predicted ~70% of the time, making carry profitable on average. Why? Three explanations dominate: (1) crash risk premium—carry is compensation for tail risk (crashes in crises), (2) liquidity premium—low-rate currencies (JPY, CHF) are liquid safe havens, high-rate currencies are less liquid EM, and (3) political/economic risk—high rates reflect instability that occasionally materializes violently. The 'short volatility' characterization is precise: carry strategies collect small positive returns in calm periods (low VIX) but suffer massive drawdowns when volatility spikes (high VIX), exactly like selling put options or insurance—you collect premiums 95% of time, then pay out 20-50× in the 5%. Empirical VIX relationship is stark: when VIX <15 (calm), carry wins 75% of months; when VIX 15-25 (moderate), 50%; when VIX >25 (stress), 30%; when VIX >40 (crisis), carry loses 80% of time with average -15% monthly returns. The 2008 example is canonical: AUD/JPY traded 100-105 for years (2005-2007) earning 5% annual carry, lulling traders into complacency and leverage (typical 5-10× for retail, 2-5× for institutions), then crashed from 105 to 60 (-43%) in three months as Lehman failed, risk appetite collapsed, and funding currencies (JPY) appreciated violently due to repatriation flows and safe-haven demand. At 10× leverage, this was a -430% loss (total wipeout + debt), and even at conservative 2× leverage it was -86% (catastrophic). The diversification illusion is dangerous: in normal times, AUD/JPY and BRL/USD have correlation ~0.3-0.4 (decent diversification), but in crises correlation spikes to 0.85-0.95 as ALL carry trades unwind simultaneously—the 2008 correlation among AUD/JPY, NZD/JPY, GBP/JPY exceeded 0.90, meaning a 'diversified' 10-pair basket behaved like 1-2 effective positions. Leverage is the killer: while 1× leverage on AUD/JPY produced -43% drawdown in 2008 (painful but survivable), 5× leverage produced total wipeout, and historical data shows that overleveraged carry funds (>3×) have 80%+ failure rate over 10-year horizons despite strategy's positive expected value. The TRY trap illustrates extreme-carry danger: Turkish Lira offered 40% carry (2018-2023), seemingly irresistible, but depreciated -75% over the period, producing -37.5% net return despite massive carry—ultra-high rates (>20%) are almost always warning signs of imminent currency collapse, not opportunity. Risk management is non-negotiable: (1) max 1-2× leverage (3× absolute ceiling), (2) VIX filter (exit at VIX >30, re-enter <20), (3) diversify 8-12 pairs (max 10-15% each), (4) volatility targeting (reduce exposure when vol rises), (5) stop-loss -15% per pair and -10% portfolio-wide, (6) monthly rebalancing (rates and correlations change), (7) avoid extreme carry (cap at 15%, exclude >20%). The momentum enhancement is empirically powerful: combining carry with trend-following (only long pairs with positive 3-month momentum) improves Sharpe from 0.5 to 0.7-0.8 by avoiding catastrophic drawdowns—for instance, filtering out negative-momentum pairs in 2008 would have reduced drawdown from -43% to -18%. Historical performance validates the strategy: G10 carry (AUD/JPY, NZD/JPY, etc.) returned 5-7% annually 1990-2023 with Sharpe 0.5-0.6, EM carry (BRL, MXN, ZAR) returned 8-12% with Sharpe 0.4-0.5, but max drawdowns were -25% (G10) and -35% (EM), occurring during every major crisis (1998 Russian default, 2008 Lehman, 2015 CHF un-peg, 2020 COVID). The bottom line: carry trades are a legitimate strategy for sophisticated investors who understand they're selling disaster insurance, accept negative skewness, manage leverage religiously, respect VIX signals, and diversify broadly—but for overleveraged retail traders chasing 'easy money,' they're a death trap that works wonderfully until it doesn't, then loses years of profits in weeks."

**Key to success:**

- Max 1-2× leverage (never 5-10×, that guarantees eventual wipeout)
- VIX filter: Exit when VIX >30, re-enter when <20 (avoids 80% of crashes)
- Diversify 8-12 pairs (max 10-15% each, but recognize correlation → 1 in tails)
- Volatility targeting: Reduce exposure when realized vol rises (target 10-15% annual vol)
- Minimum carry threshold: 2% + expected depreciation (avoid ultra-high carry >20%)
- Momentum filter: Only long pairs with positive 3-month trend (Sharpe 0.5 → 0.7-0.8)
- Stop-loss: -15% per pair, -10% portfolio-wide (exit and reassess)
- Monthly rebalancing: Rates change, correlations shift, re-rank and reweight
