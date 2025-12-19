# Itô Integration by Parts

The **integration by parts formula** is one of the fundamental computational tools in calculus. In stochastic calculus, integration by parts takes a modified form that includes an additional term arising from the quadratic variation of Brownian motion. This formula is essential for computing products of Itô processes and plays a central role in applications ranging from option pricing to filtering theory.

---

## Classical integration by parts (review)

In ordinary calculus, for differentiable functions \(f(t)\) and \(g(t)\):



$$
\int_0^t f(s) \, dg(s)
= f(t) g(t) - f(0) g(0) - \int_0^t g(s) \, df(s)
$$





Or in differential notation:



$$
d(f(t) g(t)) = f(t) \, dg(t) + g(t) \, df(t)
$$





This formula expresses the relationship between the product \(f \cdot g\) and the integrals of \(f \, dg\) and \(g \, df\).

---

## Stochastic integration by parts

For Itô processes \(X_t\) and \(Y_t\), the integration by parts formula includes an **additional term** involving their quadratic covariation:



$$
\boxed{
d(X_t Y_t) = X_t \, dY_t + Y_t \, dX_t + d[X, Y]_t
}
$$





In integral form:



$$
\boxed{
X_t Y_t = X_0 Y_0 + \int_0^t X_s \, dY_s + \int_0^t Y_s \, dX_s + [X, Y]_t
}
$$





The term \(d[X, Y]_t\) is the **differential of the quadratic covariation** and represents the "second-order interaction" between \(X\) and \(Y\).

**Comparison with classical formula**: The additional term \(d[X, Y]_t\) is absent in ordinary calculus because quadratic variation vanishes for smooth functions. In stochastic calculus, this term is **non-negligible** due to the unbounded variation of Brownian motion.

---

## Quadratic covariation review

For two Itô processes:



$$
\begin{align}
dX_t &= \mu_t^X \, dt + \sigma_t^X \, dB_t\\
dY_t &= \mu_t^Y \, dt + \sigma_t^Y \, dB_t
\end{align}
$$





their **quadratic covariation** is:



$$
d[X, Y]_t = \sigma_t^X \sigma_t^Y \, dt
$$





In integral form:



$$
[X, Y]_t = \int_0^t \sigma_s^X \sigma_s^Y \, ds
$$





**Key rules** (informal multiplication table):



$$
\begin{array}{c|ccc}
\cdot & dt & dB_t \\
\hline
dt & 0 & 0 \\
dB_t & 0 & dt
\end{array}
$$





From these rules:
- \(dt \cdot dt = 0\) (negligible)
- \(dt \cdot dB_t = 0\) (negligible)
- \(dB_t \cdot dB_t = dt\) (non-negligible!)

---

## Derivation from Itô's product rule

The integration by parts formula is a direct consequence of **Itô's product rule**.

**Setup**: Let \(X_t\) and \(Y_t\) be Itô processes. Define \(Z_t = X_t Y_t\).

**Goal**: Compute \(dZ_t\) using Itô's lemma for \(f(x, y) = xy\).

**Calculation**: The partial derivatives are:



$$
\frac{\partial f}{\partial x} = y, \quad
\frac{\partial f}{\partial y} = x, \quad
\frac{\partial^2 f}{\partial x \partial y} = 1, \quad
\frac{\partial^2 f}{\partial x^2} = \frac{\partial^2 f}{\partial y^2} = 0
$$





Applying Itô's lemma:



$$
df(X_t, Y_t)
= \frac{\partial f}{\partial x} dX_t + \frac{\partial f}{\partial y} dY_t
+ \frac{1}{2} \frac{\partial^2 f}{\partial x^2} (dX_t)^2
+ \frac{1}{2} \frac{\partial^2 f}{\partial y^2} (dY_t)^2
+ \frac{\partial^2 f}{\partial x \partial y} dX_t \, dY_t
$$





Substituting the derivatives:



$$
d(X_t Y_t)
= Y_t \, dX_t + X_t \, dY_t
+ 0 \cdot (dX_t)^2 + 0 \cdot (dY_t)^2 + 1 \cdot dX_t \, dY_t
$$





Since \(dX_t \, dY_t = d[X, Y]_t\):



$$
\boxed{
d(X_t Y_t) = Y_t \, dX_t + X_t \, dY_t + d[X, Y]_t
}
$$





This is the **stochastic integration by parts formula**. \(\square\)

---

## Special cases

### Case 1: Both processes are martingales

If \(X_t\) and \(Y_t\) are martingales driven by the same Brownian motion:



$$
dX_t = \sigma_t^X \, dB_t, \quad
dY_t = \sigma_t^Y \, dB_t
$$





Then:



$$
d(X_t Y_t) = X_t \, dY_t + Y_t \, dX_t + \sigma_t^X \sigma_t^Y \, dt
$$





Integrating:



$$
X_t Y_t = X_0 Y_0 + \int_0^t X_s \, dY_s + \int_0^t Y_s \, dX_s + \int_0^t \sigma_s^X \sigma_s^Y \, ds
$$





**Example**: For \(X_t = Y_t = B_t\) (with \(\sigma = 1\)):



$$
B_t^2 = \int_0^t B_s \, dB_s + \int_0^t B_s \, dB_s + \int_0^t 1 \, ds
= 2 \int_0^t B_s \, dB_s + t
$$





Solving for the Itô integral:



$$
\int_0^t B_s \, dB_s = \frac{B_t^2 - t}{2}
$$





This recovers the classic result.

### Case 2: One deterministic, one stochastic

If \(X_t = t\) (deterministic) and \(Y_t\) is an Itô process:



$$
dX_t = dt, \quad
dY_t = \mu_t \, dt + \sigma_t \, dB_t
$$





Then \(d[X, Y]_t = 0\) (no quadratic covariation with deterministic processes):



$$
d(t \cdot Y_t) = t \, dY_t + Y_t \, dt
$$





This is the **classical integration by parts** formula—no correction term needed when one process is deterministic.

### Case 3: Independent Brownian motions

If \(X_t\) and \(Y_t\) are driven by **independent** Brownian motions \(B_t^{(1)}\) and \(B_t^{(2)}\):



$$
dX_t = \sigma_t^X \, dB_t^{(1)}, \quad
dY_t = \sigma_t^Y \, dB_t^{(2)}
$$





Then \(d[X, Y]_t = 0\) (independent Brownian motions have zero cross-variation):



$$
d(X_t Y_t) = X_t \, dY_t + Y_t \, dX_t
$$





Again, no correction term.

---

## Worked examples

### Example 1: Computing \(\int_0^t s \, dB_s\)

**Goal**: Evaluate \(\int_0^t s \, dB_s\) using integration by parts.

**Setup**: Let \(X_t = t\) and \(Y_t = B_t\). We want to compute \(\int_0^t X_s dY_s\).

**Integration by parts**:



$$
X_t Y_t = X_0 Y_0 + \int_0^t X_s \, dY_s + \int_0^t Y_s \, dX_s + [X, Y]_t
$$





Since \(X_t = t\) is deterministic, \([X, Y]_t = 0\):



$$
t B_t = 0 + \int_0^t s \, dB_s + \int_0^t B_s \, ds
$$





Solving for the Itô integral:



$$
\boxed{
\int_0^t s \, dB_s = t B_t - \int_0^t B_s \, ds
}
$$





**Interpretation**: This expresses the stochastic integral in terms of an ordinary integral. The result is a **continuous martingale** (since the ordinary integral \(\int B_s ds\) is adapted and continuous).

### Example 2: Computing \(\int_0^t e^{B_s} \, dB_s\)

**Goal**: Evaluate \(\int_0^t e^{B_s} dB_s\).

**Setup**: Let \(f(x) = e^x\). By Itô's lemma:



$$
d(e^{B_t}) = e^{B_t} dB_t + \frac{1}{2} e^{B_t} dt
$$





Rearranging:



$$
e^{B_t} dB_t = d(e^{B_t}) - \frac{1}{2} e^{B_t} dt
$$





Integrating:



$$
\int_0^t e^{B_s} dB_s = e^{B_t} - 1 - \frac{1}{2} \int_0^t e^{B_s} ds
$$





**Note**: This is not a closed-form solution (the ordinary integral \(\int e^{B_s} ds\) has no explicit form), but it relates the stochastic integral to a deterministic integral.

### Example 3: \(\int_0^t B_s^2 \, dB_s\)

**Goal**: Compute \(\int_0^t B_s^2 dB_s\).

**Method 1 (Direct Itô's lemma)**: Let \(f(x) = x^3/3\). Then:



$$
d\left(\frac{B_t^3}{3}\right) = B_t^2 dB_t + \frac{1}{2} \cdot 2B_t \, dt = B_t^2 dB_t + B_t \, dt
$$





Rearranging:



$$
B_t^2 dB_t = d\left(\frac{B_t^3}{3}\right) - B_t \, dt
$$





Integrating:



$$
\boxed{
\int_0^t B_s^2 \, dB_s = \frac{B_t^3}{3} - \int_0^t B_s \, ds
}
$$





**Method 2 (Integration by parts)**: Let \(X_t = B_t\) and \(Y_t = B_t^2 - t\) (a martingale). Then:



$$
dX_t = dB_t, \quad
dY_t = 2B_t dB_t
$$





Integration by parts:



$$
X_t Y_t = \int_0^t X_s dY_s + \int_0^t Y_s dX_s + [X, Y]_t
$$





This gives:



$$
B_t(B_t^2 - t) = \int_0^t B_s \cdot 2B_s dB_s + \int_0^t (B_s^2 - s) dB_s + \int_0^t 2B_s \, ds
$$





Simplifying yields the same result.

---

## Application: Solving linear SDEs

Integration by parts is instrumental in solving **linear stochastic differential equations**.

### Example: Ornstein-Uhlenbeck process

Consider the SDE:



$$
dX_t = -\theta X_t \, dt + \sigma \, dB_t, \quad X_0 = x_0
$$





**Solution strategy**: Use an **integrating factor** \(e^{\theta t}\).

**Step 1**: Multiply both sides by \(e^{\theta t}\):



$$
e^{\theta t} dX_t = -\theta e^{\theta t} X_t \, dt + \sigma e^{\theta t} dB_t
$$





**Step 2**: Recognize the left side as a differential. Let \(Y_t = e^{\theta t} X_t\). By integration by parts:



$$
dY_t = d(e^{\theta t} X_t)
= e^{\theta t} dX_t + X_t d(e^{\theta t}) + d[e^{\theta t}, X_t]
$$





Since \(e^{\theta t}\) is deterministic, \(d[e^{\theta t}, X_t] = 0\):



$$
dY_t = e^{\theta t} dX_t + \theta e^{\theta t} X_t \, dt
$$





**Step 3**: Substitute \(dX_t\):



$$
dY_t = e^{\theta t}(-\theta X_t dt + \sigma dB_t) + \theta e^{\theta t} X_t dt
= \sigma e^{\theta t} dB_t
$$





**Step 4**: Integrate:



$$
Y_t = Y_0 + \sigma \int_0^t e^{\theta s} dB_s
$$





**Step 5**: Substitute back \(Y_t = e^{\theta t} X_t\):



$$
e^{\theta t} X_t = x_0 + \sigma \int_0^t e^{\theta s} dB_s
$$





**Solution**:



$$
\boxed{
X_t = e^{-\theta t} x_0 + \sigma e^{-\theta t} \int_0^t e^{\theta s} dB_s
}
$$





This is the **explicit solution** to the Ornstein-Uhlenbeck SDE, obtained via integration by parts.

---

## General formula for product of Itô integrals

Let \(I_t^{(1)} = \int_0^t H_s^{(1)} dB_s^{(1)}\) and \(I_t^{(2)} = \int_0^t H_s^{(2)} dB_s^{(2)}\) be Itô integrals (possibly with different Brownian motions). Then:



$$
I_t^{(1)} I_t^{(2)}
= \int_0^t I_s^{(1)} dI_s^{(2)} + \int_0^t I_s^{(2)} dI_s^{(1)} + [I^{(1)}, I^{(2)}]_t
$$





If \(B_s^{(1)} = B_s^{(2)} = B_s\) (same Brownian motion):



$$
[I^{(1)}, I^{(2)}]_t = \int_0^t H_s^{(1)} H_s^{(2)} \, ds
$$





If \(B_s^{(1)} \perp B_s^{(2)}\) (independent):



$$
[I^{(1)}, I^{(2)}]_t = 0
$$





This formula generalizes integration by parts to arbitrary Itô integrals.

---

## Connection to Itô's product rule

The integration by parts formula is equivalent to **Itô's product rule**:



$$
d(X_t Y_t) = X_t dY_t + Y_t dX_t + dX_t \, dY_t
$$





where \(dX_t \, dY_t\) denotes the quadratic covariation:



$$
dX_t \, dY_t = d[X, Y]_t
$$





**Why is this different from classical calculus?** In ordinary calculus, \(dx \, dy = 0\) (products of differentials vanish). In stochastic calculus, \(dB_t \, dB_t = dt\) is **non-zero**, leading to the additional term.

---

## Summary

The **stochastic integration by parts formula** is:



$$
\boxed{
d(X_t Y_t) = X_t dY_t + Y_t dX_t + d[X, Y]_t
}
$$





**Key points**:

1. **Additional term**: \(d[X, Y]_t = \sigma_t^X \sigma_t^Y dt\) arises from quadratic covariation

2. **Vanishes for deterministic processes**: If \(X_t\) or \(Y_t\) is deterministic, \(d[X, Y]_t = 0\)

3. **Vanishes for independent Brownian motions**: If \(X\) and \(Y\) are driven by independent BMs, \(d[X, Y]_t = 0\)

4. **Applications**:
   - Computing Itô integrals (e.g., \(\int s dB_s = tB_t - \int B_s ds\))
   - Solving linear SDEs (e.g., Ornstein-Uhlenbeck)
   - Expressing products of martingales
   - Change of numeraire in finance

5. **Relation to Itô's product rule**: Direct consequence of applying Itô's lemma to \(f(x, y) = xy\)

**Next**: In the Itô Quotient Rule section, we extend this technique to ratios \(X_t / Y_t\), and in Applications and Examples, we showcase the power of these computational tools across a range of problems.
