# General Short-Rate Framework


Short-rate models describe interest rates by modeling the **instantaneous short rate** \(r_t\). Once \(r_t\) is specified under the risk-neutral measure, discount factors and bond prices follow from expectation of discounted cashflows.

---

## The short rate and money-market account


The **short rate** \(r_t\) is the instantaneous continuously compounded risk-free rate. The money-market account (bank account) evolves as

\[
dB_t = r_t B_t\,dt,
\qquad B_0 = 1,
\]


so

\[
B_t = \exp\left(\int_0^t r_s ds\right).
\]



---

## Pricing zero-coupon bonds


A zero-coupon bond price at time \(t\) for maturity \(T\) is

\[
P(t,T) = \mathbb{E}^{\mathbb{Q}}\left[\exp\left(-\int_t^T r_s ds\right)\middle|\mathcal{F}_t\right].
\]



Thus, the bond price is fully determined by the risk-neutral dynamics of \(r_t\).

---

## Markov short-rate models


In a Markov short-rate model,

\[
dr_t = \mu^{\mathbb{Q}}(t,r_t)\,dt + \sigma(t,r_t)\,dW_t^{\mathbb{Q}}.
\]



Then \(P(t,T)=P(t,T,r_t)\) is a function of \(t\), \(T\), and the current short rate.

---

## Bond pricing PDE


Under sufficient regularity, \(P(t,T,r)\) satisfies the PDE

\[
\partial_t P + \mu^{\mathbb{Q}}(t,r)\partial_r P + \tfrac12\sigma(t,r)^2\partial_{rr}P - rP = 0,
\]


with terminal condition \(P(T,T,r)=1\).

---

## Calibration perspective


Short-rate models are typically calibrated to:
- today’s yield curve (fit initial term structure),
- a subset of liquid interest-rate options (caps/floors, swaptions),
- historical rate dynamics (under \(\mathbb{P}\), if desired).

A key design goal is tractability for \(P(t,T)\) and option pricing.

---

## Key takeaways


- Short-rate models start by specifying \(r_t\) under \(\mathbb{Q}\).
- Bond prices are expectations of discounted short-rate integrals.
- Markov models yield PDEs and often closed forms for bonds.

---

## Further reading


- Brigo & Mercurio, *Interest Rate Models*.
- Björk, *Arbitrage Theory in Continuous Time*.
