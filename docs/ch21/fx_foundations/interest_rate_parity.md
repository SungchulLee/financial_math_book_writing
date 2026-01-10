# Interest Rate Parity

**Interest rate parity (IRP)** is the fundamental no-arbitrage relationship in foreign exchange markets that links spot exchange rates, forward exchange rates, and interest rate differentials between two currencies, stating that the forward premium/discount must equal the interest rate differential to prevent risk-free arbitrage, while deviations from parity (basis) create trading opportunities for those who can identify mispricing or structural inefficiencies.

---

## The Core Insight

**The fundamental idea:**

- Spot rate: Current exchange rate between two currencies
- Forward rate: Locked-in future exchange rate
- Interest rate differential: Difference in yields between currencies
- **IRP relationship: Forward rate determined by spot rate + interest differential**
- **Covered IRP (CIP):** Uses forward contracts (no FX risk)
- **Uncovered IRP (UIP):** Expected spot rate movement (FX risk)
- CIP violations create arbitrage (cross-currency basis)
- UIP violations create carry trade opportunities
- Post-2008: CIP frequently violated (funding constraints, regulation)
- Basis trading exploits persistent CIP deviations

**The key equations:**

**Covered Interest Rate Parity (CIP):**

$$
\frac{F}{S} = \frac{1 + r_d}{1 + r_f}
$$

Or equivalently:

$$
F = S \times \frac{1 + r_d}{1 + r_f}
$$

Where:
- $F$ = Forward exchange rate (domestic per foreign)
- $S$ = Spot exchange rate (domestic per foreign)
- $r_d$ = Domestic interest rate
- $r_f$ = Foreign interest rate

**Forward premium/discount:**

$$
\frac{F - S}{S} \approx r_d - r_f
$$

**Example:**
- Spot USD/EUR: 1.1000 (€1 = $1.10)
- USD 1-year rate: 5.0%
- EUR 1-year rate: 3.0%
- **Forward (1-year):** $F = 1.10 \times \frac{1.05}{1.03} = 1.1214$

**EUR trades at 2% premium (forward > spot) because USD rates higher.**

**Cross-currency basis:**

$$
\text{Basis} = r_d - r_f - \frac{F - S}{S}
$$

**When basis ≠ 0, arbitrage opportunity exists (in theory).**

**Uncovered Interest Rate Parity (UIP):**

$$
E[S_{t+1}] - S_t \approx r_d - r_f
$$

Expected currency depreciation equals interest rate differential.

**You're essentially asking: "What should the forward rate be given interest rate differentials, and when forwards deviate from fair value (basis ≠ 0), how do I profit from this mispricing while managing the funding, credit, and regulatory constraints that create these persistent deviations?"**

---

## What is Interest Rate Parity?

**Before trading IRP violations, understand the framework:**

### Covered Interest Rate Parity (CIP)

**The no-arbitrage condition:**

**Strategy A: Invest in domestic currency**
1. Invest $1 at rate $r_d$
2. After 1 year: $1 \times (1 + r_d)$

**Strategy B: Invest in foreign currency (hedged)**
1. Convert $1 to foreign currency: $1/S$ units
2. Invest foreign at rate $r_f$: $(1/S) \times (1 + r_f)$
3. Lock in forward to convert back at rate $F$
4. After 1 year: $(1/S) \times (1 + r_f) \times F$

**No-arbitrage condition:**

$$
1 \times (1 + r_d) = \frac{1}{S} \times (1 + r_f) \times F
$$

**Solving for F:**

$$
F = S \times \frac{1 + r_d}{1 + r_f}
$$

**This is Covered Interest Rate Parity!**

**Numerical example:**

**Given:**
- Spot USD/JPY: 110.00 (¥110 = $1)
- USD 1-year rate: 4.5%
- JPY 1-year rate: 0.5%

**Strategy A (invest USD):**
- Start: $1,000,000
- End: $1,000,000 × 1.045 = **$1,045,000**

**Strategy B (invest JPY, hedged):**
- Convert to JPY: $1,000,000 × 110 = ¥110,000,000
- Invest JPY: ¥110,000,000 × 1.005 = ¥110,550,000
- Forward rate (from CIP): $F = 110 \times \frac{1.045}{1.005} = 114.37$
- Convert back: ¥110,550,000 / 114.37 = **$966,689**

**Wait, Strategy B lost money!**

**Problem: I used spot rate to convert back. Should use FORWARD rate locked in at start.**

**Strategy B (correct):**
- Lock in forward at 114.37
- After 1 year: ¥110,550,000 / 114.37 = **$966,689**

**Still losing! What's wrong?**

**Ah! Forward rate calculation is wrong. Let me recalculate:**

**Correct forward rate:**

$$
F = 110 \times \frac{1.045}{1.005} = 114.37
$$

**But if I lock in 114.37 forward today:**
- Pay $1M today, get ¥110M
- Invest ¥110M at 0.5%, get ¥110.55M
- Forward contract: Sell ¥110.55M at 114.37, get $966,689

**This is WRONG! The forward contract is for the PRINCIPAL, not principal + interest!**

**Let me restart with correct understanding:**

**Strategy B (correct understanding):**

1. **Today:** 
   - Borrow $1M at 4.5% for 1 year (owe $1.045M)
   - Convert to JPY at spot: ¥110M
   - Invest ¥110M at 0.5%
   - Sell forward: ¥110.55M at rate $F$

2. **1 year later:**
   - Receive: ¥110.55M (investment matures)
   - Forward settles: Receive ¥110.55M / $F$ = dollars
   - Repay loan: $1.045M

**For no-arbitrage (zero profit):**

$$
\frac{110.55M}{F} = 1.045M
$$

$$
F = \frac{110.55}{1.045} = 105.74
$$

**Wait, this gives forward LOWER than spot (110), but JPY rates are lower than USD!**

**I'm confusing quote conventions. Let me use consistent notation:**

**USD/JPY = 110 means: 1 USD = 110 JPY, or equivalently, 1 JPY = 1/110 USD**

**Let me use $S$ = USD per JPY (0.00909) instead:**

**Given:**
- $S$ = 0.00909 USD/JPY (or equivalently, JPY/USD = 110)
- $r_{\text{USD}}$ = 4.5%
- $r_{\text{JPY}}$ = 0.5%

**CIP formula:**

$$
F_{\text{USD/JPY}} = S_{\text{USD/JPY}} \times \frac{1 + r_{\text{USD}}}{1 + r_{\text{JPY}}}
$$

$$
F = 0.00909 \times \frac{1.045}{1.005} = 0.00945 \text{ USD/JPY}
$$

**Equivalently in JPY/USD:**

$$
F_{\text{JPY/USD}} = 1/0.00945 = 105.82 \text{ JPY/USD}
$$

**So forward JPY/USD = 105.82 (less than spot 110)**

**JPY strengthens in forward (105.82 < 110 means you need fewer JPY to buy $1)**

**This makes sense! USD has higher rates, so USD weakens in forward to offset rate advantage.**

**Summary:**
- Spot: 110 JPY/USD
- Forward: 105.82 JPY/USD
- USD depreciated from 110 → 105.82 (need fewer JPY per USD)
- Compensates for 4% interest rate advantage

### Uncovered Interest Rate Parity (UIP)

**Without hedging:**

If investors are risk-neutral and markets efficient:

$$
E\left[\frac{S_{t+1} - S_t}{S_t}\right] = r_d - r_f
$$

**Expected spot rate change equals interest differential.**

**Example:**
- Spot: 110 JPY/USD
- USD rate: 4.5%, JPY rate: 0.5%
- Differential: 4.0%
- **UIP prediction:** USD should depreciate 4% over 1 year
- **Expected spot (1 year):** 110 / 1.04 = 105.77 JPY/USD

**UIP rarely holds in practice!**

**Empirical evidence:**
- High interest rate currencies tend to APPRECIATE (not depreciate)
- This is the **forward premium puzzle**
- Creates carry trade opportunities

**Why UIP fails:**
1. Risk premium (high rate currencies perceived risky)
2. Central bank intervention
3. Safe haven flows
4. Peso problems (rare crashes)

### Forward Points and Swap Points

**Market convention: Quote forward as points (pips) from spot**

$$
\text{Forward Points} = (F - S) \times 10,000 \text{ (for 4-decimal currencies)}
$$

**Example:**
- Spot USD/EUR: 1.1000
- 1-year forward: 1.1020
- **Forward points: +20 pips**
- EUR at premium (forward > spot)

**Annual forward premium:**

$$
\text{Premium} = \frac{F - S}{S} = \frac{1.1020 - 1.1000}{1.1000} = 0.0182 = 1.82\%
$$

**Should equal interest differential:**
- EUR rate: 3.0%
- USD rate: 5.0%
- Differential: -2.0%
- **Close to 1.82% but not exact (basis exists)**

**Swap points** = Forward points, used in FX swaps.

---

## Economic Interpretation: Why Deviations Occur

**Understanding when and why CIP breaks down:**

### The Pre-2008 World: CIP Held

**Before financial crisis:**
- CIP deviations tiny (< 5 bp)
- Arbitrage quickly eliminated mispricings
- Banks had balance sheet capacity
- Funding cheap and abundant

**Arbitrage mechanism:**

**If F > Fair Value (forward too expensive):**

1. Borrow domestic currency
2. Convert to foreign at spot
3. Invest foreign currency
4. Sell foreign forward
5. **Profit = Basis (spread > 0)**

**Example (pre-2008):**
- Fair forward: 1.1020
- Actual forward: 1.1025 (5 pips rich)
- Arbitrage profit: 5 pips (0.045%)
- **Immediate risk-free profit!**

**This kept CIP tight.**

### Post-2008: CIP Breakdown

**After 2008 crisis:**
- CIP violations persistent (up to 100+ bp!)
- Arbitrage limited
- **Why?**

**1. Funding constraints:**

**Banks can't fund arbitrage because:**
- Balance sheets constrained (leverage limits)
- USD funding scarce (especially for non-US banks)
- Regulatory capital charges (Basel III)

**2. Counterparty risk:**

Forward contracts have credit risk. Post-2008:
- Higher counterparty risk premium
- Collateral requirements

**3. Cross-currency basis:**

Persistent deviation from CIP:

$$
\text{Basis} = (F - S)/S - (r_d - r_f) \neq 0
$$

**Typical post-2008:**
- EUR/USD basis: -20 to -50 bp (EUR "cheap")
- JPY/USD basis: -30 to -80 bp (JPY "cheap")
- **Negative basis = borrowing USD via FX swap costs more than domestic USD rate**

**Why basis persists:**

**Demand/supply imbalance:**
- Non-US banks need USD funding (large USD assets)
- Use FX swaps to convert EUR/JPY to USD
- **Excess demand for USD in FX swap market**
- Drives basis negative

**Example:**

European bank with USD assets:
- Has EUR, needs USD
- Option 1: Borrow USD at 5.0% (expensive)
- Option 2: Borrow EUR at 3.0%, swap to USD via FX swap
  - Cost: 3.0% + 2.0% (interest differential) + 0.5% (basis)
  - **Total: 5.5%** (more expensive than direct USD!)

**But still cheaper than alternatives (CP market, deposits).**

**This structural demand keeps basis negative.**

### The Cross-Currency Basis Trade

**Exploiting persistent basis:**

**Setup:**
- EUR/USD basis: -30 bp
- This means: EUR is "cheap" in FX swap market

**Trade:**
1. Lend USD (receive USD interest)
2. Borrow EUR (pay EUR interest)  
3. FX swap: EUR → USD (pay basis)
4. **Profit from basis if it persists**

**P/L:**
- Receive: USD rate 5.0%
- Pay: EUR rate 3.0% + basis 0.3%
- **Net: 5.0% - 3.3% = 1.7%**

**But requires:**
- Balance sheet capacity
- USD funding access
- Leverage

**Why it's not arbitraged away:**
- Banks constrained by regulations
- Hedge funds have limited size
- **Basis can persist for years**

---

## Key Terminology

**Spot Exchange Rate:**

- Current exchange rate for immediate delivery
- Convention: 2 business days settlement
- Quote: Domestic currency per foreign (e.g., USD/EUR = 1.10 means €1 = $1.10)

**Forward Exchange Rate:**

- Locked-in future exchange rate
- Settlement: 1 month, 3 months, 1 year, etc.
- Determined by CIP: $F = S \times \frac{1+r_d}{1+r_f}$

**Forward Premium/Discount:**

$$
\text{Premium} = \frac{F - S}{S}
$$

- Premium (F > S): Foreign currency appreciates in forward
- Discount (F < S): Foreign currency depreciates in forward
- Should equal interest differential (when CIP holds)

**Forward Points (Pips):**

- Difference between forward and spot, in smallest unit
- Convention: $(F - S) \times 10,000$ for 4-decimal currencies
- Example: Spot 1.1000, Forward 1.1020 → Forward points = +20

**Swap Points:**

- Same as forward points
- Used in FX swaps (spot + forward combined)
- Market convention: Quote swaps in points

**FX Swap:**

- Simultaneous spot and forward transaction
- Example: Buy EUR spot, sell EUR forward
- Net exposure: Zero (spot offsets forward)
- Used for funding, not speculation

**Cross-Currency Basis:**

$$
\text{Basis} = (F - S)/S - (r_d - r_f)
$$

- Deviation from CIP
- Negative basis: Foreign currency "cheap" in swap market
- Typical: EUR/USD -20 to -50 bp, JPY/USD -30 to -80 bp

**Covered Interest Arbitrage:**

- Exploit CIP violations
- Borrow low-rate, invest high-rate, hedge with forward
- Profit = Basis (if positive)
- Post-2008: Limited by funding constraints

**Interest Rate Differential:**

$$
r_d - r_f
$$

- Drives forward premium/discount
- Higher domestic rate → Domestic currency depreciates in forward
- Lower domestic rate → Domestic currency appreciates in forward

**Carry Trade:**

- Borrow low interest rate currency
- Invest high interest rate currency
- Profit = Interest differential (if spot doesn't move)
- Violates UIP (bet that high rate currency won't depreciate)

**Forward Premium Puzzle:**

- Empirical observation: High interest rate currencies appreciate (not depreciate)
- Violates UIP
- Creates carry trade opportunity

---

## Basic Interest Rate Parity Strategies

### Strategy 1: Classic Covered Interest Arbitrage

**Setup:**

**Market inefficiency (rare post-2008):**

**USD/EUR rates:**
- Spot: 1.1000 USD/EUR
- 1-year USD rate: 5.0%
- 1-year EUR rate: 3.0%
- Fair forward: $1.10 \times \frac{1.05}{1.03} = 1.1214$

**Actual market:**
- 1-year forward: 1.1250 (too high!)
- Basis: +36 pips or +0.32%

**EUR forward premium exceeds interest differential!**

**Arbitrage trade:**

1. **Borrow USD:** $10M at 5.0%
2. **Convert to EUR at spot:** $10M / 1.10 = €9.09M
3. **Invest EUR:** €9.09M at 3.0% = €9.364M after 1 year
4. **Sell EUR forward:** €9.364M at 1.1250 = $10.534M

**1-year P/L:**

| Component | Amount |
|-----------|--------|
| Forward proceeds | $10.534M |
| Loan repayment | -$10.50M |
| **Profit** | **$0.034M** |

**Return on capital (assume 10% margin): 34%**

**No FX risk! Locked in at trade inception.**

**In practice (post-2008):**
- This arbitrage rare (markets efficient)
- If exists, limited by:
  - Balance sheet capacity
  - Funding availability
  - Counterparty limits

**Realistic basis: -30 bp (not +32 bp)**

### Strategy 2: Cross-Currency Basis Trade (EUR/USD)

**Setup:**

**Structural basis (persistent):**

**EUR/USD 3-month:**
- Spot: 1.1000
- EUR 3M rate: 3.5%
- USD 3M rate: 5.5%
- Differential: -2.0% (USD higher)

**Fair forward:**
$$
F = 1.10 \times \frac{1 + 0.055 \times 0.25}{1 + 0.035 \times 0.25} = 1.1055
$$

**Actual forward: 1.1075**

**Basis:**
$$
\text{Basis} = \frac{1.1075 - 1.10}{1.10} \times \frac{1}{0.25} - 0.02 = 0.0273 - 0.02 = 0.73\%
$$

**Wait, positive basis? Let me recalculate...**

**Actually, let's compute basis correctly:**

Annual forward premium:
$$
\text{Premium} = \frac{1.1075 - 1.10}{1.10} \times \frac{1}{0.25} = 2.73\%
$$

Interest differential: 5.5% - 3.5% = 2.0%

**Basis = 2.73% - 2.0% = +0.73%** (positive, unusual)

**Typically post-2008, EUR/USD basis is NEGATIVE (-30 to -50 bp).**

**Let me use realistic example:**

**Realistic EUR/USD 3-month:**
- Forward: 1.1045 (not 1.1075)
- Premium: (1.1045 - 1.10) / 1.10 × 4 = 1.64% annualized
- Differential: 2.0%
- **Basis: 1.64% - 2.0% = -0.36% or -36 bp**

**Negative basis means EUR is "cheap" in FX swap market.**

**Trade (exploiting negative basis):**

**Long basis trade:**
1. Lend USD (buy USD deposit/bond)
2. Borrow EUR
3. FX swap: EUR → USD at spot, USD → EUR at forward
4. Profit from collecting USD interest vs. paying EUR interest + basis

**Structure (for $10M notional):**

| Action | Cashflow |
|--------|----------|
| Lend USD | -$10M (today), +$10M × 1.01375 (3M) |
| Borrow EUR | +€9.09M (today), -€9.09M × 1.00875 (3M) |
| FX swap: Spot | +$10M, -€9.09M |
| FX swap: Forward | -$10M, +€9.09M |

**Net cashflow (today):** $0$ (self-financing)

**Net cashflow (3 months):**
- USD: $10M × 1.01375 - $10M = $0.1375M
- EUR: $€9.09M × 1.00875 - €9.09M = €0.0796M$
- Convert EUR at forward: €0.0796M × 1.1045 = $0.0879M
- **Net: $0.1375M - $0.0879M = $0.0496M**

**Return: 0.496% over 3 months = 1.98% annualized**

**But wait, I need to include the basis in the forward rate!**

**Let me be more careful. The basis means:**

Effective EUR borrowing cost via FX swap:
$$
\text{Cost} = r_{\text{EUR}} + (r_{\text{USD}} - r_{\text{EUR}}) + \text{Basis}
$$
$$
= 3.5\% + 2.0\% - 0.36\% = 5.14\%
$$

**So borrowing EUR and swapping to USD costs 5.14%, while USD rate is only 5.5%.**

**Profit = 5.5% - 5.14% = 0.36%** (the basis!)

**This is the trade: Capture the basis.**

**Risks:**
1. **Basis can widen** (more negative, lose money)
2. **Rollover risk** (3M basis changes when rolling)
3. **Funding risk** (can't refinance EUR borrow)

### Strategy 3: Carry Trade with Forward Hedge (Modified)

**Setup:**

**High carry opportunity:**

**AUD/USD:**
- Spot: 0.7000 (1 AUD = 0.70 USD)
- AUD 1-year rate: 4.0%
- USD 1-year rate: 5.5%
- Differential: -1.5% (USD higher)

**Fair forward (CIP):**
$$
F = 0.70 \times \frac{1.055}{1.04} = 0.7101
$$

**AUD depreciates to 0.7101 (from 0.70) = +1.44% depreciation**

**This compensates for 1.5% rate disadvantage.**

**Uncovered carry (no hedge):**
- Borrow USD at 5.5%
- Invest AUD at 4.0%
- **If spot unchanged:** Lose -1.5% (interest differential)

**UIP says AUD should appreciate 1.5% to offset. But empirically, high rate currencies appreciate!**

**Modified strategy: Hedge with forward, capture basis**

**Actual market (with basis):**
- AUD/USD forward: 0.7080 (not 0.7101)
- **Basis: +21 bp** (AUD rich in forward)

**Trade:**
1. Borrow USD at 5.5%
2. Invest AUD at 4.0%
3. Hedge with forward: Sell AUD at 0.7080
4. Profit from basis

**P/L (on $1M):**

| Component | Amount |
|-----------|--------|
| USD borrowed | -$1M × 1.055 = -$1.055M |
| Convert to AUD | $1M / 0.70 = 1.4286M AUD |
| AUD invested | 1.4286M × 1.04 = 1.4857M AUD |
| Forward sell AUD | 1.4857M × 0.7080 = $1.0519M |
| **Profit** | **$1.0519M - $1.055M = -$0.0031M** |

**Lost money! The basis wasn't large enough to offset interest differential fully.**

**Issue: USD rates higher (5.5%) vs. AUD (4.0%), so need basis to be more positive to profit.**

**This shows: Covered carry trades need large basis to work when borrowing currency has higher rate.**

### Strategy 4: Basis Convergence Trade

**Setup:**

**Historical mean reversion:**

**EUR/USD 1-year basis:**
- Current: -50 bp (very wide, 95th percentile)
- Historical average: -25 bp
- **Expected: Basis narrows to -25 bp over 6 months**

**Trade:**
- Enter basis position at -50 bp
- Exit when narrows to -25 bp
- Profit: 25 bp convergence

**Structure:**

For $50M notional:
1. Enter 1-year EUR/USD basis at -50 bp
2. If basis narrows to -25 bp in 6 months:
   - Unwind position
   - Capture 25 bp × $50M × 0.5 years = $62,500

**Risks:**
1. **Basis widens to -70 bp:** Lose 20 bp = -$50k
2. **Rollover:** May need to roll 1-year into new 1-year
3. **Mark-to-market:** Daily P&L volatility

**Position Greeks:**

**DV01 (basis sensitivity):**
$$
\text{DV01} = \text{Notional} \times \text{Duration}
$$
$$
= \$50M \times 1.0 = \$50k \text{ per bp}
$$

**If basis moves 1 bp, P&L changes $50k.**

**Historical volatility of EUR/USD basis: 15 bp (3-month)**

**VaR (95%):**
$$
\text{VaR} = 1.65 \times 15 \text{ bp} \times \$50k = \$1.24M
$$

**Need to size position appropriately for risk tolerance.**

---

## Greeks in Interest Rate Parity Trading

**Understanding sensitivities:**

### Delta: FX Spot Sensitivity

**For covered arbitrage or basis trades:**

If properly hedged with forward:
$$
\Delta_{\text{FX}} = 0
$$

**No sensitivity to spot moves!** This is the key advantage of covered positions.

**Example:**
- Long EUR spot
- Short EUR forward (same notional)
- **Net FX exposure: Zero**

**Spot moves from 1.10 → 1.15:**
- Spot position: +$50k gain
- Forward position: -$50k loss
- **Net: $0**

**Uncovered carry trades:**

$$
\Delta_{\text{FX}} = \text{Notional} \times \frac{\partial P/L}{\partial S} = \text{Notional}
$$

**Full FX exposure!**

### Interest Rate Duration

**Covered positions have duration risk:**

**When interest rates change:**

**Scenario: USD rates rise 1%**

- Old fair forward: $F = 1.10 \times \frac{1.05}{1.03} = 1.1214$
- New fair forward: $F = 1.10 \times \frac{1.06}{1.03} = 1.1320$
- **Forward rises by 106 pips**

**If you're short forward at 1.1214:**
- Mark-to-market loss: 106 pips
- On $10M: Loss = -$10M × 0.0106 = -$106k

**Interest rate duration:**

For 1-year forward:
$$
\text{Duration} \approx 1.0 \text{ year}
$$

For 3-month forward:
$$
\text{Duration} \approx 0.25 \text{ year}
$$

**Longer maturity forwards have higher duration risk.**

**Hedging:** Use interest rate swaps to offset duration.

### Basis Risk (Specific to Cross-Currency Basis)

**Basis can be volatile:**

**EUR/USD 1-year basis volatility: ~15 bp (quarterly)**

**Position:**
- Long EUR/USD basis at -30 bp
- Notional: $100M
- Duration: 1 year

**If basis widens to -45 bp:**
- Loss: 15 bp × $100M = -$1.5M

**Basis risk factors:**
1. **Quarter-end:** Banks window-dress, basis spikes
2. **Year-end:** Massive widening (up to -100 bp!)
3. **Stress events:** USD shortage → Basis widens
4. **Regulatory changes:** Basel, Dodd-Frank impact

**Year-end basis widening example:**

**EUR/USD basis:**
- Normal: -30 bp
- Year-end (December 31): -80 bp
- January 2: -35 bp (reverts)

**If you're long basis going into year-end:**
- Temporary MTM loss: -50 bp
- Recovers in January

**Risk management:** Reduce position size before quarter/year-end.

### Cross-Currency Correlation

**Multiple basis positions:**

**EUR/USD basis and JPY/USD basis are correlated:**

$$
\rho_{\text{EUR/USD, JPY/USD}} \approx 0.7
$$

**Both driven by USD funding stress.**

**Portfolio with:**
- $100M EUR/USD basis
- $100M JPY/USD basis

**If both widen 20 bp:**
- EUR/USD loss: -$2M
- JPY/USD loss: -$2M
- **Total: -$4M**

**Diversification limited by correlation!**

**Better:** Combine USD basis trades with non-USD crosses (EUR/JPY, AUD/JPY) which have lower correlation.

---

## Interest Rate Parity Payoff Analysis

### Covered Arbitrage Expected Returns

**Setup:**
- Positive basis: +50 bp
- Notional: $10M
- Tenor: 3 months

**Scenario analysis:**

| Outcome | Probability | Basis Move | P/L | Notes |
|---------|-------------|------------|-----|-------|
| Basis persists | 40% | 0 bp | +$12.5k | Collect 50 bp × 0.25 years |
| Basis tightens | 30% | -30 bp | -$62.5k | Loses 30 bp, collects 20 bp |
| Basis widens | 20% | +20 bp | +$62.5k | Gain 20 bp + collect 50 bp |
| Extreme widening | 10% | +50 bp | +$137.5k | Crisis scenario |

**Expected value:**

$$
E[P/L] = 0.4(12.5k) + 0.3(-62.5k) + 0.2(62.5k) + 0.1(137.5k)
$$
$$
= 5k - 18.75k + 12.5k + 13.75k = \$12.5k
$$

**Expected return: 1.25% over 3 months = 5% annualized**

**But requires:**
- Balance sheet usage
- Funding availability
- Counterparty limits

**Sharpe ratio: ~0.8-1.2** (moderate volatility from basis moves)

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/irp_basis_trade_distribution.png?raw=true" alt="irp_basis_trade_distribution" width="700">
</p>
**Figure 1:** P/L distribution for basis trade showing moderate positive expected return with tail risk from extreme basis widening in crisis scenarios.

### Uncovered Carry Trade Distribution

**Setup:**
- Borrow USD at 5%, invest AUD at 4%
- Negative carry: -1%
- Hope for AUD appreciation

**Scenario analysis (1 year):**

| Outcome | Probability | FX Move | Carry | Total | Notes |
|---------|-------------|---------|-------|-------|-------|
| AUD rallies | 25% | +10% | -1% | +9% | Risk-on |
| AUD stable | 20% | +2% | -1% | +1% | Neutral |
| AUD weak | 30% | -2% | -1% | -3% | Mild risk-off |
| AUD crash | 15% | -15% | -1% | -16% | Crisis |
| AUD collapse | 10% | -25% | -1% | -26% | Extreme |

**Expected value:**

$$
E[R] = 0.25(9\%) + 0.20(1\%) + 0.30(-3\%) + 0.15(-16\%) + 0.10(-26\%)
$$
$$
= 2.25\% + 0.2\% - 0.9\% - 2.4\% - 2.6\% = -3.45\%
$$

**Negative expected return!**

**This shows: Uncovered carry with NEGATIVE carry is bad bet.**

**Typical carry trade: Borrow LOW rate, invest HIGH rate**

**Better example:**

**Borrow JPY at 0%, invest BRL at 12%:**
- Positive carry: +12%
- If BRL depreciates <12%, still profit

**Empirical evidence:**
- Carry trades profitable on average
- But crash risk (25% drawdowns)
- Sharpe ratio: ~0.5-0.7 (risky)

---

## Real-World Interest Rate Parity Examples

### Example 1: Swiss Franc Negative Rates (2015) - Basis Explosion

**Setup:**

- **Date:** January 2015
- **Event:** Swiss National Bank (SNB) removes EUR/CHF floor
- **Impact:** CHF appreciates 20% in minutes

**Pre-event:**

**EUR/CHF:**
- Spot: 1.2000 (floor maintained by SNB)
- CHF 3M rate: -0.75% (negative!)
- EUR 3M rate: 0.05%
- Differential: 0.80%

**Fair forward:**
$$
F = 1.20 \times \frac{1.0005^{0.25}}{0.9925^{0.25}} = 1.2024
$$

**CHF appreciates in forward (1.2024 > 1.20) despite lower rates!**

**Why?** Negative rates violate normal IRP intuition.

**Actual market forward: 1.2030**

**Basis: Small (+6 bp)**

**The trade (pre-crisis):**

**Hedge funds betting on floor removal:**

1. Short EUR/CHF spot (bet on CHF appreciation)
2. Long EUR/CHF forward (hedge)
3. **Net: Short-term speculation, long-term hedge**

**January 15, 2015: SNB Announcement**

**SNB removes floor!**

**EUR/CHF:**
- Spot: 1.2000 → 0.9800 (-18.3%) in 10 minutes
- **CHF appreciated 22.4%!**

**Forward market chaos:**
- Forward: 1.2030 → 0.9950
- **Massive gap**

**Impact on trades:**

**Speculators short EUR/CHF:**
- Shorted at 1.20
- Covered at 0.98
- **Profit: 22% (huge!)**

**Market makers with hedged positions:**

**Position:**
- Long EUR/CHF spot (customer sales)
- Short EUR/CHF forward (hedge)
- Assumed delta-neutral

**Problem: Liquidity dried up!**

**Spot crashed to 0.98, but:**
- Forward bids disappeared
- Could only close forward at 1.00 (not 0.985 fair value)
- **Hedge didn't work!**

**P/L:**
- Spot loss: -22%
- Forward gain: Only -20% (should be -22%)
- **Net loss: -2%** on supposedly hedged position

**On $1B position: -$20M loss!**

**Why hedge failed:**
1. **Liquidity evaporated** (no forward bids)
2. **Execution gap** (couldn't close at fair value)
3. **Slippage** (2-3% worse than theoretical)

**Basis impact:**

**Post-crash basis:**
- Normal: +6 bp
- During crash: +200 bp (!)
- **Basis exploded due to market dislocation**

**Recovery (2 weeks later):**
- Basis returned to +30 bp
- **But those who couldn't hold (margin calls) realized losses**

**Lesson:**

**Covered positions are "risk-free" in theory, but:**
- Liquidity risk
- Execution risk
- Gap risk (sudden moves)

**Basis can spike 100-300 bp in crisis!**

### Example 2: Year-End Dollar Funding Squeeze (2018) - Basis Trade Winner

**Setup:**

- **Date:** December 2018
- **Trader:** Fixed income hedge fund
- **View:** Year-end USD funding squeeze will widen basis

**Market environment:**

**EUR/USD 1-week basis (early December):**
- Basis: -40 bp
- Normal year-end: -60 to -80 bp
- **Expected widening: 20-40 bp**

**Why year-end widening?**

1. **Bank window-dressing:**
   - Reduce balance sheets for year-end reporting
   - Less willing to lend USD

2. **Regulatory:**
   - Leverage ratio (Supplementary Leverage Ratio - SLR)
   - Calculated on year-end balance sheet
   - Banks shrink FX swap books

3. **Demand:**
   - Non-US banks need USD for year-end
   - Increased demand, reduced supply
   - **Basis widens (more negative)**

**Trade (December 10, 2018):**

**Short EUR/USD basis (bet on widening):**

1. Enter 1-week EUR/USD FX swap
2. Borrow EUR, lend USD
3. Position: Short basis at -40 bp
4. Notional: $500M
5. Roll weekly through year-end

**Evolution:**

**Week of December 17:**
- Basis: -40 → -55 bp
- Widened 15 bp
- **Profit: 15 bp × $500M × 1/52 = $144k**

**Week of December 24 (Christmas):**
- Basis: -55 → -75 bp
- Widened another 20 bp
- **Profit: 20 bp × $500M × 1/52 = $192k**

**Week of December 31 (year-end):**
- Basis: -75 → -105 bp (!!)
- Widened 30 bp
- **Profit: 30 bp × $500M × 1/52 = $288k**

**Total profit (3 weeks): $624k**

**Return on capital (~$50M allocated): 1.25%**

**Annualized: 21.7%** (but only works year-end)

**January 2019: Reversal**

**Post year-end:**
- Basis: -105 → -50 bp
- **Normalized!**

**Decision: Close position**
- Locked in $624k profit
- Avoided reversal

**Why it worked:**

1. **Predictable pattern:** Year-end widening happens every year
2. **Timing:** Entered 3 weeks before, exited right after
3. **Size:** $500M notional appropriate for volatility
4. **Discipline:** Closed after year-end, didn't get greedy

**Risk that didn't materialize:**

**If basis didn't widen (stayed -40 bp):**
- Opportunity cost: 3 weeks of capital tied up
- Small carry loss: ~-$50k
- **Net: -0.1% (manageable)**

**This trade exemplifies:**
- Seasonal patterns in basis
- Regulatory impact on FX markets
- Exploiting predictable stress

### Example 3: Emerging Market Carry Crash - Turkey (2018) - Loser

**Setup:**

- **Date:** January 2018
- **Investor:** EM macro fund
- **Strategy:** Carry trade in Turkish Lira

**Turkish Lira fundamentals:**

**TRY rates vs. USD:**
- TRY 1-year rate: 13.0%
- USD 1-year rate: 2.5%
- **Carry: +10.5%** (huge!)

**Uncovered carry trade:**

**Position (January 2018):**
- Borrow $50M USD at 2.5%
- Convert to TRY: $50M × 3.78 = 189M TRY
- Invest TRY at 13.0%

**Expected 1-year return:**
- TRY interest: 189M × 0.13 = 24.57M TRY
- Total TRY: 213.57M TRY
- If spot stable at 3.78:
  - USD value: 213.57M / 3.78 = $56.5M
  - Profit: $6.5M
  - **Return: 13% (13% carry - 2.5% funding)**

**Sounds great! But...**

**Evolution - The Crash:**

**February-April 2018:**
- TRY weakens moderately: 3.78 → 4.00 (-5.5%)
- Still profitable: 13% carry - 2.5% funding - 5.5% FX = **+5% YTD**

**May-July 2018:**
- Political concerns (Erdogan opposition to rate hikes)
- TRY: 4.00 → 4.80 (-16.7%)
- **YTD: 13% - 2.5% - 21% = -10.5%**

**Fund decision: "This is overdone, TRY will recover, HOLD."**

**Fatal mistake: Didn't exit when fundamentals deteriorated.**

**August 2018: The Collapse**

**August 10: US sanctions on Turkey**

**TRY crash:**
- Spot: 4.80 → 7.20 in 1 week (-33%!)
- **Total from entry (3.78 → 7.20): -47.6%**

**Position P/L (8 months):**

| Component | Return |
|-----------|--------|
| TRY interest (8 months) | +13% × 8/12 = +8.7% |
| USD funding (8 months) | -2.5% × 8/12 = -1.7% |
| FX loss | -47.6% |
| **Total** | **-40.6%** |

**On $50M position: -$20.3M**

**Forced liquidation:**

**Fund had redemptions:**
- Investors panicked (EM selloff)
- Need to raise cash
- **Forced to close TRY position at 7.20 (worst level)**

**Aftermath:**

**September-December 2018:**
- TRY partially recovered: 7.20 → 5.50
- **If held, loss would be "only" -28%**

**But couldn't hold due to:**
1. Redemptions
2. Margin calls
3. Risk limits breached

**What went catastrophically wrong:**

1. **Ignored fundamentals:**
   - Turkey's current account deficit: -5.5% of GDP
   - External debt: 60% of GDP
   - Central bank independence concerns
   - **All red flags for currency crisis**

2. **Too much carry focus:**
   - 10.5% carry seemed irresistible
   - Ignored that high rates price in devaluation risk
   - **High rates = warning sign, not opportunity**

3. **No stop loss:**
   - Down 10% in May, should have exited
   - "It will recover" mentality
   - **Pride prevented exit**

4. **Overleveraged:**
   - $50M position in single EM currency
   - 50% of fund (!)
   - **Concentration killed the fund**

5. **Ignored UIP:**
   - UIP says: High rate currencies should depreciate
   - TRY had 10.5% rate advantage
   - **Should have depreciated ~10.5%**
   - Actually depreciated 47.6% (even worse)

**The UIP puzzle didn't hold in crisis!**

**Comparison to covered position:**

**What if hedged with forward?**

**CIP forward (January 2018):**
$$
F = 3.78 \times \frac{1.025}{1.13} = 3.43
$$

**TRY appreciates to 3.43 in forward (from 3.78 spot)**

**Covered position P/L:**
- TRY interest: +13%
- USD funding: -2.5%
- Forward hedge: Locked in at 3.43
- Final value: 213.57M / 3.43 = $62.3M
- **Profit: $12.3M (+24.6%!)**

**Covered position would have made money while uncovered lost 40.6%!**

**But: Covered carry requires paying away most of the carry through forward discount.**

**Lesson:**

**Carry trades in EM:**
- High returns in calm times
- Catastrophic losses in crisis
- Always have stop loss (-10%)
- Size conservatively (<10% of portfolio)
- **Don't fight fundamentals**

### Example 4: Brexit Vote - GBP Basis Arbitrage (2016) - Winner

**Setup:**

- **Date:** June 2016
- **Event:** Brexit referendum
- **Hedge fund:** Macro strategy

**Pre-referendum (June 20, 2016):**

**GBP/USD:**
- Spot: 1.4800
- GBP 1-month rate: 0.50%
- USD 1-month rate: 0.50%
- **No rate differential**

**Fair forward:**
$$
F = 1.48 \times \frac{1.005^{1/12}}{1.005^{1/12}} = 1.4800
$$

**Actual 1-month forward: 1.4650**

**GBP at 1.5% discount despite equal rates!**

**Basis:**
$$
\text{Basis} = \frac{1.4650 - 1.48}{1.48} \times 12 = -2.43\%
$$

**-243 bp basis! Massive deviation from CIP.**

**Why?**

**Market pricing Brexit risk:**
- Polls showing "Leave" gaining
- If Brexit: GBP crashes
- Forward market pricing this in

**But spot market not moving (yet):**
- Spot: 1.4800 (stable)
- Forward: 1.4650 (discounting)

**Arbitrage opportunity:**

**If "Remain" wins:**
- Spot stable at 1.48
- Forward will converge to 1.48
- **Profit: 1.5% from forward convergence**

**If "Leave" wins:**
- Spot crashes (say, to 1.35)
- Forward already at 1.4650
- **Loss: Depends on spot move**

**Trade (June 21, day before vote):**

**Covered arbitrage on "Remain" outcome:**

1. Borrow GBP: £100M at 0.50%
2. Convert to USD at spot: £100M × 1.48 = $148M
3. Invest USD at 0.50%: $148M
4. Buy GBP forward: $148M / 1.4650 = £101.02M

**If "Remain" wins (expected):**
- Forward converges to spot (1.48)
- Profit from basis collapse

**Risk: "Leave" wins, basis was justified**

**June 23: Referendum Day**

**Polls during day: "Remain" ahead**

**Basis tightened:**
- Forward: 1.4650 → 1.4720
- Basis: -243 bp → -130 bp
- **Profit: 113 bp × £100M = £1.13M**

**Marked to market gain!**

**June 24: "Leave" Wins - The Shock**

**Unexpected outcome:**
- "Leave" wins 52% to 48%

**GBP crashes:**
- Spot: 1.4800 → 1.3200 (-10.8%)
- Forward: 1.4720 → 1.3000

**Position P/L:**

| Component | P/L |
|-----------|-----|
| GBP borrowed | -£100M × 1.005^(3/365) = -£100.04M |
| USD invested | $148M × 1.005^(3/365) = $148.12M |
| Forward (sell USD, buy GBP) | $148.12M / 1.3000 = £113.94M |
| **Net GBP** | £113.94M - £100.04M = **£13.90M** |

**Profit: £13.90M (+13.9%!)**

**Wait, made money on "Leave" despite betting on "Remain"?**

**Yes! Because:**

1. **Borrowed GBP, invested USD** (long USD, short GBP)
2. **GBP crashed** → Good for short GBP position!
3. **Forward locked in at 1.4650** → Bought GBP back at 1.30
4. **Profit from GBP depreciation > cost of basis**

**This wasn't a bet on "Remain", it was:**
- Long USD (via covered position)
- If Remain: Profit from basis
- If Leave: Profit from GBP crash
- **Win-win! (almost)**

**Actual profit breakdown:**

**Scenario A (Remain):**
- Basis converges: +1.5%
- FX neutral: 0%
- **Total: +1.5%**

**Scenario B (Leave, actual):**
- GBP crashes: +10.8%
- Basis widens but already short GBP: +2.5%
- **Total: +13.3%**

**The trade was actually:**
- Short GBP via covered position
- Benefited from any GBP weakness
- **Optionality from basis**

**Why it worked:**

1. **Asymmetric payoff:**
   - Remain: Small profit (+1.5%)
   - Leave: Large profit (+13%)

2. **Covered position protected downside:**
   - No naked FX risk
   - Locked in with forward

3. **Market mispriced probability:**
   - Forward priced ~30% Leave probability
   - Actual: 52% Leave
   - **Forward underpriced Leave risk**

4. **Executed with discipline:**
   - Entered day before vote
   - Size appropriate (not overleveraged)
   - Closed after result (didn't overstay)

**Lesson: Basis trades around events can create asymmetric payoffs.**

---

## Best Case Scenario

### The Perfect Basis Trade - USD Shortage (March 2020 COVID)

**Setup:**

- **Date:** February 2020 (pre-COVID crisis)
- **Hedge Fund:** Global macro
- **Capital:** $1B
- **Strategy:** Anticipate USD funding stress

**Market environment:**

**EUR/USD cross-currency basis:**
- 3-month basis: -20 bp (normal)
- 1-year basis: -25 bp (normal)

**Analysis:**

**Vulnerability identified:**
- European banks: $1.5T USD assets
- Funded via FX swaps (structural demand)
- Any stress → USD shortage → Basis widens

**COVID emerging (Feb 2020):**
- Italy lockdowns
- China manufacturing halted
- **Market complacency: "It's contained"**

**Fund's view:**
- Global crisis likely
- USD funding stress will explode
- **Basis will widen dramatically**

**The perfect trade (February 25, 2020):**

**Short EUR/USD basis across curve:**

1. **3-month:** $200M short at -20 bp
2. **6-month:** $200M short at -22 bp
3. **1-year:** $300M short at -25 bp
4. **Total: $700M notional**

**Structure:**
- Lend USD (receive USD interest)
- Borrow EUR (pay EUR interest + basis)
- Profit when basis widens

**Capital allocated: $100M** (margin/liquidity buffer)

**Expected profit:**
- Normal scenario: Basis widens 10-20 bp
- Crisis scenario: Basis widens 50-100 bp
- **Target: 30-40 bp widening**

**Evolution - The Perfect Storm:**

**March 1-15: COVID accelerates**

**Market panic:**
- Italy full lockdown
- US cases rising
- Equity crash: -20%

**USD funding stress begins:**

| Date | 3M Basis | 6M Basis | 1Y Basis | MTM P/L |
|------|----------|----------|----------|---------|
| Feb 25 | -20 bp | -22 bp | -25 bp | $0 |
| Mar 5 | -35 bp | -40 bp | -45 bp | +$16.5M |
| Mar 10 | -55 bp | -65 bp | -75 bp | +$38.0M |
| Mar 15 | -85 bp | -100 bp | -115 bp | +$70.5M |

**Two weeks: +$70.5M (+70.5% return!)**

**March 16-23: Peak Crisis**

**USD shortage extreme:**
- Fed cuts to zero (March 15)
- Global panic for USD
- Banks can't fund FX swaps

**Basis explosion:**

| Date | 3M Basis | 6M Basis | 1Y Basis | MTM P/L |
|------|----------|----------|----------|---------|
| Mar 18 | -120 bp | -140 bp | -150 bp | +$98.5M |
| Mar 20 | -150 bp | -175 bp | -180 bp | +$122.0M |
| Mar 23 | -165 bp (!!) | -185 bp | -190 bp | +$133.5M |

**Peak basis: -165 bp on 3-month! (vs. -20 bp entry)**

**Widening: 145 bp in 4 weeks**

**Total P/L: +$133.5M on $100M capital = +133.5%!**

**Decision points:**

**March 23: Take profits on 50%**

**Basis at extremes:**
- 3M: -165 bp (99th percentile)
- Fed announcing USD swap lines (liquidity coming)
- **Close half position: $350M notional**

**Locked in: $66.75M**

**March 24-31: Fed Intervention**

**Fed announces:**
- Unlimited USD swap lines with ECB, BoJ, etc.
- Massive liquidity injection

**Basis begins reverting:**

| Date | 3M Basis | P/L (remaining $350M) |
|------|----------|----------------------|
| Mar 24 | -165 bp | $0 (mark) |
| Mar 26 | -120 bp | -$15.75M |
| Mar 30 | -80 bp | -$29.75M |

**Gave back profits on remaining position!**

**Decision: Close remaining 50% at -80 bp**

**Final P/L:**

| Component | Notional | Entry | Exit | Profit |
|-----------|----------|-------|------|--------|
| First 50% | $350M | -20 to -25 bp | -165 to -185 bp | +$66.75M |
| Second 50% | $350M | -20 to -25 bp | -80 to -100 bp | +$26.25M |
| **Total** | **$700M** | | | **+$93.0M** |

**Return on $100M capital: 93% in 5 weeks**

**Attribution:**

| Phase | Duration | Widening | Profit |
|-------|----------|----------|--------|
| Early crisis (Mar 1-15) | 2 weeks | 60-90 bp | +$70.5M |
| Peak panic (Mar 16-23) | 1 week | 85-165 bp | +$63.0M |
| Fed intervention (Mar 24-31) | 1 week | Reversal -85 bp | -$29.75M |
| **Net** | **5 weeks** | | **+$93.0M** |

**Why this was best case:**

1. **Perfect timing:**
   - Entered before crisis (Feb 25)
   - At normal basis levels (-20 bp)
   - **vs. entering during crisis at -80 bp (late)**

2. **Fundamental catalyst:**
   - COVID created USD shortage
   - Structural (European banks need USD)
   - **Predictable stress pattern**

3. **Unprecedented widening:**
   - 145 bp widening (extreme)
   - Historical max: 100 bp
   - **COVID was unique**

4. **Disciplined exit:**
   - Took 50% profit at peak (-165 bp)
   - Closed remaining before full reversal
   - **Locked in 93% instead of 133% → avoiding 40% giveback**

5. **Diversified across tenor:**
   - 3M, 6M, 1Y positions
   - Different sensitivities
   - **Maximized capture**

6. **Size appropriate:**
   - $700M notional on $1B fund (70%)
   - Not over-leveraged
   - Had liquidity to withstand volatility

**Comparison to alternatives:**

| Strategy | Return | Notes |
|----------|--------|-------|
| **Actual (basis trade)** | **+93%** | **Perfect execution** |
| If held 100% to Apr 30 | +45% | Gave back most gains |
| If entered Mar 15 (late) | +30% | Missed early widening |
| If closed Mar 23 (all) | +133% | Lucky timing, unsustainable |
| Cash (no trade) | 0% | Missed opportunity |

**Post-trade analysis:**

**April 2020:**
- Basis: -80 bp → -40 bp (normalized)
- Fed swap lines working
- **If held remaining 50%:**
  - Additional profit: +$14M
  - Total: $107M (not $93M)

**But: Risk of further reversal to -20 bp:**
- Would have lost $21M from -80 bp
- **Taking profit at -80 bp was correct risk management**

**This exemplifies:**
1. Macro analysis (COVID → USD shortage)
2. Structural understanding (European bank USD funding)
3. Early positioning (before market panic)
4. Disciplined profit-taking (50% at peak)
5. Risk management (closed before full reversal)

---

## Worst Case Scenario

### The Basis Convergence Trap - SNB Floor Removal (2015)

**Setup:**

- **Date:** December 2014
- **Fund:** European macro hedge fund
- **Capital:** €500M
- **Strategy:** Arbitrage EUR/CHF basis

**Market environment:**

**EUR/CHF:**
- Spot: 1.2000 (floor maintained by SNB since 2011)
- CHF rate: -0.75% (negative!)
- EUR rate: 0.05%
- Differential: +0.80%

**EUR/CHF 1-year basis:**
- Current: -35 bp
- Fair value (CIP): ~0 bp (with rate differential)
- **Basis seems wide, mean reversion opportunity**

**Fund's thesis (wrong):**

"SNB will maintain floor. EUR/CHF basis will normalize to -10 bp. Easy 25 bp profit!"

**The fatal trade (December 2014):**

**Long EUR/CHF basis (bet on tightening):**

1. **Structure:**
   - Borrow USD: $1B
   - Invest CHF (via EUR/CHF cross)
   - Basis position: Long at -35 bp
   - **Betting basis narrows to -10 bp**

2. **Notional:** $1B (200% of fund capital!)

3. **Expected profit:**
   - Basis tightens: -35 → -10 bp = 25 bp
   - Profit: $1B × 0.25% = **$2.5M** (0.5% return)

**"Risk-free" arbitrage mindset:**
- "SNB won't remove floor"
- "Basis must normalize"
- **Overconfidence**

**Evolution - The Disaster:**

**January 1-14, 2015: Building position**

**Adding to position:**
- Basis: -35 bp → -40 bp (widened!)
- Fund: "Oversold, add more"
- **Increased notional: $1B → $1.5B (300% of capital!)**

**Fatal mistake: Averaging down in structural trade**

**January 15, 2015: SNB Removes Floor**

**9:30 AM CET: SNB Announcement**

"Swiss National Bank discontinues minimum exchange rate and lowers interest rate to -0.75%"

**Market reaction:**

**EUR/CHF collapse:**
- Spot: 1.2000 → 0.9800 in 10 minutes (-18.3%)
- Then: 0.9800 → 0.8500 in 30 minutes (another -13.3%)
- **Total: 1.2000 → 0.8500 = -29.2%**

**CHF appreciated 34.5%!**

**Basis explosion:**

| Time | Spot | 1Y Basis | Position MTM |
|------|------|----------|--------------|
| 9:25 AM | 1.2000 | -40 bp | $0 (mark) |
| 9:31 AM | 1.0500 | -150 bp | -$55M |
| 9:45 AM | 0.9200 | -280 bp | -$180M |
| 10:15 AM | 0.8500 | -400 bp | -$312M |

**Basis widened from -40 bp → -400 bp!**

**Loss: 360 bp widening × $1.5B = -$312M**

**But that's not all...**

**FX loss on unhedged component:**

**Problem: Basis position has embedded CHF exposure!**

When spot moves dramatically, even "hedged" basis positions have leakage.

**Effective FX exposure: ~20% of notional** (due to maturity mismatch, imperfect hedge)

**FX loss: 0.20 × $1.5B × 29.2% = -$87.6M**

**Total loss: -$312M (basis) - $87.6M (FX) = -$399.6M**

**On €500M fund: -80% in one day!**

**Forced liquidation:**

**Banks called margins:**
- Prime brokers demanding $300M collateral
- Fund only had €200M liquid
- **Forced to close at worst levels**

**Closing trades (10:30 AM):**
- Basis: -400 bp (peak)
- Spot: 0.8500 (worst)
- **Locked in -$399.6M loss**

**Aftermath:**

**January 16-30, 2015:**
- Spot: 0.8500 → 1.0200 (recovered 20%)
- Basis: -400 bp → -150 bp (tightened 250 bp)

**If held (impossible due to margin calls):**
- Would have recovered $200M+ of losses
- Final loss: -$200M (not -$400M)

**But couldn't hold:**
- Forced liquidation
- Fund shut down
- **Total wipeout**

**What went catastrophically wrong:**

1. **Assumed floor permanent:**
   - "SNB committed to 1.20 floor"
   - Ignored SNB's QE costs (€500B+ accumulated)
   - **Central banks can change policy overnight**

2. **Ignored structural basis:**
   - Basis was wide (-35 bp) for a reason
   - CHF negative rates create funding issues
   - **Basis reflected real frictions, not mispricing**

3. **Overleveraged (300% of capital!):**
   - $1.5B position on €500M fund
   - One standard deviation basis move (50 bp) = -€37.5M loss
   - **Five sigma event (360 bp) = wipeout**

4. **Averaged down:**
   - Basis: -35 → -40 bp, added $500M
   - Turned manageable into catastrophic
   - **Never average down on structural positions**

5. **No stop loss:**
   - "This is arbitrage, no stop needed"
   - **Wrong! Basis can blow out 10x in crisis**

6. **Ignored event risk:**
   - SNB meeting January 15 (known!)
   - Should have reduced before meeting
   - **Kept full position into event**

7. **Misunderstood "risk-free":**
   - CIP arbitrage is only risk-free when:
     - Unlimited balance sheet
     - No funding constraints
     - Perfect liquidity
   - **None of these held!**

8. **Hidden FX exposure:**
   - Thought position was FX-neutral
   - Maturity mismatches created exposure
   - **Spot gap = additional loss**

**Comparison to cautious alternative:**

**What if conservative approach:**

**December 2014 (alternative):**
1. Position: $200M (40% of fund, not 300%)
2. Stop loss: Basis widens to -60 bp (exit)
3. Event risk: Close 50% before SNB meeting

**January 15 outcome (alternative):**

**Pre-meeting (Jan 14):**
- Closed 50%: $100M notional remaining
- Basis: -40 bp

**Post-announcement:**
- Basis: -400 bp
- Loss on remaining: 360 bp × $100M = -$36M
- FX loss: -$5.8M
- **Total: -$41.8M**

**On €500M fund: -8.4%** (not -80%!)

**Painful but survivable.**

**The lesson:**

**"Risk-free arbitrage" is a myth in practice:**
- CIP can violate by 100+ bp
- Event risk can blow up overnight
- Leverage magnifies disasters
- **Always have stop loss, even on "arbitrage"**

**Post-2015, basis trades require:**
1. Conservative size (<50% of capital)
2. Stop loss (basis widens 100 bp)
3. Event risk management (reduce before known events)
4. Understanding of structural vs. temporary deviations
5. Liquidity buffer (for margin calls)

**SNB 2015 wiped out dozens of funds. Don't be one of them.**

---

## What to Remember

### Core Concept

**Interest rate parity links spot, forward, and interest rates:**

$$
F = S \times \frac{1 + r_d}{1 + r_f}
$$

- Forward premium = Interest differential (when CIP holds)
- Covered IRP: No FX risk (hedged with forward)
- Uncovered IRP: FX risk (bet on spot movement)
- Basis = deviation from CIP
- Post-2008: Basis persistently non-zero (funding, regulation)

### Forward Pricing

**Fair forward rate:**

$$
F_{\text{fair}} = S \times \frac{1 + r_d \times T}{1 + r_f \times T}
$$

**Example:**
- Spot: 1.10 USD/EUR
- USD rate: 5%, EUR rate: 3%
- 1-year forward: $1.10 \times \frac{1.05}{1.03} = 1.1214$

**EUR at premium (forward > spot) because USD rates higher.**

### Cross-Currency Basis

$$
\text{Basis} = \frac{F - S}{S} \times \frac{1}{T} - (r_d - r_f)
$$

**Typical post-2008:**
- EUR/USD: -20 to -50 bp
- JPY/USD: -30 to -80 bp
- GBP/USD: -10 to -40 bp

**Negative basis = Foreign currency "cheap" in FX swap market**

### Entry Checklist - Basis Trade

**For long basis (bet on tightening):**

1. **Basis characteristics:**
   - [ ] Current basis at wide end of range (< 20th percentile)
   - [ ] Historical mean reversion pattern
   - [ ] No structural reason for wideness

2. **Catalyst:**
   - [ ] Quarter/year-end passing (basis normalizes after)
   - [ ] Central bank action (swap lines reduce stress)
   - [ ] Risk-on environment (basis tightens)

3. **Position:**
   - [ ] Size <50% of capital
   - [ ] Stop loss: Basis widens 50 bp
   - [ ] Duration appropriate (3M better than 1Y)

4. **Risk management:**
   - [ ] No major events during holding period
   - [ ] Liquidity buffer (30%+ cash)
   - [ ] Correlation to other positions <0.5

### Entry Checklist - Carry Trade

**For uncovered carry (high risk):**

1. **Interest differential:**
   - [ ] Positive carry >3% annually
   - [ ] Stable or rising differential

2. **FX view:**
   - [ ] High-rate currency not overvalued (PPP)
   - [ ] Central bank supporting currency
   - [ ] No crisis risk (fundamentals solid)

3. **Position:**
   - [ ] Size <10% of portfolio
   - [ ] Stop loss: -5% FX move
   - [ ] Correlation to other carry trades <0.6

4. **Environment:**
   - [ ] Risk-on regime (VIX < 20)
   - [ ] No upcoming elections/events
   - [ ] Liquidity normal

### Common Strategies Summary

| Strategy | Risk | Expected Return | Sharpe | Holding Period |
|----------|------|-----------------|--------|----------------|
| Covered arbitrage | Low | 1-3% | 1.5-2.0 | Days-weeks |
| Basis mean reversion | Medium | 3-8% | 0.8-1.2 | Weeks-months |
| Uncovered carry | High | 5-15% | 0.4-0.7 | Months-years |
| Event-driven basis | Medium | 5-20% | 1.0-1.5 | Weeks |

### Exit Rules

**Basis trades:**

1. **Profit targets:**
   - Basis narrows to 50th percentile: Close 50%
   - Basis at 25th percentile: Close all

2. **Stop losses:**
   - Basis widens 50 bp from entry: Exit
   - Approaching quarter/year-end: Reduce 50%
   - Major event announced: Close

**Carry trades:**

1. **Profit targets:**
   - Gain >15%: Take profits
   - FX appreciates >10%: Reduce 50%

2. **Stop losses:**
   - FX loss >5%: Exit
   - VIX >30: Reduce 50%
   - Carry differential narrows 50%: Exit

### Position Sizing

**Conservative:**

$$
\text{Position Size} = \min\left(50\% \text{ of capital}, \frac{10\%}{\text{Basis Vol}}\right)
$$

**Example:**
- Capital: $100M
- Basis volatility: 20 bp (quarterly)
- Max: min($50M, $100M × 10% / 20bp) = min($50M, $50M) = **$50M**

**For carry trades:**

$$
\text{Position Size} = \min\left(10\% \text{ of capital}, \frac{3\%}{\text{FX Vol}}\right)
$$

### Common Mistakes

1. **Assuming CIP always holds**
   - Post-2008: Persistent deviations
   - Funding, regulation create frictions

2. **Overleveraging basis trades**
   - "Risk-free" myth
   - SNB 2015 proved otherwise

3. **Ignoring event risk**
   - Central bank meetings
   - Elections, geopolitical events

4. **Averaging down**
   - Basis widens, adding more
   - Turns manageable into catastrophic

5. **No stop loss on "arbitrage"**
   - Basis can blow out 10x
   - Always have exit plan

6. **Carry trades in crisis**
   - Ignoring VIX, risk-off signals
   - "It will recover" mentality

7. **Confusing correlation**
   - EUR/USD and JPY/USD basis correlated 0.7
   - Not diversified!

8. **Quarter/year-end neglect**
   - Basis spikes predictably
   - Reduce before, re-enter after

### Performance Expectations

**Basis trades (conservative):**

| Scenario | Probability | Return | Notes |
|----------|-------------|--------|-------|
| Mean reversion | 50% | +3-6% | Basis narrows as expected |
| No change | 30% | -1% | Carry cost |
| Moderate widening | 15% | -5% | Stop loss hit |
| Extreme widening | 5% | -15% | Crisis |

**Expected return: 1-3% per trade**
**Sharpe: 0.8-1.2**

**Uncovered carry (risky):**

| Scenario | Probability | Return |
|----------|-------------|--------|
| Calm market | 60% | +8-12% |
| Moderate volatility | 25% | -3% |
| Crisis/crash | 15% | -20 to -40% |

**Expected return: 3-6% annually**
**Sharpe: 0.4-0.7**
**Max drawdown: 25-40%**

### Your Learning Path

**Phase 1 (Months 1-3): Fundamentals**
- Study CIP, UIP relationships
- Calculate forward rates
- Track basis daily (EUR/USD, JPY/USD)
- Paper trade

**Phase 2 (Months 4-6): Analysis**
- Build basis monitoring dashboard
- Identify mean reversion patterns
- Understand seasonal effects (quarter/year-end)
- Small real positions

**Phase 3 (Months 7-12): Active trading**
- Trade basis around events
- Experiment with carry (small size)
- Monitor cross-currency correlations
- Build track record

**Phase 4 (Year 2+): Systematic**
- Automated basis signals
- Portfolio of FX trades
- Risk management framework
- Scale capital

### Final Wisdom

> "Interest rate parity is the physics of FX markets—the fundamental law that governs exchange rates. Before 2008, it held with iron discipline. Post-crisis, it breaks persistently, creating opportunities for those with funding and balance sheet. The EUR/USD basis has been negative for 15 years, widening to -100 bp during COVID. Patient arbitrageurs collect 20-50 bp annually by lending USD and borrowing EUR. But the SNB 2015 proved: no arbitrage is truly risk-free. Central banks can change policy overnight, basis can blow out 10x, and 'hedged' positions can wipe you out if overleveraged. Respect the basis. Size conservatively. Always have a stop loss. The market can stay irrational longer than you can stay solvent—and more irrational than you can imagine."

**Keys to success:**

1. **Understand structural vs. temporary basis** (EUR/USD negative is structural post-2008)
2. **Trade mean reversion, not absolute levels** (basis widens → opportunity)
3. **Respect event risk** (SNB, Brexit, central bank meetings)
4. **Size conservatively** (<50% of capital for basis, <10% for carry)
5. **Always have stop loss** (even on "risk-free arbitrage")
6. **Reduce into quarter/year-end** (basis spikes predictably)
7. **Monitor correlations** (EUR/USD and JPY/USD move together)
8. **Cash is king** (30%+ buffer for margin calls)

**Most critical rule:**

$$
\text{Basis volatility} \times \text{Leverage} = \text{Potential wipeout}
$$

Even 10 bp daily basis vol × 20x leverage = 200 bp ($2M) daily swing on $100M position. One bad week with 100 bp widening = $10M loss. SNB 2015 showed 360 bp widening in 10 minutes. At 300% leverage, fund lost 80% of capital instantly. **Never leverage arbitrage >2x.** The basis market is treacherous. Trade it wisely. 🎯📊
