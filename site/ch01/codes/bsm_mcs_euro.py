# ---
# title: "BSM Monte Carlo European Option Pricing"
# description: >
#   Monte Carlo valuation of a European call option under the
#   Black-Scholes-Merton model.  This is the simplest possible
#   Monte Carlo example: generate terminal stock prices from the
#   risk-neutral GBM distribution and discount the average payoff.
#
#   The script complements the binomial-tree examples in Chapter 1
#   by showing the continuous-time limit directly via simulation.
#
# origin: "Adapted from Y. Hilpisch, Python for Finance, 2nd ed."
# ---

import math
import numpy as np

# ── Parameters ──────────────────────────────────────────────────
S0 = 100.0       # initial stock price
K = 105.0        # strike price
T = 1.0          # time to maturity (years)
r = 0.05         # risk-free rate (continuous compounding)
sigma = 0.2      # volatility (annualised)
n_sim = 100_000  # number of Monte Carlo paths

# ── Step 1: Generate terminal stock prices under Q ─────────────
# Under the risk-neutral measure the log-stock price satisfies
#   ln S_T = ln S_0 + (r - sigma^2/2) T + sigma sqrt(T) Z,  Z ~ N(0,1)
np.random.seed(42)
z = np.random.standard_normal(n_sim)
ST = S0 * np.exp((r - 0.5 * sigma ** 2) * T + sigma * math.sqrt(T) * z)

# ── Step 2: Compute discounted expected payoff ─────────────────
payoff = np.maximum(ST - K, 0)                      # call payoff
C0 = math.exp(-r * T) * np.mean(payoff)             # MC estimator
se = math.exp(-r * T) * np.std(payoff) / math.sqrt(n_sim)  # standard error

# ── Step 3: Output ─────────────────────────────────────────────
print(f"European Call (BSM Monte Carlo)")
print(f"  S0={S0}, K={K}, T={T}, r={r}, sigma={sigma}")
print(f"  Simulations: {n_sim:,}")
print(f"  Price      : {C0:.4f}")
print(f"  Std Error  : {se:.6f}")
print(f"  95% CI     : [{C0 - 1.96*se:.4f}, {C0 + 1.96*se:.4f}]")
