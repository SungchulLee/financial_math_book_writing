# ============================================================================
# black_scholes_GEOMETRIC_BROWNIAN_MOTION.py
# ============================================================================
import black_scholes as bs

# Model parameters
S0 = 100      # Current stock price
K = 105       # Strike price
T = 1         # 1 year to expiration
r = 0.05      # 5% risk-free rate
sigma = 0.2   # 20% volatility
q = 0.02      # 2% dividend yield
    
# Create the unified Black-Scholes interface
bs_model = bs.BlackScholes(S0=S0, K=K, T=T, r=r, sigma=sigma, q=q)

# risk neutral path simulation and visualization 
bs_model.plot_paths_and_histogram(
    num_paths=1000, 
    max_paths_display=50, 
    seed=42, 
    title=f'Sample GBM Paths with Final Price Distribution\nunder Risk Neutral Measure r = {r}'
    )
    
# risk neutral vs real world path simulation and visualization 
mu = 0.08  # 8% real-world drift
bs_model.plot_gbm_comparison(
    num_paths=1000, 
    max_paths_display=50, 
    seed=42, 
    mu=mu
    )