# Weighting and Market Liquidity


Calibration is only as good as its treatment of **quote quality**. Two instruments can have the same mid price but very different reliability due to liquidity, bid/ask width, and microstructure effects. Weighting schemes translate market reality into the objective function.

---

## Why weights matter


Consider weighted least squares:

\[
\mathcal{L}(\theta)=\frac12\sum_{j=1}^m w_j\,r_j(\theta)^2,
\qquad r_j(\theta)=f_j(\theta)-y_j.
\]



- Large \(w_j\): the optimizer will prioritize fitting instrument \(j\).
- Small \(w_j\): instrument \(j\) is effectively down-weighted (treated as noisy/unreliable).

Without sensible weights, calibration may overfit illiquid points and produce unstable parameters.

---

## Using bid/ask spreads as noise proxies


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

## Liquidity and surface regions


Liquidity is not uniform across the surface:

- near-the-money options are usually most liquid,
- very short maturities can be noisy (discrete dividends, microstructure),
- far OTM tails can be illiquid but informative about crash risk.

Therefore, practitioners often apply **region-dependent weights**:

- reduce weight in extreme wings unless supported by strong quotes,
- reduce weight for maturities with sparse strikes,
- enforce maturity balancing so one tenor does not dominate.

---

## Vega weighting and effective information content


In vol-space calibration, the same vol error can imply very different price errors depending on Vega:

\[
\Delta C \approx \text{Vega}\,\Delta\sigma.
\]



Possible schemes:

- **Vega-weighted vol errors:** emphasize points where vol changes matter for price.
- **Inverse-Vega weighting:** avoid ATM points dominating when Vega is huge.

There is no universal best choice; it depends on whether you want parameters optimized for **pricing** or **hedging**.

---

## Data cleaning and weighting as a single pipeline


Weighting cannot fix all issues. A robust pipeline typically includes:

1. remove stale/outlier quotes (sanity checks),
2. enforce basic no-arbitrage constraints (where possible),
3. choose weights reflecting remaining uncertainty,
4. validate stability (re-calibration under perturbations).

Think of weights as *the last step* after basic data hygiene.

---

## Practical recipes


### 1. A simple “spread + maturity balancing” scheme


- baseline: \(w_j = 1/\text{spread}_j^2\),
- per-maturity normalization so each maturity contributes similarly:

  \[
  w_{j \in T} \leftarrow \frac{w_j}{\sum_{k\in T} w_k}.
  \]



### 2. Robust weighting


Combine with robust losses (Huber):
- treat large residuals as probable bad data points,
- avoid a single quote forcing a poor global fit.

---

## Key takeaways


- Weights encode market liquidity and quote reliability.
- Bid/ask spreads provide a natural noise proxy, but require caps/floors.
- Weighting interacts with the choice of calibration target (prices vs vols).
- Stability validation (perturbation/bootstraps) is essential.

---

## Further reading


- Gatheral, *The Volatility Surface* (practical surface and calibration).
- Fengler, *Semiparametric Modeling of Implied Volatility*.
- Cont & Tankov (data issues and calibration in jump models).

---

## Exercises

**Exercise 1.** Given three option quotes with bid-ask spreads $s_1 = 0.10$, $s_2 = 0.50$, $s_3 = 0.25$, compute the bid-ask-based weights $w_j = 1/s_j^2$ (unnormalized) and the normalized weights $\tilde{w}_j = w_j / \sum_k w_k$. How much more influence does option 1 have compared to option 2?

---

**Exercise 2.** A calibration uses 30 options across 3 maturities: 5 options at $T_1 = 0.1$, 15 options at $T_2 = 0.5$, and 10 options at $T_3 = 1.0$. Without maturity balancing, which maturity dominates the fit? Apply the per-maturity normalization $w_{j \in T} \leftarrow w_j / \sum_{k \in T} w_k$ and explain how this changes the effective contribution of each maturity.

---

**Exercise 3.** Vega weighting in vol-space means using weights $w_j \propto \text{Vega}_j^2 / s_j^2$. Compute the effective weight for an ATM option with $\text{Vega} = 0.40$ and spread $s = 0.10$, versus a deep OTM option with $\text{Vega} = 0.02$ and spread $s = 0.50$. Should the ATM option have more or less weight? Discuss the implications for tail-sensitive products.

---

**Exercise 4.** A practitioner notices that after calibration, the model fits ATM options very well (residual $< 0.1$ vol points) but fits 25-delta puts poorly (residual $> 2$ vol points). Propose three possible causes: one related to weighting, one related to model limitations, and one related to data quality. For each, suggest a diagnostic test.

---

**Exercise 5.** Design a "spread + maturity balancing + cap" weighting scheme. Start with $w_j = 1/s_j^2$, apply a cap $w_j \le w_{\max}$ and floor $w_j \ge w_{\min}$, then normalize per maturity. For $w_{\max}/w_{\min} = 100$, discuss how this ratio affects the calibration. What happens if the ratio is too large? Too small?

---

**Exercise 6.** A perturbed-data stability test reveals that perturbing the price of a single deep OTM put by one tick changes a calibrated parameter by 30%. This option has a very tight spread and hence a very large weight. Propose a modification to the weighting scheme that would reduce this sensitivity without completely ignoring the option's information content.
