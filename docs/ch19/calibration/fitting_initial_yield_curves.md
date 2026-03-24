# Fitting Initial Yield Curves


A fundamental requirement of any interest-rate model is the **exact fit of the initial yield curve**. Since discount factors are directly observable from the market, a model must reproduce them to avoid static arbitrage.

---

## Market input and bootstrapping


The market provides quotes for liquid instruments such as:
- deposits and short-term rates,
- futures and FRAs,
- OIS and IRS swaps.

From these, a discount curve \(P(0,T)\) is constructed via **bootstrapping**, ensuring that each instrument is priced exactly.

---

## Curve fitting vs model fitting


Two conceptually distinct steps are involved:

1. **Curve construction:** build a smooth, arbitrage-free discount curve from market quotes.
2. **Model initialization:** ensure the model reproduces this curve at time 0.

Modern practice treats curve construction as a pre-model step.

---

## Exact fit techniques


Common approaches to enforce exact fit include:

- **Deterministic shifts:** add a time-dependent drift (e.g. Hull–White extension),
- **Initial term-structure fitting:** calibrate model functions to match \(P(0,T)\),
- **HJM framework:** exact fit is automatic by construction.

Exact fit is essential for pricing curve-sensitive products.

---

## Consequences of poor curve fit


Failure to match the initial curve leads to:
- immediate arbitrage,
- systematic mispricing of swaps and FRAs,
- unstable hedging behavior.

Thus, curve fitting is non-negotiable in practice.

---

## Key takeaways


- The initial yield curve must be fitted exactly.
- Curve construction and model calibration are separate tasks.
- Shifts and HJM ensure consistency with market curves.

---

## Further reading


- Brigo & Mercurio, curve construction.
- Andersen & Piterbarg, interest-rate modeling practice.

---

## Exercises

**Exercise 1.** Suppose you observe the following zero-coupon bond prices: $P(0,0.5) = 0.9950$, $P(0,1) = 0.9870$, $P(0,1.5) = 0.9760$, and $P(0,2) = 0.9620$. Compute the continuously compounded zero rates $R(0,T)$ for each maturity using the relation

$$
P(0,T) = e^{-R(0,T)\,T}.
$$

Verify that the zero rates are increasing with maturity and interpret this shape economically.

---

**Exercise 2.** A two-year par swap with semiannual payments has a quoted rate of $s = 3.80\%$. Using the discount factors from Exercise 1, verify whether the par swap rate is consistent with these discount factors via the formula

$$
s = \frac{1 - P(0,T_n)}{\sum_{i=1}^{n} \delta_i\, P(0,T_i)},
$$

where $\delta_i = 0.5$ for semiannual periods. If it is not consistent, explain what adjustment to the curve would be needed.

---

**Exercise 3.** Consider the Hull--White model with short-rate dynamics

$$
dr(t) = \bigl[\theta(t) - a\,r(t)\bigr]\,dt + \sigma\,dW(t).
$$

Show that exact fit to the initial term structure is achieved by choosing

$$
\theta(t) = \frac{\partial f(0,t)}{\partial t} + a\,f(0,t) + \frac{\sigma^2}{2a}\bigl(1 - e^{-2at}\bigr),
$$

where $f(0,t) = -\frac{\partial}{\partial t}\ln P(0,t)$ is the initial instantaneous forward rate. Explain why this deterministic shift approach is called "fitting the initial curve."

---

**Exercise 4.** Explain why the HJM framework provides an automatic exact fit to the initial yield curve, whereas equilibrium short-rate models (such as Vasicek or CIR without extensions) do not. In your answer, reference the role of the initial forward-rate curve $f(0,T)$ as an input to the HJM dynamics.

---

**Exercise 5.** A trader builds a discount curve by bootstrapping deposits (up to 6 months), futures (6 months to 2 years), and swaps (2 years to 30 years). After bootstrapping, the instantaneous forward-rate curve $f(0,T)$ exhibits a sudden jump at the 2-year point where futures end and swaps begin. Discuss why this discontinuity arises and propose at least two methods to produce a smoother forward-rate curve while still fitting all market instruments exactly.

---

**Exercise 6.** Consider two candidate discount curves that both reprice all market instruments exactly:

- Curve A uses piecewise-constant forward rates.
- Curve B uses cubic-spline interpolation on zero rates.

For a 10-year Bermudan swaption priced under a short-rate model calibrated to each curve, explain how the choice of interpolation method could affect (a) the shape of $\theta(t)$, (b) the model-implied volatility of forward rates, and (c) the resulting Bermudan swaption price.

---

**Exercise 7.** Suppose the initial discount curve is perturbed by a parallel shift of $+10$ basis points in all zero rates. For a portfolio consisting of a 5-year receiver swap (notional \$100 million, fixed rate 3.50%, semiannual) priced using the original curve, estimate the change in portfolio value using the first-order approximation

$$
\Delta V \approx -\text{DV01} \times \Delta r,
$$

where DV01 is the dollar value of one basis point. Explain why exact curve fitting is critical for obtaining an accurate DV01 estimate.
