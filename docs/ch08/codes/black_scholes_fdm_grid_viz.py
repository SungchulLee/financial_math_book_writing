# ============================================================================
# black_scholes_FINITE_DIFFERENCE_GRID_VISUALIZATION.py
# ============================================================================
import black_scholes as bs
    
# Model parameters
S0 = 100      # Current stock price
K = 105       # Strike price
T = 0.25      # 3 months to expiration
r = 0.05      # 5% risk-free rate
sigma = 0.2   # 20% volatility
q = 0.02      # 2% dividend yield
mu = 0.1
    
bs.BlackScholes(S0=S0, K=K, T=T, r=r, sigma=sigma, q=q).plot_finite_difference_grid(M=8, N=6)