# Why Deterministic Models Fail

Having documented the empirical properties of financial returns — heavy tails,
volatility clustering, the leverage effect, and no return autocorrelation — we
now ask a pointed question: **Can a deterministic ordinary differential equation
adequately describe asset price dynamics?** The answer is no, and the reasons
are structural, not a matter of calibration.

---

## Concept Definition

A **deterministic model** for an asset price $S(t)$ is an ordinary differential
equation (ODE) of the form

$$
\frac{dS}{dt} = f(S, t)
$$

whose solution is uniquely determined by the initial condition $S(0) = S_0$.
Given $S_0$ and $f$, the price at every future time is *exactly* known.

The canonical example is **exponential growth**:

$$
\frac{dS}{dt} = \mu S, \qquad S(0) = S_0
$$

with unique solution

$$
S(t) = S_0 e^{\mu t}
$$

More generally, any ODE satisfying standard Lipschitz conditions produces a
solution that is **continuously differentiable**: the derivative $S'(t)$ exists
at every $t$.

---

## Why Deterministic Models Fail: Five Structural Failures

### Failure 1 — Zero Variance

The log-return over a period $\Delta t$ under the exponential-growth model is

$$
r_t = \log \frac{S(t + \Delta t)}{S(t)} = \mu \Delta t
$$

This is a **constant**, not a random variable:

$$
\operatorname{Var}(r_t) = 0
$$

Real log-returns satisfy $\operatorname{Var}(r_t) = \sigma^2 \Delta t > 0$ with
annualised volatility $\sigma$ typically in the range 15–30 % for equities.
A model with zero variance cannot reproduce any observed dispersion of returns,
regardless of how $\mu$ is chosen.

### Failure 2 — Paths Are Too Smooth

The Picard–Lindelöf theorem guarantees that, under mild regularity on $f$, the
solution of $dS/dt = f(S,t)$ is continuously differentiable. In particular,
the limit

$$
\lim_{\Delta t \to 0} \frac{S(t + \Delta t) - S(t)}{\Delta t} = f(S(t), t)
$$

exists and is a *deterministic* finite value at every $t$.

Real price paths behave differently. As $\Delta t \to 0$, the normalised
empirical increment $r_t^{\text{real}} / \sqrt{\Delta t}$ — where
$r_t^{\text{real}}$ is the actual observed log-return — converges in
distribution to a non-degenerate random variable, not a constant. This is
the hallmark of Brownian motion, whose paths are **continuous but nowhere
differentiable**. The derivative $S'(t)$ does not exist for a typical
realisation of a stochastic price process.

!!! note "Quadratic variation distinguishes the two cases"
    For a differentiable path, the quadratic variation over $[0,T]$ is zero:
    $\sum_i (S_{t_{i+1}} - S_{t_i})^2 \to 0$ as the partition is refined.
    For Brownian motion paths the same sum converges to $\sigma^2 T > 0$.
    Real return data exhibit non-zero, measurable quadratic variation,
    decisively ruling out differentiable (ODE) paths.

### Failure 3 — No Volatility Clustering

Stylized fact 2 states that squared returns $r_t^2$ are strongly
autocorrelated: $\operatorname{Corr}(r_t^2, r_{t+k}^2) > 0$ for lags $k$ up
to several months.

Under any deterministic ODE, volatility is identically zero at all times.
There is nothing to cluster. A model that cannot generate variability in
the first place cannot generate *time-varying* variability in the second place.

Mathematically, GARCH-type dependence of the form

$$
\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2
$$

where $r_{t-1}^2$ is the squared return at time $t-1$ feeding into the
variance at time $t$, is simply not expressible within the ODE framework.

### Failure 4 — Cannot Produce Heavy Tails

The distribution of the log-return under the exponential-growth ODE concentrates
all probability on the single value $\mu \Delta t$:

$$
P(r_t = \mu \Delta t) = 1
$$

This distribution has no tails whatsoever. In contrast, S&P 500 daily returns
exhibit excess kurtosis of roughly 7–10 (post-2000), with events beyond
$5\sigma$ occurring roughly once every thousand days rather than once every
several million days as a Gaussian distribution would predict.

No reparametrisation of $\mu$ can resolve this; the issue is structural.

### Failure 5 — No Leverage Effect

The leverage effect is the negative correlation between a signed return at time
$t$ and the variance at time $t+1$:

$$
\operatorname{Corr}(r_t,\, \sigma_{t+1}^2) \approx -0.6
\quad \text{(empirical estimate for large-cap equities)}.
$$

Under a deterministic ODE, $r_t = \mu\Delta t$ is a constant and
$\sigma_{t+1}^2 = 0$ identically, so the correlation is undefined. There is no
mechanism by which a price decline can feed back into increased volatility.

---

## The Naive Fix and Why It Fails

A natural first attempt is to bolt random shocks onto the ODE:

$$
S(t + \Delta t) = S(t)\,e^{\mu \Delta t} + \varepsilon_t, \qquad
\varepsilon_t \sim \mathcal{N}(0,\, \sigma^2 \Delta t)
$$

**Problem 1 — Prices can go negative.** Because $\varepsilon_t$ is unbounded
below, there is positive probability that $S(t + \Delta t) < 0$, which is
economically inadmissible.

**Problem 2 — Noise does not scale with price.** The additive term
$\varepsilon_t$ has constant variance $\sigma^2 \Delta t$ regardless of the
current price level. Empirically, a \$100 stock and a \$1000 stock with the
same percentage volatility have very different dollar volatilities. Additive
noise conflates the two.

**Problem 3 — The continuous-time limit diverges.** Dividing the increment by
$\Delta t$:

$$
\frac{S(t + \Delta t) - S(t)}{\Delta t}
= \mu S(t) + \frac{\varepsilon_t}{\Delta t}
$$

As $\Delta t \to 0$, the term $\varepsilon_t / \Delta t \sim
\mathcal{N}(0,\, \sigma^2/\Delta t)$ has standard deviation growing like
$1/\sqrt{\Delta t} \to \infty$. The limit does not exist in $L^2$; additive
noise has no consistent continuous-time interpretation.

---

## The Right Fix: Multiplicative Noise

All three problems are resolved by making the noise proportional to the
current price:

$$
S(t + \Delta t) = S(t)\exp\!\left(\mu \Delta t + \sigma\sqrt{\Delta t}\cdot Z\right),
\qquad Z \sim \mathcal{N}(0,1)
$$

- **Positivity:** The exponential is always positive.
- **Correct scaling:** Both drift and diffusion are proportional to $S(t)$.
- **Finite limit:** Taking logarithms,

$$
\frac{\log S(t + \Delta t) - \log S(t)}{\sqrt{\Delta t}}
= \mu\sqrt{\Delta t} + \sigma Z \;\xrightarrow{\;\Delta t \to 0\;}\; \sigma Z
$$

which converges in distribution to $\mathcal{N}(0, \sigma^2)$. This is
precisely a rescaled Brownian increment.

Passing to the limit $\Delta t \to 0$ motivates the shorthand notation

$$
\boxed{dS_t = \mu S_t\,dt + \sigma S_t\,dW_t,}
$$

where $W_t$ is **Brownian motion**. The derivation above establishes the
*log-price* SDE directly:

$$
d(\log S_t) = \mu\,dt + \sigma\,dW_t
$$

Recovering the *price-level* SDE $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ from
it requires the stochastic chain rule — Itô's lemma — because the ordinary
chain rule treats $W_t$ as a smooth path and applies the ordinary fundamental
theorem of calculus, missing the non-zero quadratic variation of $W_t$ that
generates an extra drift term. This is the subject of Section 2.2.

!!! warning "Ordinary calculus gives the wrong drift"
    Starting from the discrete model, naive integration of the log-price SDE
    gives $\log S_t = \log S_0 + \mu t + \sigma W_t$, hence
    $S_t = S_0 e^{\mu t + \sigma W_t}$. The correct solution, derived in
    Section 2.2 via Itô's lemma, is

    $$S_t = S_0 \exp\!\left[\left(\mu - \tfrac{\sigma^2}{2}\right)t
    + \sigma W_t\right]$$
    The $-\frac{\sigma^2}{2}$ correction comes from the second-order term
    $(dW_t)^2 = dt \neq 0$ that is absent in ordinary calculus. It is not a
    small correction: for $\sigma = 0.20$, it shifts the drift by $-0.02$
    per year — comparable to a realistic risk-free rate.

---

## Comparison Table

| Property | Deterministic ODE | Real Returns | SDE (GBM) |
|---|---|---|---|
| Randomness | None | Unpredictable | Via $dW_t$ |
| Path regularity | Smooth ($C^1$) | Nowhere differentiable | Nowhere differentiable |
| Variance | 0 | $\sigma^2 \Delta t > 0$ | $\sigma^2 \Delta t$ ✓ |
| Heavy tails | No tails | Kurtosis ≈ 7–10 | Log-normal; extensions needed |
| Volatility clustering | Impossible | Yes (GARCH) | Requires stochastic-vol extensions |
| Leverage effect | Impossible | $\operatorname{Corr}(r_t,\sigma_{t+1}^2)\approx -0.6$ | Requires correlated vol |
| Positive prices | Yes | Yes | Yes (exponential) |
| Mathematical framework | Ordinary calculus | — | Itô calculus |

Basic GBM captures randomness, correct path regularity, and positive prices.
Capturing volatility clustering and the leverage effect requires further
extensions (Heston, GARCH diffusion) that are all built on the same Itô
foundation.

---

## Summary

Deterministic ODEs fail not because their parameters are poorly chosen but
because their mathematical structure is incompatible with five fundamental
empirical properties of financial returns:

1. **Zero variance** — cannot match observed return dispersion.
2. **Differentiable paths** — incompatible with nowhere-differentiable price paths.
3. **No volatility clustering** — cannot generate time-varying risk.
4. **No heavy tails** — cannot account for the frequency of extreme events.
5. **No leverage effect** — no mechanism for asymmetric volatility response.

The minimal resolution is multiplicative noise, which forces us out of ordinary
calculus and into the framework of **stochastic differential equations**. The
next section builds the conceptual bridge from these empirical conclusions to
the continuous-time theory of SDEs.

**Next:** Bridge to Stochastic Differential Equations. $\square$

---

## Exercises

**Exercise 1.** Consider the deterministic ODE $dS/dt = \mu S$ with $S(0) = 100$ and $\mu = 0.10$ (per year). Compute the price $S(t)$ at $t = 1$ year and the log return over $[0,1]$. Now compute $\operatorname{Var}(r)$ for this model. Compare with the empirical annualised volatility of a typical equity ($\sigma \approx 0.25$) and explain why no choice of $\mu$ can resolve this discrepancy.

??? success "Solution to Exercise 1"
    The solution to $dS/dt = \mu S$ with $S(0) = 100$ and $\mu = 0.10$ is:

    $$
    S(t) = S(0)e^{\mu t} = 100 e^{0.10 \times 1} = 100 e^{0.10} \approx 110.52
    $$

    The log return over $[0,1]$ is:

    $$
    r = \log\frac{S(1)}{S(0)} = \log e^{0.10} = 0.10
    $$

    Since $S(t)$ is a deterministic function, the return $r = \mu t$ is a constant (not a random variable). Therefore:

    $$
    \operatorname{Var}(r) = 0
    $$

    A typical equity has annualised volatility $\sigma \approx 0.25$, meaning $\operatorname{Var}(r_{\text{ann}}) = \sigma^2 \approx 0.0625$. No choice of $\mu$ can resolve this discrepancy because $\mu$ only controls the **level** of the deterministic return, not its variability. The variance is identically zero for any value of $\mu$ — whether $\mu = 0.01$ or $\mu = 100$, the model produces a single deterministic path with no randomness. The failure is structural: a deterministic ODE produces exactly one trajectory, so there is no ensemble of outcomes over which variance could be defined. Matching observed return dispersion requires a fundamentally different mathematical framework that incorporates randomness.

---

**Exercise 2.** The quadratic variation of a differentiable function $g(t)$ over $[0,T]$ is defined as

$$
[g]_T = \lim_{|\mathcal{P}| \to 0} \sum_{i=0}^{n-1} \bigl(g(t_{i+1}) - g(t_i)\bigr)^2
$$

Show that $[g]_T = 0$ for any continuously differentiable function. Then explain why $[W]_T = T$ for standard Brownian motion $W_t$, and why this non-zero quadratic variation rules out differentiable paths as a model for asset prices.

??? success "Solution to Exercise 2"
    **Quadratic variation of a differentiable function is zero.** Let $g$ be continuously differentiable on $[0,T]$. By the Mean Value Theorem, for each subinterval:

    $$
    g(t_{i+1}) - g(t_i) = g'(\xi_i)(t_{i+1} - t_i)
    $$

    for some $\xi_i \in (t_i, t_{i+1})$. Therefore:

    $$
    \sum_{i=0}^{n-1}(g(t_{i+1}) - g(t_i))^2 = \sum_{i=0}^{n-1}[g'(\xi_i)]^2(t_{i+1} - t_i)^2
    $$

    Since $g'$ is continuous on $[0,T]$, it is bounded: $|g'(\xi_i)| \leq M$ for some constant $M$. Let $|\mathcal{P}| = \max_i(t_{i+1} - t_i)$ denote the mesh of the partition. Then:

    $$
    \sum_{i=0}^{n-1}[g'(\xi_i)]^2(t_{i+1} - t_i)^2 \leq M^2 |\mathcal{P}| \sum_{i=0}^{n-1}(t_{i+1} - t_i) = M^2 |\mathcal{P}| \cdot T
    $$

    As $|\mathcal{P}| \to 0$, this upper bound tends to zero, so $[g]_T = 0$.

    **Quadratic variation of Brownian motion.** For standard Brownian motion $W_t$, the quadratic variation over $[0,T]$ is $[W]_T = T$. This can be seen by considering a partition $0 = t_0 < t_1 < \cdots < t_n = T$ with equal spacing $\Delta t = T/n$. The increments $\Delta W_i = W_{t_{i+1}} - W_{t_i}$ are independent with $\Delta W_i \sim \mathcal{N}(0, \Delta t)$, so $(\Delta W_i)^2$ has mean $\Delta t$ and variance $2(\Delta t)^2$. Therefore:

    $$
    \mathbb{E}\!\left[\sum_{i=0}^{n-1}(\Delta W_i)^2\right] = n\Delta t = T
    $$

    $$
    \operatorname{Var}\!\left[\sum_{i=0}^{n-1}(\Delta W_i)^2\right] = n \cdot 2(\Delta t)^2 = 2T^2/n \to 0
    $$

    By the $L^2$ convergence (mean $T$, variance $\to 0$), the sum converges to $T$ almost surely.

    **Why this rules out differentiable paths.** Real financial data exhibit non-zero quadratic variation: $\sum_i (S_{t_{i+1}} - S_{t_i})^2$ converges to a positive value $\sigma^2 T > 0$ as the partition is refined. Since any differentiable function has zero quadratic variation, ODE solutions cannot reproduce this empirical feature. Only processes with non-differentiable paths (such as Brownian motion) can generate the non-zero quadratic variation observed in real prices.

---

**Exercise 3.** Consider the naive additive-noise model $S(t + \Delta t) = S(t)e^{\mu\Delta t} + \varepsilon_t$ with $\varepsilon_t \sim \mathcal{N}(0, \sigma^2\Delta t)$. If $S(t) = 50$, $\mu = 0.05$, and $\sigma = 0.20$, compute the probability that $S(t + \Delta t) < 0$ for $\Delta t = 1/252$ (one trading day). Then repeat for the multiplicative model $S(t+\Delta t) = S(t)\exp(\mu\Delta t + \sigma\sqrt{\Delta t}\cdot Z)$ with $Z \sim \mathcal{N}(0,1)$ and explain why the probability of a negative price is exactly zero.

??? success "Solution to Exercise 3"
    **Additive-noise model:** $S(t + \Delta t) = S(t)e^{\mu\Delta t} + \varepsilon_t$ with $\varepsilon_t \sim \mathcal{N}(0, \sigma^2\Delta t)$.

    With $S(t) = 50$, $\mu = 0.05$, $\Delta t = 1/252$:

    $$
    S(t)e^{\mu\Delta t} = 50 \cdot e^{0.05/252} \approx 50 \cdot 1.000198 \approx 50.0099
    $$

    The standard deviation of $\varepsilon_t$ is $\sigma\sqrt{\Delta t} = 0.20\sqrt{1/252} = 0.20/15.875 \approx 0.01260$.

    For $S(t+\Delta t) < 0$, we need $\varepsilon_t < -50.0099$. The number of standard deviations below the mean:

    $$
    z = \frac{-50.0099}{0.01260} \approx -3969
    $$

    This is approximately 3969 standard deviations below zero. While $P(\varepsilon_t < -50.0099)$ is astronomically small (effectively zero for practical purposes), it is **strictly positive**. The Gaussian distribution has unbounded support, so there is always a non-zero probability of any real value. In principle, $P(S(t+\Delta t) < 0) > 0$, making the model economically inadmissible.

    **Multiplicative model:** $S(t+\Delta t) = S(t)\exp(\mu\Delta t + \sigma\sqrt{\Delta t}\cdot Z)$.

    Since $S(t) = 50 > 0$ and the exponential function satisfies $e^x > 0$ for all $x \in \mathbb{R}$, regardless of the value of $Z$:

    $$
    S(t+\Delta t) = 50 \cdot \exp(\mu\Delta t + \sigma\sqrt{\Delta t}\cdot Z) > 0
    $$

    The probability of a negative price is **exactly zero**. This is the fundamental advantage of multiplicative noise: the exponential structure guarantees price positivity for all realisations of the driving random variable, making it consistent with the economic requirement that asset prices cannot be negative.

---

**Exercise 4.** In the multiplicative noise model, consider the normalised log-increment

$$
\frac{\log S(t+\Delta t) - \log S(t)}{\sqrt{\Delta t}} = \mu\sqrt{\Delta t} + \sigma Z, \qquad Z \sim \mathcal{N}(0,1)
$$

Compute the mean and variance of this quantity. Take the limit as $\Delta t \to 0$ and show that it converges in distribution to $\mathcal{N}(0, \sigma^2)$. Explain why this convergence justifies the SDE notation $d(\log S_t) = \mu\,dt + \sigma\,dW_t$.

??? success "Solution to Exercise 4"
    The normalised log-increment is:

    $$
    Y_{\Delta t} = \frac{\log S(t+\Delta t) - \log S(t)}{\sqrt{\Delta t}} = \mu\sqrt{\Delta t} + \sigma Z, \quad Z \sim \mathcal{N}(0,1)
    $$

    **Mean:**

    $$
    \mathbb{E}[Y_{\Delta t}] = \mu\sqrt{\Delta t} + \sigma \cdot \mathbb{E}[Z] = \mu\sqrt{\Delta t} + 0 = \mu\sqrt{\Delta t}
    $$

    **Variance:**

    $$
    \operatorname{Var}(Y_{\Delta t}) = \sigma^2 \operatorname{Var}(Z) = \sigma^2 \cdot 1 = \sigma^2
    $$

    (The term $\mu\sqrt{\Delta t}$ is a constant and does not contribute to variance.)

    **Limit as $\Delta t \to 0$:** As $\Delta t \to 0$, the mean $\mu\sqrt{\Delta t} \to 0$ and the variance remains $\sigma^2$. Therefore:

    $$
    Y_{\Delta t} = \mu\sqrt{\Delta t} + \sigma Z \xrightarrow{d} \sigma Z \sim \mathcal{N}(0, \sigma^2)
    $$

    The convergence is in distribution (in fact, also in $L^2$ and almost surely, since only the deterministic shift vanishes).

    This convergence justifies the SDE notation $d(\log S_t) = \mu\,dt + \sigma\,dW_t$ as follows. Over an infinitesimal interval $dt$, the log-price increment is $d(\log S_t) = \mu\,dt + \sigma\,dW_t$, where $dW_t \sim \mathcal{N}(0, dt)$. Dividing by $\sqrt{dt}$:

    $$
    \frac{d(\log S_t)}{\sqrt{dt}} = \mu\sqrt{dt} + \sigma\frac{dW_t}{\sqrt{dt}}
    $$

    Since $dW_t/\sqrt{dt} \sim \mathcal{N}(0,1)$, this matches $Y_{\Delta t}$ in the limit. The SDE notation encodes the distributional structure of the limiting rescaled increment.

---

**Exercise 5.** The correct GBM solution is $S_t = S_0\exp[(\mu - \sigma^2/2)t + \sigma W_t]$, whereas naive integration gives $S_t = S_0\exp[\mu t + \sigma W_t]$. For $S_0 = 100$, $\mu = 0.08$, $\sigma = 0.30$, and $t = 5$ years, compute $\mathbb{E}[S_t]$ under both formulas. Which formula gives $\mathbb{E}[S_t] = S_0 e^{\mu t}$? Verify that the correct formula satisfies $\mathbb{E}[S_t] = S_0 e^{\mu t}$ by using the moment generating function of the normal distribution.

??? success "Solution to Exercise 5"
    **Naive formula:** $S_t = S_0\exp[\mu t + \sigma W_t]$

    Since $W_t \sim \mathcal{N}(0, t)$, we use the moment generating function $\mathbb{E}[e^{aW_t}] = e^{a^2 t/2}$:

    $$
    \mathbb{E}[S_t^{\text{naive}}] = S_0 e^{\mu t}\mathbb{E}[e^{\sigma W_t}] = S_0 e^{\mu t} \cdot e^{\sigma^2 t/2} = S_0 e^{(\mu + \sigma^2/2)t}
    $$

    With $S_0 = 100$, $\mu = 0.08$, $\sigma = 0.30$, $t = 5$:

    $$
    \mathbb{E}[S_5^{\text{naive}}] = 100\exp\!\left[(0.08 + 0.045) \times 5\right] = 100\exp(0.625) \approx 186.82
    $$

    **Correct formula:** $S_t = S_0\exp[(\mu - \sigma^2/2)t + \sigma W_t]$

    $$
    \mathbb{E}[S_t^{\text{correct}}] = S_0 e^{(\mu - \sigma^2/2)t}\mathbb{E}[e^{\sigma W_t}] = S_0 e^{(\mu - \sigma^2/2)t} \cdot e^{\sigma^2 t/2} = S_0 e^{\mu t}
    $$

    With the given parameters:

    $$
    \mathbb{E}[S_5^{\text{correct}}] = 100\exp(0.08 \times 5) = 100\exp(0.40) \approx 149.18
    $$

    The **correct formula** gives $\mathbb{E}[S_t] = S_0 e^{\mu t}$. The naive formula gives $\mathbb{E}[S_t] = S_0 e^{(\mu + \sigma^2/2)t}$, which overestimates the expected price.

    **Verification using the MGF:** For the correct formula, $\log S_t = \log S_0 + (\mu - \sigma^2/2)t + \sigma W_t$, so $S_t = S_0 \exp[(\mu - \sigma^2/2)t + \sigma W_t]$. Taking expectations:

    $$
    \mathbb{E}[S_t] = S_0 e^{(\mu - \sigma^2/2)t} \cdot \mathbb{E}[e^{\sigma W_t}]
    $$

    Since $\sigma W_t \sim \mathcal{N}(0, \sigma^2 t)$, the MGF gives $\mathbb{E}[e^{\sigma W_t}] = e^{\sigma^2 t / 2}$. Therefore:

    $$
    \mathbb{E}[S_t] = S_0 e^{(\mu - \sigma^2/2)t} \cdot e^{\sigma^2 t/2} = S_0 e^{\mu t}
    $$

    The $-\sigma^2/2$ in the exponent of the GBM solution exactly cancels the $+\sigma^2/2$ from the MGF, yielding the clean result $\mathbb{E}[S_t] = S_0 e^{\mu t}$.

---

**Exercise 6.** For each of the five structural failures of deterministic models (zero variance, smooth paths, no volatility clustering, no heavy tails, no leverage effect), state which feature of the GBM SDE $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ addresses it and which failures require extensions beyond basic GBM. Organise your answer as a table with columns: Failure, Addressed by GBM?, Required Extension.

??? success "Solution to Exercise 6"

    | Failure | Addressed by GBM? | Required Extension |
    |---|---|---|
    | Zero variance | Yes. The $\sigma S_t\,dW_t$ term gives $\operatorname{Var}(r_t) = \sigma^2\Delta t > 0$ | None |
    | Smooth paths | Yes. Brownian motion $W_t$ has continuous but nowhere-differentiable paths, so $S_t$ is also nowhere differentiable | None |
    | No volatility clustering | No. GBM has constant $\sigma$, so $\operatorname{Corr}(r_t^2, r_{t+k}^2) = 0$ | Stochastic volatility SDE (e.g., Heston: $dV_t = \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V$) |
    | No heavy tails | No. GBM produces log-normal returns with excess kurtosis 0 for log returns | Jump-diffusion models (Merton) or stochastic volatility (which generates excess kurtosis through mixing) |
    | No leverage effect | No. GBM has a single Brownian motion; there is no mechanism linking returns to future volatility | Correlated Brownian motions with $\rho < 0$ in a stochastic volatility model (Heston with $\rho < 0$) |

    In summary, GBM resolves the two most fundamental failures of deterministic models (zero variance and smooth paths) by introducing Brownian motion. However, it cannot capture the three stylized facts that involve the **structure** of volatility (clustering, heavy tails, leverage), which require the volatility itself to be a stochastic process correlated with the price.
