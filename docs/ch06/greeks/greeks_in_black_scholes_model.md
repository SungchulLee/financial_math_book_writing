# Greeks in the Black–Scholes Model

In the previous sections, Greeks were defined abstractly as partial derivatives of a pricing operator
\(V(t,S;\sigma,r,\dots)\). We now **specialize these definitions to the Black–Scholes model** and compute the Greeks explicitly from the closed-form European call/put formulas. 

---

## Notation and Black–Scholes parameters

Let

- \(S\): current underlying price (at time \(t\))
- \(K\): strike
- \(r\): constant risk-free rate
- \(\sigma\): volatility
- \(T\): maturity
- \(t\): current time
- \(\tau := T-t\): time to maturity
- \(N(\cdot)\): standard normal CDF
- \(N'(x) = \dfrac{1}{\sqrt{2\pi}}e^{-x^2/2}\): standard normal PDF

Define

\[
d_1 = \frac{\ln(S/K) + \left(r+\tfrac12\sigma^2\right)\tau}{\sigma\sqrt{\tau}},
\qquad
d_2 = d_1 - \sigma\sqrt{\tau}
\]

The Black–Scholes prices are

\[
C = S N(d_1) - K e^{-r\tau}N(d_2),
\qquad
P = K e^{-r\tau}N(-d_2) - S N(-d_1)
\]

---

## Delta

\[
\Delta := \frac{\partial V}{\partial S}
\]

- **Call**:
- 
\[
\Delta_{\text{call}} = N(d_1)
\]

- **Put**:
- 
\[
\Delta_{\text{put}} = N(d_1)-1 = -N(-d_1)
\]

Delta lies in \((0,1)\) for calls and \((-1,0)\) for puts.

---

## Gamma

\[
\Gamma := \frac{\partial^2 V}{\partial S^2}
\]

For both calls and puts,

\[
\Gamma = \frac{N'(d_1)}{S\,\sigma\sqrt{\tau}}
\]

Gamma is always positive (convexity in \(S\)) and becomes large near maturity (small \(\tau\)).

---

## Vega

\[
\nu := \frac{\partial V}{\partial \sigma}
\]

For both calls and puts,

\[
\nu = S\sqrt{\tau}\,N'(d_1)
\]

Vega is typically largest near-the-money and for moderate maturities.

---

## Theta

\[
\Theta := \frac{\partial V}{\partial t}
\]

> **Convention.** Some texts define theta as \(-\partial_t V\).  
> Here we use **calendar-time theta** \(\Theta=\partial_t V\); interpret signs accordingly.

- **Call**:
- 
\[
\Theta_{\text{call}}
= -\frac{S\sigma N'(d_1)}{2\sqrt{\tau}} - rK e^{-r\tau}N(d_2)
\]

- **Put**:
- 
\[
\Theta_{\text{put}}
= -\frac{S\sigma N'(d_1)}{2\sqrt{\tau}} + rK e^{-r\tau}N(-d_2)
\]

Theta is typically negative (time decay), with exceptions in certain regimes (e.g., deep ITM puts).

---

## Rho

\[
\rho := \frac{\partial V}{\partial r}
\]

- **Call**:
- 
\[
\rho_{\text{call}} = K\tau e^{-r\tau}N(d_2)
\]

- **Put**:
- 
\[
\rho_{\text{put}} = -K\tau e^{-r\tau}N(-d_2)
\]

Rho reflects the present-value effect of the strike and is usually small for short maturities.

---

## Symmetries and notes

- **Gamma** and **Vega** are identical for calls and puts: they depend on the diffusion of \(S\), not the payoff direction.
- **Delta**, **Theta**, and **Rho** differ between calls and puts due to payoff asymmetry and the discounting term.
- All expressions above follow by differentiating the Black–Scholes closed forms for \(C\) and \(P\).

---

## Conceptual interpretation (typical signs)

| Greek  | Meaning                                  | Call sign | Put sign |
|-------:|------------------------------------------|:---------:|:--------:|
| Delta  | price change per unit \(S\)              | \(>0\)    | \(<0\)   |
| Gamma  | convexity / rate of change of Delta      | \(>0\)    | \(>0\)   |
| Theta  | calendar-time decay                       | usually \(<0\) | usually \(<0\) |
| Vega   | sensitivity to volatility                | \(>0\)    | \(>0\)   |
| Rho    | sensitivity to interest rate             | \(>0\)    | \(<0\)   |

---

## Summary

This section shows how the abstract Greeks reduce, in the Black–Scholes model, to explicit closed-form expressions. These formulas are the baseline for practical risk management, hedging, and calibration, and they also highlight where Black–Scholes is too restrictive (e.g., constant \(\sigma\) across strikes/maturities).
