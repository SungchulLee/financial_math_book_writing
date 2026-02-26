"""
Random Variables I -- Discrete and Continuous Probability Distributions
=======================================================================

Explores random variables and fundamental probability distributions,
covering both discrete distributions (uniform, binomial, geometric, Poisson)
and continuous distributions (normal, exponential, gamma, beta, t, chi-squared).

Theory follows chapter 2 of *All of Statistics* (Wasserman, 2004).

Source: "quantitative-finance-notebooks" collection, Notebook 1.2.
"""

import numpy as np
import scipy.stats as ss

# ============================================================================
# 1. Understanding Random Variables and Probability Distributions
# ============================================================================
#
# A random variable represents a numerical outcome of a random process or a
# function that assigns values to each outcome of an experiment. Denoted X,
# random variables are categorized as:
#
#   1. Discrete -- can assume a finite, countable number of values.
#      Example: dice roll in {1, 2, 3, 4, 5, 6}.
#
#   2. Continuous -- can take an infinite number of values.
#      Examples: temperature, height, weight.
#
# Probability Mass Function (PMF) -- for discrete X:
#     f_X(x) = P(X = x)
#
# Cumulative Distribution Function (CDF):
#     F_X(x) = P(X <= x)
#
# Probability Density Function (PDF) -- for continuous X:
#     f_X(x) >= 0 for all x,  integral f_X(x) dx = 1
#     P(a < X < b) = integral_a^b f_X(x) dx
#
#     F_X(x) = integral_{-inf}^{x} f_X(t) dt
#     f_X(x) = F_X'(x)  at points where F_X is differentiable.

# ============================================================================
# 2. Discrete Probability Distributions
# ============================================================================
#
# Notation: X ~ F means "X has distribution F" (not "X is approximately F").

# ----------------------------------------------------------------------------
# 2.1 Uniform Distribution
# ----------------------------------------------------------------------------
# Every value between a and b is equally likely.
#
#     P(x1 < X < x2) = (x2 - x1) / (b - a)
#
# Example: monkey weight uniformly distributed in [20, 40] kg.
#     P(30 < X < 35) = (35 - 30) / (40 - 20) = 0.25

# ----------------------------------------------------------------------------
# 2.2 Binomial Distribution
# ----------------------------------------------------------------------------
# Counts the number of successes in n independent Bernoulli trials.
#
# Properties:
#   1. n repeated trials
#   2. Two possible outcomes per trial
#   3. Constant success probability p
#   4. Independent trials
#
# PMF:  P(X = k) = C(n,k) * p^k * (1-p)^(n-k)
#
# Example: n=12 households, P(own pet) = 0.3.
# What is P(exactly 5 own a pet)?
#     P(X=5) = C(12,5) * 0.3^5 * 0.7^7 = 0.16

n = 12                          # number sampled
k = 5                           # number of successes
p = 0.3                         # probability of success
prob = ss.binom.pmf(k, n, p)    # probability mass function

print(f"Probability that exactly 5 out of 12 sampled own a pet is: {prob:.2f}")

# What is P(at most 1 owns a pet)?
#     P(X <= 1) = P(X=0) + P(X=1)
#     = C(12,0)*0.3^0*0.7^12 + C(12,1)*0.3^1*0.7^11 = 0.09

n = 12                          # number sampled
k = 1                           # number of successes
p = 0.3                         # probability of success
prob = ss.binom.cdf(k, n, p)    # cumulative distribution function

print(f"Probability that at most one of those sampled owns a pet is: {prob:.2f}")

# The Bernoulli distribution is a special case of the binomial with n=1:
#     P(n) = P^n * (1-P)^(1-n)

# ----------------------------------------------------------------------------
# 2.3 Geometric Distribution
# ----------------------------------------------------------------------------
# Describes the probability of k failures before the first success in a
# series of Bernoulli trials.
#
# PMF:  P(X = k) = (1-p)^k * p
#
# Example: fair coin flip, P(heads) = 0.5
#     P(X=0) = (0.5)^0 * 0.5 = 0.5
#     P(X=1) = (0.5)^1 * 0.5 = 0.25
#     P(X=2) = (0.5)^2 * 0.5 = 0.125
#     P(X=3) = (0.5)^3 * 0.5 = 0.0625

# ----------------------------------------------------------------------------
# 2.4 Poisson Distribution
# ----------------------------------------------------------------------------
# Models the number of events in a fixed interval of time or space.
#
# Properties:
#   1. Successes can be counted
#   2. Mean rate lambda is known
#   3. Independent outcomes
#   4. Probability proportional to interval size
#
# PMF:  P(X = k) = lambda^k * exp(-lambda) / k!
#
# Key property: Mean = Variance = lambda
#
# Example: average 3 ticket machines out of operation at a train station.
# P(exactly 5 machines out of operation)?

k = 5                           # number of successes
mu = 3                          # mean of event
prob = ss.poisson.pmf(k, mu)    # probability mass function

print(f"Probability that at a given point in time exactly five machines are out of operation: {prob:.2f}")

# P(more than 2 machines out of operation)?

k = 2                               # number of successes
mu = 3                              # mean of event
prob = 1 - ss.poisson.cdf(k, mu)    # cumulative distribution function

print(f"Probability that at a given point in time more than two machines are out of operation: {prob:.2f}")

# ============================================================================
# 3. Continuous Probability Distributions
# ============================================================================

# ----------------------------------------------------------------------------
# 3.1 Normal Distribution
# ----------------------------------------------------------------------------
# A symmetrical bell-shaped curve defined by mean (mu) and std dev (sigma).
# X ~ N(mu, sigma^2).
#
# PDF:  f(x) = (1 / sqrt(2*pi*sigma^2)) * exp(-(x-mu)^2 / (2*sigma^2))
#
# Characteristics:
#   1. mu is also the mode and median
#   2. Normality check: Q3 - Q2 = Q2 - Q1
#      Right-skewed: (Q3 - Q2) > (Q2 - Q1)
#      Left-skewed:  (Q2 - Q1) > (Q3 - Q2)

# ----------------------------------------------------------------------------
# 3.2 Standard Normal Distribution
# ----------------------------------------------------------------------------
# X has standard normal if mu=0, sigma=1. Denoted Z.
# PDF: phi(z),  CDF: Phi(z).
#
# Standardization formula:  z = (x - mu) / sigma
#
# In a standard normal:
#   68.2% of values within 1 std dev of the mean
#   95.4% of values within 2 std devs of the mean
#   99.8% of values within 3 std devs of the mean
#
# Example: X ~ N(3, 5). Find P(X >= 1).
# P(X > 1) = 1 - P(X < 1) = 1 - Phi((1-3)/sqrt(5)) = 1 - Phi(-0.8944) = 0.81

x = 1                               # x value
mu = 3                              # mean
sigma = np.sqrt(5)                  # standard deviation
z = (x - mu) / sigma                # standardize the x value
prob = 1 - ss.norm.cdf(z)           # cumulative distribution function

print(f"Probability that X is greater than or equal to 1: {prob:.2f}")

# Find q = Phi^{-1}(0.2), i.e., q such that P(X < q) = 0.2.
#
# 0.2 = P(X < q) = Phi((q - mu) / sigma)
# From normal table: Phi(-0.8416) = 0.2
# => -0.8416 = (q - 3) / sqrt(5)
# => q = 3 - 0.8416 * sqrt(5) = 1.1181

z = ss.norm.ppf(0.2)    # inverse CDF of standard normal at 0.2
q = mu + z * sigma      # calculate q using the z-score formula

print(f"q: {q:.4f}")

# ----------------------------------------------------------------------------
# 3.3 Exponential Distribution
# ----------------------------------------------------------------------------
# X ~ Exp(lambda) with rate parameter lambda > 0:
#
#     f(x) = lambda * exp(-lambda * x),  x >= 0
#
# Used to model lifetimes of electronic components and waiting times
# between rare events.
#
# Alternative parameterization with scale beta = 1/lambda:
#     f(x) = (1/beta) * exp(-x/beta),  x >= 0

# ----------------------------------------------------------------------------
# 3.4 Gamma Distribution
# ----------------------------------------------------------------------------
# Gamma function: Gamma(alpha) = integral_0^inf y^(alpha-1) * exp(-y) dy
#
# X ~ Gamma(alpha, beta):
#     f(x) = x^(alpha-1) * exp(-x/beta) / (beta^alpha * Gamma(alpha)),  x > 0
#
# The exponential is Gamma(1, beta).
# If X_i ~ Gamma(alpha_i, beta) are independent, then
#     sum(X_i) ~ Gamma(sum(alpha_i), beta).

# ----------------------------------------------------------------------------
# 3.5 Beta Distribution
# ----------------------------------------------------------------------------
# X ~ Beta(alpha, beta) with alpha > 0, beta > 0:
#
#     f(x) = Gamma(alpha+beta) / (Gamma(alpha)*Gamma(beta))
#            * x^(alpha-1) * (1-x)^(beta-1),   0 < x < 1

# ----------------------------------------------------------------------------
# 3.6 t Distribution
# ----------------------------------------------------------------------------
# X ~ t_nu with nu degrees of freedom:
#
#     f(x) = Gamma((nu+1)/2) / Gamma(nu/2)
#            * 1 / (1 + x^2/nu)^((nu+1)/2)
#
# Similar to normal but with thicker tails.
# Normal corresponds to t with nu = infinity.

# ----------------------------------------------------------------------------
# 3.7 Chi-squared Distribution
# ----------------------------------------------------------------------------
# X ~ chi^2_p with p degrees of freedom:
#
#     f(x) = x^(p/2 - 1) * exp(-x/2) / (Gamma(p/2) * 2^(p/2)),  x > 0
#
# If Z_1, ..., Z_p are independent standard normals, then
#     sum(Z_i^2) ~ chi^2_p.
