# ============================================================================
# vasicek/vasicek_formula.py
# ============================================================================
import numpy as np
from .vasicek_base import VasicekParameters, VasicekNumericalError


class VasicekAnalytical:
    """Analytical formulas for Vasicek model."""
    
    @staticmethod
    def mean(params: VasicekParameters, t: float) -> float:
        """Analytical mean of Vasicek process at time t."""
        if t <= 0:
            return params.r0
        return params.b + (params.r0 - params.b) * np.exp(-params.a * t)
    
    @staticmethod
    def variance(params: VasicekParameters, t: float) -> float:
        """Analytical variance of Vasicek process at time t."""
        if t <= 0:
            return 0.0
        return (params.sigma**2 / (2 * params.a)) * (1 - np.exp(-2 * params.a * t))
    
    @staticmethod
    def standard_deviation(params: VasicekParameters, t: float) -> float:
        """Analytical standard deviation at time t."""
        return np.sqrt(VasicekAnalytical.variance(params, t))


class VasicekBondPricer:
    """Bond pricing utilities for Vasicek model."""
    
    @staticmethod
    def zero_coupon_bond_price(
        params: VasicekParameters,
        current_rate: float,
        time_to_maturity: float
    ) -> float:
        """
        Calculate analytical zero-coupon bond price using Vasicek formula.
        
        P(r,t,T) = A(t,T) * exp(-B(t,T) * r)
        """
        if time_to_maturity <= 0:
            return 1.0
        
        try:
            # B(t,T) coefficient
            if params.a == 0:
                B_T = time_to_maturity
            else:
                B_T = (1 - np.exp(-params.a * time_to_maturity)) / params.a
            
            # A(t,T) coefficient
            if params.a == 0:
                A_T = np.exp(-params.b * time_to_maturity + 
                            (params.sigma**2 * time_to_maturity**3) / 6)
            else:
                term1 = (params.b - params.sigma**2 / (2 * params.a**2)) * (B_T - time_to_maturity)
                term2 = (params.sigma**2 / (4 * params.a)) * B_T**2
                A_T = np.exp(term1 - term2)
            
            # Bond price
            bond_price = A_T * np.exp(-B_T * current_rate)
            
            return float(np.clip(bond_price, 1e-10, 1.0))
            
        except (OverflowError, ZeroDivisionError, ValueError) as e:
            raise VasicekNumericalError(f"Bond pricing computation failed: {e}")
    
    @staticmethod
    def yield_to_maturity(
        params: VasicekParameters,
        current_rate: float,
        time_to_maturity: float
    ) -> float:
        """Calculate yield to maturity from bond price."""
        if time_to_maturity <= 0:
            return current_rate
        
        bond_price = VasicekBondPricer.zero_coupon_bond_price(
            params, current_rate, time_to_maturity
        )
        return -np.log(bond_price) / time_to_maturity
    
    @staticmethod
    def yield_curve(
        params: VasicekParameters,
        current_rate: float,
        maturities: np.ndarray
    ) -> np.ndarray:
        """Calculate yield curve for given maturities."""
        yields = np.zeros_like(maturities)
        
        for i, T in enumerate(maturities):
            yields[i] = VasicekBondPricer.yield_to_maturity(params, current_rate, T)
        
        return yields
    
    @staticmethod
    def forward_rate(
        params: VasicekParameters,
        current_rate: float,
        t1: float,
        t2: float
    ) -> float:
        """Calculate forward rate between times t1 and t2."""
        if t1 >= t2:
            raise ValueError("t1 must be less than t2")
        
        P_t1 = VasicekBondPricer.zero_coupon_bond_price(params, current_rate, t1)
        P_t2 = VasicekBondPricer.zero_coupon_bond_price(params, current_rate, t2)
        
        return np.log(P_t1 / P_t2) / (t2 - t1)