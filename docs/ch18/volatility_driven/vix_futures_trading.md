# VIX Futures Trading


**VIX futures trading** is a volatility strategy where you trade futures contracts on the CBOE Volatility Index (VIX), profiting from changes in market fear and implied volatility levels, exploiting mean reversion, term structure dynamics, and volatility spikes during market stress.

---

## The Core Insight


**The fundamental idea:**

- VIX measures S&P 500 implied volatility (market fear gauge)
- VIX futures trade the EXPECTATION of future VIX levels
- VIX futures ≠ VIX index (critical difference!)
- VIX is mean-reverting (spikes don't last forever)
- VIX term structure usually in contango (near < far)
- Contango creates negative roll yield (decay for longs)
- Backwardation appears during crises (fear NOW > fear later)
- You can trade directionally OR harvest term structure carry
- Extreme leverage amplifies both profits and losses

**The key equations:**

$$
\text{VIX} = \sqrt{252 \times \text{Expected 30-day Variance of SPX}}
$$

$$
\text{Contango} = \frac{F_{\text{far}} - F_{\text{near}}}{F_{\text{near}}} \quad \text{(typical: 5-15\% per month)}
$$

$$
\text{VIX Futures P\&L} = \Delta F \times \$1,000 \times \text{Contracts}
$$

**You're essentially betting: "VIX will spike (go long) or decay from elevated levels (go short), and I can profit from directional moves, mean reversion, or term structure convergence while managing the extreme volatility and roll costs inherent in these instruments."**

---

## What Are VIX


**Before trading VIX futures, understand the critical mechanics:**

### 1. VIX Index vs VIX


**VIX Index (spot VIX):**

- Symbol: ^VIX or $VIX
- Calculation: 30-day implied volatility of S&P 500 options
- **Cannot be traded directly** (it's just a calculation)
- Typically 12-20 (calm) or 30-80 (crisis)
- Spikes during crashes (can hit 80+)
- Mean-reverting to ~15-18 long-term

**VIX Futures:**

- Symbol: /VX (front month), VX1-VX8 (monthly)
- Contract: $1,000 per VIX point
- **CAN be traded** (actual tradeable instruments)
- Typically trade ABOVE spot VIX (contango)
- Settlement: Cash-settled to VIX on expiration
- Expiration: Wednesday, 30 days before SPX options expiry

**The disconnect:**

$$
\text{VIX Futures} \neq \text{VIX Index}
$$

**Example:**

- VIX Index: 15.00 (spot)
- Front month VIX future: 16.50 (+10% premium)
- 2nd month VIX future: 17.80 (+18.7% premium)
- **This is contango**

**Why they differ:**

$$
F_{\text{VIX}} = \mathbb{E}[\text{VIX}_{T}] + \text{Risk Premium}
$$

- Futures price expected future VIX
- Plus premium for volatility risk
- **Futures > spot in normal markets**

### 2. VIX Term


**Definition:** The curve of VIX futures prices across expiration months.

**Normal shape (contango - 80% of the time):**

$$
\text{VIX} < F_1 < F_2 < F_3 < F_4 < ... < F_8
$$

**Example (calm market):**

| Contract | Days to Expiry | Price | Premium to Spot |
|----------|----------------|-------|-----------------|
| VIX spot | 0 | 15.00 | 0% |
| VX1 (Feb) | 30 | 16.50 | +10.0% |
| VX2 (Mar) | 60 | 17.80 | +18.7% |
| VX3 (Apr) | 90 | 18.50 | +23.3% |
| VX4 (May) | 120 | 19.00 | +26.7% |

**This contango structure creates massive roll decay for long positions!**

**Crisis shape (backwardation - 20% of the time):**

$$
\text{VIX} > F_1 > F_2 > F_3 > F_4
$$

**Example (market crash):**

| Contract | Days to Expiry | Price | Discount to Spot |
|----------|----------------|-------|------------------|
| VIX spot | 0 | 45.00 | 0% |
| VX1 (Feb) | 30 | 38.00 | -15.6% |
| VX2 (Mar) | 60 | 33.00 | -26.7% |
| VX3 (Apr) | 90 | 29.00 | -35.6% |
| VX4 (May) | 120 | 26.00 | -42.2% |

**Backwardation = extreme fear NOW, expected calm later**

### 3. How VIX Futures


**Contract specifications:**

- **Ticker:** /VX
- **Multiplier:** $1,000 per VIX point
- **Tick size:** 0.05 ($50 per contract)
- **Margin:** ~$5,000-15,000 (varies with volatility)
- **Trading hours:** Nearly 24/5
- **Settlement:** Cash to VIX index on Wed AM

**P&L calculation:**

$$
\text{P\&L} = (F_{\text{exit}} - F_{\text{entry}}) \times \$1,000 \times \text{Contracts}
$$

**Example:**

- Buy 10 VIX futures @ 17.00
- Sell @ 22.00
- Profit: (22.00 - 17.00) × $1,000 × 10 = **$50,000**

**Leverage:**

$$
\text{Notional} = 17.00 \times \$1,000 = \$17,000
$$

$$
\text{Margin} = \$7,000
$$

$$
\text{Leverage} = \frac{\$17,000}{\$7,000} = 2.4:1
$$

**Lower leverage than equity futures but MUCH higher volatility!**

### 4. The Roll Decay


**If you hold VIX futures long-term in contango:**

**Month 1:**

- Buy VX1 @ 16.50 (VIX spot 15.00)
- Hold to expiration
- VX1 converges to VIX spot
- VIX still at 15.00
- **Loss: 16.50 - 15.00 = 1.50 points ($1,500 per contract)**

**This is roll decay or contango bleed!**

**Annual cost of rolling longs in contango:**

$$
\text{Annual Decay} \approx 50\text{-}80\% \text{ of position value}
$$

**Example:**

- Start: $100,000 in VIX futures
- After 1 year of rolling in contango
- Ending value (if VIX unchanged): **$30,000-50,000**
- **Loss: $50,000-70,000 (50-70%!)**

**This is why buying and holding VIX futures is a LOSING strategy!**

### 5. Settlement and


**VIX futures settle to VIX index (spot):**

**Settlement process:**

1. **Final settlement date:** Wednesday morning
2. **Settlement time:** Market open (9:30 AM ET)
3. **Settlement value:** VIX index calculation
4. **Cash settlement:** Difference credited/debited

**Example:**

- Hold long VX1 @ 18.00
- Settlement day: VIX opens at 16.50
- Settlement P&L: (16.50 - 18.00) × $1,000 = **-$1,500**
- **No physical delivery, just cash**

**Expiration calendar:**

- VIX futures expire monthly
- Always 30 days before SPX monthly options
- Typically 3rd Wednesday of month (but check!)
- **Must roll or close before expiration**

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/vix_futures_term_structure.png?raw=true" alt="vix_futures_term_structure" width="700">
</p>
**Figure 1:** VIX futures term structure showing typical contango (upward sloping from spot VIX to far-dated contracts) and crisis backwardation (downward sloping). The convergence of near-term futures to spot VIX creates roll decay in contango and roll yield in backwardation, fundamentally affecting long-term position profitability.

---

## Economic


**Beyond the basic mechanics, understanding the economic rationale:**

### 1. VIX as Market


**The deep insight:**

VIX represents the **cost of portfolio insurance**—specifically, the annualized implied volatility of S&P 500 options. When VIX is high, insurance is expensive. When low, insurance is cheap.

**Formal representation:**

$$
\text{VIX} = 100 \times \sqrt{\frac{1}{T}\int_0^{\infty} \frac{e^{-rT}}{K^2}[C(K) + P(K)]dK}
$$

Simplified:

$$
\text{VIX} \approx \text{Annualized implied volatility of 30-day SPX options}
$$

**Economic meaning:**

$$
\frac{\text{VIX}}{100\sqrt{252}} = \text{Expected daily move in SPX}
$$

**Example:**

- VIX = 15
- Expected daily SPX move: $\frac{15}{100\sqrt{252}} = 0.94\%$
- VIX = 30
- Expected daily SPX move: $\frac{30}{100\sqrt{252}} = 1.89\%$

**VIX doubling = expected volatility doubling**

### 2. Why VIX Futures


**Economic reasons for persistent contango:**

**1. Volatility risk premium:**

Investors PAY to hedge tail risk:

$$
\mathbb{E}[\text{VIX futures return}] < 0
$$

**Long VIX = insurance seller's edge**

**Short VIX = collecting insurance premium**

**2. Mean reversion expectation:**

$$
\mathbb{E}[\text{VIX}_{t+30}] > \text{VIX}_t \quad \text{when VIX is low}
$$

When VIX at 12 (extreme low):

- Futures price in reversion to 15-16
- Premium justified
- **Market expects rise**

**3. Supply/demand imbalance:**

- Heavy demand for VIX long exposure (hedging)
- Limited natural sellers
- **Demand > supply → premium**

**4. Term structure of uncertainty:**

$$
\text{Uncertainty}_{\text{30-day}} < \text{Uncertainty}_{\text{60-day}}
$$

More time = more uncertainty → higher volatility expectation

**Empirical evidence:**

$$
\text{Average contango} = 5\text{-}10\% \text{ per month}
$$

**This means:**

Holding VIX futures long costs 5-10% per month in normal markets!

### 3. VIX Mean


**Statistical properties:**

VIX is strongly mean-reverting:

$$
d(\text{VIX}) = \kappa(\mu - \text{VIX})dt + \sigma \text{VIX}^{\gamma} dW_t
$$

Where:
- $\kappa$ = reversion speed (≈2-3 annually)
- $\mu$ = long-term mean (≈15-18)
- $\sigma$ = volatility of volatility
- $\gamma$ = elasticity (≈0.5-1.0)

**Key characteristics:**

**Half-life of VIX spike:**

$$
t_{1/2} = \frac{\ln(2)}{\kappa} \approx 3\text{-}6 \text{ months}
$$

**Example:**

- VIX spikes from 15 → 60 (300% increase)
- 3 months later: Expected VIX ≈ 37
- 6 months later: Expected VIX ≈ 26
- 12 months later: Expected VIX ≈ 18
- **Spikes decay rapidly**

**This creates short-VIX opportunity:**

$$
P(\text{VIX} > 30) \approx 5\% \text{ of days historically}
$$

$$
P(\text{VIX} > 40) \approx 1\% \text{ of days}
$$

**When VIX hits 40+:**

- Historically reverts within 3-6 months
- Short VIX from elevated levels = high probability
- **But catastrophic risk if wrong!**

### 4. The VIX-SPX


**Empirical correlation:**

$$
\text{Correlation}(\text{VIX}, \text{SPX}) \approx -0.70 \text{ to } -0.80
$$

**Negative correlation: Stocks down → VIX up**

**But asymmetric:**

**Stocks up 5%:**

- VIX typically down 10-15%
- Gradual decline

**Stocks down 5%:**

- VIX typically up 30-50%
- Explosive spike
- **Convex relationship**

**Mathematical representation:**

$$
\Delta \text{VIX} \approx -3 \times \Delta \text{SPX} \quad \text{(rough approximation)}
$$

**More accurately:**

$$
\text{VIX Change} = \alpha + \beta_1(\text{SPX Down}) + \beta_2(\text{SPX Down})^2
$$

Where $\beta_2 > 0$ (convexity)

**Example:**

- SPX -2%: VIX +8-10%
- SPX -5%: VIX +25-35%
- SPX -10%: VIX +100-150% (doubles/triples)

**This asymmetry creates hedging value:**

VIX longs are CRASH insurance, not volatility insurance

### 5. VIX Futures as


**Portfolio manager perspective:**

**Problem:**

- Own $10M equity portfolio
- Want downside protection
- Options expensive (high theta)
- **Alternative: Long VIX futures**

**Hedge ratio:**

$$
\text{VIX Contracts} = \frac{\text{Portfolio Value} \times \beta}{\text{VIX Futures Price} \times \$1,000 \times \text{Hedge Ratio}}
$$

**Example:**

- Portfolio: $10M, β = 1.0
- VIX futures: 18.00
- Hedge ratio: 3:1 (stocks down 3%, VIX up 9%)
- Target hedge: 50% of portfolio

$$
\text{Contracts} = \frac{\$10M \times 1.0 \times 0.5}{18 \times \$1,000 \times 3} = 92.6 \approx 93
$$

**Cost:**

In contango at 6%/month:

$$
\text{Monthly cost} = 93 \times 18 \times \$1,000 \times 0.06 = \$100,440
$$

$$
\text{Annual cost} = \$1.2M \text{ (12\% of portfolio!)}
$$

**This is EXPENSIVE insurance!**

**Why use VIX futures vs options:**

| Feature | VIX Futures Long | SPX Puts | SPY Puts |
|---------|------------------|----------|-----------|
| Cost | Roll decay 5-10%/mo | Premium 2-4%/mo | Premium 2-4%/mo |
| Leverage | 2-3:1 | None (paid upfront) | None |
| Convexity | High (VIX spikes) | Moderate | Moderate |
| Liquidity | Very high | Very high | Very high |
| Complexity | Medium | Low | Low |

**VIX futures advantage: Leverage + convexity**

**Disadvantage: Continuous roll cost**

### 6. Short VIX as


**The other side: Selling fear**

**Economic rationale:**

$$
\mathbb{E}[\text{VIX futures return}] < 0 \text{ for longs}
$$

$$
\Rightarrow \mathbb{E}[\text{VIX futures return}] > 0 \text{ for shorts}
$$

**Volatility risk premium:**

- Investors overpay for hedges
- VIX futures persistently expensive
- **Shorting = collecting premium**

**Historical evidence:**

- VIX in contango ~80% of the time
- Short VIX earns 5-10% per month in contango
- **Positive expectancy... until it's not**

**The catch:**

$$
P(\text{Loss} > 50\%) \approx 10\text{-}15\% \text{ of years}
$$

**Analogy: Picking up pennies in front of steamroller**

**Example:**

- Jan-Nov: Earn $100k shorting VIX (smooth)
- December: Lose $500k (market crash)
- **Net: -$400k**

**This is XIV blowup (2018) in a nutshell**

---

## Key Terminology


**VIX Index (Spot VIX):**

$$
\text{VIX} = 100 \times \sqrt{\text{30-day Implied Variance of SPX}}
$$

- CBOE Volatility Index
- "Fear gauge" for markets
- Typically 12-20 (calm), 30-80 (crisis)
- **Cannot trade directly**

**VIX Futures:**

$$
F_{\text{VIX}} = \text{Tradeable contracts on expected future VIX}
$$

- Symbol: /VX
- $1,000 per VIX point
- Monthly expirations
- Cash-settled
- **Can trade**

**Contango:**

$$
F_{\text{far}} > F_{\text{near}} > \text{VIX spot}
$$

- Upward sloping term structure
- Near-term cheaper than far-term
- Normal market state (80% of time)
- Creates negative roll yield for longs

**Backwardation:**

$$
F_{\text{far}} < F_{\text{near}} < \text{VIX spot}
$$

- Downward sloping term structure
- Near-term more expensive
- Crisis/fear state (20% of time)
- Creates positive roll yield for longs

**Roll Yield:**

$$
\text{Roll Yield} = \frac{F_{\text{near}} - F_{\text{far}}}{F_{\text{far}}} \times \frac{12}{\text{months}}
$$

- Profit/loss from rolling positions
- Negative in contango (costs money)
- Positive in backwardation (earns money)
- **Critical for long-term positions**

**Roll Decay:**

- Loss from contango when rolling longs
- VIX futures converge down to spot
- Can cost 50-80% annually
- **Why buy-and-hold VIX fails**

**Term Structure:**

$$
\{\text{VIX}, F_1, F_2, ..., F_8\}
$$

- Curve of VIX futures prices across months
- Shape indicates market regime
- Contango vs backwardation
- Trading opportunity

**Mean Reversion:**

$$
\mathbb{E}[\text{VIX}_{t+\tau}] \to \mu \text{ as } \tau \to \infty
$$

- VIX returns to long-term average
- Spikes are temporary
- Half-life 3-6 months
- **Fundamental characteristic**

**Convergence:**

$$
F_t^T \to \text{VIX}_T \text{ as } t \to T
$$

- Futures price approaches VIX at expiration
- Guaranteed by cash settlement
- Source of roll decay/yield
- **Mechanical, not optional**

**Volatility of Volatility (VolVol):**

$$
\text{VolVol} = \text{Std Dev of VIX Changes}
$$

- VIX itself is volatile
- Can move 10-30% in a day
- Makes VIX futures very risky
- Higher than most assets

**VXX, UVXY (ETPs):**

- Exchange-traded products tracking VIX futures
- VXX: 1× short-term VIX futures
- UVXY: 1.5× short-term VIX futures
- **Suffer severe contango decay**
- Not suitable for long-term holding

**SVXY (Inverse VIX ETP):**

- Short VIX futures exposure
- Profits from contango decay
- Catastrophic risk in spikes
- **Blew up in 2018 Volmageddon**

---

## The Greeks (VIX


**While VIX futures don't have traditional option Greeks, we can define analogous sensitivities:**

### 1. Delta


**Definition:** How VIX futures price changes with VIX index movement.

$$
\Delta_{\text{VIX futures}} = \frac{\partial F}{\partial \text{VIX}}
$$

**Near expiration (< 7 days):**

$$
\Delta \approx 0.9\text{-}1.0 \quad \text{(high correlation)}
$$

**Far expiration (> 90 days):**

$$
\Delta \approx 0.3\text{-}0.5 \quad \text{(low correlation)}
$$

**Example:**

**Front month (30 DTE):**

- VIX spot: 15.00 → 18.00 (+20%)
- VX1: 16.50 → 19.00 (+15.2%)
- **Delta ≈ 0.76**

**Far month (150 DTE):**

- VIX spot: 15.00 → 18.00 (+20%)
- VX5: 20.00 → 21.00 (+5%)
- **Delta ≈ 0.25**

**Interpretation:**

- Front months track VIX closely
- Back months relatively stable
- **Calendar spreads exploit this differential**

### 2. Gamma


**Definition:** How delta changes as VIX moves.

$$
\Gamma = \frac{\partial^2 F}{\partial \text{VIX}^2}
$$

**Behavior:**

**VIX spike:**

- Delta increases (futures become more responsive)
- Positive gamma
- **Convexity in favor of longs**

**Example:**

- VIX: 15 → 20: VX1 delta 0.75
- VIX: 20 → 30: VX1 delta 0.85
- VIX: 30 → 50: VX1 delta 0.95
- **Delta rising = positive gamma**

**This convexity is valuable:**

Long VIX futures benefit disproportionately from extreme spikes

### 3. Theta (Time Decay


**Definition:** How futures price changes as time passes (assuming VIX unchanged).

$$
\Theta = \frac{\partial F}{\partial t}
$$

**In contango:**

$$
\Theta < 0 \quad \text{(negative for longs)}
$$

**Example:**

- VX1: 18.00 (30 DTE)
- VIX spot: 15.00
- Premium: 3.00 points

**After 15 days (15 DTE):**

- VIX still: 15.00
- VX1 now: 16.50 (converging)
- **Loss: 1.50 points from theta**

$$
\Theta = -\frac{1.50}{15} = -0.10 \text{ points/day}
$$

**In backwardation:**

$$
\Theta > 0 \quad \text{(positive for longs!)}
$$

**Example:**

- VX1: 35.00 (30 DTE)
- VIX spot: 45.00
- Discount: -10.00 points

**After 15 days:**

- VIX still: 45.00
- VX1 now: 40.00 (converging up)
- **Gain: 5.00 points from theta**

$$
\Theta = +\frac{5.00}{15} = +0.33 \text{ points/day}
$$

**Theta is THE critical factor for VIX futures:**

- Contango theta bleeds longs 5-10%/month
- Backwardation theta pays longs
- **Must understand regime**

### 4. Vega (Volatility


**VIX futures are volatility instruments, so "vega" here means sensitivity to volatility OF volatility (vol-of-vol).**

**High vol-of-vol periods:**

- VIX itself very volatile
- Large daily swings (±10-20%)
- Futures prices whipsaw
- **High risk/reward**

**Low vol-of-vol periods:**

- VIX stable (±2-5% daily)
- Futures grind with contango
- Predictable theta decay
- **Favorable for short VIX**

**Typical vol-of-vol:**

$$
\text{Daily VIX std dev} \approx 10\text{-}15\% \text{ of VIX level}
$$

**Example:**

- VIX at 20
- Daily std dev: ±2-3 points
- 1σ range: 17-23 daily
- **Can move 10-15% in a day**

### 5. Rho (Interest


**Definition:** How VIX futures change with interest rates.

$$
\rho = \frac{\partial F}{\partial r}
$$

**Theoretical relationship:**

$$
F = \mathbb{E}[\text{VIX}_T] e^{rT}
$$

**Higher rates → slight premium in far months**

**In practice:**

$$
\rho \approx 0 \quad \text{(minimal impact)}
$$

**Interest rates barely matter for VIX futures**

Focus on VIX level and term structure instead

---

## Contract Selection


**Just as options traders select strikes/expirations, VIX traders select months:**

### 1. Front Month (VX1)


**Characteristics:**

- Highest liquidity (50k+ contracts/day)
- Tightest bid-ask ($0.05 typical)
- Delta ≈ 0.7-0.9 to spot VIX
- Highest volatility
- Rapid convergence to spot

**When to trade:**

**Long VX1:**

- Expecting immediate VIX spike
- Crash hedging
- Event-driven (FOMC, earnings season)
- **Need fast response**

**Short VX1:**

- VIX elevated (>30)
- Expecting mean reversion soon
- Contango very steep (>10%/month)
- **Short-term trade only**

**Example:**

- VIX spike from 15 → 30
- VX1: 16.50 → 32.00 (+94%)
- Profit on 10 contracts: $155,000
- **But can reverse just as fast**

**Pros:**

- Most responsive to VIX moves
- Highest liquidity
- Best for tactical trades
- **Maximum leverage to VIX**

**Cons:**

- Extreme volatility (±20% days)
- Fastest roll decay in contango
- Whipsaw risk
- **Heart attack inducing**

### 2. Characteristics:


**Characteristics:**

- Good liquidity (20k+ contracts/day)
- Delta ≈ 0.5-0.7
- Less volatile than VX1
- Still meaningful convergence

**When to trade:**

**Long VX2:**

- Medium-term bearish on stocks
- Want VIX exposure without VX1 whipsaw
- Better theta profile than VX1
- **1-2 month horizon**

**Short VX2:**

- Contango trading
- Less risky than VX1 short
- Still profitable in contango
- **Moderate income strategy**

**Pros:**

- Less volatile than VX1
- Still good liquidity
- Better risk/reward balance
- **Sweet spot for many traders**

**Cons:**

- Lower delta (less responsive)
- Still has roll decay
- Can still gap violently
- **Not "safe," just less crazy**

### 3. Back Months


**Characteristics:**

- Lower liquidity (<5k contracts/day)
- Delta ≈ 0.3-0.5
- Much less volatile
- Slow convergence

**When to trade:**

**Calendar spreads:**

- Long VX1, short VX4
- Harvest convergence differential
- Term structure trades
- **Structural strategies**

**Long-term hedges:**

- Deep OTM portfolio insurance
- Very cheap in contango
- Low theta bleed (but still exists)
- **Set and forget hedges**

**Pros:**

- Stable prices
- Lower margin
- Good for spreads
- **Less stressful**

**Cons:**

- Low liquidity (wide spreads)
- Minimal VIX sensitivity
- Still decays in contango
- **Boring**

### 4. VIX Calendar


**Most sophisticated approach:**

**Short front, long back:**

- Sell VX1 @ 17.00
- Buy VX3 @ 19.50
- Net credit: -$2.50
- **Profit from convergence differential**

**Rationale:**

- VX1 decays faster than VX3
- Collect contango premium on both
- Market-neutral to VIX direction
- **Pure term structure play**

**Example:**

**Entry:**

- VX1: 17.00 (30 DTE)
- VX3: 19.50 (90 DTE)
- Spread: -2.50

**30 days later:**

- VX1 expired → VIX at 15.50
- VX3 now 60 DTE: 18.00
- **Spread: -2.50 (VX3 = 18, VX1 settled at 15.50)**

**Wait, that doesn't work...**

**Actually need to roll VX1:**

- Close VX1 at expiry: 15.50
- VX3 still: 18.00
- Profit on VX1: 17.00 - 15.50 = **+1.50**
- VX3 declined: 19.50 - 18.00 = **+1.50**
- **Total: +3.00 points = $3,000 per spread**

**This is advanced VIX trading—harvesting term structure**

### 5. Comparison Table


| Contract | Liquidity | Delta | Daily Vol | Contango Decay | Best For |
|----------|-----------|-------|-----------|----------------|----------|
| VX1 | Excellent | 0.75 | ±15% | -10%/mo | Directional, hedges |
| VX2 | Good | 0.60 | ±10% | -7%/mo | Balanced trades |
| VX3-4 | Moderate | 0.45 | ±7% | -5%/mo | Spreads, longer hedges |
| VX5-8 | Low | 0.35 | ±5% | -3%/mo | Calendar spreads |

**Beginner recommendation: Start with VX1 or VX2 for directional, avoid unless sophisticated for spreads**

---

## Time Selection


**VIX trading is ALL about timing:**

### 1. Optimal Entry


**Best times to buy VIX futures:**

**1. VIX at extreme lows (<13):**

$$
P(\text{VIX rises} | \text{VIX} < 13) \approx 80\text{-}90\%
$$

**Historical percentiles:**

- VIX < 12: Bottom 5% (extreme complacency)
- VIX 12-15: Bottom 25% (cheap)
- VIX 15-20: Median (50%)
- VIX 20-30: Top 25% (elevated)
- VIX > 30: Top 10% (fear/panic)

**When VIX < 13:**

- Equity markets complacent
- Option premiums compressed
- Volatility likely to revert up
- **Rare opportunity to buy cheap insurance**

**2. Extended bull market (>12 months up):**

- SPX up 20-30% from lows
- No pullback in 200+ days
- Investor complacency high
- **Crash risk building**

**Historical pattern:**

Every 3-5 year bull market ends with VIX spike:

- 2007: VIX 10 → 80 (2008 crash)
- 2017: VIX 9 → 40 (2018 correction)
- 2019: VIX 12 → 85 (2020 COVID)
- **Pattern repeats**

**3. Before known events (tactical):**

- FOMC meetings
- Earnings season
- Elections
- Geopolitical tensions
- **Event premium building**

**Example:**

2 weeks before FOMC:

- VIX: 14.00
- VX1: 15.50
- After FOMC surprise: VIX → 22.00
- **Long profits**

**4. Technical signals:**

**VIX breaching lower Bollinger Band:**

$$
\text{VIX} < \text{MA}(20) - 2\sigma
$$

- Oversold condition
- Mean reversion likely
- **Entry signal**

**Equity market technical breakdown:**

- SPX breaks 200-day MA
- Momentum divergence
- Volume spikes on down days
- **VIX spike probable**

### 2. Optimal Entry


**Best times to sell VIX futures:**

**1. VIX spike to extreme levels (>30):**

$$
P(\text{VIX declines} | \text{VIX} > 30) \approx 85\text{-}95\%
$$

**Historical data:**

- VIX > 30: Reverts to <25 within 30 days (80% of time)
- VIX > 40: Reverts to <30 within 60 days (90% of time)
- VIX > 50: Peak panic, almost always decays
- **Mean reversion very reliable at extremes**

**Example:**

COVID crash March 2020:

- VIX peak: 85.47 (March 16)
- 30 days later: 33.00 (61% decline)
- 60 days later: 28.00 (67% decline)
- **Short from 60-70 level = massive profit**

**2. After crash when VIX still elevated but declining:**

**Pattern:**

- Crash happens: VIX spikes to 40-60
- Initial panic subsides: VIX falls to 25-35
- Market stabilizes but VIX still "high"
- **Short VIX at 25-30 = good risk/reward**

**Why:**

- Worst is over
- Mean reversion underway
- Contango rebuilding
- **Favorable setup**

**3. Contango re-establishment:**

**After backwardation flips to contango:**

- VIX term structure inverts during crisis
- As fear subsides, contango returns
- VX1 < VX2 < VX3
- **Theta turns positive for shorts**

**Example:**

- Day 1 (crisis): VX1 45, VX3 38 (backwardation)
- Day 30 (calming): VX1 28, VX3 30 (contango returns)
- **Short at Day 30 = favorable structure**

**4. Overbought VIX (technical):**

**VIX above upper Bollinger Band:**

$$
\text{VIX} > \text{MA}(20) + 2\sigma
$$

- Extreme fear priced in
- Likely reversion
- **Short signal**

**VIX/VX1 ratio > 0.95:**

- Futures very close to spot
- Minimal contango cushion
- Backwardation may flip to contango
- **Short becomes favorable**

### 3. When NOT to Trade


**Avoid these situations:**

**1. VIX in "neutral zone" (15-20):**

- Not cheap enough to buy
- Not expensive enough to sell
- No clear edge
- **Skip**

**2. During crisis with no sign of bottom:**

**Example: 2008 financial crisis**

- Sept 2008: VIX 30 (think peak? NO)
- Oct 2008: VIX 60 (now peak? NO!)
- Nov 2008: VIX 80 (final peak)
- **Shorting at 30 or 60 = disaster**

**Wait for:**

- VIX declining from peak
- Market stabilization
- Technical signals
- **Confirmation first**

**3. Low liquidity periods:**

- Between Christmas and New Year
- Asian holidays
- Late Friday afternoons
- **Wide spreads, poor execution**

**4. When you can't monitor:**

VIX can move 30% in an hour:

- Need real-time monitoring
- Can't set and forget
- **Active management required**

### 4. Exit Strategy


**For LONG VIX positions:**

**Exit #1: Target hit (VIX spike)**

$$
\text{If VIX} \geq \text{Entry VIX} \times 1.5 \Rightarrow \text{Close}
$$

**Example:**

- Entered: VIX 14, VX1 16.00
- Target: VIX 21 (50% spike)
- VX1 hits: 24.00
- **Close for profit**

**Exit #2: Time stop (theta bleeding)**

$$
\text{If held } > 30 \text{ days in contango} \Rightarrow \text{Close}
$$

**Contango decay accumulates:**

- Month 1: -8%
- Month 2: -7%
- Month 3: -6%
- **Cumulative: -21%**

**Exit #3: Roll to avoid expiration:**

- 7 days before expiry → Close VX1
- Open VX2 or VX3
- **Maintain exposure, avoid settlement risk**

**For SHORT VIX positions:**

**Exit #1: VIX declining to normal (won)**

$$
\text{If VIX} < 18 \Rightarrow \text{Close short}
$$

**Entered short at VIX 35:**

- VIX declines to 17
- Mission accomplished
- **Take profit**

**Exit #2: HARD STOP if VIX spiking (critical!)**

$$
\text{If VIX} > \text{Entry VIX} \times 1.2 \Rightarrow \text{CLOSE IMMEDIATELY}
$$

**Example:**

- Short VX1 @ 18.00 (VIX 16)
- VIX spikes to 20
- VX1 now: 22.00
- **Loss: $4,000 per contract**
- **MUST exit before it goes to 40!**

**Why strict stop:**

Short VIX can lose 200-300% in days:

- Short @ 20
- Crash: VIX → 60
- VX1 → 65
- **Loss: $45,000 per contract**
- **Account blown**

**Exit #3: Reduce size as profit grows:**

**Ratchet down:**

- Start: Short 20 contracts
- Profit 30%: Cover 10 contracts
- Profit 50%: Cover 5 more
- Let 5 run with stop
- **Lock profits progressively**

---

## Maximum Profit and


### 1. Long VIX Futures


**Setup:**

- Buy 10 VX1 @ 16.50
- VIX spot: 15.00
- Margin: $70,000 (10 × $7,000)
- Target: VIX spike to 25

**Maximum Profit (Spike Scenario):**

**Crisis develops:**

- VIX spikes: 15 → 35 (133% increase)
- VX1: 16.50 → 37.00 (124% increase)
- Exit: 37.00

$$
\text{Profit} = (37.00 - 16.50) \times \$1,000 \times 10 = \$205,000
$$

$$
\text{Return on margin} = \frac{\$205,000}{\$70,000} = 293\%
$$

**This is the power of long VIX in crashes!**

**Maximum Loss (Contango Decay):**

**No spike, contango grinds:**

**Month 1:**

- VIX: 15 → 14 (calm continues)
- VX1 expires at 14.00
- Roll to new VX1 @ 16.00
- **Loss: 16.50 - 14.00 = 2.50 points**

**Month 2:**

- VIX still: 14
- VX1 expires at 14.00
- **Loss: 16.00 - 14.00 = 2.00 points**

**After 6 months of rolling:**

$$
\text{Cumulative loss} \approx 50\text{-}60\% \text{ of position}
$$

$$
\text{Total loss} = \$70,000 \times 0.55 = -\$38,500
$$

**This is why long VIX can't be buy-and-hold!**

### 2. Short VIX Futures


**Setup:**

- Short 10 VX1 @ 22.00
- VIX spot: 28.00 (elevated after spike)
- Margin: $100,000 (higher due to elevated VIX)
- Target: VIX mean reversion to 16

**Maximum Profit (Mean Reversion):**

**VIX decays as expected:**

- VIX: 28 → 16 (43% decline)
- VX1: 22.00 → 15.50 (30% decline)
- Cover: 15.50

$$
\text{Profit} = (22.00 - 15.50) \times \$1,000 \times 10 = \$65,000
$$

$$
\text{Return on margin} = \frac{\$65,000}{\$100,000} = 65\%
$$

**Great return in 60-90 days!**

**Maximum Loss (Second Crash):**

**VIX re-spikes (disaster):**

**Week 1:**

- VIX: 28 → 35
- VX1: 22 → 38
- Unrealized loss: -$160,000
- **Margin call!**

**Can't meet margin call, forced liquidation:**

- Liquidated @ 38.00
- **Realized loss: $160,000 (exceeds margin!)**

**If held through full crash:**

- VIX → 60
- VX1 → 65
- **Loss: (65 - 22) × $1,000 × 10 = -$430,000**
- **4.3× margin wiped out**

**This is the risk of short VIX!**

### 3. Real Examples


**Example 1: XIV collapse (Feb 2018)**

**Product:** XIV (Short VIX ETP)

**Setup:**

- Traders short VIX futures via XIV
- Years of profits (2012-2017)
- VIX persistently low (10-15)
- **Complacency extreme**

**The Volmageddon:**

- Feb 5, 2018: VIX 17 → 37 intraday (118% spike)
- XIV: $99 → $4 (96% loss in ONE DAY)
- **Product terminated, investors wiped**

**What happened:**

- S&P 500 down only 4%
- But VIX futures gapped violently
- Short VIX positions margin-called
- Forced covering created feedback loop
- **Catastrophic collapse**

**Lesson: Short VIX can lose everything in hours**

**Example 2: COVID crash long VIX (March 2020)**

**Setup:**

- Feb 2020: VIX 13-14 (extreme low)
- Buy VX1 @ 15.50
- Position: 50 contracts

**The crash:**

- Feb 19: Entry @ 15.50
- March 16: VIX 85.47 (peak)
- VX1: ~87.00
- **Exit at 65.00 (conservative)**

$$
\text{Profit} = (65.00 - 15.50) \times \$1,000 \times 50 = \$2,475,000
$$

**Starting capital: $400,000 margin**

**Ending: $2,875,000**

**Return: 619% in 26 days!**

**Lesson: Long VIX in crashes = lottery ticket**

---

## When to Use VIX


### 1. Ideal Situations


**Use long VIX futures when:**

**1. Portfolio insurance (tail risk hedge):**

- Own large equity portfolio ($1M+)
- Want downside protection
- Options too expensive (theta bleed)
- **VIX futures as alternative**

**Example allocation:**

- Portfolio: $5M
- Allocate 2% to VIX futures: $100,000
- Buy 6 VX2 @ 17.00
- **Cheap insurance if held short-term**

**2. VIX extremely low (<13):**

$$
\text{VIX Percentile} < 10\%
$$

- Market complacent
- Volatility compressed
- Historically reverts higher
- **Cheap insurance**

**3. Before known volatility events:**

- FOMC meeting
- Elections
- Geopolitical risk building
- **Event premium play**

**4. Technical breakdown in equities:**

- SPX breaks support
- VIX breaking out
- Momentum turning negative
- **Tactical long VIX**

**5. Systematic volatility targeting:**

- Rules-based VIX allocation
- Rebalance monthly
- 5-10% portfolio to VIX longs
- **Defensive allocation strategy**

### 2. Ideal Situations


**Use short VIX futures when:**

**1. VIX spike to extremes (>30):**

$$
\text{VIX Percentile} > 90\%
$$

- Market in panic
- Fear priced to extremes
- Mean reversion highly probable
- **High probability short**

**Example:**

- VIX spikes to 45
- Historical reversion time: 60 days
- Short VX2 @ 38.00
- Target: 22.00
- **High win rate setup**

**2. Post-crisis stabilization:**

- Crash happened
- VIX declining but still elevated (25-30)
- Contango re-establishing
- **Favorable structure**

**3. Contango very steep (>8%/month):**

$$
\frac{F_2 - F_1}{F_1} > 0.08
$$

- Rich term structure premium
- Roll yield highly negative for longs
- **Collect premium via shorts**

**4. Systematic short volatility:**

- Rules-based approach
- Only when VIX > 25
- Size conservatively
- Hard stops
- **Income generation strategy**

**5. Calendar spreads (advanced):**

- Short front month
- Long back month
- Harvest convergence differential
- **Market-neutral term structure play**

### 3. Specific Use


**Use Case 1: Black Swan hedging**

**Strategy:**

- Allocate 1-3% of portfolio continuously
- Long VX3 or VX4 (cheaper than VX1)
- Accept contango bleed as "insurance premium"
- **Pays off in crash**

**Math:**

- $1M portfolio
- $20k in VX4 (5 contracts @ 20.00)
- Annual decay: ~40% = $8,000
- **Cost: 0.8% of portfolio annually**

**If crash:**

- VIX → 60
- VX4 → 50
- Profit: $150,000
- Portfolio down 30% = -$300,000
- Net: -$150,000 vs -$300,000 unhedged
- **50% protection**

**Use Case 2: Mean reversion income**

**Strategy:**

- Short VIX when >30
- Target 25% profit
- Hard stop at +30% loss
- 50% position size (never full)
- **Income in calm after storms**

**Results (hypothetical):**

- 10 trades per year
- 8 winners avg +25%
- 2 losers avg -30%
- **Net: +1.4R expected**

**Use Case 3: Event trading**

**FOMC play:**

- Week before FOMC: Long VX1
- VIX rises 2-3 points (event premium)
- Exit day before FOMC
- **Tactical 1-2 week trade**

**Stats:**

- Win rate: 60%
- Avg profit: +15%
- Avg loss: -10%
- **Positive expectancy**

---

## When NOT to Use VIX


### 1. Situations to


**1. As buy-and-hold investment:**

$$
\text{Long VIX持続 = Guaranteed loss in contango}
$$

**Math:**

- Contango decay: 5-10%/month
- Annual compounded loss: 50-80%
- **Wealth destruction**

**Example:**

- Jan 1: $100k in long VIX
- Dec 31: $30k remaining (if no spike)
- **Loss: $70k (70%!)**

**2. Shorting VIX at low levels (<18):**

**Why it fails:**

- Little room to fall further
- Unlimited upside risk
- Small premium vs huge risk
- **Terrible risk/reward**

**Example:**

- Short VX1 @ 15.00 (VIX at 13)
- Collect $2k profit over 2 months (contango)
- Then crash: VIX → 40
- VX1 → 42
- **Loss: $27,000 per contract**
- **Risk $27k to make $2k = insane**

**3. Without hard stops:**

**Short VIX without stop = Russian roulette:**

- Can make money 90% of the time
- 10% of time = catastrophic loss
- **Expected value negative**

**Historical blowups:**

- LTCM (1998)
- Bear Stearns (2007)
- XIV (2018)
- Archegos (2021)
- **All similar: short volatility, no stops**

**4. Overleveraging:**

$$
\text{VIX position} > 20\% \text{ of account = DANGER}
$$

**Why:**

- VIX can move 50-100% in days
- Margin calls happen fast
- Forced liquidation at worst prices
- **Account destruction**

**5. During confirmed crisis without expertise:**

**Amateur mistake:**

- See VIX at 40
- Think: "Must come down, I'll short!"
- VIX goes to 60
- **Wiped out**

**Professional approach:**

- Wait for clear peak
- Wait for confirmed decline
- Enter on retrace
- **Patience crucial**

**6. When you can't monitor 24/5:**

**VIX trades nearly 24 hours:**

- Sunday 6PM - Friday 5PM (ET)
- Can gap overnight
- Asian session volatility
- **Need constant monitoring**

**If you can't watch:**

- Don't trade VIX
- Use options instead (defined risk)
- Or avoid entirely
- **Active management required**

**7. Without understanding term structure:**

**Fatal mistake:**

- Think VIX futures = VIX index
- Ignore contango/backwardation
- Don't track roll costs
- **Losses inevitable**

**Must understand:**

- Term structure shape
- Roll yield calculation
- Convergence dynamics
- **Education required first**

### 2. Warning Signs to


**For LONG VIX:**

**1. Contango rebuilding after spike:**

- VX1 < VX2 < VX3 again
- Theta turning negative
- **Exit if holding for hedge**

**2. VIX declining for 30+ days:**

- Mean reversion completed
- No new catalyst
- Contango bleeding
- **Close position**

**3. Position down >30% from contango:**

- Been holding too long
- Decay accumulated
- Cut losses
- **Restart when better setup**

**For SHORT VIX:**

**1. VIX rising 20% in one day:**

- Something is breaking
- Panic beginning
- **Cover immediately**

**2. Backwardation appearing:**

- VX1 > VX2 (inversion)
- Structure turned against shorts
- Theta now negative
- **Exit**

**3. Geopolitical event escalation:**

- War breaking out
- Financial crisis spreading
- Systemic risk
- **Cover all shorts**

---

## Position Sizing and


### 1. The Golden Rule


**Maximum position sizes:**

**Conservative:**

$$
\text{VIX futures} \leq 5\% \text{ of portfolio}
$$

**Moderate:**

$$
\text{VIX futures} \leq 10\% \text{ of portfolio}
$$

**Aggressive (experienced only):**

$$
\text{VIX futures} \leq 20\% \text{ of portfolio}
$$

**NEVER >20% regardless of conviction!**

### 2. Position Sizing


**Long VIX (hedging):**

$$
\text{Contracts} = \frac{\text{Portfolio Value} \times \text{Hedge \%}}{\text{VIX Futures Price} \times \$1,000 \times \beta}
$$

**Example:**

- Portfolio: $2M
- Want 25% downside protection
- VX2: 18.00
- Hedge ratio: 3:1 (stocks -3%, VIX +9%)

$$
\text{Contracts} = \frac{\$2M \times 0.25}{18 \times \$1,000 \times 3} = 9.26 \approx 9
$$

**Long VIX (speculation):**

$$
\text{Contracts} = \frac{\text{Account Risk (2\%)}}{\text{Expected Max Adverse Move}}
$$

**Example:**

- Account: $200k
- Risk: 2% = $4,000
- Entry: VX1 @ 16.00
- Stop: 14.00 (VIX decay to 12)
- Risk per contract: 2.00 × $1,000 = $2,000

$$
\text{Contracts} = \frac{\$4,000}{\$2,000} = 2
$$

**Short VIX (income):**

$$
\text{Contracts} = \frac{\text{Account Risk (3-5\%)}}{\text{Expected Max Adverse Move}}
$$

**Example:**

- Account: $500k
- Risk: 5% = $25,000
- Short VX1 @ 28.00
- Stop: 35.00 (if VIX re-spikes)
- Risk per contract: 7.00 × $1,000 = $7,000

$$
\text{Contracts} = \frac{\$25,000}{\$7,000} = 3.57 \approx 3
$$

**NEVER short more than 5-10 contracts without institutional capital!**

### 3. Stop Loss


**For LONG VIX:**

**Time stop (primary):**

$$
\text{If held } > 30 \text{ days} \Rightarrow \text{Close}
$$

**Reason: Contango decay accumulates**

**Price stop (secondary):**

$$
\text{If down } > 25\% \Rightarrow \text{Close}
$$

**Example:**

- Entry: VX1 @ 17.00
- Down 25%: 12.75
- **Exit if hit**

**For SHORT VIX (CRITICAL):**

**Strict price stop:**

$$
\text{If VIX} > \text{Entry VIX} \times 1.3 \Rightarrow \text{CLOSE IMMEDIATELY}
$$

**Example:**

- Short VX1 @ 24.00 (VIX 22)
- Stop trigger: VIX 28.6
- VX1 likely: ~30.00
- **Exit loss: $6,000 per contract**

**Without this stop:**

- VIX continues to 50
- VX1 → 52
- **Loss: $28,000 per contract**
- **Survival at stake!**

**Maximum loss limit:**

$$
\text{Per trade max loss} = 30\% \text{ of position value}
$$

**If hit:**

- Exit all
- Review what went wrong
- Don't add to loser
- **Preserve capital**

### 4. Margin Management


**VIX futures margin is dynamic:**

**Normal VIX (15-20):**

- Initial margin: ~$5,000-7,000 per contract
- Maintenance: ~$4,000-5,000

**Elevated VIX (25-35):**

- Initial margin: ~$10,000-15,000
- Maintenance: ~$7,500-12,000

**Extreme VIX (40+):**

- Initial margin: ~$20,000-30,000
- Maintenance: ~$15,000-25,000

**Margin calls happen FAST:**

**Example:**

- Short 10 VX1 @ 20.00
- Margin posted: $70,000
- VIX spikes to 30
- VX1 → 32.00
- Mark-to-market loss: $120,000
- New margin requirement: $150,000
- **Margin call: $200,000 needed!**

**If can't meet:**

- Forced liquidation
- Worst possible prices
- **Account blown**

**Protection:**

- Keep 2-3× margin in cash reserves
- Never use >50% of capital for margin
- Size conservatively
- **Always have buffer**

### 5. Diversification


**Don't concentrate in VIX:**

**Portfolio allocation:**

- 70-80%: Core equities/bonds
- 10-15%: Alternative strategies
- 5-10%: Volatility (VIX futures)
- 5-10%: Cash/other
- **VIX as satellite, not core**

**Within VIX allocation:**

- Don't use only VX1 (too volatile)
- Don't all long or all short
- Mix VX1, VX2, VX3
- **Diversify expiration months**

**Correlation awareness:**

$$
\text{Correlation}(\text{VIX}, \text{SPX}) \approx -0.75
$$

**If long VIX:**

- You're short equities indirectly
- Don't double up with SPX shorts
- **Already have correlation**

### 6. Account: $300,000


**Account: $300,000**

**Allocation:**

- Core: $240,000 (80% in SPY, bonds)
- VIX strategies: $30,000 (10%)
- Cash reserve: $30,000 (10%)

**VIX positions:**

**Position 1: Long VX3 (hedge)**

- 5 contracts @ 19.00
- Margin: $25,000
- Stop: None (strategic hedge)
- Max loss: Accept decay
- **Insurance position**

**Position 2: Short VX1 (income)**

- 2 contracts @ 26.00 (VIX elevated at 28)
- Margin: $20,000
- Stop: 32.00 (VIX 34)
- Max loss: $12,000
- **Tactical mean reversion**

**Total VIX exposure:**

- Margin used: $45,000
- Cash reserve: $30,000
- Total available: $75,000
- **Coverage ratio: 1.67×**

**Risk analysis:**

**If VIX spikes to 50:**

- Long VX3: 19 → 42, profit $115,000
- Short VX1: 26 → stopped at 32, loss -$12,000
- **Net: +$103,000**
- **Plus core portfolio protected**

**If VIX decays to 15:**

- Long VX3: 19 → 16, loss -$15,000 (acceptable hedge cost)
- Short VX1: 26 → 15.50, profit +$21,000
- **Net: +$6,000**
- **Income from contango**

**This is balanced VIX trading:**

- Hedged extreme downside
- Income from mean reversion
- Diversified expirations
- Proper sizing
- **Professional approach**

---

## Common Mistakes


### 1. The error: See


**The error:**

- See VIX low at 13
- Think: "I'll buy and hold for crash"
- Buy 20 VX1 @ 15.00
- Hold for 6 months
- **No crash comes**

**What happens:**

**Monthly roll costs:**

- Month 1: Roll to new VX1, cost 8%
- Month 2: Roll again, cost 7%
- Month 3: Roll again, cost 8%
- Month 4: Roll again, cost 7%
- Month 5: Roll again, cost 8%
- Month 6: Roll again, cost 7%

**Cumulative:**

$$
(1 - 0.08) \times (1 - 0.07) \times ... \approx 0.56
$$

**Position value:**

- Start: $300,000
- End: $168,000
- **Loss: $132,000 (44%!)**

**All from contango decay, VIX still at 13!**

**Correct approach:**

- Long VIX only tactically (30-60 days max)
- OR accept decay as insurance cost
- OR use options instead (defined risk)
- **Never buy and hold VIX futures**

### 2. The error: VIX at


**The error:**

- VIX at 14 (normal)
- Think: "I'll short for contango income"
- Short 15 VX1 @ 15.50
- **Collecting $2-3k/month feels great**

**Months 1-8: Smooth sailing**

- Profit: $24,000
- Think: "This is easy money!"
- **Overconfident**

**Month 9: Disaster (COVID-like event)**

- VIX: 14 → 45 (221% spike)
- VX1: 15.50 → 48.00 (210% spike)
- Loss per contract: $32,500
- Total loss: 15 × $32,500 = **-$487,500**

**Margin:**

- Initial: $105,000
- Loss exceeds margin by $382,500
- **Bankruptcy**

**Correct approach:**

$$
\text{Only short VIX when} > 25
$$

$$
\text{Maximum size} = 5\text{-}10 \text{ contracts}
$$

$$
\text{ALWAYS use stops}
$$

### 3. The error: VIX at


**The error:**

- VIX at 22 (elevated)
- VX1: 20.00 (backwardation!)
- Think: "VX1 below VIX, cheap!"
- Buy VX1
- **Don't understand backwardation**

**What happens:**

**Backwardation = VIX expected to DECLINE:**

- VIX: 22 (today)
- Expected VIX in 30 days: 18
- VX1: 20 (midpoint, correct pricing)
- **Not cheap, appropriately priced**

**30 days later:**

- VIX declines to 17 (as expected)
- VX1 converges to 17
- **Loss: 20 - 17 = 3 points ($3,000)**

**Should have gone SHORT, not long!**

**Correct approach:**

**Check term structure BEFORE every trade:**

```
Contango (VX1 > VIX):
- Long = decay risk
- Short = collect premium

Backwardation (VX1 < VIX):
- Long = profit from convergence up
- Short = risk of spike
```

### 4. The error: Short


**The error:**

- Short VX1 @ 28.00 (VIX at 30)
- Set mental stop at 35.00
- VIX spikes to 33
- Think: "Just a little more, I'll wait"
- VIX → 37
- Think: "Already down, might as well hold for reversion"
- VIX → 45
- **Finally panic sell at 48**

**Result:**

$$
\text{Loss} = (48 - 28) \times \$1,000 \times 10 = -\$200,000
$$

**If had honored stop at 35:**

$$
\text{Loss} = (35 - 28) \times \$1,000 \times 10 = -\$70,000
$$

**Saved $130,000 by using HARD stop!**

**Correct approach:**

**Place HARD stop immediately:**

- Use broker's stop-loss order
- Not mental stop
- Set at entry
- **No emotions, automatic exit**

### 5. The error:


**The error:**

- Account: $100k
- Short 30 VX1 @ 25.00
- Margin: $90k (90% of account!)
- Think: "VIX will decay fast"
- **Massively overleveraged**

**Small adverse move destroys:**

- VIX: 23 → 28 (22% increase)
- VX1: 25 → 30
- Loss: $150,000
- Margin call: $50,000
- **Can't meet it**

**Forced liquidation:**

- Closed at worst price
- Account: $100k → $0
- **Wiped out**

**Correct approach:**

$$
\text{Max VIX position} = 20\% \text{ of account}
$$

For $100k:

- Maximum: $20k margin
- ~3 contracts
- **Conservative sizing**

### 6. The error: Long


**The error:**

- Long VX1 expiring Wednesday
- Monday: VX1 = 18.50, VIX = 16.00
- Think: "Maybe VIX will spike before Wednesday"
- **Holds through expiration**

**Wednesday settlement:**

- VIX opens: 15.50 (lower than Monday)
- VX1 settles: 15.50
- **Loss: 18.50 - 15.50 = 3 points**

**If had closed Monday:**

- Could sell at 18.50
- Saved 3 points = $3,000 per contract
- **Better execution**

**Plus settlement risk:**

- VIX calculation at open
- Can gap from Tuesday close
- Unpredictable
- **Avoid**

**Correct approach:**

$$
\text{Close or roll } 3\text{-}5 \text{ days before expiration}
$$

### 7. The error: VIX at


**The error:**

- VIX at 15
- VX1 at 17
- Think: "VX1 overpriced 13%, I'll short!"
- **Don't understand futures are pricing expected future VIX**

**What happens:**

- VIX stays 15 for 30 days
- VX1 converges to 15
- Profit: 2 points (lucky!)
- **But didn't understand WHY**

**Next trade:**

- VIX at 25
- VX1 at 22
- Think: "VX1 underpriced 12%, I'll buy!"
- **Backwardation means VIX expected to fall**

**30 days later:**

- VIX declines to 18
- VX1 settles: 18
- **Loss: 22 - 18 = 4 points**

**Correct approach:**

**Understand:**

$$
\text{VX1} \approx \mathbb{E}[\text{VIX}_{+30\text{days}}] + \text{Risk Premium}
$$

**In contango:**

- VX1 > VIX (normal)
- Futures price mean reversion UP

**In backwardation:**

- VX1 < VIX (fear)
- Futures price mean reversion DOWN

### 8. The error: Trade


**The error:**

**Trade 1:**

- Short VX1 @ 26, stopped at 32
- Loss: $6,000 per contract
- Emotional: Angry

**Trade 2 (Revenge):**

- Immediately re-short VX1 @ 32 (bigger size!)
- "I'll make it back!"
- No stop this time (already down)
- **Pure emotion**

**What happens:**

- VIX continues spiking to 50
- VX1 → 52
- **Loss: $20,000 more per contract**
- **Total disaster**

**Correct approach:**

**After loss:**

1. Accept it (part of trading)
2. Review what went wrong
3. Take 1-week break
4. Only trade QUALITY setup next
5. Standard size (don't revenge size up)
6. **Emotion-free decisions**

### 9. The error: VIX


**The error:**

- VIX spikes to 35
- Think: "VIX high = stocks bottoming"
- Buy stocks heavily
- **VIX goes to 60, stocks continue falling**

**Flaw in logic:**

$$
\text{High VIX} \neq \text{Bottom}
$$

**High VIX just means high fear, not peak fear**

**Examples:**

- Oct 2008: VIX 45 (thought bottom)
- Nov 2008: VIX 80 (actual bottom)
- March 2020: VIX 40 (thought bottom)
- March 16, 2020: VIX 85 (actual bottom)

**Correct approach:**

**Wait for VIX declining FROM peak:**

- VIX peaks at 85
- Declines to 65
- Confirms reversal
- **THEN buy stocks**

**VIX trend > VIX level**

### 10. The error: Trade


**The error:**

- Trade VIX futures frequently
- Don't calculate transaction costs
- Don't track roll costs
- **Unaware of bleed**

**Hidden costs:**

**Bid-ask spread:**

- VX1 spread: $0.05-0.10
- Per contract: $50-100
- 10 contracts, 2 trades/month: $2,400/year

**Roll costs (long VIX in contango):**

- Monthly roll: 7% × $17,000 = $1,190
- Annual: $14,280

**Margin interest (if applicable):**

- $100k margin @ 5%
- Annual: $5,000

**Total annual costs:**

$$
\$2,400 + \$14,280 + \$5,000 = \$21,680
$$

**On $100k position = 21.68% annual drag!**

**Correct approach:**

**Track ALL costs:**

- Spreadsheet of each trade
- Calculate roll costs
- Bid-ask slippage
- **Know true P&L**

---



## Final Wisdom


> "VIX futures are NOT an asset class to own long-term—they're a trading instrument for specific setups and tactical hedging. The persistent contango bleeds longs 50-80% annually, making buy-and-hold catastrophic. Conversely, short VIX offers tempting income through contango harvesting but carries unlimited tail risk that has destroyed countless traders and funds. The successful VIX trader is patient (waiting for extremes), disciplined (using hard stops), and properly sized (never betting the farm). Long VIX works when VIX <13 for short-term hedges or during confirmed equity breakdowns. Short VIX works when VIX >30 and showing clear mean reversion. Outside these extremes, skip the trade entirely. VIX futures are the ultimate example of a double-edged sword—capable of generating 500% returns or -100% losses within days. Respect the weapon or it will destroy you."

**Most important principles:**

- VIX futures ≠ VIX index (they diverge significantly)
- Contango decay = structural headwind for longs
- Mean reversion = core characteristic
- Short VIX = picking up pennies in front of steamroller
- Long VIX = insurance with known premium
- Timing is everything (extremes only)
- Stops are survival (not optional)
- Size conservatively (max 20% of account)

**Why this works (when done right):**

- VIX mean-reverting (statistical edge)
- Contango premium harvestable (structural edge)
- Crash convexity (hedging value)
- Behavioral predictability (fear/greed cycles)
- **Edges exist but require discipline**

**But remember:**

- One bad trade can wipe out years of gains (short VIX)
- Contango decay never stops (long VIX)
- Regime changes happen (2008, 2020)
- Leverage amplifies both ways
- **Respect the risk or be destroyed**

**Trade VIX when you have edge, skip when you don't. The market rewards patience with extremes 2-4 times per year. That's your opportunity window—the other 90% of the time, stay flat. 📊💥**