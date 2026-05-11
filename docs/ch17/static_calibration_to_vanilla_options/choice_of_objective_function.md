# Choice of Objective Function


Calibration is typically formulated as an optimization problem:

$$
\hat\theta \in \arg\min_{\theta\in\Theta} \; \mathcal{L}(\theta)
$$


where the loss $\mathcal{L}$ measures misfit between model outputs and market data. The objective function is not a mere implementation detail: it determines **statistical meaning**, **numerical stability**, and **hedging relevance**.

---

## Targets: prices vs implied vols


Two standard choices are:

### 1. Price-space objective



$$
\mathcal{L}_{\text{price}}(\theta)
= \frac12\sum_{j=1}^m w_j\big(C^{\text{model}}_j(\theta)-C^{\text{mkt}}_j\big)^2
$$



Pros:

- aligns with replication cost (prices are what you trade),
- avoids implied-vol inversion.

Cons:

- prices differ wildly in magnitude across strikes/maturities (requires careful scaling),
- deep OTM prices can be tiny but still informative about tails.

### 2. Implied-vol objective



$$
\mathcal{L}_{\text{iv}}(\theta)
= \frac12\sum_{j=1}^m w_j\big(\sigma^{\text{model}}_{\text{impl},j}(\theta)-\sigma^{\text{mkt}}_{\text{impl},j}\big)^2
$$



Pros:

- more uniform scale across the surface,
- closer to market quoting conventions.

Cons:

- implied-vol mapping can be unstable (especially near expiry or deep OTM),
- implicitly re-weights errors through Vega.

---

## Statistical interpretation


If we model observations as

$$
y_j = f_j(\theta) + \varepsilon_j,
\qquad \varepsilon_j\sim \mathcal{N}(0,\sigma_j^2)
$$


then weighted least squares with $w_j=1/\sigma_j^2$ corresponds to maximum likelihood.

This suggests:

- weights should reflect **noise variance** of quotes,
- bid/ask spreads provide a proxy for $\sigma_j$.

---

## Robust objectives (outliers and stale quotes)


Real data contain outliers. Robust alternatives include:

### 1. ₁ loss


$$
\mathcal{L}(\theta)=\sum_{j} w_j\,|r_j(\theta)|,
\qquad r_j = f_j(\theta)-y_j
$$



### 2. Huber loss

Quadratic near zero, linear in the tails. It often improves stability without sacrificing too much smoothness for optimizers.

Robust losses can be especially useful when:

- some quotes are stale,
- microstructure noise is dominant,
- surface construction introduces artifacts.

---

## Vega-weighted and “relative” errors


Because implied vol errors correspond approximately to price errors scaled by Vega,

$$
\Delta C \approx \text{Vega}\cdot \Delta \sigma
$$


one may use objectives that incorporate **Vega weighting** to make the loss more “price meaningful” while remaining in vol-space.

Other scaling choices:

- relative price errors: $(C^{\text{model}}-C^{\text{mkt}})/C^{\text{mkt}}$,
- normalized errors by forward/discount factor,
- total variance errors in $w=T\sigma^2$.

Each choice changes which parts of the surface dominate the calibration.

---

## Multi-objective calibration


Sometimes you need to fit multiple data types:

- vanillas (smile surface),
- constraints from forwards/dividends/funding,
- exotics or forward-start options,
- time-series moments (historical calibration).

A common approach is a weighted sum:

$$
\mathcal{L}(\theta)=\lambda_1\mathcal{L}_1(\theta)+\lambda_2\mathcal{L}_2(\theta)+\cdots
$$


with hyperparameters $\lambda_i$ chosen by stability/validation.

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

??? success "Solution to Exercise 1"
    The **price-space objective** for calibrating a model with parameters $\theta$ to $m$ vanilla options is

    $$
    \mathcal{L}_{\text{price}}(\theta) = \frac{1}{2} \sum_{j=1}^{m} w_j \left( C_j^{\text{model}}(\theta) - C_j^{\text{mkt}} \right)^2
    $$

    The **implied-vol-space objective** is

    $$
    \mathcal{L}_{\text{iv}}(\theta) = \frac{1}{2} \sum_{j=1}^{m} w_j \left( \sigma_j^{\text{model}}(\theta) - \sigma_j^{\text{mkt}} \right)^2
    $$

    where $\sigma_j^{\text{model}}(\theta)$ is obtained by inverting the Black--Scholes formula at the model price $C_j^{\text{model}}(\theta)$.

    **When the model is exactly correct:** There exists $\theta^*$ such that $C_j^{\text{model}}(\theta^*) = C_j^{\text{mkt}}$ for all $j$. Then $\mathcal{L}_{\text{price}}(\theta^*) = 0$ and, since the implied vol map is injective (one-to-one), $\sigma_j^{\text{model}}(\theta^*) = \sigma_j^{\text{mkt}}$ for all $j$, so $\mathcal{L}_{\text{iv}}(\theta^*) = 0$. Both objectives attain their global minimum of zero at the same $\theta^*$.

    **Example of different $\hat{\theta}$ under misspecification:** Consider calibrating a one-parameter Black--Scholes model (constant volatility $\sigma$) to two options: an ATM call and a deep OTM put, where the true market exhibits skew.

    - In price space, the ATM call has a much larger price than the OTM put. Equal weights $w_j = 1$ cause the optimizer to prioritize fitting the larger ATM price, yielding $\hat{\sigma}_{\text{price}}$ close to the ATM implied vol.
    - In vol space, both options contribute on a comparable scale. The optimizer compromises between the two implied vols, yielding $\hat{\sigma}_{\text{iv}}$ that is a weighted average of the ATM and OTM implied vols.

    Since the model cannot reproduce the skew, the best-fit $\hat{\sigma}$ differs between the two formulations. The price-space calibration effectively gives more weight to high-Vega instruments (ATM), while the vol-space calibration treats all points more equally. This demonstrates that the choice of objective function is not merely a numerical convenience but has real economic consequences for the calibrated parameters.

---

**Exercise 2.** Using the approximation $\Delta C \approx \text{Vega} \cdot \Delta\sigma$, show that minimizing the price-space objective $\sum w_j (C_j^{\text{model}} - C_j^{\text{mkt}})^2$ is approximately equivalent to minimizing $\sum w_j \cdot \text{Vega}_j^2 \cdot (\sigma_j^{\text{model}} - \sigma_j^{\text{mkt}})^2$. What does this imply about which regions of the surface dominate the price-space calibration?

??? success "Solution to Exercise 2"
    Starting from the approximation $\Delta C_j \approx \text{Vega}_j \cdot \Delta\sigma_j$, we can write

    $$
    C_j^{\text{model}} - C_j^{\text{mkt}} \approx \text{Vega}_j \cdot \left( \sigma_j^{\text{model}} - \sigma_j^{\text{mkt}} \right)
    $$

    Substituting into the price-space objective:

    $$
    \mathcal{L}_{\text{price}}(\theta) = \sum_{j} w_j \left( C_j^{\text{model}} - C_j^{\text{mkt}} \right)^2 \approx \sum_{j} w_j \cdot \text{Vega}_j^2 \cdot \left( \sigma_j^{\text{model}} - \sigma_j^{\text{mkt}} \right)^2
    $$

    This shows that the price-space objective is approximately equivalent to an implied-vol objective with **effective weights** $\tilde{w}_j = w_j \cdot \text{Vega}_j^2$.

    **Implications for which regions dominate:** Black--Scholes Vega is given by $\text{Vega} = S_0 e^{-qT}\sqrt{T}\,\phi(d_1)$, where $\phi$ is the standard normal density. Vega is largest for ATM options (where $d_1 \approx 0$ and $\phi(d_1)$ is maximized) and decays rapidly for deep OTM and deep ITM options. Furthermore, Vega increases with $\sqrt{T}$, so longer-dated options have larger Vega.

    Therefore, the effective weights $\tilde{w}_j \propto \text{Vega}_j^2$ strongly favor:

    - **ATM options** over OTM/ITM options (since Vega peaks at ATM),
    - **Longer-dated options** over shorter-dated options (since Vega grows with $\sqrt{T}$).

    The consequence is that price-space calibration disproportionately fits the ATM region and longer maturities, while effectively ignoring deep OTM options. This can be problematic for pricing tail-sensitive products (barrier options, variance swaps) that depend critically on the wings of the smile. A trader concerned with tail risk should either calibrate in vol space or use explicit inverse-Vega weighting to counteract this bias.

---

**Exercise 3.** The Huber loss is defined as $\ell_H(r) = \frac{1}{2}r^2$ for $|r| \le \delta$ and $\delta|r| - \frac{1}{2}\delta^2$ for $|r| > \delta$. Calibrate a hypothetical one-parameter model by hand: given residuals $r_1 = 0.02$, $r_2 = 0.01$, $r_3 = 0.5$ (an outlier) with $\delta = 0.1$, compute the Huber loss. Compare to the squared loss. Which residual's influence is most changed?

??? success "Solution to Exercise 3"
    The Huber loss is

    $$
    \ell_H(r) = \begin{cases} \frac{1}{2}r^2 & \text{if } |r| \le \delta \\ \delta|r| - \frac{1}{2}\delta^2 & \text{if } |r| > \delta \end{cases}
    $$

    With $\delta = 0.1$ and residuals $r_1 = 0.02$, $r_2 = 0.01$, $r_3 = 0.5$:

    **For $r_1 = 0.02$:** Since $|r_1| = 0.02 \le 0.1$, we are in the quadratic regime:

    $$
    \ell_H(r_1) = \frac{1}{2}(0.02)^2 = 0.0002
    $$

    **For $r_2 = 0.01$:** Since $|r_2| = 0.01 \le 0.1$, quadratic regime:

    $$
    \ell_H(r_2) = \frac{1}{2}(0.01)^2 = 0.00005
    $$

    **For $r_3 = 0.5$:** Since $|r_3| = 0.5 > 0.1$, linear regime:

    $$
    \ell_H(r_3) = 0.1 \cdot 0.5 - \frac{1}{2}(0.1)^2 = 0.05 - 0.005 = 0.045
    $$

    **Total Huber loss:** $\mathcal{L}_H = 0.0002 + 0.00005 + 0.045 = 0.04525$.

    **Comparison to squared loss:**

    $$
    \ell_{\text{sq}}(r_1) = \frac{1}{2}(0.02)^2 = 0.0002, \quad \ell_{\text{sq}}(r_2) = \frac{1}{2}(0.01)^2 = 0.00005, \quad \ell_{\text{sq}}(r_3) = \frac{1}{2}(0.5)^2 = 0.125
    $$

    Total squared loss: $\mathcal{L}_{\text{sq}} = 0.0002 + 0.00005 + 0.125 = 0.12525$.

    **Which residual's influence is most changed?** The outlier $r_3 = 0.5$ dominates. Under squared loss, it contributes $0.125$ out of $0.12525$ (99.8% of total loss). Under Huber loss, it contributes $0.045$ out of $0.04525$ (99.4% of total loss, but at a much reduced absolute level). The Huber loss reduces the contribution of $r_3$ from $0.125$ to $0.045$---a factor of roughly $2.8\times$ reduction---while leaving the contributions of $r_1$ and $r_2$ completely unchanged (since they fall within the quadratic region). This dramatically reduces the outlier's ability to distort the calibrated parameter.

---

**Exercise 4.** A practitioner uses relative price errors $(C^{\text{model}} - C^{\text{mkt}})/C^{\text{mkt}}$ as the calibration residual. Discuss why this may be problematic for deep out-of-the-money options where $C^{\text{mkt}}$ is very small. Propose an alternative normalization that avoids division by near-zero quantities while still equalizing the scale across the surface.

??? success "Solution to Exercise 4"
    Using relative price errors $r_j = (C_j^{\text{model}} - C_j^{\text{mkt}}) / C_j^{\text{mkt}}$ is problematic for deep OTM options because:

    1. **Division by near-zero.** A deep OTM option might have a market price of $C^{\text{mkt}} = 0.01$ or even $0.001$. A model error of $0.005$ (half a cent) then produces a relative error of 50% or 500%, completely dominating the calibration. This is numerically unstable and statistically meaningless---the absolute error is well within bid-ask noise, yet the relative metric treats it as catastrophic.

    2. **Noise amplification.** Small absolute errors in illiquid deep OTM options (which are noisy to begin with) get amplified into large relative errors, forcing the optimizer to overfit the tails at the expense of the liquid, informative part of the surface.

    3. **Singularity risk.** If any market price is zero (which can happen for very deep OTM options or after rounding), the relative error is undefined.

    **Alternative normalizations:**

    - **Vega normalization:** Use $r_j = (C_j^{\text{model}} - C_j^{\text{mkt}}) / \text{Vega}_j$. This is approximately equivalent to calibrating in implied volatility space (since $\Delta C \approx \text{Vega} \cdot \Delta\sigma$) and avoids division by near-zero because Vega, while small for deep OTM options, is bounded away from zero more gracefully than the price itself. However, Vega can also be very small for deep OTM options, so a floor may still be needed.

    - **Forward-price normalization:** Use $r_j = (C_j^{\text{model}} - C_j^{\text{mkt}}) / F_T$ where $F_T = S_0 e^{(r-q)T}$ is the forward price. The forward is always of order $S_0$ and provides a stable denominator regardless of moneyness. This puts all errors on a "percentage of forward" basis.

    - **Black--Scholes price at a reference vol:** Use $r_j = (C_j^{\text{model}} - C_j^{\text{mkt}}) / C_j^{\text{BS}}(\bar{\sigma})$ where $\bar{\sigma}$ is a fixed reference volatility (e.g., the ATM implied vol). This normalizes by a smooth function that never reaches zero for finite $K$ and $T$, while still providing scale equalization across the surface.

    - **Additive floor:** Use $r_j = (C_j^{\text{model}} - C_j^{\text{mkt}}) / \max(C_j^{\text{mkt}}, \varepsilon)$ for a small floor $\varepsilon > 0$. This is the simplest fix but introduces an arbitrary parameter $\varepsilon$.

    Among these, Vega normalization (i.e., calibrating in implied vol space) is the most widely adopted in practice because it directly aligns with market quoting conventions and provides uniform scaling.

---

**Exercise 5.** In multi-objective calibration with $\mathcal{L}(\theta) = \lambda_1\mathcal{L}_{\text{vanilla}}(\theta) + \lambda_2\mathcal{L}_{\text{exotic}}(\theta)$, discuss the Pareto frontier of the two objectives. Sketch the trade-off curve and explain how the choice of $\lambda_1/\lambda_2$ determines where on the frontier the calibration lands. When might a trader prefer to sacrifice vanilla fit to improve exotic fit?

??? success "Solution to Exercise 5"
    In multi-objective calibration, we minimize

    $$
    \mathcal{L}(\theta) = \lambda_1 \mathcal{L}_{\text{vanilla}}(\theta) + \lambda_2 \mathcal{L}_{\text{exotic}}(\theta)
    $$

    The **Pareto frontier** is the set of parameter values $\theta$ such that no other $\theta'$ can improve one objective without worsening the other. Formally, $\theta^*$ is Pareto optimal if there is no $\theta$ with $\mathcal{L}_{\text{vanilla}}(\theta) \le \mathcal{L}_{\text{vanilla}}(\theta^*)$ and $\mathcal{L}_{\text{exotic}}(\theta) \le \mathcal{L}_{\text{exotic}}(\theta^*)$ with at least one strict inequality.

    The Pareto frontier in the $(\mathcal{L}_{\text{vanilla}}, \mathcal{L}_{\text{exotic}})$ plane is a decreasing, convex curve. Points below and to the left of the frontier are infeasible; points above and to the right are suboptimal.

    Each choice of $\lambda_1 / \lambda_2$ corresponds to a different point on the Pareto frontier. The weighted-sum minimization selects the point where the frontier is tangent to a line of slope $-\lambda_1/\lambda_2$:

    - **Large $\lambda_1/\lambda_2$:** The calibration strongly prioritizes vanilla fit, landing near the left end of the frontier (low $\mathcal{L}_{\text{vanilla}}$, high $\mathcal{L}_{\text{exotic}}$).
    - **Small $\lambda_1/\lambda_2$:** The calibration prioritizes exotic fit, landing near the bottom of the frontier (high $\mathcal{L}_{\text{vanilla}}$, low $\mathcal{L}_{\text{exotic}}$).
    - **Intermediate ratios:** The calibration compromises between the two objectives.

    **When a trader might sacrifice vanilla fit for exotic fit:**

    1. **Hedging exotic books.** If the primary purpose of the model is to price and hedge a portfolio of exotic options, the trader may accept slightly wider vanilla residuals in exchange for a model that more accurately captures features relevant to exotics (e.g., forward smile dynamics, barrier behavior).
    2. **Consistent exotic pricing.** If the model must reprice existing exotic trades consistently (e.g., for P&L attribution or risk reporting), fitting the exotics that are actually in the book may be more important than perfectly matching liquid vanillas that are used only as hedging instruments.
    3. **Model limitations.** If the model class cannot simultaneously fit both vanillas and exotics well (a common situation), the trader may deliberately bias toward exotic fit when the exotic positions represent larger risk.

    The trade-off is that sacrificing vanilla fit can impair hedge effectiveness: if the model misprices vanillas used as hedging instruments, the hedges will be systematically biased. The optimal $\lambda_1/\lambda_2$ is therefore a business decision that depends on the composition of the trading book.

---

**Exercise 6.** For maximum likelihood calibration, the weights should satisfy $w_j = 1/\sigma_j^2$ where $\sigma_j$ is the standard deviation of the observation noise. If option $j$ has bid-ask spread $s_j$ and we model $\sigma_j = s_j / (2\sqrt{3})$ (uniform distribution assumption), derive the implied weight $w_j$. What assumption about the noise distribution justifies the factor $2\sqrt{3}$?

??? success "Solution to Exercise 6"
    The assumption is that the true (unobservable) mid-market price lies uniformly within the bid-ask interval $[\text{bid}, \text{ask}]$. The bid-ask spread is $s_j = \text{ask}_j - \text{bid}_j$, so the observation noise $\varepsilon_j$ (the difference between the observed mid and the true value) is modeled as

    $$
    \varepsilon_j \sim \text{Uniform}\!\left(-\frac{s_j}{2}, \frac{s_j}{2}\right)
    $$

    The standard deviation of a uniform distribution on $[a, b]$ is $(b - a) / \sqrt{12}$. Here $b - a = s_j$, so

    $$
    \sigma_j = \frac{s_j}{\sqrt{12}} = \frac{s_j}{2\sqrt{3}}
    $$

    This is where the factor $2\sqrt{3}$ originates: $\sqrt{12} = 2\sqrt{3} \approx 3.464$.

    The maximum-likelihood weight is $w_j = 1/\sigma_j^2$, so

    $$
    w_j = \frac{1}{\sigma_j^2} = \frac{(2\sqrt{3})^2}{s_j^2} = \frac{12}{s_j^2}
    $$

    Since the constant factor $12$ is the same for all $j$, it can be absorbed into the overall scale of the objective function. The relative weights are therefore

    $$
    w_j \propto \frac{1}{s_j^2}
    $$

    which recovers the standard bid-ask-based weighting scheme.

    **Justification of the noise model:** The factor $2\sqrt{3}$ arises specifically from the assumption that the true price is uniformly distributed over the bid-ask interval. This is a conservative, maximum-entropy assumption: among all distributions supported on a bounded interval with known endpoints, the uniform distribution has the largest variance (hence the largest entropy). If one instead assumed a triangular or truncated normal distribution concentrated near the mid-price, the standard deviation would be smaller and the implied weights would be larger. The uniform assumption is therefore a conservative choice that avoids overweighting any single instrument.

    Note that the actual noise distribution is likely not uniform---in liquid markets, the true price is more concentrated near the mid, while in illiquid markets, the distribution may be even wider than the quoted spread suggests. The uniform model is best viewed as a convenient, interpretable approximation rather than a precise description of market microstructure.
