# Moment Analysis of SDEs

In many stochastic differential equations the full probability distribution of the solution is difficult or impossible to obtain explicitly. Moment analysis provides an alternative: instead of solving for the entire distribution, we track a small set of summary statistics — expectations, variances, and correlations — that already capture many economically and physically relevant properties such as growth rates, volatility, persistence, and equilibrium behavior.

For Gaussian processes such as Brownian motion and the Ornstein–Uhlenbeck process, the distribution is fully determined by the first two moments. For nonlinear diffusion models such as geometric Brownian motion and the CIR process, higher moments reveal how multiplicative or state-dependent noise affects skewness, tail behavior, and long-run variability.

The models in this section illustrate three fundamental types of stochastic behavior: **pure diffusion** (Brownian motion), **multiplicative noise** (geometric Brownian motion), and **mean reversion** (Vasicek and CIR). For each model we develop moment formulas using three main techniques: direct computation from explicit solutions, Itô's lemma applied to powers, and moment ODEs derived from the infinitesimal generator.

!!! abstract "Learning Goals"
    After completing this section you should be able to:

    - compute expectations, variances, and higher moments for Gaussian and log-normal SDE models
    - use Itô isometry to evaluate variances of stochastic integrals
    - derive moment ODEs using Itô's lemma applied to powers of the process
    - understand how mean reversion produces stationary distributions
    - recognize the effect of state-dependent volatility on variance formulas

---

## 1. Brownian Motion

## SDE

The standard Brownian motion $B_t$ satisfies

$$
dB_t = dW_t, \quad B_0 = 0
$$

## Moments

By definition of standard Brownian motion, $B_t$ has distribution $\mathcal{N}(0, t)$:

$$
\mathbb{E}[B_t] = 0, \quad \operatorname{Var}(B_t) = t
$$

## Higher Moments

For a centered Gaussian random variable $X \sim \mathcal{N}(0, \sigma^2)$, all odd moments vanish by symmetry. The even moments are

$$
\mathbb{E}[X^{2k}] = \sigma^{2k} (2k-1)!! = \sigma^{2k} \cdot \frac{(2k)!}{2^k k!}
$$

where $(2k-1)!! = 1 \cdot 3 \cdot 5 \cdots (2k-1)$ is the double factorial.

For Brownian motion ($\sigma^2 = t$):

$$
\mathbb{E}[B_t^{2k}] = t^k (2k-1)!!
$$

| $k$ | $\mathbb{E}[B_t^{2k}]$ |
| --- | ----------------------- |
| 1   | $t$                     |
| 2   | $3t^2$                  |
| 3   | $15t^3$                 |
| 4   | $105t^4$                |

## Moment Generating Function

$$
M_B(u, t) = \mathbb{E}[e^{uB_t}] = e^{u^2 t/2}
$$

This follows directly from the Gaussian integral:

$$
\mathbb{E}[e^{uB_t}] = \int_{-\infty}^\infty e^{ux} \frac{1}{\sqrt{2\pi t}} e^{-x^2/(2t)}\,dx = e^{u^2 t/2}
$$

An equivalent and widely used form is the **exponential martingale identity**:

$$
\mathbb{E}\!\left[e^{uW_t - \frac{1}{2}u^2 t}\right] = 1
$$

This identity connects moment computations to the martingale techniques used in mathematical finance.

## Interpretation

Brownian motion has zero mean at all times, so there is no systematic drift. The variance grows linearly in time, reflecting the diffusive spreading of paths. Because $B_t$ is Gaussian, its distribution is completely determined by the first two moments — all higher moments follow from the variance alone.

---

## 2. Brownian Motion with Drift

## SDE and Solution

$$
dX_t = \mu\,dt + \sigma\,dW_t, \quad X_0 \in \mathbb{R}
$$

Integrating directly:

$$
X_t = X_0 + \mu t + \sigma W_t
$$

## First Two Moments

Since $W_t \sim \mathcal{N}(0, t)$:

$$
\mathbb{E}[X_t] = X_0 + \mu t, \quad \operatorname{Var}(X_t) = \sigma^2 t
$$

**Distribution:** $X_t \sim \mathcal{N}(X_0 + \mu t,\; \sigma^2 t)$

## Higher Moments and MGF

The central moments follow the Gaussian formula:

$$
\mathbb{E}[(X_t - \mathbb{E}[X_t])^n] = \begin{cases} 0 & \text{if } n \text{ odd} \\ \sigma^n t^{n/2} (n-1)!! & \text{if } n \text{ even} \end{cases}
$$

The moment generating function is

$$
\mathbb{E}[e^{uX_t}] = \exp\!\left[u(X_0 + \mu t) + \frac{u^2 \sigma^2 t}{2}\right]
$$

## Conditional Moments

For $s < t$, the increment

$$
X_t - X_s = \mu(t - s) + \sigma(W_t - W_s)
$$

is independent of $\mathcal{F}_s$ because Brownian motion has independent increments. Therefore:

$$
\mathbb{E}[X_t \mid X_s] = X_s + \mu(t - s), \quad \operatorname{Var}(X_t \mid X_s) = \sigma^2(t - s)
$$

## Interpretation

The drift $\mu$ shifts the mean linearly in time, while the variance grows at rate $\sigma^2$ regardless of $\mu$. The process has no memory of its past beyond the current value, a direct consequence of independent increments.

---

## 3. Geometric Brownian Motion

## SDE and Solution

$$
dS_t = \mu S_t\,dt + \sigma S_t\,dW_t, \quad S_0 > 0
$$

Applying Itô's lemma to $\log S_t$:

$$
S_t = S_0 \exp\!\left[\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma W_t\right]
$$

Since $\log S_t \sim \mathcal{N}\!\left(\log S_0 + (\mu - \sigma^2/2)t,\; \sigma^2 t\right)$, the process $S_t$ follows a **log-normal distribution**.

## First Two Moments

For a log-normal variable, if $Z \sim \mathcal{N}(m, v^2)$ then $\mathbb{E}[e^Z] = e^{m + v^2/2}$.

**Expectation:**

$$
\mathbb{E}[S_t] = S_0\,e^{(\mu - \sigma^2/2)t}\,\mathbb{E}[e^{\sigma W_t}] = S_0\,e^{(\mu - \sigma^2/2)t}\,e^{\sigma^2 t/2} = S_0\,e^{\mu t}
$$

The Itô correction $-\sigma^2/2$ in the exponent is exactly cancelled by the factor $\mathbb{E}[e^{\sigma W_t}] = e^{\sigma^2 t/2}$.

**Second moment:**

$$
\mathbb{E}[S_t^2] = S_0^2\,\mathbb{E}[e^{2(\mu - \sigma^2/2)t + 2\sigma W_t}] = S_0^2\,e^{2\mu t + \sigma^2 t}
$$

**Variance:**

$$
\operatorname{Var}(S_t) = \mathbb{E}[S_t^2] - (\mathbb{E}[S_t])^2 = S_0^2\,e^{2\mu t}(e^{\sigma^2 t} - 1)
$$

## General Power Moments

For any real $n$, the same log-normal technique gives

$$
\mathbb{E}[S_t^n] = S_0^n \exp\!\left[n\mu t + \frac{n(n-1)}{2}\sigma^2 t\right]
$$

This is the $n$-th **power moment**, not the moment generating function. The ordinary MGF $\mathbb{E}[e^{uS_t}]$ of a log-normal random variable does not admit a closed-form expression for $u > 0$.

**Verification:** Setting $n = 1$ gives $S_0 e^{\mu t}$ and $n = 2$ gives $S_0^2 e^{2\mu t + \sigma^2 t}$, consistent with the first two moments above.

## Conditional Moments

For $s < t$, using $S_t = S_s \exp[(\mu - \sigma^2/2)(t-s) + \sigma(W_t - W_s)]$ and the independence of the increment $W_t - W_s$ from $\mathcal{F}_s$:

$$
\mathbb{E}[S_t \mid S_s] = S_s\,e^{\mu(t-s)}, \quad \operatorname{Var}(S_t \mid S_s) = S_s^2\,e^{2\mu(t-s)}(e^{\sigma^2(t-s)} - 1)
$$

## Skewness and Kurtosis

The log-normal distribution is **right-skewed** and **heavy-tailed**:

$$
\operatorname{Skew}(S_t) = (e^{\sigma^2 t} + 2)\sqrt{e^{\sigma^2 t} - 1}
$$

$$
\operatorname{Kurt}_{\text{excess}}(S_t) = e^{4\sigma^2 t} + 2e^{3\sigma^2 t} + 3e^{2\sigma^2 t} - 6
$$

Both increase **exponentially** with $\sigma^2 t$: as time grows or volatility rises, the variance explosion drives increasingly heavy tails and extreme right skewness. This is a direct consequence of the multiplicative noise structure.

## Interpretation

GBM has the property that the expected value grows exponentially at rate $\mu$, independent of $\sigma$. However, the variance also grows exponentially, and the distribution becomes increasingly right-skewed over time. This means that while the average outcome grows, the median outcome $S_0 e^{(\mu - \sigma^2/2)t}$ grows more slowly — a direct consequence of the Itô correction. The gap between mean and median reflects the fact that mean growth is driven by rare large outcomes in the right tail of the log-normal distribution.

---

## 4. Vasicek Model (Ornstein–Uhlenbeck)

## SDE and Solution

$$
dr_t = a(b - r_t)\,dt + \sigma\,dW_t, \quad r_0 \in \mathbb{R}
$$

where $a > 0$ is the mean reversion speed, $b$ is the long-term mean, and $\sigma > 0$ is the volatility.

Using the integrating factor $e^{at}$:

$$
r_t = r_0\,e^{-at} + b(1 - e^{-at}) + \sigma\int_0^t e^{-a(t-s)}\,dW_s
$$

## Expectation

The stochastic integral has zero expectation, giving

$$
\mathbb{E}[r_t] = r_0\,e^{-at} + b(1 - e^{-at})
$$

As $t \to \infty$, $\mathbb{E}[r_t] \to b$: the process mean-reverts to the long-term level.

## Variance via Itô Isometry

The variance comes entirely from the stochastic integral term $I_t = \sigma\int_0^t e^{-a(t-s)}\,dW_s$.

By **Itô isometry**, $\mathbb{E}\!\left[\left(\int_0^t f(s)\,dW_s\right)^2\right] = \int_0^t f(s)^2\,ds$:

$$
\operatorname{Var}(r_t) = \sigma^2 e^{-2at} \int_0^t e^{2as}\,ds = \sigma^2 e^{-2at} \cdot \frac{e^{2at} - 1}{2a} = \frac{\sigma^2}{2a}(1 - e^{-2at})
$$

As $t \to \infty$, $\operatorname{Var}(r_t) \to \frac{\sigma^2}{2a}$.

**Stationary distribution:** $r_\infty \sim \mathcal{N}\!\left(b,\; \frac{\sigma^2}{2a}\right)$

## Conditional Moments

For $s < t$, restarting the process at time $s$:

$$
\mathbb{E}[r_t \mid r_s] = r_s\,e^{-a(t-s)} + b(1 - e^{-a(t-s)})
$$

$$
\operatorname{Var}(r_t \mid r_s) = \frac{\sigma^2}{2a}(1 - e^{-2a(t-s)})
$$

## Covariance and Correlation

For $s < t$:

$$
\operatorname{Cov}(r_s, r_t) = \operatorname{Var}(r_s) \cdot e^{-a(t-s)} = \frac{\sigma^2}{2a}(1 - e^{-2as}) \cdot e^{-a(t-s)}
$$

This follows from the tower property: $\operatorname{Cov}(r_s, r_t) = \operatorname{Cov}(r_s, \mathbb{E}[r_t \mid r_s]) = e^{-a(t-s)} \operatorname{Var}(r_s)$, since $\mathbb{E}[r_t \mid r_s]$ is an affine function of $r_s$.

The correlation is

$$
\rho(s, t) = \frac{\operatorname{Cov}(r_s, r_t)}{\sqrt{\operatorname{Var}(r_s)\,\operatorname{Var}(r_t)}}
$$

Because the variance of $r_t$ depends on time during the transient phase, the correlation generally depends on both $s$ and $t$ individually. When the process has reached its **stationary regime** so that $\operatorname{Var}(r_t) = \sigma^2/(2a)$ for all relevant times, the correlation simplifies to

$$
\rho(s, t) = e^{-a|t-s|}
$$

This exponentially decaying autocorrelation — depending only on the time difference $|t - s|$ — is a hallmark of second-order stationarity and is characteristic of Ornstein–Uhlenbeck processes.

!!! tip "Centered Ornstein–Uhlenbeck Process"
    Setting $b = 0$ gives the centered OU process $dX_t = -aX_t\,dt + \sigma\,dW_t$ with $\mathbb{E}[X_t] = x_0\,e^{-at}$ and $\operatorname{Var}(X_t) = \frac{\sigma^2}{2a}(1 - e^{-2at})$. All formulas above apply with $b = 0$.

## Interpretation

Mean reversion creates a fundamental tension between the deterministic pull toward $b$ and the random shocks that push the process away. The stationary variance $\sigma^2/(2a)$ reflects this balance: stronger mean reversion (larger $a$) reduces the equilibrium spread, while higher volatility increases it. The exponential memory decay means that the process effectively forgets its past on a timescale of $1/a$.

!!! note "Structural Insight: Mean Reversion vs Diffusion"
    Brownian motion and geometric Brownian motion have variances that grow without bound over time. The OU/Vasicek process behaves differently: mean reversion counteracts the accumulation of random shocks, so the variance converges to a finite limit $\sigma^2/(2a)$, producing a stationary distribution. This balance between deterministic pull ($a$) and stochastic forcing ($\sigma$) is a central theme in many stochastic models, including the CIR and Heston models used in finance.

---

## 5. CIR Model

## SDE

$$
dr_t = a(b - r_t)\,dt + \sigma\sqrt{r_t}\,dW_t, \quad r_0 > 0
$$

where $a, b, \sigma > 0$. The **Feller condition** $2ab \geq \sigma^2$ ensures that the boundary at zero is unattainable, so $r_t > 0$ for all $t > 0$. Without this condition, the process may reach zero but remains nonnegative.

The CIR model shares the mean-reverting drift of the Vasicek model, but its diffusion coefficient $\sigma\sqrt{r_t}$ depends on the state. This state dependence prevents the process from becoming negative and makes the moment analysis more involved.

## Expectation via Moment ODE

To derive $\mathbb{E}[r_t]$, we take expectations of both sides of the integral form of the SDE:

$$
\mathbb{E}[r_t] = r_0 + \int_0^t a(b - \mathbb{E}[r_s])\,ds
$$

The stochastic integral $\int_0^t \sigma\sqrt{r_s}\,dW_s$ is a martingale with zero expectation, provided the integrand is square-integrable. For the CIR process, $\mathbb{E}\!\left[\int_0^t r_s\,ds\right] < \infty$, so this condition is satisfied.

Differentiating with respect to $t$ gives the ODE

$$
\frac{d}{dt}\mathbb{E}[r_t] = a(b - \mathbb{E}[r_t])
$$

This is a linear first-order ODE with solution

$$
\mathbb{E}[r_t] = r_0\,e^{-at} + b(1 - e^{-at})
$$

The expectation is identical to the Vasicek model: the state-dependent volatility does not affect the mean because the diffusion term contributes zero expected drift.

## Variance via Second Moment ODE

To find the variance, we first derive an ODE for $\mathbb{E}[r_t^2]$.

Apply Itô's lemma to $f(r) = r^2$ with $f'(r) = 2r$ and $f''(r) = 2$:

$$
d(r_t^2) = [2ab\,r_t - 2a\,r_t^2 + \sigma^2 r_t]\,dt + 2\sigma r_t^{3/2}\,dW_t
$$

Taking expectations (the stochastic integral term vanishes):

$$
\frac{d}{dt}\mathbb{E}[r_t^2] = (2ab + \sigma^2)\,\mathbb{E}[r_t] - 2a\,\mathbb{E}[r_t^2]
$$

This is a linear first-order ODE for $m_2(t) = \mathbb{E}[r_t^2]$ with known forcing from $m(t) = \mathbb{E}[r_t]$. Using the integrating factor $e^{2at}$:

$$
\frac{d}{dt}[e^{2at} m_2(t)] = (2ab + \sigma^2)\,e^{2at}\,m(t)
$$

Substituting $m(s) = r_0\,e^{-as} + b(1 - e^{-as})$ and integrating:

$$
e^{2at} m_2(t) - r_0^2 = (2ab + \sigma^2)\!\left[r_0 \cdot \frac{e^{at} - 1}{a} + b\!\left(\frac{e^{2at} - 1}{2a} - \frac{e^{at} - 1}{a}\right)\right]
$$

Computing $\operatorname{Var}(r_t) = m_2(t) - m(t)^2$ and simplifying:

$$
\operatorname{Var}(r_t) = \frac{\sigma^2}{a}\!\left[r_0\,e^{-at}(1 - e^{-at}) + \frac{b}{2}(1 - e^{-at})^2\right]
$$

The first term captures the contribution of the initial condition (which decays over time), while the second term captures the contribution of the equilibrium level $b$.

## Long-Term Behavior

$$
\lim_{t \to \infty} \operatorname{Var}(r_t) = \frac{b\sigma^2}{2a}
$$

Compare with the Vasicek long-term variance $\sigma^2/(2a)$: the CIR variance has an extra factor of $b$ because the diffusion magnitude $\sigma\sqrt{r_t}$ grows with the level of the process, so higher equilibrium levels produce larger fluctuations.

The **stationary distribution** of the CIR process is a **Gamma distribution** with mean $b$ and variance $b\sigma^2/(2a)$. The **transition distribution** (the conditional distribution of $r_t$ given $r_0$ at finite times) follows a scaled noncentral chi-square distribution.

## Conditional Moments

For $s < t$:

$$
\mathbb{E}[r_t \mid r_s] = r_s\,e^{-a(t-s)} + b(1 - e^{-a(t-s)})
$$

$$
\operatorname{Var}(r_t \mid r_s) = r_s \frac{\sigma^2}{a}(e^{-a(t-s)} - e^{-2a(t-s)}) + \frac{b\sigma^2}{2a}(1 - e^{-a(t-s)})^2
$$

The conditional variance depends on the current level $r_s$, which is a direct consequence of state-dependent volatility. Higher rates produce larger fluctuations.

## Interpretation

The CIR model demonstrates why state-dependent volatility matters. The expectation follows the same formula as Vasicek, but the variance has a fundamentally different structure: it depends on the initial condition $r_0$ in a way that reflects the $\sqrt{r_t}$ diffusion. Near zero, the volatility vanishes, which (together with the Feller condition) prevents the process from becoming negative. This makes CIR suitable for modeling interest rates and other inherently non-negative quantities.

---

## 6. General Techniques for Moment Computation

Four main techniques are used to compute moments of SDE solutions.

## Method 1 — Direct Computation from Explicit Solutions

When an explicit solution exists, moments can be computed directly using known distributions. This approach gives the most transparent formulas but only works for a limited class of models.

**Examples in this chapter:**

- Brownian motion and BM with drift: Gaussian moments
- GBM: log-normal power moments
- Vasicek: Gaussian stochastic integral representation

## Method 2 — Itô's Lemma Applied to Powers

To find $\mathbb{E}[X_t^n]$, apply Itô's lemma to $f(x) = x^n$:

$$
d(X_t^n) = nX_t^{n-1}\,dX_t + \frac{n(n-1)}{2}X_t^{n-2}(dX_t)^2
$$

Taking expectations eliminates the stochastic integral and yields an ODE for the $n$-th moment. This technique works even when explicit solutions are unavailable.

**Example in this chapter:** In the CIR model, applying Itô's lemma to $r_t^2$ produced the second-moment ODE used to derive the variance.

## Method 3 — Moment ODEs from the Infinitesimal Generator

For an SDE $dX_t = b(X_t)\,dt + \sigma(X_t)\,dW_t$, the infinitesimal generator is

$$
\mathcal{L} = b(x)\frac{\partial}{\partial x} + \frac{\sigma^2(x)}{2}\frac{\partial^2}{\partial x^2}
$$

The evolution of expectations is governed by

$$
\frac{d}{dt}\mathbb{E}[f(X_t)] = \mathbb{E}[\mathcal{L}f(X_t)]
$$

Setting $f(x) = x^n$ produces moment ODEs. For processes with polynomial drift and diffusion coefficients (such as OU and CIR), this generates a **closed hierarchy** where each moment ODE depends only on lower moments.

## Method 4 — Characteristic Functions

The characteristic function $\phi(u, t) = \mathbb{E}[e^{iuX_t}]$ encodes all moments via

$$
\mathbb{E}[X_t^n] = \frac{1}{i^n}\frac{\partial^n \phi}{\partial u^n}\bigg|_{u=0}
$$

Vasicek and CIR are **affine diffusions**, meaning their characteristic functions have exponential-affine form and satisfy systems of Riccati ODEs. This structure extends to the Heston stochastic volatility model and affine term-structure models, making the characteristic function approach the most powerful method when direct moment computation becomes intractable.

---

## 7. Comparison Table

| Model | $\mathbb{E}[X_t]$ | $\operatorname{Var}(X_t)$ | Distribution | Volatility |
| ----- | ------------------ | ------------------------- | ------------ | ---------- |
| **BM** | $0$ | $t$ | Gaussian | constant |
| **BM with drift** | $X_0 + \mu t$ | $\sigma^2 t$ | Gaussian | constant |
| **GBM** | $S_0 e^{\mu t}$ | $S_0^2 e^{2\mu t}(e^{\sigma^2 t} - 1)$ | log-normal | multiplicative |
| **Vasicek** | $r_0 e^{-at} + b(1-e^{-at})$ | $\frac{\sigma^2}{2a}(1-e^{-2at})$ | Gaussian | constant |
| **CIR** | $r_0 e^{-at} + b(1-e^{-at})$ | $\frac{\sigma^2}{a}[r_0 e^{-at}(1-e^{-at}) + \frac{b}{2}(1-e^{-at})^2]$ | noncentral $\chi^2$ / Gamma | state-dependent |

Key observations:

- The **mean** of CIR and Vasicek is identical — state-dependent volatility does not affect the expected value
- **Variance grows linearly** for BM models but **converges to a finite limit** for mean-reverting models
- **GBM variance grows exponentially**, reflecting the compounding effect of multiplicative noise

---

## 8. Computational Strategy

When computing moments for a new SDE:

1. **Check for an explicit solution.** If one exists, use the distribution directly.
2. **Apply Itô's lemma to powers** of the process. This produces moment ODEs.
3. **Solve the ODE hierarchy.** For many models, the first and second moment ODEs are linear and solvable in closed form.
4. **Verify via simulation** for models where analytical results are complex. For processes with state-dependent diffusion (such as CIR), standard Euler schemes can introduce discretization bias, particularly near boundaries — exact simulation or higher-order methods may be needed for reliable verification.

!!! summary "Key Takeaway"
    Moment analysis extracts quantitative information from SDEs without solving for the full distribution. Gaussian processes (Brownian motion, Vasicek) have moments determined entirely by the mean and variance. Log-normal processes (GBM) require power-moment techniques. State-dependent volatility (CIR) couples the moment hierarchy, requiring ODE methods. In all cases, Itô isometry and Itô's lemma are the essential computational tools.
