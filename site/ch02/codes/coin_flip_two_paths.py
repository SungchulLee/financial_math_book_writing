# ============================================================================
# coin_flip_COIN_FLIPS_PATHS_TWO_PATHS.py
# ============================================================================
import coin_flip as cf
import matplotlib.pyplot as plt
import numpy as np

num_flips = 100 
num_paths = 2 
p_heads = 0.5 

# Initialize coin flipper with a fixed seed for reproducibility
coin_fiipper = cf.CoinFlip(seed=0)

# Simulate coin flips: +1 for heads, -1 for tails
flips = coin_fiipper.flip_coins(num_flips, p_heads, num_paths)
# print(flips.shape)

# Compute cumulative sums for each path (starting from 0)
cumsum_flips = np.cumsum(np.insert(flips, 0, 0, axis=1), axis=1)
# print(cumsum_flips.shape)

# Plot cumulative sum path
fig, ax = plt.subplots(figsize=(12, 6))
for i in range(num_paths):
    ax.plot(cumsum_flips[i], label=f'Path {i + 1}', alpha=0.7, marker="o", ms=2)
ax.set_xlabel("Number of Flips")
ax.set_ylabel("Cumulative Sum")
ax.set_title(f"Simulated Coin Flip Paths ({num_paths} paths)")
ax.axhline(0, color='black', linestyle='--', linewidth=1)
if num_paths <= 10:
    ax.legend()
plt.show()

# Display the matrix of coin flips
print("\nMatrix of Coin Flips (-1 = Tails, +1 = Heads):\n")
print(flips)

# Count the total number of heads and tails for each path
heads_count = (num_flips + np.sum(flips, axis=1)) // 2
tails_count = num_flips - heads_count

# Display the counts for each path
for i in range(num_paths):
    print(f"Path {i + 1}: Heads = {heads_count[i]}, Tails = {tails_count[i]}")