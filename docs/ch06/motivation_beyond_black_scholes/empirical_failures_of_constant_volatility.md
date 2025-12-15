# Empirical Failures of Constant Volatility

The Black–Scholes model assumes that volatility is constant over time and across states of the market. While this assumption leads to analytical tractability, it is fundamentally inconsistent with observed market behavior.

---

## 1. The constant volatility assumption

In the Black–Scholes framework, the underlying asset follows
\[
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t,
\]
where the volatility parameter \(\sigma\) is constant.

This implies:
- log-returns are normally distributed,
- return variance grows linearly with time,
- option prices depend on a single volatility parameter.

---

## 2. Empirical evidence against constancy

Market data contradict these implications:

- **Volatility clustering:** periods of high volatility tend to cluster in time.
- **Leverage effect:** volatility increases after negative returns.
- **Time-varying variance:** realized volatility changes substantially over time.

These features are visible across equities, indices, and asset classes.

---

## 3. Distributional failures

Under constant volatility, log-returns are Gaussian. Empirically, returns exhibit:

- heavy tails (excess kurtosis),
- skewness (especially negative),
- extreme events far more frequent than Gaussian predictions.

These features lead to systematic mispricing of out-of-the-money options.

---

## 4. Implications for option pricing

Because option prices reflect the entire return distribution:

- tail mis-specification affects deep OTM options,
- constant volatility cannot fit both ATM and wing prices,
- hedging strategies based on constant \(\sigma\) become unreliable.

This motivates models with richer volatility dynamics.

---

## 5. Key takeaways

- Constant volatility is empirically invalid.
- Volatility is stochastic, clustered, and state-dependent.
- Option markets reveal these failures clearly.

---

## Further reading

- Mandelbrot, early work on heavy-tailed returns.
- Engle, ARCH effects and volatility clustering.
- Cont, *Empirical Properties of Asset Returns*.
