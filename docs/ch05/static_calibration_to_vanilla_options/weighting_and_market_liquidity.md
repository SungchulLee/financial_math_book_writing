# Weighting and Market Liquidity

Calibration is only as good as its treatment of **quote quality**. Two instruments can have the same mid price but very different reliability due to liquidity, bid/ask width, and microstructure effects. Weighting schemes translate market reality into the objective function.

---

## 1. Why weights matter

Consider weighted least squares:
\[
\mathcal{L}(\theta)=\frac12\sum_{j=1}^m w_j\,r_j(\theta)^2,
\qquad r_j(\theta)=f_j(\theta)-y_j.
\]

- Large \(w_j\): the optimizer will prioritize fitting instrument \(j\).
- Small \(w_j\): instrument \(j\) is effectively down-weighted (treated as noisy/unreliable).

Without sensible weights, calibration may overfit illiquid points and produce unstable parameters.

---

## 2. Using bid/ask spreads as noise proxies

A common heuristic is:
\[
w_j \propto \frac{1}{\text{(bid-ask)}_j^2}.
\]

Intuition:
- wide spreads imply large uncertainty,
- tight spreads imply reliable pricing information.

Variants:
- use half-spread as standard deviation,
- cap weights to avoid a few ultra-tight quotes dominating,
- add a floor to spreads to prevent infinite weights.

---

## 3. Liquidity and surface regions

Liquidity is not uniform across the surface:

- near-the-money options are usually most liquid,
- very short maturities can be noisy (discrete dividends, microstructure),
- far OTM tails can be illiquid but informative about crash risk.

Therefore, practitioners often apply **region-dependent weights**:

- reduce weight in extreme wings unless supported by strong quotes,
- reduce weight for maturities with sparse strikes,
- enforce maturity balancing so one tenor does not dominate.

---

## 4. Vega weighting and effective information content

In vol-space calibration, the same vol error can imply very different price errors depending on Vega:
\[
\Delta C \approx \text{Vega}\,\Delta\sigma.
\]

Possible schemes:

- **Vega-weighted vol errors:** emphasize points where vol changes matter for price.
- **Inverse-Vega weighting:** avoid ATM points dominating when Vega is huge.

There is no universal best choice; it depends on whether you want parameters optimized for **pricing** or **hedging**.

---

## 5. Data cleaning and weighting as a single pipeline

Weighting cannot fix all issues. A robust pipeline typically includes:

1. remove stale/outlier quotes (sanity checks),
2. enforce basic no-arbitrage constraints (where possible),
3. choose weights reflecting remaining uncertainty,
4. validate stability (re-calibration under perturbations).

Think of weights as *the last step* after basic data hygiene.

---

## 6. Practical recipes

### 6.1 A simple “spread + maturity balancing” scheme

- baseline: \(w_j = 1/\text{spread}_j^2\),
- per-maturity normalization so each maturity contributes similarly:
  \[
  w_{j \in T} \leftarrow \frac{w_j}{\sum_{k\in T} w_k}.
  \]

### 6.2 Robust weighting

Combine with robust losses (Huber):
- treat large residuals as probable bad data points,
- avoid a single quote forcing a poor global fit.

---

## 7. Key takeaways

- Weights encode market liquidity and quote reliability.
- Bid/ask spreads provide a natural noise proxy, but require caps/floors.
- Weighting interacts with the choice of calibration target (prices vs vols).
- Stability validation (perturbation/bootstraps) is essential.

---

## Further reading

- Gatheral, *The Volatility Surface* (practical surface and calibration).
- Fengler, *Semiparametric Modeling of Implied Volatility*.
- Cont & Tankov (data issues and calibration in jump models).
