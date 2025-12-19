# Greeks in the Black–Scholes Model

In the previous sections, Greeks were defined abstractly as partial derivatives of a pricing operator
(V(t,S;\sigma,r,\dots)). We now **specialize these definitions to the Black–Scholes model** and compute the Greeks explicitly from the closed-form option pricing formulas.

Throughout, let
[
\tau := T - t,
]
and define
[
d_1 = \frac{\log(S_t/K) + (r + \tfrac12 \sigma^2)\tau}{\sigma \sqrt{\tau}},
\qquad
d_2 = d_1 - \sigma \sqrt{\tau}.
]
Denote by (N(\cdot)) the standard normal distribution function and by
[
N'(x) = \frac{1}{\sqrt{2\pi}} e^{-x^2/2}
]
its density.

---

## Delta

Delta measures first-order sensitivity of the option price with respect to the underlying price:
[
\Delta := \frac{\partial V}{\partial S_t}.
]

* **Call option**:
  [
  \Delta_{\text{call}} = N(d_1).
  ]

* **Put option**:
  [
  \Delta_{\text{put}} = N(d_1) - 1 = -N(-d_1).
  ]

Delta lies in ((0,1)) for calls and ((-1,0)) for puts, reflecting monotonicity of the option value in (S_t).

---

## Gamma

Gamma is the second derivative with respect to the underlying price:
[
\Gamma := \frac{\partial^2 V}{\partial S_t^2}.
]

For both calls and puts,
[
\Gamma = \frac{N'(d_1)}{S_t , \sigma , \sqrt{\tau}}.
]

Gamma is always positive, expressing the convexity of option prices in the underlying. It becomes large near maturity and for at-the-money options.

---

## Vega

Vega measures sensitivity with respect to volatility:
[
\nu := \frac{\partial V}{\partial \sigma}.
]

For both calls and puts,
[
\nu = S_t \sqrt{\tau} , N'(d_1).
]

Vega is maximized near-the-money and decreases as maturity approaches zero.

---

## Theta

Theta measures sensitivity with respect to calendar time:
[
\Theta := \frac{\partial V}{\partial t}.
]

> **Convention.** Some texts define theta as (-\partial_t V). Here we use the calendar-time convention (\partial_t V); signs must be interpreted accordingly.

* **Call option**:
  [
  \Theta_{\text{call}}
  = -\frac{S_t , \sigma , N'(d_1)}{2 \sqrt{\tau}}

  * r K e^{-r\tau} N(d_2).
    ]

* **Put option**:
  [
  \Theta_{\text{put}}
  = -\frac{S_t , \sigma , N'(d_1)}{2 \sqrt{\tau}}

  * r K e^{-r\tau} N(-d_2).
    ]

Theta is typically negative, reflecting time decay, except in special regimes (e.g. deep in-the-money puts).

---

## Rho

Rho measures sensitivity with respect to the interest rate:
[
\rho := \frac{\partial V}{\partial r}.
]

* **Call option**:
  [
  \rho_{\text{call}} = \tau K e^{-r\tau} N(d_2).
  ]

* **Put option**:
  [
  \rho_{\text{put}} = -\tau K e^{-r\tau} N(-d_2).
  ]

Rho reflects the present-value effect of the strike and is typically small for short maturities.

---

## Summary

This section illustrates how the abstract Greeks introduced earlier reduce, in the Black–Scholes model, to explicit closed-form expressions. These formulas form the basis for practical risk management, hedging, and numerical calibration in equity option markets.
