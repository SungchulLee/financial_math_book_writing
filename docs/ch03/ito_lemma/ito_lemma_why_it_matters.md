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

### Example A: Computing $\int_0^1 B_s\,dB_s$ Directly

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

### Example B: Computing $\int_0^1 sB_s\,dB_s$ Directly

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

Itô's lemma plays the same role for stochastic integrals, but with a crucial difference: the correction term $\tfrac12 f_{bb}\,ds$ accounts for the non-zero quadratic variation of Brownian motion. This correction arises because the Itô multiplication table gives $(dB_t)^2 = dt$ (see [From Taylor to Itô](from_taylor_to_ito.md)), so the second-order Taylor term $\tfrac12 f_{bb}(dB_t)^2$ does not vanish but instead contributes $\tfrac12 f_{bb}\,dt$. Where the classical FTC simply evaluates an antiderivative at the endpoints, the stochastic version must also subtract this accumulated curvature correction.

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

### Example A: $\int_0^1 B_s\,dB_s$

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

### Example B: $\int_0^1 sB_s\,dB_s$

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

### Example C: $\int_0^1 B_s^2\,dB_s$

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
