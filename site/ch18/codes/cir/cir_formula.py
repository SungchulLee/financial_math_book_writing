# ============================================================================
# cir/cir_formula.py
# ============================================================================
import numpy as np
from .cir_base import CIRParameters, CIRNumericalError


class CIRAnalytical:
    """Analytical formulas for CIR model."""
    
    @staticmethod
    def mean(params: CIRParameters, t: float) -> float:
        """Analytical mean of CIR process at time t."""
        if t <= 0:
            return params.r0
        return params.theta + (params.r0 - params.theta) * np.exp(-params.kappa * t)
    
    @staticmethod
    def variance(params: CIRParameters, t: float) -> float:
        """Analytical variance of CIR process at time t."""
        if t <= 0:
            return 0.0
            
        exp_kt = np.exp(-params.kappa * t)
        exp_2kt = np.exp(-2 * params.kappa * t)
        
        term1 = (params.r0 * params.sigma**2 / params.kappa) * (exp_kt - exp_2kt)
        term2 = (params.theta * params.sigma**2 / (2 * params.kappa)) * (1 - exp_kt)**2
        
        return term1 + term2
    
    @staticmethod
    def standard_deviation(params: CIRParameters, t: float) -> float:
        """Analytical standard deviation at time t."""
        return np.sqrt(CIRAnalytical.variance(params, t))


class CIRBondPricer:
    """Bond pricing utilities for CIR model."""
    
    @staticmethod
    def zero_coupon_bond_price(
        params: CIRParameters,
        current_rate: float,
        time_to_maturity: float
    ) -> float:
        """
        Calculate analytical zero-coupon bond price using CIR formula.
        
        P(r,t,T) = A(t,T) * exp(-B(t,T) * r)
        """
        if time_to_maturity <= 0:
            return 1.0
        
        if current_rate < 0:
            raise CIRNumericalError("Current rate cannot be negative")
        
        try:
            # Calculate helper variables
            gamma = np.sqrt(params.kappa**2 + 2 * params.sigma**2)
            exp_gamma_T = np.exp(gamma * time_to_maturity)
            
            # B(t,T) coefficient
            numerator = 2 * (exp_gamma_T - 1)
            denominator = (gamma + params.kappa) * (exp_gamma_T - 1) + 2 * gamma
            B_T = numerator / denominator
            
            # A(t,T) coefficient (using log for numerical stability)
            nu = 2 * params.kappa * params.theta / (params.sigma**2)
            
            A_numerator = 2 * gamma * np.exp((params.kappa + gamma) * time_to_maturity / 2)
            A_denominator = denominator  # Same as B_T denominator
            
            log_A_T = nu * (np.log(A_numerator) - np.log(A_denominator))
            
            # Bond price calculation
            log_bond_price = log_A_T - B_T * current_rate
            bond_price = np.exp(log_bond_price)
            
            # Ensure reasonable bounds
            return float(np.clip(bond_price, 1e-10, 1.0))
            
        except (OverflowError, ZeroDivisionError, ValueError) as e:
            raise CIRNumericalError(f"Bond pricing computation failed: {e}")
    
    @staticmethod
    def yield_to_maturity(
        params: CIRParameters,
        current_rate: float,
        time_to_maturity: float
    ) -> float:
        """Calculate yield to maturity from bond price."""
        if time_to_maturity <= 0:
            return current_rate
        
        bond_price = CIRBondPricer.zero_coupon_bond_price(
            params, current_rate, time_to_maturity
        )
        return -np.log(bond_price) / time_to_maturity
    
    @staticmethod
    def yield_curve(
        params: CIRParameters,
        current_rate: float,
        maturities: np.ndarray
    ) -> np.ndarray:
        """Calculate yield curve for given maturities."""
        yields = np.zeros_like(maturities)
        
        for i, T in enumerate(maturities):
            yields[i] = CIRBondPricer.yield_to_maturity(params, current_rate, T)
        
        return yields
    
    @staticmethod
    def forward_rate(
        params: CIRParameters,
        current_rate: float,
        t1: float,
        t2: float
    ) -> float:
        """Calculate forward rate between times t1 and t2."""
        if t1 >= t2:
            raise ValueError("t1 must be less than t2")
        
        P_t1 = CIRBondPricer.zero_coupon_bond_price(params, current_rate, t1)
        P_t2 = CIRBondPricer.zero_coupon_bond_price(params, current_rate, t2)
        
        return np.log(P_t1 / P_t2) / (t2 - t1)