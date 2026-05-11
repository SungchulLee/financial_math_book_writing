# Weighting and Market Liquidity


Calibration is only as good as its treatment of **quote quality**. Two instruments can have the same mid price but very different reliability due to liquidity, bid/ask width, and microstructure effects. Weighting schemes translate market reality into the objective function.

---

## Why weights matter


Consider weighted least squares:

$$
\mathcal{L}(\theta)=\frac12\sum_{j=1}^m w_j\,r_j(\theta)^2,
\qquad r_j(\theta)=f_j(\theta)-y_j
$$



- Large $w_j$: the optimizer will prioritize fitting instrument $j$.
- Small $w_j$: instrument $j$ is effectively down-weighted (treated as noisy/unreliable).

Without sensible weights, calibration may overfit illiquid points and produce unstable parameters.

---

## Using bid/ask spreads as noise proxies


A common heuristic is:

$$
w_j \propto \frac{1}{\text{(bid-ask)}_j^2}
$$



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

$$
\Delta C \approx \text{Vega}\,\Delta\sigma
$$



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


- baseline: $w_j = 1/\text{spread}_j^2$,
- per-maturity normalization so each maturity contributes similarly:

  $$
  w_{j \in T} \leftarrow \frac{w_j}{\sum_{k\in T} w_k}
  $$



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

??? success "Solution to Exercise 1"
    The unnormalized bid-ask-based weights are $w_j = 1/s_j^2$:

    $$
    w_1 = \frac{1}{(0.10)^2} = 100, \quad w_2 = \frac{1}{(0.50)^2} = 4, \quad w_3 = \frac{1}{(0.25)^2} = 16
    $$

    The sum of weights is $\sum_k w_k = 100 + 4 + 16 = 120$.

    The normalized weights are $\tilde{w}_j = w_j / \sum_k w_k$:

    $$
    \tilde{w}_1 = \frac{100}{120} = \frac{5}{6} \approx 0.833, \quad \tilde{w}_2 = \frac{4}{120} = \frac{1}{30} \approx 0.033, \quad \tilde{w}_3 = \frac{16}{120} = \frac{2}{15} \approx 0.133
    $$

    The ratio of influence of option 1 to option 2 is

    $$
    \frac{w_1}{w_2} = \frac{100}{4} = 25
    $$

    Option 1 has **25 times** more influence than option 2 in the calibration. This is because option 1's spread is 5 times tighter than option 2's, and since weights scale as $1/s^2$, the ratio is $5^2 = 25$.

    This highlights both the power and the danger of bid-ask weighting: a single very tight quote can dominate the entire calibration. If option 1's tight spread reflects genuine liquidity and price precision, this is appropriate. If it reflects a stale quote or a temporary microstructure artifact, the calibration will be distorted. In practice, one should impose a cap on weights to prevent any single instrument from having disproportionate influence.

---

**Exercise 2.** A calibration uses 30 options across 3 maturities: 5 options at $T_1 = 0.1$, 15 options at $T_2 = 0.5$, and 10 options at $T_3 = 1.0$. Without maturity balancing, which maturity dominates the fit? Apply the per-maturity normalization $w_{j \in T} \leftarrow w_j / \sum_{k \in T} w_k$ and explain how this changes the effective contribution of each maturity.

??? success "Solution to Exercise 2"
    Without maturity balancing, using equal weights $w_j = 1$ for all options, the contribution of each maturity to the total loss is proportional to its number of options:

    - $T_1 = 0.1$: 5 options $\Rightarrow$ 5/30 = 16.7% of total loss
    - $T_2 = 0.5$: 15 options $\Rightarrow$ 15/30 = 50.0% of total loss
    - $T_3 = 1.0$: 10 options $\Rightarrow$ 10/30 = 33.3% of total loss

    The maturity $T_2 = 0.5$ dominates the fit simply because it has the most data points, not because it is the most important or informative. The optimizer will preferentially fit the smile at $T_2$ at the expense of $T_1$ and $T_3$.

    After applying **per-maturity normalization** $w_{j \in T} \leftarrow w_j / \sum_{k \in T} w_k$, each option at maturity $T$ receives weight $1/n_T$ where $n_T$ is the number of options at that maturity:

    - Options at $T_1$: weight = $1/5 = 0.20$ each, total = $1.0$
    - Options at $T_2$: weight = $1/15 \approx 0.067$ each, total = $1.0$
    - Options at $T_3$: weight = $1/10 = 0.10$ each, total = $1.0$

    Now each maturity contributes equally (total weight = 1.0 per maturity), regardless of how many strikes are quoted. The effective contribution is:

    - $T_1$: 1/3 = 33.3%
    - $T_2$: 1/3 = 33.3%
    - $T_3$: 1/3 = 33.3%

    This ensures the model is constrained to fit the smile at all three maturities equally. The trade-off is that the dense information at $T_2$ (15 well-sampled strikes giving a detailed smile shape) is down-weighted relative to the sparse information at $T_1$ (only 5 strikes). An intermediate approach is to weight maturities proportionally to $\sqrt{n_T}$ rather than equally, which partially balances density against equal representation.

---

**Exercise 3.** Vega weighting in vol-space means using weights $w_j \propto \text{Vega}_j^2 / s_j^2$. Compute the effective weight for an ATM option with $\text{Vega} = 0.40$ and spread $s = 0.10$, versus a deep OTM option with $\text{Vega} = 0.02$ and spread $s = 0.50$. Should the ATM option have more or less weight? Discuss the implications for tail-sensitive products.

??? success "Solution to Exercise 3"
    The Vega-weighted vol-space weight is $w_j \propto \text{Vega}_j^2 / s_j^2$.

    **ATM option:** $\text{Vega} = 0.40$, spread $s = 0.10$.

    $$
    w_{\text{ATM}} \propto \frac{(0.40)^2}{(0.10)^2} = \frac{0.16}{0.01} = 16
    $$

    **Deep OTM option:** $\text{Vega} = 0.02$, spread $s = 0.50$.

    $$
    w_{\text{OTM}} \propto \frac{(0.02)^2}{(0.50)^2} = \frac{0.0004}{0.25} = 0.0016
    $$

    The ratio is

    $$
    \frac{w_{\text{ATM}}}{w_{\text{OTM}}} = \frac{16}{0.0016} = 10{,}000
    $$

    The ATM option has **10,000 times** more weight than the deep OTM option under this scheme.

    **Should the ATM option have more weight?** From a price-fitting perspective, yes: the ATM option carries far more price-relevant information (high Vega means vol errors translate to large price errors) and is more precisely observed (tight spread). The Vega weighting ensures that the calibration prioritizes regions where implied vol errors have the greatest dollar impact.

    **Implications for tail-sensitive products:** This weighting scheme effectively ignores the wings of the smile, which is problematic for products whose value depends critically on tail behavior:

    - **Barrier options** and **digital options** are sensitive to the smile shape away from ATM.
    - **Variance swaps** depend on the entire smile, with significant contributions from OTM options (especially puts, via the log-contract replication).
    - **Credit-linked products** and **gap risk** instruments depend on extreme tail probabilities.

    For these products, a calibration that fits only the ATM region will systematically misprice tail risk. Practitioners dealing with tail-sensitive products should either (i) use pure bid-ask weighting without the Vega factor, (ii) use inverse-Vega weighting to boost the wings, or (iii) add explicit tail constraints (e.g., requiring the model to match specific OTM put prices exactly) as hard constraints in the optimization.

---

**Exercise 4.** A practitioner notices that after calibration, the model fits ATM options very well (residual $< 0.1$ vol points) but fits 25-delta puts poorly (residual $> 2$ vol points). Propose three possible causes: one related to weighting, one related to model limitations, and one related to data quality. For each, suggest a diagnostic test.

??? success "Solution to Exercise 4"
    The model fits ATM options well but fits 25-delta puts poorly. Three possible causes and their diagnostics:

    **1. Weighting issue.** If the weighting scheme assigns much higher weight to ATM options (e.g., Vega-squared weighting or simply more ATM quotes in the data set), the optimizer will sacrifice 25-delta fit to improve ATM fit.

    *Diagnostic:* Inspect the effective weights across the surface. Compute the contribution of each option to the total loss. If ATM options account for $>$80% of the weighted loss, the weighting is likely the culprit. Re-calibrate with equal weights or inverse-Vega weights and check whether the 25-delta residuals improve at the expense of ATM residuals. If so, the issue is weighting, not the model.

    **2. Model limitation.** The model may lack the flexibility to simultaneously fit the ATM level and the skew at 25-delta. For example, a Heston model with fixed parameters can reproduce a certain range of skews, but if the market skew is steeper than what the model can generate, no parameter choice will fit both regions. This is a fundamental model misspecification.

    *Diagnostic:* Fix the model parameters to minimize the 25-delta residual alone (ignoring ATM) and check the resulting ATM residual. If both cannot be made small simultaneously for any $\theta$, the Pareto frontier has a large gap, confirming model inadequacy. Also compare the market smile curvature to the model's maximum achievable curvature (e.g., for Heston, the skew is bounded by a function of vol-of-vol and correlation).

    **3. Data quality issue.** The 25-delta put quotes may be stale, erroneous, or reflect microstructure effects (e.g., end-of-day marks from an illiquid market). If the "true" market smile is actually consistent with the model but the reported 25-delta quotes are off, the large residual is a data problem, not a calibration problem.

    *Diagnostic:* Check the timestamps of the 25-delta put quotes versus ATM quotes. Compare the 25-delta implied vol to historical norms and to quotes from alternative data sources (different exchanges, brokers). Check whether the 25-delta put lies within the bid-ask spread of the model price. If the model price falls within the bid-ask, the mid-price residual is not economically significant.

---

**Exercise 5.** Design a "spread + maturity balancing + cap" weighting scheme. Start with $w_j = 1/s_j^2$, apply a cap $w_j \le w_{\max}$ and floor $w_j \ge w_{\min}$, then normalize per maturity. For $w_{\max}/w_{\min} = 100$, discuss how this ratio affects the calibration. What happens if the ratio is too large? Too small?

??? success "Solution to Exercise 5"
    **Step 1: Start with bid-ask weights.** $w_j = 1/s_j^2$ for each option $j$.

    **Step 2: Apply cap and floor.**

    $$
    w_j \leftarrow \min\!\big(\max(w_j,\; w_{\min}),\; w_{\max}\big)
    $$

    where $w_{\max} / w_{\min} = 100$. For example, if $w_{\min} = 1$ then $w_{\max} = 100$.

    **Step 3: Per-maturity normalization.** For each maturity $T$:

    $$
    w_{j \in T} \leftarrow \frac{w_j}{\sum_{k \in T} w_k}
    $$

    This ensures each maturity contributes equally to the total loss.

    **Effect of the cap/floor ratio $w_{\max}/w_{\min} = 100$:**

    The ratio controls the dynamic range of weights. An option with a very tight spread (e.g., $s = 0.01$, giving $w = 10{,}000$) would be capped at $w_{\max} = 100$, while an option with a very wide spread (e.g., $s = 10$, giving $w = 0.01$) would be floored at $w_{\min} = 1$. The tightest-spread option can have at most $100\times$ the weight of the widest-spread option.

    **If the ratio is too large** (e.g., $10{,}000$): The cap and floor are ineffective. A single option with an extremely tight spread can dominate the calibration (essentially no regularization). The scheme reduces to the raw $1/s^2$ weighting with all its instability problems. Calibrated parameters can change dramatically if one tight quote is perturbed.

    **If the ratio is too small** (e.g., $2$ or $1$): All options are effectively equally weighted regardless of their spread, discarding the valuable information that spread width provides about quote reliability. The calibration treats a precise ATM quote the same as a noisy deep OTM quote, which is statistically inefficient. In the limit $w_{\max}/w_{\min} = 1$, all weights are identical.

    A ratio of $100$ is a reasonable practical choice: it allows spreads to inform the weighting meaningfully (a 10:1 range in spreads translates to a 100:1 range in weights) while preventing extreme concentration. The per-maturity normalization then ensures that this heterogeneity within a maturity does not cause one maturity to dominate another.

---

**Exercise 6.** A perturbed-data stability test reveals that perturbing the price of a single deep OTM put by one tick changes a calibrated parameter by 30%. This option has a very tight spread and hence a very large weight. Propose a modification to the weighting scheme that would reduce this sensitivity without completely ignoring the option's information content.

??? success "Solution to Exercise 6"
    The problem is that the deep OTM put has a very tight bid-ask spread, producing a very large weight $w_j = 1/s_j^2$. This tight spread may reflect genuine market precision, but the resulting parameter sensitivity is undesirable. We want to reduce the influence of this single option without setting its weight to zero.

    **Proposed modification: combine spread-based weights with a leverage/influence cap.**

    1. **Weight capping.** As a first measure, impose $w_j \le w_{\max}$ where $w_{\max}$ is chosen so that no single option contributes more than, say, 5% of the total weighted loss. This directly addresses the immediate symptom. The deep OTM put's weight is clipped, reducing its ability to move parameters.

    2. **Blending with a uniform prior.** Replace $w_j = 1/s_j^2$ with a shrinkage estimator:

        $$
        w_j = \frac{\alpha}{s_j^2} + (1 - \alpha) \cdot \bar{w}
        $$

        where $\bar{w}$ is a baseline weight (e.g., the median of all $1/s_k^2$ values) and $\alpha \in (0,1)$ controls the degree of shrinkage. This pulls extreme weights toward the center, reducing the influence of any single option while still respecting the spread-based ranking.

    3. **Influence-function-based adjustment.** After an initial calibration, compute the influence of each data point: perturb each quote by a small amount and measure the change in calibrated parameters. If any single point has influence above a threshold (as detected for this OTM put), reduce its weight iteratively until the maximum influence is acceptable. This is related to iteratively reweighted least squares (IRLS) with a robust loss function.

    4. **Use a robust loss function.** Instead of modifying the weights, replace the squared loss with a Huber or bisquare loss. Under Huber loss with threshold $\delta$, any residual larger than $\delta$ contributes linearly rather than quadratically. If the deep OTM put produces a large residual (because the model cannot perfectly fit it), the robust loss naturally down-weights its influence. This approach is principled: it treats the symptom (excessive sensitivity) by addressing the statistical cause (outlier-like behavior in the optimization landscape).

    The recommended approach in practice is a combination of (1) and (4): cap the weights to prevent any single instrument from dominating, and use a robust loss function to further protect against residuals that indicate potential data problems. This preserves the option's information content (it still contributes to the calibration, just not disproportionately) while achieving parameter stability.
