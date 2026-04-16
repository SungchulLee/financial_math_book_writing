# Stock Data and Return Computation

Before constructing stochastic models of asset prices we must establish a
rigorous empirical foundation: what does real financial data look like, how do
we extract meaningful return series from it, and what statistical summaries
characterise those series? This section answers all three questions and sets up
the empirical patterns — the **stylized facts** — that motivate everything in
Chapter 3.

---

## Concept Definition

### Adjusted Close Price

Raw closing prices are distorted by **corporate actions**: stock splits, cash
dividends, rights offerings, and spin-offs. A 2-for-1 split halves the price
overnight but delivers no economic loss; a \$1 dividend reduces the price by
roughly \$1 but is offset by the cash received. If we compute returns from
unadjusted prices these events appear as spurious extreme observations.

The **adjusted close price** retroactively rescales all historical prices so
that every computed return reflects only true economic gain or loss.

For a cash dividend $D$ paid at time $t$, the stock trades at the
**cum-dividend price** $P_{\text{cum}}$ just before the ex-date and drops to
the **ex-dividend price** $P_{\text{ex}}$ immediately after. In a
frictionless, tax-free market $P_{\text{ex}} = P_{\text{cum}} - D$ exactly;
in practice the drop is slightly smaller due to tax effects on dividends, but
data providers use the actual observed ex-date price to compute the adjustment
factor:

$$
\text{factor} = \frac{P_{\text{ex}}}{P_{\text{cum}}} \approx \frac{P_{\text{ex}}}{P_{\text{ex}} + D}
$$

so that

$$
P_{\text{adj},\,s} = P_{\text{raw},\,s} \times \frac{P_{\text{ex}}}{P_{\text{ex}} + D},
\qquad s < t
$$

This ensures that a position held through the ex-date shows the correct
total return (price change plus dividend) regardless of which prices are used.
Throughout this book **adjusted close prices** are the only price series used
for return computation.

### Two Return Definitions

Let $S_t$ denote the adjusted close price on day $t$. Two return definitions
are standard.

**Discrete (arithmetic) return:**

$$
r_t^{(D)} = \frac{S_t - S_{t-1}}{S_{t-1}} = \frac{S_t}{S_{t-1}} - 1
$$

**Continuous (log) return:**

$$
r_t^{(C)} = \log\frac{S_t}{S_{t-1}} = \log S_t - \log S_{t-1}
$$

They are related by $r^{(C)} = \log(1 + r^{(D)})$. For $|r^{(D)}| < 0.05$
the two agree to within 0.1 %; for larger moves they diverge.

---

## Explanation

### Why Log Returns for Theory

Log returns have two properties that make them essential for continuous-time
modelling.

**Time additivity.** The $n$-period log return decomposes as a sum of
single-period log returns:

$$
r_{[t,\,t+n]}^{(C)}
= \log\frac{S_{t+n}}{S_t}
= \sum_{i=1}^n r_{t+i}^{(C)}
$$

Discrete returns multiply rather than add: $1 + r_{[t,t+n]}^{(D)} =
\prod_{i=1}^n (1+r_{t+i}^{(D)})$. Sums are far easier to work with
probabilistically — central limit theorem, variance formulas, and stationarity
arguments all apply cleanly to additive quantities.

**Connection to Brownian motion.** Geometric Brownian Motion (GBM) predicts
that log returns over a period $\Delta t$ are Gaussian:

$$
r_t^{(C)} \sim \mathcal{N}\!\left(\mu\Delta t,\;\sigma^2\Delta t\right)
$$

Log returns are thus the natural observation equation for GBM and for any SDE
of the form $dS = \mu S\,dt + \sigma S\,dW$. Because of this additive Gaussian
structure, maximum likelihood estimation of the GBM parameters $(\mu, \sigma)$
is performed directly on the log-return series. The stylized facts in the next
section show precisely how real returns deviate from this Gaussian prediction.

**Convention used in this book:** Theory and estimation use log returns.
Portfolio attribution uses discrete returns.

### Statistical Moments and Annualisation

Given $T$ daily log returns $\{r_t\}_{t=1}^T$, the standard moment estimates
are

$$
\hat{\mu} = \frac{1}{T}\sum_{t=1}^T r_t,
\qquad
\hat{\sigma}^2 = \frac{1}{T-1}\sum_{t=1}^T (r_t - \hat{\mu})^2
$$

$$
\hat{\gamma}_1 = \frac{1}{T}\sum_{t=1}^T \left(\frac{r_t - \hat\mu}{\hat\sigma}\right)^3
\quad\text{(skewness)},
\qquad
\hat{\kappa} = \frac{1}{T}\sum_{t=1}^T \left(\frac{r_t - \hat\mu}{\hat\sigma}\right)^4 - 3
\quad\text{(excess kurtosis)}
$$

**Annualisation.** Let $N = 252$ (trading days per year). If daily log returns
were i.i.d., the annual log return would be the sum of $N$ independent daily
returns, giving

$$
\operatorname{Var}(r_{\text{ann}}) = N \hat\sigma^2
\quad\Longrightarrow\quad
\hat{\sigma}_{\text{ann}} = \sqrt{N}\,\hat{\sigma}, \qquad
\hat{\mu}_{\text{ann}} = N\,\hat{\mu}
$$

Mean scales linearly with horizon; volatility scales with the **square root**
of horizon — a direct consequence of the independent-increments structure
of Brownian motion.

!!! warning "The i.i.d. assumption understates true annual volatility"
    Because volatility clusters (Stylized Fact 2), daily returns are not
    independent. The $\sqrt{N}$ rule assumes zero serial correlation in
    squared returns, which is empirically violated. In the presence of GARCH
    effects, the true annualised volatility exceeds $\sqrt{252}\,\hat\sigma$
    by an amount that depends on the persistence of volatility. For
    back-of-the-envelope estimates the $\sqrt{N}$ rule is standard practice,
    but treat it as a lower bound in risk applications.

!!! note "Higher moments do not annualise simply"
    Under i.i.d. normality, skewness decreases as $\sim N^{-1/2}$ and excess
    kurtosis as $\sim N^{-1}$ with horizon — which is the mathematical content
    of Stylized Fact 5 (aggregational Gaussianity). Do not annualise skewness
    or kurtosis point estimates directly.

---

## Implementation

```python
import numpy as np
import pandas as pd
import yfinance as yf

# ── 1. Data retrieval ──────────────────────────────────────────────────────────

def get_data(ticker: str, start: str, end: str) -> pd.DataFrame:
    """Return a DataFrame with adjusted close prices."""
    raw = yf.Ticker(ticker).history(start=start, end=end)[["Close"]].copy()
    # yfinance returns timezone-aware index in some versions; normalise here.
    if raw.index.tz is not None:
        raw.index = raw.index.tz_convert(None)
    return raw

# ── 2. Quality checks ─────────────────────────────────────────────────────────

def quality_check(df: pd.DataFrame) -> None:
    """
    Print a brief quality report.

    Must be called before compute_returns() — operates on the raw Close
    column only and does not expect return columns to be present.
    """
    n_missing = df["Close"].isna().sum()
    n_nonpos  = (df["Close"] <= 0).sum()
    rets      = df["Close"].pct_change().dropna()
    n_extreme = (rets.abs() > 0.20).sum()

    print(f"Observations : {len(df)}")
    print(f"Missing      : {n_missing}")
    print(f"Non-positive : {n_nonpos}")
    print(f"Moves > 20 % : {n_extreme}  (investigate if unexpected)")

# ── 3. Return computation ─────────────────────────────────────────────────────

def compute_returns(df: pd.DataFrame) -> pd.DataFrame:
    """Add discrete and log return columns; drop the initial NaN row."""
    df = df.copy()
    df["r_disc"] = df["Close"].pct_change()
    df["r_log"]  = np.log(df["Close"] / df["Close"].shift(1))
    return df.dropna()

# ── 4. Moment estimation ──────────────────────────────────────────────────────

def moment_summary(returns: pd.Series, N: int = 252) -> dict:
    """
    Compute daily and annualised moment estimates.

    Parameters
    ----------
    returns : daily log-return series
    N       : trading days per year (default 252)

    Notes
    -----
    Sharpe ratio uses a zero risk-free rate.  To use a non-zero rate,
    subtract the *daily* risk-free rate from each *daily* return before
    calling this function — do not subtract an annualised rate, as that
    would introduce an off-by-sqrt(N) scaling error.

    The sqrt(N) annualisation of volatility assumes i.i.d. daily returns.
    In the presence of volatility clustering it understates annual vol.
    """
    mu    = returns.mean()
    sigma = returns.std(ddof=1)
    skew  = returns.skew()
    kurt  = returns.kurt()       # excess kurtosis (Fisher convention)

    ann_mu    = N * mu
    ann_sigma = np.sqrt(N) * sigma

    return {
        "daily_mean"          : mu,
        "daily_vol"           : sigma,
        "skewness"            : skew,
        "excess_kurtosis"     : kurt,
        "annual_mean"         : ann_mu,
        "annual_vol"          : ann_sigma,
        "sharpe_ratio (rf=0)" : ann_mu / ann_sigma
    }

# ── 5. Full pipeline ──────────────────────────────────────────────────────────

def analyse(ticker: str, start: str, end: str) -> pd.DataFrame:
    df    = get_data(ticker, start, end)
    quality_check(df)           # must precede compute_returns
    df    = compute_returns(df)
    stats = moment_summary(df["r_log"])
    for k, v in stats.items():
        print(f"  {k:<25s}: {v:+.6f}")
    return df

df = analyse("AAPL", "2020-01-01", "2023-12-31")
```

---

## Example

### Apple Inc. (AAPL), 2020–2023

Running the pipeline above on AAPL data for 2020–2023 (approximately 1 005
trading days) yields the following estimates. Numbers are illustrative; rerun
the code for exact figures on your data pull.

| Statistic | Daily | Annualised |
|---|---|---|
| Mean log return | ≈ +0.09 % | ≈ +22 % |
| Volatility ($\sqrt{252}$ rule) | ≈ 1.7 % | ≈ 27 % |
| Skewness | ≈ −0.3 | — |
| Excess kurtosis | ≈ 3–5 | — |

Two features stand out immediately.

**Negative skewness** means large negative returns are more extreme than large
positive returns — the distribution is left-skewed. **Positive excess kurtosis**
means the distribution is leptokurtic; extreme daily moves occur far more
frequently than a Gaussian with the same mean and variance would predict.

These are the first hints of the stylized facts examined in the next section.

!!! warning "Sample-size caveat on higher moments"
    With $T \approx 1000$ observations, the standard error of the sample
    kurtosis is roughly $\sqrt{24/T} \approx 0.15$ under normality and
    considerably larger under fat tails. Treat kurtosis and skewness point
    estimates as indicative, not precise.

---

## Comparison: Discrete vs Log Returns

| Context | Preferred measure |
|---|---|
| Continuous-time SDE theory | Log return |
| Statistical estimation (MLE for GBM) | Log return |
| Portfolio allocation | Discrete return |
| Performance reporting | Discrete return |
| Option pricing (log-normal model) | Log return |

For daily moves smaller than 5 % the two measures agree to within 0.1 % and
the choice is inconsequential. For extreme events — crashes, earnings surprises
— the distinction matters and the log return is preferred for its better
distributional properties.

---

## Summary

Sound empirical work in quantitative finance rests on three foundations
established in this section:

1. **Adjusted prices** ensure that computed returns reflect only genuine
   economic change, free from the distortions introduced by dividends and
   splits.
2. **Log returns** are time-additive, compatible with Brownian motion, and
   the natural input for MLE of GBM parameters — making them the correct
   basis for both statistical analysis and continuous-time theory.
3. **Annualised moments** — in particular the $\sqrt{N}$ volatility scaling —
   encode the independent-increments structure of Brownian motion. That
   assumption is itself violated by the stylized facts, which the next section
   documents in detail.

**Next:** Stylized Facts of Financial Returns. $\square$

---

## Exercises

**Exercise 1.** A stock closes at \$80.00 on the cum-dividend date and pays a cash dividend of \$2.00. The ex-dividend price is observed at \$78.20. Compute the adjustment factor and the adjusted close price for a historical date when the raw close was \$60.00. Explain why the adjustment factor differs slightly from $78/80$.

??? success "Solution to Exercise 1"
    The adjustment factor is computed from the ex-dividend price and the cum-dividend price:

    $$
    \text{factor} = \frac{P_{\text{ex}}}{P_{\text{cum}}} = \frac{78.20}{80.00} = 0.9775
    $$

    The adjusted close price for the historical date with raw close \$60.00 is:

    $$
    P_{\text{adj}} = 60.00 \times 0.9775 = 58.65
    $$

    The factor differs from $78/80 = 0.975$ because the theoretical ex-dividend price would be $P_{\text{cum}} - D = 80.00 - 2.00 = 78.00$, but the observed ex-dividend price is \$78.20, not \$78.00. The difference arises because in practice the stock does not drop by the full dividend amount on the ex-date. Tax effects (dividends are taxed, so the market does not discount the full pre-tax dividend), supply-demand dynamics, and other market frictions cause the ex-date drop to be slightly less than $D$. The adjustment factor uses the actually observed $P_{\text{ex}} = 78.20$, which is why it equals $0.9775$ rather than the theoretical $0.975$.

---

**Exercise 2.** On two consecutive trading days, a stock's adjusted close prices are $S_0 = 150$ and $S_1 = 147$. Compute both the discrete return $r^{(D)}$ and the log return $r^{(C)}$. Verify the relationship $r^{(C)} = \log(1 + r^{(D)})$ numerically, and compute the absolute difference between the two return measures. At what approximate magnitude of $|r^{(D)}|$ does the difference between the two measures first exceed 0.5 %?

??? success "Solution to Exercise 2"
    The discrete return is:

    $$
    r^{(D)} = \frac{S_1 - S_0}{S_0} = \frac{147 - 150}{150} = -0.02
    $$

    The log return is:

    $$
    r^{(C)} = \log\frac{S_1}{S_0} = \log\frac{147}{150} = \log(0.98) \approx -0.020203
    $$

    Verifying the relationship:

    $$
    \log(1 + r^{(D)}) = \log(1 + (-0.02)) = \log(0.98) \approx -0.020203 = r^{(C)}
    $$

    The absolute difference between the two measures is:

    $$
    |r^{(D)} - r^{(C)}| = |-0.02 - (-0.020203)| = 0.000203 \approx 0.02\%
    $$

    To find when the difference first exceeds 0.5%, we need $|r^{(D)} - \log(1+r^{(D)})| > 0.005$. Using the Taylor expansion $\log(1+x) \approx x - x^2/2$, the difference is approximately $|x^2/2|$. Setting $x^2/2 = 0.005$ gives $|x| = \sqrt{0.01} = 0.1$. So the difference first exceeds 0.5% when $|r^{(D)}| \approx 10\%$, i.e., a daily move of about 10%.

---

**Exercise 3.** Let $\{r_t^{(C)}\}_{t=1}^{5}$ be five consecutive daily log returns: $+0.012$, $-0.008$, $+0.015$, $-0.003$, $+0.006$. Compute the 5-day cumulative log return directly as a sum. Then convert each daily log return to a discrete return, compute the 5-day cumulative discrete return as

$$
1 + r_{[1,5]}^{(D)} = \prod_{t=1}^{5}(1 + r_t^{(D)})
$$

and verify that $\log(1 + r_{[1,5]}^{(D)})$ equals the sum of log returns.

??? success "Solution to Exercise 3"
    The 5-day cumulative log return is the sum of the daily log returns:

    $$
    r_{[1,5]}^{(C)} = 0.012 + (-0.008) + 0.015 + (-0.003) + 0.006 = 0.022
    $$

    Converting each daily log return to a discrete return using $r_t^{(D)} = e^{r_t^{(C)}} - 1$:

    | Day | $r_t^{(C)}$ | $r_t^{(D)} = e^{r_t^{(C)}} - 1$ |
    |---|---|---|
    | 1 | $+0.012$ | $e^{0.012} - 1 \approx 0.012072$ |
    | 2 | $-0.008$ | $e^{-0.008} - 1 \approx -0.007968$ |
    | 3 | $+0.015$ | $e^{0.015} - 1 \approx 0.015113$ |
    | 4 | $-0.003$ | $e^{-0.003} - 1 \approx -0.002996$ |
    | 5 | $+0.006$ | $e^{0.006} - 1 \approx 0.006018$ |

    The 5-day cumulative discrete return is:

    $$
    1 + r_{[1,5]}^{(D)} = \prod_{t=1}^{5}(1 + r_t^{(D)}) = e^{0.012} \cdot e^{-0.008} \cdot e^{0.015} \cdot e^{-0.003} \cdot e^{0.006}
    $$

    $$
    = e^{0.012 - 0.008 + 0.015 - 0.003 + 0.006} = e^{0.022}
    $$

    Therefore:

    $$
    \log(1 + r_{[1,5]}^{(D)}) = \log(e^{0.022}) = 0.022 = \sum_{t=1}^{5} r_t^{(C)}
    $$

    This confirms the identity. The key insight is that $1 + r_t^{(D)} = e^{r_t^{(C)}}$, so the product of discrete gross returns equals the exponential of the sum of log returns, and taking logarithms recovers the sum.

---

**Exercise 4.** A daily log-return series of $T = 504$ observations (approximately two years) has sample mean $\hat{\mu} = 0.0004$ and sample standard deviation $\hat{\sigma} = 0.018$. Compute the annualised mean return and annualised volatility using $N = 252$. Then compute the annualised Sharpe ratio (assuming zero risk-free rate). State the key assumption under which the $\sqrt{N}$ volatility scaling is valid, and explain why this assumption is violated in practice.

??? success "Solution to Exercise 4"
    The annualised mean return is:

    $$
    \hat{\mu}_{\text{ann}} = N \hat{\mu} = 252 \times 0.0004 = 0.1008 \approx 10.08\%
    $$

    The annualised volatility is:

    $$
    \hat{\sigma}_{\text{ann}} = \sqrt{N}\,\hat{\sigma} = \sqrt{252} \times 0.018 \approx 15.875 \times 0.018 \approx 0.2858 \approx 28.58\%
    $$

    The annualised Sharpe ratio (with zero risk-free rate) is:

    $$
    \text{SR} = \frac{\hat{\mu}_{\text{ann}}}{\hat{\sigma}_{\text{ann}}} = \frac{0.1008}{0.2858} \approx 0.3527
    $$

    The $\sqrt{N}$ volatility scaling is valid under the assumption that daily log returns are **independent and identically distributed (i.i.d.)**. Specifically, if $r_1, \ldots, r_N$ are i.i.d. with variance $\hat{\sigma}^2$, then $\operatorname{Var}(r_1 + \cdots + r_N) = N\hat{\sigma}^2$, giving $\hat{\sigma}_{\text{ann}} = \sqrt{N}\,\hat{\sigma}$.

    This assumption is violated in practice because of **volatility clustering** (Stylized Fact 2): squared returns are positively autocorrelated, meaning $\operatorname{Cov}(r_t^2, r_{t+k}^2) > 0$ for $k \geq 1$. When returns are not independent, the variance of the annual sum includes covariance terms:

    $$
    \operatorname{Var}\!\left(\sum_{t=1}^{N} r_t\right) = \sum_{t=1}^{N} \operatorname{Var}(r_t) + 2\sum_{t<s} \operatorname{Cov}(r_t, r_s)
    $$

    While $\operatorname{Cov}(r_t, r_s) \approx 0$ (no return autocorrelation), the non-constant conditional variance induced by GARCH effects means the effective variance of the sum exceeds $N\hat{\sigma}^2$. The $\sqrt{N}$ rule therefore **understates** the true annualised volatility.

---

**Exercise 5.** Show algebraically that for an $n$-period investment the discrete return satisfies

$$
1 + r_{[t,\,t+n]}^{(D)} = \prod_{i=1}^{n}(1 + r_{t+i}^{(D)})
$$

while the log return satisfies $r_{[t,\,t+n]}^{(C)} = \sum_{i=1}^{n} r_{t+i}^{(C)}$. Explain why the additive property of log returns makes them more convenient for probabilistic analysis involving the Central Limit Theorem.

??? success "Solution to Exercise 5"
    **Discrete return multiplicativity.** By definition $1 + r_{t+i}^{(D)} = S_{t+i}/S_{t+i-1}$. Taking the product:

    $$
    \prod_{i=1}^{n}(1 + r_{t+i}^{(D)}) = \prod_{i=1}^{n}\frac{S_{t+i}}{S_{t+i-1}} = \frac{S_{t+1}}{S_t} \cdot \frac{S_{t+2}}{S_{t+1}} \cdots \frac{S_{t+n}}{S_{t+n-1}} = \frac{S_{t+n}}{S_t}
    $$

    The right-hand side is by definition $1 + r_{[t,t+n]}^{(D)}$, establishing the result.

    **Log return additivity.** By definition $r_{t+i}^{(C)} = \log S_{t+i} - \log S_{t+i-1}$. Summing:

    $$
    \sum_{i=1}^{n} r_{t+i}^{(C)} = \sum_{i=1}^{n}(\log S_{t+i} - \log S_{t+i-1})
    $$

    This is a telescoping sum:

    $$
    = \log S_{t+n} - \log S_t = \log\frac{S_{t+n}}{S_t} = r_{[t,t+n]}^{(C)}
    $$

    **Why additivity is convenient for the CLT.** The Central Limit Theorem applies to **sums** of random variables: if $X_1, \ldots, X_n$ are i.i.d. with finite mean $\mu$ and variance $\sigma^2$, then

    $$
    \frac{\sum_{i=1}^n X_i - n\mu}{\sigma\sqrt{n}} \xrightarrow{d} \mathcal{N}(0,1)
    $$

    Since $n$-period log returns are sums of single-period log returns, the CLT applies directly. This gives us the distributional convergence to normality at long horizons (aggregational Gaussianity), simple formulas for the variance of multi-period returns ($\operatorname{Var} = n\sigma^2$ under i.i.d.), and a natural connection to Brownian motion via Donsker's theorem. In contrast, discrete returns multiply, and the distribution of products of random variables is far harder to characterise — there is no simple "product CLT" that gives Gaussian limits.

---

**Exercise 6.** A sample of $T = 1000$ daily log returns yields excess kurtosis $\hat{\kappa} = 4.2$ and skewness $\hat{\gamma}_1 = -0.35$. Under the null hypothesis of i.i.d. normality, the standard error of the sample excess kurtosis is approximately $\sqrt{24/T}$ and the standard error of the sample skewness is approximately $\sqrt{6/T}$. Compute both standard errors, construct approximate 95 % confidence intervals for the true kurtosis and skewness, and determine whether the Gaussian null ($\kappa = 0$, $\gamma_1 = 0$) can be rejected at the 5 % level for each moment.

??? success "Solution to Exercise 6"
    **Standard error of excess kurtosis:**

    $$
    \text{SE}(\hat{\kappa}) = \sqrt{\frac{24}{T}} = \sqrt{\frac{24}{1000}} = \sqrt{0.024} \approx 0.1549
    $$

    **Standard error of skewness:**

    $$
    \text{SE}(\hat{\gamma}_1) = \sqrt{\frac{6}{T}} = \sqrt{\frac{6}{1000}} = \sqrt{0.006} \approx 0.0775
    $$

    **95% confidence interval for excess kurtosis** (using $z_{0.025} = 1.96$):

    $$
    \hat{\kappa} \pm 1.96 \times \text{SE}(\hat{\kappa}) = 4.2 \pm 1.96 \times 0.1549 = 4.2 \pm 0.3036
    $$

    $$
    \text{CI}_\kappa = [3.896,\; 4.504]
    $$

    **95% confidence interval for skewness:**

    $$
    \hat{\gamma}_1 \pm 1.96 \times \text{SE}(\hat{\gamma}_1) = -0.35 \pm 1.96 \times 0.0775 = -0.35 \pm 0.1519
    $$

    $$
    \text{CI}_{\gamma_1} = [-0.502,\; -0.198]
    $$

    **Testing the Gaussian null for kurtosis** ($H_0: \kappa = 0$): The test statistic is $\hat{\kappa}/\text{SE}(\hat{\kappa}) = 4.2/0.1549 \approx 27.1$. Since $|27.1| \gg 1.96$, we reject $H_0$ at the 5% level. The Gaussian null of zero excess kurtosis is overwhelmingly rejected.

    **Testing the Gaussian null for skewness** ($H_0: \gamma_1 = 0$): The test statistic is $|\hat{\gamma}_1|/\text{SE}(\hat{\gamma}_1) = 0.35/0.0775 \approx 4.52$. Since $|4.52| > 1.96$, we reject $H_0$ at the 5% level. The Gaussian null of zero skewness is also rejected.

    Both confidence intervals exclude zero, confirming that daily log returns are significantly non-Gaussian in both skewness and kurtosis.
