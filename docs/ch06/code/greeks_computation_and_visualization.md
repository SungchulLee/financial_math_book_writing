# Python: Greeks Computation and Visualization


This section provides complete Python implementations for computing and visualizing the Black–Scholes Greeks, intended as companion code for the theoretical material in Chapter 6.

---

## Black–Scholes Greeks: closed-form implementation


```python
import numpy as np
from scipy.stats import norm


def bs_greeks(S, K, tau, r, sigma, option_type='call'):
    """
    Compute all Black-Scholes Greeks for European options.

    Parameters
    ----------
    S : float or array
        Current underlying price
    K : float
        Strike price
    tau : float or array
        Time to maturity (years)
    r : float
        Risk-free rate
    sigma : float
        Volatility
    option_type : str
        'call' or 'put'

    Returns
    -------
    dict with keys: price, delta, gamma, theta, vega, rho
    """
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * tau) / (sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)

    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)
    nd1 = norm.pdf(d1)

    # Gamma and Vega are the same for calls and puts
    gamma = nd1 / (S * sigma * np.sqrt(tau))
    vega = S * np.sqrt(tau) * nd1  # per 1 unit change in sigma

    if option_type == 'call':
        price = S * Nd1 - K * np.exp(-r * tau) * Nd2
        delta = Nd1
        theta = (-S * nd1 * sigma / (2 * np.sqrt(tau))
                 - r * K * np.exp(-r * tau) * Nd2)
        rho = K * tau * np.exp(-r * tau) * Nd2
    else:
        price = K * np.exp(-r * tau) * norm.cdf(-d2) - S * norm.cdf(-d1)
        delta = Nd1 - 1
        theta = (-S * nd1 * sigma / (2 * np.sqrt(tau))
                 + r * K * np.exp(-r * tau) * norm.cdf(-d2))
        rho = -K * tau * np.exp(-r * tau) * norm.cdf(-d2)

    return {
        'price': price,
        'delta': delta,
        'gamma': gamma,
        'theta': theta,
        'vega': vega,
        'rho': rho
    }
```

---

## Greeks as functions of spot price


```python
import matplotlib.pyplot as plt

S_range = np.linspace(60, 140, 500)
K, tau, r, sigma = 100, 0.5, 0.05, 0.2

greeks_call = bs_greeks(S_range, K, tau, r, sigma, 'call')
greeks_put = bs_greeks(S_range, K, tau, r, sigma, 'put')

fig, axes = plt.subplots(2, 3, figsize=(16, 10))

# Delta
axes[0, 0].plot(S_range, greeks_call['delta'], 'b-', label='Call', linewidth=2)
axes[0, 0].plot(S_range, greeks_put['delta'], 'r-', label='Put', linewidth=2)
axes[0, 0].set_title('Delta vs Spot')
axes[0, 0].axvline(K, color='gray', linestyle='--', alpha=0.5)
axes[0, 0].legend()
axes[0, 0].grid(True, alpha=0.3)

# Gamma
axes[0, 1].plot(S_range, greeks_call['gamma'], 'g-', linewidth=2)
axes[0, 1].set_title('Gamma vs Spot')
axes[0, 1].axvline(K, color='gray', linestyle='--', alpha=0.5)
axes[0, 1].grid(True, alpha=0.3)

# Theta
axes[0, 2].plot(S_range, greeks_call['theta'] / 252, 'b-', label='Call', linewidth=2)
axes[0, 2].plot(S_range, greeks_put['theta'] / 252, 'r-', label='Put', linewidth=2)
axes[0, 2].set_title('Theta (daily) vs Spot')
axes[0, 2].axvline(K, color='gray', linestyle='--', alpha=0.5)
axes[0, 2].legend()
axes[0, 2].grid(True, alpha=0.3)

# Vega
axes[1, 0].plot(S_range, greeks_call['vega'] / 100, 'purple', linewidth=2)
axes[1, 0].set_title('Vega (per 1% vol) vs Spot')
axes[1, 0].axvline(K, color='gray', linestyle='--', alpha=0.5)
axes[1, 0].grid(True, alpha=0.3)

# Rho
axes[1, 1].plot(S_range, greeks_call['rho'] / 100, 'b-', label='Call', linewidth=2)
axes[1, 1].plot(S_range, greeks_put['rho'] / 100, 'r-', label='Put', linewidth=2)
axes[1, 1].set_title('Rho (per 1% rate) vs Spot')
axes[1, 1].axvline(K, color='gray', linestyle='--', alpha=0.5)
axes[1, 1].legend()
axes[1, 1].grid(True, alpha=0.3)

# Price
axes[1, 2].plot(S_range, greeks_call['price'], 'b-', label='Call', linewidth=2)
axes[1, 2].plot(S_range, greeks_put['price'], 'r-', label='Put', linewidth=2)
axes[1, 2].plot(S_range, np.maximum(S_range - K, 0), 'b--', alpha=0.4, label='Call intrinsic')
axes[1, 2].plot(S_range, np.maximum(K - S_range, 0), 'r--', alpha=0.4, label='Put intrinsic')
axes[1, 2].set_title('Option Price vs Spot')
axes[1, 2].legend()
axes[1, 2].grid(True, alpha=0.3)

for ax in axes.flat:
    ax.set_xlabel('Spot Price')
plt.suptitle('Black-Scholes Greeks (K=100, τ=0.5, σ=0.2, r=0.05)', fontsize=14)
plt.tight_layout()
plt.show()
```

---

## Greeks across time to maturity


```python
tau_range = np.linspace(0.01, 1.0, 300)
S, K, r, sigma = 100, 100, 0.05, 0.2  # ATM

greeks_tau = bs_greeks(S, K, tau_range, r, sigma, 'call')

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

axes[0, 0].plot(tau_range, greeks_tau['delta'], 'b-', linewidth=2)
axes[0, 0].set_title('ATM Call Delta vs τ')
axes[0, 0].set_ylabel('Delta')

axes[0, 1].plot(tau_range, greeks_tau['gamma'], 'g-', linewidth=2)
axes[0, 1].set_title('ATM Gamma vs τ (blows up as τ→0)')
axes[0, 1].set_ylabel('Gamma')

axes[1, 0].plot(tau_range, greeks_tau['theta'] / 252, 'r-', linewidth=2)
axes[1, 0].set_title('ATM Theta (daily) vs τ')
axes[1, 0].set_ylabel('Theta ($/day)')

axes[1, 1].plot(tau_range, greeks_tau['vega'], 'purple', linewidth=2)
axes[1, 1].set_title('ATM Vega vs τ')
axes[1, 1].set_ylabel('Vega')

for ax in axes.flat:
    ax.set_xlabel('Time to Maturity (years)')
    ax.grid(True, alpha=0.3)
plt.suptitle('ATM Greeks vs Time to Maturity', fontsize=14)
plt.tight_layout()
plt.show()
```

Key observations from the plots:

- **Gamma** diverges as \(\tau \to 0\) for ATM options (\(\Gamma \sim 1/\sqrt{\tau}\)).
- **Theta** becomes most negative near expiry (\(\Theta \sim -1/\sqrt{\tau}\)).
- **Vega** peaks at moderate maturities and decays as \(\sqrt{\tau}\) for short maturities.
- **Delta** approaches 0.5 for all maturities at ATM.

---

## Greeks surface: spot × maturity


```python
from mpl_toolkits.mplot3d import Axes3D

S_grid = np.linspace(70, 130, 100)
tau_grid = np.linspace(0.02, 1.0, 100)
S_mesh, tau_mesh = np.meshgrid(S_grid, tau_grid)

greeks_surf = bs_greeks(S_mesh, 100, tau_mesh, 0.05, 0.2, 'call')

fig, axes = plt.subplots(1, 3, figsize=(18, 6), subplot_kw={'projection': '3d'})

axes[0].plot_surface(S_mesh, tau_mesh, greeks_surf['delta'],
                     cmap='coolwarm', alpha=0.8)
axes[0].set_title('Delta Surface')
axes[0].set_xlabel('S')
axes[0].set_ylabel('τ')

axes[1].plot_surface(S_mesh, tau_mesh, greeks_surf['gamma'],
                     cmap='viridis', alpha=0.8)
axes[1].set_title('Gamma Surface')
axes[1].set_xlabel('S')
axes[1].set_ylabel('τ')

axes[2].plot_surface(S_mesh, tau_mesh, greeks_surf['vega'],
                     cmap='plasma', alpha=0.8)
axes[2].set_title('Vega Surface')
axes[2].set_xlabel('S')
axes[2].set_ylabel('τ')

plt.suptitle('Greek Surfaces (K=100, σ=0.2, r=0.05)', fontsize=14)
plt.tight_layout()
plt.show()
```

---

## P&L simulation: hedged vs. unhedged


```python
np.random.seed(42)

# Parameters
S0, K, T, r, sigma = 100, 100, 0.25, 0.05, 0.2
n_steps = 63  # daily for 1 quarter
dt = T / n_steps
n_paths = 5000

# Simulate GBM paths
Z = np.random.randn(n_paths, n_steps)
S = np.zeros((n_paths, n_steps + 1))
S[:, 0] = S0
for i in range(n_steps):
    S[:, i+1] = S[:, i] * np.exp((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z[:, i])

# Option payoff
payoff = np.maximum(S[:, -1] - K, 0)
option_cost = bs_greeks(S0, K, T, r, sigma, 'call')['price']

# Unhedged P&L: payoff minus premium
unhedged_pnl = np.exp(-r*T) * payoff - option_cost

# Delta-hedged P&L
hedge_pnl = np.zeros(n_paths)
for i in range(n_steps):
    tau_i = T - i * dt
    if tau_i < 1e-8:
        break
    delta_i = bs_greeks(S[:, i], K, tau_i, r, sigma, 'call')['delta']
    hedge_pnl += delta_i * (S[:, i+1] - S[:, i])

# Hedged P&L = option payoff - hedge gains - premium
hedged_pnl = np.exp(-r*T) * payoff - hedge_pnl - option_cost

fig, axes = plt.subplots(1, 2, figsize=(14, 5))
axes[0].hist(unhedged_pnl, bins=80, alpha=0.7, color='steelblue', edgecolor='black')
axes[0].axvline(0, color='red', linestyle='--')
axes[0].set_title(f'Unhedged P&L (std={unhedged_pnl.std():.2f})')
axes[0].set_xlabel('P&L ($)')

axes[1].hist(hedged_pnl, bins=80, alpha=0.7, color='darkorange', edgecolor='black')
axes[1].axvline(0, color='red', linestyle='--')
axes[1].set_title(f'Delta-Hedged P&L (std={hedged_pnl.std():.2f})')
axes[1].set_xlabel('P&L ($)')

plt.suptitle('P&L Distribution: Unhedged vs. Delta-Hedged (5000 paths)', fontsize=13)
plt.tight_layout()
plt.show()

print(f"Unhedged P&L: mean={unhedged_pnl.mean():.4f}, std={unhedged_pnl.std():.4f}")
print(f"Hedged P&L:   mean={hedged_pnl.mean():.4f}, std={hedged_pnl.std():.4f}")
```

The hedged P&L distribution should be much tighter than the unhedged distribution, with residual variance driven by discrete rebalancing and gamma effects.

---

## Hedge quantity calculator


```python
def compute_hedge(portfolio, instruments):
    """
    Compute hedge quantities to neutralize delta, gamma, and vega.

    Parameters
    ----------
    portfolio : dict with 'delta', 'gamma', 'vega'
    instruments : list of dicts, each with 'name', 'delta', 'gamma', 'vega'

    Returns
    -------
    dict of hedge quantities and residual Greeks
    """
    print("=== Current Portfolio ===")
    print(f"  Delta: {portfolio['delta']:+.2f}")
    print(f"  Gamma: {portfolio['gamma']:+.4f}")
    print(f"  Vega:  {portfolio['vega']:+.2f}")

    result = dict(portfolio)

    # Gamma hedge first (if instrument available)
    if len(instruments) >= 1 and instruments[0]['gamma'] != 0:
        inst = instruments[0]
        n = -result['gamma'] / inst['gamma']
        print(f"\nStep 1: {n:+.1f} units of {inst['name']}")
        result['delta'] += n * inst['delta']
        result['gamma'] += n * inst['gamma']
        result['vega'] += n * inst['vega']

    # Delta hedge with shares
    shares = -result['delta']
    result['delta'] = 0.0
    print(f"Step 2: {shares:+.1f} shares (delta hedge)")

    print(f"\n=== Hedged Portfolio ===")
    print(f"  Delta: {result['delta']:+.4f}")
    print(f"  Gamma: {result['gamma']:+.4f}")
    print(f"  Vega:  {result['vega']:+.2f}")

    return result


# Example usage
portfolio = {'delta': 60, 'gamma': 4.0, 'vega': 250}
instruments = [{'name': 'ATM Put', 'delta': -0.5, 'gamma': 0.05, 'vega': 3.0}]

compute_hedge(portfolio, instruments)
```

---

## What to remember


- The `bs_greeks` function provides all five first-order Greeks from closed-form Black–Scholes formulas.
- Greeks surfaces reveal how sensitivities concentrate near ATM and blow up near expiry.
- Monte Carlo P&L simulations demonstrate the variance reduction achieved by delta hedging.
- Systematic hedge quantity computation ensures consistent risk management across complex portfolios.
