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

---

**Exercise 2.** Explain why the non-decreasing condition on the weight function $\phi$ is necessary for the spectral risk measure to be coherent. What economic property does this condition encode (hint: aversion to tail risk)?

---

**Exercise 3.** The exponential spectral risk measure uses $\phi(u) = \frac{\gamma e^{\gamma u}}{e^\gamma - 1}$ for risk aversion parameter $\gamma > 0$. Compute $\phi(0)$ and $\phi(1)$ for $\gamma = 2$. Explain how increasing $\gamma$ shifts more weight toward the tail of the loss distribution.

---

**Exercise 4.** VaR at level $\alpha$ can be written as $\text{VaR}_\alpha(X) = \int_0^1 \text{VaR}_u(X)\,\delta(u - \alpha)\,du$, where $\delta$ is the Dirac delta. Explain why this weight function is not non-decreasing and hence VaR is not a spectral risk measure. What property of coherence does VaR consequently lack?

---

**Exercise 5.** For a portfolio loss $X \sim N(0, \sigma^2)$, compute the spectral risk measure with the exponential weight function from Exercise 3. Express the result as a function of $\sigma$ and $\gamma$. How does it compare to $\text{ES}_{0.95}$?

---

**Exercise 6.** Discuss the practical challenges of implementing spectral risk measures in a trading desk risk system. How would you estimate a spectral risk measure from historical P&L data? What are the advantages over simply using ES at a fixed confidence level?
