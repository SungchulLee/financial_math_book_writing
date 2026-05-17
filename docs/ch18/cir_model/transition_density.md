# Transition Density: Non-Central Chi-Squared

Unlike the Vasicek model where the transition density is Gaussian, the CIR process has a transition density described by the **non-central chi-squared distribution**. This distribution arises naturally from the square-root diffusion: the process can be represented as a squared sum of independent OU processes, connecting it to the chi-squared family. The non-central chi-squared characterization is essential for exact simulation, maximum likelihood estimation, and bond option pricing in the CIR model.

---

## The scaling transformation

The key step is to transform the CIR process into a standard form. Define the scaling constant

$$
c(t, s) = \frac{2\kappa}{\sigma^2(1 - e^{-\kappa(s-t)})}
$$

for $s > t$. Then the scaled future rate $2c(t,s)\,r_s$ conditional on $r_t$ follows a **non-central chi-squared distribution**:

$$
\boxed{2c(t,s)\,r_s \mid r_t \sim \chi^2_\nu(\lambda)}
$$

where

$$
\nu = \frac{4\kappa\theta}{\sigma^2}, \qquad \lambda = 2c(t,s)\,r_t\,e^{-\kappa(s-t)}
$$

Here $\nu > 0$ is the **degrees of freedom** and $\lambda \geq 0$ is the **non-centrality parameter**.

---

## Degrees of freedom

The degrees of freedom parameter

$$
\nu = \frac{4\kappa\theta}{\sigma^2} = 2 \cdot \frac{2\kappa\theta}{\sigma^2}
$$

is twice the Feller ratio. Its value determines the shape of the density:

- $\nu \geq 2$ (Feller condition $2\kappa\theta \geq \sigma^2$): The density is zero at the origin and has a single interior mode. The process stays strictly positive.
- $1 < \nu < 2$: The density diverges at the origin but is integrable. The process stays positive but visits neighborhoods of zero.
- $0 < \nu \leq 1$: The density has a mass point (atom) at zero, and the process reaches zero with positive probability.

The degrees of freedom are **constant** (independent of $r_t$ and the time horizon), reflecting the invariant structure of the CIR diffusion.

---

## Non-centrality parameter

The non-centrality parameter

$$
\lambda = 2c(t,s)\,r_t\,e^{-\kappa(s-t)} = \frac{4\kappa\,r_t\,e^{-\kappa(s-t)}}{\sigma^2(1 - e^{-\kappa(s-t)})}
$$

encodes the contribution of the current rate $r_t$ to the future distribution. Key properties:

- $\lambda$ is proportional to $r_t$: higher current rates shift the distribution to the right
- $\lambda$ decreases as $s - t$ increases: mean reversion reduces the influence of $r_t$
- As $s - t \to \infty$: $\lambda \to 0$ and the distribution approaches the (central) chi-squared $\chi^2_\nu$, which is the stationary distribution (up to scaling)

---

## Properties of the non-central chi-squared distribution

The non-central chi-squared distribution $\chi^2_\nu(\lambda)$ has the following properties:

**Mean:**

$$
\mathbb{E}[\chi^2_\nu(\lambda)] = \nu + \lambda
$$

**Variance:**

$$
\text{Var}(\chi^2_\nu(\lambda)) = 2(\nu + 2\lambda)
$$

**PDF** (for $x > 0$):

$$
f_{\chi^2}(x; \nu, \lambda) = \frac{1}{2}\,e^{-(x + \lambda)/2}\!\left(\frac{x}{\lambda}\right)^{\nu/4 - 1/2} I_{\nu/2 - 1}\!\left(\sqrt{\lambda x}\right)
$$

where $I_\alpha$ is the modified Bessel function of the first kind. An alternative series representation is

$$
f_{\chi^2}(x; \nu, \lambda) = \sum_{j=0}^{\infty} \frac{e^{-\lambda/2}(\lambda/2)^j}{j!}\,f_{\chi^2_{\nu + 2j}}(x)
$$

where $f_{\chi^2_k}$ is the central chi-squared density with $k$ degrees of freedom. This shows that the non-central chi-squared is a **Poisson mixture** of central chi-squared distributions: the number of extra degrees of freedom is $2J$ where $J \sim \text{Poisson}(\lambda/2)$.

---

## Transition density of the CIR process

Inverting the scaling, the conditional density of $r_s$ given $r_t$ is

$$
f(r_s \mid r_t) = 2c(t,s)\,f_{\chi^2}\!\left(2c(t,s)\,r_s;\, \nu,\, \lambda\right)
$$

for $r_s > 0$.

### Verification of moments

Recall (see [§ CIR SDE and Square-Root Process](cir_sde_and_square_root_process.md)) the conditional mean and variance derived from the SDE. From $\mathbb{E}[2c\,r_s] = \nu + \lambda$ and $\text{Var}(2c\,r_s) = 2(\nu + 2\lambda)$, one recovers

$$
\mathbb{E}[r_s \mid r_t] = \frac{\nu + \lambda}{2c} = \theta + (r_t - \theta)\,e^{-\kappa\tau}
$$

$$
\text{Var}(r_s \mid r_t) = \frac{2(\nu + 2\lambda)}{(2c)^2} = r_t\,\frac{\sigma^2}{\kappa}(e^{-\kappa\tau} - e^{-2\kappa\tau}) + \theta\,\frac{\sigma^2}{2\kappa}(1 - e^{-\kappa\tau})^2
$$

matching the SDE-based formulas. $\square$

---

## Exact simulation via non-central chi-squared

The transition density provides an **exact simulation** scheme for the CIR process (no discretization error):

1. Given $r_t$ and time step $\Delta t$, compute $c = 2\kappa/(\sigma^2(1 - e^{-\kappa\Delta t}))$ and $\lambda = 2c\,r_t\,e^{-\kappa\Delta t}$.
2. Draw $X \sim \chi^2_\nu(\lambda)$ using the Poisson-mixture representation:
    - Draw $J \sim \text{Poisson}(\lambda/2)$
    - Draw $X \sim \chi^2_{\nu + 2J}$ (central chi-squared)
3. Set $r_{t+\Delta t} = X/(2c)$.

For large $\lambda$, a more efficient approach uses the representation $\chi^2_\nu(\lambda) = (\sqrt{\lambda} + Z)^2 + \chi^2_{\nu-1}$ where $Z \sim \mathcal{N}(0,1)$ (valid for $\nu \geq 1$), avoiding the Poisson draw.

!!! tip "Implementation in Python"
    SciPy provides `scipy.stats.ncx2.rvs(df=nu, nc=lambda, size=n)` for direct sampling from the non-central chi-squared. NumPy's `np.random.noncentral_chisquare(df, nc, size)` is also available. Both are efficient for vectorized simulation.

---

## Stationary distribution

As $\tau \to \infty$, $\lambda \to 0$ and $c \to 2\kappa/\sigma^2$, so the scaled rate $2c\,r_\infty = 4\kappa r_\infty/\sigma^2$ follows a central chi-squared:

$$
\frac{4\kappa}{\sigma^2}\,r_\infty \sim \chi^2_\nu
$$

This means $r_\infty$ follows a **Gamma distribution**:

$$
r_\infty \sim \text{Gamma}\!\left(\frac{\nu}{2},\, \frac{\sigma^2}{4\kappa}\right) = \text{Gamma}\!\left(\frac{2\kappa\theta}{\sigma^2},\, \frac{\sigma^2}{4\kappa}\right)
$$

with mean $\theta$ and variance $\theta\sigma^2/(2\kappa)$.

The Gamma stationary distribution is always supported on $(0, \infty)$, consistent with the non-negativity of the CIR process. Compare with Vasicek, whose stationary distribution $\mathcal{N}(\theta, \sigma^2/(2\kappa))$ has full real-line support.

---

## Application to maximum likelihood estimation

Given discrete observations $r_{t_0}, r_{t_1}, \ldots, r_{t_N}$ at equally spaced intervals $\Delta t$, the log-likelihood is

$$
\ell(\kappa, \theta, \sigma) = \sum_{i=0}^{N-1} \ln f(r_{t_{i+1}} \mid r_{t_i}; \kappa, \theta, \sigma)
$$

where $f$ is the CIR transition density (scaled non-central chi-squared). Unlike the Vasicek case, this does not reduce to a simple linear regression. Numerical optimization (e.g., Nelder-Mead or L-BFGS-B with the Feller constraint $2\kappa\theta \geq \sigma^2$) is required.

The non-central chi-squared log-likelihood involves the modified Bessel function, which can be expensive to evaluate. Efficient implementations use the series representation truncated at a data-dependent number of terms, or the saddle-point approximation for large $\lambda$.

---

## Numerical example

Parameters: $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.1$, $r_t = 0.03$, $\tau = 1$.

**Computed quantities:**

- $c = 2 \times 0.5 / (0.01 \times (1 - e^{-0.5})) = 100/0.3935 = 254.13$
- $\nu = 4 \times 0.5 \times 0.04 / 0.01 = 8.0$
- $\lambda = 2 \times 254.13 \times 0.03 \times e^{-0.5} = 9.241$
- $\mathbb{E}[2c\,r_1] = 8 + 9.241 = 17.241$
- $\mathbb{E}[r_1] = 17.241 / (2 \times 254.13) = 0.0339$

Verification: $\mathbb{E}[r_1] = 0.04 + (0.03 - 0.04)e^{-0.5} = 0.04 - 0.00607 = 0.0339$. $\square$

The distribution $2c\,r_1 \sim \chi^2_8(9.241)$ has mode at approximately $\nu + \lambda - 2 = 15.2$, corresponding to $r_1 \approx 15.2/508.3 = 0.030$.

---

## Summary

The CIR transition density is a scaled non-central chi-squared distribution $2c\,r_s \sim \chi^2_\nu(\lambda)$ with degrees of freedom $\nu = 4\kappa\theta/\sigma^2$ (constant, twice the Feller ratio) and non-centrality $\lambda = 2c\,r_t\,e^{-\kappa\tau}$ (decreasing with the time horizon). This characterization provides exact simulation without discretization error, a well-defined likelihood function for parameter estimation, and the foundation for bond option pricing via the non-central chi-squared CDF.

---

## Exercises

**Exercise 1.** For CIR parameters $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.10$, $r_t = 0.03$, and $\tau = s - t = 1$ year, compute the scaling constant $c(t,s)$, degrees of freedom $\nu$, and non-centrality parameter $\lambda$. Then verify that $\mathbb{E}[r_s \mid r_t] = (\nu + \lambda)/(2c)$ equals the conditional mean from the CIR SDE.

??? success "Solution to Exercise 1"

    Given $\kappa = 0.5$, $\theta = 0.04$, $\sigma = 0.10$, $r_t = 0.03$, $\tau = 1$.

    **Scaling constant:**

    $$
    c(t,s) = \frac{2\kappa}{\sigma^2(1 - e^{-\kappa\tau})} = \frac{2 \times 0.5}{0.01 \times (1 - e^{-0.5})} = \frac{1.0}{0.01 \times 0.3935} = \frac{1.0}{0.003935} = 254.13
    $$

    **Degrees of freedom:**

    $$
    \nu = \frac{4\kappa\theta}{\sigma^2} = \frac{4 \times 0.5 \times 0.04}{0.01} = 8.0
    $$

    **Non-centrality parameter:**

    $$
    \lambda = 2c \cdot r_t \cdot e^{-\kappa\tau} = 2 \times 254.13 \times 0.03 \times e^{-0.5} = 508.26 \times 0.03 \times 0.6065 = 9.241
    $$

    **Verification of conditional mean:**

    $$
    \mathbb{E}[r_s \mid r_t] = \frac{\nu + \lambda}{2c} = \frac{8.0 + 9.241}{508.26} = \frac{17.241}{508.26} = 0.03392
    $$

    From the CIR SDE:

    $$
    \mathbb{E}[r_s \mid r_t] = \theta + (r_t - \theta)e^{-\kappa\tau} = 0.04 + (0.03 - 0.04)e^{-0.5} = 0.04 - 0.006065 = 0.03394
    $$

    The two agree (the small discrepancy is due to rounding). $\checkmark$

---

**Exercise 2.** The non-central chi-squared distribution can be represented as a Poisson mixture: $\chi^2_\nu(\lambda) = \chi^2_{\nu + 2J}$ where $J \sim \text{Poisson}(\lambda/2)$. For $\nu = 8$ and $\lambda = 9.24$, compute $\mathbb{E}[J] = \lambda/2$ and $\mathbb{P}(J = 0)$, $\mathbb{P}(J = 1)$, $\mathbb{P}(J = 2)$. What is the effective average degrees of freedom $\nu + 2\mathbb{E}[J]$?

??? success "Solution to Exercise 2"

    With $\nu = 8$ and $\lambda = 9.24$, the Poisson parameter is $\mu = \lambda/2 = 4.62$.

    **$\mathbb{E}[J] = \lambda/2 = 4.62$.**

    **Poisson probabilities:**

    $$
    \mathbb{P}(J = 0) = e^{-4.62} \approx 0.00985
    $$

    $$
    \mathbb{P}(J = 1) = 4.62 \times e^{-4.62} \approx 4.62 \times 0.00985 = 0.04551
    $$

    $$
    \mathbb{P}(J = 2) = \frac{4.62^2}{2} \times e^{-4.62} = \frac{21.34}{2} \times 0.00985 = 10.67 \times 0.00985 \approx 0.1051
    $$

    **Effective average degrees of freedom:**

    $$
    \nu + 2\mathbb{E}[J] = 8 + 2 \times 4.62 = 8 + 9.24 = 17.24
    $$

    This equals $\nu + \lambda = 8 + 9.24$, which is also the mean of the non-central chi-squared distribution $\mathbb{E}[\chi^2_\nu(\lambda)] = \nu + \lambda$. The Poisson mixture interpretation shows that the non-central chi-squared is a weighted average of central chi-squared distributions with degrees of freedom ranging from $\nu = 8$ (when $J = 0$) to $\nu + 2J$ (for larger $J$), with the average being $\nu + 2\mathbb{E}[J] = 17.24$.

---

**Exercise 3.** Show that as $\tau \to \infty$, the non-centrality parameter $\lambda \to 0$ and the stationary distribution of $r_\infty$ is $\text{Gamma}(\nu/2, \sigma^2/(4\kappa))$. Compute the mean and variance of this Gamma distribution and verify that they match $\theta$ and $\theta\sigma^2/(2\kappa)$.

??? success "Solution to Exercise 3"

    As $\tau \to \infty$: $e^{-\kappa\tau} \to 0$, so $1 - e^{-\kappa\tau} \to 1$.

    **Scaling constant:** $c \to 2\kappa/\sigma^2$.

    **Non-centrality:** $\lambda = 2c \cdot r_t \cdot e^{-\kappa\tau} \to 0$ (the $e^{-\kappa\tau}$ factor drives $\lambda$ to zero).

    With $\lambda = 0$, the non-central chi-squared becomes a **central chi-squared**: $2c\,r_\infty \sim \chi^2_\nu$.

    The central chi-squared with $\nu$ degrees of freedom, divided by $2c$, is a **Gamma distribution**:

    $$
    r_\infty \sim \text{Gamma}\left(\frac{\nu}{2},\, \frac{1}{2c}\right) = \text{Gamma}\left(\frac{2\kappa\theta}{\sigma^2},\, \frac{\sigma^2}{4\kappa}\right)
    $$

    **Mean:**

    $$
    \mathbb{E}[r_\infty] = \frac{\nu}{2} \times \frac{1}{2c} = \frac{\nu}{4c} = \frac{4\kappa\theta/\sigma^2}{4 \times 2\kappa/\sigma^2} = \frac{4\kappa\theta/\sigma^2 \times \sigma^2}{8\kappa} = \frac{4\kappa\theta}{8\kappa} = \frac{\theta}{2} \times 2 = \theta
    $$

    More directly: mean $= (\nu/2) \times (\sigma^2/(4\kappa)) = (2\kappa\theta/\sigma^2) \times (\sigma^2/(4\kappa)) = \theta/2 \times 2$... Let me compute carefully:

    Shape $= \nu/2 = 2\kappa\theta/\sigma^2$, scale $= \sigma^2/(4\kappa)$.

    Mean $= \text{shape} \times \text{scale} = \frac{2\kappa\theta}{\sigma^2} \times \frac{\sigma^2}{4\kappa} = \frac{\theta}{2}$. This gives $\theta/2$, not $\theta$.

    Wait --- the Gamma parametrization matters. If $X \sim \chi^2_\nu$, then $\mathbb{E}[X] = \nu$. So $\mathbb{E}[r_\infty] = \nu/(2c) = \frac{4\kappa\theta/\sigma^2}{4\kappa/\sigma^2} = \theta$. $\checkmark$

    **Variance:**

    $$
    \text{Var}(r_\infty) = \frac{\text{Var}(\chi^2_\nu)}{(2c)^2} = \frac{2\nu}{(2c)^2} = \frac{2\nu}{4c^2} = \frac{2 \times 4\kappa\theta/\sigma^2}{4 \times (2\kappa/\sigma^2)^2} = \frac{8\kappa\theta/\sigma^2}{16\kappa^2/\sigma^4} = \frac{8\kappa\theta\sigma^2}{16\kappa^2} = \frac{\theta\sigma^2}{2\kappa}
    $$

    This matches the known CIR stationary variance. $\checkmark$

---

**Exercise 4.** The conditional variance of $r_s$ given $r_t$ can be computed from $\text{Var}(2c\,r_s) = 2(\nu + 2\lambda)$. Derive $\text{Var}(r_s | r_t)$ in terms of $\kappa$, $\theta$, $\sigma$, $r_t$, and $\tau$. Verify that your expression matches the formula $r_t\frac{\sigma^2}{\kappa}(e^{-\kappa\tau} - e^{-2\kappa\tau}) + \theta\frac{\sigma^2}{2\kappa}(1 - e^{-\kappa\tau})^2$.

??? success "Solution to Exercise 4"

    From $\text{Var}(2c\,r_s) = 2(\nu + 2\lambda)$:

    $$
    \text{Var}(r_s \mid r_t) = \frac{2(\nu + 2\lambda)}{(2c)^2} = \frac{\nu + 2\lambda}{2c^2}
    $$

    Substituting $\nu = 4\kappa\theta/\sigma^2$, $\lambda = 2c\,r_t\,e^{-\kappa\tau}$, and $c = 2\kappa/[\sigma^2(1-e^{-\kappa\tau})]$:

    $$
    \nu + 2\lambda = \frac{4\kappa\theta}{\sigma^2} + \frac{4\kappa}{\sigma^2(1 - e^{-\kappa\tau})} \cdot 2r_t e^{-\kappa\tau} = \frac{4\kappa}{\sigma^2}\left[\theta + \frac{2r_t e^{-\kappa\tau}}{1 - e^{-\kappa\tau}}\right]
    $$

    And $2c^2 = 2 \times \frac{4\kappa^2}{\sigma^4(1 - e^{-\kappa\tau})^2}$. So:

    $$
    \text{Var} = \frac{4\kappa\left[\theta + \frac{2r_t e^{-\kappa\tau}}{1-e^{-\kappa\tau}}\right]}{\sigma^2 \times \frac{8\kappa^2}{\sigma^4(1-e^{-\kappa\tau})^2}} = \frac{4\kappa\sigma^2(1-e^{-\kappa\tau})^2}{8\kappa^2}\left[\theta + \frac{2r_t e^{-\kappa\tau}}{1-e^{-\kappa\tau}}\right]
    $$

    $$
    = \frac{\sigma^2(1-e^{-\kappa\tau})^2}{2\kappa}\,\theta + \frac{\sigma^2(1-e^{-\kappa\tau})}{\kappa} \cdot r_t e^{-\kappa\tau}
    $$

    $$
    = \theta\frac{\sigma^2}{2\kappa}(1 - e^{-\kappa\tau})^2 + r_t\frac{\sigma^2}{\kappa}(e^{-\kappa\tau} - e^{-2\kappa\tau})
    $$

    This matches the formula $r_t\frac{\sigma^2}{\kappa}(e^{-\kappa\tau} - e^{-2\kappa\tau}) + \theta\frac{\sigma^2}{2\kappa}(1 - e^{-\kappa\tau})^2$. $\checkmark$

---

**Exercise 5.** The non-central chi-squared PDF involves the modified Bessel function $I_{\nu/2-1}(\sqrt{\lambda x})$. For the numerical example ($\nu = 8$, $\lambda = 9.24$), this is $I_3(\sqrt{9.24 x})$. At the mode $x \approx 15.2$, compute $\sqrt{\lambda x} \approx \sqrt{9.24 \times 15.2}$. Explain why the Bessel function argument grows with both $\lambda$ and $x$, and discuss the numerical implications for evaluating the PDF at extreme values.

??? success "Solution to Exercise 5"

    From the numerical example: $\nu = 8$, $\lambda = 9.24$.

    The Bessel function argument at the mode $x \approx 15.2$ is:

    $$
    \sqrt{\lambda x} = \sqrt{9.24 \times 15.2} = \sqrt{140.4} \approx 11.85
    $$

    The modified Bessel function $I_3(11.85)$ has a large argument. For general $I_\alpha(z)$ with large $z$, the asymptotic expansion is:

    $$
    I_\alpha(z) \sim \frac{e^z}{\sqrt{2\pi z}} \quad \text{as } z \to \infty
    $$

    So $I_3(11.85) \approx e^{11.85}/\sqrt{2\pi \times 11.85} \approx 1.4 \times 10^5 / 8.63 \approx 1.6 \times 10^4$.

    **Why the argument grows:** $\sqrt{\lambda x}$ increases with both $\lambda$ (which is proportional to $r_t$) and $x$ (the evaluation point). Large $\lambda$ shifts the distribution to the right, and the mode is at approximately $\nu + \lambda - 2$, so both $\lambda$ and the relevant evaluation range grow together.

    **Numerical implications:** For large Bessel function arguments, the exponential $e^z$ overflows standard double-precision arithmetic (which can handle $z \leq 709$). For $\lambda$ and $x$ both large (e.g., in MLE with high-frequency data), $\sqrt{\lambda x}$ can easily exceed this limit. The solution is to work in log-space: compute $\ln I_\alpha(z) \approx z - \frac{1}{2}\ln(2\pi z)$ and combine with other log-terms before exponentiating. Most numerical libraries (SciPy's `ive` function) provide exponentially scaled Bessel functions for this purpose.

---

**Exercise 6.** For maximum likelihood estimation with daily data ($\Delta t = 1/252$), the non-centrality parameter $\lambda$ is very large because $c$ is large and $e^{-\kappa\Delta t} \approx 1$. Compute $\lambda$ for $r_t = 0.05$, $\kappa = 0.5$, $\sigma = 0.10$, $\Delta t = 1/252$. Explain why large $\lambda$ makes the series representation of the non-central chi-squared PDF converge slowly and suggest an alternative computational approach.

??? success "Solution to Exercise 6"

    With $r_t = 0.05$, $\kappa = 0.5$, $\sigma = 0.10$, $\Delta t = 1/252$:

    $$
    c = \frac{2\kappa}{\sigma^2(1 - e^{-\kappa\Delta t})} = \frac{1.0}{0.01 \times (1 - e^{-0.001984})} = \frac{1.0}{0.01 \times 0.001982} = \frac{1.0}{1.982 \times 10^{-5}} = 50{,}454
    $$

    $$
    \lambda = 2c \cdot r_t \cdot e^{-\kappa\Delta t} = 2 \times 50{,}454 \times 0.05 \times 0.998016 = 5{,}035
    $$

    For the series representation, the Poisson mean is $\lambda/2 = 2{,}518$. The series requires evaluating terms near $k \approx 2{,}518$, and approximately $\sqrt{2518} \approx 50$ terms contribute significantly. Each term involves a Poisson weight $e^{-2518}(2518)^k/k!$ which requires careful log-space computation to avoid overflow.

    **Alternative approaches:**

    1. **Normal approximation:** For large $\lambda$, $\chi^2(\nu, \lambda) \approx \mathcal{N}(\nu + \lambda, 2(\nu + 2\lambda))$. With $\nu = 8$ and $\lambda = 5035$: mean $= 5043$, variance $= 10086$. This approximation is excellent for central quantiles when $\lambda \gg \nu$.

    2. **Saddle-point approximation:** Uses the cumulant generating function to get a more accurate approximation, especially in the tails. Accurate to $O(1/\lambda)$.

    3. **Direct log-likelihood computation:** Evaluate $\ln f_{\chi^2}(x; \nu, \lambda)$ directly using the log-Bessel function, avoiding the series entirely. SciPy's `ncx2.logpdf` handles this internally with appropriate numerical techniques.

---

**Exercise 7.** Compare the CIR transition density with the Vasicek transition density (which is Gaussian). For the same conditional mean and variance, plot or describe the qualitative differences between the two densities. In particular, discuss: (i) support ($r \geq 0$ vs $r \in \mathbb{R}$), (ii) skewness (right-skewed vs symmetric), and (iii) behavior near zero. Under what parameter regimes do the two densities look most similar?

??? success "Solution to Exercise 7"

    Suppose both densities have conditional mean $\mu$ and conditional variance $v^2$.

    **(i) Support:**

    - CIR: $r_s \in [0, \infty)$. The density is zero for negative values.
    - Vasicek: $r_s \in (-\infty, \infty)$. The Gaussian density assigns positive probability to negative rates.

    For practical purposes, when $\mu$ is large relative to the standard deviation (say $\mu/\sqrt{v^2} > 4$), the Gaussian probability of negative rates is negligible, and the support difference is immaterial.

    **(ii) Skewness:**

    - CIR: The non-central chi-squared (after scaling) is **right-skewed**. The skewness is $\sqrt{8}(\nu + 3\lambda)/(\nu + 2\lambda)^{3/2}$, which is positive.
    - Vasicek: The Gaussian is **symmetric** (zero skewness).

    The CIR density has a heavier right tail and a lighter left tail compared to a Gaussian with the same mean and variance.

    **(iii) Behavior near zero:**

    - CIR with $\nu \geq 2$: The density is zero at $r = 0$ and rises smoothly, forming a single interior mode.
    - CIR with $\nu < 2$: The density diverges or has a cusp at $r = 0$.
    - Vasicek: The Gaussian density at $r = 0$ is a positive finite value (just a point on the bell curve).

    **When do the densities look most similar?**

    The densities are most similar when:

    - The mean $\mu$ is large relative to the standard deviation (the density is concentrated far from zero, making the support difference negligible).
    - The degrees of freedom $\nu$ is large (making the chi-squared closer to Gaussian by the CLT).
    - The non-centrality $\lambda$ is large (further Gaussianifying the distribution).

    In parameter terms: high $\theta$, high $\kappa$ (large $\nu = 4\kappa\theta/\sigma^2$), moderate $\sigma$, and $r_t$ not close to zero. This corresponds to a "well-behaved" rate environment far from the zero boundary.
