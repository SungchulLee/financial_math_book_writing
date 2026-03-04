# Random Walk

## Introduction

Before introducing Brownian motion axiomatically, we begin with the discrete-time simple random walk. This serves three purposes:

1. It provides concrete intuition for the abstract properties of Brownian motion.
2. It historically motivated the development of continuous stochastic processes.
3. It motivates the rigorous justification of Brownian motion as a scaling limit via Donsker's invariance principle, proved in [Donsker's Theorem](donsker_theorem.md).

The simple random walk is a canonical example of a stochastic process, characterized by a discrete sequence of steps that evolve in an independent and identically distributed (i.i.d.) manner. It is a fundamental building block in probability theory, underpinning the analysis of diffusion phenomena, financial time series, statistical physics, and population dynamics.

---

## Notation

Throughout this section we use the following conventions consistently.

| Symbol | Meaning |
|---|---|
| $S_n$ | Position of the discrete random walk at time $n$ |
| $X_i$ or $\xi_i$ | The $i$-th step increment ($\pm 1$) |
| $S^{(n)}(t)$ | Scaled random walk (continuous-time embedding) |
| $W_t$ | Brownian motion (limiting process) |
| $p$ | Probability of a $+1$ step |

For the **general** walk we write $X_i$; for the **symmetric** case ($p = 1/2$) we use the special notation $\xi_i$ to signal that $\mathbb{E}[\xi_i] = 0$.

---

## Formal Definition

Let $\{S_n\}_{n \geq 0}$ be a discrete-time stochastic process defined recursively: for $n \geq 1$,

$$S_n = S_{n-1} + X_n$$

where $S_0 = 0$ and $\{X_n\}_{n \geq 1}$ is a sequence of **independent** random variables taking values in $\{-1, +1\}$ with

$$\mathbb{P}(X_n = +1) = p, \qquad \mathbb{P}(X_n = -1) = 1 - p, \qquad p \in (0,1).$$

The parameter $p$ governs the drift of the process.

**Equivalent summation form.** Since $S_0 = 0$, the position at time $n$ is simply the cumulative sum of all steps:

$$S_n = \sum_{i=1}^n X_i$$

This is the form we use most often in computations.

---

## Symmetric Random Walk

![Simple Random Walk](../brownian_motion/figures/simple_random_walk.png)

A **symmetric random walk** corresponds to $p = 1/2$, so that $+1$ and $-1$ steps are equally likely. Unless stated otherwise, the remaining pages in this section focus on the symmetric case.

In the symmetric case we write $X_i = \xi_i$, where

$$\mathbb{P}(\xi_i = +1) = \mathbb{P}(\xi_i = -1) = \frac{1}{2}$$

and the walk is

$$S_n = \sum_{i=1}^n \xi_i, \qquad S_0 = 0.$$

**Interpretations.** At each step the process moves up or down by 1 with equal probability. This can model:

- A gambler's cumulative net winnings in a fair coin-flip game.
- Displacement of a particle undergoing random collisions (Einstein, 1905).
- Price changes in a discrete-time market model (Bachelier, 1900).

---

## Asymmetric Random Walk

For $p \neq 1/2$, the walk has a **nonzero drift** $\mu := 2p - 1$:

- $p > 1/2$: positive drift — the walk tends upward.
- $p < 1/2$: negative drift — the walk tends downward.

As we show in [Moments of Random Walk](moments_of_random_walk.md), the mean position grows linearly: $\mathbb{E}[S_n] = n(2p-1)$. The asymmetric walk is also **transient** in $d = 1$: any nonzero drift causes the walk to drift to $\pm\infty$ and visit each state only finitely many times (see [Recurrence and Transience](recurrence_and_transience.md)).

---

## References

- Bachelier, L. (1900). *Théorie de la spéculation*. Annales scientifiques de l'École normale supérieure.
- Einstein, A. (1905). Über die von der molekularkinetischen Theorie der Wärme geforderte Bewegung. *Annalen der Physik*.
- Feller, W. (1968). *An Introduction to Probability Theory and Its Applications*, Vol. 1, 3rd ed. Wiley.
- Lawler, G. F., & Limic, V. (2010). *Random Walk: A Modern Introduction*. Cambridge University Press.
