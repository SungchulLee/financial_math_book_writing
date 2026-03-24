# Vega Risk and Vol-of-Vol


Under stochastic volatility, option risk is no longer captured by delta alone. **Vega risk** and, more subtly, **volatility-of-volatility (vol-of-vol) risk** become central drivers of P&L and hedging performance.

---

## Vega in stochastic volatility models


In Black–Scholes, vega measures sensitivity to a single volatility parameter:

\[
\text{Vega} = \partial_{\sigma} P.
\]



In stochastic volatility models, volatility itself is random, so vega represents sensitivity to:
- the current variance level,
- the volatility state variable,
- the implied volatility surface.

Thus, vega is model- and state-dependent.

---

## Vol-of-vol risk


The parameter (or process) controlling volatility fluctuations—often denoted \(\xi\)—introduces **second-order volatility risk**.

Consequences:
- option prices depend on uncertainty of future volatility,
- convexity in volatility matters,
- products sensitive to smile curvature are especially exposed.

This risk cannot be hedged by delta or vega alone.

---

## Greeks beyond vega


Common higher-order sensitivities include:
- **Volga (vomma):** sensitivity of vega to volatility,
- **Vanna:** cross-sensitivity between spot and volatility,
- sensitivities to variance process parameters.

These Greeks are typically large for long-dated or exotic options.

---

## Practical implications


- Vega hedging with a single option is insufficient.
- Smile dynamics cause residual P&L even for delta–vega neutral portfolios.
- Vol-of-vol risk explains persistent hedging errors in practice.

---

## Key takeaways


- Vega risk is richer under stochastic volatility.
- Vol-of-vol introduces unhedgeable second-order effects.
- Understanding higher-order Greeks is essential for risk management.

---

## Further reading


- Taleb, *Dynamic Hedging*.
- Bergomi, *Stochastic Volatility Modeling*.

---

## Exercises

**Exercise 1.** In the Black-Scholes model, vega is $\partial C/\partial\sigma$, a sensitivity to a single constant parameter. In the Heston model, explain why there are multiple "vega-like" sensitivities: $\partial C/\partial V_0$ (spot variance), $\partial C/\partial\theta$ (long-run variance), and $\partial C/\partial\xi$ (vol-of-vol). For a short-maturity ATM call, which of these three is most important and why?

---

**Exercise 2.** Volga (or vomma) is defined as

$$
\text{Volga} = \frac{\partial^2 C}{\partial\sigma^2} = \frac{\partial\,\text{Vega}}{\partial\sigma}
$$

For a Black-Scholes call, $\text{Volga} = S\sqrt{T}\,n(d_1)\,\frac{d_1 d_2}{\sigma}$ where $n$ is the standard normal density. Compute volga for an ATM call with $S = 100$, $K = 100$, $T = 1$, $\sigma = 0.20$, $r = 0.03$. Is volga positive or negative for ATM options? How does it change for deep OTM options?

---

**Exercise 3.** Vanna measures the cross-sensitivity between spot and volatility:

$$
\text{Vanna} = \frac{\partial^2 C}{\partial S\,\partial\sigma} = \frac{\partial\Delta}{\partial\sigma}
$$

Explain why vanna is especially important when $\rho < 0$ (leverage effect). If the S&P 500 drops 5% and volatility simultaneously increases by 3 vol points, estimate the additional delta change for a portfolio with vanna exposure of $0.05$. Should a trader who is long vanna be worried about a market crash?

---

**Exercise 4.** A delta-vega hedged portfolio has zero exposure to both spot price changes and parallel shifts in implied volatility. However, the portfolio still has P&L risk. Identify at least three sources of residual risk and explain which stochastic volatility parameters they relate to. For each source, name a potential hedging instrument.

---

**Exercise 5.** The vol-of-vol parameter $\xi$ in the Heston model controls the curvature of the implied volatility smile. Consider two portfolios: (a) a short butterfly spread (short wings, long center) and (b) a long straddle. Which portfolio has greater exposure to changes in $\xi$? Explain using the relationship between smile curvature and butterfly prices.

---

**Exercise 6.** A risk manager wants to decompose the daily P&L of a stochastic-volatility-priced option portfolio. Propose a decomposition into the following components and explain how each is computed:

$$
\text{Total P\&L} = \Delta\,dS + \text{Vega}\,d\sigma + \frac{1}{2}\Gamma(dS)^2 + \text{Vanna}\,dS\,d\sigma + \frac{1}{2}\text{Volga}(d\sigma)^2 + \text{Theta}\,dt + \text{Residual}
$$

If $dS = -2$, $d\sigma = +0.015$, $\Delta = 0.50$, $\Gamma = 0.02$, Vega $= 20$, Vanna $= 0.03$, Volga $= 1.5$, Theta $= -0.05$, and $dt = 1/252$, compute each component and the total P&L (assuming zero residual).
