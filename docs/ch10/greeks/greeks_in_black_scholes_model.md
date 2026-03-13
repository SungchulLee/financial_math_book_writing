# Greeks in the Black–Scholes Model


In the previous sections, Greeks were defined abstractly as partial derivatives of a pricing operator
\(V(t,S;\sigma,r,\dots)\). We now **specialize these definitions to the Black–Scholes model** and compute the Greeks explicitly from the closed-form European call/put formulas. 

> **Cross-reference.** The Black–Scholes formula \(C = SN(d_1) - Ke^{-r\tau}N(d_2)\) was derived in **Section 5.6** using risk-neutral pricing. This section differentiates that formula to obtain closed-form Greeks.

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

## Preliminary: Derivatives of \(d_1\) and \(d_2\)


Before computing Greeks, we establish the key derivatives:

\[
\frac{\partial d_1}{\partial S} = \frac{1}{S\sigma\sqrt{\tau}},
\qquad
\frac{\partial d_2}{\partial S} = \frac{\partial d_1}{\partial S} = \frac{1}{S\sigma\sqrt{\tau}}
\]

\[
\frac{\partial d_1}{\partial \sigma} = -\frac{d_2}{\sigma},
\qquad
\frac{\partial d_2}{\partial \sigma} = -\frac{d_1}{\sigma}
\]

\[
\frac{\partial d_1}{\partial \tau} = -\frac{d_2}{2\tau},
\qquad
\frac{\partial d_2}{\partial \tau} = -\frac{d_1}{2\tau}
\]

A crucial identity linking \(N'(d_1)\) and \(N'(d_2)\):

\[
\boxed{S N'(d_1) = K e^{-r\tau} N'(d_2)}
\]

**Proof.** Since \(d_1 - d_2 = \sigma\sqrt{\tau}\), we have

\[
\frac{N'(d_1)}{N'(d_2)} = \exp\!\left(-\frac{d_1^2 - d_2^2}{2}\right)
= \exp\!\left(-\frac{(d_1-d_2)(d_1+d_2)}{2}\right)
\]

Now \(d_1 + d_2 = 2d_1 - \sigma\sqrt{\tau}\), and using \(d_1 = \frac{\ln(S/K) + (r + \frac12\sigma^2)\tau}{\sigma\sqrt{\tau}}\):

\[
\frac{d_1^2 - d_2^2}{2} = \frac{\sigma\sqrt{\tau}(d_1 + d_2)}{2} = \ln(S/K) + r\tau
\]

Thus \(\frac{N'(d_1)}{N'(d_2)} = \frac{K e^{-r\tau}}{S}\), giving \(S N'(d_1) = K e^{-r\tau} N'(d_2)\). \(\square\)

---

## Delta


\[
\Delta := \frac{\partial V}{\partial S}
\]

**Derivation for a call.** Differentiate \(C = SN(d_1) - Ke^{-r\tau}N(d_2)\) with respect to \(S\):

\[
\frac{\partial C}{\partial S} = N(d_1) + S N'(d_1)\frac{\partial d_1}{\partial S} - Ke^{-r\tau}N'(d_2)\frac{\partial d_2}{\partial S}
\]

Since \(\frac{\partial d_1}{\partial S} = \frac{\partial d_2}{\partial S} = \frac{1}{S\sigma\sqrt{\tau}}\):

\[
\frac{\partial C}{\partial S} = N(d_1) + \frac{N'(d_1)}{\sigma\sqrt{\tau}} - \frac{Ke^{-r\tau}N'(d_2)}{S\sigma\sqrt{\tau}}
\]

Using the identity \(SN'(d_1) = Ke^{-r\tau}N'(d_2)\), the last two terms cancel:

\[
\boxed{\Delta_{\text{call}} = N(d_1)}
\]

- **Call**:
\[
\Delta_{\text{call}} = N(d_1)
\]

- **Put** (by put-call parity \(P = C - S + Ke^{-r\tau}\)):
\[
\Delta_{\text{put}} = N(d_1)-1 = -N(-d_1)
\]

Delta lies in \((0,1)\) for calls and \((-1,0)\) for puts.

---

## Gamma


\[
\Gamma := \frac{\partial^2 V}{\partial S^2}
\]

**Derivation.** Differentiate \(\Delta_{\text{call}} = N(d_1)\) with respect to \(S\):

\[
\Gamma = N'(d_1)\frac{\partial d_1}{\partial S} = N'(d_1) \cdot \frac{1}{S\sigma\sqrt{\tau}}
\]

For both calls and puts,

\[
\boxed{\Gamma = \frac{N'(d_1)}{S\,\sigma\sqrt{\tau}}}
\]

Gamma is always positive (convexity in \(S\)) and becomes large near maturity (small \(\tau\)). Note that \(\Gamma_{\text{call}} = \Gamma_{\text{put}}\) since they differ by a linear function of \(S\).

---

## Vega


\[
\nu := \frac{\partial V}{\partial \sigma}
\]

**Derivation for a call.** Differentiate \(C = SN(d_1) - Ke^{-r\tau}N(d_2)\) with respect to \(\sigma\):

\[
\frac{\partial C}{\partial \sigma} = SN'(d_1)\frac{\partial d_1}{\partial \sigma} - Ke^{-r\tau}N'(d_2)\frac{\partial d_2}{\partial \sigma}
\]

Using \(\frac{\partial d_1}{\partial \sigma} = -\frac{d_2}{\sigma}\) and \(\frac{\partial d_2}{\partial \sigma} = -\frac{d_1}{\sigma}\):

\[
\nu = -\frac{SN'(d_1)d_2}{\sigma} + \frac{Ke^{-r\tau}N'(d_2)d_1}{\sigma}
\]

Using \(SN'(d_1) = Ke^{-r\tau}N'(d_2)\) and \(d_1 - d_2 = \sigma\sqrt{\tau}\):

\[
\nu = \frac{SN'(d_1)}{\sigma}(d_1 - d_2) = SN'(d_1) \cdot \sqrt{\tau}
\]

For both calls and puts,

\[
\boxed{\nu = S\sqrt{\tau}\,N'(d_1)}
\]

Vega is typically largest near-the-money and for moderate maturities.

---

## Theta


\[
\Theta := \frac{\partial V}{\partial t}
\]

> **Convention.** Some texts define theta as \(-\partial_t V\) (time-to-maturity derivative).  
> Here we use **calendar-time theta** \(\Theta=\partial_t V\). Since \(\tau = T - t\), we have \(\frac{\partial}{\partial t} = -\frac{\partial}{\partial \tau}\).

**Derivation for a call.** Using the Black–Scholes PDE:

\[
\Theta = -\frac{1}{2}\sigma^2 S^2 \Gamma - rS\Delta + rV
\]

Substituting the explicit forms:

\[
\Theta_{\text{call}} = -\frac{S\sigma N'(d_1)}{2\sqrt{\tau}} - rKe^{-r\tau}N(d_2)
\]

- **Call**:
\[
\Theta_{\text{call}}
= -\frac{S\sigma N'(d_1)}{2\sqrt{\tau}} - rK e^{-r\tau}N(d_2)
\]

- **Put**:
\[
\Theta_{\text{put}}
= -\frac{S\sigma N'(d_1)}{2\sqrt{\tau}} + rK e^{-r\tau}N(-d_2)
\]

Theta is typically negative (time decay), with exceptions in certain regimes (e.g., deep ITM puts where the interest earned on the strike exceeds time decay).

---

## Rho


\[
\rho := \frac{\partial V}{\partial r}
\]

**Derivation for a call.** Differentiate \(C = SN(d_1) - Ke^{-r\tau}N(d_2)\) with respect to \(r\):

\[
\frac{\partial C}{\partial r} = SN'(d_1)\frac{\partial d_1}{\partial r} + K\tau e^{-r\tau}N(d_2) - Ke^{-r\tau}N'(d_2)\frac{\partial d_2}{\partial r}
\]

Since \(\frac{\partial d_1}{\partial r} = \frac{\partial d_2}{\partial r} = \frac{\sqrt{\tau}}{\sigma}\), the terms involving \(N'\) cancel:

\[
\boxed{\rho_{\text{call}} = K\tau e^{-r\tau}N(d_2)}
\]

- **Call**:
\[
\rho_{\text{call}} = K\tau e^{-r\tau}N(d_2)
\]

- **Put**:
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

---

## Detailed Derivations from First Principles

### Delta Derivation

The delta of a European call option measures the rate of change of the call price with respect to the underlying stock price.

Starting from the Black–Scholes call formula:
\[
C = S N(d_1) - Ke^{-r\tau} N(d_2)
\]

Differentiate with respect to \(S\):
\[
\frac{\partial C}{\partial S} = N(d_1) + S N'(d_1) \frac{\partial d_1}{\partial S} - Ke^{-r\tau} N'(d_2) \frac{\partial d_2}{\partial S}
\]

Since both \(\frac{\partial d_1}{\partial S}\) and \(\frac{\partial d_2}{\partial S}\) equal \(\frac{1}{S\sigma\sqrt{\tau}}\), and using the key identity \(S N'(d_1) = Ke^{-r\tau} N'(d_2)\), the derivative terms simplify:

\[
\frac{\partial C}{\partial S} = N(d_1) + \frac{N'(d_1)}{\sigma\sqrt{\tau}} - \frac{Ke^{-r\tau}N'(d_2)}{S\sigma\sqrt{\tau}} = N(d_1)
\]

Thus, the delta of a call simplifies to the probability that the option finishes in-the-money under the risk-neutral measure.

### Gamma Derivation

Gamma measures the second-order sensitivity to price changes, representing the convexity (curvature) of the option value.

Differentiate the call delta \(\Delta = N(d_1)\) with respect to \(S\):

\[
\Gamma = \frac{\partial^2 C}{\partial S^2} = \frac{\partial N(d_1)}{\partial S} = N'(d_1) \frac{\partial d_1}{\partial S}
\]

Substituting \(\frac{\partial d_1}{\partial S} = \frac{1}{S\sigma\sqrt{\tau}}\):

\[
\Gamma = \frac{1}{\sqrt{2\pi}} e^{-d_1^2/2} \cdot \frac{1}{S\sigma\sqrt{\tau}}
\]

**Peak of Gamma.** Setting \(\frac{\partial^2 \Gamma}{\partial S^2} = 0\), we find that gamma is maximized when:
\[
d_1 = -\sigma\sqrt{\tau} \quad \Rightarrow \quad S = Ke^{-rT} \exp\left(-\frac{3}{2}\sigma^2\tau\right)
\]

This shows that gamma is largest for at-the-money options and decreases away from the strike.

### Vega Derivation

Vega measures sensitivity to changes in volatility, the sole parameter in Black–Scholes subject to estimation error.

Differentiate the call price with respect to \(\sigma\):

\[
\frac{\partial C}{\partial \sigma} = S N'(d_1) \frac{\partial d_1}{\partial \sigma} - Ke^{-r\tau} N'(d_2) \frac{\partial d_2}{\partial \sigma}
\]

Using \(\frac{\partial d_1}{\partial \sigma} = -\frac{d_2}{\sigma}\) and \(\frac{\partial d_2}{\partial \sigma} = -\frac{d_1}{\sigma}\):

\[
\nu = -\frac{SN'(d_1)d_2}{\sigma} + \frac{Ke^{-r\tau}N'(d_2)d_1}{\sigma}
\]

With the identity \(SN'(d_1) = Ke^{-r\tau}N'(d_2)\) and \(d_1 - d_2 = \sigma\sqrt{\tau}\):

\[
\nu = \frac{SN'(d_1)}{\sigma}(d_1 - d_2) = SN'(d_1)\sqrt{\tau}
\]

Vega is always positive, indicating that option values increase with volatility, and is typically largest near-the-money.

---

## Higher-Order Greeks


For completeness, we present three commonly used second-order cross-Greeks:

**Charm** (delta decay):
\[
\text{Charm} := \frac{\partial \Delta}{\partial \tau} = -\frac{\partial \Delta}{\partial t}
\]

For a call:
\[
\text{Charm}_{\text{call}} = -N'(d_1)\left(\frac{2(r-q)\tau - d_2\sigma\sqrt{\tau}}{2\tau\sigma\sqrt{\tau}}\right)
\]

where \(q\) is the dividend yield (set \(q=0\) for non-dividend-paying stocks). Charm measures how delta changes as time passes.

**Vanna** (delta-vol sensitivity):
\[
\text{Vanna} := \frac{\partial \Delta}{\partial \sigma} = \frac{\partial \nu}{\partial S}
\]

\[
\boxed{\text{Vanna} = -\frac{N'(d_1)d_2}{\sigma} = \frac{\nu}{S}\left(1 - \frac{d_1}{\sigma\sqrt{\tau}}\right)}
\]

Vanna measures how delta changes with volatility, or equivalently how vega changes with spot.

**Volga** (vega convexity):
\[
\text{Volga} := \frac{\partial^2 V}{\partial \sigma^2} = \frac{\partial \nu}{\partial \sigma}
\]

\[
\boxed{\text{Volga} = \nu \cdot \frac{d_1 d_2}{\sigma}}
\]

Volga is important for volatility surface dynamics and smile risk management. Long volga positions benefit from volatility-of-volatility.

> **Forward reference.** These higher-order Greeks become central in **Chapter 7** (Implied Volatility) for understanding smile dynamics, and in **Chapter 9** (Stochastic Volatility) for analyzing model risk.
