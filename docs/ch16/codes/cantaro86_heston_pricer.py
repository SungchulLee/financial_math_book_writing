# -*- coding: utf-8 -*-
"""
cantaro86_heston_pricer.py

Heston Stochastic Volatility Model: Pricing via Fourier Inversion,
Fast Fourier Transform (FFT), and Monte Carlo Simulation.

This self-contained educational module combines and adapts material from
cantaro86's "Financial Models Numerical Methods" (FMNM) library:
  - CF.py            : Heston characteristic function (Schoutens formulation)
  - probabilities.py : Risk-neutral probabilities Q1, Q2 via Fourier inversion
  - FFT.py           : Lewis (2001) FFT pricing and implied-volatility extraction
  - Heston_pricer.py : Orchestration class for Fourier, FFT, and Monte Carlo
  - heston.pyx       : Cython Euler scheme (re-implemented in pure NumPy here)

Original author: cantaro86
Repository: https://github.com/cantaro86/Financial-Models-Numerical-Methods
License: MIT

Adapted for the Quantitative Finance with Python course, Chapter 16.
"""

import numpy as np
from scipy.integrate import quad
from scipy.fftpack import ifft
from scipy.interpolate import interp1d
from scipy.optimize import fsolve
from scipy.stats import sem
from time import time
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt


# ============================================================================
# 1. Heston Characteristic Function -- Schoutens (2004) formulation
# ============================================================================

def cf_heston_good(u, t, v0, mu, kappa, theta, sigma, rho):
    """
    Heston characteristic function using the numerically stable formulation
    proposed by Schoutens (2004).

    The Heston (1993) model specifies the risk-neutral dynamics:

        dS / S  = mu dt + sqrt(v) dW_S
        dv      = kappa (theta - v) dt + sigma sqrt(v) dW_v
        dW_S dW_v = rho dt

    The characteristic function phi(u) = E[exp(i u X_t)] of the log-price
    X_t = ln(S_t) is computed using the "good" formulation that avoids the
    branch-cut discontinuity present in Heston's original paper.

    Parameters
    ----------
    u : float or ndarray
        Fourier variable.
    t : float
        Time to maturity.
    v0 : float
        Initial (spot) variance.
    mu : float
        Risk-neutral drift (typically the risk-free rate r).
    kappa : float
        Mean-reversion speed of the variance process.
    theta : float
        Long-run variance level.
    sigma : float
        Volatility of variance (vol-of-vol).
    rho : float
        Correlation between the two Brownian motions.

    Returns
    -------
    complex or ndarray of complex
        Value(s) of the characteristic function at u.
    """
    xi = kappa - sigma * rho * u * 1j
    d = np.sqrt(xi**2 + sigma**2 * (u**2 + 1j * u))
    g1 = (xi + d) / (xi - d)
    g2 = 1.0 / g1

    cf = np.exp(
        1j * u * mu * t
        + (kappa * theta)
        / (sigma**2)
        * ((xi - d) * t - 2.0 * np.log((1 - g2 * np.exp(-d * t)) / (1 - g2)))
        + (v0 / sigma**2)
        * (xi - d)
        * (1 - np.exp(-d * t))
        / (1 - g2 * np.exp(-d * t))
    )
    return cf


# ============================================================================
# 2. Risk-Neutral Probabilities Q1 and Q2 (Fourier Inversion)
# ============================================================================

def Q1(k, cf, right_lim):
    """
    Probability of finishing in-the-money under the *stock numeraire*.

    Computes  P_1 = 1/2 + 1/pi int_0^{inf} Re[ e^{-iuk} phi(u-i) / (iu phi(-i)) ] du

    This is used in the decomposition of the European call price:
        C = S0 * Q1  -  K * exp(-rT) * Q2

    Parameters
    ----------
    k : float
        Log-moneyness ln(K / S0).
    cf : callable
        Characteristic function phi(u) of the log-price.
    right_lim : float
        Upper integration limit (e.g. 2000).

    Returns
    -------
    float
        The Q1 probability.
    """

    def integrand(u):
        return np.real(
            (np.exp(-u * k * 1j) / (u * 1j))
            * cf(u - 1j)
            / cf(-1.0000000000001j)
        )

    return 0.5 + (1.0 / np.pi) * quad(integrand, 1e-15, right_lim, limit=2000)[0]


def Q2(k, cf, right_lim):
    """
    Probability of finishing in-the-money under the *money-market numeraire*.

    Computes  P_2 = 1/2 + 1/pi int_0^{inf} Re[ e^{-iuk} phi(u) / (iu) ] du

    Parameters
    ----------
    k : float
        Log-moneyness ln(K / S0).
    cf : callable
        Characteristic function phi(u) of the log-price.
    right_lim : float
        Upper integration limit (e.g. 2000).

    Returns
    -------
    float
        The Q2 probability.
    """

    def integrand(u):
        return np.real(np.exp(-u * k * 1j) / (u * 1j) * cf(u))

    return 0.5 + (1.0 / np.pi) * quad(integrand, 1e-15, right_lim, limit=2000)[0]


# ============================================================================
# 3. FFT Pricing via Lewis (2001) Formula
# ============================================================================

def fft_lewis(K, S0, r, T, cf, interp="cubic"):
    """
    Price a vector of European call options using the FFT-based approach
    derived from Lewis (2001).

    The Lewis representation expresses the call price as:
        C(K) = S0 - sqrt(S0 K) exp(-rT) / pi * I(ln(S0/K))
    where I(.) is evaluated efficiently via IFFT on a regular grid and then
    interpolated to the desired strike values.

    Parameters
    ----------
    K : float or ndarray
        Strike price(s).
    S0 : float
        Spot price.
    r : float
        Risk-free interest rate.
    T : float
        Time to maturity.
    cf : callable
        Characteristic function of the log-price.
    interp : str, optional
        Interpolation method: "cubic" (default) or "linear".

    Returns
    -------
    ndarray
        European call price(s) for each strike in K.
    """
    K = np.asarray(K, dtype=float)
    N = 2**15  # FFT is most efficient when N is a power of 2
    B = 500  # integration upper limit in Fourier space
    dx = B / N
    x = np.arange(N) * dx  # grid in Fourier space (excludes B)

    # Simpson's rule weights
    weight = 3 + (-1) ** (np.arange(N) + 1)
    weight[0] = 1
    weight[N - 1] = 1

    # Build the log-strike grid via the FFT relationship
    dk = 2 * np.pi / B
    b = N * dk / 2
    ks = -b + dk * np.arange(N)

    # Construct the integrand and apply IFFT
    integrand = (
        np.exp(-1j * b * np.arange(N) * dx)
        * cf(x - 0.5j)
        * 1.0
        / (x**2 + 0.25)
        * weight
        * dx
        / 3
    )
    integral_value = np.real(ifft(integrand) * N)

    # Interpolate to the requested strikes
    if interp == "linear":
        spline = interp1d(ks, integral_value, kind="linear")
    else:
        spline = interp1d(ks, integral_value, kind="cubic")

    prices = S0 - np.sqrt(S0 * K) * np.exp(-r * T) / np.pi * spline(np.log(S0 / K))
    return prices


# ============================================================================
# 4. Implied Volatility Extraction via Lewis Formula
# ============================================================================

def iv_from_lewis(K, S0, T, r, cf, disp=False):
    """
    Extract the Black-Scholes implied volatility for a European call by
    matching the Lewis (2001) Fourier integral representation of the Heston
    price to the corresponding Black-Scholes integral.

    The method solves for sigma_BS such that the Lewis integrals for the
    Heston model and for Black-Scholes coincide.

    Parameters
    ----------
    K : float
        Strike price.
    S0 : float
        Spot price.
    T : float
        Time to maturity.
    r : float
        Risk-free interest rate.
    cf : callable
        Characteristic function of the Heston log-price.
    disp : bool, optional
        If True, print a diagnostic message when the solver fails.

    Returns
    -------
    float
        Black-Scholes implied volatility, or -1 if solver fails.
    """
    k = np.log(S0 / K)

    def obj_fun(sig):
        integrand = lambda u: np.real(
            np.exp(u * k * 1j)
            * (
                cf(u - 0.5j)
                - np.exp(1j * u * r * T + 0.5 * r * T)
                * np.exp(-0.5 * T * (u**2 + 0.25) * sig**2)
            )
            * 1.0
            / (u**2 + 0.25)
        )
        int_value = quad(integrand, 1e-15, 2000, limit=2000, full_output=1)[0]
        return int_value

    # Try several initial guesses to improve robustness
    for x0 in [0.2, 1.0, 2.0, 4.0, 0.0001]:
        x, _, solved, msg = fsolve(obj_fun, [x0], full_output=True, xtol=1e-4)
        if solved == 1:
            return x[0]

    if disp:
        print(f"IV solve failed at strike K={K}: {msg}")
    return -1.0


# ============================================================================
# 5. Heston Euler Monte Carlo (Pure NumPy -- replaces Cython version)
# ============================================================================

def heston_euler_mc(N, paths, T, S0, v0, mu, rho, kappa, theta, sigma):
    """
    Simulate terminal stock price S(T) and variance v(T) under the Heston
    model using an Euler-Maruyama discretisation with the *reflection*
    (absolute value) scheme for the variance process.

    The discretisation is:
        v_{t+1} = | v_t + kappa (theta - v_t) dt + sigma sqrt(v_t) sqrt(dt) Z_v |
        S_{t+1} = S_t exp[ (mu - 0.5 v_t) dt + sqrt(v_t) sqrt(dt) Z_S ]

    where Z_S, Z_v are correlated standard normals with correlation rho.

    Parameters
    ----------
    N : int
        Number of time steps.
    paths : int
        Number of Monte Carlo paths.
    T : float
        Time to maturity.
    S0 : float
        Spot price.
    v0 : float
        Spot variance.
    mu : float
        Risk-neutral drift (risk-free rate).
    rho : float
        Correlation between stock and variance Brownian motions.
    kappa : float
        Mean-reversion speed.
    theta : float
        Long-run variance.
    sigma : float
        Vol-of-vol.

    Returns
    -------
    S_T : ndarray, shape (paths,)
        Terminal stock prices.
    v_T : ndarray, shape (paths,)
        Terminal variance values.
    """
    dt = T / (N - 1)
    dt_sq = np.sqrt(dt)

    # Pre-allocate terminal values
    S_T = np.zeros(paths)
    v_T = np.zeros(paths)

    for p in range(paths):
        # Correlated Brownian increments
        Z_S = np.random.standard_normal(N - 1)
        Z_v = rho * Z_S + np.sqrt(1 - rho**2) * np.random.standard_normal(N - 1)

        S = S0
        v = v0
        for t in range(N - 1):
            # Reflection scheme: take abs() to keep variance non-negative
            v_new = np.abs(
                v + kappa * (theta - v) * dt + sigma * np.sqrt(v) * dt_sq * Z_v[t]
            )
            S = S * np.exp((mu - 0.5 * v) * dt + np.sqrt(v) * dt_sq * Z_S[t])
            v = v_new

        S_T[p] = S
        v_T[p] = v

    return S_T, v_T


# ============================================================================
# 6. Heston Pricer: Unified Interface
# ============================================================================

class HestonPricer:
    """
    Unified pricer for European options under the Heston stochastic
    volatility model.

    Supported pricing methods:
        - fourier_inversion() : Semi-analytical via Q1/Q2 decomposition.
        - fft(K_vec)          : FFT-based pricing over a vector of strikes.
        - monte_carlo(...)    : Euler Monte Carlo with reflection scheme.
        - implied_vol_lewis() : Black-Scholes implied vol from Lewis formula.

    Parameters
    ----------
    S0 : float
        Spot price.
    K : float
        Strike price (scalar, used by Fourier inversion and MC).
    T : float
        Time to maturity in years.
    r : float
        Risk-free interest rate.
    v0 : float
        Spot variance.
    kappa : float
        Mean-reversion speed.
    theta : float
        Long-run variance.
    sigma : float
        Vol-of-vol.
    rho : float
        Correlation between stock and variance Brownian motions.
    payoff : str
        "call" or "put".
    """

    def __init__(self, S0, K, T, r, v0, kappa, theta, sigma, rho, payoff="call"):
        self.S0 = S0
        self.K = K
        self.T = T
        self.r = r
        self.v0 = v0
        self.kappa = kappa
        self.theta = theta
        self.sigma = sigma
        self.rho = rho
        self.payoff = payoff

    def _cf(self, u):
        """Bound characteristic function with the instance's Heston parameters."""
        return cf_heston_good(
            u,
            t=self.T,
            v0=self.v0,
            mu=self.r,
            kappa=self.kappa,
            theta=self.theta,
            sigma=self.sigma,
            rho=self.rho,
        )

    # ------------------------------------------------------------------
    # Fourier inversion
    # ------------------------------------------------------------------
    def fourier_inversion(self):
        """
        Price via semi-analytical Fourier inversion of the characteristic
        function using the Q1/Q2 probability decomposition.

        Call = S0 * Q1 - K * exp(-rT) * Q2
        Put  = K * exp(-rT) * (1 - Q2) - S0 * (1 - Q1)

        Returns
        -------
        float
            European option price.
        """
        k = np.log(self.K / self.S0)  # log-moneyness
        limit_max = 2000

        if self.payoff == "call":
            price = (
                self.S0 * Q1(k, self._cf, limit_max)
                - self.K * np.exp(-self.r * self.T) * Q2(k, self._cf, limit_max)
            )
        elif self.payoff == "put":
            price = (
                self.K * np.exp(-self.r * self.T) * (1 - Q2(k, self._cf, limit_max))
                - self.S0 * (1 - Q1(k, self._cf, limit_max))
            )
        else:
            raise ValueError("payoff must be 'call' or 'put'")
        return price

    # ------------------------------------------------------------------
    # FFT pricing
    # ------------------------------------------------------------------
    def fft(self, K_vec):
        """
        FFT-based pricing over a vector of strikes using Lewis (2001).

        For puts, the call prices are obtained first and then converted
        via put-call parity.

        Parameters
        ----------
        K_vec : array-like
            Vector of strike prices.

        Returns
        -------
        ndarray
            Option prices for each strike.
        """
        K_vec = np.asarray(K_vec, dtype=float)

        if self.payoff == "call":
            return fft_lewis(K_vec, self.S0, self.r, self.T, self._cf, interp="cubic")
        elif self.payoff == "put":
            call_prices = fft_lewis(
                K_vec, self.S0, self.r, self.T, self._cf, interp="cubic"
            )
            return call_prices - self.S0 + K_vec * np.exp(-self.r * self.T)
        else:
            raise ValueError("payoff must be 'call' or 'put'")

    # ------------------------------------------------------------------
    # Monte Carlo
    # ------------------------------------------------------------------
    def monte_carlo(self, n_steps=500, n_paths=100000):
        """
        Price via Euler Monte Carlo with the reflection scheme.

        Parameters
        ----------
        n_steps : int
            Number of time steps per path.
        n_paths : int
            Number of simulated paths.

        Returns
        -------
        price : float
            Discounted Monte Carlo estimate of the option price.
        std_err : float
            Standard error of the Monte Carlo estimate.
        elapsed : float
            Wall-clock time in seconds.
        """
        t0 = time()

        S_T, _ = heston_euler_mc(
            N=n_steps,
            paths=n_paths,
            T=self.T,
            S0=self.S0,
            v0=self.v0,
            mu=self.r,
            rho=self.rho,
            kappa=self.kappa,
            theta=self.theta,
            sigma=self.sigma,
        )

        # Compute discounted payoff
        if self.payoff == "call":
            payoffs = np.maximum(S_T - self.K, 0.0)
        elif self.payoff == "put":
            payoffs = np.maximum(self.K - S_T, 0.0)
        else:
            raise ValueError("payoff must be 'call' or 'put'")

        discounted = np.exp(-self.r * self.T) * payoffs
        price = np.mean(discounted)
        std_err = sem(discounted)
        elapsed = time() - t0

        return price, std_err, elapsed

    # ------------------------------------------------------------------
    # Implied volatility
    # ------------------------------------------------------------------
    def implied_vol_lewis(self, K_scalar=None):
        """
        Extract the Black-Scholes implied volatility for a European call
        using the Lewis (2001) integral matching approach.

        Parameters
        ----------
        K_scalar : float, optional
            Strike to evaluate. If None, uses self.K.

        Returns
        -------
        float
            Implied volatility (annualised), or -1 if the solver fails.
        """
        K_eval = K_scalar if K_scalar is not None else self.K
        return iv_from_lewis(K_eval, self.S0, self.T, self.r, self._cf, disp=True)


# ============================================================================
# 7. Main Demo
# ============================================================================

def main():
    """
    Comprehensive demonstration of the Heston pricer.

    Steps
    -----
    1. Set up Heston model parameters.
    2. Price a European call via Fourier inversion.
    3. Price the same call via Monte Carlo (with standard error).
    4. Price across a vector of strikes using FFT.
    5. Extract the Heston implied-volatility smile.
    6. Plot the smile and compare pricing methods.
    """
    print("=" * 72)
    print("  Heston Stochastic Volatility Model -- Pricing Demo")
    print("  (Based on cantaro86, Financial Models Numerical Methods)")
    print("=" * 72)

    # ------------------------------------------------------------------
    # Step 1: Heston parameters
    # ------------------------------------------------------------------
    S0 = 100.0        # spot price
    K_atm = 100.0     # at-the-money strike
    T = 1.0            # maturity (1 year)
    r = 0.05           # risk-free rate

    v0 = 0.04          # spot variance
    kappa = 1.5        # mean-reversion speed
    theta = 0.04       # long-run variance
    sigma = 0.3        # vol-of-vol
    rho = -0.7         # correlation (negative skew)

    # Feller condition check
    feller = 2 * kappa * theta - sigma**2
    print(f"\nHeston parameters:")
    print(f"  S0={S0}, K={K_atm}, T={T}, r={r}")
    print(f"  v0={v0}, kappa={kappa}, theta={theta}, sigma={sigma}, rho={rho}")
    print(f"  Feller condition: 2*kappa*theta - sigma^2 = {feller:.4f}",
          "(satisfied)" if feller > 0 else "(NOT satisfied -- variance can hit zero)")

    # ------------------------------------------------------------------
    # Step 2: Fourier inversion pricing
    # ------------------------------------------------------------------
    print("\n" + "-" * 72)
    print("  Fourier Inversion Pricing (Q1/Q2 Decomposition)")
    print("-" * 72)

    pricer_call = HestonPricer(
        S0=S0, K=K_atm, T=T, r=r,
        v0=v0, kappa=kappa, theta=theta, sigma=sigma, rho=rho,
        payoff="call",
    )
    pricer_put = HestonPricer(
        S0=S0, K=K_atm, T=T, r=r,
        v0=v0, kappa=kappa, theta=theta, sigma=sigma, rho=rho,
        payoff="put",
    )

    call_fourier = pricer_call.fourier_inversion()
    put_fourier = pricer_put.fourier_inversion()

    # Verify put-call parity: C - P = S0 - K * exp(-rT)
    parity_lhs = call_fourier - put_fourier
    parity_rhs = S0 - K_atm * np.exp(-r * T)

    print(f"  Call price (Fourier):  {call_fourier:.6f}")
    print(f"  Put  price (Fourier):  {put_fourier:.6f}")
    print(f"  Put-call parity check: C - P = {parity_lhs:.6f},  "
          f"S0 - K*exp(-rT) = {parity_rhs:.6f},  "
          f"error = {abs(parity_lhs - parity_rhs):.2e}")

    # ------------------------------------------------------------------
    # Step 3: Monte Carlo pricing
    # ------------------------------------------------------------------
    print("\n" + "-" * 72)
    print("  Monte Carlo Pricing (Euler scheme, reflection for variance)")
    print("-" * 72)

    np.random.seed(42)
    mc_price, mc_se, mc_time = pricer_call.monte_carlo(n_steps=500, n_paths=100000)

    print(f"  Call price (MC):       {mc_price:.6f}")
    print(f"  Standard error:        {mc_se:.6f}")
    print(f"  95% confidence:        [{mc_price - 1.96*mc_se:.6f}, "
          f"{mc_price + 1.96*mc_se:.6f}]")
    print(f"  Wall-clock time:       {mc_time:.2f} s")
    print(f"  Fourier vs MC diff:    {abs(call_fourier - mc_price):.6f}")

    # ------------------------------------------------------------------
    # Step 4: FFT pricing across a vector of strikes
    # ------------------------------------------------------------------
    print("\n" + "-" * 72)
    print("  FFT Pricing (Lewis 2001) Across Strikes")
    print("-" * 72)

    K_vec = np.arange(80, 121, 2.0)
    fft_prices = pricer_call.fft(K_vec)

    print(f"  {'Strike':>8s}  {'FFT Call':>10s}")
    print(f"  {'------':>8s}  {'--------':>10s}")
    for k_i, p_i in zip(K_vec, fft_prices):
        print(f"  {k_i:8.1f}  {p_i:10.6f}")

    # ------------------------------------------------------------------
    # Step 5: Implied volatility smile
    # ------------------------------------------------------------------
    print("\n" + "-" * 72)
    print("  Implied Volatility Smile Extraction (Lewis formula)")
    print("-" * 72)

    K_smile = np.arange(80, 121, 2.0)
    iv_smile = []
    for k_i in K_smile:
        iv_val = pricer_call.implied_vol_lewis(K_scalar=k_i)
        iv_smile.append(iv_val)

    iv_smile = np.array(iv_smile)

    print(f"  {'Strike':>8s}  {'IV (%)':>10s}")
    print(f"  {'------':>8s}  {'------':>10s}")
    for k_i, iv_i in zip(K_smile, iv_smile):
        if iv_i > 0:
            print(f"  {k_i:8.1f}  {iv_i*100:10.4f}")
        else:
            print(f"  {k_i:8.1f}  {'FAILED':>10s}")

    # ------------------------------------------------------------------
    # Step 6: Comparison of pricing methods
    # ------------------------------------------------------------------
    print("\n" + "-" * 72)
    print("  Method Comparison at ATM Strike K = 100")
    print("-" * 72)

    # FFT price at K=100
    fft_atm = pricer_call.fft(np.array([K_atm]))[0]

    print(f"  {'Method':<25s}  {'Price':>10s}")
    print(f"  {'-'*25:<25s}  {'-'*10:>10s}")
    print(f"  {'Fourier inversion':<25s}  {call_fourier:10.6f}")
    print(f"  {'FFT (Lewis)':<25s}  {fft_atm:10.6f}")
    print(f"  {'Monte Carlo (100k paths)':<25s}  {mc_price:10.6f}")

    # ------------------------------------------------------------------
    # Step 7: Plot implied volatility smile
    # ------------------------------------------------------------------
    valid = iv_smile > 0
    if np.any(valid):
        fig, axes = plt.subplots(1, 2, figsize=(14, 5))

        # Left panel: IV smile
        ax1 = axes[0]
        ax1.plot(
            K_smile[valid],
            iv_smile[valid] * 100,
            "b-o",
            markersize=4,
            linewidth=1.5,
            label="Heston IV smile",
        )
        ax1.axvline(S0, color="gray", linestyle="--", alpha=0.5, label=f"Spot S0={S0}")
        ax1.set_xlabel("Strike (K)")
        ax1.set_ylabel("Implied Volatility (%)")
        ax1.set_title("Heston Implied Volatility Smile")
        ax1.legend()
        ax1.grid(True, alpha=0.3)

        # Right panel: FFT call prices vs strikes
        ax2 = axes[1]
        ax2.plot(
            K_vec,
            fft_prices,
            "r-s",
            markersize=4,
            linewidth=1.5,
            label="FFT call prices",
        )
        ax2.axvline(S0, color="gray", linestyle="--", alpha=0.5, label=f"Spot S0={S0}")
        ax2.set_xlabel("Strike (K)")
        ax2.set_ylabel("Call Price")
        ax2.set_title("Heston Call Prices via FFT")
        ax2.legend()
        ax2.grid(True, alpha=0.3)

        plt.tight_layout()
        fig_path = "/tmp/cantaro86_heston_pricer.png"
        plt.savefig(fig_path, dpi=150)
        print(f"\n  Figure saved to {fig_path}")
        plt.close()
    else:
        print("\n  WARNING: No valid implied volatilities were extracted; skipping plot.")

    print("\n" + "=" * 72)
    print("  Demo complete.")
    print("=" * 72)


if __name__ == "__main__":
    main()
