# ============================================================================
# black_scholes_IMPLIED_VOLATILITY_6_FIGURES.py 
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
    
# Load real VSTOXX data (with auto-download if needed)
model.load_data(auto_download=True)  # This will download if file doesn't exist
    
# Compute implied volatilities on real data
model.compute_implied_volatility_batch(sigma_0=2.0)
    
# Get summary statistics
stats = model.get_summary_statistics()
print(f"📊 Results Summary:")
print(f"   ✅ Valid computations: {stats['count']:,}")
print(f"   📈 Mean volatility: {stats['mean']:.4f} ({stats['mean']*100:.2f}%)")
print(f"   📏 Range: {stats['min']:.4f} - {stats['max']:.4f}")
print(f"   📊 Std deviation: {stats['std']:.4f}")
    
# Plot 1: Volatility Smiles (creates its own figure)
model.plot_volatility_smiles("Real VSTOXX Implied Volatility Smiles")
    
# Plot 2: 3D Surface (creates its own figure)
model.plot_3d_surface(
    title="Real VSTOXX - 3D Volatility Surface",
    save_path="./data/real_3d_surface.png"
)
    
# Plot 3: 3D Smiles (creates its own figure)
model.plot_3d_smiles(
    title="Real VSTOXX - 3D Volatility Smiles",
    save_path="./data/real_3d_smiles.png"
)