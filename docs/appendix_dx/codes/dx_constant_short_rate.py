# ---
# title: "DX Framework — Constant Short Rate Discounting"
# description: >
#   Implements continuous discounting with a flat (constant) short rate:
#     D(t, T) = exp(-r * (T - t))
#   This is the simplest discount-curve object accepted by the DX
#   simulation and valuation classes.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import numpy as np


def _get_year_deltas(date_list, day_count=365.0):
    """Inline year-fraction helper (see dx_get_year_deltas.py)."""
    start = min(date_list)
    return np.array([(d - start).days / day_count for d in date_list])


class ConstantShortRate:
    """Flat discount curve for continuous compounding.

    Parameters
    ----------
    name : str
        Identifier (e.g. ``'risk_free'``).
    short_rate : float
        Annualised continuously-compounded rate.

    Methods
    -------
    get_discount_factors(date_list, dtobjects=True)
        Returns an (N x 2) array of ``[date, discount_factor]`` pairs.

    Examples
    --------
    >>> import datetime as dt
    >>> csr = ConstantShortRate('rf', 0.05)
    >>> dates = [dt.datetime(2024,1,1), dt.datetime(2025,1,1)]
    >>> csr.get_discount_factors(dates)
    """

    def __init__(self, name: str, short_rate: float):
        self.name = name
        self.short_rate = short_rate
        if short_rate < 0:
            raise ValueError(
                "Short rate is negative. While negative rates exist in "
                "practice, this simple model does not support them."
            )

    def get_discount_factors(self, date_list, dtobjects: bool = True):
        """Compute discount factors for a list of dates or year fractions.

        Parameters
        ----------
        date_list : list
            Datetime objects (if *dtobjects=True*) or numeric year fractions.
        dtobjects : bool
            If True, convert datetimes to year fractions first.

        Returns
        -------
        numpy.ndarray  (N x 2)
            Column 0 = dates/fractions, column 1 = discount factors.
        """
        if dtobjects:
            dlist = _get_year_deltas(date_list)
        else:
            dlist = np.array(date_list)
        dflist = np.exp(-self.short_rate * dlist)
        return np.array((date_list, dflist)).T
