

# Factor Models and Risk Attribution



In portfolio theory, the covariance matrix of asset returns is a critical input to optimization. However, direct estimation of the full $n \times n$ covariance matrix becomes statistically unreliable and computationally unstable when the number of assets $n$ is large relative to the number of observations. Furthermore, interpreting the sources of risk and return in such high-dimensional systems can be opaque. **Factor models** address these issues by imposing a lower-dimensional structure on asset returns, enabling more efficient estimation and providing insight into the economic drivers of portfolio performance.

This section introduces the theory of factor models, distinguishes between statistical and economic factor decompositions, explains their role in risk modeling, and develops quantitative methods for **portfolio risk attribution**—decomposing total risk into contributions from systematic factors and idiosyncratic components.



## 1. Linear Factor Models



A **linear factor model** expresses the return on asset $i$ as a linear combination of $K$ risk factors:

$$
r_i = \alpha_i + \sum_{k=1}^K \beta_{ik} f_k + \epsilon_i = \alpha_i + \boldsymbol{\beta}_i^T \mathbf{f} + \epsilon_i
$$

where:

- $\alpha_i$ is the asset-specific intercept (expected return unexplained by factors),
- $\boldsymbol{\beta}_i = (\beta_{i1}, \dots, \beta_{iK})^T$ is the vector of factor exposures,
- $\mathbf{f} = (f_1, \dots, f_K)^T$ is the vector of factor returns,
- $\epsilon_i$ is the idiosyncratic return component.

Assumptions:

- $\mathbb{E}[\mathbf{f}] = \boldsymbol{\mu}_f$, $\mathrm{Cov}[\mathbf{f}] = \boldsymbol{\Sigma}_f$,
- $\mathbb{E}[\epsilon_i] = 0$, $\mathrm{Cov}[\epsilon_i, f_k] = 0$,
- $\mathrm{Cov}[\epsilon_i, \epsilon_j] = 0$ for $i \neq j$ (in some models).

The return vector $\mathbf{r} \in \mathbb{R}^n$ across $n$ assets can then be written as:

$$
\mathbf{r} = \boldsymbol{\alpha} + \mathbf{B} \mathbf{f} + \boldsymbol{\epsilon}
$$

with:

- $\mathbf{B} \in \mathbb{R}^{n \times K}$: factor loading matrix,
- $\boldsymbol{\epsilon} \in \mathbb{R}^n$: vector of idiosyncratic returns.



## 2. Covariance Structure under Factor Models



The implied covariance matrix of asset returns under the factor model is:

$$
\boldsymbol{\Sigma}_r = \mathbf{B} \boldsymbol{\Sigma}_f \mathbf{B}^T + \boldsymbol{\Psi}
$$

where:

- $\boldsymbol{\Sigma}_f$ is the covariance matrix of factor returns,
- $\boldsymbol{\Psi}$ is a diagonal matrix of specific variances: $\Psi_{ii} = \mathrm{Var}[\epsilon_i]$.

This decomposition significantly reduces the number of parameters to estimate:

- Sample covariance matrix: $\mathcal{O}(n^2)$ parameters.
- Factor model: $\mathcal{O}(nK + K^2)$ parameters.

When $K \ll n$, this leads to more stable estimates, particularly important for portfolio construction and stress testing.



## 3. Types of Factor Models



### A. Macroeconomic Factor Models



Factors represent observable economic variables (e.g., GDP growth, inflation, interest rates). Exposures ($\boldsymbol{\beta}_i$) are estimated via time-series regression:

$$
r_{it} = \alpha_i + \boldsymbol{\beta}_i^T \mathbf{f}_t + \epsilon_{it}
$$

Advantage: interpretability and economic intuition. Drawback: limited explanatory power and sensitivity to macro data revisions.



### B. Statistical Factor Models (e.g., PCA)



Constructed by extracting orthogonal directions that explain most of the variance in asset returns.

- Use eigenvalue decomposition of the sample covariance matrix:
  $$
  \boldsymbol{\Sigma} = \mathbf{Q} \mathbf{\Lambda} \mathbf{Q}^T
  $$
  where top $K$ eigenvectors define the latent factors.

Advantage: dimensionality reduction. Drawback: lack of economic interpretability and instability across samples.



### C. Fundamental Factor Models



Used in practice by quantitative investment firms (e.g., BARRA, Axioma). Factors include valuation ratios, momentum, size, liquidity, and industry classifications. Often blended with risk model priors and proprietary adjustments.



## 4. Risk Decomposition and Factor Attribution



Factor models facilitate **risk attribution**, allowing total portfolio variance to be decomposed as:

$$
\sigma_P^2 = \mathbf{w}^T \boldsymbol{\Sigma}_r \mathbf{w} = \underbrace{\mathbf{w}^T \mathbf{B} \boldsymbol{\Sigma}_f \mathbf{B}^T \mathbf{w}}_{\text{Systematic (factor) risk}} + \underbrace{\mathbf{w}^T \boldsymbol{\Psi} \mathbf{w}}_{\text{Idiosyncratic risk}}
$$

Letting $\mathbf{z} = \mathbf{B}^T \mathbf{w}$ denote portfolio exposures to factors, the **factor contribution to variance** is:

$$
\text{Factor}_k = z_k^2 \cdot \mathrm{Var}[f_k] + \sum_{j \neq k} z_k z_j \cdot \mathrm{Cov}[f_k, f_j]
$$

Define the **marginal contribution to risk** (MCR) of asset $i$:

$$
\text{MCR}_i = \frac{\partial \sigma_P}{\partial w_i} = \frac{(\boldsymbol{\Sigma}_r \mathbf{w})_i}{\sigma_P}
$$

Then the **risk contribution** (RC) of asset $i$ is:

$$
\text{RC}_i = w_i \cdot \text{MCR}_i = \frac{w_i (\boldsymbol{\Sigma}_r \mathbf{w})_i}{\sigma_P}
$$

This is known as **Euler decomposition** of risk, and satisfies:

$$
\sum_{i=1}^n \text{RC}_i = \sigma_P
$$

Risk attribution tools are used extensively in portfolio monitoring, compliance, and risk budgeting frameworks.



## 5. Application in Portfolio Construction and Monitoring



Factor models are integral to advanced portfolio analytics in the following areas:

- **Risk budgeting**: constrain or target risk contributions from individual factors or groups.
- **Stress testing**: simulate portfolio behavior under extreme moves in key factors (e.g., interest rate spikes).
- **Optimization constraints**: impose limits on factor exposures within the optimization problem.
- **Performance attribution**: decompose realized returns into contributions from factor premia and specific alpha.

Example constraint in optimization:

$$
| \mathbf{B}^T \mathbf{w} - \mathbf{b}_{\text{target}} | \leq \boldsymbol{\epsilon}
$$

ensures the portfolio's exposure to systematic risk factors is aligned with desired targets.



## Summary



Factor models impose structured assumptions on asset return dynamics, enabling more stable estimation of covariances, improved interpretability of portfolio risks, and greater control in optimization. By decomposing risk into systematic and idiosyncratic components, investors can manage exposures in a transparent, modular fashion. Whether implemented via economic, statistical, or fundamental factor structures, these models form the backbone of quantitative risk management, performance attribution, and institutional portfolio construction.