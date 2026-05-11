# Vasicek Base

## Background

Vasicek Base

Educational script demonstrating vasicek base concepts.

---

## Code

```python
"""
Vasicek Base

Educational script demonstrating vasicek base concepts.
"""

# ============================================================================
# vasicek/vasicek_base.py
# ============================================================================
from dataclasses import dataclass
from enum import Enum
from typing import Dict


class VasicekScheme(Enum):
    """Vasicek discretization schemes."""
    EULER_MARUYAMA = "euler_maruyama"
    EXACT = "exact"  # Vasicek has exact simulation
    MILSTEIN = "milstein"  # Same as Euler for linear drift


class VasicekConfig:
    """Configuration class for Vasicek model settings."""
    
    # Default model parameters
    DEFAULT_R0 = 0.03
    DEFAULT_B = 0.05  # long-term mean (b)
    DEFAULT_A = 0.1   # mean reversion speed (a)
    DEFAULT_SIGMA = 0.03
    DEFAULT_MATURITY = 10.0
    
    # Numerical constraints
    MIN_RATE = -0.1  # Vasicek can go negative
    MAX_RATE = 1.0
    MIN_TIME = 1e-6
    MAX_TIME = 100.0
    
    # Simulation defaults
    DEFAULT_NUM_PATHS = 1000
    
    # Validation tolerances
    VALIDATION_TOLERANCE = 0.05


# ===============================================
# Custom Exceptions
# ===============================================

class VasicekError(Exception):
    """Base exception for Vasicek model errors."""
    pass


class VasicekParameterError(VasicekError):
    """Exception for invalid Vasicek model parameters."""
    pass


class VasicekSimulationError(VasicekError):
    """Exception for simulation-related errors."""
    pass


class VasicekValidationError(VasicekError):
    """Exception for validation failures."""
    pass


class VasicekNumericalError(VasicekError):
    """Exception for numerical computation errors."""
    pass


# ===============================================
# Parameter Classes
# ===============================================

@dataclass(frozen=True)
class VasicekParameters:
    """Immutable container for Vasicek model parameters."""
    r0: float      # Initial rate
    b: float       # Long-term mean (θ in some notation)
    a: float       # Mean reversion speed (κ in some notation)
    sigma: float   # Constant volatility
    maturity_time: float
    
    def __post_init__(self):
        """Validate parameters after initialization."""
        self._validate_parameters()
    
    def _validate_parameters(self) -> None:
        """Validate all Vasicek parameters."""
        if not (VasicekConfig.MIN_RATE < self.r0 < VasicekConfig.MAX_RATE):
            raise VasicekParameterError(
                f"Initial rate r0={self.r0} must be in "
                f"({VasicekConfig.MIN_RATE}, {VasicekConfig.MAX_RATE})"
            )
        
        if not (VasicekConfig.MIN_RATE < self.b < VasicekConfig.MAX_RATE):
            raise VasicekParameterError(
                f"Long-term mean b={self.b} must be in "
                f"({VasicekConfig.MIN_RATE}, {VasicekConfig.MAX_RATE})"
            )
        
        if self.a <= 0:
            raise VasicekParameterError(
                f"Mean reversion speed a={self.a} must be positive"
            )
        
        if self.sigma <= 0:
            raise VasicekParameterError(
                f"Volatility sigma={self.sigma} must be positive"
            )
        
        if not (VasicekConfig.MIN_TIME < self.maturity_time < VasicekConfig.MAX_TIME):
            raise VasicekParameterError(
                f"Maturity time={self.maturity_time} must be in "
                f"({VasicekConfig.MIN_TIME}, {VasicekConfig.MAX_TIME})"
            )
    
    def to_dict(self) -> Dict[str, float]:
        """Convert parameters to dictionary."""
        return {
            'r0': self.r0,
            'b': self.b,
            'a': self.a,
            'sigma': self.sigma,
            'maturity_time': self.maturity_time
        }


if __name__ == "__main__":
    pass
```

## Exercises

**Exercise 1.**
The Vasicek SDE is $dr = a(b - r)\,dt + \sigma\,dW$. Explain why the `MIN_RATE` in `VasicekConfig` is $-0.1$ rather than a small positive number as in the CIR model.

??? success "Solution to Exercise 1"
    Unlike the CIR model where the diffusion coefficient $\sigma\sqrt{r}$ vanishes at $r = 0$ (preventing negative rates under the Feller condition), the Vasicek model has constant diffusion $\sigma$. Since $r(t)$ is normally distributed, it can take any real value, including negative ones. Setting `MIN_RATE = -0.1` allows the model to accommodate negative rates down to $-10\%$, which reflects realistic scenarios observed in markets (e.g., the negative interest rate policies adopted by the ECB and BOJ). The CIR model uses `MIN_RATE = 1e-10` because its theoretical process is always non-negative.

---

**Exercise 2.**
Create a `VasicekParameters` instance with $r_0 = 0.02$, $b = 0.04$, $a = 0.15$, $\sigma = 0.01$, and `maturity_time = 20.0`. Convert it to a dictionary and verify all fields.

??? success "Solution to Exercise 2"
    ```python
    params = VasicekParameters(r0=0.02, b=0.04, a=0.15, sigma=0.01, maturity_time=20.0)
    d = params.to_dict()
    ```

    The dictionary is `{'r0': 0.02, 'b': 0.04, 'a': 0.15, 'sigma': 0.01, 'maturity_time': 20.0}`. All parameters pass validation: $r_0 = 0.02 \in (-0.1, 1.0)$, $b = 0.04 \in (-0.1, 1.0)$, $a = 0.15 > 0$, $\sigma = 0.01 > 0$, and `maturity_time` $= 20.0 \in (10^{-6}, 100)$.

---

**Exercise 3.**
What exception is raised if you try to create `VasicekParameters(r0=0.03, b=0.05, a=-0.1, sigma=0.02, maturity_time=10.0)`? Explain why this constraint exists.

??? success "Solution to Exercise 3"
    A `VasicekParameterError` is raised with the message "Mean reversion speed a=-0.1 must be positive." The mean reversion speed $a$ must be positive to ensure that the process $r(t)$ reverts toward the long-term mean $b$. If $a \leq 0$, the drift term $a(b - r)$ would push the rate away from $b$ (or provide no reversion), causing the process to be non-stationary and potentially diverge.

---

**Exercise 4.**
Compare the `VasicekParameters` dataclass to `CIRParameters`. List two key structural differences and explain how they reflect the mathematical differences between the models.

??? success "Solution to Exercise 4"

    1. **No Feller condition**: `CIRParameters` includes a `feller_parameter` property and `check_feller_condition` method, which are absent in `VasicekParameters`. This is because the CIR diffusion $\sigma\sqrt{r}$ requires $2\kappa\theta \geq \sigma^2$ to prevent the rate from reaching zero, while Vasicek's constant diffusion $\sigma$ has no analogous constraint.

    2. **Negative rate bounds**: `VasicekConfig.MIN_RATE = -0.1` allows negative initial rates and long-term means, while `CIRConfig.MIN_RATE = 1e-10` enforces strict positivity. This reflects the fact that the Vasicek process is Gaussian (taking values in $(-\infty, +\infty)$) while the CIR process is supported on $[0, +\infty)$.
