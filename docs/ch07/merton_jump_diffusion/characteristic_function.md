# Characteristic Function

Fourier methods are among the most efficient tools for pricing options under models more complex than Black-Scholes. The starting point is the **characteristic function** of the log-price, which encodes the entire probability distribution in a single complex-valued function. For the Merton jump-diffusion model, the characteristic function has a closed-form expression that combines the Gaussian characteristic function of the diffusion with the Levy-Khintchine formula for the jump component.

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:

    1. Define the characteristic function and explain its role in Fourier-based option pricing
    2. Derive the characteristic function of the Merton jump-diffusion log-return
    3. Identify the Levy-Khintchine structure and interpret each component
    4. Extract cumulants from the characteristic function and connect them to moments

---

## Motivation

### Why Characteristic Functions

The probability density of the Merton log-return is a Gaussian mixture (sum over Poisson-weighted normals). While the density itself is an infinite series, the characteristic function takes a compact closed form. This matters for two practical reasons:

1. **Fourier pricing**: The Carr-Madan formula and the COS method express option prices as integrals involving the characteristic function, which can be evaluated by FFT in $O(N \log N)$ operations.
2. **Model comparison**: Different jump-diffusion and stochastic volatility models are most easily compared through their characteristic functions, since the pricing machinery is the same regardless of the model.

### Review of Characteristic Functions

For a real-valued random variable $X$, the characteristic function is:

$$
\phi_X(u) = \mathbb{E}[e^{iuX}], \quad u \in \mathbb{R}
$$

Key properties:

- $\phi_X(0) = 1$ and $|\phi_X(u)| \leq 1$ for all $u$
- $\phi_X$ uniquely determines the distribution of $X$
- If $X$ and $Y$ are independent, then $\phi_{X+Y}(u) = \phi_X(u) \cdot \phi_Y(u)$
- The $n$-th moment (if it exists) satisfies $\mathbb{E}[X^n] = \frac{1}{i^n}\phi_X^{(n)}(0)$

---

## Characteristic Function of the Merton Log-Return

### Setup

From the Ito formula for jump processes, the log-return over $[0, T]$ is:

$$
x_T \equiv \ln\frac{S_T}{S_0} = \underbrace{\left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2\right)T}_{\text{drift}} + \underbrace{\sigma W_T}_{\text{diffusion}} + \underbrace{\sum_{i=1}^{N_T}\ln Y_i}_{\text{jumps}}
$$

The three components are mutually independent (Brownian motion, Poisson process, and jump sizes are independent by assumption).

### Derivation

!!! info "Theorem: Characteristic Function of the Merton Log-Return"
    The characteristic function of the log-return $x_T$ under $\mathbb{Q}$ is

    $$
    \phi_{x_T}(u) = \exp\!\left[iu\mu'T - \frac{1}{2}\sigma^2 u^2 T + \lambda T\!\left(e^{iu\mu_J - \frac{1}{2}\sigma_J^2 u^2} - 1\right)\right]
    $$

    where $\mu' = r - \lambda\bar{k} - \frac{1}{2}\sigma^2$ is the adjusted drift.

**Proof.** By independence of the three components:

$$
\phi_{x_T}(u) = \mathbb{E}[e^{iux_T}] = e^{iu\mu'T} \cdot \mathbb{E}[e^{iu\sigma W_T}] \cdot \mathbb{E}\!\left[e^{iu\sum_{i=1}^{N_T}\ln Y_i}\right]
$$

**Factor 1 (drift):** The deterministic drift contributes $e^{iu\mu'T}$.

**Factor 2 (diffusion):** Since $\sigma W_T \sim N(0, \sigma^2 T)$, the characteristic function of a normal is:

$$
\mathbb{E}[e^{iu\sigma W_T}] = e^{-\frac{1}{2}\sigma^2 u^2 T}
$$

**Factor 3 (jumps):** This is the characteristic function of a compound Poisson process with jump sizes $\ln Y_i \sim N(\mu_J, \sigma_J^2)$. Using the compound Poisson MGF result (replacing the real argument by $iu$):

$$
\mathbb{E}\!\left[e^{iu\sum_{i=1}^{N_T}\ln Y_i}\right] = \exp\!\left[\lambda T\bigl(\phi_{\ln Y}(u) - 1\bigr)\right]
$$

where $\phi_{\ln Y}(u) = \mathbb{E}[e^{iu\ln Y}] = e^{iu\mu_J - \frac{1}{2}\sigma_J^2 u^2}$ is the characteristic function of a $N(\mu_J, \sigma_J^2)$ random variable.

Multiplying the three factors:

$$
\phi_{x_T}(u) = \exp\!\left[iu\mu'T - \frac{1}{2}\sigma^2 u^2 T + \lambda T\!\left(e^{iu\mu_J - \frac{1}{2}\sigma_J^2 u^2} - 1\right)\right]
$$

$\square$

---

## The Levy-Khintchine Representation

### General Framework

The Levy-Khintchine theorem states that the characteristic function of any Levy process $L_t$ (a process with stationary, independent increments and cadlag paths) has the form:

$$
\phi_{L_t}(u) = \exp\!\left[t\left(iu\gamma - \frac{1}{2}\sigma^2 u^2 + \int_{\mathbb{R}\setminus\{0\}}\bigl(e^{iuy} - 1 - iuy\mathbf{1}_{|y|<1}\bigr)\nu(dy)\right)\right]
$$

where:

- $\gamma \in \mathbb{R}$ is the drift
- $\sigma^2 \geq 0$ is the Gaussian variance
- $\nu$ is the **Levy measure**, satisfying $\int \min(1, y^2)\,\nu(dy) < \infty$

The triple $(\gamma, \sigma^2, \nu)$ is called the **Levy-Khintchine triplet** and uniquely characterizes the process.

### Merton Model as a Levy Process

The Merton log-return $x_T$ is a Levy process with triplet:

| Component | Value |
|-----------|-------|
| Drift $\gamma$ | $r - \lambda\bar{k} - \frac{1}{2}\sigma^2 + \lambda\int_{|y|<1} y\,\nu(dy)$ |
| Gaussian variance $\sigma^2$ | Diffusion variance |
| Levy measure $\nu(dy)$ | $\lambda \cdot \frac{1}{\sigma_J\sqrt{2\pi}} e^{-(y-\mu_J)^2/(2\sigma_J^2)}\,dy$ |

The Levy measure $\nu$ is **finite**: $\nu(\mathbb{R}) = \lambda < \infty$. This means the Merton model is a **finite-activity** jump process --- there are finitely many jumps in any bounded time interval (almost surely). This is in contrast to infinite-activity models such as Variance Gamma or CGMY, where the Levy measure has infinite total mass and infinitely many small jumps accumulate in finite time.

!!! tip "Finite Activity Simplifies the Levy-Khintchine Formula"
    When $\nu(\mathbb{R}) < \infty$, the truncation indicator $\mathbf{1}_{|y|<1}$ in the Levy-Khintchine formula can be dropped (both integrals converge), and the drift term simplifies. The characteristic exponent becomes:

    $$
    \psi(u) = iu\mu' - \frac{1}{2}\sigma^2 u^2 + \lambda\bigl(\phi_{\ln Y}(u) - 1\bigr)
    $$

    so that $\phi_{x_T}(u) = e^{T\psi(u)}$.

---

## Cumulants

### Definition

The cumulant generating function (for the characteristic function) is:

$$
\Psi(u) = \ln \phi_{x_T}(u) = iu\mu'T - \frac{1}{2}\sigma^2 u^2 T + \lambda T\!\left(e^{iu\mu_J - \frac{1}{2}\sigma_J^2 u^2} - 1\right)
$$

The $n$-th cumulant $\kappa_n$ is extracted by Taylor-expanding $\Psi(u)$ around $u = 0$:

$$
\Psi(u) = \sum_{n=1}^{\infty} \kappa_n \frac{(iu)^n}{n!}
$$

### Explicit Cumulants

Expanding the exponential $e^{iu\mu_J - \frac{1}{2}\sigma_J^2 u^2}$ and collecting powers of $iu$:

**First cumulant (mean):**

$$
\kappa_1 = \left(r - \lambda\bar{k} - \frac{1}{2}\sigma^2 + \lambda\mu_J\right)T
$$

**Second cumulant (variance):**

$$
\kappa_2 = \left(\sigma^2 + \lambda(\mu_J^2 + \sigma_J^2)\right)T
$$

**Third cumulant:**

$$
\kappa_3 = \lambda(\mu_J^3 + 3\mu_J\sigma_J^2)T
$$

**Fourth cumulant:**

$$
\kappa_4 = \lambda(\mu_J^4 + 6\mu_J^2\sigma_J^2 + 3\sigma_J^4)T
$$

The general pattern is that the $n$-th cumulant of the jump component equals $\lambda T$ times the $n$-th moment of $\ln Y \sim N(\mu_J, \sigma_J^2)$, while the diffusion contributes only to $\kappa_1$ and $\kappa_2$.

### Cumulants and Distribution Shape

The standardized cumulants give the skewness and excess kurtosis:

$$
\text{Skewness} = \frac{\kappa_3}{\kappa_2^{3/2}}, \qquad \text{Excess kurtosis} = \frac{\kappa_4}{\kappa_2^2}
$$

Both quantities are determined entirely by the jump parameters $(\lambda, \mu_J, \sigma_J)$ and the diffusion volatility $\sigma$. As $T \to 0$, the skewness diverges as $T^{-1/2}$ and the kurtosis diverges as $T^{-1}$, reflecting the dominance of jumps at short time scales.

---

## Connection to Fourier Pricing

### The Carr-Madan Formula

The price of a European call with strike $K$ and maturity $T$ can be expressed as:

$$
C(K) = \frac{e^{-rT-\alpha k}}{\pi}\int_0^{\infty} e^{-ivk}\frac{\phi_{x_T}(v - (\alpha+1)i)}{(\alpha + iv)(\alpha + 1 + iv)}\,dv
$$

where $k = \ln K$, $\alpha > 0$ is a damping parameter, and $\phi_{x_T}$ is the characteristic function derived above. This integral is evaluated numerically using the FFT, producing option prices across a grid of strikes in $O(N\log N)$ operations.

### Why the Closed-Form Characteristic Function Matters

Without a closed-form characteristic function, Fourier pricing requires numerical evaluation of $\phi$ at each quadrature point, which itself might involve Monte Carlo or PDE solvers. The Merton model's analytical $\phi$ makes FFT pricing extremely fast --- typically under one millisecond for a full strike grid.

---

## Worked Example

!!! example "Computing the Characteristic Function"
    Consider the parameters $r = 0.05$, $\sigma = 0.20$, $\lambda = 0.5$, $\mu_J = -0.10$, $\sigma_J = 0.30$, $T = 1$.

    **Step 1: Adjusted drift.**

    $$
    \bar{k} = e^{-0.10 + 0.045} - 1 \approx -0.0535
    $$

    $$
    \mu' = 0.05 - 0.5(-0.0535) - \frac{1}{2}(0.04) = 0.05 + 0.0268 - 0.02 = 0.0568
    $$

    **Step 2: Evaluate $\phi_{x_1}(u)$ at $u = 1$.**

    $$
    \phi_{x_1}(1) = \exp\!\left[i(0.0568) - \frac{1}{2}(0.04) + 0.5\!\left(e^{-0.10i - 0.045} - 1\right)\right]
    $$

    Computing the jump factor:

    $$
    e^{-0.10i - 0.045} = e^{-0.045}(\cos 0.10 - i\sin 0.10) \approx 0.956(0.995 - 0.0998i) \approx 0.951 - 0.0954i
    $$

    $$
    0.5(0.951 - 0.0954i - 1) = 0.5(-0.049 - 0.0954i) = -0.0245 - 0.0477i
    $$

    $$
    \phi_{x_1}(1) = \exp\!\left[(0.0568i - 0.02 - 0.0245 - 0.0477i)\right] = \exp\!\left[-0.0445 + 0.0091i\right]
    $$

    $$
    |\phi_{x_1}(1)| = e^{-0.0445} \approx 0.9565
    $$

    **Step 3: Cumulants.**

    $$
    \kappa_1 = (0.0568 + 0.5 \times (-0.10)) \times 1 = 0.0068
    $$

    $$
    \kappa_2 = (0.04 + 0.5(0.01 + 0.09)) \times 1 = 0.04 + 0.05 = 0.09
    $$

    $$
    \kappa_3 = 0.5(-0.001 + 3(-0.10)(0.09)) \times 1 = 0.5(-0.001 - 0.027) = -0.014
    $$

    $$
    \text{Skewness} = \frac{-0.014}{0.09^{3/2}} = \frac{-0.014}{0.027} \approx -0.519
    $$

    The negative skewness confirms the leftward asymmetry from downward jumps.

---

## Summary

The characteristic function of the Merton log-return has the closed-form expression $\phi_{x_T}(u) = \exp[iu\mu'T - \frac{1}{2}\sigma^2 u^2 T + \lambda T(e^{iu\mu_J - \frac{1}{2}\sigma_J^2 u^2} - 1)]$, combining a Gaussian factor from the diffusion with an exponential factor from the compound Poisson jumps. This structure is a special case of the Levy-Khintchine formula for finite-activity Levy processes. The cumulants extracted from the characteristic function reveal that jumps contribute all cumulants of order three and above, generating the negative skewness and excess kurtosis that distinguish the Merton model from Black-Scholes. The closed-form characteristic function enables efficient Fourier-based option pricing via the Carr-Madan formula and FFT methods.
