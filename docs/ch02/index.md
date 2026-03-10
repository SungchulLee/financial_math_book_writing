# Chapter 2: Stochastic Processes

!!! warning "Incomplete page"
    This is a chapter index page and does not follow the five-section structure.

This chapter develops the probabilistic machinery underlying continuous-time finance: random walks, Brownian motion, filtrations, martingales, and stopping times.

## Key Topics

### Random Walks and Brownian Motion

The simple symmetric random walk $S_n = \sum_{i=1}^n X_i$ with $\mathbb{P}(X_i = \pm 1) = 1/2$ serves as the discrete precursor to Brownian motion. Donsker's theorem establishes that the rescaled walk $W^{(n)}_t = n^{-1/2} S_{\lfloor nt \rfloor}$ converges weakly in $C[0,T]$ to standard Brownian motion, which is the unique process with continuous paths, independent Gaussian increments, and $W_0 = 0$.

### Path Properties

Brownian paths are continuous but nowhere differentiable (a.s.), and Holder continuous of order $\alpha < 1/2$ but not $\alpha = 1/2$. The quadratic variation $\langle W \rangle_t = t$ is the hallmark property that distinguishes stochastic from classical calculus.

### Martingale Theory

A martingale satisfies $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ for $s \leq t$. Key results include Doob's maximal inequality, the optional sampling theorem, martingale convergence, and the Doob-Meyer decomposition of submartingales into martingale plus predictable increasing parts.

!!! note "Role in the Book"
    Brownian motion and martingale theory developed here are the essential prerequisites for stochastic calculus (Chapter 3), Girsanov's theorem (Chapter 4), and the Feynman-Kac connection (Chapter 5).
