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

## Further Reading

- Mandelbrot, B. (1963). *The variation of certain speculative prices*. Journal of Business.
- Engle, R. (1982). *Autoregressive conditional heteroskedasticity*. Econometrica.
- Bollerslev, T. (1986). *Generalized autoregressive conditional heteroskedasticity*. Journal of Econometrics.
- Cont, R. (2001). *Empirical properties of asset returns: stylized facts and statistical issues*. Quantitative Finance.
- Black, F. (1976). *Studies of stock price volatility changes*. Proceedings of the Business and Economics Section, ASA.
