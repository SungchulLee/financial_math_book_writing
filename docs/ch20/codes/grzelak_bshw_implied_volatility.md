# Black-Scholes-Hull-White Implied Volatility

## Background

BSHW model implied volatility term structure computation.

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak

---

## Code

```python
"""
BSHW model implied volatility term structure computation.

This code is purely educational and comes from the Financial Engineering
course by L.A. Grzelak, based on the book "Mathematical Modeling and Computation
in Finance: With Exercises and Python and MATLAB Computer Codes",
by C.W. Oosterlee and L.A. Grzelak, World Scientific Publishing Europe Ltd, 2019.

@author: Lech A. Grzelak
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate
import scipy.stats as st
import enum
import scipy.optimize as optimize


# ======================================================================

class OptionType(enum.Enum):
    CALL = 1.0
    PUT = -1.0


def bs_call_option_price(cp, s_0, k, sigma, tau, r):
    """Black-Scholes option price."""
    if isinstance(k, list):
        k = np.array(k).reshape([len(k), 1])
    d1 = (np.log(s_0 / k) + (r + 0.5 * sigma ** 2.0) * tau) / (sigma * np.sqrt(tau))
    d2 = d1 - sigma * np.sqrt(tau)
    if cp == OptionType.CALL:
        value = st.norm.cdf(d1) * s_0 - st.norm.cdf(d2) * k * np.exp(-r * tau)
    elif cp == OptionType.PUT:
        value = st.norm.cdf(-d2) * k * np.exp(-r * tau) - st.norm.cdf(-d1) * s_0
    return value


def implied_volatility_black76(cp, frwd_market_price, k, t, frwd_stock):
    """Implied volatility using Black76."""
    func = lambda sigma: np.power(bs_call_option_price(cp, frwd_stock, k, sigma, t, 0.0) - frwd_market_price, 1.0)
    implied_vol = optimize.newton(func, 0.2, tol=1e-9)
    return implied_vol


def bshw_volatility(t, eta, sigma, rho, lambd):
    """BSHW model volatility."""
    br = lambda t_val, t_end: 1.0 / lambd * (np.exp(-lambd * (t_end - t_val)) - 1.0)
    sigma_f = lambda t_val: np.sqrt(sigma * sigma + eta * eta * br(t_val, t) * br(t_val, t) -
                                    2.0 * rho * sigma * eta * br(t_val, t))
    z_grid = np.linspace(0.0, t, 2500)
    sigma_c = np.sqrt(1.0 / t * integrate.trapz(sigma_f(z_grid) * sigma_f(z_grid), z_grid))
    return sigma_c


def bshw_option_price(cp, s0, k, p0t, t, eta, sigma, rho, lambd):
    """BSHW option price."""
    frwd_s0 = s0 / p0t
    vol = bshw_volatility(t, eta, sigma, rho, lambd)
    r = 0.0
    black_price = bs_call_option_price(cp, frwd_s0, k, vol, t, r)
    return p0t * black_price


def main():
    """Main computation."""
    cp = OptionType.CALL

    # HW model settings
    lambd = 0.1
    eta = 0.01
    sigma = 0.2
    rho = 0.3
    s0 = 100

    # Strike equals stock value, thus ATM
    k = [100]
    k = np.array(k).reshape([len(k), 1])

    # ZCB curve
    p0t = lambda t: np.exp(-0.05 * t)

    # Maturities at which to compute implied volatility
    t_mat = np.linspace(0.1, 5.0, 20)

    # Effect of lambda
    plt.figure(2)
    plt.grid()
    plt.xlabel('maturity, T')
    plt.ylabel('implied volatility')
    lambda_v = [0.001, 0.1, 0.5, 1.5]
    legend = []
    for lambda_temp in lambda_v:
        iv = np.zeros((len(t_mat), 1))
        for idx in range(0, len(t_mat)):
            t = t_mat[idx]
            val = bshw_option_price(cp, s0, k, p0t(t), t, eta, sigma, rho, lambda_temp)
            frwd_stock = s0 / p0t(t)
            val_frwd = val / p0t(t)
            iv[idx] = implied_volatility_black76(cp, val_frwd, k, t, frwd_stock)
        plt.plot(t_mat, iv * 100.0)
        legend.append('lambda={0}'.format(lambda_temp))
    plt.legend(legend)

    # Effect of eta
    plt.figure(3)
    plt.grid()
    plt.xlabel('maturity, T')
    plt.ylabel('implied volatility')
    eta_v = [0.001, 0.05, 0.1, 0.15]
    legend = []
    for eta_temp in eta_v:
        iv = np.zeros((len(t_mat), 1))
        for idx in range(0, len(t_mat)):
            t = t_mat[idx]
            val = bshw_option_price(cp, s0, k, p0t(t), t, eta_temp, sigma, rho, lambd)
            frwd_stock = s0 / p0t(t)
            val_frwd = val / p0t(t)
            iv[idx] = implied_volatility_black76(cp, val_frwd, k, t, frwd_stock)
        plt.plot(t_mat, iv * 100.0)
        legend.append('eta={0}'.format(eta_temp))
    plt.legend(legend)

    # Effect of sigma
    plt.figure(4)
    plt.grid()
    plt.xlabel('maturity, T')
    plt.ylabel('implied volatility')
    sigma_v = [0.1, 0.2, 0.3, 0.4]
    legend = []
    for sigma_temp in sigma_v:
        iv = np.zeros((len(t_mat), 1))
        for idx in range(0, len(t_mat)):
            t = t_mat[idx]
            val = bshw_option_price(cp, s0, k, p0t(t), t, eta, sigma_temp, rho, lambd)
            frwd_stock = s0 / p0t(t)
            val_frwd = val / p0t(t)
            iv[idx] = implied_volatility_black76(cp, val_frwd, k, t, frwd_stock)
        plt.plot(t_mat, iv * 100.0)
        legend.append('sigma={0}'.format(sigma_temp))
    plt.legend(legend)

    # Effect of rho
    plt.figure(5)
    plt.grid()
    plt.xlabel('maturity, T')
    plt.ylabel('implied volatility')
    rho_v = [-0.7, -0.3, 0.3, 0.7]
    legend = []
    for rho_temp in rho_v:
        iv = np.zeros((len(t_mat), 1))
        for idx in range(0, len(t_mat)):
            t = t_mat[idx]
            val = bshw_option_price(cp, s0, k, p0t(t), t, eta, sigma, rho_temp, lambd)
            frwd_stock = s0 / p0t(t)
            val_frwd = val / p0t(t)
            iv[idx] = implied_volatility_black76(cp, val_frwd, k, t, frwd_stock)
        plt.plot(t_mat, iv * 100.0)
        legend.append('rho={0}'.format(rho_temp))
    plt.legend(legend)


if __name__ == "__main__":
    main()
```

## Exercises

**Exercise 1.**
The BSHW model generates a term structure of implied volatilities that varies with option maturity. Explain why shorter-dated and longer-dated options have different implied volatilities even for ATM strikes.

??? success "Solution to Exercise 1"
    For short-dated options, the stochastic interest rate has minimal impact because the variance of $\int_0^T r(s)\,ds$ is small. The implied volatility is close to $\sigma_S$ (the asset volatility). For long-dated options, the accumulated interest rate uncertainty becomes significant, adding to the total variance of the log-asset price:

    $$
    \text{Var}[\ln S(T)] \approx \sigma_S^2 T + \text{terms involving } \eta, \rho, \lambda.
    $$

    This additional variance increases the implied volatility for long-dated options, creating a term structure that rises with maturity (if $\rho < 0$ or $\eta > 0$).

---

**Exercise 2.**
If the BSHW model has $\sigma_S = 20\%$, $\eta = 1\%$, $\lambda = 5\%$, and $\rho = -0.3$, qualitatively describe the implied volatility term structure for ATM options.

??? success "Solution to Exercise 2"

    - At short maturities ($T < 1$ year), the implied vol is approximately $\sigma_S = 20\%$.
    - At longer maturities, the interest rate variance contribution grows. With $\eta = 1\%$ (small rate vol), the effect is modest -- perhaps adding $0.5-1\%$ to implied vol at 10 years.
    - The negative correlation $\rho = -0.3$ introduces skew but has a relatively minor effect on ATM vol.
    - The mean reversion $\lambda = 5\%$ limits the long-run interest rate variance to $\eta^2/(2\lambda) = 0.01\%$, keeping the term structure effect bounded.

    Overall, the ATM implied vol term structure would gently rise from $20\%$ at short maturities to approximately $20.5-21\%$ at 10 years.

---

**Exercise 3.**
How would increasing the correlation $\rho$ from $-0.3$ to $+0.3$ change the implied volatility skew?

??? success "Solution to Exercise 3"
    With $\rho = -0.3$: When rates rise (bad for bonds), stocks tend to fall, amplifying downside risk. This steepens the put skew (higher implied vol for low strikes).

    With $\rho = +0.3$: When rates rise, stocks tend to rise too. This reduces downside risk and can flatten or reverse the skew, with higher implied vol for high strikes. The change from negative to positive correlation shifts the skew from "equity-like" (downward sloping) to "interest-rate-like" (potentially upward sloping), which has significant implications for pricing and hedging long-dated equity options.

---

**Exercise 4.**
Explain why the BSHW model is particularly important for pricing long-dated equity options and equity-linked insurance products.

??? success "Solution to Exercise 4"
    For maturities beyond 5 years, the assumption of constant (or deterministic) interest rates becomes unrealistic. The BSHW model captures the joint dynamics of equity and interest rates, which is crucial for:

    1. **Variable annuities**: These insurance products have maturities of 10-30 years and include guaranteed minimum benefits linked to equity performance, discounted at prevailing rates.
    2. **Convertible bonds**: Long-dated instruments where both equity and rate risk matter.
    3. **Equity-linked notes**: Structured products with long tenors.

    Using a flat-rate model would misprice these products by ignoring the correlation between equity performance and the discount rate, leading to hedging errors.
