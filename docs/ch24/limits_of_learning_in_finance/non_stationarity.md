# Non-Stationarity


A fundamental limitation of learning in finance is **non-stationarity**: the statistical properties of financial data change over time.

---

## What is non-stationarity?


A process is non-stationary if:
- distributions evolve over time,
- parameters drift,
- structural breaks occur.

Most financial time series exhibit non-stationarity.

---

## Sources in financial markets


Non-stationarity arises from:
- changing market regimes,
- regulatory and institutional shifts,
- technological innovation,
- endogenous feedback from trading strategies.

These changes invalidate static models.

---

## Impact on learning algorithms


Non-stationarity causes:
- degradation of predictive performance,
- instability of parameter estimates,
- misleading backtests.

Models trained on past data may fail abruptly.

---

## Mitigation strategies


Common approaches include:
- rolling-window estimation,
- adaptive and online learning,
- regime-switching models,
- stress testing beyond historical data.

No method fully eliminates the problem.

---

## Key takeaways


- Financial data is inherently non-stationary.
- Learning performance degrades over time.
- Continuous monitoring is essential.

---

## Further reading


- Cont, model uncertainty and instability.
- Hamilton, regime changes in economics.

---

## Exercises

**Exercise 1.** A GARCH(1,1) model $\sigma_t^2 = \omega + \alpha r_{t-1}^2 + \beta \sigma_{t-1}^2$ is estimated on 10 years of daily equity returns. After a major market regime change (e.g., a financial crisis), the estimated parameters shift significantly. Compute the half-life of the GARCH variance process $h = -\log(2)/\log(\alpha + \beta)$ and explain how the persistence parameter $\alpha + \beta$ relates to non-stationarity.

---

**Exercise 2.** Describe the rolling-window estimation approach for a mean-variance portfolio. If the window size is $W = 252$ trading days, explain the trade-off: a larger window provides more data (reducing estimation error) but may include stale data from a different regime (increasing misspecification). How would you choose $W$ optimally?

---

**Exercise 3.** The Augmented Dickey-Fuller (ADF) test examines whether a time series has a unit root (a form of non-stationarity). For the model $\Delta x_t = \alpha + \beta x_{t-1} + \sum_{j=1}^p \gamma_j \Delta x_{t-j} + \varepsilon_t$, explain what the null hypothesis $\beta = 0$ means and how rejection (or non-rejection) informs the choice of learning algorithm for return prediction.

---

**Exercise 4.** In a two-regime Hamilton regime-switching model, returns follow $r_t | s_t = i \sim N(\mu_i, \sigma_i^2)$ with transition matrix $P = \begin{pmatrix} p_{11} & 1-p_{11} \\ 1-p_{22} & p_{22} \end{pmatrix}$. If $p_{11} = 0.98$ and $p_{22} = 0.90$, compute the expected duration of each regime and the stationary probability of being in each regime. Explain why models trained on data predominantly from regime 1 may fail catastrophically in regime 2.

---

**Exercise 5.** An online learning algorithm uses exponential weighting with decay parameter $\lambda$: $\hat{\mu}_t = (1-\lambda)\hat{\mu}_{t-1} + \lambda r_t$. Show that this is equivalent to a weighted average with exponentially declining weights. For what value of $\lambda$ does the effective window size equal approximately 60 days? How does $\lambda$ trade off responsiveness to regime changes against noise sensitivity?

---

**Exercise 6.** Non-stationarity can be structural (permanent regime change) or transient (temporary dislocation). Design a monitoring system that distinguishes between these two cases using: (a) CUSUM tests for detecting structural breaks, and (b) mean-reversion tests for detecting transient dislocations. Explain why the appropriate response differs: recalibration for structural breaks versus patience for transient dislocations.
