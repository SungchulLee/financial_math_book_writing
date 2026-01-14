# Terminal Boundary


## Why Conditions

A PDE alone does not determine a unique solution.
Financial contracts specify *terminal* and *boundary* conditions.

---

## Terminal Conditions

For a European payoff \(\Phi(X_T)\):
\[
u(T,x) = \Phi(x).
\]

Examples:
- Call option: \( (x-K)^+ \)
- Put option: \( (K-x)^+ \)

---

## Boundary Conditions

Boundaries encode contractual features:
- Absorbing (Dirichlet): default, barriers
- Reflecting (Neumann): regulatory constraints

Example (down-and-out barrier):
\[
u(t,B) = 0.
\]

---

## Mathematical

- Dirichlet: value specified
- Neumann: derivative specified
- Mixed conditions

---

## Financial

Boundary conditions reflect:
- Early termination
- Insolvency
- Regulatory or contractual limits

---

## Connection Forward

Boundary behavior becomes crucial in exotic option pricing.