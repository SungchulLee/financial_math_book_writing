# ============================================================================
# black_scholes_IMPLIED_VOLATILITY_1_SINGLE_OPTION_ANALYSIS.py 
# ============================================================================
import black_scholes as bs

# Initialize for single option
model = bs.BlackScholesImpliedVol(
    S0=100,      # Stock price
    K=105,       # Strike price
    T=0.25,      # 3 months
    r=0.05,      # 5% risk-free rate
    sigma=0.2,   # Initial volatility
    q=0.02       # 2% dividend yield
)
    
# Market price of the option
market_price = 7.5
    
print(f"Option Parameters:")
print(f"  S₀: ${model.S0}, K: ${model.K}, T: {model.T}yr, r: {model.r:.1%}, q: {model.q:.1%}")
print(f"  Market Price: ${market_price}")
    
# Compute implied volatility
implied_vol = model.compute(
    market_price=market_price,
    sigma_0=0.2,
    option_type="call"
)
    
print(f"\n✅ Implied Volatility: {implied_vol:.4f} ({implied_vol*100:.2f}%)")