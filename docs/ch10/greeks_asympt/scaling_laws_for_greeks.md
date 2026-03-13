# Scaling Laws for Greeks


This section provides a unified framework for understanding how Greeks scale with time-to-maturity \(\tau\) and moneyness.

---

## Near-the-money ATM scaling table


For at-the-money options (\(S \approx K\)) in Black–Scholes:

| Greek | ATM Formula | Scaling in \(\tau\) | Behavior as \(\tau \to 0\) |
|:------|:------------|:--------------------|:---------------------------|
| \(\Delta\) | \(N(d_1) \approx \frac{1}{2}\) | \(\mathcal{O}(1)\) | \(\to \frac{1}{2}\) |
| \(\Gamma\) | \(\frac{1}{S\sigma\sqrt{2\pi\tau}}\) | \(\tau^{-1/2}\) | \(\to \infty\) |
| \(\Theta\) | \(-\frac{S\sigma}{2\sqrt{2\pi\tau}}\) | \(\tau^{-1/2}\) | \(\to -\infty\) |
| \(\nu\) (Vega) | \(\frac{S\sqrt{\tau}}{\sqrt{2\pi}}\) | \(\tau^{1/2}\) | \(\to 0\) |
| \(\rho\) | \(\frac{K\tau}{2}e^{-r\tau}\) | \(\tau\) | \(\to 0\) |

---

## Theta-Gamma relationship


A fundamental identity links theta and gamma for delta-hedged positions:

\[
\boxed{\Theta + \frac{1}{2}\sigma^2 S^2 \Gamma = rV - rS\Delta}
\]

For ATM options where \(\Delta \approx \frac{1}{2}\) and \(V \approx \frac{S\sigma\sqrt{\tau}}{\sqrt{2\pi}}\):

\[
\Theta \approx -\frac{1}{2}\sigma^2 S^2 \Gamma + \mathcal{O}(\sqrt{\tau})
\]

This shows that **time decay and gamma are two sides of the same coin**: options with high gamma (convexity benefit) must pay for it through time decay.

---

## Dimensional analysis


Greeks can be understood through dimensional analysis. Let \([X]\) denote the dimension of \(X\):

| Quantity | Dimension |
|:---------|:----------|
| \(V\) (price) | \(\$\) |
| \(S\) (spot) | \(\$\) |
| \(\tau\) (time) | \(T\) |
| \(\sigma\) (volatility) | \(T^{-1/2}\) |

Then:
- \(\Delta = \partial V/\partial S\) is dimensionless
- \(\Gamma = \partial^2 V/\partial S^2\) has dimension \(\$^{-1}\)
- \(\Theta = \partial V/\partial t\) has dimension \(\$/T\)
- \(\nu = \partial V/\partial \sigma\) has dimension \(\$ \cdot T^{1/2}\)

The ATM scalings follow from \(V_{\text{ATM}} \sim S\sigma\sqrt{\tau}\):

\[
\Gamma_{\text{ATM}} \sim \frac{V}{S^2} \cdot \frac{1}{\sigma\sqrt{\tau}} \sim \frac{1}{S\sigma\sqrt{\tau}}
\]

---

## Far from the money: exponential decay


For OTM options with log-moneyness \(x = \ln(K/S)\):

| Greek | OTM decay rate |
|:------|:---------------|
| \(\Delta\) | \(\exp(-x^2/(2\sigma^2\tau))\) |
| \(\Gamma\) | \(\frac{1}{S}\exp(-x^2/(2\sigma^2\tau))\) |
| \(\nu\) | \(S\sqrt{\tau}\exp(-x^2/(2\sigma^2\tau))\) |

The characteristic scale separating ATM from OTM is \(|x| \sim \sigma\sqrt{\tau}\).

---

## Unified asymptotic expansion


For options near ATM as \(\tau \to 0\), all Greeks can be expanded in powers of \(\sqrt{\tau}\):

**Price:**
\[
V = V_0 + V_1 \sqrt{\tau} + V_2 \tau + \mathcal{O}(\tau^{3/2})
\]

where \(V_0 = (S-K)^+\) (intrinsic), \(V_1 = \frac{S\sigma}{\sqrt{2\pi}}\mathbf{1}_{\text{ATM}}\) (ATM time value).

**Greeks:**
\[
\Gamma = \frac{1}{S\sigma\sqrt{2\pi\tau}} + \mathcal{O}(1)
\]
\[
\Theta = -\frac{S\sigma}{2\sqrt{2\pi\tau}} + \mathcal{O}(1)
\]
\[
\nu = \frac{S\sqrt{\tau}}{\sqrt{2\pi}} + \mathcal{O}(\tau)
\]

---

## Medium maturity: vega dominance


For moderate maturities (\(\tau \sim 1\) year), vega often dominates portfolio risk:

- Vega is maximized around \(\tau \sim 1/(2r)\) for typical interest rates
- Gamma remains bounded: \(\Gamma \sim \frac{1}{S\sigma}\)
- Theta-vega ratio: \(\Theta/\nu \sim -\sigma/(2\tau)\)

---

## Long maturity asymptotics


For \(\tau \to \infty\):

**Call price:** \(C \to S\) (assuming no dividends)

**Greeks:**
- \(\Delta \to 1\)
- \(\Gamma \to 0\) as \(\tau^{-1/2}\)
- \(\nu \to S\sqrt{\tau}N'(d_1) \sim S\sqrt{\tau}/\sqrt{2\pi}\) grows without bound
- \(\rho \to K\tau e^{-r\tau}N(d_2)\) grows then decays

---

## Practical implications


1. **Short-dated options**: Large gamma, unstable delta hedging, high theta decay
2. **Medium-dated options**: Vega dominance, sensitivity to implied vol changes
3. **Long-dated options**: Low gamma, stable delta, model risk concerns

---

## Greeks scaling summary


\[
\boxed{
\begin{aligned}
&\text{ATM, short maturity:} & \Gamma &\sim \tau^{-1/2}, & \nu &\sim \tau^{1/2}, & \Theta &\sim -\tau^{-1/2} \\
&\text{OTM, any maturity:} & \text{All} &\sim \exp(-x^2/(2\sigma^2\tau))
\end{aligned}
}
\]

---

## What to remember


- Short-dated ATM options: large gamma (\(\tau^{-1/2}\)), unstable higher Greeks
- Vega scales as \(\sqrt{\tau}\), peaking at moderate maturities
- Theta and gamma are linked: \(\Theta \approx -\frac{1}{2}\sigma^2 S^2 \Gamma\) for ATM
- Extreme strikes: tail-dominated sensitivities with exponential decay
- Dimensional analysis provides quick scaling estimates
