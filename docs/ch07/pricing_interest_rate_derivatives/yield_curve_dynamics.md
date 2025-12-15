# Yield Curve Dynamics

Pricing interest-rate derivatives requires understanding not only today’s yield curve but also how the **entire curve evolves over time**. Yield curve dynamics are central to term-structure modeling.

---

## 1. From static curves to dynamics

A static yield curve specifies \(P(0,T)\) or \(f(0,T)\).
A dynamic model specifies how these quantities evolve:
\[
T \mapsto P(t,T), \quad t>0.
\]

Short-rate models induce dynamics for the full curve through the evolution of \(r_t\).

---

## 2. Curve dynamics under short-rate models

Given \(r_t\), bond prices evolve as
\[
P(t,T) = P(t,T,r_t).
\]

Consequences:
- the curve moves in a low-dimensional way,
- all maturities are driven by the same state variable(s),
- this limits flexibility but ensures consistency.

---

## 3. Drift restrictions and no-arbitrage

No-arbitrage imposes strong constraints on curve dynamics:
- drifts of bond prices are determined by volatility,
- arbitrage-free evolution ties together different maturities.

These ideas are formalized in HJM theory.

---

## 4. Implications for derivative pricing

Yield curve dynamics determine:
- swap and FRA pricing,
- cap/floor and swaption dynamics,
- hedging behavior across maturities.

Model choice affects which curve moves are possible.

---

## 5. Key takeaways

- Yield curve dynamics are essential for IR derivative pricing.
- Short-rate models generate low-dimensional curve movements.
- No-arbitrage tightly constrains curve evolution.

---

## Further reading

- Heath, Jarrow & Morton (HJM).
- Filipović, *Term-Structure Models*.
