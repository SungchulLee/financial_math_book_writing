"""
SARIMA Models
=============
Seasonal Autoregressive Integrated Moving Average (SARIMA) models for time series
with both ordinary and seasonal correlation structure.

Covers the SARIMA(p, d, q)(P, D, Q)_s framework, including definitions of
seasonal AR and MA polynomials, causality/invertibility conditions, and
simulation of a SARMA(1,1)(1,1)_12 sample path.

Reference: Chapter 5, Applied Time Series Analysis and Forecasting with Python
(Huang & Petukhina, 2022).

Source: "quantitative-finance-notebooks" collection (Notebook 3.2).
"""

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

# =============================================================================
# 1. SARIMA Models
# =============================================================================
#
# Suppose we have a nonstationary time series {X_t} with trend and seasonal
# period s. If the differenced series
#
#     Y_t = (1 - B)^d (1 - B^s)^D X_t
#
# is stationary, then we can find an appropriate model for {Y_t}.
#
# We use an ARMA model to characterize the ordinary correlation of a time
# series: phi(B) Y_t = theta(B) eps_t. For seasonal correlation, we use a
# similar form: Phi(B^s) Y_t = Theta(B^s) eps_t. When a time series has both
# ordinary and seasonal correlation, we combine them into a single model.
#
# -----------------------------------------------------------------------------
# Definition: SARIMA(p, d, q)(P, D, Q)_s
# -----------------------------------------------------------------------------
#
# If d and D are nonnegative integers and B is the backshift operator, then
# {X_t} is a SARIMA(p, d, q)(P, D, Q)_s process with seasonal period s if
# Y_t = (1 - B)^d (1 - B^s)^D X_t is stationary and {X_t} satisfies:
#
#     phi(B) Phi(B^s) (1 - B)^d (1 - B^s)^D X_t = theta(B) Theta(B^s) eps_t
#                                                                       (1.1)
#     eps_t ~ WN(0, sigma_eps^2)
#
# where:
#   phi(z)   = 1 - phi_1 z - ... - phi_p z^p        (AR polynomial)
#   theta(z) = 1 + theta_1 z + ... + theta_q z^q     (MA polynomial)
#   Phi(z)   = 1 - Phi_1 z - ... - Phi_P z^P         (seasonal AR polynomial)
#   Theta(z) = 1 + Theta_1 z + ... + Theta_Q z^Q     (seasonal MA polynomial)
#
# -----------------------------------------------------------------------------
# Key remarks
# -----------------------------------------------------------------------------
#
# - phi(B) and theta(B) model ordinary correlation;
#   Phi(B^s) and Theta(B^s) model seasonal correlation.
#
# - The resulting SARMA(p, q)(P, Q)_s model for Y_t is causal iff
#   phi(z) != 0 and Phi(z) != 0 for all |z| <= 1;
#   it is invertible iff theta(z) != 0 and Theta(z) != 0 for all |z| <= 1.
#
# - Special cases:
#     d = D = 0  =>  SARMA(p, q)(P, Q)_s
#     p = q = d = 0  =>  pure SARIMA(P, D, Q)_s
#     d = D = p = q = 0  =>  pure SARMA(P, Q)_s
#         Q = 0  =>  pure SAR(P)_s
#         P = 0  =>  pure SMA(Q)_s

# =============================================================================
# 2. Simulation of a SARMA(1,1)(1,1)_12 model
# =============================================================================
#
# Model:
#     X_t = 0.7 X_{t-1} + 0.5 eps_{t-1} - 0.3 X_{t-12} + 0.2 eps_{t-12} + eps_t
#
# where eps_t ~ iid N(0, 1).  Sample size N = 192.

N = 192
X = np.zeros(N)
phi_1, theta_1 = 0.7, 0.5
phi_12, theta_12 = -0.3, 0.2
epsilon = ss.norm.rvs(loc=0, scale=1, size=N, random_state=42)
for t in range(1, N):
    X[t] = (phi_1 * X[t - 1]
            + theta_1 * epsilon[t - 1]
            + phi_12 * X[t - 12]
            + theta_12 * epsilon[t - 12]
            + epsilon[t])

# Plot the sample path
plt.figure(figsize=(6, 3))
plt.plot(X)
plt.title('SARMA(1, 1)(1, 1, 12) Sample Path')
plt.xlabel('N')
plt.grid(True)
plt.show()
