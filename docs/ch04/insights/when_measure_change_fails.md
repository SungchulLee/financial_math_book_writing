# When Measure Change Fails


The machinery of Girsanov's theorem and risk-neutral pricing rests on precise
technical conditions. When these conditions are violated, the measure change
either produces an invalid probability measure or fails to be unique.
Understanding these failure modes is not merely a technical exercise---it
reveals the **boundaries of the no-arbitrage pricing framework** and connects
to economically meaningful phenomena such as asset price bubbles, incomplete
markets, and model risk.

!!! abstract "How to read this section"
    There are three main ways the framework fails:

    1. **The measure does not exist** --- Novikov/Kazamaki failure (mass leakage)
    2. **Prices are not martingales** --- strict local martingales (bubbles)
    3. **The measure is not unique** --- incomplete markets (pricing ambiguity)

    Two additional failure modes (infinite-horizon singularity, no ELMM)
    complete the catalog.

These failure modes are not pathologies---they correspond to economically
meaningful regimes. This section catalogs each mode and its financial
consequences.

---

## Failure Mode 1: Novikov and Kazamaki Conditions Violated

Girsanov's theorem requires the stochastic exponential

$$
Z_t = \exp\left(-\int_0^t \theta_s\,dW_s^{\mathbb{P}} - \frac{1}{2}\int_0^t \theta_s^2\,ds\right)
$$

to be a **true martingale** with $\mathbb{E}^{\mathbb{P}}[Z_T] = 1$.
As a non-negative local martingale, $Z_t$ is automatically a supermartingale
(Fatou's lemma). The danger is that $\mathbb{E}^{\mathbb{P}}[Z_T] < 1$---a
**strict local martingale**---so that $Z_T$ does not define a valid density.

The [Novikov condition](../martingale/novikov_kazamaki_conditions.md)

$$
\mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \theta_s^2\,ds\right)\right] < \infty
$$

and the weaker Kazamaki condition guarantee the true martingale property.
When both fail, mass "leaks to infinity" and the measure change is invalid:
the quadratic variation $\int_0^t \theta_s^2\,ds$ explodes, driving
$\mathcal{E}(M)_t$ toward zero in expectation. The **defect**

$$
\delta := 1 - \mathbb{E}^{\mathbb{P}}[Z_T] > 0
$$

measures the escaped mass. The normalized density
$Z_T / \mathbb{E}^{\mathbb{P}}[Z_T]$ defines a probability measure, but it
is **not equivalent** to $\mathbb{P}$: it ignores events where $Z_T = 0$.

### Example: Exploding Market Price of Risk

Consider $\theta_t = c / \sqrt{T - t}$ for $t < T$, where $c > 0$. Then

$$
\int_0^T \theta_s^2\,ds = \int_0^T \frac{c^2}{T - s}\,ds = +\infty
$$

The Novikov condition fails because the exponential of an infinite quantity
is infinite. As $t \to T$, the stochastic exponential $Z_t \to 0$ almost
surely, and $\mathbb{E}[Z_T] < 1$.

!!! warning "A market price of risk that blows up near maturity"
    This pathology arises in models where volatility vanishes or the drift
    becomes unbounded near a terminal time. It signals that the model's
    risk-neutral measure does not exist on the full interval $[0, T]$, and
    derivative prices computed via $\mathbb{E}^{\mathbb{Q}}$ are not
    well-defined.

---

## Failure Mode 2: Strict Local Martingales and Bubbles

### Intuition

Even when a risk-neutral measure $\mathbb{Q}$ exists, the discounted price
process $\tilde{S}_t = e^{-rt}S_t$ may fail to be a **true** $\mathbb{Q}$-martingale.
If $\tilde{S}_t$ is only a strict local martingale under $\mathbb{Q}$, then

$$
\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] < S_0
$$

The gap $S_0 - \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T]$ is interpreted as the
**bubble component** of the asset price: the current price exceeds the
discounted expected future payoff.

### Definition

**Definition (Asset Price Bubble).**
An asset price process $S_t$ exhibits a bubble if the discounted price
$\tilde{S}_t = S_t / B_t$ is a strict local martingale under an equivalent
local martingale measure $\mathbb{Q}$. The bubble size at time $t$ is

$$
\beta_t := S_t - B_t\,\mathbb{E}^{\mathbb{Q}}\!\left[\frac{S_T}{B_T}\;\middle|\;\mathcal{F}_t\right] > 0
$$

### Consequences for Derivatives Pricing

When bubbles are present:

1. **Put-call parity fails** in its classical form. The standard relationship
   $C - P = S_0 - Ke^{-rT}$ must be modified to account for the bubble.
2. **European call prices** may exceed the stock price, which is impossible
   in the standard Black-Scholes framework.
3. **American options** are no longer equivalent to European options for calls
   on non-dividend-paying stocks.

### Example: The CEV Model

The Constant Elasticity of Variance (CEV) model has dynamics

$$
dS_t = rS_t\,dt + \sigma S_t^{\beta}\,dW_t^{\mathbb{Q}}
$$

under the risk-neutral measure, where $\beta > 0$ is the elasticity parameter.

- For $\beta < 1$: The discounted price is a true martingale. No bubble.
- For $\beta = 1$: Geometric Brownian motion (Black-Scholes). No bubble.
- For $\beta > 1$: The discounted price is a **strict local martingale**. The
  process can reach infinity in finite time with positive probability, and
  the supermartingale property gives $\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] < S_0$.

### Example: Reciprocal of the 3D Bessel Process

The canonical mathematical example of a strict local martingale is
$X_t = 1/R_t$, where $R_t$ is the three-dimensional Bessel process
starting from $R_0 > 0$. By Ito's lemma:

$$
dX_t = -\frac{1}{R_t^2}\,dR_t + \frac{1}{R_t^3}\,dt
$$

Since $R_t$ satisfies $dR_t = \frac{1}{R_t}\,dt + dW_t$, substitution gives
$dX_t = -X_t^2\,dW_t$. This is a non-negative local martingale (no drift
term), and since $R_t \to \infty$ a.s., we have $X_t \to 0$ a.s. The
expectation $\mathbb{E}[X_t]$ is strictly decreasing, confirming that $X_t$ is
a strict local martingale. This process serves as the prototype for
understanding how mass leaks in financial models.

---

## Failure Mode 3: Incomplete Markets

### Intuition

The risk premium decomposition $\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}$
may have **no solution** or **infinitely many solutions**, depending on the
relationship between the number of assets $n$ and the number of risk
factors $d$. When the market is incomplete, the risk-neutral measure is not
unique, and derivative prices are not determined by no-arbitrage alone.

### The Mathematical Structure

Consider a market with $n$ traded assets and $d$ independent Brownian
motions, where $d > n$. The volatility matrix $\Sigma$ is $n \times d$ with
rank at most $n < d$.

The equation $\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}$
admits a family of solutions parameterized by $d - n$ free parameters. Each
valid $\boldsymbol{\theta}$ defines a different risk-neutral measure
$\mathbb{Q}^{\boldsymbol{\theta}}$ via Girsanov's theorem.

**Consequence:** For a non-traded contingent claim $\Phi(X_T)$, different
risk-neutral measures give different prices:

$$
V_0^{\boldsymbol{\theta}} = \mathbb{E}^{\mathbb{Q}^{\boldsymbol{\theta}}}\!\left[e^{-rT}\Phi(X_T)\right]
$$

The set of all such prices forms the **no-arbitrage pricing interval**
$[\underline{V}, \overline{V}]$, where

$$
\underline{V} = \inf_{\boldsymbol{\theta}} V_0^{\boldsymbol{\theta}}, \qquad \overline{V} = \sup_{\boldsymbol{\theta}} V_0^{\boldsymbol{\theta}}
$$

Any price within this interval is consistent with no-arbitrage. No-arbitrage
alone cannot determine a unique price.

### Example: Stochastic Volatility

In the Heston model, the stock and variance processes are

$$
dS_t = \mu S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^{1,\mathbb{P}}
$$

$$
dV_t = \kappa(\bar{V} - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{2,\mathbb{P}}
$$

There are two Brownian motions but only one traded asset ($S_t$). The
stock dynamics determine $\theta_1 = (\mu - r)/\sqrt{V_t}$, but $\theta_2$
(the **volatility risk premium**) is a free parameter because variance is
not directly traded.

Different choices of $\theta_2$ lead to different risk-neutral dynamics for
$V_t$:

$$
dV_t = \left[\kappa(\bar{V} - V_t) - \xi\sqrt{V_t}\,\theta_2\right]dt + \xi\sqrt{V_t}\,dW_t^{2,\mathbb{Q}}
$$

Each choice produces different option prices for volatility-sensitive
derivatives (e.g., variance swaps, VIX options). In practice, $\theta_2$
is determined by **calibration** to liquid option prices rather than by
no-arbitrage arguments. See
[Practitioner Perspective](practitioner_perspective.md) for how this
calibration is performed.

!!! note "The Second Fundamental Theorem"
    The Second Fundamental Theorem of Asset Pricing states:
    an arbitrage-free market is **complete** if and only if the equivalent
    local martingale measure is **unique**. Incomplete markets are precisely
    those with multiple valid risk-neutral measures.

---

## Failure Mode 4: Absolute Continuity Breaks Down

### The Problem

For Girsanov's theorem to apply, $\mathbb{Q}$ must be **equivalent** to
$\mathbb{P}$ (mutual absolute continuity): $\mathbb{P}(A) = 0 \iff \mathbb{Q}(A) = 0$.
On finite time intervals, this is typically ensured by the martingale property
of $Z_t$.

However, on **infinite time horizons** $[0, \infty)$, equivalence can fail.
Two probability measures that are equivalent on every $\mathcal{F}_T$ (for
finite $T$) may be **mutually singular** on $\mathcal{F}_{\infty}$.

### Example: Brownian Motion with Drift

Under $\mathbb{P}$, let $X_t = W_t$ (zero drift). Under $\mathbb{Q}$, let
$X_t = W_t + \theta t$ (constant drift $\theta \neq 0$).

- On $\mathcal{F}_T$ for any finite $T$: $\mathbb{Q} \sim \mathbb{P}$
  (Girsanov applies).
- On $\mathcal{F}_{\infty}$: By the law of large numbers,
  $X_t / t \to 0$ under $\mathbb{P}$ and $X_t / t \to \theta$ under
  $\mathbb{Q}$, almost surely. These events are disjoint, so
  $\mathbb{P} \perp \mathbb{Q}$ on $\mathcal{F}_{\infty}$.

!!! warning "Infinite-horizon pricing"
    This means risk-neutral pricing cannot be naively extended to perpetual
    claims without careful analysis. For perpetual American options and
    other infinite-horizon derivatives, one must work on finite horizons
    and take limits, verifying that the limit is well-behaved.

---

## Failure Mode 5: No Equivalent Martingale Measure Exists

### The Problem

The First Fundamental Theorem of Asset Pricing guarantees that an equivalent
local martingale measure exists if and only if there is no free lunch with
vanishing risk (NFLVR). If the market admits arbitrage, **no** equivalent
martingale measure exists, and the entire measure-change framework breaks down.

### When Does This Happen?

Arbitrage opportunities can arise from:

- **Model misspecification**: The assumed dynamics do not match reality,
  creating phantom arbitrage (e.g., assuming constant volatility when
  the true volatility has jumps).
- **Market frictions ignored**: Transaction costs, borrowing constraints,
  and short-selling restrictions invalidate the frictionless
  self-financing arguments underlying the FTAP.
- **Negative interest rates**: Some older models (e.g., lognormal short
  rate models) can produce negative rates with positive probability, potentially
  creating arbitrage if not handled carefully.

In these cases, one must either modify the model, weaken the no-arbitrage
condition (e.g., to "no arbitrage of the first kind"), or work with
super-replication and model-free bounds.

---

## Summary of Failure Modes

| Failure Mode | Technical Cause | Financial Consequence |
|---|---|---|
| Novikov/Kazamaki violated | $\mathbb{E}[Z_T] < 1$ | Invalid pricing measure |
| Strict local martingale | $\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] < S_0$ | Asset price bubbles |
| Incomplete market | $\boldsymbol{\theta}$ not unique | Pricing interval, not unique price |
| Infinite horizon | $\mathbb{P} \perp \mathbb{Q}$ on $\mathcal{F}_{\infty}$ | Perpetual claims ill-defined |
| No ELMM exists | Arbitrage present | Framework inapplicable |

---

## Implications for Practice

!!! tip "What practitioners actually worry about"
    Not all failure modes are equally relevant in day-to-day work. The most
    common in practice are: **(1)** incompleteness and the resulting model risk,
    **(2)** calibration inconsistency across instruments or maturities, and
    **(3)** extreme parameter regimes where Novikov-type conditions are close to
    failing. Bubbles and infinite-horizon singularities, while theoretically
    important, arise far less frequently.

Each failure mode has practical consequences:

1. **Model validation**: Before applying risk-neutral pricing, verify that
   the Novikov or Kazamaki condition holds for the chosen model. This is
   a non-negotiable prerequisite.
2. **Bubble detection**: If calibrated model parameters imply strict local
   martingale behavior, the model may be signaling a bubble or may simply
   be misspecified.
3. **Incomplete market pricing**: In stochastic volatility or jump models,
   the choice of $\boldsymbol{\theta}$ must be made explicit. Relying on
   calibration to liquid instruments effectively selects a particular
   risk-neutral measure from the family of valid measures.
4. **Horizon effects**: For long-dated derivatives, the near-singularity of
   $\mathbb{P}$ and $\mathbb{Q}$ means that risk-neutral probabilities can
   differ dramatically from physical probabilities, amplifying model risk.

For a discussion of how practitioners navigate these challenges, see
[Practitioner Perspective](practitioner_perspective.md). For the role of the
risk premium in determining the measure change, see
[Risk Premium Decomposition](risk_premium_decomposition.md).

---

## Exercises

**Exercise 1.**
Consider the market price of risk $\theta_t = c / \sqrt{T - t}$ for $t < T$. Verify that the Novikov condition fails by computing $\int_0^T \theta_s^2\,ds$ and showing it diverges. Explain in financial terms why a model with a market price of risk that blows up near maturity is problematic.

??? success "Solution to Exercise 1"
    Computing the integral:

    $$
    \int_0^T \theta_s^2\,ds = \int_0^T \frac{c^2}{T - s}\,ds
    $$

    Using the substitution $u = T - s$, $du = -ds$:

    $$
    \int_0^T \frac{c^2}{T - s}\,ds = c^2\int_0^T \frac{1}{u}\,du = c^2\left[\ln u\right]_{\epsilon}^{T} \to +\infty \text{ as } \epsilon \to 0
    $$

    Since $\int_0^T \theta_s^2\,ds = +\infty$, the Novikov condition requires

    $$
    \mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \theta_s^2\,ds\right)\right] < \infty
    $$

    but the integrand diverges, so the exponential is infinite and the condition fails.

    **Financial interpretation:** A market price of risk that blows up near maturity means the risk premium becomes unbounded as $t \to T$. This implies that the compensation required for bearing risk over the interval $[t, T]$ grows without bound as $t$ approaches $T$. In practical terms, the model would require infinitely aggressive reweighting of probabilities near the terminal time, which is economically unreasonable. The stochastic exponential $Z_t$ converges to zero almost surely, meaning the "probability measure" $\mathbb{Q}$ loses mass and cannot serve as a valid pricing measure on $[0, T]$. Any derivative prices computed under this $\mathbb{Q}$ would be unreliable or undefined.

---

**Exercise 2.**
Let $Z_t$ be the stochastic exponential defining the Radon–Nikodym derivative. Suppose $\mathbb{E}^{\mathbb{P}}[Z_T] = 0.95$. Compute the defect $\delta$ and explain why $Z_T / \mathbb{E}^{\mathbb{P}}[Z_T]$ does not define a measure equivalent to $\mathbb{P}$. Where has the "missing mass" gone?

??? success "Solution to Exercise 2"
    The defect is

    $$
    \delta = 1 - \mathbb{E}^{\mathbb{P}}[Z_T] = 1 - 0.95 = 0.05
    $$

    The normalized density $\tilde{Z}_T = Z_T / \mathbb{E}^{\mathbb{P}}[Z_T] = Z_T / 0.95$ integrates to 1 and thus defines a probability measure $\tilde{\mathbb{Q}}$. However, $\tilde{\mathbb{Q}}$ is **not equivalent** to $\mathbb{P}$.

    To see why, note that $Z_T \geq 0$ a.s. under $\mathbb{P}$. The fact that $\mathbb{E}[Z_T] < 1$ means that $Z_T$ is "smaller than it should be" on average---probability mass has leaked away. Technically, the event $\{Z_T = 0\}$ may have positive $\mathbb{P}$-probability, or more precisely, $Z_T$ may concentrate less mass on certain events than required for equivalence. The measure $\tilde{\mathbb{Q}}$ assigns zero probability to any event where $Z_T = 0$, but $\mathbb{P}$ may assign positive probability to such events, breaking mutual absolute continuity.

    The "missing mass" of $\delta = 0.05$ has escaped to infinity in the following sense: the stochastic exponential $Z_t$ is a supermartingale (not a true martingale), and its expected value decreases over time. The paths along which $Z_t$ becomes very small contribute less and less to the expectation. In financial terms, these are extreme paths (e.g., with very large positive Brownian increments) that the measure change attempts to downweight so aggressively that their contribution to the total probability vanishes. The resulting $\tilde{\mathbb{Q}}$ effectively ignores these extreme scenarios, which means it cannot correctly price claims that pay off in those states.

---

**Exercise 3.**
In the CEV model $dS_t = rS_t\,dt + \sigma S_t^{\beta}\,dW_t^{\mathbb{Q}}$, the discounted price process is a strict local martingale when $\beta > 1$. Show that the bubble component $\beta_0 = S_0 - \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] > 0$ in this case. Explain why put-call parity $C - P = S_0 - Ke^{-rT}$ must be modified when a bubble is present.

??? success "Solution to Exercise 3"
    When $\beta > 1$ in the CEV model, the discounted price process $\tilde{S}_t = e^{-rt}S_t$ is a strict local martingale under $\mathbb{Q}$. By the supermartingale property:

    $$
    \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T \mid \mathcal{F}_0] \leq S_0
    $$

    with strict inequality when $\tilde{S}_t$ is a strict local martingale. Therefore the bubble component is

    $$
    \beta_0 = S_0 - \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] > 0
    $$

    This means the current price $S_0$ exceeds the risk-neutral expected discounted future value. The difference is the bubble: the portion of the price not justified by the fundamental (discounted expected payoff).

    **Modification of put-call parity:** In the standard framework where $\tilde{S}_t$ is a true martingale, put-call parity states

    $$
    C - P = S_0 - Ke^{-rT}
    $$

    This derivation uses $\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] = S_0$. When a bubble is present, $\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] = S_0 - \beta_0 < S_0$. The call price is

    $$
    C = \mathbb{E}^{\mathbb{Q}}[e^{-rT}(S_T - K)^+]
    $$

    and the put price is

    $$
    P = \mathbb{E}^{\mathbb{Q}}[e^{-rT}(K - S_T)^+]
    $$

    Computing $C - P$:

    $$
    C - P = \mathbb{E}^{\mathbb{Q}}[e^{-rT}(S_T - K)] = \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] - Ke^{-rT} = (S_0 - \beta_0) - Ke^{-rT}
    $$

    So the modified put-call parity is $C - P = S_0 - Ke^{-rT} - \beta_0$, which differs from the standard formula by the bubble term $\beta_0$.

---

**Exercise 4.**
Consider the Heston model with stock dynamics $dS_t = \mu S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^{1,\mathbb{P}}$ and variance dynamics $dV_t = \kappa(\bar{V} - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{2,\mathbb{P}}$. Explain why $\theta_1$ is determined by no-arbitrage but $\theta_2$ is not. If a practitioner chooses $\theta_2 = 0$ vs $\theta_2 = -0.5$, describe qualitatively how the risk-neutral variance dynamics differ and which choice produces higher prices for out-of-the-money put options.

??? success "Solution to Exercise 4"
    **Why $\theta_1$ is determined:** The stock $S_t$ is traded, so no-arbitrage requires the discounted stock price to be a $\mathbb{Q}$-martingale. This pins down the drift removal for the Brownian motion $W^1$ driving stock returns. Specifically, the stock dynamics give $\mu - r = \sqrt{V_t}\,\theta_1$, so $\theta_1 = (\mu - r)/\sqrt{V_t}$.

    **Why $\theta_2$ is free:** The variance process $V_t$ is driven by $W^2$ but is not directly traded. There is no asset whose price depends solely on $W^2$ that would impose a no-arbitrage constraint on $\theta_2$. The volatility risk premium $\theta_2$ is therefore a free parameter, and each choice defines a different risk-neutral measure.

    **Comparing $\theta_2 = 0$ vs $\theta_2 = -0.5$:**

    With $\theta_2 = 0$, the risk-neutral variance dynamics are

    $$
    dV_t = \kappa(\bar{V} - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{2,\mathbb{Q}}
    $$

    With $\theta_2 = -0.5$, the dynamics become

    $$
    dV_t = \left[\kappa(\bar{V} - V_t) + 0.5\xi\sqrt{V_t}\right]dt + \xi\sqrt{V_t}\,dW_t^{2,\mathbb{Q}}
    $$

    The additional positive drift term $0.5\xi\sqrt{V_t}$ means that under $\theta_2 = -0.5$, the risk-neutral variance process has a higher mean level. Higher risk-neutral variance means fatter tails in the risk-neutral distribution of $S_T$. Out-of-the-money put options pay off in the left tail, so fatter tails increase their risk-neutral expected payoff. Therefore, $\theta_2 = -0.5$ produces **higher prices** for out-of-the-money puts compared to $\theta_2 = 0$.

    This is consistent with the empirical observation that the volatility risk premium is typically negative ($\theta_2 < 0$), which is necessary to generate the volatility skew observed in equity option markets.

---

**Exercise 5.**
Under $\mathbb{P}$, let $X_t = W_t$ (standard Brownian motion), and under $\mathbb{Q}$, let $X_t = W_t + \theta t$ for $\theta \neq 0$. Using the law of large numbers, show that $X_t / t \to 0$ $\mathbb{P}$-a.s. and $X_t / t \to \theta$ $\mathbb{Q}$-a.s. Conclude that $\mathbb{P} \perp \mathbb{Q}$ on $\mathcal{F}_{\infty}$ and explain the implication for pricing perpetual derivatives.

??? success "Solution to Exercise 5"
    Under $\mathbb{P}$, $X_t = W_t$ is a standard Brownian motion. By the strong law of large numbers for Brownian motion:

    $$
    \frac{X_t}{t} = \frac{W_t}{t} \to 0 \quad \mathbb{P}\text{-a.s.}
    $$

    Under $\mathbb{Q}$, $X_t = W_t + \theta t$ where $W_t$ is a $\mathbb{P}$-Brownian motion. Equivalently, $X_t = \tilde{W}_t + \theta t$ where $\tilde{W}_t = W_t$ is a standard Brownian motion under... but more directly:

    $$
    \frac{X_t}{t} = \frac{W_t}{t} + \theta \to \theta \quad \mathbb{Q}\text{-a.s.}
    $$

    because under $\mathbb{Q}$, $X_t - \theta t$ is a $\mathbb{Q}$-Brownian motion, so $(X_t - \theta t)/t \to 0$ $\mathbb{Q}$-a.s.

    Now define the events $A = \{\omega : X_t(\omega)/t \to 0\}$ and $B = \{\omega : X_t(\omega)/t \to \theta\}$. Since $\theta \neq 0$, these events are disjoint: $A \cap B = \emptyset$. We have $\mathbb{P}(A) = 1$ and $\mathbb{Q}(B) = 1$, so $\mathbb{P}(B) \leq \mathbb{P}(A^c) = 0$ and $\mathbb{Q}(A) \leq \mathbb{Q}(B^c) = 0$.

    Therefore $\mathbb{P}(B) = 0$ while $\mathbb{Q}(B) = 1$, which means $\mathbb{P}$ and $\mathbb{Q}$ are **mutually singular** on $\mathcal{F}_{\infty}$: $\mathbb{P} \perp \mathbb{Q}$.

    **Implication for perpetual derivatives:** Since $\mathbb{P}$ and $\mathbb{Q}$ are singular on $\mathcal{F}_{\infty}$, risk-neutral pricing via $\mathbb{E}^{\mathbb{Q}}[\cdot]$ cannot be directly applied to claims with infinite horizon. The equivalence of measures, which is essential for interpreting the risk-neutral expectation as an arbitrage-free price, breaks down. For perpetual American options or other infinite-horizon claims, one must work on finite horizons $[0, T]$ (where $\mathbb{P} \sim \mathbb{Q}$) and then carefully take the limit $T \to \infty$, verifying that convergence is well-behaved.

---

**Exercise 6.**
A model for an equity market assumes constant volatility and a constant positive risk-free rate, but through a calibration error the model parameters imply a negative forward variance for certain maturities. Explain which failure mode this represents, why no equivalent martingale measure can exist in this case, and what the practitioner should do to remedy the situation.

??? success "Solution to Exercise 6"
    This represents **Failure Mode 5: No equivalent martingale measure exists**.

    A negative forward variance means that the model implies $\sigma^2(t) < 0$ for some future time $t$. Since variance must be non-negative, this is a fundamental inconsistency in the model: no valid diffusion process can have negative instantaneous variance. The model's assumed dynamics are not well-defined, and the SDE describing the asset price process has no solution for those maturities.

    Without a well-defined asset price process, one cannot construct a risk-neutral measure. More precisely, the discounted price process cannot be expressed as a martingale under any equivalent measure because the process itself is not mathematically valid. The calibration error has produced model parameters that violate the basic conditions for the existence of an equivalent martingale measure.

    **Remedy:** The practitioner should:

    1. Re-examine the calibration procedure to identify the source of the error (e.g., interpolation of implied volatilities that produces a non-monotone total variance surface).
    2. Impose **arbitrage-free constraints** on the calibration: the total implied variance $\sigma_{\mathrm{imp}}^2(K, T) \cdot T$ must be non-decreasing in $T$ for each strike $K$ (calendar spread arbitrage condition).
    3. Use a model that guarantees non-negative variance by construction (e.g., the Heston model where the CIR dynamics ensure $V_t \geq 0$ under the Feller condition).

---

**Exercise 7.**
Consider a market with $n = 1$ traded asset and $d = 2$ Brownian motions. The stock dynamics are $dS_t = \mu S_t\,dt + \sigma_1 S_t\,dW_t^1 + \sigma_2 S_t\,dW_t^2$. The risk premium equation is $\mu - r = \sigma_1\theta_1 + \sigma_2\theta_2$, which defines a line in $(\theta_1, \theta_2)$ space. Parametrize the family of risk-neutral measures by writing $\theta_2$ as a function of $\theta_1$. For the claim $\Phi = (W_T^2)^2$, explain why different points on this line produce different prices.

??? success "Solution to Exercise 7"
    The risk premium equation $\mu - r = \sigma_1\theta_1 + \sigma_2\theta_2$ is a single linear equation in two unknowns. Solving for $\theta_2$:

    $$
    \theta_2 = \frac{\mu - r - \sigma_1\theta_1}{\sigma_2}
    $$

    This parametrizes the family of risk-neutral measures as a line in $(\theta_1, \theta_2)$ space. Each point on this line defines a different $\boldsymbol{\theta} = (\theta_1, \theta_2)$ and hence a different risk-neutral measure $\mathbb{Q}^{\boldsymbol{\theta}}$ via Girsanov's theorem.

    Under any choice of $\boldsymbol{\theta}$, the risk-neutral Brownian motions are

    $$
    W_t^{i,\mathbb{Q}} = W_t^{i,\mathbb{P}} + \theta_i t, \quad i = 1, 2
    $$

    The claim $\Phi = (W_T^2)^2$ depends on the second Brownian motion. Under $\mathbb{Q}^{\boldsymbol{\theta}}$:

    $$
    W_T^{2,\mathbb{P}} = W_T^{2,\mathbb{Q}} - \theta_2 T
    $$

    But the claim is written on $W_T^2 = W_T^{2,\mathbb{P}}$, so

    $$
    \Phi = (W_T^{2,\mathbb{P}})^2 = (W_T^{2,\mathbb{Q}} - \theta_2 T)^2
    $$

    The price is

    $$
    V_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}\!\left[(W_T^{2,\mathbb{Q}} - \theta_2 T)^2\right]
    $$

    Since $W_T^{2,\mathbb{Q}} \sim N(0, T)$ under $\mathbb{Q}$:

    $$
    V_0 = e^{-rT}\left[\mathbb{E}^{\mathbb{Q}}[(W_T^{2,\mathbb{Q}})^2] - 2\theta_2 T\,\mathbb{E}^{\mathbb{Q}}[W_T^{2,\mathbb{Q}}] + \theta_2^2 T^2\right] = e^{-rT}(T + \theta_2^2 T^2)
    $$

    Since $\theta_2 = (\mu - r - \sigma_1\theta_1)/\sigma_2$ depends on the free parameter $\theta_1$, different points on the line give different values of $\theta_2$ and hence different prices. The claim $\Phi = (W_T^2)^2$ has exposure to the second Brownian motion, which is not hedgeable using the single traded asset. This unhedgeable risk is priced differently by each risk-neutral measure, producing the pricing interval characteristic of incomplete markets.
