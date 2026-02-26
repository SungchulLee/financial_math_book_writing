# american_bermudan_exercise.py
"""
American and Bermudan Exercise on Binomial/Trinomial Tree.

This module implements binomial and trinomial trees with American and
Bermudan early exercise features for interest rate derivatives and equity
options. Hull-White trinomial trees are demonstrated for rates.
"""

import numpy as np
from typing import List, Tuple, Dict


class BinomialTree:
    """Binomial tree for option pricing with early exercise."""
    
    def __init__(self, S0: float, r: float, sigma: float, T: float, N: int):
        """
        Initialize binomial tree.
        
        Args:
            S0: Initial spot price
            r: Risk-free rate
            sigma: Volatility
            T: Time to maturity
            N: Number of steps
        """
        self.S0 = S0
        self.r = r
        self.sigma = sigma
        self.T = T
        self.N = N
        self.dt = T / N
        
        # Up and down factors
        self.u = np.exp(sigma * np.sqrt(self.dt))
        self.d = 1 / self.u
        
        # Risk-neutral probability
        self.p = (np.exp(r * self.dt) - self.d) / (self.u - self.d)
    
    def american_option_price(
        self,
        K: float,
        option_type: str = "put"
    ) -> Tuple[float, np.ndarray]:
        """
        Price American option with early exercise.
        
        Args:
            K: Strike price
            option_type: "call" or "put"
        
        Returns:
            Tuple of (option_price, exercise_nodes)
        """
        # Initialize tree for terminal payoffs
        node_values = np.zeros((self.N + 1, self.N + 1))
        exercise_nodes = np.zeros((self.N + 1, self.N + 1), dtype=bool)
        
        # Terminal payoffs at maturity
        for j in range(self.N + 1):
            S_T = self.S0 * (self.u ** (self.N - j)) * (self.d ** j)
            
            if option_type == "call":
                node_values[self.N, j] = max(S_T - K, 0)
            else:  # put
                node_values[self.N, j] = max(K - S_T, 0)
            
            if node_values[self.N, j] > 0:
                exercise_nodes[self.N, j] = True
        
        # Backward induction
        discount_factor = np.exp(-self.r * self.dt)
        
        for i in range(self.N - 1, -1, -1):
            for j in range(i + 1):
                # Current spot price at this node
                S_t = self.S0 * (self.u ** (i - j)) * (self.d ** j)
                
                # Continuation value (expected value of future cash flows)
                continuation = discount_factor * (
                    self.p * node_values[i + 1, j] +
                    (1 - self.p) * node_values[i + 1, j + 1]
                )
                
                # Intrinsic value (immediate exercise)
                if option_type == "call":
                    intrinsic = max(S_t - K, 0)
                else:  # put
                    intrinsic = max(K - S_t, 0)
                
                # American: take maximum (early exercise allowed)
                node_values[i, j] = max(continuation, intrinsic)
                
                # Mark as early exercise node if intrinsic > continuation
                if intrinsic > continuation and intrinsic > 0:
                    exercise_nodes[i, j] = True
        
        return node_values[0, 0], exercise_nodes
    
    def european_option_price(
        self,
        K: float,
        option_type: str = "put"
    ) -> float:
        """
        Price European option (no early exercise).
        
        Args:
            K: Strike price
            option_type: "call" or "put"
        
        Returns:
            Option price
        """
        # Terminal payoffs
        node_values = np.zeros(self.N + 1)
        
        for j in range(self.N + 1):
            S_T = self.S0 * (self.u ** (self.N - j)) * (self.d ** j)
            
            if option_type == "call":
                node_values[j] = max(S_T - K, 0)
            else:
                node_values[j] = max(K - S_T, 0)
        
        # Backward induction (no early exercise)
        discount_factor = np.exp(-self.r * self.dt)
        
        for i in range(self.N - 1, -1, -1):
            for j in range(i + 1):
                node_values[j] = discount_factor * (
                    self.p * node_values[j] +
                    (1 - self.p) * node_values[j + 1]
                )
        
        return node_values[0]


class TrinomialTree:
    """Trinomial tree with three branches per node."""
    
    def __init__(self, S0: float, r: float, sigma: float, T: float, N: int):
        """
        Initialize trinomial tree.
        
        Args:
            S0: Initial spot price
            r: Risk-free rate
            sigma: Volatility
            T: Time to maturity
            N: Number of steps
        """
        self.S0 = S0
        self.r = r
        self.sigma = sigma
        self.T = T
        self.N = N
        self.dt = T / N
        
        # Tree parameters (Boyle's parameterization)
        self.u = np.exp(sigma * np.sqrt(2 * self.dt))
        self.d = 1 / self.u
        self.m = 1.0  # Middle factor
        
        # Risk-neutral probabilities
        self.pu, self.pm, self.pd = self._compute_probabilities()
    
    def _compute_probabilities(self) -> Tuple[float, float, float]:
        """Compute risk-neutral probabilities for trinomial tree."""
        lambda_param = (self.sigma * np.sqrt(self.dt))**2 / 2
        
        pu = (1.0 / (2 * lambda_param**2)) * (
            (np.exp(self.r * self.dt) - np.exp(-self.sigma * np.sqrt(2 * self.dt) * self.dt)) *
            (np.exp(self.sigma * np.sqrt(2 * self.dt) * self.dt) - 1)
        )
        pd = (1.0 / (2 * lambda_param**2)) * (
            (np.exp(self.sigma * np.sqrt(2 * self.dt) * self.dt) - np.exp(self.r * self.dt)) *
            (1 - np.exp(-self.sigma * np.sqrt(2 * self.dt) * self.dt))
        )
        pm = 1 - pu - pd
        
        # Simplified approximation
        pu = (1.0 / 6.0) * (lambda_param + 0.5)
        pd = (1.0 / 6.0) * (lambda_param + 0.5)
        pm = 1 - 2 * pd
        
        return pu, pm, pd
    
    def bermudan_option_price(
        self,
        K: float,
        exercise_dates: List[int],
        option_type: str = "put"
    ) -> float:
        """
        Price Bermudan option with discrete exercise dates.
        
        Args:
            K: Strike price
            exercise_dates: List of node indices where exercise allowed (0 to N)
            option_type: "call" or "put"
        
        Returns:
            Option price
        """
        # Build tree: at step i, we have -i to i middle positions
        # Indexed as node_values[i][j] where j ranges over all states
        
        node_values = {}
        
        # Terminal values at maturity
        for j in range(-self.N, self.N + 1):
            S_T = self.S0 * (self.u ** j)
            
            if option_type == "call":
                payoff = max(S_T - K, 0)
            else:
                payoff = max(K - S_T, 0)
            
            node_values[(self.N, j)] = payoff
        
        # Backward induction
        discount_factor = np.exp(-self.r * self.dt)
        
        for i in range(self.N - 1, -1, -1):
            for j in range(-i, i + 1):
                S_t = self.S0 * (self.u ** j)
                
                # Continuation value
                continuation = discount_factor * (
                    self.pu * node_values.get((i + 1, j + 1), 0) +
                    self.pm * node_values.get((i + 1, j), 0) +
                    self.pd * node_values.get((i + 1, j - 1), 0)
                )
                
                # Intrinsic value
                if option_type == "call":
                    intrinsic = max(S_t - K, 0)
                else:
                    intrinsic = max(K - S_t, 0)
                
                # Check if exercise allowed at this node
                if i in exercise_dates:
                    node_values[(i, j)] = max(continuation, intrinsic)
                else:
                    node_values[(i, j)] = continuation
        
        return node_values[(0, 0)]


def compare_american_european():
    """Compare American and European option prices."""
    S0, K, r, sigma, T = 100, 100, 0.05, 0.2, 1.0
    N = 100
    
    # Binomial tree
    tree = BinomialTree(S0, r, sigma, T, N)
    
    american_put = tree.american_option_price(K, "put")[0]
    european_put = tree.european_option_price(K, "put")
    
    american_call = tree.american_option_price(K, "call")[0]
    european_call = tree.european_option_price(K, "call")
    
    print("American vs European Option Pricing")
    print("=" * 60)
    print(f"Parameters: S0={S0}, K={K}, r={r}, σ={sigma}, T={T}")
    print(f"\nPut Options:")
    print(f"  European: {european_put:.6f}")
    print(f"  American: {american_put:.6f}")
    print(f"  Early Exercise Value: {american_put - european_put:.6f}")
    
    print(f"\nCall Options:")
    print(f"  European: {european_call:.6f}")
    print(f"  American: {american_call:.6f}")
    print(f"  Early Exercise Value: {american_call - european_call:.6f}")


def bermudan_example():
    """Example Bermudan option pricing."""
    S0, K, r, sigma, T = 100, 100, 0.05, 0.2, 1.0
    N = 50
    
    tree = TrinomialTree(S0, r, sigma, T, N)
    
    # Exercise allowed at annual dates
    exercise_dates = [0, N // 4, N // 2, 3 * N // 4, N]
    
    bermudan_price = tree.bermudan_option_price(K, exercise_dates, "put")
    
    print(f"\nBermudan Put Option: {bermudan_price:.6f}")
    print(f"Exercise dates: steps {exercise_dates}")


if __name__ == "__main__":
    compare_american_european()
    bermudan_example()
