# Central Bank Policy

**Central bank policy trades** involve positioning futures contracts to profit from anticipated or actual changes in monetary policy by major central banks (Federal Reserve, ECB, BOJ, BOE, etc.), exploiting the predictable market reactions to interest rate decisions, forward guidance, quantitative easing/tightening, and macroeconomic policy shifts.

---

## The Core Insight

**The fundamental idea:**

- Central banks control short-term interest rates
- Monetary policy affects all asset classes
- Policy changes are telegraphed (forward guidance)
- Market reactions are large and predictable
- Trade the policy stance, not just the economy
- Multiple futures contracts affected simultaneously

**The key relationship:**

$$
\text{Asset Price Change} = f(\Delta \text{Policy Rate}, \Delta \text{Expectations}, \text{Surprise})
$$

Where:
- $\Delta \text{Policy Rate}$ = Actual rate change
- $\Delta \text{Expectations}$ = Change in forward guidance
- $\text{Surprise}$ = Deviation from market consensus

**The policy transmission mechanism:**

$$
\text{Fed Rate} \to \text{Treasury Yields} \to \text{Equity Valuations} \to \text{Dollar Strength} \to \text{Commodity Prices}
$$

**You're essentially betting: "I can predict how the central bank will change policy, or how markets will react to the policy change, and position futures contracts to profit from the predictable cascade of effects across asset classes."**

---

## What Are Central

**Before trading policy decisions, understand the central bank toolkit:**

### 1. The Central Bank

**1. Policy Interest Rates**

**Federal Reserve (U.S.):**
- **Federal Funds Rate:** Target for overnight lending between banks
- Range: Currently 5.25-5.50% (as of early 2024)
- Changed in 0.25% or 0.50% increments
- **8 FOMC meetings per year** (scheduled)

**Impact cascade:**
$$
\text{Fed Funds Rate} \uparrow \implies \text{Treasuries} \uparrow \implies \text{Equities} \downarrow \implies \text{Dollar} \uparrow
$$

**Other major central banks:**
- **ECB:** European Central Bank (Deposit Rate)
- **BOJ:** Bank of Japan (Policy Rate, historically negative)
- **BOE:** Bank of England (Bank Rate)
- **SNB, RBA, RBNZ:** Swiss, Australian, New Zealand central banks

**2. Forward Guidance**

**Definition:** Central bank communication about future policy intentions

**Types:**

**Calendar-based:**
> "We expect to maintain rates at current levels through mid-2024"

**State-dependent:**
> "We will not raise rates until inflation sustainably reaches 2%"

**Qualitative:**
> "We see risks tilted to the downside"

**Market impact:**
- Changes expectations
- More important than single rate decision
- **Can move markets more than actual policy!**

**3. Quantitative Easing (QE) / Tightening (QT)**

**QE: Central bank buys assets**
- Increases money supply
- Lowers long-term yields
- Boosts asset prices
- **Risk-on environment**

**QT: Central bank sells assets or lets them mature**
- Decreases money supply
- Raises long-term yields
- Pressures asset prices
- **Risk-off environment**

**Balance sheet size matters:**
- Fed: $9 trillion peak (COVID)
- ECB: €8 trillion
- BOJ: ¥750 trillion (>100% of GDP!)

### 2. The Policy Cycle

**Typical cycle:**

1. **Easing cycle (dovish):**
   - Cut rates
   - Implement QE
   - Dovish forward guidance
   - **Duration: 1-3 years**

2. **Steady state:**
   - Rates on hold
   - Neutral guidance
   - Monitor data
   - **Duration: 6-18 months**

3. **Tightening cycle (hawkish):**
   - Raise rates
   - Implement QT
   - Hawkish forward guidance
   - **Duration: 1-2 years**

**Current example (2022-2024):**
- **2020-2021:** Easing (COVID response, 0% rates)
- **2022-2023:** Aggressive tightening (inflation fight, 0% → 5.5%)
- **2024:** Pause, eventual easing expected

### 3. Market Reactions

**Rate hike (hawkish):**

| Asset Class | Reaction | Futures Contract |
|-------------|----------|------------------|
| Treasury bonds | Prices ↓ (yields ↑) | ZB, ZN, ZF (short) |
| Equity indices | ↓ (higher discount rate) | ES, NQ (short) |
| Dollar | ↑ (higher yields attract capital) | DX (long) |
| Gold | ↓ (opportunity cost rises) | GC (short) |
| Commodities | Mixed (dollar strength vs. demand) | CL, NG (varies) |

**Rate cut (dovish):**

| Asset Class | Reaction | Futures Contract |
|-------------|----------|------------------|
| Treasury bonds | Prices ↑ (yields ↓) | ZB, ZN, ZF (long) |
| Equity indices | ↑ (lower discount rate) | ES, NQ (long) |
| Dollar | ↓ (lower yields reduce appeal) | DX (short) |
| Gold | ↑ (lower opportunity cost) | GC (long) |
| Commodities | ↑ (weaker dollar, growth) | CL, NG (long) |

**The surprise factor:**

$$
\text{Market Move} = \beta_1 \cdot \text{Expected Change} + \beta_2 \cdot \text{Surprise}
$$

Where typically: $|\beta_2| >> |\beta_1|$

**Example:**
- Expected: +0.25% rate hike (priced in)
- Actual: +0.50% rate hike (surprise!)
- **Market reaction: 2-3× larger than if 0.50% was expected**

### 4. Simple Example

**Setup (June 2023 FOMC meeting):**

**Pre-meeting:**
- Current Fed Funds: 5.00-5.25%
- Market expects: Hold (70% probability)
- Minority expects: +0.25% hike (30% probability)

**Your analysis:**
- Inflation still elevated
- Job market strong
- Fed commentary hawkish
- **Predict: They will hike (+0.25%)**

**The trade:**

**One day before FOMC:**
- Short 10 ES (S&P 500 E-mini) at 4,450
- Short 5 NQ (NASDAQ) at 15,500
- Short 10 ZN (10-Year Treasury) at 113-00
- **Position: Betting on hawkish surprise**

**FOMC decision:**
- **Actual: +0.25% hike** (as you predicted!)
- Plus hawkish guidance: "Further hikes may be necessary"
- **Double hawkish surprise** (hike + guidance)

**Market reaction (next day):**
- ES: 4,450 → 4,380 (down 70 points)
- NQ: 15,500 → 15,200 (down 300 points)
- ZN: 113-00 → 111-16 (down 1.5 points)

**P&L:**

**ES (short):**
- 70 points × $50/point × 10 contracts = **+$35,000**

**NQ (short):**
- 300 points × $20/point × 5 contracts = **+$30,000**

**ZN (short):**
- 1.5 points × $1,000/point × 10 contracts = **+$15,000**

**Total: +$80,000 in one day!** 🎯

**On margin of ~$50,000:** Return = **160%** in 24 hours!

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/central_bank_policy_trades.png?raw=true" alt="central_bank_policy_trades" width="700">
</p>
**Figure 1:** Illustration of central bank policy trade showing typical market reactions across asset classes to hawkish (rate hike) vs. dovish (rate cut) monetary policy decisions. The surprise component often dominates the market response.

---

## Economic

**Beyond the mechanical reactions, understanding the transmission mechanisms:**

### 1. The Monetary

**1. Interest Rate Channel**

**Direct mechanism:**

$$
r \uparrow \implies \text{Cost of Capital} \uparrow \implies \text{Investment} \downarrow \implies \text{GDP} \downarrow
$$

**Asset valuation:**

$$
\text{Stock Price} = \sum_{t=1}^{\infty} \frac{E[\text{Earnings}_t]}{(1+r)^t}
$$

**Higher $r$ → Lower present value → Lower stock prices**

**Bond pricing:**

$$
P = \sum_{t=1}^{n} \frac{C}{(1+r)^t} + \frac{F}{(1+r)^n}
$$

**Higher $r$ → Lower bond prices**

**2. Exchange Rate Channel**

**Uncovered Interest Parity:**

$$
E[\Delta S] = r_{\text{domestic}} - r_{\text{foreign}}
$$

**Higher domestic rates → Currency appreciation**

**Example:**
- Fed raises rates 0.50%
- ECB on hold
- Dollar strengthens vs. Euro
- **DX futures rally**

**3. Asset Price Channel (Wealth Effect)**

**Mechanism:**

$$
\text{Rates} \downarrow \implies \text{Asset Prices} \uparrow \implies \text{Wealth} \uparrow \implies \text{Consumption} \uparrow
$$

**Example:**
- Fed cuts rates 0.50%
- Stock market rallies 5%
- Homeowners feel wealthier
- **Consumer spending increases**

**4. Credit Channel**

**Bank lending:**

$$
\text{Policy Rate} \downarrow \implies \text{Lending Spreads} \downarrow \implies \text{Credit Growth} \uparrow
$$

**Corporate borrowing:**
- Lower rates → Cheaper debt
- More investment
- **Economic expansion**

### 2. The Taylor Rule

**Prescriptive policy rule:**

$$
i_t = r^* + \pi_t + 0.5(\pi_t - \pi^*) + 0.5(y_t - y^*)
$$

Where:
- $i_t$ = Target policy rate
- $r^*$ = Equilibrium real rate (~2%)
- $\pi_t$ = Current inflation
- $\pi^*$ = Target inflation (2%)
- $y_t - y^*$ = Output gap

**Trading application:**

**If actual rate < Taylor Rule → Fed behind the curve → Expect hikes**
**If actual rate > Taylor Rule → Fed ahead of the curve → Expect cuts**

**Example (2022):**
- Inflation: 8%
- Taylor Rule: Fed should be at 6-7%
- Actual Fed Funds: 0%
- **Prediction: Aggressive tightening ahead** ✓

### 3. Forward Guidance

**The commitment mechanism:**

**Credible guidance:**
- Central bank history of following through
- Clear communication
- **Markets trust and price it in**

**Non-credible guidance:**
- History of policy reversals
- Unclear messaging
- **Markets skeptical, volatile reactions**

**Example: ECB vs. Fed**
- Fed: High credibility (follows guidance 90%+)
- ECB: Lower credibility (political constraints)
- **Fed guidance moves markets more**

### 4. Quantitative

**The portfolio balance channel:**

$$
\text{CB buys bonds} \implies \text{Bond prices} \uparrow \implies \text{Yields} \downarrow \implies \text{Risk assets} \uparrow
$$

**QE impact:**

**Direct:**
- Removes safe assets from market
- Investors forced into riskier assets
- **"Don't fight the Fed"**

**Signaling:**
- Shows commitment to accommodation
- Lowers long-term rate expectations
- **Confidence boost**

**Example: 2020 COVID QE**
- Fed announced unlimited QE (March 2020)
- 10-Year yield: 1.5% → 0.5% (fell 100 bps)
- S&P 500: 2,200 → 3,200 (up 45% in 3 months)
- **Massive policy response = Massive market reaction**

### 5. Why This

**Understanding policy transmission helps you:**

1. **Predict cross-asset reactions:**
   - Rate hike → Which assets hurt most?
   - QE announcement → Which assets benefit most?
   - **Position across multiple futures**

2. **Time entry/exit:**
   - Front-run before decision
   - Fade after overreaction
   - **Maximize edge**

3. **Assess credibility:**
   - Will markets believe guidance?
   - History of policy pivots
   - **Adjust conviction**

4. **Identify regime changes:**
   - End of tightening cycle
   - Start of easing cycle
   - **Biggest opportunities**

**Professionals say: "Central banks are the biggest players in the market. Understanding their playbook gives you the ultimate edge—it's like trading with marked cards, but legal."**

---
