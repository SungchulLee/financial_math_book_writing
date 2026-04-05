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

---

## Exercises

**Exercise 1.** The leverage effect is quantified by $\Delta\sigma_{\text{ATM}} \approx \beta \cdot \frac{\Delta S}{S}$ with $\beta \approx -2.0$ for the S&P 500. If the SPX drops 4% in one day, estimate the change in ATM implied volatility. If ATM IV was 16% before the move, what is the new ATM IV?

??? success "Solution to Exercise 1"
    Using the leverage effect relationship $\Delta\sigma_{\text{ATM}} \approx \beta \cdot \frac{\Delta S}{S}$ with $\beta = -2.0$:

    $$
    \Delta\sigma_{\text{ATM}} \approx (-2.0) \times (-0.04) = 0.08 = 8\%
    $$

    So ATM implied volatility increases by approximately 8 percentage points. Starting from $\sigma_{\text{ATM}} = 16\%$:

    $$
    \sigma_{\text{ATM}}^{\text{new}} = 16\% + 8\% = 24\%
    $$

    The new ATM IV is approximately 24%. This is consistent with empirical observations: a 4% daily decline in SPX (a large but not extreme move) roughly pushes vol from a calm regime into an elevated regime. Note that this linear approximation may overestimate the effect for very large moves, as the relationship is only approximately linear.

---

**Exercise 2.** The asymmetry $|\beta_{\text{down}}| > |\beta_{\text{up}}|$ means volatility responds more strongly to down moves than up moves. Propose a simple piecewise-linear model for the spot-vol relationship: $\Delta\sigma = \beta_+ \frac{\Delta S}{S}$ for $\Delta S > 0$ and $\Delta\sigma = \beta_- \frac{\Delta S}{S}$ for $\Delta S < 0$ with $|\beta_-| > |\beta_+|$. Using $\beta_+ = -1.0$ and $\beta_- = -3.0$, compute $\Delta\sigma$ for (a) $\Delta S/S = +3\%$ and (b) $\Delta S/S = -3\%$.

??? success "Solution to Exercise 2"
    The piecewise-linear model is:

    $$
    \Delta\sigma =
    \begin{cases}
    \beta_+ \dfrac{\Delta S}{S} & \text{if } \Delta S > 0 \\[6pt]
    \beta_- \dfrac{\Delta S}{S} & \text{if } \Delta S < 0
    \end{cases}
    $$

    with $\beta_+ = -1.0$ and $\beta_- = -3.0$.

    **(a)** For $\Delta S / S = +3\%$:

    $$
    \Delta\sigma = (-1.0) \times 0.03 = -0.03 = -3\%
    $$

    ATM vol decreases by 3 percentage points when the spot rises 3%.

    **(b)** For $\Delta S / S = -3\%$:

    $$
    \Delta\sigma = (-3.0) \times (-0.03) = 0.09 = 9\%
    $$

    ATM vol increases by 9 percentage points when the spot drops 3%.

    The asymmetry is stark: a 3% down move produces a vol change three times larger than a 3% up move of the same magnitude. This captures the empirical observation that markets exhibit a much stronger volatility response to negative returns ("crashophobia"), driven by increased hedging demand for downside protection.

---

**Exercise 3.** Implied volatility exhibits mean reversion with a characteristic half-life of 2-4 weeks for equity indices. If the current ATM IV is 35% (elevated due to a crisis) and the long-run mean is 18%, use the mean-reversion model $\sigma(t) = \sigma_\infty + (\sigma_0 - \sigma_\infty)e^{-\lambda t}$ with half-life 3 weeks ($\lambda = \ln 2 / 3$ per week) to predict ATM IV in 1 week, 4 weeks, and 12 weeks.

??? success "Solution to Exercise 3"
    The mean-reversion model is $\sigma(t) = \sigma_\infty + (\sigma_0 - \sigma_\infty)e^{-\lambda t}$ with $\sigma_0 = 35\%$, $\sigma_\infty = 18\%$, and $\lambda = \ln 2 / 3 \approx 0.2310$ per week.

    **At $t = 1$ week:**

    $$
    \sigma(1) = 18 + (35 - 18)e^{-0.2310 \times 1} = 18 + 17 \times e^{-0.2310} = 18 + 17 \times 0.7937 \approx 31.49\%
    $$

    **At $t = 4$ weeks:**

    $$
    \sigma(4) = 18 + 17 \times e^{-0.2310 \times 4} = 18 + 17 \times e^{-0.9241} = 18 + 17 \times 0.3969 \approx 24.75\%
    $$

    **At $t = 12$ weeks:**

    $$
    \sigma(12) = 18 + 17 \times e^{-0.2310 \times 12} = 18 + 17 \times e^{-2.7726} = 18 + 17 \times 0.0625 \approx 19.06\%
    $$

    After 12 weeks (approximately 3 months), ATM IV has nearly reverted to its long-run level. The half-life of 3 weeks means that after 3 weeks, the excess vol above the mean ($17\%$) is halved to $8.5\%$, giving $\sigma(3) \approx 26.5\%$. After four half-lives (12 weeks), only $1/16$ of the excess remains.

---

**Exercise 4.** The skew-spot beta measures how the slope of the smile changes with spot: $\frac{d(\text{skew})}{d(\log S)} \approx -0.4$ for SPX. If the current 25-delta skew is 6 vol points and the spot drops 5%, estimate the new skew. What does this steepening mean for the price of OTM puts relative to ATM options?

??? success "Solution to Exercise 4"
    The skew-spot beta is $\frac{d(\text{skew})}{d(\log S)} \approx -0.4$. With a 5% spot decline, $\Delta \log S \approx -0.05$:

    $$
    \Delta(\text{skew}) \approx (-0.4) \times (-0.05) = +0.02 = +2 \text{ vol points}
    $$

    The new skew is:

    $$
    \text{Skew}_{\text{new}} = 6 + 2 = 8 \text{ vol points}
    $$

    **Economic interpretation of skew steepening:** A steeper skew means that OTM puts have become relatively more expensive compared to ATM options. Specifically:

    - The 25-delta put implied volatility has increased by more than the ATM vol.
    - The risk-neutral distribution has developed a fatter left tail, reflecting higher market-implied crash probability.
    - Protective put demand has increased as the market drops, bidding up downside protection.
    - Hedgers and portfolio insurers increase put buying during selloffs, reinforcing the skew steepening.

    For traders, this means that the cost of downside hedging via OTM puts rises disproportionately during market declines, a self-reinforcing dynamic.

---

**Exercise 5.** Term structure inversion is a hallmark of crisis periods. Describe the mechanism by which a sudden spike in short-term uncertainty (e.g., a flash crash) inverts the volatility term structure. Why does the long end of the term structure respond less dramatically than the short end?

??? success "Solution to Exercise 5"
    **Mechanism of term structure inversion:** Under normal conditions, the volatility term structure is upward sloping because longer-dated options incorporate more uncertainty. A sudden spike in short-term uncertainty (e.g., a flash crash) dramatically increases short-dated implied volatility while leaving long-dated vol relatively unchanged, inverting the term structure.

    The specific mechanism is:

    1. A flash crash causes an immediate spike in realized volatility and demand for short-dated hedging instruments.
    2. Short-dated options (1-week to 1-month) see their implied volatility surge as gamma hedging demand intensifies and market makers widen spreads.
    3. The VIX (which reflects roughly 30-day implied vol) spikes sharply.

    **Why the long end responds less:** Long-dated implied volatility is anchored by several factors:

    - **Mean reversion:** The market expects elevated volatility to revert over time, so the long-dated vol reflects the average expected vol over a long horizon, not the current spike.
    - **Structural sellers:** Pension funds and insurers systematically sell long-dated vol (e.g., covered call strategies), providing a dampening effect.
    - **Information content:** A flash crash is typically viewed as a short-lived liquidity event, not a permanent shift in fundamentals. Long-dated options price in the expectation that conditions will normalize.
    - **Variance convexity:** The long-dated total variance $w(T) = \sigma^2 T$ is a weighted average over the entire horizon. A brief spike in short-term vol has a diluted effect on the long-dated average.

    The inversion typically resolves within 1-4 weeks as short-term vol decays and the term structure re-steepens.

---

**Exercise 6.** The volatility smile exhibits "stickiness" that lies between sticky strike and sticky delta. The skew stickiness ratio (SSR) for SPX is approximately 0.4-0.6. Define the SSR and explain how it relates to the spot-vol beta $\beta$. If SSR = 0.5 and the smile skew is 20% per unit log-moneyness, compute the effective spot-vol sensitivity $\Sigma_S = \frac{\partial \sigma_{\text{IV}}}{\partial S}$ for $S = 100$.

??? success "Solution to Exercise 6"
    **Definition of the SSR:** The skew stickiness ratio is defined as:

    $$
    \text{SSR} = \frac{\Delta \sigma_{\text{ATM}}}{\Delta \sigma_{\text{ATM}}^{\text{sticky-strike}}}
    $$

    where $\Delta \sigma_{\text{ATM}}^{\text{sticky-strike}}$ is the ATM vol change that would occur under the sticky-strike assumption (i.e., the smile does not move, and the ATM vol changes only because the ATM point slides along the fixed smile).

    **Relationship to the spot-vol beta $\beta$:** Under sticky strike, the change in ATM vol when spot moves is determined entirely by the skew slope $s$:

    $$
    \Delta \sigma_{\text{ATM}}^{\text{sticky-strike}} = s \cdot \frac{\Delta S}{S}
    $$

    where $s = \frac{\partial \sigma}{\partial \log K}\big|_{K=S}$ is the skew slope (negative for equities). The actual ATM vol change is $\Delta \sigma_{\text{ATM}} = \beta \cdot \frac{\Delta S}{S}$. Therefore:

    $$
    \text{SSR} = \frac{\beta}{s}
    $$

    Since $\beta < 0$ and $s < 0$ for equities, $\text{SSR} > 0$. SSR = 0 means the smile is perfectly sticky-strike ($\beta = 0$, ATM vol does not move with spot beyond the slide effect). SSR = 1 means sticky-delta (the entire smile shifts with spot).

    **Computing $\Sigma_S$:** The smile skew in log-moneyness is $s = \frac{\partial \sigma}{\partial \log(K/S)} = -20\%$ per unit log-moneyness (negative because we express it as a slope in the strike direction). With SSR = 0.5:

    $$
    \beta = \text{SSR} \times s = 0.5 \times (-0.20) = -0.10
    $$

    The effective spot-vol sensitivity is:

    $$
    \Sigma_S = \frac{\partial \sigma_{\text{IV}}}{\partial S} = \frac{\beta}{S} = \frac{-0.10}{100} = -0.001
    $$

    This means that for each 1-point increase in the spot price (from $S = 100$), ATM implied volatility decreases by 0.1 percentage points (10 basis points of vol).

---

**Exercise 7.** List five key stylized facts of implied volatility dynamics for equity indices. For each, state (a) the qualitative observation, (b) a typical quantitative value, and (c) which model class (local vol, Heston, SABR, rough vol) best captures it. Identify which stylized fact is hardest for standard models to reproduce.

??? success "Solution to Exercise 7"
    | Stylized Fact | (a) Qualitative Observation | (b) Typical Value (SPX) | (c) Best Model Class |
    |---|---|---|---|
    | **Leverage effect** | Vol rises when spot falls; negative spot-vol correlation | $\beta \approx -2.0$; $\rho_{S,\sigma} \approx -0.75$ | Heston / SABR (via $\rho < 0$) |
    | **Volatility clustering** | Periods of high vol followed by high vol, and low by low | GARCH $\alpha + \beta \approx 0.99$ | Rough vol (long memory via $H < 0.5$) |
    | **Mean reversion** | Vol reverts to a long-run level after spikes | Half-life 2-3 weeks; long-run level 15-18% | Heston (via $\kappa$, $\theta$) |
    | **Skew persistence** | Forward smile maintains non-zero skew over time | 25-delta skew $\approx$ 5-8 vol points, persists months ahead | SABR / Bergomi |
    | **Term structure reactivity** | Short-dated vol responds more to spot shocks than long-dated vol | $\beta_{\text{1M}} \approx -2.5$; $\beta_{\text{1Y}} \approx -1.5$ | Rough vol / multi-factor stochastic vol |

    **Hardest stylized fact to reproduce:** Volatility clustering with the correct degree of long memory is the most challenging for standard models. Classical stochastic volatility models (Heston, SABR) generate exponential autocorrelation decay, while empirical vol exhibits power-law decay consistent with long memory. The rough volatility framework (with Hurst parameter $H \approx 0.1$) captures this long-memory behavior, but at the cost of losing the Markov property, complicating calibration and simulation. The simultaneous reproduction of both long memory and realistic forward smile dynamics remains an active area of research.
