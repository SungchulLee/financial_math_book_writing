"""
Two-Factor Hull-White Interest Rate Model

This module implements the two-factor Hull-White model, which extends
the one-factor model with two correlated mean-reverting factors.

The SDE is:
    dr(t) = [theta(t) - lambda1*x(t) - lambda2*y(t)] dt + sigma1*dW1(t) + sigma2*dW2(t)
    dx(t) = -lambda1*x(t) dt + dW1(t)
    dy(t) = -lambda2*y(t) dt + dW2(t)

where r(t) = f(0,t) + x(t) + y(t), and dW1 and dW2 are correlated with correlation rho.

Key features:
- Two independent mean-reverting factors with correlation
- Cholesky decomposition for correlated Brownian motions
- More flexible term structure modeling than one-factor model
- Captures both parallel and non-parallel yield curve shifts

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
        ZCB price function P(t, T) where t is fixed
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


class HullWhite2:
    """
    Two-Factor Hull-White Model.

    The model uses two correlated mean-reverting factors to describe
    the dynamics of the short rate.

    Parameters
    ----------
    sigma1 : float
        Volatility of first factor
    sigma2 : float
        Volatility of second factor
    lambd1 : float
        Mean reversion rate of first factor
    lambd2 : float
        Mean reversion rate of second factor
    rho : float
        Correlation between Brownian motions (-1 < rho < 1)
    P : callable
        Initial zero-coupon bond price function P(0, T)
    """

    def __init__(self, sigma1, sigma2, lambd1, lambd2, rho, P):
        """Initialize Hull-White two-factor model."""
        self.sigma1 = sigma1
        self.sigma2 = sigma2
        self.lambd1 = lambd1
        self.lambd2 = lambd2
        self.rho = rho
        self.P = P

        # Extract initial rate
        self.r0 = compute_r0(P)

        # Precompute Cholesky decomposition for correlated Brownian motions
        # [dW1]   [1    0  ] [dZ1]
        # [dW2] = [rho sqrt(1-rho^2)] [dZ2]
        self.chol_factor = np.sqrt(1.0 - rho**2)

    def _compute_theta(self, t):
        """
        Compute theta(t) for the two-factor model.

        Parameters
        ----------
        t : float
            Time

        Returns
        -------
        float
            theta(t)

        Notes
        -----
        In the two-factor model, theta is adjusted to account for both factors.
        """
        f_t = f(self.P, t)
        df_dt = df_over_dT(self.P, t)

        # Correction terms for both factors
        if self.lambd1 > 1e-8:
            term1 = self.sigma1**2 / (2 * self.lambd1**2) * (1 - np.exp(-2 * self.lambd1 * t))**2
        else:
            term1 = self.sigma1**2 * t**2 / 2

        if self.lambd2 > 1e-8:
            term2 = self.sigma2**2 / (2 * self.lambd2**2) * (1 - np.exp(-2 * self.lambd2 * t))**2
        else:
            term2 = self.sigma2**2 * t**2 / 2

        if self.lambd1 > 1e-8 and self.lambd2 > 1e-8:
            cross_term = 2 * self.sigma1 * self.sigma2 * self.rho / (
                self.lambd1 * self.lambd2 * (self.lambd1 + self.lambd2)
            ) * (1 - np.exp(-(self.lambd1 + self.lambd2) * t))**2
        else:
            cross_term = 0.0

        return df_dt + self.lambd1 * f_t + self.lambd2 * f_t + term1 + term2 + cross_term

    def _compute_Bx(self, T, U):
        """
        Compute B_x coefficient for first factor.

        Parameters
        ----------
        T : float
            Current time
        U : float
            Bond maturity

        Returns
        -------
        float
            B_x(T, U)
        """
        if self.lambd1 > 1e-8:
            return (1 - np.exp(-self.lambd1 * (U - T))) / self.lambd1
        else:
            return U - T

    def _compute_By(self, T, U):
        """
        Compute B_y coefficient for second factor.

        Parameters
        ----------
        T : float
            Current time
        U : float
            Bond maturity

        Returns
        -------
        float
            B_y(T, U)
        """
        if self.lambd2 > 1e-8:
            return (1 - np.exp(-self.lambd2 * (U - T))) / self.lambd2
        else:
            return U - T

    def compute_A(self, T, U):
        """
        Compute A coefficient for ZCB pricing.

        Parameters
        ----------
        T : float
            Current time
        U : float
            Bond maturity

        Returns
        -------
        float
            A(T, U)

        Notes
        -----
        Bond price: P(T, U) = A(T, U) * exp(-Bx(T, U)*x(T) - By(T, U)*y(T))
        """
        Bx = self._compute_Bx(T, U)
        By = self._compute_By(T, U)

        # Variance of bond price logarithm
        var_Bx = self.sigma1**2 / (2 * self.lambd1**2) * Bx**2 if self.lambd1 > 1e-8 else 0.5 * self.sigma1**2 * Bx**2
        var_By = self.sigma2**2 / (2 * self.lambd2**2) * By**2 if self.lambd2 > 1e-8 else 0.5 * self.sigma2**2 * By**2

        # Cross-term
        if self.lambd1 > 1e-8 and self.lambd2 > 1e-8:
            cov_term = self.sigma1 * self.sigma2 * self.rho / (self.lambd1 * self.lambd2) * Bx * By
        else:
            cov_term = 0.0

        # A = P(0, U) / P(0, T) * exp(0.5 * [variance terms])
        exp_adj = 0.5 * (var_Bx + var_By + 2 * cov_term)

        return self.P(U) / self.P(T) * np.exp(exp_adj)

    def compute_B(self, T, U):
        """
        Compute combined B coefficient (deprecated; use compute_Bx and compute_By).

        Parameters
        ----------
        T : float
            Current time
        U : float
            Bond maturity

        Returns
        -------
        tuple
            (Bx, By)
        """
        return self._compute_Bx(T, U), self._compute_By(T, U)

    def compute_ZCB(self, T, U, x_T, y_T):
        """
        Compute zero-coupon bond price at time T.

        Parameters
        ----------
        T : float
            Current time
        U : float
            Bond maturity
        x_T : float
            Factor x at time T
        y_T : float
            Factor y at time T

        Returns
        -------
        float
            P(T, U)
        """
        A_TU = self.compute_A(T, U)
        Bx_TU = self._compute_Bx(T, U)
        By_TU = self._compute_By(T, U)

        return A_TU * np.exp(-Bx_TU * x_T - By_TU * y_T)

    def generate_sample_paths(self, T, num_steps, num_paths, seed=None):
        """
        Generate sample paths for the two-factor model.

        Parameters
        ----------
        T : float
            Total time horizon
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
        X : ndarray
            First factor paths (num_paths, num_steps + 1)
        Y : ndarray
            Second factor paths (num_paths, num_steps + 1)
        R : ndarray
            Short rate paths (num_paths, num_steps + 1)
        M : ndarray
            Money market account (num_paths, num_steps + 1)
        """
        if seed is not None:
            np.random.seed(seed)

        # Time grid
        t = np.linspace(0, T, num_steps + 1)
        dt = t[1] - t[0]
        sqrt_dt = np.sqrt(dt)

        # Initialize
        X = np.zeros((num_paths, num_steps + 1))
        Y = np.zeros((num_paths, num_steps + 1))
        R = np.zeros((num_paths, num_steps + 1))
        M = np.ones((num_paths, num_steps + 1))

        # Initial short rate
        R[:, 0] = self.r0

        # Generate standard normal increments
        Z1 = np.random.normal(0, 1, (num_paths, num_steps))
        Z2 = np.random.normal(0, 1, (num_paths, num_steps))

        # Create correlated Brownian increments using Cholesky
        # dW1 = dZ1
        # dW2 = rho * dZ1 + sqrt(1 - rho^2) * dZ2
        dW1 = Z1
        dW2 = self.rho * Z1 + self.chol_factor * Z2

        # Simulation
        for i in range(num_steps):
            theta_t = self._compute_theta(t[i])

            # Factor dynamics
            # dx = -lambda1*x dt + sigma1 dW1
            dX = -self.lambd1 * X[:, i] * dt + self.sigma1 * sqrt_dt * dW1[:, i]
            X[:, i+1] = X[:, i] + dX

            # dy = -lambda2*y dt + sigma2 dW2
            dY = -self.lambd2 * Y[:, i] * dt + self.sigma2 * sqrt_dt * dW2[:, i]
            Y[:, i+1] = Y[:, i] + dY

            # Short rate: r = f(0, t) + x + y
            r_forward = f(self.P, t[i])
            R[:, i+1] = r_forward + X[:, i+1] + Y[:, i+1]

            # Money market: dM/M = r dt
            M[:, i+1] = M[:, i] * np.exp(R[:, i] * dt)

        return t, X, Y, R, M

    def phi(self, t):
        """
        Deterministic shift (phi function) for the model.

        Parameters
        ----------
        t : float
            Time

        Returns
        -------
        float
            phi(t)

        Notes
        -----
        phi(t) = f(0, t) is the initial forward rate
        """
        return f(self.P, t)


def main():
    """
    Demonstrate two-factor Hull-White model with visualization.
    """
    print("=" * 70)
    print("Two-Factor Hull-White Interest Rate Model Demonstration")
    print("=" * 70)

    # Parameters
    T_total = 10.0
    num_steps = 100
    num_paths = 1000

    # Model parameters
    sigma1 = 0.015  # Volatility of first factor
    sigma2 = 0.010  # Volatility of second factor
    lambd1 = 0.10   # Mean reversion of first factor
    lambd2 = 0.02   # Mean reversion of second factor (slower)
    rho = 0.5       # Correlation between factors

    print(f"\nModel Parameters:")
    print(f"  Sigma1 (volatility 1):    {sigma1:.4f}")
    print(f"  Sigma2 (volatility 2):    {sigma2:.4f}")
    print(f"  Lambda1 (mean reversion 1): {lambd1:.4f}")
    print(f"  Lambda2 (mean reversion 2): {lambd2:.4f}")
    print(f"  Rho (correlation):        {rho:.4f}")
    print()

    # Flat yield curve at 5%
    r0 = 0.05
    def P_0(T):
        return np.exp(-r0 * T)

    print(f"Initial short rate r(0) = {r0:.4f}")
    print()

    # Create model
    print("Creating Hull-White two-factor model...")
    hw2 = HullWhite2(sigma1, sigma2, lambd1, lambd2, rho, P_0)

    # Generate paths
    print("Generating sample paths...")
    t_grid, X_paths, Y_paths, R_paths, M_paths = hw2.generate_sample_paths(
        T_total, num_steps, num_paths, seed=42
    )

    print(f"  Generated {num_paths} paths with {num_steps} steps")
    print(f"  Time horizon: {T_total} years")
    print()

    # Statistics
    mean_x = np.mean(X_paths, axis=0)
    std_x = np.std(X_paths, axis=0)
    mean_y = np.mean(Y_paths, axis=0)
    std_y = np.std(Y_paths, axis=0)
    mean_r = np.mean(R_paths, axis=0)
    std_r = np.std(R_paths, axis=0)

    print("Factor X statistics at final time T={}:".format(T_total))
    print(f"  Mean x(T):    {mean_x[-1]:.6f}")
    print(f"  Std x(T):     {std_x[-1]:.6f}")
    print()

    print("Factor Y statistics at final time T={}:".format(T_total))
    print(f"  Mean y(T):    {mean_y[-1]:.6f}")
    print(f"  Std y(T):     {std_y[-1]:.6f}")
    print()

    print("Short rate statistics at final time T={}:".format(T_total))
    print(f"  Mean r(T):    {mean_r[-1]:.6f}")
    print(f"  Std r(T):     {std_r[-1]:.6f}")
    print(f"  Min r(T):     {R_paths[:, -1].min():.6f}")
    print(f"  Max r(T):     {R_paths[:, -1].max():.6f}")
    print()

    # Compute correlation between factors at final time
    corr_xy = np.corrcoef(X_paths[:, -1], Y_paths[:, -1])[0, 1]
    print(f"Realized correlation between X and Y at T={T_total}: {corr_xy:.4f}")
    print(f"(Target correlation: {rho:.4f})")
    print()

    # Visualization
    fig, axes = plt.subplots(2, 3, figsize=(16, 10))

    # Plot 1: Factor X paths
    ax = axes[0, 0]
    sample_indices = np.arange(0, num_paths, max(1, num_paths // 50))
    for idx in sample_indices:
        ax.plot(t_grid, X_paths[idx, :], alpha=0.3, linewidth=0.8)
    ax.plot(t_grid, mean_x, 'r-', linewidth=2, label='Mean')
    ax.fill_between(t_grid, mean_x - std_x, mean_x + std_x,
                     alpha=0.2, color='red', label='Mean +/- 1 Std')
    ax.set_xlabel('Time (years)')
    ax.set_ylabel('x(t)')
    ax.set_title('Factor X Paths')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 2: Factor Y paths
    ax = axes[0, 1]
    for idx in sample_indices:
        ax.plot(t_grid, Y_paths[idx, :], alpha=0.3, linewidth=0.8)
    ax.plot(t_grid, mean_y, 'b-', linewidth=2, label='Mean')
    ax.fill_between(t_grid, mean_y - std_y, mean_y + std_y,
                     alpha=0.2, color='blue', label='Mean +/- 1 Std')
    ax.set_xlabel('Time (years)')
    ax.set_ylabel('y(t)')
    ax.set_title('Factor Y Paths')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 3: Short rate paths
    ax = axes[0, 2]
    for idx in sample_indices:
        ax.plot(t_grid, R_paths[idx, :], alpha=0.3, linewidth=0.8)
    ax.plot(t_grid, mean_r, 'g-', linewidth=2, label='Mean')
    ax.fill_between(t_grid, mean_r - std_r, mean_r + std_r,
                     alpha=0.2, color='green', label='Mean +/- 1 Std')
    ax.set_xlabel('Time (years)')
    ax.set_ylabel('r(t)')
    ax.set_title('Short Rate r(t) = f(0,t) + x(t) + y(t)')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 4: Terminal distribution of X
    ax = axes[1, 0]
    ax.hist(X_paths[:, -1], bins=40, density=True, alpha=0.7, edgecolor='black')
    ax.axvline(mean_x[-1], color='r', linestyle='--', linewidth=2, label='Mean')
    ax.set_xlabel('x(T)')
    ax.set_ylabel('Density')
    ax.set_title(f'Terminal Distribution of x(T) at T={T_total}')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 5: Terminal distribution of Y
    ax = axes[1, 1]
    ax.hist(Y_paths[:, -1], bins=40, density=True, alpha=0.7, edgecolor='black')
    ax.axvline(mean_y[-1], color='b', linestyle='--', linewidth=2, label='Mean')
    ax.set_xlabel('y(T)')
    ax.set_ylabel('Density')
    ax.set_title(f'Terminal Distribution of y(T) at T={T_total}')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Plot 6: Scatter plot of X vs Y (correlation)
    ax = axes[1, 2]
    ax.scatter(X_paths[:, -1], Y_paths[:, -1], alpha=0.5, s=10)
    ax.set_xlabel('x(T)')
    ax.set_ylabel('y(T)')
    ax.set_title(f'Correlation between Factors: {corr_xy:.3f}')
    ax.grid(True, alpha=0.3)

    # Add text with model info
    textstr = f'Target rho={rho:.3f}\nRealized rho={corr_xy:.3f}'
    ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=10,
            verticalalignment='top', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

    plt.tight_layout()
    plt.savefig('hull_white_two_factor.png', dpi=150, bbox_inches='tight')
    print("Figure saved as 'hull_white_two_factor.png'")
    plt.show()


if __name__ == '__main__':
    main()
