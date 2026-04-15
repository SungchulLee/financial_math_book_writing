# From SDF to CAPM to Factor Models

The same $\theta$ that removes drift in Girsanov's theorem is the price of risk in asset pricing models. What appears as a technical measure change in continuous time reappears as risk premia in equilibrium models.

In the [unifying framework](../martingale/unifying_principle.md) of this chapter, every pricing model is ultimately a statement about the stochastic discount factor. This section shows how CAPM and multi-factor models emerge as special cases of the SDF, connecting the measure-change machinery of earlier sections to the equilibrium perspective of asset pricing.

!!! info "Prerequisites"
    This section assumes familiarity with:

    - [What the SDF Really Means](sdf.md)
    - [Market Price of Risk](../risk_neutral/market_price_of_risk.md)
    - [Risk Premium Decomposition](risk_premium_decomposition.md)

---

## Why This Bridge Matters

The stochastic discount factor (SDF) is the **most general** representation of pricing. Classic models like CAPM and modern factor models are **special cases** of the same idea. Each model restricts the form of the SDF, which in turn determines the Girsanov kernel $\boldsymbol{\theta}$ that mediates the change from $\mathbb{P}$ to $\mathbb{Q}$.

> All asset pricing models are statements about how returns covary with the SDF.

---

## The Fundamental Pricing Equation

For an asset with price $P_0$ today and payoff $P_T$ at time $T$, the **gross return** $R_T = P_T / P_0$ tells you how many dollars you end up with per dollar invested. From the SDF pricing formula $P_0 = \mathbb{E}^{\mathbb{P}}[M_T P_T]$, dividing both sides by $P_0$ gives:

$$
\mathbb{E}^{\mathbb{P}}[M_T R_T] = 1
$$

Expanding via $\mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y] + \operatorname{Cov}(X,Y)$ and using $\mathbb{E}^{\mathbb{P}}[M_T] = e^{-rT} = 1/R_f$ where $R_f = e^{rT}$ is the gross risk-free return:

$$
\mathbb{E}^{\mathbb{P}}[R_T] - R_f = -R_f \cdot \operatorname{Cov}^{\mathbb{P}}(M_T, R_T)
$$

This gives the key insight:

> Expected excess returns are determined by **covariance with the SDF**.

---

## Intuition: What Gets Rewarded

* Assets that perform well in **bad states** (high $M_T$) are valuable → **low returns**
* Assets that perform poorly in bad states → risky → **high returns**

A stock that crashes in recessions has negative covariance with $M_T$ — it fails when investors need it most — and must offer a positive risk premium. An insurance contract that pays in recessions has positive covariance with $M_T$ and earns below the risk-free rate: investors accept lower returns because the payoff arrives exactly when marginal utility is high.

This is the entire logic of risk premia.

---

## From SDF to CAPM

The general SDF $M_T = e^{-rT} u'(C_T)/u'(C_0)$ is a nonlinear function of consumption. CAPM arises when we approximate it as **linear in market returns** — an assumption that is exact under quadratic utility or jointly Gaussian returns:

$$
M_T = a - b R_M
$$

Since $\operatorname{Cov}(M_T, R_i) = -b\,\operatorname{Cov}(R_M, R_i)$, the risk premium formula becomes proportional to market covariance. Applying it to the market itself and dividing yields:

$$
\mathbb{E}[R_i] - R_f = \beta_i\,(\mathbb{E}[R_M] - R_f)
$$

where:

$$
\beta_i = \frac{\operatorname{Cov}(R_i, R_M)}{\operatorname{Var}(R_M)}
$$

This is the **CAPM**.

> CAPM = SDF driven by a single factor (the market).

---

## From CAPM to Factor Models

CAPM uses a single factor. Allowing the SDF to depend on $k$ factors gives the multi-factor generalization:

$$
M_T = a - b_1 F_1 - b_2 F_2 - \cdots - b_k F_k
$$

Then expected returns satisfy:

$$
\mathbb{E}[R_i] - R_f = \sum_{j=1}^k \beta_{ij} \lambda_j
$$

where:

* $F_j$ = factors (market, size, value, etc.)
* $\beta_{ij}$ = exposure to factor $j$
* $\lambda_j$ = price of risk for factor $j$

> Factor models are multi-dimensional SDFs — and multi-dimensional measure changes.

---

## Risk Premium Revisited

The SDF framework connects directly to the [market price of risk](../risk_neutral/market_price_of_risk.md) from continuous-time finance:

$$
\mu - r = \sigma \theta
$$

In multi-factor form:

$$
\boldsymbol{\mu} - r\mathbf{1} = \Sigma \boldsymbol{\theta}
$$

The factor model and measure-change equations are the same structure in different notation:

| Factor model | Measure change | Role |
|---|---|---|
| $\beta_{ij}$ | $\sigma_{ij}$ | Exposure to risk source $j$ |
| $\lambda_j$ | $\theta_j$ | Price per unit of risk source $j$ |
| $\sum_j \beta_{ij}\lambda_j$ | $\sum_j \sigma_{ij}\theta_j$ | Total risk premium on asset $i$ |

---

## Big Unification

All frameworks say the same thing:

| Framework      | Object       | Meaning                     |
| -------------- | ------------ | --------------------------- |
| SDF            | $M_T$        | State pricing / preferences |
| CAPM           | $\beta$      | Market exposure             |
| Factor models  | $\beta_{ij}$ | Multi-factor exposure       |
| Measure change | $\theta$     | Price of risk               |

---

## Guiding Insight

> Risk premia exist because investors dislike states where marginal utility is high.

Everything else is a representation of this idea:

* SDF → direct economic weighting
* CAPM → single-factor approximation
* Factor models → richer structure

---

!!! abstract "Key takeaway"
    The SDF is the most general pricing object. CAPM is a one-factor SDF. Factor models are multi-factor SDFs. Modern asset pricing is not a collection of models — it is one idea expressed at different levels of approximation.

---

## Exercises

**Exercise 1.**
Starting from $\mathbb{E}[M_T R_T] = 1$ and the linear SDF $M_T = a - bR_M$, derive the CAPM equation $\mathbb{E}[R_i] - R_f = \beta_i(\mathbb{E}[R_M] - R_f)$. Identify the constants $a$ and $b$ in terms of $R_f$ and $\mathbb{E}[R_M]$.

??? success "Solution to Exercise 1"
    From $\mathbb{E}[M_T R_T] = 1$, expand using $M_T = a - bR_M$:

    $$
    \mathbb{E}[(a - bR_M)R_i] = 1
    $$

    $$
    a\,\mathbb{E}[R_i] - b\,\mathbb{E}[R_M R_i] = 1
    $$

    Apply the same equation to the risk-free asset ($R_i = R_f = 1 + r$):

    $$
    a\,R_f - b\,\mathbb{E}[R_M]\,R_f = 1 \quad \Rightarrow \quad a - b\,\mathbb{E}[R_M] = 1/R_f
    $$

    Apply to the market itself ($R_i = R_M$):

    $$
    a\,\mathbb{E}[R_M] - b\,\mathbb{E}[R_M^2] = 1
    $$

    Subtracting the risk-free equation from the general one and rearranging yields:

    $$
    \mathbb{E}[R_i] - R_f = \frac{b}{a - b\,\mathbb{E}[R_M]}\,\text{Cov}(R_i, R_M) = \frac{\text{Cov}(R_i, R_M)}{\text{Var}(R_M)}\,(\mathbb{E}[R_M] - R_f)
    $$

    which is the CAPM: $\mathbb{E}[R_i] - R_f = \beta_i\,(\mathbb{E}[R_M] - R_f)$.

---

**Exercise 2.**
Explain why a linear SDF $M_T = a - bR_M$ is economically restrictive. What assumption on preferences or return distributions makes it exact? (Hint: consider quadratic utility or Gaussian returns.)

??? success "Solution to Exercise 2"
    A linear SDF is exact under either of two conditions:

    - **Quadratic utility**: $u(C) = C - \frac{\gamma}{2}C^2$ gives $u'(C) = 1 - \gamma C$, which is linear in consumption. If consumption is proportional to market wealth, $M_T \propto u'(C_T)$ is linear in $R_M$.

    - **Gaussian returns**: If all returns are jointly normal, then $\mathbb{E}[R_i \mid R_M]$ is linear in $R_M$ for any SDF. The conditional expectation structure makes the pricing equation behave as if the SDF were linear, even if it is not.

    In general, the true SDF $M_T = e^{-rT}u'(C_T)/u'(C_0)$ is a nonlinear function of consumption, and the linear approximation fails when returns are skewed, heavy-tailed, or when utility is not quadratic. This motivates multi-factor models that capture higher-order risk.

---

**Exercise 3.**
In a two-factor model with $M_T = a - b_1 F_1 - b_2 F_2$, derive the pricing equation $\mathbb{E}[R_i] - R_f = \beta_{i1}\lambda_1 + \beta_{i2}\lambda_2$. Identify $\lambda_j$ in terms of $b_j$ and the factor moments.

??? success "Solution to Exercise 3"
    From $\mathbb{E}[M_T R_i] = 1$ with $M_T = a - b_1 F_1 - b_2 F_2$:

    $$
    a\,\mathbb{E}[R_i] - b_1\,\mathbb{E}[F_1 R_i] - b_2\,\mathbb{E}[F_2 R_i] = 1
    $$

    Applying to the risk-free asset: $a - b_1\,\mathbb{E}[F_1] - b_2\,\mathbb{E}[F_2] = 1/R_f$.

    Subtracting and using $\text{Cov}(F_j, R_i) = \mathbb{E}[F_j R_i] - \mathbb{E}[F_j]\mathbb{E}[R_i]$:

    $$
    \mathbb{E}[R_i] - R_f = \frac{b_1}{a - b_1\mathbb{E}[F_1] - b_2\mathbb{E}[F_2]}\,\text{Cov}(F_1, R_i) + \frac{b_2}{a - b_1\mathbb{E}[F_1] - b_2\mathbb{E}[F_2]}\,\text{Cov}(F_2, R_i)
    $$

    Defining $\beta_{ij}$ via multivariate regression of $R_i$ on $(F_1, F_2)$ and $\lambda_j$ as the factor risk premia, this gives the two-factor pricing equation. Each $\lambda_j$ represents the excess return earned per unit of exposure to factor $j$.

---

**Exercise 4.**
The SDF approach gives $\mu - r = \sigma\theta$ (single factor) and $\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}$ (multi-factor). Explain how $\boldsymbol{\theta}$ in the measure-change framework corresponds to the factor loadings and risk premia $(\beta, \lambda)$ in the factor model framework. Why does non-uniqueness of $\boldsymbol{\theta}$ correspond to market incompleteness?

??? success "Solution to Exercise 4"
    The market price of risk $\boldsymbol{\theta}$ is the Girsanov kernel that removes drift from discounted prices. In matrix form, $\boldsymbol{\mu} - r\mathbf{1} = \Sigma\boldsymbol{\theta}$ says excess returns equal volatility exposure times prices of risk.

    In the factor model, $\mathbb{E}[R_i] - R_f = \sum_j \beta_{ij}\lambda_j$ says excess returns equal factor exposure times factor risk premia. The correspondence is:

    - $\Sigma\boldsymbol{\theta}$ plays the role of $\beta\lambda$
    - The volatility matrix $\Sigma$ encodes the factor exposures
    - The prices of risk $\boldsymbol{\theta}$ encode the risk premia per unit of Brownian shock

    When the number of Brownian motions exceeds the number of traded assets, $\Sigma$ has a non-trivial null space and $\boldsymbol{\theta}$ is not uniquely determined. Each valid $\boldsymbol{\theta}$ defines a different ELMM and a different set of derivative prices. This is **market incompleteness**: the pricing kernel is not fully pinned down by traded asset prices, and additional information (calibration, equilibrium, or preference assumptions) is needed to select a unique measure.
