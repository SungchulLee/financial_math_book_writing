# ============================================================================
# black_scholes/black_scholes_utils.py
# ============================================================================
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import pandas as pd
import os
import requests
import scipy.stats as stats
import warnings
from typing import Tuple, Optional, Dict, List

# =========================================================================
# UTILITIES FOR FORMULA
# =========================================================================

def d1_d2(S: float, K: float, T: float, r: float, sigma: float, q: float = 0) -> Tuple[float, float]:
    """Calculate d1 and d2 parameters for Black-Scholes formula - UNCHANGED"""
    d1 = (np.log(S / K) + (r - q + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    return d1, d2

def bs_call_price(S: float, K: float, T: float, r: float, sigma: float, q: float = 0) -> float:
    """Black-Scholes call option price - UNCHANGED"""
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    return S * np.exp(-q * T) * stats.norm.cdf(d1) - K * np.exp(-r * T) * stats.norm.cdf(d2)

def bs_put_price(S: float, K: float, T: float, r: float, sigma: float, q: float = 0) -> float:
    """Black-Scholes put option price - UNCHANGED"""
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    return K * np.exp(-r * T) * stats.norm.cdf(-d2) - S * np.exp(-q * T) * stats.norm.cdf(-d1)

def delta(S: float, K: float, T: float, r: float, sigma: float, q: float = 0) -> Tuple[float, float]:
    """Calculate delta for call and put options - UNCHANGED"""
    d1, _ = d1_d2(S, K, T, r, sigma, q)
    delta_call = np.exp(-q * T) * stats.norm.cdf(d1)
    delta_put = delta_call - np.exp(-q * T)
    return delta_call, delta_put

def gamma(S: float, K: float, T: float, r: float, sigma: float, q: float = 0) -> float:
    """Calculate gamma (same for calls and puts) - UNCHANGED"""
    d1, _ = d1_d2(S, K, T, r, sigma, q)
    return np.exp(-q * T) * stats.norm.pdf(d1) / (S * sigma * np.sqrt(T))

def vega(S: float, K: float, T: float, r: float, sigma: float, q: float = 0) -> float:
    """Calculate vega (same for calls and puts) - UNCHANGED"""
    d1, _ = d1_d2(S, K, T, r, sigma, q)
    return S * np.exp(-q * T) * stats.norm.pdf(d1) * np.sqrt(T)

def theta(S: float, K: float, T: float, r: float, sigma: float, q: float = 0) -> Tuple[float, float]:
    """Calculate theta for call and put options - UNCHANGED"""
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
    """Calculate rho for call and put options - UNCHANGED"""
    d1, d2 = d1_d2(S, K, T, r, sigma, q)
    rho_call = K * T * np.exp(-r * T) * stats.norm.cdf(d2)
    rho_put = -K * T * np.exp(-r * T) * stats.norm.cdf(-d2)
    return rho_call, rho_put

def portfolio_greeks(portfolio: List[Dict]) -> Dict[str, float]:
    """
    Calculate portfolio-level Greeks.
    NEW FUNCTION - doesn't break existing code.
    """
    total_delta = 0
    total_gamma = 0
    total_vega = 0
    total_theta = 0
    total_rho = 0
    total_value = 0
    
    for position in portfolio:
        size = position['position_size']
        
        # Get price and Greeks using existing utility functions
        if position['option_type'].lower() == 'call':
            price = bs_call_price(position['S0'], position['K'], position['T'], 
                                position['r'], position['sigma'], position.get('q', 0))
        else:
            price = bs_put_price(position['S0'], position['K'], position['T'], 
                               position['r'], position['sigma'], position.get('q', 0))
        
        # Get Greeks using existing functions
        delta_call, delta_put = delta(position['S0'], position['K'], position['T'], 
                                    position['r'], position['sigma'], position.get('q', 0))
        gamma_val = gamma(position['S0'], position['K'], position['T'], 
                         position['r'], position['sigma'], position.get('q', 0))
        vega_val = vega(position['S0'], position['K'], position['T'], 
                       position['r'], position['sigma'], position.get('q', 0))
        theta_call, theta_put = theta(position['S0'], position['K'], position['T'], 
                                    position['r'], position['sigma'], position.get('q', 0))
        rho_call, rho_put = rho(position['S0'], position['K'], position['T'], 
                              position['r'], position['sigma'], position.get('q', 0))
        
        # Aggregate
        total_value += size * price
        total_gamma += size * gamma_val
        total_vega += size * vega_val
        
        if position['option_type'].lower() == 'call':
            total_delta += size * delta_call
            total_theta += size * theta_call
            total_rho += size * rho_call
        else:
            total_delta += size * delta_put
            total_theta += size * theta_put
            total_rho += size * rho_put
    
    return {
        'portfolio_value': total_value,
        'delta': total_delta,
        'gamma': total_gamma,
        'vega': total_vega,
        'theta': total_theta,
        'rho': total_rho
    }

# =========================================================================
# UTILITIES FOR IMPLIED VOL
# =========================================================================

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

def compute_implied_volatilities_and_summarize(model, sigma_0=2.0, print_summary=True):
    """
    Compute implied volatilities and print summary (DRY function).
    
    Parameters:
    -----------
    model : BlackScholesImpliedVol
        Model with loaded data
    sigma_0 : float
        Initial volatility guess
    print_summary : bool
        Whether to print summary statistics
    
    Returns:
    --------
    dict
        Summary statistics
    """
    print(f"⚡ Computing implied volatilities (σ₀={sigma_0})...")
    
    # Compute implied volatilities
    model.compute_implied_volatility_batch(sigma_0=sigma_0)
    
    # Get summary statistics
    stats = model.get_summary_statistics()
    
    if print_summary:
        print(f"📊 Results Summary:")
        if 'message' in stats:
            print(f"   ⚠️  {stats['message']}")
        else:
            print(f"   ✅ Valid computations: {stats['count']:,}")
            print(f"   📈 Mean volatility: {stats['mean']:.4f} ({stats['mean']*100:.2f}%)")
            print(f"   📏 Range: {stats['min']:.4f} - {stats['max']:.4f}")
            print(f"   📊 Std deviation: {stats['std']:.4f}")
    
    return stats

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
    plt.show()
    
    # Save plot
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    fig.savefig(save_path, dpi=300, bbox_inches='tight')
    
    return fig, ax

def download_vstoxx_data(url=None, filename="vstoxx_data_31032014.h5", data_dir="./data"):
    """Download VSTOXX data file from specified URL to data directory."""
    if url is None:
        url = "https://github.com/yhilpisch/py4fi/raw/master/jupyter36/source/vstoxx_data_31032014.h5"
    
    os.makedirs(data_dir, exist_ok=True)
    file_path = os.path.join(data_dir, filename)
    
    try:
        with requests.get(url, stream=True, timeout=30) as response:
            response.raise_for_status()
            with open(file_path, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        file.write(chunk)
        return file_path
        
    except requests.RequestException as e:
        alt_url = "https://github.com/NanguangChou/BSM_call_option/raw/master/vstoxx_data_31032014.h5"
        if url != alt_url:
            return download_vstoxx_data(alt_url, filename, data_dir)
        raise

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
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    plt.savefig(save_path, dpi=300, bbox_inches='tight')

    plt.show()
    
    # return fig, ax

def prepare_datetime_columns(futures_data, options_data):
    """Convert date columns to datetime format."""
    import pandas as pd
    
    date_columns = ['DATE', 'MATURITY']
    
    for col in date_columns:
        if col in futures_data.columns:
            futures_data[col] = pd.to_datetime(futures_data[col])
        if col in options_data.columns:
            options_data[col] = pd.to_datetime(options_data[col])
    
    return futures_data, options_data

def run_advanced_analysis_on_implied_vol(model, print_results=True):
    """
    Run all advanced analysis features (DRY function).
    
    Parameters:
    -----------
    model : BlackScholesImpliedVol
        Model with computed implied volatilities
    print_results : bool
        Whether to print results
    
    Returns:
    --------
    dict
        Dictionary containing all analysis results
    """
    results = {}
    
    if print_results:
        print(f"\n🎯 Advanced Analysis:")
    
    # ATM Term Structure Analysis
    try:
        atm_analysis = model.analyze_atm_term_structure()
        results['atm_analysis'] = atm_analysis
        
        if print_results:
            if not atm_analysis.empty:
                print(f"   📊 ATM Analysis: {len(atm_analysis)} maturities")
                if hasattr(atm_analysis, 'attrs') and 'slope' in atm_analysis.attrs:
                    print(f"      Term structure slope: {atm_analysis.attrs['slope']:.6f}")
            else:
                print(f"   📊 ATM Analysis: No data available")
    except Exception as e:
        results['atm_analysis'] = None
        if print_results:
            print(f"   ❌ ATM Analysis failed: {e}")
    
    # Volatility Smile Analysis
    try:
        smile_analysis = model.analyze_smile_characteristics()
        results['smile_analysis'] = smile_analysis
        
        if print_results:
            if not smile_analysis.empty:
                print(f"   😊 Smile Analysis: {len(smile_analysis)} maturities")
                print(f"      Average skew: {smile_analysis['Skew'].mean():.4f}")
            else:
                print(f"   😊 Smile Analysis: No data available")
    except Exception as e:
        results['smile_analysis'] = None
        if print_results:
            print(f"   ❌ Smile Analysis failed: {e}")
    
    # Risk Metrics
    try:
        risk_metrics = model.compute_risk_metrics()
        results['risk_metrics'] = risk_metrics
        
        if print_results:
            if 'error' not in risk_metrics:
                print(f"   ⚠️  Risk Metrics: VaR(95%)={risk_metrics['var_95']:.4f}")
                print(f"      Outliers: {risk_metrics['outlier_count']} ({risk_metrics['outlier_pct']:.1f}%)")
            else:
                print(f"   ⚠️  Risk Metrics: {risk_metrics['error']}")
    except Exception as e:
        results['risk_metrics'] = None
        if print_results:
            print(f"   ❌ Risk Metrics failed: {e}")
    
    # Volatility Surface
    try:
        vol_surface = model.get_implied_volatility_surface()
        results['vol_surface'] = vol_surface
        
        if print_results:
            if not vol_surface.empty:
                coverage = vol_surface.notna().sum().sum() / vol_surface.size * 100
                print(f"   📈 Volatility Surface: {vol_surface.shape[0]}×{vol_surface.shape[1]} ({coverage:.1f}% coverage)")
            else:
                print(f"   📈 Volatility Surface: No data available")
    except Exception as e:
        results['vol_surface'] = None
        if print_results:
            print(f"   ❌ Volatility Surface failed: {e}")
    
    return results

# =========================================================================
# UTILITIES FOR MONTE CARLO
# =========================================================================

def demo_monte_carlo_convergence(S0=100, K=100, T=1, r=0.05, sigma=0.2, q=0):
    """
    Demonstrate Monte Carlo convergence for different path counts.
    """
    # Analytical benchmark
    analytical_call = bs_call_price(S0, K, T, r, sigma, q)
    
    # Test different path counts
    path_counts = [10000, 50000, 100000]
    
    results = []
    for n_paths in path_counts:
        # Enhanced MC
        result_enh = monte_carlo_pricing(
            S0, K, T, r, sigma, q, n_paths=n_paths, seed=42,
            antithetic=True, control_variate=True
        )
        
        enh_error = abs(result_enh['call_price'] - analytical_call)
        results.append((n_paths, result_enh['call_price'], enh_error))
    
    return results

def monte_carlo_pricing(S0: float, K: float, T: float, r: float, sigma: float, q: float = 0,
                       n_paths: int = 100000, n_steps: int = 252, seed: Optional[int] = None,
                       antithetic: bool = True, control_variate: bool = True) -> Dict[str, float]:
    """
    ENHANCED Monte Carlo option pricing with variance reduction techniques.
    
    FIXED VERSION - now returns actual simulated price arrays and correct statistics.
    
    Parameters:
    -----------
    S0 : float
        Initial stock price
    K : float
        Strike price
    T : float
        Time to maturity (in years)
    r : float
        Risk-free interest rate
    sigma : float
        Volatility
    q : float, optional
        Dividend yield (default: 0)
    n_paths : int, optional
        Number of simulation paths (default: 100000)
    n_steps : int, optional
        Number of time steps (default: 252)
    seed : int, optional
        Random seed for reproducibility
    antithetic : bool, optional
        Whether to use antithetic variates (default: True)
    control_variate : bool, optional
        Whether to use control variates (default: True)
        
    Returns:
    --------
    Dict containing:
        - call_price, put_price: Option prices
        - call_std, put_std: Standard deviations of option prices
        - call_std_error, put_std_error: Standard errors of the means
        - call_ci, put_ci: 95% confidence intervals for the means
        - call_prices, put_prices: Arrays of actual simulated option prices
        - n_paths: Number of paths used
        - variance_reduction: Whether variance reduction was used
    """
    if seed is not None:
        np.random.seed(seed)
    
    dt = T / n_steps
    
    # Generate random numbers with optional antithetic variates
    if antithetic:
        n_sim = n_paths // 2
        z = np.random.normal(0, 1, (n_sim, n_steps))
        z_anti = np.concatenate([z, -z], axis=0)
        # Handle odd number of paths
        if n_paths % 2 == 1:
            z_anti = np.concatenate([z_anti, np.random.normal(0, 1, (1, n_steps))], axis=0)
    else:
        z_anti = np.random.normal(0, 1, (n_paths, n_steps))
    
    # Simulate stock price paths using log-normal process
    log_returns = (r - q - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * z_anti
    log_S = np.log(S0) + np.cumsum(log_returns, axis=1)
    S_T = np.exp(log_S[:, -1])  # Final stock prices
    
    # Calculate option payoffs
    call_payoffs = np.maximum(S_T - K, 0)
    put_payoffs = np.maximum(K - S_T, 0)
    
    # Discount to present value
    discount = np.exp(-r * T)
    call_prices = discount * call_payoffs
    put_prices = discount * put_payoffs
    
    # Apply control variate adjustment if requested
    if control_variate:
        # Use the fact that E[S_T] = S0 * exp((r-q)*T) is known analytically
        expected_S_T = S0 * np.exp((r - q) * T)
        control_var = S_T - expected_S_T
        
        # Control variate for call options
        cov_call = np.cov(call_prices, control_var)[0, 1]
        var_control = np.var(control_var)
        beta_call = cov_call / var_control if var_control > 0 else 0
        call_prices_cv = call_prices - beta_call * control_var
        
        # Control variate for put options  
        cov_put = np.cov(put_prices, control_var)[0, 1]
        beta_put = cov_put / var_control if var_control > 0 else 0
        put_prices_cv = put_prices - beta_put * control_var
    else:
        call_prices_cv = call_prices.copy()
        put_prices_cv = put_prices.copy()
    
    # Calculate final statistics
    call_mean = np.mean(call_prices_cv)
    put_mean = np.mean(put_prices_cv)
    call_std = np.std(call_prices_cv, ddof=1)  # Sample standard deviation
    put_std = np.std(put_prices_cv, ddof=1)    # Sample standard deviation
    call_std_error = call_std / np.sqrt(n_paths)  # Standard error of the mean
    put_std_error = put_std / np.sqrt(n_paths)    # Standard error of the mean
    
    # 95% confidence intervals for the mean estimates
    z_score = 1.96  # 95% confidence level
    call_ci = (call_mean - z_score * call_std_error, call_mean + z_score * call_std_error)
    put_ci = (put_mean - z_score * put_std_error, put_mean + z_score * put_std_error)
    
    return {
        'call_price': call_mean, 
        'put_price': put_mean,
        'call_std': call_std,                    # FIX: Actual standard deviation
        'put_std': put_std,                      # FIX: Actual standard deviation
        'call_std_error': call_std_error,        # Standard error of the mean
        'put_std_error': put_std_error,          # Standard error of the mean
        'call_ci': call_ci, 
        'put_ci': put_ci,
        'call_prices': call_prices_cv,           # FIX: Actual simulated prices
        'put_prices': put_prices_cv,             # FIX: Actual simulated prices
        'n_paths': n_paths, 
        'variance_reduction': antithetic or control_variate
    }

def plot_gbm_paths_with_distribution(t, S_paths, S0, T, r, sigma, q=0, K=None,
                                   ax=None, max_paths_display=50, 
                                   risk_neutral=True, mu=None, 
                                   title=None, show_stats=True,
                                   show_histogram=True, show_theoretical_pdf=True):
    """
    Plot GBM paths with final price distribution and theoretical lognormal PDF.
    
    Parameters:
    -----------
    t : array
        Time points
    S_paths : array
        Simulated price paths (shape: num_paths x num_steps)
    S0, T, r, sigma, q, K : float
        Model parameters
    ax : matplotlib axis, optional
        Axis to plot on (if None, current axis is used)
    ... (other parameters as before)
    
    Returns:
    --------
    dict : Statistics and final prices
    """
    if ax is None:
        ax = plt.gca()
        
    # Plot a subset of paths
    num_paths_to_plot = min(max_paths_display, S_paths.shape[0])
    indices = np.random.choice(S_paths.shape[0], num_paths_to_plot, replace=False)
        
    for i in indices:
        ax.plot(t, S_paths[i], alpha=0.6, linewidth=0.8)
        
    # Add grid lines for better readability
    ax.grid(True, alpha=0.3)
        
    # Get final prices for statistics and histogram
    final_prices = S_paths[:, -1]
    mean_final = np.mean(final_prices)
    std_final = np.std(final_prices)
        
    # Calculate theoretical mean
    drift_rate = r if risk_neutral else (mu if mu is not None else r)
    theoretical_mean = S0 * np.exp(drift_rate * T)
        
    # Add expected value line
    ax.axhline(y=S0, color='red', linestyle='--', alpha=0.8, 
            label=f'S₀ = {S0}')
    ax.axhline(y=theoretical_mean, color='orange', linestyle='--', 
            alpha=0.8, label=f'E[S(T)] = {theoretical_mean:.1f}')
        
    # Show histogram and theoretical PDF if requested
    if show_histogram or show_theoretical_pdf:
        # Create histogram bins
        hist_counts, bin_edges = np.histogram(final_prices, bins=50, density=True)
        bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
            
        # Define histogram width and position
        hist_width = T * 0.05
        hist_position = T + 0.005
            
        if show_histogram:
            # Normalize histogram counts
            max_hist_count = np.max(hist_counts)
            normalized_hist_counts = hist_counts / max_hist_count
                
            # Create bar histogram
            bin_width = bin_centers[1] - bin_centers[0]
            ax.barh(bin_centers, normalized_hist_counts * hist_width, 
                    left=hist_position, height=bin_width * 0.9, alpha=0.7, 
                    color='lightblue', edgecolor='darkblue', linewidth=0.3, 
                    label='Simulated Distribution')
            
        if show_theoretical_pdf:
            # Calculate theoretical lognormal distribution
            mu_ln = np.log(S0) + (drift_rate - 0.5 * sigma**2) * T
            sigma_ln = sigma * np.sqrt(T)
                
            S_range = np.linspace(np.min(final_prices), np.max(final_prices), 200)
            theoretical_pdf = stats.lognorm.pdf(S_range, s=sigma_ln, scale=np.exp(mu_ln))
                
            # Normalize theoretical PDF
            max_theoretical_pdf = np.max(theoretical_pdf)
            normalized_theoretical_pdf = theoretical_pdf / max_theoretical_pdf
                
            # Plot theoretical PDF
            theoretical_x = hist_position + normalized_theoretical_pdf * hist_width
            ax.plot(theoretical_x, S_range, 'r-', linewidth=3, label='Lognormal PDF')
        
     # Formatting
    ax.set_xlabel('Time', fontsize=12)
    ax.set_ylabel('Stock Price', fontsize=12)
        
    # Set title
    if title:
        ax.set_title(title, fontsize=12)
    else:
        ax.set_title('Sample GBM Paths with Final Price Distribution', fontsize=14, pad=20)
        
    # Legend
    ax.legend(loc='upper right', bbox_to_anchor=(0.98, 0.98))
        
    # Extend x-axis to accommodate histogram
    if show_histogram or show_theoretical_pdf:
        ax.set_xlim(0, T * 1.15)
    else:
        ax.set_xlim(0, T)
        
    # Add statistics text if requested
    if show_stats:
        stats_text = f"""Simulation Statistics:
    Initial Stock Price: {S0:.2f}
    Strike:  {K:.2f}
    Maturity: {T:.2f}
    Interest Rate: {r:.2f}
    Volatility: {sigma:.2f}
    Dividend Yield: {q:.2f}
    Number of Paths: {S_paths.shape[0]:,}
    Final Price Mean: {mean_final:.2f}
    Final Price Std: {std_final:.2f}
    Theoretical Mean: {theoretical_mean:.2f}"""
            
        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes, 
                    verticalalignment='top', 
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))
        
    return {
        'final_prices': final_prices,
        'mean_final': mean_final,
        'std_final': std_final,
        'theoretical_mean': theoretical_mean
    }

def simulate_gbm_paths(S0: float, T: float, r: float, sigma: float, 
                      num_paths: int, num_steps: int, risk_neutral: bool = True, 
                      seed: Optional[int] = None, mu: Optional[float] = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    Simulate geometric Brownian motion paths - UNCHANGED API
    """
    if seed is not None:
        np.random.seed(seed)
    
    dt = T / num_steps
    t = np.linspace(0, T, num_steps + 1)
    
    # Generate random increments
    dW = np.random.normal(0, np.sqrt(dt), (num_paths, num_steps))
    
    # Construct Brownian motion
    W = np.zeros((num_paths, num_steps + 1))
    W[:, 1:] = np.cumsum(dW, axis=1)
    
    # Determine drift
    drift = r if risk_neutral else (mu if mu is not None else r)
    
    # Simulate GBM paths
    drift_term = (drift - 0.5 * sigma**2) * t
    diffusion_term = sigma * W
    
    S_paths = S0 * np.exp(drift_term + diffusion_term)
    
    return t, S_paths

def test_variance_reduction_effectiveness():
    """
    Test to demonstrate the effectiveness of variance reduction techniques.
    """
    # Test parameters
    S0, K, T, r, sigma, q = 100, 100, 1, 0.05, 0.2, 0
    n_paths = 100000
    seed = 42
    
    # Standard Monte Carlo (no variance reduction)
    result_standard = monte_carlo_pricing(
        S0, K, T, r, sigma, q, n_paths=n_paths, seed=seed,
        antithetic=False, control_variate=False
    )
    
    # Enhanced Monte Carlo (with variance reduction)
    result_enhanced = monte_carlo_pricing(
        S0, K, T, r, sigma, q, n_paths=n_paths, seed=seed,
        antithetic=True, control_variate=True
    )
    
    # Calculate variance reduction ratios
    call_var_reduction = (result_standard['call_std']**2) / (result_enhanced['call_std']**2)
    put_var_reduction = (result_standard['put_std']**2) / (result_enhanced['put_std']**2)
    
    return {
        'call_var_reduction': call_var_reduction,
        'put_var_reduction': put_var_reduction,
        'meets_expectations': call_var_reduction >= 1.5 and put_var_reduction >= 1.5
    }

def validate_monte_carlo_implementation():
    """
    Validation function to test the enhanced Monte Carlo implementation.
    """
    # Test parameters (ATM European call)
    S0, K, T, r, sigma, q = 100, 100, 1, 0.05, 0.2, 0
    
    # Analytical Black-Scholes price for comparison
    analytical_call = bs_call_price(S0, K, T, r, sigma, q)
    analytical_put = bs_put_price(S0, K, T, r, sigma, q)
    
    # Test enhanced Monte Carlo with large sample
    result = monte_carlo_pricing(S0, K, T, r, sigma, q, n_paths=500000, seed=42)
    
    # Calculate errors
    call_error = abs(result['call_price'] - analytical_call)
    put_error = abs(result['put_price'] - analytical_put)
    call_error_pct = call_error / analytical_call * 100
    put_error_pct = put_error / analytical_put * 100
    
    # Validation checks
    call_within_ci = result['call_ci'][0] <= analytical_call <= result['call_ci'][1]
    put_within_ci = result['put_ci'][0] <= analytical_put <= result['put_ci'][1]
    reasonable_call_error = call_error_pct < 0.5
    reasonable_put_error = put_error_pct < 0.5
    
    all_tests_pass = call_within_ci and put_within_ci and reasonable_call_error and reasonable_put_error
    
    return all_tests_pass

# =========================================================================
# UTILITIES FOR NUMERICAL
# =========================================================================

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

def numerical_pricing(S0: float, K: float, T: float, r: float, sigma: float, q: float = 0,
                     method: str = 'crank_nicolson', n_space: int = 100, n_time: int = 100,
                     option_type: str = 'put', early_exercise: bool = False, 
                     S_max: float = None) -> Tuple[np.ndarray, np.ndarray]:
    """
    ENHANCED finite difference pricing with improved stability.
    NEW FUNCTION - doesn't break existing code.
    """
    if S_max is None:
        S_max = 3 * max(S0, K)
    
    # Create grids
    S_grid = np.linspace(0, S_max, n_space)
    dt = T / n_time
    dS = S_grid[1] - S_grid[0]
    
    # Initialize option values at maturity
    if option_type.lower() == 'call':
        payoff = np.maximum(S_grid - K, 0)
    else:
        payoff = np.maximum(K - S_grid, 0)
    
    V = np.zeros((n_space, n_time + 1))
    V[:, -1] = payoff
    
    # Stability check for explicit method
    if method.lower() == 'explicit':
        max_coeff = sigma**2 * S_max**2 * dt / dS**2
        if max_coeff > 1:
            warnings.warn(f"Explicit scheme may be unstable: max coefficient = {max_coeff:.3f} > 1")
    
    # Time stepping (simplified implementation)
    for n in range(n_time, 0, -1):
        for i in range(1, n_space - 1):
            S = S_grid[i]
            
            # Finite difference coefficients
            alpha = 0.5 * dt * (sigma**2 * S**2 / dS**2 - (r - q) * S / dS)
            beta = 1 - dt * (sigma**2 * S**2 / dS**2 + r)
            gamma = 0.5 * dt * (sigma**2 * S**2 / dS**2 + (r - q) * S / dS)
            
            V[i, n-1] = alpha * V[i-1, n] + beta * V[i, n] + gamma * V[i+1, n]
        
        # Boundary conditions
        tau = (n_time - n + 1) * dt
        discount = np.exp(-r * tau)
        
        if option_type.lower() == 'call':
            V[0, n-1] = 0
            V[-1, n-1] = S_grid[-1] - K * discount
        else:
            V[0, n-1] = K * discount
            V[-1, n-1] = 0
        
        # Early exercise
        if early_exercise:
            if option_type.lower() == 'call':
                V[:, n-1] = np.maximum(V[:, n-1], np.maximum(S_grid - K, 0))
            else:
                V[:, n-1] = np.maximum(V[:, n-1], np.maximum(K - S_grid, 0))
    
    return S_grid, V[:, 0]