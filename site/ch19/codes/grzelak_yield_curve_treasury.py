"""
Yield curve construction from treasury swap instruments.

Based on "Financial Engineering" course by L.A. Grzelak.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak
"""
import enum
import numpy as np
from copy import deepcopy
from scipy.interpolate import splrep, splev, interp1d


class OptionTypeSwap(enum.Enum):
    """Swap option type enumeration."""
    RECEIVER = 1.0
    PAYER = -1.0


def ir_swap(option_type, notional, strike, t, t_i, t_m, n, p0t):
    """
    Compute interest rate swap value.

    Parameters
    ----------
    option_type : OptionTypeSwap
        PAYER or RECEIVER
    notional : float
        Notional amount
    strike : float
        Strike rate
    t : float
        Current time
    t_i : float
        Swap start time
    t_m : float
        Swap end time
    n : int
        Number of payment dates
    p0t : callable
        Zero-coupon bond pricing function

    Returns
    -------
    float
        Swap value
    """
    ti_grid = np.linspace(t_i, t_m, int(n))
    tau = ti_grid[1] - ti_grid[0]

    # Overwrite t_i if t > t_i
    prev_ti = ti_grid[np.where(ti_grid < t)]
    if np.size(prev_ti) > 0:
        t_i = prev_ti[-1]

    # Handle case when some payments are already done
    ti_grid = ti_grid[np.where(ti_grid > t)]

    temp = 0.0
    for idx, ti in enumerate(ti_grid):
        if ti > t_i:
            temp = temp + tau * p0t(ti)

    p_t_ti = p0t(t_i)
    p_t_tm = p0t(t_m)

    if option_type == OptionTypeSwap.PAYER:
        swap = (p_t_ti - p_t_tm) - strike * temp
    elif option_type == OptionTypeSwap.RECEIVER:
        swap = strike * temp - (p_t_ti - p_t_tm)

    return swap * notional


def p0t_model(t, ti, ri, method):
    """
    Compute zero-coupon bond price using interpolation.

    Parameters
    ----------
    t : float or array
        Time point(s)
    ti : array
        Interpolation nodes (times)
    ri : array
        Interpolation values (rates)
    method : callable
        Interpolation method

    Returns
    -------
    float or array
        Bond price P(0,t)
    """
    r_interp = method(ti, ri)
    r = r_interp(t)
    return np.exp(-r * t)


def yield_curve(instruments, maturities, r0, method, tol):
    """
    Compute yield curve from instrument prices.

    Parameters
    ----------
    instruments : list of callable
        List of instrument pricing functions
    maturities : array
        Maturity points
    r0 : array
        Initial rate guess
    method : callable
        Interpolation method
    tol : float
        Convergence tolerance

    Returns
    -------
    array
        Optimal rates at maturities
    """
    r0 = deepcopy(r0)
    ri = multivariate_newton_raphson(r0, maturities, instruments, method,
                                     tol=tol)
    return ri


def multivariate_newton_raphson(ri, ti, instruments, method, tol):
    """
    Multi-dimensional Newton-Raphson solver.

    Parameters
    ----------
    ri : array
        Initial rate guess
    ti : array
        Time nodes
    instruments : list of callable
        Instrument pricing functions
    method : callable
        Interpolation method
    tol : float
        Convergence tolerance

    Returns
    -------
    array
        Converged rates
    """
    err = 10e10
    idx = 0
    while err > tol:
        idx = idx + 1
        values = evaluate_instruments(ti, ri, instruments, method)
        j = jacobian(ti, ri, instruments, method)
        j_inv = np.linalg.inv(j)
        err = -np.dot(j_inv, values)
        ri[0:] = ri[0:] + err
        err = np.linalg.norm(err)
        print('index in the loop is', idx, ' Error is ', err)
    return ri


def jacobian(ti, ri, instruments, method):
    """
    Compute Jacobian matrix for Newton-Raphson.

    Parameters
    ----------
    ti : array
        Time nodes
    ri : array
        Current rate estimate
    instruments : list of callable
        Instrument pricing functions
    method : callable
        Interpolation method

    Returns
    -------
    ndarray
        (n_instruments, n_instruments) Jacobian matrix
    """
    eps = 1e-05
    swap_num = len(ti)
    j = np.zeros((swap_num, swap_num))
    val = evaluate_instruments(ti, ri, instruments, method)
    ri_up = deepcopy(ri)

    for j_idx in range(0, len(ri)):
        ri_up[j_idx] = ri[j_idx] + eps
        val_up = evaluate_instruments(ti, ri_up, instruments, method)
        ri_up[j_idx] = ri[j_idx]
        dv = (val_up - val) / eps
        j[:, j_idx] = dv[:]
    return j


def evaluate_instruments(ti, ri, instruments, method):
    """
    Evaluate all instruments at given rates.

    Parameters
    ----------
    ti : array
        Time nodes
    ri : array
        Rates at nodes
    instruments : list of callable
        Instrument pricing functions
    method : callable
        Interpolation method

    Returns
    -------
    array
        Instrument values
    """
    p0t_temp = lambda t: p0t_model(t, ti, ri, method)
    val = np.zeros(len(instruments))
    for i in range(0, len(instruments)):
        val[i] = instruments[i](p0t_temp)
    return val


def linear_interpolation(ti, ri):
    """
    Linear interpolation function.

    Parameters
    ----------
    ti : array
        Interpolation nodes
    ri : array
        Interpolation values

    Returns
    -------
    callable
        Interpolation function
    """
    interpolator = lambda t: np.interp(t, ti, ri)
    return interpolator


def main():
    """Run yield curve construction."""
    # ============= Parameters =============
    tol = 1.0e-15
    r0 = np.array([0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01])
    method = linear_interpolation

    # Construct swaps for yield curve building
    k = np.array([0.04 / 100.0, 0.16 / 100.0, 0.31 / 100.0, 0.81 / 100.0,
                  1.28 / 100.0, 1.62 / 100.0, 2.22 / 100.0, 2.30 / 100.0])
    mat = np.array([1.0, 2.0, 3.0, 5.0, 7.0, 10.0, 20.0, 30.0])

    # ============= Build Instruments =============
    swap1 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[0], 0.0, 0.0,
                                 mat[0], 4 * mat[0], p0t)
    swap2 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[1], 0.0, 0.0,
                                 mat[1], 4 * mat[1], p0t)
    swap3 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[2], 0.0, 0.0,
                                 mat[2], 4 * mat[2], p0t)
    swap4 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[3], 0.0, 0.0,
                                 mat[3], 4 * mat[3], p0t)
    swap5 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[4], 0.0, 0.0,
                                 mat[4], 4 * mat[4], p0t)
    swap6 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[5], 0.0, 0.0,
                                 mat[5], 4 * mat[5], p0t)
    swap7 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[6], 0.0, 0.0,
                                 mat[6], 4 * mat[6], p0t)
    swap8 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[7], 0.0, 0.0,
                                 mat[7], 4 * mat[7], p0t)
    instruments = [swap1, swap2, swap3, swap4, swap5, swap6, swap7, swap8]

    # ============= Determine Optimal Spine Points =============
    ri = yield_curve(instruments, mat, r0, method, tol)
    print('\n Spine points are', ri, '\n')

    # ============= Build Zero-Coupon Bond Curves =============
    p0t_initial = lambda t: p0t_model(t, mat, r0, method)
    p0t = lambda t: p0t_model(t, mat, ri, method)

    # ============= Price Back the Swaps =============
    swaps_model = np.zeros(len(instruments))
    swaps_initial = np.zeros(len(instruments))
    for i in range(0, len(instruments)):
        swaps_initial[i] = instruments[i](p0t_initial)
        swaps_model[i] = instruments[i](p0t)

    print('Prices for Par Swaps (initial) = ', swaps_initial, '\n')
    print('Prices for Par Swaps = ', swaps_model, '\n')


if __name__ == "__main__":
    main()
