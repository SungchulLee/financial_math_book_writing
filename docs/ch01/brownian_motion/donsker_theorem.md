# Donsker's Theorem

## Introduction

The **Donsker invariance principle** (also called **Donsker's theorem** or the **functional central limit theorem**) rigorously establishes that appropriately scaled random walks converge to Brownian motion. This is not merely convergence of finite-dimensional distributions, but **weak convergence in the space of continuous functions** $C[0,T]$.

This theorem:

- Justifies treating Brownian motion as the continuous limit of discrete random walks
- Explains why diverse physical phenomena (diffusion, stock prices, polymer chains) exhibit similar statistical behavior
- Provides theoretical foundation for Monte Carlo simulation using discrete approximations

Before diving into the rigorous mathematics, we place Donsker's contribution within the broader historical development of Brownian motion theory.

## Historical and Conceptual Context

### The Logical Chain: Wiener → Kolmogorov → Donsker → Lévy

The development of Brownian motion theory follows a coherent mathematical progression. While the chronological order differs slightly (Lévy's foundational work spans the 1930s–40s, overlapping with Kolmogorov, while Donsker's theorem appeared in 1951), the **conceptual order** tells a cleaner story:

| Mathematician | Contribution | Key Question |
|---------------|--------------|--------------|
| **Wiener** (1923) | Construction | How do we build a probability measure on path space? |
| **Kolmogorov** (1933) | Axiomatization | What does it mean to define a stochastic process? |
| **Donsker** (1951) | Universality | Why does Brownian motion arise everywhere? |
| **Lévy** (1930s–48) | Structure | What are the intrinsic properties of Brownian paths? |

*Note on Lévy:* Paul Lévy developed local time theory in the 1930s and published his comprehensive treatise *Processus stochastiques et mouvement brownien* in 1948. His work on fine path properties and the characterization of Brownian motion via independent increments logically depends on existence theory, hence the conceptual ordering above.

### Wiener: Constructing Brownian Motion as a Measure on Path Space

**The Problem.** Before Wiener, Brownian motion was described by Gaussian transition densities and the heat equation, but **no probability space** existed on which a single random continuous path lived. The fundamental difficulty:

> How do you define a probability measure on an infinite-dimensional space of functions?

**Wiener's Solution.** Wiener constructed a probability measure $\mu$ on $C([0,\infty), \mathbb{R})$ such that the coordinate process $W_t(\omega) = \omega(t)$ satisfies:

- $W_0 = 0$
- Independent, stationary Gaussian increments
- Almost surely continuous paths

This is **Wiener measure**. Mathematically, expectation is defined via limits of finite-dimensional integrals, and tight control of Gaussian increments ensures path continuity.

**Significance.** Brownian motion becomes a bona fide random element of a Banach space—no longer a heuristic. However, the construction is highly specialized and gives little guidance for other processes.

### Kolmogorov: Abstract Existence and Regularity

Kolmogorov asked a deeper structural question:

> What does it *mean* to define a stochastic process?

**Axiomatization.** Probability is now $(\Omega, \mathcal{F}, \mathbb{P})$, and processes are families of random variables $\{X_t\}_{t \in T}$. This separates the **law** of the process from any particular realization.

**Extension Theorem.** Kolmogorov proved that a consistent family of finite-dimensional distributions defines a stochastic process. For Brownian motion, Gaussian marginals with covariance $\mathbb{E}[W_s W_t] = \min(s,t)$ are sufficient to ensure existence—before path properties are even discussed.

**Continuity Criterion.** Kolmogorov's continuity theorem shows that moment bounds imply existence of continuous (or Hölder) modifications. Applied to Brownian motion, this explains continuity rigorously and quantifies roughness (Hölder exponent $< 1/2$).

**Key Shift.** Existence and regularity become **theorems**, not construction-dependent facts.

### Donsker: Brownian Motion as a Universal Scaling Limit

At this point, Brownian motion exists abstractly—but it remains a *primitive object*. Donsker asked the crucial question:

> Why does Brownian motion arise in nature and in mathematics?

The answer is the **functional central limit theorem**: Brownian motion is not fundamental but rather the **universal diffusive limit** of discrete random systems. This explains why Wiener's object is canonical and why Kolmogorov's Gaussian process is ubiquitous.

The remainder of this chapter develops Donsker's theorem rigorously.

### Lévy: Brownian Motion as a Canonical Pathwise Object

After Donsker establishes universality, Lévy asks the final, deepest question:

> Given that Brownian motion is universal, what is its intrinsic structure?

**Independent Increments as Structure.** Lévy identifies Brownian motion as the unique (up to scaling) continuous process with stationary independent increments, leading to the general theory of **Lévy processes**.

**Fine Path Properties.** Lévy investigates exact modulus of continuity, the law of the iterated logarithm, and almost sure oscillatory behavior—showing Brownian motion is continuous but maximally irregular.

**Local Time.** One of Lévy's deepest insights: Brownian paths admit a **local time** $L_t(x)$ measuring how long the path spends near $x$, connecting Brownian motion to potential theory, PDEs, and later stochastic calculus.

## Function Space Setup

### The Space $C[0,T]$

Let $C[0,T]$ denote the space of continuous functions $\omega: [0,T] \to \mathbb{R}$ with $\omega(0) = 0$.

**Metric.** We equip $C[0,T]$ with the **uniform metric** (supremum norm):

$$d(\omega_1, \omega_2) := \sup_{t \in [0,T]} |\omega_1(t) - \omega_2(t)|$$

**Borel $\sigma$-algebra.** Let $\mathcal{B}(C[0,T])$ be the Borel $\sigma$-algebra generated by open sets in the uniform metric.

**Topology.** The uniform metric induces the topology of **uniform convergence**. A sequence $\omega_n \to \omega$ in $C[0,T]$ if and only if

$$\sup_{t \in [0,T]} |\omega_n(t) - \omega(t)| \to 0$$

### Probability Measures on Path Space

A **probability measure** $\mathbb{P}$ on $(C[0,T], \mathcal{B}(C[0,T]))$ assigns probabilities to sets of continuous paths.

**Canonical process.** Define the coordinate process $W_t(\omega) = \omega(t)$ for $\omega \in C[0,T]$. Then $\{W_t\}_{t \in [0,T]}$ is a stochastic process with sample paths in $C[0,T]$.

**Example.** **Wiener measure** $\mathbb{W}$ on $C[0,T]$ is the unique probability measure such that the canonical process $\{W_t\}$ is a Brownian motion.

## Weak Convergence in Function Spaces

### Definition

**Definition 1.2.1** (Weak Convergence in $C[0,T]$)

A sequence of probability measures $\{\mathbb{P}_n\}$ on $C[0,T]$ **converges weakly** to $\mathbb{P}$ (written $\mathbb{P}_n \Rightarrow \mathbb{P}$) if for every bounded continuous functional $F: C[0,T] \to \mathbb{R}$:

$$\int_{C[0,T]} F(\omega) \, d\mathbb{P}_n(\omega) \to \int_{C[0,T]} F(\omega) \, d\mathbb{P}(\omega)$$

**Equivalently** (Portmanteau theorem), any of the following conditions implies the others:

1. $\mathbb{E}_n[F] \to \mathbb{E}[F]$ for all bounded continuous $F$
2. $\limsup_n \mathbb{P}_n(C) \leq \mathbb{P}(C)$ for all closed sets $C$
3. $\liminf_n \mathbb{P}_n(G) \geq \mathbb{P}(G)$ for all open sets $G$
4. $\lim_n \mathbb{P}_n(A) = \mathbb{P}(A)$ for all continuity sets $A$ (i.e., $\mathbb{P}(\partial A) = 0$)

### Convergence in Distribution

If $X_n$ are $C[0,T]$-valued random elements with laws $\mathbb{P}_n$, we write

$$X_n \xrightarrow{d} X \quad \text{or} \quad X_n \Rightarrow X$$

if $\mathbb{P}_n \Rightarrow \mathbb{P}$, where $\mathbb{P}$ is the law of $X$.

**For our purposes:** We view the scaled random walk $S^{(n)}$ as a random element of $C[0,T]$ via piecewise linear interpolation:

$$W^{(n)}(t) = \frac{1}{\sqrt{n}} S_{\lfloor nt \rfloor} + (nt - \lfloor nt \rfloor) \frac{\xi_{\lfloor nt \rfloor+1}}{\sqrt{n}}$$

## Donsker's Theorem

### Statement

**Theorem 1.2.2** (Donsker's Invariance Principle)

Let $\{\xi_i\}_{i=1}^{\infty}$ be i.i.d. random variables with

$$\mathbb{E}[\xi_i] = 0, \quad \mathbb{E}[\xi_i^2] = 1, \quad \mathbb{E}[|\xi_i|^3] < \infty$$

Define $S_n = \sum_{i=1}^n \xi_i$ and the continuous-time interpolation

$$W^{(n)}(t) = \frac{1}{\sqrt{n}} S_{\lfloor nt \rfloor} + (nt - \lfloor nt \rfloor) \frac{\xi_{\lfloor nt \rfloor+1}}{\sqrt{n}}, \quad t \in [0,T]$$

Then as $n \to \infty$:

$$W^{(n)} \Rightarrow W \quad \text{in } C[0,T]$$

where $W$ is a standard Brownian motion on $[0,T]$.

**Remarks:**

1. **Moment conditions:** The finite third moment $\mathbb{E}[|\xi_i|^3] < \infty$ is used to obtain Berry-Esseen type quantitative convergence rates. However, this condition can be relaxed:

   - **Minimal condition:** $\mathbb{E}[\xi_i^2] = 1$ suffices for the theorem to hold, since the Lindeberg condition is automatically satisfied for i.i.d. sequences with finite variance.
   - **Stronger condition:** $\mathbb{E}[|\xi_i|^3] < \infty$ provides explicit error bounds of order $O(n^{-1/2})$ in the CLT approximation.

2. **"Invariance principle"** refers to the fact that the **limit is universal**—it depends only on the first two moments of $\xi_i$, not the entire distribution. Any centered, unit-variance i.i.d. sequence gives the same limit.

3. For simple random walk ($\xi_i \in \{-1,1\}$ with equal probability), all moment conditions are trivially satisfied.

### Proof Strategy

Proving weak convergence in infinite-dimensional spaces requires two steps:

**Step 1: Finite-dimensional convergence.** For any $0 \leq t_1 < t_2 < \cdots < t_k \leq T$:

$$\left(W^{(n)}(t_1), \ldots, W^{(n)}(t_k)\right) \xrightarrow{d} \left(W(t_1), \ldots, W(t_k)\right)$$

as $n \to \infty$ in $\mathbb{R}^k$.

**Step 2: Tightness.** The sequence $\{W^{(n)}\}$ is tight in $C[0,T]$, i.e., for every $\epsilon > 0$, there exists a compact set $K_\epsilon \subset C[0,T]$ such that

$$\sup_n \mathbb{P}(W^{(n)} \notin K_\epsilon) < \epsilon$$

By **Prokhorov's theorem**, tightness plus finite-dimensional convergence implies weak convergence.

**Theorem 1.2.2a** (Prokhorov's Theorem)

Let $\{\mathbb{P}_n\}$ be a sequence of probability measures on a Polish space (complete separable metric space) $S$. Then:

1. If $\{\mathbb{P}_n\}$ is tight, it is **relatively compact**: every subsequence has a further subsequence that converges weakly.
2. Conversely, if $\{\mathbb{P}_n\}$ is relatively compact, it is tight.

In particular, tightness combined with uniqueness of finite-dimensional limits implies weak convergence of the entire sequence.

## Finite-Dimensional Convergence

### Multivariate CLT for Increments

**Lemma 1.2.3**

For fixed times $0 = t_0 < t_1 < \cdots < t_k \leq T$, define the increment vector:

$$\mathbf{Y}^{(n)} = \begin{pmatrix} W^{(n)}(t_1) - W^{(n)}(t_0) \\ W^{(n)}(t_2) - W^{(n)}(t_1) \\ \vdots \\ W^{(n)}(t_k) - W^{(n)}(t_{k-1}) \end{pmatrix}$$

Then $\mathbf{Y}^{(n)} \xrightarrow{d} \mathbf{Y}$, where $\mathbf{Y} \sim \mathcal{N}(0, \Sigma)$ with

$$\Sigma = \text{diag}(t_1 - t_0, t_2 - t_1, \ldots, t_k - t_{k-1})$$

**Proof:**

Each increment

$$W^{(n)}(t_{i+1}) - W^{(n)}(t_i) \approx \frac{1}{\sqrt{n}} \sum_{j=\lfloor nt_i \rfloor+1}^{\lfloor nt_{i+1} \rfloor} \xi_j$$

is a sum of approximately $n(t_{i+1} - t_i)$ i.i.d. terms with mean 0 and variance 1.

By the multivariate CLT (or Cramér–Wold device), since the increments are independent:

$$\mathbf{Y}^{(n)} \xrightarrow{d} \mathcal{N}(0, \Sigma) \quad \square$$

**Corollary 1.2.4**

Since $(W(t_1), \ldots, W(t_k))$ can be written as partial sums of the independent Gaussian increments:

$$(W^{(n)}(t_1), \ldots, W^{(n)}(t_k)) \xrightarrow{d} (W(t_1), \ldots, W(t_k))$$

where $W$ is a Brownian motion. $\square$

## Tightness

Establishing tightness requires showing the scaled random walks don't oscillate too wildly.

### Modulus of Continuity

**Definition 1.2.5** (Modulus of Continuity)

For $\omega \in C[0,T]$ and $\delta > 0$, define:

$$w_\omega(\delta) := \sup_{\substack{s,t \in [0,T] \\ |t-s| \leq \delta}} |\omega(t) - \omega(s)|$$

This measures the maximum oscillation of $\omega$ over intervals of length $\delta$.

**Lemma 1.2.6** (Arzelà–Ascoli)

A subset $K \subset C[0,T]$ is compact if and only if:

1. $K$ is closed and bounded
2. $K$ is **equicontinuous**: $\lim_{\delta \to 0} \sup_{\omega \in K} w_\omega(\delta) = 0$

### Aldous' Tightness Criterion

**Theorem 1.2.7** (Aldous' Criterion for $C[0,T]$)

The sequence $\{W^{(n)}\}$ is tight in $C[0,T]$ if:

1. For each $t \in [0,T]$, $\{W^{(n)}(t)\}$ is tight in $\mathbb{R}$ (uniformly bounded in probability)

2. For every $\epsilon > 0$ and $\eta > 0$, there exists $\delta > 0$ such that

$$\limsup_{n \to \infty} \mathbb{P}\left( w_{W^{(n)}}(\delta) \geq \epsilon \right) \leq \eta$$

### Verification of Tightness

**Condition (1).** By finite-dimensional convergence, $W^{(n)}(t) \xrightarrow{d} W(t) \sim \mathcal{N}(0,t)$, so $\{W^{(n)}(t)\}$ is tight in $\mathbb{R}$.

**Condition (2).** We need to control oscillations. For $|t-s| \leq \delta$:

$$|W^{(n)}(t) - W^{(n)}(s)| \approx \frac{1}{\sqrt{n}} \left| \sum_{i=\lfloor ns \rfloor+1}^{\lfloor nt \rfloor} \xi_i \right|$$

The number of terms is approximately $n|t-s| \leq n\delta$. By Markov's inequality:

$$\mathbb{P}(|W^{(n)}(t) - W^{(n)}(s)| \geq \epsilon) \leq \frac{\mathbb{E}[|W^{(n)}(t) - W^{(n)}(s)|^2]}{\epsilon^2} = \frac{|t-s|}{\epsilon^2} \leq \frac{\delta}{\epsilon^2}$$

To control the modulus of continuity $w_{W^{(n)}}(\delta)$, we cannot simply apply a union bound over a $\delta$-net (which would give a bound independent of $\delta$). Instead, we require a **maximal inequality**. Using Doob's $L^2$ maximal inequality for the martingale $M_k = \sum_{i=1}^k \xi_i$:

$$\mathbb{E}\left[\max_{1 \leq k \leq m} M_k^2\right] \leq 4\mathbb{E}[M_m^2] = 4m$$

Applying this to control oscillations over intervals of length $\delta$ (containing $\approx n\delta$ steps):

$$\mathbb{P}\left( w_{W^{(n)}}(\delta) \geq \epsilon \right) \leq \frac{C \cdot T \cdot \delta}{\epsilon^2}$$

for some constant $C > 0$. Choosing $\delta$ sufficiently small makes this probability arbitrarily small, uniformly in $n$. $\square$

### Completing the Proof

**Proof of Donsker's Theorem (Sketch):**

1. *Finite-dimensional convergence* holds by the multivariate CLT
2. *Tightness* holds by Aldous' criterion
3. By **Prokhorov's theorem**, $\{W^{(n)}\}$ has a weakly convergent subsequence
4. The limit must have the finite-dimensional distributions of Brownian motion
5. By **uniqueness of Brownian motion**, the limit is standard Brownian motion
6. Since the limit is unique, the entire sequence converges (not just a subsequence)

Therefore: $W^{(n)} \Rightarrow W$ in $C[0,T]$. $\square$

## Consequences and Applications

### Continuous Mapping Theorem

**Theorem 1.2.8** (Continuous Mapping Theorem)

If $W^{(n)} \Rightarrow W$ in $C[0,T]$ and $\Phi: C[0,T] \to \mathbb{R}$ is continuous with respect to the uniform metric, then:

$$\Phi(W^{(n)}) \xrightarrow{d} \Phi(W)$$

**Applications:**

1. **Maximum functional:** $\Phi(\omega) = \sup_{t \in [0,T]} \omega(t)$

$$\sup_{t \in [0,T]} W^{(n)}(t) \xrightarrow{d} \sup_{t \in [0,T]} W(t)$$

2. **Occupation time:** For continuous $f$:

$$\int_0^T f(W^{(n)}(s)) \, ds \xrightarrow{d} \int_0^T f(W(s)) \, ds$$

3. **Reflection principle:** Properties of the reflected Brownian motion $|W(t)|$ can be studied via limiting discrete random walks.

### Generalization to Non-Unit Variance

**Corollary 1.2.9**

If $\mathbb{E}[\xi_i] = 0$ and $\mathbb{E}[\xi_i^2] = \sigma^2$, then with the piecewise linear interpolation:

$$W^{(n)}(t) := \frac{1}{\sqrt{n}} S_{\lfloor nt \rfloor} + (nt - \lfloor nt \rfloor) \frac{\xi_{\lfloor nt \rfloor+1}}{\sqrt{n}} \Rightarrow \sigma W(t)$$

where $W$ is standard Brownian motion.

**Proof:** Rescale $\xi_i' = \xi_i/\sigma$ to have unit variance, apply Donsker, then scale back. $\square$

This explains why volatility $\sigma$ appears as a **multiplier** in stochastic differential equations:

$$dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$$

### Constructing Brownian Motion via Limiting Random Walks

Donsker's theorem provides an alternative approach to **constructing** Brownian motion:

1. Fix a probability space $(\Omega, \mathcal{F}, \mathbb{P})$ supporting i.i.d. $\{\xi_i\}$ with mean 0, variance 1
2. Define $W^{(n)}$ as above
3. By Skorokhod's representation theorem, we can find a probability space where $W^{(n)} \to W$ almost surely in $C[0,T]$
4. The limit process $W$ is a Brownian motion

**Note:** While elegant, this construction is less direct than the **Wiener measure** approach via Kolmogorov's extension theorem.

### Monte Carlo and Euler–Maruyama Discretization

Donsker's theorem justifies **Euler–Maruyama discretization** for SDEs.

Consider the SDE:

$$dX_t = \mu(X_t) \, dt + \sigma(X_t) \, dW_t$$

**Discretization.** With time step $\Delta t = T/n$:

$$X_{k+1} = X_k + \mu(X_k) \Delta t + \sigma(X_k) \sqrt{\Delta t} \, \xi_{k+1}$$

where $\xi_k \sim \mathcal{N}(0,1)$ (or any i.i.d. mean-zero, unit-variance sequence).

**Justification.** As $n \to \infty$ (i.e., $\Delta t \to 0$), the discrete approximation

$$\sum_{k=0}^{n-1} \sigma(X_k) \sqrt{\Delta t} \, \xi_{k+1} \approx \frac{1}{\sqrt{n}} \sum_{k=1}^n \sigma(X_k) \xi_k$$

converges (in an appropriate sense) to the stochastic integral

$$\int_0^T \sigma(X_s) \, dW_s$$

by Donsker's theorem and continuous mapping arguments.

## Final Synthesis

The development of Brownian motion theory follows a beautiful logical progression:

> **Wiener** constructed Brownian motion as a measure on path space.  
> **Kolmogorov** embedded it into a general, axiomatic theory of stochastic processes and explained its regularity.  
> **Donsker** showed that Brownian motion arises universally as the scaling limit of discrete random systems.  
> **Lévy** uncovered the deep structural and geometric properties of Brownian paths and placed Brownian motion within the larger class of Lévy processes.

Donsker's theorem is the keystone that explains **why** Brownian motion appears throughout mathematics, physics, and finance: it is not a special construction but the inevitable limit of any sufficiently random discrete process under appropriate scaling.

## Historical Notes

- **Donsker (1951, 1952):** Monroe D. Donsker proved the functional CLT for random walks, extending Wiener's 1923 construction of Brownian motion
- **Invariance:** The term "invariance principle" was popularized by Erdős and Kac, emphasizing the universality of the Gaussian limit
- **Skorokhod (1956):** Developed the Skorokhod metric and representation theorem, crucial for functional limit theorems
- **Billingsley (1968):** *Convergence of Probability Measures* systematized weak convergence theory in metric spaces

## Summary

Donsker's invariance principle establishes that:

1. **Scaled random walks converge to Brownian motion** in the strong sense of weak convergence in $C[0,T]$

2. The **limit is universal**: it depends only on mean and variance, not the specific distribution of $\{\xi_i\}$

3. **Continuous functionals** of the random walk converge to the same functionals of Brownian motion

4. This rigorously justifies:
   - Viewing Brownian motion as "continuous random walk"
   - Discretization schemes for SDEs
   - Physical models of diffusion

## Exercises

1. Let $\{\xi_i\}$ be i.i.d. with $\mathbb{E}[\xi_i] = 0$, $\mathbb{E}[\xi_i^2] = 1$, and define the scaled random walk $W^{(n)}(t) = \frac{1}{\sqrt{n}} S_{\lfloor nt \rfloor}$.

   (a) Verify that for fixed $t$, $W^{(n)}(t) \xrightarrow{d} \mathcal{N}(0, t)$ using the classical CLT.
   
   (b) For $0 < s < t$, show that $(W^{(n)}(s), W^{(n)}(t))$ converges in distribution to a bivariate Gaussian with the correct covariance structure.

2. (Continuous Mapping Theorem Application) Let $W^{(n)} \Rightarrow W$ in $C[0,1]$.

   (a) Show that $\sup_{t \in [0,1]} W^{(n)}(t) \xrightarrow{d} \sup_{t \in [0,1]} W(t)$.
   
   (b) Use the reflection principle to find the distribution of $\sup_{t \in [0,1]} W(t)$.

3. (Universality) Consider $\xi_i$ uniformly distributed on $\{-\sqrt{3}, 0, \sqrt{3}\}$ with probabilities $\{1/6, 2/3, 1/6\}$.

   (a) Verify that $\mathbb{E}[\xi_i] = 0$ and $\mathbb{E}[\xi_i^2] = 1$.
   
   (b) Explain why the scaled random walk still converges to standard Brownian motion.
   
   (c) Simulate paths and compare with the fair coin flip case.

## References

- Billingsley, P. (1968). *Convergence of Probability Measures*. Wiley.
- Donsker, M. D. (1951). An invariance principle for certain probability limit theorems. *Memoirs of the AMS*, 6.
- Durrett, R. (2019). *Probability: Theory and Examples*, 5th ed. Cambridge University Press.
- Kallenberg, O. (2002). *Foundations of Modern Probability*, 2nd ed. Springer.
- Karatzas, I., & Shreve, S. E. (1991). *Brownian Motion and Stochastic Calculus*, 2nd ed. Springer.
