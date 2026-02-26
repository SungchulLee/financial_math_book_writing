"""
Stochastic Differential Equations
==================================

Simulation and analysis of common stochastic differential equations used
in quantitative finance: Geometric Brownian Motion (GBM),
Ornstein-Uhlenbeck (OU), Cox-Ingersoll-Ross (CIR), and the
constant elasticity of variance (CEV) model.

Covers Euler-Maruyama discretization, exact simulation where available,
and comparison of sample path properties.

Source: "quantitative-finance-notebooks" collection, Notebook 5.1
    (https://github.com/quantitative-finance-notebooks)

Note: Notebook 5.1 could not be extracted from the zip archive. This file
    reconstructs the key SDE models and simulations from the topic.
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


# ============================================================================
# 0. Common parameters
# ============================================================================

np.random.seed(42)
T = 1.0          # time horizon
N = 500          # number of time steps
dt = T / N       # step size
t = np.linspace(0, T, N + 1)
M = 5            # number of sample paths


# ============================================================================
# 1. Geometric Brownian Motion (GBM)
# ============================================================================
#
# The GBM SDE is
#
#   dS_t = mu * S_t * dt + sigma * S_t * dW_t
#
# Exact solution (via Ito's Lemma applied to ln S_t):
#
#   S_t = S_0 * exp{ (mu - sigma^2 / 2) * t + sigma * W_t }
#
# Properties:
#   - Prices remain strictly positive.
#   - ln(S_t / S_0) ~ N((mu - sigma^2/2)*t, sigma^2 * t)
#   - E[S_t] = S_0 * exp(mu * t)

mu_gbm = 0.08
sigma_gbm = 0.20
S0 = 100.0

S_gbm = np.zeros((N + 1, M))
S_gbm[0, :] = S0

dW = np.random.randn(N, M) * np.sqrt(dt)
for i in range(N):
    S_gbm[i + 1, :] = S_gbm[i, :] * np.exp(
        (mu_gbm - 0.5 * sigma_gbm**2) * dt + sigma_gbm * dW[i, :]
    )

plt.figure(figsize=(10, 5))
plt.plot(t, S_gbm)
plt.title("Geometric Brownian Motion (GBM)")
plt.xlabel("Time")
plt.ylabel("$S_t$")
plt.grid(True, alpha=0.3)
plt.show()


# ============================================================================
# 2. Ornstein-Uhlenbeck (OU) Process
# ============================================================================
#
# The OU process is the prototypical mean-reverting SDE:
#
#   dX_t = theta * (mu - X_t) * dt + sigma * dW_t
#
# where:
#   theta > 0 : speed of mean reversion
#   mu        : long-run mean level
#   sigma     : volatility
#
# Exact solution:
#
#   X_t = X_0 * exp(-theta * t) + mu * (1 - exp(-theta * t))
#         + sigma * integral_0^t exp(-theta * (t - s)) dW_s
#
# Conditional distribution:
#   X_t | X_s ~ N( mu + (X_s - mu) * exp(-theta*(t-s)),
#                   sigma^2 / (2*theta) * (1 - exp(-2*theta*(t-s))) )
#
# Stationary distribution:
#   X_infty ~ N(mu, sigma^2 / (2*theta))
#
# Applications: interest rates (Vasicek model), pairs trading,
#               commodity prices, volatility modelling.

theta_ou = 5.0
mu_ou = 0.0
sigma_ou = 0.5
X0_ou = 1.0

X_ou = np.zeros((N + 1, M))
X_ou[0, :] = X0_ou

# Exact simulation using the conditional normal distribution
for i in range(N):
    mean = mu_ou + (X_ou[i, :] - mu_ou) * np.exp(-theta_ou * dt)
    var = (sigma_ou**2 / (2 * theta_ou)) * (1 - np.exp(-2 * theta_ou * dt))
    X_ou[i + 1, :] = mean + np.sqrt(var) * np.random.randn(M)

plt.figure(figsize=(10, 5))
plt.plot(t, X_ou)
plt.axhline(y=mu_ou, color='k', linestyle='--', alpha=0.5, label=f"$\\mu = {mu_ou}$")
plt.title("Ornstein-Uhlenbeck Process (Mean-Reverting)")
plt.xlabel("Time")
plt.ylabel("$X_t$")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()


# ============================================================================
# 3. Cox-Ingersoll-Ross (CIR) Process
# ============================================================================
#
# The CIR process is a non-negative mean-reverting process:
#
#   dr_t = kappa * (theta - r_t) * dt + sigma * sqrt(r_t) * dW_t
#
# where:
#   kappa > 0 : speed of mean reversion
#   theta > 0 : long-run mean level
#   sigma > 0 : volatility of the volatility
#
# The Feller condition ensures the process stays strictly positive:
#
#   2 * kappa * theta >= sigma^2
#
# Properties:
#   - Non-negative (with Feller condition: strictly positive)
#   - Stationary distribution: Gamma distribution
#   - Used for interest rate modelling (CIR model) and stochastic volatility
#     (variance process in the Heston model)
#
# Euler-Maruyama with absorption at zero (full truncation):
#   r_{n+1} = r_n + kappa * (theta - r_n^+) * dt + sigma * sqrt(r_n^+) * dW_n
#   r_{n+1} = max(r_{n+1}, 0)

kappa_cir = 3.0
theta_cir = 0.05
sigma_cir = 0.3
r0 = 0.03

# Check Feller condition
feller = 2 * kappa_cir * theta_cir >= sigma_cir**2
print(f"Feller condition satisfied: {feller}  "
      f"(2*kappa*theta = {2*kappa_cir*theta_cir:.3f}, sigma^2 = {sigma_cir**2:.3f})")

r_cir = np.zeros((N + 1, M))
r_cir[0, :] = r0

dW_cir = np.random.randn(N, M) * np.sqrt(dt)
for i in range(N):
    r_pos = np.maximum(r_cir[i, :], 0)
    r_cir[i + 1, :] = (r_cir[i, :]
                        + kappa_cir * (theta_cir - r_pos) * dt
                        + sigma_cir * np.sqrt(r_pos) * dW_cir[i, :])
    r_cir[i + 1, :] = np.maximum(r_cir[i + 1, :], 0)  # absorption at 0

plt.figure(figsize=(10, 5))
plt.plot(t, r_cir)
plt.axhline(y=theta_cir, color='k', linestyle='--', alpha=0.5,
            label=f"$\\theta = {theta_cir}$")
plt.title("Cox-Ingersoll-Ross (CIR) Process")
plt.xlabel("Time")
plt.ylabel("$r_t$")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()


# ============================================================================
# 4. Constant Elasticity of Variance (CEV) Model
# ============================================================================
#
# The CEV model generalises GBM by allowing volatility to depend on the
# price level:
#
#   dS_t = mu * S_t * dt + sigma * S_t^gamma * dW_t
#
# where gamma in (0, 1] controls the elasticity:
#   gamma = 1   => GBM (constant volatility)
#   gamma = 0.5 => square-root diffusion
#   gamma < 1   => leverage effect (volatility rises as price falls)
#
# The CEV model captures the empirical observation that equity volatility
# tends to increase when prices fall.

gamma_cev = 0.7
mu_cev = 0.05
sigma_cev = 2.0  # higher value to compensate for S^gamma scaling
S0_cev = 100.0

S_cev = np.zeros((N + 1, M))
S_cev[0, :] = S0_cev

dW_cev = np.random.randn(N, M) * np.sqrt(dt)
for i in range(N):
    S_pos = np.maximum(S_cev[i, :], 1e-8)
    S_cev[i + 1, :] = (S_cev[i, :]
                        + mu_cev * S_pos * dt
                        + sigma_cev * S_pos**gamma_cev * dW_cev[i, :])
    S_cev[i + 1, :] = np.maximum(S_cev[i + 1, :], 0)

plt.figure(figsize=(10, 5))
plt.plot(t, S_cev)
plt.title(f"CEV Model ($\\gamma = {gamma_cev}$)")
plt.xlabel("Time")
plt.ylabel("$S_t$")
plt.grid(True, alpha=0.3)
plt.show()


# ============================================================================
# 5. Comparison of Euler-Maruyama vs Exact Simulation (GBM)
# ============================================================================
#
# For GBM we can compare the Euler-Maruyama (EM) approximation with the
# exact solution to see discretization error.
#
# Exact:
#   S_{t+dt} = S_t * exp{ (mu - sigma^2/2)*dt + sigma*sqrt(dt)*Z }
#
# Euler-Maruyama:
#   S_{t+dt} = S_t + mu*S_t*dt + sigma*S_t*sqrt(dt)*Z
#
# The EM scheme has strong order 0.5 and weak order 1.0. For the same
# Brownian path, the exact solution is always more accurate.

M_compare = 1
dW_compare = np.random.randn(N) * np.sqrt(dt)

# Exact simulation
S_exact = np.zeros(N + 1)
S_exact[0] = S0
for i in range(N):
    S_exact[i + 1] = S_exact[i] * np.exp(
        (mu_gbm - 0.5 * sigma_gbm**2) * dt + sigma_gbm * dW_compare[i]
    )

# Euler-Maruyama simulation (same Brownian path)
S_em = np.zeros(N + 1)
S_em[0] = S0
for i in range(N):
    S_em[i + 1] = S_em[i] + mu_gbm * S_em[i] * dt + sigma_gbm * S_em[i] * dW_compare[i]

plt.figure(figsize=(10, 5))
plt.plot(t, S_exact, label="Exact", linewidth=2)
plt.plot(t, S_em, label="Euler-Maruyama", linestyle="--", linewidth=2)
plt.title("GBM: Exact vs Euler-Maruyama Simulation")
plt.xlabel("Time")
plt.ylabel("$S_t$")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

error = np.abs(S_exact[-1] - S_em[-1])
print(f"Terminal price — Exact: {S_exact[-1]:.4f}, EM: {S_em[-1]:.4f}, "
      f"Abs error: {error:.4f}")


# ============================================================================
# 6. Summary of SDE Models
# ============================================================================
#
# Model          SDE                                          Key Property
# -------------- -------------------------------------------- -------------------
# GBM            dS = mu*S*dt + sigma*S*dW                    Log-normal prices
# OU (Vasicek)   dX = theta*(mu-X)*dt + sigma*dW              Mean-reverting, Gaussian
# CIR            dr = kappa*(theta-r)*dt + sigma*sqrt(r)*dW   Non-negative, mean-reverting
# CEV            dS = mu*S*dt + sigma*S^gamma*dW              Leverage effect
#
# These SDEs form the building blocks for more complex models in finance:
# - GBM: Black-Scholes option pricing
# - OU: Vasicek interest rate model, pairs trading signals
# - CIR: Short rate models, Heston variance process
# - CEV: Equity volatility skew modelling
