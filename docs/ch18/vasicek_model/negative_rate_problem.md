# The Negative Rate Problem

The Vasicek model allows the short rate $r_t$ to take any real value because the driving noise is Gaussian and the diffusion coefficient is constant. Since $r_t \mid r_0 \sim \mathcal{N}(\mu(t), v^2(t))$ with full support on $(-\infty, +\infty)$, there is always a strictly positive probability that rates become negative. Before the 2010s this was considered a serious theoretical deficiency; after the introduction of negative policy rates in Europe and Japan, it became a feature that the model captures naturally. This section quantifies the probability of negative rates, examines its consequences for bond pricing, and discusses practical remedies.

---

## Probability of negative rates

### Exact formula

Recall (see [§ Explicit solution and distribution](explicit_solution_and_distribution.md)) the conditional Gaussian distribution $r_t \mid r_0 \sim \mathcal{N}(\mu(t), v^2(t))$. The probability of a negative rate at time $t$ is

$$
\boxed{\mathbb{P}(r_t < 0) = \Phi\!\left(-\frac{\mu(t)}{v(t)}\right)}
$$

where $\Phi$ is the standard normal CDF.

### Asymptotic probability

As $t \to \infty$, $\mu(t) \to \theta$ and $v(t) \to \sigma/\sqrt{2\kappa}$, so the stationary probability of negative rates is

$$
\mathbb{P}(r_\infty < 0) = \Phi\!\left(-\frac{\theta\sqrt{2\kappa}}{\sigma}\right)
$$

This depends on the **signal-to-noise ratio** $\theta\sqrt{2\kappa}/\sigma$: the higher the ratio, the less likely negative rates are.

---

## Numerical examples

### Example 1: Typical pre-crisis parameters

Parameters: $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.02$, $r_0 = 0.04$.

- Stationary standard deviation: $\sigma/\sqrt{2\kappa} = 0.02/\sqrt{0.6} = 0.02582$
- Signal-to-noise ratio: $0.05/0.02582 = 1.936$
- $\mathbb{P}(r_\infty < 0) = \Phi(-1.936) = 2.64\%$

At various horizons:

| Horizon $t$ | $\mu(t)$ | $v(t)$ | $\mathbb{P}(r_t < 0)$ |
|:-:|:-:|:-:|:-:|
| 1 year | 4.26% | 1.52% | 0.25% |
| 5 years | 4.89% | 2.42% | 2.17% |
| 10 years | 4.99% | 2.57% | 2.60% |
| Stationary | 5.00% | 2.58% | 2.64% |

The probability starts very small (the current rate is well above zero) and increases toward the stationary value.

### Example 2: Low-rate environment

Parameters: $\kappa = 0.1$, $\theta = 0.01$, $\sigma = 0.015$, $r_0 = 0.005$.

- Stationary standard deviation: $0.015/\sqrt{0.2} = 0.03354$
- Signal-to-noise ratio: $0.01/0.03354 = 0.298$
- $\mathbb{P}(r_\infty < 0) = \Phi(-0.298) = 38.3\%$

In a low-rate, low-mean-reversion environment, the model predicts that rates are negative more than a third of the time in steady state.

---

## Consequences for bond pricing

### Bond prices exceeding par

When $r_t < 0$, the money market account $B_t = e^{\int_0^t r_s\,ds}$ decreases: lending at a negative rate means paying the borrower. In terms of bond pricing, the discount factor satisfies

$$
P(t,T) = \mathbb{E}^{\mathbb{Q}}_t\!\left[e^{-\int_t^T r_s\,ds}\right]
$$

If the integrated short rate $\int_t^T r_s\,ds$ is negative with sufficient probability, the expectation can exceed $1$, meaning $P(t,T) > 1$. This implies a **negative yield**: $R(t,T) = -\ln P(t,T)/\tau < 0$.

In the Vasicek model, the yield is $R(t,T) = B(\tau)/\tau \cdot r_t - \ln A(\tau)/\tau$. When $r_t$ is sufficiently negative, $R(t,T) < 0$ and $P(t,T) > 1$.

### Impact on the yield curve

Negative short rates shift the entire yield curve downward. The long-run yield $R_\infty = \theta - \sigma^2/(2\kappa^2)$ can itself be negative if $\sigma^2/(2\kappa^2) > \theta$, which occurs when volatility is high relative to the mean-reversion level.

### Bond option pricing

Negative rates do not invalidate the bond option formulas (the ZCB call and put formulas remain valid for any value of $r_t$), but they can produce unexpected behavior:

- Forward bond prices $P(t,S)/P(t,T)$ can exceed $1$ even for $S > T$
- Caplet values for low strikes can become very small since the probability of rates exceeding the strike is diminished

---

## Historical context

### Pre-2008 view

Before the global financial crisis, negative nominal interest rates were considered impossible:

- Investors could hold physical cash at zero return
- The "zero lower bound" was a standard assumption in macroeconomics
- The Vasicek model's negative rate property was seen as a material deficiency
- The CIR model was often preferred specifically because it enforces $r_t \geq 0$

### Post-2012 reality

Several central banks adopted negative policy rates:

| Central Bank | Date | Rate |
|---|---|---|
| Denmark (DNB) | July 2012 | $-0.20\%$ |
| ECB | June 2014 | $-0.10\%$ |
| Switzerland (SNB) | December 2014 | $-0.75\%$ |
| Sweden (Riksbank) | February 2015 | $-0.10\%$ |
| Bank of Japan | January 2016 | $-0.10\%$ |

Government bond yields turned negative across much of Europe and Japan. At the peak in 2019, over \$17 trillion of debt carried negative yields.

In this environment, the Vasicek model's ability to produce negative rates became an advantage rather than a liability.

---

## Practical remedies and alternatives

### Shifted Vasicek model

Add a deterministic shift to ensure rates stay above a lower bound $\underline{r}$:

$$
r_t = \underline{r} + x_t, \qquad dx_t = \kappa(\theta' - x_t)\,dt + \sigma\,dW_t
$$

where $x_t$ follows the standard Vasicek dynamics. Since $x_t$ is Gaussian, $r_t$ can still go below $\underline{r}$, but setting $\underline{r}$ sufficiently negative (e.g., $-2\%$) reduces this probability to negligible levels.

### CIR model

Recall (see [§ CIR](../cir_model/bond_options.md)) that the square-root diffusion $\sigma\sqrt{r_t}$ enforces $r_t \geq 0$ under the Feller condition. CIR cannot reproduce empirically observed negative rates.

### Shifted log-normal models

Recall (see [§ Black-Karasinski](../black_karasinski/calibration_to_cap_volatilities.md)) that BK and shifted-Black specifications enforce $r_t > \underline{r}$ at the cost of analytical tractability.

### Absorbing or reflecting boundaries

One can modify the Vasicek model by imposing a boundary condition at $r = 0$ (either absorption or reflection). This destroys the Gaussian distribution and the closed-form bond pricing formulas, making it impractical for most applications.

---

## Quantifying the economic impact

### Expected time spent below zero

The fraction of time the Vasicek short rate spends below zero in steady state is $\Phi(-\theta\sqrt{2\kappa}/\sigma)$. For Example 1 above, this is 2.64%. Over a 30-year horizon, the rate is expected to be negative for approximately $0.8$ years.

### Bond price distortion

The effect of negative rates on bond prices can be quantified through the convexity correction. The Vasicek bond price is

$$
P(t,T) = \exp\!\left(-B(\tau)\,r_t + \ln A(\tau)\right)
$$

The term $\ln A(\tau)$ includes the effect $-\sigma^2 B(\tau)^2/(4\kappa)$, which arises partly from the possibility of negative rate paths increasing the discount factor above $1$. This convexity effect is of order $\sigma^2\tau^2$ for small $\tau$ and remains bounded as $\tau \to \infty$.

---

## Summary

The Gaussian distribution of the Vasicek short rate implies $\mathbb{P}(r_t < 0) = \Phi(-\mu(t)/v(t)) > 0$ for all parameter values. The probability is controlled by the signal-to-noise ratio $\theta\sqrt{2\kappa}/\sigma$ and increases with volatility and horizon. While historically viewed as a deficiency, the negative rate property became empirically relevant after 2012. The main practical remedies---shifted models, CIR, and log-normal specifications---each trade off analytical tractability against distributional constraints. For calibration to modern rate markets where negative rates are observed, the unmodified Vasicek model is a reasonable choice.

---

## Exercises

**Exercise 1.** For Vasicek parameters $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.025$, $r_0 = 0.04$, compute $\mathbb{P}(r_t < 0)$ at $t = 1, 5, 10$ years and in the stationary limit. How does the signal-to-noise ratio $\theta\sqrt{2\kappa}/\sigma$ compare with the pre-crisis example in the text?

??? success "Solution to Exercise 1"
    With $\kappa = 0.5$, $\theta = 0.06$, $\sigma = 0.025$, $r_0 = 0.04$.

    **Signal-to-noise ratio:**

    $$
    \frac{\theta\sqrt{2\kappa}}{\sigma} = \frac{0.06 \times \sqrt{1.0}}{0.025} = \frac{0.06}{0.025} = 2.400
    $$

    Compare with the pre-crisis example: $\theta\sqrt{2\kappa}/\sigma = 0.05\sqrt{0.6}/0.02 = 0.05 \times 0.7746/0.02 = 1.936$. The current ratio 2.400 is larger, indicating negative rates are less likely.

    **Stationary probability:**

    $$
    \mathbb{P}(r_\infty < 0) = \Phi(-2.400) = 0.0082 = 0.82\%
    $$

    **At $t = 1$:**

    $$
    \mu(1) = 0.06 + (0.04 - 0.06)e^{-0.5} = 0.06 - 0.02 \times 0.6065 = 0.04787
    $$

    $$
    v(1) = \frac{0.025}{\sqrt{1.0}}\sqrt{1 - e^{-1.0}} = 0.025\sqrt{0.6321} = 0.025 \times 0.7951 = 0.01988
    $$

    $$
    \mathbb{P}(r_1 < 0) = \Phi\!\left(\frac{-0.04787}{0.01988}\right) = \Phi(-2.408) = 0.0080
    $$

    **At $t = 5$:**

    $$
    \mu(5) = 0.06 - 0.02 \times e^{-2.5} = 0.06 - 0.00164 = 0.05836
    $$

    $$
    v(5) = 0.025\sqrt{1 - e^{-5}} = 0.025 \times 0.9966 = 0.02492
    $$

    $$
    \mathbb{P}(r_5 < 0) = \Phi\!\left(\frac{-0.05836}{0.02492}\right) = \Phi(-2.342) = 0.0096
    $$

    **At $t = 10$:**

    $$
    \mu(10) \approx 0.06, \quad v(10) \approx 0.025
    $$

    $$
    \mathbb{P}(r_{10} < 0) = \Phi(-0.06/0.025) = \Phi(-2.400) = 0.0082
    $$

    The probability increases from about 0.80% at $t = 1$ to 0.96% at $t = 5$, then settles to 0.82% in the stationary limit.

---

**Exercise 2.** Derive the stationary probability of negative rates $\mathbb{P}(r_\infty < 0) = \Phi(-\theta\sqrt{2\kappa}/\sigma)$ from the stationary distribution $r_\infty \sim \mathcal{N}(\theta, \sigma^2/(2\kappa))$. For what value of $\sigma$ does this probability equal exactly 5% when $\kappa = 0.3$ and $\theta = 0.05$?

??? success "Solution to Exercise 2"
    The stationary distribution is $r_\infty \sim \mathcal{N}(\theta, \sigma^2/(2\kappa))$. The probability of a negative rate is:

    $$
    \mathbb{P}(r_\infty < 0) = \mathbb{P}\!\left(\frac{r_\infty - \theta}{\sigma/\sqrt{2\kappa}} < \frac{0 - \theta}{\sigma/\sqrt{2\kappa}}\right) = \Phi\!\left(-\frac{\theta}{\sigma/\sqrt{2\kappa}}\right) = \Phi\!\left(-\frac{\theta\sqrt{2\kappa}}{\sigma}\right)
    $$

    This confirms $\mathbb{P}(r_\infty < 0) = \Phi(-\theta\sqrt{2\kappa}/\sigma)$.

    For this probability to equal exactly 5% with $\kappa = 0.3$ and $\theta = 0.05$:

    $$
    \Phi\!\left(-\frac{0.05\sqrt{0.6}}{\sigma}\right) = 0.05
    $$

    Since $\Phi(-1.645) = 0.05$:

    $$
    \frac{0.05\sqrt{0.6}}{\sigma} = 1.645 \quad \Longrightarrow \quad \sigma = \frac{0.05\sqrt{0.6}}{1.645} = \frac{0.05 \times 0.7746}{1.645} = \frac{0.03873}{1.645} = 0.02354
    $$

    So $\sigma \approx 2.35\%$ gives exactly a 5% stationary probability of negative rates.

---

**Exercise 3.** In a low-rate environment with $\kappa = 0.1$, $\theta = 0.01$, $\sigma = 0.015$, $r_0 = 0.005$, the text reports $\mathbb{P}(r_\infty < 0) = 38.3\%$. Verify this calculation. Then find the value of $\kappa$ (holding $\theta$ and $\sigma$ fixed) that would reduce the stationary negative-rate probability to 5%.

??? success "Solution to Exercise 3"
    **Verification.** With $\kappa = 0.1$, $\theta = 0.01$, $\sigma = 0.015$:

    $$
    \frac{\theta\sqrt{2\kappa}}{\sigma} = \frac{0.01\sqrt{0.2}}{0.015} = \frac{0.01 \times 0.4472}{0.015} = \frac{0.004472}{0.015} = 0.2981
    $$

    $$
    \mathbb{P}(r_\infty < 0) = \Phi(-0.2981) = 0.3828 \approx 38.3\%
    $$

    This confirms the text's calculation.

    **Finding $\kappa$ for 5% probability.** We need:

    $$
    \Phi\!\left(-\frac{\theta\sqrt{2\kappa}}{\sigma}\right) = 0.05 \quad \Longrightarrow \quad \frac{0.01\sqrt{2\kappa}}{0.015} = 1.645
    $$

    $$
    \sqrt{2\kappa} = \frac{1.645 \times 0.015}{0.01} = 2.4675
    $$

    $$
    2\kappa = 6.0886 \quad \Longrightarrow \quad \kappa = 3.044
    $$

    A mean-reversion speed of $\kappa \approx 3.04$ is needed---extremely fast mean reversion with a half-life of $\ln 2/3.04 \approx 0.23$ years. This is unrealistically high, reflecting the fact that in a low-rate environment ($\theta = 1\%$) with moderate volatility ($\sigma = 1.5\%$), only very strong mean reversion can keep negative rates rare.

---

**Exercise 4.** When the short rate is negative, the zero-coupon bond price can exceed par ($P(t,T) > 1$). Using the Vasicek formula $P(t,T) = A(\tau)e^{-B(\tau)r_t}$, find the critical short rate $r^*(T)$ such that $P(0,T) = 1$ for $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.02$, and $T = 5$. Is $r^*(T)$ positive or negative?

??? success "Solution to Exercise 4"
    Setting $P(0,T) = 1$ with $P(0,T) = A(\tau)\,e^{-B(\tau)\,r_0}$:

    $$
    A(\tau)\,e^{-B(\tau)\,r_0} = 1 \quad \Longrightarrow \quad r_0 = r^*(T) = \frac{\ln A(\tau)}{B(\tau)}
    $$

    Wait---$P(0,T) = 1$ means $\ln A(\tau) - B(\tau)\,r^* = 0$, so:

    $$
    r^*(T) = \frac{\ln A(\tau)}{B(\tau)}
    $$

    For $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.02$, $T = 5$:

    $$
    B(5) = \frac{1 - e^{-1.5}}{0.3} = \frac{1 - 0.2231}{0.3} = 2.590
    $$

    $$
    \ln A(5) = \left(0.05 - \frac{0.0004}{0.18}\right)(2.590 - 5) - \frac{0.0004}{1.2} \times 2.590^2
    $$

    $$
    = (0.05 - 0.002222)(-2.410) - 0.000333 \times 6.708
    $$

    $$
    = 0.04778 \times (-2.410) - 0.002236 = -0.11515 - 0.002236 = -0.11738
    $$

    $$
    r^*(5) = \frac{-0.11738}{2.590} = -0.04532
    $$

    The critical rate is $r^* \approx -4.53\%$, which is **negative**. This makes sense: the bond price $P(0,T)$ exceeds 1 only when the current short rate is sufficiently negative (below $-4.53\%$), pulling down the integrated discount factor. For any $r_0 > -4.53\%$, the 5-year bond trades below par.

---

**Exercise 5.** The long-run yield is $R_\infty = \theta - \sigma^2/(2\kappa^2)$. Find the condition on $(\kappa, \theta, \sigma)$ under which $R_\infty < 0$. For $\kappa = 0.1$ and $\theta = 0.02$, what is the maximum volatility $\sigma$ for which $R_\infty$ remains positive?

??? success "Solution to Exercise 5"
    The condition for $R_\infty < 0$ is:

    $$
    \theta - \frac{\sigma^2}{2\kappa^2} < 0 \quad \Longleftrightarrow \quad \sigma^2 > 2\kappa^2\theta \quad \Longleftrightarrow \quad \sigma > \kappa\sqrt{2\theta}
    $$

    For $\kappa = 0.1$ and $\theta = 0.02$:

    $$
    \sigma_{\max} = \kappa\sqrt{2\theta} = 0.1\sqrt{0.04} = 0.1 \times 0.2 = 0.02
    $$

    For $\sigma < 0.02$ (i.e., $\sigma < 2\%$), $R_\infty > 0$. For $\sigma > 0.02$, $R_\infty < 0$.

    **Interpretation.** The convexity correction $\sigma^2/(2\kappa^2)$ grows quadratically in $\sigma$ and inverse-quadratically in $\kappa$. With slow mean reversion ($\kappa = 0.1$), rates wander extensively, producing large convexity effects. When the volatility exceeds 2%, the convexity correction overwhelms the long-run mean $\theta = 2\%$, and even the asymptotic yield turns negative. This is a parametric region where the model predicts that very long-term bonds would have negative yields even in steady state.

---

**Exercise 6.** In the shifted Vasicek model $r_t = \underline{r} + x_t$ where $x_t$ follows standard Vasicek dynamics, the probability of rates below $\underline{r}$ is the same as the probability of negative rates in the original model. If the original model has $\mathbb{P}(r_\infty < 0) = 2.64\%$, what is $\mathbb{P}(r_\infty < \underline{r})$ in the shifted model? Explain why the shift does not eliminate the tail risk but merely relocates it.

??? success "Solution to Exercise 6"
    In the shifted model $r_t = \underline{r} + x_t$, the variable $x_t$ follows standard Vasicek dynamics. Therefore:

    $$
    \mathbb{P}(r_\infty < \underline{r}) = \mathbb{P}(x_\infty < 0) = \mathbb{P}(r_\infty^{\text{original}} < 0) = 2.64\%
    $$

    The probability that $r_t$ falls below the shift $\underline{r}$ is **exactly the same** as the probability of negative rates in the unshifted model. The shift merely translates the entire distribution downward by $\underline{r}$.

    The shift **does not eliminate tail risk**; it **relocates** it. Instead of rates going below zero, they go below $\underline{r}$. If $\underline{r} = -2\%$, then rates below $-2\%$ occur with the same probability (2.64%) as negative rates occurred before. The distribution shape and its tails are unchanged---only the location parameter shifts.

    This is a fundamental limitation of the shifted approach: any Gaussian model has infinite support, so there is always a positive probability of reaching any threshold, no matter how far in the tail. The shift is pragmatically useful (making the problematic region economically less relevant) but does not solve the mathematical issue of unbounded support.

---

**Exercise 7.** Compare the Vasicek and CIR models in terms of their treatment of negative rates. For the CIR model $dr_t = \kappa(\theta - r_t)dt + \sigma\sqrt{r_t}\,dW_t$ with the Feller condition $2\kappa\theta \geq \sigma^2$, explain why $r_t \geq 0$ almost surely. What empirical scenarios favor the Vasicek model's ability to produce negative rates over CIR's non-negativity constraint?

??? success "Solution to Exercise 7"
    **CIR non-negativity.** In the CIR model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$, the diffusion coefficient is $\sigma\sqrt{r_t}$. As $r_t \to 0^+$:

    - The drift $\kappa(\theta - r_t) \to \kappa\theta > 0$ (pushes rates upward)
    - The diffusion $\sigma\sqrt{r_t} \to 0$ (noise vanishes)

    When $r_t$ approaches zero, the upward drift dominates while the noise disappears, preventing the process from crossing zero. Formally, the Feller condition $2\kappa\theta \geq \sigma^2$ ensures that the drift at zero is strong enough that $r_t = 0$ is an entrance boundary (never reached) rather than an attainable boundary. The comparison theorem for SDEs then guarantees $r_t > 0$ almost surely for all $t > 0$ if $r_0 > 0$.

    **When Vasicek's negative rates are preferred:**

    1. **Negative rate environments (post-2012):** When central banks set negative policy rates (ECB at $-0.50\%$, SNB at $-0.75\%$), the CIR model cannot calibrate to observed negative rates since $r_t \geq 0$ by construction. The Vasicek model naturally accommodates these observations.

    2. **Negative-yielding bonds:** Over \$17 trillion of bonds traded at negative yields in 2019. Pricing models must produce $P(t,T) > 1$ (negative yields), which requires the short rate to be negative with positive probability.

    3. **Analytical tractability of options:** The Vasicek model's Gaussian distribution leads to simpler bond option formulas than CIR, whose non-central chi-squared distribution requires more complex computations.

    4. **Calibration flexibility:** The Vasicek model can fit yield curves that imply negative forward rates at some horizons, which is common in low-rate regimes.
