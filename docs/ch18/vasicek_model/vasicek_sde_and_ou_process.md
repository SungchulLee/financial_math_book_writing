# Vasicek SDE and Ornstein-Uhlenbeck Process

*This section covers the Vasicek SDE and its connection to the Ornstein-Uhlenbeck process in the context of Chapter 18.*

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Understand the Vasicek SDE for short rates
    2. Recognize the Vasicek model as a special case of the Ornstein-Uhlenbeck process
    3. Interpret the parameters of the model
    4. Understand the mean-reversion property
    5. Appreciate the role of Vasicek in interest rate modeling

---

## Overview

The **Vasicek model** is one of the most fundamental and elegant models in interest rate modeling. It describes the evolution of the instantaneous short rate $r_t$ and belongs to the broader class of one-factor short-rate models. The key innovation of the Vasicek model is the introduction of mean reversion, making it more realistic than the earlier Merton model which allowed rates to become arbitrarily negative.

---

## Vasicek Stochastic Differential Equation

The short rate $r_t$ in the Vasicek model follows the SDE:

$$dr_t = \alpha(\theta - r_t)dt + \sigma dW_t$$

where:
- $r_t$ is the instantaneous short rate at time $t$
- $\alpha > 0$ is the **mean reversion speed** parameter
- $\theta$ is the **long-run mean** (also called the equilibrium rate)
- $\sigma > 0$ is the **volatility** of the short rate
- $W_t$ is a standard Wiener process (Brownian motion)

### Interpretation of Parameters

**Mean Reversion Speed ($\alpha$)**:
- Controls how quickly rates revert to the long-run mean
- Larger $\alpha$ means faster mean reversion
- Small $\alpha$ means slow reversion (rates wander for longer periods)
- Typical values: $\alpha \in [0.05, 1.0]$ depending on the modeling horizon

**Long-Run Mean ($\theta$)**:
- The equilibrium interest rate level
- Represents the average rate around which short rates fluctuate
- Typically calibrated to historical averages or market expectations
- Can be constant or time-dependent in extensions

**Volatility ($\sigma$)**:
- Controls the magnitude of random fluctuations
- Higher volatility means more pronounced rate movements
- Typical values: $\sigma \in [0.005, 0.03]$ (50 to 300 basis points)
- Standard deviation of rates grows as $\sqrt{t}$ in the long run

---

## Connection to Ornstein-Uhlenbeck Process

The Vasicek SDE is precisely an **Ornstein-Uhlenbeck (OU) process**, one of the most important stochastic processes in quantitative finance. The OU process is defined as:

$$dx_t = -\lambda x_t dt + \sigma dW_t$$

where $x_t$ is mean zero. The Vasicek model can be rewritten in OU form by defining the deviation from the long-run mean:

$$y_t = r_t - \theta$$

Then:

$$dy_t = d(r_t - \theta) = dr_t = \alpha(\theta - r_t)dt + \sigma dW_t = -\alpha y_t dt + \sigma dW_t$$

This is exactly the Ornstein-Uhlenbeck form with $\lambda = \alpha$.

### Properties of the OU Process

**Mean Reversion**:
- The process is attracted to its equilibrium level ($\theta$ for Vasicek)
- The drift term $\alpha(\theta - r_t)$ is positive when $r_t < \theta$ and negative when $r_t > \theta$
- This creates an automatic "restoring force" toward equilibrium

**Stationary Distribution**:
- In the long run, the process converges to a stationary distribution
- For Vasicek: $r_\infty \sim \mathcal{N}(\theta, \sigma^2/(2\alpha))$
- The stationary variance depends on both $\sigma$ (volatility) and $\alpha$ (mean reversion speed)

**Path Properties**:
- Paths are continuous but highly fluctuating
- The process exhibits "clustering" behavior around the long-run mean
- Mean reversion prevents explosive behavior (unlike geometric Brownian motion)

---

## Mean Reversion Dynamics

### Graphical Interpretation

When plotting sample paths of the Vasicek model:

**For strong mean reversion (large $\alpha$)**:
- Paths that deviate above $\theta$ are quickly pulled back down
- Same for paths below $\theta$: quickly restored upward
- Paths oscillate tightly around the mean
- Variation around the mean is relatively modest

**For weak mean reversion (small $\alpha$)**:
- Paths wander far from $\theta$ for extended periods
- Slower return to equilibrium
- More pronounced trends and trending behavior
- Greater variation around the mean

**Impact of volatility ($\sigma$)**:
- Higher $\sigma$ causes more dramatic excursions from $\theta$
- Mean reversion still operates, but the path is "noisier"
- Extreme values become more likely

### Mathematical Expression of Mean Reversion

The instantaneous drift (expected change) of the short rate is:

$$\mathbb{E}[dr_t | r_t] = \alpha(\theta - r_t)dt$$

This shows that:
- If $r_t > \theta$: the drift is negative (rates expected to decrease)
- If $r_t < \theta$: the drift is positive (rates expected to increase)
- If $r_t = \theta$: the drift is zero (equilibrium)

The magnitude of the expected change is proportional to the deviation from equilibrium, scaled by the mean reversion speed $\alpha$.

---

## Comparison with Other Models

| Model | SDE | Key Feature | Limitation |
|-------|-----|-------------|-----------|
| **Vasicek** | $dr_t = \alpha(\theta - r_t)dt + \sigma dW_t$ | Mean reversion | Allows negative rates |
| **Merton** | $dr_t = \mu dt + \sigma dW_t$ | Simple, closed-form | No mean reversion |
| **CIR** | $dr_t = \alpha(\theta - r_t)dt + \sigma\sqrt{r_t} dW_t$ | Positive rates | More complex |
| **Hull-White** | $dr_t = (\theta(t) - ar_t)dt + \sigma dW_t$ | Calibratable | Time-varying parameters |

---

## Extensions and Variants

**Time-Dependent Parameters**:
- $\alpha(t)$, $\theta(t)$, $\sigma(t)$ can be made time-dependent
- Allows calibration to initial term structure
- Hull-White model is Vasicek with time-varying $\theta(t)$

**Multi-Factor Vasicek**:
- Multiple correlated short-rate factors
- Better captures term structure dynamics
- More parameters but more flexibility

**Negative Rate Handling**:
- Original Vasicek allows negative rates (problematic pre-2008)
- Modern implementations may add lower bounds
- Alternative: CIR model prevents negative rates

---

## Summary

The **Vasicek model** combines elegant mathematical tractability with realistic mean-reversion behavior. Its stochastic differential equation:

$$dr_t = \alpha(\theta - r_t)dt + \sigma dW_t$$

defines one of the foundational frameworks in interest rate modeling. By recognizing it as an Ornstein-Uhlenbeck process, we gain access to well-developed stochastic process theory and can derive explicit formulas for bond prices and interest rate derivatives.

The mean-reversion property makes the model particularly suitable for long-term interest rate projections and risk management applications, where the assumption that rates fluctuate around a stable long-run equilibrium is reasonable.

**Based on**: QuantPie Lecture Notes - Interest Rate Modeling
