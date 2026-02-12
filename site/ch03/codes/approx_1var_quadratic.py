# ============================================================================
# APPROXIMATE_ONE_VARIABLE_FUNCTION_QUADRATICALLY.py
# ============================================================================
import matplotlib.pyplot as plt
import numpy as np

# Define x range
x = np.linspace(0., 2.)

# Define functions
f = np.exp(x - 1) + (x - 1)**2             # Original nonlinear function
# g = x                                    # Linear approximation (tangent at x=1)
h = x + 1.5*(x-1)**2                       # Quadratic approximation

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(1, 1, 'or', label=r'Expansion Point ($x=1$)')
ax.plot(x, f, label=r'Original Function: $f(x) = e^{x-1} + (x-1)^2$')
ax.plot(x, h, 'r--', label=r'Quadratic Approximation: $h(x) = x + 1.5(x-1)^2$')
ax.set_title("Original Function vs Quadratic Approximation at $x=1$", fontsize=14)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)
ax.grid(True, alpha=0.3)
ax.legend(loc=(0.1,0.7), fontsize=14)
ax.set_ylim(0,4)
for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)
for spine in ["bottom","left"]:
    ax.spines[spine].set_position("zero")
plt.tight_layout()
plt.show()