# Why Itô’s Lemma Matters: From Direct Computation to a Fundamental Theorem


Before the development of **Itô’s lemma**, computing stochastic integrals often meant wrestling directly with the **definition** (Riemann-sum limits), hoping for telescoping tricks, and carefully tracking **quadratic variation**.  

**Analogy**: Just as the Fundamental Theorem of Calculus turns painful Riemann sums into simple antiderivative evaluations, **Itô’s lemma turns painful stochastic integral computations into systematic applications of a chain rule**.

---

## The Definition of the Itô Integral (Hard Way)


Recall the Itô integral is defined as an \(L^2\)-limit of Riemann sums:


\[
\int_0^t f(s,B_s)\,dB_s
:= \lim_{n\to\infty} \sum_{i=0}^{n-1} f(t_i,B_{t_i})\,\bigl(B_{t_{i+1}}-B_{t_i}\bigr),
\qquad t_i = i\,t/n,
\]



where the integrand is evaluated at the **left endpoint**.

**The challenge**: Direct computation typically requires
1. clever algebraic identities to telescope sums,
2. recognition of convergence to quadratic variation,
3. careful bookkeeping across multiple limits.

To see why this becomes unpleasant quickly, we compute a few integrals directly.

---

## Example: Computing \(\int_0^1 B_s\,dB_s\) Directly


By definition,


\[
\int_0^1 B_s\,dB_s
= \lim_{n\to\infty} \sum_{i=0}^{n-1} B_{t_i}\,(B_{t_{i+1}}-B_{t_i}),\qquad t_i=i/n.
\]



Use the identity \(2xy=(x+y)^2-x^2-y^2\) with \(x=B_{t_i}\), \(y=B_{t_{i+1}}-B_{t_i}\):


\[
B_{t_i}(B_{t_{i+1}}-B_{t_i})
= \frac12\bigl(B_{t_{i+1}}^2-B_{t_i}^2\bigr)
-\frac12\bigl(B_{t_{i+1}}-B_{t_i}\bigr)^2.
\]



Summing over \(i\) gives a telescoping term and a quadratic-variation term:

- Telescoping:

  $$
  \sum_{i=0}^{n-1}(B_{t_{i+1}}^2-B_{t_i}^2)=B_1^2-B_0^2=B_1^2.
  $$


- Quadratic variation:

  $$
  \sum_{i=0}^{n-1}(B_{t_{i+1}}-B_{t_i})^2 \xrightarrow{a.s.} [B,B]_1 = 1.
  $$



Therefore,

$$
\boxed{
\int_0^1 B_s\,dB_s = \frac12 B_1^2 - \frac12.
}
$$



Even this “simple” integral required a special trick and knowledge of quadratic variation.

---

## Example: Computing \(\int_0^1 sB_s\,dB_s\) Directly (Messy)


The definition gives

\[
\int_0^1 sB_s\,dB_s
= \lim_{n\to\infty}\sum_{i=0}^{n-1} t_i B_{t_i}(B_{t_{i+1}}-B_{t_i}).
\]



At this point, one tries to rewrite terms so that:
- some pieces telescope,
- some pieces converge to ordinary integrals,
- and some pieces converge to quadratic-variation terms.

Carrying this through leads to the identity (and many intermediate steps):


\[
\boxed{
\int_0^1 sB_s\,dB_s
= \frac12 B_1^2
- \frac12\int_0^1 B_s^2\,ds
- \frac14.
}
\]



This computation is *far* more error-prone than Example 1 and already produces another random integral \(\int_0^1 B_s^2 ds\).

---

## Why Direct Computation Breaks Down Quickly


Try to compute

\[
\int_0^1 B_s^2\,dB_s
= \lim_{n\to\infty}\sum_{i=0}^{n-1} B_{t_i}^2(B_{t_{i+1}}-B_{t_i}).
\]



You would need to rewrite \(B_{t_i}^2(B_{t_{i+1}}-B_{t_i})\) into telescoping terms plus quadratic-variation corrections.  
This becomes rapidly intractable as the integrand’s algebraic complexity increases.

---

# The Easy Way: Itô’s Lemma as a Fundamental Theorem


The point of Itô’s lemma is that it *automatically* accounts for quadratic variation, turning stochastic integration into a systematic procedure.

---

## Ordinary Integrals: The Classical Analogy


Without the Fundamental Theorem of Calculus,

\[
\int_0^t g(s)\,ds
=
\lim_{n\to\infty}\sum_{k=1}^n g\left((k-1)\frac{t}{n}\right)\frac{t}{n}.
\]



With it,

\[
\int_0^t g(s)\,ds = G(t)-G(0),\qquad G'=g.
\]



---

## Itô Integrals Without Itô’s Lemma


By definition,

\[
\int_0^t g(s,B_s)\,dB_s
=
\lim_{n\to\infty}
\sum_{k=1}^n
g\left((k-1)\frac{t}{n},B_{(k-1)t/n}\right)
\bigl(B_{kt/n}-B_{(k-1)t/n}\bigr).
\]



Exact—but usually not computable by hand.

---

## The “Fundamental Theorem” Recipe via Itô’s Lemma


To compute an Itô integral \(\int_0^t g(s,B_s)\,dB_s\), do this:

### 1. Step 1: Identify the integrand


\[
\int_0^t g(s,B_s)\,dB_s.
\]



### 2. Step 2: Find \(f\) such that \(f_b = g\)

Find a function \(f(t,b)\) satisfying

\[
f_b(s,b)=g(s,b).
\]



### 3. Step 3: Apply Itô’s lemma to \(f(t,B_t)\)


\[
f(t,B_t)-f(0,B_0)
=
\int_0^t f_t(s,B_s)\,ds
+\int_0^t f_b(s,B_s)\,dB_s
+\frac12\int_0^t f_{bb}(s,B_s)\,ds.
\]



### 4. Step 4: Solve for the Itô integral


\[
\boxed{
\int_0^t g(s,B_s)\,dB_s
=
f(t,B_t)-f(0,B_0)
-\int_0^t f_t(s,B_s)\,ds
-\frac12\int_0^t f_{bb}(s,B_s)\,ds.
}
\]



This is the stochastic analogue of “\(\int g = G - G(0)\)”.

---

## Re-doing the Earlier Examples (Fast)


### 1. Example A: \(\int_0^1 B_s\,dB_s\)

Choose \(f(b)=\frac12 b^2\). Then \(f_b=b\), \(f_{bb}=1\). Itô’s lemma gives

\[
\frac12 B_1^2 - \frac12 B_0^2
= \int_0^1 B_s\,dB_s + \frac12\int_0^1 1\,ds,
\]


so

\[
\boxed{
\int_0^1 B_s\,dB_s = \frac12 B_1^2 - \frac12.
}
\]



### 2. Example B: \(\int_0^1 sB_s\,dB_s\)

Choose \(f(t,b)=\frac12 t b^2\). Then \(f_b=tb\), \(f_t=\frac12 b^2\), \(f_{bb}=t\). Itô’s lemma yields

\[
\boxed{
\int_0^1 sB_s\,dB_s
= \frac12 B_1^2 - \frac12\int_0^1 B_s^2\,ds - \frac14.
}
\]



### 3. Example C: \(\int_0^1 B_s^2\,dB_s\)

Choose \(f(b)=\frac13 b^3\). Then \(f_b=b^2\), \(f_{bb}=2b\). Itô’s lemma gives

\[
\frac13 B_1^3
= \int_0^1 B_s^2\,dB_s + \int_0^1 B_s\,ds,
\]


so

\[
\boxed{
\int_0^1 B_s^2\,dB_s
= \frac13 B_1^3 - \int_0^1 B_s\,ds.
}
\]



---

## Summary


- **Direct computation** of Itô integrals (via Riemann sums) quickly becomes a technical maze.
- **Itô’s lemma** packages all quadratic-variation effects into a clean rule.
- As a result, Itô’s lemma functions as a **Fundamental Theorem of Stochastic Calculus**: it turns stochastic integration into a systematic “antiderivative-like” procedure.
