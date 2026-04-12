# Short-Maturity Asymptotics


Let $\tau:=T-t\downarrow 0$. Short-maturity asymptotics describe how prices concentrate near the current state.

---

## Diffusive scaling


Typical diffusion increments are $\mathcal{O}(\sqrt{\tau})$, so near-the-money regions dominate short-time pricing.

---

## Black–Scholes log return



$$
\log\frac{S_T}{S_t}
=
\left(r-\frac{1}{2}\sigma^2\right)\tau+\sigma\sqrt{\tau}\,Z,
\qquad Z\sim\mathcal{N}(0,1)
$$



---

## ATM call price asymptotics


For an at-the-money call ($S = K$), as $\tau \to 0$:

$$
\boxed{C_{\text{ATM}} = S\sigma\sqrt{\frac{\tau}{2\pi}} + \mathcal{O}(\tau)}
$$

**Derivation.** At the money, $d_1 = \frac{(r + \frac12\sigma^2)\tau}{\sigma\sqrt{\tau}} = \mathcal{O}(\sqrt{\tau})$, so:

$$
N(d_1) = \frac{1}{2} + \frac{d_1}{\sqrt{2\pi}} + \mathcal{O}(d_1^3) = \frac{1}{2} + \mathcal{O}(\sqrt{\tau})
$$

$$
N(d_2) = \frac{1}{2} - \frac{\sigma\sqrt{\tau}}{\sqrt{2\pi}} + \mathcal{O}(\tau)
$$

Thus:

$$
C = SN(d_1) - Ke^{-r\tau}N(d_2) \approx \frac{S - K}{2} + S \cdot \frac{\sigma\sqrt{\tau}}{\sqrt{2\pi}}
$$

For $S = K$: $C_{\text{ATM}} \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}}$.

---

## Near-ATM expansion


For small log-moneyness $x = \ln(S/K)$ with $|x| = \mathcal{O}(\sqrt{\tau})$:

$$
C(S,K,\tau) = S\sigma\sqrt{\frac{\tau}{2\pi}} + \frac{x}{2}S + \mathcal{O}(\tau)
$$

The leading order depends only on $\sigma$ and $\tau$, not on $r$.

---

## Far OTM is exponentially small


For strikes far from $S$, short-time prices scale like

$$
V(t,S;K)\approx \exp\!\left(-\frac{I(S,K)}{\tau}\right) \cdot (\text{polynomial prefactor})
$$


where $I$ is a rate function (large deviations).

**Explicit form for OTM call** ($K > Se^{r\tau}$):

$$
\boxed{C \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}|x|} \exp\!\left(-\frac{x^2}{2\sigma^2\tau}\right), \quad x = \ln(K/S)}
$$

The rate function is:

$$
I(S,K) = \frac{(\ln(K/S))^2}{2\sigma^2}
$$

This is the squared geodesic distance in the log-moneyness metric, connecting to heat kernel small-time expansions.

**Derivation.** For large $|d_2|$:

$$
N(-d_2) \approx \frac{N'(d_2)}{|d_2|} = \frac{1}{\sqrt{2\pi}|d_2|}e^{-d_2^2/2}
$$

Since $d_2 \approx -\frac{x}{\sigma\sqrt{\tau}}$ for small $\tau$, the exponential term dominates.

---

## ITM call near expiry


For an in-the-money call ($S > K$):

$$
C \approx (S - Ke^{-r\tau}) + \text{(exponentially small time value)}
$$

The intrinsic value dominates; the time value decays like:

$$
C - (S-K)^+ \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}} e^{-x^2/(2\sigma^2\tau)}
$$

---

## Greeks near expiry


**ATM Greeks** as $\tau \to 0$:

| Greek | ATM behavior | Scaling |
|:------|:-------------|:--------|
| $\Delta$ | $\to \frac{1}{2}$ | $\mathcal{O}(1)$ |
| $\Gamma$ | $\frac{1}{S\sigma\sqrt{2\pi\tau}}$ | $\tau^{-1/2}$ |
| $\Theta$ | $-\frac{S\sigma}{2\sqrt{2\pi\tau}}$ | $\tau^{-1/2}$ |
| $\nu$ | $\frac{S\sqrt{\tau}}{\sqrt{2\pi}}$ | $\sqrt{\tau}$ |

---

## Connection to implied volatility


Short-maturity implied volatility $\Sigma(K,\tau)$ satisfies:

$$
\Sigma(K,\tau) \to \sigma_{\text{local}}(S) \quad \text{as } \tau \to 0
$$

where $\sigma_{\text{local}}(S)$ is the local volatility at spot. This is the basis for Dupire's formula and local volatility calibration.

> **Forward reference.** This connects to **Chapter 7** (Implied Volatility) and the small-time behavior of the implied volatility smile.

---

## What to remember


- Typical moves are $\mathcal{O}(\sqrt{\tau})$.
- ATM call price: $C \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}}$.
- Far OTM prices decay as $\exp(-x^2/(2\sigma^2\tau))$ with rate function $I = x^2/(2\sigma^2)$.
- Gamma and theta blow up like $\tau^{-1/2}$ near ATM.
- Short-maturity implied vol converges to local vol.

---

## Exercises

**Exercise 1.** Verify the ATM call price formula $C_{\text{ATM}} \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}}$ by expanding $N(d_1)$ and $N(d_2)$ for $S = K$ and small $\tau$. Compute the ATM price for $S = 100$, $\sigma = 0.30$, $\tau = 5/252$ using both the exact Black--Scholes formula and the asymptotic approximation. What is the relative error?

??? success "Solution to Exercise 1"
    We start from the Black--Scholes call price $C = SN(d_1) - Ke^{-r\tau}N(d_2)$ with

    $$
    d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}, \quad d_2 = d_1 - \sigma\sqrt{\tau}
    $$

    Setting $S = K$ gives $\ln(S/K) = 0$, so

    $$
    d_1 = \frac{(r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}} = \frac{r + \frac{1}{2}\sigma^2}{\sigma}\sqrt{\tau} = \mathcal{O}(\sqrt{\tau})
    $$

    $$
    d_2 = d_1 - \sigma\sqrt{\tau} = \frac{r - \frac{1}{2}\sigma^2}{\sigma}\sqrt{\tau} = \mathcal{O}(\sqrt{\tau})
    $$

    Expanding $N(z) = \frac{1}{2} + \frac{z}{\sqrt{2\pi}} + \mathcal{O}(z^3)$ for small $z$:

    $$
    N(d_1) = \frac{1}{2} + \frac{d_1}{\sqrt{2\pi}} + \mathcal{O}(\tau^{3/2})
    $$

    $$
    N(d_2) = \frac{1}{2} + \frac{d_2}{\sqrt{2\pi}} + \mathcal{O}(\tau^{3/2})
    $$

    Also $e^{-r\tau} = 1 - r\tau + \mathcal{O}(\tau^2)$. Substituting with $S = K$:

    $$
    C = S\left(\frac{1}{2} + \frac{d_1}{\sqrt{2\pi}}\right) - S(1 - r\tau)\left(\frac{1}{2} + \frac{d_2}{\sqrt{2\pi}}\right) + \mathcal{O}(\tau)
    $$

    $$
    = \frac{S}{\sqrt{2\pi}}(d_1 - d_2) + \frac{S}{2}r\tau + \mathcal{O}(\tau) = \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}} + \mathcal{O}(\tau)
    $$

    **Numerical comparison.** With $S = K = 100$, $\sigma = 0.30$, $\tau = 5/252 \approx 0.01984$, $r = 0$:

    - Asymptotic: $C \approx \frac{100 \times 0.30 \times \sqrt{0.01984}}{\sqrt{2\pi}} = \frac{30 \times 0.14086}{2.5066} \approx 1.686$
    - Exact Black--Scholes: $d_1 = \frac{0.5 \times 0.09 \times 0.01984}{0.30 \times 0.14086} \approx 0.02113$, $d_2 = 0.02113 - 0.04226 = -0.02113$, giving $C \approx 1.686$

    The relative error is less than $0.1\%$, confirming the approximation is excellent for short maturities.

---

**Exercise 2.** For an OTM call with $K = 110$ and $S = 100$, compute the rate function $I(S,K) = (\ln(K/S))^2/(2\sigma^2)$ for $\sigma = 0.20$. Then estimate the call price using the far-OTM formula for $\tau = 5/252$ and compare with the exact Black--Scholes price.

??? success "Solution to Exercise 2"
    The rate function is

    $$
    I(S,K) = \frac{(\ln(K/S))^2}{2\sigma^2} = \frac{(\ln(110/100))^2}{2 \times 0.04} = \frac{(\ln 1.1)^2}{0.08} = \frac{(0.09531)^2}{0.08} = \frac{0.009084}{0.08} = 0.11355
    $$

    For $\tau = 5/252 \approx 0.01984$, $x = \ln(K/S) = 0.09531$:

    The far-OTM approximation gives

    $$
    C \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}|x|} \exp\!\left(-\frac{x^2}{2\sigma^2\tau}\right) = \frac{100 \times 0.20 \times \sqrt{0.01984}}{\sqrt{2\pi} \times 0.09531} \exp\!\left(-\frac{0.009084}{2 \times 0.04 \times 0.01984}\right)
    $$

    Computing the prefactor: $\frac{100 \times 0.20 \times 0.14086}{2.5066 \times 0.09531} = \frac{2.8172}{0.23892} \approx 11.79$

    The exponent: $-\frac{0.009084}{0.001587} = -5.7246$

    $$
    C \approx 11.79 \times e^{-5.7246} = 11.79 \times 0.003264 \approx 0.0385
    $$

    Exact Black--Scholes: $d_1 = \frac{-0.09531 + 0.5 \times 0.04 \times 0.01984}{0.20 \times 0.14086} = \frac{-0.09491}{0.02817} = -3.369$, $d_2 = -3.369 - 0.02817 = -3.397$. This gives $C = 100 \times N(-3.369) - 110 \times N(-3.397) \approx 0.038$. The asymptotic formula is very accurate for this far-OTM, short-maturity case.

---

**Exercise 3.** The Greeks table shows that ATM gamma scales as $\tau^{-1/2}$ while vega scales as $\tau^{1/2}$ near expiry. Compute the ratio $\nu / \Gamma = \sigma S^2 \tau$ for $S = 100$, $\sigma = 0.20$ at $\tau = 1$ day, $1$ week, and $1$ month. What does this ratio tell you about the relative importance of gamma versus vega hedging near expiry?

??? success "Solution to Exercise 3"
    From the ATM formulas, $\Gamma = \frac{1}{S\sigma\sqrt{2\pi\tau}}$ and $\nu = \frac{S\sqrt{\tau}}{\sqrt{2\pi}}$, so

    $$
    \frac{\nu}{\Gamma} = \frac{S\sqrt{\tau}/\sqrt{2\pi}}{1/(S\sigma\sqrt{2\pi\tau})} = S^2 \sigma \tau
    $$

    With $S = 100$, $\sigma = 0.20$:

    - $\tau = 1/252 \approx 0.00397$: $\nu/\Gamma = 10000 \times 0.20 \times 0.00397 = 7.94$
    - $\tau = 5/252 \approx 0.01984$: $\nu/\Gamma = 10000 \times 0.20 \times 0.01984 = 39.68$
    - $\tau = 21/252 \approx 0.08333$: $\nu/\Gamma = 10000 \times 0.20 \times 0.08333 = 166.7$

    **Interpretation.** The ratio $\nu/\Gamma = S^2\sigma\tau$ shrinks linearly as $\tau \to 0$. Near expiry, gamma is enormous relative to vega. This means short-dated ATM options are dominated by realized-volatility (gamma) risk, not implied-volatility (vega) risk. Gamma hedging is far more important than vega hedging for options near expiry.

---

**Exercise 4.** For an ITM call with $S = 110$, $K = 100$, the time value decays as $C - (S-K)^+ \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}}e^{-x^2/(2\sigma^2\tau)}$ where $x = \ln(K/S)$. Compute this time value for $\sigma = 0.20$ and $\tau = 1/252$. Is the time value material or negligible?

??? success "Solution to Exercise 4"
    With $S = 110$, $K = 100$, $\sigma = 0.20$, $\tau = 1/252$, the log-moneyness is $x = \ln(K/S) = \ln(100/110) = -0.09531$.

    The time value formula gives

    $$
    C - (S-K)^+ \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}} \exp\!\left(-\frac{x^2}{2\sigma^2\tau}\right)
    $$

    Computing each piece:

    - Prefactor: $\frac{110 \times 0.20 \times \sqrt{1/252}}{\sqrt{2\pi}} = \frac{110 \times 0.20 \times 0.06299}{2.5066} = \frac{1.3859}{2.5066} = 0.5529$
    - Exponent: $-\frac{(0.09531)^2}{2 \times 0.04 \times 0.003968} = -\frac{0.009084}{0.0003175} = -28.62$

    $$
    C - (S-K)^+ \approx 0.5529 \times e^{-28.62} \approx 0.5529 \times 3.64 \times 10^{-13} \approx 2.01 \times 10^{-13}
    $$

    The time value is **completely negligible** --- effectively zero. The option is so deep ITM relative to one day's worth of volatility that there is essentially no chance of it ending OTM. The call price is almost exactly the intrinsic value $S - K = 10$.

---

**Exercise 5.** The connection between short-maturity implied volatility and local volatility states $\Sigma(K,\tau) \to \sigma_{\text{local}}(S)$ as $\tau \to 0$. Explain intuitively why the short-maturity smile "sees" only the local volatility at the current spot. What information about the volatility surface is lost in this limit?

??? success "Solution to Exercise 5"
    As $\tau \to 0$, the risk-neutral distribution of $S_T$ concentrates tightly around $S_t$. With only an infinitesimal time for the asset to move, the option price depends only on the local behavior of the diffusion near the current spot.

    For a general local volatility model $dS_t = rS_t\,dt + \sigma(S_t, t)S_t\,dW_t$, the short-maturity density of $S_T$ near $S_t$ is approximately Gaussian in log-space with variance $\sigma(S_t, t)^2\tau$. Therefore the implied volatility of an option with strike near $S_t$ converges to $\sigma_{\text{local}}(S_t, t)$, the instantaneous local volatility at spot.

    **Information lost in this limit:**

    - The global shape of $\sigma(S, t)$ away from $S_t$ is invisible --- the smile is determined only by the local value.
    - Any mean-reversion or correlation structure in stochastic volatility models is irrelevant for infinitesimally short maturities.
    - Jump components are suppressed relative to the diffusion at short time scales (jumps contribute at rate $\lambda\tau$ vs. diffusion at rate $\sqrt{\tau}$), so the limit does not detect jump risk.
    - Term structure effects (how $\sigma$ varies with $t$) are lost since only the current instant matters.

    In summary, the short-maturity limit provides a "snapshot" of instantaneous local volatility but discards all global, dynamic, and tail information.

---

**Exercise 6.** Consider a portfolio of options with maturities $\tau_1 = 1$ day and $\tau_2 = 1$ year, both ATM. Using the scaling laws, compare the gamma, theta, and vega of each position. If both positions have the same notional, which contributes more to (a) daily P&L volatility and (b) sensitivity to implied vol changes?

??? success "Solution to Exercise 6"
    Using the ATM scaling formulas with $S = 100$, $\sigma = 0.20$:

    **Position 1:** $\tau_1 = 1/252 \approx 0.00397$

    - $\Gamma_1 = \frac{1}{S\sigma\sqrt{2\pi\tau_1}} = \frac{1}{100 \times 0.20 \times \sqrt{2\pi \times 0.00397}} = \frac{1}{20 \times 0.1580} = \frac{1}{3.160} = 0.3165$
    - $\Theta_1 = -\frac{S\sigma}{2\sqrt{2\pi\tau_1}} = -\frac{100 \times 0.20}{2 \times 0.1580} = -\frac{20}{0.3160} = -63.29$
    - $\nu_1 = \frac{S\sqrt{\tau_1}}{\sqrt{2\pi}} = \frac{100 \times 0.06299}{2.5066} = 2.513$

    **Position 2:** $\tau_2 = 1$ year

    - $\Gamma_2 = \frac{1}{100 \times 0.20 \times \sqrt{2\pi}} = \frac{1}{50.13} = 0.01995$
    - $\Theta_2 = -\frac{20}{2\sqrt{2\pi}} = -\frac{20}{5.013} = -3.990$
    - $\nu_2 = \frac{100}{\sqrt{2\pi}} = 39.89$

    **Ratios:** $\Gamma_1/\Gamma_2 \approx 15.9$, $\Theta_1/\Theta_2 \approx 15.9$, $\nu_1/\nu_2 \approx 0.063$.

    **(a) Daily P&L volatility.** The gamma P&L for a delta-hedged position scales as $\frac{1}{2}\Gamma S^2 (\Delta S/S)^2$. Since $\Gamma_1 \gg \Gamma_2$, the short-dated option contributes far more to daily P&L volatility. Theta also offsets this: the short-dated option has much larger daily time decay.

    **(b) Sensitivity to implied vol changes.** Vega measures this directly. Since $\nu_2 \gg \nu_1$, the long-dated option is roughly 16 times more sensitive to implied volatility changes. A 1 vol-point move in implied vol causes a much larger price change in the 1-year option.

    **Summary:** Short-dated options dominate gamma/theta risk (realized vol matters most), while long-dated options dominate vega risk (implied vol matters most).
