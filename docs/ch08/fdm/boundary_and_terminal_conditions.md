# Boundary and Terminal Conditions


Numerical PDE pricing requires:
- a **terminal condition** at \(t=T\),
- **boundary conditions** in \(S\) after truncating \((0,\infty)\) to \([0,S_{\max}]\).

---

## Terminal Condition


For a European payoff \(\Phi(S)\),

\[
\boxed{V(T,S)=\Phi(S).}
\]


In time-to-maturity \(\tau=T-t\), this becomes \(u(0,S)=\Phi(S)\).

Payoffs often have kinks (e.g. \((S-K)^+\)), affecting accuracy near \(\tau=0\).

---

## Truncation


Choose \(S_{\max}\) large enough to make truncation error negligible in the region of interest.

---

## Vanilla Boundary Conditions


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

## Neumann-Type Alternatives


Call delta tends to \(1\) as \(S\to\infty\):

\[
\boxed{V_S(t,S_{\max})\approx 1.}
\]


Put delta tends to \(0\):

\[
\boxed{V_S(t,S_{\max})\approx 0.}
\]



---

## Implementation Notes


At boundaries, use one-sided differences, ghost points, or enforce asymptotic formulas. Boundary choices interact with stability and monotonicity.

---

## What to Remember


- Terminal payoff regularity matters.
- Boundary conditions are part of the model numerically.
- Dirichlet and Neumann conditions are both used in practice.

---

## Exercises

**Exercise 1.** For a European call with $K = 100$, $r = 0.05$, and $T = 0.5$, compute the Dirichlet boundary values at $S = 0$ and $S_{\max} = 300$ at times $t = 0$, $t = 0.25$, and $t = 0.5$. How do the boundary values change as $t$ approaches maturity?

---

**Exercise 2.** Explain why the terminal condition for a European option in the time-to-maturity formulation becomes an initial condition $u(0, S) = \Phi(S)$. Write down the initial condition explicitly for a put option with strike $K$.

---

**Exercise 3.** The Neumann boundary condition for a call at the upper boundary is $V_S(t, S_{\max}) \approx 1$. Using a backward finite difference at $j = M$, express $V_M^n$ in terms of $V_{M-1}^n$ and $\Delta S$. Compare this to the Dirichlet condition $V_M^n = S_{\max} - Ke^{-r(T - t_n)}$ and discuss which is more appropriate when $S_{\max}$ is not sufficiently large.

---

**Exercise 4.** Consider a domain $[0, S_{\max}]$ with $S_{\max} = 200$ and $K = 100$. Estimate the truncation error at $S = 100$ caused by the artificial boundary at $S_{\max}$ for a European put. Why is this error negligible for puts but potentially problematic for calls if $S_{\max}$ is too small?

---

**Exercise 5.** The payoff $\Phi(S) = (S - K)^+$ has a discontinuous first derivative at $S = K$. Explain how this kink affects the accuracy of the FDM solution near $\tau = 0$. Describe the Rannacher smoothing technique and explain why it helps.

---

**Exercise 6.** A ghost-point implementation of the Neumann condition $V_S(t, S_{\max}) = 1$ introduces a fictitious node $S_{M+1}$ and uses the central difference $(V_{M+1}^n - V_{M-1}^n)/(2\Delta S) = 1$ to express $V_{M+1}^n$. Derive the resulting equation for $V_M^n$ in the implicit scheme.
