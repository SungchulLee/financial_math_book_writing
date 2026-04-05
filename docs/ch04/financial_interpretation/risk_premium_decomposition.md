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

!!! abstract "Core identity"
    Risk premium is the wedge between how assets evolve ($\mathbb{P}$) and
    how they are priced ($\mathbb{Q}$).

---

## The Single-Asset Decomposition

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

This identity decomposes return into:

| Component | Symbol | Interpretation |
|-----------|--------|----------------|
| Risk-free rate | $r$ | Compensation for the passage of time |
| Volatility | $\sigma$ | Magnitude of randomness per unit time |
| Market price of risk | $\theta$ | Compensation per unit of volatility |
| Risk premium | $\sigma\theta$ | Total compensation for bearing risk |

The risk premium $\sigma\theta = \mu - r$ is the excess return that investors
demand for holding the risky asset instead of the risk-free bond.

!!! note "Interpretation"
    The risk premium is exactly what must be removed from the physical drift
    to turn the physical measure into the pricing measure. It is not "extra
    drift"---it is the cost of changing measure.

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

A larger $|\theta|$ means more aggressive reweighting: the further $\mu$ is
from $r$, the more the measure must be tilted.

---

## Different Measures, Different Drifts

The same process $S_t$ has different drifts under different measures:

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

!!! warning "The market price of risk is not directly observable"
    In practice, $\theta_t$ cannot be read off from market data. It must be
    inferred jointly with model assumptions---either estimated from historical
    returns under $\mathbb{P}$ (where it is confounded with estimation error)
    or extracted from option prices under $\mathbb{Q}$ (where it is absorbed
    into the calibrated dynamics). This unobservability is a fundamental source
    of model risk.

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

---

## Exercises

**Exercise 1.**
A stock has physical drift $\mu = 0.10$, volatility $\sigma = 0.30$, and the risk-free rate is $r = 0.02$. Compute the market price of risk $\theta$, the risk premium $\sigma\theta$, and write the Radon-Nikodym derivative $d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_T}$ for $T = 1$.

??? success "Solution to Exercise 1"
    The market price of risk is

    $$
    \theta = \frac{\mu - r}{\sigma} = \frac{0.10 - 0.02}{0.30} = \frac{0.08}{0.30} = \frac{4}{15} \approx 0.2667
    $$

    The risk premium is

    $$
    \sigma\theta = 0.30 \times \frac{4}{15} = 0.08
    $$

    This confirms $\mu - r = 0.10 - 0.02 = 0.08$.

    The Radon-Nikodym derivative for $T = 1$ is

    $$
    \frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_1} = \exp\!\left(-\theta W_1^{\mathbb{P}} - \frac{1}{2}\theta^2\right) = \exp\!\left(-\frac{4}{15}W_1^{\mathbb{P}} - \frac{1}{2}\cdot\frac{16}{225}\right)
    $$

    $$
    = \exp\!\left(-\frac{4}{15}W_1^{\mathbb{P}} - \frac{8}{225}\right)
    $$

    This stochastic exponential reweights paths: those with positive $W_1^{\mathbb{P}}$ (above-average returns) are downweighted, and those with negative $W_1^{\mathbb{P}}$ (below-average returns) are upweighted, effectively removing the risk premium from the drift.

---

**Exercise 2.**
Starting from the $\mathbb{P}$-dynamics $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}$ and the Girsanov relation $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$ (for constant $\theta$), derive the $\mathbb{Q}$-dynamics of $S_t$ and verify that the drift becomes $r$. Explain why the volatility $\sigma$ is unchanged under the measure change.

??? success "Solution to Exercise 2"
    Starting from the $\mathbb{P}$-dynamics:

    $$
    dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
    $$

    The Girsanov relation gives $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$, so $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \theta\,dt$. Substituting:

    $$
    dS_t = \mu S_t\,dt + \sigma S_t\left(dW_t^{\mathbb{Q}} - \theta\,dt\right)
    $$

    $$
    = \left(\mu - \sigma\theta\right)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
    $$

    Using $\theta = (\mu - r)/\sigma$, we get $\sigma\theta = \mu - r$, so

    $$
    \mu - \sigma\theta = \mu - (\mu - r) = r
    $$

    Therefore the $\mathbb{Q}$-dynamics are

    $$
    dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
    $$

    The drift has changed from $\mu$ to $r$, confirming the measure change removes the risk premium.

    The volatility $\sigma$ is unchanged because it is the diffusion coefficient, which is determined by the quadratic variation $\langle S \rangle_t = \sigma^2 S_t^2\,dt$. Quadratic variation is a path-by-path property: it depends on the sample paths of the process, not on the probability weights assigned to those paths. Since $\mathbb{P}$ and $\mathbb{Q}$ are equivalent measures defined on the same sample space with the same paths, the quadratic variation---and hence the volatility---is identical under both measures.

---

**Exercise 3.**
In the Vasicek model, the short rate follows $dr_t = \kappa(\bar{r} - r_t)\,dt + \sigma_r\,dW_t^{\mathbb{P}}$ with $\kappa = 0.5$, $\bar{r} = 0.04$, $\sigma_r = 0.01$, and market price of interest rate risk $\theta = 0.3$. Compute the risk-neutral long-run mean $\bar{r}^{\mathbb{Q}}$ and explain the economic intuition for why $\bar{r}^{\mathbb{Q}} < \bar{r}$ when $\theta > 0$.

??? success "Solution to Exercise 3"
    The risk-neutral long-run mean in the Vasicek model is

    $$
    \bar{r}^{\mathbb{Q}} = \bar{r} - \frac{\sigma_r\theta}{\kappa} = 0.04 - \frac{0.01 \times 0.3}{0.5} = 0.04 - 0.006 = 0.034
    $$

    Since $\theta > 0$, we have $\bar{r}^{\mathbb{Q}} = 0.034 < 0.04 = \bar{r}$.

    **Economic intuition:** A positive market price of interest rate risk $\theta > 0$ means investors demand compensation for bearing interest rate risk. Under $\mathbb{P}$, the short rate mean-reverts to a higher level $\bar{r} = 0.04$ because this level includes the risk premium.

    Under $\mathbb{Q}$, the risk premium is removed, so the long-run mean is lower. The risk-neutral measure reweights scenarios such that higher interest rate paths are downweighted (their excess return above the risk-free rate is stripped away). This lower risk-neutral mean shifts the yield curve: bond prices, which are expectations of discounted payoffs under $\mathbb{Q}$, are computed using this lower long-run mean, effectively embedding the term premium into the yield curve.

---

**Exercise 4.**
Consider three assets driven by two independent Brownian motions with drift vector $\boldsymbol{\mu} = (0.08, 0.12, 0.06)^{\top}$, risk-free rate $r = 0.02$, and volatility matrix

$$
\Sigma = \begin{pmatrix} 0.20 & 0.10 \\ 0.15 & 0.25 \\ 0.10 & 0.05 \end{pmatrix}
$$

Determine whether the system $\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}$ has a solution. If so, is it unique? If not, explain the no-arbitrage implication.

??? success "Solution to Exercise 4"
    The system is $\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}$, which gives

    $$
    \begin{pmatrix} 0.06 \\ 0.10 \\ 0.04 \end{pmatrix} = \begin{pmatrix} 0.20 & 0.10 \\ 0.15 & 0.25 \\ 0.10 & 0.05 \end{pmatrix} \begin{pmatrix} \theta_1 \\ \theta_2 \end{pmatrix}
    $$

    This is an overdetermined system with 3 equations and 2 unknowns. We need to check if the vector $(0.06, 0.10, 0.04)^{\top}$ lies in the column space of $\Sigma$.

    Using the first two equations:

    $$
    0.20\theta_1 + 0.10\theta_2 = 0.06
    $$

    $$
    0.15\theta_1 + 0.25\theta_2 = 0.10
    $$

    From the first equation: $\theta_2 = 0.6 - 2\theta_1$. Substituting into the second:

    $$
    0.15\theta_1 + 0.25(0.6 - 2\theta_1) = 0.10
    $$

    $$
    0.15\theta_1 + 0.15 - 0.50\theta_1 = 0.10
    $$

    $$
    -0.35\theta_1 = -0.05 \implies \theta_1 = \frac{1}{7} \approx 0.1429
    $$

    $$
    \theta_2 = 0.6 - \frac{2}{7} = \frac{16}{35} \approx 0.3143
    $$

    Now check the third equation: $0.10\theta_1 + 0.05\theta_2 = 0.10 \times \frac{1}{7} + 0.05 \times \frac{16}{35} = \frac{0.10}{7} + \frac{0.80}{35} = \frac{0.50}{35} + \frac{0.80}{35} = \frac{1.30}{35} \approx 0.0371$.

    This does not equal $0.04$. Therefore the system has **no solution**.

    **No-arbitrage implication:** The inconsistency means that the three excess returns are not compatible with any single market price of risk vector. This implies an **arbitrage opportunity** exists: the three assets' risk premia are inconsistent with the assumption of two independent risk factors. One can construct a portfolio of the three assets that has zero exposure to both Brownian motions but earns a positive excess return, violating no-arbitrage.

---

**Exercise 5.**
Prove that the Sharpe ratio $(\mu - r)/\sigma$ is the same for all assets in a single-factor complete market. Hint: use the risk premium decomposition and the fact that $\theta$ is unique in a complete market.

??? success "Solution to Exercise 5"
    In a single-factor complete market, there is one Brownian motion and one risky asset, so $n = d = 1$. Each asset $i$ has dynamics

    $$
    dS_t^i = \mu_i S_t^i\,dt + \sigma_i S_t^i\,dW_t^{\mathbb{P}}
    $$

    The risk premium decomposition for each asset is

    $$
    \mu_i - r = \sigma_i\theta
    $$

    where $\theta$ is the unique market price of risk (since the market is complete, $\theta$ is determined uniquely). Dividing both sides by $\sigma_i$:

    $$
    \frac{\mu_i - r}{\sigma_i} = \theta
    $$

    The left side is the Sharpe ratio of asset $i$. Since $\theta$ is the same for all assets (it is a property of the market, not of individual assets), the Sharpe ratio $(\mu_i - r)/\sigma_i = \theta$ is identical for every traded asset.

    This is the continuous-time analogue of the result from CAPM: in equilibrium, all assets on the capital market line have the same Sharpe ratio, equal to the market price of risk. The uniqueness of $\theta$ in a complete market is what enforces this equality.

---

**Exercise 6.**
Consider a stock with time-varying market price of risk $\theta_t$ satisfying

$$
\int_0^T \theta_t^2\,dt < \infty \quad \text{a.s.}
$$

Write the Radon-Nikodym derivative $d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_T}$ in terms of $\theta_t$ and explain why the Novikov condition $\mathbb{E}^{\mathbb{P}}[\exp(\frac{1}{2}\int_0^T \theta_t^2\,dt)] < \infty$ is sufficient to guarantee that the stochastic exponential is a true martingale.

??? success "Solution to Exercise 6"
    For a time-varying market price of risk $\theta_t$, the Radon-Nikodym derivative is given by the stochastic exponential

    $$
    \frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = Z_T = \exp\!\left(-\int_0^T \theta_t\,dW_t^{\mathbb{P}} - \frac{1}{2}\int_0^T \theta_t^2\,dt\right)
    $$

    This is $Z_T = \mathcal{E}(M)_T$ where $M_t = -\int_0^t \theta_s\,dW_s^{\mathbb{P}}$ is a continuous local martingale.

    The stochastic exponential $Z_t$ is always a non-negative local martingale, hence a supermartingale by Fatou's lemma. For $Z_T$ to define a valid probability density, we need $\mathbb{E}^{\mathbb{P}}[Z_T] = 1$, which requires $Z_t$ to be a **true** martingale.

    The **Novikov condition** states that if

    $$
    \mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\frac{1}{2}\int_0^T \theta_t^2\,dt\right)\right] < \infty
    $$

    then $Z_t$ is a true martingale on $[0, T]$. The intuition is as follows: The quadratic variation of $M$ is $\langle M \rangle_T = \int_0^T \theta_t^2\,dt$, which controls how fast the local martingale $M_t$ can fluctuate. If the exponential moment of $\langle M \rangle_T / 2$ is finite, the fluctuations of $M_t$ are sufficiently controlled to prevent mass from leaking to infinity. Specifically, the condition ensures that $Z_t$ cannot drift systematically downward in expectation (which would happen if paths with very large $|M_t|$ values carried too much weight), guaranteeing $\mathbb{E}[Z_T] = 1$.

---

**Exercise 7.**
In the CAPM framework, asset $i$ has $\beta_i = 1.2$, the market expected return is $\mu_M = 0.09$, market volatility is $\sigma_M = 0.18$, and $r = 0.03$. Compute the expected return $\mu_i$ using the CAPM relation, determine the market price of risk $\theta_M$, and express asset $i$'s risk premium in the form $\sigma_i \rho_{iM} \theta_M$ given that $\sigma_i = 0.24$ and $\rho_{iM} = 0.9$. Verify consistency with the CAPM formula.

??? success "Solution to Exercise 7"
    **CAPM expected return:** Using $\mu_i - r = \beta_i(\mu_M - r)$:

    $$
    \mu_i = r + \beta_i(\mu_M - r) = 0.03 + 1.2 \times (0.09 - 0.03) = 0.03 + 1.2 \times 0.06 = 0.03 + 0.072 = 0.102
    $$

    **Market price of risk:**

    $$
    \theta_M = \frac{\mu_M - r}{\sigma_M} = \frac{0.09 - 0.03}{0.18} = \frac{0.06}{0.18} = \frac{1}{3} \approx 0.3333
    $$

    **Risk premium in the form $\sigma_i \rho_{iM} \theta_M$:**

    $$
    \sigma_i \rho_{iM} \theta_M = 0.24 \times 0.9 \times \frac{1}{3} = 0.072
    $$

    **Verification:** The CAPM risk premium is $\beta_i(\mu_M - r) = 1.2 \times 0.06 = 0.072$.

    To confirm consistency, recall that $\beta_i = \frac{\operatorname{Cov}(R_i, R_M)}{\operatorname{Var}(R_M)} = \frac{\rho_{iM}\sigma_i\sigma_M}{\sigma_M^2} = \frac{\rho_{iM}\sigma_i}{\sigma_M}$. Therefore:

    $$
    \beta_i(\mu_M - r) = \frac{\rho_{iM}\sigma_i}{\sigma_M}(\mu_M - r) = \rho_{iM}\sigma_i \cdot \frac{\mu_M - r}{\sigma_M} = \sigma_i\rho_{iM}\theta_M
    $$

    Numerically: $\beta_i = \frac{0.9 \times 0.24}{0.18} = 1.2$ $\checkmark$, and $\sigma_i\rho_{iM}\theta_M = 0.072 = \beta_i(\mu_M - r)$ $\checkmark$. The two expressions for the risk premium are identical, confirming the consistency of the CAPM with the market price of risk framework.
