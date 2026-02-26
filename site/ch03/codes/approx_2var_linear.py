# ============================================================================
# APPROXIMATE_TWO_VARIABLE_FUNCTION_LINEARLY.py
# ============================================================================
import matplotlib.pyplot as plt
import numpy as np

# Define domain
t = np.linspace(0., 2.)
b = np.linspace(1., 3.)
T, B = np.meshgrid(t, b)

# Define functions
F = np.exp(T - 1) + (T - 1)**2 + (B - 2)**2                # Original function
G = T                                                      # Linear approximation

fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': '3d'})
surf1 = ax.plot_surface(T, B, F, rstride=2, cstride=2, cmap='coolwarm',
                        linewidth=0.5, antialiased=True, alpha=0.6)
surf2 = ax.plot_surface(T, B, G, rstride=2, cstride=2, cmap='Greys',
                        linewidth=0.5, antialiased=True, alpha=0.4)

# Plot marker
# Find closest grid point to t=1, b=2
i = np.abs(b - 2).argmin()  # row index (b-axis)
j = np.abs(t - 1).argmin()  # column index (t-axis)
z = F[i, j] # Compute z-value at (t=1, b=2)
ax.scatter(t[j], b[i], z, color='red', s=100) # Plot marker

ax.set_title(r"Original Function vs Linear Approximation at $x=1$, $b=2$", fontsize=14)
ax.set_xlabel('Time $t$', fontsize=14)
ax.set_ylabel('State $b$', fontsize=14)
ax.set_zlabel('$f(t,b)$', fontsize=14)

# 3D plots don't support legend natively with plot_surface, so we mimic it
from matplotlib.lines import Line2D
custom_lines = [
    Line2D([0], [0], color='red', marker='o', linestyle='None', label='Tylor  Expansion Point (x=1, b=2)'),
    Line2D([0], [0], color='firebrick', lw=3, label=r'Original Function: $f(t, b) = e^{t-1} + (t-1)^2 + (b-2)^2$'),
    Line2D([0], [0], color='gray', lw=3, label=r'Linear Approximation: $g(t) = t$'), 
]
ax.legend(handles=custom_lines, loc=(0.0, 0.8), fontsize=14)

ax.view_init(elev=30, azim=-70)
plt.tight_layout()
plt.show()