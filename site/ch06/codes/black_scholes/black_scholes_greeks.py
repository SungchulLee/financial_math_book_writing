# ============================================================================
# black_scholes/black_scholes_greeks.py
# ============================================================================
"""
Greeks calculation (Delta, Gamma, Theta, etc.)
UNCHANGED API - improved internal implementation using utility functions.
"""

from .black_scholes_base import BlackScholesBase
from .black_scholes_utils import delta, gamma, vega, theta, rho

class BlackScholesGreeks(BlackScholesBase):
    """
    Greeks calculation for Black-Scholes options.
    API UNCHANGED - now delegates to utility functions.
    """
    
    def delta(self):
        """
        Calculate delta for call and put options.
        UNCHANGED API - now delegates to utility function.
        """
        return delta(self.S0, self.K, self.T, self.r, self.sigma, self.q)
    
    def gamma(self):
        """
        Calculate gamma (same for calls and puts).
        UNCHANGED API - now delegates to utility function.
        """
        return gamma(self.S0, self.K, self.T, self.r, self.sigma, self.q)
    
    def vega(self):
        """
        Calculate vega (same for calls and puts).
        UNCHANGED API - now delegates to utility function.
        """
        return vega(self.S0, self.K, self.T, self.r, self.sigma, self.q)
    
    def theta(self):
        """
        Calculate theta for call and put options.
        UNCHANGED API - now delegates to utility function.
        """
        return theta(self.S0, self.K, self.T, self.r, self.sigma, self.q)
    
    def rho(self):
        """
        Calculate rho for call and put options.
        UNCHANGED API - now delegates to utility function.
        """
        return rho(self.S0, self.K, self.T, self.r, self.sigma, self.q)