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
\text{factor} = \frac{P_{\text{ex}}}{P_{\text{cum}}} \approx \frac{P_{\text{ex}}}{P_{\text{ex}} + D},
$$

so that

$$
P_{\text{adj},\,s} = P_{\text{raw},\,s} \times \frac{P_{\text{ex}}}{P_{\text{ex}} + D},
\qquad s < t.
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
r_t^{(D)} = \frac{S_t - S_{t-1}}{S_{t-1}} = \frac{S_t}{S_{t-1}} - 1.
$$

**Continuous (log) return:**

$$
r_t^{(C)} = \log\frac{S_t}{S_{t-1}} = \log S_t - \log S_{t-1}.
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
= \sum_{i=1}^n r_{t+i}^{(C)}.
$$

Discrete returns multiply rather than add: $1 + r_{[t,t+n]}^{(D)} =
\prod_{i=1}^n (1+r_{t+i}^{(D)})$. Sums are far easier to work with
probabilistically — central limit theorem, variance formulas, and stationarity
arguments all apply cleanly to additive quantities.

**Connection to Brownian motion.** Geometric Brownian Motion (GBM) predicts
that log returns over a period $\Delta t$ are Gaussian:

$$
r_t^{(C)} \sim \mathcal{N}\!\left(\mu\Delta t,\;\sigma^2\Delta t\right).
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
\hat{\sigma}^2 = \frac{1}{T-1}\sum_{t=1}^T (r_t - \hat{\mu})^2,
$$

$$
\hat{\gamma}_1 = \frac{1}{T}\sum_{t=1}^T \left(\frac{r_t - \hat\mu}{\hat\sigma}\right)^3
\quad\text{(skewness)},
\qquad
\hat{\kappa} = \frac{1}{T}\sum_{t=1}^T \left(\frac{r_t - \hat\mu}{\hat\sigma}\right)^4 - 3
\quad\text{(excess kurtosis)}.
$$

**Annualisation.** Let $N = 252$ (trading days per year). If daily log returns
were i.i.d., the annual log return would be the sum of $N$ independent daily
returns, giving

$$
\operatorname{Var}(r_{\text{ann}}) = N \hat\sigma^2
\quad\Longrightarrow\quad
\hat{\sigma}_{\text{ann}} = \sqrt{N}\,\hat{\sigma}, \qquad
\hat{\mu}_{\text{ann}} = N\,\hat{\mu}.
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
        "sharpe_ratio (rf=0)" : ann_mu / ann_sigma,
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

---

**Exercise 2.** On two consecutive trading days, a stock's adjusted close prices are $S_0 = 150$ and $S_1 = 147$. Compute both the discrete return $r^{(D)}$ and the log return $r^{(C)}$. Verify the relationship $r^{(C)} = \log(1 + r^{(D)})$ numerically, and compute the absolute difference between the two return measures. At what approximate magnitude of $|r^{(D)}|$ does the difference between the two measures first exceed 0.5 %?

---

**Exercise 3.** Let $\{r_t^{(C)}\}_{t=1}^{5}$ be five consecutive daily log returns: $+0.012$, $-0.008$, $+0.015$, $-0.003$, $+0.006$. Compute the 5-day cumulative log return directly as a sum. Then convert each daily log return to a discrete return, compute the 5-day cumulative discrete return as

$$
1 + r_{[1,5]}^{(D)} = \prod_{t=1}^{5}(1 + r_t^{(D)}),
$$

and verify that $\log(1 + r_{[1,5]}^{(D)})$ equals the sum of log returns.

---

**Exercise 4.** A daily log-return series of $T = 504$ observations (approximately two years) has sample mean $\hat{\mu} = 0.0004$ and sample standard deviation $\hat{\sigma} = 0.018$. Compute the annualised mean return and annualised volatility using $N = 252$. Then compute the annualised Sharpe ratio (assuming zero risk-free rate). State the key assumption under which the $\sqrt{N}$ volatility scaling is valid, and explain why this assumption is violated in practice.

---

**Exercise 5.** Show algebraically that for an $n$-period investment the discrete return satisfies

$$
1 + r_{[t,\,t+n]}^{(D)} = \prod_{i=1}^{n}(1 + r_{t+i}^{(D)}),
$$

while the log return satisfies $r_{[t,\,t+n]}^{(C)} = \sum_{i=1}^{n} r_{t+i}^{(C)}$. Explain why the additive property of log returns makes them more convenient for probabilistic analysis involving the Central Limit Theorem.

---

**Exercise 6.** A sample of $T = 1000$ daily log returns yields excess kurtosis $\hat{\kappa} = 4.2$ and skewness $\hat{\gamma}_1 = -0.35$. Under the null hypothesis of i.i.d. normality, the standard error of the sample excess kurtosis is approximately $\sqrt{24/T}$ and the standard error of the sample skewness is approximately $\sqrt{6/T}$. Compute both standard errors, construct approximate 95 % confidence intervals for the true kurtosis and skewness, and determine whether the Gaussian null ($\kappa = 0$, $\gamma_1 = 0$) can be rejected at the 5 % level for each moment.
