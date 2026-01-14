# Moments Brownian



## Introduction



In **Brownian Motion Foundations**, we established that for standard Brownian motion $\{W_t\}_{t \ge 0}$:

$$\mathbb{E}[W_t] = 0, \quad \mathbb{E}[W_t^2] = t$$



These are the first two moments. But what about higher moments? Can we find explicit formulas for $\mathbb{E}[W_t^k]$ for all $k$?

Understanding the complete moment structure of Brownian motion provides:

1. **Analytical tools** for computing expectations of functions of Brownian motion
2. **Connections to Hermite polynomials** and spectral decomposition
3. **Foundation for Wiener chaos decomposition** (used in stochastic analysis and numerical methods)
4. **Moment-matching techniques** in option pricing and risk management

This section derives the full moment structure using the **moment generating function (MGF)** technique, revealing the rich analytical structure underlying the Gaussian distribution.

## Moment Generating



### 1. Definition



For a random variable $X$, the **moment generating function** is:

$$\phi_X(t) := \mathbb{E}[e^{tX}]$$



provided the expectation exists in a neighborhood of $t = 0$.

**Why it's useful:**

The MGF encodes all moments via derivatives:

$$\mathbb{E}[X^k] = \phi_X^{(k)}(0) = \left.\frac{d^k}{dt^k}\mathbb{E}[e^{tX}]\right|_{t=0}$$



Alternatively, via Taylor expansion:

$$\phi_X(t) = \sum_{k=0}^\infty \frac{\mathbb{E}[X^k]}{k!} t^k$$



### 2. MGF Normal Distri



**Theorem 1.5.1** (MGF of Gaussian)

If $X \sim \mathcal{N}(\mu, \sigma^2)$, then:

$$\boxed{
\phi_X(t) = \mathbb{E}[e^{tX}] = \exp\left(\mu t + \frac{1}{2} \sigma^2 t^2\right)
}$$



**Proof:**

We compute:

$$\phi_X(t) = \int_{-\infty}^{\infty} e^{tx} \cdot \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left( -\frac{(x - \mu)^2}{2 \sigma^2} \right) dx$$



$$= \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left( -\frac{(x - \mu)^2}{2\sigma^2} + tx \right) dx$$



**Step 1: Complete the square in the exponent.**


$$-\frac{(x - \mu)^2}{2\sigma^2} + tx = -\frac{1}{2\sigma^2} \left[ (x - \mu)^2 - 2\sigma^2 tx \right]$$



$$= -\frac{1}{2\sigma^2} \left[ x^2 - 2\mu x + \mu^2 - 2\sigma^2 t x \right]$$



$$= -\frac{1}{2\sigma^2} \left[ x^2 - 2(\mu + \sigma^2 t)x + \mu^2 \right]$$



Add and subtract $(\mu + \sigma^2 t)^2$:

$$= -\frac{1}{2\sigma^2} \left[ x^2 - 2(\mu + \sigma^2 t)x + (\mu + \sigma^2 t)^2 - (\mu + \sigma^2 t)^2 + \mu^2 \right]$$



$$= -\frac{(x - (\mu + \sigma^2 t))^2}{2\sigma^2} + \frac{(\mu + \sigma^2 t)^2 - \mu^2}{2\sigma^2}$$



Simplify the constant term:

$$\frac{(\mu + \sigma^2 t)^2 - \mu^2}{2\sigma^2} = \frac{\mu^2 + 2\mu\sigma^2 t + \sigma^4 t^2 - \mu^2}{2\sigma^2} = \mu t + \frac{1}{2}\sigma^2 t^2$$



**Step 2: Factor out the constant.**


$$\phi_X(t) = \exp\left(\mu t + \frac{1}{2} \sigma^2 t^2\right) \int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left( -\frac{(x - (\mu + \sigma^2 t))^2}{2\sigma^2} \right) dx$$



The integral is the total probability of a Gaussian density with mean $\mu + \sigma^2 t$ and variance $\sigma^2$:

$$\int_{-\infty}^{\infty} \frac{1}{\sqrt{2\pi \sigma^2}} \exp\left( -\frac{(x - (\mu + \sigma^2 t))^2}{2\sigma^2} \right) dx = 1$$



Therefore:

$$\phi_X(t) = \exp\left(\mu t + \frac{1}{2} \sigma^2 t^2\right) \quad \square$$



**Corollary 1.5.2**

For standard Brownian motion at time $T$, $W_T \sim \mathcal{N}(0, T)$, so:

$$\mathbb{E}[e^{\theta W_T}] = \exp\left(\frac{1}{2} \theta^2 T\right)$$



## Complete Moment



### 1. Main Result



**Theorem 1.5.3** (Moments of Brownian Motion)

Let $W_T$ be standard Brownian motion at time $T$. Then:

1. **Odd moments vanish:**

$$\boxed{
\mathbb{E}[W_T^{2k+1}] = 0 \quad \text{for all } k \ge 0
}$$



2. **Even moments:**

$$\boxed{
\mathbb{E}[W_T^{2k}] = \frac{(2k)!}{k! \, 2^k} T^k = (2k-1)!! \cdot T^k \quad \text{for all } k \ge 0
}$$



where $(2k-1)!! = 1 \cdot 3 \cdot 5 \cdots (2k-1)$ is the **double factorial**.

**Proof:**

Since $W_T \sim \mathcal{N}(0, T)$, by Corollary 1.5.2:

$$\mathbb{E}[e^{\theta W_T}] = \exp\left(\frac{1}{2} T \theta^2\right)$$



**Step 1: Expand the MGF in a Taylor series.**

On the left-hand side:

$$\mathbb{E}[e^{\theta W_T}] = \mathbb{E}\left[\sum_{k=0}^\infty \frac{(\theta W_T)^k}{k!}\right] = \sum_{k=0}^\infty \frac{\mathbb{E}[W_T^k]}{k!} \theta^k$$



On the right-hand side:

$$\exp\left(\frac{1}{2} T \theta^2\right) = \sum_{j=0}^\infty \frac{1}{j!} \left(\frac{1}{2} T \theta^2\right)^j = \sum_{j=0}^\infty \frac{T^j}{j! \, 2^j} \theta^{2j}$$



**Step 2: Compare coefficients.**

The right-hand side contains **only even powers** of $\theta$. Therefore:

- Coefficients of $\theta^{2k+1}$: 

$$\frac{\mathbb{E}[W_T^{2k+1}]}{(2k+1)!} = 0 \implies \mathbb{E}[W_T^{2k+1}] = 0$$



- Coefficients of $\theta^{2k}$:

$$\frac{\mathbb{E}[W_T^{2k}]}{(2k)!} = \frac{T^k}{k! \, 2^k}$$



Solving for $\mathbb{E}[W_T^{2k}]$:

$$\mathbb{E}[W_T^{2k}] = \frac{(2k)!}{k! \, 2^k} T^k$$



**Step 3: Relate to double factorial.**

Note that:

$$(2k-1)!! = 1 \cdot 3 \cdot 5 \cdots (2k-1) = \frac{(2k)!}{2^k \cdot k!}$$



This is because:

$$(2k)! = [2k \cdot (2k-2) \cdot (2k-4) \cdots 2] \cdot [(2k-1) \cdot (2k-3) \cdots 1]$$



$$= 2^k \cdot k! \cdot (2k-1)!!$$



Therefore:

$$\mathbb{E}[W_T^{2k}] = (2k-1)!! \cdot T^k \quad \square$$



### 2. Explicit Values



**Table of first few moments:**

| $k$ | $\mathbb{E}[W_T^k]$ | Value at $T=1$ |
|-----|---------------------|----------------|
| 0 | 1 | 1 |
| 1 | 0 | 0 |
| 2 | $T$ | 1 |
| 3 | 0 | 0 |
| 4 | $3T^2$ | 3 |
| 5 | 0 | 0 |
| 6 | $15T^3$ | 15 |
| 7 | 0 | 0 |
| 8 | $105T^4$ | 105 |

**Pattern:** Even moments grow as $(2k-1)!! \cdot T^k$, where:

$$1!! = 1, \quad 3!! = 3, \quad 5!! = 15, \quad 7!! = 105, \quad \ldots$$



### 3. Alternative Deriv



**Alternative proof for even moments:**


$$\mathbb{E}[W_T^{2k}] = \int_{-\infty}^{\infty} x^{2k} \frac{1}{\sqrt{2\pi T}} e^{-x^2/(2T)} dx$$



Substitute $y = x/\sqrt{T}$:

$$= \int_{-\infty}^{\infty} (y\sqrt{T})^{2k} \frac{1}{\sqrt{2\pi}} e^{-y^2/2} \sqrt{T} \, dy = T^k \int_{-\infty}^{\infty} y^{2k} \frac{1}{\sqrt{2\pi}} e^{-y^2/2} dy$$



The integral $\int_{-\infty}^{\infty} y^{2k} \frac{1}{\sqrt{2\pi}} e^{-y^2/2} dy = (2k-1)!!$ is a standard result for the standard normal distribution.

## Deeper Analytical



### 1. Connection Hermit



The moments are intimately connected to **Hermite polynomials**, which form an orthogonal basis in $L^2(\mathbb{R}, e^{-x^2/2}dx)$.

**Definition:** The **probabilist's Hermite polynomials** $H_n(x)$ are defined by:

$$H_n(x) = (-1)^n e^{x^2/2} \frac{d^n}{dx^n} e^{-x^2/2}$$



or equivalently via the generating function:

$$e^{tx - t^2/2} = \sum_{n=0}^\infty \frac{t^n}{n!} H_n(x)$$



**Key property:**

If $X \sim \mathcal{N}(0,1)$, then:

$$\mathbb{E}[H_n(X)] = 0 \quad \text{for } n \ge 1$$



$$\mathbb{E}[H_m(X) H_n(X)] = n! \, \delta_{mn}$$



**Connection to moments:**

The moments can be expressed as:

$$\mathbb{E}[X^n] = \mathbb{E}[H_n(X)] + \text{lower order terms}$$



For example:

- $H_0(x) = 1$, so $\mathbb{E}[H_0(X)] = 1$
- $H_1(x) = x$, so $\mathbb{E}[H_1(X)] = 0$
- $H_2(x) = x^2 - 1$, so $\mathbb{E}[H_2(X)] = 0$ and $\mathbb{E}[X^2] = 1$
- $H_3(x) = x^3 - 3x$, so $\mathbb{E}[X^3] = 3\mathbb{E}[X] = 0$
- $H_4(x) = x^4 - 6x^2 + 3$, so $\mathbb{E}[X^4] = 6\mathbb{E}[X^2] - 3 = 3$

### 2. Wiener Chaos Deco



The Hermite polynomials provide a **spectral decomposition** of $L^2(\Omega, \mathcal{F}, \mathbb{P})$ for functionals of Brownian motion.

**Theorem 1.5.4** (Wiener Chaos Expansion - Informal Statement)

Any $F \in L^2(\Omega)$ measurable with respect to $\sigma(W_s : s \in [0,T])$ can be written as:

$$F = \sum_{n=0}^\infty I_n(f_n)$$


where $I_n$ is the $n$-th order **multiple Wiener integral**.

**For Brownian motion at time $T$:**

$$W_T^{2k} = \sum_{j=0}^{2k} c_{j} H_j(W_T/\sqrt{T})$$



The moments $\mathbb{E}[W_T^{2k}]$ determine the coefficients $c_j$ in this expansion.

**Application:** This decomposition is fundamental in:
- Malliavin calculus
- Numerical methods for SPDEs
- Variance reduction in Monte Carlo simulation

### 3. Wick Products Nor



The double factorial $(2k-1)!!$ counts the number of **pairings** in Wick products.

**Definition:** The **Wick product** (normal ordered product) of $W_T$ is:

$$:W_T^{2k}: = \sum_{j=0}^k (-1)^j \binom{k}{j} (2j-1)!! \, T^j \, W_T^{2k-2j}$$



**Property:**

$$\mathbb{E}[:W_T^{2k}:] = 0$$



The ordinary moment is:

$$W_T^{2k} = :W_T^{2k}: + \text{lower order Wick products}$$



This structure appears in:

- Quantum field theory (Feynman diagrams)
- Combinatorics (matching problems)
- Stochastic analysis (cumulants)

## Asymptotic Behavior



### 1. Growth Rate



Using Stirling's approximation:

$$k! \sim \sqrt{2\pi k} \left(\frac{k}{e}\right)^k$$



We can estimate:

$$(2k-1)!! = \frac{(2k)!}{2^k k!} \sim \sqrt{2} \left(\frac{2k}{e}\right)^k$$



Therefore:

$$\mathbb{E}[W_T^{2k}] \sim \sqrt{2} \left(\frac{2kT}{e}\right)^k$$



**Interpretation:** Moments grow **superexponentially** in $k$. This reflects the heavy contribution of tail behavior despite Gaussian decay:

- Probability decays as $e^{-x^2/(2T)}$ (super-exponentially fast)
- But moments grow due to $x^{2k}$ weighting in the integral
- The balance gives factorial growth

**Comparison with bounded processes:**

For a process $X_t$ bounded by $|X_t| \le M$:

$$\mathbb{E}[X_T^{2k}] \le M^{2k}$$



The moment sequence is dominated by a geometric sequence, not factorials.

## Applications



### 1. Application 1 Com



**Example:** Compute $\mathbb{E}\left[\left(\int_0^T W_s ds\right)^2\right]$.

**Solution:**

By Fubini's theorem:

$$\mathbb{E}\left[\left(\int_0^T W_s ds\right)^2\right] = \mathbb{E}\left[\int_0^T \int_0^T W_s W_t \, ds \, dt\right]$$



$$= \int_0^T \int_0^T \mathbb{E}[W_s W_t] \, ds \, dt = \int_0^T \int_0^T \min(s,t) \, ds \, dt$$



Splitting the region:

$$= 2\int_0^T \int_0^s t \, dt \, ds = 2\int_0^T \frac{s^2}{2} ds = \frac{T^3}{3}$$



This uses $\mathbb{E}[W_s W_t] = \min(s,t)$ from the covariance structure, which is derivable from the second moment.

### 2. Application 2 Mom



In incomplete markets, one approach to pricing is **moment matching**:

1. Compute moments of the underlying asset return (e.g., $\mathbb{E}[S_T^k]$)
2. Find a distribution that matches these moments
3. Price the option under this distribution

For geometric Brownian motion:

$$S_T = S_0 e^{(\mu - \sigma^2/2)T + \sigma W_T}$$



The moments $\mathbb{E}[W_T^k]$ determine $\mathbb{E}[S_T^k]$ via:

$$\mathbb{E}[S_T^k] = S_0^k e^{k(\mu - \sigma^2/2)T} \mathbb{E}[e^{k\sigma W_T}] = S_0^k e^{k\mu T + k^2\sigma^2T/2}$$



### 3. Application 3 Var



In Monte Carlo simulation, one can use:

$$W_T^2 - T$$


as a **control variate** (it has zero mean and known variance).

The variance of $W_T^2$ is:

$$\text{Var}(W_T^2) = \mathbb{E}[W_T^4] - (\mathbb{E}[W_T^2])^2 = 3T^2 - T^2 = 2T^2$$



This is computed using the fourth moment formula.

### 4. Application 4 Che



When implementing numerical schemes for SDEs, one can verify correctness by checking if simulated paths match theoretical moments.

**Example:** For Euler-Maruyama discretization of $dX_t = dW_t$:

$$X_{n+1} = X_n + \sqrt{\Delta t} \, Z_n$$


where $Z_n \sim \mathcal{N}(0,1)$.

At time $T = N \Delta t$:

$$X_N = \sum_{n=0}^{N-1} \sqrt{\Delta t} \, Z_n$$



Expected moments:

$$\mathbb{E}[X_N^2] = N \Delta t = T \quad \checkmark$$



$$\mathbb{E}[X_N^4] = \mathbb{E}\left[\left(\sum_{n=0}^{N-1} \sqrt{\Delta t} \, Z_n\right)^4\right] = 3(N\Delta t)^2 = 3T^2 \quad \text{(requires calculation)}$$



Checking against the theoretical value $3T^2$ verifies the scheme.

## Summary



The complete moment structure of Brownian motion is:

1. **Odd moments vanish:** $\mathbb{E}[W_T^{2k+1}] = 0$ (by symmetry)
2. **Even moments:** $\mathbb{E}[W_T^{2k}] = (2k-1)!! \cdot T^k$ (by MGF method)
3. **Growth rate:** Moments grow as $\sim \sqrt{2}(2kT/e)^k$ (superexponential)

**Key insights:**

- The MGF technique provides a systematic way to compute all moments
- The double factorial $(2k-1)!!$ has deep connections to combinatorics (pairings)
- Moments encode the full Gaussian structure and connect to Hermite polynomials
- The Wiener chaos decomposition uses moments to build a spectral basis
- Applications range from option pricing to numerical verification

**Looking ahead:**

These moment formulas will be used in:
- **Itô's lemma** (Chapter 1.4): Computing $\mathbb{E}[f(W_T)]$ for nonlinear $f$
- **Feynman-Kac formula** (Chapter 1.7): Solving PDEs via expectations
- **Monte Carlo methods**: Variance reduction and moment matching

## Exercises



1. Verify that $\mathbb{E}[W_T^6] = 15T^3$ by direct integration against the Gaussian density.

2. Compute $\mathbb{E}[W_T^8]$ using the MGF method.

3. Show that $\text{Var}(W_T^2) = 2T^2$ using the fourth moment formula.

4. For geometric Brownian motion $S_T = S_0 e^{(\mu - \sigma^2/2)T + \sigma W_T}$, compute $\mathbb{E}[S_T]$ and $\text{Var}(S_T)$ using the MGF of $W_T$.

5. Prove that $(2k-1)!! = \frac{(2k)!}{2^k k!}$ by induction or direct counting argument.

6. Show that $\mathbb{E}[(W_T - W_S)^4] = 3(T-S)^2$ for $S < T$ using the moment formula and independent increments.

## References



- Karatzas, I., & Shreve, S. E. (1991). *Brownian Motion and Stochastic Calculus*, 2nd ed. Springer. (Chapter 1)
- Nualart, D. (2006). *The Malliavin Calculus and Related Topics*, 2nd ed. Springer. (Wiener chaos decomposition)
- Janson, S. (1997). *Gaussian Hilbert Spaces*. Cambridge University Press. (Hermite polynomials and moments)
- Simon, B. (2015). *Basic Complex Analysis*. American Mathematical Society. (Generating functions and moment problems)
