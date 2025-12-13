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

## Delta equation (formal)

Let \(\Delta=V_S\). Differentiate the PDE with respect to \(S\):
\[
\frac{\partial \Delta}{\partial t}
+\frac{1}{2}\sigma^2 \frac{\partial}{\partial S}\!\left(S^2 V_{SS}\right)
+r\frac{\partial}{\partial S}\!\left(SV_S\right)
-r\Delta=0.
\]
This produces a linear PDE involving higher derivatives; it is most useful for:
- boundary behavior,
- maximum principle arguments,
- regularity insights.

---

## What to remember

- Differentiating the pricing PDE yields PDEs for Greeks.
- For stable computation, combine PDE identities with transformations or expectation formulas.
