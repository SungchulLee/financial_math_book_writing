# ============================================================================
# black_scholes_GREEKS.py
# ============================================================================
import black_scholes as bs
import matplotlib.pyplot as plt
import numpy as np

# Parameters
S = np.array(range(50,151),dtype=np.int64) # underlying prices
K = 100                                    # strike price
T = 1.0                                    # time to maturity (in years)
r = 0.05                                   # risk-free interest rate
sigma = 0.2                                # volatility

# Plotting
fig, axes = plt.subplots(5,1, figsize=(6, 10), constrained_layout=True)

# Delta: price sensitivity to underlying price change
delta_call, delta_put = bs.delta(S, K, T, r, sigma)
axes[0].plot(S, delta_call, label="Call", color="blue", lw=5, alpha=0.3)
axes[0].plot(S, delta_put, label="Put", color="red")
axes[0].set_title("Delta")

# Gamma: delta sensitivity to underlying price change (same for calls and puts)
gamma_call_and_put = bs.gamma(S, K, T, r, sigma)
axes[1].plot(S, gamma_call_and_put, color="blue", lw=5, alpha=0.3)
axes[1].set_title("Gamma")

# Vega: price sensitivity to volatility change (same for calls and puts)
vega_call_and_put = bs.vega(S, K, T, r, sigma)
axes[2].plot(S, vega_call_and_put, color="blue", lw=5, alpha=0.3)
axes[2].set_title("Vega")

# Theta: price sensitivity to time decay
theta_call, theta_put = bs.theta(S, K, T, r, sigma)
axes[3].plot(S, theta_call, label="Call", color="blue", lw=5, alpha=0.3)
axes[3].plot(S, theta_put, label="Put", color="red")
axes[3].set_title("Theta")

# Rho: price sensitivity to interest rate change
rho_call, rho_put = bs.rho(S, K, T, r, sigma)
axes[4].plot(S, rho_call, label="Call", color="blue", lw=5, alpha=0.3)
axes[4].plot(S, rho_put, label="Put", color="red")
axes[4].set_title("Rho")

for i, ax in enumerate(axes):
    for spine in ["top","right"]:
        ax.spines[spine].set_visible(False)
    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_position(("data", 100))
    ax.set_xlabel("Underlying Price $S$")
    ax.set_ylabel("Value")
    ax.grid(False)
    if i not in {1,2}:
        ax.legend()

plt.show()