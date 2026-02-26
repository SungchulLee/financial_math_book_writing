"""
Parametric Inference
====================
Explores parametric inference including the method of moments and maximum
likelihood estimation (MLE), with reference to chapters 6 and 9 from
*All of Statistics* (Wasserman, 2004) and Reid (2020).

Source: "quantitative-finance-notebooks" collection
    Notebook 2.1 - Parametric Inference
"""

import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# 1. Parametric and Nonparametric Models
# =============================================================================
#
# A statistical model F is a set of distributions (or densities or regression
# functions). A parametric model is a set F that can be parameterized by a
# finite number of parameters. For example, if we assume that the data come
# from a normal distribution, then the model is:
#
#   F = { f(x; mu, sigma) = (1 / (sigma * sqrt(2*pi)))
#             * exp( -1/(2*sigma^2) * (x - mu)^2 ),  mu in R, sigma > 0 }
#
# This is a two-parameter model. We write the density as f(x; mu, sigma) to
# show that x is a value of the random variable whereas mu and sigma are
# parameters.
#
# In general, a parametric model takes the form:
#
#   F = { f(x; theta) : theta in Theta }
#
# where theta is an unknown parameter (or vector of parameters) that can take
# values in the parameter space Theta. If theta is a vector but we are only
# interested in one component of theta, we call the remaining parameters
# nuisance parameters. A nonparametric model is a set F that cannot be
# parameterized by a finite number of parameters.

# =============================================================================
# 2. Parametric Inference
# =============================================================================

# -----------------------------------------------------------------------------
# 2.1 The Method of Moments
# -----------------------------------------------------------------------------
#
# The first method for generating parametric estimators is called the method of
# moments. These estimators are not optimal but they are often easy to compute.
# They are also useful as starting values for other methods that require
# iterative numerical routines.
#
# Suppose that the parameter theta = (theta_1, ..., theta_k) has k components.
# For 1 <= j <= k, define the j-th moment:
#
#   alpha_j = E_theta(X^j) = integral of x^j dF_theta(x)
#
# and the j-th sample moment:
#
#   alpha_hat_j = (1/n) * sum_{i=1}^{n} X_i^j
#
# The method of moments estimator theta_hat_n is defined to be the value of
# theta such that:
#
#   alpha_1(theta_hat_n) = alpha_hat_1
#   alpha_2(theta_hat_n) = alpha_hat_2
#       ...
#   alpha_k(theta_hat_n) = alpha_hat_k

# -----------------------------------------------------------------------------
# 2.2 Maximum Likelihood
# -----------------------------------------------------------------------------
#
# The most common method for estimating parameters in a parametric model is the
# maximum likelihood method. Let X_1, ..., X_n be IID with PDF f(x; theta).
#
# The likelihood function is defined by:
#
#   L_n(theta) = prod_{i=1}^{n} f(X_i; theta)
#
# The log-likelihood function is:
#
#   l_n(theta) = log L_n(theta)
#
# The likelihood function is just the joint density of the data, except that we
# treat it as a function of the parameter theta. L_n : Theta -> [0, inf).
# The likelihood function is NOT a density function: in general, L_n(theta)
# does not integrate to 1 (with respect to theta).
#
# The maximum likelihood estimator (MLE), denoted theta_hat_n, is the value of
# theta that maximizes L_n(theta). The maximum of l_n(theta) occurs at the same
# place as the maximum of L_n(theta), so maximizing the log-likelihood leads to
# the same answer. Often, it is easier to work with the log-likelihood.
#
# Example (Reid, 2020): Using the exponential distribution with failure times
# t = [27, 64, 3, 18, 8]. We need an initial estimate for the model parameter
# (lambda), e.g. lambda = 0.1 as a first guess.
#
# Exponential PDF:      f(t) = lambda * exp(-lambda * t)
# Exponential Log-PDF:  ln(f(t)) = ln(lambda) - lambda * t
#
# Substituting lambda = 0.1 and t = [27, 64, 3, 18, 8]:
#
#   L(lambda=0.1 | t) = (ln(0.1) - 0.1*27) + (ln(0.1) - 0.1*64)
#                      + (ln(0.1) - 0.1*3)  + (ln(0.1) - 0.1*18)
#                      + (ln(0.1) - 0.1*8)
#                      = -23.512925

# --- MLE for Exponential Distribution: grid search over lambda ---

t = np.array([27, 64, 3, 18, 8])
lambda_array = np.geomspace(0.01, 0.1, 100)
LL = np.zeros(len(lambda_array))

for i, lambda_value in enumerate(lambda_array):
    loglik = np.log(lambda_value) - lambda_value * t
    LL[i] = loglik.sum()

max_LL = LL[np.argmax(LL)]
max_lambda = lambda_array[np.argmax(LL)]

# Plot the log-likelihood over the range of lambda values
plt.figure(figsize=(5, 3))
plt.plot(lambda_array, LL)
plt.xlabel(r'$\lambda$')
plt.ylabel('Log-likelihood')
plt.scatter(max_lambda, max_LL, color='r',
            label=f'MLE at $\\lambda$ = {max_lambda:.5f}')
plt.legend()
plt.show()
