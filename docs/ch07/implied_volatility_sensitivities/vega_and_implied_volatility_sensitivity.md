# Vega and Implied Volatility Sensitivity


Implied volatility sensitivities play a central role in option risk management. Among them, **vega** measures how option prices respond to changes in implied volatility and serves as the primary channel through which volatility risk is transmitted.

---

## Definition of vega


For an option with price \(P\) and implied volatility \(\sigma_{\text{impl}}\), **vega** is defined as

\[
\text{Vega} = \frac{\partial P}{\partial \sigma_{\text{impl}}}.
\]



In the Black–Scholes model, vega has a closed-form expression and is:
- positive for both calls and puts,
- largest for at-the-money options,
- decreasing for very short or very long maturities.

---

## Vega as sensitivity to market quotes


Because implied volatility is the market-quoted variable, vega measures sensitivity to **observable market moves** rather than model parameters.

Small changes in implied volatility lead to price changes approximated by:

\[
\Delta P \approx \text{Vega} \cdot \Delta \sigma_{\text{impl}}.
\]



This linear approximation underlies most day-to-day volatility risk management.

---

## Dependence on strike and maturity


Vega depends strongly on:
- **moneyness:** highest near ATM,
- **maturity:** increases with time to expiry (up to a point),
- **interest rates and forwards:** through discounting and normalization.

As a result, vega exposure is distributed unevenly across an option book.

---

## Beyond Black–Scholes


Outside Black–Scholes:
- vega depends on the assumed smile dynamics,
- implied vol sensitivity may differ across strikes,
- model-consistent vegas may diverge from quote-based vegas.

This motivates careful interpretation of vega hedges.

---

## Key takeaways


- Vega measures price sensitivity to implied volatility.
- It is largest near ATM and for intermediate maturities.
- Vega is a first-order approximation and must be interpreted carefully in smile models.

---

## Further reading


- Hull, *Options, Futures, and Other Derivatives*.
- Taleb, *Dynamic Hedging*.
