# Bridge to Stochastic Differential Equations

The previous sections established that financial returns are random,
non-differentiable, heavy-tailed, and exhibit volatility clustering — none
of which deterministic ODEs can reproduce. This section builds the precise
conceptual bridge from **discrete-time random walks** to **continuous-time
stochastic differential equations (SDEs)**, which form the mathematical core
of modern quantitative finance.

The bridge has three spans: (1) the discrete model that is already familiar,
(2) the limit process that arises as the time step shrinks, and (3) the
shorthand SDE notation that encodes that limit.

---

## Concept Definition

A **stochastic differential equation** is an equation of the form

$$
dX_t = \mu(X_t, t)\,dt + \sigma(X_t, t)\,dW_t,
$$

where:

- $X_t$ is the **state variable** (e.g., an asset price or interest rate),
- $\mu(X_t,t)$ is the **drift function** — the infinitesimal expected change,
- $\sigma(X_t,t)$ is the **diffusion function** — the infinitesimal volatility,
- $W_t$ is **standard Brownian motion**.

This equation is shorthand for the integral equation

$$
X_t = X_0
+ \int_0^t \mu(X_s, s)\,ds
+ \int_0^t \sigma(X_s, s)\,dW_s,
$$

where the first integral is an ordinary Riemann integral and the second is an
**Itô stochastic integral**, whose rigorous definition is the subject of
Section 2.1.

---

## From Discrete Random Walk to Continuous-Time Limit

### Step 1 — The Discrete-Time Model

Fix a time step $\Delta t > 0$. Suppose log-prices evolve via

$$
\log S_{n+1} - \log S_n = \mu\,\Delta t + \sigma\sqrt{\Delta t}\cdot Z_n,
\qquad Z_n \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(0,1).
$$

Equivalently, in multiplicative form:

$$
S_{n+1} = S_n \exp\!\left(\mu\,\Delta t + \sigma\sqrt{\Delta t}\cdot Z_n\right).
$$

This model has three desirable properties:

- **Positivity:** $S_n > 0$ for all $n$ whenever $S_0 > 0$.
- **Correct variance scaling:** $\operatorname{Var}(\log S_{n+1} - \log S_n) = \sigma^2\Delta t$, consistent with empirical returns.
- **Multiplicative structure:** Volatility is proportional to price level.

### Step 2 — Refining the Time Step

Let $t = n\,\Delta t$ and write the change over one step as

$$
S(t+\Delta t) - S(t)
= S(t)\!\left[\exp\!\left(\mu\,\Delta t + \sigma\sqrt{\Delta t}\cdot Z\right) - 1\right].
$$

For small $\Delta t$ the first-order Taylor expansion $e^x - 1 \approx x$ gives
the **heuristic approximation**

$$
S(t+\Delta t) - S(t)
\approx S(t)\!\left(\mu\,\Delta t + \sigma\sqrt{\Delta t}\cdot Z\right).
$$

!!! warning "This expansion discards the Itô correction"
    The full second-order expansion gives $e^x - 1 \approx x + \frac{1}{2}x^2$.
    The discarded term $\frac{1}{2}(\sigma\sqrt{\Delta t})^2 = \frac{1}{2}\sigma^2\Delta t$
    is $O(\Delta t)$ — the same asymptotic order as the drift $\mu\Delta t$ —
    and therefore cannot be neglected when identifying the drift coefficient
    of the limiting SDE. Its contribution is precisely the $-\frac{\sigma^2}{2}$
    drift correction derived rigorously in Section 2.2 via Itô's lemma. The
    first-order expansion is sufficient to motivate the *structure* of the SDE
    (drift + diffusion terms) but not to determine the exact drift coefficient.

Rearranging the first-order approximation:

$$
\frac{S(t+\Delta t) - S(t)}{\Delta t}
\approx \mu\,S(t) + \sigma\,S(t)\,\frac{Z}{\sqrt{\Delta t}}.
$$

As $\Delta t \to 0$ the second term $\sigma S(t) \cdot Z/\sqrt{\Delta t}$ does
not converge pathwise — its $L^2$ norm grows like $1/\sqrt{\Delta t}$. This is
precisely why ordinary calculus is insufficient: the natural limit of the
rescaled increment is not a classical derivative but a distributional object.
The correct framework takes a **weak limit** of the entire rescaled random walk,
not a pointwise limit of the ratio above.

### Step 3 — Donsker's Theorem (Functional CLT)

Donsker's theorem applies to the rescaled log-price walk — the cumulative sum
of $Z_i$ increments — and shows it converges to Brownian motion. The price
process $S_t$ then follows by applying the exponential map to that limit.

!!! note "Donsker's Invariance Principle (1951)"
    Let $Z_1, Z_2, \ldots$ be i.i.d. with mean zero and variance one (not
    necessarily Gaussian). Define the linearly interpolated random walk,
    for $t \in [0, T)$:

    $$
    W^{(\Delta t)}(t)
    = \sqrt{\Delta t}\sum_{i=1}^{\lfloor t/\Delta t \rfloor} Z_i
    + \sqrt{\Delta t}\!\left(\frac{t}{\Delta t}
      - \left\lfloor\frac{t}{\Delta t}\right\rfloor\right)
      Z_{\lfloor t/\Delta t\rfloor+1},
    $$

    with $W^{(\Delta t)}(T)$ defined by continuity. As $\Delta t \to 0$,
    $W^{(\Delta t)} \xrightarrow{d} W$ in the space of continuous functions
    on $[0,T]$, where $W$ is standard Brownian motion.

Two remarks are essential:

1. **Universality:** The limit is Brownian motion regardless of the distribution
   of $Z_i$, as long as the mean is zero and variance is one. This justifies
   using Brownian motion as the canonical noise process for any asset whose
   log-returns have finite variance.
2. **The $\sqrt{\Delta t}$ scaling is decisive.** Scaling by $\Delta t$ would
   collapse the walk to zero; scaling by $1$ (no rescaling) would cause it to
   diverge. Only $\sqrt{\Delta t}$ keeps the limit non-degenerate.

### Step 4 — The Formal SDE Limit

With Donsker's theorem in hand, the discrete model

$$
S(t+\Delta t) - S(t) \approx \mu\,S(t)\,\Delta t + \sigma\,S(t)\,\sqrt{\Delta t}\cdot Z
$$

converges in distribution, as $\Delta t \to 0$, to the SDE

$$
\boxed{dS_t = \mu\,S_t\,dt + \sigma\,S_t\,dW_t.}
$$

This is **Geometric Brownian Motion (GBM)**, the foundation of the
Black-Scholes model. Its explicit solution — derived in Section 2.2 using
Itô's lemma, which recovers the $O(\Delta t)$ term discarded above — is

$$
S_t = S_0 \exp\!\left[\left(\mu - \tfrac{\sigma^2}{2}\right)t + \sigma W_t\right].
$$

The $-\frac{\sigma^2}{2}$ drift correction is a consequence of
$(dW_t)^2 = dt \neq 0$, not of the heuristic derivation here.

!!! warning "Notation is heuristic, content is rigorous"
    Writing "$dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$" is a compact shorthand.
    The symbol $dW_t$ does not denote an ordinary derivative — Brownian paths
    are nowhere differentiable, so $W'(t)$ does not exist. The meaning is
    always the integral form
    $S_t = S_0 + \int_0^t \mu S_s\,ds + \int_0^t \sigma S_s\,dW_s$,
    where the second integral is defined via Itô's construction (Section 2.1).

---

## What is $dW_t$?

Standard Brownian motion $W_t$ is a stochastic process satisfying:

1. $W_0 = 0$ almost surely,
2. **Independent increments:** $W_t - W_s \perp W_u - W_v$ for non-overlapping intervals $[s,t]$ and $[u,v]$,
3. **Gaussian increments:** $W_t - W_s \sim \mathcal{N}(0,\, t-s)$ for $s < t$,
4. **Continuous paths:** $t \mapsto W_t$ is continuous almost surely.

The symbol $dW_t$ is shorthand for the infinitesimal increment
$W_{t+dt} - W_t \sim \mathcal{N}(0, dt)$, satisfying

$$
\mathbb{E}[dW_t] = 0, \qquad \mathbb{E}[(dW_t)^2] = dt.
$$

The second identity — $(dW_t)^2 = dt$ in the mean-square sense — has a
precise pathwise version: the **quadratic variation** of $W$ over $[0,T]$ is
exactly $T$:

$$
\lim_{|\mathcal{P}|\to 0}
\sum_{i} \bigl(W_{t_{i+1}} - W_{t_i}\bigr)^2 = T \quad \text{almost surely.}
$$

This stands in sharp contrast to ordinary calculus, where $(dx)^2 = 0$ for
smooth functions. It is precisely this non-vanishing quadratic variation that
forces the modification of the chain rule known as **Itô's lemma**:

$$
df(W_t) = f'(W_t)\,dW_t + \tfrac{1}{2}f''(W_t)\,dt.
$$

The extra term $\frac{1}{2}f''(W_t)\,dt$ has no analogue in ordinary calculus;
it arises directly from $(dW_t)^2 = dt$.

---

## Anatomy of a General SDE

### Drift and Diffusion

The general Itô SDE

$$
dX_t = \mu(X_t, t)\,dt + \sigma(X_t, t)\,dW_t
$$

has two components with distinct roles.

**Drift term $\mu(X_t,t)\,dt$:**
the deterministic trend with $\mathbb{E}[dX_t \mid X_t] = \mu(X_t,t)\,dt$,
units $[X]$ per unit time, analogue of the ODE right-hand side.

**Diffusion term $\sigma(X_t,t)\,dW_t$:**
random fluctuations with $\operatorname{Var}(dX_t \mid X_t) = \sigma^2(X_t,t)\,dt$,
units $[X]$ per $\sqrt{\text{time}}$, mean zero so it adds uncertainty but
not bias.

### Integral Form

The SDE is always an abbreviation for

$$
X_t = X_0
+ \underbrace{\int_0^t \mu(X_s, s)\,ds}_{\text{Riemann integral}}
+ \underbrace{\int_0^t \sigma(X_s, s)\,dW_s}_{\text{Itô integral}}.
$$

The Itô integral cannot be defined as a Riemann–Stieltjes integral because
Brownian paths have unbounded variation. Section 2.1 gives its rigorous
construction as a mean-square limit of **left-endpoint** sums:

$$
\int_0^t \sigma(X_s,s)\,dW_s
= \lim_{|\mathcal{P}|\to 0}
\sum_i \sigma(X_{t_i}, t_i)\bigl(W_{t_{i+1}} - W_{t_i}\bigr).
$$

Left endpoints are used because they make the integrand $\sigma(X_{t_i}, t_i)$
measurable with respect to the information available at time $t_i$, *before*
the increment $W_{t_{i+1}} - W_{t_i}$ is observed. This **non-anticipativity**
is what gives the Itô integral its martingale property. By contrast, a
right-endpoint integrand $\sigma(X_{t_{i+1}}, t_{i+1})$ would use information
about the future increment to determine its own coefficient, destroying the
martingale property and introducing a systematic bias. Section 2.1 makes
this precise.

---

## The Journey in One Diagram

```
Real return data
      │
      │  (heavy tails, clustering, non-differentiable paths)
      ▼
Stylized facts
      │
      │  (ODE has zero variance, smooth paths — Failures 1–5)
      ▼
Deterministic models fail
      │
      │  (multiplicative noise, Δt → 0, Donsker's theorem)
      ▼
Discrete random walk  ──────────────────►  Brownian motion W_t
      │                                         │
      │  (formal limit)                         │  (rigorous foundation)
      ▼                                         ▼
  dS_t = μ S_t dt + σ S_t dW_t    ◄────  Itô calculus
      │
      │  (solve via Itô's lemma, Section 2.2)
      ▼
  S_t = S_0 exp[(μ − σ²/2)t + σ W_t]
      │
      │  (extend drift/diffusion functions)
      ▼
General SDEs  →  Quantitative finance models
```

---

## What Comes Next

The bridge is now conceptually complete. Three items remain to be made rigorous.

**Section 2.1 — Itô Integration**
Defines $\int_0^t f(s)\,dW_s$ as a mean-square limit, establishes the Itô
isometry $\mathbb{E}\!\left[\left(\int_0^t f\,dW\right)^2\right] =
\int_0^t \mathbb{E}[f^2]\,ds$, and proves the martingale property.

**Section 2.2 — Itô's Lemma**
Derives the stochastic chain rule $df(X_t) = f'(X_t)\,dX_t +
\frac{1}{2}f''(X_t)(dX_t)^2$, explains why the second-order term survives,
and verifies the GBM solution stated above — showing explicitly how the
$-\frac{\sigma^2}{2}$ correction emerges from the non-zero quadratic variation
of $W_t$.

**Section 2.3 — SDE Theory**
Presents canonical models (GBM, Vasicek/OU, CIR), solves them analytically
where possible, and discusses numerical simulation when no closed form exists.
Correlated multi-dimensional SDEs, including the Heston stochastic volatility
model, are covered in Section 2.4.

---

## Summary

The passage from discrete to continuous time is governed by one key observation:
the $\sqrt{\Delta t}$ scaling of random shocks is the only scaling consistent
with a non-degenerate continuous-time limit. Donsker's theorem makes this
precise — the rescaled log-price random walk converges to Brownian motion in
distribution, universally across all finite-variance innovations, and the
price process follows by the exponential map.

The resulting continuous-time object, the SDE

$$
dX_t = \mu(X_t,t)\,dt + \sigma(X_t,t)\,dW_t,
$$

captures what the deterministic ODE cannot: randomness, non-differentiable
paths, and a volatility that may depend on state and time. Making this
construction rigorous, and learning to compute with it, is the goal of
Chapter 2.

**Next:** Section 2.1 — Itô Integration. $\square$

---

## Exercises

**Exercise 1.** Starting from the discrete model $\log S_{n+1} - \log S_n = \mu\,\Delta t + \sigma\sqrt{\Delta t}\cdot Z_n$ with $Z_n \sim \mathcal{N}(0,1)$ i.i.d., derive the mean and variance of the log-price $\log S_N$ after $N$ steps. Show that $\operatorname{Var}(\log S_N) = \sigma^2 N\Delta t = \sigma^2 T$ where $T = N\Delta t$, confirming that variance scales linearly with total time regardless of the step size $\Delta t$.

---

**Exercise 2.** Donsker's theorem states that the rescaled random walk $W^{(\Delta t)}(t) = \sqrt{\Delta t}\sum_{i=1}^{\lfloor t/\Delta t\rfloor} Z_i$ converges in distribution to Brownian motion. Suppose the $Z_i$ are i.i.d. with $\mathbb{E}[Z_i] = 0$, $\operatorname{Var}(Z_i) = 1$, but $Z_i$ follows a Rademacher distribution ($P(Z_i = +1) = P(Z_i = -1) = 1/2$) rather than a Gaussian. Does Donsker's theorem still apply? What is the limiting process? Explain why this universality result is important for the use of Brownian motion in finance.

---

**Exercise 3.** For standard Brownian motion $W_t$, verify from the defining properties that:

(a) $\mathbb{E}[W_t] = 0$ for all $t \geq 0$,

(b) $\operatorname{Var}(W_t) = t$,

(c) $\operatorname{Cov}(W_s, W_t) = \min(s, t)$ for $s, t \geq 0$.

For part (c), use the decomposition $W_t = (W_t - W_s) + W_s$ and the independent-increments property.

---

**Exercise 4.** Consider the general SDE $dX_t = \mu(X_t,t)\,dt + \sigma(X_t,t)\,dW_t$. For each of the following models, identify the drift function $\mu(x,t)$ and diffusion function $\sigma(x,t)$, and state whether the diffusion is additive or multiplicative:

(a) Geometric Brownian Motion: $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$

(b) Ornstein–Uhlenbeck: $dX_t = \kappa(\theta - X_t)\,dt + \sigma\,dW_t$

(c) Cox–Ingersoll–Ross: $dr_t = \kappa(\theta - r_t)\,dt + \xi\sqrt{r_t}\,dW_t$

---

**Exercise 5.** The Itô integral uses left-endpoint evaluation: $\sum_i \sigma(X_{t_i}, t_i)(W_{t_{i+1}} - W_{t_i})$. Explain why using right-endpoint evaluation $\sigma(X_{t_{i+1}}, t_{i+1})$ instead would violate the non-anticipativity requirement. What practical consequence does this have for the martingale property of the Itô integral? Specifically, show that $\mathbb{E}\!\left[\sigma(X_{t_i}, t_i)(W_{t_{i+1}} - W_{t_i}) \mid \mathcal{F}_{t_i}\right] = 0$ when $\sigma(X_{t_i}, t_i)$ is $\mathcal{F}_{t_i}$-measurable, and explain why this fails if $\sigma(X_{t_{i+1}}, t_{i+1})$ is used.

---

**Exercise 6.** The heuristic first-order expansion of the discrete model gives

$$
S(t+\Delta t) - S(t) \approx \mu\,S(t)\,\Delta t + \sigma\,S(t)\,\sqrt{\Delta t}\cdot Z
$$

The second-order expansion includes the additional term $\frac{1}{2}\sigma^2 S(t)\,\Delta t$. Show that this extra term is $O(\Delta t)$ and therefore the same order as the drift $\mu\,S(t)\,\Delta t$. Explain why ignoring it changes the drift coefficient of the limiting SDE, and identify the resulting $-\sigma^2/2$ correction in the GBM solution $S_t = S_0\exp[(\mu - \sigma^2/2)t + \sigma W_t]$.

---

## Solutions

??? success "Solution to Exercise 1"
    After $N$ steps, the log-price is:

    $$
    \log S_N = \log S_0 + \sum_{n=0}^{N-1}(\log S_{n+1} - \log S_n) = \log S_0 + \sum_{n=0}^{N-1}(\mu\,\Delta t + \sigma\sqrt{\Delta t}\cdot Z_n)
    $$

    **Mean:** Since $\mathbb{E}[Z_n] = 0$ for all $n$:

    $$
    \mathbb{E}[\log S_N] = \log S_0 + \sum_{n=0}^{N-1}\mu\,\Delta t = \log S_0 + N\mu\,\Delta t = \log S_0 + \mu T
    $$

    where $T = N\Delta t$.

    **Variance:** Since the $Z_n$ are i.i.d. with $\operatorname{Var}(Z_n) = 1$, and $\log S_0$ is a constant:

    $$
    \operatorname{Var}(\log S_N) = \operatorname{Var}\!\left(\sum_{n=0}^{N-1}\sigma\sqrt{\Delta t}\cdot Z_n\right) = \sum_{n=0}^{N-1}\sigma^2\Delta t\cdot\operatorname{Var}(Z_n) = N\sigma^2\Delta t
    $$

    Since $T = N\Delta t$:

    $$
    \operatorname{Var}(\log S_N) = \sigma^2 N\Delta t = \sigma^2 T
    $$

    The variance depends only on the total time $T = N\Delta t$, not on the individual values of $N$ and $\Delta t$. Whether we use $N = 252$ steps of $\Delta t = 1/252$ or $N = 25200$ steps of $\Delta t = 1/25200$, the variance is $\sigma^2 T$ in both cases. This confirms that the variance of the log-price scales linearly with total time, independent of the discretisation — a necessary consistency condition for the continuous-time limit to be well-defined.

??? success "Solution to Exercise 2"
    Yes, Donsker's theorem still applies. The theorem requires only that the $Z_i$ are i.i.d. with $\mathbb{E}[Z_i] = 0$ and $\operatorname{Var}(Z_i) = 1$. The Rademacher distribution satisfies both conditions:

    $$
    \mathbb{E}[Z_i] = \frac{1}{2}(+1) + \frac{1}{2}(-1) = 0
    $$

    $$
    \operatorname{Var}(Z_i) = \mathbb{E}[Z_i^2] = \frac{1}{2}(1)^2 + \frac{1}{2}(-1)^2 = 1
    $$

    The limiting process is **standard Brownian motion** $W_t$, the same limit as for Gaussian increments.

    This universality is important for finance because it means the choice of Brownian motion as the canonical noise process does not depend on the specific distribution of individual price shocks. Real daily returns are non-Gaussian (heavy-tailed, skewed), yet the rescaled cumulative return process still converges to Brownian motion as the time step shrinks, provided the increments have finite variance. This justifies using the SDE framework $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ as a continuous-time model regardless of the precise distributional form of discrete-time returns. The only requirement is finite variance — when this fails (e.g., for stable distributions with $\alpha < 2$), the limit is no longer Brownian motion but a Levy process, requiring a different framework.

??? success "Solution to Exercise 3"
    **(a)** By property 3 (Gaussian increments), $W_t = W_t - W_0 \sim \mathcal{N}(0, t - 0) = \mathcal{N}(0, t)$. Therefore:

    $$
    \mathbb{E}[W_t] = 0 \quad \text{for all } t \geq 0
    $$

    **(b)** From the same property:

    $$
    \operatorname{Var}(W_t) = \mathbb{E}[W_t^2] - (\mathbb{E}[W_t])^2 = \mathbb{E}[W_t^2] - 0 = t
    $$

    **(c)** Assume without loss of generality that $s \leq t$. Decompose $W_t = (W_t - W_s) + W_s$. Then:

    $$
    \operatorname{Cov}(W_s, W_t) = \operatorname{Cov}(W_s, (W_t - W_s) + W_s)
    $$

    $$
    = \operatorname{Cov}(W_s, W_t - W_s) + \operatorname{Cov}(W_s, W_s)
    $$

    By property 2 (independent increments), $W_t - W_s$ is independent of $W_s = W_s - W_0$ since the intervals $[0, s]$ and $[s, t]$ are non-overlapping. For independent random variables, the covariance is zero:

    $$
    \operatorname{Cov}(W_s, W_t - W_s) = 0
    $$

    Therefore:

    $$
    \operatorname{Cov}(W_s, W_t) = 0 + \operatorname{Var}(W_s) = s = \min(s, t)
    $$

    By symmetry ($\operatorname{Cov}(W_s, W_t) = \operatorname{Cov}(W_t, W_s)$), the result holds for $s > t$ as well, giving $\operatorname{Cov}(W_s, W_t) = \min(s, t)$ for all $s, t \geq 0$.

??? success "Solution to Exercise 4"
    **(a) Geometric Brownian Motion:** $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$

    - Drift: $\mu(x, t) = \mu x$
    - Diffusion: $\sigma(x, t) = \sigma x$
    - The diffusion is **multiplicative** because $\sigma(x,t)$ depends on the state $x$ (proportional to the current price).

    **(b) Ornstein--Uhlenbeck:** $dX_t = \kappa(\theta - X_t)\,dt + \sigma\,dW_t$

    - Drift: $\mu(x, t) = \kappa(\theta - x)$ (mean-reverting toward $\theta$)
    - Diffusion: $\sigma(x, t) = \sigma$ (a constant)
    - The diffusion is **additive** because $\sigma(x,t) = \sigma$ does not depend on the state $x$.

    **(c) Cox--Ingersoll--Ross:** $dr_t = \kappa(\theta - r_t)\,dt + \xi\sqrt{r_t}\,dW_t$

    - Drift: $\mu(x, t) = \kappa(\theta - x)$ (mean-reverting toward $\theta$, same structure as OU)
    - Diffusion: $\sigma(x, t) = \xi\sqrt{x}$
    - The diffusion is **multiplicative** because $\sigma(x,t) = \xi\sqrt{x}$ depends on the state $x$. This square-root diffusion ensures that the volatility of the interest rate decreases as $r_t$ approaches zero, which helps keep $r_t$ non-negative (under the Feller condition $2\kappa\theta \geq \xi^2$).

??? success "Solution to Exercise 5"
    **Non-anticipativity with left-endpoint evaluation.** When the integrand is $\sigma(X_{t_i}, t_i)$, it depends only on the state at time $t_i$. The increment $W_{t_{i+1}} - W_{t_i}$ is the Brownian motion increment over the interval $(t_i, t_{i+1}]$. By the independent-increments property, $W_{t_{i+1}} - W_{t_i}$ is independent of $\mathcal{F}_{t_i}$ (the information available up to time $t_i$). Since $\sigma(X_{t_i}, t_i)$ is $\mathcal{F}_{t_i}$-measurable, the integrand is determined **before** the increment is realised — this is non-anticipativity.

    **Why right-endpoint evaluation violates non-anticipativity.** If we use $\sigma(X_{t_{i+1}}, t_{i+1})$, the integrand depends on $X_{t_{i+1}}$, which itself depends on the increment $W_{t_{i+1}} - W_{t_i}$ (through the SDE dynamics). The coefficient of the Brownian increment would therefore depend on the increment itself — this is "looking into the future" and violates non-anticipativity.

    **Martingale property with left-endpoint evaluation.** For the left-endpoint sum, consider a single term. Since $\sigma(X_{t_i}, t_i)$ is $\mathcal{F}_{t_i}$-measurable and $W_{t_{i+1}} - W_{t_i}$ is independent of $\mathcal{F}_{t_i}$:

    $$
    \mathbb{E}[\sigma(X_{t_i}, t_i)(W_{t_{i+1}} - W_{t_i}) \mid \mathcal{F}_{t_i}] = \sigma(X_{t_i}, t_i)\,\mathbb{E}[W_{t_{i+1}} - W_{t_i} \mid \mathcal{F}_{t_i}]
    $$

    $$
    = \sigma(X_{t_i}, t_i) \cdot 0 = 0
    $$

    The key step is pulling $\sigma(X_{t_i}, t_i)$ outside the conditional expectation (valid because it is $\mathcal{F}_{t_i}$-measurable), and then using $\mathbb{E}[W_{t_{i+1}} - W_{t_i} \mid \mathcal{F}_{t_i}] = 0$ (independent increments with zero mean).

    **Why this fails with right-endpoint evaluation.** If we use $\sigma(X_{t_{i+1}}, t_{i+1})$, it is not $\mathcal{F}_{t_i}$-measurable, so we cannot pull it outside the conditional expectation. Moreover, $\sigma(X_{t_{i+1}}, t_{i+1})$ and $W_{t_{i+1}} - W_{t_i}$ are generally **correlated** (since $X_{t_{i+1}}$ depends on $W_{t_{i+1}} - W_{t_i}$), so:

    $$
    \mathbb{E}[\sigma(X_{t_{i+1}}, t_{i+1})(W_{t_{i+1}} - W_{t_i}) \mid \mathcal{F}_{t_i}] \neq 0
    $$

    in general. The non-zero conditional expectation introduces a systematic drift, destroying the martingale property of the stochastic integral. This is the essential difference between Ito and Stratonovich integration.

??? success "Solution to Exercise 6"
    Starting from the discrete multiplicative model:

    $$
    S(t+\Delta t) = S(t)\exp(\mu\Delta t + \sigma\sqrt{\Delta t}\cdot Z)
    $$

    The exact increment is:

    $$
    S(t+\Delta t) - S(t) = S(t)\left[\exp(\mu\Delta t + \sigma\sqrt{\Delta t}\cdot Z) - 1\right]
    $$

    Let $x = \mu\Delta t + \sigma\sqrt{\Delta t}\cdot Z$. The second-order Taylor expansion of $e^x - 1$ is:

    $$
    e^x - 1 \approx x + \frac{1}{2}x^2
    $$

    Expanding $x^2$:

    $$
    x^2 = (\mu\Delta t + \sigma\sqrt{\Delta t}\cdot Z)^2 = \mu^2(\Delta t)^2 + 2\mu\sigma(\Delta t)^{3/2}Z + \sigma^2\Delta t\cdot Z^2
    $$

    The dominant term is $\sigma^2\Delta t \cdot Z^2$, which is $O(\Delta t)$ (since $\mathbb{E}[Z^2] = 1$). The other terms are $O((\Delta t)^{3/2})$ or higher and vanish in the limit. Therefore the second-order correction is:

    $$
    \frac{1}{2}x^2 \approx \frac{1}{2}\sigma^2\Delta t\cdot Z^2
    $$

    **This is $O(\Delta t)$** — the same order as the drift term $\mu\Delta t$. Since $\mathbb{E}[Z^2] = 1$, the expected value of this correction is $\frac{1}{2}\sigma^2\Delta t$, contributing an additional drift of $+\frac{1}{2}\sigma^2$ per unit time.

    **Why ignoring it changes the drift.** The full expansion of the increment is:

    $$
    S(t+\Delta t) - S(t) \approx S(t)\!\left[\mu\Delta t + \sigma\sqrt{\Delta t}\cdot Z + \tfrac{1}{2}\sigma^2\Delta t \cdot Z^2\right]
    $$

    Taking expectations: $\mathbb{E}[Z] = 0$ and $\mathbb{E}[Z^2] = 1$, so the expected increment per unit time is $\mu + \frac{1}{2}\sigma^2$, not $\mu$. The first-order expansion misses the $\frac{1}{2}\sigma^2$ term, leading to an incorrect drift.

    **Connection to the GBM solution.** The log-price SDE is $d(\log S_t) = \mu\,dt + \sigma\,dW_t$ (from the discrete model). Applying Ito's lemma to $f(S) = \log S$ with $dS_t = \tilde{\mu}S_t\,dt + \sigma S_t\,dW_t$ yields:

    $$
    d(\log S_t) = \left(\tilde{\mu} - \frac{\sigma^2}{2}\right)dt + \sigma\,dW_t
    $$

    The $-\sigma^2/2$ arises from the $(dW_t)^2 = dt$ quadratic variation term in Ito's lemma. Integrating:

    $$
    \log S_t = \log S_0 + \left(\tilde{\mu} - \frac{\sigma^2}{2}\right)t + \sigma W_t
    $$

    $$
    S_t = S_0\exp\!\left[\left(\tilde{\mu} - \frac{\sigma^2}{2}\right)t + \sigma W_t\right]
    $$

    Here $\tilde{\mu}$ is the drift of the price-level SDE, and $\tilde{\mu} - \sigma^2/2$ is the drift of the log-price. The $-\sigma^2/2$ correction is the continuous-time manifestation of the second-order term $\frac{1}{2}\sigma^2\Delta t$ that the first-order heuristic expansion discarded. This term is the hallmark of Ito calculus and has no analogue in ordinary calculus.
