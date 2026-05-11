# Joint Calibration Across Strikes and Maturities


Stochastic volatility parameters influence the **entire implied volatility surface**. Reliable calibration therefore requires fitting **jointly across strikes and maturities**, rather than focusing on individual slices.

---

## Why joint calibration is necessary


Single-maturity calibration can:

- fit the smile locally,
- but produce inconsistent parameters across maturities.

Joint calibration enforces:

- parameter consistency,
- coherent term-structure behavior,
- improved identifiability.

---

## Objective function across the surface


A typical joint objective is

$$
\mathcal{L}(\theta)
= \frac12\sum_{i,j} w_{ij}
\big(\sigma^{\text{model}}_{\text{impl}}(k_i,T_j;\theta)

- \sigma^{\text{mkt}}_{\text{impl}}(k_i,T_j)\big)^2
$$



Key design choices:

- maturity balancing (avoid one tenor dominating),
- liquidity-based weights,
- exclusion of unreliable wings.

---

## Surface-wide sensitivities


Parameters affect different regions:

- $\rho$: skew across strikes,
- $\xi$: smile curvature and term-structure interaction,
- $\kappa, \theta$: long-maturity variance level.

Joint calibration ensures these effects are reconciled globally.

---

## Numerical considerations


- pricing speed is critical (FFT, closed forms),
- gradients/Jacobians improve optimizer robustness,
- good initial guesses reduce convergence to spurious minima.

---

## Validation


After calibration, validate by:

- checking per-maturity residual patterns,
- ensuring smooth parameter evolution over time,
- testing sensitivity to weight changes.

---

## Key takeaways


- Joint calibration improves identifiability and consistency.
- Weighting and maturity balance are as important as the model.
- Global surface fit is more meaningful than local perfection.

---

## Further reading


- Gatheral, *The Volatility Surface*.
- Lord & Kahl, efficient Heston calibration.
- Andersen & Piterbarg, multi-maturity calibration practice.

---

## Exercises

**Exercise 1.** A joint calibration objective is

$$
\mathcal{L}(\theta) = \frac{1}{2}\sum_{i,j} w_{ij}\bigl(\sigma^{\text{model}}_{\text{impl}}(k_i, T_j; \theta) - \sigma^{\text{mkt}}_{\text{impl}}(k_i, T_j)\bigr)^2
$$

Suppose the surface has 5 strikes and 4 maturities (20 data points). If the Heston model has 5 free parameters, what is the degrees-of-freedom count? Is the system over-determined, under-determined, or exactly determined? What would happen if the model had 20 free parameters instead?

??? success "Solution to Exercise 1"
    The degrees of freedom equal the number of data points minus the number of free parameters:

    $$
    \text{d.f.} = 20 - 5 = 15
    $$

    The system is **over-determined**: there are 20 equations (implied vol constraints) but only 5 unknowns. This means we cannot expect a perfect fit, and the calibration minimizes the weighted sum of squared residuals. The 15 excess constraints provide the information needed to pin down the parameters and allow us to assess goodness of fit (e.g., via RMSE or chi-squared statistics).

    **If the model had 20 free parameters:** The system would be **exactly determined** (d.f. $= 0$), meaning the model could interpolate all market quotes perfectly. However, this would be problematic:

    - The model would overfit, matching noise in the data
    - There would be no residual information to assess fit quality
    - The parameter estimates would be highly sensitive to individual quotes (no statistical averaging)
    - Out-of-sample performance (pricing options at non-observed strikes/maturities) would likely be poor
    - The calibration would essentially become a complex interpolation scheme rather than a parsimonious model

    A model with more than 20 free parameters would be under-determined, with infinitely many exact-fit solutions and no meaningful parameter estimates without regularization.

---

**Exercise 2.** Explain why equal weighting across maturities can lead to the short-maturity smile dominating the calibration. If the surface has 5 strikes at each of $T = 0.08, 0.25, 0.5, 1.0$ years, and ATM implied vols are $25\%, 20\%, 18\%, 17\%$, propose a weighting scheme that balances maturities. One common choice is $w_{ij} = 1/\sigma^{\text{mkt}}(k_i, T_j)^2$. Explain the rationale.

??? success "Solution to Exercise 2"
    **Why equal weighting biases toward short maturities:** Short-maturity options have higher absolute implied volatilities and steeper smiles (larger absolute differences across strikes). With equal weights, the larger absolute residuals at short maturities contribute more to the objective function, causing the optimizer to prioritize fitting the short end at the expense of longer maturities. In the given example, the 25% ATM vol at $T = 0.08$ generates residuals roughly $25/17 \approx 1.47$ times larger than the 17% ATM vol at $T = 1.0$ for the same relative misfit.

    **Proposed weighting scheme:** The inverse-variance weighting $w_{ij} = 1/\sigma^{\text{mkt}}(k_i, T_j)^2$ normalizes each residual by the market level:

    $$
    \mathcal{L}(\theta) = \frac{1}{2}\sum_{i,j}\frac{1}{\sigma^{\text{mkt}}(k_i, T_j)^2}\bigl(\sigma^{\text{model}}(k_i, T_j; \theta) - \sigma^{\text{mkt}}(k_i, T_j)\bigr)^2
    $$

    **Rationale:** This transforms the objective into a sum of squared *relative* errors. Each term becomes

    $$
    \Bigl(\frac{\sigma^{\text{model}} - \sigma^{\text{mkt}}}{\sigma^{\text{mkt}}}\Bigr)^2
    $$

    which treats a 1% relative misfit at 25% vol the same as a 1% relative misfit at 17% vol. This ensures that all maturities contribute roughly equally to the optimization, regardless of their absolute implied vol levels.

    For the given data, the weights at ATM would be $w \propto 1/(0.25)^2 = 16$ at $T = 0.08$ versus $w \propto 1/(0.17)^2 \approx 34.6$ at $T = 1.0$, effectively upweighting the long end to compensate for its lower absolute vol.

---

**Exercise 3.** The Heston parameter $\rho$ primarily controls the skew across strikes, while $\kappa$ and $\theta$ primarily control the term structure. Design a two-stage calibration: (a) first fix $\kappa$ and $\theta$ using ATM implied volatilities across maturities; (b) then calibrate $\rho$, $\xi$, and $V_0$ to the full smile at each maturity. What advantages does this staged approach have over simultaneous optimization? What are its drawbacks?

??? success "Solution to Exercise 3"
    **Two-stage calibration:**

    **(a) Stage 1 — ATM term structure:** Extract ATM implied volatilities $\sigma_{\text{ATM}}(T_j)$ for each maturity $T_j$. Using the Heston ATM variance approximation

    $$
    \sigma_{\text{ATM}}^2(T) \approx V_0 \cdot \frac{1-e^{-\kappa T}}{\kappa T} + \theta\Bigl(1 - \frac{1-e^{-\kappa T}}{\kappa T}\Bigr)
    $$

    fit $\kappa$ and $\theta$ (and possibly $V_0$) to the ATM term structure. This is a low-dimensional problem (2--3 parameters, one data point per maturity) that can be solved quickly and robustly.

    **(b) Stage 2 — Full smile:** With $\kappa$ and $\theta$ fixed from Stage 1, calibrate $\rho$, $\xi$, and $V_0$ to the full implied volatility surface across all strikes and maturities. These three parameters control the skew ($\rho$), curvature ($\xi$), and short-term level ($V_0$) of the smile, and are typically well-identified from cross-sectional data.

    **Advantages:**

    - Each stage solves a lower-dimensional problem, reducing the risk of convergence to local minima
    - Stage 1 isolates the poorly-identified $(\kappa, \theta)$ pair and constrains them from term-structure information (where they are most identifiable)
    - Stage 2 benefits from a well-conditioned landscape since $\rho$ and $\xi$ have distinct effects on the smile shape
    - The overall procedure is faster and more transparent than simultaneous optimization

    **Drawbacks:**

    - The ATM variance approximation used in Stage 1 is not exact; the true ATM implied vol depends on all five parameters (including $\rho$ and $\xi$)
    - Stage 1 ignores information from the smile shape that could help identify $\kappa$ and $\theta$
    - The two stages may not converge to the global optimum of the joint objective — the staged solution is generally suboptimal compared to full simultaneous calibration
    - The approach assumes a clean separation of parameter effects that may not hold for extreme parameters

---

**Exercise 4.** After calibrating the Heston model to the full surface, the residuals $\sigma^{\text{model}} - \sigma^{\text{mkt}}$ show a systematic pattern: the model overprices short-maturity OTM puts and underprices long-maturity ATM options. What does this pattern suggest about the model's limitations? Which additional model feature (jumps, time-dependent parameters, multi-factor volatility) would most likely address this pattern?

??? success "Solution to Exercise 4"
    **Interpreting the residual pattern:** The systematic pattern — overpricing short-maturity OTM puts and underpricing long-maturity ATM options — reveals two distinct limitations of the basic Heston model:

    - **Short-maturity OTM puts overpriced:** The Heston model generates too much left-tail probability at short maturities. In the Heston framework, the short-maturity smile is driven primarily by $\rho$ and $\xi$, and the model can produce steep skew through negative $\rho$. However, the diffusive dynamics generate skew that decays at rate $1/\sqrt{T}$, which may not match the market's steeper short-maturity skew (often driven by jump risk). By calibrating $\rho$ to match the overall skew level, the model may overshoot at short maturities while undershooting at longer ones.

    - **Long-maturity ATM options underpriced:** The Heston model's constant-parameter structure constrains the variance term structure. If the model cannot simultaneously match the short-maturity smile steepness and the long-maturity ATM level, the long-end fit suffers. This suggests the market prices in features not captured by constant Heston parameters.

    **Most likely remedy — jumps in the asset price:** Adding a jump component (e.g., Bates model = Heston + Merton jumps) would most directly address the pattern:

    - Jumps generate additional short-maturity OTM put pricing *independently* of $\rho$, so the model need not overload $\rho$ to match short-dated skew. The jump intensity and size handle short-maturity tail risk, while $\rho$ handles the diffusive skew at longer maturities.
    - With jumps absorbing the short-maturity smile steepness, the remaining Heston parameters ($\kappa$, $\theta$) are free to better fit the long-maturity ATM level.

    Time-dependent parameters could also address this (e.g., piecewise-constant $\xi(t)$ or $\rho(t)$), but at the cost of additional complexity and potential instability. Multi-factor volatility models add flexibility in the term structure but may not specifically address the OTM put mispricing.

---

**Exercise 5.** A calibration uses 30 market quotes (6 strikes $\times$ 5 maturities) with weights proportional to open interest. The resulting RMSE in implied vol is 0.45%. If the weights are changed to be uniform, the RMSE drops to 0.38% but the longest-maturity fit deteriorates significantly. Discuss the trade-off. In a production setting for hedging vanilla options, which weighting would you prefer and why?

??? success "Solution to Exercise 5"
    **Trade-off analysis:**

    The open-interest weighting produces RMSE $= 0.45\%$ but distributes errors according to market liquidity, meaning the most actively traded instruments (which generate the most hedging demand) are fitted best. The higher overall RMSE is driven by poor fit on illiquid, low-open-interest instruments.

    The uniform weighting produces lower RMSE $= 0.38\%$ overall but deteriorates the long-maturity fit significantly. This means the optimizer reallocated fitting capacity from liquid long-maturity options to improve already-well-fitted short-maturity instruments.

    **Production recommendation:** For hedging vanilla options, **open-interest weighting** (or more generally, liquidity-based weighting) is preferred for several reasons:

    - Hedging P&L is concentrated in liquid instruments where the desk has the largest positions. A 0.1% implied vol misfit on a highly traded option matters more than a 0.5% misfit on a rarely traded one.
    - Long-maturity options carry more vega per contract, so a given implied vol error translates into a larger dollar hedging error. Sacrificing long-maturity fit (as uniform weighting does) can create significant risk.
    - The illiquid instruments that inflate RMSE under open-interest weighting often have wide bid-ask spreads, so their "market" implied vols are less reliable. Fitting them precisely may actually be fitting noise.
    - The 0.07% RMSE improvement under uniform weighting is likely within the bid-ask spread of most instruments and therefore economically insignificant.

    The 0.45% RMSE under open-interest weighting is acceptable if the residuals at high-open-interest instruments are within bid-ask bounds (typically 0.2--0.5 vol points for liquid equity index options).

---

**Exercise 6.** Compare single-maturity calibration with joint calibration by considering the following experiment: calibrate the Heston model separately to each of $T = 0.25, 0.5, 1.0$ (yielding three separate parameter sets $\theta_1, \theta_2, \theta_3$) and jointly to all three maturities (yielding one parameter set $\theta_{\text{joint}}$). If the separate calibrations give $\kappa_1 = 5.0$, $\kappa_2 = 2.5$, $\kappa_3 = 1.8$, what does this variation reveal about the Heston model? Would you expect $\kappa_{\text{joint}}$ to be close to any of the individual values?

??? success "Solution to Exercise 6"
    **What the $\kappa$ variation reveals:** The decreasing pattern $\kappa_1 = 5.0 > \kappa_2 = 2.5 > \kappa_3 = 1.8$ across maturities $T = 0.25, 0.5, 1.0$ reveals a fundamental limitation of the Heston model: **the constant-parameter assumption is inconsistent with the market's term structure of implied volatility dynamics.**

    Each single-maturity calibration finds the $\kappa$ that best explains that particular slice of the smile. The short-maturity calibration ($T = 0.25$) needs fast mean reversion ($\kappa = 5.0$) to match the observed smile shape and level, while the long-maturity calibration ($T = 1.0$) needs slower mean reversion ($\kappa = 1.8$) to match the flatter, less steep long-dated smile. This suggests that the volatility dynamics are richer than a single mean-reversion speed can capture — possibly due to multiple volatility factors operating on different time scales, or due to jump components that affect short and long maturities differently.

    **Expectation for $\kappa_{\text{joint}}$:** The joint calibration must compromise across all three maturities, so $\kappa_{\text{joint}}$ will generally be a **weighted average** of the individual values, with the weights depending on the number of quotes and the weighting scheme at each maturity. One would expect

    $$
    \kappa_3 = 1.8 \leq \kappa_{\text{joint}} \leq \kappa_1 = 5.0
    $$

    with $\kappa_{\text{joint}}$ likely falling near the center, perhaps around $2.5$--$3.0$, though the exact value depends on the relative influence of each maturity in the objective.

    Importantly, $\kappa_{\text{joint}}$ will **not** be close to any single individual value, and the joint fit will be worse than any single-maturity fit at its own maturity. The residual pattern will typically show systematic structure (e.g., overpricing short-maturity options and underpricing long-maturity ones, or vice versa), confirming that the model is misspecified in its term-structure behavior. This motivates extensions such as multi-factor stochastic volatility models (e.g., double Heston with two mean-reversion speeds) or models with time-dependent parameters.
