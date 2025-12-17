# Itô Processes

An **Itô process** is a stochastic process constructed by combining ordinary (Lebesgue) integration and stochastic (Itô) integration. These processes form the natural class of semimartingales for which Itô's formula applies, and they serve as the foundation for stochastic differential equations in continuous time.

---

## Definition

An **Itô process** is a continuous adapted process \(X_t\) that can be written in the form:


$$
\boxed{
X_t = X_0 + \int_0^t \mu_s \, ds + \int_0^t \sigma_s \, dB_s
}
$$



where:

- \(X_0\) is an \(\mathcal{F}_0\)-measurable random variable (the initial value)
- \(\mu_t\) is an adapted process satisfying \(\int_0^T |\mu_s| \, ds < \infty\) a.s. (the **drift coefficient**)
- \(\sigma_t\) is an adapted process satisfying \(\int_0^T \sigma_s^2 \, ds < \infty\) a.s. (the **diffusion coefficient**)
- \(B_t\) is a standard Brownian motion

**Differential notation**: We often write this compactly as:


$$
dX_t = \mu_t \, dt + \sigma_t \, dB_t
$$



with the understanding that this is shorthand for the integral equation above.

**Interpretation**:

- The **drift term** \(\int_0^t \mu_s ds\) represents deterministic, predictable evolution
- The **diffusion term** \(\int_0^t \sigma_s dB_s\) represents random fluctuations
- The process \(X_t\) is a semimartingale—a sum of a finite variation process and a local martingale

---

## Basic examples

### Example 1: Brownian motion

Standard Brownian motion is the simplest Itô process:


$$
B_t = B_0 + \int_0^t 0 \, ds + \int_0^t 1 \, dB_s = \int_0^t dB_s
$$



Here, \(\mu_t = 0\) (no drift) and \(\sigma_t = 1\) (unit diffusion).

### Example 2: Brownian motion with drift

A Brownian motion with constant drift \(\mu\) and volatility \(\sigma\):


$$
X_t = X_0 + \mu t + \sigma B_t
= X_0 + \int_0^t \mu \, ds + \int_0^t \sigma \, dB_s
$$



In differential form: \(dX_t = \mu \, dt + \sigma \, dB_t\).

**Properties**:

- \(\mathbb{E}[X_t] = X_0 + \mu t\) (linear expected growth)
- \(\text{Var}(X_t) = \sigma^2 t\) (growing uncertainty)
- \(X_t \sim N(X_0 + \mu t, \sigma^2 t)\)

This process is widely used in physics (particle motion with constant force) and finance (stock prices under the Black-Scholes model with log-normal returns).

### Example 3: Integrated Brownian motion

Define:


$$
X_t = \int_0^t B_s \, ds
$$



This is **not** directly an Itô process, but it can be expressed using integration by parts as:


$$
X_t = t B_t - \int_0^t s \, dB_s
$$



Thus, \(X_t\) is an Itô process with:


$$
dX_t = B_t \, dt - t \, dB_t
$$



(This anticipates Itô's integration by parts formula.)

### Example 4: Quadratic variation as an Itô process

The process \(B_t^2 - t\) is a martingale (established in Section 1.2). We can express it as:


$$
B_t^2 - t = \int_0^t 2B_s \, dB_s
$$



This is an Itô process with \(\mu_t = -1\) (implicit drift correction) and \(\sigma_t = 2B_t\).

**Verification**: Applying Itô's formula to \(f(x) = x^2\):


$$
d(B_t^2) = 2B_t \, dB_t + dt
$$



Thus:


$$
d(B_t^2 - t) = 2B_t \, dB_t
$$



confirming the representation.

---

## Differential notation and interpretation

The notation \(dX_t = \mu_t dt + \sigma_t dB_t\) should be understood as:


$$
X_t - X_s = \int_s^t \mu_u \, du + \int_s^t \sigma_u \, dB_u
\quad \text{for } s < t
$$



**Key points**:

1. \(dX_t\) is **not** a derivative—it is an infinitesimal increment
2. \(dt\) represents an ordinary (deterministic) infinitesimal
3. \(dB_t\) represents a stochastic infinitesimal with "variance \(dt\)"
4. The equality is in the integral sense, not pointwise

**Heuristic rules** (formalized by Itô's formula):


$$
\begin{align}
dt \cdot dt &= 0\\
dB_t \cdot dt &= 0\\
dB_t \cdot dB_t &= dt
\end{align}
$$



These "multiplication rules" capture the essence of stochastic calculus: deterministic infinitesimals are negligible compared to stochastic ones, and the quadratic variation of Brownian motion is of order \(dt\).

---

## Properties of Itô processes

### Martingale characterization

An Itô process \(X_t = X_0 + \int_0^t \mu_s ds + \int_0^t \sigma_s dB_s\) is:

1. A **martingale** if and only if \(\mu_t = 0\) a.e. (no drift)
2. A **local martingale** if \(\mu_t = 0\) and \(\sigma_t\) is locally square-integrable
3. A **submartingale** if \(\mu_t \ge 0\) (nonnegative drift)
4. A **supermartingale** if \(\mu_t \le 0\) (nonpositive drift)

**Proof of (1)**: For \(s < t\):


$$
\mathbb{E}[X_t \mid \mathcal{F}_s]
= \mathbb{E}\left[X_s + \int_s^t \mu_u du + \int_s^t \sigma_u dB_u \,\Big|\, \mathcal{F}_s\right]
$$



The stochastic integral is a martingale, so:


$$
\mathbb{E}\left[\int_s^t \sigma_u dB_u \,\Big|\, \mathcal{F}_s\right] = 0
$$



Thus:


$$
\mathbb{E}[X_t \mid \mathcal{F}_s]
= X_s + \mathbb{E}\left[\int_s^t \mu_u du \,\Big|\, \mathcal{F}_s\right]
$$



The martingale property \(\mathbb{E}[X_t \mid \mathcal{F}_s] = X_s\) holds if and only if \(\mu_t = 0\) a.e. \(\square\)

**Example**: The process \(B_t^2 - t\) is a martingale because it has the representation:


$$
B_t^2 - t = \int_0^t 2B_s \, dB_s
$$



with \(\mu_t = 0\).

### Quadratic variation

The quadratic variation of an Itô process is determined entirely by its diffusion coefficient.

**Theorem**: If \(X_t = X_0 + \int_0^t \mu_s ds + \int_0^t \sigma_s dB_s\), then:


$$
\boxed{
[X, X]_t = \int_0^t \sigma_s^2 \, ds
}
$$



**Proof**: The quadratic variation of a finite variation process is zero, so:


$$
\left[\int_0^t \mu_s ds, \int_0^t \mu_s ds\right]_t = 0
$$



By bilinearity of quadratic covariation:


$$
[X, X]_t
= \left[\int_0^t \sigma_s dB_s, \int_0^t \sigma_s dB_s\right]_t
= \int_0^t \sigma_s^2 \, ds
$$



where the last equality follows from the quadratic variation property of the Itô integral. \(\square\)

**Corollary**: The **instantaneous variance** (or **spot volatility**) of \(X_t\) at time \(t\) is \(\sigma_t^2\).

### Path properties

**Theorem (Continuity)**: If \(\mu_t\) and \(\sigma_t\) are continuous adapted processes, then \(X_t\) has continuous sample paths almost surely.

**Proof**: The ordinary integral \(\int_0^t \mu_s ds\) is continuous in \(t\). The stochastic integral \(\int_0^t \sigma_s dB_s\) has a continuous modification (established in the properties section). Therefore, \(X_t\) is continuous. \(\square\)

---

## The Doob-Meyer decomposition

For an Itô process, the **Doob-Meyer decomposition** is explicit.

**Theorem**: Let \(X_t\) be an Itô process with \(\mu_t \ge 0\). Then \(X_t\) is a submartingale, and its Doob-Meyer decomposition is:


$$
X_t = M_t + A_t
$$



where:

- \(M_t = X_0 + \int_0^t \sigma_s dB_s\) is a continuous local martingale
- \(A_t = \int_0^t \mu_s ds\) is a continuous, increasing, adapted process

This decomposition is **unique** (up to indistinguishability).

**Interpretation**: Every submartingale can be decomposed into a "fair game" (martingale) plus a "house advantage" (increasing process). For Itô processes, this decomposition is given explicitly by separating the drift and diffusion terms.

---

## Examples revisited

### Ornstein-Uhlenbeck process

The **Ornstein-Uhlenbeck process** is defined by:


$$
dX_t = -\theta X_t \, dt + \sigma \, dB_t
$$



where \(\theta > 0\) is a mean-reversion parameter and \(\sigma > 0\) is volatility.

This is an Itô process with:

- Drift: \(\mu_t = -\theta X_t\) (mean-reverting toward zero)
- Diffusion: \(\sigma_t = \sigma\) (constant volatility)

**Properties**:

- \(X_t\) is a Gaussian process
- Mean reversion: \(\mathbb{E}[X_t] \to 0\) as \(t \to \infty\)
- Stationary distribution: \(X_t \sim N(0, \sigma^2 / (2\theta))\) for large \(t\)

The Ornstein-Uhlenbeck process is used in physics (velocity of a particle under friction) and finance (interest rate models, volatility models).

### Geometric Brownian motion (informal preview)

Consider the process:


$$
dS_t = \mu S_t \, dt + \sigma S_t \, dB_t
$$



This is **not** directly an Itô process in the sense defined above, because the coefficients \(\mu S_t\) and \(\sigma S_t\) depend on the unknown process \(S_t\) itself.

However, we can interpret this as a **stochastic differential equation (SDE)**, which we will study in Chapter 2. Using Itô's formula, the solution is:


$$
S_t = S_0 \exp\left(\left(\mu - \frac{\sigma^2}{2}\right)t + \sigma B_t\right)
$$



This process is widely used in mathematical finance as a model for stock prices (Black-Scholes model).

---

## Extension: Multidimensional Itô processes

In applications, we often encounter systems of coupled Itô processes.

**Definition**: An \(n\)-dimensional Itô process \(\mathbf{X}_t = (X_t^1, \ldots, X_t^n)^\top\) is a vector process satisfying:


$$
X_t^i = X_0^i + \int_0^t \mu_s^i \, ds + \sum_{j=1}^m \int_0^t \sigma_s^{ij} \, dB_s^j
$$



where \(B^1, \ldots, B^m\) are independent Brownian motions.

In differential form:


$$
dX_t^i = \mu_t^i \, dt + \sum_{j=1}^m \sigma_t^{ij} \, dB_t^j
$$



or in matrix notation:


$$
d\mathbf{X}_t = \boldsymbol{\mu}_t \, dt + \boldsymbol{\Sigma}_t \, d\mathbf{B}_t
$$



where \(\boldsymbol{\Sigma}_t\) is an \(n \times m\) matrix (the **diffusion matrix**).

**Quadratic variation**: For multidimensional Itô processes:


$$
[X^i, X^j]_t = \sum_{k=1}^m \int_0^t \sigma_s^{ik} \sigma_s^{jk} \, ds
$$



This generalizes the scalar case.

---

## Connection to stochastic differential equations

The notation \(dX_t = \mu_t dt + \sigma_t dB_t\) naturally leads to **stochastic differential equations (SDEs)**:


$$
dX_t = \mu(t, X_t) \, dt + \sigma(t, X_t) \, dB_t
$$



where the drift and diffusion coefficients now **depend on the current state** \(X_t\).

**Key difference**:

- **Itô process** (this section): \(\mu_t\) and \(\sigma_t\) are given adapted processes
- **SDE** (Chapter 2): \(\mu_t = \mu(t, X_t)\) and \(\sigma_t = \sigma(t, X_t)\) are functions of the unknown process \(X_t\)

**Example**:

- Itô process: \(dX_t = f(t) \, dt + g(t) \, dB_t\) where \(f, g\) are deterministic
- SDE: \(dX_t = f(t, X_t) \, dt + g(t, X_t) \, dB_t\) where \(f, g\) depend on \(X_t\)

SDEs require existence and uniqueness theorems (Lipschitz conditions, etc.), which we defer to Chapter 2.

---

## Summary

Itô processes are the fundamental building blocks of stochastic calculus:

1. **General form**: \(X_t = X_0 + \int_0^t \mu_s ds + \int_0^t \sigma_s dB_s\)

2. **Components**:
   - Drift \(\mu_t\): deterministic evolution
   - Diffusion \(\sigma_t\): random fluctuations

3. **Key properties**:
   - Continuous paths (if \(\mu, \sigma\) continuous)
   - Quadratic variation: \([X, X]_t = \int_0^t \sigma_s^2 ds\)
   - Martingale iff \(\mu_t = 0\)

4. **Doob-Meyer decomposition**: Explicit splitting into martingale + drift

5. **Examples**: Brownian motion with drift, Ornstein-Uhlenbeck, geometric Brownian motion

**What's next?**

In Section 1.4, we develop **Itô's lemma**—the fundamental theorem for computing \(df(t, X_t)\) when \(X_t\) is an Itô process. This is the "chain rule" of stochastic calculus and enables explicit computation of:

- Transformations of Itô processes
- Solutions to SDEs
- Option pricing formulas
- Optimization in stochastic control

Itô's lemma is where the quadratic variation structure \(dB_t \cdot dB_t = dt\) becomes manifest in calculations, distinguishing stochastic calculus from its classical counterpart.
