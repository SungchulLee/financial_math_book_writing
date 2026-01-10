# Terminal and Boundary Conditions

## 1. Why Conditions Matter
A PDE alone does not determine a unique solution.
Financial contracts specify *terminal* and *boundary* conditions.

---

## 2. Terminal Conditions
For a European payoff \(\Phi(X_T)\):
\[
u(T,x) = \Phi(x).
\]

Examples:
- Call option: \( (x-K)^+ \)
- Put option: \( (K-x)^+ \)

---

## 3. Boundary Conditions
Boundaries encode contractual features:
- Absorbing (Dirichlet): default, barriers
- Reflecting (Neumann): regulatory constraints

Example (down-and-out barrier):
\[
u(t,B) = 0.
\]

---

## 4. Mathematical Classification
- Dirichlet: value specified
- Neumann: derivative specified
- Mixed conditions

---

## 5. Financial Interpretation
Boundary conditions reflect:
- Early termination
- Insolvency
- Regulatory or contractual limits

---

## 6. Connection Forward
Boundary behavior becomes crucial in exotic option pricing.