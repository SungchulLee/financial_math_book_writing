# Empirical Failures of Constant Volatility

The Black–Scholes model assumes that volatility is constant over time and across states of the market. While this assumption leads to analytical tractability, it is fundamentally inconsistent with observed market behavior. This section documents the empirical evidence against constant volatility and its implications for option pricing.

---

### The Constant Volatility Assumption

Recall (see [§ BS Formula Statement](../../ch06/black_scholes_formula/bs_formula_statement.md)): GBM $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ with constant $\sigma$ predicts Gaussian log-returns, linear variance scaling $\text{Var}[\log S_T] = \sigma^2 T$, independent increments, and a single implied volatility across strikes/maturities.

Each prediction fails empirically.

---

### Volatility Clustering

Recall (see [§ Stylized Facts](../../ch03/empirical_motivation/stylized_facts.md)): returns are nearly uncorrelated but **squared returns** show persistent positive autocorrelation (S&P 500: $\rho_1 \approx 0.15$–$0.25$, half-life 20–40 days), formalized by ARCH/GARCH with $\alpha + \beta \approx 0.99$. Volatility is therefore predictable, contradicting constant $\sigma$.

---

### The Leverage Effect

Recall (see [§ Stylized Facts](../../ch03/empirical_motivation/stylized_facts.md) and [§ Correlation and Leverage Effect](../general_stochastic_volatility_framework/correlation_and_leverage_effect.md)): equity returns and subsequent volatility changes are negatively correlated, $\text{Corr}(r_t, \sigma_{t+1}^2 - \sigma_t^2) \in [-0.7, -0.4]$ for S&P 500. Economic drivers — balance-sheet leverage, time-varying risk premia, behavioral asymmetry — combine to produce the **negative skew** in equity index implied volatility surfaces.

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

Recall (see [§ Stylized Facts](../../ch03/empirical_motivation/stylized_facts.md)): empirical return distributions depart from the Gaussian benchmark in three persistent ways — heavy tails (daily kurtosis 5–10, aggregating toward 3 at long horizons), negative skewness for equity indices ($-1.0$ to $-0.3$), and extreme-event frequency far exceeding Gaussian predictions (e.g., $3\sigma$ daily moves occur $\sim 1\%$–$2\%$ of the time vs. $0.27\%$ predicted; the 1987 crash was $\sim 20\sigma$). Aggregational Gaussianity — kurtosis decaying toward 3 at longer horizons — is precisely the signature of conditional normality with random variance.

---

### Implications for Option Pricing

The distributional failures translate directly into option pricing anomalies:

#### Systematic Mispricing of OTM Options

Under Black–Scholes with constant $\sigma$, OTM puts are underpriced relative to the empirical (heavier) left tail; OTM call mispricing varies by asset class.

#### The Volatility Smile

Recall (see [§ Skew and Smile](../../ch12/implied_volatility_surface/skew_and_smile.md)): constant $\sigma$ predicts a flat $\sigma_{\text{impl}}(K)$; markets show a non-flat smile/skew that prices non-Gaussian risks.

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

### Empirical Evidence: QuantPie Analysis (WMT 1972–2022)

Recall (see [§ Stock Data and Returns](../../ch03/empirical_motivation/stock_data_and_returns.md) and [§ Stylized Facts](../../ch03/empirical_motivation/stylized_facts.md)): a 30-day rolling standard deviation on Walmart over five decades displays large, persistent regime variation (vol ratios exceeding 5:1) and clear clustering; the daily return histogram is sharply leptokurtic (excess kurtosis 2–7) with both tails far heavier than the fitted normal — frequencies in the $|r| > 3\sigma$ region exceed the Gaussian prediction by an order of magnitude or more. The combined implication: constant-vol models misprice tail risk, normality-based VaR understates downside, and successful models must inject time-varying volatility plus tail-risk components.

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
