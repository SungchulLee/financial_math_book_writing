# Feller Condition and Boundary Behavior

The variance process in the Heston model is a **square-root diffusion**, whose behavior near zero is critical for both theory and numerics.

---

## 1. The CIR variance process

The variance follows
\[
dV_t = \kappa(\theta - V_t)dt + \xi\sqrt{V_t}\,dW_t^V.
\]

This is a Cox–Ingersoll–Ross (CIR) process.

---

## 2. The Feller condition

The **Feller condition**
\[
2\kappa\theta \ge \xi^2
\]
ensures that:
- the boundary \(V_t=0\) is unattainable,
- variance remains strictly positive.

If the condition fails:
- variance can hit zero,
- but remains non-negative.

---

## 3. Practical relevance

In practice:
- many calibrated Heston parameters violate the Feller condition,
- option pricing formulas remain valid,
- simulation schemes must be chosen carefully.

Thus, the Feller condition is sufficient but not necessary.

---

## 4. Boundary behavior and numerics

Near-zero variance can cause:
- numerical instability in simulations,
- bias in Euler schemes.

Common remedies:
- full truncation schemes,
- reflection or absorption handling,
- exact simulation of CIR transitions.

---

## 5. Key takeaways

- The Feller condition guarantees strict positivity.
- Violations are common in market calibration.
- Careful numerical treatment is essential.

---

## Further reading

- Cox, Ingersoll & Ross (1985).
- Andersen, efficient simulation of Heston.
