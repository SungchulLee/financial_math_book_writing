# Monotone Schemes and Viscosity Solutions

When classical smooth solutions fail (e.g. obstacle problems), **viscosity solutions** give the correct weak notion, and **monotone schemes** are a key route to convergence.

---

## 1. Viscosity Solutions (Idea)

For a PDE \(F(t,x,u,Du,D^2u)=0\), viscosity sub/supersolutions are defined via smooth test functions touching from above/below. Comparison principles yield uniqueness.

---

## 2. Monotone Schemes

A scheme \(\mathcal{S}_\Delta\) is monotone if increasing input data cannot decrease the output (discrete comparison). Practically this is tied to nonnegative stencil coefficients and discrete maximum principles.

---

## 3. Consistency + Stability + Monotonicity

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

## 4. Application to American Options

Obstacle problems require monotone discretizations and constraint enforcement (projection/LCP) to ensure convergence to the correct viscosity solution.

---

## 5. What to Remember

- Viscosity solutions handle nonsmoothness and inequalities.
- Monotone schemes preserve comparison principles discretely.
- This pairing is central for reliable American option numerics.
