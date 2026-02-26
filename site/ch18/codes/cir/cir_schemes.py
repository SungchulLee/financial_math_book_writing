# ============================================================================
# cir/cir_schemes.py
# ============================================================================
import numpy as np
from typing import Callable
from .cir_base import CIRParameters, CIRScheme, CIRNumericalError


def euler_maruyama_scheme(
    params: CIRParameters,
    brownian_increments: np.ndarray,
    dt: float,
    absorption_fix: bool = True
) -> np.ndarray:
    """Euler-Maruyama discretization scheme for CIR."""
    num_paths, num_steps = brownian_increments.shape
    rates = np.full((num_paths, num_steps + 1), params.r0, dtype=np.float64)
    
    for i in range(num_steps):
        current_rates = rates[:, i]
        
        # Ensure non-negative rates for square root
        current_rates_pos = np.maximum(current_rates, 0.0)
        sqrt_rates = np.sqrt(current_rates_pos)
        
        # CIR dynamics: dr = κ(θ - r)dt + σ√r dW
        drift = params.kappa * (params.theta - current_rates) * dt
        diffusion = params.sigma * sqrt_rates * brownian_increments[:, i]
        
        rates[:, i + 1] = current_rates + drift + diffusion
        
        # Apply absorption at zero if requested
        if absorption_fix:
            rates[:, i + 1] = np.maximum(rates[:, i + 1], 0.0)
    
    return rates


def milstein_scheme(
    params: CIRParameters,
    brownian_increments: np.ndarray,
    dt: float,
    absorption_fix: bool = True
) -> np.ndarray:
    """Milstein discretization scheme with second-order correction."""
    num_paths, num_steps = brownian_increments.shape
    rates = np.full((num_paths, num_steps + 1), params.r0, dtype=np.float64)
    
    for i in range(num_steps):
        current_rates = rates[:, i]
        current_rates_pos = np.maximum(current_rates, 0.0)
        sqrt_rates = np.sqrt(current_rates_pos)
        
        dW = brownian_increments[:, i]
        
        # Euler part
        drift = params.kappa * (params.theta - current_rates) * dt
        diffusion = params.sigma * sqrt_rates * dW
        
        # Milstein correction: 0.5 * σ * (∂σ/∂r) * (dW² - dt)
        # For CIR: σ(r) = σ√r, so ∂σ/∂r = σ/(2√r)
        milstein_correction = 0.25 * params.sigma**2 * (dW**2 - dt)
        
        rates[:, i + 1] = current_rates + drift + diffusion + milstein_correction
        
        if absorption_fix:
            rates[:, i + 1] = np.maximum(rates[:, i + 1], 0.0)
    
    return rates


def truncated_euler_scheme(
    params: CIRParameters,
    brownian_increments: np.ndarray,
    dt: float,
    absorption_fix: bool = True
) -> np.ndarray:
    """Truncated Euler scheme that handles negative rates more carefully."""
    num_paths, num_steps = brownian_increments.shape
    rates = np.full((num_paths, num_steps + 1), params.r0, dtype=np.float64)
    
    for i in range(num_steps):
        current_rates = rates[:, i]
        
        # Drift uses original rate for mean reversion
        drift = params.kappa * (params.theta - current_rates) * dt
        
        # Diffusion uses truncated rate to avoid sqrt of negative
        current_rates_pos = np.maximum(current_rates, 0.0)
        sqrt_rates = np.sqrt(current_rates_pos)
        diffusion = params.sigma * sqrt_rates * brownian_increments[:, i]
        
        rates[:, i + 1] = current_rates + drift + diffusion
        
        # Always apply truncation in this scheme
        rates[:, i + 1] = np.maximum(rates[:, i + 1], 0.0)
    
    return rates


def exact_scheme(
    params: CIRParameters,
    brownian_increments: np.ndarray,
    dt: float,
    absorption_fix: bool = True
) -> np.ndarray:
    """
    Exact simulation scheme using non-central chi-squared distribution.
    
    Note: This is a placeholder implementation.
    Full exact simulation requires sampling from non-central chi-squared.
    """
    # For now, fall back to Milstein which is more accurate than Euler
    return milstein_scheme(params, brownian_increments, dt, absorption_fix)


# Scheme registry
SCHEME_REGISTRY = {
    CIRScheme.EULER_MARUYAMA: euler_maruyama_scheme,
    CIRScheme.MILSTEIN: milstein_scheme,
    CIRScheme.TRUNCATED_EULER: truncated_euler_scheme,
    CIRScheme.EXACT: exact_scheme,
}


def get_scheme_simulator(scheme: CIRScheme) -> Callable:
    """Get the appropriate scheme simulator function."""
    if scheme not in SCHEME_REGISTRY:
        raise CIRNumericalError(f"Unknown scheme: {scheme}")
    
    return SCHEME_REGISTRY[scheme]