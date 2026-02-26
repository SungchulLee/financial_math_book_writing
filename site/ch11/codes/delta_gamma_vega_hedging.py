# delta_gamma_vega_hedging.py
"""
Delta-Gamma-Vega Hedging Simulation.

This module implements multi-greek hedging strategies that simultaneously hedge
delta (directional risk), gamma (convexity), and vega (volatility risk).

Realistic hedging requires managing multiple Greeks, not just delta.
"""

import numpy as np
import pandas as pd
from typing import Dict, Tuple, List
from scipy.stats import norm


class MultiGreekHedger:
    """Portfolio hedging with delta, gamma, and vega constraints."""
    
    def __init__(self, S0: float, K_option: float, T: float, r: float, sigma: float):
        """
        Initialize hedging portfolio.
        
        Args:
            S0: Initial spot price
            K_option: Option strike to hedge
            T: Time to maturity
            r: Risk-free rate
            sigma: Volatility
        """
        self.S0 = S0
        self.K_option = K_option
        self.T = T
        self.r = r
        self.sigma = sigma
        
        # Hedge instruments: spot, call, put
        self.K_call_hedge = S0  # ATM call
        self.K_put_hedge = S0   # ATM put
    
    def _compute_d1_d2(self, S: float, K: float, T: float) -> Tuple[float, float]:
        """Compute d1, d2 for Black-Scholes."""
        d1 = (np.log(S / K) + (self.r + 0.5 * self.sigma**2) * T) / (
            self.sigma * np.sqrt(T)
        )
        d2 = d1 - self.sigma * np.sqrt(T)
        return d1, d2
    
    def get_greeks(self, S: float, K: float, T: float, position: str = "long") -> Dict:
        """
        Compute Greeks for an option position.
        
        Args:
            S: Current spot price
            K: Option strike
            T: Time to maturity
            position: "long" (bought) or "short" (sold)
        
        Returns:
            Dictionary with delta, gamma, vega
        """
        d1, d2 = self._compute_d1_d2(S, K, T)
        
        delta = norm.cdf(d1)
        gamma = norm.pdf(d1) / (S * self.sigma * np.sqrt(T)) if S > 0 else 0
        vega = S * norm.pdf(d1) * np.sqrt(T) / 100  # Per 1% vol change
        
        if position == "short":
            delta = -delta
            gamma = -gamma
            vega = -vega
        
        return {"delta": delta, "gamma": gamma, "vega": vega}
    
    def construct_hedge(
        self,
        S: float,
        position: str = "long",
        target_delta: float = 0.0,
        target_gamma: float = 0.0,
        target_vega: float = 0.0
    ) -> Dict[str, float]:
        """
        Construct hedge portfolio to neutralize Greeks.
        
        Uses spot (delta only), call (positive gamma/vega), and put (positive gamma/vega)
        to hedge a short option position.
        
        Args:
            S: Current spot price
            position: "long" (short option, long hedge) or "short" (long option, short hedge)
            target_delta/gamma/vega: Target Greeks to achieve
        
        Returns:
            Dictionary with quantities: {'spot': x, 'call': y, 'put': z}
        """
        # Greeks for each instrument at current S
        greeks_spot = {"delta": 1, "gamma": 0, "vega": 0}
        greeks_call = self.get_greeks(S, self.K_call_hedge, self.T, position="long")
        greeks_put = self.get_greeks(S, self.K_put_hedge, self.T, position="long")
        
        # System: Ax = b where x = [n_spot, n_call, n_put]
        # A = [[Δ_spot, Δ_call, Δ_put],
        #      [Γ_spot, Γ_call, Γ_put],
        #      [V_spot, V_call, V_put]]
        A = np.array([
            [greeks_spot["delta"], greeks_call["delta"], greeks_put["delta"]],
            [greeks_spot["gamma"], greeks_call["gamma"], greeks_put["gamma"]],
            [greeks_spot["vega"], greeks_call["vega"], greeks_put["vega"]]
        ])
        
        b = np.array([target_delta, target_gamma, target_vega])
        
        try:
            x = np.linalg.solve(A, b)
            return {
                "spot": x[0],
                "call": x[1],
                "put": x[2]
            }
        except np.linalg.LinAlgError:
            # If system singular, use least-squares approximation
            x, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
            return {
                "spot": x[0],
                "call": x[1],
                "put": x[2]
            }
    
    def portfolio_greeks(
        self,
        S: float,
        positions: Dict[str, float]
    ) -> Dict[str, float]:
        """
        Compute total Greeks for a portfolio.
        
        Args:
            S: Current spot price
            positions: Dictionary with keys 'option', 'spot', 'call', 'put'
                      and quantities (negative = short)
        
        Returns:
            Dictionary with total delta, gamma, vega
        """
        total_greeks = {"delta": 0, "gamma": 0, "vega": 0}
        
        # Option position
        if "option" in positions:
            greeks_opt = self.get_greeks(S, self.K_option, self.T, "long")
            for greek in total_greeks:
                total_greeks[greek] += positions["option"] * greeks_opt[greek]
        
        # Spot position
        if "spot" in positions:
            total_greeks["delta"] += positions["spot"]
        
        # Call hedge
        if "call" in positions:
            greeks_call = self.get_greeks(S, self.K_call_hedge, self.T, "long")
            for greek in total_greeks:
                total_greeks[greek] += positions["call"] * greeks_call[greek]
        
        # Put hedge
        if "put" in positions:
            greeks_put = self.get_greeks(S, self.K_put_hedge, self.T, "long")
            for greek in total_greeks:
                total_greeks[greek] += positions["put"] * greeks_put[greek]
        
        return total_greeks
    
    def simulate_p_and_l(
        self,
        initial_S: float,
        positions: Dict[str, float],
        spot_scenarios: np.ndarray,
        vol_changes: np.ndarray = None,
        time_decay: float = 1/252  # One trading day
    ) -> Tuple[np.ndarray, pd.DataFrame]:
        """
        Simulate P&L across spot and volatility scenarios.
        
        Args:
            initial_S: Initial spot price
            positions: Dictionary with quantities
            spot_scenarios: Array of spot prices to test
            vol_changes: Array of volatility changes (in percent)
            time_decay: Time decay in years (default 1 day)
        
        Returns:
            Tuple of (pnl_array, summary_df)
        """
        if vol_changes is None:
            vol_changes = np.array([-1, 0, 1])  # -1%, 0%, +1% vol changes
        
        # Compute initial portfolio Greeks at spot 0 (reference)
        initial_greeks = self.portfolio_greeks(initial_S, positions)
        
        pnl_matrix = np.zeros((len(spot_scenarios), len(vol_changes)))
        
        for i, S_new in enumerate(spot_scenarios):
            for j, vol_change in enumerate(vol_changes):
                dS = S_new - initial_S
                sigma_new = self.sigma + vol_change / 100
                
                # Taylor expansion: P&L ≈ Δ·dS + 0.5·Γ·dS² + V·dσ - Θ·dt
                greeks = self.portfolio_greeks(initial_S, positions)
                
                delta_pnl = greeks["delta"] * dS
                gamma_pnl = 0.5 * greeks["gamma"] * dS**2
                vega_pnl = greeks["vega"] * vol_change  # vol_change in percent
                
                # Simplified theta (ignored for brevity)
                pnl = delta_pnl + gamma_pnl + vega_pnl
                pnl_matrix[i, j] = pnl
        
        # Create summary dataframe
        summary_data = {
            'Spot': spot_scenarios,
        }
        for j, vol_change in enumerate(vol_changes):
            summary_data[f'Vol {vol_change:+.0f}%'] = pnl_matrix[:, j]
        
        df = pd.DataFrame(summary_data)
        return pnl_matrix, df
    
    def compute_hedge_effectiveness(
        self,
        S_initial: float,
        positions_unhedged: Dict[str, float],
        positions_hedged: Dict[str, float],
        scenarios: List[Tuple[float, float]]  # (spot, vol_change_pct)
    ) -> Dict:
        """
        Compare P&L variance between hedged and unhedged portfolios.
        
        Args:
            S_initial: Initial spot
            positions_unhedged: Unhedged portfolio
            positions_hedged: Hedged portfolio
            scenarios: List of (S_new, vol_change) scenarios
        
        Returns:
            Dictionary with variance reduction metrics
        """
        pnl_unhedged = []
        pnl_hedged = []
        
        for S_new, vol_change in scenarios:
            # Compute Greeks at initial spot
            dS = S_new - S_initial
            
            # Unhedged
            greeks_uh = self.portfolio_greeks(S_initial, positions_unhedged)
            pnl_uh = (greeks_uh["delta"] * dS + 
                     0.5 * greeks_uh["gamma"] * dS**2 + 
                     greeks_uh["vega"] * vol_change)
            pnl_unhedged.append(pnl_uh)
            
            # Hedged
            greeks_h = self.portfolio_greeks(S_initial, positions_hedged)
            pnl_h = (greeks_h["delta"] * dS + 
                    0.5 * greeks_h["gamma"] * dS**2 + 
                    greeks_h["vega"] * vol_change)
            pnl_hedged.append(pnl_h)
        
        pnl_unhedged = np.array(pnl_unhedged)
        pnl_hedged = np.array(pnl_hedged)
        
        var_reduction = 1 - (np.var(pnl_hedged) / np.var(pnl_unhedged))
        
        return {
            "unhedged_var": np.var(pnl_unhedged),
            "hedged_var": np.var(pnl_hedged),
            "variance_reduction": var_reduction,
            "unhedged_mean_pnl": np.mean(pnl_unhedged),
            "hedged_mean_pnl": np.mean(pnl_hedged)
        }


def example_delta_gamma_vega_hedge():
    """Example: hedge a short call position."""
    hedger = MultiGreekHedger(S0=100, K_option=100, T=0.25, r=0.05, sigma=0.20)
    
    # Short 1 call option
    positions_unhedged = {
        "option": -1,  # Short
        "spot": 0,
        "call": 0,
        "put": 0
    }
    
    print("Multi-Greek Hedging Example")
    print("=" * 60)
    print("\nUnhedged Position (short 1 call at-the-money):")
    greeks_unhedged = hedger.portfolio_greeks(100, positions_unhedged)
    print(f"  Delta: {greeks_unhedged['delta']:.4f}")
    print(f"  Gamma: {greeks_unhedged['gamma']:.6f}")
    print(f"  Vega:  {greeks_unhedged['vega']:.4f}")
    
    # Construct hedge
    hedge_positions = hedger.construct_hedge(100, "short")
    print(f"\nHedge Portfolio:")
    print(f"  Spot:  {hedge_positions['spot']:.4f} shares")
    print(f"  Call:  {hedge_positions['call']:.4f} contracts")
    print(f"  Put:   {hedge_positions['put']:.4f} contracts")
    
    # Hedged position
    positions_hedged = {
        "option": -1,
        "spot": hedge_positions["spot"],
        "call": hedge_positions["call"],
        "put": hedge_positions["put"]
    }
    
    print("\nHedged Position:")
    greeks_hedged = hedger.portfolio_greeks(100, positions_hedged)
    print(f"  Delta: {greeks_hedged['delta']:.4f}")
    print(f"  Gamma: {greeks_hedged['gamma']:.6f}")
    print(f"  Vega:  {greeks_hedged['vega']:.4f}")
    
    # P&L scenarios
    spots = np.linspace(90, 110, 21)
    vol_changes = np.array([-2, -1, 0, 1, 2])
    
    pnl, df = hedger.simulate_p_and_l(100, positions_hedged, spots, vol_changes)
    print("\nP&L at different spot/vol levels (hedged):")
    print(df.to_string(index=False))


if __name__ == "__main__":
    example_delta_gamma_vega_hedge()
