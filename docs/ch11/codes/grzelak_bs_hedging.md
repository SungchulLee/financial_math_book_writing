# Black-Scholes Hedging (Grzelak)

## Background

Delta hedging with the Black-Scholes model.

Demonstrates dynamic delta hedging strategy for European options,
analyzing profit and loss from hedging errors.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.

---

## Code

```python
# -*- coding: utf-8 -*-
"""
Delta hedging with the Black-Scholes model.

Demonstrates dynamic delta hedging strategy for European options,
analyzing profit and loss from hedging errors.

Reference:
    Oosterlee & Grzelak (2019). Mathematical Modeling and Computation in
    Finance. World Scientific.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as st
import enum


# =============================================================================
# 1. Enum Definition
# =============================================================================

class OptionType(enum.Enum):
    """Enumeration for option type."""
    CALL = 1.0
    PUT = -1.0


# =============================================================================
# 2. Path Generation
# =============================================================================

def generate_paths_gbm(num_paths, num_steps, maturity, r, sigma, s0):
    """
    Generate GBM paths using Euler discretization.

    Parameters
    ----------
    num_paths : int
        Number of sample paths.
    num_steps : int
        Number of time steps.
    maturity : float
        Time to maturity (T).
    r : float
        Risk-free rate.
    sigma : float
        Volatility.
    s0 : float
        Initial stock price.

    Returns
    -------
    paths : dict
        Dictionary with keys 'time' and 'S'.
    """
    z = np.random.normal(0.0, 1.0, (num_paths, num_steps))
    x = np.zeros((num_paths, num_steps + 1))
    w = np.zeros((num_paths, num_steps + 1))
    time = np.zeros(num_steps + 1)

    x[:, 0] = np.log(s0)

    dt = maturity / float(num_steps)
    for i in range(num_steps):
        # Ensure samples from normal have mean 0 and variance 1
        if num_paths > 1:
            z[:, i] = (z[:, i] - np.mean(z[:, i])) / np.std(z[:, i])
        w[:, i + 1] = w[:, i] + np.sqrt(dt) * z[:, i]
        x[:, i + 1] = x[:, i] + (r - 0.5 * sigma * sigma) * dt + sigma * (w[:, i + 1] - w[:, i])
        time[i + 1] = time[i] + dt

    # Compute stock prices from log-prices
    s = np.exp(x)
    paths = {"time": time, "S": s}
    return paths


# =============================================================================
# 3. Black-Scholes Pricing Functions
# =============================================================================

def bs_call_put_option_price(option_type, s0, strikes, sigma, t, maturity, r):
    """
    Black-Scholes Call/Put option price.

    Parameters
    ----------
    option_type : OptionType
        CALL or PUT.
    s0 : float
        Initial stock price.
    strikes : array_like
        Strike prices.
    sigma : float
        Volatility.
    t : float
        Current time.
    maturity : float
        Maturity (T).
    r : float
        Risk-free rate.

    Returns
    -------
    value : ndarray
        Option price.
    """
    strikes = np.array(strikes).reshape([len(strikes), 1])
    d1 = (np.log(s0 / strikes) + (r + 0.5 * np.power(sigma, 2.0)) * (maturity - t)) / (sigma * np.sqrt(maturity - t))
    d2 = d1 - sigma * np.sqrt(maturity - t)
    if option_type == OptionType.CALL:
        value = st.norm.cdf(d1) * s0 - st.norm.cdf(d2) * strikes * np.exp(-r * (maturity - t))
    elif option_type == OptionType.PUT:
        value = st.norm.cdf(-d2) * strikes * np.exp(-r * (maturity - t)) - st.norm.cdf(-d1) * s0
    return value


def bs_delta(option_type, s0, strikes, sigma, t, maturity, r):
    """
    Black-Scholes delta (first derivative w.r.t. spot).

    Parameters
    ----------
    option_type : OptionType
        CALL or PUT.
    s0 : float
        Current stock price.
    strikes : array_like
        Strike prices.
    sigma : float
        Volatility.
    t : float
        Current time.
    maturity : float
        Maturity (T).
    r : float
        Risk-free rate.

    Returns
    -------
    delta : ndarray
        Option delta.
    """
    # Handle numerical issues near maturity
    if t - maturity > 10e-20 and maturity - t < 10e-7:
        t = maturity

    strikes = np.array(strikes).reshape([len(strikes), 1])
    d1 = (np.log(s0 / strikes) + (r + 0.5 * np.power(sigma, 2.0)) * (maturity - t)) / (sigma * np.sqrt(maturity - t))
    if option_type == OptionType.CALL:
        value = st.norm.cdf(d1)
    elif option_type == OptionType.PUT:
        value = st.norm.cdf(d1) - 1.0
    return value


# =============================================================================
# 4. Visualization
# =============================================================================

def plot_single_path_results(time, stock_prices, call_prices, deltas, pnl):
    """
    Plot results for a single sample path.

    Parameters
    ----------
    time : ndarray
        Time grid.
    stock_prices : ndarray
        Stock prices along path.
    call_prices : ndarray
        Option prices along path.
    deltas : ndarray
        Delta values along path.
    pnl : ndarray
        Profit and loss along path.
    """
    plt.figure(1, figsize=(10, 6))
    plt.plot(time, stock_prices, label='Stock')
    plt.plot(time, call_prices, label='Call Price')
    plt.plot(time, deltas, label='Delta')
    plt.plot(time, pnl, label='P&L')
    plt.legend()
    plt.grid()
    plt.xlabel('Time')
    plt.ylabel('Value')
    plt.title('Single Path Hedging Results')
    plt.tight_layout()


def plot_pnl_histogram(pnl_final):
    """
    Plot histogram of final P&L across all paths.

    Parameters
    ----------
    pnl_final : ndarray
        Final P&L values for all paths.
    """
    plt.figure(2, figsize=(10, 6))
    plt.hist(pnl_final, 50)
    plt.grid()
    plt.xlim([-0.1, 0.1])
    plt.xlabel('Final P&L')
    plt.ylabel('Frequency')
    plt.title('Distribution of Final Hedging P&L')
    plt.tight_layout()


# =============================================================================
# 5. Main
# =============================================================================

def main():
    """Run delta hedging simulation with Black-Scholes model."""
    # ===== Parameters =====
    num_paths = 5000
    num_steps = 1000
    maturity = 1.0
    r = 0.1  # Risk-free rate
    sigma = 0.2  # Volatility
    s0 = 1.0  # Initial stock price
    strikes = [0.95]
    option_type = OptionType.CALL

    np.random.seed(1)
    paths = generate_paths_gbm(num_paths, num_steps, maturity, r, sigma, s0)
    time = paths["time"]
    stock = paths["S"]

    # ===== Hedging Setup =====
    # Define callable functions for option pricing and delta
    def option_price_func(t, strike, spot):
        return bs_call_put_option_price(option_type, spot, strike, sigma, t, maturity, r)

    def delta_func(t, strike, spot):
        return bs_delta(option_type, spot, strike, sigma, t, maturity, r)

    # Initialize portfolio
    pnl = np.zeros((num_paths, num_steps + 1))
    delta_init = delta_func(0.0, strikes, s0)
    pnl[:, 0] = option_price_func(0.0, strikes, s0) - delta_init * s0

    # Track option prices and deltas
    call_matrix = np.zeros((num_paths, num_steps + 1))
    call_matrix[:, 0] = option_price_func(0.0, strikes, s0)
    delta_matrix = np.zeros((num_paths, num_steps + 1))
    delta_matrix[:, 0] = delta_func(0.0, strikes, s0)

    # ===== Dynamic Hedging Loop =====
    for i in range(1, num_steps + 1):
        dt = time[i] - time[i - 1]
        delta_old = delta_func(time[i - 1], strikes, stock[:, i - 1])
        delta_curr = delta_func(time[i], strikes, stock[:, i])

        # Update P&L: accrue interest and rehedge
        pnl[:, i] = pnl[:, i - 1] * np.exp(r * dt) - (delta_curr - delta_old) * stock[:, i]
        call_matrix[:, i] = option_price_func(time[i], strikes, stock[:, i])
        delta_matrix[:, i] = delta_curr

    # Final settlement: pay option payoff and liquidate hedge
    pnl[:, -1] = pnl[:, -1] - np.maximum(stock[:, -1] - np.array(strikes), 0) + delta_matrix[:, -1] * stock[:, -1]

    # ===== Results Analysis =====
    path_id = 13
    plot_single_path_results(time, stock[path_id, :], call_matrix[path_id, :],
                            delta_matrix[path_id, :], pnl[path_id, :])
    plot_pnl_histogram(pnl[:, -1])
    plt.show()

    # Print sample results
    for i in range(num_paths):
        print('path_id={0:2d}, PnL(t_0)={1:0.4f}, PnL(T-1)={2:0.4f}, S(T)={3:0.4f}, max(S(T)-K,0)={4:0.4f}, PnL(T)={5:0.4f}'.format(
            i, pnl[0, 0], pnl[i, -2], stock[i, -1], np.maximum(stock[i, -1] - np.array(strikes), 0)[0], pnl[i, -1]))


if __name__ == "__main__":
    main()
```


## Exercises

**Exercise 1.**
In the BS hedging simulation, the delta is recomputed at each time step. Explain why the hedge ratio changes even if the stock price does not move.

??? success "Solution to Exercise 1"
    Delta depends on time to maturity: $\Delta = N(d_1)$ where $d_1$ involves $\sqrt{T - t}$ in the denominator. As time passes ($t$ increases), $T - t$ decreases, causing $d_1$ to change. For ITM options, delta increases toward 1; for OTM options, it decreases toward 0. Even without stock movement, the passage of time changes the hedge ratio.

---

**Exercise 2.**
The P&L histogram shows a narrow distribution centered at zero. What would happen to this distribution if the hedging frequency were reduced from 1000 to 50 steps?

??? success "Solution to Exercise 2"
    The P&L variance scales as $O(1/N)$ where $N$ is the number of rebalancing steps. Reducing from 1000 to 50 increases variance by factor $1000/50 = 20$, so std increases by $\sqrt{20} \approx 4.5$. The histogram would be much wider, with more extreme outcomes. Some paths would show significant losses, demonstrating the cost of infrequent hedging.

---

**Exercise 3.**
For the path $S_0 = 1$, $K = 0.95$ (ITM call), explain why the initial delta is above 0.5 and how it evolves along a typical path.

??? success "Solution to Exercise 3"
    With $S_0/K = 1/0.95 = 1.053$ (ITM), $d_1 > 0$, so $\Delta = N(d_1) > 0.5$. Along a typical path where $S$ stays near $S_0$: as $T - t$ decreases, $d_1 \to +\infty$ for ITM options, so $\Delta \to 1$. If the stock drops below $K$, delta decreases. The delta path mirrors the "probability of finishing ITM" which resolves to 0 or 1 at expiry.

---

**Exercise 4.**
The final settlement step is $\text{PnL}_T = \text{PnL}_{T^-} - \max(S_T - K, 0) + \Delta_T \cdot S_T$. Explain each term.

??? success "Solution to Exercise 4"
    $\text{PnL}_{T^-}$: accumulated cash from hedging activities. $-\max(S_T - K, 0)$: option payoff the hedger must pay (they sold the call). $+\Delta_T \cdot S_T$: proceeds from liquidating the stock hedge position ($\Delta_T$ shares at price $S_T$). If hedging were perfect, $\Delta_T \cdot S_T$ would exactly offset the payoff when ITM and the cash balance would be zero, giving PnL $= 0$.