# The Negative Rate Problem

The Vasicek model allows the short rate $r_t$ to take any real value because the driving noise is Gaussian and the diffusion coefficient is constant. Since $r_t \mid r_0 \sim \mathcal{N}(\mu(t), v^2(t))$ with full support on $(-\infty, +\infty)$, there is always a strictly positive probability that rates become negative. Before the 2010s this was considered a serious theoretical deficiency; after the introduction of negative policy rates in Europe and Japan, it became a feature that the model captures naturally. This section quantifies the probability of negative rates, examines its consequences for bond pricing, and discusses practical remedies.

---

## Probability of negative rates

### Exact formula

Recall the conditional distribution under the risk-neutral measure:

$$
r_t \mid r_0 \sim \mathcal{N}\!\left(\mu(t),\, v^2(t)\right)
$$

where

$$
\mu(t) = \theta + (r_0 - \theta)\,e^{-\kappa t}, \qquad v^2(t) = \frac{\sigma^2}{2\kappa}\!\left(1 - e^{-2\kappa t}\right)
$$

The probability of a negative rate at time $t$ is

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

The Cox-Ingersoll-Ross model

$$
dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t
$$

ensures $r_t \geq 0$ when the Feller condition $2\kappa\theta \geq \sigma^2$ holds. The square-root diffusion vanishes at $r_t = 0$, creating a natural reflecting boundary. However, CIR cannot produce negative rates when they are empirically observed.

### Shifted log-normal models

Black-Karasinski and shifted Black models ensure $r_t > \underline{r}$ by modeling $\ln(r_t - \underline{r})$ as a diffusion. These models sacrifice analytical tractability.

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

---

**Exercise 2.** Derive the stationary probability of negative rates $\mathbb{P}(r_\infty < 0) = \Phi(-\theta\sqrt{2\kappa}/\sigma)$ from the stationary distribution $r_\infty \sim \mathcal{N}(\theta, \sigma^2/(2\kappa))$. For what value of $\sigma$ does this probability equal exactly 5% when $\kappa = 0.3$ and $\theta = 0.05$?

---

**Exercise 3.** In a low-rate environment with $\kappa = 0.1$, $\theta = 0.01$, $\sigma = 0.015$, $r_0 = 0.005$, the text reports $\mathbb{P}(r_\infty < 0) = 38.3\%$. Verify this calculation. Then find the value of $\kappa$ (holding $\theta$ and $\sigma$ fixed) that would reduce the stationary negative-rate probability to 5%.

---

**Exercise 4.** When the short rate is negative, the zero-coupon bond price can exceed par ($P(t,T) > 1$). Using the Vasicek formula $P(t,T) = A(\tau)e^{-B(\tau)r_t}$, find the critical short rate $r^*(T)$ such that $P(0,T) = 1$ for $\kappa = 0.3$, $\theta = 0.05$, $\sigma = 0.02$, and $T = 5$. Is $r^*(T)$ positive or negative?

---

**Exercise 5.** The long-run yield is $R_\infty = \theta - \sigma^2/(2\kappa^2)$. Find the condition on $(\kappa, \theta, \sigma)$ under which $R_\infty < 0$. For $\kappa = 0.1$ and $\theta = 0.02$, what is the maximum volatility $\sigma$ for which $R_\infty$ remains positive?

---

**Exercise 6.** In the shifted Vasicek model $r_t = \underline{r} + x_t$ where $x_t$ follows standard Vasicek dynamics, the probability of rates below $\underline{r}$ is the same as the probability of negative rates in the original model. If the original model has $\mathbb{P}(r_\infty < 0) = 2.64\%$, what is $\mathbb{P}(r_\infty < \underline{r})$ in the shifted model? Explain why the shift does not eliminate the tail risk but merely relocates it.

---

**Exercise 7.** Compare the Vasicek and CIR models in terms of their treatment of negative rates. For the CIR model $dr_t = \kappa(\theta - r_t)dt + \sigma\sqrt{r_t}\,dW_t$ with the Feller condition $2\kappa\theta \geq \sigma^2$, explain why $r_t \geq 0$ almost surely. What empirical scenarios favor the Vasicek model's ability to produce negative rates over CIR's non-negativity constraint?
