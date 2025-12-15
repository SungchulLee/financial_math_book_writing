# Default Intensity and Hazard Rates

Reduced-form (intensity-based) credit models treat default as an exogenous random event governed by a **default intensity** or **hazard rate**. These models focus on tractability and calibration to market prices.

---

## 1. Default time and intensity

Let \(\tau\) denote the default time. An **intensity process** \((\lambda_t)_{t\ge0}\) is a non-negative, \(\mathcal{F}_t\)-adapted process such that default occurs with conditional probability
\[
\mathbb{Q}(t < \tau \le t+dt \mid \mathcal{F}_t, \tau>t) \approx \lambda_t\,dt.
\]

The intensity governs the instantaneous likelihood of default.

---

## 2. Hazard rate interpretation

The process \(\lambda_t\) is also called the **hazard rate**. Intuitively:
- high \(\lambda_t\) means imminent default risk,
- low \(\lambda_t\) corresponds to near-survival certainty over short horizons.

Unlike structural models, \(\lambda_t\) is not derived from firm value dynamics.

---

## 3. Information structure

Reduced-form models typically assume:
- default is a surprise event,
- \(\tau\) is not predictable from \(\mathcal{F}_t\),
- default information enters only through intensity.

This aligns naturally with progressive enlargement and immersion.

---

## 4. Modeling choices for intensity

Common specifications include:
- deterministic or piecewise-constant intensities,
- affine diffusion intensities (e.g., CIR-type),
- regime-switching or jump-driven intensities.

Choice reflects a trade-off between realism and calibration stability.

---

## 5. Key takeaways

- Default intensity governs instantaneous default risk.
- Hazard rates are exogenous modeling inputs.
- Reduced-form models emphasize tractability and calibration.

---

## Further reading

- Duffie & Singleton, intensity-based credit risk.
- Bielecki & Rutkowski, hazard rate models.
