# Boundary and Terminal Behavior of Greeks

Greeks exhibit characteristic behavior near \(S\to 0\), \(S\to\infty\), and \(t\uparrow T\). This matters for hedging and numerics.

---

## Far-field behavior (vanilla calls)

As \(S\to\infty\), a call behaves like

\[
V(t,S)\sim S - K e^{-r(T-t)},
\]


so

\[
\Delta(t,S)\to 1,
\qquad
\Gamma(t,S)\to 0.
\]


As \(S\to 0\),

\[
V(t,S)\to 0,
\qquad \Delta(t,S)\to 0,
\qquad \Gamma(t,S)\to 0.
\]



---

## Near maturity

At maturity \(V(T,S)=\Phi(S)\). For payoffs with kinks, derivatives at \(T\) are not classical; gamma concentrates near the kink, explaining near-expiry instability.

---

## What to remember

- Boundary conditions for PDE numerics are guided by far-field Greek limits.
- Near maturity, gamma spikes near the strike; delta becomes step-like.
