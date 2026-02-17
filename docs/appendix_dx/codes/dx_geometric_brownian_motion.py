# ---
# title: "DX Framework — Geometric Brownian Motion Simulation"
# description: >
#   Generates Monte Carlo paths for the Black-Scholes-Merton model:
#     dS = r S dt + sigma S dW   (under Q)
#   using log-Euler discretisation (exact for GBM):
#     S_{t+1} = S_t exp[(r - sigma^2/2) dt + sigma sqrt(dt) Z]
#
#   Supports both independent and correlated (Cholesky) random numbers
#   for multi-asset portfolio simulations.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import numpy as np

# Relative imports within the DX framework
from dx_sn_random_numbers import sn_random_numbers
from dx_simulation_class import SimulationClass


class GeometricBrownianMotion(SimulationClass):
    """Simulate GBM paths for use in Monte Carlo pricing.

    Inherits all attributes from ``SimulationClass``.
    """

    def __init__(self, name, mar_env, corr=False):
        super().__init__(name, mar_env, corr)

    def update(self, initial_value=None, volatility=None, final_date=None):
        """Update model parameters and invalidate cached paths."""
        if initial_value is not None:
            self.initial_value = initial_value
        if volatility is not None:
            self.volatility = volatility
        if final_date is not None:
            self.final_date = final_date
        self.instrument_values = None

    def generate_paths(self, fixed_seed=False, day_count=365.0):
        """Generate simulated GBM price paths.

        Parameters
        ----------
        fixed_seed : bool
            If True, fix the random seed for reproducibility.
        day_count : float
            Days per year for year-fraction computation.
        """
        if self.time_grid is None:
            self.generate_time_grid()

        M = len(self.time_grid)  # time steps
        I = self.paths            # number of paths

        paths = np.zeros((M, I))
        paths[0] = self.initial_value

        if not self.correlated:
            rand = sn_random_numbers((1, M, I), fixed_seed=fixed_seed)
        else:
            rand = self.random_numbers

        short_rate = self.discount_curve.short_rate

        for t in range(1, M):
            if not self.correlated:
                ran = rand[t]
            else:
                ran = np.dot(self.cholesky_matrix, rand[:, t, :])
                ran = ran[self.rn_set]

            dt = (self.time_grid[t] - self.time_grid[t - 1]).days / day_count

            # Log-Euler step (exact for GBM)
            paths[t] = paths[t - 1] * np.exp(
                (short_rate - 0.5 * self.volatility ** 2) * dt
                + self.volatility * np.sqrt(dt) * ran
            )

        self.instrument_values = paths
