# CIR Variance Process Solution

The variance process in the Heston model is a Cox-Ingersoll-Ross (CIR) diffusion, named after its original application to interest rate modeling. Unlike many stochastic processes, the CIR process has an explicitly known transition density: the conditional distribution of $v_T$ given $v_t$ is a scaled non-central chi-squared distribution. This exact distributional characterization is fundamental for several purposes -- it enables unbiased simulation (the Broadie-Kaya exact scheme), provides the moments of the variance process in closed form, and yields the Laplace transform that connects to the affine characteristic function.

This section derives the transition density, expresses it in terms of the non-central chi-squared distribution, states the characteristic function of $v_T$, and provides the exact sampling formula. We assume familiarity with the Heston SDE from the [model definition section](../model_definition/heston_sde_and_parameters.md) and with the [non-central chi-squared distribution](non_central_chi_squared.md).

!!! abstract "Learning Objectives"
    After completing this section, you should be able to:

    - State the transition density of the CIR variance process in terms of the non-central chi-squared distribution
    - Identify the degrees of freedom and non-centrality parameters
    - Derive the Laplace transform of $v_T$ conditional on $v_t$
    - Explain how the exact transition density enables unbiased simulation
    - Compute the conditional expectation and variance of $v_T$ from the transition distribution

---

## The CIR Process

### Setup

The variance process in the Heston model satisfies:

$$
dv_t = \kappa(\theta - v_t)\,dt + \sigma_v\sqrt{v_t}\,dW_t
$$

with $\kappa > 0$, $\theta > 0$, $\sigma_v > 0$, and $v_0 > 0$. This is the Cox-Ingersoll-Ross (1985) process, originally proposed for modeling the short rate of interest.

### Integral Form

Integrating the SDE from $t$ to $T$ with $\tau = T - t$:

$$
v_T = v_t + \kappa\theta\tau - \kappa\int_t^T v_s\,ds + \sigma_v\int_t^T \sqrt{v_s}\,dW_s
$$

The last term is a stochastic integral (a martingale with zero expectation), and the mean-reversion integral $\int_t^T v_s\,ds$ is the integrated variance, which itself has a known distribution (used in the Broadie-Kaya exact simulation scheme). Rather than working with this integral form directly, we proceed through the connection to Bessel processes to derive the exact transition density.

---

## Transition Density via the Non-Central Chi-Squared Distribution

### The Key Result

!!! success "Theorem: CIR Transition Density"
    Let $v_t > 0$ be the variance at time $t$, and let $\tau = T - t > 0$. The conditional distribution of $v_T$ given $v_t$ is:

    $$
    v_T \;\Big|\; v_t \;\sim\; \frac{c}{2}\;\chi^2_\delta(\lambda)
    $$

    where $\chi^2_\delta(\lambda)$ denotes the non-central chi-squared distribution with $\delta$ degrees of freedom and non-centrality parameter $\lambda$, and:

    $$
    c = \frac{\sigma_v^2(1 - e^{-\kappa\tau})}{4\kappa}
    $$

    $$
    \delta = \frac{4\kappa\theta}{\sigma_v^2}
    $$

    $$
    \lambda = \frac{4\kappa\,e^{-\kappa\tau}\,v_t}{\sigma_v^2(1 - e^{-\kappa\tau})} = \frac{v_t}{c}\,e^{-\kappa\tau}\cdot\frac{2}{1} = \frac{4\kappa\,v_t\,e^{-\kappa\tau}}{\sigma_v^2(1-e^{-\kappa\tau})}
    $$

    Equivalently, $v_T / c$ follows a non-central chi-squared distribution with $\delta$ degrees of freedom and non-centrality parameter $\lambda$.

### Interpretation of the Parameters

**Degrees of freedom $\delta = 4\kappa\theta/\sigma_v^2$.** This is twice the Feller ratio. When $\delta \geq 2$ (Feller condition), the non-central chi-squared density is zero at the origin, confirming that $v_T > 0$ a.s. When $\delta < 2$, the density has a singularity at zero, reflecting the positive probability of $v_T$ being near zero.

**Non-centrality parameter $\lambda$.** This depends on the current variance $v_t$ and decays exponentially with $\tau$ at rate $\kappa$. As $\tau \to \infty$, $\lambda \to 0$ and $v_T / c \to \chi^2_\delta(0) = \chi^2_\delta$, the central chi-squared distribution. This reflects the mean-reversion: for large $\tau$, the process "forgets" its initial condition.

**Scale parameter $c$.** This parameter converts from the chi-squared scale to the variance scale. As $\tau \to \infty$, $c \to \sigma_v^2/(4\kappa)$.

### Proof Sketch

The proof proceeds in three steps:

**Step 1.** Define the time-changed process $\tilde{v}_s = e^{\kappa s}v_s$. Ito's lemma gives:

$$
d\tilde{v}_s = e^{\kappa s}(dv_s + \kappa v_s\,ds) = e^{\kappa s}\kappa\theta\,ds + e^{\kappa s}\sigma_v\sqrt{v_s}\,dW_s = \kappa\theta\,e^{\kappa s}\,ds + \sigma_v\sqrt{\tilde{v}_s\,e^{\kappa s}}\,dW_s
$$

**Step 2.** Introduce the deterministic time change $\psi(s) = \frac{\sigma_v^2}{4\kappa}(e^{\kappa s} - 1)$ and show that $R_u = \tilde{v}_{\psi^{-1}(u)}/(\sigma_v^2/4)$ is a squared Bessel process of dimension $\delta = 4\kappa\theta/\sigma_v^2$ started at $4v_0/\sigma_v^2$.

**Step 3.** The transition density of the squared Bessel process of dimension $\delta$ is known to be a non-central chi-squared distribution. Inverting the time change and scaling gives the result. $\square$

---

## The Transition Density Function

The probability density function of $v_T$ given $v_t$ can be written explicitly using the non-central chi-squared density.

!!! info "Definition: CIR Transition Density"
    The transition density of the CIR process is:

    $$
    f_{v_T|v_t}(v) = \frac{1}{c}\,f_{\chi^2_\delta(\lambda)}\!\left(\frac{v}{c}\right)
    $$

    where $f_{\chi^2_\delta(\lambda)}$ is the non-central chi-squared density. Using the Bessel function representation:

    $$
    f_{v_T|v_t}(v) = \frac{\kappa}{\sigma_v^2\sinh(\kappa\tau/2)}\exp\!\left(-\frac{\kappa(v_t e^{-\kappa\tau} + v)}{2c\kappa}\right)\left(\frac{v}{v_t e^{-\kappa\tau}}\right)^{(\delta-2)/4} I_{(\delta-2)/2}\!\left(\frac{2\sqrt{v\,v_t\,e^{-\kappa\tau}}}{c}\right)
    $$

    where $I_\nu$ is the modified Bessel function of the first kind of order $\nu$.

The Bessel function representation is useful for analytical computations but is numerically delicate for small arguments. In practice, the non-central chi-squared CDF is computed using well-optimized library routines.

---

## Laplace Transform and Characteristic Function

The Laplace transform of $v_T$ given $v_t$ has a particularly clean exponential-affine form, which is the hallmark of the CIR process being an affine diffusion.

!!! success "Proposition: Laplace Transform of the CIR Process"
    For $w \geq 0$:

    $$
    \mathbb{E}\!\left[e^{-w\,v_T} \,\middle|\, v_t\right] = \exp\!\left(-\frac{2\kappa\theta}{\sigma_v^2}\ln\!\left(\frac{2\gamma\,e^{(\kappa+\gamma)\tau/2}}{\gamma + \kappa + (\gamma - \kappa)e^{-\gamma\tau}}\right) - \frac{2w\,v_t\,e^{-\kappa\tau}}{(\gamma + \kappa)(1-e^{-\gamma\tau})^{-1} + (\gamma - \kappa)}\right)
    $$

    where $\gamma = \sqrt{\kappa^2 + 2\sigma_v^2 w}$.

    A simpler equivalent form (using the non-central chi-squared moment generating function) is:

    $$
    \mathbb{E}\!\left[e^{-w\,v_T} \,\middle|\, v_t\right] = \left(\frac{1}{1 + 2cw}\right)^{\delta/2} \exp\!\left(-\frac{\lambda\,cw}{1 + 2cw}\right)
    $$

    where $c$, $\delta$, $\lambda$ are as defined in the transition density theorem.

**Proof.** The second form follows directly from the moment generating function of the non-central chi-squared distribution. If $X \sim \chi^2_\delta(\lambda)$, then $\mathbb{E}[e^{-wX}] = (1 + 2w)^{-\delta/2}\exp(-\lambda w/(1+2w))$ for $w > -1/2$. Since $v_T = c\,X$ where $X \sim \chi^2_\delta(\lambda)$:

$$
\mathbb{E}[e^{-w\,v_T}] = \mathbb{E}[e^{-wc\,X}] = (1 + 2cw)^{-\delta/2}\exp\!\left(-\frac{\lambda\,cw}{1+2cw}\right)
$$

$\square$

The exponential-affine form of this Laplace transform -- the exponent is linear in $v_t$ (through $\lambda$) -- is precisely the affine property that makes the Heston characteristic function tractable.

---

## Exact Sampling

The non-central chi-squared representation provides an exact (unbiased) method for sampling $v_T$ given $v_t$.

!!! tip "Algorithm: Exact CIR Sampling"
    To sample $v_T$ given $v_t$:

    1. Compute $c = \sigma_v^2(1-e^{-\kappa\tau})/(4\kappa)$
    2. Compute $\delta = 4\kappa\theta/\sigma_v^2$
    3. Compute $\lambda = v_t\,e^{-\kappa\tau}/c$
    4. Sample $X \sim \chi^2_\delta(\lambda)$ (non-central chi-squared)
    5. Set $v_T = c \cdot X$

    For the non-central chi-squared sampling in step 4, use one of:

    - **Poisson mixture**: Sample $N \sim \text{Poisson}(\lambda/2)$, then $X \sim \chi^2_{\delta + 2N}$ (central)
    - **Normal approximation** (large $\lambda$): $X \approx \delta + \lambda + \sqrt{2(\delta + 2\lambda)}\,Z$ where $Z \sim N(0,1)$
    - **Inverse CDF**: Use the non-central chi-squared CDF and its inverse

This exact sampling avoids the negative-variance problem of Euler discretization and eliminates time-discretization bias. It is used in the Broadie-Kaya (2006) exact simulation algorithm for the full Heston model, discussed in the [exact simulation section](../monte_carlo/exact_simulation_broadie_kaya.md).

---

## Worked Example: Transition Distribution

??? example "Computing the Transition Distribution"
    Parameters: $\kappa = 2.0$, $\theta = 0.04$, $\sigma_v = 0.5$, $v_t = 0.06$, $\tau = 0.5$ years.

    **Step 1: Scale parameter.**

    $$
    c = \frac{0.25(1-e^{-1.0})}{8} = \frac{0.25 \times 0.6321}{8} = 0.01975
    $$

    **Step 2: Degrees of freedom.**

    $$
    \delta = \frac{4(2)(0.04)}{0.25} = 1.28
    $$

    Since $\delta < 2$, the Feller condition is violated, and the density has a mass near zero.

    **Step 3: Non-centrality parameter.**

    $$
    \lambda = \frac{4(2)(0.06)\,e^{-1.0}}{0.25(1-e^{-1.0})} = \frac{0.48 \times 0.3679}{0.25 \times 0.6321} = \frac{0.17659}{0.15803} = 1.1174
    $$

    **Step 4: Moments.**

    $$
    \mathbb{E}[v_T \mid v_t] = c(\delta + \lambda) = 0.01975(1.28 + 1.1174) = 0.01975 \times 2.3974 = 0.04735
    $$

    This matches the direct formula $\theta + (v_t - \theta)e^{-\kappa\tau} = 0.04 + 0.02 \times 0.3679 = 0.04736$.

    $$
    \text{Var}(v_T \mid v_t) = 2c^2(\delta + 2\lambda) = 2(0.01975)^2(1.28 + 2.2349) = 2(0.000390)(3.5149) = 0.002742
    $$

    The standard deviation is $\sqrt{0.002742} \approx 0.0524$, which is comparable to the mean, indicating a highly skewed distribution.

---

## Stationary Distribution

As $\tau \to \infty$, the CIR process reaches its stationary distribution (assuming $\kappa > 0$).

!!! success "Proposition: CIR Stationary Distribution"
    The stationary distribution of the CIR process is the Gamma distribution:

    $$
    v_\infty \sim \text{Gamma}\!\left(\frac{2\kappa\theta}{\sigma_v^2},\; \frac{2\kappa}{\sigma_v^2}\right)
    $$

    with shape parameter $\alpha = 2\kappa\theta/\sigma_v^2 = \delta/2$ and rate parameter $\beta = 2\kappa/\sigma_v^2$. The mean is $\alpha/\beta = \theta$ and the variance is $\alpha/\beta^2 = \theta\sigma_v^2/(2\kappa)$.

**Proof.** As $\tau \to \infty$: $c \to \sigma_v^2/(4\kappa)$, $\lambda \to 0$. The distribution $v_T/c \to \chi^2_\delta(0) = \chi^2_\delta = \text{Gamma}(\delta/2, 1/2)$. Therefore $v_T = c \cdot (v_T/c) \to \frac{\sigma_v^2}{4\kappa}\text{Gamma}(\delta/2, 1/2) = \text{Gamma}(\delta/2, 2\kappa/\sigma_v^2)$. $\square$

---

## Summary

The CIR variance process has an explicit transition density given by a scaled non-central chi-squared distribution. The three parameters of this distribution -- the scale $c$, degrees of freedom $\delta = 4\kappa\theta/\sigma_v^2$, and non-centrality $\lambda = 4\kappa v_t e^{-\kappa\tau}/(\sigma_v^2(1-e^{-\kappa\tau}))$ -- encode the mean-reversion dynamics, the distance from the current state, and the time horizon. The Laplace transform inherits the affine structure of the CIR process, and the exact transition density enables unbiased simulation. In the long run, the process converges to a Gamma stationary distribution with mean $\theta$.

The [next section](variance_process_moments.md) derives explicit formulas for the conditional and unconditional moments of the variance process.

---
