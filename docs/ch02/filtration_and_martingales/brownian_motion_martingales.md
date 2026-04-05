# Brownian Motion Martingales

## Introduction

Brownian motion occupies a unique position in probability theory: it is simultaneously the simplest continuous-time stochastic process and the most fundamental. Its martingale properties are not merely technical facts but reveal deep structural truths about the nature of randomness.

In this section, we systematically develop the martingale structure of Brownian motion, proceeding from the basic martingale property through polynomial martingales to the exponential martingale. A remarkable fact emerges: these seemingly disparate martingales are all manifestations of a single underlying structure.

---

## Brownian Motion as a Martingale

Let $W = \{W_t\}_{t \ge 0}$ be a standard Brownian motion on a filtered probability space $(\Omega, \mathcal{F}, (\mathcal{F}_t), \mathbb{P})$, where $(\mathcal{F}_t)$ is the natural filtration augmented to satisfy the usual conditions.

**Theorem**: $W_t$ is a martingale with respect to $(\mathcal{F}_t)$.

**Proof**: We verify the three requirements:

1. **Adaptedness**: By construction, $W_t$ is $\mathcal{F}_t$-measurable.

2. **Integrability**: Since $W_t \sim N(0, t)$, we have $\mathbb{E}|W_t| = \sqrt{2t/\pi} < \infty$.

3. **Martingale property**: For $0 \le s < t$, decompose $W_t = W_s + (W_t - W_s)$. Then:

$$
\mathbb{E}[W_t \mid \mathcal{F}_s] = \mathbb{E}[W_s \mid \mathcal{F}_s] + \mathbb{E}[W_t - W_s \mid \mathcal{F}_s]
$$

Since $W_s$ is $\mathcal{F}_s$-measurable, $\mathbb{E}[W_s \mid \mathcal{F}_s] = W_s$. Since $W_t - W_s$ is independent of $\mathcal{F}_s$ (by the independent increments property) and $\mathbb{E}[W_t - W_s] = 0$:

$$
\mathbb{E}[W_t - W_s \mid \mathcal{F}_s] = \mathbb{E}[W_t - W_s] = 0
$$

Therefore, $\mathbb{E}[W_t \mid \mathcal{F}_s] = W_s$. $\square$

$$
\boxed{W_t \text{ is a martingale}}
$$

**Remark**: The martingale property encodes that Brownian motion has "no drift." The best prediction of where the particle will be in the future is its current position. This is the mathematical formalization of "pure noise."

---

## Polynomial Martingales: First Examples

Simple transformations of Brownian motion, when properly compensated, yield new martingales. These compensated processes reveal the moment structure of Brownian motion.

### The Quadratic Martingale: W_t² - t

**Theorem**: The process $M_t = W_t^2 - t$ is a martingale.

**Proof**: For $0 \le s < t$, we compute $\mathbb{E}[W_t^2 \mid \mathcal{F}_s]$. Writing $W_t = W_s + (W_t - W_s)$:

$$
W_t^2 = W_s^2 + 2W_s(W_t - W_s) + (W_t - W_s)^2
$$

Taking conditional expectations (using that $W_s$ is $\mathcal{F}_s$-measurable, so $2W_s$ factors out by the "taking out what is known" property):

$$
\mathbb{E}[W_t^2 \mid \mathcal{F}_s] = W_s^2 + 2W_s \cdot \mathbb{E}[W_t - W_s] + \mathbb{E}[(W_t - W_s)^2]
$$

Using $\mathbb{E}[W_t - W_s] = 0$ and $\mathbb{E}[(W_t - W_s)^2] = \text{Var}(W_t - W_s) = t - s$:

$$
\mathbb{E}[W_t^2 \mid \mathcal{F}_s] = W_s^2 + (t - s)
$$

Therefore:

$$
\mathbb{E}[W_t^2 - t \mid \mathcal{F}_s] = W_s^2 + (t-s) - t = W_s^2 - s
$$

$$
\boxed{W_t^2 - t \text{ is a martingale}}
$$

**Interpretation**: While $\mathbb{E}[W_t^2] = t$ grows linearly, the martingale $W_t^2 - t$ oscillates around zero with no expected drift. The compensation term $t$ exactly cancels the deterministic growth in the second moment.

**Connection to quadratic variation**: This martingale foreshadows the quadratic variation $[W]_t = t$. The process $W_t^2 - [W]_t$ being a martingale is a general fact for continuous local martingales.

### The Cubic Martingale: W_t³ - 3tW_t

**Theorem**: The process $M_t = W_t^3 - 3tW_t$ is a martingale.

**Proof**: We need the third moment of a Gaussian: if $Z \sim N(0, \sigma^2)$, then $\mathbb{E}[Z^3] = 0$ by symmetry.

Expanding $(W_s + (W_t - W_s))^3$ and using the binomial theorem:

$$
W_t^3 = W_s^3 + 3W_s^2(W_t - W_s) + 3W_s(W_t - W_s)^2 + (W_t - W_s)^3
$$

Taking conditional expectations:

$$
\mathbb{E}[W_t^3 \mid \mathcal{F}_s] = W_s^3 + 3W_s^2 \cdot 0 + 3W_s \cdot (t-s) + 0 = W_s^3 + 3W_s(t-s)
$$

Also, $\mathbb{E}[tW_t \mid \mathcal{F}_s] = t \cdot \mathbb{E}[W_t \mid \mathcal{F}_s] = t \cdot W_s$ (using the martingale property of $W_t$). Therefore:

$$
\mathbb{E}[W_t^3 - 3tW_t \mid \mathcal{F}_s] = W_s^3 + 3W_s(t-s) - 3tW_s = W_s^3 - 3sW_s
$$

$$
\boxed{W_t^3 - 3tW_t \text{ is a martingale}}
$$

---

## The Pattern: Hermite Polynomials

The polynomial martingales are not arbitrary—they follow a beautiful pattern connected to **Hermite polynomials**.

Define the probabilist's Hermite polynomials $H_n(x)$ by the generating function:

$$
\exp\left(tx - \frac{t^2}{2}\right) = \sum_{n=0}^\infty \frac{t^n}{n!} H_n(x)
$$

The first few are:

$$
H_0(x) = 1, \quad H_1(x) = x, \quad H_2(x) = x^2 - 1, \quad H_3(x) = x^3 - 3x
$$

**Theorem**: For each $n \ge 0$, the process

$$
M_t^{(n)} = t^{n/2} H_n\left(\frac{W_t}{\sqrt{t}}\right)
$$

is a martingale. Equivalently, if we write $H_n(W_t, t)$ for the process obtained by replacing $x^k$ with $W_t^k$ and multiplying by appropriate powers of $t$:

$$
H_n(W_t, t) = \sum_{k=0}^{\lfloor n/2 \rfloor} \frac{(-1)^k n!}{k!(n-2k)!} W_t^{n-2k} t^k
$$

is a martingale.

**Examples**:

- $n = 1$: $H_1(W_t, t) = W_t$
- $n = 2$: $H_2(W_t, t) = W_t^2 - t$  
- $n = 3$: $H_3(W_t, t) = W_t^3 - 3tW_t$
- $n = 4$: $H_4(W_t, t) = W_t^4 - 6tW_t^2 + 3t^2$

This pattern continues indefinitely, with each polynomial martingale encoding higher-order moment information.

---

## The Exponential Martingale

The most important Brownian martingale is the **exponential martingale**:

$$
\boxed{Z_t^\theta = \exp\left(\theta W_t - \frac{\theta^2 t}{2}\right)}
$$

**Theorem**: For any $\theta \in \mathbb{R}$, the process $Z_t^\theta$ is a strictly positive martingale with $\mathbb{E}[Z_t^\theta] = 1$.

**Proof**: For $0 \le s < t$, write:

$$
Z_t^\theta = \exp\left(\theta W_s - \frac{\theta^2 s}{2}\right) \cdot \exp\left(\theta(W_t - W_s) - \frac{\theta^2(t-s)}{2}\right) = Z_s^\theta \cdot Y
$$

where $Y = \exp\left(\theta(W_t - W_s) - \frac{\theta^2(t-s)}{2}\right)$.

Since $W_t - W_s \sim N(0, t-s)$ is independent of $\mathcal{F}_s$:

$$
\mathbb{E}[Y] = \mathbb{E}\left[\exp(\theta \cdot N(0, t-s))\right] \cdot \exp\left(-\frac{\theta^2(t-s)}{2}\right)
$$

Using the moment generating function $\mathbb{E}[e^{\theta Z}] = e^{\theta^2 \sigma^2/2}$ for $Z \sim N(0, \sigma^2)$:

$$
\mathbb{E}[Y] = \exp\left(\frac{\theta^2(t-s)}{2}\right) \cdot \exp\left(-\frac{\theta^2(t-s)}{2}\right) = 1
$$

Therefore:

$$
\mathbb{E}[Z_t^\theta \mid \mathcal{F}_s] = Z_s^\theta \cdot \mathbb{E}[Y] = Z_s^\theta
$$

$$
\boxed{Z_t^\theta = \exp\left(\theta W_t - \frac{\theta^2 t}{2}\right) \text{ is a martingale}}
$$

**Remark on the compensator**: The term $-\frac{\theta^2 t}{2}$ is exactly what is needed to cancel the exponential growth. This is an instance of a general principle: $\exp(M_t - \frac{1}{2}[M]_t)$ is a local martingale for any continuous local martingale $M_t$.

---

## The Generating Function Principle

The exponential martingale is not just another example—it **generates all polynomial martingales**.

**Theorem**: Expanding $Z_t^\theta$ as a power series in $\theta$:

$$
\exp\left(\theta W_t - \frac{\theta^2 t}{2}\right) = \sum_{n=0}^\infty \frac{\theta^n}{n!} H_n(W_t, t)
$$

each coefficient $H_n(W_t, t)$ is a martingale.

**Proof**: Since $Z_t^\theta$ is a martingale for each $\theta$, the martingale property gives $\mathbb{E}[Z_t^\theta \mid \mathcal{F}_s] = Z_s^\theta$.

To interchange the sum and conditional expectation, note that for $|\theta| \le R$:
$$
\sum_{n=0}^\infty \frac{|\theta|^n}{n!} |H_n(W_t, t)| \le \exp\left(R|W_t| + \frac{R^2 t}{2}\right) \in L^1
$$
(a standard Gaussian moment estimate). By dominated convergence for conditional expectations:

$$
\mathbb{E}\left[\sum_{n=0}^\infty \frac{\theta^n}{n!} H_n(W_t, t) \,\Big|\, \mathcal{F}_s\right] = \sum_{n=0}^\infty \frac{\theta^n}{n!} \mathbb{E}[H_n(W_t, t) \mid \mathcal{F}_s]
$$

Since this equals $Z_s^\theta = \sum_{n=0}^\infty \frac{\theta^n}{n!} H_n(W_s, s)$ for all $\theta \in \mathbb{R}$, comparing coefficients of $\theta^n$ yields:

$$
\mathbb{E}[H_n(W_t, t) \mid \mathcal{F}_s] = H_n(W_s, s) \quad \text{for each } n \quad \square
$$

**Consequences**:

| Power of $\theta$ | Coefficient | Martingale |
|-------------------|-------------|------------|
| $\theta^0$ | $1$ | Trivially a martingale |
| $\theta^1$ | $W_t$ | Brownian motion |
| $\theta^2$ | $\frac{1}{2}(W_t^2 - t)$ | Compensated square |
| $\theta^3$ | $\frac{1}{6}(W_t^3 - 3tW_t)$ | Compensated cube |

This unification is elegant: the exponential martingale encodes **all** moment information about Brownian motion in a single object.

---

## Applications of the Exponential Martingale

### 1. Girsanov's Theorem

The exponential martingale is the **Radon–Nikodym derivative** for changing probability measures. Under the measure $\mathbb{Q}$ defined by

$$
\frac{d\mathbb{Q}}{d\mathbb{P}}\Big|_{\mathcal{F}_t} = Z_t^\theta
$$

the process $\widetilde{W}_t = W_t - \theta t$ is a $\mathbb{Q}$-Brownian motion. This is the heart of Girsanov's theorem.

**Financial interpretation**: Girsanov allows us to transform a real-world measure (with drift) to a risk-neutral measure (without drift), enabling derivative pricing.

### 2. Moment Generating Functions

For any stopping time $\tau$, the optional sampling theorem (when applicable) gives:

$$
\mathbb{E}\left[\exp\left(\theta W_\tau - \frac{\theta^2 \tau}{2}\right)\right] = 1
$$

This yields the joint Laplace transform of $(W_\tau, \tau)$ and is the key to computing hitting time distributions.

### 3. Large Deviations

The exponential martingale structure underlies **Cramér's theorem** and large deviation estimates for Brownian motion:

$$
\mathbb{P}(W_t \ge a) \le \exp\left(-\frac{a^2}{2t}\right) \quad \text{for } a > 0
$$

This follows by applying Markov's inequality to the exponential martingale.

---

## The Stochastic Exponential

The exponential martingale is a special case of the **stochastic exponential** (or Doléans-Dade exponential), whose full treatment requires Itô calculus (see *Itô's Formula* and *Stochastic Integration*). We state the result here for completeness.

For any continuous local martingale $M_t$ with $M_0 = 0$, define:

$$
\mathcal{E}(M)_t := \exp\left(M_t - \frac{1}{2}[M]_t\right)
$$

where $[M]_t$ is the quadratic variation.

**Theorem**: $\mathcal{E}(M)_t$ is a local martingale. It is the unique solution to:

$$
dZ_t = Z_t \, dM_t, \quad Z_0 = 1
$$

For Brownian motion, $[W]_t = t$, recovering our exponential martingale:

$$
\mathcal{E}(\theta W)_t = \exp\left(\theta W_t - \frac{\theta^2 t}{2}\right)
$$

---

## Summary Table

| Martingale | Expression | Key Property |
|------------|------------|--------------|
| Brownian motion | $W_t$ | Fundamental; "pure noise" |
| Compensated square | $W_t^2 - t$ | Encodes variance growth |
| Compensated cube | $W_t^3 - 3tW_t$ | Encodes third moment |
| Hermite polynomial | $H_n(W_t, t)$ | General $n$-th moment |
| Exponential | $\exp(\theta W_t - \frac{\theta^2 t}{2})$ | Generates all polynomial martingales |

---

## Looking Ahead

The martingale structure of Brownian motion is the foundation for:

- **Stopping times and optional sampling**: Evaluating martingales at random times
- **Girsanov's theorem**: Changing probability measures via exponential martingales
- **Itô calculus**: The exponential martingale satisfies $dZ_t = \theta Z_t \, dW_t$
- **Risk-neutral pricing**: Discounted prices are martingales under the risk-neutral measure

In the next sections, we develop the theory of stopping times and the Optional Sampling Theorem, which allow us to exploit these martingale identities at random times—crucial for boundary value problems and option pricing.

---

## Exercises

### Exercise 1: Exponential Martingale Verification

(a) Prove directly that $Z_t^\theta = \exp(\theta W_t - \frac{\theta^2 t}{2})$ is a martingale for any $\theta \in \mathbb{R}$.

(b) Compute $\mathbb{E}[Z_t^\theta]$ and $\text{Var}(Z_t^\theta)$.

(c) Show that $Z_t^\theta \to 0$ almost surely as $t \to \infty$ for $\theta \neq 0$.

??? success "Solution to Exercise 1"
    **(a)** For $0 \le s < t$, factor $Z_t^\theta = Z_s^\theta \cdot Y$ where $Y = \exp(\theta(W_t - W_s) - \frac{\theta^2}{2}(t - s))$.

    Since $W_t - W_s \sim N(0, t-s)$ is independent of $\mathcal{F}_s$ and $Z_s^\theta$ is $\mathcal{F}_s$-measurable:

    $$
    \mathbb{E}[Z_t^\theta \mid \mathcal{F}_s] = Z_s^\theta \cdot \mathbb{E}[Y]
    $$

    Computing $\mathbb{E}[Y]$: for $Z \sim N(0, t-s)$, $\mathbb{E}[e^{\theta Z}] = e^{\theta^2(t-s)/2}$. Therefore:

    $$
    \mathbb{E}[Y] = e^{\theta^2(t-s)/2} \cdot e^{-\theta^2(t-s)/2} = 1
    $$

    So $\mathbb{E}[Z_t^\theta \mid \mathcal{F}_s] = Z_s^\theta$, confirming $Z_t^\theta$ is a martingale. $\square$

    **(b)** $\mathbb{E}[Z_t^\theta] = \mathbb{E}[Z_0^\theta] = e^{\theta \cdot 0 - 0} = 1$ (by the martingale property, or direct computation).

    For the variance: $\text{Var}(Z_t^\theta) = \mathbb{E}[(Z_t^\theta)^2] - (\mathbb{E}[Z_t^\theta])^2 = \mathbb{E}[e^{2\theta W_t - \theta^2 t}] - 1$.

    $$
    \mathbb{E}[e^{2\theta W_t - \theta^2 t}] = e^{-\theta^2 t} \cdot \mathbb{E}[e^{2\theta W_t}] = e^{-\theta^2 t} \cdot e^{(2\theta)^2 t/2} = e^{-\theta^2 t + 2\theta^2 t} = e^{\theta^2 t}
    $$

    Therefore $\text{Var}(Z_t^\theta) = e^{\theta^2 t} - 1$.

    **(c)** $\log Z_t^\theta = \theta W_t - \frac{\theta^2}{2}t$. By the law of the iterated logarithm, $|W_t| \le C\sqrt{t \log\log t}$ eventually a.s. for some constant, so $W_t/t \to 0$ a.s. Therefore:

    $$
    \frac{\log Z_t^\theta}{t} = \theta \frac{W_t}{t} - \frac{\theta^2}{2} \to -\frac{\theta^2}{2} < 0 \quad \text{a.s.}
    $$

    Since $\log Z_t^\theta \to -\infty$ a.s., $Z_t^\theta \to 0$ a.s. $\square$

---

### Exercise 2: Generating Polynomial Martingales

(a) Expand $\exp(\theta W_t - \frac{\theta^2 t}{2})$ as a power series in $\theta$ up to order 4.

(b) Identify the coefficient of $\theta^4$ and verify it is a martingale.

(c) State the general pattern: what is the martingale corresponding to $\theta^n$?

??? success "Solution to Exercise 2"
    **(a)** Write $\exp(\theta W_t - \frac{\theta^2 t}{2})$ using the Taylor expansion of the exponential. Let $x = \theta W_t$ and $y = \frac{\theta^2 t}{2}$:

    $$
    e^{x - y} = e^x \cdot e^{-y} = \left(\sum_{k=0}^\infty \frac{(\theta W_t)^k}{k!}\right)\left(\sum_{j=0}^\infty \frac{(-\theta^2 t/2)^j}{j!}\right)
    $$

    Collecting terms by powers of $\theta$:

    - $\theta^0$: $1$
    - $\theta^1$: $W_t$
    - $\theta^2$: $\frac{W_t^2}{2} - \frac{t}{2} = \frac{1}{2}(W_t^2 - t)$
    - $\theta^3$: $\frac{W_t^3}{6} - \frac{tW_t}{2} = \frac{1}{6}(W_t^3 - 3tW_t)$
    - $\theta^4$: $\frac{W_t^4}{24} - \frac{tW_t^2}{4} + \frac{t^2}{8} = \frac{1}{24}(W_t^4 - 6tW_t^2 + 3t^2)$

    **(b)** The coefficient of $\theta^4$ is $\frac{1}{24}(W_t^4 - 6tW_t^2 + 3t^2) = \frac{1}{4!}H_4(W_t, t)$.

    To verify it is a martingale, expand $W_t = W_s + \Delta$ where $\Delta = W_t - W_s \sim N(0, t-s)$:

    Using the moments $\mathbb{E}[\Delta^k]$: $\mathbb{E}[\Delta] = 0$, $\mathbb{E}[\Delta^2] = t-s$, $\mathbb{E}[\Delta^3] = 0$, $\mathbb{E}[\Delta^4] = 3(t-s)^2$, one computes $\mathbb{E}[W_t^4 - 6tW_t^2 + 3t^2 \mid \mathcal{F}_s]$ and verifies it equals $W_s^4 - 6sW_s^2 + 3s^2$.

    **(c)** The general pattern: the coefficient of $\theta^n/n!$ in $\exp(\theta W_t - \theta^2 t/2)$ is $H_n(W_t, t)$, the $n$-th Hermite polynomial martingale:

    $$
    H_n(W_t, t) = t^{n/2} H_n\left(\frac{W_t}{\sqrt{t}}\right) = \sum_{k=0}^{\lfloor n/2 \rfloor} \frac{(-1)^k n!}{k!(n-2k)!} W_t^{n-2k} t^k
    $$

---

### Exercise 3: Two-Sided Exponential

Consider $Z_t = \cosh(\theta W_t) \exp(-\frac{\theta^2 t}{2})$.

(a) Prove that $Z_t$ is a martingale.

(b) Express $Z_t$ in terms of exponential martingales with parameters $\pm\theta$.

(c) Find the analogous martingale involving $\sinh$.

??? success "Solution to Exercise 3"
    **(a)** $\cosh(\theta W_t) = \frac{e^{\theta W_t} + e^{-\theta W_t}}{2}$. Therefore:

    $$
    Z_t = \cosh(\theta W_t) e^{-\theta^2 t/2} = \frac{1}{2}\left(e^{\theta W_t - \theta^2 t/2} + e^{-\theta W_t - \theta^2 t/2}\right)
    $$

    Each term is an exponential martingale: $e^{\theta W_t - \theta^2 t/2} = Z_t^\theta$ and $e^{-\theta W_t - (-\theta)^2 t/2} = e^{-\theta W_t - \theta^2 t/2} = Z_t^{-\theta}$. Since $Z_t = \frac{1}{2}(Z_t^\theta + Z_t^{-\theta})$ is the average of two martingales, it is a martingale. $\square$

    **(b)** As shown above:

    $$
    Z_t = \frac{1}{2}\left(Z_t^\theta + Z_t^{-\theta}\right) = \frac{1}{2}\left(\exp\left(\theta W_t - \frac{\theta^2 t}{2}\right) + \exp\left(-\theta W_t - \frac{\theta^2 t}{2}\right)\right)
    $$

    **(c)** The $\sinh$ analogue: $\sinh(\theta W_t) e^{-\theta^2 t/2} = \frac{1}{2}(Z_t^\theta - Z_t^{-\theta})$.

    Since it is the difference of two martingales (scaled by $1/2$), it is also a martingale:

    $$
    \widetilde{Z}_t = \sinh(\theta W_t) \exp\left(-\frac{\theta^2 t}{2}\right)
    $$

---

### Exercise 4: Martingale Characterization of Brownian Motion

Prove **Lévy's characterization**: If $M_t$ is a continuous martingale with $M_0 = 0$ and $[M]_t = t$, then $M_t$ is a standard Brownian motion.

*Hint*: Show that $\exp(\theta M_t - \frac{\theta^2 t}{2})$ is a martingale for all $\theta$ and use uniqueness of moment generating functions.

??? success "Solution to Exercise 4"
    Assume $M_t$ is a continuous martingale with $M_0 = 0$ and $[M]_t = t$. We want to show $M_t$ is a standard Brownian motion.

    Consider $Z_t^\theta = \exp(\theta M_t - \frac{\theta^2}{2}[M]_t) = \exp(\theta M_t - \frac{\theta^2 t}{2})$.

    By the general theory of stochastic exponentials, $Z_t^\theta = \mathcal{E}(\theta M)_t$ is a local martingale. Since $[M]_t = t$ is deterministic and $M$ is continuous, $Z_t^\theta$ is in fact a true martingale (this can be verified using Novikov's condition: $\mathbb{E}[\exp(\frac{1}{2}\theta^2 [M]_T)] = \exp(\frac{\theta^2 T}{2}) < \infty$).

    Therefore $\mathbb{E}[\exp(i\alpha M_t)] = \exp(-\frac{\alpha^2 t}{2})$ for all $\alpha \in \mathbb{R}$ (by evaluating the martingale property at $\theta = i\alpha$ via analytic continuation, or by direct computation using the martingale property of $Z_t^\theta$).

    This is the characteristic function of $N(0, t)$, so $M_t \sim N(0, t)$.

    For the joint distribution: by the martingale property and the fact that $[M]$ is deterministic, the increments $M_t - M_s$ are independent of $\mathcal{F}_s$ with distribution $N(0, t-s)$. This follows because $\exp(i\alpha(M_t - M_s)) \cdot \exp(\frac{\alpha^2(t-s)}{2})$ is a martingale, so $\mathbb{E}[\exp(i\alpha(M_t - M_s)) \mid \mathcal{F}_s] = \exp(-\frac{\alpha^2(t-s)}{2})$, which is the characteristic function of $N(0, t-s)$, independent of $\mathcal{F}_s$.

    Therefore $M_t$ has stationary independent Gaussian increments, continuous paths, and $M_0 = 0$: it is a standard Brownian motion. $\square$

---

### Exercise 5: The Martingale Problem

(a) State the martingale problem for Brownian motion: for which functions $f$ is $f(W_t) - \frac{1}{2}\int_0^t f''(W_s) \, ds$ a local martingale?

(b) Verify this for $f(x) = x^2$ and $f(x) = e^{\theta x}$.

(c) Explain the connection to the heat equation $\partial_t u = \frac{1}{2} \partial_{xx} u$.

??? success "Solution to Exercise 5"
    **(a)** The **martingale problem for Brownian motion**: for any $f \in C^2(\mathbb{R})$, the process

    $$
    f(W_t) - \frac{1}{2}\int_0^t f''(W_s)\,ds
    $$

    is a local martingale. This follows from Ito's formula:

    $$
    f(W_t) = f(W_0) + \int_0^t f'(W_s)\,dW_s + \frac{1}{2}\int_0^t f''(W_s)\,ds
    $$

    The stochastic integral $\int_0^t f'(W_s)\,dW_s$ is a local martingale. Hence $f(W_t) - f(W_0) - \frac{1}{2}\int_0^t f''(W_s)\,ds = \int_0^t f'(W_s)\,dW_s$ is a local martingale.

    **(b)** For $f(x) = x^2$: $f'(x) = 2x$, $f''(x) = 2$.

    $$
    W_t^2 - \frac{1}{2}\int_0^t 2\,ds = W_t^2 - t
    $$

    This is the martingale $W_t^2 - t$, confirming the result.

    For $f(x) = e^{\theta x}$: $f'(x) = \theta e^{\theta x}$, $f''(x) = \theta^2 e^{\theta x}$.

    $$
    e^{\theta W_t} - \frac{\theta^2}{2}\int_0^t e^{\theta W_s}\,ds
    $$

    is a local martingale. This is consistent with the exponential martingale: $e^{\theta W_t - \theta^2 t/2}$ is a martingale, and the drift term $\frac{\theta^2}{2}e^{\theta W_s}$ is exactly what Ito's formula produces.

    **(c)** The connection to the heat equation: if $u(x, t)$ solves $\partial_t u = \frac{1}{2}\partial_{xx} u$, then $u(W_t, T - t)$ is a local martingale for $0 \le t \le T$.

    This follows from Ito's formula applied to $g(t) = u(W_t, T - t)$:

    $$
    dg = \partial_x u \cdot dW_t + \left(-\partial_t u + \frac{1}{2}\partial_{xx} u\right)dt = \partial_x u \cdot dW_t + 0 \cdot dt
    $$

    (using the PDE $\partial_t u = \frac{1}{2}\partial_{xx} u$). The drift vanishes, so $g(t)$ is a local martingale.

    This is the Feynman-Kac connection: solutions of the heat equation can be represented as conditional expectations of Brownian functionals, and conversely, martingales of the form $f(W_t)$ with compensated drift are characterized by the generator equation $\frac{1}{2}f'' = 0$ (harmonic functions) for the drift-free case.
