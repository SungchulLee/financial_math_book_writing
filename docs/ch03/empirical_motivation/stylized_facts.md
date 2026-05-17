# Stylized Facts of Financial Returns

Recall (see [§ Stock Data and Return Computation](stock_data_and_returns.md)):
log return series and their sample moments have already been defined. We now
catalogue the **empirical regularities** that appear robustly across assets,
markets, and time periods. These regularities — called **stylized facts** —
are the empirical constraints any credible model must respect. The
implications of each fact for modelling are stated as constraints only; the
question of which mathematical framework satisfies them is taken up in
[§ Why Deterministic Models Fail](why_deterministic_fails.md) and
[§ Bridge to Stochastic Differential Equations](bridge_to_sdes.md).

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
\kappa = \frac{\mathbb{E}[(r - \mu)^4]}{\sigma^4} - 3
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
\quad \text{as } x \to \infty
$$

with tail index $\alpha \approx 3$–$5$ for daily equity returns. A Gaussian
has exponentially thin tails; any finite $\alpha$ implies dramatically heavier
tails.

A tractable parametric family capturing this is the **Student-$t$ distribution**
with $\nu$ degrees of freedom:

$$
f(x;\nu) \propto \left(1 + \frac{x^2}{\nu}\right)^{-(\nu+1)/2}
$$

Empirical fits for equity indices typically give $\nu \approx 4$–$6$.

!!! warning "The boundary case $\\nu = 4$"
    For $\nu \leq 4$ the fourth moment of the Student-$t$ does not exist, so
    the kurtosis is formally infinite. Empirical kurtosis estimates are always
    finite (the sample is finite), so $\nu = 4$ marks a boundary: fits with
    $\nu$ slightly above 4 produce very large but finite kurtosis consistent
    with the table above. Use $\nu > 4$ strictly when finite kurtosis is
    required.

### Constraint on Models

Any acceptable model must produce a marginal return distribution with excess
kurtosis in the empirical range above. A Gaussian innovation process
($\kappa = 0$) cannot satisfy this constraint.

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

### Constraint on Models

Any acceptable model must reproduce positive, persistent autocorrelation of
$r_t^2$ (and $|r_t|$) while keeping $\operatorname{Corr}(r_t, r_{t-k})$
negligible. A constant-volatility model cannot satisfy this constraint.

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

### Constraint on Models

Any acceptable model must produce a negative correlation between the signed
return at time $t$ and the conditional variance at time $t+1$. A model in
which volatility is independent of the price process cannot satisfy this
constraint.

---

## Stylized Fact 4: Absence of Return Autocorrelation

### Observation

For daily and lower frequencies, log returns show no statistically significant
autocorrelation:

$$
\operatorname{Corr}(r_t,\, r_{t-k}) \approx 0 \quad \text{for } k \geq 1
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

### Constraint on Models

Any acceptable model must produce returns with no exploitable serial
correlation at daily or lower frequencies.

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

### Constraint on Models

Any acceptable model must reproduce the systematic decrease of excess
kurtosis with aggregation horizon, while remaining accurate at the daily
scale where non-Gaussianity is most pronounced.

---

## Summary of Empirical Constraints

| Stylized fact | Constraint any model must satisfy |
|---|---|
| Heavy tails | Marginal return distribution has excess kurtosis $\gg 0$ at daily frequency |
| Volatility clustering | $\operatorname{Corr}(r_t^2, r_{t-k}^2) > 0$ for $k$ up to ${\sim}100$ days |
| Leverage effect | $\operatorname{Corr}(r_t, \sigma_{t+1}^2) < 0$ |
| No return autocorrelation | $\operatorname{Corr}(r_t, r_{t-k}) \approx 0$ for $k \geq 1$ |
| Aggregational Gaussianity | Excess kurtosis decreases with aggregation horizon |

These are the five empirical bars that the modelling framework introduced in
later sections must clear.

---

## Conclusion

The stylized facts reveal that financial returns are:

- **non-Gaussian** (heavy tails, negative skewness),
- **conditionally heteroskedastic** (volatility clusters),
- **asymmetrically responsive to shocks** (leverage effect),
- **unpredictable in direction** (no return autocorrelation), and
- **approximately Gaussian at long horizons** (aggregational Gaussianity).

A model that ignores these facts will produce incorrect risk measures,
mispriced options, and unreliable simulations. These five constraints are
the empirical bar that any candidate framework must clear.

**Next:** [§ Why Deterministic Models Fail](why_deterministic_fails.md).
$\square$

---

## Exercises

**Exercise 1.** The excess kurtosis of a Student-$t$ distribution with $\nu > 4$ degrees of freedom is $6/(\nu - 4)$. If an empirical estimate of excess kurtosis for daily equity returns is $\hat{\kappa} = 6$, what value of $\nu$ does this imply? For this $\nu$, does the fourth moment of the Student-$t$ distribution exist? What happens to the theoretical kurtosis as $\nu \to 4^+$?

??? success "Solution to Exercise 1"
    The excess kurtosis of a Student-$t$ distribution with $\nu > 4$ degrees of freedom is $6/(\nu - 4)$. Setting this equal to the empirical estimate:

    $$
    \frac{6}{\nu - 4} = 6 \implies \nu - 4 = 1 \implies \nu = 5
    $$

    For $\nu = 5$, the fourth moment exists because the $k$-th moment of the Student-$t$ exists if and only if $\nu > k$, and here $\nu = 5 > 4$. Therefore the fourth moment (and hence the kurtosis) is finite.

    As $\nu \to 4^+$, we have $\nu - 4 \to 0^+$, so

    $$
    \kappa = \frac{6}{\nu - 4} \to +\infty
    $$

    The theoretical kurtosis diverges to infinity. At $\nu = 4$ exactly, the fourth moment ceases to exist, and for $\nu < 4$ the kurtosis is undefined. This boundary behaviour reflects the fact that heavier tails (smaller $\nu$) produce more extreme observations, inflating the fourth moment relative to the squared variance.

---

**Exercise 2.** Suppose daily log returns $\{r_t\}$ satisfy $\operatorname{Corr}(r_t, r_{t-k}) = 0$ for all $k \geq 1$, but $\operatorname{Corr}(r_t^2, r_{t-1}^2) = 0.25$. Explain why these two conditions are not contradictory. Write down a simple GARCH(1,1) model

$$
r_t = \sigma_t Z_t, \quad Z_t \sim \mathcal{N}(0,1), \quad \sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2
$$

and verify that $\mathbb{E}[r_t \mid \mathcal{F}_{t-1}] = 0$ while $\operatorname{Var}(r_t \mid \mathcal{F}_{t-1}) = \sigma_t^2$ varies over time.

??? success "Solution to Exercise 2"
    The two conditions are not contradictory because they concern different aspects of the return process.

    The condition $\operatorname{Corr}(r_t, r_{t-k}) = 0$ means that the **signed direction** of returns is unpredictable — the conditional mean is (approximately) zero. The condition $\operatorname{Corr}(r_t^2, r_{t-1}^2) = 0.25 > 0$ means that the **magnitude** of returns is predictable — the conditional variance varies over time and is autocorrelated.

    A process can have zero conditional mean and non-constant conditional variance simultaneously. The GARCH(1,1) model provides exactly this structure:

    $$
    r_t = \sigma_t Z_t, \quad Z_t \sim \mathcal{N}(0,1), \quad \sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2
    $$

    **Verification that $\mathbb{E}[r_t \mid \mathcal{F}_{t-1}] = 0$:** Since $\sigma_t^2$ depends only on $r_{t-1}^2$ and $\sigma_{t-1}^2$, $\sigma_t$ is $\mathcal{F}_{t-1}$-measurable. Also $Z_t$ is independent of $\mathcal{F}_{t-1}$ by construction. Therefore:

    $$
    \mathbb{E}[r_t \mid \mathcal{F}_{t-1}] = \mathbb{E}[\sigma_t Z_t \mid \mathcal{F}_{t-1}] = \sigma_t \mathbb{E}[Z_t \mid \mathcal{F}_{t-1}] = \sigma_t \cdot 0 = 0
    $$

    **Verification that $\operatorname{Var}(r_t \mid \mathcal{F}_{t-1}) = \sigma_t^2$ varies over time:** Since the conditional mean is zero:

    $$
    \operatorname{Var}(r_t \mid \mathcal{F}_{t-1}) = \mathbb{E}[r_t^2 \mid \mathcal{F}_{t-1}] = \mathbb{E}[\sigma_t^2 Z_t^2 \mid \mathcal{F}_{t-1}] = \sigma_t^2 \mathbb{E}[Z_t^2] = \sigma_t^2
    $$

    Because $\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2$ depends on the past squared return, the conditional variance changes over time. After a large $|r_{t-1}|$, $\sigma_t^2$ increases, making a large $|r_t|$ more likely (regardless of sign). This is precisely volatility clustering with unpredictable returns.

---

**Exercise 3.** The tail of a distribution follows a power law $P(|r| > x) \sim C x^{-\alpha}$ with $\alpha = 4$. A Gaussian distribution with the same variance $\sigma^2$ has $P(|r| > x) \approx \frac{\sigma}{x\sqrt{2\pi}} e^{-x^2/(2\sigma^2)}$ for large $x$. Taking $\sigma = 0.01$ (daily), compute both probabilities at $x = 5\sigma = 0.05$ (choose $C$ so that the power-law probability at $x = 3\sigma$ matches the Gaussian probability at $x = 3\sigma$). How many times more likely is a $5\sigma$ event under the power-law tail than under the Gaussian?

??? success "Solution to Exercise 3"
    **Step 1: Calibrate $C$ so that the power-law and Gaussian probabilities match at $x = 3\sigma$.**

    The Gaussian probability at $x = 3\sigma = 0.03$:

    $$
    P_G(|r| > 3\sigma) \approx \frac{\sigma}{3\sigma\sqrt{2\pi}} e^{-9/2} = \frac{1}{3\sqrt{2\pi}} e^{-4.5} \approx \frac{0.01111}{0.1330} \approx 0.01111 \times \frac{1}{1} \approx 0.002700
    $$

    More precisely, $P(|Z| > 3) = 2\Phi(-3) \approx 2 \times 0.001350 = 0.002700$.

    The power-law probability at $x = 3\sigma = 0.03$:

    $$
    P_{PL}(|r| > 0.03) = C \cdot (0.03)^{-4} = C \cdot \frac{1}{8.1 \times 10^{-7}} = \frac{C}{8.1 \times 10^{-7}}
    $$

    Setting equal: $C / (0.03)^4 = 0.002700$, so

    $$
    C = 0.002700 \times (0.03)^4 = 0.002700 \times 8.1 \times 10^{-7} = 2.187 \times 10^{-9}
    $$

    **Step 2: Compute both probabilities at $x = 5\sigma = 0.05$.**

    Gaussian:

    $$
    P_G(|r| > 5\sigma) = 2\Phi(-5) \approx 5.73 \times 10^{-7}
    $$

    Power law:

    $$
    P_{PL}(|r| > 0.05) = C \cdot (0.05)^{-4} = \frac{2.187 \times 10^{-9}}{6.25 \times 10^{-6}} = 3.499 \times 10^{-4}
    $$

    **Step 3: Ratio.**

    $$
    \frac{P_{PL}}{P_G} = \frac{3.499 \times 10^{-4}}{5.73 \times 10^{-7}} \approx 611
    $$

    A $5\sigma$ event is roughly **600 times more likely** under the power-law tail than under the Gaussian. This demonstrates quantitatively why Gaussian risk models severely underestimate the frequency of extreme events.

---

**Exercise 4.** The leverage effect is characterised by $\operatorname{Corr}(r_t, \sigma_{t+1}^2) < 0$. In the Heston model the correlation between the Brownian motions driving the price and variance processes is $\rho$. Explain qualitatively why $\rho < 0$ generates the leverage effect. Specifically, if $dS_t = \mu S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^S$ and $dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V$ with $\operatorname{Corr}(dW_t^S, dW_t^V) = \rho\,dt$, trace through what happens to $V_t$ when $S_t$ experiences a large negative shock (i.e., $dW_t^S \ll 0$) and $\rho = -0.7$.

??? success "Solution to Exercise 4"
    In the Heston model:

    $$
    dS_t = \mu S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^S
    $$

    $$
    dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V
    $$

    with $\operatorname{Corr}(dW_t^S, dW_t^V) = \rho\,dt$.

    When $\rho < 0$, the Brownian motions $W_t^S$ and $W_t^V$ are negatively correlated. This means that when $dW_t^S$ takes a large negative value (a negative price shock), $dW_t^V$ tends to take a large **positive** value.

    Tracing through the mechanism with $\rho = -0.7$ and $dW_t^S \ll 0$:

    1. **Price falls:** A large negative $dW_t^S$ causes $dS_t$ to be strongly negative (the diffusion term $\sqrt{V_t} S_t\,dW_t^S$ dominates), so the stock price drops sharply.

    2. **Variance increases:** Because $\rho = -0.7$, when $dW_t^S$ is very negative, $dW_t^V$ tends to be positive (with correlation $-0.7$). The positive $dW_t^V$ feeds into the variance dynamics through the term $\xi\sqrt{V_t}\,dW_t^V > 0$, pushing $dV_t$ upward beyond what the mean-reversion term $\kappa(\theta - V_t)\,dt$ alone would produce.

    3. **Result:** A negative return at time $t$ is associated with an increase in the variance process $V_t$. Since $\sigma_t = \sqrt{V_t}$, this means volatility rises after a price decline.

    This is exactly the leverage effect: $\operatorname{Corr}(r_t, \sigma_{t+1}^2) < 0$. The negative correlation $\rho$ between the two driving Brownian motions is the continuous-time mechanism that generates the asymmetric volatility response observed empirically. A positive return (large positive $dW_t^S$) would tend to produce negative $dW_t^V$, decreasing variance — but the effect is weaker in magnitude for positive returns due to the asymmetric nature of the observed leverage effect, which additional model features (such as non-linear drift in $V_t$) can capture.

---

**Exercise 5.** Aggregational Gaussianity states that excess kurtosis decreases with the return horizon. Under i.i.d. assumptions, if a daily return has excess kurtosis $\kappa_1$, show that the $n$-day return (sum of $n$ daily returns) has excess kurtosis

$$
\kappa_n = \frac{\kappa_1}{n}
$$

Using this formula, if $\kappa_1 = 8$ at daily frequency, compute the excess kurtosis at weekly ($n = 5$), monthly ($n = 21$), and quarterly ($n = 63$) horizons. At what horizon does the excess kurtosis drop below 0.5?

??? success "Solution to Exercise 5"
    If $r_1, r_2, \ldots, r_n$ are i.i.d. daily returns each with excess kurtosis $\kappa_1$ and variance $\sigma^2$, the $n$-day return is $R_n = \sum_{i=1}^n r_i$.

    By the additivity of cumulants for independent random variables, the fourth cumulant of a sum of independent variables equals the sum of the fourth cumulants. The fourth cumulant is $\kappa_4 = \kappa_1 \sigma^4$ for each daily return, and $\operatorname{Var}(R_n) = n\sigma^2$. Therefore:

    $$
    \kappa_n = \frac{\text{fourth cumulant of } R_n}{(\operatorname{Var}(R_n))^2} = \frac{n \kappa_1 \sigma^4}{(n\sigma^2)^2} = \frac{n \kappa_1 \sigma^4}{n^2 \sigma^4} = \frac{\kappa_1}{n}
    $$

    With $\kappa_1 = 8$:

    | Horizon | $n$ | $\kappa_n = 8/n$ |
    |---|---|---|
    | Weekly | 5 | $8/5 = 1.60$ |
    | Monthly | 21 | $8/21 \approx 0.381$ |
    | Quarterly | 63 | $8/63 \approx 0.127$ |

    To find when $\kappa_n < 0.5$:

    $$
    \frac{8}{n} < 0.5 \implies n > 16
    $$

    The excess kurtosis drops below 0.5 at horizon $n = 17$ days (roughly 3.5 weeks). This confirms aggregational Gaussianity: as the horizon increases, the return distribution becomes progressively closer to Gaussian.

---

**Exercise 6.** You are given a time series of 2520 daily log returns (approximately 10 years). Describe step-by-step how you would test for each of the five stylized facts documented in this section. For each fact, state: (a) the specific quantity you would compute or the test you would run, (b) the null hypothesis, and (c) what outcome would confirm the presence of the stylized fact. You do not need to perform the computations; outline the methodology only.

??? success "Solution to Exercise 6"
    **Fact 1: Heavy tails (leptokurtosis).**

    (a) Compute the sample excess kurtosis $\hat{\kappa} = \frac{1}{T}\sum_{t=1}^T \left(\frac{r_t - \hat{\mu}}{\hat{\sigma}}\right)^4 - 3$. Alternatively, perform a Jarque–Bera test, which combines skewness and kurtosis into a single test statistic $\text{JB} = \frac{T}{6}\left(\hat{\gamma}_1^2 + \frac{(\hat{\kappa})^2}{4}\right)$.

    (b) $H_0$: Returns are drawn from a Gaussian distribution, i.e., $\kappa = 0$.

    (c) Reject if $\hat{\kappa}$ is significantly positive (excess kurtosis $\gg 0$). For $T = 2520$, the standard error is $\sqrt{24/2520} \approx 0.098$. Any $\hat{\kappa} > 0.19$ would be significant at 5%.

    **Fact 2: Volatility clustering.**

    (a) Compute the autocorrelation function (ACF) of squared returns $r_t^2$ for lags $k = 1, \ldots, 50$. Run Engle's ARCH test: regress $r_t^2$ on $r_{t-1}^2, \ldots, r_{t-p}^2$ and test whether all slope coefficients are jointly zero using an $F$-test or $TR^2 \sim \chi^2_p$.

    (b) $H_0$: No ARCH effects, i.e., $\operatorname{Corr}(r_t^2, r_{t-k}^2) = 0$ for all $k \geq 1$ (constant conditional variance).

    (c) Reject if the ARCH test $p$-value is below 0.05, or equivalently if the ACF of $r_t^2$ shows significant positive values at multiple lags.

    **Fact 3: Leverage effect.**

    (a) Compute the cross-correlation $\operatorname{Corr}(r_t, r_{t+k}^2)$ for forward lags $k = 1, 2, \ldots, 20$.

    (b) $H_0$: No leverage effect, i.e., $\operatorname{Corr}(r_t, r_{t+k}^2) = 0$ for all $k \geq 1$.

    (c) Confirm the leverage effect if these cross-correlations are significantly **negative** at short positive lags (typically $k = 1, \ldots, 5$), indicating that negative returns precede higher volatility.

    **Fact 4: Absence of return autocorrelation.**

    (a) Compute the ACF of signed returns $r_t$ for lags $k = 1, \ldots, 20$. Run the Ljung–Box test: $Q = T(T+2)\sum_{k=1}^{m}\frac{\hat{\rho}_k^2}{T-k}$, where $\hat{\rho}_k$ is the sample autocorrelation at lag $k$.

    (b) $H_0$: Returns are serially uncorrelated, i.e., $\rho_k = 0$ for all tested lags.

    (c) **Fail to reject** $H_0$ — the stylized fact is confirmed by the **absence** of significant autocorrelation. Expect fewer than 1–2 lags out of 20 to be significant (consistent with the 5% false positive rate).

    **Fact 5: Aggregational Gaussianity.**

    (a) Aggregate daily returns into weekly ($n = 5$), monthly ($n = 21$), and quarterly ($n = 63$) returns by summing log returns. Compute excess kurtosis at each horizon. Optionally, apply the Jarque–Bera test at each horizon.

    (b) $H_0$: Returns at the given horizon are Gaussian ($\kappa = 0$, $\gamma_1 = 0$).

    (c) Confirm aggregational Gaussianity if the excess kurtosis **decreases** monotonically with horizon, and the Jarque–Bera test becomes non-significant (fail to reject normality) at longer horizons such as monthly or quarterly.
