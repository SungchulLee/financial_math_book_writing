# Risk Reversals

**Risk reversals** are synthetic stock positions created by simultaneously buying a call and selling a put (or vice versa), primarily used to trade the volatility skew while maintaining directional exposure with minimal upfront cost.

---

## The Core Insight

**The fundamental idea:**

- Volatility skew exists: OTM puts trade at higher IV than OTM calls
- This skew premium can be captured or traded
- Create synthetic long/short stock with zero (or minimal) cost
- Express directional view while trading skew
- Different from owning stock: no dividend, expiration risk
- Leverage without upfront capital (or collect premium)

**The key equation:**

$$
\text{Risk Reversal P&L} = \Delta \cdot (S_T - S_0) \pm \text{Net Premium} \pm \text{Skew Change}
$$

$$
\text{Zero-Cost Setup: } C_{\text{buy}} - P_{\text{sell}} \approx 0 \text{ (initial net premium)}
$$

**You're essentially betting: "I want directional exposure AND the volatility skew will move in my favor."**

---

## What Is a Risk Reversal?

**Before trading risk reversals, understand what you're creating:**

### Bullish Risk Reversal (Synthetic Long Stock)

**Definition:** Buy OTM call + Sell OTM put, typically with strikes equidistant from current price or adjusted for zero cost.

**Structure:**

- **Buy:** OTM call at strike $K_C$ (e.g., $105 call)
- **Sell:** OTM put at strike $K_P$ (e.g., $95 put)
- **Current stock:** $S_0 = 100$
- **Net premium:** Ideally $\approx 0$ (or small debit/credit)

**Position characteristics:**

- Delta: ~+1.0 (stock-like)
- Vega: Short (sold put vega > bought call vega due to skew)
- Theta: Slightly positive (net time decay from put sale)
- Gamma: Positive near strikes, but less than long straddle

**Example:**

- Stock at $100
- Buy $105 call for $3.50
- Sell $95 put for $3.50
- **Net cost: $0 (zero-cost collar)**

**At expiration:**

- Stock at $110 → Call worth $5, put expires → **P&L: +$5 per share**
- Stock at $100 → Both expire → **P&L: $0**
- Stock at $90 → Put assigned, own stock at $95, now worth $90 → **P&L: -$5 per share**

### Bearish Risk Reversal (Synthetic Short Stock)

**Definition:** Sell OTM call + Buy OTM put, creating synthetic short exposure.

**Structure:**

- **Sell:** OTM call at strike $K_C$ (e.g., $105 call)
- **Buy:** OTM put at strike $K_P$ (e.g., $95 put)
- **Current stock:** $S_0 = 100$
- **Net premium:** Ideally $\approx 0$ (or small credit/debit)

**Position characteristics:**

- Delta: ~-1.0 (short stock equivalent)
- Vega: Long (bought put vega > sold call vega)
- Theta: Slightly negative (pay for put time value)
- Gamma: Negative near strikes

**Example:**

- Stock at $100
- Sell $105 call for $3.50 (collect)
- Buy $95 put for $3.50 (pay)
- **Net cost: $0**

**At expiration:**

- Stock at $110 → Call assigned, must deliver → **P&L: -$5 per share**
- Stock at $100 → Both expire → **P&L: $0**
- Stock at $90 → Put worth $5 → **P&L: +$5 per share**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/risk_reversal_payoff.png?raw=true" alt="risk_reversal" width="700">
</p>
**Figure 1:** Payoff diagrams for bullish (synthetic long) and bearish (synthetic short) risk reversals, showing linear stock-like P&L profiles with no upfront cost but obligations on both sides.

---

## Economic Interpretation: Trading the Skew Premium

**Beyond the basic definition, understanding what risk reversals REALLY are economically:**

### Why Does Skew Exist?

**The fundamental market asymmetry:**

In most equity markets, OTM puts trade at HIGHER implied volatility than OTM calls at equivalent distance from spot. This creates the "volatility smile" or "skew."

**Reasons for equity skew:**

1. **Demand imbalance:** Investors buy puts for protection, sell calls for income
2. **Leverage effect:** Stock drops → Leverage increases → Realized vol increases
3. **Crash fear:** Markets fall faster than they rise (negative skewness)
4. **Supply/demand:** Put buyers willing to overpay for insurance

**Quantifying skew:**

$$
\text{Skew} = IV_{\text{Put}}(K_P) - IV_{\text{Call}}(K_C) > 0 \quad \text{(typically 3-8 vol points)}
$$

**Example:**
- Stock at $100
- $95 put IV: 28%
- $105 call IV: 22%
- **Skew: 6% (95 put richer than 105 call)**

### The Risk Reversal as Skew Arbitrage

**When you construct a zero-cost risk reversal:**

$$
\underbrace{C(K_C, \sigma_C)}_{\text{Buy call at lower IV}} = \underbrace{P(K_P, \sigma_P)}_{\text{Sell put at higher IV}}
$$

**What you're really doing:**

1. **Selling expensive volatility** (the put at 28% IV)
2. **Buying cheap volatility** (the call at 22% IV)
3. **Creating delta-one position** with skew exposure
4. **Profit if:** Skew flattens, call IV rises, or put IV falls

**Formal decomposition:**

$$
\begin{align}
\text{RR P&L} &= \underbrace{\Delta \cdot \Delta S}_{\text{Directional}} + \underbrace{\text{Vega}_{\text{net}} \cdot \Delta \sigma_{\text{avg}}}_{\text{Vol level change}} \\
&+ \underbrace{\text{Skew sensitivity} \cdot \Delta \text{Skew}}_{\text{Smile shape change}} + \underbrace{\Theta \cdot t}_{\text{Time decay}}
\end{align}
$$

### Put-Call Parity and Synthetic Positions

**Risk reversal creates synthetic stock via put-call parity:**

$$
S + P - C = Ke^{-rT}
$$

**Rearranging:**

$$
S = C - P + Ke^{-rT}
$$

**For zero-cost risk reversal where $C = P$:**

$$
\text{Synthetic Stock} = \underbrace{C - P}_{\text{=0}} + K \approx S_0
$$

**This means:**
- **Long call + Short put ≈ Long stock**
- **Short call + Long put ≈ Short stock**

---

## Key Terminology

**Risk Reversal:**

- Specific name for call-put combinations with opposite positions
- Also called: collar, fence, combo, synthetic long/short
- Always involves one long, one short option

**Skew:**

- Difference in IV between OTM puts and OTM calls
- Typically measured at 25-delta or fixed strikes
- Positive skew: Puts more expensive than calls (equity markets)
- Negative skew: Calls more expensive than puts (rare, sometimes commodities)

**Zero-Cost Collar:**

- Risk reversal constructed with net premium = $0
- Strikes chosen to balance call purchase with put sale
- Also called "costless collar" or "zero-premium fence"

**25-Delta Risk Reversal:**

- Market convention: Use 25-delta put and 25-delta call
- Quoted as: "25RR = X vol points"
- Example: "AAPL 1M 25RR = +3.5%" means 25-delta put IV is 3.5% higher than 25-delta call IV

---

## Why Trade Risk Reversals?

**Use cases for risk reversals:**

### 1. Directional View with Zero Cost

**Scenario:** Bullish on NVDA but don't want to deploy $50,000 for 100 shares

**Trade:**
- Buy $550 call for $25
- Sell $500 put for $25
- **Net cost: $0**

**Outcome:**
- Stock at $600 → Call worth $50, P&L = $50/share ($5,000 total)
- Stock at $550 → Both expire, P&L = $0
- Stock at $480 → Put assigned, own 100 shares at $500, now worth $480 → P&L = -$20/share (-$2,000)

**Why this works:**
- No upfront capital required
- Full stock-like exposure above $500
- Defined risk below $500 (own stock at $500)

### 2. Skew Monetization

**Scenario:** Equity markets overpricing downside protection, underpricing upside

**Observation:**
- SPY $95 put (5% OTM): IV = 20%
- SPY $105 call (5% OTM): IV = 14%
- **Skew = 6% (rich put, cheap call)**

**Trade:**
- Sell $95 put for $4.20
- Buy $105 call for $2.50
- **Net credit: $1.70 (get paid to enter!)**

**Outcome if skew normalizes:**
- Skew reduces to 3% (historical average)
- Put IV drops 1.5%, call IV rises 1.5%
- Position gains from vega even if SPY unchanged
- **Plus collected $1.70 upfront**

---

## Greeks Behavior

### Delta: Stock-Like Directional Exposure

**Bullish risk reversal delta:**

$$
\Delta_{\text{RR}} = \Delta_{\text{call}} - \Delta_{\text{put}} \approx +1.0
$$

**Example:**
- Buy $105 call: $\Delta = +0.52$
- Sell $95 put: $\Delta = -0.48$
- **Net delta: +1.00** (exactly like owning 100 shares)

### Vega: Short Volatility Exposure (Bullish RR)

**Vega asymmetry:**

$$
\text{Vega}_{\text{RR}} = \text{Vega}_{\text{call}} - \text{Vega}_{\text{put}} < 0 \quad \text{(net short)}
$$

**Why short vega?**

- Puts have HIGHER vega than calls (due to skew)
- You sold put (short high vega), bought call (long low vega)
- Net effect: Short vega

**Example:**
- $105 call vega: +0.15
- $95 put vega: +0.22
- **Net vega: -0.07** (lose $7 if IV rises 1%)

### Skew Vega: The Hidden Greek

**For bullish RR:**

- If skew FLATTENS (put IV ↓, call IV ↑): **Gain**
- If skew STEEPENS (put IV ↑, call IV ↓): **Loss**

**Example: Market crash fear increases**
- Puts get bid up: 25% → 30% IV (+5%)
- Calls unchanged: 20% IV
- Skew: 5% → 10% (+5% steepening)

**Impact on bullish RR:**
- Short $95 put: Loss from higher IV = -$110
- Long $105 call: No change = $0
- **Net loss: -$110** (even if stock unchanged)

**This is why risk reversals are SKEW TRADES, not just directional!**

---

## Common Pitfalls

### 1. Ignoring Skew Changes

**The mistake:**

"I'm bullish on AAPL, so I'll do a bullish risk reversal. Simple directional bet!"

**What you missed:**

Risk reversals are SKEW trades, not pure directional trades. You're short vega AND short skew.

**Example:**
- AAPL rallies +5% (correct directional call)
- But market selloff increases overall fear
- Skew steepens: 4% → 8%
- **Your P&L: -$200** (despite being right on direction!)

### 2. Treating as "Free" Stock

**The mistake:**

"Zero cost = free stock exposure, no risk!"

**What you missed:**

- **Put assignment risk:** Forced to buy stock at strike
- **No dividends:** Miss income from actual stock
- **Expiration risk:** Must close or roll
- **Margin requirements:** Options margin can be substantial

### 3. Assignment Risk

**Scenario:** Holding bullish RR into expiration

**Setup:**
- Buy $105 call, sell $95 put
- Stock at $94.50 on expiration day

**What happens:**
- Put is $0.50 ITM → **Automatic assignment**
- You now own 100 shares at $95
- Stock at $94.50 → Immediate -$50 loss
- **Plus:** Overnight risk (stock could gap down Monday)

**Lesson:** Close risk reversals before expiration to avoid assignment risk.

---

## Risk Management Rules

**Essential guidelines:**

### Position Sizing

**Rule of thumb:**

$$
\text{Position Size} = \frac{\text{Max Loss Tolerance}}{\text{Put Strike}}
$$

**Example:**

- $100,000 account
- 10% max loss per trade = $10,000
- Put strike = $95
- **Max size: 1 contract (100 shares × $95 = $9,500 potential assignment)**

### Exit Rules

**Set upfront:**

- **Profit target:** +25% on stock move
- **Stop loss:** Stock reaches put strike - $2
- **Time stop:** Close at 7 days to expiry (avoid assignment)
- **Skew stop:** Exit if skew steepens >3%

---

## Real-World Examples

### Example 1: NVDA Bullish RR (Successful Trade)

**Setup (July 2024):**

- NVDA at $120
- AI boom driving stock, but expensive to buy
- Want exposure without capital outlay

**Trade:** Bullish risk reversal (3-month expiry)

- Buy $130 call for $8.50
- Sell $110 put for $8.50
- **Net cost: $0**

**Outcome (September 2024):**

- NVDA rallies to $140 on strong AI demand
- $130 call now worth $10
- $110 put expires worthless
- **Profit: $10 per share ($1,000 per contract)**

**Lesson:** Zero-cost directional trade can generate substantial returns.

### Example 2: SPY Skew Steepening Loss

**Setup (January 2024):**

- SPY at $480
- Bullish RR: Buy $490 call, sell $470 put (zero cost)

**Outcome (February 2024):**

- Market selloff: SPY → $460 (-4.2%)
- Skew steepens: 4% → 9%
- **P&L:**
  - Delta: -$20
  - Skew impact: -$350
  - **Total: -$370 per contract**

**Lesson:** Bullish RR is SHORT skew. Skew steepening hurts badly.

---

## What to Remember

### Core Concept

**Risk reversals create synthetic stock positions:**

$$
\text{Bullish RR} = \text{Long Call} + \text{Short Put} \approx \text{Long Stock}
$$

- Typically zero net premium
- Stock-like delta exposure  
- Short vega (bullish RR) or long vega (bearish RR)
- Direct skew sensitivity
- Assignment risk on short option

### The Greeks

- **Delta:** ≈±1.0 (stock-like)
- **Gamma:** Positive at long option, negative at short option
- **Theta:** Slightly positive (bullish RR)
- **Vega:** Negative (bullish RR), positive (bearish RR)
- **Skew sensitivity:** HIGH - this is a skew trade!

### When to Use

**Bullish RR when:**

- Bullish directional view
- Limited capital available
- Skew is rich (high put IV)
- Comfortable owning stock at put strike
- IV expected to decrease

**Don't use when:**

- Skew at historical lows
- Insufficient capital for assignment
- Near ex-dividend dates
- As permanent stock replacement

### Common Mistakes

1. Ignoring skew levels before entering
2. Treating as "free" stock
3. Holding through expiration
4. Using bullish RR as hedge (wrong direction!)
5. Forgetting dividend impact
6. Over-sizing based on "zero cost"

### Final Wisdom

> "Risk reversals are deceptively simple - just a call and a put. But you're trading three things simultaneously: direction, volatility level, and skew. Ignore any one of these and you'll get hurt. Remember: it's NOT free stock. It's a financed position with embedded skew exposure. Respect the skew."

**Key to success:**

- Monitor skew levels (percentiles, historical context)
- Size for assignment risk, not "zero cost"
- Close before expiration (avoid assignment nightmares)
- Use when skew is in your favor
- Have exit plan for both profits and losses 📊🎯
