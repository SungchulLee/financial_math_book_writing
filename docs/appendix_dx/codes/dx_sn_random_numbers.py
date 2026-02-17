# ---
# title: "DX Framework — Variance-Reduced Random Numbers"
# description: >
#   Generates standard-normal pseudo-random numbers with two
#   optional variance-reduction techniques:
#     1. Antithetic variates  — concatenate Z and −Z
#     2. Moment matching      — shift and scale so that
#        sample mean = 0 and sample std = 1
#
#   These techniques improve Monte Carlo convergence at negligible
#   computational cost and are used by all DX simulation classes.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import numpy as np


def sn_random_numbers(shape, antithetic: bool = True,
                      moment_matching: bool = True,
                      fixed_seed: bool = False):
    """Generate a (possibly variance-reduced) standard-normal random array.

    Parameters
    ----------
    shape : tuple (o, n, m)
        Desired output shape:
          o = number of risk factors,
          n = number of time steps,
          m = number of paths  (must be even if *antithetic=True*).
    antithetic : bool
        If True, generate half the paths and mirror them (−Z).
    moment_matching : bool
        If True, standardise the sample to exact mean 0 and std 1.
    fixed_seed : bool
        If True, fix the NumPy random seed (for reproducibility).

    Returns
    -------
    numpy.ndarray
        Array of shape ``(n, m)`` if *o == 1*, else ``(o, n, m)``.

    Examples
    --------
    >>> ran = sn_random_numbers((1, 50, 10000))
    >>> print(ran.shape)   # (50, 10000)
    >>> print(ran.mean())  # ≈ 0.0 (moment-matched)
    >>> print(ran.std())   # ≈ 1.0
    """
    if fixed_seed:
        np.random.seed(1000)

    if antithetic:
        ran = np.random.standard_normal((shape[0], shape[1], shape[2] // 2))
        ran = np.concatenate((ran, -ran), axis=2)
    else:
        ran = np.random.standard_normal(shape)

    if moment_matching:
        ran = ran - np.mean(ran)
        ran = ran / np.std(ran)

    # squeeze leading dimension when there is a single risk factor
    if shape[0] == 1:
        return ran[0]
    return ran
