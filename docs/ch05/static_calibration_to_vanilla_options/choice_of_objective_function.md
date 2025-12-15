# Choice of Objective Function

Calibration is typically formulated as an optimization problem:
\[
\hat\theta \in \arg\min_{\theta\in\Theta} \; \mathcal{L}(\theta),
\]
where the loss \(\mathcal{L}\) measures misfit between model outputs and market data. The objective function is not a mere implementation detail: it determines **statistical meaning**, **numerical stability**, and **hedging relevance**.

---

## 1. Targets: prices vs implied vols

Two standard choices are:

### 1.1 Price-space objective

\[
\mathcal{L}_{\text{price}}(\theta)
= \frac12\sum_{j=1}^m w_j\big(C^{\text{model}}_j(\theta)-C^{\text{mkt}}_j\big)^2.
\]

Pros:
- aligns with replication cost (prices are what you trade),
- avoids implied-vol inversion.

Cons:
- prices differ wildly in magnitude across strikes/maturities (requires careful scaling),
- deep OTM prices can be tiny but still informative about tails.

### 1.2 Implied-vol objective

\[
\mathcal{L}_{\text{iv}}(\theta)
= \frac12\sum_{j=1}^m w_j\big(\sigma^{\text{model}}_{\text{impl},j}(\theta)-\sigma^{\text{mkt}}_{\text{impl},j}\big)^2.
\]

Pros:
- more uniform scale across the surface,
- closer to market quoting conventions.

Cons:
- implied-vol mapping can be unstable (especially near expiry or deep OTM),
- implicitly re-weights errors through Vega.

---

## 2. Statistical interpretation

If we model observations as
\[
y_j = f_j(\theta) + \varepsilon_j,
\qquad \varepsilon_j\sim \mathcal{N}(0,\sigma_j^2),
\]
then weighted least squares with \(w_j=1/\sigma_j^2\) corresponds to maximum likelihood.

This suggests:
- weights should reflect **noise variance** of quotes,
- bid/ask spreads provide a proxy for \(\sigma_j\).

---

## 3. Robust objectives (outliers and stale quotes)

Real data contain outliers. Robust alternatives include:

### 3.1 \(\ell_1\) loss
\[
\mathcal{L}(\theta)=\sum_{j} w_j\,|r_j(\theta)|,
\qquad r_j = f_j(\theta)-y_j.
\]

### 3.2 Huber loss
Quadratic near zero, linear in the tails. It often improves stability without sacrificing too much smoothness for optimizers.

Robust losses can be especially useful when:
- some quotes are stale,
- microstructure noise is dominant,
- surface construction introduces artifacts.

---

## 4. Vega-weighted and “relative” errors

Because implied vol errors correspond approximately to price errors scaled by Vega,
\[
\Delta C \approx \text{Vega}\cdot \Delta \sigma,
\]
one may use objectives that incorporate **Vega weighting** to make the loss more “price meaningful” while remaining in vol-space.

Other scaling choices:
- relative price errors: \((C^{\text{model}}-C^{\text{mkt}})/C^{\text{mkt}}\),
- normalized errors by forward/discount factor,
- total variance errors in \(w=T\sigma^2\).

Each choice changes which parts of the surface dominate the calibration.

---

## 5. Multi-objective calibration

Sometimes you need to fit multiple data types:

- vanillas (smile surface),
- constraints from forwards/dividends/funding,
- exotics or forward-start options,
- time-series moments (historical calibration).

A common approach is a weighted sum:
\[
\mathcal{L}(\theta)=\lambda_1\mathcal{L}_1(\theta)+\lambda_2\mathcal{L}_2(\theta)+\cdots
\]
with hyperparameters \(\lambda_i\) chosen by stability/validation.

---

## 6. Key takeaways

- The objective function defines *what it means* to “fit the market”.
- Price-space and vol-space objectives can yield materially different parameters.
- Robust and scaled objectives reduce sensitivity to outliers and heteroscedastic noise.
- A good objective aligns with both **quote uncertainty** and **hedging priorities**.

---

## Further reading

- Inverse problems and regularization: Engl, Hanke & Neubauer.
- Practical calibration choices: Gatheral; Cont & Tankov; Andersen & Piterbarg.
