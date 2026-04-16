# Bridge to Stochastic Differential Equations

The previous sections established that financial returns are random,
non-differentiable, heavy-tailed, and exhibit volatility clustering---none
of which deterministic ODEs can reproduce. This section builds the conceptual
bridge from **discrete-time random walks** to **continuous-time stochastic
differential equations (SDEs)**, showing why the SDE form emerges naturally
as the only consistent continuous-time limit.

The bridge has three spans: (1) the familiar discrete model, (2) the limit
process that arises as the time step shrinks, and (3) the SDE notation that
encodes that limit. The goal is to explain *structure*, not machinery---the
rigorous definitions of the Ito integral, Ito's lemma, and SDE theory follow
in Sections 2.1--2.3.

---

## From Discrete Random Walk to Continuous-Time Limit

### Step 1 --- The Discrete-Time Model

Fix a time step $\Delta t > 0$. Suppose log-prices evolve via

$$
\log S_{n+1} - \log S_n = \mu\,\Delta t + \sigma\sqrt{\Delta t}\cdot Z_n,
\qquad Z_n \stackrel{\text{i.i.d.}}{\sim} \mathcal{N}(0,1)
$$

Equivalently, in multiplicative form:

$$
S_{n+1} = S_n \exp\!\left(\mu\,\Delta t + \sigma\sqrt{\Delta t}\cdot Z_n\right)
$$

This model has three desirable properties:

- **Positivity:** $S_n > 0$ for all $n$ whenever $S_0 > 0$.
- **Correct variance scaling:** $\operatorname{Var}(\log S_{n+1} - \log S_n) = \sigma^2\Delta t$.
- **Multiplicative structure:** Volatility is proportional to price level.

### Step 2 --- Refining the Time Step

Let $t = n\,\Delta t$ and write the change over one step as

$$
S(t+\Delta t) - S(t)
= S(t)\!\left[\exp\!\left(\mu\,\Delta t + \sigma\sqrt{\Delta t}\cdot Z\right) - 1\right]
$$

For small $\Delta t$ the first-order Taylor expansion $e^x - 1 \approx x$ gives
the heuristic approximation

$$
S(t+\Delta t) - S(t)
\approx S(t)\!\left(\mu\,\Delta t + \sigma\sqrt{\Delta t}\cdot Z\right)
$$

!!! warning "This expansion discards the Ito correction"
    The full second-order expansion gives $e^x - 1 \approx x + \frac{1}{2}x^2$.
    The discarded term $\frac{1}{2}\sigma^2\Delta t$ is $O(\Delta t)$---the
    same order as the drift $\mu\Delta t$---and therefore cannot be neglected
    when identifying the exact drift of the limiting SDE. This correction is
    derived rigorously via Ito's lemma in Section 2.2. The first-order
    expansion is sufficient to motivate the *structure* of the SDE but not to
    determine the exact drift coefficient.

Rearranging:

$$
\frac{S(t+\Delta t) - S(t)}{\Delta t}
\approx \mu\,S(t) + \sigma\,S(t)\,\frac{Z}{\sqrt{\Delta t}}
$$

As $\Delta t \to 0$, the term $Z/\sqrt{\Delta t}$ diverges---the limit is not
a classical derivative but a distributional object. This is precisely why
ordinary calculus fails and a new framework (Ito calculus, Section 2.1) is
needed. The correct approach takes a **weak limit** of the entire rescaled
random walk.

### Step 3 --- Donsker's Theorem (Functional CLT)

Donsker's theorem provides the rigorous passage from discrete to continuous
time. It applies to the cumulative sum of rescaled increments and shows it
converges in distribution to Brownian motion.

!!! note "Donsker's Invariance Principle (1951)"
    Let $Z_1, Z_2, \ldots$ be i.i.d. with mean zero and variance one (not
    necessarily Gaussian). Define the rescaled partial-sum process

    $$
    W^{(\Delta t)}(t) = \sqrt{\Delta t}\sum_{i=1}^{\lfloor t/\Delta t \rfloor} Z_i
    $$

    As $\Delta t \to 0$, $W^{(\Delta t)} \xrightarrow{d} W$ in the space of
    continuous functions on $[0,T]$, where $W$ is standard Brownian motion.

Two consequences are essential:

1. **Universality.** The limit is Brownian motion regardless of the
   distribution of $Z_i$, as long as mean is zero and variance is one. This
   justifies using Brownian motion as the canonical noise for any asset whose
   log-returns have finite variance.
2. **The $\sqrt{\Delta t}$ scaling is decisive.** Scaling by $\Delta t$ would
   collapse the walk to zero; no rescaling would cause divergence. Only
   $\sqrt{\Delta t}$ produces a non-degenerate limit.

### Step 4 --- The SDE Limit

With Donsker's theorem in hand, the discrete model

$$
S(t+\Delta t) - S(t) \approx \mu\,S(t)\,\Delta t + \sigma\,S(t)\,\sqrt{\Delta t}\cdot Z
$$

converges in distribution, as $\Delta t \to 0$, to

$$
\boxed{dS_t = \mu\,S_t\,dt + \sigma\,S_t\,dW_t}
$$

This is **Geometric Brownian Motion (GBM)**, the foundation of the
Black--Scholes model. Its explicit solution---derived in Section 2.2 using
Ito's lemma---is

$$
S_t = S_0 \exp\!\left[\left(\mu - \tfrac{\sigma^2}{2}\right)t + \sigma W_t\right]
$$

The $-\sigma^2/2$ drift correction is a consequence of the non-vanishing
quadratic variation $(dW_t)^2 = dt$, not of the heuristic derivation here.

!!! note "SDE notation is shorthand"
    The symbol $dW_t$ does not denote an ordinary derivative---Brownian paths
    are nowhere differentiable. The SDE always means the integral equation
    $S_t = S_0 + \int_0^t \mu S_s\,ds + \int_0^t \sigma S_s\,dW_s$,
    where the second integral is defined via Ito's construction (Section 2.1).

---

## Emergence of the General SDE

The GBM derivation above used constant drift $\mu$ and constant proportional
volatility $\sigma$. Replacing these with state- and time-dependent functions
gives the general Ito SDE:

$$
dX_t = \mu(X_t, t)\,dt + \sigma(X_t, t)\,dW_t
$$

- The **drift** $\mu(X_t, t)\,dt$ is the infinitesimal expected change---the
  analogue of the ODE right-hand side.
- The **diffusion** $\sigma(X_t, t)\,dW_t$ encodes random fluctuations whose
  magnitude may depend on state and time.

Different choices of $\mu$ and $\sigma$ produce different financial models.
The classification of these models and their solutions is the subject of
Section 2.3.

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
      │  (extend drift/diffusion functions)
      ▼
General SDEs  →  Quantitative finance models
```

---

## What Comes Next

The bridge is conceptually complete. Three items remain to be made rigorous:

- **Section 2.1 --- Ito Integration:** Defines $\int_0^t f(s)\,dW_s$ as a
  mean-square limit, establishes the Ito isometry, and proves the martingale
  property.
- **Section 2.2 --- Ito's Lemma:** Derives the stochastic chain rule and
  verifies the GBM solution, showing how the $-\sigma^2/2$ correction emerges
  from the non-zero quadratic variation.
- **Section 2.3 --- SDE Theory:** Presents canonical models (GBM,
  Vasicek/OU, CIR), solves them analytically where possible, and discusses
  numerical simulation.

---

## Summary

The passage from discrete to continuous time is governed by one key
observation: the $\sqrt{\Delta t}$ scaling of random shocks is the only
scaling consistent with a non-degenerate continuous-time limit. Donsker's
theorem makes this precise---the rescaled random walk converges to Brownian
motion universally across all finite-variance innovations.

The resulting SDE

$$
dX_t = \mu(X_t,t)\,dt + \sigma(X_t,t)\,dW_t
$$

captures what the deterministic ODE cannot: randomness, non-differentiable
paths, and state-dependent volatility. Making this construction rigorous is
the goal of the next three sections. $\square$

---

## Exercises

**Exercise 1.**
Starting from the discrete model
$\log S_{n+1} - \log S_n = \mu\,\Delta t + \sigma\sqrt{\Delta t}\cdot Z_n$
with $Z_n \sim \mathcal{N}(0,1)$ i.i.d., derive the mean and variance of
$\log S_N$ after $N$ steps. Show that
$\operatorname{Var}(\log S_N) = \sigma^2 T$ where $T = N\Delta t$,
independent of the step size.

??? success "Solution to Exercise 1"
    After $N$ steps:

    $$
    \log S_N = \log S_0 + \sum_{n=0}^{N-1}(\mu\,\Delta t + \sigma\sqrt{\Delta t}\cdot Z_n)
    $$

    **Mean:** Since $\mathbb{E}[Z_n] = 0$:

    $$
    \mathbb{E}[\log S_N] = \log S_0 + N\mu\,\Delta t = \log S_0 + \mu T
    $$

    **Variance:** Since the $Z_n$ are i.i.d. with unit variance:

    $$
    \operatorname{Var}(\log S_N) = \sum_{n=0}^{N-1}\sigma^2\Delta t = N\sigma^2\Delta t = \sigma^2 T
    $$

    The variance depends only on $T = N\Delta t$, not on $N$ and $\Delta t$ individually. This scale-invariance is a necessary condition for the continuous-time limit to be well-defined.

---

**Exercise 2.**
Donsker's theorem requires only i.i.d. increments with mean zero and
variance one. Suppose $Z_i$ follows a Rademacher distribution
($P(Z_i = +1) = P(Z_i = -1) = 1/2$) instead of a Gaussian. Does
Donsker's theorem still apply? What is the limiting process? Explain why
this universality matters for financial modeling.

??? success "Solution to Exercise 2"
    Yes. The Rademacher distribution satisfies $\mathbb{E}[Z_i] = 0$ and $\operatorname{Var}(Z_i) = 1$, so Donsker's theorem applies. The limiting process is standard Brownian motion---the same as for Gaussian increments.

    This universality matters because real daily returns are non-Gaussian (heavy-tailed, skewed), yet the rescaled cumulative process still converges to Brownian motion as $\Delta t \to 0$, provided increments have finite variance. The choice of Brownian motion as the canonical noise does not depend on the precise distributional form of discrete returns. The only requirement is finite variance---when this fails (e.g., stable distributions with index $\alpha < 2$), the limit is a Levy process, requiring a different framework.

---

**Exercise 3.**
The heuristic first-order expansion gives
$S(t+\Delta t) - S(t) \approx \mu\,S(t)\,\Delta t + \sigma\,S(t)\,\sqrt{\Delta t}\cdot Z$.
The second-order expansion includes an additional term
$\frac{1}{2}\sigma^2 S(t)\,\Delta t$. Show that this term is $O(\Delta t)$
and therefore the same order as the drift. Explain how this leads to the
$-\sigma^2/2$ correction in the GBM solution.

??? success "Solution to Exercise 3"
    Let $x = \mu\Delta t + \sigma\sqrt{\Delta t}\cdot Z$. The second-order expansion of $e^x - 1$ gives:

    $$
    e^x - 1 \approx x + \frac{1}{2}x^2
    $$

    Expanding $x^2$:

    $$
    x^2 = \mu^2(\Delta t)^2 + 2\mu\sigma(\Delta t)^{3/2}Z + \sigma^2\Delta t\cdot Z^2
    $$

    The dominant term is $\sigma^2\Delta t \cdot Z^2$, which is $O(\Delta t)$ since $\mathbb{E}[Z^2] = 1$. The other terms are $O((\Delta t)^{3/2})$ or higher. So $\frac{1}{2}x^2 \approx \frac{1}{2}\sigma^2\Delta t \cdot Z^2$ is the same asymptotic order as the drift $\mu\Delta t$.

    Taking expectations: $\mathbb{E}[Z^2] = 1$, so the correction contributes an additional drift of $+\frac{1}{2}\sigma^2$ per unit time. In the continuous-time limit, Ito's lemma applied to $\log S_t$ produces:

    $$
    d(\log S_t) = \left(\mu - \frac{\sigma^2}{2}\right)dt + \sigma\,dW_t
    $$

    The $-\sigma^2/2$ arises from $(dW_t)^2 = dt$. Integrating gives the GBM solution $S_t = S_0\exp[(\mu - \sigma^2/2)t + \sigma W_t]$.

---

**Exercise 4.**
For each of the following models, identify the drift function
$\mu(x,t)$ and diffusion function $\sigma(x,t)$, and state whether the
diffusion is additive or multiplicative:

(a) Geometric Brownian Motion: $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$

(b) Ornstein--Uhlenbeck: $dX_t = \kappa(\theta - X_t)\,dt + \sigma\,dW_t$

(c) Cox--Ingersoll--Ross: $dr_t = \kappa(\theta - r_t)\,dt + \xi\sqrt{r_t}\,dW_t$

??? success "Solution to Exercise 4"
    **(a) GBM:** Drift $\mu(x,t) = \mu x$, diffusion $\sigma(x,t) = \sigma x$. **Multiplicative** ($\sigma$ depends on state $x$).

    **(b) OU:** Drift $\mu(x,t) = \kappa(\theta - x)$ (mean-reverting toward $\theta$), diffusion $\sigma(x,t) = \sigma$ (constant). **Additive** ($\sigma$ does not depend on $x$).

    **(c) CIR:** Drift $\mu(x,t) = \kappa(\theta - x)$ (mean-reverting), diffusion $\sigma(x,t) = \xi\sqrt{x}$. **Multiplicative** ($\sigma$ depends on $x$). The square-root diffusion ensures volatility decreases as $r_t$ approaches zero, helping keep $r_t$ non-negative under the Feller condition $2\kappa\theta \geq \xi^2$.

---

**Exercise 5.**
Explain why the $\sqrt{\Delta t}$ scaling in Donsker's theorem is the
unique scaling that produces a non-degenerate limit. What happens if
increments are scaled by $\Delta t$ instead? By $1$ (no rescaling)?
Connect this to the non-differentiability of Brownian paths.

??? success "Solution to Exercise 5"
    The partial sum $S_N = \sum_{i=1}^N Z_i$ has variance $N$, so $\operatorname{Var}(S_N) = N = T/\Delta t$.

    - **Scaling by $\Delta t$:** The rescaled process $\Delta t \cdot S_{\lfloor t/\Delta t\rfloor}$ has variance $(\Delta t)^2 \cdot T/\Delta t = \Delta t \cdot T \to 0$. The limit is the constant zero---degenerate.
    - **No rescaling ($\times 1$):** The process $S_{\lfloor t/\Delta t\rfloor}$ has variance $T/\Delta t \to \infty$. The process diverges.
    - **Scaling by $\sqrt{\Delta t}$:** The process $\sqrt{\Delta t}\cdot S_{\lfloor t/\Delta t\rfloor}$ has variance $\Delta t \cdot T/\Delta t = T$, finite and non-zero. This is the only scaling that keeps the variance fixed at $T$.

    This connects to non-differentiability: Brownian motion satisfies $\operatorname{Var}(W_{t+h} - W_t) = h$, so $(W_{t+h} - W_t)/h$ has variance $1/h \to \infty$ as $h \to 0$. The "derivative" $dW_t/dt$ does not exist. The $\sqrt{\Delta t}$ scaling is the mathematical signature of this non-differentiability---the increment $\Delta W \sim \sqrt{\Delta t}$ is much larger than $\Delta t$, which is why $(dW_t)^2 = dt \neq 0$ in Ito calculus.
