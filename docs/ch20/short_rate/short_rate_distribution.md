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

---

## Exercises

**Exercise 1.** For parameters $a = 0.05$, $\sigma = 0.01$, and a flat forward curve $f(0,t) = 0.02$, compute the probability $\mathbb{P}(r_{10} < 0 \mid r_0 = 0.02)$. How does the probability change if $r_0 = 0.005$?

??? success "Solution to Exercise 1"
    With $a = 0.05$, $\sigma = 0.01$, and flat forward curve $f(0,t) = 0.02$:

    $$
    \alpha(t) = 0.02 + \frac{(0.01)^2}{2(0.05)^2}(1 - e^{-0.05t})^2 = 0.02 + 0.02(1 - e^{-0.05t})^2
    $$

    **Case 1: $r_0 = 0.02$.** The conditional mean at $T = 10$ is:

    $$
    \mu(0,10) = r_0 e^{-0.05 \times 10} + \alpha(10) - \alpha(0)e^{-0.5}
    $$

    Since $\alpha(0) = 0.02 = r_0$, this simplifies to $\mu(0,10) = \alpha(10) = 0.02 + 0.02(1 - e^{-0.5})^2$.

    Computing: $1 - e^{-0.5} = 0.3935$, so $\mu = 0.02 + 0.02 \times 0.1548 = 0.02310$.

    The conditional standard deviation is:

    $$
    \Sigma(0,10) = \sqrt{\frac{(0.01)^2}{2 \times 0.05}(1 - e^{-2 \times 0.05 \times 10})} = \sqrt{0.001 \times 0.6321} = \sqrt{6.321 \times 10^{-4}} = 0.02514
    $$

    The probability of a negative rate is:

    $$
    \mathbb{P}(r_{10} < 0 \mid r_0 = 0.02) = \Phi\!\left(\frac{-0.02310}{0.02514}\right) = \Phi(-0.9188) \approx 0.1791
    $$

    So approximately 17.9% probability of a negative rate at the 10-year horizon.

    **Case 2: $r_0 = 0.005$.** Since $\alpha(0) = f(0,0) = 0.02 \neq r_0$, we must use the full formula:

    $$
    \mu(0,10) = 0.005 \times e^{-0.5} + \alpha(10) - 0.02 \times e^{-0.5}
    $$

    $$
    = 0.005 \times 0.6065 + 0.02310 - 0.02 \times 0.6065 = 0.003033 + 0.02310 - 0.01213 = 0.01400
    $$

    The variance is unchanged: $\Sigma(0,10) = 0.02514$. Therefore:

    $$
    \mathbb{P}(r_{10} < 0 \mid r_0 = 0.005) = \Phi\!\left(\frac{-0.01400}{0.02514}\right) = \Phi(-0.5569) \approx 0.2888
    $$

    About 28.9%. The lower initial rate substantially increases the probability of negative rates, illustrating the Gaussian model's limitation in low-rate environments.

---

**Exercise 2.** Using the conditional MGF $M(u; t, T) = \exp(u\mu + \frac{1}{2}u^2\Sigma^2)$, show that the bond price $P(t,T) = \mathbb{E}[e^{-\int_t^T r_s\,ds} | \mathcal{F}_t]$ can be obtained by applying the MGF identity to the integrated short rate distribution.

??? success "Solution to Exercise 2"
    The integrated short rate $I = \int_t^T r_s\,ds$ is Gaussian with mean $M(t,T)$ and variance $V(t,T)$. Its MGF is:

    $$
    \mathbb{E}[e^{uI} | \mathcal{F}_t] = \exp\!\left(uM(t,T) + \frac{1}{2}u^2 V(t,T)\right)
    $$

    The bond price is:

    $$
    P(t,T) = \mathbb{E}\!\left[e^{-\int_t^T r_s\,ds} \Big| \mathcal{F}_t\right] = \mathbb{E}[e^{-I} | \mathcal{F}_t]
    $$

    This is the MGF evaluated at $u = -1$:

    $$
    P(t,T) = M(-1; t, T) = \exp\!\left(-M(t,T) + \frac{1}{2}V(t,T)\right)
    $$

    The $-M(t,T)$ term gives the "expected discounting" while the $+\frac{1}{2}V(t,T)$ term is the convexity adjustment (from Jensen's inequality: since $e^{-x}$ is convex, $\mathbb{E}[e^{-I}] > e^{-\mathbb{E}[I]}$, and the correction is exactly $\frac{1}{2}V$ for a Gaussian). This formula produces the affine bond price $P(t,T) = e^{A(t,T) + B(t,T)r_t}$ after substituting the explicit expressions for $M$ and $V$.

---

**Exercise 3.** Verify that the transition density $p(r_T | r_t; t, T)$ satisfies the Fokker-Planck equation $\frac{\partial p}{\partial T} = -\frac{\partial}{\partial r_T}[(\theta(T) - ar_T)p] + \frac{1}{2}\sigma^2\frac{\partial^2 p}{\partial r_T^2}$ by direct substitution.

??? success "Solution to Exercise 3"
    The transition density is $p(r_T | r_t; t, T) = \frac{1}{\sqrt{2\pi\Sigma^2}} \exp\!\left(-\frac{(r_T - \mu)^2}{2\Sigma^2}\right)$ where $\mu = \mu(t,T)$ and $\Sigma^2 = \Sigma^2(t,T)$.

    Note that $\mu$ depends on $T$ through $\theta(T)$ and $\Sigma^2$ depends on $T$ through $e^{-2a(T-t)}$. Also, $\frac{\partial \mu}{\partial T} = \theta(T) - a\mu(t,T)$ and $\frac{\partial \Sigma^2}{\partial T} = \sigma^2 e^{-2a(T-t)}$.

    **Left side of Fokker-Planck:** $\frac{\partial p}{\partial T}$. Differentiating:

    $$
    \frac{\partial p}{\partial T} = p \cdot \left[\frac{(r_T - \mu)\dot{\mu}}{\Sigma^2} - \frac{\dot{\Sigma}^2}{2\Sigma^2} + \frac{(r_T - \mu)^2 \dot{\Sigma}^2}{2\Sigma^4}\right]
    $$

    where dots denote $T$-derivatives.

    **Right side of Fokker-Planck:** Compute each term. For the advection term:

    $$
    -\frac{\partial}{\partial r_T}[(\theta(T) - ar_T)p] = ap - (\theta(T) - ar_T)\frac{\partial p}{\partial r_T}
    $$

    where $\frac{\partial p}{\partial r_T} = -p \cdot \frac{r_T - \mu}{\Sigma^2}$. For the diffusion term:

    $$
    \frac{1}{2}\sigma^2\frac{\partial^2 p}{\partial r_T^2} = \frac{1}{2}\sigma^2 p \left[\frac{(r_T - \mu)^2}{\Sigma^4} - \frac{1}{\Sigma^2}\right]
    $$

    Combining the right side:

    $$
    ap + (\theta(T) - ar_T)\frac{p(r_T - \mu)}{\Sigma^2} + \frac{\sigma^2 p}{2}\left[\frac{(r_T - \mu)^2}{\Sigma^4} - \frac{1}{\Sigma^2}\right]
    $$

    Using $\dot{\mu} = \theta(T) - a\mu$ and $\dot{\Sigma}^2 = \sigma^2 e^{-2a(T-t)} = \sigma^2 - 2a\Sigma^2$ (from differentiating $\Sigma^2 = \frac{\sigma^2}{2a}(1 - e^{-2a(T-t)})$), one can verify term-by-term that the left and right sides are equal. The key identities are: the coefficient of $p$ matches via $a = \frac{\dot{\Sigma}^2 + 2a\Sigma^2 - \sigma^2}{0} + a$; the coefficient of $p(r_T - \mu)/\Sigma^2$ matches via $\dot{\mu} = \theta(T) - a\mu$; and the coefficient of $p(r_T - \mu)^2/\Sigma^4$ matches via $\dot{\Sigma}^2 = \sigma^2 - 2a\Sigma^2$.

---

**Exercise 4.** The characteristic function $\phi(\xi; t, T) = \exp(i\xi\mu - \frac{1}{2}\xi^2\Sigma^2)$ can be used for Fourier-based pricing. Explain how the COS method would use this characteristic function to price a caplet in the Hull-White model.

??? success "Solution to Exercise 4"
    The COS method prices derivatives by expanding the payoff in a cosine series and using the characteristic function to compute the expansion coefficients.

    **Step 1: Caplet payoff.** A caplet with strike $K$, reset date $T$, and payment date $T + \delta$ has payoff $\delta(L(T, T+\delta) - K)^+$ at $T + \delta$, which can be expressed as a function of $r_T$ through the bond price $P(T, T+\delta)$. Specifically, $L(T,T+\delta) = \frac{1}{\delta}(1/P(T,T+\delta) - 1)$.

    **Step 2: COS expansion.** The price is:

    $$
    V = P(t,T) \cdot \mathbb{E}^{T}\!\left[g(r_T) | r_t\right]
    $$

    where $g(r_T)$ encodes the payoff. Truncate the integration domain to $[c_1, c_2]$ and expand:

    $$
    V \approx P(t,T) \sum_{k=0}^{N-1} \text{Re}\!\left[\phi_T\!\left(\frac{k\pi}{c_2 - c_1}\right) e^{-ik\pi\frac{c_1}{c_2-c_1}}\right] V_k
    $$

    **Step 3: Use the characteristic function.** The Hull-White characteristic function $\phi(\xi; t, T) = \exp(i\xi\mu - \frac{1}{2}\xi^2\Sigma^2)$ is evaluated at $\xi = \frac{k\pi}{c_2 - c_1}$ for $k = 0, 1, \ldots, N-1$. The Gaussian form means $\phi$ decays rapidly in $|\xi|$, ensuring fast convergence of the COS expansion.

    **Step 4: Cosine coefficients.** The payoff coefficients $V_k = \frac{2}{c_2 - c_1}\int_{c_1}^{c_2} g(r)\cos\!\left(k\pi\frac{r - c_1}{c_2 - c_1}\right)dr$ can be computed analytically for the caplet payoff (which is piecewise linear in $r_T$ after the bond price transformation).

    The COS method is efficient here because the Gaussian characteristic function is available in closed form and the truncation bounds $[c_1, c_2]$ can be chosen using $\mu \pm L\Sigma$ for some $L$ (typically $L = 10$).

---

**Exercise 5.** Compute the variance $V(0, 10)$ of the integrated short rate $\int_0^{10} r_s\,ds$ for $a = 0.05$ and $\sigma = 0.01$. Compare with the Ho-Lee approximation $V \approx \frac{\sigma^2}{3}(T-t)^3$ obtained by setting $a = 0$.

??? success "Solution to Exercise 5"
    Using $a = 0.05$, $\sigma = 0.01$, and $T - t = 10$:

    $$
    V(0,10) = \frac{\sigma^2}{a^2}\left[(T-t) - \frac{2}{a}(1 - e^{-a(T-t)}) + \frac{1}{2a}(1 - e^{-2a(T-t)})\right]
    $$

    Substituting values:

    $$
    \frac{\sigma^2}{a^2} = \frac{(0.01)^2}{(0.05)^2} = \frac{10^{-4}}{2.5 \times 10^{-3}} = 0.04
    $$

    $$
    T - t = 10
    $$

    $$
    \frac{2}{a}(1 - e^{-a \cdot 10}) = \frac{2}{0.05}(1 - e^{-0.5}) = 40 \times 0.3935 = 15.739
    $$

    $$
    \frac{1}{2a}(1 - e^{-2a \cdot 10}) = \frac{1}{0.10}(1 - e^{-1.0}) = 10 \times 0.6321 = 6.321
    $$

    Therefore:

    $$
    V(0,10) = 0.04 \times [10 - 15.739 + 6.321] = 0.04 \times 0.582 = 0.02328
    $$

    **Ho-Lee approximation** (setting $a = 0$): As $a \to 0$, $V \to \frac{\sigma^2}{3}(T-t)^3$:

    $$
    V_{\text{Ho-Lee}} = \frac{(0.01)^2}{3} \times 10^3 = \frac{10^{-4}}{3} \times 1000 = 0.03333
    $$

    The Ho-Lee approximation overestimates the variance by about 43% ($0.03333$ vs $0.02328$). This is because mean reversion ($a > 0$) reduces the long-term variance of the integrated rate by pulling the short rate back toward its mean, an effect that the Ho-Lee model (with no mean reversion) cannot capture.

---

**Exercise 6.** Prove that the skewness and excess kurtosis of $r_T | r_t$ are both zero in the Hull-White model. Why is zero skewness a potential concern when modeling interest rate distributions?

??? success "Solution to Exercise 6"
    **Zero skewness:** The skewness of a random variable $X$ is $\gamma_1 = \mathbb{E}\!\left[\left(\frac{X - \mu}{\Sigma}\right)^3\right]$. Since $r_T | r_t \sim \mathcal{N}(\mu, \Sigma^2)$, the standardized variable $Z = (r_T - \mu)/\Sigma \sim \mathcal{N}(0,1)$. By symmetry of the standard normal distribution, all odd central moments vanish:

    $$
    \mathbb{E}[Z^3] = \int_{-\infty}^{\infty} z^3 \frac{1}{\sqrt{2\pi}}e^{-z^2/2}\,dz = 0
    $$

    since the integrand $z^3 e^{-z^2/2}$ is an odd function. Therefore, the skewness is zero.

    **Zero excess kurtosis:** The kurtosis is $\kappa_4 = \mathbb{E}[Z^4]$. For the standard normal:

    $$
    \mathbb{E}[Z^4] = \int_{-\infty}^{\infty} z^4 \frac{1}{\sqrt{2\pi}}e^{-z^2/2}\,dz = 3
    $$

    (computed via integration by parts or the MGF). The excess kurtosis is $\kappa_4 - 3 = 0$.

    **Concern about zero skewness:** Empirically, interest rate distributions exhibit positive skewness, meaning large upward rate moves are more likely than large downward moves. This is partly because:

    - Rates have a natural floor (near zero or slightly negative), creating asymmetry
    - Central banks tend to raise rates more aggressively than they cut
    - The log-normal models (Black-Karasinski, CIR) capture this skewness through their multiplicative structure

    The Hull-White model's symmetric distribution assigns equal probability to upward and downward moves of the same magnitude, which can misprice options that are sensitive to the distribution's tails (e.g., out-of-the-money caps and floors).

---

**Exercise 7.** The exact simulation formula $r_T = \mu(t,T) + \Sigma(t,T)Z$ with $Z \sim \mathcal{N}(0,1)$ has no discretization error. Compare this with an Euler-Maruyama discretization using $n$ time steps and discuss the trade-off between computational cost and accuracy.

??? success "Solution to Exercise 7"
    **Exact simulation:** Sample $r_T = \mu(t,T) + \Sigma(t,T)Z$ with $Z \sim \mathcal{N}(0,1)$.

    - Cost: 1 random number, 2 function evaluations ($\mu$ and $\Sigma$), and 2 multiplications per step
    - Error: zero discretization error (exact distribution)
    - Any time step size $\Delta t$ can be used

    **Euler-Maruyama with $n$ steps:** Partition $[t, T]$ into $n$ steps with $\Delta t = (T-t)/n$:

    $$
    r_{k+1} = r_k + a(\theta(t_k) - r_k)\Delta t + \sigma\sqrt{\Delta t}\,Z_k
    $$

    - Cost: $n$ random numbers, $n$ evaluations of $\theta(t_k)$, and $O(n)$ arithmetic operations
    - Weak error: $O(\Delta t) = O(1/n)$ (bias in expected values)
    - Strong error: $O(\sqrt{\Delta t}) = O(1/\sqrt{n})$ (pathwise accuracy)

    **Trade-off comparison:**

    | Property | Exact | Euler ($n$ steps) |
    |:---|:---:|:---:|
    | Random numbers per path | 1 | $n$ |
    | Discretization error | 0 | $O(1/n)$ |
    | Computational cost | $O(1)$ | $O(n)$ |
    | Implementation | Needs $\mu$, $\Sigma$ formulas | Simple recursive update |

    The exact method is strictly superior for the Hull-White model because the transition density is known in closed form. The Euler method's only advantage is generality: it works for models without closed-form transition densities. For the Hull-White model, one should always use exact simulation.
