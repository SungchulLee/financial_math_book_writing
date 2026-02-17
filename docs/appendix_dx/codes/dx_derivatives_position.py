# ---
# title: "DX Framework — Derivatives Position"
# description: >
#   A data class representing a single derivatives position within
#   a portfolio.  It bundles the position's metadata:
#     - quantity (number of contracts)
#     - underlying risk factor name
#     - market environment (parameters for valuation)
#     - option type (European / American)
#     - payoff function string
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---


class DerivativesPosition:
    """Container for a single derivatives position.

    Parameters
    ----------
    name : str
        Position identifier.
    quantity : float
        Number of contracts (positive = long, negative = short).
    underlying : str
        Name of the risk factor / underlying asset.
    mar_env : MarketEnvironment
        Parameters specific to this position (strike, maturity, …).
    otype : str
        ``'European'`` or ``'American'``.
    payoff_func : str
        Payoff expression (see ValuationClass documentation).
    """

    def __init__(self, name, quantity, underlying, mar_env,
                 otype, payoff_func):
        self.name = name
        self.quantity = quantity
        self.underlying = underlying
        self.mar_env = mar_env
        self.otype = otype
        self.payoff_func = payoff_func

    def get_info(self):
        """Print a human-readable summary of the position."""
        print(f"{'NAME':<20} {self.name}")
        print(f"{'QUANTITY':<20} {self.quantity}")
        print(f"{'UNDERLYING':<20} {self.underlying}")
        print(f"{'OPTION TYPE':<20} {self.otype}")
        print(f"{'PAYOFF':<20} {self.payoff_func}")
        print("MARKET ENVIRONMENT")
        for key, val in self.mar_env.constants.items():
            print(f"  {key}: {val}")

    def __repr__(self):
        return (f"DerivativesPosition('{self.name}', qty={self.quantity}, "
                f"otype='{self.otype}')")
