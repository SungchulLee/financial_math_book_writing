# Applications and Examples of Itô Calculus

Having developed the machinery of Itô's lemma, the product rule, integration by parts, and the quotient rule, we now showcase these tools through a comprehensive collection of applications. This section demonstrates the computational power of Itô calculus and connects to the martingale theory developed in Section 1.2.

---

## Example 1: Computing \(\int_0^t B_s \, dB_s\)

**Problem**: Evaluate \(\int_0^t B_s dB_s\).

**Method**: Apply Itô's lemma to \(f(x) = x^2/2\).

**Solution**: 

The partial derivatives are:


$$
f'(x) = x, \quad f''(x) = 1
$$



Itô's lemma gives:


$$
df(B_t) = f'(B_t) dB_t + \frac{1}{2} f''(B_t) (dB_t)^2
= B_t dB_t + \frac{1}{2} dt
$$



Therefore:


$$
d\left(\frac{B_t^2}{2}\right) = B_t dB_t + \frac{1}{2} dt
$$



Integrating from \(0\) to \(t\):


$$
\frac{B_t^2}{2} - 0 = \int_0^t B_s dB_s + \frac{1}{2} \int_0^t ds
$$




$$
\boxed{
\int_0^t B_s \, dB_s = \frac{B_t^2 - t}{2}
}
$$



**Verification**: This matches the result from Section 1.2—the process \(B_t^2 - t\) is a martingale, and we've shown it can be written as a pure Itô integral:


$$
B_t^2 - t = 2 \int_0^t B_s dB_s
$$



---

## Example 2: Computing \(\int_0^t B_s^2 \, dB_s\)

**Problem**: Evaluate \(\int_0^t B_s^2 dB_s\).

**Method**: Apply Itô's lemma to \(f(x) = x^3/3\).

**Solution**:


$$
f'(x) = x^2, \quad f''(x) = 2x
$$



Itô's lemma:


$$
d\left(\frac{B_t^3}{3}\right) = B_t^2 dB_t + \frac{1}{2} \cdot 2B_t \, dt
= B_t^2 dB_t + B_t \, dt
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



**Connection to martingales**: Recall from Section 1.2 that \(B_t^3 - 3tB_t\) is a martingale. We can verify:


$$
B_t^3 - 3tB_t = 3\int_0^t B_s^2 dB_s + 3\int_0^t B_s ds - 3tB_t
= 3\int_0^t B_s^2 dB_s
$$



using integration by parts on \(\int_0^t B_s ds\).

---

## Example 3: Deriving the exponential martingale

**Problem**: Show that \(Z_t = \exp(\theta B_t - \frac{1}{2}\theta^2 t)\) is a martingale.

**Method**: Apply Itô's lemma to verify \(dZ_t\) has no \(dt\) term.

**Solution**:

Let \(f(t, x) = \exp(\theta x - \frac{1}{2}\theta^2 t)\). The partial derivatives are:


$$
\frac{\partial f}{\partial t} = -\frac{1}{2}\theta^2 f, \quad
\frac{\partial f}{\partial x} = \theta f, \quad
\frac{\partial^2 f}{\partial x^2} = \theta^2 f
$$



Applying Itô's lemma:


$$
dZ_t = \frac{\partial f}{\partial t} dt + \frac{\partial f}{\partial x} dB_t + \frac{1}{2} \frac{\partial^2 f}{\partial x^2} dt
$$




$$
= -\frac{1}{2}\theta^2 Z_t \, dt + \theta Z_t \, dB_t + \frac{1}{2} \theta^2 Z_t \, dt
$$




$$
= \theta Z_t \, dB_t
$$



The \(dt\) terms cancel! Therefore:


$$
Z_t = Z_0 + \int_0^t \theta Z_s dB_s
$$



Since \(Z_0 = 1\) and the integral is a martingale:


$$
\boxed{
Z_t = \exp\left(\theta B_t - \frac{1}{2}\theta^2 t\right) \text{ is a martingale}
}
$$



**Applications**:

- **Girsanov's theorem**: \(Z_t\) is the Radon-Nikodym derivative for measure change
- **Risk-neutral pricing**: Used to transform from physical to risk-neutral measure
- **Cameron-Martin formula**: Shift the drift of Brownian motion

---

## Example 4: Geometric Brownian motion

**Problem**: Solve the SDE:


$$
dS_t = \mu S_t \, dt + \sigma S_t \, dB_t, \quad S_0 = s_0
$$



**Method**: Guess \(S_t = s_0 e^{X_t}\) and find \(X_t\) using Itô's lemma.

**Solution**:

Let \(f(x) = s_0 e^x\). Then:


$$
f'(x) = s_0 e^x, \quad f''(x) = s_0 e^x
$$



If \(S_t = f(X_t)\), then by Itô's lemma:


$$
dS_t = f'(X_t) dX_t + \frac{1}{2} f''(X_t) (dX_t)^2
$$



Suppose \(dX_t = \alpha dt + \beta dB_t\) (to be determined). Then \((dX_t)^2 = \beta^2 dt\), so:


$$
dS_t = S_t (\alpha dt + \beta dB_t) + \frac{1}{2} S_t \beta^2 dt
= S_t \left(\alpha + \frac{1}{2}\beta^2\right) dt + S_t \beta dB_t
$$



Matching coefficients with \(dS_t = \mu S_t dt + \sigma S_t dB_t\):


$$
\beta = \sigma, \quad
\alpha + \frac{1}{2}\sigma^2 = \mu
$$



Therefore:


$$
dX_t = \left(\mu - \frac{1}{2}\sigma^2\right) dt + \sigma dB_t
$$



Integrating:


$$
X_t = X_0 + \left(\mu - \frac{1}{2}\sigma^2\right) t + \sigma B_t
$$



**Solution**:


$$
\boxed{
S_t = s_0 \exp\left(\left(\mu - \frac{1}{2}\sigma^2\right) t + \sigma B_t\right)
}
$$



**Key observations**:

- The \(-\frac{1}{2}\sigma^2 t\) term is the **Itô correction** arising from \((dB_t)^2 = dt\)
- \(\mathbb{E}[S_t] = s_0 e^{\mu t}\) (exponential growth at rate \(\mu\))
- \(S_t\) is **log-normally distributed**: \(\log S_t \sim N(\log s_0 + (\mu - \frac{1}{2}\sigma^2)t, \sigma^2 t)\)
- This is the foundation of the **Black-Scholes model** in finance

---

## Example 5: Computing \(\int_0^t e^{B_s} \, dB_s\)

**Problem**: Relate \(\int_0^t e^{B_s} dB_s\) to ordinary integrals.

**Method**: Apply Itô's lemma to \(f(x) = e^x\).

**Solution**:


$$
f'(x) = e^x, \quad f''(x) = e^x
$$



Itô's lemma:


$$
d(e^{B_t}) = e^{B_t} dB_t + \frac{1}{2} e^{B_t} dt
$$



Rearranging:


$$
e^{B_t} dB_t = d(e^{B_t}) - \frac{1}{2} e^{B_t} dt
$$



Integrating:


$$
\boxed{
\int_0^t e^{B_s} dB_s = e^{B_t} - 1 - \frac{1}{2} \int_0^t e^{B_s} ds
}
$$



**Note**: The ordinary integral \(\int_0^t e^{B_s} ds\) has no closed form, but this relation is still useful in theoretical work and numerical methods.

---

## Example 6: Reciprocal of Brownian motion

**Problem**: Let \(Y_t = 1/B_t\) (assuming \(B_t > 0\)). Find \(dY_t\).

**Method**: Apply Itô's lemma to \(f(x) = 1/x\).

**Solution**:


$$
f'(x) = -\frac{1}{x^2}, \quad f''(x) = \frac{2}{x^3}
$$



Itô's lemma:


$$
dY_t = -\frac{1}{B_t^2} dB_t + \frac{1}{2} \cdot \frac{2}{B_t^3} dt
= -\frac{1}{B_t^2} dB_t + \frac{1}{B_t^3} dt
$$




$$
\boxed{
d\left(\frac{1}{B_t}\right) = \frac{1}{B_t^3} dt - \frac{1}{B_t^2} dB_t
}
$$



**Observation**: The drift term \(\frac{1}{B_t^3}\) explodes as \(B_t \to 0\), reflecting the singularity of the reciprocal function.

---

## Example 7: Brownian bridge via change of measure

**Problem**: Show that \(X_t = B_t - \frac{t}{T} B_T\) is a Brownian bridge (conditioned to end at 0 at time \(T\)).

**Method**: Compute \(dX_t\) using differentiation rules.

**Solution**:

Since \(B_T\) is \(\mathcal{F}_T\)-measurable (a "future" random variable from the perspective of time \(t < T\)):


$$
dX_t = dB_t - \frac{1}{T} B_T \, dt
$$



For \(t < T\), \(B_T\) acts as a constant. Therefore:


$$
\boxed{
dX_t = dB_t - \frac{B_T}{T} dt
}
$$



**Interpretation**: This is a Brownian motion with time-dependent drift pulling it toward 0 at time \(T\).

**Verification of endpoint**: At \(t = T\):


$$
X_T = B_T - \frac{T}{T} B_T = 0
$$



So \(X_t\) is "pinned" at 0 at time \(T\).

---

## Example 8: Bessel process

**Problem**: Let \(R_t = |B_t|\) be the absolute value of Brownian motion. Find the SDE satisfied by \(R_t\) (away from 0).

**Method**: Apply Itô's lemma to \(f(x) = |x|\), which is problematic at 0. Instead, use \(f(x) = \sqrt{x^2}\).

**Solution**:

For \(R_t^2 = B_t^2\), we have by Itô's lemma:


$$
d(R_t^2) = 2B_t dB_t + dt
$$



Using the relation \(d(R_t^2) = 2R_t dR_t + (dR_t)^2\), we get (formally):


$$
2R_t dR_t = 2B_t dB_t + dt - (dR_t)^2
$$



Since \(B_t = \pm R_t\) and assuming \((dR_t)^2 \approx 0\) for heuristic purposes:


$$
dR_t \approx \frac{1}{R_t} \frac{dt}{2} + \text{sgn}(B_t) dB_t
$$



**More carefully**: The rigorous derivation gives:


$$
\boxed{
dR_t = \frac{dt}{2R_t} + \text{sgn}(B_t) dB_t
}
$$



for \(R_t > 0\). This is the **1-dimensional Bessel process**.

**Note**: The drift term \(\frac{1}{2R_t}\) pushes the process away from 0, explaining why \(|B_t|\) spends little time near 0.

---

## Example 9: Deriving all polynomial martingales

**Problem**: Systematically derive all polynomial martingales \(B_t^n - c_n(t)\).

**Method**: Use Itô's lemma on \(f(x) = x^n\).

**General formula**:

For \(f(x) = x^n\):


$$
f'(x) = nx^{n-1}, \quad f''(x) = n(n-1)x^{n-2}
$$



Itô's lemma:


$$
d(B_t^n) = nB_t^{n-1} dB_t + \frac{1}{2} n(n-1) B_t^{n-2} dt
$$



For \(B_t^n - c_n(t)\) to be a martingale, the \(dt\) term must vanish after subtracting \(dc_n\):


$$
\frac{1}{2} n(n-1) B_t^{n-2} dt - c_n'(t) dt = 0
$$



Therefore:


$$
c_n'(t) = \frac{1}{2} n(n-1) B_t^{n-2}
$$



This requires \(c_n(t)\) to depend on \(B_t\), which contradicts the martingale property unless we integrate properly.

**Correct approach**: For specific \(n\):

- \(n=2\): \(d(B_t^2) = 2B_t dB_t + dt \Rightarrow B_t^2 - t\) is a martingale
- \(n=3\): \(d(B_t^3) = 3B_t^2 dB_t + 3B_t dt \Rightarrow d(B_t^3 - 3tB_t) = 3B_t^2 dB_t\)
- \(n=4\): \(d(B_t^4) = 4B_t^3 dB_t + 6B_t^2 dt \Rightarrow B_t^4 - 6tB_t^2 + 3t^2\) is a martingale

The pattern continues via **Hermite polynomials**.

---

## Example 10: Lévy's characterization of Brownian motion

**Problem**: Show that if \(M_t\) is a continuous martingale with \([M, M]_t = t\), then \(M_t\) is a Brownian motion.

**Method**: Use Itô's lemma to show \(\exp(iuM_t + \frac{1}{2}u^2 t)\) is a martingale, implying \(M_t \sim N(0, t)\).

**Solution**:

Let \(f(x) = e^{iux}\) and \(Z_t = f(M_t) \cdot e^{\frac{1}{2}u^2 t}\). We compute:


$$
df(M_t) = iue^{iuM_t} dM_t + \frac{1}{2}(iu)^2 e^{iuM_t} d[M, M]_t
= iue^{iuM_t} dM_t - \frac{1}{2}u^2 e^{iuM_t} dt
$$



since \([M, M]_t = t\) implies \(d[M, M]_t = dt\).

For \(Z_t\):


$$
dZ_t = d(e^{iuM_t} e^{\frac{1}{2}u^2 t})
= e^{\frac{1}{2}u^2 t} df(M_t) + e^{iuM_t} d(e^{\frac{1}{2}u^2 t})
$$




$$
= e^{\frac{1}{2}u^2 t} \left(iue^{iuM_t} dM_t - \frac{1}{2}u^2 e^{iuM_t} dt\right) + e^{iuM_t} \frac{1}{2}u^2 e^{\frac{1}{2}u^2 t} dt
$$




$$
= Z_t (iu dM_t)
$$



The \(dt\) terms cancel! Therefore \(Z_t\) is a martingale:


$$
\mathbb{E}[e^{iuM_t + \frac{1}{2}u^2 t} \mid \mathcal{F}_0] = e^{0} = 1
$$



This means:


$$
\mathbb{E}[e^{iuM_t}] = e^{-\frac{1}{2}u^2 t}
$$



This is the **characteristic function of \(N(0, t)\)**. Combined with continuity and the martingale property, this proves \(M_t\) is a Brownian motion.


$$
\boxed{
\text{Lévy's theorem: } M_t \text{ continuous martingale with } [M, M]_t = t \Rightarrow M_t \text{ is Brownian motion}
}
$$



---

## Example 11: Tanaka's formula (local time)

**Problem**: Compute \(d|B_t|\) for Brownian motion.

**Issue**: The function \(f(x) = |x|\) is not differentiable at 0, so Itô's lemma doesn't directly apply.

**Resolution**: Use **Tanaka's formula**:


$$
\boxed{
|B_t| = \int_0^t \text{sgn}(B_s) dB_s + L_t
}
$$



where \(L_t\) is the **local time** of Brownian motion at 0:


$$
L_t = \lim_{\varepsilon \to 0} \frac{1}{2\varepsilon} \int_0^t \mathbf{1}_{|B_s| < \varepsilon} ds
$$



**Interpretation**: \(L_t\) measures the "amount of time" Brownian motion spends near 0. It increases only when \(B_t = 0\).

**Differential form**:


$$
d|B_t| = \text{sgn}(B_t) dB_t + dL_t
$$



This is the correct generalization of Itô's lemma to non-smooth functions.

---

## Example 12: Stratonovich integral vs. Itô integral

**Problem**: Show that the Stratonovich integral satisfies the classical chain rule.

**Definition**: The **Stratonovich integral** is defined as:


$$
\int_0^t H_s \circ dB_s
:= \lim \sum_i \frac{H_{t_i} + H_{t_{i+1}}}{2} (B_{t_{i+1}} - B_{t_i})
$$



(midpoint evaluation, not left-endpoint).

**Relation to Itô integral**:


$$
\int_0^t H_s \circ dB_s
= \int_0^t H_s dB_s + \frac{1}{2} [H, B]_t
$$



**Chain rule**: For \(Y_t = f(B_t)\):


$$
dY_t = f'(B_t) \circ dB_t
$$



(No second-order term! This looks like the classical chain rule.)

**Why Itô is preferred**: Despite the simpler chain rule, the **Itô integral is a martingale**, while the Stratonovich integral generally is not. This makes Itô calculus more natural for probability theory and finance.

---

## Summary of applications

Itô calculus enables:

1. **Computing stochastic integrals**: \(\int B_s dB_s\), \(\int B_s^2 dB_s\), etc.

2. **Deriving martingales**: Polynomial and exponential martingales from Section 1.2

3. **Solving SDEs**: Geometric Brownian motion, Ornstein-Uhlenbeck, linear SDEs

4. **Change of variables**: Transforming processes via nonlinear functions

5. **Characterization theorems**: Lévy's characterization of Brownian motion

6. **Risk-neutral pricing**: Exponential martingale for measure change (Girsanov)

7. **Numerical methods**: Euler-Maruyama, Milstein schemes for SDE simulation

8. **Option pricing**: Black-Scholes formula, Greeks, hedging strategies

The tools developed in this chapter—Itô's lemma, product rule, integration by parts, and quotient rule—form the **computational backbone** of continuous-time stochastic processes and financial mathematics.

**Next**: In Chapter 2, we develop the theory of **stochastic differential equations** (SDEs), where the drift and diffusion coefficients depend on the unknown process itself, requiring existence and uniqueness theorems.
