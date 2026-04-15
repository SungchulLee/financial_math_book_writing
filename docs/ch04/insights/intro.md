# Measure Change and Financial Interpretation

The previous sections established how to construct the risk-neutral measure
$\mathbb{Q}$ using Girsanov’s theorem and the Radon--Nikodym derivative. This
section answers the next natural question:

> **What do we do with $\mathbb{Q}$?**

The answer is pricing. Under $\mathbb{Q}$, the value of any contingent claim
is a discounted expectation, and the complex problem of derivative valuation
reduces to computing an integral. Everything else in this section is
commentary on that fact: what the formula means, why it works, and where
it breaks down.

---

## The Central Formula

The risk-neutral valuation principle states that the time-$0$ price of a
contingent claim with payoff $X_T$ at maturity $T$ is

$$
V_0 = \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\,X_T\right]
$$

where the expectation is taken under the risk-neutral measure $\mathbb{Q}$
and $r_s$ is the instantaneous risk-free rate. When $r$ is constant, this
simplifies to

$$
V_0 = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}[X_T]
$$

> Pricing = expectation under the measure that makes discounted prices
> martingales.

---

## Core Topics

The essential content focuses on three questions:

1. **What is the difference between $\mathbb{P}$ and $\mathbb{Q}$?**
   The [physical vs risk-neutral world](physical_vs_risk_neutral.md)
   clarifies the roles of the two measures and why they must not be confused.

2. **Where does the risk premium go?**
   The [risk premium decomposition](risk_premium_decomposition.md) shows
   how Girsanov’s theorem absorbs the excess return $\mu - r$ into the
   measure change, leaving only the risk-free drift under $\mathbb{Q}$.

3. **What is the difference between pricing and hedging?**
   [Pricing vs hedging](pricing_vs_hedging.md) explains that pricing is
   an expectation under $\mathbb{Q}$, while hedging is a pathwise
   replication that does not depend on the choice of measure.

---

## Deeper Perspectives

The remaining topics extend the pricing framework in different directions:

* The [stochastic discount factor](sdf.md) provides the economic
  foundation --- it explains *why* the risk-neutral measure exists by
  connecting measure change to investor preferences and marginal utility.

* [From SDF to CAPM](sdf_to_capm.md) shows that equilibrium asset pricing
  models (CAPM, factor models) are special cases of the same structure.

* The [practitioner perspective](practitioner_perspective.md) examines how
  the theoretical framework is actually used: calibration, model risk,
  discrete hedging, and the implied volatility surface.

* [When measure change fails](when_measure_change_fails.md) catalogs the
  failure modes --- Novikov violation, strict local martingales (bubbles),
  incomplete markets --- that mark the boundaries of the framework.

---

## Guiding Principle

> The physical measure describes reality.
> The risk-neutral measure prices claims in it.

The risk premium decomposition explains what the measure change removes;
pricing vs hedging explains what it does and does not affect; the SDF
explains why it works economically; and the failure modes show where
it breaks down.

---

## Exercises

**Exercise 1.**
A stock follows geometric Brownian motion under $\mathbb{P}$ with drift
$\mu = 0.12$, volatility $\sigma = 0.20$, and risk-free rate $r = 0.03$.
Using the risk-neutral valuation formula, compute the price of a
derivative that pays $S_T^2$ at time $T = 1$ (take $S_0 = 1$).

??? success "Solution to Exercise 1"
    Under $\mathbb{Q}$, the stock dynamics are $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$, so

    $$
    S_T = S_0 \exp\!\left[\left(r - \tfrac{1}{2}\sigma^2\right)T + \sigma W_T^{\mathbb{Q}}\right]
    $$

    Therefore

    $$
    S_T^2 = S_0^2 \exp\!\left[2\left(r - \tfrac{1}{2}\sigma^2\right)T + 2\sigma W_T^{\mathbb{Q}}\right]
    $$

    Since $W_T^{\mathbb{Q}} \sim N(0, T)$ under $\mathbb{Q}$, the moment generating function gives

    $$
    \mathbb{E}^{\mathbb{Q}}[S_T^2] = S_0^2 \exp\!\left[2\left(r - \tfrac{1}{2}\sigma^2\right)T + \tfrac{1}{2}(2\sigma)^2 T\right] = S_0^2 \exp\!\left[(2r + \sigma^2)T\right]
    $$

    The price is

    $$
    V_0 = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}[S_T^2] = S_0^2 \exp\!\left[(r + \sigma^2)T\right]
    $$

    Substituting $S_0 = 1$, $r = 0.03$, $\sigma = 0.20$, $T = 1$:

    $$
    V_0 = \exp(0.03 + 0.04) = e^{0.07} \approx 1.0725
    $$

    The physical drift $\mu = 0.12$ does not appear --- only $r$ and $\sigma$ determine the price.

---

**Exercise 2.**
A colleague argues that a stock with higher expected return $\mu$ should
produce more expensive call options. Using the risk-neutral valuation
formula, identify the error in this reasoning and explain why derivative
prices are independent of $\mu$.

??? success "Solution to Exercise 2"
    The risk-neutral valuation formula computes an expectation under $\mathbb{Q}$, where
    the stock dynamics are $dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}$.
    Girsanov’s theorem absorbs the physical drift $\mu$ into the change of
    measure: the Radon--Nikodym derivative depends on $\theta = (\mu - r)/\sigma$,
    but once we compute under $\mathbb{Q}$, only $r$ and $\sigma$ remain.

    The colleague’s error is confusing the physical measure $\mathbb{P}$ with
    the pricing measure $\mathbb{Q}$. Under $\mathbb{P}$, a higher $\mu$ means
    the stock is more likely to reach higher values. But pricing uses
    $\mathbb{Q}$, where every stock has drift $r$ regardless of its physical
    drift. A higher $\mu$ changes the Radon--Nikodym derivative (reweighting
    paths more aggressively) but does not change the risk-neutral distribution
    of $S_T$. Therefore option prices are independent of $\mu$.

    This is the fundamental insight of Black--Scholes: option prices depend on
    volatility and the risk-free rate, not on the expected return of the
    underlying.

---

**Exercise 3.**
In the risk-neutral valuation formula with stochastic rates, the discount
factor is $e^{-\int_0^T r_s\,ds}$. Explain why discounting at the
path-dependent rate $r_s$ is necessary rather than at a fixed rate. What
goes wrong if one discounts at $\bar{r} = \mathbb{E}^{\mathbb{Q}}[\frac{1}{T}\int_0^T r_s\,ds]$ instead?

??? success "Solution to Exercise 3"
    The discount factor $e^{-\int_0^T r_s\,ds}$ appears because the
    money market account $B_t = e^{\int_0^t r_s\,ds}$ is the numéraire. The
    discounted price process $V_t / B_t$ must be a $\mathbb{Q}$-martingale,
    which requires discounting at the actual realized path of short rates,
    not at their expected value.

    Replacing the stochastic discount factor with a deterministic one introduces
    an error because

    $$
    e^{-\bar{r}T} \neq \mathbb{E}^{\mathbb{Q}}\!\left[e^{-\int_0^T r_s\,ds}\right]
    $$

    by Jensen’s inequality (since the exponential is convex). More importantly,
    the correct formula $V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-\int_0^T r_s\,ds}\,X_T]$
    captures the covariance between the discount factor and the payoff. When
    interest rates and the payoff are correlated (as they generally are when
    rates affect asset prices), replacing the stochastic discount with a constant
    ignores this covariance and misprices the claim.

---

**Exercise 4.**
Consider a European call with payoff $(S_T - K)^+$ and a digital option
with payoff $\mathbf{1}_{S_T > K}$. Write the risk-neutral pricing formula
for each. Then show that $\partial C / \partial K = -e^{-rT}\,\mathbb{Q}(S_T > K)$, where $C$ is the call price.

??? success "Solution to Exercise 4"
    The risk-neutral prices are

    $$
    C = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+], \qquad D = e^{-rT}\,\mathbb{E}^{\mathbb{Q}}[\mathbf{1}_{S_T > K}] = e^{-rT}\,\mathbb{Q}(S_T > K)
    $$

    Write the call price as an integral over the risk-neutral density $q(s)$ of $S_T$:

    $$
    C = e^{-rT}\int_K^{\infty}(s - K)\,q(s)\,ds
    $$

    Differentiating under the integral with respect to $K$:

    $$
    \frac{\partial C}{\partial K} = e^{-rT}\!\left[-(K - K)\,q(K) - \int_K^{\infty} q(s)\,ds\right] = -e^{-rT}\int_K^{\infty} q(s)\,ds
    $$

    $$
    = -e^{-rT}\,\mathbb{Q}(S_T > K)
    $$

    This shows $D = -\partial C / \partial K$: the digital call price equals the
    negative of the strike-derivative of the European call price. In practice,
    this relationship is used to hedge digital options with call spreads.

---

**Exercise 5.**
Prove that if the discounted price process $\tilde{S}_t = e^{-rt}S_t$ is a
$\mathbb{Q}$-martingale, then $\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] = S_0$.
Explain why this is an essential consistency check for any risk-neutral
pricing model.

??? success "Solution to Exercise 5"
    If $\tilde{S}_t = e^{-rt}S_t$ is a $\mathbb{Q}$-martingale, then by the
    martingale property:

    $$
    \mathbb{E}^{\mathbb{Q}}[\tilde{S}_T \mid \mathcal{F}_0] = \tilde{S}_0
    $$

    Since $\tilde{S}_T = e^{-rT}S_T$ and $\tilde{S}_0 = S_0$:

    $$
    \mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] = S_0
    $$

    This is an essential consistency check because the stock is a traded
    asset with known price $S_0$. Applying the risk-neutral valuation
    formula to the stock (whose "payoff" at $T$ is $S_T$) must recover
    its current price. Any model that fails this check is internally
    inconsistent: it would misprice the underlying, and all derivative
    prices built on it would be unreliable.

    When this equality fails --- specifically when
    $\mathbb{E}^{\mathbb{Q}}[e^{-rT}S_T] < S_0$ --- the discounted price is
    a strict local martingale rather than a true martingale, which is
    interpreted as an asset price bubble.

