# ---
# title: "DX Framework — European Option Valuation (Monte Carlo)"
# description: >
#   Values European-style derivatives by Monte Carlo simulation.
#   The payoff is evaluated at maturity and discounted.  Because the
#   payoff function is specified as a Python string, this class can
#   handle vanilla calls/puts, digitals, Asian (mean-based), and
#   lookback (max/min-based) options without modification.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import numpy as np

from dx_valuation_class import ValuationClass


class ValuationMCSEuropean(ValuationClass):
    """Monte Carlo valuation of European-exercise derivatives.

    Methods
    -------
    generate_payoff(fixed_seed)
        Evaluate the payoff function across all simulated paths.
    present_value(accuracy, fixed_seed, full)
        Discounted Monte Carlo estimator.
    """

    def generate_payoff(self, fixed_seed=False):
        """Compute per-path payoff at maturity.

        The following variables are available inside ``self.payoff_func``:
        ``maturity_value``, ``mean_value``, ``max_value``, ``min_value``,
        ``strike``.
        """
        try:
            strike = self.strike  # noqa: F841  (used in eval)
        except AttributeError:
            pass

        paths = self.underlying.get_instrument_values(fixed_seed=fixed_seed)
        time_grid = self.underlying.time_grid

        try:
            time_index = int(np.where(time_grid == self.maturity)[0])
        except TypeError:
            print('Maturity date not in time grid of underlying.')
            return None

        maturity_value = paths[time_index]                  # noqa: F841
        mean_value = np.mean(paths[:time_index], axis=0)    # noqa: F841
        max_value = np.max(paths[:time_index], axis=0)      # noqa: F841
        min_value = np.min(paths[:time_index], axis=0)      # noqa: F841

        try:
            payoff = eval(self.payoff_func)
            return payoff
        except Exception as e:
            print(f'Error evaluating payoff function: {e}')
            return None

    def present_value(self, accuracy=6, fixed_seed=False, full=False):
        """Discounted expected payoff (Monte Carlo estimator).

        Parameters
        ----------
        accuracy : int
            Decimal places in the returned result.
        fixed_seed : bool
            Use deterministic seed for reproducibility.
        full : bool
            If True, also return the full array of per-path present values.
        """
        cash_flow = self.generate_payoff(fixed_seed=fixed_seed)
        discount_factor = self.discount_curve.get_discount_factors(
            (self.pricing_date, self.maturity))[0, 1]

        result = discount_factor * np.sum(cash_flow) / len(cash_flow)

        if full:
            return round(result, accuracy), discount_factor * cash_flow
        return round(result, accuracy)
