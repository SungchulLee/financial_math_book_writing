"""
Heath-Jarrow-Morton (HJM) Forward Rate Model - Multi-Factor Implementation

This module implements the Heath-Jarrow-Morton framework for forward rate modeling.
The HJM model directly specifies the dynamics of the entire forward rate curve,
ensuring no-arbitrage by construction.

The forward rate dynamics are:
    df(t, T) = mu(t, T) dt + sum_j sigma_j(t, T) dW_j(t)

where the drift mu must satisfy the no-arbitrage condition:
    mu(t, T) = sum_j sigma_j(t, T) * integral_t^T sigma_j(t, s) ds

Key features:
- Multi-factor specification with independent Brownian motions
- No-arbitrage condition enforced via drift specification
- Forward rate curve evolution
- Implied zero-coupon bond prices
- Non-recombining tree structure

Based on: QuantPie Lecture Notes
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.stats import norm


def f(P, T):
    """
    Extract forward rate from zero-coupon bond prices.

    Parameters
    ----------
    P : callable
        ZCB price function P(0, T)
    T : float
        Maturity time

    Returns
    -------
    float
        Forward rate f(0, T)

    Notes
    -----
    f(0, T) = -d/dT log(P(0, T))
    Computed via finite difference
    """
    dT = 1e-6
    if T <= dT:
        log_P_plus = np.log(P(T + dT))
        log_P_current = np.log(P(T))
        return -(log_P_plus - log_P_current) / dT
    else:
        log_P_minus = np.log(P(T - dT))
        log_P_plus = np.log(P(T + dT))
        return -(log_P_plus - log_P_minus) / (2 * dT)


def df_over_dT(P, T):
    """
    Compute derivative of forward rate with respect to maturity.

    Parameters
    ----------
    P : callable
        ZCB price function
    T : float
        Maturity time

    Returns
    -------
    float
        df/dT(0, T)
    """
    dT = 1e-6
    f_minus = f(P, T - dT)
    f_plus = f(P, T + dT)
    return (f_plus - f_minus) / (2 * dT)


def compute_r0(P):
    """
    Extract initial short rate from yield curve.

    Parameters
    ----------
    P : callable
        ZCB price function P(0, T)

    Returns
    -------
    float
        r(0) = f(0, 0)
    """
    return f(P, 0.0)


class HJMModel:
    """
    Heath-Jarrow-Morton Multi-Factor Forward Rate Model.

    The model directly specifies forward rate dynamics under the no-arbitrage condition.

    Parameters
    ----------
    P_0 : callable
        Initial zero-coupon bond price function P(0, T)
    sigma_funcs : list of callable
        List of volatility functions sigma_j(t, T) for each factor
    num_factors : int
        Number of factors (len(sigma_funcs))
    """

    def __init__(self, P_0, sigma_funcs, num_factors=2):
        """Initialize HJM model."""
        self.P_0 = P_0
        self.sigma_funcs = sigma_funcs
        self.num_factors = num_factors

        # Extract initial forward rate curve
        self.r0 = compute_r0(P_0)

    def _compute_drift(self, t, T):
        """
        Compute drift (mu) satisfying no-arbitrage condition.

        Parameters
        ----------
        t : float
            Current time
        T : float
            Forward rate maturity

        Returns
        -------
        float
            mu(t, T)

        Notes
        -----
        No-arbitrage condition:
        mu(t, T) = sum_j sigma_j(t, T) * integral_t^T sigma_j(t, s) ds
        """
        mu = 0.0

        for j in range(self.num_factors):
            # sigma_j at (t, T)
            sigma_jT = self.sigma_funcs[j](t, T)

            # Integral of sigma_j from t to T
            def integrand(s):
                return self.sigma_funcs[j](t, s)

            integral, _ = quad(integrand, t, T, limit=100)

            # Accumulate drift
            mu += sigma_jT * integral

        return mu

    def _compute_volatilities(self, t, T):
        """
        Compute volatilities sigma_j(t, T) for all factors.

        Parameters
        ----------
        t : float
            Current time
        T : float
            Forward rate maturity

        Returns
        -------
        ndarray
            Volatilities for each factor (num_factors,)
        """
        sigmas = np.zeros(self.num_factors)
        for j in range(self.num_factors):
            sigmas[j] = self.sigma_funcs[j](t, T)
        return sigmas

    def generate_forward_paths(self, T_horizon, T_maturities, num_steps, num_paths, seed=None):
        """
        Generate sample paths for forward rates.

        Parameters
        ----------
        T_horizon : float
            Time horizon for simulation
        T_maturities : ndarray
            Maturity times for which to track forward rates
        num_steps : int
            Number of time steps
        num_paths : int
            Number of Monte Carlo paths
        seed : int, optional
            Random seed

        Returns
        -------
        t : ndarray
            Time grid (num_steps + 1,)
        F : ndarray
            Forward rate paths (num_paths, num_steps + 1, len(T_maturities))
        R : ndarray
            Short rate paths (num_paths, num_steps + 1)
        """
        if seed is not None:
            np.random.seed(seed)

        # Time grid
        t = np.linspace(0, T_horizon, num_steps + 1)
        dt = t[1] - t[0]
        sqrt_dt = np.sqrt(dt)

        # Number of maturities to track
        n_maturities = len(T_maturities)

        # Initialize arrays
        F = np.zeros((num_paths, num_steps + 1, n_maturities))
        R = np.zeros((num_paths, num_steps + 1))

        # Set initial forward rates
        for m_idx, T_m in enumerate(T_maturities):
            F[:, 0, m_idx] = f(self.P_0, T_m)
        R[:, 0] = self.r0

        # Generate Brownian increments
        dW = np.random.normal(0, 1, (num_paths, num_steps, self.num_factors))

        # Simulation loop
        for i in range(num_steps):
            t_current = t[i]

            for m_idx, T_m in enumerate(T_maturities):
                # Skip if maturity has passed
                if T_m <= t_current:
                    if m_idx == 0:
                        F[:, i+1, m_idx] = R[:, i]
                    continue

                # Compute drift and volatilities
                mu = self._compute_drift(t_current, T_m)
                sigmas = self._compute_volatilities(t_current, T_m)

                # Forward rate increment
                df = mu * dt + np.dot(sigmas, dW[:, i, :].T) * sqrt_dt

                # Update forward rate
                F[:, i+1, m_idx] = F[:, i, m_idx] + df

            # Short rate is the forward rate at t with maturity t (f(t, t) = r(t))
            # Approximate with forward rate with shortest maturity
            if n_maturities > 0:
                dt_mat = T_maturities[0]
                if dt_mat > 1e-6:
                    # Interpolate/extrapolate to get r(t)
                    R[:, i+1] = F[:, i+1, 0]
                else:
                    R[:, i+1] = R[:, i]

        return t, F, R

    def compute_zcb_price(self, t, T, forward_rates, T_maturities):
        """
        Compute zero-coupon bond price from forward rates.

        Parameters
        ----------
        t : float
            Current time
        T : float
            Bond maturity
        forward_rates : ndarray
            Forward rates f(t, s) at current time
        T_maturities : ndarray
            Maturity times for forward rates

        Returns
        -------
        float
            P(t, T)

        Notes
        -----
        P(t, T) = exp(-integral_t^T f(t, s) ds)
        """
        if T <= t:
            return 1.0

        # Integrate forward rates using trapezoidal rule
        # Find indices in T_maturities between t and T
        valid_mask = (T_maturities >= t) & (T_maturities <= T)
        valid_maturities = T_maturities[valid_mask]
        valid_forward_rates = forward_rates[valid_mask]

        if len(valid_maturities) == 0:
            # Extrapolate with first available forward rate
            integral = forward_rates[0] * (T - t)
        else:
            # Numerical integration via trapezoidal rule
            integral = np.trapz(valid_forward_rates, valid_maturities)

        return np.exp(-integral)


def main():
    """
    Demonstrate HJM multi-factor model with forward rate path simulation.
    """
    print("=" * 70)
    print("Heath-Jarrow-Morton (HJM) Multi-Factor Model Demonstration")
    print("=" * 70)

    # Simulation parameters
    T_horizon = 5.0
    num_steps = 50
    num_paths = 500

    # Model parameters
    r0 = 0.05  # Initial short rate (5%)

    # Flat initial yield curve
    def P_0(T):
        return np.exp(-r0 * T)

    print(f"\nInitial short rate r(0) = {r0:.4f}")
    print(f"Initial yield curve: flat at {r0*100:.2f}%")
    print()

    # Define volatility functions for each factor
    # Factor 1: slower decay with maturity
    def sigma_1(t, T):
        return 0.010 * np.exp(-0.1 * (T - t))

    # Factor 2: faster decay with maturity
    def sigma_2(t, T):
        return 0.005 * np.exp(-0.5 * (T - t))

    sigma_funcs = [sigma_1, sigma_2]
    num_factors = len(sigma_funcs)

    print(f"Number of factors: {num_factors}")
    print(f"  Factor 1: sigma_1(t,T) = 0.010 * exp(-0.1*(T-t))")
    print(f"  Factor 2: sigma_2(t,T) = 0.005 * exp(-0.5*(T-t))")
    print()

    # Create HJM model
    print("Creating HJM model...")
    hjm = HJMModel(P_0, sigma_funcs, num_factors)

    # Maturities to track
    T_maturities = np.array([1.0, 2.0, 3.0, 5.0, 7.0, 10.0])

    # Generate paths
    print("Generating forward rate paths...")
    t_grid, F_paths, R_paths = hjm.generate_forward_paths(
        T_horizon, T_maturities, num_steps, num_paths, seed=42
    )

    print(f"  Generated {num_paths} paths with {num_steps} steps")
    print(f"  Time horizon: {T_horizon} years")
    print(f"  Tracked maturities: {T_maturities}")
    print()

    # Statistics
    mean_r = np.mean(R_paths, axis=0)
    std_r = np.std(R_paths, axis=0)

    print(f"Short rate statistics at T={T_horizon}:")
    print(f"  Mean r(T):     {mean_r[-1]:.6f}")
    print(f"  Std r(T):      {std_r[-1]:.6f}")
    print(f"  Min r(T):      {R_paths[:, -1].min():.6f}")
    print(f"  Max r(T):      {R_paths[:, -1].max():.6f}")
    print()

    # Forward rate evolution
    print("Forward rates at T=0 (initial curve):")
    for m_idx, T_m in enumerate(T_maturities):
        print(f"  f(0, {T_m:.1f}) = {F_paths[0, 0, m_idx]:.6f}")
    print()

    # Visualization
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Plot 1: Short rate paths
    ax = axes[0, 0]
    sample_indices = np.arange(0, num_paths, max(1, num_paths // 50))
    for idx in sample_indices:
        ax.plot(t_grid, R_paths[idx, :], alpha=0.3, linewidth=0.8)
    ax.plot(t_grid, mean_r, 'r-', linewidth=2, label='Mean')
    ax.fill_between(t_grid, mean_r - std_r, mean_r + std_r,
                     alpha=0.2, color='red', label='Mean +/- 1 Std')
    ax.set_xlabel('Time (years)')
    ax.set_ylabel('Short rate r(t)')
    ax.set_title('Short Rate Paths')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 2: Terminal short rate distribution
    ax = axes[0, 1]
    ax.hist(R_paths[:, -1], bins=40, density=True, alpha=0.7, edgecolor='black')
    ax.axvline(mean_r[-1], color='r', linestyle='--', linewidth=2, label='Mean')
    ax.set_xlabel('Short rate r(T)')
    ax.set_ylabel('Density')
    ax.set_title(f'Terminal Distribution of r(T) at T={T_horizon}')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 3: Forward rate evolution (mean)
    ax = axes[1, 0]
    for m_idx, T_m in enumerate(T_maturities):
        mean_forward = np.mean(F_paths[:, :, m_idx], axis=0)
        ax.plot(t_grid, mean_forward, label=f'f(t, {T_m:.1f})', linewidth=2)
    ax.set_xlabel('Time (years)')
    ax.set_ylabel('Forward rate')
    ax.set_title('Evolution of Mean Forward Rates')
    ax.legend(loc='best', fontsize=9)
    ax.grid(True, alpha=0.3)

    # Plot 4: Yield curve at different times
    ax = axes[1, 1]
    time_points_to_plot = [0, num_steps // 2, num_steps]
    colors = ['blue', 'green', 'red']
    labels = [f't={t_grid[tp]:.2f}' for tp in time_points_to_plot]

    for tp_idx, tp in enumerate(time_points_to_plot):
        mean_forwards = np.mean(F_paths[:, tp, :], axis=0)
        ax.plot(T_maturities, mean_forwards, 'o-', color=colors[tp_idx],
                label=labels[tp_idx], linewidth=2, markersize=6)

    ax.set_xlabel('Maturity (years)')
    ax.set_ylabel('Forward rate')
    ax.set_title('Forward Rate Curve at Different Times')
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('hjm_simulation_multi_factor.png', dpi=150, bbox_inches='tight')
    print("Figure saved as 'hjm_simulation_multi_factor.png'")
    plt.show()


if __name__ == '__main__':
    main()
