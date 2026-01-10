# Random Walk Foundations

## Introduction

Before introducing Brownian motion axiomatically, we begin with the discrete-time simple random walk. This serves three purposes: 

(1) It provides concrete intuition for the abstract properties of Brownian motion. 

(2) It historically motivated the development of continuous stochastic processes.

(3) It rigorously justifies Brownian motion as a scaling limit via Donsker's invariance principle.

The simple random walk is a canonical example of a stochastic process, characterized by a discrete sequence of steps that evolve in an independent and identically distributed (i.i.d.) manner. This process serves as a fundamental building block in probability theory, underpinning the analysis of diffusion phenomena, financial time series, statistical physics, and population dynamics.

## Simple Random Walk

### Formal Definition

Let $\{S_n\}_{n \geq 0}$ be a discrete-time stochastic process defined recursively as: for $n \geq 1$

$$S_n = S_{n-1} + X_n$$


where $S_0 = 0$ and $\{X_n\}$ is a sequence of independent Bernoulli-distributed random variables such that:

$$\mathbb{P}(X_n = +1) = p, \quad \mathbb{P}(X_n = -1) = 1 - p$$



The parameter $p$ governs the drift of the process, distinguishing between symmetric and asymmetric random walks.

**Equivalent Formulation:** We can write, with $S_0 = 0$

$$S_n = \sum_{i=1}^n X_i$$



### Symmetric vs. Asymmetric Random Walks

#### Symmetric Random Walk

A **symmetric random walk** corresponds to $p = 1/2$, ensuring an equal probability of moving in either direction. For the remainder of this section, unless otherwise specified, we focus on this symmetric case.

**Notation:** For the symmetric case, we denote $X_i = \xi_i$ where

$$\mathbb{P}(\xi_i = 1) = \mathbb{P}(\xi_i = -1) = \frac{1}{2}$$



The **simple symmetric random walk** is the discrete-time stochastic process, with $S_0 = 0$:

$$S_n = \sum_{i=1}^n \xi_i$$



**Interpretation:** At each time step $n$, the process moves up (+1) or down (-1) with equal probability. This can represent:

- A gambler's cumulative winnings in a fair coin-flipping game
- Displacement of a particle undergoing random collisions  
- Price changes in a discrete-time market model (Bachelier, 1900)

#### Asymmetric Random Walk

For $p \neq 1/2$, the random walk exhibits directional bias, resulting in a nonzero drift. Specifically:

- For $p > 1/2$: positive drift (upward bias)

- For $p < 1/2$: negative drift (downward bias)

The recurrence behavior differs markedly from the symmetric case, particularly in higher-dimensional settings.

## Fundamental Properties

### Expectation and Variance

The first two moments of $S_n$ provide key insights into its asymptotic behavior.

**Proposition 1.1.1** (Moments of Random Walk)

For the general random walk $S_n$ with parameter $p$:

1. $\mathbb{E}[S_n] = n(2p - 1)$

2. $\text{Var}(S_n) = 4np(1 - p)$

For the symmetric random walk ($p = 1/2$):

1. $\mathbb{E}[S_n] = 0$

2. $\text{Var}(S_n) = n$

3. $\mathbb{E}[S_n^4] = 3n^2 - 2n$

**Proof:**

*General case:*

(1) By independence and $\mathbb{E}[X_i] = p \cdot 1 + (1-p) \cdot (-1) = 2p - 1$:

$$\mathbb{E}[S_n] = \sum_{i=1}^n \mathbb{E}[X_i] = n(2p - 1)$$



When $p = 1/2$, this gives $\mathbb{E}[S_n] = 0$, reflecting a lack of directional preference.

(2) Since $X_i^2 = 1$ almost surely:

$$\mathbb{E}[X_i^2] = 1, \quad \text{Var}(X_i) = 1 - (2p-1)^2 = 4p(1-p)$$



By independence:

$$\text{Var}(S_n) = \sum_{i=1}^n \text{Var}(X_i) = 4np(1 - p)$$



For the symmetric case, this simplifies to $\text{Var}(S_n) = n$, reinforcing the diffusive nature of the process.

*Symmetric case - fourth moment:*

(3) For $p = 1/2$, we have $\xi_i \in \{-1, 1\}$ with $\xi_i^2 = 1$ and $\xi_i^4 = 1$. Expanding:

$$S_n^4 = \left(\sum_{i=1}^n \xi_i\right)^4 = \sum_{i=1}^n \xi_i^4 + 6\sum_{i<j}\xi_i^2\xi_j^2 + \text{(cross terms)}$$



Since $\mathbb{E}[\xi_i\xi_j] = 0$ for $i \neq j$:

$$\mathbb{E}[S_n^4] = n + 6\binom{n}{2} = n + 3n(n-1) = 3n^2 - 2n \quad \square$$



### Quadratic Variation

A crucial property that distinguishes random walks from smooth paths is their quadratic variation.

**Definition 1.1.2** (Discrete Quadratic Variation)

The quadratic variation of $S_n$ over $[0,n]$ is

$$[S]_n := \sum_{i=1}^n (S_i - S_{i-1})^2 = \sum_{i=1}^n X_i^2$$



**Proposition 1.1.3**

For any random walk (symmetric or asymmetric), $[S]_n = n$ almost surely.

**Proof:**

Since $X_i \in \{-1, 1\}$, we have $X_i^2 = 1$ for all $i$. Therefore:

$$[S]_n = \sum_{i=1}^n X_i^2 = n \quad \square$$



**Remark:** This deterministic quadratic variation is fundamental. It shows that the "accumulated squared displacement" grows linearly with time, not quadratically as for smooth functions. This property persists in the continuous limit and underlies Itô's lemma.

### Recurrence and Transience

The probability of return to the origin depends crucially on dimensionality. These results, first established by Pólya, underscore the role of dimensionality in determining long-term behavior.

**Theorem 1.1.4** (Pólya's Recurrence Theorem)

For a symmetric random walk in $\mathbb{Z}^d$:

- **$d = 1$**: The walk is **recurrent**. The probability of returning to the origin is 1.

- **$d = 2$**: The walk is **recurrent**. The expected number of returns to the origin is infinite.

- **$d \geq 3$**: The walk is **transient**. There is a positive probability of never returning to the origin.

**Proof sketch for $d=1$:**

The probability of first return at time $2n$ is given by

$$f_{2n} = \frac{1}{2n-1}\binom{2n}{n}\left(\frac{1}{2}\right)^{2n}$$



Using Stirling's approximation, $f_{2n} \sim \frac{1}{\sqrt{\pi n}}$, which is not summable. However, the total return probability

$$\sum_{n=1}^\infty f_{2n} = 1$$


proving recurrence. $\square$

**Remark:** The distinction between recurrence and transience has profound implications in statistical mechanics, polymer physics, and random graph theory. For asymmetric walks ($p \neq 1/2$), even in one dimension, the walk can be transient if the drift is sufficiently strong.

## Continuous-Time Interpolation

To connect discrete random walks to continuous-time processes, we introduce appropriate scaling.

### Scaled Random Walk

For a fixed time horizon $T > 0$ and discretization parameter $n \in \mathbb{N}$, define the **scaled random walk** by, for $t \in [0, T]$:

$$S^{(n)}(t) := \frac{1}{\sqrt{n}} S_{[nt]}$$


where $[nt]$ denotes the integer part (floor) of $nt$.

**Key Scalings:**

- **Time scaling:** $n$ steps occur in time interval $[0,T]$, so $\Delta t = T/n$
- **Space scaling:** Factor $1/\sqrt{n}$ ensures variance remains $O(1)$

**Rationale:** For a smooth function $f(t)$ with $f(0) = 0$:

$$f(t) \sim f'(0) \cdot t + \frac{1}{2}f''(0) \cdot t^2 + \cdots$$



For the random walk, there is no "derivative," but the variance grows linearly:

$$\text{Var}(S_n) = n \implies \text{Var}\left(\frac{S_n}{\sqrt{n}}\right) = 1$$



Thus, the scaling $1/\sqrt{n}$ is the correct normalization to obtain a non-trivial limit.

### Piecewise Linear Interpolation

For technical reasons (to obtain processes in $C[0,T]$), we use piecewise linear interpolation:

$$W^{(n)}(t) := \frac{1}{\sqrt{n}} S_{[nt]} + (nt - [nt]) \cdot \frac{1}{\sqrt{n}} \xi_{[nt]+1}$$



This defines $W^{(n)} \in C[0,T]$ for each $n$, where $C[0,T]$ is the space of continuous functions on $[0,T]$.

**Geometric Interpretation:** Between integer multiples of $1/n$, we linearly interpolate using the next random increment $\xi_{[nt]+1}$.

### Asymptotic Properties

**Proposition 1.1.5** (Convergence of Moments)

For fixed $t \in [0,T]$ and the symmetric random walk:

1. $\mathbb{E}[S^{(n)}(t)] = 0$
2. $\text{Var}(S^{(n)}(t)) \to t$ as $n \to \infty$
3. For $s < t$: $\text{Cov}(S^{(n)}(s), S^{(n)}(t)) \to \min(s,t)$ as $n \to \infty$

**Proof:**

(1) Clear from linearity of expectation.

(2) We have $[nt] = nt - \{nt\}$ where $0 \leq \{nt\} < 1$. Thus:

$$\text{Var}(S^{(n)}(t)) = \frac{1}{n}\text{Var}(S_{[nt]}) = \frac{[nt]}{n} = t - \frac{\{nt\}}{n} \to t$$



(3) For $s < t$:

$$\begin{array}{lll}
\text{Cov}(S^{(n)}(s), S^{(n)}(t)) 
&=&\displaystyle \frac{1}{n}\text{Cov}(S_{[ns]}, S_{[nt]}) \\
&=&\displaystyle \frac{1}{n} \min([ns], [nt])\\
&=&\displaystyle \frac{[ns]}{n} \to s = \min(s,t) \quad \square
\end{array}$$



## Central Limit Theorem

The CLT for i.i.d. sequences is the engine driving convergence to Brownian motion.

**Theorem 1.1.6** (Classical CLT)

Let $\{\xi_i\}$ be i.i.d. with $\mathbb{E}[\xi_i] = 0$ and $\mathbb{E}[\xi_i^2] = \sigma^2 < \infty$. Then:

$$\frac{1}{\sqrt{n}} \sum_{i=1}^n \xi_i \xrightarrow{d} \mathcal{N}(0, \sigma^2)$$


as $n \to \infty$.

For the simple random walk with $\sigma^2 = 1$:

$$\frac{S_n}{\sqrt{n}} \xrightarrow{d} \mathcal{N}(0, 1)$$



This implies that for fixed $t$, $S^{(n)}(t) \xrightarrow{d} \mathcal{N}(0, t)$.

**However:** Finite-dimensional convergence is insufficient! We need **functional convergence** in the space $C[0,T]$.

### Scaling Limit and Convergence to Brownian Motion

A fundamental result in probability theory, **Donsker's Invariance Principle** (proven rigorously in the next section), states that as the number of steps grows, the properly rescaled simple random walk converges in distribution to a standard Wiener process:

$$\frac{S_{[nt]}}{\sqrt{n}} \Rightarrow W_t$$


where $W_t$ denotes Brownian motion. This limit theorem establishes a bridge between discrete and continuous-time stochastic processes and has far-reaching implications in fields such as statistical mechanics and financial modeling.

## Structural Properties

### Independent Increments

A property that transfers cleanly from discrete to continuous time.

**Proposition 1.1.7** (Independent Increments) 

For $0 \leq t_1 < t_2 < \cdots < t_k \leq T$, the increments

$$S^{(n)}(t_2) - S^{(n)}(t_1), \, S^{(n)}(t_3) - S^{(n)}(t_2), \, \ldots, \, S^{(n)}(t_k) - S^{(n)}(t_{k-1})$$


are independent for each $n$.

**Proof:** 

Each increment $S^{(n)}(t_{i+1}) - S^{(n)}(t_i)$ depends on disjoint sets of $\{\xi_j\}$ variables, which are independent by construction. $\square$

**Remark:** This property is preserved in the limit, making Brownian motion a **Lévy process** (stochastic process with stationary independent increments).

### Markov Property

**Proposition 1.1.8**

The simple random walk $\{S_n\}$ is a Markov chain:

$$\mathbb{P}(S_{n+1} = j \mid S_n = i, S_{n-1} = i_{n-1}, \ldots, S_0 = i_0) = \mathbb{P}(S_{n+1} = j \mid S_n = i)$$



**Proof:**

Since $S_{n+1} = S_n + \xi_{n+1}$ and $\xi_{n+1}$ is independent of $\mathcal{F}_n = \sigma(\xi_1, \ldots, \xi_n)$:

$$\mathbb{P}(S_{n+1} \in A \mid \mathcal{F}_n) = \mathbb{P}(S_n + \xi_{n+1} \in A \mid S_n)$$


which depends only on $S_n$, not the entire history. $\square$

The scaled version $S^{(n)}(t)$ inherits this Markov property, which persists in the Brownian limit.

## Path Properties

### Non-Differentiability Heuristic

**Observation:** The random walk has "corners" at every integer time $n$. The slope between $n-1$ and $n$ is $\xi_n \in \{-1, 1\}$, which changes randomly.

For the scaled version, consider the difference quotient:

$$\frac{S^{(n)}(t + \Delta t) - S^{(n)}(t)}{\Delta t} \approx \frac{\xi_{[nt]+1}}{\sqrt{n} \cdot (1/n)} = \sqrt{n} \cdot \xi_{[nt]+1} \sim \sqrt{n} \cdot O(1)$$


which diverges as $n \to \infty$.

**Heuristic Conclusion:** In the limit, Brownian motion should be continuous but nowhere differentiable.

**Rigorous Statement:** Brownian motion is almost surely continuous everywhere but differentiable nowhere. This was proven by Wiener using Fourier analysis.

### Quadratic Variation in Continuous Time

For the scaled random walk:

$$[S^{(n)}]_t = \sum_{i=1}^{[nt]} (S^{(n)}(i/n) - S^{(n)}((i-1)/n))^2 = \frac{1}{n} \sum_{i=1}^{[nt]} \xi_i^2 = \frac{[nt]}{n} \to t$$



This suggests that in the limit, the **quadratic variation equals $t$**, not $t^2$ as for smooth functions.

**Key Insight:** If $f(t)$ is differentiable with derivative $f'(t)$, then

$$\sum_{i=0}^{n-1} (f(t_{i+1}) - f(t_i))^2 \approx \sum_{i=0}^{n-1} (f'(t_i))^2 (\Delta t)^2 = O((\Delta t)^2) \to 0$$



But for Brownian motion:

$$\langle W \rangle_t = t \quad \text{(non-zero quadratic variation)}$$



This is the foundation for Itô's formula: when we compute $(dW_t)^2$, we get $dt$, not 0.

## Applications and Theoretical Significance

1. **Gambler's Ruin Problem**: Models the probability of a gambler going bankrupt when repeatedly wagering in a fair or biased game.

2. **Financial Market Modeling**: While simplistic, the random walk hypothesis serves as an idealized framework for asset price movements, forming the foundation for more sophisticated models such as geometric Brownian motion.

3. **Diffusion Processes**: The motion of particles in a fluid (Brownian motion) is well-approximated by discrete random walk models.

4. **Population Genetics**: Used in Wright-Fisher and Moran models to describe allele frequency fluctuations due to genetic drift.

5. **Markov Chains and Reinforcement Learning**: Random walks serve as prototypical examples of Markovian state transitions, with applications in dynamic programming and artificial intelligence.

## Connection to Finance

### Historical Note

Louis Bachelier's 1900 PhD thesis *Théorie de la Spéculation* used random walks to model stock prices, predating Einstein's 1905 work on physical Brownian motion. Bachelier's model:

$$S_n = S_0 + \sum_{i=1}^n \xi_i$$


where $S_n$ represents the price at time $n$.

### Scaling to Continuous Time

The continuous limit

$$S(t) = S_0 + \sigma W_t$$


gives an **arithmetic Brownian motion**, which can be negative (problematic for stock prices).

The **geometric Brownian motion** (studied in later chapters)

$$S(t) = S_0 \exp\left(\mu t + \sigma W_t - \frac{\sigma^2 t}{2}\right)$$


remains positive and is the foundation of Black-Scholes theory.

## Summary

The simple random walk provides:

1. **Intuitive picture** of random motion in discrete time
2. **Concrete calculations** for mean, variance, quadratic variation  
3. **Independent increments** structure
4. **Markov property**
5. **Recurrence vs. transience** depending on dimension
6. **Heuristic for non-differentiability** and non-zero quadratic variation
7. **Motivation for scaling limits** via CLT

The natural question: **Can we make the limiting procedure rigorous?** Yes—via **Donsker's invariance principle**, which we prove in the next section.

For computational illustrations of these concepts, see the accompanying section on **Random Walk Simulations**.

## References

- Bachelier, L. (1900). *Théorie de la spéculation*. Annales scientifiques de l'École normale supérieure.
- Einstein, A. (1905). *Über die von der molekularkinetischen Theorie der Wärme geforderte Bewegung von in ruhenden Flüssigkeiten suspendierten Teilchen*. Annalen der Physik.
- Feller, W. (1968). *An Introduction to Probability Theory and Its Applications*, Vol. 1, 3rd ed.
- Lawler, G. F., & Limic, V. (2010). *Random Walk: A Modern Introduction*. Cambridge University Press.
- Pólya, G. (1921). *Über eine Aufgabe der Wahrscheinlichkeitsrechnung betreffend die Irrfahrt im Straßennetz*. Mathematische Annalen, 84(1-2), 149-160.
