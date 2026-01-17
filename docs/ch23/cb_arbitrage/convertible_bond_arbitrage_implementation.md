# Convertible Bond Arbitrage: Implementation

> **Part 2 of 3** | See also: [Mechanics](convertible_bond_mechanics.md) | [Risk & Performance](convertible_bond_arbitrage_risk.md)

This section covers the practical implementation of convertible bond arbitrage: P&L drivers, position management, hedging mechanics, and execution considerations.

---

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

### 1. Similarities to Gamma Scalping


**Mechanically similar:**

- Long instrument with embedded option

- Delta hedge with short stock

- Rebalance to harvest gamma

- Profit from volatility

**The P&L from gamma is identical:**
$$
\text{Gamma P\&L} = \frac{1}{2}\Gamma(\delta S)^2
$$

### 2. Key Differences from Gamma Scalping


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

### 5. Sum Total


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


### 1. Advantages ✓


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

### 2. Disadvantages ✗


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


### 1. Favorable Conditions


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

### 2. Unfavorable Conditions


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

### 1. Pre-2008 ("The Golden Age")


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

### 2. Post-2008 ("The New Reality")


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


**What happens when everything goes wrong with convertible arbitrage:**

### 1. The Nightmare Setup


**Example: Large established company facing disruption**

**Company profile:**

- General Motors (March 2005 actual historical example)

- Stock: $35 (down from $60 peak)

- Bond rating: BBB (investment grade, barely)

- Outstanding convertible bond:

  - Issued 2001 at better times

  - Face value: $1,000

  - Coupon: 3%

  - Conversion price: $45

  - Maturity: 2031 (long-dated)

**Your position:**

- Buy GM converts at $920 (seemed cheap - 8% discount!)

- Bond floor estimated: $850

- Embedded option: $70

- Delta hedge: 35% (stock at $35 vs. conversion at $45)

- Short 7,778 shares per $1M face value

**Position size:**

- $100M face value purchased at $920 = $92M outlay

- With 4× leverage (typical pre-2005)

- **Your equity: $23M**

- Borrowed: $69M

### 2. The Catastrophic Sequence


**Week 1: The credit downgrade**

**May 5, 2005: S&P announces downgrade**

- GM downgraded: BBB → BB+ (junk status!)

- Immediate market panic

- GM bonds crash

- Convert bonds devastated

**Market reaction (Day 1):**

- GM stock: $35 → $31 (-11%)

- Convert bonds: $920 → $750 (-18.5%!)

- **Your position loss:**

  - Converts: -$170 per bond × 100,000 bonds = -$17M

  - Short stock gain: $4 per share × 7,778 shares per $1M = +$3.1M

  - **Net loss: -$13.9M** (-15.1% on position)

**On your $23M equity with 4× leverage:**

- Loss: $13.9M

- **Remaining equity: $9.1M** (-60% drawdown!)

**But it gets worse...**

**Week 1 continued: Margin calls**

**Your prime broker calls:**
> "We need additional margin. Your equity dropped 60%. Either add $10M cash or we start liquidating."

**Your response:**

- You don't have $10M cash readily available

- **Forced to sell positions** at worst possible time

**Forced liquidation (Day 3-5):**

- Try to sell $50M face value

- Market knows you're forced seller

- Bid-ask spreads explode: Normally $2, now $15!

- Can only sell at $730 (market $750 but illiquid)

- **Additional loss:** $(750 - 730) × 50,000 = -$1M$ from liquidation slippage

**Week 1 total damage:**

- Initial loss: -$13.9M

- Liquidation slippage: -$1M

- **Week 1 total: -$14.9M** (-65% of equity!)

**Remaining position:**

- $50M face value left

- Equity: $8.1M

- **Effective leverage now: 6×** (worse than before!)

### 3. The Deterioration Continues


**Weeks 2-4: Credit death spiral**

**May-June 2005: Cascade effects**

**Week 2:**

- Credit default swaps on GM spike

- Market realizes pension obligations massive

- Healthcare liabilities enormous

- **Bankruptcy chatter** begins

**Convert pricing:**

- Bond floor collapses: $850 → $650 (-23%)

- Embedded option almost worthless (stock at $28, conversion at $45)

- **Converts: $750 → $570** (-24%)

**Your position (remaining $50M face):**

- Loss: $(750 - 570) × 50,000 = -$9M$

- Stock hedge: Gained $(35 - 28) × 3,889 = +$2.7M$

- **Net loss: -$6.3M**

**Your equity:**

- Started Week 2 with: $8.1M

- After Week 2-4 losses: $1.8M

- **Total drawdown: 92%!**

**Week 5: Capitulation**

**Remaining position:**

- $50M face worth only $28.5M (57% of par!)

- Your equity: $1.8M

- Can't take anymore

- **Liquidate everything** at $570

**Final liquidation:**

- Sell converts: $570

- Cover stock short at $28

- Close position

### 4. Maximum Loss Calculation


**Complete P&L:**

**Initial investment:**

- Equity: $23,000,000

- Leverage: 4×

- Position: $92,000,000

**Phase 1: Credit event (Week 1):**

- Convert loss: $920 → $750 = -$17,000,000

- Stock hedge gain: +$3,100,000

- **Net: -$13,900,000**

**Phase 2: Forced liquidation (Week 1):**

- Slippage: -$1,000,000

**Phase 3: Continued deterioration (Weeks 2-4):**

- Convert loss: $750 → $570 = -$9,000,000

- Stock hedge gain: +$2,700,000

- **Net: -$6,300,000**

**Total losses:**

- Total: $13.9M + $1M + $6.3M = **$21,200,000**

- Started with: $23,000,000 equity

- **Remaining: $1,800,000**

- **Total loss: 92% of capital**

**Impact on portfolio:**
$$
\text{Recovery Needed} = \frac{1}{1 - 0.92} - 1 = 1,150\%
$$

**You need to make 1,150% just to get back to even!**

### 5. What Went Wrong: The Five Deadly Factors


**1. Wrong credit analysis (Fatal error #1):**

- Assumed BBB = safe

- **Ignored:**

  - Pension underfunding ($10B hole)

  - Healthcare obligations

  - Market share losses

  - SUV cycle turning

**Lesson:** Investment grade does NOT mean safe!

**2. Wrong leverage (Fatal error #2):**

- 4× leverage turned -15% loss → -60% equity loss

- Then forced selling amplified damage

- **Leverage killed the fund**

**Calculation showing leverage impact:**

- No leverage: -15% loss on $23M = -$3.45M (survived!)

- With 4× leverage: -60% loss = -$13.8M (near death)

- **Leverage amplified loss 4×**

**3. Wrong entry price (Error #3):**

- Bought at $920 thinking "cheap"

- Bond floor at $850

- **Only $70 cushion!** (7.6%)

- When floor collapsed to $650, lost $270 per bond

**Should have:**

- Required minimum 20% cushion (floor $700 minimum)

- Would have avoided this position entirely

**4. Wrong delta hedge assumptions (Error #4):**

- Delta 35% hedge protected against stock moves

- **But:** Credit events affect convert MORE than stock suggests

- Convert fell 38%, stock fell 20%

- **Delta hedge insufficient** for credit events

**Formula showed flaw:**
$$
\text{Delta Hedge P&L} = \Delta \times \Delta S \times \text{Shares}
$$

**This assumes credit risk hedged. It's NOT!**

**5. Wrong liquidity assumptions (Error #5):**

- Assumed could always exit at fair value

- **Reality:** Bid-ask exploded in crisis

- Forced sellers get crushed

- **Liquidity disappeared** exactly when needed

### 6. The Cascade Effect


**How one loss becomes complete destruction:**

**Trade 1: Initial GM position**

- Loss: -$13.9M

- Equity: $23M → $9.1M

**Trade 2: Revenge trading (psychological error):**

- "Need to make it back!"

- Take on Ford position (similar situation)

- $30M face value (oversize relative to remaining equity!)

- Ford credit also deteriorates

- **Additional loss: -$4.5M**

- Equity: $9.1M → $4.6M

**Trade 3: Desperation (death spiral):**

- "One more trade to recover"

- Buy deeply distressed converts (yielding 15%!)

- Hope for recovery

- **Company actually declares bankruptcy**

- Bonds → Zero

- **Loss: -$3M**

- Final equity: $4.6M → $1.6M

**Total damage:**

- Started: $23M

- Ended: $1.6M

- **Total loss: 93%**

- **Psychological destruction:** Complete

### 7. Real Historical Disasters


**Actual 2005 Convertible Arbitrage Meltdown:**

**Funds that shut down:**

- Numerous multi-billion dollar funds closed

- Estimated losses: $5-10 billion industry-wide

**Specific casualties:**

**Citadel:**

- Drew down -50% (survived but painful)

- Used lower leverage than peers (saved them)

- Had to accept investments at deep discounts to recover

**Smaller funds:**

- Many 100% wipeouts

- Forced liquidations

- Investors lost everything

**Why it was systemic:**

1. **Crowded trade:**

   - Everyone in same positions

   - All forced sellers simultaneously

   - No bids available

2. **Leverage amplified:**

   - Industry average: 6-8× leverage

   - Turned small credit events into catastrophes

3. **Correlation spike:**

   - All converts crashed together

   - "Diversification" disappeared

   - No place to hide

4. **Liquidity evaporated:**

   - Bid-ask spreads 10-20× normal

   - Impossible to exit cleanly

### 8. The Greeks Disaster Analysis


**How each Greek hurt:**

**Delta:**

- Hedged for stock moves

- **But credit moves weren't captured by delta**

- Net: Delta hedge FAILED in credit event

**Gamma:**

- Should profit from stock volatility

- **But when stock gaps, can't rebalance**

- Lost gamma opportunity (gaps prevented scalping)

**Vega:**

- Long vega position

- Vol DID spike (good!)

- **But credit component dominated** (bond floor collapse)

- Vega gains trivial vs. credit losses

**Rho (credit spreads):**

- Long credit (exposed to spread widening)

- Spreads exploded: 200 bps → 700 bps

- **Unhedged exposure killed position**

**Conclusion:** Greeks framework BREAKS DOWN in credit events!

### 9. Psychology of the Disaster


**Stage 1: Denial (Day 1-2)**

- "It's just temporary volatility"

- "GM won't actually fail"

- "Market overreacting"

- **Held position, hoped for recovery**

**Stage 2: Hope (Day 3-7)**

- "Just need credit spreads to stabilize"

- "Stock will bounce"

- "We can ride this out"

- **Prime broker forced their hand** (margin calls eliminated choice)

**Stage 3: Anger (Week 2)**

- "This is manipulation!"

- "Credit rating agencies failed"

- "Prime brokers forced selling at worst prices"

- **Revenge trading** begins (doubling down)

**Stage 4: Capitulation (Week 3-5)**

- "Get me out of everything"

- "Can't take the stress"

- "Closing fund, returning capital"

- **Liquidate at absolute worst prices**

**Stage 5: PTSD (Months later)**

- Many portfolio managers never returned to strategy

- Industry permanently scarred

- **Structural changes:** Lower leverage, better risk management

### 10. Preventing the Worst Case


**The Four Pillars of Survival:**

**Pillar 1: Credit analysis is PARAMOUNT**

$$
\boxed{\text{Credit Risk} > \text{Options Risk}}
$$

**Must do:**

- Full credit analysis (balance sheet, cash flow, debt coverage)

- Monitor credit default swaps daily

- Stress test: "What if credit spreads double?"

- Diversify credit exposure (max 10% per name)

**Credit checklist before every trade:**

- □ Debt/EBITDA < 3×?

- □ Interest coverage > 5×?

- □ Credit rating ≥ BBB?

- □ CDS < 300 bps?

- □ Industry trends stable?

**Pillar 2: Leverage discipline**

$$
\text{Max Leverage} = \frac{1}{\text{Max Drawdown Tolerance}}
$$

**If can tolerate 20% drawdown:**

- Max leverage = 1 / 0.20 = 5×

**But use LESS! Markets exceed expectations!**

**Safe leverage rules:**

- Conservative: 2-3×

- Moderate: 3-4×  

- **NEVER > 5×** (suicide post-2005)

**Pillar 3: Entry price discipline**

**Must have cushion to bond floor:**

$$
\text{Minimum Cushion} = \frac{\text{Entry Price} - \text{Bond Floor}}{\text{Entry Price}} > 15\%
$$

**Example:**

- Entry price: $920

- Bond floor: $800

- Cushion: $(920 - 800) / 920 = 13%$

- **REJECT!** (Below 15% minimum)

**Only buy if:**

- At discount to fair value, AND

- Sufficient cushion to bond floor, AND

- Bond floor based on STRESS credit spreads (not current)

**Pillar 4: Position sizing and diversification**

**Per position limits:**

- Max 10% of portfolio per convert

- Max 20% in single industry

- Max 30% in similar credit quality

**Portfolio limits:**

- Minimum 10 positions

- Maximum correlation 0.3 across positions

- Regular stress testing

**Sizing formula:**

$$
\text{Max Size} = \frac{\text{Portfolio} \times 2\%}{\text{Max Loss per Convert}} 
$$

**Example:**

- Portfolio: $100M

- Max loss if credit collapses: 30% per convert

- **Max size:** $100M × 0.02 / 0.30 = $6.67M per convert

### 11. The Ultimate Protection: Stress Testing


**Required monthly stress tests:**

**Scenario 1: Credit event**

- All credit spreads +300 bps

- Bond floors drop 25%

- What's portfolio loss?

- **Must be < 20% of equity**

**Scenario 2: Market crash**

- Stocks down 30%

- Vol spikes to 60%

- Credit spreads +200 bps  

- What's P&L?

**Scenario 3: Liquidity crisis**

- Bid-ask spreads triple

- Forced to liquidate 50% of book

- What's slippage cost?

**If ANY scenario causes >30% loss:**

- **Reduce position size immediately**

- Add hedges

- Raise cash

### 12. The Final Wisdom


**Convertible arbitrage lessons from 2005:**

1. **Credit risk dominates** - Bond floor is not a floor if credit deteriorates

2. **Leverage kills** - Even great strategies fail with too much leverage

3. **Liquidity matters** - Can't exit when everyone exits together

4. **Correlations spike** - Diversification fails in crisis

5. **Forced selling spirals** - Margin calls force worst-price liquidations

**The professional convertible arbitrage trader's creed:**

> "I analyze credit more than options. I use minimal leverage. I demand entry price discipline. I diversify religiously. I stress test monthly. I'm still trading in 10 years because I survived 2005-style events that killed my peers."

**Position accordingly. The market WILL test you with credit events. Will you survive?**

$$
\boxed{\text{Survival} > \text{Optimization}}
$$



