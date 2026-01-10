# ============================================================================
# black_scholes_IMPLIED_VOLATILITY_ 2_VSTOXX BATCH_ANALYSIS.py 
# ============================================================================
import black_scholes as bs
    
# Initialize for VSTOXX
model = bs.BlackScholesImpliedVol(
        S0=17.6639,  # VSTOXX spot value
        K=18.0,      # Placeholder
        T=0.25,      # Placeholder
        r=0.01,      # Risk-free rate
        sigma=0.2,   # Initial volatility
        tol=0.5      # Moneyness tolerance
    )
    
# Load data 
model.load_data()
    
# Show data summary
data_summary = model.get_data_summary()
print(f"  📊 Total options: {data_summary['total_options']:,}")
print(f"  📅 Unique maturities: {data_summary['unique_maturities']}")
print(f"  💲 Strike range: {data_summary['strike_range']['min']:.1f} - {data_summary['strike_range']['max']:.1f}", end="\n"*2)
    
# Compute implied volatilities
bs.compute_implied_volatilities_and_summarize(model, sigma_0=2.0)
    
# Run advanced analysis
bs.run_advanced_analysis_on_implied_vol(model)