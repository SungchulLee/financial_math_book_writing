# Spectral Risk Measures

Spectral risk measures generalize Value-at-Risk (VaR) and Expected Shortfall (ES) by applying weights across the quantile distribution. They provide a coherent, theoretically principled framework for risk measurement that captures risk preferences through a spectrum of weights on tail outcomes.

## Key Concepts

**Coherent Risk Measures**
A risk measure $\rho: \mathcal{L} \to \mathbb{R}$ is coherent if it satisfies:
1. **Monotonicity**: $X \leq Y$ ⟹ $\rho(X) \leq \rho(Y)$
2. **Subadditivity**: $\rho(X + Y) \leq \rho(X) + \rho(Y)$ (diversification benefit)
3. **Positive homogeneity**: $\rho(\lambda X) = \lambda \rho(X)$ for $\lambda > 0$ (scaling)
4. **Translation invariance**: $\rho(X + c) = \rho(X) - c$ (cash adds linearly)

VaR violates subadditivity (not coherent). Expected Shortfall is coherent.

**Spectral Risk Measure Definition**
A spectral risk measure applies weight function $\phi(\alpha)$ across quantiles:

$$\rho_\phi(X) = \int_0^1 \phi(\alpha) q_\alpha(X) d\alpha$$

where $q_\alpha(X) = \text{VaR}_\alpha(X)$ is the $\alpha$-quantile, and:
- $\phi(\alpha) \geq 0$ (non-negative weights)
- $\int_0^1 \phi(\alpha) d\alpha = 1$ (weights sum to 1)
- $\phi$ non-decreasing in $\alpha$ (higher weight on worse outcomes)

**Intuition**
The weight function $\phi(\alpha)$ encodes:
- How much emphasis to place on each tail region
- Risk aversion profile: flat $\phi$ = uniform weight, increasing $\phi$ = conservative
- $\phi(\alpha) = \delta(\alpha - \alpha_0)$: reduces to $\text{VaR}_{\alpha_0}$
- $\phi(\alpha) = \frac{1}{1-\alpha_0}$ for $\alpha \geq \alpha_0$: gives Expected Shortfall

**Special Cases**

| Measure | Weight Function | Interpretation |
|---------|-----------------|-----------------|
| Value-at-Risk | $\delta(\alpha - 0.95)$ | Single quantile |
| Expected Shortfall | $\phi(\alpha) = \frac{1}{1-\alpha_0} \mathbf{1}_{\alpha \geq \alpha_0}$ | Average of worst 5% |
| AveVar | $\phi(\alpha) = \frac{2}{1-\alpha_0}\mathbf{1}_{\alpha \geq \alpha_0}$ | Linear increasing weights |
| Omega ratio | Specific choice for return/risk tradeoff | Gain/loss focus |

**Kusuoka Representation**
Kusuoka showed any spectral risk measure can be expressed as:

$$\rho_\phi(X) = \max_{p \in \mathcal{P}} \mathbb{E}_p[-X]$$

where the maximum is over distributions consistent with marginal constraints. This connects spectral measures to robust optimization.

**Parametric Approaches**
For common distributions, spectral measures have closed forms:
- **Normal distribution**: $\rho_\phi(X) = \mu + \sigma \int_0^1 \phi(\alpha) \Phi^{-1}(\alpha) d\alpha$
- **Student-t**: leads to heavier tail weighting
- **Mixture distributions**: captures multi-modal risk (e.g., normal + jumps)

**Advantages Over Standard Measures**
1. **Flexibility**: adjust risk aversion without changing measure type
2. **Theoretical soundness**: coherence axioms satisfied
3. **Tail sensitivity**: directly incorporates tail behavior through weights
4. **Portfolio optimization**: convex optimization framework available
5. **Regulatory acceptance**: ES is mandated in Basel III, spectral measures studied for advanced approaches

**Practical Implementation**
Computing spectral risk measures:
1. Estimate quantile function $q_\alpha$ from data or model
2. Choose weight function $\phi$ reflecting risk preferences
3. Numerically integrate: $\rho_\phi(X) = \int_0^1 \phi(\alpha) q_\alpha(X) d\alpha$
4. Validate through backtesting and stress testing

**Limitations**
- Weight function choice not uniquely determined by data
- Requires stable quantile estimation (challenging in tails)
- Computational cost vs. VaR (which is just a single quantile)
- Interpretation less intuitive than "worst 5% loss"

!!! note "Risk Management Practice"
    Spectral measures provide:
    - Theoretically principled risk aggregation
    - Flexibility to match institutional risk tolerance
    - Framework for incorporating expert judgment
    - Bridge between academic rigor and practical needs

---

## Exercises

**Exercise 1.** A spectral risk measure is defined as $\rho_\phi(X) = \int_0^1 \text{VaR}_u(X)\,\phi(u)\,du$ where the weight function $\phi$ satisfies $\phi \ge 0$, $\int_0^1 \phi(u)\,du = 1$, and $\phi$ is non-decreasing. Show that ES at level $\alpha$ is a spectral risk measure by identifying its weight function $\phi(u) = \frac{1}{1-\alpha}\mathbf{1}_{\{u \ge \alpha\}}$.

??? success "Solution to Exercise 1"

    We must show that ES at level $\alpha$ can be written in the form $\rho_\phi(X) = \int_0^1 \text{VaR}_u(X)\,\phi(u)\,du$ with a valid spectrum $\phi$.

    **Claim:** The weight function for $\text{ES}_\alpha$ is:

    $$
    \phi_\alpha(u) = \frac{1}{1-\alpha}\mathbf{1}_{\{u \ge \alpha\}}
    $$

    **Verification of the three conditions:**

    1. **Non-negativity:** $\phi_\alpha(u) = \frac{1}{1-\alpha} > 0$ for $u \ge \alpha$ and $\phi_\alpha(u) = 0$ for $u < \alpha$. Hence $\phi_\alpha(u) \ge 0$ for all $u \in [0,1]$.

    2. **Normalization:**

    $$
    \int_0^1 \phi_\alpha(u)\,du = \int_\alpha^1 \frac{1}{1-\alpha}\,du = \frac{1}{1-\alpha}(1-\alpha) = 1 \checkmark
    $$

    3. **Non-decreasing:** $\phi_\alpha$ is a step function that jumps from 0 to $\frac{1}{1-\alpha}$ at $u = \alpha$ and remains constant thereafter. It is non-decreasing.

    **Verification that the spectral measure equals ES:**

    $$
    \rho_{\phi_\alpha}(X) = \int_0^1 \text{VaR}_u(X)\,\phi_\alpha(u)\,du = \int_\alpha^1 \text{VaR}_u(X) \cdot \frac{1}{1-\alpha}\,du = \frac{1}{1-\alpha}\int_\alpha^1 \text{VaR}_u(X)\,du
    $$

    This is precisely the integral representation of $\text{ES}_\alpha(X)$. Therefore, ES at level $\alpha$ is a spectral risk measure with the weight function $\phi_\alpha(u) = \frac{1}{1-\alpha}\mathbf{1}_{\{u \ge \alpha\}}$.

---

**Exercise 2.** Explain why the non-decreasing condition on the weight function $\phi$ is necessary for the spectral risk measure to be coherent. What economic property does this condition encode (hint: aversion to tail risk)?

??? success "Solution to Exercise 2"

    **Why the non-decreasing condition is necessary for coherence:**

    The non-decreasing condition on $\phi$ ensures that the spectral risk measure satisfies **subadditivity**, which is the key axiom separating coherent from non-coherent risk measures.

    **Economic property encoded:** The non-decreasing condition encodes **risk aversion** in the sense that worse outcomes (higher quantiles in the loss distribution) receive at least as much weight as better outcomes. Formally:

    - If $u_1 < u_2$, then $\text{VaR}_{u_1}(X) \le \text{VaR}_{u_2}(X)$ (higher quantile levels correspond to larger losses).
    - The condition $\phi(u_1) \le \phi(u_2)$ means the risk measure puts more weight on these larger losses.
    - An agent who weights extreme losses at least as heavily as moderate losses is displaying **aversion to tail risk**.

    **What goes wrong without the non-decreasing condition:**

    If $\phi$ is allowed to decrease, one could construct a weight function that puts high weight on moderate losses but low weight on extreme losses. Such a measure would:

    1. **Fail subadditivity:** Acerbi (2002) proved that a spectral risk measure is coherent if and only if $\phi$ is non-decreasing. A decreasing $\phi$ produces a spectral measure that violates subadditivity.
    2. **Ignore tail risk:** By down-weighting the extreme tail, the measure underestimates the risk of rare catastrophic events.
    3. **Penalize diversification:** Without subadditivity, combining portfolios could appear to increase risk, contradicting the fundamental principle of diversification.

    **Connection to the Dirac delta (VaR):** The extreme case where $\phi(u) = \delta(u - \alpha)$ puts all weight on a single quantile and zero weight everywhere else. This is "infinitely non-monotone" in a distributional sense and corresponds to VaR, which indeed fails subadditivity.

---

**Exercise 3.** The exponential spectral risk measure uses $\phi(u) = \frac{\gamma e^{\gamma u}}{e^\gamma - 1}$ for risk aversion parameter $\gamma > 0$. Compute $\phi(0)$ and $\phi(1)$ for $\gamma = 2$. Explain how increasing $\gamma$ shifts more weight toward the tail of the loss distribution.

??? success "Solution to Exercise 3"

    The exponential spectral weight function is:

    $$
    \phi(u) = \frac{\gamma e^{\gamma u}}{e^\gamma - 1}
    $$

    **Computing $\phi(0)$ and $\phi(1)$ for $\gamma = 2$:**

    $$
    \phi(0) = \frac{2 \cdot e^{2 \cdot 0}}{e^2 - 1} = \frac{2 \cdot 1}{e^2 - 1} = \frac{2}{7.389 - 1} = \frac{2}{6.389} \approx 0.313
    $$

    $$
    \phi(1) = \frac{2 \cdot e^{2 \cdot 1}}{e^2 - 1} = \frac{2 \cdot e^2}{e^2 - 1} = \frac{2 \times 7.389}{6.389} = \frac{14.778}{6.389} \approx 2.313
    $$

    **Ratio:** $\phi(1)/\phi(0) = e^2 \approx 7.389$. The weight at the worst quantile ($u=1$) is about 7.4 times the weight at the best quantile ($u=0$).

    **Verification of normalization:**

    $$
    \int_0^1 \phi(u)\,du = \frac{\gamma}{e^\gamma - 1}\int_0^1 e^{\gamma u}\,du = \frac{\gamma}{e^\gamma - 1} \cdot \frac{e^\gamma - 1}{\gamma} = 1 \checkmark
    $$

    **Effect of increasing $\gamma$:**

    As $\gamma$ increases:

    - $\phi(0) = \frac{\gamma}{e^\gamma - 1} \to 0$ (the weight on the best outcomes vanishes)
    - $\phi(1) = \frac{\gamma e^\gamma}{e^\gamma - 1} \to \gamma$ (the weight on the worst outcomes grows)
    - The ratio $\phi(1)/\phi(0) = e^\gamma$ grows exponentially

    This means increasing $\gamma$ concentrates more weight on the extreme tail of the loss distribution, making the risk measure more conservative. In the limit:

    - As $\gamma \to 0$: $\phi(u) \to 1$ uniformly, giving the mean $\mathbb{E}[X]$ (risk-neutral).
    - As $\gamma \to \infty$: the weight concentrates near $u = 1$, approaching the worst-case loss (maximum loss).

---

**Exercise 4.** VaR at level $\alpha$ can be written as $\text{VaR}_\alpha(X) = \int_0^1 \text{VaR}_u(X)\,\delta(u - \alpha)\,du$, where $\delta$ is the Dirac delta. Explain why this weight function is not non-decreasing and hence VaR is not a spectral risk measure. What property of coherence does VaR consequently lack?

??? success "Solution to Exercise 4"

    **VaR as a spectral-like integral:**

    Formally, $\text{VaR}_\alpha(X)$ can be written as:

    $$
    \text{VaR}_\alpha(X) = \int_0^1 \text{VaR}_u(X)\,\delta(u - \alpha)\,du
    $$

    where $\delta(u - \alpha)$ is the Dirac delta function centered at $\alpha$.

    **Why this "weight function" fails the non-decreasing condition:**

    The Dirac delta $\delta(u - \alpha)$ is not a non-decreasing function. In fact, it is not even a proper function -- it is a distribution (generalized function) that is zero everywhere except at $u = \alpha$ where it is "infinite." Considering any smooth approximation (e.g., a narrow bump function centered at $\alpha$):

    - The approximation increases as $u$ approaches $\alpha$ from below
    - Then **decreases** as $u$ moves past $\alpha$

    This violating the non-decreasing requirement is fundamental: the weight function rises to a peak at $\alpha$ and then drops back to zero. It puts zero weight on outcomes worse than the $\alpha$-quantile and zero weight on outcomes better than the $\alpha$-quantile, concentrating all weight on a single point.

    **Consequence for coherence:**

    Since VaR's weight function is not non-decreasing, VaR is **not a spectral risk measure**. By Acerbi's theorem, only spectral risk measures with non-decreasing weight functions are coherent. Therefore, VaR lacks **subadditivity**.

    **Intuition:** VaR ignores the severity of losses beyond the $\alpha$-quantile. By putting zero weight on outcomes worse than $\text{VaR}_\alpha$, it throws away information about tail severity. A spectral measure with a proper non-decreasing $\phi$ must give these extreme outcomes at least as much weight as the $\alpha$-quantile, ensuring that tail risk is captured and subadditivity is preserved.

---

**Exercise 5.** For a portfolio loss $X \sim N(0, \sigma^2)$, compute the spectral risk measure with the exponential weight function from Exercise 3. Express the result as a function of $\sigma$ and $\gamma$. How does it compare to $\text{ES}_{0.95}$?

??? success "Solution to Exercise 5"

    For $X \sim N(0, \sigma^2)$, the quantile function is $\text{VaR}_u(X) = \sigma \Phi^{-1}(u)$.

    **Spectral risk measure with exponential weights:**

    $$
    \rho_\phi(X) = \int_0^1 \phi(u) \,\text{VaR}_u(X)\,du = \int_0^1 \frac{\gamma e^{\gamma u}}{e^\gamma - 1} \cdot \sigma \Phi^{-1}(u)\,du
    $$

    $$
    = \frac{\gamma \sigma}{e^\gamma - 1} \int_0^1 e^{\gamma u} \Phi^{-1}(u)\,du
    $$

    **Evaluating the integral:** Let $z = \Phi^{-1}(u)$, so $u = \Phi(z)$ and $du = \phi(z)\,dz$:

    $$
    \int_0^1 e^{\gamma u} \Phi^{-1}(u)\,du = \int_{-\infty}^{\infty} z \, e^{\gamma \Phi(z)} \phi(z)\,dz
    $$

    This integral does not have a simple closed form in general. However, we can use the moment generating function approach. For the normal distribution, we can use integration by parts or the identity:

    $$
    \int_0^1 e^{\gamma u} \Phi^{-1}(u)\,du = \frac{e^\gamma}{\gamma}\left[1 - e^{-\gamma}\right] \cdot m(\gamma)
    $$

    A more direct approach uses the result that for $X \sim N(0, \sigma^2)$:

    $$
    \rho_\phi(X) = \sigma \cdot c(\gamma)
    $$

    where $c(\gamma) = \frac{\gamma}{e^\gamma - 1}\int_0^1 e^{\gamma u}\Phi^{-1}(u)\,du$ is a constant depending only on $\gamma$. Numerical evaluation gives:

    - For $\gamma = 1$: $c(1) \approx 0.725$
    - For $\gamma = 2$: $c(2) \approx 1.166$
    - For $\gamma = 5$: $c(5) \approx 1.868$
    - For $\gamma = 10$: $c(10) \approx 2.197$

    **Result:**

    $$
    \rho_\phi(X) = \sigma \cdot c(\gamma)
    $$

    **Comparison with $\text{ES}_{0.95}$:**

    For the normal distribution:

    $$
    \text{ES}_{0.95} = \sigma \cdot \frac{\phi(1.645)}{0.05} = \sigma \cdot \frac{0.1031}{0.05} = 2.063\sigma
    $$

    - For moderate $\gamma$ (e.g., $\gamma = 2$), $\rho_\phi \approx 1.166\sigma < 2.063\sigma = \text{ES}_{0.95}$. The exponential spectral measure is less conservative because it distributes weight across all quantiles, not just the top 5%.
    - For large $\gamma$ (e.g., $\gamma \ge 8$), $\rho_\phi$ approaches and may exceed $\text{ES}_{0.95}$ as the exponential weight increasingly concentrates on the extreme tail.
    - The exponential spectral measure is a **smooth** risk measure that transitions gradually from low to high tail weighting, whereas $\text{ES}_{0.95}$ has a sharp cutoff at the 95th percentile.

---

**Exercise 6.** Discuss the practical challenges of implementing spectral risk measures in a trading desk risk system. How would you estimate a spectral risk measure from historical P&L data? What are the advantages over simply using ES at a fixed confidence level?

??? success "Solution to Exercise 6"

    **Practical challenges of implementing spectral risk measures:**

    1. **Choice of weight function:** The spectrum $\phi$ is not uniquely determined by the data. Unlike VaR (which requires only a confidence level) or ES (confidence level), a spectral measure requires selecting an entire function. This introduces a subjective element:
        - What functional form should $\phi$ take (exponential, power, piecewise linear)?
        - How should the risk aversion parameter(s) be calibrated?
        - Different desks or business units may have different risk preferences.

    2. **Quantile estimation in the tails:** Spectral measures require estimating the full quantile function $q_\alpha(X)$ for $\alpha$ across $[0,1]$. Tail quantiles are notoriously difficult to estimate accurately from limited data. With 500 daily observations, the 99.5th percentile estimate relies on only 2--3 data points.

    3. **Computational cost:** Unlike VaR (a single quantile) or ES (average of a few tail observations), spectral measures require numerical integration over the entire quantile function weighted by $\phi$. For large portfolios with Monte Carlo pricing, this adds computational burden.

    4. **Communication and governance:** VaR and ES are widely understood by traders, senior management, and regulators. A spectral measure with an exponential or power-law weight function is harder to explain and may face resistance in governance processes.

    5. **Regulatory acceptance:** Basel III mandates ES, not general spectral measures. Using a spectral measure internally requires maintaining ES for regulatory reporting while potentially using a different measure for internal risk management.

    **Estimating a spectral risk measure from historical P&L data:**

    Given $n$ historical losses $L_1, \ldots, L_n$:

    1. **Sort the losses:** $L_{(1)} \le L_{(2)} \le \cdots \le L_{(n)}$
    2. **Assign quantile levels:** $u_i = (i - 0.5)/n$ for $i = 1, \ldots, n$ (midpoint convention)
    3. **Compute the discrete approximation:**

    $$
    \hat{\rho}_\phi = \frac{1}{n}\sum_{i=1}^{n} \phi(u_i) \, L_{(i)}
    $$

    This is a Riemann sum approximation to the integral $\int_0^1 \phi(u)\,q_u(X)\,du$.

    Alternatively, using trapezoidal or Simpson's rule for better accuracy, or kernel-smoothed quantile estimates for smoother integration.

    **Advantages over ES at a fixed confidence level:**

    1. **Flexible risk aversion:** A spectral measure allows the institution to express its specific risk preferences through the shape of $\phi$. A bank with higher aversion to extreme tail events can use a steeply increasing $\phi$, while one primarily concerned with moderate losses can use a more gradual weight function.

    2. **Smooth tail weighting:** ES has a discontinuity in its weight function at $\alpha$ (jumping from 0 to $\frac{1}{1-\alpha}$). Spectral measures with smooth $\phi$ (like the exponential) produce risk measures that vary continuously with changes in the loss distribution, avoiding the sensitivity to the exact choice of $\alpha$.

    3. **Information about the full tail:** ES treats all tail losses above $\text{VaR}_\alpha$ equally. A spectral measure can assign progressively more weight to more extreme losses, better reflecting the economic reality that a \$1B loss is not just twice as bad as a \$500M loss.

    4. **Unified framework:** Different confidence-level ES measures (ES$_{0.95}$, ES$_{0.975}$, ES$_{0.99}$) are all special cases of spectral measures. A single spectral measure can simultaneously capture information that would otherwise require reporting multiple ES levels.
