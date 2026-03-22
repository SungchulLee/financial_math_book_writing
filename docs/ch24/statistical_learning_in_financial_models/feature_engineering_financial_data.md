# Feature Engineering for Financial Data

Feature engineering transforms raw market observables into informative predictors for learning algorithms. In finance, where signal-to-noise ratios are extremely low ($R^2 \approx 0.25\%$ for daily return prediction), the choice and construction of features is often more important than the choice of learning algorithm. This section develops a systematic framework for constructing return, volatility, microstructure, and cross-sectional features, with careful attention to stationarity, look-ahead bias, and the unique challenges of financial data.

---

## Principles of Financial Feature Engineering

### Stationarity Requirement

Most learning algorithms assume that the joint distribution of features and targets is stationary (or at least locally stationary). Raw financial prices $S_t$ are non-stationary---they exhibit trends, mean-reversion in some regimes, and unit-root behavior. Features must be transformed to achieve (approximate) stationarity.

**Definition (Stationarity Transformation).** A transformation $\phi : \{S_t\} \to \{X_t\}$ is a stationarity transformation if the resulting series $\{X_t\}$ is (weakly) stationary:

$$
\mathbb{E}[X_t] = \mu, \quad \text{Cov}(X_t, X_{t+h}) = \gamma(h) \quad \text{(independent of } t\text{)}
$$

Common transformations:

- **Log returns:** $r_t = \log(S_t / S_{t-1})$ --- removes price level non-stationarity
- **Fractional differencing:** $d$-th order differencing with $d \in (0, 1)$ that preserves memory while achieving stationarity
- **Normalization:** $\tilde{X}_t = (X_t - \hat{\mu}_t) / \hat{\sigma}_t$ using rolling estimates

### Look-Ahead Bias

**Definition (Look-Ahead Bias).** A feature $X_t$ exhibits look-ahead bias if its computation at time $t$ uses information from times $s > t$.

This is the most common and most dangerous error in financial ML. All features must be **point-in-time**: computable using only information available at the time of the prediction.

!!! danger "Common Sources of Look-Ahead Bias"
    - Using future data in normalization (e.g., standardizing by full-sample mean/variance)
    - Filling missing values with future observations
    - Using revised economic data rather than first-release data
    - Survivorship bias in cross-sectional features (only including firms that survive to the end)

---

## Return Features

### Simple and Log Returns

**Definition.** The simple return and log return over horizon $h$ are:

$$
R_t^{(h)} = \frac{S_t - S_{t-h}}{S_{t-h}}, \quad r_t^{(h)} = \log\frac{S_t}{S_{t-h}}
$$

For small returns, $r_t^{(h)} \approx R_t^{(h)}$. Log returns are additive over time: $r_t^{(h)} = \sum_{k=0}^{h-1} r_{t-k}^{(1)}$.

### Multi-Horizon Return Features

Return signals are often horizon-dependent. Construct features at multiple horizons:

$$
\mathbf{r}_t = \left(r_t^{(1)}, \; r_t^{(5)}, \; r_t^{(21)}, \; r_t^{(63)}, \; r_t^{(252)}\right)
$$

corresponding to daily, weekly, monthly, quarterly, and annual returns.

### Momentum and Reversal Features

**Momentum:** Cumulative return over a lookback window, excluding the most recent period:

$$
\text{Mom}_{t}^{(L,S)} = r_t^{(L)} - r_t^{(S)} = \log\frac{S_t}{S_{t-L}} - \log\frac{S_t}{S_{t-S}}
$$

Typical choices: $L = 252, S = 21$ (12-month momentum, skipping the most recent month).

**Reversal:** Short-horizon return, often negatively predictive:

$$
\text{Rev}_t^{(h)} = -r_t^{(h)}
$$

for $h = 1$ (daily) or $h = 5$ (weekly).

### Excess Returns

Features defined relative to a benchmark:

$$
r_t^{\text{excess}} = r_t - r_t^{\text{benchmark}}
$$

where the benchmark may be the market return, a sector return, or the risk-free rate.

---

## Volatility Features

### Realized Volatility

**Definition.** The realized volatility over window $[t-L, t]$ using $n$ intraday returns is:

$$
\text{RV}_t^{(L)} = \sqrt{\sum_{i=1}^{n} r_{t_i}^2}
$$

For daily data with $n = 1$ return per day:

$$
\hat{\sigma}_t^{(L)} = \sqrt{\frac{1}{L-1}\sum_{k=0}^{L-1}(r_{t-k} - \bar{r})^2}
$$

### EWMA Volatility

The exponentially weighted moving average provides a more responsive estimate:

$$
\hat{\sigma}_t^2 = \lambda \hat{\sigma}_{t-1}^2 + (1 - \lambda) r_t^2
$$

with $\lambda \approx 0.94$ (RiskMetrics daily). This requires no window length selection and adapts to volatility clustering.

### Volatility Ratio Features

**Definition.** The volatility ratio captures changes in volatility regime:

$$
\text{VolRatio}_t^{(S,L)} = \frac{\hat{\sigma}_t^{(S)}}{\hat{\sigma}_t^{(L)}}
$$

where $S < L$ (e.g., $S = 5, L = 63$). Values $> 1$ indicate increasing volatility; values $< 1$ indicate decreasing volatility.

### Parkinson and Garman-Klass Estimators

Using high-low-open-close (HLOC) data for more efficient volatility estimation:

**Parkinson:**

$$
\hat{\sigma}_t^{\text{Park}} = \frac{1}{\sqrt{4\log 2}} \cdot |\log H_t - \log L_t|
$$

**Garman-Klass:**

$$
\hat{\sigma}_t^{\text{GK}} = \sqrt{\frac{1}{2}(\log H_t - \log L_t)^2 - (2\log 2 - 1)(\log C_t - \log O_t)^2}
$$

where $H_t, L_t, O_t, C_t$ are the high, low, open, and close prices. These are 5--8 times more efficient than the close-to-close estimator.

---

## Microstructure Features

### Bid-Ask Spread

The spread captures liquidity and information asymmetry:

$$
\text{Spread}_t = \frac{A_t - B_t}{M_t}
$$

where $A_t, B_t, M_t$ are ask, bid, and mid prices. Wider spreads indicate lower liquidity or higher information asymmetry.

### Order Book Imbalance

**Definition.** The order book imbalance at level $k$ is:

$$
\text{OBI}_t^{(k)} = \frac{\sum_{i=1}^k V_t^{B,i} - \sum_{i=1}^k V_t^{A,i}}{\sum_{i=1}^k V_t^{B,i} + \sum_{i=1}^k V_t^{A,i}}
$$

where $V_t^{B,i}$ and $V_t^{A,i}$ are bid and ask volumes at the $i$-th level. Positive imbalance (more buying pressure) predicts short-term price increases.

### Kyle Lambda (Price Impact)

The Kyle lambda measures the price sensitivity to order flow:

$$
\Delta S_t = \alpha + \lambda_{\text{Kyle}} \cdot \text{OFI}_t + \varepsilon_t
$$

where $\text{OFI}_t$ is the signed order flow imbalance. Higher $\lambda_{\text{Kyle}}$ indicates less liquid markets.

### Volume Features

**Relative volume:**

$$
\text{RelVol}_t = \frac{V_t}{\bar{V}_t^{(L)}}
$$

where $\bar{V}_t^{(L)} = \frac{1}{L}\sum_{k=1}^L V_{t-k}$. High relative volume may signal informed trading or regime changes.

**Volume-weighted return:**

$$
r_t^{\text{VW}} = r_t \cdot \frac{V_t}{\bar{V}_t^{(L)}}
$$

---

## Cross-Sectional Features

### Rank Transformation

**Definition.** The cross-sectional rank at time $t$ for asset $i$ among $N$ assets:

$$
\text{Rank}_{i,t} = \frac{\text{rank of } X_{i,t} \text{ among } \{X_{1,t}, \ldots, X_{N,t}\}}{N}
$$

Rank transformation produces uniform marginals, reduces the impact of outliers, and makes features comparable across different characteristic types.

**Proposition.** Cross-sectional rank features are robust to non-stationarity in the cross-sectional distribution. If the distribution of $X_{i,t}$ shifts over time but the ordering is preserved, the rank features remain stable.

### Standardized Cross-Sectional Features

$$
\tilde{X}_{i,t} = \frac{X_{i,t} - \bar{X}_t}{\hat{\sigma}_t^X}
$$

where $\bar{X}_t = \frac{1}{N}\sum_i X_{i,t}$ and $\hat{\sigma}_t^X$ are the cross-sectional mean and standard deviation.

### Industry-Adjusted Features

$$
X_{i,t}^{\text{adj}} = X_{i,t} - \bar{X}_{g(i),t}
$$

where $g(i)$ denotes the industry group of asset $i$ and $\bar{X}_{g(i),t}$ is the industry average. This removes common industry effects, isolating idiosyncratic signals.

---

## Feature Selection and Dimensionality Reduction

### Mutual Information

**Definition.** The mutual information between feature $X$ and target $Y$ is:

$$
I(X; Y) = \int \int p(x,y) \log\frac{p(x,y)}{p(x)p(y)} \, dx \, dy
$$

Unlike correlation, mutual information captures nonlinear dependencies. Features with high $I(X; Y)$ are informative regardless of the functional form of the relationship.

### PCA-Based Feature Construction

Principal component analysis of the feature matrix $\mathbf{X} \in \mathbb{R}^{n \times p}$:

$$
\mathbf{X} = \mathbf{U} \mathbf{\Lambda} \mathbf{V}^\top
$$

The first $k$ principal components $\mathbf{Z} = \mathbf{X}\mathbf{V}_k$ explain the most variance while reducing dimensionality from $p$ to $k$.

**Financial application:** Statistical factor models use the first $k$ PCs of the return matrix as latent factors:

$$
r_{i,t} = \alpha_i + \sum_{j=1}^k \beta_{ij} F_{j,t} + \varepsilon_{i,t}
$$

### LASSO Feature Selection

The LASSO penalty induces sparsity, selecting relevant features:

$$
\hat{\beta} = \arg\min_\beta \left\{\sum_t (r_{t+1} - X_t^\top \beta)^2 + \lambda \|\beta\|_1\right\}
$$

Features with $\hat{\beta}_j \neq 0$ are selected as predictive. The adaptive LASSO with feature-specific penalties $\lambda_j = \lambda / |\tilde{\beta}_j|^\gamma$ achieves oracle properties (correct selection asymptotically).

---

## Time-Series Feature Construction

### Rolling Statistics

**Definition.** A rolling statistic of order $(f, L)$ is:

$$
F_t^{(f,L)} = f(X_{t-L+1}, X_{t-L+2}, \ldots, X_t)
$$

where $f$ is a summary function and $L$ is the window length. Common choices:

- Rolling mean: $f = \text{mean}$ --- trend indicator
- Rolling skewness: $f = \text{skew}$ --- asymmetry in recent returns
- Rolling kurtosis: $f = \text{kurt}$ --- tail heaviness
- Rolling autocorrelation: $f = \text{acf}(\cdot, 1)$ --- persistence

### Fractional Differencing

**Definition (Fractionally Differenced Series -- Lopez de Prado 2018).** The fractional differencing operator of order $d$ is:

$$
(1 - B)^d X_t = \sum_{k=0}^{\infty} \binom{d}{k}(-1)^k X_{t-k}
$$

where $B$ is the backshift operator. For $d \in (0, 0.5)$, the series is stationary while retaining long memory.

The optimal $d$ is the smallest value that achieves stationarity (e.g., passing an augmented Dickey-Fuller test at the 5% level). This preserves more information than full differencing ($d = 1$).

---

## Key Takeaways

1. **Stationarity** and **point-in-time correctness** are non-negotiable requirements for financial features---violations lead to spurious predictive performance.

2. **Return features** at multiple horizons capture momentum, reversal, and mean-reversion effects at different time scales.

3. **Volatility features** (realized, EWMA, range-based) are among the most predictive signals in finance due to volatility clustering.

4. **Microstructure features** (spread, imbalance, volume) capture short-term dynamics and liquidity conditions.

5. **Cross-sectional transformations** (rank, standardization, industry adjustment) improve robustness and comparability across assets.

6. **Dimensionality reduction** via PCA and sparse selection (LASSO) prevents overfitting in the high-dimensional, low-signal financial environment.

---

## Further Reading

- Gu, Kelly & Xiu (2020), "Empirical Asset Pricing via Machine Learning"
- Lopez de Prado (2018), *Advances in Financial Machine Learning*, Chapters 3--5
- Cartea, Jaimungal & Penalva (2015), *Algorithmic and High-Frequency Trading*
- Hastie, Tibshirani & Friedman (2009), *ESL*, Chapters 3 and 18
- Harvey, Liu & Zhu (2016), "... and the Cross-Section of Expected Returns"
