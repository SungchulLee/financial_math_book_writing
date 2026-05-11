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

---

## Exercises

**Exercise 1.** A stock has daily closing prices $S_0 = 100$, $S_1 = 102$, $S_2 = 99$, $S_3 = 101$.

(a) Compute the simple returns and log returns for each day.

(b) Verify that the 3-day log return equals the sum of the daily log returns.

(c) Compute the 3-day momentum feature $\text{Mom}^{(3,1)}$ and explain its interpretation.

??? success "Solution to Exercise 1"
    **(a)** Given prices $S_0 = 100$, $S_1 = 102$, $S_2 = 99$, $S_3 = 101$.

    **Simple returns:**

    $$
    R_1 = \frac{S_1 - S_0}{S_0} = \frac{102 - 100}{100} = 0.02 = 2\%
    $$

    $$
    R_2 = \frac{S_2 - S_1}{S_1} = \frac{99 - 102}{102} = -0.02941 \approx -2.94\%
    $$

    $$
    R_3 = \frac{S_3 - S_2}{S_2} = \frac{101 - 99}{99} = 0.02020 \approx 2.02\%
    $$

    **Log returns:**

    $$
    r_1 = \log\frac{S_1}{S_0} = \log\frac{102}{100} = \log 1.02 \approx 0.01980
    $$

    $$
    r_2 = \log\frac{S_2}{S_1} = \log\frac{99}{102} = \log 0.97059 \approx -0.02985
    $$

    $$
    r_3 = \log\frac{S_3}{S_2} = \log\frac{101}{99} = \log 1.02020 \approx 0.02000
    $$

    **(b)** The 3-day log return is:

    $$
    r^{(3)} = \log\frac{S_3}{S_0} = \log\frac{101}{100} = \log 1.01 \approx 0.00995
    $$

    The sum of daily log returns is:

    $$
    r_1 + r_2 + r_3 = 0.01980 + (-0.02985) + 0.02000 = 0.00995
    $$

    Indeed $r^{(3)} = r_1 + r_2 + r_3$, confirming the additivity property of log returns.

    **(c)** The 3-day momentum feature $\text{Mom}^{(3,1)}$ is defined as:

    $$
    \text{Mom}_3^{(3,1)} = r_3^{(3)} - r_3^{(1)} = \log\frac{S_3}{S_0} - \log\frac{S_3}{S_2}
    $$

    $$
    = \log\frac{S_3}{S_0} - \log\frac{S_3}{S_2} = \log\frac{S_2}{S_0} = \log\frac{99}{100} = \log 0.99 \approx -0.01005
    $$

    **Interpretation:** $\text{Mom}^{(3,1)}$ is the cumulative return over the 3-day period **excluding** the most recent day. It captures the intermediate-term price movement while removing the most recent return. This is motivated by the empirical observation that very recent returns may reflect short-term reversal (microstructure effects, bid-ask bounce), while intermediate-term returns contain momentum information. The negative value of $-1\%$ indicates that over the first two days (excluding the last), the stock experienced a net decline.

---

**Exercise 2.** Given 20 days of daily returns, compute the EWMA volatility $\hat{\sigma}_t^2 = \lambda \hat{\sigma}_{t-1}^2 + (1 - \lambda) r_t^2$ with $\lambda = 0.94$, starting from $\hat{\sigma}_0^2 = \text{Var}(r)$ (sample variance). Compare the EWMA estimate at $t = 20$ with the rolling 20-day standard deviation. Which responds faster to a volatility spike at $t = 15$?

??? success "Solution to Exercise 2"
    The EWMA recursion is $\hat{\sigma}_t^2 = \lambda \hat{\sigma}_{t-1}^2 + (1-\lambda) r_t^2$ with $\lambda = 0.94$.

    **Initialization:** $\hat{\sigma}_0^2 = \text{Var}(r)$ (sample variance of all 20 returns).

    **Key property of EWMA:** Unrolling the recursion:

    $$
    \hat{\sigma}_t^2 = (1-\lambda) \sum_{k=0}^{t-1} \lambda^k r_{t-k}^2 + \lambda^t \hat{\sigma}_0^2
    $$

    The weight on observation $r_{t-k}^2$ is $(1-\lambda)\lambda^k = 0.06 \times 0.94^k$. Recent observations receive exponentially more weight.

    **Response to a volatility spike at $t = 15$:** Suppose returns are approximately $r_t \approx 0.01$ for $t \neq 15$, and $r_{15} = 0.05$ (a large spike).

    At $t = 15$, the EWMA immediately incorporates the spike:

    $$
    \hat{\sigma}_{15}^2 = 0.94 \hat{\sigma}_{14}^2 + 0.06 \times (0.05)^2 = 0.94 \hat{\sigma}_{14}^2 + 0.00015
    $$

    If $\hat{\sigma}_{14}^2 \approx 0.0001$ (corresponding to $\sigma \approx 1\%$):

    $$
    \hat{\sigma}_{15}^2 \approx 0.94 \times 0.0001 + 0.00015 = 0.000094 + 0.00015 = 0.000244
    $$

    So $\hat{\sigma}_{15} \approx 1.56\%$, a sharp jump from $1\%$.

    At $t = 20$ (5 days after the spike):

    $$
    \hat{\sigma}_{20}^2 \approx 0.94^5 \times 0.000244 + (1 - 0.94^5) \times 0.0001 \approx 0.735 \times 0.000244 + 0.265 \times 0.0001
    $$

    $$
    \approx 0.000179 + 0.0000265 \approx 0.000206
    $$

    So $\hat{\sigma}_{20} \approx 1.43\%$---still elevated.

    **Rolling 20-day standard deviation at $t = 20$:** This uses all 20 returns equally. With one outlier of 0.05 and 19 returns of 0.01:

    $$
    \hat{\sigma}_{\text{roll}} = \sqrt{\frac{1}{19}\left[19 \times (0.01 - \bar{r})^2 + (0.05 - \bar{r})^2\right]}
    $$

    where $\bar{r} = (19 \times 0.01 + 0.05)/20 = 0.012$. This gives equal weight to the spike regardless of when it occurred.

    **Comparison:** The EWMA responds **faster** to the volatility spike because it places $6\%$ weight on the most recent observation, versus $5\%$ ($= 1/20$) for the rolling window. More importantly, EWMA places decaying weights: the spike at $t = 15$ receives weight $0.06 \times 0.94^5 \approx 4.4\%$ at $t = 20$, while the rolling window still gives it a full $5\%$. If the spike occurred at $t = 1$ instead of $t = 15$, EWMA would give it weight $0.06 \times 0.94^{19} \approx 1.9\%$, while the rolling window would still give $5\%$. EWMA forgets old information exponentially, making it more adaptive to changing volatility regimes.

---

**Exercise 3.** Explain why each of the following constitutes look-ahead bias:

(a) Standardizing features using the full-sample mean and variance.

(b) Using revised GDP figures instead of first-release data.

(c) Computing momentum only for stocks that survive to the end of the sample.

For each case, describe how to construct the feature correctly.

??? success "Solution to Exercise 3"
    **(a) Full-sample standardization:** Standardizing feature $X_t$ using the mean and variance computed over the entire sample $\{X_1, \ldots, X_T\}$ constitutes look-ahead bias because:

    - At time $t$, the feature value $\tilde{X}_t = (X_t - \bar{X}) / \hat{\sigma}_X$ uses $\bar{X}$ and $\hat{\sigma}_X$ that include future observations $X_{t+1}, \ldots, X_T$.
    - If volatility increases in the latter part of the sample, the full-sample standard deviation is larger than the information available at time $t$, artificially compressing early features.
    - **Correct approach:** Use an **expanding-window** or **rolling-window** standardization: $\tilde{X}_t = (X_t - \bar{X}_{1:t}) / \hat{\sigma}_{1:t}$, computed only from data up to time $t$.

    **(b) Revised GDP figures:** GDP is initially released with preliminary estimates, then revised multiple times over subsequent months and years. Using the final revised figure at time $t$ constitutes look-ahead bias because:

    - At time $t$ (when GDP is first released), only the preliminary estimate is available.
    - The revised figure incorporates additional data that only becomes available later.
    - A model trained on revised data may appear to predict well in-sample, but in real time, it would only have access to the preliminary (noisier) data.
    - **Correct approach:** Use **vintage (real-time) data** that records what was actually known at each point in time. The Federal Reserve Bank of Philadelphia's Real-Time Data Research Center maintains such archives.

    **(c) Survivorship-biased momentum:** Computing momentum only for stocks that exist at the end of the sample creates look-ahead bias because:

    - Stocks that went bankrupt or were delisted are excluded, but at time $t$ we do not know which stocks will survive.
    - Stocks that decline severely and are delisted would have had strongly negative momentum---excluding them biases the average momentum signal upward.
    - This makes momentum appear more profitable than it would be in a real-time portfolio.
    - **Correct approach:** Use the **point-in-time universe**: at each time $t$, include all stocks that were actively trading at time $t$, regardless of what happens to them later. Delisted stocks should be included with their delisting returns up to the point of delisting.

---

**Exercise 4.** Consider the Parkinson volatility estimator $\hat{\sigma}^{\text{Park}} = |\log H - \log L| / \sqrt{4 \log 2}$.

(a) Show that $\mathbb{E}[(\log H - \log L)^2] = 4 \log 2 \cdot \sigma^2$ for geometric Brownian motion (hint: the range of a Brownian bridge).

(b) Explain why this estimator is more efficient than the close-to-close estimator $|r_t|$.

??? success "Solution to Exercise 4"
    **(a)** Under geometric Brownian motion $dS = \mu S \, dt + \sigma S \, dW$, the log price $\log S_t$ follows a Brownian motion (with drift). Over a single period $[0, 1]$, $\log S_t - \log S_0 = (\mu - \sigma^2/2)t + \sigma W_t$. The range of the log price process is determined by the range of the Brownian motion component.

    For a standard Brownian motion $W_t$ on $[0, 1]$:

    $$
    H - L = \max_{0 \leq t \leq 1} W_t - \min_{0 \leq t \leq 1} W_t
    $$

    The key result (from the theory of Brownian motion range, related to the Brownian bridge) is:

    $$
    \mathbb{E}[(\max W_t - \min W_t)^2] = 4 \log 2
    $$

    This can be derived using the reflection principle and the known distribution of the range. Specifically, the density of the range $R = \max W - \min W$ of a standard Brownian bridge on $[0,1]$ is known, and:

    $$
    \mathbb{E}[R^2] = \sum_{k=1}^{\infty} \frac{8}{k^2 \pi^2} = \frac{8}{\pi^2} \cdot \frac{\pi^2}{6} = \frac{4}{3}
    $$

    However, for the unconditional Brownian motion (not bridge), the result involves the full range and gives $\mathbb{E}[(\log H - \log L)^2] = 4\log 2 \cdot \sigma^2$. This comes from the identity:

    $$
    \mathbb{E}\left[\left(\max_{0 \leq t \leq 1} \sigma W_t - \min_{0 \leq t \leq 1} \sigma W_t\right)^2\right] = 4\sigma^2 \log 2
    $$

    Therefore:

    $$
    \hat{\sigma}^{\text{Park}} = \frac{|\log H - \log L|}{\sqrt{4\log 2}}
    $$

    satisfies $\mathbb{E}[(\hat{\sigma}^{\text{Park}})^2] = \frac{\mathbb{E}[(\log H - \log L)^2]}{4\log 2} = \frac{4\log 2 \cdot \sigma^2}{4\log 2} = \sigma^2$, so it is an unbiased estimator of $\sigma^2$.

    **(b)** The Parkinson estimator is more efficient than the close-to-close estimator because:

    1. **Information content:** The close-to-close estimator $|r_t| = |\log C_t - \log O_t|$ uses only two price observations (open and close). The Parkinson estimator uses the high and low, which summarize the entire intraday price path.

    2. **Efficiency ratio:** The variance of the Parkinson estimator relative to the close-to-close estimator can be computed. For one period, the close-to-close estimator is $(r_t)^2 = \sigma^2 Z^2$ where $Z \sim N(0,1)$, so $\text{Var}[(r_t)^2] = 2\sigma^4$ (since $\text{Var}[Z^2] = 2$). The Parkinson estimator has variance approximately $\sigma^4 / (4\log 2)^2 \times \text{Var}[R^2]$, which works out to be approximately $\sigma^4 \times 0.37$, compared to $2\sigma^4$ for close-to-close.

    3. The **efficiency gain** is approximately a factor of 5: the Parkinson estimator has roughly 5 times lower variance than the close-to-close estimator. Intuitively, the high and low prices capture the full excursion of the intraday process, providing much more information about volatility than just the endpoint. This is especially valuable when intraday data is not available but HLOC data is.

---

**Exercise 5.** For a cross-section of $N = 500$ stocks, you observe a raw feature $X_{i,t}$ (e.g., market capitalization). Describe the difference between:

(a) Cross-sectional rank: $\text{Rank}_{i,t} / N$

(b) Cross-sectional z-score: $(X_{i,t} - \bar{X}_t) / \hat{\sigma}_t^X$

(c) Industry-adjusted feature: $X_{i,t} - \bar{X}_{g(i),t}$

Under what conditions would you prefer rank over z-score? When is industry adjustment necessary?

??? success "Solution to Exercise 5"
    **(a) Cross-sectional rank: $\text{Rank}_{i,t}/N$.**

    This maps each stock's feature value to $[0, 1]$ based on its rank among all $N = 500$ stocks. Properties:

    - Produces a **uniform distribution** over $\{1/N, 2/N, \ldots, 1\}$ by construction
    - **Robust to outliers**: a stock with market cap 100 times the median gets the same rank score as one with 2 times the median (if both are the largest)
    - **Nonlinear transformation**: destroys information about the magnitude of differences between stocks
    - **Robust to non-stationarity**: if all market caps double over time, ranks are unchanged

    **(b) Cross-sectional z-score: $(X_{i,t} - \bar{X}_t)/\hat{\sigma}_t^X$.**

    This standardizes to zero mean and unit variance in the cross-section. Properties:

    - Preserves **relative magnitudes**: a stock twice as far from the mean as another gets twice the z-score
    - **Sensitive to outliers**: a single mega-cap stock can dominate $\bar{X}_t$ and $\hat{\sigma}_t^X$, distorting all other z-scores
    - Distribution depends on the underlying cross-sectional distribution (often right-skewed for features like market cap)
    - Produces approximately standard normal values if the cross-section is approximately Gaussian

    **(c) Industry-adjusted feature: $X_{i,t} - \bar{X}_{g(i),t}$.**

    This removes the industry-level mean. Properties:

    - Captures **within-industry** variation, removing common industry effects
    - A bank with average-for-banking market cap gets a value near zero, even if banking is large overall
    - Does not standardize for scale across industries

    **When to prefer rank over z-score:** Use rank when:

    - The feature has **heavy tails or extreme outliers** (e.g., market cap, trading volume) that would distort z-scores
    - The cross-sectional distribution is **highly skewed** or changes shape over time
    - You want features that are **comparable across different characteristic types** (all mapped to $[0,1]$)

    **When is industry adjustment necessary:** Use industry adjustment when:

    - The feature has strong **industry-level variation** that is not predictive of returns (e.g., book-to-market ratios vary systematically by industry due to accounting conventions, not due to mispricing)
    - You want to isolate **stock-specific signals** within industries
    - The target variable (returns) is also industry-adjusted or the strategy is industry-neutral

---

**Exercise 6.** The fractional differencing operator of order $d$ is $(1 - B)^d X_t = \sum_{k=0}^{\infty} \binom{d}{k} (-1)^k X_{t-k}$. Compute the first four weights $w_k = \binom{d}{k}(-1)^k$ for $d = 0.4$. Explain why $d \in (0, 0.5)$ produces a stationary series while preserving more memory than full differencing ($d = 1$).

??? success "Solution to Exercise 6"
    The fractional differencing operator weights are $w_k = \binom{d}{k}(-1)^k$. The generalized binomial coefficient is:

    $$
    \binom{d}{k} = \frac{d(d-1)(d-2)\cdots(d-k+1)}{k!}
    $$

    For $d = 0.4$:

    **$k = 0$:**

    $$
    w_0 = \binom{0.4}{0}(-1)^0 = 1 \times 1 = 1
    $$

    **$k = 1$:**

    $$
    w_1 = \binom{0.4}{1}(-1)^1 = 0.4 \times (-1) = -0.4
    $$

    **$k = 2$:**

    $$
    w_2 = \binom{0.4}{2}(-1)^2 = \frac{0.4 \times (0.4-1)}{2!} \times 1 = \frac{0.4 \times (-0.6)}{2} = \frac{-0.24}{2} = -0.12
    $$

    **$k = 3$:**

    $$
    w_3 = \binom{0.4}{3}(-1)^3 = \frac{0.4 \times (-0.6) \times (-1.6)}{3!} \times (-1) = \frac{0.384}{6} \times (-1) = -0.064
    $$

    Summary of weights:

    | $k$ | $w_k$ |
    |-----|-------|
    | 0 | $1$ |
    | 1 | $-0.4$ |
    | 2 | $-0.12$ |
    | 3 | $-0.064$ |

    The fractionally differenced series is:

    $$
    (1-B)^{0.4} X_t = X_t - 0.4 X_{t-1} - 0.12 X_{t-2} - 0.064 X_{t-3} - \cdots
    $$

    **Why $d \in (0, 0.5)$ produces stationarity while preserving memory:**

    1. **Stationarity:** A time series is stationary (in the fractional integration framework) if $d < 0.5$. A unit root process ($d = 1$) is non-stationary. Fractional differencing with $d \in (0, 0.5)$ removes just enough of the non-stationary component to achieve stationarity, while $d = 1$ (full differencing) removes more than necessary.

    2. **Memory preservation:** The weights $w_k$ decay as $k^{-(d+1)}$ for large $k$:

        - For $d = 1$: weights are $(1, -1, 0, 0, \ldots)$---only the most recent observation matters, all memory is destroyed.
        - For $d = 0.4$: weights decay slowly as $k^{-1.4}$, so observations from the distant past still receive non-negligible weight. The series retains **long memory**.

    3. **Information content:** Full differencing ($d = 1$) maps $X_t \to X_t - X_{t-1} = \Delta X_t$, which discards all information about the price level. For financial applications where the level contains information (e.g., deviation from a long-run mean), this destroys valuable signal. Fractional differencing with $d = 0.4$ retains a weighted average of all past levels, preserving long-range dependence and level information while ensuring stationarity.

    4. **Quantitative comparison:** The autocorrelation function of a fractionally differenced series with parameter $d$ decays as $\rho(k) \sim k^{2d-1}$. For $d = 0.4$, $\rho(k) \sim k^{-0.2}$, which decays very slowly (long memory). For $d = 1$, the differenced series may have no memory at all if the original series is a random walk. The fractional approach achieves the minimum information loss needed for stationarity.
