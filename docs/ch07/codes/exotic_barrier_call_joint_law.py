"""
Barrier Option Pricing via the Joint Law of (W_t, M_t)

This script prices up-and-out call options using three methods:
1. Closed-form via the image method (reflection principle)
2. Numerical integration of the joint density f_{M_T, W_T}
3. Monte Carlo simulation with barrier monitoring

The joint density of the running maximum M_T and terminal value W_T
of standard Brownian motion is:

    f_{M_T, W_T}(m, w) = 2(2m - w) / (T * sqrt(2*pi*T)) * exp(-(2m - w)^2 / (2T))

for m >= 0 and w <= m.
"""

import numpy as np
from scipy.stats import norm
from scipy.integrate import dblquad
import matplotlib.pyplot as plt


# =============================================================================
# 1. Black-Scholes Vanilla Call Price
# =============================================================================

def bs_call_price(S, K, T, r, sigma):
    """Standard Black-Scholes European call price."""
    if T <= 0:
        return max(S - K, 0.0)
    d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)


# =============================================================================
# 2. Closed-Form: Up-and-Out Call via Image Method
# =============================================================================

def up_and_out_call_closed_form(S0, K, H, T, r, sigma):
    """
    Closed-form price of an up-and-out call option.

    C_UO = C_BS(S0, K) - (S0/H)^(2*lambda - 2) * C_BS(H^2/S0, K)

    where lambda = r / sigma^2 + 1/2.

    Parameters
    ----------
    S0 : float – Initial stock price
    K  : float – Strike price
    H  : float – Upper barrier (H > S0)
    T  : float – Time to maturity (years)
    r  : float – Risk-free rate
    sigma : float – Volatility

    Returns
    -------
    float – Up-and-out call price
    """
    if S0 >= H:
        return 0.0  # Already knocked out

    lam = r / sigma**2 + 0.5
    C_vanilla = bs_call_price(S0, K, T, r, sigma)
    C_image = bs_call_price(H**2 / S0, K, T, r, sigma)
    C_uo = C_vanilla - (S0 / H)**(2 * lam - 2) * C_image

    return max(C_uo, 0.0)


# =============================================================================
# 3. Joint Density of (M_T, W_T) for Standard Brownian Motion
# =============================================================================

def joint_density_MW(m, w, T):
    """
    Joint density f_{M_T, W_T}(m, w) for standard Brownian motion.

    f(m, w) = 2(2m - w) / (T * sqrt(2*pi*T)) * exp(-(2m - w)^2 / (2T))

    Valid for m >= 0 and w <= m.

    Parameters
    ----------
    m : float – Running maximum value
    w : float – Terminal Brownian motion value
    T : float – Time horizon

    Returns
    -------
    float – Joint density value
    """
    if m < 0 or w > m:
        return 0.0
    u = 2 * m - w
    return u / (T * np.sqrt(2 * np.pi * T)) * 2 * np.exp(-u**2 / (2 * T))


# =============================================================================
# 4. Numerical Integration via Joint Density
# =============================================================================

def up_and_out_call_joint_density(S0, K, H, T, r, sigma, n_w=200, n_m=200):
    """
    Price an up-and-out call by numerically integrating over the
    joint density of (M_T, W_T).

    C_UO = e^{-rT} * int int (S_T(w) - K)^+ * f_{M_T, W_T}(m, w) dm dw

    subject to m < b (barrier not hit).

    Parameters
    ----------
    S0    : float – Initial stock price
    K     : float – Strike price
    H     : float – Upper barrier
    T     : float – Time to maturity
    r     : float – Risk-free rate
    sigma : float – Volatility
    n_w   : int   – Grid points in w-direction
    n_m   : int   – Grid points in m-direction

    Returns
    -------
    float – Up-and-out call price (numerical)
    """
    if S0 >= H:
        return 0.0

    # Barrier in Brownian motion space
    b = (1.0 / sigma) * np.log(H / S0)
    drift = (r - 0.5 * sigma**2) * T

    # w range: need S_T > K, i.e., w > (log(K/S0) - drift) / sigma
    w_min_payoff = (np.log(K / S0) - drift) / sigma
    w_min = max(w_min_payoff, -6 * np.sqrt(T))  # Ensure reasonable range
    w_max = b  # w cannot exceed b (since w <= m < b)

    if w_min >= w_max:
        return 0.0

    # Create grid
    w_vals = np.linspace(w_min, w_max, n_w)
    dw = (w_max - w_min) / (n_w - 1) if n_w > 1 else 0.0

    price = 0.0
    for w in w_vals:
        # m range: max(0, w) <= m < b
        m_lo = max(0.0, w)
        m_hi = b
        if m_lo >= m_hi:
            continue

        m_vals = np.linspace(m_lo, m_hi, n_m)
        dm = (m_hi - m_lo) / (n_m - 1) if n_m > 1 else 0.0

        # Stock price at terminal time
        S_T = S0 * np.exp(drift + sigma * w)
        payoff = max(S_T - K, 0.0)

        if payoff <= 0:
            continue

        # Integrate over m using trapezoidal rule
        density_vals = np.array([joint_density_MW(m, w, T) for m in m_vals])
        inner_integral = np.trapz(density_vals, m_vals)

        price += payoff * inner_integral * dw

    return np.exp(-r * T) * price


def up_and_out_call_scipy(S0, K, H, T, r, sigma):
    """
    Price an up-and-out call using scipy.integrate.dblquad for
    higher accuracy.

    Parameters
    ----------
    S0    : float – Initial stock price
    K     : float – Strike price
    H     : float – Upper barrier
    T     : float – Time to maturity
    r     : float – Risk-free rate
    sigma : float – Volatility

    Returns
    -------
    float – Up-and-out call price
    float – Estimated integration error
    """
    if S0 >= H:
        return 0.0, 0.0

    b = (1.0 / sigma) * np.log(H / S0)
    drift = (r - 0.5 * sigma**2) * T
    w_min_payoff = (np.log(K / S0) - drift) / sigma

    def integrand(m, w):
        S_T = S0 * np.exp(drift + sigma * w)
        payoff = max(S_T - K, 0.0)
        return payoff * joint_density_MW(m, w, T)

    def m_lower(w):
        return max(0.0, w)

    def m_upper(w):
        return b

    result, error = dblquad(
        integrand,
        w_min_payoff, b,  # w limits
        m_lower, m_upper,  # m limits (functions of w)
        epsabs=1e-10,
        epsrel=1e-10
    )

    return np.exp(-r * T) * result, error


# =============================================================================
# 5. Monte Carlo Simulation
# =============================================================================

def up_and_out_call_monte_carlo(S0, K, H, T, r, sigma, n_paths=100000,
                                  n_steps=252, seed=42):
    """
    Monte Carlo price of an up-and-out call with discrete barrier monitoring.

    Parameters
    ----------
    S0      : float – Initial stock price
    K       : float – Strike price
    H       : float – Upper barrier
    T       : float – Time to maturity
    r       : float – Risk-free rate
    sigma   : float – Volatility
    n_paths : int   – Number of simulation paths
    n_steps : int   – Number of time steps per path
    seed    : int   – Random seed

    Returns
    -------
    float – Monte Carlo price estimate
    float – Standard error
    """
    rng = np.random.default_rng(seed)
    dt = T / n_steps
    drift_dt = (r - 0.5 * sigma**2) * dt
    vol_sqrt_dt = sigma * np.sqrt(dt)

    # Simulate log-price paths
    Z = rng.standard_normal((n_paths, n_steps))
    log_S = np.log(S0) + np.cumsum(drift_dt + vol_sqrt_dt * Z, axis=1)

    # Check barrier condition (max over path)
    max_log_S = np.max(log_S, axis=1)
    not_knocked_out = max_log_S < np.log(H)

    # Terminal payoff
    S_T = np.exp(log_S[:, -1])
    payoffs = np.maximum(S_T - K, 0.0) * not_knocked_out

    # Discounted price
    disc_payoffs = np.exp(-r * T) * payoffs
    price = np.mean(disc_payoffs)
    std_err = np.std(disc_payoffs) / np.sqrt(n_paths)

    return price, std_err


# =============================================================================
# 6. Brownian Bridge Correction for Monte Carlo
# =============================================================================

def up_and_out_call_mc_bridge(S0, K, H, T, r, sigma, n_paths=100000,
                                n_steps=252, seed=42):
    """
    Monte Carlo with Brownian bridge correction for continuous barrier
    monitoring.

    Between each pair of discrete time points, the probability that
    the continuous path crosses the barrier is:

        P(max S in [t_i, t_{i+1}] > H | S_{t_i}, S_{t_{i+1}})
        = exp(-2 * log(H/S_i) * log(H/S_{i+1}) / (sigma^2 * dt))

    if both S_i, S_{i+1} < H, and 1 otherwise.

    Parameters
    ----------
    S0      : float – Initial stock price
    K       : float – Strike price
    H       : float – Upper barrier
    T       : float – Time to maturity
    r       : float – Risk-free rate
    sigma   : float – Volatility
    n_paths : int   – Number of simulation paths
    n_steps : int   – Number of time steps per path
    seed    : int   – Random seed

    Returns
    -------
    float – Monte Carlo price with bridge correction
    float – Standard error
    """
    rng = np.random.default_rng(seed)
    dt = T / n_steps
    drift_dt = (r - 0.5 * sigma**2) * dt
    vol_sqrt_dt = sigma * np.sqrt(dt)

    Z = rng.standard_normal((n_paths, n_steps))
    log_S = np.zeros((n_paths, n_steps + 1))
    log_S[:, 0] = np.log(S0)

    for i in range(n_steps):
        log_S[:, i + 1] = log_S[:, i] + drift_dt + vol_sqrt_dt * Z[:, i]

    log_H = np.log(H)

    # Survival probability via Brownian bridge
    survival_prob = np.ones(n_paths)
    for i in range(n_steps):
        S_i = log_S[:, i]
        S_ip1 = log_S[:, i + 1]

        # If either endpoint exceeds barrier, knocked out
        crossed = (S_i >= log_H) | (S_ip1 >= log_H)
        survival_prob[crossed] = 0.0

        # Brownian bridge correction for non-crossed paths
        not_crossed = ~crossed & (survival_prob > 0)
        if np.any(not_crossed):
            a = log_H - S_i[not_crossed]
            b_val = log_H - S_ip1[not_crossed]
            p_cross = np.exp(-2.0 * a * b_val / (sigma**2 * dt))
            # Generate uniform to decide if barrier was crossed
            U = rng.uniform(size=np.sum(not_crossed))
            knocked = U < p_cross
            idx = np.where(not_crossed)[0]
            survival_prob[idx[knocked]] = 0.0

    S_T = np.exp(log_S[:, -1])
    payoffs = np.maximum(S_T - K, 0.0) * (survival_prob > 0)
    disc_payoffs = np.exp(-r * T) * payoffs
    price = np.mean(disc_payoffs)
    std_err = np.std(disc_payoffs) / np.sqrt(n_paths)

    return price, std_err


# =============================================================================
# 7. Visualization
# =============================================================================

def plot_joint_density(T=1.0, b=1.5, n_grid=200):
    """
    Plot the joint density f_{M_T, W_T}(m, w) with the barrier constraint m < b.

    Parameters
    ----------
    T      : float – Time horizon
    b      : float – Barrier level in Brownian motion space
    n_grid : int   – Grid resolution
    """
    w_vals = np.linspace(-3 * np.sqrt(T), b, n_grid)
    m_vals = np.linspace(0, b, n_grid)
    W, M = np.meshgrid(w_vals, m_vals)

    # Evaluate density (respecting w <= m constraint)
    Z = np.zeros_like(W)
    for i in range(n_grid):
        for j in range(n_grid):
            if W[i, j] <= M[i, j]:
                Z[i, j] = joint_density_MW(M[i, j], W[i, j], T)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Contour plot
    ax = axes[0]
    cf = ax.contourf(W, M, Z, levels=30, cmap='viridis')
    ax.set_xlabel(r'$W_T$ (terminal value)', fontsize=12)
    ax.set_ylabel(r'$M_T$ (running maximum)', fontsize=12)
    ax.set_title(r'Joint Density $f_{M_T, W_T}(m, w)$ with Barrier $m < b$', fontsize=13)
    ax.axhline(y=b, color='red', linestyle='--', linewidth=2, label=f'Barrier $b = {b:.1f}$')
    ax.plot(w_vals, w_vals, 'w--', linewidth=1, alpha=0.5, label=r'$w = m$ boundary')
    ax.legend(fontsize=10)
    plt.colorbar(cf, ax=ax, label='Density')

    # Marginal density of W_T given M_T < b
    ax = axes[1]
    marginal_w = np.zeros(n_grid)
    for j, w in enumerate(w_vals):
        m_lo = max(0.0, w)
        if m_lo < b:
            m_range = np.linspace(m_lo, b, 100)
            densities = [joint_density_MW(m, w, T) for m in m_range]
            marginal_w[j] = np.trapz(densities, m_range)

    # Compare with unconstrained normal density
    normal_density = norm.pdf(w_vals, loc=0, scale=np.sqrt(T))

    ax.plot(w_vals, marginal_w, 'b-', linewidth=2, label=r'$f_{W_T | M_T < b}(w)$')
    ax.plot(w_vals, normal_density, 'k--', linewidth=1.5, alpha=0.6,
            label=r'$\phi(w; 0, T)$ (unconstrained)')
    ax.fill_between(w_vals, marginal_w, alpha=0.2, color='blue')
    ax.set_xlabel(r'$W_T$', fontsize=12)
    ax.set_ylabel('Density', fontsize=12)
    ax.set_title(r'Marginal of $W_T$ Constrained by $M_T < b$', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('joint_density_barrier.png', dpi=150, bbox_inches='tight')
    plt.show()


def plot_price_comparison(S0=100, K=100, T=1.0, r=0.05, sigma=0.2):
    """
    Compare up-and-out call prices across barrier levels using all methods.

    Parameters
    ----------
    S0    : float – Initial stock price
    K     : float – Strike price
    T     : float – Time to maturity
    r     : float – Risk-free rate
    sigma : float – Volatility
    """
    barriers = np.linspace(S0 * 1.05, S0 * 2.0, 20)

    prices_closed = []
    prices_numerical = []
    prices_mc = []
    mc_errors = []

    print(f"{'Barrier':>10} {'Closed-Form':>12} {'Joint Density':>14} {'Monte Carlo':>12} {'MC Std Err':>10}")
    print("-" * 62)

    for H in barriers:
        # Closed-form
        p_cf = up_and_out_call_closed_form(S0, K, H, T, r, sigma)
        prices_closed.append(p_cf)

        # Joint density (scipy)
        p_jd, _ = up_and_out_call_scipy(S0, K, H, T, r, sigma)
        prices_numerical.append(p_jd)

        # Monte Carlo with bridge
        p_mc, se_mc = up_and_out_call_mc_bridge(S0, K, H, T, r, sigma,
                                                  n_paths=50000, n_steps=252)
        prices_mc.append(p_mc)
        mc_errors.append(se_mc)

        print(f"{H:10.2f} {p_cf:12.6f} {p_jd:14.6f} {p_mc:12.6f} {se_mc:10.6f}")

    # Vanilla BS price for reference
    vanilla_price = bs_call_price(S0, K, T, r, sigma)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Price comparison
    ax = axes[0]
    ax.plot(barriers, prices_closed, 'b-', linewidth=2, label='Closed-Form (Image)')
    ax.plot(barriers, prices_numerical, 'r--', linewidth=2, label='Joint Density (Scipy)')
    ax.errorbar(barriers, prices_mc, yerr=np.array(mc_errors) * 1.96, fmt='go',
                markersize=4, capsize=3, label='Monte Carlo (Bridge)')
    ax.axhline(y=vanilla_price, color='gray', linestyle=':', linewidth=1,
               label=f'Vanilla BS = {vanilla_price:.4f}')
    ax.set_xlabel('Barrier Level $H$', fontsize=12)
    ax.set_ylabel('Option Price', fontsize=12)
    ax.set_title('Up-and-Out Call Price vs Barrier Level', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    # Pricing error (relative to closed-form)
    ax = axes[1]
    errors_jd = np.array(prices_numerical) - np.array(prices_closed)
    errors_mc = np.array(prices_mc) - np.array(prices_closed)
    ax.plot(barriers, errors_jd, 'r-o', markersize=4, linewidth=1.5,
            label='Joint Density - Closed Form')
    ax.plot(barriers, errors_mc, 'g-s', markersize=4, linewidth=1.5,
            label='Monte Carlo - Closed Form')
    ax.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    ax.set_xlabel('Barrier Level $H$', fontsize=12)
    ax.set_ylabel('Pricing Error', fontsize=12)
    ax.set_title('Pricing Error Relative to Closed-Form', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('barrier_price_comparison.png', dpi=150, bbox_inches='tight')
    plt.show()


# =============================================================================
# 8. Main Execution
# =============================================================================

if __name__ == "__main__":
    # Parameters
    S0 = 100.0    # Initial stock price
    K = 100.0     # Strike price
    H = 130.0     # Upper barrier
    T = 1.0       # Time to maturity (1 year)
    r = 0.05      # Risk-free rate
    sigma = 0.20  # Volatility

    print("=" * 65)
    print("  Barrier Option Pricing via Joint Law of (W_t, M_t)")
    print("=" * 65)
    print(f"\n  S0 = {S0}, K = {K}, H = {H}, T = {T}, r = {r}, sigma = {sigma}\n")

    # Method 1: Closed-form
    price_cf = up_and_out_call_closed_form(S0, K, H, T, r, sigma)
    print(f"  [1] Closed-Form (Image Method):    {price_cf:.6f}")

    # Method 2: Joint density (manual grid)
    price_grid = up_and_out_call_joint_density(S0, K, H, T, r, sigma, n_w=300, n_m=300)
    print(f"  [2] Joint Density (Grid 300x300):   {price_grid:.6f}")

    # Method 3: Joint density (scipy)
    price_scipy, err_scipy = up_and_out_call_scipy(S0, K, H, T, r, sigma)
    print(f"  [3] Joint Density (Scipy dblquad):  {price_scipy:.6f}  (err ~ {err_scipy:.2e})")

    # Method 4: Monte Carlo (discrete monitoring)
    price_mc, se_mc = up_and_out_call_monte_carlo(S0, K, H, T, r, sigma,
                                                    n_paths=200000, n_steps=252)
    print(f"  [4] Monte Carlo (discrete, 200K):   {price_mc:.6f}  (SE = {se_mc:.6f})")

    # Method 5: Monte Carlo with Brownian bridge
    price_bb, se_bb = up_and_out_call_mc_bridge(S0, K, H, T, r, sigma,
                                                  n_paths=200000, n_steps=252)
    print(f"  [5] Monte Carlo (bridge, 200K):     {price_bb:.6f}  (SE = {se_bb:.6f})")

    # Reference: Vanilla BS price
    vanilla = bs_call_price(S0, K, T, r, sigma)
    print(f"\n  Vanilla BS Call Price:              {vanilla:.6f}")
    print(f"  Barrier Discount (UO/Vanilla):      {price_cf / vanilla:.4f}")

    print("\n" + "=" * 65)
    print("  In-Out Parity Check")
    print("=" * 65)
    price_ui = vanilla - price_cf
    print(f"  Up-and-In Call = Vanilla - UO:      {price_ui:.6f}")
    print(f"  Sum (UI + UO):                      {price_ui + price_cf:.6f}")
    print(f"  Vanilla:                            {vanilla:.6f}")
    print(f"  Parity Error:                       {abs(price_ui + price_cf - vanilla):.2e}")

    # Visualizations
    print("\n  Generating plots...")
    plot_joint_density(T=T, b=(1.0 / sigma) * np.log(H / S0))
    plot_price_comparison(S0=S0, K=K, T=T, r=r, sigma=sigma)

    print("\n  Done.")
