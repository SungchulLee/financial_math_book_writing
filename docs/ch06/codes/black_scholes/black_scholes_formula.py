# ============================================================================
# black_scholes/black_scholes_formula.py
# ============================================================================
"""
Analytical BS formulas and option pricing.
UNCHANGED API - improved internal implementation using utility functions.
"""

from .black_scholes_base import BlackScholesBase
from .black_scholes_utils import bs_call_price, bs_put_price

class BlackScholesFormula(BlackScholesBase):
    """
    Analytical Black-Scholes formula implementation.
    API UNCHANGED - delegates to utility functions for consistency.
    """
    
    def price(self):
        """
        Calculate call and put option prices.
        UNCHANGED API - now delegates to utility functions.
        """
        return (
            bs_call_price(self.S0, self.K, self.T, self.r, self.sigma, self.q),
            bs_put_price(self.S0, self.K, self.T, self.r, self.sigma, self.q)
        )