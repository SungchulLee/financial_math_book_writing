# LMM Correlation Parameterization

In the LIBOR Market Model, individual forward rates are driven by correlated Brownian motions, and the **correlation matrix** $\rho = (\rho_{ij})$ controls how forward rates co-move. While caplet prices depend only on individual forward rate volatilities, the prices of multi-rate products --- swaptions, spread options, CMS derivatives --- depend critically on the correlation structure. This section presents the standard parametric correlation forms, discusses estimation and positive-definiteness constraints, and examines the impact of correlation on exotic pricing.

---

## Role of Correlation in the LMM

### Forward Rate Dynamics

Under any common measure, the forward LIBOR rates $L_0(t), L_1(t), \ldots, L_{n-1}(t)$ are driven by correlated Brownian motions:

$$
dW_i \cdot dW_j = \rho_{ij} \, dt
$$

The correlation matrix $\rho \in \mathbb{R}^{n \times n}$ must satisfy:

- **Symmetry:** $\rho_{ij} = \rho_{ji}$
- **Unit diagonal:** $\rho_{ii} = 1$
- **Positive semi-definiteness:** $x^\top \rho \, x \geq 0$ for all $x \in \mathbb{R}^n$

### Where Correlation Enters

| Product | Correlation Sensitivity |
|---|---|
| Caplet | None (single forward rate) |
| Swaption | Moderate (weighted sum of forward rates) |
| CMS spread option | High (difference of swap rates) |
| Ratchet/Snowball | Very high (path-dependent on multiple rates) |

---

## Parametric Correlation Structures

### One-Parameter Exponential Decay

The simplest specification is

$$
\rho_{ij} = e^{-\beta |T_i - T_j|}
$$

where $\beta > 0$ controls the decay rate. This matrix is:

- **Always positive definite** for $\beta > 0$
- **Toeplitz:** $\rho_{ij}$ depends only on $|i - j|$ (for equally spaced tenors)
- **Monotonically decreasing** with maturity separation

For $\beta = 0$: perfect correlation. As $\beta \to \infty$: correlation approaches zero for $i \neq j$.

??? example "Exponential Decay Matrix (beta = 0.1, annual tenors)"

    For 5 forward rates at 1Y, 2Y, 3Y, 4Y, 5Y with $\beta = 0.1$:

    | | $L_1$ | $L_2$ | $L_3$ | $L_4$ | $L_5$ |
    |---|---|---|---|---|---|
    | $L_1$ | 1.000 | 0.905 | 0.819 | 0.741 | 0.670 |
    | $L_2$ | 0.905 | 1.000 | 0.905 | 0.819 | 0.741 |
    | $L_3$ | 0.819 | 0.905 | 1.000 | 0.905 | 0.819 |
    | $L_4$ | 0.741 | 0.819 | 0.905 | 1.000 | 0.905 |
    | $L_5$ | 0.670 | 0.741 | 0.819 | 0.905 | 1.000 |

### Two-Parameter Model with Long-Run Correlation

$$
\rho_{ij} = \rho_\infty + (1 - \rho_\infty) \, e^{-\beta |T_i - T_j|}
$$

This adds a **long-run correlation floor** $\rho_\infty \in [0, 1)$. Even distant forward rates remain correlated at level $\rho_\infty$, reflecting the common dependence on the overall interest rate level.

**Positive definiteness:** The matrix is positive definite when $\rho_\infty \geq 0$ and $\beta > 0$, since it can be decomposed as $\rho_\infty \mathbf{1}\mathbf{1}^\top + (1-\rho_\infty)\rho^{\text{exp}}$, where $\rho^{\text{exp}}$ is the exponential decay matrix.

### Three-Parameter Model

$$
\rho_{ij} = \rho_\infty + (1 - \rho_\infty) \, e^{-(\beta_1 |T_i - T_j| + \beta_2 |T_i - T_j|^2)}
$$

The quadratic term allows different decay rates for nearby and distant tenors.

### Angle-Based Parameterization

Rebonato (1999) proposed

$$
\rho_{ij} = \cos(\theta_i - \theta_j)
$$

where $\theta_i$ are angles assigned to each forward rate. This automatically guarantees positive semi-definiteness because $\rho = VV^\top$ with $V_i = (\cos\theta_i, \sin\theta_i)$.

For a smooth angle function $\theta_i = a + b \cdot T_i$:

$$
\rho_{ij} = \cos\bigl(b(T_i - T_j)\bigr)
$$

This produces oscillating correlations, which may not be financially intuitive but can improve swaption fits.

---

## Positive Definiteness

### Why It Matters

If the correlation matrix is not positive semi-definite, the Cholesky decomposition used for Monte Carlo simulation fails, and the model produces pathological behavior (imaginary "volatilities").

### Ensuring Positive Definiteness

**Approach 1 --- Parametric forms.** The exponential and angle-based forms are guaranteed positive definite by construction.

**Approach 2 --- Eigenvalue repair.** Given an empirically estimated matrix that is not positive definite:

1. Compute the eigendecomposition $\hat{\rho} = V \Lambda V^\top$
2. Replace negative eigenvalues: $\tilde{\lambda}_i = \max(\lambda_i, \epsilon)$ for small $\epsilon > 0$
3. Reconstruct: $\tilde{\rho} = V \tilde{\Lambda} V^\top$
4. Normalize to unit diagonal

**Approach 3 --- Rank reduction.** Approximate the full-rank matrix by a rank-$d$ matrix:

$$
\rho \approx B B^\top, \qquad B \in \mathbb{R}^{n \times d}
$$

where $B$ contains the first $d$ scaled eigenvectors. This is both positive semi-definite by construction and computationally efficient for simulation.

---

## Historical Estimation

### From Market Data

Given a time series of forward rate changes $\Delta L_i^{(k)}$ for $k = 1, \ldots, N$:

$$
\hat{\rho}_{ij} = \frac{\sum_{k=1}^{N} \Delta L_i^{(k)} \, \Delta L_j^{(k)}}{\sqrt{\sum_{k=1}^{N} (\Delta L_i^{(k)})^2} \cdot \sqrt{\sum_{k=1}^{N} (\Delta L_j^{(k)})^2}}
$$

### Challenges

- **Estimation noise:** For $n$ forward rates, the matrix has $n(n-1)/2$ entries but the data may have fewer independent observations
- **Non-stationarity:** Correlations change over time (e.g., during crises, correlations spike)
- **Tenor structure:** Forward rates with adjacent maturities are nearly collinear, amplifying estimation noise

### Shrinkage Estimators

To improve stability, shrink toward a structured target:

$$
\hat{\rho}^{\text{shrink}} = \alpha \, \hat{\rho} + (1 - \alpha) \, \rho^{\text{target}}
$$

where $\rho^{\text{target}}$ is a parametric model (e.g., exponential decay) and $\alpha \in [0, 1]$ is the shrinkage intensity, often chosen by cross-validation.

---

## Impact on Exotic Pricing

### Swaption Volatility

From Rebonato's formula, the swaption implied volatility depends on correlation through

$$
\sigma_S^2 T_0 \approx \sum_{i,j} \frac{w_i w_j L_i(0) L_j(0)}{S(0)^2} \, \rho_{ij} \int_0^{T_0} \sigma_i(t) \sigma_j(t) \, dt
$$

**Higher correlation increases swaption volatility** because the forward rates move more in tandem, producing larger swing in the swap rate.

### CMS Spread Options

A CMS spread option pays $\max(S_{\text{long}} - S_{\text{short}} - K, 0)$, where $S_{\text{long}}$ and $S_{\text{short}}$ are swap rates of different tenors.

The spread volatility is

$$
\sigma_{\text{spread}}^2 \approx \sigma_{\text{long}}^2 + \sigma_{\text{short}}^2 - 2 \rho_{\text{long,short}} \, \sigma_{\text{long}} \, \sigma_{\text{short}}
$$

**Higher correlation reduces spread volatility** and hence spread option prices. This makes spread options strongly sensitive to the correlation model.

### Exotic Sensitivity Summary

!!! warning "Correlation Risk"
    Exotic interest rate derivatives (Bermudan swaptions, range accruals, CMS spread options) can have significant exposure to the correlation structure. Mis-specifying correlations in the LMM can lead to systematic pricing errors that are invisible in vanilla calibration (caplets, co-terminal swaptions).

---

## Rank Reduction for Simulation

### Motivation

A full $n \times n$ correlation matrix requires $n$ independent Brownian motions. With $n = 120$ (30-year quarterly), this is computationally expensive. Rank reduction uses $d \ll n$ factors.

### Procedure

1. Compute eigenvectors $v_1, \ldots, v_d$ corresponding to the $d$ largest eigenvalues
2. Form the loading matrix $B = [v_1\sqrt{\lambda_1}, \ldots, v_d\sqrt{\lambda_d}] \in \mathbb{R}^{n \times d}$
3. The approximate correlation is $\tilde{\rho} = BB^\top$
4. Normalize rows to achieve unit diagonal: $\tilde{\rho}_{ij} \to \tilde{\rho}_{ij} / \sqrt{\tilde{\rho}_{ii} \, \tilde{\rho}_{jj}}$

Typically $d = 3$ to $5$ captures 95--99% of the correlation structure.

### Simulation with Reduced Factors

Generate $d$ independent standard normals $z_1, \ldots, z_d$ and compute correlated increments:

$$
\Delta W_i = \sum_{k=1}^{d} B_{ik} \, z_k \cdot \sqrt{\Delta t}
$$

This is far more efficient than the full $n$-dimensional Cholesky decomposition.

---

## Key Takeaways

- The LMM correlation matrix $\rho_{ij}$ governs the co-movement of forward rates and is the key input for multi-rate derivative pricing
- **Exponential decay** $\rho_{ij} = e^{-\beta|T_i - T_j|}$ is the standard one-parameter specification, always positive definite
- **Two-parameter** and **angle-based** models offer greater flexibility for calibration to swaptions
- **Positive definiteness** is a binding constraint; parametric forms, eigenvalue repair, and rank reduction enforce it
- **Historical estimation** is noisy and benefits from shrinkage toward parametric targets
- Correlation affects swaption prices (higher correlation raises vol) and spread option prices (higher correlation reduces vol), making accurate calibration essential for exotic pricing

---

## Further Reading

- Rebonato (2004), *Volatility and Correlation*, Chapters 21--23
- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapter 7
- Andersen & Piterbarg (2010), *Interest Rate Modeling*, Volume II, Chapter 15
- Schoenmakers & Coffey (2003), "Systematic Generation of Parametric Correlation Structures"
