# Monotone Schemes and Viscosity Solutions


When classical smooth solutions fail (e.g. obstacle problems), **viscosity solutions** give the correct weak notion, and **monotone schemes** are a key route to convergence.

---

## Viscosity Solutions (Idea)


For a PDE \(F(t,x,u,Du,D^2u)=0\), viscosity sub/supersolutions are defined via smooth test functions touching from above/below. Comparison principles yield uniqueness.

---

## Monotone Schemes


A scheme \(\mathcal{S}_\Delta\) is monotone if increasing input data cannot decrease the output (discrete comparison). Practically this is tied to nonnegative stencil coefficients and discrete maximum principles.

---

## Consistency + Stability + Monotonicity


A foundational convergence principle (orientation) is that:

\[
\boxed{
\text{consistent} + \text{stable} + \text{monotone}
\Longrightarrow
\text{convergence to the viscosity solution}
}
\]


when a comparison principle holds.

---

## Application to American Options


Obstacle problems require monotone discretizations and constraint enforcement (projection/LCP) to ensure convergence to the correct viscosity solution.

---

## What to Remember


- Viscosity solutions handle nonsmoothness and inequalities.
- Monotone schemes preserve comparison principles discretely.
- This pairing is central for reliable American option numerics.

---

## Exercises

**Exercise 1.** State the convergence principle: consistent + stable + monotone implies convergence to the viscosity solution. Explain why each of the three conditions is necessary by describing what can go wrong if one is removed.

---

**Exercise 2.** Consider the explicit scheme $u_j^{n+1} = a_j u_{j-1}^n + b_j u_j^n + c_j u_{j+1}^n$. Under what conditions on the coefficients $a_j$, $b_j$, $c_j$ is the scheme monotone? Show that the CFL condition $\Delta\tau \leq (\Delta S)^2 / (\sigma^2 S_{\max}^2)$ is related to the non-negativity of $b_j$.

---

**Exercise 3.** The Crank-Nicolson scheme is second-order accurate but not monotone in general. Give an example of how non-monotonicity can produce spurious oscillations in the numerical solution of an American option problem.

---

**Exercise 4.** Define what it means for a function $u$ to be a viscosity subsolution of a PDE $F(x, u, Du, D^2u) = 0$. Why is the viscosity framework necessary for American option pricing, where the solution satisfies an inequality rather than an equation?

---

**Exercise 5.** Explain the discrete maximum principle: $\min_j u_j^n \leq u_j^{n+1} \leq \max_j u_j^n$. Show that this holds for the explicit scheme when all stencil coefficients are non-negative and sum to one. Why does this property guarantee that option prices remain non-negative?

---

**Exercise 6.** For the American option obstacle problem $\min(-u_\tau + \mathcal{L}u,\; u - \Phi) = 0$, explain how the projection $u_j^{n+1} \leftarrow \max(u_j^{n+1}, \Phi_j)$ preserves monotonicity when applied after a monotone time-stepping scheme.
