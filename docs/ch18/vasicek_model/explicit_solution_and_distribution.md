# Explicit Solution and Distribution

*This section covers the explicit solution and distribution of the Vasicek short rate in the context of Chapter 18.*

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Derive the explicit solution to the Vasicek SDE
    2. Understand the distribution of short rates at any future time
    3. Calculate expected values and variances
    4. Interpret the asymptotic behavior of the process
    5. Use distributional properties for risk management

---

## Overview

While the Vasicek SDE is elegant and intuitive, having explicit solutions and understanding the distribution of future rates is crucial for practical implementation. This section derives closed-form expressions for the mean and variance of Vasicek short rates, which can then be used for forecasting, option pricing, and risk measurement.

---

## Solving the Vasicek SDE

### Method: Integrating Factor

The Vasicek SDE is:

$$dr_t = \alpha(\theta - r_t)dt + \sigma dW_t$$

This is a linear SDE with a known explicit solution. We can solve it using the integrating factor method.

First, rewrite the equation in standard form:

$$dr_t + \alpha r_t dt = \alpha\theta dt + \sigma dW_t$$

The integrating factor is $e^{\alpha t}$. Multiply both sides:

$$e^{\alpha t}dr_t + \alpha e^{\alpha t}r_t dt = \alpha\theta e^{\alpha t}dt + \sigma e^{\alpha t}dW_t$$

The left side is $d(e^{\alpha t}r_t)$:

$$d(e^{\alpha t}r_t) = \alpha\theta e^{\alpha t}dt + \sigma e^{\alpha t}dW_t$$

Integrating from $0$ to $t$:

$$e^{\alpha t}r_t - r_0 = \alpha\theta\int_0^t e^{\alpha s}ds + \sigma\int_0^t e^{\alpha s}dW_s$$

The deterministic integral evaluates to:

$$\int_0^t e^{\alpha s}ds = \frac{1}{\alpha}(e^{\alpha t} - 1)$$

Therefore:

$$e^{\alpha t}r_t = r_0 + \theta(e^{\alpha t} - 1) + \sigma\int_0^t e^{\alpha s}dW_s$$

Solving for $r_t$:

$$\boxed{r_t = e^{-\alpha t}r_0 + \theta(1 - e^{-\alpha t}) + \sigma e^{-\alpha t}\int_0^t e^{\alpha s}dW_s}$$

This is the **explicit solution** of the Vasicek SDE.

### Alternative Form

The solution can also be written as:

$$r_t = e^{-\alpha t}r_0 + (1 - e^{-\alpha t})\theta + \sigma\int_0^t e^{-\alpha(t-s)}dW_s$$

This form shows that $r_t$ is a weighted average of:
1. The initial rate $r_0$ (decaying exponentially)
2. The long-run mean $\theta$ (approaching with weight $1 - e^{-\alpha t}$)
3. Accumulated random shocks weighted by their exponential decay

---

## Distribution of Short Rates

### Conditional Distribution Given r_0

Since the solution is a linear combination of the initial condition, a constant, and a Gaussian integral, $r_t$ is **normally distributed** conditional on $r_0$:

$$r_t | r_0 \sim \mathcal{N}(\mu(t), \sigma^2(t))$$

where the conditional mean and variance are:

$$\boxed{\mathbb{E}[r_t | r_0] = e^{-\alpha t}r_0 + (1 - e^{-\alpha t})\theta}$$

$$\boxed{\text{Var}(r_t | r_0) = \frac{\sigma^2}{2\alpha}(1 - e^{-2\alpha t})}$$

### Derivation of Conditional Mean

Taking the expectation of the explicit solution:

$$\mathbb{E}[r_t] = e^{-\alpha t}r_0 + (1 - e^{-\alpha t})\theta + \sigma e^{-\alpha t}\mathbb{E}\left[\int_0^t e^{\alpha s}dW_s\right]$$

The Itô integral has zero expectation:

$$\mathbb{E}\left[\int_0^t e^{\alpha s}dW_s\right] = 0$$

Therefore:

$$\mathbb{E}[r_t | r_0] = e^{-\alpha t}r_0 + (1 - e^{-\alpha t})\theta$$

This can be rewritten as:

$$\mathbb{E}[r_t | r_0] = \theta + e^{-\alpha t}(r_0 - \theta)$$

**Interpretation**: The expected rate is a weighted average of the initial rate and the long-run mean, where the weight on the initial rate exponentially decays at rate $\alpha$.

### Derivation of Conditional Variance

The variance is determined by the stochastic integral component. Using Itô's isometry:

$$\text{Var}\left(\int_0^t e^{-\alpha(t-s)}dW_s\right) = \mathbb{E}\left[\left(\int_0^t e^{-\alpha(t-s)}dW_s\right)^2\right]$$

$$= \int_0^t e^{-2\alpha(t-s)}ds$$

Substituting $u = t - s$:

$$= \int_0^t e^{-2\alpha u}du = \left[-\frac{1}{2\alpha}e^{-2\alpha u}\right]_0^t$$

$$= \frac{1}{2\alpha}(1 - e^{-2\alpha t})$$

Therefore:

$$\text{Var}(r_t | r_0) = \sigma^2 \cdot \frac{1}{2\alpha}(1 - e^{-2\alpha t})$$

---

## Asymptotic Distribution

### As t → ∞

As time progresses to infinity, the effect of the initial condition $r_0$ vanishes, and the conditional distribution converges to the **stationary distribution**:

$$\lim_{t \to \infty} \mathbb{E}[r_t | r_0] = \theta$$

$$\lim_{t \to \infty} \text{Var}(r_t | r_0) = \frac{\sigma^2}{2\alpha}$$

Therefore, the stationary distribution is:

$$\boxed{r_\infty \sim \mathcal{N}\left(\theta, \frac{\sigma^2}{2\alpha}\right)}$$

### Interpretation of Stationary Variance

The long-run volatility $\sqrt{\frac{\sigma^2}{2\alpha}}$ depends on two competing effects:

**Higher volatility $\sigma$**: Increases long-run variance (more shocks)
**Higher mean reversion $\alpha$**: Decreases long-run variance (shocks are damped faster)

The ratio $\frac{\sigma^2}{2\alpha}$ balances these effects. For example:
- If we double $\sigma$ (more turbulent), variance quadruples
- If we double $\alpha$ (stronger mean reversion), variance halves

---

## Sample Paths and Monte Carlo Simulation

### Discretization Scheme

For numerical simulation, the Euler-Maruyama discretization is:

$$r_{t+\Delta t} = r_t + \alpha(\theta - r_t)\Delta t + \sigma \sqrt{\Delta t} \cdot Z$$

where $Z \sim \mathcal{N}(0, 1)$ and $\Delta t$ is the time step.

Alternatively, using the exact solution for discrete times:

$$r_{t_{i+1}} = e^{-\alpha(t_{i+1} - t_i)}r_{t_i} + (1 - e^{-\alpha(t_{i+1} - t_i)})\theta + \sigma\sqrt{\frac{1 - e^{-2\alpha(t_{i+1} - t_i)}}{2\alpha}} \cdot Z$$

The second form is **exact** (no discretization error) when moving between time steps.

### Path Characteristics

Sample paths of Vasicek rates typically exhibit:

1. **Mean-reversion clustering**: Paths oscillate around $\theta$
2. **Exponential decay of perturbations**: Deviations from equilibrium exponentially decay at rate $\alpha$
3. **Bounded variance growth**: Unlike Brownian motion, variance bounded at $\frac{\sigma^2}{2\alpha}$
4. **Continuous paths**: No jumps (in the basic model)

### Effect of Parameters on Paths

**Increasing $\alpha$ (faster mean reversion)**:
- Paths cluster more tightly around $\theta$
- Faster return to mean after shocks
- Less variation from equilibrium

**Increasing $\sigma$ (higher volatility)**:
- More dramatic excursions from $\theta$
- Greater amplitude of fluctuations
- Wider band of typical values

**Changing $\theta$ (different equilibrium)**:
- Shifts the entire path up or down
- Mean-reversion target changes
- Doesn't affect volatility structure

---

## Transition Density

The transition probability density from $r_s$ at time $s$ to $r_t$ at time $t > s$ is Gaussian:

$$f(r_t | r_s) = \frac{1}{\sqrt{2\pi\sigma^2(t-s)}} \exp\left[-\frac{(r_t - m(t-s))^2}{2\sigma^2(t-s)}\right]$$

where:

$$m(t-s) = e^{-\alpha(t-s)}r_s + (1 - e^{-\alpha(t-s)})\theta$$

$$\sigma^2(t-s) = \frac{\sigma^2}{2\alpha}(1 - e^{-2\alpha(t-s)})$$

This transition density is essential for:
- Computing likelihood functions for parameter estimation
- Filtering and state estimation
- Computing conditional probabilities in option pricing

---

## Practical Implications

### Forecasting

For a one-year forecast with $r_0 = 0.03$, $\theta = 0.04$, $\alpha = 0.2$, $\sigma = 0.01$:

$$\mathbb{E}[r_1] = e^{-0.2}(0.03) + (1 - e^{-0.2})(0.04) = 0.0357$$

The forecast is between the current rate and the long-run mean, closer to the current rate due to the short horizon.

**Confidence intervals** can be computed from the variance:

$$\text{SD}[r_1] = \sqrt{\frac{0.01^2}{2(0.2)}(1 - e^{-2(0.2)})} = 0.0048$$

A 95% confidence interval: $[0.0357 - 1.96(0.0048), 0.0357 + 1.96(0.0048)] = [0.0261, 0.0453]$

### Risk Management

The stationary variance $\frac{\sigma^2}{2\alpha}$ provides a measure of long-run interest rate risk. Portfolio managers use this to set:
- Duration targets
- Hedge ratios
- Value-at-risk (VaR) limits

---

## Summary

The Vasicek model admits a **closed-form solution** with explicit distributional properties:

1. **Conditional mean**: Exponentially weighted average of initial rate and long-run mean
2. **Conditional variance**: Grows from 0 to $\frac{\sigma^2}{2\alpha}$ as time increases
3. **Stationary distribution**: Normal with mean $\theta$ and variance $\frac{\sigma^2}{2\alpha}$
4. **Transition density**: Gaussian between any two times

These explicit formulas enable precise forecasting, efficient simulation, and rigorous risk quantification without resorting to approximations.

**Based on**: QuantPie Lecture Notes - Interest Rate Modeling

---

## Exercises

**Exercise 1.** For Vasicek parameters $\kappa = 0.5$ (using $\alpha = \kappa$), $\theta = 0.05$, $\sigma = 0.02$, and $r_0 = 0.03$, compute the conditional mean $\mathbb{E}[r_t | r_0]$ and conditional standard deviation $\sqrt{\text{Var}(r_t | r_0)}$ at $t = 1, 5, 10$ years.

??? success "Solution to Exercise 1"
    Using $\kappa = 0.5$, $\theta = 0.05$, $\sigma = 0.02$, $r_0 = 0.03$.

    The conditional mean is $\mathbb{E}[r_t | r_0] = \theta + (r_0 - \theta)e^{-\kappa t} = 0.05 + (0.03 - 0.05)e^{-0.5t} = 0.05 - 0.02\,e^{-0.5t}$.

    The conditional standard deviation is $\text{SD}(r_t) = \sigma\sqrt{\frac{1 - e^{-2\kappa t}}{2\kappa}} = 0.02\sqrt{\frac{1 - e^{-t}}{1.0}}$.

    **At $t = 1$:**

    $$
    \mathbb{E}[r_1] = 0.05 - 0.02 \times e^{-0.5} = 0.05 - 0.02 \times 0.6065 = 0.05 - 0.01213 = 0.03787
    $$

    $$
    \text{SD}(r_1) = 0.02\sqrt{1 - e^{-1}} = 0.02\sqrt{1 - 0.3679} = 0.02\sqrt{0.6321} = 0.02 \times 0.7951 = 0.01590
    $$

    **At $t = 5$:**

    $$
    \mathbb{E}[r_5] = 0.05 - 0.02 \times e^{-2.5} = 0.05 - 0.02 \times 0.0821 = 0.05 - 0.00164 = 0.04836
    $$

    $$
    \text{SD}(r_5) = 0.02\sqrt{1 - e^{-5}} = 0.02\sqrt{1 - 0.00674} = 0.02\sqrt{0.99326} = 0.02 \times 0.9966 = 0.01993
    $$

    **At $t = 10$:**

    $$
    \mathbb{E}[r_{10}] = 0.05 - 0.02 \times e^{-5} = 0.05 - 0.02 \times 0.00674 = 0.05 - 0.000135 = 0.04987
    $$

    $$
    \text{SD}(r_{10}) = 0.02\sqrt{1 - e^{-10}} = 0.02\sqrt{0.99995} \approx 0.02000
    $$

    The mean converges to $\theta = 0.05$ and the standard deviation converges to $\sigma/\sqrt{2\kappa} = 0.02/\sqrt{1.0} = 0.02$, both essentially reached by $t = 10$.

---

**Exercise 2.** Derive the stationary distribution by taking $t \to \infty$ in the conditional mean and variance formulas. Show that $r_\infty \sim \mathcal{N}(\theta, \sigma^2/(2\kappa))$. For the parameters in Exercise 1, compute the stationary mean and standard deviation.

??? success "Solution to Exercise 2"
    The conditional mean is $\mathbb{E}[r_t | r_0] = \theta + (r_0 - \theta)e^{-\kappa t}$. As $t \to \infty$, $e^{-\kappa t} \to 0$ (since $\kappa > 0$), so:

    $$
    \lim_{t \to \infty} \mathbb{E}[r_t | r_0] = \theta
    $$

    The conditional variance is $\text{Var}(r_t | r_0) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$. As $t \to \infty$, $e^{-2\kappa t} \to 0$, so:

    $$
    \lim_{t \to \infty} \text{Var}(r_t | r_0) = \frac{\sigma^2}{2\kappa}
    $$

    Since $r_t$ is Gaussian for all $t$ (being a linear functional of Gaussian noise), the limiting distribution is also Gaussian:

    $$
    r_\infty \sim \mathcal{N}\!\left(\theta,\; \frac{\sigma^2}{2\kappa}\right)
    $$

    For the parameters in Exercise 1 ($\kappa = 0.5$, $\theta = 0.05$, $\sigma = 0.02$):

    $$
    \text{Stationary mean} = \theta = 0.05 = 5\%
    $$

    $$
    \text{Stationary SD} = \frac{\sigma}{\sqrt{2\kappa}} = \frac{0.02}{\sqrt{1.0}} = 0.02 = 2\%
    $$

    In steady state, the short rate fluctuates around 5% with a standard deviation of 2%, so approximately 95% of the time it lies in the interval $[1\%, 9\%]$.

---

**Exercise 3.** Using the explicit solution $r_t = r_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t}) + \sigma\int_0^t e^{-\kappa(t-s)}dW_s$, explain why $r_t$ is Gaussian. Identify the deterministic part and the stochastic part. What distribution does the stochastic integral have?

??? success "Solution to Exercise 3"
    The explicit solution is:

    $$
    r_t = \underbrace{r_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t})}_{\text{deterministic part}} + \underbrace{\sigma\int_0^t e^{-\kappa(t-s)}\,dW_s}_{\text{stochastic part}}
    $$

    The **deterministic part** $\mu(t) = r_0 e^{-\kappa t} + \theta(1 - e^{-\kappa t})$ is a non-random function of $t$ that interpolates from $r_0$ (at $t = 0$) to $\theta$ (as $t \to \infty$).

    The **stochastic part** is the Ito integral $X_t = \sigma\int_0^t e^{-\kappa(t-s)}\,dW_s$. Since the integrand $\sigma e^{-\kappa(t-s)}$ is a deterministic (non-random) function of $s$, this Ito integral is **Gaussian** with:

    - Mean: $\mathbb{E}[X_t] = 0$ (Ito integrals of deterministic integrands have zero mean)
    - Variance: $\text{Var}(X_t) = \sigma^2\int_0^t e^{-2\kappa(t-s)}\,ds = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$ (by Ito's isometry)

    Since $r_t = \mu(t) + X_t$ is the sum of a constant and a Gaussian random variable, $r_t$ is itself **Gaussian**:

    $$
    r_t \sim \mathcal{N}\!\left(\mu(t),\; \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})\right)
    $$

    The key property is that the Ito integral of a deterministic function against Brownian motion is always normally distributed---this is a fundamental result of stochastic calculus.

---

**Exercise 4.** Compute $\mathbb{P}(r_5 > 0.08 | r_0 = 0.03)$ for $\kappa = 0.5$, $\theta = 0.05$, $\sigma = 0.02$. Also compute $\mathbb{P}(r_5 < 0 | r_0 = 0.03)$.

??? success "Solution to Exercise 4"
    With $\kappa = 0.5$, $\theta = 0.05$, $\sigma = 0.02$, $r_0 = 0.03$, at $t = 5$:

    $$
    \mu(5) = 0.05 + (0.03 - 0.05)e^{-2.5} = 0.05 - 0.02 \times 0.0821 = 0.04836
    $$

    $$
    v(5) = 0.02\sqrt{\frac{1 - e^{-5}}{1.0}} = 0.02 \times 0.9966 = 0.01993
    $$

    **Probability $r_5 > 0.08$:**

    $$
    \mathbb{P}(r_5 > 0.08) = 1 - \Phi\!\left(\frac{0.08 - 0.04836}{0.01993}\right) = 1 - \Phi(1.587) = 1 - 0.9437 = 0.0563
    $$

    There is approximately a **5.6%** probability that rates exceed 8% in 5 years.

    **Probability $r_5 < 0$:**

    $$
    \mathbb{P}(r_5 < 0) = \Phi\!\left(\frac{0 - 0.04836}{0.01993}\right) = \Phi(-2.427) = 0.0076
    $$

    There is approximately a **0.76%** probability of negative rates at the 5-year horizon. This illustrates the well-known feature that the Vasicek model assigns positive probability to negative rates, though for these parameters the probability is small.

---

**Exercise 5.** The half-life of mean reversion is $t_{1/2} = \ln 2/\kappa$. Compute $t_{1/2}$ for $\kappa = 0.1, 0.5, 2.0$. After two half-lives, what fraction of the initial deviation $r_0 - \theta$ remains?

??? success "Solution to Exercise 5"
    The half-life is the time for the expected deviation $\mathbb{E}[r_t - \theta | r_0] = (r_0 - \theta)e^{-\kappa t}$ to decay to half its initial value:

    $$
    e^{-\kappa t_{1/2}} = \frac{1}{2} \quad \Longrightarrow \quad t_{1/2} = \frac{\ln 2}{\kappa}
    $$

    For the three values:

    - $\kappa = 0.1$: $t_{1/2} = \ln 2 / 0.1 = 6.93$ years
    - $\kappa = 0.5$: $t_{1/2} = \ln 2 / 0.5 = 1.39$ years
    - $\kappa = 2.0$: $t_{1/2} = \ln 2 / 2.0 = 0.347$ years $\approx$ 4.2 months

    After **two half-lives** ($t = 2t_{1/2}$):

    $$
    e^{-\kappa \cdot 2t_{1/2}} = e^{-2\ln 2} = e^{\ln(1/4)} = \frac{1}{4}
    $$

    So one-quarter (25%) of the initial deviation $r_0 - \theta$ remains. This is analogous to radioactive decay: after $n$ half-lives, the fraction remaining is $(1/2)^n$. After two half-lives, only 25% of the original shock persists.

---

**Exercise 6.** Show that the conditional variance $\text{Var}(r_t | r_0) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$ is monotonically increasing in $t$ and bounded above by $\sigma^2/(2\kappa)$. Sketch the variance as a function of $t$ for $\kappa = 0.5$, $\sigma = 0.02$.

??? success "Solution to Exercise 6"
    The conditional variance is $V(t) = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})$.

    **Monotonicity:** Taking the derivative with respect to $t$:

    $$
    V'(t) = \frac{\sigma^2}{2\kappa} \cdot 2\kappa\,e^{-2\kappa t} = \sigma^2\,e^{-2\kappa t} > 0
    $$

    Since $V'(t) > 0$ for all $t > 0$, the variance is **strictly increasing** in $t$.

    **Upper bound:** As $t \to \infty$, $e^{-2\kappa t} \to 0$, so:

    $$
    \sup_{t \geq 0} V(t) = \lim_{t \to \infty} V(t) = \frac{\sigma^2}{2\kappa}
    $$

    The variance is bounded above by $\sigma^2/(2\kappa)$ and approaches this bound asymptotically but never reaches it for finite $t$.

    **Sketch for $\kappa = 0.5$, $\sigma = 0.02$:** The upper bound is $V_\infty = 0.0004/1.0 = 0.0004$. The curve $V(t) = 0.0004(1 - e^{-t})$ starts at 0, rises steeply at first (slope $\sigma^2 = 0.0004$ at $t = 0$), then decelerates and asymptotes to $0.0004$. By $t = 3$ (about three time constants $1/(2\kappa) = 1$), the variance has reached $1 - e^{-3} \approx 95\%$ of its limiting value.

---

**Exercise 7.** The transition density $p(r_t | r_0)$ is Gaussian with known mean and variance. Write the log-likelihood function for $N$ equally spaced observations $r_0, r_{\Delta t}, r_{2\Delta t}, \ldots$ and show that maximizing it is equivalent to an OLS regression of $r_{t+\Delta t}$ on $r_t$.

??? success "Solution to Exercise 7"
    Given $N$ equally spaced observations $r_0, r_{\Delta t}, r_{2\Delta t}, \ldots, r_{N\Delta t}$, the transition density is:

    $$
    p(r_{(i+1)\Delta t} \mid r_{i\Delta t}) = \frac{1}{\sqrt{2\pi v^2}} \exp\!\left(-\frac{(r_{(i+1)\Delta t} - \mu_i)^2}{2v^2}\right)
    $$

    where $\mu_i = \theta + (r_{i\Delta t} - \theta)e^{-\kappa\Delta t}$ and $v^2 = \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa\Delta t})$.

    The log-likelihood is:

    $$
    \ell(\kappa, \theta, \sigma) = \sum_{i=0}^{N-1} \ln p(r_{(i+1)\Delta t} \mid r_{i\Delta t}) = -\frac{N}{2}\ln(2\pi v^2) - \frac{1}{2v^2}\sum_{i=0}^{N-1}(r_{(i+1)\Delta t} - \mu_i)^2
    $$

    Define $\phi = e^{-\kappa\Delta t}$, $a = \theta(1 - \phi)$, and $b = \phi$. Then $\mu_i = a + b\,r_{i\Delta t}$, and:

    $$
    \ell = -\frac{N}{2}\ln(2\pi v^2) - \frac{1}{2v^2}\sum_{i=0}^{N-1}(r_{(i+1)\Delta t} - a - b\,r_{i\Delta t})^2
    $$

    This is the log-likelihood of a linear regression model $Y_i = a + b\,X_i + \epsilon_i$ where $Y_i = r_{(i+1)\Delta t}$, $X_i = r_{i\Delta t}$, and $\epsilon_i \sim \mathcal{N}(0, v^2)$.

    Maximizing $\ell$ with respect to $a$ and $b$ (for fixed $v^2$) is equivalent to minimizing $\sum(Y_i - a - bX_i)^2$, which is exactly the **ordinary least squares** (OLS) criterion. The OLS estimators are:

    $$
    \hat{b} = \frac{\sum (X_i - \bar{X})(Y_i - \bar{Y})}{\sum (X_i - \bar{X})^2}, \qquad \hat{a} = \bar{Y} - \hat{b}\,\bar{X}
    $$

    The residual variance $\hat{v}^2 = \frac{1}{N}\sum(Y_i - \hat{a} - \hat{b}X_i)^2$ completes the MLE. The Vasicek parameters are then recovered: $\hat{\kappa} = -\ln\hat{b}/\Delta t$, $\hat{\theta} = \hat{a}/(1-\hat{b})$, $\hat{\sigma} = \hat{v}\sqrt{2\hat{\kappa}/(1-e^{-2\hat{\kappa}\Delta t})}$.
