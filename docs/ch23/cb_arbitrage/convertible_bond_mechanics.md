# Convertible Bond Mechanics and Valuation

> **Part 1 of 3** | See also: [Implementation](convertible_bond_arbitrage_implementation.md) | [Risk & Performance](convertible_bond_arbitrage_risk.md)

**Convertible bond arbitrage** is a strategy where you profit from mispriced embedded optionality by buying convertible bonds and hedging away the directional risk through short stock positions.

> **Prerequisites:** This section requires understanding of option pricing (Chapter 5: Black-Scholes), delta hedging and gamma mechanics (Chapter 6), and credit risk fundamentals. For the Merton model connection between equity volatility and credit spreads, see the equity-credit basis discussion in Section 23.4.2.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/convertible_bond_arbitrage_delta.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 1:** Convertible Bond Arbitrage Delta visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/convertible_bond_arbitrage_payoff.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 2:** Convertible Bond Arbitrage Payoff visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/convertible_bond_arbitrage_pnl.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 3:** Convertible Bond Arbitrage Pnl visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/convertible_bond_arbitrage_structure.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 4:** Convertible Bond Arbitrage Structure visualization.

---

## The Core Insight


**The fundamental idea:**

- A convertible bond is a hybrid security: part bond, part stock option

- It gives you: regular coupon payments + the option to convert to stock

- The embedded option often trades at a discount to similar exchange-traded options

- You can buy this "cheap option" and delta hedge to extract value

- Profit from the underpriced optionality

**The key equation:**

$$
\text{Convertible Bond} = \text{Straight Bond} + \text{Embedded Call Option}
$$

**You're essentially buying a discounted call option with bond financing!**

---

## What Is a Convertible Bond?


**Before understanding the arbitrage, you need to understand the instrument:**

### 1. The Basic Structure


**A convertible bond gives the holder:**

1. **Regular coupon payments** (like a normal bond)

         - Fixed interest rate (usually lower than non-convertible debt)

         - Paid semi-annually
   
2. **Principal repayment at maturity** (like a normal bond)

         - Face value returned if not converted
   
3. **Option to convert** into stock (the special feature!)

         - Convert each bond into a fixed number of shares

         - Conversion ratio determines how many shares

         - You can choose when to convert (up to maturity)

**Example:**

**ABC Corp Convertible Bond:**

- Face value: $1,000

- Coupon: 2% annually

- Maturity: 5 years

- Conversion ratio: 20 shares per bond

- Current stock price: $45

**What you get:**

- $20/year in coupons (2% × $1,000)

- Option to convert $1,000 bond → 20 shares

- Conversion price: $1,000 ÷ 20 = $50 per share

**When would you convert?**

- If stock goes to $60: Convert! Get 20 shares × $60 = $1,200 (vs. $1,000 bond)

- If stock stays at $45: Don't convert! Keep getting coupons and principal

**The convertible bond is essentially:**

- A bond (debt security) 

- PLUS a call option on the stock with strike = $50

---

## The Embedded Option


**This is CRUCIAL to understand:**

### 1. Decomposing the Convertible Bond


$$
\boxed{\text{Convertible Bond Value} = \text{Bond Floor} + \text{Conversion Option Value}}
$$

**1. Bond Floor (Straight Debt Value)**

- What the bond would be worth WITHOUT the conversion feature

- Present value of coupons + principal

- Determined by credit spread and interest rates

**Example:**

- $1,000 face value, 2% coupon, 5 years

- Company's straight debt trades at 5% yield

- Bond floor ≈ $870 (present value at 5% discount rate)

**2. Conversion Option Value**

- Value of the right to convert into stock

- This is essentially a call option!

- Strike price = conversion price ($50 in our example)

- Maturity = bond maturity (5 years)

**Example:**

- Stock at $45, strike $50, 5 years to expiration

- Using Black-Scholes with 30% vol: option worth ≈ $150

**Total convertible bond value:**

- Bond floor: $870

- Option value: $150

- **Theoretical value: $1,020**

**But in the market:**

- Convertible might trade at only $980!

- The embedded option is underpriced by $40

- **This is the arbitrage opportunity!**

---

## Why Is the Option Underpriced?


**Several reasons:**

### 1. Different Investor Bases


**Convertible bond investors:**

- Bond funds (fixed income mandates)

- May not fully appreciate option value

- Focus on yield and credit

**Option investors:**

- Equity derivatives traders

- Understand optionality

- But don't naturally buy bonds

**Result:** Embedded option trades at discount to exchange-traded equivalent

### 2. Structural Features


**Complexity:**

- Call provisions (issuer can force conversion)

- Put provisions (investor can sell back to issuer)

- Credit risk affects option value

- Hard to value precisely

**Liquidity:**

- Less liquid than straight bonds or options

- Liquidity discount

### 3. Supply/Demand Dynamics


**Issuance reasons:**

- Companies issue converts for cheaper financing

- Supply often exceeds demand from sophisticated arbitrageurs

- Creates structural discount

### 4. Forced Sellers


**Hedge fund redemptions:**

- During crises, hedge funds sell converts

- Price depression creates opportunities

- Similar to other arbitrage dislocations

---

## The Arbitrage Strategy


**Now we can understand the trade:**

### 1. The Basic Trade


**What you do:**

1. **Buy the convertible bond**

   - Get the underpriced embedded option

   - Get coupon income

   - Have credit risk

2. **Short the underlying stock (delta hedge)**

   - Hedge away directional risk

   - Maintain delta-neutral position

   - Like all strategies we've studied!

3. **Dynamically rebalance**

   - As stock moves, delta changes

   - Adjust short position

   - Harvest gamma (like gamma scalping)

4. **Hold position and collect returns**

   - Earn from underpriced option

   - Collect coupon income

   - Gamma scalping profits

   - Credit arbitrage if bond recovers

**The goal:** Extract value from the mispriced embedded option while hedging away risks you don't want (stock direction, interest rates).

---

## The Portfolio


Your convertible arbitrage portfolio consists of:

$$
\Pi = \text{Long Convertible Bond} + \text{Short Stock (delta hedge)} + \text{Other hedges}
$$

More precisely:

$$
\Pi = \text{CB}(S, t, r, \text{credit}) - \Delta \cdot S - \text{IR hedge}
$$

where:

- CB = Convertible bond value

- $\Delta$ = Delta of embedded option

- S = Stock price

- IR hedge = Interest rate hedge (optional)

**Why this structure?**

1. **Long convertible:** Get cheap embedded option + coupon income

2. **Short stock:** Hedge directional equity risk (delta)

3. **Interest rate hedge (optional):** Hedge duration risk

4. **Credit exposure:** Typically left unhedged (part of the bet)

**What you're exposed to:**

- ✓ Gamma (from embedded option - you want this!)

- ✓ Credit spread changes (you usually want tightening)

- ✓ Vega (volatility changes)

- ✗ Delta (hedged away)

- ✗ Interest rates (can hedge if desired)

---


---

## Economic Interpretation


**Understanding what convertible bond arbitrage REALLY represents economically:**

### 1. The Core Economic Trade-Off


Convertible bond arbitrage is fundamentally about **exploiting capital structure inefficiencies**. You're not just trading options—you're trading the **relationship between debt and equity**.

**What you're really doing:**

$$
\text{CB Arbitrage} = \text{Long Cheap Optionality} + \text{Delta Hedge} - \text{Carry Cost}
$$

**The no-arbitrage breakdown:**

$$
\text{Convertible Bond Value} = \underbrace{\text{Bond Floor}}_{\text{credit component}} + \underbrace{\text{Conversion Premium}}_{\text{equity option}}
$$

**Your trade:**

- **Buy underpriced optionality** (embedded call is cheaper than exchange-traded options)

- **Hedge directional risk** (short stock to neutralize delta)

- **Extract multiple alpha sources** (gamma scalping, credit spread, volatility, coupon income)

### 2. Why Convertible Bonds Exist


**The issuer's perspective (company issuing the bond):**

**Traditional high-yield bond:**

- Must pay 8-12% coupon

- No equity dilution

- Fixed obligation

**Convertible bond:**

- Pay only 2-4% coupon (much cheaper!)

- Give away option to convert (equity dilution if stock rises)

- **Trade-off:** Lower interest cost for potential dilution

**Economic rationale:**

- **Growth companies** with limited cash flow

- Want to **minimize interest expense**

- Willing to accept **future dilution** if stock price rises (success scenario)

- Investors accept lower coupon because they get equity upside

**Example:** Tesla issued convertible bonds in 2014-2017:

- Regular high-yield debt would cost: 8-10% coupon

- Convertible bonds issued at: 1.25-2.375% coupon

- **Saved hundreds of millions in interest**

- Stock price rose dramatically → bonds converted → shareholders diluted

- **But Tesla didn't care** (dilution at high prices is acceptable)

### 3. Why the Embedded Option Is Underpriced


**The mispricing mechanism:**

**Exchange-traded options (expensive):**

- Trade on liquid markets

- Subject to supply/demand

- Retail and institutional competition

- Market makers price efficiently

- **Implied volatility:** Often 30-40% for growth stocks

**Embedded option in convertible (cheap):**

- No separate market

- Priced by bond investors (not options traders!)

- **Bond investors** typically:

  - Focus on credit risk, not volatility

  - Don't dynamically hedge

  - Price option using **historical vol** (lower than implied)

  - Mis-estimate option value

- **Implied volatility equivalent:** Often 20-25% for same stock

**The arbitrage:**

- Embedded option priced at 20% vol

- Exchange options priced at 35% vol

- **Gap = 15 vol points** = Your edge!

**Why doesn't this close immediately?**

1. **Different investor bases:**

   - Convertible buyers: Credit investors (pension funds, insurance)

   - Option traders: Hedge funds, market makers

   - Limited overlap → pricing inefficiency persists

2. **Complexity:**

   - Not obvious how to arbitrage

   - Requires sophisticated modeling

   - Capital intensive (need to finance bond purchase)

3. **Structural impediments:**

   - Credit investors can't short stock

   - Equity options traders don't analyze bonds

   - Regulatory constraints (insurance companies have bond mandates)

### 4. The Five Profit Sources


**Unlike simple option strategies, convertible arbitrage has FIVE independent P&L sources:**

### 5. Gamma Scalping (Primary Source)


**The mechanism:**

Stock volatility → Delta changes → Rebalance → Buy low, sell high

**The mathematics:**

$$
\text{Gamma P&L} = \frac{1}{2}\Gamma \times (\text{Realized Vol})^2 \times S^2 \times dt
$$

**Intuition:**

- You're **long gamma** (from embedded call option)

- Stock moves around → You profit from rebalancing

- **Need:** Realized volatility to actually occur

**Example:**

- Convertible bond gamma: 0.10

- Stock at $50, moves $2 per day average

- Daily gamma P&L: $0.5 × 0.10 × $2² = **$0.20 per day**

- Annual: $0.20 × 250 = **$50 profit per $1,000 bond**

**Key insight:** This is the SAME mechanism as gamma scalping options, but you:

- Get it cheaper (embedded option underpriced)

- Get paid coupons (positive carry)

- Have credit upside (bond floor can increase)

### 6. Coupon Income (Unique to Converts)


**The steady income:**

Most strategies don't have positive carry. Convertibles do!

**Typical convertible:**

- Coupon: 1-4% annually

- Even after paying stock borrow cost (0.5-3%)

- **Net carry:** Often positive or near-zero

**Example:**

- Buy $1M face value convertible at par

- Coupon: 2.5% = $25,000/year

- Short stock borrow cost: 1.5% = -$15,000/year

- **Net positive carry: $10,000/year**

**This is HUGE** because:

- Most gamma scalping strategies bleed theta

- Here, you get paid while waiting for volatility!

- Reduces breakeven hurdle

### 7. Credit Spread Tightening


**The bond floor can rise:**

$$
\text{Bond Floor} = \sum_{t=1}^{T} \frac{\text{Coupon}_t}{(1+r+s)^t} + \frac{\text{Principal}}{(1+r+s)^T}
$$

Where $s$ = credit spread

**If credit spread narrows:**

- Bond floor increases

- Convert value increases

- **You profit** (even if stock doesn't move!)

**Example:**

- Company issues convert when credit spread = 600 bps (risky)

- Company improves operations

- Credit spread tightens to 300 bps

- Bond floor rises from $800 → $950

- **Profit: $150 per $1,000 face value**

**Historical edge:**

- Many converts issued by growth companies

- As companies mature → creditworthiness improves

- **Structural long credit bias profitable**

### 8. Volatility Expansion


**The vega component:**

$$
\text{Vega P&L} = \text{Vega} \times \Delta\sigma
$$

**You're long vega:**

- Embedded option has positive vega

- If implied volatility rises → option more valuable

- Convert price increases

**Example:**

- Tech selloff → VIX spikes

- Implied vol for growth stocks: 25% → 45%

- Vega = 0.30 per vol point

- **Profit: 0.30 × 20 = $6 per $1,000 face**

**But caution:**

- Vega exposure cuts both ways

- If vol collapses → you lose

- **2006-2007:** Vol crushed, hurt many CB arbitrage funds

### 9. Call Feature Extraction


**Many converts have issuer call options:**

**Structure:**

- Company can call (redeem) bond after 3-5 years

- Usually at 102-105% of par

- Forces conversion if in-the-money

**Your profit:**

- If company calls bond → forced conversion

- You capture **full parity** (intrinsic value)

- Plus call premium (102-105%)

**Example:**

- Convert trading at $1,100 (10% premium to parity $1,000)

- Company calls at $1,020

- **You receive minimum of parity ($1,000) or call price ($1,020)**

- Realize embedded option value immediately

### 10. Capital Structure Arbitrage


**Convertible arbitrage is really a form of capital structure arbitrage:**

**The capital stack:**

```
[Most Senior]

1. Senior Secured Debt

2. Senior Unsecured Debt

3. Subordinated Debt

4. **Convertible Bonds** ← You buy these

5. Preferred Stock

6. Common Stock ← You short this
[Most Junior]
```

**Your position:**

- **Long** subordinated debt (convert)

- **Short** common equity (stock)

- **Net:** Betting on credit improving relative to equity volatility

**Economic interpretation:**

- If company does well → credit improves (bond floor rises) + stock volatility profits

- If company struggles → bond has downside protection (you're long the bond!)

- **Asymmetric payoff:** Limited downside (bond floor), unlimited upside (gamma profits)

### 11. The Greeks Decomposition


**Unlike pure equity options, convertible bonds have HYBRID greeks:**

### 12. Delta (Equity Sensitivity)


$$
\Delta_{\text{convert}} = \frac{\partial V}{\partial S} = N(d_1) \times \text{Conversion Ratio}
$$

- Starts near 0 (out-of-money, bond-like)

- Increases to 1.0 (in-the-money, stock-like)

- **Your hedge:** Short $\Delta \times$ shares

### 13. Gamma (Convexity)


$$
\Gamma_{\text{convert}} = \frac{\partial^2 V}{\partial S^2} = \frac{n(d_1)}{S\sigma\sqrt{T}}
$$

- Highest when at-the-money

- **Source of rebalancing profits**

- Need realized volatility to monetize

### 14. Rho (Interest Rate Sensitivity)


$$
\rho_{\text{convert}} = \frac{\partial V}{\partial r} = \underbrace{-\text{Duration} \times V_{\text{bond}}}_{\text{bond component}} + \underbrace{\rho_{\text{option}}}_{\text{option component}}
$$

**Key complexity:**

- Rising rates → bond value decreases (negative rho from bond)

- Rising rates → option value increases (positive rho from option)

- **Net effect:** Depends on in-the-money-ness

**Hedging:**

- If out-of-money (bond-like) → Need to hedge interest rate risk

- Use Treasury futures or swaps

- Adds complexity and cost

### 15. Credit Spread Delta (Unique to Converts!)


$$
\Delta_{\text{credit}} = \frac{\partial V}{\partial s} < 0
$$

- Tighter spreads → higher bond floor

- Wider spreads → lower bond floor

- **Your exposure:** Long credit (want spreads to tighten)

**Risk:** If company credit deteriorates → bond floor collapses → lose money even if delta hedged!

### 16. Vega (Volatility Sensitivity)


$$
\nu_{\text{convert}} = \frac{\partial V}{\partial \sigma} = S \times n(d_1) \times \sqrt{T}
$$

- Always positive (long optionality)

- **Benefit:** Vol expansion = profit

- **Risk:** Vol contraction = loss

### 17. The Financing Economics


**Critical aspect often overlooked:**

**To do convertible arbitrage, you need:**

1. **Buy the bond:** Requires capital = $1,000 per bond

2. **Short the stock:** Requires locate + borrow cost

3. **Post margin:** For short stock position

**Total capital required:**

- Bond purchase: $1,000 (can be levered 3:1 to 10:1)

- Margin for short: $300-500 (reg T margin)

- **Net capital:** $500-1,000 per bond if using leverage

**Leverage analysis:**

**No leverage:**

- Buy bond with $1,000 cash

- Expected return: 8-12% on gamma + carry

- **ROI: 8-12%**

**3:1 Leverage (typical hedge fund):**

- Use $333 equity, borrow $667

- Financing cost: 5% × $667 = $33.35

- Gross return: $100 (on $1,000 bond)

- Net return: $100 - $33.35 = $66.65

- **ROI: $66.65 / $333 = 20%**

**5:1 Leverage (aggressive):**

- Use $200 equity, borrow $800

- Financing cost: 5% × $800 = $40

- **ROI: ($100 - $40) / $200 = 30%**

**Key insight:** Leverage amplifies returns but also risks!

**The 2005 crisis:**

- Funds using 10:1 leverage

- When credit spreads widened (bond floor dropped)

- Losses amplified by leverage

- **Many funds blew up**

### 18. Professional Institutional Perspective


**Market makers / Credit Suisse, Morgan Stanley, etc.:**

**Business model:**

- Underwrite convertible bonds for issuers

- **Can't hold inventory** (too risky)

- Immediately **delta hedge** and sell to hedge funds

- Make money on underwriting fees

**Role in market:**

- Provide liquidity

- Price convertibles using sophisticated models

- Compete to win issuance mandates

**Hedge funds / Citadel, Elliott, Caxton, etc.:**

**Business model:**

- Buy convertibles from underwriters

- Hold as **arbitrage positions**

- Extract multiple alpha sources

- Target 10-15% levered returns

**Capital deployment:**

- Typical fund: $1-5 billion AUM

- Use 3-5× leverage

- Manage 50-200 positions

- Risk management crucial (2005 wipeout!)

**Insurance companies / Pension funds:**

**Business model:**

- Buy-and-hold investors

- Attracted by: Credit + equity upside

- **Don't hedge** (passive investors)

- Hold to maturity or conversion

**Role in mispricing:**

- They set initial prices (bond investor mindset)

- Under-value embedded optionality

- Create arbitrage opportunity for hedge funds

### 19. When Convertible Arbitrage Offers Economic Edge


**The strategy works best when:**

### 20. New Issuance (Primary Market)


**Why:**

- Underwriters need to place bonds quickly

- Pricing pressure (must sell entire deal)

- **Hedge funds get better prices** (can absorb large size)

**Historical:**

- 2000-2007: Heavy issuance ($50B+/year)

- Post-2008: Issuance dropped (<$20B/year)

- **Best arbitrage opportunities in heavy issuance periods**

### 21. Credit Improving / Equity Volatile


**Perfect setup:**

- Company fundamentals improving (credit spread tightening)

- Stock still volatile (gamma profits available)

- **Example:** Early-stage growth companies

**Historical example:**

- Netflix 2013-2015

- Credit improving (business model proving out)

- Stock volatile (regulatory uncertainty, competition)

- **Converts performed excellently**

### 22. High Volatility Environment


**Need:**

- Realized volatility to monetize gamma

- If stock doesn't move → gamma profits don't materialize

**Example:**

- 2020 COVID crash: Vol spiked → huge gamma profits

- 2017-2018: Vol crushed (VIX < 12) → tough environment

### 23. Positive Carry Regime


**Need:**

- Coupon > Stock borrow cost

- **Net positive carry** makes waiting profitable

**Example:**

- 2010-2015: Low interest rates, low borrow costs, decent coupons

- **Nice carry environment**

### 24. Low Correlation Environment


**Portfolio benefit:**

- Many uncorrelated convert positions

- Diversify across sectors, credits, volatilities

- **Reduce portfolio risk** while maintaining returns

### 25. Why Convertible Arbitrage Has Declined Post-2008


**Pre-2008: Golden age**

- Heavy issuance ($50-80B/year)

- Multiple large hedge funds (billions in AUM)

- Good returns (12-15% levered)

- Low correlation to equity markets

**2008 Financial Crisis: The wipeout**

- Credit spreads exploded (bond floors collapsed)

- Stock prices plummeted (delta hedges insufficient)

- Leverage amplified losses

- **Many funds shut down** (Citadel lost 50%+, others worse)

**Post-2008: Permanently changed**

**1. Issuance decline:**

- $50B+ per year → $15-25B per year

- Fewer opportunities

**2. Investor demand:**

- Insurance/pension funds withdrew (burned)

- Less natural buyer base

- Converts now pricier (less mispriced)

**3. Regulatory changes:**

- Higher capital requirements for leverage

- Harder to finance positions

- Lower returns available

**4. Market structure:**

- More hedge funds competing

- Better models (less mispricing)

- Tighter arbitrage spreads

**Current state:**

- Strategy still exists but smaller

- Returns: 6-8% (vs. 12-15% historically)

- Requires more sophistication

- Concentrated in specialist funds

### 26. Summary of Economic Insights


**Convertible bond arbitrage is:**

1. **Capital structure arbitrage** - Long debt, short equity

2. **Underpriced optionality** - Embedded option cheaper than exchange options

3. **Five profit sources** - Gamma, carry, credit, vol, calls

4. **Sophisticated strategy** - Requires complex risk management

5. **Capacity constrained** - Issuance limits opportunities

6. **Leverage dependent** - Returns require 3-5× leverage

7. **Crisis vulnerable** - 2008 showed extreme downside

**The professional edge:**

Understanding converts means understanding:

- Capital structure dynamics

- Option pricing vs. credit pricing

- How to model hybrid securities

- Multi-factor risk management

- Financing economics

**Master converts → Master complex derivatives.**

---
