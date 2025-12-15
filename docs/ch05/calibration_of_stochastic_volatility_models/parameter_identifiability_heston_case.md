# Parameter Identifiability (Heston Case)

Stochastic volatility models introduce latent dynamics that improve realism but complicate calibration. The Heston model is the canonical example where **parameter identifiability** is partial and maturity-dependent.

---

## 1. The Heston model

Under the risk-neutral measure \(\mathbb{Q}\), the Heston model is
\[
\begin{aligned}
dS_t &= (r-q)S_t\,dt + \sqrt{V_t}\,S_t\,dW_t^S,\\
dV_t &= \kappa(\theta - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^V,\\
d\langle W^S, W^V \rangle_t &= \rho\,dt,
\end{aligned}
\]
with parameters:
- \(\kappa\): mean-reversion speed,
- \(\theta\): long-run variance,
- \(\xi\): volatility of volatility,
- \(\rho\): spot/vol correlation,
- \(V_0\): initial variance.

---

## 2. Structural versus practical identifiability

### 2.1 Structural identifiability

In theory, a sufficiently rich set of option prices across strikes and maturities uniquely determines the Heston parameters (up to mild degeneracies).

### 2.2 Practical identifiability

In practice:
- market data are finite and noisy,
- sensitivities vary strongly across maturities,
- some parameters affect prices in similar ways.

As a result, several parameters are only **weakly identifiable**.

---

## 3. Sensitivity by maturity

Different parameters dominate at different horizons:

- **Short maturities:**
  - \(V_0\) and instantaneous variance dominate,
  - weak sensitivity to \(\kappa\) and \(\theta\).
- **Medium maturities:**
  - \(\xi\) and \(\rho\) affect smile curvature and skew.
- **Long maturities:**
  - \(\theta\) and \(\kappa\) dominate the term structure.

This implies that calibrating to a narrow maturity range leads to parameter entanglement.

---

## 4. Common degeneracies

Typical near-degeneracies include:

- \(V_0\) vs \(\theta\): both control variance level,
- \(\kappa\) vs \(\theta\): slow mean reversion mimics a shifted long-run level,
- \(\xi\) vs \(\rho\): both influence smile curvature.

These appear as flat directions in the loss landscape.

---

## 5. Diagnostics for identifiability

Practical tools include:

- **Jacobian/SVD analysis** across the surface,
- **profile likelihoods** for each parameter,
- **fix-and-refit experiments** (freeze one parameter),
- **time stability checks** across trading days.

---

## 6. Improving identifiability

- use a wide range of maturities,
- incorporate skew-sensitive instruments (OTM puts/calls),
- impose economically motivated bounds,
- regularize weakly identified parameters (see Chapter 5.3).

---

## 7. Key takeaways

- Not all Heston parameters are equally identifiable from vanillas.
- Identifiability is maturity-dependent.
- Stability often improves by constraining or regularizing weak directions.

---

## Further reading

- Heston (1993), “A Closed-Form Solution for Options with Stochastic Volatility”.
- Gatheral, *The Volatility Surface*.
- Andersen & Piterbarg, practitioner discussions on Heston calibration.
