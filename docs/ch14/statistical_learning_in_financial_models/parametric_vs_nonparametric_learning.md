# Parametric vs Nonparametric Learning

Statistical learning methods in quantitative finance can be broadly classified into **parametric** and **nonparametric** approaches. This distinction reflects a fundamental trade-off between structural assumptions and flexibility, with profound implications for model stability, data efficiency, and out-of-sample performance.

---

## The Learning Problem

Consider the general supervised learning setup. We observe data $(X_1, Y_1), \ldots, (X_n, Y_n)$ drawn from some unknown joint distribution $\mathbb{P}_{X,Y}$ and seek to estimate a function $f^*$ that minimizes expected loss:

$$
f^* = \arg\min_{f \in \mathcal{F}} \mathbb{E}_{(X,Y) \sim \mathbb{P}}[L(Y, f(X))],
$$

where $\mathcal{F}$ is the hypothesis class and $L$ is a loss function (e.g., squared error $L(y, \hat{y}) = (y - \hat{y})^2$).

The choice of $\mathcal{F}$ determines whether our approach is parametric or nonparametric.

---

## Parametric Learning

### Definition

A **parametric model** assumes that the true function $f^*$ belongs to a family indexed by a finite-dimensional parameter:

$$
\mathcal{F}_{\text{param}} = \{f(\cdot; \theta) : \theta \in \Theta \subseteq \mathbb{R}^d\}.
$$

The learning problem reduces to estimating $\theta$ from data.

### Examples in Finance

**Linear factor models.** Asset returns are modeled as:

$$
R_i = \alpha_i + \sum_{j=1}^k \beta_{ij} F_j + \varepsilon_i,
$$

where $\theta = (\alpha_i, \beta_{i1}, \ldots, \beta_{ik})$ has dimension $k+1$.

**GARCH volatility models.** The conditional variance follows:

$$
\sigma_t^2 = \omega + \sum_{i=1}^p \alpha_i r_{t-i}^2 + \sum_{j=1}^q \beta_j \sigma_{t-j}^2,
$$

with parameter vector $\theta = (\omega, \alpha_1, \ldots, \alpha_p, \beta_1, \ldots, \beta_q) \in \mathbb{R}^{p+q+1}$.

**Parametric option pricing.** Under Black–Scholes, the single parameter $\sigma$ (volatility) determines all option prices. Under Heston, we have $\theta = (v_0, \kappa, \bar{v}, \sigma_v, \rho) \in \mathbb{R}^5$.

### Maximum Likelihood Estimation

For parametric models with density $p(y|x; \theta)$, the maximum likelihood estimator is:

$$
\hat{\theta}_{\text{MLE}} = \arg\max_{\theta \in \Theta} \sum_{i=1}^n \log p(Y_i | X_i; \theta).
$$

Under regularity conditions, MLE achieves asymptotic efficiency:

$$
\sqrt{n}(\hat{\theta}_{\text{MLE}} - \theta^*) \xrightarrow{d} \mathcal{N}(0, \mathcal{I}(\theta^*)^{-1}),
$$

where $\mathcal{I}(\theta)$ is the Fisher information matrix:

$$
\mathcal{I}(\theta) = -\mathbb{E}\left[\frac{\partial^2 \log p(Y|X;\theta)}{\partial \theta \partial \theta^\top}\right].
$$

### Convergence Rates

Parametric estimators typically achieve the **parametric rate** of convergence:

$$
\|\hat{\theta} - \theta^*\| = O_p(n^{-1/2}).
$$

This rate is independent of the input dimension, making parametric methods highly data-efficient when the model is correctly specified.

### Model Misspecification

The critical vulnerability of parametric methods is **misspecification**. If $f^* \notin \mathcal{F}_{\text{param}}$, then even with infinite data, the best we can achieve is the pseudo-true parameter:

$$
\theta^\dagger = \arg\min_{\theta \in \Theta} D_{\text{KL}}(\mathbb{P}_{Y|X}^* \| \mathbb{P}_{Y|X}^\theta),
$$

where $D_{\text{KL}}$ denotes Kullback–Leibler divergence. The approximation error $\|f(\cdot; \theta^\dagger) - f^*\|$ does not vanish with more data.

---

## Nonparametric Learning

### Definition

**Nonparametric models** do not assume a fixed functional form. Instead, the hypothesis class grows with sample size:

$$
\mathcal{F}_{\text{nonparam}} = \{f : \mathcal{X} \to \mathbb{R} \mid f \text{ satisfies smoothness conditions}\}.
$$

Common smoothness assumptions include Hölder continuity, bounded derivatives, or membership in a Sobolev space.

### Kernel Regression (Nadaraya–Watson Estimator)

Given observations $(X_i, Y_i)_{i=1}^n$, the kernel regression estimator is:

$$
\hat{f}_h(x) = \frac{\sum_{i=1}^n K_h(x - X_i) Y_i}{\sum_{i=1}^n K_h(x - X_i)},
$$

where $K_h(\cdot) = h^{-d} K(\cdot/h)$ is a scaled kernel (e.g., Gaussian) and $h > 0$ is the bandwidth.

**Bias-variance decomposition.** For the Nadaraya–Watson estimator:

$$
\text{Bias}[\hat{f}_h(x)] = \frac{h^2}{2} \mu_2(K) \text{tr}(\nabla^2 f(x)) + o(h^2),
$$

$$
\text{Var}[\hat{f}_h(x)] = \frac{R(K)}{nh^d p(x)} \sigma^2(x) + o((nh^d)^{-1}),
$$

where $\mu_2(K) = \int u^2 K(u) du$, $R(K) = \int K(u)^2 du$, $p(x)$ is the density of $X$, and $\sigma^2(x) = \text{Var}(Y|X=x)$.

### Local Polynomial Regression

Local polynomial regression fits a polynomial of degree $p$ locally around each point $x$:

$$
\hat{\beta}(x) = \arg\min_{\beta} \sum_{i=1}^n K_h(x - X_i) \left(Y_i - \sum_{j=0}^p \beta_j (X_i - x)^j\right)^2.
$$

The estimator is $\hat{f}(x) = \hat{\beta}_0(x)$. Local linear regression ($p=1$) has superior boundary behavior compared to Nadaraya–Watson.

### Regression Splines

**Cubic splines** approximate $f$ using piecewise polynomials with continuity constraints at knots $\xi_1 < \cdots < \xi_K$:

$$
\hat{f}(x) = \sum_{j=0}^3 \beta_j x^j + \sum_{k=1}^K \gamma_k (x - \xi_k)_+^3,
$$

where $(u)_+ = \max(u, 0)$.

**Smoothing splines** solve:

$$
\hat{f} = \arg\min_{f} \left\{ \sum_{i=1}^n (Y_i - f(X_i))^2 + \lambda \int (f''(x))^2 dx \right\},
$$

where $\lambda > 0$ controls the smoothness penalty.

### k-Nearest Neighbors

The k-NN estimator averages responses from the $k$ closest training points:

$$
\hat{f}_k(x) = \frac{1}{k} \sum_{i \in N_k(x)} Y_i,
$$

where $N_k(x)$ denotes the indices of the $k$ nearest neighbors of $x$.

### Convergence Rates and Stone's Theorem

**Theorem (Stone, 1982).** Let $f^*$ belong to the Hölder class $\mathcal{H}(\beta, L)$ of functions with bounded derivatives up to order $\lfloor \beta \rfloor$ and $\beta$-Hölder continuous highest derivative. Then for any nonparametric regression estimator:

$$
\inf_{\hat{f}} \sup_{f^* \in \mathcal{H}(\beta, L)} \mathbb{E}\|\hat{f} - f^*\|_2^2 \asymp n^{-\frac{2\beta}{2\beta + d}}.
$$

This **minimax optimal rate** reveals the curse of dimensionality: as dimension $d$ increases, convergence slows dramatically.

**Example.** For twice-differentiable functions ($\beta = 2$):
- $d = 1$: Rate is $n^{-4/5}$
- $d = 5$: Rate is $n^{-4/9}$  
- $d = 10$: Rate is $n^{-2/7}$
- $d = 20$: Rate is $n^{-1/6}$

With 1,000 observations, effective estimation in 20 dimensions requires smoothness equivalent to $1000^{1/6} \approx 3$ observations in one dimension.

---

## Semi-Parametric Models

### Definition

**Semi-parametric models** combine parametric components for primary structure with nonparametric components for nuisance functions:

$$
\mathbb{E}[Y|X,Z] = g(X^\top \beta) + f(Z),
$$

where $\beta \in \mathbb{R}^p$ is finite-dimensional and $f$ is nonparametric.

### Partially Linear Models

The partially linear model:

$$
Y = X^\top \beta + f(Z) + \varepsilon
$$

is estimated via **Robinson's differencing**:

1. Estimate $\mathbb{E}[Y|Z]$ and $\mathbb{E}[X|Z]$ nonparametrically
2. Compute residuals: $\tilde{Y} = Y - \hat{\mathbb{E}}[Y|Z]$, $\tilde{X} = X - \hat{\mathbb{E}}[X|Z]$
3. Estimate $\beta$ by OLS on residuals: $\hat{\beta} = (\tilde{X}^\top \tilde{X})^{-1} \tilde{X}^\top \tilde{Y}$

Under regularity conditions, $\hat{\beta}$ achieves the parametric rate $\sqrt{n}$-consistency despite the nonparametric component.

### Single-Index Models

The single-index model:

$$
\mathbb{E}[Y|X] = g(X^\top \beta)
$$

reduces a high-dimensional regression to estimating a direction $\beta$ and a univariate link function $g$.

**Average derivative estimation.** Under suitable conditions:

$$
\mathbb{E}[\nabla \mathbb{E}[Y|X]] \propto \beta,
$$

allowing consistent estimation of $\beta$ (up to scale) using kernel density estimates.

### Additive Models

Additive models assume:

$$
\mathbb{E}[Y|X_1, \ldots, X_d] = \alpha + \sum_{j=1}^d f_j(X_j).
$$

The **backfitting algorithm** iteratively estimates each $f_j$:

1. Initialize $\hat{f}_j^{(0)} = 0$ for all $j$
2. For $m = 1, 2, \ldots$:
   - For $j = 1, \ldots, d$:
     $$\hat{f}_j^{(m)} = \mathcal{S}_j\left(Y - \hat{\alpha} - \sum_{k \neq j} \hat{f}_k^{(m-1)}\right)$$
   where $\mathcal{S}_j$ is a univariate smoother
3. Iterate until convergence

Additive models achieve the univariate rate $n^{-2\beta/(2\beta+1)}$ rather than the multivariate rate, circumventing the curse of dimensionality under the additivity assumption.

---

## Financial Applications and Considerations

### Option Pricing: Parametric vs Nonparametric

**Parametric approach (risk-neutral).** Assume dynamics under $\mathbb{Q}$:

$$
dS_t = r S_t dt + \sigma(S_t, t) S_t dW_t^{\mathbb{Q}},
$$

with parametric volatility $\sigma(S, t; \theta)$. Option prices are computed via PDE or Monte Carlo.

**Nonparametric approach.** Directly estimate the option pricing function:

$$
C(S, K, T) = \hat{f}(S, K, T)
$$

from observed prices, without specifying dynamics.

**Trade-offs:**
- Parametric: Ensures no-arbitrage (if model is arbitrage-free), extrapolates consistently, but may misspecify dynamics
- Nonparametric: Flexible fit to observed prices, but may violate no-arbitrage, poor extrapolation

### Volatility Surface Estimation

The implied volatility surface $\sigma_{\text{imp}}(K, T)$ can be estimated:

**Parametrically:** SVI parameterization (see Chapter 8):

$$
\sigma^2(k) = a + b\left(\rho(k-m) + \sqrt{(k-m)^2 + \sigma^2}\right),
$$

where $k = \log(K/F)$ is log-moneyness.

**Nonparametrically:** Kernel smoothing of observed implied volatilities:

$$
\hat{\sigma}_{\text{imp}}(K, T) = \frac{\sum_{i} K_h(K - K_i, T - T_i) \sigma_i^{\text{obs}}}{\sum_{i} K_h(K - K_i, T - T_i)}.
$$

**Semi-parametrically:** Parametric term structure with nonparametric smile:

$$
\sigma_{\text{imp}}(K, T) = \sigma_{\text{ATM}}(T) \cdot g(K/S; T),
$$

where $\sigma_{\text{ATM}}(T)$ is parametric and $g$ is estimated nonparametrically.

### Return Prediction

For predicting returns $R_{t+1}$ from predictors $X_t$:

**Parametric (linear predictability):**

$$
R_{t+1} = \alpha + \beta^\top X_t + \varepsilon_{t+1}.
$$

Campbell and Shiller's dividend-price ratio regression is a classic example.

**Nonparametric:**

$$
R_{t+1} = f(X_t) + \varepsilon_{t+1},
$$

estimated via kernel methods or trees.

**Empirical finding:** Due to low signal-to-noise ratios in returns (often $R^2 < 0.05$), nonparametric methods frequently underperform simple linear models out-of-sample. The flexibility that allows fitting complex patterns also fits noise.

---

## Model Selection

### Information Criteria

For parametric models with $d$ parameters and maximized log-likelihood $\ell_n(\hat{\theta})$:

**Akaike Information Criterion:**

$$
\text{AIC} = -2\ell_n(\hat{\theta}) + 2d.
$$

**Bayesian Information Criterion:**

$$
\text{BIC} = -2\ell_n(\hat{\theta}) + d \log n.
$$

BIC penalizes complexity more heavily and is consistent (selects true model as $n \to \infty$ if it's in the candidate set).

### Cross-Validation

For nonparametric methods, cross-validation estimates out-of-sample error:

$$
\text{CV}(\lambda) = \frac{1}{n} \sum_{i=1}^n L(Y_i, \hat{f}_{-i}^\lambda(X_i)),
$$

where $\hat{f}_{-i}^\lambda$ is fitted without observation $i$ using tuning parameter $\lambda$.

**Leave-one-out CV** is computationally expensive but has low variance. **K-fold CV** (typically $K = 5$ or $10$) balances bias and variance.

### Time Series Cross-Validation

Standard CV assumes i.i.d. data. For time series, use **rolling-window** or **expanding-window** validation:

$$
\text{CV}_{\text{rolling}} = \frac{1}{T-w-h+1} \sum_{t=w}^{T-h} L(Y_{t+h}, \hat{f}_{t-w+1:t}(X_t)),
$$

where $w$ is window size and $h$ is forecast horizon.

---

## Statistical Properties Summary

| Property | Parametric | Nonparametric |
|----------|------------|---------------|
| Convergence rate | $O(n^{-1/2})$ | $O(n^{-2\beta/(2\beta+d)})$ |
| Dimension dependence | None | Severe |
| Misspecification | Inconsistent | Consistent |
| Interpretability | High | Low |
| Data efficiency | High | Low |
| Extrapolation | Good (if correct) | Poor |

---

## Key Takeaways

1. **Parametric models** assume finite-dimensional structure, achieving fast $\sqrt{n}$ convergence when correctly specified but suffering from misspecification bias.

2. **Nonparametric models** let data determine the functional form, achieving consistency under weak assumptions but at slower rates that degrade with dimension.

3. **Semi-parametric models** combine parametric structure for interpretable components with nonparametric flexibility for nuisance functions.

4. **In finance**, low signal-to-noise ratios and limited effective sample sizes often favor simpler parametric models, despite potential misspecification.

5. **Model selection** via cross-validation (appropriately adapted for time series) is essential for choosing complexity levels.

---

## Further Reading

- Hastie, Tibshirani & Friedman, *The Elements of Statistical Learning*, Chapters 2–6
- Tsybakov, *Introduction to Nonparametric Estimation*
- Fan & Gijbels, *Local Polynomial Modelling and Its Applications*
- Aït-Sahalia & Lo (1998), "Nonparametric Estimation of State-Price Densities"
- Robinson (1988), "Root-N-Consistent Semiparametric Regression"
