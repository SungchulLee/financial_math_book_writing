# Python: P&L Simulation under Hedging Strategies


This section implements a comprehensive P&L simulator that compares hedging strategies under realistic conditions including gamma and vega effects.

---

### Simulation framework


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

### Single-path P&L comparison


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

### Multi-path Monte Carlo with hedging frequency analysis


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

This demonstrates that more frequent rebalancing reduces hedging error variance, but with diminishing returns (the error scales as $\sqrt{\Delta t}$).

---

### P&L decomposition: theta vs. gamma


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

### What to remember


- Single-path simulations illustrate how hedging strategies perform on specific market scenarios.
- Monte Carlo simulations quantify hedging error distributions across many scenarios.
- Rebalancing frequency analysis confirms the $\sqrt{\Delta t}$ scaling of discrete hedging error.
- The theta-gamma decomposition is the key diagnostic for understanding delta-hedged P&L.

---

## Exercises

**Exercise 1.** Modify the single-path simulation to include a **proportional transaction cost** of $\kappa = 0.001$ (10 bps) per dollar traded at each rebalancing. Recompute the dynamic hedge P&L with transaction costs included. How much do transaction costs erode the hedging performance?

??? success "Solution to Exercise 1"

    At each rebalancing step, the transaction cost is proportional to the dollar value of shares traded:

    $$
    \text{TC}_i = \kappa \cdot S_{i+1} \cdot |\Delta_{i+1} - \Delta_i| \cdot N_{\text{options}}
    $$

    where $\kappa = 0.001$ and $\Delta_i$ is the Black--Scholes delta used at step $i$.

    ```python
    np.random.seed(123)

    S0, K, T, r, sigma = 100, 100, 0.25, 0.05, 0.20
    num_options = 100
    n_steps = 63
    dt = T / n_steps
    kappa = 0.001

    Z = np.random.randn(n_steps)
    S_path = np.zeros(n_steps + 1)
    S_path[0] = S0
    for i in range(n_steps):
        S_path[i+1] = S_path[i] * np.exp((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z[i])

    pnl_dynamic = np.zeros(n_steps + 1)
    pnl_dynamic_tc = np.zeros(n_steps + 1)
    total_tc = 0.0

    prev_delta = bs_delta(S0, K, T, r, sigma)
    dyn_shares = -num_options * prev_delta

    for i in range(n_steps):
        tau_i = T - i * dt
        dS = S_path[i+1] - S_path[i]
        V_now = num_options * bs_price(S_path[i], K, tau_i, r, sigma)
        V_next = num_options * bs_price(S_path[i+1], K, tau_i - dt, r, sigma)
        dV = V_next - V_now

        pnl_dynamic[i+1] = pnl_dynamic[i] + dV + dyn_shares * dS
        pnl_dynamic_tc[i+1] = pnl_dynamic_tc[i] + dV + dyn_shares * dS

        if tau_i - dt > 1e-8:
            new_delta = bs_delta(S_path[i+1], K, tau_i - dt, r, sigma)
            trade_cost = kappa * S_path[i+1] * abs(new_delta - prev_delta) * num_options
            total_tc += trade_cost
            pnl_dynamic_tc[i+1] -= trade_cost
            dyn_shares = -num_options * new_delta
            prev_delta = new_delta

    print(f"Dynamic hedge P&L (no TC):   {pnl_dynamic[-1]:.4f}")
    print(f"Dynamic hedge P&L (with TC): {pnl_dynamic_tc[-1]:.4f}")
    print(f"Total transaction costs:     {total_tc:.4f}")
    ```

    With $\kappa = 0.001$, transaction costs typically consume a meaningful fraction of the initial option premium. The erosion increases with rebalancing frequency, creating the classical trade-off between hedging accuracy and transaction costs.

---

**Exercise 2.** In the multi-path Monte Carlo simulation, compute the **skewness** and **kurtosis** of the hedged P&L distribution for daily rebalancing. Is the distribution approximately Gaussian, as predicted by the CLT? At what rebalancing frequency does the distribution become noticeably non-Gaussian?

??? success "Solution to Exercise 2"

    After computing the hedged P&L distribution for each frequency, add:

    ```python
    from scipy.stats import skew, kurtosis

    np.random.seed(42)
    S0, K, T, r, sigma = 100, 100, 0.5, 0.05, 0.20
    n_paths = 10000
    n_steps_sim = 252

    for n_rebal in [252, 52, 12, 4]:
        dt_sim = T / n_steps_sim
        rebal_interval = max(n_steps_sim // n_rebal, 1)

        Z = np.random.randn(n_paths, n_steps_sim)
        S = np.zeros((n_paths, n_steps_sim + 1))
        S[:, 0] = S0
        for i in range(n_steps_sim):
            S[:, i+1] = S[:, i] * np.exp((r - 0.5*sigma**2)*dt_sim
                                           + sigma*np.sqrt(dt_sim)*Z[:, i])

        hedge_gains = np.zeros(n_paths)
        current_delta = bs_delta(S0, K, T, r, sigma) * np.ones(n_paths)
        for i in range(n_steps_sim):
            hedge_gains += current_delta * (S[:, i+1] - S[:, i])
            if (i + 1) % rebal_interval == 0:
                tau_i = T - (i + 1) * dt_sim
                if tau_i > 1e-8:
                    current_delta = bs_delta(S[:, i+1], K, tau_i, r, sigma)

        payoff = np.maximum(S[:, -1] - K, 0)
        hedged_pnl = np.exp(-r*T) * payoff - hedge_gains - bs_price(S0, K, T, r, sigma)

        sk = skew(hedged_pnl)
        ku = kurtosis(hedged_pnl)  # excess kurtosis
        print(f"Rebalancing {n_rebal:>3d}x: skew={sk:+.3f}, excess kurtosis={ku:.3f}")
    ```

    For daily rebalancing, the skewness is close to zero and the excess kurtosis is small (typically below 0.5), consistent with the CLT prediction. At quarterly rebalancing (4 times), the distribution becomes visibly right-skewed and leptokurtic, since each rebalancing interval is long enough that the individual hedging errors are far from Gaussian. The transition typically becomes noticeable at monthly or less frequent rebalancing.

---

**Exercise 3.** Extend the rebalancing frequency analysis to include a **non-uniform** rebalancing schedule that rebalances more frequently near expiry (when gamma is large). Compare the hedging error standard deviation with uniform daily rebalancing using the same total number of rebalancing dates.

??? success "Solution to Exercise 3"

    A natural non-uniform schedule concentrates more rebalancing dates near expiry, where gamma is largest. One approach is to space rebalancing times according to $t_k = T(k/N)^2$ for $k = 0, 1, \ldots, N$, so intervals shrink near $T$:

    ```python
    np.random.seed(42)
    S0, K, T, r, sigma = 100, 100, 0.5, 0.05, 0.20
    n_paths = 10000
    n_steps_fine = 252
    dt_fine = T / n_steps_fine
    N_rebal = 63  # total number of rebalancing dates

    # Non-uniform schedule: t_k = T * (k/N)^2
    rebal_times_nonuniform = T * (np.arange(N_rebal + 1) / N_rebal)**2
    rebal_indices_nonuniform = np.unique(
        np.round(rebal_times_nonuniform / dt_fine).astype(int)
    )
    rebal_indices_nonuniform = rebal_indices_nonuniform[
        rebal_indices_nonuniform < n_steps_fine
    ]

    # Uniform schedule with same count
    rebal_indices_uniform = np.round(
        np.linspace(0, n_steps_fine - 1, N_rebal)
    ).astype(int)

    Z = np.random.randn(n_paths, n_steps_fine)
    S = np.zeros((n_paths, n_steps_fine + 1))
    S[:, 0] = S0
    for i in range(n_steps_fine):
        S[:, i+1] = S[:, i] * np.exp((r - 0.5*sigma**2)*dt_fine
                                       + sigma*np.sqrt(dt_fine)*Z[:, i])

    def compute_hedged_pnl(S, rebal_set):
        hedge_gains = np.zeros(n_paths)
        current_delta = bs_delta(S0, K, T, r, sigma) * np.ones(n_paths)
        for i in range(n_steps_fine):
            hedge_gains += current_delta * (S[:, i+1] - S[:, i])
            if i in rebal_set:
                tau_i = T - (i + 1) * dt_fine
                if tau_i > 1e-8:
                    current_delta = bs_delta(S[:, i+1], K, tau_i, r, sigma)
        payoff = np.maximum(S[:, -1] - K, 0)
        return np.exp(-r*T) * payoff - hedge_gains - bs_price(S0, K, T, r, sigma)

    pnl_uniform = compute_hedged_pnl(S, set(rebal_indices_uniform))
    pnl_nonuniform = compute_hedged_pnl(S, set(rebal_indices_nonuniform))

    print(f"Uniform   rebalancing std: {pnl_uniform.std():.4f}")
    print(f"Nonuniform rebalancing std: {pnl_nonuniform.std():.4f}")
    ```

    The non-uniform schedule typically achieves a lower hedging error standard deviation than the uniform schedule with the same total number of trades, because it allocates more rebalancing events to the high-gamma period near expiry where discrete hedging errors are largest.

---

**Exercise 4.** The theta-gamma decomposition shows that daily hedged P&L is approximately $\Theta_i \cdot \Delta t + \frac{1}{2}\Gamma_i(\Delta S_i)^2$. For the simulated path, compute the correlation between the daily gamma P&L and the squared daily return $(R_i)^2$. Is the correlation close to 1, as predicted by theory?

??? success "Solution to Exercise 4"

    The daily gamma P&L is $\frac{1}{2}\Gamma_i (\Delta S_i)^2$, and the squared daily return is $R_i^2 = (\Delta S_i / S_i)^2$. Since $\Gamma_i$ and $S_i$ vary slowly relative to $(\Delta S_i)^2$, we expect high correlation:

    ```python
    np.random.seed(7)
    S0, K, T, r, sigma = 100, 100, 0.1, 0.05, 0.20
    n_steps = 25
    dt = T / n_steps

    Z = np.random.randn(n_steps)
    S_path = np.zeros(n_steps + 1)
    S_path[0] = S0
    for i in range(n_steps):
        S_path[i+1] = S_path[i] * np.exp((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z[i])

    gamma_pnl = np.zeros(n_steps)
    squared_returns = np.zeros(n_steps)

    for i in range(n_steps):
        tau_i = T - i * dt
        S_i = S_path[i]
        dS = S_path[i+1] - S_path[i]

        gamma_i = bs_gamma(S_i, K, tau_i, r, sigma)
        gamma_pnl[i] = 0.5 * gamma_i * dS**2
        squared_returns[i] = (dS / S_i)**2

    corr = np.corrcoef(gamma_pnl, squared_returns)[0, 1]
    print(f"Correlation between gamma P&L and R^2: {corr:.6f}")
    ```

    The correlation is very close to 1 (typically $> 0.99$). This is because

    $$
    \frac{1}{2}\Gamma_i (\Delta S_i)^2 = \frac{1}{2}\Gamma_i S_i^2 \cdot R_i^2
    $$

    and the factor $\frac{1}{2}\Gamma_i S_i^2$ varies slowly across steps (it changes smoothly with $S$ and $\tau$), so it acts approximately as a positive constant multiplier that preserves the rank ordering of $R_i^2$.

---

**Exercise 5.** Simulate the hedged P&L under a **misspecified volatility** scenario: the true dynamics use $\sigma = 0.25$ while the hedger computes deltas using $\hat{\sigma} = 0.20$. Plot the distribution of hedged P&L and compute its mean. Verify that the mean hedging error is approximately $\frac{1}{2}\bar{\Gamma}S^2(\sigma^2 - \hat{\sigma}^2)T$.

??? success "Solution to Exercise 5"

    The hedger uses $\hat{\sigma} = 0.20$ for delta computation while the stock evolves with $\sigma_{\text{true}} = 0.25$:

    ```python
    np.random.seed(42)
    S0, K, T, r = 100, 100, 0.5, 0.05
    sigma_true = 0.25
    sigma_hedge = 0.20
    n_steps = 126
    dt = T / n_steps
    n_paths = 10000

    Z = np.random.randn(n_paths, n_steps)
    S = np.zeros((n_paths, n_steps + 1))
    S[:, 0] = S0
    for i in range(n_steps):
        S[:, i+1] = S[:, i] * np.exp((r - 0.5*sigma_true**2)*dt
                                       + sigma_true*np.sqrt(dt)*Z[:, i])

    # Hedger uses wrong vol for delta
    hedge_gains = np.zeros(n_paths)
    for i in range(n_steps):
        tau_i = T - i * dt
        if tau_i < 1e-8:
            break
        delta_i = bs_delta(S[:, i], K, tau_i, r, sigma_hedge)
        hedge_gains += delta_i * (S[:, i+1] - S[:, i])

    payoff = np.maximum(S[:, -1] - K, 0)
    # Option sold at implied vol price
    option_cost = bs_price(S0, K, T, r, sigma_hedge)
    hedged_pnl = np.exp(-r*T) * payoff - hedge_gains - option_cost

    print(f"Mean hedged P&L: {hedged_pnl.mean():.4f}")
    print(f"Std hedged P&L:  {hedged_pnl.std():.4f}")

    # Theoretical prediction
    gamma_atm = norm.pdf(0) / (S0 * sigma_hedge * np.sqrt(T / 2))
    predicted_mean = 0.5 * gamma_atm * S0**2 * (sigma_true**2 - sigma_hedge**2) * T
    print(f"Predicted mean error (approx): {predicted_mean:.4f}")
    ```

    The mean hedged P&L is systematically positive (the hedger sold the option too cheaply), and the magnitude approximately matches

    $$
    \frac{1}{2}\bar{\Gamma}\,S^2\,(\sigma^2 - \hat{\sigma}^2)\,T
    $$

    This is the classic result: selling options at implied vol $\hat{\sigma}$ and hedging with that vol, when realized vol is $\sigma > \hat{\sigma}$, produces a systematic loss to the seller (gain to the buyer). The sign of the mean error equals the sign of $\sigma^2 - \hat{\sigma}^2$.

---

**Exercise 6.** Implement a **Whalley-Wilmott no-trade band** strategy: only rebalance when the current delta deviates from the target delta by more than $h = (3\lambda/(2\Gamma))^{1/3}$ with $\lambda = 0.001$. Compare the total cost (hedging error variance + transaction costs) with the fixed-frequency strategies from the multi-path simulation.

??? success "Solution to Exercise 6"

    The Whalley--Wilmott band around the target delta is $\pm h$ where

    $$
    h = \left(\frac{3\lambda}{2\Gamma}\right)^{1/3}
    $$

    with $\lambda$ the proportional transaction cost. Rebalancing occurs only when $|\Delta_{\text{current}} - \Delta_{\text{target}}| > h$.

    ```python
    np.random.seed(42)
    S0, K, T, r, sigma = 100, 100, 0.5, 0.05, 0.20
    n_paths = 10000
    n_steps = 126
    dt = T / n_steps
    lam = 0.001  # transaction cost rate

    Z = np.random.randn(n_paths, n_steps)
    S = np.zeros((n_paths, n_steps + 1))
    S[:, 0] = S0
    for i in range(n_steps):
        S[:, i+1] = S[:, i] * np.exp((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z[:, i])

    # Whalley-Wilmott strategy
    current_delta = bs_delta(S0, K, T, r, sigma) * np.ones(n_paths)
    ww_gains = np.zeros(n_paths)
    ww_tc = np.zeros(n_paths)
    n_trades_ww = np.zeros(n_paths)

    for i in range(n_steps):
        ww_gains += current_delta * (S[:, i+1] - S[:, i])
        tau_i = T - (i + 1) * dt
        if tau_i > 1e-8:
            target_delta = bs_delta(S[:, i+1], K, tau_i, r, sigma)
            gamma_i = bs_gamma(S[:, i+1], K, tau_i, r, sigma)

            # Whalley-Wilmott band
            h = (3 * lam / (2 * np.maximum(gamma_i, 1e-10)))**(1.0/3.0)

            rebalance_mask = np.abs(current_delta - target_delta) > h
            trade_size = np.where(rebalance_mask, np.abs(target_delta - current_delta), 0)
            ww_tc += lam * S[:, i+1] * trade_size
            current_delta = np.where(rebalance_mask, target_delta, current_delta)
            n_trades_ww += rebalance_mask

    payoff = np.maximum(S[:, -1] - K, 0)
    option_cost = bs_price(S0, K, T, r, sigma)
    ww_pnl = np.exp(-r*T) * payoff - ww_gains - option_cost - ww_tc

    # Daily rebalancing with same transaction costs for comparison
    current_delta_daily = bs_delta(S0, K, T, r, sigma) * np.ones(n_paths)
    daily_gains = np.zeros(n_paths)
    daily_tc = np.zeros(n_paths)

    for i in range(n_steps):
        daily_gains += current_delta_daily * (S[:, i+1] - S[:, i])
        tau_i = T - (i + 1) * dt
        if tau_i > 1e-8:
            new_delta = bs_delta(S[:, i+1], K, tau_i, r, sigma)
            daily_tc += lam * S[:, i+1] * np.abs(new_delta - current_delta_daily)
            current_delta_daily = new_delta

    daily_pnl = np.exp(-r*T) * payoff - daily_gains - option_cost - daily_tc

    print(f"Daily rebalancing:  std={daily_pnl.std():.4f}, "
          f"mean TC={daily_tc.mean():.4f}")
    print(f"Whalley-Wilmott:    std={ww_pnl.std():.4f}, "
          f"mean TC={ww_tc.mean():.4f}, "
          f"mean trades={n_trades_ww.mean():.1f}/{n_steps}")
    ```

    The Whalley--Wilmott strategy achieves a favorable trade-off: it incurs substantially lower transaction costs than daily rebalancing while only slightly increasing the hedging error variance. The no-trade band is adaptive -- it widens when gamma is small (far from ATM or long maturity) and narrows when gamma is large (near ATM close to expiry), which is exactly where hedging accuracy matters most. The total cost (variance plus expected transaction costs) is typically lower for the Whalley--Wilmott strategy than for any fixed-frequency strategy.
