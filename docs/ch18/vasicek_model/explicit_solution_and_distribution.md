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

### Conditional Distribution Given $r_0$

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

### As $t \to \infty$

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
