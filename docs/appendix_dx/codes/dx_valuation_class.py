# ---
# title: "DX Framework — Valuation Base Class"
# description: >
#   Base class for single-factor derivatives valuation via Monte Carlo.
#   Provides:
#     - payoff function specification (as a Python expression string)
#     - numerical Delta (forward-difference on S0)
#     - numerical Vega  (forward-difference on sigma)
#
#   Subclasses implement `present_value()` for European or American exercise.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---


class ValuationClass:
    """Base class for Monte Carlo derivative valuation.

    Parameters
    ----------
    name : str
        Name of the derivative.
    underlying : SimulationClass
        Object modelling the single risk factor.
    mar_env : MarketEnvironment
        Must contain ``maturity`` and ``currency``; ``strike`` is optional.
    payoff_func : str
        Python expression for the payoff.  Available variables:
        ``maturity_value``, ``mean_value``, ``max_value``, ``min_value``,
        ``instrument_values``, ``strike``.
        Example: ``'np.maximum(maturity_value - strike, 0)'``
    """

    def __init__(self, name, underlying, mar_env, payoff_func=''):
        self.name = name
        self.pricing_date = mar_env.pricing_date
        try:
            self.strike = mar_env.get_constant('strike')
        except KeyError:
            pass
        self.maturity = mar_env.get_constant('maturity')
        self.currency = mar_env.get_constant('currency')
        self.frequency = underlying.frequency
        self.paths = underlying.paths
        self.discount_curve = underlying.discount_curve
        self.payoff_func = payoff_func
        self.underlying = underlying
        self.underlying.special_dates.extend([self.pricing_date, self.maturity])

    def update(self, initial_value=None, volatility=None,
               strike=None, maturity=None):
        """Update parameters and invalidate cached paths when necessary."""
        if initial_value is not None:
            self.underlying.update(initial_value=initial_value)
        if volatility is not None:
            self.underlying.update(volatility=volatility)
        if strike is not None:
            self.strike = strike
        if maturity is not None:
            self.maturity = maturity
            if maturity not in self.underlying.time_grid:
                self.underlying.special_dates.append(maturity)
                self.underlying.instrument_values = None

    # ── Numerical Greeks ────────────────────────────────────────
    def delta(self, interval=None, accuracy=4):
        """Numerical Delta via forward-difference on initial value."""
        if interval is None:
            interval = self.underlying.initial_value / 50.0

        value_left = self.present_value(fixed_seed=True)
        initial_del = self.underlying.initial_value + interval
        self.underlying.update(initial_value=initial_del)
        value_right = self.present_value(fixed_seed=True)
        self.underlying.update(initial_value=initial_del - interval)

        delta = (value_right - value_left) / interval
        return round(max(-1.0, min(1.0, delta)), accuracy)

    def vega(self, interval=0.01, accuracy=4):
        """Numerical Vega via forward-difference on volatility."""
        if interval < self.underlying.volatility / 50.0:
            interval = self.underlying.volatility / 50.0

        value_left = self.present_value(fixed_seed=True)
        vola_del = self.underlying.volatility + interval
        self.underlying.update(volatility=vola_del)
        value_right = self.present_value(fixed_seed=True)
        self.underlying.update(volatility=vola_del - interval)

        return round((value_right - value_left) / interval, accuracy)

    def present_value(self, accuracy=6, fixed_seed=False, full=False):
        raise NotImplementedError("Subclasses must implement present_value().")
