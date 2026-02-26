# ============================================================================
# black_scholes/black_scholes_numerical.py
# ============================================================================
import numpy as np
from .black_scholes_base import BlackScholesBase
from .black_scholes_schemes import explicit_scheme, implicit_scheme, cn_scheme, explicit_log_scheme, implicit_log_scheme, cn_log_scheme

class BlackScholesNumericalSolver(BlackScholesBase):
    def solve(self, method="explicit", option_type="put", **kwargs):
        if method == "explicit":
            return self.explicit(option_type=option_type, **kwargs)
        elif method == "implicit":
            return self.implicit(option_type=option_type, **kwargs)
        elif method == "cn":
            return self.cn(option_type=option_type, **kwargs)
        elif method == "explicit_log":
            return self.explicit_log(option_type=option_type, **kwargs)
        elif method == "implicit_log":
            return self.implicit_log(option_type=option_type, **kwargs)
        elif method == "cn_log":
            return self.cn_log(option_type=option_type, **kwargs)
        else:
            raise ValueError(f"Unknown method: {method}. Choose from 'explicit', 'implicit', 'cn', 'explicit_log', 'implicit_log', 'cn_log'.")
        
    def _payoff(self, S, option_type):
        """Calculate option payoff at expiration."""
        if option_type == 'put':
            return np.maximum(self.K - S, 0)
        elif option_type == 'call':
            return np.maximum(S - self.K, 0)
        else:
            raise ValueError("option_type must be 'put' or 'call'")

    def _check_stability_explicit(self, Smax, dS, dt):
        """Check stability condition for explicit finite difference scheme in original stock space."""
        coeff = (self.sigma**2 * Smax**2 * dt) / (dS**2)
        if coeff > 1:
            raise ValueError(f"⚠️ Unstable explicit scheme: sigma² * Smax² * dt / dS² = {coeff:.4f} > 1. "
                            "Reduce dt or increase dS.")

    def explicit(self, option_type='put', Smin=0, Smax=200, NS=100, NT=None, early_exercise=False):
        dS = (Smax - Smin) / (NS - 1)
        if NT is None:
            dt_stable = (dS ** 2) / (self.sigma ** 2 * Smax ** 2)
            NT = int(np.ceil(self.T / (0.5 * dt_stable)))
        if NT < 2:
            raise ValueError("NT must be at least 2 for time-stepping.")
        dt = self.T / (NT - 1)

        self._check_stability_explicit(Smax, dS, dt)

        return explicit_scheme(self, option_type, Smin, Smax, NS, NT, early_exercise)

    def implicit(self, option_type='put', Smin=1e-3, Smax=500, NS=100, NT=100, early_exercise=False):
        return implicit_scheme(self, option_type, Smin, Smax, NS, NT, early_exercise)

    def cn(self, option_type='put', Smin=0, Smax=200, NS=100, NT=100, early_exercise=False):
        return cn_scheme(self, option_type, Smin, Smax, NS, NT, early_exercise)

    def _check_stability_explicit_log(self, dx, dt):
        """Check CFL stability condition for explicit finite difference scheme in log-price space."""
        coeff = self.sigma**2 * dt / dx**2
        if coeff > 1:
            raise ValueError(f"⚠️ Unstable scheme: sigma^2 * dt / dx^2 = {coeff:.4f} > 1. "
                            "Reduce dt or increase dx to satisfy stability condition.")

    def explicit_log(self, option_type='put', Smin=1e-3, Smax=500, NX=100, NT=None, early_exercise=False):
        xmin, xmax = np.log(Smin), np.log(Smax)
        dx = (xmax - xmin) / (NX - 1)

        if NT is None:
            dt_stable = dx**2 / self.sigma**2
            NT = int(np.ceil(self.T / (0.5 * dt_stable)))
        if NT < 2:
            raise ValueError("NT must be at least 2 for time stepping.")
        dt = self.T / (NT - 1)

        self._check_stability_explicit_log(dx, dt)
        return explicit_log_scheme(self, option_type, Smin, Smax, NX, NT, early_exercise)

    def implicit_log(self, option_type='put', Smin=1e-3, Smax=500, NX=100, NT=100, early_exercise=False):
        return implicit_log_scheme(self, option_type, Smin, Smax, NX, NT, early_exercise)

    def cn_log(self, option_type='put', Smin=1e-3, Smax=500, NX=100, NT=100, early_exercise=False):
        return cn_log_scheme(self, option_type, Smin, Smax, NX, NT, early_exercise)