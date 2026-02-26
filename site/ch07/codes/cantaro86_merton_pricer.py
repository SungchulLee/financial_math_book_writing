"""
Merton Jump-Diffusion Option Pricer -- Five Methods Compared.

This standalone educational module prices European options under the Merton
jump-diffusion model using five complementary approaches:

    1. Closed-form series  (sum of BS prices weighted by Poisson probabilities)
    2. Fourier inversion    (Gil-Pelaez via the characteristic function)
    3. FFT pricing          (Lewis formula evaluated on a strike grid)
    4. Monte Carlo          (Poisson jumps + log-normal jump sizes)
    5. PIDE solver          (implicit finite-difference + convolution for jumps)

It also extracts the jump-diffusion implied volatility smile via the Lewis
integral representation.

The code is adapted from the FMNM library by cantaro86:

    cantaro86, "Financial Models Numerical Methods"
    https://github.com/cantaro86/Financial-Models-Numerical-Methods

Original source files: Merton_pricer.py, CF.py, probabilities.py,
BS_pricer.py, FFT.py  (all (c) cantaro86, MIT licence).

All helper functions (Black-Scholes formula, characteristic function,
Q1/Q2 probabilities, fft_Lewis, IV_from_Lewis) are inlined below so that
this script is fully self-contained -- no external FMNM imports are needed.
"""

import numpy as np
import scipy.stats as ss
from math import factorial
from functools import partial
from scipy import sparse, signal
from scipy.sparse.linalg import splu
from scipy.fftpack import ifft
from scipy.interpolate import interp1d
from scipy.integrate import quad
from scipy.optimize import fsolve
import matplotlib.pyplot as plt


# ============================================================================
# 1.  Inlined helpers -- Black-Scholes, characteristic function, transforms
# ============================================================================

def bs_price(payoff, S0, K, T, r, sigma):
    """
    Black-Scholes closed-form price for a European call or put.

    Parameters
    ----------
    payoff : str
        "call" or "put".
    S0 : float
        Current underlying price.
    K : float
        Strike price.
    T : float
        Time to maturity (years).
    r : float
        Risk-free interest rate (annualised).
    sigma : float
        Volatility of the underlying (annualised).

    Returns
    -------
    float
        Option price.
    """
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if payoff == "call":
        return S0 * ss.norm.cdf(d1) - K * np.exp(-r * T) * ss.norm.cdf(d2)
    elif payoff == "put":
        return K * np.exp(-r * T) * ss.norm.cdf(-d2) - S0 * ss.norm.cdf(-d1)
    else:
        raise ValueError("payoff must be 'call' or 'put'")


def bs_vega(sigma, S0, K, T, r):
    """
    Black-Scholes vega (derivative of price w.r.t. volatility).

    Used internally by the implied-volatility solver.
    """
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    return S0 * np.sqrt(T) * ss.norm.pdf(d1)


def cf_merton(u, t, mu, sig, lam, muJ, sigJ):
    r"""
    Characteristic function of the log-price X_t under the Merton model.

    .. math::
        \phi(u) = \exp\!\bigl[
            t\bigl(i u \mu - \tfrac12 u^2 \sigma^2
            + \lambda(e^{i u \mu_J - \frac12 u^2 \sigma_J^2} - 1)\bigr)
        \bigr]

    Parameters
    ----------
    u : float or ndarray
        Fourier variable.
    t : float
        Time horizon.
    mu : float
        Drift of the continuous component (risk-neutral: r - 0.5*sig^2 - m).
    sig : float
        Diffusion volatility.
    lam : float
        Jump intensity (Poisson rate).
    muJ : float
        Mean of the (normal) log-jump size.
    sigJ : float
        Std dev of the (normal) log-jump size.

    Returns
    -------
    complex or ndarray of complex
    """
    return np.exp(
        t * (
            1j * u * mu
            - 0.5 * u ** 2 * sig ** 2
            + lam * (np.exp(1j * u * muJ - 0.5 * u ** 2 * sigJ ** 2) - 1)
        )
    )


def Q1(k, cf, right_lim):
    """
    Probability of finishing in-the-money under the *stock* numeraire.

    Computed via Gil-Pelaez inversion of the characteristic function.

    Parameters
    ----------
    k : float
        Log-moneyness  ln(K / S0).
    cf : callable
        Characteristic function  cf(u).
    right_lim : float
        Upper integration limit (use np.inf for full integral).
    """
    def integrand(u):
        return np.real(
            (np.exp(-u * k * 1j) / (u * 1j))
            * cf(u - 1j) / cf(-1.0000000000001j)
        )
    return 0.5 + (1.0 / np.pi) * quad(integrand, 1e-15, right_lim, limit=2000)[0]


def Q2(k, cf, right_lim):
    """
    Probability of finishing in-the-money under the *money-market* numeraire.

    Parameters
    ----------
    k : float
        Log-moneyness  ln(K / S0).
    cf : callable
        Characteristic function  cf(u).
    right_lim : float
        Upper integration limit.
    """
    def integrand(u):
        return np.real(
            np.exp(-u * k * 1j) / (u * 1j) * cf(u)
        )
    return 0.5 + (1.0 / np.pi) * quad(integrand, 1e-15, right_lim, limit=2000)[0]


def fft_Lewis(K, S0, r, T, cf, interp="cubic"):
    """
    Price a European call for a *vector* of strikes using the FFT / Lewis
    representation.

    Parameters
    ----------
    K : ndarray
        Vector of strike prices.
    S0 : float
        Spot price.
    r : float
        Risk-free rate.
    T : float
        Time to maturity.
    cf : callable
        Characteristic function of the log-price.
    interp : str
        Interpolation scheme ("cubic" or "linear").

    Returns
    -------
    ndarray
        Call prices corresponding to each strike in K.
    """
    N = 2 ** 15                          # FFT size (power of 2 for speed)
    B = 500                              # integration upper bound
    dx = B / N
    x = np.arange(N) * dx

    # Simpson weights
    weight = 3 + (-1) ** (np.arange(N) + 1)
    weight[0] = 1
    weight[N - 1] = 1

    dk = 2 * np.pi / B
    b = N * dk / 2
    ks = -b + dk * np.arange(N)

    integrand = (
        np.exp(-1j * b * np.arange(N) * dx)
        * cf(x - 0.5j)
        * 1.0 / (x ** 2 + 0.25)
        * weight * dx / 3
    )
    integral_value = np.real(ifft(integrand) * N)

    spline = interp1d(ks, integral_value, kind=interp)
    prices = S0 - np.sqrt(S0 * K) * np.exp(-r * T) / np.pi * spline(np.log(S0 / K))
    return prices


def IV_from_Lewis(K, S0, T, r, cf, disp=False):
    """
    Extract the Black-Scholes implied volatility that matches the Merton
    price for strike *K*, using the Lewis integral representation.

    Parameters
    ----------
    K : float
        Strike price (scalar).
    S0 : float
        Spot price.
    T : float
        Time to maturity.
    r : float
        Risk-free rate.
    cf : callable
        Characteristic function of the Merton log-price.
    disp : bool
        Print diagnostics on failure.

    Returns
    -------
    float
        Implied volatility, or -1 if the solver fails.
    """
    k = np.log(S0 / K)

    def obj_fun(sig):
        integrand = (
            lambda u: np.real(
                np.exp(u * k * 1j)
                * (
                    cf(u - 0.5j)
                    - np.exp(1j * u * r * T + 0.5 * r * T)
                      * np.exp(-0.5 * T * (u ** 2 + 0.25) * sig ** 2)
                )
            )
            * 1.0 / (u ** 2 + 0.25)
        )
        return quad(integrand, 1e-15, 2000, limit=2000, full_output=1)[0]

    for x0 in [0.2, 1.0, 2.0, 4.0, 0.0001]:
        x, _, solved, msg = fsolve(obj_fun, [x0], full_output=True, xtol=1e-4)
        if solved == 1:
            return x[0]
    if disp:
        print("Strike", K, msg)
    return -1


# ============================================================================
# 2.  Merton closed-form series
# ============================================================================

def merton_closed_formula(S0, K, T, r, sig, lam, muJ, sigJ,
                          payoff="call", n_terms=18):
    r"""
    Merton closed-form option price via a Poisson-weighted sum of
    Black-Scholes prices.

    The price is

    .. math::
        V = \sum_{n=0}^{N}
            \frac{e^{-\lambda' T}(\lambda' T)^n}{n!}\;
            \mathrm{BS}\!\bigl(S_0, K, T, r_n, \sigma_n\bigr)

    where

    * :math:`\lambda' = \lambda \exp(\mu_J + \sigma_J^2/2)`,
    * :math:`r_n = r - m + n(\mu_J + \sigma_J^2/2)/T`,
    * :math:`\sigma_n = \sqrt{\sigma^2 + n\sigma_J^2/T}`,
    * :math:`m = \lambda(e^{\mu_J + \sigma_J^2/2} - 1)`.

    Parameters
    ----------
    S0, K, T, r, sig : float
        Spot, strike, maturity, risk-free rate, diffusion vol.
    lam : float
        Jump intensity.
    muJ, sigJ : float
        Mean and std dev of the normal log-jump size.
    payoff : str
        "call" or "put".
    n_terms : int
        Number of terms retained in the infinite series.

    Returns
    -------
    float
        Option price.
    """
    # Compensator m and modified intensity lam'
    m = lam * (np.exp(muJ + 0.5 * sigJ ** 2) - 1)
    lam_prime = lam * np.exp(muJ + 0.5 * sigJ ** 2)

    price = 0.0
    for n in range(n_terms):
        # Poisson weight
        w_n = np.exp(-lam_prime * T) * (lam_prime * T) ** n / factorial(n)
        # Adjusted rate and volatility
        r_n = r - m + n * (muJ + 0.5 * sigJ ** 2) / T
        sig_n = np.sqrt(sig ** 2 + n * sigJ ** 2 / T)
        price += w_n * bs_price(payoff, S0, K, T, r_n, sig_n)
    return price


# ============================================================================
# 3.  Fourier-inversion pricing
# ============================================================================

def merton_fourier_inversion(S0, K, T, r, sig, lam, muJ, sigJ, payoff="call"):
    """
    Price a European option by direct inversion of the Merton characteristic
    function (Gil-Pelaez formula through Q1, Q2).

    Parameters
    ----------
    S0, K, T, r, sig, lam, muJ, sigJ : float
        Model parameters (see ``merton_closed_formula``).
    payoff : str
        "call" or "put".

    Returns
    -------
    float
        Option price.
    """
    k = np.log(K / S0)                       # log-moneyness
    m = lam * (np.exp(muJ + 0.5 * sigJ ** 2) - 1)

    cf_Mert = partial(
        cf_merton,
        t=T,
        mu=(r - 0.5 * sig ** 2 - m),
        sig=sig,
        lam=lam,
        muJ=muJ,
        sigJ=sigJ,
    )

    if payoff == "call":
        return (
            S0 * Q1(k, cf_Mert, np.inf)
            - K * np.exp(-r * T) * Q2(k, cf_Mert, np.inf)
        )
    elif payoff == "put":
        return (
            K * np.exp(-r * T) * (1 - Q2(k, cf_Mert, np.inf))
            - S0 * (1 - Q1(k, cf_Mert, np.inf))
        )
    else:
        raise ValueError("payoff must be 'call' or 'put'")


# ============================================================================
# 4.  FFT pricing across a vector of strikes
# ============================================================================

def merton_fft(S0, K_vec, T, r, sig, lam, muJ, sigJ, payoff="call"):
    """
    Price European calls (or puts via put-call parity) for many strikes at
    once using the FFT approach of Lewis.

    Parameters
    ----------
    K_vec : array-like
        Vector of strikes.
    payoff : str
        "call" or "put".

    Returns
    -------
    ndarray
        Option prices for each strike.
    """
    K_vec = np.asarray(K_vec, dtype=float)
    m = lam * (np.exp(muJ + 0.5 * sigJ ** 2) - 1)

    cf_Mert = partial(
        cf_merton,
        t=T,
        mu=(r - 0.5 * sig ** 2 - m),
        sig=sig,
        lam=lam,
        muJ=muJ,
        sigJ=sigJ,
    )

    call_prices = fft_Lewis(K_vec, S0, r, T, cf_Mert, interp="cubic")
    if payoff == "call":
        return call_prices
    elif payoff == "put":
        return call_prices - S0 + K_vec * np.exp(-r * T)
    else:
        raise ValueError("payoff must be 'call' or 'put'")


# ============================================================================
# 5.  Monte Carlo
# ============================================================================

def merton_mc(S0, K, T, r, sig, lam, muJ, sigJ, payoff="call",
              N_paths=200_000, seed=None):
    """
    Monte Carlo pricing of a European option under the Merton model.

    At each path the terminal stock price is generated *exactly* (no time
    discretisation) as

        S_T = S0 * exp[(r - m - 0.5*sig^2)*T + sig*sqrt(T)*Z
                       + sum_{j=1}^{N_T} J_j ]

    where N_T ~ Poisson(lam*T) and J_j ~ N(muJ, sigJ^2).

    Parameters
    ----------
    N_paths : int
        Number of Monte Carlo paths.
    seed : int or None
        Random seed for reproducibility.

    Returns
    -------
    price : float
        Discounted expected payoff.
    std_err : float
        Standard error of the Monte Carlo estimate.
    """
    rng = np.random.default_rng(seed)

    m = lam * (np.exp(muJ + 0.5 * sigJ ** 2) - 1)   # drift compensator

    # Diffusion component
    Z = rng.standard_normal(N_paths)

    # Jump component -- Poisson number of jumps per path
    N_jumps = rng.poisson(lam * T, N_paths)

    # Total jump sizes:  sum of N_jumps[i] i.i.d. N(muJ, sigJ^2) for path i
    # Efficient vectorised approach: sum of normals is normal
    jump_sum = np.array([
        rng.normal(muJ * nj, sigJ * np.sqrt(nj)) if nj > 0 else 0.0
        for nj in N_jumps
    ])

    # Terminal log-price
    log_ST = (
        np.log(S0)
        + (r - m - 0.5 * sig ** 2) * T
        + sig * np.sqrt(T) * Z
        + jump_sum
    )
    S_T = np.exp(log_ST)

    # Discounted payoff
    if payoff == "call":
        payoffs = np.maximum(S_T - K, 0)
    elif payoff == "put":
        payoffs = np.maximum(K - S_T, 0)
    else:
        raise ValueError("payoff must be 'call' or 'put'")

    disc_payoffs = np.exp(-r * T) * payoffs
    price = np.mean(disc_payoffs)
    std_err = np.std(disc_payoffs, ddof=1) / np.sqrt(N_paths)
    return price, std_err


# ============================================================================
# 6.  PIDE solver  (implicit in diffusion + explicit convolution for jumps)
# ============================================================================

def merton_pide(S0, K, T, r, sig, lam, muJ, sigJ, payoff="call",
                Nspace=500, Ntime=400):
    r"""
    Solve the Merton PIDE on a log-price grid via an implicit (in the
    differential part) / explicit (in the integral part) finite-difference
    scheme.

    The PIDE (in terms of x = ln S) reads

    .. math::
        0 = \frac{\partial V}{\partial t}
            + (r - m - \tfrac12\sigma^2)\frac{\partial V}{\partial x}
            + \tfrac12\sigma^2\frac{\partial^2 V}{\partial x^2}
            + \int_{-\infty}^{+\infty} \bigl[V(x+y) - V(x)\bigr]\,\nu(dy)
            - r\,V

    The jump integral is evaluated by discrete convolution (via
    ``scipy.signal.convolve``) which uses FFT internally.

    Parameters
    ----------
    Nspace : int
        Number of spatial grid points in the interior domain.
    Ntime : int
        Number of time steps.

    Returns
    -------
    price : float
        Interpolated option price at S0.
    S_vec : ndarray
        Interior spot-price grid (for plotting).
    price_vec : ndarray
        Option prices on the interior grid at t = 0 (for plotting).
    """
    # Domain in log-price space
    S_max = 6.0 * K
    S_min = K / 6.0
    x_max = np.log(S_max)
    x_min = np.log(S_min)

    # Measure of "how far" jumps can reach (used to set extra boundary points)
    dev_X = np.sqrt(lam * sigJ ** 2 + lam * muJ ** 2)

    dx = (x_max - x_min) / (Nspace - 1)
    extraP = int(np.floor(5.0 * dev_X / dx))     # extra points for convolution

    # Extended spatial grid
    x = np.linspace(
        x_min - extraP * dx,
        x_max + extraP * dx,
        Nspace + 2 * extraP,
    )
    t, dt = np.linspace(0, T, Ntime, retstep=True)

    # Terminal payoff on the full grid
    if payoff == "call":
        Payoff = np.maximum(np.exp(x) - K, 0)
    elif payoff == "put":
        Payoff = np.maximum(K - np.exp(x), 0)
    else:
        raise ValueError("payoff must be 'call' or 'put'")

    # Value grid  V[space, time]
    V = np.zeros((Nspace + 2 * extraP, Ntime))
    V[:, -1] = Payoff                              # terminal condition

    # Boundary conditions (set for all time levels)
    if payoff == "call":
        V[-extraP - 1:, :] = (
            np.exp(x[-extraP - 1:]).reshape(-1, 1)
            * np.ones((extraP + 1, Ntime))
            - K * np.exp(-r * t[::-1]) * np.ones((extraP + 1, Ntime))
        )
        V[:extraP + 1, :] = 0.0
    else:
        V[-extraP - 1:, :] = 0.0
        V[:extraP + 1, :] = (
            K * np.exp(-r * t[::-1]) * np.ones((extraP + 1, Ntime))
        )

    # ------------------------------------------------------------------
    # Discretise the Levy measure nu on the jump grid  [-extraP-1..extraP+1]*dx
    # ------------------------------------------------------------------
    cdf_pts = np.linspace(
        -(extraP + 1 + 0.5) * dx,
         (extraP + 1 + 0.5) * dx,
        2 * (extraP + 2),
    )
    cdf_vals = ss.norm.cdf(cdf_pts, loc=muJ, scale=sigJ)
    nu = lam * np.diff(cdf_vals)           # discrete jump measure

    lam_appr = np.sum(nu)
    exp_grid = np.array([
        np.exp(i * dx) - 1 for i in range(-(extraP + 1), extraP + 2)
    ])
    m_appr = exp_grid @ nu                 # discrete mean jump size

    # ------------------------------------------------------------------
    # Tridiagonal matrix for the implicit diffusion part
    # ------------------------------------------------------------------
    sig2 = sig ** 2
    dxx = dx ** 2
    a = (dt / 2) * ((r - m_appr - 0.5 * sig2) / dx - sig2 / dxx)
    b = 1 + dt * (sig2 / dxx + r + lam_appr)
    c = -(dt / 2) * ((r - m_appr - 0.5 * sig2) / dx + sig2 / dxx)

    D = sparse.diags([a, b, c], [-1, 0, 1],
                      shape=(Nspace - 2, Nspace - 2)).tocsc()
    DD = splu(D)

    offset = np.zeros(Nspace - 2)

    # ------------------------------------------------------------------
    # Backward time-stepping
    # ------------------------------------------------------------------
    for i in range(Ntime - 2, -1, -1):
        offset[0]  = a * V[extraP, i]
        offset[-1] = c * V[-1 - extraP, i]

        # Jump integral via convolution (explicit in the old time level)
        V_jump = (
            V[extraP + 1: -extraP - 1, i + 1]
            + dt * signal.convolve(V[:, i + 1], nu[::-1],
                                   mode="valid", method="fft")
        )
        V[extraP + 1: -extraP - 1, i] = DD.solve(V_jump - offset)

    # Interpolate price at S0
    X0 = np.log(S0)
    price = float(np.interp(X0, x, V[:, 0]))

    # Interior grid values for plotting
    S_vec    = np.exp(x[extraP + 1: -extraP - 1])
    price_vec = V[extraP + 1: -extraP - 1, 0]
    return price, S_vec, price_vec


# ============================================================================
# 7.  Implied-volatility smile extraction
# ============================================================================

def merton_iv_smile(S0, K_vec, T, r, sig, lam, muJ, sigJ):
    """
    Compute the Merton implied-volatility smile across a vector of strikes
    using the Lewis integral representation.

    Parameters
    ----------
    K_vec : array-like
        Vector of strikes.

    Returns
    -------
    iv : ndarray
        Black-Scholes implied volatilities for each strike.
    """
    m = lam * (np.exp(muJ + 0.5 * sigJ ** 2) - 1)
    cf_Mert = partial(
        cf_merton,
        t=T,
        mu=(r - 0.5 * sig ** 2 - m),
        sig=sig,
        lam=lam,
        muJ=muJ,
        sigJ=sigJ,
    )
    iv = np.array([
        IV_from_Lewis(Ki, S0, T, r, cf_Mert) for Ki in K_vec
    ])
    return iv


# ============================================================================
# 8.  Demo
# ============================================================================

if __name__ == "__main__":

    # ------------------------------------------------------------------
    # Model parameters
    # ------------------------------------------------------------------
    S0   = 100.0       # spot price
    K    = 100.0       # strike (ATM)
    T    = 1.0         # maturity (years)
    r    = 0.05        # risk-free rate
    sig  = 0.2         # diffusion volatility
    lam  = 0.75        # jump intensity  (expected 0.75 jumps per year)
    muJ  = -0.10       # mean of log-jump size  (negative => downward jumps)
    sigJ = 0.30        # std dev of log-jump size

    print("=" * 68)
    print("  Merton Jump-Diffusion Pricer  --  Method Comparison")
    print("=" * 68)
    print(f"  S0 = {S0},  K = {K},  T = {T},  r = {r}")
    print(f"  sig = {sig},  lam = {lam},  muJ = {muJ},  sigJ = {sigJ}")
    print("-" * 68)

    # ------------------------------------------------------------------
    # 1) Closed-form series
    # ------------------------------------------------------------------
    price_closed = merton_closed_formula(S0, K, T, r, sig, lam, muJ, sigJ,
                                         payoff="call")

    # ------------------------------------------------------------------
    # 2) Fourier inversion  (Gil-Pelaez)
    # ------------------------------------------------------------------
    price_fourier = merton_fourier_inversion(S0, K, T, r, sig, lam, muJ, sigJ,
                                              payoff="call")

    # ------------------------------------------------------------------
    # 3) FFT  (single ATM strike, but method returns a vector)
    # ------------------------------------------------------------------
    price_fft = merton_fft(S0, [K], T, r, sig, lam, muJ, sigJ,
                           payoff="call")[0]

    # ------------------------------------------------------------------
    # 4) Monte Carlo
    # ------------------------------------------------------------------
    price_mc, se_mc = merton_mc(S0, K, T, r, sig, lam, muJ, sigJ,
                                payoff="call", N_paths=500_000, seed=42)

    # ------------------------------------------------------------------
    # 5) PIDE
    # ------------------------------------------------------------------
    price_pide, S_pide, V_pide = merton_pide(
        S0, K, T, r, sig, lam, muJ, sigJ, payoff="call",
        Nspace=500, Ntime=400,
    )

    # ------------------------------------------------------------------
    # Comparison table
    # ------------------------------------------------------------------
    print(f"\n{'Method':<25s}  {'Price':>12s}  {'Diff vs Closed':>16s}")
    print("-" * 58)
    methods = [
        ("Closed formula",        price_closed, 0.0),
        ("Fourier inversion",     price_fourier, price_fourier - price_closed),
        ("FFT (Lewis)",           price_fft,     price_fft     - price_closed),
        ("Monte Carlo (500k)",    price_mc,      price_mc      - price_closed),
        ("PIDE (500x400)",        price_pide,    price_pide    - price_closed),
    ]
    for name, px, diff in methods:
        print(f"  {name:<23s}  {px:12.6f}  {diff:+16.6f}")
    print(f"\n  MC standard error: {se_mc:.6f}")
    print("-" * 58)

    # ------------------------------------------------------------------
    # Plot 1 -- Merton price curve vs intrinsic payoff
    # ------------------------------------------------------------------
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    ax = axes[0]
    S_plot = S_pide
    payoff_plot = np.maximum(S_plot - K, 0)
    ax.plot(S_plot, payoff_plot, "b--", lw=1.5, label="Payoff  max(S-K, 0)")
    ax.plot(S_plot, V_pide, "r-", lw=2, label="Merton PIDE price")
    ax.set_xlim(40, 200)
    ax.set_ylim(-2, 110)
    ax.set_xlabel("Spot price  S")
    ax.set_ylabel("Option value")
    ax.set_title("Merton Call: Price Curve vs Payoff")
    ax.legend(loc="upper left")
    ax.grid(True, alpha=0.3)

    # ------------------------------------------------------------------
    # Plot 2 -- Implied-volatility smile
    # ------------------------------------------------------------------
    K_smile = np.linspace(70, 140, 40)
    iv_smile = merton_iv_smile(S0, K_smile, T, r, sig, lam, muJ, sigJ)

    ax = axes[1]
    ax.plot(K_smile, iv_smile, "ko-", markersize=4, lw=1.5)
    ax.axhline(sig, color="grey", ls="--", lw=1, label=f"Diffusion vol = {sig}")
    ax.set_xlabel("Strike  K")
    ax.set_ylabel("Implied volatility")
    ax.set_title("Merton Jump-Diffusion IV Smile")
    ax.legend()
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("cantaro86_merton_pricer_demo.png", dpi=150)
    plt.show()

    print("\nDone.  Plots saved to cantaro86_merton_pricer_demo.png")
