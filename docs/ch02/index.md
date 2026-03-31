# Chapter 2: Stochastic Processes

This chapter builds the probabilistic engine that powers continuous-time finance. Starting from discrete random walks and their scaling limits, we construct Brownian motion, study its remarkable path properties, and develop the martingale theory that underpins fair pricing. These tools---random walks, Brownian motion, filtrations, martingales, and stopping times---form the foundation for everything that follows.

## Chapter Roadmap

| Section | Topics |
|---------|--------|
| 2.1 Simple Random Walk | Symmetric walk, moments, moment generating function, martingale property, recurrence, scaling limit, Donsker's theorem |
| 2.2 Brownian Motion | Definition, moments, scaling and time change, Holder continuity, quadratic variation, reflection principle, first passage times |
| 2.3 Martingale Theory | Filtrations, conditional expectation, adapted processes, martingales, stopping times, Doob's inequalities, convergence, Doob--Meyer decomposition, uniform integrability |

## Key Topics

### Random Walks and Brownian Motion

Random walks provide the most natural discrete model for asset prices evolving under uncertainty. Understanding their large-scale behavior reveals why Brownian motion, rather than some other continuous process, is the canonical building block of stochastic finance.

The simple symmetric random walk $S_n = \sum_{i=1}^n X_i$ with $\mathbb{P}(X_i = \pm 1) = 1/2$ serves as the discrete precursor to Brownian motion. The rescaled walk $W^{(n)}_t = n^{-1/2} S_{\lfloor nt \rfloor}$ converges in distribution to standard Brownian motion as $n \to \infty$. This is the content of Donsker's theorem: weak convergence holds in $C[0,T]$ equipped with the sup-norm topology.

Standard Brownian motion is the unique (in law) process satisfying:

1. **Initial condition.** $W_0 = 0$.
2. **Continuous paths.** $t \mapsto W_t$ is continuous almost surely.
3. **Independent increments.** For $0 \leq t_1 < t_2 < \cdots < t_n$, the increments $W_{t_2} - W_{t_1}, \ldots, W_{t_n} - W_{t_{n-1}}$ are independent.
4. **Gaussian increments.** $W_t - W_s \sim \mathcal{N}(0, t - s)$ for $0 \leq s < t$.

### Path Properties

The fine structure of Brownian paths explains why classical calculus fails for stochastic processes and motivates the need for Ito calculus in later chapters.

Brownian paths are continuous but nowhere differentiable (a.s.). They are Holder continuous of order $\alpha < 1/2$ but not of order $\alpha = 1/2$, quantifying their roughness precisely.

The quadratic variation $\langle W \rangle_t = t$ (a.s.) is the hallmark property that distinguishes stochastic from classical calculus: partitions of a Brownian path accumulate squared increments at a deterministic, linear rate.

### Martingale Theory

Martingales formalize the notion of a fair game---a process whose future expected value, given all available information, equals its current value. This concept is central to pricing: under the risk-neutral measure, discounted asset prices are martingales.

A martingale satisfies $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ for $s \leq t$. The theory provides powerful tools organized around two themes:

- **Controlling extremes and convergence**: Doob's maximal inequality bounds the probability that a martingale exceeds a threshold, and the martingale convergence theorem guarantees almost-sure limits under boundedness conditions.
- **Structural decomposition**: The optional sampling theorem extends the martingale property to stopping times under appropriate integrability, and the Doob--Meyer decomposition uniquely splits a submartingale into a martingale plus a predictable increasing process.

!!! note "Role in the Book"
    Brownian motion and martingale theory developed here are the essential prerequisites for stochastic calculus (Chapter 3), Girsanov's theorem (Chapter 4), and the Feynman--Kac connection (Chapter 5). The reader should be comfortable with the probability foundations from Chapter 1, particularly conditional expectation and filtrations.
