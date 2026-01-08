# Dispersion Trading

**Dispersion trading** is a strategy where you profit from the difference between index volatility and the weighted average of individual stock volatilities by exploiting the correlation structure of the market.





---

## The Core Insight

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/dispersion_trading_correlation.png?raw=true" alt="dispersion_trading_correlation" width="700">
</p>
<p align="center"><em>Figure 1: Correlation dynamics showing relationship between individual stock correlations and index volatility levels</em></p>

**The fundamental idea:**

- An index (like S&P 500) has its own volatility

- Each stock in the index also has its own volatility

- **These are NOT the same thing!**

- Index volatility depends on how correlated the stocks are

- You can bet that this relationship is mispriced

**The key equation:**
$$
\sigma_{\text{index}}^2 = \sum w_i^2 \sigma_i^2 + \sum_{i \neq j} w_i w_j \rho_{ij} \sigma_i \sigma_j
$$

**In plain English:**

- Index volatility = individual volatilities + correlation effects

- When correlation is high → index vol is high (stocks move together)

- When correlation is low → index vol is low (stocks offset each other)

- You can trade this relationship!

**You're essentially betting: "The market has the wrong view on how much stocks will move together."**

---

## The Volatility-Correlation Relationship

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/dispersion_trading_pnl.png?raw=true" alt="dispersion_trading_pnl" width="700">
</p>
<p align="center"><em>Figure 2: P&L profile of long dispersion trade demonstrating profit from declining correlation</em></p>

**This is CRUCIAL to understand:**

### 1. A Simple Example

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/dispersion_trading_realized_implied.png?raw=true" alt="dispersion_trading_realized_implied" width="700">
</p>
<p align="center"><em>Figure 3: Realized vs. implied correlation comparison showing historical dispersion premium</em></p>

**Imagine an index with two stocks (equal weighted):**

**Stock A:** $\sigma_A = 30\%$ volatility

**Stock B:** $\sigma_B = 30\%$ volatility

**What's the index volatility?** It depends on correlation!

**Case 1: Perfect Correlation ($\rho = +1$)**

- Stocks always move together

- Index volatility: $\sigma_{\text{index}} = 30\%$

- Index vol = Average of individual vols

**Case 2: No Correlation ($\rho = 0$)**

- Stocks move independently

- Index volatility: $\sigma_{\text{index}} = \frac{30\%}{\sqrt{2}} \approx 21\%$

- Index vol < Individual vols (diversification!)

**Case 3: Negative Correlation ($\rho = -1$)**

- Stocks move in opposite directions

- Index volatility: $\sigma_{\text{index}} = 0\%$

- Perfectly hedged!

**The key insight:** Index vol is ALWAYS less than or equal to the average individual vol (unless correlation = 1)

$$
\sigma_{\text{index}} \leq \sqrt{\sum w_i^2 \sigma_i^2}
$$

**This gap is what dispersion traders exploit!**

---

## What Is Dispersion Trading?

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/dispersion_trading_vol_comparison.png?raw=true" alt="dispersion_trading_vol_comparison" width="700">
</p>
<p align="center"><em>Figure 4: Volatility comparison between index and individual stock components illustrating diversification benefit</em></p>

**Dispersion trading is betting on the CORRELATION structure:**

### 1. The Fundamental Trade

**Classic "Long Dispersion" (Most Common):**

1. Sell index options (short index volatility) 

2. Buy individual stock options (long individual stock volatilities)

3. Delta hedge everything

4. Profit when stocks "disperse" (move independently, low correlation)

**"Short Dispersion" (Opposite):**

1. Buy index options (long index volatility)

2. Sell individual stock options (short individual stock volatilities)

3. Delta hedge everything

4. Profit when stocks "correlate" (move together, high correlation)

**What you're betting on:**

- **Long dispersion:** "Stocks will move independently (low correlation)"

- **Short dispersion:** "Stocks will move together (high correlation)"

---

## The Basic Idea

**What you do (Long Dispersion):**

1. **Choose an index** (e.g., S&P 500, but often use a smaller basket like 10-20 stocks)

2. **Sell index options** (typically ATM straddles on the index)

3. **Buy options on individual stocks** (ATM straddles on each component)

4. **Delta hedge everything** (both index and all individual stocks)

5. **Position size** to be roughly volatility-neutral overall

6. **Profit when** stocks move around independently (low correlation)

**The goal:** Profit when realized correlation is lower than what was priced into the options (implied correlation).

**Key insight:** You're not betting on whether volatility is high or low—you're betting on how TOGETHER stocks move!

---

## The Portfolio

Your dispersion trading portfolio consists of:

$$
\Pi = \text{Short Index Options} + \text{Long Individual Options} + \text{Delta Hedges}
$$

More precisely:

$$
\Pi = -V_{\text{index}}(S_{\text{index}}, t) + \sum_{i=1}^{n} w_i V_i(S_i, t) - \Delta_{\text{index}} \cdot S_{\text{index}} + \sum_{i=1}^{n} \Delta_i \cdot S_i
$$

where:

- $V_{\text{index}}$ = index option value (you're short)

- $V_i$ = individual stock option values (you're long)

- $w_i$ = weights chosen to make position volatility-neutral

- Delta hedges on both index and all stocks

**Why this structure?**

- Short index options: negative exposure to index vol

- Long individual options: positive exposure to individual vols

- Net exposure: correlation/dispersion

- Delta hedges: remove directional risk

**Portfolio Greeks:**

$$
\Delta_{\text{net}} = -\Delta_{\text{index}} + \sum_{i=1}^{n} w_i \Delta_i \approx 0
$$

$$
\Gamma_{\text{net}} = -\Gamma_{\text{index}} + \sum_{i=1}^{n} w_i \Gamma_i
$$

$$
\mathcal{V}_{\text{net}} = -\mathcal{V}_{\text{index}} + \sum_{i=1}^{n} w_i \mathcal{V}_i
$$

**Goal:** Make $\mathcal{V}_{\text{net}} \approx 0$ (vega neutral), isolating correlation exposure.

**Weight selection:**

To achieve vega neutrality:
$$
w_i = \frac{\text{Market Cap}_i}{\sum_j \text{Market Cap}_j} \times \frac{\mathcal{V}_{\text{index}}}{\mathcal{V}_i}
$$

Approximately market-cap weighted, adjusted for vega matching.

---

## Economic

**Understanding what this strategy REALLY represents economically:**

### 1. The Core Economic Trade-Off

**Dispersion trading is fundamentally trading the value of diversification.**

**Economic meaning:**

$$
\text{Index Variance} = \underbrace{\text{Average Individual Variance}}_{\text{idiosyncratic risk}} + \underbrace{\text{Covariance Terms}}_{\text{systematic risk}}
$$

When you go **long dispersion**, you're betting:

- Individual stock movements (idiosyncratic risk) will dominate

- Covariance terms (systematic risk) will be smaller than priced

- Diversification will work better than expected

When you go **short dispersion**, you're betting:

- Systematic risk will dominate

- Stocks will move together more than expected

- Diversification will fail

### 2. The Dispersion Premium

**Historical observation:**

$$
\rho^{\text{implied}} > \rho^{\text{realized}}
$$

On average, implied correlation exceeds realized correlation by 5-15%.

**Why this premium exists:**

1. **Index option demand:** Portfolio hedgers buy index puts (raises index IV)

2. **Single-stock supply:** Market makers sell single-stock options (lowers single-stock IV)

3. **Crisis fear:** Markets overprice "all stocks down together" scenarios

4. **Liquidity premium:** Index options more liquid than single stocks

**Analogy to volatility risk premium:**

Just as $\sigma^{\text{implied}} > \sigma^{\text{realized}}$ (vol risk premium), we have $\rho^{\text{implied}} > \rho^{\text{realized}}$ (dispersion premium).

**Long dispersion collects this premium** (similar to selling volatility collects vol risk premium).

### 3. Why This Structure Exists Economically

**Market participants with different needs:**

**Index put buyers (create long dispersion opportunity):**

- Pension funds hedging portfolios

- Risk parity funds

- Systematic strategies

- **Pay premium** for tail protection

**Single-stock option sellers (provide the other side):**

- Market makers managing inventory

- Corporate buyback programs

- Retail traders selling covered calls

- **Collect premium** for providing liquidity

**Dispersion traders (arbitrageurs):**

- Connect these markets

- Extract the pricing gap

- Provide liquidity to both sides

### 4. The Correlation Surface

**Professional perspective:** Options market has a full **correlation surface**:

$$
\rho(\text{strike}, \text{tenor}, \text{basket size})
$$

Different strikes, expirations, and basket compositions imply different correlations.

**Trading opportunities:**

- **Correlation skew:** OTM index puts imply higher correlation than ATM

- **Correlation term structure:** Near-term vs. long-term correlation bets

- **Cross-sectional dispersion:** Sector vs. index correlation

### 5. Fair Value Framework

**Theoretical fair value of dispersion trade:**

$$
\text{Fair Value} = \int_0^T \left[\frac{1}{2}\Gamma_{\text{net}} \sum_{i=1}^n (dS_i)^2 - \Theta_{\text{net}} dt\right]
$$

This depends on:

- Realized individual stock volatilities

- Realized correlation among stocks

- Transaction costs from rebalancing

**Break-even correlation:**

$$
\rho_{\text{breakeven}} = \frac{\left(\sum w_i \sigma_i\right)^2 - (\sigma_{\text{index}}^{\text{paid}})^2}{\sum_{i \neq j} w_i w_j \sigma_i \sigma_j}
$$

If realized correlation falls below this, long dispersion profits.

### 6. The Macro Connection

**Correlation is NOT constant:**

$$
\rho_t = f(\text{market regime}, \text{VIX level}, \text{uncertainty})
$$

**Low correlation regimes:**

- Bull markets, low VIX

- Stock-picking environment

- Idiosyncratic stories dominate

**High correlation regimes:**

- Bear markets, high VIX  

- "Risk on/risk off"

- Macro factors dominate

**Strategic implication:** Enter long dispersion in high-correlation regimes (expecting mean reversion), exit in low-correlation regimes.

### 7. Professional Institutional Perspective

**Institutional traders view dispersion as:**

1. **Correlation arbitrage:** 

   - Pure exposure to correlation risk premium

   - Similar to vol arbitrage but one level more complex

2. **Portfolio hedging tool:**

   - Short dispersion hedges "all stocks down together" scenario

   - Long dispersion profits from stock-specific moves

3. **Structural edge:**

   - Retail can't easily access (too complex, too many legs)

   - Institutions have economies of scale (lower transaction costs)

   - Market structure creates persistent mispricing

4. **Alpha generation:**

   - Uncorrelated to traditional factors

   - Provides diversification to L/S equity strategies

   - Can enhance Sharpe ratio of portfolio

**Risk management perspective:**

Dispersion trading is essentially buying insurance against:

- **Long dispersion:** Protects against correlated market rallies/selloffs

- **Short dispersion:** Protects against idiosyncratic stock events

Understanding the economic foundations helps you recognize when the strategy offers genuine edge versus when market pricing is fair. The dispersion premium exists, but it's compensation for:

- Operational complexity

- Transaction costs

- Tail risk (correlations can spike suddenly)

- Capital requirements

---

## Understanding Implied Correlation

**Before we can understand dispersion trading P&L, we need implied correlation:**

### 1. What Is Implied Correlation?

**From options, we observe:**

- Index implied volatility: $\sigma_{\text{index}}^{\text{implied}}$ (from index options)

- Individual implied volatilities: $\sigma_i^{\text{implied}}$ (from single-stock options)

**We can back out implied correlation:**

$$
\rho^{\text{implied}} = \frac{(\sigma_{\text{index}}^{\text{implied}})^2 - \sum w_i^2 (\sigma_i^{\text{implied}})^2}{\sum_{i \neq j} w_i w_j \sigma_i^{\text{implied}} \sigma_j^{\text{implied}}}
$$

**This is the correlation that the market is pricing in!**

### 2. Example

**Market data:**

- SPX (S&P 500 index) IV = 20%

- Average single-stock IV = 35%

- Equal-weighted basket of 10 stocks

**Simplified calculation:**

For equal weights ($w_i = 0.1$):

$$
(20\%)^2 = 10 \times (0.1)^2 \times (35\%)^2 + \rho \times 90 \times (0.1)^2 \times (35\%)^2
$$

$$
0.04 = 0.01 \times 0.1225 + \rho \times 0.09 \times 0.1225
$$

$$
0.04 = 0.001225 + \rho \times 0.011025
$$

$$
\rho = \frac{0.04 - 0.001225}{0.011025} \approx 0.352 = 35.2\%
$$

Wait, let me recalculate more carefully. For equal-weighted portfolio:

$$
\sigma_{\text{index}}^2 = \frac{1}{n}\overline{\sigma^2} + \left(1 - \frac{1}{n}\right)\overline{\rho \sigma^2}
$$

where $\overline{\sigma^2}$ is average variance and $\overline{\rho}$ is average correlation.

$$
(0.20)^2 = \frac{1}{10}(0.35)^2 + \frac{9}{10}\rho(0.35)^2
$$

$$
0.04 = 0.01225 + 0.11025\rho
$$

$$
\rho = \frac{0.04 - 0.01225}{0.11025} \approx 0.252 = 25.2\%
$$

**Interpretation:** Market is pricing in roughly 25% correlation among stocks.

**Your trade:**

- If you think realized correlation will be < 25% → long dispersion

- If you think realized correlation will be > 25% → short dispersion

### 3. Implied Correlation Dynamics

**Typical values:**

```
Market Regime:
Bull market (VIX 12): Implied ρ ≈ 15-20%
Normal (VIX 15-20):  Implied ρ ≈ 25-35%
Stress (VIX 25-35):  Implied ρ ≈ 40-60%
Crisis (VIX 50+):    Implied ρ ≈ 70-90%
```

**Key pattern:** Correlation spikes in crises, mean-reverts in calm periods.

**Trading implication:**

- **High implied correlation** (VIX spike, crisis) → Enter long dispersion

- **Low implied correlation** (Bull market) → Enter short dispersion or avoid

### 4. The Correlation Term Structure

**Just like vol has term structure, so does correlation:**

```
Tenor:
1-month:  ρ_implied = 40% (crisis just happened)
3-month:  ρ_implied = 30% (mean reversion expected)
6-month:  ρ_implied = 25% (long-run average)
```

**Trading opportunity:** If term structure is steep, trade the reversion.

---

## The P&L Formula

**For a dispersion trade, the P&L is complex, but conceptually:**

$$
d\Pi \approx \underbrace{\text{Correlation P\&L}}_{\text{primary profit source}} + \underbrace{\text{Vega P\&L}}_{\text{side effect}} + \underbrace{\text{Gamma P\&L}}_{\text{rebalancing}} - \underbrace{\text{Net Theta}}_{\text{carry}}
$$

**Breaking it down:**

### 1. Correlation P&L (Your Main Bet)

**This is what you're trading:**

$$
\text{Correlation P\&L} \approx f(\rho^{\text{realized}} - \rho^{\text{implied}})
$$

- **Long dispersion:** Profit when $\rho^{\text{realized}} < \rho^{\text{implied}}$ (stocks move independently)

- **Short dispersion:** Profit when $\rho^{\text{realized}} > \rho^{\text{implied}}$ (stocks move together)

**More precisely:**

$$
\text{Correlation P\&L} = \frac{1}{2}\Gamma_{\text{index}}\left[(\Delta S_{\text{index}})^2 - \sum_{i=1}^n w_i (\Delta S_i)^2\right]
$$

The index move vs. sum of individual moves captures correlation.

**Example:**

If stocks move independently (low correlation):

- Individual stock moves are large: $\sum w_i (\Delta S_i)^2$ is large

- But they cancel in index: $(\Delta S_{\text{index}})^2$ is small

- **Long dispersion profits:** You're long individual gammas, short index gamma

If stocks move together (high correlation):

- Individual stock moves: $\sum w_i (\Delta S_i)^2$ 

- Index move nearly equals sum: $(\Delta S_{\text{index}})^2 \approx \sum w_i (\Delta S_i)^2$

- **Long dispersion breaks even or loses** (no correlation benefit)

### 2. Vega P&L (Side Effect)

**Changes in implied volatilities affect position value:**

$$
\text{Vega P\&L} = -\mathcal{V}_{\text{index}} \Delta\sigma_{\text{index}} + \sum_{i=1}^n w_i \mathcal{V}_i \Delta\sigma_i
$$

**For vega-neutral position:**

This should be close to zero, but in practice:

- Index IV and single-stock IVs don't move perfectly together

- Can create unexpected P&L

**Example:**

Market selloff:

- Index IV spikes +10 points (hurts short index position)

- Single-stock IVs increase +8 points (helps long stock positions)

- **Net vega P&L:** Slightly negative

### 3. Gamma P&L (Rebalancing)

**Daily profit/loss from delta rebalancing:**

$$
\text{Gamma P\&L} = -\frac{1}{2}\Gamma_{\text{index}}(\Delta S_{\text{index}})^2 + \sum_{i=1}^n w_i \frac{1}{2}\Gamma_i (\Delta S_i)^2
$$

**This is closely related to correlation P&L.**

**Key insight:** The more stocks move independently, the more gamma P&L you make from rebalancing individual positions.

### 4. Theta P&L (Time Decay)

**Daily cost of holding options:**

$$
\text{Theta P\&L} = -\Theta_{\text{index}} + \sum_{i=1}^n w_i \Theta_i
$$

**For long dispersion:**

- You're long individual options (negative theta)

- You're short index options (positive theta)

- **Net theta can be positive or negative** depending on position sizing

**Typical structure:** Small positive or neutral theta for long dispersion (you're collecting premium on index, paying on stocks, roughly balanced).

### 5. Complete Daily P&L

**Putting it together:**

$$
\text{Daily P\&L} = \underbrace{\frac{1}{2}\Gamma_{\text{net}}\left[\sum w_i (dS_i)^2 - (dS_{\text{index}})^2\right]}_{\text{Correlation/Gamma}} + \underbrace{\mathcal{V}_{\text{net}} d\sigma}_{\text{Vega}} + \underbrace{\Theta_{\text{net}} dt}_{\text{Theta}}
$$

**Your goal:** Make first term dominate (correlation working in your favor).

---

## Long vs. Short Dispersion

### 1. Long Dispersion (Most Common)

**Structure:**

- Short index options

- Long individual stock options

- Delta hedged

**Greeks profile:**

- $\Gamma_{\text{net}} > 0$ (net long gamma on individual stocks)

- $\mathcal{V}_{\text{net}} \approx 0$ (vega neutral)

- $\Theta_{\text{net}} \approx 0$ (roughly neutral)

**Profit when:**

- Correlation decreases

- Stocks move independently

- Realized correlation < implied correlation

**Typical scenarios:**

- Enter after VIX spike (implied corr high)

- Exit as correlations normalize

- Collect dispersion premium

**Risk:**

- "Correlation goes to 1 in crisis"

- All stocks crash together

- Index gamma loss > individual gamma gains

### 2. Short Dispersion (Contrarian)

**Structure:**

- Long index options

- Short individual stock options

- Delta hedged

**Greeks profile:**

- $\Gamma_{\text{net}} < 0$ (net short gamma)

- $\mathcal{V}_{\text{net}} \approx 0$ (vega neutral)

- $\Theta_{\text{net}} > 0$ (positive theta)

**Profit when:**

- Correlation increases

- Stocks move together

- Realized correlation > implied correlation

**Typical scenarios:**

- Enter in low correlation environment

- Bet on mean reversion to higher correlation

- Or anticipate crisis/shock

**Risk:**

- If stocks remain uncorrelated, bleed theta

- Transaction costs from managing many short stock options

### 3. Comparison

| Aspect | Long Dispersion | Short Dispersion |
|--------|----------------|------------------|
| **Position** | Long stocks, short index | Short stocks, long index |
| **Gamma** | Long individual gamma | Short individual gamma |
| **Theta** | Neutral to slightly positive | Positive |
| **Profits from** | Low correlation | High correlation |
| **Historical edge** | Dispersion premium | Against premium |
| **Crisis behavior** | Loses (corr spikes) | Wins (corr spikes) |
| **Complexity** | High (many stocks) | Very high (short many) |

**Most institutional players:** Long dispersion default, short dispersion tactically.

---

## Example Trade Walkthrough

**Let's make this concrete with a simplified example:**

### 1. Setup

**Choose basket:**

- Stock A, B, C, D, E (equal weighted in basket)

- Basket value: $500 ($100 each)

**Market data:**

- Each stock IV: 40%

- Index IV: 25%

- This implies correlation ≈ 20%

**Your view:** Stocks will move more independently (realized correlation < 20%)

### 2. Step 1

**Index options:**

- Sell 1 ATM call (25 IV)

- Sell 1 ATM put (25 IV)

- Collect: $25 premium

**Greeks:**

- $\Gamma_{\text{index}} = 0.05$

- $\mathcal{V}_{\text{index}} = 100$

- $\Theta_{\text{index}} = +15$ /day

### 3. Step 2

**For each stock (A, B, C, D, E):**

- Buy ATM call (40 IV)

- Buy ATM put (40 IV)

- Pay: $10 per stock × 5 = $50 total

**Greeks (per stock):**

- $\Gamma_i = 0.015$

- $\mathcal{V}_i = 25$

- $\Theta_i = -6$ /day

**Total:**

- $\Gamma_{\text{stocks}} = 5 \times 0.015 = 0.075$

- $\mathcal{V}_{\text{stocks}} = 5 \times 25 = 125$

- $\Theta_{\text{stocks}} = 5 \times (-6) = -30$ /day

### 4. Step 3

**Net Greeks:**

- $\Gamma_{\text{net}} = 0.075 - 0.05 = 0.025$ (long gamma)

- $\mathcal{V}_{\text{net}} = 125 - 100 = 25$ (long vega, adjust if needed)

- $\Theta_{\text{net}} = 15 - 30 = -15$ /day (paying theta)

**Cost:**

- Paid $50 for stocks

- Collected $25 from index

- **Net cost: $25**

### 5. Step 4

**Initial deltas:**

- Index: $\Delta_{\text{index}} = 0$ (sold ATM straddle)

- Each stock: $\Delta_i = 0$ (bought ATM straddles)

**Hedge needed:** None initially (already delta neutral).

### 6. 1

**Day 1 moves:**

- Stock A: +5%

- Stock B: -4%

- Stock C: +6%

- Stock D: -3%

- Stock E: +2%

**Index move:** 
$$
\Delta S_{\text{index}} = \frac{1}{5}(5 - 4 + 6 - 3 + 2) = \frac{6}{5} = 1.2\%
$$

**P&L calculation:**

**Index gamma loss:**
$$

-\frac{1}{2} \times 0.05 \times (1.2)^2 \times 500^2 = -\$18
$$

**Individual gamma gains:**
$$
\frac{1}{2} \times 0.015 \times [(5^2 + 4^2 + 6^2 + 3^2 + 2^2)] \times 100^2
$$
$$
= \frac{1}{2} \times 0.015 \times 90 \times 100^2 = \$675
$$

Wait, let me recalculate this properly. The gamma P&L should be:

$$
\text{Gamma P\&L}_i = \frac{1}{2}\Gamma_i (S_i \times \Delta\%)^2 = \frac{1}{2} \times 0.015 \times (100 \times 0.05)^2 = 0.1875
$$

For all stocks:
$$
= \frac{1}{2} \times 0.015 \times [(5^2 + 4^2 + 6^2 + 3^2 + 2^2)] = 0.0075 \times 90 = \$0.675
$$

Actually, gamma P&L should be calculated as:
$$
\text{Gamma P\&L} = \frac{1}{2}\Gamma (\Delta S)^2
$$

Let me redo this more carefully:

**Individual stocks:**

- Stock A: $\frac{1}{2} \times 0.015 \times 5^2 = 0.1875$

- Stock B: $\frac{1}{2} \times 0.015 \times 4^2 = 0.12$

- Stock C: $\frac{1}{2} \times 0.015 \times 6^2 = 0.27$

- Stock D: $\frac{1}{2} \times 0.015 \times 3^2 = 0.0675$

- Stock E: $\frac{1}{2} \times 0.015 \times 2^2 = 0.03$

- **Total: $0.675$**

**Index:**

- $-\frac{1}{2} \times 0.05 \times 1.2^2 = -0.036$

**Net gamma P&L: $0.675 - 0.036 = \$0.639$**

**Plus theta P&L:** $-15$ (one day)

**Day 1 P&L: $0.64 - 0.15 = $0.49$**

Over 30 days, if this pattern continues:
$$
30 \times 0.49 = \$14.7 \text{ profit on } \$25 \text{ cost} = 59\% \text{ return}
$$

### 7. 2

**Day 1 moves: All stocks move together**

- Stock A, B, C, D, E: All +5%

**Index move:** +5% (perfect correlation)

**P&L calculation:**

**Individual gamma gains:**
$$
5 \times \frac{1}{2} \times 0.015 \times 5^2 = \$0.9375
$$

**Index gamma loss:**
$$

-\frac{1}{2} \times 0.05 \times 5^2 = -\$0.625
$$

**Net gamma P&L: $0.9375 - 0.625 = \$0.3125$**

**Plus theta P&L:** $-0.15$

**Day 1 P&L: $0.31 - 0.15 = \$0.16$**

Much worse than low-correlation case! Over time, if this continues:
$$
30 \times 0.16 = \$4.8 \text{ profit on } \$25 \text{ cost} = 19\% \text{ return}
$$

Or could even lose if theta dominates.

**Key insight:** Same absolute moves, but **correlation matters enormously** for P&L.

---

## Time Evolution and Management

### 1. Entry Timing

**Best times to enter long dispersion:**

1. **After VIX spikes** (correlation elevated)

   - Implied correlation: 60-70%

   - Expected: Mean reversion to 30-40%

   - Trade the reversion

2. **High dispersion premium** (implied corr >> realized corr)

   - Historical spread: 5-10%

   - Current spread: 15-20%

   - Abnormally high premium

3. **Market stabilizing** after crisis

   - Correlation spiked during crisis

   - Now normalizing

   - Capture the decline

**Avoid entering:**

- Low VIX environments (correlation already low)

- No dispersion premium (implied ≈ realized)

- Right before known crisis events

### 2. Position Management Framework

**Daily tasks:**

1. **Delta rebalance**

   - Check all deltas (index + all stocks)

   - Rebalance if any $|\Delta| > \text{threshold}$

   - Minimize transaction costs

2. **P&L attribution**

   - Gamma P&L: How much from moves?

   - Vega P&L: How much from IV changes?

   - Theta P&L: Time decay cost

   - **Correlation P&L: Is thesis working?**

3. **Greeks monitoring**

   - Vega still neutral?

   - Gamma exposure within limits?

   - Theta bleed acceptable?

### 3. Rebalancing Strategy

**Delta rebalancing:**

Set thresholds:

- Rebalance when $|\Delta| > 0.10$ per position

- Or daily at consistent time (e.g., close)

**Example:**

Stock A moved +5%:

- Call delta now 0.70, put delta -0.30

- Net delta: +0.40

- **Action:** Sell 0.40 shares of stock A

**Transaction costs:**

Each rebalance costs bid-ask spread + commissions:

- 10 stocks × daily rebalancing × 0.02% spread = 0.2% daily

- Over 30 days: ~6% cost!

**Trade-off:**

- Frequent rebalancing: Better delta neutrality, but higher costs

- Infrequent rebalancing: Lower costs, but more delta risk

**Professional approach:** Rebalance when delta exceeds threshold, not on fixed schedule.

### 4. Exit Strategies

**Take profit when:**

1. **Realized correlation significantly below implied**

   - Entered at implied 60%, realized running at 30%

   - Lock in profit before mean reversion

2. **Hit profit target**

   - e.g., +40% on premium paid

   - Take risk off table

3. **Correlation normalizing**

   - Mean reversion complete

   - No more edge

**Cut losses when:**

1. **Correlation rising, not falling**

   - Wrong on thesis

   - Exit before losses accelerate

2. **VIX spiking again**

   - Correlation going to spike

   - Long dispersion will suffer

3. **Transaction costs eating profits**

   - Realized that operational costs > edge

   - Close before grinding to zero

### 5. Roll Strategy

**As expiration approaches:**

Option 1: **Close entire position**

- Take profit/loss

- Clean exit

Option 2: **Roll forward**

- Close current options

- Open new options in next expiry

- Continue correlation bet

**When to roll:**

- Thesis still valid

- Implied correlation still elevated

- Haven't hit profit target yet

**When to close:**

- Thesis invalidated

- Correlation normalized

- Operational fatigue

---

## Analysis

### 1. 1

**Setup:**

- VIX spike to 35 (crisis)

- Implied correlation: 70%

- Enter long dispersion

**What happens:**

- Markets stabilize over 30 days

- VIX drops to 18

- Realized correlation: 25%

**P&L drivers:**

Correlation P&L: Large positive (25% vs. 70% implied)
Gamma P&L: Positive from independent stock moves
Vega P&L: Neutral (vega balanced)
Theta P&L: Slightly negative

**Result:** +60% return in 30 days

**Why it worked:**

- Entered at peak correlation

- Captured mean reversion

- Thesis validated

### 2. 2

**Setup:**

- Enter long dispersion after initial VIX spike

- Think worst is over

**What happens:**

- Second wave of crisis

- VIX spikes further to 50

- Correlation goes to 85%

**P&L drivers:**

Correlation P&L: Large negative (85% vs. 70% expected)
Gamma P&L: Negative (all stocks moving together)
Vega P&L: Negative (index IV rising faster than stock IVs)
Theta P&L: Negative

**Result:** -40% loss in 10 days

**Why it failed:**

- Wrong timing (crisis not over)

- Correlation can spike further

- "All correlations go to 1" in crisis

### 3. 3

**Setup:**

- Enter long dispersion in normal market

- Implied correlation: 35%

- Realize realized correlation is also 35%

**What happens:**

- Over 60 days, correlation stays at 35%

- No edge materializes

- Theta bleeds position

**P&L drivers:**

Correlation P&L: Zero (realized = implied)
Gamma P&L: Neutral (net zero gamma)
Vega P&L: Neutral
Theta P&L: Negative (-$15/day × 60 = -$900)

**Transaction costs:** -$500 (rebalancing)

**Result:** -20% loss from theta + costs

**Why it failed:**

- No mispricing (implied = realized)

- Paid theta for nothing

- Transaction costs added up

### 4. 4

**Setup:**

- Enter long dispersion

- Balanced position (vega neutral)

**What happens:**

- Index IV decreases 10 points (good for short index)

- But stock IVs decrease 5 points (bad for long stocks)

**P&L drivers:**

Correlation P&L: Working as expected
Vega P&L: **Large positive** (unbalanced vega moves)
Gamma P&L: Positive
Theta P&L: Negative

**Result:** +45% return (mostly from vega!)

**Why it worked:**

- Got lucky on vol moves

- Index vol decreased more than stock vol

- Unintended profit source

### 5. 5

**Setup:**

- Enter dispersion on 20 illiquid stocks

- Wide bid-ask spreads (0.5%)

**What happens:**

- Correlation trades work (+30% on paper)

- But constant rebalancing

- 20 stocks × daily rebalances × 0.5% = 10% per day!

**P&L drivers:**

Correlation P&L: +$300
Transaction costs: -$250
Theta P&L: -$100

**Result:** -$50 loss despite being right!

**Why it failed:**

- Transaction costs overwhelmed edge

- Too many illiquid positions

- Operational execution poor

---

## Risk Management

### 1. Position Sizing

**Maximum size calculation:**

$$
\text{Max Position} = \frac{\text{Portfolio} \times \text{Risk\%}}{\text{Max Expected Loss}}
$$

**For dispersion:**

- Risk 5% of portfolio

- Max expected loss: 50% (crisis scenario)

- **Max position: 10% of portfolio**

**Practical limits:**

1. **Per-trade limit:** 5-10% of portfolio

2. **Concentration limit:** No more than 2-3 dispersion trades simultaneously

3. **Correlation to other trades:** Consider correlations with other strategies

### 2. Greeks Limits

**Set hard limits on Greeks exposure:**

**Gamma:**

- Max net gamma: $0.10 per $100k portfolio

- Prevents excessive rebalancing costs

**Vega:**

- Keep vega neutral: $|\mathcal{V}_{\text{net}}| < \$50$ per $100k

- Avoid unintended volatility bets

**Theta:**

- Max daily theta: -$30 per $100k portfolio

- Limit time decay risk

**Delta:**

- Rebalance when $|\Delta| > 0.10$ per position

- Maintain direction neutrality

### 3. Correlation Risk Limits

**Monitor correlation exposure:**

$$
\text{Correlation Exposure} = \Gamma_{\text{net}} \times (\rho^{\text{breakeven}} - \rho^{\text{current}})
$$

**Risk limits:**

1. **Max correlation exposure:** 100 bps of correlation

   - If breakeven is 30%, limit position so max loss occurs at 40% correlation

2. **Stress test:** What if correlation goes to 90% (crisis)?

   - Ensure survivable loss

3. **Concentration:** Don't have all dispersion trades with same correlation bet

   - Diversify across sectors, regions, time horizons

### 4. Stop Loss Rules

**Hard stops:**

1. **Portfolio-level:** Exit if position down 20-30%

2. **Correlation-level:** Exit if realized correlation moves 15% against you

3. **VIX-level:** Exit if VIX spikes +10 points suddenly

4. **Time-based:** Exit if no progress after 50% of time elapsed

### 5. Operational Risk Management

**Dispersion is operationally complex:**

1. **Number of positions:** 10-20+ individual stocks + index

2. **Rebalancing frequency:** Daily or more

3. **Transaction costs:** Can exceed edge if not careful

4. **Systems risk:** Need robust systems to manage

**Mitigation:**

- Start small (5-stock basket)

- Automate rebalancing (algo execution)

- Monitor transaction costs daily

- Have backup systems

### 6. Crisis Risk (The Big One)

**"All correlations go to 1 in a crisis"**

**Long dispersion is SHORT a crisis:**

- When markets crash, stocks correlate

- Your short index position loses BIG

- Your long stock positions don't gain enough

- **Net: Large loss**

**Protection strategies:**

1. **Size conservatively:** Never so large that crisis wipes you out

2. **Stop loss:** Exit if VIX spikes significantly

3. **Hedge:** Buy OTM index puts as tail hedge

4. **Timing:** Only enter after crisis starts (don't enter before)

**Historical examples:**

- **2008 Crisis:** Correlation went to 85%, long dispersion lost 40-60%

- **2020 COVID:** Correlation spiked to 90%, long dispersion crushed

- **2022 Bear:** Correlation elevated but not extreme, long dispersion OK

---

## Advanced Topics

### 1. Dispersion vs. Correlation Swaps

**Dispersion trading:** Options-based, delta hedged

**Correlation swaps:** Direct derivative on correlation

$$
\text{Payoff}_{\text{corr swap}} = \text{Notional} \times (\rho^{\text{realized}} - \rho^{\text{strike}})
$$

**Advantages of correlation swaps:**

- Pure exposure (no gamma, vega, theta complications)

- No rebalancing needed

- Simpler P&L

**Disadvantages:**

- OTC only (no exchange)

- Less liquid

- Harder for retail

**Most institutions:** Use dispersion (options) because liquidity and ability to lever.

### 2. Sector vs. Index Dispersion

**Instead of index vs. stocks, trade sector vs. stocks:**

Example:

- Short XLF options (Financial sector ETF)

- Long options on JPM, BAC, C, WFC, etc.

**Advantages:**

- More homogeneous basket (banks vs. banks)

- Clearer correlation dynamics

- Less diversification benefit to eliminate

**Disadvantages:**

- Less liquidity in sector options

- Smaller dispersion premium

### 3. Cross-Asset Dispersion

**Extend concept across asset classes:**

- Short multi-asset index (e.g., balanced fund)

- Long individual equity, bond, commodity, FX options

**Betting on:** Asset class correlations

**Professional application:** Risk parity funds use this to manage correlation exposure.

### 4. Implied vs. Local Correlation

**Two types of correlation:**

1. **Implied correlation:** Backed out from current option prices

2. **Local correlation:** Instantaneous correlation between returns

$$
\rho_{\text{local}}(S, t) = \text{Corr}(dS_i, dS_j | S, t)
$$

**They're different!** Local correlation can vary with stock prices and time.

**Trading opportunity:** If you have better model of local correlation, can exploit mismatch with implied correlation.

---

## Common Mistakes

### 1. Mistake 1

**The error:**
"Correlation edge is 5%, so I'll make 5%!"

**The reality:**

- Rebalancing costs: 3%

- Bid-ask spreads: 1.5%

- Slippage: 0.5%

- **Net: 0% after costs**

**Lesson:** Transaction costs can exceed edge. Need scale and efficiency.

**Fix:**

- Trade liquid names only

- Batch rebalancing

- Use algorithms

- Calculate break-even considering costs

### 2. Mistake 2

**The error:**
"Max loss is premium, so I can size large"

**The reality:**

In crisis, correlation spikes:

- 30% position loses 40% = -12% portfolio

- 50% position loses 40% = -20% portfolio

**Lesson:** Size for crisis scenarios, not normal scenarios.

**Fix:**

- Max 10% per position

- Stress test for 90% correlation

- Have stop losses

### 3. Mistake 3

**The error:**
"Correlation is low (20%), let me go long dispersion"

**The reality:**

Low correlation can stay low or go lower:

- Already at equilibrium

- No mean reversion edge

- Just paying theta

**Lesson:** Enter when correlation is EXTREME (high for long dispersion), not normal.

**Fix:**

- Wait for VIX spike (implied corr high)

- Enter after crisis starts

- Trade the reversion, not the level

### 4. Mistake 4

**The error:**
"I matched notionals, so I'm vega neutral"

**The reality:**

$$
\mathcal{V}_{\text{index}} \neq \sum w_i \mathcal{V}_i
$$

Even with equal notionals, vegas differ by:

- Strike (ATM vs. OTM)

- Tenor (different expirations)

- Vol of vol (different sensitivities)

**Lesson:** Check vegas explicitly, don't assume.

**Fix:**

- Calculate $\mathcal{V}_{\text{net}}$ daily

- Adjust weights to maintain neutrality

- Monitor vega P&L separately

### 5. Mistake 5

**The error:**
"More stocks = more diversification = better"

**The reality:**

50 stocks in basket:

- 50 × daily rebalancing

- 50 × option positions

- 50 × transaction costs

- Operational nightmare

**Lesson:** Sweet spot is 10-20 stocks for retail, 20-50 for institutions.

**Fix:**

- Start with 5-10 stocks

- Focus on liquid names

- Keep operationally manageable

### 6. Mistake 6

**The error:**
"Correlation is rising, but my thesis says it should fall. Hold!"

**The reality:**

Correlation can stay high longer than you can stay solvent:

- 2008: High correlation lasted months

- Theta bleeding daily

- Transaction costs mounting

**Lesson:** Have stop loss. Don't fight clear trend.

**Fix:**

- Exit if correlation moves 15% against you

- Don't average down

- Live to trade another day

### 7. Mistake 7

**The error:**
"Options are for volatility, dividends don't matter"

**The reality:**

Stock options affected by dividends:

- Forward price adjustment

- Put-call parity shifts

- Can create unwanted delta

**Lesson:** Dividend events can disrupt carefully balanced position.

**Fix:**

- Track ex-dividend dates

- Adjust positions before ex-div

- Account for dividend in pricing

### 8. Mistake 8

**The error:**
"Vega neutral means no exposure to volatility changes"

**The reality:**

Vega neutral means:
$$
\mathcal{V}_{\text{net}} = 0
$$

But you still have exposure to:

- **Realized volatility** (through gamma)

- **Correlation** (your actual bet)

- **Vol of vol** (vanna, volga)

**Lesson:** Vega neutral ≠ volatility neutral. You're still trading volatility through correlation.

**Fix:**

- Understand what you're actually trading

- Track realized vol separately from implied vol

- Know your true exposures

### 9. Mistake 9

**The error:**
"ATM index options and ATM stock options, all set"

**The reality:**

Skew differs between index and stocks:

- Index: Steep put skew (crash protection)

- Stocks: Varied skew (some flat, some steep)

**Lesson:** Skew differences create hidden vega exposure.

**Fix:**

- Match strikes carefully (both ATM)

- Monitor skew changes

- Consider using multiple strikes

### 10. Mistake 10

**The error:**
"I'll just see what happens and adjust"

**The reality:**

Without plan:

- Don't know when to exit

- Emotional decisions

- Death by indecision

**Lesson:** Need clear rules before entering.

**Fix:**

Before entry, define:

1. Profit target: +40%

2. Stop loss: -30%

3. Time limit: 60 days max

4. Correlation exit: If realized > implied by 15%, exit

5. VIX exit: If VIX spikes +10, exit

**Write it down. Follow it.**

---

## Real-World Examples

### 1. Pension Duration Cut via Futures

**Setup:**

- March 2009, post-Lehman crisis

- VIX peaked at 80, now at 40

- Implied correlation: 75%

- Historical average: 35%

**Trade:**

- Long dispersion on S&P financials basket

- 10 banks: JPM, BAC, C, WFC, GS, MS, USB, PNC, STT, BK

- 60-day options

**Entry:**

- Paid $50k for individual straddles

- Collected $35k from XLF index straddles

- **Net cost: $15k**

**What happened:**

**Weeks 1-4:**

- Markets stabilized

- Correlation dropped: 75% → 55%

- Some stocks rallied, others lagged

- **P&L: +$8k** (+53%)

**Weeks 5-8:**

- Correlation continued normalizing: 55% → 40%

- Individual stocks showing distinct patterns

- **P&L: +$12k** (+80%)

**Week 8: Exit**

- Realized correlation: 38%

- Close to long-run average

- **Final P&L: +$12k on $15k** = 80% in 60 days

**Post-trade analysis:**

✓ Perfect timing (entered after crisis peak)
✓ Captured mean reversion
✓ Exited before over-staying

**Key lesson:** Post-crisis is ideal time for long dispersion.

### 2. Transition Risk Hedge

**Setup:**

- June 2016, Brexit vote imminent

- Trader thinks "volatility will be high but correlation normal"

- Enters long dispersion

**Trade:**

- Long dispersion on FTSE 100 basket

- 30-day options

- Net cost: £20k

**What happened:**

**Day of Brexit vote:**

- Leave wins (surprise!)

- Markets crash globally

- Correlation spikes: 40% → 85%

**P&L drivers:**

- Index straddle (short): Lost £15k (massive index move)

- Individual straddles (long): Gained £10k (all stocks moved, but not enough)

- **Net: -£5k** (-25%) in ONE DAY

**Aftermath:**

- Correlation stayed elevated

- Continued losses over next week

- **Final: -£8k loss** (-40%)

**Post-trade analysis:**

✗ Wrong timing (entered before binary event)
✗ Didn't anticipate correlation spike
✗ No stop loss in place

**Key lesson:** Don't enter before binary events. Correlation can spike violently.

### 3. Portable Alpha with Futures

**Setup:**

- Early March 2020, COVID spreading

- VIX at 30, rising

- Trader enters long dispersion thinking "VIX is high"

**Trade:**

- Long dispersion on tech stocks

- AAPL, MSFT, GOOGL, AMZN, FB, NFLX, NVDA, etc.

- 45-day options

- Net cost: $30k

**What happened:**

**March 12-16 (Crash week):**

- VIX spikes to 85

- ALL stocks crash together

- Correlation: 50% → 95%

**P&L cascade:**

Day 1: -$3k
Day 2: -$5k  
Day 3: -$8k
Day 4: -$6k
Day 5: -$4k

**Week 1: -$26k** (-87% of capital!)

**Trader response:**

- Panic sold remaining positions

- **Final loss: -$28k** (-93%)

**Post-trade analysis:**

✗ Catastrophically wrong timing
✗ Entered as crisis was STARTING, not ending
✗ No risk management (position too large)
✗ "All correlations go to 1 in crisis" proven again

**Key lesson:** Long dispersion is disastrous in beginning of crisis. Only enter AFTER peak.

### 4. Tactical Duration Extension

**Setup:**

- 2017, VIX at historical lows (10-12)

- Implied correlation: 25%

- Trader enters long dispersion thinking "seems cheap"

**Trade:**

- Long dispersion on S&P 500 basket

- 90-day rolling position (kept rolling every 30 days)

- Average net cost: $10k per roll

**What happened:**

**Month 1:**

- Correlation: 25% (unchanged)

- Theta: -$3k

- Transaction costs: -$1k

- **P&L: -$4k**

**Month 2:**

- Correlation still 25%

- Theta: -$3k

- Transaction costs: -$1k

- **P&L: -$4k**

**Month 3:**

- Getting frustrated, but "any day now..."

- Correlation: 26% (wrong direction!)

- Theta: -$3k

- Transaction costs: -$1k

- **P&L: -$5k**

**Total over 3 months: -$13k on average $10k position**

**Finally exits after 3 months.**

**Post-trade analysis:**

✗ No edge (implied = realized)
✗ Paid theta for nothing
✗ Transaction costs compounded
✗ Wrong environment (VIX already low, no room for correlation to fall)

**Key lesson:** Don't enter when correlation is already normal. Need extremes.

### 5. Duration Hedge Failure in Crisis

**Setup:**

- Late 2019, trade war cooling

- VIX low (12-15)

- Correlation low (18%)

- Trader thinks "correlation will rise as uncertainty increases"

**Trade:**

- **Short dispersion** on tech stocks

- Long QQQ straddle, short individual straddles

- Net credit: $8k (positive theta position)

**What happened:**

**Weeks 1-4:**

- Trade tensions flare up

- Market becomes "risk on/risk off"

- Correlation rises: 18% → 25%

- **P&L: +$3k**

**Weeks 5-8:**

- Correlation continues rising: 25% → 32%

- All tech stocks moving together

- Theta collecting: +$120/day

- **P&L: +$6k**

**Week 8: Exit**

- Hit profit target (+75% on premium)

- Exit before correlation mean reverts

- **Final P&L: +$6k on $8k** = 75% return

**Post-trade analysis:**

✓ Correct timing (low correlation, macro uncertainty building)
✓ Right strategy for environment (short dispersion when correlation will rise)
✓ Good exit discipline (took profits)

**Key lesson:** Short dispersion can work, but requires different setup (low correlation → rising).

### 6. Common Patterns Across Examples

**Winners had:**

1. Correct timing relative to correlation cycle

2. Clear thesis (correlation direction)

3. Risk management (stops or profit targets)

4. Understanding of regime

**Losers had:**

1. Wrong timing (entering before crisis or at wrong point in cycle)

2. No risk management (too large, no stops)

3. Fighting the tape (holding losing positions)

4. Misunderstanding correlation dynamics

---



## Practical Guidance

**Step-by-step implementation framework:**

### 1. Step 1

**Before entering, evaluate:**

**Volatility environment:**

Check:

- Current VIX level: ____

- VIX percentile (0-100): ____

- VIX trend (rising/falling): ____

**Interpretation:**

- VIX >30 + falling: Good for long dispersion ✓

- VIX 15-25 + stable: Neutral, wait

- VIX <15 + rising: Avoid long dispersion ✗

**Correlation environment:**

Calculate:

- Implied correlation: ____ % (from options)

- Realized correlation (30-day): ____ %

- Historical average: ____ %

**Interpretation:**

- Implied > Realized + 10%: Dispersion premium exists ✓

- Implied ≈ Realized: No edge, avoid

- Implied < Realized: Wrong setup for long dispersion ✗

**Market conditions:**

- Liquidity: Check bid-ask spreads (<0.5% okay)

- Options volume: Need minimum 1000 contracts/day per name

- Volatility of volatility: High vol-of-vol = harder to manage

### 2. Step 2

**Enter LONG dispersion when:**

1. VIX >30 after spike (crisis aftermath)

2. Implied correlation >60% (extreme level)

3. Dispersion premium >10% (implied >> realized)

4. Clear catalyst for normalization (Fed action, crisis resolution)

**Avoid long dispersion when:**

1. VIX <20 and stable (correlation already normal)

2. Implied correlation <40% (no room to fall)

3. No dispersion premium (implied ≈ realized)

4. Crisis just beginning (correlation can spike further)

**Enter SHORT dispersion when:**

1. VIX <15 (historically low)

2. Implied correlation <25% (very low)

3. Macro uncertainty building (expect rise)

4. Mean reversion setup (correlation too low)

### 3. Step 3

**Select 10-20 stocks:**

Criteria:

- Liquid (>$10M daily volume)

- Optionable (tight bid-ask on options)

- Representative of index

- Mix of sectors

**Example S&P basket (10 stocks):**

- Tech: AAPL, MSFT, GOOGL

- Finance: JPM, BAC

- Healthcare: UNH, JNJ

- Consumer: AMZN, WMT

- Industrial: CAT

**Weighting:**

Use market-cap weighted or equal-weighted:

- Market-cap: Matches index better

- Equal-weighted: Simpler, easier to manage

### 4. Step 4

**Calculate maximum position size:**

$$
\text{Max Size} = \frac{\text{Portfolio} \times 5\%}{\text{Expected Max Loss (50\%)}} = \text{Portfolio} \times 10\%
$$

**But be conservative: Use 5% of portfolio as cost**

**Example:**

- Portfolio: $500k

- Max position cost: $25k (5%)

- This limits worst-case loss to ~$12.5k (2.5% of portfolio)

**Check Greeks limits:**

Before entering, verify:

- $|\mathcal{V}_{\text{net}}| < 10\% \text{ of portfolio vega capacity}$

- $|\Gamma_{\text{net}}| < 0.05 \text{ per } \$100k$

- $|\Theta_{\text{net}}| < \$50/\text{day per } \$100k$

### 5. Step 5

**Order of operations:**

1. **Calculate vega-neutral weights** first

2. **Enter index options** (sell straddles)

3. **Simultaneously enter stock options** (buy straddles)

4. **Delta hedge immediately** (futures or ETFs)

5. **Verify Greeks** match targets

**Best practices:**

- Use limit orders (don't market order)

- Enter during liquid hours (10am-3pm)

- Check spreads before entering (wide spreads = bad)

- Split order if large (don't move market)

**Execution example:**

```
Target: Long dispersion, $25k cost

Step 1: Sell SPY straddles

- Sell 10 calls at $5.00

- Sell 10 puts at $5.00

- Collect: $10k

Step 2: Buy individual straddles

- Buy each stock straddle for $3.5k

- Total: $35k

Step 3: Verify

- Net cost: $35k - $10k = $25k ✓

- Vega net: -100 + 125 = +25 (adjust)

Step 4: Adjust for vega neutral

- Reduce stock positions slightly

- Final vega net: -5 (close enough)

Step 5: Delta hedge

- All deltas initially ~0

- No hedge needed yet
```

### 6. Step 6

**Daily checklist (5-10 minutes):**

□ Check all deltas (should be near 0)
□ Rebalance if |Δ| > 0.10 anywhere
□ Calculate daily P&L by component
□ Update correlation estimate
□ Check for dividends or corporate actions

**Weekly deep dive (30 minutes):**

□ Recalculate implied correlation
□ Calculate realized correlation
□ P&L attribution (correlation, gamma, vega, theta)
□ Verify thesis still valid
□ Check proximity to profit target or stop loss

**Rebalancing triggers:**

**Delta:** Rebalance when |Δ| > 0.10

- Example: Stock delta goes from 0 to +0.15

- Action: Sell 0.15 shares to neutralize

**Vega:** Rebalance when |Vega net| > $50

- Adjust weights to restore neutrality

- Usually monthly, not daily

**Gamma:** Monitor but don't rebalance gamma

- Gamma is your profit source

- Let it fluctuate

### 7. Step 7

**Take profit triggers (any one):**

1. Hit profit target (+40-60%)

2. Realized correlation < implied by 20%+

3. Correlation normalized (back to historical average)

4. VIX normalized (<18)

**Stop loss triggers (any one):**

1. Position down 20-30%

2. Realized correlation > implied by 15%

3. VIX spiking +10 points

4. 50% of time elapsed with no profit

**Exit execution:**

**Method 1: Full exit**

- Close all positions simultaneously

- Accept some slippage for clean exit

- Best for stop losses

**Method 2: Staged exit**

- Close 50% at first profit trigger

- Close remaining 50% at second trigger

- Good for taking profits gradually

**Example exit:**

```
Week 5: Position at +45%
→ Close 50% (lock in +22.5% on half)
→ Hold 50% (aiming for +60%)

Week 7: Position now at +55%
→ Close remaining 50% (+27.5% on second half)
→ Total: +50% average

VS. holding all: Might hit +60%, might fall to +30%
```

### 8. Step 8

**Track every trade:**

```
Trade Journal Template:

Date: _______
Position: Long dispersion on [basket]
Cost: $______
Greeks: Δ=__, Γ=__, ν=__, θ=__

Entry Thesis:

- Implied correlation: ____%

- Expected realized: ____%

- Expected profit: ___%

Weekly Updates:
Week 1: Realized corr ___, P&L ___
Week 2: Realized corr ___, P&L ___
...

Exit:
Date: ______
Exit correlation: ____%
Final P&L: ___% (vs. ___% target)

Lessons:
✓ What worked:
✗ What didn't:
→ Next time:
```

**This journal is GOLD for learning!**

---

## Common Mistakes

[Content as provided in original document]

---
