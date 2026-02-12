# ============================================================================
# black_scholes_TIME_DECAY_OF_OPTION_VALUES.py
# ============================================================================
import black_scholes as bs
import matplotlib.pyplot as plt
import numpy as np

# Market parameters
r = 0.05        # risk-free rate
sigma = 0.2     # volatility
T = 1.0         # maturity in years
days = np.linspace(0.01, T, 100)  # time to maturity

# Create plots for three moneyness cases
fig, ax = plt.subplots(3, 2, figsize=(14, 9))

# Moneyness scenarios
spot_prices = [80, 100, 120]
labels = ["In-the-money", "At-the-money", "Out-of-the-money"]
K = 100  # fixed strike

for i, S in enumerate(spot_prices):

    ax[i, 0].plot(days, bs.bs_call_price(S, K, days, r, sigma), color='blue')
    ax[i, 0].invert_xaxis()
    ax[i, 0].set_title(f"Call Price: {labels[2 - i]}")
    ax[i, 0].set_xlabel("Time to Maturity (Years)")
    ax[i, 0].set_ylabel("Call Value")
    ax[i, 0].grid(True)

    ax[i, 1].plot(days, bs.bs_put_price(S, K, days, r, sigma), color='red')
    ax[i, 1].invert_xaxis()
    ax[i, 1].set_title(f"Put Price: {labels[i]}")
    ax[i, 1].set_xlabel("Time to Maturity (Years)")
    ax[i, 1].set_ylabel("Put Value")
    ax[i, 1].grid(True)

fig.suptitle("European Call and Put Prices vs. Time to Maturity for Different Moneyness Scenarios", fontsize=16)
plt.tight_layout()
plt.show()