"""
Construction of multi-curve discount and forward curves from swap instruments.

Based on "Financial Engineering" course by L.A. Grzelak.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak
"""
import enum
import numpy as np
import matplotlib.pyplot as plt
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

    temp = 0.0
    for idx, ti in enumerate(ti_grid):
        if idx > 0:
            temp = temp + tau * p0t(ti)

    p_t_ti = p0t(t_i)
    p_t_tm = p0t(t_m)

    if option_type == OptionTypeSwap.PAYER:
        swap = (p_t_ti - p_t_tm) - strike * temp
    elif option_type == OptionTypeSwap.RECEIVER:
        swap = strike * temp - (p_t_ti - p_t_tm)

    return swap * notional


def ir_swap_multi_curve(option_type, notional, strike, t, t_i, t_m, n,
                        p0t, p0t_frd):
    """
    Compute interest rate swap value using multi-curve framework.

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
        Discount curve (zero-coupon bond pricing function)
    p0t_frd : callable
        Forward curve (zero-coupon bond pricing function)

    Returns
    -------
    float
        Swap value
    """
    ti_grid = np.linspace(t_i, t_m, int(n))
    tau = ti_grid[1] - ti_grid[0]

    swap = 0.0
    for idx, ti in enumerate(ti_grid):
        # L(t_0, t_{k-1}, t_k) from forward curve
        if idx > 0:
            l_frwd = (1.0 / tau * (p0t_frd(ti_grid[idx - 1]) -
                                   p0t_frd(ti_grid[idx])) /
                      p0t_frd(ti_grid[idx]))
            swap = swap + tau * p0t(ti_grid[idx]) * (l_frwd - strike)

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


def spline_interpolate(ti, ri):
    """
    Spline interpolation function.

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
    interpolator = splrep(ti, ri, s=0.01)
    interp = lambda t: splev(t, interpolator)
    return interp


def scipy_1d_interpolate(ti, ri):
    """
    Scipy 1D quadratic interpolation.

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
    interpolator = lambda t: interp1d(ti, ri, kind='quadratic')(t)
    return interpolator


def plot_curves(t, p0t_discount, p0t_frwd):
    """
    Plot discount and forward curves.

    Parameters
    ----------
    t : array
        Time points
    p0t_discount : callable
        Discount curve function
    p0t_frwd : callable
        Forward curve function
    """
    plt.figure()
    plt.plot(t, p0t_discount(t), '--r')
    plt.plot(t, p0t_frwd(t), '-b')
    plt.legend(['discount', 'forecast'])


def main():
    """Run multi-curve yield curve construction."""
    # ============= Parameters =============
    tol = 1.0e-15
    r0 = np.array([0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01])
    method = linear_interpolation

    # Discount curve instruments
    k = np.array([0.04 / 100.0, 0.16 / 100.0, 0.31 / 100.0, 0.81 / 100.0,
                  1.28 / 100.0, 1.62 / 100.0, 2.22 / 100.0, 2.30 / 100.0])
    mat = np.array([1.0, 2.0, 3.0, 5.0, 7.0, 10.0, 20.0, 30.0])

    # ============= Build Discount Curve =============
    swap1 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[0], 0.0, 0.0,
                                 mat[0], 4 * mat[0], p0t)
    swap2 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[1], 0.0, 0.0,
                                 mat[1], 5 * mat[1], p0t)
    swap3 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[2], 0.0, 0.0,
                                 mat[2], 6 * mat[2], p0t)
    swap4 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[3], 0.0, 0.0,
                                 mat[3], 7 * mat[3], p0t)
    swap5 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[4], 0.0, 0.0,
                                 mat[4], 8 * mat[4], p0t)
    swap6 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[5], 0.0, 0.0,
                                 mat[5], 9 * mat[5], p0t)
    swap7 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[6], 0.0, 0.0,
                                 mat[6], 10 * mat[6], p0t)
    swap8 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[7], 0.0, 0.0,
                                 mat[7], 11 * mat[7], p0t)
    instruments = [swap1, swap2, swap3, swap4, swap5, swap6, swap7, swap8]

    ri = yield_curve(instruments, mat, r0, method, tol)
    print('\n Spine points are', ri, '\n')

    p0t_initial = lambda t: p0t_model(t, mat, r0, method)
    p0t = lambda t: p0t_model(t, mat, ri, method)

    # Price back swaps
    swaps_model = np.zeros(len(instruments))
    swaps_initial = np.zeros(len(instruments))
    for i in range(0, len(instruments)):
        swaps_model[i] = instruments[i](p0t)
        swaps_initial[i] = instruments[i](p0t_initial)

    print('Prices for Par Swaps (initial) = ', swaps_initial, '\n')
    print('Prices for Par Swaps = ', swaps_model, '\n')

    # ============= Multi-curve Extension =============
    p0t_frd = deepcopy(p0t)
    k_test = 0.2
    swap1_test = lambda p0t_arg: ir_swap(OptionTypeSwap.PAYER, 1, k_test, 0.0,
                                          0.0, mat[0], 4 * mat[0], p0t_arg)
    swap1_mc = lambda p0t_arg: ir_swap_multi_curve(
        OptionTypeSwap.PAYER, 1, k_test, 0.0, 0.0, mat[0], 4 * mat[0],
        p0t_arg, p0t_frd)
    print('Sanity check: swap1 = {0}, swap2 = {1}'.format(
        swap1_test(p0t), swap1_mc(p0t)))

    # ============= Forward Curve Instruments =============
    r0_frwd = np.array([0.01, 0.01, 0.01, 0.01])
    k_frwd = np.array([0.09 / 100.0, 0.26 / 100.0, 0.37 / 100.0, 1.91 / 100.0])
    mat_frwd = np.array([1.0, 2.0, 3.0, 5.0])

    p0t_discount = lambda t: p0t_model(t, mat, ri, method)
    swap1_frwd = lambda p0t_frwd_arg: ir_swap_multi_curve(
        OptionTypeSwap.PAYER, 1, k_frwd[0], 0.0, 0.0, mat_frwd[0],
        4 * mat_frwd[0], p0t_discount, p0t_frwd_arg)
    swap2_frwd = lambda p0t_frwd_arg: ir_swap_multi_curve(
        OptionTypeSwap.PAYER, 1, k_frwd[1], 0.0, 0.0, mat_frwd[1],
        5 * mat_frwd[1], p0t_discount, p0t_frwd_arg)
    swap3_frwd = lambda p0t_frwd_arg: ir_swap_multi_curve(
        OptionTypeSwap.PAYER, 1, k_frwd[2], 0.0, 0.0, mat_frwd[2],
        6 * mat_frwd[2], p0t_discount, p0t_frwd_arg)
    swap4_frwd = lambda p0t_frwd_arg: ir_swap_multi_curve(
        OptionTypeSwap.PAYER, 1, k_frwd[3], 0.0, 0.0, mat_frwd[3],
        7 * mat_frwd[3], p0t_discount, p0t_frwd_arg)

    instruments_frwd = [swap1_frwd, swap2_frwd, swap3_frwd, swap4_frwd]

    # ============= Solve Forward Curve =============
    ri_frwd = yield_curve(instruments_frwd, mat_frwd, r0_frwd, method, tol)
    print('\n Frwd Spine points are', ri_frwd, '\n')

    p0t_frwd_initial = lambda t: p0t_model(t, mat_frwd, r0_frwd, method)
    p0t_frwd = lambda t: p0t_model(t, mat_frwd, ri_frwd, method)

    # Price forward curve swaps
    swaps_model_frwd = np.zeros(len(instruments_frwd))
    swaps_initial_frwd = np.zeros(len(instruments_frwd))

    for i in range(0, len(instruments_frwd)):
        swaps_model_frwd[i] = instruments_frwd[i](p0t_frwd)
        swaps_initial_frwd[i] = instruments_frwd[i](p0t_frwd_initial)

    print('Prices for Par Swaps (initial) = ', swaps_initial_frwd, '\n')
    print('Prices for Par Swaps = ', swaps_model_frwd, '\n')

    print(swap1_frwd(p0t_frwd))

    # ============= Plotting =============
    t = np.linspace(0, 10, 100)
    plot_curves(t, p0t_discount, p0t_frwd)


if __name__ == "__main__":
    main()
