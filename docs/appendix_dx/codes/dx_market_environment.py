# ---
# title: "DX Framework — Market Environment"
# description: >
#   A lightweight container for market data used throughout the DX
#   derivatives analytics library.  It stores three categories of data:
#     - constants  (scalars: rates, vols, initial values …)
#     - lists      (arrays: time grids, special dates …)
#     - curves     (objects: discount curves, forward curves …)
#
#   Multiple environments can be merged with `add_environment()`,
#   which is essential when building portfolio-level valuations.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---


class MarketEnvironment:
    """Container for market data needed by simulation and valuation classes.

    Parameters
    ----------
    name : str
        Identifier for this environment (e.g. ``'market_2024'``).
    pricing_date : datetime
        Reference / valuation date.

    Examples
    --------
    >>> import datetime as dt
    >>> me = MarketEnvironment('demo', dt.datetime(2024, 1, 1))
    >>> me.add_constant('initial_value', 100.0)
    >>> me.add_constant('volatility', 0.20)
    >>> me.get_constant('volatility')
    0.2
    """

    def __init__(self, name: str, pricing_date):
        self.name = name
        self.pricing_date = pricing_date
        self.constants: dict = {}
        self.lists: dict = {}
        self.curves: dict = {}

    # ── constants ───────────────────────────────────────────────
    def add_constant(self, key: str, constant):
        self.constants[key] = constant

    def get_constant(self, key: str):
        return self.constants[key]

    # ── lists ───────────────────────────────────────────────────
    def add_list(self, key: str, list_object):
        self.lists[key] = list_object

    def get_list(self, key: str):
        return self.lists[key]

    # ── curves ──────────────────────────────────────────────────
    def add_curve(self, key: str, curve):
        self.curves[key] = curve

    def get_curve(self, key: str):
        return self.curves[key]

    # ── merge ───────────────────────────────────────────────────
    def add_environment(self, env: "MarketEnvironment"):
        """Merge another MarketEnvironment into this one (overwrites duplicates)."""
        self.constants.update(env.constants)
        self.lists.update(env.lists)
        self.curves.update(env.curves)

    def __repr__(self):
        return (f"MarketEnvironment('{self.name}', "
                f"constants={len(self.constants)}, "
                f"lists={len(self.lists)}, "
                f"curves={len(self.curves)})")
