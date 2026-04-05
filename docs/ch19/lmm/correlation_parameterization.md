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

---

## Exercises

**Exercise 1.** For four forward rates with annual spacing ($T_i = i$ for $i = 1, \ldots, 4$), construct the $4 \times 4$ correlation matrix using the exponential decay parameterization $\rho_{ij} = e^{-\beta|T_i - T_j|}$ with $\beta = 0.15$. Verify that the matrix is symmetric and positive definite by computing its eigenvalues.

??? success "Solution to Exercise 1"
    For four forward rates with annual spacing $T_i = i$ for $i = 1, 2, 3, 4$, and $\beta = 0.15$:

    $$
    \rho_{ij} = e^{-0.15|i - j|}
    $$

    Computing each entry:

    - $\rho_{11} = \rho_{22} = \rho_{33} = \rho_{44} = e^0 = 1$
    - $\rho_{12} = \rho_{21} = \rho_{23} = \rho_{32} = \rho_{34} = \rho_{43} = e^{-0.15} = 0.8607$
    - $\rho_{13} = \rho_{31} = \rho_{24} = \rho_{42} = e^{-0.30} = 0.7408$
    - $\rho_{14} = \rho_{41} = e^{-0.45} = 0.6376$

    The correlation matrix is:

    $$
    \rho = \begin{pmatrix} 1 & 0.8607 & 0.7408 & 0.6376 \\ 0.8607 & 1 & 0.8607 & 0.7408 \\ 0.7408 & 0.8607 & 1 & 0.8607 \\ 0.6376 & 0.7408 & 0.8607 & 1 \end{pmatrix}
    $$

    **Symmetry:** By construction, $\rho_{ij} = e^{-\beta|i-j|} = e^{-\beta|j-i|} = \rho_{ji}$. The matrix is symmetric.

    **Positive definiteness:** The exponential decay matrix is a special case of a Toeplitz correlation matrix with $\rho_{ij} = r^{|i-j|}$ where $r = e^{-\beta} \in (0, 1)$. This matrix is known to be positive definite with eigenvalues:

    $$
    \lambda_k = \frac{1 - r^2}{1 + r^2 - 2r\cos(\pi k/(n+1))}, \quad k = 1, \ldots, n
    $$

    For $n = 4$, $r = 0.8607$:

    - All denominators $1 + r^2 - 2r\cos(\theta)$ are positive for $r < 1$
    - Therefore all eigenvalues are positive

    Computing numerically, the eigenvalues are approximately $\lambda_1 \approx 3.17$, $\lambda_2 \approx 0.54$, $\lambda_3 \approx 0.19$, $\lambda_4 \approx 0.10$. All are strictly positive, confirming positive definiteness.

---

**Exercise 2.** The two-parameter correlation model $\rho_{ij} = \rho_\infty + (1 - \rho_\infty)e^{-\beta|T_i - T_j|}$ introduces a floor correlation $\rho_\infty$. For $\rho_\infty = 0.3$ and $\beta = 0.20$, compute the correlation between the 1-year and 10-year forward rates, and between the 1-year and 30-year forward rates. Compare with the one-parameter model ($\rho_\infty = 0$).

??? success "Solution to Exercise 2"
    **Two-parameter model:** $\rho_{ij} = \rho_\infty + (1 - \rho_\infty)e^{-\beta|T_i - T_j|}$ with $\rho_\infty = 0.3$, $\beta = 0.20$.

    **Correlation between 1Y and 10Y rates** ($|T_i - T_j| = 9$):

    $$
    \rho_{1,10} = 0.3 + 0.7 \times e^{-0.20 \times 9} = 0.3 + 0.7 \times e^{-1.8} = 0.3 + 0.7 \times 0.1653 = 0.3 + 0.1157 = 0.4157
    $$

    **Correlation between 1Y and 30Y rates** ($|T_i - T_j| = 29$):

    $$
    \rho_{1,30} = 0.3 + 0.7 \times e^{-0.20 \times 29} = 0.3 + 0.7 \times e^{-5.8} = 0.3 + 0.7 \times 0.00303 = 0.3 + 0.00212 = 0.3021
    $$

    **One-parameter model** ($\rho_\infty = 0$):

    $$
    \rho_{1,10}^{\text{1-par}} = e^{-0.20 \times 9} = e^{-1.8} = 0.1653
    $$

    $$
    \rho_{1,30}^{\text{1-par}} = e^{-0.20 \times 29} = e^{-5.8} = 0.00303
    $$

    **Comparison:**

    | Pair | Two-parameter | One-parameter |
    |---|---|---|
    | 1Y--10Y | 0.416 | 0.165 |
    | 1Y--30Y | 0.302 | 0.003 |

    The two-parameter model maintains a floor correlation of $\rho_\infty = 0.30$, so even very distant forward rates remain meaningfully correlated. The one-parameter model allows correlations to decay to nearly zero, which may be unrealistic since all forward rates share some common dependence on the overall level of interest rates.

    For the 1Y--30Y pair, the one-parameter model gives near-zero correlation (0.3%), while the two-parameter model gives 30.2%. This difference has a substantial impact on the pricing of CMS spread options and other products sensitive to the correlation between short and long rates.

---

**Exercise 3.** Explain why a correlation matrix estimated from historical data may not be positive definite. If you estimate the $10 \times 10$ correlation matrix from 60 monthly observations, what rank deficiency issues can arise? Describe the eigenvalue repair procedure: set negative eigenvalues to a small positive value $\epsilon$, reconstruct the matrix, and rescale to unit diagonal.

??? success "Solution to Exercise 3"
    **Why the sample correlation matrix may not be positive definite:**

    A sample correlation matrix from $N$ observations of $n$ variables has rank at most $\min(N, n)$. For a $10 \times 10$ matrix estimated from 60 monthly observations:

    - The matrix has $10 \times 9/2 = 45$ off-diagonal entries to estimate
    - With 60 observations, the sample covariance matrix has rank at most $\min(60, 10) = 10$, so in this case the sample matrix is technically full rank

    However, positive definiteness can fail in practice due to:

    1. **Missing data:** If some forward rate observations are unavailable on certain dates, the pairwise correlations may be computed from different subsets of data, leading to an inconsistent matrix
    2. **Stale data or asynchronous observations:** If rates are recorded at slightly different times, the estimated correlations can be distorted
    3. **Non-stationarity:** Correlations change over time; using a rolling window can produce matrices that hover near singularity
    4. **Numerical precision:** Rounding errors can push small eigenvalues below zero

    If $N < n$ (e.g., 8 observations for 10 variables), the matrix has rank at most 8 and is guaranteed **not** positive definite (it has at least 2 zero eigenvalues and potentially negative eigenvalues due to numerical noise).

    **Eigenvalue repair procedure:**

    1. Compute the eigendecomposition: $\hat{\rho} = V\Lambda V^\top$, where $\Lambda = \text{diag}(\lambda_1, \ldots, \lambda_n)$
    2. Replace negative eigenvalues: $\tilde{\lambda}_i = \max(\lambda_i, \epsilon)$ for small $\epsilon > 0$ (e.g., $\epsilon = 10^{-6}$)
    3. Reconstruct: $\tilde{\rho} = V\tilde{\Lambda}V^\top$
    4. The diagonal of $\tilde{\rho}$ may no longer be exactly 1. Rescale to unit diagonal:

        $$
        \hat{\rho}_{ij}^{\text{repaired}} = \frac{\tilde{\rho}_{ij}}{\sqrt{\tilde{\rho}_{ii}\,\tilde{\rho}_{jj}}}
        $$

    The repaired matrix is positive definite by construction (all eigenvalues $\geq \epsilon > 0$), though the rescaling step may slightly perturb the eigenvalues. A second round of repair is rarely needed.

---

**Exercise 4.** In Rebonato's angle-based parameterization, $\rho_{ij} = \cos(\theta_i - \theta_j)$ with $\theta_i = a + bT_i + ce^{-dT_i}$. For $a = 0.1$, $b = 0.05$, $c = 0.3$, $d = 0.2$, compute the angles $\theta_1, \theta_5, \theta_{10}$ for maturities 1, 5, and 10 years. Then compute $\rho_{1,5}$, $\rho_{1,10}$, and $\rho_{5,10}$. Verify that the resulting matrix is positive semi-definite by construction.

??? success "Solution to Exercise 4"
    **Angle-based parameterization:** $\theta_i = a + bT_i + ce^{-dT_i}$ with $a = 0.1$, $b = 0.05$, $c = 0.3$, $d = 0.2$.

    **Compute angles:**

    $$
    \theta_1 = 0.1 + 0.05(1) + 0.3\,e^{-0.2(1)} = 0.1 + 0.05 + 0.3 \times 0.8187 = 0.1 + 0.05 + 0.2456 = 0.3956
    $$

    $$
    \theta_5 = 0.1 + 0.05(5) + 0.3\,e^{-0.2(5)} = 0.1 + 0.25 + 0.3 \times 0.3679 = 0.1 + 0.25 + 0.1104 = 0.4604
    $$

    $$
    \theta_{10} = 0.1 + 0.05(10) + 0.3\,e^{-0.2(10)} = 0.1 + 0.50 + 0.3 \times 0.1353 = 0.1 + 0.50 + 0.0406 = 0.6406
    $$

    **Compute correlations:**

    $$
    \rho_{1,5} = \cos(\theta_1 - \theta_5) = \cos(0.3956 - 0.4604) = \cos(-0.0648) = \cos(0.0648) = 0.9979
    $$

    $$
    \rho_{1,10} = \cos(\theta_1 - \theta_{10}) = \cos(0.3956 - 0.6406) = \cos(-0.2450) = \cos(0.2450) = 0.9701
    $$

    $$
    \rho_{5,10} = \cos(\theta_5 - \theta_{10}) = \cos(0.4604 - 0.6406) = \cos(-0.1802) = \cos(0.1802) = 0.9838
    $$

    **Positive semi-definiteness by construction:**

    The angle-based matrix $\rho_{ij} = \cos(\theta_i - \theta_j)$ can be written as:

    $$
    \rho_{ij} = \cos\theta_i\cos\theta_j + \sin\theta_i\sin\theta_j
    $$

    Define the matrix $V \in \mathbb{R}^{n \times 2}$ with rows $V_i = (\cos\theta_i, \sin\theta_i)$. Then:

    $$
    \rho = VV^\top
    $$

    For any vector $x \in \mathbb{R}^n$:

    $$
    x^\top\rho\,x = x^\top VV^\top x = \|V^\top x\|^2 \geq 0
    $$

    Therefore $\rho$ is positive semi-definite by construction. It has rank at most 2, which means this parameterization implicitly performs a rank-2 reduction of the correlation structure.

---

**Exercise 5.** A CMS spread option pays $\max(S_{10Y} - S_{2Y} - K, 0)$. Explain qualitatively why this product is short correlation: higher correlation between the 10Y and 2Y swap rates reduces the volatility of the spread and hence the option value. Using Rebonato's swaption volatility formula, describe how the correlation parameters would be calibrated to CMS spread option prices.

??? success "Solution to Exercise 5"
    **CMS spread option is short correlation:**

    A CMS spread option pays $\max(S_{10Y} - S_{2Y} - K, 0)$. The value depends on the volatility of the spread $S_{10Y} - S_{2Y}$.

    The spread volatility (approximately) satisfies:

    $$
    \sigma_{\text{spread}}^2 \approx \sigma_{10Y}^2 + \sigma_{2Y}^2 - 2\rho_{10Y, 2Y}\,\sigma_{10Y}\,\sigma_{2Y}
    $$

    **Higher correlation $\rho_{10Y, 2Y}$** means the two swap rates move more in tandem, **reducing** the spread volatility and hence the option value. Therefore, the option is **short correlation**: its value decreases when correlation increases.

    **Calibration using Rebonato's formula:**

    Each swap rate's volatility depends on the LMM forward rate volatilities and correlations via Rebonato's formula:

    $$
    \sigma_{S}^2 T_0 = \sum_{i,j}\frac{w_i w_j L_i(0) L_j(0)}{S(0)^2}\rho_{ij}\int_0^{T_0}\sigma_i(t)\sigma_j(t)\,dt
    $$

    The correlation $\rho_{10Y, 2Y}$ between the 10Y and 2Y swap rates is an emergent quantity that depends on the full forward rate correlation matrix $\rho_{ij}$.

    **Calibration procedure:**

    1. Fix forward rate volatilities $\sigma_i$ from caplet calibration
    2. Choose a parametric correlation family (e.g., two-parameter exponential decay)
    3. For each parameter set $(\rho_\infty, \beta)$:
        - Compute individual swap rate volatilities $\sigma_{10Y}$ and $\sigma_{2Y}$ via Rebonato's formula
        - Compute the cross-correlation $\rho_{10Y, 2Y}$ from the forward rate correlation structure
        - Price the CMS spread option using these quantities
    4. Optimize $(\rho_\infty, \beta)$ to match market CMS spread option prices

    The challenge is that vanilla swaptions determine only the marginal swap rate volatilities, while CMS spread options are sensitive to the cross-correlation, which provides additional information for calibrating the correlation structure.

---

**Exercise 6.** Rank reduction approximates the $n \times n$ correlation matrix $\rho$ by a rank-$d$ matrix $\hat{\rho} = BB^\top$ where $B \in \mathbb{R}^{n \times d}$. For $n = 10$ and $d = 3$, how many free parameters does $B$ have (before imposing unit diagonal)? Describe the optimization problem for finding the best rank-3 approximation and discuss when $d = 3$ is sufficient in practice.

??? success "Solution to Exercise 6"
    **Rank reduction:** $\hat{\rho} = BB^\top$ with $B \in \mathbb{R}^{n \times d}$, $n = 10$, $d = 3$.

    **Number of free parameters in $B$:**

    $B$ has $n \times d = 10 \times 3 = 30$ entries. However, there is a rotational redundancy: for any $d \times d$ orthogonal matrix $Q$, $\tilde{B} = BQ$ satisfies $\tilde{B}\tilde{B}^\top = BQQ^\top B^\top = BB^\top$. The orthogonal group $O(d)$ has $d(d-1)/2 = 3$ free parameters, so the effective number of free parameters is:

    $$
    nd - \frac{d(d-1)}{2} = 30 - 3 = 27
    $$

    After imposing the unit diagonal constraint ($\sum_{k=1}^d B_{ik}^2 = 1$ for each $i$), we subtract $n = 10$ constraints:

    $$
    27 - 10 = 17 \text{ effective free parameters}
    $$

    Compare this to the full $10 \times 10$ correlation matrix, which has $10 \times 9/2 = 45$ free off-diagonal entries.

    **Optimization for the best rank-3 approximation:**

    The goal is to find $B$ that minimizes the Frobenius norm error:

    $$
    \min_{B \in \mathbb{R}^{n \times d}} \|\rho - BB^\top\|_F^2 \quad \text{subject to } (BB^\top)_{ii} = 1
    $$

    Without the unit diagonal constraint, the solution is given by the truncated eigendecomposition: $B = V_d \Lambda_d^{1/2}$, where $V_d$ contains the $d$ leading eigenvectors and $\Lambda_d$ the corresponding eigenvalues.

    With the diagonal constraint, a common approach is:

    1. Start with the truncated eigendecomposition as an initial guess
    2. Normalize each row of $B$ to unit length: $B_i \leftarrow B_i / \|B_i\|$
    3. Iteratively refine using gradient descent on the off-diagonal errors

    **When $d = 3$ is sufficient:**

    Principal component analysis of interest rate correlation matrices typically shows that 2--3 factors explain 95--99% of the variance:

    - **Factor 1 (level):** All rates move together --- explains ~80% of variance
    - **Factor 2 (slope):** Short and long rates move in opposite directions --- explains ~10--15%
    - **Factor 3 (curvature):** Medium rates move opposite to short and long --- explains ~3--5%

    For most pricing applications, $d = 3$ captures the essential correlation structure. The approximation may be insufficient for products very sensitive to specific pairwise correlations (e.g., CMS spread options on specific tenor pairs).

---

**Exercise 7.** Shrinkage estimation combines the sample correlation matrix $\hat{\rho}_{\text{sample}}$ with a parametric target $\hat{\rho}_{\text{target}}$: $\hat{\rho} = (1-\alpha)\hat{\rho}_{\text{sample}} + \alpha\,\hat{\rho}_{\text{target}}$. For $\alpha \in [0, 1]$, explain how this ensures positive definiteness (assuming the target is positive definite). Discuss the trade-off: what happens at $\alpha = 0$ (pure sample) versus $\alpha = 1$ (pure target)?

??? success "Solution to Exercise 7"
    **Shrinkage estimator:** $\hat{\rho} = (1 - \alpha)\hat{\rho}_{\text{sample}} + \alpha\,\hat{\rho}_{\text{target}}$ for $\alpha \in [0, 1]$.

    **Positive definiteness:**

    Assume $\hat{\rho}_{\text{target}}$ is positive definite (all eigenvalues $> 0$). For any vector $x$:

    $$
    x^\top\hat{\rho}\,x = (1-\alpha)\,x^\top\hat{\rho}_{\text{sample}}\,x + \alpha\,x^\top\hat{\rho}_{\text{target}}\,x
    $$

    If $\hat{\rho}_{\text{sample}}$ is positive semi-definite (eigenvalues $\geq 0$), both terms are non-negative, and the second is strictly positive (since the target is positive definite), so $\hat{\rho}$ is positive definite for any $\alpha > 0$.

    Even if $\hat{\rho}_{\text{sample}}$ has some negative eigenvalues, for $\alpha$ sufficiently large, the positive contribution from the target dominates, ensuring positive definiteness. Specifically, if $\lambda_{\min}^{\text{sample}}$ is the most negative eigenvalue of $\hat{\rho}_{\text{sample}}$ and $\lambda_{\min}^{\text{target}} > 0$ is the smallest eigenvalue of the target, then $\hat{\rho}$ is positive definite when:

    $$
    (1-\alpha)\lambda_{\min}^{\text{sample}} + \alpha\lambda_{\min}^{\text{target}} > 0 \quad \Rightarrow \quad \alpha > \frac{-\lambda_{\min}^{\text{sample}}}{\lambda_{\min}^{\text{target}} - \lambda_{\min}^{\text{sample}}}
    $$

    **Trade-off analysis:**

    **$\alpha = 0$ (pure sample):**

    - Uses only the empirical data: $\hat{\rho} = \hat{\rho}_{\text{sample}}$
    - **Pros:** No model assumptions; captures actual data patterns
    - **Cons:** High estimation noise (especially with limited data); may not be positive definite; unstable over time; individual pairwise correlations can be poorly estimated

    **$\alpha = 1$ (pure target):**

    - Uses only the parametric model: $\hat{\rho} = \hat{\rho}_{\text{target}}$
    - **Pros:** Always positive definite; smooth and stable; depends on only a few parameters (e.g., 1--3 for exponential decay)
    - **Cons:** Ignores all information in the data; may be misspecified (the true correlation structure may not follow the parametric form); cannot capture irregular features of the actual correlation

    **Optimal $\alpha$:** The shrinkage intensity is typically chosen by cross-validation or the Ledoit--Wolf analytical formula. It balances:

    - **Bias** (introduced by the parametric target, increasing with $\alpha$)
    - **Variance** (from sampling noise, decreasing with $\alpha$)

    For typical interest rate data with $n \approx 10$--20 forward rates and $N \approx 60$--250 observations, optimal $\alpha$ is often in the range 0.2--0.5, reflecting the substantial estimation noise in financial correlation matrices.
