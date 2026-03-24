# When Measure Change Fails


The machinery of Girsanov's theorem and risk-neutral pricing rests on precise
technical conditions. When these conditions are violated, the measure change
either produces an invalid probability measure or fails to be unique.
Understanding these failure modes is not merely a technical exercise---it
reveals the **boundaries of the no-arbitrage pricing framework** and connects
to economically meaningful phenomena such as asset price bubbles, incomplete
markets, and model risk.

This section catalogs the principal ways in which measure change can fail and
their financial consequences.

---

## Failure Mode 1: Novikov and Kazamaki Conditions Violated

### Intuition

Girsanov's theorem requires the stochastic exponential

$$
Z_t = \exp\left(-\int_0^t \theta_s\,dW_s^{\mathbb{P}} - \frac{1}{2}\int_0^t \theta_s^2\,ds\right)
$$

to be a **true martingale** with $\mathbb{E}^{\mathbb{P}}[Z_T] = 1$. Since
$Z_t$ is always a non-negative local martingale, it is automatically a
supermartingale by Fatou's lemma. The danger is that it may be a **strict
local martingale**, meaning $\mathbb{E}^{\mathbb{P}}[Z_T] < 1$, so that $Z_T$
does not define a valid probability density.

The [Novikov condition](../martingale_foundations/novikov_kazamaki_conditions.md)

$$
\mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \theta_s^2\,ds\right)\right] < \infty
$$

and the weaker Kazamaki condition provide sufficient guarantees. When
**both** fail, mass can "leak to infinity," and the measure change is invalid.

### The Mechanism of Mass Leakage

When $\theta_t$ grows too fast, the Brownian integral $M_t = \int_0^t \theta_s\,dW_s$
has explosively growing quadratic variation $\langle M \rangle_t = \int_0^t \theta_s^2\,ds$.
The stochastic exponential $\mathcal{E}(M)_t$ can then drift toward zero
in expectation even though it remains strictly positive pathwise. The "missing
mass" $1 - \mathbb{E}[Z_T]$ represents probability that has escaped to infinity.

Formally, if $Z_t$ is a strict local martingale, define the **defect**:

$$
\delta := 1 - \mathbb{E}^{\mathbb{P}}[Z_T] > 0
$$

The quantity $Z_T / \mathbb{E}^{\mathbb{P}}[Z_T]$ defines a probability
measure, but it is **not equivalent** to $\mathbb{P}$: it assigns zero
probability to events where $Z_T = 0$, which can occur in the limit.

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

---

**Exercise 2.**
Let $Z_t$ be the stochastic exponential defining the Radon-Nikodym derivative. Suppose $\mathbb{E}^{\mathbb{P}}[Z_T] = 0.95$. Compute the defect $\delta$ and explain why $Z_T / \mathbb{E}^{\mathbb{P}}[Z_T]$ does not define a measure equivalent to $\mathbb{P}$. Where has the "missing mass" gone?

---

**Exercise 3.**
In the CEV model $dS_t = rS_t\,dt + \sigma S_t^{\beta}\,dW_t^{\mathbb{Q}}$, the discounted price process is a strict local martingale when $\beta > 1$. Show that the bubble component $\beta_0 = S_0 - \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] > 0$ in this case. Explain why put-call parity $C - P = S_0 - Ke^{-rT}$ must be modified when a bubble is present.

---

**Exercise 4.**
Consider the Heston model with stock dynamics $dS_t = \mu S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^{1,\mathbb{P}}$ and variance dynamics $dV_t = \kappa(\bar{V} - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{2,\mathbb{P}}$. Explain why $\theta_1$ is determined by no-arbitrage but $\theta_2$ is not. If a practitioner chooses $\theta_2 = 0$ vs $\theta_2 = -0.5$, describe qualitatively how the risk-neutral variance dynamics differ and which choice produces higher prices for out-of-the-money put options.

---

**Exercise 5.**
Under $\mathbb{P}$, let $X_t = W_t$ (standard Brownian motion), and under $\mathbb{Q}$, let $X_t = W_t + \theta t$ for $\theta \neq 0$. Using the law of large numbers, show that $X_t / t \to 0$ $\mathbb{P}$-a.s. and $X_t / t \to \theta$ $\mathbb{Q}$-a.s. Conclude that $\mathbb{P} \perp \mathbb{Q}$ on $\mathcal{F}_{\infty}$ and explain the implication for pricing perpetual derivatives.

---

**Exercise 6.**
A model for an equity market assumes constant volatility and a constant positive risk-free rate, but through a calibration error the model parameters imply a negative forward variance for certain maturities. Explain which failure mode this represents, why no equivalent martingale measure can exist in this case, and what the practitioner should do to remedy the situation.

---

**Exercise 7.**
Consider a market with $n = 1$ traded asset and $d = 2$ Brownian motions. The stock dynamics are $dS_t = \mu S_t\,dt + \sigma_1 S_t\,dW_t^1 + \sigma_2 S_t\,dW_t^2$. The risk premium equation is $\mu - r = \sigma_1\theta_1 + \sigma_2\theta_2$, which defines a line in $(\theta_1, \theta_2)$ space. Parametrize the family of risk-neutral measures by writing $\theta_2$ as a function of $\theta_1$. For the claim $\Phi = (W_T^2)^2$, explain why different points on this line produce different prices.
