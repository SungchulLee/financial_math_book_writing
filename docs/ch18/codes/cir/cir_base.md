# Cir Base

## Background

Cir Base

Educational script demonstrating cir base concepts.

---

## Code

```python
"""
Cir Base

Educational script demonstrating cir base concepts.
"""

# ============================================================================
# cir/cir_base.py
# ============================================================================
import warnings
from dataclasses import dataclass
from enum import Enum
from typing import Dict


class CIRScheme(Enum):
    """CIR discretization schemes."""
    EULER_MARUYAMA = "euler_maruyama"
    MILSTEIN = "milstein"
    EXACT = "exact"
    TRUNCATED_EULER = "truncated_euler"


class CIRConfig:
    """Configuration class for CIR model settings."""
    
    # Default model parameters
    DEFAULT_R0 = 0.03
    DEFAULT_THETA = 0.05
    DEFAULT_KAPPA = 0.1
    DEFAULT_SIGMA = 0.03
    DEFAULT_MATURITY = 10.0
    
    # Numerical constraints
    MIN_RATE = 1e-10
    MAX_RATE = 1.0
    MIN_TIME = 1e-6
    MAX_TIME = 100.0
    
    # Simulation defaults
    DEFAULT_NUM_PATHS = 1000
    
    # Validation tolerances
    VALIDATION_TOLERANCE = 0.05
    FELLER_WARNING_THRESHOLD = 0.9


# ===============================================
# Custom Exceptions
# ===============================================

class CIRError(Exception):
    """Base exception for CIR model errors."""
    pass


class CIRParameterError(CIRError):
    """Exception for invalid CIR model parameters."""
    pass


class CIRSimulationError(CIRError):
    """Exception for simulation-related errors."""
    pass


class CIRValidationError(CIRError):
    """Exception for validation failures."""
    pass


class CIRNumericalError(CIRError):
    """Exception for numerical computation errors."""
    pass


# ===============================================
# Parameter Classes
# ===============================================

@dataclass(frozen=True)
class CIRParameters:
    """Immutable container for CIR model parameters."""
    r0: float
    theta: float
    kappa: float
    sigma: float
    maturity_time: float
    
    def __post_init__(self):
        """Validate parameters after initialization."""
        self._validate_parameters()
    
    def _validate_parameters(self) -> None:
        """Validate all CIR parameters."""
        if not (CIRConfig.MIN_RATE < self.r0 < CIRConfig.MAX_RATE):
            raise CIRParameterError(
                f"Initial rate r0={self.r0} must be in "
                f"({CIRConfig.MIN_RATE}, {CIRConfig.MAX_RATE})"
            )
        
        if not (CIRConfig.MIN_RATE < self.theta < CIRConfig.MAX_RATE):
            raise CIRParameterError(
                f"Long-term mean theta={self.theta} must be in "
                f"({CIRConfig.MIN_RATE}, {CIRConfig.MAX_RATE})"
            )
        
        if self.kappa <= 0:
            raise CIRParameterError(
                f"Mean reversion speed kappa={self.kappa} must be positive"
            )
        
        if self.sigma <= 0:
            raise CIRParameterError(
                f"Volatility sigma={self.sigma} must be positive"
            )
        
        if not (CIRConfig.MIN_TIME < self.maturity_time < CIRConfig.MAX_TIME):
            raise CIRParameterError(
                f"Maturity time={self.maturity_time} must be in "
                f"({CIRConfig.MIN_TIME}, {CIRConfig.MAX_TIME})"
            )
    
    @property
    def feller_parameter(self) -> float:
        """Calculate the Feller parameter: 2κθ/σ²."""
        return (2 * self.kappa * self.theta) / (self.sigma ** 2)
    
    @property
    def satisfies_feller_condition(self) -> bool:
        """Check if parameters satisfy the Feller condition."""
        return self.feller_parameter >= 1.0
    
    def check_feller_condition(self, strict: bool = True) -> None:
        """Check Feller condition and raise warnings/errors."""
        if not self.satisfies_feller_condition:
            if strict and self.feller_parameter < CIRConfig.FELLER_WARNING_THRESHOLD:
                raise CIRParameterError(
                    f"Feller condition strongly violated: "
                    f"2κθ/σ² = {self.feller_parameter:.3f} < 1. "
                    f"Consider adjusting parameters or use strict=False."
                )
            else:
                warnings.warn(
                    f"Feller condition violated: "
                    f"2κθ/σ² = {self.feller_parameter:.3f} < 1. "
                    f"Rates may occasionally reach zero.",
                    UserWarning
                )
    
    def to_dict(self) -> Dict[str, float]:
        """Convert parameters to dictionary."""
        return {
            'r0': self.r0,
            'theta': self.theta,
            'kappa': self.kappa,
            'sigma': self.sigma,
            'maturity_time': self.maturity_time,
            'feller_parameter': self.feller_parameter
        }


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
The CIR model parameters are $r_0 = 0.04$, $\theta = 0.06$, $\kappa = 0.3$, and $\sigma = 0.08$. Compute the Feller parameter and determine whether the Feller condition is satisfied.

??? success "Solution to Exercise 1"
    The Feller parameter is defined as

    $$
    \frac{2\kappa\theta}{\sigma^2}.
    $$

    Substituting the given values:

    $$
    \frac{2 \times 0.3 \times 0.06}{0.08^2} = \frac{0.036}{0.0064} = 5.625.
    $$

    Since $5.625 \geq 1$, the Feller condition $2\kappa\theta \geq \sigma^2$ is satisfied. This means the short rate process will remain strictly positive almost surely.

---

**Exercise 2.**
Explain the role of each parameter in the `CIRParameters` dataclass: $r_0$, $\theta$, $\kappa$, $\sigma$, and `maturity_time`. How does each affect the behavior of the CIR process?

??? success "Solution to Exercise 2"

    - $r_0$: The initial short rate at time $t = 0$. It sets the starting point for all simulated paths.
    - $\theta$: The long-term mean level. As $t \to \infty$, the expected value of the short rate converges to $\theta$.
    - $\kappa$: The mean reversion speed. A larger $\kappa$ pulls the rate back toward $\theta$ more quickly, reducing path dispersion.
    - $\sigma$: The volatility parameter. It scales the diffusion term $\sigma \sqrt{r}\,dW$, controlling the magnitude of random fluctuations. Unlike Vasicek, volatility in CIR depends on $\sqrt{r}$, which prevents negative rates when the Feller condition holds.
    - `maturity_time`: The time horizon $T$ for the simulation. It determines how far into the future the model is evaluated.

---

**Exercise 3.**
Suppose $\kappa = 0.2$, $\theta = 0.05$, and we want the Feller condition to hold. What is the maximum allowable volatility $\sigma$?

??? success "Solution to Exercise 3"
    The Feller condition requires

    $$
    2\kappa\theta \geq \sigma^2.
    $$

    Substituting:

    $$
    2 \times 0.2 \times 0.05 = 0.02 \geq \sigma^2.
    $$

    Therefore the maximum allowable volatility is

    $$
    \sigma_{\max} = \sqrt{0.02} = \sqrt{2/100} = \frac{\sqrt{2}}{10} \approx 0.1414.
    $$

---

**Exercise 4.**
The `CIRConfig` class sets `MIN_RATE = 1e-10` and `MAX_RATE = 1.0` for both $r_0$ and $\theta$. Explain why these bounds are appropriate for an interest rate model, and describe a scenario where the `FELLER_WARNING_THRESHOLD = 0.9` would trigger a warning but not an error.

??? success "Solution to Exercise 4"
    Interest rates are typically positive and small (a few percent), so requiring $r_0, \theta \in (10^{-10}, 1.0)$ ensures values are positive (consistent with the CIR model's non-negativity property) while excluding unrealistically large rates above 100%.

    The `FELLER_WARNING_THRESHOLD = 0.9` triggers a warning (but not an error in strict mode) when the Feller parameter lies in $[0.9, 1.0)$. For example, with $\kappa = 0.2$, $\theta = 0.04$, and $\sigma = 0.13$:

    $$
    \frac{2 \times 0.2 \times 0.04}{0.13^2} = \frac{0.016}{0.0169} \approx 0.947.
    $$

    Since $0.9 \leq 0.947 < 1.0$, the Feller condition is technically violated, but only mildly. The code issues a `UserWarning` rather than raising `CIRParameterError`, because rates may only occasionally touch zero.
