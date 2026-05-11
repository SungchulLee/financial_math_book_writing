# Fokker-Planck for Financial Models

The Fokker-Planck equation describes the evolution of probability density functions for diffusion processes. It is the forward equation counterpart to the backward Kolmogorov equation and provides crucial insights into the probability distribution of asset prices under various financial models.

## Key Concepts

See [Kolmogorov Forward Equation](kolmogorov_forward.md) for the definition and
derivation of the Fokker-Planck equation, and
[Transition Densities for Standard SDEs](transition_densities_standard_sdes.md) for
explicit densities of BM, OU, GBM, and CIR. The present page focuses on
finance-specific interpretation, calibration, and risk applications.

**Finance-specific interpretations:**

- **Geometric Brownian Motion (GBM)**: the log-price is Gaussian, which underpins the
  Black-Scholes distribution of terminal stock prices.
- **Cox-Ingersoll-Ross (CIR)**: the transition density is non-central chi-square under
  suitable parameter conditions, enabling analytic bond pricing.
- **Mean-reverting processes (OU, CIR)**: stationary densities encode long-run
  behavior and are the starting point for calibration to historical distributions.

!!! note "Practical Significance"
    Fokker-Planck equations enable:

    - Analytical computation of option prices (no boundary conditions needed unlike PDEs)
    - Calibration of model parameters to observed density features
    - Risk management through understanding the distribution of future asset values
    - Construction of transition probability matrices for discrete approximations

For the forward-vs-backward duality, see
[Forward–Backward Duality](forward_backward_duality.md).

---

## Exercises

**Exercise 1.**
Write the Fokker-Planck equation for the Ornstein-Uhlenbeck process $dX_t = -\kappa X_t\,dt + \sigma\,dB_t$. Verify that the stationary density $p_\infty(x) \propto \exp(-\kappa x^2/\sigma^2)$ satisfies $\mathcal{L}^* p_\infty = 0$.

??? success "Solution to Exercise 1"
    The Ornstein-Uhlenbeck process has $\mu(x) = -\kappa x$ and $\sigma(x) = \sigma$ (constant). The Fokker-Planck equation is:

    $$
    \frac{\partial p}{\partial t} = -\frac{\partial}{\partial x}[(-\kappa x)p] + \frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2 p] = \kappa\frac{\partial(xp)}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial x^2}
    $$

    The adjoint operator is:

    $$
    \mathcal{L}^* p = \kappa\frac{\partial(xp)}{\partial x} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial x^2}
    $$

    Now we verify that $p_\infty(x) = C\exp(-\kappa x^2/\sigma^2)$ satisfies $\mathcal{L}^* p_\infty = 0$. Compute:

    $$
    \frac{\partial(x p_\infty)}{\partial x} = p_\infty + x p_\infty' = p_\infty + x\left(-\frac{2\kappa x}{\sigma^2}\right)p_\infty = p_\infty\left(1 - \frac{2\kappa x^2}{\sigma^2}\right)
    $$

    $$
    \frac{\partial^2 p_\infty}{\partial x^2} = \frac{\partial}{\partial x}\left(-\frac{2\kappa x}{\sigma^2}p_\infty\right) = -\frac{2\kappa}{\sigma^2}p_\infty + \frac{4\kappa^2 x^2}{\sigma^4}p_\infty = p_\infty\left(-\frac{2\kappa}{\sigma^2} + \frac{4\kappa^2 x^2}{\sigma^4}\right)
    $$

    Therefore:

    $$
    \mathcal{L}^* p_\infty = \kappa p_\infty\left(1 - \frac{2\kappa x^2}{\sigma^2}\right) + \frac{\sigma^2}{2}p_\infty\left(-\frac{2\kappa}{\sigma^2} + \frac{4\kappa^2 x^2}{\sigma^4}\right)
    $$

    $$
    = p_\infty\left[\kappa - \frac{2\kappa^2 x^2}{\sigma^2} - \kappa + \frac{2\kappa^2 x^2}{\sigma^2}\right] = 0
    $$

    Thus $p_\infty(x) \propto \exp(-\kappa x^2/\sigma^2)$ is indeed the stationary density, which is a Gaussian $N(0, \sigma^2/(2\kappa))$.

---

**Exercise 2.**
Starting from the general Fokker-Planck equation for $dX_t = \mu(X_t, t)\,dt + \sigma(X_t, t)\,dB_t$, derive the Fokker-Planck equation for geometric Brownian motion $dS_t = \mu S_t\,dt + \sigma S_t\,dB_t$ by identifying $\mu(S) = \mu S$ and $\sigma(S) = \sigma S$. Expand all derivatives using the product rule.

??? success "Solution to Exercise 2"
    For GBM, $\mu(S) = \mu S$ and $\sigma(S) = \sigma S$. Substituting into the general Fokker-Planck equation:

    $$
    \frac{\partial p}{\partial t} = -\frac{\partial}{\partial S}[\mu S \cdot p] + \frac{1}{2}\frac{\partial^2}{\partial S^2}[\sigma^2 S^2 \cdot p]
    $$

    **Expanding the drift term** using the product rule:

    $$
    -\frac{\partial}{\partial S}[\mu S p] = -\mu\left(p + S\frac{\partial p}{\partial S}\right) = -\mu p - \mu S\frac{\partial p}{\partial S}
    $$

    **Expanding the diffusion term** — let $D(S) = \sigma^2 S^2$. First derivative:

    $$
    \frac{\partial}{\partial S}[\sigma^2 S^2 p] = 2\sigma^2 S p + \sigma^2 S^2 \frac{\partial p}{\partial S}
    $$

    Second derivative:

    $$
    \frac{\partial^2}{\partial S^2}[\sigma^2 S^2 p] = \frac{\partial}{\partial S}\left[2\sigma^2 S p + \sigma^2 S^2 \frac{\partial p}{\partial S}\right]
    $$

    $$
    = 2\sigma^2 p + 2\sigma^2 S\frac{\partial p}{\partial S} + 2\sigma^2 S\frac{\partial p}{\partial S} + \sigma^2 S^2\frac{\partial^2 p}{\partial S^2}
    $$

    $$
    = 2\sigma^2 p + 4\sigma^2 S\frac{\partial p}{\partial S} + \sigma^2 S^2\frac{\partial^2 p}{\partial S^2}
    $$

    **Combining:**

    $$
    \frac{\partial p}{\partial t} = -\mu p - \mu S\frac{\partial p}{\partial S} + \sigma^2 p + 2\sigma^2 S\frac{\partial p}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 p}{\partial S^2}
    $$

    $$
    = (\sigma^2 - \mu)p + (2\sigma^2 - \mu)S\frac{\partial p}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 p}{\partial S^2}
    $$

---

**Exercise 3.**
For the CIR process $dr_t = \kappa(\theta - r_t)\,dt + \sqrt{\gamma r_t}\,dB_t$, write down the Fokker-Planck equation. Determine the stationary density by solving $\mathcal{L}^* p_\infty = 0$ and identify it as a Gamma distribution. Under what condition on $\kappa$, $\theta$, and $\gamma$ is $p_\infty$ integrable?

??? success "Solution to Exercise 3"
    For the CIR process, $\mu(r) = \kappa(\theta - r)$ and $\sigma(r) = \sqrt{\gamma r}$, so $\sigma^2(r) = \gamma r$. The Fokker-Planck equation is:

    $$
    \frac{\partial p}{\partial t} = -\frac{\partial}{\partial r}[\kappa(\theta - r)p] + \frac{1}{2}\frac{\partial^2}{\partial r^2}[\gamma r \cdot p]
    $$

    For the stationary density, set $\partial_t p = 0$ and use the zero-current condition $J = 0$:

    $$
    \kappa(\theta - r)p_\infty = \frac{1}{2}\frac{d}{dr}[\gamma r \cdot p_\infty]
    $$

    Expanding the right side:

    $$
    \kappa(\theta - r)p_\infty = \frac{\gamma}{2}p_\infty + \frac{\gamma r}{2}p_\infty'
    $$

    Rearranging:

    $$
    p_\infty' = \frac{2\kappa(\theta - r) - \gamma}{\gamma r}p_\infty = \left(\frac{2\kappa\theta - \gamma}{\gamma r} - \frac{2\kappa}{\gamma}\right)p_\infty
    $$

    This ODE has the solution:

    $$
    p_\infty(r) \propto r^{(2\kappa\theta/\gamma) - 1}\exp\left(-\frac{2\kappa r}{\gamma}\right)
    $$

    This is a **Gamma distribution** with shape parameter $\alpha = 2\kappa\theta/\gamma$ and rate parameter $\beta = 2\kappa/\gamma$.

    For $p_\infty$ to be integrable (i.e., a valid density), we need the exponent of $r$ to satisfy $(2\kappa\theta/\gamma) - 1 > -1$, which gives the condition:

    $$
    \frac{2\kappa\theta}{\gamma} > 0
    $$

    This is automatically satisfied when $\kappa, \theta, \gamma > 0$. However, for $p_\infty(r)$ to be integrable near $r = 0$ (so the density does not blow up too fast), we need $\alpha = 2\kappa\theta/\gamma > 0$. The stronger **Feller condition** $2\kappa\theta \geq \gamma$ (i.e., $\alpha \geq 1$) ensures the density is bounded at the origin.

---

**Exercise 4.**
Using the Fokker-Planck derivation via Ito's lemma and test functions, show that for any smooth test function $f$ with compact support and any diffusion process $X_t$:

$$
\frac{d}{dt}\mathbb{E}[f(X_t)] = \mathbb{E}\left[\mu(X_t)f'(X_t) + \frac{1}{2}\sigma^2(X_t)f''(X_t)\right]
$$

Explain how integration by parts transfers the derivatives from $f$ to $p$.

??? success "Solution to Exercise 4"
    For a general diffusion $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dB_t$, apply Ito's lemma to a smooth test function $f$ with compact support:

    $$
    df(X_t) = f'(X_t)\,dX_t + \frac{1}{2}f''(X_t)\,d\langle X\rangle_t
    $$

    $$
    = \left[\mu(X_t)f'(X_t) + \frac{1}{2}\sigma^2(X_t)f''(X_t)\right]dt + \sigma(X_t)f'(X_t)\,dB_t
    $$

    Taking expectations (the stochastic integral vanishes since $f$ has compact support and is bounded):

    $$
    \frac{d}{dt}\mathbb{E}[f(X_t)] = \mathbb{E}\left[\mu(X_t)f'(X_t) + \frac{1}{2}\sigma^2(X_t)f''(X_t)\right]
    $$

    Now, writing expectations using the transition density $p(x, t)$:

    $$
    \frac{d}{dt}\int f(x)p(x,t)\,dx = \int\left[\mu(x)f'(x) + \frac{\sigma^2(x)}{2}f''(x)\right]p(x,t)\,dx
    $$

    **Integration by parts** transfers the derivatives from $f$ to $p$:

    For the drift term:

    $$
    \int \mu(x)f'(x)p\,dx = -\int f(x)\frac{\partial}{\partial x}[\mu(x)p]\,dx
    $$

    (boundary terms vanish because $f$ has compact support).

    For the diffusion term (integrating by parts twice):

    $$
    \int \frac{\sigma^2(x)}{2}f''(x)p\,dx = \int f(x)\frac{1}{2}\frac{\partial^2}{\partial x^2}[\sigma^2(x)p]\,dx
    $$

    The net effect is that each derivative on $f$ is transferred to the product of the coefficient and $p$, with a sign change per integration by parts. This transforms the generator $\mathcal{L}$ acting on $f$ into the adjoint $\mathcal{L}^*$ acting on $p$.

---

**Exercise 5.**
For geometric Brownian motion with drift $\mu$ and volatility $\sigma$, verify that the log-normal density

$$
p(y, t) = \frac{1}{\sigma\sqrt{2\pi t}} \exp\left(-\frac{(y - (\mu - \sigma^2/2)t)^2}{2\sigma^2 t}\right)
$$

(where $y = \ln S$) satisfies the Fokker-Planck equation in log-space. What is the Fokker-Planck equation in the original $S$ variable?

??? success "Solution to Exercise 5"
    In log-space with $y = \ln S$, Ito's lemma gives $dY_t = (\mu - \sigma^2/2)\,dt + \sigma\,dB_t$. This is Brownian motion with drift $\tilde{\mu} = \mu - \sigma^2/2$ and diffusion coefficient $\sigma$, so the Fokker-Planck equation in log-space is:

    $$
    \frac{\partial p}{\partial t} = -\tilde{\mu}\frac{\partial p}{\partial y} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial y^2} = -\left(\mu - \frac{\sigma^2}{2}\right)\frac{\partial p}{\partial y} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial y^2}
    $$

    **Verification**: The given density is $p(y,t) = \frac{1}{\sigma\sqrt{2\pi t}}\exp\left(-\frac{(y - \tilde{\mu}t)^2}{2\sigma^2 t}\right)$. Let $z = y - \tilde{\mu}t$. Then:

    $$
    \frac{\partial p}{\partial t} = p\left[-\frac{1}{2t} + \frac{z^2}{2\sigma^2 t^2} + \frac{\tilde{\mu}z}{\sigma^2 t}\right]
    $$

    $$
    \frac{\partial p}{\partial y} = -\frac{z}{\sigma^2 t}p, \qquad \frac{\partial^2 p}{\partial y^2} = \left(\frac{z^2}{\sigma^4 t^2} - \frac{1}{\sigma^2 t}\right)p
    $$

    Computing the right-hand side:

    $$
    -\tilde{\mu}\frac{\partial p}{\partial y} + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial y^2} = \frac{\tilde{\mu}z}{\sigma^2 t}p + \frac{\sigma^2}{2}\left(\frac{z^2}{\sigma^4 t^2} - \frac{1}{\sigma^2 t}\right)p
    $$

    $$
    = p\left[\frac{\tilde{\mu}z}{\sigma^2 t} + \frac{z^2}{2\sigma^2 t^2} - \frac{1}{2t}\right] = \frac{\partial p}{\partial t}
    $$

    The Fokker-Planck equation in the original $S$ variable is:

    $$
    \frac{\partial p}{\partial t} = -\frac{\partial}{\partial S}[\mu S \cdot p] + \frac{1}{2}\frac{\partial^2}{\partial S^2}[\sigma^2 S^2 \cdot p]
    $$

---

**Exercise 6.**
Explain why the Fokker-Planck equation for the Ornstein-Uhlenbeck process has a well-defined stationary distribution while standard Brownian motion does not. Relate this to the sign of the mean-reversion parameter $\kappa$ and the behavior of the probability current $J(x) = \mu(x)p - \frac{1}{2}\partial_x[\sigma^2 p]$ at stationarity.

??? success "Solution to Exercise 6"
    **Ornstein-Uhlenbeck process**: The Fokker-Planck equation is $\partial_t p = \kappa\partial_x(xp) + \frac{\sigma^2}{2}\partial_{xx}p$. The drift $\mu(x) = -\kappa x$ with $\kappa > 0$ pushes probability mass back toward zero. The probability current is:

    $$
    J(x) = -\kappa x \cdot p - \frac{\sigma^2}{2}\frac{\partial p}{\partial x}
    $$

    At stationarity, $J = 0$, which gives the ODE $-\kappa x\,p_\infty = \frac{\sigma^2}{2}p_\infty'$. This yields $p_\infty \propto \exp(-\kappa x^2/\sigma^2)$, a Gaussian with finite variance $\sigma^2/(2\kappa)$. The key is that the mean-reverting drift confines probability mass to a bounded region.

    **Standard Brownian motion**: Here $\mu = 0$ and $\sigma = 1$, so the Fokker-Planck equation is $\partial_t p = \frac{1}{2}\partial_{xx}p$. The probability current at stationarity would require $J = -\frac{1}{2}\partial_x p = 0$, which means $p_\infty = \text{const}$. But a constant on $\mathbb{R}$ is not integrable, so no stationary density exists.

    The fundamental difference is the sign and nature of the drift:

    - When $\kappa > 0$, the drift $-\kappa x$ creates a restoring force that balances diffusion, producing a normalizable stationary density.
    - When there is no drift, diffusion spreads probability mass indefinitely, and the variance grows as $t$ without bound.

---

**Exercise 7.**
In the table comparing forward and backward equations, the forward equation describes the evolution of density while the backward equation describes PDE solutions for expected values. For a European call option with payoff $g(S_T) = (S_T - K)^+$, explain which equation you would use to find the option price and which you would use to find the terminal distribution of $S_T$. How are the two approaches connected via the identity $\mathbb{E}[g(X_T)] = \int g(x)\,p(x, T)\,dx$?

??? success "Solution to Exercise 7"
    **Option pricing (backward equation)**: To find the option price $V(t, S) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+ \mid S_t = S]$, we use the **backward Kolmogorov equation** (or equivalently the Black-Scholes PDE):

    $$
    \frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = rV
    $$

    with terminal condition $V(T, S) = (S - K)^+$. This PDE is solved backward from $T$ to $t$ and gives the option price as a function of the current stock price and time.

    **Terminal distribution (forward equation)**: To find the probability density of $S_T$ under the risk-neutral measure, we solve the **Fokker-Planck (forward) equation**:

    $$
    \frac{\partial p}{\partial t} = -\frac{\partial}{\partial S}[rS \cdot p] + \frac{1}{2}\frac{\partial^2}{\partial S^2}[\sigma^2 S^2 \cdot p]
    $$

    with initial condition $p(S, 0 \mid S_0) = \delta(S - S_0)$.

    **Connection**: The two approaches are linked by the identity:

    $$
    V(0, S_0) = e^{-rT}\mathbb{E}^{\mathbb{Q}}[g(S_T)] = e^{-rT}\int_0^{\infty} g(S)\,p(S, T \mid S_0, 0)\,dS
    $$

    The backward approach solves one PDE (with terminal condition $g$) and evaluates at the initial point — efficient when we want the price for one payoff at many initial prices. The forward approach solves another PDE (with delta initial condition) and integrates against $g$ — efficient when we want to price many different payoffs for the same initial condition, since the density $p$ can be reused for any payoff $g$.
