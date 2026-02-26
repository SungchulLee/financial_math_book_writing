# ============================================================================
# black_scholes_IMPLIED_VOLATILITY_ 4_CUSTOM_ANALYSIS_AND_FILTERING.py 
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
bs.compute_implied_volatilities_and_summarize(model, print_summary=False)
    
print(f"🔍 Custom Filtering Examples:")
    
# High volatility options
high_vol = model.filter_options(min_vol=0.4, max_ttm=0.5)
print(f"   📈 High volatility options (>40%, <6mo): {len(high_vol)}")
    
# ATM options
atm_options = model.filter_options(min_moneyness=0.95, max_moneyness=1.05)
print(f"   🎯 ATM options (95-105% moneyness): {len(atm_options)}")
    
# Short-term options
short_term = model.filter_options(max_ttm=0.25)
print(f"   ⏰ Short-term options (<3mo): {len(short_term)}")
    
# Custom analysis on filtered data
if len(atm_options) > 0:
    atm_vol_mean = atm_options['IMP_VOL'].mean()
    print(f"   📊 ATM average volatility: {atm_vol_mean:.4f}")