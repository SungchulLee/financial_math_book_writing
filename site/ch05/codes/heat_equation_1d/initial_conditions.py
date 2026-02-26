# ============================================================================
# heat_equation_1d/initial_conditions.py
# ============================================================================
import numpy as np
from typing import Callable


def step_function(x: np.ndarray, start: float = 0.4, end: float = 0.6, 
                  value: float = 1.0, L: float = 1.0) -> np.ndarray:
    """
    Create a step function initial condition.
    
    Args:
        x: Spatial grid points
        start: Relative start position (0 to 1)
        end: Relative end position (0 to 1)
        value: Height of the step
        L: Length of domain
        
    Returns:
        Initial condition array
    """
    u_initial = np.zeros_like(x)
    mask = (x >= start * L) & (x <= end * L)
    u_initial[mask] = value
    return u_initial


def gaussian_pulse(x: np.ndarray, center: float = 0.5, width: float = 0.1, 
                   amplitude: float = 1.0, L: float = 1.0) -> np.ndarray:
    """
    Create a Gaussian pulse initial condition.
    
    Args:
        x: Spatial grid points
        center: Relative center position (0 to 1)
        width: Width parameter (standard deviation)
        amplitude: Peak amplitude
        L: Length of domain
        
    Returns:
        Initial condition array
    """
    x_center = center * L
    return amplitude * np.exp(-(x - x_center)**2 / (2 * width**2))


def sine_wave(x: np.ndarray, n_modes: int = 1, amplitude: float = 1.0, 
              L: float = 1.0) -> np.ndarray:
    """
    Create a sine wave initial condition.
    
    Args:
        x: Spatial grid points
        n_modes: Number of sine modes
        amplitude: Amplitude of the wave
        L: Length of domain
        
    Returns:
        Initial condition array
    """
    return amplitude * np.sin(n_modes * np.pi * x / L)


def triangle_wave(x: np.ndarray, peak_pos: float = 0.5, amplitude: float = 1.0, 
                  L: float = 1.0) -> np.ndarray:
    """
    Create a triangle wave initial condition.
    
    Args:
        x: Spatial grid points
        peak_pos: Relative position of peak (0 to 1)
        amplitude: Peak amplitude
        L: Length of domain
        
    Returns:
        Initial condition array
    """
    x_peak = peak_pos * L
    u_initial = np.zeros_like(x)
    
    # Left side of triangle
    left_mask = x <= x_peak
    u_initial[left_mask] = amplitude * x[left_mask] / x_peak
    
    # Right side of triangle
    right_mask = x > x_peak
    u_initial[right_mask] = amplitude * (L - x[right_mask]) / (L - x_peak)
    
    return u_initial


def custom_function(x: np.ndarray, func: Callable[[np.ndarray], np.ndarray]) -> np.ndarray:
    """
    Create initial condition from a custom function.
    
    Args:
        x: Spatial grid points
        func: Function that takes x array and returns u array
        
    Returns:
        Initial condition array
    """
    return func(x)


def zero_initial_condition(x: np.ndarray) -> np.ndarray:
    """
    Create zero initial condition (useful for source problems).
    
    Args:
        x: Spatial grid points
        
    Returns:
        Zero initial condition array
    """
    return np.zeros_like(x)