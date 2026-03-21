# Boundary and Terminal Behavior of Greeks


Greeks exhibit characteristic behavior near \(S\to 0\), \(S\to\infty\), and \(t\uparrow T\). This matters for hedging and numerics.

---

## Far-field behavior (vanilla calls)


As \(S\to\infty\), a call behaves like

\[
V(t,S)\sim S - K e^{-r(T-t)},
\]


so

\[
\Delta(t,S)\to 1,
\qquad
\Gamma(t,S)\to 0.
\]

**Quantitative refinement.** More precisely, for large \(S\):

\[
\Delta = 1 - N(-d_1) = 1 - \mathcal{O}\!\left(e^{-d_1^2/2}\right)
\]

\[
\Gamma = \frac{N'(d_1)}{S\sigma\sqrt{\tau}} = \mathcal{O}\!\left(\frac{1}{S}e^{-d_1^2/2}\right)
\]

Since \(d_1 \sim \frac{\ln(S/K)}{\sigma\sqrt{\tau}}\) for large \(S\), the decay is faster than any polynomial.

As \(S\to 0\),

\[
V(t,S)\to 0,
\qquad \Delta(t,S)\to 0,
\qquad \Gamma(t,S)\to 0.
\]

**Quantitative refinement.** For small \(S\):

\[
\Delta = N(d_1) = \mathcal{O}\!\left(e^{-d_1^2/2}\right), \qquad d_1 \to -\infty
\]

\[
\Gamma = \mathcal{O}\!\left(\frac{1}{S}e^{-d_1^2/2}\right)
\]

---

## Near maturity: quantitative asymptotics


At maturity \(V(T,S)=\Phi(S)\). For payoffs with kinks, derivatives at \(T\) are not classical; gamma concentrates near the kink.

**ATM behavior as \(\tau \to 0\).** For \(S = K\) (at-the-money):

\[
\Delta_{\text{ATM}} = N(d_1) \to \frac{1}{2} + \mathcal{O}(\sqrt{\tau})
\]

\[
\Gamma_{\text{ATM}} = \frac{N'(0)}{K\sigma\sqrt{\tau}} = \frac{1}{K\sigma\sqrt{2\pi\tau}} \sim \tau^{-1/2}
\]

\[
\nu_{\text{ATM}} = K\sqrt{\tau}N'(0) = \frac{K\sqrt{\tau}}{\sqrt{2\pi}} \sim \sqrt{\tau}
\]

\[
\Theta_{\text{ATM}} \sim -\frac{K\sigma}{2\sqrt{2\pi\tau}} \sim -\tau^{-1/2}
\]

**Transition layer width.** The region where delta transitions from 0 to 1 has width

\[
\delta S \sim S \cdot \sigma\sqrt{\tau}
\]

in spot space, or equivalently \(\delta x \sim \sigma\sqrt{\tau}\) in log-moneyness \(x = \ln(S/K)\).

---

## OTM and ITM behavior near expiry


**Out-of-the-money call** (\(S < K\)): As \(\tau \to 0\),

\[
\Delta \to 0 \quad \text{exponentially fast: } \Delta \approx \exp\!\left(-\frac{(\ln(K/S))^2}{2\sigma^2\tau}\right)
\]

**In-the-money call** (\(S > K\)): As \(\tau \to 0\),

\[
\Delta \to 1 \quad \text{exponentially fast: } 1 - \Delta \approx \exp\!\left(-\frac{(\ln(S/K))^2}{2\sigma^2\tau}\right)
\]

---

## Numerical boundary conditions


For finite-difference PDE solvers:

| Boundary | Condition for Call |
|:---------|:-------------------|
| \(S = 0\) | \(V = 0\), \(\Delta = 0\), \(\Gamma = 0\) |
| \(S = S_{\max}\) | \(V \approx S - Ke^{-r\tau}\), \(\Delta \approx 1\), \(\Gamma \approx 0\) |
| \(t = T\) | \(V = (S-K)^+\), \(\Delta = \mathbf{1}_{S>K}\) (step), \(\Gamma = \delta(S-K)\) |

---

## What to remember


- Boundary conditions for PDE numerics are guided by far-field Greek limits.
- Near maturity, gamma spikes near the strike with \(\Gamma \sim \tau^{-1/2}\); delta becomes step-like.
- Transition layer has width \(\mathcal{O}(\sigma\sqrt{\tau})\) in log-moneyness.
- Far from the money, Greeks decay exponentially with rate \(\sim 1/\tau\).
