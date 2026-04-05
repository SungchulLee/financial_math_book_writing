# Empirical Failures of Constant Volatility

The Black–Scholes model assumes that volatility is constant over time and across states of the market. While this assumption leads to analytical tractability, it is fundamentally inconsistent with observed market behavior. This section documents the empirical evidence against constant volatility and its implications for option pricing.

---

### The Constant Volatility Assumption

In the Black–Scholes framework, the underlying asset follows geometric Brownian motion:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t
$$

where the volatility parameter $\sigma$ is constant. This implies several testable predictions:

1. **Normality of log-returns:** $\log(S_{t+\Delta}/S_t) \sim \mathcal{N}\bigl((\mu - \tfrac{1}{2}\sigma^2)\Delta, \sigma^2\Delta\bigr)$
2. **Linear variance scaling:** $\text{Var}[\log S_T] = \sigma^2 T$
3. **Independence of increments:** returns over non-overlapping periods are independent
4. **Single implied volatility:** all options on the same underlying share one $\sigma$

Each of these predictions fails empirically.

---

### Volatility Clustering

One of the most robust findings in financial econometrics is **volatility clustering**: large price changes tend to be followed by large price changes (of either sign), and small changes by small changes.

Formally, while returns $r_t$ are approximately uncorrelated:

$$
\text{Corr}(r_t, r_{t+k}) \approx 0 \quad \text{for } k \geq 1
$$

squared returns exhibit significant positive autocorrelation:

$$
\text{Corr}(r_t^2, r_{t+k}^2) > 0 \quad \text{for } k = 1, 2, \ldots, 50+
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
\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2
$$

where typically $\alpha + \beta \approx 0.95$–$0.99$, indicating high persistence.

---

### The Leverage Effect

The **leverage effect** refers to the negative correlation between returns and subsequent volatility changes: when prices fall, volatility tends to rise.

Let $r_t$ denote the return and $\sigma_{t+1}$ the subsequent volatility. Empirically:

$$
\text{Corr}(r_t, \sigma_{t+1}^2 - \sigma_t^2) < 0
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

### Time-Varying Realized Volatility

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
\text{Std}[\sigma_{\text{realized}}] \approx 0.4 \times \mathbb{E}[\sigma_{\text{realized}}]
$$

implying a coefficient of variation around 40%.

---

### Distributional Failures

Under constant volatility, log-returns are Gaussian. Empirically, returns exhibit systematic departures:

#### Heavy Tails (Leptokurtosis)

The kurtosis of a Gaussian is 3. Empirical return distributions have excess kurtosis:

$$
\text{Kurt}[r] = \frac{\mathbb{E}[(r - \mu)^4]}{(\mathbb{E}[(r-\mu)^2])^2} > 3
$$

**Typical values:**

| Frequency | Kurtosis |
|-----------|----------|
| Daily | 5–10 |
| Weekly | 4–6 |
| Monthly | 3.5–5 |

The aggregational Gaussianity (kurtosis approaching 3 at longer horizons) is consistent with stochastic volatility: conditional normality with random variance produces unconditional heavy tails.

#### Negative Skewness

Equity returns, especially for indices, exhibit negative skewness:

$$
\text{Skew}[r] = \frac{\mathbb{E}[(r - \mu)^3]}{(\mathbb{E}[(r-\mu)^2])^{3/2}} < 0
$$

**Typical values for equity indices:** $-0.3$ to $-1.0$

This reflects the leverage effect and the occasional occurrence of market crashes.

#### Extreme Events

The probability of extreme returns far exceeds Gaussian predictions:

| Event | Gaussian probability | Empirical frequency |
|-------|---------------------|---------------------|
| 3$\sigma$ daily move | 0.27% | 1%–2% |
| 5$\sigma$ daily move | 0.00006% | 0.1%–0.5% |
| 10$\sigma$ daily move | $\approx 0$ | Has occurred |

The 1987 crash ($-22.6\%$ in one day, $\approx 20\sigma$) and 2020 COVID shock illustrate that extreme events are not "tail events" under realistic distributions.

---

### Implications for Option Pricing

The distributional failures translate directly into option pricing anomalies:

#### Systematic Mispricing of OTM Options

Under Black–Scholes with constant $\sigma$:
- OTM puts are underpriced (true distribution has heavier left tail)
- OTM calls may be overpriced or underpriced depending on the asset

#### The Volatility Smile

If Black–Scholes held with constant $\sigma$, implied volatility would be flat across strikes. Instead:

$$
\sigma_{\text{impl}}(K) \neq \text{constant}
$$

The pattern—higher implied volatility for OTM puts (low strikes) and sometimes OTM calls (high strikes)—reflects the market's recognition of non-Gaussian risks.

#### Hedging Failures

Delta hedging under constant volatility assumes:

$$
\Delta = \frac{\partial C}{\partial S} = N(d_1)
$$

with known, stable $\sigma$. When volatility is stochastic:
- Delta itself becomes random
- Hedging P&L has non-zero variance even with continuous rebalancing
- Volatility exposure (vega risk) cannot be hedged by the underlying alone

---

### Quantitative Summary

| Stylized Fact | Black–Scholes Prediction | Empirical Reality |
|---------------|-------------------------|-------------------|
| Return distribution | Gaussian | Heavy-tailed, skewed |
| Kurtosis | 3 | 5–10 (daily) |
| Skewness | 0 | $-0.3$ to $-1.0$ |
| Volatility | Constant | Time-varying, clustered |
| Return-vol correlation | 0 | $-0.4$ to $-0.7$ (equity) |
| Implied volatility | Flat | Smile/skew |

---

### Key Takeaways

- Constant volatility is empirically invalid across all asset classes
- Volatility is stochastic, persistent, and exhibits the leverage effect
- Return distributions have heavy tails and (for equities) negative skew
- These features cause systematic option mispricing under Black–Scholes
- Stochastic volatility models address these failures directly

---

### Empirical Evidence: QuantPie Analysis

The empirical failures of constant volatility can be directly demonstrated through computational analysis of historical stock data. This section presents concrete evidence from a rolling-window volatility analysis on Walmart (WMT) stock spanning from August 1972 to January 2022.

#### Rolling Window Volatility Analysis

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

#### Leptokurtic Distribution: High Peak

When comparing the empirical distribution of daily returns to a fitted normal distribution, a striking feature emerges: **excess concentration near zero returns**.

The histogram of returns shows a much higher peak (narrower center) than the normal distribution fit:

$$\text{Actual return density at } r = 0 \gg \text{Normal}(0, \sigma) \text{ density}$$

This **leptokurtic** or high-peak property reflects:

1. **Small daily moves are very common:** Markets experience many "normal" trading days
2. **Wider extreme tails:** The probability mass that should be in the tails under normality is concentrated in the center, leaving heavier tails

**Quantitative evidence (WMT, 1972–2022):**

$$\text{Excess Kurtosis} = \text{Kurt}[\text{Returns}] - 3 > 0 \quad (\text{typical: 2–7 for daily data})$$

The excess kurtosis demonstrates that returns are **not normal**: the distribution is too "peaky" and has too-heavy tails.

#### Fat Tails: Excess Probability of Extreme Events

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

#### Summary of Distributional Failures

| Property | Black–Scholes Assumption | Empirical Observation |
|----------|--------------------------|----------------------|
| Volatility | Constant across time | 30-day vol: 0.5%–5%+ per day |
| Kurtosis | 3 (normal) | 5–10 (daily data) |
| Peak shape | Normal bell curve | **Higher peak** (leptokurtic) |
| Tail probability at $3\sigma$ | 0.27% | 1%–2% |
| Tail probability at $5\sigma$ | 0.00006% | 0.1%–0.5% |

#### Practical Implications

These empirical findings have direct consequences:

1. **Option pricing:** Constant-volatility models systematically misprice tail risk, undervaluing OTM puts and calls

2. **Risk management:** Value-at-Risk (VaR) calculations assuming normality underestimate tail risk, leading to insufficient capital buffers

3. **Hedging:** Delta hedging with constant volatility incurs significant P&L variance during periods of rising volatility

4. **Model requirements:** Successful models must incorporate:
   - Time-varying (stochastic) volatility
   - Mean-reverting or jump components to capture tail risk
   - Non-normal conditional distributions

---

### Further Reading

- Mandelbrot, B. (1963). *The variation of certain speculative prices*. Journal of Business.
- Engle, R. (1982). *Autoregressive conditional heteroskedasticity*. Econometrica.
- Bollerslev, T. (1986). *Generalized autoregressive conditional heteroskedasticity*. Journal of Econometrics.
- Cont, R. (2001). *Empirical properties of asset returns: stylized facts and statistical issues*. Quantitative Finance.
- Black, F. (1976). *Studies of stock price volatility changes*. Proceedings of the Business and Economics Section, ASA.

---

## Exercises

**Exercise 1.** Suppose daily log-returns on a stock index have sample kurtosis $\hat{\kappa} = 7.2$ and sample skewness $\hat{s} = -0.6$. Explain why these values are inconsistent with the constant-volatility Black–Scholes assumption, and describe which features of the return distribution they reveal.

??? success "Solution to Exercise 1"
    Under the constant-volatility Black–Scholes assumption, log-returns are normally distributed. A normal distribution has kurtosis $\kappa = 3$ and skewness $s = 0$.

    **Kurtosis $\hat{\kappa} = 7.2$:** This is well above 3, indicating **leptokurtosis** (heavy tails). The return distribution has more probability mass in the center and in the extreme tails than a Gaussian. Extreme events (both large gains and large losses) occur far more frequently than the normal model predicts.

    **Skewness $\hat{s} = -0.6$:** This is significantly negative, indicating the return distribution is **left-skewed**. Large negative returns (crashes) are more frequent or more severe than large positive returns. This asymmetry is linked to the leverage effect: when prices fall, volatility tends to rise, amplifying downside moves.

    Together, these values reveal that:

    1. The true return distribution has **fat tails**, making extreme moves much more likely than Black–Scholes predicts
    2. The distribution is **asymmetric**, with a heavier left tail, reflecting crash risk
    3. Constant volatility cannot generate either feature — both require stochastic volatility, jumps, or both

---

**Exercise 2.** A GARCH(1,1) model for daily variance is given by

$$
\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2
$$

with $\omega = 0.000002$, $\alpha = 0.08$, and $\beta = 0.91$. Compute the unconditional (long-run) variance $\bar{\sigma}^2 = \omega / (1 - \alpha - \beta)$, convert it to annualized volatility (assume 252 trading days), and verify that $\alpha + \beta < 1$ so the process is stationary.

??? success "Solution to Exercise 2"
    The unconditional (long-run) variance of a stationary GARCH(1,1) process is

    $$
    \bar{\sigma}^2 = \frac{\omega}{1 - \alpha - \beta}
    $$

    **Stationarity check:** $\alpha + \beta = 0.08 + 0.91 = 0.99 < 1$, so the process is stationary.

    **Long-run variance:**

    $$
    \bar{\sigma}^2 = \frac{0.000002}{1 - 0.99} = \frac{0.000002}{0.01} = 0.0002
    $$

    **Annualized volatility:** The daily variance is $\bar{\sigma}^2 = 0.0002$, so the daily standard deviation is $\sqrt{0.0002} \approx 0.01414$. Annualizing with 252 trading days:

    $$
    \sigma_{\text{annual}} = \sqrt{252 \times 0.0002} = \sqrt{0.0504} \approx 0.2245 = 22.45\%
    $$

    The high persistence ($\alpha + \beta = 0.99$) means volatility shocks decay very slowly, with a half-life of $\log(2)/\log(1/0.99) \approx 69$ days. This is consistent with the empirically observed long memory in volatility.

---

**Exercise 3.** Using the leverage effect, explain qualitatively why out-of-the-money put options on equity indices tend to have higher implied volatility than at-the-money options. How does the empirical correlation $\text{Corr}(r_t, \sigma_{t+1}^2 - \sigma_t^2) \approx -0.5$ manifest in the implied volatility surface?

??? success "Solution to Exercise 3"
    The **leverage effect** is the negative correlation between returns and subsequent volatility: when prices fall, volatility rises. This directly generates the negative skew in implied volatility.

    **Mechanism for OTM put pricing:**

    1. OTM puts pay off when the stock drops significantly
    2. Due to the leverage effect, a large price decline is accompanied by a volatility increase
    3. Higher volatility increases the probability of further extreme moves
    4. This makes the left tail of the risk-neutral distribution heavier than a constant-volatility model predicts
    5. To match market prices that reflect this heavy left tail, the Black–Scholes model requires a higher implied volatility for low-strike (OTM put) options

    **Manifestation of $\text{Corr}(r_t, \sigma_{t+1}^2 - \sigma_t^2) \approx -0.5$:**

    The correlation of $-0.5$ means that roughly half of the variation in volatility changes is linearly associated with returns. In the implied volatility surface:

    - **Strike dimension:** The negative correlation produces a downward-sloping smile (skew). Lower strikes correspond to negative return scenarios, which are associated with higher volatility, hence higher implied vol
    - **Time dimension:** After a market decline, both the level of the implied volatility surface rises and the skew steepens, because the conditional probability of further declines with high volatility increases
    - **Magnitude:** A correlation of $-0.5$ generates a skew of approximately 1.5%–4% per 10% of moneyness for equity indices, consistent with observed data

---

**Exercise 4.** Consider a stock with annualized volatility that fluctuates between $\sigma_{\text{low}} = 10\%$ and $\sigma_{\text{high}} = 50\%$ across market regimes. Compute the ratio of the 1-day 99% Value-at-Risk in the high-volatility regime to that in the low-volatility regime, assuming conditionally normal returns. What does this imply about risk management under constant-volatility assumptions?

??? success "Solution to Exercise 4"
    For conditionally normal returns, the 1-day 99% VaR is

    $$
    \text{VaR}_{99\%} = z_{0.99} \cdot \sigma_{\text{daily}} = 2.326 \cdot \frac{\sigma_{\text{annual}}}{\sqrt{252}}
    $$

    **High-volatility regime:**

    $$
    \text{VaR}_{\text{high}} = 2.326 \times \frac{0.50}{\sqrt{252}} = 2.326 \times 0.03150 = 0.07327 = 7.33\%
    $$

    **Low-volatility regime:**

    $$
    \text{VaR}_{\text{low}} = 2.326 \times \frac{0.10}{\sqrt{252}} = 2.326 \times 0.006300 = 0.01465 = 1.47\%
    $$

    **Ratio:**

    $$
    \frac{\text{VaR}_{\text{high}}}{\text{VaR}_{\text{low}}} = \frac{\sigma_{\text{high}}}{\sigma_{\text{low}}} = \frac{50\%}{10\%} = 5
    $$

    The VaR in the high-volatility regime is **5 times** that in the low-volatility regime.

    **Risk management implications:** A constant-volatility assumption uses a single $\sigma$ (perhaps the historical average, say 20%–25%). This means:

    - In high-vol regimes, the model **underestimates** risk by a factor of 2 or more, leading to insufficient capital reserves
    - In low-vol regimes, the model **overestimates** risk, tying up excess capital unnecessarily
    - Transitions between regimes are the most dangerous — capital buffers calibrated to calm markets are inadequate when volatility spikes

---

**Exercise 5.** Suppose you observe that over a 20-year sample, the frequency of daily returns exceeding $3\sigma$ in magnitude is $1.8\%$, where $\sigma$ is the sample standard deviation. Under a Gaussian distribution, the expected frequency is approximately $0.27\%$. Compute the ratio of empirical to theoretical frequency. If you were pricing a digital option that pays $\$1$ when the daily return exceeds $3\sigma$, by what factor would the Black–Scholes price (assuming normality) underestimate the fair value?

??? success "Solution to Exercise 5"
    **Ratio of empirical to theoretical frequency:**

    $$
    \frac{f_{\text{empirical}}}{f_{\text{Gaussian}}} = \frac{1.8\%}{0.27\%} = \frac{1.8}{0.27} \approx 6.67
    $$

    The empirical frequency of $3\sigma$ events is approximately **6.67 times** the Gaussian prediction.

    **Digital option mispricing:**

    A digital option paying $\$1$ when $|r| > 3\sigma$ has:

    - **Black–Scholes (Gaussian) price:** $e^{-rT} \times 0.0027$ per day (discounted probability under normality)
    - **Fair value:** $e^{-rT} \times 0.018$ per day (based on empirical frequency)

    The Black–Scholes price underestimates the fair value by a factor of

    $$
    \frac{0.018}{0.0027} \approx 6.67
    $$

    The normality-based price is roughly **one-seventh** of the true value. This underpricing factor would be even larger for more extreme thresholds (e.g., $5\sigma$ events), where the ratio of empirical to Gaussian frequency can exceed 100.

---

**Exercise 6.** The autocorrelation of squared daily returns at lag $k$ is defined as

$$
\rho_k = \text{Corr}(r_t^2, r_{t+k}^2)
$$

Suppose $\rho_1 = 0.20$ and the autocorrelation decays exponentially: $\rho_k = \rho_1 \cdot e^{-\lambda(k-1)}$ with $\lambda = 0.03$. Estimate the half-life of volatility clustering in trading days (i.e., the lag $k^*$ at which $\rho_{k^*} = \rho_1 / 2$). Explain why this persistence is incompatible with constant volatility.

??? success "Solution to Exercise 6"
    The autocorrelation decays as $\rho_k = \rho_1 \cdot e^{-\lambda(k-1)}$, and we want the half-life $k^*$ where $\rho_{k^*} = \rho_1 / 2$.

    Setting up the equation:

    $$
    \rho_1 \cdot e^{-\lambda(k^* - 1)} = \frac{\rho_1}{2}
    $$

    Dividing both sides by $\rho_1$:

    $$
    e^{-\lambda(k^* - 1)} = \frac{1}{2}
    $$

    Taking the natural logarithm:

    $$
    -\lambda(k^* - 1) = -\ln 2
    $$

    $$
    k^* - 1 = \frac{\ln 2}{\lambda} = \frac{0.6931}{0.03} \approx 23.1
    $$

    $$
    k^* \approx 24.1 \text{ trading days}
    $$

    The half-life of volatility clustering is approximately **24 trading days** (roughly 5 weeks).

    **Incompatibility with constant volatility:** Under constant volatility, squared returns $r_t^2$ would be i.i.d. (independent and identically distributed), implying $\rho_k = 0$ for all $k \geq 1$. The significant autocorrelation ($\rho_1 = 0.20$) and slow decay (half-life of 24 days) mean that knowing today's volatility provides substantial information about volatility over the next month. This predictability is fundamentally inconsistent with a constant $\sigma$ and requires a model where volatility evolves as a persistent stochastic process.

---

**Exercise 7.** A trader delta-hedges a short call position assuming constant volatility $\sigma = 20\%$. During the life of the option, realized volatility turns out to be $30\%$. Using the Black–Scholes gamma P&L formula, the daily hedging P&L from the volatility mismatch is approximately

$$
\text{P\&L} \approx \frac{1}{2}\Gamma S^2 (\sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2)\,\Delta t
$$

If $\Gamma = 0.02$, $S = 100$, and $\Delta t = 1/252$, compute the daily P&L leakage. Explain why this systematic loss arises and how stochastic volatility models address it.

??? success "Solution to Exercise 7"
    **Daily P&L computation:**

    $$
    \text{P\&L} \approx \frac{1}{2} \Gamma S^2 (\sigma_{\text{realized}}^2 - \sigma_{\text{implied}}^2)\,\Delta t
    $$

    Substituting the given values:

    $$
    \text{P\&L} = \frac{1}{2} \times 0.02 \times 100^2 \times (0.30^2 - 0.20^2) \times \frac{1}{252}
    $$

    Computing step by step:

    - $\frac{1}{2} \times 0.02 \times 10000 = 100$
    - $0.30^2 - 0.20^2 = 0.09 - 0.04 = 0.05$
    - $\Delta t = 1/252 \approx 0.003968$

    $$
    \text{P\&L} = 100 \times 0.05 \times 0.003968 \approx 0.0198
    $$

    The daily P&L leakage is approximately $\$0.020$ (about 2 cents per day per unit of gamma).

    **Why this systematic loss arises:** The trader sold the call and delta-hedges assuming $\sigma = 20\%$. However, the actual realized volatility is $30\%$, meaning the stock moves more than the hedge anticipates. Each day, the gamma exposure causes the hedge to be systematically "wrong" — the stock moves farther than expected, and the convexity of the option means the hedge under-compensates. Since the trader is short gamma, higher realized volatility produces a systematic loss.

    **How stochastic volatility models address this:** Stochastic volatility models recognize that $\sigma$ is random, introducing vega risk as an explicit factor. This leads to:

    1. **More accurate implied volatilities** that reflect expected future volatility variation
    2. **Vega hedging** using other options, so the trader is not exposed to volatility mismatch
    3. **Model-consistent Greeks** that account for the correlation between price and volatility moves
    4. **Volatility risk premium** that compensates option sellers for bearing the risk of realized-vs-implied volatility mismatch
