# ---
# title: "DX Framework — Jump Diffusion (Merton 1976)"
# description: >
#   Generates Monte Carlo paths for the Merton jump-diffusion model:
#     dS/S = (r - r_J) dt + sigma dW + J dN
#   where N is a Poisson process with intensity lambda and
#   ln(1 + J) ~ N(mu, delta^2).
#
#   The drift is compensated so that the discounted price is a martingale:
#     r_J = lambda * (exp(mu + delta^2/2) - 1)
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import numpy as np

from dx_sn_random_numbers import sn_random_numbers
from dx_simulation_class import SimulationClass


class JumpDiffusion(SimulationClass):
    """Simulate Merton jump-diffusion paths.

    Additional MarketEnvironment constants required:
        ``lambda`` – jump intensity (per year),
        ``mu``     – mean of log-jump size,
        ``delta``  – std of log-jump size.
    """

    def __init__(self, name, mar_env, corr=False):
        super().__init__(name, mar_env, corr)
        self.lamb = mar_env.get_constant('lambda')
        self.mu = mar_env.get_constant('mu')
        self.delt = mar_env.get_constant('delta')

    def update(self, initial_value=None, volatility=None,
               lamb=None, mu=None, delta=None, final_date=None):
        if initial_value is not None:
            self.initial_value = initial_value
        if volatility is not None:
            self.volatility = volatility
        if lamb is not None:
            self.lamb = lamb
        if mu is not None:
            self.mu = mu
        if delta is not None:
            self.delt = delta
        if final_date is not None:
            self.final_date = final_date
        self.instrument_values = None

    def generate_paths(self, fixed_seed=False, day_count=365.0):
        """Generate Merton jump-diffusion paths."""
        if self.time_grid is None:
            self.generate_time_grid()

        M = len(self.time_grid)
        I = self.paths
        paths = np.zeros((M, I))
        paths[0] = self.initial_value

        # Diffusion component random numbers
        if not self.correlated:
            sn1 = sn_random_numbers((1, M, I), fixed_seed=fixed_seed)
        else:
            sn1 = self.random_numbers

        # Independent random numbers for the jump component
        sn2 = sn_random_numbers((1, M, I), fixed_seed=fixed_seed)

        # Drift compensation for the jump component
        rj = self.lamb * (np.exp(self.mu + 0.5 * self.delt ** 2) - 1)

        short_rate = self.discount_curve.short_rate

        for t in range(1, M):
            if not self.correlated:
                ran = sn1[t]
            else:
                ran = np.dot(self.cholesky_matrix, sn1[:, t, :])
                ran = ran[self.rn_set]

            dt = (self.time_grid[t] - self.time_grid[t - 1]).days / day_count

            # Number of jumps in [t-1, t] ~ Poisson(lambda * dt)
            poi = np.random.poisson(self.lamb * dt, I)

            # Combine diffusion and jump
            paths[t] = paths[t - 1] * (
                np.exp((short_rate - rj - 0.5 * self.volatility ** 2) * dt
                       + self.volatility * np.sqrt(dt) * ran)
                + (np.exp(self.mu + self.delt * sn2[t]) - 1) * poi
            )

        self.instrument_values = paths
