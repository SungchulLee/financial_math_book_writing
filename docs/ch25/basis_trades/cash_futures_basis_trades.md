# Cash-Futures Basis Trades


**Cash-futures basis trades** exploit the spread between the price of a cash bond and its corresponding futures contract, capturing mispricings driven by funding costs, delivery options, and supply-demand imbalances.

---

## The Core Insight


**The fundamental idea:**

- Futures price should equal cash price plus carry cost
- Basis = Futures Price - Cash Price (adjusted)
- Basis reflects funding costs, delivery options, and technical factors
- Rich basis = Futures expensive (short futures, long cash)
- Cheap basis = Futures cheap (long futures, short cash)
- Convergence at delivery generates profit

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/basis_trading.png?raw=true" alt="basis_trading" width="700">
</p>
**Figure 1:** Time series of Treasury futures basis showing mean reversion around theoretical carry, with deviations creating trading opportunities when basis becomes rich (positive) or cheap (negative).

**You're essentially asking: "How do I profit from the cash-futures relationship when it deviates from fair value?"**

---

## What Is the Basis?


### 1. Basic Definition


**The basis:**

$$
\text{Basis} = \text{Futures Price} - (\text{Cash Price} \times \text{Conversion Factor})
$$

**For Treasury futures:**
- Futures are standardized (notional 6% coupon)
- Actual deliverable bonds have different coupons
- Conversion factor adjusts for coupon differences

**Example:**
- 10Y Treasury futures: 110-00 (110.00)
- Cash 10Y bond: 108-16 (108.50)
- Conversion factor: 0.9850

**Adjusted cash price:**

$$
108.50 \times 0.9850 = 106.87
$$

**Basis:**

$$
110.00 - 106.87 = 3.13 \text{ (313 ticks)}
$$

### 2. Theoretical Basis (Cost of Carry)


**No-arbitrage condition:**

$$
\text{Futures Price} = \text{Cash Price} + \text{Carry Cost}
$$

**Carry cost:**

$$
\text{Carry} = (\text{Repo Rate} - \text{Coupon Income}) \times \frac{\text{Days to Delivery}}{360}
$$

**Example:**
- Cash bond: $100
- Coupon: 4% annually
- Repo rate: 2% annually
- Days to delivery: 90

**Theoretical carry:**

$$
\text{Carry} = (0.02 - 0.04) \times 100 \times \frac{90}{360} = -0.50
$$

**Theoretical futures price:**

$$
100 + (-0.50) = 99.50
$$

**Negative carry = Futures should trade below cash (backwardation)**

### 3. Gross Basis vs Net Basis


**Gross basis:**

$$
\text{Gross Basis} = \text{Futures} - \text{Conversion Factor} \times \text{Cash}
$$

**Net basis:**

$$
\text{Net Basis} = \text{Gross Basis} - \text{Theoretical Carry}
$$

**Net basis is the mispricing (trading opportunity)**

**Example:**
- Gross basis: 3.13
- Theoretical carry: 2.50
- **Net basis: 3.13 - 2.50 = 0.63 (rich)**

**Rich net basis → Short futures, long cash**

### 4. Conversion Factor


**Why conversion factors exist:**

Futures contract specifies 6% coupon bond:
- Actual deliverable bonds have various coupons (2-5%)
- Need adjustment to make delivery fair
- Higher coupon bonds worth more → CF > 1
- Lower coupon bonds worth less → CF < 1

**Calculation (approximate):**

$$
\text{CF} = \frac{\text{PV of Bond at 6\% Yield}}{\text{Par Value}}
$$

**Example:**
- 10Y bond, 4% coupon
- At 6% yield: PV = 85.28
- **CF = 85.28 / 100 = 0.8528**

### 5. Cheapest-to-Deliver (CTD)


**Multiple delivery options:**

Treasury futures allow delivery of any bond in a basket:
- 10Y futures: Bonds with 6.5-10 years remaining
- 30Y futures: Bonds with ≥ 15 years remaining

**Seller chooses which to deliver (profit maximization)**

**CTD bond:**

$$
\text{CTD} = \arg\min_i \left(\text{Cash Price}_i \times \text{CF}_i - \text{Futures Price}\right)
$$

**The bond with lowest adjusted cost to deliver**

**Example (10Y futures at 110):**
- Bond A: Cash = 108, CF = 0.98 → Cost = 108 × 0.98 = 105.84
- Bond B: Cash = 110, CF = 1.00 → Cost = 110 × 1.00 = 110.00
- **Bond A is CTD (lower cost to deliver)**

### 6. Implied Repo Rate


**Alternative measure of richness:**

$$
\text{IRR} = \frac{\text{Futures Price} \times \text{CF} - \text{Cash Price} + \text{Coupon}}{\text{Cash Price}} \times \frac{360}{\text{Days}}
$$

**Interpretation:**
- IRR = Repo rate that makes basis trade break-even
- IRR > Actual repo rate → Futures cheap (long futures)
- IRR < Actual repo rate → Futures rich (short futures)

**Example:**
- Futures: 110
- Cash: 108
- CF: 0.98
- Coupon accrued: 0.50
- Days: 90
- Actual repo: 2.0%

**IRR:**

$$
\text{IRR} = \frac{110 \times 0.98 - 108 + 0.50}{108} \times \frac{360}{90} = 0.18\% \text{ annually}
$$

**IRR (0.18%) < Repo (2.0%) → Futures rich, short basis**

### 7. Delivery Option Value


**Short futures holder has options:**

**Quality option:**
- Choose which bond to deliver (CTD selection)
- Value when yield curve moves (CTD switches)

**Timing option:**
- Choose when to deliver during delivery month
- Deliver on favorable days

**Wild card option:**
- Futures settle 2 PM, bonds trade until 4 PM
- If bond rallies 2-4 PM, don't deliver today
- Wait for better opportunity

**Embedded option value:**

$$
\text{Net Basis} = \text{Theoretical Carry} + \text{Option Value}
$$

**Typical option value: 2-10 ticks (depending on volatility)**

---

## Basis Trading Strategies


**How to profit from basis:**

### 1. Long Basis Trade


**Setup: Net basis cheap (futures underpriced)**

**Position:**
- Long futures
- Short cash bond
- Finance short via repo

**P&L at delivery:**

$$
\text{P\&L} = (\text{Futures}_T - \text{Futures}_0) - (\text{Cash}_T - \text{Cash}_0) + \text{Carry}
$$

**Example:**
- Futures: 110.00
- Cash: 108.50
- CF: 0.98
- Theoretical carry: -0.50 (negative carry)
- Net basis: -0.25 (cheap)

**At delivery (futures converge to cash):**
- Futures → 106.87 (108.50 × 0.98)
- P&L: (106.87 - 110.00) = -3.13 (futures loss)
- Cash: 106.87 - 108.50 = +1.63 (short profit)
- Carry: -0.50 (cost)
- **Net: -3.13 + 1.63 + 0.50 = -1.00**

**Wait, this loses! Need to recalculate...**

**Correct calculation:**
- Initial net basis: -0.25 (futures underpriced)
- Final net basis: 0 (convergence)
- **Profit: 0 - (-0.25) = 0.25**

### 2. Short Basis Trade


**Setup: Net basis rich (futures overpriced)**

**Position:**
- Short futures
- Long cash bond
- Finance via repo (borrow cash, post bond)

**P&L:**

$$
\text{P\&L} = -(\text{Futures}_T - \text{Futures}_0) + (\text{Cash}_T - \text{Cash}_0) - \text{Carry}
$$

**Example:**
- Net basis: +0.50 (rich)

**At delivery:**
- Net basis converges to 0
- **Profit: 0.50 - 0 = 0.50**

### 3. Basis Curve Trade


**Exploit basis across maturities:**

**Setup:**
- Near contract basis: +0.30 (rich)
- Far contract basis: -0.20 (cheap)
- Spread: 0.50

**Position:**
- Short near contract (rich)
- Long far contract (cheap)
- Dollar-neutral

**Profit if spread narrows:**
- Spread → 0.20 (narrowed by 0.30)
- **Gain: 0.30**

### 4. CTD Switch Trade


**Bet on CTD bond changing:**

**Setup:**
- Current CTD: Bond A
- If rates rise 50 bps, CTD switches to Bond B

**Position:**
- Long Bond B
- Short Bond A
- Short futures (hedge)

**If CTD switches:**
- Bond B becomes more valuable (now deliverable)
- **Profit from relative value shift**

### 5. Delivery Month Calendar


**Basis converges during delivery month:**

**Position:**
- 10 days before delivery: Net basis = 0.40
- Short futures, long cash
- Hold through delivery

**Convergence:**
- Net basis → 0.10 (option value only)
- **Profit: 0.30**

### 6. Volatility-Driven Basis


**Option value increases with volatility:**

**Setup:**
- Volatility low, net basis = 0.15 (option value suppressed)
- Expect volatility spike (Fed announcement)

**Position:**
- Short futures, long cash (short net basis)
- Collect cheap option value

**If volatility spikes:**
- Net basis widens to 0.35 (option value rises)
- **Lose on basis widening (chose wrong direction!)**

**Actually, want to be LONG basis (long futures, short cash) when vol low:**
- Buy cheap optionality
- Profit when vol spikes and basis widens

### 7. Funding Advantage Trade


**Exploit special repo rates:**

**Setup:**
- CTD bond goes "special" (tight repo rate)
- GC repo: 2.5%
- Special repo (CTD): 1.0%

**Position:**
- Long CTD bond
- Finance at 1.0% (special rate)
- Short futures
- Implied repo rate: 1.8%

**Positive carry:**
- Earn: 1.8% (implied)
- Pay: 1.0% (special)
- **Net: +0.8% annually (carry profit)**

---

## Mathematical Framework


### 1. Basis Decomposition


**Net basis components:**

$$
\text{Net Basis} = \text{Financing Value} + \text{Delivery Option Value} + \text{Supply-Demand}
$$

**Financing value:**

$$
\text{Financing} = (\text{GC Rate} - \text{Actual Repo Rate}) \times \frac{\text{Days}}{360}
$$

**Delivery option value:**

$$
\text{Option Value} \approx k \times \sigma \times \sqrt{T}
$$

Where $\sigma$ = Yield volatility, $T$ = Time to delivery

### 2. Convergence P&L


**For short basis trade:**

$$
\text{P\&L} = (\text{Net Basis}_0 - \text{Net Basis}_T) \times \text{Notional} / 100
$$

**Example:**
- Notional: $1M
- Initial net basis: 0.60
- Final net basis: 0.10

**Profit:**

$$
(0.60 - 0.10) \times \frac{\$1M}{100} = \$5,000
$$

### 3. Implied Repo Rate Formula


**Exact IRR:**

$$
\text{IRR} = \frac{(\text{Futures Price} / 100) \times \text{CF} - \text{Cash Price} / 100 + \text{Accrued Interest}}{\text{Cash Price} / 100 + \text{Accrued Interest}} \times \frac{360}{\text{Days to Delivery}}
$$

### 4. Conversion Factor Duration


**Price sensitivity of adjusted cash:**

$$
\text{DV01}_{\text{adjusted}} = \text{DV01}_{\text{cash}} \times \text{CF}
$$

**Hedge ratio:**

$$
\text{Futures Contracts} = \frac{\text{Cash DV01}}{\text{Futures DV01} \times \text{CF}}
$$

### 5. CTD Selection Algorithm


**Minimize delivered cost:**

$$
\text{CTD} = \arg\min_i \left[\text{Cash Price}_i \times \text{CF}_i - \text{Futures Price}\right]
$$

**Alternatively, maximize IRR:**

$$
\text{CTD} = \arg\max_i \text{IRR}_i
$$

### 6. Option Value Estimation


**Delivery option value (approximate):**

$$
\text{Option Value} \approx 0.5 \times \text{Gamma} \times \sigma^2 \times T
$$

Where:
- Gamma = Convexity of CTD bond
- $\sigma$ = Daily yield volatility
- $T$ = Days to delivery

**Typical value: 5-15 ticks**

### 7. Calendar Spread Basis


**Price differential between contracts:**

$$
\text{Calendar Spread} = \text{Basis}_{\text{far}} - \text{Basis}_{\text{near}}
$$

**Expected change:**

$$
\Delta \text{Spread} = (\text{Carry}_{\text{far}} - \text{Carry}_{\text{near}}) - (\text{Option}_{\text{far}} - \text{Option}_{\text{near}})
$$

---

## Common Mistakes


**Pitfalls to avoid:**

### 1. Ignoring Conversion Factor


**Mistake:** Compare futures to cash directly

**Why it fails:** Misestimate basis

**Example:**
- Futures: 110.00
- Cash: 108.00
- Think basis = 2.00

**Actual (with CF = 0.98):**
- Adjusted cash: 108.00 × 0.98 = 105.84
- **Actual basis: 4.16 (double what you thought!)**

**Fix:** Always adjust cash by conversion factor

### 2. Wrong Carry Calculation


**Mistake:** Ignore coupon income

**Why it fails:** Overestimate carry cost

**Example:**
- Repo rate: 3%
- Forget coupon: 4%
- Think positive carry

**Actual:**
- Net carry: 3% - 4% = -1% (negative!)
- **Futures should trade below cash**

**Fix:** Carry = Repo rate - Coupon income

### 3. Neglecting Delivery Options


**Mistake:** Trade net basis at zero

**Why it fails:** Option value always positive

**Example:**
- Net basis = 0.05
- Think "close to fair value"
- Short basis (sell futures, buy cash)

**But:**
- Option value ≈ 0.08
- Net basis should be 0.08
- Currently cheap, not rich!
- **Wrong direction, lose money**

**Fix:** Net basis should equal option value at minimum

### 4. Misidentifying CTD


**Mistake:** Trade wrong bond

**Why it fails:** Not actually cheapest-to-deliver

**Example:**
- Trade basis on Bond A
- Bond B is actually CTD
- Basis on Bond A doesn't converge
- **Bond A - futures spread widens, lose money**

**Fix:** Calculate IRR for all deliverable bonds, trade the CTD

### 5. Ignoring Repo Specials


**Mistake:** Assume GC repo rate

**Why it fails:** CTD often goes special

**Example:**
- Calculate basis using GC rate (2.5%)
- CTD bond special at 1.0%
- Can't finance at GC
- **Actual carry 1.5% worse than expected**

**Fix:** Check actual repo rate for CTD bond

### 6. Poor Timing


**Mistake:** Enter trade far from delivery

**Why it fails:** Basis can widen before converging

**Example:**
- 60 days to delivery, net basis = 0.40
- Short basis (sell futures, buy cash)
- Volatility spikes, basis widens to 0.80
- **Mark-to-market loss, margin call**

**Fix:** Enter closer to delivery (< 30 days), less time for adverse moves

### 7. Leverage Mismatch


**Mistake:** Unhedged basis trade

**Why it fails:** Directional exposure

**Example:**
- Short $10M futures (think basis trade)
- Forget to buy $10M cash bonds
- Just short futures naked
- Rates fall, futures rally
- **Large directional loss**

**Fix:** Match positions: long futures = short cash (dollar-neutral)

### 8. Neglecting Accrued Interest


**Mistake:** Don't account for accrued

**Why it fails:** Basis calculation wrong

**Example:**
- Cash bond trades "clean" (without accrued)
- Accrued interest: 1.50
- Ignore accrued in calculation
- **Basis misstated by 1.50**

**Fix:** Use "dirty" price (clean + accrued)

---

## Risk Management Rules


### 1. Position Sizing


**Maximum basis notional:**

$$
\text{Max Notional} = \frac{\text{Risk Capital}}{\text{Basis Volatility} \times \text{DV01}}
$$

**Example:**
- Risk capital: $100,000
- Basis volatility: 0.30 (30 ticks)
- DV01: $100 per tick

**Max notional:**

$$
\frac{\$100,000}{0.30 \times \$100} = \$3.3M
$$

**Rule of thumb:** Max 5% of portfolio in basis trades

### 2. Hedge Ratio


**Dollar-neutral hedge:**

$$
\text{Cash Amount} = \text{Futures Notional} \times \text{CF}
$$

**DV01-neutral hedge:**

$$
\text{Cash DV01} = \text{Futures DV01} \times \text{CF} \times \text{Hedge Ratio}
$$

**Typical hedge ratio: 0.95-1.05 (slight under/over-hedge)**

### 3. Entry Thresholds


**Minimum net basis for trade:**

- **Rich basis (short):** Net basis > Option value + 0.10
- **Cheap basis (long):** Net basis < Option value - 0.10

**Example:**
- Option value: 0.08
- Enter short basis if net basis > 0.18
- Enter long basis if net basis < -0.02

### 4. Stop-Loss Rules


**Basis widening stop:**

- **Short basis:** Exit if net basis widens by 0.20
- **Long basis:** Exit if net basis cheapens by 0.20

**Time stop:**
- Exit at 10 days before delivery (avoid squeeze risk)

### 5. Monitoring Frequency


**Daily:**
- Net basis calculation
- Repo rate for CTD
- Implied repo rate
- Mark-to-market P&L

**Weekly:**
- CTD switch probability
- Option value estimate
- Yield volatility

### 6. Delivery Month Management


**Last 30 days:**
- Tighten stops (0.10 basis move)
- Monitor delivery notices
- Prepare for physical settlement or cash-out

**Last 10 days:**
- Most convergence happens here
- High risk period (squeezes possible)
- Reduce position if basis not converging

### 7. Diversification


**Spread risk across:**
- Multiple contracts (10Y, 30Y)
- Multiple delivery cycles (March, June, September)
- Long and short basis positions

**Don't concentrate:**
- All positions in one contract
- Same direction (all short basis)

---

## Real-World Examples


### 1. Classic Convergence Trade (2019)


**Setup:**
- 10Y futures (TYZ19) December delivery
- CTD: 2.625% 11/15/2029
- 30 days before delivery
- Net basis: 0.45 (rich)
- Option value estimate: 0.12

**Trade:**
- Short 100 futures contracts @ 130-16
- Long $10M CTD bond @ 101-24
- Finance at GC repo: 1.8%

**Outcome:**
- Over 30 days, net basis converged to 0.15
- Profit: (0.45 - 0.15) × $10M / 100 = $30,000
- **Annualized return: 30% on capital**

**Lesson:** Classic basis convergence trade works in normal markets

### 2. Squeeze Risk (March 2020)


**Setup:**
- COVID crisis, dealer balance sheets full
- Short basis positions crowded
- CTD bond scarce

**Event:**
- CTD goes "super special" (repo at -1%)
- Net basis widens from 0.30 to 0.80 (option value + scarcity)
- Short basis traders lose

**Outcome:**
- Some funds lost 20-30% on basis trades
- Forced to cover at wide basis
- **Lesson:** Delivery month squeezes are real

### 3. CTD Switch Trade (2015)


**Setup:**
- 30Y futures, yields expected to rise
- Current CTD: 3.0% 08/15/2042 (duration 20)
- Alternative CTD: 4.0% 02/15/2036 (duration 18)
- If yields rise 50 bps, CTD switches to shorter duration bond

**Trade:**
- Long 4.0% bond
- Short 3.0% bond
- Short futures (hedge)

**Outcome:**
- Yields rose 40 bps
- CTD switched
- 4.0% bond outperformed 3.0% by 1.50
- **Profit: 1.50 on spread, hedged directionality**

**Lesson:** CTD switches create relative value opportunities

### 4. Funding Advantage (2018)


**Setup:**
- 10Y CTD goes special
- GC repo: 2.2%
- CTD repo: 0.8% (140 bps special)

**Trade:**
- Long $50M CTD bond @ 98-16
- Finance at 0.8% special rate
- Short 50 futures @ 120-00
- Implied repo: 1.9%

**Carry:**
- Earn: 1.9% (implied repo)
- Pay: 0.8% (special)
- **Positive carry: 1.1% annualized**

**Held 6 months:**
- Carry profit: $50M × 1.1% × 0.5 = $275,000
- Basis also converged slightly: +$50,000
- **Total: $325,000 (1.3% return in 6 months)**

**Lesson:** Specials create carry opportunities

---

## Practical Steps


### 1. Identify Opportunity


**Daily analysis:**

1. **Calculate net basis for all contracts:**
   - Download futures prices
   - Download CTD bond prices
   - Compute IRR, net basis
   - Compare to historical

2. **Screen for extremes:**
   - Net basis > 0.25 (potentially rich)
   - Net basis < 0 (potentially cheap)
   - IRR vs. repo spread > 50 bps

3. **Check option value:**
   - Estimate from volatility
   - Subtract from net basis
   - Determine true mispricing

### 2. Trade Execution


**For short basis trade:**

1. **Day 1 (simultaneously):**
   - Short futures: Sell TY contracts
   - Long cash: Buy CTD bond (dirty price)
   - Arrange repo financing

2. **Confirm hedge:**
   - Cash notional = Futures notional × CF
   - Check DV01 match

3. **Monitor:**
   - Daily MTM
   - Repo rate (check for specials)
   - Net basis convergence

### 3. Position Management


**Daily tasks:**

- Update net basis calculation
- Check accrued interest changes
- Monitor repo rate for CTD
- Compute implied repo rate
- MTM P&L

**Weekly tasks:**

- Recalculate CTD (in case switch)
- Review option value estimate
- Check delivery month calendar
- Adjust hedge ratio if needed

### 4. Exit Strategy


**Planned exits:**

- **Target:** Net basis converges to 0.15 (option value)
- **Stop:** Net basis moves 0.20 against you
- **Time:** Exit 10 days before first delivery day

**Example:**
- Entered at net basis 0.45 (short)
- Target: 0.15 (profit = 0.30)
- Stop: 0.65 (loss = 0.20)

### 5. Delivery Management


**If holding into delivery month:**

1. **Monitor delivery notices:**
   - First notice day
   - Last trading day
   - Last delivery day

2. **Decide:**
   - Cash out futures position (offset)
   - Accept delivery (if long futures)
   - Make delivery (if short futures)

3. **Settle:**
   - Physical delivery (bond transfer)
   - Invoice price calculation
   - Final P&L accounting

---

## Final Wisdom


> "Cash-futures basis trading is the ultimate 'convergence trade' - buying cheap and selling rich with a known endpoint (delivery). It's mathematically precise, empirically stable, and historically profitable, but it's not free money. The three killers are: (1) funding stress when the CTD goes special and your carry explodes negative, (2) delivery month squeezes when dealers reduce balance sheets and net basis widens instead of converging, and (3) misidentifying the CTD and trading a bond that doesn't converge. Done right with proper CTD analysis, conservative sizing, and disciplined exits before the last 10 days, basis trades generate 5-15% annually with low volatility. The key is patience, precision, and paranoia about delivery month dynamics."

**Key to success:**

- **Calculate accurately:** Always use conversion factor, include accrued interest, subtract theoretical carry
- **Identify CTD:** Calculate IRR for all deliverable bonds, trade only the cheapest-to-deliver
- **Monitor funding:** Check repo rate daily, CTD bonds often go special (destroys positive carry)
- **Size conservatively:** Max 5% portfolio, basis can widen before converging (interim MTM pain)
- **Time entry:** Enter < 60 days to delivery, most convergence happens last 30 days
- **Exit early:** Don't hold past 10 days before first delivery day (squeeze risk too high)
- **Hedge properly:** Dollar-neutral (Cash notional = Futures × CF), check DV01 match
- **Remember:** This is a financing trade, not a directional bet - stay neutral to rates
