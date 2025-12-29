# Convertible Bond Arbitrage

**Convertible bond arbitrage** is a strategy where you profit from mispriced embedded optionality by buying convertible bonds and hedging away the directional risk through short stock positions.

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

### The Basic Structure

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

### Decomposing the Convertible Bond

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

### The Basic Trade

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

**Understanding what this strategy REALLY represents economically:**

### The Core Economic Trade-Off

This strategy involves specific economic trade-offs that determine when it's most valuable. The key is understanding what you're giving up versus what you're gaining in economic terms.

**Economic equivalence:**

$$
\text{Strategy P\&L} = \text{Greeks Exposure} + \text{Rebalancing} - \text{Costs}
$$

### Why This Structure Exists Economically

Markets create these strategies because different participants have different:
- Risk preferences (directional vs. convexity)
- Time horizons (short-term vs. long-term)
- Capital constraints (leverage limitations)
- View on volatility vs. direction

### Professional Institutional Perspective

Institutional traders view this strategy as a tool for:
1. **Greeks arbitrage:** Extracting value from Greeks mispricing
2. **Risk transformation:** Converting one type of risk into another
3. **Capital efficiency:** Optimal use of buying power for Greeks exposure
4. **Market making:** Providing liquidity while managing Greeks

Understanding the economic foundations helps you recognize when the strategy offers genuine edge versus when market pricing is fair.


## The P&L Formula

For a convertible bond arbitrage position:

$$
\delta \Pi \approx \underbrace{\text{Coupon Income}}_{\text{steady cash flow}} + \underbrace{\frac{1}{2}\Gamma(\delta S)^2}_{\text{gamma scalping}} + \underbrace{\text{Credit P\&L}}_{\text{spread tightening}} + \underbrace{\text{Vega} \cdot \delta\sigma}_{\text{vol changes}} - \underbrace{\text{Costs}}_{\text{borrow, IR}}
$$

**Breaking it down:**

### 1. Coupon Income (Steady Income)

**The bond pays coupons:**

- Typically 0-3% annually
- Lower than straight bonds (because of conversion feature)
- Still positive income stream

**This is unique to convertible arbitrage!**
- Unlike pure option positions (no carry)
- Helps offset costs

### 2. Gamma P&L (Like Gamma Scalping)

**From delta hedging rebalancing:**
$$
\text{Gamma P\&L} = \frac{1}{2}\Gamma(\delta S)^2
$$

- Stock moves → delta changes → rebalance → buy low/sell high
- **Same mechanism as gamma scalping!**
- This is a major profit source

### 3. Credit P&L (Spread Changes)

**Bond credit spread can tighten:**

- If company's creditworthiness improves
- If market credit conditions improve
- Bond value increases independent of stock price

**Example:**

- Buy convert when credit spread = 500 bps
- Spread tightens to 300 bps → bond floor increases
- Profit even if stock doesn't move!

### 4. Vega P&L (Volatility Changes)

**Embedded option has vega:**

- If implied volatility increases → option value increases
- Convertible bond value increases
- Profit (if you're long vega, which you are)

**Similar to vega trading!**

### 5. Costs (Negative Carry)

**You pay several costs:**

**Stock borrow cost:**

- Short stock requires borrowing shares
- Borrow rate can be 0.1% to 10%+ (for hard-to-borrow stocks)
- This is your main cost

**Interest rate exposure:**

- May need to hedge interest rate risk
- Costs money

**Financing:**

- Cost to finance the bond purchase
- Leverage costs

**Net carry:**
$$
\text{Net Carry} = \text{Coupon Income} - \text{Stock Borrow Cost} - \text{Other Costs}
$$

**Goal:** Positive net carry + gamma profits + credit spread tightening > 0

---

## Concrete Example: Convertible Bond Arbitrage Trade

**Setup:**

**XYZ Corp Convertible Bond:**

- Face value: $1,000
- Coupon: 2.5% ($25/year)
- Maturity: 5 years
- Conversion ratio: 25 shares per bond
- Conversion price: $40 per share

**Stock:** $38 currently

**Market prices:**

- Convertible bond trading at: $950
- Straight bond value (bond floor): $850
- Embedded option theoretical value: $130
- **Actual implied option value in convert: $100 ($950 - $850)**
- **Undervalued by $30!**

**The Trade:**

**1. Buy 100 convertible bonds**
- Cost: $950 × 100 = $95,000
- Embedded: 25 shares × 100 bonds = 2,500 share call option equivalent
- Delta of embedded option: 0.50 (at the money)

**2. Short stock (delta hedge)**
- Delta hedge: 0.50 × 2,500 = 1,250 shares short
- Short at $38: receive $47,500

**3. Net investment:**

- Long converts: -$95,000
- Short stock: +$47,500
- **Net: -$47,500**

**Scenario 1: Stock Rises to $45 (You Harvest Gamma)**

After 3 months:
- Stock at $45 (up from $38)
- Convert bond value: $1,050 (bond floor + option value increased)
- Your P&L on converts: $1,050 - $950 = +$100 per bond = +$10,000

**Delta hedging P&L:**

- Delta increased from 0.50 to 0.70 (stock moved up)
- You rebalanced: shorted more stock as it rose
- Gamma P&L from rebalancing: approximately +$3,000

**Stock hedge P&L:**

- Started short 1,250 shares at $38
- Stock now $45
- Mark-to-market loss: 1,250 × ($45-$38) = -$8,750

**Coupon income:**

- Earned $25/bond × 100 bonds × 0.25 years = +$625

**Borrow cost:**

- Stock borrow rate 1% annually
- 1,250 shares × $38 × 1% × 0.25 = -$119

**Net P&L:**

- Converts: +$10,000
- Stock hedge (initial): -$8,750
- Gamma rebalancing: +$3,000
- Coupon: +$625
- Borrow: -$119
- **Total: +$4,756**

**You profited from:**

- Embedded option appreciation
- Gamma scalping gains from rebalancing
- Coupon income > borrow costs

**Scenario 2: Credit Spread Tightens (Stock Doesn't Move)**

After 6 months:
- Stock still at $38 (no movement)
- Company reports strong earnings, credit improves
- Credit spread tightens from 500 bps to 300 bps
- Bond floor increases from $850 to $920
- Convert value increases to $1,020 (bond floor + option value)

**Your P&L:**

- Converts: $1,020 - $950 = +$70 per bond = +$7,000
- Stock hedge: no change (stock hasn't moved)
- Coupon income: $25 × 100 × 0.5 = +$1,250
- Borrow cost: 1,250 × $38 × 1% × 0.5 = -$238
- **Total: +$8,012**

**You profited from credit spread tightening even though stock didn't move!**

**Scenario 3: Stock Crashes (Hedged)**

After 1 month:
- Stock crashes to $28 (down from $38)
- Convert value drops to $880 (option less valuable, approaching bond floor)

**Your P&L:**

- Converts: $880 - $950 = -$70 per bond = -$7,000
- Stock hedge: Short 1,250 at $38, now $28 = +$12,500 profit
- Gamma P&L from rebalancing: +$2,000 (bought low as stock fell)
- Coupon: +$208
- Borrow: -$40
- **Total: +$7,668**

**You're protected! Stock losses offset by hedge gains and gamma scalping.**

---

## Convertible Arbitrage vs. Other Strategies

**Let's see how convertible arbitrage fits with what we've learned:**

| Strategy | Instrument | Primary Exposure | What You Want | Unique Feature |
|----------|-----------|------------------|---------------|----------------|
| **Delta Hedging** | Options | None (hedged) | Stability | Risk management |
| **Gamma Scalping** | Options | Gamma (realized vol) | Stock to move | Pay theta for gamma |
| **Vega Trading** | Options | Vega (implied vol) | IV to change | Bet on expectations |
| **Dispersion Trading** | Options (many) | Correlation | Independent moves | Trade structure |
| **Convertible Arbitrage** | Convertible Bonds | Gamma + Credit + Vega | Multiple sources | Coupon income! |

### Similarities to Gamma Scalping

**Mechanically similar:**

- Long instrument with embedded option
- Delta hedge with short stock
- Rebalance to harvest gamma
- Profit from volatility

**The P&L from gamma is identical:**
$$
\text{Gamma P\&L} = \frac{1}{2}\Gamma(\delta S)^2
$$

### Key Differences from Gamma Scalping

| Aspect | Gamma Scalping | Convertible Arbitrage |
|--------|---------------|----------------------|
| **Instrument** | Exchange-traded options | Convertible bonds |
| **Coupon income** | None (pay theta) | Yes (receive coupons) |
| **Credit exposure** | None | Yes (bond credit risk) |
| **Liquidity** | High | Lower |
| **Complexity** | Moderate | High |
| **Profit sources** | Gamma only | Gamma + Credit + Vega + Coupon |
| **Borrow costs** | Minimal | Can be significant |
| **Entry reason** | Option undervalued | Embedded option + structural reasons |

**The BIG difference:**

- **Gamma scalping:** Pure play on realized volatility
- **Convertible arbitrage:** Multi-factor opportunity (gamma + credit + coupon + vega)

**This is both an advantage (more profit sources) and disadvantage (more risk factors)**

---

## Why Convertible Arbitrage Exists

**Several structural reasons:**

### 1. Market Segmentation

**Different investors, different goals:**

- **Bond investors:** Focus on yield, credit, may underprice option
- **Equity investors:** Don't naturally buy bonds
- **Arbitrageurs:** Bridge the gap

### 2. Forced Sellers

**Issuers use converts strategically:**

- Cheaper financing than straight debt
- Don't want to dilute with equity immediately
- Creates supply

**Hedge fund redemptions:**

- During stress, funds must liquidate
- Sells converts at fire-sale prices
- Creates opportunities

### 3. Complexity Premium

**Hard to value:**

- Credit risk + equity option + interest rate risk
- Call/put provisions complicate valuation
- Illiquid
- Complexity creates discount

### 4. Financing Advantage

**Arbitrageurs can finance efficiently:**

- Prime brokers provide leverage
- Can lock in attractive financing
- Retail/smaller investors can't compete

### 5. Hedging Infrastructure

**Requires sophistication:**

- Delta hedging expertise
- Risk management systems
- Stock borrow relationships
- Barrier to entry = persistent opportunity

---

## The Multiple Profit Sources

**Unlike pure option strategies, convertible arbitrage has FOUR profit sources:**

### 1. Cheapness Capture

**Initial entry discount:**

- Embedded option worth $130
- Market implies only $100
- $30 profit when mispricing corrects

**This is "buying undervalued assets"**

### 2. Gamma Scalping

**From dynamic hedging:**

- Stock volatility → rebalancing profits
- Buy low, sell high mechanically
- Same as pure gamma scalping

### 3. Credit Spread Capture

**Credit improvement:**

- Company's credit improves
- Spread tightens (e.g., 500 bps → 300 bps)
- Bond floor increases
- Independent of stock price!

**This is unique to converts!**

### 4. Coupon Income

**Steady cash flow:**

- Receive 0-3% annually
- Helps offset borrow costs
- Positive carry if coupons > costs

**This too is unique!**

### Sum Total

**Best case scenario:** All four work in your favor
- Entry: bought cheap ✓
- Stock bounced around: gamma profits ✓
- Credit improved: spread tightened ✓
- Coupons > borrow costs: positive carry ✓

**This is why convertible arbitrage can be very attractive!**

---

## Risks and Challenges

### 1. Credit Risk (The Big One)

**Company goes bankrupt:**

- Bond value → 0
- Stock value → 0
- Your hedge doesn't help!
- **This is your unhedged risk**

**Example: Lehman Brothers 2008**
- Lehman converts were popular trades
- Company went bankrupt
- Investors lost 90%+
- Stock hedge didn't matter

**Management:**

- Diversify across issuers
- Monitor credit carefully
- Set position limits
- Use credit default swaps to hedge (reduces returns)

### 2. Borrow Costs (Can Kill Returns)

**Stock borrow can be expensive:**

- "Hard to borrow" stocks: 5-10%+ annually
- Can exceed coupon income
- Negative carry kills returns

**Borrow rates can spike:**

- During short squeezes
- When stock becomes scarce
- Can force position closure

**Example:**

- Convert pays 2% coupon
- Borrow costs 8%
- Negative carry: -6% annually
- Need gamma + credit to overcome!

### 3. Liquidity Risk

**Converts are less liquid:**

- Wide bid-ask spreads
- Hard to exit in size
- Price gaps in stress

**2008 example:**

- Convert market froze
- Couldn't exit positions
- Forced liquidations at losses

### 4. Call Risk (Issuer Can Force Conversion)

**Issuer has rights too:**

- Can "call" the bond (force redemption)
- Usually when stock is well above conversion price
- Kills your gamma profits (position terminated)

**Example:**

- Stock at $60, conversion price $40
- Issuer calls the bond
- You must convert and close position
- Lose future gamma potential

### 5. Multiple Risk Factors

**Unlike pure gamma scalping:**

- Exposed to credit, interest rates, equity, volatility
- Correlation between factors
- Complex risk management

**Stress scenario:**

- Credit deteriorates → bond floor drops
- Stock crashes → option worthless
- Borrow costs spike → negative carry
- All at once! (2008)

### 6. Model Risk

**Valuation is complex:**

- Need to value embedded option
- Credit risk affects option value
- Call/put provisions
- If model is wrong, your hedge is wrong

### 7. Financing Risk

**Leverage is essential:**

- Need prime broker financing
- Margin calls during volatility
- Refinancing risk

**2008 example:**

- Prime brokers withdrew financing
- Hedge funds forced to liquidate
- Downward spiral

---

## Pros and Cons

### Advantages ✓

**1. Multiple profit sources**
- Gamma + Credit + Coupon + Vega
- Diversified return streams
- Not reliant on single factor

**2. Structural edge**
- Market segmentation
- Complexity premium
- Persistent mispricing

**3. Downside protection (partially)**
- Bond floor provides cushion
- Stock hedge protects from equity moves
- Credit is main unhedged risk

**4. Positive carry (often)**
- Coupon income
- Can exceed borrow costs
- Unlike pure options (negative theta)

**5. Volatility is your friend**
- Gamma scalping profits from vol
- Higher vol → more gamma P&L
- Like gamma scalping

**6. Credit improvement adds alpha**
- Independent profit source
- Can profit even if stock doesn't move
- Diversifies return profile

**7. Market neutral (mostly)**
- Delta hedged
- Not betting on stock direction
- Focus on relative value

**8. Event-driven opportunities**
- Hedge fund liquidations
- Market dislocations
- Crisis opportunities (if you have capital!)

### Disadvantages ✗

**1. Credit risk is unhedged**
- Company bankruptcy = total loss
- This is your "tail risk"
- Hard to diversify away completely
- 2008 showed this dramatically

**2. Borrow costs can be prohibitive**
- Hard-to-borrow stocks expensive
- Rates can spike unpredictably
- Negative carry kills returns
- Can force early exit

**3. Complexity**
- Multiple risk factors
- Complex valuation
- Sophisticated systems needed
- High operational burden

**4. Illiquidity**
- Wide spreads
- Hard to exit in size
- Price gaps during stress
- Forced liquidations at worst times

**5. Call risk**
- Issuer can terminate position
- Lose future profit potential
- Timing is out of your control

**6. Capital intensive**
- Need significant capital base
- Leverage amplifies risks
- Prime broker relationships essential

**7. Correlation in crises**
- All risks hit at once in stress
- Credit deteriorates + borrow spikes + liquidity dries up
- "When you need diversification most, it fails"

**8. Operational complexity**
- Must manage bonds + stocks + hedges
- Corporate actions (dividends, M&A, etc.)
- Conversion mechanics
- Intensive monitoring

**9. Limited opportunity set**
- Fewer converts than stocks/options
- Need specific characteristics
- Can't always find good trades

---

## When Convertible Arbitrage Works Best

### Favorable Conditions

**1. Market dislocations**
- Hedge fund liquidations
- Credit crises (2008, 2020)
- Converts trade at fire-sale prices
- Best opportunities!

**2. Stable credit environment**
- Low default risk
- Credit spreads stable or tightening
- Not during credit crises

**3. Positive carry**
- Coupon > borrow cost
- Can earn while waiting
- Enhances returns

**4. Reasonable volatility**
- Stock moves enough for gamma scalping
- Not too volatile (harder to hedge)
- "Goldilocks" volatility

**5. Available borrow**
- Stock not hard to borrow
- Reasonable borrow costs
- Stable borrow markets

**6. Liquid converts**
- Tight spreads
- Can enter/exit efficiently
- Sufficient issuance

### Unfavorable Conditions

**1. Credit crisis**
- Default risk high
- Credit spreads widening
- This is your worst enemy

**2. Hard to borrow stocks**
- Borrow costs > coupon
- Negative carry
- Unstable borrow

**3. Low volatility**
- Little gamma to harvest
- Main profit source reduced
- Returns compressed

**4. Illiquid markets**
- Wide spreads
- Can't execute efficiently
- Stuck in positions

**5. Issuer call risk high**
- Stock well above conversion price
- Position likely to be called
- Limited upside

**6. Leverage stress**
- Prime broker issues
- Margin calls
- Forced liquidations

---

## The Evolution: Pre-2008 vs. Post-2008

**The strategy changed dramatically after the financial crisis:**

### Pre-2008 ("The Golden Age")

**Characteristics:**

- Abundant opportunities
- High leverage (5-10x)
- Low borrow costs
- Stable credit environment
- Hedge funds returned 10-15% annually

**Why it worked:**

- Market segmentation strong
- Less competition
- Complexity premium high

### Post-2008 ("The New Reality")

**Characteristics:**

- Fewer opportunities
- Lower leverage (2-4x)
- Higher borrow costs
- Credit risk awareness
- Returns compressed to 5-8%

**What changed:**

- Prime brokers more conservative
- More competition (everyone learned the strategy)
- Regulation increased complexity
- Less convert issuance

**Today:**

- Still viable but more challenging
- Need larger capital base
- Lower returns
- More selective

---

## Practical Implementation

### 1. Screening for Opportunities

**Look for:**

- Undervalued embedded option
- Positive or neutral carry (coupon > borrow)
- Reasonable credit (B+ or better)
- Liquid convertible (tight spreads)
- Stock volatility (for gamma)

**Metrics:**

- "Cheapness": Embedded option value vs. theoretical
- Credit spread vs. historical
- Borrow cost vs. coupon
- Liquidity (bid-ask spread)

### 2. Position Sizing

**Risk management:**

- Limit per issuer (credit risk)
- Total portfolio leverage
- Sector diversification
- Maximum position size

**Rule of thumb:**

- No more than 2-3% per issuer
- Total leverage 2-4x
- Diversify across 30-50 positions

### 3. Delta Hedging

**Hedge ratios:**

- Calculate option delta
- Short stock proportionally
- Rebalance daily or when delta changes >10%

**Not over-optimizing:**

- Don't rebalance too frequently (costs)
- Focus on staying roughly neutral
- Unlike pure gamma scalping (where optimization matters)

### 4. Monitoring

**Daily tasks:**

- Monitor credit spreads
- Check borrow costs
- Rebalance delta
- Corporate actions

**Weekly:**

- Review position P&L
- Adjust hedges if needed
- Check for call risk

### 5. Exit Discipline

**Exit when:**

- Credit deteriorates
- Borrow costs spike
- Cheapness disappears (converged)
- Better opportunities elsewhere
- Approaching maturity

---


---

## Worst Case Scenario

**What happens when everything goes wrong:**

### The Nightmare Setup

**How it starts:**
- [Unfavorable Greeks behavior]
- [Market moves against position]
- [Rebalancing losses mount]

**The deterioration:**

**Week 1:**
- [Early warning signs in Greeks]
- [Position losing value]
- [Rebalancing creating losses]
- [Critical decision point]

**Through expiration:**
- [Continued adverse Greeks dynamics]
- [Mounting hedge costs]
- [Maximum loss approached/realized]
- [Final outcome]

### Maximum Loss Calculation

**Worst case mathematics:**

$$
\text{Max Loss} = \text{Option Premium} + \text{Hedging Costs} + \text{Slippage}
$$

**Or for leveraged Greeks:**

$$
\text{Max Loss} = \text{Greeks Exposure} \times \text{Adverse Move} + \text{Transaction Costs}
$$

**Example calculation:**
- Position: [Specific position]
- Greeks exposure: [Delta, gamma, vega, theta]
- Adverse scenario: [What went wrong]
- Rebalancing costs: [Excessive]
- **Loss: [Calculation]**

### What Goes Wrong

The worst case occurs when:
1. **Wrong Greeks exposure:** Market behavior opposite to position
2. **Wrong volatility:** Realized vol doesn't materialize (or too much)
3. **Wrong timing:** Adverse moves happen quickly
4. **Wrong costs:** Transaction costs explode
5. **Wrong liquidity:** Cannot rebalance efficiently

### The Cascade Effect

**Multiple compounding failures:**

**Trade 1: Initial loss**
- [Setup and expectation]
- [What went wrong]
- [Loss amount]

**Trade 2: Revenge trading**
- [Doubling down]
- [Further losses]
- [Psychological damage]

**Trade 3: Account damage**
- [Desperation]
- [Major loss]
- [Recovery difficulty]

**Total damage:**
- Cumulative loss: [Amount]
- Portfolio impact: [Percentage]
- Time to recover: [Estimate]

### Greeks Blow-Up Scenarios

**Gamma blow-up:**
- [Large gap move]
- [Cannot rebalance]
- [Massive slippage]
- [Assignment risk]

**Vega collapse:**
- [IV crush]
- [Long vega position destroyed]
- [No recovery possible]

**Theta burn:**
- [No volatility materialized]
- [Time decay relentless]
- [Position expires worthless]

### Real Disasters

**Historical example 1:**
- [Specific event/strategy]
- [What happened to Greeks]
- [Final loss]
- [Lesson learned]

**Historical example 2:**
- [Specific event/strategy]
- [What happened to Greeks]
- [Final loss]
- [Lesson learned]

### Transaction Cost Death Spiral

**The problem:**
- Over-hedging/rebalancing
- Small price moves triggering rebalances
- Bid-ask spread eating profits
- Commission accumulation

**The math:**
- Expected Greeks P&L: $X
- Actual transaction costs: $Y > $X
- Net loss despite correct directional view

**Prevention:** Optimal rebalancing frequency, delta bands

### Psychology of Greeks Losses

**Emotional stages:**
1. **Confusion:** "My Greeks model says this should work"
2. **Denial:** "Just need volatility to pick up"
3. **Frustration:** "Transaction costs are killing me"
4. **Capitulation:** "Close everything"
5. **Learning:** "What did my Greeks analysis miss?"

**Winning trader mindset:**
- Greeks models are imperfect
- Accept losses in adverse scenarios
- Learn from Greeks attribution
- Improve risk management

### Preventing Worst Case

**Risk management strategies:**

1. **Position sizing by Greeks:**
   - Limit max delta exposure
   - Cap gamma concentration
   - Control vega risk
   - Monitor theta bleed

2. **Rebalancing discipline:**
   - Set delta bands
   - Consider transaction costs
   - Don't over-rebalance
   - Use algorithms if possible

3. **Diversification:**
   - Multiple Greeks exposures
   - Different underlyings
   - Various timeframes
   - Offsetting positions

4. **Liquidity requirements:**
   - Only trade liquid options
   - Ensure can exit/rebalance
   - Monitor volume and spreads
   - Have contingency plans

5. **Scenario analysis:**
   - Stress test all Greeks
   - Model extreme moves
   - Calculate worst-case costs
   - Plan exit strategies

### The Ultimate Protection

**Greeks risk limits:**

$$
\text{Max Delta} < \text{Limit}_\Delta
$$
$$
\text{Max Gamma} < \text{Limit}_\Gamma  
$$
$$
\text{Max Vega} < \text{Limit}_\nu
$$
$$
\text{Max Theta} < \text{Limit}_\theta
$$

Respect these limits religiously. A single Greeks blow-up can destroy months or years of careful P&L accumulation.

**Remember:** Greeks strategies amplify both gains and losses. The market WILL test your risk management. Proper position sizing and discipline determine survival.



---

## Best Case Scenario

**What happens when everything goes right:**

### The Perfect Setup

**Ideal entry conditions:**
- [Greeks favorably positioned]
- [Volatility at optimal level]
- [Market conditions supporting strategy]
- [Liquidity abundant]

**The optimal sequence:**

**Week 1:**
- [Initial Greeks behavior]
- [Favorable market moves]
- [Successful rebalancing]
- [P&L accumulation begins]

**Through position:**
- [Continued favorable Greeks dynamics]
- [Optimal rebalancing opportunities]
- [Greeks P&L exceeding costs]
- [Final profitable exit]

### Maximum Profit Achievement

**Best case mathematics:**

$$
\text{Max Profit} = \text{Greeks P\&L} - \text{Hedging Costs} - \text{Theta Decay}
$$

**Example calculation:**
- Position: [Specific position]
- Greeks exposure: [Delta, gamma, vega, theta]
- Market move: [Favorable scenario]
- Rebalancing: [Optimal frequency]
- **Profit: [Calculation]**

### What Makes It Perfect

The best case requires:
1. **Right Greeks setup:** Exposure matches market behavior
2. **Right volatility:** Realized matches expectations
3. **Right timing:** Greeks P&L accumulates quickly
4. **Right costs:** Transaction costs remain low
5. **Right liquidity:** Can rebalance efficiently

### Greeks P&L Breakdown

**Component analysis:**

**Delta P&L:**
- [How delta contributed]
- [Directional component]

**Gamma P&L:**
- [Rebalancing profits]
- [Convexity capture]

**Vega P&L:**
- [Volatility change impact]
- [IV expansion/contraction]

**Theta P&L:**
- [Time decay cost/benefit]
- [Carry component]

**Net P&L:** Sum of all Greeks components minus costs

### Comparison to Alternatives

**This strategy vs. [Alternative approach]:**
- [Greeks exposure comparison]
- [Cost-benefit analysis]
- [When this strategy wins]
- [Trade-offs involved]

### Professional Profit-Taking

**When to exit:**
- Greeks P&L target achieved
- Market conditions changing
- Transaction costs increasing
- Better opportunity elsewhere

**The compounding advantage:**

By taking profits and redeploying into new favorable Greeks setups, you can achieve better risk-adjusted returns than holding positions hoping for maximum theoretical profit.

### The Dream Scenario

**Extreme best case:**
- [Exceptional Greeks alignment]
- [Massive realized vol vs. low costs]
- [Multiple profitable rebalances]
- [Outsized P&L]

**Probability:** Rare but illustrates potential

**Key insight:** Best case demonstrates the strategy's maximum potential, but realistic expectations should be more modest. Position sizing should assume median outcomes, not best case.



---


---

## Practical Guidance

**Step-by-step implementation framework:**

### Step 1: Market Assessment

**Before entering, evaluate:**

1. **Volatility environment:**
   - Current IV level and percentile
   - Implied vs. realized volatility spread
   - Term structure of volatility

2. **Greeks landscape:**
   - Which Greeks are mispriced
   - Expected Greeks P&L
   - Rebalancing frequency required

3. **Market conditions:**
   - Liquidity in options and underlying
   - Bid-ask spreads
   - Transaction cost environment

### Step 2: Strategy Selection Criteria

**Enter this strategy when:**
- [Specific Greeks conditions]
- [Volatility requirements]
- [Liquidity sufficient for rebalancing]
- [Expected Greeks P&L > costs]

**Avoid this strategy when:**
- [Unfavorable Greeks environment]
- [High transaction costs]
- [Insufficient liquidity]
- [Wrong volatility regime]

### Step 3: Position Sizing

**Calculate maximum position size:**

$$
\text{Max Size} = \frac{\text{Portfolio} \times \text{Risk\%}}{\text{Max Greeks Loss}}
$$

**For Greeks strategies, consider:**
- Greeks exposure limits
- Rebalancing capacity
- Capital for hedge adjustments
- Margin requirements

### Step 4: Entry Execution

**Best practices:**

1. **Greeks analysis:** Calculate all relevant Greeks before entry
2. **Liquidity check:** Ensure sufficient volume for rebalancing
3. **Spread analysis:** Check bid-ask spreads on all legs
4. **Hedge execution:** Enter hedges simultaneously with options

**Rebalancing framework:**
- Delta rebalance when: |Δ| > threshold
- Vega adjustment when: IV moves X%
- Gamma management when: Position size changes
- Transaction cost consideration: Balance frequency vs. cost

### Step 5: Position Management

**Active management rules:**

**Greeks monitoring:**
- Track delta daily (minimum)
- Monitor gamma exposure
- Watch vega for IV changes
- Calculate P&L attribution by Greek

**Rebalancing triggers:**
- Delta: Rebalance when exceeds threshold
- Vega: Adjust on IV regime changes
- Gamma: Scale position with proximity to strikes
- Theta: Monitor daily decay

**Profit/loss targets:**
- Take profit at: [Greeks P&L target]
- Cut losses at: [Max acceptable Greeks loss]
- Time-based exit: [Time decay considerations]

### Step 6: Risk Management

**Greeks risk limits:**
- Max delta exposure: [Limit]
- Max gamma concentration: [Limit]
- Max vega exposure: [Limit]
- Theta bleed tolerance: [Limit]

**Portfolio-level controls:**
- Correlation of Greeks across positions
- Aggregate exposure monitoring
- Stress testing for market moves
- Worst-case scenario planning

### Step 7: Record Keeping

**Track for every trade:**
- Entry Greeks (delta, gamma, vega, theta)
- Rebalancing frequency and costs
- P&L by Greek component
- Actual vs. expected volatility
- Transaction costs vs. Greeks P&L
- Lessons learned

### Common Execution Mistakes to Avoid

1. **Ignoring transaction costs** - Frequent rebalancing eats profits
2. **Wrong rebalancing frequency** - Too often or too infrequent
3. **Insufficient liquidity** - Cannot execute rebalances efficiently
4. **Over-leveraging Greeks** - Excessive exposure to single Greek
5. **Neglecting other Greeks** - Focus on one Greek, ignore others
6. **Poor hedge timing** - Waiting too long or reacting too quickly

### Professional Implementation Tips

**For delta hedging:**
- Use delta bands (don't chase every move)
- Consider transaction costs
- Rebalance at consistent intervals

**For gamma scalping:**
- Need sufficient realized vol
- Monitor gamma P&L vs. theta cost
- Scale position size with gamma exposure

**For vega trading:**
- Understand vol term structure
- Watch for regime changes
- Consider vega cross-effects (vanna, volga)


## Common Mistakes

[Common errors to avoid]



---

## Real-World Examples

[Concrete examples]


## What to Remember

### Core Concepts

**Convertible bonds = Bonds + Embedded Call Options**

$$
\text{Convert} = \text{Straight Bond} + \text{Call Option}
$$

- The embedded option often trades cheap
- Buy the convert, short stock (delta hedge)
- Extract value from underpriced optionality

### The Arbitrage Structure

**Position:**

- Long convertible bond (cheap option + coupon)
- Short stock (delta hedge)
- Optional: hedge interest rates

**P&L sources:**

1. **Cheapness capture** - embedded option undervalued
2. **Gamma scalping** - dynamic hedging profits
3. **Credit spread tightening** - bond floor increases
4. **Coupon income** - positive carry

### Comparison to Gamma Scalping

**Similarities:**

- Both delta hedge options
- Both harvest gamma
- Both profit from volatility
- Mechanically similar

**Differences:**

- **Instrument:** Converts vs. exchange-traded options
- **Coupon:** Receive income vs. pay theta
- **Credit:** Exposed vs. no credit risk
- **Complexity:** Higher vs. lower
- **Profit sources:** Multiple vs. single

### The Big Risk: Credit

**Unhedged credit risk is your tail risk:**

- Company bankruptcy → total loss
- Stock hedge doesn't help
- Must diversify
- Monitor carefully

### Historical Context

**Pre-2008:** "Golden age"
- High returns (10-15%)
- High leverage
- Less competition

**Post-2008:** "New reality"
- Lower returns (5-8%)
- Lower leverage
- More competition
- Still viable but harder

### Success Factors

**What you need:**

1. **Credit analysis** - avoid defaults
2. **Delta hedging discipline** - stay neutral
3. **Borrow management** - minimize costs
4. **Diversification** - many positions
5. **Capital** - sufficient size for efficiency
6. **Patience** - let the trade work

### The Deep Insight

**Convertible arbitrage is "multi-factor volatility arbitrage":**

Unlike pure gamma scalping (single profit source):
- Gamma: Like gamma scalping (profit from realized vol)
- Credit: Like credit arbitrage (profit from spread tightening)
- Coupon: Like bond investing (collect income)
- Vega: Like vega trading (profit from IV changes)

**You're simultaneously:**

- A volatility trader (gamma scalping)
- A credit investor (bond holder)
- A relative value arbitrageur (cheapness)

**This diversification of profit sources is both:**

- **Advantage:** Multiple ways to win
- **Challenge:** Multiple things to manage

### The Complete Hierarchy Now

**Your curriculum progression:**

1. **Delta Hedging** → Risk management (insurance)
2. **Gamma Scalping** → Single-asset realized vol
3. **Vega Trading** → Single-asset implied vol
4. **Dispersion Trading** → Multi-asset correlation
5. **Convertible Arbitrage** → Multi-factor (gamma + credit + coupon + vega)

**Each level builds on delta hedging but adds complexity:**

- More profit sources
- More risk factors
- More sophistication required

**Convertible arbitrage represents a "real-world" strategy:**

- Used by major hedge funds
- Billions in AUM
- Requires institutional infrastructure
- But the concepts build directly on gamma scalping!

### Final Wisdom

**The beauty of convertible arbitrage:**

- Takes the elegant concept of gamma scalping
- Adds bond income and credit exposure
- Creates a multi-dimensional opportunity
- More complex, but potentially more robust

**The challenge:**

- Credit risk can dominate (2008 lesson)
- Operational complexity high
- Lower returns than past
- Not for everyone

**But the core insight remains:**

- **You're buying a cheap option (embedded in convert)**
- **Financing it with bond coupons**
- **Hedging away the directional risk**
- **Harvesting gamma and credit value**

**This is gamma scalping + credit investing + bond financing all in one trade!**
