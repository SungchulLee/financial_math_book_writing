# Stock Data and Return Computation


The quantitative rigor of any financial modeling exercise is predicated upon the fidelity and precision of its underlying data inputs. Before constructing theoretical frameworks involving stochastic differential equations, we must first establish a robust empirical foundation through proper data retrieval, preprocessing, and statistical characterization. This section provides a technically detailed exposition of the procedures required for extracting and transforming asset price data—procedures that establish the empirical substrate on which theoretical constructs are operationalized in practice.

---

## Historical Data Retrieval


### 1. Data Sources and Quality


A robust empirical foundation begins with the acquisition of high-resolution and appropriately adjusted time series data. In contemporary computational finance workflows, historical financial data are commonly retrieved through automated APIs. 

**Primary data sources:**
- **Exchange feeds:** Direct market data (most reliable, often proprietary)
- **Bloomberg/Reuters:** Professional-grade data with corporate action adjustments
- **Yahoo Finance:** Freely accessible via `yfinance` library
- **CRSP/Compustat:** Academic research databases with survivorship-bias corrections

### 2. The Adjusted Close Price


Of particular relevance is the **adjusted closing price**, a field that retroactively corrects for events such as:

- **Dividends:** Cash distributions to shareholders
- **Stock splits:** Changes in number of shares outstanding
- **Rights offerings:** Subscription rights for new shares
- **Spin-offs:** Corporate restructurings

**Why adjustment matters:**

Without proper adjustment, a 2-for-1 stock split would appear as a 50% price drop overnight, creating a spurious return observation. The adjusted price retroactively scales historical prices to ensure **return continuity**.

**Mathematical adjustment:**

For a dividend $D$ paid at time $t$:

$$
P_{\text{adj}}^{\text{pre-div}} = P_{\text{unadj}}^{\text{pre-div}} \times \frac{P_{\text{adj}}^{\text{post-div}}}{P_{\text{unadj}}^{\text{post-div}} + D}
$$

This ensures that returns computed from adjusted prices are economically meaningful.

### 3. Data Retrieval Implementation


```python
import yfinance as yf
import pandas as pd
import numpy as np

class USStock:
    """
    Stock data retrieval and preprocessing.
    """
    def __init__(self, ticker):
        self.ticker = ticker
        self.df = None
        
    def get_data(self, start_date, end_date):
        """
        Retrieve adjusted OHLCV data from Yahoo Finance.
        
        Parameters:
        -----------
        start_date : str
            Start date in 'YYYY-MM-DD' format
        end_date : str
            End date in 'YYYY-MM-DD' format
        """
        stock = yf.Ticker(self.ticker)
        self.df = stock.history(start=start_date, end=end_date)
        
        # Keep only adjusted close for return calculations
        self.df = self.df[['Close']].copy()
        
        print(f"Retrieved {len(self.df)} daily observations for {self.ticker}")
        print(f"Date range: {self.df.index[0]} to {self.df.index[-1]}")
        
        return self.df
```

**Example usage:**

```python
# Retrieve Apple stock data for 2023
apple = USStock("AAPL")
df = apple.get_data(start_date="2023-01-01", end_date="2023-12-31")
```

### 4. Data Quality Checks


Before proceeding, verify:

1. **No missing dates** (accounting for weekends/holidays)
2. **No zero or negative prices**
3. **No extreme outliers** (investigate >20% daily moves)
4. **Proper chronological ordering**

```python
def data_quality_check(df):
    """Perform basic data quality checks."""
    # Check for missing values
    if df['Close'].isna().any():
        print(f"Warning: {df['Close'].isna().sum()} missing values")
    
    # Check for non-positive prices
    if (df['Close'] <= 0).any():
        print("Warning: Non-positive prices detected")
    
    # Check for extreme moves (potential data errors)
    returns = df['Close'].pct_change()
    extreme = returns[abs(returns) > 0.20]
    if len(extreme) > 0:
        print(f"Warning: {len(extreme)} extreme daily moves (>20%)")
        print(extreme)
    
    # Check monotonic time index
    if not df.index.is_monotonic_increasing:
        print("Warning: Non-monotonic time index")
```

---

## Return Metrics: Discrete and Continuous Formulations


Transforming raw price data into return series is a critical intermediate step that recasts the time series from levels to increments. Two principal forms of returns are widely utilized, each with distinct mathematical properties and applications.

### 1. Discrete (Arithmetic) Return


**Definition:**

$$
r_t^{(D)} = \frac{S_t - S_{t-1}}{S_{t-1}} = \frac{S_t}{S_{t-1}} - 1
$$

**Properties:**

- **Interpretation:** Proportional change in price over one period
- **Portfolio aggregation:** Returns of portfolio components are linearly additive:
  $$
  r_P = \sum_{i=1}^n w_i r_i
  $$
- **Time aggregation:** NOT time-additive across multiple periods
- **Common usage:** Performance reporting, portfolio attribution, backtesting

**Multi-period discrete return:**

$$
1 + r_{[t, t+n]} = \prod_{i=1}^n (1 + r_{t+i})
$$

### 2. Continuous (Logarithmic) Return


**Definition:**

$$
r_t^{(C)} = \log\left(\frac{S_t}{S_{t-1}}\right) = \log S_t - \log S_{t-1}
$$

**Properties:**

- **Time additivity:** Log returns are additive across time:
  $$
  r_{[t, t+n]}^{(C)} = \sum_{i=1}^n r_{t+i}^{(C)}
  $$
- **Symmetry:** $r^{(C)}(S_1 \to S_2) = -r^{(C)}(S_2 \to S_1)$
- **Continuous compounding:** Natural for continuous-time models
- **Statistical properties:** Often closer to normality than discrete returns
- **Theory:** Essential for geometric Brownian motion and Itô calculus

**Connection to discrete returns:**

For small returns, the Taylor expansion gives:

$$
r^{(C)} = \log(1 + r^{(D)}) \approx r^{(D)} - \frac{(r^{(D)})^2}{2} + \frac{(r^{(D)})^3}{3} - \cdots
$$

For $|r^{(D)}| < 0.10$, the approximation $r^{(C)} \approx r^{(D)}$ is accurate to within 0.5%.

### 3. Implementation


```python
def compute_returns(df):
    """
    Compute both discrete and continuous returns.
    
    Parameters:
    -----------
    df : DataFrame
        DataFrame with 'Close' column
        
    Returns:
    --------
    DataFrame with return columns added
    """
    # Discrete returns
    df['Return'] = df['Close'].pct_change()
    
    # Continuous (log) returns
    df['Return_Log'] = np.log(df['Close'] / df['Close'].shift(1))
    
    # Remove first row (NaN due to differencing)
    df.dropna(inplace=True)
    
    print(f"Computed returns for {len(df)} observations")
    print(f"Mean discrete return: {df['Return'].mean():.6f}")
    print(f"Mean log return: {df['Return_Log'].mean():.6f}")
    
    return df
```

### 4. Which Return Measure to Use?


| Context | Preferred Return |
|---------|------------------|
| **Theoretical modeling** | Logarithmic (continuous-time SDEs) |
| **Portfolio allocation** | Discrete (linear aggregation) |
| **Statistical estimation** | Logarithmic (better distributional properties) |
| **Performance reporting** | Discrete (intuitive interpretation) |
| **Option pricing** | Logarithmic (log-normal assumption) |
| **Risk management** | Both (VaR uses discrete, theoretical models use log) |

**Throughout this book:** We primarily use **logarithmic returns** when developing theory (SDEs, option pricing) and switch to discrete returns when discussing portfolio applications.

---

## Statistical Characterization: Moment Estimation


With return series in hand, we proceed to estimate their empirical moments—quantities that underpin subsequent modeling and optimization procedures.

### 1. Sample Moments


**First moment (sample mean):**

$$
\hat{\mu} = \frac{1}{T} \sum_{t=1}^{T} r_t
$$

This estimates the expected return $\mathbb{E}[r_t]$ under the assumption of stationarity.

**Second central moment (sample variance):**

$$
\hat{\sigma}^2 = \frac{1}{T - 1} \sum_{t=1}^{T} (r_t - \hat{\mu})^2
$$

The $(T-1)$ denominator provides an unbiased estimator (Bessel's correction).

**Sample standard deviation (volatility):**

$$
\hat{\sigma} = \sqrt{\hat{\sigma}^2}
$$

**Higher moments:**

- **Skewness:** $\hat{\gamma}_1 = \frac{1}{T}\sum_{t=1}^T \left(\frac{r_t - \hat{\mu}}{\hat{\sigma}}\right)^3$
- **Excess kurtosis:** $\hat{\gamma}_2 = \frac{1}{T}\sum_{t=1}^T \left(\frac{r_t - \hat{\mu}}{\hat{\sigma}}\right)^4 - 3$

### 2. Assumptions and Limitations


These estimators assume:

1. **Weak stationarity:** $\mathbb{E}[r_t]$ and $\text{Var}(r_t)$ constant over time
2. **Ergodicity:** Time averages converge to ensemble averages
3. **Finite moments:** $\mathbb{E}[r_t^2] < \infty$

**Violations in practice:**

- **Regime changes:** Market crashes, policy shifts
- **Structural breaks:** Regulatory changes, technological disruption
- **Time-varying volatility:** GARCH effects, volatility clustering
- **Fat tails:** Extreme events more common than Gaussian predicts

Despite these violations, sample moments serve as the default estimators in classical theory.

### 3. Implementation


```python
def compute_statistics(df, return_col='Return_Log'):
    """
    Compute sample statistics for return series.
    
    Parameters:
    -----------
    df : DataFrame
        DataFrame with return column
    return_col : str
        Name of return column to analyze
        
    Returns:
    --------
    dict : Dictionary of statistics
    """
    returns = df[return_col].dropna()
    
    stats = {
        'mean': returns.mean(),
        'std': returns.std(),
        'var': returns.var(),
        'skew': returns.skew(),
        'kurt': returns.kurtosis(),  # Excess kurtosis
        'min': returns.min(),
        'max': returns.max(),
        'count': len(returns)
    }
    
    return stats
```

---

## Annualization


To enable alignment with decision-making horizons, daily estimates are converted to annualized quantities under the i.i.d. assumption.

### 1. Time Scaling Under Independence


**Assumption:** Returns are i.i.d. across time.

**Consequence:** Variances add, means scale linearly.

For $n$ independent periods:

$$
\mathbb{E}[r_{[1,n]}] = n \cdot \mathbb{E}[r_1], \quad \text{Var}(r_{[1,n]}) = n \cdot \text{Var}(r_1)
$$

Therefore:

$$
\sigma_{[1,n]} = \sqrt{n} \cdot \sigma_1
$$

This is the famous **square-root-of-time rule**.

### 2. Annualization Formulas


**Trading days per year:** $N = 252$ (U.S. equity markets)

**Annualized mean return:**

$$
\mu_{\text{ann}} = \mu_{\text{daily}} \times N = \mu_{\text{daily}} \times 252
$$

**Annualized volatility:**

$$
\sigma_{\text{ann}} = \sigma_{\text{daily}} \times \sqrt{N} = \sigma_{\text{daily}} \times \sqrt{252}
$$

**Note:** Some practitioners use $N = 250$ or $N = 365$ (calendar days). The choice depends on context and convention.

### 3. When Annualization Fails


The square-root rule breaks down when:

1. **Autocorrelation exists:** Returns are not independent
2. **Volatility clustering:** Variance changes over time (GARCH)
3. **Long-range dependence:** Fractional Brownian motion
4. **Jump processes:** Discontinuous price movements

In these cases, empirical scaling may deviate from $\sqrt{N}$.

### 4. Implementation


```python
def annualize_statistics(daily_stats, N=252):
    """
    Annualize daily statistics.
    
    Parameters:
    -----------
    daily_stats : dict
        Dictionary of daily statistics
    N : int
        Number of trading days per year (default 252)
        
    Returns:
    --------
    dict : Annualized statistics
    """
    ann_stats = {
        'mean_annual': daily_stats['mean'] * N,
        'std_annual': daily_stats['std'] * np.sqrt(N),
        'sharpe_annual': (daily_stats['mean'] * N) / (daily_stats['std'] * np.sqrt(N))
                        if daily_stats['std'] > 0 else 0
    }
    
    return ann_stats
```

**Example:**

```python
# Compute daily statistics
daily = compute_statistics(df, return_col='Return_Log')

# Annualize
annual = annualize_statistics(daily, N=252)

print(f"Daily mean: {daily['mean']:.6f}")
print(f"Annual mean: {annual['mean_annual']:.4f}")
print(f"Daily volatility: {daily['std']:.6f}")
print(f"Annual volatility: {annual['std_annual']:.4f}")
```

**Typical output for S&P 500:**

```
Daily mean: 0.000320
Annual mean: 0.0807  (8.07% per year)
Daily volatility: 0.012500
Annual volatility: 0.1984  (19.84% per year)
```

---

## Diagnostics and Statistical Validation


Prior to engaging in modeling, it is imperative to subject the empirical return series to rigorous diagnostic scrutiny. The reliability of any model is only as sound as the statistical properties of its inputs.

### 1. Visual Diagnostics


**1. Price time series:**

```python
import matplotlib.pyplot as plt

def plot_price_series(df, ticker):
    """Plot price time series."""
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df.index, df['Close'], linewidth=1.5)
    ax.set_title(f'{ticker} Price Series', fontsize=14)
    ax.set_xlabel('Date')
    ax.set_ylabel('Price ($)')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
```

**What to look for:**
- Trends (bull/bear markets)
- Structural breaks (market crashes)
- Volatility regimes (calm vs turbulent periods)

**2. Return time series:**

```python
def plot_return_series(df, return_col='Return_Log'):
    """Plot return time series."""
    fig, ax = plt.subplots(figsize=(12, 4))
    ax.plot(df.index, df[return_col], linewidth=0.8, alpha=0.7)
    ax.axhline(0, color='black', linestyle='--', linewidth=1)
    ax.set_title('Log Return Series', fontsize=14)
    ax.set_xlabel('Date')
    ax.set_ylabel('Log Return')
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
```

**What to look for:**
- **Volatility clustering:** Large moves followed by large moves
- **Outliers:** Extreme events (crashes, earnings surprises)
- **Mean reversion:** Returns oscillating around zero

**3. Return distribution:**

```python
from scipy import stats

def plot_return_distribution(df, return_col='Return_Log'):
    """Plot histogram with Gaussian overlay."""
    returns = df[return_col].dropna()
    
    mu = returns.mean()
    sigma = returns.std()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Histogram
    ax.hist(returns, bins=50, density=True, alpha=0.7, 
            edgecolor='black', label='Empirical')
    
    # Gaussian overlay
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 200)
    ax.plot(x, stats.norm.pdf(x, mu, sigma), 'r-', linewidth=2,
            label='Gaussian fit')
    
    ax.set_xlabel('Log Return')
    ax.set_ylabel('Density')
    ax.set_title('Return Distribution vs Gaussian')
    ax.legend()
    ax.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()
```

**What to look for:**
- **Heavy tails:** More mass in tails than Gaussian
- **Skewness:** Asymmetry (left tail often heavier for equities)
- **Peakedness:** Returns more concentrated around mean than Gaussian

### 2. Quantitative Tests


**1. Normality tests:**

```python
def test_normality(df, return_col='Return_Log'):
    """Perform normality tests."""
    returns = df[return_col].dropna()
    
    # Jarque-Bera test
    jb_stat, jb_pval = stats.jarque_bera(returns)
    
    # Shapiro-Wilk test
    sw_stat, sw_pval = stats.shapiro(returns[:5000])  # Limited to 5000 obs
    
    # Anderson-Darling test
    ad_result = stats.anderson(returns, dist='norm')
    
    print("=" * 60)
    print("NORMALITY TESTS")
    print("=" * 60)
    print(f"Jarque-Bera statistic: {jb_stat:.4f}")
    print(f"Jarque-Bera p-value: {jb_pval:.6f}")
    print(f"  → {'REJECT' if jb_pval < 0.05 else 'FAIL TO REJECT'} normality at 5% level")
    print()
    print(f"Shapiro-Wilk statistic: {sw_stat:.4f}")
    print(f"Shapiro-Wilk p-value: {sw_pval:.6f}")
    print(f"  → {'REJECT' if sw_pval < 0.05 else 'FAIL TO REJECT'} normality at 5% level")
    print("=" * 60)
```

**Expected result:** For most financial returns, these tests **reject normality** due to fat tails and skewness.

**2. Autocorrelation analysis:**

```python
from statsmodels.graphics.tsaplots import plot_acf

def plot_autocorrelation(df, return_col='Return_Log', lags=40):
    """Plot autocorrelation function."""
    returns = df[return_col].dropna()
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # ACF of returns
    plot_acf(returns, lags=lags, ax=ax1, alpha=0.05)
    ax1.set_title('ACF of Returns')
    
    # ACF of squared returns
    plot_acf(returns**2, lags=lags, ax=ax2, alpha=0.05)
    ax2.set_title('ACF of Squared Returns (Volatility)')
    
    plt.tight_layout()
    plt.show()
```

**Expected pattern:**
- Returns: Little to no autocorrelation (markets are efficient)
- Squared returns: **Strong autocorrelation** (volatility clustering)

### 3. Rolling Window Statistics


```python
def plot_rolling_statistics(df, return_col='Return_Log', window=60):
    """Plot rolling mean and volatility."""
    returns = df[return_col]
    
    # Compute rolling statistics
    rolling_mean = returns.rolling(window=window).mean()
    rolling_std = returns.rolling(window=window).std()
    
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 8))
    
    # Rolling mean
    ax1.plot(df.index, rolling_mean, label=f'{window}-day rolling mean')
    ax1.axhline(returns.mean(), color='red', linestyle='--', 
                label='Overall mean')
    ax1.set_ylabel('Mean Return')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Rolling volatility
    ax2.plot(df.index, rolling_std, label=f'{window}-day rolling std')
    ax2.axhline(returns.std(), color='red', linestyle='--',
                label='Overall std')
    ax2.set_ylabel('Volatility')
    ax2.set_xlabel('Date')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
```

**What to look for:**
- **Time-varying volatility:** Periods of high/low uncertainty
- **Regime changes:** Shifts in mean return
- **Crisis periods:** Volatility spikes during market stress

---

## Complete Example Workflow


```python
# Complete analysis pipeline
def analyze_stock(ticker, start_date, end_date):
    """Complete stock data analysis workflow."""
    
    # 1. Retrieve data
    print(f"\n{'='*60}")
    print(f"ANALYZING {ticker}")
    print(f"{'='*60}\n")
    
    stock = USStock(ticker)
    df = stock.get_data(start_date, end_date)
    
    # 2. Quality check
    data_quality_check(df)
    
    # 3. Compute returns
    df = compute_returns(df)
    
    # 4. Compute statistics
    daily_stats = compute_statistics(df, 'Return_Log')
    annual_stats = annualize_statistics(daily_stats)
    
    # 5. Print results
    print("\nDAILY STATISTICS:")
    for key, val in daily_stats.items():
        print(f"  {key:10s}: {val:10.6f}")
    
    print("\nANNUAL STATISTICS:")
    for key, val in annual_stats.items():
        print(f"  {key:20s}: {val:10.4f}")
    
    # 6. Normality tests
    test_normality(df, 'Return_Log')
    
    # 7. Visualizations
    plot_price_series(df, ticker)
    plot_return_series(df, 'Return_Log')
    plot_return_distribution(df, 'Return_Log')
    plot_autocorrelation(df, 'Return_Log')
    plot_rolling_statistics(df, 'Return_Log')
    
    return df, daily_stats, annual_stats

# Execute
df, daily, annual = analyze_stock("AAPL", "2020-01-01", "2023-12-31")
```

---

## Summary


This section has articulated a methodologically rigorous pathway for transforming raw financial data into statistically validated return series. The combination of:

1. **Disciplined data preprocessing** (adjusted prices, quality checks)
2. **Accurate return transformation** (discrete vs continuous)
3. **Robust statistical estimation** (moments, annualization)
4. **Critical diagnostic validation** (tests, visualizations)

ensures that the inputs to subsequent modeling are both theoretically sound and empirically credible.

### 1. Key Takeaways


**Empirical observations that motivate stochastic models:**

1. Returns exhibit **time-varying volatility** (not constant as in simple models)
2. Distributions show **heavy tails** (more extreme events than Gaussian)
3. **Volatility clustering** (high volatility follows high volatility)
4. **Leverage effect** (negative returns correlate with volatility increases)

These **stylized facts** cannot be captured by deterministic models and motivate the development of stochastic differential equations in the following sections.

**Next:** We examine these stylized facts in detail and show why deterministic models are insufficient for modeling financial returns.
