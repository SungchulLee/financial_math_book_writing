# -*- coding: utf-8 -*-
"""
hull_white_model_class.py

Hull-White One-Factor Model - Class-Based Implementation

This module provides a complete, object-oriented implementation of the
one-factor Hull-White short-rate model:

    dr(t) = lambda [theta(t) - r(t)] dt + sigma dW^Q(t)

where theta(t) is calibrated to match the initial yield curve P(0,T).

Key features:
    - Named functions A(t,T), B(t,T) for the affine bond pricing formula
    - Zero-coupon bond pricing: P(t,T) = exp(A + B * r_t)
    - Bond option pricing via closed-form formulas
    - Caplet / floorlet pricing
    - Swap pricing (payer and receiver)
    - Monte Carlo path generation with variance reduction

Based on: QuantPie Lecture Notes on Hull-White Model
"""

import enum
import numpy as np
from scipy import stats
from scipy.integrate import trapz
from scipy.optimize import newton


E = np.exp
E1 = lambda x: np.exp(x) - 1.0
L = np.log


class OptionType(enum.Enum):
    CALL = 1
    PUT = -1


class OptionTypeSwap(enum.Enum):
    RECEIVER = 1.0
    PAYER = -1.0


# ---------------------------------------------------------------------------
# Yield-curve helpers (numerical differentiation of P(0,T))
# ---------------------------------------------------------------------------

def f(T, P, dT=0.0001):
    """Instantaneous forward rate: f(0,T) = -d/dT ln P(0,T)."""
    return -(L(P(T + dT)) - L(P(T - dT))) / (2 * dT)


def df_over_dT(T, P, dT=0.0001):
    """Derivative of the instantaneous forward rate."""
    return (f(T + dT, P) - f(T - dT, P)) / (2 * dT)


def compute_r0(P):
    """Extract the initial short rate r(0) from the yield curve."""
    return f(T=0.0001, P=P, dT=0.0001)


# ---------------------------------------------------------------------------
# Black-Scholes / Black-76 helpers
# ---------------------------------------------------------------------------

def compute_Option_Price(S_0, K, sigma, tau, r, CP):
    """Black-76 option price (call or put)."""
    if K is list:
        K = np.array(K).reshape((len(K), 1))
    eps = 1e-16
    d1 = (L(S_0 / K) + (r + 0.5 * sigma**2) * tau) / (sigma * np.sqrt(tau) + eps)
    d2 = d1 - sigma * np.sqrt(tau)
    if CP == OptionType.CALL:
        return S_0 * stats.norm.cdf(d1) - K * np.exp(-r * tau) * stats.norm.cdf(d2)
    elif CP == OptionType.PUT:
        return -S_0 * stats.norm.cdf(-d1) + K * np.exp(-r * tau) * stats.norm.cdf(-d2)


def compute_Implied_Volatility_using_Black76(market_price, K, T, S_0, CP, verbose=0):
    """Implied volatility via Newton's method on Black-76."""
    sigmaGrid = np.linspace(0.0, 5.0, 5_000)
    optPriceGrid = compute_Option_Price(S_0, K, sigmaGrid, T, r=0.0, CP=CP)
    sigmaInitial = np.interp(market_price, optPriceGrid, sigmaGrid)
    if verbose:
        print(f"{K = }")
        print(f"{sigmaInitial = }")
    func = lambda sigma: compute_Option_Price(S_0, K, sigma, T, r=0.0, CP=CP) - market_price
    impliedVol = newton(func, sigmaInitial, tol=1e-15)
    if verbose:
        print(f"{impliedVol = }")
    if impliedVol > 2.0:
        impliedVol = 0.0
    return impliedVol


# ---------------------------------------------------------------------------
# Hull-White model class
# ---------------------------------------------------------------------------

class HullWhite:
    """
    One-factor Hull-White short-rate model.

    Parameters
    ----------
    sigma : float
        Volatility parameter.
    lambd : float
        Mean-reversion speed.
    P : callable
        Zero-coupon bond price P(0,t) as a function of maturity t.
    """

    def __init__(self, sigma, lambd, P):
        self.sigma = sigma
        self.lambd = lambd
        self.P = P

    # --- Named functions ---

    def compute_sigma_P(self, t, T):
        """sigma_P(t,T) = sigma * B(t,T)."""
        return self.sigma * self.compute_B(t, T)

    def compute_theta(self, t):
        """
        Mean-reversion target theta(t) calibrated to the initial curve:

            theta(t) = f(0,t) + (1/lambda) df/dt + sigma^2/(2*lambda^2)(1 - e^{-2*lambda*t})
        """
        first = f(t, self.P)
        second = df_over_dT(t, self.P) / self.lambd
        third = -self.sigma**2 / (2 * self.lambd**2) * E1(-2 * self.lambd * t)
        return first + second + third

    def compute_theta_T(self, t, T):
        """theta^T(t) = theta(t) + sigma^2/lambda * B(T-t) -- drift under the T-forward measure."""
        first = self.compute_theta(t)
        second = self.sigma**2 / self.lambd * self.compute_B(t, T)
        return first + second

    def compute_A(self, t, T):
        """
        A(tau) in P(t,T) = exp(A(tau) + B(tau) r(t)).

        Computed via analytical formula + numerical integration of theta.
        """
        tau = T - t
        head = -self.sigma**2 / (4 * self.lambd**3)
        tail = 3 - 2 * self.lambd * tau - 4 * E(-self.lambd * tau) + E(-2 * self.lambd * tau)
        first = head * tail

        tau_prime = np.linspace(0, tau, 250)
        theta = self.compute_theta
        B = lambda s: self.compute_B(t=0, T=s)
        second = self.lambd * trapz(theta(T - tau_prime) * B(tau_prime), tau_prime)
        return first + second

    def compute_B(self, t, T):
        """B(tau) = -(1 - e^{-lambda*tau})/lambda in P(t,T) = exp(A + B*r_t)."""
        tau = T - t
        return E1(-self.lambd * tau) / self.lambd

    # --- Bond pricing ---

    def compute_ZCB(self, t, T, r_t):
        """Zero-coupon bond price P(t,T) = exp(A(tau) + B(tau) r_t)."""
        A = self.compute_A(t, T)
        B = self.compute_B(t, T)
        return E(A + B * r_t)

    # --- Monte Carlo simulation ---

    def generate_sample_paths(self, num_paths, num_steps, T, seed=None):
        """
        Simulate Hull-White short-rate paths via Euler discretization.

        Returns
        -------
        t : ndarray of shape (num_steps + 1,)
        R : ndarray of shape (num_paths, num_steps + 1)
            Short-rate paths.
        M : ndarray of shape (num_paths, num_steps + 1)
            Money market account paths.
        """
        if seed is not None:
            np.random.seed(seed)

        r0 = compute_r0(self.P)
        theta = self.compute_theta

        Z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
        R = np.ones((num_paths, num_steps + 1)) * r0
        M = np.ones((num_paths, num_steps + 1))

        t = np.linspace(0, T, num_steps + 1)
        dt = t[1] - t[0]
        sqrt_dt = np.sqrt(dt)
        for i in range(num_steps):
            if num_paths > 1:
                Z[:, i] = (Z[:, i] - Z[:, i].mean()) / Z[:, i].std()
            dW = sqrt_dt * Z[:, i]
            # Hull-White Short Rate Dynamics
            # dr(t) = lambda(theta(t) - r(t)) dt + sigma dW^Q(t)
            R[:, i + 1] = R[:, i] + self.lambd * (theta(t[i]) - R[:, i]) * dt + self.sigma * dW
            M[:, i + 1] = M[:, i] * np.exp(R[:, i] * dt)
        return t, R, M

    # --- Moments of r(T) ---

    def compute_mu_r_T(self, T):
        """E^Q[r(T)] -- mean short rate at T under Q."""
        r0 = compute_r0(self.P)
        theta = self.compute_theta
        s = np.linspace(0.0, T, 2_500)
        integrand = lambda s: theta(s) * E(-self.lambd * (T - s))
        return r0 * E(-self.lambd * T) + self.lambd * trapz(integrand(s), s)

    def compute_mu_r_T_ForwardMeasure(self, T):
        """E^T[r(T)] -- mean short rate at T under the T-forward measure."""
        r0 = compute_r0(self.P)
        theta_T_Forward = lambda s, T: self.compute_theta_T(s, T)
        s = np.linspace(0.0, T, 2_500)
        integrand = lambda s: theta_T_Forward(s, T) * E(-self.lambd * (T - s))
        return r0 * E(-self.lambd * T) + self.lambd * trapz(integrand(s), s)

    def compute_sigma_square_r_T(self, T):
        """Var^Q[r(T)]."""
        return -self.sigma**2 / (2 * self.lambd) * E1(-2 * self.lambd * T)

    # --- Bond options ---

    def compute_ZCB_Option_Price(self, K, T1, T2, CP):
        """
        Price of a European option on a zero-coupon bond P(T1, T2).

        Parameters
        ----------
        K : float -- strike price
        T1 : float -- option expiry
        T2 : float -- bond maturity
        CP : OptionType -- CALL or PUT
        """
        A = self.compute_A(T1, T2)
        B = self.compute_B(T1, T2)
        mu = self.compute_mu_r_T_ForwardMeasure(T1)
        v = np.sqrt(self.compute_sigma_square_r_T(T1))

        K_hat = K * E(-A)
        a = (L(K_hat) - B * mu) / (B * v)
        d1 = a - B * v
        d2 = d1 + B * v
        value = self.P(T1) * E(A) * (
            E(0.5 * B**2 * v**2 + B * mu) * stats.norm.cdf(d1) - K_hat * stats.norm.cdf(d2)
        )

        if CP == OptionType.CALL:
            return value
        elif CP == OptionType.PUT:
            return value - self.P(T2) + K * self.P(T1)

    # --- Caplets / floorlets ---

    def compute_Caplet_Floorlet_Price(self, N, K, T1, T2, CP):
        """
        Price a caplet (CP=CALL) or floorlet (CP=PUT).

        Parameters
        ----------
        N : float -- notional
        K : float -- strike rate
        T1, T2 : float -- accrual period [T1, T2]
        CP : OptionType -- CALL (caplet) or PUT (floorlet)
        """
        N_new = N * (1.0 + (T2 - T1) * K)
        K_new = 1 / (1.0 + (T2 - T1) * K)
        if CP == OptionType.CALL:
            return N_new * self.compute_ZCB_Option_Price(K_new, T1, T2, CP=OptionType.PUT)
        elif CP == OptionType.PUT:
            return N_new * self.compute_ZCB_Option_Price(K_new, T1, T2, CP=OptionType.CALL)

    # --- Swap pricing ---

    def compute_Swap_Price(self, t, r_t, notional, K, Ti, Tm, n, CP):
        """
        Price an interest-rate swap under Hull-White.

        Parameters
        ----------
        t : float -- current time
        r_t : float or ndarray -- current short rate(s)
        notional : float -- notional amount
        K : float -- fixed rate
        Ti, Tm : float -- swap start and end
        n : int -- number of payment dates
        CP : OptionTypeSwap -- PAYER or RECEIVER
        """
        if n == 1:
            Ti_grid = np.array((Ti, Tm))
        else:
            Ti_grid = np.linspace(Ti, Tm, n)
        tau = Ti_grid[1] - Ti_grid[0]

        if np.size(Ti_grid[np.where(Ti_grid < t)]) > 0:
            Ti = Ti_grid[np.where(Ti_grid < t)][-1]

        A_mn = np.zeros(np.size(r_t))
        P_t_Ti_Lambda = lambda Ti_val: self.compute_ZCB(t, Ti_val, r_t)
        P_t_Ti = P_t_Ti_Lambda(Ti)
        P_t_Tm = P_t_Ti_Lambda(Tm)

        for idx, ti in enumerate(Ti_grid[np.where(Ti_grid >= t)]):
            if ti > Ti:
                A_mn = A_mn + tau * P_t_Ti_Lambda(ti)

        if CP == OptionTypeSwap.PAYER:
            swap = (P_t_Ti - P_t_Tm) - K * A_mn
        elif CP == OptionTypeSwap.RECEIVER:
            swap = K * A_mn - (P_t_Ti - P_t_Tm)
        return swap * notional


# ---------------------------------------------------------------------------
# Standalone helpers (functional interface)
# ---------------------------------------------------------------------------

def compute_pdf_r_T(P, lambd, sigma, T):
    """PDF of r(T) under Q -- normal distribution."""
    hw = HullWhite(sigma, lambd, P)
    mu = hw.compute_mu_r_T(T)
    var = hw.compute_sigma_square_r_T(T)
    return stats.norm(mu, np.sqrt(var)).pdf


# ---------------------------------------------------------------------------
# Main -- example usage
# ---------------------------------------------------------------------------

def main():
    """Demonstrate the Hull-White model class."""
    import matplotlib.pyplot as plt

    print("Hull-White One-Factor Model -- Class Demo")
    print("=" * 50)

    # Flat yield curve at 3%
    r_flat = 0.03
    P = lambda T: np.exp(-r_flat * T)

    sigma = 0.01
    lambd = 0.5
    hw = HullWhite(sigma, lambd, P)

    # Simulate short-rate paths
    T = 10.0
    num_paths = 500
    num_steps = 500
    t, R, M = hw.generate_sample_paths(num_paths, num_steps, T, seed=42)

    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Plot paths
    for i in range(min(50, num_paths)):
        axes[0].plot(t, R[i], alpha=0.3, lw=0.5)
    axes[0].axhline(r_flat, color="red", ls="--", label=f"r0 = {r_flat}")
    axes[0].set_title(f"Hull-White Short Rate Paths (sigma={sigma}, lambda={lambd})")
    axes[0].set_xlabel("Time (years)")
    axes[0].set_ylabel("r(t)")
    axes[0].legend()
    axes[0].grid(True, alpha=0.3)

    # Plot ZCB prices
    T_grid = np.linspace(0.5, 30, 60)
    zcb = [hw.compute_ZCB(0, Ti, r_flat) for Ti in T_grid]
    axes[1].plot(T_grid, zcb, "b-", lw=2)
    axes[1].set_title("Zero-Coupon Bond Prices P(0,T)")
    axes[1].set_xlabel("Maturity T")
    axes[1].set_ylabel("P(0,T)")
    axes[1].grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("/tmp/hull_white_model_class.png", dpi=150)
    print("Figure saved to /tmp/hull_white_model_class.png")
    plt.close()

    # Derivative pricing demo
    print(f"\n--- Bond Option Pricing ---")
    K = 0.95
    T1, T2 = 1.0, 2.0
    call_price = hw.compute_ZCB_Option_Price(K, T1, T2, OptionType.CALL)
    put_price = hw.compute_ZCB_Option_Price(K, T1, T2, OptionType.PUT)
    print(f"ZCB Option (K={K}, T1={T1}, T2={T2}): Call={call_price:.6f}, Put={put_price:.6f}")

    print(f"\n--- Caplet/Floorlet Pricing ---")
    N = 1_000_000
    K_rate = 0.03
    caplet = hw.compute_Caplet_Floorlet_Price(N, K_rate, T1, T2, OptionType.CALL)
    floorlet = hw.compute_Caplet_Floorlet_Price(N, K_rate, T1, T2, OptionType.PUT)
    print(f"Caplet (N={N:,.0f}, K={K_rate}): {caplet:.2f}")
    print(f"Floorlet (N={N:,.0f}, K={K_rate}): {floorlet:.2f}")


if __name__ == "__main__":
    main()
