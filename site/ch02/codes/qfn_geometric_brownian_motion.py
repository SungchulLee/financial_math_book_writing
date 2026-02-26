"""
Geometric Brownian Motion (GBM)
===============================

Explores geometric Brownian motion with reference to Chapter 3 from
"Stochastic Calculus for Finance II: Continuous-Time Models" (Shreve, 2008).

Covers:
  - Brownian motion fundamentals (martingales, Markov processes, quadratic variation)
  - GBM stochastic differential equation and its analytical solution via Ito's Lemma
  - Euler-Maruyama simulation method
  - Analytical (vectorized) simulation method
  - Multivariate GBM with correlated price paths

Source: "quantitative-finance-notebooks" collection
    Notebook 4.2 - Geometric Brownian Motion
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

# =============================================================================
# 1. Brownian Motion
# =============================================================================
#
# Brownian motion is a continuous stochastic process W(t), t >= 0, that has
# independent, normally distributed increments. For Brownian motion starting
# at 0, if 0 = t_0 < t_1 < ... < t_m, then the increments
#
#   W(t_1) - W(t_0), W(t_2) - W(t_1), ..., W(t_m) - W(t_{m-1})
#
# are independent and normally distributed with
#
#   E[W(t_{i+1}) - W(t_i)] = 0,    Var[W(t_{i+1}) - W(t_i)] = t_{i+1} - t_i.
#
# Two important classes of adapted stochastic processes are martingales and
# Markov processes.
#
# Martingale property:
#   E[M(t) | F(s)] = M(s)   for all 0 <= s <= t <= T.
#
# If E[M(t) | F(s)] >= M(s), we have a submartingale.
# If the inequality is reversed, we have a supermartingale.
#
# Markov property:
#   E[f(X(t)) | F(s)] = g(X(s))
#
# The estimate of f(X(t)) made at time s depends only on the process value
# X(s) at time s and not on the path of the process before time s.
#
# Brownian motion is both a martingale and a Markov process. Its transition
# density is:
#
#   p(tau, x, y) = (1 / sqrt(2*pi*tau)) * exp{ -(y - x)^2 / (2*tau) }
#
# A profound property of Brownian motion is that it accumulates quadratic
# variation at rate one per unit time:
#
#   sum_{j=0}^{m-1} (W(t_{j+1}) - W(t_j))^2  -->  T_2 - T_1
#
# as the partition becomes finer. We write dW(t)*dW(t) = dt.

# =============================================================================
# 2. Geometric Brownian Motion
# =============================================================================
#
# GBM was popularised in financial mathematics by Fisher Black and Myron Scholes
# when they used it to derive the Black-Scholes equation. The SDE which describes
# the evolution of a GBM stochastic process is:
#
#   dS_t = mu * S_t * dt + sigma * S_t * dW_t
#
# where:
#   dS_t  = change in asset price S at time t
#   mu    = drift coefficient (expected rate of return)
#   sigma = volatility coefficient (expected fluctuation)
#   W_t   = Wiener process (Brownian motion)
#
# The solution (via Ito's Lemma), given initial value S_0:
#
#   S_t = S_0 * exp{ (mu - 0.5*sigma^2)*t + sigma*W_t }
#
# The term (mu - 0.5*sigma^2)*t is the deterministic trend, adjusted for the
# volatility's effect on the average growth rate. The term sigma*W_t introduces
# randomness scaled by volatility.
#
# Discretized for numerical simulation:
#
#   S_t = S_0 * exp{ (mu - 0.5*sigma^2)*dt + sigma*sqrt(dt)*Z_t }
#
# where Z_t ~ N(0, 1).
#
# The log-normal distribution of S_t ensures positive asset prices:
#
#   ln(S_t) ~ N( ln(S_0) + (mu - 0.5*sigma^2)*t,  sigma^2 * t )
#
# Expected value and variance:
#
#   E[S_t]   = S_0 * exp(mu * t)
#   Var[S_t] = S_0^2 * exp(2*mu*t) * (exp(sigma^2 * t) - 1)

# -----------------------------------------------------------------------------
# Parameters
# -----------------------------------------------------------------------------
T = 1.0                            # time horizon
N = 252                            # number of steps within time horizon
time = np.linspace(0, T, N + 1)   # from 0 to T with N+1 points (inclusive of T)
dt = T / N                         # time step increment
M = 1000                           # number of simulations
mu = 0.1                           # drift coefficient per unit T
sigma = 0.3                        # volatility per unit T
S0 = 100.0                         # initial asset price

# =============================================================================
# 2.1 Euler-Maruyama Method
# =============================================================================
# Simulates the GBM process step-by-step.

# Initialize an array to store the simulated paths
S = np.zeros((N + 1, M))
S[0, :] = S0

# Simulate the GBM process
Z = ss.norm.rvs(loc=0, scale=1, size=(N, M), random_state=42)
for t in range(1, N + 1):
    S[t, :] = S[t-1, :] * np.exp((mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[t-1, :])

# Plot the simulated price paths
plt.figure(figsize=(6, 4))
plt.plot(time, S)
plt.title('GBM Simulated Price Paths')
plt.xlabel('Time')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# =============================================================================
# 2.2 Analytical Method
# =============================================================================
# Utilizes vectorized operations to compute cumulative sums of log return increments.

# Initialize an array to store the simulated paths
S = np.zeros((N + 1, M))
S[0, :] = S0

# Simulate the GBM process
W = ss.norm.rvs(loc=(mu - 0.5 * sigma**2) * dt, scale=sigma * np.sqrt(dt), size=(N, M), random_state=42
    )
S[1:, :] = S0 * np.exp(np.cumsum(W, axis=0))

# Plot the simulated price paths
plt.figure(figsize=(6, 4))
plt.plot(time, S)
plt.title('GBM Simulated Price Paths')
plt.xlabel('Time')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# =============================================================================
# 2.3 Multivariate GBM
# =============================================================================
#
# GBM can be extended to the case where there are multiple correlated price
# paths. Each price path follows the underlying process:
#
#   dS_t^i = mu_i * S_t^i * dt + sigma_i * S_t^i * dW_t^i
#
# where the Wiener processes are correlated such that:
#
#   E(dW_t^i * dW_t^j) = rho_{i,j} * dt,   with rho_{i,i} = 1.
#
# Covariance between assets:
#
#   Cov(S_t^i, S_t^j) = S_0^i * S_0^j * exp((mu_i + mu_j)*t)
#                        * (exp(rho_{i,j} * sigma_i * sigma_j * t) - 1)
#
# A multivariate formulation with independent driving Brownian motions W_t^j:
#
#   dS_t^i = mu_i * S_t^i * dt + sum_{j=1}^{d} sigma_{i,j} * S_t^i * dW_t^j
#
# where sigma_{i,j} = rho_{i,j} * sigma_i * sigma_j encodes the correlation.

# -----------------------------------------------------------------------------
# Multivariate Parameters
# -----------------------------------------------------------------------------
T = 1.0                                              # time horizon
N = 252                                              # number of steps within time horizon
time = np.linspace(0, T, N + 1)                      # from 0 to T with N+1 points (inclusive of T)
dt = T / N                                           # time step increment
M = 1000                                             # number of simulations
mu = np.array([0.1, 0.12])                           # drift coefficients for each asset per unit T
sigma = np.array([0.3, 0.27])                        # volatility coefficients for each asset per unit T
S0 = np.array([100.0, 80.0])                         # initial asset prices
num_endog = len(S0)                                  # number of assets
cov = np.array([[0.09, 0.04], [0.04, 0.07]])         # covariance matrix

# Initialize an array to store the simulated paths
S = np.zeros((N + 1, M, num_endog))
S[0, :, :] = S0

# Simulate the GBM process
W = ss.multivariate_normal.rvs(mean=(mu - 0.5 * np.diag(cov)) * dt, cov=cov * dt, size=(N, M), random_state=42)
S[1:, :, :] = S0 * np.exp(np.cumsum(W, axis=0))

# Plot the simulated price paths
plt.figure(figsize=(6, 4))
plt.plot(time, S[:, :, 0], color='C0', alpha=0.5)
plt.plot(time, S[:, :, 1], color='C1', alpha=0.25)
plt.title('Multivariate GBM Simulated Price Paths')
plt.xlabel('Time')
plt.ylabel('Price')
plt.grid(True)
plt.show()
