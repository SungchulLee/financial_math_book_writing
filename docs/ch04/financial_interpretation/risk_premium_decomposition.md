# Risk Premium Decomposition


Every risky asset earns a return above the risk-free rate. This excess return
compensates investors for bearing uncertainty, and its magnitude is governed by
the **market price of risk**. Risk premium decomposition makes this relationship
precise: it splits the physical drift into a risk-free component and a risk
premium, revealing exactly how the change of measure from $\mathbb{P}$ to
$\mathbb{Q}$ removes the compensation for risk.

Understanding this decomposition is essential for interpreting observed returns,
calibrating models, and connecting economic intuition to the probabilistic
machinery of Girsanov's theorem.

---

## The Single-Asset Decomposition

### Intuition

Under the physical measure $\mathbb{P}$, an asset's drift $\mu$ reflects both
the time value of money and compensation for risk. Under the risk-neutral
measure $\mathbb{Q}$, only the time value of money remains. The difference
$\mu - r$ is the risk premium, and the market price of risk $\theta$ normalizes
this premium by volatility.

### Setup and Derivation

Consider a risky asset with dynamics under $\mathbb{P}$:

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
$$

where $\mu$ is the physical drift, $\sigma > 0$ is the volatility, and
$r$ is the risk-free rate. The **market price of risk** is

$$
\theta := \frac{\mu - r}{\sigma}
$$

Rearranging gives the **risk premium decomposition**:

$$
\mu = r + \sigma\theta
$$

This identity has three components:

| Component | Symbol | Interpretation |
|-----------|--------|----------------|
| Risk-free rate | $r$ | Compensation for the passage of time |
| Volatility | $\sigma$ | Magnitude of randomness per unit time |
| Market price of risk | $\theta$ | Compensation per unit of volatility |
| Risk premium | $\sigma\theta$ | Total compensation for bearing risk |

The risk premium $\sigma\theta = \mu - r$ is the excess return that investors
demand for holding the risky asset instead of the risk-free bond.

---

## Connection to Measure Change

### How Girsanov Removes the Premium

Girsanov's theorem constructs the risk-neutral measure $\mathbb{Q}$ by defining

$$
W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds
$$

Substituting into the asset dynamics gives

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}} = \mu S_t\,dt + \sigma S_t\left(dW_t^{\mathbb{Q}} - \theta\,dt\right)
$$

which simplifies to

$$
dS_t = (\mu - \sigma\theta)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}} = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

The risk premium $\sigma\theta$ is subtracted from the drift, leaving only the
risk-free rate $r$. Crucially, the volatility $\sigma$ is **unchanged** by the
measure change.

!!! note "Drift changes, volatility does not"
    Under Girsanov's theorem, the measure change affects only the drift of
    the Brownian motion. The diffusion coefficient (volatility) is invariant
    because it is determined by the quadratic variation, which is a
    path-by-path quantity unaffected by reweighting probabilities. This is why
    option prices depend on $\sigma$ but not on $\mu$.

### The Radon-Nikodym Derivative

The risk premium determines the Radon-Nikodym derivative between the two
measures. For constant $\theta$:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = \exp\left(-\theta W_T^{\mathbb{P}} - \frac{1}{2}\theta^2 T\right)
$$

A larger market price of risk $|\theta|$ means a more aggressive reweighting of
paths. This is consistent with the economic intuition: the further the physical
drift is from $r$, the more the probability measure must be tilted to remove
the risk premium.

---

## Different Measures, Different Drifts

The same stochastic process $S_t$ has different drift rates under different
probability measures. This is a consequence of the risk premium decomposition
and the definition of each measure.

| Measure | Drift of $S_t$ | Interpretation |
|---------|-----------------|----------------|
| $\mathbb{P}$ (physical) | $\mu = r + \sigma\theta$ | Reflects risk preferences |
| $\mathbb{Q}$ (risk-neutral) | $r$ | Pricing measure |
| $\mathbb{Q}^T$ (forward) | $r - \sigma_P(t,T)$ | Bond-normalized pricing |

Under every equivalent measure, the volatility $\sigma$ remains the same, but
the drift changes. This is the content of Girsanov's theorem: equivalent
measures can only differ in their drift assignment, not in the diffusion.

!!! tip "Why derivative prices do not depend on the physical drift"
    Since $\mathbb{Q}$ replaces $\mu$ with $r$, the risk-neutral valuation
    formula $V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-rT}\Phi(S_T)]$ involves only
    $r$ and $\sigma$, not $\mu$. This explains the remarkable fact, first
    observed in the Black-Scholes model, that option prices are independent of
    the expected return on the underlying asset. See
    [Physical vs Risk-Neutral World](physical_vs_risk_neutral_world.md) for
    further discussion.

---

## Multi-Asset Decomposition

### The Vector Equation

In a market with $n$ risky assets driven by a $d$-dimensional Brownian motion
$\mathbf{W}_t^{\mathbb{P}} = (W_t^1, \ldots, W_t^d)^{\top}$, each asset
satisfies

$$
dS_t^i = \mu_i S_t^i\,dt + S_t^i \sum_{j=1}^{d} \sigma_{ij}\,dW_t^{j,\mathbb{P}}
$$

The risk premium decomposition generalizes to the **vector equation**:

$$
\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}
$$

where $\boldsymbol{\mu} = (\mu_1, \ldots, \mu_n)^{\top}$ is the vector of
physical drifts, $\Sigma$ is the $n \times d$ volatility matrix, and
$\boldsymbol{\theta} \in \mathbb{R}^d$ is the market price of risk vector.

### Existence and Uniqueness

The solvability of $\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}$
depends on the market structure:

- **Complete market** ($n = d$, $\Sigma$ invertible): $\boldsymbol{\theta}$
  is unique, so $\boldsymbol{\theta} = \Sigma^{-1}(\boldsymbol{\mu} - r\mathbf{1})$.
  The risk-neutral measure $\mathbb{Q}$ is unique.
- **Overdetermined** ($n > d$): The system has a solution only if
  $\boldsymbol{\mu} - r\mathbf{1} \in \operatorname{range}(\Sigma)$. This
  is the **consistency condition** for no-arbitrage.
- **Underdetermined** ($n < d$): Infinitely many solutions
  $\boldsymbol{\theta}$ exist. Each choice corresponds to a different
  risk-neutral measure. The market is **incomplete**.

!!! warning "Incomplete markets and non-unique risk premia"
    When the market is incomplete, the risk premium decomposition is not
    unique. Different choices of $\boldsymbol{\theta}$ lead to different
    risk-neutral measures, and derivative prices depend on which
    $\boldsymbol{\theta}$ is selected. This is a fundamental challenge in
    pricing derivatives in stochastic volatility or jump-diffusion models.
    See [When Measure Change Fails](when_measure_change_fails.md) for a
    detailed treatment.

---

## Economic Interpretations

### Connection to the Sharpe Ratio

For a single asset, the market price of risk equals the **Sharpe ratio**:

$$
\theta = \frac{\mu - r}{\sigma} = \text{Sharpe ratio}
$$

The Sharpe ratio measures risk-adjusted excess return, making it a natural
quantity to appear in the measure change. In the multi-asset setting, the
analogous object is $\|\boldsymbol{\theta}\|$, which represents the maximum
achievable Sharpe ratio across all portfolios (the slope of the capital market
line).

### Connection to CAPM

The Capital Asset Pricing Model provides a structural decomposition of risk
premia. For asset $i$ in a single-factor model:

$$
\mu_i - r = \beta_i(\mu_M - r)
$$

where $\beta_i = \operatorname{Cov}(R_i, R_M) / \operatorname{Var}(R_M)$ and
$\mu_M$ is the expected market return. The CAPM states that only **systematic
risk** (exposure to the market factor) is compensated. In the language of
measure change:

- The market price of risk $\theta_M = (\mu_M - r)/\sigma_M$ is the same for
  all assets.
- Asset $i$'s risk premium is $\sigma_i \rho_{iM}\theta_M = \beta_i(\mu_M - r)$.
- Idiosyncratic risk receives no premium because it can be diversified away.

### Risk Premium as a Stochastic Process

In general, the market price of risk is **time-varying and stochastic**:

$$
\theta_t = \frac{\mu_t - r_t}{\sigma_t}
$$

Empirical evidence shows that $\theta_t$ varies with:

- business cycle conditions (higher in recessions),
- market volatility (the "leverage effect"),
- interest rate levels.

Time-varying risk premia are central to term structure models (e.g., the
Vasicek and CIR models) and to explaining observed patterns in asset returns.

---

## Worked Examples

### Example 1: Black-Scholes Model

Consider a stock with $\mu = 0.12$, $\sigma = 0.20$, and $r = 0.03$.

The market price of risk is

$$
\theta = \frac{0.12 - 0.03}{0.20} = 0.45
$$

The risk premium decomposition reads

$$
\underbrace{0.12}_{\mu} = \underbrace{0.03}_{r} + \underbrace{0.20 \times 0.45}_{\sigma\theta = 0.09}
$$

Under $\mathbb{P}$, the stock earns 12% per year. Under $\mathbb{Q}$, it earns
only 3% (the risk-free rate). The 9% difference is the risk premium.

The Radon-Nikodym derivative for a one-year horizon is

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_1} = \exp\left(-0.45\,W_1^{\mathbb{P}} - \frac{1}{2}(0.45)^2\right)
$$

Novikov's condition is trivially satisfied since $\theta$ is constant:
$\mathbb{E}[\exp(\frac{1}{2}\theta^2 T)] = \exp(\frac{1}{2}(0.45)^2) < \infty$.

??? example "Numerical illustration"
    For a path where $W_1^{\mathbb{P}} = 1.0$:

    - Radon-Nikodym weight: $\exp(-0.45 \times 1.0 - 0.5 \times 0.2025) = \exp(-0.5513) \approx 0.576$
    - This path is **downweighted** under $\mathbb{Q}$ because the positive
      Brownian increment contributed to above-average returns, which must be
      penalized to remove the drift.

    For a path where $W_1^{\mathbb{P}} = -1.0$:

    - Radon-Nikodym weight: $\exp(0.45 \times 1.0 - 0.5 \times 0.2025) = \exp(0.3488) \approx 1.417$
    - This path is **upweighted** because negative Brownian increments correspond
      to below-average returns.

### Example 2: Vasicek Interest Rate Model

Under $\mathbb{P}$, the short rate follows

$$
dr_t = \kappa(\bar{r} - r_t)\,dt + \sigma_r\,dW_t^{\mathbb{P}}
$$

With an exogenous market price of interest rate risk $\theta$, the risk-neutral
dynamics become

$$
dr_t = \kappa(\bar{r} - r_t)\,dt + \sigma_r\left(dW_t^{\mathbb{Q}} - \theta\,dt\right) = \left[\kappa(\bar{r} - r_t) - \sigma_r\theta\right]dt + \sigma_r\,dW_t^{\mathbb{Q}}
$$

Rewriting:

$$
dr_t = \kappa\!\left(\bar{r} - \frac{\sigma_r\theta}{\kappa} - r_t\right)dt + \sigma_r\,dW_t^{\mathbb{Q}} = \kappa(\bar{r}^{\mathbb{Q}} - r_t)\,dt + \sigma_r\,dW_t^{\mathbb{Q}}
$$

The risk-neutral long-run mean is

$$
\bar{r}^{\mathbb{Q}} = \bar{r} - \frac{\sigma_r\theta}{\kappa}
$$

If $\theta > 0$ (investors demand positive compensation for interest rate risk),
then $\bar{r}^{\mathbb{Q}} < \bar{r}$: the risk-neutral long-run mean is lower
than the physical one. This shifts the entire yield curve, illustrating how the
risk premium affects bond pricing.

### Example 3: Two Correlated Stocks

Consider two stocks driven by two independent Brownian motions with parameters:

$$
\mu_1 = 0.10, \quad \mu_2 = 0.08, \quad r = 0.02
$$

and volatility matrix

$$
\Sigma = \begin{pmatrix} 0.25 & 0.05 \\ 0.10 & 0.30 \end{pmatrix}
$$

The market price of risk vector solves

$$
\begin{pmatrix} 0.08 \\ 0.06 \end{pmatrix} = \begin{pmatrix} 0.25 & 0.05 \\ 0.10 & 0.30 \end{pmatrix} \begin{pmatrix} \theta_1 \\ \theta_2 \end{pmatrix}
$$

Since $\det(\Sigma) = 0.25 \times 0.30 - 0.05 \times 0.10 = 0.07 \neq 0$,
the market is complete and $\boldsymbol{\theta}$ is unique:

$$
\boldsymbol{\theta} = \Sigma^{-1}\begin{pmatrix} 0.08 \\ 0.06 \end{pmatrix} = \frac{1}{0.07}\begin{pmatrix} 0.30 & -0.05 \\ -0.10 & 0.25 \end{pmatrix}\begin{pmatrix} 0.08 \\ 0.06 \end{pmatrix} = \begin{pmatrix} 0.30 \\ 0.10 \end{pmatrix}
$$

The risk premium for each asset decomposes as:

- Asset 1: $\mu_1 - r = 0.25 \times 0.30 + 0.05 \times 0.10 = 0.08$ $\checkmark$
- Asset 2: $\mu_2 - r = 0.10 \times 0.30 + 0.30 \times 0.10 = 0.06$ $\checkmark$

Each asset's excess return is explained by its exposure (via the volatility
matrix rows) to the common risk factors, priced at rates $\theta_1$ and
$\theta_2$.

---

## Summary

The risk premium decomposition $\mu = r + \sigma\theta$ is the financial
content of Girsanov's theorem:

- **The risk-free rate** $r$ compensates for time.
- **The risk premium** $\sigma\theta$ compensates for bearing volatility.
- **The market price of risk** $\theta$ determines the measure change.

Under $\mathbb{P}$, the drift reflects risk preferences. Under $\mathbb{Q}$,
the drift is the risk-free rate. Volatility is invariant across equivalent
measures. In complete markets, $\theta$ is unique; in incomplete markets, the
decomposition admits multiple solutions, each corresponding to a different
pricing measure.

For the implications when the risk premium decomposition breaks down, see
[When Measure Change Fails](when_measure_change_fails.md). For practical
aspects of calibrating $\theta$ from market data, see
[Practitioner Perspective](practitioner_perspective.md).
