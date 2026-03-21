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
\frac{dS}{dt} = f(S, t),
$$

whose solution is uniquely determined by the initial condition $S(0) = S_0$.
Given $S_0$ and $f$, the price at every future time is *exactly* known.

The canonical example is **exponential growth**:

$$
\frac{dS}{dt} = \mu S, \qquad S(0) = S_0,
$$

with unique solution

$$
S(t) = S_0 e^{\mu t}.
$$

More generally, any ODE satisfying standard Lipschitz conditions produces a
solution that is **continuously differentiable**: the derivative $S'(t)$ exists
at every $t$.

---

## Why Deterministic Models Fail: Five Structural Failures

### Failure 1 — Zero Variance

The log-return over a period $\Delta t$ under the exponential-growth model is

$$
r_t = \log \frac{S(t + \Delta t)}{S(t)} = \mu \Delta t.
$$

This is a **constant**, not a random variable:

$$
\operatorname{Var}(r_t) = 0.
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
\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2,
$$

where $r_{t-1}^2$ is the squared return at time $t-1$ feeding into the
variance at time $t$, is simply not expressible within the ODE framework.

### Failure 4 — Cannot Produce Heavy Tails

The distribution of the log-return under the exponential-growth ODE concentrates
all probability on the single value $\mu \Delta t$:

$$
P(r_t = \mu \Delta t) = 1.
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
\varepsilon_t \sim \mathcal{N}(0,\, \sigma^2 \Delta t).
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
= \mu S(t) + \frac{\varepsilon_t}{\Delta t}.
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
\qquad Z \sim \mathcal{N}(0,1).
$$

- **Positivity:** The exponential is always positive.
- **Correct scaling:** Both drift and diffusion are proportional to $S(t)$.
- **Finite limit:** Taking logarithms,

$$
\frac{\log S(t + \Delta t) - \log S(t)}{\sqrt{\Delta t}}
= \mu\sqrt{\Delta t} + \sigma Z \;\xrightarrow{\;\Delta t \to 0\;}\; \sigma Z,
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
d(\log S_t) = \mu\,dt + \sigma\,dW_t.
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
    + \sigma W_t\right].$$
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
