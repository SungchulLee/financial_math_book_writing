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

From $\mathbb{E}[2c\,r_s] = \nu + \lambda$:

$$
\mathbb{E}[r_s \mid r_t] = \frac{\nu + \lambda}{2c} = \frac{4\kappa\theta/\sigma^2 + 4\kappa\,r_t\,e^{-\kappa\tau}/(\sigma^2(1 - e^{-\kappa\tau}))}{4\kappa/(\sigma^2(1 - e^{-\kappa\tau}))}
$$

$$
= \theta(1 - e^{-\kappa\tau}) + r_t\,e^{-\kappa\tau} = \theta + (r_t - \theta)\,e^{-\kappa\tau}
$$

This matches the conditional mean derived directly from the SDE. $\square$

Similarly, from $\text{Var}(2c\,r_s) = 2(\nu + 2\lambda)$:

$$
\text{Var}(r_s \mid r_t) = \frac{2(\nu + 2\lambda)}{(2c)^2} = r_t\,\frac{\sigma^2}{\kappa}(e^{-\kappa\tau} - e^{-2\kappa\tau}) + \theta\,\frac{\sigma^2}{2\kappa}(1 - e^{-\kappa\tau})^2
$$

matching the variance formula from the CIR SDE section. $\square$

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
