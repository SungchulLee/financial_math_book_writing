"""
BSM Model I: Replication and Derivation
========================================

This module derives the Black-Scholes-Merton option pricing framework from
first principles, following the replication argument. Starting from the
assumption of geometric Brownian motion for the stock price, we construct
the risk-neutral measure via the Cameron-Martin-Girsanov theorem and
demonstrate that all integrable claims can be replicated by a self-financing
portfolio of stock and bond.

The code implements:
  - Delta (hedge ratio) and bond holding calculations for European options
  - Simulation of realised price paths under GBM
  - Discrete-time delta hedging along a realised path
  - Tracking of hedging error arising from discrete rebalancing

Two complete examples are provided: one where the call option expires in the
money and one where it expires out of the money, illustrating how the hedge
portfolio converges to the option payoff and the nature of discrete hedging
error.

Source: "quantitative-finance-notebooks" collection, Notebook 4.4.
Reference: Baxter and Rennie, Financial Calculus (1996), Chapter 3.
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as ss


# ============================================================================
# 1. Black-Scholes-Merton Model
# ============================================================================
#
# We posit the existence of deterministic r, mu, and sigma such that the bond
# price B_t and the stock price follow:
#
#   B_t = exp(r * t)
#   S_t = S_0 * exp(mu * t + sigma * W_t)
#
# where r is the riskless interest rate, mu is the stock drift, and sigma is
# the stock volatility. There are no transaction costs and both instruments
# are freely and instantaneously tradable either long or short.
#
# --------------------------------------------------------------------------
# 1.1 Zero Interest Rates
# --------------------------------------------------------------------------
#
# For a first run at Black-Scholes, assume r = 0. For an arbitrary claim X,
# knowable by some time horizon T, we find a replicating strategy (phi, psi)
# via a three-step process:
#
#   1. Find a measure Q under which S_t is a martingale.
#   2. Form the process E_t = E_Q(X | F_t).
#   3. Find a previsible process phi_t such that dE_t = phi_t dS_t.
#
# Step one:
#   The stock follows exponential Brownian motion. Applying Ito's lemma to
#   S_t = exp(Y_t) where Y_t = mu*t + sigma*W_t gives:
#
#     dS_t = (mu + 0.5 * sigma^2) * S_t * dt + sigma * S_t * dW_t
#
#   Setting gamma = (mu + 0.5*sigma^2) / sigma, the Cameron-Martin-Girsanov
#   theorem provides a measure Q such that W_tilde = W_t + gamma*t is
#   Q-Brownian motion, yielding:
#
#     dS_t = sigma * S_t * dW_tilde_t
#
#   so Q is the martingale measure for S_t.
#
# Step two:
#   Form the process E_t = E_Q(X | F_t).
#
# Step three:
#   By the martingale representation theorem, there exists a previsible
#   phi_t such that:
#
#     E_t = E_Q(X) + integral_0^t phi_s dS_s
#
# The replicating strategy holds phi_t units of stock and
# psi_t = E_t - phi_t * S_t units of the bond. Since B_t = 1 (r=0),
# V_t = E_t, and the strategy is self-financing with V_T = X.
# The arbitrage price at time 0 is E_Q(X).
#
# Key surprises:
#   1. Replicating strategies exist for arbitrary claims.
#   2. The price is an expectation under Q, not under the real measure P.
#   3. The stock process is simple under its martingale measure.
#
# --------------------------------------------------------------------------
# 1.2 Non-Zero Interest Rates
# --------------------------------------------------------------------------
#
# When r != 0, we work with the discounted stock Z_t = B_t^{-1} * S_t and
# discounted claim B_T^{-1} * X. The SDE for Z_t is:
#
#   dZ_t = Z_t * ((mu - r + 0.5*sigma^2) * dt + sigma * dW_t)
#
# Step one: C-M-G with drift (mu - r + 0.5*sigma^2)/sigma gives Q such that
#   dZ_t = sigma * Z_t * dW_tilde_t  (Z_t is a Q-martingale)
#
# Step two: E_t = E_Q(B_T^{-1} * X | F_t)
#
# Step three: Martingale representation gives phi_t with dE_t = phi_t dZ_t
#
# The portfolio (phi_t, psi_t = E_t - phi_t * Z_t) is self-financing and
# replicates X. Using the product rule d(B_t Z_t) = B_t dZ_t + Z_t dB_t,
# we recover dV_t = phi_t dS_t + psi_t dB_t.
#
# --------------------------------------------------------------------------
# 1.3 Summary
# --------------------------------------------------------------------------
#
# In the Black-Scholes model with S_t = S_0 * exp(mu*t + sigma*W_t) and
# B_t = exp(r*t), all integrable claims X have replicating strategies.
# The arbitrage price is:
#
#   V_t = B_t * E_Q(B_T^{-1} * X | F_t) = exp(-r*(T-t)) * E_Q(X | F_t)
#
# where Q is the martingale measure for the discounted stock.


# ============================================================================
# 2. Black-Scholes Formula
# ============================================================================
#
# The Black-Scholes formula for European call options:
#
#   V(s, T) = s * Phi(d1) - k * exp(-r*T) * Phi(d2)
#
# where:
#   d1 = (log(s/k) + (r + 0.5*sigma^2)*T) / (sigma * sqrt(T))
#   d2 = (log(s/k) + (r - 0.5*sigma^2)*T) / (sigma * sqrt(T))
#
# Put options can be priced via put-call parity.


# ============================================================================
# 3. Explicit Black-Scholes Hedge
# ============================================================================
#
# The hedge (amount of stock held) is the derivative of V w.r.t. stock price:
#
#   phi_t = dV/ds (S_t, T-t) = Phi(d1)
#
# phi is always between 0 and 1 for a call. The bond holding at any time is:
#
#   B_t * psi_t = -k * exp(-r*(T-t)) * Phi(d2)
#
# As maturity approaches:
#   - OTM: both stock and bond holdings go to zero (option worthless)
#   - ITM: stock holding -> 1, bond holding -> -k (replicating the payoff)


# ============================================================================
# Helper Functions
# ============================================================================

def calculate_delta(S0, K, T, r, sigma, payoff='call'):
    """Calculate the Black-Scholes delta (hedge ratio).

    Parameters
    ----------
    S0 : float
        Current stock price.
    K : float
        Strike price.
    T : float
        Time to maturity.
    r : float
        Risk-free interest rate.
    sigma : float
        Volatility.
    payoff : str
        'call' or 'put'.

    Returns
    -------
    float
        Delta of the option.
    """
    d1 = (np.log(S0 / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    if payoff.lower() == 'call':
        return ss.norm.cdf(d1)
    elif payoff.lower() == 'put':
        return ss.norm.cdf(d1) - 1


def calculate_bond_holding(S0, K, T, r, sigma, payoff='call'):
    """Calculate the bond holding in the replicating portfolio.

    Parameters
    ----------
    S0 : float
        Current stock price.
    K : float
        Strike price.
    T : float
        Time to maturity.
    r : float
        Risk-free interest rate.
    sigma : float
        Volatility.
    payoff : str
        'call' or 'put'.

    Returns
    -------
    float
        Value of the bond position (negative indicates borrowing).
    """
    d2 = (np.log(S0 / K) + (r - 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
    if payoff.lower() == 'call':
        return -K * np.exp(-r * T) * ss.norm.cdf(d2)
    elif payoff.lower() == 'put':
        return -K * np.exp(-r * T) * (ss.norm.cdf(d2) - 1)


# ============================================================================
# Parameters
# ============================================================================

T = 1.0                            # time horizon
N = 10                             # number of steps within time horizon
time = np.linspace(0, T, N + 1)    # from 0 to T with N+1 points (inclusive of T)
dt = T / N                         # time step increment
mu = 0.02                          # drift coefficient per unit T
sigma = 0.15                       # volatility per unit T
S0 = 100.0                         # initial asset price
K = 100.0                          # strike price
r = 0.04                           # risk-free rate per unit T


# ============================================================================
# Example 1: Option Expires In The Money
# ============================================================================

# Simulate a realised price path
S = np.zeros(N + 1)
S[0] = S0
Z = ss.norm.rvs(loc=0, scale=1, size=N, random_state=5)
for t in range(1, N + 1):
    S[t] = S[t-1] * np.exp(mu * dt + sigma * np.sqrt(dt) * Z[t-1])

# Plot the realised price path
plt.figure(figsize=(6, 4))
plt.plot(time, S)
plt.title('Realised Price Path')
plt.xlabel('Time')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# Calculate option price at time 0
delta = calculate_delta(S0, K, T, r, sigma, payoff='call')
bond_holding = calculate_bond_holding(S0, K, T, r, sigma, payoff='call')
V0 = delta * S0 + bond_holding

# Print results
print(f"### At t0 ###")
print(f"Stock price (S0): {S0:.2f}")
print(f"Option price (V0): {V0:.2f}")
print(f"Delta (delta): {delta:.2f}")
print(f"Buy delta * S0 of stock: {delta * S0:.2f}")
print(f"Financed by borrowing V0 - delta * S0 = bond_holding: {bond_holding:.2f}")

# Rebalancing through time along the realised price path
deltas = np.zeros(N + 1)
bond_holdings = np.zeros(N + 1)
V = np.zeros(N + 1)
for t in range(N + 1):
    tau = T - t * dt
    if tau <= 0:
        tau = 1e-8    # avoid divide by zero
    deltas[t] = calculate_delta(S[t], K, tau, r, sigma, 'call')
    bond_holdings[t] = calculate_bond_holding(S[t], K, tau, r, sigma, 'call')
    V[t] = deltas[t] * S[t] + bond_holdings[t]

# Calculate realised option payoff at time T
ST = S[-1]
payoff_T = max(ST - K, 0)

# Print results
print(f"### At T ###")
print(f"Stock price (ST): {ST:.2f}")
print(f"Option terminal value (payoff_T): {payoff_T:.2f}")

# Plot option value, delta, and bond holding over time
plt.figure(figsize=(16, 4))

plt.subplot(1, 3, 1)
plt.plot(time, V)
plt.scatter(time[-1], payoff_T, color='red', label='Option Terminal Value')
plt.title('Option Value')
plt.xlabel('Time')
plt.grid(True)
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(time, deltas)
plt.title('Stock Hedge (Delta)')
plt.xlabel('Time')
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(time, bond_holdings)
plt.title('Bond Holding')
plt.xlabel('Time')
plt.grid(True)

plt.tight_layout()
plt.show()

# Create a dataframe to show delta hedging over time
df = pd.DataFrame({
    'time': time,
    'stock_price': S,
    'option_value': V,
    'delta': deltas
})

# How many shares to trade each step
df['delta_change'] = df['delta'].diff()

# Cashflow from trading shares
# negative = you pay cash to buy shares
# positive = you receive cash from selling shares
df.loc[0, 'stock_trade_cashflow'] = -df.loc[0, 'delta'] * df.loc[0, 'stock_price']
df.loc[1:, 'stock_trade_cashflow'] = (-df.loc[1:, 'delta_change'] * df.loc[1:, 'stock_price'])

# Cash account (borrowing)
df['cash_account'] = 0.0

# t = 0: receive option premium, then buy initial delta shares
df.loc[0, 'cash_account'] = V0 + df.loc[0, 'stock_trade_cashflow']

# Propagate through time with interest
for t in range(1, len(df)):
    df.loc[t, 'cash_account'] = (
        df.loc[t - 1, 'cash_account'] * np.exp(r * dt) + df.loc[t, 'stock_trade_cashflow']
    )

# Hedge portfolio value at each step
df['hedge_portfolio_value'] = (df['delta'] * df['stock_price'] + df['cash_account'])

print(df)

print(f"Terminal hedging error: {df['hedge_portfolio_value'].iloc[-1] - payoff_T:.3f}")

# This simulation demonstrates that dynamic delta hedging can approximately
# replicate the payoff of a European option. However, because hedging occurs
# at discrete intervals rather than continuously, a non-zero hedging error
# remains at expiry (which could be positive or negative). The magnitude of
# this error reflects the limitations of discrete rebalancing and the
# sensitivity of option value to nonlinear price movements. As the
# rebalancing frequency increases, the hedging error tends toward zero,
# consistent with Black-Scholes theory.


# ============================================================================
# Example 2: Option Expires Out of The Money
# ============================================================================

# Simulate a realised price path
S = np.zeros(N + 1)
S[0] = S0
Z = ss.norm.rvs(loc=0, scale=1, size=N, random_state=6)
for t in range(1, N + 1):
    S[t] = S[t-1] * np.exp(mu * dt + sigma * np.sqrt(dt) * Z[t-1])

# Plot the realised price path
plt.figure(figsize=(6, 4))
plt.plot(time, S, color='C1')
plt.title('Realised Price Path')
plt.xlabel('Time')
plt.ylabel('Price')
plt.grid(True)
plt.show()

# Calculate option price at time 0
delta = calculate_delta(S0, K, T, r, sigma, payoff='call')
bond_holding = calculate_bond_holding(S0, K, T, r, sigma, payoff='call')
V0 = delta * S0 + bond_holding

# Print results
print(f"### At t0 ###")
print(f"Stock price (S0): {S0:.2f}")
print(f"Option price (V0): {V0:.2f}")
print(f"Delta (delta): {delta:.2f}")
print(f"Buy delta * S0 of stock: {delta * S0:.2f}")
print(f"Financed by borrowing V0 - delta * S0 = bond_holding: {bond_holding:.2f}")

# Rebalancing through time along the realised price path
deltas = np.zeros(N + 1)
bond_holdings = np.zeros(N + 1)
V = np.zeros(N + 1)
for t in range(N + 1):
    tau = T - t * dt
    if tau <= 0:
        tau = 1e-8    # avoid divide by zero
    deltas[t] = calculate_delta(S[t], K, tau, r, sigma, 'call')
    bond_holdings[t] = calculate_bond_holding(S[t], K, tau, r, sigma, 'call')
    V[t] = deltas[t] * S[t] + bond_holdings[t]

# Calculate realised option payoff at time T
ST = S[-1]
payoff_T = max(ST - K, 0)

# Print results
print(f"### At T ###")
print(f"Stock price (ST): {ST:.2f}")
print(f"Option terminal value (payoff_T): {payoff_T:.2f}")

# Plot option value, delta, and bond holding over time
plt.figure(figsize=(16, 4))

plt.subplot(1, 3, 1)
plt.plot(time, V, color='C1')
plt.scatter(time[-1], payoff_T, color='red', label='Option Terminal Value')
plt.title('Option Value')
plt.xlabel('Time')
plt.grid(True)
plt.legend()

plt.subplot(1, 3, 2)
plt.plot(time, deltas, color='C1')
plt.title('Stock Hedge (Delta)')
plt.xlabel('Time')
plt.grid(True)

plt.subplot(1, 3, 3)
plt.plot(time, bond_holdings, color='C1')
plt.title('Bond Holding')
plt.xlabel('Time')
plt.grid(True)

plt.tight_layout()
plt.show()

# Create a dataframe to show delta hedging over time
df = pd.DataFrame({
    'time': time,
    'stock_price': S,
    'option_value': V,
    'delta': deltas
})

# How many shares to trade each step
df['delta_change'] = df['delta'].diff()

# Cashflow from trading shares
# negative = you pay cash to buy shares
# positive = you receive cash from selling shares
df.loc[0, 'stock_trade_cashflow'] = -df.loc[0, 'delta'] * df.loc[0, 'stock_price']
df.loc[1:, 'stock_trade_cashflow'] = (-df.loc[1:, 'delta_change'] * df.loc[1:, 'stock_price'])

# Cash account (borrowing)
df['cash_account'] = 0.0

# t = 0: receive option premium, then buy initial delta shares
df.loc[0, 'cash_account'] = V0 + df.loc[0, 'stock_trade_cashflow']

# Propagate through time with interest
for t in range(1, len(df)):
    df.loc[t, 'cash_account'] = (
        df.loc[t-1, 'cash_account'] * np.exp(r * dt) + df.loc[t, 'stock_trade_cashflow']
    )

# Hedge portfolio value at each step
df['hedge_portfolio_value'] = (df['delta'] * df['stock_price'] + df['cash_account'])

print(df)

print(f"Terminal hedging error: {df['hedge_portfolio_value'].iloc[-1] - payoff_T:.3f}")
