# ============================================================================
# black_scholes_IMPLIED_VOLATILITY_ 3_COMPREHENSIVE_WORKFLOW.py 
# ============================================================================
import black_scholes as bs
    
# Initialize model
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
    
# Compute implied volatilities
bs.compute_implied_volatilities_and_summarize(model, sigma_0=2.0, print_summary=False)
    
# Use the built-in comprehensive analysis
results = model.run_full_analysis(
    create_plots=True,
    save_results=True,
    results_dir="./data/comprehensive_unified"
)
        
print(f"✅ Comprehensive analysis completed!")
print(f"📁 Results saved to: ./data/comprehensive_unified/")
        
# Show summary of what was generated
print(f"\n📋 Generated Results:")
for key, value in results.items():
    if hasattr(value, 'shape'):  # DataFrame
        print(f"   📊 {key}: {value.shape} data")
    elif isinstance(value, dict):
        print(f"   📋 {key}: {len(value)} metrics")
    elif value is not None:
        print(f"   ✅ {key}: Generated")