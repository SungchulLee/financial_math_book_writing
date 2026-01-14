# Taylor Expansion II: Quadratic Approximation


Linear approximation captures the first-order change in a function. For many applications (including Itô calculus), we must keep **second-order terms**.

---

## Quadratic Approximation in One Variable


For a twice differentiable function \(f(x)\),

\[
df = f_x\,dx + \frac{1}{2} f_{xx} (dx)^2.
\]

Equivalently, around \(x_0\),

\[
f(x)\approx f(x_0)+f_x(x_0)(x-x_0)+\frac12 f_{xx}(x_0)(x-x_0)^2.
\]

---

## Python Example: Quadratic Approximation in 1D


### 1. Problem


Approximate \(f(1.1)\) using the quadratic approximation at \(x_0=1\), where

\[
f(x)=e^{x-1}+(x-1)^2.
\]

### 2. Solution (by differentials)


\[
\begin{array}{ccccccccccccccc}
df&=&f_x&*&dx&+&\frac12&*&f_{xx}&*&(dx)^2\\
\uparrow&&\uparrow&&\uparrow&&&&\uparrow&&\uparrow\\
f(x)-f(x_0)&&f_x(x_0)&&x-x_0&&&&f_{xx}(x_0)&&(x-x_0)^2\\
f(1.1)-f(1)&&f_x(1)&&1.1-1&&&&f_{xx}(1)&&(1.1-1)^2\\
\end{array}
\]

We have \(f(1)=1\), \(f_x(1)=1\), and

\[
f_{xx}(x)=e^{x-1}+2\Rightarrow f_{xx}(1)=3.
\]

Therefore,

\[
f(1.1)-1 = 1\cdot 0.1 + \frac12\cdot 3\cdot (0.1)^2
\quad\Rightarrow\quad
f(1.1)\approx 1.115.
\]

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0., 2.)
f = np.exp(x - 1) + (x - 1)**2
h = x + 1.5*(x-1)**2  # quadratic approximation at x=1

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(1, 1, 'or', label=r'Expansion point ($x=1$)')
ax.plot(x, f, label=r'Original: $f(x)=e^{x-1}+(x-1)^2$')
ax.plot(x, h, 'r--', label=r'Quadratic approx: $h(x)=x+1.5(x-1)^2$')
ax.set_title(r"Original Function vs Quadratic Approximation at $x=1$", fontsize=14)
ax.set_xlabel("x", fontsize=12)
ax.set_ylabel("y", fontsize=12)
ax.grid(True, alpha=0.3)
ax.legend(loc=(0.1,0.7), fontsize=11)
ax.set_ylim(0,4)
for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)
for spine in ["bottom","left"]:
    ax.spines[spine].set_position("zero")
plt.tight_layout()
plt.show()
```

---

## Quadratic Approximation in Two Variables


For a twice differentiable function \(f(t,b)\), the second-order expansion is

\[
df
= f_t\,dt + f_b\,db
+ \frac12 f_{tt}(dt)^2 + \frac12 f_{bb}(db)^2 + f_{tb}(dt)(db).
\]

---

## Python Example: Quadratic Approximation in 2D


### 1. Problem


Approximate \(f(1.1,1.8)\) using the quadratic approximation at \((t_0,b_0)=(1,2)\), where

\[
f(t,b)=e^{t-1}+(t-1)^2+(b-2)^2.
\]

### 2. Solution (by expansion)


First-order terms:

\[
f(1.1,1.8)\approx f(1,2)+ f_t(1,2)\cdot 0.1 + f_b(1,2)\cdot(-0.2).
\]

Second-order terms:

\[
+\frac12 f_{tt}(1,2)\cdot (0.1)^2
+\frac12 f_{bb}(1,2)\cdot (-0.2)^2
+ f_{tb}(1,2)\cdot (0.1)(-0.2).
\]

We compute:
- \(f(1,2)=1\)
- \(f_t(1,2)=1\), \(f_b(1,2)=0\)
- \(f_{tt}(t,b)=e^{t-1}+2 \Rightarrow f_{tt}(1,2)=3\)
- \(f_{bb}(t,b)=2\)
- \(f_{tb}(t,b)=0\)

Therefore,

\[
\begin{aligned}
f(1.1,1.8)
&\approx 1 + 1\cdot 0.1 + 0\cdot(-0.2)
+ \frac12\cdot 3\cdot (0.1)^2
+ \frac12\cdot 2\cdot (0.2)^2 \\
&= 1 + 0.1 + 0.015 + 0.04
= 1.155.
\end{aligned}
\]

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

t = np.linspace(0., 2.)
b = np.linspace(1., 3.)
T, B = np.meshgrid(t, b)

F = np.exp(T - 1) + (T - 1)**2 + (B - 2)**2
H = T + 1.5*(T-1)**2 + (B-2)**2  # quadratic approximation surface

fig, ax = plt.subplots(figsize=(10, 6), subplot_kw={'projection': '3d'})
ax.plot_surface(T, B, F, rstride=2, cstride=2, linewidth=0.5, alpha=0.6)
ax.plot_surface(T, B, H, rstride=2, cstride=2, linewidth=0.5, alpha=0.4)

i = np.abs(b - 2).argmin()
j = np.abs(t - 1).argmin()
z = F[i, j]
ax.scatter(t[j], b[i], z, color='red', s=80)

ax.set_title(r"Original Function vs Quadratic Approximation at $(t,b)=(1,2)$", fontsize=14)
ax.set_xlabel('t', fontsize=12)
ax.set_ylabel('b', fontsize=12)
ax.set_zlabel('f(t,b)', fontsize=12)

custom_lines = [
    Line2D([0], [0], color='red', marker='o', linestyle='None', label='Expansion point'),
    Line2D([0], [0], color='black', lw=3, label='Original surface'),
    Line2D([0], [0], color='gray', lw=3, label='Quadratic approximation'),
]
ax.legend(handles=custom_lines, loc=(0.0, 0.8), fontsize=11)
ax.view_init(elev=30, azim=-70)
plt.tight_layout()
plt.show()
```
