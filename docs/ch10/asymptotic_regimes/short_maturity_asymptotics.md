# Short-Maturity Asymptotics


Let \(\tau:=T-t\downarrow 0\). Short-maturity asymptotics describe how prices concentrate near the current state.

---

## Diffusive scaling


Typical diffusion increments are \(\mathcal{O}(\sqrt{\tau})\), so near-the-money regions dominate short-time pricing.

---

## Black–Scholes log return



\[
\log\frac{S_T}{S_t}
=
\left(r-\frac{1}{2}\sigma^2\right)\tau+\sigma\sqrt{\tau}\,Z,
\qquad Z\sim\mathcal{N}(0,1).
\]



---

## ATM call price asymptotics


For an at-the-money call (\(S = K\)), as \(\tau \to 0\):

\[
\boxed{C_{\text{ATM}} = S\sigma\sqrt{\frac{\tau}{2\pi}} + \mathcal{O}(\tau)}
\]

**Derivation.** At the money, \(d_1 = \frac{(r + \frac12\sigma^2)\tau}{\sigma\sqrt{\tau}} = \mathcal{O}(\sqrt{\tau})\), so:

\[
N(d_1) = \frac{1}{2} + \frac{d_1}{\sqrt{2\pi}} + \mathcal{O}(d_1^3) = \frac{1}{2} + \mathcal{O}(\sqrt{\tau})
\]

\[
N(d_2) = \frac{1}{2} - \frac{\sigma\sqrt{\tau}}{\sqrt{2\pi}} + \mathcal{O}(\tau)
\]

Thus:
\[
C = SN(d_1) - Ke^{-r\tau}N(d_2) \approx \frac{S - K}{2} + S \cdot \frac{\sigma\sqrt{\tau}}{\sqrt{2\pi}}
\]

For \(S = K\): \(C_{\text{ATM}} \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}}\).

---

## Near-ATM expansion


For small log-moneyness \(x = \ln(S/K)\) with \(|x| = \mathcal{O}(\sqrt{\tau})\):

\[
C(S,K,\tau) = S\sigma\sqrt{\frac{\tau}{2\pi}} + \frac{x}{2}S + \mathcal{O}(\tau)
\]

The leading order depends only on \(\sigma\) and \(\tau\), not on \(r\).

---

## Far OTM is exponentially small


For strikes far from \(S\), short-time prices scale like

\[
V(t,S;K)\approx \exp\!\left(-\frac{I(S,K)}{\tau}\right) \cdot (\text{polynomial prefactor}),
\]


where \(I\) is a rate function (large deviations).

**Explicit form for OTM call** (\(K > Se^{r\tau}\)):

\[
\boxed{C \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}|x|} \exp\!\left(-\frac{x^2}{2\sigma^2\tau}\right), \quad x = \ln(K/S)}
\]

The rate function is:

\[
I(S,K) = \frac{(\ln(K/S))^2}{2\sigma^2}
\]

This is the squared geodesic distance in the log-moneyness metric, connecting to heat kernel small-time expansions.

**Derivation.** For large \(|d_2|\):

\[
N(-d_2) \approx \frac{N'(d_2)}{|d_2|} = \frac{1}{\sqrt{2\pi}|d_2|}e^{-d_2^2/2}
\]

Since \(d_2 \approx -\frac{x}{\sigma\sqrt{\tau}}\) for small \(\tau\), the exponential term dominates.

---

## ITM call near expiry


For an in-the-money call (\(S > K\)):

\[
C \approx (S - Ke^{-r\tau}) + \text{(exponentially small time value)}
\]

The intrinsic value dominates; the time value decays like:

\[
C - (S-K)^+ \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}} e^{-x^2/(2\sigma^2\tau)}
\]

---

## Greeks near expiry


**ATM Greeks** as \(\tau \to 0\):

| Greek | ATM behavior | Scaling |
|:------|:-------------|:--------|
| \(\Delta\) | \(\to \frac{1}{2}\) | \(\mathcal{O}(1)\) |
| \(\Gamma\) | \(\frac{1}{S\sigma\sqrt{2\pi\tau}}\) | \(\tau^{-1/2}\) |
| \(\Theta\) | \(-\frac{S\sigma}{2\sqrt{2\pi\tau}}\) | \(\tau^{-1/2}\) |
| \(\nu\) | \(\frac{S\sqrt{\tau}}{\sqrt{2\pi}}\) | \(\sqrt{\tau}\) |

---

## Connection to implied volatility


Short-maturity implied volatility \(\Sigma(K,\tau)\) satisfies:

\[
\Sigma(K,\tau) \to \sigma_{\text{local}}(S) \quad \text{as } \tau \to 0
\]

where \(\sigma_{\text{local}}(S)\) is the local volatility at spot. This is the basis for Dupire's formula and local volatility calibration.

> **Forward reference.** This connects to **Chapter 7** (Implied Volatility) and the small-time behavior of the implied volatility smile.

---

## What to remember


- Typical moves are \(\mathcal{O}(\sqrt{\tau})\).
- ATM call price: \(C \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}}\).
- Far OTM prices decay as \(\exp(-x^2/(2\sigma^2\tau))\) with rate function \(I = x^2/(2\sigma^2)\).
- Gamma and theta blow up like \(\tau^{-1/2}\) near ATM.
- Short-maturity implied vol converges to local vol.

---

## Exercises

**Exercise 1.** Verify the ATM call price formula $C_{\text{ATM}} \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}}$ by expanding $N(d_1)$ and $N(d_2)$ for $S = K$ and small $\tau$. Compute the ATM price for $S = 100$, $\sigma = 0.30$, $\tau = 5/252$ using both the exact Black--Scholes formula and the asymptotic approximation. What is the relative error?

---

**Exercise 2.** For an OTM call with $K = 110$ and $S = 100$, compute the rate function $I(S,K) = (\ln(K/S))^2/(2\sigma^2)$ for $\sigma = 0.20$. Then estimate the call price using the far-OTM formula for $\tau = 5/252$ and compare with the exact Black--Scholes price.

---

**Exercise 3.** The Greeks table shows that ATM gamma scales as $\tau^{-1/2}$ while vega scales as $\tau^{1/2}$ near expiry. Compute the ratio $\nu / \Gamma = \sigma S^2 \tau$ for $S = 100$, $\sigma = 0.20$ at $\tau = 1$ day, $1$ week, and $1$ month. What does this ratio tell you about the relative importance of gamma versus vega hedging near expiry?

---

**Exercise 4.** For an ITM call with $S = 110$, $K = 100$, the time value decays as $C - (S-K)^+ \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}}e^{-x^2/(2\sigma^2\tau)}$ where $x = \ln(K/S)$. Compute this time value for $\sigma = 0.20$ and $\tau = 1/252$. Is the time value material or negligible?

---

**Exercise 5.** The connection between short-maturity implied volatility and local volatility states $\Sigma(K,\tau) \to \sigma_{\text{local}}(S)$ as $\tau \to 0$. Explain intuitively why the short-maturity smile "sees" only the local volatility at the current spot. What information about the volatility surface is lost in this limit?

---

**Exercise 6.** Consider a portfolio of options with maturities $\tau_1 = 1$ day and $\tau_2 = 1$ year, both ATM. Using the scaling laws, compare the gamma, theta, and vega of each position. If both positions have the same notional, which contributes more to (a) daily P&L volatility and (b) sensitivity to implied vol changes?
