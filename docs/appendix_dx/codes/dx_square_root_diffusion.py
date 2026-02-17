# ---
# title: "DX Framework — Square-Root Diffusion (CIR Model)"
# description: >
#   Generates Monte Carlo paths for the Cox-Ingersoll-Ross (1985) model:
#     dv = kappa (theta - v) dt + sigma sqrt(v) dW
#   using full-truncation Euler discretisation (ensures non-negativity):
#     v_{t+1} = max(0, v_t + kappa (theta - v_t^+) dt + sigma sqrt(v_t^+) sqrt(dt) Z)
#
#   The CIR process is widely used for interest rates (short-rate models)
#   and variance processes (Heston model).
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import numpy as np

from dx_sn_random_numbers import sn_random_numbers
from dx_simulation_class import SimulationClass


class SquareRootDiffusion(SimulationClass):
    """Simulate CIR / square-root diffusion paths.

    Additional MarketEnvironment constants required:
        ``kappa`` – mean-reversion speed,
        ``theta`` – long-run level.
    """

    def __init__(self, name, mar_env, corr=False):
        super().__init__(name, mar_env, corr)
        self.kappa = mar_env.get_constant('kappa')
        self.theta = mar_env.get_constant('theta')

    def update(self, initial_value=None, volatility=None,
               kappa=None, theta=None, final_date=None):
        if initial_value is not None:
            self.initial_value = initial_value
        if volatility is not None:
            self.volatility = volatility
        if kappa is not None:
            self.kappa = kappa
        if theta is not None:
            self.theta = theta
        if final_date is not None:
            self.final_date = final_date
        self.instrument_values = None

    def generate_paths(self, fixed_seed=True, day_count=365.0):
        """Generate CIR paths with full-truncation Euler scheme."""
        if self.time_grid is None:
            self.generate_time_grid()

        M = len(self.time_grid)
        I = self.paths

        paths = np.zeros((M, I))
        paths_ = np.zeros_like(paths)  # pre-truncation values
        paths[0] = self.initial_value
        paths_[0] = self.initial_value

        if not self.correlated:
            rand = sn_random_numbers((1, M, I), fixed_seed=fixed_seed)
        else:
            rand = self.random_numbers

        for t in range(1, M):
            dt = (self.time_grid[t] - self.time_grid[t - 1]).days / day_count
            if not self.correlated:
                ran = rand[t]
            else:
                ran = np.dot(self.cholesky_matrix, rand[:, t, :])
                ran = ran[self.rn_set]

            # Full truncation: apply max(0, ·) inside drift and diffusion
            paths_[t] = (
                paths_[t - 1]
                + self.kappa * (self.theta - np.maximum(0, paths_[t - 1])) * dt
                + np.sqrt(np.maximum(0, paths_[t - 1]))
                  * self.volatility * np.sqrt(dt) * ran
            )
            paths[t] = np.maximum(0, paths_[t])

        self.instrument_values = paths
