# Non-Central Chi-Squared Distribution

The non-central chi-squared distribution appears naturally when modeling squared sums of normally distributed variables with non-zero means. This is essential in the Heston model for understanding the variance dynamics of the underlying asset.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Understand central and non-central chi-squared distributions
    2. Recognize the role of the non-centrality parameter
    3. Apply the distribution to variance process modeling in Heston

---

## Central Chi-Squared Distribution

Let \((X_1, X_2, \ldots, X_k)\) be \(k\) independent, normally distributed random variables with means \(\mu_i = 0\) and variances \(\sigma_i^2\).

The sum of squared normalized variables follows a chi-squared distribution with \(k\) degrees of freedom:

\[
\sum_{i=1}^{k} \left(\frac{X_i}{\sigma_i}\right)^2 \sim \chi^2_k
\]

The PDF of the central chi-squared distribution with \(k\) degrees of freedom is:

\[
f_{\chi^2_k}(x) = \frac{1}{2^{k/2}\Gamma(k/2)} x^{k/2-1} e^{-x/2}, \quad x > 0
\]

---

## Non-Central Chi-Squared Distribution

Now consider \((X_1, X_2, \ldots, X_k)\) with **non-zero means** \(\mu_i\) and variances \(\sigma_i^2\).

The sum of squared normalized variables follows a **non-central chi-squared distribution** with \(k\) degrees of freedom and **non-centrality parameter**:

\[
\lambda = \sum_{i=1}^{k} \left(\frac{\mu_i}{\sigma_i}\right)^2
\]

### Probability Density Function

The non-central chi-squared distribution can be expressed as a mixture of central chi-squared distributions:

\[
f(x; k, \lambda) = \sum_{i=0}^{\infty} \frac{e^{-\lambda/2}(\lambda/2)^i}{i!} f_{\chi^2(k+2i)}(x)
\]

Alternatively, using a modified Bessel function of the first kind \(I_{\nu}\):

\[
f(x; k, \lambda) = \frac{1}{2} e^{-(x+\lambda)/2} \left(\frac{x}{\lambda}\right)^{k/4-1/2} I_{k/2-1}(\sqrt{\lambda x})
\]

### Properties

- When \(\lambda = 0\), the non-central chi-squared reduces to the central chi-squared distribution.
- The mean is \(k + \lambda\).
- The variance is \(2k + 4\lambda\).
- The distribution is skewed, with skewness increasing as \(\lambda\) increases.

---

## Application to CIR Process Transitions

In the Cox–Ingersoll–Ross (CIR) process for interest rates:

\[
dr = \kappa(\bar{r} - r)dt + \gamma\sqrt{r}dW^{\mathbb{Q}}
\]

The transition distribution of \(r(T)\) conditional on \(r(t)\) follows a non-central chi-squared distribution (scaled). This is crucial for:

- Pricing zero-coupon bonds
- Computing transition probabilities
- Simulating the variance process in Heston

---

## Feller Condition and Boundary Behavior

A critical property of CIR-type processes is the **Feller condition**, which controls whether the process can reach zero:

\[
2\kappa\bar{r} \geq \gamma^2 \quad \Rightarrow \quad r(t) \text{ stays strictly positive a.s.}
\]

\[
2\kappa\bar{r} < \gamma^2 \quad \Rightarrow \quad r(t) \text{ may reach zero; probability mass accumulates at } 0
\]

When the Feller condition is violated, special care is needed in simulation and density recovery to avoid negative rates or variance values.

---

## Summary

The non-central chi-squared distribution characterizes the transition dynamics of variance processes in Heston and interest rate processes in CIR models. Understanding its properties—especially the non-centrality parameter, mean, and variance—is essential for accurate pricing and risk management of derivatives that depend on these processes.

---

## Exercises

**Exercise 1.** A non-central chi-squared random variable $X \sim \chi^2(\nu, \lambda)$ with $\nu$ degrees of freedom and non-centrality $\lambda$ has mean $\nu + \lambda$ and variance $2(\nu + 2\lambda)$. Verify these formulas for $\nu = 4$ and $\lambda = 3$.

??? success "Solution to Exercise 1"
    For $X \sim \chi^2(\nu, \lambda)$ with $\nu = 4$ and $\lambda = 3$:

    **Mean:**

    $$
    \mathbb{E}[X] = \nu + \lambda = 4 + 3 = 7
    $$

    **Variance:**

    $$
    \operatorname{Var}(X) = 2(\nu + 2\lambda) = 2(4 + 6) = 2 \times 10 = 20
    $$

    **Verification via the Poisson mixture representation:** The non-central chi-squared can be written as $X = \sum_{i=1}^{\nu} (Z_i + \mu_i)^2$ where $Z_i \sim N(0,1)$ and $\lambda = \sum \mu_i^2$. Each term $(Z_i + \mu_i)^2$ has mean $1 + \mu_i^2$ and variance $2 + 4\mu_i^2$. Summing over $\nu = 4$ terms:

    $$
    \mathbb{E}[X] = \sum_{i=1}^{4} (1 + \mu_i^2) = 4 + \sum_{i=1}^{4} \mu_i^2 = 4 + 3 = 7 \;\checkmark
    $$

    For the variance, the independence of the $Z_i$ gives:

    $$
    \operatorname{Var}(X) = \sum_{i=1}^{4} (2 + 4\mu_i^2) = 2 \times 4 + 4\sum_{i=1}^{4}\mu_i^2 = 8 + 12 = 20 \;\checkmark
    $$

    Both formulas are confirmed.

---

**Exercise 2.** For the CIR process, the scaled transition density gives $v_T/c \sim \chi^2(\delta, \lambda)$ where $\delta = 4\kappa\theta/\sigma_v^2$ and $c = \sigma_v^2(1 - e^{-\kappa\tau})/(4\kappa)$. Compute $\delta$ and $c$ for $\kappa = 2$, $\theta = 0.04$, $\sigma_v = 0.3$, $\tau = 1$.

??? success "Solution to Exercise 2"
    With $\kappa = 2$, $\theta = 0.04$, $\sigma_v = 0.3$, $\tau = 1$:

    **Degrees of freedom:**

    $$
    \delta = \frac{4\kappa\theta}{\sigma_v^2} = \frac{4 \times 2 \times 0.04}{0.09} = \frac{0.32}{0.09} = 3.556
    $$

    **Scale parameter:**

    $$
    c = \frac{\sigma_v^2(1 - e^{-\kappa\tau})}{4\kappa} = \frac{0.09(1 - e^{-2})}{8} = \frac{0.09 \times 0.8647}{8} = \frac{0.07782}{8} = 0.009728
    $$

    Since $\delta = 3.556 > 2$, the Feller condition is satisfied ($2\kappa\theta = 0.16 > 0.09 = \sigma_v^2$), and the chi-squared density is zero at the origin, ensuring $v_T > 0$ almost surely.

    The transition distribution of $v_T/c$ is $\chi^2(3.556, \lambda)$ where $\lambda$ depends on the current variance $v_t$. The scale $c = 0.009728$ converts from the chi-squared scale to the variance scale.

---

**Exercise 3.** The non-central chi-squared CDF can be computed as a mixture of central chi-squared CDFs: $F_{\chi^2(\nu,\lambda)}(x) = \sum_{k=0}^\infty \frac{e^{-\lambda/2}(\lambda/2)^k}{k!} F_{\chi^2(\nu+2k)}(x)$. Explain why this is a Poisson-weighted sum and relate the Poisson parameter $\lambda/2$ to the CIR non-centrality.

??? success "Solution to Exercise 3"
    The non-central chi-squared CDF as a Poisson mixture is:

    $$
    F_{\chi^2(\nu,\lambda)}(x) = \sum_{k=0}^{\infty} \frac{e^{-\lambda/2}(\lambda/2)^k}{k!}\,F_{\chi^2(\nu+2k)}(x)
    $$

    **Why this is a Poisson-weighted sum:** The weights $w_k = \frac{e^{-\lambda/2}(\lambda/2)^k}{k!}$ are exactly the probability mass function of a Poisson random variable $N \sim \text{Poisson}(\lambda/2)$, evaluated at $k$. These weights are non-negative and sum to one: $\sum_{k=0}^\infty w_k = 1$. Therefore the non-central chi-squared CDF is a mixture (convex combination) of central chi-squared CDFs with degrees of freedom $\nu, \nu+2, \nu+4, \ldots$

    This representation has a constructive interpretation: to sample $X \sim \chi^2(\nu, \lambda)$:

    1. First sample $N \sim \text{Poisson}(\lambda/2)$
    2. Then sample $X \sim \chi^2(\nu + 2N)$ (a central chi-squared with random degrees of freedom)

    **Relation to the CIR non-centrality:** For the CIR process, the non-centrality parameter is:

    $$
    \lambda = \frac{4\kappa\,v_t\,e^{-\kappa\tau}}{\sigma_v^2(1 - e^{-\kappa\tau})}
    $$

    The Poisson parameter is $\lambda/2$, which is proportional to $v_t\,e^{-\kappa\tau}$ -- the "memory" of the initial condition decayed by mean reversion. When $v_t$ is large, $\lambda/2$ is large, and the Poisson distribution has a large mean, meaning the random degrees of freedom $\nu + 2N$ is typically much larger than $\nu$. This shifts the chi-squared distribution to the right, reflecting the fact that a higher starting variance produces a higher conditional variance. As $\tau \to \infty$, $\lambda \to 0$, $N \to 0$ a.s., and the distribution reduces to the central $\chi^2_\nu$ -- the stationary (Gamma) distribution.

---

**Exercise 4.** When $\delta < 2$ (Feller condition violated), the density $f_{\chi^2(\delta, \lambda)}(x)$ has a singularity at $x = 0$. Explain the physical meaning: for the variance process, this means there is positive probability of $V_T$ being exactly zero. How does the non-centrality $\lambda$ (which depends on $v_t$) affect this probability?

??? success "Solution to Exercise 4"
    When $\delta < 2$ (Feller condition violated), the density $f_{\chi^2(\delta, \lambda)}(x)$ has a singularity at $x = 0$. Specifically, as $x \to 0^+$:

    $$
    f_{\chi^2(\delta, \lambda)}(x) \propto x^{\delta/2 - 1}
    $$

    For $\delta < 2$, the exponent $\delta/2 - 1 < 0$, so the density diverges as $x \to 0$.

    **Physical meaning for the variance process:** Since $v_T = c \cdot X$ where $X \sim \chi^2(\delta, \lambda)$, the density of $v_T$ near zero is:

    $$
    f_{v_T}(v) = \frac{1}{c} f_{\chi^2(\delta,\lambda)}\!\left(\frac{v}{c}\right) \propto v^{\delta/2 - 1}
    $$

    This means there is significant probability mass concentrated near $v_T = 0$. The variance process can reach (or come arbitrarily close to) zero, which corresponds to the instantaneous volatility $\sqrt{v_T}$ approaching zero.

    **Effect of the non-centrality parameter $\lambda$:** The non-centrality $\lambda$ is proportional to $v_t\,e^{-\kappa\tau}$. A larger $\lambda$ shifts the chi-squared distribution to the right, away from zero. This means:

    - When $v_t$ is large (current variance is high), $\lambda$ is large, and $\mathbb{P}(v_T \approx 0)$ is small -- the process is far from the boundary.
    - When $v_t$ is small (current variance is already near zero), $\lambda$ is small, and $\mathbb{P}(v_T \approx 0)$ is significant.
    - As $\tau$ increases, $\lambda$ decreases (the exponential decay $e^{-\kappa\tau}$ shrinks the non-centrality), so the process has more time to wander toward zero, increasing $\mathbb{P}(v_T \approx 0)$.

    In the extreme $\tau \to \infty$, $\lambda \to 0$ and the distribution becomes $\chi^2_\delta(0)$, which for $\delta < 2$ has the maximum concentration of probability near zero (but still with $\mathbb{E}[v_\infty] = \theta > 0$). The boundary at zero is *accessible but instantaneously reflecting*: the process touches zero but immediately bounces back due to the positive drift $\kappa\theta > 0$.

---

**Exercise 5.** To sample from a non-central chi-squared distribution, one common method uses $\chi^2(\nu, \lambda) = \chi^2(\nu - 1) + (Z + \sqrt{\lambda})^2$ where $Z \sim N(0,1)$ and $\chi^2(\nu-1)$ is central chi-squared (valid for $\nu \geq 1$). Describe the steps to generate a sample of $v_T$ given $v_t$ using this decomposition.

??? success "Solution to Exercise 5"
    Given $v_t$, to sample $v_T$ using the decomposition $\chi^2(\nu, \lambda) = \chi^2(\nu - 1) + (Z + \sqrt{\lambda})^2$ where $Z \sim N(0,1)$ (valid for $\nu \geq 1$):

    **Step 1: Compute the CIR transition parameters.**

    $$
    c = \frac{\sigma_v^2(1 - e^{-\kappa\tau})}{4\kappa}, \qquad \delta = \frac{4\kappa\theta}{\sigma_v^2}, \qquad \lambda = \frac{4\kappa\,v_t\,e^{-\kappa\tau}}{\sigma_v^2(1 - e^{-\kappa\tau})}
    $$

    **Step 2: Sample a standard normal.** Draw $Z \sim N(0,1)$.

    **Step 3: Compute the non-central component.** Compute $(Z + \sqrt{\lambda})^2$. This is a non-central chi-squared with 1 degree of freedom and non-centrality $\lambda$.

    **Step 4: Sample the central chi-squared component.** Draw $Y \sim \chi^2(\delta - 1)$, which is a central chi-squared with $\delta - 1$ degrees of freedom. If $\delta - 1$ is not an integer, use a Gamma random variable: $Y \sim \text{Gamma}((\delta-1)/2, 1/2)$, since $\chi^2_k = \text{Gamma}(k/2, 1/2)$ for any $k > 0$.

    **Step 5: Combine.** The non-central chi-squared sample is:

    $$
    X = Y + (Z + \sqrt{\lambda})^2
    $$

    **Step 6: Scale to get $v_T$.** Set $v_T = c \cdot X$.

    **Important caveat:** This decomposition requires $\delta \geq 1$ (so that $\delta - 1 \geq 0$ and the central chi-squared is well-defined). When $\delta < 1$ (severe Feller violation), the Poisson mixture method must be used instead: draw $N \sim \text{Poisson}(\lambda/2)$, then $X \sim \chi^2(\delta + 2N)$.

---

**Exercise 6.** Compare the computational cost of exact sampling from the non-central chi-squared distribution versus Euler discretization with $N$ time steps. For what values of $N$ does exact sampling become preferable?

??? success "Solution to Exercise 6"
    **Exact sampling (non-central chi-squared) cost per step:**

    - Compute three parameters $c$, $\delta$, $\lambda$: $O(1)$
    - Sample from the non-central chi-squared: this involves sampling one $N(0,1)$, one $\text{Gamma}$ random variable, and a few arithmetic operations. Total cost: $O(1)$ per time step (a constant, roughly equivalent to 3--5 uniform random number generations plus special function evaluations)

    For a single step from $v_t$ to $v_T$, exact sampling costs $O(1)$ and produces a sample from the *exact* transition distribution with zero discretization error.

    **Euler discretization cost for $N$ steps:**

    - Each step requires: one $N(0,1)$ sample, a few multiplications and additions. Cost per step: $O(1)$
    - Total cost for $N$ steps: $O(N)$
    - Discretization bias: $O(\Delta t) = O(\tau/N)$ (weak convergence order 1 for standard Euler, though the square-root diffusion can reduce this to order $1/2$ near zero)

    **Comparison:**

    | Method | Cost | Bias | Risk of negative $v$ |
    |:---|:---:|:---:|:---:|
    | Exact (NCX2) | $O(1)$ | $0$ | None |
    | Euler ($N$ steps) | $O(N)$ | $O(\tau/N)$ | Yes, needs fixing |

    Exact sampling is preferable as soon as $N > 1$. Even for $N = 1$ (a single Euler step), the exact method is comparable in cost but has zero bias and no negative-variance problem. The only situation where Euler discretization might be preferred is when the full path $\{v_{t_1}, v_{t_2}, \ldots, v_{t_N}\}$ is needed at intermediate times (e.g., for path-dependent payoffs), since exact sampling gives only the terminal value $v_T$. However, for generating the full path, one can apply exact sampling iteratively at each time step, achieving $O(N)$ cost with zero discretization error at each step -- strictly dominating Euler in accuracy for the same computational cost.

    In practice, exact sampling becomes clearly preferable for $N \geq 5$--$10$, where the accumulated Euler bias and the need for negative-variance corrections make the approximate scheme unreliable, especially when $\delta < 2$ (Feller condition violated).
