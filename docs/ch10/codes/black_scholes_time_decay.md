# Time Decay of Option Values

## Background

Black Scholes Time Decay

Educational script demonstrating black scholes time decay concepts.

---

## Code

```python
"""
Black Scholes Time Decay

Educational script demonstrating black scholes time decay concepts.
"""

# ============================================================================
# black_scholes_TIME_DECAY_OF_OPTION_VALUES.py
# ============================================================================
import black_scholes as bs
import matplotlib.pyplot as plt
import numpy as np

# Market parameters


if __name__ == "__main__":
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
```


## Exercises

**Exercise 1.**
For an ITM call ($S = 120$, $K = 100$), its time value is $C - \max(S - K, 0)$. Explain why ITM options have less time value than ATM options.

??? success "Solution to Exercise 1"
    Time value $= C - (S - K)$ for ITM calls. ITM options behave more like the underlying stock (delta close to 1), so the "optionality" component is small. ATM options have the most uncertainty about finishing ITM or OTM, giving maximum time value. The time value is related to the option gamma, which peaks at ATM and decreases for deep ITM/OTM options.

---

**Exercise 2.**
The put time decay curve differs from the call curve. For a deep ITM put ($S = 80$, $K = 100$), explain whether its time value increases or decreases with time to maturity.

??? success "Solution to Exercise 2"
    For a deep ITM put, the value approaches $Ke^{-rT} - S$ as $T$ increases (the discounted strike minus stock price). As $T$ grows, $Ke^{-rT}$ decreases, so the put value actually *decreases* with longer maturity for very deep ITM puts when $r > 0$. This creates a positive theta (unusual!), reflecting the benefit of receiving the exercise proceeds sooner.

---

**Exercise 3.**
At expiry ($T \to 0$), the call value converges to $\max(S - K, 0)$ with a kink at $S = K$. Describe how the time decay curve at $S = K$ approaches zero as $T \to 0$.

??? success "Solution to Exercise 3"
    At $S = K$: the ATM call value is approximately $S\sigma\sqrt{T}/(2\sqrt{2\pi}) \approx 0.4 S\sigma\sqrt{T}$. As $T \to 0$, this vanishes as $\sqrt{T}$, which is a square-root decay. The rate of decay (theta) diverges as $1/\sqrt{T}$, confirming the accelerating time decay near expiry. The call value curve smoothly transitions from a smooth function of $S$ to the kinked payoff.

---

**Exercise 4.**
For three moneyness levels ($S = 80, 100, 120$ with $K = 100$), rank the call options by their rate of time decay at $T = 0.5$.

??? success "Solution to Exercise 4"
    ATM ($S = 100$) has the fastest time decay because gamma and the time value are maximized. ITM ($S = 120$) has moderate decay since its delta is close to 1 and time value is smaller. OTM ($S = 80$) also has moderate decay as its value is mostly time value, but the absolute amount is small. Ranking by absolute theta: ATM > ITM > OTM. Ranking by percentage of value: OTM > ATM > ITM.