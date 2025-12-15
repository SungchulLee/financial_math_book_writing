# Non-Stationarity

A fundamental limitation of learning in finance is **non-stationarity**: the statistical properties of financial data change over time.

---

## 1. What is non-stationarity?

A process is non-stationary if:
- distributions evolve over time,
- parameters drift,
- structural breaks occur.

Most financial time series exhibit non-stationarity.

---

## 2. Sources in financial markets

Non-stationarity arises from:
- changing market regimes,
- regulatory and institutional shifts,
- technological innovation,
- endogenous feedback from trading strategies.

These changes invalidate static models.

---

## 3. Impact on learning algorithms

Non-stationarity causes:
- degradation of predictive performance,
- instability of parameter estimates,
- misleading backtests.

Models trained on past data may fail abruptly.

---

## 4. Mitigation strategies

Common approaches include:
- rolling-window estimation,
- adaptive and online learning,
- regime-switching models,
- stress testing beyond historical data.

No method fully eliminates the problem.

---

## 5. Key takeaways

- Financial data is inherently non-stationary.
- Learning performance degrades over time.
- Continuous monitoring is essential.

---

## Further reading

- Cont, model uncertainty and instability.
- Hamilton, regime changes in economics.
