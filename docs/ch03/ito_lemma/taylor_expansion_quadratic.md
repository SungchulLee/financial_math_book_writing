# Taylor Expansion II: Quadratic Approximation

The previous section showed that linear approximations capture local slope. However, many functions bend, and the tangent line cannot capture this curvature.

Quadratic approximation extends this idea by incorporating curvature through **second-order terms**.

Geometrically:

* **Linear approximation** gives a **tangent line** (or tangent plane).
* **Quadratic approximation** gives the **best local quadratic approximation** (or curved surface).

Including the quadratic term allows the approximation to follow the curvature of the function more closely near the expansion point.

---

### Quadratic Approximation in One Variable

Extending the linear approximation from the previous section, we include a second-order term. If $f$ is twice differentiable near $x_0$, we can write the **second-order Taylor approximation** as

$$
f(x) \approx
f(x_0)

+ f'(x_0)(x-x_0)
+ \frac12 f''(x_0)(x-x_0)^2
$$

Using increment notation,

$$
\Delta f
\approx
f'(x_0)\Delta x
+
\frac12 f''(x_0)(\Delta x)^2
$$

where

$$
\Delta x = x-x_0
$$

The second term captures the **curvature of the function near the expansion point**.

---

### Python Example: Quadratic Approximation in 1D

#### 1. Problem

Approximate $f(1.1)$ using the quadratic approximation at $x_0=1$, where

$$
f(x)=e^{x-1}+(x-1)^2
$$

This example is useful because the exponential term introduces curvature while the polynomial keeps the derivatives simple.

#### 2. Solution

First compute derivatives.

$$
f'(x)=e^{x-1}+2(x-1)
$$

$$
f''(x)=e^{x-1}+2
$$

Evaluate them at $x_0=1$:

$$
f(1)=1,\qquad f'(1)=1,\qquad f''(1)=3
$$

Let $\Delta x = 1.1-1 = 0.1$. The quadratic approximation gives

$$
f(1.1)
\approx
1 + 1(0.1) + \frac12 \cdot 3 (0.1)^2
= 1.115
$$

The true value is $f(1.1)=e^{0.1}+0.01\approx1.11517$. Compared with the linear approximation (which gives $1.1$), the quadratic approximation reduces the error from $\approx 0.015$ to $\approx 0.00017$ — a reduction of roughly two orders of magnitude — illustrating how the second-order term captures **local curvature**.

---

### Python Visualization

```python
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0., 2.)

# original function
f = np.exp(x - 1) + (x - 1)**2

# quadratic approximation at x=1: f(1) + f'(1)(x-1) + 0.5*f''(1)*(x-1)^2
# f(1)=1, f'(1)=1, f''(1)=3, so 0.5*f''(1)=1.5
h = 1 + (x-1) + 1.5*(x-1)**2

fig, ax = plt.subplots(figsize=(12,6))

ax.plot(1, 1, 'or', label=r'Expansion point ($x=1$)')
ax.plot(x, f, color='steelblue', label=r'Original: $f(x)=e^{x-1}+(x-1)^2$')
ax.plot(x, h, color='orange', linestyle='--', label=r'Quadratic approximation')

ax.set_title("Original Function vs Quadratic Approximation at x=1")
ax.set_xlabel("x")
ax.set_ylabel("y")

ax.grid(True, alpha=0.3)
ax.legend(loc=(0.1, 0.7))
ax.set_ylim(0, 4)

for spine in ["top","right"]:
    ax.spines[spine].set_visible(False)

for spine in ["bottom","left"]:
    ax.spines[spine].set_position("zero")

plt.tight_layout()
plt.show()
```

![taylor_expansion_quadratic_1d](./image/taylor_expansion_quadratic_1d.png)

*Figure 1. Quadratic approximation of $f(x)=e^{x-1}+(x-1)^2$ at $x=1$. The blue curve shows the original function, the dashed orange curve is the quadratic Taylor approximation, and the red dot marks the expansion point.*

Near the expansion point the two curves are almost identical. The quadratic curve follows the original function much more closely than the tangent line, illustrating how second-order terms capture **local curvature**.

---

### Quadratic Approximation in Two Variables

For a twice differentiable function $f(t,b)$, the second-order Taylor expansion includes both **pure second derivatives** and **cross derivatives**.

$$
\Delta f
\approx
f_t\Delta t
+
f_b\Delta b
+
\frac12 f_{tt}(\Delta t)^2
+
\frac12 f_{bb}(\Delta b)^2
+
f_{tb}\Delta t\Delta b
$$

This expansion describes how the surface bends in different directions.

In compact matrix form:

$$
f(x) \approx
f(x_0)
+
\nabla f(x_0)^T(x-x_0)
+
\frac12 (x-x_0)^T H (x-x_0)
$$

where $H$ is the **Hessian matrix**, the matrix of all second-order partial derivatives of $f$. It describes how the function bends in different directions.

---

### Python Example: Quadratic Approximation in 2D

#### 1. Problem

Approximate $f(1.1,1.8)$ using the quadratic approximation at

$$
(t_0,b_0)=(1,2)
$$

where

$$
f(t,b)=e^{t-1}+(t-1)^2+(b-2)^2
$$

#### 2. Solution

First compute partial derivatives:

$$
f_t=e^{t-1}+2(t-1),\qquad f_b=2(b-2)
$$

Second derivatives:

$$
f_{tt}=e^{t-1}+2,\qquad f_{bb}=2,\qquad f_{tb}=0
$$

Since $t$ and $b$ enter the function separately (no cross term), the cross-partial $f_{tb}=0$, and the cross term in the expansion vanishes.

Evaluate at $(1,2)$:

$$
f(1,2)=1,\qquad f_t(1,2)=1,\qquad f_b(1,2)=0,\qquad f_{tt}(1,2)=3,\qquad f_{bb}(1,2)=2
$$

Let $\Delta t=0.1$ and $\Delta b=1.8-2=-0.2$. Substituting all four terms into the expansion explicitly:

$$
f(1.1,1.8)
\approx
\underbrace{1}_{f}
+\underbrace{1(0.1)}_{f_t\Delta t}
+\underbrace{0(-0.2)}_{f_b\Delta b}
+\underbrace{\frac12(3)(0.1)^2}_{0.015}
+\underbrace{\frac12(2)(0.2)^2}_{0.04}
= 1.155
$$

Note that $|\Delta b| = 0.2$ so $\frac12 f_{bb}(\Delta b)^2 = \frac12(2)(0.04) = 0.04$, not $0.2$.

---

### Python Visualization

```python
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

t = np.linspace(0.,2.)
b = np.linspace(1.,3.)

T,B = np.meshgrid(t,b)

# original function
F = np.exp(T-1)+(T-1)**2+(B-2)**2

# quadratic approximation: f(1,2) + f_t*(T-1) + 0.5*f_tt*(T-1)^2 + 0.5*f_bb*(B-2)^2
H = 1 + (T-1) + 1.5*(T-1)**2 + (B-2)**2

fig,ax = plt.subplots(figsize=(10,6),subplot_kw={'projection':'3d'})

ax.plot_surface(T,B,F,alpha=0.7,color="b")
ax.plot_surface(T,B,H,alpha=0.4,color="orange")

# expansion point
i = np.abs(b-2).argmin()
j = np.abs(t-1).argmin()
z = F[i,j]

ax.scatter(t[j],b[i],z,color='red',s=80)

ax.set_title("Original Function vs Quadratic Approximation")
ax.set_xlabel("t")
ax.set_ylabel("b")
ax.set_zlabel("f(t,b)")

custom_lines=[
Line2D([0],[0],color='red',marker='o',linestyle='None',label='Expansion point'),
Line2D([0],[0],color='b',lw=3,label='Original surface'),
Line2D([0],[0],color='orange',lw=3,label='Quadratic approximation surface')
]

ax.legend(handles=custom_lines,loc=(0.0,0.8))
ax.view_init(elev=30,azim=-70)

plt.tight_layout()
plt.show()
```

![taylor_expansion_quadratic_2d](./image/taylor_expansion_quadratic_2d.png)

*Figure 2. Quadratic Taylor approximation of the surface $f(t,b)=e^{t-1}+(t-1)^2+(b-2)^2$ at $(1,2)$. The blue surface represents the original function and the orange surface represents the quadratic approximation. The red dot marks the expansion point.*

Near the expansion point the quadratic surface follows the original function very closely, capturing curvature that the tangent plane misses.

---

Quadratic Taylor expansions play a crucial role in many areas of mathematics. In stochastic calculus, second-order terms become essential because random fluctuations produce non-negligible quadratic effects — an idea that leads directly to **Itô's lemma**.

!!! abstract "The central fact"

    Classical calculus ignores second-order terms because they vanish.
    Stochastic calculus keeps them because they don't.

#### Deterministic vs Brownian Scaling

In deterministic calculus, $(dt)^2 \ll dt$, so the quadratic term in a Taylor expansion is negligible. Brownian motion is fundamentally different.

Recall (see [Quadratic Variation of Brownian Motion](../../ch02/brownian_motion/quadratic_variation_of_brownian_motion.md) for the underlying convergence and [§ From Taylor to Itô](from_taylor_to_ito.md) for the canonical multiplication table): Brownian increments scale as $\Delta B_t \sim \sqrt{\Delta t}$, so $(\Delta B_t)^2 \sim \Delta t$ — same order as the linear term. This is promoted to the algebraic rule $(dB_t)^2 = dt$, with $(dt)^2 = 0$ and $dt\,dB_t = 0$.

To illustrate, we simulate a Brownian path and examine both a nonlinear transformation and its quadratic variation.

```python
import numpy as np
import matplotlib.pyplot as plt

# simulation parameters
T = 1
N = 2000
dt = T / N

# fix seed for reproducibility
np.random.seed(42)

# Brownian increments and path
dB = np.sqrt(dt) * np.random.randn(N)
B = np.concatenate(([0], np.cumsum(dB)))

# nonlinear function
F = B**2

# time grids
t_path = np.linspace(0, T, N + 1)
t_incr = np.linspace(dt, T, N)

# quadratic variation and cumulative time
qv = np.cumsum(dB**2)
cum_dt = np.cumsum(np.full(N, dt))

# figure with two axes
fig, (ax1, ax2) = plt.subplots(
    1, 2, figsize=(12, 4)
)

# left plot: Brownian path and transformed path
ax1.plot(t_path, B, label=r"Brownian path $B_t$")
ax1.plot(t_path, F, label=r"$f(B_t)=B_t^2$")
ax1.set_title("Function of Brownian Motion")
ax1.set_xlabel("time")
ax1.set_ylabel("value")
ax1.legend()

# right plot: quadratic variation
ax2.plot(t_incr, qv, label=r"Quadratic variation $\sum(\Delta B_i)^2$")
ax2.plot(t_incr, cum_dt, "--", label=r"Cumulative time $t = \sum dt$")
ax2.set_title("Quadratic Variation")
ax2.set_xlabel("time")
ax2.set_ylabel("value")
ax2.legend()

plt.tight_layout()
plt.show()
```

![Function_of_Brownian_motion](./image/function_of_brownian_motion.png)

*Figure 3. Left: a simulated Brownian path $B_t$ and the transformed process $B_t^2$. Right: the cumulative squared increments $\sum (\Delta B_i)^2$ compared with cumulative time $t = \sum dt$. The close agreement in the right panel illustrates that $(\Delta B_t)^2 \sim \Delta t$, motivating why the squared increment cannot be ignored when expanding functions of Brownian motion.*

Unlike deterministic calculus, the squared increment does **not** vanish. This is why quadratic terms cannot be ignored when expanding functions of Brownian motion. This phenomenon leads directly to the modified Taylor expansion known as **Itô's lemma**.

---

## Exercises

**Exercise 1.** Let $f(x) = \cos(x)$. Compute the second-order Taylor approximation around $x_0 = 0$ and use it to approximate $\cos(0.3)$. Compare with the exact value and compute the absolute error.

??? success "Solution to Exercise 1"
    The second-order Taylor approximation of $f(x) = \cos(x)$ around $x_0 = 0$ requires $f(0) = 1$, $f'(0) = -\sin(0) = 0$, and $f''(0) = -\cos(0) = -1$:

    $$
    \cos(x) \approx 1 + 0 \cdot x + \frac{1}{2}(-1)x^2 = 1 - \frac{x^2}{2}
    $$

    At $x = 0.3$:

    $$
    \cos(0.3) \approx 1 - \frac{(0.3)^2}{2} = 1 - 0.045 = 0.955
    $$

    The exact value is $\cos(0.3) = 0.95534\ldots$, so the absolute error is approximately $|0.955 - 0.95534| \approx 0.00034$. This small error confirms the accuracy of the quadratic approximation for small increments.

---

**Exercise 2.** For the function $f(t, b) = e^t \sin(b)$, compute all partial derivatives up to second order at the expansion point $(t_0, b_0) = (0, 0)$. Write the full second-order Taylor expansion.

??? success "Solution to Exercise 2"
    Compute all partial derivatives of $f(t, b) = e^t \sin(b)$ at $(0, 0)$:

    - $f(0, 0) = e^0 \sin(0) = 0$
    - $f_t = e^t \sin(b)$, so $f_t(0, 0) = 0$
    - $f_b = e^t \cos(b)$, so $f_b(0, 0) = 1$
    - $f_{tt} = e^t \sin(b)$, so $f_{tt}(0, 0) = 0$
    - $f_{bb} = -e^t \sin(b)$, so $f_{bb}(0, 0) = 0$
    - $f_{tb} = e^t \cos(b)$, so $f_{tb}(0, 0) = 1$

    The full second-order Taylor expansion is

    $$
    f(t, b) \approx 0 + 0 \cdot t + 1 \cdot b + \frac{1}{2}(0)t^2 + \frac{1}{2}(0)b^2 + 1 \cdot tb = b + tb
    $$

    That is, $f(t, b) \approx b(1 + t)$.

---

**Exercise 3.** Consider $f(x) = \sqrt{1 + x}$ expanded around $x_0 = 0$.

(a) Write the second-order Taylor approximation.

(b) Compute the linear approximation error and the quadratic approximation error at $x = 0.2$.

(c) Verify that the quadratic approximation error is roughly proportional to $(\Delta x)^3$ by comparing errors at $x = 0.1$ and $x = 0.2$.

??? success "Solution to Exercise 3"
    **(a)** For $f(x) = \sqrt{1 + x}$, we have $f(0) = 1$, $f'(x) = \frac{1}{2}(1+x)^{-1/2}$ so $f'(0) = \frac{1}{2}$, and $f''(x) = -\frac{1}{4}(1+x)^{-3/2}$ so $f''(0) = -\frac{1}{4}$. The second-order Taylor approximation is

    $$
    \sqrt{1+x} \approx 1 + \frac{1}{2}x + \frac{1}{2}\left(-\frac{1}{4}\right)x^2 = 1 + \frac{x}{2} - \frac{x^2}{8}
    $$

    **(b)** At $x = 0.2$, the exact value is $\sqrt{1.2} = 1.09544\ldots$

    - Linear approximation: $1 + 0.1 = 1.1$, error $\approx 0.00456$
    - Quadratic approximation: $1 + 0.1 - 0.005 = 1.095$, error $\approx 0.00044$

    The quadratic approximation reduces the error by roughly a factor of $10$.

    **(c)** At $x = 0.1$: exact value $\sqrt{1.1} = 1.04881\ldots$, quadratic approximation $1 + 0.05 - 0.00125 = 1.04875$, error $\approx 0.00006$. At $x = 0.2$: error $\approx 0.00044$. The ratio is $0.00044 / 0.00006 \approx 7.3 \approx 2^3 = 8$, consistent with the error being proportional to $(\Delta x)^3$ (since $0.2/0.1 = 2$ and $2^3 = 8$).

---

**Exercise 4.** In the two-variable expansion

$$
\Delta f \approx f_t \Delta t + f_b \Delta b + \frac{1}{2}f_{tt}(\Delta t)^2 + \frac{1}{2}f_{bb}(\Delta b)^2 + f_{tb}\Delta t \Delta b
$$

explain why, for a deterministic variable $b$ with $\Delta b = O(\Delta t)$, all three second-order terms are $O((\Delta t)^2)$ and can be dropped. Then explain why, when $b = B_t$ is a Brownian motion with $\Delta B_t = O(\sqrt{\Delta t})$, the term $\frac{1}{2}f_{bb}(\Delta B_t)^2$ is $O(\Delta t)$ and must be retained.

??? success "Solution to Exercise 4"
    For a deterministic variable $b$ with $\Delta b = O(\Delta t)$, the three second-order terms scale as:

    - $\frac{1}{2}f_{tt}(\Delta t)^2 = O((\Delta t)^2)$
    - $\frac{1}{2}f_{bb}(\Delta b)^2 = O((\Delta t)^2)$ since $(\Delta b)^2 = O((\Delta t)^2)$
    - $f_{tb}\Delta t \Delta b = O((\Delta t)^2)$ since $\Delta t \cdot \Delta b = O((\Delta t)^2)$

    All three are $O((\Delta t)^2)$, which is negligible compared to the first-order terms $O(\Delta t)$, so they can be dropped.

    When $b = B_t$ is a Brownian motion, $\Delta B_t = O(\sqrt{\Delta t})$, so $(\Delta B_t)^2 = O(\Delta t)$. The term $\frac{1}{2}f_{bb}(\Delta B_t)^2 = O(\Delta t)$ is the same order as the first-order terms $f_t\Delta t$ and $f_b\Delta B_t$, and therefore must be retained. The other two second-order terms remain $O((\Delta t)^{3/2})$ or higher and still vanish.

---

**Exercise 5.** The Hessian matrix of $f(t, b) = t^2 b + e^b$ at $(t_0, b_0) = (1, 0)$ is

$$
H = \begin{pmatrix} f_{tt} & f_{tb} \\ f_{bt} & f_{bb} \end{pmatrix}
$$

Compute $H$ at $(1, 0)$ and write the full quadratic Taylor expansion of $f$ around this point.

??? success "Solution to Exercise 5"
    For $f(t, b) = t^2 b + e^b$, compute derivatives:

    - $f_t = 2tb$, so $f_t(1, 0) = 0$
    - $f_b = t^2 + e^b$, so $f_b(1, 0) = 2$
    - $f_{tt} = 2b$, so $f_{tt}(1, 0) = 0$
    - $f_{bb} = e^b$, so $f_{bb}(1, 0) = 1$
    - $f_{tb} = 2t$, so $f_{tb}(1, 0) = 2$

    The Hessian at $(1, 0)$ is

    $$
    H = \begin{pmatrix} 0 & 2 \\ 2 & 1 \end{pmatrix}
    $$

    Also, $f(1, 0) = 0 + 1 = 1$. The full quadratic Taylor expansion is

    $$
    f(t, b) \approx 1 + 0 \cdot (t-1) + 2b + \frac{1}{2}\left[0 \cdot (t-1)^2 + 2 \cdot 2(t-1)b + 1 \cdot b^2\right]
    $$

    which simplifies to

    $$
    f(t, b) \approx 1 + 2b + 2(t-1)b + \frac{1}{2}b^2
    $$

---

**Exercise 6.** For a Brownian motion with time step $\Delta t$, consider the three second-order products $(\Delta t)^2$, $\Delta t \cdot \Delta B_t$, and $(\Delta B_t)^2$. State the order of each in terms of powers of $\Delta t$, and identify which ones survive in the limit $\Delta t \to 0$ (i.e., which are $O(\Delta t)$ rather than $o(\Delta t)$).

??? success "Solution to Exercise 6"
    The three second-order products and their orders are:

    - $(\Delta t)^2 = O((\Delta t)^2)$: this is $o(\Delta t)$, so it **vanishes**
    - $\Delta t \cdot \Delta B_t = O((\Delta t)^{3/2})$: since $3/2 > 1$, this is $o(\Delta t)$, so it **vanishes**
    - $(\Delta B_t)^2 = O(\Delta t)$: this is exactly $O(\Delta t)$, so it **survives**

    Only $(\Delta B_t)^2$ survives in the limit $\Delta t \to 0$. This is the term that gives rise to the Itô correction.

---

**Exercise 7.** Simulate a Brownian path with $N = 5000$ steps over $[0, 1]$. For the function $f(x) = x^3$, compute $f(B_T) - f(B_0)$ along the path. Then compute the sum

$$
\sum_{i=0}^{N-1}\left[f'(B_{t_i})\Delta B_i + \frac{1}{2}f''(B_{t_i})(\Delta B_i)^2\right]
$$

Verify numerically that this sum closely approximates $f(B_T) - f(B_0)$, confirming that the quadratic correction term is essential.

??? success "Solution to Exercise 7"
    For $f(x) = x^3$, we have $f'(x) = 3x^2$ and $f''(x) = 6x$. The sum

    $$
    S = \sum_{i=0}^{N-1}\left[3B_{t_i}^2 \Delta B_i + \frac{1}{2}(6B_{t_i})(\Delta B_i)^2\right] = \sum_{i=0}^{N-1}\left[3B_{t_i}^2 \Delta B_i + 3B_{t_i}(\Delta B_i)^2\right]
    $$

    approximates $f(B_T) - f(B_0) = B_T^3$ (since $B_0 = 0$). This is because the sum is precisely the discrete version of the Itô formula applied to $f(x) = x^3$:

    $$
    B_T^3 = \int_0^T 3B_s^2\,dB_s + \frac{1}{2}\int_0^T 6B_s\,ds
    $$

    The first sum term approximates $\int_0^T 3B_s^2\,dB_s$ and the second approximates $3\int_0^T B_s\,ds$ (using $(\Delta B_i)^2 \approx \Delta t$). Running the simulation will confirm that $S \approx B_T^3$, verifying that the quadratic correction is essential — omitting the $3B_{t_i}(\Delta B_i)^2$ terms would leave only the stochastic integral part, which systematically deviates from the true value.
