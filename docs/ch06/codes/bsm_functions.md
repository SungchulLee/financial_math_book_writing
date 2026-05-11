# Black-Scholes-Merton Functions (Call, Put, Vega, Implied Volatility)

## Background

Bsm Functions

Educational script demonstrating bsm functions concepts.

---

## Code

```python
"""
Bsm Functions

Educational script demonstrating bsm functions concepts.
"""

# ---
# title: "BSM Analytical Functions"
# description: >
#   Standalone utility functions for Black-Scholes-Merton pricing:
#     - bsm_call_value  : closed-form European call price
#     - bsm_put_value   : closed-form European put price (via put-call parity)
#     - bsm_vega        : Vega (sensitivity to volatility)
#     - bsm_call_imp_vol: Newton-Raphson implied volatility solver
#
#   These functions are intentionally stateless (no classes) so they
#   can be imported as building blocks elsewhere in the book.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

from math import log, sqrt, exp
from scipy import stats
import numpy as np


# ======================================================================
# ── Black-Scholes-Merton call value ────────────────────────────
def bsm_call_value(S0, K, T, r, sigma):
    """Analytical European call price under BSM.

    Parameters
    ----------
    S0 : float    – current stock price
    K  : float    – strike price
    T  : float    – time to maturity (year fraction)
    r  : float    – risk-free rate (continuous compounding)
    sigma : float – volatility (annualised)

    Returns
    -------
    float – call option present value
    """
    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    value = S0 * stats.norm.cdf(d1) - K * exp(-r * T) * stats.norm.cdf(d2)
    return value


# ── Black-Scholes-Merton put value (via put-call parity) ──────
def bsm_put_value(S0, K, T, r, sigma):
    """Analytical European put price under BSM (put-call parity).

    Parameters
    ----------
    S0, K, T, r, sigma : same as bsm_call_value

    Returns
    -------
    float – put option present value
    """
    call = bsm_call_value(S0, K, T, r, sigma)
    return call - S0 + K * exp(-r * T)


# ── Vega ───────────────────────────────────────────────────────
def bsm_vega(S0, K, T, r, sigma):
    """Vega of a European option under BSM.

    Returns
    -------
    float – partial derivative of the option price w.r.t. sigma
    """
    S0 = float(S0)
    d1 = (log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    return S0 * stats.norm.pdf(d1) * sqrt(T)


# ── Implied volatility (Newton-Raphson) ────────────────────────
def bsm_call_imp_vol(S0, K, T, r, C0, sigma_est=0.25, tol=1e-10, max_iter=100):
    """Implied volatility of a European call via Newton-Raphson.

    Parameters
    ----------
    C0 : float        – observed market price of the call
    sigma_est : float – initial guess for implied vol
    tol : float       – convergence tolerance
    max_iter : int    – maximum iterations

    Returns
    -------
    float – implied volatility estimate
    """
    for _ in range(max_iter):
        diff = bsm_call_value(S0, K, T, r, sigma_est) - C0
        vega = bsm_vega(S0, K, T, r, sigma_est)
        if abs(vega) < 1e-14:
            break
        sigma_est -= diff / vega
        if abs(diff) < tol:
            break
    return sigma_est


# ── Quick demonstration ────────────────────────────────────────
if __name__ == "__main__":
    S0, K, T, r, sigma = 100.0, 105.0, 1.0, 0.05, 0.2

    call = bsm_call_value(S0, K, T, r, sigma)
    put = bsm_put_value(S0, K, T, r, sigma)
    vega = bsm_vega(S0, K, T, r, sigma)

    print(f"BSM Analytical Pricing  (S0={S0}, K={K}, T={T}, r={r}, sigma={sigma})")
    print(f"  Call  : {call:.6f}")
    print(f"  Put   : {put:.6f}")
    print(f"  Vega  : {vega:.6f}")

    # Round-trip: price -> implied vol -> price
    iv = bsm_call_imp_vol(S0, K, T, r, call)
    print(f"  IV    : {iv:.6f}  (should recover {sigma})")
```

## Exercises

**Exercise 1.**
The `bsm_call_value` function implements the BS call formula as a standalone function. Explain the advantage of stateless functions over class methods for building blocks.

??? success "Solution to Exercise 1"
    Stateless (pure) functions have several advantages as building blocks:

    1. **No side effects**: Output depends only on inputs, making behavior predictable and testable.
    2. **Composability**: Can be freely combined without worrying about shared state or initialization order.
    3. **Vectorizability**: Can be applied to arrays of inputs using NumPy broadcasting without modification.
    4. **Thread safety**: No shared mutable state means safe parallel execution.
    5. **Import flexibility**: Users can import individual functions without the overhead of a class hierarchy.

---

**Exercise 2.**
Derive the put price formula from the call price using put-call parity. Show that $P = Ke^{-rT}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)$.

??? success "Solution to Exercise 2"
    From put-call parity: $P = C - S + Ke^{-rT} = [S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)] - S + Ke^{-rT}$.

    $$
    P = S[\mathcal{N}(d_1) - 1] + Ke^{-rT}[1 - \mathcal{N}(d_2)] = -S\mathcal{N}(-d_1) + Ke^{-rT}\mathcal{N}(-d_2)
    $$

    using $\Phi(-x) = 1 - \Phi(x)$. Therefore $P = Ke^{-rT}\mathcal{N}(-d_2) - S\mathcal{N}(-d_1)$.

---

**Exercise 3.**
The `bsm_vega` function computes $\nu = S\phi(d_1)\sqrt{T}$. Verify that this equals $\partial C / \partial \sigma$ by differentiating the BS call formula.

??? success "Solution to Exercise 3"
    Differentiating $C = S\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$ with respect to $\sigma$:

    $$
    \frac{\partial C}{\partial \sigma} = S\phi(d_1)\frac{\partial d_1}{\partial \sigma} - Ke^{-rT}\phi(d_2)\frac{\partial d_2}{\partial \sigma}
    $$

    Since $d_2 = d_1 - \sigma\sqrt{T}$: $\frac{\partial d_2}{\partial \sigma} = \frac{\partial d_1}{\partial \sigma} - \sqrt{T}$. Also, $S\phi(d_1) = Ke^{-rT}\phi(d_2)$ (a standard identity). Substituting:

    $$
    \frac{\partial C}{\partial \sigma} = S\phi(d_1)\sqrt{T} = \nu
    $$

---

**Exercise 4.**
The `bsm_call_imp_vol` function uses Newton-Raphson. Write the update formula and explain why vega as the derivative ensures quadratic convergence near the solution.

??? success "Solution to Exercise 4"
    Update: $\sigma_{n+1} = \sigma_n - \frac{C_{\text{BS}}(\sigma_n) - C_{\text{market}}}{\nu(\sigma_n)}$.

    Newton-Raphson has quadratic convergence (the error squares at each iteration) when: (1) the function is twice continuously differentiable (BS price is $C^\infty$ in $\sigma$), (2) the derivative (vega) is nonzero at the root ($\nu > 0$ always), and (3) the initial guess is sufficiently close.

    Since vega is always positive and the BS price is smooth and monotone in $\sigma$, Newton-Raphson converges rapidly, typically within 3--5 iterations to machine precision.
