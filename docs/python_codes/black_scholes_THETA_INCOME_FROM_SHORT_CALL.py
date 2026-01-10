# ============================================================================
# black_scholes_THETA_INCOME_FROM_SHORT_CALL.py
# ============================================================================
import black_scholes as bs
import matplotlib.pyplot as plt
import numpy as np

S = 100
K = 100
Ts = np.linspace(0.01, 0.5, 100)  # 0.5 years to expiry
r = 0.01
sigma = 0.2

theta_call, _ = bs.theta(S, K, Ts, r, sigma)

plt.plot(Ts, - theta_call, label="Short Call Theta Income", color='orange')
plt.xlabel("Time to Maturity (Years)")
plt.ylabel("Theta (per year)")
plt.title("Theta Income from Short Call Option")
plt.grid(True)
plt.legend()
plt.gca().invert_xaxis()
plt.tight_layout()
plt.show()