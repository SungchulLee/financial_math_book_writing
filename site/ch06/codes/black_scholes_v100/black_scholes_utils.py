# ============================================================================
# black_scholes/black_scholes_utils.py
# ============================================================================
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import requests
import scipy.stats as stats
from typing import Tuple

def d1_d2(S, K, T, r, sigma, q=0):
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return d1, d2

def bs_call_price(S, K, T, r, sigma, q=0):
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    return S * np.exp(-q * T) * stats.norm.cdf(d1) - K * np.exp(-r * T) * stats.norm.cdf(d2)

def bs_put_price(S, K, T, r, sigma, q=0):
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    return K * np.exp(-r * T) * stats.norm.cdf(-d2) - S * np.exp(-q * T) * stats.norm.cdf(-d1)

def delta(S, K, T, r, sigma, q=0):
    d1, _ = d1_d2(S, K, T, r, sigma, q)
    delta_call = np.exp(-q * T) * stats.norm.cdf(d1)
    delta_put = delta_call - np.exp(-q * T)
    return delta_call, delta_put

def gamma(S, K, T, r, sigma, q=0):
    d1, _ = d1_d2(S, K, T, r, sigma, q)
    return np.exp(-q * T) * stats.norm.pdf(d1) / (S * sigma * np.sqrt(T))

def vega(S, K, T, r, sigma, q=0):
    d1, _ = d1_d2(S, K, T, r, sigma, q)
    return S * np.exp(-q * T) * stats.norm.pdf(d1) * np.sqrt(T)

def theta(S: float, K: float, T: float, r: float, sigma: float, q: float = 0) -> Tuple[float, float]:
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    
    # Common term
    term1 = -S * np.exp(-q * T) * stats.norm.pdf(d1) * sigma / (2 * np.sqrt(T))
    term2_call = -r * K * np.exp(-r * T) * stats.norm.cdf(d2)
    term2_put = r * K * np.exp(-r * T) * stats.norm.cdf(-d2)
    term3 = q * S * np.exp(-q * T)
    
    theta_call = term1 + term2_call - term3 * stats.norm.cdf(d1)
    theta_put = term1 + term2_put + term3 * stats.norm.cdf(-d1)
    
    return theta_call, theta_put

def rho(S: float, K: float, T: float, r: float, sigma: float, q: float = 0) -> Tuple[float, float]:
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    rho_call = K * T * np.exp(-r * T) * stats.norm.cdf(d2)
    rho_put = -K * T * np.exp(-r * T) * stats.norm.cdf(-d2)
    return rho_call, rho_put

def implied_volatility(S0, K, T, r, market_price, sigma_0, q=0, 
                       num_iter=100, option_type="call", tol=1e-6):
    """
    Calculate implied volatility using Newton-Raphson method.
    
    Parameters:
    -----------
    S0 : float
        Current stock price
    K : float
        Strike price
    T : float
        Time to maturity
    r : float
        Risk-free rate
    market_price : float
        Observed market price of the option
    sigma_0 : float
        Initial guess for volatility
    q : float, optional
        Dividend yield (default: 0)
    num_iter : int, optional
        Maximum iterations (default: 100)
    option_type : str, optional
        'call' or 'put' (default: 'call')
    tol : float, optional
        Convergence tolerance (default: 1e-6)
    
    Returns:
    --------
    float : Implied volatility or np.nan if no convergence
    """
    # Newton-Raphson iteration
    sigma = sigma_0
    
    for _ in range(num_iter):
        # Compute option price using existing functions
        if option_type == "call":
            price = bs_call_price(S0, K, T, r, sigma, q)
        elif option_type == "put":
            price = bs_put_price(S0, K, T, r, sigma, q)
        else:
            raise ValueError("option_type must be 'call' or 'put'")
        
        # Compute vega using existing function
        option_vega = vega(S0, K, T, r, sigma, q)
        
        # Calculate difference
        diff = price - market_price
        
        # Check convergence
        if abs(diff) < tol:
            return sigma
        
        # Avoid division by zero or tiny vega (numerical instability)
        if option_vega < 1e-6:
            break
        
        # Newton-Raphson update
        sigma -= diff / option_vega
        
        # Clamp sigma to avoid runaway (volatility should be positive and reasonable)
        sigma = max(1e-4, min(sigma, 5.0))
    
    # Return NaN if no convergence
    return np.nan

def load_vstoxx_data(data_path='./data/vstoxx_data_31032014.h5', auto_download=True):
    """Load VSTOXX futures and options data from HDF5 file."""
    if not os.path.exists(data_path) and auto_download:
        print(f"📂 Data file not found at {data_path}")
        data_dir = os.path.dirname(data_path) or "./data"
        filename = os.path.basename(data_path)
        data_path = download_vstoxx_data(filename=filename, data_dir=data_dir)
    
    try:
        print(f"📊 Loading data from: {data_path}")
        h5 = pd.HDFStore(data_path, 'r')
        futures_data = h5['futures_data'].copy()
        options_data = h5['options_data'].copy()
        h5.close()
        
        # Convert datetime columns
        futures_data, options_data = prepare_datetime_columns(futures_data, options_data)
        
        # Add column for implied volatilities
        options_data['IMP_VOL'] = np.NaN
        
        print(f"✅ Data loaded successfully.")
        print(f"   Futures data shape: {futures_data.shape}")
        print(f"   Options data shape: {options_data.shape}")
        
        return futures_data, options_data
        
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        raise

def compute_batch_implied_volatility(options_data, futures_data, S0,
                                   sigma_0=2.0, num_iter=100, tol=0.5,
                                   r=0.0, q=0.0):
    """
    Compute implied volatility for all options in the dataset.
    
    Parameters:
    -----------
    options_data : pd.DataFrame
        Options data with columns: MATURITY, STRIKE, TTM, PRICE
    futures_data : pd.DataFrame  
        Futures data with columns: MATURITY, PRICE
    sigma_0 : float
        Initial guess for volatility
    num_iter : int
        Maximum iterations
    tol : float
        Moneyness tolerance
    r : float
        Risk-free rate
    q : float
        Dividend yield
    
    Returns:
    --------
    pd.DataFrame : Options data with IMP_VOL column populated
    """
    print(f"⚡ Computing implied volatilities for {len(options_data)} options...")
    
    options_copy = options_data.copy()
    processed_count = 0
    success_count = 0
    
    for idx in options_copy.index:
        maturity = options_copy.loc[idx, 'MATURITY']
        forward_prices = futures_data[futures_data['MATURITY'] == maturity]['PRICE'].values
        
        if len(forward_prices) == 0:
            continue
            
        forward = forward_prices[0]
        strike = options_copy.loc[idx, 'STRIKE']
        
        # Only process options with moneyness within tolerance
        if forward * (1 - tol) < strike < forward * (1 + tol):
            processed_count += 1
            
            call_market = options_copy.loc[idx, 'PRICE']
            T = options_copy.loc[idx, 'TTM']
            
            try:
                implied_vol = implied_volatility(
                    S0=S0,
                    K=strike,
                    T=T,
                    r=r,
                    market_price=call_market,
                    sigma_0=sigma_0,
                    q=q,
                    num_iter=num_iter,
                    option_type="call"
                )
                
                if not np.isnan(implied_vol) and 0.001 < implied_vol < 50:
                    options_copy.loc[idx, 'IMP_VOL'] = implied_vol
                    success_count += 1
                
            except Exception as e:
                print(f"⚠️  Error computing implied vol for option {idx}: {e}")
                continue
    
    print(f"✅ Processed {processed_count} options, {success_count} successful calculations")
    return options_copy

def get_volatility_surface(options_data, strikes=None, maturities=None):
    """Extract implied volatility surface for visualization."""
    filtered_data = options_data.dropna(subset=['IMP_VOL'])
    filtered_data = filtered_data[
        (filtered_data['IMP_VOL'] > 0) & 
        (filtered_data['IMP_VOL'] < 50)
    ]
    
    if strikes is not None:
        filtered_data = filtered_data[filtered_data['STRIKE'].isin(strikes)]
    
    if maturities is not None:
        filtered_data = filtered_data[filtered_data['MATURITY'].isin(maturities)]
    
    vol_surface = filtered_data.pivot_table(
        values='IMP_VOL',
        index='STRIKE',
        columns='MATURITY',
        aggfunc='mean'
    )
    
    return vol_surface

def get_implied_vol_summary_stats(options_data):
    """Get summary statistics of the implied volatilities."""
    implied_vols = options_data['IMP_VOL'].dropna()
    implied_vols = implied_vols[(implied_vols > 0) & (implied_vols < 50)]
    
    if len(implied_vols) == 0:
        return {"message": "No valid implied volatilities computed yet."}
    
    return {
        "count": len(implied_vols),
        "mean": implied_vols.mean(),
        "std": implied_vols.std(),
        "min": implied_vols.min(),
        "max": implied_vols.max(),
        "median": implied_vols.median(),
        "25th_percentile": implied_vols.quantile(0.25),
        "75th_percentile": implied_vols.quantile(0.75)
    }

def plot_volatility_smiles(options_data, title="VSTOXX Implied Volatility Smile"):
    """Plot volatility smiles for different maturities."""
    print("📊 Creating volatility smile plots...")
    
    plot_data = options_data[
        (options_data['IMP_VOL'] > 0) & 
        (options_data['IMP_VOL'] < 50)
    ].copy()
    
    if plot_data.empty:
        print("❌ No valid implied volatilities to plot")
        return None, None
    
    maturities = sorted(plot_data['MATURITY'].unique())
    fig, ax = plt.subplots(figsize=(12, 8))
    colors = plt.cm.tab10(np.linspace(0, 1, len(maturities)))
    
    for i, maturity in enumerate(maturities):
        maturity_data = plot_data[plot_data['MATURITY'] == maturity].sort_values('STRIKE')
        
        if len(maturity_data) > 1:
            strikes = maturity_data['STRIKE'].values
            imp_vols = maturity_data['IMP_VOL'].values
            
            ax.plot(strikes, imp_vols, 
                   color=colors[i], linewidth=2, label=maturity.strftime('%Y-%m-%d'))
            ax.scatter(strikes, imp_vols, 
                      color=colors[i], s=50, alpha=0.7)
    
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Strike Price', fontsize=12)
    ax.set_ylabel('Implied Volatility', fontsize=12)
    ax.set_title(title, fontsize=14, fontweight='bold')
    ax.legend(title='Maturity', bbox_to_anchor=(1.05, 1), loc='upper left')
    
    plt.tight_layout()
    
    os.makedirs('./data', exist_ok=True)
    plt.savefig('./data/vstoxx_volatility_smiles.png', dpi=300, bbox_inches='tight')
    plt.show()
    
    print(f"✅ Plotted volatility smiles for {len(maturities)} maturities")
    return fig, ax

def analyze_atm_term_structure(options_data, S0):
    """
    Analyze at-the-money volatility term structure.
    
    Parameters:
    -----------
    options_data : pd.DataFrame
        Options data with IMP_VOL column
    S0 : float
        Current underlying price
        
    Returns:
    --------
    pd.DataFrame
        ATM volatility data with term structure metrics
    """
    atm_data = []
    
    for maturity in options_data['MATURITY'].unique():
        maturity_options = options_data[
            (options_data['MATURITY'] == maturity) & 
            (options_data['IMP_VOL'].notna()) &
            (options_data['IMP_VOL'] > 0)
        ]
        
        if len(maturity_options) > 0:
            # Find ATM option (closest to S0)
            atm_option = maturity_options.loc[
                (maturity_options['STRIKE'] - S0).abs().idxmin()
            ]
            
            atm_data.append({
                'Maturity': maturity,
                'Days_to_Expiry': atm_option['TTM'] * 365,
                'Strike': atm_option['STRIKE'],
                'ATM_Vol': atm_option['IMP_VOL'],
                'Moneyness': atm_option['STRIKE'] / S0
            })
    
    if not atm_data:
        return pd.DataFrame()
    
    atm_df = pd.DataFrame(atm_data).sort_values('Days_to_Expiry')
    
    # Calculate term structure metrics
    if len(atm_df) > 1:
        correlation = np.corrcoef(atm_df['Days_to_Expiry'], atm_df['ATM_Vol'])[0,1]
        slope = np.polyfit(atm_df['Days_to_Expiry'], atm_df['ATM_Vol'], 1)[0]
        
        atm_df.attrs['correlation'] = correlation
        atm_df.attrs['slope'] = slope
        atm_df.attrs['shape'] = 'Upward sloping' if slope > 0 else 'Downward sloping'
    
    return atm_df

def analyze_volatility_smile_characteristics(vol_surface, S0):
    """
    Analyze volatility smile characteristics across maturities.
    
    Parameters:
    -----------
    vol_surface : pd.DataFrame
        Volatility surface (strikes x maturities)
    S0 : float
        Current underlying price
        
    Returns:
    --------
    pd.DataFrame
        Smile characteristics by maturity
    """
    smile_stats = []
    
    for maturity in vol_surface.columns:
        maturity_data = vol_surface[maturity].dropna()
        
        if len(maturity_data) >= 3:  # Need at least 3 points
            strikes = maturity_data.index.values
            vols = maturity_data.values
            
            # Find ATM point
            atm_idx = np.argmin(np.abs(strikes - S0))
            atm_vol = vols[atm_idx]
            
            # Calculate smile characteristics
            vol_range = vols.max() - vols.min()
            vol_std = np.std(vols)
            
            # Calculate skew (OTM put vol - OTM call vol)
            otm_put_vol = vols[0] if len(vols) > 0 else np.nan
            otm_call_vol = vols[-1] if len(vols) > 0 else np.nan
            skew = otm_put_vol - otm_call_vol if not (np.isnan(otm_put_vol) or np.isnan(otm_call_vol)) else np.nan
            
            smile_stats.append({
                'Maturity': maturity.strftime('%Y-%m-%d'),
                'Days_to_Expiry': (maturity - pd.Timestamp('2014-03-31')).days,
                'ATM_Vol': atm_vol,
                'Vol_Range': vol_range,
                'Vol_Std': vol_std,
                'Skew': skew,
                'Data_Points': len(maturity_data)
            })
    
    return pd.DataFrame(smile_stats) if smile_stats else pd.DataFrame()

def compute_volatility_risk_metrics(options_data):
    """
    Compute risk metrics from implied volatility data.
    
    Parameters:
    -----------
    options_data : pd.DataFrame
        Options data with IMP_VOL column
        
    Returns:
    --------
    dict
        Dictionary containing various risk metrics
    """
    valid_vols = options_data[
        (options_data['IMP_VOL'].notna()) &
        (options_data['IMP_VOL'] > 0) &
        (options_data['IMP_VOL'] < 50)
    ]['IMP_VOL']
    
    if len(valid_vols) == 0:
        return {"error": "No valid volatility data"}
    
    # Calculate metrics
    mean_vol = valid_vols.mean()
    std_vol = valid_vols.std()
    
    # Value at Risk (VaR)
    var_95 = np.percentile(valid_vols, 95)
    var_99 = np.percentile(valid_vols, 99)
    
    # Expected Shortfall (CVaR)
    cvar_95 = valid_vols[valid_vols >= var_95].mean()
    cvar_99 = valid_vols[valid_vols >= var_99].mean()
    
    # Outlier detection
    outliers = valid_vols[(valid_vols < mean_vol - 2*std_vol) | (valid_vols > mean_vol + 2*std_vol)]
    
    return {
        'mean_vol': mean_vol,
        'vol_of_vol': std_vol,
        'var_95': var_95,
        'var_99': var_99,
        'cvar_95': cvar_95,
        'cvar_99': cvar_99,
        'outlier_count': len(outliers),
        'outlier_pct': len(outliers) / len(valid_vols) * 100,
        'total_observations': len(valid_vols)
    }

def plot_3d_volatility_surface(vol_surface, title="3D Implied Volatility Surface", 
                              save_path="./data/3d_volatility_surface.png"):
    """
    Create a 3D surface plot of implied volatility.
    
    Parameters:
    -----------
    vol_surface : pd.DataFrame
        Volatility surface (strikes x maturities)
    title : str
        Plot title
    save_path : str
        Path to save the plot
        
    Returns:
    --------
    tuple
        (matplotlib.Figure, matplotlib.Axes) or (None, None) if insufficient data
    """
    if vol_surface.empty:
        print("❌ No volatility surface data available for 3D plot")
        return None, None
    
    # Clean data
    vol_surface_clean = vol_surface.dropna(how='all', axis=0).dropna(how='all', axis=1)
    
    if vol_surface_clean.shape[0] < 2 or vol_surface_clean.shape[1] < 2:
        print("❌ Insufficient data points for 3D surface (need at least 2x2)")
        return None, None
    
    # Prepare data
    strikes = vol_surface_clean.index.values
    maturities = vol_surface_clean.columns
    days_to_expiry = [(mat - pd.Timestamp('2014-03-31')).days for mat in maturities]
    
    # Create meshgrid
    X, Y = np.meshgrid(strikes, days_to_expiry)
    Z = vol_surface_clean.T.values
    
    # Create the plot
    fig = plt.figure(figsize=(14, 10))
    ax = fig.add_subplot(111, projection='3d')
    
    # Plot surface
    surface = ax.plot_surface(X, Y, Z, 
                             cmap=cm.viridis,
                             alpha=0.8,
                             linewidth=0.5,
                             antialiased=True,
                             edgecolors='gray')
    
    # Add contour lines
    contours = ax.contour(X, Y, Z, 
                         levels=10, 
                         zdir='z', 
                         offset=np.nanmin(Z) - 0.05,
                         cmap=cm.viridis,
                         alpha=0.6)
    
    # Add data points
    for i, strike in enumerate(strikes):
        for j, days in enumerate(days_to_expiry):
            if not np.isnan(Z[j, i]):
                ax.scatter([strike], [days], [Z[j, i]], 
                          color='red', s=20, alpha=0.7)
    
    # Customize plot
    ax.set_xlabel('Strike Price', fontsize=12, labelpad=10)
    ax.set_ylabel('Days to Expiry', fontsize=12, labelpad=10)
    ax.set_zlabel('Implied Volatility', fontsize=12, labelpad=10)
    ax.set_title(title, fontsize=14, fontweight='bold', pad=20)
    
    # Add colorbar
    cbar = plt.colorbar(surface, ax=ax, shrink=0.5, aspect=20, pad=0.1)
    cbar.set_label('Implied Volatility', rotation=270, labelpad=20)
    
    # Set viewing angle
    ax.view_init(elev=25, azim=45)
    ax.grid(True, alpha=0.3)
    
    # Add statistics
    valid_vols = vol_surface_clean.values[~np.isnan(vol_surface_clean.values)]
    if len(valid_vols) > 0:
        stats_text = f"""Surface Statistics:
Data Points: {len(valid_vols)}
Min Vol: {valid_vols.min():.4f}
Max Vol: {valid_vols.max():.4f}
Mean Vol: {valid_vols.mean():.4f}
Strike Range: {strikes.min():.1f} - {strikes.max():.1f}
Days Range: {min(days_to_expiry)} - {max(days_to_expiry)}"""
        
        ax.text2D(0.02, 0.98, stats_text, transform=ax.transAxes, 
                 verticalalignment='top', fontsize=9,
                 bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    plt.tight_layout()
    
    # Save plot
    import os
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig, ax

def create_volatility_smile_3d(vol_surface, title="3D Volatility Smiles",
                              save_path="./data/3d_volatility_smiles.png"):
    """
    Create a 3D plot showing volatility smiles across different maturities.
    
    Parameters:
    -----------
    vol_surface : pd.DataFrame
        Volatility surface (strikes x maturities)
    title : str
        Plot title
    save_path : str
        Path to save the plot
        
    Returns:
    --------
    tuple
        (matplotlib.Figure, matplotlib.Axes)
    """
    if vol_surface.empty:
        print("❌ No volatility surface data available")
        return None, None
    
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')
    
    colors = plt.cm.tab10(np.linspace(0, 1, len(vol_surface.columns)))
    
    for i, maturity in enumerate(vol_surface.columns):
        maturity_data = vol_surface[maturity].dropna()
        
        if len(maturity_data) > 1:
            strikes = maturity_data.index.values
            vols = maturity_data.values
            days = (maturity - pd.Timestamp('2014-03-31')).days
            
            # Plot line and scatter points
            ax.plot(strikes, [days] * len(strikes), vols,
                   color=colors[i], linewidth=2, label=f"{days} days")
            ax.scatter(strikes, [days] * len(strikes), vols,
                      color=colors[i], s=30, alpha=0.7)
    
    ax.set_xlabel('Strike Price')
    ax.set_ylabel('Days to Expiry')
    ax.set_zlabel('Implied Volatility')
    ax.set_title(title)
    ax.legend(bbox_to_anchor=(1.1, 1), loc='upper left')
    
    plt.tight_layout()
    
    # Save plot
    import os
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig, ax

def simulate_gbm_paths(S0, T, r, sigma, num_paths, num_steps, mu=None, risk_neutral=True, seed=None):
    # Set random seed for reproducibility
    if seed is not None:
        np.random.seed(seed)
    
    # Create time grid
    dt = T / num_steps
    t = np.linspace(0, T, num_steps + 1)
    
    # Generate Brownian motion increments
    dW = np.random.normal(0, np.sqrt(dt), size=(num_paths, num_steps))
    
    # Construct Brownian motion paths
    # B(0) = 0, B(t) = cumulative sum of increments
    B = np.zeros((num_paths, num_steps + 1))
    B[:, 1:] = np.cumsum(dW, axis=1)
    
    # Determine drift rate
    if risk_neutral:
        drift_rate = r
    else:
        drift_rate = mu if mu is not None else r
    
    # Calculate drift and diffusion terms
    drift = (drift_rate - 0.5 * sigma**2) * t  # shape: (num_steps + 1,)
    diffusion = sigma * B  # shape: (num_paths, num_steps + 1)
    
    # Simulate GBM paths: S(t) = S0 * exp((μ - σ²/2)t + σB(t))
    S_paths = S0 * np.exp(drift + diffusion)
    
    return t, S_paths

def draw_finite_difference_grid(M=5, N=5):
    """
    Draw an enhanced annotated finite difference grid for Black-Scholes equation
    with clear distinction between different types of grid points.
    
    Parameters:
    -----------
    M : int
        Number of spatial steps (default: 5)
    N : int
        Number of time steps (default: 5)
    """
    import matplotlib.pyplot as plt
    import numpy as np
    
    fig, ax = plt.subplots(figsize=(12, 10))

    # Draw grid lines
    for n in range(N+1):
        ax.plot(range(M+1), [n]*(M+1), color='black', linewidth=0.5, alpha=0.3)
    for m in range(M+1):
        ax.plot([m]*(N+1), range(N+1), color='black', linewidth=0.5, alpha=0.3)

    # Define point styles for different types of grid points
    point_styles = {
        'initial': {'color': 'red', 'marker': 'o', 'size': 120, 'label': 'Option Payoff (t=T)'},
        'boundary_spatial': {'color': 'green', 'marker': 's', 'size': 100, 'label': 'Boundary Condition (S=0, S=Smax)'},
        'interior': {'color': 'blue', 'marker': '^', 'size': 80, 'label': 'Interior Points (computed)'},
        'corner': {'color': 'purple', 'marker': 'D', 'size': 100, 'label': 'Corner Points'},
        'computed_boundary': {'color': 'orange', 'marker': 'v', 'size': 80, 'label': 'Current Option Value (computed)'}
    }

    # Draw grid points with different styles based on their role
    legend_handles = {}
    for n in range(N+1):
        for m in range(M+1):
            # Determine point type
            if n == N:  # Initial condition (t = T, expiration)
                if m == 0 or m == M:  # Corner points at expiration
                    style_key = 'corner'
                else:  # Interior points at expiration
                    style_key = 'initial'
            elif m == 0 or m == M:  # Spatial boundaries (S = 0 or S = Smax)
                if n == 0:  # Corner at t = 0
                    style_key = 'corner'
                else:  # Spatial boundary points
                    style_key = 'boundary_spatial'
            elif n == 0:  # Time boundary at t = 0 (today)
                style_key = 'computed_boundary'
            else:  # Interior points
                style_key = 'interior'
            
            style = point_styles[style_key]
            scatter = ax.scatter(m, n, c=style['color'], marker=style['marker'], 
                               s=style['size'], alpha=0.8, edgecolors='black', 
                               linewidth=1, zorder=3)
            
            # Store handle for legend (avoid duplicates)
            if style_key not in legend_handles:
                legend_handles[style_key] = scatter

    # Create appropriate tick labels based on M and N
    if M <= 6:
        x_labels = [f'(i = {i})' for i in range(M+1)]
        x_positions = list(range(M+1))
    else:
        x_labels = ['(i = 0)', '(i = 1)', '⋯', f'(i = {M-1})', f'(i = {M})']
        x_positions = [0, 1, M//2, M-1, M]
    
    if N <= 6:
        y_labels = [f'(n = {i})' for i in range(N+1)]
        y_positions = list(range(N+1))
    else:
        y_labels = ['(n = 0)', '(n = 1)', '⋯', f'(n = {N-1})', f'(n = {N})']
        y_positions = [0, 1, N//2, N-1, N]

    # Set axis ticks and labels
    ax.set_xticks(x_positions)
    ax.set_xticklabels(x_labels)
    ax.set_yticks(y_positions)
    ax.set_yticklabels(y_labels)

    # Axis labels
    ax.set_xlabel('S (Stock Price)', fontsize=14, fontweight='bold')
    ax.set_ylabel('t (Time)', fontsize=14, fontweight='bold')

    # Boundary labels with better positioning
    ax.text(-0.3, -0.3, r'$S_{\min}$', fontsize=12, ha='center', color='darkgreen', fontweight='bold')
    ax.text(M+0.3, -0.3, r'$S_{\max}$', fontsize=12, ha='center', color='darkgreen', fontweight='bold')
    ax.text(-0.7, 0, r'$t = 0$', fontsize=12, va='center', color='darkorange', fontweight='bold')
    ax.text(-0.7, N, r'$t = T$', fontsize=12, va='center', color='darkred', fontweight='bold')

    # Add arrows showing solution direction and time stepping (positioned to avoid grid points)
    if M >= 3 and N >= 3:
        # Simple directional arrow without text box
        ax.annotate('', xy=(M//2-2/3, 0.5), xytext=(M//2-2/3, N-0.5),
                   arrowprops=dict(arrowstyle='->', lw=3, color='darkred'))
        ax.text(M//2-1/3, N//2, 'Solution\nDirection', rotation=-90, ha='center', va='center',
               fontsize=10, color='darkred', fontweight='bold')

    # Frame and scale
    ax.set_xlim(-1.2, M+1.2)
    ax.set_ylim(-0.8, N+1.2)
    ax.set_aspect('equal')
    
    # Add subtle grid
    ax.grid(True, alpha=0.2, linestyle=':', color='gray')

    # Create legend with proper ordering
    legend_order = ['initial', 'boundary_spatial', 'interior', 'computed_boundary', 'corner']
    legend_elements = []
    for key in legend_order:
        if key in legend_handles:
            style = point_styles[key]
            legend_elements.append(plt.scatter([], [], c=style['color'], marker=style['marker'], 
                                             s=style['size'], alpha=0.8, edgecolors='black', 
                                             linewidth=1, label=style['label']))

    ax.legend(handles=legend_elements, loc='upper right',
             frameon=True, fancybox=True, shadow=True, fontsize=9)

    # Enhanced title
    title = f"Finite Difference Grid for Black-Scholes PDE\n"
    title += f"Spatial Grid: {M+1} points, Time Grid: {N+1} points"
    plt.title(title, fontsize=16, pad=20, fontweight='bold')
    
    # Simplified explanation positioned outside the grid area
    explanation = """Key Points:
• Red circles: Initial conditions at expiration (t=T)
• Green squares: Spatial boundary conditions (S=0, S=Smax)
• Blue triangles: Interior points solved by finite difference
• Orange triangles: Time boundary at t=0 (computed)
• Purple diamonds: Corner points
Process: Start with payoff at expiration → solve backwards to today"""
    
    ax.text(0.013, 0.99, explanation, transform=ax.transAxes, 
            verticalalignment='top', horizontalalignment='left',
            bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.9),
            fontsize=9)
    
    plt.tight_layout()
    plt.show()
    
    return fig, ax

def download_vstoxx_data(url=None, filename="vstoxx_data_31032014.h5", data_dir="./data"):
    """Download VSTOXX data file from specified URL to data directory."""
    if url is None:
        url = "https://github.com/yhilpisch/py4fi/raw/master/jupyter36/source/vstoxx_data_31032014.h5"
    
    os.makedirs(data_dir, exist_ok=True)
    file_path = os.path.join(data_dir, filename)
    
    print(f"📥 Downloading VSTOXX data from: {url}")
    print(f"📁 Saving to: {file_path}")
    
    try:
        with requests.get(url, stream=True, timeout=30) as response:
            response.raise_for_status()
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
        
        print(f"✅ Successfully downloaded: {file_path}")
        return file_path
        
    except requests.RequestException as e:
        print(f"❌ Download failed: {e}")
        alt_url = "https://github.com/NanguangChou/BSM_call_option/raw/master/vstoxx_data_31032014.h5"
        if url != alt_url:
            print(f"🔄 Trying alternative URL: {alt_url}")
            return download_vstoxx_data(alt_url, filename, data_dir)
        raise

def prepare_datetime_columns(futures_data, options_data):
    """Convert date columns to datetime format."""
    print("🔄 Converting datetime columns...")
    
    date_columns = ['DATE', 'MATURITY']
    
    for col in date_columns:
        if col in futures_data.columns:
            futures_data[col] = pd.to_datetime(futures_data[col])
        if col in options_data.columns:
            options_data[col] = pd.to_datetime(options_data[col])
    
    print("✅ Datetime conversion completed")
    return futures_data, options_data

def create_synthetic_options_data(S0=100, strikes=None, maturities=None, n_options=50, seed=42):
    """
    Create synthetic options data for testing and demonstration purposes.
    
    Parameters:
    -----------
    S0 : float
        Current underlying price
    strikes : array-like, optional
        Strike prices to use (default: around ATM)
    maturities : array-like, optional
        Maturity dates to use (default: monthly for 6 months)
    n_options : int
        Number of options to generate if strikes/maturities not provided
    seed : int
        Random seed for reproducibility
        
    Returns:
    --------
    tuple
        (options_data, futures_data) as pandas DataFrames
    """
    np.random.seed(seed)
    
    # Default strikes around ATM
    if strikes is None:
        strikes = np.linspace(S0 * 0.9, S0 * 1.1, 10)
    
    # Default maturities
    if maturities is None:
        maturities = pd.date_range('2024-01-01', periods=6, freq='M')
    
    synthetic_options = []
    for strike in strikes:
        for i, maturity in enumerate(maturities):
            ttm = (i + 1) * 0.083  # Months to years approximation
            
            # Generate synthetic option price with volatility smile
            moneyness = strike / S0
            base_vol = 0.2 + 0.1 * (moneyness - 1)**2  # U-shaped smile
            
            # Black-Scholes price with some noise
            d1 = (np.log(S0/strike) + (0.05 + 0.5*base_vol**2)*ttm) / (base_vol*np.sqrt(ttm))
            d2 = d1 - base_vol*np.sqrt(ttm)
            
            from scipy.stats import norm
            bs_price = S0*norm.cdf(d1) - strike*np.exp(-0.05*ttm)*norm.cdf(d2)
            option_price = max(bs_price + np.random.normal(0, 0.5), 0.1)
            
            synthetic_options.append({
                'STRIKE': strike,
                'TTM': ttm,
                'MATURITY': maturity,
                'PRICE': option_price,
                'DATE': pd.Timestamp('2024-01-01')
            })
    
    options_data = pd.DataFrame(synthetic_options)
    
    # Create corresponding futures data
    futures_data = pd.DataFrame({
        'MATURITY': maturities,
        'PRICE': [S0] * len(maturities),
        'DATE': [pd.Timestamp('2024-01-01')] * len(maturities)
    })
    
    return options_data, futures_data

def plot_volatility_surface_analysis(vol_surface, title="Volatility Surface Analysis"):
    """
    Create a comprehensive 4-panel plot of volatility surface analysis.
    
    Parameters:
    -----------
    vol_surface : pd.DataFrame
        Volatility surface (strikes x maturities)
    title : str
        Main title for the plot
        
    Returns:
    --------
    tuple
        (matplotlib.Figure, array of matplotlib.Axes)
    """
    if vol_surface is None or vol_surface.empty:
        print("No volatility surface data to plot")
        return None, None
    
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # Panel 1: Heatmap of the entire surface
    ax1 = axes[0, 0]
    im = ax1.imshow(vol_surface.values, cmap='viridis', aspect='auto', interpolation='nearest')
    ax1.set_title('Volatility Surface Heatmap')
    ax1.set_xlabel('Maturity Index')
    ax1.set_ylabel('Strike Index')
    plt.colorbar(im, ax=ax1, label='Implied Volatility')
    
    # Panel 2: Volatility smile for first available maturity
    ax2 = axes[0, 1]
    first_maturity = vol_surface.columns[0]
    vol_smile = vol_surface[first_maturity].dropna()
    if len(vol_smile) > 0:
        ax2.plot(vol_smile.index, vol_smile.values, 'bo-', linewidth=2, markersize=6)
        ax2.set_xlabel('Strike Price')
        ax2.set_ylabel('Implied Volatility')
        ax2.set_title(f'Volatility Smile\n{first_maturity.strftime("%Y-%m-%d") if hasattr(first_maturity, "strftime") else first_maturity}')
        ax2.grid(True, alpha=0.3)
    
    # Panel 3: Term structure for ATM option
    ax3 = axes[1, 0]
    if len(vol_surface.index) > 0:
        atm_strike_idx = len(vol_surface.index) // 2
        atm_strike = vol_surface.index[atm_strike_idx]
        term_structure = vol_surface.loc[atm_strike].dropna()
        
        if len(term_structure) > 0:
            x_vals = [(mat - vol_surface.columns[0]).days if hasattr(mat, 'strftime') else i 
                     for i, mat in enumerate(term_structure.index)]
            ax3.plot(x_vals, term_structure.values, 'ro-', linewidth=2, markersize=6)
            ax3.set_xlabel('Days to Maturity')
            ax3.set_ylabel('Implied Volatility')
            ax3.set_title(f'Term Structure\nStrike: {atm_strike:.2f}')
            ax3.grid(True, alpha=0.3)
    
    # Panel 4: Distribution of implied volatilities
    ax4 = axes[1, 1]
    vol_data = vol_surface.values.flatten()
    vol_data = vol_data[~np.isnan(vol_data)]
    
    if len(vol_data) > 0:
        ax4.hist(vol_data, bins=20, alpha=0.7, edgecolor='black', color='skyblue')
        ax4.axvline(np.mean(vol_data), color='red', linestyle='--', 
                   label=f'Mean: {np.mean(vol_data):.3f}')
        ax4.axvline(np.median(vol_data), color='orange', linestyle='--', 
                   label=f'Median: {np.median(vol_data):.3f}')
        ax4.set_xlabel('Implied Volatility')
        ax4.set_ylabel('Frequency')
        ax4.set_title('Distribution of Implied Volatilities')
        ax4.legend()
        ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.suptitle(title, y=0.98, fontsize=14, fontweight='bold')
    
    return fig, axes

def explore_data_structure(options_data, futures_data, detailed=True):
    """
    Explore and summarize the structure of options and futures data.
    
    Parameters:
    -----------
    options_data : pd.DataFrame
        Options data
    futures_data : pd.DataFrame
        Futures data
    detailed : bool
        Whether to show detailed statistics
        
    Returns:
    --------
    dict
        Summary statistics and information
    """
    summary = {}
    
    print("="*60)
    print("DATA STRUCTURE EXPLORATION")
    print("="*60)
    
    # Options data analysis
    if options_data is not None:
        print(f"\n📊 OPTIONS DATA:")
        print(f"  Shape: {options_data.shape}")
        print(f"  Columns: {list(options_data.columns)}")
        
        if detailed:
            numeric_cols = options_data.select_dtypes(include=[np.number]).columns
            print(f"\n  Numeric Summary:")
            for col in numeric_cols:
                if col in options_data.columns:
                    data = options_data[col].dropna()
                    print(f"    {col}: {data.min():.4f} - {data.max():.4f} (mean: {data.mean():.4f})")
            
            if 'MATURITY' in options_data.columns:
                unique_maturities = options_data['MATURITY'].nunique()
                print(f"  Unique maturities: {unique_maturities}")
        
        summary['options'] = {
            'shape': options_data.shape,
            'columns': list(options_data.columns),
            'numeric_summary': {}
        }
        
        for col in options_data.select_dtypes(include=[np.number]).columns:
            if col in options_data.columns:
                data = options_data[col].dropna()
                summary['options']['numeric_summary'][col] = {
                    'min': data.min(),
                    'max': data.max(),
                    'mean': data.mean(),
                    'std': data.std()
                }
    
    # Futures data analysis
    if futures_data is not None:
        print(f"\n📈 FUTURES DATA:")
        print(f"  Shape: {futures_data.shape}")
        print(f"  Columns: {list(futures_data.columns)}")
        
        if detailed and 'PRICE' in futures_data.columns:
            prices = futures_data['PRICE'].dropna()
            print(f"  Price range: {prices.min():.4f} - {prices.max():.4f}")
        
        summary['futures'] = {
            'shape': futures_data.shape,
            'columns': list(futures_data.columns)
        }
    
    # Data quality checks
    print(f"\n🔍 DATA QUALITY:")
    if options_data is not None:
        missing_options = options_data.isnull().sum().sum()
        print(f"  Options missing values: {missing_options}")
        
    if futures_data is not None:
        missing_futures = futures_data.isnull().sum().sum()
        print(f"  Futures missing values: {missing_futures}")
    
    print("="*60)
    
    return summary

def find_extreme_volatility_options(options_data, n_extreme=5):
    """
    Find options with highest and lowest implied volatilities.
    
    Parameters:
    -----------
    options_data : pd.DataFrame
        Options data with IMP_VOL column
    n_extreme : int
        Number of extreme options to return
        
    Returns:
    --------
    dict
        Dictionary with highest and lowest volatility options
    """
    if options_data is None or 'IMP_VOL' not in options_data.columns:
        return {'highest': None, 'lowest': None}
    
    valid_options = options_data.dropna(subset=['IMP_VOL'])
    
    if len(valid_options) == 0:
        return {'highest': None, 'lowest': None}
    
    # Find extreme volatilities
    highest_vol = valid_options.nlargest(n_extreme, 'IMP_VOL')
    lowest_vol = valid_options.nsmallest(n_extreme, 'IMP_VOL')
    
    print(f"\n📊 EXTREME VOLATILITY OPTIONS (Top {n_extreme}):")
    print("\n🔴 HIGHEST IMPLIED VOLATILITIES:")
    for i, (idx, row) in enumerate(highest_vol.iterrows()):
        print(f"  {i+1}. Strike: {row['STRIKE']:.2f}, TTM: {row['TTM']:.4f}, "
              f"Price: {row['PRICE']:.4f}, IV: {row['IMP_VOL']:.4f}")
    
    print("\n🔵 LOWEST IMPLIED VOLATILITIES:")
    for i, (idx, row) in enumerate(lowest_vol.iterrows()):
        print(f"  {i+1}. Strike: {row['STRIKE']:.2f}, TTM: {row['TTM']:.4f}, "
              f"Price: {row['PRICE']:.4f}, IV: {row['IMP_VOL']:.4f}")
    
    return {
        'highest': highest_vol,
        'lowest': lowest_vol
    }

def save_analysis_summary(options_data, vol_surface, stats, save_path="./data/analysis_summary.txt"):
    """
    Save a comprehensive analysis summary to a text file.
    
    Parameters:
    -----------
    options_data : pd.DataFrame
        Options data with computed implied volatilities
    vol_surface : pd.DataFrame
        Volatility surface
    stats : dict
        Summary statistics from get_summary_statistics()
    save_path : str
        Path to save the summary file
    """
    import os
    from datetime import datetime
    
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    with open(save_path, 'w') as f:
        f.write("BLACK-SCHOLES IMPLIED VOLATILITY ANALYSIS SUMMARY\n")
        f.write("="*60 + "\n")
        f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
        
        # Basic statistics
        if 'message' not in stats:
            f.write("IMPLIED VOLATILITY STATISTICS:\n")
            f.write(f"  Total computations: {stats['count']:,}\n")
            f.write(f"  Mean volatility: {stats['mean']:.4f} ({stats['mean']*100:.2f}%)\n")
            f.write(f"  Standard deviation: {stats['std']:.4f}\n")
            f.write(f"  Range: {stats['min']:.4f} - {stats['max']:.4f}\n")
            f.write(f"  Median: {stats['median']:.4f}\n")
            f.write(f"  25th-75th percentile: {stats['25th_percentile']:.4f} - {stats['75th_percentile']:.4f}\n\n")
        
        # Data summary
        if options_data is not None:
            f.write("DATA SUMMARY:\n")
            f.write(f"  Total options: {len(options_data):,}\n")
            f.write(f"  Options with valid IV: {len(options_data.dropna(subset=['IMP_VOL'])) if 'IMP_VOL' in options_data.columns else 0:,}\n")
            
            if 'STRIKE' in options_data.columns:
                f.write(f"  Strike range: {options_data['STRIKE'].min():.2f} - {options_data['STRIKE'].max():.2f}\n")
            if 'TTM' in options_data.columns:
                f.write(f"  TTM range: {options_data['TTM'].min():.4f} - {options_data['TTM'].max():.4f}\n")
        
        # Volatility surface
        if vol_surface is not None and not vol_surface.empty:
            f.write(f"\nVOLATILITY SURFACE:\n")
            f.write(f"  Dimensions: {vol_surface.shape[0]} strikes × {vol_surface.shape[1]} maturities\n")
            f.write(f"  Data coverage: {vol_surface.notna().sum().sum()} / {vol_surface.size} cells\n")
            f.write(f"  Coverage rate: {vol_surface.notna().sum().sum() / vol_surface.size * 100:.1f}%\n")
    
    print(f"📄 Analysis summary saved to: {save_path}")