# Volatility Risk Premium


Stochastic volatility models distinguish between **risk-neutral** and **physical** volatility dynamics. The gap between them is captured by the **volatility risk premium (VRP)**, which has direct implications for calibration and interpretation.

---

## Risk-neutral calibration


Option prices identify parameters under the risk-neutral measure \(\mathbb{Q}\).
These parameters reflect:
- investor risk preferences,
- compensation for unhedgeable volatility risk.

They should not be confused with historical estimates.

---

## Physical dynamics


Historical time-series analysis estimates parameters under the physical measure \(\mathbb{P}\).
Empirically:
- realized volatility is lower than option-implied variance,
- volatility shocks earn negative premia.

---

## Implications for calibration


Mixing \(\mathbb{P}\) and \(\mathbb{Q}\) parameters without modeling VRP leads to:

- inconsistent dynamics,
- misleading economic interpretation,
- degraded calibration stability.

Calibration should be measure-consistent.

---

## Joint modeling approaches


Advanced frameworks introduce:
- explicit VRP processes,
- joint estimation using options and realized variance,
- Bayesian separation of measures.

These improve interpretability but increase complexity.

---

## Key takeaways


- Volatility risk premium explains discrepancies between historical and implied volatility.
- Option calibration recovers risk-neutral dynamics only.
- Measure consistency is essential.

---

## Further reading


- Bollerslev et al., variance risk premium.
- Carr & Wu, volatility premia.

---

## Exercises

**Exercise 1.** A Heston model calibrated to 3-month S&P 500 options gives $\theta^{\mathbb{Q}} = 0.052$ and $\kappa^{\mathbb{Q}} = 3.5$. Time-series estimation from daily returns gives $\theta^{\mathbb{P}} = 0.038$ and $\kappa^{\mathbb{P}} = 1.8$. Compute the ratio $\theta^{\mathbb{Q}}/\theta^{\mathbb{P}}$ and $\kappa^{\mathbb{Q}}/\kappa^{\mathbb{P}}$. Interpret the difference in each parameter in terms of the volatility risk premium.

---

**Exercise 2.** The VIX index (squared, divided by 100) approximates the 30-day risk-neutral expected variance $\mathbb{E}^{\mathbb{Q}}[\sigma^2]$. Suppose VIX $= 22$ (so $\mathbb{E}^{\mathbb{Q}}[\sigma^2] \approx (22\%)^2 = 0.0484$) and subsequent realized variance over 30 days is $(17\%)^2 = 0.0289$. Compute the VRP for this period. If a trader systematically sells 30-day variance swaps at the VIX level, what is the expected annualized return in volatility points?

---

**Exercise 3.** A practitioner calibrates a Heston model to options data and uses the risk-neutral parameters $(\kappa^{\mathbb{Q}}, \theta^{\mathbb{Q}})$ for a VaR calculation. Explain why this is incorrect. Specifically, if $\kappa^{\mathbb{Q}} > \kappa^{\mathbb{P}}$, how would the VaR estimate be affected? Would the risk-neutral VaR overestimate or underestimate the true risk?

---

**Exercise 4.** Describe a joint estimation procedure that uses both option prices and realized variance data. Specifically, for the Heston model with volatility risk premium $\lambda^V = \lambda\sqrt{V}$: (a) what data goes into the $\mathbb{Q}$-likelihood? (b) what data goes into the $\mathbb{P}$-likelihood? (c) what parameters are shared across both likelihoods? (d) what parameters are identified only from one data source?

---

**Exercise 5.** The relationship $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda\xi$ connects the two measures. Given $\xi = 0.4$ and estimates $\kappa^{\mathbb{P}} = 2.0$, $\kappa^{\mathbb{Q}} = 3.2$, compute $\lambda$. Then compute $\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/\kappa^{\mathbb{Q}}$ for $\theta^{\mathbb{P}} = 0.04$. Is the resulting $\theta^{\mathbb{Q}} > \theta^{\mathbb{P}}$ or $\theta^{\mathbb{Q}} < \theta^{\mathbb{P}}$? Interpret this result economically.

---

**Exercise 6.** Explain why the VRP tends to be larger (more positive) during periods of market stress. Consider the following three mechanisms and explain how each contributes: (a) increased demand for portfolio insurance (OTM puts); (b) higher risk aversion during downturns; (c) correlation of volatility spikes with negative wealth shocks. Which mechanism do you think is most important?
