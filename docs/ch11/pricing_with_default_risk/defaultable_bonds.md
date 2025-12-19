# Defaultable Bonds

Defaultable bonds are bonds subject to issuer default risk. Their pricing reflects both interest-rate discounting and the possibility of default with partial recovery.

---

## 1. Payoff structure

A defaultable zero-coupon bond pays:
- 1 at maturity \(T\) if no default occurs before \(T\),
- a recovery payment if default occurs at \(\tau \le T\).

Thus, cashflows depend on the random default time.

---

## 2. Pricing principle

Under the risk-neutral measure,

\[
P^d(t,T) = \mathbb{E}^{\mathbb{Q}}\left[
e^{-\int_t^T r_s ds}\, \mathbf{1}_{\{\tau > T\}}
+ e^{-\int_t^{\tau} r_s ds}\, R_{\tau}\, \mathbf{1}_{\{t<\tau\le T\}}
\middle| \mathcal{F}_t
\right],
\]


where \(R_{\tau}\) is the recovery payoff.

---

## 3. Credit spread interpretation

The yield on a defaultable bond exceeds the risk-free yield.
The difference, the **credit spread**, compensates for:
- expected default losses,
- risk premia,
- liquidity effects.

In reduced-form models, spreads are driven by intensity and recovery assumptions.

---

## 4. Coupon-bearing bonds

Coupon bonds are priced as sums of defaultable zero-coupon components.
Default typically accelerates remaining cashflows and triggers recovery.

---

## 5. Key takeaways

- Defaultable bonds combine interest-rate and credit risk.
- Pricing requires modeling default timing and recovery.
- Credit spreads emerge endogenously.

---

## Further reading

- Duffie & Singleton, defaultable term structures.
- Bielecki & Rutkowski, credit bond pricing.
