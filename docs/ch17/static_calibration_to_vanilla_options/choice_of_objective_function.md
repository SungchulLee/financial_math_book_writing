# Choice of Objective Function


Calibration is typically formulated as an optimization problem:

\[
\hat\theta \in \arg\min_{\theta\in\Theta} \; \mathcal{L}(\theta),
\]


where the loss \(\mathcal{L}\) measures misfit between model outputs and market data. The objective function is not a mere implementation detail: it determines **statistical meaning**, **numerical stability**, and **hedging relevance**.

---

## Targets: prices vs implied vols


Two standard choices are:

### 1. Price-space objective



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

### 2. Implied-vol objective



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

## Statistical interpretation


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

## Robust objectives (outliers and stale quotes)


Real data contain outliers. Robust alternatives include:

### 1. \(\ell_1\) loss


\[
\mathcal{L}(\theta)=\sum_{j} w_j\,|r_j(\theta)|,
\qquad r_j = f_j(\theta)-y_j.
\]



### 2. Huber loss

Quadratic near zero, linear in the tails. It often improves stability without sacrificing too much smoothness for optimizers.

Robust losses can be especially useful when:
- some quotes are stale,
- microstructure noise is dominant,
- surface construction introduces artifacts.

---

## Vega-weighted and “relative” errors


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

## Multi-objective calibration


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

## Key takeaways


- The objective function defines *what it means* to “fit the market”.
- Price-space and vol-space objectives can yield materially different parameters.
- Robust and scaled objectives reduce sensitivity to outliers and heteroscedastic noise.
- A good objective aligns with both **quote uncertainty** and **hedging priorities**.

---

## Further reading


- Inverse problems and regularization: Engl, Hanke & Neubauer.
- Practical calibration choices: Gatheral; Cont & Tankov; Andersen & Piterbarg.

---

## Exercises

**Exercise 1.** Write down the price-space and implied-vol-space objective functions for calibrating a model to $m$ vanilla options. Show that if the model is exactly correct, both objectives are minimized at the same $\theta$. Give an example of how the two can yield different $\hat{\theta}$ when the model is misspecified.

---

**Exercise 2.** Using the approximation $\Delta C \approx \text{Vega} \cdot \Delta\sigma$, show that minimizing the price-space objective $\sum w_j (C_j^{\text{model}} - C_j^{\text{mkt}})^2$ is approximately equivalent to minimizing $\sum w_j \cdot \text{Vega}_j^2 \cdot (\sigma_j^{\text{model}} - \sigma_j^{\text{mkt}})^2$. What does this imply about which regions of the surface dominate the price-space calibration?

---

**Exercise 3.** The Huber loss is defined as $\ell_H(r) = \frac{1}{2}r^2$ for $|r| \le \delta$ and $\delta|r| - \frac{1}{2}\delta^2$ for $|r| > \delta$. Calibrate a hypothetical one-parameter model by hand: given residuals $r_1 = 0.02$, $r_2 = 0.01$, $r_3 = 0.5$ (an outlier) with $\delta = 0.1$, compute the Huber loss. Compare to the squared loss. Which residual's influence is most changed?

---

**Exercise 4.** A practitioner uses relative price errors $(C^{\text{model}} - C^{\text{mkt}})/C^{\text{mkt}}$ as the calibration residual. Discuss why this may be problematic for deep out-of-the-money options where $C^{\text{mkt}}$ is very small. Propose an alternative normalization that avoids division by near-zero quantities while still equalizing the scale across the surface.

---

**Exercise 5.** In multi-objective calibration with $\mathcal{L}(\theta) = \lambda_1\mathcal{L}_{\text{vanilla}}(\theta) + \lambda_2\mathcal{L}_{\text{exotic}}(\theta)$, discuss the Pareto frontier of the two objectives. Sketch the trade-off curve and explain how the choice of $\lambda_1/\lambda_2$ determines where on the frontier the calibration lands. When might a trader prefer to sacrifice vanilla fit to improve exotic fit?

---

**Exercise 6.** For maximum likelihood calibration, the weights should satisfy $w_j = 1/\sigma_j^2$ where $\sigma_j$ is the standard deviation of the observation noise. If option $j$ has bid-ask spread $s_j$ and we model $\sigma_j = s_j / (2\sqrt{3})$ (uniform distribution assumption), derive the implied weight $w_j$. What assumption about the noise distribution justifies the factor $2\sqrt{3}$?
