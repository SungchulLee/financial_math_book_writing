# Treasury Yield Curve

## Background

Yield curve construction from treasury swap instruments.

Based on "Financial Engineering" course by L.A. Grzelak.
The course is based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.
@author: Lech A. Grzelak

---

## Code

```python
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


# ======================================================================
# Main
# ======================================================================

if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
Describe the difference between a yield curve constructed from treasury instruments versus one constructed from swap instruments. Which is more commonly used for derivative pricing?

??? success "Solution to Exercise 1"
    Treasury yield curves are built from government bonds, which are considered default-free. They reflect the risk-free rate but may include liquidity premia and are affected by government supply/demand dynamics. Swap yield curves are built from interest rate swaps, which reflect interbank credit risk (historically LIBOR, now SOFR-based). Swap curves are smoother because swaps are standardized OTC contracts available at many maturities.

    For derivative pricing, swap curves (specifically OIS curves for discounting) are more commonly used because derivatives are typically collateralized, and the collateral rate matches OIS. Treasury curves are used for government bond analytics and as benchmarks.

---

**Exercise 2.**
The Newton-Raphson method requires an initial guess for the rates. What happens if the initial guess is far from the solution, and how does the code handle this?

??? success "Solution to Exercise 2"
    If the initial guess is far from the solution, Newton-Raphson may converge slowly, diverge, or converge to a wrong local minimum. The code uses $r_0 = 0.01$ for all spine points, which is a reasonable initial guess for typical interest rate environments ($0-5\%$). The convergence is monitored via the norm of the update vector, and the loop continues until $\|\text{err}\| < \text{tol}$. In practice, if the market swap rates are reasonable, this initial guess leads to convergence within $5-10$ iterations.

---

**Exercise 3.**
If par swap rates are $\{2\%, 3\%, 4\%, 5\%\}$ at maturities $\{1, 5, 10, 30\}$ years, the curve is upward-sloping. What does this imply about the market's expectation for future short-term rates?

??? success "Solution to Exercise 3"
    An upward-sloping yield curve implies that longer-term rates are higher than shorter-term rates. Under the expectations hypothesis, this means the market expects short-term rates to rise in the future:

    $$
    f(0, t_1, t_2) > y(0, t_1) \implies \text{expected future short rates exceed current short rates}.
    $$

    However, this interpretation is complicated by the term premium: investors may demand higher yields for longer maturities due to increased interest rate risk, even if they expect rates to remain constant. The actual expectation component and the risk premium component cannot be separated from the yield curve alone.

---

**Exercise 4.**
Explain the role of the convergence tolerance parameter `tol = 1e-15` and why such high precision is used.

??? success "Solution to Exercise 4"
    The tolerance $10^{-15}$ requires the Newton-Raphson solution to be accurate to near machine precision (double-precision floating point has about 16 significant digits). This extreme precision is used because:

    1. **Consistency**: Even small errors in the yield curve can propagate and amplify in derivative pricing, especially for long-dated or exotic instruments.
    2. **Greeks accuracy**: Finite-difference Greeks involve subtracting nearby prices; if the curve is not solved precisely, the price differences are contaminated by curve-fitting noise rather than genuine sensitivities.
    3. **Repricing**: Par swaps should reprice to exactly zero; any residual value indicates a calibration error.
