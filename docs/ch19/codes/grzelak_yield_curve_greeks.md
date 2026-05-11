# Yield Curve with Greeks

## Background

Yield curve Greeks: sensitivity analysis of swap prices to rate changes.

Based on "Financial Engineering" course by L.A. Grzelak.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak

---

## Code

```python
"""
Yield curve Greeks: sensitivity analysis of swap prices to rate changes.

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


# ======================================================================
# Functions / Classes
# ======================================================================


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
    if t >= ti[-1]:
        r = ri[-1]
    elif t <= ti[0]:
        r = ri[0]
    elif t > ti[0] and t < ti[-1]:
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


def quadratic_interpolation(ti, ri):
    """
    Quadratic interpolation function.

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
    interpolator = interp1d(ti, ri, kind='quadratic')
    return interpolator


def cubic_interpolation(ti, ri):
    """
    Cubic interpolation function.

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
    interpolator = interp1d(ti, ri, kind='cubic')
    return interpolator


def build_instruments(k, mat):
    """
    Build swap instrument list for yield curve construction.

    Parameters
    ----------
    k : array
        Strike rates
    mat : array
        Maturities

    Returns
    -------
    list
        List of instrument pricing functions
    """
    swap1 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[0], 0.0, 0.0,
                                 mat[0], 4 * mat[0], p0t)
    swap2 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[1], 0.0, 0.0,
                                 mat[1], 4 * mat[1], p0t)
    swap3 = lambda p0t: ir_swap(OptionTypeSwap.RECEIVER, 1, k[2], 0.0, 0.0,
                                 mat[2], 4 * mat[2], p0t)
    swap4 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[3], 0.0, 0.0,
                                 mat[3], 4 * mat[3], p0t)
    swap5 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[4], 0.0, 0.0,
                                 mat[4], 4 * mat[4], p0t)
    swap6 = lambda p0t: ir_swap(OptionTypeSwap.RECEIVER, 1, k[5], 0.0, 0.0,
                                 mat[5], 4 * mat[5], p0t)
    swap7 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[6], 0.0, 0.0,
                                 mat[6], 4 * mat[6], p0t)
    swap8 = lambda p0t: ir_swap(OptionTypeSwap.PAYER, 1, k[7], 0.0, 0.0,
                                 mat[7], 4 * mat[7], p0t)
    instruments = [swap1, swap2, swap3, swap4, swap5, swap6, swap7, swap8]
    return instruments


def main():
    """Run Greeks computation."""
    # ============= Parameters =============
    tol = 1.0e-8
    r0 = np.array([0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01])
    method = cubic_interpolation

    # Construct swaps for yield curve building
    k = np.array([0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09])
    mat = np.array([1.0, 2.0, 3.0, 5.0, 7.0, 10.0, 20.0, 30.0])

    instruments = build_instruments(k, mat)
    ri = yield_curve(instruments, mat, r0, method, tol)
    p0t = lambda t: p0t_model(t, mat, ri, method)

    # Define off-market swap
    swap_lambda = lambda p0t_arg: ir_swap(OptionTypeSwap.PAYER, 1, 0.03, 0.0,
                                           0.0, 4, 6 * mat[0], p0t_arg)
    swap = swap_lambda(p0t)
    print('Swap price = ', swap)

    # ============= Compute Greeks =============
    dk = 0.0001
    delta = np.zeros(len(k))
    k_new = k.copy()
    for i in range(0, len(k)):
        k_new[i] = k_new[i] + dk
        instruments = build_instruments(k_new, mat)
        ri = yield_curve(instruments, mat, r0, method, tol)
        p0t_new = lambda t: p0t_model(t, mat, ri, method)
        swap_shock = swap_lambda(p0t_new)
        delta[i] = (swap_shock - swap) / dk
        k_new[i] = k_new[i] - dk

    print(delta)


# ======================================================================
# Main
# ======================================================================

if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
Yield curve Greeks measure the sensitivity of a derivative's price to changes in the swap rates used to construct the curve. Describe how the Delta for each swap rate is computed via finite differences.

??? success "Solution to Exercise 1"
    For each swap rate $k_i$ in the yield curve construction:

    1. Bump $k_i$ by a small amount $\delta k = 0.01\%$ (1 basis point).
    2. Rebuild the yield curve using Newton-Raphson with the bumped rate.
    3. Reprice the target swap using the new curve: $V_{\text{up}} = V(k_i + \delta k)$.
    4. Compute the Delta: $\Delta_i = (V_{\text{up}} - V_{\text{base}})/\delta k$.

    This is repeated for each of the $n$ swap rates, producing a vector of sensitivities showing how the target swap's value changes when each underlying instrument moves.

---

**Exercise 2.**
If the Deltas of a payer swap with respect to the 8 swap rates are $\Delta = [0.2, 0.5, 1.3, -0.1, 0.8, 2.1, -0.3, 0.05]$, which swap rate has the largest impact on the derivative's price?

??? success "Solution to Exercise 2"
    The swap rate with the largest absolute Delta is the 6th rate (10-year maturity) with $|\Delta_6| = 2.1$. A 1 basis point move in the 10-year swap rate changes the derivative price by $2.1$ units. The negative Deltas at positions 4 and 7 indicate that increases in those rates actually decrease the derivative's value, suggesting offsetting sensitivities at those maturities.

---

**Exercise 3.**
Explain why the interpolation method (linear vs. cubic) affects the computed Greeks and how to choose an appropriate method.

??? success "Solution to Exercise 3"
    The interpolation method determines how a bump in one swap rate propagates to neighboring maturities. With linear interpolation, a bump at maturity $T_k$ only affects the curve segment between $T_{k-1}$ and $T_{k+1}$, producing localized Greeks. With cubic interpolation, the bump propagates further due to the global smoothness constraints, potentially affecting discount factors at distant maturities.

    Choose cubic interpolation when smooth forward rates are needed (for realistic hedging and risk decomposition). Choose linear interpolation when localized sensitivities are desired and forward rate smoothness is less important. In practice, cubic is preferred for production risk systems because it avoids spurious hedging artifacts from forward rate discontinuities.

---

**Exercise 4.**
The code builds 8 swap instruments at maturities from 1 to 30 years. If a new instrument at 15 years is added, how does this affect the yield curve construction and the dimension of the Jacobian matrix?

??? success "Solution to Exercise 4"
    Adding a 15-year instrument increases the number of spine points from 8 to 9. The Jacobian matrix grows from $8 \times 8$ to $9 \times 9$. The yield curve has one more degree of freedom, allowing it to fit an additional market observable. The Newton-Raphson system now solves 9 equations (swap values equal zero) in 9 unknowns (spine point rates). The interpolated curve between the 10-year and 20-year points becomes more constrained, potentially improving the accuracy of prices for instruments with maturities near 15 years.
