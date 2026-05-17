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

with $\kappa > 0$, $\theta > 0$, $\sigma_v > 0$, and $v_0 > 0$. Recall (see [§ CIR short-rate model](../../ch18/cir_model/bond_options.md)) the same SDE was originally proposed by Cox-Ingersoll-Ross (1985) for the short rate; affine-class membership is treated in [§ Vasicek/CIR as affine](../../ch15/examples/vasicek_cir_as_affine.md).

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

## Exercises

**Exercise 1.** For CIR parameters $\kappa = 2$, $\theta = 0.04$, $\sigma_v = 0.3$, $v_0 = 0.06$, and $\tau = 1$, compute the non-central chi-squared parameters: scale $c$, degrees of freedom $\delta = 4\kappa\theta/\sigma_v^2$, and non-centrality $\lambda = 4\kappa v_0 e^{-\kappa\tau}/(\sigma_v^2(1 - e^{-\kappa\tau}))$.

??? success "Solution to Exercise 1"
    We are given $\kappa = 2$, $\theta = 0.04$, $\sigma_v = 0.3$, $v_0 = 0.06$, and $\tau = 1$.

    **Scale parameter:**

    $$
    c = \frac{\sigma_v^2(1 - e^{-\kappa\tau})}{4\kappa} = \frac{0.09(1 - e^{-2})}{8} = \frac{0.09 \times 0.8647}{8} = \frac{0.07782}{8} = 0.009728
    $$

    **Degrees of freedom:**

    $$
    \delta = \frac{4\kappa\theta}{\sigma_v^2} = \frac{4 \times 2 \times 0.04}{0.09} = \frac{0.32}{0.09} = 3.556
    $$

    Since $\delta > 2$, the Feller condition $2\kappa\theta \geq \sigma_v^2$ is satisfied ($0.16 > 0.09$), and the variance process remains strictly positive.

    **Non-centrality parameter:**

    $$
    \lambda = \frac{4\kappa v_0 e^{-\kappa\tau}}{\sigma_v^2(1 - e^{-\kappa\tau})} = \frac{4 \times 2 \times 0.06 \times e^{-2}}{0.09 \times (1 - e^{-2})} = \frac{0.48 \times 0.1353}{0.09 \times 0.8647} = \frac{0.06495}{0.07782} = 0.8346
    $$

    The transition distribution is therefore $v_T \mid v_0 \sim \frac{c}{2}\,\chi^2_{3.556}(0.8346)$, or equivalently $v_T/c \sim \chi^2_{3.556}(0.8346)$.

---

**Exercise 2.** Using the parameters from Exercise 1, compute $\mathbb{E}[v_T \mid v_0]$ using both the direct formula $\theta + (v_0 - \theta)e^{-\kappa\tau}$ and the non-central chi-squared mean formula $c(\delta + \lambda)$. Verify they agree.

??? success "Solution to Exercise 2"
    Using the parameters from Exercise 1: $\kappa = 2$, $\theta = 0.04$, $v_0 = 0.06$, $\tau = 1$.

    **Method 1: Direct formula.**

    $$
    \mathbb{E}[v_T \mid v_0] = \theta + (v_0 - \theta)e^{-\kappa\tau} = 0.04 + (0.06 - 0.04)e^{-2} = 0.04 + 0.02 \times 0.1353 = 0.04 + 0.002707 = 0.04271
    $$

    **Method 2: Non-central chi-squared mean formula.**

    The mean of $\chi^2_\delta(\lambda)$ is $\delta + \lambda$, and $v_T = c \cdot X$ where $X \sim \chi^2_\delta(\lambda)$, so:

    $$
    \mathbb{E}[v_T \mid v_0] = c(\delta + \lambda) = 0.009728 \times (3.556 + 0.8346) = 0.009728 \times 4.390 = 0.04271
    $$

    The two methods agree: $\mathbb{E}[v_T \mid v_0] = 0.04271$. This is between $v_0 = 0.06$ and $\theta = 0.04$, consistent with mean reversion pulling the elevated variance back toward the long-run level over one year.

---

**Exercise 3.** The Laplace transform of the CIR transition density is $\mathbb{E}[e^{-uv_T} \mid v_t] = \exp(\tilde{\phi}(\tau, -u) + \tilde{\psi}(\tau, -u)v_t)$. For bond pricing ($u = 1$, $v = r$), relate this to the zero-coupon bond price formula.

??? success "Solution to Exercise 3"
    The Laplace transform of the CIR process using the non-central chi-squared representation is:

    $$
    \mathbb{E}\!\left[e^{-u\,v_T} \,\middle|\, v_t\right] = \left(\frac{1}{1 + 2cu}\right)^{\delta/2} \exp\!\left(-\frac{\lambda\,cu}{1 + 2cu}\right)
    $$

    For a zero-coupon bond price in the CIR interest rate model, the short rate $r_t$ replaces $v_t$, and the bond price is:

    $$
    P(t,T) = \mathbb{E}^{\mathbb{Q}}\!\left[\exp\!\left(-\int_t^T r_s\,ds\right) \,\middle|\, r_t\right]
    $$

    This is *not* the same as $\mathbb{E}[e^{-r_T}|r_t]$ (which sets $u = 1$ for the terminal value). However, the affine structure of the CIR process ensures that the bond price also has an exponential-affine form:

    $$
    P(t,T) = \exp\!\left(A(\tau) - B(\tau)\,r_t\right)
    $$

    where $A(\tau)$ and $B(\tau)$ satisfy Riccati ODEs. The function $B(\tau)$ satisfies:

    $$
    B(\tau) = \frac{2(e^{\gamma\tau} - 1)}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}
    $$

    with $\gamma = \sqrt{\kappa^2 + 2\sigma_v^2}$, and $A(\tau)$ is:

    $$
    A(\tau) = \frac{2\kappa\theta}{\sigma_v^2}\ln\!\left(\frac{2\gamma\,e^{(\kappa + \gamma)\tau/2}}{(\gamma + \kappa)(e^{\gamma\tau} - 1) + 2\gamma}\right)
    $$

    The connection is that both the Laplace transform of $v_T$ and the bond price exploit the affine property: the exponent is always of the form $\alpha(\tau) + \beta(\tau)v_t$ (linear in $v_t$). For the Laplace transform at the terminal point ($u = 1$), we get the conditional moment generating function evaluated at $-1$. For the bond price, the integrated exponential functional leads to the Riccati system. Both are consequences of the same affine structure of the CIR diffusion.

---

**Exercise 4.** Describe the Broadie-Kaya exact simulation algorithm for the CIR process. What is the key step that requires sampling from a non-central chi-squared distribution, and why does this produce unbiased samples?

??? success "Solution to Exercise 4"
    The Broadie-Kaya (2006) exact simulation algorithm for the CIR variance process proceeds as follows:

    **Step 1.** Given the current variance $v_t$ at time $t$, compute the non-central chi-squared parameters for time $T = t + \Delta t$:

    - Scale: $c = \sigma_v^2(1 - e^{-\kappa\Delta t})/(4\kappa)$
    - Degrees of freedom: $\delta = 4\kappa\theta/\sigma_v^2$
    - Non-centrality: $\lambda = 4\kappa v_t e^{-\kappa\Delta t}/(\sigma_v^2(1 - e^{-\kappa\Delta t}))$

    **Step 2.** Sample $X \sim \chi^2_\delta(\lambda)$ from the non-central chi-squared distribution. This is the key step. One standard approach:

    - If $\delta > 1$: Sample $Z \sim N(0,1)$ and $Y \sim \chi^2_{\delta-1}$ (central chi-squared). Then $X = (Z + \sqrt{\lambda})^2 + Y$.
    - If $\delta \leq 1$: Sample $N \sim \text{Poisson}(\lambda/2)$, then $X \sim \chi^2_{\delta + 2N}$ (central chi-squared with random degrees of freedom).

    **Step 3.** Set $v_T = c \cdot X$.

    **Why this is unbiased:** The non-central chi-squared distribution is the *exact* conditional distribution of $v_T/c$ given $v_t$. Every sample drawn from this distribution is a draw from the true transition kernel of the CIR process. There is no time-discretization error because we are sampling from the exact solution, not from a discrete-time approximation. By contrast, Euler discretization introduces bias of order $O(\Delta t)$ and can produce negative variance values, requiring ad hoc corrections (such as absorption or reflection at zero) that distort the distribution.

    The exact sampling approach guarantees that the marginal distribution at each time step is correct, regardless of the step size $\Delta t$. This is particularly valuable for long time steps and for processes near the Feller boundary where Euler schemes are unreliable.

---

**Exercise 5.** As $\tau \to \infty$, the CIR process converges to a Gamma stationary distribution. Compute the shape parameter $\alpha = 2\kappa\theta/\sigma_v^2$ and rate parameter $\beta = 2\kappa/\sigma_v^2$ for the parameters in Exercise 1. What is the stationary mean and variance?

??? success "Solution to Exercise 5"
    Using $\kappa = 2$, $\theta = 0.04$, $\sigma_v = 0.3$:

    **Shape parameter:**

    $$
    \alpha = \frac{2\kappa\theta}{\sigma_v^2} = \frac{2 \times 2 \times 0.04}{0.09} = \frac{0.16}{0.09} = 1.778
    $$

    **Rate parameter:**

    $$
    \beta = \frac{2\kappa}{\sigma_v^2} = \frac{4}{0.09} = 44.44
    $$

    So the stationary distribution is $v_\infty \sim \text{Gamma}(1.778, 44.44)$.

    **Stationary mean:**

    $$
    \mathbb{E}[v_\infty] = \frac{\alpha}{\beta} = \frac{1.778}{44.44} = 0.04 = \theta
    $$

    **Stationary variance:**

    $$
    \text{Var}(v_\infty) = \frac{\alpha}{\beta^2} = \frac{1.778}{1975.1} = 0.0009003
    $$

    Equivalently, using the direct formula:

    $$
    \text{Var}(v_\infty) = \frac{\theta\sigma_v^2}{2\kappa} = \frac{0.04 \times 0.09}{4} = 0.0009
    $$

    The stationary standard deviation is $\sqrt{0.0009} = 0.03$, which is 75% of the mean (coefficient of variation = 0.75). This indicates substantial variability in the long-run variance.

    Note that since $\delta = 2\alpha = 3.556 > 2$, the Feller condition is satisfied, confirming that the process remains strictly positive in the stationary regime.

---

**Exercise 6.** When the Feller condition is violated ($\delta < 2$), the non-central chi-squared distribution has a point mass at zero. For $\kappa = 1$, $\theta = 0.02$, $\sigma_v = 0.5$, compute $\delta$ and explain why $\mathbb{P}(v_T = 0 \mid v_0) > 0$ for sufficiently large $T$.

??? success "Solution to Exercise 6"
    For $\kappa = 1$, $\theta = 0.02$, $\sigma_v = 0.5$:

    **Degrees of freedom:**

    $$
    \delta = \frac{4\kappa\theta}{\sigma_v^2} = \frac{4 \times 1 \times 0.02}{0.25} = \frac{0.08}{0.25} = 0.32
    $$

    **Feller condition check:** The Feller condition requires $2\kappa\theta \geq \sigma_v^2$, i.e., $0.04 \geq 0.25$, which is clearly violated. The Feller ratio is $2\kappa\theta/\sigma_v^2 = 0.16 \ll 1$.

    **Why $\mathbb{P}(v_T = 0 \mid v_0) > 0$ for large $T$:** When $\delta < 2$, the non-central chi-squared density $f_{\chi^2_\delta(\lambda)}(x)$ has a singularity at $x = 0$. More precisely, for $\delta < 1$ (as in this case with $\delta = 0.32$), the density diverges as $x \to 0^+$, and the CDF satisfies $F_{\chi^2_\delta(\lambda)}(0) > 0$ when $\lambda > 0$ (via the Poisson mixture representation, the $k=0$ term contributes $e^{-\lambda/2}F_{\chi^2_\delta}(0)$, and for $\delta < 2$, $\chi^2_\delta$ has positive mass near zero).

    As $T \to \infty$, the non-centrality parameter $\lambda = 4\kappa v_0 e^{-\kappa T}/(\sigma_v^2(1 - e^{-\kappa T})) \to 0$. In this limit, $v_T/c \to \chi^2_\delta(0) = \chi^2_\delta$, which is a central chi-squared with $\delta = 0.32$ degrees of freedom. For the central $\chi^2_\delta$ with $\delta < 1$, the density diverges at zero as $x^{\delta/2 - 1} = x^{-0.84}$, concentrating significant probability mass near zero.

    Physically, this means the vol-of-vol $\sigma_v$ is large relative to the mean-reverting drift near zero. Near $v = 0$, the drift is $\kappa\theta = 0.02$ (pulling away from zero), but the diffusion coefficient is $\sigma_v\sqrt{v}$, which, although it vanishes at zero, is large enough relative to the drift for small $v$ (when $\delta < 2$) that the process can reach the boundary. Once at zero, the process immediately reflects back (since $\kappa\theta > 0$), but the boundary is accessible. In simulation, this requires special handling to ensure the non-negativity constraint is maintained.
