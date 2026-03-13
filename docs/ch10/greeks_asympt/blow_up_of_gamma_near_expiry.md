# Blow-Up of Gamma Near Expiry


For vanilla options, gamma becomes large near expiry around the strike.

---

## Scaling


In Black–Scholes,

\[
\Gamma(t,S)= \frac{N'(d_1)}{S\sigma\sqrt{\tau}},
\qquad \tau=T-t.
\]


Thus near the money (where \(N'(d_1) \approx 1/\sqrt{2\pi}\)),

\[
\boxed{\Gamma_{\text{ATM}} = \frac{1}{S\sigma\sqrt{2\pi\tau}} \sim \tau^{-1/2}}
\]

**Numerical example.** For \(S = K = 100\), \(\sigma = 20\%\):

| \(\tau\) (days) | \(\Gamma\) | Interpretation |
|:----------------|:-----------|:---------------|
| 30 | 0.055 | Normal |
| 7 | 0.114 | Elevated |
| 1 | 0.301 | High |
| 0.1 (2.4 hrs) | 0.951 | Extreme |

---

## Localization


As \(\tau\downarrow 0\), \(N'(d_1)\) localizes near \(S\approx K\):

\[
N'(d_1) = \frac{1}{\sqrt{2\pi}}\exp\!\left(-\frac{d_1^2}{2}\right)
\]

where \(d_1 = \frac{\ln(S/K)}{\sigma\sqrt{\tau}} + \mathcal{O}(\sqrt{\tau})\).

For \(|S - K| \gg K\sigma\sqrt{\tau}\), gamma decays exponentially:

\[
\Gamma \sim \frac{1}{S\sigma\sqrt{\tau}}\exp\!\left(-\frac{(\ln(S/K))^2}{2\sigma^2\tau}\right)
\]

The gamma "peak" has:
- **Height**: \(\mathcal{O}(\tau^{-1/2})\)
- **Width**: \(\mathcal{O}(\sigma\sqrt{\tau})\) in log-moneyness
- **Area** (integral): \(\mathcal{O}(1)\), conserved as \(\tau \to 0\)

---

## Interpretation: smoothing of the payoff kink


Diffusion smoothing replaces the payoff's kink (distributional second derivative) by a bump of width \(\mathcal{O}(\sqrt{\tau})\) and height \(\mathcal{O}(\tau^{-1/2})\).

At maturity, for a call:
\[
\Phi''(S) = \delta(S - K) \quad \text{(Dirac delta)}
\]

For \(t < T\), this regularizes to:
\[
\Gamma(t,S) \approx \frac{1}{K\sigma\sqrt{2\pi\tau}}\exp\!\left(-\frac{(\ln(S/K))^2}{2\sigma^2\tau}\right)
\]

This is a **Gaussian approximation to the Dirac delta** with variance \(\sigma^2\tau\).

---

## Theta asymptotics near expiry


Theta exhibits similar blow-up behavior near ATM:

\[
\boxed{\Theta_{\text{ATM}} = -\frac{S\sigma}{2\sqrt{2\pi\tau}} \sim -\tau^{-1/2}}
\]

The theta-gamma identity confirms:
\[
\Theta = -\frac{1}{2}\sigma^2 S^2 \Gamma + \text{(bounded terms)}
\]

**Numerical example.** For \(S = K = 100\), \(\sigma = 20\%\), \(r = 5\%\):

| \(\tau\) (days) | \(\Theta\) (per day) |
|:----------------|:---------------------|
| 30 | -0.044 |
| 7 | -0.091 |
| 1 | -0.240 |

---

## Consequences for hedging


1. **Delta instability**: Near expiry ATM, delta swings rapidly between 0 and 1
2. **Rebalancing frequency**: Must increase as \(\tau \to 0\) to maintain hedge quality
3. **Transaction costs**: Gamma-driven turnover becomes expensive
4. **Pin risk**: At expiry, small \(S\) moves cause large P&L swings

---

## Maximum gamma position


The strike \(K^*\) that maximizes gamma for fixed \(S\) and \(\tau\) is:

\[
K^* = S \exp\!\left(-\left(r - \frac{1}{2}\sigma^2\right)\tau\right) \approx S
\]

The maximum gamma is:
\[
\Gamma_{\max} = \frac{1}{S\sigma\sqrt{2\pi\tau}}
\]

---

## What to remember


- Gamma spikes near the strike as maturity approaches: \(\Gamma_{\text{ATM}} \sim \tau^{-1/2}\)
- Theta also blows up: \(\Theta_{\text{ATM}} \sim -\tau^{-1/2}\)
- The gamma peak has width \(\sigma\sqrt{\tau}\) and height \(\tau^{-1/2}\), with unit area
- This amplifies discrete hedging error and makes numerical gamma unstable
- Near-expiry ATM positions require careful risk management
