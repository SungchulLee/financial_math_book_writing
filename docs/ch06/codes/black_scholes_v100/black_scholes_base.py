# ============================================================================
# black_scholes/black_scholes_base.py
# ============================================================================


class BlackScholesBase:
    def __init__(self, S0, K, T, r, sigma, q=0):
        self.S0 = S0        # Initial stock price
        self.K = K          # Strike price
        self.T = T          # Time to maturity (in years)
        self.r = r          # Risk-free interest rate
        self.sigma = sigma  # Volatility of the underlying asset
        self.q = q          # Continuous dividend yield