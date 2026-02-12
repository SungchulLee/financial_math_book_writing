# greeks_computation_and_visualization.py
"""
Greeks Computation and Visualization.

This module computes the Greeks (delta, gamma, vega, theta, rho) for the 
Black-Scholes model and provides visualization of their behavior across 
spot price, time, and volatility dimensions.

Greeks measure sensitivity of option price to different market parameters.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from typing import Dict, Tuple


class GreeksCalculator:
    """Compute Greeks for European options under Black-Scholes model."""
    
    def __init__(self, K: float, T: float, r: float, sigma: float):
        """
        Initialize Greeks calculator with contract parameters.
        
        Args:
            K: Strike price
            T: Time to maturity
            r: Risk-free rate
            sigma: Volatility
        """
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
    
    def _compute_d1_d2(self, S: float) -> Tuple[float, float]:
        """Compute d1 and d2 from Black-Scholes formula."""
        d1 = (np.log(S / self.K) + (self.r + 0.5 * self.sigma**2) * self.T) / (
            self.sigma * np.sqrt(self.T)
        )
        d2 = d1 - self.sigma * np.sqrt(self.T)
        return d1, d2
    
    def call_price(self, S: float) -> float:
        """Compute call option price."""
        d1, d2 = self._compute_d1_d2(S)
        return S * norm.cdf(d1) - self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
    
    def put_price(self, S: float) -> float:
        """Compute put option price."""
        d1, d2 = self._compute_d1_d2(S)
        return self.K * np.exp(-self.r * self.T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    
    def delta_call(self, S: float) -> float:
        """Delta: ∂C/∂S (sensitivity to spot price)."""
        d1, _ = self._compute_d1_d2(S)
        return norm.cdf(d1)
    
    def delta_put(self, S: float) -> float:
        """Delta for put option."""
        d1, _ = self._compute_d1_d2(S)
        return norm.cdf(d1) - 1
    
    def gamma(self, S: float) -> float:
        """Gamma: ∂²C/∂S² (convexity, second derivative)."""
        if S <= 0:
            return 0
        d1, _ = self._compute_d1_d2(S)
        return norm.pdf(d1) / (S * self.sigma * np.sqrt(self.T))
    
    def vega(self, S: float) -> float:
        """Vega: ∂C/∂σ (sensitivity to volatility). Per 1% change."""
        d1, _ = self._compute_d1_d2(S)
        return S * norm.pdf(d1) * np.sqrt(self.T) / 100  # Per 1% change
    
    def theta_call(self, S: float) -> float:
        """Theta for call: -∂C/∂t (time decay). Per day."""
        d1, d2 = self._compute_d1_d2(S)
        term1 = -S * norm.pdf(d1) * self.sigma / (2 * np.sqrt(self.T))
        term2 = -self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(d2)
        return (term1 + term2) / 365  # Per day
    
    def theta_put(self, S: float) -> float:
        """Theta for put: -∂P/∂t (time decay). Per day."""
        d1, d2 = self._compute_d1_d2(S)
        term1 = -S * norm.pdf(d1) * self.sigma / (2 * np.sqrt(self.T))
        term2 = self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(-d2)
        return (term1 + term2) / 365  # Per day
    
    def rho_call(self, S: float) -> float:
        """Rho for call: ∂C/∂r (sensitivity to interest rates). Per 1% change."""
        _, d2 = self._compute_d1_d2(S)
        return self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(d2) / 100
    
    def rho_put(self, S: float) -> float:
        """Rho for put: ∂P/∂r (sensitivity to interest rates). Per 1% change."""
        _, d2 = self._compute_d1_d2(S)
        return -self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(-d2) / 100
    
    def all_greeks_call(self, S: float) -> Dict[str, float]:
        """Compute all Greeks for a call option."""
        return {
            "price": self.call_price(S),
            "delta": self.delta_call(S),
            "gamma": self.gamma(S),
            "vega": self.vega(S),
            "theta": self.theta_call(S),
            "rho": self.rho_call(S)
        }
    
    def all_greeks_put(self, S: float) -> Dict[str, float]:
        """Compute all Greeks for a put option."""
        return {
            "price": self.put_price(S),
            "delta": self.delta_put(S),
            "gamma": self.gamma(S),
            "vega": self.vega(S),
            "theta": self.theta_put(S),
            "rho": self.rho_put(S)
        }


def plot_greeks(
    K: float = 100,
    T: float = 1.0,
    r: float = 0.05,
    sigma: float = 0.2,
    spot_range: Tuple[float, float] = (70, 130),
    option_type: str = "call"
) -> None:
    """
    Plot Greeks across spot price range.
    
    Args:
        K: Strike price
        T: Time to maturity
        r: Risk-free rate
        sigma: Volatility
        spot_range: Range of spot prices for x-axis
        option_type: "call" or "put"
    """
    calc = GreeksCalculator(K, T, r, sigma)
    spots = np.linspace(spot_range[0], spot_range[1], 100)
    
    # Compute Greeks
    if option_type == "call":
        prices = [calc.call_price(S) for S in spots]
        deltas = [calc.delta_call(S) for S in spots]
        all_greeks = [calc.all_greeks_call(S) for S in spots]
    else:
        prices = [calc.put_price(S) for S in spots]
        deltas = [calc.delta_put(S) for S in spots]
        all_greeks = [calc.all_greeks_put(S) for S in spots]
    
    gammas = [g["gamma"] for g in all_greeks]
    vegas = [g["vega"] for g in all_greeks]
    thetas = [g["theta"] for g in all_greeks]
    rhos = [g["rho"] for g in all_greeks]
    
    # Create figure with subplots
    fig, axes = plt.subplots(3, 2, figsize=(14, 10))
    fig.suptitle(f"Black-Scholes Greeks - {option_type.upper()} Option", fontsize=14)
    
    # Price
    axes[0, 0].plot(spots, prices, 'b-', linewidth=2)
    axes[0, 0].axvline(K, color='r', linestyle='--', alpha=0.5, label='Strike')
    axes[0, 0].set_ylabel('Price')
    axes[0, 0].set_title('Option Price')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].legend()
    
    # Delta
    axes[0, 1].plot(spots, deltas, 'g-', linewidth=2)
    axes[0, 1].axvline(K, color='r', linestyle='--', alpha=0.5, label='Strike')
    axes[0, 1].axhline(0.5, color='k', linestyle=':', alpha=0.3)
    axes[0, 1].set_ylabel('Delta')
    axes[0, 1].set_title('Delta (∂P/∂S)')
    axes[0, 1].grid(True, alpha=0.3)
    axes[0, 1].legend()
    
    # Gamma
    axes[1, 0].plot(spots, gammas, 'r-', linewidth=2)
    axes[1, 0].axvline(K, color='r', linestyle='--', alpha=0.5, label='Strike')
    axes[1, 0].set_ylabel('Gamma')
    axes[1, 0].set_title('Gamma (∂²P/∂S²)')
    axes[1, 0].grid(True, alpha=0.3)
    axes[1, 0].legend()
    
    # Vega
    axes[1, 1].plot(spots, vegas, 'm-', linewidth=2)
    axes[1, 1].axvline(K, color='r', linestyle='--', alpha=0.5, label='Strike')
    axes[1, 1].set_ylabel('Vega')
    axes[1, 1].set_title('Vega (∂P/∂σ per 1%)')
    axes[1, 1].grid(True, alpha=0.3)
    axes[1, 1].legend()
    
    # Theta
    axes[2, 0].plot(spots, thetas, 'c-', linewidth=2)
    axes[2, 0].axvline(K, color='r', linestyle='--', alpha=0.5, label='Strike')
    axes[2, 0].set_xlabel('Spot Price')
    axes[2, 0].set_ylabel('Theta')
    axes[2, 0].set_title('Theta (time decay per day)')
    axes[2, 0].grid(True, alpha=0.3)
    axes[2, 0].legend()
    
    # Rho
    axes[2, 1].plot(spots, rhos, 'orange', linewidth=2)
    axes[2, 1].axvline(K, color='r', linestyle='--', alpha=0.5, label='Strike')
    axes[2, 1].set_xlabel('Spot Price')
    axes[2, 1].set_ylabel('Rho')
    axes[2, 1].set_title('Rho (∂P/∂r per 1%)')
    axes[2, 1].grid(True, alpha=0.3)
    axes[2, 1].legend()
    
    plt.tight_layout()
    return fig


def print_greeks_table(
    K: float = 100,
    T: float = 1.0,
    r: float = 0.05,
    sigma: float = 0.2,
    spot_values: list = None
) -> None:
    """Print Greeks for selected spot prices."""
    if spot_values is None:
        spot_values = [90, 95, 100, 105, 110]
    
    calc = GreeksCalculator(K, T, r, sigma)
    
    print("Black-Scholes Greeks Analysis")
    print("=" * 80)
    print(f"Strike: {K}, Maturity: {T}, Rate: {r}, Volatility: {sigma}")
    print("\nCALL OPTIONS:")
    print(f"{'Spot':<8} {'Price':<10} {'Delta':<10} {'Gamma':<10} {'Vega':<10} {'Theta':<10} {'Rho':<10}")
    print("-" * 80)
    
    for S in spot_values:
        greeks = calc.all_greeks_call(S)
        print(f"{S:<8.2f} {greeks['price']:<10.4f} {greeks['delta']:<10.4f} "
              f"{greeks['gamma']:<10.6f} {greeks['vega']:<10.4f} {greeks['theta']:<10.4f} {greeks['rho']:<10.4f}")
    
    print("\nPUT OPTIONS:")
    print(f"{'Spot':<8} {'Price':<10} {'Delta':<10} {'Gamma':<10} {'Vega':<10} {'Theta':<10} {'Rho':<10}")
    print("-" * 80)
    
    for S in spot_values:
        greeks = calc.all_greeks_put(S)
        print(f"{S:<8.2f} {greeks['price']:<10.4f} {greeks['delta']:<10.4f} "
              f"{greeks['gamma']:<10.6f} {greeks['vega']:<10.4f} {greeks['theta']:<10.4f} {greeks['rho']:<10.4f}")


if __name__ == "__main__":
    print_greeks_table()
    print("\n(For visualization, run plot_greeks() to display matplotlib figures)")
