# When Measure Change Fails

The risk-neutral pricing formula breaks when its hypotheses break.
The measure $\mathbb{Q}$ must exist, be equivalent to $\mathbb{P}$, and make
discounted prices true martingales. Each condition can fail, and each failure
corresponds to an economically meaningful phenomenon---bubbles, incomplete
markets, or model misspecification. This section catalogs the five failure
modes and their financial consequences.

!!! abstract "The five failure modes"
    1. **Novikov/Kazamaki violated** --- mass leaks, pricing measure invalid
    2. **Strict local martingale** --- bubbles, put-call parity breaks
    3. **Incomplete market** --- pricing interval, not a unique price
    4. **Infinite-horizon singularity** --- $\mathbb{P} \perp \mathbb{Q}$ on $\mathcal{F}_\infty$
    5. **No ELMM exists** --- arbitrage present, framework inapplicable

!!! note "Scope"
    This is advanced material that marks the boundaries of the pricing
    framework. It assumes familiarity with the core pricing sections and
    the [Practitioner Perspective](practitioner_perspective.md).

---

## Failure Mode 1: Novikov and Kazamaki Conditions Violated

Girsanov's theorem requires the Radon-Nikodym density process

$$
Z_t = \exp\!\left(-\int_0^t \theta_s\,dW_s^{\mathbb{P}} - \frac{1}{2}\int_0^t \theta_s^2\,ds\right)
$$

to satisfy $\mathbb{E}^{\mathbb{P}}[Z_T] = 1$. As a non-negative local
martingale, $Z_t$ is automatically a supermartingale. The danger is
$\mathbb{E}^{\mathbb{P}}[Z_T] < 1$---a strict local martingale---so that
$Z_T$ fails to define a valid density.

The Novikov condition

$$
\mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \theta_s^2\,ds\right)\right] < \infty
$$

guarantees the true martingale property. When it fails, mass leaks to
infinity: the quadratic variation $\int_0^t \theta_s^2\,ds$ explodes,
driving $Z_t$ toward zero. The **defect**

$$
\delta := 1 - \mathbb{E}^{\mathbb{P}}[Z_T] > 0
$$

measures the escaped mass. The normalized density
$Z_T / \mathbb{E}^{\mathbb{P}}[Z_T]$ defines a probability measure, but one
that is **not equivalent** to $\mathbb{P}$: it ignores events where
$Z_T = 0$.

### Example: Exploding Market Price of Risk

Take $\theta_t = c / \sqrt{T - t}$ for $t < T$. Then

$$
\int_0^T \theta_s^2\,ds = \int_0^T \frac{c^2}{T - s}\,ds = +\infty
$$

The Novikov condition fails. As $t \to T$, the stochastic exponential
$Z_t \to 0$ a.s., and $\mathbb{E}[Z_T] < 1$.

!!! warning "Pathological market price of risk"
    A market price of risk that blows up near maturity signals that the
    model's risk-neutral measure does not exist on the full interval
    $[0, T]$. Derivative prices computed via $\mathbb{E}^{\mathbb{Q}}$
    are not well-defined.

---

## Failure Mode 2: Strict Local Martingales and Bubbles

Even when $\mathbb{Q}$ exists, the discounted price $\tilde{S}_t = e^{-rt}S_t$
may fail to be a true $\mathbb{Q}$-martingale. If $\tilde{S}_t$ is only a
strict local martingale, then

$$
\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] < S_0
$$

The gap is the **bubble component**: the current price exceeds the discounted
expected future payoff.

**Definition (Asset Price Bubble).**
The asset $S_t$ exhibits a bubble if $\tilde{S}_t = S_t / B_t$ is a strict
local martingale under an equivalent local martingale measure $\mathbb{Q}$.
The bubble size at time $t$ is

$$
\beta_t := S_t - B_t\,\mathbb{E}^{\mathbb{Q}}\!\left[\frac{S_T}{B_T}\;\middle|\;\mathcal{F}_t\right] > 0
$$

### Consequences for Pricing

1. **Put-call parity fails** in its classical form: $C - P = S_0 - Ke^{-rT}$
   must be corrected by $\beta_0$.
2. **European calls** may exceed the stock price.
3. **American calls** on non-dividend-paying stocks may be worth more than
   their European counterparts.

### Example: CEV Model

The Constant Elasticity of Variance model has dynamics

$$
dS_t = rS_t\,dt + \sigma S_t^{\beta}\,dW_t^{\mathbb{Q}}
$$

- $\beta \leq 1$: discounted price is a true martingale. No bubble.
- $\beta > 1$: discounted price is a strict local martingale. The process
  can reach infinity in finite time, and the supermartingale property gives
  $\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] < S_0$.

### Example: Reciprocal of the 3D Bessel Process

The canonical strict local martingale is $X_t = 1/R_t$, where $R_t$ is the
three-dimensional Bessel process with $R_0 > 0$. Substituting
$dR_t = (1/R_t)\,dt + dW_t$ into Ito's formula gives $dX_t = -X_t^2\,dW_t$.
This is a non-negative driftless local martingale. Since $R_t \to \infty$
a.s., $X_t \to 0$ a.s. and $\mathbb{E}[X_t]$ is strictly decreasing---the
prototype for mass leakage in financial models.

---

## Failure Mode 3: Incomplete Markets

When there are more risk factors than traded assets, the risk premium equation
$\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}$ has infinitely
many solutions. Each solution defines a different risk-neutral measure, and
derivative prices are no longer uniquely determined by no-arbitrage.

### Mathematical Structure

With $n$ traded assets, $d > n$ independent Brownian motions, and an
$n \times d$ volatility matrix $\Sigma$ of rank $n$, the equation admits
a $(d - n)$-parameter family of solutions. For a non-traded claim
$\Phi(X_T)$, each $\boldsymbol{\theta}$ produces a different price:

$$
V_0^{\boldsymbol{\theta}} = \mathbb{E}^{\mathbb{Q}^{\boldsymbol{\theta}}}\!\left[e^{-rT}\Phi(X_T)\right]
$$

The set of all such prices forms the **no-arbitrage pricing interval**

$$
\underline{V} = \inf_{\boldsymbol{\theta}} V_0^{\boldsymbol{\theta}}, \qquad \overline{V} = \sup_{\boldsymbol{\theta}} V_0^{\boldsymbol{\theta}}
$$

Any price in $[\underline{V}, \overline{V}]$ is consistent with no-arbitrage.

### Example: Stochastic Volatility (Heston)

$$
dS_t = \mu S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^{1,\mathbb{P}}
$$

$$
dV_t = \kappa(\bar{V} - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{2,\mathbb{P}}
$$

Two Brownian motions, one traded asset. No-arbitrage pins down
$\theta_1 = (\mu - r)/\sqrt{V_t}$, but the volatility risk premium
$\theta_2$ is free. Different choices of $\theta_2$ yield different
risk-neutral variance dynamics:

$$
dV_t = \left[\kappa(\bar{V} - V_t) - \xi\sqrt{V_t}\,\theta_2\right]dt + \xi\sqrt{V_t}\,dW_t^{2,\mathbb{Q}}
$$

In practice, $\theta_2$ is determined by calibration to liquid options, not
by no-arbitrage. See
[Practitioner Perspective](practitioner_perspective.md).

!!! note "The Second Fundamental Theorem"
    An arbitrage-free market is **complete** if and only if the equivalent
    local martingale measure is **unique**. Incomplete markets are precisely
    those with multiple valid risk-neutral measures.

---

## Failure Mode 4: Absolute Continuity Breaks on Infinite Horizons

On finite intervals, Girsanov's theorem ensures $\mathbb{Q} \sim \mathbb{P}$.
On infinite horizons, two measures that are equivalent on every
$\mathcal{F}_T$ can become **mutually singular** on $\mathcal{F}_\infty$.

### Example: Brownian Motion with Drift

Under $\mathbb{P}$, let $X_t = W_t$. Under $\mathbb{Q}$, let
$X_t = W_t + \theta t$ with $\theta \neq 0$.

- On $\mathcal{F}_T$ for any finite $T$: $\mathbb{Q} \sim \mathbb{P}$.
- On $\mathcal{F}_\infty$: by the law of large numbers,
  $X_t / t \to 0$ $\mathbb{P}$-a.s. and $X_t / t \to \theta$
  $\mathbb{Q}$-a.s. These events are disjoint, so
  $\mathbb{P} \perp \mathbb{Q}$.

!!! warning "Infinite-horizon pricing"
    Risk-neutral pricing cannot be naively extended to perpetual claims.
    For perpetual American options, one must work on finite horizons and
    take limits, verifying convergence at each step.

---

## Failure Mode 5: No Equivalent Martingale Measure Exists

The First Fundamental Theorem guarantees that an equivalent local martingale
measure exists if and only if NFLVR (no free lunch with vanishing risk) holds.
If the market admits arbitrage, no such measure exists and the framework is
inapplicable.

### When This Happens

- **Model misspecification**: assumed dynamics create phantom arbitrage
  (e.g., constant volatility when the true process has jumps).
- **Ignored frictions**: transaction costs, borrowing constraints, and
  short-selling restrictions invalidate the frictionless self-financing
  arguments underlying FTAP.
- **Calibration errors**: parameters that imply negative forward variance
  make the SDE ill-defined.

In these cases, one must modify the model, weaken the no-arbitrage condition,
or resort to super-replication and model-free bounds.

---

## Summary of Failure Modes

| Failure Mode | Technical Cause | Financial Consequence |
|---|---|---|
| Novikov/Kazamaki violated | $\mathbb{E}[Z_T] < 1$ | Invalid pricing measure |
| Strict local martingale | $\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] < S_0$ | Asset price bubbles |
| Incomplete market | $\boldsymbol{\theta}$ not unique | Pricing interval, not unique price |
| Infinite horizon | $\mathbb{P} \perp \mathbb{Q}$ on $\mathcal{F}_\infty$ | Perpetual claims ill-defined |
| No ELMM exists | Arbitrage present | Framework inapplicable |

!!! tip "What practitioners worry about most"
    The most common failure modes in day-to-day work are **(1)** incompleteness
    and the resulting model risk, **(2)** calibration inconsistency across
    instruments, and **(3)** extreme parameter regimes where Novikov-type
    conditions are close to failing. Bubbles and infinite-horizon singularities
    are theoretically important but arise less frequently in practice.

---

## Exercises

**Exercise 1.**
Consider the market price of risk $\theta_t = c / \sqrt{T - t}$ for $t < T$. Verify that the Novikov condition fails by computing $\int_0^T \theta_s^2\,ds$. Explain in financial terms why a model with a market price of risk that blows up near maturity is problematic.

??? success "Solution to Exercise 1"
    Computing the integral via $u = T - s$:

    $$
    \int_0^T \theta_s^2\,ds = \int_0^T \frac{c^2}{T - s}\,ds = c^2 \int_0^T \frac{du}{u} = c^2 [\ln u]_{\epsilon}^{T} \to +\infty
    $$

    Since the integral diverges, $\exp\!\left(\frac{1}{2}\int_0^T \theta_s^2\,ds\right) = +\infty$ and the Novikov condition fails.

    **Financial interpretation.** A market price of risk that blows up near maturity requires unbounded probability reweighting as $t \to T$. The stochastic exponential $Z_t \to 0$ a.s., meaning the "measure" $\mathbb{Q}$ loses mass and cannot serve as a valid pricing measure on $[0,T]$. Derivative prices computed under this $\mathbb{Q}$ are undefined.

---

**Exercise 2.**
Suppose $\mathbb{E}^{\mathbb{P}}[Z_T] = 0.95$. Compute the defect $\delta$ and explain why $Z_T / \mathbb{E}^{\mathbb{P}}[Z_T]$ does not define a measure equivalent to $\mathbb{P}$.

??? success "Solution to Exercise 2"
    The defect is

    $$
    \delta = 1 - \mathbb{E}^{\mathbb{P}}[Z_T] = 1 - 0.95 = 0.05
    $$

    The normalized density $\tilde{Z}_T = Z_T / 0.95$ integrates to 1 and defines a probability measure $\tilde{\mathbb{Q}}$. However, $\tilde{\mathbb{Q}}$ is **not equivalent** to $\mathbb{P}$ because $Z_T$ is a supermartingale (not a true martingale) and the event $\{Z_T = 0\}$ may have positive $\mathbb{P}$-probability. The measure $\tilde{\mathbb{Q}}$ assigns zero probability to any event where $Z_T = 0$, while $\mathbb{P}$ may assign positive probability to such events, breaking mutual absolute continuity.

    The missing mass of $\delta = 0.05$ has escaped along extreme paths where $Z_t$ was driven to zero by explosive quadratic variation. The resulting $\tilde{\mathbb{Q}}$ ignores these scenarios, so it cannot correctly price claims that pay off in those states.

---

**Exercise 3.**
In the CEV model with $\beta > 1$, show that the bubble component $\beta_0 = S_0 - \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] > 0$. Derive the modified put-call parity when a bubble is present.

??? success "Solution to Exercise 3"
    When $\beta > 1$, the discounted price $\tilde{S}_t = e^{-rt}S_t$ is a strict local martingale under $\mathbb{Q}$. By the supermartingale property:

    $$
    \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] \leq S_0
    $$

    with strict inequality, so $\beta_0 = S_0 - \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] > 0$.

    **Modified put-call parity.** The call and put prices are $C = \mathbb{E}^{\mathbb{Q}}[e^{-rT}(S_T - K)^+]$ and $P = \mathbb{E}^{\mathbb{Q}}[e^{-rT}(K - S_T)^+]$. Then

    $$
    C - P = \mathbb{E}^{\mathbb{Q}}[e^{-rT}(S_T - K)] = \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] - Ke^{-rT} = (S_0 - \beta_0) - Ke^{-rT}
    $$

    The modified relation is $C - P = S_0 - Ke^{-rT} - \beta_0$, differing from the standard formula by the bubble term.

---

**Exercise 4.**
In the Heston model, explain why $\theta_1$ is determined by no-arbitrage but $\theta_2$ is not. If $\theta_2 = 0$ vs $\theta_2 = -0.5$, which choice produces higher out-of-the-money put prices?

??? success "Solution to Exercise 4"
    **$\theta_1$ is pinned down** because $S_t$ is traded: no-arbitrage requires the discounted stock to be a $\mathbb{Q}$-martingale, giving $\theta_1 = (\mu - r)/\sqrt{V_t}$.

    **$\theta_2$ is free** because $V_t$ is not traded. No asset depends solely on $W^2$, so no no-arbitrage constraint determines $\theta_2$.

    With $\theta_2 = 0$, the risk-neutral variance dynamics are unchanged from $\mathbb{P}$. With $\theta_2 = -0.5$:

    $$
    dV_t = \left[\kappa(\bar{V} - V_t) + 0.5\xi\sqrt{V_t}\right]dt + \xi\sqrt{V_t}\,dW_t^{2,\mathbb{Q}}
    $$

    The additional positive drift raises the risk-neutral mean variance, producing fatter tails in the distribution of $S_T$. Out-of-the-money puts pay off in the left tail, so $\theta_2 = -0.5$ produces **higher OTM put prices**. This is consistent with the empirically negative volatility risk premium needed to generate the equity skew.

---

**Exercise 5.**
Show that $\mathbb{P} \perp \mathbb{Q}$ on $\mathcal{F}_\infty$ when $X_t = W_t$ under $\mathbb{P}$ and $X_t = W_t + \theta t$ under $\mathbb{Q}$ with $\theta \neq 0$. What does this imply for pricing perpetual derivatives?

??? success "Solution to Exercise 5"
    By the strong law of large numbers for Brownian motion:

    - Under $\mathbb{P}$: $X_t / t = W_t / t \to 0$ a.s.
    - Under $\mathbb{Q}$: $X_t / t = (W_t + \theta t)/t \to \theta$ a.s.

    Define $A = \{\omega : X_t/t \to 0\}$ and $B = \{\omega : X_t/t \to \theta\}$. Since $\theta \neq 0$, $A \cap B = \emptyset$. We have $\mathbb{P}(A) = 1$ and $\mathbb{Q}(B) = 1$, so $\mathbb{P}(B) = 0$ and $\mathbb{Q}(A) = 0$. Therefore $\mathbb{P} \perp \mathbb{Q}$ on $\mathcal{F}_\infty$.

    **Implication.** Since equivalence breaks on $\mathcal{F}_\infty$, risk-neutral pricing cannot be directly applied to perpetual claims. For perpetual American options, one must work on finite horizons $[0, T]$ where $\mathbb{P} \sim \mathbb{Q}$ and carefully take $T \to \infty$, verifying convergence at each step.

---

**Exercise 6.**
A calibration error produces negative forward variance for certain maturities. Identify the failure mode, explain why no equivalent martingale measure exists, and describe the remedy.

??? success "Solution to Exercise 6"
    This is **Failure Mode 5: no ELMM exists**.

    Negative forward variance means $\sigma^2(t) < 0$ for some $t$, which is undefined for a diffusion process. The SDE has no solution, so no price process exists and no equivalent martingale measure can be constructed.

    **Remedy:**

    1. Re-examine interpolation to find the source of the error.
    2. Impose arbitrage-free constraints: total implied variance $\sigma_{\mathrm{imp}}^2(K,T) \cdot T$ must be non-decreasing in $T$ for each $K$ (calendar spread condition).
    3. Use models that guarantee non-negative variance by construction (e.g., Heston with Feller condition).
