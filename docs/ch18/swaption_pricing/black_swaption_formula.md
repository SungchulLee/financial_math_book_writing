# Black Swaption Formula

!!! tip "Key Idea"
    The Black swaption formula follows from the same principle as Black-Scholes: choose the right numeraire so that the relevant underlying becomes a martingale, then price the option as a discounted expectation under the associated measure.

A European swaption is an option on a swap. For a payer swaption, the holder has the right at expiry $T_m$ to enter a swap that pays fixed rate $K$ and receives floating over the interval $[T_m, T_n]$.

The derivation rests on three facts:

1. The value of a payer swap is $\text{IRS}^{\text{Payer}}(t) = N A_{m,n}(t)(S_{m,n}(t) - K)$, where $A_{m,n}(t) = \sum_{k=m+1}^n \tau_k P(t, T_k)$ is the swap annuity and $S_{m,n}(t) = \frac{P(t,T_m) - P(t,T_n)}{A_{m,n}(t)}$ is the par swap rate.

2. The payoff of a payer swaption at expiry $T_m$ is $N A_{m,n}(T_m)(S_{m,n}(T_m) - K)^+$.

3. Under the annuity measure $\mathbb{Q}^A$, the swap rate $S_{m,n}(t)$ is a martingale.

These facts reduce swaption pricing to the pricing of an option on a martingale under an appropriate measure.

---

## Swaption Payoff

A payer swaption exercised at time $T_m$ gives the holder the value of entering the payer swap at strike $K$. Since the payer swap value at $T_m$ is

$$
\text{IRS}^{\text{Payer}}(T_m) = N A_{m,n}(T_m)(S_{m,n}(T_m) - K)
$$

the payer swaption payoff is

$$
V^{\text{pay}}(T_m) = N A_{m,n}(T_m)(S_{m,n}(T_m) - K)^+
$$

Similarly, the receiver swaption payoff is

$$
V^{\text{rec}}(T_m) = N A_{m,n}(T_m)(K - S_{m,n}(T_m))^+
$$

---

## Pricing Under the Annuity Measure

Let the annuity

$$
A_{m,n}(t) = \sum_{k=m+1}^n \tau_k P(t, T_k)
$$

serve as numeraire. The corresponding pricing measure is the **annuity measure** $\mathbb{Q}^A$.

Under this measure, the swap rate $S_{m,n}(t)$ is a martingale. Therefore, the time-$t$ value of the payer swaption is

$$
V^{\text{pay}}(t) = N A_{m,n}(t) \, \mathbb{E}^{\mathbb{Q}^A}\!\left[(S_{m,n}(T_m) - K)^+ \mid \mathcal{F}_t\right]
$$

This is the exact analogue of expressing an option price as numeraire times an expectation under the corresponding forward measure.

---

## Lognormal Assumption for the Swap Rate

To obtain a closed form, assume that under $\mathbb{Q}^A$, the swap rate follows a lognormal diffusion:

$$
dS_{m,n}(t) = \sigma_S S_{m,n}(t) \, dW_t^A, \qquad t \leq T_m
$$

where $\sigma_S$ is the swaption volatility. Because $S_{m,n}(t)$ is a martingale under $\mathbb{Q}^A$, there is **no drift term**. The solution is

$$
S_{m,n}(T_m) = S_{m,n}(t) \exp\!\left(-\frac{1}{2}\sigma_S^2(T_m - t) + \sigma_S\sqrt{T_m - t} \, Z\right)
$$

where $Z \sim \mathcal{N}(0,1)$ under $\mathbb{Q}^A$. Thus $\ln S_{m,n}(T_m)$ is normally distributed with mean $\ln S_{m,n}(t) - \frac{1}{2}\sigma_S^2(T_m - t)$ and variance $\sigma_S^2(T_m - t)$.

---

## Reduction to the Black Formula

We now compute

$$
\mathbb{E}^{\mathbb{Q}^A}\!\left[(S_{m,n}(T_m) - K)^+ \mid \mathcal{F}_t\right]
$$

This is exactly the same expectation that appears in the Black formula for an option on a forward price. Therefore,

$$
\mathbb{E}^{\mathbb{Q}^A}\!\left[(S_{m,n}(T_m) - K)^+ \mid \mathcal{F}_t\right] = S_{m,n}(t)\Phi(d_1) - K\Phi(d_2)
$$

where

$$
d_1 = \frac{\ln(S_{m,n}(t)/K) + \frac{1}{2}\sigma_S^2(T_m - t)}{\sigma_S\sqrt{T_m - t}}, \qquad d_2 = d_1 - \sigma_S\sqrt{T_m - t}
$$

and $\Phi$ is the standard normal cumulative distribution function.

Substituting back into the annuity-measure pricing formula gives the **Black payer swaption formula**:

$$
\boxed{V^{\text{pay}}(t) = N A_{m,n}(t)\left[S_{m,n}(t)\Phi(d_1) - K\Phi(d_2)\right]}
$$

---

## Receiver Swaption Formula

By the same argument, the receiver swaption value is

$$
\boxed{V^{\text{rec}}(t) = N A_{m,n}(t)\left[K\Phi(-d_2) - S_{m,n}(t)\Phi(-d_1)\right]}
$$

This is the put-version of the same Black formula.

---

## Interpretation

The formula has a clear structure:

- $S_{m,n}(t)$ plays the role of the underlying (analogous to the stock price in Black-Scholes)
- $K$ is the strike swap rate
- $A_{m,n}(t)$ plays the role of the discounting factor, but for the swap cash-flow stream rather than for a single maturity
- $\sigma_S$ is the volatility of the swap rate under the annuity measure

The Black swaption formula is not a separate theory from Black-Scholes. It is the same pricing logic applied to a different underlying and a different numeraire.

---

## Why the Annuity Measure is the Right One

Under the money-market measure, the swap rate generally has a nonzero drift. That makes direct option pricing cumbersome.

Under the annuity measure, however, the swap rate becomes a martingale, and the payoff

$$
N A_{m,n}(T_m)(S_{m,n}(T_m) - K)^+
$$

simplifies to annuity times a standard call payoff on a martingale. This is exactly why the Black formula emerges so cleanly.

The choice of numeraire is therefore not a technical trick but the key conceptual step that turns swaption pricing into a tractable problem.

---

## Payer-Receiver Parity

Using the identity $(x - K)^+ - (K - x)^+ = x - K$, we obtain

$$
V^{\text{pay}}(t) - V^{\text{rec}}(t) = N A_{m,n}(t)(S_{m,n}(t) - K)
$$

which is exactly the value of the underlying payer swap. This is the swaption analogue of put-call parity.

---

!!! note "Big Picture"
    The Black swaption formula is the interest-rate analogue of the Black formula for options on forwards. In Chapter 6, forward prices become martingales under a forward measure. In the swaption setting, swap rates become martingales under the annuity measure. In both cases, once the correct numeraire is chosen, the option price reduces to the expectation of a convex payoff under a lognormal martingale. The difference is not in the pricing principle, but in the object being modeled: a swap rate instead of a stock price.

---

## Exercises

**Exercise 1.** A 1-year into 5-year payer swaption has strike $K = 3\%$, swaption volatility $\sigma_S = 20\%$, current par swap rate $S_{m,n}(0) = 3.5\%$, and annuity factor $A_{m,n}(0) = 4.50$. The notional is $N = 10{,}000{,}000$. Compute $d_1$, $d_2$, and the swaption price.

??? success "Solution to Exercise 1"
    With $T_m = 1$, $S = 0.035$, $K = 0.03$, $\sigma_S = 0.20$:

    $$
    d_1 = \frac{\ln(0.035/0.03) + \frac{1}{2}(0.04)(1)}{0.20 \times 1} = \frac{\ln(1.1667) + 0.02}{0.20} = \frac{0.15415 + 0.02}{0.20} = \frac{0.17415}{0.20} = 0.8708
    $$

    $$
    d_2 = 0.8708 - 0.20 = 0.6708
    $$

    From normal tables: $\Phi(0.8708) \approx 0.8081$, $\Phi(0.6708) \approx 0.7488$.

    $$
    V^{\text{pay}} = 10{,}000{,}000 \times 4.50 \times [0.035 \times 0.8081 - 0.03 \times 0.7488]
    $$

    $$
    = 45{,}000{,}000 \times [0.028284 - 0.022464] = 45{,}000{,}000 \times 0.005820 = 261{,}900
    $$

    The payer swaption is worth approximately \$261,900.

---

**Exercise 2.** Using the same parameters as Exercise 1, compute the receiver swaption price. Verify payer-receiver parity: $V^{\text{pay}} - V^{\text{rec}} = N A_{m,n}(0)(S_{m,n}(0) - K)$.

??? success "Solution to Exercise 2"
    $$
    V^{\text{rec}} = N A_{m,n}(0)[K\Phi(-d_2) - S_{m,n}(0)\Phi(-d_1)]
    $$

    With $\Phi(-0.6708) = 1 - 0.7488 = 0.2512$ and $\Phi(-0.8708) = 1 - 0.8081 = 0.1919$:

    $$
    V^{\text{rec}} = 45{,}000{,}000 \times [0.03 \times 0.2512 - 0.035 \times 0.1919]
    $$

    $$
    = 45{,}000{,}000 \times [0.007536 - 0.006717] = 45{,}000{,}000 \times 0.000819 = 36{,}855
    $$

    **Parity check:**

    $$
    V^{\text{pay}} - V^{\text{rec}} = 261{,}900 - 36{,}855 = 225{,}045
    $$

    $$
    N A_{m,n}(0)(S - K) = 45{,}000{,}000 \times (0.035 - 0.03) = 45{,}000{,}000 \times 0.005 = 225{,}000
    $$

    The small difference is due to rounding. Parity holds. $\square$

---

**Exercise 3.** Explain why the swap rate $S_{m,n}(t)$ is a martingale under the annuity measure $\mathbb{Q}^A$ but not under the money-market measure $\mathbb{Q}$. What goes wrong if one tries to apply the Black formula directly under $\mathbb{Q}$?

??? success "Solution to Exercise 3"
    Under $\mathbb{Q}^A$, the numeraire is $A_{m,n}(t)$. The payer swap value divided by the numeraire is:

    $$
    \frac{\text{IRS}^{\text{Payer}}(t)}{A_{m,n}(t)} = N(S_{m,n}(t) - K)
    $$

    Since any traded asset divided by the numeraire is a $\mathbb{Q}^A$-martingale, and $K$ is constant, $S_{m,n}(t)$ is a $\mathbb{Q}^A$-martingale.

    Under the money-market measure $\mathbb{Q}$, the numeraire is the money-market account $M(t) = e^{\int_0^t r(s) ds}$. The swap rate divided by this numeraire has no reason to be driftless — in general, $S_{m,n}(t)$ will have a nonzero, state-dependent drift under $\mathbb{Q}$ because $A_{m,n}(t)/M(t)$ is stochastic when rates are random.

    If one tries to apply the Black formula under $\mathbb{Q}$, the swap rate is not a martingale, so the lognormal assumption $dS = \sigma S \, dW$ is inconsistent (the drift is missing). The resulting price would be incorrect unless the drift is explicitly modeled, which destroys the simplicity of the closed-form formula.

---

**Exercise 4.** An at-the-money payer swaption has $S_{m,n}(t) = K$. Show that $d_1 = \frac{1}{2}\sigma_S\sqrt{T_m - t}$ and $d_2 = -\frac{1}{2}\sigma_S\sqrt{T_m - t}$. Derive the ATM approximation $V^{\text{pay}} \approx N A_{m,n}(t) \cdot S_{m,n}(t) \cdot \frac{\sigma_S\sqrt{T_m - t}}{\sqrt{2\pi}}$ for small volatility-time product.

??? success "Solution to Exercise 4"
    When $S_{m,n}(t) = K$, $\ln(S/K) = 0$, so:

    $$
    d_1 = \frac{0 + \frac{1}{2}\sigma_S^2(T_m - t)}{\sigma_S\sqrt{T_m - t}} = \frac{\sigma_S\sqrt{T_m - t}}{2}
    $$

    $$
    d_2 = d_1 - \sigma_S\sqrt{T_m - t} = -\frac{\sigma_S\sqrt{T_m - t}}{2}
    $$

    Let $\epsilon = \frac{\sigma_S\sqrt{T_m - t}}{2}$. For small $\epsilon$, $\Phi(\epsilon) \approx \frac{1}{2} + \frac{\epsilon}{\sqrt{2\pi}}$ and $\Phi(-\epsilon) \approx \frac{1}{2} - \frac{\epsilon}{\sqrt{2\pi}}$. With $S = K$:

    $$
    V^{\text{pay}} = N A \cdot S\left[\Phi(\epsilon) - \Phi(-\epsilon)\right] = N A \cdot S \cdot \frac{2\epsilon}{\sqrt{2\pi}}
    $$

    Substituting $\epsilon = \frac{\sigma_S\sqrt{T_m - t}}{2}$:

    $$
    V^{\text{pay}} \approx N A_{m,n}(t) \cdot S_{m,n}(t) \cdot \frac{\sigma_S\sqrt{T_m - t}}{\sqrt{2\pi}}
    $$

    This is the ATM swaption approximation — the exact analogue of the ATM call approximation $C \approx 0.4 \cdot S \sigma\sqrt{T}$ from Chapter 6. It shows that ATM swaption prices are approximately linear in volatility and proportional to $\sqrt{T_m - t}$.

---

**Exercise 5.** The Black swaption formula uses a single volatility $\sigma_S$. In practice, the market quotes different implied volatilities for different strikes. Explain what a **swaption volatility cube** is and why the Black formula, despite being derived under a flat-volatility assumption, remains the standard quoting convention.

??? success "Solution to Exercise 5"
    A **swaption volatility cube** is a three-dimensional grid of implied volatilities indexed by:

    - **Option expiry** $T_m$ (e.g., 1 month, 1 year, 5 years, 10 years)
    - **Swap tenor** $T_n - T_m$ (e.g., 2 years, 5 years, 10 years, 30 years)
    - **Strike** $K$ (e.g., ATM, ATM $\pm$ 50bp, ATM $\pm$ 100bp)

    For each point in the cube, the market quotes an implied volatility $\sigma_S(T_m, T_n - T_m, K)$ such that the Black formula reproduces the observed swaption price.

    The Black formula remains the standard quoting convention despite the flat-volatility assumption because it provides a **bijection** between prices and volatilities. Since the Black formula is strictly increasing in $\sigma_S$ (positive vega), every positive swaption price corresponds to a unique implied volatility. This makes $\sigma_S$ a convenient unit for quoting and comparing swaption prices, just as implied volatility serves the same role for equity options via Black-Scholes.

    The strike dependence of implied volatility (the **volatility smile or skew**) indicates that the true dynamics of the swap rate are not lognormal. More sophisticated models (SABR, shifted lognormal, local volatility) capture the smile but still use the Black formula as the benchmark quoting convention.
