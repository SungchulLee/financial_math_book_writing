#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cantaro86_bs_pricer.py
Black-Scholes Pricer -- Multi-Method Educational Implementation

Credits
-------
Based on the BS_pricer class from:
    cantaro86, "Financial Models Numerical Methods" (FMNM)
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Adapted as a SELF-CONTAINED educational module for the
"Quant Finance with Python" course (Chapter 6 -- Black-Scholes).

All external FMNM dependencies have been inlined so the file runs
stand-alone with only NumPy, SciPy, and Matplotlib.

Methods implemented
-------------------
1. Closed-form Black-Scholes formula (call and put)
2. Vega (dPrice / dSigma)
3. Monte Carlo simulation (European options)
4. PDE solver -- implicit finite-difference scheme via sparse LU
5. Longstaff-Schwartz Method (LSM) for American put options
"""

import numpy as np
import scipy.stats as ss
from scipy import sparse
from scipy.sparse.linalg import splu
import matplotlib.pyplot as plt
from time import time


# ============================================================================
# 1. CLOSED-FORM BLACK-SCHOLES FORMULA
# ============================================================================

def bs_price(payoff, S0, K, T, r, sigma):
    """
    Analytical Black-Scholes price for a European option.

    Parameters
    ----------
    payoff : str
        "call" or "put"
    S0 : float
        Current stock / index price
    K : float
        Strike price
    T : float
        Time to maturity in years
    r : float
        Risk-free interest rate (continuous compounding)
    sigma : float
        Annualised volatility

    Returns
    -------
    float
        Option present value
    """
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S0 / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    if payoff == "call":
        return S0 * ss.norm.cdf(d1) - K * np.exp(-r * T) * ss.norm.cdf(d2)
    elif payoff == "put":
        return K * np.exp(-r * T) * ss.norm.cdf(-d2) - S0 * ss.norm.cdf(-d1)
    else:
        raise ValueError("payoff must be 'call' or 'put'")


def bs_vega(S0, K, T, r, sigma):
    """
    Black-Scholes Vega: partial derivative of the option price w.r.t. sigma.

    Vega is the same for calls and puts under Black-Scholes.

    Parameters
    ----------
    S0, K, T, r, sigma : float
        Standard Black-Scholes parameters

    Returns
    -------
    float
        Vega value
    """
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return S0 * np.sqrt(T) * ss.norm.pdf(d1)


# ============================================================================
# 2. BS_PRICER CLASS -- MULTI-METHOD ENGINE
# ============================================================================

class BS_pricer:
    """
    Self-contained Black-Scholes pricer with multiple pricing methods.

    Pricing methods available through instance methods:
        closed_formula()   -- exact Black-Scholes formula
        MC()               -- Monte Carlo simulation (European)
        PDE_price()        -- implicit finite-difference PDE solver
        LSM()              -- Longstaff-Schwartz for American puts

    Static helpers:
        BlackScholes()     -- quick static closed-form price
        vega()             -- quick static vega calculation

    Parameters
    ----------
    S0 : float       Current stock price
    K : float        Strike price
    T : float        Time to maturity (years)
    r : float        Risk-free rate
    sigma : float    Volatility
    payoff : str     "call" or "put"
    exercise : str   "European" or "American"
    """

    def __init__(self, S0, K, T, r, sigma, payoff="call", exercise="European"):
        self.S0 = float(S0)
        self.K = float(K)
        self.T = float(T)
        self.r = float(r)
        self.sig = float(sigma)
        self.payoff = payoff
        self.exercise = exercise

        # Populated by PDE_price for plotting
        self.price = 0.0
        self.S_vec = None
        self.price_vec = None
        self.mesh = None

    # ----------------------------------------------------------------
    # Payoff helper
    # ----------------------------------------------------------------
    def payoff_f(self, S):
        """Compute the payoff vector for an array of spot prices."""
        if self.payoff == "call":
            return np.maximum(S - self.K, 0)
        elif self.payoff == "put":
            return np.maximum(self.K - S, 0)
        else:
            raise ValueError("payoff must be 'call' or 'put'")

    # ----------------------------------------------------------------
    # 2a. Static Black-Scholes helpers
    # ----------------------------------------------------------------
    @staticmethod
    def BlackScholes(payoff="call", S0=100.0, K=100.0, T=1.0, r=0.1, sigma=0.2):
        """Static convenience wrapper around the module-level bs_price()."""
        return bs_price(payoff, S0, K, T, r, sigma)

    @staticmethod
    def vega(sigma, S0, K, T, r):
        """Static convenience wrapper around the module-level bs_vega()."""
        return bs_vega(S0, K, T, r, sigma)

    # ----------------------------------------------------------------
    # 2b. Closed-form (instance method)
    # ----------------------------------------------------------------
    def closed_formula(self):
        """
        Black-Scholes closed-form price using instance parameters.

        Returns
        -------
        float
            Option price
        """
        return bs_price(self.payoff, self.S0, self.K, self.T, self.r, self.sig)

    # ----------------------------------------------------------------
    # 2c. Monte Carlo
    # ----------------------------------------------------------------
    def MC(self, N=100_000, Err=False, Time=False):
        """
        Monte Carlo pricing of a European option under GBM.

        The terminal stock price is simulated directly (no path needed
        for European options):

            S_T = S0 * exp((r - 0.5*sig^2)*T + sig*sqrt(T)*Z),   Z ~ N(0,1)

        Parameters
        ----------
        N : int
            Number of simulation paths
        Err : bool
            If True, also return the standard error of the MC estimate
        Time : bool
            If True, also return the elapsed wall-clock time

        Returns
        -------
        float or tuple
            Price, and optionally (std_error, elapsed_time)
        """
        t_init = time()

        # Simulate terminal stock prices under risk-neutral measure
        Z = np.random.standard_normal(N)
        S_T = self.S0 * np.exp(
            (self.r - 0.5 * self.sig ** 2) * self.T
            + self.sig * np.sqrt(self.T) * Z
        )

        # Discounted payoffs
        disc_payoffs = np.exp(-self.r * self.T) * self.payoff_f(S_T)
        V = np.mean(disc_payoffs)

        elapsed = time() - t_init
        std_err = ss.sem(disc_payoffs)

        if Err and Time:
            return V, std_err, elapsed
        elif Err:
            return V, std_err
        elif Time:
            return V, elapsed
        else:
            return V

    # ----------------------------------------------------------------
    # 2d. PDE solver (implicit finite-difference via sparse LU)
    # ----------------------------------------------------------------
    def PDE_price(self, steps, Time=False):
        """
        Solve the Black-Scholes PDE on a log-price grid using an
        implicit (backward Euler) finite-difference scheme.

        The PDE in log-price x = ln(S):

            dV/dt + (r - sig^2/2) dV/dx + 0.5*sig^2 d^2V/dx^2 - r*V = 0

        The implicit scheme leads to a tridiagonal system solved at each
        time step via a sparse LU factorisation (scipy.sparse.linalg.splu).

        For American options the early-exercise constraint is imposed at
        each time step by taking the element-wise maximum against the
        intrinsic payoff.

        Parameters
        ----------
        steps : tuple of int
            (Nspace, Ntime) -- number of spatial and temporal grid points
        Time : bool
            If True, also return the elapsed wall-clock time

        Returns
        -------
        float or tuple
            Interpolated price at S0, and optionally elapsed_time
        """
        t_init = time()

        Nspace, Ntime = steps

        # Spatial domain in log-price
        S_max = 6.0 * self.K
        S_min = self.K / 6.0
        x_max = np.log(S_max)
        x_min = np.log(S_min)
        x0 = np.log(self.S0)           # current log-price

        x, dx = np.linspace(x_min, x_max, Nspace, retstep=True)
        t, dt = np.linspace(0, self.T, Ntime, retstep=True)

        self.S_vec = np.exp(x)          # grid of stock prices
        Payoff = self.payoff_f(self.S_vec)

        # Solution matrix: V[i, j] = option value at (x_i, t_j)
        V = np.zeros((Nspace, Ntime))

        # ---- Terminal condition (at maturity t = T) ----
        V[:, -1] = Payoff

        # ---- Boundary conditions ----
        if self.payoff == "call":
            V[-1, :] = np.exp(x_max) - self.K * np.exp(-self.r * t[::-1])
            V[0, :] = 0.0
        else:  # put
            V[-1, :] = 0.0
            V[0, :] = Payoff[0] * np.exp(-self.r * t[::-1])

        # ---- Tridiagonal coefficients for the implicit scheme ----
        sig2 = self.sig ** 2
        dxx = dx ** 2
        a = (dt / 2.0) * ((self.r - 0.5 * sig2) / dx - sig2 / dxx)
        b = 1.0 + dt * (sig2 / dxx + self.r)
        c = -(dt / 2.0) * ((self.r - 0.5 * sig2) / dx + sig2 / dxx)

        # Build sparse tridiagonal matrix (interior points only)
        D = sparse.diags(
            [a, b, c], [-1, 0, 1],
            shape=(Nspace - 2, Nspace - 2)
        ).tocsc()

        # Pre-factor with sparse LU for efficiency
        DD = splu(D)

        offset = np.zeros(Nspace - 2)

        # ---- Backward time-stepping ----
        if self.exercise == "European":
            for i in range(Ntime - 2, -1, -1):
                offset[0] = a * V[0, i]
                offset[-1] = c * V[-1, i]
                V[1:-1, i] = DD.solve(V[1:-1, i + 1] - offset)
        elif self.exercise == "American":
            for i in range(Ntime - 2, -1, -1):
                offset[0] = a * V[0, i]
                offset[-1] = c * V[-1, i]
                V[1:-1, i] = np.maximum(
                    DD.solve(V[1:-1, i + 1] - offset),
                    Payoff[1:-1]
                )
        else:
            raise ValueError("exercise must be 'European' or 'American'")

        # Interpolate to find the price at the current stock price S0
        self.price = np.interp(x0, x, V[:, 0])
        self.price_vec = V[:, 0]
        self.mesh = V

        elapsed = time() - t_init
        if Time:
            return self.price, elapsed
        return self.price

    # ----------------------------------------------------------------
    # 2e. Longstaff-Schwartz Method (American put)
    # ----------------------------------------------------------------
    def LSM(self, N=10_000, paths=10_000, order=2):
        """
        Longstaff-Schwartz Method for pricing American put options.

        At each exercise date the method performs a least-squares polynomial
        regression of the discounted future cash-flows on the current stock
        price.  Paths where the immediate exercise value exceeds the
        estimated continuation value are exercised early.

        Parameters
        ----------
        N : int
            Number of time steps per path
        paths : int
            Number of simulated paths
        order : int
            Polynomial order for the continuation-value regression

        Returns
        -------
        float
            Estimated American put price
        """
        if self.payoff != "put":
            raise ValueError("LSM is implemented for put options only")

        dt = self.T / (N - 1)
        df = np.exp(-self.r * dt)           # one-step discount factor

        # Simulate log-price increments and build the price matrix
        X0 = np.zeros((paths, 1))
        increments = ss.norm.rvs(
            loc=(self.r - 0.5 * self.sig ** 2) * dt,
            scale=self.sig * np.sqrt(dt),
            size=(paths, N - 1),
        )
        X = np.concatenate((X0, increments), axis=1).cumsum(axis=1)
        S = self.S0 * np.exp(X)             # paths x N price matrix

        # Intrinsic value (put payoff) along every path and time step
        H = np.maximum(self.K - S, 0.0)

        # Value matrix -- initialised at terminal payoff
        V = np.zeros_like(H)
        V[:, -1] = H[:, -1]

        # ---- Backward induction with regression ----
        for t_idx in range(N - 2, 0, -1):
            in_the_money = H[:, t_idx] > 0   # only regress on ITM paths
            if np.sum(in_the_money) == 0:
                V[:, t_idx] = V[:, t_idx + 1] * df
                continue

            # Polynomial regression: continuation value ~ f(S)
            rg = np.polyfit(
                S[in_the_money, t_idx],
                V[in_the_money, t_idx + 1] * df,
                order,
            )
            C = np.polyval(rg, S[in_the_money, t_idx])

            # Decision: exercise now if intrinsic > continuation estimate
            exercise = np.zeros(paths, dtype=bool)
            exercise[in_the_money] = H[in_the_money, t_idx] > C

            V[exercise, t_idx] = H[exercise, t_idx]
            V[exercise, t_idx + 1:] = 0        # kill future cash-flows
            discount_path = V[:, t_idx] == 0
            V[discount_path, t_idx] = V[discount_path, t_idx + 1] * df

        # Price = discounted average of values at t=1
        V0 = np.mean(V[:, 1]) * df
        return V0

    # ----------------------------------------------------------------
    # 2f. Plotting helpers
    # ----------------------------------------------------------------
    def plot(self, axis=None):
        """
        Plot the intrinsic payoff alongside the Black-Scholes price curve
        obtained from the PDE solver.

        If the PDE has not been run yet, it is executed automatically with
        a fine grid (7000 x 5000).
        """
        if self.S_vec is None or self.price_vec is None:
            self.PDE_price((7000, 5000))

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(self.S_vec, self.payoff_f(self.S_vec),
                color="blue", linewidth=2, label="Payoff at expiry")
        ax.plot(self.S_vec, self.price_vec,
                color="red", linewidth=2, label="BS price (PDE)")
        if isinstance(axis, list):
            ax.axis(axis)
        ax.set_xlabel("Stock price  $S$", fontsize=12)
        ax.set_ylabel("Option value", fontsize=12)
        ax.set_title(
            f"{self.exercise} {self.payoff.capitalize()} -- "
            f"Black-Scholes Price Curve",
            fontsize=13,
        )
        ax.legend(fontsize=11)
        ax.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

    def mesh_plt(self):
        """
        3-D surface plot of the option value over (S, t) from the PDE mesh.
        """
        if self.S_vec is None or self.mesh is None:
            self.PDE_price((7000, 5000))

        fig = plt.figure(figsize=(10, 7))
        ax = fig.add_subplot(111, projection="3d")

        T_grid = np.linspace(0, self.T, self.mesh.shape[1])
        X, Y = np.meshgrid(T_grid, self.S_vec)
        ax.plot_surface(Y, X, self.mesh, cmap="ocean", alpha=0.85)
        ax.set_title(
            f"{self.exercise} {self.payoff.capitalize()} -- "
            f"BS Price Surface",
            fontsize=13,
        )
        ax.set_xlabel("S")
        ax.set_ylabel("t")
        ax.set_zlabel("V")
        ax.view_init(30, -100)
        plt.tight_layout()
        plt.show()


# ============================================================================
# 3. COMPREHENSIVE DEMO
# ============================================================================

def main():
    """
    Demonstrate all pricing methods and compare results in a summary table.
    """

    print("=" * 75)
    print("  Black-Scholes Multi-Method Pricer")
    print("  Based on cantaro86 / Financial-Models-Numerical-Methods")
    print("=" * 75)

    # ------------------------------------------------------------------
    # Market parameters
    # ------------------------------------------------------------------
    S0    = 100.0     # current stock price
    K     = 100.0     # strike price  (at-the-money)
    T     = 1.0       # time to maturity (1 year)
    r     = 0.05      # risk-free rate (5 %)
    sigma = 0.20      # volatility    (20 %)

    print(f"\nMarket Parameters:")
    print(f"  Spot price   S0    = {S0}")
    print(f"  Strike price K     = {K}")
    print(f"  Maturity     T     = {T} year")
    print(f"  Risk-free    r     = {r:.2%}")
    print(f"  Volatility   sigma = {sigma:.2%}")

    # ------------------------------------------------------------------
    # A. Closed-form pricing (call and put)
    # ------------------------------------------------------------------
    print("\n" + "-" * 75)
    print("A. CLOSED-FORM BLACK-SCHOLES PRICES")
    print("-" * 75)

    call_pricer = BS_pricer(S0, K, T, r, sigma, payoff="call", exercise="European")
    put_pricer  = BS_pricer(S0, K, T, r, sigma, payoff="put",  exercise="European")

    call_cf = call_pricer.closed_formula()
    put_cf  = put_pricer.closed_formula()

    print(f"  European Call : {call_cf:.6f}")
    print(f"  European Put  : {put_cf:.6f}")

    # Put-call parity check
    parity_lhs = call_cf - put_cf
    parity_rhs = S0 - K * np.exp(-r * T)
    print(f"\n  Put-Call Parity check:  C - P = S0 - K*exp(-rT)")
    print(f"    LHS (C - P)     = {parity_lhs:.6f}")
    print(f"    RHS             = {parity_rhs:.6f}")
    print(f"    Difference      = {abs(parity_lhs - parity_rhs):.2e}")

    # Vega
    v = bs_vega(S0, K, T, r, sigma)
    print(f"\n  Vega (dPrice/dSigma) = {v:.6f}")

    # ------------------------------------------------------------------
    # B. Monte Carlo pricing
    # ------------------------------------------------------------------
    print("\n" + "-" * 75)
    print("B. MONTE CARLO PRICING (European)")
    print("-" * 75)

    np.random.seed(42)
    N_mc = 500_000

    call_mc, call_se, call_t = call_pricer.MC(N=N_mc, Err=True, Time=True)
    put_mc,  put_se,  put_t  = put_pricer.MC(N=N_mc, Err=True, Time=True)

    print(f"  Paths = {N_mc:,}")
    print(f"  Call MC price : {call_mc:.6f}  (SE = {call_se:.6f}, time = {call_t:.3f}s)")
    print(f"  Put  MC price : {put_mc:.6f}  (SE = {put_se:.6f}, time = {put_t:.3f}s)")
    print(f"  Call error vs closed-form : {abs(call_mc - call_cf):.6f}")
    print(f"  Put  error vs closed-form : {abs(put_mc - put_cf):.6f}")

    # ------------------------------------------------------------------
    # C. PDE pricing and convergence
    # ------------------------------------------------------------------
    print("\n" + "-" * 75)
    print("C. PDE PRICING (Implicit Finite-Difference, Sparse LU)")
    print("-" * 75)

    grid_sizes = [
        (200,  100),
        (500,  250),
        (1000, 500),
        (2000, 1000),
        (5000, 2500),
    ]

    print(f"\n  {'Nspace':>8} {'Ntime':>8} {'Call PDE':>12} {'Error':>12} {'Time (s)':>10}")
    print(f"  {'-'*54}")

    for ns, nt in grid_sizes:
        pricer_tmp = BS_pricer(S0, K, T, r, sigma, payoff="call", exercise="European")
        pde_val, pde_t = pricer_tmp.PDE_price((ns, nt), Time=True)
        err = abs(pde_val - call_cf)
        print(f"  {ns:>8} {nt:>8} {pde_val:>12.6f} {err:>12.6f} {pde_t:>10.4f}")

    # Run a fine-grid PDE for the put as well (used for plotting later)
    fine_ns, fine_nt = 5000, 2500
    put_pde_val, put_pde_t = put_pricer.PDE_price((fine_ns, fine_nt), Time=True)
    call_pde_val, _ = call_pricer.PDE_price((fine_ns, fine_nt), Time=True)

    print(f"\n  Fine-grid ({fine_ns} x {fine_nt}):")
    print(f"    Call PDE = {call_pde_val:.6f}   (error = {abs(call_pde_val - call_cf):.2e})")
    print(f"    Put  PDE = {put_pde_val:.6f}   (error = {abs(put_pde_val - put_cf):.2e})")

    # ------------------------------------------------------------------
    # D. American put via Longstaff-Schwartz
    # ------------------------------------------------------------------
    print("\n" + "-" * 75)
    print("D. AMERICAN PUT -- LONGSTAFF-SCHWARTZ METHOD (LSM)")
    print("-" * 75)

    np.random.seed(42)
    am_pricer = BS_pricer(S0, K, T, r, sigma, payoff="put", exercise="American")

    # Run LSM several times to show variability
    n_runs = 5
    lsm_prices = []
    print(f"\n  LSM parameters: N_steps=10000, paths=50000, poly_order=2")
    print(f"  Running {n_runs} independent trials ...\n")

    for run in range(1, n_runs + 1):
        lsm_val = am_pricer.LSM(N=10_000, paths=50_000, order=2)
        lsm_prices.append(lsm_val)
        print(f"    Trial {run}: American Put = {lsm_val:.6f}")

    lsm_mean = np.mean(lsm_prices)
    lsm_std  = np.std(lsm_prices, ddof=1)

    print(f"\n  LSM mean   = {lsm_mean:.6f}")
    print(f"  LSM std    = {lsm_std:.6f}")
    print(f"  European put (closed-form) = {put_cf:.6f}")
    print(f"  Early-exercise premium     ~ {lsm_mean - put_cf:.6f}")

    # Also price American put via PDE for comparison
    am_pde_pricer = BS_pricer(S0, K, T, r, sigma, payoff="put", exercise="American")
    am_pde_val = am_pde_pricer.PDE_price((5000, 2500))
    print(f"\n  American put via PDE (5000x2500) = {am_pde_val:.6f}")
    print(f"  PDE early-exercise premium       = {am_pde_val - put_cf:.6f}")

    # ------------------------------------------------------------------
    # E. Summary comparison table
    # ------------------------------------------------------------------
    print("\n" + "=" * 75)
    print("E. SUMMARY -- ALL METHODS")
    print("=" * 75)

    header = (
        f"  {'Method':<28} {'Call':>12} {'Put':>12} {'Am. Put':>12}"
    )
    print(header)
    print(f"  {'-' * 66}")

    print(f"  {'Closed-form (exact)':<28} {call_cf:>12.6f} {put_cf:>12.6f} {'n/a':>12}")
    print(f"  {'Monte Carlo (500k paths)':<28} {call_mc:>12.6f} {put_mc:>12.6f} {'n/a':>12}")
    print(f"  {'PDE implicit (5000x2500)':<28} {call_pde_val:>12.6f} {put_pde_val:>12.6f} {am_pde_val:>12.6f}")
    print(f"  {'LSM (50k paths, mean)':<28} {'n/a':>12} {'n/a':>12} {lsm_mean:>12.6f}")
    print(f"  {'-' * 66}")

    print("\n  Observations:")
    print(f"    - MC and PDE converge to the closed-form for European options.")
    print(f"    - American put > European put by the early-exercise premium.")
    print(f"    - LSM and PDE American prices should be close; LSM has")
    print(f"      simulation noise while PDE has discretisation error.")

    # ------------------------------------------------------------------
    # F. Plot: payoff vs BS price curve (European call)
    # ------------------------------------------------------------------
    print("\n" + "-" * 75)
    print("F. PLOT -- Payoff vs Black-Scholes Price Curve (European Call)")
    print("-" * 75)
    print("  (Close the plot window to continue.)\n")

    call_pricer.plot(axis=[0, 3 * K, -5, K])

    print("\n" + "=" * 75)
    print("  Demo complete.")
    print("=" * 75)


if __name__ == "__main__":
    main()
