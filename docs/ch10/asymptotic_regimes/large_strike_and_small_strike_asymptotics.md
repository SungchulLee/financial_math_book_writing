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

??? success "Solution to Exercise 1"
    With $S = 100$, $\sigma = 0.20$, $\tau = 1$, $r = 0.03$, the forward is $F = Se^{r\tau} = 103.05$. The large-strike asymptotic formula for OTM calls is

    $$
    C \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}|\ln(K/S)|} \exp\!\left(-\frac{(\ln(K/S))^2}{2\sigma^2\tau}\right)
    $$

    **$K = 150$:** $\ln(K/S) = \ln(1.5) = 0.4055$

    $$
    C_{150} \approx \frac{100 \times 0.20}{\sqrt{2\pi} \times 0.4055} \exp\!\left(-\frac{0.1644}{0.08}\right) = \frac{20}{1.017} \exp(-2.056) = 19.67 \times 0.1281 = 2.519
    $$

    Exact Black--Scholes: $d_1 = \frac{-0.4055 + 0.05}{0.20} = -1.778$, $d_2 = -1.978$, giving $C = 100 \times N(-1.778) - 150 \times e^{-0.03} \times N(-1.978) = 100 \times 0.03774 - 145.6 \times 0.02400 = 3.774 - 3.494 = 0.280$. The asymptotic formula significantly overestimates because $K = 150$ is not sufficiently far OTM.

    **$K = 200$:** $\ln(K/S) = \ln(2) = 0.6931$

    $$
    C_{200} \approx \frac{20}{\sqrt{2\pi} \times 0.6931} \exp\!\left(-\frac{0.4804}{0.08}\right) = \frac{20}{1.738} \exp(-6.005) = 11.51 \times 0.002472 = 0.02845
    $$

    Exact: $d_1 = \frac{-0.6931 + 0.05}{0.20} = -3.216$, $d_2 = -3.416$, $C = 100 \times N(-3.216) - 200 e^{-0.03} N(-3.416) = 100 \times 0.000651 - 194.1 \times 0.000318 = 0.0651 - 0.0617 = 0.0034$. Still an overestimate by an order of magnitude.

    **$K = 300$:** $\ln(K/S) = \ln(3) = 1.0986$

    $$
    C_{300} \approx \frac{20}{\sqrt{2\pi} \times 1.0986} \exp\!\left(-\frac{1.2069}{0.08}\right) = \frac{20}{2.755} \exp(-15.09) = 7.261 \times 2.78 \times 10^{-7} = 2.02 \times 10^{-6}
    $$

    Exact: $d_1 = \frac{-1.0986 + 0.05}{0.20} = -5.243$, $d_2 = -5.443$. Both $N(d_1)$ and $N(d_2)$ are astronomically small (of order $10^{-8}$), giving $C \approx 8 \times 10^{-7}$. The asymptotic approximation improves with increasing $K$, and by $K = 300$ the order of magnitude is comparable, though the prefactor correction matters.

    The asymptotic formula becomes a good approximation when $|\ln(K/S)|/(\sigma\sqrt{\tau}) \gg 1$, i.e., when $d_2$ is very negative. For $\sigma = 0.20$ and $\tau = 1$, this requires roughly $K > 200$.

---

**Exercise 2.** Roger Lee's moment formula states that the right-tail slope $\beta_R$ of implied variance is bounded by $2 - 4(\sqrt{\alpha^2 + \alpha} - \alpha)$ when $\mathbb{E}[S_T^{1+\alpha}] < \infty$. For the log-normal model where all moments are finite ($\alpha \to \infty$), show that $\beta_R \to 0$, confirming that Black--Scholes implied volatility is bounded for extreme strikes.

??? success "Solution to Exercise 2"
    Roger Lee's bound states $\beta_R \leq 2 - 4(\sqrt{\alpha^2 + \alpha} - \alpha)$ when $\mathbb{E}[S_T^{1+\alpha}] < \infty$.

    For the log-normal model, $S_T = S_0 \exp((r - \sigma^2/2)T + \sigma W_T)$, so

    $$
    \mathbb{E}[S_T^{1+\alpha}] = S_0^{1+\alpha} \exp\!\left((1+\alpha)(r - \sigma^2/2)T + \frac{(1+\alpha)^2\sigma^2 T}{2}\right) < \infty
    $$

    for all $\alpha > 0$. Thus the bound holds for all $\alpha$.

    Define $f(\alpha) = 2 - 4(\sqrt{\alpha^2 + \alpha} - \alpha)$. We need to show $f(\alpha) \to 0$ as $\alpha \to \infty$.

    Rationalizing: $\sqrt{\alpha^2 + \alpha} - \alpha = \frac{\alpha}{\sqrt{\alpha^2 + \alpha} + \alpha}$. For large $\alpha$:

    $$
    \sqrt{\alpha^2 + \alpha} = \alpha\sqrt{1 + 1/\alpha} \approx \alpha\left(1 + \frac{1}{2\alpha} - \frac{1}{8\alpha^2} + \cdots\right) = \alpha + \frac{1}{2} - \frac{1}{8\alpha} + \cdots
    $$

    So $\sqrt{\alpha^2 + \alpha} - \alpha \to \frac{1}{2}$ as $\alpha \to \infty$, and

    $$
    f(\alpha) \to 2 - 4 \times \frac{1}{2} = 2 - 2 = 0
    $$

    Since $\beta_R \leq f(\alpha)$ for all $\alpha$ and $\beta_R \geq 0$ by definition, taking $\alpha \to \infty$ gives $\beta_R = 0$. By an identical argument, $\beta_L = 0$.

    This confirms that Black--Scholes implied volatility is bounded (does not blow up) at extreme strikes, consistent with the Gaussian tail decay.

---

**Exercise 3.** The OTM put asymptotics show $P \approx \frac{Ke^{-r\tau}\sigma\sqrt{\tau}}{\sqrt{2\pi}|\ln(S/K)|}\exp(-\frac{(\ln(S/K))^2}{2\sigma^2\tau})$ for $K \to 0$. For $S = 100$, $K = 50$, $\sigma = 0.25$, $\tau = 0.5$, compute this approximation and compare with the exact put price.

??? success "Solution to Exercise 3"
    With $S = 100$, $K = 50$, $\sigma = 0.25$, $\tau = 0.5$, $r = 0$ (assuming zero rate unless stated):

    $$
    P \approx \frac{Ke^{-r\tau}\sigma\sqrt{\tau}}{\sqrt{2\pi}|\ln(S/K)|} \exp\!\left(-\frac{(\ln(S/K))^2}{2\sigma^2\tau}\right)
    $$

    $\ln(S/K) = \ln(100/50) = \ln 2 = 0.6931$

    Prefactor: $\frac{50 \times 0.25 \times \sqrt{0.5}}{\sqrt{2\pi} \times 0.6931} = \frac{50 \times 0.25 \times 0.7071}{1.738} = \frac{8.839}{1.738} = 5.086$

    Exponent: $-\frac{(0.6931)^2}{2 \times 0.0625 \times 0.5} = -\frac{0.4804}{0.0625} = -7.687$

    $$
    P \approx 5.086 \times e^{-7.687} = 5.086 \times 4.577 \times 10^{-4} = 0.002328
    $$

    Exact Black--Scholes put: $d_1 = \frac{0.6931 + 0.5 \times 0.0625 \times 0.5}{0.25\sqrt{0.5}} = \frac{0.6931 + 0.01563}{0.17678} = \frac{0.7087}{0.17678} = 4.009$, $d_2 = 4.009 - 0.17678 = 3.832$.

    $P = Ke^{-r\tau}N(-d_2) - SN(-d_1) = 50 \times N(-3.832) - 100 \times N(-4.009)$

    $N(-3.832) \approx 6.37 \times 10^{-5}$, $N(-4.009) \approx 3.05 \times 10^{-5}$

    $P \approx 50 \times 6.37 \times 10^{-5} - 100 \times 3.05 \times 10^{-5} = 0.003185 - 0.003050 = 0.000135$

    The asymptotic formula gives $0.00233$ vs. the exact $0.000135$ --- it overestimates by about an order of magnitude. The Gaussian tail approximation $N(-|d|) \approx N'(d)/|d|$ is responsible for this discrepancy; it becomes accurate only for very extreme tails. For $K = 50$, the asymptotic regime is only just beginning.

---

**Exercise 4.** All Greeks vanish exponentially for far OTM options. For a call with $K = 200$ when $S = 100$, $\sigma = 0.20$, $\tau = 1$, compute $\Delta$, $\Gamma$, and $\nu$ using the exact formulas. Verify that they are negligibly small. What does this imply about hedging deep OTM options?

??? success "Solution to Exercise 4"
    With $K = 200$, $S = 100$, $\sigma = 0.20$, $\tau = 1$, $r = 0$ (assume zero rate for simplicity):

    $$
    d_1 = \frac{\ln(100/200) + \frac{1}{2}(0.04)(1)}{0.20} = \frac{-0.6931 + 0.02}{0.20} = \frac{-0.6731}{0.20} = -3.366
    $$

    $$
    d_2 = -3.366 - 0.20 = -3.566
    $$

    **Delta:** $\Delta = N(d_1) = N(-3.366) \approx 3.82 \times 10^{-4}$

    **Gamma:** $\Gamma = \frac{N'(d_1)}{S\sigma\sqrt{\tau}} = \frac{\frac{1}{\sqrt{2\pi}}e^{-d_1^2/2}}{100 \times 0.20} = \frac{\frac{1}{2.5066}e^{-5.664}}{20} = \frac{0.3989 \times 3.47 \times 10^{-3}}{20} = 6.92 \times 10^{-5}$

    **Vega:** $\nu = S\sqrt{\tau}N'(d_1) = 100 \times 0.3989 \times e^{-5.664} = 100 \times 0.3989 \times 3.47 \times 10^{-3} = 0.1384$

    All three Greeks are negligibly small. The delta of $3.82 \times 10^{-4}$ means the option barely responds to spot moves. Gamma and vega are similarly tiny.

    **Hedging implications.** Deep OTM options are essentially unhedgeable in practice because:

    1. The Greeks are so small that the hedge ratios are near zero --- any hedge has negligible sensitivity to the option.
    2. The option's value comes entirely from extreme tail events, which are poorly captured by continuous delta-hedging.
    3. Transaction costs of maintaining a delta hedge far exceed the Greeks' contributions.
    4. The option's risk is "jump risk" --- a sudden large move can make it ITM instantly, and no smooth hedging strategy protects against this.

---

**Exercise 5.** Market implied volatility smiles often show steeper wings than the Black--Scholes model predicts. Using the tail behavior framework, explain why models with heavier tails (e.g., jump-diffusion or variance gamma) produce implied volatility that increases with $|k|$ for large $|k|$, while Black--Scholes does not.

??? success "Solution to Exercise 5"
    In Black--Scholes, the risk-neutral log-return $\ln(S_T/S_0)$ is Gaussian with thin (sub-exponential) tails. The implied volatility smile is nearly flat because the model's distributional tails decay as fast as a Gaussian.

    In models with heavier tails, the risk-neutral density $q(s)$ satisfies

    $$
    q(s) \sim s^{-(1+\alpha)} \quad \text{for large } s
    $$

    (power-law tail) or has exponential tails that are slower than Gaussian. For such models:

    **1. OTM call prices decay slower.** The call price $C(K) = e^{-r\tau}\int_K^\infty (s-K)q(s)\,ds$ decays as a power law or slow exponential in $K$, rather than Gaussian.

    **2. Implied vol must increase.** The Black--Scholes model can only produce such slow decay by using a higher implied volatility. For a fixed strike $K$ far from ATM, the implied vol $\Sigma(K)$ must be elevated above ATM vol to match the market price.

    **3. Wings blow up.** As $|k| \to \infty$, the gap between the heavy-tailed model's price and a flat-vol Black--Scholes price grows, requiring $\Sigma(k)$ to increase with $|k|$. Roger Lee's formula quantifies this: $\Sigma(k)^2\tau/|k| \to \beta > 0$ when moments are finite only up to some order.

    Specific examples:

    - **Jump-diffusion (Merton):** Jumps add mass to the tails, producing a smile that flattens with maturity as the central limit theorem kicks in.
    - **Variance gamma:** The log-return has semi-heavy (exponential) tails, producing steep wings that persist at all maturities.

    In summary, any model with tails heavier than Gaussian necessarily produces implied volatility that increases at extreme strikes, because the Black--Scholes pricing map must compensate with higher vol to match the elevated tail probabilities.

---

**Exercise 6.** In log-moneyness coordinates $k = \ln(K/F)$ where $F = Se^{r\tau}$, the right-tail call price decays as $\exp(-(k - \frac{1}{2}\sigma^2\tau)^2/(2\sigma^2\tau))$. Show that for fixed $\sigma^2\tau$, the tails become thinner as $\tau$ decreases (equivalently, as $\sigma$ increases for fixed $\tau$). What does this mean for the shape of the short-maturity smile?

??? success "Solution to Exercise 6"
    The right-tail call price decays as

    $$
    C(k) \sim \exp\!\left(-\frac{(k - \frac{1}{2}\sigma^2\tau)^2}{2\sigma^2\tau}\right)
    $$

    Let $v = \sigma^2\tau$ (the total variance). Rewriting:

    $$
    C(k) \sim \exp\!\left(-\frac{(k - v/2)^2}{2v}\right) = \exp\!\left(-\frac{k^2}{2v} + \frac{k}{2} - \frac{v}{8}\right)
    $$

    The dominant term for large $k$ is $-k^2/(2v)$. For fixed $v$, this is the same regardless of $\tau$.

    However, the statement asks about fixed $\sigma^2\tau$ while varying $\tau$. If $v = \sigma^2\tau$ is fixed, then $\sigma = \sqrt{v/\tau}$. As $\tau$ decreases (so $\sigma$ increases to maintain constant $v$), the total variance stays constant, and the tail behavior is identical. The tails do not become thinner for fixed $v$.

    The correct interpretation: for fixed $\sigma$ (not fixed $\sigma^2\tau$), decreasing $\tau$ reduces $v = \sigma^2\tau$, making the exponent $-k^2/(2v)$ more negative for any given $k > 0$. This means tails become thinner.

    **Formal statement.** For fixed $\sigma$ and $k > 0$:

    $$
    \frac{\partial}{\partial \tau}\left(-\frac{k^2}{2\sigma^2\tau}\right) = \frac{k^2}{2\sigma^2\tau^2} > 0
    $$

    So as $\tau$ decreases, the exponent becomes more negative, and the tail decays faster.

    **Shape of the short-maturity smile.** Thinner tails mean that OTM options are cheaper relative to ATM options. In the Black--Scholes model, the implied volatility is constant, so the smile is flat at all maturities. But in models where the tail thickness does not scale exactly as $\sigma^2\tau$, shorter maturities produce steeper smiles --- the wings are more pronounced because the diffusion has less time to reach extreme strikes, amplifying any non-Gaussian features of the model.
