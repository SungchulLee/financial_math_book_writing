import numpy as np
import matplotlib.pyplot as plt

# Requires: PortfolioOptimizer class
# from portfolio_optimizer_CLASS import PortfolioOptimizer

tickers = ['META', 'AAPL', 'NFLX', 'GOOG']
start_date = '2024-01-01'
end_date = '2024-12-31'
risk_free_rate = 0.03
num_portfolios = 100_000

optimizer = PortfolioOptimizer(tickers, start_date, end_date, risk_free_rate)
optimizer.plot()
optimizer.compare_strategies()

# 1. Rolling Sharpe Ratio (equal-weighted)
rolling_sharpe = optimizer.rolling_sharpe_ratio(window=63)
rolling_sharpe.plot(title="Rolling Sharpe Ratio (63-day)", figsize=(10, 5))
plt.xlabel("Date")
plt.ylabel("Sharpe Ratio")
plt.grid(True)
plt.tight_layout()
plt.show()

# 2. Plot correlation matrix
optimizer.plot_correlation_matrix()

# 3. Value at Risk (VaR) for equal-weighted portfolio
w_equal = optimizer.equal_portfolio()
var_95 = optimizer.value_at_risk(w_equal, alpha=0.05)
print(f"\n📉 95% Value at Risk (VaR) for Equal-Weighted Portfolio: {var_95:.4%}")

# 4. Return distribution plots
optimizer.plot_return_distributions()

# 5. Custom objective optimization (example: minimize negative Sharpe ratio)
def custom_neg_sharpe(weights):
    # Return negative Sharpe ratio (must avoid NaNs or divisions by zero)
    try:
        return -optimizer.portfolio_performance(weights)[2]
    except:
        return 1e6  # Large penalty in case of failure

n = len(optimizer.mu)
bounds = [(0, 1)] * n  # Long-only (non-negative weights)
constraints = {'type': 'eq', 'fun': lambda w: np.sum(w) - 1}  # Weights sum to 1

custom_opt_weights = optimizer.optimize_custom_objective(
    objective_fn=custom_neg_sharpe,
    bounds=bounds,
    constraints=constraints
)

r, v, s = optimizer.portfolio_performance(custom_opt_weights)
print("\n🧮 Custom Optimized Portfolio (Max Sharpe via Custom Objective):")
print(custom_opt_weights.apply(lambda x: f"{x:.2%}"))
print(f"Return: {r:.2%}, Volatility: {v:.2%}, Sharpe: {s:.2f}")