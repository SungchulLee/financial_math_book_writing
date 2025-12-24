# Diagonal Spreads

**Diagonal spreads** are option strategies where you **buy and sell options of the same type** (calls or puts) with **different strike prices AND different expiration dates**. They combine the ideas of **vertical spreads (different strikes)** and **calendar spreads (different expirations)** to create positions that can profit from **time decay, direction, and/or volatility changes** with **defined (or mostly-defined) risk**.

---

## The Core Insight

**The fundamental idea:**
- Options closer to expiration decay faster (higher theta)
- Options farther out decay slower (lower theta)
- So you can **own a longer-dated option** and **sell a shorter-dated option** against it
- Repeatedly “rent out” the short-term option premium
- Keep some directional exposure via strike choices
- Often reduces cost vs. buying a long option outright

**The key equation (intuition):**
\[
\text{Edge} \approx \text{Theta collected on short} - \text{Theta paid on long}
\]
You’re essentially betting:
> “Time decay will work for me, and the underlying won’t move too far against my structure before I can manage it.”

---

## What Is a Diagonal Spread?

### The Structure

A diagonal spread uses:
- **Same option type**: call/call or put/put
- **Different strikes**: \(K_1 \neq K_2\)
- **Different expirations**: \(T_1 \neq T_2\)

**Typical construction (most common):**
- **BUY** a longer-dated option (back month)
- **SELL** a shorter-dated option (front month)

This is often called a **diagonal calendar**.

---

## Why Diagonals Exist

### 1. Turn Time Decay into an Asset
Long options pay theta.
But diagonals can be structured so the **short option’s theta** helps offset (or exceed) what you pay on the long option.

### 2. Flexible Directional Bias
By choosing strikes:
- **Bullish diagonal (calls)**: long call is ITM/ATM, short call is OTM
- **Bearish diagonal (puts)**: long put is ITM/ATM, short put is OTM

### 3. Capital Efficiency (Key Use Case)
A major practical diagonal is the **Poor Man’s Covered Call (PMCC)**:
- A long-dated ITM call replaces owning 100 shares
- You sell short-dated calls against it for income

---

## Types of Diagonal Spreads

### 1) Call Diagonal (Bullish / Income)
**Structure:**
- Buy a longer-dated call (often ITM)
- Sell a shorter-dated call (often OTM)

**Goal:** collect short-call premium while keeping bullish upside.

### 2) Put Diagonal (Bearish / Income)
**Structure:**
- Buy a longer-dated put (often ITM)
- Sell a shorter-dated put (often OTM)

**Goal:** collect short-put premium while keeping bearish exposure.

### 3) Neutral / Range Diagonal
Strikes chosen closer to spot, aiming to profit primarily from **time decay** and **mean reversion**, but this is more sensitive and requires tighter management.

---

## The Portfolio

### Call Diagonal (generic)
\[
\Pi = C(S, K_{\text{long}}, T_{\text{long}}) - C(S, K_{\text{short}}, T_{\text{short}})
\]
where \(T_{\text{long}} > T_{\text{short}}\).

### Put Diagonal (generic)
\[
\Pi = P(S, K_{\text{long}}, T_{\text{long}}) - P(S, K_{\text{short}}, T_{\text{short}})
\]
where \(T_{\text{long}} > T_{\text{short}}\).

**Greeks (typical):**
- **Delta:** depends on strikes; usually directional
- **Theta:** can be **positive** (if short theta dominates)
- **Vega:** often **positive-ish** (because you’re net long longer-dated vol)
- **Gamma:** usually small vs. pure short-term positions, but short leg can create assignment/pin risk near expiry

---

## Concrete Example 1: Bullish Call Diagonal (PMCC Style)

**Setup:**
- Stock at \(S = 100\)
- You’re moderately bullish, but want income

**Trade:**
- Buy 90-day **$90 call** (ITM) for **$14**
- Sell 30-day **$105 call** (OTM) for **$2**

**Net debit:** \(14 - 2 = 12\) (=$1,200 per spread)

**Intuition:**
- The long ITM call behaves like stock (high delta)
- The short OTM call brings in premium and decays quickly
- If the short expires worthless, you can sell another one next month

**Key outcomes at the short expiration (30 days):**
- If stock is below $105: short expires worthless → keep premium, continue
- If stock rises above $105: short may be assigned → you manage by rolling/closing

---

## Concrete Example 2: Bearish Put Diagonal

**Setup:**
- Stock at \(S = 100\)
- You expect mild decline or sideways, want bearish tilt

**Trade:**
- Buy 90-day **$110 put** (ITM) for **$13**
- Sell 30-day **$95 put** (OTM) for **$2**

**Net debit:** \(13 - 2 = 11\)

**Goal:**
- If stock stays above $95: short put decays → keep premium
- If stock drops toward $95: position gains delta, but manage assignment risk

---

## Strike Selection Strategy

### Long Leg (Back Month)
**Common approach:**
- Choose **ITM** (especially for PMCC)
  - Higher delta (more stock-like)
  - Less theta decay per day (relative)
  - More intrinsic value, less “wasting” time value

**Rule of thumb (practitioner-style):**
- Long call delta ~ **0.70–0.85** for PMCC-style diagonals
- Long put delta ~ **-0.70 to -0.85** for bearish diagonals

### Short Leg (Front Month)
**Common approach:**
- Choose **OTM** at a strike where you’re “willing” to cap near-term move
- You want meaningful premium but not too close to the money

**Rule of thumb:**
- Short call delta ~ **0.20–0.35**
- Short put delta ~ **-0.20 to -0.35**

---

## Time Frame Selection

### Typical expirations
- Long leg: **60–180 days**
- Short leg: **20–45 days**

**Why this works:**
- The short leg has relatively high theta decay
- The long leg is more stable, giving you time to adjust

**PMCC preference:**
- Long leg often **90–180 days** (or LEAPS 1–2 years for more stability)
- Short leg often **~30–45 days** and rolled repeatedly

---

## Position Management

### 1) Close or Roll the Short Leg
If the short option is:
- **Profitable early** (e.g., you’ve captured 50–80% of its premium), consider buying it back and reselling a new one.
- **Threatened** (stock approaching short strike), you can:
  - **Roll up and out** (calls) / **roll down and out** (puts)
  - Convert the position into a different structure (e.g., vertical)
  - Close the entire diagonal

### 2) Avoid Holding the Short Leg into Expiration (Often)
Near expiration:
- gamma risk increases
- pin risk increases
- assignment becomes more likely

Many traders close/roll with **~7–14 days** left, especially if the short is near the money.

### 3) Assignment Handling (Important)
If a short call gets assigned, you may end up short shares.
If a short put gets assigned, you may end up long shares.

**Practical approach:**
- manage by rolling before assignment becomes likely
- avoid short options that are deep ITM near expiry unless you intend assignment

---

## Pros and Cons

### Diagonals — Advantages ✓
**1. Flexible design**
- Can be bullish, bearish, or neutral-ish

**2. Can generate income**
- Short leg premium can offset long leg cost

**3. Better capital efficiency**
- Especially PMCC: stock-like exposure with less capital than buying shares

**4. Often improved “cost basis” over time**
- Repeated short premium can reduce effective cost of the long option

### Diagonals — Disadvantages ✗
**1. More moving parts**
- Strike + expiration choices matter a lot

**2. Assignment and pin risk on the short leg**
- Especially near expiration

**3. Not fully defined risk in practice (sometimes)**
- If assignment happens unexpectedly, you can temporarily hold stock exposure
- Still manageable, but requires comfort with mechanics

**4. Directional whipsaws**
- Sudden moves can hurt if short leg gets challenged and long leg loses value (or IV shifts)

---

## Common Mistakes

### 1) Buying a Long Leg with Too Little Time
If the long option expires soon, theta decay can overwhelm the strategy.
**Fix:** use a longer-dated long leg (60–180 days or more).

### 2) Selling the Short Leg Too Close to the Money
You collect more premium but increase assignment risk and cap upside too aggressively.
**Fix:** start with OTM short strikes and adjust gradually.

### 3) Holding the Short Leg Too Close to Expiration
Pin risk and gamma explode.
**Fix:** roll/close earlier (commonly 7–14 days remaining).

### 4) Ignoring Implied Volatility
If IV collapses, long leg can lose value.
**Fix:** avoid overpaying for the long leg; consider entering after volatility spikes when appropriate.

### 5) Over-sizing Because It “Feels Covered”
PMCC is not identical to a covered call.
Your long call can lose value sharply.
**Fix:** size conservatively and treat it as an options position with real risk.

---

## When to Use Diagonals

### Best conditions
- You have a **directional bias** (mild/moderate)
- You want to **benefit from theta** (short leg decay)
- You’re comfortable managing rolls and avoiding assignment surprises

### Avoid when
- Big binary event risk inside the short leg (earnings, FDA, etc.)
- You cannot monitor or manage assignment/rolls
- Liquidity is poor (wide bid-ask spreads)

---

## Summary

Diagonal spreads are a powerful “hybrid” strategy:
- **Directional exposure** from strike selection
- **Income** from selling short-term options
- **Time-structure advantage** from faster decay in the front month

They’re especially useful as a next step after:
- long calls/puts,
- covered calls/cash-secured puts,
- and vertical spreads.
