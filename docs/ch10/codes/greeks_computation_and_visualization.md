# Python: Greeks Computation and Visualization


This section provides complete Python implementations for computing and visualizing the Black–Scholes Greeks, intended as companion code for the theoretical material in Chapter 6.

---

### Black–Scholes Greeks: closed-form implementation


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

### Greeks as functions of spot price


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

### Greeks across time to maturity


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

- **Gamma** diverges as $\tau \to 0$ for ATM options ($\Gamma \sim 1/\sqrt{\tau}$).
- **Theta** becomes most negative near expiry ($\Theta \sim -1/\sqrt{\tau}$).
- **Vega** peaks at moderate maturities and decays as $\sqrt{\tau}$ for short maturities.
- **Delta** approaches 0.5 for all maturities at ATM.

---

### Greeks surface: spot × maturity


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

### P&L simulation: hedged vs. unhedged


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

### Hedge quantity calculator


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

### What to remember


- The `bs_greeks` function provides all five first-order Greeks from closed-form Black–Scholes formulas.
- Greeks surfaces reveal how sensitivities concentrate near ATM and blow up near expiry.
- Monte Carlo P&L simulations demonstrate the variance reduction achieved by delta hedging.
- Systematic hedge quantity computation ensures consistent risk management across complex portfolios.

---

## Exercises

**Exercise 1.** Modify the `bs_greeks` function to include the higher-order Greeks: charm, vanna, and volga. Test your implementation by computing these Greeks for an ATM call with $S = K = 100$, $\tau = 0.5$, $r = 0.05$, $\sigma = 0.20$, and verify that vanna agrees with the formula $\text{Vanna} = -N'(d_1)d_2/\sigma$.

??? success "Solution to Exercise 1"

    The higher-order Greeks for a European call under Black--Scholes are defined as follows.

    **Charm** (delta decay, $\partial \Delta / \partial \tau$):

    $$
    \text{Charm} = -N'(d_1)\!\left(\frac{2(r+\tfrac12\sigma^2)\tau - d_2\,\sigma\sqrt{\tau}}{2\tau\,\sigma\sqrt{\tau}}\right)
    $$

    For a put, the sign of the first term flips.

    **Vanna** ($\partial \Delta / \partial \sigma = \partial \text{Vega} / \partial S$):

    $$
    \text{Vanna} = -N'(d_1)\,\frac{d_2}{\sigma}
    $$

    **Volga** (vega convexity, $\partial^2 V / \partial \sigma^2$):

    $$
    \text{Volga} = \text{Vega} \cdot \frac{d_1\,d_2}{\sigma}
    $$

    The extended function:

    ```python
    def bs_greeks_extended(S, K, tau, r, sigma, option_type='call'):
        d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * tau) / (sigma * np.sqrt(tau))
        d2 = d1 - sigma * np.sqrt(tau)
        nd1 = norm.pdf(d1)

        # Standard Greeks (as before)
        greeks = bs_greeks(S, K, tau, r, sigma, option_type)

        # Vanna
        vanna = -nd1 * d2 / sigma

        # Volga
        vega = S * np.sqrt(tau) * nd1
        volga = vega * d1 * d2 / sigma

        # Charm
        charm_common = nd1 * (2 * (r + 0.5 * sigma**2) * tau
                              - d2 * sigma * np.sqrt(tau)) / (
                              2 * tau * sigma * np.sqrt(tau))
        if option_type == 'call':
            charm = -charm_common
        else:
            charm = -charm_common  # same formula; put-call parity gives identical charm

        greeks.update({'charm': charm, 'vanna': vanna, 'volga': volga})
        return greeks
    ```

    **Verification** at $S = K = 100$, $\tau = 0.5$, $r = 0.05$, $\sigma = 0.20$:

    ```python
    g = bs_greeks_extended(100, 100, 0.5, 0.05, 0.2, 'call')
    d1 = (np.log(1) + (0.05 + 0.02) * 0.5) / (0.2 * np.sqrt(0.5))
    d2 = d1 - 0.2 * np.sqrt(0.5)
    vanna_check = -norm.pdf(d1) * d2 / 0.2
    print(f"Vanna from function: {g['vanna']:.6f}")
    print(f"Vanna from formula:  {vanna_check:.6f}")
    ```

    Both values will agree to machine precision.

---

**Exercise 2.** Using the Greeks surface code, generate a contour plot (instead of a 3D surface) of gamma over the $(S, \tau)$ plane. Identify the region where gamma exceeds $0.05$ and shade it. How does this region change if volatility increases from $0.20$ to $0.40$?

??? success "Solution to Exercise 2"

    Replace the 3D surface with a contour plot and shade the region where $\Gamma > 0.05$:

    ```python
    S_grid = np.linspace(70, 130, 200)
    tau_grid = np.linspace(0.02, 1.0, 200)
    S_mesh, tau_mesh = np.meshgrid(S_grid, tau_grid)

    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    for ax, vol, title in zip(axes, [0.20, 0.40], ['σ = 0.20', 'σ = 0.40']):
        greeks_s = bs_greeks(S_mesh, 100, tau_mesh, 0.05, vol, 'call')
        gamma_vals = greeks_s['gamma']

        cs = ax.contourf(S_mesh, tau_mesh, gamma_vals, levels=20, cmap='viridis')
        ax.contour(S_mesh, tau_mesh, gamma_vals, levels=[0.05],
                   colors='red', linewidths=2)
        ax.contourf(S_mesh, tau_mesh, gamma_vals, levels=[0.05, gamma_vals.max()],
                    colors=['red'], alpha=0.2)
        plt.colorbar(cs, ax=ax)
        ax.set_xlabel('Spot Price')
        ax.set_ylabel('Time to Maturity')
        ax.set_title(f'Gamma Contour ({title})')

    plt.tight_layout()
    plt.show()
    ```

    **Observations:** When $\sigma$ increases from $0.20$ to $0.40$, the gamma surface flattens. The high-gamma region ($\Gamma > 0.05$) shrinks because the peak gamma near ATM at short maturities is given by

    $$
    \Gamma_{\text{ATM}} = \frac{N'(0)}{S\,\sigma\sqrt{\tau}} = \frac{1}{S\,\sigma\sqrt{2\pi\tau}}
    $$

    Doubling $\sigma$ halves the peak gamma for each $\tau$, so the $\Gamma > 0.05$ region requires shorter maturities and stays closer to ATM. Effectively the red-shaded zone contracts toward $(S, \tau) = (K, 0)$.

---

**Exercise 3.** The P&L simulation compares unhedged and delta-hedged portfolios. Extend the simulation to include a **delta-gamma hedged** portfolio that also trades a second option to neutralize gamma at each step. Compare the three strategies' P&L distributions.

??? success "Solution to Exercise 3"

    To implement delta-gamma hedging, at each step we trade an additional option (say an ATM put with strike $K_2 = 100$ and a different maturity $T_2 = 1.0$) to neutralize gamma before delta-hedging with shares.

    ```python
    np.random.seed(42)
    S0, K, T, r, sigma = 100, 100, 0.25, 0.05, 0.2
    K2, T2 = 100, 1.0  # second option for gamma hedging
    n_steps = 63
    dt = T / n_steps
    n_paths = 5000

    Z = np.random.randn(n_paths, n_steps)
    S = np.zeros((n_paths, n_steps + 1))
    S[:, 0] = S0
    for i in range(n_steps):
        S[:, i+1] = S[:, i] * np.exp((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z[:, i])

    payoff = np.maximum(S[:, -1] - K, 0)
    option_cost = bs_greeks(S0, K, T, r, sigma, 'call')['price']

    # Strategy 1: unhedged
    unhedged_pnl = np.exp(-r*T) * payoff - option_cost

    # Strategy 2: delta-hedged
    delta_gains = np.zeros(n_paths)
    for i in range(n_steps):
        tau_i = T - i * dt
        if tau_i < 1e-8:
            break
        delta_i = bs_greeks(S[:, i], K, tau_i, r, sigma, 'call')['delta']
        delta_gains += delta_i * (S[:, i+1] - S[:, i])
    delta_hedged_pnl = np.exp(-r*T) * payoff - delta_gains - option_cost

    # Strategy 3: delta-gamma hedged
    dg_gains = np.zeros(n_paths)
    for i in range(n_steps):
        tau_i = T - i * dt
        tau2_i = T2 - i * dt
        if tau_i < 1e-8:
            break
        g1 = bs_greeks(S[:, i], K, tau_i, r, sigma, 'call')
        g2 = bs_greeks(S[:, i], K2, tau2_i, r, sigma, 'call')

        # Gamma-neutralize: n2 units of option 2
        n2 = -g1['gamma'] / g2['gamma']
        # Delta-neutralize: shares = -(delta1 + n2 * delta2)
        net_delta = g1['delta'] + n2 * g2['delta']

        dS = S[:, i+1] - S[:, i]
        # P&L from option 2 position
        if tau2_i - dt > 1e-8:
            V2_now = bs_greeks(S[:, i], K2, tau2_i, r, sigma, 'call')['price']
            V2_next = bs_greeks(S[:, i+1], K2, tau2_i - dt, r, sigma, 'call')['price']
            dg_gains += net_delta * dS + n2 * (V2_next - V2_now)
        else:
            dg_gains += net_delta * dS

    dg_hedged_pnl = np.exp(-r*T) * payoff - dg_gains - option_cost
    ```

    Plotting the three distributions shows that delta-gamma hedging further reduces the P&L standard deviation beyond delta-only hedging, because the dominant source of discrete hedging error (the gamma term $\frac{1}{2}\Gamma(\Delta S)^2$) is neutralized at each step.

---

**Exercise 4.** The hedge quantity calculator uses a sequential approach: gamma-hedge first, then delta-hedge. Modify the code to perform **joint gamma-vega hedging** using two option instruments, solving the $2 \times 2$ linear system, and then delta-hedging with shares.

??? success "Solution to Exercise 4"

    With two option instruments available, we solve for positions $n_1, n_2$ that simultaneously zero gamma and vega:

    $$
    \begin{pmatrix} \Gamma_1 & \Gamma_2 \\ \mathcal{V}_1 & \mathcal{V}_2 \end{pmatrix}
    \begin{pmatrix} n_1 \\ n_2 \end{pmatrix}
    = -\begin{pmatrix} \Gamma_{\text{port}} \\ \mathcal{V}_{\text{port}} \end{pmatrix}
    $$

    Then delta-hedge with shares: $n_{\text{shares}} = -(\Delta_{\text{port}} + n_1 \Delta_1 + n_2 \Delta_2)$.

    ```python
    def compute_hedge_joint(portfolio, instruments):
        """
        Joint gamma-vega hedge using two options, then delta-hedge with shares.
        """
        assert len(instruments) >= 2, "Need at least two option instruments"
        inst1, inst2 = instruments[0], instruments[1]

        # Build 2x2 system
        A = np.array([
            [inst1['gamma'], inst2['gamma']],
            [inst1['vega'],  inst2['vega']]
        ])
        b = -np.array([portfolio['gamma'], portfolio['vega']])

        n = np.linalg.solve(A, b)
        n1, n2 = n

        print(f"Gamma-Vega hedge: {n1:+.2f} units of {inst1['name']}, "
              f"{n2:+.2f} units of {inst2['name']}")

        result = {
            'delta': portfolio['delta'] + n1 * inst1['delta'] + n2 * inst2['delta'],
            'gamma': portfolio['gamma'] + n1 * inst1['gamma'] + n2 * inst2['gamma'],
            'vega':  portfolio['vega']  + n1 * inst1['vega']  + n2 * inst2['vega']
        }

        shares = -result['delta']
        result['delta'] = 0.0
        print(f"Delta hedge: {shares:+.2f} shares")

        print(f"\nResidual Greeks: Delta={result['delta']:+.6f}, "
              f"Gamma={result['gamma']:+.6f}, Vega={result['vega']:+.4f}")

        return result

    # Example
    portfolio = {'delta': 60, 'gamma': 4.0, 'vega': 250}
    instruments = [
        {'name': 'ATM Put',  'delta': -0.5, 'gamma': 0.05, 'vega': 3.0},
        {'name': 'OTM Call', 'delta':  0.3, 'gamma': 0.03, 'vega': 2.5}
    ]
    compute_hedge_joint(portfolio, instruments)
    ```

    The $2 \times 2$ solve requires the matrix $A$ to be non-singular, i.e., the two instruments must have linearly independent $(\Gamma, \mathcal{V})$ profiles. This fails if both instruments have the same gamma-to-vega ratio.

---

**Exercise 5.** Run the P&L simulation with different random seeds and compute the mean and standard deviation of the hedged P&L standard deviation across 50 random seeds. How stable is the estimate of hedging quality? Does the central limit theorem prediction $\text{Std}(\text{HE}) \sim \sqrt{\Delta t}$ hold empirically?

??? success "Solution to Exercise 5"

    We run 50 independent experiments, each with a different random seed, and collect the standard deviation of the hedged P&L:

    ```python
    S0, K, T, r, sigma = 100, 100, 0.25, 0.05, 0.2
    n_steps = 63
    dt = T / n_steps
    n_paths = 5000
    n_seeds = 50

    std_list = []
    for seed in range(n_seeds):
        np.random.seed(seed)
        Z = np.random.randn(n_paths, n_steps)
        S = np.zeros((n_paths, n_steps + 1))
        S[:, 0] = S0
        for i in range(n_steps):
            S[:, i+1] = S[:, i] * np.exp((r - 0.5*sigma**2)*dt
                                           + sigma*np.sqrt(dt)*Z[:, i])

        payoff = np.maximum(S[:, -1] - K, 0)
        option_cost = bs_greeks(S0, K, T, r, sigma, 'call')['price']

        hedge_pnl = np.zeros(n_paths)
        for i in range(n_steps):
            tau_i = T - i * dt
            if tau_i < 1e-8:
                break
            delta_i = bs_greeks(S[:, i], K, tau_i, r, sigma, 'call')['delta']
            hedge_pnl += delta_i * (S[:, i+1] - S[:, i])

        hedged_pnl = np.exp(-r*T) * payoff - hedge_pnl - option_cost
        std_list.append(hedged_pnl.std())

    std_array = np.array(std_list)
    print(f"Mean of hedging-error std: {std_array.mean():.4f}")
    print(f"Std of hedging-error std:  {std_array.std():.4f}")
    print(f"Coefficient of variation:  {std_array.std() / std_array.mean():.4f}")
    ```

    The estimate is quite stable: the coefficient of variation across seeds is typically below 2--3%, because with $n_{\text{paths}} = 5000$ the Monte Carlo sampling error on the standard deviation is $\mathcal{O}(1/\sqrt{2 n_{\text{paths}}})$.

    For the $\sqrt{\Delta t}$ prediction, run the same experiment for different step counts (e.g., $n = 16, 32, 63, 126, 252$) and regress $\log(\text{Std})$ on $\log(\Delta t)$. The slope should be approximately $0.5$:

    $$
    \text{Std}(\text{HE}) \propto \sqrt{\Delta t}
    $$

    This follows from the fact that each discrete hedging error at step $i$ is approximately $\frac{1}{2}\Gamma_i S_i^2 \sigma^2[(\Delta W_i)^2 - \Delta t]$, and these increments are independent with variance $\mathcal{O}(\Delta t^2)$, so summing $T / \Delta t$ terms gives total variance $\mathcal{O}(\Delta t)$.

---

**Exercise 6.** Add a theta term to the P&L decomposition by computing $\Theta_i \cdot \Delta t$ at each step. Verify that the sum $\sum_i (\Theta_i \cdot \Delta t + \frac{1}{2}\Gamma_i(\Delta S_i)^2)$ approximately equals the total hedged P&L. For what fraction of steps does the gamma P&L exceed the theta cost?

??? success "Solution to Exercise 6"

    At each step $i$ with remaining time $\tau_i$, we compute the theta and gamma contributions:

    $$
    \text{Theta P\&L}_i = \Theta_i \cdot \Delta t, \qquad \text{Gamma P\&L}_i = \frac{1}{2}\,\Gamma_i\,(\Delta S_i)^2
    $$

    ```python
    np.random.seed(42)
    S0, K, T, r, sigma = 100, 100, 0.25, 0.05, 0.2
    n_steps = 63
    dt = T / n_steps

    Z = np.random.randn(n_steps)
    S_path = np.zeros(n_steps + 1)
    S_path[0] = S0
    for i in range(n_steps):
        S_path[i+1] = S_path[i] * np.exp((r - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*Z[i])

    theta_terms = np.zeros(n_steps)
    gamma_terms = np.zeros(n_steps)
    actual_hedge_pnl = np.zeros(n_steps)

    for i in range(n_steps):
        tau_i = T - i * dt
        if tau_i < 1e-8:
            break
        g = bs_greeks(S_path[i], K, tau_i, r, sigma, 'call')
        dS = S_path[i+1] - S_path[i]

        theta_terms[i] = g['theta'] * dt
        gamma_terms[i] = 0.5 * g['gamma'] * dS**2

        # Actual hedged P&L: option value change minus delta hedge gain
        V_now = g['price']
        V_next = bs_greeks(S_path[i+1], K, tau_i - dt, r, sigma, 'call')['price']
        actual_hedge_pnl[i] = (V_next - V_now) - g['delta'] * dS

    approx_total = np.sum(theta_terms + gamma_terms)
    actual_total = np.sum(actual_hedge_pnl)

    print(f"Sum of (Theta*dt + 0.5*Gamma*dS^2): {approx_total:.6f}")
    print(f"Actual total hedged P&L:             {actual_total:.6f}")
    print(f"Approximation error:                 {abs(approx_total - actual_total):.6f}")

    # Fraction of steps where gamma P&L exceeds theta cost
    gamma_exceeds = np.sum(gamma_terms > np.abs(theta_terms))
    print(f"\nFraction of steps where gamma P&L > |theta|: "
          f"{gamma_exceeds}/{n_steps} = {gamma_exceeds / n_steps:.2%}")
    ```

    The approximation agrees closely with the actual hedged P&L because the Taylor expansion of the option value change gives

    $$
    dV \approx \Delta\,dS + \frac{1}{2}\,\Gamma\,(dS)^2 + \Theta\,dt
    $$

    and the delta term is exactly offset by the hedge. The residual higher-order terms ($\mathcal{O}(dS^3)$ and cross-terms) are negligible for small $\Delta t$.

    Typically, gamma P&L exceeds the theta cost in roughly 30--40% of steps. This is consistent with the fact that $(\Delta W)^2 > \Delta t$ occurs when $|Z| > 1$, which happens with probability $\approx 31.7\%$ under a standard normal distribution.
