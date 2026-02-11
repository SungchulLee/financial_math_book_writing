# Value-at-Risk (VaR)

**Value-at-Risk (VaR)** is the most widely used market risk measure in finance. It summarizes potential losses over a fixed horizon at a given confidence level in a single number.

---

## Definition

Let $L$ denote the (random) loss of a portfolio over a given horizon. For a confidence level $\alpha \in (0,1)$, the Value-at-Risk is defined as the **$\alpha$-quantile** of the loss distribution:

$$
\text{VaR}_{\alpha}(L) = \inf\{x \in \mathbb{R} : F_L(x) \ge \alpha\} = F_L^{-1}(\alpha)
$$

where $F_L(x) = \mathbb{P}(L \le x)$ is the cumulative distribution function of $L$.

**Sign convention:** We adopt the loss convention where $L > 0$ represents a loss. Some texts use the profit convention where $L < 0$ represents a loss, leading to $\text{VaR}_\alpha = -F_L^{-1}(1-\alpha)$.

---

## Interpretation

A statement such as:

> "The one-day 99% VaR is \$10 million"

means that, under the model:

- With probability 99%, losses will not exceed \$10 million over one day
- Equivalently, losses exceed \$10 million with probability at most 1%

VaR answers the question: *"What is the maximum loss at confidence level $\alpha$?"*

---

## Parametric VaR Under Normality

If portfolio returns $R \sim N(\mu, \sigma^2)$ over horizon $\Delta t$, the loss $L = -R$ satisfies:

$$
\text{VaR}_\alpha = -\mu + \sigma \Phi^{-1}(\alpha)
$$

where $\Phi^{-1}$ is the standard normal quantile function.

**Example:** For $\alpha = 0.99$, we have $\Phi^{-1}(0.99) \approx 2.326$, so:

$$
\text{VaR}_{0.99} \approx -\mu + 2.326\sigma
$$

For daily returns with $\mu \approx 0$, this simplifies to $\text{VaR}_{0.99} \approx 2.326\sigma$.

---

## VaR Estimation Methods

### Historical Simulation

Order historical losses $L_{(1)} \le L_{(2)} \le \cdots \le L_{(n)}$ and estimate:

$$
\widehat{\text{VaR}}_\alpha = L_{(\lceil n\alpha \rceil)}
$$

**Advantages:** Model-free, captures fat tails if present in data.

**Disadvantages:** Requires sufficient historical data, assumes stationarity.

### Variance-Covariance (Parametric) Method

Assume returns follow a multivariate normal distribution:

$$
\mathbf{R} \sim N(\boldsymbol{\mu}, \boldsymbol{\Sigma})
$$

For portfolio weights $\mathbf{w}$, the portfolio variance is $\sigma_P^2 = \mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}$, giving:

$$
\text{VaR}_\alpha = -\mathbf{w}^\top \boldsymbol{\mu} + \sqrt{\mathbf{w}^\top \boldsymbol{\Sigma} \mathbf{w}} \cdot \Phi^{-1}(\alpha)
$$

**Advantages:** Computationally efficient, analytically tractable.

**Disadvantages:** Normality assumption often violated, underestimates tail risk.

### Monte Carlo Simulation

1. Specify a model for risk factors (returns, rates, volatilities)
2. Simulate $N$ scenarios of portfolio value
3. Compute losses and take the empirical $\alpha$-quantile

**Advantages:** Flexible, handles nonlinearities and path-dependence.

**Disadvantages:** Computationally intensive, model-dependent.

---

## Scaling VaR Across Horizons

Under the assumption of i.i.d. returns, VaR scales with the square root of time:

$$
\text{VaR}_\alpha(h \text{ days}) \approx \sqrt{h} \cdot \text{VaR}_\alpha(1 \text{ day})
$$

This **square-root-of-time rule** is exact for normally distributed returns but only approximate otherwise. It tends to underestimate multi-day VaR when returns exhibit volatility clustering or fat tails.

---

## VaR Is Not Subadditive: A Counterexample

A critical limitation of VaR is that it can violate **subadditivity**:

$$
\text{VaR}_\alpha(L_1 + L_2) \le \text{VaR}_\alpha(L_1) + \text{VaR}_\alpha(L_2) \quad \text{(may fail)}
$$

**Counterexample:** Consider two bonds, each defaulting independently with probability 4%. At the 95% confidence level:

- **Bond 1 alone:** $\text{VaR}_{0.95}(L_1) = 0$ (95th percentile is no default)
- **Bond 2 alone:** $\text{VaR}_{0.95}(L_2) = 0$
- **Portfolio:** $\mathbb{P}(\text{at least one default}) = 1 - 0.96^2 = 7.84\% > 5\%$

Thus, $\text{VaR}_{0.95}(L_1 + L_2) > 0$ even though $\text{VaR}_{0.95}(L_1) + \text{VaR}_{0.95}(L_2) = 0$.

This violates the diversification principle: combining positions can *increase* measured VaR.

---

## Elicitability of VaR

A risk measure $\rho$ is **elicitable** if there exists a scoring function $S(x, y)$ such that:

$$
\rho(L) = \arg\min_x \mathbb{E}[S(x, L)]
$$

**VaR is elicitable.** The scoring function for the $\alpha$-quantile is:

$$
S(x, L) = (\mathbf{1}_{L \le x} - \alpha)(x - L)
$$

This is the **pinball loss** (or quantile loss) function, which is asymmetric around the quantile.

**Implications for backtesting:**
- Elicitability enables comparative backtesting via scoring rules
- One can assess which of two VaR models performs better by comparing average scores
- This property is valuable for model selection and validation

---

## Regulatory Use of VaR

VaR became the standard regulatory risk measure under the **1996 Market Risk Amendment** to Basel I:

- Banks required to hold capital against market risk
- Internal models approach: capital = $k \times \text{VaR}_{0.99}^{10\text{-day}}$ where $k \ge 3$
- Multiplier $k$ increases with backtesting failures

**Basel III/IV transition:** Regulators now favor Expected Shortfall (ES) over VaR due to VaR's theoretical limitations, particularly the failure of subadditivity.

---

## Strengths and Limitations

**Strengths:**

- Intuitive and easy to communicate to non-specialists
- Single number summarizes tail risk
- Widely adopted by regulators and industry
- Elicitable, enabling proper backtesting

**Limitations:**

- Ignores the magnitude of losses beyond the quantile (tail blindness)
- Not subadditive: can penalize diversification
- Sensitive to distributional assumptions
- May encourage manipulation (hiding risk just beyond the VaR threshold)

---

## Key Takeaways

- VaR measures the $\alpha$-quantile of the loss distribution
- It is simple and widely used but theoretically incomplete
- VaR fails subadditivity, violating the diversification principle
- VaR is elicitable, unlike ES, which affects backtesting methodology
- Its limitations motivate coherent alternatives like Expected Shortfall

---

## Further Reading

- Jorion, P., *Value at Risk: The New Benchmark for Managing Financial Risk*
- McNeil, A., Frey, R., & Embrechts, P., *Quantitative Risk Management*
- Artzner, P., Delbaen, F., Eber, J.-M., & Heath, D. (1999), "Coherent Measures of Risk"
- Gneiting, T. (2011), "Making and Evaluating Point Forecasts" (elicitability)
