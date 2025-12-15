# Affine Term Structure

Many short-rate models (including Vasicek and CIR) belong to the **affine term structure** class. Affine structure explains why bond prices have closed forms and provides a framework for multi-factor generalizations.

---

## 1. Affine bond prices

A term structure model is affine if zero-coupon bond prices can be written as
\[
P(t,T) = \exp\big(A(t,T) - B(t,T)^{\top}X_t\big),
\]
where:
- \(X_t\) is a state vector (often including the short rate),
- \(A\) and \(B\) are deterministic functions.

In the one-factor case, \(X_t=r_t\).

---

## 2. Why affine models are tractable

Affine models lead to:
- exponential-affine characteristic functions,
- Riccati-type ODEs for \(A\) and \(B\),
- closed-form bond prices and efficient option pricing in many cases.

This is analogous to affine stochastic volatility (e.g., Heston).

---

## 3. Examples

- **Vasicek:** Gaussian affine model.
- **CIR:** square-root affine model.
- **Multi-factor affine models:** sums of OU/CIR factors.

These models are widely used for curve and swaption pricing (often with shifts).

---

## 4. Fitting the initial yield curve

A common practical extension is **time-dependent drift** (e.g., Hull–White):
- preserves affine structure,
- fits today’s yield curve exactly,
- retains analytical tractability.

---

## 5. Key takeaways

- Affine structure yields exponential-affine bond prices.
- Vasicek and CIR are key affine examples.
- Affine term structure theory supports scalable multi-factor extensions.

---

## Further reading

- Duffie & Kan, affine term structure models.
- Filipović, *Term-Structure Models*.
- Brigo & Mercurio, affine short-rate modeling.
