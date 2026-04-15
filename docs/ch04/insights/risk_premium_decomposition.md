# Risk Premium Decomposition

Risk-neutral valuation replaces the physical drift $\mu$ with the risk-free rate
$r$---but what exactly is removed? The answer is the **risk premium** $\sigma\theta$,
where $\theta = (\mu - r)/\sigma$ is the market price of risk. The decomposition
$\mu = r + \sigma\theta$ splits the physical drift into a time-value component and a
risk-compensation component, revealing the financial content of Girsanov's theorem.

!!! abstract "Core identity"
    The risk premium $\sigma\theta = \mu - r$ is the wedge between how assets evolve
    under $\mathbb{P}$ and how they are priced under $\mathbb{Q}$. Girsanov's
    theorem removes exactly this wedge.

---

## The Decomposition

Under $\mathbb{P}$, a risky asset follows

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}
$$

The **market price of risk** is defined as

$$
\theta := \frac{\mu - r}{\sigma}
$$

Rearranging gives the **risk premium decomposition**:

$$
\mu = r + \sigma\theta
$$

| Component | Symbol | Interpretation |
|-----------|--------|----------------|
| Risk-free rate | $r$ | Compensation for the passage of time |
| Volatility | $\sigma$ | Magnitude of randomness per unit time |
| Market price of risk | $\theta$ | Compensation per unit of volatility |
| Risk premium | $\sigma\theta$ | Total excess return for bearing risk |

The risk premium $\sigma\theta = \mu - r$ is exactly what Girsanov's theorem
subtracts from the physical drift to produce the pricing measure.

!!! note "Interpretation"
    The risk premium is not "extra drift"---it is the cost of changing measure.
    Removing it turns $\mathbb{P}$ into $\mathbb{Q}$.

---

## How Girsanov Removes the Premium

Girsanov's theorem defines

$$
W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \int_0^t \theta_s\,ds
$$

Substituting $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \theta\,dt$ into the asset
dynamics:

$$
dS_t = \mu S_t\,dt + \sigma S_t\left(dW_t^{\mathbb{Q}} - \theta\,dt\right) = (\mu - \sigma\theta)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

Since $\mu - \sigma\theta = r$, the $\mathbb{Q}$-dynamics are

$$
dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
$$

The drift changes from $\mu$ to $r$. The volatility $\sigma$ is **unchanged**
because it is determined by the quadratic variation $\langle S \rangle_t = \sigma^2 S_t^2\,dt$---a path-by-path quantity unaffected by reweighting probabilities.

!!! note "Drift changes, volatility does not"
    This is why option prices depend on $\sigma$ but not on $\mu$.

### The Radon--Nikodym Derivative

The risk premium determines the density between measures. For constant $\theta$:

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = \exp\!\left(-\theta W_T^{\mathbb{P}} - \frac{1}{2}\theta^2 T\right)
$$

A larger $|\theta|$ means more aggressive reweighting: the further $\mu$ is from
$r$, the more the measure must be tilted.

---

## Different Measures, Different Drifts

The same process $S_t$ has different drifts under different measures:

| Measure | Drift of $S_t$ | Interpretation |
|---------|-----------------|----------------|
| $\mathbb{P}$ (physical) | $\mu = r + \sigma\theta$ | Reflects risk preferences |
| $\mathbb{Q}$ (risk-neutral) | $r$ | Pricing measure |
| $\mathbb{Q}^T$ (forward) | $r - \sigma_P(t,T)$ | Bond-normalized pricing |

Under every equivalent measure the volatility $\sigma$ is preserved; only the drift
changes. This is the content of Girsanov's theorem.

!!! tip "Why derivative prices do not depend on the physical drift"
    Since $\mathbb{Q}$ replaces $\mu$ with $r$, the valuation formula
    $V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-rT}\Phi(S_T)]$ involves only $r$ and
    $\sigma$, not $\mu$. See
    [Physical vs Risk-Neutral World](physical_vs_risk_neutral.md) for further
    discussion.

---

## Economic Interpretations

### Sharpe Ratio Connection

For a single asset, the market price of risk equals the **Sharpe ratio**:

$$
\theta = \frac{\mu - r}{\sigma} = \text{Sharpe ratio}
$$

The Sharpe ratio measures risk-adjusted excess return---a natural quantity to govern
the measure change. In a multi-asset setting the analogous object is
$\|\boldsymbol{\theta}\|$, the maximum achievable Sharpe ratio across all portfolios
(the slope of the capital market line).

### Equilibrium Connection

The market price of risk $\theta$ also appears in equilibrium asset pricing.
The CAPM relation $\mu_i - r = \beta_i(\mu_M - r)$ is equivalent to the risk
premium decomposition when $\theta$ is driven by a single market factor. For
the full development---including multi-factor models and the stochastic discount
factor---see [From SDF to CAPM](sdf_to_capm.md).

### Time-Varying Risk Premia

In general, $\theta_t = (\mu_t - r_t)/\sigma_t$ is **stochastic**. Empirical
evidence shows it varies with business cycle conditions, market volatility, and
interest rate levels. Time-varying risk premia are central to term structure models
and to explaining observed patterns in asset returns.

!!! warning "The market price of risk is not directly observable"
    In practice, $\theta_t$ must be inferred jointly with model assumptions---either
    estimated from historical returns under $\mathbb{P}$ (confounded with estimation
    error) or extracted from option prices under $\mathbb{Q}$ (absorbed into
    calibrated dynamics). This unobservability is a fundamental source of model risk.

---

## Worked Example: Black-Scholes Model

Consider a stock with $\mu = 0.12$, $\sigma = 0.20$, and $r = 0.03$. The market
price of risk is

$$
\theta = \frac{0.12 - 0.03}{0.20} = 0.45
$$

The decomposition reads

$$
\underbrace{0.12}_{\mu} = \underbrace{0.03}_{r} + \underbrace{0.20 \times 0.45}_{\sigma\theta = 0.09}
$$

Under $\mathbb{P}$, the stock earns 12% per year. Under $\mathbb{Q}$, it earns
only 3%. The 9% difference is the risk premium.

The Radon--Nikodym derivative for a one-year horizon is

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_1} = \exp\!\left(-0.45\,W_1^{\mathbb{P}} - \tfrac{1}{2}(0.45)^2\right)
$$

Paths with positive $W_1^{\mathbb{P}}$ (above-average returns) receive weight below 1
under $\mathbb{Q}$; paths with negative $W_1^{\mathbb{P}}$ receive weight above 1.
The measure change systematically penalizes high-return paths to remove the drift.

---

## Summary

The risk premium decomposition $\mu = r + \sigma\theta$ is the financial content of
Girsanov's theorem:

- **$r$** compensates for time.
- **$\sigma\theta$** compensates for bearing volatility.
- **$\theta$** determines the measure change.

Under $\mathbb{P}$ the drift reflects risk preferences; under $\mathbb{Q}$ it is $r$.
Volatility is invariant across equivalent measures. In complete markets $\theta$ is
unique; in incomplete markets the decomposition admits multiple solutions, each
corresponding to a different pricing measure.

For the implications when the decomposition breaks down, see
[When Measure Change Fails](when_measure_change_fails.md). For calibration in
practice, see [Practitioner Perspective](practitioner_perspective.md).

---

## Exercises

**Exercise 1.**
A stock has physical drift $\mu = 0.10$, volatility $\sigma = 0.30$, and risk-free
rate $r = 0.02$. Compute the market price of risk $\theta$, the risk premium
$\sigma\theta$, and write the Radon--Nikodym derivative
$d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_T}$ for $T = 1$.

??? success "Solution to Exercise 1"
    The market price of risk is

    $$
    \theta = \frac{\mu - r}{\sigma} = \frac{0.10 - 0.02}{0.30} = \frac{4}{15} \approx 0.2667
    $$

    The risk premium is

    $$
    \sigma\theta = 0.30 \times \frac{4}{15} = 0.08
    $$

    This confirms $\mu - r = 0.10 - 0.02 = 0.08$.

    The Radon--Nikodym derivative for $T = 1$ is

    $$
    \frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_1} = \exp\!\left(-\frac{4}{15}W_1^{\mathbb{P}} - \frac{1}{2}\cdot\frac{16}{225}\right) = \exp\!\left(-\frac{4}{15}W_1^{\mathbb{P}} - \frac{8}{225}\right)
    $$

    Paths with positive $W_1^{\mathbb{P}}$ are downweighted and paths with negative $W_1^{\mathbb{P}}$ are upweighted, removing the risk premium from the drift.

---

**Exercise 2.**
Starting from $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t^{\mathbb{P}}$ and the Girsanov
relation $W_t^{\mathbb{Q}} = W_t^{\mathbb{P}} + \theta t$, derive the
$\mathbb{Q}$-dynamics of $S_t$ and verify that the drift becomes $r$. Explain why
$\sigma$ is unchanged.

??? success "Solution to Exercise 2"
    From the Girsanov relation, $dW_t^{\mathbb{P}} = dW_t^{\mathbb{Q}} - \theta\,dt$. Substituting:

    $$
    dS_t = \mu S_t\,dt + \sigma S_t\left(dW_t^{\mathbb{Q}} - \theta\,dt\right) = (\mu - \sigma\theta)S_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
    $$

    Using $\theta = (\mu - r)/\sigma$ gives $\sigma\theta = \mu - r$, so $\mu - \sigma\theta = r$ and

    $$
    dS_t = rS_t\,dt + \sigma S_t\,dW_t^{\mathbb{Q}}
    $$

    The drift changes from $\mu$ to $r$, confirming the measure change removes the risk premium.

    The volatility $\sigma$ is unchanged because it equals the diffusion coefficient, determined by the quadratic variation $\langle S \rangle_t = \sigma^2 S_t^2\,dt$. Quadratic variation is a path-by-path property depending on sample paths, not on probability weights. Since $\mathbb{P}$ and $\mathbb{Q}$ share the same paths, the volatility is identical under both measures.

---

**Exercise 3.**
In the Vasicek model, the short rate follows
$dr_t = \kappa(\bar{r} - r_t)\,dt + \sigma_r\,dW_t^{\mathbb{P}}$ with
$\kappa = 0.5$, $\bar{r} = 0.04$, $\sigma_r = 0.01$, and market price of interest
rate risk $\theta = 0.3$. Compute the risk-neutral long-run mean
$\bar{r}^{\mathbb{Q}}$ and explain why $\bar{r}^{\mathbb{Q}} < \bar{r}$ when
$\theta > 0$.

??? success "Solution to Exercise 3"
    Under $\mathbb{Q}$, the Vasicek dynamics become

    $$
    dr_t = \left[\kappa(\bar{r} - r_t) - \sigma_r\theta\right]dt + \sigma_r\,dW_t^{\mathbb{Q}} = \kappa\!\left(\bar{r} - \frac{\sigma_r\theta}{\kappa} - r_t\right)dt + \sigma_r\,dW_t^{\mathbb{Q}}
    $$

    The risk-neutral long-run mean is

    $$
    \bar{r}^{\mathbb{Q}} = \bar{r} - \frac{\sigma_r\theta}{\kappa} = 0.04 - \frac{0.01 \times 0.3}{0.5} = 0.04 - 0.006 = 0.034
    $$

    Since $\theta > 0$, we have $\bar{r}^{\mathbb{Q}} = 0.034 < 0.04 = \bar{r}$.

    **Economic intuition.** A positive $\theta$ means investors demand compensation for interest rate risk. Under $\mathbb{P}$, the long-run mean $\bar{r}$ includes this compensation. Under $\mathbb{Q}$, the premium is removed, so the long-run mean is lower. Bond prices---computed as $\mathbb{Q}$-expectations of discounted payoffs---use this lower mean, embedding the term premium into the yield curve.

---

**Exercise 4.**
Prove that the Sharpe ratio $(\mu_i - r)/\sigma_i$ is the same for all assets in a
single-factor complete market.

??? success "Solution to Exercise 4"
    In a single-factor complete market ($n = d = 1$), each asset satisfies

    $$
    dS_t^i = \mu_i S_t^i\,dt + \sigma_i S_t^i\,dW_t^{\mathbb{P}}
    $$

    The risk premium decomposition gives

    $$
    \mu_i - r = \sigma_i\theta
    $$

    where $\theta$ is the unique market price of risk. Dividing by $\sigma_i$:

    $$
    \frac{\mu_i - r}{\sigma_i} = \theta
    $$

    The left side is the Sharpe ratio of asset $i$. Since $\theta$ is a property of the market (not of individual assets) and is unique in a complete market, the Sharpe ratio is identical for every traded asset.

    This is the continuous-time analogue of CAPM: in equilibrium, all assets on the capital market line share the same Sharpe ratio, equal to the market price of risk. $\square$

---

**Exercise 5.**
For a time-varying market price of risk $\theta_t$ with
$\int_0^T \theta_t^2\,dt < \infty$ a.s., write the Radon--Nikodym derivative
$d\mathbb{Q}/d\mathbb{P}|_{\mathcal{F}_T}$ and explain why the Novikov condition

$$
\mathbb{E}^{\mathbb{P}}\!\left[\exp\!\left(\tfrac{1}{2}\int_0^T \theta_t^2\,dt\right)\right] < \infty
$$

guarantees the stochastic exponential is a true martingale.

??? success "Solution to Exercise 5"
    The Radon--Nikodym derivative is

    $$
    \frac{d\mathbb{Q}}{d\mathbb{P}}\bigg|_{\mathcal{F}_T} = Z_T = \exp\!\left(-\int_0^T \theta_t\,dW_t^{\mathbb{P}} - \frac{1}{2}\int_0^T \theta_t^2\,dt\right)
    $$

    This is $Z_T = \mathcal{E}(M)_T$ where $M_t = -\int_0^t \theta_s\,dW_s^{\mathbb{P}}$ is a continuous local martingale with quadratic variation $\langle M \rangle_T = \int_0^T \theta_t^2\,dt$.

    The process $Z_t$ is a non-negative local martingale, hence a supermartingale by Fatou's lemma. For $Z_T$ to define a valid probability density we need $\mathbb{E}^{\mathbb{P}}[Z_T] = 1$, requiring $Z_t$ to be a true martingale.

    The Novikov condition controls the exponential moment of $\langle M \rangle_T / 2$. When this moment is finite, the fluctuations of $M_t$ are bounded enough to prevent probability mass from leaking to infinity. This ensures $Z_t$ cannot drift systematically downward in expectation, guaranteeing $\mathbb{E}[Z_T] = 1$ and making $\mathbb{Q}$ a well-defined probability measure.

---

**Exercise 6.**
Consider three assets driven by two independent Brownian motions with
$\boldsymbol{\mu} = (0.08, 0.12, 0.06)^{\top}$, $r = 0.02$, and volatility matrix

$$
\Sigma = \begin{pmatrix} 0.20 & 0.10 \\ 0.15 & 0.25 \\ 0.10 & 0.05 \end{pmatrix}
$$

Determine whether $\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}$ has a
solution. What is the no-arbitrage implication?

??? success "Solution to Exercise 6"
    The system is

    $$
    \begin{pmatrix} 0.06 \\ 0.10 \\ 0.04 \end{pmatrix} = \begin{pmatrix} 0.20 & 0.10 \\ 0.15 & 0.25 \\ 0.10 & 0.05 \end{pmatrix} \begin{pmatrix} \theta_1 \\ \theta_2 \end{pmatrix}
    $$

    This is overdetermined (3 equations, 2 unknowns). Using the first two equations: from $0.20\theta_1 + 0.10\theta_2 = 0.06$ we get $\theta_2 = 0.6 - 2\theta_1$. Substituting into the second equation:

    $$
    0.15\theta_1 + 0.25(0.6 - 2\theta_1) = 0.10 \implies -0.35\theta_1 = -0.05 \implies \theta_1 = \tfrac{1}{7}
    $$

    $$
    \theta_2 = 0.6 - \tfrac{2}{7} = \tfrac{16}{35}
    $$

    Checking the third equation: $0.10 \times \frac{1}{7} + 0.05 \times \frac{16}{35} = \frac{0.50 + 0.80}{35} = \frac{1.30}{35} \approx 0.0371 \neq 0.04$.

    The system has **no solution**. The three excess returns are inconsistent with any single market price of risk vector. This implies an **arbitrage opportunity**: one can construct a portfolio of the three assets with zero exposure to both Brownian motions but positive excess return, violating no-arbitrage.
