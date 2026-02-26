"""
BSM Model II: Pricing Methods
==============================

Implements three approaches for pricing European options under the
Black-Scholes-Merton framework:

1. **Closed-form formula** -- the classical BSM analytical solution.
2. **Monte Carlo simulation** -- risk-neutral expectation estimated via
   sampling terminal stock prices.
3. **Binomial tree** -- Cox-Ross-Rubinstein lattice backward induction.

Each method is demonstrated for both call and put options, and results are
cross-checked with put-call parity.

Source
------
From the "quantitative-finance-notebooks" collection
(Notebook 4.5 -- Black-Scholes-Merton Model II).
Reference: Shreve (2008), *Stochastic Calculus for Finance II*;
Cantarutti (2019), Financial-Models-Numerical-Methods.
"""

import numpy as np
import scipy.stats as ss

# ============================================================================
# 1. Black-Scholes Closed Formula
# ============================================================================
#
# Consider a European call option that pays (S(T) - K)^+ at time T. The
# strike price K is some nonnegative constant. Black, Scholes, and Merton
# argued that the value of this call at any time should depend on the time
# (more precisely, on the time to expiration) and on the value of the stock
# price at that time, and of course it should also depend on a constant rate
# of interest r, the volatility of the stock sigma, and the contractual
# strike price K.
#
# Using the Ito-Doeblin formula, we derive the BSM PDE. Let the stock price
# S(t) follow a geometric Brownian motion:
#
#   dS(t) = alpha * S(t) dt + sigma * S(t) dW(t)
#
# Let c(t, S(t)) be the price at time t of a European call paying
# (S(T) - K)^+ at expiration time T. The delta-hedging rule gives:
#
#   Delta(t) = c_x(t, S(t))                                         (1.1)
#
# and the Black-Scholes-Merton PDE:
#
#   c_t + r*x*c_x + 0.5*sigma^2*x^2*c_xx = r*c
#
# with boundary conditions:
#   c(T, x) = (x - K)^+
#   c(t, 0) = 0
#   lim_{x->inf} [c(t,x) - (x - e^{-r(T-t)} K)] = 0
#
# The closed-form solution is:
#
#   c(t, x) = x * N(d1) - K * e^{-r(T-t)} * N(d2)                  (1.2)
#
# where:
#   d1 = [ln(x/K) + (r + 0.5*sigma^2)(T-t)] / [sigma * sqrt(T-t)]
#   d2 = d1 - sigma * sqrt(T-t)
#
# and N is the standard normal CDF. N(d1) and N(d2) can be interpreted as
# the risk-neutral probabilities of S(T) > K in the stock and money market
# numeraires respectively.


def closed_formula(S0, K, T, r, sigma, payoff='call'):
    """
    Calculate the price of a European option using the Black-Scholes closed formula.

    Args:
        S0 (float): Initial price (current price).
        K (float): Strike price of the option.
        T (float): Time to expiration (in years).
        r (float): Annual risk-free interest rate.
        sigma (float): Annual volatility (standard deviation of the returns).
        payoff (Literal['call', 'put']): Option payoff ('call' or 'put'). Defaults to 'call'.

    Returns:
        float: The estimated price of the option using the Black-Scholes closed formula.
    """
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    if payoff == 'call':
        return S0 * ss.norm.cdf(d1) - K * np.exp(-r * T) * ss.norm.cdf(d2)
    elif payoff == 'put':
        return K * np.exp(-r * T) * ss.norm.cdf(-d2) - S0 * ss.norm.cdf(-d1)


# ============================================================================
# 1.3 Put-Call Parity
# ============================================================================
#
# Put-call parity defines a relationship between the price of a European
# call option and European put option, both with the identical strike price
# and expiry: a portfolio of a long call and a short put is equivalent to
# a single forward contract at this strike price and expiry.
#
#   C(t) - P(t) = S(t) - K * e^{-r(T-t)}


# ============================================================================
# 2. Monte Carlo Method
# ============================================================================
#
# Simulate terminal stock prices:
#
#   S_T^i = S0 * exp{(r - 0.5*sigma^2)*T + sigma*W_T^i}
#
# for 1 <= i <= M.
#
# The Monte Carlo estimate for a European option price is based on
# approximating the risk-neutral expected discounted payoff:
#
#   E^Q[(S_T - K)^+ | S0] ~ (1/N) * sum_{i=1}^{N} (S_T^i - K)^+


def monte_carlo_method(S0, K, T, r, sigma, M, payoff='call', seed=None):
    """
    Calculate the price of a European option using Monte Carlo simulation.

    Args:
        S0 (float): Initial price (current price).
        K (float): Strike price of the option.
        T (float): Time to expiration (in years).
        r (float): Annual risk-free interest rate.
        sigma (float): Annual volatility (standard deviation of the returns).
        M (int): Number of Monte Carlo simulations.
        payoff (Literal['call', 'put']): Option payoff ('call' or 'put'). Defaults to 'call'.
        seed (Union[int, None]): Random seed for reproducibility. Defaults to None.

    Returns:
        tuple containing:
            - V (float): The estimated price of the option using Monte Carlo simulation.
            - std_err (float): The standard error of the option price using Monte Carlo simulation.
    """
    # Generate random normal variables for Brownian motion
    W = ss.norm.rvs(loc=(r - 0.5 * sigma**2) * T, scale=sigma * np.sqrt(T), size=M, random_state=seed)

    # Calculate terminal prices
    ST = S0 * np.exp(W)

    # Calculate discounted payoffs for call and put options
    if payoff == 'call':
        payoffs = np.exp(-r * T) * np.maximum(ST - K, 0)
        std_err = ss.sem(np.exp(-r * T) * np.maximum(ST - K, 0))
    elif payoff == 'put':
        payoffs = np.exp(-r * T) * np.maximum(K - ST, 0)
        std_err = ss.sem(np.exp(-r * T) * np.maximum(K - ST, 0))
    else:
        raise ValueError("Invalid payoff type. Specify 'call' or 'put'!")

    V = np.mean(payoffs)

    return V, std_err


# ============================================================================
# 3. Binomial Method
# ============================================================================
#
# The binomial option pricing model is a discrete-time model used to price
# European-style options by modeling the price evolution of the underlying
# asset over time.
#
# At each time step dt, the underlying asset price can move up or down:
#
#   u = exp(sigma * sqrt(dt)),   d = 1/u
#
# The risk-neutral probability of an up movement is:
#
#   p = (exp(r * dt) - d) / (u - d)
#
# A binomial tree is constructed starting from the initial stock price S0.
# The tree evolves over N time steps, where dt = T/N. At each step, the
# stock price can move up to u*S0 or down to d*S0. Under the risk-neutral
# measure, the expected discounted payoff equals the current option price.


def binomial_method(S0, K, T, r, sigma, N, payoff='call'):
    """
    Calculate the price of a European option using the binomial option pricing model.

    Args:
        S0 (float): Initial price (current price).
        K (float): Strike price of the option.
        T (float): Time to expiration (in years).
        r (float): Annual risk-free interest rate.
        sigma (float): Annual volatility (standard deviation of the returns).
        N (int): Number of time steps in the binomial model.
        payoff (Literal['call', 'put']): Option payoff ('call' or 'put'). Defaults to 'call'.

    Returns:
        float: The estimated price of the option using the binomial model.
    """
    dt = T / N                         # time step increment
    u = np.exp(sigma * np.sqrt(dt))    # up factor
    d = 1.0 / u                        # down factor

    # Initialize price vector and calculate terminal price array
    V = np.zeros(N + 1)
    ST = np.array([S0 * u**j * d**(N - j) for j in range(N + 1)])

    # Risk-neutral probabilities
    p = (np.exp(r * dt) - d) / (u - d)
    q = 1.0 - p

    # Determine option payoff type
    if payoff == 'call':
        V[:] = np.maximum(ST - K, 0.0)
    elif payoff == 'put':
        V[:] = np.maximum(K - ST, 0.0)
    else:
        raise ValueError("Invalid payoff type. Specify 'call' or 'put'!")

    # Backward iteration through the tree
    for i in range(N - 1, -1, -1):
        V[:-1] = np.exp(-r * dt) * (p * V[1:] + q * V[:-1])

    # Return the calculated option price
    return V[0]


# ============================================================================
# Main -- run demonstrations
# ============================================================================

if __name__ == "__main__":

    # Define parameters
    S0 = 100.0     # spot price
    K = 100.0      # strike price
    T = 1.0        # time to expiration (in years)
    r = 0.04       # annual risk free rate
    sigma = 0.2    # annual volatility rate

    # ------------------------------------------------------------------
    # 1. Closed-form prices
    # ------------------------------------------------------------------
    call = closed_formula(S0, K, T, r, sigma, 'call')
    put = closed_formula(S0, K, T, r, sigma, 'put')

    print("=" * 55)
    print("Black-Scholes Closed Formula")
    print("=" * 55)
    print(f"Call price: {call:.3f}")
    print(f"Put price:  {put:.3f}")

    # ------------------------------------------------------------------
    # 1.3 Put-call parity check
    # ------------------------------------------------------------------
    put_call_parity = put + S0 - K * np.exp(-r * T)

    print(f"\nPut-call parity check:")
    print(f"  Call price:            {call:.3f}")
    print(f"  Put-call parity price: {put_call_parity:.3f}")

    # ------------------------------------------------------------------
    # 2. Monte Carlo prices
    # ------------------------------------------------------------------
    call_mc, call_mc_err = monte_carlo_method(S0, K, T, r, sigma, M=10000000, payoff='call', seed=42)
    put_mc, put_mc_err = monte_carlo_method(S0, K, T, r, sigma, M=10000000, payoff='put', seed=42)

    print("\n" + "=" * 55)
    print("Monte Carlo Method")
    print("=" * 55)
    print(f"Call price: {call_mc:.3f}, std error: {call_mc_err:.6f}")
    print(f"Put price:  {put_mc:.3f}, std error: {put_mc_err:.6f}")

    # ------------------------------------------------------------------
    # 3. Binomial tree prices
    # ------------------------------------------------------------------
    call_bn = binomial_method(S0, K, T, r, sigma, N=15000, payoff='call')
    put_bn = binomial_method(S0, K, T, r, sigma, N=15000, payoff='put')

    print("\n" + "=" * 55)
    print("Binomial Method")
    print("=" * 55)
    print(f"Call price: {call_bn:.3f}")
    print(f"Put price:  {put_bn:.3f}")
