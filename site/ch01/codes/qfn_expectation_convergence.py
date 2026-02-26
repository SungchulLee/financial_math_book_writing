"""
Expectation and Convergence
============================
Exploration of expectation, variance, covariance, Taylor series, and convergence
of random variables. Covers manual vs. NumPy/SciPy computations for key
statistical quantities, Taylor series approximations of sin(x), Euler's formula,
and the definitions of convergence in probability and in distribution.

Reference: Chapter 3 of "All of Statistics" (Wasserman, 2004).

Source: From the "quantitative-finance-notebooks" collection.
"""

import math

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as ss

# =============================================================================
# 1. Expectation of a Random Variable
# =============================================================================
#
# The expected value (mean, first moment) of X is defined as:
#
#   E[X] = integral x dF(x)
#        = sum_x x f(x),       if X is discrete
#        = integral x f(x) dx, if X is continuous
#
# assuming the sum (or integral) is well defined. Notation:
#
#   E[X] = EX = integral x dF(x) = mu = mu_X
#
# Think of E[X] as the average (1/n) sum_{i=1}^{n} X_i of a large number
# of IID draws X_1, ..., X_n. The fact that E[X] ~ (1/n) sum X_i is
# formalised by the law of large numbers.

# Generate random variable
n = 1000
x = ss.norm.rvs(size=n, random_state=42)

# Calculate mean
mu_x = np.sum(x) / n

# Print results
print(f"Mean of x (manual calculation): {mu_x:.3f}")
print(f"Mean of x (using numpy): {np.mean(x):.3f}")

# =============================================================================
# 2. Variance and Covariance
# =============================================================================
#
# The variance measures the "spread" of a distribution. For a random variable
# X with mean mu, the variance is:
#
#   sigma^2 = E[(X - mu)^2] = integral (x - mu)^2 dF(x)
#
# The standard deviation is sd(X) = sqrt(V(X)).
#
# For random variables X and Y with means mu_X, mu_Y and standard deviations
# sigma_X, sigma_Y, the covariance is:
#
#   Cov(X, Y) = E[(X - mu_X)(Y - mu_Y)]
#
# and the correlation is:
#
#   rho = Cov(X, Y) / (sigma_X * sigma_Y)

# Calculate variance
var_x = np.sum((x - mu_x) ** 2) / n

# Print results
print(f"\nVariance of x (manual calculation): {var_x:.3f}")
print(f"Variance of x (using numpy): {np.var(x, ddof=0):.3f}")

# Calculate standard deviation
sd_x = np.sqrt(var_x)

# Print results
print(f"\nStandard deviation of x (manual calculation): {sd_x:.3f}")
print(f"Standard deviation of x (using numpy): {np.std(x, ddof=0):.3f}")

# Generate a second random variable
y = 0.8 * x + ss.norm.rvs(scale=0.6, size=n, random_state=34)
mu_y = np.sum(y) / n
var_y = np.sum((y - mu_y) ** 2) / n
sd_y = np.sqrt(var_y)

# Print results
print(f"\nMean of y: {mu_y:.3f}")
print(f"Variance of y: {var_y:.3f}")
print(f"Standard deviation of y: {sd_y:.3f}")

# Calculate covariance
cov_xy = np.sum((x - mu_x) * (y - mu_y)) / n

# Print results
print(f"\nCovariance of x and y (manual calculation): {cov_xy:.3f}")
print(f"Covariance of x and y (using numpy): {np.cov(x, y, ddof=0)[0, 1]:.3f}")

# Covariance matrix
cov_matrix = np.cov(x, y, ddof=0)

# Print results
print(f"\nCovariance matrix: \n{np.round(cov_matrix, 3)}")

# Calculate correlation
corr_xy = cov_xy / (sd_x * sd_y)

# Print results
print(f"\nCorrelation of x and y (manual calculation): {corr_xy:.3f}")
print(f"Correlation of x and y (using numpy): {np.corrcoef(x, y)[0, 1]:.3f}")

# Correlation matrix
corr_matrix = np.corrcoef(x, y)

# Print results
print(f"\nCorrelation matrix: \n{np.round(corr_matrix, 3)}")

# =============================================================================
# 3. Taylor Series
# =============================================================================
#
# The Taylor series of a function is an infinite sum of terms expressed in
# terms of the function's derivatives at a single point. A function f(x)
# may be expanded about a point a (provided the derivatives are smooth
# and exist):
#
#   f(x) = f(a) + f'(a)(x-a) + f''(a)(x-a)^2/2! + f'''(a)(x-a)^3/3! + ...
#
# If a = 0, the expansion is known as a Maclaurin series.
#
# Example: f(x) = sin(x), a = 0
#
#   sin(x) = x - x^3/3! + x^5/5! - ...

X = np.linspace(-5, 5, 1000)
y_sin = np.sin(X)
yT3 = X - X**3 / math.factorial(3)
yT5 = X - X**3 / math.factorial(3) + X**5 / math.factorial(5)
yT7 = X - X**3 / math.factorial(3) + X**5 / math.factorial(5) - X**7 / math.factorial(7)

plt.figure(figsize=(6, 4))
plt.plot(X, y_sin, label="sin(x)")
plt.plot(X, yT3, linestyle="dotted", label="third-order Taylor series")
plt.plot(X, yT5, linestyle="dotted", label="fifth-order Taylor series")
plt.plot(X, yT7, linestyle="dotted", label="seventh-order Taylor series")
plt.ylim(-2.05, 2.05)
plt.title("Taylor Series Approximation of sin(x) about x=0")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend(fontsize=8, framealpha=0)
plt.show()

# -----------------------------------------------------------------------------
# Maclaurin series of e^x
# -----------------------------------------------------------------------------
#
# Since every derivative of e^x equals e^x and e^0 = 1:
#
#   e^x = 1 + x + x^2/2! + x^3/3! + x^4/4! + ...
#
# Euler's formula establishes the relationship between trigonometric functions
# and the complex exponential. Let i = sqrt(-1):
#
#   e^{ix} = 1 + ix + (ix)^2/2! + (ix)^3/3! + ...
#          = (1 - x^2/2! + x^4/4! + ...) + i(x - x^3/3! + x^5/5! + ...)
#          = cos(x) + i sin(x)
#
# The even powers of x form the Taylor series of cos(x), and the odd powers
# (multiplied by i) form the Taylor series of sin(x). This gives Euler's
# formula:
#
#   e^{ix} = cos(x) + i sin(x)

# =============================================================================
# 4. Convergence of Random Variables
# =============================================================================
#
# Let X_1, X_2, ... be a sequence of random variables and let X be another
# random variable. Let F_n denote the CDF of X_n and F the CDF of X.
#
# 1. Convergence in probability:  X_n --P--> X
#    For every epsilon > 0,
#      P(|X_n - X| > epsilon) -> 0  as n -> infinity.
#
# 2. Convergence in distribution:  X_n --d--> X
#      lim_{n -> infinity} F_n(t) = F(t)
#    at all t for which F is continuous.
