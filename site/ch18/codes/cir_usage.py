# ============================================================================
# cir_USAGE.py
# ============================================================================
import brownian_motion as bmw
import cir
import matplotlib.pyplot as plt
import numpy as np
import traceback

def example_1_basic_usage():
    """Example 1: Basic CIR model usage and simulation."""
    print("=" * 60)
    print("EXAMPLE 1: BASIC CIR MODEL USAGE")
    print("=" * 60)
    
    # Create CIR model
    model = cir.create_cir_model(
        r0=0.03,           # Initial rate 3%
        theta=0.05,        # Long-term mean 5%
        kappa=0.1,         # Mean reversion speed
        sigma=0.03,        # Volatility 3%
        maturity_time=10.0, # 10 years
        seed=42
    )
    
    print(f"Model Parameters:")
    for key, value in model.parameters.to_dict().items():
        print(f"  {key}: {value:.4f}")
    
    print(f"\nFeller Condition: {model.parameters.satisfies_feller_condition}")
    print(f"Feller Parameter: {model.parameters.feller_parameter:.3f}")
    
    # Configure and run simulation
    config = cir.SimulationConfig(
        num_paths=5000,
        scheme=cir.CIRScheme.EULER_MARUYAMA,
        increment_type=bmw.IncrementType.NORMAL,
        absorption_fix=True
    )
    
    print(f"\nRunning simulation with {config.num_paths} paths...")
    result = model.simulate_cir(config)
    
    # Display results
    stats = result.get_statistics()
    print(f"\nResults:")
    print(f"  Final rate mean: {stats['final_rates']['mean']:.4f}")
    print(f"  Final rate std:  {stats['final_rates']['std']:.4f}")
    print(f"  Minimum rate:    {stats['path_statistics']['global_min']:.6f}")
    print(f"  Negative rates:  {stats['path_statistics']['has_negative']}")
    
    return model, result

def example_2_scheme_comparison():
    """Example 2: Compare discretization schemes."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: SCHEME COMPARISON")
    print("=" * 60)
    
    schemes = [cir.CIRScheme.EULER_MARUYAMA, cir.CIRScheme.MILSTEIN, cir.CIRScheme.TRUNCATED_EULER]
    
    print(f"{'Scheme':<20} {'Final Mean':<12} {'Final Std':<12} {'Min Rate':<12}")
    print("-" * 60)
    
    for scheme in schemes:
        model = cir.create_cir_model(r0=0.03, theta=0.05, kappa=0.1, sigma=0.03, seed=123)
        config = cir.SimulationConfig(num_paths=1000, scheme=scheme)
        result = model.simulate_cir(config)
        
        final_mean = np.mean(result.final_rates)
        final_std = np.std(result.final_rates)
        min_rate = np.min(result.short_rate_paths)
        
        print(f"{scheme.value:<20} {final_mean:<12.4f} {final_std:<12.4f} {min_rate:<12.6f}")
        
        # Validation
        validator = cir.CIRValidator()
        validation = validator.full_validation(result)
        overall_pass = all(v.passed for v in validation.values())
        print(f"{'':>20} Validation: {'✓ PASS' if overall_pass else '✗ FAIL'}")

def example_3_parameter_sensitivity():
    """Example 3: Parameter sensitivity analysis."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: PARAMETER SENSITIVITY")
    print("=" * 60)
    
    base_params = {'r0': 0.03, 'theta': 0.05, 'kappa': 0.1, 'sigma': 0.03, 'maturity_time': 10.0, 'seed': 456}
    sensitivity_tests = {
        'sigma': [0.02, 0.025, 0.03, 0.035, 0.04],
        'kappa': [0.05, 0.075, 0.1, 0.15, 0.2],
        'theta': [0.03, 0.04, 0.05, 0.06, 0.07]
    }
    
    for param_name, param_values in sensitivity_tests.items():
        print(f"\n{param_name.upper()} Sensitivity:")
        print(f"{'Value':<8} {'Feller':<8} {'Mean':<8} {'Std':<8} {'Neg%':<6}")
        print("-" * 42)
        
        for param_value in param_values:
            test_params = base_params.copy()
            test_params[param_name] = param_value
            
            result = cir.quick_simulation(num_paths=2000, **test_params)
            
            final_mean = np.mean(result.final_rates)
            final_std = np.std(result.final_rates)
            neg_pct = np.mean(result.short_rate_paths < 0) * 100
            feller = result.parameters.feller_parameter
            
            print(f"{param_value:<8.3f} {feller:<8.3f} {final_mean:<8.4f} "
                  f"{final_std:<8.4f} {neg_pct:<6.2f}")

def example_4_bond_pricing():
    """Example 4: Bond pricing and yield curves."""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: BOND PRICING")
    print("=" * 60)
    
    model = cir.create_cir_model(r0=0.03, theta=0.05, kappa=0.1, sigma=0.03)
    current_rate = 0.03
    maturities = np.array([0.25, 0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30])
    
    print(f"{'Maturity':<10} {'Bond Price':<12} {'Yield':<8} {'Forward':<8}")
    print("-" * 42)
    
    for maturity in maturities:
        bond_price = cir.CIRBondPricer.zero_coupon_bond_price(
            model.parameters, current_rate, maturity
        )
        yield_rate = cir.CIRBondPricer.yield_to_maturity(
            model.parameters, current_rate, maturity
        )
        
        # Calculate forward rate if available
        if maturity > 1:
            try:
                forward_rate = cir.CIRBondPricer.forward_rate(
                    model.parameters, current_rate, maturity-1, maturity
                )
                forward_str = f"{forward_rate:.4f}"
            except:
                forward_str = "N/A"
        else:
            forward_str = "N/A"
        
        print(f"{maturity:<10.2f} {bond_price:<12.6f} {yield_rate:<8.4f} {forward_str:<8}")
    
    # Yield curve scenarios
    print(f"\nYield Curve Scenarios:")
    rate_scenarios = [0.01, 0.03, 0.05, 0.07]
    selected_maturities = [1, 5, 10, 30]
    
    print(f"{'Maturity':<10}", end="")
    for rate in rate_scenarios:
        print(f"r={rate:.3f}    ", end="")
    print()
    print("-" * (10 + 10 * len(rate_scenarios)))
    
    for maturity in selected_maturities:
        print(f"{maturity:<10.1f}", end="")
        for rate in rate_scenarios:
            yield_val = cir.CIRBondPricer.yield_to_maturity(model.parameters, rate, maturity)
            print(f"{yield_val:<10.4f}", end="")
        print()

def example_5_comprehensive_analysis():
    """Example 5: Comprehensive analysis."""
    print("\n" + "=" * 60)
    print("EXAMPLE 5: COMPREHENSIVE ANALYSIS")
    print("=" * 60)
    
    # Try advanced analyzer, fall back to basic
    try:
        analyzer_class = cir.CIRAnalyzer
        use_analyzer = True
    except AttributeError:
        use_analyzer = False
    
    model = cir.create_cir_model(
        r0=0.025, theta=0.045, kappa=0.12, sigma=0.028,
        maturity_time=15.0, seed=789
    )
    
    config = cir.SimulationConfig(
        num_paths=5000,
        scheme=cir.CIRScheme.MILSTEIN,
        increment_type=bmw.IncrementType.NORMAL
    )

    result = model.simulate_cir(config)
    
    if use_analyzer:
        analyzer = analyzer_class(model)

        try:
            analysis = analyzer.comprehensive_analysis(result)
        except Exception as e:
            traceback.print_exc()
            return None
        
        try:
            print(f"Model Parameters:")
            for key, value in model.parameters.to_dict().items():
                print(f"  {key}: {value:.4f}")
        except Exception as e:
            print(f"{e}")
        
        if 'validation_results' in analysis:
            try:
                print(f"\nValidation Results:")
                for test_name, validation in analysis['validation_results'].items():
                    status = "✓ PASS" if validation.passed else "✗ FAIL"
                    print(f"  {test_name}: {status} (error: {validation.error_percentage:.2f}%)")
            except Exception as e:
                print(f"{e}")
        else:
            print("validation_results not found in analysis")
        
        if 'model_metrics' in analysis:
            try:
                print(f"\nAnalysis Summary:")
                for key, value in analysis['model_metrics'].items():
                    print(f"  {key}: {value:.4f}")
            except Exception as e:
                print(f"{e}")
        else:
            print("model_metrics not found in analysis")
        
        return analysis
    else:
        validator = cir.CIRValidator()

        try:
            validation_results = validator.full_validation(result)
        except Exception as e:
            print(f"{e}")
            traceback.print_exc()
            return None
        
        try:
            print(f"Model Parameters:")
            for key, value in model.parameters.to_dict().items():
                print(f"  {key}: {value:.4f}")
        except Exception as e:
            print(f"{e}")
        
        try:
            print(f"\nValidation Results:")
            for test_name, validation in validation_results.items():
                status = "✓ PASS" if validation.passed else "✗ FAIL"
                print(f"  {test_name}: {status} (error: {validation.error_percentage:.2f}%)")
        except Exception as e:
            print(f"{e}")
        
        return result

def example_6_visualization():
    """Example 6: Comprehensive visualization."""
    print("\n" + "=" * 60)
    print("EXAMPLE 6: VISUALIZATION")
    print("=" * 60)
    
    # Create model and simulate
    model = cir.create_cir_model(r0=0.03, theta=0.05, kappa=0.1, sigma=0.03, seed=42)
    config = cir.SimulationConfig(num_paths=1000, scheme=cir.CIRScheme.MILSTEIN)
    result = model.simulate_cir(config)
    
    # Create figure
    fig = plt.figure(figsize=(16, 12))
    gs = fig.add_gridspec(2, 2, height_ratios=[2, 1], hspace=0.35, wspace=0.25)
    
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1])
    ax3 = fig.add_subplot(gs[1, :])
    
    # Path evolution with confidence bands
    empirical_means = np.mean(result.short_rate_paths, axis=0)
    empirical_stds = np.std(result.short_rate_paths, axis=0)
    theoretical_means = np.array([model.analytical_mean(t) for t in result.time_steps])
    theoretical_stds = np.array([model.analytical_std(t) for t in result.time_steps])
    
    # Sample paths
    for i in range(min(50, result.num_paths)):
        ax1.plot(result.time_steps, result.short_rate_paths[i], 
                alpha=0.8, linewidth=0.8, color='lightgray', zorder=1)
    
    # Confidence bands
    emp_upper = empirical_means + empirical_stds
    emp_lower = empirical_means - empirical_stds
    ax1.fill_between(result.time_steps, emp_lower, emp_upper,
                    alpha=0.3, color='blue', label='Empirical ±1σ', zorder=2)
    
    theo_upper = theoretical_means + theoretical_stds
    theo_lower = theoretical_means - theoretical_stds
    ax1.fill_between(result.time_steps, theo_lower, theo_upper,
                    alpha=0.2, color='red', label='Theoretical ±1σ', zorder=2)
    
    # Means
    ax1.plot(result.time_steps, empirical_means, 
            color='blue', linewidth=3, label='Empirical Mean', zorder=4)
    ax1.plot(result.time_steps, theoretical_means, 
            color='red', linewidth=3, linestyle='--', 
            label='Theoretical Mean', zorder=4)
    
    ax1.set_title('CIR Short Rate Paths', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Time (Years)')
    ax1.set_ylabel('Short Rate')
    ax1.legend(loc='upper right', fontsize=10, framealpha=0.9)
    ax1.grid(True, alpha=0.3)
    
    # Final rate distribution
    ax2.hist(result.final_rates, bins=50, density=True, alpha=0.7, 
            color='skyblue', edgecolor='black')
    
    emp_final_mean = np.mean(result.final_rates)
    emp_final_std = np.std(result.final_rates)
    theo_final_mean = model.analytical_mean(result.time_steps[-1])
    theo_final_std = model.analytical_std(result.time_steps[-1])
    
    # Means and standard deviations
    ax2.axvline(emp_final_mean, color='blue', linewidth=3, 
               label=f'Empirical Mean: {emp_final_mean:.4f}')
    ax2.axvline(theo_final_mean, color='red', linewidth=3, linestyle='--',
               label=f'Theoretical Mean: {theo_final_mean:.4f}')
    
    # ±1σ bounds
    ax2.axvline(emp_final_mean - emp_final_std, color='blue', linewidth=1, alpha=0.5, linestyle=':')
    ax2.axvline(emp_final_mean + emp_final_std, color='blue', linewidth=1, alpha=0.5, 
               linestyle=':', label='Empirical ±1σ')
    ax2.axvline(theo_final_mean - theo_final_std, color='red', linewidth=1, alpha=0.5, linestyle=':')
    ax2.axvline(theo_final_mean + theo_final_std, color='red', linewidth=1, alpha=0.5, 
               linestyle=':', label='Theoretical ±1σ')
    
    ax2.set_title('Final Rate Distribution', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Final Rate')
    ax2.set_ylabel('Density')
    ax2.legend(loc='upper right', fontsize=10, framealpha=0.9)
    ax2.grid(True, alpha=0.3)
    
    # Statistics box
    std_ratio = emp_final_std / theo_final_std
    dist_comparison = f'Emp Std: {emp_final_std:.4f}\n'
    dist_comparison += f'Theo Std: {theo_final_std:.4f}\n'
    dist_comparison += f'Ratio: {std_ratio:.3f}\n'
    dist_comparison += f'N: {len(result.final_rates):,}'
    
    ax2.text(0.98, 0.25, dist_comparison, transform=ax2.transAxes, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen", alpha=0.9),
            verticalalignment='top', horizontalalignment='right', fontsize=9)
    
    # Yield curve
    maturities = np.array([0.25, 0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30])
    yields = np.array([cir.CIRBondPricer.yield_to_maturity(model.parameters, model.parameters.r0, T) 
                      for T in maturities])
    
    ax3.plot(maturities, yields, 'bo-', linewidth=3, markersize=8, 
            label='CIR Yield Curve', markerfacecolor='white', markeredgewidth=2)
    
    # Reference lines
    ax3.axhline(y=model.parameters.r0, color='green', linestyle=':', linewidth=2, 
               label=f'Current Rate: {model.parameters.r0:.3f}')
    ax3.axhline(y=model.parameters.theta, color='orange', linestyle=':', linewidth=2,
               label=f'Long-term Mean: {model.parameters.theta:.3f}')
    
    # Key yield annotations
    key_indices = [0, 2, 5, 7, 9, 10]
    for i in key_indices:
        mat, yld = maturities[i], yields[i]
        ax3.annotate(f'{yld:.3f}', xy=(mat, yld), xytext=(0, 12), 
                    textcoords='offset points', ha='center', fontsize=9,
                    bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8))
    
    ax3.set_title('CIR Yield Curve', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Maturity (Years)')
    ax3.set_ylabel('Yield')
    ax3.legend(loc='center left', fontsize=11, framealpha=0.9)
    ax3.grid(True, alpha=0.3)
    
    # Curve analysis
    short_rate = yields[0]
    long_rate = yields[-1]
    slope = (long_rate - short_rate) * 10000
    
    curve_analysis = f'Term Structure:\n'
    curve_analysis += f'Short: {short_rate:.4f}\n'
    curve_analysis += f'Long: {long_rate:.4f}\n'
    curve_analysis += f'Slope: {slope:.0f} bp'
    
    ax3.text(0.02, 0.98, curve_analysis, transform=ax3.transAxes, 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="lightcyan", alpha=0.9),
            verticalalignment='top', fontsize=10)
    
    # Overall formatting
    plt.suptitle(f'CIR Model Analysis (Feller: {model.parameters.feller_parameter:.3f})', 
                 fontsize=18, fontweight='bold')
    
    param_text = f'r₀={model.parameters.r0:.3f}, θ={model.parameters.theta:.3f}, κ={model.parameters.kappa:.3f}, σ={model.parameters.sigma:.3f}'
    plt.figtext(0.5, 0.92, param_text, ha='center', fontsize=12, style='italic')
    
    plt.subplots_adjust(top=0.85)
    plt.show()
    
    print("✓ Visualization completed")

def example_7_performance_analysis():
    """Example 7: Performance analysis."""
    print("\n" + "=" * 60)
    print("EXAMPLE 7: PERFORMANCE ANALYSIS")
    print("=" * 60)
    
    import time
    
    test_configs = [
        {'paths': 1000, 'scheme': cir.CIRScheme.EULER_MARUYAMA},
        {'paths': 1000, 'scheme': cir.CIRScheme.MILSTEIN},
        {'paths': 5000, 'scheme': cir.CIRScheme.EULER_MARUYAMA},
    ]
    
    model = cir.create_cir_model(r0=0.03, theta=0.05, kappa=0.1, sigma=0.03, seed=42)
    
    print(f"{'Paths':<8} {'Scheme':<18} {'Time (s)':<10}")
    print("-" * 40)
    
    for config in test_configs:
        sim_config = cir.SimulationConfig(
            num_paths=config['paths'],
            scheme=config['scheme']
        )
        
        start_time = time.time()
        result = model.simulate_cir(sim_config)
        elapsed_time = time.time() - start_time
        
        print(f"{config['paths']:<8} {config['scheme'].value:<18} {elapsed_time:<10.3f}")

def example_8_feller_exploration():
    """Example 8: Feller condition exploration."""
    print("\n" + "=" * 60)
    print("EXAMPLE 8: FELLER CONDITION EXPLORATION")
    print("=" * 60)
    
    import warnings
    
    test_cases = [
        {"name": "Strong Feller", "theta": 0.08, "kappa": 0.2, "sigma": 0.03},
        {"name": "Weak Feller", "theta": 0.05, "kappa": 0.1, "sigma": 0.032},
        {"name": "Mild Violation", "theta": 0.04, "kappa": 0.1, "sigma": 0.035},
    ]
    
    print(f"{'Case':<15} {'Feller':<8} {'Neg%':<8} {'Mean':<8}")
    print("-" * 42)
    
    for case in test_cases:
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")
            model = cir.create_cir_model(
                r0=0.03, 
                theta=case['theta'], 
                kappa=case['kappa'], 
                sigma=case['sigma'],
                check_feller=False
            )
        
        config = cir.SimulationConfig(num_paths=3000, scheme=cir.CIRScheme.TRUNCATED_EULER)
        result = model.simulate_cir(config)
        
        negative_pct = np.mean(result.short_rate_paths < 0) * 100
        
        print(f"{case['name']:<15} {model.parameters.feller_parameter:<8.3f} "
              f"{negative_pct:<8.2f} {np.mean(result.final_rates):<8.4f}")

def example_9_convergence_analysis():
    """Example 9: Monte Carlo convergence analysis."""
    print("\n" + "=" * 60)
    print("EXAMPLE 9: CONVERGENCE ANALYSIS")
    print("=" * 60)
    
    model = cir.create_cir_model(r0=0.03, theta=0.05, kappa=0.1, sigma=0.03, seed=123)
    path_counts = [100, 500, 1000, 2000, 5000]
    
    theoretical_mean = model.analytical_mean(model.parameters.maturity_time)
    theoretical_var = model.analytical_variance(model.parameters.maturity_time)
    
    print(f"Theoretical mean: {theoretical_mean:.6f}")
    print(f"Theoretical variance: {theoretical_var:.6f}")
    print()
    print(f"{'Paths':<8} {'Mean':<10} {'Mean Err':<10} {'Var':<10} {'Var Err':<10}")
    print("-" * 55)
    
    for num_paths in path_counts:
        config = cir.SimulationConfig(
            num_paths=num_paths, 
            scheme=cir.CIRScheme.EULER_MARUYAMA
        )
        result = model.simulate_cir(config)
        
        empirical_mean = np.mean(result.final_rates)
        empirical_var = np.var(result.final_rates)
        
        mean_error = abs(empirical_mean - theoretical_mean)
        var_error = abs(empirical_var - theoretical_var)
        
        print(f"{num_paths:<8} {empirical_mean:<10.6f} {mean_error:<10.6f} "
              f"{empirical_var:<10.6f} {var_error:<10.6f}")

def example_10_calibration():
    """Example 10: Parameter calibration."""
    print("\n" + "=" * 60)
    print("EXAMPLE 10: PARAMETER CALIBRATION")
    print("=" * 60)
    
    # Generate synthetic data
    true_params = {'r0': 0.035, 'theta': 0.055, 'kappa': 0.08, 'sigma': 0.025, 'maturity_time': 5.0}
    
    true_model = cir.create_cir_model(**true_params, seed=999)
    config = cir.SimulationConfig(
        num_paths=1,
        num_steps=1260,
        scheme=cir.CIRScheme.MILSTEIN
    )
    
    historical_result = true_model.simulate_cir(config)
    historical_rates = historical_result.short_rate_paths[0, :]
    time_step = historical_result.time_step_size
    
    print(f"Historical data: {len(historical_rates)} observations")
    print(f"  Mean: {np.mean(historical_rates):.4f}")
    print(f"  Std: {np.std(historical_rates):.4f}")
    
    # Estimate parameters
    estimated_params = cir.CIRCalibrator.estimate_parameters_from_data(
        historical_rates, time_step
    )
    
    print(f"\nParameter Estimation:")
    print(f"{'Parameter':<10} {'True':<10} {'Estimated':<10} {'Error':<10}")
    print("-" * 45)
    
    for param_name in ['r0', 'theta', 'kappa', 'sigma']:
        true_val = true_params[param_name]
        est_val = estimated_params[param_name]
        error = abs(true_val - est_val) / true_val * 100
        
        print(f"{param_name:<10} {true_val:<10.4f} {est_val:<10.4f} {error:<10.2f}%")
    
    # Validate estimated model
    estimated_model = cir.create_cir_model(**estimated_params, seed=999)
    validation_config = cir.SimulationConfig(num_paths=5000, scheme=cir.CIRScheme.MILSTEIN)
    validation_result = estimated_model.simulate_cir(validation_config)
    
    validator = cir.CIRValidator()
    validation_results = validator.full_validation(validation_result)
    
    overall_pass = all(v.passed for v in validation_results.values())
    print(f"\nValidation: {'✓ PASS' if overall_pass else '✗ FAIL'}")

def run_all_examples():
    """Run all examples."""
    print("CIR PACKAGE USAGE EXAMPLES")
    print("=" * 80)
    
    examples = [
        example_1_basic_usage,
        example_2_scheme_comparison,
        example_3_parameter_sensitivity,
        example_4_bond_pricing,
        example_5_comprehensive_analysis,
        example_6_visualization,
        example_7_performance_analysis,
        example_8_feller_exploration,
        example_9_convergence_analysis,
        example_10_calibration
    ]
    
    for example in examples:
        try:
            example()
        except Exception as e:
            print(f"Error in {example.__name__}: {e}")
    
    print("\n" + "=" * 80)
    print("All examples completed!")

if __name__ == "__main__":
    run_all_examples()