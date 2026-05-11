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

---

## Exercises

---

**Exercise 1.** Consider the linear SDE

$$
dX_t = (2 - 3X_t)\,dt + 4\,dW_t, \qquad X_0 = 0
$$

(a) Identify the mean-reversion speed $a$, long-term mean $\theta$, and volatility $\sigma$.

(b) Solve using the integrating factor method. Write the integrating factor explicitly.

(c) Compute $\mathbb{E}[X_t]$ and $\operatorname{Var}[X_t]$.

??? success "Solution to Exercise 3"
    The SDE $dX_t = (2 - 3X_t)\,dt + 4\,dW_t$ is an Ornstein-Uhlenbeck process.

    **(a)** Rewrite the drift as $a(\theta - X_t) = 3(\frac{2}{3} - X_t)$, so:

    - Mean-reversion speed: $a = 3$
    - Long-term mean: $\theta = 2/3$
    - Volatility: $\sigma = 4$

    **(b)** The integrating factor is $M(t) = e^{3t}$. Define $Y_t = e^{3t}X_t$. By the Ito product rule (no quadratic covariation since $e^{3t}$ is deterministic):

    $$
    dY_t = 3e^{3t}X_t\,dt + e^{3t}\,dX_t = 3e^{3t}X_t\,dt + e^{3t}[(2 - 3X_t)\,dt + 4\,dW_t]
    $$

    $$
    = 2e^{3t}\,dt + 4e^{3t}\,dW_t
    $$

    Integrating: $Y_t = Y_0 + \int_0^t 2e^{3s}\,ds + \int_0^t 4e^{3s}\,dW_s = 0 + \frac{2}{3}(e^{3t} - 1) + 4\int_0^t e^{3s}\,dW_s$

    Dividing by $e^{3t}$:

    $$
    X_t = \frac{2}{3}(1 - e^{-3t}) + 4\int_0^t e^{-3(t-s)}\,dW_s
    $$

    **(c)** The expectation is (the stochastic integral has zero mean):

    $$
    \mathbb{E}[X_t] = \frac{2}{3}(1 - e^{-3t})
    $$

    The variance is computed via Ito isometry:

    $$
    \operatorname{Var}[X_t] = 16 \int_0^t e^{-6(t-s)}\,ds = 16 \cdot \frac{1 - e^{-6t}}{6} = \frac{8}{3}(1 - e^{-6t})
    $$

---

**Exercise 2.** Solve the Vasicek model

$$
dr_t = 0.5(0.04 - r_t)\,dt + 0.01\,dW_t, \qquad r_0 = 0.03
$$

(a) Write the explicit solution for $r_t$.

(b) Find the stationary distribution.

(c) Compute $\mathbb{E}[r_1]$ and $\operatorname{Var}[r_1]$.

??? success "Solution to Exercise 5"
    The Vasicek model $dr_t = 0.5(0.04 - r_t)\,dt + 0.01\,dW_t$ has $a = 0.5$, $\theta = 0.04$, $\sigma = 0.01$, $r_0 = 0.03$.

    **(a)** The explicit solution is:

    $$
    r_t = 0.03\,e^{-0.5t} + 0.04(1 - e^{-0.5t}) + 0.01\int_0^t e^{-0.5(t-s)}\,dW_s
    $$

    **(b)** The stationary distribution is $r_\infty \sim \mathcal{N}\!\left(\theta, \frac{\sigma^2}{2a}\right)$:

    $$
    r_\infty \sim \mathcal{N}\!\left(0.04,\; \frac{0.0001}{1.0}\right) = \mathcal{N}(0.04,\; 0.0001)
    $$

    The stationary standard deviation is $\sqrt{0.0001} = 0.01 = 1\%$.

    **(c)** At $t = 1$:

    $$
    \mathbb{E}[r_1] = 0.03\,e^{-0.5} + 0.04(1 - e^{-0.5}) = 0.03 \times 0.6065 + 0.04 \times 0.3935 \approx 0.03394
    $$

    $$
    \operatorname{Var}[r_1] = \frac{0.0001}{1.0}(1 - e^{-1.0}) = 0.0001 \times 0.6321 \approx 6.321 \times 10^{-5}
    $$

**Exercise 3.** For Vasicek parameters $\alpha = 0.3$, $\theta = 0.05$, $\sigma = 0.02$, compute the instantaneous expected drift $\mathbb{E}[dr_t \mid r_t]$ when $r_t = 0.02$, $r_t = 0.05$, and $r_t = 0.08$. Interpret the sign and magnitude of the drift in each case.

??? success "Solution to Exercise 1"
    The instantaneous expected drift is $\mathbb{E}[dr_t \mid r_t] = \alpha(\theta - r_t)\,dt$ with $\alpha = 0.3$ and $\theta = 0.05$.

    **When $r_t = 0.02$:**

    $$
    \alpha(\theta - r_t) = 0.3 \times (0.05 - 0.02) = 0.3 \times 0.03 = 0.009
    $$

    The drift is **positive** (+90 bp/year). The rate is below equilibrium, so the mean-reversion force pushes it upward toward $\theta = 5\%$.

    **When $r_t = 0.05$:**

    $$
    \alpha(\theta - r_t) = 0.3 \times (0.05 - 0.05) = 0
    $$

    The drift is **zero**. The rate is exactly at the long-run mean, so there is no deterministic pull in either direction. Changes are driven purely by the random term $\sigma\,dW_t$.

    **When $r_t = 0.08$:**

    $$
    \alpha(\theta - r_t) = 0.3 \times (0.05 - 0.08) = 0.3 \times (-0.03) = -0.009
    $$

    The drift is **negative** ($-90$ bp/year). The rate is above equilibrium, so the mean-reversion force pulls it downward. The magnitude is the same as the $r_t = 0.02$ case because the deviation from $\theta$ is symmetric.

---

**Exercise 4.** Transform the Vasicek SDE into the standard OU form by defining $y_t = r_t - \theta$. Write the SDE for $y_t$ and identify the mean-reversion speed and volatility. What is the stationary distribution of $y_t$, and how does it relate to the stationary distribution of $r_t$?

??? success "Solution to Exercise 2"
    Define $y_t = r_t - \theta$. Then:

    $$
    dy_t = dr_t = \alpha(\theta - r_t)\,dt + \sigma\,dW_t = \alpha(\theta - (y_t + \theta))\,dt + \sigma\,dW_t = -\alpha y_t\,dt + \sigma\,dW_t
    $$

    This is the standard OU form $dy_t = -\alpha y_t\,dt + \sigma\,dW_t$ with:

    - Mean-reversion speed: $\alpha$ (same as the original Vasicek parameter)
    - Volatility: $\sigma$ (same as the original)
    - Equilibrium level: $0$ (the OU process mean-reverts to zero)

    The stationary distribution of $y_t$ is:

    $$
    y_\infty \sim \mathcal{N}\!\left(0,\; \frac{\sigma^2}{2\alpha}\right)
    $$

    Since $r_t = y_t + \theta$, the stationary distribution of $r_t$ is obtained by shifting:

    $$
    r_\infty = y_\infty + \theta \sim \mathcal{N}\!\left(\theta,\; \frac{\sigma^2}{2\alpha}\right)
    $$

    The mean shifts from $0$ to $\theta$, while the variance $\sigma^2/(2\alpha)$ is unchanged. This confirms the result for the Vasicek stationary distribution.

---

**Exercise 5.** The stationary variance of the Vasicek model is $\sigma^2/(2\alpha)$. For $\alpha = 0.5$ and $\sigma = 0.02$, compute the stationary standard deviation. If $\alpha$ is halved to $0.25$ while keeping $\sigma$ fixed, by what factor does the stationary standard deviation change? Explain intuitively why weaker mean reversion increases long-run variability.

??? success "Solution to Exercise 3"
    The stationary standard deviation is:

    $$
    \text{SD}(r_\infty) = \frac{\sigma}{\sqrt{2\alpha}}
    $$

    For $\alpha = 0.5$, $\sigma = 0.02$:

    $$
    \text{SD} = \frac{0.02}{\sqrt{1.0}} = 0.02 = 2.0\%
    $$

    For $\alpha = 0.25$, $\sigma = 0.02$:

    $$
    \text{SD} = \frac{0.02}{\sqrt{0.5}} = \frac{0.02}{0.7071} = 0.02828 = 2.83\%
    $$

    The factor of change is $\sqrt{2} \approx 1.414$: halving $\alpha$ increases the stationary standard deviation by a factor of $\sqrt{2}$.

    **Intuition:** Weaker mean reversion ($\alpha = 0.25$ vs $0.5$) means the process takes longer to return to $\theta$ after a random shock. Each shock has more time to propagate before being damped, so shocks accumulate more effectively, producing larger long-run variability. The stationary variance $\sigma^2/(2\alpha)$ reflects the balance between the rate of shock arrival ($\sigma^2$ per unit time) and the rate of damping ($2\alpha$). Halving the damping rate doubles the variance (and increases the SD by $\sqrt{2}$).

---

**Exercise 6.** Compare the Vasicek SDE $dr_t = \alpha(\theta - r_t)dt + \sigma dW_t$ with the Merton model $dr_t = \mu\,dt + \sigma dW_t$. Show that the Merton model is a special case of Vasicek with $\alpha = 0$. What happens to the stationary distribution formula $\mathcal{N}(\theta, \sigma^2/(2\alpha))$ as $\alpha \to 0$? Does the Merton model have a stationary distribution?

??? success "Solution to Exercise 4"
    The Merton model is $dr_t = \mu\,dt + \sigma\,dW_t$. We can write the Vasicek SDE as:

    $$
    dr_t = \alpha\theta\,dt - \alpha r_t\,dt + \sigma\,dW_t
    $$

    Setting $\alpha = 0$: $dr_t = 0 \cdot \theta\,dt - 0 \cdot r_t\,dt + \sigma\,dW_t = \sigma\,dW_t$, which is the Merton model with $\mu = 0$. For general $\mu$, the Merton model is Vasicek with $\alpha = 0$ and $\alpha\theta = \mu$ (i.e., $\mu = \alpha\theta$ in the limit, though this requires $\theta \to \infty$ if $\alpha \to 0$ with $\mu \neq 0$). More precisely, the Merton drift $\mu$ corresponds to taking $\alpha \to 0$ while $\alpha\theta \to \mu$.

    **Stationary distribution as $\alpha \to 0$:** The stationary variance is $\sigma^2/(2\alpha)$. As $\alpha \to 0^+$:

    $$
    \frac{\sigma^2}{2\alpha} \to +\infty
    $$

    The variance diverges to infinity. This means the Merton model has **no stationary distribution**: without mean reversion, the process $r_t = r_0 + \mu t + \sigma W_t$ is a random walk with drift, whose variance $\sigma^2 t$ grows without bound. The rate wanders arbitrarily far from any fixed level, and no equilibrium distribution exists.

---

**Exercise 7.** The mean reversion speed $\alpha$ determines how quickly the process returns to $\theta$ after a shock. If rates are currently at $r_0 = 0.08$ and $\theta = 0.05$, compute the expected rate $\mathbb{E}[r_t \mid r_0]$ at $t = 1, 3, 5$ years for $\alpha = 0.1$ and $\alpha = 1.0$ (using the formula from the explicit solution section). How many years does it take for the expected deviation $r_0 - \theta$ to decay to 10% of its initial value in each case?

??? success "Solution to Exercise 5"
    The conditional expected rate is $\mathbb{E}[r_t \mid r_0] = \theta + (r_0 - \theta)e^{-\alpha t}$ with $r_0 = 0.08$, $\theta = 0.05$.

    **For $\alpha = 0.1$:**

    | $t$ | $e^{-0.1t}$ | $\mathbb{E}[r_t]$ |
    |:-:|:-:|:-:|
    | 1 | 0.9048 | $0.05 + 0.03 \times 0.9048 = 0.07715$ |
    | 3 | 0.7408 | $0.05 + 0.03 \times 0.7408 = 0.07222$ |
    | 5 | 0.6065 | $0.05 + 0.03 \times 0.6065 = 0.06820$ |

    Time for deviation to decay to 10%: $e^{-0.1t} = 0.1 \Rightarrow t = \ln(10)/0.1 = 23.03$ years.

    **For $\alpha = 1.0$:**

    | $t$ | $e^{-t}$ | $\mathbb{E}[r_t]$ |
    |:-:|:-:|:-:|
    | 1 | 0.3679 | $0.05 + 0.03 \times 0.3679 = 0.06104$ |
    | 3 | 0.0498 | $0.05 + 0.03 \times 0.0498 = 0.05149$ |
    | 5 | 0.0067 | $0.05 + 0.03 \times 0.0067 = 0.05020$ |

    Time for deviation to decay to 10%: $e^{-t} = 0.1 \Rightarrow t = \ln(10) = 2.303$ years.

    With $\alpha = 1.0$, the expected rate is nearly at equilibrium by year 3. With $\alpha = 0.1$, the 3% initial deviation barely halves in 5 years and takes over 23 years to decay to 10%.

---

**Exercise 8.** The Hull-White model $dr_t = (\theta(t) - ar_t)dt + \sigma dW_t$ generalizes Vasicek by allowing a time-dependent $\theta(t)$. Explain why this extension enables exact calibration to an arbitrary initial yield curve. What property of the constant-$\theta$ Vasicek model prevents it from matching an arbitrary yield curve?

??? success "Solution to Exercise 6"
    The Hull-White model $dr_t = (\theta(t) - ar_t)\,dt + \sigma\,dW_t$ has a **time-dependent** function $\theta(t)$. The bond pricing formula becomes $P(0,T) = A(0,T)\,e^{-B(T)\,r_0}$ where $\ln A(0,T)$ now involves an integral of $\theta(s)$.

    The key equation is: given any observed initial forward rate curve $f^{\text{mkt}}(0,T)$, one can choose $\theta(t)$ so that the model forward rate matches the market:

    $$
    f^{\text{model}}(0,T) = f^{\text{mkt}}(0,T) \quad \text{for all } T
    $$

    This gives $\theta(t) = f_T^{\text{mkt}}(0,t) + af^{\text{mkt}}(0,t) + \frac{\sigma^2}{2a}(1 - e^{-2at})$. Since $\theta(t)$ has a free function (infinitely many degrees of freedom), it can match any smooth initial yield curve exactly.

    The **constant-$\theta$ Vasicek model** has only three parameters $(\kappa, \theta, \sigma)$, producing a yield curve of a specific functional form. This three-parameter family of curves is too restrictive to match an arbitrary observed yield curve, which may have local humps, kinks, or other features requiring more flexibility. The fundamental limitation is that the Vasicek model imposes a rigid shape: the yield interpolates between $r_0$ and $R_\infty = \theta - \sigma^2/(2\kappa^2)$ along a fixed exponential path, with no room for local adjustments.

---

**Exercise 9.** The CIR model replaces the constant diffusion $\sigma$ in Vasicek with $\sigma\sqrt{r_t}$. Explain qualitatively how the square-root diffusion prevents negative rates. Does the CIR model remain an Ornstein-Uhlenbeck process? What key analytical property of the OU process (linearity of the SDE in $r_t$) is lost in CIR?

??? success "Solution to Exercise 7"
    In the CIR model, the diffusion coefficient is $\sigma\sqrt{r_t}$ instead of the constant $\sigma$ in Vasicek.

    **How square-root diffusion prevents negative rates:** As $r_t \to 0^+$, the noise term $\sigma\sqrt{r_t}\,dW_t$ vanishes because $\sqrt{r_t} \to 0$. Simultaneously, the drift $\kappa(\theta - r_t) \to \kappa\theta > 0$ pushes the rate upward. Near zero, the process is dominated by the positive drift with negligible noise, preventing it from crossing into negative territory. The Feller condition $2\kappa\theta \geq \sigma^2$ ensures the drift is strong enough relative to the noise that zero is never reached.

    **Is CIR an OU process?** No. The OU process is defined by a **linear** SDE $dx_t = -\alpha x_t\,dt + \sigma\,dW_t$ with constant diffusion coefficient. The CIR SDE $dr_t = \kappa(\theta - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t$ has a state-dependent diffusion $\sigma\sqrt{r_t}$, making it nonlinear. It belongs to the broader class of affine diffusions but is not an OU process.

    **Key analytical property lost:** The OU process has the property that the SDE is **linear in the state variable** with **additive** (state-independent) noise. This linearity guarantees:

    1. The solution is a Gaussian process (sums and integrals of Gaussian variables remain Gaussian).
    2. The transition density is explicitly Gaussian.
    3. Bond prices have the simple exponential-affine form with closed-form $A$ and $B$ from linear ODEs.

    In CIR, the multiplicative noise $\sigma\sqrt{r_t}$ breaks linearity. The solution is no longer Gaussian---it follows a non-central chi-squared distribution. The ODE for $B(\tau)$ becomes a Riccati equation (quadratic rather than linear), producing a more complex $B$ involving $\gamma = \sqrt{\kappa^2 + 2\sigma^2}$. While closed-form solutions still exist (thanks to the affine structure), they are more involved than the Vasicek case.
