"""
American Options
=================

Exploration of American options, covering stopping times, the perpetual American put,
the fixed-expiration American put (with Monte Carlo pricing via backward induction),
and American calls on dividend-paying and non-dividend-paying assets. The theoretical
discussion follows chapter 8 of *Stochastic Calculus for Finance II: Continuous-Time
Models* (Shreve, 2008).

Source: "quantitative-finance-notebooks" collection (Notebook 5.4 American Options).
"""

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import numpy as np
import scipy.stats as ss

# ============================================================================
# 0. Introduction
# ============================================================================
# The purpose of this script is to explore American options with reference to
# chapter 8 from *Stochastic Calculus for Finance II Continuous-Time Models*
# (Shreve, 2008).

# ============================================================================
# 1. Stopping Times
# ============================================================================
# European option contracts specify an expiration date, and if the option is to
# be exercised at all, the exercise must occur on the expiration date. An
# *American* option allows the owner to choose to exercise at any time up to and
# including the expiration date. Because of this early exercise feature, such an
# option is at least as valuable as its European counterpart. Sometimes the
# difference in value is negligible or even zero, and then American and European
# options are close or exact substitutes. We shall see that the early exercise
# feature for a call on a stock paying no dividends is worthless; American and
# European calls on such a stock have the same price. In other cases, most
# notably put options, the value of this early exercise feature, the so-called
# *early exercise premium*, can be substantial. An intermediate option between
# American and European is *Bermudan*, an option that permits early exercise but
# only on a contractually specified finite set of dates.
#
# Because an American option can be exercised at any time prior to its
# expiration, it can never be worth less than the payoff associated with
# immediate exercise. This is called the *intrinsic value* of the option. In
# contrast to the case for a European option, whose discounted price process is
# a martingale under the risk-neutral measure, the discounted price process of
# an American option is a supermartingale under this measure. The holder of this
# option may fail to exercise at the optimal exercise date, and in this case the
# discounted option price has a tendency to fall; hence, the supermartingale
# property. During any period of time in which it is not optimal to exercise,
# however, the discounted price process behaves as a martingale.
#
# To price an American option, just as with a European option, we could imagine
# selling the option in exchange for some initial capital and then consider how
# to use this capital to hedge the short position in the option. In this case,
# we would need to be ready to pay off the option at all times prior to the
# expiration date because we do not know when it will be exercised.
#
# A stopping time tau is a random variable taking values in [0, inf] satisfying
#
#     {tau <= t} in F(t)   for all t >= 0.
#
# Thus a stopping time tau has the property that the decision to stop at time t
# must be based on information available at time t.

# ============================================================================
# 2. American Put
# ============================================================================

# ----------------------------------------------------------------------------
# 2.1 Perpetual American Put
# ----------------------------------------------------------------------------
# The simplest interesting American option is the *perpetual American put*. It
# is interesting because the optimal exercise policy is not obvious, and it is
# simple because this policy can be determined explicitly. Although this is not
# a traded option, we begin our discussion with it in order to present in a
# simple context the ideas behind the subsequent analysis of more realistic
# options.
#
# The underlying asset has the price process S(t) given by
#
#     dS(t) = r S(t) dt + sigma S(t) dW~(t),                       (2.1.1)
#
# where the interest rate r and the volatility sigma are strictly positive
# constants and W~(t) is a Brownian motion under the risk-neutral probability
# measure P~. The perpetual American put pays K - S(t) if it is exercised at
# time t. This is its intrinsic value.
#
# Let T be the set of all stopping times. The price of the perpetual American
# put is defined to be
#
#     v_*(x) = max_{tau in T} E~[ e^{-r tau} (K - S(tau)) ],       (2.1.2)
#
# where x = S(0) is the initial stock price. In the event that tau = inf, we
# interpret e^{-r tau} (K - S(tau)) to be zero.
#
# The idea behind this is that the owner of the perpetual American put can
# choose an exercise time tau, subject only to the condition that she may not
# look ahead to determine when to exercise. The mathematical formulation of
# this "not look ahead" restriction is that tau must be a stopping time. The
# price of the option at time zero is the risk-neutral expected payoff of the
# option, discounted from the exercise time back to time zero. If the option is
# never exercised, its payoff is zero. The owner of the option should choose the
# exercise strategy that maximizes this expected payoff, discounted back to time
# zero, and thus we define the price of the option to be the maximum over
# tau in T of the discounted expected payoffs.

# ----------------------------------------------------------------------------
# 2.2 Fixed-Expiration American Put
# ----------------------------------------------------------------------------
# Let's now consider an American put on a stock whose price is the same
# geometric Brownian motion in equation (2.1.1), but now the put has a finite
# expiration time T.
#
# Let 0 <= t <= T and x >= 0 be given. Assume S(t) = x. Let F_u^(t),
# t <= u <= T, denote the sigma-algebra generated by the process S(v) as v
# ranges over [t, u], and let T_{t,T} denote the set of stopping times for the
# filtration F_u^(t), t <= u <= T, taking values in [t, T] or taking the value
# infinity. In other words, {tau <= u} in F_u^(t) for every u in [t, T]; a
# stopping time in T_{t,T} makes the decision to stop at a time u in [t, T]
# based only on the path of the stock price between times t and u. The price at
# time t of the American put expiring at time T is defined to be
#
#     v(t, x) = max_{tau in T_{t,T}} E~[ e^{-r(tau - t)} (K - S(tau)) | S(t) = x ].
#
# In the event that tau = inf, we interpret e^{-r tau} (K - S(tau)) to be zero.
# This is the case when the put expires unexercised.
#
# Let's consider an example in Python.

# ---------------------------------------------------------------------------
# Define parameters
# ---------------------------------------------------------------------------
S0 = 100.0      # initial asset price
K = 100.0       # strike price
T = 1.0         # time to maturity
r = 0.04        # risk-free rate per unit T
sigma = 0.2     # volatility per unit T

# ---------------------------------------------------------------------------
# Monte Carlo method -- backward induction for American put pricing
# ---------------------------------------------------------------------------
N = 252
dt = T / N
M = 100000
S = np.zeros((N + 1, M))
S[0, :] = S0

Z = ss.norm.rvs(loc=0, scale=1, size=(N, M), random_state=42)
for t in range(1, N + 1):
    S[t, :] = S[t-1, :] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * Z[t-1, :])

payoffs = np.maximum(K - S, 0)
option_values = payoffs[-1, :]

# Backward induction to determine optimal stopping
for i in range(N - 1, -1, -1):
    discounted_payoff = np.exp(-r * dt) * option_values
    option_values = np.maximum(payoffs[i, :], discounted_payoff)

american_put = np.mean(option_values)
american_put_std_err = ss.sem(option_values)

print(f"The price of the American put option is: {american_put:.3f}"
      f"\nwith standard error: {american_put_std_err:.3f}")

# ============================================================================
# 3. American Call
# ============================================================================

# ----------------------------------------------------------------------------
# 3.1 Underlying Asset Pays No Dividends
# ----------------------------------------------------------------------------
# In the case of a non-dividend-paying asset, American and European calls have
# the same price. The details can be found in Shreve (2008, pp. 361 - 363), but
# are not presented here.

# ----------------------------------------------------------------------------
# 3.2 Underlying Asset Pays Dividends
# ----------------------------------------------------------------------------
# If the asset pays dividends, the prices of American and European calls may
# differ.
#
# Let's consider an American call on an asset that pays dividends whose price
# process is a geometric Brownian motion governed by equation (2.1.1). We assume
# there are times 0 < t_1 < t_2 < ... < t_n < T, and at each time t_j the
# dividend paid is a_j * S(t_j-), where S(t_j-) denotes the asset price just
# prior to the dividend payment. The asset price S(t_j) after the dividend
# payment is the asset price before the dividend payment less the dividend
# payment:
#
#     S(t_j) = S(t_j-) - a_j * S(t_j-) = (1 - a_j) * S(t_j-).
#
# We assume that each a_j, j = 1, ..., n, is a number between 0 and 1. We set
# t_0 = 0, but this is not a dividend payment date. We also assume that T is
# not a dividend payment date, although it is not difficult to modify the
# analysis to handle the case when T is a dividend payment date.
#
# We will not go through the details here, but Shreve (2008, pp. 363 - 368)
# shows that it is not optimal to exercise an American call on this asset except
# possibly immediately before a dividend payment. The price of the call is shown
# to satisfy the Black-Scholes-Merton PDE between dividend payment dates. At
# dividend payment dates, the price of the call is the maximum of the call's
# intrinsic value and the price of the call after the dividend is paid and the
# stock price is reduced by the amount of the payment. These observations lead
# to a recursive algorithm for determining the price.
