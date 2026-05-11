# Cir Numerical

## Background

Cir Numerical

Educational script demonstrating cir numerical concepts.

---

## Code

```python
"""
Cir Numerical

Educational script demonstrating cir numerical concepts.
"""

# ============================================================================
# cir/cir_numerical.py
# ============================================================================
import numpy as np
import scipy.optimize as opt
import scipy.stats as stats
from typing import Optional, Tuple, Dict, Any
from .cir_base import CIRParameters, CIRNumericalError


class CIRNumerical:
    """Advanced numerical methods for CIR model."""
    
    @staticmethod
    def transition_density(
        params: CIRParameters,
        r_current: float,
        r_future: float,
        dt: float
    ) -> float:
        """
        Calculate the transition probability density function for CIR.
        
        The CIR process has a known transition density involving
        the non-central chi-squared distribution.
        """
        try:
            c = 2 * params.kappa / (params.sigma**2 * (1 - np.exp(-params.kappa * dt)))
            q = 2 * params.kappa * params.theta / params.sigma**2 - 1
            
            nc = c * r_current * np.exp(-params.kappa * dt)  # non-centrality parameter
            x = c * r_future
            
            # Use non-central chi-squared density
            return c * stats.ncx2.pdf(x, df=2*(q+1), nc=nc)
            
        except Exception as e:
            raise CIRNumericalError(f"Transition density calculation failed: {e}")
    
    @staticmethod
    def exact_simulation_step(
        params: CIRParameters,
        r_current: float,
        dt: float,
        random_state: Optional[np.random.RandomState] = None
    ) -> float:
        """
        Exact simulation of one CIR step using non-central chi-squared distribution.
        
        This is the theoretically correct way to simulate CIR, but requires
        sampling from non-central chi-squared distribution.
        """
        if random_state is None:
            random_state = np.random.RandomState()
        
        try:
            # Parameters for the exact distribution
            c = 2 * params.kappa / (params.sigma**2 * (1 - np.exp(-params.kappa * dt)))
            q = 2 * params.kappa * params.theta / params.sigma**2 - 1
            nc = c * r_current * np.exp(-params.kappa * dt)
            
            # Sample from non-central chi-squared
            chi_squared_sample = stats.ncx2.rvs(df=2*(q+1), nc=nc, random_state=random_state)
            
            return chi_squared_sample / c
            
        except Exception as e:
            raise CIRNumericalError(f"Exact simulation step failed: {e}")
    
    @staticmethod
    def calibrate_to_yield_curve(
        yield_curve_maturities: np.ndarray,
        yield_curve_rates: np.ndarray,
        initial_guess: Optional[Dict[str, float]] = None
    ) -> Tuple[CIRParameters, Dict[str, Any]]:
        """
        Calibrate CIR parameters to match an observed yield curve.
        
        Uses optimization to find parameters that best fit the yield curve.
        """
        if len(yield_curve_maturities) != len(yield_curve_rates):
            raise ValueError("Maturities and rates must have same length")
        
        # Set up initial guess
        if initial_guess is None:
            initial_guess = {
                'r0': yield_curve_rates[0],
                'theta': np.mean(yield_curve_rates),
                'kappa': 0.1,
                'sigma': 0.03
            }
        
        def objective_function(params_array):
            """Objective function for optimization."""
            try:
                r0, theta, kappa, sigma = params_array
                
                # Ensure positive parameters
                if any(p <= 0 for p in [r0, theta, kappa, sigma]):
                    return 1e6
                
                # Create temporary parameters
                temp_params = CIRParameters(
                    r0=r0, theta=theta, kappa=kappa, sigma=sigma, maturity_time=max(yield_curve_maturities)
                )
                
                # Calculate model yield curve
                from .cir_formula import CIRBondPricer
                model_yields = CIRBondPricer.yield_curve(temp_params, r0, yield_curve_maturities)
                
                # Calculate sum of squared errors
                return np.sum((model_yields - yield_curve_rates)**2)
                
            except Exception:
                return 1e6
        
        # Set up optimization
        initial_params = [
            initial_guess['r0'],
            initial_guess['theta'], 
            initial_guess['kappa'],
            initial_guess['sigma']
        ]
        
        # Bounds to ensure positive parameters
        bounds = [(1e-6, 1.0), (1e-6, 1.0), (1e-6, 5.0), (1e-6, 1.0)]
        
        try:
            # Run optimization
            result = opt.minimize(
                objective_function,
                initial_params,
                method='L-BFGS-B',
                bounds=bounds
            )
            
            if result.success:
                r0_opt, theta_opt, kappa_opt, sigma_opt = result.x
                
                optimized_params = CIRParameters(
                    r0=r0_opt,
                    theta=theta_opt,
                    kappa=kappa_opt,
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
                raise CIRNumericalError(f"Optimization failed: {result.message}")
                
        except Exception as e:
            raise CIRNumericalError(f"Calibration failed: {e}")


class CIRRiskMetrics:
    """Risk metrics and sensitivity analysis for CIR model."""
    
    @staticmethod
    def duration(params: CIRParameters, current_rate: float, maturity: float) -> float:
        """Calculate modified duration of a zero-coupon bond."""
        # Numerical derivative of bond price with respect to rate
        dr = 1e-6
        
        from .cir_formula import CIRBondPricer
        
        price_up = CIRBondPricer.zero_coupon_bond_price(params, current_rate + dr, maturity)
        price_down = CIRBondPricer.zero_coupon_bond_price(params, current_rate - dr, maturity)
        price_base = CIRBondPricer.zero_coupon_bond_price(params, current_rate, maturity)
        
        return -(price_up - price_down) / (2 * dr * price_base)
    
    @staticmethod
    def convexity(params: CIRParameters, current_rate: float, maturity: float) -> float:
        """Calculate convexity of a zero-coupon bond."""
        # Numerical second derivative
        dr = 1e-6
        
        from .cir_formula import CIRBondPricer
        
        price_up = CIRBondPricer.zero_coupon_bond_price(params, current_rate + dr, maturity)
        price_down = CIRBondPricer.zero_coupon_bond_price(params, current_rate - dr, maturity)
        price_base = CIRBondPricer.zero_coupon_bond_price(params, current_rate, maturity)
        
        return (price_up - 2 * price_base + price_down) / (dr**2 * price_base)
    
    @staticmethod
    def parameter_sensitivities(
        params: CIRParameters,
        current_rate: float,
        maturity: float
    ) -> Dict[str, float]:
        """Calculate sensitivities to CIR parameters."""
        from .cir_formula import CIRBondPricer
        
        base_price = CIRBondPricer.zero_coupon_bond_price(params, current_rate, maturity)
        
        sensitivities = {}
        delta = 1e-6
        
        # Sensitivity to kappa
        params_kappa_up = CIRParameters(
            params.r0, params.theta, params.kappa + delta, params.sigma, params.maturity_time
        )
        price_kappa_up = CIRBondPricer.zero_coupon_bond_price(params_kappa_up, current_rate, maturity)
        sensitivities['kappa'] = (price_kappa_up - base_price) / delta
        
        # Sensitivity to theta
        params_theta_up = CIRParameters(
            params.r0, params.theta + delta, params.kappa, params.sigma, params.maturity_time
        )
        price_theta_up = CIRBondPricer.zero_coupon_bond_price(params_theta_up, current_rate, maturity)
        sensitivities['theta'] = (price_theta_up - base_price) / delta
        
        # Sensitivity to sigma
        params_sigma_up = CIRParameters(
            params.r0, params.theta, params.kappa, params.sigma + delta, params.maturity_time
        )
        price_sigma_up = CIRBondPricer.zero_coupon_bond_price(params_sigma_up, current_rate, maturity)
        sensitivities['sigma'] = (price_sigma_up - base_price) / delta
        
        return sensitivities


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
The CIR transition density involves the non-central chi-squared distribution. Given parameters $\kappa = 0.2$, $\theta = 0.05$, $\sigma = 0.04$, $r_{\text{current}} = 0.03$, and $\Delta t = 1$, compute the scaling factor $c$ and the non-centrality parameter $\lambda$.

??? success "Solution to Exercise 1"
    The scaling factor is

    $$
    c = \frac{2\kappa}{\sigma^2(1 - e^{-\kappa \Delta t})} = \frac{2 \times 0.2}{0.04^2 \times (1 - e^{-0.2})} = \frac{0.4}{0.0016 \times 0.1813} = \frac{0.4}{0.000290} \approx 1379.3.
    $$

    The non-centrality parameter is

    $$
    \lambda = c \cdot r_{\text{current}} \cdot e^{-\kappa \Delta t} = 1379.3 \times 0.03 \times e^{-0.2} \approx 1379.3 \times 0.03 \times 0.8187 \approx 33.87.
    $$

---

**Exercise 2.**
Explain the difference between the Euler-Maruyama approximation and the exact simulation step for the CIR model. When would you prefer one over the other?

??? success "Solution to Exercise 2"
    The Euler-Maruyama scheme discretizes the SDE directly:

    $$
    r_{i+1} = r_i + \kappa(\theta - r_i)\,\Delta t + \sigma\sqrt{r_i}\,\Delta W_i.
    $$

    It introduces discretization error of order $O(\sqrt{\Delta t})$ and can produce negative values. The exact simulation uses the known transition distribution: $c \cdot r_{t+\Delta t}$ follows a non-central chi-squared distribution with degrees of freedom $2q + 2$ and non-centrality $\lambda = c \cdot r_t \cdot e^{-\kappa \Delta t}$. The exact method has no discretization error regardless of time step size, but requires sampling from the non-central chi-squared distribution, which is computationally more expensive per step. Prefer exact simulation for accuracy (e.g., pricing or calibration), and Euler-Maruyama for speed in exploratory analysis with fine time grids.

---

**Exercise 3.**
The calibration method minimizes the sum of squared errors between model yields and observed yields. If the observed yield curve has maturities $T \in \{1, 5, 10, 30\}$ with yields $\{2\%, 3\%, 3.5\%, 4\%\}$, write the objective function explicitly.

??? success "Solution to Exercise 3"
    Let $\hat{y}(T; r_0, \theta, \kappa, \sigma)$ denote the CIR model yield at maturity $T$. The objective function is

    $$
    f(r_0, \theta, \kappa, \sigma) = \sum_{i=1}^{4} \bigl[\hat{y}(T_i; r_0, \theta, \kappa, \sigma) - y_i^{\text{obs}}\bigr]^2,
    $$

    which expands to

    $$
    f = [\hat{y}(1) - 0.02]^2 + [\hat{y}(5) - 0.03]^2 + [\hat{y}(10) - 0.035]^2 + [\hat{y}(30) - 0.04]^2.
    $$

    The model yield is $\hat{y}(T) = -\ln P(r_0, 0, T)/T$, where $P$ is the CIR bond price. The optimization finds $(r_0^*, \theta^*, \kappa^*, \sigma^*)$ that minimizes $f$ subject to positivity constraints.

---

**Exercise 4.**
Using the numerical duration and convexity formulas in the code, compute the approximate bond price change when the rate shifts from $r = 0.04$ to $r = 0.045$, given a duration of $D = 7.5$ and convexity of $C = 65$. The current bond price is $P = 0.70$.

??? success "Solution to Exercise 4"
    The second-order Taylor approximation for the bond price change is

    $$
    \Delta P \approx -D \cdot \Delta r \cdot P + \frac{1}{2}\,C \cdot (\Delta r)^2 \cdot P,
    $$

    where $\Delta r = 0.005$. Substituting:

    $$
    \Delta P \approx -7.5 \times 0.005 \times 0.70 + \frac{1}{2} \times 65 \times (0.005)^2 \times 0.70.
    $$

    Computing each term:

    $$
    \Delta P \approx -0.02625 + 0.5 \times 65 \times 0.000025 \times 0.70 = -0.02625 + 0.000569 \approx -0.02568.
    $$

    The bond price decreases by approximately $0.0257$, from $0.70$ to about $0.6743$.
