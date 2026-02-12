# Vega Asymptotics and Smile Sensitivity


Vega concentrates near the money and vanishes as maturity shrinks. In models with a volatility smile, the concept of vega generalizes from a single scalar to a multi-dimensional surface sensitivity.

---

## Black–Scholes vega: closed form


In the Black–Scholes model, vega for both calls and puts is

\[
\nu = S\sqrt{\tau}\,N'(d_1) = S\sqrt{\tau}\,\frac{1}{\sqrt{2\pi}}\exp\!\left(-\frac{d_1^2}{2}\right)
\]

where \(d_1 = \frac{\ln(S/K) + (r + \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}\). Note that vega is always non-negative: higher volatility always increases the value of a vanilla option.

---

## Near-the-money scaling


When \(S \approx K\) (ATM), we have \(d_1 \approx \frac{(r + \frac{1}{2}\sigma^2)\sqrt{\tau}}{\sigma} = \mathcal{O}(\sqrt{\tau})\), so \(N'(d_1) \approx \frac{1}{\sqrt{2\pi}}\). Therefore

\[
\boxed{\nu_{\text{ATM}} \approx \frac{S\sqrt{\tau}}{\sqrt{2\pi}} \sim S\sqrt{\tau}}
\]

Key observations:

- Vega scales as \(\sqrt{\tau}\) for ATM options: it vanishes at expiry but slowly.
- For fixed \(\tau\), vega peaks at-the-money and decays as the option moves OTM or deep ITM.
- The peak vega value grows with maturity, making long-dated ATM options most sensitive to volatility.

---

## Away-from-the-money decay


For \(|x| = |\ln(S/K)| \gg \sigma\sqrt{\tau}\), the Gaussian factor dominates:

\[
\nu \sim S\sqrt{\tau}\,\exp\!\left(-\frac{x^2}{2\sigma^2\tau}\right)
\]

This shows vega decays **exponentially** in the square of log-moneyness, normalized by \(\sigma^2\tau\). Deep ITM and OTM options have negligible vega for short maturities.

---

## Short-maturity asymptotics


As \(\tau \to 0\) with fixed moneyness:

\[
\nu \to 0 \quad \text{for all } S \neq K
\]

The rate of decay depends on moneyness:

- **ATM** (\(S = K\)): \(\nu \sim \sqrt{\tau}\), slow decay.
- **OTM/ITM**: \(\nu \sim \sqrt{\tau}\exp(-x^2/(2\sigma^2\tau))\), exponentially fast decay.

In the rescaled variable \(z = x/(\sigma\sqrt{\tau})\), vega has the inner-layer form

\[
\nu \approx \frac{S\sqrt{\tau}}{\sqrt{2\pi}}\exp\!\left(-\frac{z^2}{2}\right)
\]

showing that vega concentrates on a band of width \(\sigma\sqrt{\tau}\) in log-moneyness — the same boundary layer that governs delta and gamma near expiry.

---

## Vega and the theta-gamma relationship


From the Black–Scholes PDE, there is a direct link between vega and gamma:

\[
\nu = \sigma S^2 \tau \,\Gamma
\]

This identity shows that vega and gamma are proportional (in Black–Scholes), with the proportionality factor \(\sigma S^2 \tau\). Consequently:

- Vega risk and gamma risk are not independent in Black–Scholes.
- Hedging gamma automatically hedges vega in this model (but not in stochastic volatility models).

---

## Smile models: generalized vega


With an implied volatility surface \(\Sigma(T,K)\), the Black–Scholes vega measures sensitivity to a **parallel shift** of the entire surface. In practice, the surface deforms non-uniformly, motivating several generalizations:

**Bucket vega.** Partition the surface into regions (buckets) by maturity and strike, and compute sensitivity to a shift in each bucket independently:

\[
\nu_{ij} = \frac{\partial V}{\partial \Sigma_{ij}}
\]

where \(\Sigma_{ij}\) is the implied vol in bucket \((T_i, K_j)\). This gives a **vega matrix** rather than a single number.

**Vega by maturity (term structure vega).** For portfolios of options at different maturities, compute sensitivity to shifts in each maturity slice:

\[
\nu(T_i) = \sum_{j} \frac{\partial V_j}{\partial \sigma(T_i)}
\]

**Model vega.** In parametric models (Heston, SABR), vega can be defined with respect to each model parameter. For the Heston model with parameters \((\bar{v}, \kappa, \xi, \rho, v_0)\):

\[
\frac{\partial V}{\partial v_0}, \quad \frac{\partial V}{\partial \bar{v}}, \quad \frac{\partial V}{\partial \xi}
\]

each measure a different aspect of volatility sensitivity.

---

## Vega convexity (volga/vomma)


The second derivative of the option price with respect to volatility is called **volga** (or vomma):

\[
\text{Volga} = \frac{\partial^2 V}{\partial \sigma^2} = \frac{\partial \nu}{\partial \sigma}
\]

In Black–Scholes:

\[
\text{Volga} = \nu \cdot \frac{d_1 d_2}{\sigma}
\]

Volga is positive for OTM/ITM options (\(d_1 d_2 > 0\)) and negative for ATM options (\(d_1 d_2 < 0\) when \(d_1\) and \(d_2\) have opposite signs). Volga matters for:

- Pricing convexity adjustments in smile models.
- Understanding the P&L of vega-hedged positions when volatility moves substantially.

---

## Practical implications


**Vega exposure management.** A portfolio's aggregate vega determines its first-order exposure to implied volatility shifts. Vega-neutral portfolios combine long and short options to achieve \(\sum_i \nu_i = 0\).

**Maturity mismatch.** Hedging a long-dated option's vega with short-dated options requires more contracts (since short-dated vega \(\sim \sqrt{\tau_{\text{short}}}\) is smaller) and introduces term structure risk.

**Vega and P&L attribution.** For a portfolio with vega \(\nu\), an implied vol move of \(\Delta\sigma\) generates approximate P&L:

\[
\Delta V \approx \nu \cdot \Delta\sigma + \frac{1}{2}\text{Volga}\cdot(\Delta\sigma)^2
\]

---

## What to remember


- Short-maturity vega vanishes but localizes sharply near ATM, scaling as \(\sqrt{\tau}\).
- In Black–Scholes, vega is proportional to gamma via \(\nu = \sigma S^2 \tau \Gamma\).
- In smile models, vega is multi-dimensional (surface risk), requiring bucket vegas or model-parameter sensitivities.
- Volga (vega convexity) matters for large vol moves and smile pricing adjustments.
