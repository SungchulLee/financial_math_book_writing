"""
Exotic Options
==============

Exploration of exotic (path-dependent) options including barrier options,
lookback options, and Asian options. Each option type is priced using
closed-form formulas where available and Monte Carlo simulation.

Barrier options knock out or knock in when the underlying asset crosses a
barrier level. Lookback options have payoffs based on the maximum (or minimum)
asset price over the option's lifetime. Asian options depend on the time
average of the underlying asset price.

Reference:
    Shreve, S. E. (2008). *Stochastic Calculus for Finance II:
    Continuous-Time Models*, Chapter 7.

Source:
    From the "quantitative-finance-notebooks" collection by Matt Mcd,
    notebook "5.3 Exotic Options".
    See also: Cantarutti (2019), Financial-Models-Numerical-Methods.
"""

import numpy as np
import scipy.stats as ss


# =============================================================================
# Parameters
# =============================================================================

S0 = 100.0      # initial asset price
K = 100.0       # strike price
B = 115.0       # barrier price (used for barrier options)
T = 1.0         # time to maturity
r = 0.04        # risk-free rate per unit T
sigma = 0.2     # volatility per unit T

N = 252          # number of time steps (trading days)
dt = T / N       # time step size
M = 100000       # number of Monte Carlo paths


# =============================================================================
# 1. Barrier Options
# =============================================================================
#
# Barrier options are path-dependent options that either "knock out"
# (become worthless) or "knock in" (activate) when the underlying asset
# price crosses a specified barrier level.
#
# Types:
#   - Up-and-out:  barrier above initial price; knocks out if price rises above it
#   - Down-and-out: barrier below initial price; knocks out if price falls below it
#   - Up-and-in:   pays off only if price rises above the barrier
#   - Down-and-in: pays off only if price falls below the barrier
#
# The underlying asset follows geometric Brownian motion:
#
#   dS(t) = r S(t) dt + sigma S(t) dW~(t)
#
# with solution:
#
#   S(t) = S(0) exp(sigma W^(t))
#
# where W^(t) = alpha*t + W~(t) and alpha = (1/sigma)(r - sigma^2/2).
#
# For the up-and-out call with strike K < B, the payoff is:
#
#   V(T) = (S(T) - K)^+  *  I{max_{0<=t<=T} S(t) <= B}
#
# Using transformed variables:
#   k = (1/sigma) log(K/S(0)),   b = (1/sigma) log(B/S(0))

# ---- 1.1 Up-and-Out Call: Closed Formula ----

d1 = lambda t, x: 1 / (sigma * np.sqrt(t)) * (np.log(x) + (r + 0.5 * sigma**2) * t)
d2 = lambda t, x: 1 / (sigma * np.sqrt(t)) * (np.log(x) + (r - 0.5 * sigma**2) * t)

closed_barrier_u = (
    S0 * (ss.norm.cdf(d1(T, S0 / K)) - ss.norm.cdf(d1(T, S0 / B)))
    - np.exp(-r * T) * K * (ss.norm.cdf(d2(T, S0 / K)) - ss.norm.cdf(d2(T, S0 / B)))
    - B * (S0 / B) ** (-2 * r / sigma**2)
        * (ss.norm.cdf(d1(T, B**2 / (S0 * K))) - ss.norm.cdf(d1(T, B / S0)))
    + np.exp(-r * T) * K * (S0 / B) ** (-2 * r / sigma**2 + 1)
        * (ss.norm.cdf(d2(T, B**2 / (S0 * K))) - ss.norm.cdf(d2(T, B / S0)))
)

print(f"The price of the Up-and-Out call option by closed formula is: {closed_barrier_u:.3f}")

# ---- 1.2 Up-and-Out Call: Monte Carlo ----
# Apply Broadie-Glasserman-Kou continuity correction for discrete monitoring.

beta1 = 0.5826                                       # correction factor
B_adj = B * np.exp(-beta1 * np.sqrt(dt) * sigma)     # adjusted barrier

S = np.zeros((N + 1, M))
S[0, :] = S0

Z = ss.norm.rvs(loc=0, scale=1, size=(N, M), random_state=42)
for t in range(1, N + 1):
    S[t, :] = S[t - 1, :] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[t - 1, :])

MT = np.amax(S, axis=0)
ST = S[-1, :]
payoffs = np.maximum(ST - K, 0)
payoffs[MT >= B_adj] = 0
mc_barrier_u = np.exp(-r * T) * np.mean(payoffs)
mc_barrier_std_err_u = np.exp(-r * T) * ss.sem(payoffs)

print(f"The price of the Up-and-Out call option by Monte Carlo simulation is: {mc_barrier_u:.3f}")
print(f"  standard error: {mc_barrier_std_err_u:.3f}")


# =============================================================================
# 2. Lookback Options
# =============================================================================
#
# A lookback option has a payoff based on the maximum (or minimum) that the
# underlying asset price attains over some time interval prior to expiration.
#
# For a floating-strike lookback option, the payoff is:
#
#   V(T) = Y(T) - S(T)
#
# where Y(T) = max_{0<=u<=T} S(u) is the running maximum of the asset price.
#
# The risk-neutral price at time t is:
#
#   V(t) = E~[e^{-r(T-t)} (Y(T) - S(T)) | F(t)]
#
# Since (S(t), Y(t)) is Markov, there exists v(t, x, y) such that
# V(t) = v(t, S(t), Y(t)).

# ---- 2.1 Floating Strike Lookback: Closed Formula ----

Sy = 100.0      # maximum asset price up to time t (if t = 0, Sy = S0)
z = S0 / Sy     # change of variable

closed_lookback = S0 * (
    (1 + sigma**2 / (2 * r)) * z * ss.norm.cdf(d1(T, z))
    + np.exp(-r * T) * ss.norm.cdf(-d2(T, z))
    - (sigma**2 / (2 * r)) * np.exp(-r * T) * z ** (1 - (2 * r / sigma**2))
        * ss.norm.cdf(-d2(T, 1 / z))
    - z
)

print(f"\nThe price of the Lookback option by closed formula is: {closed_lookback:.3f}")

# ---- 2.2 Floating Strike Lookback: Monte Carlo ----

S = np.zeros((N + 1, M))
S[0, :] = S0

Z = ss.norm.rvs(loc=0, scale=1, size=(N, M), random_state=42)
for t in range(1, N + 1):
    S[t, :] = S[t - 1, :] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[t - 1, :])

YT = np.amax(S, axis=0)
ST = S[-1, :]
payoffs = np.maximum(YT - ST, 0)
mc_lookback = np.exp(-r * T) * np.mean(payoffs)
mc_lookback_std_err = np.exp(-r * T) * ss.sem(payoffs)

print(f"The price of the Lookback option by Monte Carlo simulation is: {mc_lookback:.3f}")
print(f"  standard error: {mc_lookback_std_err:.3f}")


# =============================================================================
# 3. Asian Options
# =============================================================================
#
# An Asian option has a payoff that includes a time average of the underlying
# asset price. The average may be computed from continuous sampling:
#
#   (1/T) integral_0^T S(t) dt
#
# or from discrete sampling:
#
#   (1/m) sum_{j=1}^{m} S(t_j),  where 0 < t_1 < t_2 < ... < t_m = T
#
# The primary motivation for averaging is to make the option's payoff more
# robust against manipulation of the underlying asset price near expiration.
#
# Asian option prices are not known in closed form; they must be computed
# via PDEs or Monte Carlo simulation.

# ---- 3.1 Fixed Strike Asian Call ----
#
# The payoff at time T is:
#
#   V(T) = ( (1/T) integral_0^T S(t) dt  -  K )^+
#
# with risk-neutral price:
#
#   V(t) = E~[e^{-r(T-t)} V(T) | F(t)]

# Monte Carlo method

S = np.zeros((N + 1, M))
S[0, :] = S0

Z = ss.norm.rvs(loc=0, scale=1, size=(N, M), random_state=42)
for t in range(1, N + 1):
    S[t, :] = S[t - 1, :] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[t - 1, :])

AT = np.mean(S, axis=0)
payoffs = np.maximum(AT - K, 0)
mc_asian_fixed = np.exp(-r * T) * np.mean(payoffs)
mc_asian_fixed_std_err = np.exp(-r * T) * ss.sem(payoffs)

print(f"\nThe price of the Fixed Strike Asian Call option by Monte Carlo simulation is: {mc_asian_fixed:.3f}")
print(f"  standard error: {mc_asian_fixed_std_err:.3f}")
