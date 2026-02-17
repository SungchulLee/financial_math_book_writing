# ---
# title: "DX Framework — Year-Fraction Utility"
# description: >
#   Converts a list of datetime objects into an array of year fractions
#   relative to the earliest date.  This is the fundamental date-handling
#   utility used across the DX framework for discounting and simulation.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import numpy as np


def get_year_deltas(date_list, day_count: float = 365.0):
    """Convert datetime objects to year fractions (normalised to zero at start).

    Parameters
    ----------
    date_list : list[datetime]
        Collection of datetime objects.
    day_count : float
        Days per year (365 = actual/365; 360 = 30/360 convention).

    Returns
    -------
    numpy.ndarray
        Year fractions with the first element equal to 0.0.

    Examples
    --------
    >>> import datetime as dt
    >>> dates = [dt.datetime(2024,1,1), dt.datetime(2024,7,1), dt.datetime(2025,1,1)]
    >>> deltas = get_year_deltas(dates)
    >>> print(deltas)  # [0.  0.49589...  1.00274...]
    """
    start = min(date_list)
    delta_list = [(date - start).days / day_count for date in date_list]
    return np.array(delta_list)
