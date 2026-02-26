# ============================================================================
# coin_flip_COIN_FLIPS_PATHS_ONE_PATH.py
# ============================================================================
import coin_flip as cf
import matplotlib.pyplot as plt
import numpy as np

num_flips = 100 
p_heads = 0.5 

# Simulate coin flips: +1 for heads, -1 for tails
coin_fiipper = cf.CoinFlip(seed=0)
flips = coin_fiipper.flip_coins(num_flips, p_heads)
print("Results:", flips)

# Count heads and tails
heads_count = (num_flips + np.sum(flips)) // 2
tails_count = num_flips - heads_count
print(f"Heads: {heads_count}, Tails: {tails_count}")

# Cumulative sum as random walk
cumsum_flips = np.cumsum(np.insert(flips, 0, 0))

# Plot cumulative sum path
fig, ax = plt.subplots(figsize=(10, 5))
ax.plot(cumsum_flips, marker='o', linestyle='-')
ax.set_xlabel("Number of Flips")
ax.set_ylabel("Cumulative Sum")
ax.set_title("Cumulative Sum of Coin Flips")
ax.axhline(0, color='black', linestyle='--', linewidth=1)
plt.show()