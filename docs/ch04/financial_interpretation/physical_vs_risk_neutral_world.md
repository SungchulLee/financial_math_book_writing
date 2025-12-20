# Physical vs Risk-Neutral World

The distinction between the physical and risk-neutral probability measures is
one of the most common sources of confusion in quantitative finance.

This section clarifies their respective roles.

---

## The Physical Measure \(\mathbb{P}\)

The physical (or real-world) measure describes how asset prices actually evolve.
It reflects:
- economic growth,
- investor risk preferences,
- empirical return distributions.

Under \(\mathbb{P}\), expected returns include risk premia.

---

## The Risk-Neutral Measure \(\mathbb{Q}\)

The risk-neutral measure is a **pricing tool**, not a description of reality.
Under \(\mathbb{Q}\):
- discounted asset prices are martingales,
- expected excess returns vanish,
- probabilities are adjusted for risk.

It is constructed mathematically via Girsanov’s theorem or numéraire techniques.

---

## Same Paths, Different Weights

A crucial point is that \(\mathbb{P}\) and \(\mathbb{Q}\) are **equivalent measures**:
- they assign positive probability to the same events,
- but with different likelihoods.

Thus, measure change does not alter which scenarios are possible,
only how they are weighted.

---

## Why \(\mathbb{Q}\) Is Not “Believed”

The risk-neutral measure should not be interpreted as:
- a forecast of future prices,
- an investor’s belief,
- a statistical model of returns.

Its sole purpose is to ensure arbitrage-free pricing.

Forecasting and risk management must be performed under \(\mathbb{P}\).

---

## Practical Implications

- Use \(\mathbb{Q}\) for pricing derivatives.
- Use \(\mathbb{P}\) for risk, forecasting, and portfolio optimization.
- Mixing the two leads to systematic errors.

---

## Takeaway

> The physical measure explains the world.
> The risk-neutral measure prices claims in it.

Keeping this distinction clear is essential for both theoretical understanding
and practical modeling.
