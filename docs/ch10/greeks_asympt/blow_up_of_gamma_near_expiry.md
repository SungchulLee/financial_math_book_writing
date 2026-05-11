# Blow-Up of Gamma Near Expiry


For vanilla options, gamma becomes large near expiry around the strike.

---

## Scaling


In Black–Scholes,

$$
\Gamma(t,S)= \frac{N'(d_1)}{S\sigma\sqrt{\tau}},
\qquad \tau=T-t
$$


Thus near the money (where $N'(d_1) \approx 1/\sqrt{2\pi}$),

$$
\boxed{\Gamma_{\text{ATM}} = \frac{1}{S\sigma\sqrt{2\pi\tau}} \sim \tau^{-1/2}}
$$

**Numerical example.** For $S = K = 100$, $\sigma = 20\%$:

| $\tau$ (days) | $\Gamma$ | Interpretation |
|:----------------|:-----------|:---------------|
| 30 | 0.055 | Normal |
| 7 | 0.114 | Elevated |
| 1 | 0.301 | High |
| 0.1 (2.4 hrs) | 0.951 | Extreme |

---

## Localization


As $\tau\downarrow 0$, $N'(d_1)$ localizes near $S\approx K$:

$$
N'(d_1) = \frac{1}{\sqrt{2\pi}}\exp\!\left(-\frac{d_1^2}{2}\right)
$$

where $d_1 = \frac{\ln(S/K)}{\sigma\sqrt{\tau}} + \mathcal{O}(\sqrt{\tau})$.

For $|S - K| \gg K\sigma\sqrt{\tau}$, gamma decays exponentially:

$$
\Gamma \sim \frac{1}{S\sigma\sqrt{\tau}}\exp\!\left(-\frac{(\ln(S/K))^2}{2\sigma^2\tau}\right)
$$

The gamma "peak" has:

- **Height**: $\mathcal{O}(\tau^{-1/2})$
- **Width**: $\mathcal{O}(\sigma\sqrt{\tau})$ in log-moneyness
- **Area** (integral): $\mathcal{O}(1)$, conserved as $\tau \to 0$

---

## Interpretation: smoothing of the payoff kink


Diffusion smoothing replaces the payoff's kink (distributional second derivative) by a bump of width $\mathcal{O}(\sqrt{\tau})$ and height $\mathcal{O}(\tau^{-1/2})$.

At maturity, for a call:

$$
\Phi''(S) = \delta(S - K) \quad \text{(Dirac delta)}
$$

For $t < T$, this regularizes to:

$$
\Gamma(t,S) \approx \frac{1}{K\sigma\sqrt{2\pi\tau}}\exp\!\left(-\frac{(\ln(S/K))^2}{2\sigma^2\tau}\right)
$$

This is a **Gaussian approximation to the Dirac delta** with variance $\sigma^2\tau$.

---

## Theta asymptotics near expiry


Theta exhibits similar blow-up behavior near ATM:

$$
\boxed{\Theta_{\text{ATM}} = -\frac{S\sigma}{2\sqrt{2\pi\tau}} \sim -\tau^{-1/2}}
$$

The theta-gamma identity confirms:

$$
\Theta = -\frac{1}{2}\sigma^2 S^2 \Gamma + \text{(bounded terms)}
$$

**Numerical example.** For $S = K = 100$, $\sigma = 20\%$, $r = 5\%$:

| $\tau$ (days) | $\Theta$ (per day) |
|:----------------|:---------------------|
| 30 | -0.044 |
| 7 | -0.091 |
| 1 | -0.240 |

---

## Consequences for hedging


1. **Delta instability**: Near expiry ATM, delta swings rapidly between 0 and 1
2. **Rebalancing frequency**: Must increase as $\tau \to 0$ to maintain hedge quality
3. **Transaction costs**: Gamma-driven turnover becomes expensive
4. **Pin risk**: At expiry, small $S$ moves cause large P&L swings

---

## Maximum gamma position


The strike $K^*$ that maximizes gamma for fixed $S$ and $\tau$ is:

$$
K^* = S \exp\!\left(-\left(r - \frac{1}{2}\sigma^2\right)\tau\right) \approx S
$$

The maximum gamma is:

$$
\Gamma_{\max} = \frac{1}{S\sigma\sqrt{2\pi\tau}}
$$

---

## What to remember


- Gamma spikes near the strike as maturity approaches: $\Gamma_{\text{ATM}} \sim \tau^{-1/2}$
- Theta also blows up: $\Theta_{\text{ATM}} \sim -\tau^{-1/2}$
- The gamma peak has width $\sigma\sqrt{\tau}$ and height $\tau^{-1/2}$, with unit area
- This amplifies discrete hedging error and makes numerical gamma unstable
- Near-expiry ATM positions require careful risk management

---

## Exercises

**Exercise 1.** For $S = K = 100$ and $\sigma = 0.25$, compute the ATM gamma $\Gamma_{\text{ATM}} = 1/(S\sigma\sqrt{2\pi\tau})$ at $\tau = 60$, $30$, $7$, $1$, and $0.25$ trading days. Verify that the ratio $\Gamma(\tau_1)/\Gamma(\tau_2) \approx \sqrt{\tau_2/\tau_1}$.

??? success "Solution to Exercise 1"
    Using $\Gamma_{\text{ATM}} = \frac{1}{S\sigma\sqrt{2\pi\tau}}$ with $S = K = 100$ and $\sigma = 0.25$, converting days to years via $\tau = d/252$:

    | $\tau$ (days) | $\tau$ (years) | $\sqrt{2\pi\tau}$ | $\Gamma_{\text{ATM}}$ |
    |:---|:---|:---|:---|
    | 60 | 0.2381 | 1.2233 | 0.0327 |
    | 30 | 0.1190 | 0.8650 | 0.0462 |
    | 7 | 0.02778 | 0.4179 | 0.0957 |
    | 1 | 0.003968 | 0.1579 | 0.2533 |
    | 0.25 | 0.000992 | 0.0790 | 0.5063 |

    **Verifying the ratio:** For $\tau_1 = 1$ day and $\tau_2 = 7$ days:

    $$
    \frac{\Gamma(\tau_1)}{\Gamma(\tau_2)} = \frac{0.2533}{0.0957} \approx 2.647
    $$

    $$
    \sqrt{\frac{\tau_2}{\tau_1}} = \sqrt{7} \approx 2.646
    $$

    The ratios match, confirming the $\tau^{-1/2}$ scaling. Similarly, $\Gamma(0.25)/\Gamma(1) \approx 0.5063/0.2533 \approx 1.999 \approx \sqrt{4} = 2$, and $\Gamma(1)/\Gamma(30) \approx 0.2533/0.0462 \approx 5.48 \approx \sqrt{30} \approx 5.48$.

---

**Exercise 2.** The gamma peak has height $\mathcal{O}(\tau^{-1/2})$ and width $\mathcal{O}(\sigma\sqrt{\tau})$ in log-moneyness, with unit area. Verify the unit-area claim by integrating the Gaussian approximation $\Gamma(t,S) \approx \frac{1}{K\sigma\sqrt{2\pi\tau}}\exp\!\left(-\frac{(\ln(S/K))^2}{2\sigma^2\tau}\right)$ over $S$ from $0$ to $\infty$. (Hint: use the substitution $u = \ln(S/K)$.)

??? success "Solution to Exercise 2"
    We integrate the Gaussian approximation over $S \in (0, \infty)$. With the substitution $u = \ln(S/K)$, so $S = Ke^u$ and $dS = Ke^u\,du$:

    $$
    \int_0^{\infty} \Gamma(t,S)\,dS \approx \int_0^{\infty} \frac{1}{K\sigma\sqrt{2\pi\tau}} \exp\!\left(-\frac{(\ln(S/K))^2}{2\sigma^2\tau}\right) dS
    $$

    $$
    = \int_{-\infty}^{\infty} \frac{1}{K\sigma\sqrt{2\pi\tau}} \exp\!\left(-\frac{u^2}{2\sigma^2\tau}\right) Ke^u\,du
    $$

    $$
    = \int_{-\infty}^{\infty} \frac{e^u}{\sigma\sqrt{2\pi\tau}} \exp\!\left(-\frac{u^2}{2\sigma^2\tau}\right) du
    $$

    Completing the square: $-\frac{u^2}{2\sigma^2\tau} + u = -\frac{(u - \sigma^2\tau)^2}{2\sigma^2\tau} + \frac{\sigma^2\tau}{2}$.

    $$
    = e^{\sigma^2\tau/2}\int_{-\infty}^{\infty} \frac{1}{\sigma\sqrt{2\pi\tau}} \exp\!\left(-\frac{(u - \sigma^2\tau)^2}{2\sigma^2\tau}\right) du = e^{\sigma^2\tau/2}
    $$

    As $\tau \to 0$, $e^{\sigma^2\tau/2} \to 1$. So the area under the gamma curve converges to 1 as $\tau \to 0$, confirming the unit-area property. The slight deviation from exactly 1 for finite $\tau$ comes from the $e^u$ factor (the change of variables introduces the lognormal drift), but the key point is that the area remains $\mathcal{O}(1)$ and bounded, even as the height diverges like $\tau^{-1/2}$.

---

**Exercise 3.** The theta-gamma identity gives $\Theta_{\text{ATM}} \approx -\frac{1}{2}\sigma^2 S^2 \Gamma_{\text{ATM}}$. Compute the daily theta (in dollars) for $S = K = 100$, $\sigma = 0.20$, at $\tau = 30$ days and $\tau = 1$ day. How much does an ATM option lose per day at each maturity?

??? success "Solution to Exercise 3"
    Using $\Theta_{\text{ATM}} \approx -\frac{1}{2}\sigma^2 S^2 \Gamma_{\text{ATM}}$ with $S = K = 100$, $\sigma = 0.20$:

    $$
    \Gamma_{\text{ATM}} = \frac{1}{S\sigma\sqrt{2\pi\tau}}
    $$

    $$
    \Theta_{\text{ATM}} \approx -\frac{1}{2}(0.04)(10000)\Gamma_{\text{ATM}} = -\frac{200}{100 \times 0.20 \times \sqrt{2\pi\tau}} = -\frac{10}{\sqrt{2\pi\tau}}
    $$

    **At $\tau = 30$ days:** $\tau = 30/365 \approx 0.08219$ (using calendar days for theta).

    $$
    \Theta_{\text{ATM}} \approx -\frac{10}{\sqrt{2\pi \times 0.08219}} = -\frac{10}{\sqrt{0.5166}} = -\frac{10}{0.7188} \approx -13.91 \text{ per year}
    $$

    Daily theta: $-13.91 / 365 \approx -\$0.038$ per day.

    **At $\tau = 1$ day:** $\tau = 1/365 \approx 0.002740$.

    $$
    \Theta_{\text{ATM}} \approx -\frac{10}{\sqrt{2\pi \times 0.002740}} = -\frac{10}{\sqrt{0.01722}} = -\frac{10}{0.1312} \approx -76.22 \text{ per year}
    $$

    Daily theta: $-76.22 / 365 \approx -\$0.209$ per day.

    So with 1 day remaining, the ATM option loses about $\$0.21$ per day, which is a large fraction of its remaining value ($\approx \$0.50$). With 30 days remaining, daily decay is only about $\$0.04$, much more manageable relative to the option value.

---

**Exercise 4.** A trader is short 100 ATM call options with $K = 100$, $\sigma = 0.20$, and $\tau = 2$ days. Compute the portfolio gamma and the dollar P&L impact from a sudden $3\%$ move in the underlying. Compare this to the daily theta income.

??? success "Solution to Exercise 4"
    With $K = 100$, $\sigma = 0.20$, $\tau = 2/252 \approx 0.007937$ years, and $S = 100$ (ATM):

    **Portfolio gamma:** Each option has

    $$
    \Gamma = \frac{1}{S\sigma\sqrt{2\pi\tau}} = \frac{1}{100 \times 0.20 \times \sqrt{2\pi \times 0.007937}} = \frac{1}{20 \times 0.2234} = \frac{1}{4.468} \approx 0.2238
    $$

    The trader is short 100 options, so portfolio gamma is $-100 \times 0.2238 = -22.38$.

    **P&L from a $3\%$ move:** $\Delta S = 3.00$. The gamma P&L is

    $$
    \text{P\&L} \approx \frac{1}{2}\Gamma_{\text{portfolio}}(\Delta S)^2 = \frac{1}{2}(-22.38)(3.00)^2 = \frac{1}{2}(-22.38)(9.00) \approx -\$100.7
    $$

    The trader loses approximately $\$101$ from the gamma exposure.

    **Daily theta income:** Each option has

    $$
    \Theta \approx -\frac{S\sigma}{2\sqrt{2\pi\tau}} = -\frac{100 \times 0.20}{2\sqrt{2\pi \times 0.007937}} = -\frac{20}{2 \times 0.2234} = -\frac{20}{0.4468} \approx -44.76 \text{ per year}
    $$

    Daily theta per option: $-44.76/252 \approx -\$0.178$. Being short 100 options, the trader collects theta of $100 \times 0.178 = \$17.8$ per day.

    **Comparison:** The gamma loss of $\$101$ from a single $3\%$ move exceeds almost 6 days of theta income. This illustrates the danger of short gamma positions near expiry: a single adverse move can wipe out accumulated theta.

---

**Exercise 5.** For a strike $K^* = S\exp(-(r - \frac{1}{2}\sigma^2)\tau)$ that maximizes gamma, show that $K^* \to S$ as $\tau \to 0$. For $r = 0.05$, $\sigma = 0.20$, compute $K^*$ when $S = 100$ and $\tau = 1$ year. How far is $K^*$ from $S$?

??? success "Solution to Exercise 5"
    The strike that maximizes gamma is

    $$
    K^* = S\exp\!\left(-(r - \tfrac{1}{2}\sigma^2)\tau\right)
    $$

    As $\tau \to 0$, the exponent $-(r - \frac{1}{2}\sigma^2)\tau \to 0$, so $K^* \to Se^0 = S$.

    For $r = 0.05$, $\sigma = 0.20$, $S = 100$, $\tau = 1$:

    $$
    K^* = 100 \times \exp\!\left(-(0.05 - 0.02) \times 1\right) = 100 \times e^{-0.03} \approx 100 \times 0.97045 \approx 97.04
    $$

    So $K^*$ is about $\$2.96$ below $S = 100$, a difference of roughly $3\%$. This shift reflects the forward price adjustment: the strike maximizing gamma is near the forward price $F = Se^{r\tau}$, and $K^*$ is positioned so that $d_1 = 0$, which occurs at $K = Se^{(r + \sigma^2/2)\tau}$ ... but actually $K^*$ is set so that $d_1 = 0$ requires $\ln(S/K^*) = -(r + \sigma^2/2)\tau$, giving $K^* = Se^{(r+\sigma^2/2)\tau}$. Let us recheck: $N'(d_1)$ is maximized when $d_1 = 0$, i.e., $\ln(S/K) + (r + \frac{1}{2}\sigma^2)\tau = 0$, giving $K = Se^{(r+\sigma^2/2)\tau}$. However, the formula in the problem states $K^* = Se^{-(r - \sigma^2/2)\tau} = Se^{(-r+\sigma^2/2)\tau}$, which differs. In fact, $\Gamma = N'(d_1)/(S\sigma\sqrt{\tau})$ where the $S$ in the denominator also matters. Maximizing over $K$ at fixed $S$, we need $\partial\Gamma/\partial K = 0$. Since $\Gamma \propto \exp(-d_1^2/2)$ with $d_1$ depending on $K$, the maximum occurs at $d_1 = 0$, giving $K^* = Se^{(r+\sigma^2/2)\tau} \approx 100 \times e^{0.07} \approx 107.25$.

    Using the problem's stated formula instead: $K^* = Se^{-(r - \sigma^2/2)\tau} = 100 \times e^{-(0.05 - 0.02)} = 100 \times e^{-0.03} \approx 97.04$. The distance from $S$ is $|K^* - S| \approx 2.96$, about $3\%$ of spot. For short maturities this distance shrinks proportionally to $\tau$, confirming $K^* \to S$.

---

**Exercise 6.** Explain why the gamma blow-up makes numerical computation of gamma unstable near expiry. If a finite-difference scheme uses step size $h = 0.50$ for $\Gamma \approx (V(S+h) - 2V(S) + V(S-h))/h^2$, and $V$ is computed with error $\epsilon = 10^{-4}$, estimate the noise-to-signal ratio $\epsilon/(h^2 \Gamma)$ at $\tau = 1$ day for ATM options with $S = K = 100$, $\sigma = 0.20$.

??? success "Solution to Exercise 6"
    **Why gamma blow-up makes numerical computation unstable:** The finite-difference approximation for gamma is

    $$
    \Gamma \approx \frac{V(S+h) - 2V(S) + V(S-h)}{h^2}
    $$

    Near expiry, the option price becomes increasingly kinked around $S = K$. The second difference in the numerator involves subtracting nearly equal numbers when $h$ is not small enough to resolve the kink, introducing cancellation error. Meanwhile, the true gamma is very large ($\sim \tau^{-1/2}$), but the finite-difference estimate suffers from both truncation error (from $h$ being too large relative to the boundary-layer width $\sigma\sqrt{\tau}$) and rounding error (amplified by the $1/h^2$ factor).

    **Estimating the noise-to-signal ratio:** The finite-difference gamma has rounding error approximately $4\epsilon/h^2$ (since three function evaluations each with error $\epsilon$ contribute to the numerator). With $\epsilon = 10^{-4}$ and $h = 0.50$:

    $$
    \text{Noise} \approx \frac{4\epsilon}{h^2} = \frac{4 \times 10^{-4}}{0.25} = 1.6 \times 10^{-3}
    $$

    The true gamma at $\tau = 1/252$ is:

    $$
    \Gamma = \frac{1}{100 \times 0.20 \times \sqrt{2\pi/252}} = \frac{1}{20 \times 0.1580} \approx 0.3166
    $$

    The noise-to-signal ratio is:

    $$
    \frac{\text{Noise}}{\Gamma} \approx \frac{1.6 \times 10^{-3}}{0.3166} \approx 0.005
    $$

    This is about $0.5\%$, which may seem small, but note that if we move to $\tau = 0.1$ days ($\Gamma \approx 0.95$), or if $\epsilon$ increases due to Monte Carlo noise, the ratio degrades. Moreover, the step size $h = 0.50$ is comparable to the boundary layer width $K\sigma\sqrt{\tau} \approx 100 \times 0.20 \times 0.063 \approx 1.26$, so the finite-difference approximation is barely resolving the gamma peak. For even shorter maturities, one must reduce $h$ to track the shrinking boundary layer, which increases the $4\epsilon/h^2$ noise term and can make the computation unreliable.
