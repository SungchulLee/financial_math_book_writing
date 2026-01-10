# ============================================================================
# brownian_motion_ITO_AND_STRATONOVICH_INTEGRAL.py
# ============================================================================
import brownian_motion as bmw
import matplotlib.pyplot as plt
import numpy as np

# Parameters
T = 1.0           # Total time
N = 1000          # Number of time steps
seed = 42         # For reproducibility

# Create Brownian motion simulator and generate 1 path
bm = bmw.BrownianMotion(maturity_time=T, seed=seed)
result = bm.simulate(num_paths=1, num_steps=N)

# Extract components
t = result.time_steps
dt = result.time_step_size
W = result.brownian_paths[0]   # Shape: (N+1,)
dW = result.increments[0]      # Shape: (N,)

# Itô Integral: left-point rule → ∑ f(t_i) ΔB_i, with f = B_t
f_left = W[:-1]
ito_integral = np.concatenate(([0], np.cumsum(f_left * dW)))

# Stratonovich Integral: mid-point rule → ∑ (f(t_i)+f(t_{i+1}))/2 * ΔB_i
f_mid = 0.5 * (W[:-1] + W[1:])
stratonovich_integral = np.concatenate(([0], np.cumsum(f_mid * dW)))

# Plot
fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(t, W, label='Brownian Motion', color='blue')
ax.plot(t, ito_integral, '--r', label="Itô Integral")
ax.plot(t, stratonovich_integral, '--g', label="Stratonovich Integral")

# Labels and decoration
ax.set_title(r'Itô vs Stratonovich Integral : $\int_0^TB_tdB_t$', fontsize=25)
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.legend(loc=(0.1,0.8))
for spine in ["top", "right"]:
    ax.spines[spine].set_visible(False)
for spine in ["bottom", "left"]:
    ax.spines[spine].set_position("zero")

plt.tight_layout()
plt.show()