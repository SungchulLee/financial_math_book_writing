# ============================================================================
# brownian_motion_BROWNIAN_MOTION.py
# ============================================================================
import brownian_motion as bmw
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Set simulation parameters
num_paths = 10_000  # Number of Brownian motion paths
num_steps = 1_000   # Number of time steps
maturity_time = 2   # Maturity time for Brownian motion (T = 2)

# Instantiate the BrownianMotion class and run the Monte Carlo simulation
bm = bmw.BrownianMotion(maturity_time=maturity_time, seed=0)
result = bm.simulate(num_paths, num_steps)
time_steps = result.time_steps
brownian_paths = result.brownian_paths

# Create a figure with two subplots to display sample paths and final distribution
fig, (ax_paths, ax_distribution) = plt.subplots(1, 2, figsize=(12, 4))

# Plot 10 sample paths of the Brownian motion
ax_paths.set_title(f'Ten Sample Paths of $B_t$')
for i in range(10):
    ax_paths.plot(time_steps, brownian_paths[i, :], alpha=0.5)

# Plot the distribution of the Brownian motion at maturity (t = T)
ax_distribution.set_title(f'Distribution of $B_{{{maturity_time}}}$')
_, bin_locations, _ = ax_distribution.hist(brownian_paths[:, -1], bins=100, density=True, alpha=0.5, label=f"$B_{{{maturity_time}}}$ Samples")
x_values = bin_locations
y_values = stats.norm(loc=0, scale=np.sqrt(maturity_time)).pdf(x_values)
ax_distribution.plot(x_values, y_values, '--r', label=f"$N(0,{maturity_time})$ PDF")
ax_distribution.legend()

for ax in (ax_paths, ax_distribution):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_position("zero")
plt.tight_layout()
plt.show()