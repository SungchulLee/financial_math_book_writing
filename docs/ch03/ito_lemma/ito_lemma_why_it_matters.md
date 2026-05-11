# Why Itô's Lemma Matters

Without Itô's lemma, computing stochastic integrals means wrestling directly with Riemann-sum limits. With it, the computation becomes systematic. This page motivates Itô's lemma by showing what it replaces, then demonstrates how it functions as the **Fundamental Theorem of Stochastic Calculus**.

**Concept.** Itô's lemma is a systematic antiderivative-based method for evaluating stochastic integrals of the form $\int_0^t g(s, B_s)\,dB_s$, playing the same role as the Fundamental Theorem of Calculus in ordinary integration.

---

## 1. The Direct Computation Problem

The **Itô integral** is defined as an $L^2$-limit of Riemann sums:

$$
\int_0^t f(s,B_s)\,dB_s
:= \lim_{n\to\infty} \sum_{i=0}^{n-1} f(t_i,B_{t_i})\,\bigl(B_{t_{i+1}}-B_{t_i}\bigr),
\qquad t_i = i\,t/n
$$

where the integrand is evaluated at the **left endpoint**.

Direct computation from this definition typically requires:

- Clever algebraic identities to telescope sums
- Recognition of which sums converge to quadratic variation $[B,B]_t$
- Careful bookkeeping across multiple limits

To see why this becomes unpleasant quickly, we compute a few integrals directly.

---

## 2. Why the Direct Approach Is Hard

### Example A: Computing the Integral of B dB Directly

By definition,

$$
\int_0^1 B_s\,dB_s
= \lim_{n\to\infty} \sum_{i=0}^{n-1} B_{t_i}\,(B_{t_{i+1}}-B_{t_i}),\qquad t_i=i/n
$$

Use the identity $2xy=(x+y)^2-x^2-y^2$ with $x=B_{t_i}$, $y=B_{t_{i+1}}-B_{t_i}$:

$$
B_{t_i}(B_{t_{i+1}}-B_{t_i})
= \frac12\bigl(B_{t_{i+1}}^2-B_{t_i}^2\bigr)
-\frac12\bigl(B_{t_{i+1}}-B_{t_i}\bigr)^2
$$

Summing over $i$ gives a telescoping term and a quadratic-variation term:

- Telescoping:

    $$
    \sum_{i=0}^{n-1}(B_{t_{i+1}}^2-B_{t_i}^2)=B_1^2-B_0^2=B_1^2
    $$

- Quadratic variation:

    $$
    \sum_{i=0}^{n-1}(B_{t_{i+1}}-B_{t_i})^2 \xrightarrow{L^2} [B,B]_1 = 1
    $$

Therefore,

$$
\boxed{
\int_0^1 B_s\,dB_s = \frac12 B_1^2 - \frac12
}
$$

Even this "simple" integral required a special algebraic trick and knowledge of quadratic variation.

### Example B: Computing the Integral of sB dB Directly

The definition gives

$$
\int_0^1 sB_s\,dB_s
= \lim_{n\to\infty}\sum_{i=0}^{n-1} t_i B_{t_i}(B_{t_{i+1}}-B_{t_i})
$$

Write $2t_i B_{t_i}(B_{t_{i+1}}-B_{t_i}) = t_i(B_{t_{i+1}}^2 - B_{t_i}^2) - t_i(B_{t_{i+1}}-B_{t_i})^2$ and apply Abel summation (summation by parts) to the first sum:

$$
\sum_{i=0}^{n-1} t_i(B_{t_{i+1}}^2 - B_{t_i}^2)
= t_{n-1}B_1^2 - \sum_{i=1}^{n-1}(t_i - t_{i-1})B_{t_i}^2
$$

As $n\to\infty$: the boundary term $t_{n-1}B_1^2 \to B_1^2$, the ordinary Riemann sum converges to $\int_0^1 B_s^2\,ds$, and the quadratic-variation sum satisfies

$$
\sum_{i=0}^{n-1} t_i(B_{t_{i+1}}-B_{t_i})^2 \xrightarrow{L^2} \int_0^1 s\,d[B,B]_s = \int_0^1 s\,ds = \frac12
$$

Combining and dividing by 2:

$$
\boxed{
\int_0^1 sB_s\,dB_s
= \frac12 B_1^2

- \frac12\int_0^1 B_s^2\,ds
- \frac14
}
$$

This computation is far more error-prone than Example A and produces another random integral $\int_0^1 B_s^2\,ds$ that has no closed form. More complex integrands make things worse rapidly.

---

## 3. Itô's Lemma as a Fundamental Theorem

In ordinary calculus, the Fundamental Theorem eliminates Riemann-sum computations:

$$
\int_0^t g(s)\,ds = G(t)-G(0),\qquad G'=g
$$

Itô's lemma plays the same role for stochastic integrals, but with the Itô correction $\tfrac12 f_{bb}\,dt$ — the curvature term that survives because $(dB_t)^2 = dt$ (see [Quadratic Taylor Expansion](taylor_expansion_quadratic.md)). Where the classical FTC simply evaluates an antiderivative at the endpoints, the stochastic version must also subtract this accumulated curvature correction.

To compute $\int_0^t g(s,B_s)\,dB_s$ using Itô's lemma:

1. **Identify the integrand** $g(s,b)$ in $\int_0^t g(s,B_s)\,dB_s$
2. **Find an antiderivative** $f(t,b)$ such that $f_b(s,b) = g(s,b)$
3. **Apply Itô's lemma** to $f(t,B_t)$:

    $$
    f(t,B_t)-f(0,B_0)
    =
    \int_0^t f_t(s,B_s)\,ds
    +\int_0^t f_b(s,B_s)\,dB_s
    +\frac12\int_0^t f_{bb}(s,B_s)\,ds
    $$

4. **Solve for the Itô integral**, noting that the remaining integrals $\int_0^t f_t\,ds$ and $\int_0^t f_{bb}\,ds$ are **ordinary (Riemann) integrals**, not stochastic integrals:

    $$
    \boxed{
    \int_0^t g(s,B_s)\,dB_s
    =
    f(t,B_t)-f(0,B_0)
    -\int_0^t f_t(s,B_s)\,ds
    -\frac12\int_0^t f_{bb}(s,B_s)\,ds
    }
    $$

This is the stochastic analogue of $\int_0^t g(s)\,ds = G(t) - G(0)$. The right-hand side involves only the antiderivative evaluated at endpoints and two ordinary integrals — no stochastic limits required.

---

## 4. Re-doing the Earlier Examples

### Example A: Integral of B dB

Choose $f(b)=\frac12 b^2$. Then $f_t=0$, $f_b=b$, $f_{bb}=1$. Itô's lemma gives (using $B_0 = 0$):

$$
\frac12 B_1^2 - \underbrace{\frac12 \cdot 0^2}_{f(0,B_0)=0}
= \underbrace{\int_0^1 0\,ds}_{=\,0}

+ \int_0^1 B_s\,dB_s
+ \frac12\int_0^1 1\,ds
$$

so

$$
\boxed{
\int_0^1 B_s\,dB_s = \frac12 B_1^2 - \frac12
}
$$

### Example B: Integral of sB dB

Choose $f(t,b)=\frac12 t b^2$. Then $f_t=\frac12 b^2$, $f_b=tb$, $f_{bb}=t$. Itô's lemma gives (using $B_0 = 0$):

$$
\frac12 \cdot 1 \cdot B_1^2 - 0
= \int_0^1 \frac12 B_s^2\,ds

+ \int_0^1 sB_s\,dB_s
+ \frac12\int_0^1 s\,ds
$$

The last term is an ordinary integral: $\frac12\int_0^1 s\,ds = \frac12 \cdot \frac12 = \frac14$. Solving for the Itô integral:

$$
\boxed{
\int_0^1 sB_s\,dB_s
= \frac12 B_1^2 - \frac12\int_0^1 B_s^2\,ds - \frac14
}
$$

!!! note "Speed vs. Closed Form"

    The result still contains $\int_0^1 B_s^2\,ds$ — but we arrived at it in a few lines rather than through pages of Riemann-sum manipulations.

### Example C: Integral of B² dB

Choose $f(b)=\frac13 b^3$. Then $f_t=0$, $f_b=b^2$, $f_{bb}=2b$, so $\frac12 f_{bb}\,ds = b\,ds = B_s\,ds$. Itô's lemma gives (using $B_0 = 0$):

$$
\frac13 B_1^3 - 0
= \underbrace{\int_0^1 0\,ds}_{f_t=0,\;=\,0}

+ \int_0^1 B_s^2\,dB_s
+ \int_0^1 B_s\,ds
$$

Rearranging:

$$
\boxed{
\int_0^1 B_s^2\,dB_s
= \frac13 B_1^3 - \int_0^1 B_s\,ds
}
$$

---

## 5. Summary

| Integral | Antiderivative chosen | Method | Result |
|---|---|---|---|
| $\int_0^1 B_s\,dB_s$ | $f = \frac12 b^2$ | Itô's lemma | $\frac12 B_1^2 - \frac12$ |
| $\int_0^1 sB_s\,dB_s$ | $f = \frac12 tb^2$ | Itô's lemma | $\frac12 B_1^2 - \frac12\int_0^1 B_s^2\,ds - \frac14$ |
| $\int_0^1 B_s^2\,dB_s$ | $f = \frac13 b^3$ | Itô's lemma | $\frac13 B_1^3 - \int_0^1 B_s\,ds$ |

Just as the classical Fundamental Theorem of Calculus turns Riemann sums into antiderivative evaluations, Itô's lemma turns stochastic integral computations into systematic applications of a chain rule — functioning as a **Fundamental Theorem of Stochastic Calculus**. The formal statement appears in [Itô's Lemma](ito_lemma.md).

---

## Exercises

**Exercise 1.** Compute $\int_0^t B_s^3\,dB_s$ by choosing an appropriate antiderivative $f(x)$ such that $f'(x) = x^3$, applying Itô's lemma, and solving for the stochastic integral.

??? success "Solution to Exercise 1"
    Choose $f(x) = \frac{1}{4}x^4$, so that $f'(x) = x^3$. Then $f''(x) = 3x^2$. Applying Itô's lemma:

    $$
    d\!\left(\frac{B_t^4}{4}\right) = B_t^3\,dB_t + \frac{1}{2}(3B_t^2)\,dt
    $$

    Integrating from $0$ to $t$ (with $B_0 = 0$):

    $$
    \frac{B_t^4}{4} = \int_0^t B_s^3\,dB_s + \frac{3}{2}\int_0^t B_s^2\,ds
    $$

    Solving for the stochastic integral:

    $$
    \int_0^t B_s^3\,dB_s = \frac{1}{4}B_t^4 - \frac{3}{2}\int_0^t B_s^2\,ds
    $$

---

**Exercise 2.** Evaluate $\int_0^1 B_s\,dB_s$ directly from the Riemann-sum definition (as in Example A of this page), but this time on the interval $[0, T]$ for general $T > 0$. Show that the result is $\frac{1}{2}(B_T^2 - T)$.

??? success "Solution to Exercise 2"
    By definition, on $[0, T]$ with $t_i = iT/n$:

    $$
    \int_0^T B_s\,dB_s = \lim_{n\to\infty}\sum_{i=0}^{n-1}B_{t_i}(B_{t_{i+1}} - B_{t_i})
    $$

    Using $2xy = (x+y)^2 - x^2 - y^2$ with $x = B_{t_i}$, $y = B_{t_{i+1}} - B_{t_i}$:

    $$
    B_{t_i}(B_{t_{i+1}} - B_{t_i}) = \frac{1}{2}(B_{t_{i+1}}^2 - B_{t_i}^2) - \frac{1}{2}(B_{t_{i+1}} - B_{t_i})^2
    $$

    Summing: the first part telescopes to $\frac{1}{2}(B_T^2 - B_0^2) = \frac{1}{2}B_T^2$. The second part converges in $L^2$ to $\frac{1}{2}[B,B]_T = \frac{1}{2}T$. Therefore

    $$
    \int_0^T B_s\,dB_s = \frac{1}{2}B_T^2 - \frac{1}{2}T = \frac{1}{2}(B_T^2 - T)
    $$

---

**Exercise 3.** Choose the antiderivative $f(t, b) = \frac{1}{3}t b^3$ and apply Itô's lemma to compute $d\!\left(\frac{1}{3}t B_t^3\right)$. Use the result to express $\int_0^t s B_s^2\,dB_s$ in terms of $B_t$, $t$, and ordinary integrals.

??? success "Solution to Exercise 3"
    For $f(t, b) = \frac{1}{3}t b^3$, compute:

    - $f_t = \frac{1}{3}b^3$
    - $f_b = tb^2$
    - $f_{bb} = 2tb$

    Itô's lemma gives:

    $$
    d\!\left(\frac{1}{3}tB_t^3\right) = \frac{1}{3}B_t^3\,dt + tB_t^2\,dB_t + \frac{1}{2}(2tB_t)\,dt
    $$

    Simplifying: $d\!\left(\frac{1}{3}tB_t^3\right) = \frac{1}{3}B_t^3\,dt + tB_t^2\,dB_t + tB_t\,dt$. Integrating from $0$ to $t$:

    $$
    \frac{1}{3}tB_t^3 = \int_0^s \frac{1}{3}B_u^3\,du + \int_0^t sB_s^2\,dB_s + \int_0^t sB_s\,ds
    $$

    Solving for the stochastic integral:

    $$
    \int_0^t s B_s^2\,dB_s = \frac{1}{3}tB_t^3 - \frac{1}{3}\int_0^t B_s^3\,ds - \int_0^t sB_s\,ds
    $$

---

**Exercise 4.** Consider $\int_0^t \cos(B_s)\,dB_s$.

(a) Identify an antiderivative $f(x)$ such that $f'(x) = \cos(x)$.

(b) Compute $f''(x)$ and apply Itô's lemma.

(c) Express $\int_0^t \cos(B_s)\,dB_s$ in terms of $\sin(B_t)$ and an ordinary integral.

??? success "Solution to Exercise 4"
    **(a)** The antiderivative is $f(x) = \sin(x)$, since $f'(x) = \cos(x)$.

    **(b)** We have $f''(x) = -\sin(x)$. Applying Itô's lemma to $f(B_t) = \sin(B_t)$:

    $$
    d(\sin(B_t)) = \cos(B_t)\,dB_t + \frac{1}{2}(-\sin(B_t))\,dt
    $$

    **(c)** Integrating from $0$ to $t$ (with $B_0 = 0$, so $\sin(B_0) = 0$):

    $$
    \sin(B_t) = \int_0^t \cos(B_s)\,dB_s - \frac{1}{2}\int_0^t \sin(B_s)\,ds
    $$

    Solving for the stochastic integral:

    $$
    \int_0^t \cos(B_s)\,dB_s = \sin(B_t) + \frac{1}{2}\int_0^t \sin(B_s)\,ds
    $$

---

**Exercise 5.** Explain why the direct Riemann-sum approach to computing $\int_0^1 B_s^2\,dB_s$ would require Abel summation and careful limit arguments, while the antiderivative method (choosing $f(x) = \frac{1}{3}x^3$) yields the answer in three lines. What is the role of the Itô correction $\frac{1}{2}f''(B_s)\,ds$ in making the shortcut work?

??? success "Solution to Exercise 5"
    The direct approach to $\int_0^1 B_s^2\,dB_s$ starts from

    $$
    \sum_{i=0}^{n-1}B_{t_i}^2(B_{t_{i+1}} - B_{t_i})
    $$

    To handle this, one would need to use an identity like $x^2 y = \frac{1}{3}[(x+y)^3 - x^3] - xy^2 - \frac{1}{3}y^3$ (or a similar algebraic decomposition), then apply Abel summation to telescoping sums, carefully track the quadratic variation terms, and take limits. This involves several pages of calculation and multiple convergence arguments.

    The antiderivative method simply chooses $f(x) = \frac{1}{3}x^3$ with $f'(x) = x^2$ and $f''(x) = 2x$, applies Itô's lemma:

    $$
    d\!\left(\frac{B_t^3}{3}\right) = B_t^2\,dB_t + B_t\,dt
    $$

    and rearranges to get $\int_0^t B_s^2\,dB_s = \frac{1}{3}B_t^3 - \int_0^t B_s\,ds$ in three lines. The Itô correction $\frac{1}{2}f''(B_s)\,ds = B_s\,ds$ is the term that accounts for the quadratic variation contribution. Without it, the antiderivative evaluation $f(B_t) - f(B_0)$ would equal the stochastic integral plus an error — the correction term precisely fills this gap.

---

**Exercise 6.** Let $f(b) = e^{-b}$. Use the Itô lemma antiderivative method to evaluate $\int_0^t e^{-B_s}\,dB_s$. Write the result in terms of $e^{-B_t}$ and an ordinary integral involving $e^{-B_s}$.

??? success "Solution to Exercise 6"
    For $f(b) = e^{-b}$: $f'(b) = -e^{-b}$ and $f''(b) = e^{-b}$. Applying Itô's lemma:

    $$
    d(e^{-B_t}) = -e^{-B_t}\,dB_t + \frac{1}{2}e^{-B_t}\,dt
    $$

    Integrating from $0$ to $t$ (with $B_0 = 0$, so $e^{-B_0} = 1$):

    $$
    e^{-B_t} - 1 = -\int_0^t e^{-B_s}\,dB_s + \frac{1}{2}\int_0^t e^{-B_s}\,ds
    $$

    Since $f'(x) = -e^{-x}$, the integrand we want is $e^{-B_s} = -f'(B_s)$. Rearranging:

    $$
    \int_0^t e^{-B_s}\,dB_s = 1 - e^{-B_t} + \frac{1}{2}\int_0^t e^{-B_s}\,ds
    $$

---

**Exercise 7.** The general strategy states: choose $f(t, x)$ with $f_x = g$, apply Itô's lemma, and rearrange. Show that this strategy can fail to produce a closed-form answer by attempting to compute $\int_0^t e^{B_s^2}\,dB_s$. Specifically, find $f(x)$ with $f'(x) = e^{x^2}$, compute $f''(x)$, and explain why the resulting correction integral $\frac{1}{2}\int_0^t f''(B_s)\,ds$ does not simplify the problem.

??? success "Solution to Exercise 7"
    The antiderivative is $f(x) = \int_0^x e^{u^2}\,du$ (the imaginary error function, up to a constant — it has no elementary closed form). Then $f'(x) = e^{x^2}$ and $f''(x) = 2x\,e^{x^2}$. Itô's lemma gives:

    $$
    f(B_t) - f(0) = \int_0^t e^{B_s^2}\,dB_s + \frac{1}{2}\int_0^t 2B_s\,e^{B_s^2}\,ds
    $$

    Rearranging:

    $$
    \int_0^t e^{B_s^2}\,dB_s = f(B_t) - \int_0^t B_s\,e^{B_s^2}\,ds
    $$

    The right-hand side involves $f(B_t) = \int_0^{B_t} e^{u^2}\,du$ (no closed form) and the ordinary integral $\int_0^t B_s e^{B_s^2}\,ds$ (also no closed form). The strategy does not simplify the problem because neither the antiderivative $f$ nor the correction integral $\frac{1}{2}\int_0^t f''(B_s)\,ds$ can be evaluated in closed form. This illustrates that the antiderivative method, while systematic, is only as useful as the tractability of $f$ and its derivatives.
