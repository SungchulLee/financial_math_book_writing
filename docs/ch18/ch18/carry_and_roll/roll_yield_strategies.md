# Roll Yield Strategies

**Roll yield strategies** involve systematically profiting from or managing the cost/benefit of rolling futures positions from expiring contracts to later-dated contracts, exploiting predictable patterns in the futures curve shape (contango or backwardation) to generate returns independent of absolute price movements.

---

## The Core Insight

**The fundamental idea:**

- Futures contracts expire - must roll to maintain exposure
- Rolling has a cost (contango) or benefit (backwardation)
- This "roll yield" compounds over time
- Can dominate total returns (more important than price movement!)
- Curve shape is often predictable (seasonal, storage-driven)
- Trade the curve shape, not the price level

**The key equation:**

$$
\text{Roll Yield} = \frac{F_{\text{near}} - F_{\text{far}}}{F_{\text{near}}} \times \frac{1}{T_{\text{roll}}}
$$

Where:
- $F_{\text{near}}$ = Price of expiring (near) contract
- $F_{\text{far}}$ = Price of next (far) contract
- $T_{\text{roll}}$ = Time period for annualization

**The total return decomposition:**

$$
\text{Total Return} = \underbrace{\text{Spot Return}}_{\text{Price change}} + \underbrace{\text{Roll Yield}}_{\text{Curve shape}} + \underbrace{\text{Collateral Return}}_{\text{Interest on margin}}
$$

**You're essentially betting: "I can predict whether the futures curve will be upward or downward sloping, and profit from the roll regardless of price direction."**

---

## What is Roll Yield?

**Before trading roll yield, understand what you're actually capturing:**

### 1. The Rolling Mechanism

**Definition:** Roll yield is the profit or loss from closing an expiring futures contract and opening the next contract, driven by the difference in price between the two contracts.

**Why rolling is necessary:**

- Futures contracts have fixed expiration dates
- To maintain continuous exposure, must close expiring contract
- Simultaneously open next-dated contract
- The price difference creates a cost or benefit

**Example:**

**Month 1:**
- Long crude oil March contract at $75/barrel
- Position: Continuous exposure to oil

**Late February (approaching expiration):**
- March contract: $76/barrel (close at $76)
- June contract: $78/barrel (open at $78)
- **Roll cost: $78 - $76 = $2/barrel**

**This $2 cost is negative roll yield in contango.**

### 2. Contango vs. Backwardation

**Contango (Upward-sloping curve):**

$$
F_{\text{far}} > F_{\text{near}} \quad \implies \quad \text{Roll Yield} < 0
$$

**Characteristics:**
- Later contracts more expensive than near
- Normal for storable commodities
- Reflects carrying costs (storage + financing)
- **Hurts long positions (sell low, buy high)**
- Benefits short positions

**Example:**
- March crude: $75
- June crude: $78
- September crude: $80
- **Curve slopes up (contango)**

**Roll cost for long:**
- Close March at $75
- Open June at $78
- **Cost: $3/barrel (negative roll yield)**

**Backwardation (Downward-sloping curve):**

$$
F_{\text{near}} > F_{\text{far}} \quad \implies \quad \text{Roll Yield} > 0
$$

**Characteristics:**
- Near contracts more expensive than far
- Indicates supply shortage or high convenience yield
- Abnormal market condition
- **Benefits long positions (sell high, buy low)**
- Hurts short positions

**Example:**
- March crude: $80
- June crude: $77
- September crude: $75
- **Curve slopes down (backwardation)**

**Roll benefit for long:**
- Close March at $80
- Open June at $77
- **Gain: $3/barrel (positive roll yield)**

### 3. The Compounding Effect

**Single roll:**
- Roll cost/benefit: $2/barrel
- On 1,000 barrels: $2,000
- Seems small

**But rolls compound:**

**Example: 12 monthly rolls in steep contango**

| Month | Near | Far | Roll Cost | Cumulative |
|-------|------|-----|-----------|------------|
| 1 | $75 | $78 | -$3 | -$3 |
| 2 | $78 | $81 | -$3 | -$6 |
| 3 | $81 | $84 | -$3 | -$9 |
| 4 | $84 | $87 | -$3 | -$12 |
| ... | ... | ... | ... | ... |
| 12 | $108 | $111 | -$3 | **-$36** |

**Annual roll cost: $36/barrel!**

**On initial $75 position: -48% from rolls alone!**

**Even if oil price unchanged, you lost 48% from rolling!**

This is why understanding roll yield is CRITICAL.

### 4. Real-World Example

**The commodity ETF trap:**

**USO structure:**
- Tracks crude oil via front-month futures
- Rolls monthly (forced)
- Investors think they're getting oil exposure

**2009-2020 Performance:**

**Oil spot price:**
- Start: $50/barrel (2009)
- End: $50/barrel (2020)
- **Change: 0%**

**USO price:**
- Start: $100/share
- End: $25/share (adjusted for reverse splits)
- **Change: -75%!**

**How did this happen?**

**Persistent contango:**
- Had to roll from front month to next month
- Always paid premium (contango)
- 11 years × 12 rolls × average $1.50 cost = **-$198 cumulative**
- **Roll yield destroyed the fund**

**Lesson: Roll yield can dominate returns!**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/roll_yield_strategies.png?raw=true" alt="roll_yield_strategies" width="700">
</p>
**Figure 1:** Illustration of roll yield in contango (negative roll) and backwardation (positive roll). The futures curve shape determines whether rolling positions generates profit or loss, independent of absolute price levels.

---

## Economic Interpretation

**Beyond the mechanical explanation, understanding the economic drivers:**

### 1. The Cost of Carry Framework

**For storable commodities, futures prices reflect carry costs:**

$$
F_t = S_t \cdot e^{(r+u-y)(T-t)}
$$

Where:
- $F_t$ = Futures price
- $S_t$ = Spot price
- $r$ = Interest rate (financing cost)
- $u$ = Storage cost
- $y$ = Convenience yield
- $T-t$ = Time to expiration

**The futures curve slope:**

$$
\frac{\partial F}{\partial T} = S \cdot e^{(r+u-y)(T-t)} \cdot (r+u-y)
$$

**Interpretation:**

If $r + u > y$ (carry costs > convenience yield):
- $\frac{\partial F}{\partial T} > 0$ → **Contango**
- Later contracts higher (compensate for carry)
- **Negative roll yield for longs**

If $y > r + u$ (convenience yield > carry costs):
- $\frac{\partial F}{\partial T} < 0$ → **Backwardation**
- Near contracts higher (immediate need premium)
- **Positive roll yield for longs**

### 2. Storage Theory and Convenience Yield

**The Theory of Storage (Kaldor, Working, Brennan):**

**When inventories high:**
- Low convenience yield (easy to get commodity)
- Storage costs dominate
- $u > y$ → Contango
- **Negative roll yield expected**

**When inventories low:**
- High convenience yield (immediate delivery valuable)
- Stockout risk premium
- $y > u$ → Backwardation
- **Positive roll yield expected**

**The convenience yield reflects:**
- Value of having commodity NOW vs. later
- Production flexibility (refineries, processors)
- Stockout insurance
- Seasonal demand patterns

**Example: Crude oil**

**Normal times (inventories adequate):**
- Refineries comfortable with stock levels
- Convenience yield: ~1-2%
- Storage + financing: ~4-5%
- Net carry: +3%
- **Contango: $1-$2/barrel (negative roll yield)**

**Supply disruption (inventories critical):**
- Refineries desperate for immediate oil
- Convenience yield: 10%+
- Storage irrelevant (nothing to store!)
- Net carry: -8%
- **Backwardation: $5-$10/barrel (positive roll yield)**

### 3. Why This Perspective Matters

**Understanding roll yield economics helps you:**

1. **Predict curve shape:**
   - Inventory reports → Storage theory
   - Seasonal patterns → Predictable changes
   - Index flows → Financialization pressure

2. **Identify opportunities:**
   - Extreme contango → Potential mean reversion
   - Extreme backwardation → Temporary shortage

3. **Manage positions:**
   - Persistent contango → Avoid long futures, use options
   - Backwardation → Favor long futures over spot
   - **Choose instrument based on curve**

4. **Structure trades:**
   - Calendar spreads to isolate roll yield
   - Curve trades (steepeners/flatteners)
   - **Pure roll yield capture**

**This is why sophisticated traders say: "In commodities, the curve IS the trade."**

---

## What to Remember

### 1. Core Concept

**Roll yield is the profit or loss from rolling futures contracts:**

$$
\text{Roll Yield} = \frac{F_{\text{near}} - F_{\text{far}}}{F_{\text{near}}}
$$

**Total futures return:**

$$
\text{Total Return} = \text{Spot Return} + \text{Roll Yield} + \text{Collateral Return}
$$

- Roll yield can dominate total returns
- Independent of spot price direction
- **Can make or break commodity investing**

### 2. Contango vs. Backwardation

**Contango (negative roll):**

$$
F_{\text{far}} > F_{\text{near}} \quad \implies \quad \text{Roll Yield} < 0
$$

- Upward-sloping curve
- Normal for storable commodities
- Reflects carry costs
- **Hurts long positions (sell low, buy high)**

**Backwardation (positive roll):**

$$
F_{\text{near}} > F_{\text{far}} \quad \implies \quad \text{Roll Yield} > 0
$$

- Downward-sloping curve
- Indicates supply tightness
- Convenience yield > carry costs
- **Benefits long positions (sell high, buy low)**

### 3. Why Roll Yield Exists

**Cost of carry:**

$$
F = S \cdot e^{(r+u-y)(T-t)}
$$

- $r$ = Interest rate
- $u$ = Storage cost
- $y$ = Convenience yield

**If $r+u > y$:** Contango (negative roll)
**If $y > r+u$:** Backwardation (positive roll)

### 4. The Compounding Effect

**Single roll:** Small impact (-3%)
**Multiple rolls:** MASSIVE impact

**Example:**
- Monthly roll: -3%
- Annual: 12 × -3% = -36%
- 5 years: -85% cumulative
- **Time multiplies roll impact exponentially**

### 5. Key Magnitudes

**Typical roll yields:**

| Commodity | Contango | Backwardation | Frequency |
|-----------|----------|---------------|-----------|
| Crude oil | -20% to -40%/year | +15% to +60%/year | Mixed |
| Natural gas (summer) | -30% to -55%/year | Rare | Seasonal |
| Natural gas (winter) | Rare | +20% to +100%/year | Seasonal |
| Gold | -4% to -6%/year | Rare | Almost always contango |
| Corn (post-harvest) | -5% to -20%/year | Rare | Harvest-driven |

### 6. When to Trade for Roll Yield

**Enter long when:**
- Backwardation >5% monthly
- Seasonal pattern favorable (winter natural gas)
- Inventory data supports tightness
- **Positive roll expected**

**Avoid long when:**
- Contango >3% monthly
- Seasonal contango period (summer natural gas, post-harvest grains)
- High inventory levels
- **Negative roll expected - use alternatives!**

### 7. Best Case Scenarios

**Maximum positive roll:**
- Steep backwardation (>10% monthly)
- Sustained (6+ months)
- Spot price also rising
- **Returns: +100% to +3,000% possible**

**Examples:**
- 2022 Europe natural gas: +3,200% return in 6 months (roll +85%, spot +75%)
- 2007-08 crude oil: +2,340% return in 18 months (roll +49%, spot +164%)
- **Roll yield exceeded spot return**

### 8. Worst Case Scenarios

**Maximum negative roll:**
- Steep contango (<-4% monthly)
- Persistent (years)
- Spot price also falling
- **Losses: -90% to -99% total destruction**

**Examples:**
- USO 2009-2020: -95% loss (oil spot -20%, roll cost -75%)
- UNG 2010-2020: -93% loss (gas spot -44%, roll cost -49%)
- S&P GSCI 2008-2020: -91% loss (spot -36%, roll cost -55%)
- **Roll yield destroyed more value than spot declines**

### 9. The USO Disaster (Critical Lesson)

**What happened:**
- 2009: Oil $50/barrel, USO $100/share
- 2020: Oil $50/barrel, USO $25/share
- **Oil unchanged, USO down 75%!**

**Why:**
- Persistent contango: -3% monthly average
- 11 years × 12 rolls = 132 rolls
- Cumulative roll cost: -75%
- **Compounding destroyed value**

**Lesson:**
- Never buy commodity ETFs in contango
- Calculate annualized roll cost FIRST
- -3% monthly = -36% annually = -99% in 10 years
- **Time is the enemy in contango**

### 10. Strategic Implications

**For long exposure:**

**In contango (>3% monthly):**
- Avoid futures → Use alternatives
- Commodity stocks (no roll, dividends)
- Physical commodity (if storage < roll cost)
- Long-dated options (1-2 rolls/year vs. 12)
- **Don't buy commodity ETFs!**

**In backwardation (>5% monthly):**
- Prefer futures (earn positive roll)
- Front-month optimal (maximize roll benefit)
- **Capture roll yield actively**

**For hedgers:**
- Stack in contango (minimize rolls)
- Strip in backwardation (maximize rolls)
- Optimize roll timing (avoid fixed schedules)
- **Manage roll costs actively - can save 10-20%**

### 11. Seasonal Patterns

**Natural gas:**
- Winter (Nov-Mar): Backwardation +20% to +100% → **Long**
- Summer (Apr-Oct): Contango -30% to -55% → **Avoid/Short**
- Pattern reliability: 80-90%

**Agricultural commodities:**
- Pre-harvest: Moderate contango -2% to -5%
- Harvest (Oct-Nov): Steep contango -10% to -20% → **Avoid**
- Post-harvest (Dec-Mar): Moderate contango -5% to -8%
- Pattern reliability: 70-80%

**Energy products:**
- Gasoline: Summer demand → Backwardation (May-Aug)
- Heating oil: Winter demand → Backwardation (Nov-Feb)

### 12. Common Mistakes

1. **Ignoring curve shape** (only looking at spot price)
2. **Buying commodity ETFs in contango** (USO, UNG disasters)
3. **Not calculating annualized roll cost** before entering
4. **Holding through unfavorable seasons** (summer natural gas)
5. **Thinking "oil ETF" = "oil price"** (totally different!)
6. **No exit plan for persistent negative roll**
7. **Not using alternatives when appropriate**
8. **Rolling on fixed schedule** (get front-run, pay more)

### 13. Roll Management Techniques

**Optimize rolling:**
- Don't roll on fixed dates (avoid index front-running)
- Wait for favorable spreads (can save 10-20%)
- Monitor spread daily during roll window
- **Execute when contango narrowest**

**Stagger positions:**
- Mix of front, 2nd, 3rd month contracts
- Smooth roll profile over time
- Reduce concentration risk
- **Average better roll prices**

**Seasonal strategy:**
- Natural gas: Long October-March only (positive roll)
- Agricultural: Avoid September-November (harvest contango)
- **Trade with seasonality, not against it**

### 14. Key Formulas

**Roll yield (single roll):**

$$
\text{Roll \%} = \frac{F_{\text{close}} - F_{\text{open}}}{F_{\text{close}}}
$$

**Annualized roll yield:**

$$
\text{Annual Roll Yield} = \text{Monthly Roll \%} \times 12
$$

**Or more precisely:**

$$
\text{Annual} = \left(1 + \text{Monthly Roll}\right)^{12} - 1
$$

**Total futures return:**

$$
R_{\text{total}} = R_{\text{spot}} + R_{\text{roll}} + R_{\text{collateral}}
$$

**Approximate roll cost:**

For small monthly rolls:

$$
\text{Annual Roll Cost} \approx \frac{F_2 - F_1}{F_1} \times 12
$$

### 15. Alternatives to Avoid Negative Roll

**When contango >3% monthly:**

| Alternative | Roll Impact | Pros | Cons |
|------------|-------------|------|------|
| Physical commodity | None | No roll cost | Storage, insurance costs |
| Commodity stocks | None | Dividends, no roll | Company-specific risk |
| Long-dated options (LEAPS) | Minimal (1-2/year) | Low roll frequency | Time decay, premium |
| Calendar spreads | Isolated | Pure curve trade | Two positions, margin |
| Avoid the market | None | Capital preserved | No exposure at all |

### 16. The Fundamental Truth

**Roll yield often MORE important than spot price:**

**Evidence:**
- USO: Spot -20%, Roll -75% → Total -95%
- 2022 Europe gas: Spot +75%, Roll +85% → Total +160%
- **Curve shape >>> Price direction**

**Why this happens:**
- Roll yield compounds (12+ rolls per year)
- Spot return doesn't compound same way
- **Time amplifies roll impact**

### 17. Calculation Before Entry

**ALWAYS calculate before entering position:**

**Example: Crude oil**

**Current curve:**
- Front month: $75/barrel
- 2nd month: $78/barrel
- Difference: $3

**Monthly roll cost:**

$$
\frac{78 - 75}{75} = 4\%
$$

**Annualized:**

$$
4\% \times 12 = 48\% \text{ annual cost!}
$$

**Decision:**
- If bullish on oil but curve this steep
- **Don't use futures! Use stocks or long-dated options**
- Otherwise need oil to rise >48% just to break even on roll

### 18. Risk Management

**Position sizing in contango:**
- Smaller positions (roll bleeds value)
- Shorter duration (don't compound losses)
- Active monitoring (exit if curve steepens)

**Position sizing in backwardation:**
- Can be larger (roll adds value)
- Longer duration (let roll compound)
- Still monitor (curve can flip)

**Stop losses:**
- If backwardation → contango: Exit immediately
- If contango steepens >2× expected: Exit
- **Curve reversal = thesis broken**

### 19. Performance Attribution

**Decompose returns to understand:**

**Example: 1-year oil position**

- Starting price: $75
- Ending price: $80
- Spot return: +6.7%
- Roll cost: -36% (monthly -3%)
- Collateral: +4%
- **Total: -25.3%** (lost money despite oil rising!)

**Attribution:**
- Spot: +$5 × 1,000 = +$5,000
- Roll: -$27 × 1,000 = -$27,000
- Collateral: +$3,000
- **Net: -$19,000** ☠️

**Lesson: Track roll separately from spot!**

### 20. Historical Statistics

**Crude oil (2000-2023 average):**
- Average curve: Contango
- Average monthly roll: -2.5%
- Average annual roll: -30%
- **Persistent negative roll**

**Natural gas (2000-2023):**
- Summer average: -35% annual
- Winter average: +25% annual
- **Highly seasonal, predictable**

**Gold (2000-2023):**
- Average roll: -4.8% annual
- Very stable (tracks interest rates)
- **Consistently negative, predictable**

### 21. When Roll Yield Strategy Works

**Best conditions:**
1. Predictable seasonal patterns
2. Clear inventory signals
3. Mean-reverting curve shape
4. Ability to time entry/exit
5. **Discipline to avoid contango**

**Poor conditions:**
1. Unpredictable curve changes
2. Need continuous exposure
3. Can't time market
4. **Must hold through contango**

### 22. Comparison

**Same commodity exposure, different roll:**

**Example: Oil exposure**

**Exxon stock:**
- No roll yield impact
- Dividend yield: +3-4%
- Company-specific risk
- **Total: Spot + dividend**

**Oil futures:**
- Roll yield: -30% (contango) or +20% (backwardation)
- No dividends
- Pure commodity exposure
- **Total: Spot + roll + collateral**

**Which is better?**
- Contango >5%: **Stocks win**
- Backwardation >10%: **Futures win**
- Otherwise: **Similar**

### 23. The Professional Approach

**How professionals trade roll yield:**

1. **Calculate annualized roll FIRST**
2. **Compare to historical average**
3. **Check inventory data**
4. **Consider seasonality**
5. **Choose optimal instrument**
6. **Monitor curve daily**
7. **Exit if thesis breaks**
8. **Never "set and forget"**

### 24. Final Wisdom

> "In commodity futures, the curve is the trade. You can be right on direction and still lose everything if you ignore roll yield. Contango is a silent killer that compounds monthly, destroying value even when prices are flat. Backwardation is a hidden profit engine that can double your returns. Professional traders who survive know: never fight the curve for long, and always calculate the annual roll cost before entering any commodity position. If you don't understand roll yield, you're not investing in commodities—you're just donating money to those who do."

**Key principles:**

1. **Calculate annualized roll cost BEFORE entering (non-negotiable)**
2. **In contango >3% monthly → Use alternatives, not futures**
3. **In backwardation >5% monthly → Futures attractive**
4. **Monitor curve shape religiously (daily in volatile markets)**
5. **Exit immediately if curve turns against you**
6. **Seasonal patterns are your friend (trade with them)**
7. **Time compounds roll impact (longer = more important)**
8. **Never buy commodity ETFs without checking curve**

**Most important:**

Roll yield can be +100% or -90% annually. It compounds. It's predictable. It's often larger than spot returns. It's the difference between massive profits and total loss. **Ignore it at your peril.** 🎯📉📈

**Remember the USO lesson:**
- Oil unchanged over 11 years
- USO lost 75%
- **All from roll yield**
- Don't let this be you! ⚠️

### 25. Core Concept

**Roll yield is the profit or loss from rolling futures contracts:**

$$
\text{Roll Yield} = \frac{F_{\text{near}} - F_{\text{far}}}{F_{\text{near}}}
$$

**Total futures return:**

$$
\text{Total Return} = \text{Spot Return} + \text{Roll Yield} + \text{Collateral Return}
$$

- Roll yield can dominate total returns
- Independent of spot price direction
- **Can make or break commodity investing**

### 26. The Compounding Effect

**Single roll:** Small impact (-3%)
**Multiple rolls:** MASSIVE impact

**Example:**
- Monthly roll: -3%
- Annual: 12 × -3% = -36%
- 5 years: -85% cumulative
- **Time multiplies roll impact**

### 27. Contango vs. Backwardation

**Contango (negative roll):**

$$
F_{\text{far}} > F_{\text{near}} \quad \implies \quad \text{Roll Yield} < 0
$$

- Upward-sloping curve
- Normal for storable commodities
- **Hurts long positions (sell low, buy high)**

**Backwardation (positive roll):**

$$
F_{\text{near}} > F_{\text{far}} \quad \implies \quad \text{Roll Yield} > 0
$$

- Downward-sloping curve
- Indicates supply tightness
- **Benefits long positions (sell high, buy low)**

### 28. When to Trade for Roll Yield

**Enter long when:**
- Backwardation >5% monthly
- Seasonal pattern favorable (winter natural gas)
- Inventory data supports tightness
- **Positive roll expected**

**Avoid long when:**
- Contango >3% monthly
- Seasonal contango period (summer natural gas)
- High inventory levels
- **Negative roll expected - use alternatives!**

### 29. Best Case

**Example: 2022 Europe Natural Gas**
- Entry: €40/MWh (backwardation €5/month)
- 6 months of rolling: +€34 from roll yield (+85%)
- Spot also rose: +€30 (+75%)
- **Total: +160% (roll > spot!)** 🎯

### 30. Worst Case

**Example: USO 2009-2020**
- Oil spot: $50 → $40 (-20%)
- USO: $40 → $2 (-95%)
- **Roll yield cost: -75%!** ☠️
- Persistent contango killed the fund

### 31. Critical Lessons

**From USO disaster:**
- Never buy commodity ETFs in contango
- Calculate annualized roll cost first
- -3% monthly = -36% annually = -99% over 10 years
- **Time is the enemy in contango**

**From successful trades:**
- Backwardation can add +50-100% annually
- Seasonal patterns are predictable
- Natural gas: Long winter, avoid summer
- **Curve shape matters more than price**

### 32. Alternatives to Avoid Negative Roll

**In persistent contango (>3% monthly):**
- Commodity stocks (no roll, dividends)
- Physical commodity (storage < roll cost)
- Long-dated options (1-2 rolls/year vs. 12)
- **Don't use front-month futures!**

### 33. Key Magnitudes

| Commodity | Typical Contango | Typical Backwardation |
|-----------|-----------------|---------------------|
| Crude oil | -20% to -40%/year | +15% to +60%/year |
| Natural gas (summer) | -30% to -55%/year | N/A |
| Natural gas (winter) | N/A | +20% to +100%/year |
| Gold | -4% to -6%/year | Rare |

### 34. Final Wisdom

> "In commodity futures, the curve is the trade. You can be right on direction and still lose everything if you ignore roll yield. Contango is a silent killer that compounds monthly. Backwardation is a hidden profit engine. Calculate the annual roll cost BEFORE entering any commodity position. If you don't understand roll yield, you're just donating money to those who do."

**Most important rules:**

1. Calculate annualized roll cost ALWAYS
2. In contango >3% monthly → Use alternatives  
3. In backwardation >5% monthly → Futures attractive
4. Monitor curve shape religiously
5. Exit if curve turns against you
6. **Never ignore the curve - it compounds!** 🎯📉📈
