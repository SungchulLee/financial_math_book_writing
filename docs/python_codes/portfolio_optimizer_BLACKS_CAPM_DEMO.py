import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Requires: PortfolioOptimizer class
# from portfolio_optimizer_CLASS import PortfolioOptimizer

# Step 1: Initialize the optimizer
tickers = ['META', 'AAPL', 'NFLX', 'GOOG']
start_date = '2024-01-01'
end_date = '2024-12-31'
risk_free_rate = 0.03
num_portfolios = 100_000

optimizer = PortfolioOptimizer(tickers, start_date, end_date, risk_free_rate)

# Step 2: Plot the efficient frontier and both CAPM lines (Standard and Black's)
fig, ax = plt.subplots(figsize=(8, 3))
optimizer.plot_random_portfolios(ax, num_portfolios=num_portfolios, short=True)
optimizer.plot_capital_market_line(ax, short=True)
optimizer.plot_zero_beta_line(ax, short=True)
optimizer.plot_efficient_frontier(ax, short=True)
optimizer.plot_gmvp(ax, short=True)
optimizer.plot_equal_portfolio(ax)
optimizer.plot_zero_beta_portfolio(ax, short=True)

# Plot individual assets with smaller annotation offset
volatilities = pd.Series(np.sqrt(np.diag(optimizer.sigma)), index=optimizer.mu.index)
for ticker in optimizer.mu.index:
    x = volatilities[ticker]
    y = optimizer.mu[ticker]
    ax.plot(x, y, 'o', color='red')
    ax.annotate(ticker, (x + 0.002, y), fontsize=9)

# Set reasonable axis limits
returns = optimizer.mu.values
vols = np.sqrt(np.diag(optimizer.sigma))
ax.set_xlim([0, np.percentile(vols, 99) * 1.5])
ax.set_ylim([0, np.percentile(returns, 99) * 1.5])

ax.set_title("Efficient Frontier with Capital Market Line and Zero-Beta Line")
ax.set_xlabel("Volatility (σ)")
ax.set_ylabel("Expected Return (μ)")
ax.grid(True)

# Move legend outside
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()

print(end="\n\n\n")

# Step 3: Compare theoretical vs empirical efficient frontier
fig, ax = plt.subplots(figsize=(8, 3))
optimizer.plot_theoretical_vs_empirical_frontier(ax)

# Add grid, tighter view
ax.grid(True)
ax.set_xlim(left=0)
ax.set_ylim(bottom=0)

# Add titles and labels
ax.set_title("Theoretical vs Empirical Efficient Frontier")
ax.set_xlabel("Volatility (σ)")
ax.set_ylabel("Expected Return (μ)")

# Optional: highlight endpoints (e.g., GMVP or max return)
df_theory = optimizer.efficient_frontier(short=True)
df_empirical = optimizer.efficient_frontier(short=False)

# Plot endpoints
ax.plot(df_theory.Volatility.iloc[[0, -1]], df_theory.Return.iloc[[0, -1]], 'o', color='blue')
ax.plot(df_empirical.Volatility.iloc[[0, -1]], df_empirical.Return.iloc[[0, -1]], 'o', color='orange')

# Move legend outside
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.tight_layout()
plt.show()

print(end="\n\n\n")

# Step 4: Plot return-beta lines for Standard CAPM vs Black's CAPM
fig, ax = plt.subplots(figsize=(8, 3))
optimizer.plot_return_beta_lines(ax)
ax.set_title("Return vs Beta: Standard CAPM vs Black's CAPM")
plt.tight_layout()
plt.show()

print("\n\n\n")

# Step 5: Display Alpha Table for Deeper Insight (no display())
print("Alpha Comparison Table (CAPM vs Black's CAPM):\n")
alpha_table = optimizer.compute_alpha_table().sort_values("Alpha (CAPM)", ascending=False)
print(alpha_table.to_string())