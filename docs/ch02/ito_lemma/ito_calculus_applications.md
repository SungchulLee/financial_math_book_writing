# Applications and Examples of Itô Calculus

Having developed the machinery of Itô's lemma, the product rule, integration by parts, and the quotient rule, we now showcase these tools through a comprehensive collection of applications. This section demonstrates the computational power of Itô calculus and connects to the martingale theory developed earlier.

---

## Example 1: Computing \( \int_0^t B_s \, dB_s \)

**Problem**: Evaluate \( \int_0^t B_s \, dB_s \).

**Method**: Apply Itô's lemma to \( f(x) = x^2 / 2 \).

**Solution**:


\[
f'(x) = x, \qquad f''(x) = 1
\]



Itô's lemma gives:


\[
df(B_t) = B_t \, dB_t + \frac{1}{2} \, dt
\]



Hence,


\[
d\!\left(\frac{B_t^2}{2}\right) = B_t \, dB_t + \frac{1}{2} \, dt
\]



Integrating from \(0\) to \(t\):


\[
\frac{B_t^2}{2}
= \int_0^t B_s \, dB_s + \frac{1}{2} t
\]



Therefore,


\[
\boxed{
\int_0^t B_s \, dB_s = \frac{B_t^2 - t}{2}
}
\]



This confirms that \( B_t^2 - t \) is a martingale.

---

## Example 2: Computing \( \int_0^t s \, dB_s \)

**Problem**: Evaluate the Itô integral

\[
\int_0^t s \, dB_s.
\]



**Solution**:

The integrand \( s \) is deterministic and square-integrable on \( [0,t] \), so the integral is a martingale and


\[
\mathbb{E}\left[\int_0^t s \, dB_s\right] = 0.
\]



By the Itô isometry,


\[
\mathbb{E}\left[\left(\int_0^t s \, dB_s\right)^2\right]
= \int_0^t s^2 \, ds
= \frac{t^3}{3}.
\]



Hence,


\[
\boxed{
\int_0^t s \, dB_s \sim \mathcal{N}\!\left(0, \frac{t^3}{3}\right)
}
\]



This example illustrates how deterministic time-dependent integrands lead to explicit Gaussian distributions.

---

## Example 3: Computing \( \int_0^t s B_s \, dB_s \)

**Problem**: Simplify

\[
\int_0^t s B_s \, dB_s.
\]



**Method**: Apply Itô’s formula to a time-dependent function.

**Solution**:

Consider

\[
f(t,x) = \frac{1}{2} t x^2.
\]



Its derivatives are:


\[
\frac{\partial f}{\partial t} = \frac{1}{2} x^2,
\quad
\frac{\partial f}{\partial x} = t x,
\quad
\frac{\partial^2 f}{\partial x^2} = t.
\]



By Itô’s formula,


\[
df(t,B_t)
= \frac{1}{2} B_t^2 \, dt
+ t B_t \, dB_t
+ \frac{1}{2} t \, dt.
\]



Rearranging,


\[
t B_t \, dB_t
= d\!\left(\frac{1}{2} t B_t^2\right)
- \frac{1}{2} B_t^2 \, dt
- \frac{1}{2} t \, dt.
\]



Integrating from \(0\) to \(t\):


\[
\boxed{
\int_0^t s B_s \, dB_s
= \frac{1}{2} t B_t^2
- \frac{1}{2} \int_0^t B_s^2 \, ds
- \frac{1}{4} t^2
}
\]



This example shows how **time dependence in the integrand** introduces additional drift terms.

---

## Example 4: Computing \( \int_0^t B_s^2 \, dB_s \)

**Problem**: Evaluate \( \int_0^t B_s^2 \, dB_s \).

**Method**: Apply Itô's lemma to \( f(x) = x^3 / 3 \).

**Solution**:


\[
f'(x) = x^2, \qquad f''(x) = 2x
\]



Itô's lemma:


\[
d\!\left(\frac{B_t^3}{3}\right)
= B_t^2 \, dB_t + B_t \, dt
\]



Thus,


\[
\boxed{
\int_0^t B_s^2 \, dB_s
= \frac{B_t^3}{3} - \int_0^t B_s \, ds
}
\]



---

## Example 5: Deriving the Exponential Martingale

**Problem**: Show that

\[
Z_t = \exp\!\left(\theta B_t - \frac{1}{2}\theta^2 t\right)
\]


is a martingale.

**Solution**:

Applying Itô’s lemma yields


\[
dZ_t = \theta Z_t \, dB_t,
\]



with no drift term. Hence,


\[
\boxed{
Z_t \text{ is a martingale}
}
\]



This process is fundamental in **Girsanov’s theorem** and **risk-neutral pricing**.

---

## Example 6: Geometric Brownian Motion

**Problem**: Solve the SDE

\[
dS_t = \mu S_t \, dt + \sigma S_t \, dB_t, \qquad S_0 = s_0.
\]



**Solution**:


\[
\boxed{
S_t = s_0 \exp\!\left(
\left(\mu - \frac{1}{2}\sigma^2\right)t + \sigma B_t
\right)
}
\]



This is the cornerstone of the **Black–Scholes model**.

---

## Example 7: Computing \( \int_0^t e^{B_s} \, dB_s \)

**Problem**: Relate \( \int_0^t e^{B_s} \, dB_s \) to ordinary integrals.

**Solution**:


\[
\boxed{
\int_0^t e^{B_s} \, dB_s
= e^{B_t} - 1 - \frac{1}{2} \int_0^t e^{B_s} \, ds
}
\]



---

## Example 8: Reciprocal of Brownian Motion

**Problem**: Let \( Y_t = 1 / B_t \) (assuming \( B_t > 0 \)). Find \( dY_t \).

**Solution**:


\[
\boxed{
d\!\left(\frac{1}{B_t}\right)
= \frac{1}{B_t^3} \, dt - \frac{1}{B_t^2} \, dB_t
}
\]



---

## Example 9: Brownian Bridge

**Problem**: Show that

\[
X_t = B_t - \frac{t}{T} B_T
\]


is a Brownian bridge.

**Solution**:


\[
\boxed{
dX_t = dB_t - \frac{B_T}{T} \, dt
}
\quad\text{and}\quad X_T = 0.
\]



---

## Summary

These examples demonstrate how Itô calculus enables:

- Explicit evaluation of stochastic integrals
- Construction of martingales
- Solution of stochastic differential equations
- Precise handling of time-dependent randomness

Together, they form the computational backbone of continuous-time stochastic analysis.
