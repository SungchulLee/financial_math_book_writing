"""
The Magic of Log Returns
=========================
Explores the properties of log (continuously compounded) returns versus simple
(arithmetic) returns.  Covers calculation of both return types, conversion
between returns and prices, and the relationship between log-normality of
prices and normality of log returns.

Source: "quantitative-finance-notebooks" collection, Notebook 4.1
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================================
# 0. Introduction
# ============================================================================
# The purpose of this script is to explore the magic of log returns.  Methods
# for calculating simple returns, log returns, and conversions from returns to
# prices are clearly explained with simple examples.

# --- Sample price series ---
prices = np.array([50.0, 54.0, 51.0, 56.0, 57.0, 63.0])
dates = pd.date_range(start="2024-01-01", periods=len(prices), freq="D")
S = pd.Series(prices, index=dates)
print(f"Price Series (S) \n\n{S}")

plt.figure(figsize=(5, 3))
plt.plot(S)
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.ylabel("Price")
plt.show()

# ============================================================================
# 1. Simple returns
# ============================================================================
# Simple returns (arithmetic returns) are the most straightforward way to
# calculate returns -- the percentage change in the asset's price over a
# specified period, ignoring the compounding effect.
#
#   r_t = (S_t - S_{t-1}) / S_{t-1}
#       = S_t / S_{t-1} - 1

r = (S / S.shift(1)) - 1
print(f"Simple Returns (r) \n\n{r}")

# ============================================================================
# 2. Log returns
# ============================================================================
# Log returns (continuously compounded returns) take the compounding effect
# into account by computing the natural logarithm of the price ratio:
#
#   R_t = ln(S_t / S_{t-1})

R = np.log(S / S.shift(1))
print(f"Log Returns (R) \n\n{R}")

# ----------------------------------------------------------------------------
# 2.1 The natural logarithm and e
# ----------------------------------------------------------------------------
# The natural logarithm determines the exponent in  y = e^x.  That is,
# ln(y) = x  is equivalent to  y = e^x.
#
# Example: y = 2  =>  x = ln(2) ~ 0.6931  =>  e^x = 2.

y = 2.0
x = np.log(y)
print(f"Original y: {y}")
print(f"x = ln(y): {x}")
print(f"y = e^x: {np.exp(x)}")

# ----------------------------------------------------------------------------
# 2.2 Converting log returns back to prices
# ----------------------------------------------------------------------------
# Given the initial price S_0, the full price series can be recovered via:
#
#   S_t = S_0 * exp( sum_{i=1}^{t} R_i )
#
# The advantage of log returns is their additive nature: summing log returns
# over time is equivalent to multiplying price ratios, thanks to
# ln(a * b) = ln(a) + ln(b).

S0 = S.values[0]
S1_5 = S0 * np.exp(np.cumsum(R.values[1:], axis=0))
S_from_R = np.concatenate([np.array([S0]), S1_5])

plt.figure(figsize=(5, 3))
plt.plot(S, label="Original Price Series")
plt.plot(dates, S_from_R, linestyle="dotted", color="red", label="Reconstructed Price Series")
plt.xlabel("Date")
plt.xticks(rotation=45)
plt.ylabel("Price")
plt.legend(framealpha=0)
plt.show()

# ----------------------------------------------------------------------------
# 2.3 Converting log returns back to simple returns
# ----------------------------------------------------------------------------
# Simple returns can be recovered from log returns via:
#
#   r_t = e^{R_t} - 1

t = 1
print(f"{r.iloc[t]:.6f} = {np.exp(R.iloc[t]) - 1:.6f}")

# ----------------------------------------------------------------------------
# 2.4 Log returns follow a normal distribution
# ----------------------------------------------------------------------------
# Asset prices are commonly modelled as lognormally distributed (ensuring
# non-negative prices).  If prices are lognormal, then log prices -- and hence
# log returns -- are normally distributed:
#
#   ln(S_t / S_0) = ln(S_t) - ln(S_0) = ln(1 + r_t)

t = 1
print(f"{np.log(S.iloc[t] / S0):.6f} = {np.log(S.iloc[t]) - np.log(S0):.6f} = {np.log(1 + r.iloc[t]):.6f}")
