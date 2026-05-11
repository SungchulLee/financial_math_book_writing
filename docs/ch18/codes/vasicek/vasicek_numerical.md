# Vasicek Numerical

## Background

Vasicek Numerical

Educational script demonstrating vasicek numerical concepts.

---

## Code

```python
"""
Vasicek Numerical

Educational script demonstrating vasicek numerical concepts.
"""

# ============================================================================
# vasicek/vasicek_numerical.py
# ============================================================================
import numpy as np
from typing import Optional, Tuple, Dict, Any
from .vasicek_base import VasicekParameters, VasicekNumericalError


class VasicekNumerical:
    """Advanced numerical methods for Vasicek model."""
    
    @staticmethod
    def transition_density(
        params: VasicekParameters,
        r_current: float,
        r_future: float,
        dt: float
    ) -> float:
        """
        Calculate the transition probability density function for Vasicek.
        
        The Vasicek process has a Gaussian transition density.
        """
        try:
            # Analytical mean and variance for transition
            mean = params.b + (r_current - params.b) * np.exp(-params.a * dt)
            variance = (params.sigma**2 / (2 * params.a)) * (1 - np.exp(-2 * params.a * dt))
            
            if variance <= 0:
                raise ValueError("Variance must be positive")
            
            # Gaussian density
            density = (1 / np.sqrt(2 * np.pi * variance)) * np.exp(-0.5 * (r_future - mean)**2 / variance)
            
            return density
            
        except Exception as e:
            raise VasicekNumericalError(f"Transition density calculation failed: {e}")
    
    @staticmethod
    def calibrate_to_yield_curve(
        yield_curve_maturities: np.ndarray,
        yield_curve_rates: np.ndarray,
        initial_guess: Optional[Dict[str, float]] = None
    ) -> Tuple[VasicekParameters, Dict[str, Any]]:
        """
        Calibrate Vasicek parameters to match an observed yield curve.
        
        Uses optimization to find parameters that best fit the yield curve.
        """
        try:
            from scipy import optimize
        except ImportError:
            raise VasicekNumericalError("scipy required for yield curve calibration")
        
        if len(yield_curve_maturities) != len(yield_curve_rates):
            raise ValueError("Maturities and rates must have same length")
        
        # Set up initial guess
        if initial_guess is None:
            initial_guess = {
                'r0': yield_curve_rates[0],
                'b': np.mean(yield_curve_rates),
                'a': 0.1,
                'sigma': 0.02
            }
        
        def objective_function(params_array):
            """Objective function for optimization."""
            try:
                r0, b, a, sigma = params_array
                
                # Ensure positive parameters where needed
                if a <= 0 or sigma <= 0:
                    return 1e6
                
                # Create temporary parameters
                temp_params = VasicekParameters(
                    r0=r0, b=b, a=a, sigma=sigma, 
                    maturity_time=max(yield_curve_maturities)
                )
                
                # Calculate model yield curve
                from .vasicek_formula import VasicekBondPricer
                model_yields = VasicekBondPricer.yield_curve(temp_params, r0, yield_curve_maturities)
                
                # Calculate sum of squared errors
                return np.sum((model_yields - yield_curve_rates)**2)
                
            except Exception:
                return 1e6
        
        # Set up optimization
        initial_params = [
            initial_guess['r0'],
            initial_guess['b'], 
            initial_guess['a'],
            initial_guess['sigma']
        ]
        
        # Bounds: r0 and b can be negative, a and sigma must be positive
        bounds = [(-0.1, 1.0), (-0.1, 1.0), (1e-6, 5.0), (1e-6, 1.0)]
        
        try:
            # Run optimization
            result = optimize.minimize(
                objective_function,
                initial_params,
                method='L-BFGS-B',
                bounds=bounds
            )
            
            if result.success:
                r0_opt, b_opt, a_opt, sigma_opt = result.x
                
                optimized_params = VasicekParameters(
                    r0=r0_opt,
                    b=b_opt,
                    a=a_opt,
                    sigma=sigma_opt,
                    maturity_time=max(yield_curve_maturities)
                )
                
                optimization_info = {
                    'success': True,
                    'final_error': result.fun,
                    'iterations': result.nit,
                    'message': result.message
                }
                
                return optimized_params, optimization_info
                
            else:
                raise VasicekNumericalError(f"Optimization failed: {result.message}")
                
        except Exception as e:
            raise VasicekNumericalError(f"Calibration failed: {e}")


class VasicekRiskMetrics:
    """Risk metrics and sensitivity analysis for Vasicek model."""
    
    @staticmethod
    def duration(params: VasicekParameters, current_rate: float, maturity: float) -> float:
        """Calculate modified duration of a zero-coupon bond."""
        # For Vasicek, we can calculate this analytically
        if params.a == 0:
            return maturity
        
        B_T = (1 - np.exp(-params.a * maturity)) / params.a
        return B_T
    
    @staticmethod
    def convexity(params: VasicekParameters, current_rate: float, maturity: float) -> float:
        """Calculate convexity of a zero-coupon bond."""
        # Analytical convexity for Vasicek
        if params.a == 0:
            return maturity**2
        
        B_T = (1 - np.exp(-params.a * maturity)) / params.a
        return B_T**2
    
    @staticmethod
    def parameter_sensitivities(
        params: VasicekParameters,
        current_rate: float,
        maturity: float
    ) -> Dict[str, float]:
        """Calculate sensitivities to Vasicek parameters."""
        from .vasicek_formula import VasicekBondPricer
        
        base_price = VasicekBondPricer.zero_coupon_bond_price(params, current_rate, maturity)
        
        sensitivities = {}
        delta = 1e-6
        
        # Sensitivity to a (mean reversion)
        params_a_up = VasicekParameters(
            params.r0, params.b, params.a + delta, params.sigma, params.maturity_time
        )
        price_a_up = VasicekBondPricer.zero_coupon_bond_price(params_a_up, current_rate, maturity)
        sensitivities['a'] = (price_a_up - base_price) / delta
        
        # Sensitivity to b (long-term mean)
        params_b_up = VasicekParameters(
            params.r0, params.b + delta, params.a, params.sigma, params.maturity_time
        )
        price_b_up = VasicekBondPricer.zero_coupon_bond_price(params_b_up, current_rate, maturity)
        sensitivities['b'] = (price_b_up - base_price) / delta
        
        # Sensitivity to sigma
        params_sigma_up = VasicekParameters(
            params.r0, params.b, params.a, params.sigma + delta, params.maturity_time
        )
        price_sigma_up = VasicekBondPricer.zero_coupon_bond_price(params_sigma_up, current_rate, maturity)
        sensitivities['sigma'] = (price_sigma_up - base_price) / delta
        
        return sensitivities


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
The Vasicek transition density is Gaussian. Given $a = 0.15$, $b = 0.05$, $\sigma = 0.02$, $r_{\text{current}} = 0.03$, and $\Delta t = 1$, compute the conditional mean and variance of $r(t + 1) \mid r(t) = 0.03$.

??? success "Solution to Exercise 1"
    The conditional mean is

    $$
    \mu = b + (r_{\text{current}} - b)e^{-a\Delta t} = 0.05 + (0.03 - 0.05)e^{-0.15} = 0.05 - 0.02 \times 0.8607 = 0.03279.
    $$

    The conditional variance is

    $$
    v^2 = \frac{\sigma^2}{2a}(1 - e^{-2a\Delta t}) = \frac{0.0004}{0.3}(1 - e^{-0.3}) = 0.001333 \times 0.2592 = 0.000346.
    $$

    The standard deviation is $\sqrt{0.000346} \approx 0.0186$.

---

**Exercise 2.**
Explain how the Vasicek duration $D = B(T) = (1 - e^{-aT})/a$ differs from the Macaulay duration of a zero-coupon bond, which equals $T$.

??? success "Solution to Exercise 2"
    The Macaulay duration of a zero-coupon bond is simply its maturity $T$, representing the weighted average time of cash flows. The Vasicek duration $B(T) = (1 - e^{-aT})/a$ is the model-specific sensitivity of the bond price to changes in the short rate:

    $$
    D_{\text{Vasicek}} = -\frac{1}{P}\frac{\partial P}{\partial r} = B(T).
    $$

    For small $a$ (weak mean reversion), $B(T) \approx T$, recovering Macaulay duration. For large $a$, $B(T) \to 1/a$, which is bounded. This saturation reflects that under strong mean reversion, rate shocks are transient, so long-dated bonds are less sensitive to the current short rate than Macaulay duration would suggest.

---

**Exercise 3.**
The Vasicek convexity for a zero-coupon bond is $C = B(T)^2$. If $a = 0.1$ and $T = 10$, compute the convexity and interpret it.

??? success "Solution to Exercise 3"
    First compute $B(10) = (1 - e^{-1})/0.1 = (1 - 0.3679)/0.1 = 6.321$. Then

    $$
    C = B(10)^2 = 6.321^2 = 39.95.
    $$

    Convexity measures the curvature of the price-yield relationship. A positive convexity of $39.95$ means that the bond price gains more from a rate decrease than it loses from an equal rate increase. For a 1-basis-point rate change, the convexity adjustment to the duration approximation is $\frac{1}{2} \times 39.95 \times (0.0001)^2 \approx 2 \times 10^{-7}$, which is negligible for small shifts but becomes important for large rate moves.

---

**Exercise 4.**
The OLS calibration for Vasicek uses the discrete regression $r_{t+1} = \alpha + \beta r_t + \varepsilon_t$. Show how $\alpha$ and $\beta$ relate to the continuous-time parameters $a$ and $b$.

??? success "Solution to Exercise 4"
    The exact discrete-time transition of the Vasicek model is

    $$
    r_{t+1} = b(1 - e^{-a\Delta t}) + e^{-a\Delta t}\,r_t + \varepsilon_t,
    $$

    where $\varepsilon_t \sim \mathcal{N}(0, \sigma^2(1 - e^{-2a\Delta t})/(2a))$. Comparing with $r_{t+1} = \alpha + \beta\,r_t + \varepsilon_t$:

    $$
    \beta = e^{-a\Delta t}, \qquad \alpha = b(1 - \beta).
    $$

    Inverting: $a = -\ln(\beta)/\Delta t$ and $b = \alpha/(1 - \beta)$. The volatility is recovered from the residual variance: $\sigma = \hat{\sigma}_\varepsilon \sqrt{2a/(1 - \beta^2)}$.
