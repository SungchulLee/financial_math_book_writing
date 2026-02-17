# ---
# title: "DX Framework — American Option Valuation (LSM Monte Carlo)"
# description: >
#   Values American-style derivatives using the Longstaff-Schwartz (2001)
#   Least-Squares Monte Carlo algorithm:
#     1. Simulate paths forward.
#     2. Walk backwards from maturity: at each exercise date, regress
#        continuation values on current asset prices.
#     3. Exercise when the immediate payoff exceeds the estimated
#        continuation value.
#
#   The regression uses polynomial basis functions of configurable degree.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import numpy as np

from dx_valuation_class import ValuationClass


class ValuationMCSAmerican(ValuationClass):
    """Monte Carlo valuation of American-exercise derivatives (LSM).

    Methods
    -------
    generate_payoff(fixed_seed)
        Returns instrument values, inner (exercise) values, and time indices.
    present_value(accuracy, fixed_seed, bf, full)
        LSM estimator of the American option value.
    """

    def generate_payoff(self, fixed_seed=False):
        try:
            strike = self.strike  # noqa: F841
        except AttributeError:
            pass

        paths = self.underlying.get_instrument_values(fixed_seed=fixed_seed)
        time_grid = self.underlying.time_grid

        time_index_start = int(np.where(time_grid == self.pricing_date)[0])
        time_index_end = int(np.where(time_grid == self.maturity)[0])

        instrument_values = paths[time_index_start:time_index_end + 1]
        payoff = eval(self.payoff_func)
        return instrument_values, payoff, time_index_start, time_index_end

    def present_value(self, accuracy=6, fixed_seed=False, bf=5, full=False):
        """Longstaff-Schwartz LSM estimator.

        Parameters
        ----------
        accuracy : int
            Decimal places.
        fixed_seed : bool
            Fix random seed for reproducibility.
        bf : int
            Number of polynomial basis functions for the regression.
        full : bool
            If True, also return the full per-path value array.
        """
        instrument_values, inner_values, ti_start, ti_end = \
            self.generate_payoff(fixed_seed=fixed_seed)

        time_list = self.underlying.time_grid[ti_start:ti_end + 1]
        discount_factors = self.discount_curve.get_discount_factors(
            time_list, dtobjects=True)

        # Start from terminal payoff
        V = inner_values[-1]

        # Backward induction
        for t in range(len(time_list) - 2, 0, -1):
            df = discount_factors[t, 1] / discount_factors[t + 1, 1]

            # Regression: continuation value ≈ polynomial(S_t)
            rg = np.polyfit(instrument_values[t], V * df, bf)
            C = np.polyval(rg, instrument_values[t])

            # Exercise decision: exercise if inner value > continuation
            V = np.where(inner_values[t] > C, inner_values[t], V * df)

        # Discount from first exercise date to pricing date
        df = discount_factors[0, 1] / discount_factors[1, 1]
        result = df * np.sum(V) / len(V)

        if full:
            return round(result, accuracy), df * V
        return round(result, accuracy)
