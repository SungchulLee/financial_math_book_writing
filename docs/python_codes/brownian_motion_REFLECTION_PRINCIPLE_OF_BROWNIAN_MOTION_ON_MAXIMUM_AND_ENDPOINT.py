# ============================================================================
# brownian_motion_REFLECTION_PRINCIPLE_OF_BROWNIAN_MOTION_ON_MAXIMUM_AND_ENDPOINT.py
# ============================================================================
import brownian_motion as bmw
import matplotlib.pyplot as plt
import numpy as np

a = 2
b = - 1.5
seed = 0

# Instantiate and search for a valid path
bm = bmw.BrownianMotion(maturity_time=5, seed=seed)
found = False
seed = 0

while not found:
    result = bm.simulate()
    t, dt, sqrt_dt, paths = result.time_steps, result.time_step_size, result.sqrt_time_step_size, result.brownian_paths
    path = paths[0]
    hits_a = np.where(path >= a)[0]
    if len(hits_a) > 0 and path[-1] < b:
        hit_index = hits_a[0]
        found = True
    else:
        seed += 1
        bm.reset_seed(seed)

# Reflect path after hitting 2
reflected_path = path.copy()
reflected_path[hit_index + 1:] = 2 * path[hit_index] - path[hit_index + 1:]

# Plotting the path and its reflection
fig, ax = plt.subplots(figsize=(10, 5))

ax.plot(t, path, label='Original Path', lw=5, alpha=0.3, color="blue")
ax.plot(t, reflected_path, linestyle='-', lw=1, label=f'Reflected Path (after hitting {a})', color="red")

ax.scatter(t[hit_index], path[hit_index], color='blue', zorder=5, label=f'Original Path First Hit At {a}')
ax.scatter(t[-1], path[-1], color='black', zorder=5, label=f'Original Path Last Landing Below {b}')
ax.scatter(t[-1], reflected_path[-1], color='red', zorder=5, label=f'Reflected Path Last Landing Above {a+(a-b)}')

ax.axhline(a, color='blue', linestyle=':', label=f'Level : {a}')
ax.axhline(b, color='black', linestyle=':', label=f'Level : {b}')
ax.axhline(a+(a-b), color='red', linestyle=':', label=f'Level : {a+(a-b)}')

ax.set_title(f'Brownian Motion: Path Hitting {a} and Reflected Beyond')
ax.set_xlabel('Time')
ax.set_ylabel('Value')
ax.legend( loc=(0.05,0.6) )
for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)
for spine in ["bottom","left"]:
    ax.spines[spine].set_position("zero")

fig.tight_layout()
plt.show()