# Greeks via Feynman–Kac


Feynman–Kac represents prices as expectations and can yield expectation representations for Greeks. This probabilistic approach is foundational for Monte Carlo methods and extends naturally beyond Black–Scholes.

---

## Price as expectation


Under the risk-neutral measure $\mathbb{Q}$,

$$
\mathrm{d}S_t = rS_t\,\mathrm{d}t + \sigma S_t\,\mathrm{d}W_t
$$

and the Feynman–Kac theorem gives

$$
V(t,S) = \mathbb{E}^{t,S}\!\left[e^{-r(T-t)}\Phi(S_T)\right]
$$

where $\mathbb{E}^{t,S}$ denotes expectation conditional on $S_t = S$. This is the probabilistic counterpart of the Black–Scholes PDE: $V$ solves the PDE if and only if it equals this conditional expectation.

---

## The stochastic flow


In Black–Scholes, the terminal value has the explicit form

$$
S_T = S\exp\!\left((r - \tfrac{1}{2}\sigma^2)\tau + \sigma(W_T - W_t)\right), \quad \tau = T - t
$$

This is $C^\infty$ in the initial condition $S$, and the **stochastic flow derivative** (Jacobian) is

$$
\boxed{\frac{\partial S_T}{\partial S} = \frac{S_T}{S}}
$$

This ratio is key: it converts differentiation with respect to the initial condition into a multiplicative weight involving the terminal value. The identity holds because geometric Brownian motion is log-linear in its initial condition.

---

## Delta via pathwise differentiation


For sufficiently smooth payoff $\Phi$, we can interchange differentiation and expectation:

$$
\Delta(t,S) = \frac{\partial}{\partial S}\mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi(S_T)\right]
= \mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\frac{\partial S_T}{\partial S}\right]
$$

Using the stochastic flow:

$$
\boxed{
\Delta(t,S) = \mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\frac{S_T}{S}\right]
}
$$

**Verification for the European call.** With $\Phi(x) = (x - K)^+$, we have $\Phi'(x) = \mathbf{1}_{x > K}$ (a.e.), so

$$
\Delta = \frac{e^{-r\tau}}{S}\mathbb{E}^{t,S}\!\left[S_T \mathbf{1}_{S_T > K}\right]
$$

Computing this expectation under the log-normal distribution recovers $\Delta = N(d_1)$.

---

## Vega via Feynman–Kac


The sensitivity to volatility requires differentiating through the distribution of $S_T$. Writing $S_T = S\exp((r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}\,Z)$ where $Z \sim N(0,1)$:

$$
\frac{\partial S_T}{\partial \sigma} = S_T\left(-\sigma\tau + \sqrt{\tau}\,Z\right)
$$

For smooth $\Phi$:

$$
\nu(t,S) = \mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\cdot S_T(-\sigma\tau + \sqrt{\tau}\,Z)\right]
$$

This is the **pathwise vega estimator**, valid when $\Phi$ is differentiable. It provides an unbiased Monte Carlo estimator for vega.

---

## Rho via Feynman–Kac


Differentiating with respect to $r$ affects both the discount factor and the drift:

$$
\rho = \frac{\partial}{\partial r}\mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi(S_T)\right]
$$

This gives two terms:

$$
\rho = -\tau\,V(t,S) + e^{-r\tau}\mathbb{E}^{t,S}\!\left[\Phi'(S_T)\frac{\partial S_T}{\partial r}\right]
$$

Since $\frac{\partial S_T}{\partial r} = \tau S_T$:

$$
\rho = -\tau V + e^{-r\tau}\tau\,\mathbb{E}^{t,S}\!\left[\Phi'(S_T)S_T\right]
$$

For a call, this simplifies to $\rho = K\tau e^{-r\tau}N(d_2)$.

---

## Gamma is delicate


The second derivative with respect to $S$ requires

$$
\Gamma = \mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi''(S_T)\left(\frac{S_T}{S}\right)^2\right] + \mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\frac{\partial^2 S_T}{\partial S^2}\right]
$$

For geometric Brownian motion, $\frac{\partial^2 S_T}{\partial S^2} = 0$ (the flow is linear in $S$), so

$$
\Gamma = \frac{1}{S^2}\mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi''(S_T)S_T^2\right]
$$

**Problem.** For the standard call payoff $\Phi(x) = (x-K)^+$, we have $\Phi''(x) = \delta(x-K)$ (Dirac delta), which is distributional. The pathwise approach breaks down because the payoff has a kink at $K$.

**Resolutions:**

- **Smoothing**: replace $\Phi$ by a smooth approximation $\Phi_\epsilon$ and take $\epsilon \to 0$.
- **Likelihood ratio method**: move the derivative from the payoff to the density (see *Likelihood Ratio and Malliavin Methods*).
- **PDE-based gamma**: compute from the closed-form $\Gamma = N'(d_1)/(S\sigma\sqrt{\tau})$ directly.
- **Finite differences**: estimate $\Gamma \approx (V(S+h) - 2V(S) + V(S-h))/h^2$ via re-simulation.

---

## General diffusion models


For a general SDE $dS_t = \mu(t,S_t)\,dt + \sigma(t,S_t)\,dW_t$, the stochastic flow $Y_t := \partial S_t/\partial S_0$ satisfies the **variational equation**:

$$
dY_t = \mu'(t,S_t)Y_t\,dt + \sigma'(t,S_t)Y_t\,dW_t, \quad Y_0 = 1
$$

where primes denote derivatives with respect to $S$. The delta is then

$$
\Delta = \mathbb{E}\!\left[e^{-r\tau}\Phi'(S_T)Y_T\right]
$$

This extends the Feynman–Kac approach to local volatility models, CEV models, and beyond — wherever the flow $Y_T$ can be simulated alongside the forward path.

---

## Practical Monte Carlo implementation


The Feynman–Kac representations lead to the following Monte Carlo workflow for Greeks:

1. **Simulate paths**: generate $N$ independent paths of $S_T^{(i)}$.
2. **Delta**: compute $\hat{\Delta} = \frac{1}{N}\sum_{i=1}^N e^{-r\tau}\Phi'(S_T^{(i)})\frac{S_T^{(i)}}{S}$.
3. **Vega**: compute $\hat{\nu} = \frac{1}{N}\sum_{i=1}^N e^{-r\tau}\Phi'(S_T^{(i)})S_T^{(i)}(-\sigma\tau + \sqrt{\tau}\,Z^{(i)})$.
4. **Gamma**: use likelihood ratio weights or finite differences (not pathwise).

Variance reduction techniques (antithetic variates, control variates, importance sampling) can dramatically improve the efficiency of these estimators.

---

## What to remember


- Delta can be written as an expectation involving the Jacobian $\partial S_T/\partial S$, enabling pathwise Monte Carlo estimation.
- Vega and rho have analogous pathwise representations.
- Gamma requires more care when payoffs are nonsmooth; the pathwise method fails for kinked payoffs like vanilla calls and puts.
- The stochastic flow approach generalizes to arbitrary diffusion models through the variational equation.

---

## Exercises

**Exercise 1.** Verify the stochastic flow identity $\frac{\partial S_T}{\partial S} = \frac{S_T}{S}$ for geometric Brownian motion $S_T = S\exp((r - \frac{1}{2}\sigma^2)\tau + \sigma(W_T - W_t))$ by direct differentiation with respect to $S$.

??? success "Solution to Exercise 1"
    We have

    $$
    S_T = S \exp\!\left((r - \tfrac{1}{2}\sigma^2)\tau + \sigma(W_T - W_t)\right)
    $$

    The exponential factor does not depend on $S$, so differentiation with respect to $S$ gives

    $$
    \frac{\partial S_T}{\partial S} = \exp\!\left((r - \tfrac{1}{2}\sigma^2)\tau + \sigma(W_T - W_t)\right)
    $$

    But $S_T / S = \exp\!\left((r - \tfrac{1}{2}\sigma^2)\tau + \sigma(W_T - W_t)\right)$ by definition. Therefore

    $$
    \frac{\partial S_T}{\partial S} = \frac{S_T}{S}
    $$

    This holds because $S_T$ is linear in $S$ (it factors as $S$ times an $S$-independent random variable), which is the defining property of geometric Brownian motion.

---

**Exercise 2.** The pathwise delta formula for a European call gives $\Delta = \frac{e^{-r\tau}}{S}\mathbb{E}^{t,S}[S_T \mathbf{1}_{S_T > K}]$. Evaluate this expectation under the risk-neutral log-normal distribution and recover $\Delta = N(d_1)$. (Hint: use the fact that $S_T/S = \exp((r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z)$.)

??? success "Solution to Exercise 2"
    We need to evaluate $\Delta = \frac{e^{-r\tau}}{S}\mathbb{E}^{t,S}[S_T \mathbf{1}_{S_T > K}]$. Writing $S_T = S e^{(r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z}$ with $Z \sim \mathcal{N}(0,1)$:

    $$
    \Delta = \frac{e^{-r\tau}}{S} \cdot S \cdot \mathbb{E}\!\left[e^{(r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z} \mathbf{1}_{S e^{(r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z} > K}\right]
    $$

    The indicator $S_T > K$ is equivalent to $Z > -d_2$ where $d_2 = \frac{\ln(S/K) + (r - \frac{1}{2}\sigma^2)\tau}{\sigma\sqrt{\tau}}$. Thus

    $$
    \Delta = e^{-r\tau} \int_{-d_2}^{\infty} e^{(r-\frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}z} \frac{1}{\sqrt{2\pi}} e^{-z^2/2} \, dz
    $$

    Completing the square in the exponent: $(r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}z - \frac{z^2}{2} = r\tau - \frac{1}{2}(z - \sigma\sqrt{\tau})^2$. Substituting $u = z - \sigma\sqrt{\tau}$:

    $$
    \Delta = \int_{-d_2 - \sigma\sqrt{\tau}}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-u^2/2}\,du = \int_{-d_1}^{\infty} \frac{1}{\sqrt{2\pi}} e^{-u^2/2}\,du = N(d_1)
    $$

    since $d_1 = d_2 + \sigma\sqrt{\tau}$.

---

**Exercise 3.** For the rho formula $\rho = -\tau V + e^{-r\tau}\tau \mathbb{E}^{t,S}[\Phi'(S_T)S_T]$, explain the two contributions: one from the discount factor and one from the drift. For a deep ITM call where $\Phi'(S_T) \approx 1$ and $V \approx S - Ke^{-r\tau}$, show that $\rho \approx K\tau e^{-r\tau}$.

??? success "Solution to Exercise 3"
    The rho formula $\rho = -\tau V + e^{-r\tau}\tau\,\mathbb{E}^{t,S}[\Phi'(S_T)S_T]$ has two terms:

    - **Discount factor term** $(-\tau V)$: increasing $r$ by $dr$ makes the discount factor $e^{-r\tau}$ smaller by approximately $\tau e^{-r\tau} dr$, reducing the present value. This gives a negative contribution proportional to the option price.
    - **Drift term** $(e^{-r\tau}\tau\,\mathbb{E}[\Phi'(S_T)S_T])$: increasing $r$ raises the risk-neutral drift of $S_T$, making $S_T$ stochastically larger, which increases the payoff. This is a positive contribution.

    For a deep ITM call, $\Phi'(S_T) = \mathbf{1}_{S_T > K} \approx 1$ almost surely, and $V \approx S - K e^{-r\tau}$. Then:

    $$
    \rho \approx -\tau(S - Ke^{-r\tau}) + e^{-r\tau}\tau\,\mathbb{E}[S_T]
    $$

    Under risk-neutrality, $\mathbb{E}[S_T] = S e^{r\tau}$, so $e^{-r\tau}\mathbb{E}[S_T] = S$. Therefore

    $$
    \rho \approx -\tau S + K\tau e^{-r\tau} + \tau S = K\tau e^{-r\tau}
    $$

---

**Exercise 4.** The pathwise approach to gamma fails for the call payoff because $\Phi''(x) = \delta(x - K)$. However, for $\frac{\partial^2 S_T}{\partial S^2} = 0$ in GBM, the gamma expression simplifies. Show that $\Gamma = \frac{1}{S^2}\mathbb{E}^{t,S}[e^{-r\tau}\Phi''(S_T)S_T^2]$, and explain why this is only formal (not rigorous) for the call payoff.

??? success "Solution to Exercise 4"
    Starting from the general gamma formula, with two terms involving $\Phi''(S_T)$ and $\frac{\partial^2 S_T}{\partial S^2}$:

    For GBM, $S_T = S \cdot e^{(\cdots)}$ is linear in $S$, so $\frac{\partial^2 S_T}{\partial S^2} = 0$. The gamma reduces to

    $$
    \Gamma = \mathbb{E}^{t,S}\!\left[e^{-r\tau} \Phi''(S_T) \left(\frac{S_T}{S}\right)^2\right] = \frac{1}{S^2}\mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi''(S_T) S_T^2\right]
    $$

    For the call payoff $\Phi(x) = (x - K)^+$, we have $\Phi'(x) = \mathbf{1}_{x>K}$ and $\Phi''(x) = \delta(x - K)$ in the distributional sense. The expression $\mathbb{E}[e^{-r\tau}\delta(S_T - K)S_T^2]$ is only formal because:

    1. The Dirac delta $\delta(x-K)$ is not a function but a distribution. It cannot be pointwise evaluated at a random variable.
    2. The pathwise interchange of differentiation and expectation that leads to this formula requires $\Phi \in C^2$, which the call payoff violates.
    3. A rigorous treatment requires either smoothing the payoff (replacing $\Phi$ by a mollified version $\Phi_\epsilon$ and taking limits) or using the likelihood ratio/Malliavin approach to avoid differentiating $\Phi$ altogether.

    Nevertheless, the formal expression can be given meaning: $\mathbb{E}[\delta(S_T - K) \cdot g(S_T)] = g(K) \cdot p_{S_T}(K)$ where $p_{S_T}$ is the density of $S_T$, yielding $\Gamma = \frac{e^{-r\tau} K^2}{S^2} p_{S_T}(K) = \frac{N'(d_1)}{S\sigma\sqrt{\tau}}$.

---

**Exercise 5.** For a general diffusion $dS_t = \mu(t, S_t)\,dt + \sigma(t, S_t)\,dW_t$, the variational equation for $Y_t = \partial S_t / \partial S_0$ is $dY_t = \mu'(t,S_t)Y_t\,dt + \sigma'(t,S_t)Y_t\,dW_t$ with $Y_0 = 1$. For the CEV model $\sigma(S) = \sigma_0 S^{\beta-1}$, compute $\sigma'(S)$ and write down the variational equation. Does $Y_T = S_T/S_0$ still hold?

??? success "Solution to Exercise 5"
    For the CEV model with $\sigma(S) = \sigma_0 S^{\beta - 1}$, we compute

    $$
    \sigma'(S) = \frac{\partial}{\partial S}\left(\sigma_0 S^{\beta-1}\right) = \sigma_0(\beta - 1)S^{\beta - 2}
    $$

    The variational equation for $Y_t = \partial S_t / \partial S_0$ becomes

    $$
    dY_t = \mu'(t, S_t) Y_t \, dt + \sigma_0(\beta - 1) S_t^{\beta - 2} Y_t \, dW_t, \quad Y_0 = 1
    $$

    where $\mu'(t, S_t) = r$ if the drift is $\mu(S) = rS$.

    The identity $Y_T = S_T / S_0$ does **not** hold in general for the CEV model when $\beta \neq 1$. This identity relies on the SDE being linear in $S$ (i.e., both drift and diffusion being proportional to $S$). In the CEV model, the diffusion coefficient $\sigma_0 S^\beta$ is nonlinear in $S$ when $\beta \neq 1$, so the stochastic flow is no longer simply $S_T/S_0$. One must simulate the variational equation alongside the forward path to obtain $Y_T$.

    In the special case $\beta = 1$, the CEV model reduces to geometric Brownian motion, $\sigma'(S) = 0$, the variational equation becomes $dY_t = rY_t\,dt$, giving $Y_T = e^{r\tau}$. But $S_T/S_0 = e^{(r-\frac{1}{2}\sigma_0^2)\tau + \sigma_0 W_\tau}$, which does not equal $e^{r\tau}$ either. The correct statement for GBM is that both numerator and denominator in $Y_T = S_T/S_0$ share the same Brownian increments. The variational equation for GBM gives $dY_t = rY_t\,dt + \sigma_0 Y_t\,dW_t$ (since $\sigma'(S) = 0$ for $\beta=1$ but the full diffusion term in the variational equation involves $\sigma'(S_t)Y_t$, which vanishes), which indeed has the solution $Y_T = S_T/S_0$.

---

**Exercise 6.** Describe the Monte Carlo workflow for computing delta and vega simultaneously along a single set of simulated paths. How many additional function evaluations are needed per path compared to computing the price alone? What are the advantages of pathwise estimation over finite-difference estimation in this context?

??? success "Solution to Exercise 6"
    **Workflow for simultaneous delta and vega estimation:**

    For each of $N$ simulated paths, indexed by $i = 1, \ldots, N$:

    1. Draw $Z^{(i)} \sim \mathcal{N}(0,1)$
    2. Compute $S_T^{(i)} = S \exp\!\left((r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z^{(i)}\right)$
    3. Evaluate the payoff $\Phi(S_T^{(i)})$ and its derivative $\Phi'(S_T^{(i)})$
    4. Compute the **price** contribution: $e^{-r\tau}\Phi(S_T^{(i)})$
    5. Compute the **delta** contribution: $e^{-r\tau}\Phi'(S_T^{(i)}) \cdot S_T^{(i)} / S$
    6. Compute the **vega** contribution: $e^{-r\tau}\Phi'(S_T^{(i)}) \cdot S_T^{(i)}(\sqrt{\tau}Z^{(i)} - \sigma\tau)$

    Average each to obtain $\hat{V}$, $\hat{\Delta}$, and $\hat{\nu}$.

    **Additional cost per path:** Only one extra function evaluation ($\Phi'$) is needed. The quantities $S_T^{(i)}/S$ and $S_T^{(i)}(\sqrt{\tau}Z^{(i)} - \sigma\tau)$ are simple arithmetic operations on already-computed values. So the marginal cost is essentially one evaluation of $\Phi'$ per path, regardless of how many Greeks are computed.

    **Advantages over finite differences:**

    - **Efficiency**: Finite-difference delta requires at least two price simulations (e.g., $V(S+h)$ and $V(S-h)$), each with $N$ paths. Pathwise estimation reuses the same $N$ paths for all Greeks simultaneously.
    - **No step-size tuning**: Finite differences require choosing $h$, balancing bias ($O(h^2)$ for central differences) against variance (which grows as $h \to 0$). Pathwise estimators are unbiased with no such tuning parameter.
    - **Correlation**: Since all Greeks are estimated from the same paths, their estimators are naturally correlated, which is useful for portfolio-level risk analysis and variance reduction via control variates.
