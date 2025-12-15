# Infinite-Dimensional SDEs

Because HJM models the forward rate curve for all maturities, it naturally leads to **infinite-dimensional stochastic differential equations**.

---

## 1. Infinite-dimensional state space

At each time \(t\), the state is the function
\[
T \mapsto f(t,T),
\]
an element of a function space (e.g., a Hilbert space).

This contrasts with finite-dimensional short-rate models.

---

## 2. Mathematical formulation

Formally, HJM can be written as an SDE in a function space:
\[
df_t = \alpha_t\,dt + \Sigma_t\,dW_t,
\]
where:
- \(f_t\) is a curve,
- \(\Sigma_t\) is a linear operator.

Rigorous treatment uses stochastic calculus in Hilbert spaces.

---

## 3. Finite-dimensional realizations

In practice, one often restricts to:
- separable volatility structures,
- finite-factor representations,
- basis expansions in maturity.

These yield **finite-dimensional realizations** consistent with HJM.

---

## 4. Numerical implementation

Common approaches include:
- maturity discretization (time–maturity grids),
- factor models for volatility,
- projection onto basis functions.

Trade-offs arise between realism and tractability.

---

## 5. Key takeaways

- HJM is intrinsically infinite-dimensional.
- Practical models use finite-factor approximations.
- Mathematical rigor guides stable implementation.

---

## Further reading

- Filipović, *Consistency Problems for HJM Models*.
- Da Prato & Zabczyk, infinite-dimensional SDEs.
