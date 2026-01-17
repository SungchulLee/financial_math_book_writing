# Cryptocurrency Correlation with Traditional Assets


**Crypto-TradFi correlation analysis** examines the dynamic relationships between Bitcoin, Ethereum, and traditional assets (equities, bonds, gold, commodities) across different market regimes, revealing that correlations are highly unstable—ranging from near-zero during normal periods (supporting the "digital gold" diversification thesis) to 0.6-0.8+ during market stress (eliminating diversification benefits precisely when needed most), with structural breaks occurring around major events (COVID crash, Fed tightening cycles, risk-off episodes), making naive portfolio optimization dangerous and necessitating regime-aware allocation frameworks that account for correlation breakdown during tail events.

---

## The Core Insight


**The fundamental idea:**

- Crypto correlation with equities: Near-zero historically, 0.6-0.8 during stress
- "Digital gold" narrative: Partially valid, but fails in tail events
- Correlation is time-varying: Different in bull vs bear vs crisis
- Diversification benefits: Real in normal times, vanish when needed most
- Bitcoin vs Ethereum: Different correlation profiles (ETH more equity-like)
- Regime dependence: Fed policy, risk sentiment drive correlation dynamics
- Portfolio implications: Cannot assume stable low correlation for allocation

<p align="center">
<img src="https://github.com/SungchulLee/img/blob/main/crypto_tradfi_correlation.png?raw=true" alt="crypto_tradfi_correlation" width="700">
</p>
**Figure 1:** Cryptocurrency-traditional asset correlations showing rolling 90-day correlation between BTC and S&P 500, gold, and bonds from 2017-2024, highlighting regime changes, correlation breakdown during stress periods (March 2020, May 2021, November 2022), and structural shifts following institutional adoption.

**You're essentially asking: "Does crypto actually provide diversification, and when does it fail?"**

---

## Historical Correlation Analysis


### 1. BTC-Equity Correlation Evolution


**Pre-2020 (Early Era):**

| Period | BTC-SPX Correlation | Interpretation |
|--------|---------------------|----------------|
| 2014-2016 | -0.05 to +0.15 | Near-zero, independent |
| 2017-2019 | 0.00 to +0.20 | Low positive, retail-driven |

**Key characteristic:** Bitcoin traded on crypto-specific factors (halving, adoption news, exchange launches).

**2020-2024 (Institutional Era):**

| Period | BTC-SPX Correlation | Driver |
|--------|---------------------|--------|
| Jan-Feb 2020 | 0.10 | Pre-COVID normal |
| Mar 2020 (COVID) | **0.70** | Risk-off crash |
| Apr-Dec 2020 | 0.35 | Recovery, institutional entry |
| 2021 Bull | 0.40-0.50 | Macro-driven, Fed liquidity |
| Jan-Jun 2022 | **0.65-0.75** | Fed tightening, risk-off |
| Jul-Dec 2022 | 0.55 | Crypto-specific (FTX) |
| 2023-2024 | 0.45-0.55 | New equilibrium |

**Formula for rolling correlation:**

$$
\rho_{t}^{(n)} = \frac{\text{Cov}(r_{BTC,t-n:t}, r_{SPX,t-n:t})}{\sigma_{BTC} \cdot \sigma_{SPX}}
$$

Where $n$ = lookback window (typically 90 days).


### 2. The March 2020 Correlation Spike


**Event:** COVID-19 market crash

**Timeline:**

- Feb 19, 2020: S&P 500 peak (3,386)
- Mar 23, 2020: S&P 500 bottom (2,237) — **-34%**
- Feb 13, 2020: BTC peak ($10,500)
- Mar 12, 2020: BTC bottom ($3,800) — **-63%**

**Correlation:**

Pre-crash (Jan-Feb): ρ = 0.15
During crash (Mar): ρ = **0.72**
Post-crash (Apr-Jun): ρ = 0.40

**Interpretation:**

In liquidity crisis, everything correlated to 1.0:
- Forced selling across assets
- Margin calls liquidate everything
- Cash is only uncorrelated asset

**Formula for crisis correlation:**

$$
\rho_{\text{crisis}} \approx 1 - \frac{\text{Idiosyncratic Vol}}{\text{Systematic Vol}}
$$

When systematic risk dominates, all assets correlate.


### 3. Correlation by Asset Class


**90-day rolling correlations (2020-2024 average):**

| Asset Pair | Normal | Risk-Off | Risk-On |
|------------|--------|----------|---------|
| BTC - S&P 500 | 0.30 | 0.65 | 0.45 |
| BTC - Nasdaq | 0.35 | 0.70 | 0.50 |
| BTC - Gold | 0.15 | 0.30 | 0.10 |
| BTC - Bonds (AGG) | -0.10 | 0.20 | -0.15 |
| BTC - USD Index | -0.25 | -0.40 | -0.20 |
| ETH - S&P 500 | 0.40 | 0.72 | 0.55 |
| ETH - BTC | 0.85 | 0.90 | 0.80 |

**Key observations:**

1. **BTC-Gold:** Low correlation (0.15 average) supports "digital gold" somewhat, but increases to 0.30 in stress
2. **BTC-Bonds:** Negative correlation (good diversifier) but flips positive in crisis
3. **BTC-USD:** Consistently negative (BTC benefits from dollar weakness)
4. **ETH vs BTC:** ETH more correlated with equities (tech stock behavior)


### 4. ETH as "Tech Stock Proxy"


**Correlation comparison:**

| Period | ETH-Nasdaq | BTC-Nasdaq | Difference |
|--------|------------|------------|------------|
| 2021 Bull | 0.55 | 0.45 | ETH +0.10 |
| 2022 Bear | 0.75 | 0.65 | ETH +0.10 |
| 2023 | 0.60 | 0.50 | ETH +0.10 |

**Interpretation:**

ETH trades like leveraged tech:
- Higher beta to risk assets
- Stronger in liquidity-driven rallies
- Worse in rate-hiking environments

**ETH-specific factors:**

- DeFi activity (TVL correlation)
- Gas fee revenue (usage-based valuation)
- Staking yield (competes with real rates)

$$
\text{ETH Correlation} = 0.8 \times \text{BTC Correlation} + 0.2 \times \text{Tech Factor}
$$

---

## Regime-Based Correlation Analysis


### 1. Defining Market Regimes


**Risk-on regime:**
- VIX < 20
- Credit spreads tight
- Positive equity momentum
- Correlation: Lower (0.30-0.40)

**Risk-off regime:**
- VIX > 25
- Credit spreads widening
- Negative equity momentum
- Correlation: Higher (0.55-0.75)

**Crisis regime:**
- VIX > 40
- Liquidity crisis
- Forced deleveraging
- Correlation: Extreme (0.70-0.90)

**Regime detection:**

$$
\text{Regime} = \begin{cases}
\text{Risk-On} & \text{if VIX} < 20 \text{ and SPX trend} > 0 \\
\text{Risk-Off} & \text{if VIX} \in [20, 40] \text{ or SPX trend} < 0 \\
\text{Crisis} & \text{if VIX} > 40
\end{cases}
$$


### 2. Correlation Conditional on Regime


**Historical statistics (2020-2024):**

| Regime | Days | BTC-SPX ρ | BTC Vol | SPX Vol |
|--------|------|-----------|---------|---------|
| Risk-On | 650 | 0.32 | 55% | 12% |
| Risk-Off | 400 | 0.58 | 75% | 20% |
| Crisis | 50 | 0.74 | 120% | 35% |

**Implication:**

Diversification works 65% of time (Risk-On days) but fails when needed most (Crisis days).


### 3. Correlation Asymmetry


**Down-market vs up-market correlation:**

$$
\rho^- = \text{Corr}(r_{BTC}, r_{SPX} | r_{SPX} < 0)
$$

$$
\rho^+ = \text{Corr}(r_{BTC}, r_{SPX} | r_{SPX} > 0)
$$

**Empirical results (2020-2024):**

| Condition | ρ^+ (up days) | ρ^- (down days) |
|-----------|---------------|-----------------|
| BTC-SPX | 0.25 | **0.52** |
| ETH-SPX | 0.35 | **0.62** |

**"Correlation goes to 1 when you need it most"**

On down days, correlation doubles—diversification evaporates.

---

## The "Digital Gold" Analysis


### 1. BTC vs Gold Properties


**Gold as safe haven:**
- Negative equity correlation in stress
- Inflation hedge (long-term)
- No yield (opportunity cost)
- Physical scarcity

**BTC proponents argue:**
- Fixed supply (21M cap)
- Non-sovereign (no government control)
- Portable (digital)
- Divisible

**Empirical comparison:**

| Crisis Event | Gold Return | BTC Return | Correlation |
|--------------|-------------|------------|-------------|
| COVID Mar 2020 | -5% | -50% | +0.72 |
| Ukraine Feb 2022 | +7% | -8% | -0.15 |
| SVB Mar 2023 | +8% | +30% | +0.45 |

**Observation:** BTC fails as safe haven in liquidity crises, works in banking crises.


### 2. When BTC Acts Like Gold


**Conditions for low/negative correlation:**

1. **Dollar weakness:** BTC-USD correlation = -0.25 (similar to gold)
2. **Banking stress:** BTC gains during bank failures (SVB: +30%)
3. **Slow grind volatility:** Normal market, BTC independent

**Conditions for high correlation:**

1. **Liquidity crisis:** Forced selling, margin calls
2. **Fed tightening:** Risk assets correlated
3. **Extreme VIX:** All correlations → 1


### 3. Correlation with Inflation


**BTC as inflation hedge:**

| Period | Inflation | BTC Return | Real Return |
|--------|-----------|------------|-------------|
| 2020 | 1.2% | +300% | +299% |
| 2021 | 7.0% | +60% | +53% |
| 2022 | 6.5% | -65% | -71.5% |
| 2023 | 3.4% | +155% | +152% |

**Interpretation:**

BTC not reliably correlated with inflation:
- Returns driven by liquidity, adoption, halving cycles
- 2022: High inflation + Fed tightening = BTC crash
- Not a stable inflation hedge (unlike TIPS)

---

## Portfolio Implications


### 1. Naive Optimization Fails


**Mean-variance optimization assumes stable correlation:**

$$
\sigma_p^2 = w_{BTC}^2 \sigma_{BTC}^2 + w_{SPX}^2 \sigma_{SPX}^2 + 2 w_{BTC} w_{SPX} \rho \sigma_{BTC} \sigma_{SPX}
$$

**Problem:** Using average correlation (ρ = 0.40) underestimates tail risk.


**Scenario analysis:**

| Scenario | ρ Used | Actual ρ | Estimated Vol | Actual Vol |
|----------|--------|----------|---------------|------------|
| Normal | 0.40 | 0.40 | 15% | 15% |
| Crisis | 0.40 | 0.75 | 15% | **22%** |

Using normal-period correlation in crisis underestimates portfolio risk by 50%.


### 2. Regime-Aware Allocation


**Dynamic correlation model:**

$$
\rho_t = \rho_{\text{base}} + \beta_{\text{VIX}} \times (\text{VIX}_t - 20) + \beta_{\text{trend}} \times \text{SPX Trend}
$$

**Calibrated:**
- ρ_base = 0.30
- β_VIX = 0.015 (each VIX point adds 1.5% to correlation)
- β_trend = -0.10 (negative trend increases correlation)

**Example:**

VIX = 35, SPX trend = -5%:

$$
\rho = 0.30 + 0.015 \times 15 + (-0.10) \times (-0.05) = 0.30 + 0.225 + 0.005 = 0.53
$$


### 3. Recommended Allocation Framework


**Conservative (assumes crisis correlation):**

Use ρ = 0.70 for sizing (worst-case)

**Result:** Lower BTC allocation (2-5% of portfolio)

**Moderate (regime-aware):**

$$
w_{BTC} = \begin{cases}
10\% & \text{VIX} < 20 \\
5\% & \text{VIX} \in [20, 30] \\
2\% & \text{VIX} > 30
\end{cases}
$$

**Dynamic (volatility targeting):**

$$
w_{BTC} = \frac{\text{Target Vol Contribution}}{\sigma_{BTC} \times \sqrt{1 + \rho \times w_{SPX}/w_{BTC}}}
$$

Reduce allocation when correlation or volatility spikes.

---

## Empirical Case Studies


### 1. 2022: Perfect Storm of Correlation


**Setup:**
- Fed pivot from QE to QT
- Rising rates (0% → 5%)
- Risk-off across all assets

**Correlations (2022):**

| Pair | Q1 | Q2 | Q3 | Q4 |
|------|----|----|----|----|
| BTC-SPX | 0.65 | 0.72 | 0.58 | 0.52 |
| BTC-Nasdaq | 0.70 | 0.78 | 0.65 | 0.55 |

**Returns:**
- BTC: -65%
- SPX: -19%
- Nasdaq: -33%

**Lesson:** In Fed tightening, crypto = leveraged risk asset.


### 2. March 2023: Banking Crisis Decoupling


**Setup:**
- SVB collapse
- Regional bank stress
- Flight to safety

**Correlations (Mar 2023):**

| Pair | Pre-SVB | During Crisis | Post |
|------|---------|---------------|------|
| BTC-SPX | 0.48 | 0.25 | 0.42 |
| BTC-Gold | 0.15 | 0.45 | 0.20 |

**Returns (Mar 2023):**
- BTC: +30%
- Gold: +8%
- SPX: -2%
- Regional Banks: -30%

**Lesson:** BTC can decouple in banking crises (self-custody narrative).


### 3. 2024 ETF Approval: Structural Shift


**Setup:**
- Bitcoin spot ETF approved (Jan 2024)
- Institutional access simplified
- Correlation implications

**Pre-ETF (2023):** ρ(BTC, SPX) = 0.48
**Post-ETF (2024):** ρ(BTC, SPX) = 0.55

**Interpretation:**

ETF inflows = More correlated with equity sentiment:
- Same investors buying both
- Risk-on/off flows more synchronized
- Diversification benefit reduced

---

## Practical Recommendations


### 1. For Portfolio Construction


**Do:**
- Use crisis correlation (0.65-0.75) for stress testing
- Implement dynamic allocation based on VIX
- Size positions assuming diversification fails in tails
- Consider BTC and ETH separately (different profiles)

**Don't:**
- Assume stable low correlation
- Use full historical sample for optimization
- Treat crypto as pure diversifier
- Ignore regime changes


### 2. Correlation Monitoring Protocol


**Weekly:**
- Calculate 30-day rolling correlation
- Compare to 90-day and 180-day
- Note divergences

**Daily (risk management):**
- Monitor VIX
- If VIX > 25: Assume higher correlation
- If VIX > 35: Reduce crypto allocation

**Trigger-based:**
- If 30-day ρ > 0.60: Reassess allocation
- If BTC-SPX both down >3% same day: Crisis mode


### 3. Hedging Considerations


**When correlation high:**
- Crypto positions = equity risk amplifier
- Consider reducing, not hedging (expensive)

**When correlation low:**
- True diversification benefit
- Can maintain or increase allocation

**Put options (SPX):**
- Provide protection across correlated assets
- SPX puts hedge both equity and crypto tail risk (when correlated)

---

## Final Wisdom


> "The cruel irony of cryptocurrency as a diversifier is that it works exactly backward from what you want—in calm markets when diversification matters least, Bitcoin shows low correlation to equities (0.30-0.40), supporting the 'digital gold' thesis, but in crisis when diversification matters most, correlation spikes to 0.65-0.80, turning your 'hedge' into an amplifier of losses. March 2020 proved this devastatingly: BTC dropped 63% in the same week equities crashed 34%, correlation hitting 0.72, as margin calls forced liquidation of everything liquid, and crypto was the most liquid asset to sell. The mechanism is simple—in liquidity crises, all correlations go to 1 because forced sellers don't care about fundamental value, they need cash, and the most liquid assets get sold first. Bitcoin's 24/7 liquidity, perversely, makes it the first thing sold on a Friday afternoon when equity markets are closed. The 2022 Fed tightening cycle confirmed this wasn't a one-time anomaly: BTC-Nasdaq correlation held 0.65-0.78 throughout the year as rising rates crushed all risk assets together, with BTC's -65% outpacing Nasdaq's -33% with its characteristic high-beta behavior. Yet there are nuances: the March 2023 banking crisis showed BTC can decouple when the threat is specifically to traditional finance—SVB's collapse sent BTC up 30% while banks crashed, as 'be your own bank' suddenly resonated. The practical implication: don't count on diversification for crisis protection (use options, cash instead), but do capture the real diversification benefit during the 65% of time markets are calm. Regime-aware allocation is essential: 10% crypto allocation in low-VIX environment, 5% when VIX elevated, 2% in crisis, dynamically adjusting as conditions change. The ETF era likely increases correlation permanently as the same institutions now trade both—correlation has structurally risen from 0.35 (pre-2020) to 0.50 (2024), and this is the new normal. For portfolio construction, the conservative approach uses crisis correlation (0.70) for all sizing and stress testing, accepting lower expected returns for more honest risk assessment. The bottom line: crypto provides diversification when you don't need it and correlation when you do—build your portfolio accordingly."

**Key to success:**

- Use crisis correlation (0.65-0.75) for position sizing, not average
- Implement regime-aware allocation (reduce when VIX > 25)
- Monitor 30-day rolling correlation weekly
- Treat ETH as leveraged tech, BTC as volatile gold
- Don't rely on crypto for tail hedging (it correlates in tails)
- Consider put options on SPX for portfolio protection (hedges both)
- Accept that ETF era means structurally higher correlation (new equilibrium ~0.50)
- Diversification benefit is real 65% of time—capture it, but don't count on it in crisis
