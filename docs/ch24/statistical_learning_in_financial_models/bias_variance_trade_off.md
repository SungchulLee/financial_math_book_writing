# Bias–Variance Trade-Off

The **bias–variance trade-off** is a fundamental principle in statistical learning that governs the balance between model complexity and generalization. Understanding this trade-off is essential for building robust financial models that perform well out-of-sample.

---

## The Prediction Problem

Consider predicting a response $Y$ from features $X$ using an estimator $\hat{f}$ trained on data $\mathcal{D}_n = \{(X_i, Y_i)\}_{i=1}^n$. Assume the true data-generating process is:

$$
Y = f^*(X) + \varepsilon, \quad \mathbb{E}[\varepsilon | X] = 0, \quad \text{Var}(\varepsilon | X) = \sigma^2(X)
$$

The goal is to minimize the **expected prediction error** (EPE) at a new point $x_0$:

$$
\text{EPE}(x_0) = \mathbb{E}_{Y_0, \mathcal{D}_n}\left[(Y_0 - \hat{f}(x_0))^2\right]
$$

where the expectation is over both the new observation $Y_0$ and the training data $\mathcal{D}_n$.

---

## Bias–Variance Decomposition

### Theorem (Bias–Variance Decomposition)

For squared error loss, the expected prediction error decomposes as:

$$
\text{EPE}(x_0) = \underbrace{\sigma^2(x_0)}_{\text{Irreducible Error}} + \underbrace{\left(\mathbb{E}_{\mathcal{D}_n}[\hat{f}(x_0)] - f^*(x_0)\right)^2}_{\text{Bias}^2} + \underbrace{\mathbb{E}_{\mathcal{D}_n}\left[\left(\hat{f}(x_0) - \mathbb{E}_{\mathcal{D}_n}[\hat{f}(x_0)]\right)^2\right]}_{\text{Variance}}
$$

More compactly:

$$
\text{EPE}(x_0) = \sigma^2(x_0) + \text{Bias}^2[\hat{f}(x_0)] + \text{Var}[\hat{f}(x_0)]
$$

### Proof

Begin by expanding the squared error:

$$
\mathbb{E}[(Y_0 - \hat{f}(x_0))^2] = \mathbb{E}[(Y_0 - f^*(x_0) + f^*(x_0) - \hat{f}(x_0))^2]
$$

Expanding the square:

$$
= \mathbb{E}[(Y_0 - f^*(x_0))^2] + \mathbb{E}[(f^*(x_0) - \hat{f}(x_0))^2] + 2\mathbb{E}[(Y_0 - f^*(x_0))(f^*(x_0) - \hat{f}(x_0))]
$$

**First term:** Since $Y_0 = f^*(x_0) + \varepsilon_0$ with $\mathbb{E}[\varepsilon_0] = 0$:

$$
\mathbb{E}[(Y_0 - f^*(x_0))^2] = \mathbb{E}[\varepsilon_0^2] = \sigma^2(x_0)
$$

**Cross term:** Note that $Y_0 - f^*(x_0) = \varepsilon_0$ is independent of $\mathcal{D}_n$ (and hence of $\hat{f}$):

$$
\mathbb{E}[(Y_0 - f^*(x_0))(f^*(x_0) - \hat{f}(x_0))] = \mathbb{E}[\varepsilon_0] \cdot \mathbb{E}[f^*(x_0) - \hat{f}(x_0)] = 0
$$

**Second term:** Let $\bar{f}(x_0) = \mathbb{E}_{\mathcal{D}_n}[\hat{f}(x_0)]$. Then:

$$
\mathbb{E}[(f^*(x_0) - \hat{f}(x_0))^2] = \mathbb{E}[(f^*(x_0) - \bar{f}(x_0) + \bar{f}(x_0) - \hat{f}(x_0))^2]
$$

Expanding:

$$
= (f^*(x_0) - \bar{f}(x_0))^2 + \mathbb{E}[(\hat{f}(x_0) - \bar{f}(x_0))^2] + 2(f^*(x_0) - \bar{f}(x_0))\mathbb{E}[\bar{f}(x_0) - \hat{f}(x_0)]
$$

The cross term vanishes since $\mathbb{E}[\hat{f}(x_0) - \bar{f}(x_0)] = 0$ by definition of $\bar{f}$.

Thus:

$$
\mathbb{E}[(f^*(x_0) - \hat{f}(x_0))^2] = (f^*(x_0) - \bar{f}(x_0))^2 + \mathbb{E}[(\hat{f}(x_0) - \bar{f}(x_0))^2] = \text{Bias}^2 + \text{Var}
$$

$\square$

---

## Interpretation of Components

### Irreducible Error

The term $\sigma^2(x_0) = \text{Var}(Y|X = x_0)$ represents inherent noise in the data-generating process. No estimator can reduce this component—it sets a lower bound on achievable prediction error.

In finance, irreducible error is often large:
- Daily equity returns: $\sigma \approx 1\%$, signal (expected return) $\approx 0.05\%$
- Signal-to-noise ratio: $\text{SNR} = |\mu|/\sigma \approx 0.05$

This low SNR means that even optimal predictors explain only a tiny fraction of variance.

### Bias

**Bias** measures systematic error due to model misspecification:

$$
\text{Bias}[\hat{f}(x_0)] = \mathbb{E}_{\mathcal{D}_n}[\hat{f}(x_0)] - f^*(x_0)
$$

Bias arises when:
- The model class is too restrictive (e.g., fitting a line to a quadratic relationship)
- Regularization shrinks estimates toward a fixed target
- Prior beliefs in Bayesian estimation are incorrect

**High bias** indicates **underfitting**: the model fails to capture systematic patterns in the data.

### Variance

**Variance** measures sensitivity to training data fluctuations:

$$
\text{Var}[\hat{f}(x_0)] = \mathbb{E}_{\mathcal{D}_n}\left[(\hat{f}(x_0) - \bar{f}(x_0))^2\right]
$$

Variance is high when:
- The model is overly flexible
- Sample size is small
- Features are highly collinear
- Noise level is high

**High variance** indicates **overfitting**: the model fits noise rather than signal.

---

## The Trade-Off

### Complexity and the Trade-Off

As model complexity increases:
- **Bias decreases**: More flexible models can approximate $f^*$ more closely
- **Variance increases**: More parameters to estimate from the same data

The optimal complexity minimizes total error $\text{Bias}^2 + \text{Variance}$.

### Mathematical Illustration: Polynomial Regression

Consider fitting a polynomial of degree $p$ to data from $Y = f^*(X) + \varepsilon$.

For the estimator $\hat{f}_p(x) = \sum_{j=0}^p \hat{\beta}_j x^j$:

**Bias:** If $f^*$ is a polynomial of degree $q$:
- $p < q$: $\text{Bias} \neq 0$ (underfitting)
- $p \geq q$: $\text{Bias} = 0$ (correctly or overspecified)

**Variance:** For OLS estimator with design matrix $\mathbf{X}$:

$$
\text{Var}[\hat{f}_p(x_0)] = \sigma^2 \mathbf{x}_0^\top (\mathbf{X}^\top \mathbf{X})^{-1} \mathbf{x}_0
$$

where $\mathbf{x}_0 = (1, x_0, x_0^2, \ldots, x_0^p)^\top$.

As $p$ increases, $(\mathbf{X}^\top \mathbf{X})^{-1}$ becomes more ill-conditioned, and variance grows.

### Regularization and Bias–Variance

**Ridge regression** adds an $\ell_2$ penalty:

$$
\hat{\beta}_{\text{ridge}} = \arg\min_\beta \left\{ \sum_{i=1}^n (Y_i - X_i^\top \beta)^2 + \lambda \|\beta\|_2^2 \right\} = (\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^\top \mathbf{Y}
$$

**Effect on bias and variance:**

$$
\text{Bias}[\hat{\beta}_{\text{ridge}}] = -\lambda (\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I})^{-1} \beta^*
$$

$$
\text{Var}[\hat{\beta}_{\text{ridge}}] = \sigma^2 (\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I})^{-1} \mathbf{X}^\top \mathbf{X} (\mathbf{X}^\top \mathbf{X} + \lambda \mathbf{I})^{-1}
$$

As $\lambda$ increases:
- Bias increases (shrinkage toward zero)
- Variance decreases (regularization stabilizes estimates)

The optimal $\lambda$ minimizes total prediction error.

---

## Bias–Variance for Different Estimators

### k-Nearest Neighbors

For k-NN regression:

$$
\hat{f}_k(x) = \frac{1}{k} \sum_{i \in N_k(x)} Y_i
$$

**Bias:** As $k$ increases, we average over a larger neighborhood:

$$
\text{Bias}[\hat{f}_k(x)] \approx \frac{1}{2} \Delta f(x) \cdot r_k^2(x)
$$

where $r_k(x)$ is the distance to the $k$-th nearest neighbor and $\Delta f$ is the Laplacian.

**Variance:**

$$
\text{Var}[\hat{f}_k(x)] = \frac{\sigma^2}{k}
$$

- Small $k$: Low bias, high variance (overfit)
- Large $k$: High bias, low variance (underfit)

Optimal $k$ balances these effects, typically $k \propto n^{4/(4+d)}$ for smooth functions.

### Kernel Regression

For Nadaraya–Watson with bandwidth $h$:

$$
\text{Bias}[\hat{f}_h(x)] = O(h^2), \quad \text{Var}[\hat{f}_h(x)] = O((nh^d)^{-1})
$$

Mean squared error:

$$
\text{MSE} = O(h^4) + O((nh^d)^{-1})
$$

Optimal bandwidth: $h^* \propto n^{-1/(4+d)}$, giving $\text{MSE}^* = O(n^{-4/(4+d)})$.

### Neural Networks

For neural networks with $M$ hidden units:

- **Approximation error** (related to bias): Decreases with $M$ as the network can represent more complex functions
- **Estimation error** (related to variance): Increases with $M$ as more parameters require more data

Modern deep learning often operates in the **overparameterized regime** ($M \gg n$), where classical bias–variance intuition requires modification (see "double descent" phenomenon below).

---

## Integrated Mean Squared Error

For global assessment, we integrate over the input distribution:

$$
\text{IMSE} = \int \text{MSE}(x) \, p(x) \, dx = \int \left[\text{Bias}^2(x) + \text{Var}(x)\right] p(x) \, dx
$$

This is often estimated via cross-validation:

$$
\widehat{\text{IMSE}} \approx \frac{1}{n} \sum_{i=1}^n (Y_i - \hat{f}_{-i}(X_i))^2
$$

---

## Financial Data Characteristics

### Low Signal-to-Noise Ratio

In financial prediction:

$$
R_{t+1} = \underbrace{\mu(X_t)}_{\text{small}} + \underbrace{\varepsilon_{t+1}}_{\text{large}}
$$

With $|\mu| \approx 0.05\%$ daily and $\sigma \approx 1\%$, the irreducible error dominates:

$$
R^2 = \frac{\text{Var}(\mu(X))}{\text{Var}(R)} \approx \frac{(0.0005)^2}{(0.01)^2} = 0.0025 = 0.25\%
$$

Even a perfect model explains only $\sim 0.25\%$ of daily return variance!

**Implication:** Variance reduction is paramount. Simple models with low variance often outperform complex models with lower bias but higher variance.

### Effective Sample Size

Financial time series exhibit:
- **Autocorrelation:** Reduces effective sample size
- **Heteroskedasticity:** Some observations more informative than others
- **Structural breaks:** Historical data may not represent future dynamics

Effective sample size:

$$
n_{\text{eff}} = \frac{n}{1 + 2\sum_{k=1}^{\infty} \rho_k} \ll n
$$

where $\rho_k$ is autocorrelation at lag $k$. For highly persistent series, $n_{\text{eff}}$ can be orders of magnitude smaller than $n$.

### Non-Stationarity

If the true function $f^*_t$ changes over time, using all historical data introduces bias:

$$
\text{Bias} = \mathbb{E}[\hat{f}] - f^*_T \neq 0
$$

even if $\mathbb{E}[\hat{f}] = \bar{f}^*$ (average over time).

Rolling windows trade bias against variance:
- **Short windows:** Low bias (recent data), high variance (few observations)
- **Long windows:** High bias (old data), low variance (many observations)

---

## Double Descent and Modern Interpolation

### Classical U-Shaped Curve

Classical theory predicts a U-shaped test error curve:
- Underfitting region: High bias, low variance
- Optimal complexity: Minimum total error
- Overfitting region: Low bias, high variance

### Double Descent Phenomenon

Modern overparameterized models (deep networks, random forests with many trees) exhibit **double descent**:

1. **First descent:** Classical regime, test error decreases then increases
2. **Interpolation threshold:** Model perfectly fits training data
3. **Second descent:** Test error decreases again as model complexity grows further

**Mechanism:** In the overparameterized regime, among all interpolating solutions, the one with minimum norm (implicit regularization) generalizes well.

### Implications for Finance

1. **Ensemble methods** (bagging, boosting) reduce variance without much bias increase, often effective in finance
2. **Strong regularization** is typically beneficial given high noise
3. **Classical complexity selection** (cross-validation) remains the safest approach

---

## Practical Strategies for Variance Reduction

### Regularization

**$\ell_2$ regularization (Ridge):** Shrinks all coefficients proportionally:

$$
\hat{\beta}_{\text{ridge}} = \arg\min_\beta \left\{ \|\mathbf{y} - \mathbf{X}\beta\|_2^2 + \lambda \|\beta\|_2^2 \right\}
$$

**$\ell_1$ regularization (LASSO):** Induces sparsity:

$$
\hat{\beta}_{\text{lasso}} = \arg\min_\beta \left\{ \|\mathbf{y} - \mathbf{X}\beta\|_2^2 + \lambda \|\beta\|_1 \right\}
$$

**Elastic net:** Combines both:

$$
\hat{\beta}_{\text{EN}} = \arg\min_\beta \left\{ \|\mathbf{y} - \mathbf{X}\beta\|_2^2 + \lambda_1 \|\beta\|_1 + \lambda_2 \|\beta\|_2^2 \right\}
$$

### Bagging (Bootstrap Aggregating)

Generate $B$ bootstrap samples, fit model on each, average predictions:

$$
\hat{f}_{\text{bag}}(x) = \frac{1}{B} \sum_{b=1}^B \hat{f}^{(b)}(x)
$$

**Variance reduction:**

$$
\text{Var}[\hat{f}_{\text{bag}}] = \frac{1}{B}\text{Var}[\hat{f}] + \frac{B-1}{B}\text{Cov}[\hat{f}^{(1)}, \hat{f}^{(2)}]
$$

For uncorrelated estimators, variance reduces by factor $B$. In practice, correlation limits reduction.

### Model Averaging

Bayesian model averaging or frequentist combination:

$$
\hat{f}_{\text{avg}}(x) = \sum_{m=1}^M w_m \hat{f}_m(x)
$$

where weights $w_m$ reflect model quality (e.g., inverse variance weighting).

### Early Stopping

For iterative algorithms (gradient descent, boosting), stop before convergence:

- Early iterations: High bias, low variance
- Late iterations: Low bias, high variance

Validation-based early stopping selects optimal iteration count.

---

## Connection to Information-Theoretic Quantities

### Bias–Variance and KL Divergence

For probabilistic models, the expected log-likelihood decomposes similarly:

$$
\mathbb{E}_{\mathcal{D}_n}[D_{\text{KL}}(p^* \| \hat{p})] = D_{\text{KL}}(p^* \| \bar{p}) + \mathbb{E}_{\mathcal{D}_n}[D_{\text{KL}}(\bar{p} \| \hat{p})]
$$

where $\bar{p} = \mathbb{E}[\hat{p}]$.

The first term is "bias" (systematic divergence from truth), the second is "variance" (variability of the estimate).

### AIC and Bias Correction

Akaike's Information Criterion corrects for optimistic in-sample error:

$$
\text{AIC} = -2\ell_n(\hat{\theta}) + 2d
$$

where the penalty $2d$ approximates the expected optimism due to variance.

---

## Example: Factor Model Selection

Consider selecting among factor models for expected returns:

$$
\mathbb{E}[R_i] = \alpha_i + \sum_{j=1}^k \beta_{ij} \lambda_j
$$

With $k$ factors, we have $k$ factor risk premia $\lambda_j$ to estimate.

**Bias:** More factors can capture cross-sectional patterns
**Variance:** More parameters to estimate from limited assets and time periods

**Empirical finding (Harvey et al., 2016):** Many published factors are likely false discoveries—the variance inflation from testing many factors outweighs the bias reduction.

---

## Key Takeaways

1. **Bias** reflects systematic error from model restrictions; **variance** reflects sensitivity to training data.

2. **Optimal complexity** balances bias and variance to minimize total prediction error.

3. **Financial data** has extremely low signal-to-noise, making variance control paramount.

4. **Regularization, ensembling, and averaging** are effective variance reduction techniques.

5. **Cross-validation** (time-series appropriate) empirically navigates the bias–variance trade-off.

6. **Simple models often win** in finance due to high noise and limited effective samples.

---

## Further Reading

- Geman, Bienenstock & Doursat (1992), "Neural Networks and the Bias/Variance Dilemma"
- Hastie, Tibshirani & Friedman, *ESL*, Chapter 7
- Belkin et al. (2019), "Reconciling Modern Machine Learning and the Bias-Variance Trade-off"
- Gu, Kelly & Xiu (2020), "Empirical Asset Pricing via Machine Learning"
- Cochrane (2011), "Presidential Address: Discount Rates"

---

## Exercises

**Exercise 1.** A linear regression model $\hat{f}(x) = \hat{\beta}_0 + \hat{\beta}_1 x$ is fitted to daily S&P 500 returns predicted by the previous day's VIX level. The true relationship is $f^*(x) = 0.001 - 0.0002 x + 0.000001 x^2$ (slightly nonlinear). The noise standard deviation is $\sigma = 0.01$. (a) Compute the bias at $x_0 = 20$ (VIX = 20): the linear model omits the quadratic term, so $\text{Bias} = \mathbb{E}[\hat{f}(x_0)] - f^*(x_0)$ depends on the missing term. (b) For $n = 252$ daily observations, the variance of the linear prediction is approximately $\text{Var}[\hat{f}(x_0)] \approx \sigma^2(1/n + (x_0 - \bar{x})^2/\sum(x_i - \bar{x})^2)$. Estimate this variance. (c) Compare the total MSE of the linear model with a quadratic model at $x_0 = 20$. Which has lower total error?

??? success "Solution to Exercise 1"
    **(a)** The true relationship is $f^*(x) = 0.001 - 0.0002x + 0.000001x^2$. The linear model $\hat{f}(x) = \hat{\beta}_0 + \hat{\beta}_1 x$ cannot capture the quadratic term. If the linear model converges to its population projection onto $f^*$, the fitted linear function will approximate $f^*$ well in the region of the data but will systematically miss the curvature.

    The bias at $x_0 = 20$ is due to the omitted quadratic term. The population linear projection of $f^*(x) = 0.001 - 0.0002x + 0.000001x^2$ minimizes $\mathbb{E}[(f^*(X) - \beta_0 - \beta_1 X)^2]$. The omitted component is essentially $0.000001x^2$ evaluated around the mean.

    If VIX values are centered around $\bar{x} \approx 20$ with some spread, the linear model absorbs the quadratic term into the intercept and slope at the mean. The bias at $x_0 = 20$ is approximately the quadratic residual at that point. Since the linear projection passes through the mean of $f^*$, and $x_0 = 20$ may be near the mean, the bias at this point is relatively small. More precisely:

    $$
    \text{Bias}(x_0) \approx 0.000001(x_0^2 - \mathbb{E}[X^2]) + 0.000001 \mathbb{E}[X^2] - 0.000001\frac{\text{Cov}(X, X^2)}{\text{Var}(X)}(x_0 - \mathbb{E}[X])
    $$

    For simplicity, if VIX is approximately centered at 20, the bias at $x_0 = 20$ is small---on the order of $0.000001 \cdot \text{Var}(X) \approx 0.000001 \times 25 = 0.000025$ (assuming standard deviation of VIX $\approx 5$). So $\text{Bias}^2 \approx (0.000025)^2 = 6.25 \times 10^{-10}$.

    **(b)** The variance of the linear prediction at $x_0$ is:

    $$
    \text{Var}[\hat{f}(x_0)] \approx \sigma^2 \left(\frac{1}{n} + \frac{(x_0 - \bar{x})^2}{\sum_{i=1}^n (x_i - \bar{x})^2}\right)
    $$

    With $\sigma = 0.01$, $n = 252$, and assuming $x_0 = \bar{x} = 20$ (VIX at its mean):

    $$
    \text{Var}[\hat{f}(20)] \approx (0.01)^2 \cdot \frac{1}{252} = \frac{10^{-4}}{252} \approx 3.97 \times 10^{-7}
    $$

    If $x_0$ is not exactly at the mean, say $x_0 - \bar{x} = 5$ and $\sum(x_i - \bar{x})^2 \approx 252 \times 25 = 6300$:

    $$
    \text{Var}[\hat{f}(25)] \approx 10^{-4}\left(\frac{1}{252} + \frac{25}{6300}\right) = 10^{-4}(0.00397 + 0.00397) \approx 7.94 \times 10^{-7}
    $$

    **(c)** For the **linear model** at $x_0 = 20$:

    $$
    \text{MSE}_{\text{linear}} = \text{Bias}^2 + \text{Var} \approx 6.25 \times 10^{-10} + 3.97 \times 10^{-7} \approx 3.97 \times 10^{-7}
    $$

    The bias is negligible compared to the variance.

    For the **quadratic model** (3 parameters: intercept, linear, quadratic), the bias is zero (correctly specified), and the variance is approximately:

    $$
    \text{Var}_{\text{quad}} \approx \sigma^2 \cdot \frac{3}{n} = \frac{3 \times 10^{-4}}{252} \approx 1.19 \times 10^{-6}
    $$

    (This is approximate; the exact variance depends on the design matrix for the quadratic fit.)

    So:

    $$
    \text{MSE}_{\text{quad}} \approx 0 + 1.19 \times 10^{-6} = 1.19 \times 10^{-6}
    $$

    The **linear model has lower total MSE** ($3.97 \times 10^{-7} < 1.19 \times 10^{-6}$). The quadratic model eliminates a tiny bias but incurs substantially more variance from the additional parameter. This illustrates that when the omitted nonlinearity is small relative to the noise, simpler models win.

---

**Exercise 2.** The signal-to-noise ratio in daily equity return prediction is approximately $\text{SNR} = |\mu|/\sigma \approx 0.05$, giving $R^2 \approx 0.25\%$. (a) If a model achieves $R^2 = 2\%$ in-sample on daily data, argue that it is very likely overfitting. What in-sample $R^2$ would you expect from a true model with $R^2_{\text{true}} = 0.25\%$? (b) Compute the out-of-sample $R^2$ penalty due to estimation variance: $R^2_{\text{OOS}} \approx R^2_{\text{true}} - d/n$ where $d$ is the number of parameters and $n$ is the sample size. For $d = 10$ and $n = 252$, is $R^2_{\text{OOS}}$ positive? (c) Argue that in this low-SNR regime, models with fewer parameters (lower variance) consistently outperform models with many parameters (lower bias), even if the true relationship is complex.

??? success "Solution to Exercise 2"
    **(a)** A model achieving $R^2 = 2\%$ in-sample on daily data is almost certainly overfitting, since the true $R^2$ is approximately 0.25%.

    The in-sample $R^2$ is optimistically biased. For a model with $d$ parameters and $n$ observations, the expected in-sample $R^2$ exceeds the true $R^2$ by approximately:

    $$
    R^2_{\text{in-sample}} \approx R^2_{\text{true}} + \frac{d}{n}(1 - R^2_{\text{true}})
    $$

    For a true model with $R^2_{\text{true}} = 0.25\%$ and $d = 10$, $n = 252$:

    $$
    R^2_{\text{in-sample}} \approx 0.0025 + \frac{10}{252}(1 - 0.0025) \approx 0.0025 + 0.0397 \approx 4.2\%
    $$

    An in-sample $R^2$ of 2% could therefore arise from a model with no true predictive power at all (just from overfitting with about 5 parameters out of 252 observations). The expected in-sample $R^2$ from a true model is approximately $0.25\% + d/n \approx 0.25\% + 4\% = 4.2\%$ for 10 parameters. The 2% figure suggests either fewer parameters or some mild predictive power, but distinguishing these is difficult.

    **(b)** The out-of-sample $R^2$ penalty formula gives:

    $$
    R^2_{\text{OOS}} \approx R^2_{\text{true}} - \frac{d}{n} = 0.0025 - \frac{10}{252} = 0.0025 - 0.0397 = -0.0372
    $$

    The out-of-sample $R^2$ is **negative** ($-3.7\%$). This means the model performs worse than a simple historical mean forecast. With $d = 10$ parameters and $n = 252$ observations, the estimation variance overwhelms the true signal. The model would need $n > d / R^2_{\text{true}} = 10 / 0.0025 = 4000$ observations (approximately 16 years of daily data) for the out-of-sample $R^2$ to be positive.

    **(c)** In this low-SNR regime, the bias-variance trade-off heavily favors simple models:

    - The true $R^2$ is only 0.25%, so the maximum possible improvement from capturing nonlinearities or additional factors is bounded above by some small increment over 0.25%.
    - Each additional parameter adds approximately $1/n$ to the variance component of MSE.
    - For $n = 252$, each parameter costs roughly $1/252 \approx 0.4\%$ in out-of-sample $R^2$.

    Therefore, a model with even 1 parameter can barely break even, and a model with 10 parameters is almost certainly net-negative. The bias reduction from using many parameters or complex nonlinear models is bounded by the total signal strength ($R^2 \approx 0.25\%$), while the variance cost grows linearly with model complexity. Models with fewer parameters (lower variance) consistently outperform those with more parameters (lower bias) because the variance cost of complexity far exceeds the bias benefit in this extreme low-signal environment.

---

**Exercise 3.** Ridge regression estimates are $\hat{\beta}_{\text{ridge}} = (\mathbf{X}^\top \mathbf{X} + \lambda I)^{-1}\mathbf{X}^\top \mathbf{Y}$. For a factor model with $d = 50$ factors and $n = 120$ months: (a) The OLS estimator is ill-conditioned because $d/n = 0.42$. Show that $\hat{\beta}_{\text{OLS}}$ has high variance by noting that $\text{Var}[\hat{\beta}_{\text{OLS}}] = \sigma^2 (\mathbf{X}^\top \mathbf{X})^{-1}$ and small eigenvalues of $\mathbf{X}^\top \mathbf{X}$ inflate this. (b) Ridge shrinks eigenvalues by replacing $\lambda_j$ with $\lambda_j + \lambda$. Show that the MSE of $\hat{\beta}_{\text{ridge}}$ is $\sum_j \frac{\lambda^2 \beta_j^{*2}}{(\lambda_j + \lambda)^2} + \sigma^2 \sum_j \frac{\lambda_j}{(\lambda_j + \lambda)^2}$ (bias + variance). (c) Find the optimal $\lambda$ by differentiating the MSE and argue that it is positive whenever $d > 2$, proving that OLS is inadmissible.

??? success "Solution to Exercise 3"
    **(a)** The OLS estimator has covariance:

    $$
    \text{Cov}(\hat{\beta}_{\text{OLS}}) = \sigma^2 (\mathbf{X}^\top \mathbf{X})^{-1}
    $$

    Let the eigendecomposition of $\mathbf{X}^\top \mathbf{X}$ be $\sum_{j=1}^d \lambda_j v_j v_j^\top$. Then:

    $$
    (\mathbf{X}^\top \mathbf{X})^{-1} = \sum_{j=1}^d \frac{1}{\lambda_j} v_j v_j^\top
    $$

    The total variance (trace) is:

    $$
    \text{tr}(\text{Cov}(\hat{\beta}_{\text{OLS}})) = \sigma^2 \sum_{j=1}^d \frac{1}{\lambda_j}
    $$

    With $d = 50$ and $n = 120$, the ratio $d/n = 0.42$ is large. By random matrix theory (Marchenko-Pastur), even if the true covariance of factors is identity, the smallest sample eigenvalues are of order $(1 - \sqrt{d/n})^2 \approx (1 - 0.65)^2 = 0.12$ times $n$, so $\lambda_{\min} \approx 0.12 \times 120 = 14.5$. The corresponding contribution to variance is $\sigma^2/14.5$. With many small eigenvalues near this lower bound, the total variance $\sigma^2 \sum 1/\lambda_j$ becomes very large, making OLS highly unstable.

    **(b)** The ridge estimator in the eigenbasis of $\mathbf{X}^\top \mathbf{X}$ has, for each component $j$:

    $$
    \hat{\beta}_j^{\text{ridge}} = \frac{\lambda_j}{\lambda_j + \lambda} \hat{\beta}_j^{\text{OLS}}
    $$

    The bias of the $j$-th component is:

    $$
    \text{Bias}_j = \mathbb{E}[\hat{\beta}_j^{\text{ridge}}] - \beta_j^* = \frac{\lambda_j}{\lambda_j + \lambda}\beta_j^* - \beta_j^* = \frac{-\lambda}{\lambda_j + \lambda}\beta_j^*
    $$

    So $\text{Bias}_j^2 = \frac{\lambda^2 \beta_j^{*2}}{(\lambda_j + \lambda)^2}$.

    The variance of the $j$-th component is:

    $$
    \text{Var}_j = \text{Var}\left(\frac{\lambda_j}{\lambda_j + \lambda}\hat{\beta}_j^{\text{OLS}}\right) = \frac{\lambda_j^2}{(\lambda_j + \lambda)^2} \cdot \frac{\sigma^2}{\lambda_j} = \frac{\sigma^2 \lambda_j}{(\lambda_j + \lambda)^2}
    $$

    The total MSE is:

    $$
    \text{MSE}(\lambda) = \sum_{j=1}^d \left[\frac{\lambda^2 \beta_j^{*2}}{(\lambda_j + \lambda)^2} + \frac{\sigma^2 \lambda_j}{(\lambda_j + \lambda)^2}\right]
    $$

    **(c)** Differentiating the MSE with respect to $\lambda$ and evaluating at $\lambda = 0$:

    $$
    \frac{\partial \text{MSE}}{\partial \lambda}\bigg|_{\lambda=0} = \sum_{j=1}^d \left[\frac{2 \cdot 0 \cdot \beta_j^{*2}}{\lambda_j^2} - \frac{2\sigma^2}{\lambda_j^2}\right] = -\frac{2\sigma^2}{\lambda_j} \cdot d \cdot \text{(harmonic mean)}^{-1}
    $$

    More carefully, at $\lambda = 0$:

    $$
    \frac{\partial \text{MSE}}{\partial \lambda}\bigg|_{\lambda=0} = \sum_{j=1}^d \frac{2(0 \cdot \beta_j^{*2} \cdot \lambda_j - \sigma^2 \lambda_j)}{\lambda_j^3} \cdot \lambda_j = -2\sigma^2 \sum_{j=1}^d \frac{1}{\lambda_j^2} \cdot \lambda_j
    $$

    Let us compute this more carefully. Write $\text{MSE}(\lambda) = B(\lambda) + V(\lambda)$ where:

    $$
    B(\lambda) = \lambda^2 \sum_j \frac{\beta_j^{*2}}{(\lambda_j + \lambda)^2}, \quad V(\lambda) = \sigma^2 \sum_j \frac{\lambda_j}{(\lambda_j + \lambda)^2}
    $$

    $$
    B'(0) = 0 \quad \text{(since } B(\lambda) = O(\lambda^2) \text{)}
    $$

    $$
    V'(0) = -2\sigma^2 \sum_j \frac{\lambda_j}{(\lambda_j)^3} = -2\sigma^2 \sum_j \frac{1}{\lambda_j^2} < 0
    $$

    Wait---let us be precise. $V(\lambda) = \sigma^2 \sum_j \lambda_j (\lambda_j + \lambda)^{-2}$, so:

    $$
    V'(\lambda) = -2\sigma^2 \sum_j \frac{\lambda_j}{(\lambda_j + \lambda)^3}
    $$

    At $\lambda = 0$: $V'(0) = -2\sigma^2 \sum_j \lambda_j^{-2} < 0$.

    Since $\text{MSE}'(0) = B'(0) + V'(0) = 0 + V'(0) < 0$, the MSE is strictly decreasing at $\lambda = 0$. This means moving $\lambda$ from 0 to a small positive value always reduces MSE.

    Therefore the optimal $\lambda^* > 0$, which proves that **OLS ($\lambda = 0$) is inadmissible**: there always exists a ridge estimator with strictly lower MSE. This holds for any $d \geq 1$ (the original James-Stein result shows inadmissibility for $d \geq 3$ in the simpler normal means problem, but in the regression context with any noise level, the argument above shows $\lambda^* > 0$ always).

---

**Exercise 4.** Bagging (bootstrap aggregating) reduces variance. A random forest predicts stock returns using 100 trees, each fitted on a bootstrap sample. (a) If each tree has bias $b$ and variance $v$, and trees have pairwise correlation $\rho$, the bagged estimator has $\text{Var}_{\text{bag}} = \rho v + (1-\rho)v/B$ where $B = 100$ is the number of trees. Compute $\text{Var}_{\text{bag}}$ for $v = 0.01$, $\rho = 0.3$. (b) Explain why the bias of the bagged estimator is approximately unchanged: $\text{Bias}_{\text{bag}} \approx b$. (c) The random forest reduces $\rho$ by restricting each split to a random subset of features. If $\rho$ decreases from 0.3 to 0.1, recompute $\text{Var}_{\text{bag}}$. Discuss why decorrelation is the key mechanism.

??? success "Solution to Exercise 4"
    **(a)** Each tree has bias $b$ and variance $v$. The bagged estimator averages $B = 100$ trees with pairwise correlation $\rho$. The variance of the bagged estimator is:

    $$
    \text{Var}_{\text{bag}} = \rho v + \frac{(1-\rho)v}{B}
    $$

    With $v = 0.01$, $\rho = 0.3$, $B = 100$:

    $$
    \text{Var}_{\text{bag}} = 0.3 \times 0.01 + \frac{(1-0.3) \times 0.01}{100} = 0.003 + \frac{0.007}{100} = 0.003 + 0.00007 = 0.00307
    $$

    The variance is reduced from $v = 0.01$ to $0.00307$, a reduction of about 69%.

    **(b)** The bias of the bagged estimator is approximately unchanged because:

    $$
    \text{Bias}[\hat{f}_{\text{bag}}(x)] = \mathbb{E}\left[\frac{1}{B}\sum_{b=1}^B \hat{f}^{(b)}(x)\right] - f^*(x) = \frac{1}{B}\sum_{b=1}^B \mathbb{E}[\hat{f}^{(b)}(x)] - f^*(x)
    $$

    Each bootstrap estimator $\hat{f}^{(b)}$ is trained on a bootstrap sample of the same size $n$, so $\mathbb{E}[\hat{f}^{(b)}(x)] \approx \mathbb{E}[\hat{f}(x)]$ for each $b$ (the bias of a bootstrap estimator is approximately the same as the original estimator). Therefore:

    $$
    \text{Bias}[\hat{f}_{\text{bag}}(x)] \approx \mathbb{E}[\hat{f}(x)] - f^*(x) = b
    $$

    Bagging is a variance reduction technique that does not affect bias (to first order). The slight caveat is that bootstrap sampling with replacement changes the effective sample slightly (about 63.2% unique observations), which can marginally increase bias, but this effect is small.

    **(c)** With $\rho$ decreased from 0.3 to 0.1 (via random feature subsampling):

    $$
    \text{Var}_{\text{bag}} = 0.1 \times 0.01 + \frac{(1-0.1) \times 0.01}{100} = 0.001 + \frac{0.009}{100} = 0.001 + 0.00009 = 0.00109
    $$

    Compared to the original bagging variance of 0.00307, the random forest variance of 0.00109 is a further 64% reduction.

    **Why decorrelation is the key mechanism:** Looking at the variance formula $\text{Var}_{\text{bag}} = \rho v + (1-\rho)v/B$, for large $B$ the second term $(1-\rho)v/B$ becomes negligible. The irreducible variance floor is $\rho v$. Simply adding more trees (increasing $B$) cannot reduce variance below $\rho v$. The only way to push the floor down is to reduce the correlation $\rho$ between trees. The random forest achieves this by randomly restricting each split to a subset of $m \ll p$ features, so different trees use different features and make different splits, reducing their correlation. This decorrelation is the fundamental innovation that distinguishes random forests from simple bagging.

---

**Exercise 5.** The double descent phenomenon challenges classical bias-variance intuition. (a) Sketch the U-shaped classical test error curve and the double descent curve on the same axes, with model complexity on the x-axis. Label the interpolation threshold where the model perfectly fits the training data. (b) Explain the mechanism of the second descent: among all models that interpolate the training data, the minimum-norm solution generalizes well because it is implicitly regularized. (c) In finance, where $n$ is small and noise is high, argue that the interpolation threshold is reached at low complexity ($d \approx n$). The double descent region ($d \gg n$) requires massively overparameterized models. Is this regime practically relevant for financial prediction? Discuss.

??? success "Solution to Exercise 5"
    **(a)** The **classical U-shaped curve** starts with high test error at low complexity (high bias, low variance), decreases to an optimal point, then increases again at high complexity (low bias, high variance).

    The **double descent curve** follows the U-shape initially but then, at the **interpolation threshold** (where model complexity $d$ equals sample size $n$ and the model can perfectly fit the training data), the test error spikes sharply. Beyond this threshold, as $d$ continues to grow ($d \gg n$), the test error **decreases again**, forming a second descent.

    The key features to label on the plot:

    - Left region ($d \ll n$): classical underfit-to-overfit regime
    - Interpolation threshold ($d \approx n$): peak test error, model barely interpolates with high-norm solution
    - Right region ($d \gg n$): overparameterized regime, test error decreases

    **(b)** The mechanism of the second descent is **implicit regularization through minimum-norm interpolation**.

    When $d > n$, there are infinitely many solutions that perfectly interpolate the training data (zero training error). Among these, gradient descent (and related algorithms) converge to the **minimum-norm solution**:

    $$
    \hat{\beta} = \mathbf{X}^\top (\mathbf{X}\mathbf{X}^\top)^{-1} \mathbf{Y}
    $$

    This minimum-norm solution has a special structure: it distributes the interpolation requirement across many parameters, so each parameter is small. As $d$ grows far beyond $n$, each parameter becomes even smaller (the norm $\|\hat{\beta}\|$ decreases), providing an implicit regularization effect similar to explicit ridge regression. The interpolating solution becomes smoother as it has more degrees of freedom to achieve interpolation with a low-complexity function.

    **(c)** In finance, the interpolation threshold occurs at $d \approx n$. With typical financial sample sizes:

    - Monthly returns: $n \approx 120$ to $600$ observations
    - Daily returns: $n \approx 252$ to $5000$ observations

    The interpolation threshold is reached at modest complexity levels. The double descent region ($d \gg n$) requires massively overparameterized models (thousands to millions of parameters), which corresponds to very large neural networks or kernel machines.

    **Practical relevance is limited** for several reasons:

    1. Financial data has extremely low SNR ($R^2 \approx 0.25\%$). Even in the second descent regime, the implicit regularization must be very strong to avoid fitting noise, and the theoretical guarantees for benign interpolation typically require sufficient signal strength.

    2. Financial time series are non-stationary, so the stationarity assumptions underlying double descent theory may not hold.

    3. The sample sizes in finance are small enough that even modest overparameterization leads to the interpolation threshold, where performance is worst.

    4. Computational and interpretability requirements in finance favor simpler models.

    For these reasons, the **classical regime** (cross-validation to select optimal complexity well below the interpolation threshold) remains the most reliable approach for financial prediction. The double descent phenomenon is more relevant in domains with larger datasets and higher signal-to-noise ratios (e.g., image classification, natural language processing).

---

**Exercise 6.** A fund manager must choose the lookback window for estimating expected returns. Short windows (e.g., 1 year) have low bias but high variance; long windows (e.g., 10 years) have high bias (if the market has changed) but low variance. (a) Model the expected return as $\mu_t = \mu + \delta_t$ where $\delta_t$ is a slow drift with $\text{Var}(\delta_t) = \sigma_\delta^2 t$. The rolling-window estimator using the last $W$ observations has $\text{Bias}^2 \approx \sigma_\delta^2 W / 3$ and $\text{Var} \approx \sigma^2 / W$. (b) Minimize the total MSE to find the optimal window $W^* = (3\sigma^2 / \sigma_\delta^2)^{1/2}$. For $\sigma = 0.16$ (annualized), $\sigma_\delta = 0.02$/year, compute $W^*$ in years. (c) Relate this to the bias-variance tradeoff: faster drift (larger $\sigma_\delta$) favors shorter windows (lower bias), while higher noise ($\sigma$) favors longer windows (lower variance).

??? success "Solution to Exercise 6"
    **(a)** The rolling-window estimator using the last $W$ observations has:

    - **Bias:** The expected return drifts as $\mu_t = \mu + \delta_t$. The rolling mean estimates an average over $[t-W, t]$, which is centered at $t - W/2$ rather than $t$. If $\delta_t$ has variance $\sigma_\delta^2 t$ (random walk drift), the squared bias from using stale data is:

    $$
    \text{Bias}^2 \approx \frac{\sigma_\delta^2 W}{3}
    $$

    This arises because the average lag of observations in the window is $W/2$, and integrating the squared drift over the window gives $\sigma_\delta^2 \int_0^W (W - s)^2 / W^2 \, ds \cdot W = \sigma_\delta^2 W / 3$.

    - **Variance:** The estimation variance from averaging $W$ noisy observations is:

    $$
    \text{Var} \approx \frac{\sigma^2}{W}
    $$

    **(b)** The total MSE is:

    $$
    \text{MSE}(W) = \frac{\sigma_\delta^2 W}{3} + \frac{\sigma^2}{W}
    $$

    To minimize, take the derivative and set to zero:

    $$
    \frac{d}{dW}\text{MSE} = \frac{\sigma_\delta^2}{3} - \frac{\sigma^2}{W^2} = 0
    $$

    Solving:

    $$
    W^2 = \frac{3\sigma^2}{\sigma_\delta^2} \implies W^* = \left(\frac{3\sigma^2}{\sigma_\delta^2}\right)^{1/2}
    $$

    With $\sigma = 0.16$ (annualized) and $\sigma_\delta = 0.02$/year:

    $$
    W^* = \sqrt{\frac{3 \times 0.16^2}{0.02^2}} = \sqrt{\frac{3 \times 0.0256}{0.0004}} = \sqrt{\frac{0.0768}{0.0004}} = \sqrt{192} \approx 13.9 \text{ years}
    $$

    **(c)** This result directly illustrates the bias-variance trade-off:

    - **Faster drift (larger $\sigma_\delta$):** The denominator $\sigma_\delta^2$ increases, so $W^*$ decreases. When the market environment changes rapidly, old data becomes misleading (high bias), so shorter windows are needed to stay current.

    - **Higher noise (larger $\sigma$):** The numerator $\sigma^2$ increases, so $W^*$ increases. When returns are noisy, we need more observations to average out the noise (reduce variance), even at the cost of some staleness.

    The optimal window $W^* \approx 14$ years is surprisingly long, reflecting the fact that drift in expected returns ($\sigma_\delta = 2\%$/year) is slow compared to return volatility ($\sigma = 16\%$/year). The noise overwhelms the drift, so variance reduction (long windows) is more important than bias reduction (short windows). This is another manifestation of the low signal-to-noise ratio in financial data favoring simpler, more stable estimators.

---

**Exercise 7.** Cross-validation for time series must respect temporal ordering to avoid look-ahead bias. (a) Describe the rolling-window cross-validation procedure: at time $t$, train on $[t-W, t]$ and test on $[t+1, t+h]$. Compute the average test error across all valid $t$. (b) Compare this with standard $K$-fold CV, which shuffles the data. Explain why shuffling destroys the temporal dependence structure and leads to optimistic error estimates. (c) A LASSO model for return prediction selects 5 features out of 50 using rolling CV with $W = 120$ months and $h = 1$ month. The in-sample $R^2$ is 8% and the out-of-sample $R^2$ is 1.5%. Is the model useful? Compute the t-statistic for the out-of-sample $R^2$ and discuss statistical significance.

??? success "Solution to Exercise 7"
    **(a)** The **rolling-window cross-validation** procedure works as follows:

    For each valid time index $t$ from $t = W$ to $t = T - h$:

    1. **Training set:** Use observations from time $t - W + 1$ to $t$ (the most recent $W$ observations).
    2. **Fit the model** on the training set to obtain $\hat{f}_{[t-W+1:t]}$.
    3. **Test:** Predict $Y_{t+h}$ using $X_t$ and compute the test error $L(Y_{t+h}, \hat{f}_{[t-W+1:t]}(X_t))$.

    The average test error is:

    $$
    \text{CV}_{\text{rolling}} = \frac{1}{T - W - h + 1} \sum_{t=W}^{T-h} L(Y_{t+h}, \hat{f}_{[t-W+1:t]}(X_t))
    $$

    This procedure respects the temporal ordering: at each evaluation point, only past data is used for training, and the test observation is strictly in the future.

    **(b)** Standard $K$-fold CV randomly partitions data into $K$ folds, trains on $K-1$ folds, and tests on the held-out fold. For time series, this is problematic because:

    1. **Future data leaks into training:** A random partition may place observation $t+5$ in the training set while testing on $t$. The model effectively "sees" future information.

    2. **Autocorrelation inflates apparent performance:** Adjacent observations are correlated. If observation $t$ is in the test set but $t-1$ and $t+1$ are in the training set, the model can achieve low test error simply by interpolating between nearby training points, not by genuine prediction.

    3. **Non-stationarity is ignored:** Standard CV assumes the data distribution is the same across folds. If the market regime shifts over time, training on a mix of past and future regimes and testing on intermediate periods gives unrealistically good performance.

    The result is **optimistic error estimates**: standard CV reports lower error than the model would achieve in real-time deployment.

    **(c)** With in-sample $R^2 = 8\%$ and out-of-sample $R^2 = 1.5\%$, the large gap ($8\% - 1.5\% = 6.5\%$) indicates substantial overfitting, but the out-of-sample $R^2$ is still positive, which is promising.

    To assess statistical significance, we use the test for out-of-sample $R^2$. The t-statistic for testing $R^2_{\text{OOS}} > 0$ can be approximated using the Clark-West or Diebold-Mariano framework. A simple approximation:

    $$
    t = \frac{R^2_{\text{OOS}}}{\text{SE}(R^2_{\text{OOS}})} \approx \frac{R^2_{\text{OOS}} \sqrt{T_{\text{OOS}}}}{\sqrt{2(1 - R^2_{\text{OOS}})^2 / T_{\text{OOS}} + 4R^2_{\text{OOS}}(1-R^2_{\text{OOS}})/T_{\text{OOS}}}}
    $$

    More practically, with $T_{\text{OOS}}$ out-of-sample months (if the total sample is, say, 30 years = 360 months minus 120 training = 240 OOS months):

    $$
    t \approx R^2_{\text{OOS}} \cdot \sqrt{\frac{T_{\text{OOS}}}{2}} \cdot \frac{1}{1 - R^2_{\text{OOS}}} \approx 0.015 \times \sqrt{\frac{240}{2}} \times \frac{1}{0.985} \approx 0.015 \times 10.95 \times 1.015 \approx 0.167
    $$

    This is well below the critical value of 1.65 (one-sided, 5% level), so the out-of-sample $R^2$ is **not statistically significant**.

    However, a more standard test considers the relative MSPE (mean squared prediction error). Campbell and Thompson (2008) suggest that an out-of-sample $R^2$ of 0.5% per month can be economically significant for a mean-variance investor. An $R^2_{\text{OOS}}$ of 1.5% is economically meaningful if genuine, but the statistical test suggests we cannot confidently distinguish it from zero. The model may be useful as part of a diversified signal combination, but should not be relied upon as a standalone predictor. More out-of-sample data or alternative statistical tests (e.g., encompassing tests) would strengthen the evaluation.
