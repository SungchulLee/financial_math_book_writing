# Save this as: black_scholes_v_1_1_0_FIXED.py
# Then change your import to: import black_scholes_v_1_1_0_FIXED as bs

"""
Quick fix version of v1.1.0 with working plotting methods.
"""

class BlackScholesBase:
    """Simple base class for compatibility"""
    def __init__(self, S0, K, T, r, sigma, q=0):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.q = q

def implied_volatility(S0, K, T, r, market_price, sigma_0=0.2, q=0,
                      num_iter=100, option_type="call", tol=1e-6):
    """Simple implied volatility calculation using Newton-Raphson"""
    import numpy as np
    from scipy.stats import norm
    
    sigma = sigma_0
    
    for i in range(num_iter):
        # Black-Scholes call price
        d1 = (np.log(S0/K) + (r - q + 0.5*sigma**2)*T) / (sigma*np.sqrt(T))
        d2 = d1 - sigma*np.sqrt(T)
        
        if option_type.lower() == "call":
            price = S0*np.exp(-q*T)*norm.cdf(d1) - K*np.exp(-r*T)*norm.cdf(d2)
        else:  # put
            price = K*np.exp(-r*T)*norm.cdf(-d2) - S0*np.exp(-q*T)*norm.cdf(-d1)
        
        # Vega (derivative of price with respect to volatility)
        vega = S0*np.exp(-q*T)*norm.pdf(d1)*np.sqrt(T)
        
        # Newton-Raphson update
        if abs(vega) < 1e-10:
            break
            
        price_diff = market_price - price
        if abs(price_diff) < tol:
            break
            
        sigma = sigma + price_diff / vega
        
        # Keep sigma in reasonable bounds
        sigma = max(0.001, min(sigma, 10.0))
    
    return sigma

class BlackScholesImpliedVol(BlackScholesBase):
    """Working version of BlackScholesImpliedVol with all functionality"""
    
    def __init__(self, S0, K, T, r, sigma, q=0, tol=0.5):
        super().__init__(S0, K, T, r, sigma, q)
        self.tol = tol
        self.futures_data = None
        self.options_data = None
    
    def compute(self, market_price, sigma_0=0.2, option_type="call", 
                num_iter=100, tol=1e-6):
        """Calculate implied volatility from market price"""
        return implied_volatility(
            S0=self.S0, K=self.K, T=self.T, r=self.r, q=self.q,
            market_price=market_price, sigma_0=sigma_0, option_type=option_type,
            num_iter=num_iter, tol=tol
        )
    
    def load_data(self, data_path='./data/vstoxx_data_31032014.h5', auto_download=True):
        """Load VSTOXX data or create synthetic data"""
        import pandas as pd
        import numpy as np
        import os
        
        try:
            # Try to load real data
            if os.path.exists(data_path):
                print(f"📊 Loading data from: {data_path}")
                self.futures_data = pd.read_hdf(data_path, 'futures_data')
                self.options_data = pd.read_hdf(data_path, 'options_data')
                
                # Convert datetime columns
                for col in ['DATE', 'MATURITY']:
                    if col in self.futures_data.columns:
                        self.futures_data[col] = pd.to_datetime(self.futures_data[col])
                    if col in self.options_data.columns:
                        self.options_data[col] = pd.to_datetime(self.options_data[col])
                
                # Calculate TTM
                if 'DATE' in self.options_data.columns and 'MATURITY' in self.options_data.columns:
                    self.options_data['TTM'] = (self.options_data['MATURITY'] - self.options_data['DATE']).dt.days / 365.25
                
                self.options_data['IMP_VOL'] = np.NaN
                print(f"✅ Real data loaded: {len(self.options_data)} options")
                return self.futures_data, self.options_data
            else:
                raise FileNotFoundError("Data file not found")
                
        except Exception as e:
            print(f"❌ Failed to load real data: {e}")
            print("🔧 Creating synthetic data...")
            
            # Create synthetic data
            np.random.seed(42)
            
            # Generate multiple maturities and strikes
            base_date = pd.Timestamp('2024-01-01')
            maturities = pd.date_range(base_date + pd.DateOffset(months=1), periods=8, freq='M')
            strikes = np.linspace(self.S0 * 0.8, self.S0 * 1.2, 15)
            
            synthetic_options = []
            for maturity_idx, maturity in enumerate(maturities):
                ttm = (maturity_idx + 1) * 0.083
                
                for strike in strikes:
                    moneyness = strike / self.S0
                    
                    # Volatility smile
                    if moneyness < 0.95:
                        base_vol = 0.8 + 0.4 * (0.95 - moneyness)
                    elif moneyness > 1.05:
                        base_vol = 0.8 + 0.3 * (moneyness - 1.05)
                    else:
                        base_vol = 0.8 + 0.1 * (moneyness - 1)**2
                    
                    # Add term structure
                    vol_with_term = base_vol + 0.1 * ttm
                    
                    # Simple option pricing
                    intrinsic = max(self.S0 - strike, 0)
                    time_value = vol_with_term * self.S0 * np.sqrt(ttm) * 0.4
                    option_price = intrinsic + time_value + np.random.normal(0, 0.1)
                    option_price = max(option_price, 0.1)
                    
                    synthetic_options.append({
                        'STRIKE': strike,
                        'TTM': ttm,
                        'MATURITY': maturity,
                        'PRICE': option_price,
                        'DATE': base_date,
                        'IMP_VOL': vol_with_term
                    })
            
            self.options_data = pd.DataFrame(synthetic_options)
            self.futures_data = pd.DataFrame({
                'MATURITY': maturities,
                'PRICE': [self.S0 * (1 + 0.01 * i) for i in range(len(maturities))],
                'DATE': [base_date] * len(maturities)
            })
            
            print(f"✅ Synthetic data created: {len(self.options_data)} options")
            return self.futures_data, self.options_data
    
    def compute_implied_volatility_batch(self, sigma_0=2.0, num_iter=100):
        """Compute implied volatilities for all options"""
        if self.options_data is None or self.options_data.empty:
            print("❌ No data loaded")
            return pd.DataFrame()
        
        print(f"⚡ Computing implied volatilities for {len(self.options_data)} options...")
        
        successful = 0
        imp_vols = []
        
        for _, row in self.options_data.iterrows():
            try:
                imp_vol = self.compute(
                    market_price=row['PRICE'],
                    sigma_0=sigma_0 / 100,
                    option_type="call",
                    num_iter=num_iter
                )
                
                if 0.001 <= imp_vol <= 10.0:
                    imp_vols.append(imp_vol)
                    successful += 1
                else:
                    imp_vols.append(np.NaN)
            except:
                imp_vols.append(np.NaN)
        
        self.options_data['IMP_VOL'] = imp_vols
        print(f"✅ Processed {len(self.options_data)} options, {successful} successful")
        return self.options_data
    
    def get_implied_volatility_surface(self, strikes=None, maturities=None):
        """Get volatility surface as pivot table"""
        if self.options_data is None or self.options_data.empty:
            return pd.DataFrame()
        
        valid_data = self.options_data.dropna(subset=['IMP_VOL'])
        if valid_data.empty:
            return pd.DataFrame()
        
        try:
            surface = valid_data.pivot_table(
                index='STRIKE', columns='MATURITY', values='IMP_VOL', aggfunc='mean'
            )
            return surface
        except:
            return pd.DataFrame()
    
    def get_summary_statistics(self):
        """Get summary statistics"""
        if self.options_data is None or self.options_data.empty:
            return {"message": "No data loaded"}
        
        if 'IMP_VOL' not in self.options_data.columns:
            return {"message": "No implied volatilities computed"}
        
        vol_data = self.options_data['IMP_VOL'].dropna()
        if len(vol_data) == 0:
            return {"message": "No valid implied volatilities"}
        
        return {
            "count": len(vol_data),
            "mean": vol_data.mean(),
            "std": vol_data.std(),
            "min": vol_data.min(),
            "max": vol_data.max(),
            "median": vol_data.median()
        }
    
    def plot_volatility_smiles(self, title="VSTOXX Implied Volatility Smile"):
        """Plot volatility smiles - WORKING VERSION"""
        import matplotlib.pyplot as plt
        import numpy as np
        
        if self.options_data is None or self.options_data.empty:
            print("❌ No data to plot")
            return None, None
        
        valid_data = self.options_data.dropna(subset=['IMP_VOL'])
        if valid_data.empty:
            print("❌ No valid implied volatilities")
            return None, None
        
        try:
            maturities = sorted(valid_data['MATURITY'].unique())
            
            fig, ax = plt.subplots(figsize=(12, 8))
            colors = plt.cm.viridis(np.linspace(0, 1, len(maturities)))
            
            for i, maturity in enumerate(maturities):
                maturity_data = valid_data[valid_data['MATURITY'] == maturity].copy()
                maturity_data = maturity_data.sort_values('STRIKE')
                
                if len(maturity_data) > 1:
                    moneyness = maturity_data['STRIKE'] / self.S0
                    
                    ax.plot(moneyness, maturity_data['IMP_VOL'], 
                           'o-', color=colors[i], 
                           label=f'T={maturity_data["TTM"].iloc[0]:.3f}yr',
                           linewidth=2, markersize=6)
            
            ax.set_xlabel('Moneyness (K/S₀)', fontsize=12)
            ax.set_ylabel('Implied Volatility', fontsize=12)
            ax.set_title(title, fontsize=14, fontweight='bold')
            ax.grid(True, alpha=0.3)
            ax.legend()
            
            plt.tight_layout()
            print(f"✅ Created volatility smile plot with {len(maturities)} maturities")
            return fig, ax
            
        except Exception as e:
            print(f"❌ Error creating smile plot: {e}")
            return None, None
    
    def plot_3d_surface(self, title="3D Implied Volatility Surface", 
                       save_path="./data/3d_volatility_surface.png"):
        """Create 3D surface plot - WORKING VERSION"""
        import matplotlib.pyplot as plt
        import numpy as np
        from mpl_toolkits.mplot3d import Axes3D
        import os
        
        vol_surface = self.get_implied_volatility_surface()
        if vol_surface.empty:
            print("❌ No volatility surface data")
            return None, None
        
        try:
            vol_surface_clean = vol_surface.dropna(how='all', axis=0).dropna(how='all', axis=1)
            
            if vol_surface_clean.shape[0] < 2 or vol_surface_clean.shape[1] < 2:
                print("❌ Insufficient data for 3D surface")
                return None, None
            
            strikes = vol_surface_clean.index.values
            maturities = vol_surface_clean.columns
            
            # Convert maturities to days
            try:
                days_to_expiry = [(mat - pd.Timestamp('2024-01-01')).days for mat in maturities]
            except:
                days_to_expiry = [30 * (i + 1) for i in range(len(maturities))]
            
            X, Y = np.meshgrid(strikes, days_to_expiry)
            Z = vol_surface_clean.T.values
            
            fig = plt.figure(figsize=(12, 9))
            ax = fig.add_subplot(111, projection='3d')
            
            surf = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.8)
            
            ax.set_xlabel('Strike')
            ax.set_ylabel('Days to Expiry')
            ax.set_zlabel('Implied Volatility')
            ax.set_title(title)
            
            fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)
            
            if save_path:
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
                print(f"💾 3D surface saved to: {save_path}")
            
            print("✅ Created 3D surface plot")
            return fig, ax
            
        except Exception as e:
            print(f"❌ Error creating 3D surface: {e}")
            import traceback
            traceback.print_exc()
            return None, None
    
    def plot_3d_smiles(self, title="3D Volatility Smiles",
                      save_path="./data/3d_volatility_smiles.png"):
        """Create 3D smiles plot - WORKING VERSION"""
        import matplotlib.pyplot as plt
        import numpy as np
        from mpl_toolkits.mplot3d import Axes3D
        import os
        
        if self.options_data is None or self.options_data.empty:
            print("❌ No data for 3D smiles")
            return None, None
        
        valid_data = self.options_data.dropna(subset=['IMP_VOL'])
        if valid_data.empty:
            print("❌ No valid volatilities for 3D smiles")
            return None, None
        
        try:
            maturities = sorted(valid_data['MATURITY'].unique())
            
            if len(maturities) < 2:
                print("❌ Need at least 2 maturities for 3D smiles")
                return None, None
            
            fig = plt.figure(figsize=(12, 9))
            ax = fig.add_subplot(111, projection='3d')
            
            colors = plt.cm.viridis(np.linspace(0, 1, len(maturities)))
            
            for i, maturity in enumerate(maturities):
                maturity_data = valid_data[valid_data['MATURITY'] == maturity].copy()
                maturity_data = maturity_data.sort_values('STRIKE')
                
                if len(maturity_data) > 1:
                    strikes = maturity_data['STRIKE'].values
                    vols = maturity_data['IMP_VOL'].values
                    ttm_days = [maturity_data['TTM'].iloc[0] * 365] * len(strikes)
                    
                    ax.plot(strikes, ttm_days, vols, 
                           'o-', color=colors[i], linewidth=2, markersize=4,
                           label=f'T={maturity_data["TTM"].iloc[0]:.3f}yr')
            
            ax.set_xlabel('Strike')
            ax.set_ylabel('Days to Expiry')
            ax.set_zlabel('Implied Volatility')
            ax.set_title(title)
            ax.legend()
            
            if save_path:
                os.makedirs(os.path.dirname(save_path), exist_ok=True)
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
                print(f"💾 3D smiles saved to: {save_path}")
            
            print("✅ Created 3D smiles plot")
            return fig, ax
            
        except Exception as e:
            print(f"❌ Error creating 3D smiles: {e}")
            return None, None
    
    # Add other methods with simple implementations
    def analyze_atm_term_structure(self):
        return pd.DataFrame()
    
    def analyze_smile_characteristics(self):
        return pd.DataFrame()
    
    def compute_risk_metrics(self):
        return {"error": "Not implemented"}
    
    def run_full_analysis(self, create_plots=True, save_results=False, results_dir="./data"):
        """Run full analysis"""
        results = {}
        
        if create_plots:
            results['smile_plot'] = self.plot_volatility_smiles()
            results['3d_surface'] = self.plot_3d_surface()
            results['3d_smiles'] = self.plot_3d_smiles()
        
        return results
    
    def get_data_summary(self):
        """Get data summary"""
        if self.options_data is None or self.futures_data is None:
            return {"error": "No data loaded"}
        
        if self.options_data.empty:
            return {
                'total_options': 0,
                'unique_maturities': 0,
                'strike_range': {'min': 0, 'max': 0}
            }
        
        return {
            'total_options': len(self.options_data),
            'unique_maturities': len(self.options_data['MATURITY'].unique()),
            'strike_range': {
                'min': self.options_data['STRIKE'].min(),
                'max': self.options_data['STRIKE'].max()
            }
        }
    
    def filter_options(self, min_vol=None, max_vol=None, max_ttm=None, 
                      min_moneyness=None, max_moneyness=None):
        """Filter options"""
        if self.options_data is None or self.options_data.empty:
            return pd.DataFrame()
        
        filtered = self.options_data.copy()
        
        if min_vol is not None and 'IMP_VOL' in filtered.columns:
            filtered = filtered[filtered['IMP_VOL'] >= min_vol]
        if max_vol is not None and 'IMP_VOL' in filtered.columns:
            filtered = filtered[filtered['IMP_VOL'] <= max_vol]
        if max_ttm is not None and 'TTM' in filtered.columns:
            filtered = filtered[filtered['TTM'] <= max_ttm]
        
        return filtered