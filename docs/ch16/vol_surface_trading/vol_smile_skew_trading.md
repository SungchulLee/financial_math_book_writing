# Volatility Smile and Skew Trading

**Volatility smile and skew trading** is a strategy where you profit from mispricing across different option strikes by exploiting the fact that options at different strikes trade at different implied volatilities.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/vol_smile_skew_trading_put_skew.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 1:** Vol Smile Skew Trading Put Skew visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/vol_smile_skew_trading_smile_dynamics.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 2:** Vol Smile Skew Trading Smile Dynamics visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/vol_smile_skew_trading_smile_pattern.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 3:** Vol Smile Skew Trading Smile Pattern visualization.

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/vol_smile_skew_trading_strategy.png?raw=true" alt="long_call_vs_put" width="700">
</p>

**Figure 4:** Vol Smile Skew Trading Strategy visualization.

---

## The Core Insight

**The fundamental idea:**

- Black-Scholes theory says: all options on the same stock should have the same implied volatility

- Reality: options at different strikes trade at DIFFERENT implied volatilities

- This creates a pattern called the "volatility smile" or "volatility skew"

- You can trade the SHAPE of this curve, not just the level

- Profit from relative mispricing across strikes

**The key observation:**

$$
\text{IV}_{\text{OTM put}} > \text{IV}_{\text{ATM}} < \text{IV}_{\text{OTM call}} \quad \text{(smile)}
$$

or

$$
\text{IV}_{\text{OTM put}} > \text{IV}_{\text{ATM}} > \text{IV}_{\text{OTM call}} \quad \text{(skew)}
$$

**You're essentially betting: "The market has the wrong shape for implied volatility across strikes."**

---

## What Is the Volatility Smile/Skew?

**Before trading it, we need to understand what it is:**

### The Black-Scholes Expectation

**Theory says:**

- All options on the same underlying, same expiration should have the same implied volatility

- Volatility is a property of the stock, not the strike

- Plot IV vs. Strike → should be flat line

**Example (theoretical):**

- Stock at $100

- ATM call (K=$100): IV = 20%

- OTM call (K=$110): IV = 20%

- OTM put (K=$90): IV = 20%

- **All the same!**

### The Market Reality

**In practice:**

- Different strikes trade at DIFFERENT implied volatilities

- Plot IV vs. Strike → curved line (smile or skew)

- This violates Black-Scholes assumptions

**Example (real market - equities):**

- Stock at $100

- OTM put (K=$90): IV = 25% (high!)

- ATM call (K=$100): IV = 20%

- OTM call (K=$110): IV = 18% (low!)

- **Downward sloping → "volatility skew"**

**Example (real market - FX):**

- EUR/USD at 1.10

- OTM put (K=1.05): IV = 12% (high)

- ATM (K=1.10): IV = 10%

- OTM call (K=1.15): IV = 12% (high)

- **U-shaped → "volatility smile"**

### Visualizing the Patterns

```
Equity Skew (typical):          FX Smile (typical):
    IV                              IV
     ↑                               ↑
  25%|  \                        12%|    /‾‾\
  20%|   \___                    10%|___/   \___
  15%|       \                    8%|
     |________\___→ Strike            |___________→ Strike
     90  100  110                    1.05 1.10 1.15
    OTM  ATM  OTM                    OTM  ATM  OTM
    Put      Call                    Put      Call
```

### Types of Patterns

**1. Volatility Skew (Equities, Indices)**

- Downward sloping from left to right

- OTM puts more expensive than OTM calls

- "Crash protection premium"

**2. Volatility Smile (FX, Some Commodities)**

- U-shaped curve

- Both wings elevated

- Symmetric or asymmetric

**3. Reverse Skew (Rare)**

- Upward sloping

- OTM calls more expensive than OTM puts

- Sometimes in takeover situations

---

## Why Does the Smile/Skew Exist?

**Several reasons why reality differs from Black-Scholes:**

### 1. Crash Fear (Equity Skew)

**Post-1987 phenomenon:**

- 1987 crash traumatized markets

- Deep fear of large downward moves

- Investors pay premium for downside protection

- OTM puts expensive (high IV)

**Supply/Demand:**

- Everyone wants to buy puts (protection)

- Limited sellers

- Price (IV) gets bid up

### 2. Fat Tails (Smile)

**Reality vs. Theory:**

- Black-Scholes assumes log-normal returns

- Reality: returns have fatter tails (more extreme moves)

- Both large ups AND downs more likely than theory

- Both wings (OTM puts and calls) elevated

### 3. Stochastic Volatility

**Volatility itself is random:**

- Black-Scholes assumes constant volatility

- Reality: volatility changes over time

- Volatility clustering (high vol persists)

- Creates smile pattern naturally

### 4. Jump Risk

**Discrete jumps:**

- Stocks can gap (earnings, news, takeovers)

- Black-Scholes assumes continuous price movement

- Jumps create demand for OTM options

- Elevates wings

### 5. Leverage Effect

**Stock down → volatility up:**

- When stock drops, leverage increases (debt/equity)

- Company becomes riskier

- Volatility increases

- Creates negative correlation between price and vol

- Produces skew

### 6. Supply/Demand Imbalances

**Structural demand:**

- Portfolio managers buy puts for insurance

- Covered call writers sell calls

- Corporate buybacks reduce call supply

- Creates persistent skew

---

## The Basic Idea

**What you do:**

### Identify Mispricing

**Compare current skew to:**

1. Historical average skew

2. Theoretical "fair" skew (model-based)

3. Cross-sectionally (this stock vs. others)

4. Intertemporally (front month vs. back month)

### Construct Trade

**Three main approaches:**

**A. Directional Skew Bet**

- Believe skew will steepen or flatten

- Trade structures that profit from shape changes

- Example: Butterfly spreads, risk reversals

**B. Relative Value**

- One strike looks cheap vs. another

- Buy cheap, sell expensive

- Hedge the net vega/delta

**C. Volatility Surface Arbitrage**

- Exploit inconsistencies across strikes AND maturities

- Complex multi-leg trades

- Statistical arbitrage

### Delta Hedge

**As always:**

- Maintain delta neutrality

- Focus on the skew exposure

- Not betting on stock direction

---

## The Portfolio

Your smile/skew trading portfolio consists of:

$$
\Pi = \sum_i w_i \cdot \text{Option}_i(K_i) + \text{Delta Hedge}
$$

where you hold options at multiple strikes $K_i$ with weights $w_i$.

**Why this structure?**


- Multiple strikes → exposure to skew shape

- Weights chosen to target specific skew sensitivity

- Delta hedge → isolate skew risk from directional risk

- Often vega-neutral too (trade pure skew)

**What you're exposed to:**


- ✓ Skew changes (your bet)

- ✓ Some gamma (from option positions)

- ✗ Delta (hedged away)

- ✗ Vega level (often hedged to be neutral)

---


---

## Economic Interpretation

**Understanding what volatility smile/skew trading REALLY represents economically:**

### The Core Economic Trade-Off

Volatility smile and skew trading is fundamentally about **exploiting market inefficiencies in how tail risk is priced across strikes**. You're not just trading volatility levels—you're trading the **shape of the fear distribution**.

**What you're really doing:**

$$
\text{Skew Trade} = \text{Long Underpriced Vol} + \text{Short Overpriced Vol} + \text{Delta Hedge}
$$

**The economic reality:**

$$
\text{Smile/Skew} = \underbrace{\text{Crash Fear}}_{\text{behavioral}} + \underbrace{\text{Supply/Demand}}_{\text{structural}} + \underbrace{\text{Fat Tails}}_{\text{statistical}}
$$

### Why the Smile/Skew Exists: The Five Forces

**Black-Scholes assumes:**

- Log-normal stock returns

- Constant volatility

- No jumps or crashes

- **Result:** Flat implied volatility across strikes

**Reality violates ALL these assumptions!**

#### Force 1: Crash Fear (Post-1987)

**The 1987 crash changed everything:**

**Before October 1987:**

- Volatility smile relatively flat

- Markets assumed normal distributions

- 20% one-day crash considered "impossible"

**After October 19, 1987:**

- Dow dropped 22.6% in ONE DAY

- Options traders realized: **Crashes happen!**

- Put options became insurance against disasters

- **Demand for OTM puts spiked permanently**

**Economic result:**
$$
\text{IV}_{\text{OTM Put}} > \text{IV}_{\text{ATM}}
$$

**The mechanism:**

- Investors want protection against crashes

- Buy OTM puts (insurance)

- **Demand >> Supply** for downside protection

- Puts trade at higher IV (more expensive)

- **This creates the skew!**

**Example (SPX options):**

- SPX at 4,500

- ATM straddle (K=4500): IV = 18%

- 10% OTM put (K=4050): IV = 22% (+4 vol points!)

- 10% OTM call (K=4950): IV = 16% (-2 vol points)

- **Skew slope: -0.6 vol points per 1% moneyness**

**Why this persists:**

- Behavioral: Fear > Greed (loss aversion)

- Institutional: Portfolio insurance demand constant

- Structural: Put sellers require premium for tail risk

#### Force 2: Fat Tails (Leptokurtosis)

**Black-Scholes assumes normal distribution:**

- Kurtosis = 3 (thin tails)

- Extreme moves rare (3-sigma = 0.3% chance)

- 5-sigma moves "never" happen

**Real stock returns have fat tails:**

- Kurtosis = 5-7 (fat tails!)

- 3-sigma moves: ~2% of days (vs. 0.3% theoretical)

- 5-sigma+ moves: Happen every few years (vs. never)

**Historical evidence:**

- October 1987: -22.6% (20+ sigma event!)

- March 2020 COVID: -12% days (10+ sigma)

- **Conclusion:** Extreme moves FAR more common than normal distribution predicts

**Economic implication:**
$$
P(\text{Large Move}) _{\text{Real}} > P(\text{Large Move})_{\text{Black-Scholes}}
$$

**Therefore:**

- OTM options (protecting against large moves) too cheap under BS

- Market corrects by trading them at **higher IV**

- Creates smile/skew pattern

**Mathematical correction:**

Black-Scholes underprices tails. Market adds "correction factor":

$$
\text{IV}(K) = \text{ATM IV} + \alpha \times \left(\frac{K - S}{S}\right) + \beta \times \left(\frac{K - S}{S}\right)^2
$$

Where:

- $\alpha$ = skew slope (typically negative for equities)

- $\beta$ = smile curvature (convexity term)

#### Force 3: Supply and Demand Imbalance

**Options are NOT created equal in supply/demand:**

**Demand side (buyers):**

- **OTM puts:** Huge demand from:

  - Portfolio managers (hedge $trillions in equity)

  - Pension funds (downside protection mandate)

  - Retail investors (FOMO crash protection post-2008)

- **ATM options:** Moderate demand (speculation, volatility trading)

- **OTM calls:** Lower demand (some covered call sellers buy them back)

**Supply side (sellers):**

- **OTM puts:** Limited supply (scary to sell unlimited downside)

- **ATM options:** Market makers provide (delta hedgable)

- **OTM calls:** Lots of supply (covered call programs, buy-write funds)

**Net effect:**

$$
\text{Skew} = \frac{\text{Put Demand} - \text{Put Supply}}{\text{Call Demand} - \text{Call Supply}}
$$

**Result for equities:**

- Put IV inflated (demand > supply)

- Call IV depressed (supply > demand)

- **Downward sloping skew**

**Example (AAPL):**

- AAPL at $180

- 90-day 10% OTM put (K=$162): IV = 28%

- 90-day ATM (K=$180): IV = 24%

- 90-day 10% OTM call (K=$198): IV = 22%

- **4% skew for puts, 2% for calls**

**Why?**

- Portfolio managers holding AAPL buy puts (hedge)

- Covered call sellers sell calls (income generation)

- Market makers balance supply/demand via pricing (IV)

#### Force 4: Sticky Strike Phenomenon

**Empirical observation:**

When stock moves, **strikes don't move**—they're sticky!

**Example:**

- **t=0:** SPX at 4,500, buy 4,400 put at IV=20%

- **t=1:** SPX drops to 4,400

- **Question:** What's IV of 4,400 put now?

**Two models:**

**Model 1: Sticky delta**

- 4,400 put was 2% OTM, now ATM

- Should trade at ATM IV now

- **Prediction:** IV drops 20% → 18%

**Model 2: Sticky strike**

- 4,400 strike always trades at ~20% IV

- Doesn't matter if ATM or OTM

- **Prediction:** IV stays at 20%

**Empirical reality: Sticky strike wins!**

**Why this creates trading opportunities:**

- Stock moves change which strikes are ATM/OTM

- But IV at each strike stays relatively constant

- **You can trade the moneyness changes**

**Example trade:**

- Skew currently: 20% (ATM) to 25% (10% OTM put)

- Expect stock to drop 5%

- **After drop:** What was ATM becomes OTM → IV rises!

- **Profit:** Rising IV on your options

#### Force 5: Volatility Clustering

**Volatility is NOT constant (BS assumes it is):**

**Empirical fact:**

- High volatility periods cluster

- Low volatility periods cluster

- Volatility has **positive autocorrelation**

**GARCH effect:**

- Today's high vol → tomorrow likely high vol

- **Volatility is predictable!**

**Impact on smile:**

**Low vol regime:**

- Smile relatively flat

- OTM options trade closer to ATM

- Market complacent

**High vol regime:**

- Smile steepens dramatically!

- OTM puts trade 5-10 vol points above ATM

- Fear premium spikes

**Example (SPX 2017 vs 2020):**

**January 2017 (VIX = 11, low vol):**

- ATM: IV = 11%

- 10% OTM put: IV = 13% (skew = 2%)

- **Smile flat**

**March 2020 (VIX = 65, high vol):**

- ATM: IV = 65%

- 10% OTM put: IV = 85% (skew = 20%!)

- **Smile ultra-steep**

**Trading implication:**

- **Sell skew in low vol** (will steepen when vol rises)

- **Buy skew in high vol** (will flatten when vol falls)

### The Professional Institutional Perspective

**How different players view the smile/skew:**

#### Market Makers (Citadel, Susquehanna, IMC)

**Business model:**

- Provide liquidity on ALL strikes

- Quote bid/ask on every option

- **Goal:** Capture bid-ask spread, stay delta/vega neutral

**Skew management:**

- Long skew from retail buying puts (hedge demand)

- Short skew from institutional selling calls (overwriting)

- **Net position:** Often long skew (short OTM puts, long OTM calls)

**Hedging:**

- Use variance swaps to hedge vega

- Use skew swaps to hedge skew risk explicitly

- Dynamic delta hedging

**P&L sources:**

- Bid-ask spread capture

- Skew trading (buy cheap, sell expensive)

- Gamma scalping

#### Hedge Funds (Volatility Arbitrage Funds)

**Examples:** Capstone, Ronin, IMC

**Strategy:**

- Identify mispriced skew

- Trade mean-reversion in skew

- **Example:** If 25-delta skew at 5 vol points (high vs. 3 historical average)

  - Sell skew (sell OTM puts, buy OTM calls)

  - Wait for skew to revert to 3

  - Close for profit

**Sizing:**

- Vega-neutral (don't want directional vol exposure)

- Skew exposure: 1,000-10,000 vega per vol point

- **Example:** If skew tightens 1 vol point = $10,000 profit

#### Investment Banks (Goldman, JPM, Morgan Stanley)

**Business model:**

- Sell structured products to clients

- Often short volatility/skew

- **Need to hedge**

**Example:**

- Sell autocallable note to client

- Note is short volatility + short skew

- Bank hedges by buying options (becomes long skew)

- Banks accumulate long skew positions

**Impact on market:**

- Banks keep OTM put IV elevated (continuous buying)

- This supports the skew structure

#### Pension Funds / Asset Managers

**Holdings:** $trillions in equities

**Mandate:** Protect downside

**Solution:** Buy OTM puts

**Effect:**

- Constant structural demand for downside protection

- **Permanently inflates put skew**

- This is a STRUCTURAL feature, not temporary

**Quantitative evidence:**

- AUM of equity portfolios: ~$50 trillion globally

- Even 1% hedged = $500B in put demand

- **Massive** compared to options market size

- **Result:** Persistent skew

### Why Skew Trading Offers Economic Edge

**The strategy works when:**

#### 1. Skew Mean-Reversion

**Historical observation:**

- Skew fluctuates but reverts to long-term average

- **SPX 25-delta skew:**

  - Long-term average: ~4 vol points

  - Range: 2-8 vol points

  - Mean-reverting!

**Trade:**

- Skew at 7 vol points (elevated) → Sell skew

- Skew at 2 vol points (flat) → Buy skew

- **Expectation:** Reversion to 4

**Probability:**

- ~70% mean-reversion over 1-3 months

- **Expected value positive**

#### 2. Volatility Regime Changes

**Low vol → High vol transition:**

- Skew steepens (always!)

- **Be long skew** entering turbulence

**High vol → Low vol transition:**

- Skew flattens (always!)

- **Be short skew** entering calm

**Historical pattern:**

- 2017: VIX 10-12, skew flat → 2018: VIX spike, skew steep

- 2019: VIX 12-15, skew normal → 2020: VIX 80, skew ultra-steep

- **Predictable pattern!**

#### 3. Event Risk Mispricing

**Before known events (earnings, Fed, elections):**

- Market prices in general volatility

- But often **mis-prices the skew!**

**Example:**

- Earnings next week

- ATM IV rises 30% → 40% (correct)

- But skew should steepen (downside earnings miss scarier than upside beat)

- If skew doesn't steepen enough → **Buy skew** pre-earnings

**Statistical edge:**

- Historical: Earnings create -0.5 vol point skew steepening

- If market only prices +0.2 → **Arb opportunity**

### The Mathematical Framework

**Defining skew mathematically:**

**Risk reversal (most common):**
$$
\text{Skew} = \text{IV}_{25\Delta \text{ Put}} - \text{IV}_{25\Delta \text{ Call}}
$$

**Typical values (SPX):**

- Normal market: 3-5 vol points

- Stressed market: 8-15 vol points

- Crisis: 20+ vol points

**Butterfly (smile curvature):**
$$
\text{Butterfly} = \frac{\text{IV}_{25\Delta \text{ Put}} + \text{IV}_{25\Delta \text{ Call}}}{2} - \text{IV}_{\text{ATM}}
$$

**Interpreting:**

- Positive butterfly = U-shaped smile

- Negative butterfly = Inverted (rare)

- Zero butterfly = Pure skew (no smile)

**Trading the numbers:**

**Sell risk reversal (bet on skew flattening):**

- Sell 25-delta put at IV=25%

- Buy 25-delta call at IV=20%

- **Collect:** 5 vol points × vega

- **Profit if:** Skew narrows to 3 vol points

**Example P&L:**

- Vega per contract: $40 per vol point

- 10 contracts = 400 vega

- Skew tightens 5 → 3 (2 vol points)

- **Profit: 400 × 2 = $800**

### Why Smile Trading Has Become Harder (Post-2008)

**Pre-2008:**

- Less competition

- Wider skew mis-pricing

- Easier edges (4-6% annual returns common)

**Post-2008:**

- More volatility hedge funds

- Better models (SVJ, Heston)

- Tighter markets

- **Returns:** 2-4% annual (still positive but harder)

**Key changes:**

1. **Better analytics:**

   - Every fund has skew monitoring

   - Real-time tracking of skew vs. historical

   - **Harder to find mispricing**

2. **More capital:**

   - $10B+ in vol arb funds globally

   - Competition eliminates inefficiencies faster

3. **Smarter market makers:**

   - Use machine learning for skew pricing

   - Adjust quotes based on order flow

   - **Bid-ask spreads tighter**

4. **Regulation (Dodd-Frank, MiFID):**

   - More reporting requirements

   - Higher capital requirements

   - **Reduces leverage available**

### Summary of Economic Insights

**The volatility smile/skew exists because:**

1. **Crash fear** - 1987 permanently changed psychology

2. **Fat tails** - Real distributions have thicker tails than Black-Scholes

3. **Supply/demand** - Structural put demand from portfolio hedging

4. **Sticky strikes** - Options trade at strike-specific IV

5. **Vol clustering** - Volatility regimes create smile dynamics

**Trading opportunities arise from:**

- Skew mean-reversion (primary edge)

- Volatility regime transitions (secondary edge)

- Event risk mispricing (tactical edge)

**The professional approach:**

- Vega-neutral skew trades (avoid directional vol risk)

- Statistical arbitrage (trade deviations from historical norms)

- Risk management (skew can widen further than you think!)

**Master the smile → Understand options market structure.**

---



## Common Skew Trading Strategies

### 1. Butterfly Spread

**The classic skew trade:**

**Structure:**

- Buy 1 OTM put (low strike)

- Sell 2 ATM options (middle strike)  

- Buy 1 OTM call (high strike)

**Example:**

- Stock at $100

- Buy 1 put K=$90 (IV = 25%)

- Sell 2 calls K=$100 (IV = 20%)

- Buy 1 call K=$110 (IV = 18%)

**Position characteristics:**

- Delta-neutral (approximately)

- Limited risk (max loss = net debit)

- Profits if realized vol is low (stock stays near middle)

- **Skew exposure:** Short the wings (high IV), long the body (low IV)

**When to use:**

- Believe smile is too pronounced (wings too expensive)

- Expect stock to stay in range

- Volatility will be realized mostly at-the-money

**P&L at expiry:**
```
    P&L
     ↑
     |      /‾‾\
     |     /    \

  ---+----/------\----
     |   /        \
     |__/          \___
        90  100  110  Strike
```

Maximum profit if stock exactly at $100 at expiry.

### 2. Risk Reversal (Collar)

**Directional skew bet:**

**Structure:**

- Buy OTM call

- Sell OTM put (same distance from ATM)

**Example:**

- Stock at $100

- Buy call K=$110 (IV = 18%)

- Sell put K=$90 (IV = 25%)

**Position characteristics:**

- Positive delta (bullish bias)

- Skew exposure: Short the steep part (put), long the flat part (call)

- **Zero cost or small credit** (put premium > call premium due to skew)

**When to use:**

- Believe skew will flatten

- Bullish on stock (positive delta is feature, not bug)

- Puts are overpriced relative to calls

**Skew bet:**

- If skew flattens (put IV drops, call IV rises) → profit

- If skew steepens (put IV rises, call IV drops) → loss

### 3. Call Spread vs. Put Spread Arbitrage

**Relative value between call spreads and put spreads:**

**Structure:**

- Buy call spread (buy low strike call, sell high strike call)

- Sell put spread (sell low strike put, buy high strike put)

**Example:**

- Buy $100-110 call spread

- Sell $90-100 put spread

**Position characteristics:**

- Delta-neutral (if strikes chosen appropriately)

- Profits from skew mispricing

- Put spread expensive → sell it

- Call spread cheap → buy it

**When to use:**

- Put-call parity violations due to skew

- Statistical arbitrage

### 4. Skew Straddle/Strangle

**Modified straddle exploiting skew:**

**Structure:**

- Instead of buying ATM straddle (call + put same strike)

- Buy OTM put (expensive, high IV)

- Sell OTM call (cheap, low IV)

- Approximately delta-neutral

**When to use:**

- Capture skew premium

- Neutral to slightly bearish

- Collect from expensive puts, pay less for calls

### 5. Vertical Spread Compression

**Trade relative richness within same side:**

**Structure:**

- Within puts: Sell near-ATM put, buy far-OTM put

- The spread in IV between them may be too wide

**Example:**

- Stock at $100

- Sell put K=$95 (IV = 23%)

- Buy put K=$85 (IV = 28%)

- Skew says $85 put too expensive relative to $95 put

**When to use:**

- Skew is too steep even within one wing

- Believe spread will compress

---

## Measuring Skew

**How to quantify skew:**

### 1. 25-Delta Risk Reversal

**Market standard:**

$$
\text{25Δ RR} = \text{IV}_{25\Delta \text{ call}} - \text{IV}_{25\Delta \text{ put}}
$$

**What it measures:**

- Difference in IV between 25-delta call and put

- Positive value → puts more expensive (typical equity skew)

- More negative → steeper skew

**Example:**

- 25Δ put IV = 25%

- 25Δ call IV = 18%  

- RR = 18% - 25% = -7%

- Steep skew (typical equities)

### 2. 25-Delta Butterfly

**Market standard for smile:**

$$
\text{25Δ BF} = \frac{\text{IV}_{25\Delta \text{ call}} + \text{IV}_{25\Delta \text{ put}}}{2} - \text{IV}_{\text{ATM}}
$$

**What it measures:**

- How elevated the wings are vs. the body

- Higher value → more pronounced smile

### 3. Skew Slope

**Simple measure:**

$$
\text{Skew Slope} = \frac{\text{IV}_{90\% \text{ strike}} - \text{IV}_{110\% \text{ strike}}}{20\%}
$$

**Normalized by moneyness.**

### 4. At-The-Money vs. Out-of-The-Money Spread

$$
\text{Skew Spread} = \text{IV}_{\text{OTM put}} - \text{IV}_{\text{ATM}}
$$

**Direct measure of downside protection premium.**

---

## The P&L Sources

**Your P&L from skew trading comes from:**

### 1. Skew Change (Primary)

$$
\text{Skew P\&L} = \sum_i \text{Vega}_i \times \Delta \text{IV}_i
$$

**In plain English:**

- Each option position has vega at its strike

- IV at each strike can change independently

- Your P&L depends on relative IV changes

**Example (Butterfly):**

- Long wings (high IV strikes): Vega × (-ΔIV) if wings compress

- Short body (low IV strike): Vega × (+ΔIV) if body expands  

- Net: Profit if smile flattens

### 2. Realized Volatility vs. Implied (Secondary)

**Still have gamma exposure:**

- Multiple option positions → net gamma

- Stock moves → rebalancing P&L

- Similar to gamma scalping but with skew bias

### 3. Time Decay (Theta)

**Net theta depends on structure:**

- Butterflies: usually positive theta (short ATM, long wings)

- Risk reversals: depends on specifics

- Must manage this

### 4. Vega Changes (If Not Neutral)

**Overall IV level changes:**

- If not vega-neutral, exposed to parallel shifts

- Separate from skew changes

**Complete P&L:**

$$
\delta \Pi \approx \sum_i \text{Vega}_i \cdot \delta \text{IV}_i + \frac{1}{2}\Gamma(\delta S)^2 - \theta \, \delta t
$$

**Primary bet:** The $\sum_i \text{Vega}_i \cdot \delta \text{IV}_i$ term where IVs at different strikes change differently.

---

## Concrete Example: Trading a Steep Skew

**Setup:**

**Stock:** Tech company at $100

**Your analysis:**

- Current skew is historically steep

- OTM put IV = 30%

- ATM IV = 22%

- OTM call IV = 18%

- **Skew spread: 30% - 22% = 8%** (vs. historical average of 5%)

**Your view:** "Skew will normalize (flatten) toward 5% spread"

**The Trade: Butterfly Spread**

**Positions:**

1. Buy 10 OTM puts K=$90 at IV=30%

         - Cost: $2.50 per contract

         - Vega: 0.15 per contract

         - Total cost: $2,500

2. Sell 20 ATM calls K=$100 at IV=22%

         - Receive: $4.00 per contract

         - Vega: -0.25 per contract (short)

         - Total receive: $8,000

3. Buy 10 OTM calls K=$110 at IV=18%

         - Cost: $1.50 per contract

         - Vega: 0.15 per contract

         - Total cost: $1,500

**Net cost:** $2,500 - $8,000 + $1,500 = **-$4,000** (credit!)

**Delta hedge:** Position is approximately delta-neutral initially

**Scenario 1: Skew Normalizes (You're Right!)**

After 30 days:

- Stock still at $100 (no movement)

- Skew flattens toward historical average

- OTM put IV: 30% → 27% (-3%)

- ATM IV: 22% → 22% (unchanged)

- OTM call IV: 18% → 20% (+2%)

**Your P&L:**

- **Wing puts:** 10 × 0.15 × (-3%) = -0.45 per share = -$450

- **ATM calls:** 20 × (-0.25) × 0 = 0

- **Wing calls:** 10 × 0.15 × (+2%) = +0.30 per share = +$300

- **Net from skew change:** -$450 + $300 = **-$150** (small loss from skew)

**But also:**

- **Theta earned:** Positive (short ATM, long wings) ≈ +$600

- **Gamma P&L:** Small (stock didn't move) ≈ $0

- **Total P&L:** -$150 + $600 = **+$450**

Plus you initially collected $4,000, so total profit!

**Scenario 2: Skew Steepens (You're Wrong)**

After 30 days:

- Stock still at $100

- Skew gets even steeper (crisis fear)

- OTM put IV: 30% → 35% (+5%)

- ATM IV: 22% → 23% (+1%)

- OTM call IV: 18% → 17% (-1%)

**Your P&L:**

- **Wing puts:** 10 × 0.15 × (+5%) = +0.75 per share = +$750

- **ATM calls:** 20 × (-0.25) × (+1%) = -0.05 per share × 20 = -$500

- **Wing calls:** 10 × 0.15 × (-1%) = -0.15 per share = -$150

- **Net from skew change:** +$750 - $500 - $150 = **+$100**

Wait, you made money? That's because wings moved more than body!

**But:**

- **Theta earned:** +$600

- **Total:** +$100 + $600 = **+$700**

Actually still profitable due to theta! (This shows butterflies can be complex.)

---

## Smile/Skew Trading vs. Other Strategies

| Strategy | What You Trade | Primary Exposure | Need Multiple Strikes? |
|----------|---------------|------------------|----------------------|
| **Delta Hedging** | Nothing (risk mgmt) | None | No |
| **Gamma Scalping** | Realized vol (level) | Gamma | No (single ATM) |
| **Vega Trading** | Implied vol (level) | Vega | No (single strike) |
| **Smile/Skew Trading** | Implied vol (shape) | Relative vega | **YES (multiple strikes)** |
| **Dispersion** | Correlation | Multi-asset | YES (many assets) |
| **Variance Swaps** | Realized variance | Pure variance | No (single contract) |

### Key Differences

**Smile/Skew vs. Vega Trading:**

| Aspect | Vega Trading | Smile/Skew Trading |
|--------|-------------|-------------------|
| **What you trade** | IV level (all strikes move together) | IV shape (strikes move independently) |
| **Position** | Single strike (typically ATM) | Multiple strikes |
| **Hedging** | Delta hedge | Delta hedge + often vega-neutral |
| **Exposure** | Parallel shift in IV | Twist/curve in IV |
| **Example bet** | "IV will go from 20% to 25%" | "OTM puts will cheapen relative to ATM" |

**Smile/Skew vs. Gamma Scalping:**

| Aspect | Gamma Scalping | Smile/Skew Trading |
|--------|---------------|-------------------|
| **Profit source** | Realized volatility | Implied volatility shape |
| **What matters** | How much stock moves | Relative pricing across strikes |
| **Hedging** | Delta only | Delta + often vega |
| **Time horizon** | Hold to expiry (weeks-months) | Can be shorter (days-weeks) |

---

## Why Smile/Skew Trading Exists

**Why do opportunities persist?**

### 1. Structural Demand

**Persistent forces:**

- Portfolio insurance (demand for puts)

- Covered call writing (supply of calls)

- Corporate hedging

- Creates sustained skew

### 2. Behavioral Biases

**Market psychology:**

- Fear is stronger than greed (put demand)

- Crash fear persists (post-1987)

- Recency bias

- Loss aversion

### 3. Model Limitations

**Black-Scholes inadequacy:**

- Real returns aren't log-normal

- Volatility isn't constant

- Jumps exist

- Smile reflects these realities

### 4. Supply/Demand Imbalances

**Temporary dislocations:**

- Hedging flows (OpEx, rebalancing)

- Dealer positioning

- Market microstructure

### 5. Information Asymmetry

**Different market participants:**

- Some understand skew dynamics

- Others just buy/sell for hedging

- Creates opportunities for informed traders

---

## Pros and Cons

### Advantages ✓

**1. Additional dimension to trade**

- Beyond just "high vol" or "low vol"

- Can trade the curve, not just the level

- More opportunities

**2. Mean reversion**

- Skew tends to revert to historical averages

- Provides statistical edge

- Quantifiable with data

**3. Can be delta-neutral and vega-neutral**

- Pure skew exposure

- Minimal directional or level risk

- Focused bet

**4. Multiple strategies available**

- Butterflies, risk reversals, spreads

- Different risk/reward profiles

- Flexibility

**5. Structural edges**

- Persistent supply/demand imbalances

- Behavioral biases

- Market inefficiencies

**6. Lower capital requirements than dispersion**

- Single asset (not 10-50)

- More accessible than full dispersion

**7. Shorter time horizons possible**

- Skew can change in days/weeks

- Don't need to wait months

- More dynamic trading

### Disadvantages ✗

**1. Complexity**

- Must understand multi-leg options

- Greeks across strikes

- More moving parts than single-strike trades

**2. Transaction costs multiply**

- Trading multiple strikes

- Each leg has bid-ask spread

- Can erode profits

**3. Model risk**

- What's the "right" skew?

- How to define mispricing?

- Model-dependent

**4. Multiple risk factors**

- Still have gamma, theta, vega level

- Not purely skew exposure

- Complex risk management

**5. Can be wrong on direction**

- Skew can steepen when you expect flattening

- Mean reversion can take time

- Structural changes can shift "normal"

**6. Liquidity varies**

- ATM most liquid

- Wings can be illiquid

- Wider spreads on OTM

**7. Requires sophistication**

- Not beginner-friendly

- Need advanced options knowledge

- Risk management crucial

**8. Gamma can dominate**

- If stock moves a lot, gamma P&L > skew P&L

- Your skew bet becomes secondary

- Hard to isolate pure skew

---

## When Smile/Skew Trading Works Best

### For "Short Skew" (Skew Flattening Bets)

**Favorable conditions:**

- **Historically steep skew** (high percentile)

- **Post-crisis environment** (fear elevated)

- **VIX elevated but declining**

- **Put IV elevated relative to calls**

- **Strong trend or low realized vol**

**Example trades:**

- Butterflies (short wings, long body)

- Long risk reversals (if also bullish)

**Markets:**

- Equities after panic

- Indices post-crash

- Individual stocks after earnings fear

### For "Long Skew" (Skew Steepening Bets)

**Favorable conditions:**

- **Historically flat skew** (low percentile)

- **Complacent markets** (extended rally)

- **VIX low and grinding lower**

- **Put IV cheap relative to calls**

- **Building fragility**

**Example trades:**

- Reverse butterflies

- Short risk reversals (also hedges downside)

**Markets:**

- Equities in late bull market

- Before earnings or events

- When protection is cheap

### For Relative Value

**Favorable conditions:**

- Clear mispricing between strikes

- Mean reversion expected

- Liquid markets (tight spreads)

- Statistical edge identified

**Example trades:**

- Calendar spreads across skew

- Vertical spread arb

- Cross-strike relative value

---

## Measuring Success: Skew P&L Attribution

**How to know if you made money from skew vs. other factors:**

### P&L Decomposition

$$
\text{Total P\&L} = \underbrace{\text{Skew P\&L}}_{\text{your bet}} + \underbrace{\text{Parallel Vega P\&L}}_{\text{level change}} + \underbrace{\text{Gamma P\&L}}_{\text{realized vol}} + \underbrace{\text{Theta P\&L}}_{\text{time decay}}
$$

**Isolating skew P&L:**

1. **Mark IVs at each strike** at entry and exit

2. **Calculate parallel shift:** Average IV change across strikes

3. **Calculate skew change:** IV changes relative to average

4. **Attribute P&L:**

   - Parallel: $\sum \text{Vega}_i \times \text{Average IV change}$

   - Skew: $\sum \text{Vega}_i \times (\Delta \text{IV}_i - \text{Average IV change})$

**Example:**

- Entry: Put IV=30%, ATM IV=22%, Call IV=18%

- Exit: Put IV=32%, ATM IV=25%, Call IV=23%

- **Parallel shift:** Average increase = +3%

- **Skew changes:** Put: +2%-3%=-1%, ATM: +3%-3%=0%, Call: +5%-3%=+2%

- Skew flattened (call caught up)!

---

## Advanced: Skew Dynamics

**How skew changes over time:**

### Sticky Strike vs. Sticky Delta

**Two models for skew behavior:**

**Sticky Strike:**

- IV at each fixed strike stays constant

- As stock moves, new strikes become ATM

- Skew curve shifts with spot

**Sticky Delta:**

- IV at each delta level stays constant

- 25-delta put always has same IV

- Skew curve moves with spot

**Reality:** Somewhere in between, market-dependent

### Term Structure of Skew

**Skew varies by maturity:**

- Front-month: often steeper

- Back-month: often flatter

- Can trade term structure of skew

**Example structure:**

- 1-month skew: 8% spread

- 3-month skew: 6% spread

- 6-month skew: 5% spread

**Trade:** Calendar spread exploiting term structure differences

---


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


## Real-World Examples

### Example 1: Post-Earnings Skew Crush

**Before earnings:**

- Implied volatility elevated across all strikes

- Skew steep (fear of downside surprise)

**After earnings (stock moves 5%):**

- IV collapses across all strikes

- Skew normalizes

- Butterfly profits from both IV decline and skew normalization

### Example 2: 2008 Financial Crisis

**Pre-crisis:**

- Equity skew moderate

- OTM puts relatively cheap

**During crisis:**

- Skew steepened dramatically

- Put IV exploded

- Long skew positions (long OTM puts) highly profitable

**Post-crisis:**

- Skew remained elevated for years

- "New normal" for equity skew

- Structural shift

### Example 3: GameStop Short Squeeze (Jan 2021)

**During squeeze:**

- Call IV exploded (everyone wanted calls)

- Put IV elevated but less so

- **Reverse skew:** Calls more expensive than puts!

- Rare opportunity

**Trade:**

- Short risk reversals (sell expensive calls, buy cheaper puts)

- Profit as skew normalized

---

## Practical Implementation

### 1. Skew Screening

**Identify opportunities:**

- Calculate current skew metrics (RR, BF)

- Compare to historical percentiles

- Flag extreme readings

- Check liquidity

**Tools:**

- Bloomberg: SKEW function

- Option analytics platforms

- Custom Python scripts

### 2. Position Construction

**Choose structure based on:**

- View (steepening vs. flattening)

- Risk appetite

- Capital available

- Liquidity constraints

**Common structures:**

- Conservative: Butterflies (limited risk)

- Aggressive: Naked skew bets

- Balanced: Risk reversals with delta hedge

### 3. Risk Management

**Monitor:**

- Skew metrics daily

- Delta drift (rebalance as needed)

- Net vega (manage level exposure)

- P&L attribution

**Limits:**

- Maximum vega per strike

- Maximum net vega (level exposure)

- Stop-loss on skew widening beyond threshold

### 4. Exit Discipline

**Exit when:**

- Skew normalizes to target

- Structural change invalidates thesis

- Better opportunities elsewhere

- Risk/reward deteriorates

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


## What to Remember

### Core Concept

**The volatility smile/skew is the pattern of implied volatilities across strikes:**

$$
\text{IV}(K) \neq \text{constant}
$$

- Black-Scholes says it should be flat

- Reality: curved (smile or skew)

- You trade the SHAPE, not just the LEVEL

### Why It Exists

**Violations of Black-Scholes assumptions:**

1. Fat tails (extreme moves more likely)

2. Stochastic volatility (vol changes)

3. Jumps (discrete price moves)

4. Leverage effect (price-vol correlation)

5. Supply/demand (structural hedging demand)

### Two Main Patterns

**Equity Skew:**

- Downward sloping (OTM puts > ATM > OTM calls)

- Crash fear premium

- Most common in equities/indices

**FX Smile:**

- U-shaped (both wings elevated)

- Fat tails on both sides

- Symmetric or asymmetric

### Common Strategies

**1. Butterflies:**

- Trade smile richness/cheapness

- Long wings + short body or vice versa

- Limited risk

**2. Risk Reversals:**

- Trade skew slope

- Long call + short put or vice versa

- Directional bias

**3. Spread Arb:**

- Relative value within one wing

- Exploit steep skew within puts or calls

### Measuring Skew

**Market standards:**

- **25Δ Risk Reversal:** Call IV - Put IV

- **25Δ Butterfly:** (Call IV + Put IV)/2 - ATM IV

- **Skew spread:** OTM put IV - ATM IV

### Comparison to Other Strategies

| What You Trade | Strategy |
|---------------|----------|
| Volatility **level** | Vega trading, gamma scalping |
| Volatility **shape** | Smile/skew trading |
| Volatility **term structure** | Calendar spreads |
| **Multi-asset** correlation | Dispersion trading |

**All build on delta hedging foundation!**

### Success Factors

**What you need:**

1. **Statistical edge:** Historical analysis of skew

2. **Market view:** Will skew steepen or flatten?

3. **Execution:** Manage transaction costs

4. **Risk management:** Multiple Greeks to monitor

5. **Patience:** Mean reversion takes time

### The Deep Insight

**Smile/skew trading reveals:**

- Markets are smarter than Black-Scholes

- Risk is multidimensional (not just "high" or "low" vol)

- Strike matters (not all options are created equal)

- Shape contains information (market's view of tail risk)

**The pattern reflects:**

- Collective market fears (crash protection)

- Real return distribution (fat tails)

- Structural supply/demand (portfolio insurance)

### Your Complete Toolkit Now

**Seven strategies, all built on delta hedging:**

1. **Delta Hedging** → Risk management

2. **Gamma Scalping** → Realized vol (level)

3. **Vega Trading** → Implied vol (level)

4. **Smile/Skew Trading** → Implied vol (shape) ✓

5. **Dispersion Trading** → Multi-asset correlation

6. **Convertible Arb** → Multi-factor

7. **Variance Swaps** → Pure realized variance

**Each adds a dimension:**

- Level (gamma, vega)

- Shape (smile/skew) ← New!

- Time (calendar spreads - next?)

- Assets (dispersion)

- Factors (convertibles)

### Practical Wisdom

- **Skew mean-reverts** but slowly

- **Extreme readings** are opportunities

- **Transaction costs** matter (multiple legs)

- **Gamma can dominate** your skew bet

- **Liquidity varies** across strikes

- **Model risk** is significant

### Final Thought

**Smile/skew trading is about understanding that:**

"Not all volatility is created equal. The market pays different prices for different strikes because risk is multidimensional. Trade the curve, not just the level."

**This is sophisticated volatility trading:**

- Beyond single-strike bets

- Exploiting rich/cheap relationships

- Capturing structural inefficiencies

- But with complexity comes the need for discipline

**You're now trading the topology of the volatility surface!** 📈