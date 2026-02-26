"""
Jump Processes
==============

Exploration of jump processes in continuous-time finance, covering Poisson processes,
compound Poisson processes, and the Merton jump-diffusion model. Includes both
Euler-Maruyama and analytical (vectorized) simulation methods for the Merton
jump-diffusion process.

Theory is based on Chapter 11 of *Stochastic Calculus for Finance II
Continuous-Time Models* (Shreve, 2008).

Source: From the "quantitative-finance-notebooks" collection.
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss


# =============================================================================
# 1. Poisson Process
# =============================================================================
#
# In the way that Brownian motion is the basic building block for
# continuous-path processes, the Poisson process serves as the starting point
# for jump processes.
#
# To construct a Poisson process, we begin with a sequence tau_1, tau_2, ...
# of independent exponential random variables, all with the same mean 1/lambda.
# An event ("jump") occurs from time to time:
#   - The first jump occurs at time tau_1.
#   - The second occurs tau_2 time units after the first.
#   - The third occurs tau_3 time units after the second, etc.
#
# The tau_k are called the *interarrival times*. The *arrival times* are:
#
#   S_n = sum_{k=1}^{n} tau_k
#
# The *Poisson process* N(t) counts the number of jumps at or before time t:
#
#   N(t) = 0  if 0 <= t < S_1,
#          1  if S_1 <= t < S_2,
#          ...
#          n  if S_n <= t < S_{n+1},
#          ...
#
# At the jump times N(t) is right-continuous: N(t) = lim_{s -> t+} N(s).
# Because the expected time between jumps is 1/lambda, jumps arrive at an
# average rate of lambda per unit time. We say N(t) has *intensity* lambda.


# =============================================================================
# Compound Poisson Process
# =============================================================================
#
# When a Poisson process jumps, it always jumps up one unit. For financial
# models, we need random jump sizes.
#
# Let N(t) be a Poisson process with intensity lambda, and let Y_1, Y_2, ...
# be i.i.d. random variables with mean beta = E[Y_i], independent of N(t).
# The *compound Poisson process* is:
#
#   Q(t) = sum_{i=1}^{N(t)} Y_i,  t >= 0.
#
# Jumps in Q(t) occur at the same times as in N(t), but with random sizes
# Y_1, Y_2, .... The increments of Q(t) are independent:
#
#   Q(s)       = sum_{i=1}^{N(s)} Y_i
#   Q(t)-Q(s)  = sum_{i=N(s)+1}^{N(t)} Y_i     (independent of Q(s))
#
# Q(t)-Q(s) has the same distribution as Q(t-s).
#
# The mean of the compound Poisson process is:
#
#   E[Q(t)] = beta * lambda * t
#
# On average there are lambda*t jumps in [0,t], the average jump size is beta,
# and the number of jumps is independent of the jump sizes.


# =============================================================================
# 2. Jump Processes and Their Integrals
# =============================================================================
#
# We define the stochastic integral  int_0^t Phi(s) dX(s)  where X can have
# jumps. The integrators are right-continuous and of the form:
#
#   X(t) = X(0) + I(t) + R(t) + J(t),                           (2.1)
#
# where:
#   - X(0) is a nonrandom initial condition.
#   - I(t) = int_0^t Gamma(s) dW(s)   is the Ito integral part.
#   - R(t) = int_0^t Theta(s) ds       is the Riemann integral part.
#   - J(t) is an adapted, right-continuous pure jump process with J(0)=0.
#
# The continuous part of X(t) is:
#
#   X^c(t) = X(0) + I(t) + R(t)
#          = X(0) + int_0^t Gamma(s) dW(s) + int_0^t Theta(s) ds
#
# with quadratic variation:
#
#   [X^c, X^c](t) = int_0^t Gamma^2(s) ds
#
# or in differential form:  dX^c(t) dX^c(t) = Gamma^2(t) dt.
#
# J(t) is a pure jump process: it has only finitely many jumps on each
# finite interval (0,T] and is constant between jumps. A Poisson process and
# a compound Poisson process have this property. A compensated Poisson process
# does not because it decreases between jumps.
#
# The Ito-Doeblin formula for jump processes is not covered here but can be
# found on pages 483-492 (Shreve, 2008).


# =============================================================================
# 3. Merton Jump-Diffusion Process
# =============================================================================
#
# The Merton jump-diffusion process is described by the SDE:
#
#   dX_t = mu * S_t dt + sigma * S_t dW + S_t dJ_t,
#
# where J = {J_t, t in [0,T]} is an adapted compound Poisson process:
#
#   J_t = sum_{i=1}^{N_t} Y_i,
#
# N = {N_t, t in [0,T]} is a standard Poisson process with intensity lambda,
# and Y_i ~ N(alpha, xi^2) are the jump sizes with mean alpha and variance xi^2.


# Define parameters
T = 1.0                             # time horizon
N = 252                             # number of steps within time horizon
time = np.linspace(0, T, N + 1)     # from 0 to T with N+1 points (inclusive of T)
dt = T / N                          # time step increment
M = 1000                            # number of simulations
mu = 0.1                            # drift coefficient per unit T
sigma = 0.3                         # volatility per unit T
lambda_jump = 0.18                  # mean number of jumps per unit T
mu_jump = 0.2                       # mean jump size per unit T
sigma_jump = 0.5                    # jump size volatility per unit T
S0 = 100.0                          # initial asset price


# -----------------------------------------------------------------------------
# 3.1 Euler-Maruyama Method
# -----------------------------------------------------------------------------
# Simulates the Merton jump-diffusion process step-by-step.

# Initialize an array to store the simulated paths
S = np.zeros((N + 1, M))
S[0, :] = S0

# Simulate the GBM and jump process
Z = ss.norm.rvs(loc=0, scale=1, size=(N, M), random_state=42)
J_size = ss.norm.rvs(loc=mu_jump, scale=sigma_jump, size=(N, M), random_state=43)
J_occur = ss.poisson.rvs(mu=lambda_jump * dt, size=(N, M), random_state=44)

# Simulate the paths
for t in range(1, N + 1):
    S[t, :] = S[t-1, :] * np.exp(
        (mu - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[t-1, :] + J_size[t-1, :] * J_occur[t-1, :]
    )

# Plot the simulated price paths
plt.figure(figsize=(6, 4))
plt.plot(time, S)
plt.title('Merton Jump-Diffusion Simulated Price Paths')
plt.xlabel('Time')
plt.ylabel('Price')
plt.grid(True)
plt.show()


# -----------------------------------------------------------------------------
# 3.2 Analytical Method
# -----------------------------------------------------------------------------
# Utilizes vectorized operations to compute cumulative sums of log return
# and jump increments.

# Initialize an array to store the simulated paths
S = np.zeros((N + 1, M))
S[0, :] = S0

# Simulate the Merton Jump Diffusion process
Z = ss.norm.rvs(loc=(mu - 0.5 * sigma**2) * dt, scale=sigma * np.sqrt(dt), size=(N, M), random_state=42)
J_size = ss.norm.rvs(loc=mu_jump, scale=sigma_jump, size=(N, M), random_state=43)
J_occur = ss.poisson.rvs(mu=lambda_jump * dt, size=(N, M), random_state=44)

# Calculate the asset price paths
S[1:, :] = S0 * np.exp(np.cumsum(Z, axis=0) + np.cumsum(J_size * J_occur, axis=0))

# Plot the simulated price paths
plt.figure(figsize=(6, 4))
plt.plot(time, S)
plt.title('Merton Jump-Diffusion Simulated Price Paths')
plt.xlabel('Time')
plt.ylabel('Price')
plt.grid(True)
plt.show()
