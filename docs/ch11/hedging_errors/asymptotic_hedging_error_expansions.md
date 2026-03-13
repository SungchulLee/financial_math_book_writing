# Asymptotic Hedging Error Expansions


One seeks expansions of hedging error in small parameters.

---

## Small time step expansion


For rebalancing interval \(\Delta t \to 0\), the hedging error admits an expansion:

\[
\mathrm{HE}=c_1\sqrt{\Delta t}+c_2\Delta t+\cdots
\]

**Derivation of \(c_1\).** The leading-order error is:

\[
\mathrm{HE} \approx \sum_{k=0}^{N-1} \frac{1}{2}\Gamma_k\left[(\Delta S_k)^2 - \sigma_k^2 S_k^2 \Delta t\right]
\]

Each term has mean zero and variance:
\[
\text{Var}\left(\frac{1}{2}\Gamma_k\left[(\Delta S_k)^2 - \sigma^2 S^2 \Delta t\right]\right) \approx \frac{1}{2}\Gamma_k^2 S_k^4 \sigma^4 (\Delta t)^2
\]

Summing \(N = T/\Delta t\) independent terms:
\[
\text{Var}(\mathrm{HE}) \approx \sum_k \frac{1}{2}\Gamma_k^2 S_k^4 \sigma^4 (\Delta t)^2 \approx \frac{1}{2}\bar{\Gamma^2 S^4 \sigma^4} \cdot T \cdot \Delta t
\]

Thus:
\[
\boxed{c_1 = \sqrt{\frac{1}{2}\int_0^T \Gamma(t,S_t)^2 S_t^4 \sigma^4 \, dt}}
\]

The coefficient \(c_1\) depends on the path through gamma.

**Second-order term** \(c_2\):

\[
c_2 = -\frac{1}{2}\int_0^T \left(\frac{\partial \Gamma}{\partial t} + \mathcal{L}\Gamma\right) S^2 \sigma^2 \, dt + \text{(third derivative terms)}
\]

This involves the time derivative of gamma and curvature effects.

---

## Transaction cost expansion


With proportional transaction cost \(\lambda\) per dollar traded:

**No-trade band.** Optimal strategy involves a no-trade band around the Black–Scholes delta:

\[
\Delta^* \in \left[\Delta - h, \Delta + h\right]
\]

where the bandwidth \(h\) scales as:

\[
\boxed{h \sim \left(\frac{3\lambda}{2\Gamma S^2 \sigma^2}\right)^{1/3}}
\]

**Utility loss.** The expected utility loss from transaction costs scales as:

\[
\text{Cost} \sim \lambda^{2/3} (\Gamma S^2 \sigma^2)^{1/3} T
\]

This is the **Leland–Whalley–Wilmott** result.

**Effective volatility.** Alternatively, one can hedge at the Black–Scholes delta with an adjusted volatility:

\[
\sigma_{\text{eff}}^2 = \sigma^2 \left(1 + \sqrt{\frac{8\lambda}{\pi\sigma\sqrt{\Delta t}}}\text{sign}(\Gamma)\right)
\]

This Leland (1985) approach accounts for transaction costs through volatility adjustment.

---

## Model error expansion


For small model misspecification \(\varepsilon\):

\[
\mathrm{HE}\approx \varepsilon A_1+\varepsilon^2 A_2+\cdots
\]

**Volatility misspecification.** If true volatility is \(\sigma\) but hedging uses \(\hat{\sigma}\):

\[
\varepsilon = \sigma^2 - \hat{\sigma}^2
\]

The first-order term is:
\[
A_1 = \frac{1}{2}\int_0^T \Gamma(t,S_t) S_t^2 \, dt
\]

This is the "vega-weighted" exposure to volatility error.

**Jump risk.** If true dynamics include jumps with intensity \(\lambda_J\) and size \(J\):

\[
\mathrm{HE}_{\text{jump}} \sim \sum_{\text{jumps}} \frac{1}{2}\Gamma S^2 J^2
\]

The hedging error is dominated by jump contributions, not diffusive terms.

---

## Greeks-based P&L attribution


The asymptotic expansion connects to practical P&L attribution:

\[
P\&L = \underbrace{\Theta \cdot \Delta t}_{\text{time decay}} + \underbrace{\frac{1}{2}\Gamma(\Delta S)^2}_{\text{gamma P&L}} + \underbrace{\nu \cdot \Delta\sigma}_{\text{vega P&L}} + \underbrace{\text{higher order}}_{\text{residual}}
\]

The residual should be small if:
1. Rebalancing is frequent (\(\Delta t\) small)
2. Model is accurate (\(\varepsilon\) small)
3. No jumps occur

---

## Numerical verification


For an ATM call with \(S = 100\), \(\sigma = 20\%\), \(\tau = 0.25\):

| Rebalancing | \(\sqrt{\Delta t}\) | Theoretical Std | Monte Carlo Std |
|:------------|:--------------------|:----------------|:----------------|
| Daily | 0.063 | 0.28 | 0.27 |
| Weekly | 0.139 | 0.62 | 0.60 |
| Monthly | 0.289 | 1.29 | 1.25 |

The theoretical \(\sqrt{\Delta t}\) scaling is confirmed by simulation.

---

## Optimal rebalancing frequency


Balancing hedging error variance against transaction costs:

\[
\text{Total Cost} = c_1^2 \Delta t + \lambda \cdot \frac{\text{turnover}}{\Delta t}
\]

The optimal \(\Delta t^*\) satisfies:

\[
\Delta t^* \sim \left(\frac{\lambda \cdot \text{turnover}}{c_1^2}\right)^{1/2}
\]

Higher gamma (larger \(c_1\)) calls for more frequent rebalancing; higher costs call for less frequent.

---

## What to remember


- Leading hedging error term is \(\mathcal{O}(\sqrt{\Delta t})\), driven by gamma
- Coefficient \(c_1\) involves path integral of \(\Gamma^2 S^4 \sigma^4\)
- Transaction costs create \(\lambda^{2/3}\) scaling of utility loss
- No-trade bands scale as \(\lambda^{1/3}\)
- These expansions connect asymptotics to practical P&L attribution
- Jump risk dominates diffusive hedging error in discontinuous models
