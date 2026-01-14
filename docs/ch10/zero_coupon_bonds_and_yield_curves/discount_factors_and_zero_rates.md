# Discount Factors and Zero Rates


Yield curves summarize the time value of money and are foundational for pricing fixed-income instruments and for discounting cashflows in derivatives. This section introduces **discount factors** and **zero (spot) rates**, along with key conventions.

---

## Discount factors


A **discount factor** \(P(0,T)\) is the time-0 price of a zero-coupon bond paying 1 unit of currency at maturity \(T\):

\[
P(0,T) = \text{Price at }0\text{ of a claim paying }1\text{ at }T.
\]



Properties (in standard, positive-rate environments):
- \(P(0,0)=1\),
- \(P(0,T)\) is non-increasing in \(T\),
- \(0 < P(0,T) \le 1\).

In modern markets, negative rates can occur, but discount factors remain positive.

---

## Zero (spot) rates


The **continuously compounded zero rate** \(z(0,T)\) is defined by

\[
P(0,T) = e^{-z(0,T)\,T}
\quad\Longleftrightarrow\quad
z(0,T) = -\frac{1}{T}\log P(0,T).
\]



Alternative compounding conventions are common:

- **Simple compounding:** \(P(0,T)=\frac{1}{1+R(0,T)T}\)
- **Annual compounding:** \(P(0,T)=\frac{1}{(1+R(0,T))^{T}}\) (when \(T\) is in years)

Converting between conventions is routine but must be handled consistently.

---

## Interpretation and uses


Zero rates and discount factors are used to:
- discount deterministic cashflows,
- price zero-coupon bonds and coupons (by decomposition),
- build forward rates and term structures (next section).

In practice, a full curve is built by **bootstrapping** from liquid market instruments (deposits, futures, swaps, OIS, etc.).

---

## Short rate intuition (optional)


If \(r_t\) is the instantaneous short rate under the risk-neutral measure, then

\[
P(0,T) = \mathbb{E}^{\mathbb{Q}}\left[e^{-\int_0^T r_s ds}\right].
\]


In deterministic-rate settings, this reduces to \(P(0,T)=e^{-\int_0^T r(s)ds}\).

---

## Key takeaways


- Discount factors \(P(0,T)\) are the primitives of the yield curve.
- Zero rates are logarithmic transforms of discount factors.
- Compounding conventions matter; be explicit and consistent.

---

## Further reading


- Brigo & Mercurio, *Interest Rate Models*.
- Hull, *Options, Futures, and Other Derivatives* (yield curve basics).
