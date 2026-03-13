# Empirical Stylized Facts of Smile Dynamics


## Introduction


Empirical studies of implied volatility dynamics reveal robust **stylized facts** that any realistic model should aim to reproduce. These patterns are observed across asset classes and time periods, providing essential benchmarks for model validation and development.

This section documents the key empirical regularities in smile dynamics, their quantitative characteristics, and implications for modeling.

## Skew Dynamics


### 1. Leverage Effect


**Definition:** The tendency for implied volatility to increase when spot prices decrease.

**Quantitative relationship:**

$$
\Delta \sigma_{\text{ATM}} \approx \beta \cdot \frac{\Delta S}{S}
$$


where $\beta < 0$ (typically $\beta \approx -1.5$ to $-2.5$ for equity indices).

**Empirical evidence:**
- S&P 500: $\beta \approx -2.0$ (1990-2020 average)
- EURO STOXX 50: $\beta \approx -1.8$
- Individual stocks: More variable, $\beta \approx -1.0$ to $-2.5$

**Asymmetry:**

$$
|\beta_{\text{down}}| > |\beta_{\text{up}}|
$$


The vol response is stronger for down moves than up moves.

### 2. Skew Steepening After Crashes


**Observation:** After large negative returns, the implied volatility skew steepens significantly.

**Mechanism:**
- OTM put demand increases (hedging, panic)
- Risk-neutral left tail becomes fatter
- Market prices higher crash probability

**Quantitative measure:**

$$
\text{Skew}_{25\Delta} = \sigma_{\text{25DP}} - \sigma_{\text{ATM}}
$$


**Post-crash behavior:**
- Normal regime: Skew $\approx$ 5-8 vol points
- Post-crash: Skew $\approx$ 15-25 vol points
- Decay time: 1-3 months

### 3. Skew Mean Reversion


**Observation:** Elevated skew reverts to long-run average.

**Half-life:** Approximately 1-2 months for equity indices.

**Model implications:** Models should incorporate:
- Skew dynamics correlated with vol level
- Mean reversion in skew
- Asymmetric response to up/down moves

## Term Structure Behavior


### 1. Short-Term Vol Response


**Observation:** Short-dated implied volatility responds more strongly to spot moves than long-dated vol.

**Quantitative relationship:**

$$
|\beta(T_{\text{short}})| > |\beta(T_{\text{long}})|
$$


**Example (SPX):**
- 1-month vol: $\beta \approx -2.5$
- 1-year vol: $\beta \approx -1.5$

**Implication:** Term structure flattens or inverts during stress.

### 2. Term Structure Inversion


**Observation:** During market stress, the term structure inverts (short > long).

**Frequency:** Approximately 15-20% of the time for SPX since 1990.

**Triggers:**
- Large spot declines (> 3% daily)
- VIX spikes (> 30)
- Crisis events

**Resolution:** Term structure normalizes within 1-4 weeks typically.

### 3. Volatility Propagation


**Observation:** Volatility shocks propagate gradually across maturities.

**Mechanism:**
- Impact short maturities first
- Slowly affects longer maturities
- Long-end acts as "anchor"

**Time scale:** Full propagation takes 1-2 weeks.

## Persistence and Mean Reversion


### 1. Volatility Persistence


**Observation:** Implied volatility exhibits strong persistence (high autocorrelation).

**Quantitative measure:**

$$
\text{ACF}(\sigma_{\text{ATM}}, \text{lag } k) = \rho^k
$$


where $\rho \approx 0.95$ for daily data.

**Half-life:** Approximately 2-4 weeks for ATM vol.

### 2. Mean Reversion


**Observation:** Implied volatility reverts to a long-run level.

**Long-run levels (approximate):**

| Asset | Long-run ATM Vol |
|-------|------------------|
| SPX | 15-18% |
| EURO STOXX | 18-22% |
| EUR/USD | 8-10% |
| Gold | 14-16% |

**Mean reversion speed:** Varies by asset and regime:
- Normal times: Slow (half-life 1-2 months)
- Post-spike: Faster (half-life 1-2 weeks)

### 3. Volatility Clustering


**Observation:** High volatility tends to follow high volatility, low follows low.

**GARCH-like behavior:**

$$
\sigma_{t+1}^2 \approx \omega + \alpha \epsilon_t^2 + \beta \sigma_t^2
$$


**Empirical fit:** $\alpha + \beta \approx 0.99$ for equity indices.

**Implication:** Stochastic volatility models needed, not constant vol.

## Cross-Asset Patterns


### 1. Equity Indices


**Characteristics:**
- Strong negative skew (crashophobia)
- Leverage effect pronounced
- Term structure usually upward sloping
- Skew steeper for shorter maturities

**Typical values (SPX):**

| Measure | Normal | Stress |
|---------|--------|--------|
| ATM Vol | 12-18% | 25-50%+ |
| 25D Skew | 4-8% | 12-25% |
| Term Slope | +2-4% | -5-15% |

### 2. FX Markets


**Characteristics:**
- Smile more symmetric (smirk less pronounced)
- Risk reversals vary by currency pair
- Closer to sticky delta than equities

**G10 currencies (EUR/USD):**
- ATM vol: 6-10% typically
- Risk reversal: Near zero (slight puts over calls)
- Smile (butterfly): 0.3-1.0%

**EM currencies:**
- Higher overall vol
- More pronounced skew (downside for EM currency)
- Event risk (elections, crises)

### 3. Commodities


**Energy (Crude Oil):**
- Positive skew common (upside tail)
- Seasonal effects in term structure
- Event risk (OPEC, geopolitics)

**Precious Metals (Gold):**
- Modest negative skew
- Flight-to-quality during stress
- Vol correlated with equity stress

### 4. Interest Rates


**Characteristics:**
- Smile around ATM (both tails priced)
- Term structure tied to rate expectations
- Vol depends on rate level (lower rates → lower vol)

## Quantitative Measures


### 1. Skew Stickiness Ratio (SSR)


**Definition:**

$$
\text{SSR} = \frac{\Delta \sigma_{\text{ATM}}}{\Delta \sigma_{\text{ATM}}^{\text{sticky-strike}}}
$$


where the denominator is the ATM vol change predicted by sticky strike.

**Interpretation:**
- SSR = 0: Pure sticky strike
- SSR = 1: Pure sticky delta/moneyness
- SSR = 0.3-0.6: Typical empirical range

### 2. Spot-Vol Correlation


**Definition:**

$$
\rho_{S,\sigma} = \text{Corr}(\Delta \log S, \Delta \sigma_{\text{ATM}})
$$


**Empirical values:**

| Asset | $\rho_{S,\sigma}$ |
|-------|-------------------|
| SPX | -0.70 to -0.80 |
| EURO STOXX | -0.65 to -0.75 |
| EUR/USD | -0.10 to +0.10 |
| Gold | -0.20 to -0.40 |

### 3. Vol-of-Vol


**Definition:** The volatility of ATM implied volatility.

$$
\text{Vol-of-Vol} = \text{Std}(\Delta \sigma_{\text{ATM}}) \cdot \sqrt{252}
$$


**Empirical values:**
- SPX: 3-5% (annualized)
- Higher during stress periods

### 4. Skew-Spot Beta


**Definition:**

$$
\beta_{\text{skew}} = \frac{d(\text{Skew})}{d(\log S)}
$$


**Empirical values:**
- SPX: -0.3 to -0.5
- Skew steepens approximately 0.3-0.5 vol points per 1% spot decline

## Time Scales


### 1. Summary of Time Scales


| Effect | Time Scale |
|--------|------------|
| Spot-vol correlation | Intraday to daily |
| Immediate vol response | Intraday |
| Vol mean reversion | Days to weeks |
| Skew normalization | Weeks to months |
| Term structure normalization | Weeks to months |
| Long-run vol estimation | Months to years |

### 2. Event-Driven Dynamics


**Pre-event:**
- Term structure humps at event maturity
- Vol elevated for event-spanning options

**Post-event:**
- Vol crush if event resolves uncertainty
- Vol spike if event creates uncertainty
- Skew adjusts to new information

## Implications for Modeling


### 1. Model Requirements


A good model should capture:

| Stylized Fact | Model Feature |
|---------------|---------------|
| Leverage effect | Negative spot-vol correlation ($\rho < 0$) |
| Skew persistence | Stochastic volatility |
| Vol clustering | Mean-reverting variance |
| Term structure | Multi-factor or time-dependent parameters |
| Vol-of-vol | Non-trivial $\xi$ parameter |

### 2. Model Comparison


| Model | Leverage | Persistence | Clustering | Term Structure |
|-------|----------|-------------|------------|----------------|
| Black-Scholes | ✗ | ✗ | ✗ | ✗ |
| Local Vol | ✓ (via calibration) | ✗ | ✗ | ✓ |
| Heston | ✓ | ✓ | ✓ | Partial |
| SABR | ✓ | ✓ | ✓ | Partial |
| Bergomi | ✓ | ✓ | ✓ | ✓ |

### 3. Calibration Guidance


**Parameters from stylized facts:**

- $\rho$: From spot-vol correlation (-0.7 for SPX)
- $\kappa$: From vol persistence (half-life 2-4 weeks)
- $\xi$: From vol-of-vol (match VIX-of-VIX)
- $\theta$: From long-run vol level

## Summary


### Key Stylized Facts

1. **Leverage effect:** Vol increases when spot decreases ($\beta \approx -2$)
2. **Skew dynamics:** Steepens after crashes, mean-reverts over weeks
3. **Persistence:** High autocorrelation ($\rho \approx 0.95$)
4. **Mean reversion:** Vol returns to long-run level
5. **Term structure:** Short-end more reactive, inverts during stress
6. **Cross-asset:** Patterns vary but leverage effect common in equities

### Quantitative Benchmarks

| Measure | Typical Value (SPX) |
|---------|---------------------|
| Spot-vol correlation | -0.75 |
| Vol-of-vol | 4% (annualized) |
| Vol half-life | 2-3 weeks |
| SSR | 0.4-0.6 |
| Skew-spot beta | -0.4 |

### Model Validation

- Compare model-implied dynamics to stylized facts
- Check spot-vol correlation, vol-of-vol, persistence
- Validate forward smile behavior
- Test on out-of-sample stress periods

---

## Further Reading


- Cont, R. *Empirical Properties of Asset Returns: Stylized Facts and Statistical Issues*
- Gatheral, J. *The Volatility Surface*
- Bergomi, L. *Smile Dynamics* series
- Bouchaud, J.P. and Potters, M. *Theory of Financial Risk and Derivative Pricing*
