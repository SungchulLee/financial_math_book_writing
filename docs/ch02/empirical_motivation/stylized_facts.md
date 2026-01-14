# Stylized Facts of Financial Returns


Having established proper data handling and return computation in the previous section, we now turn to the **empirical regularities** observed across financial markets. These "stylized facts" are robust statistical patterns that appear consistently across different assets, time periods, and markets. Understanding these regularities is essential because they reveal the limitations of simple models and motivate the sophisticated stochastic frameworks developed in subsequent chapters.

---

## The Importance of Stylized Facts


**Definition:** A **stylized fact** is an empirical regularity that:
1. Appears consistently across multiple datasets
2. Is robust to different measurement methods
3. Cannot be explained by simple deterministic or i.i.d. models
4. Guides the development of realistic mathematical models

**Historical context:** The term was popularized by Nicholas Kaldor (1961) in economics and adapted to finance by Rama Cont (2001) in his influential survey of empirical properties of asset returns.

**Why they matter:**

- They constrain which models are plausible
- They guide model calibration and parameter estimation
- They reveal market microstructure and behavioral patterns
- They inform risk management and trading strategies

---

## Stylized Fact 1: Heavy Tails (Leptokurtosis)


### 1. Observation


**Empirical finding:** The distribution of financial returns has **fatter tails** than the Gaussian (normal) distribution.

**Quantitative evidence:**

- **Excess kurtosis:** For Gaussian, kurtosis = 3. For S&P 500 daily returns: kurtosis ≈ 7-10
- **Extreme events:** Returns beyond 5 standard deviations occur far more frequently than Gaussian predicts

**Gaussian prediction vs reality:**

| Event | Gaussian Probability | Empirical Frequency |
|-------|---------------------|-------------------|
| $\|r\| > 5\sigma$ | Once per 3.5 million days | Once per 3-5 years |
| $\|r\| > 4\sigma$ | Once per 31,000 days | Once per year |
| $\|r\| > 3\sigma$ | Once per 370 days | Once per 3 months |

### 2. Visualization


```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def compare_tail_behavior(df, return_col='Return_Log'):
    """Compare empirical tails to Gaussian."""
    returns = df[return_col].dropna()
    standardized = (returns - returns.mean()) / returns.std()
    
    # Empirical quantiles
    emp_quantiles = np.percentile(standardized, [0.1, 1, 5, 95, 99, 99.9])
    
    # Gaussian quantiles
    gauss_quantiles = stats.norm.ppf([0.001, 0.01, 0.05, 0.95, 0.99, 0.999])
    
    # Q-Q plot
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    
    # Q-Q plot
    stats.probplot(standardized, dist="norm", plot=ax1)
    ax1.set_title('Q-Q Plot: Returns vs Gaussian', fontsize=12)
    ax1.grid(True, alpha=0.3)
    
    # Tail comparison
    labels = ['0.1%', '1%', '5%', '95%', '99%', '99.9%']
    x = np.arange(len(labels))
    width = 0.35
    
    ax2.bar(x - width/2, emp_quantiles, width, label='Empirical', alpha=0.7)
    ax2.bar(x + width/2, gauss_quantiles, width, label='Gaussian', alpha=0.7)
    ax2.set_xticks(x)
    ax2.set_xticklabels(labels)
    ax2.set_ylabel('Standardized Return')
    ax2.set_title('Tail Quantiles: Empirical vs Gaussian')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Print comparison
    print("\nTAIL COMPARISON:")
    print("="*50)
    print(f"{'Percentile':<12} {'Empirical':>12} {'Gaussian':>12}")
    print("="*50)
    for i, label in enumerate(labels):
        print(f"{label:<12} {emp_quantiles[i]:>12.3f} {gauss_quantiles[i]:>12.3f}")
```

**Interpretation:** Deviation from 45-degree line in Q-Q plot indicates fat tails.

### 3. Mathematical Characterization


**Power-law tails:** Empirical evidence suggests:

$$
P(|r| > x) \sim x^{-\alpha} \quad \text{for large } x
$$

with **tail index** $\alpha \approx 3-5$ (compared to Gaussian's exponential decay).

**Student's t-distribution:** A common alternative to Gaussian:

$$
f(x; \nu) \propto \left(1 + \frac{x^2}{\nu}\right)^{-(\nu+1)/2}
$$

with degrees of freedom $\nu \approx 4-6$ for S&P 500.

### 4. Implications


1. **Risk management:** VaR underestimated if Gaussian assumed
2. **Option pricing:** Out-of-the-money options more valuable
3. **Portfolio optimization:** Tail risk dominates mean-variance trade-off
4. **Market crashes:** More frequent than simple models predict

---

## Stylized Fact 2: Volatility Clustering


### 1. Observation


**Mandelbrot (1963):** "Large changes tend to be followed by large changes—of either sign—and small changes tend to be followed by small changes."

**Quantitative evidence:**

- Returns show **little autocorrelation**: $\text{Corr}(r_t, r_{t+k}) \approx 0$
- **Squared returns** show strong autocorrelation: $\text{Corr}(r_t^2, r_{t+k}^2) > 0$ for $k \leq 100$
- **Absolute returns** also autocorrelated: $\text{Corr}(|r_t|, |r_{t+k}|) > 0$

### 2. Visualization


```python
def plot_volatility_clustering(df, return_col='Return_Log'):
    """Visualize volatility clustering."""
    returns = df[return_col].dropna()
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 10))
    
    # Returns over time
    ax1.plot(returns.index, returns, linewidth=0.5, alpha=0.7)
    ax1.set_ylabel('Return')
    ax1.set_title('Return Series: Observe Clustering of Large Moves')
    ax1.grid(True, alpha=0.3)
    
    # Squared returns (volatility proxy)
    ax2.plot(returns.index, returns**2, linewidth=0.5, alpha=0.7, color='red')
    ax2.set_ylabel('Squared Return')
    ax2.set_title('Squared Returns: Volatility Proxy')
    ax2.grid(True, alpha=0.3)
    
    # 20-day rolling volatility
    rolling_vol = returns.rolling(window=20).std()
    ax3.plot(returns.index, rolling_vol, linewidth=1.5, color='darkred')
    ax3.set_ylabel('Rolling Volatility')
    ax3.set_xlabel('Date')
    ax3.set_title('20-Day Rolling Volatility')
    ax3.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
```

### 3. Autocorrelation Analysis


```python
from statsmodels.graphics.tsaplots import plot_acf

def analyze_autocorrelation(df, return_col='Return_Log', lags=100):
    """Compare autocorrelation of returns and squared returns."""
    returns = df[return_col].dropna()
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 10))
    
    # ACF of returns
    plot_acf(returns, lags=lags, ax=ax1, alpha=0.05)
    ax1.set_title('ACF of Returns (Should be near zero)')
    ax1.set_ylabel('Autocorrelation')
    
    # ACF of squared returns
    plot_acf(returns**2, lags=lags, ax=ax2, alpha=0.05)
    ax2.set_title('ACF of Squared Returns (Shows persistence)')
    ax2.set_ylabel('Autocorrelation')
    
    # ACF of absolute returns
    plot_acf(np.abs(returns), lags=lags, ax=ax3, alpha=0.05)
    ax3.set_title('ACF of Absolute Returns (Also shows persistence)')
    ax3.set_ylabel('Autocorrelation')
    ax3.set_xlabel('Lag')
    
    plt.tight_layout()
    plt.show()
```

### 4. ARCH/GARCH Effects


**ARCH test:** Tests null hypothesis of no ARCH effects.

```python
from statsmodels.stats.diagnostic import het_arch

def test_arch_effects(df, return_col='Return_Log', nlags=10):
    """Test for ARCH effects."""
    returns = df[return_col].dropna()
    
    # Engle's ARCH test
    test_stat, p_value, _, _ = het_arch(returns, nlags=nlags)
    
    print(f"\nARCH TEST (Testing for volatility clustering):")
    print(f"  Test statistic: {test_stat:.4f}")
    print(f"  P-value: {p_value:.6f}")
    print(f"  Conclusion: {'REJECT H0 - ARCH effects present' if p_value < 0.05 else 'Fail to reject H0'}")
```

**Expected result:** Strong rejection of null hypothesis → volatility clustering present.

### 5. Implications


1. **Conditional heteroskedasticity:** Variance changes over time
2. **GARCH models:** Essential for volatility forecasting
3. **Option pricing:** Stochastic volatility models needed
4. **Risk management:** Time-varying VaR estimates

---

## Stylized Fact 3: Leverage Effect


### 1. Observation


**Black (1976):** Negative correlation between returns and volatility changes.

**Asymmetry:**
- **Negative returns** → volatility **increases** (strong effect)
- **Positive returns** → volatility **decreases** (weaker effect)

**Quantitative evidence:** Correlation between $r_t$ and $\sigma_{t+1}$ typically $\rho \approx -0.5$ to $-0.7$ for equity indices.

### 2. Visualization


```python
def plot_leverage_effect(df, return_col='Return_Log', window=20):
    """Visualize leverage effect."""
    returns = df[return_col].dropna()
    
    # Compute rolling volatility (forward-looking)
    rolling_vol = returns.rolling(window=window).std().shift(-window)
    
    # Scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))
    
    scatter = ax.scatter(returns, rolling_vol, alpha=0.3, s=10)
    
    # Add trend line
    from numpy.polynomial import Polynomial
    mask = ~np.isnan(rolling_vol)
    p = Polynomial.fit(returns[mask], rolling_vol[mask], deg=1)
    x_fit = np.linspace(returns.min(), returns.max(), 100)
    y_fit = p(x_fit)
    ax.plot(x_fit, y_fit, 'r-', linewidth=2, label='Linear fit')
    
    # Correlation
    corr = np.corrcoef(returns[mask], rolling_vol[mask])[0, 1]
    
    ax.set_xlabel('Return')
    ax.set_ylabel(f'Future {window}-Day Volatility')
    ax.set_title(f'Leverage Effect (Correlation: {corr:.3f})')
    ax.legend()
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    print(f"Correlation(return, future volatility): {corr:.4f}")
```

### 3. Explanations


**Original (Black):** Financial leverage hypothesis
- Stock price ↓ → Debt/Equity ↑ → Financial risk ↑ → Volatility ↑

**Alternative (Campbell-Hentschel):** Volatility feedback
- Expected volatility ↑ → Required return ↑ → Price ↓

**Behavioral:** Risk aversion and loss aversion
- Losses trigger panic selling → Volatility ↑

### 4. Implications


1. **Asymmetric models needed:** EGARCH, GJR-GARCH
2. **Option pricing:** Skewed implied volatility surface
3. **Risk management:** Downside risk management crucial
4. **Portfolio hedging:** Protective puts more expensive

---

## Stylized Fact 4: Absence of Autocorrelation in Returns


### 1. Observation


**Efficient Market Hypothesis (EMH):** Asset prices reflect all available information.

**Implication:** Returns should be **unpredictable** from past returns.

**Empirical evidence:**

$$
\text{Corr}(r_t, r_{t-k}) \approx 0 \quad \text{for } k \geq 1
$$

(with minor exceptions at very short horizons due to microstructure effects)

### 2. Testing


```python
from statsmodels.stats.diagnostic import acorr_ljungbox

def test_return_predictability(df, return_col='Return_Log', lags=20):
    """Test for return autocorrelation."""
    returns = df[return_col].dropna()
    
    # Ljung-Box test for autocorrelation
    lb_test = acorr_ljungbox(returns, lags=lags, return_df=True)
    
    print(f"\nLJUNG-BOX TEST FOR AUTOCORRELATION:")
    print("="*60)
    print(f"{'Lag':<10} {'Test Statistic':<20} {'P-value':<15}")
    print("="*60)
    
    for i in range(min(10, lags)):
        print(f"{i+1:<10} {lb_test['lb_stat'].iloc[i]:<20.4f} {lb_test['lb_pvalue'].iloc[i]:<15.6f}")
    
    # Overall conclusion
    significant = (lb_test['lb_pvalue'] < 0.05).sum()
    print(f"\nSignificant autocorrelations (5% level): {significant} out of {lags}")
```

### 3. Implications


1. **Market efficiency:** Past returns don't predict future returns
2. **Technical analysis limited:** Trend-following strategies face challenges
3. **Random walk hypothesis:** First-order approximation
4. **Martingale models:** Appropriate for pricing

---

## Stylized Fact 5: Aggregational Gaussianity


### 1. Observation


**Time-scaling property:** As aggregation horizon increases, returns become **more Gaussian**.

- **Daily returns:** Fat-tailed, skewed, leptokurtic
- **Monthly returns:** Closer to Gaussian
- **Yearly returns:** Approximately Gaussian

**Central Limit Theorem:** Sum of i.i.d. random variables → Gaussian

**But:** Volatility clustering violates independence, slowing convergence.

### 2. Demonstration


```python
def demonstrate_aggregational_gaussianity(df, return_col='Return_Log'):
    """Show how distribution becomes more Gaussian with aggregation."""
    returns = df[return_col].dropna()
    
    # Compute returns at different horizons
    daily = returns
    weekly = returns.rolling(window=5).sum().dropna()
    monthly = returns.rolling(window=21).sum().dropna()
    
    fig, axes = plt.subplots(1, 3, figsize=(15, 4))
    
    for ax, data, label in zip(axes, [daily, weekly, monthly], 
                                 ['Daily', 'Weekly', 'Monthly']):
        # Standardize
        std_data = (data - data.mean()) / data.std()
        
        # Histogram
        ax.hist(std_data, bins=50, density=True, alpha=0.7, edgecolor='black')
        
        # Gaussian overlay
        x = np.linspace(-4, 4, 200)
        ax.plot(x, stats.norm.pdf(x), 'r-', linewidth=2, label='Gaussian')
        
        # Compute kurtosis
        kurt = stats.kurtosis(std_data)
        
        ax.set_title(f'{label} Returns\nKurtosis: {kurt:.2f}')
        ax.set_xlabel('Standardized Return')
        ax.set_ylabel('Density')
        ax.legend()
        ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
```

### 3. Implications


1. **Long-horizon modeling:** Gaussian approximation more justified
2. **Short-horizon risks:** Non-Gaussian models essential
3. **Value-at-Risk:** Horizon-dependent model selection

---

## Stylized Fact 6: Slow Decay of Autocorrelation in Absolute Returns


### 1. Observation


**Long memory in volatility:** The autocorrelation function of $|r_t|$ decays **slowly** (power-law rather than exponential).

$$
\text{Corr}(|r_t|, |r_{t+k}|) \sim k^{-\beta} \quad \text{with } \beta \approx 0.2-0.4
$$

This is **slower** than exponential decay $e^{-\lambda k}$.

### 2. Implications


1. **Long-memory models:** Fractionally integrated processes
2. **FIGARCH models:** Capture long-range dependence
3. **Volatility forecasting:** Past volatility relevant for long horizons

---

## Stylized Fact 7: Volume-Volatility Correlation


### 1. Observation


**Positive correlation** between trading volume and volatility:

- High volume → High volatility
- Low volume → Low volatility

**Sequential information arrival:** Both driven by information flow to market.

### 2. Implications


1. **Market microstructure:** Information-based trading models
2. **Liquidity risk:** Volume-dependent transaction costs
3. **Volatility modeling:** Incorporate volume as explanatory variable

---

## Stylized Fact 8: Asymmetry in Time Scales


### 1. Observation


**Different behavior at different frequencies:**

- **Intraday (seconds to minutes):** Microstructure noise, bid-ask bounce
- **Daily:** Stylized facts most pronounced
- **Weekly/Monthly:** More Gaussian, mean reversion possible
- **Yearly:** Fundamental factors dominate

### 2. Implications


Model selection depends critically on time horizon of analysis.

---

## Summary of Stylized Facts


| Stylized Fact | Implication | Model Feature Needed |
|--------------|-------------|---------------------|
| **Heavy tails** | Extreme events common | Non-Gaussian innovations |
| **Volatility clustering** | Volatility persistent | GARCH, stochastic volatility |
| **Leverage effect** | Downside risk asymmetric | Correlation structure |
| **No return autocorrelation** | Markets efficient | Martingale structure |
| **Aggregational Gaussianity** | CLT applies long-term | Time-dependent distributions |
| **Long memory in |r|** | Volatility long-range dependent | Fractional processes |
| **Volume-volatility** | Information-based trading | Microstructure models |

---

## Complete Diagnostic Code


```python
def complete_stylized_facts_analysis(df, return_col='Return_Log'):
    """
    Comprehensive analysis of stylized facts.
    
    Parameters:
    -----------
    df : DataFrame
        DataFrame with return data
    return_col : str
        Name of return column
    """
    print("\n" + "="*70)
    print("STYLIZED FACTS ANALYSIS")
    print("="*70)
    
    returns = df[return_col].dropna()
    
    # 1. Heavy tails
    print("\n1. HEAVY TAILS:")
    kurt = stats.kurtosis(returns)
    skew = stats.skew(returns)
    print(f"   Excess kurtosis: {kurt:.4f} (Gaussian = 0)")
    print(f"   Skewness: {skew:.4f} (Gaussian = 0)")
    
    compare_tail_behavior(df, return_col)
    
    # 2. Volatility clustering
    print("\n2. VOLATILITY CLUSTERING:")
    test_arch_effects(df, return_col)
    analyze_autocorrelation(df, return_col)
    plot_volatility_clustering(df, return_col)
    
    # 3. Leverage effect
    print("\n3. LEVERAGE EFFECT:")
    plot_leverage_effect(df, return_col)
    
    # 4. Return predictability
    print("\n4. RETURN PREDICTABILITY:")
    test_return_predictability(df, return_col)
    
    # 5. Aggregational Gaussianity
    print("\n5. AGGREGATIONAL GAUSSIANITY:")
    demonstrate_aggregational_gaussianity(df, return_col)
    
    print("\n" + "="*70)
    print("ANALYSIS COMPLETE")
    print("="*70)

# Execute
complete_stylized_facts_analysis(df, 'Return_Log')
```

---

## Conclusion


These stylized facts reveal that financial returns are **far more complex** than simple i.i.d. Gaussian processes. Key challenges for modeling:

1. **Time-varying volatility** (not constant)
2. **Fat tails** (not Gaussian)
3. **Asymmetric responses** (not symmetric)
4. **Long memory** (not Markov)

**Next step:** Understand why deterministic models cannot capture these phenomena and why we need stochastic differential equations.
