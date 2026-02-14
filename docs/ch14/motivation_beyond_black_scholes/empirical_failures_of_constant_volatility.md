# Empirical Failures of Constant Volatility

The Black–Scholes model assumes that volatility is constant over time and across states of the market. While this assumption leads to analytical tractability, it is fundamentally inconsistent with observed market behavior. This section documents the empirical evidence against constant volatility and its implications for option pricing.

---

## The Constant Volatility Assumption

In the Black–Scholes framework, the underlying asset follows geometric Brownian motion:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t,
$$

where the volatility parameter $\sigma$ is constant. This implies several testable predictions:

1. **Normality of log-returns:** $\log(S_{t+\Delta}/S_t) \sim \mathcal{N}\bigl((\mu - \tfrac{1}{2}\sigma^2)\Delta, \sigma^2\Delta\bigr)$
2. **Linear variance scaling:** $\text{Var}[\log S_T] = \sigma^2 T$
3. **Independence of increments:** returns over non-overlapping periods are independent
4. **Single implied volatility:** all options on the same underlying share one $\sigma$

Each of these predictions fails empirically.

---

## Volatility Clustering

One of the most robust findings in financial econometrics is **volatility clustering**: large price changes tend to be followed by large price changes (of either sign), and small changes by small changes.

Formally, while returns $r_t$ are approximately uncorrelated:

$$
\text{Corr}(r_t, r_{t+k}) \approx 0 \quad \text{for } k \geq 1,
$$

squared returns exhibit significant positive autocorrelation:

$$
\text{Corr}(r_t^2, r_{t+k}^2) > 0 \quad \text{for } k = 1, 2, \ldots, 50+.
$$

**Quantitative evidence:**

| Asset Class | Autocorrelation of $r_t^2$ at lag 1 | Decay half-life |
|-------------|-------------------------------------|-----------------|
| S&P 500 | 0.15–0.25 | 20–40 days |
| Individual equities | 0.10–0.20 | 10–30 days |
| FX majors | 0.10–0.15 | 15–25 days |

This persistence implies that volatility is **predictable**, contradicting the constant-$\sigma$ assumption.

The ARCH/GARCH literature (Engle 1982, Bollerslev 1986) formalizes this by modeling conditional variance as:

$$
\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2,
$$

where typically $\alpha + \beta \approx 0.95$–$0.99$, indicating high persistence.

---

## The Leverage Effect

The **leverage effect** refers to the negative correlation between returns and subsequent volatility changes: when prices fall, volatility tends to rise.

Let $r_t$ denote the return and $\sigma_{t+1}$ the subsequent volatility. Empirically:

$$
\text{Corr}(r_t, \sigma_{t+1}^2 - \sigma_t^2) < 0.
$$

**Typical magnitudes:**

| Market | Correlation estimate |
|--------|---------------------|
| S&P 500 | $-0.4$ to $-0.7$ |
| Individual stocks | $-0.2$ to $-0.5$ |
| FX | Near zero |
| Commodities | Mixed |

**Economic interpretations:**

1. **Balance sheet effects:** A price decline increases leverage (debt/equity ratio), making the firm riskier.

2. **Risk premium channel:** Negative returns signal deteriorating economic conditions, increasing risk premia.

3. **Behavioral effects:** Investors react asymmetrically to losses versus gains.

The leverage effect has profound implications for option pricing: it generates the characteristic **negative skew** in implied volatility surfaces for equity indices.

---

## Time-Varying Realized Volatility

Realized volatility, estimated from high-frequency data, varies substantially over time:

$$
RV_t = \sqrt{\sum_{i=1}^{n} r_{t,i}^2}
$$

where $r_{t,i}$ are intraday returns.

**Historical ranges for S&P 500 annualized volatility:**

| Period | Volatility range |
|--------|------------------|
| Calm markets (2017) | 6%–10% |
| Normal conditions | 12%–20% |
| Stressed markets (2008, 2020) | 40%–80%+ |

The ratio between high and low volatility regimes exceeds 5:1, making constant volatility untenable.

**Volatility of volatility:** The standard deviation of realized volatility is itself substantial. For the S&P 500:

$$
\text{Std}[\sigma_{\text{realized}}] \approx 0.4 \times \mathbb{E}[\sigma_{\text{realized}}],
$$

implying a coefficient of variation around 40%.

---

## Distributional Failures

Under constant volatility, log-returns are Gaussian. Empirically, returns exhibit systematic departures:

### Heavy Tails (Leptokurtosis)

The kurtosis of a Gaussian is 3. Empirical return distributions have excess kurtosis:

$$
\text{Kurt}[r] = \frac{\mathbb{E}[(r - \mu)^4]}{(\mathbb{E}[(r-\mu)^2])^2} > 3.
$$

**Typical values:**

| Frequency | Kurtosis |
|-----------|----------|
| Daily | 5–10 |
| Weekly | 4–6 |
| Monthly | 3.5–5 |

The aggregational Gaussianity (kurtosis approaching 3 at longer horizons) is consistent with stochastic volatility: conditional normality with random variance produces unconditional heavy tails.

### Negative Skewness

Equity returns, especially for indices, exhibit negative skewness:

$$
\text{Skew}[r] = \frac{\mathbb{E}[(r - \mu)^3]}{(\mathbb{E}[(r-\mu)^2])^{3/2}} < 0.
$$

**Typical values for equity indices:** $-0.3$ to $-1.0$

This reflects the leverage effect and the occasional occurrence of market crashes.

### Extreme Events

The probability of extreme returns far exceeds Gaussian predictions:

| Event | Gaussian probability | Empirical frequency |
|-------|---------------------|---------------------|
| 3$\sigma$ daily move | 0.27% | 1%–2% |
| 5$\sigma$ daily move | 0.00006% | 0.1%–0.5% |
| 10$\sigma$ daily move | $\approx 0$ | Has occurred |

The 1987 crash ($-22.6\%$ in one day, $\approx 20\sigma$) and 2020 COVID shock illustrate that extreme events are not "tail events" under realistic distributions.

---

## Implications for Option Pricing

The distributional failures translate directly into option pricing anomalies:

### Systematic Mispricing of OTM Options

Under Black–Scholes with constant $\sigma$:
- OTM puts are underpriced (true distribution has heavier left tail)
- OTM calls may be overpriced or underpriced depending on the asset

### The Volatility Smile

If Black–Scholes held with constant $\sigma$, implied volatility would be flat across strikes. Instead:

$$
\sigma_{\text{impl}}(K) \neq \text{constant}.
$$

The pattern—higher implied volatility for OTM puts (low strikes) and sometimes OTM calls (high strikes)—reflects the market's recognition of non-Gaussian risks.

### Hedging Failures

Delta hedging under constant volatility assumes:

$$
\Delta = \frac{\partial C}{\partial S} = N(d_1)
$$

with known, stable $\sigma$. When volatility is stochastic:
- Delta itself becomes random
- Hedging P&L has non-zero variance even with continuous rebalancing
- Volatility exposure (vega risk) cannot be hedged by the underlying alone

---

## Quantitative Summary

| Stylized Fact | Black–Scholes Prediction | Empirical Reality |
|---------------|-------------------------|-------------------|
| Return distribution | Gaussian | Heavy-tailed, skewed |
| Kurtosis | 3 | 5–10 (daily) |
| Skewness | 0 | $-0.3$ to $-1.0$ |
| Volatility | Constant | Time-varying, clustered |
| Return-vol correlation | 0 | $-0.4$ to $-0.7$ (equity) |
| Implied volatility | Flat | Smile/skew |

---

## Key Takeaways

- Constant volatility is empirically invalid across all asset classes
- Volatility is stochastic, persistent, and exhibits the leverage effect
- Return distributions have heavy tails and (for equities) negative skew
- These features cause systematic option mispricing under Black–Scholes
- Stochastic volatility models address these failures directly

---

## Empirical Evidence: QuantPie Analysis

The empirical failures of constant volatility can be directly demonstrated through computational analysis of historical stock data. This section presents concrete evidence from a rolling-window volatility analysis on Walmart (WMT) stock spanning from August 1972 to January 2022.

### Rolling Window Volatility Analysis

A 30-day rolling window standard deviation analysis reveals substantial time-variation in volatility:

```python
import yfinance as yf
import pandas as pd
import numpy as np

# Download historical data
ticker = 'WMT'
stock = yf.Ticker(ticker)
df = stock.history(period='max')

# Compute daily log-returns
df['Return'] = df['Close'].pct_change()

# 30-day rolling standard deviation
window = 30
df['Rolling_Vol_30d'] = df['Return'].rolling(window).std()
```

**Key findings:**

- The 30-day rolling standard deviation fluctuates dramatically over the 50-year period
- Volatility is **not constant**: same asset exhibits vastly different risk profiles across different time periods
- This time-variation in volatility directly contradicts the constant-$\sigma$ assumption of Black–Scholes

The rolling volatility exhibits clear clustering patterns, with periods of elevated volatility persisting over months to years, separated by calmer regimes.

### Leptokurtic Distribution: High Peak

When comparing the empirical distribution of daily returns to a fitted normal distribution, a striking feature emerges: **excess concentration near zero returns**.

The histogram of returns shows a much higher peak (narrower center) than the normal distribution fit:

$$\text{Actual return density at } r = 0 \gg \text{Normal}(0, \sigma) \text{ density}$$

This **leptokurtic** or high-peak property reflects:

1. **Small daily moves are very common:** Markets experience many "normal" trading days
2. **Wider extreme tails:** The probability mass that should be in the tails under normality is concentrated in the center, leaving heavier tails

**Quantitative evidence (WMT, 1972–2022):**

$$\text{Excess Kurtosis} = \text{Kurt}[\text{Returns}] - 3 > 0 \quad (\text{typical: 2–7 for daily data})$$

The excess kurtosis demonstrates that returns are **not normal**: the distribution is too "peaky" and has too-heavy tails.

### Fat Tails: Excess Probability of Extreme Events

When examining returns in the extreme tails (beyond $\pm 3\sigma$ from the mean), empirical frequencies vastly exceed normal distribution predictions.

**Fat right tail** (large positive returns):
- Empirical observation: significant density in returns $r > 3\sigma$
- Normal prediction: negligible probability (0.27% per day)
- Gap: An order of magnitude difference in extreme positive moves

**Fat left tail** (large negative returns):
- Empirical observation: pronounced density in returns $r < -3\sigma$
- Normal prediction: exponentially small probability
- Gap: The left tail is even fatter than the right, reflecting downside risk concentration

**Comparison to Normal PDF:**

For bins in the extreme tails:

$$\frac{n_{\text{empirical}}(r > 3\sigma)}{y_{\text{normal}}(r > 3\sigma)} \gg 1$$

where $n$ denotes observed frequency density and $y$ denotes the normal probability density function.

The empirical tail frequencies are orders of magnitude larger than the normal model predicts, meaning:

- Crashes and rallies are far more probable than Gaussian assumptions suggest
- Option pricing models must account for this tail risk
- Risk management assuming normality underestimates downside exposure

### Summary of Distributional Failures

| Property | Black–Scholes Assumption | Empirical Observation |
|----------|--------------------------|----------------------|
| Volatility | Constant across time | 30-day vol: 0.5%–5%+ per day |
| Kurtosis | 3 (normal) | 5–10 (daily data) |
| Peak shape | Normal bell curve | **Higher peak** (leptokurtic) |
| Tail probability at $3\sigma$ | 0.27% | 1%–2% |
| Tail probability at $5\sigma$ | 0.00006% | 0.1%–0.5% |

### Practical Implications

These empirical findings have direct consequences:

1. **Option pricing:** Constant-volatility models systematically misprice tail risk, undervaluing OTM puts and calls

2. **Risk management:** Value-at-Risk (VaR) calculations assuming normality underestimate tail risk, leading to insufficient capital buffers

3. **Hedging:** Delta hedging with constant volatility incurs significant P&L variance during periods of rising volatility

4. **Model requirements:** Successful models must incorporate:
   - Time-varying (stochastic) volatility
   - Mean-reverting or jump components to capture tail risk
   - Non-normal conditional distributions

---

## Further Reading

- Mandelbrot, B. (1963). *The variation of certain speculative prices*. Journal of Business.
- Engle, R. (1982). *Autoregressive conditional heteroskedasticity*. Econometrica.
- Bollerslev, T. (1986). *Generalized autoregressive conditional heteroskedasticity*. Journal of Econometrics.
- Cont, R. (2001). *Empirical properties of asset returns: stylized facts and statistical issues*. Quantitative Finance.
- Black, F. (1976). *Studies of stock price volatility changes*. Proceedings of the Business and Economics Section, ASA.
