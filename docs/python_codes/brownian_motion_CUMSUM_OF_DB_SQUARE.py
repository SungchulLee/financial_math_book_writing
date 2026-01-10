# ============================================================================
# brownian_motion_CUMSUM_OF_DB_SQUARE.py
# ============================================================================
import brownian_motion as bmw
import matplotlib.pyplot as plt
import numpy as np

# Simulation parameters
num_paths = 1_000
num_steps = 10_000
T = 2

# Instantiate and simulate
bm = bmw.BrownianMotion(maturity_time=T, seed=0)
result = bm.simulate(num_paths=num_paths, num_steps=num_steps)

# Extract results
t = result.time_steps                # shape: (num_steps + 1,)
dB = result.increments               # shape: (num_paths, num_steps)
cumsum_dB_square = np.concatenate(
    [np.zeros((num_paths, 1)), np.cumsum(dB**2, axis=1)],
    axis=1
)

# Plotting
fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 4))

# Sample path plots
ax0.set_title(r'Ten Sample Paths of $\sum (dB)^2$')
for i in range(10):
    ax0.plot(t, cumsum_dB_square[i])

# Histogram of final values
ax1.set_title(fr'Distribution of $\sum (dB)^2$ at $T={T}$')
ax1.hist(cumsum_dB_square[:, -1], bins=100, density=True)

plt.tight_layout()
plt.show()