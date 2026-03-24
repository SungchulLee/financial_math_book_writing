# Large-Strike and Small-Strike Asymptotics


Extreme strikes probe the tail behavior of the risk-neutral distribution.

---

## Tail control


For a call,


\[
C(t,S;K)=e^{-r\tau}\mathbb{E}[(S_T-K)^+],
\]



and for large \(K\) the main contribution is the tail \(\mathbb{P}(S_T>K)\). Similarly, deep OTM puts are controlled by \(\mathbb{P}(S_T<K)\).

---

## Black–Scholes tails


Since \(\log S_T\) is normal, tail probabilities have Gaussian asymptotics in log-strike.

**Large strike (OTM call).** For \(K \to \infty\) with fixed \(S\):

\[
d_2 = \frac{\ln(S/K) + (r - \frac12\sigma^2)\tau}{\sigma\sqrt{\tau}} \to -\infty
\]

Using Gaussian tail bounds:

\[
\boxed{C \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}|\ln(K/S)|} \exp\!\left(-\frac{(\ln(K/S))^2}{2\sigma^2\tau}\right)}
\]

**Small strike (OTM put).** For \(K \to 0\) with fixed \(S\):

\[
d_1 \to +\infty, \quad d_2 \to +\infty
\]

\[
\boxed{P \approx \frac{Ke^{-r\tau}\sigma\sqrt{\tau}}{\sqrt{2\pi}|\ln(S/K)|} \exp\!\left(-\frac{(\ln(S/K))^2}{2\sigma^2\tau}\right)}
\]

---

## Log-strike asymptotics


Define log-moneyness \(k = \ln(K/F)\) where \(F = Se^{r\tau}\) is the forward price.

**Right tail** (\(k \to +\infty\)):
\[
C(k) \sim e^{-r\tau} \cdot \frac{\sigma\sqrt{\tau}}{\sqrt{2\pi}k} \exp\!\left(-\frac{(k - \frac12\sigma^2\tau)^2}{2\sigma^2\tau}\right)
\]

**Left tail** (\(k \to -\infty\)):
\[
P(k) \sim e^{-r\tau} \cdot \frac{\sigma\sqrt{\tau}}{\sqrt{2\pi}|k|} \exp\!\left(-\frac{(k + \frac12\sigma^2\tau)^2}{2\sigma^2\tau}\right)
\]

---

## Implied volatility at extreme strikes


The Black–Scholes implied volatility \(\Sigma(K)\) has specific limiting behavior:

**Roger Lee's moment formula.** Define the tail slopes:
\[
\beta_R = \limsup_{k \to +\infty} \frac{\Sigma(k)^2 \tau}{k}, \quad \beta_L = \limsup_{k \to -\infty} \frac{\Sigma(k)^2 \tau}{|k|}
\]

These are related to the existence of moments:
- If \(\mathbb{E}[S_T^{1+\alpha}] < \infty\), then \(\beta_R \leq 2 - 4(\sqrt{\alpha^2 + \alpha} - \alpha)\)
- If \(\mathbb{E}[S_T^{-\alpha}] < \infty\), then \(\beta_L \leq 2 - 4(\sqrt{\alpha^2 + \alpha} - \alpha)\)

For Black–Scholes (all moments finite), \(\beta_R = \beta_L = 0\), meaning implied vol is bounded.

---

## Greeks at extreme strikes


**Delta asymptotics:**

Large \(K\): \(\Delta_{\text{call}} = N(d_1) \approx \frac{N'(d_1)}{|d_1|} \to 0\) exponentially

Small \(K\): \(\Delta_{\text{call}} \to 1\) exponentially fast

**Gamma asymptotics:**

\[
\Gamma = \frac{N'(d_1)}{S\sigma\sqrt{\tau}} \to 0 \quad \text{exponentially for } K \to 0, \infty
\]

**Vega asymptotics:**

\[
\nu = S\sqrt{\tau}N'(d_1) \to 0 \quad \text{exponentially}
\]

---

## Tail risk and moment conditions


The tail behavior of option prices reflects moment conditions on the underlying:

| Moment condition | Tail behavior | Implied vol |
|:-----------------|:--------------|:------------|
| All moments finite (BS) | Gaussian tails | Bounded |
| Finite variance only | Polynomial tails | Wings blow up |
| Heavy tails (Lévy) | Power law | Steep smile |

---

## Practical implications


1. **Far OTM options are nearly worthless** in Black–Scholes due to thin Gaussian tails
2. **Market smiles** often show steeper tails than Black–Scholes predicts
3. **Tail risk hedging** requires models with fatter tails (jumps, stochastic vol)
4. **Calibration** to extreme strikes reveals distributional assumptions

> **Forward reference.** The implied volatility smile and its wing behavior are analyzed in detail in **Chapter 7**.

---

## What to remember


- Extreme strikes encode tail probabilities.
- Black–Scholes tails are Gaussian: prices decay as \(\exp(-(\ln K)^2/(2\sigma^2\tau))\).
- Implied volatility at extreme strikes reflects moment conditions (Roger Lee's formula).
- Market option prices often imply fatter tails than log-normal.
- Greeks vanish exponentially for far OTM options.

---

## Exercises

**Exercise 1.** For $S = 100$, $\sigma = 0.20$, $\tau = 1$, $r = 0.03$, compute the OTM call price using the large-strike asymptotic formula for $K = 150$, $200$, and $300$. Compare with the exact Black--Scholes prices. At what strike does the asymptotic formula become a good approximation?

---

**Exercise 2.** Roger Lee's moment formula states that the right-tail slope $\beta_R$ of implied variance is bounded by $2 - 4(\sqrt{\alpha^2 + \alpha} - \alpha)$ when $\mathbb{E}[S_T^{1+\alpha}] < \infty$. For the log-normal model where all moments are finite ($\alpha \to \infty$), show that $\beta_R \to 0$, confirming that Black--Scholes implied volatility is bounded for extreme strikes.

---

**Exercise 3.** The OTM put asymptotics show $P \approx \frac{Ke^{-r\tau}\sigma\sqrt{\tau}}{\sqrt{2\pi}|\ln(S/K)|}\exp(-\frac{(\ln(S/K))^2}{2\sigma^2\tau})$ for $K \to 0$. For $S = 100$, $K = 50$, $\sigma = 0.25$, $\tau = 0.5$, compute this approximation and compare with the exact put price.

---

**Exercise 4.** All Greeks vanish exponentially for far OTM options. For a call with $K = 200$ when $S = 100$, $\sigma = 0.20$, $\tau = 1$, compute $\Delta$, $\Gamma$, and $\nu$ using the exact formulas. Verify that they are negligibly small. What does this imply about hedging deep OTM options?

---

**Exercise 5.** Market implied volatility smiles often show steeper wings than the Black--Scholes model predicts. Using the tail behavior framework, explain why models with heavier tails (e.g., jump-diffusion or variance gamma) produce implied volatility that increases with $|k|$ for large $|k|$, while Black--Scholes does not.

---

**Exercise 6.** In log-moneyness coordinates $k = \ln(K/F)$ where $F = Se^{r\tau}$, the right-tail call price decays as $\exp(-(k - \frac{1}{2}\sigma^2\tau)^2/(2\sigma^2\tau))$. Show that for fixed $\sigma^2\tau$, the tails become thinner as $\tau$ decreases (equivalently, as $\sigma$ increases for fixed $\tau$). What does this mean for the shape of the short-maturity smile?
