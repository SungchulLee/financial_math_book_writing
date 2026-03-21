# Linear Approximation and First-Order Taylor Expansion

A central idea in calculus is that **smooth functions behave almost linearly when examined locally**. If we zoom in sufficiently near a point, the graph of a differentiable function becomes nearly indistinguishable from its tangent line.

If \(f\) is differentiable at a point \(x_0\), then the function admits a **first-order Taylor expansion** around \(x_0\):

\[
f(x) \approx f(x_0) + f'(x_0)(x-x_0)
\]

The right-hand side is the equation of the **tangent line** at \(x_0\). It matches both the value and the slope of the function at that point, which makes it the best linear approximation near \(x_0\).

Writing the increment \(\Delta x = x - x_0\) and the corresponding change in function value \(\Delta f = f(x) - f(x_0)\), we can express the approximation as

\[
\Delta f \approx f'(x_0)\,\Delta x
\]

This states that **small input changes produce approximately linear output changes**.

!!! info "Geometric interpretation"

    The first-order Taylor expansion replaces a curved function with its **tangent line** (or **tangent plane** in higher dimensions). The approximation works because smooth functions become nearly linear when viewed sufficiently close to a point.

---

## Example: A One-Dimensional Approximation

Consider

\[
f(x)=e^{x-1}+(x-1)^2
\]

expanded around \(x_0=1\).

We compute

\[
f(1)=1
\]

and

\[
f'(x)=e^{x-1}+2(x-1), \quad f'(1)=1
\]

The linear approximation is therefore

\[
f(x) \approx 1 + (x-1)
\]

The following Python code plots the original function together with its tangent line.

```python
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.exp(x-1) + (x-1)**2

def tangent(x):
    return 1 + (x-1)

x = np.linspace(-1,3,400)

fig, ax = plt.subplots(figsize=(6,4))
ax.plot(x, f(x), color='steelblue', label="f(x)")
ax.plot(x, tangent(x), color='orange', linestyle="--", label="tangent line")
ax.scatter([1],[1], color="red", zorder=5)
ax.legend()
ax.set_xlabel("x")
ax.set_ylabel("value")
ax.set_title("Linear approximation at x = 1")
plt.tight_layout()
plt.show()
```

![taylor_expansion_linear_1d](./image/taylor_expansion_linear_1d.png)

*Figure 1. Linear approximation of \(f(x)=e^{x-1}+(x-1)^2\) at \(x=1\). The blue curve shows the original function and the dashed orange line is the tangent line \(1 + (x-1)\). The red dot marks the expansion point.*

The plot shows that near \(x=1\), the tangent line and the function are almost indistinguishable. As we move farther from the expansion point, the curvature of the function becomes more visible and the approximation deteriorates.

This illustrates an important point: **linear approximations are local**.

The difference between the function and its linear approximation is typically proportional to \((x - x_0)^2\). This means the error shrinks **much faster** than the distance to the expansion point, making the linear approximation extremely accurate locally. This quadratic error scaling will become important when we consider second-order Taylor expansions.

---

## Extending the Idea to Two Variables

The same idea applies to functions of several variables.

Suppose a function depends on two inputs

\[
f(t,b)
\]

where

* \(t\) represents **time**
* \(b\) represents the **value of a Brownian motion**

Functions of the form \(f(t,B_t)\) will appear frequently in stochastic calculus, so we adopt this notation from the start.

The partial derivatives \(f_t = \partial f/\partial t\) and \(f_b = \partial f/\partial b\) describe how \(f\) changes with each input independently. If \(f\) is differentiable, the first-order Taylor expansion around \((t_0,b_0)\) is

\[
f(t,b) \approx f(t_0,b_0)
+ f_t(t_0,b_0)(t-t_0)
+ f_b(t_0,b_0)(b-b_0)
\]

Geometrically, this corresponds to the **tangent plane** to the surface \(f(t,b)\).

---

## Example: A Two-Dimensional Approximation

Consider

\[
f(t,b)=e^{t-1}+(t-1)^2+(b-2)^2
\]

Note that both the $t$- and $b$-directions have curvature, so the tangent plane will not be exact in either direction away from $(1,2)$.

We expand around

\[
(t_0,b_0)=(1,2)
\]

First compute

\[
f(1,2)=1
\]

Next compute partial derivatives

\[
f_t(t,b)=e^{t-1}+2(t-1), \qquad f_t(1,2)=1
\]

\[
f_b(t,b)=2(b-2), \qquad f_b(1,2)=0
\]

The partial derivative $f_b(1,2)=0$ because $(b-2)^2$ has a minimum at $b=2$, so the surface is momentarily flat in the $b$-direction at the expansion point.

The linear approximation becomes

\[
f(t,b) \approx 1 + (t-1) + 0 \cdot (b-2) = 1 + (t-1)
\]

Because $f_b(1,2)=0$, the tangent plane has no tilt in the $b$-direction — it is flat along that axis, resembling a cylinder rather than a general tilted plane.

---

## Visualizing the Tangent Plane

The following Python code visualizes the surface and its tangent plane.

```python
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

def f(t,b):
    return np.exp(t-1) + (t-1)**2 + (b-2)**2

def tangent_plane(t,b):
    return 1 + (t-1)

t = np.linspace(-1,3,50)
b = np.linspace(0,4,50)

T,B = np.meshgrid(t,b)

Z = f(T,B)
Z_lin = tangent_plane(T,B)

fig = plt.figure(figsize=(7,5))
ax = fig.add_subplot(111, projection='3d')

ax.plot_surface(T,B,Z,alpha=0.7,color='steelblue')
ax.plot_surface(T,B,Z_lin,alpha=0.4,color='orange')

ax.scatter([1],[2],[1], color='red', s=80)

ax.set_xlabel("t")
ax.set_ylabel("b")
ax.set_zlabel("f(t,b)")

custom_lines = [
    Line2D([0],[0], color='red', marker='o', linestyle='None', label='Expansion point'),
    Line2D([0],[0], color='steelblue', lw=3, label='Original surface'),
    Line2D([0],[0], color='orange', lw=3, label='Tangent plane'),
]
ax.legend(handles=custom_lines, loc=(0.0, 0.8))

plt.title("Surface and tangent plane at (1,2)")
plt.tight_layout()
plt.show()
```

![taylor_expansion_linear_2d](./image/taylor_expansion_linear_2d.png)

*Figure 2. Tangent-plane approximation of the surface \(f(t,b)=e^{t-1}+(t-1)^2+(b-2)^2\) at the point \((1,2)\). The blue surface represents the original function and the orange plane is the linear Taylor approximation. The red dot marks the expansion point. Because $f_b(1,2)=0$, the tangent plane is flat in the $b$-direction; both directions nonetheless have curvature, so the surface diverges from the plane as we move away from $(1,2)$.*

The figure shows the surface \(f(t,b)\) together with its tangent plane. Near the expansion point \((1,2)\), the two surfaces coincide closely. As we move away, curvature causes the true surface to diverge from the linear approximation.

---

## Looking Ahead

Linear approximations capture the dominant behavior of small deterministic changes. Higher-order terms usually become negligible as increments shrink — and for smooth, deterministic paths this is guaranteed, since $(\Delta x)^2 = O((\Delta t)^2)$ vanishes faster than $\Delta t$.

Brownian motion breaks this guarantee. Its increments scale like \(\Delta B_t \sim \sqrt{\Delta t}\), so their squares satisfy

\[
(\Delta B_t)^2 \sim \Delta t
\]

This means the quadratic term in the Taylor expansion does **not** vanish — it contributes at the same order as the linear terms. The next section makes this precise by examining exactly how large second-order corrections become, and why ignoring them leads to wrong answers.

That analysis leads to **Itô's lemma**, which can be viewed as a Taylor expansion that keeps the quadratic term. The scaling $(\Delta B_t)^2 \sim \Delta t$ is made precise in [From Taylor to Itô](from_taylor_to_ito.md) and [Quadratic Variation of Brownian Motion](../../ch02/brownian_motion/quadratic_variation_of_brownian_motion.md), and is the key fact that makes this correction necessary.
