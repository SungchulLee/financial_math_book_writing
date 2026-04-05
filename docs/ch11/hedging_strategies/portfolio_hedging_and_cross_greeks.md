# Portfolio Hedging and Cross-Greeks

When a trading book contains options on multiple underlyings, the risk management problem becomes genuinely multi-dimensional. **Cross-Greeks** --- sensitivities involving more than one underlying --- capture correlation-driven risks that are invisible to single-asset analysis. This section develops the framework for portfolio-level hedging with emphasis on the **cross-gamma** matrix and its implications for hedging error.

---

## Multi-Asset Sensitivity Framework

### Portfolio Value and First-Order Sensitivities

Consider a portfolio of options depending on $d$ underlying assets with prices $S = (S_1, \ldots, S_d)^T$. The portfolio value $\Pi(t, S)$ admits a Taylor expansion:

$$
\delta\Pi \approx \sum_{i=1}^d \Delta_i\,\delta S_i + \Theta\,\delta t + \frac{1}{2}\sum_{i=1}^d \sum_{j=1}^d \Gamma_{ij}\,\delta S_i\,\delta S_j + \sum_{i=1}^d \mathcal{V}_i\,\delta\sigma_i
$$

where the sensitivities are:

| Greek | Definition | Interpretation |
|:---|:---|:---|
| $\Delta_i = \frac{\partial \Pi}{\partial S_i}$ | Delta vector | Directional exposure to asset $i$ |
| $\Gamma_{ij} = \frac{\partial^2 \Pi}{\partial S_i \partial S_j}$ | Gamma matrix | Second-order (cross-)sensitivity |
| $\Theta = \frac{\partial \Pi}{\partial t}$ | Theta | Time decay |
| $\mathcal{V}_i = \frac{\partial \Pi}{\partial \sigma_i}$ | Vega vector | Volatility exposure to asset $i$ |

### Vector and Matrix Notation

The delta vector and gamma matrix in compact form:

$$
\boldsymbol{\Delta} = \nabla_S \Pi \in \mathbb{R}^d, \qquad \boldsymbol{\Gamma} = \nabla_S^2 \Pi \in \mathbb{R}^{d \times d}
$$

The second-order Taylor expansion becomes:

$$
\boxed{\delta\Pi \approx \boldsymbol{\Delta}^T \delta\mathbf{S} + \Theta\,\delta t + \frac{1}{2}\,\delta\mathbf{S}^T \boldsymbol{\Gamma}\,\delta\mathbf{S}}
$$

---

## Cross-Gamma: Definition and Structure

### Definition

The **cross-gamma** between assets $i$ and $j$ is:

$$
\Gamma_{ij} = \frac{\partial^2 \Pi}{\partial S_i \partial S_j}, \quad i \neq j
$$

The diagonal entries $\Gamma_{ii}$ are the standard single-asset gammas. The full gamma matrix $\boldsymbol{\Gamma}$ is symmetric: $\Gamma_{ij} = \Gamma_{ji}$.

### When Cross-Gamma Arises

Cross-gamma is nonzero when the portfolio contains instruments that depend on multiple underlyings simultaneously:

- **Basket options**: Options on $\sum_i w_i S_i$ have cross-gammas proportional to $w_i w_j$.
- **Spread options**: Options on $S_1 - S_2$ have $\Gamma_{12} < 0$.
- **Quanto options**: Currency-adjusted options create cross-gamma between the asset and the exchange rate.
- **Correlation-dependent structures**: Worst-of, best-of, and rainbow options.

!!! info "Single-Asset Options"
    A portfolio containing only single-asset options (each depending on only one $S_i$) has $\Gamma_{ij} = 0$ for $i \neq j$. The gamma matrix is diagonal, and the multi-asset hedging problem decouples into $d$ independent single-asset problems.

### Cross-Gamma for a Two-Asset Basket

Consider a call on the basket $B = w_1 S_1 + w_2 S_2$ with strike $K$. The payoff is $(B - K)^+$. By the chain rule:

$$
\Delta_i = w_i \frac{\partial C}{\partial B}, \qquad \Gamma_{ij} = w_i w_j \frac{\partial^2 C}{\partial B^2}
$$

where $C(B)$ is the call price as a function of the basket level. Since $\frac{\partial^2 C}{\partial B^2} > 0$ (the call has positive gamma in $B$), the cross-gamma $\Gamma_{12} = w_1 w_2 \frac{\partial^2 C}{\partial B^2} > 0$ for positive weights.

---

## Portfolio-Level Delta Hedging

### The Multi-Asset Delta Hedge

To delta-hedge the portfolio, hold $-\Delta_i$ shares of asset $i$ for each $i = 1, \ldots, d$. The hedged portfolio is:

$$
\Pi_{\text{hedged}} = \Pi - \sum_{i=1}^d \Delta_i S_i
$$

The residual P&L after delta hedging is:

$$
\delta\Pi_{\text{hedged}} \approx \Theta\,\delta t + \frac{1}{2}\,\delta\mathbf{S}^T \boldsymbol{\Gamma}\,\delta\mathbf{S}
$$

### Hedged P&L in Terms of Correlations

Under geometric Brownian motion for each asset ($dS_i = \mu_i S_i\,dt + \sigma_i S_i\,dW_i$ with $\operatorname{Corr}(dW_i, dW_j) = \rho_{ij}$), the expected delta-hedged P&L over $\delta t$ is:

$$
\mathbb{E}[\delta\Pi_{\text{hedged}}] = \left(\Theta + \frac{1}{2}\sum_{i,j} \Gamma_{ij} \rho_{ij} \sigma_i \sigma_j S_i S_j\right)\delta t
$$

The cross-gamma terms $\Gamma_{ij}\rho_{ij}\sigma_i\sigma_j S_i S_j$ contribute to the expected P&L through the **correlation structure**. If correlations change, these terms produce unexpected gains or losses.

---

## Gamma Hedging in Multiple Dimensions

### The Hedging System

To neutralize the entire gamma matrix, we need hedging instruments with their own gamma matrices. Let $H^{(l)}$ be the $l$-th hedging instrument with gamma matrix $\boldsymbol{\Gamma}^{(l)}$. To achieve $\boldsymbol{\Gamma}_{\text{portfolio}} = \mathbf{0}$, solve:

$$
\sum_{l=1}^L n_l\,\boldsymbol{\Gamma}^{(l)} = -\boldsymbol{\Gamma}_{\text{existing}}
$$

Since $\boldsymbol{\Gamma}$ is a $d \times d$ symmetric matrix with $d(d+1)/2$ independent entries, we need at least $L = d(d+1)/2$ hedging instruments to fully neutralize the gamma matrix.

!!! warning "Dimensionality Curse"
    For $d = 2$ assets: need at least 3 instruments ($\Gamma_{11}, \Gamma_{12}, \Gamma_{22}$).

    For $d = 5$ assets: need at least 15 instruments.

    For $d = 10$ assets: need at least 55 instruments.

    Full gamma neutralization becomes impractical for large $d$. In practice, traders focus on the most significant gamma exposures.

### Partial Gamma Hedging

When full neutralization is infeasible, prioritize:

1. **Diagonal gammas** $\Gamma_{ii}$: Hedge single-asset gammas first using single-asset options.
2. **Largest cross-gammas**: Hedge the $\Gamma_{ij}$ entries with the greatest dollar exposure $|\Gamma_{ij} \rho_{ij} \sigma_i \sigma_j S_i S_j|$.
3. **Accept residual**: Leave smaller cross-gamma exposures unhedged and monitor.

---

## Cross-Gamma Effects on Hedging Error

### Variance of Delta-Hedged P&L

The variance of the delta-hedged P&L over one step $\delta t$ involves the fourth moments of the joint returns:

$$
\operatorname{Var}(\delta\Pi_{\text{hedged}}) \approx \frac{1}{2}\sum_{i,j,k,l} \Gamma_{ij}\Gamma_{kl}\,C_{ijkl}\,(\delta t)^2
$$

where $C_{ijkl} = \operatorname{Cov}(\delta S_i\,\delta S_j,\; \delta S_k\,\delta S_l)$ is the fourth-order covariance tensor. For jointly normal returns:

$$
C_{ijkl} = (\rho_{ik}\rho_{jl} + \rho_{il}\rho_{jk})\sigma_i\sigma_j\sigma_k\sigma_l S_i S_j S_k S_l\,(\delta t)^2
$$

### Two-Asset Special Case

For $d = 2$, the hedged P&L variance simplifies to:

$$
\operatorname{Var}(\delta\Pi_{\text{hedged}}) \approx \left[\frac{1}{2}(\Gamma_{11} S_1^2 \sigma_1^2)^2 + 2\rho_{12}^2 \Gamma_{11}\Gamma_{22}S_1^2 S_2^2 \sigma_1^2\sigma_2^2 + \frac{1}{2}(\Gamma_{22}S_2^2\sigma_2^2)^2 + 2(\Gamma_{12}S_1 S_2 \sigma_1\sigma_2)^2(1 + \rho_{12}^2)\right](\delta t)^2
$$

The cross-gamma $\Gamma_{12}$ contributes an additional variance term that depends on $(1 + \rho_{12}^2)$, which is always positive and amplified by high correlation.

---

## Correlation Risk

### Sensitivity to Correlation

The portfolio vega with respect to correlation $\rho_{ij}$ is:

$$
\frac{\partial \Pi}{\partial \rho_{ij}} = \text{``correlation vega'' or ``cega''}
$$

This sensitivity is particularly important for:

- Basket options (highly sensitive to pairwise correlations)
- Worst-of options (increase in correlation increases value)
- Spread options (increase in correlation decreases value)

### Correlation and Cross-Gamma

The delta-hedged P&L depends on correlations through the cross-gamma terms. If the true correlation differs from the model correlation:

$$
\delta\Pi_{\text{hedged}} \approx \frac{1}{2}\sum_{i \neq j} \Gamma_{ij} S_i S_j \sigma_i \sigma_j (\rho_{ij}^{\text{realized}} - \rho_{ij}^{\text{model}})\,\delta t + \cdots
$$

This is the **correlation P&L** --- a source of model risk that is difficult to hedge because correlation derivatives are illiquid.

---

## Worked Example: Two-Asset Portfolio

A trader holds the following positions:

- **Long 100 calls** on asset 1 ($S_1 = 100$, $K_1 = 100$, $\sigma_1 = 25\%$)
- **Short 50 puts** on asset 2 ($S_2 = 80$, $K_2 = 85$, $\sigma_2 = 30\%$)
- **Long 20 basket calls** on $0.6 S_1 + 0.4 S_2$ ($K = 95$)

Per-option Greeks (illustrative values):

| | Call on $S_1$ | Put on $S_2$ | Basket call |
|:---|:---|:---|:---|
| $\Delta_1$ | 0.55 | 0 | 0.36 |
| $\Delta_2$ | 0 | $-0.45$ | 0.24 |
| $\Gamma_{11}$ | 0.032 | 0 | 0.012 |
| $\Gamma_{22}$ | 0 | 0.028 | 0.005 |
| $\Gamma_{12}$ | 0 | 0 | 0.008 |

**Portfolio-level Greeks:**

$$
\boldsymbol{\Delta} = \begin{pmatrix} 100(0.55) + 20(0.36) \\ -50(-0.45) + 20(0.24) \end{pmatrix} = \begin{pmatrix} 62.2 \\ 27.3 \end{pmatrix}
$$

$$
\boldsymbol{\Gamma} = \begin{pmatrix} 100(0.032) + 20(0.012) & 20(0.008) \\ 20(0.008) & -50(0.028) + 20(0.005) \end{pmatrix} = \begin{pmatrix} 3.44 & 0.16 \\ 0.16 & -1.30 \end{pmatrix}
$$

**Delta hedge:** Short 62.2 shares of asset 1 and 27.3 shares of asset 2.

**Gamma analysis:** The portfolio is long $\Gamma_{11}$ (benefits from moves in $S_1$) and short $\Gamma_{22}$ (exposed to moves in $S_2$). The cross-gamma $\Gamma_{12} = 0.16$ means correlated moves in both assets create additional P&L.

To fully gamma-hedge, the trader would need at least 3 additional instruments with independent gamma structures to neutralize $\Gamma_{11}$, $\Gamma_{22}$, and $\Gamma_{12}$ simultaneously.

---

## Practical Portfolio Risk Management

### Bucketed Sensitivities

Large trading books aggregate Greeks into **buckets**:

- **By underlying**: Total delta, gamma per asset
- **By maturity**: Short-dated vs. long-dated gamma
- **By strike**: ATM vs. wing gamma
- **By correlation pair**: Cross-gamma for each asset pair

### Risk Limits

Portfolio risk limits are typically expressed as:

| Metric | Definition | Typical limit |
|:---|:---|:---|
| Net delta per asset | $|\Delta_i|$ in shares | Asset-dependent |
| Dollar gamma per asset | $\frac{1}{2}\Gamma_{ii}S_i^2$ | \$X per 1% move |
| Cross-gamma | $\Gamma_{ij}S_iS_j$ | \$Y per 1% correlated move |
| Vega per asset | $\mathcal{V}_i$ | \$Z per 1 vol point |

### Hedging Priority

In practice, the hedging priority for a multi-asset book is:

1. **Delta**: Neutralize directional risk using the underlyings.
2. **Largest gammas**: Hedge dominant diagonal gammas using ATM options.
3. **Vega**: Manage volatility exposure using options at various strikes and maturities.
4. **Cross-gamma**: Address if material, using multi-asset derivatives or proxy hedges.
5. **Higher-order**: Speed, charm, vanna --- monitor but rarely hedge directly.

---

## Summary

| Concept | Key point |
|:---|:---|
| Delta vector | $\boldsymbol{\Delta} \in \mathbb{R}^d$ captures directional exposure to each asset |
| Gamma matrix | $\boldsymbol{\Gamma} \in \mathbb{R}^{d \times d}$ (symmetric); diagonal = single-asset, off-diagonal = cross |
| Cross-gamma | Arises from multi-asset instruments; drives correlation-dependent P&L |
| Full gamma hedge | Requires $d(d+1)/2$ instruments --- impractical for large $d$ |
| Correlation risk | Cross-gamma terms couple the P&L to realized correlations |
| Hedged P&L | $\delta\Pi_{\text{hedged}} \approx \frac{1}{2}\delta\mathbf{S}^T\boldsymbol{\Gamma}\,\delta\mathbf{S} + \Theta\,\delta t$ |
| Practical approach | Prioritize diagonal gamma, hedge largest cross-gammas selectively |

---

## Exercises

**Exercise 1.** For a portfolio with delta vector $\boldsymbol{\Delta} = (30, -20)^T$ and gamma matrix $\boldsymbol{\Gamma} = \begin{pmatrix} 2.0 & 0.5 \\ 0.5 & 1.5 \end{pmatrix}$, compute the delta-hedged P&L from a simultaneous move $\delta S_1 = +3$, $\delta S_2 = -2$. Decompose the P&L into contributions from $\Gamma_{11}$, $\Gamma_{22}$, and $\Gamma_{12}$.

??? success "Solution to Exercise 1"
    The delta-hedged P&L from second-order terms is:

    $$
    \delta\Pi_{\text{hedged}} \approx \frac{1}{2}\,\delta\mathbf{S}^T \boldsymbol{\Gamma}\,\delta\mathbf{S} = \frac{1}{2}\begin{pmatrix} 3 & -2 \end{pmatrix}\begin{pmatrix} 2.0 & 0.5 \\ 0.5 & 1.5 \end{pmatrix}\begin{pmatrix} 3 \\ -2 \end{pmatrix}
    $$

    First compute $\boldsymbol{\Gamma}\,\delta\mathbf{S}$:

    $$
    \begin{pmatrix} 2.0 & 0.5 \\ 0.5 & 1.5 \end{pmatrix}\begin{pmatrix} 3 \\ -2 \end{pmatrix} = \begin{pmatrix} 2.0(3) + 0.5(-2) \\ 0.5(3) + 1.5(-2) \end{pmatrix} = \begin{pmatrix} 5.0 \\ -1.5 \end{pmatrix}
    $$

    Then:

    $$
    \delta\Pi_{\text{hedged}} = \frac{1}{2}\begin{pmatrix} 3 & -2 \end{pmatrix}\begin{pmatrix} 5.0 \\ -1.5 \end{pmatrix} = \frac{1}{2}(15.0 + 3.0) = \frac{1}{2}(18.0) = 9.0
    $$

    **Decomposition by component:**

    - From $\Gamma_{11}$: $\frac{1}{2}\Gamma_{11}(\delta S_1)^2 = \frac{1}{2}(2.0)(3)^2 = 9.0$
    - From $\Gamma_{22}$: $\frac{1}{2}\Gamma_{22}(\delta S_2)^2 = \frac{1}{2}(1.5)(-2)^2 = 3.0$
    - From $\Gamma_{12}$: $\Gamma_{12}\,\delta S_1\,\delta S_2 = 0.5(3)(-2) = -3.0$

    (The cross-gamma term appears twice in the sum due to symmetry: $\Gamma_{12}\delta S_1\delta S_2 + \Gamma_{21}\delta S_2\delta S_1 = 2 \times 0.5 \times 3 \times (-2) = -6.0$, but in the quadratic form this is already captured as $\Gamma_{12}\delta S_1\delta S_2 = -3.0$ with the factor of 2 from symmetry included.)

    **Total:** $9.0 + 3.0 + (-3.0) = 9.0$, confirming the matrix computation.

    The cross-gamma reduces the P&L by $\$3.00$ because the assets moved in opposite directions ($\delta S_1 > 0$, $\delta S_2 < 0$) while $\Gamma_{12} > 0$.

---

**Exercise 2.** A basket call on $B = 0.6S_1 + 0.4S_2$ has gamma $\frac{\partial^2 C}{\partial B^2} = 0.03$. Compute the cross-gamma $\Gamma_{12} = w_1 w_2 \frac{\partial^2 C}{\partial B^2}$ and the diagonal gammas $\Gamma_{11}$ and $\Gamma_{22}$. Verify that the gamma matrix is positive semidefinite.

??? success "Solution to Exercise 2"
    For a basket call on $B = w_1 S_1 + w_2 S_2$ with $w_1 = 0.6$, $w_2 = 0.4$, and $\frac{\partial^2 C}{\partial B^2} = 0.03$:

    **Cross-gamma:**

    $$
    \Gamma_{12} = w_1 w_2 \frac{\partial^2 C}{\partial B^2} = (0.6)(0.4)(0.03) = 0.0072
    $$

    **Diagonal gammas:**

    $$
    \Gamma_{11} = w_1^2 \frac{\partial^2 C}{\partial B^2} = (0.6)^2(0.03) = 0.0108
    $$

    $$
    \Gamma_{22} = w_2^2 \frac{\partial^2 C}{\partial B^2} = (0.4)^2(0.03) = 0.0048
    $$

    **Positive semidefiniteness.** The gamma matrix is:

    $$
    \boldsymbol{\Gamma} = \frac{\partial^2 C}{\partial B^2}\begin{pmatrix} w_1^2 & w_1 w_2 \\ w_1 w_2 & w_2^2 \end{pmatrix} = 0.03\begin{pmatrix} 0.36 & 0.24 \\ 0.24 & 0.16 \end{pmatrix}
    $$

    This is a rank-1 matrix: $\boldsymbol{\Gamma} = 0.03\,\mathbf{w}\mathbf{w}^T$ where $\mathbf{w} = (0.6, 0.4)^T$. A rank-1 outer product $\mathbf{w}\mathbf{w}^T$ is always positive semidefinite (its eigenvalues are $\|\mathbf{w}\|^2 > 0$ and $0$). Multiplying by the positive scalar $0.03$ preserves positive semidefiniteness.

    Alternatively, verify: $\det(\boldsymbol{\Gamma}) = 0.03^2(0.36 \times 0.16 - 0.24^2) = 0.0009(0.0576 - 0.0576) = 0$, and $\operatorname{tr}(\boldsymbol{\Gamma}) = 0.03(0.36 + 0.16) = 0.0156 > 0$. Both eigenvalues are non-negative, confirming positive semidefiniteness.

---

**Exercise 3.** Full gamma neutralization for $d = 3$ assets requires $d(d+1)/2 = 6$ hedging instruments. If only 3 single-asset options are available (one per underlying), which gamma matrix entries can be neutralized and which remain unhedged? Describe the residual risk.

??? success "Solution to Exercise 3"
    For $d = 3$ assets, the gamma matrix has $3(3+1)/2 = 6$ independent entries: $\Gamma_{11}$, $\Gamma_{22}$, $\Gamma_{33}$, $\Gamma_{12}$, $\Gamma_{13}$, $\Gamma_{23}$.

    With 3 single-asset options (one per underlying), each option $l$ has a gamma matrix with only one nonzero entry: $\Gamma_{ll}^{(l)} \neq 0$ and all other entries zero (since single-asset options have zero cross-gamma).

    **What can be neutralized:** The three diagonal entries $\Gamma_{11}$, $\Gamma_{22}$, $\Gamma_{33}$ can each be independently neutralized by choosing appropriate positions in the corresponding single-asset options.

    **What remains unhedged:** The three cross-gamma entries $\Gamma_{12}$, $\Gamma_{13}$, $\Gamma_{23}$ cannot be affected by single-asset options at all. These entries remain at their original values.

    **Residual risk.** The unhedged cross-gammas create P&L exposure to correlated moves:

    $$
    \delta\Pi_{\text{residual}} \approx \Gamma_{12}\,\delta S_1\,\delta S_2 + \Gamma_{13}\,\delta S_1\,\delta S_3 + \Gamma_{23}\,\delta S_2\,\delta S_3
    $$

    This residual risk is driven by the realized correlations between the assets. To hedge it, the trader would need multi-asset derivatives (e.g., basket options, spread options, or correlation swaps) that generate nonzero off-diagonal gamma entries.

---

**Exercise 4.** The correlation P&L is $\frac{1}{2}\sum_{i \neq j}\Gamma_{ij}S_iS_j\sigma_i\sigma_j(\rho_{ij}^{\text{realized}} - \rho_{ij}^{\text{model}})\,\delta t$. For a two-asset portfolio with $\Gamma_{12} = 0.5$, $S_1 = S_2 = 100$, $\sigma_1 = \sigma_2 = 0.20$, compute the daily P&L impact if the realized correlation is $\rho^{\text{real}} = 0.8$ while the model assumes $\rho^{\text{model}} = 0.6$.

??? success "Solution to Exercise 4"
    The correlation P&L formula for two assets (the sum over $i \neq j$ gives two terms $\Gamma_{12}$ and $\Gamma_{21}$, which are equal):

    $$
    \text{P\&L}_{\text{corr}} = \Gamma_{12} S_1 S_2 \sigma_1 \sigma_2 (\rho^{\text{real}} - \rho^{\text{model}})\,\delta t
    $$

    (The factor of $\frac{1}{2}$ in the sum and the two symmetric terms combine to give a single factor of 1.)

    Substituting $\Gamma_{12} = 0.5$, $S_1 = S_2 = 100$, $\sigma_1 = \sigma_2 = 0.20$, $\rho^{\text{real}} = 0.8$, $\rho^{\text{model}} = 0.6$, and $\delta t = 1/252$:

    $$
    \text{P\&L}_{\text{corr}} = 0.5 \times 100 \times 100 \times 0.20 \times 0.20 \times (0.8 - 0.6) \times \frac{1}{252}
    $$

    $$
    = 0.5 \times 10000 \times 0.04 \times 0.2 \times \frac{1}{252}
    $$

    $$
    = 0.5 \times 80 \times \frac{1}{252} = \frac{40}{252} \approx \$0.159 \text{ per day}
    $$

    The positive cross-gamma combined with realized correlation exceeding the model correlation produces a small daily gain. Over a month (21 trading days), this would accumulate to approximately $\$3.33$. While small in absolute terms, this systematic bias compounds and represents a genuine model risk if the correlation mismatch persists.

---

**Exercise 5.** Using the worked example portfolio ($\boldsymbol{\Gamma} = \begin{pmatrix} 3.44 & 0.16 \\ 0.16 & -1.30 \end{pmatrix}$), compute the variance of the delta-hedged P&L over one day assuming $\sigma_1 = 0.25$, $\sigma_2 = 0.30$, $\rho_{12} = 0.5$, $S_1 = 100$, $S_2 = 80$. Which term dominates: the diagonal gammas or the cross-gamma?

??? success "Solution to Exercise 5"
    From the worked example: $\boldsymbol{\Gamma} = \begin{pmatrix} 3.44 & 0.16 \\ 0.16 & -1.30 \end{pmatrix}$, $\sigma_1 = 0.25$, $\sigma_2 = 0.30$, $\rho_{12} = 0.5$, $S_1 = 100$, $S_2 = 80$, $\delta t = 1/252$.

    Using the two-asset variance formula, define the dollar-gamma quantities:

    - $a_1 = \Gamma_{11}S_1^2\sigma_1^2 = 3.44 \times 100^2 \times 0.25^2 = 3.44 \times 10000 \times 0.0625 = 2150$
    - $a_2 = \Gamma_{22}S_2^2\sigma_2^2 = (-1.30) \times 80^2 \times 0.30^2 = -1.30 \times 6400 \times 0.09 = -748.8$
    - $a_{12} = \Gamma_{12}S_1 S_2 \sigma_1\sigma_2 = 0.16 \times 100 \times 80 \times 0.25 \times 0.30 = 0.16 \times 600 = 96$

    The variance of the hedged P&L (dropping the $(\delta t)^2$ factor and restoring it at the end):

    $$
    \operatorname{Var}(\delta\Pi_{\text{hedged}}) \approx \left[\frac{1}{2}a_1^2 + 2\rho_{12}^2 a_1 a_2 \cdot \frac{1}{2} + \frac{1}{2}a_2^2 + 2a_{12}^2(1+\rho_{12}^2)\right]\frac{(\delta t)^2}{4}
    $$

    Using the simplified version for the dominant contributions:

    - $\frac{1}{2}a_1^2 = \frac{1}{2}(2150)^2 = 2{,}311{,}250$
    - $\frac{1}{2}a_2^2 = \frac{1}{2}(748.8)^2 = 280{,}351$
    - $2a_{12}^2(1+\rho_{12}^2) = 2(96)^2(1+0.25) = 2(9216)(1.25) = 23{,}040$
    - Cross term: $2\rho_{12}^2 \cdot \frac{1}{2} \cdot a_1 \cdot a_2 = 0.25 \times 2150 \times (-748.8) = -402{,}480$ (this represents the $\Gamma_{11}\Gamma_{22}$ interaction)

    The $\Gamma_{11}$ diagonal term ($\sim 2.3M$) clearly dominates, followed by the $\Gamma_{22}$ term ($\sim 280K$). The cross-gamma contribution ($\sim 23K$) is relatively small, roughly $1\%$ of the total variance. This is expected because $|\Gamma_{12}| = 0.16$ is much smaller than $|\Gamma_{11}| = 3.44$ and $|\Gamma_{22}| = 1.30$.

    The diagonal gammas dominate the hedging error variance.

---

**Exercise 6.** A risk manager sets limits of $|\Gamma_{ii}S_i^2/2| \leq \$500$ per asset and $|\Gamma_{ij}S_iS_j| \leq \$200$ per pair. For the worked example portfolio, check which limits are satisfied and which are breached. Propose a partial hedging plan that brings all exposures within limits using the fewest instruments.

??? success "Solution to Exercise 6"
    From the worked example: $\boldsymbol{\Gamma} = \begin{pmatrix} 3.44 & 0.16 \\ 0.16 & -1.30 \end{pmatrix}$, $S_1 = 100$, $S_2 = 80$.

    **Check diagonal gamma limits ($|\Gamma_{ii}S_i^2/2| \leq \$500$):**

    - Asset 1: $|\Gamma_{11}S_1^2/2| = |3.44 \times 100^2 / 2| = |3.44 \times 5000| = \$17{,}200$ --- **breached** (exceeds $\$500$ by a factor of $34\times$)
    - Asset 2: $|\Gamma_{22}S_2^2/2| = |-1.30 \times 80^2 / 2| = 1.30 \times 3200 = \$4{,}160$ --- **breached** (exceeds $\$500$ by a factor of $8.3\times$)

    **Check cross-gamma limit ($|\Gamma_{ij}S_iS_j| \leq \$200$):**

    - Pair (1,2): $|\Gamma_{12}S_1 S_2| = |0.16 \times 100 \times 80| = \$1{,}280$ --- **breached** (exceeds $\$200$ by a factor of $6.4\times$)

    All three limits are breached.

    **Partial hedging plan.** To bring all exposures within limits using the fewest instruments:

    1. **Hedge $\Gamma_{11}$ with a single-asset option on asset 1.** Target residual $|\Gamma_{11}^{\text{res}}| \leq 2 \times 500 / 100^2 = 0.10$. Need to reduce $\Gamma_{11}$ from $3.44$ to at most $0.10$, requiring an option position contributing $\Gamma \approx -3.34$.

    2. **Hedge $\Gamma_{22}$ with a single-asset option on asset 2.** Target residual $|\Gamma_{22}^{\text{res}}| \leq 2 \times 500 / 80^2 = 0.156$. Need to reduce $|\Gamma_{22}|$ from $1.30$ to at most $0.156$, requiring an option position contributing $\Gamma \approx +1.14$.

    3. **Hedge $\Gamma_{12}$ with a multi-asset instrument** (e.g., a basket or spread option on assets 1 and 2). Target residual $|\Gamma_{12}^{\text{res}}| \leq 200 / (100 \times 80) = 0.025$. Need to reduce $\Gamma_{12}$ from $0.16$ to at most $0.025$.

    This requires a minimum of **3 instruments**: one single-asset option per underlying plus one multi-asset derivative. After adding these instruments, re-delta-hedge both underlyings with shares. If the multi-asset instrument is unavailable, the first two instruments (single-asset options) bring the two diagonal exposures within limits, leaving only the cross-gamma breach, which may be accepted as residual risk given its smaller relative magnitude.
