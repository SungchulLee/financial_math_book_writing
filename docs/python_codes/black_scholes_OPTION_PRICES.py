# ============================================================================
# black_scholes_OPTION_PRICES.py
# ============================================================================
import binomial_model as bm
import black_scholes as bs
import numpy as np


class OptionPricingComparison:
    """
    A class to compare option pricing between Binomial and Black-Scholes models.
    Uses separate models for pricing accuracy vs visualization.
    """
    
    def __init__(self, S, K, T, r, sigma, M_pricing=500, M_visual=6, model='JR'):
        self.S = S
        self.K = K
        self.T = T
        self.r = r
        self.sigma = sigma
        self.M_pricing = M_pricing
        self.M_visual = M_visual
        self.model = model
        
        # High-precision model for pricing
        self.pricing_model = bm.BinomialModel(S, K, T, r, sigma, M_pricing, model=model)
        
        # Small model for visualization
        self.visual_model = bm.BinomialModel(S, K, T, r, sigma, M_visual, model=model)
        
        # Black-Scholes for comparison (using the new wrapper)
        self.bs_model = bs.BlackScholes(S, K, T, r, sigma)
    
    def compare_prices(self, option_type="call", pricing_method="risk_neutral"):
        """Compare high-precision binomial vs Black-Scholes prices."""
        
        # Get high-precision binomial price
        if pricing_method == "risk_neutral":
            binomial_price = self.pricing_model.risk_neutral_valuation(option_type=option_type)
        elif pricing_method == "state_price":
            binomial_price = self.pricing_model.state_price_valuation(option_type=option_type)
        else:
            raise ValueError("pricing_method must be 'risk_neutral' or 'state_price'")
        
        # Get Black-Scholes prices using the wrapper
        bs_call, bs_put = self.bs_model.price_analytical()
        bs_price = bs_call if option_type == "call" else bs_put
        
        # Calculate difference
        difference = abs(binomial_price - bs_price)
        relative_error = (difference / bs_price) * 100
        
        return {
            'binomial_price': binomial_price,
            'black_scholes_price': bs_price,
            'absolute_difference': difference,
            'relative_error_percent': relative_error,
            'option_type': option_type,
            'pricing_method': pricing_method,
            'binomial_steps': self.M_pricing,
            'binomial_model': self.model
        }
    
    def compare_american_vs_european(self, option_type="put"):
        """Compare American vs European option prices using high-precision model."""
        european_price = self.pricing_model.risk_neutral_valuation(
            option_type=option_type, american=False
        )
        american_price = self.pricing_model.risk_neutral_valuation(
            option_type=option_type, american=True
        )
        
        early_exercise_premium = american_price - european_price
        
        return {
            'european_price': european_price,
            'american_price': american_price,
            'early_exercise_premium': early_exercise_premium,
            'option_type': option_type
        }
    
    def compare_barrier_option(self, option_type="call", barrier_level=None):
        """Compare regular vs barrier option prices using high-precision model."""
        if barrier_level is None:
            barrier_level = self.S * 0.8  # 80% of current price
        
        regular_price = self.pricing_model.risk_neutral_valuation(option_type=option_type)
        barrier_price = self.pricing_model.risk_neutral_valuation(
            option_type=option_type, barrier=barrier_level
        )
        
        barrier_discount = regular_price - barrier_price
        discount_percent = (barrier_discount / regular_price) * 100
        
        return {
            'regular_price': regular_price,
            'barrier_price': barrier_price,
            'barrier_level': barrier_level,
            'barrier_discount': barrier_discount,
            'discount_percent': discount_percent,
            'option_type': option_type
        }
    
    def print_comparison(self, option_type="call", pricing_method="risk_neutral"):
        """Print a formatted comparison of option prices."""
        results = self.compare_prices(option_type, pricing_method)
        
        print(f"\n{'='*80}")
        print(f"OPTION PRICING COMPARISON - {option_type.upper()} OPTION")
        print(f"{'='*80}")
        print(f"Stock Price (S₀):          ${self.S}")
        print(f"Strike Price (K):          ${self.K}")
        print(f"Time to Maturity (T):      {self.T} years")
        print(f"Risk-free Rate (r):        {self.r*100:.1f}%")
        print(f"Volatility (σ):            {self.sigma*100:.1f}%")
        print(f"Binomial Steps (Pricing):  {self.M_pricing}")
        print(f"Binomial Steps (Visual):   {self.M_visual}")
        print(f"Binomial Model:            {self.model}")
        print(f"Pricing Method:            {pricing_method}")
        print(f"{'='*80}")
        print(f"Binomial Model Price:      ${results['binomial_price']:.6f}")
        print(f"Black-Scholes Price:       ${results['black_scholes_price']:.6f}")
        print(f"Absolute Difference:       ${results['absolute_difference']:.6f}")
        print(f"Relative Error:            {results['relative_error_percent']:.4f}%")
        print(f"{'='*80}")
    
    def print_american_comparison(self, option_type="put"):
        """Print American vs European option comparison."""
        results = self.compare_american_vs_european(option_type)
        
        print(f"\n{'='*80}")
        print(f"AMERICAN vs EUROPEAN - {option_type.upper()} OPTION")
        print(f"{'='*80}")
        print(f"European Price:            ${results['european_price']:.6f}")
        print(f"American Price:            ${results['american_price']:.6f}")
        print(f"Early Exercise Premium:    ${results['early_exercise_premium']:.6f}")
        print(f"Premium as % of European:  {(results['early_exercise_premium']/results['european_price']*100):.3f}%")
        print(f"{'='*80}")
    
    def print_barrier_comparison(self, option_type="call", barrier_level=None):
        """Print barrier option comparison."""
        results = self.compare_barrier_option(option_type, barrier_level)
        
        print(f"\n{'='*80}")
        print(f"(Knocks Out) BARRIER OPTION - {option_type.upper()} OPTION")
        print(f"{'='*80}")
        print(f"Regular Price:             ${results['regular_price']:.6f}")
        print(f"Barrier Price:             ${results['barrier_price']:.6f}")
        print(f"Barrier Level:             ${results['barrier_level']:.2f}")
        print(f"Barrier Discount:          ${results['barrier_discount']:.6f}")
        print(f"Discount Percentage:       {results['discount_percent']:.3f}%")
        print(f"{'='*80}")
    
    def convergence_analysis(self, option_type="call", step_sizes=None):
        """Analyze convergence of binomial model to Black-Scholes as steps increase."""
        if step_sizes is None:
            step_sizes = [5, 10, 25, 50, 100, 250, 500, 1000]
        
        # Get Black-Scholes reference price
        bs_call, bs_put = self.bs_model.price_analytical()
        bs_price = bs_call if option_type == "call" else bs_put
        
        results = []
        
        for M in step_sizes:
            # Create new binomial model for this step size
            bm_model = bm.BinomialModel(self.S, self.K, self.T, self.r, self.sigma, M, model=self.model)
            binomial_price = bm_model.risk_neutral_valuation(option_type=option_type)
            relative_error = abs(binomial_price - bs_price) / bs_price * 100
            
            results.append({
                'steps': M,
                'binomial_price': binomial_price,
                'black_scholes_price': bs_price,
                'relative_error_percent': relative_error
            })
        
        return results
    
    def print_convergence_analysis(self, option_type="call"):
        """Print convergence analysis results."""
        results = self.convergence_analysis(option_type)
        
        print(f"\n{'='*80}")
        print(f"CONVERGENCE ANALYSIS - {option_type.upper()} OPTION")
        print(f"{'='*80}")
        print(f"{'Steps':<8} {'Binomial Price':<16} {'BS Price':<12} {'Abs Error':<12} {'Rel Error (%)':<15}")
        print(f"{'-'*80}")
        
        bs_price = results[0]['black_scholes_price']
        for result in results:
            abs_error = abs(result['binomial_price'] - bs_price)
            print(f"{result['steps']:<8} "
                  f"${result['binomial_price']:<15.6f} "
                  f"${result['black_scholes_price']:<11.6f} "
                  f"${abs_error:<11.6f} "
                  f"{result['relative_error_percent']:<14.4f}")
        
        print(f"{'='*80}")
    
    def plot_tree_visual(self, title_suffix=""):
        """Plot the small visualization tree."""
        title = f"Binomial Tree Structure ({self.M_visual} steps){title_suffix}"
        print(f"\nPlotting visualization tree ({self.M_visual} steps)...")
        self.visual_model.plot_tree(figsize=(12, 8), title=title)
        print("Tree visualization completed!")
    
    def demonstrate_visual_vs_pricing(self, option_type="call"):
        """Show the difference between visual model and pricing model accuracy."""
        print(f"\n{'='*80}")
        print(f"VISUAL MODEL vs PRICING MODEL - {option_type.upper()} OPTION")
        print(f"{'='*80}")
        
        # Visual model price
        visual_price = self.visual_model.risk_neutral_valuation(option_type=option_type)
        
        # Pricing model price  
        pricing_price = self.pricing_model.risk_neutral_valuation(option_type=option_type)
        
        # Black-Scholes price
        bs_call, bs_put = self.bs_model.price_analytical()
        bs_price = bs_call if option_type == "call" else bs_put
        
        print(f"Visual Model ({self.M_visual} steps):         ${visual_price:.6f}")
        print(f"Pricing Model ({self.M_pricing} steps):      ${pricing_price:.6f}")
        print(f"Black-Scholes (continuous):     ${bs_price:.6f}")
        print(f"")
        print(f"Visual vs BS Error:             ${abs(visual_price - bs_price):.6f} ({abs(visual_price - bs_price)/bs_price*100:.3f}%)")
        print(f"Pricing vs BS Error:            ${abs(pricing_price - bs_price):.6f} ({abs(pricing_price - bs_price)/bs_price*100:.4f}%)")
        print(f"Improvement Factor:             {(abs(visual_price - bs_price)/abs(pricing_price - bs_price)):.1f}x more accurate")
        print(f"{'='*80}")
    
    def compare_black_scholes_methods(self, option_type="call"):
        """Compare different Black-Scholes pricing methods."""
        print(f"\n{'='*80}")
        print(f"BLACK-SCHOLES METHODS COMPARISON - {option_type.upper()} OPTION")
        print(f"{'='*80}")
        
        # Analytical pricing
        call_analytical, put_analytical = self.bs_model.price_analytical()
        analytical_price = call_analytical if option_type == "call" else put_analytical
        
        # Monte Carlo pricing
        mc_results = self.bs_model.price_monte_carlo(num_paths=100000, plot_histogram=False, seed=0)
        mc_call_price, mc_put_price = mc_results[0], mc_results[1]
        mc_price = mc_call_price if option_type == "call" else mc_put_price
        mc_std = mc_results[2] if option_type == "call" else mc_results[3]
        
        # Numerical pricing
        S_grid, option_values = self.bs_model.price_numerical(
            method='cn', option_type=option_type, NS=200, NT=100
        )
        # Find price at current stock price
        idx = np.argmin(np.abs(S_grid - self.S))
        numerical_price = option_values[idx]
        
        print(f"Analytical Price:          ${analytical_price:.6f}")
        print(f"Monte Carlo Price:         ${mc_price:.6f} ± ${mc_std/np.sqrt(100000):.6f}")
        print(f"Numerical (CN) Price:      ${numerical_price:.6f}")
        print(f"")
        print(f"MC vs Analytical Error:    ${abs(mc_price - analytical_price):.6f}")
        print(f"Numerical vs Analytical:   ${abs(numerical_price - analytical_price):.6f}")
        print(f"{'='*80}")
        
        return {
            'analytical': analytical_price,
            'monte_carlo': mc_price,
            'numerical': numerical_price
        }
    
    def demonstrate_greeks(self):
        """Demonstrate Greeks calculation using Black-Scholes wrapper."""
        print(f"\n{'='*80}")
        print("BLACK-SCHOLES GREEKS ANALYSIS")
        print(f"{'='*80}")
        
        greeks = self.bs_model.calculate_greeks()
        
        print(f"Option Greeks:")
        print(f"  Delta (Call/Put):      {greeks['delta_call']:>8.4f} / {greeks['delta_put']:>8.4f}")
        print(f"  Gamma:                 {greeks['gamma']:>8.6f}")
        print(f"  Vega:                  {greeks['vega']:>8.4f}")
        print(f"  Theta (Call/Put):      {greeks['theta_call']:>8.4f} / {greeks['theta_put']:>8.4f}")
        print(f"  Rho (Call/Put):        {greeks['rho_call']:>8.4f} / {greeks['rho_put']:>8.4f}")
        print(f"")
        print("Interpretation:")
        print(f"• Delta: Price sensitivity to stock price changes")
        print(f"• Gamma: Delta sensitivity to stock price changes")
        print(f"• Vega: Price sensitivity to volatility changes")
        print(f"• Theta: Price decay due to time passage")
        print(f"• Rho: Price sensitivity to interest rate changes")
        print(f"{'='*80}")


def main():
    """
    Main function demonstrating practical option pricing with updated Black-Scholes wrapper.
    
    Key Principle: Use high steps for pricing, low steps for visualization.
    """
    
    print(f"")
    print("=" * 80)
    print("🎯 PRACTICAL OPTION PRICING - BINOMIAL vs BLACK-SCHOLES")
    print("=" * 80)
    
    # Market Parameters
    S = 100      # Current stock price
    K = 100      # Strike price (at-the-money)
    T = 1        # Time to maturity (1 year)
    r = 0.05     # Risk-free rate (5%)
    sigma = 0.2  # Volatility (20%)
    
    # Model Parameters
    M_pricing = 500    # High precision for pricing
    M_visual = 6       # Small tree for visualization
    model_type = 'JR'  # Jarrow-Rudd model
    
    print(f"Market Parameters:")
    print(f"  Stock Price (S₀): ${S}")
    print(f"  Strike Price (K): ${K}")
    print(f"  Time to Maturity: {T} year")
    print(f"  Risk-free Rate:   {r*100}%")
    print(f"  Volatility:       {sigma*100}%")
    print(f"")
    print(f"Model Configuration:")
    print(f"  Pricing Steps:    {M_pricing} (for accuracy)")
    print(f"  Visual Steps:     {M_visual} (for clarity)")
    print(f"  Model Type:       {model_type}")
    print("=" * 80)
    
    # Create comparison object
    comparison = OptionPricingComparison(
        S, K, T, r, sigma, 
        M_pricing=M_pricing, 
        M_visual=M_visual, 
        model=model_type
    )
    
    # 1. Basic Price Comparison (Binomial vs Black-Scholes)
    comparison.print_comparison(option_type="call", pricing_method="risk_neutral")
    comparison.print_comparison(option_type="put", pricing_method="risk_neutral")
    
    # 2. Compare Different Binomial Pricing Methods
    print(f"\n{'='*80}")
    print("COMPARING BINOMIAL PRICING METHODS")
    print(f"{'='*80}")
    
    call_rn = comparison.pricing_model.risk_neutral_valuation("call")
    call_sp = comparison.pricing_model.state_price_valuation("call")
    
    print(f"Call Option - Risk Neutral Method:  ${call_rn:.6f}")
    print(f"Call Option - State Price Method:   ${call_sp:.6f}")
    print(f"Difference between methods:         ${abs(call_rn - call_sp):.8f}")
    print("✓ Both methods should give identical results (within numerical precision)")
    print(f"{'='*80}")
    
    # 3. Black-Scholes Methods Comparison
    comparison.compare_black_scholes_methods(option_type="call")
    
    # 4. Greeks Analysis
    comparison.demonstrate_greeks()
    
    # 5. American vs European Options
    comparison.print_american_comparison(option_type="put")
    
    # 6. Barrier Options
    comparison.print_barrier_comparison(option_type="call", barrier_level=90)
    
    # 7. Visual vs Pricing Model Demonstration
    comparison.demonstrate_visual_vs_pricing(option_type="call")
    
    # 8. Convergence Analysis
    comparison.print_convergence_analysis(option_type="call")
    
    # 9. Tree Visualization
    comparison.plot_tree_visual(title_suffix=" - Educational Purpose")
    
    # 10. Model Comparison Across Different Types
    print(f"\n{'='*80}")
    print("COMPARING BINOMIAL MODELS")
    print(f"{'='*80}")
    
    models_to_test = ['JR', 'CRR', 'Wilmott']
    bs_call, _ = comparison.bs_model.price_analytical()
    
    print(f"{'Model':<14} {'Call Price':<12} {'Error vs BS':<12} {'Rel Error %':<12}")
    print("-" * 80)
    
    for model in models_to_test:
        bm_model = bm.BinomialModel(S, K, T, r, sigma, M_pricing, model=model)
        price = bm_model.risk_neutral_valuation("call")
        error = abs(price - bs_call)
        rel_error = error / bs_call * 100
        
        print(f"{model:<14} ${price:<11.6f} ${error:<11.6f} {rel_error:<11.4f}")
    
    print(f"{'Black-Scholes':<14} ${bs_call:<11.6f}")
    print("=" * 80)
    print()
    
    # 11. Direct Usage Examples (Your Original Style)
    print(f"{'='*80}")
    print("DIRECT USAGE EXAMPLES")
    print(f"{'='*80}")
    
    # Example 1: Quick pricing with both models
    print("Example 1: Quick Option Pricing")
    binomial_model = bm.BinomialModel(S, K, T, r, sigma, M_pricing, model='JR')
    bs_model = bs.BlackScholes(S, K, T, r, sigma)
    
    call_price_bin = binomial_model.risk_neutral_valuation(option_type="call")
    put_price_bin = binomial_model.risk_neutral_valuation(option_type="put")
    call_price_bs, put_price_bs = bs_model.price_analytical()
    
    print(f"  Binomial      - Call: ${call_price_bin:.4f}, Put: ${put_price_bin:.4f}")
    print(f"  Black-Scholes - Call: ${call_price_bs:.4f}, Put: ${put_price_bs:.4f}")
    print(f"  Put-Call Parity Check: C - P = S - K*e^(-rT)")
    parity_left = call_price_bs - put_price_bs
    parity_right = S - K * np.exp(-r * T)
    print(f"    Left side:  ${parity_left:.6f}")
    print(f"    Right side: ${parity_right:.6f}")
    print(f"    Difference: ${abs(parity_left - parity_right):.8f}")
    
    # Example 2: Parameter access
    print(f"\nExample 2: Accessing Model Parameters")
    print(f"  Binomial Model:")
    print(f"    Up factor (U):        {binomial_model.U:.6f}")
    print(f"    Down factor (D):      {binomial_model.D:.6f}")
    print(f"    Risk-neutral prob:    {binomial_model.q_u:.6f}")
    print(f"    Time step (dt):       {binomial_model.dt:.6f}")
    print(f"  Black-Scholes Model:")
    print(f"    Spot price:           ${bs_model.spot_price}")
    print(f"    Strike price:         ${bs_model.strike_price}")
    print(f"    Volatility:           {bs_model.volatility}")
    print(f"    Risk-free rate:       {bs_model.risk_free_rate}")
    
    # Example 3: American options
    print(f"\nExample 3: American Options")
    european_put = binomial_model.risk_neutral_valuation("put", american=False)
    american_put = binomial_model.risk_neutral_valuation("put", american=True)
    early_exercise_value = american_put - european_put
    
    print(f"  European Put:         ${european_put:.6f}")
    print(f"  American Put:         ${american_put:.6f}")
    print(f"  Early Exercise Value: ${early_exercise_value:.6f}")
    
    # Example 4: Barrier options
    print(f"\nExample 4: (Knocks Out) Barrier Options with Barrier Level 90")
    regular_call = binomial_model.risk_neutral_valuation("call")
    barrier_call = binomial_model.risk_neutral_valuation("call", barrier=90)
    barrier_discount = regular_call - barrier_call
    
    print(f"  Regular Call:         ${regular_call:.6f}")
    print(f"  Barrier Call:         ${barrier_call:.6f}")
    print(f"  Barrier Discount:     ${barrier_discount:.6f}")
    
    # Example 5: Black-Scholes wrapper demonstration
    print(f"\nExample 5: Black-Scholes Wrapper Usage")
    print(f"  Model Summary:")
    bs_model.summary()
    print(f"{'='*80}")
    print(f"")
    
    print(f"{'='*80}")
    print(f"🎉 Analysis Complete!")
    print("=" * 80)
    print("Key Takeaways:")
    print("• Use high steps (500+) for accurate pricing")
    print("• Use low steps (≤8) for tree visualization")
    print("• Binomial models converge to Black-Scholes")
    print("• American options have early exercise premium")
    print("• Barrier options trade at discount to vanilla options")
    print("• Black-Scholes wrapper provides unified interface")
    print("• Multiple pricing methods give consistent results")
    print(f"{'='*80}")
    print()

if __name__ == "__main__":
    main()    