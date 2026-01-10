# ============================================================================
# vasicek/vasicek_schemes.py
# ============================================================================
import numpy as np
from typing import Callable
from .vasicek_base import VasicekParameters, VasicekScheme, VasicekNumericalError


def euler_maruyama_scheme(
    params: VasicekParameters,
    brownian_increments: np.ndarray,
    dt: float,
    **kwargs  # Absorb unused parameters for consistency with CIR
) -> np.ndarray:
    """Euler-Maruyama discretization scheme for Vasicek."""
    num_paths, num_steps = brownian_increments.shape
    rates = np.full((num_paths, num_steps + 1), params.r0, dtype=np.float64)
    
    for i in range(num_steps):
        current_rates = rates[:, i]
        
        # Vasicek dynamics: dr = a(b - r)dt + σ dW
        drift = params.a * (params.b - current_rates) * dt
        diffusion = params.sigma * brownian_increments[:, i]
        
        rates[:, i + 1] = current_rates + drift + diffusion
    
    return rates


def exact_scheme(
    params: VasicekParameters,
    brownian_increments: np.ndarray,
    dt: float,
    **kwargs
) -> np.ndarray:
    """
    Exact simulation scheme for Vasicek model.
    
    The Vasicek model has a known exact solution:
    r(t+dt) = r(t)*exp(-a*dt) + b*(1-exp(-a*dt)) + σ*sqrt((1-exp(-2*a*dt))/(2*a))*Z
    where Z ~ N(0,1)
    """
    num_paths, num_steps = brownian_increments.shape
    rates = np.full((num_paths, num_steps + 1), params.r0, dtype=np.float64)
    
    # Pre-calculate coefficients
    exp_a_dt = np.exp(-params.a * dt)
    mean_coeff = 1 - exp_a_dt
    
    if params.a != 0:
        var_coeff = params.sigma * np.sqrt((1 - np.exp(-2 * params.a * dt)) / (2 * params.a))
    else:
        var_coeff = params.sigma * np.sqrt(dt)
    
    for i in range(num_steps):
        current_rates = rates[:, i]
        
        # Exact Vasicek transition
        mean_term = current_rates * exp_a_dt + params.b * mean_coeff
        noise_term = var_coeff * brownian_increments[:, i] / np.sqrt(dt)  # Convert to standard normal
        
        rates[:, i + 1] = mean_term + noise_term
    
    return rates


def milstein_scheme(
    params: VasicekParameters,
    brownian_increments: np.ndarray,
    dt: float,
    **kwargs
) -> np.ndarray:
    """
    Milstein scheme for Vasicek model.
    
    For Vasicek, Milstein is the same as Euler-Maruyama since the diffusion
    coefficient is constant (no dependence on r).
    """
    return euler_maruyama_scheme(params, brownian_increments, dt, **kwargs)


# Scheme registry
SCHEME_REGISTRY = {
    VasicekScheme.EULER_MARUYAMA: euler_maruyama_scheme,
    VasicekScheme.EXACT: exact_scheme,
    VasicekScheme.MILSTEIN: milstein_scheme,
}


def get_scheme_simulator(scheme: VasicekScheme) -> Callable:
    """Get the appropriate scheme simulator function."""
    if scheme not in SCHEME_REGISTRY:
        raise VasicekNumericalError(f"Unknown scheme: {scheme}")
    
    return SCHEME_REGISTRY[scheme]