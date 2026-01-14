# No-Arbitrage Relations


No-arbitrage principles link discount factors, zero rates, and forward rates. These relations are the foundation of curve construction and fixed-income pricing.

---

## Replication argument for forwards


Consider lending 1 unit from 0 to \(T_2\) via:
- buying a \(T_2\) zero-coupon bond, cost \(P(0,T_2)\).

Alternatively, lend from 0 to \(T_1\) and then roll over from \(T_1\) to \(T_2\):
- buy a \(T_1\) bond, cost \(P(0,T_1)\),
- at \(T_1\), reinvest at the forward rate.

No-arbitrage implies equality of terminal payoffs, yielding

\[
\frac{P(0,T_1)}{P(0,T_2)} = 1 + F(0;T_1,T_2)(T_2-T_1).
\]



---

## Discount factor monotonicity and positivity


Under absence of arbitrage with non-negative rates:
- \(P(0,T)\) is decreasing in \(T\),
- forward rates are non-negative.

With negative rates, discount factors can still be decreasing but forwards/zeros may be negative; positivity constraints must be handled with care.

---

## Coupon bond pricing by discounting


A coupon bond with cashflows \(c_i\) at times \(T_i\) has price

\[
B_0 = \sum_i c_i\,P(0,T_i).
\]



This is a direct consequence of linearity and absence of arbitrage: each cashflow is discounted using the appropriate \(P(0,T_i)\).

---

## Basic arbitrage checks for a curve


A constructed curve should satisfy:
- \(P(0,0)=1\),
- \(P(0,T)>0\),
- smoothness/shape consistent with market instruments,
- no obvious calendar arbitrage in implied forwards (no extreme oscillations without justification).

In practice, these checks guide interpolation and smoothing choices.

---

## Key takeaways


- No-arbitrage links forwards and discount factors via replication.
- Discounting prices coupon bonds and deterministic cashflows.
- Curve construction must respect positivity and shape constraints.

---

## Further reading


- Björk, *Arbitrage Theory in Continuous Time*.
- Brigo & Mercurio, *Interest Rate Models*.
