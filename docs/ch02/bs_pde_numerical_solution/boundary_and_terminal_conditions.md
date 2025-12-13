# Boundary and Terminal Conditions

Numerical PDE pricing requires:
- a **terminal condition** at \(t=T\),
- **boundary conditions** in \(S\) after truncating \((0,\infty)\) to \([0,S_{\max}]\).

---

## 1. Terminal Condition

For a European payoff \(\Phi(S)\),
\[
\boxed{V(T,S)=\Phi(S).}
\]
In time-to-maturity \(\tau=T-t\), this becomes \(u(0,S)=\Phi(S)\).

Payoffs often have kinks (e.g. \((S-K)^+\)), affecting accuracy near \(\tau=0\).

---

## 2. Truncation

Choose \(S_{\max}\) large enough to make truncation error negligible in the region of interest.

---

## 3. Vanilla Boundary Conditions

Call:
\[
\boxed{
V(t,0)=0,
\qquad
V(t,S_{\max})\approx S_{\max}-Ke^{-r(T-t)}.
}
\]

Put:
\[
\boxed{
V(t,0)\approx Ke^{-r(T-t)},
\qquad
V(t,S_{\max})\approx 0.
}
\]

---

## 4. Neumann-Type Alternatives

Call delta tends to \(1\) as \(S\to\infty\):
\[
\boxed{V_S(t,S_{\max})\approx 1.}
\]
Put delta tends to \(0\):
\[
\boxed{V_S(t,S_{\max})\approx 0.}
\]

---

## 5. Implementation Notes

At boundaries, use one-sided differences, ghost points, or enforce asymptotic formulas. Boundary choices interact with stability and monotonicity.

---

## 6. What to Remember

- Terminal payoff regularity matters.
- Boundary conditions are part of the model numerically.
- Dirichlet and Neumann conditions are both used in practice.
