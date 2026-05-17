# Smile and Term Structure Revisited

The volatility smile and non-flat implied-volatility term structure are the most visible failures of constant-volatility Black–Scholes. They are introduced and analyzed in detail in Chapter 12; here we revisit them only to extract the empirical features that any stochastic volatility model must reproduce.

Recall (see [§ Skew and Smile](../../ch12/implied_volatility_surface/skew_and_smile.md)): implied volatility $\sigma_{\text{impl}}(K,T)$ is the unique $\sigma$ solving $C^{\text{BS}}(S_0,K,T,r,q,\sigma) = C^{\text{mkt}}(K,T)$; constant-vol predicts a flat surface, markets show a two-dimensional pattern in $(K,T)$.

Recall (see [§ Empirical Smile (SPX)](../../ch12/implied_volatility_surface/empirical_smile_spx.md)): equity indices show **negative skew** ($\sigma_{\text{impl}}(K_1) > \sigma_{\text{impl}}(K_2)$ for $K_1 < K_2$); FX shows a more symmetric **smile**; single-stock and commodity surfaces vary by sector.

Recall (see [§ Term Structure](../../ch12/implied_volatility_surface/term_structure.md)): the ATM term structure is upward-sloping in calm regimes, downward-sloping (backwardated) in stress; the variance-of-the-average representation $\sigma_{\text{impl}}^2(T)\cdot T \approx \int_0^T \mathbb{E}^{\mathbb{Q}}[V_s]\,ds$ links term structure to mean-reverting variance.

Recall (see [§ Smile Dynamics — Forward Smile](../../ch12/smile_dynamics/forward_smile.md)): short-maturity smiles are steeper, with skew scaling roughly as $1/\sqrt{T}$ under standard diffusion models; sticky-strike vs sticky-delta dynamics bracket the realistic regime.

---

## Economic Interpretation

The implied volatility surface encodes market beliefs and risk premia:

### Risk-Neutral Density

The Breeden–Litzenberger formula (Chapter 7) recovers the risk-neutral density:

$$
f^{\mathbb{Q}}(S_T = K) = e^{rT} \frac{\partial^2 C}{\partial K^2}\bigg|_{K}
$$

A non-flat smile implies a non-Gaussian risk-neutral density:

- Steep put skew → heavy left tail → crash risk priced
- Elevated wings → fat tails → extreme moves priced

### Variance Risk Premium

The gap between implied and realized variance:

$$
VRP = \mathbb{E}^{\mathbb{Q}}[\sigma^2] - \mathbb{E}^{\mathbb{P}}[\sigma^2]
$$

is typically positive for equity indices (investors pay a premium for volatility protection). The term structure of VRP reveals:

- Short-term VRP tends to be larger
- VRP increases during stress
- Mean reversion of VRP itself

### Demand and Supply

The smile also reflects market microstructure:

- Institutional demand for OTM puts (portfolio insurance)
- Market makers' inventory and hedging costs
- Flow imbalances in specific strikes/maturities

---

## Implications for Stochastic Volatility Models

A viable SV model must jointly explain smile existence, negative equity skew, smile curvature, skew decay in $T$, and the ATM term structure. Recall (see [§ Two-Factor Diffusion Models](../general_stochastic_volatility_framework/two_factor_diffusion_models.md) and [§ Heston Model Definition](../the_heston_model/model_definition.md)): the Heston parameters provide a minimal vocabulary — non-constant $V_t$ (smile), $\rho < 0$ (skew), $\xi > 0$ (curvature), $\kappa > 0$ (skew/term-structure decay).

---

## Empirical Smile: S&P 500 Example

Recall (see [§ Empirical Smile (SPX)](../../ch12/implied_volatility_surface/empirical_smile_spx.md) and [§ Term Structure](../../ch12/implied_volatility_surface/term_structure.md)): representative 1-month smile runs from $\sim 22\%$ at the 90% strike to $\sim 13.5\%$ at the 110% strike, and the ATM term structure under normal conditions rises gently from $\sim 14\%$ (1 week) to $\sim 19\%$ (2 years); qualitative features persist across regimes.

---

## Key Takeaways

- The volatility smile is ubiquitous and persistent across asset classes
- Equity indices exhibit negative skew; FX shows more symmetric smiles
- Term structure reflects volatility mean reversion and risk premia
- Short-maturity smiles are steeper than long-maturity smiles
- The smile encodes risk-neutral beliefs about tail risk
- Any realistic model must explain smile, skew, and term structure jointly

---

## Further Reading

- Rubinstein, M. (1994). *Implied binomial trees*. Journal of Finance.
- Gatheral, J. (2006). *The Volatility Surface: A Practitioner's Guide*. Wiley.
- Carr, P. & Wu, L. (2009). *Variance risk premiums*. Review of Financial Studies.
- Bates, D. (2000). *Post-'87 crash fears in the S&P 500 futures options market*. Journal of Econometrics.
- Cont, R. & da Fonseca, J. (2002). *Dynamics of implied volatility surfaces*. Quantitative Finance.

---

## Exercises

**Exercise 1.** The following ATM implied volatilities are observed for S&P 500 options:

| Maturity | Implied Vol |
|----------|-------------|
| 1 month  | 22%         |
| 3 months | 19%         |
| 6 months | 17%         |
| 1 year   | 16%         |

Is the term structure in contango or backwardation? What does this shape suggest about the current volatility regime relative to the long-run level? Estimate the long-run volatility $\bar{\sigma}$ implied by the data.

??? success "Solution to Exercise 1"
    **Contango vs. backwardation:** The term structure is **in backwardation** (also called inverted). Short-term implied volatility (22%) exceeds long-term implied volatility (16%), meaning $\sigma_{\text{impl}}(T)$ is decreasing in $T$.

    **Current volatility regime:** Backwardation indicates that current (instantaneous) volatility is **above** the long-run equilibrium level. The market expects volatility to **mean-revert downward** over time. This shape is typical during or just after a period of market stress, when realized volatility is elevated but expected to normalize.

    **Estimating long-run volatility $\bar{\sigma}$:** Under a mean-reverting volatility process, the implied volatility for very long maturities converges to $\bar{\sigma}$. The data show a decreasing pattern:

    | Maturity | Implied Vol |
    |----------|-------------|
    | 1 month  | 22%         |
    | 3 months | 19%         |
    | 6 months | 17%         |
    | 1 year   | 16%         |

    The rate of decrease is slowing (3% drop from 1m to 3m, 2% from 3m to 6m, 1% from 6m to 1y), suggesting convergence. Extrapolating, $\bar{\sigma} \approx 15\%$–$16\%$. A reasonable estimate is $\bar{\sigma} \approx 15\%$, representing the level the term structure is asymptotically approaching.

---

**Exercise 2.** Under a mean-reverting volatility process, the ATM implied variance satisfies approximately

$$
\sigma_{\text{impl}}^2(T) \approx V_0 \cdot \frac{1 - e^{-\kappa T}}{\kappa T} + \bar{\sigma}^2 \cdot \left(1 - \frac{1 - e^{-\kappa T}}{\kappa T}\right)
$$

Given $V_0 = (25\%)^2$, $\bar{\sigma}^2 = (18\%)^2$, and $\kappa = 2.0$, compute $\sigma_{\text{impl}}(T)$ for $T = 0.25, 0.5, 1.0, 2.0$ years. Verify that the term structure interpolates between $\sqrt{V_0}$ and $\bar{\sigma}$.

??? success "Solution to Exercise 2"
    The formula is

    $$
    \sigma_{\text{impl}}^2(T) = V_0 \cdot \frac{1 - e^{-\kappa T}}{\kappa T} + \bar{\sigma}^2 \cdot \left(1 - \frac{1 - e^{-\kappa T}}{\kappa T}\right)
    $$

    with $V_0 = 0.0625$, $\bar{\sigma}^2 = 0.0324$, and $\kappa = 2.0$.

    Define $g(T) = \dfrac{1 - e^{-\kappa T}}{\kappa T}$, so $\sigma_{\text{impl}}^2(T) = V_0 \cdot g(T) + \bar{\sigma}^2 \cdot (1 - g(T))$.

    **For $T = 0.25$:** $g(0.25) = \dfrac{1 - e^{-0.5}}{0.5} = \dfrac{1 - 0.6065}{0.5} = \dfrac{0.3935}{0.5} = 0.7870$

    $$
    \sigma_{\text{impl}}^2 = 0.0625 \times 0.7870 + 0.0324 \times 0.2130 = 0.04919 + 0.006900 = 0.05609
    $$

    $$
    \sigma_{\text{impl}} = \sqrt{0.05609} \approx 23.68\%
    $$

    **For $T = 0.5$:** $g(0.5) = \dfrac{1 - e^{-1.0}}{1.0} = 1 - 0.3679 = 0.6321$

    $$
    \sigma_{\text{impl}}^2 = 0.0625 \times 0.6321 + 0.0324 \times 0.3679 = 0.03951 + 0.01192 = 0.05143
    $$

    $$
    \sigma_{\text{impl}} = \sqrt{0.05143} \approx 22.68\%
    $$

    **For $T = 1.0$:** $g(1.0) = \dfrac{1 - e^{-2.0}}{2.0} = \dfrac{1 - 0.1353}{2.0} = \dfrac{0.8647}{2.0} = 0.4324$

    $$
    \sigma_{\text{impl}}^2 = 0.0625 \times 0.4324 + 0.0324 \times 0.5676 = 0.02703 + 0.01839 = 0.04542
    $$

    $$
    \sigma_{\text{impl}} = \sqrt{0.04542} \approx 21.31\%
    $$

    **For $T = 2.0$:** $g(2.0) = \dfrac{1 - e^{-4.0}}{4.0} = \dfrac{1 - 0.01832}{4.0} = \dfrac{0.9817}{4.0} = 0.2454$

    $$
    \sigma_{\text{impl}}^2 = 0.0625 \times 0.2454 + 0.0324 \times 0.7546 = 0.01534 + 0.02445 = 0.03979
    $$

    $$
    \sigma_{\text{impl}} = \sqrt{0.03979} \approx 19.95\%
    $$

    **Summary:**

    | $T$ | $g(T)$ | $\sigma_{\text{impl}}$ |
    |-----|--------|------------------------|
    | 0.25 | 0.787 | 23.68% |
    | 0.50 | 0.632 | 22.68% |
    | 1.00 | 0.432 | 21.31% |
    | 2.00 | 0.245 | 19.95% |

    **Verification:** As $T \to 0$, $g(T) \to 1$, so $\sigma_{\text{impl}} \to \sqrt{V_0} = 25\%$. As $T \to \infty$, $g(T) \to 0$, so $\sigma_{\text{impl}} \to \bar{\sigma} = 18\%$. The computed values decrease monotonically from near 25% toward 18%, confirming the interpolation property.

---

**Exercise 3.** For equity index options, the implied volatility skew is often measured as

$$
\text{Skew} = \sigma_{\text{impl}}(90\%) - \sigma_{\text{impl}}(100\%)
$$

where percentages refer to strike as a fraction of spot. Suppose the 1-month skew is 7% and the 1-year skew is 2.5%. Verify that this is roughly consistent with the scaling relationship $\text{Skew}(T) \propto 1/\sqrt{T}$. What mechanism in stochastic volatility models generates this decay?

??? success "Solution to Exercise 3"
    **Verifying the scaling relationship:**

    If $\text{Skew}(T) \propto 1/\sqrt{T}$, then

    $$
    \frac{\text{Skew}(T_1)}{\text{Skew}(T_2)} = \sqrt{\frac{T_2}{T_1}}
    $$

    With $T_1 = 1/12$ year (1 month) and $T_2 = 1$ year:

    $$
    \frac{\text{Skew}(1/12)}{\text{Skew}(1)} = \sqrt{\frac{1}{1/12}} = \sqrt{12} \approx 3.46
    $$

    The observed ratio:

    $$
    \frac{7\%}{2.5\%} = 2.80
    $$

    The predicted ratio is 3.46, while the observed ratio is 2.80. These are in **rough agreement** (within the range expected given the approximation), confirming the $1/\sqrt{T}$ scaling as a reasonable first-order description. The slight discrepancy may arise from:

    - Higher-order terms in the expansion
    - Vol-of-vol effects that modify the scaling
    - The term structure of skew not being exactly power-law

    **Mechanism in stochastic volatility models:** The $1/\sqrt{T}$ decay arises from the interaction of two effects:

    1. **Price-volatility correlation ($\rho < 0$):** This generates skew. Over short horizons, a single volatility shock has a proportionally large effect on the return distribution's asymmetry
    2. **Mean reversion of volatility ($\kappa > 0$):** Over longer horizons, volatility reverts to its mean, diluting the impact of the current price-vol correlation. The effective skew contribution of any single shock decays as the volatility mean-reverts

    Mathematically, the skew scales as $\rho \xi / \sqrt{T}$ to leading order in stochastic volatility expansions, where $\rho$ is the correlation and $\xi$ is the vol-of-vol. The $1/\sqrt{T}$ factor reflects the central limit theorem: over longer periods, the accumulated skew from many small shocks averages out relative to the total variance.

---

**Exercise 4.** Using the Breeden–Litzenberger formula, the risk-neutral density is

$$
f^{\mathbb{Q}}(S_T = K) = e^{rT} \frac{\partial^2 C}{\partial K^2}\bigg|_{K}
$$

Suppose the call price function is $C(K) = e^{-rT}[\mu - K + \frac{1}{2}\sigma^2 K^{-1}]$ for a hypothetical model. Compute $\partial^2 C / \partial K^2$ and interpret the shape of the implied risk-neutral density. How would this density differ from a lognormal?

??? success "Solution to Exercise 4"
    **Computing the second derivative:**

    Given $C(K) = e^{-rT}\left[\mu - K + \frac{1}{2}\sigma^2 K^{-1}\right]$:

    First derivative:

    $$
    \frac{\partial C}{\partial K} = e^{-rT}\left[-1 - \frac{1}{2}\sigma^2 K^{-2}\right]
    $$

    Second derivative:

    $$
    \frac{\partial^2 C}{\partial K^2} = e^{-rT}\left[\sigma^2 K^{-3}\right] = \frac{e^{-rT}\sigma^2}{K^3}
    $$

    Applying the Breeden–Litzenberger formula:

    $$
    f^{\mathbb{Q}}(S_T = K) = e^{rT} \cdot \frac{e^{-rT}\sigma^2}{K^3} = \frac{\sigma^2}{K^3}
    $$

    **Interpretation:** The risk-neutral density is $f^{\mathbb{Q}}(x) = \sigma^2 / x^3$ for $x > 0$. This is a **heavy-tailed, right-skewed** density (a Pareto-type distribution), meaning:

    1. **Heavy right tail:** The density decays as $x^{-3}$, which is much slower than the exponential decay of a lognormal distribution. This implies significantly higher probability of extreme upward moves
    2. **No left tail concentration:** Unlike equity distributions, there is no extra weight on the left tail
    3. **Infinite variance:** The $x^{-3}$ tail implies that the second moment $\mathbb{E}[S_T^2] = \int \sigma^2 x^{-1}\,dx$ diverges, unlike a lognormal which has all moments finite

    **Difference from lognormal:** A lognormal density has the form $f(x) = \frac{1}{x\sigma_{\ln}\sqrt{2\pi}} \exp\left(-\frac{(\ln x - \mu_{\ln})^2}{2\sigma_{\ln}^2}\right)$, which decays faster than any power law. The hypothetical $K^{-3}$ density has much heavier tails and would generate a strongly upward-sloping implied volatility smile for high strikes.

    Note: This hypothetical call price function is illustrative and may not satisfy all no-arbitrage conditions (such as proper boundary behavior), but it demonstrates how the Breeden–Litzenberger formula extracts distributional information.

---

**Exercise 5.** Explain the difference between "sticky strike" and "sticky delta" smile dynamics. A trader observes that when the S&P 500 drops by 2%, the implied volatility of a fixed-strike 4000 put increases by 1.5 vol points, while the 25-delta put implied vol remains roughly unchanged. Which smile model is more consistent with this observation? What are the hedging implications of using the wrong model?

??? success "Solution to Exercise 5"
    **Sticky strike:** The implied volatility of a specific strike $K$ remains constant as the underlying moves. The smile is "anchored" to absolute strike levels.

    **Sticky delta:** The implied volatility for a specific delta level (e.g., 25-delta put) remains constant as the underlying moves. The smile is "anchored" to moneyness relative to the current forward.

    **Analysis of the observation:**

    When the S&P 500 drops by 2%:

    - The fixed-strike 4000 put's implied vol increases by 1.5 vol points — this means the implied volatility at strike 4000 is **not** constant; it increased. This is **inconsistent with sticky strike**, which would predict no change
    - The 25-delta put implied vol remains roughly unchanged — this means the smile, when parameterized by delta (i.e., relative moneyness), is stable

    This observation is **consistent with sticky delta** (floating smile). As the spot drops, the 4000 strike becomes less out-of-the-money (closer to ATM), and under sticky delta, it "picks up" the higher implied vol associated with its new, less-OTM delta level. Meanwhile, the 25-delta put (which now corresponds to a lower absolute strike) retains the same implied vol.

    **Hedging implications of using the wrong model:**

    - **Using sticky strike when reality is sticky delta:** The trader underestimates how much implied vol changes when the spot moves. Delta hedges will be systematically wrong because the model misses the skew-induced delta adjustment. Specifically, the "skew delta" correction:

    $$
    \Delta_{\text{adjusted}} = \Delta_{\text{BS}} + \mathcal{V} \cdot \frac{\partial \sigma_{\text{impl}}}{\partial S}
    $$

    is zero under sticky strike but nonzero under sticky delta, leading to **under-hedging of downside risk**

    - **Using sticky delta when reality is sticky strike:** The trader over-adjusts for smile dynamics, introducing unnecessary hedging activity and transaction costs

---

**Exercise 6.** The variance risk premium is defined as $VRP = \mathbb{E}^{\mathbb{Q}}[\sigma^2] - \mathbb{E}^{\mathbb{P}}[\sigma^2]$. Given a 3-month variance swap rate of $(17\%)^2$ and an expected realized variance of $(14\%)^2$, compute the annualized $VRP$. A trader sells the variance swap at the swap rate and realizes the actual variance. What is the expected profit in variance points? Why is this premium typically positive for equity indices?

??? success "Solution to Exercise 6"
    **Computing the annualized VRP:**

    $$
    VRP = \mathbb{E}^{\mathbb{Q}}[\sigma^2] - \mathbb{E}^{\mathbb{P}}[\sigma^2] = (0.17)^2 - (0.14)^2 = 0.0289 - 0.0196 = 0.0093
    $$

    The annualized $VRP$ is $93$ variance points (or $0.93\%$ in variance terms).

    **Expected profit for the variance swap seller:**

    The trader sells the variance swap at the swap rate $(17\%)^2 = 0.0289$ and pays out the realized variance. The expected P&L is:

    $$
    \text{Expected P\&L} = \text{Swap rate} - \mathbb{E}^{\mathbb{P}}[\text{RV}^2] = 0.0289 - 0.0196 = 0.0093
    $$

    In volatility points: the trader receives an implied vol of 17% but expects to pay only 14%, netting approximately 3 vol points of profit (in variance terms, 93 variance points for a 3-month horizon).

    **Why the premium is typically positive for equity indices:**

    1. **Insurance demand:** Institutional investors (pension funds, endowments) systematically buy portfolio insurance via puts and variance swaps, pushing up the risk-neutral expected variance
    2. **Leverage effect:** Volatility spikes during market downturns, so variance swap sellers lose money precisely when broader portfolios are also losing — this systematic risk requires compensation
    3. **Negatively correlated with consumption:** High volatility periods coincide with recessions and declining consumption, making variance exposure a source of systematic risk
    4. **Jump risk:** The risk-neutral measure overweights crash scenarios relative to the physical measure, inflating the variance swap rate

---

**Exercise 7.** A stochastic volatility model must jointly explain the smile, skew, and term structure. Fill in the following mapping and give a brief justification for each entry:

| Surface feature         | Model parameter        |
|------------------------|------------------------|
| Negative equity skew    | ?                      |
| Smile curvature (wings) | ?                      |
| Term structure shape    | ?                      |
| ATM level              | ?                      |

Using the Heston model parameters ($\kappa$, $\theta$, $\xi$, $\rho$, $V_0$), identify which parameter primarily controls each feature.

??? success "Solution to Exercise 7"
    The completed table with Heston model parameter identification:

    | Surface feature         | Model parameter        | Justification |
    |------------------------|------------------------|---------------|
    | Negative equity skew    | $\rho$ (price-vol correlation) | A negative $\rho$ means that when $S$ drops, $V$ tends to rise, making the risk-neutral distribution left-skewed and generating higher implied vol for low strikes |
    | Smile curvature (wings) | $\xi$ (vol-of-vol) | A larger $\xi$ increases the variability of volatility, fattening both tails of the risk-neutral distribution and raising implied vol for both deep OTM puts and calls |
    | Term structure shape    | $\kappa$ (mean-reversion speed) | Fast mean reversion ($\kappa$ large) causes short-term vol to revert quickly to $\theta$, flattening the term structure; slow mean reversion preserves the gap between $V_0$ and $\theta$ |
    | ATM level              | $V_0$ and $\theta$ (current and long-run variance) | $V_0$ determines the short-term ATM level, while $\theta$ sets the long-term ATM level; the ATM implied vol interpolates between $\sqrt{V_0}$ and $\sqrt{\theta}$ |

    **Detailed justifications:**

    - **$\rho$ controls skew:** In the Heston model, the instantaneous correlation between $dW^S$ and $dW^V$ is $\rho$. When $\rho < 0$, a downward move in $S$ coincides with an upward move in $V$, so the conditional distribution after a price decline has higher variance. This asymmetry generates negative skew in the implied volatility surface. Typical equity index values are $\rho \in [-0.9, -0.5]$

    - **$\xi$ controls curvature:** The vol-of-vol parameter determines how much $V_t$ fluctuates around its mean. Higher $\xi$ leads to greater dispersion in realized volatility paths, which translates to fatter tails in the terminal distribution and more pronounced smile curvature (higher wings)

    - **$\kappa$ controls term structure:** The mean-reversion speed governs how quickly $V_t$ returns to $\theta$. For short maturities, implied vol is near $\sqrt{V_0}$; for long maturities, it approaches $\sqrt{\theta}$. The rate of transition is controlled by $\kappa$

    - **$V_0$ and $\theta$ control ATM level:** The current variance $V_0$ sets the starting point and dominates short-maturity ATM implied vol, while the long-run mean $\theta$ determines the asymptotic ATM level
