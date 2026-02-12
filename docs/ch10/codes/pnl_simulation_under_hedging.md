# Python: P&L Simulation under Hedging Strategies


This section implements a comprehensive P&L simulator that compares hedging strategies under realistic conditions including gamma and vega effects.

---

## Simulation framework


The simulator tracks a portfolio consisting of European call options and various hedging instruments over a simulated price path, computing P&L under different hedging approaches.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


def bs_price(S, K, tau, r, sigma, option_type='call'):
    """Black-Scholes European option price."""
    if np.any(tau < 1e-10):
        tau = np.maximum(tau, 1e-10)
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * tau) / (sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)
    if option_type == 'call':
        return S * norm.cdf(d1) - K * np.exp(-r * tau) * norm.cdf(d2)
    else:
        return K * np.exp(-r * tau) * norm.cdf(-d2) - S * norm.cdf(-d1)


def bs_delta(S, K, tau, r, sigma, option_type='call'):
    """Black-Scholes delta."""
    tau = np.maximum(tau, 1e-10)
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * tau) / (sigma * np.sqrt(tau))
    if option_type == 'call':
        return norm.cdf(d1)
    else:
        return norm.cdf(d1) - 1


def bs_gamma(S, K, tau, r, sigma):
    """Black-Scholes gamma (same for calls and puts)."""
    tau = np.maximum(tau, 1e-10)
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * tau) / (sigma * np.sqrt(tau))
    return norm.pdf(d1) / (S * sigma * np.sqrt(tau))


def bs_vega(S, K, tau, r, sigma):
    """Black-Scholes vega."""
    tau = np.maximum(tau, 1e-10)
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * tau) / (sigma * np.sqrt(tau))
    return S * np.sqrt(tau) * norm.pdf(d1)
```

---

## Single-path P&L comparison


```python
np.random.seed(123)

# Parameters
S0, K, T, r, sigma = 100, 100, 0.25, 0.05, 0.20
num_options = 100
n_steps = 63  # daily rebalancing for ~3 months
dt = T / n_steps

# Generate one stock price path (GBM)
Z = np.random.randn(n_steps)
S_path = np.zeros(n_steps + 1)
S_path[0] = S0
for i in range(n_steps):
    S_path[i+1] = S_path[i] * np.exp((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z[i])

# Initial option value
V0 = num_options * bs_price(S0, K, T, r, sigma)

# Track P&L for each strategy
pnl_unhedged = np.zeros(n_steps + 1)
pnl_static = np.zeros(n_steps + 1)
pnl_dynamic = np.zeros(n_steps + 1)

# Initial delta for static hedge
delta_0 = bs_delta(S0, K, T, r, sigma)
static_shares = -num_options * delta_0

# Dynamic hedge: track share position
dyn_shares = -num_options * delta_0

for i in range(n_steps):
    tau_i = T - i * dt
    dS = S_path[i+1] - S_path[i]

    # Option value change
    V_now = num_options * bs_price(S_path[i], K, tau_i, r, sigma)
    V_next = num_options * bs_price(S_path[i+1], K, tau_i - dt, r, sigma)
    dV = V_next - V_now

    # Unhedged: just option P&L
    pnl_unhedged[i+1] = pnl_unhedged[i] + dV

    # Static hedge: option + fixed share position
    pnl_static[i+1] = pnl_static[i] + dV + static_shares * dS

    # Dynamic hedge: option + rebalanced share position
    pnl_dynamic[i+1] = pnl_dynamic[i] + dV + dyn_shares * dS

    # Rebalance dynamic hedge
    if tau_i - dt > 1e-8:
        new_delta = bs_delta(S_path[i+1], K, tau_i - dt, r, sigma)
        dyn_shares = -num_options * new_delta

# Plot
days = np.arange(n_steps + 1)

fig, axes = plt.subplots(2, 1, figsize=(14, 10))

axes[0].plot(days, S_path, 'k-', linewidth=2)
axes[0].axhline(K, color='red', linestyle='--', alpha=0.5, label=f'Strike = {K}')
axes[0].set_ylabel('Stock Price ($)')
axes[0].set_title('Simulated Stock Price Path')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(days, pnl_unhedged, label='Unhedged', linewidth=2)
axes[1].plot(days, pnl_static, label='Static Delta Hedge', linewidth=2)
axes[1].plot(days, pnl_dynamic, label='Dynamic Delta Hedge', linewidth=2)
axes[1].axhline(0, color='gray', linestyle='--', alpha=0.5)
axes[1].set_xlabel('Trading Day')
axes[1].set_ylabel('Cumulative P&L ($)')
axes[1].set_title('P&L Evolution under Different Hedging Strategies')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

---

## Multi-path Monte Carlo with hedging frequency analysis


```python
np.random.seed(42)

S0, K, T, r, sigma = 100, 100, 0.5, 0.05, 0.20
num_options = 1
n_paths = 10000

rebalance_frequencies = [1, 5, 21, 63]  # daily, weekly, monthly, quarterly
freq_labels = ['Daily', 'Weekly', 'Monthly', 'Quarterly']
colors = ['#2196F3', '#4CAF50', '#FF9800', '#F44336']

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
axes = axes.flatten()

for idx, (n_rebal, label) in enumerate(zip(rebalance_frequencies, freq_labels)):
    n_steps = max(int(T * 252), 252)
    dt_sim = T / n_steps
    rebal_interval = max(n_steps // n_rebal, 1) if n_rebal < n_steps else 1

    # Simulate paths
    Z = np.random.randn(n_paths, n_steps)
    S = np.zeros((n_paths, n_steps + 1))
    S[:, 0] = S0
    for i in range(n_steps):
        S[:, i+1] = S[:, i] * np.exp((r - 0.5*sigma**2)*dt_sim
                                       + sigma*np.sqrt(dt_sim)*Z[:, i])

    # Compute hedge P&L
    hedge_gains = np.zeros(n_paths)
    current_delta = bs_delta(S0, K, T, r, sigma) * np.ones(n_paths)

    for i in range(n_steps):
        hedge_gains += current_delta * (S[:, i+1] - S[:, i])

        # Rebalance?
        if (i + 1) % rebal_interval == 0:
            tau_i = T - (i + 1) * dt_sim
            if tau_i > 1e-8:
                current_delta = bs_delta(S[:, i+1], K, tau_i, r, sigma)

    # Final P&L
    payoff = np.maximum(S[:, -1] - K, 0)
    option_cost = bs_price(S0, K, T, r, sigma)
    hedged_pnl = np.exp(-r*T) * payoff - hedge_gains - option_cost

    axes[idx].hist(hedged_pnl, bins=80, alpha=0.7, color=colors[idx],
                   edgecolor='black', linewidth=0.5, density=True)
    axes[idx].axvline(0, color='red', linestyle='--')
    axes[idx].set_title(f'{label} Rebalancing (std={hedged_pnl.std():.4f})')
    axes[idx].set_xlabel('Hedging P&L ($)')

plt.suptitle('Effect of Rebalancing Frequency on Hedging Error', fontsize=14)
plt.tight_layout()
plt.show()
```

This demonstrates that more frequent rebalancing reduces hedging error variance, but with diminishing returns (the error scales as \(\sqrt{\Delta t}\)).

---

## P&L decomposition: theta vs. gamma


```python
np.random.seed(7)

S0, K, T, r, sigma = 100, 100, 0.1, 0.05, 0.20
n_steps = 25
dt = T / n_steps

# Simulate path
Z = np.random.randn(n_steps)
S_path = np.zeros(n_steps + 1)
S_path[0] = S0
for i in range(n_steps):
    S_path[i+1] = S_path[i] * np.exp((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z[i])

# Decompose daily hedged P&L into theta and gamma components
theta_pnl = np.zeros(n_steps)
gamma_pnl = np.zeros(n_steps)

for i in range(n_steps):
    tau_i = T - i * dt
    S_i = S_path[i]
    dS = S_path[i+1] - S_path[i]

    d1 = (np.log(S_i / K) + (r + 0.5*sigma**2) * tau_i) / (sigma * np.sqrt(tau_i))
    d2 = d1 - sigma * np.sqrt(tau_i)

    gamma_i = norm.pdf(d1) / (S_i * sigma * np.sqrt(tau_i))
    theta_i = (-S_i * norm.pdf(d1) * sigma / (2 * np.sqrt(tau_i))
               - r * K * np.exp(-r * tau_i) * norm.cdf(d2))

    theta_pnl[i] = theta_i * dt
    gamma_pnl[i] = 0.5 * gamma_i * dS**2

days = np.arange(1, n_steps + 1)

fig, axes = plt.subplots(2, 1, figsize=(12, 8))

axes[0].bar(days, theta_pnl, alpha=0.7, color='red', label='Theta (time decay)')
axes[0].bar(days, gamma_pnl, alpha=0.7, color='green', label='Gamma (convexity gain)',
            bottom=theta_pnl)
axes[0].set_ylabel('Daily P&L ($)')
axes[0].set_title('Delta-Hedged P&L Decomposition: Theta vs Gamma')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

axes[1].plot(days, np.cumsum(theta_pnl), 'r-', linewidth=2, label='Cumulative Theta')
axes[1].plot(days, np.cumsum(gamma_pnl), 'g-', linewidth=2, label='Cumulative Gamma')
axes[1].plot(days, np.cumsum(theta_pnl + gamma_pnl), 'k--', linewidth=2,
             label='Total Hedged P&L')
axes[1].set_xlabel('Trading Day')
axes[1].set_ylabel('Cumulative P&L ($)')
axes[1].set_title('Cumulative Theta-Gamma Decomposition')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

The decomposition shows the fundamental tension: theta bleeds value continuously (red bars, negative), while gamma generates occasional gains when the underlying moves (green bars, positive). The net P&L depends on whether realized moves are sufficient to offset the theta cost.

---

## What to remember


- Single-path simulations illustrate how hedging strategies perform on specific market scenarios.
- Monte Carlo simulations quantify hedging error distributions across many scenarios.
- Rebalancing frequency analysis confirms the \(\sqrt{\Delta t}\) scaling of discrete hedging error.
- The theta-gamma decomposition is the key diagnostic for understanding delta-hedged P&L.
