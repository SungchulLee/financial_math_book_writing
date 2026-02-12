# ============================================================================
# black_scholes/black_scholes_formula.py
# ============================================================================
from .black_scholes_base import BlackScholesBase
from .black_scholes_utils import bs_call_price, bs_put_price

class BlackScholesFormula(BlackScholesBase):
    def price(self):
        return bs_call_price(self.S0, self.K, self.T, self.r, self.sigma, self.q), \
               bs_put_price(self.S0, self.K, self.T, self.r, self.sigma, self.q)