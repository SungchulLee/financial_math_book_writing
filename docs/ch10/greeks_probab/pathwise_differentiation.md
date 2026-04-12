# Pathwise Differentiation


Pathwise differentiation computes Greeks by differentiating sample paths with respect to parameters or initial data.

---

## Mathematical framework


The key idea is to interchange differentiation and expectation:

$$
\frac{\partial}{\partial \theta} \mathbb{E}[\Phi(S_T^\theta)] = \mathbb{E}\left[\Phi'(S_T^\theta) \frac{\partial S_T^\theta}{\partial \theta}\right]
$$

**Justification.** This interchange is valid under dominated convergence if:

1. $\Phi$ is Lipschitz continuous (hence a.e. differentiable)
2. $\frac{\partial S_T^\theta}{\partial \theta}$ exists a.s. and is integrable
3. There exists an integrable dominating function: $|\Phi'(S_T^\theta) \frac{\partial S_T^\theta}{\partial \theta}| \leq g(S_T)$ with $\mathbb{E}[g(S_T)] < \infty$

For smooth payoffs with polynomial growth, condition (3) follows from moment bounds on $S_T$ and its Jacobian.

---

## Delta (Black–Scholes)


Since $\partial S_T/\partial S = S_T/S$,

$$
\Delta(t,S)=\mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\frac{S_T}{S}\right]
$$


for smooth $\Phi$.

**Explicit verification.** For the log-normal model:

$$
S_T = S \exp\!\left((r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z\right), \quad Z \sim \mathcal{N}(0,1)
$$

The Jacobian $\frac{\partial S_T}{\partial S} = \frac{S_T}{S}$ satisfies $\mathbb{E}[(\frac{S_T}{S})^2] = e^{\sigma^2\tau} < \infty$.

For a call with $\Phi(x) = (x-K)^+$ (which is Lipschitz but not smooth), the formula still yields:

$$
\Delta = \mathbb{E}^{t,S}\!\left[e^{-r\tau}\mathbf{1}_{S_T > K}\frac{S_T}{S}\right] = e^{-r\tau}\mathbb{E}\!\left[\mathbf{1}_{S_T > K}\frac{S_T}{S}\right]
$$

This equals $N(d_1)$ after evaluation.

---

## Vega (Black–Scholes)


Differentiate $S_T$ with respect to $\sigma$:

$$
S_T = S \exp\!\left((r - \frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z\right)
$$

$$
\frac{\partial S_T}{\partial \sigma}
=
S_T\left(\sqrt{\tau}Z - \sigma\tau\right)
$$

Thus, for smooth $\Phi$,

$$
\boxed{
\nu(t,S)=
\mathbb{E}^{t,S}\!\left[e^{-r\tau}\Phi'(S_T)\,S_T\left(\sqrt{\tau}Z - \sigma\tau\right)\right]
}
$$

**Integrability condition.** Since $|Z|e^{aZ}$ has finite moments for Gaussian $Z$, the pathwise vega estimator is well-defined.

---

## Rho (Black–Scholes)


Differentiate with respect to $r$:

$$
\frac{\partial S_T}{\partial r} = S_T \cdot \tau
$$

and the discount factor contributes $-\tau e^{-r\tau}$. Thus:

$$
\rho = \mathbb{E}^{t,S}\!\left[-\tau e^{-r\tau}\Phi(S_T) + e^{-r\tau}\Phi'(S_T) \cdot S_T \tau\right]
$$

For a call, this simplifies to $\rho = K\tau e^{-r\tau}N(d_2)$.

---

## Limitation: non-smooth payoffs


If $\Phi$ has kinks, $\Phi'$ is discontinuous and pathwise differentiation faces issues:

1. **Delta for calls/puts**: $\Phi'(x) = \mathbf{1}_{x > K}$ is well-defined a.e., so delta works
2. **Gamma**: $\Phi''(x) = \delta(S-K)$ is distributional, so naive pathwise differentiation fails
3. **Digital options**: $\Phi(x) = \mathbf{1}_{x > K}$, so $\Phi' = \delta(S-K)$ and pathwise delta fails

For these cases, likelihood ratio methods avoid derivatives of $\Phi$ entirely.

---

## Comparison: pathwise vs likelihood ratio


| Method | Requires smooth $\Phi$? | Variance | Implementation |
|:-------|:-------------------------|:---------|:---------------|
| Pathwise | Yes (or Lipschitz) | Lower | Differentiate paths |
| Likelihood ratio | No | Higher | Differentiate density |

**Rule of thumb**: Use pathwise when possible (smooth payoffs), switch to LR for digital/barrier options.

---

## Monte Carlo Implementation: Finite Difference Methods

The simplest computational approach is finite difference approximation:

$$
\frac{\partial V}{\partial \theta} \approx \frac{V(\theta + d\theta) - V(\theta)}{d\theta} \quad \text{(Forward Difference)}
$$

$$
\frac{\partial V}{\partial \theta} \approx \frac{V(\theta) - V(\theta - d\theta)}{d\theta} \quad \text{(Backward Difference)}
$$

$$
\frac{\partial V}{\partial \theta} \approx \frac{V(\theta + d\theta) - V(\theta - d\theta)}{2d\theta} \quad \text{(Central Difference, second-order)}
$$

Central differences have $O(d\theta^2)$ error, while forward and backward differences have $O(d\theta)$ error. The practical challenge is choosing $d\theta$ to balance discretization error and sampling noise.

---

## Likelihood Ratio Method

The likelihood ratio method, also called the score function method, computes Greeks without differentiating the payoff function. Instead, it differentiates the probability density:

$$
\frac{\partial V}{\partial \theta} = e^{-r\tau} \int V(T,S) \frac{\partial f_\theta(s)}{\partial \theta} ds
$$

Rewriting using the density:

$$
\frac{\partial V}{\partial \theta} = e^{-r\tau} \int V(T,S) \frac{\partial \log f_\theta(s)}{\partial \theta} f_\theta(s) ds = e^{-r\tau} \mathbb{E}\left[V(T,S) \frac{\partial \log f(S_T)}{\partial \theta}\right]
$$

### Likelihood Ratio Delta

For a Black–Scholes stock process with parameter $\theta = S_0$ (initial price):

$$
S_T = S_0 \exp\left(\left(r - \frac{1}{2}\sigma^2\right)\tau + \sigma\sqrt{\tau}Z\right), \quad Z \sim \mathcal{N}(0,1)
$$

Taking the log derivative with respect to $S_0$:

$$
\frac{\partial \log f(S_T)}{\partial S_0} = \frac{1}{S_0}
$$

Thus:

$$
\Delta = e^{-r\tau} \mathbb{E}\left[V(T,S_T) \cdot \frac{1}{S_0}\right]
$$

For a call option, this becomes:

$$
\Delta = \frac{e^{-r\tau}}{S_0} \mathbb{E}[(S_T - K)^+ ]
$$

### Likelihood Ratio Vega

For volatility parameter $\theta = \sigma$:

$$
S_T = S_0 \exp\left(\left(r - \frac{1}{2}\sigma^2\right)\tau + \sigma\sqrt{\tau}Z\right)
$$

The score function (log derivative of density) with respect to $\sigma$ is:

$$
\frac{\partial \log f(S_T)}{\partial \sigma} = \frac{1}{\sigma^3\tau}\left(\log(S_T/S_0) - \left(r - \frac{1}{2}\sigma^2\right)\tau\right) \cdot \left(\sqrt{\tau}Z - \sigma\tau\right)
$$

Simplifying:

$$
\nu = \frac{e^{-r\tau}}{\sigma\tau} \mathbb{E}\left[\max(S_T - K, 0) \left(\sqrt{\tau}Z - \sigma\tau\right)\right]
$$

The advantage of likelihood ratio is that it works for non-smooth payoffs (e.g., digital options) where pathwise differentiation fails.

---

## Pathwise Delta in Heston Model

For the Heston stochastic volatility model:

$$
dS(t) = rS(t)dt + \sqrt{v(t)}S(t)dW_x^{\mathbb{Q}}(t)
$$

The pathwise delta under Heston is:

$$
\Delta = e^{-r\tau} \mathbb{E}^{\mathbb{Q}}\left[\Phi'(S_T) \frac{S_T}{S_0}\right]
$$

The key difference from Black–Scholes is that the Jacobian $\frac{\partial S_T}{\partial S_0}$ still equals $\frac{S_T}{S_0}$ due to linearity in the drift coefficient with respect to $S$, but the path-dependent volatility introduces additional variance in the Monte Carlo estimator.

---

## What to remember


- Pathwise methods are natural for smooth payoffs and have lower variance.
- Interchange of $\partial/\partial\theta$ and $\mathbb{E}$ requires dominated convergence conditions.
- For Lipschitz payoffs, pathwise delta and vega are well-defined.
- Likelihood ratio methods work for kinked payoffs (gamma, digital options) but exhibit higher variance.
- Finite difference is simple to implement but requires careful choice of step size $d\theta$.
- Heston model preserves pathwise delta formula but increases sampling variance due to stochastic volatility.

---

## Exercises

**Exercise 1.** For a European call with payoff $\Phi(x) = (x - K)^+$, verify that $\Phi'(x) = \mathbf{1}_{x > K}$ almost everywhere, and that the pathwise delta formula $\Delta = \mathbb{E}^{t,S}[e^{-r\tau}\mathbf{1}_{S_T > K} \cdot S_T/S]$ is well-defined despite the kink in the payoff.

??? success "Solution to Exercise 1"
    The call payoff is $\Phi(x) = (x - K)^+ = \max(x - K, 0)$. This function is continuous, convex, and piecewise linear with a kink at $x = K$. It is differentiable everywhere except at $x = K$, with

    $$
    \Phi'(x) = \begin{cases} 0 & x < K \\ 1 & x > K \end{cases}
    $$

    At $x = K$, the left derivative is 0 and the right derivative is 1. Since $S_T$ has a continuous (log-normal) distribution, $\mathbb{P}(S_T = K) = 0$, so $\Phi'(S_T) = \mathbf{1}_{S_T > K}$ holds almost surely.

    The pathwise delta formula gives

    $$
    \Delta = \mathbb{E}^{t,S}\!\left[e^{-r\tau} \mathbf{1}_{S_T > K} \cdot \frac{S_T}{S}\right]
    $$

    This is well-defined because the integrand is bounded by $e^{-r\tau} S_T / S$, and $\mathbb{E}[S_T/S] = e^{r\tau} < \infty$ under the log-normal model. The Lipschitz property of $\Phi$ (with Lipschitz constant 1) ensures the dominated convergence condition is satisfied: $|\Phi'(S_T)| \leq 1$, so $|\Phi'(S_T) \cdot S_T/S| \leq S_T/S$, which is integrable.

    Thus the interchange of differentiation and expectation is justified despite the kink, because the kink occurs on a set of measure zero under the continuous distribution of $S_T$.

---

**Exercise 2.** Compute the pathwise vega weight $\frac{\partial S_T}{\partial \sigma} = S_T(\sqrt{\tau}Z - \sigma\tau)$ for $S = 100$, $\sigma = 0.20$, $\tau = 0.5$, and a specific realization $Z = 1.5$. What is $S_T$ in this case, and what is the vega contribution from this single path?

??? success "Solution to Exercise 2"
    Given $S = 100$, $\sigma = 0.20$, $\tau = 0.5$, and $Z = 1.5$, first compute $S_T$:

    $$
    S_T = 100 \exp\!\left((r - \tfrac{1}{2}(0.04))(0.5) + 0.20\sqrt{0.5}(1.5)\right)
    $$

    Taking $r = 0.05$ (a typical value):

    $$
    S_T = 100 \exp\!\left((0.05 - 0.02)(0.5) + 0.20 \times 0.7071 \times 1.5\right) = 100 \exp(0.015 + 0.2121) = 100 \exp(0.2271) \approx 125.50
    $$

    The vega weight is

    $$
    \frac{\partial S_T}{\partial \sigma} = S_T(\sqrt{\tau}Z - \sigma\tau) = 125.50 \times (0.7071 \times 1.5 - 0.20 \times 0.5)
    $$

    $$
    = 125.50 \times (1.0607 - 0.10) = 125.50 \times 0.9607 \approx 120.57
    $$

    The vega contribution from this single path (for a call with strike $K < S_T$) would be $e^{-r\tau} \Phi'(S_T) \times 120.57$. For a smooth payoff where $\Phi'(S_T)$ is known, this gives the single-path vega estimate. The large magnitude of the weight ($\approx 120.57$) indicates substantial sensitivity of this particular path to volatility.

---

**Exercise 3.** For a digital option with payoff $\Phi(x) = \mathbf{1}_{x > K}$, we have $\Phi'(x) = \delta(x - K)$. Explain why the pathwise delta formula fails for this payoff. What would a naive Monte Carlo estimator of $\mathbb{E}[e^{-r\tau}\delta(S_T - K) \cdot S_T/S]$ compute, and why is it not useful?

??? success "Solution to Exercise 3"
    For the digital payoff $\Phi(x) = \mathbf{1}_{x > K}$, the derivative in the distributional sense is $\Phi'(x) = \delta(x - K)$, the Dirac delta at $K$.

    The pathwise delta formula would formally give

    $$
    \Delta = \mathbb{E}\!\left[e^{-r\tau} \delta(S_T - K) \cdot \frac{S_T}{S}\right]
    $$

    This fails for several reasons:

    1. **The Dirac delta is not a function.** It is a distribution (generalized function), and $\delta(S_T - K)$ cannot be evaluated pointwise at a random variable. The expression $\delta(S_T - K)$ is not a well-defined random variable.

    2. **A naive Monte Carlo estimator is useless.** In simulation, $S_T^{(i)}$ is a continuous random variable, so $\mathbb{P}(S_T^{(i)} = K) = 0$ for every path. A naive implementation that checks whether $S_T = K$ would return zero for every single simulated path, giving $\hat{\Delta} = 0$ regardless of $N$. This is not a consistent estimator.

    3. **The interchange of differentiation and expectation is not valid** because $\Phi$ is not Lipschitz (it is discontinuous). The dominated convergence theorem cannot be applied since the difference quotients $(\Phi(x+h) - \Phi(x))/h$ do not converge to a bounded function near $x = K$.

    The correct digital delta is $e^{-r\tau} p_{S_T}(K) \cdot K/S$, where $p_{S_T}$ is the log-normal density. This must be obtained via the likelihood ratio method, which avoids differentiating the payoff.

---

**Exercise 4.** The central difference approximation $\frac{\partial V}{\partial \theta} \approx \frac{V(\theta + d\theta) - V(\theta - d\theta)}{2d\theta}$ has $O(d\theta^2)$ error. If $V$ is estimated by Monte Carlo with $N = 10^6$ paths, the sampling error is approximately $\epsilon \sim N^{-1/2} \approx 10^{-3}$. What is the optimal $d\theta$ that balances discretization and sampling errors?

??? success "Solution to Exercise 4"
    The total error in the central difference estimator is

    $$
    \text{Error} = \underbrace{C \cdot d\theta^2}_{\text{discretization bias}} + \underbrace{\frac{\epsilon}{d\theta}}_{\text{amplified sampling noise}}
    $$

    The discretization error is $O(d\theta^2)$ for central differences. The sampling error in each $V(\theta \pm d\theta)$ is approximately $\epsilon \approx 10^{-3}$, and taking the difference amplifies this by $1/d\theta$ (since $\text{Var}[(V_+ - V_-)/2d\theta] \approx \epsilon^2/d\theta^2$ when using independent paths).

    Minimizing the total error, we set the derivative with respect to $d\theta$ to zero:

    $$
    \frac{d}{d(d\theta)}\left(C \cdot d\theta^2 + \frac{\epsilon}{d\theta}\right) = 2C \cdot d\theta - \frac{\epsilon}{d\theta^2} = 0
    $$

    Solving: $d\theta^3 = \frac{\epsilon}{2C}$, so

    $$
    d\theta^* \sim \epsilon^{1/3} \approx (10^{-3})^{1/3} = 10^{-1} = 0.1
    $$

    For a parameter like the initial stock price $S = 100$, this means $d S \approx 0.1$, i.e., roughly a 0.1% perturbation. For volatility $\sigma = 0.20$, this means $d\sigma \approx 0.1 \times \sigma \approx 0.02$.

    At the optimal step size, the total error is $O(\epsilon^{2/3}) \approx 10^{-2}$, which is worse than both the pure discretization and pure sampling errors individually. This illustrates the fundamental limitation of finite-difference Greeks in Monte Carlo: the step size cannot be made too small (noise amplification) or too large (bias).

---

**Exercise 5.** In the Heston model, the pathwise delta formula is $\Delta = e^{-r\tau}\mathbb{E}^{\mathbb{Q}}[\Phi'(S_T) \cdot S_T/S_0]$, the same form as Black--Scholes. Explain why the Jacobian $\partial S_T / \partial S_0 = S_T/S_0$ still holds despite stochastic volatility. Does the pathwise vega formula change in the Heston model?

??? success "Solution to Exercise 5"
    In the Heston model, the stock price SDE is $dS_t = rS_t\,dt + \sqrt{v_t}S_t\,dW_x^{\mathbb{Q}}$. The key observation is that both the drift $\mu(S) = rS$ and the diffusion $\sigma(S, v) = \sqrt{v}S$ are **linear in** $S$. The volatility $v_t$ follows its own process but does not depend on $S_0$.

    The Jacobian $Y_t = \partial S_t / \partial S_0$ satisfies the variational equation

    $$
    dY_t = rY_t\,dt + \sqrt{v_t}Y_t\,dW_x^{\mathbb{Q}}, \quad Y_0 = 1
    $$

    Since $S_t$ itself satisfies $dS_t = rS_t\,dt + \sqrt{v_t}S_t\,dW_x^{\mathbb{Q}}$, we see that $S_t/S_0$ satisfies the same SDE as $Y_t$ with the same initial condition $S_0/S_0 = 1$. By uniqueness of solutions, $Y_t = S_t/S_0$ for all $t$. Hence $\partial S_T / \partial S_0 = S_T / S_0$ still holds.

    The pathwise vega formula **does change** in the Heston model. Vega (sensitivity to the initial variance $v_0$) requires differentiating $S_T$ with respect to $v_0$. Since $v_0$ affects $v_t$ for all $t$ through the variance process, and $v_t$ enters the stock SDE through $\sqrt{v_t}$, the sensitivity $\partial S_T / \partial v_0$ involves the coupled system:

    $$
    \frac{\partial S_T}{\partial v_0} = \int_0^T \frac{\partial(\sqrt{v_s}S_s)}{\partial v_0}\,dW_x^{\mathbb{Q}} + \ldots
    $$

    This requires simulating the joint sensitivity of $(S_t, v_t)$ with respect to $v_0$, which is more complex than in Black--Scholes and does not yield a simple closed-form weight.

---

**Exercise 6.** The dominated convergence conditions for interchanging $\partial/\partial\theta$ and $\mathbb{E}$ require an integrable dominating function. For a power payoff $\Phi(x) = x^3$, verify that the condition $|\Phi'(S_T) \cdot S_T/S| \leq g(S_T)$ is satisfied for some integrable $g$ under the log-normal distribution. What happens for payoffs with exponential growth, such as $\Phi(x) = e^x$?

??? success "Solution to Exercise 6"
    For $\Phi(x) = x^3$, we have $\Phi'(x) = 3x^2$. The integrand in the pathwise delta formula is

    $$
    \left|\Phi'(S_T) \cdot \frac{S_T}{S}\right| = \frac{3S_T^3}{S}
    $$

    We need $\mathbb{E}[S_T^3] < \infty$. Under the log-normal distribution, $S_T = S e^{(r-\frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z}$, so

    $$
    \mathbb{E}[S_T^3] = S^3 e^{3(r-\frac{1}{2}\sigma^2)\tau} \mathbb{E}[e^{3\sigma\sqrt{\tau}Z}] = S^3 e^{3(r-\frac{1}{2}\sigma^2)\tau + \frac{9}{2}\sigma^2\tau}
    $$

    This is finite for all finite $\sigma, \tau$. So we can take $g(S_T) = 3S_T^3/S$, which is integrable, and the dominated convergence condition is satisfied.

    For $\Phi(x) = e^x$, we have $\Phi'(x) = e^x$, so the integrand becomes

    $$
    \left|\Phi'(S_T) \cdot \frac{S_T}{S}\right| = \frac{S_T e^{S_T}}{S}
    $$

    We need $\mathbb{E}[S_T e^{S_T}] < \infty$. Since $S_T$ is log-normal, $e^{S_T} = \exp(S e^{(r-\frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}Z})$. For large $Z$, this grows as $\exp(Ce^{\sigma\sqrt{\tau}Z})$, which is a double exponential in $Z$. The Gaussian density $e^{-z^2/2}$ decays only as a single exponential, so

    $$
    \mathbb{E}[e^{S_T}] = \int_{-\infty}^{\infty} \exp\!\left(S e^{(r-\frac{1}{2}\sigma^2)\tau + \sigma\sqrt{\tau}z}\right) \frac{e^{-z^2/2}}{\sqrt{2\pi}}\,dz = \infty
    $$

    The expectation diverges. Therefore the dominated convergence condition fails, and the pathwise interchange of differentiation and expectation is not justified for payoffs with exponential growth. Such payoffs require alternative approaches (e.g., truncation or working with the Laplace transform).
