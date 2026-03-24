# Differentiating the Black–Scholes PDE


Greeks can be characterized by differentiating the Black–Scholes PDE satisfied by the option price.

---

## Black–Scholes PDE


For a European option \(V(t,S)\),

\[
\boxed{
\frac{\partial V}{\partial t}
+\frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}
+rS\frac{\partial V}{\partial S}
-rV=0,
\qquad V(T,S)=\Phi(S).
}
\]



---

## Delta equation


Let \(\Delta=V_S\). Differentiate the PDE with respect to \(S\):

\[
\frac{\partial}{\partial S}\left(\frac{\partial V}{\partial t}\right)
+\frac{1}{2}\sigma^2 \frac{\partial}{\partial S}\!\left(S^2 V_{SS}\right)
+r\frac{\partial}{\partial S}\!\left(SV_S\right)
-rV_S=0
\]

Computing each term:
- \(\frac{\partial}{\partial S}(S^2 V_{SS}) = 2S V_{SS} + S^2 V_{SSS}\)
- \(\frac{\partial}{\partial S}(S V_S) = V_S + S V_{SS}\)

Substituting \(\Delta = V_S\), \(\Gamma = V_{SS}\), and \(\Delta_S = \Gamma\):

\[
\frac{\partial \Delta}{\partial t}
+ \frac{1}{2}\sigma^2(2S\Gamma + S^2\Gamma_S)
+ r(\Delta + S\Gamma)
- r\Delta = 0
\]

Simplifying:

\[
\boxed{
\frac{\partial \Delta}{\partial t}
+ \frac{1}{2}\sigma^2 S^2 \Delta_{SS}
+ (r + \sigma^2)S\,\Delta_S
+ \sigma^2 \Delta
- r\Delta = 0
}
\]

Or in operator form:

\[
\frac{\partial \Delta}{\partial t} + \mathcal{L}\Delta + \sigma^2 S \Gamma = 0
\]

where \(\mathcal{L}\) is the Black–Scholes operator. The terminal condition is \(\Delta(T,S) = \Phi'(S)\) (which may be distributional for kinked payoffs).

---

## Gamma equation


Let \(\Gamma = V_{SS}\). Differentiate the delta PDE with respect to \(S\):

\[
\frac{\partial \Gamma}{\partial t}
+ \frac{1}{2}\sigma^2 S^2 \Gamma_{SS}
+ (r + 2\sigma^2)S\,\Gamma_S
+ (2\sigma^2 + r)\Gamma
- r\Gamma = 0
\]

Simplifying:

\[
\boxed{
\frac{\partial \Gamma}{\partial t}
+ \frac{1}{2}\sigma^2 S^2 \Gamma_{SS}
+ (r + 2\sigma^2)S\,\Gamma_S
+ 2\sigma^2 \Gamma = 0
}
\]

The terminal condition is \(\Gamma(T,S) = \Phi''(S)\). For a vanilla call, \(\Phi''(S) = \delta(S-K)\) (Dirac delta), explaining why gamma concentrates near the strike as \(t \to T\).

---

## Practical use of PDE identities


These PDEs are useful for:
- **Boundary behavior analysis**: determining far-field limits \(S \to 0\) and \(S \to \infty\)
- **Maximum principle arguments**: establishing bounds on Greeks
- **Regularity theory**: understanding smoothness away from maturity
- **Numerical schemes**: designing stable finite-difference methods for Greeks

---

## What to remember


- Differentiating the pricing PDE yields PDEs for Greeks.
- Delta satisfies a modified Black–Scholes PDE with an extra drift term.
- Gamma satisfies its own PDE with terminal condition given by \(\Phi''\).
- For stable computation, combine PDE identities with transformations or expectation formulas.

---

## Exercises

**Exercise 1.** Starting from the Black--Scholes PDE $\partial_t V + \frac{1}{2}\sigma^2 S^2 V_{SS} + rSV_S - rV = 0$, differentiate with respect to $S$ and verify that the delta PDE contains the extra terms $\sigma^2 S \Gamma$ compared to the original PDE.

---

**Exercise 2.** The gamma PDE has terminal condition $\Gamma(T,S) = \Phi''(S)$. For a vanilla call $\Phi(S) = (S-K)^+$, explain why $\Phi''(S) = \delta(S-K)$ is distributional. How does the parabolic PDE "regularize" this Dirac delta into a smooth function for $t < T$?

---

**Exercise 3.** Use the delta PDE to determine the far-field behavior of delta: show that $\Delta(t,S) \to 1$ as $S \to \infty$ and $\Delta(t,S) \to 0$ as $S \to 0$ for a European call, consistent with boundary conditions.

---

**Exercise 4.** Differentiate the Black--Scholes PDE with respect to $r$ to derive the PDE for rho. Verify that the source term is $V - S V_S$ and the terminal condition is $\rho(T,S) = 0$.

---

**Exercise 5.** Consider designing a finite-difference scheme to solve the gamma PDE numerically. Why is this more challenging than solving the original Black--Scholes PDE? Discuss the role of the distributional terminal condition and propose a regularization approach.

---

**Exercise 6.** The delta PDE can be written as $\partial_t \Delta + \mathcal{L}\Delta + \sigma^2 S\Gamma = 0$ where $\mathcal{L}$ is the Black--Scholes operator. Show that substituting the Black--Scholes delta $\Delta = N(d_1)$ and gamma $\Gamma = N'(d_1)/(S\sigma\sqrt{\tau})$ into this PDE yields an identity. (Hint: use the known time derivatives of $d_1$.)
