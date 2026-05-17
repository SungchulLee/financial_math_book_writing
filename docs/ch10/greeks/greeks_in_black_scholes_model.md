# Greeks in the Black–Scholes Model


Recall (see [§ Delta, Gamma, Vega, Theta, Rho](delta_gamma_vega_theta_rho.md)): Greeks are partial derivatives of the pricing map $V(t,S;\sigma,r,\dots)$. We now **specialize these definitions to the Black–Scholes model** and compute the Greeks explicitly from the closed-form European call/put formulas.

Recall (see [§ Black–Scholes formula](../../ch06/black_scholes_formula/bs_formula_statement.md)): $C = SN(d_1) - Ke^{-r\tau}N(d_2)$ — this section differentiates that formula.

---

## Notation and Black–Scholes parameters


Let

- $S$: current underlying price (at time $t$)
- $K$: strike
- $r$: constant risk-free rate
- $\sigma$: volatility
- $T$: maturity
- $t$: current time
- $\tau := T-t$: time to maturity
- $N(\cdot)$: standard normal CDF
- $N'(x) = \dfrac{1}{\sqrt{2\pi}}e^{-x^2/2}$: standard normal PDF

Define

$$
d_1 = \frac{\ln(S/K) + \left(r+\tfrac12\sigma^2\right)\tau}{\sigma\sqrt{\tau}},
\qquad
d_2 = d_1 - \sigma\sqrt{\tau}
$$

The Black–Scholes prices are

$$
C = S N(d_1) - K e^{-r\tau}N(d_2),
\qquad
P = K e^{-r\tau}N(-d_2) - S N(-d_1)
$$

---

## Preliminary: Derivatives of d₁ and d₂


Before computing Greeks, we establish the key derivatives:

$$
\frac{\partial d_1}{\partial S} = \frac{1}{S\sigma\sqrt{\tau}},
\qquad
\frac{\partial d_2}{\partial S} = \frac{\partial d_1}{\partial S} = \frac{1}{S\sigma\sqrt{\tau}}
$$

$$
\frac{\partial d_1}{\partial \sigma} = -\frac{d_2}{\sigma},
\qquad
\frac{\partial d_2}{\partial \sigma} = -\frac{d_1}{\sigma}
$$

$$
\frac{\partial d_1}{\partial \tau} = -\frac{d_2}{2\tau},
\qquad
\frac{\partial d_2}{\partial \tau} = -\frac{d_1}{2\tau}
$$

A crucial identity linking $N'(d_1)$ and $N'(d_2)$:

$$
\boxed{S N'(d_1) = K e^{-r\tau} N'(d_2)}
$$

**Proof.** Since $d_1 - d_2 = \sigma\sqrt{\tau}$, we have

$$
\frac{N'(d_1)}{N'(d_2)} = \exp\!\left(-\frac{d_1^2 - d_2^2}{2}\right)
= \exp\!\left(-\frac{(d_1-d_2)(d_1+d_2)}{2}\right)
$$

Now $d_1 + d_2 = 2d_1 - \sigma\sqrt{\tau}$, and using $d_1 = \frac{\ln(S/K) + (r + \frac12\sigma^2)\tau}{\sigma\sqrt{\tau}}$:

$$
\frac{d_1^2 - d_2^2}{2} = \frac{\sigma\sqrt{\tau}(d_1 + d_2)}{2} = \ln(S/K) + r\tau
$$

Thus $\frac{N'(d_1)}{N'(d_2)} = \frac{K e^{-r\tau}}{S}$, giving $S N'(d_1) = K e^{-r\tau} N'(d_2)$. $\square$

---

## Delta


$$
\Delta := \frac{\partial V}{\partial S}
$$

**Derivation for a call.** Differentiate $C = SN(d_1) - Ke^{-r\tau}N(d_2)$ with respect to $S$:

$$
\frac{\partial C}{\partial S} = N(d_1) + S N'(d_1)\frac{\partial d_1}{\partial S} - Ke^{-r\tau}N'(d_2)\frac{\partial d_2}{\partial S}
$$

Since $\frac{\partial d_1}{\partial S} = \frac{\partial d_2}{\partial S} = \frac{1}{S\sigma\sqrt{\tau}}$:

$$
\frac{\partial C}{\partial S} = N(d_1) + \frac{N'(d_1)}{\sigma\sqrt{\tau}} - \frac{Ke^{-r\tau}N'(d_2)}{S\sigma\sqrt{\tau}}
$$

Using the identity $SN'(d_1) = Ke^{-r\tau}N'(d_2)$, the last two terms cancel:

$$
\boxed{\Delta_{\text{call}} = N(d_1)}
$$

- **Call**:

$$
\Delta_{\text{call}} = N(d_1)
$$

- **Put** (by put-call parity $P = C - S + Ke^{-r\tau}$):

$$
\Delta_{\text{put}} = N(d_1)-1 = -N(-d_1)
$$

Delta lies in $(0,1)$ for calls and $(-1,0)$ for puts.

---

## Gamma


$$
\Gamma := \frac{\partial^2 V}{\partial S^2}
$$

**Derivation.** Differentiate $\Delta_{\text{call}} = N(d_1)$ with respect to $S$:

$$
\Gamma = N'(d_1)\frac{\partial d_1}{\partial S} = N'(d_1) \cdot \frac{1}{S\sigma\sqrt{\tau}}
$$

For both calls and puts,

$$
\boxed{\Gamma = \frac{N'(d_1)}{S\,\sigma\sqrt{\tau}}}
$$

Gamma is always positive (convexity in $S$) and becomes large near maturity (small $\tau$). Note that $\Gamma_{\text{call}} = \Gamma_{\text{put}}$ since they differ by a linear function of $S$.

---

## Vega


$$
\nu := \frac{\partial V}{\partial \sigma}
$$

**Derivation for a call.** Differentiate $C = SN(d_1) - Ke^{-r\tau}N(d_2)$ with respect to $\sigma$:

$$
\frac{\partial C}{\partial \sigma} = SN'(d_1)\frac{\partial d_1}{\partial \sigma} - Ke^{-r\tau}N'(d_2)\frac{\partial d_2}{\partial \sigma}
$$

Using $\frac{\partial d_1}{\partial \sigma} = -\frac{d_2}{\sigma}$ and $\frac{\partial d_2}{\partial \sigma} = -\frac{d_1}{\sigma}$:

$$
\nu = -\frac{SN'(d_1)d_2}{\sigma} + \frac{Ke^{-r\tau}N'(d_2)d_1}{\sigma}
$$

Using $SN'(d_1) = Ke^{-r\tau}N'(d_2)$ and $d_1 - d_2 = \sigma\sqrt{\tau}$:

$$
\nu = \frac{SN'(d_1)}{\sigma}(d_1 - d_2) = SN'(d_1) \cdot \sqrt{\tau}
$$

For both calls and puts,

$$
\boxed{\nu = S\sqrt{\tau}\,N'(d_1)}
$$

Vega is typically largest near-the-money and for moderate maturities.

---

## Theta


$$
\Theta := \frac{\partial V}{\partial t}
$$

> **Convention.** Some texts define theta as $-\partial_t V$ (time-to-maturity derivative).  
> Here we use **calendar-time theta** $\Theta=\partial_t V$. Since $\tau = T - t$, we have $\frac{\partial}{\partial t} = -\frac{\partial}{\partial \tau}$.

**Derivation for a call.** Recall (see [§ BS PDE structure](../../ch06/bs_pde_structure/discounting_and_killing_term.md)): from the Black–Scholes PDE,

$$
\Theta = -\frac{1}{2}\sigma^2 S^2 \Gamma - rS\Delta + rV
$$

Substituting the explicit forms:

$$
\Theta_{\text{call}} = -\frac{S\sigma N'(d_1)}{2\sqrt{\tau}} - rKe^{-r\tau}N(d_2)
$$

- **Call**:

$$
\Theta_{\text{call}}
= -\frac{S\sigma N'(d_1)}{2\sqrt{\tau}} - rK e^{-r\tau}N(d_2)
$$

- **Put**:

$$
\Theta_{\text{put}}
= -\frac{S\sigma N'(d_1)}{2\sqrt{\tau}} + rK e^{-r\tau}N(-d_2)
$$

Theta is typically negative (time decay), with exceptions in certain regimes (e.g., deep ITM puts where the interest earned on the strike exceeds time decay).

---

## Rho


$$
\rho := \frac{\partial V}{\partial r}
$$

**Derivation for a call.** Differentiate $C = SN(d_1) - Ke^{-r\tau}N(d_2)$ with respect to $r$:

$$
\frac{\partial C}{\partial r} = SN'(d_1)\frac{\partial d_1}{\partial r} + K\tau e^{-r\tau}N(d_2) - Ke^{-r\tau}N'(d_2)\frac{\partial d_2}{\partial r}
$$

Since $\frac{\partial d_1}{\partial r} = \frac{\partial d_2}{\partial r} = \frac{\sqrt{\tau}}{\sigma}$, the terms involving $N'$ cancel:

$$
\boxed{\rho_{\text{call}} = K\tau e^{-r\tau}N(d_2)}
$$

- **Call**:

$$
\rho_{\text{call}} = K\tau e^{-r\tau}N(d_2)
$$

- **Put**:

$$
\rho_{\text{put}} = -K\tau e^{-r\tau}N(-d_2)
$$

Rho reflects the present-value effect of the strike and is usually small for short maturities.

---

## Symmetries and notes


- **Gamma** and **Vega** are identical for calls and puts: they depend on the diffusion of $S$, not the payoff direction.
- **Delta**, **Theta**, and **Rho** differ between calls and puts due to payoff asymmetry and the discounting term.
- All expressions above follow by differentiating the Black–Scholes closed forms for $C$ and $P$.

---

## Conceptual interpretation (typical signs)


| Greek  | Meaning                                  | Call sign | Put sign |
|-------:|------------------------------------------|:---------:|:--------:|
| Delta  | price change per unit $S$              | $>0$    | $<0$   |
| Gamma  | convexity / rate of change of Delta      | $>0$    | $>0$   |
| Theta  | calendar-time decay                       | usually $<0$ | usually $<0$ |
| Vega   | sensitivity to volatility                | $>0$    | $>0$   |
| Rho    | sensitivity to interest rate             | $>0$    | $<0$   |

---

## Summary


This section shows how the abstract Greeks reduce, in the Black–Scholes model, to explicit closed-form expressions. These formulas are the baseline for practical risk management, hedging, and calibration, and they also highlight where Black–Scholes is too restrictive (e.g., constant $\sigma$ across strikes/maturities).

---

## Higher-Order Greeks


For completeness, we present three commonly used second-order cross-Greeks:

**Charm** (delta decay):

$$
\text{Charm} := \frac{\partial \Delta}{\partial \tau} = -\frac{\partial \Delta}{\partial t}
$$

For a call:

$$
\text{Charm}_{\text{call}} = -N'(d_1)\left(\frac{2(r-q)\tau - d_2\sigma\sqrt{\tau}}{2\tau\sigma\sqrt{\tau}}\right)
$$

where $q$ is the dividend yield (set $q=0$ for non-dividend-paying stocks). Charm measures how delta changes as time passes.

**Vanna** (delta-vol sensitivity):

$$
\text{Vanna} := \frac{\partial \Delta}{\partial \sigma} = \frac{\partial \nu}{\partial S}
$$

$$
\boxed{\text{Vanna} = -\frac{N'(d_1)d_2}{\sigma} = \frac{\nu}{S}\left(1 - \frac{d_1}{\sigma\sqrt{\tau}}\right)}
$$

Vanna measures how delta changes with volatility, or equivalently how vega changes with spot.

**Volga** (vega convexity):

$$
\text{Volga} := \frac{\partial^2 V}{\partial \sigma^2} = \frac{\partial \nu}{\partial \sigma}
$$

$$
\boxed{\text{Volga} = \nu \cdot \frac{d_1 d_2}{\sigma}}
$$

Volga is important for volatility surface dynamics and smile risk management. Long volga positions benefit from volatility-of-volatility.

> **Forward reference.** Deferred — see [§ Vega and the smile](../../ch12/implied_volatility_sensitivities/vega_and_implied_volatility_sensitivity.md) for the role of vanna/volga in smile dynamics, and [§ Greek asymptotics](../greeks_asympt/blow_up_of_gamma_near_expiry.md) for limiting behavior.

---

## Exercises

**Exercise 1.** Using the identity $SN'(d_1) = Ke^{-r\tau}N'(d_2)$, verify that vega is the same for a European call and a European put by directly computing $\partial P / \partial \sigma$ from the put formula $P = Ke^{-r\tau}N(-d_2) - SN(-d_1)$.

??? success "Solution to Exercise 1"
    The put formula is $P = Ke^{-r\tau}N(-d_2) - SN(-d_1)$. Differentiate with respect to $\sigma$:

    $$
    \frac{\partial P}{\partial \sigma} = Ke^{-r\tau}N'(-d_2)\frac{\partial(-d_2)}{\partial \sigma} - SN'(-d_1)\frac{\partial(-d_1)}{\partial \sigma}
    $$

    Since $N'(-x) = N'(x)$ (the standard normal PDF is symmetric), this becomes:

    $$
    \frac{\partial P}{\partial \sigma} = -Ke^{-r\tau}N'(d_2)\frac{\partial d_2}{\partial \sigma} + SN'(d_1)\frac{\partial d_1}{\partial \sigma}
    $$

    Using $\frac{\partial d_1}{\partial \sigma} = -\frac{d_2}{\sigma}$ and $\frac{\partial d_2}{\partial \sigma} = -\frac{d_1}{\sigma}$:

    $$
    \frac{\partial P}{\partial \sigma} = \frac{Ke^{-r\tau}N'(d_2)d_1}{\sigma} - \frac{SN'(d_1)d_2}{\sigma}
    $$

    Applying the identity $SN'(d_1) = Ke^{-r\tau}N'(d_2)$:

    $$
    \frac{\partial P}{\partial \sigma} = \frac{SN'(d_1)d_1}{\sigma} - \frac{SN'(d_1)d_2}{\sigma} = \frac{SN'(d_1)(d_1 - d_2)}{\sigma} = \frac{SN'(d_1)\sigma\sqrt{\tau}}{\sigma} = SN'(d_1)\sqrt{\tau}
    $$

    This equals the call vega $\nu = S\sqrt{\tau}\,N'(d_1)$, confirming that $\nu_{\text{call}} = \nu_{\text{put}}$.

---

**Exercise 2.** For a European call with $S = 100$, $K = 105$, $\tau = 0.5$, $r = 0.03$, $\sigma = 0.25$, compute $d_1$, $d_2$, and all five Greeks: $\Delta$, $\Gamma$, $\nu$, $\Theta$, $\rho$. Verify the theta-gamma identity $\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma + rS\Delta - rC = 0$.

??? success "Solution to Exercise 2"
    **Given:** $S = 100$, $K = 105$, $\tau = 0.5$, $r = 0.03$, $\sigma = 0.25$.

    **Step 1: Compute $d_1$ and $d_2$.**

    $$
    d_1 = \frac{\ln(100/105) + (0.03 + \frac{1}{2}(0.0625))(0.5)}{0.25\sqrt{0.5}} = \frac{-0.04879 + 0.03063}{0.17678} = \frac{-0.01817}{0.17678} = -0.10278
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{\tau} = -0.10278 - 0.17678 = -0.27956
    $$

    **Step 2: Evaluate the normal CDF and PDF.**

    $N(d_1) = N(-0.10278) \approx 0.4591$, $N(d_2) = N(-0.27956) \approx 0.3899$, $N'(d_1) = \frac{1}{\sqrt{2\pi}}e^{-d_1^2/2} \approx 0.3970$.

    **Step 3: Compute Greeks.**

    - $\Delta = N(d_1) \approx 0.4591$
    - $\Gamma = \frac{N'(d_1)}{S\sigma\sqrt{\tau}} = \frac{0.3970}{100 \times 0.17678} \approx 0.02246$
    - $\nu = S\sqrt{\tau}\,N'(d_1) = 100 \times 0.7071 \times 0.3970 \approx 28.07$
    - $\Theta = -\frac{S\sigma N'(d_1)}{2\sqrt{\tau}} - rKe^{-r\tau}N(d_2) = -\frac{100 \times 0.25 \times 0.3970}{2 \times 0.7071} - 0.03 \times 105 \times e^{-0.015} \times 0.3899$

        Computing each term: first term $= -\frac{9.925}{1.4142} = -7.019$; second term $= -0.03 \times 103.43 \times 0.3899 = -1.210$.

        $\Theta \approx -7.019 - 1.210 = -8.229$

    - $\rho = K\tau e^{-r\tau}N(d_2) = 105 \times 0.5 \times e^{-0.015} \times 0.3899 \approx 52.5 \times 0.9851 \times 0.3899 \approx 20.16$

    **Step 4: Verify the theta-gamma identity.** The call price is:

    $$
    C = SN(d_1) - Ke^{-r\tau}N(d_2) = 100 \times 0.4591 - 103.43 \times 0.3899 \approx 45.91 - 40.33 = 5.58
    $$

    Check $\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma + rS\Delta - rC$:

    $$
    -8.229 + \frac{1}{2}(0.0625)(10000)(0.02246) + 0.03(100)(0.4591) - 0.03(5.58)
    $$

    $$
    = -8.229 + 7.019 + 1.377 - 0.167 = 0.000
    $$

    The identity is verified (up to rounding).

---

**Exercise 3.** Prove that the peak of gamma occurs near $S = K$ for short maturities by setting $d_1 = 0$ and solving for $S$ in terms of $K$, $r$, $\sigma$, and $\tau$. Show that as $\tau \to 0$, the peak location converges to $S = K$.

??? success "Solution to Exercise 3"
    The gamma is:

    $$
    \Gamma = \frac{N'(d_1)}{S\sigma\sqrt{\tau}}
    $$

    Since $N'(d_1) = \frac{1}{\sqrt{2\pi}}e^{-d_1^2/2}$ is maximized when $d_1 = 0$, the peak of gamma (as a function of $S$) occurs approximately when $d_1 = 0$.

    Setting $d_1 = 0$:

    $$
    \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}} = 0
    $$

    Solving for $S$:

    $$
    \ln(S/K) = -(r + \tfrac{1}{2}\sigma^2)\tau
    $$

    $$
    S^* = K\exp\!\left(-(r + \tfrac{1}{2}\sigma^2)\tau\right)
    $$

    As $\tau \to 0$:

    $$
    S^* = K\exp\!\left(-(r + \tfrac{1}{2}\sigma^2)\tau\right) \to K \cdot e^0 = K
    $$

    Therefore the peak of gamma converges to $S = K$ as maturity approaches. For small $\tau$, the peak is slightly below $K$ (since the exponent is negative), but the deviation is of order $\tau$ and vanishes at expiration.

    Note: the precise maximum of $\Gamma(S)$ for fixed $\tau$ requires differentiating $\Gamma$ with respect to $S$ and solving $\frac{\partial\Gamma}{\partial S} = 0$, which gives a slightly different condition ($d_1 = \sigma\sqrt{\tau}$ rather than $d_1 = 0$). However, this distinction also vanishes as $\tau \to 0$, and the conclusion $S^* \to K$ is the same.

---

**Exercise 4.** Using the closed-form expression for charm,

$$
\text{Charm}_{\text{call}} = -N'(d_1)\left(\frac{2(r-q)\tau - d_2\sigma\sqrt{\tau}}{2\tau\sigma\sqrt{\tau}}\right)
$$

with $q = 0$, compute the rate at which delta changes over one day for an ATM call with $S = K = 100$, $\sigma = 0.20$, $r = 0.05$, $\tau = 30/365$. Interpret the sign of charm in terms of the hedger's rebalancing needs.

??? success "Solution to Exercise 4"
    **Given:** $S = K = 100$, $\sigma = 0.20$, $r = 0.05$, $\tau = 30/365 \approx 0.08219$, $q = 0$.

    **Step 1: Compute $d_1$ and $d_2$.**

    For ATM ($S = K$):

    $$
    d_1 = \frac{\ln(1) + (0.05 + 0.02)(0.08219)}{0.20\sqrt{0.08219}} = \frac{0 + 0.005753}{0.05733} = 0.10035
    $$

    $$
    d_2 = d_1 - 0.05733 = 0.04302
    $$

    **Step 2: Compute $N'(d_1)$.**

    $$
    N'(d_1) = \frac{1}{\sqrt{2\pi}}e^{-d_1^2/2} = \frac{1}{\sqrt{2\pi}}e^{-0.005035} \approx 0.3987
    $$

    **Step 3: Compute charm.**

    $$
    \text{Charm}_{\text{call}} = -N'(d_1)\left(\frac{2r\tau - d_2\sigma\sqrt{\tau}}{2\tau\sigma\sqrt{\tau}}\right)
    $$

    Numerator of the fraction: $2(0.05)(0.08219) - (0.04302)(0.20)(0.28669) = 0.008219 - 0.002467 = 0.005752$.

    Denominator: $2(0.08219)(0.20)(0.28669) = 0.009413$.

    $$
    \text{Charm}_{\text{call}} = -0.3987 \times \frac{0.005752}{0.009413} = -0.3987 \times 0.6112 = -0.2437
    $$

    **Step 4: Rate of delta change over one day.** One day corresponds to $\delta\tau = -1/365$ (time to maturity decreases). Since charm is defined as $-\partial\Delta/\partial t = \partial\Delta/\partial\tau$:

    $$
    \delta\Delta \approx \text{Charm} \times \delta\tau = -0.2437 \times \frac{1}{365} \approx -0.000668
    $$

    Wait -- we must be careful with signs. Charm $= \partial\Delta/\partial\tau = -\partial\Delta/\partial t$. As one day passes, $t$ increases by $1/365$, so:

    $$
    \delta\Delta \approx \frac{\partial\Delta}{\partial t}\delta t = -\text{Charm} \times \frac{1}{365} = 0.2437 \times \frac{1}{365} \approx 0.000668
    $$

    **Interpretation.** The positive sign means delta increases slightly as time passes (for this near-ATM call). This is because an ATM call with $d_1 > 0$ sees its delta pushed toward $0.5$ more decisively as the diffusion narrows with less time remaining. The hedger must buy approximately $0.067$ additional delta-units per 100 shares per day to stay hedged.

---

**Exercise 5.** Show that volga $= \nu \cdot d_1 d_2 / \sigma$ is negative for options that are near-the-money (where $d_1 > 0$ and $d_2 < 0$) and positive for options that are sufficiently far from the money. At what moneyness does volga change sign?

??? success "Solution to Exercise 5"
    Volga is given by:

    $$
    \text{Volga} = \nu \cdot \frac{d_1 d_2}{\sigma}
    $$

    Since $\nu = S\sqrt{\tau}\,N'(d_1) > 0$ and $\sigma > 0$, the sign of volga is determined by the sign of $d_1 d_2$.

    Recall $d_2 = d_1 - \sigma\sqrt{\tau}$. For near-the-money options, $d_1 \approx \frac{1}{2}\sigma\sqrt{\tau} > 0$ (slightly positive for ATM), so:

    $$
    d_2 \approx d_1 - \sigma\sqrt{\tau} \approx -\frac{1}{2}\sigma\sqrt{\tau} < 0
    $$

    Therefore $d_1 > 0$ and $d_2 < 0$, giving $d_1 d_2 < 0$, and **volga is negative** for near-the-money options.

    **Volga changes sign** when either $d_1 = 0$ or $d_2 = 0$:

    - $d_2 = 0$ when $d_1 = \sigma\sqrt{\tau}$, i.e., $\ln(S/K) + (r + \frac{1}{2}\sigma^2)\tau = \sigma^2\tau$, giving $S = K\exp\!\left((\frac{1}{2}\sigma^2 - r)\tau\right)$.
    - $d_1 = 0$ when $S = K\exp\!\left(-(r + \frac{1}{2}\sigma^2)\tau\right)$.

    For sufficiently far OTM or ITM options, both $d_1$ and $d_2$ have the same sign (both positive deep ITM, both negative deep OTM), making $d_1 d_2 > 0$ and **volga positive**.

    In summary, volga is negative in a band around the money where $d_1$ and $d_2$ have opposite signs, and positive outside this band.

---

**Exercise 6.** Using put-call parity $P = C - S + Ke^{-r\tau}$, derive the put formulas for $\Delta_{\text{put}}$, $\Theta_{\text{put}}$, and $\rho_{\text{put}}$ from the corresponding call formulas without differentiating the put pricing formula directly.

??? success "Solution to Exercise 6"
    Starting from put-call parity: $P = C - S + Ke^{-r\tau}$.

    **Put delta.** Differentiate with respect to $S$:

    $$
    \Delta_{\text{put}} = \frac{\partial P}{\partial S} = \frac{\partial C}{\partial S} - 1 = \Delta_{\text{call}} - 1 = N(d_1) - 1 = -N(-d_1)
    $$

    **Put theta.** Differentiate with respect to $t$ (using $\frac{\partial\tau}{\partial t} = -1$):

    $$
    \Theta_{\text{put}} = \frac{\partial P}{\partial t} = \frac{\partial C}{\partial t} - 0 + \frac{\partial}{\partial t}\!\left(Ke^{-r\tau}\right)
    $$

    Since $\frac{\partial}{\partial t}(Ke^{-r(T-t)}) = rKe^{-r\tau}$:

    $$
    \Theta_{\text{put}} = \Theta_{\text{call}} + rKe^{-r\tau}
    $$

    Substituting $\Theta_{\text{call}} = -\frac{S\sigma N'(d_1)}{2\sqrt{\tau}} - rKe^{-r\tau}N(d_2)$:

    $$
    \Theta_{\text{put}} = -\frac{S\sigma N'(d_1)}{2\sqrt{\tau}} - rKe^{-r\tau}N(d_2) + rKe^{-r\tau}
    $$

    $$
    = -\frac{S\sigma N'(d_1)}{2\sqrt{\tau}} + rKe^{-r\tau}(1 - N(d_2))
    $$

    $$
    = -\frac{S\sigma N'(d_1)}{2\sqrt{\tau}} + rKe^{-r\tau}N(-d_2)
    $$

    **Put rho.** Differentiate with respect to $r$:

    $$
    \rho_{\text{put}} = \frac{\partial P}{\partial r} = \frac{\partial C}{\partial r} + \frac{\partial}{\partial r}\!\left(Ke^{-r\tau}\right) = \rho_{\text{call}} - K\tau e^{-r\tau}
    $$

    Substituting $\rho_{\text{call}} = K\tau e^{-r\tau}N(d_2)$:

    $$
    \rho_{\text{put}} = K\tau e^{-r\tau}N(d_2) - K\tau e^{-r\tau} = -K\tau e^{-r\tau}(1 - N(d_2)) = -K\tau e^{-r\tau}N(-d_2)
    $$

    All three results match the standard Black-Scholes put Greek formulas.
