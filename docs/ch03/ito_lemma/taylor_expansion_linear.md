# Linear Approximation and First-Order Taylor Expansion

A central idea in calculus is that **smooth functions behave almost linearly when examined locally**. If we zoom in sufficiently near a point, the graph of a differentiable function becomes nearly indistinguishable from its tangent line.

If $f$ is differentiable at a point $x_0$, then the function admits a **first-order Taylor expansion** around $x_0$:

$$
f(x) \approx f(x_0) + f'(x_0)(x-x_0)
$$

The right-hand side is the equation of the **tangent line** at $x_0$. It matches both the value and the slope of the function at that point, which makes it the best linear approximation near $x_0$.

Writing the increment $\Delta x = x - x_0$ and the corresponding change in function value $\Delta f = f(x) - f(x_0)$, we can express the approximation as

$$
\Delta f \approx f'(x_0)\,\Delta x
$$

This states that **small input changes produce approximately linear output changes**.

!!! info "Geometric interpretation"

    The first-order Taylor expansion replaces a curved function with its **tangent line** (or **tangent plane** in higher dimensions). The approximation works because smooth functions become nearly linear when viewed sufficiently close to a point.

---

## Example: A One-Dimensional Approximation

Consider

$$
f(x)=e^{x-1}+(x-1)^2
$$

expanded around $x_0=1$.

We compute

$$
f(1)=1
$$

and

$$
f'(x)=e^{x-1}+2(x-1), \quad f'(1)=1
$$

The linear approximation is therefore

$$
f(x) \approx 1 + (x-1)
$$

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

*Figure 1. Linear approximation of $f(x)=e^{x-1}+(x-1)^2$ at $x=1$. The blue curve shows the original function and the dashed orange line is the tangent line $1 + (x-1)$. The red dot marks the expansion point.*

The plot shows that near $x=1$, the tangent line and the function are almost indistinguishable. As we move farther from the expansion point, the curvature of the function becomes more visible and the approximation deteriorates.

This illustrates an important point: **linear approximations are local**.

The difference between the function and its linear approximation is typically proportional to $(x - x_0)^2$. This means the error shrinks **much faster** than the distance to the expansion point, making the linear approximation extremely accurate locally. This quadratic error scaling will become important when we consider second-order Taylor expansions.

---

## Extending the Idea to Two Variables

The same idea applies to functions of several variables.

Suppose a function depends on two inputs

$$
f(t,b)
$$

where

* $t$ represents **time**
* $b$ represents the **value of a Brownian motion**

Functions of the form $f(t,B_t)$ will appear frequently in stochastic calculus, so we adopt this notation from the start.

The partial derivatives $f_t = \partial f/\partial t$ and $f_b = \partial f/\partial b$ describe how $f$ changes with each input independently. If $f$ is differentiable, the first-order Taylor expansion around $(t_0,b_0)$ is

$$
f(t,b) \approx f(t_0,b_0)
+ f_t(t_0,b_0)(t-t_0)
+ f_b(t_0,b_0)(b-b_0)
$$

Geometrically, this corresponds to the **tangent plane** to the surface $f(t,b)$.

---

## Example: A Two-Dimensional Approximation

Consider

$$
f(t,b)=e^{t-1}+(t-1)^2+(b-2)^2
$$

Note that both the $t$- and $b$-directions have curvature, so the tangent plane will not be exact in either direction away from $(1,2)$.

We expand around

$$
(t_0,b_0)=(1,2)
$$

First compute

$$
f(1,2)=1
$$

Next compute partial derivatives

$$
f_t(t,b)=e^{t-1}+2(t-1), \qquad f_t(1,2)=1
$$

$$
f_b(t,b)=2(b-2), \qquad f_b(1,2)=0
$$

The partial derivative $f_b(1,2)=0$ because $(b-2)^2$ has a minimum at $b=2$, so the surface is momentarily flat in the $b$-direction at the expansion point.

The linear approximation becomes

$$
f(t,b) \approx 1 + (t-1) + 0 \cdot (b-2) = 1 + (t-1)
$$

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

*Figure 2. Tangent-plane approximation of the surface $f(t,b)=e^{t-1}+(t-1)^2+(b-2)^2$ at the point $(1,2)$. The blue surface represents the original function and the orange plane is the linear Taylor approximation. The red dot marks the expansion point. Because $f_b(1,2)=0$, the tangent plane is flat in the $b$-direction; both directions nonetheless have curvature, so the surface diverges from the plane as we move away from $(1,2)$.*

The figure shows the surface $f(t,b)$ together with its tangent plane. Near the expansion point $(1,2)$, the two surfaces coincide closely. As we move away, curvature causes the true surface to diverge from the linear approximation.

---

## Looking Ahead

Linear approximations capture the dominant behavior of small deterministic changes. Higher-order terms usually become negligible as increments shrink — and for smooth, deterministic paths this is guaranteed, since $(\Delta x)^2 = O((\Delta t)^2)$ vanishes faster than $\Delta t$.

Brownian motion breaks this guarantee. Its increments scale like $\Delta B_t \sim \sqrt{\Delta t}$, so their squares satisfy

$$
(\Delta B_t)^2 \sim \Delta t
$$

This means the quadratic term in the Taylor expansion does **not** vanish — it contributes at the same order as the linear terms. The next section makes this precise by examining exactly how large second-order corrections become, and why ignoring them leads to wrong answers.

That analysis leads to **Itô's lemma**, which can be viewed as a Taylor expansion that keeps the quadratic term. The scaling $(\Delta B_t)^2 \sim \Delta t$ is made precise in [From Taylor to Itô](from_taylor_to_ito.md) and [Quadratic Variation of Brownian Motion](../../ch02/brownian_motion/quadratic_variation_of_brownian_motion.md), and is the key fact that makes this correction necessary.

---

## Exercises

**Exercise 1.** Let $f(x) = \sin(x)$. Write the first-order Taylor approximation of $f$ around $x_0 = 0$. Use it to approximate $f(0.1)$ and compare with the exact value.

??? success "Solution to Exercise 1"
    The first-order Taylor approximation of $f(x) = \sin(x)$ around $x_0 = 0$ is

    $$
    f(x) \approx f(0) + f'(0)(x - 0) = 0 + 1 \cdot x = x
    $$

    since $\sin(0) = 0$ and $\cos(0) = 1$. Using this to approximate $f(0.1)$:

    $$
    \sin(0.1) \approx 0.1
    $$

    The exact value is $\sin(0.1) = 0.09983\ldots$, so the approximation error is approximately $0.00017$. This error is proportional to $(\Delta x)^2 = 0.01$, consistent with the general theory that first-order Taylor errors scale quadratically.

---

**Exercise 2.** For the function $f(t, b) = t^2 + tb + b^3$, compute the first-order Taylor expansion around $(t_0, b_0) = (1, 1)$. Identify the tangent plane equation explicitly.

??? success "Solution to Exercise 2"
    We compute $f(1,1) = 1 + 1 + 1 = 3$. The partial derivatives are

    $$
    f_t(t, b) = 2t + b, \qquad f_b(t, b) = t + 3b^2
    $$

    Evaluating at $(1, 1)$: $f_t(1,1) = 3$ and $f_b(1,1) = 4$. The first-order Taylor expansion is

    $$
    f(t, b) \approx 3 + 3(t - 1) + 4(b - 1)
    $$

    The tangent plane equation is $z = 3 + 3(t - 1) + 4(b - 1)$, or equivalently $z = 3t + 4b - 4$.

---

**Exercise 3.** A deterministic path satisfies $\Delta x = O(\Delta t)$, so $(\Delta x)^2 = O((\Delta t)^2)$. Explain why this means the quadratic term in the Taylor expansion is negligible for smooth deterministic functions. Then explain why the same argument fails for Brownian motion, where $\Delta B_t \sim \sqrt{\Delta t}$.

??? success "Solution to Exercise 3"
    For a deterministic path, the increment satisfies $\Delta x = O(\Delta t)$. Squaring gives $(\Delta x)^2 = O((\Delta t)^2)$. In the Taylor expansion, the first-order term $f'(x_0)\Delta x$ is $O(\Delta t)$, while the second-order term $\frac{1}{2}f''(x_0)(\Delta x)^2$ is $O((\Delta t)^2)$. As $\Delta t \to 0$, the quadratic term vanishes much faster than the linear term, so it can be safely dropped.

    For Brownian motion, $\Delta B_t \sim \sqrt{\Delta t}$, so $(\Delta B_t)^2 \sim \Delta t$. The quadratic term $\frac{1}{2}f''(\Delta B_t)^2$ is therefore $O(\Delta t)$ — the **same order** as the linear term $f'(\Delta t)$. Since it does not vanish relative to the first-order terms, it cannot be neglected.

---

**Exercise 4.** Consider $f(x) = \log(x)$ expanded around $x_0 = 1$.

(a) Write the first-order Taylor approximation.

(b) Use it to approximate $\log(1.05)$.

(c) Compute the exact value and the absolute error. How does the error scale with $\Delta x = 0.05$?

??? success "Solution to Exercise 4"
    **(a)** We have $f(x) = \log(x)$, $f'(x) = 1/x$, and $f(1) = 0$, $f'(1) = 1$. The first-order Taylor approximation around $x_0 = 1$ is

    $$
    f(x) \approx 0 + 1 \cdot (x - 1) = x - 1
    $$

    **(b)** Approximating $\log(1.05)$:

    $$
    \log(1.05) \approx 1.05 - 1 = 0.05
    $$

    **(c)** The exact value is $\log(1.05) = 0.04879\ldots$. The absolute error is $|0.05 - 0.04879| \approx 0.00121$. Since $f''(x) = -1/x^2$ and the error of a first-order approximation is approximately $\frac{1}{2}|f''(x_0)|(\Delta x)^2 = \frac{1}{2}(1)(0.05)^2 = 0.00125$, the error scales as $(\Delta x)^2$, which matches the observed value.

---

**Exercise 5.** Let $f(t, b) = e^{-t}\cos(b)$. Compute the partial derivatives $f_t(0, 0)$ and $f_b(0, 0)$, and write the first-order Taylor expansion around $(0, 0)$. What is the geometric interpretation of the result?

??? success "Solution to Exercise 5"
    The partial derivatives of $f(t, b) = e^{-t}\cos(b)$ are

    $$
    f_t(t, b) = -e^{-t}\cos(b), \qquad f_b(t, b) = -e^{-t}\sin(b)
    $$

    Evaluating at $(0, 0)$: $f(0, 0) = 1$, $f_t(0, 0) = -1$, and $f_b(0, 0) = 0$. The first-order Taylor expansion is

    $$
    f(t, b) \approx 1 - t + 0 \cdot b = 1 - t
    $$

    Geometrically, the tangent plane at $(0, 0)$ is flat in the $b$-direction (since $f_b(0,0) = 0$) and has slope $-1$ in the $t$-direction. The surface is momentarily at a maximum in $b$ at $b = 0$ (since $\cos(b)$ peaks there), while it decays exponentially in $t$.

---

**Exercise 6.** The error of a first-order Taylor approximation is proportional to $(\Delta x)^2$. Suppose you approximate $f(x) = e^x$ at $x_0 = 0$ with $\Delta x = 0.1$ and observe an error $\epsilon$. Predict (without computing the exact value) by what factor the error decreases if you reduce $\Delta x$ to $0.01$.

??? success "Solution to Exercise 6"
    The error of a first-order Taylor approximation scales as $C(\Delta x)^2$ for some constant $C$ depending on $f''$. If the error at $\Delta x = 0.1$ is $\epsilon$, then $\epsilon \approx C(0.1)^2 = 0.01C$. At $\Delta x = 0.01$, the error is approximately $C(0.01)^2 = 0.0001C$. The ratio of errors is

    $$
    \frac{0.0001C}{0.01C} = \frac{1}{100}
    $$

    The error decreases by a factor of $100$. Equivalently, reducing $\Delta x$ by a factor of $10$ reduces the error by a factor of $10^2 = 100$.

---

**Exercise 7.** A Brownian motion path is simulated with $N = 1000$ steps over $[0, 1]$, so $\Delta t = 0.001$. For each increment $\Delta B_i$, we have $\mathbb{E}[(\Delta B_i)^2] = \Delta t$.

(a) What is the expected value of $\sum_{i=0}^{N-1} (\Delta B_i)^2$?

(b) Why does this sum converge to $t = 1$ as $N \to \infty$, while $\sum_{i=0}^{N-1} (\Delta t)^2 \to 0$?

(c) Explain in one sentence why this difference is the reason linear Taylor approximations are insufficient for functions of Brownian motion.

??? success "Solution to Exercise 7"
    **(a)** Since $\mathbb{E}[(\Delta B_i)^2] = \Delta t = 0.001$ for each increment, and the increments are independent:

    $$
    \mathbb{E}\!\left[\sum_{i=0}^{N-1}(\Delta B_i)^2\right] = \sum_{i=0}^{N-1}\mathbb{E}[(\Delta B_i)^2] = N \cdot \Delta t = 1000 \cdot 0.001 = 1
    $$

    **(b)** The sum $\sum_{i=0}^{N-1}(\Delta B_i)^2$ converges to $[B,B]_1 = 1$ by the quadratic variation property of Brownian motion. Each $(\Delta B_i)^2$ is of order $\Delta t$, and there are $N = 1/\Delta t$ such terms, so the total is of order $1$. In contrast, $\sum_{i=0}^{N-1}(\Delta t)^2 = N(\Delta t)^2 = \Delta t \to 0$ because each term is $(\Delta t)^2$ (one order smaller), so the sum vanishes.

    **(c)** Because $\sum(\Delta B_i)^2$ converges to a non-zero limit (rather than to zero), the quadratic term $\frac{1}{2}f''(\Delta B)^2$ in the Taylor expansion accumulates a finite contribution, making it impossible to ignore — and thus the linear Taylor approximation is insufficient.
