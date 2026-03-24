# Poisson Process and Jump Size Distribution

In the Merton jump-diffusion model, discontinuous price moves arrive at random times governed by a **Poisson process**, and the magnitude of each jump is drawn from a **log-normal distribution**. This section develops both components rigorously. Understanding the Poisson process and the compound Poisson process is essential because they determine the statistical properties of jump-diffusion returns, including the characteristic function, the moments, and the behavior of the implied volatility smile at short maturities.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. State the axiomatic definition of a Poisson process and derive its key properties
    2. Construct the compound Poisson process and compute its moment generating function
    3. Derive the moments of the log-normal jump size distribution used in Merton's model
    4. Calculate the total variance and higher moments contributed by the jump component

---

## The Poisson Process

### Intuition

Imagine monitoring a stock price for sudden jumps. These jumps occur at unpredictable times, but they have a well-defined average rate: perhaps one jump every two years, corresponding to intensity $\lambda = 0.5$. Between jumps, the price diffuses continuously. The Poisson process provides the mathematical framework for counting such randomly arriving events.

### Axiomatic Definition

!!! info "Definition: Poisson Process"
    A counting process $N = \{N_t\}_{t \geq 0}$ is a **Poisson process** with intensity $\lambda > 0$ if:

    1. $N_0 = 0$
    2. $N$ has **independent increments**: for $0 \leq t_1 < t_2 \leq t_3 < t_4$, the increments $N_{t_2} - N_{t_1}$ and $N_{t_4} - N_{t_3}$ are independent
    3. $N$ has **stationary increments**: $N_{t+s} - N_t \sim \text{Poisson}(\lambda s)$ for all $t, s \geq 0$
    4. $\mathbb{P}(N_{t+h} - N_t \geq 2) = o(h)$ as $h \to 0$ (no simultaneous jumps)

The distribution of the increment is:

$$
\mathbb{P}(N_{t+s} - N_t = n) = \frac{(\lambda s)^n}{n!} e^{-\lambda s}, \quad n = 0, 1, 2, \ldots
$$

### Key Properties

**Moments.** For the Poisson distribution with parameter $\lambda t$:

$$
\mathbb{E}[N_t] = \lambda t, \qquad \operatorname{Var}(N_t) = \lambda t
$$

The equality of mean and variance is a signature property of the Poisson distribution.

**Inter-arrival times.** Let $T_i$ denote the time of the $i$-th jump. The inter-arrival times $\tau_i = T_i - T_{i-1}$ (with $T_0 = 0$) are independent and exponentially distributed:

$$
\tau_i \sim \text{Exp}(\lambda), \qquad f_{\tau}(s) = \lambda e^{-\lambda s}, \quad s \geq 0
$$

!!! info "Proposition: Memoryless Property"
    The exponential distribution is the unique continuous distribution satisfying

    $$
    \mathbb{P}(\tau > t + s \mid \tau > t) = \mathbb{P}(\tau > s) = e^{-\lambda s}
    $$

    for all $t, s \geq 0$.

**Proof.** For $\tau \sim \text{Exp}(\lambda)$, we have $\mathbb{P}(\tau > u) = e^{-\lambda u}$. Therefore:

$$
\mathbb{P}(\tau > t + s \mid \tau > t) = \frac{\mathbb{P}(\tau > t + s)}{\mathbb{P}(\tau > t)} = \frac{e^{-\lambda(t+s)}}{e^{-\lambda t}} = e^{-\lambda s} = \mathbb{P}(\tau > s)
$$

$\square$

This memoryless property means that, given no jump has occurred so far, the distribution of the waiting time until the next jump is the same regardless of how long one has already waited. In financial terms, the jump hazard rate is constant.

### The Compensated Poisson Process

The compensated (or centered) Poisson process subtracts the deterministic trend:

$$
\tilde{N}_t = N_t - \lambda t
$$

This process is a $\mathbb{Q}$-martingale with $\mathbb{E}[\tilde{N}_t] = 0$, and it plays a central role in the stochastic calculus for jump processes. The compensator $\lambda t$ is the unique predictable, increasing process such that $N_t - \lambda t$ is a martingale.

---

## The Compound Poisson Process

### Definition and Construction

The Poisson process counts events; the compound Poisson process also assigns a random magnitude to each event.

!!! info "Definition: Compound Poisson Process"
    Let $N_t$ be a Poisson process with intensity $\lambda$, and let $\{Z_i\}_{i \geq 1}$ be i.i.d. random variables (independent of $N$) with common distribution $F_Z$. The **compound Poisson process** is

    $$
    J_t = \sum_{i=1}^{N_t} Z_i
    $$

    with the convention that the empty sum ($N_t = 0$) equals zero.

In the Merton model, $Z_i = Y_i - 1$ where $Y_i$ is the multiplicative jump factor, so $J_t = \sum_{i=1}^{N_t}(Y_i - 1)$.

### Moment Generating Function

The MGF of $J_t$ follows from conditioning on $N_t$:

!!! info "Proposition: MGF of the Compound Poisson Process"
    If $M_Z(u) = \mathbb{E}[e^{uZ_1}]$ exists, then

    $$
    M_{J_t}(u) = \mathbb{E}[e^{uJ_t}] = \exp\!\bigl(\lambda t\,(M_Z(u) - 1)\bigr)
    $$

**Proof.** Condition on the number of jumps:

$$
\mathbb{E}[e^{uJ_t}] = \sum_{n=0}^{\infty} \mathbb{E}\!\left[e^{u\sum_{i=1}^n Z_i}\right] \mathbb{P}(N_t = n)
$$

By independence of the $Z_i$:

$$
= \sum_{n=0}^{\infty} [M_Z(u)]^n \frac{(\lambda t)^n}{n!} e^{-\lambda t} = e^{-\lambda t} \sum_{n=0}^{\infty} \frac{[\lambda t \, M_Z(u)]^n}{n!} = e^{-\lambda t} \cdot e^{\lambda t \, M_Z(u)}
$$

$$
= \exp\!\bigl(\lambda t(M_Z(u) - 1)\bigr)
$$

$\square$

### Moments via Cumulants

The cumulant generating function of $J_t$ is:

$$
\ln M_{J_t}(u) = \lambda t\,(M_Z(u) - 1)
$$

Expanding $M_Z(u) = 1 + \mathbb{E}[Z]\,u + \frac{1}{2}\mathbb{E}[Z^2]\,u^2 + \cdots$ and collecting terms:

$$
\mathbb{E}[J_t] = \lambda t \, \mathbb{E}[Z_1]
$$

$$
\operatorname{Var}(J_t) = \lambda t \, \mathbb{E}[Z_1^2]
$$

The variance formula follows from the law of total variance:

$$
\operatorname{Var}(J_t) = \mathbb{E}[N_t]\operatorname{Var}(Z_1) + \operatorname{Var}(N_t)(\mathbb{E}[Z_1])^2 = \lambda t \, \sigma_Z^2 + \lambda t \, \mu_Z^2 = \lambda t \, \mathbb{E}[Z_1^2]
$$

where $\mu_Z = \mathbb{E}[Z_1]$ and $\sigma_Z^2 = \operatorname{Var}(Z_1)$.

---

## Log-Normal Jump Size Distribution

### Merton's Specification

Merton's original model specifies that the logarithm of the jump multiplier $Y_i$ is normally distributed:

$$
\ln Y_i \sim N(\mu_J, \sigma_J^2)
$$

This means $Y_i$ itself is log-normally distributed with density:

$$
f_{Y}(y) = \frac{1}{y\sigma_J\sqrt{2\pi}} \exp\!\left(-\frac{(\ln y - \mu_J)^2}{2\sigma_J^2}\right), \quad y > 0
$$

### Moments of the Jump Multiplier

The $k$-th moment of $Y_i$ follows directly from the log-normal MGF:

$$
\mathbb{E}[Y_i^k] = e^{k\mu_J + k^2\sigma_J^2/2}
$$

In particular:

| Quantity | Formula | Typical value |
|----------|---------|---------------|
| $\mathbb{E}[Y_i]$ | $e^{\mu_J + \sigma_J^2/2}$ | $\approx 0.95$ |
| $\mathbb{E}[Y_i^2]$ | $e^{2\mu_J + 2\sigma_J^2}$ | $\approx 0.99$ |
| $\operatorname{Var}(Y_i)$ | $e^{2\mu_J + \sigma_J^2}(e^{\sigma_J^2} - 1)$ | $\approx 0.08$ |

The "typical values" use $\mu_J = -0.10$ and $\sigma_J = 0.30$.

### The Compensator Revisited

The expected relative jump size is:

$$
\bar{k} = \mathbb{E}[Y_i - 1] = e^{\mu_J + \sigma_J^2/2} - 1
$$

When $\mu_J < 0$ and $\sigma_J$ is moderate, $\bar{k} < 0$, meaning jumps on average reduce the price. The compensator $\lambda\bar{k}$ is then negative, so the drift $r - \lambda\bar{k} > r$ compensates by increasing the continuous drift to maintain the martingale property.

---

## Moments of the Jump Component in Log-Returns

### Setup

In the log-price process, the jump contribution over $[0, t]$ is:

$$
\mathcal{J}_t = \sum_{i=1}^{N_t} \ln Y_i
$$

This is a compound Poisson process with jump sizes $Z_i = \ln Y_i \sim N(\mu_J, \sigma_J^2)$.

### First Four Moments

Applying the compound Poisson moment formulas with $Z_i \sim N(\mu_J, \sigma_J^2)$:

**Mean:**

$$
\mathbb{E}[\mathcal{J}_t] = \lambda t \, \mu_J
$$

**Variance:**

$$
\operatorname{Var}(\mathcal{J}_t) = \lambda t \,(\sigma_J^2 + \mu_J^2)
$$

**Third central moment:**

$$
\mathbb{E}[(\mathcal{J}_t - \mathbb{E}[\mathcal{J}_t])^3] = \lambda t \,(\mu_J^3 + 3\mu_J\sigma_J^2)
$$

**Fourth central moment (excess):**

$$
\mathbb{E}[(\mathcal{J}_t - \mathbb{E}[\mathcal{J}_t])^4] - 3[\operatorname{Var}(\mathcal{J}_t)]^2 = \lambda t \,(\mu_J^4 + 6\mu_J^2\sigma_J^2 + 3\sigma_J^4)
$$

These formulas follow from the general result that the $n$-th cumulant of a compound Poisson process is $\lambda t$ times the $n$-th moment of the jump size distribution.

### Contribution to Return Distribution Shape

The total log-return variance, skewness, and kurtosis combine the diffusion and jump components:

$$
\text{Total variance} = \sigma^2 t + \lambda t(\sigma_J^2 + \mu_J^2)
$$

$$
\text{Skewness} = \frac{\lambda t(\mu_J^3 + 3\mu_J\sigma_J^2)}{[\sigma^2 t + \lambda t(\sigma_J^2 + \mu_J^2)]^{3/2}}
$$

Note that as $t \to 0$, the skewness scales as $t^{-1/2}$ (assuming jumps dominate), which becomes arbitrarily large in magnitude. This explains why short-maturity implied volatility smiles are steeper than long-maturity smiles in the Merton model.

---

## Worked Example

!!! example "Computing Jump Moments"
    Suppose $\lambda = 0.5$, $\mu_J = -0.10$, $\sigma_J = 0.30$, and consider a one-year horizon $t = 1$.

    **Expected number of jumps:** $\lambda t = 0.5$

    **Mean of jump component in log-returns:**

    $$
    \mathbb{E}[\mathcal{J}_1] = 0.5 \times (-0.10) = -0.05
    $$

    **Variance of jump component:**

    $$
    \operatorname{Var}(\mathcal{J}_1) = 0.5 \times (0.09 + 0.01) = 0.05
    $$

    **Compensator:**

    $$
    \bar{k} = e^{-0.10 + 0.045} - 1 = e^{-0.055} - 1 \approx -0.0535
    $$

    **Probability of zero jumps in one year:**

    $$
    \mathbb{P}(N_1 = 0) = e^{-0.5} \approx 0.6065
    $$

    So roughly 60.7% of the time, no jumps occur, and the model reduces to pure diffusion. There is a 30.3% probability of exactly one jump and a 7.6% probability of two jumps. The probability of three or more jumps is about 1.4%.

    **Probability of a jump exceeding 20% downward:**

    For a single jump, $\ln Y < \ln 0.80 = -0.2231$:

    $$
    \mathbb{P}(\ln Y < -0.2231) = \Phi\!\left(\frac{-0.2231 - (-0.10)}{0.30}\right) = \Phi(-0.410) \approx 0.341
    $$

    Given that a jump occurs, there is about a 34.1% chance it exceeds 20% downward. The unconditional probability of at least one such jump in a year is approximately $1 - e^{-0.5 \times 0.341} \approx 0.157$.

---

## Summary

The Poisson process provides the counting mechanism for jump arrivals, with intensity $\lambda$ governing the expected frequency and exponentially distributed inter-arrival times encoding the memoryless property. The compound Poisson process pairs each jump with a random magnitude, and its MGF factorizes elegantly as $\exp(\lambda t(M_Z(u) - 1))$. In Merton's model, the log-normal jump specification $\ln Y_i \sim N(\mu_J, \sigma_J^2)$ generates negative skewness (when $\mu_J < 0$) and positive excess kurtosis in the return distribution, matching the stylized facts of equity markets that pure diffusion cannot reproduce.

---

## Exercises

**Exercise 1.** Prove that the inter-arrival times of a Poisson process with intensity $\lambda$ are exponentially distributed with parameter $\lambda$. Use the definition $\tau_1 = \inf\{t > 0 : N_t \geq 1\}$ and the fact that $\mathbb{P}(N_t = 0) = e^{-\lambda t}$ to derive $\mathbb{P}(\tau_1 > t) = e^{-\lambda t}$.

---

**Exercise 2.** Derive the moment generating function of the compound Poisson process $J_t = \sum_{i=1}^{N_t} Z_i$ by conditioning on $N_t$. Starting from $M_{J_t}(u) = \mathbb{E}[e^{uJ_t}] = \sum_{n=0}^{\infty} \mathbb{E}[e^{u\sum Z_i}] \mathbb{P}(N_t = n)$, show that $M_{J_t}(u) = \exp(\lambda t(M_Z(u) - 1))$.

---

**Exercise 3.** For the log-normal jump multiplier $Y$ with $\ln Y \sim N(\mu_J, \sigma_J^2)$, compute $\mathbb{E}[Y]$, $\mathbb{E}[Y^2]$, and $\text{Var}(Y)$ in terms of $\mu_J$ and $\sigma_J$. Verify your formulas numerically for $\mu_J = -0.10$ and $\sigma_J = 0.30$.

---

**Exercise 4.** Using the variance decomposition $\text{Var}(J_t) = \mathbb{E}[N_t]\text{Var}(Z_1) + \text{Var}(N_t)(\mathbb{E}[Z_1])^2$, derive the jump variance $\text{Var}(\mathcal{J}_t) = \lambda t(\sigma_J^2 + \mu_J^2)$ where $\mathcal{J}_t = \sum_{i=1}^{N_t} \ln Y_i$. Identify the two sources of randomness contributing to this variance.

---

**Exercise 5.** For $\lambda = 0.5$ and $T = 1$ year, compute the probabilities $\mathbb{P}(N_T = 0)$, $\mathbb{P}(N_T = 1)$, $\mathbb{P}(N_T = 2)$, and $\mathbb{P}(N_T \geq 3)$. What fraction of simulated paths will exhibit no jumps at all? How does this affect the computational efficiency of Monte Carlo simulation?

---

**Exercise 6.** The compensated Poisson process $\tilde{N}_t = N_t - \lambda t$ is a martingale. Verify that $\mathbb{E}[\tilde{N}_t] = 0$ and compute $\text{Var}(\tilde{N}_t)$. Explain the role of the compensated Poisson process in the stochastic calculus for jump processes, drawing an analogy with the role of Brownian motion in continuous stochastic calculus.
