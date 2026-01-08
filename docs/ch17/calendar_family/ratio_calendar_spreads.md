# Ratio Calendar Spreads

**Ratio calendar spreads** are strategies where you use **unequal numbers of contracts** across different expiration dates, creating asymmetric positions that can enhance returns, reduce cost, or create unique risk/reward profiles by trading both term structure differences and quantity ratios simultaneously.





---

## The Core Insight

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/ratio_calendar_spreads_greeks.png?raw=true" alt="ratio_calendar_spreads_greeks" width="700">
</p>
<p align="center"><em>Figure 1: Greek exposures of ratio calendar spreads showing theta enhancement (1x2) vs. vega leverage (2x1) profiles</em></p>

**The fundamental idea:**

- Standard calendars use 1:1 ratio (sell 1 front, buy 1 back)
- But what if you **sell MORE front month options** than you buy back month?
- Or **buy MORE back month** than you sell front month?
- **Solution:** Use RATIOS to modify the payoff structure
- Collect more theta (1x2, 1x3 ratios)
- Or reduce cost and gain leverage (2x1, 3x1 ratios)
- Creates a "volatility ratio structure" with enhanced or reduced theta

**The key equation:**

$$
\text{Ratio Calendar} = n_{\text{back}} \times V_{\text{back}}(T_{\text{back}}) - n_{\text{front}} \times V_{\text{front}}(T_{\text{front}})
$$

where $n_{\text{back}} \neq n_{\text{front}}$ (the ratio is not 1:1)

**You're essentially betting: "I want to adjust my theta/vega exposure by using unequal contract counts, trading term structure with leverage or enhanced income."**

---

## What Is a Ratio Calendar?

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/ratio_calendar_spreads_management.png?raw=true" alt="ratio_calendar_spreads_management" width="700">
</p>
<p align="center"><em>Figure 2: Position management framework for ratio calendars including adjustment triggers and risk monitoring</em></p>

**Before understanding ratio calendars, we need to recall standard calendars:**

### 1. Quick Standard Calendar Recap

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/ratio_calendar_spreads_payoff.png?raw=true" alt="ratio_calendar_spreads_payoff" width="700">
</p>
<p align="center"><em>Figure 3: Payoff diagrams comparing 1x2 (unlimited upside risk) vs. 2x1 (defined risk) structures</em></p>

**Standard 1:1 calendar spread:**

- Sell 1 front month option
- Buy 1 back month option  
- Same strike
- Same number of contracts
- Profits from time decay + term structure

**Limitations of 1:1 calendars:**

- Theta collection limited by 1:1 ratio
- Capital commitment fixed
- Risk/reward ratio predetermined
- No leverage or income enhancement

**The ratio calendar solution:**

**Two main types:**

**1. Front-heavy ratios (1x2, 1x3):**

- Sell MORE front month than back month
- Example: Buy 1 back, Sell 2 front
- **Enhanced theta collection**
- Lower net cost (or even credit)
- But additional risk if stock moves

**2. Back-heavy ratios (2x1, 3x1):**

- Buy MORE back month than sell front
- Example: Buy 2 back, Sell 1 front
- **Reduced net cost**
- More vega exposure
- Leveraged term structure bet

---

## The Structure

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/ratio_calendar_spreads_ratio_comparison.png?raw=true" alt="ratio_calendar_spreads_ratio_comparison" width="700">
</p>
<p align="center"><em>Figure 4: Ratio comparison showing theta collection vs. capital efficiency trade-offs across different ratios</em></p>

### 1. Basic Ratio Calendar

**Front-heavy ratio (1x2 - most common):**

**Components:**

- Buy 1 back month option at strike $K$
- Sell 2 front month options at strike $K$
- Net: Often **small debit or even credit**

**Example:**

- Stock at $100
- Buy 1 three-month $100 call @ $5.50
- Sell 2 one-month $100 calls @ $3.00 each
- Net: $5.50 - $6.00 = **-$0.50 credit** (receive $50)

**Back-heavy ratio (2x1):**

**Components:**

- Buy 2 back month options at strike $K$
- Sell 1 front month option at strike $K$
- Net: **Larger debit** than 1:1

**Example:**

- Stock at $100
- Buy 2 three-month $100 calls @ $5.50 each = $11.00
- Sell 1 one-month $100 call @ $3.00
- Net: $11.00 - $3.00 = **$8.00 debit**

### 2. The Visual

**1x2 Ratio Calendar (Front-heavy):**

```
              1x2 Ratio Calendar
    Profit
      ↑
   +$300|      /‾‾\
      0 |____/      \___
      - |              \
      - |               \___
  Loss  |                   \___
        |________________________
        $95  $100  $105  $110  $115
             ↑
           Strike
        (short 2, long 1)
```

**Key features:**

- Maximum profit at strike
- **Unlimited risk** on upside (naked short call exposure)
- Profit if stays near strike
- Enhanced theta from extra short

**2x1 Ratio Calendar (Back-heavy):**

```
              2x1 Ratio Calendar
    Profit
      ↑
   +$500|           /‾‾‾‾
   +$300|        /‾‾
      0 |______/
      - |    
  Loss  |
        |________________________
        $95  $100  $105  $110  $115
             ↑
           Strike
        (long 2, short 1)
```

**Key features:**

- Profit increases with upward move
- Limited downside (max loss = net debit)
- Less theta but more vega
- Leveraged term structure exposure

---

## The Portfolio

### 1. Front-Heavy Ratio (1x2)

$$
\Pi_{1x2} = V_{\text{back}}(S, K, T_{\text{back}}) - 2 \times V_{\text{front}}(S, K, T_{\text{front}})
$$

where:

- $V_{\text{back}}$ = Long back month option (1 contract)
- $V_{\text{front}}$ = Short front month option (2 contracts)
- $T_{\text{back}} > T_{\text{front}}$

**Greeks (typical):**

- **Delta:** Approximately neutral near strike, but changes with price
- **Theta:** **Strongly positive** (two shorts vs one long)
- **Vega:** Can be **negative** (net short vega if front vol > back vol weighted)
- **Gamma:** **Negative** (short gamma from extra front month)

**Portfolio Greeks formulas:**

$$
\Delta_{\text{net}} = \Delta_{\text{back}} - 2\Delta_{\text{front}}
$$

$$
\Theta_{\text{net}} = \Theta_{\text{back}} + 2|\Theta_{\text{front}}| > 0
$$

$$
\mathcal{V}_{\text{net}} = \mathcal{V}_{\text{back}} - 2\mathcal{V}_{\text{front}}
$$

$$
\Gamma_{\text{net}} = \Gamma_{\text{back}} - 2\Gamma_{\text{front}} < 0
$$

**Critical risk:**

- **Unlimited upside risk** from the extra naked short call
- Similar to short straddle risk on one side
- Requires management or hedging

### 2. Back-Heavy Ratio (2x1)

$$
\Pi_{2x1} = 2 \times V_{\text{back}}(S, K, T_{\text{back}}) - V_{\text{front}}(S, K, T_{\text{front}})
$$

where:

- $V_{\text{back}}$ = Long back month option (2 contracts)
- $V_{\text{front}}$ = Short front month option (1 contract)
- $T_{\text{back}} > T_{\text{front}}$

**Greeks (typical):**

- **Delta:** Directional (depends on strikes, usually positive for calls)
- **Theta:** **Positive** but less than 1x2 (one short vs two longs)
- **Vega:** **Strongly positive** (net long vega from extra back month)
- **Gamma:** **Positive** (net long gamma from extra back month)

**Portfolio Greeks formulas:**

$$
\Delta_{\text{net}} = 2\Delta_{\text{back}} - \Delta_{\text{front}} > 0
$$

$$
\Theta_{\text{net}} = 2\Theta_{\text{back}} + |\Theta_{\text{front}}|
$$

$$
\mathcal{V}_{\text{net}} = 2\mathcal{V}_{\text{back}} - \mathcal{V}_{\text{front}} > 0
$$

$$
\Gamma_{\text{net}} = 2\Gamma_{\text{back}} - \Gamma_{\text{front}} > 0
$$

**Risk profile:**

- **Limited downside** (max loss = net debit paid)
- Unlimited upside potential
- Leveraged vega exposure
- More expensive than 1:1

---

## Economic

**Understanding what ratio calendars REALLY represent economically:**

### 1. The Core Economic Trade-Off

**Ratio calendars modify the fundamental calendar spread trade-off through leverage:**

$$
\text{1x2 P\&L} = \underbrace{2\Theta_{\text{front}} - \Theta_{\text{back}}}_{\text{Enhanced theta}} - \underbrace{\text{Unlimited Risk}}_{\text{Cost of leverage}}
$$

$$
\text{2x1 P\&L} = \underbrace{2\mathcal{V}_{\text{back}} - \mathcal{V}_{\text{front}}}_{\text{Leveraged vega}} - \underbrace{\text{Higher Capital}}_{\text{Cost of leverage}}
$$

**Economic meaning:**

**For 1x2 (Front-Heavy):**

You're essentially **selling naked volatility** while partially hedging with long back month. This creates:
- Maximum theta extraction (collecting premium on 2× contracts)
- Unlimited upside risk (the extra naked short call/put)
- Net short vega exposure (opposite of standard calendar!)

**Analogy:** Like running a rental property (collect rent = theta) but being short fire insurance (unlimited risk if house burns down).

**For 2x1 (Back-Heavy):**

You're creating **leveraged vega exposure** similar to buying options on margin:
- 2× the vega of standard calendar for only ~1.6× the cost
- Defined risk (max loss = debit paid)
- Minimal theta benefit

**Analogy:** Like using leverage to buy 2 houses while renting out 1 to offset costs.

### 2. The Theta-Risk Trade-off Spectrum

**The fundamental insight:**

$$
\text{Theta Collection} \propto \text{Risk Taken}
$$

```
Ratio Spectrum:
                                    
2x1  ←──────── 1.5x1 ────── 1x1 ────── 1x1.5 ──────→  1x2
  |              |           |            |             |
  ↑              ↑           ↑            ↑             ↑
Low θ        Balanced     Standard    Enhanced     Maximum θ
Defined      Defined      Defined     Semi-undef   Unlimited
Risk         Risk         Risk        Risk         Risk

Vega: +++      ++           +            -            --
Theta: 0       +            +            ++           +++
```

**Why the trade-off exists:**

**Economic principle:** No free lunch
- More theta collection → Must accept more risk
- More risk reduction → Must accept less theta or pay more premium
- Ratios let you choose your position on this spectrum

### 3. The Leverage Multiplier Effect

**For 1x2 ratio:**

$$
\text{Theta Multiplier} = \frac{2\Theta_{\text{front}} - \Theta_{\text{back}}}{\Theta_{\text{front}} - \Theta_{\text{back}}} \approx 1.5\text{-}2.0\times
$$

Example:
- 1x1 calendar: Net theta = +$10/day
- 1x2 calendar: Net theta = +$30/day
- **Theta enhancement: 3×**

But with cost:
- 1x1 risk: Limited (net debit)
- 1x2 risk: **Unlimited** (naked short exposure)

**For 2x1 ratio:**

$$
\text{Vega Multiplier} = \frac{2\mathcal{V}_{\text{back}} - \mathcal{V}_{\text{front}}}{\mathcal{V}_{\text{back}} - \mathcal{V}_{\text{front}}} \approx 1.8\text{-}2.2\times
$$

Example:
- 1x1 calendar: Net vega = +0.10
- 2x1 calendar: Net vega = +0.45
- **Vega enhancement: 4.5×**

Capital efficiency:
- 2× vega exposure for ~1.6× the capital
- Capital efficiency: 1.25×

### 4. Why Markets Allow This Structure

**Supply and demand imbalances:**

**For 1x2 (collecting theta):**

Market participants who create demand:
- **Retail investors:** Buy protective puts/calls
- **Institutions:** Buy tail hedges
- **Speculators:** Buy lottery tickets on earnings

This buying pressure creates **inflated front-month premiums** (especially near events), which ratio calendar sellers can harvest.

**Historical edge:** Front-month options trade at IV premium due to:
- Event uncertainty (earnings, Fed, etc.)
- Higher demand for short-term protection
- Roll dynamics (futures/options rolling)

**For 2x1 (leveraged vega):**

When is this structure valuable?
- **Low IV environments:** When IV is suppressed, buying 2× back month options positions you for mean reversion
- **Term structure flat/inverted:** Abnormal term structures create entry opportunities
- **Pre-volatility regime change:** Before IV expansion cycles

**Economic edge:** Back-month options are often "cheaper" on a vega-per-dollar basis due to:
- Less trading volume (less price discovery)
- Lower demand (fewer hedgers)
- Time decay offset (lower theta per vega unit)

### 5. The Volatility Risk Premium in Ratios

**Enhanced vol risk premium capture (1x2):**

Standard calendar collects vol risk premium:
$$
\text{Premium}_{\text{calendar}} = (\sigma^{\text{impl}}_{\text{front}} - \sigma^{\text{impl}}_{\text{back}}) \times \text{Vega}
$$

Ratio calendar amplifies this:
$$
\text{Premium}_{1x2} = 2 \times \sigma^{\text{impl}}_{\text{front}} - \sigma^{\text{impl}}_{\text{back}} \times \text{Vega}
$$

**Example:**
- Front IV: 30%, Back IV: 25%
- 1x1 calendar: Collects 5% vol differential
- 1x2 calendar: Collects (2×30% - 25%) = 35% **differential**

**But:** This 7× enhancement comes with unlimited risk if front month IV explodes.

### 6. Professional Institutional Perspective

**Institutional use cases:**

**1x2 Ratio Calendars:**
- **Market makers:** Collect theta while maintaining inventory
- **Volatility sellers:** Enhanced income strategies
- **Portfolio yield:** Generate monthly income on boring stocks

**Typical setup:**
- Run 20-30 ratio calendars simultaneously
- Diversified across sectors (correlation < 0.3)
- Total theta collection: $500-1000/day
- Risk management: Automated adjustment algorithms

**2x1 Ratio Calendars:**
- **Volatility traders:** Leverage low-IV environments
- **Macro funds:** Position for uncertainty increases
- **Event-driven funds:** Pre-position before catalysts

**Typical setup:**
- Concentrated positions (3-5 names)
- Higher conviction required
- Total vega exposure: $5-10k per 1% IV move
- Profit target: 40-80% of debit within 30-45 days

### 7. When Ratio Calendars Offer Edge

**1x2 edge exists when:**

1. **IVR > 50%:** Front month premiums elevated
2. **Stock range-bound:** Technical levels clear
3. **No binary events:** Earnings > 45 days away
4. **You can monitor daily:** Active management capability

**Expected value:** Positive due to theta collection exceeding average adjustment costs

**2x1 edge exists when:**

1. **IVR < 30%:** IV suppressed, room for expansion
2. **Term structure abnormal:** Flat or inverted
3. **Macro uncertainty building:** IV expansion catalysts forming
4. **Directional catalyst:** Non-binary positive developments

**Expected value:** Positive if IV expands 5+ points or term structure steepens significantly

Understanding these economic foundations helps recognize when ratio calendars offer genuine edge versus when you're taking on risk without adequate compensation.

---

## The P&L Formula

### 1. For 1x2 Front-Heavy Ratio

$$
\delta \Pi_{1x2} \approx \underbrace{2 \times \Theta_{\text{front}} - \Theta_{\text{back}}}_{\text{Enhanced theta (positive)}} + \underbrace{(2 \times \mathcal{V}_{\text{front}} - \mathcal{V}_{\text{back}}) \delta\sigma}_{\text{Net vega (often negative)}} + \underbrace{\Gamma \text{ P\&L}}_{\text{Usually negative gamma}}
$$

**Breaking it down:**

**1. Theta P&L (Primary Edge for 1x2)**

$$
\Theta_{\text{net}} = 2 \times |\Theta_{\text{front}}| - |\Theta_{\text{back}}|
$$

**Typically:**

- Two short front options: $2 \times (+\$20) = +\$40$ per day
- One long back option: $-\$10$ per day
- **Net theta: +$30 per day**

This is the main profit source for 1x2 ratios.

**2. Vega P&L (Can Be Negative!)**

$$
\mathcal{V}_{\text{net}} = \mathcal{V}_{\text{back}} - 2 \times \mathcal{V}_{\text{front}}
$$

**Example:**
- Back month vega: +0.35
- Front month vega: 0.25 each
- **Net: 0.35 - 2(0.25) = -0.15** (short vega!)

**Counterintuitive:** Unlike standard calendars, 1x2 can be **net short vega**.

**3. Gamma P&L (Negative)**

$$
\Gamma_{\text{net}} = \Gamma_{\text{back}} - 2 \times \Gamma_{\text{front}} < 0
$$

**Danger:** Net short gamma means large stock moves hurt position.

### 2. For 2x1 Back-Heavy Ratio

$$
\delta \Pi_{2x1} \approx \underbrace{2 \times \mathcal{V}_{\text{back}} \delta\sigma - \mathcal{V}_{\text{front}} \delta\sigma}_{\text{Leveraged vega (positive)}} + \underbrace{\Theta_{\text{net}} dt}_{\text{Minimal theta}} + \underbrace{\Gamma \text{ P\&L}}_{\text{Positive gamma}}
$$

**1. Vega P&L (Primary Edge)**

$$
\mathcal{V}_{\text{net}} = 2 \times \mathcal{V}_{\text{back}} - \mathcal{V}_{\text{front}}
$$

**Example:**
- Back month vega: 0.35 each
- Front month vega: 0.25
- **Net: 2(0.35) - 0.25 = +0.45** (strong long vega!)

**This is the play** - you want IV to increase.

**2. Theta P&L (Minimal)**

$$
\Theta_{\text{net}} = 2 \times \Theta_{\text{back}} + |\Theta_{\text{front}}|
$$

Often close to zero. Not the primary profit source.

**3. Gamma P&L (Positive)**

$$
\Gamma_{\text{net}} = 2 \times \Gamma_{\text{back}} - \Gamma_{\text{front}} > 0
$$

Benefits from movement, more forgiving than 1x2.

---

## Concrete Examples

### 1. Pension Duration Cut via Futures

**Setup (early March 2024):**

- AAPL at $180
- Range-bound $175-$185 for 4 weeks
- IV: Front 25%, Back 28%
- No earnings for 60 days

**The trade:**

- Sell 2x 30-day $180 calls @ $4.50 = $9.00
- Buy 1x 90-day $180 call @ $8.50
- **Net credit: $0.50** ($50 per spread)

**Position Greeks:**
- Theta: +$25/day
- Vega: -0.12 (net short vega)
- Gamma: -0.03 (net short gamma)

**Week 1-4 progression:**

| Week | Stock | Front Value | Back Value | Position Value | Theta Collected | P&L |
|------|-------|-------------|------------|----------------|-----------------|-----|
| 0 | $180 | $9.00 | $8.50 | +$0.50 | $0 | +$50 |
| 1 | $182 | $7.80 | $8.20 | +$0.60 | $175 | +$235 |
| 2 | $179 | $6.20 | $7.80 | +$0.40 | $350 | +$390 |
| 3 | $181 | $4.40 | $7.50 | +$2.70 | $525 | +$795 |
| 4 | $180 | $2.20 | $7.00 | +$4.30 | $700 | +$1,130 |

**Front expiration (Day 30):**

- Stock: $180.50
- Front calls expire near-worthless: $0.30 each
- Back call value: $6.80

**Final P&L:**
- Kept from fronts: $9.00 - $0.60 = $8.40
- Back call: Started $8.50, now $6.80 = -$1.70
- **Net: +$8.40 - $1.70 = +$6.70**

**Profit: $670 on $50 credit = 1,340% ROI**

**Why it worked:**
- Stock stayed in range
- Theta dominated
- No large moves (gamma didn't hurt)
- Managed conservatively

---

[I'll continue with more examples and complete sections. Due to length, let me append the critical Worst Case and Best Case scenarios now]

