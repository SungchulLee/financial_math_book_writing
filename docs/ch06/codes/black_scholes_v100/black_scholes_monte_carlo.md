# Black Scholes Monte Carlo

## Background

Black Scholes Monte Carlo

Educational script demonstrating black scholes monte carlo concepts.

---

## Code

```python
"""
Black Scholes Monte Carlo

Educational script demonstrating black scholes monte carlo concepts.
"""

# ============================================================================
# black_scholes/black_scholes_monte_carlo.py
# ============================================================================
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
from .black_scholes_base import BlackScholesBase
from .black_scholes_utils import simulate_gbm_paths


class BlackScholesMonteCarlo(BlackScholesBase):
    def price(self, num_paths=10000, steps_per_year=252, seed=None, plot_histogram=True):
        """
        Price options using Monte Carlo simulation.
        
        Parameters:
        -----------
        num_paths : int
            Number of simulation paths
        steps_per_year : int
            Number of time steps per year
        seed : int, optional
            Random seed for reproducibility
        plot_histogram : bool
            Whether to plot histograms of option prices
            
        Returns:
        --------
        tuple: (call_price, put_price, call_price_std, put_price_std, 
                call_ci, put_ci, call_prices, put_prices)
        """
        self.num_paths = num_paths

        # Fix: Use correct number of steps (not steps_per_year directly)
        num_steps = int(steps_per_year * self.T)
        
        _, paths = simulate_gbm_paths(
            self.S0, self.T, self.r, self.sigma, 
            num_paths, num_steps, 
            risk_neutral=True, seed=seed
        )
        
        S_T = paths[:, -1]
        discount = np.exp(-self.r * self.T)
        
        # Calculate option payoffs
        call_payoffs = np.maximum(S_T - self.K, 0)
        put_payoffs = np.maximum(self.K - S_T, 0)
        
        # Calculate discounted prices
        call_prices = discount * call_payoffs
        put_prices = discount * put_payoffs
        
        # Calculate statistics
        call_price = np.mean(call_prices)
        put_price = np.mean(put_prices)
        call_price_std = np.std(call_prices)
        put_price_std = np.std(put_prices)
        
        # Calculate empirical confidence intervals
        call_ci = self._calculate_empirical_ci(call_prices, confidence_level=0.95)
        put_ci = self._calculate_empirical_ci(put_prices, confidence_level=0.95)
        
        # Plot histograms if requested
        if plot_histogram:
            self._plot_histograms(call_prices, put_prices, call_price, put_price, 
                                call_price_std, put_price_std, call_ci, put_ci)
        
        return call_price, put_price, call_price_std, put_price_std, call_ci, put_ci, call_prices, put_prices
    
    def _calculate_empirical_ci(self, prices, confidence_level=0.95):
        """Calculate empirical confidence interval using percentiles."""
        alpha = 1 - confidence_level
        lower_percentile = (alpha / 2) * 100
        upper_percentile = (1 - alpha / 2) * 100
        
        ci_lower = np.percentile(prices, lower_percentile)
        ci_upper = np.percentile(prices, upper_percentile)
        
        return (ci_lower, ci_upper)
    
    # Redundant with calculate_bootstrap_ci
    # def _calculate_bootstrap_ci(self, prices, confidence_level=0.95, n_bootstrap=1000):
    #     """Calculate bootstrap confidence interval for the mean."""
    #     np.random.seed(42)  # For reproducibility
    #     bootstrap_means = []
        
    #     for _ in range(n_bootstrap):
    #         # Resample with replacement
    #         bootstrap_sample = np.random.choice(prices, size=len(prices), replace=True)
    #         bootstrap_means.append(np.mean(bootstrap_sample))
        
    #     bootstrap_means = np.array(bootstrap_means)
    #     return self._calculate_empirical_ci(bootstrap_means, confidence_level)
    
    def calculate_bootstrap_ci(self, data, confidence_level=0.95, n_bootstrap=1000):
        """
        Public method to calculate bootstrap confidence interval for the mean.
        Can be called externally for E[X] estimation.
        """
        np.random.seed(42)  # For reproducibility
        bootstrap_means = []
        
        for _ in range(n_bootstrap):
            # Resample with replacement
            bootstrap_sample = np.random.choice(data, size=len(data), replace=True)
            bootstrap_means.append(np.mean(bootstrap_sample))
        
        bootstrap_means = np.array(bootstrap_means)
        alpha = 1 - confidence_level
        lower_percentile = (alpha / 2) * 100
        upper_percentile = (1 - alpha / 2) * 100
        
        ci_lower = np.percentile(bootstrap_means, lower_percentile)
        ci_upper = np.percentile(bootstrap_means, upper_percentile)
        
        return (ci_lower, ci_upper)
    
    def _plot_histograms(self, call_prices, put_prices, call_mean, put_mean, 
                        call_std, put_std, call_ci, put_ci):
        """Plot histograms of option prices with normal density overlay and confidence intervals."""
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Call option histogram
        ax1.hist(call_prices, bins=50, density=True, alpha=0.7, color='green', 
                edgecolor='black', label='Monte Carlo')
        
        # Normal distribution overlay for call (for comparison)
        x_call = np.linspace(call_prices.min(), call_prices.max(), 1000)
        normal_call = stats.norm.pdf(x_call, call_mean, call_std)
        ax1.plot(x_call, normal_call, 'r-', linewidth=2, alpha=0.7, label='Normal Density (for comparison)')
        
        # Add confidence interval shading
        ax1.axvspan(call_ci[0], call_ci[1], alpha=0.3, color='orange', label=f'95% CI: [{call_ci[0]:.3f}, {call_ci[1]:.3f}]')
        ax1.axvline(call_mean, color='red', linestyle='--', alpha=0.8, 
                   label=f'Mean: {call_mean:.4f}')
        ax1.axvline(call_ci[0], color='orange', linestyle='-', alpha=0.8)
        ax1.axvline(call_ci[1], color='orange', linestyle='-', alpha=0.8)
        
        ax1.set_xlabel('Call Option Price')
        ax1.set_ylabel('Density')
        ax1.set_title(f'Call Option Price Distribution\n'
                     f'Mean: {call_mean:.4f}, Std: {call_std:.4f}')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Put option histogram
        ax2.hist(put_prices, bins=50, density=True, alpha=0.7, color='green', 
                edgecolor='black', label='Monte Carlo')
        
        # Normal distribution overlay for put (for comparison)
        x_put = np.linspace(put_prices.min(), put_prices.max(), 1000)
        normal_put = stats.norm.pdf(x_put, put_mean, put_std)
        ax2.plot(x_put, normal_put, 'r-', linewidth=2, alpha=0.7, label='Normal Density (for comparison)')
        
        # Add confidence interval shading
        ax2.axvspan(put_ci[0], put_ci[1], alpha=0.3, color='orange', label=f'95% CI: [{put_ci[0]:.3f}, {put_ci[1]:.3f}]')
        ax2.axvline(put_mean, color='red', linestyle='--', alpha=0.8, 
                   label=f'Mean: {put_mean:.4f}')
        ax2.axvline(put_ci[0], color='orange', linestyle='-', alpha=0.8)
        ax2.axvline(put_ci[1], color='orange', linestyle='-', alpha=0.8)
        
        ax2.set_xlabel('Put Option Price')
        ax2.set_ylabel('Density')
        ax2.set_title(f'Put Option Price Distribution\n'
                     f'Mean: {put_mean:.4f}, Std: {put_std:.4f}')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.show()
        
        # Print detailed statistics
        self._print_detailed_statistics(call_prices, put_prices, call_mean, put_mean, 
                                       call_std, put_std, call_ci, put_ci)
    
    def _print_detailed_statistics(self, call_prices, put_prices, call_mean, put_mean, 
                                  call_std, put_std, call_ci, put_ci):
        """Print comprehensive statistics including confidence intervals."""
        print(f"\n{'='*80}")
        print(f"MONTE CARLO OPTION PRICING STATISTICS (SAMPLE SIZE {self.num_paths:,})")
        print(f"{'='*80}")
        
        # Basic statistics
        print(f"\nBasic Statistics:")
        print(f"{'Option':<10}{'Mean':<10}{'Std':<10}{'Min':<10}{'Max':<10}{'Median':<10}")
        print("-" * 80)
        print(f"{'Call':<10}{call_mean:<10.4f}{call_std:<10.4f}{call_prices.min():<10.4f}"
              f"{call_prices.max():<10.4f}{np.median(call_prices):<10.4f}")
        print(f"{'Put':<10}{put_mean:<10.4f}{put_std:<10.4f}{put_prices.min():<10.4f}"
              f"{put_prices.max():<10.4f}{np.median(put_prices):<10.4f}")
        
        # Distribution shape
        print(f"\nDistribution Shape:")
        print(f"{'Option':<10}{'Skewness':<12}{'Kurtosis (excess)':<18}{'% Zero':<12}")
        print("-" * 80)
        call_skew = stats.skew(call_prices)
        put_skew = stats.skew(put_prices)
        call_kurt = stats.kurtosis(call_prices)
        put_kurt = stats.kurtosis(put_prices)
        call_zero_pct = np.sum(call_prices == 0) / len(call_prices) * 100
        put_zero_pct = np.sum(put_prices == 0) / len(put_prices) * 100
        
        print(f"{'Call':<10}{call_skew:<12.4f}{call_kurt:<18.4f}{call_zero_pct:<5.2f}%")
        print(f"{'Put':<10}{put_skew:<12.4f}{put_kurt:<18.4f}{put_zero_pct:<5.2f}%")
        
        # Confidence intervals for option prices (what you usually want)
        print(f"\n95% Confidence Intervals for OPTION PRICES (Empirical):")
        print(f"{'Option':<10}{'Lower Bound':<12}{'Upper Bound':<12}{'Width':<12}")
        print("-" * 80)
        call_width = call_ci[1] - call_ci[0]
        put_width = put_ci[1] - put_ci[0]
        print(f"{'Call':<10}{call_ci[0]:<12.4f}{call_ci[1]:<12.4f}{call_width:<12.4f}")
        print(f"{'Put':<10}{put_ci[0]:<12.4f}{put_ci[1]:<12.4f}{put_width:<12.4f}")
        
        # Bootstrap confidence intervals for the mean estimate (for statistical inference)
        call_bootstrap_ci = self.calculate_bootstrap_ci(call_prices)
        put_bootstrap_ci = self.calculate_bootstrap_ci(put_prices)
        
        print(f"\n95% Confidence Intervals for MEAN ESTIMATE (Bootstrap):")
        print(f"{'Option':<10}{'Lower Bound':<12}{'Upper Bound':<12}{'Width':<12}")
        print("-" * 80)
        call_boot_width = call_bootstrap_ci[1] - call_bootstrap_ci[0]
        put_boot_width = put_bootstrap_ci[1] - put_bootstrap_ci[0]
        print(f"{'Call':<10}{call_bootstrap_ci[0]:<12.4f}{call_bootstrap_ci[1]:<12.4f}{call_boot_width:<12.4f}")
        print(f"{'Put':<10}{put_bootstrap_ci[0]:<12.4f}{put_bootstrap_ci[1]:<12.4f}{put_boot_width:<12.4f}")
        
        print(f"\nInterpretation:")
        print("• OPTION PRICES CI: 95% of individual option outcomes fall in this range")
        print("• MEAN ESTIMATE CI: 95% confidence that true expected price is in this range")
        print("• High skewness indicates non-normal distribution")
        print("• % Zero shows proportion of out-of-the-money options at expiration")
        print(f"{'='*80}")


if __name__ == "__main__":
    pass
```
## Exercises

**Exercise 1.**
Write the risk-neutral GBM dynamics used for Monte Carlo pricing. How is the exact solution (log-normal) used to simulate terminal stock prices?

??? success "Solution to Exercise 1"
    Under the risk-neutral measure: $dS_t = (r - q)S_t\,dt + \sigma S_t\,dW_t^Q$. The exact solution is

    $$
    S_T = S_0 xp\!\Bigl((r - q - \tfrac{1}{2}\sigma^2)T + \sigma\sqrt{T}\,Z\Bigr), \quad Z \sim \mathcal{N}(0,1)
    $$

    For MC pricing, generate $N$ draws of $Z_i \sim \mathcal{N}(0,1)$, compute $S_T^{(i)}$, and estimate the call price as $\hat{C} = e^{-rT}\frac{1}{N}\sum_{i=1}^N \max(S_T^{(i)} - K, 0)$.

---

**Exercise 2.**
Explain the antithetic variates technique. If $Z$ produces payoff $\phi_1$ and $-Z$ produces payoff $\phi_2$, show that $\mathrm{Var}(ar{\phi}_{\text{anti}}) \le \mathrm{Var}(ar{\phi})$.

??? success "Solution to Exercise 2"
    The antithetic estimator is $ar{\phi}_{\text{anti}} = \frac{1}{2}(\phi_1 + \phi_2)$. Its variance is

    $$
    \mathrm{Var}(ar{\phi}_{\text{anti}}) = \frac{1}{4}[\mathrm{Var}(\phi_1) + \mathrm{Var}(\phi_2) + 2\mathrm{Cov}(\phi_1, \phi_2)]
    $$

    Since $\phi_1$ and $\phi_2$ use the same $Z$ (and $-Z$), they are negatively correlated for monotone payoffs: $\mathrm{Cov}(\phi_1, \phi_2) < 0$. Therefore $\mathrm{Var}(ar{\phi}_{\text{anti}}) < \frac{1}{2}\mathrm{Var}(\phi_1) = \mathrm{Var}(ar{\phi})$ for $N/2$ pairs, giving the same cost but lower variance.

---

**Exercise 3.**
The MC standard error is $\mathrm{SE} = \hat{\sigma}_{\text{payoff}} / \sqrt{N}$. If the estimated price is $\$10.42$ with SE $= 0.05$, how many paths are needed for SE $= 0.01$?

??? success "Solution to Exercise 3"
    From $\mathrm{SE} = \hat{\sigma}/\sqrt{N}$, we have $\hat{\sigma} = 0.05\sqrt{N}$. With the current $N$:

    For SE $= 0.01$: $N_{\text{new}} = (\hat{\sigma}/0.01)^2 = (0.05\sqrt{N}/0.01)^2 = 25N$.

    If the original used $N = 10{,}000$ paths, we need $N_{\text{new}} = 250{,}000$. The MC convergence rate $O(1/\sqrt{N})$ means reducing SE by a factor of 5 requires 25 times as many paths.

---

**Exercise 4.**
Compare the "enhanced" mode (variance reduction) with the "legacy" mode (plain MC). Under what conditions is the variance reduction most effective?

??? success "Solution to Exercise 4"
    Variance reduction is most effective when:

    1. **Antithetic variates**: The payoff is monotone in the underlying (as for calls/puts), maximizing the negative correlation. Less effective for path-dependent options with non-monotone payoffs.
    2. **Control variates**: When a correlated instrument with a known price exists (e.g., using the European call as a control for a barrier option). Effectiveness is proportional to $
ho^2$ between the target and control payoffs.

    3. **ATM options**: Variance is highest for ATM options (large payoff uncertainty), so the absolute variance reduction is greatest there.

    For deep ITM/OTM options, the payoff variance is already small, so variance reduction provides less absolute benefit (though the relative improvement may still be significant).
