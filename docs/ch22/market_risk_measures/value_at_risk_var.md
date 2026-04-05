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

---

## Exercises

**Exercise 1.** A portfolio's daily P&L is normally distributed with mean $\mu = 0$ and standard deviation $\sigma = \$5\text{M}$. Compute the 1-day 99% VaR. Then compute the 10-day 99% VaR using the square-root-of-time rule.

??? success "Solution to Exercise 1"

    We are given $L \sim N(\mu, \sigma^2)$ with $\mu = 0$ and $\sigma = \$5\text{M}$.

    **1-day 99% VaR:**

    Using the parametric formula with $\mu = 0$:

    $$
    \text{VaR}_{0.99} = -\mu + \sigma \Phi^{-1}(0.99) = 0 + 5 \times 2.326 = \$11.63\text{M}
    $$

    **10-day 99% VaR using the square-root-of-time rule:**

    Under the assumption of i.i.d. normal returns, VaR scales with $\sqrt{h}$:

    $$
    \text{VaR}_{0.99}^{10\text{-day}} = \sqrt{10} \times \text{VaR}_{0.99}^{1\text{-day}} = \sqrt{10} \times 11.63 \approx 3.162 \times 11.63 \approx \$36.77\text{M}
    $$

    Alternatively, the 10-day loss has $\sigma_{10} = \sigma \sqrt{10} = 5\sqrt{10} \approx 15.81$, and:

    $$
    \text{VaR}_{0.99}^{10\text{-day}} = 15.81 \times 2.326 \approx \$36.77\text{M}
    $$

---

**Exercise 2.** Using historical simulation with 500 daily returns, explain how to compute the 99% VaR. How many observations fall in the tail beyond the VaR estimate? What is the main advantage of historical simulation over the parametric (normal) approach?

??? success "Solution to Exercise 2"

    With $n = 500$ daily returns and $\alpha = 0.99$:

    **Procedure:** Order the 500 historical losses from smallest to largest: $L_{(1)} \le L_{(2)} \le \cdots \le L_{(500)}$. The 99% VaR is estimated as:

    $$
    \widehat{\text{VaR}}_{0.99} = L_{(\lceil 500 \times 0.99 \rceil)} = L_{(495)}
    $$

    That is, the 495th largest loss in the ordered sample.

    **Number of observations in the tail beyond VaR:** There are $500 - 495 = 5$ observations that exceed the VaR estimate. This represents the $1\%$ tail: $500 \times (1 - 0.99) = 5$ observations.

    **Main advantage of historical simulation over the parametric approach:** Historical simulation is **model-free** (nonparametric). It does not assume any distributional form (such as normality) for the returns. It automatically captures empirical features present in the data, including fat tails, skewness, and complex dependence structures across assets. The parametric method, by contrast, typically assumes normality which understates tail risk when the true distribution has heavier tails.

---

**Exercise 3.** Construct a two-asset example demonstrating that VaR is not subadditive. Let $X_1$ and $X_2$ each have a 4% probability of losing \$100 and 96% probability of zero loss. If the losses are perfectly negatively correlated, compute $\text{VaR}_{0.95}(X_1)$, $\text{VaR}_{0.95}(X_2)$, and $\text{VaR}_{0.95}(X_1 + X_2)$.

??? success "Solution to Exercise 3"

    Let $X_1$ and $X_2$ each have:

    - $\mathbb{P}(X_i = 100) = 0.04$ (loss of \$100 with probability 4%)
    - $\mathbb{P}(X_i = 0) = 0.96$ (no loss with probability 96%)

    **Individual VaRs at 95% confidence:**

    For each $X_i$, we need the 0.95-quantile. Since $\mathbb{P}(X_i \le 0) = 0.96 \ge 0.95$, the 95th percentile is 0:

    $$
    \text{VaR}_{0.95}(X_1) = 0, \quad \text{VaR}_{0.95}(X_2) = 0
    $$

    **Now consider perfect negative correlation.** With two Bernoulli losses, "perfectly negatively correlated" means: when one defaults, the other does not, and vice versa. Since each has a 4% probability, we can construct:

    - $\mathbb{P}(X_1 = 100, X_2 = 0) = 0.04$
    - $\mathbb{P}(X_1 = 0, X_2 = 100) = 0.04$
    - $\mathbb{P}(X_1 = 0, X_2 = 0) = 0.92$

    (Note: $\mathbb{P}(X_1 = 100, X_2 = 100) = 0$ under perfect negative correlation.)

    The portfolio loss $X_1 + X_2$ takes values:

    - $X_1 + X_2 = 100$ with probability $0.04 + 0.04 = 0.08$
    - $X_1 + X_2 = 0$ with probability $0.92$

    Since $\mathbb{P}(X_1 + X_2 \le 0) = 0.92 < 0.95$, the 95th percentile of $X_1 + X_2$ is 100:

    $$
    \text{VaR}_{0.95}(X_1 + X_2) = 100
    $$

    **Subadditivity check:**

    $$
    \text{VaR}_{0.95}(X_1 + X_2) = 100 > 0 = \text{VaR}_{0.95}(X_1) + \text{VaR}_{0.95}(X_2)
    $$

    VaR is violated: the combined portfolio has a strictly higher VaR than the sum of individual VaRs, even under negative correlation. This demonstrates that VaR is not subadditive.

---

**Exercise 4.** A bank uses VaR as its primary risk measure. Explain the "cliff effect": positions can be structured to have VaR just below the threshold while having very large expected losses beyond VaR. Why does this make VaR a poor measure of tail risk?

??? success "Solution to Exercise 4"

    The **cliff effect** refers to the fact that VaR only reports a threshold (quantile) and is completely blind to the magnitude of losses beyond that threshold.

    **How it works:** A trader can structure positions so that:

    - Losses up to the VaR level are small, keeping VaR low
    - But conditional on exceeding VaR, losses are catastrophically large

    **Example:** Consider selling deep out-of-the-money options. Most of the time, the options expire worthless (small gains). The probability of a large loss may be, say, 0.5%, which is below the 1% tail. Thus VaR$_{0.99}$ reports a small or even negative number (a gain). However, if the tail event occurs, losses can be enormous.

    **Why this makes VaR a poor tail risk measure:**

    1. VaR ignores the **severity** of tail losses. Two portfolios can have identical VaR but vastly different expected losses in the tail.
    2. VaR can be **manipulated**: by pushing risk just beyond the VaR threshold, a trader can make the position appear safe while concentrating risk in the extreme tail.
    3. VaR provides **no incentive** to reduce the magnitude of tail losses, only their probability.
    4. This is precisely the limitation that Expected Shortfall (ES) addresses, since ES measures the average loss in the tail beyond VaR.

---

**Exercise 5.** Kupiec's POF (Proportion of Failures) test is used to backtest VaR. Over 250 trading days, a 99% VaR model produces 5 exceedances. Compute the expected number of exceedances and perform a binomial test at the 5% significance level. Is the model rejected?

??? success "Solution to Exercise 5"

    **Setup:** Over $n = 250$ trading days with a 99% VaR model ($p = 1 - \alpha = 0.01$), we observe $x = 5$ exceedances.

    **Expected number of exceedances:**

    $$
    \mathbb{E}[X] = np = 250 \times 0.01 = 2.5
    $$

    **Binomial test:** Under the null hypothesis that the model is correct, the number of exceedances $X \sim \text{Binomial}(250, 0.01)$.

    We compute the p-value $\mathbb{P}(X \ge 5)$ using the binomial distribution. First, compute $\mathbb{P}(X \le 4)$:

    $$
    \mathbb{P}(X = k) = \binom{250}{k} (0.01)^k (0.99)^{250-k}
    $$

    Computing each term:

    - $\mathbb{P}(X = 0) = (0.99)^{250} \approx 0.0811$
    - $\mathbb{P}(X = 1) = 250 \times 0.01 \times (0.99)^{249} \approx 0.2048$
    - $\mathbb{P}(X = 2) = \binom{250}{2} (0.01)^2 (0.99)^{248} \approx 0.2573$
    - $\mathbb{P}(X = 3) = \binom{250}{3} (0.01)^3 (0.99)^{247} \approx 0.2145$
    - $\mathbb{P}(X = 4) = \binom{250}{4} (0.01)^4 (0.99)^{246} \approx 0.1336$

    So $\mathbb{P}(X \le 4) \approx 0.8913$, and:

    $$
    \mathbb{P}(X \ge 5) = 1 - \mathbb{P}(X \le 4) \approx 1 - 0.8913 = 0.1087
    $$

    **Alternatively, using Kupiec's likelihood ratio test:**

    $$
    LR_{\text{POF}} = -2 \ln \frac{(1-p)^{n-x} p^x}{(1-\hat{p})^{n-x} \hat{p}^x}
    $$

    where $\hat{p} = 5/250 = 0.02$:

    $$
    LR_{\text{POF}} = -2 \left[(250-5)\ln\frac{0.99}{0.98} + 5\ln\frac{0.01}{0.02}\right]
    $$

    $$
    = -2 \left[245 \times 0.01005 + 5 \times (-0.6931)\right] = -2[2.462 - 3.466] = -2 \times (-1.004) = 2.008
    $$

    The critical value for $\chi^2(1)$ at the 5% significance level is 3.841.

    **Conclusion:** Since $LR_{\text{POF}} = 2.008 < 3.841$ (or equivalently, the p-value $\approx 0.109 > 0.05$), we **fail to reject** the null hypothesis at the 5% significance level. The model is not rejected, though 5 exceedances is somewhat elevated relative to the expected 2.5. Under the Basel traffic light system, 5 exceedances places the model in the **yellow zone**, triggering an increased capital multiplier.

---

**Exercise 6.** Compare VaR at the 99% level for three distributions with the same mean and variance: (a) normal, (b) Student-$t$ with 4 degrees of freedom, and (c) a mixture of two normals. Which distribution produces the highest VaR? What does this reveal about VaR's sensitivity to distributional assumptions?

??? success "Solution to Exercise 6"

    We compare $\text{VaR}_{0.99}$ for three distributions with mean $\mu = 0$ and variance $\sigma^2$.

    **(a) Normal distribution:** $L \sim N(0, \sigma^2)$

    $$
    \text{VaR}_{0.99}^{\text{Normal}} = \sigma \Phi^{-1}(0.99) = 2.326\sigma
    $$

    **(b) Student-$t$ with $\nu = 4$ degrees of freedom:**

    The Student-$t$ distribution with $\nu$ degrees of freedom has variance $\nu/(\nu-2)$. To match variance $\sigma^2$, we use $L = \sigma \sqrt{(\nu-2)/\nu} \cdot T$ where $T \sim t_\nu$. For $\nu = 4$:

    $$
    L = \sigma \sqrt{\frac{2}{4}} \cdot T = \frac{\sigma}{\sqrt{2}} T
    $$

    The 99th percentile of $t_4$ is $t_4^{-1}(0.99) \approx 3.747$, so:

    $$
    \text{VaR}_{0.99}^{t_4} = \frac{\sigma}{\sqrt{2}} \times 3.747 \approx 2.650\sigma
    $$

    **(c) Mixture of two normals:**

    Consider $L \sim 0.9 \cdot N(0, \sigma_1^2) + 0.1 \cdot N(0, \sigma_2^2)$ with the constraint $0.9\sigma_1^2 + 0.1\sigma_2^2 = \sigma^2$. Taking $\sigma_1 = 0.5\sigma$ and $\sigma_2 = \sqrt{(σ^2 - 0.9 \times 0.25\sigma^2)/0.1} = \sqrt{7.75}\,\sigma \approx 2.784\sigma$:

    The 99th percentile of the mixture is dominated by the heavy component. Using $\sigma_2 \approx 2.784\sigma$:

    $$
    \text{VaR}_{0.99}^{\text{mix}} \approx \sigma_2 \times \Phi^{-1}(0.99) \approx 2.784\sigma \times 2.326 \approx 6.48\sigma
    $$

    More precisely, the quantile of the mixture satisfies $0.9\,\Phi(x/\sigma_1) + 0.1\,\Phi(x/\sigma_2) = 0.99$. A numerical solution yields $\text{VaR}_{0.99}^{\text{mix}} \approx 4.5\sigma$ to $6.5\sigma$ depending on the exact parameter choice.

    **Ranking:** $\text{VaR}_{0.99}^{\text{Normal}} < \text{VaR}_{0.99}^{t_4} < \text{VaR}_{0.99}^{\text{mix}}$

    **Key insight:** VaR is highly sensitive to distributional assumptions. Distributions with heavier tails (Student-$t$, mixture of normals) produce substantially larger VaR than the normal distribution, even when all three share the same mean and variance. The normal assumption systematically underestimates tail risk. This underscores the danger of relying on the parametric (variance-covariance) method with a normality assumption, particularly at high confidence levels where the tail shape matters most.
