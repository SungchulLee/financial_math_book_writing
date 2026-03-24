# HJM Volatility Structures and Factor Models

In the HJM framework, the no-arbitrage drift condition $\alpha(t,T) = \sigma(t,T)\int_t^T \sigma(t,u)\,du$ implies that the entire model is determined by the **volatility function** $\sigma(t,T)$. This section examines the principal choices of volatility structure --- from simple one-factor specifications to multi-factor models --- and shows how **principal component analysis** (PCA) of historical yield curve data informs these choices.

---

## The Role of Volatility in HJM

### Recap of the Framework

The HJM dynamics of the instantaneous forward rate under the risk-neutral measure are

$$
df(t,T) = \alpha(t,T)\,dt + \sum_{i=1}^{d} \sigma_i(t,T)\,dW_t^i
$$

where the drift is uniquely determined:

$$
\alpha(t,T) = \sum_{i=1}^{d} \sigma_i(t,T) \int_t^T \sigma_i(t,u)\,du
$$

The **volatility functions** $\sigma_i(t,T)$ for $i = 1, \ldots, d$ are the modeler's sole input. They control:

- The magnitude of forward rate movements at each maturity
- The correlation between forward rates at different maturities
- The number of independent sources of randomness (factors)
- The analytical tractability of the model

---

## One-Factor Models

### Constant Volatility (Ho--Lee)

The simplest specification is

$$
\sigma(t,T) = \sigma
$$

where $\sigma > 0$ is a constant. This produces:

- **Drift:** $\alpha(t,T) = \sigma^2(T - t)$
- **Bond volatility:** $\Sigma(t,T) = \sigma(T - t)$
- **Short rate:** $r_t = f(0,t) + \sigma^2 t^2/2 + \sigma W_t$ (Gaussian, equivalent to Ho--Lee model)

All maturities have the same instantaneous volatility and perfect correlation. Yield curve shifts are **parallel only**.

!!! warning "Limitation of Constant Volatility"
    Constant volatility implies that all forward rates move in lockstep. This precludes steepening, flattening, or butterfly movements of the yield curve --- patterns routinely observed in markets.

### Exponentially Decaying Volatility (Hull--White / Vasicek)

A more realistic one-factor choice is

$$
\sigma(t,T) = \sigma \, e^{-\kappa(T-t)}
$$

where $\kappa > 0$ is the mean-reversion speed. This gives:

- **Drift:** $\alpha(t,T) = \frac{\sigma^2}{\kappa} e^{-\kappa(T-t)}\bigl(1 - e^{-\kappa(T-t)}\bigr)$
- **Bond volatility:** $\Sigma(t,T) = \frac{\sigma}{\kappa}\bigl(1 - e^{-\kappa(T-t)}\bigr)$
- **Short rate:** Gaussian mean-reverting process (Hull--White / extended Vasicek)

Short-maturity forward rates are more volatile than long-maturity rates. The ratio of volatilities at maturities $T_1$ and $T_2$ is $e^{-\kappa(T_1 - T_2)}$, creating a **term structure of volatility** that decays with maturity.

### Humped Volatility

Market data often shows volatility peaking at intermediate maturities. A common parametrization is

$$
\sigma(t,T) = \sigma\bigl(a + b(T-t)\bigr) e^{-c(T-t)}
$$

where $a, b, c > 0$. The maximum volatility occurs at time-to-maturity $(1/c) - (a/b)$ (when positive). This captures the "hump" typically observed at the 2--5 year point.

---

## Multi-Factor Models

### Motivation

One-factor models impose perfect instantaneous correlation between all forward rates. Empirically, yield curve movements are driven by multiple independent factors, and one-factor models cannot capture:

- Curve steepening/flattening (requires at least two factors)
- Butterfly movements (requires at least three factors)
- Basis risk between different tenors

### General d-Factor HJM

With $d$ independent Brownian motions $W_t^1, \ldots, W_t^d$:

$$
df(t,T) = \alpha(t,T)\,dt + \sum_{i=1}^{d} \sigma_i(t,T)\,dW_t^i
$$

The instantaneous variance of $f(t,T)$ is

$$
\text{Var}(df(t,T)) = \sum_{i=1}^{d} \sigma_i(t,T)^2 \, dt
$$

The instantaneous correlation between forward rates at maturities $T$ and $S$ is

$$
\rho(t; T, S) = \frac{\sum_{i=1}^{d} \sigma_i(t,T) \, \sigma_i(t,S)}{\sqrt{\sum_{i=1}^{d} \sigma_i(t,T)^2} \cdot \sqrt{\sum_{i=1}^{d} \sigma_i(t,S)^2}}
$$

With multiple factors, this correlation is less than one for $T \neq S$, allowing non-parallel curve movements.

### Two-Factor Example

A common two-factor specification is:

$$
\sigma_1(t,T) = \sigma_1 \, e^{-\kappa_1(T-t)}, \qquad \sigma_2(t,T) = \sigma_2 \, e^{-\kappa_2(T-t)}
$$

with $\kappa_1 < \kappa_2$. Factor 1 (slow decay) drives **level** shifts, while factor 2 (fast decay) drives **slope** changes. The correlation between forward rates at maturities $T$ and $S$ decreases as $|T - S|$ increases.

### Three-Factor Model

Adding a third factor with a humped volatility loading:

$$
\sigma_3(t,T) = \sigma_3 \, (T-t) \, e^{-\kappa_3(T-t)}
$$

captures **curvature** (butterfly) movements. This factor has zero loading at very short and very long maturities, peaking at an intermediate point.

---

## Separable Volatility Structures

### Definition

A volatility function is **separable** if it factors into a time component and a maturity component:

$$
\sigma_i(t,T) = \phi_i(t) \, \psi_i(T-t)
$$

where $\phi_i(t)$ depends on current time and $\psi_i(\tau)$ depends on time-to-maturity $\tau = T - t$.

### Time-Homogeneous Volatility

A special case of separability is **time-homogeneity**, where $\phi_i(t) = 1$:

$$
\sigma_i(t,T) = \psi_i(T-t)
$$

The volatility depends only on time-to-maturity. This produces stationary dynamics: the behavior of a 5-year forward rate is the same regardless of whether we observe it in 2025 or 2030.

### Advantages of Separability

- **Analytical tractability:** Bond prices and option formulas may admit closed-form expressions
- **Reduced calibration dimensionality:** Fewer parameters to estimate
- **Intuitive interpretation:** Time and maturity effects are decoupled
- **Markovian short rates:** Certain separable forms yield Markovian short-rate models (important for PDE-based pricing)

### The Markov Property

A separable one-factor HJM model with $\sigma(t,T) = \sigma(T-t)$ leads to a Markovian short rate if and only if $\sigma(T-t)$ is of the exponential form $\sigma \, e^{-\kappa(T-t)}$ (Carverhill's result). More generally, Ritchken and Sankarasubramanian showed that Markovianity is achieved when $\sigma(t,T) = \sigma(t,t) \, e^{-\int_t^T \kappa(u)\,du}$, requiring only one additional state variable.

---

## Principal Component Analysis of Yield Curves

### Motivation

Rather than choosing volatility structures a priori, one can extract them from historical yield curve data. PCA provides an empirical decomposition of yield curve movements into orthogonal factors.

### Setup

Let $\Delta f_k(T_j)$ denote the change in the forward rate at maturity $T_j$ on day $k$, for $j = 1, \ldots, m$ maturities and $k = 1, \ldots, N$ observations. Collect these into an $N \times m$ data matrix $X$.

### Covariance Matrix

The sample covariance matrix of forward rate changes is

$$
C = \frac{1}{N-1} X^\top X \in \mathbb{R}^{m \times m}
$$

where we assume $X$ is centered (mean-subtracted).

### Eigendecomposition

Decompose $C$ as

$$
C = V \Lambda V^\top
$$

where $\Lambda = \text{diag}(\lambda_1, \ldots, \lambda_m)$ with eigenvalues $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_m \geq 0$ and $V = [v_1, \ldots, v_m]$ is the orthogonal matrix of eigenvectors.

### Interpretation of Principal Components

The $i$-th principal component $v_i \in \mathbb{R}^m$ defines a pattern of yield curve movement. The eigenvalue $\lambda_i$ represents the variance explained by this component. The fraction of total variance explained by the first $d$ components is

$$
R_d = \frac{\sum_{i=1}^{d} \lambda_i}{\sum_{i=1}^{m} \lambda_i}
$$

### Empirical Results

Decades of empirical studies across multiple currencies consistently find:

| PC | Interpretation | Variance Explained | Cumulative |
|---|---|---|---|
| PC1 | Level (parallel shift) | ~80--85% | ~80--85% |
| PC2 | Slope (steepening/flattening) | ~10--12% | ~92--95% |
| PC3 | Curvature (butterfly) | ~3--5% | ~96--99% |

Three factors typically explain over 95% of yield curve variation. This motivates the use of 2--3 factor HJM models.

### From PCA to HJM Volatility Functions

The PCA eigenvectors define the HJM volatility loadings. Set

$$
\sigma_i(t,T) = \sqrt{\lambda_i} \, v_i(T-t)
$$

where $v_i(\tau)$ is the $i$-th eigenvector evaluated at time-to-maturity $\tau$. This produces a multi-factor HJM model that matches the observed covariance structure of yield curve movements.

In practice, the raw PCA loadings are often smoothed and parametrized (e.g., by fitting exponential or polynomial forms) to ensure regularity and facilitate calibration.

??? example "Stylized PCA Loadings"

    Typical shapes of the first three PCA loadings as functions of time-to-maturity $\tau$:

    - **PC1 (Level):** Approximately constant, $v_1(\tau) \approx c_1$ for all $\tau$. All maturities move together.
    - **PC2 (Slope):** Monotonically decreasing, $v_2(\tau) > 0$ for short $\tau$ and $v_2(\tau) < 0$ for long $\tau$. Short rates and long rates move in opposite directions.
    - **PC3 (Curvature):** Positive at short and long maturities, negative at intermediate maturities. The curve bows up or down at the belly.

---

## Piecewise Constant Volatility

### Definition

For calibration flexibility, the volatility can be specified as piecewise constant over both time and maturity intervals:

$$
\sigma_i(t,T) = \sigma_{i,k,l} \quad \text{for } T_{k-1} \leq t < T_k, \; T_{l-1} \leq T - t < T_l
$$

### Parameter Count

With $K$ time intervals, $L$ maturity intervals, and $d$ factors, the model has $d \times K \times L$ volatility parameters. This provides maximum calibration flexibility but introduces the risk of overfitting.

### Calibration Strategy

A common approach is to:

1. Fix the number of factors from PCA (typically $d = 2$ or $d = 3$)
2. Choose a coarse grid for time and maturity intervals
3. Calibrate to market cap/swaption prices using least-squares optimization
4. Apply regularization to ensure smoothness across grid points

---

## Comparison of Volatility Structures

| Specification | Parameters | Tractability | Curve Dynamics | Typical Use |
|---|---|---|---|---|
| Constant | 1 | Very high | Parallel only | Pedagogical |
| Exponential | 2 ($\sigma, \kappa$) | High | Level + limited slope | Short-rate models |
| Humped | 3--4 | Moderate | Level + hump | Cap calibration |
| Separable multi-factor | $2d$--$3d$ | Moderate | Level + slope + curvature | General purpose |
| Piecewise constant | $d \times K \times L$ | Low | Any | Full calibration |

---

## Key Takeaways

- The volatility function $\sigma(t,T)$ is the sole modeling input in HJM; the drift follows from no-arbitrage
- **One-factor models** impose perfect correlation between forward rates and produce only parallel shifts
- **Multi-factor models** allow level, slope, and curvature movements, consistent with empirical evidence
- **Separable structures** $\sigma_i(t,T) = \phi_i(t)\psi_i(T-t)$ balance tractability with flexibility
- **Principal component analysis** of historical yield curve data reveals that 2--3 factors explain over 95% of variation, guiding the choice of factor number and loadings
- **Piecewise constant** specifications offer maximum calibration flexibility at the cost of increased parameter count and reduced tractability

---

## Further Reading

- Rebonato (2004), *Volatility and Correlation*, Chapters on PCA and term structure
- Brigo & Mercurio (2006), *Interest Rate Models: Theory and Practice*, Chapter 5 (HJM)
- Filipović (2009), *Term-Structure Models: A Graduate Course*, Chapter 7
- Litterman & Scheinkman (1991), "Common Factors Affecting Bond Returns" (original PCA study)

---

## Exercises

**Exercise 1.** Consider a one-factor HJM model with constant volatility $\sigma(t, T) = 0.01$. Compute the correlation between changes in the 2-year and 10-year forward rates over a small time interval $dt$. Explain why this model implies that all forward rates are perfectly correlated and discuss the limitation for pricing instruments sensitive to curve shape (e.g., CMS spread options).

---

**Exercise 2.** A two-factor HJM model has exponential volatility structures $\sigma_1(t, T) = \sigma_1 e^{-\kappa_1(T-t)}$ and $\sigma_2(t, T) = \sigma_2 e^{-\kappa_2(T-t)}$ with $\sigma_1 = 0.010$, $\kappa_1 = 0.03$, $\sigma_2 = 0.008$, $\kappa_2 = 0.50$. Compute the instantaneous correlation between the 1-year and 10-year forward rates. How does this correlation depend on the relative magnitudes of the two factors?

---

**Exercise 3.** The humped volatility function $\sigma(t, T) = [\sigma_0 + \sigma_1(T-t)]e^{-\kappa(T-t)}$ is a common specification. For $\sigma_0 = 0.005$, $\sigma_1 = 0.003$, and $\kappa = 0.20$, find the time-to-maturity $\tau^* = T - t$ at which the volatility is maximized. Compute the peak volatility and the long-maturity asymptotic volatility.

---

**Exercise 4.** A principal component analysis of weekly changes in US Treasury zero rates (2Y, 5Y, 10Y, 30Y) produces the following first three eigenvectors:

| Maturity | PC1 (Level) | PC2 (Slope) | PC3 (Curvature) |
|---|---|---|---|
| 2Y | 0.45 | -0.60 | 0.55 |
| 5Y | 0.50 | -0.20 | -0.50 |
| 10Y | 0.52 | 0.30 | -0.30 |
| 30Y | 0.53 | 0.70 | 0.60 |

The eigenvalues are $\lambda_1 = 85$, $\lambda_2 = 10$, $\lambda_3 = 3$ (in basis points squared per week). What fraction of total variance is explained by the first two factors? Describe how you would use these eigenvectors to construct a three-factor HJM model.

---

**Exercise 5.** Explain the concept of a separable volatility structure $\sigma_i(t, T) = \phi_i(t)\,\psi_i(T-t)$ in the context of HJM. Why does separability simplify the computation of the drift condition? Show that for a separable specification, the drift becomes

$$
\alpha(t, T) = \sum_{i=1}^d \phi_i(t)^2\,\psi_i(T-t)\int_t^T \psi_i(u-t)\,du
$$

---

**Exercise 6.** A piecewise-constant volatility specification assigns a constant volatility to each forward rate in each time period: $\sigma(t, T) = \lambda_{j,k}$ for $t \in [t_{k-1}, t_k)$ and $T \in [T_{j-1}, T_j)$. For a model with 4 quarterly periods and 4 forward rates, write down the full volatility matrix $\Lambda = (\lambda_{j,k})$ and count the number of free parameters. Compare this with the 2--4 parameters of the abcd specification and discuss the trade-off.

---

**Exercise 7.** In a one-factor model, all forward rates are perfectly correlated. Prove this formally by showing that the instantaneous correlation

$$
\rho(T_1, T_2) = \frac{\sigma(t, T_1)\,\sigma(t, T_2)}{\sqrt{\sigma(t, T_1)^2\,\sigma(t, T_2)^2}} = 1
$$

for any $T_1, T_2$. Then show that in a two-factor model, the correlation is strictly less than 1 in general, and express it in terms of the factor loadings at $T_1$ and $T_2$.
