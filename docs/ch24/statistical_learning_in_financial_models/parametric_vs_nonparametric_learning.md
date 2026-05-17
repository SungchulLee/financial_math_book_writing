# Parametric vs Nonparametric Learning

Statistical learning methods in quantitative finance can be broadly classified into **parametric** and **nonparametric** approaches. This distinction reflects a fundamental trade-off between structural assumptions and flexibility, with profound implications for model stability, data efficiency, and out-of-sample performance.

---

## The Learning Problem

Consider the general supervised learning setup. We observe data $(X_1, Y_1), \ldots, (X_n, Y_n)$ drawn from some unknown joint distribution $\mathbb{P}_{X,Y}$ and seek to estimate a function $f^*$ that minimizes expected loss:

$$
f^* = \arg\min_{f \in \mathcal{F}} \mathbb{E}_{(X,Y) \sim \mathbb{P}}[L(Y, f(X))]
$$

where $\mathcal{F}$ is the hypothesis class and $L$ is a loss function (e.g., squared error $L(y, \hat{y}) = (y - \hat{y})^2$).

The choice of $\mathcal{F}$ determines whether our approach is parametric or nonparametric.

---

## Parametric Learning

### Definition

A **parametric model** assumes that the true function $f^*$ belongs to a family indexed by a finite-dimensional parameter:

$$
\mathcal{F}_{\text{param}} = \{f(\cdot; \theta) : \theta \in \Theta \subseteq \mathbb{R}^d\}
$$

The learning problem reduces to estimating $\theta$ from data.

### Examples in Finance

**Linear factor models.** Asset returns are modeled as:

$$
R_i = \alpha_i + \sum_{j=1}^k \beta_{ij} F_j + \varepsilon_i
$$

where $\theta = (\alpha_i, \beta_{i1}, \ldots, \beta_{ik})$ has dimension $k+1$.

**GARCH volatility models.** The conditional variance follows:

$$
\sigma_t^2 = \omega + \sum_{i=1}^p \alpha_i r_{t-i}^2 + \sum_{j=1}^q \beta_j \sigma_{t-j}^2
$$

with parameter vector $\theta = (\omega, \alpha_1, \ldots, \alpha_p, \beta_1, \ldots, \beta_q) \in \mathbb{R}^{p+q+1}$.

**Parametric option pricing.** Under Black–Scholes, the single parameter $\sigma$ (volatility) determines all option prices. Under Heston, we have $\theta = (v_0, \kappa, \bar{v}, \sigma_v, \rho) \in \mathbb{R}^5$.

### Maximum Likelihood Estimation

For parametric models with density $p(y|x; \theta)$, the maximum likelihood estimator is:

$$
\hat{\theta}_{\text{MLE}} = \arg\max_{\theta \in \Theta} \sum_{i=1}^n \log p(Y_i | X_i; \theta)
$$

Under regularity conditions, MLE achieves asymptotic efficiency:

$$
\sqrt{n}(\hat{\theta}_{\text{MLE}} - \theta^*) \xrightarrow{d} \mathcal{N}(0, \mathcal{I}(\theta^*)^{-1})
$$

where $\mathcal{I}(\theta)$ is the Fisher information matrix:

$$
\mathcal{I}(\theta) = -\mathbb{E}\left[\frac{\partial^2 \log p(Y|X;\theta)}{\partial \theta \partial \theta^\top}\right]
$$

### Convergence Rates

Parametric estimators typically achieve the **parametric rate** of convergence:

$$
\|\hat{\theta} - \theta^*\| = O_p(n^{-1/2})
$$

This rate is independent of the input dimension, making parametric methods highly data-efficient when the model is correctly specified.

### Model Misspecification

The critical vulnerability of parametric methods is **misspecification**. If $f^* \notin \mathcal{F}_{\text{param}}$, then even with infinite data, the best we can achieve is the pseudo-true parameter:

$$
\theta^\dagger = \arg\min_{\theta \in \Theta} D_{\text{KL}}(\mathbb{P}_{Y|X}^* \| \mathbb{P}_{Y|X}^\theta)
$$

where $D_{\text{KL}}$ denotes Kullback–Leibler divergence. The approximation error $\|f(\cdot; \theta^\dagger) - f^*\|$ does not vanish with more data.

---

## Nonparametric Learning

### Definition

**Nonparametric models** do not assume a fixed functional form. Instead, the hypothesis class grows with sample size:

$$
\mathcal{F}_{\text{nonparam}} = \{f : \mathcal{X} \to \mathbb{R} \mid f \text{ satisfies smoothness conditions}\}
$$

Common smoothness assumptions include Hölder continuity, bounded derivatives, or membership in a Sobolev space.

### Kernel Regression (Nadaraya–Watson Estimator)

Given observations $(X_i, Y_i)_{i=1}^n$, the kernel regression estimator is:

$$
\hat{f}_h(x) = \frac{\sum_{i=1}^n K_h(x - X_i) Y_i}{\sum_{i=1}^n K_h(x - X_i)}
$$

where $K_h(\cdot) = h^{-d} K(\cdot/h)$ is a scaled kernel (e.g., Gaussian) and $h > 0$ is the bandwidth.

**Bias-variance decomposition.** For the Nadaraya–Watson estimator:

$$
\text{Bias}[\hat{f}_h(x)] = \frac{h^2}{2} \mu_2(K) \text{tr}(\nabla^2 f(x)) + o(h^2)
$$

$$
\text{Var}[\hat{f}_h(x)] = \frac{R(K)}{nh^d p(x)} \sigma^2(x) + o((nh^d)^{-1})
$$

where $\mu_2(K) = \int u^2 K(u) du$, $R(K) = \int K(u)^2 du$, $p(x)$ is the density of $X$, and $\sigma^2(x) = \text{Var}(Y|X=x)$.

### Local Polynomial Regression

Local polynomial regression fits a polynomial of degree $p$ locally around each point $x$:

$$
\hat{\beta}(x) = \arg\min_{\beta} \sum_{i=1}^n K_h(x - X_i) \left(Y_i - \sum_{j=0}^p \beta_j (X_i - x)^j\right)^2
$$

The estimator is $\hat{f}(x) = \hat{\beta}_0(x)$. Local linear regression ($p=1$) has superior boundary behavior compared to Nadaraya–Watson.

### Regression Splines

**Cubic splines** approximate $f$ using piecewise polynomials with continuity constraints at knots $\xi_1 < \cdots < \xi_K$:

$$
\hat{f}(x) = \sum_{j=0}^3 \beta_j x^j + \sum_{k=1}^K \gamma_k (x - \xi_k)_+^3
$$

where $(u)_+ = \max(u, 0)$.

**Smoothing splines** solve:

$$
\hat{f} = \arg\min_{f} \left\{ \sum_{i=1}^n (Y_i - f(X_i))^2 + \lambda \int (f''(x))^2 dx \right\}
$$

where $\lambda > 0$ controls the smoothness penalty.

### k-Nearest Neighbors

The k-NN estimator averages responses from the $k$ closest training points:

$$
\hat{f}_k(x) = \frac{1}{k} \sum_{i \in N_k(x)} Y_i
$$

where $N_k(x)$ denotes the indices of the $k$ nearest neighbors of $x$.

### Convergence Rates and Stone's Theorem

**Theorem (Stone, 1982).** Let $f^*$ belong to the Hölder class $\mathcal{H}(\beta, L)$ of functions with bounded derivatives up to order $\lfloor \beta \rfloor$ and $\beta$-Hölder continuous highest derivative. Then for any nonparametric regression estimator:

$$
\inf_{\hat{f}} \sup_{f^* \in \mathcal{H}(\beta, L)} \mathbb{E}\|\hat{f} - f^*\|_2^2 \asymp n^{-\frac{2\beta}{2\beta + d}}
$$

This **minimax optimal rate** reveals the curse of dimensionality: as dimension $d$ increases, convergence slows dramatically.

**Example.** For twice-differentiable functions ($\beta = 2$): rate is $n^{-4/5}$ at $d=1$, $n^{-4/9}$ at $d=5$, $n^{-2/7}$ at $d=10$, $n^{-1/6}$ at $d=20$. Recall the effective sample size analysis (see [§ Curse of Dimensionality](curse_of_dimensionality.md)).

---

## Semi-Parametric Models

### Definition

**Semi-parametric models** combine parametric components for primary structure with nonparametric components for nuisance functions:

$$
\mathbb{E}[Y|X,Z] = g(X^\top \beta) + f(Z)
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
\mathbb{E}[\nabla \mathbb{E}[Y|X]] \propto \beta
$$

allowing consistent estimation of $\beta$ (up to scale) using kernel density estimates.

### Additive Models

Additive models assume:

$$
\mathbb{E}[Y|X_1, \ldots, X_d] = \alpha + \sum_{j=1}^d f_j(X_j)
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
dS_t = r S_t dt + \sigma(S_t, t) S_t dW_t^{\mathbb{Q}}
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
\sigma^2(k) = a + b\left(\rho(k-m) + \sqrt{(k-m)^2 + \sigma^2}\right)
$$

where $k = \log(K/F)$ is log-moneyness.

**Nonparametrically:** Kernel smoothing of observed implied volatilities:

$$
\hat{\sigma}_{\text{imp}}(K, T) = \frac{\sum_{i} K_h(K - K_i, T - T_i) \sigma_i^{\text{obs}}}{\sum_{i} K_h(K - K_i, T - T_i)}
$$

**Semi-parametrically:** Parametric term structure with nonparametric smile:

$$
\sigma_{\text{imp}}(K, T) = \sigma_{\text{ATM}}(T) \cdot g(K/S; T)
$$

where $\sigma_{\text{ATM}}(T)$ is parametric and $g$ is estimated nonparametrically.

### Return Prediction

For predicting returns $R_{t+1}$ from predictors $X_t$:

**Parametric (linear predictability):**

$$
R_{t+1} = \alpha + \beta^\top X_t + \varepsilon_{t+1}
$$

Campbell and Shiller's dividend-price ratio regression is a classic example.

**Nonparametric:**

$$
R_{t+1} = f(X_t) + \varepsilon_{t+1}
$$

estimated via kernel methods or trees.

**Empirical finding:** Recall the low-SNR regime in financial returns (see [§ Bias–Variance Trade-Off](bias_variance_trade_off.md)). Nonparametric methods frequently underperform simple linear models out-of-sample: the flexibility that allows fitting complex patterns also fits noise.

---

## Model Selection

### Information Criteria

For parametric models with $d$ parameters and maximized log-likelihood $\ell_n(\hat{\theta})$:

**Akaike Information Criterion** (Recall: $\text{AIC} = -2\ell_n(\hat{\theta}) + 2d$; see [§ Bias–Variance Trade-Off](bias_variance_trade_off.md)).

**Bayesian Information Criterion:**

$$
\text{BIC} = -2\ell_n(\hat{\theta}) + d \log n
$$

BIC penalizes complexity more heavily and is consistent (selects true model as $n \to \infty$ if it's in the candidate set).

### Cross-Validation

For nonparametric methods, cross-validation estimates out-of-sample error:

$$
\text{CV}(\lambda) = \frac{1}{n} \sum_{i=1}^n L(Y_i, \hat{f}_{-i}^\lambda(X_i))
$$

where $\hat{f}_{-i}^\lambda$ is fitted without observation $i$ using tuning parameter $\lambda$.

**Leave-one-out CV** is computationally expensive but has low variance. **K-fold CV** (typically $K = 5$ or $10$) balances bias and variance.

### Time Series Cross-Validation

Standard CV assumes i.i.d. data. For time series, use **rolling-window** or **expanding-window** validation:

$$
\text{CV}_{\text{rolling}} = \frac{1}{T-w-h+1} \sum_{t=w}^{T-h} L(Y_{t+h}, \hat{f}_{t-w+1:t}(X_t))
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

---

## Exercises

**Exercise 1.** Consider a GARCH(1,1) model $\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2$.

(a) How many parameters does this model have? What is the convergence rate for estimating them with $n$ observations?

(b) If the true conditional variance follows a regime-switching process, explain why the GARCH MLE converges to a pseudo-true parameter rather than the truth. What does this imply for risk forecasts?

??? success "Solution to Exercise 1"
    **(a)** The GARCH(1,1) model $\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2$ has **3 parameters**: $\theta = (\omega, \alpha, \beta)$. Since this is a parametric model with a finite-dimensional parameter vector $\theta \in \mathbb{R}^3$, the convergence rate for estimating these parameters (via MLE or quasi-MLE) is the standard parametric rate:

    $$
    \|\hat{\theta} - \theta^*\| = O_p(n^{-1/2})
    $$

    This rate is independent of the dimension of the input and depends only on having $n$ observations and the regularity of the likelihood.

    **(b)** If the true conditional variance follows a regime-switching process, e.g.,

    $$
    \sigma_t^2 = \begin{cases} \omega_1 + \alpha_1 r_{t-1}^2 + \beta_1 \sigma_{t-1}^2 & \text{in regime 1} \\ \omega_2 + \alpha_2 r_{t-1}^2 + \beta_2 \sigma_{t-1}^2 & \text{in regime 2} \end{cases}
    $$

    then the single-regime GARCH(1,1) is **misspecified**: the true DGP does not belong to $\mathcal{F}_{\text{param}}$. The MLE converges not to the true parameters but to the pseudo-true parameter:

    $$
    \theta^\dagger = \arg\min_{\theta \in \Theta} D_{\text{KL}}(\mathbb{P}^* \| \mathbb{P}^\theta)
    $$

    This pseudo-true parameter is the single-regime GARCH that is closest in KL divergence to the true regime-switching model. The approximation error $\|f(\cdot; \theta^\dagger) - f^*\|$ does **not** vanish as $n \to \infty$.

    **Implications for risk forecasts:** The GARCH model will produce volatility estimates that are a weighted average of the two regimes. In the high-volatility regime, GARCH will **underestimate** risk (its estimate is pulled down by the low-regime component), and in the low-volatility regime, it will **overestimate** risk. This systematic bias is particularly dangerous for tail risk measures (VaR, Expected Shortfall), where underestimation in crisis periods leads to inadequate capital reserves.

---

**Exercise 2.** For the Nadaraya–Watson kernel regression estimator with Gaussian kernel and bandwidth $h$, the bias is $O(h^2)$ and the variance is $O(1/(nh^d))$.

(a) Derive the optimal bandwidth $h^*$ that minimizes the mean integrated squared error by balancing bias and variance.

(b) Compute $h^*$ and the resulting MISE rate for $d = 1$ and $d = 10$ with $n = 1000$. Interpret the difference.

??? success "Solution to Exercise 2"
    **(a)** The mean integrated squared error (MISE) for the Nadaraya-Watson estimator is:

    $$
    \text{MISE}(h) = \int \left[\text{Bias}^2(x) + \text{Var}(x)\right] p(x) \, dx
    $$

    Using $\text{Bias}^2 = O(h^4)$ and $\text{Var} = O((nh^d)^{-1})$:

    $$
    \text{MISE}(h) = C_1 h^4 + \frac{C_2}{nh^d}
    $$

    To minimize, take the derivative with respect to $h$ and set it to zero:

    $$
    \frac{d}{dh}\text{MISE}(h) = 4C_1 h^3 - \frac{d \cdot C_2}{n h^{d+1}} = 0
    $$

    Solving for $h$:

    $$
    4C_1 h^3 = \frac{d \cdot C_2}{n h^{d+1}} \implies h^{4+d} = \frac{d \cdot C_2}{4 C_1 n}
    $$

    Therefore:

    $$
    h^* \propto n^{-1/(4+d)}
    $$

    Substituting back into the MISE expression:

    $$
    \text{MISE}^* = O\left(n^{-4/(4+d)}\right)
    $$

    **(b)** For $d = 1$ with $n = 1000$:

    $$
    h^* \propto 1000^{-1/5} = 1000^{-0.2} \approx 0.251
    $$

    $$
    \text{MISE}^* = O(1000^{-4/5}) = O(1000^{-0.8}) \approx O(0.004)
    $$

    For $d = 10$ with $n = 1000$:

    $$
    h^* \propto 1000^{-1/14} = 1000^{-0.071} \approx 0.632
    $$

    $$
    \text{MISE}^* = O(1000^{-4/14}) = O(1000^{-0.286}) \approx O(0.096)
    $$

    **Interpretation:** In one dimension, the MISE is approximately 0.004, indicating good estimation quality. In ten dimensions, the MISE is approximately 0.096---about 24 times larger. The optimal bandwidth $h^*$ in 10 dimensions is 0.632, meaning the "local" neighborhood spans 63% of the data range in each direction, which is hardly local at all. This illustrates the curse of dimensionality: with the same 1000 observations, moving from $d = 1$ to $d = 10$ drastically degrades nonparametric estimation quality.

---

**Exercise 3.** A partially linear model for returns is

$$
R_{t+1} = \beta \cdot \text{DivYield}_t + f(\text{Volatility}_t) + \varepsilon_{t+1}
$$

(a) Describe Robinson's differencing procedure to estimate $\beta$ at the parametric rate $\sqrt{n}$.

(b) Why is it advantageous to model the volatility effect nonparametrically while keeping the dividend yield effect linear?

??? success "Solution to Exercise 3"
    **(a)** Robinson's differencing procedure for the partially linear model $R_{t+1} = \beta \cdot \text{DivYield}_t + f(\text{Volatility}_t) + \varepsilon_{t+1}$ proceeds in three steps.

    **Step 1: Nonparametric regression of $R_{t+1}$ on $\text{Volatility}_t$.** Estimate $m_R(v) = \mathbb{E}[R_{t+1} | \text{Volatility}_t = v]$ using kernel regression (e.g., Nadaraya-Watson):

    $$
    \hat{m}_R(v) = \frac{\sum_t K_h(v - \text{Vol}_t) R_{t+1}}{\sum_t K_h(v - \text{Vol}_t)}
    $$

    **Step 2: Nonparametric regression of $\text{DivYield}_t$ on $\text{Volatility}_t$.** Similarly estimate $m_D(v) = \mathbb{E}[\text{DivYield}_t | \text{Volatility}_t = v]$:

    $$
    \hat{m}_D(v) = \frac{\sum_t K_h(v - \text{Vol}_t) \text{DivYield}_t}{\sum_t K_h(v - \text{Vol}_t)}
    $$

    **Step 3: OLS on residuals.** Compute the residuals:

    $$
    \tilde{R}_{t+1} = R_{t+1} - \hat{m}_R(\text{Vol}_t), \quad \tilde{D}_t = \text{DivYield}_t - \hat{m}_D(\text{Vol}_t)
    $$

    Then estimate $\beta$ by OLS:

    $$
    \hat{\beta} = \frac{\sum_t \tilde{D}_t \tilde{R}_{t+1}}{\sum_t \tilde{D}_t^2}
    $$

    The key insight is that by taking conditional expectations of the original equation:

    $$
    \mathbb{E}[R_{t+1} | \text{Vol}_t] = \beta \cdot \mathbb{E}[\text{DivYield}_t | \text{Vol}_t] + f(\text{Vol}_t) + 0
    $$

    Subtracting eliminates the nonparametric component $f$:

    $$
    R_{t+1} - \mathbb{E}[R_{t+1} | \text{Vol}_t] = \beta \left(\text{DivYield}_t - \mathbb{E}[\text{DivYield}_t | \text{Vol}_t]\right) + \varepsilon_{t+1}
    $$

    Under regularity conditions, $\hat{\beta}$ achieves $\sqrt{n}$-consistency because the nonparametric estimation errors in Steps 1 and 2 converge fast enough (at rate $n^{-2/(4+1)} = n^{-2/5}$) that they do not affect the asymptotic distribution of $\hat{\beta}$.

    **(b)** There are several reasons to model the volatility effect nonparametrically while keeping dividend yield linear:

    1. **Nonlinear volatility-return relationship:** The relationship between volatility and future returns is known to be nonlinear. At low volatility, expected returns may be moderate; at high volatility, there is a risk premium but also potential mean-reversion. A linear specification would miss these effects.

    2. **Linear dividend yield predictability:** The dividend-price ratio is a well-established linear predictor of returns (Campbell and Shiller, 1988). Economic theory (the present-value identity) supports a log-linear relationship.

    3. **Interpretability of $\beta$:** Keeping the dividend yield effect parametric yields a single interpretable coefficient $\beta$ that measures the marginal predictive effect of dividend yield, controlling for volatility.

    4. **Data efficiency:** The parametric component is estimated at rate $\sqrt{n}$ regardless of the nonparametric component. If both were nonparametric, estimation would be slower and require more data.

    5. **Avoiding the curse of dimensionality:** With two nonparametric components, we would need to estimate a bivariate surface, facing the curse of dimensionality. The semi-parametric approach reduces this to one parametric direction and one univariate nonparametric function.

---

**Exercise 4.** You are estimating the Black–Scholes implied volatility surface from 200 observed option prices.

(a) A parametric approach uses the SVI parameterization with 5 parameters per maturity slice. With 4 maturities, how many total parameters are estimated? What is the convergence rate?

(b) A nonparametric approach uses kernel smoothing in the $(K, T)$ plane. Using Stone's rate with $\beta = 2$ and $d = 2$, what is the convergence rate with 200 observations?

(c) Which approach would you recommend and why?

??? success "Solution to Exercise 4"
    **(a)** The SVI parameterization has 5 parameters per maturity slice: $(a, b, \rho, m, \sigma)$. With 4 maturities, the total number of parameters is:

    $$
    d = 5 \times 4 = 20
    $$

    Since this is a parametric model with $d = 20$ parameters, the convergence rate is the parametric rate:

    $$
    \|\hat{\theta} - \theta^*\| = O_p(n^{-1/2}) = O_p(200^{-1/2}) \approx O_p(0.071)
    $$

    **(b)** For the nonparametric kernel smoothing approach in the $(K, T)$ plane, we have $d = 2$ input dimensions. Using Stone's minimax rate with $\beta = 2$ (twice-differentiable functions):

    $$
    \text{MISE} = O\left(n^{-2\beta/(2\beta+d)}\right) = O\left(200^{-4/(4+2)}\right) = O\left(200^{-2/3}\right)
    $$

    Numerically:

    $$
    200^{-2/3} = (200)^{-0.667} \approx 0.029
    $$

    For comparison, the parametric rate gives $200^{-1} \approx 0.005$ for MSE (since parametric MSE is $O(n^{-1})$). The nonparametric rate is about 6 times worse.

    **(c)** With only 200 observations, the **parametric SVI approach is preferable** for the following reasons:

    1. **Better convergence rate:** The parametric rate $O(n^{-1})$ for MSE substantially outperforms the nonparametric rate $O(n^{-2/3})$ at $n = 200$.

    2. **No-arbitrage constraints:** The SVI parameterization can be constrained to satisfy static no-arbitrage conditions (e.g., non-negative butterfly spreads, non-negative calendar spreads). The nonparametric estimator may produce arbitrage-violable surfaces.

    3. **Extrapolation:** The SVI formula provides meaningful extrapolation to strikes and maturities not observed in the data. The kernel estimator degrades severely outside the data support.

    4. **Smoothness:** The parametric surface is automatically smooth, while the nonparametric estimator may be noisy with only 200 data points spread across two dimensions.

    5. **Parsimony:** 20 parameters for 200 observations gives a ratio of 1:10, which is reasonable. The nonparametric approach implicitly has an effective number of parameters comparable to $n$, leading to overfitting risk.

    The main caveat is that if the SVI functional form is a poor approximation to the true surface, the parametric approach introduces misspecification bias that cannot be reduced with more data.

---

**Exercise 5.** Compare AIC and BIC for selecting between a 3-factor and a 5-factor linear return model estimated on $n = 120$ monthly observations. If both models have log-likelihoods $\ell_3 = -340$ and $\ell_5 = -335$:

(a) Compute AIC and BIC for each model.

(b) Which model does each criterion select? Explain why they may disagree.

??? success "Solution to Exercise 5"
    **(a)** For the **3-factor model** ($d = 3$ parameters: intercept + 3 betas, so $d = 4$; but typically in this context $d$ counts the factor loadings plus intercept, so let us use $d = 3$ for factors + 1 for intercept = 4. However, the problem states $d = 3$ and $d = 5$ directly as model parameters):

    With $d_3 = 3$ (including intercept: actually the problem states 3-factor and 5-factor, so the number of parameters is $d_3 = 4$ and $d_5 = 6$ respectively if we count the intercept. Let us follow the convention that a $k$-factor model has $k + 1$ parameters).

    Actually, re-reading the problem, it says "3-factor" and "5-factor" models with log-likelihoods given. The standard convention is that a $k$-factor model has $d = k + 1$ parameters (intercept + $k$ slopes). So $d_3 = 4$ and $d_5 = 6$.

    **AIC:**

    $$
    \text{AIC}_3 = -2(-340) + 2(4) = 680 + 8 = 688
    $$

    $$
    \text{AIC}_5 = -2(-335) + 2(6) = 670 + 12 = 682
    $$

    **BIC:**

    $$
    \text{BIC}_3 = -2(-340) + 4 \log(120) = 680 + 4(4.787) = 680 + 19.15 = 699.15
    $$

    $$
    \text{BIC}_5 = -2(-335) + 6 \log(120) = 670 + 6(4.787) = 670 + 28.72 = 698.72
    $$

    **(b)** Both criteria prefer lower values.

    - **AIC selects the 5-factor model** ($\text{AIC}_5 = 682 < 688 = \text{AIC}_3$). The improvement in log-likelihood ($\Delta \ell = 5$) is large enough to justify the 2 additional parameters under AIC's penalty of $2 \times 2 = 4$.

    - **BIC selects the 5-factor model** as well ($\text{BIC}_5 = 698.72 < 699.15 = \text{BIC}_3$), though the margin is very narrow.

    In general, AIC and BIC can disagree because BIC penalizes complexity more heavily (penalty $d \log n$ vs. $2d$). For $n = 120$, $\log(120) \approx 4.79$, so BIC penalizes each additional parameter by about 4.79 vs. AIC's penalty of 2. Here the log-likelihood improvement of 5 per additional parameter is large enough that even BIC selects the 5-factor model, but barely. With a smaller improvement (e.g., $\ell_5 = -337$), BIC would select the 3-factor model while AIC might still prefer the 5-factor model. BIC is **consistent** (selects the true model as $n \to \infty$) while AIC tends to select slightly overfit models, but AIC is asymptotically efficient (minimizes prediction error).

---

**Exercise 6.** Explain why nonparametric return prediction models frequently underperform simple linear models out-of-sample in finance, despite being more flexible. Your answer should reference the signal-to-noise ratio, the curse of dimensionality, and the bias–variance trade-off.

??? success "Solution to Exercise 6"
    Nonparametric models frequently underperform simple linear models out-of-sample in financial return prediction due to the interaction of three factors:

    **1. Signal-to-noise ratio.** Financial returns have an extremely low signal-to-noise ratio. Daily equity returns exhibit $R^2 \approx 0.25\%$, meaning that the predictable component $\mu(X_t)$ is tiny relative to the noise $\varepsilon_{t+1}$:

    $$
    R_{t+1} = \underbrace{\mu(X_t)}_{\text{SNR} \approx 0.05} + \underbrace{\varepsilon_{t+1}}_{\sigma \approx 1\%}
    $$

    Any estimator's prediction error is $\text{MSE} = \text{Bias}^2 + \text{Variance} + \sigma^2$, and the irreducible error $\sigma^2$ dominates. The tiny signal means that even small amounts of variance in the estimator can overwhelm the bias reduction from using a more flexible model.

    **2. Curse of dimensionality.** Nonparametric methods suffer convergence rates that degrade with input dimension $d$. By Stone's theorem, the minimax rate is:

    $$
    \text{MSE}_{\text{nonpar}} = O\left(n^{-2\beta/(2\beta + d)}\right)
    $$

    With typical financial predictors ($d = 5$ to $20$) and sample sizes ($n \approx 250$ to $5000$), the effective sample size is very small. For example, with $\beta = 2$, $d = 10$, and $n = 1000$, the effective sample size is $n_{\text{eff}} \approx 8$---far too few to reliably estimate any nonlinear structure.

    By contrast, the parametric linear model achieves $\text{MSE}_{\text{param}} = O(n^{-1})$ regardless of $d$ (assuming correct specification or mild misspecification).

    **3. Bias-variance trade-off.** In the decomposition $\text{MSE} = \text{Bias}^2 + \text{Variance}$:

    - **Linear model:** Has potentially higher bias (if the true function is nonlinear) but very low variance due to few parameters. With $d + 1$ parameters and $n$ observations, variance is $O(d/n)$.
    - **Nonparametric model:** Has lower bias (can approximate any smooth function) but much higher variance because it effectively estimates many local parameters.

    When SNR is low, the bias from using a linear model is small in absolute terms (the nonlinear component of the signal is even smaller than the already-tiny linear signal). Meanwhile, the variance penalty of the nonparametric model is large. The net effect is:

    $$
    \text{MSE}_{\text{linear}} = \underbrace{\text{Bias}_{\text{linear}}^2}_{\text{small}} + \underbrace{\text{Var}_{\text{linear}}}_{\text{small}} < \underbrace{\text{Bias}_{\text{nonpar}}^2}_{\approx 0} + \underbrace{\text{Var}_{\text{nonpar}}}_{\text{large}} = \text{MSE}_{\text{nonpar}}
    $$

    In summary, the flexibility of nonparametric models is a liability in finance: the additional degrees of freedom fit noise rather than the weak signal, producing worse out-of-sample predictions. This is why simple linear models, ridge regression, and other heavily regularized approaches tend to dominate in empirical asset pricing.
