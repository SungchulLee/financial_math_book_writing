# ============================================================================
# vasicek_USAGE.py
# ============================================================================
import brownian_motion as bmw
import cir
import logging
import matplotlib.pyplot as plt
import numpy as np
import sys
import vasicek as vik

def setup_logging():
    """Setup logging for examples."""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def example_1_basic_usage():
    """Example 1: Basic Vasicek model usage and simulation."""
    print("\n" + "=" * 60)
    print("EXAMPLE 1: BASIC VASICEK MODEL USAGE")
    print("=" * 60)
    
    # Create Vasicek model using factory function
    model = vik.create_vasicek_model(
        r0=0.03,           # Initial rate 3%
        b=0.05,            # Long-term mean 5%
        a=0.1,             # Mean reversion speed
        sigma=0.02,        # Constant volatility 2%
        maturity_time=10.0, # 10 years
        seed=42            # For reproducibility
    )
    
    print("Model Parameters:")
    for key, value in model.parameters.to_dict().items():
        print(f"  {key}: {value:.4f}")
    
    # Configure simulation - use EXACT scheme (unique to Vasicek)
    config = vik.SimulationConfig(
        num_paths=5000,
        scheme=vik.VasicekScheme.EXACT,  # Exact simulation!
        increment_type=bmw.IncrementType.NORMAL
    )
    
    print(f"\nSimulation Configuration:")
    print(f"  Number of paths: {config.num_paths}")
    print(f"  Scheme: {config.scheme.value} (no discretization error!)")
    print(f"  Increment type: {config.increment_type.value}")
    
    # Run simulation
    print("Running simulation...")
    result = model.simulate_vasicek(config)
    
    # Display basic results
    stats = result.get_statistics()
    print("\nBasic Statistics:")
    print(f"  Simulation paths: {result.num_paths}")
    print(f"  Time steps: {result.num_time_steps}")
    print(f"  Time step size: {result.time_step_size:.6f}")
    
    print("\nFinal Rate Statistics:")
    for key, value in stats['final_rates'].items():
        print(f"  {key.capitalize()}: {value:.4f}")
    
    print("\nPath Statistics:")
    for key, value in stats['path_statistics'].items():
        if isinstance(value, bool):
            print(f"  {key}: {value}")
        else:
            print(f"  {key}: {value:.4f}")
    
    print("\nVasicek Features:")
    print(f"  ✅ Negative rates allowed: {'Yes' if result.has_negative_rates else 'No'}")
    print(f"  ✅ Negative rate %: {stats['path_statistics']['negative_rate_percentage']:.2f}%")
    print(f"  ✅ Gaussian distribution")
    print(f"  ✅ Exact simulation available")
    
    return model, result

def example_2_scheme_comparison():
    """Example 2: Compare different discretization schemes."""
    print("\n" + "=" * 60)
    print("EXAMPLE 2: DISCRETIZATION SCHEME COMPARISON")
    print("=" * 60)
    
    # Test parameters
    base_params = {
        'r0': 0.03,
        'b': 0.05,
        'a': 0.1,
        'sigma': 0.02,
        'maturity_time': 5.0,
        'seed': 123
    }
    
    schemes_to_test = [
        vik.VasicekScheme.EXACT,
        vik.VasicekScheme.EULER_MARUYAMA,
        vik.VasicekScheme.MILSTEIN  # Same as Euler for Vasicek
    ]
    
    results = {}
    
    print(f"Comparing schemes with 1000 paths over {base_params['maturity_time']} years:")
    print(f"{'Scheme':<20} {'Final Mean':<12} {'Final Std':<12} {'Min Rate':<12} {'Neg %':<8}")
    print("-" * 70)
    
    for scheme in schemes_to_test:
        # Create model
        model = vik.create_vasicek_model(**base_params)
        
        # Configure with different scheme
        config = vik.SimulationConfig(
            num_paths=1000,
            scheme=scheme,
            increment_type=bmw.IncrementType.NORMAL
        )
        
        # Run simulation
        result = model.simulate_vasicek(config)
        
        # Calculate statistics
        final_mean = np.mean(result.final_rates)
        final_std = np.std(result.final_rates)
        min_rate = np.min(result.short_rate_paths)
        neg_pct = np.mean(result.short_rate_paths < 0) * 100
        
        results[scheme] = result
        
        print(f"{scheme.value:<20} {final_mean:<12.4f} {final_std:<12.4f} "
              f"{min_rate:<12.6f} {neg_pct:<8.2f}")
    
    # Validate each scheme
    print("\nValidation Results:")
    validator = vik.VasicekValidator()
    
    for scheme, result in results.items():
        validation = validator.full_validation(result)
        overall_pass = all(v.passed for v in validation.values())
        print(f"  {scheme.value}: {'✅ PASS' if overall_pass else '❌ FAIL'}")
        
        for test_name, val_result in validation.items():
            status = "PASS" if val_result.passed else "FAIL"
            print(f"    {test_name}: {status} (error: {val_result.error_percentage:.2f}%)")
    
    print("\nKey Insights:")
    print("  ✅ EXACT: Perfect convergence (no discretization error)")
    print("  ✅ EULER_MARUYAMA: Small discretization bias") 
    print("  ✅ MILSTEIN: Same as Euler for Vasicek (constant diffusion)")
    
    return results

def example_3_bond_pricing():
    """Example 3: Bond pricing and yield curve analysis."""
    print("\n" + "=" * 60)
    print("EXAMPLE 3: BOND PRICING AND YIELD CURVES")
    print("=" * 60)
    
    # Create Vasicek model
    model = vik.create_vasicek_model(
        r0=0.03, b=0.05, a=0.1, sigma=0.02,
        maturity_time=30.0  # Extended for yield curve
    )
    
    current_rate = 0.03
    maturities = np.array([0.25, 0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30])
    
    print(f"Vasicek Model Bond Pricing (Current rate: {current_rate:.3f}):")
    print(f"{'Maturity':<10} {'Bond Price':<12} {'Yield':<8} {'Forward':<8}")
    print("-" * 42)
    
    for maturity in maturities:
        # Calculate bond price and yield
        bond_price = vik.VasicekBondPricer.zero_coupon_bond_price(
            model.parameters, current_rate, maturity
        )
        yield_rate = vik.VasicekBondPricer.yield_to_maturity(
            model.parameters, current_rate, maturity
        )
        
        # Calculate forward rate (1 year forward)
        if maturity > 1:
            forward_rate = vik.VasicekBondPricer.forward_rate(
                model.parameters, current_rate, maturity-1, maturity
            )
            forward_str = f"{forward_rate:.4f}"
        else:
            forward_str = "N/A"
        
        print(f"{maturity:<10.2f} {bond_price:<12.6f} {yield_rate:<8.4f} {forward_str:<8}")
    
    # Yield curve scenarios (including negative rates)
    print("\nYield Curve Scenarios (Vasicek handles negative rates!):")
    rate_scenarios = [-0.01, 0.01, 0.03, 0.05, 0.07]
    selected_maturities = [1, 5, 10, 30]
    
    print(f"{'Maturity':<10}", end="")
    for rate in rate_scenarios:
        print(f"r={rate:.3f}    ", end="")
    print()
    print("-" * (10 + 10 * len(rate_scenarios)))
    
    for maturity in selected_maturities:
        print(f"{maturity:<10.1f}", end="")
        for rate in rate_scenarios:
            yield_val = vik.VasicekBondPricer.yield_to_maturity(
                model.parameters, rate, maturity
            )
            print(f"{yield_val:<10.4f}", end="")
        print()
    
    return model

def example_4_comprehensive_analysis():
    """Example 4: Comprehensive analysis."""
    print("\n" + "=" * 60)
    print("EXAMPLE 4: COMPREHENSIVE MODEL ANALYSIS")
    print("=" * 60)
    
    # Create model and run simulation
    model = vik.create_vasicek_model(
        r0=0.025, b=0.045, a=0.12, sigma=0.018,
        maturity_time=15.0, seed=789
    )
    
    config = vik.SimulationConfig(
        num_paths=5000,
        scheme=vik.VasicekScheme.EXACT,
        increment_type=bmw.IncrementType.NORMAL
    )
    
    result = model.simulate_vasicek(config)
    
    # Try comprehensive analysis, fall back to basic if needed
    if hasattr(vik, 'VasicekAnalyzer'):
        analyzer = vik.VasicekAnalyzer(model)
        analysis = analyzer.comprehensive_analysis(result)
        
        print("Model Parameters:")
        for key, value in analysis['model_parameters'].items():
            print(f"  {key}: {value:.4f}")
        
        print("\nValidation Results:")
        for test_name, validation in analysis['validation_results'].items():
            status = "✅ PASS" if validation.passed else "❌ FAIL"
            print(f"  {validation.test_name}: {status}")
            print(f"    Empirical: {validation.empirical_value:.6f}")
            print(f"    Theoretical: {validation.theoretical_value:.6f}")
            print(f"    Error: {validation.error_percentage:.2f}%")
        
        print("\nOverall Assessment:")
        assessment = analysis['overall_assessment']
        print(f"  Quality Score: {assessment['quality_score']:.1f}/100")
        print(f"  Validation Passed: {assessment['validation_passed']}")
        print(f"  Negative Rates Present: {assessment['negative_rates_present']}")
        
        return analysis
        
    else:
        print("VasicekAnalyzer not available - running basic analysis")
        
        # Basic validation
        validator = vik.VasicekValidator()
        validation_results = validator.full_validation(result)
        
        print("Model Parameters:")
        for key, value in model.parameters.to_dict().items():
            print(f"  {key}: {value:.4f}")
        
        print("\nValidation Results:")
        for test_name, validation in validation_results.items():
            status = "✅ PASS" if validation.passed else "❌ FAIL"
            print(f"  {test_name}: {status} (error: {validation.error_percentage:.2f}%)")
        
        # Basic statistics
        result_stats = result.get_statistics()
        print("\nSimulation Statistics:")
        print(f"  Final rate mean: {result_stats['final_rates']['mean']:.4f}")
        print(f"  Final rate std: {result_stats['final_rates']['std']:.4f}")
        print(f"  Minimum rate: {result_stats['path_statistics']['global_min']:.6f}")
        print(f"  Negative rates: {result_stats['path_statistics']['has_negative']}")
        print(f"  Negative rate %: {result_stats['path_statistics']['negative_rate_percentage']:.2f}%")
        
        return result
    
    print("\n" + "=" * 60)
    print("EXAMPLE 4: COMPREHENSIVE MODEL ANALYSIS")
    print("=" * 60)
    
    if not HAS_ANALYZER:
        print("VasicekAnalyzer not available - running basic analysis")
        return example_4_basic_analysis()
    
    # Create model and run simulation
    model = create_vasicek_model(
        r0=0.025, b=0.045, a=0.12, sigma=0.018,
        maturity_time=15.0, seed=789
    )
    
    config = SimulationConfig(
        num_paths=8000,
        scheme=VasicekScheme.EXACT,
        increment_type=IncrementType.NORMAL
    )
    
    result = model.simulate_vasicek(config)
    
    # Comprehensive analysis
    analyzer = VasicekAnalyzer(model)
    analysis = analyzer.comprehensive_analysis(result)
    
    print("Model Parameters:")
    for key, value in analysis['model_parameters'].items():
        print(f"  {key}: {value:.4f}")
    
    print("\nValidation Results:")
    for test_name, validation in analysis['validation_results'].items():
        status = "✅ PASS" if validation.passed else "❌ FAIL"
        print(f"  {validation.test_name}: {status}")
        print(f"    Empirical: {validation.empirical_value:.6f}")
        print(f"    Theoretical: {validation.theoretical_value:.6f}")
        print(f"    Error: {validation.error_percentage:.2f}%")
    
    print("\nModel Quality Metrics:")
    for key, value in analysis['model_metrics'].items():
        print(f"  {key}: {value:.4f}")
    
    print("\nOverall Assessment:")
    assessment = analysis['overall_assessment']
    print(f"  Quality Score: {assessment['quality_score']:.1f}/100")
    print(f"  Validation Passed: {assessment['validation_passed']}")
    print(f"  Negative Rates Present: {assessment['negative_rates_present']}")
    
    return analysis

def example_4_basic_analysis():
    """Basic analysis when VasicekAnalyzer is not available."""
    model = vik.create_vasicek_model(
        r0=0.025, b=0.045, a=0.12, sigma=0.018,
        maturity_time=15.0, seed=789
    )
    
    config = vik.SimulationConfig(
        num_paths=5000,
        scheme=vik.VasicekScheme.EXACT,
        increment_type=bmw.IncrementType.NORMAL
    )
    
    result = model.simulate_vasicek(config)
    
    # Basic validation
    validator = vik.VasicekValidator()
    validation_results = validator.full_validation(result)
    
    print("Model Parameters:")
    for key, value in model.parameters.to_dict().items():
        print(f"  {key}: {value:.4f}")
    
    print("\nValidation Results:")
    for test_name, validation in validation_results.items():
        status = "✅ PASS" if validation.passed else "❌ FAIL"
        print(f"  {test_name}: {status} (error: {validation.error_percentage:.2f}%)")
    
    # Basic statistics
    stats = result.get_statistics()
    print("\nSimulation Statistics:")
    print(f"  Final rate mean: {stats['final_rates']['mean']:.4f}")
    print(f"  Final rate std: {stats['final_rates']['std']:.4f}")
    print(f"  Minimum rate: {stats['path_statistics']['global_min']:.6f}")
    print(f"  Negative rates: {stats['path_statistics']['has_negative']}")
    print(f"  Negative rate %: {stats['path_statistics']['negative_rate_percentage']:.2f}%")
    
    return result

def example_5_visualization():
    """Example 5: Visualization (if matplotlib available)."""
    print("\n" + "=" * 60)
    print("EXAMPLE 5: VASICEK VISUALIZATION")
    print("=" * 60)
    
    # Create model and simulate
    model = vik.create_vasicek_model(r0=0.03, b=0.05, a=0.1, sigma=0.02, seed=42)
    config = vik.SimulationConfig(num_paths=1000, scheme=vik.VasicekScheme.EXACT)
    result = model.simulate_vasicek(config)
    
    # Create visualization - now just 3 plots in better layout
    fig = plt.figure(figsize=(16, 10))
    gs = fig.add_gridspec(2, 2, height_ratios=[1, 1], width_ratios=[1, 1], 
                         hspace=0.3, wspace=0.25)
    
    # Top row: Rate paths and distribution
    ax1 = fig.add_subplot(gs[0, 0])
    ax2 = fig.add_subplot(gs[0, 1]) 
    
    # Bottom row: Yield curve spanning full width
    ax3 = fig.add_subplot(gs[1, :])
    
    # 1. Sample paths with confidence bands
    for i in range(min(50, result.num_paths)):
        ax1.plot(result.time_steps, result.short_rate_paths[i], 
                alpha=0.3, color='lightblue', linewidth=0.5)
    
    # Calculate empirical statistics
    mean_path = np.mean(result.short_rate_paths, axis=0)
    std_path = np.std(result.short_rate_paths, axis=0)
    
    # Theoretical statistics
    theoretical_mean = np.array([model.analytical_mean(t) for t in result.time_steps])
    theoretical_std = np.array([model.analytical_std(t) for t in result.time_steps])
    
    # Plot confidence bands
    ax1.fill_between(result.time_steps, 
                     mean_path - std_path, mean_path + std_path,
                     alpha=0.3, color='red', label='Empirical ±1σ')
    ax1.fill_between(result.time_steps, 
                     theoretical_mean - theoretical_std, theoretical_mean + theoretical_std,
                     alpha=0.2, color='gray', label='Theoretical ±1σ')
    
    # Plot means
    ax1.plot(result.time_steps, mean_path, 'r-', linewidth=2, label='Empirical Mean')
    ax1.plot(result.time_steps, theoretical_mean, 'k--', linewidth=2, label='Theoretical Mean')
    
    ax1.set_title('Vasicek Short Rate Paths', fontsize=14, fontweight='bold')
    ax1.set_xlabel('Time (Years)')
    ax1.set_ylabel('Interest Rate')
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='black', linestyle=':', alpha=0.5)
    
    # 2. Final rate distribution with confidence intervals
    ax2.hist(result.final_rates, bins=50, density=True, alpha=0.7, color='lightblue', edgecolor='navy')
    
    # Calculate final statistics
    emp_final_mean = np.mean(result.final_rates)
    emp_final_std = np.std(result.final_rates)
    theo_final_mean = model.analytical_mean(result.time_steps[-1])
    theo_final_std = model.analytical_std(result.time_steps[-1])
    
    # Plot means
    ax2.axvline(emp_final_mean, color='red', linestyle='-', linewidth=3,
               label=f'Empirical: {emp_final_mean:.4f}')
    ax2.axvline(theo_final_mean, color='black', linestyle='--', linewidth=3,
               label=f'Theoretical: {theo_final_mean:.4f}')
    
    # Plot ±1σ bounds
    ax2.axvline(emp_final_mean - emp_final_std, color='red', linestyle=':', alpha=0.7, linewidth=2)
    ax2.axvline(emp_final_mean + emp_final_std, color='red', linestyle=':', alpha=0.7, linewidth=2,
               label='Empirical ±1σ')
    ax2.axvline(theo_final_mean - theo_final_std, color='black', linestyle=':', alpha=0.7, linewidth=2)
    ax2.axvline(theo_final_mean + theo_final_std, color='black', linestyle=':', alpha=0.7, linewidth=2,
               label='Theoretical ±1σ')
    
    ax2.set_title('Final Rate Distribution (Gaussian)', fontsize=14, fontweight='bold')
    ax2.set_xlabel('Final Rate')
    ax2.set_ylabel('Density')
    ax2.legend(loc='upper left')
    ax2.grid(True, alpha=0.3)
    
    # 3. Yield curve - full width at bottom
    maturities = np.array([0.25, 0.5, 1, 2, 3, 5, 7, 10, 15, 20, 30])
    current_rate = 0.03  # Use current rate consistently
    yields = np.array([vik.VasicekBondPricer.yield_to_maturity(model.parameters, current_rate, T) 
                      for T in maturities])
    
    ax3.plot(maturities, yields, 'b-', linewidth=3, marker='o', markersize=6, 
             markerfacecolor='white', markeredgewidth=2, label='Vasicek Yield Curve')
    ax3.axhline(y=current_rate, color='green', linestyle=':', linewidth=2,
               label=f'Current Rate (r₀): {current_rate:.3f}')
    ax3.axhline(y=model.parameters.b, color='orange', linestyle=':', linewidth=2,
               label=f'Long-term Mean (b): {model.parameters.b:.3f}')
    ax3.axhline(y=0, color='black', linestyle=':', alpha=0.5, linewidth=1)
    
    # Add yield annotations for key maturities
    key_maturities = [1, 5, 10, 30]
    for mat in key_maturities:
        idx = np.where(maturities == mat)[0]
        if len(idx) > 0:
            yield_val = yields[idx[0]]
            ax3.annotate(f'{yield_val:.3f}', 
                        xy=(mat, yield_val), xytext=(0, 15),
                        textcoords='offset points', ha='center', fontsize=10,
                        bbox=dict(boxstyle="round,pad=0.2", facecolor="white", alpha=0.8))
    
    ax3.set_title('Vasicek Yield Curve', fontsize=14, fontweight='bold')
    ax3.set_xlabel('Maturity (Years)')
    ax3.set_ylabel('Yield')
    ax3.legend(loc='lower right')
    ax3.grid(True, alpha=0.3)
    ax3.set_xlim(0, 32)
    
    # Add model info
    param_text = f'Parameters: r₀={model.parameters.r0:.3f}, b={model.parameters.a:.3f}, a={model.parameters.b:.1f}, σ={model.parameters.sigma:.3f}'
    convergence_error = abs(emp_final_mean - theo_final_mean)/abs(theo_final_mean)*100
    quality_text = f'Paths: {result.num_paths:,} | Convergence Error: {convergence_error:.2f}% | Scheme: {config.scheme.value}'
    
    plt.figtext(0.5, 0.93, param_text, ha='center', fontsize=12)
    plt.figtext(0.5, 0.90, quality_text, ha='center', fontsize=12)
    
    plt.suptitle('Vasicek Model Analysis', fontsize=18, fontweight='bold', y=0.98)
    plt.tight_layout()
    plt.subplots_adjust(top=0.85, bottom=0.08)
    plt.show()
    
    print("✅ Visualization created successfully!")
    print(f"Final rate statistics:")
    print(f"  Empirical mean: {emp_final_mean:.4f} (±{emp_final_std:.4f})")
    print(f"  Theoretical mean: {theo_final_mean:.4f} (±{theo_final_std:.4f})")
    print(f"  Convergence error: {convergence_error:.2f}%")
    
    # Show some negative rate statistics
    negative_pct = np.mean(result.short_rate_paths < 0) * 100
    print(f"  Negative rates: {negative_pct:.2f}% of all simulated rates")
    
    return fig


def example_6_parameter_sensitivity():
    """Example 3: Parameter sensitivity analysis."""
    print("\n" + "=" * 80)
    print("EXAMPLE 6: PARAMETER SENSITIVITY ANALYSIS")
    print("=" * 80)
    
    base_params = {
        'r0': 0.03,
        'b': 0.05,
        'a': 0.1,
        'sigma': 0.02,
        'maturity_time': 10.0,
        'seed': 456
    }
    
    # Test different parameter values
    sensitivity_tests = {
        'sigma': [0.01, 0.015, 0.02, 0.025, 0.03],
        'a': [0.05, 0.075, 0.1, 0.15, 0.2],
        'b': [0.03, 0.04, 0.05, 0.06, 0.07]
    }
    
    for param_name, param_values in sensitivity_tests.items():
        print(f"\n{param_name.upper()} Sensitivity Analysis:")
        print(f"{'Value':<8} {'Mean':<8} {'Std':<8} {'Min':<8} {'Max':<8} {'Neg%':<6}")
        print("-" * 50)
        
        for param_value in param_values:
            # Create modified parameters
            test_params = base_params.copy()
            test_params[param_name] = param_value
            
            try:
                # Quick simulation
                result = vik.quick_simulation(num_paths=2000, **test_params)
                
                # Calculate metrics
                final_mean = np.mean(result.final_rates)
                final_std = np.std(result.final_rates)
                min_rate = np.min(result.short_rate_paths)
                max_rate = np.max(result.short_rate_paths)
                neg_pct = np.mean(result.short_rate_paths < 0) * 100
                
                print(f"{param_value:<8.3f} {final_mean:<8.4f} {final_std:<8.4f} "
                      f"{min_rate:<8.4f} {max_rate:<8.4f} {neg_pct:<6.2f}")
                
            except Exception as e:
                print(f"{param_value:<8.3f} ERROR: {str(e)[:30]}")

    return result
  

def example_7_vasicek_vs_cir_comparison():
    """Example 7: Direct comparison between Vasicek and CIR models."""
    print("\n" + "=" * 80)
    print("EXAMPLE 7: VASICEK VS CIR COMPARISON")
    print("=" * 80)
    
    # Common parameters (adjusted for each model)
    common_params = {
        'maturity_time': 10.0,
        'seed': 42
    }
    
    # Vasicek model
    vasicek_model = vik.create_vasicek_model(
        r0=0.03, b=0.05, a=0.1, sigma=0.02, **common_params
    )
    
    vasicek_config = vik.SimulationConfig(
        num_paths=5000,
        scheme=vik.VasicekScheme.EXACT,
        increment_type=bmw.IncrementType.NORMAL
    )
    
    vasicek_result = vasicek_model.simulate_vasicek(vasicek_config)
    
    print(f"Model Comparison Results:")
    print(f"{'Feature':<25} {'Vasicek':<15} {'CIR':<15}")
    print("-" * 60)
    
    # Vasicek stats
    v_stats = vasicek_result.get_statistics()
    v_final_mean = v_stats['final_rates']['mean']
    v_final_std = v_stats['final_rates']['std']
    v_min_rate = v_stats['path_statistics']['global_min']
    v_neg_pct = v_stats['path_statistics']['negative_rate_percentage']
    
    cir_model = cir.create_cir_model(r0=0.03, theta=0.05, kappa=0.1, sigma=0.02, **common_params)
    cir_config = cir.SimulationConfig(
        num_paths=5000,
        scheme=cir.CIRScheme.MILSTEIN,
        increment_type=bmw.IncrementType.NORMAL
    )
        
    cir_result = cir_model.simulate_cir(cir_config)
    c_stats = cir_result.get_statistics()
    c_final_mean = c_stats['final_rates']['mean']
    c_final_std = c_stats['final_rates']['std']
    c_min_rate = c_stats['path_statistics']['global_min']
    c_neg_pct = c_stats['path_statistics']['negative_rate_percentage']
        
    # Comparison table
    print(f"{'SDE Form':<25} {'a(b-r)dt+σdW':<15} {'κ(θ-r)dt+σ√r dW':<15}")
    print(f"{'Final Mean':<25} {v_final_mean:<15.4f} {c_final_mean:<15.4f}")
    print(f"{'Final Std':<25} {v_final_std:<15.4f} {c_final_std:<15.4f}")
    print(f"{'Min Rate':<25} {v_min_rate:<15.6f} {c_min_rate:<15.6f}")
    print(f"{'Negative Rates %':<25} {v_neg_pct:<15.2f} {c_neg_pct:<15.2f}")
    print(f"{'Distribution':<25} {'Gaussian':<15} {'Non-central χ²':<15}")
    print(f"{'Exact Simulation':<25} {'Available':<15} {'Not Available':<15}")
    print(f"{'Can Go Negative':<25} {'Yes':<15} {'No':<15}")
    print(f"{'Volatility':<25} {'Constant':<15} {'√r dependent':<15}")
    
    print(f"\nKey Differences:")
    print(f"📊 Distribution: Vasicek → Gaussian, CIR → Chi-squared based")
    print(f"📈 Volatility: Vasicek → Constant, CIR → Proportional to √rate")
    print(f"📉 Negative Rates: Vasicek → Allowed, CIR → Prevented")
    print(f"🎯 Simulation: Vasicek → Exact available, CIR → Discretization needed")
    print(f"📏 Use Case: Vasicek → Low rate environments, CIR → Positive rate environments")
    
    return vasicek_result

def example_8_exact_vs_euler_comparison():
    """Example 8: Compare exact vs Euler simulation in Vasicek."""
    print("\n" + "=" * 80)
    print("EXAMPLE 8: EXACT VS EULER SIMULATION COMPARISON")
    print("=" * 80)
    
    # Create model
    model = vik.create_vasicek_model(r0=0.03, b=0.05, a=0.1, sigma=0.02, seed=123)
    
    # Test different time steps for Euler
    time_steps_to_test = [10, 50, 250, 1000]  # steps per year
    
    print(f"Comparing Exact vs Euler schemes:")
    print(f"{'Steps/Year':<12} {'Scheme':<15} {'Final Mean':<12} {'Final Std':<12} {'Mean Error':<12} {'Std Error':<12}")
    print("-" * 85)
    
    # Exact simulation (reference)
    exact_config = vik.SimulationConfig(
        num_paths=5000,
        scheme=vik.VasicekScheme.EXACT,
        increment_type=bmw.IncrementType.NORMAL
    )
    exact_result = model.simulate_vasicek(exact_config)
    exact_mean = np.mean(exact_result.final_rates)
    exact_std = np.std(exact_result.final_rates)
    
    print(f"{'N/A':<12} {'EXACT':<15} {exact_mean:<12.6f} {exact_std:<12.6f} {'0.000000':<12} {'0.000000':<12}")
    
    # Theoretical values
    theo_mean = model.analytical_mean(model.parameters.maturity_time)
    theo_std = model.analytical_std(model.parameters.maturity_time)
    
    print(f"{'N/A':<12} {'THEORETICAL':<15} {theo_mean:<12.6f} {theo_std:<12.6f} {'N/A':<12} {'N/A':<12}")
    print("-" * 85)
    
    # Euler simulations with different time steps
    for steps_per_year in time_steps_to_test:
        total_steps = int(steps_per_year * model.parameters.maturity_time)
        
        euler_config = vik.SimulationConfig(
            num_paths=5000,
            num_steps=total_steps,
            scheme=vik.VasicekScheme.EULER_MARUYAMA,
            increment_type=bmw.IncrementType.NORMAL
        )
        
        euler_result = model.simulate_vasicek(euler_config)
        euler_mean = np.mean(euler_result.final_rates)
        euler_std = np.std(euler_result.final_rates)
        
        # Errors relative to exact
        mean_error = abs(euler_mean - exact_mean)
        std_error = abs(euler_std - exact_std)
        
        print(f"{steps_per_year:<12} {'EULER':<15} {euler_mean:<12.6f} {euler_std:<12.6f} {mean_error:<12.6f} {std_error:<12.6f}")
    
    print(f"\nKey Insights:")
    print(f"✓ EXACT scheme has zero discretization error")
    print(f"✓ EULER error decreases as time steps increase")
    print(f"✓ For Vasicek, exact simulation is computationally efficient")
    print(f"✓ Use exact scheme unless studying discretization effects")
    
    # Validation comparison
    print(f"\nValidation Comparison:")
    validator = vik.VasicekValidator()
    
    exact_validation = validator.full_validation(exact_result)
    print(f"EXACT scheme validation:")
    for test_name, validation in exact_validation.items():
        status = "✓ PASS" if validation.passed else "✗ FAIL"
        print(f"  {test_name}: {status} (error: {validation.error_percentage:.3f}%)")
    
    # Test worst Euler case
    worst_euler_config = vik.SimulationConfig(
        num_paths=5000,
        num_steps=int(10 * model.parameters.maturity_time),  # Only 10 steps/year
        scheme=vik.VasicekScheme.EULER_MARUYAMA,
        increment_type=vik.IncrementType.NORMAL
    )
    worst_euler_result = model.simulate_vasicek(worst_euler_config)
    worst_euler_validation = validator.full_validation(worst_euler_result)
    
    print(f"\nEULER (10 steps/year) validation:")
    for test_name, validation in worst_euler_validation.items():
        status = "✓ PASS" if validation.passed else "✗ FAIL"
        print(f"  {test_name}: {status} (error: {validation.error_percentage:.3f}%)")

    return 1

def run_all_examples():
    """Run all available examples."""
    print("VASICEK PACKAGE DEMONSTRATION")
    print("=" * 60)
    
    setup_logging()
    
    examples = [
        ("Basic Usage", example_1_basic_usage),
        ("Scheme Comparison", example_2_scheme_comparison),
        ("Bond Pricing", example_3_bond_pricing),
        ("Comprehensive Analysis", example_4_comprehensive_analysis),
        ("Visualization", example_5_visualization),
        ("Parameter Sensitivity", example_6_parameter_sensitivity),
        ("Vasicek vs CIR", example_7_vasicek_vs_cir_comparison),
        ("Exact vs Euler", example_8_exact_vs_euler_comparison),
    ]
    
    results = []
    
    for name, example_func in examples:
        print(f"\n{'='*10} {name} {'='*10}")
        try:
            result = example_func()
            results.append((name, result))
            print(f"✅ {name} completed successfully")
        except Exception as e:
            print(f"❌ {name} failed: {e}")
            import traceback
            traceback.print_exc()
    
    # Summary
    print("\n" + "=" * 60)
    print("EXECUTION SUMMARY")
    print("=" * 60)
    
    successful = sum(1 for name, result in results if result is not None)
    total = len(examples)
    
    print(f"Successfully completed: {successful}/{total} examples")
    
    if successful == total:
        print("🎉 All examples completed successfully!")
    elif successful >= total * 0.7:
        print("👍 Most examples completed successfully.")
    else:
        print("⚠️  Several examples failed. Check error messages above.")
    
    return results

def main():
    """Main function with command line options."""
    if len(sys.argv) > 1:
        if sys.argv[1] == '--basic':
            example_1_basic_usage()
        elif sys.argv[1] == '--test':
            example_1_basic_usage()
            example_2_scheme_comparison()
        elif sys.argv[1] == '--bonds':
            example_3_bond_pricing()
        elif sys.argv[1] == '--viz':
            example_5_visualization()
        else:
            print("Usage: python vasicek_main.py [--basic|--test|--bonds|--viz]")
            print("  --basic: Run basic example only")
            print("  --test:  Run basic tests")
            print("  --bonds: Run bond pricing example")
            print("  --viz:   Run visualization example")
            print("  (no args): Run all examples")
    else:
        run_all_examples()

if __name__ == "__main__":
    main()