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
\mathbb{E}[W_t \mid \mathcal{F}_s] = \mathbb{E}[W_s \mid \mathcal{F}_s] + \mathbb{E}[W_t - W_s \mid \mathcal{F}_s].
$$

Since $W_s$ is $\mathcal{F}_s$-measurable, $\mathbb{E}[W_s \mid \mathcal{F}_s] = W_s$. Since $W_t - W_s$ is independent of $\mathcal{F}_s$ (by the independent increments property) and $\mathbb{E}[W_t - W_s] = 0$:

$$
\mathbb{E}[W_t - W_s \mid \mathcal{F}_s] = \mathbb{E}[W_t - W_s] = 0.
$$

Therefore, $\mathbb{E}[W_t \mid \mathcal{F}_s] = W_s$. $\square$

$$
\boxed{W_t \text{ is a martingale}}
$$

**Remark**: The martingale property encodes that Brownian motion has "no drift." The best prediction of where the particle will be in the future is its current position. This is the mathematical formalization of "pure noise."

---

## Polynomial Martingales: First Examples

Simple transformations of Brownian motion, when properly compensated, yield new martingales. These compensated processes reveal the moment structure of Brownian motion.

### The Quadratic Martingale: $W_t^2 - t$

**Theorem**: The process $M_t = W_t^2 - t$ is a martingale.

**Proof**: For $0 \le s < t$, we compute $\mathbb{E}[W_t^2 \mid \mathcal{F}_s]$. Writing $W_t = W_s + (W_t - W_s)$:

$$
W_t^2 = W_s^2 + 2W_s(W_t - W_s) + (W_t - W_s)^2.
$$

Taking conditional expectations:

$$
\mathbb{E}[W_t^2 \mid \mathcal{F}_s] = W_s^2 + 2W_s \cdot \mathbb{E}[W_t - W_s] + \mathbb{E}[(W_t - W_s)^2].
$$

Using $\mathbb{E}[W_t - W_s] = 0$ and $\mathbb{E}[(W_t - W_s)^2] = \text{Var}(W_t - W_s) = t - s$:

$$
\mathbb{E}[W_t^2 \mid \mathcal{F}_s] = W_s^2 + (t - s).
$$

Therefore:

$$
\mathbb{E}[W_t^2 - t \mid \mathcal{F}_s] = W_s^2 + (t-s) - t = W_s^2 - s.
$$

$$
\boxed{W_t^2 - t \text{ is a martingale}}
$$

**Interpretation**: While $\mathbb{E}[W_t^2] = t$ grows linearly, the martingale $W_t^2 - t$ oscillates around zero with no expected drift. The compensation term $t$ exactly cancels the deterministic growth in the second moment.

**Connection to quadratic variation**: This martingale foreshadows the quadratic variation $[W]_t = t$. The process $W_t^2 - [W]_t$ being a martingale is a general fact for continuous local martingales.

### The Cubic Martingale: $W_t^3 - 3tW_t$

**Theorem**: The process $M_t = W_t^3 - 3tW_t$ is a martingale.

**Proof**: We need the third moment of a Gaussian: if $Z \sim N(0, \sigma^2)$, then $\mathbb{E}[Z^3] = 0$ by symmetry.

Expanding $(W_s + (W_t - W_s))^3$ and using the binomial theorem:

$$
W_t^3 = W_s^3 + 3W_s^2(W_t - W_s) + 3W_s(W_t - W_s)^2 + (W_t - W_s)^3.
$$

Taking conditional expectations:

$$
\mathbb{E}[W_t^3 \mid \mathcal{F}_s] = W_s^3 + 3W_s^2 \cdot 0 + 3W_s \cdot (t-s) + 0 = W_s^3 + 3W_s(t-s).
$$

Also, $\mathbb{E}[tW_t \mid \mathcal{F}_s] = t \cdot W_s$. Therefore:

$$
\mathbb{E}[W_t^3 - 3tW_t \mid \mathcal{F}_s] = W_s^3 + 3W_s(t-s) - 3tW_s = W_s^3 - 3sW_s.
$$

$$
\boxed{W_t^3 - 3tW_t \text{ is a martingale}}
$$

---

## The Pattern: Hermite Polynomials

The polynomial martingales are not arbitrary—they follow a beautiful pattern connected to **Hermite polynomials**.

Define the probabilist's Hermite polynomials $H_n(x)$ by the generating function:

$$
\exp\left(tx - \frac{t^2}{2}\right) = \sum_{n=0}^\infty \frac{t^n}{n!} H_n(x).
$$

The first few are:

$$
H_0(x) = 1, \quad H_1(x) = x, \quad H_2(x) = x^2 - 1, \quad H_3(x) = x^3 - 3x.
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
Z_t^\theta = \exp\left(\theta W_s - \frac{\theta^2 s}{2}\right) \cdot \exp\left(\theta(W_t - W_s) - \frac{\theta^2(t-s)}{2}\right) = Z_s^\theta \cdot Y,
$$

where $Y = \exp\left(\theta(W_t - W_s) - \frac{\theta^2(t-s)}{2}\right)$.

Since $W_t - W_s \sim N(0, t-s)$ is independent of $\mathcal{F}_s$:

$$
\mathbb{E}[Y] = \mathbb{E}\left[\exp(\theta \cdot N(0, t-s))\right] \cdot \exp\left(-\frac{\theta^2(t-s)}{2}\right).
$$

Using the moment generating function $\mathbb{E}[e^{\theta Z}] = e^{\theta^2 \sigma^2/2}$ for $Z \sim N(0, \sigma^2)$:

$$
\mathbb{E}[Y] = \exp\left(\frac{\theta^2(t-s)}{2}\right) \cdot \exp\left(-\frac{\theta^2(t-s)}{2}\right) = 1.
$$

Therefore:

$$
\mathbb{E}[Z_t^\theta \mid \mathcal{F}_s] = Z_s^\theta \cdot \mathbb{E}[Y] = Z_s^\theta.
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
\exp\left(\theta W_t - \frac{\theta^2 t}{2}\right) = \sum_{n=0}^\infty \frac{\theta^n}{n!} H_n(W_t, t),
$$

each coefficient $H_n(W_t, t)$ is a martingale.

**Proof**: Since $Z_t^\theta$ is a martingale for each $\theta$, and conditional expectation is linear:

$$
\mathbb{E}\left[\sum_{n=0}^\infty \frac{\theta^n}{n!} H_n(W_t, t) \,\Big|\, \mathcal{F}_s\right] = \sum_{n=0}^\infty \frac{\theta^n}{n!} \mathbb{E}[H_n(W_t, t) \mid \mathcal{F}_s].
$$

For this to equal $Z_s^\theta = \sum_{n=0}^\infty \frac{\theta^n}{n!} H_n(W_s, s)$ for all $\theta$, we need:

$$
\mathbb{E}[H_n(W_t, t) \mid \mathcal{F}_s] = H_n(W_s, s) \quad \text{for each } n. \quad \square
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
\frac{d\mathbb{Q}}{d\mathbb{P}}\Big|_{\mathcal{F}_t} = Z_t^\theta,
$$

the process $\widetilde{W}_t = W_t - \theta t$ is a $\mathbb{Q}$-Brownian motion. This is the heart of Girsanov's theorem.

**Financial interpretation**: Girsanov allows us to transform a real-world measure (with drift) to a risk-neutral measure (without drift), enabling derivative pricing.

### 2. Moment Generating Functions

For any stopping time $\tau$, the optional sampling theorem (when applicable) gives:

$$
\mathbb{E}\left[\exp\left(\theta W_\tau - \frac{\theta^2 \tau}{2}\right)\right] = 1.
$$

This yields the joint Laplace transform of $(W_\tau, \tau)$ and is the key to computing hitting time distributions.

### 3. Large Deviations

The exponential martingale structure underlies **Cramér's theorem** and large deviation estimates for Brownian motion:

$$
\mathbb{P}(W_t \ge a) \le \exp\left(-\frac{a^2}{2t}\right) \quad \text{for } a > 0.
$$

This follows by applying Markov's inequality to the exponential martingale.

---

## The Stochastic Exponential

The exponential martingale is a special case of the **stochastic exponential** (or Doléans-Dade exponential). For any continuous local martingale $M_t$ with $M_0 = 0$, define:

$$
\mathcal{E}(M)_t := \exp\left(M_t - \frac{1}{2}[M]_t\right),
$$

where $[M]_t$ is the quadratic variation.

**Theorem**: $\mathcal{E}(M)_t$ is a local martingale. It is the unique solution to:

$$
dZ_t = Z_t \, dM_t, \quad Z_0 = 1.
$$

For Brownian motion, $[W]_t = t$, recovering our exponential martingale:

$$
\mathcal{E}(\theta W)_t = \exp\left(\theta W_t - \frac{\theta^2 t}{2}\right).
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

### Exercise 2: Generating Polynomial Martingales

(a) Expand $\exp(\theta W_t - \frac{\theta^2 t}{2})$ as a power series in $\theta$ up to order 4.

(b) Identify the coefficient of $\theta^4$ and verify it is a martingale.

(c) State the general pattern: what is the martingale corresponding to $\theta^n$?

### Exercise 3: Two-Sided Exponential

Consider $Z_t = \cosh(\theta W_t) \exp(-\frac{\theta^2 t}{2})$.

(a) Prove that $Z_t$ is a martingale.

(b) Express $Z_t$ in terms of exponential martingales with parameters $\pm\theta$.

(c) Find the analogous martingale involving $\sinh$.

### Exercise 4: Martingale Characterization of Brownian Motion

Prove **Lévy's characterization**: If $M_t$ is a continuous martingale with $M_0 = 0$ and $[M]_t = t$, then $M_t$ is a standard Brownian motion.

*Hint*: Show that $\exp(\theta M_t - \frac{\theta^2 t}{2})$ is a martingale for all $\theta$ and use uniqueness of moment generating functions.

### Exercise 5: The Martingale Problem

(a) State the martingale problem for Brownian motion: for which functions $f$ is $f(W_t) - \frac{1}{2}\int_0^t f''(W_s) \, ds$ a local martingale?

(b) Verify this for $f(x) = x^2$ and $f(x) = e^{\theta x}$.

(c) Explain the connection to the heat equation $\partial_t u = \frac{1}{2} \partial_{xx} u$.
