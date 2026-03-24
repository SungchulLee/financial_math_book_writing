# Volatility Structure Calibration


Beyond fitting today’s curve, interest-rate models must specify and calibrate a **volatility structure** that governs the dynamics of rates and prices of interest-rate options.

---

## What is being calibrated?


Depending on the model, calibration targets include:
- short-rate volatility parameters,
- forward-rate volatilities (HJM),
- cap/floor and swaption implied volatilities.

The volatility structure determines smile, skew, and term-structure dynamics.

---

## Typical calibration instruments


Common calibration instruments are:
- caplets and floorlets,
- caps/floors across maturities,
- swaptions across expiries and tenors.

These instruments are liquid and sensitive to rate volatility.

---

## Model-dependent considerations


- **Short-rate models:** limited flexibility, often need extensions or multi-factor versions.
- **HJM models:** volatility functions calibrated directly to market data.
- **Market models (LMM):** volatilities tied to forward LIBOR rates.

Model choice strongly affects calibration quality.

---

## Regularization and smoothing


Volatility calibration is an inverse problem and often ill-posed.
Stability is improved by:
- smoothness penalties across maturity,
- parsimonious parametrizations,
- restricting factor dimensionality.

Overfitting leads to poor out-of-sample behavior.

---

## Key takeaways


- Volatility structure drives option prices and dynamics.
- Calibration relies on caps and swaptions.
- Regularization is essential for stable volatility surfaces.

---

## Further reading


- Rebonato, *Interest-Rate Option Models*.
- Brigo & Mercurio, volatility calibration.

---

## Exercises

**Exercise 1.** A one-factor Hull--White model has volatility parameter $\sigma$ and mean-reversion speed $a$. You observe at-the-money caplet implied volatilities for maturities 1Y through 10Y. Explain why a single constant $\sigma$ cannot reproduce a humped caplet volatility term structure and describe the minimal extension (e.g., piecewise-constant $\sigma(t)$) needed to fit the observed caplet volatilities exactly.

---

**Exercise 2.** Suppose the market quotes at-the-money cap volatilities (flat volatilities) for maturities $T = 2, 3, 5, 7, 10$ years. Describe the stripping procedure to extract individual caplet volatilities from these flat cap volatilities. If the 5Y flat cap volatility is 18.5% and the 3Y flat cap volatility is 17.0%, is it possible for all caplet volatilities between years 3 and 5 to be below 17.0%? Justify your answer.

---

**Exercise 3.** In the LIBOR Market Model, the instantaneous volatility of forward rate $L_i$ is given by a function $\sigma_i(t)$ of time. Consider the abcd parameterization

$$
\sigma_i(t) = \bigl(a + b(T_i - t)\bigr)e^{-c(T_i - t)} + d
$$

Derive the model Black caplet volatility

$$
v_i^2 = \frac{1}{T_i}\int_0^{T_i} \sigma_i(t)^2\,dt
$$

as a closed-form expression in $(a,b,c,d)$. Verify that for $b = 0$ and $c = 0$ the caplet volatility reduces to $v_i = a + d$.

---

**Exercise 4.** A trader calibrates a two-factor HJM model with volatility functions $\sigma_1(t,T) = \sigma_1 e^{-\kappa_1(T-t)}$ and $\sigma_2(t,T) = \sigma_2 e^{-\kappa_2(T-t)}$ to a grid of swaption prices. The calibrated parameters are $\sigma_1 = 1.2\%$, $\kappa_1 = 0.05$, $\sigma_2 = 0.8\%$, $\kappa_2 = 0.50$. Interpret each factor economically (level vs curvature). Explain how the two factors combine to produce a richer volatility term structure than a single-factor model.

---

**Exercise 5.** You are given a $5 \times 5$ swaption volatility matrix (expiries: 1Y, 2Y, 3Y, 5Y, 7Y; tenors: 1Y, 2Y, 3Y, 5Y, 7Y). Describe a calibration strategy that first targets the ATM diagonal (expiry = tenor) and then uses residual degrees of freedom to match off-diagonal entries. Why might the off-diagonal swaptions be harder to fit, and what does a poor off-diagonal fit reveal about the correlation structure?

---

**Exercise 6.** Consider adding a smoothness penalty to the volatility calibration objective:

$$
\min_{\sigma(\cdot)} \sum_i w_i\bigl(V_i^{\text{model}} - V_i^{\text{mkt}}\bigr)^2 + \lambda \int_0^T \!\left(\frac{d^2\sigma}{dt^2}\right)^2 dt
$$

Explain the role of $\lambda$ and how you would choose it in practice. What happens if $\lambda$ is too large? What if it is too small?

---

**Exercise 7.** A practitioner observes that a calibrated volatility surface reprices all caps and swaptions within 0.5 bps but produces unrealistic forward-rate dynamics when used for Monte Carlo simulation of exotic products (e.g., CMS spread options). Explain why good static calibration does not guarantee good dynamic behavior and discuss at least two diagnostics the practitioner should perform to assess the quality of the calibrated dynamics.
