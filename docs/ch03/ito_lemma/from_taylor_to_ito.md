# From Taylor to Itô

This page is the **canonical home of the Itô multiplication table** and the mechanical
derivation of Itô's formula from a second-order Taylor expansion. Other pages in this
section recall the rule $(dB_t)^2 = dt$ and link back here rather than rederive it.

Recall (see [§ Quadratic Approximation](taylor_expansion_quadratic.md)): the second-order
Taylor expansion already contains the term $\tfrac12 f_{xx}(\Delta x)^2$. The novelty here
is purely in the **scaling** of $(\Delta B_t)^2$ — the rest is bookkeeping.

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

The survival of $(dW_t)^2$ is the central fact. The scaling argument behind each rule — why deterministic squares vanish but Brownian squares survive — is developed in [Quadratic Taylor Expansion](taylor_expansion_quadratic.md) and [Quadratic Variation of Brownian Motion](../../ch02/brownian_motion/quadratic_variation_of_brownian_motion.md). Here we simply apply the table mechanically.

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

---

## 5. Role in the System

This page is the **origin** of Itô calculus: a single mechanism (Brownian scaling) generates a single rule $(dW_t)^2 = dt$, which forces a single new identity (Itô's formula). Everything downstream is a corollary:

```mermaid
flowchart LR
    A[Taylor Expansion] --> B["(dW)² = dt"]
    B --> C[Itô's Lemma]
    C --> D[Generator]
    D --> E[Dynkin Formula]
```

Subsequent pages **apply** the multiplication table rather than rederive it: [Itô's Lemma](ito_lemma.md) states the transformation rule, [Itô Rules](ito_rules.md) develop the derived identities (product, quotient, integration by parts), and [Applications](ito_calculus_applications.md) puts the lemma to work.

---

## Exercises

**Exercise 1.** Using the Itô multiplication table, evaluate each of the following products:

(a) $(3\,dt)(2\,dW_t)$

(b) $(dW_t)(5\,dW_t)$

(c) $(\mu\,dt + \sigma\,dW_t)^2$ for constants $\mu$ and $\sigma$

??? success "Solution to Exercise 1"
    **(a)** $(3\,dt)(2\,dW_t) = 6\,dt\,dW_t = 6 \cdot 0 = 0$ since $dt\,dW_t = 0$ by the multiplication table.

    **(b)** $(dW_t)(5\,dW_t) = 5(dW_t)^2 = 5\,dt$ since $(dW_t)^2 = dt$.

    **(c)** Expanding:

    $$
    (\mu\,dt + \sigma\,dW_t)^2 = \mu^2(dt)^2 + 2\mu\sigma\,dt\,dW_t + \sigma^2(dW_t)^2
    $$

    Applying the multiplication table: $(dt)^2 = 0$, $dt\,dW_t = 0$, $(dW_t)^2 = dt$. Therefore

    $$
    (\mu\,dt + \sigma\,dW_t)^2 = \sigma^2\,dt
    $$

    Only the Brownian component survives when squaring an Itô differential.

---

**Exercise 2.** Let $f(x) = e^x$. Write out all five terms of the second-order Taylor expansion for $f(t, W_t + dW_t) - f(t, W_t)$, apply the multiplication table term by term, and derive Itô's formula for $d(e^{W_t})$.

??? success "Solution to Exercise 2"
    For $f(x) = e^x$ (no explicit time dependence), we have $f_t = 0$, $f_{tt} = 0$, $f_{tx} = 0$, and $f_x = e^x$, $f_{xx} = e^x$. The five-term expansion is

    $$
    f(t, W_t + dW_t) - f(t, W_t) = 0 \cdot dt + e^{W_t}\,dW_t + \frac{1}{2}(0)(dt)^2 + 0 \cdot dt\,dW_t + \frac{1}{2}e^{W_t}(dW_t)^2
    $$

    Applying the multiplication table: $(dt)^2 = 0$, $dt\,dW_t = 0$, $(dW_t)^2 = dt$:

    $$
    d(e^{W_t}) = e^{W_t}\,dW_t + \frac{1}{2}e^{W_t}\,dt
    $$

    The Itô correction $\frac{1}{2}e^{W_t}\,dt$ arises from the positive curvature of $e^x$ (since $f''(x) = e^x > 0$).

---

**Exercise 3.** Explain why $(dt \cdot dW_t) = 0$ by analyzing the order of magnitude. Specifically, if $dW_t = O(\sqrt{dt})$, show that $dt \cdot dW_t = O((dt)^{3/2})$, and explain why this vanishes faster than $dt$.

??? success "Solution to Exercise 3"
    If $dW_t = O(\sqrt{dt})$, then

    $$
    dt \cdot dW_t = O(dt \cdot \sqrt{dt}) = O((dt)^{3/2})
    $$

    Since $3/2 > 1$, this product vanishes faster than $dt$ as $dt \to 0$. Formally, $\frac{dt \cdot dW_t}{dt} = O((dt)^{1/2}) \to 0$, so $dt \cdot dW_t = o(dt)$. In the Taylor expansion, any term that is $o(dt)$ makes zero contribution in the infinitesimal limit and is therefore set to zero in the Itô multiplication table.

---

**Exercise 4.** Apply the derivation of Section 3 to the function $f(t, x) = \sin(x)$. Compute $f_t$, $f_x$, $f_{xx}$, substitute into the five-term Taylor expansion, apply the multiplication table, and write the resulting Itô formula for $d(\sin(W_t))$.

??? success "Solution to Exercise 4"
    For $f(t, x) = \sin(x)$: $f_t = 0$, $f_x = \cos(x)$, $f_{tt} = 0$, $f_{tx} = 0$, $f_{xx} = -\sin(x)$. The five-term expansion gives

    $$
    d(\sin(W_t)) = 0 \cdot dt + \cos(W_t)\,dW_t + \frac{1}{2}(0)(dt)^2 + 0 \cdot dt\,dW_t + \frac{1}{2}(-\sin(W_t))(dW_t)^2
    $$

    Applying the multiplication table (only $(dW_t)^2 = dt$ survives):

    $$
    d(\sin(W_t)) = \cos(W_t)\,dW_t - \frac{1}{2}\sin(W_t)\,dt
    $$

    The Itô correction $-\frac{1}{2}\sin(W_t)\,dt$ arises from the negative curvature of $\sin(x)$ at points where $\sin(x) > 0$.

---

**Exercise 5.** Consider a general Itô process $dX_t = \mu_t\,dt + \sigma_t\,dW_t$.

(a) Expand $(dX_t)^2 = (\mu_t\,dt + \sigma_t\,dW_t)^2$ into four terms.

(b) Apply the multiplication table to each term and show that $(dX_t)^2 = \sigma_t^2\,dt$.

(c) Use this to write the second-order Taylor term $\frac{1}{2}f_{xx}(dX_t)^2$ for a general $C^2$ function $f$.

??? success "Solution to Exercise 5"
    **(a)** Expanding $(dX_t)^2 = (\mu_t\,dt + \sigma_t\,dW_t)^2$:

    $$
    (dX_t)^2 = \mu_t^2(dt)^2 + 2\mu_t\sigma_t\,dt\,dW_t + \sigma_t^2(dW_t)^2
    $$

    **(b)** Applying the multiplication table term by term:

    - $\mu_t^2(dt)^2 = 0$
    - $2\mu_t\sigma_t\,dt\,dW_t = 0$
    - $\sigma_t^2(dW_t)^2 = \sigma_t^2\,dt$

    Therefore $(dX_t)^2 = \sigma_t^2\,dt$.

    **(c)** The second-order Taylor term becomes

    $$
    \frac{1}{2}f_{xx}(dX_t)^2 = \frac{1}{2}f''(X_t)\sigma_t^2\,dt
    $$

    This is the Itô correction for a general Itô process: it depends only on the diffusion coefficient $\sigma_t$ and the second derivative of $f$.

---

**Exercise 6.** Let $f(x) = x^3$. Derive $d(W_t^3)$ by writing out the full five-term Taylor expansion and applying the multiplication table. Verify that your result matches what you would obtain from applying Itô's formula directly.

??? success "Solution to Exercise 6"
    For $f(x) = x^3$: $f_t = 0$, $f_x = 3x^2$, $f_{xx} = 6x$, $f_{tt} = f_{tx} = 0$. The five-term expansion:

    $$
    d(W_t^3) = 0 \cdot dt + 3W_t^2\,dW_t + 0 + 0 + \frac{1}{2}(6W_t)(dW_t)^2
    $$

    Applying $(dW_t)^2 = dt$:

    $$
    d(W_t^3) = 3W_t^2\,dW_t + 3W_t\,dt
    $$

    Verification via Itô's formula: $df(B_t) = f'(B_t)\,dB_t + \frac{1}{2}f''(B_t)\,dt = 3W_t^2\,dW_t + \frac{1}{2}(6W_t)\,dt = 3W_t^2\,dW_t + 3W_t\,dt$. The results match.

---

**Exercise 7.** Suppose two independent Brownian motions $W_t^1$ and $W_t^2$ are given. Using the multiplication table extended to two independent Brownian motions (where $dW_t^1 \cdot dW_t^2 = 0$), compute $(dW_t^1 + dW_t^2)^2$ and interpret the result.

??? success "Solution to Exercise 7"
    Expanding $(dW_t^1 + dW_t^2)^2$:

    $$
    (dW_t^1 + dW_t^2)^2 = (dW_t^1)^2 + 2\,dW_t^1\,dW_t^2 + (dW_t^2)^2
    $$

    Since $W_t^1$ and $W_t^2$ are independent: $(dW_t^1)^2 = dt$, $(dW_t^2)^2 = dt$, and $dW_t^1 \cdot dW_t^2 = 0$. Therefore

    $$
    (dW_t^1 + dW_t^2)^2 = dt + 0 + dt = 2\,dt
    $$

    Interpretation: the process $W_t^1 + W_t^2$ has quadratic variation $2t$, which is twice that of a single Brownian motion. This is consistent with the fact that $W_t^1 + W_t^2$ has variance $2t$ (the variances add for independent processes). Equivalently, $\frac{1}{\sqrt{2}}(W_t^1 + W_t^2)$ is a standard Brownian motion with quadratic variation $t$.
