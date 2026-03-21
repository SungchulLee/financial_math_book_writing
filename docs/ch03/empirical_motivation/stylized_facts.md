# Stylized Facts of Financial Returns

Having computed log return series and estimated their moments, we now document
the **empirical regularities** that appear robustly across assets, markets, and
time periods. These regularities — called **stylized facts** — are the empirical
constraints that any credible model must respect. They are also the direct
motivation for stochastic differential equations: each fact exposes a failure
mode of simpler models and points toward the mathematical structure needed to
fix it.

---

## Concept Definition

A **stylized fact** is an empirical regularity of financial returns that:

1. appears consistently across many assets, markets, and sample periods,
2. is robust to the precise measurement method used,
3. cannot be explained by an i.i.d. Gaussian model, and
4. constrains the class of plausible mathematical models.

The term was popularised in finance by Rama Cont (2001) in a systematic survey
of equity and FX return data. The five facts documented below are the ones
most directly relevant to the SDE models developed in this book.

---

## Stylized Fact 1: Heavy Tails (Leptokurtosis)

### Observation

The marginal distribution of daily log returns has **fatter tails** than the
Gaussian distribution with the same mean and variance. This is measured by
**excess kurtosis**:

$$
\kappa = \frac{\mathbb{E}[(r - \mu)^4]}{\sigma^4} - 3.
$$

For a Gaussian distribution $\kappa = 0$ by definition. Empirical estimates
for major equity indices at daily frequency:

| Index | Sample period | Excess kurtosis |
|---|---|---|
| S&P 500 | 1928–2023 | ≈ 20 (includes 1929, 1987 crashes) |
| S&P 500 | 2000–2023 | ≈ 9 |
| KOSPI | 2000–2023 | ≈ 7 (approximate; varies by sample) |
| EUR/USD | 2000–2023 | ≈ 5 |

As a consequence, extreme events occur far more frequently than Gaussian models
predict:

| Event | Gaussian probability | Empirical frequency (S&P 500, 2000–2023) |
|---|---|---|
| $\|r\| > 3\sigma$ | 1 in 370 days | 1 in ~50 days |
| $\|r\| > 4\sigma$ | 1 in 31 600 days | 1 in ~200 days |
| $\|r\| > 5\sigma$ | 1 in 3.5 million days | 1 in ~1 000 days |

### Mathematical Characterisation

Tail behaviour is well approximated by a **power law**:

$$
P(|r| > x) \sim C\,x^{-\alpha}
\quad \text{as } x \to \infty,
$$

with tail index $\alpha \approx 3$–$5$ for daily equity returns. A Gaussian
has exponentially thin tails; any finite $\alpha$ implies dramatically heavier
tails.

A tractable parametric family capturing this is the **Student-$t$ distribution**
with $\nu$ degrees of freedom:

$$
f(x;\nu) \propto \left(1 + \frac{x^2}{\nu}\right)^{-(\nu+1)/2}.
$$

Empirical fits for equity indices typically give $\nu \approx 4$–$6$.

!!! warning "The boundary case $\\nu = 4$"
    For $\nu \leq 4$ the fourth moment of the Student-$t$ does not exist, so
    the kurtosis is formally infinite. Empirical kurtosis estimates are always
    finite (the sample is finite), so $\nu = 4$ marks a boundary: fits with
    $\nu$ slightly above 4 produce very large but finite kurtosis consistent
    with the table above. Use $\nu > 4$ strictly when finite kurtosis is
    required.

### Implication for Modelling

Basic GBM assumes Gaussian log-returns ($\kappa = 0$). Capturing heavy tails
requires either jump-diffusion models (compound Poisson jumps added to the SDE)
or stochastic volatility models (Heston, SABR), both of which are extensions of
the Itô SDE framework developed in this book.

---

## Stylized Fact 2: Volatility Clustering

### Observation

Mandelbrot (1963) noted: *large changes tend to be followed by large changes,
of either sign, and small changes tend to be followed by small changes.*

Quantitatively:

- Log returns $r_t$ show **little or no autocorrelation**:
  $\operatorname{Corr}(r_t, r_{t-k}) \approx 0$ for $k \geq 1$.
- Squared returns $r_t^2$ (a proxy for volatility) show **strong positive
  autocorrelation** that decays slowly:
  $\operatorname{Corr}(r_t^2, r_{t-k}^2) > 0$ for lags $k$ up to 100 days or more.
- Absolute returns $|r_t|$ show similarly persistent autocorrelation.

The combination — unpredictable direction, predictable magnitude — is the
defining signature of volatility clustering.

!!! note "Why can magnitude be predictable when direction is not?"
    This is not a contradiction. Returns being unpredictable means
    $\mathbb{E}[r_t \mid \mathcal{F}_{t-1}] \approx 0$: the *conditional mean*
    is zero. Volatility clustering means $\operatorname{Var}(r_t \mid
    \mathcal{F}_{t-1})$ is time-varying and autocorrelated. A process can have
    zero conditional mean and non-constant conditional variance simultaneously —
    this is precisely the GARCH family of models.

### Testing

Engle's ARCH test regresses $r_t^2$ on its own lags and tests whether all
slope coefficients are zero. For virtually every equity index at daily
frequency, the null is rejected at $p \ll 0.001$.

```python
from statsmodels.stats.diagnostic import het_arch

def test_arch(returns, nlags=10):
    stat, pval, _, _ = het_arch(returns, nlags=nlags)
    print(f"ARCH({nlags}): stat = {stat:.2f},  p-value = {pval:.2e}")
    conclusion = "ARCH effects present" if pval < 0.05 else "No ARCH effects"
    print(f"Conclusion: {conclusion}")
```

### Implication for Modelling

Basic GBM has constant volatility $\sigma$. Capturing clustering requires
either discrete-time GARCH processes or their continuous-time analogues —
stochastic volatility SDEs such as the Heston model, where $\sigma_t$ itself
satisfies a mean-reverting SDE.

---

## Stylized Fact 3: The Leverage Effect

### Observation

There is a **negative correlation** between today's signed return and
tomorrow's variance — specifically, $\operatorname{Corr}(r_t, \sigma_{t+1}^2)$
— whose magnitude for large-cap equities is typically in the range $-0.5$
to $-0.8$. The relationship is asymmetric:

- A large **negative** return today substantially increases tomorrow's volatility.
- A large **positive** return today has a smaller, sometimes negligible, effect.

The effect was first documented by Black (1976), who attributed it to the
increase in financial leverage following a price decline (equity falls,
debt/equity ratio rises, making the firm riskier). An alternative explanation
is the **volatility feedback** hypothesis: anticipated higher future volatility
raises the risk premium, requiring a price fall today.

### Testing

The standard non-parametric diagnostic computes the cross-correlation between
the signed return $r_t$ and the future squared return $r_{t+k}^2$ at lags
$k = 1, 2, \ldots$. Negative values confirm the direction of the leverage
effect.

```python
import numpy as np

def leverage_test(returns, max_lag=20):
    """
    Compute Corr(r_t, r_{t+k}^2) for k = 1, ..., max_lag.

    Negative values at positive lags indicate the leverage effect:
    a negative return today predicts higher variance tomorrow.

    Parameters
    ----------
    returns  : pd.Series of signed log returns
    max_lag  : int, number of forward lags to compute

    Returns
    -------
    list of float, one correlation per lag
    """
    corrs = []
    for k in range(1, max_lag + 1):
        r_signed  = returns.iloc[:-k].values        # r_t  (signed)
        r_sq_lead = (returns.iloc[k:].values) ** 2  # r_{t+k}^2 (variance proxy)
        corrs.append(float(np.corrcoef(r_signed, r_sq_lead)[0, 1]))
    return corrs
```

!!! note "Why the diagnostic values are smaller than the true correlation"
    This test correlates $r_t$ with $r_{t+k}^2$, which is a **noisy proxy**
    for the true variance $\sigma_{t+k}^2$. Measurement noise in the proxy
    attenuates the correlation toward zero. Typical values from this test are
    $-0.1$ to $-0.3$ at short lags, whereas the underlying
    $\operatorname{Corr}(r_t, \sigma_{t+1}^2)$ is closer to $-0.5$ to $-0.8$.
    Both numbers are consistent: the attenuation is a known property of
    noisy-proxy regressions, not a sign that the effect is weaker than claimed.

### Implication for Modelling

The leverage effect cannot be captured by any model in which volatility is
independent of the price process. It requires a **negative correlation**
between the Brownian motions driving price and volatility — precisely the
parameter $\rho < 0$ in the Heston model:

$$
\operatorname{Cov}(dW_t^S,\, dW_t^V) = \rho\,dt, \qquad \rho \approx -0.6,
$$

where $dW_t^S$ and $dW_t^V$ are standard Brownian increments each with
variance $dt$, so $\rho$ is their correlation coefficient. In the Heston
model, $dW_t^V$ drives the variance process $V_t = \sigma_t^2$, so $\rho < 0$
is the continuous-time counterpart of the empirical
$\operatorname{Corr}(r_t, \sigma_{t+1}^2) < 0$ observed above.

---

## Stylized Fact 4: Absence of Return Autocorrelation

### Observation

For daily and lower frequencies, log returns show no statistically significant
autocorrelation:

$$
\operatorname{Corr}(r_t,\, r_{t-k}) \approx 0 \quad \text{for } k \geq 1.
$$

This is the empirical content of the **Efficient Market Hypothesis** in its
weak form: past prices contain no exploitable information about future returns.

Minor exceptions exist at very short horizons (intraday) due to bid-ask bounce
and market microstructure, but these disappear at daily and lower frequencies.

The Ljung–Box test provides a formal check:

```python
try:
    # statsmodels >= 0.13
    from statsmodels.stats.diagnostic import acorr_ljungbox
except ImportError:
    from statsmodels.tsa.stattools import acorr_ljungbox

def test_return_autocorrelation(returns, lags=20):
    result = acorr_ljungbox(returns, lags=lags, return_df=True)
    n_sig  = (result["lb_pvalue"] < 0.05).sum()
    print(f"Ljung-Box: {n_sig}/{lags} lags significant at 5 %")
```

For most equity indices fewer than 1–2 lags out of 20 will be significant,
consistent with no systematic autocorrelation.

### Implication for Modelling

The absence of return autocorrelation motivates **martingale models** for
discounted price processes — a property satisfied by GBM under the risk-neutral
measure and by all arbitrage-free pricing models.

---

## Stylized Fact 5: Aggregational Gaussianity

### Observation

Daily log returns are non-Gaussian (heavy tails, negative skewness). As we
aggregate over longer horizons, the distribution becomes **progressively more
Gaussian**. The kurtosis table in Fact 1 shows that the full S&P 500 history
reaches excess kurtosis ≈ 20; at shorter post-2000 samples the daily figure
is ≈ 9, and it decreases steadily with horizon:

| Horizon | Typical excess kurtosis |
|---|---|
| Daily | 7–10 (post-2000; see Fact 1 for century-long estimates) |
| Weekly (5 days) | 3–8 |
| Monthly (21 days) | 1–3 |
| Quarterly (63 days) | 0.5–1.5 |

This convergence is predicted by the **Central Limit Theorem**: the sum of
$n$ weakly-dependent random variables with finite variance converges to a
Gaussian as $n \to \infty$.

!!! note "Convergence is slower than i.i.d. CLT predicts"
    Because volatility clusters (Fact 2), daily returns are not independent.
    The effective sample size for the CLT is smaller than the nominal $n$,
    so convergence to Gaussianity is slower than for i.i.d. data. At monthly
    horizons non-Gaussianity is still detectable but much reduced. The
    mathematical content of this fact is that skewness decreases as
    $\sim n^{-1/2}$ and excess kurtosis as $\sim n^{-1}$ with horizon under
    i.i.d. assumptions — the direction is correct even if the rate is slower
    in practice due to clustering.

### Implication for Modelling

GBM's Gaussian log-return distribution is a reasonable approximation at
monthly and quarterly horizons, but not at daily horizons. Models that
need to be accurate at short horizons require non-Gaussian innovations,
jump components, or stochastic volatility.

---

## Summary of Stylized Facts and Model Requirements

| Stylized fact | Basic GBM | Required extension |
|---|---|---|
| Heavy tails | ✗ Gaussian | Jump diffusion or stochastic volatility |
| Volatility clustering | ✗ Constant $\sigma$ | Stochastic volatility SDE |
| Leverage effect | ✗ Independent noise | Correlated Brownian motions ($\rho < 0$) |
| No return autocorrelation | ✓ Martingale structure | Already satisfied |
| Aggregational Gaussianity | ✓ At long horizons | Already approximately satisfied |

Basic GBM satisfies two of the five facts. The remaining three — heavy tails,
clustering, and the leverage effect — require extensions that all remain within
the Itô SDE framework. This is why developing that framework rigorously is
worth the mathematical investment.

---

## Conclusion

The stylized facts reveal that financial returns are:

- **non-Gaussian** (heavy tails, negative skewness),
- **conditionally heteroskedastic** (volatility clusters),
- **asymmetrically responsive to shocks** (leverage effect),
- **unpredictable in direction** (no return autocorrelation), and
- **approximately Gaussian at long horizons** (aggregational Gaussianity).

A model that ignores these facts will produce incorrect risk measures,
mispriced options, and unreliable simulations. The next section shows
rigorously why deterministic ODEs fail to reproduce even the most basic
of these properties, and motivates the transition to stochastic differential
equations.

**Next:** Why Deterministic Models Fail. $\square$
