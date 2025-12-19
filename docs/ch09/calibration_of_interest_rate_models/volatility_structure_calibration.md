# Volatility Structure Calibration

Beyond fitting today’s curve, interest-rate models must specify and calibrate a **volatility structure** that governs the dynamics of rates and prices of interest-rate options.

---

## 1. What is being calibrated?

Depending on the model, calibration targets include:
- short-rate volatility parameters,
- forward-rate volatilities (HJM),
- cap/floor and swaption implied volatilities.

The volatility structure determines smile, skew, and term-structure dynamics.

---

## 2. Typical calibration instruments

Common calibration instruments are:
- caplets and floorlets,
- caps/floors across maturities,
- swaptions across expiries and tenors.

These instruments are liquid and sensitive to rate volatility.

---

## 3. Model-dependent considerations

- **Short-rate models:** limited flexibility, often need extensions or multi-factor versions.
- **HJM models:** volatility functions calibrated directly to market data.
- **Market models (LMM):** volatilities tied to forward LIBOR rates.

Model choice strongly affects calibration quality.

---

## 4. Regularization and smoothing

Volatility calibration is an inverse problem and often ill-posed.
Stability is improved by:
- smoothness penalties across maturity,
- parsimonious parametrizations,
- restricting factor dimensionality.

Overfitting leads to poor out-of-sample behavior.

---

## 5. Key takeaways

- Volatility structure drives option prices and dynamics.
- Calibration relies on caps and swaptions.
- Regularization is essential for stable volatility surfaces.

---

## Further reading

- Rebonato, *Interest-Rate Option Models*.
- Brigo & Mercurio, volatility calibration.
