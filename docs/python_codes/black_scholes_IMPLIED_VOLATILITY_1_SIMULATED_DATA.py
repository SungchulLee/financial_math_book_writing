# ============================================================================
# black_scholes_IMPLIED_VOLATILITY.py 
# ============================================================================
import black_scholes as bs
    
# Create model with synthetic data
model = bs.BlackScholesImpliedVol(S0=100, K=100, T=0.25, r=0.05, sigma=0.2, tol=0.3)
model.create_synthetic_data()
    
# Compute implied volatilities
bs.compute_implied_volatilities_and_summarize(model, sigma_0=2.0)
    
# Run advanced analysis
bs.run_advanced_analysis_on_implied_vol(model)

    
