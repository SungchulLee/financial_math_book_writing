# ============================================================================
# black_scholes/black_scholes_implied_vol.py
# ============================================================================
from .black_scholes_base import BlackScholesBase
from .black_scholes_utils import (
    implied_volatility, 
    load_vstoxx_data, 
    compute_batch_implied_volatility,
    get_volatility_surface,
    get_implied_vol_summary_stats,
    plot_volatility_smiles,
    # Advanced analysis functions
    analyze_atm_term_structure,
    analyze_volatility_smile_characteristics,
    compute_volatility_risk_metrics,
    plot_3d_volatility_surface,
    create_volatility_smile_3d
)

class BlackScholesImpliedVol(BlackScholesBase):
    """
    Enhanced Black-Scholes implied volatility calculator with advanced analysis.
    
    This class provides both basic implied volatility calculations and advanced
    analysis capabilities while maintaining clean separation of concerns by
    delegating computations to utility functions.
    """
    
    def __init__(self, S0, K, T, r, sigma, q=0, tol=0.5):
        """Initialize the implied volatility calculator."""
        super().__init__(S0, K, T, r, sigma, q)
        self.tol = tol
        self.futures_data = None
        self.options_data = None
    
    # =========================================================================
    # CORE FUNCTIONALITY
    # =========================================================================
    
    def compute(self, market_price, sigma_0=0.2, option_type="call", 
                num_iter=100, tol=1e-6):
        """Calculate implied volatility from market price."""
        return implied_volatility(
            S0=self.S0, K=self.K, T=self.T, r=self.r,
            market_price=market_price, sigma_0=sigma_0, q=self.q,
            num_iter=num_iter, option_type=option_type, tol=tol
        )
    
    def load_data(self, data_path='./data/vstoxx_data_31032014.h5', auto_download=True):
        """Load VSTOXX futures and options data."""
        self.futures_data, self.options_data = load_vstoxx_data(data_path, auto_download)
    
    def compute_implied_volatility_batch(self, sigma_0=2.0, num_iter=100):
        """Compute implied volatility for all loaded options."""
        if self.options_data is None or self.futures_data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        self.options_data = compute_batch_implied_volatility(
            options_data=self.options_data, futures_data=self.futures_data,
            S0=self.S0, sigma_0=sigma_0, num_iter=num_iter,
            tol=self.tol, r=self.r, q=self.q
        )
        return self.options_data
    
    # =========================================================================
    # BASIC ANALYSIS METHODS
    # =========================================================================
    
    def get_implied_volatility_surface(self, strikes=None, maturities=None):
        """Extract implied volatility surface as a pivot table."""
        if self.options_data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        return get_volatility_surface(self.options_data, strikes, maturities)
    
    def get_summary_statistics(self):
        """Get summary statistics of computed implied volatilities."""
        if self.options_data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        return get_implied_vol_summary_stats(self.options_data)
    
    def plot_volatility_smiles(self, title="VSTOXX Implied Volatility Smile"):
        """Generate volatility smile plots for different maturities."""
        if self.options_data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        return plot_volatility_smiles(self.options_data, title)
    
    # =========================================================================
    # ADVANCED ANALYSIS METHODS (Convenience wrappers)
    # =========================================================================
    
    def analyze_atm_term_structure(self):
        """
        Analyze at-the-money volatility term structure.
        
        Returns:
        --------
        pd.DataFrame
            ATM volatility data with term structure metrics
        """
        if self.options_data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        return analyze_atm_term_structure(self.options_data, self.S0)
    
    def analyze_smile_characteristics(self):
        """
        Analyze volatility smile characteristics across maturities.
        
        Returns:
        --------
        pd.DataFrame
            Smile characteristics by maturity
        """
        if self.options_data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        vol_surface = self.get_implied_volatility_surface()
        return analyze_volatility_smile_characteristics(vol_surface, self.S0)
    
    def compute_risk_metrics(self):
        """
        Compute risk metrics from implied volatility data.
        
        Returns:
        --------
        dict
            Dictionary containing various risk metrics
        """
        if self.options_data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        return compute_volatility_risk_metrics(self.options_data)
    
    def plot_3d_surface(self, title="3D Implied Volatility Surface", 
                       save_path="./data/3d_volatility_surface.png"):
        """
        Create a 3D surface plot of implied volatility.
        
        Parameters:
        -----------
        title : str
            Plot title
        save_path : str
            Path to save the plot
            
        Returns:
        --------
        tuple
            (matplotlib.Figure, matplotlib.Axes) or (None, None) if insufficient data
        """
        if self.options_data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        vol_surface = self.get_implied_volatility_surface()
        return plot_3d_volatility_surface(vol_surface, title, save_path)
    
    def plot_3d_smiles(self, title="3D Volatility Smiles",
                      save_path="./data/3d_volatility_smiles.png"):
        """
        Create a 3D plot showing volatility smiles across different maturities.
        
        Parameters:
        -----------
        title : str
            Plot title
        save_path : str
            Path to save the plot
            
        Returns:
        --------
        tuple
            (matplotlib.Figure, matplotlib.Axes)
        """
        if self.options_data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        vol_surface = self.get_implied_volatility_surface()
        return create_volatility_smile_3d(vol_surface, title, save_path)
    
    # =========================================================================
    # COMPREHENSIVE ANALYSIS METHODS
    # =========================================================================
    
    def run_full_analysis(self, create_plots=True, save_results=False, 
                         results_dir="./data/analysis_results"):
        """
        Run a comprehensive analysis of the implied volatility data.
        
        This method orchestrates all available analysis functions to provide
        a complete picture of the volatility surface and its characteristics.
        
        Parameters:
        -----------
        create_plots : bool, optional
            Whether to create visualization plots (default: True)
        save_results : bool, optional
            Whether to save results to files (default: False)
        results_dir : str, optional
            Directory to save results (default: "./data/analysis_results")
            
        Returns:
        --------
        dict
            Dictionary containing all analysis results
        """
        if self.options_data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        print("🔍 Running comprehensive implied volatility analysis...")
        
        results = {}
        
        # Basic statistics
        print("📊 Computing basic statistics...")
        results['summary_stats'] = self.get_summary_statistics()
        
        # Volatility surface
        print("📈 Extracting volatility surface...")
        results['vol_surface'] = self.get_implied_volatility_surface()
        
        # ATM term structure
        print("🎯 Analyzing ATM term structure...")
        results['atm_term_structure'] = self.analyze_atm_term_structure()
        
        # Smile characteristics
        print("😊 Analyzing smile characteristics...")
        results['smile_characteristics'] = self.analyze_smile_characteristics()
        
        # Risk metrics
        print("⚠️ Computing risk metrics...")
        results['risk_metrics'] = self.compute_risk_metrics()
        
        # Create plots if requested
        if create_plots:
            print("📊 Creating visualizations...")
            
            # Basic smile plots
            results['smile_plot'] = self.plot_volatility_smiles()
            
            # 3D surface plot
            if not results['vol_surface'].empty:
                results['3d_surface'] = self.plot_3d_surface()
                results['3d_smiles'] = self.plot_3d_smiles()
        
        # Save results if requested
        if save_results:
            print(f"💾 Saving results to {results_dir}...")
            self._save_analysis_results(results, results_dir)
        
        print("✅ Comprehensive analysis completed!")
        return results
    
    def _save_analysis_results(self, results, results_dir):
        """Save analysis results to files."""
        import os
        import json
        import pandas as pd
        
        os.makedirs(results_dir, exist_ok=True)
        
        # Save DataFrames as CSV
        for key, value in results.items():
            if isinstance(value, pd.DataFrame) and not value.empty:
                value.to_csv(os.path.join(results_dir, f"{key}.csv"), index=False)
        
        # Save dictionaries as JSON
        json_results = {}
        for key, value in results.items():
            if isinstance(value, dict):
                json_results[key] = value
        
        if json_results:
            with open(os.path.join(results_dir, "analysis_summary.json"), 'w') as f:
                json.dump(json_results, f, indent=2, default=str)
        
        # Save processed options data
        if self.options_data is not None:
            self.options_data.to_csv(os.path.join(results_dir, "processed_options.csv"), index=False)
    
    # =========================================================================
    # UTILITY METHODS
    # =========================================================================
    
    def get_data_summary(self):
        """Get a summary of the loaded data."""
        if self.options_data is None or self.futures_data is None:
            return {"error": "No data loaded"}
        
        valid_iv = self.options_data['IMP_VOL'].dropna()
        valid_iv = valid_iv[(valid_iv > 0) & (valid_iv < 50)]
        
        return {
            'total_options': len(self.options_data),
            'valid_implied_vols': len(valid_iv),
            'success_rate': len(valid_iv) / len(self.options_data) * 100,
            'date_range': {
                'start': self.options_data['DATE'].min(),
                'end': self.options_data['DATE'].max()
            },
            'unique_maturities': len(self.options_data['MATURITY'].unique()),
            'strike_range': {
                'min': self.options_data['STRIKE'].min(),
                'max': self.options_data['STRIKE'].max()
            },
            'futures_data_points': len(self.futures_data)
        }
    
    def filter_options(self, min_vol=None, max_vol=None, max_ttm=None, 
                      min_moneyness=None, max_moneyness=None):
        """
        Filter options based on various criteria.
        
        Parameters:
        -----------
        min_vol, max_vol : float, optional
            Minimum and maximum implied volatility
        max_ttm : float, optional
            Maximum time to maturity (in years)
        min_moneyness, max_moneyness : float, optional
            Moneyness range (strike/spot ratio)
            
        Returns:
        --------
        pd.DataFrame
            Filtered options data
        """
        if self.options_data is None:
            raise ValueError("Data not loaded. Call load_data() first.")
        
        filtered = self.options_data.copy()
        
        # Apply filters
        if min_vol is not None:
            filtered = filtered[filtered['IMP_VOL'] >= min_vol]
        if max_vol is not None:
            filtered = filtered[filtered['IMP_VOL'] <= max_vol]
        if max_ttm is not None:
            filtered = filtered[filtered['TTM'] <= max_ttm]
        
        if min_moneyness is not None or max_moneyness is not None:
            moneyness = filtered['STRIKE'] / self.S0
            if min_moneyness is not None:
                filtered = filtered[moneyness >= min_moneyness]
            if max_moneyness is not None:
                filtered = filtered[moneyness <= max_moneyness]
        
        return filtered