"""
Bayesian Inference
==================
Explores Bayesian inference: prior and posterior distributions, Bayes' theorem,
posterior updating with conjugate Beta-Bernoulli model, and visualization of how
the posterior concentrates around the true parameter as data accumulates.

Reference: Chapter 11, *All of Statistics* (Wasserman, 2004).

Source: "quantitative-finance-notebooks" collection.
"""

import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt

# =============================================================================
# 1. The Bayesian Method
# =============================================================================
#
# Frequentist (classical) methods make inferences about a population based on
# observed frequencies or proportions in a sample.  In contrast, Bayesian
# inference treats probability as a measure of belief or uncertainty.
#
# Bayesian inference proceeds as follows:
#
#   1. Choose a prior distribution f(theta) expressing beliefs about the
#      parameter theta before seeing any data.
#
#   2. Choose a statistical model f(x | theta) reflecting beliefs about x
#      given theta.
#
#   3. After observing data X_1, ..., X_n, update beliefs by computing the
#      posterior distribution f(theta | X_1, ..., X_n).
#
# For discrete theta and a single discrete observation X, Bayes' theorem gives:
#
#   P(Theta = theta | X = x)
#       = P(X = x | Theta = theta) P(Theta = theta)
#         / sum_theta P(X = x | Theta = theta) P(Theta = theta)
#
# The continuous version uses density functions:
#
#   f(theta | x) = f(x | theta) f(theta) / int f(x | theta) f(theta) d(theta)
#
# For n IID observations X_1, ..., X_n we replace f(x | theta) with the
# likelihood:
#
#   f(x_1, ..., x_n | theta) = prod_{i=1}^{n} f(x_i | theta) = L_n(theta)
#
# Writing x^n = (x_1, ..., x_n):
#
#   f(theta | x^n) = L_n(theta) f(theta) / c_n  proportional to  L_n(theta) f(theta)
#
# where c_n = int L_n(theta) f(theta) d(theta) is the normalizing constant
# (independent of theta).
#
# Summary:  Posterior  is proportional to  Likelihood x Prior
#
#   f(theta | x^n)  proportional to  L_n(theta) f(theta)
#
# The normalizing constant c_n can always be recovered later when needed.

# =============================================================================
# Posterior point and interval estimates
# =============================================================================
#
# Point estimate -- the posterior mean:
#
#   theta_bar_n = int theta f(theta | x^n) d(theta)
#               = int theta L_n(theta) f(theta) d(theta)
#                 / int L_n(theta) f(theta) d(theta)
#
# Interval estimate -- find a and b such that:
#
#   int_{-inf}^{a} f(theta | x^n) d(theta) = alpha / 2
#   int_{b}^{inf}  f(theta | x^n) d(theta) = alpha / 2
#
# Then C = (a, b) is a (1 - alpha) posterior interval:
#
#   P(theta in C | x^n) = int_a^b f(theta | x^n) d(theta) = 1 - alpha

# =============================================================================
# 2. Example: Beta-Bernoulli Conjugate Model (Coin Flipping)
# =============================================================================
#
# Start with a Beta(1,1) = Uniform prior and simulate 1000 coin flips.
# For various numbers of flips (0, 1, 5, 10, ..., 1000), compute and plot
# the posterior distribution of the probability of heads.
#
# With a Beta(a0, b0) prior and observing h heads in N flips, the posterior is:
#
#   Beta(a0 + h,  b0 + N - h)
#
# Here a0 = b0 = 1 (uniform prior).

dist = ss.beta                                                         # Beta distribution for posterior
n_trials = [0, 1, 5, 10, 50, 100, 500, 1000]                          # number of trials
data = ss.bernoulli.rvs(p=0.5, size=n_trials[-1], random_state=42)    # simulate coin flips
x = np.linspace(0, 1, 100)                                            # points at which to evaluate the Beta pdf

# Plot the posterior distribution
plt.figure(figsize=(8, 5))
for k, N in enumerate(n_trials):
    plt.subplot(3, 4, k + 1)
    heads = data[:N].sum()                                             # number of heads in the first N flips
    y = dist.pdf(x, a=1 + heads, b=1 + N - heads)                     # posterior distribution
    plt.plot(x, y, label=f"Observe {N} tosses\n{heads} heads")
    plt.fill_between(x, 0, y, color='lightblue', alpha=0.4)
    plt.vlines(0.5, 0, max(y), color='k', linestyles='--')            # true probability line
    plt.xlabel('$p$, probability of heads')
    plt.ylabel('Density') if k % 4 == 0 else None
    plt.legend(fontsize=7)
plt.suptitle('Bayesian Updating of Posterior Probabilities', fontsize=12)
plt.tight_layout()
plt.show()

# The posterior probabilities are represented by the curves, and our uncertainty
# is proportional to the width of the curve.  As we observe more data our
# posterior probabilities shift and tighten closer and closer around the true
# value of p = 0.5 (marked by a dashed line).
