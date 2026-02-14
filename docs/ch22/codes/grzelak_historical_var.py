"""
Historical Value-at-Risk (VaR) calculation using real market data.

This educational code demonstrates VaR estimation using historical simulation
of interest rate derivatives portfolio. It builds yield curves from market data,
revalues portfolio under historical scenarios, and computes Value-at-Risk metrics.
Based on "Financial Engineering" course by L.A. Grzelak.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

Market data source:
https://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yieldYear&year=2021

@author: Lech A. Grzelak
"""

import enum
from copy import deepcopy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ============= Option Type Enum =============
class OptionTypeSwap(enum.Enum):
    """Defines swap option types: receiver or payer."""
    RECEIVER = 1.0
    PAYER = -1.0


# ============= Swap Pricing =============
def ir_swap(option_type, notional, strike, t, ti, tm, n, p0t):
    """
    Compute interest rate swap price using discount bond curve.

    Parameters
    ----------
    option_type : OptionTypeSwap
        Payer or receiver swap.
    notional : float
        Notional amount.
    strike : float
        Strike rate.
    t : float
        Evaluation time.
    ti, tm : float
        Swap start and end times.
    n : int
        Number of payment dates.
    p0t : callable
        Zero coupon bond price function P(0, T).

    Returns
    -------
    float
        Swap price.
    """
    ti_grid = np.linspace(ti, tm, int(n))
    tau = ti_grid[1] - ti_grid[0]

    # Overwrite Ti if t > Ti
    prev_ti = ti_grid[np.where(ti_grid < t)]
    if np.size(prev_ti) > 0:
        ti = prev_ti[-1]

    # Handle case when some payments are already done
    ti_grid = ti_grid[np.where(ti_grid > t)]

    temp = 0.0

    for idx, ti_val in enumerate(ti_grid):
        if ti_val > ti:
            temp = temp + tau * p0t(ti_val)

    p_t_ti = p0t(ti)
    p_t_tm = p0t(tm)

    if option_type == OptionTypeSwap.PAYER:
        swap = (p_t_ti - p_t_tm) - strike * temp
    elif option_type == OptionTypeSwap.RECEIVER:
        swap = strike * temp - (p_t_ti - p_t_tm)

    return swap * notional


# ============= Yield Curve Calibration =============
def p0t_model(t, ti, ri, method):
    """
    Compute zero coupon bond price using interpolated yield curve.

    Parameters
    ----------
    t : float
        Maturity time.
    ti : ndarray
        Spine point maturities.
    ri : ndarray
        Spine point yields.
    method : callable
        Interpolation method that returns a function ri(t).

    Returns
    -------
    float
        Zero coupon bond price P(0, t).
    """
    r_interp = method(ti, ri)
    r = r_interp(t)
    return np.exp(-r * t)


def yield_curve(instruments, maturities, r0, method, tol):
    """
    Calibrate yield curve from market swap quotes using Newton-Raphson.

    Parameters
    ----------
    instruments : list
        List of swap pricing functions to calibrate to.
    maturities : ndarray
        Maturity points for the yield curve.
    r0 : ndarray
        Initial guess for spine point yields.
    method : callable
        Interpolation method.
    tol : float
        Convergence tolerance.

    Returns
    -------
    ndarray
        Calibrated spine point yields.
    """
    r0 = deepcopy(r0)
    ri = multivariate_newton_raphson(r0, maturities, instruments, method, tol=tol)
    return ri


def multivariate_newton_raphson(ri, ti, instruments, method, tol):
    """
    Multivariate Newton-Raphson solver for yield curve calibration.

    Parameters
    ----------
    ri : ndarray
        Initial yield guesses.
    ti : ndarray
        Maturity points.
    instruments : list
        List of pricing functions to match.
    method : callable
        Interpolation method.
    tol : float
        Convergence tolerance.

    Returns
    -------
    ndarray
        Solved yields.
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
    return ri


def jacobian(ti, ri, instruments, method):
    """
    Compute Jacobian matrix for Newton-Raphson solver.

    Parameters
    ----------
    ti : ndarray
        Maturity points.
    ri : ndarray
        Current yields.
    instruments : list
        Pricing functions.
    method : callable
        Interpolation method.

    Returns
    -------
    ndarray
        Jacobian matrix of shape (len(instruments), len(ri)).
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
    Evaluate all swap instruments at given yields.

    Parameters
    ----------
    ti : ndarray
        Maturity points.
    ri : ndarray
        Yields at maturity points.
    instruments : list
        Pricing functions.
    method : callable
        Interpolation method.

    Returns
    -------
    ndarray
        Prices of all instruments.
    """
    p0t_temp = lambda t: p0t_model(t, ti, ri, method)
    val = np.zeros(len(instruments))
    for i in range(0, len(instruments)):
        val[i] = instruments[i](p0t_temp)
    return val


# ============= Interpolation =============
def linear_interpolation(ti, ri):
    """
    Create linear interpolation function for yield curve.

    Parameters
    ----------
    ti : ndarray
        Maturity points.
    ri : ndarray
        Yields at maturity points.

    Returns
    -------
    callable
        Interpolation function r(t).
    """
    interpolator = lambda t: np.interp(t, ti, ri)
    return interpolator


# ============= Curve Building =============
def build_yield_curve(strike_rates, maturities):
    """
    Build zero coupon bond curve from market swap quotes.

    Parameters
    ----------
    strike_rates : ndarray
        Market swap rates at each maturity.
    maturities : ndarray
        Maturity points for swaps.

    Returns
    -------
    tuple
        (p0t function, list of swap instruments)
    """
    # Convergence tolerance
    tol = 1.0e-15
    # Initial guess for spine points
    r0 = np.array([0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01])
    # Interpolation method
    method = linear_interpolation

    # Define swap pricing functions for calibration
    swap_funcs = [
        lambda p0t, k=strike_rates[i], mat=maturities[i]: ir_swap(
            OptionTypeSwap.PAYER, 1, k, 0.0, 0.0, mat, 4 * mat, p0t
        )
        for i in range(len(strike_rates))
    ]

    # Determine optimal spine points
    ri = yield_curve(swap_funcs, maturities, r0, method, tol)

    # Build zero coupon bond curve from spine points
    p0t = lambda t: p0t_model(t, maturities, ri, method)
    return p0t, swap_funcs


# ============= Portfolio =============
def portfolio(p0t):
    """
    Compute portfolio value from collection of interest rate swaps.

    Parameters
    ----------
    p0t : callable
        Zero coupon bond price function.

    Returns
    -------
    float
        Total portfolio value.
    """
    value = (
        ir_swap(OptionTypeSwap.RECEIVER, 1000000, 0.02, 0.0, 0.0, 20, 20, p0t)
        + ir_swap(OptionTypeSwap.PAYER, 500000, 0.01, 0.0, 0.0, 10, 20, p0t)
        + ir_swap(OptionTypeSwap.RECEIVER, 25000, 0.02, 0.0, 0.0, 30, 60, p0t)
        + ir_swap(OptionTypeSwap.PAYER, 74000, 0.005, 0.0, 0.0, 5, 10, p0t)
        + ir_swap(OptionTypeSwap.RECEIVER, 254000, 0.032, 0.0, 0.0, 15, 10, p0t)
        + ir_swap(OptionTypeSwap.RECEIVER, 854000, 0.01, 0.0, 0.0, 7, 20, p0t)
        + ir_swap(OptionTypeSwap.PAYER, 350000, 0.028, 0.0, 0.0, 10, 20, p0t)
        + ir_swap(OptionTypeSwap.PAYER, 1000000, -0.01, 0.0, 0.0, 5, 20, p0t)
        + ir_swap(OptionTypeSwap.RECEIVER, 1000000, 0.01, 0.0, 0.0, 14, 20, p0t)
        + ir_swap(OptionTypeSwap.PAYER, 1000000, 0.03, 0.0, 0.0, 2, 4, p0t)
    )
    return value


# ============= VaR Plotting =============
def plot_var_histogram(pv_data, var_estimate, es_estimate):
    """
    Plot histogram of portfolio P&L with VaR and ES markers.

    Parameters
    ----------
    pv_data : ndarray
        Portfolio values from historical scenarios.
    var_estimate : float
        Value-at-Risk estimate.
    es_estimate : float
        Expected shortfall estimate.
    """
    plt.figure(1)
    plt.grid()
    plt.hist(pv_data, 20)
    plt.plot(var_estimate, 0, "or")
    plt.plot(es_estimate, 0, "ok")
    plt.legend(["VaR", "ES", "P&L"])


# ============= Main Calculation =============
def main():
    """
    Main computation: compute historical VaR using market data and scenario analysis.
    """
    # --------- Configuration ---------
    # Load market data: swap rates from historical dates
    market_data_xls = pd.read_excel("MrktData.xlsx")

    # Divide by 100 as rates are expressed in percentages
    market_data = np.array(market_data_xls) / 100.0

    # --------- Scenario Generation ---------
    # Build 1D scenarios from historical changes
    shape = np.shape(market_data)
    num_scenarios = shape[0]
    num_instruments = shape[1]

    scenarios = np.zeros((num_scenarios - 1, num_instruments))
    for i in range(0, num_scenarios - 1):
        for j in range(0, num_instruments):
            scenarios[i, j] = market_data[i + 1, j] - market_data[i, j]

    # --------- Yield Curve Calibration ---------
    # Market quotes for swaps today
    swaps_market = np.array([0.08, 0.2, 0.4, 0.77, 1.07, 1.29, 1.82, 1.9]) / 100
    maturities = np.array([1.0, 2.0, 3.0, 5.0, 7.0, 10.0, 20.0, 30.0])

    # Generate shocked yield curves for each scenario
    swaps_market_shocked = np.zeros((num_scenarios - 1, num_instruments))
    for i in range(0, num_scenarios - 1):
        for j in range(0, num_instruments):
            swaps_market_shocked[i, j] = swaps_market[j] + scenarios[i, j]

    # --------- Portfolio Revaluation ---------
    # Build yield curves and revalue portfolio for each scenario
    yc_for_var = []
    for i in range(0, num_scenarios - 1):
        p0t, instruments = build_yield_curve(swaps_market_shocked[i, :], maturities)
        yc_for_var.append(p0t)
        print("Scenario number", i, " out of  ", num_scenarios - 1)

    # Revalue portfolio under all scenarios
    portfolio_pv = np.zeros(num_scenarios - 1)
    for i in range(0, num_scenarios - 1):
        portfolio_pv[i] = portfolio(yc_for_var[i])

    # Current yield curve
    yc_today, insts = build_yield_curve(swaps_market, maturities)
    print("Current Portfolio PV is ", portfolio(yc_today))

    # --------- VaR Calculation ---------
    # Confidence level
    alpha = 0.05

    # Value-at-Risk estimate
    hvar_estimate = np.quantile(portfolio_pv, alpha)
    print("(H)VaR for alpha = ", alpha, " is equal to=", hvar_estimate)

    # Expected shortfall (conditional VaR)
    cond_losses = portfolio_pv[portfolio_pv < hvar_estimate]
    print("P&L which < VaR_alpha =", cond_losses)
    es = np.mean(cond_losses)
    print("Expected shortfall = ", es)

    # --------- Generate Plot ---------
    plot_var_histogram(portfolio_pv, hvar_estimate, es)

    return 0.0


if __name__ == "__main__":
    main()
