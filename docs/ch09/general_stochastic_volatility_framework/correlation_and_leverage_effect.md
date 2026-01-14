# Correlation and Leverage Effect


A defining feature of equity markets is the **leverage effect**: negative returns are associated with rising volatility. In stochastic volatility models, this is captured by **correlation** between price and volatility shocks.

---

## Correlated Brownian motions


In two-factor models, we allow

\[
d\langle W^S, W^V \rangle_t = \rho\,dt,
\]


with correlation coefficient \(\rho \in [-1,1]\).

This single parameter has a profound impact on option prices.

---

## Leverage effect in equity markets


Empirically:
- equity returns and volatility changes are negatively correlated,
- large price drops are followed by volatility spikes,
- this asymmetry is stable across markets and time.

Negative \(\rho\) reproduces this behavior.

---

## Impact on implied volatility smile


Correlation primarily controls **skew**:

- negative \(\rho\) → downward-sloping implied volatility skew,
- stronger magnitude → steeper skew,
- near-zero \(\rho\) → symmetric smiles.

This explains why skew is persistent even in calm markets.

---

## Dynamic interpretation


Economically, the leverage effect reflects:
- balance-sheet effects,
- changing risk premia,
- asymmetric investor reactions to losses.

Stochastic volatility models encode these effects parsimoniously via correlation.

---

## Key takeaways


- Correlation between price and volatility is essential.
- It explains skew in implied volatility surfaces.
- The leverage effect is a robust empirical fact.

---

## Further reading


- Black (1976), leverage effect.
- Bouchaud et al., empirical studies of skew.
- Gatheral, *The Volatility Surface*.
