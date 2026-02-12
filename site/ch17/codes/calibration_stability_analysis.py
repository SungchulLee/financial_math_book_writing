# calibration_stability_analysis.py
"""
Calibration Stability Analysis.

This module analyzes the stability and robustness of model calibration
across different optimization runs, market conditions, and data perturb-
ations. Essential for understanding model risk in parameter uncertainty.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple
from scipy.optimize import differential_evolution, minimize
import matplotlib.pyplot as plt


class StabilityAnalyzer:
    """Analyze calibration stability across multiple runs."""
    
    def __init__(self, calibrator_func, objective_func):
        """
        Initialize analyzer.
        
        Args:
            calibrator_func: Function that performs calibration
            objective_func: Objective function being minimized
        """
        self.calibrator_func = calibrator_func
        self.objective_func = objective_func
        self.results = []
    
    def multiple_runs(
        self,
        num_runs: int = 10,
        market_data: Dict = None,
        different_seeds: bool = True,
        **kwargs
    ) -> List[Dict]:
        """
        Run calibration multiple times with different seeds.
        
        Args:
            num_runs: Number of calibration runs
            market_data: Market data for calibration
            different_seeds: Use different random seeds
            **kwargs: Additional arguments to calibrator
        
        Returns:
            List of calibration results
        """
        results = []
        
        for i in range(num_runs):
            seed = i if different_seeds else 42
            
            result = self.calibrator_func(
                market_data=market_data,
                seed=seed,
                **kwargs
            )
            result['run_number'] = i
            results.append(result)
        
        self.results = results
        return results
    
    def analyze_parameter_stability(
        self,
        results: List[Dict],
        param_names: List[str]
    ) -> Dict:
        """
        Analyze stability of calibrated parameters.
        
        Args:
            results: List of calibration results
            param_names: Names of parameters to analyze
        
        Returns:
            Dictionary with stability metrics
        """
        param_values = {p: [] for p in param_names}
        
        for result in results:
            for param in param_names:
                if param in result:
                    param_values[param].append(result[param])
        
        stability_stats = {}
        
        for param in param_names:
            values = np.array(param_values[param])
            
            stability_stats[param] = {
                'mean': np.mean(values),
                'std': np.std(values),
                'cv': np.std(values) / np.mean(values) if np.mean(values) != 0 else np.inf,
                'min': np.min(values),
                'max': np.max(values),
                'range': np.max(values) - np.min(values),
                'median': np.median(values),
                'iqr': np.percentile(values, 75) - np.percentile(values, 25)
            }
        
        return stability_stats
    
    def perturb_market_data(
        self,
        market_data: Dict,
        perturbation_level: float = 0.01,
        num_perturbations: int = 10,
        param_bounds: List = None
    ) -> Tuple[List[Dict], List[Dict]]:
        """
        Calibrate to perturbed versions of market data.
        
        Args:
            market_data: Original market data
            perturbation_level: Relative perturbation (e.g., 0.01 = 1%)
            num_perturbations: Number of perturbed datasets
            param_bounds: Parameter bounds for calibration
        
        Returns:
            Tuple of (perturbed_market_data_list, calibration_results_list)
        """
        original_prices = market_data['prices']
        perturbed_datasets = []
        calibration_results = []
        
        for i in range(num_perturbations):
            # Add random noise to prices
            noise = np.random.normal(0, perturbation_level, len(original_prices))
            perturbed_prices = original_prices * (1 + noise)
            
            perturbed_data = market_data.copy()
            perturbed_data['prices'] = perturbed_prices
            perturbed_datasets.append(perturbed_data)
            
            # Calibrate to perturbed data
            result = self.calibrator_func(
                market_data=perturbed_data,
                seed=42
            )
            calibration_results.append(result)
        
        return perturbed_datasets, calibration_results
    
    def sensitivity_to_bounds(
        self,
        market_data: Dict,
        base_bounds: List,
        perturbation_factor: float = 0.5
    ) -> Dict:
        """
        Analyze sensitivity of calibration to parameter bounds.
        
        Args:
            market_data: Market data
            base_bounds: Original parameter bounds
            perturbation_factor: Factor to expand/contract bounds
        
        Returns:
            Dictionary comparing results across different bounds
        """
        results_by_bounds = {}
        
        # Test different bound specifications
        bound_scenarios = {
            'base': base_bounds,
            'tight': [(b[0] * 1.1, b[1] * 0.9) for b in base_bounds],
            'loose': [(b[0] * 0.9, b[1] * 1.1) for b in base_bounds],
        }
        
        for scenario_name, bounds in bound_scenarios.items():
            try:
                result = differential_evolution(
                    lambda p: self.objective_func(p, market_data),
                    bounds,
                    seed=42,
                    maxiter=300
                )
                results_by_bounds[scenario_name] = {
                    'params': result.x,
                    'error': result.fun,
                    'success': result.success
                }
            except Exception as e:
                results_by_bounds[scenario_name] = {'error': str(e)}
        
        return results_by_bounds
    
    def convergence_analysis(
        self,
        market_data: Dict,
        initial_guesses: List,
        param_names: List[str]
    ) -> pd.DataFrame:
        """
        Analyze convergence from different starting points.
        
        Args:
            market_data: Market data
            initial_guesses: List of initial parameter guesses
            param_names: Names of parameters
        
        Returns:
            DataFrame with convergence results
        """
        convergence_data = []
        
        for i, guess in enumerate(initial_guesses):
            result = minimize(
                lambda p: self.objective_func(p, market_data),
                guess,
                method='Nelder-Mead'
            )
            
            row = {
                'initial_guess': i,
                'convergence_success': result.success,
                'final_error': result.fun,
                'num_iterations': result.nit,
                'num_function_calls': result.nfev
            }
            
            for j, param_name in enumerate(param_names):
                row[param_name] = result.x[j]
            
            convergence_data.append(row)
        
        return pd.DataFrame(convergence_data)
    
    def parameter_coupling_analysis(
        self,
        results: List[Dict],
        param_names: List[str]
    ) -> pd.DataFrame:
        """
        Analyze correlations between calibrated parameters.
        
        Args:
            results: Calibration results
            param_names: Parameter names
        
        Returns:
            Correlation matrix DataFrame
        """
        param_matrix = []
        
        for result in results:
            row = [result.get(p, np.nan) for p in param_names]
            param_matrix.append(row)
        
        param_matrix = np.array(param_matrix)
        corr_matrix = np.corrcoef(param_matrix.T)
        
        return pd.DataFrame(
            corr_matrix,
            index=param_names,
            columns=param_names
        )
    
    def plot_stability(
        self,
        results: List[Dict],
        param_names: List[str],
        figsize: Tuple = (12, 8)
    ) -> None:
        """
        Create visualization of parameter stability.
        
        Args:
            results: Calibration results
            param_names: Parameter names to plot
            figsize: Figure size
        """
        fig, axes = plt.subplots(2, 2, figsize=figsize)
        
        param_values = {p: [] for p in param_names}
        for result in results:
            for param in param_names:
                if param in result:
                    param_values[param].append(result[param])
        
        # Box plots
        data_for_box = [np.array(param_values[p]) for p in param_names]
        axes[0, 0].boxplot(data_for_box, labels=param_names)
        axes[0, 0].set_title('Parameter Distribution Across Runs')
        axes[0, 0].set_ylabel('Parameter Value')
        axes[0, 0].grid(True, alpha=0.3)
        
        # Convergence path
        if len(results) > 1:
            errors = [r.get('error', r.get('fun', np.nan)) for r in results]
            axes[0, 1].plot(range(len(errors)), errors, 'b-o')
            axes[0, 1].set_title('Calibration Error Across Runs')
            axes[0, 1].set_xlabel('Run Number')
            axes[0, 1].set_ylabel('Objective Function Value')
            axes[0, 1].grid(True, alpha=0.3)
        
        # Time series of first two parameters
        if len(param_names) >= 2:
            p1_vals = param_values[param_names[0]]
            p2_vals = param_values[param_names[1]]
            axes[1, 0].scatter(p1_vals, p2_vals, alpha=0.6)
            axes[1, 0].set_xlabel(param_names[0])
            axes[1, 0].set_ylabel(param_names[1])
            axes[1, 0].set_title('Parameter Coupling')
            axes[1, 0].grid(True, alpha=0.3)
        
        # Coefficient of variation
        if len(param_names) > 0:
            cvs = []
            for p in param_names:
                vals = np.array(param_values[p])
                cv = np.std(vals) / np.mean(vals) if np.mean(vals) != 0 else 0
                cvs.append(cv)
            
            axes[1, 1].bar(param_names, cvs)
            axes[1, 1].set_title('Coefficient of Variation by Parameter')
            axes[1, 1].set_ylabel('CV')
            axes[1, 1].grid(True, alpha=0.3, axis='y')
        
        plt.tight_layout()
        return fig


def example_stability_analysis():
    """Example stability analysis."""
    print("Calibration Stability Analysis Example")
    print("=" * 60)
    
    # Dummy calibrator for demonstration
    def dummy_calibrator(market_data, seed=42):
        np.random.seed(seed)
        return {
            'param1': 0.1 + np.random.normal(0, 0.02),
            'param2': 2.0 + np.random.normal(0, 0.3),
            'param3': 0.05 + np.random.normal(0, 0.01),
            'error': np.random.uniform(0.001, 0.01)
        }
    
    def dummy_objective(params, market_data):
        return np.sum(params**2)
    
    analyzer = StabilityAnalyzer(dummy_calibrator, dummy_objective)
    
    # Run multiple calibrations
    results = analyzer.multiple_runs(num_runs=20)
    
    # Analyze stability
    stability = analyzer.analyze_parameter_stability(
        results,
        ['param1', 'param2', 'param3']
    )
    
    print("\nParameter Stability Statistics:")
    print("-" * 60)
    for param, stats in stability.items():
        print(f"\n{param}:")
        print(f"  Mean: {stats['mean']:.6f}")
        print(f"  Std Dev: {stats['std']:.6f}")
        print(f"  CV: {stats['cv']:.4f}")
        print(f"  Range: [{stats['min']:.6f}, {stats['max']:.6f}]")


if __name__ == "__main__":
    example_stability_analysis()
