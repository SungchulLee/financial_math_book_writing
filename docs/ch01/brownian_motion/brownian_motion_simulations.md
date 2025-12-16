# Brownian Motion Overview

## Introduction

Having established the discrete random walk and its scaling limit via Donsker's theorem, we now define **Brownian motion** axiomatically. Brownian motion (also called the **Wiener process**) is the canonical continuous-time random motion that serves as the foundation for:

- Stochastic calculus and stochastic differential equations
- Mathematical finance (Black-Scholes theory)
- Statistical physics (diffusion processes)
- Filtering theory and signal processing

Brownian motion is the **only** stochastic process that is simultaneously:
1. Continuous
2. Markov
3. Has stationary independent increments
4. Has Gaussian increments

This uniqueness makes it the fundamental building block for continuous-time stochastic modeling.

## Intuitive Construction: Paper and Pencil Brownian Motion

Before giving the formal definition, we develop intuition through discrete approximations.

### Construction via Standard Normal Coin Flips

Consider the following discrete-to-continuous procedure:

| Quantity | Notation |
|----------|----------|
| Number of ticks per year | $n$ |
| Standard normal coin flip at tick $k$ | $X_k$ |
| Number of ticks between $0$ and $t$ | $nt$ |
| Cumulative standard normal coin flips up to time $t$ | $\displaystyle\sum_{k=1}^{nt}X_k$ |
| **Normalized cumulative sum** | $\displaystyle B_t= \frac{1}{\sqrt{n}}\sum_{k=1}^{nt}X_k$ |

where $X_k \stackrel{\text{iid}}{\sim} \mathcal{N}(0,1)$.

**Key observation:** As $n \to \infty$, by the central limit theorem (more precisely, Donsker's theorem), $B_t$ converges to Brownian motion.

### Construction via Fair Coin Flips

Equivalently, using $\{-1, +1\}$ random variables:

| Quantity | Notation |
|----------|----------|
| Number of ticks per year | $n$ |
| Fair coin flip at tick $k$ ($H = 1$, $T = -1$) | $X_k$ |
| Number of ticks between $0$ and $t$ | $nt$ |
| Cumulative fair coin flips up to time $t$ | $\displaystyle\sum_{k=1}^{nt}X_k$ |
| **Normalized cumulative sum** | $\displaystyle B_t= \frac{1}{\sqrt{n}}\sum_{k=1}^{nt}X_k$ |

where $\mathbb{P}(X_k = 1) = \mathbb{P}(X_k = -1) = 1/2$.

### Construction via Arbitrary i.i.d. Sequences

More generally, for any i.i.d. sequence $\{X_k\}$ with $\mathbb{E}[X_k] = \mu$ and $\text{Var}(X_k) = \sigma^2$:

| Quantity | Notation |
|----------|----------|
| Number of ticks per year | $n$ |
| Standardized i.i.d. coin flip at tick $k$ | $\displaystyle\frac{X_k-\mu}{\sigma}$ |
| Number of ticks between $0$ and $t$ | $nt$ |
| Cumulative standardized coin flips up to time $t$ | $\displaystyle \sum_{k=1}^{nt}\frac{X_k-\mu}{\sigma}$ |
| **Normalized cumulative sum** | $\displaystyle B_t= \frac{1}{\sqrt{n}}\sum_{k=1}^{nt}\frac{X_k-\mu}{\sigma}$ |

By Donsker's invariance principle, all three constructions yield the same limit: **Brownian motion**.

### Example: Concrete Path Construction

**Problem:** We flip a fair coin 10 times and get:

$$HHTHTTHHHT$$



Construct a Brownian motion sample path up to time $t = 1$.

**Solution:** With $n = 10$ ticks per year:

| Time | $0/10$ | $1/10$ | $2/10$ | $3/10$ | $4/10$ | $5/10$ | $6/10$ | $7/10$ | $8/10$ | $9/10$ | $10/10$ |
|------|--------|--------|--------|--------|--------|--------|--------|--------|--------|--------|---------|
| Coin flip | — | $H$ | $H$ | $T$ | $H$ | $T$ | $T$ | $H$ | $H$ | $H$ | $T$ |
| Conversion | — | $1$ | $1$ | $-1$ | $1$ | $-1$ | $-1$ | $1$ | $1$ | $1$ | $-1$ |
| Cum sum | $0$ | $1$ | $2$ | $1$ | $2$ | $1$ | $0$ | $1$ | $2$ | $3$ | $2$ |
| $B_t$ | $0$ | $\frac{1}{\sqrt{10}}$ | $\frac{2}{\sqrt{10}}$ | $\frac{1}{\sqrt{10}}$ | $\frac{2}{\sqrt{10}}$ | $\frac{1}{\sqrt{10}}$ | $0$ | $\frac{1}{\sqrt{10}}$ | $\frac{2}{\sqrt{10}}$ | $\frac{3}{\sqrt{10}}$ | $\frac{2}{\sqrt{10}}$ |

This piecewise linear path is an approximation to a true Brownian path. As $n \to \infty$, such approximations converge to continuous Brownian motion.

## Axiomatic Definition of Brownian Motion

Having built intuition, we now define Brownian motion rigorously.

### Definition 1.3.1 (Standard Brownian Motion / Wiener Process)

A **standard Brownian motion** $\{W_t\}_{t \ge 0}$ on a probability space $(\Omega,\mathcal{F},\mathbb{P})$ is a stochastic process satisfying:

**(i) Initial condition:**

$$W_0 = 0 \quad \text{almost surely}$$



**(ii) Independent increments:** For $0 \le t_0 < t_1 < \cdots < t_n$, the increments

$$W_{t_1}-W_{t_0},\quad W_{t_2}-W_{t_1},\quad \ldots,\quad W_{t_n}-W_{t_{n-1}}$$


are independent random variables.

**(iii) Stationary increments:** For $0 \le s < t$,

$$W_t - W_s \sim \mathcal{N}(0,t-s)$$



**(iv) Continuity of paths:** The map

$$t \mapsto W_t(\omega) \quad \text{is continuous for almost every } \omega \in \Omega$$



**Remark 1:** Conditions (i)-(iii) specify the finite-dimensional distributions (Gaussian with specific covariance). Condition (iv) selects the continuous version among all processes with these distributions.

**Remark 2:** Properties (ii) and (iii) together make Brownian motion a **Lévy process** (continuous-time analog of random walk with independent, stationary increments).

### Intuition Behind the Definition

**(1) Initial condition $W_0 = 0$:** At time 0, we haven't flipped any coins, so the cumulative sum is zero.

**(2) Independent increments:** For any time intervals $[t_{i-1}, t_i]$ and $[t_{j-1}, t_j]$ with $i \neq j$, the coin flips in one interval are completely independent of those in the other. Thus:

$$W_{t_i}-W_{t_{i-1}} \text{ are all independent}$$



**(3) Stationary Gaussian increments:** For standardized i.i.d. increments $\frac{X_k-\mu}{\sigma}$ with mean 0 and variance 1:

$$\begin{array}{lll}
&&\displaystyle \frac{X_k-\mu}{\sigma}\ \text{iid with mean 0, variance 1}\\
&\Rightarrow&\displaystyle
\sum_{k=ns+1}^{nt}\frac{X_k-\mu}{\sigma}\ \text{has mean 0, variance }n(t-s)\\
&\Rightarrow&\displaystyle
\frac{1}{\sqrt{n}}\sum_{k=ns+1}^{nt}\frac{X_k-\mu}{\sigma}\ \text{has mean 0, variance }t-s\\
&\Rightarrow&\displaystyle
W_t-W_s=\frac{1}{\sqrt{n}}\sum_{k=ns+1}^{nt}\frac{X_k-\mu}{\sigma}\quad\overset{d}{\to}\quad\mathcal{N}(0,t-s)\quad\text{by CLT as }n\to\infty
\end{array}$$



**(4) Continuity:** As $n \to \infty$, the piecewise linear interpolation converges uniformly to a continuous path (Donsker's theorem).

## Finite-Dimensional Distributions

### Joint Distribution

**Proposition 1.3.2**

For any $0 \le t_1 < t_2 < \cdots < t_n$, the random vector

$$(W_{t_1}, W_{t_2}, \ldots, W_{t_n})$$


is multivariate Gaussian with mean zero and covariance matrix $\Sigma$ where

$$\Sigma_{ij} = \mathbb{E}[W_{t_i} W_{t_j}] = \min(t_i,t_j)$$



**Proof:**

Write the vector in terms of independent increments:

$$\begin{pmatrix} W_{t_1} \\ W_{t_2} \\ \vdots \\ W_{t_n} \end{pmatrix}
= 
\begin{pmatrix} 
1 & 0 & 0 & \cdots & 0 \\
1 & 1 & 0 & \cdots & 0 \\
1 & 1 & 1 & \cdots & 0 \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & 1 & 1 & \cdots & 1
\end{pmatrix}
\begin{pmatrix} W_{t_1} - W_0 \\ W_{t_2} - W_{t_1} \\ \vdots \\ W_{t_n} - W_{t_{n-1}} \end{pmatrix}$$



Since the increments are independent Gaussians, their linear combination is Gaussian. The covariance is:

$$\mathbb{E}[W_{t_i} W_{t_j}] = \mathbb{E}\left[\left(\sum_{k=1}^i \Delta W_k\right)\left(\sum_{\ell=1}^j \Delta W_\ell\right)\right]
= \sum_{k=1}^{\min(i,j)} \mathbb{E}[(\Delta W_k)^2] = \sum_{k=1}^{\min(i,j)} \Delta t_k = t_{\min(i,j)} = \min(t_i, t_j) \quad \square$$



**Corollary 1.3.3**

In particular:

$$\mathbb{E}[W_t] = 0, \quad \mathbb{E}[W_t^2] = t, \quad \mathbb{E}[W_s W_t] = \min(s,t)$$



### Characteristic Function

**Proposition 1.3.4**

For $0 \le s < t$ and $\lambda \in \mathbb{R}$:

$$\boxed{
\mathbb{E}\left[e^{i\lambda(W_t-W_s)}\right]
=
\exp\left(-\frac{1}{2}\lambda^2(t-s)\right)
}$$



**Proof:**

Since $W_t - W_s \sim \mathcal{N}(0, t-s)$, its characteristic function is:

$$\mathbb{E}[e^{i\lambda X}] = \exp\left(i\lambda \mu - \frac{1}{2}\lambda^2\sigma^2\right)$$


with $\mu = 0$ and $\sigma^2 = t-s$. $\square$

This characteristic function uniquely characterizes the Gaussian increment structure.

## Covariance Structure

The covariance function contains rich information about Brownian motion's path properties.

**Theorem 1.3.5** (Covariance Formula)

For all $s,t \ge 0$:

$$\boxed{
\mathbb{E}[W_s W_t] = \min(s,t)
}$$



**Proof:**

Without loss of generality, assume $s \le t$. Then:

$$\mathbb{E}[W_s W_t] = \mathbb{E}[W_s (W_s + (W_t - W_s))]
= \mathbb{E}[W_s^2] + \mathbb{E}[W_s(W_t - W_s)]$$



By independent increments, $W_s$ and $W_t - W_s$ are independent, so:

$$\mathbb{E}[W_s(W_t - W_s)] = \mathbb{E}[W_s]\mathbb{E}[W_t - W_s] = 0 \cdot 0 = 0$$



Therefore:

$$\mathbb{E}[W_s W_t] = \mathbb{E}[W_s^2] = s = \min(s,t) \quad \square$$



**Implications of the covariance structure:**

1. **Non-differentiability**: If $W_t$ were differentiable, then $\text{Cov}(W_s, W_t) \sim st$, not $\min(s,t)$
2. **Long-range correlation**: $W_s$ and $W_t$ are correlated for all $s, t$ (not just nearby times)
3. **Self-similarity**: The $\min$ structure is scale-invariant (see Section 7)

## Construction via Kolmogorov Extension Theorem

We now sketch the rigorous construction of Brownian motion.

### Step 1: Specify Finite-Dimensional Distributions

For any finite collection of times $0 \le t_1 < \cdots < t_n$, define:

$$(W_{t_1}, \ldots, W_{t_n}) \sim \mathcal{N}(0, \Sigma), \quad \Sigma_{ij} = \min(t_i, t_j)$$



### Step 2: Verify Consistency

**Kolmogorov consistency conditions:** For any permutation and any subcollection of times, the marginal distributions must agree.

This follows from the properties of the Gaussian distribution and the $\min$ covariance structure.

### Step 3: Apply Kolmogorov Extension Theorem

**Theorem 1.3.6** (Kolmogorov Extension)

If the finite-dimensional distributions are consistent, there exists a stochastic process $\{W_t\}_{t \ge 0}$ with these distributions.

**Proof:** See any text on measure-theoretic probability (e.g., Billingsley, Kallenberg). $\square$

### Step 4: Ensure Continuity

The Kolmogorov extension theorem gives a process, but doesn't guarantee continuous paths. We need:

**Theorem 1.3.7** (Kolmogorov-Chentsov Continuity Theorem)

If there exist constants $\alpha, \beta, C > 0$ such that

$$\mathbb{E}[|W_t - W_s|^\alpha] \le C|t - s|^{1+\beta}$$


for all $s, t$, then $W$ has a continuous modification.

**Verification for Brownian motion:**

For $\alpha = 4$:

$$\mathbb{E}[|W_t - W_s|^4] = \mathbb{E}[(W_t - W_s)^4] = 3(t-s)^2$$


using the fourth moment of a Gaussian $\mathcal{N}(0, t-s)$.

Thus, we can take $\beta = 1$ and $C = 3$, satisfying the criterion with $\alpha = 4 > 1$. $\square$

**Conclusion:** There exists a continuous version of the Wiener process, which we call **Brownian motion**.

## Scaling Property (Self-Similarity)

**Theorem 1.3.8** (Scaling / Self-Similarity)

For any $c > 0$ and $t \ge 0$:

$$\boxed{
W_{ct} \overset{d}{=} \sqrt{c} \, W_t
}$$



where $\overset{d}{=}$ denotes equality in distribution.

**Proof:**

Both sides are Gaussian with mean zero. For the variance:
- Left side: $\mathbb{E}[W_{ct}^2] = ct$
- Right side: $\mathbb{E}[(\sqrt{c} W_t)^2] = c \mathbb{E}[W_t^2] = c \cdot t$

Since they have the same finite-dimensional distributions, they are equal in distribution. $\square$

**Interpretation:** Brownian motion has **no intrinsic time scale**. Zooming in by a factor $c$ in time is equivalent to zooming in by $\sqrt{c}$ in space.

**Hurst exponent:** The exponent $H = 1/2$ characterizes Brownian motion. Processes with $H \neq 1/2$ are called **fractional Brownian motions**.

## Nowhere Differentiability

One of the most striking properties of Brownian motion is its nowhere differentiability.

**Theorem 1.3.9** (Nowhere Differentiability)

With probability one,

$$\limsup_{h \to 0} \frac{|W_{t+h}-W_t|}{|h|} = \infty$$


for every $t \ge 0$.

**Proof sketch:**

Suppose $W_t$ were differentiable at some $t$. Then for small $h$:

$$W_{t+h} - W_t \approx W'(t) \cdot h$$



But:

$$\mathbb{E}[(W_{t+h} - W_t)^2] = h$$



So the "derivative" $W'(t)$ would satisfy:

$$\mathbb{E}[(W'(t))^2] \cdot h^2 \approx h \implies \mathbb{E}[(W'(t))^2] \approx 1/h \to \infty$$



This heuristic can be made rigorous using martingale techniques and the law of iterated logarithm. $\square$

**Rigorous statement (Paley-Wiener-Zygmund):**

Almost surely, for all $t \ge 0$:

$$\limsup_{h \to 0} \frac{|W_{t+h} - W_t|}{\sqrt{2h \log(1/h)}} = 1$$



**Implications:**

- Brownian paths are continuous but nowhere differentiable
- Total variation is infinite: $\int_0^T |dW_t| = \infty$ almost surely
- Classical calculus (e.g., chain rule) fails; we need **Itô calculus**

## Quadratic Variation

While first-order variation is infinite, second-order variation (quadratic variation) is finite.

**Theorem 1.3.10** (Quadratic Variation)

For any partition $\Pi_n = \{0 = t_0 < t_1 < \cdots < t_n = T\}$ with mesh $|\Pi_n| = \max_i(t_{i+1} - t_i) \to 0$:

$$\boxed{
\sum_{i=0}^{n-1} (W_{t_{i+1}}-W_{t_i})^2
\ \xrightarrow{\mathbb{P}}\ 
T
}$$



**Proof:**

Let $Q_n = \sum_{i=0}^{n-1} (W_{t_{i+1}} - W_{t_i})^2$. Compute the mean and variance:

*Mean:*

$$\mathbb{E}[Q_n] = \sum_{i=0}^{n-1} \mathbb{E}[(W_{t_{i+1}} - W_{t_i})^2] = \sum_{i=0}^{n-1} (t_{i+1} - t_i) = T$$



*Variance:*

$$\text{Var}(Q_n) = \sum_{i=0}^{n-1} \text{Var}[(W_{t_{i+1}} - W_{t_i})^2]$$



For a Gaussian $X \sim \mathcal{N}(0, \sigma^2)$:

$$\text{Var}(X^2) = \mathbb{E}[X^4] - (\mathbb{E}[X^2])^2 = 3\sigma^4 - \sigma^4 = 2\sigma^4$$



Thus:

$$\text{Var}(Q_n) = \sum_{i=0}^{n-1} 2(t_{i+1} - t_i)^2 \le 2|\Pi_n| \sum_{i=0}^{n-1}(t_{i+1} - t_i) = 2|\Pi_n| T \to 0$$



By Chebyshev's inequality, $Q_n \xrightarrow{\mathbb{P}} T$. $\square$

**Notation:** We write:

$$\langle W \rangle_T = T \quad \text{or} \quad d\langle W \rangle_t = dt$$



**This is the foundation for Itô's formula.** When computing $(dW_t)^2$, we get $dt$, not 0.

## Martingale Property

**Theorem 1.3.11** (Martingale Property)

Brownian motion is a martingale with respect to its natural filtration $\mathcal{F}_t = \sigma(W_s : s \le t)$:

$$\boxed{
\mathbb{E}[W_t \mid \mathcal{F}_s] = W_s, \quad 0 \le s \le t
}$$



**Proof:**

Write:

$$W_t = W_s + (W_t - W_s)$$



By independent increments, $W_t - W_s$ is independent of $\mathcal{F}_s$. Thus:

$$\mathbb{E}[W_t \mid \mathcal{F}_s] = W_s + \mathbb{E}[W_t - W_s \mid \mathcal{F}_s] = W_s + \mathbb{E}[W_t - W_s] = W_s + 0 = W_s \quad \square$$



**Corollary 1.3.12**

The process $W_t^2 - t$ is also a martingale:

$$\mathbb{E}[W_t^2 - t \mid \mathcal{F}_s] = W_s^2 - s$$



**Proof:**


$$\mathbb{E}[W_t^2 \mid \mathcal{F}_s] = \mathbb{E}[(W_s + (W_t - W_s))^2 \mid \mathcal{F}_s]
= W_s^2 + 2W_s\mathbb{E}[W_t - W_s] + \mathbb{E}[(W_t - W_s)^2]$$



$$= W_s^2 + 0 + (t - s) = W_s^2 + t - s$$



Therefore:

$$\mathbb{E}[W_t^2 - t \mid \mathcal{F}_s] = W_s^2 + t - s - t = W_s^2 - s \quad \square$$



This martingale property is essential for stochastic integration and the Itô isometry.

## Strong Markov Property

The Markov property extends to random stopping times.

**Definition 1.3.13** (Stopping Time)

A random variable $\tau: \Omega \to [0, \infty]$ is a **stopping time** with respect to $\{\mathcal{F}_t\}$ if

$$\{\tau \le t\} \in \mathcal{F}_t \quad \text{for all } t \ge 0$$



**Theorem 1.3.14** (Strong Markov Property)

For any stopping time $\tau$ with $\mathbb{P}(\tau < \infty) = 1$ and $t \ge 0$:

$$\boxed{
W_{\tau+t} - W_\tau \text{ is independent of } \mathcal{F}_\tau
}$$


and has the same distribution as $W_t$ (i.e., $\mathcal{N}(0, t)$).

**Proof:** Requires approximation of $\tau$ by discrete stopping times and a limiting argument. See Karatzas & Shreve (1991). $\square$

**Interpretation:** Brownian motion "starts afresh" at stopping times, not just at deterministic times. This is crucial for:
- First passage time analysis
- Optimal stopping problems
- Reflected Brownian motion

## Connection to the Heat Equation

Brownian motion is intimately connected to the **heat equation** (diffusion PDE).

**Theorem 1.3.15** (Feynman-Kac for Heat Equation)

Define

$$u(x,t) = \mathbb{E}[f(x + W_t)]$$


for a bounded continuous function $f: \mathbb{R} \to \mathbb{R}$.

Then $u$ satisfies the heat equation:

$$\boxed{
\frac{\partial u}{\partial t} = \frac{1}{2} \frac{\partial^2 u}{\partial x^2}
}$$


with initial condition $u(x, 0) = f(x)$.

**Proof sketch:**

Compute:

$$\frac{\partial u}{\partial t} = \lim_{h \to 0} \frac{u(x, t+h) - u(x,t)}{h}
= \lim_{h \to 0} \frac{\mathbb{E}[f(x + W_{t+h})] - \mathbb{E}[f(x + W_t)]}{h}$$



Using the Markov property:

$$u(x, t+h) = \mathbb{E}[\mathbb{E}[f(x + W_{t+h}) \mid \mathcal{F}_t]]
= \mathbb{E}[u(x + W_t, h)]$$



For small $h$, expand using Taylor series and $\mathbb{E}[W_h] = 0$, $\mathbb{E}[W_h^2] = h$:

$$u(x + W_t, h) \approx u(x + W_t, 0) + h \frac{\partial u}{\partial t} + W_t \frac{\partial u}{\partial x} + \frac{1}{2}W_t^2 \frac{\partial^2 u}{\partial x^2}$$



Taking expectations and using $\mathbb{E}[W_t] = 0$, $\mathbb{E}[W_t^2] = h$:

$$\frac{\partial u}{\partial t} = \frac{1}{2}\frac{\partial^2 u}{\partial x^2} \quad \square$$



**Remark:** This connection shows that Brownian motion is the **probabilistic representation** of solutions to the heat equation. This is the foundation of the **Feynman-Kac formula** studied in Section 1.7.

## First Passage Times and Reflection Principle

**Definition 1.3.16** (Hitting Time)

For $a \in \mathbb{R}$, define the **first passage time** to level $a$:

$$\tau_a = \inf\{t \ge 0 : W_t = a\}$$



**Theorem 1.3.17** (Recurrence of Brownian Motion)

For all $a \in \mathbb{R}$:

$$\mathbb{P}(\tau_a < \infty) = 1$$



That is, Brownian motion hits every level with probability one.

**Proof sketch:**

By the strong Markov property and symmetry, if $W_t$ hasn't hit $a$ by time $t$, it still has a positive probability of hitting $a$ in the next interval. Repeating this argument infinitely many times gives probability 1. $\square$

**Theorem 1.3.18** (Expected Hitting Time)

Despite certain hitting, the expected hitting time is infinite:

$$\mathbb{E}[\tau_a] = \infty \quad \text{for all } a \neq 0$$



**Proof:**

For $a > 0$, by the optional stopping theorem (which requires justification), if $\mathbb{E}[\tau_a] < \infty$:

$$\mathbb{E}[W_{\tau_a}] = \mathbb{E}[W_0] = 0$$



But $W_{\tau_a} = a$ by definition, giving $a = 0$, a contradiction. $\square$

**Reflection Principle:**

For $a > 0$:

$$\mathbb{P}\left(\max_{0 \le s \le t} W_s \ge a\right) = 2\mathbb{P}(W_t \ge a)$$



This symmetry is derived from reflecting the Brownian path after it first hits level $a$.

## Computational Illustration

*Note: This simulation code can also be placed in a separate "Brownian Motion Simulations" file following the segregated approach.*

### Python Implementation

```python
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Simulation parameters
num_paths = 10_000   # Number of Brownian motion paths
num_steps = 1_000    # Number of time steps
maturity_time = 2    # Maturity time for Brownian motion (T = 2)

# Set random seed for reproducibility
np.random.seed(0)

# Generate time discretization
dt = maturity_time / num_steps
time_steps = np.linspace(0, maturity_time, num_steps + 1)

# Generate Brownian motion paths
# Each increment is N(0, dt), cumsum gives Brownian motion
dW = np.random.normal(0, np.sqrt(dt), size=(num_paths, num_steps))
brownian_paths = np.cumsum(np.hstack([np.zeros((num_paths, 1)), dW]), axis=1)

# Create figure with two subplots
fig, (ax_paths, ax_distribution) = plt.subplots(1, 2, figsize=(12, 4))

# Plot 10 sample paths
ax_paths.set_title(f'Ten Sample Paths of $W_t$')
for i in range(10):
    ax_paths.plot(time_steps, brownian_paths[i, :], alpha=0.7)
ax_paths.set_xlabel('Time $t$')
ax_paths.set_ylabel('$W_t$')
ax_paths.grid(alpha=0.3)

# Plot distribution at maturity
ax_distribution.set_title(f'Distribution of $W_{{{maturity_time}}}$')
_, bin_locations, _ = ax_distribution.hist(
    brownian_paths[:, -1], 
    bins=100, 
    density=True, 
    alpha=0.6, 
    label=f"$W_{{{maturity_time}}}$ Samples"
)

# Overlay theoretical N(0, T) density
x_values = bin_locations
y_values = stats.norm(loc=0, scale=np.sqrt(maturity_time)).pdf(x_values)
ax_distribution.plot(x_values, y_values, '--r', linewidth=2, 
                     label=f"$\mathcal{{N}}(0,{maturity_time})$ PDF")
ax_distribution.set_xlabel('$W_T$')
ax_distribution.set_ylabel('Density')
ax_distribution.legend()
ax_distribution.grid(alpha=0.3)

plt.tight_layout()
plt.show()

# Verify mean and variance
print(f"Sample mean of W_{maturity_time}: {np.mean(brownian_paths[:, -1]):.4f} (theoretical: 0)")
print(f"Sample variance of W_{maturity_time}: {np.var(brownian_paths[:, -1]):.4f} (theoretical: {maturity_time})")
```

**Output interpretation:**
- Left plot shows the characteristic "wiggly" continuous paths
- Right plot confirms $W_T \sim \mathcal{N}(0, T)$
- Sample statistics match theoretical values closely

## Summary

Brownian motion is uniquely characterized by:
1. **Continuous paths** (nowhere differentiable, infinite variation)
2. **Gaussian increments** with variance equal to time elapsed
3. **Independent increments** (Markov property and strong Markov property)
4. **Quadratic variation** $\langle W \rangle_t = t$ (foundation for Itô calculus)
5. **Martingale property** (essential for stochastic integration)
6. **Connection to PDEs** (probabilistic representation of heat equation solutions)

These properties make Brownian motion the fundamental building block for:
- Stochastic differential equations (Chapter 1.6)
- Itô calculus (Chapter 1.4)
- Option pricing via Black-Scholes (later chapters)
- Interest rate models, volatility models, and beyond

## References

- Billingsley, P. (1995). *Probability and Measure*, 3rd ed. Wiley.
- Karatzas, I., & Shreve, S. E. (1991). *Brownian Motion and Stochastic Calculus*, 2nd ed. Springer.
- Kallenberg, O. (2002). *Foundations of Modern Probability*, 2nd ed. Springer.
- Mörters, P., & Peres, Y. (2010). *Brownian Motion*. Cambridge University Press.
- Revuz, D., & Yor, M. (1999). *Continuous Martingales and Brownian Motion*, 3rd ed. Springer.
