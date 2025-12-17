# Computing Itô Integrals: The Hard Way vs. The Easy Way

Before the development of Itô's lemma, computing stochastic integrals was a laborious process involving careful manipulation of Riemann sums, telescoping series, and quadratic variation. This section demonstrates the **direct computation** of Itô integrals from the definition, highlighting the computational difficulty and motivating the power of Itô's lemma.

**Analogy**: Just as the Fundamental Theorem of Calculus transforms painful Riemann sum computations into simple antiderivative evaluations, **Itô's lemma transforms painful stochastic integral computations into simple applications of the chain rule**.

---

## The definition of the Itô integral

Recall that the Itô integral is defined as the \(L^2\)-limit of Riemann sums:


$$
\int_0^t f(s, B_s) \, dB_s
:= \lim_{n \to \infty} \sum_{i=0}^{n-1} f(t_i, B_{t_i}) (B_{t_{i+1}} - B_{t_i})
$$



where \(t_i = it/n\) is a uniform partition and we evaluate \(f\) at the **left endpoint** of each interval.

**The challenge**: For non-trivial integrands \(f(s, B_s)\), computing this limit directly requires:
1. Clever algebraic manipulations to telescope or simplify sums
2. Recognition of convergence to quadratic variation
3. Careful tracking of multiple limiting processes

Let's see this in action.

---

## Example 1: Computing \(\int_0^1 B_s \, dB_s\) directly

**Problem**: Evaluate \(\int_0^1 B_s dB_s\) using only the definition of the Itô integral.

### Step 1: Write the Riemann sum

By definition:


$$
\int_0^1 B_s \, dB_s
= \lim_{n \to \infty} \sum_{i=0}^{n-1} B_{t_i} (B_{t_{i+1}} - B_{t_i})
$$



where \(t_i = i/n\).

### Step 2: Algebraic manipulation

The key trick is to use the identity:


$$
2xy = (x + y)^2 - x^2 - y^2
$$



Setting \(x = B_{t_i}\) and \(y = B_{t_{i+1}} - B_{t_i}\):


$$
2B_{t_i}(B_{t_{i+1}} - B_{t_i})
= (B_{t_i} + B_{t_{i+1}} - B_{t_i})^2 - B_{t_i}^2 - (B_{t_{i+1}} - B_{t_i})^2
$$




$$
= B_{t_{i+1}}^2 - B_{t_i}^2 - (B_{t_{i+1}} - B_{t_i})^2
$$



Therefore:


$$
B_{t_i}(B_{t_{i+1}} - B_{t_i})
= \frac{1}{2}\big[B_{t_{i+1}}^2 - B_{t_i}^2\big] - \frac{1}{2}(B_{t_{i+1}} - B_{t_i})^2
$$



### Step 3: Sum over the partition


$$
\sum_{i=0}^{n-1} B_{t_i}(B_{t_{i+1}} - B_{t_i})
= \frac{1}{2}\sum_{i=0}^{n-1} \big[B_{t_{i+1}}^2 - B_{t_i}^2\big]
- \frac{1}{2}\sum_{i=0}^{n-1} (B_{t_{i+1}} - B_{t_i})^2
$$



### Step 4: Evaluate each sum in the limit

**First sum (telescoping)**:


$$
\sum_{i=0}^{n-1} \big[B_{t_{i+1}}^2 - B_{t_i}^2\big]
= B_1^2 - B_0^2
= B_1^2
$$



since \(B_0 = 0\).

**Second sum (quadratic variation)**:


$$
\sum_{i=0}^{n-1} (B_{t_{i+1}} - B_{t_i})^2
\xrightarrow{\text{a.s.}} [B, B]_1 = 1
$$



This is the **quadratic variation** of Brownian motion on \([0, 1]\).

### Step 5: Combine the results


$$
\int_0^1 B_s \, dB_s
= \frac{1}{2}B_1^2 - \frac{1}{2} \cdot 1
$$




$$
\boxed{
\int_0^1 B_s \, dB_s = \frac{1}{2}B_1^2 - \frac{1}{2}
}
$$



**Remarks**:
- This computation required recognizing a clever algebraic identity
- We needed to know the quadratic variation formula \([B, B]_t = t\)
- The calculation was non-trivial despite the simple integrand \(B_s\)

---

## Example 2: Computing \(\int_0^1 s B_s \, dB_s\) directly

**Problem**: Evaluate \(\int_0^1 s B_s dB_s\) using only the definition.

This is significantly more complex than Example 1.

### Step 1: Write the Riemann sum


$$
\int_0^1 s B_s \, dB_s
= \lim_{n \to \infty} \sum_{i=0}^{n-1} t_i B_{t_i} (B_{t_{i+1}} - B_{t_i})
$$



### Step 2: Expand using the product identity

We use a similar but more complex algebraic trick. The key is to recognize:


$$
t_i B_{t_i} (B_{t_{i+1}} - B_{t_i})
$$



We'll express this in terms that telescope or converge to known limits.

**Approach**: Write out:


$$
t_i B_{t_i} (B_{t_{i+1}} - B_{t_i})
= \frac{1}{2}\big[t_{i+1} B_{t_{i+1}}^2 - t_i B_{t_i}^2\big]
- \frac{1}{2}(t_{i+1} - t_i) B_{t_{i+1}}^2
- \frac{1}{2}t_i(B_{t_{i+1}} - B_{t_i})^2
$$



Let's verify this identity by expanding the right-hand side:


$$
\begin{align}
\text{RHS} &= \frac{1}{2}t_{i+1}B_{t_{i+1}}^2 - \frac{1}{2}t_i B_{t_i}^2
- \frac{1}{2}dt \cdot B_{t_{i+1}}^2
- \frac{1}{2}t_i(B_{t_{i+1}} - B_{t_i})^2\\
&= \frac{1}{2}t_{i+1}B_{t_{i+1}}^2 - \frac{1}{2}t_i B_{t_i}^2
- \frac{1}{2}dt \cdot B_{t_{i+1}}^2
- \frac{1}{2}t_i(B_{t_{i+1}}^2 - 2B_{t_{i+1}}B_{t_i} + B_{t_i}^2)\\
&= \frac{1}{2}(t_{i+1} - t_i - dt)B_{t_{i+1}}^2
- \frac{1}{2}t_i B_{t_i}^2 + t_i B_{t_{i+1}}B_{t_i} - \frac{1}{2}t_i B_{t_i}^2\\
&= -\frac{1}{2}dt \cdot B_{t_{i+1}}^2 + t_i B_{t_i}B_{t_{i+1}}
\end{align}
$$



Wait, let me reconsider. Let's use a different decomposition.

**Better approach**: We can write:


$$
\begin{align}
t_i B_{t_i} (B_{t_{i+1}} - B_{t_i})
&= \frac{1}{2}(t_{i+1} B_{t_{i+1}}^2 - t_i B_{t_i}^2)\\
&\quad - \frac{1}{2}(t_{i+1} - t_i) B_{t_{i+1}}^2\\
&\quad - \frac{1}{2} t_i (B_{t_{i+1}} - B_{t_i})^2
\end{align}
$$



### Step 3: Further decomposition of the second term

The term \(-\frac{1}{2}dt \cdot B_{t_{i+1}}^2\) needs to be related to quantities at \(t_i\):


$$
-\frac{1}{2}dt \cdot B_{t_{i+1}}^2
= -\frac{1}{2}dt \cdot B_{t_i}^2
- \frac{1}{2}dt \cdot (B_{t_{i+1}}^2 - B_{t_i}^2)
$$



The difference can be written as:


$$
B_{t_{i+1}}^2 - B_{t_i}^2
= 2B_{t_i}(B_{t_{i+1}} - B_{t_i}) + (B_{t_{i+1}} - B_{t_i})^2
$$



Therefore:


$$
-\frac{1}{2}dt \cdot B_{t_{i+1}}^2
= -\frac{1}{2}dt \cdot B_{t_i}^2
- dt \cdot B_{t_i}(B_{t_{i+1}} - B_{t_i})
- \frac{1}{2}dt \cdot (B_{t_{i+1}} - B_{t_i})^2
$$



### Step 4: Sum over the partition

This becomes extremely messy. Let's organize the terms that arise:


$$
\begin{align}
\sum_{i=0}^{n-1} t_i B_{t_i}(B_{t_{i+1}} - B_{t_i})
&= \frac{1}{2}\sum_{i=0}^{n-1}(t_{i+1}B_{t_{i+1}}^2 - t_i B_{t_i}^2)\\
&\quad - \frac{1}{2}\sum_{i=0}^{n-1} dt \cdot B_{t_i}^2\\
&\quad - \sum_{i=0}^{n-1} dt \cdot B_{t_i}(B_{t_{i+1}} - B_{t_i})\\
&\quad - \frac{1}{2}\sum_{i=0}^{n-1} (t_i + dt)(B_{t_{i+1}} - B_{t_i})^2
\end{align}
$$



### Step 5: Take limits

**First term (telescoping)**:


$$
\frac{1}{2}\sum_{i=0}^{n-1}(t_{i+1}B_{t_{i+1}}^2 - t_i B_{t_i}^2)
= \frac{1}{2}(1 \cdot B_1^2 - 0)
= \frac{1}{2}B_1^2
$$



**Second term (Riemann integral)**:


$$
\frac{1}{2}\sum_{i=0}^{n-1} dt \cdot B_{t_i}^2
\to \frac{1}{2}\int_0^1 B_s^2 \, ds
$$



**Third term (Itô integral in the limit)**:


$$
\sum_{i=0}^{n-1} dt \cdot B_{t_i}(B_{t_{i+1}} - B_{t_i})
= dt \cdot \sum_{i=0}^{n-1} B_{t_i}(B_{t_{i+1}} - B_{t_i})
$$



Since \(dt = 1/n \to 0\) and the sum is bounded, this term vanishes:


$$
\frac{1}{n} \sum_{i=0}^{n-1} B_{t_i}(B_{t_{i+1}} - B_{t_i})
\to 0
$$



**Fourth term (quadratic variation weighted by time)**:


$$
\frac{1}{2}\sum_{i=0}^{n-1} t_i (B_{t_{i+1}} - B_{t_i})^2
\to \frac{1}{2}\int_0^1 t \, d[B, B]_s
= \frac{1}{2}\int_0^1 t \, ds
= \frac{1}{4}
$$



The second part:


$$
\frac{1}{2}\sum_{i=0}^{n-1} dt \cdot (B_{t_{i+1}} - B_{t_i})^2
= \frac{dt}{2}\sum_{i=0}^{n-1} (B_{t_{i+1}} - B_{t_i})^2
\to 0 \cdot 1 = 0
$$



### Step 6: Final result

Combining all terms:


$$
\int_0^1 s B_s \, dB_s
= \frac{1}{2}B_1^2 - \frac{1}{2}\int_0^1 B_s^2 ds - \frac{1}{4}
$$




$$
\boxed{
\int_0^1 s B_s \, dB_s
= \frac{1}{2}B_1^2 - \frac{1}{2}\int_0^1 B_s^2 ds - \frac{1}{4}
}
$$



**Remarks**:
- This computation was **extremely tedious**
- We needed multiple clever decompositions
- The result involves another integral \(\int_0^1 B_s^2 ds\) that we cannot evaluate explicitly
- The calculation was error-prone with many terms to track

---

## Example 3: Attempting \(\int_0^1 B_s^2 \, dB_s\) directly

**Problem**: Try to compute \(\int_0^1 B_s^2 dB_s\) using the definition.

### The Riemann sum


$$
\int_0^1 B_s^2 \, dB_s
= \lim_{n \to \infty} \sum_{i=0}^{n-1} B_{t_i}^2 (B_{t_{i+1}} - B_{t_i})
$$



### Attempting the expansion

We would need to write:


$$
B_{t_i}^2 (B_{t_{i+1}} - B_{t_i})
= \text{???}
$$



in terms that telescope or converge to known limits.

One might try:


$$
B_{t_i}^2 (B_{t_{i+1}} - B_{t_i})
= \frac{1}{3}(B_{t_{i+1}}^3 - B_{t_i}^3) - \text{correction terms}
$$



But working out the correction terms becomes **prohibitively complex**. The direct computation quickly becomes intractable.

**Conclusion**: For polynomials of degree 2 and higher, direct computation from the definition is essentially impractical.

---

## The easy way: Using Itô's lemma

Now let's redo all three examples using **Itô's lemma** and see the dramatic simplification.

### Example 1 revisited: \(\int_0^1 B_s \, dB_s\)

**Apply Itô's lemma** to \(f(x) = x^2/2\):


$$
d\left(\frac{B_t^2}{2}\right)
= B_t \, dB_t + \frac{1}{2} \cdot 1 \, dt
$$



Integrating:


$$
\frac{B_1^2}{2} = \int_0^1 B_s \, dB_s + \frac{1}{2}
$$



Therefore:


$$
\int_0^1 B_s \, dB_s = \frac{B_1^2}{2} - \frac{1}{2}
$$



**Time required**: 30 seconds. No clever tricks needed.

### Example 2 revisited: \(\int_0^1 s B_s \, dB_s\)

**Method 1**: Integration by parts.

Since \(d(sB_s) = s \, dB_s + B_s \, ds\):


$$
1 \cdot B_1 - 0 = \int_0^1 s \, dB_s + \int_0^1 B_s \, ds
$$



Therefore:


$$
\int_0^1 s B_s \, dB_s = B_1 - \int_0^1 B_s \, ds
$$



Wait, this is for \(\int s dB_s\), not \(\int s B_s dB_s\).

**Method 2**: Use Itô's lemma on \(f(t, x) = tx^2/2\):


$$
\begin{align}
\frac{\partial f}{\partial t} &= \frac{x^2}{2}\\
\frac{\partial f}{\partial x} &= tx\\
\frac{\partial^2 f}{\partial x^2} &= t
\end{align}
$$



Itô's lemma:


$$
d\left(\frac{tB_t^2}{2}\right)
= \frac{B_t^2}{2} dt + tB_t \, dB_t + \frac{t}{2} dt
$$




$$
= tB_t \, dB_t + \frac{B_t^2 + t}{2} dt
$$



Integrating:


$$
\frac{B_1^2}{2} = \int_0^1 sB_s \, dB_s + \frac{1}{2}\int_0^1 (B_s^2 + s) ds
$$



Therefore:


$$
\int_0^1 sB_s \, dB_s
= \frac{B_1^2}{2} - \frac{1}{2}\int_0^1 B_s^2 ds - \frac{1}{4}
$$



**Time required**: 2 minutes. Straightforward application of Itô's lemma.

### Example 3 revisited: \(\int_0^1 B_s^2 \, dB_s\)

**Apply Itô's lemma** to \(f(x) = x^3/3\):


$$
d\left(\frac{B_t^3}{3}\right)
= B_t^2 \, dB_t + \frac{1}{2} \cdot 2B_t \, dt
= B_t^2 \, dB_t + B_t \, dt
$$



Integrating:


$$
\frac{B_1^3}{3} = \int_0^1 B_s^2 \, dB_s + \int_0^1 B_s \, ds
$$



Therefore:


$$
\int_0^1 B_s^2 \, dB_s
= \frac{B_1^3}{3} - \int_0^1 B_s \, ds
$$



**Time required**: 1 minute. Trivial application of Itô's lemma.

---

## Comparison table

| **Integral** | **Direct computation** | **Using Itô's lemma** |
|--------------|------------------------|------------------------|
| \(\int_0^1 B_s \, dB_s\) | ~5 minutes, requires tricks | 30 seconds |
| \(\int_0^1 s B_s \, dB_s\) | ~15 minutes, very tedious | 2 minutes |
| \(\int_0^1 B_s^2 \, dB_s\) | Essentially intractable | 1 minute |
| \(\int_0^1 B_s^n \, dB_s\) | Hopeless for \(n \ge 3\) | Apply to \(x^{n+1}/(n+1)\) |

---

## The analogy with classical calculus

**Riemann sums vs. Fundamental Theorem of Calculus**:

- **Hard way**: \(\int_0^1 x^2 dx = \lim_{n \to \infty} \sum_{i=1}^n (i/n)^2 \cdot (1/n)\) (painful)
- **Easy way**: \(\int_0^1 x^2 dx = [x^3/3]_0^1 = 1/3\) (trivial)

**Direct Itô integral vs. Itô's lemma**:

- **Hard way**: Manipulate Riemann sums, recognize quadratic variation, telescope carefully
- **Easy way**: Apply Itô's lemma to \(f(x)\), integrate, solve for the integral

**The lesson**: Just as the Fundamental Theorem of Calculus transforms integration from a computational nightmare into a simple lookup of antiderivatives, **Itô's lemma transforms stochastic integration from an intricate combinatorial exercise into a straightforward application of the chain rule**.

---

## Why does Itô's lemma work so well?

The power of Itô's lemma comes from the fact that:


$$
df(B_t) = f'(B_t) dB_t + \frac{1}{2}f''(B_t) dt
$$



This **relates integrals to known processes**. Instead of computing \(\int g(B_s) dB_s\) directly, we:

1. Find \(f\) such that \(f'(x) = g(x)\) (just like finding an antiderivative)
2. Apply Itô's lemma to get \(df(B_t) = g(B_t) dB_t + \text{(dt term)}\)
3. Integrate both sides
4. Solve for \(\int g(B_s) dB_s\)

The second-order term \(\frac{1}{2}f''(B_t) dt\) accounts for the quadratic variation automatically—we don't need to track it manually!

---

## Summary

**Computing Itô integrals directly**:
- Requires clever algebraic identities
- Involves careful tracking of quadratic variation
- Becomes intractable for complex integrands
- Is error-prone with many terms

**Computing Itô integrals with Itô's lemma**:
- Straightforward application of the chain rule
- Quadratic variation is handled automatically
- Works for arbitrary smooth functions
- Fast and reliable

**The bottom line**: **Itô's lemma is to stochastic calculus what the Fundamental Theorem of Calculus is to ordinary calculus**—it transforms a computational burden into a simple, systematic procedure.

This is why Itô's lemma is called the **fundamental theorem of stochastic calculus**.
