# Identifiability Issues


Credit risk calibration suffers from **identifiability problems**, especially when multiple parameters affect prices in similar ways.

---

## Recovery vs hazard rate trade-off


A central identifiability issue is:

- higher hazard rate + higher recovery
- vs lower hazard rate + lower recovery.

Both can fit the same CDS spreads.

---

## Limited market information


Challenges include:

- sparse maturity coverage,
- illiquidity in stressed markets,
- noisy quotes.

This limits the information content of calibration targets.

---

## Consequences in practice


Poor identifiability leads to:

- unstable parameter estimates,
- sensitivity to small quote changes,
- misleading economic interpretation.

These are intrinsic inverse-problem features.

---

## Mitigation strategies


Stability is improved by:

- fixing recovery rates,
- restricting parameter dynamics,
- smoothing hazard rate curves,
- prioritizing robust fits.

---

## Key takeaways


- Identifiability issues are inherent in credit calibration.
- Recovery and intensity are weakly separable.
- Stability often outweighs theoretical precision.

---

## Further reading


- Engl et al., inverse problems.
- Cont, model uncertainty in credit.

---

## Exercises

**Exercise 1.** A 5-year CDS spread is 90 bp. Show that the parameter pairs $(\lambda = 1.5\%, R = 40\%)$ and $(\lambda = 1.29\%, R = 30\%)$ both approximately reproduce this spread using $s \approx (1 - R)\lambda$. What does this imply about the uniqueness of the calibrated parameters?

??? success "Solution to Exercise 1"
    **Given:** 5-year CDS spread $s = 90$ bp = 0.0090.

    **Pair 1:** $\lambda = 1.5\%$, $R = 40\%$

    $$
    s \approx (1-R)\lambda = (1 - 0.40) \times 0.015 = 0.60 \times 0.015 = 0.0090 = 90 \text{ bp} \quad \checkmark
    $$

    **Pair 2:** $\lambda = 1.29\%$, $R = 30\%$

    $$
    s \approx (1-R)\lambda = (1 - 0.30) \times 0.0129 = 0.70 \times 0.0129 = 0.00903 \approx 90 \text{ bp} \quad \checkmark
    $$

    Both parameter pairs reproduce the observed spread to within rounding precision.

    **Implication for uniqueness:**

    The calibrated parameters $(\lambda, R)$ are **not uniquely determined** by the CDS spread alone. The approximate pricing equation $s \approx (1-R)\lambda$ defines a **one-dimensional manifold** (a curve) in the $(\lambda, R)$ parameter space:

    $$
    \lambda = \frac{s}{1-R}
    $$

    Any point on this curve produces the same spread. The two pairs given are simply two points on this curve:

    - $(R = 0.40, \lambda = 0.015)$
    - $(R = 0.30, \lambda = 0.0129)$

    This means the calibration problem has infinitely many solutions. To obtain a unique solution, one must either:

    1. Fix $R$ externally (e.g., $R = 40\%$ by convention) and solve for $\lambda$, or
    2. Use additional market data that provides independent information about $R$ (e.g., defaulted bond prices, recovery rate swaps), or
    3. Calibrate to multiple instruments that break the degeneracy (e.g., CDS with different subordination levels, equity tranche prices).

    This is the fundamental **recovery-intensity identifiability problem** in credit risk calibration.

---

**Exercise 2.** Suppose a calibration procedure recovers hazard rates $\lambda_1 = 120$ bp and $\lambda_2 = 180$ bp from two CDS maturities. A small change in the 3-year CDS spread (from 100 bp to 105 bp) causes $\lambda_2$ to jump from 180 bp to 230 bp. Explain why this instability arises and how it relates to the condition number of the inverse problem.

??? success "Solution to Exercise 2"
    **The instability scenario:** A 5 bp change in the 3-year CDS spread (from 100 bp to 105 bp) causes $\lambda_2$ to jump from 180 bp to 230 bp---a 50 bp change, representing a 10:1 amplification factor.

    **Why this instability arises:**

    In sequential bootstrapping, $\lambda_2$ is determined by the **marginal** information in the 3-year CDS spread, after accounting for the contribution of the already-calibrated $\lambda_1$. The 3-year CDS spread reflects the *average* intensity over $[0, 3]$, but $\lambda_1$ is already fixed from the 1-year CDS. The marginal hazard rate $\lambda_2$ must absorb all the difference between the 3-year CDS's requirements and what $\lambda_1$ already provides.

    Formally, the 3-year CDS spread is approximately:

    $$
    s_3 \approx (1-R) \cdot \bar{\lambda}_{[0,3]}
    $$

    where $\bar{\lambda}_{[0,3]}$ is the average intensity over $[0,3]$. With $\lambda_1$ covering $[0,1]$ and $\lambda_2$ covering $(1,3]$:

    $$
    \bar{\lambda}_{[0,3]} = \frac{1 \cdot \lambda_1 + 2 \cdot \lambda_2}{3}
    $$

    Solving for $\lambda_2$:

    $$
    \lambda_2 = \frac{3 \cdot \bar{\lambda}_{[0,3]} - \lambda_1}{2} = \frac{3s_3/(1-R) - \lambda_1}{2}
    $$

    A perturbation $\delta s_3$ in the 3-year spread produces:

    $$
    \delta \lambda_2 = \frac{3}{2(1-R)} \delta s_3 = \frac{3}{2 \times 0.60} \times 5 = \frac{3 \times 5}{1.2} = 12.5 \text{ bp}
    $$

    However, when the premium payment dates, discounting, and the nonlinear survival probability function are included, the amplification can be even larger, especially when the marginal period is short relative to the total maturity.

    **Connection to the condition number:**

    This is an **ill-conditioned inverse problem**. The condition number measures how much the output (parameters) changes relative to a change in input (market data):

    $$
    \kappa = \frac{\|\delta \lambda_2\| / \|\lambda_2\|}{\|\delta s_3\| / \|s_3\|} = \frac{50/180}{5/100} = \frac{0.278}{0.050} = 5.56
    $$

    A condition number of 5.56 means that a 1% perturbation in the input spread produces a 5.56% perturbation in the output hazard rate. Large condition numbers indicate that the inverse problem amplifies data noise, making parameter estimates unreliable.

    The instability is particularly severe when:

    - The marginal period is short (small $\Delta T$), concentrating all adjustment into a narrow interval
    - The spread curve is nearly flat, so marginal information content is low
    - Earlier hazard rates absorb most of the average, leaving $\lambda_2$ to capture a small residual with high sensitivity

---

**Exercise 3.** Describe the "recovery-intensity trade-off" in formal terms. Given the approximate CDS pricing equation $s \approx (1 - R)\lambda$, show that the partial derivatives $\partial s / \partial R$ and $\partial s / \partial \lambda$ are proportional, making $R$ and $\lambda$ nearly collinear in calibration. What additional data or constraints could break this collinearity?

??? success "Solution to Exercise 3"
    **Formal statement of the recovery-intensity trade-off:**

    The approximate CDS pricing equation is:

    $$
    s = (1-R)\lambda
    $$

    This defines a **level set** in the $(R, \lambda)$ parameter space: for a given spread $s$, the set of admissible parameters is the curve $\lambda = s/(1-R)$.

    **Partial derivatives:**

    $$
    \frac{\partial s}{\partial \lambda} = 1 - R
    $$

    $$
    \frac{\partial s}{\partial R} = -\lambda
    $$

    **Proportionality (collinearity):**

    The gradient of $s$ with respect to $(\lambda, R)$ is:

    $$
    \nabla_{(\lambda, R)} s = (1-R, -\lambda)
    $$

    Along the constraint $s = (1-R)\lambda$, we have $\lambda = s/(1-R)$, so:

    $$
    \frac{\partial s / \partial R}{\partial s / \partial \lambda} = \frac{-\lambda}{1-R} = \frac{-s/(1-R)}{1-R} = \frac{-s}{(1-R)^2}
    $$

    This ratio is constant for a given spread, meaning the two partial derivatives are proportional along the constraint. In a least-squares calibration minimizing $\sum_i (s_i^{\text{model}} - s_i^{\text{market}})^2$, the Hessian matrix in the $(\lambda, R)$ directions is nearly singular because the sensitivity vectors are nearly collinear.

    Formally, consider the Jacobian of the pricing function $\mathbf{s}(\lambda, R)$:

    $$
    J = \begin{pmatrix} \partial s_1/\partial \lambda & \partial s_1/\partial R \\ \vdots & \vdots \\ \partial s_n/\partial \lambda & \partial s_n/\partial R \end{pmatrix} = \begin{pmatrix} 1-R & -\lambda_1 \\ \vdots & \vdots \\ 1-R & -\lambda_n \end{pmatrix}
    $$

    If hazard rates are similar (e.g., flat term structure with $\lambda_i \approx \lambda$), the columns of $J$ are nearly proportional: column 2 $\approx -\lambda/(1-R) \times$ column 1. The matrix $J^T J$ (which determines the normal equations) is nearly singular, and its smallest eigenvalue is close to zero---this is the precise sense in which $R$ and $\lambda$ are "nearly collinear."

    **Additional data or constraints to break collinearity:**

    1. **Defaulted bond prices or recovery rate swaps:** These provide direct information about $R$ independently of $\lambda$, breaking the degeneracy.

    2. **Equity tranche prices:** In portfolio credit models, equity tranche prices are sensitive to the distribution of losses (not just expected loss), providing information that distinguishes $R$ from $\lambda$.

    3. **Multiple seniority instruments:** Senior and subordinated CDS on the same issuer have different effective recovery rates, providing two equations with different $R$ values.

    4. **Cross-sectional constraints:** Fixing $R$ across issuers in the same industry (e.g., $R = 40\%$ for all senior unsecured) and calibrating only $\lambda$ is the most common practical approach.

---

**Exercise 4.** A practitioner fixes $R = 40\%$ for all issuers in a calibration exercise. Discuss the advantages and disadvantages of this approach from an identifiability perspective. Under what circumstances might fixing recovery lead to economically misleading hazard rates?

??? success "Solution to Exercise 4"
    **The practice:** Fixing $R = 40\%$ for all issuers and calibrating only $\lambda$ from CDS spreads.

    **Advantages from an identifiability perspective:**

    1. **Eliminates the $R$-$\lambda$ degeneracy:** With $R$ fixed, the calibration equation $s = (1-R)\lambda$ has a unique solution $\lambda = s/(1-R)$. The inverse problem becomes well-posed, with each CDS spread determining exactly one hazard rate.

    2. **Stability:** Since $\lambda$ is a simple function of the observable spread, small changes in $s$ produce proportionally small changes in $\lambda$ (no amplification from the trade-off).

    3. **Consistency across issuers:** A common recovery rate makes hazard rates comparable across issuers. If issuer A has $s_A = 100$ bp and issuer B has $s_B = 200$ bp, their hazard rate ratio is exactly 2, reflecting the relative credit quality without distortion from recovery assumptions.

    4. **Industry convention:** $R = 40\%$ is the ISDA standard for senior unsecured obligations, ensuring consistency across market participants.

    **Disadvantages:**

    1. **Model misspecification:** Actual recovery rates vary significantly across issuers, industries, and seniority levels. Moody's data shows historical recoveries ranging from 10% (subordinated debt in distressed industries) to 80% (senior secured bank loans). Forcing $R = 40\%$ ignores this heterogeneity.

    2. **Biased hazard rates:** If the true recovery rate differs from 40%, the calibrated hazard rate absorbs the error. For an issuer with true $R = 60\%$:

        - True hazard rate: $\lambda_{\text{true}} = s/(1-0.60) = s/0.40$
        - Calibrated hazard rate: $\lambda_{\text{calib}} = s/(1-0.40) = s/0.60$
        - Ratio: $\lambda_{\text{calib}}/\lambda_{\text{true}} = 0.40/0.60 = 0.67$

        The calibrated hazard rate understates the true default intensity by 33%.

    3. **Misleading economic interpretation:** The hazard rate is interpreted as the instantaneous default probability. If $R$ is misspecified, $\lambda$ no longer reflects the true default likelihood. This can mislead risk managers who use $\lambda$ for credit scoring, limit setting, or portfolio construction.

    **Circumstances where fixing $R$ leads to misleading hazard rates:**

    - **Secured vs. unsecured debt:** A secured lender with expected $R = 70\%$ and an unsecured lender with expected $R = 30\%$ on the same borrower would have very different CDS spreads. Calibrating both with $R = 40\%$ produces hazard rates that incorrectly suggest different default probabilities for the same entity.

    - **Distressed issuers:** Near default, recovery rate uncertainty is highest. Market-implied recovery rates (from recovery rate swaps or distressed bond prices) can be 20% or 60%, far from the standard 40%.

    - **Cross-sector comparisons:** Financial institutions typically have lower recovery rates than industrial firms. Using $R = 40\%$ for both makes financials appear less risky (lower $\lambda$) than they truly are.

---

**Exercise 5.** Explain how smoothness constraints on the hazard rate curve (e.g., penalizing $\sum_i (\lambda_{i+1} - \lambda_i)^2$) help mitigate identifiability issues in sequential bootstrapping. What trade-off does the modeler face between fitting accuracy and parameter stability?

??? success "Solution to Exercise 5"
    **Smoothness constraints on the hazard rate curve:**

    A typical smoothness penalty takes the form:

    $$
    \mathcal{P}(\boldsymbol{\lambda}) = \alpha \sum_{i=1}^{n-1} (\lambda_{i+1} - \lambda_i)^2
    $$

    where $\alpha > 0$ is the regularization parameter. The calibration objective becomes:

    $$
    \min_{\boldsymbol{\lambda}} \sum_{i=1}^{n} \left(s_i^{\text{model}} - s_i^{\text{market}}\right)^2 + \alpha \sum_{i=1}^{n-1} (\lambda_{i+1} - \lambda_i)^2
    $$

    **How smoothness constraints mitigate identifiability issues:**

    1. **Regularization of the inverse problem:** In sequential bootstrapping, each hazard rate is determined by a single CDS spread. If that spread is noisy, the hazard rate inherits (and amplifies) the noise. The smoothness penalty couples adjacent hazard rates, so noise in one spread is distributed across neighboring intervals rather than concentrated in one parameter.

    2. **Reduction of effective degrees of freedom:** The penalty term reduces the model's effective dimensionality. Without regularization, $n$ CDS spreads determine $n$ independent hazard rates. With strong regularization, the hazard rate curve is forced to be nearly flat, effectively reducing to 1--2 degrees of freedom. This prevents overfitting to noisy data.

    3. **Prevention of negative hazard rates:** When CDS spreads are inverted, sequential bootstrapping can produce negative marginal hazard rates. The smoothness penalty discourages large drops between adjacent hazard rates, making negative values less likely (though not impossible without an explicit constraint).

    4. **Stability under perturbation:** A small change in one CDS spread now affects all hazard rates (through the coupling), but the effect on each individual rate is small. The condition number of the inverse problem is reduced.

    **The trade-off between fitting accuracy and parameter stability:**

    - **Small $\alpha$:** The penalty is weak, so the calibration closely fits all CDS spreads ($s_i^{\text{model}} \approx s_i^{\text{market}}$). However, the hazard rate curve may oscillate wildly, especially if spreads are noisy. Parameters are accurate (low bias) but unstable (high variance).

    - **Large $\alpha$:** The penalty dominates, forcing a smooth (nearly flat) hazard rate curve. CDS pricing errors increase because the model cannot capture genuine term structure features. Parameters are stable (low variance) but biased---legitimate curvature in the hazard rate term structure is suppressed.

    - **Optimal $\alpha$:** Balances bias and variance. Common selection methods include cross-validation (hold out one CDS maturity, calibrate to the rest, measure prediction error) or the L-curve method (plot fitting error vs. penalty, choose the "elbow").

    This is a classic **bias-variance trade-off** from regularization theory (Tikhonov regularization), applied to the credit calibration setting.

---

**Exercise 6.** In illiquid credit markets, CDS quotes may have wide bid-ask spreads (e.g., 20 bp). Explain how this uncertainty propagates through the bootstrapping algorithm. If the 3-year CDS spread is known only to lie in $[80, 100]$ bp, estimate the range of implied hazard rates for the $(1\text{Y}, 3\text{Y}]$ period, assuming $R = 40\%$ and a previously calibrated $\lambda_1 = 100$ bp.

??? success "Solution to Exercise 6"
    **Propagation of uncertainty through bootstrapping:**

    In sequential bootstrapping, uncertainty in each CDS spread propagates forward and accumulates:

    - **Step 1:** $\lambda_1$ is determined by the 1-year spread alone. If $s_1$ has uncertainty $\pm \delta s_1$, then $\lambda_1$ has uncertainty $\pm \delta s_1/(1-R)$.

    - **Step 2:** $\lambda_2$ depends on both the 3-year spread $s_2$ and the previously calibrated $\lambda_1$. Uncertainty in $\lambda_1$ propagates into $\lambda_2$, *in addition to* the direct uncertainty from $s_2$. The marginal hazard rate $\lambda_2$ absorbs both sources of error.

    - **Step $i$:** $\lambda_i$ accumulates uncertainty from all previous steps plus the direct uncertainty from $s_i$. Later nodes have progressively larger error bars.

    For wide bid-ask spreads (e.g., 20 bp), the uncertainty at each node is approximately $\delta \lambda_i \sim 20/(1-R) \approx 33$ bp. For marginal periods, the amplification factor can be much larger (as shown in Exercise 2).

    **Estimation for the $(1\text{Y}, 3\text{Y}]$ period:**

    **Given:** $s_3 \in [80, 100]$ bp, $R = 40\%$, $\lambda_1 = 100$ bp = 1.00%.

    The 3-year CDS spread reflects the average intensity over $[0, 3]$. Using the simplified relationship for piecewise-constant intensity:

    $$
    s_3 \approx (1-R) \cdot \bar{\lambda}_{[0,3]}
    $$

    where:

    $$
    \bar{\lambda}_{[0,3]} = \frac{1 \cdot \lambda_1 + 2 \cdot \lambda_2}{3}
    $$

    Solving for $\lambda_2$:

    $$
    \lambda_2 = \frac{3 \cdot s_3/(1-R) - \lambda_1}{2}
    $$

    **Lower bound** ($s_3 = 80$ bp):

    $$
    \lambda_2^{\min} = \frac{3 \times 0.0080/0.60 - 0.0100}{2} = \frac{3 \times 0.01333 - 0.0100}{2} = \frac{0.04000 - 0.0100}{2} = \frac{0.0300}{2} = 1.50\% = 150 \text{ bp}
    $$

    **Upper bound** ($s_3 = 100$ bp):

    $$
    \lambda_2^{\max} = \frac{3 \times 0.0100/0.60 - 0.0100}{2} = \frac{3 \times 0.01667 - 0.0100}{2} = \frac{0.05000 - 0.0100}{2} = \frac{0.0400}{2} = 2.00\% = 200 \text{ bp}
    $$

    **Result:** $\lambda_2 \in [150, 200]$ bp.

    The 20 bp uncertainty in the 3-year CDS spread translates to a 50 bp uncertainty in the marginal hazard rate---an amplification factor of 2.5. This amplification arises because the marginal period $(1, 3]$ is 2 years long, but $\lambda_2$ must absorb all the difference between the 3-year average and the fixed $\lambda_1$, creating a leverage effect.

    In practice, this means that for illiquid names, bootstrapped hazard rates in marginal periods can be highly unreliable. Risk managers should report confidence intervals alongside point estimates, and downstream calculations (CVA, hedging ratios) should incorporate parameter uncertainty through sensitivity analysis or Bayesian methods.
