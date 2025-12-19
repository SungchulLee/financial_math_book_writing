# Stability, Consistency, and Convergence

A numerical scheme is assessed by:
- **Consistency**: local approximation of the PDE,
- **Stability**: control of error growth,
- **Convergence**: approach to the true solution as the mesh refines.

A guiding principle for linear well-posed problems is:

\[
\boxed{\text{Consistency}+\text{Stability}\Longrightarrow\text{Convergence}.}
\]



---

## 1. Consistency

For a smooth test function \(u\), a scheme is consistent if the local truncation error tends to zero:

\[
\boxed{
\mathcal{D}_\Delta u = \mathcal{D}u + o(1)\quad (\Delta\to 0),
}
\]


where \(\mathcal{D}u=0\) is the PDE.

---

## 2. Stability

For a linear recursion \(u^{n+1}=Bu^n+g^n\), stability requires a uniform bound

\[
\boxed{\|B^n\|\le C}
\]


in a suitable norm, uniformly as mesh sizes vanish.

Explicit schemes often require CFL-type restrictions; implicit schemes are typically more stable.

---

## 3. Payoff Regularity Matters

Vanilla payoffs (call/put) are not \(C^1\), so the solution is less regular near \(\tau=0\). This can reduce observed convergence order unless smoothing is used.

---

## 4. Monotonicity and Maximum Principles

Discrete comparison principles (monotone schemes) are especially important for variational inequalities (American options) and for convergence to viscosity solutions.

---

## 5. What to Remember

- Consistency is local; stability is global; convergence is the goal.
- Nonsmooth payoffs can dominate error near maturity.
- Monotonicity links numerical methods to viscosity solutions.
