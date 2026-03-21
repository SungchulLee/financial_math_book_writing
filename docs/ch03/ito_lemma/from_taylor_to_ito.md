# From Taylor to Itô

This page derives Itô's formula mechanically from a second-order Taylor expansion.
The key tool is the **Itô multiplication table**, which evaluates each second-order
differential product term by term, reducing the five-term expansion to Itô's formula.

---

## 1. Second-Order Taylor Expansion

Let $f(t, x)$ be $C^{1,2}([0,\infty)\times\mathbb{R})$. A second-order Taylor
expansion in the increments $dt$ and $dW_t$ gives

$$
f(t+dt,\, W_t + dW_t) - f(t,\, W_t)
= f_t \, dt + f_x \, dW_t
+ \tfrac{1}{2} f_{tt} (dt)^2
+ f_{tx} \, dt \, dW_t
+ \tfrac{1}{2} f_{xx} (dW_t)^2
$$

where all partial derivatives are evaluated at $(t, W_t)$, and

$$
f_t = \frac{\partial f}{\partial t}, \quad
f_x = \frac{\partial f}{\partial x}, \quad
f_{tt} = \frac{\partial^2 f}{\partial t^2}, \quad
f_{tx} = \frac{\partial^2 f}{\partial t \, \partial x}, \quad
f_{xx} = \frac{\partial^2 f}{\partial x^2}
$$

This expansion has two first-order terms ($f_t\,dt$ and $f_x\,dW_t$) and three
second-order terms. The next step is to decide which of the second-order terms survive.

---

## 2. The Itô Multiplication Table

Each second-order term involves a product of two differentials.
The following table gives the limiting value of each product:

$$
\begin{array}{c|cc}
\times & dt & dW_t \\
\hline
dt     & 0  & 0    \\
dW_t   & 0  & dt   \\
\end{array}
$$

That is:

$$
(dt)^2 = 0, \qquad dt \, dW_t = 0, \qquad (dW_t)^2 = dt
$$

**Why each rule holds:**

| Product | Order | Verdict |
|---|---|---|
| $(dt)^2$ | $O((\Delta t)^2)$ | vanishes — higher-order infinitesimal |
| $dt \, dW_t$ | $O((\Delta t)^{3/2})$ | vanishes — since $3/2 > 1$, this is $o(dt)$ |
| $(dW_t)^2$ | $O(\Delta t)$ | **survives** — this is quadratic variation |

The survival of $(dW_t)^2$ is the central fact. A smooth **deterministic** path
satisfies $\Delta x = O(\Delta t)$, so $(\Delta x)^2 = O((\Delta t)^2)$ vanishes.
Brownian motion instead satisfies $\Delta W_t = O(\sqrt{\Delta t})$, so
$(\Delta W_t)^2 = O(\Delta t)$ — the same order as $dt$ itself. The rigorous
statement is that the quadratic variation of Brownian motion equals $t$; see
[Quadratic Variation of Brownian Motion](../../ch02/brownian_motion/quadratic_variation_of_brownian_motion.md).

!!! tip "The key asymmetry"

    A smooth **deterministic** path satisfies $\Delta x = O(\Delta t)$, so $(\Delta x)^2 = O((\Delta t)^2)$ — it **vanishes**.  
    Brownian motion satisfies $\Delta W = O(\sqrt{\Delta t})$, so $(\Delta W)^2 = O(\Delta t)$ — it **survives**.  
    This single difference is the source of the Itô correction term that separates stochastic calculus from ordinary calculus.

---

## 3. Applying the Table Term by Term

Return to the five-term expansion and apply the multiplication table to each
second-order product:

$$
f(t+dt,\, W_t+dW_t) - f(t,\, W_t)
= f_t \, dt
+ f_x \, dW_t
+ \tfrac{1}{2} f_{tt} \underbrace{(dt)^2}_{=\,0}
+ f_{tx} \underbrace{dt \, dW_t}_{=\,0}
+ \tfrac{1}{2} f_{xx} \underbrace{(dW_t)^2}_{=\,dt}
$$

Dropping the zero terms and substituting $(dW_t)^2 = dt$:

$$
\boxed{
df(t, W_t)
= f_t \, dt + f_x \, dW_t + \tfrac{1}{2} f_{xx} \, dt
}
$$

This is **Itô's formula**. The term $\tfrac{1}{2} f_{xx} \, dt$ is the **Itô correction** —
it has no counterpart in ordinary calculus and arises entirely from the survival of
$(dW_t)^2$.

$\square$

---

## 4. Worked Example

Let $f(x) = x^2$. We set $f(t,x) = x^2$, so $f_t = f_{tt} = f_{tx} = 0$,
$f_x = 2x$, and $f_{xx} = 2$.

**Step 1.** Write all five terms in the same order as Section 1,
substituting the zero coefficients explicitly:

$$
f(t, W_t + dW_t) - f(t, W_t)
= \underbrace{0 \cdot dt}_{f_t\,dt\,=\,0}
+ f_x \, dW_t
+ \tfrac{1}{2} f_{tt} \underbrace{(dt)^2}_{=\,0}
+ f_{tx} \underbrace{dt \, dW_t}_{=\,0}
+ \tfrac{1}{2} f_{xx} (dW_t)^2
$$

**Step 2.** Drop the zero terms and substitute $f_x = 2x\big|_{x=W_t} = 2W_t$
and $f_{xx} = 2$:

$$
= 2W_t \, dW_t + \tfrac{1}{2} \cdot 2 \cdot (dW_t)^2
$$

**Step 3.** Apply $(dW_t)^2 = dt$ and simplify $\tfrac{1}{2} \cdot 2 = 1$:

$$
d(W_t^2) = 2W_t \, dW_t + dt
$$

In ordinary calculus one would expect only $d(x^2) = 2x\,dx$. The extra $dt$
term is the Itô correction: the positive curvature of $x^2$ converts symmetric
Brownian fluctuations into a positive drift.

$\square$

---

!!! note "Extension to general Itô processes"

    The same procedure extends to a general Itô process $dX_t = \mu_t\,dt + \sigma_t\,dW_t$. The key step is that $(dX_t)^2 = \sigma_t^2\,dt$, because only the $dW_t$ component survives squaring: $(\mu_t\,dt)^2 = 0$, $\mu_t\,dt\cdot\sigma_t\,dW_t = 0$, and $(\sigma_t\,dW_t)^2 = \sigma_t^2\,dt$. Substituting this into the second-order Taylor term yields the general Itô formula; see [Itô's Lemma](ito_lemma.md).
