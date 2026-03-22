# Short Rate Distribution

The Hull-White model produces a Gaussian short rate, meaning the conditional distribution of $r_T$ given $r_t$ is fully characterized by its mean and variance. This Gaussian property is both the model's greatest strength (enabling closed-form pricing) and its most discussed limitation (allowing negative rates). This section derives the complete distributional characterization, including the transition density, moment generating function, characteristic function, and the probability of negative rates.

!!! info "Prerequisites"
    - Hull-White SDE and explicit solution (this chapter)
    - Ito isometry for stochastic integrals
    - Gaussian random variables: density, MGF, characteristic function
    - Normal distribution and its properties

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the conditional distribution of $r_T$ given $r_t$
    2. Derive the conditional mean and variance from the explicit solution
    3. Write the transition density in closed form
    4. Compute the moment generating function and characteristic function
    5. Evaluate the probability of negative interest rates

---

## Conditional Distribution

The starting point is the explicit solution of the Hull-White SDE derived in the SDE section.

!!! note "Theorem: Gaussian Conditional Distribution"
    Under the Hull-White model, $r_T$ conditional on $\mathcal{F}_t$ (equivalently, conditional on $r_t$) is normally distributed:

    $$
    r_T \mid r_t \sim \mathcal{N}\!\left(\mu(t,T),\; \Sigma^2(t,T)\right)
    $$

    where the **conditional mean** is

    $$
    \mu(t,T) = r_t\, e^{-a(T-t)} + \int_t^T e^{-a(T-u)}\, \theta(u)\, du
    $$

    and the **conditional variance** is

    $$
    \Sigma^2(t,T) = \frac{\sigma^2}{2a}\bigl(1 - e^{-2a(T-t)}\bigr)
    $$

???+ note "Proof"
    From the explicit solution:

    $$
    r_T = r_t\, e^{-a(T-t)} + \int_t^T e^{-a(T-u)}\, \theta(u)\, du + \sigma \int_t^T e^{-a(T-u)}\, dW_u^{\mathbb{Q}}
    $$

    The first two terms are $\mathcal{F}_t$-measurable (deterministic given $r_t$). The third term is a stochastic integral of a deterministic integrand against Brownian motion, hence Gaussian with mean zero.

    **Conditional mean:**

    $$
    \mathbb{E}[r_T \mid \mathcal{F}_t] = r_t\, e^{-a(T-t)} + \int_t^T e^{-a(T-u)}\, \theta(u)\, du + 0 = \mu(t,T)
    $$

    **Conditional variance** (by the Ito isometry):

    $$
    \text{Var}[r_T \mid \mathcal{F}_t] = \sigma^2 \int_t^T e^{-2a(T-u)}\, du
    $$

    Evaluate the integral:

    $$
    \sigma^2 \int_t^T e^{-2a(T-u)}\, du = \sigma^2 \left[\frac{1}{2a}\, e^{-2a(T-u)}\right]_{u=t}^{u=T} = \frac{\sigma^2}{2a}\bigl(1 - e^{-2a(T-t)}\bigr)
    $$

    $\square$

---

## The Conditional Mean in Detail

Using the expression $\theta(t) = f'(0,t) + af(0,t) + \frac{\sigma^2}{2a}(1-e^{-2at})$, the conditional mean can be written purely in terms of market observables.

!!! note "Proposition: Conditional Mean via Initial Curve"
    The conditional mean can be expressed as

    $$
    \mu(t,T) = r_t\, e^{-a(T-t)} + \alpha(T) - \alpha(t)\, e^{-a(T-t)}
    $$

    where $\alpha(t) = f(0,t) + \frac{\sigma^2}{2a^2}(1 - e^{-at})^2$ is the deterministic mean function.

???+ note "Proof"
    The function $\alpha(t)$ satisfies $\alpha(t) = \psi(t)\big|_{r_0 \text{ absorbed}}$ from the short rate decomposition. Using $r_t = \alpha(t) + \sigma \int_0^t e^{-a(t-s)}\, dW_s$, the conditional mean becomes

    $$
    \mu(t,T) = r_t\, e^{-a(T-t)} + \int_t^T e^{-a(T-u)}\, \theta(u)\, du
    $$

    The integral $\int_t^T e^{-a(T-u)} \theta(u)\, du = \alpha(T) - \alpha(t) e^{-a(T-t)}$ follows from the definition of $\alpha$ and the ODE that $\alpha$ satisfies: $\alpha'(t) = \theta(t) - a\alpha(t)$ with appropriate initial conditions, which gives the stated result upon applying the variation of constants formula. $\square$

This representation is computationally efficient because $\alpha(t)$ depends only on the initial forward curve and model parameters, and can be precomputed for all required time points.

---

## Transition Density

The Gaussian conditional distribution immediately gives the transition density.

!!! note "Corollary: Transition Density"
    The transition density of $r_T$ given $r_t$ under the Hull-White model is

    $$
    p(r_T \mid r_t; t, T) = \frac{1}{\sqrt{2\pi\, \Sigma^2(t,T)}} \exp\!\left(-\frac{(r_T - \mu(t,T))^2}{2\, \Sigma^2(t,T)}\right)
    $$

    This is the density of a normal distribution with mean $\mu(t,T)$ and variance $\Sigma^2(t,T)$.

The transition density is the Green's function of the Fokker-Planck (forward Kolmogorov) equation associated with the Hull-White diffusion:

$$
\frac{\partial p}{\partial T} = -\frac{\partial}{\partial r_T}\bigl[(\theta(T) - ar_T)\, p\bigr] + \frac{1}{2}\sigma^2 \frac{\partial^2 p}{\partial r_T^2}
$$

The explicit Gaussian form makes Monte Carlo simulation trivial: given $r_t$, one samples $r_T = \mu(t,T) + \Sigma(t,T)\, Z$ where $Z \sim \mathcal{N}(0,1)$, with no discretization error.

---

## Moment Generating Function

The moment generating function (MGF) provides a compact encoding of all moments and connects directly to bond pricing.

!!! note "Theorem: Conditional MGF"
    The conditional moment generating function of $r_T$ given $r_t$ is

    $$
    M(u; t, T) = \mathbb{E}\bigl[e^{u\, r_T} \mid r_t\bigr] = \exp\!\left(u\, \mu(t,T) + \frac{1}{2}\, u^2\, \Sigma^2(t,T)\right)
    $$

    for all $u \in \mathbb{R}$.

???+ note "Proof"
    Since $r_T \mid r_t \sim \mathcal{N}(\mu, \Sigma^2)$, the MGF of a Gaussian random variable with mean $\mu$ and variance $\Sigma^2$ is

    $$
    M(u) = \mathbb{E}[e^{uX}] = e^{u\mu + \frac{1}{2}u^2\Sigma^2}
    $$

    This is a standard result from probability theory. $\square$

!!! example "Application: Moments of the Short Rate"
    The first four conditional moments follow from differentiation of the MGF:

    - $\mathbb{E}[r_T \mid r_t] = M'(0) = \mu(t,T)$
    - $\mathbb{E}[r_T^2 \mid r_t] = M''(0) = \mu^2 + \Sigma^2$
    - $\text{Var}[r_T \mid r_t] = \Sigma^2(t,T)$
    - Skewness $= 0$ (Gaussian is symmetric)
    - Excess kurtosis $= 0$ (Gaussian has zero excess kurtosis)

    The vanishing skewness and kurtosis reflect the Gaussian limitation: the Hull-White model cannot capture the empirically observed skewness in rate distributions.

---

## Characteristic Function

The characteristic function is the Fourier counterpart of the MGF, obtained by setting $u = i\xi$.

!!! note "Corollary: Conditional Characteristic Function"
    The conditional characteristic function of $r_T$ given $r_t$ is

    $$
    \phi(\xi; t, T) = \mathbb{E}\bigl[e^{i\xi\, r_T} \mid r_t\bigr] = \exp\!\left(i\xi\, \mu(t,T) - \frac{1}{2}\, \xi^2\, \Sigma^2(t,T)\right)
    $$

The characteristic function is essential for Fourier-based pricing methods (COS method, FFT) applied to interest rate derivatives under the Hull-White model.

---

## Probability of Negative Rates

The Gaussian distribution assigns positive probability to all real values, including negative interest rates.

!!! note "Proposition: Negative Rate Probability"
    The probability that the short rate is negative at time $T$, conditional on $r_t$, is

    $$
    \mathbb{P}(r_T < 0 \mid r_t) = \Phi\!\left(\frac{-\mu(t,T)}{\Sigma(t,T)}\right)
    $$

    where $\Phi$ is the standard normal cumulative distribution function.

???+ note "Proof"
    Since $r_T \mid r_t \sim \mathcal{N}(\mu, \Sigma^2)$:

    $$
    \mathbb{P}(r_T < 0 \mid r_t) = \mathbb{P}\!\left(\frac{r_T - \mu}{\Sigma} < \frac{-\mu}{\Sigma}\right) = \Phi\!\left(\frac{-\mu}{\Sigma}\right)
    $$

    $\square$

!!! example "Numerical Example: Negative Rate Probability"
    With parameters $a = 0.05$, $\sigma = 0.01$, $r_0 = 0.03$, and a flat curve $f(0,t) = 0.03$:

    | Horizon $T$ | $\mu(0,T)$ | $\Sigma(0,T)$ | $\mathbb{P}(r_T < 0)$ |
    |:---:|:---:|:---:|:---:|
    | 1 | 0.0302 | 0.0070 | $8.0 \times 10^{-6}$ |
    | 5 | 0.0311 | 0.0141 | $1.4 \times 10^{-2}$ |
    | 10 | 0.0320 | 0.0173 | $3.2 \times 10^{-2}$ |
    | 30 | 0.0348 | 0.0200 | $4.1 \times 10^{-2}$ |

    The probability of negative rates is negligible for short horizons but reaches approximately 4% at the 30-year horizon. For low-rate environments (e.g., $r_0 = 0.005$), these probabilities become substantially larger, motivating log-normal alternatives like the Black-Karasinski model.

---

## Distribution of the Integrated Short Rate

For bond pricing, the distribution of the integrated short rate $\int_t^T r_s\, ds$ is equally important.

!!! note "Theorem: Integrated Short Rate Distribution"
    Under the Hull-White model, the integrated short rate conditional on $\mathcal{F}_t$ is Gaussian:

    $$
    \int_t^T r_s\, ds \;\Big|\; \mathcal{F}_t \sim \mathcal{N}\!\left(M(t,T),\; V(t,T)\right)
    $$

    where

    $$
    M(t,T) = \mathbb{E}\!\left[\int_t^T r_s\, ds \,\Big|\, r_t\right] = B(t,T)\bigl[r_t - \alpha(t)\bigr] + \ln\frac{P(0,t)}{P(0,T)} + \frac{1}{2}\bigl[V(0,T) - V(0,t)\bigr]
    $$

    and

    $$
    V(t,T) = \frac{\sigma^2}{a^2}\left[(T-t) - 2\,\frac{1-e^{-a(T-t)}}{a} + \frac{1-e^{-2a(T-t)}}{2a}\right]
    $$

    with $B(t,T) = (1 - e^{-a(T-t)})/a$.

???+ note "Proof"
    Since $r_s = \mu(t,s) + \sigma \int_t^s e^{-a(s-u)}\, dW_u$, the integral $\int_t^T r_s\, ds$ is a sum of a deterministic part and a Gaussian stochastic integral. The mean is obtained by integrating $\mu(t,s)$ over $[t,T]$. The variance is computed by the Ito isometry applied to the double integral:

    $$
    V(t,T) = \text{Var}\!\left[\int_t^T \sigma \int_t^s e^{-a(s-u)}\, dW_u\, ds \,\Big|\, r_t\right]
    $$

    By Fubini's theorem for stochastic integrals, this equals

    $$
    V(t,T) = \sigma^2 \int_t^T \left(\int_u^T e^{-a(s-u)}\, ds\right)^2 du = \sigma^2 \int_t^T \left(\frac{1 - e^{-a(T-u)}}{a}\right)^2 du
    $$

    Evaluating: let $v = T - u$, then

    $$
    V(t,T) = \frac{\sigma^2}{a^2} \int_0^{T-t} (1 - e^{-av})^2\, dv = \frac{\sigma^2}{a^2}\left[(T-t) - \frac{2}{a}(1 - e^{-a(T-t)}) + \frac{1}{2a}(1 - e^{-2a(T-t)})\right]
    $$

    $\square$

The Gaussian distribution of $\int_t^T r_s\, ds$ is what makes the bond price $P(t,T) = \mathbb{E}^{\mathbb{Q}}[e^{-\int_t^T r_s\, ds} \mid \mathcal{F}_t]$ analytically tractable via the MGF of a Gaussian.

---

## Summary

The Hull-White short rate has a Gaussian conditional distribution $r_T \mid r_t \sim \mathcal{N}(\mu(t,T), \Sigma^2(t,T))$ with mean $\mu(t,T) = r_t e^{-a(T-t)} + \int_t^T e^{-a(T-u)} \theta(u)\, du$ and variance $\Sigma^2(t,T) = \frac{\sigma^2}{2a}(1 - e^{-2a(T-t)})$. The transition density, MGF, and characteristic function all follow from the Gaussian property. The integrated short rate $\int_t^T r_s\, ds$ is also Gaussian, which is the foundation for analytical bond pricing. The probability of negative rates is $\Phi(-\mu/\Sigma)$, which is small but nonzero for typical parameters and becomes the principal limitation of the Gaussian framework.
