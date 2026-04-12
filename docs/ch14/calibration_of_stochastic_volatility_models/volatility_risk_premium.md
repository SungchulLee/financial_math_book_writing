# Volatility Risk Premium


Stochastic volatility models distinguish between **risk-neutral** and **physical** volatility dynamics. The gap between them is captured by the **volatility risk premium (VRP)**, which has direct implications for calibration and interpretation.

---

## Risk-neutral calibration


Option prices identify parameters under the risk-neutral measure $\mathbb{Q}$.
These parameters reflect:
- investor risk preferences,
- compensation for unhedgeable volatility risk.

They should not be confused with historical estimates.

---

## Physical dynamics


Historical time-series analysis estimates parameters under the physical measure $\mathbb{P}$.
Empirically:
- realized volatility is lower than option-implied variance,
- volatility shocks earn negative premia.

---

## Implications for calibration


Mixing $\mathbb{P}$ and $\mathbb{Q}$ parameters without modeling VRP leads to:

- inconsistent dynamics,
- misleading economic interpretation,
- degraded calibration stability.

Calibration should be measure-consistent.

---

## Joint modeling approaches


Advanced frameworks introduce:
- explicit VRP processes,
- joint estimation using options and realized variance,
- Bayesian separation of measures.

These improve interpretability but increase complexity.

---

## Key takeaways


- Volatility risk premium explains discrepancies between historical and implied volatility.
- Option calibration recovers risk-neutral dynamics only.
- Measure consistency is essential.

---

## Further reading


- Bollerslev et al., variance risk premium.
- Carr & Wu, volatility premia.

---

## Exercises

**Exercise 1.** A Heston model calibrated to 3-month S&P 500 options gives $\theta^{\mathbb{Q}} = 0.052$ and $\kappa^{\mathbb{Q}} = 3.5$. Time-series estimation from daily returns gives $\theta^{\mathbb{P}} = 0.038$ and $\kappa^{\mathbb{P}} = 1.8$. Compute the ratio $\theta^{\mathbb{Q}}/\theta^{\mathbb{P}}$ and $\kappa^{\mathbb{Q}}/\kappa^{\mathbb{P}}$. Interpret the difference in each parameter in terms of the volatility risk premium.

??? success "Solution to Exercise 1"
    Computing the ratios:

    $$
    \frac{\theta^{\mathbb{Q}}}{\theta^{\mathbb{P}}} = \frac{0.052}{0.038} \approx 1.368
    $$

    $$
    \frac{\kappa^{\mathbb{Q}}}{\kappa^{\mathbb{P}}} = \frac{3.5}{1.8} \approx 1.944
    $$

    **Interpretation of $\theta^{\mathbb{Q}} > \theta^{\mathbb{P}}$:** The risk-neutral long-run variance ($0.052$) exceeds the physical long-run variance ($0.038$) by about 37%. This means that option markets price in a higher long-run volatility level than what is historically realized. The excess reflects the **variance risk premium**: investors demand compensation for bearing variance risk, inflating the risk-neutral expectation of future variance. Economically, sellers of variance (e.g., writers of straddles or variance swaps) earn a premium because variance tends to spike during market downturns when marginal utility is high.

    **Interpretation of $\kappa^{\mathbb{Q}} > \kappa^{\mathbb{P}}$:** The risk-neutral mean reversion speed ($3.5$) is nearly twice the physical mean reversion speed ($1.8$). Under $\mathbb{Q}$, volatility mean-reverts faster, meaning option markets imply that volatility shocks are more transient than they actually are under $\mathbb{P}$. This is consistent with a negative market price of volatility risk $\lambda < 0$: since $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda\xi$ with $\lambda > 0$ in the convention used here (or equivalently, the risk adjustment increases $\kappa$), the faster mean reversion under $\mathbb{Q}$ reflects the fact that risk-averse investors discount future volatility states asymmetrically.

---

**Exercise 2.** The VIX index (squared, divided by 100) approximates the 30-day risk-neutral expected variance $\mathbb{E}^{\mathbb{Q}}[\sigma^2]$. Suppose VIX $= 22$ (so $\mathbb{E}^{\mathbb{Q}}[\sigma^2] \approx (22\%)^2 = 0.0484$) and subsequent realized variance over 30 days is $(17\%)^2 = 0.0289$. Compute the VRP for this period. If a trader systematically sells 30-day variance swaps at the VIX level, what is the expected annualized return in volatility points?

??? success "Solution to Exercise 2"
    **Computing the VRP:**

    $$
    \text{VRP} = \mathbb{E}^{\mathbb{Q}}[\sigma^2] - \text{RV}^2 = 0.0484 - 0.0289 = 0.0195
    $$

    In volatility terms, this corresponds to going from $22\%$ implied to $17\%$ realized, a gap of $5$ vol points.

    **Annualized return from selling variance swaps:** A trader who systematically sells 30-day variance swaps at the VIX level receives the swap rate (approximately $\text{VIX}^2/100$) and pays realized variance. The expected profit per period is $0.0195$ in variance terms. Since a variance swap pays in variance units, the expected annualized return in variance terms is

    $$
    \text{VRP}_{\text{annual}} = 0.0195 \times 12 \approx 0.234
    $$

    for monthly rolls (approximately 12 non-overlapping 30-day periods per year).

    Converting to volatility points: the square root of the annualized variance profit is not directly meaningful because variance swap payoffs are linear in variance, not volatility. However, the per-period volatility gap is $22\% - 17\% = 5$ vol points, so the strategy earns approximately $5$ vol points per month, or roughly $5 \times \sqrt{12} \approx 17.3$ annualized vol points on a volatility scale.

    In practice, this overstates the risk-adjusted return because the strategy has significant left-tail risk: realized variance occasionally spikes well above VIX (e.g., during the 2008 crisis or March 2020), leading to large losses that offset many months of profits.

---

**Exercise 3.** A practitioner calibrates a Heston model to options data and uses the risk-neutral parameters $(\kappa^{\mathbb{Q}}, \theta^{\mathbb{Q}})$ for a VaR calculation. Explain why this is incorrect. Specifically, if $\kappa^{\mathbb{Q}} > \kappa^{\mathbb{P}}$, how would the VaR estimate be affected? Would the risk-neutral VaR overestimate or underestimate the true risk?

??? success "Solution to Exercise 3"
    Using risk-neutral parameters $(\kappa^{\mathbb{Q}}, \theta^{\mathbb{Q}})$ for VaR is incorrect because VaR measures the tail of the **physical** ($\mathbb{P}$) distribution of portfolio returns, not the risk-neutral distribution. The risk-neutral measure is designed for pricing derivatives, not for forecasting real-world returns or risks.

    **Effect of $\kappa^{\mathbb{Q}} > \kappa^{\mathbb{P}}$:** The risk-neutral mean-reversion speed is faster, which means that under $\mathbb{Q}$, volatility shocks die out more quickly. If a VaR model uses $\kappa^{\mathbb{Q}}$ instead of $\kappa^{\mathbb{P}}$, it assumes volatility reverts to its mean faster than it actually does under $\mathbb{P}$. Consequently:

    - The model predicts **narrower** confidence intervals for future variance paths
    - Volatility clustering is **underestimated** — the model thinks high-vol regimes are shorter-lived than they really are
    - The tails of the simulated P&L distribution are **thinner** than reality

    Therefore, the risk-neutral VaR **underestimates** the true risk. The VaR number will be too small, giving a false sense of security. This is particularly dangerous during periods of elevated volatility, where the slower physical mean reversion ($\kappa^{\mathbb{P}} = 1.8$) means volatility persists longer than the risk-neutral model ($\kappa^{\mathbb{Q}} = 3.5$) predicts, leading to larger drawdowns than the VaR forecast anticipates.

---

**Exercise 4.** Describe a joint estimation procedure that uses both option prices and realized variance data. Specifically, for the Heston model with volatility risk premium $\lambda^V = \lambda\sqrt{V}$: (a) what data goes into the $\mathbb{Q}$-likelihood? (b) what data goes into the $\mathbb{P}$-likelihood? (c) what parameters are shared across both likelihoods? (d) what parameters are identified only from one data source?

??? success "Solution to Exercise 4"
    **Joint estimation procedure for the Heston model with VRP:**

    The volatility risk premium enters through $\lambda^V = \lambda\sqrt{V}$, which shifts the variance drift between measures. Under $\mathbb{P}$, the variance follows $dV_t = \kappa^{\mathbb{P}}(\theta^{\mathbb{P}} - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{\mathbb{P}}$, and under $\mathbb{Q}$, $dV_t = \kappa^{\mathbb{Q}}(\theta^{\mathbb{Q}} - V_t)\,dt + \xi\sqrt{V_t}\,dW_t^{\mathbb{Q}}$ with $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda\xi$ and $\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/\kappa^{\mathbb{Q}}$.

    **(a) $\mathbb{Q}$-likelihood:** Cross-sectional option price data (implied volatilities across strikes and maturities on each observation date). The $\mathbb{Q}$-likelihood measures how well the model matches observed option prices using the risk-neutral parameters $(\kappa^{\mathbb{Q}}, \theta^{\mathbb{Q}}, \xi, \rho, V_0)$.

    **(b) $\mathbb{P}$-likelihood:** Time-series data of asset returns and (optionally) realized variance estimates. The $\mathbb{P}$-likelihood is constructed from the transition density of $(S_t, V_t)$ under the physical measure, evaluated at observed returns. If a volatility proxy (e.g., realized variance from high-frequency data) is available, it provides additional information about the variance path.

    **(c) Shared parameters:** The vol-of-vol $\xi$, correlation $\rho$, and the variance path $\{V_t\}$ are shared across both measures (the Girsanov change of measure does not affect diffusion coefficients). The spot variance $V_t$ at each date is a latent variable common to both likelihoods.

    **(d) Parameters identified from one source only:** The market price of volatility risk $\lambda$ is identified only from the joint information — it requires comparing $\mathbb{P}$ and $\mathbb{Q}$ parameters. The physical drift parameters $(\kappa^{\mathbb{P}}, \theta^{\mathbb{P}})$ are identified primarily from time-series data, while the risk-neutral drift parameters $(\kappa^{\mathbb{Q}}, \theta^{\mathbb{Q}})$ are identified primarily from option data.

---

**Exercise 5.** The relationship $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda\xi$ connects the two measures. Given $\xi = 0.4$ and estimates $\kappa^{\mathbb{P}} = 2.0$, $\kappa^{\mathbb{Q}} = 3.2$, compute $\lambda$. Then compute $\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/\kappa^{\mathbb{Q}}$ for $\theta^{\mathbb{P}} = 0.04$. Is the resulting $\theta^{\mathbb{Q}} > \theta^{\mathbb{P}}$ or $\theta^{\mathbb{Q}} < \theta^{\mathbb{P}}$? Interpret this result economically.

??? success "Solution to Exercise 5"
    **Computing $\lambda$:** From the relationship $\kappa^{\mathbb{Q}} = \kappa^{\mathbb{P}} + \lambda\xi$:

    $$
    \lambda = \frac{\kappa^{\mathbb{Q}} - \kappa^{\mathbb{P}}}{\xi} = \frac{3.2 - 2.0}{0.4} = 3.0
    $$

    **Computing $\theta^{\mathbb{Q}}$:** Using the relationship $\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/\kappa^{\mathbb{Q}}$:

    $$
    \theta^{\mathbb{Q}} = \frac{\kappa^{\mathbb{P}}\theta^{\mathbb{P}}}{\kappa^{\mathbb{Q}}} = \frac{2.0 \times 0.04}{3.2} = \frac{0.08}{3.2} = 0.025
    $$

    Since $\theta^{\mathbb{Q}} = 0.025 < 0.04 = \theta^{\mathbb{P}}$, the risk-neutral long-run variance is **lower** than the physical long-run variance.

    **Economic interpretation:** This result may seem counterintuitive, since we often observe $\theta^{\mathbb{Q}} > \theta^{\mathbb{P}}$ empirically. The reason is that the specific relationship $\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}/\kappa^{\mathbb{Q}}$ arises from preserving $\kappa\theta$ across measures (i.e., $\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}}$). Since $\kappa^{\mathbb{Q}} > \kappa^{\mathbb{P}}$, we must have $\theta^{\mathbb{Q}} < \theta^{\mathbb{P}}$ to maintain this equality.

    This means the risk premium is absorbed entirely through faster mean reversion rather than through a higher long-run level. The variance is pulled toward its mean more aggressively under $\mathbb{Q}$, so option prices reflect expectations of quicker volatility normalization. The product $\kappa^{\mathbb{Q}}\theta^{\mathbb{Q}} = \kappa^{\mathbb{P}}\theta^{\mathbb{P}} = 0.08$ is preserved, meaning the unconditional "pull" on the variance process is the same under both measures, but the speed-level decomposition differs.

---

**Exercise 6.** Explain why the VRP tends to be larger (more positive) during periods of market stress. Consider the following three mechanisms and explain how each contributes: (a) increased demand for portfolio insurance (OTM puts); (b) higher risk aversion during downturns; (c) correlation of volatility spikes with negative wealth shocks. Which mechanism do you think is most important?

??? success "Solution to Exercise 6"
    The VRP tends to be larger during market stress due to three reinforcing mechanisms:

    **(a) Increased demand for portfolio insurance:** During market downturns, institutional investors rush to buy OTM puts for portfolio protection. This demand pressure drives up option prices, particularly for puts, inflating implied volatility well above the level justified by expected future realized volatility. The supply of volatility insurance is relatively inelastic (dealers have limited capacity to warehouse volatility risk), so the demand shock translates directly into higher option premia and a wider VRP.

    **(b) Higher risk aversion during downturns:** In equilibrium asset pricing models with time-varying risk aversion (e.g., habit formation or loss aversion), investors become more risk-averse after wealth declines. Higher risk aversion means a larger Radon–Nikodym derivative $d\mathbb{Q}/d\mathbb{P}$ in bad states, which inflates the $\mathbb{Q}$-expectation of variance relative to $\mathbb{P}$. Formally, if the pricing kernel loads negatively on variance innovations, then the VRP equals the covariance of the pricing kernel with variance shocks, which becomes more negative (larger premium) when risk aversion is elevated.

    **(c) Correlation of volatility spikes with negative wealth shocks:** Volatility is strongly negatively correlated with equity returns (the "leverage effect"). This means volatility spikes coincide with states where investors' marginal utility is high. Since the risk premium for any risk factor is proportional to its covariance with the pricing kernel, and since high marginal utility (bad states) coincides with high volatility, variance carries a large negative risk premium (i.e., variance buyers accept lower expected returns because variance pays off in bad states). During stress, this correlation strengthens, amplifying the VRP.

    **Most important mechanism:** Mechanism (c) is arguably the most fundamental. The leverage effect is a structural feature of equity markets (driven by financial and operating leverage), and it directly connects variance risk to the pricing kernel through the negative correlation between returns and volatility. Mechanisms (a) and (b) are partly consequences of (c): the demand for puts is high precisely because volatility is correlated with negative returns, and risk aversion rises because volatility spikes accompany wealth destruction. However, mechanism (a) has the strongest short-term impact during acute crises, when the demand-supply imbalance in the options market can dominate.
