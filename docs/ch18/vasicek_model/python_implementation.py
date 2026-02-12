# python_implementation.py
"""
Vasicek Model Python Implementation.

This module implements the Vasicek model for interest rate modeling,
including bond pricing, simulation, and calibration.

Vasicek Model: dr_t = a(b - r_t)dt + σ dB_t
"""

import numpy as np
from scipy.optimize import minimize
from scipy.special import erf
from typing import Tuple, Dict


class VasicekModel:
    """Vasicek interest rate model."""
    
    def __init__(self, a: float, b: float, sigma: float):
        """
        Initialize Vasicek model parameters.
        
        Args:
            a: Mean reversion speed
            b: Long-run mean level
            sigma: Volatility
        """
        self.a = a
        self.b = b
        self.sigma = sigma
    
    def bond_price(
        self,
        r0: float,
        T: float,
        t: float = 0
    ) -> float:
        """
        Compute zero-coupon bond price P(t, T).
        
        Analytical formula: P(t,T) = A(t,T) * exp(-B(t,T) * r_t)
        
        where:
            B(t,T) = (1 - exp(-a(T-t)))/a
            A(t,T) = exp((b - σ²/(2a²))(B(t,T) - (T-t)) - σ²/(4a)*B(t,T)²)
        
        Args:
            r0: Current short rate
            T: Maturity
            t: Current time
        
        Returns:
            Bond price
        """
        tau = T - t  # Time to maturity
        
        if tau < 1e-10:  # At maturity
            return 1.0
        
        B = (1 - np.exp(-self.a * tau)) / self.a
        
        A_log = (self.b - self.sigma**2 / (2 * self.a**2)) * (
            B - tau
        ) - (self.sigma**2 / (4 * self.a)) * B**2
        A = np.exp(A_log)
        
        price = A * np.exp(-B * r0)
        return price
    
    def forward_rate(
        self,
        r0: float,
        T: float,
        t: float = 0
    ) -> float:
        """
        Compute instantaneous forward rate f(t, T).
        
        f(t,T) = -∂ln(P(t,T))/∂T
        
        Args:
            r0: Current short rate
            T: Forward rate maturity
            t: Current time
        
        Returns:
            Instantaneous forward rate
        """
        tau = T - t
        
        # Forward rate formula
        B = (1 - np.exp(-self.a * tau)) / self.a
        dB = np.exp(-self.a * tau)  # dB/dT
        
        # f = -dln(A)/dT - dB/dT * r
        f_forward = (
            self.b - (self.sigma**2 / (2 * self.a**2)) * dB +
            dB * r0
        )
        
        return f_forward
    
    def bond_price_volatility(
        self,
        T: float,
        t: float = 0
    ) -> float:
        """
        Compute volatility of bond returns.
        
        Volatility(dP/P) = B(t,T) * σ
        
        Args:
            T: Bond maturity
            t: Current time
        
        Returns:
            Bond return volatility
        """
        tau = T - t
        B = (1 - np.exp(-self.a * tau)) / self.a
        return B * self.sigma
    
    def simulate_paths(
        self,
        r0: float,
        T: float,
        num_paths: int = 1000,
        num_steps: int = 100,
        seed: int = None
    ) -> np.ndarray:
        """
        Simulate interest rate paths using Euler discretization.
        
        Args:
            r0: Initial rate
            T: Maturity
            num_paths: Number of paths
            num_steps: Time steps
            seed: Random seed
        
        Returns:
            Array of shape (num_paths, num_steps + 1) with rate paths
        """
        if seed is not None:
            np.random.seed(seed)
        
        dt = T / num_steps
        r_paths = np.zeros((num_paths, num_steps + 1))
        r_paths[:, 0] = r0
        
        for i in range(num_steps):
            dB = np.random.normal(0, np.sqrt(dt), num_paths)
            r_t = r_paths[:, i]
            
            # Euler step: dr = a(b - r)dt + σ dB
            r_paths[:, i + 1] = r_t + self.a * (self.b - r_t) * dt + self.sigma * dB
        
        return r_paths
    
    def bond_option_price(
        self,
        K: float,
        T_option: float,
        T_bond: float,
        r0: float,
        option_type: str = "call"
    ) -> float:
        """
        Price European option on zero-coupon bond.
        
        Analytical formula using Jamshidian's approach.
        
        Args:
            K: Strike price of bond option
            T_option: Option maturity
            T_bond: Bond maturity (T_bond > T_option)
            r0: Current rate
            option_type: "call" or "put"
        
        Returns:
            Option price
        """
        from scipy.stats import norm
        
        # Bond volatility
        tau = T_bond - T_option
        B_bond = (1 - np.exp(-self.a * tau)) / self.a
        sigma_P = B_bond * self.sigma
        
        # Bond price at maturity
        P_T = self.bond_price(r0, T_bond)
        
        # Critical rate (Jamshidian)
        # Solve: P(r*, T_bond) = K
        def bond_price_func(r):
            return self.bond_price(r, T_bond) - K
        
        from scipy.optimize import brentq
        try:
            r_star = brentq(bond_price_func, -0.1, 0.5)
        except:
            r_star = self.b  # Fallback
        
        # Option payoff coefficient
        P_Tstar = self.bond_price(r_star, T_bond)
        
        # d value
        d = (np.log(P_T / P_Tstar) + 0.5 * sigma_P**2 * T_option) / (
            sigma_P * np.sqrt(T_option)
        )
        
        if option_type == "call":
            price = P_T * norm.cdf(d) - K * norm.cdf(d - sigma_P * np.sqrt(T_option))
        else:
            price = K * norm.cdf(-d + sigma_P * np.sqrt(T_option)) - P_T * norm.cdf(-d)
        
        return max(price, 0)
    
    def calibrate_to_bond_prices(
        self,
        maturities: np.ndarray,
        prices: np.ndarray,
        r0: float
    ) -> Dict:
        """
        Calibrate model to observed bond prices.
        
        Args:
            maturities: Array of bond maturities
            prices: Array of observed bond prices
            r0: Current short rate (assumed observable)
        
        Returns:
            Dictionary with calibrated parameters
        """
        def objective(params):
            a, b, sigma = params
            
            # Constraints
            if a <= 0 or sigma <= 0:
                return 1e10
            
            model = VasicekModel(a, b, sigma)
            
            total_error = 0
            for T, price_obs in zip(maturities, prices):
                price_model = model.bond_price(r0, T)
                error = (price_model - price_obs)**2
                total_error += error
            
            return total_error
        
        # Initial guess
        x0 = [0.1, 0.05, 0.01]
        
        result = minimize(
            objective,
            x0,
            method='Nelder-Mead',
            options={'xatol': 1e-8, 'fatol': 1e-8}
        )
        
        a_cal, b_cal, sigma_cal = result.x
        
        return {
            'a': a_cal,
            'b': b_cal,
            'sigma': sigma_cal,
            'error': result.fun,
            'success': result.success
        }
    
    def yield_curve(
        self,
        r0: float,
        maturities: np.ndarray
    ) -> np.ndarray:
        """
        Compute yield curve (spot rates).
        
        y(T) = -ln(P(0,T))/T
        
        Args:
            r0: Current short rate
            maturities: Array of maturities
        
        Returns:
            Array of spot rates
        """
        yields = []
        
        for T in maturities:
            price = self.bond_price(r0, T)
            if price > 0:
                y = -np.log(price) / T
                yields.append(y)
            else:
                yields.append(np.nan)
        
        return np.array(yields)


def example_vasicek():
    """Example Vasicek model computations."""
    # Parameters
    a = 0.2
    b = 0.05
    sigma = 0.02
    
    model = VasicekModel(a, b, sigma)
    
    print("Vasicek Model Example")
    print("=" * 60)
    print(f"Parameters: a={a}, b={b}, σ={sigma}")
    
    # Current rate
    r0 = 0.04
    print(f"\nCurrent short rate: r0 = {r0:.4f}")
    
    # Bond prices
    maturities = np.array([1, 2, 5, 10])
    print("\nBond Prices:")
    print(f"{'Maturity':<12} {'Price':<12} {'Yield':<12}")
    print("-" * 40)
    
    for T in maturities:
        price = model.bond_price(r0, T)
        y = model.yield_curve(r0, np.array([T]))[0]
        print(f"{T:<12.1f} {price:<12.6f} {y:<12.4%}")
    
    # Bond option
    print("\nBond Option Prices:")
    print(f"{'T_opt':<8} {'T_bond':<8} {'Strike':<12} {'Call':<12} {'Put':<12}")
    print("-" * 60)
    
    for T_opt in [1, 2]:
        for T_bond in [5, 10]:
            if T_bond > T_opt:
                K = 0.95
                call = model.bond_option_price(K, T_opt, T_bond, r0, "call")
                put = model.bond_option_price(K, T_opt, T_bond, r0, "put")
                print(f"{T_opt:<8.1f} {T_bond:<8.1f} {K:<12.4f} {call:<12.6f} {put:<12.6f}")
    
    # Simulation
    print("\nSimulation Statistics:")
    paths = model.simulate_paths(r0, T=5, num_paths=10000, num_steps=100)
    print(f"  Mean rate at T=5: {np.mean(paths[:, -1]):.4f}")
    print(f"  Std rate at T=5: {np.std(paths[:, -1]):.4f}")
    print(f"  Min rate at T=5: {np.min(paths[:, -1]):.4f}")
    print(f"  Max rate at T=5: {np.max(paths[:, -1]):.4f}")


if __name__ == "__main__":
    example_vasicek()
