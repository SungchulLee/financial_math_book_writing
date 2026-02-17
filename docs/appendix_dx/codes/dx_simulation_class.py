# ---
# title: "DX Framework — Simulation Base Class"
# description: >
#   Abstract base class that every DX simulation model inherits from.
#   It handles:
#     - extraction of parameters from a MarketEnvironment
#     - construction of the time grid (including special dates)
#     - management of correlated random numbers (Cholesky approach)
#
#   Concrete subclasses (GBM, CIR, Merton) override `generate_paths()`.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import numpy as np
import pandas as pd


class SimulationClass:
    """Base class providing common infrastructure for Monte Carlo models.

    Parameters
    ----------
    name : str
        Name of the underlying / risk factor.
    mar_env : MarketEnvironment
        Must contain at least: ``initial_value``, ``volatility``,
        ``final_date``, ``currency``, ``frequency``, ``paths``,
        and a discount curve keyed as ``'discount_curve'``.
    corr : bool
        True when the object participates in a correlated portfolio.
    """

    def __init__(self, name, mar_env, corr):
        self.name = name
        self.pricing_date = mar_env.pricing_date
        self.initial_value = mar_env.get_constant('initial_value')
        self.volatility = mar_env.get_constant('volatility')
        self.final_date = mar_env.get_constant('final_date')
        self.currency = mar_env.get_constant('currency')
        self.frequency = mar_env.get_constant('frequency')
        self.paths = mar_env.get_constant('paths')
        self.discount_curve = mar_env.get_curve('discount_curve')

        # optional: pre-built time grid (portfolio context)
        try:
            self.time_grid = mar_env.get_list('time_grid')
        except KeyError:
            self.time_grid = None

        # optional: special exercise / observation dates
        try:
            self.special_dates = mar_env.get_list('special_dates')
        except KeyError:
            self.special_dates = []

        self.instrument_values = None
        self.correlated = corr

        if corr:
            self.cholesky_matrix = mar_env.get_list('cholesky_matrix')
            self.rn_set = mar_env.get_list('rn_set')[self.name]
            self.random_numbers = mar_env.get_list('random_numbers')

    # ── time grid construction ──────────────────────────────────
    def generate_time_grid(self):
        """Build the simulation time grid from pricing_date to final_date."""
        start = self.pricing_date
        end = self.final_date
        time_grid = pd.date_range(start=start, end=end,
                                  freq=self.frequency).to_pydatetime()
        time_grid = list(time_grid)

        if start not in time_grid:
            time_grid.insert(0, start)
        if end not in time_grid:
            time_grid.append(end)
        if self.special_dates:
            time_grid.extend(self.special_dates)
            time_grid = sorted(set(time_grid))

        self.time_grid = np.array(time_grid)

    # ── lazy path generation ────────────────────────────────────
    def get_instrument_values(self, fixed_seed=True):
        """Return simulated paths, generating them on first call."""
        if self.instrument_values is None:
            self.generate_paths(fixed_seed=fixed_seed, day_count=365.0)
        elif not fixed_seed:
            self.generate_paths(fixed_seed=fixed_seed, day_count=365.0)
        return self.instrument_values

    def generate_paths(self, fixed_seed=False, day_count=365.0):
        """Override in subclass."""
        raise NotImplementedError("Subclasses must implement generate_paths().")
