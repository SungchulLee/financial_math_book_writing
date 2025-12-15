# SABR Model

The SABR model is a widely used **stochastic volatility model** designed to capture smile dynamics with a parsimonious parameterization. It is especially popular in interest-rate and FX markets, but its concepts generalize to equity volatility modeling.

---

## 1. Model definition

Under the risk-neutral measure, the SABR model is defined by
\[
\begin{aligned}
dF_t &= \sigma_t F_t^{\beta}\,dW_t^F,\\
d\sigma_t &= \nu\,\sigma_t\,dW_t^{\sigma},\\
d\langle W^F, W^{\sigma} \rangle_t &= \rho\,dt,
\end{aligned}
\]
where:
- \(F_t\) is the forward price,
- \(\sigma_t\) is stochastic volatility,
- \(\beta \in [0,1]\) controls elasticity,
- \(\nu\) is vol-of-vol,
- \(\rho\) is correlation.

---

## 2. Interpretation of parameters

- **\(\beta\):** interpolates between normal (\(\beta=0\)) and lognormal (\(\beta=1\)) dynamics,
- **\(\nu\):** controls smile curvature,
- **\(\rho\):** controls skew,
- **initial \(\sigma_0\):** sets ATM level.

This makes SABR intuitive and flexible.

---

## 3. Approximate implied volatility formula

A key feature of SABR is the **asymptotic implied volatility formula** (Hagan et al.), which provides:
- fast pricing,
- analytical calibration,
- explicit smile dependence.

Although approximate, it is highly accurate for many markets.

---

## 4. Strengths and limitations

Strengths:
- parsimonious (few parameters),
- closed-form implied volatility approximation,
- excellent smile fit near ATM.

Limitations:
- approximation accuracy deteriorates far from ATM,
- limited dynamic consistency,
- less suitable for long-dated equity options.

---

## 5. Key takeaways

- SABR is a practical smile model.
- Its popularity stems from analytical tractability.
- It is best viewed as a local-stochastic hybrid.

---

## Further reading

- Hagan et al., *Managing Smile Risk*.
- Rebonato, *Interest-Rate Option Models*.
