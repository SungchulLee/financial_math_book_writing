# Affine Term Structure


Many short-rate models (including Vasicek and CIR) belong to the **affine term structure** class. Affine structure explains why bond prices have closed forms and provides a framework for multi-factor generalizations.

---

## Affine bond prices


A term structure model is affine if zero-coupon bond prices can be written as

\[
P(t,T) = \exp\big(A(t,T) - B(t,T)^{\top}X_t\big),
\]


where:
- \(X_t\) is a state vector (often including the short rate),
- \(A\) and \(B\) are deterministic functions.

In the one-factor case, \(X_t=r_t\).

---

## Why affine models are tractable


Affine models lead to:
- exponential-affine characteristic functions,
- Riccati-type ODEs for \(A\) and \(B\),
- closed-form bond prices and efficient option pricing in many cases.

This is analogous to affine stochastic volatility (e.g., Heston).

---

## Examples


- **Vasicek:** Gaussian affine model.
- **CIR:** square-root affine model.
- **Multi-factor affine models:** sums of OU/CIR factors.

These models are widely used for curve and swaption pricing (often with shifts).

---

## Fitting the initial yield curve


A common practical extension is **time-dependent drift** (e.g., Hull–White):
- preserves affine structure,
- fits today’s yield curve exactly,
- retains analytical tractability.

---

## Key takeaways


- Affine structure yields exponential-affine bond prices.
- Vasicek and CIR are key affine examples.
- Affine term structure theory supports scalable multi-factor extensions.

---

## Further reading


- Duffie & Kan, affine term structure models.
- Filipović, *Term-Structure Models*.
- Brigo & Mercurio, affine short-rate modeling.

---

## Exercises

**Exercise 1.** For the affine bond price $P(t,T) = e^{A(t,T) - B(t,T)r_t}$, compute the yield $R(t,T) = -\ln P(t,T)/(T-t)$ and the instantaneous forward rate $f(t,T) = -\partial_T \ln P(t,T)$. Express both in terms of $A$ and $B$ and their derivatives.

---

**Exercise 2.** Verify that the Vasicek model with $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ is affine by showing that the Riccati equations for $A$ and $B$ have the required form $\partial_T B = -1 + \kappa B$ and $\partial_T A = \kappa\theta B - \frac{1}{2}\sigma^2 B^2$ with $A(T,T) = 0$, $B(T,T) = 0$.

---

**Exercise 3.** Explain why the CIR model is affine but the Black-Karasinski model is not. What specific structural property of the drift and diffusion is required for affine structure?

---

**Exercise 4.** In a two-factor affine model with state $X_t = (r_t, v_t)$, the bond price is $P(t,T) = e^{A(t,T) - B_1(t,T)r_t - B_2(t,T)v_t}$. Discuss the advantage of having a second factor $v_t$ for fitting the yield curve and its volatility structure.

---

**Exercise 5.** Show that in an affine model, the yield $R(t,T) = -A(t,T)/(T-t) + B(t,T)r_t/(T-t)$ is linear (affine) in the short rate $r_t$. Why does this property make calibration and pricing computationally efficient?

---

**Exercise 6.** The Riccati ODEs in affine models can be solved in closed form for Vasicek and CIR. For a general affine model, these ODEs may require numerical integration. Describe a numerical method (e.g., Runge-Kutta) for solving the Riccati system, and discuss the accuracy requirements for bond pricing applications.
