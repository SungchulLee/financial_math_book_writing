# Heston Model Characteristic Function

The characteristic function (CF) is the Fourier transform of the probability density function. For the Heston stochastic volatility model, the characteristic function has a closed-form expression that makes it invaluable for option pricing via Fourier methods.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the Heston characteristic function
    2. Understand the role of the non-centrality parameter
    3. Use the CF for density recovery and option pricing

---

## Heston Model Specification

The Heston (1993) model for asset price and volatility dynamics under the risk-neutral measure is:

\[
dS(t) = r S(t) dt + \sqrt{v(t)} S(t) dW_x^{\mathbb{Q}}(t)
\]

\[
dv(t) = \kappa(\bar{v} - v(t)) dt + \gamma\sqrt{v(t)} dW_v^{\mathbb{Q}}(t)
\]

where the two Brownian motions are correlated: \(d W_x^{\mathbb{Q}} dW_v^{\mathbb{Q}} = \rho dt\).

---

## Characteristic Function Formula

The characteristic function of \(X_T = \log S(T)\) conditional on the initial state \((t, S, v)\) is:

\[
\varphi(u) := \mathbb{E}^{\mathbb{Q}}\left[e^{iu X_T} \big| \mathcal{F}(t)\right] = e^{r(T-t) + A(\tau,u) + B(\tau,u)X + C(\tau,u)v}
\]

where \(\tau = T - t\) is time to maturity, and the components are:

\[
\boxed{
\begin{aligned}
A(\tau,u) &= \frac{\kappa\bar{v}\tau}{\gamma^2}\left(\kappa - \gamma\rho iu - D\right) - \frac{2\kappa\bar{v}}{\gamma^2}\log\left(\frac{1 - ge^{-D\tau}}{1-g}\right)\\[0.5em]
B(\tau,u) &= iu\\[0.5em]
C(\tau,u) &= \frac{1 - e^{-D\tau}}{\gamma^2(1 - ge^{-D\tau})}(\kappa - \gamma\rho iu - D)\\[0.5em]
D &= \sqrt{(\kappa - \gamma\rho iu)^2 + (u^2 + iu)\gamma^2}\\[0.5em]
g &= \frac{\kappa - \gamma\rho iu - D}{\kappa - \gamma\rho iu + D}
\end{aligned}
}
\]

---

## Key Structural Elements

**Complex argument \(D\):** The term \(D\) encodes the interaction between mean reversion rate \(\kappa\), volatility of volatility \(\gamma\), and correlation \(\rho\). The square root ensures the solution is well-defined for all complex arguments \(u\).

**Ratio \(g\):** The ratio \(g\) is crucial for stability in numerical computation and controls the asymptotic behavior as \(\tau \to \infty\).

**Logarithmic term in \(A\):** The log term arises from integrating the CIR-type variance process and captures the mean reversion dynamics.

---

## Transform to Physical Measure

If we wish to transition from the risk-neutral measure \(\mathbb{Q}\) to the physical measure \(\mathbb{P}\), we adjust the mean reversion level and the drift:

\[
dS(t) = \mu S(t) dt + \sqrt{v(t)} S(t) dW_x^{\mathbb{P}}(t)
\]

\[
dv(t) = \kappa(\bar{v}^{\mathbb{P}} - v(t)) dt + \gamma\sqrt{v(t)} dW_v^{\mathbb{P}}(t)
\]

Under Girsanov's theorem, the risk-neutral mean reversion level becomes:

\[
\bar{v} = \bar{v}^{\mathbb{P}} - \frac{\rho\gamma(\mu - r)}{\kappa}
\]

This adjustment ensures consistency between physical and risk-neutral dynamics while preserving the Heston model structure.

---

## Properties and Computational Notes

1. **Affine structure:** The exponent is linear in \(X\) and \(v\), making the Heston model an affine jump-diffusion (without jumps).

2. **Numerical stability:** When computing \(D\) for complex \(u\), care must be taken with the square root branch. Typically, the square root is chosen such that \(\text{Im}(D) > 0\).

3. **Decay at infinity:** As \(|u| \to \infty\), the CF decays sufficiently fast, allowing Fourier inversion via FFT.

4. **Special case:** When \(\rho = 0\), the stock and variance dynamics decouple, simplifying the derivation.

---

## Summary

The Heston characteristic function provides a closed-form expression for the joint distribution of log-returns and variance. Its affine structure enables efficient option pricing through Fourier methods (FFT and COS methods) and is the foundation for understanding smile dynamics and variance-of-variance effects in modern derivatives markets.
