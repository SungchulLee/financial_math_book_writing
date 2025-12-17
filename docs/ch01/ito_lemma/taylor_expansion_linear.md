# Taylor Expansion I: Linear Approximation

This section reviews the **first-order Taylor expansion**, i.e., *linear approximation*. The goal is to build the mindset that “differentials” capture how a function changes under small perturbations—an idea we will later reuse in stochastic calculus.

---

## 1. Linear Approximation in One Variable

For a differentiable function \(f(x)\), the first-order approximation is

\[
df = f_x \, dx.
\]

Equivalently, around a point \(x_0\),

\[
f(x) \approx f(x_0) + f_x(x_0)\,(x-x_0).
\]

---

## 2. Python Example: Linear Approximation in 1D

### Problem

Approximate \(f(1.1)\) using the linear approximation of \(f\) at \(x_0=1\), where

\[
f(x)=e^{x-1}+(x-1)^2.
\]

### Solution (by differentials)

\[
\begin{array}{ccccccc}
df&=&f_x&*&dx\\
\uparrow&&\uparrow&&\uparrow\\
f(x)-f(x_0)&&f_x(x_0)&&x-x_0\\
f(1.1)-f(1)&&f_x(1)&&1.1-1\\
\end{array}
\]

We compute \(f(1)=1\), and

\[
f_x(x)=e^{x-1}+2(x-1)\quad\Rightarrow\quad f_x(1)=1.
\]

Therefore,

\[
f(1.1)-1=1\cdot(1.1-1)
\quad\Rightarrow\quad
f(1.1)\approx 1.1.
\]

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0., 2.)

f = np.exp(x - 1) + (x - 1)**2   # original function
g = x                             # linear approximation at x=1

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(1, 1, 'or', label='Taylor expansion point (x=1)')
ax.plot(x, f, label=r'Original: $f(x)=e^{x-1}+(x-1)^2$')
ax.plot(x, g, 'r--', label=r'Linear approx: $g(x)=x$')
ax.set_title(r"Original Function vs Linear Approximation at $x=1$", fontsize=14)
ax.set_xlabel("x", fontsize=14)
ax.set_ylabel("y", fontsize=14)
ax.grid(True, alpha=0.3)
ax.legend(loc=(0.1,0.7), fontsize=12)
for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)
for spine in ["bottom","left"]:
    ax.spines[spine].set_position("zero")
plt.tight_layout()
plt.show()
```

---

## 3. Linear Approximation in Two Variables

For a differentiable function \(f(t,b)\),

\[
df = f_t\,dt + f_b\,db.
\]

Equivalently, around \((t_0,b_0)\),

\[
f(t,b) \approx f(t_0,b_0)+ f_t(t_0,b_0)(t-t_0) + f_b(t_0,b_0)(b-b_0).
\]

---

## 4. Python Example: Linear Approximation in 2D

### Problem

Approximate \(f(1.1,1.8)\) using the linear approximation at \((t_0,b_0)=(1,2)\), where

\[
f(t,b)=e^{t-1}+(t-1)^2+(b-2)^2.
\]

### Solution (by differentials)

\[
\begin{array}{ccccccc}
df&=&f_t&*&dt&+&f_b&*&db\\
\uparrow&&\uparrow&&\uparrow&&\uparrow&&\uparrow\\
f(t,b)-f(t_0,b_0)&&f_t(t_0,b_0)&&t-t_0&&f_b(t_0,b_0)&&b-b_0\\
f(1.1,1.8)-f(1,2)&&f_t(1,2)&&1.1-1&&f_b(1,2)&&1.8-2\\
\end{array}
\]

We compute \(f(1,2)=1\). Also,

\[
f_t(t,b)=e^{t-1}+2(t-1)\Rightarrow f_t(1,2)=1,\qquad
f_b(t,b)=2(b-2)\Rightarrow f_b(1,2)=0.
\]

Therefore,

\[
f(1.1,1.8)-1=1\cdot(0.1)+0\cdot(-0.2)
\quad\Rightarrow\quad
f(1.1,1.8)\approx 1.1.
\]

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

t = np.linspace(0., 2.)
b = np.linspace(1., 3.)
T, B = np.meshgrid(t, b)

F = np.exp(T - 1) + (T - 1)**2 + (B - 2)**2  # original function
G = T                                        # linear approximation at (1,2)

fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': '3d'})
ax.plot_surface(T, B, F, rstride=2, cstride=2, linewidth=0.5, alpha=0.6)
ax.plot_surface(T, B, G, rstride=2, cstride=2, linewidth=0.5, alpha=0.4)

i = np.abs(b - 2).argmin()
j = np.abs(t - 1).argmin()
z = F[i, j]
ax.scatter(t[j], b[i], z, color='red', s=80)

ax.set_title(r"Original Function vs Linear Approximation at $(t,b)=(1,2)$", fontsize=14)
ax.set_xlabel('t', fontsize=12)
ax.set_ylabel('b', fontsize=12)
ax.set_zlabel('f(t,b)', fontsize=12)

custom_lines = [
    Line2D([0], [0], color='red', marker='o', linestyle='None', label='Expansion point'),
    Line2D([0], [0], color='black', lw=3, label='Original surface'),
    Line2D([0], [0], color='gray', lw=3, label='Linear approximation'),
]
ax.legend(handles=custom_lines, loc=(0.0, 0.8), fontsize=11)
ax.view_init(elev=30, azim=-70)
plt.tight_layout()
plt.show()
```
