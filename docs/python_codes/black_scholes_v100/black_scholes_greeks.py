# ============================================================================
# black_scholes/black_scholes_greeks.py
# ============================================================================
from .black_scholes_base import BlackScholesBase
from .black_scholes_utils import delta, gamma, vega

class BlackScholesGreeks(BlackScholesBase):
    def delta(self):
        return delta(self.S0, self.K, self.T, self.r, self.sigma, self.q)

    def gamma(self):
        return gamma(self.S0, self.K, self.T, self.r, self.sigma, self.q)

    def vega(self):
        return vega(self.S0, self.K, self.T, self.r, self.sigma, self.q)