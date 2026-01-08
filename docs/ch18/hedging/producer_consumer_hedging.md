# Producer-Consumer Hedging

**Producer-consumer hedging** is an options and futures strategy where businesses lock in future prices to eliminate price uncertainty, protecting profit margins against adverse price movements while maintaining core business operations.

---

## The Core Insight

**The fundamental idea:**

- Producers sell commodities/products in the future (farmers, miners, oil companies)
- Consumers buy commodities/inputs in the future (airlines, manufacturers, food companies)
- Both face price uncertainty that threatens profit margins
- Options and futures allow locking in prices today for future transactions
- Trade profit opportunity for certainty and stability
- Focus on business risk management, not speculation

**The key equation:**

$$
\text{Hedged Profit} = \text{Operating Profit} + \text{Hedge P\&L}
$$

Where hedge P&L offsets price movements:

$$
\text{Producer: } \text{Hedge P\&L} = -\Delta S \quad (\text{gain when prices fall})
$$

$$
\text{Consumer: } \text{Hedge P\&L} = +\Delta S \quad (\text{gain when prices rise})
$$

**You're essentially betting: "I want stable, predictable profits. I'll give up upside to eliminate downside."**

---

## What Is Producer-Consumer Hedging?

**Before implementing hedging strategies, understand the business need:**

### 1. Producer Hedging

**Definition:** A producer hedges by selling futures or buying puts to lock in a minimum selling price for their product, protecting against price declines.

**When producers hedge:**

- They produce commodities (wheat, oil, gold, etc.)
- They sell output months in the future
- They fear prices will DROP before they sell
- They lock in today's price (or floor price)
- They sacrifice upside if prices RISE
- They gain stability and predictable cash flows

**Example - Wheat Farmer:**

- September: Plant wheat, will harvest in June
- Wheat currently $7/bushel
- Expects to harvest 100,000 bushels
- Revenue at risk: 100,000 × $7 = $700,000
- Fears: drought elsewhere → bumper crop → prices crash to $5

**Hedge:**

- Sell 20 futures contracts (5,000 bushels each)
- Lock in $7/bushel selling price
- Cost: Minimal (margin requirement)
- Result: Revenue guaranteed at $700,000 regardless of June price

**At harvest (June):**

- If wheat at $5 → Lose $2/bushel on crop BUT gain $2/bushel on futures → Net $7
- If wheat at $9 → Gain $2/bushel on crop BUT lose $2/bushel on futures → Net $7
- **Price locked, profit stable, business predictable**

### 2. Consumer Hedging

**Definition:** A consumer hedges by buying futures or buying calls to lock in a maximum purchase price for their inputs, protecting against price increases.

**When consumers hedge:**

- They need commodities as inputs (jet fuel, copper, wheat)
- They buy inputs months in the future  
- They fear prices will RISE before they buy
- They lock in today's price (or ceiling price)
- They sacrifice savings if prices DROP
- They gain cost certainty and budget predictability

**Example - Airline:**

- January: Planning summer schedule
- Jet fuel currently $2.50/gallon
- Need 100 million gallons for summer
- Cost at risk: 100M × $2.50 = $250M
- Fears: Middle East conflict → oil spike → fuel at $4/gallon

**Hedge:**

- Buy crude oil futures (jet fuel proxy)
- Or buy call options on crude
- Lock in ~$2.50/gallon effective price
- Cost: Premium if using options, margin if futures

**In summer:**

- If fuel at $4 → Pay $4/gallon BUT gain $1.50/gallon on futures → Net $2.50
- If fuel at $2 → Pay $2/gallon BUT lose $0.50/gallon on futures → Net $2.50
- **Cost locked, budget protected, ticket prices stable**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/producer_consumer_hedging.png?raw=true" alt="producer_consumer_hedging" width="700">
</p>
**Figure 1:** Producer vs. consumer hedging showing how each party locks in prices: producers eliminate downside by selling futures/buying puts, consumers eliminate upside risk by buying futures/calls, both achieve profit stability at the cost of foregoing favorable price movements.

---

## Economic

**Beyond the basic mechanics, understanding the REAL economics of hedging:**

### 1. Hedging as Insurance Premium

**The deep insight:**

Hedging is economically equivalent to **buying insurance against price volatility**. When a business hedges, they are essentially:

1. **Paying an insurance premium** (option cost or futures opportunity cost)
2. **Transferring price risk** to speculators willing to bear it
3. **Locking in profit margins** regardless of market moves
4. **Stabilizing cash flows** for operational planning

**Formal decomposition:**

$$
\underbrace{\text{Unhedged Business}}_{\text{High variance}} = \underbrace{\text{Operating Profit}}_{\text{Known}} + \underbrace{\text{Price Exposure}}_{\text{Unknown}}
$$

$$
\underbrace{\text{Hedged Business}}_{\text{Low variance}} = \underbrace{\text{Operating Profit}}_{\text{Known}} + \underbrace{\text{Hedge P\&L}}_{\text{Offsets price moves}} - \underbrace{\text{Insurance Cost}}_{\text{Premium/opportunity cost}}
$$

**Why this matters:**

**Unhedged producer (farmer):**

- Wheat at $7 → Revenue $700k
- Wheat at $5 → Revenue $500k  
- Wheat at $9 → Revenue $900k
- **Variance: $400k range, cannot plan**
- Cannot commit to equipment purchases
- Cannot secure bank loans (unpredictable cash flow)
- Might go bankrupt in bad year

**Hedged producer:**

- Revenue: $680k regardless of price (after hedge costs)
- Can plan capex investments
- Can secure financing (banks love stability)
- Can sign fixed-price supply contracts
- **No bankruptcy risk from price moves**

**The "insurance premium" is the $20k difference:**

$$
\text{Insurance Cost} = \text{Unhedged Expected} - \text{Hedged Certain}
$$

$$
\$20k = \$700k - \$680k
$$

**This is the cost of certainty, worth it for business stability.**

### 2. The Producer's Economic Dilemma

**Consider a coffee producer (Colombia):**

**Scenario: September, harvest in March**

- Coffee currently $1.50/lb
- Will harvest 1 million lbs
- Revenue at risk: $1.5M
- Production cost: $1.00/lb (all-in)
- Unhedged profit: $0.50/lb = $500k

**The dilemma:**

| Coffee Price in March | Revenue | Profit | Business Impact |
|----------------------|---------|--------|-----------------|
| $0.80 | $800k | -$200k | **Bankruptcy** |
| $1.20 | $1.2M | $200k | Struggling |
| $1.50 | $1.5M | $500k | Target profit |
| $2.00 | $2.0M | $1.0M | Windfall |

**Unhedged: Massive variance, existential risk**

**Hedged (sell futures at $1.50):**

- Revenue: $1.5M guaranteed
- Profit: $500k guaranteed
- Can plan expansion, hire workers, secure loans
- **Business survives bad years**

**The economic trade:**

- Give up windfall ($2.00 scenario)
- Eliminate bankruptcy ($0.80 scenario)
- **Rational business decision for survival**

### 3. The Consumer's Economic Dilemma

**Consider an airline (Southwest):**

**Scenario: January, summer flying season ahead**

- Jet fuel currently $2.50/gallon
- Need 100M gallons for summer
- Ticket prices already set at $300/flight
- Fuel cost per flight: 200 gallons × $2.50 = $500
- Target profit: $50/flight

**The dilemma:**

| Fuel Price in Summer | Cost/Flight | Profit/Flight | Business Impact |
|---------------------|-------------|---------------|-----------------|
| $4.00 | $800 | -$250 | **Massive losses** |
| $3.00 | $600 | -$50 | Unprofitable |
| $2.50 | $500 | $50 | Target |
| $2.00 | $400 | $150 | Great margin |

**Unhedged: Can't raise ticket prices mid-season, massive risk**

**Hedged (buy calls at $2.50 strike, pay $0.10 premium):**

- Effective max cost: $2.60/gallon
- Profit: $40/flight minimum (if fuel spikes)
- Can still benefit if fuel drops to $2.00
- **Business protected from bankruptcy**

**The insurance premium:**

$$
\text{Premium cost} = 100M \text{ gal} \times \$0.10 = \$10M
$$

**This $10M buys protection against $150M loss (fuel to $4)**

**ROI on insurance:**

$$
\text{Insurance Value} = \frac{\text{Protected Loss}}{\text{Premium Paid}} = \frac{\$150M}{\$10M} = 15:1
$$

**Rational decision for survival**

### 4. Put-Call Parity in Hedging Context

**The fundamental relationship applies to hedging:**

$$
\text{Long Stock} + \text{Long Put} = \text{Long Call} + \text{PV(Strike)}
$$

**Rearranging for hedging strategies:**

**Producer hedging equivalence:**

$$
\underbrace{\text{Own Asset}}_{\text{Wheat inventory}} + \underbrace{\text{Long Put}}_{\text{Price floor}} = \underbrace{\text{Synthetic Future}}_{\text{Locked price}}
$$

**Consumer hedging equivalence:**

$$
\underbrace{\text{Short Asset}}_{\text{Need to buy}} + \underbrace{\text{Long Call}}_{\text{Price cap}} = \underbrace{\text{Synthetic Future}}_{\text{Locked price}}
$$

**Practical implication:**

A producer can hedge with:
1. Sell futures (simplest)
2. Buy puts (retains upside, costs premium)
3. Collar (sell calls to finance puts, partial upside)

A consumer can hedge with:
1. Buy futures (simplest)
2. Buy calls (retains downside savings, costs premium)
3. Collar (sell puts to finance calls, partial downside)

**All achieve same goal: price certainty**

### 5. Why Businesses MUST Hedge

**The survival equation:**

$$
P(\text{Bankruptcy}) = P(\text{Price Move} > \text{Equity Buffer})
$$

**Unhedged:**

- Coffee producer with $500k equity
- If price drops to $0.80, loses $700k
- **Bankruptcy: $700k loss > $500k equity**

**Hedged:**

- Same producer, hedged at $1.50
- Price drops to $0.80: Hedge gains $700k, offsets loss
- **Survives: Net impact = $0**

**The asymmetry:**

| Scenario | Unhedged | Hedged |
|----------|----------|--------|
| Good prices ($2.00) | $1M profit (amazing!) | $500k profit (ok) |
| Bad prices ($0.80) | **Bankrupt** (dead) | $500k profit (alive) |

**One bad year kills unhedged business. Hedged business survives.**

**This is why CFOs hedge: Survival > Speculation**

### 6. The Speculator's Role

**Who takes the other side of hedges?**

**Speculators (hedge funds, commodity traders):**

- Don't produce or consume the commodity
- Take price risk for profit
- Provide liquidity to hedgers
- Get paid risk premium

**Economic function:**

$$
\text{Hedger pays risk premium} \rightarrow \text{Speculator accepts risk}
$$

**Example:**

- Farmer sells wheat futures at $7
- Speculator buys at $7
- If wheat → $5: Farmer wins, speculator loses $2
- If wheat → $9: Farmer neutral, speculator wins $2
- **Speculator bets on prices, farmer ensures stability**

**Society benefits:**

- Farmers get price certainty → Plant more crops
- Food supply more stable
- Speculators provide capital → Market liquidity
- **Risk transferred from those who can't bear it to those who can**

**This is the economic purpose of derivatives markets**

---

## Key Terminology

**Hedge:**

- Position that offsets business exposure
- Reduces or eliminates price risk
- Not meant to profit (meant to stabilize)
- Core business risk management tool

**Basis Risk:**

- When hedge doesn't perfectly match exposure
- Example: Hedge crude oil but need jet fuel (correlation ≠ 1)
- Example: Hedge June futures but sell in July (time mismatch)
- Residual risk remaining after hedge

**Notional Exposure:**

- Dollar amount of business risk
- Example: 100k bushels × $7 = $700k notional
- Determines hedge size
- Must match production/consumption volume

**Hedge Ratio:**

- Proportion of exposure to hedge
- 100% hedge = Full protection, no upside
- 50% hedge = Partial protection, some upside
- Dynamic hedging = Adjust ratio over time

**Collar:**

- Buy put (downside protection)
- Sell call (finance put with call premium)
- Net cost: Zero or low
- Trade: Limited upside for limited downside

**Carrying Costs:**

- Storage costs
- Insurance
- Interest (cost of capital)
- Spoilage/degradation
- Affects futures pricing

**Backwardation:**

- Near futures > Far futures
- Implies shortage (supply tight)
- Producers can sell near-term at premium
- Common in commodities

**Contango:**

- Far futures > Near futures
- Implies surplus (storage costs)
- Consumers can buy near-term cheaper
- Normal commodity curve state

---

## Mathematical Foundation

### 1. The Perfect Hedge Equation

**For a producer with quantity $Q$ and hedge ratio $h$:**

$$
\text{Total Profit} = Q \cdot (S_T - C) + h \cdot Q \cdot (F_0 - S_T)
$$

Where:
- $Q$ = Quantity (bushels, barrels, pounds)
- $S_T$ = Spot price at time $T$
- $C$ = Production cost per unit
- $F_0$ = Futures price locked in today
- $h$ = Hedge ratio (0 to 1)

**Full hedge ($h = 1$):**

$$
\text{Profit} = Q \cdot (S_T - C) + Q \cdot (F_0 - S_T) = Q \cdot (F_0 - C)
$$

**Result: Profit independent of $S_T$ (price locked!)**

**Example:**

- $Q = 100,000$ bushels
- $C = \$5/bushel$ (production cost)
- $F_0 = \$7/bushel$ (futures price)
- $h = 1$ (full hedge)

**Scenarios:**

| $S_T$ | Crop Revenue | Futures P&L | Total | Profit |
|-------|-------------|-------------|-------|--------|
| $5 | $500k | +$200k | $700k | $200k |
| $6 | $600k | +$100k | $700k | $200k |
| $7 | $700k | $0 | $700k | $200k |
| $8 | $800k | -$100k | $700k | $200k |
| $9 | $900k | -$200k | $700k | $200k |

**Profit locked at $Q \cdot (F_0 - C) = 100k \times (\$7 - \$5) = \$200k$**

### 2. Optimal Hedge Ratio

**The variance-minimizing hedge ratio:**

$$
h^* = \rho \cdot \frac{\sigma_S}{\sigma_F}
$$

Where:
- $\rho$ = Correlation between spot and futures
- $\sigma_S$ = Standard deviation of spot price changes
- $\sigma_F$ = Standard deviation of futures price changes

**For perfect correlation ($\rho = 1$) and equal volatilities:**

$$
h^* = 1 \quad (\text{full hedge optimal})
$$

**For imperfect correlation (basis risk):**

$$
h^* < 1 \quad (\text{partial hedge optimal})
$$

**Example:**

- Jet fuel spot volatility: $\sigma_S = 20\%$
- Crude oil futures volatility: $\sigma_F = 25\%$
- Correlation: $\rho = 0.85$

$$
h^* = 0.85 \times \frac{0.20}{0.25} = 0.85 \times 0.80 = 0.68
$$

**Optimal hedge: 68% of exposure (not 100%)**

**Why?** Jet fuel ≠ crude perfectly, so over-hedging adds risk

### 3. Options vs. Futures for Hedging

**Producer choice:**

**Option 1: Sell Futures**

$$
\text{Payoff} = F_0 - S_T \quad (\text{linear, locks price})
$$

- Cost: Minimal (margin)
- Benefit: Perfect hedge, full protection
- Drawback: No upside if prices rise

**Option 2: Buy Put**

$$
\text{Payoff} = \max(K - S_T, 0) - P \quad (\text{floor, keeps upside})
$$

- Cost: Premium $P$
- Benefit: Keeps upside if prices rise above $K + P$
- Drawback: Expensive

**Break-even comparison:**

**Futures:** Locked at $F_0 = \$7$

**Put:** Strike $K = \$7$, Premium $P = \$0.50$

| $S_T$ | Futures Net | Put Net | Better Choice |
|-------|------------|---------|---------------|
| $5 | $7.00 | $6.50 | Futures |
| $6 | $7.00 | $6.50 | Futures |
| $7 | $7.00 | $6.50 | Futures |
| $7.50 | $7.00 | $7.00 | Equal |
| $8 | $7.00 | $7.50 | Put |
| $9 | $7.00 | $8.50 | Put |

**Put better if $S_T > \$7.50$ (upside benefit > premium)**

### 4. Consumer Hedge Equation

**For a consumer needing quantity $Q$ at future time $T$:**

$$
\text{Total Cost} = Q \cdot S_T - h \cdot Q \cdot (S_T - F_0)
$$

**Full hedge ($h = 1$):**

$$
\text{Cost} = Q \cdot S_T - Q \cdot (S_T - F_0) = Q \cdot F_0
$$

**Cost locked at $Q \cdot F_0$ regardless of $S_T$**

**Example - Airline:**

- $Q = 100M$ gallons
- $F_0 = \$2.50/gallon$
- $h = 1$

**Scenarios:**

| $S_T$ | Spot Cost | Futures Gain | Net Cost | Per Gallon |
|-------|-----------|--------------|----------|-----------|
| $2.00 | $200M | -$50M | $250M | $2.50 |
| $2.50 | $250M | $0 | $250M | $2.50 |
| $3.00 | $300M | +$50M | $250M | $2.50 |
| $4.00 | $400M | +$150M | $250M | $2.50 |

**Cost locked, budget certain, operations stable**

### 5. Hedge Effectiveness

**Measuring hedge quality:**

$$
\text{Effectiveness} = 1 - \frac{\text{Var}(\text{Hedged Profit})}{\text{Var}(\text{Unhedged Profit})}
$$

**Perfect hedge:** Effectiveness = 1 (100%, zero variance)

**No hedge:** Effectiveness = 0 (original variance)

**Example:**

- Unhedged profit variance: $\sigma^2_U = \$10M^2$
- Hedged profit variance: $\sigma^2_H = \$1M^2$

$$
\text{Effectiveness} = 1 - \frac{1}{10} = 0.90 = 90\%
$$

**Interpretation: Hedge eliminated 90% of profit variance**

### 6. Expected Profit with Risk Premium

**In reality, hedgers pay risk premium to speculators:**

$$
\mathbb{E}[S_T] = F_0 + \text{Risk Premium}
$$

**For producer (short futures):**

$$
\mathbb{E}[\text{Profit}] = Q \cdot (F_0 - C) - Q \cdot \text{Risk Premium}
$$

**Example:**

- Expected spot: $\mathbb{E}[S_T] = \$7.20$
- Futures: $F_0 = \$7.00$
- Risk premium: $\$0.20$

**Unhedged expected profit:**

$$
Q \cdot (\mathbb{E}[S_T] - C) = 100k \times (7.20 - 5) = \$220k
$$

**Hedged certain profit:**

$$
Q \cdot (F_0 - C) = 100k \times (7 - 5) = \$200k
$$

**Cost of hedge: $\$20k$ (risk premium paid)**

**But: Eliminates bankruptcy risk, worth the cost**

---

## Step-by-Step Setup

### 1. Phase 1

**1. Identify Price Risk:**

**Producer checklist:**

- What commodity do you produce?
- What quantity per period?
- What's your production cost?
- When do you sell (timing)?
- What's your breakeven price?

**Example - Corn farmer:**

- Commodity: Corn
- Quantity: 500,000 bushels/year
- Cost: $3.50/bushel (seed, labor, equipment, land)
- Timing: Harvest October, sell November
- Breakeven: $3.50/bushel minimum

**Consumer checklist:**

- What commodity do you need?
- What quantity per period?
- What's your budget constraint?
- When do you buy (timing)?
- What's your maximum acceptable price?

**Example - Breakfast cereal manufacturer:**

- Commodity: Corn
- Quantity: 2 million bushels/year
- Budget: $10M allocated ($5/bushel)
- Timing: Purchase quarterly
- Max price: $6/bushel (above this, unprofitable)

**2. Quantify Exposure:**

$$
\text{Notional Exposure} = \text{Quantity} \times \text{Current Price}
$$

**Corn farmer:**

$$
500,000 \times \$4.50 = \$2.25M \text{ at risk}
$$

**Cereal maker:**

$$
2,000,000 \times \$4.50 = \$9M \text{ at risk}
$$

**3. Determine Risk Tolerance:**

**Questions to answer:**

- How much price variance can business absorb?
- What price level causes distress?
- What's the equity buffer?
- Is survival or profit optimization the goal?

**Example - Farmer with $300k equity:**

- Current profit: $500k (at $4.50 corn)
- At $3.00 corn: Profit = -$250k (loss)
- **Bankruptcy if corn below $2.90** (equity wiped out)
- **Must hedge to survive**

### 2. Phase 2

**Decision tree:**

**For producers:**

```
Need certainty? → Sell Futures (lock price)
Want upside potential? → Buy Puts (floor price, pay premium)
Minimize cost? → Collar (put + sell call, near-zero cost)
```

**For consumers:**

```
Need certainty? → Buy Futures (lock price)
Want downside savings? → Buy Calls (cap price, pay premium)
Minimize cost? → Collar (call + sell put, near-zero cost)
```

**Factors to consider:**

| Factor | Futures | Options (Put/Call) | Collar |
|--------|---------|-------------------|--------|
| Cost | Minimal (margin) | Premium ($0.30-$0.70) | Low/zero |
| Certainty | Complete | Floor/cap only | Band |
| Upside/savings | None | Full | Partial |
| Complexity | Low | Medium | High |

**Most common choice: Futures for simplicity**

### 3. Phase 3

**Determine contracts needed:**

**Futures contract specification:**

- Corn: 5,000 bushels per contract
- Crude oil: 1,000 barrels per contract
- Gold: 100 troy ounces per contract

**Formula:**

$$
\text{Contracts} = \frac{\text{Exposure Quantity}}{\text{Contract Size}} \times h
$$

**Example - Corn farmer (500k bushels, full hedge):**

$$
\text{Contracts} = \frac{500,000}{5,000} \times 1 = 100 \text{ contracts}
$$

**Example - Airline (100M gallons jet fuel, 90% hedge):**

Jet fuel ≈ 0.85 correlation with crude oil

$$
\text{Crude contracts} = \frac{100M \text{ gal}}{42 \text{ gal/barrel}} \times \frac{1}{1,000 \text{ bbl/contract}} \times 0.90
$$

$$
= \frac{100,000,000}{42,000} \times 0.90 \approx 2,143 \text{ contracts}
$$

**Adjust for:**

- Basis risk (correlation < 1)
- Timing mismatch
- Rolling contracts
- Margin requirements

### 4. Phase 4

**Timing considerations:**

**Producer (sell futures/buy puts):**

**Bad timing:**

- Wait until harvest → Market moved against you
- All at once → Timing risk concentrated

**Good timing:**

- Start 6-12 months before harvest
- Layer in 25% every 2 months
- Average entry prices
- Reduce timing risk

**Example - Wheat farmer (February, harvest June):**

- February: Hedge 25% (25k bushels) at $7.20
- March: Hedge 25% (25k bushels) at $6.90
- April: Hedge 25% (25k bushels) at $7.10
- May: Hedge 25% (25k bushels) at $7.00
- **Average: $7.05, reduced timing risk**

**Consumer (buy futures/calls):**

**Strategy:**

- Hedge quarterly needs
- Roll forward as consumed
- Layer in over time
- Budget certainty maintained

**Execution steps:**

1. **Open brokerage account:**
   - Commodity broker (not stock broker)
   - Margin account required
   - Understand margin calls

2. **Place order:**
   - Specify contract (Dec 2024 Corn)
   - Specify quantity (100 contracts)
   - Limit order (don't use market)
   - Confirm execution

3. **Post margin:**
   - Initial margin: ~5-10% of notional
   - Maintenance margin: Must maintain
   - Mark-to-market daily
   - **Must have cash for margin calls**

4. **Document hedge:**
   - Why hedging (business purpose)
   - Quantity matched to exposure
   - Accounting treatment (hedge accounting)
   - Tax implications

### 5. Phase 5

**Daily monitoring:**

✅ Mark-to-market P&L
✅ Margin balance (avoid margin call)
✅ Basis tracking (convergence?)
✅ Production/consumption on schedule?

**Adjustment triggers:**

**Production change:**

- Drought reduces crop yield 30%
- **Action:** Reduce hedge by 30% (sell back contracts)

**Consumption change:**

- Summer travel demand up 20%
- **Action:** Increase fuel hedge by 20%

**Price moves dramatically:**

- Locked corn at $7, now $10
- Losing $3/bushel on futures
- **Action:** Nothing if business cash flow supports it
- This is the hedge WORKING (protecting business)

**Rolling contracts:**

**As expiration approaches:**

- Close near-month position
- Open next-month position
- Manage roll costs
- Maintain continuous hedge

**Example - June corn to December corn:**

- May: Close June futures
- May: Open December futures
- Cost: Spread between June and December
- Maintains hedge through year

### 6. Complete Example

**Background:**

- Producer: Colombian coffee farm
- Production: 2 million lbs/year
- Cost: $1.00/lb (all-in)
- Harvest: March 2025
- Current price: $1.50/lb (September 2024)

**Step 1: Assess exposure:**

- Notional: 2M × $1.50 = $3M
- Expected profit: 2M × ($1.50 - $1.00) = $1M
- Bankruptcy if price < $0.90 (can't cover costs + debt service)
- **Must hedge to ensure survival**

**Step 2: Choose instrument:**

- Option A: Sell futures at $1.50
- Option B: Buy $1.40 puts for $0.08
- Option C: Collar ($1.40 put, sell $1.65 call)

**Choice: Collar (minimal cost, retains some upside)**

**Step 3: Calculate contracts:**

- Coffee futures: 37,500 lbs per contract
- Contracts needed: 2,000,000 / 37,500 = 53.3 ≈ 53 contracts

**Step 4: Execute (September 2024):**

- Buy 53 March 2025 $1.40 puts @ $0.08 = $4,240 per contract × 53 = $225k
- Sell 53 March 2025 $1.65 calls @ $0.07 = $3,710 per contract × 53 = $197k
- **Net cost: $28k (very low)**

**Step 5: Scenarios at harvest (March 2025):**

| Coffee Price | Crop Value | Put P&L | Call P&L | Net | $/lb |
|-------------|-----------|---------|----------|-----|------|
| $0.80 | $1.6M | +$1.2M | $0 | $2.77M | $1.39 |
| $1.00 | $2.0M | +$800k | $0 | $2.77M | $1.39 |
| $1.40 | $2.8M | $0 | $0 | $2.77M | $1.39 |
| $1.65 | $3.3M | $0 | -$500k | $2.77M | $1.39 |
| $2.00 | $4.0M | $0 | -$1.3M | $2.67M | $1.34 |

**Result:**

- Price floor: $1.39/lb (protected downside)
- Price cap: $1.64/lb (gave up extreme upside)
- **Business survives all scenarios, profit stable $770k-$870k**

---

## Greeks Analysis (Options Hedging)

### 1. Delta

**What it means:**

$$
\Delta = \frac{\partial V}{\partial S}
$$

**In hedging context:** How much hedge value changes per $1 commodity move.

**For producers using puts:**

- Put delta: -0.40 (OTM), -0.50 (ATM), -0.70 (ITM)
- Negative delta = Gains when commodity drops
- Should match business exposure (positive delta in commodity)

**Example:**

- Own 100k bushels corn (delta = +100k)
- Buy 100k ATM puts (delta = -50k)
- **Net delta: +50k (50% hedged)**

**For consumers using calls:**

- Call delta: +0.40 (OTM), +0.50 (ATM), +0.70 (ITM)
- Positive delta = Gains when commodity rises
- Should match business exposure (negative delta in need)

**Monitoring:**

$$
\text{Hedge Ratio} = \frac{|\text{Hedge Delta}|}{|\text{Business Delta}|}
$$

**Target: Close to 1.0 for full hedge**

### 2. Gamma

**What it means:**

$$
\Gamma = \frac{\partial \Delta}{\partial S}
$$

**In hedging:** How hedge effectiveness changes as prices move.

**For hedgers:**

- High gamma (short-dated) = Hedge effectiveness varies
- Low gamma (long-dated) = Hedge effectiveness stable
- **Prefer LOW gamma for predictable protection**

**Example:**

**Short-dated put (30 DTE):**

- At $7: Delta = -0.50
- At $6: Delta = -0.75 (more protection)
- At $8: Delta = -0.25 (less protection)
- **Gamma = 0.10 (high variability)**

**Long-dated put (180 DTE):**

- At $7: Delta = -0.50
- At $6: Delta = -0.55 (slight change)
- At $8: Delta = -0.45 (slight change)
- **Gamma = 0.02 (stable)**

**Hedging preference: Long-dated (stable delta)**

### 3. Theta

**What it means:**

$$
\Theta = \frac{\partial V}{\partial t}
$$

**In hedging:** Daily cost of maintaining option protection.

**This is your insurance premium:**

$$
\text{Daily Insurance Cost} = |\Theta|
$$

**Example - Put protection:**

- Strike: $7.00
- Premium: $0.50
- DTE: 180 days
- **Theta: -$0.50/180 = -$0.0028/day**

**Annual insurance:**

$$
\$0.0028 \times 365 = \$1.02 \text{ per bushel per year}
$$

**For 100k bushels: $102k/year insurance cost**

**Is it worth it?**

- Protects against $2-3 price drops (= $200k-$300k losses)
- **Yes, insurance cheaper than potential loss**

**Theta management:**

- Accept theta as cost of protection
- Don't try to "trade around it"
- Focus on business risk, not option decay
- **Insurance premiums are supposed to decay**

### 4. Vega

**What it means:**

$$
\mathcal{V} = \frac{\partial V}{\partial \sigma}
$$

**In hedging:** How hedge value changes with volatility shifts.

**For put buyers (producers):**

- Vega positive = Benefit from IV increases
- When markets panic, puts become more valuable
- **Bonus protection during crises**

**For call buyers (consumers):**

- Vega positive = Benefit from IV increases
- Crisis → Higher oil prices AND higher hedge values
- **Double protection effect**

**Example:**

- Bought $7 puts for $0.50 (IV = 30%)
- Crisis hits, IV → 50% (+20 points)
- Vega = $0.03
- **Put value: $0.50 → $1.10 (gained $0.60)**

**Practical consideration:**

- Buy options when IV LOW (cheap)
- Avoid buying when IV HIGH (expensive)
- Check IV percentile before hedging

**IV timing:**

| Scenario | IV Level | Hedge Strategy |
|----------|----------|---------------|
| Calm markets | 20-30% | Buy puts/calls (cheap) |
| Normal | 30-40% | Reasonable time |
| Volatile | 40-60% | Consider futures instead |
| Crisis | 60%+ | Options very expensive, use futures |

---

## Real-World Examples

### 1. Pension Duration Cut via Futures

**Background:**

- Farm: 5,000 acres in Kansas
- Crop: Winter wheat
- Timeline: Plant September 2023, harvest June 2024
- Expected yield: 50 bushels/acre = 250,000 bushels
- Production cost: $5.00/bushel

**Market conditions (September 2023):**

- Wheat: $6.80/bushel (December 2024 futures)
- Expected profit: 250k × ($6.80 - $5.00) = $450k

**The risk:**

- Russia/Ukraine war could end → Surplus → Prices crash
- Drought elsewhere could end → Bumper crop → Prices crash
- **Worst case: $4.50/bushel → Loss of $125k**

**Hedge decision:**

- Sell 50 December 2024 wheat futures (5k bushels each)
- Lock in $6.80/bushel
- Cost: $30k initial margin (returned later)

**Timeline:**

| Date | Wheat Price | Futures P&L | Business Status |
|------|------------|------------|-----------------|
| Sep 2023 | $6.80 | $0 | Planted, hedged |
| Dec 2023 | $7.20 | -$100k | Growing well |
| Mar 2024 | $6.50 | +$75k | Good conditions |
| Jun 2024 | $5.80 | +$250k | Harvest time |

**At harvest (June 2024):**

- Spot wheat: $5.80
- Sold crop: 250k × $5.80 = $1.45M
- Futures gain: 250k × ($6.80 - $5.80) = $250k
- **Total revenue: $1.70M = 250k × $6.80 (as planned)**

**Final result:**

- Revenue: $1.70M (locked in)
- Cost: $1.25M
- **Profit: $450k (exactly as projected in September)**

**Why it worked:**

- Locked price when favorable
- Eliminated 9-month uncertainty
- Could plan capex, secure loans
- **Business stability achieved**

**Without hedge:**

- Revenue: $1.45M (at $5.80 spot)
- Cost: $1.25M
- Profit: $200k (44% less than planned)
- **Uncertainty, potential missed loan payment**

### 2. Transition Risk Hedge

**Background:**

- Airline: Regional carrier, 50 aircraft
- Fuel needs: 200 million gallons/year
- Timeline: January 2024 planning for summer
- Tickets already sold at $300/seat

**Market conditions (January 2024):**

- Crude oil: $75/barrel
- Jet fuel: $2.50/gallon (actual purchase price)
- Summer futures (Jul-Sep): $2.60/gallon

**The risk:**

- Middle East tensions → Oil spikes to $120
- Jet fuel could hit $4.00/gallon
- **Disaster: $1.50/gal increase = $300M extra cost → Bankruptcy**

**Hedge decision:**

- Buy crude oil call options (jet fuel proxy)
- Strike: $80/barrel (≈ $2.70/gallon jet fuel)
- Premium: $4/barrel (≈ $0.10/gallon)
- Quantity: 80% of summer needs (160M gallons)

**Cost:**

$$
160M \text{ gal} \times \$0.10 = \$16M \text{ premium paid}
$$

**Timeline:**

| Month | Jet Fuel | Crude Oil | Call Value | Hedge Status |
|-------|----------|-----------|-----------|--------------|
| Jan 2024 | $2.50 | $75 | $4 | Bought calls |
| Apr 2024 | $2.80 | $82 | $10 | ITM, gaining |
| Jun 2024 | $3.40 | $105 | $29 | Deep ITM |
| Aug 2024 | $3.80 | $115 | $39 | Maximum gain |

**Result (Summer 2024):**

**Fuel purchased:**

- 200M gallons × $3.80 = $760M cash outflow

**Call options:**

- 160M gallons hedged
- Crude: $115 (up $40 from strike $80)
- Conversion: $40/barrel ÷ 42 gal/barrel ≈ $0.95/gal
- **Hedge gain: 160M × $0.95 = $152M**

**Net fuel cost:**

$$
\$760M - \$152M = \$608M
$$

$$
\text{Effective price: } \frac{\$608M}{200M} = \$3.04/\text{gal}
$$

**Compare to unhedged:**

- Unhedged: $760M ($3.80/gal)
- Hedged: $608M ($3.04/gal)
- **Savings: $152M (hedge saved the company)**

**Why it worked:**

- Insurance premium ($16M) was tiny vs. protected loss ($152M)
- Business survived oil spike
- Ticket prices remained stable
- **ROI: $152M gain / $16M premium = 9.5x return**

**CEO quote:**

> "Without the hedge, we would have lost $152M in the summer. That's more than our annual profit. The $16M premium saved the company from bankruptcy."

### 3. Portable Alpha with Futures

**Background:**

- Company: Medium gold miner
- Production: 200,000 oz/year
- Cost: $1,200/oz
- Timeline: 2020-2022 forward hedge

**Decision (January 2020):**

- Gold: $1,550/oz
- Management: "Lock in profits, reduce uncertainty"
- Hedge: Sell 3-year forward contracts (600k oz)
- Price locked: $1,550/oz

**What happened:**

| Year | Gold Price | Unhedged Profit | Hedged Profit | Foregone |
|------|-----------|----------------|---------------|----------|
| 2020 | $1,770 | $114M | $70M | -$44M |
| 2021 | $1,800 | $120M | $70M | -$50M |
| 2022 | $1,940 | $148M | $70M | -$78M |

**Result:**

- Hedged profit: $210M over 3 years
- Unhedged profit: $382M over 3 years
- **Cost of hedge: $172M in foregone profits**

**Shareholder anger:**

- Stock underperformed competitors by 40%
- CEO ousted
- Board fired for "over-hedging"

**What went wrong:**

1. **Too much hedged:** 100% of production (should be 30-50%)
2. **Too long:** 3 years out (should be 6-12 months rolling)
3. **No flexibility:** Couldn't benefit from gold bull market
4. **Misaligned incentives:** Management risk-averse, shareholders wanted upside

**Lesson:** Hedging is about survival, not profit elimination. Partial hedges preserve upside.

### 4. Tactical Duration Extension

**Background:**

- Company: Starbucks-style chain
- Coffee needs: 10 million lbs/year
- Timeline: Hedging 2024 needs in January

**Hedge decision:**

- Buy coffee futures (Arabica, Colombian)
- Quantity: 267 contracts (37,500 lbs each)
- Price locked: $1.60/lb

**The problem (basis risk):**

- Hedge: Colombian Arabica futures
- Actual purchases: Mix of Colombian (60%) + Brazilian (40%)
- Correlation: 0.75 (not perfect)

**What happened:**

| Month | Colombian | Brazilian | Blended Cost | Futures | Hedge P&L |
|-------|-----------|-----------|-------------|---------|-----------|
| Jan | $1.60 | $1.30 | $1.48 | $1.60 | $0 |
| Apr | $1.90 | $1.50 | $1.76 | $1.90 | +$0.30 |
| Jul | $2.20 | $1.60 | $1.98 | $2.20 | +$0.60 |
| Oct | $2.10 | $1.90 | $2.02 | $2.10 | +$0.50 |

**Expected:**

- If perfect hedge: Cost locked at $1.48
- Futures gain should offset spot increase

**Actual:**

- Blended cost: $2.02 (up $0.54)
- Futures gain: $0.50 (Colombian up $0.50)
- **Net effective cost: $2.02 - $0.50 = $1.52 (vs. target $1.48)**

**Basis slippage: $0.04/lb × 10M = $400k unexpected cost**

**Why basis risk occurred:**

- Brazilian coffee didn't move with Colombian
- Correlation broke down (different weather, different supply)
- 25% of blend wasn't truly hedged

**Lesson:** Cross-hedging (hedging one commodity with another) has basis risk. Better to hedge exact exposure or accept partial coverage.

### 5. Duration Hedge Failure in Crisis

**Background:**

- Company: Regional gas utility
- Customers: 500,000 homes
- Needs: 50 billion cubic feet/year
- Model: Buy gas monthly, sell to customers

**Challenge:**

- Winter demand spikes (cold = high usage)
- Summer demand low
- Prices volatile ($2-$8 range)
- Must provide stable customer rates

**Hedge strategy (rolling):**

**January 2024:**

- Hedge April-June delivery (spring)
- Buy 3 months of contracts at $2.80/MMBtu

**April 2024:**

- Roll hedge forward
- Hedge July-September (summer) at $2.60

**July 2024:**

- Roll again
- Hedge October-December (winter) at $3.20

**Result over year:**

| Quarter | Spot Price | Hedge Price | Effective Cost | Customer Rate |
|---------|-----------|-------------|----------------|---------------|
| Q1 | $4.50 | $3.00 | $3.00 | $3.50 |
| Q2 | $2.20 | $2.80 | $2.80 | $3.50 |
| Q3 | $2.80 | $2.60 | $2.60 | $3.50 |
| Q4 | $5.20 | $3.20 | $3.20 | $3.50 |

**Average:**

- Spot average: $3.68/MMBtu
- Hedged average: $2.90/MMBtu
- Customer rate: $3.50/MMBtu (stable all year)
- **Profit margin: $0.60/MMBtu locked in**

**Why rolling worked:**

- Captured low summer prices for winter
- Avoided spikes in Q1 and Q4
- Customers got stable rates (happy)
- Utility got stable margins (profitable)
- **Textbook hedging success**

---

## Risk Management

### 1. Position Sizing for Hedgers

**The fundamental principle:**

$$
\text{Hedge Size} = \text{Business Exposure} \times \text{Hedge Ratio}
$$

**Conservative (100% hedge):**

- Hedge entire exposure
- Complete price certainty
- Zero upside/downside
- **Use when:** Survival critical, low equity buffer

**Moderate (50-70% hedge):**

- Hedge majority, keep some exposure
- Partial upside/downside
- Balance stability and opportunity
- **Use when:** Healthy balance sheet, want some flexibility

**Aggressive (30-50% hedge):**

- Hedge minimum, keep significant exposure
- Major upside/downside potential
- Speculative element
- **Use when:** Strong finances, bullish/bearish view

**Example - Oil producer:**

**Scenario: Produce 1M barrels/year, oil at $80**

| Hedge Ratio | Contracts | Locked Revenue | Exposure | Strategy |
|------------|-----------|----------------|----------|----------|
| 100% | 1,000 | $80M | $0 | Conservative |
| 70% | 700 | $56M | $24M | Moderate |
| 50% | 500 | $40M | $40M | Balanced |
| 30% | 300 | $24M | $56M | Aggressive |

**Decision factors:**

- Debt levels (high debt → More hedge)
- Equity buffer (low equity → More hedge)
- Market view (bullish → Less hedge)
- Volatility tolerance (low → More hedge)

### 2. Margin Management

**Critical for futures hedgers:**

**Initial margin:**

- Posted when opening position
- Typically 5-10% of notional
- Held by broker
- Returned when closed

**Maintenance margin:**

- Minimum balance required
- Typically 75% of initial margin
- Falls below → Margin call

**Margin call:**

- Must deposit more funds
- Usually within 24 hours
- If don't deposit → Position liquidated

**Example - Corn hedge:**

- Hedge: 100 contracts (500k bushels)
- Price: $7/bushel
- Notional: $3.5M
- Initial margin: 7% = $245k

**Price moves:**

| Day | Corn Price | Futures P&L | Margin Balance | Action |
|-----|-----------|------------|----------------|--------|
| 1 | $7.00 | $0 | $245k | OK |
| 2 | $6.80 | +$100k | $345k | OK |
| 3 | $7.50 | -$250k | -$5k | **MARGIN CALL** |

**Day 3 margin call:**

- Must deposit $250k immediately
- Or close position (forced exit)
- **This is the risk of futures hedging**

**Cash management strategy:**

1. **Maintain buffer:**
   - Keep 2-3x margin in reserves
   - Example: $245k margin → Keep $600k available

2. **Line of credit:**
   - Bank credit line for margin calls
   - Pre-arranged, draws automatically

3. **Monitor daily:**
   - Check margin balance every day
   - Project potential calls
   - Never get surprised

4. **Hedge timing:**
   - Don't hedge if can't support margin
   - Options alternative (no margin calls)

### 3. Basis Risk Management

**Understanding basis:**

$$
\text{Basis} = \text{Spot Price} - \text{Futures Price}
$$

**Types of basis risk:**

**1. Location basis:**

- Hedge: CBOT corn (Chicago)
- Actual: Local elevator (Kansas)
- Difference: Transportation, local supply/demand

**2. Quality basis:**

- Hedge: No. 2 yellow corn
- Actual: Lower quality corn
- Difference: Quality discount

**3. Time basis:**

- Hedge: December futures
- Actual: Sell in November
- Difference: One-month gap

**Managing basis risk:**

**Strategy 1: Accept it**

- Small basis (< 5% variance)
- Not worth complex hedge
- Monitor but don't over-hedge

**Strategy 2: Stack and roll**

- Use nearest futures month
- Roll monthly
- Matches timing better

**Strategy 3: OTC contracts**

- Customize with dealer
- Exact location, quality, timing
- Higher cost but perfect match

**Example - Wheat farmer:**

**Basis history:**

| Month | Chicago Futures | Local Cash | Basis |
|-------|----------------|------------|-------|
| Jun 2023 | $7.00 | $6.80 | -$0.20 |
| Jun 2022 | $8.00 | $7.70 | -$0.30 |
| Jun 2021 | $6.50 | $6.30 | -$0.20 |

**Average basis: -$0.23**

**Hedging adjustment:**

- Futures: $7.00
- Expected basis: -$0.23
- **Expected effective price: $6.77**

**Hedge accordingly:**

- Target: $6.75 minimum
- Futures gives: $6.77 effective
- **Close enough, hedge works**

### 4. Stop-Loss for Speculators (Not Hedgers!)

**Critical distinction:**

**Speculators:** Use stop-losses

**Hedgers:** DON'T use stop-losses

**Why?**

**Hedger example:**

- Airline hedged fuel at $2.50
- Fuel spikes to $4.00
- Futures losing $1.50/gallon (paper loss)
- Stop-loss would exit at -$0.75
- **Then fuel STAYS at $4.00 → Unhedged disaster**

**The hedge is WORKING even when losing money:**

- Futures: -$1.50/gallon
- Spot fuel: +$1.50/gallon
- **Net: $0 (perfect hedge)**

**Never exit hedge due to paper losses**

**The only reasons to exit hedge:**

1. Business exposure eliminated (produced less, need less)
2. Switching to different hedge (rolling, adjusting)
3. Company shutting down (no more exposure)

**Rule:** Hedge losses are offset by business gains. Stay the course.

### 5. Accounting Considerations

**Hedge accounting (very important):**

**Without hedge accounting:**

- Hedge gains/losses: Income statement (P&L)
- Business gains/losses: Later (when transaction occurs)
- **Result: Artificial volatility in earnings**

**With hedge accounting:**

- Hedge gains/losses: Deferred (balance sheet)
- Recognized when underlying transaction occurs
- **Result: Smooth earnings, hedge and hedged item match**

**Requirements:**

1. Document hedge at inception
2. Prove effectiveness (80-125% range)
3. Assess quarterly
4. Match hedge to business exposure

**Example - Airline:**

**Without hedge accounting (Jan-Dec):**

| Quarter | Fuel Cost | Futures Gain | Net | Reported |
|---------|-----------|--------------|-----|----------|
| Q1 | $60M | $0 | $60M | $60M cost |
| Q2 | $65M | $5M | $60M | $60M cost |
| Q3 | $70M | $15M | $55M | $55M cost |
| Q4 | $75M | $30M | $45M | $45M cost |

Reported earnings: Volatile ($60M → $55M → $45M)

**With hedge accounting:**

- All quarters: $60M cost reported
- Hedge gains deferred, recognized with fuel purchase
- **Smooth earnings, investors happy**

---



## Final Wisdom

> "Hedging is not about making money—it's about surviving to make money another day. The best hedge is the one you never regret because your business is still operating ten years from now. Accept that you'll sometimes 'lose' by foregoing gains, but remember: every time prices move against you, your hedge is the reason you're still in business. The goal isn't maximum profit; it's sustainable profit over decades."

**Key to success:**

- Clear business purpose (not speculation)
- Conservative sizing (50-70% typical)
- Adequate margin reserves (3-5x)
- Long-term perspective (survival > one year's gains)
- Discipline (don't exit due to regret)
- Proper documentation (accounting, compliance)

**Most important:** A hedge that "loses money" (foregoes gains) but keeps your business solvent is a SUCCESSFUL hedge. Measure success by business survival and stability, not hedge P&L in isolation. 🌾✈️⛽

**REMEMBER: The best outcome is a boring, predictable business that survives all market conditions.** 🎯