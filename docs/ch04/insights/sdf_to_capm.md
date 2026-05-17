# From SDF to CAPM and Factor Models

The SDF framework is the most general representation of pricing. Classic models like CAPM and multi-factor models are special cases that arise by restricting the form of $M_T$. This section traces those restrictions and reveals a unification: the Girsanov kernel $\boldsymbol{\theta}$ and the factor risk premia $\boldsymbol{\lambda}$ are the same mathematical object.

!!! info "Prerequisites"
    This section assumes familiarity with:

    - [What the SDF Really Means](sdf.md)
    - [Market Price of Risk](../risk_neutral/market_price_of_risk.md)

!!! note "Scope"
    This material belongs to equilibrium asset pricing theory, not derivative
    pricing. It is not required for computing option values but shows how the
    measure-change machinery of Girsanov's theorem connects to the risk-return
    tradeoffs studied in portfolio theory.

---

## Linear SDF Gives CAPM

The general SDF $M_T = e^{-rT} u'(C_T)/u'(C_0)$ is nonlinear in consumption. CAPM arises when we approximate it as linear in market returns---an assumption that is exact under quadratic utility or jointly Gaussian returns:

$$
M_T = a - b R_M
$$

Since $\operatorname{Cov}(M_T, R_i) = -b\,\operatorname{Cov}(R_M, R_i)$, the risk premium formula $\mathbb{E}[R_i] - R_f = -R_f \operatorname{Cov}(M_T, R_i)$ becomes proportional to market covariance. Applying it to the market itself and dividing yields:

$$
\mathbb{E}[R_i] - R_f = \beta_i\,(\mathbb{E}[R_M] - R_f)
$$

where $\beta_i = \operatorname{Cov}(R_i, R_M) / \operatorname{Var}(R_M)$. CAPM is an SDF driven by a single factor.

---

## Multi-Factor SDF Gives Factor Models

Allowing the SDF to depend on $k$ factors gives:

$$
M_T = a - b_1 F_1 - b_2 F_2 - \cdots - b_k F_k
$$

Then expected returns satisfy:

$$
\mathbb{E}[R_i] - R_f = \sum_{j=1}^k \beta_{ij} \lambda_j
$$

where $\beta_{ij}$ is the exposure to factor $j$ and $\lambda_j$ is the price of risk for factor $j$. Factor models are multi-dimensional SDFs.

---

## The Unification

The continuous-time market price of risk $\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}$ and the factor pricing equation $\mathbb{E}[\mathbf{R}] - R_f\mathbf{1} = \beta\boldsymbol{\lambda}$ are the same structure in different notation:

| Factor model | Measure change | Role |
|---|---|---|
| $\beta_{ij}$ | $\sigma_{ij}$ | Exposure to risk source $j$ |
| $\lambda_j$ | $\theta_j$ | Price per unit of risk source $j$ |
| $\sum_j \beta_{ij}\lambda_j$ | $\sum_j \sigma_{ij}\theta_j$ | Total risk premium on asset $i$ |

Risk premia exist because investors dislike states where marginal utility is high. Everything else---SDF, CAPM, factor models, measure changes---is a representation of this single idea at different levels of generality.

---

## Exercises

**Exercise 1.**
Starting from $\mathbb{E}[M_T R_T] = 1$ and the linear SDF $M_T = a - bR_M$, derive the CAPM equation $\mathbb{E}[R_i] - R_f = \beta_i(\mathbb{E}[R_M] - R_f)$.

??? success "Solution to Exercise 1"
    From $\mathbb{E}[(a - bR_M)R_i] = 1$, expand:

    $$
    a\,\mathbb{E}[R_i] - b\,\mathbb{E}[R_M R_i] = 1
    $$

    Apply to the risk-free asset ($R_i = R_f$):

    $$
    a\,R_f - b\,\mathbb{E}[R_M]\,R_f = 1 \quad \Rightarrow \quad a - b\,\mathbb{E}[R_M] = 1/R_f
    $$

    Subtract the risk-free equation from the general one and use $\mathbb{E}[R_M R_i] = \operatorname{Cov}(R_M, R_i) + \mathbb{E}[R_M]\mathbb{E}[R_i]$ to get:

    $$
    \mathbb{E}[R_i] - R_f = \frac{b\,R_f}{1}\,\operatorname{Cov}(R_i, R_M)
    $$

    Applying the same equation to the market ($R_i = R_M$) gives $\mathbb{E}[R_M] - R_f = b\,R_f\,\operatorname{Var}(R_M)$. Dividing:

    $$
    \mathbb{E}[R_i] - R_f = \frac{\operatorname{Cov}(R_i, R_M)}{\operatorname{Var}(R_M)}\,(\mathbb{E}[R_M] - R_f) = \beta_i\,(\mathbb{E}[R_M] - R_f)
    $$

---

**Exercise 2.**
Explain why a linear SDF $M_T = a - bR_M$ is economically restrictive. Under what conditions on preferences or return distributions is it exact?

??? success "Solution to Exercise 2"
    A linear SDF is exact under either of two conditions:

    - **Quadratic utility**: $u(C) = C - \frac{\gamma}{2}C^2$ gives $u'(C) = 1 - \gamma C$, which is linear in consumption. If consumption is proportional to market wealth, $M_T \propto u'(C_T)$ is linear in $R_M$.

    - **Gaussian returns**: If all returns are jointly normal, then $\mathbb{E}[R_i \mid R_M]$ is linear in $R_M$ for any SDF. The conditional expectation structure makes the pricing equation behave as if the SDF were linear.

    In general, $M_T = e^{-rT}u'(C_T)/u'(C_0)$ is nonlinear, and the linear approximation fails when returns are skewed, heavy-tailed, or utility is not quadratic. This motivates multi-factor models.

---

**Exercise 3.**
In a two-factor model with $M_T = a - b_1 F_1 - b_2 F_2$, derive the pricing equation $\mathbb{E}[R_i] - R_f = \beta_{i1}\lambda_1 + \beta_{i2}\lambda_2$.

??? success "Solution to Exercise 3"
    From $\mathbb{E}[M_T R_i] = 1$:

    $$
    a\,\mathbb{E}[R_i] - b_1\,\mathbb{E}[F_1 R_i] - b_2\,\mathbb{E}[F_2 R_i] = 1
    $$

    Applying to the risk-free asset: $a - b_1\,\mathbb{E}[F_1] - b_2\,\mathbb{E}[F_2] = 1/R_f$. Subtracting and decomposing $\mathbb{E}[F_j R_i]$ into mean and covariance terms:

    $$
    \mathbb{E}[R_i] - R_f = R_f\bigl(b_1\,\operatorname{Cov}(F_1, R_i) + b_2\,\operatorname{Cov}(F_2, R_i)\bigr)
    $$

    Defining $\beta_{ij}$ via multivariate regression of $R_i$ on $(F_1, F_2)$ and $\lambda_j$ as the corresponding factor risk premia, this gives $\mathbb{E}[R_i] - R_f = \beta_{i1}\lambda_1 + \beta_{i2}\lambda_2$, where each $\lambda_j$ represents the excess return per unit of exposure to factor $j$.

---

**Exercise 4.**
Explain how the Girsanov kernel $\boldsymbol{\theta}$ in the measure-change framework corresponds to the factor risk premia $\boldsymbol{\lambda}$ in the factor model framework. Why does non-uniqueness of $\boldsymbol{\theta}$ correspond to market incompleteness?

??? success "Solution to Exercise 4"
    The market price of risk $\boldsymbol{\theta}$ is the Girsanov kernel that removes drift from discounted prices. In matrix form, $\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}$ says excess returns equal volatility exposure times prices of risk. Comparing with $\mathbb{E}[\mathbf{R}] - R_f\mathbf{1} = \beta\boldsymbol{\lambda}$, the volatility matrix $\Sigma$ encodes factor exposures and $\boldsymbol{\theta}$ encodes risk premia per unit of Brownian shock.

    When the number of Brownian motions exceeds the number of traded assets, $\Sigma$ has a non-trivial null space and $\boldsymbol{\theta}$ is not uniquely determined. Each valid $\boldsymbol{\theta}$ defines a different equivalent local martingale measure and different derivative prices. This is market incompleteness: the pricing kernel is not fully pinned down by traded assets, and additional information (calibration, equilibrium, or preferences) is needed to select a unique measure.

---

**Exercise 5.**
In a single-factor market with $M_T = a - bR_M$ and $\mathbb{E}[M_T] = 1/R_f$,
identify which quantity plays the role of the market price of risk $\theta$
in [§ Risk Premium Decomposition](risk_premium_decomposition.md). Express
$\theta$ explicitly in terms of $b$, $R_f$, and the market's volatility.

??? success "Solution to Exercise 5"
    Comparing $\mathbb{E}[R_M] - R_f = -R_f \operatorname{Cov}(M_T, R_M)$
    with $M_T = a - bR_M$ gives $\operatorname{Cov}(M_T, R_M) = -b\,\operatorname{Var}(R_M)$, so

    $$
    \mathbb{E}[R_M] - R_f = bR_f\,\operatorname{Var}(R_M) = bR_f\,\sigma_M^2
    $$

    The Sharpe ratio of the market is

    $$
    \theta = \frac{\mathbb{E}[R_M] - R_f}{\sigma_M} = bR_f\,\sigma_M
    $$

    The SDF coefficient $b$ governs the price of market risk, so
    $bR_f\sigma_M$ plays the role of the Girsanov kernel $\theta$ in the
    continuous-time pricing framework. $\square$

---

**Exercise 6.**
A claim has zero exposure to every priced factor: $\beta_{ij} = 0$ for all
$j$. Use the factor pricing equation to determine its expected return.
Connect the result to the canonical drift-removal statement in
[§ Risk Premium Decomposition](risk_premium_decomposition.md).

??? success "Solution to Exercise 6"
    From $\mathbb{E}[R_i] - R_f = \sum_j \beta_{ij}\lambda_j = 0$, the claim
    earns the risk-free rate: $\mathbb{E}[R_i] = R_f$.

    The continuous-time analogue is that an asset with zero exposure to every
    Brownian shock ($\sigma_{ij} = 0$ for all $j$) has $\mu_i = r$ under
    $\mathbb{P}$ already, and the Girsanov substitution leaves its dynamics
    unchanged. In both representations, a position carrying no priced risk
    earns no risk premium.
