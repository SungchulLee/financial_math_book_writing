# Roll Yield


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

### 1. The Rolling


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

### 2. Contango vs.


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

### 3. The Compounding


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

### 4. Real-World


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

## Economic


**Beyond the mechanical explanation, understanding the economic drivers:**

### 1. The Cost of Carry


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

### 2. Storage Theory


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

### 3. Why This


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

## Final Wisdom


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

### 2. The Compounding


**Single roll:** Small impact (-3%)
**Multiple rolls:** MASSIVE impact

**Example:**
- Monthly roll: -3%
- Annual: 12 × -3% = -36%
- 5 years: -85% cumulative
- **Time multiplies roll impact**

### 3. Contango vs.


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

### 4. When to Trade for


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

### 5. Best Case


**Example: 2022 Europe Natural Gas**
- Entry: €40/MWh (backwardation €5/month)
- 6 months of rolling: +€34 from roll yield (+85%)
- Spot also rose: +€30 (+75%)
- **Total: +160% (roll > spot!)** 🎯

### 6. Worst Case


**Example: USO 2009-2020**
- Oil spot: $50 → $40 (-20%)
- USO: $40 → $2 (-95%)
- **Roll yield cost: -75%!** ☠️
- Persistent contango killed the fund

### 7. Critical Lessons


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

### 8. Alternatives to


**In persistent contango (>3% monthly):**
- Commodity stocks (no roll, dividends)
- Physical commodity (storage < roll cost)
- Long-dated options (1-2 rolls/year vs. 12)
- **Don't use front-month futures!**

### 9. Key Magnitudes


| Commodity | Typical Contango | Typical Backwardation |
|-----------|-----------------|---------------------|
| Crude oil | -20% to -40%/year | +15% to +60%/year |
| Natural gas (summer) | -30% to -55%/year | N/A |
| Natural gas (winter) | N/A | +20% to +100%/year |
| Gold | -4% to -6%/year | Rare |


> "In commodity futures, the curve is the trade. You can be right on direction and still lose everything if you ignore roll yield. Contango is a silent killer that compounds monthly. Backwardation is a hidden profit engine. Calculate the annual roll cost BEFORE entering any commodity position. If you don't understand roll yield, you're just donating money to those who do."

**Most important rules:**

1. Calculate annualized roll cost ALWAYS
2. In contango >3% monthly → Use alternatives  
3. In backwardation >5% monthly → Futures attractive
4. Monitor curve shape religiously
5. Exit if curve turns against you
6. **Never ignore the curve - it compounds!** 🎯📉📈