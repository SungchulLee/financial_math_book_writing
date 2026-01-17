# Python Code Appendix - Chapter 24: Variance and Volatility

This appendix provides Python implementations of the key concepts and strategies covered in Chapter 24.

## Modules Overview

| Module | Purpose | Key Functions |
|--------|---------|---------------|
| `variance_swap_pricing.py` | Variance swap pricing and analytics | Log-contract replication, fair strike calculation, MTM |
| `dispersion_backtest.py` | Dispersion trading simulation | Correlation analysis, P&L simulation, Gaussian copula |
| `vrp_measurement.py` | Variance risk premium measurement | HAR-RV model, VRP time series, position sizing |
| `dynamic_hedge_backtest.py` | Dynamic hedging simulation | VIX-scaled hedging, strategy comparison |
| `correlation_analysis.py` | Correlation tracking and analysis | Implied vs realized, regime classification |

---

## Module Details

### 1. variance_swap_pricing.py

**Key Functions:**

```python
# Calculate realized variance from price series
rv = calculate_realized_variance(prices, annualization=252)

# Calculate fair variance swap strike
K_var = calculate_fair_variance_strike(
    spot, forward, strikes, call_prices, put_prices, r, T
)

# Apply discrete monitoring adjustment
K_discrete = discrete_monitoring_adjustment(K_continuous, skewness, n_observations)

# Mark-to-market calculation
mtm = mark_to_market_variance_swap(
    notional, strike, realized_variance_accrued, forward_variance,
    days_elapsed, days_total, r
)

# Convert between notionals
vega_notional = variance_to_vega_notional(variance_notional, strike_vol)
variance_notional = vega_to_variance_notional(vega_notional, strike_vol)
```

### 2. dispersion_backtest.py

**Key Functions:**

```python
# Gaussian copula approximation for index vol
index_vol = gaussian_copula_index_vol(avg_stock_vol, avg_correlation, n_stocks)

# Calculate implied correlation from option prices
impl_corr = calculate_implied_correlation(index_iv, stock_ivs, weights)

# Correlation swap strike
K_rho = calculate_correlation_swap_strike(index_iv, stock_ivs, weights)

# Simulate dispersion trade P&L
result = simulate_dispersion_trade_pnl(index_returns, stock_returns, trade_spec)
```

### 3. vrp_measurement.py

**Key Functions:**

```python
# Fit HAR-RV model
params = fit_har_rv_model(rv_series, forecast_horizon=22)

# Forecast realized variance
rv_forecast = forecast_realized_variance(rv_d, rv_w, rv_m, params)

# Calculate VRP series
vrp = calculate_vrp_series(implied_variance, returns, method='har_rv')

# VRP-based position sizing
position = vrp_based_position_sizing(vrp, vix, base_notional)
```

### 4. dynamic_hedge_backtest.py

**Key Functions:**

```python
# VIX-based scaling functions
ratio = linear_vix_scaling(vix, vix_min=12, vix_max=22)
ratio = sigmoid_vix_scaling(vix, vix_mid=20, steepness=0.2)
ratio = conditional_hedge_rule(vix, threshold_low=15, threshold_high=25)

# Rebalancing decision
should_rebal = should_rebalance(vix_current, vix_last, days_since_last)

# Full backtest
results_df, summary = backtest_dynamic_hedge(
    portfolio_returns, vix_series, implied_variance, scaling_func
)

# Compare strategies
comparison = compare_hedge_strategies(
    portfolio_returns, vix_series, implied_variance
)
```

### 5. correlation_analysis.py

**Key Functions:**

```python
# Rolling correlation
corr = calculate_rolling_correlation(returns1, returns2, window=20)
avg_corr = calculate_average_pairwise_correlation(returns_df, window=20)

# VIX-correlation relationship
relationship = estimate_vix_correlation_relationship(vix_series, corr_series)
pred_corr = predict_correlation_from_vix(vix, alpha, beta)

# Regime classification
regime = classify_correlation_regime(correlation, vix)

# Trading signal
signal = generate_correlation_trading_signal(implied_corr, realized_corr, vix)
```

---

## Dependencies

```
numpy>=1.20.0
pandas>=1.3.0
scipy>=1.7.0
```

## Usage Example

```python
import numpy as np
import pandas as pd
from variance_swap_pricing import calculate_realized_variance, calculate_fair_variance_strike
from dispersion_backtest import gaussian_copula_index_vol, simulate_dispersion_trade_pnl
from vrp_measurement import fit_har_rv_model, calculate_vrp_series
from dynamic_hedge_backtest import backtest_dynamic_hedge, linear_vix_scaling
from correlation_analysis import calculate_average_pairwise_correlation

# Example: Calculate VRP and set up dynamic hedge
# 1. Get market data
returns = pd.read_csv('returns.csv', index_col=0, parse_dates=True)
vix = pd.read_csv('vix.csv', index_col=0, parse_dates=True)['VIX']

# 2. Calculate realized variance
rv = calculate_realized_variance(returns.values, annualization=252)

# 3. Fit HAR-RV model
rv_series = pd.Series(rv, index=returns.index)
params = fit_har_rv_model(rv_series)

# 4. Backtest dynamic hedge
results, summary = backtest_dynamic_hedge(
    returns, vix, implied_variance,
    lambda v: linear_vix_scaling(v, 12, 22)
)

print(f"Total P&L: ${summary.total_pnl:,.0f}")
print(f"Sharpe: {summary.sharpe_ratio:.2f}")
```

---

## Running Tests

Each module includes a `__main__` block with demonstrations:

```bash
python variance_swap_pricing.py
python dispersion_backtest.py
python vrp_measurement.py
python dynamic_hedge_backtest.py
python correlation_analysis.py
```

---

## Notes

1. **Data Requirements:** These modules work with daily return data. Intraday data would provide more accurate realized variance estimates.

2. **Production Use:** For production systems, add proper error handling, logging, and consider using vectorized operations for performance.

3. **Model Limitations:** The HAR-RV model assumes stationarity. During regime changes, consider re-fitting the model.

4. **Transaction Costs:** The backtests include simplified transaction cost models. Real trading would require more detailed cost modeling.

---

## Related Chapters

- Chapter 7: Implied Volatility (for option pricing inputs)
- Chapter 9: Stochastic Volatility (for vol-of-vol modeling)
- Chapter 12: Risk Management (for VaR and stress testing)
- Chapter 17: IV Strategies (for related trading strategies)
