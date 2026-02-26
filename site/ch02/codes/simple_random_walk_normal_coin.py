# ============================================================================
# simple_random_walk_SIMPLE_RANDOM_WALK_NORMAL_COIN.py
# ============================================================================
import matplotlib.pyplot as plt
import simple_random_walk as srw

num_paths = 10
num_steps = 1_000

srw_model = srw.SimpleRandomWalk(seed=0)
t, SRW = srw_model.simulate(num_paths, num_steps, step_type=srw.StepType.NORMAL)

fig, ax = plt.subplots(figsize=(12,3))
for i in range(num_paths):
    ax.plot(t, SRW[i], color='blue', alpha=0.3)
ax.set_xlabel("Time")
ax.set_ylabel("Position")
ax.set_title("Simple Random Walk using Fair Coin")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
plt.show()