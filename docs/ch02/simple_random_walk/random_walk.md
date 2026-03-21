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
| $\xi_i$ | The $i$-th step increment ($\pm 1$); used for both general and symmetric cases |
| $S^{(n)}(t)$ | Scaled random walk (continuous-time embedding) |
| $W^{(n)}(t)$ | Piecewise-linear interpolation of the scaled walk |
| $W_t$ | Brownian motion (limiting process) |
| $p$ | Probability of a $+1$ step |

---

## Formal Definition

Let $\{S_n\}_{n \geq 0}$ be a discrete-time stochastic process defined recursively: for $n \geq 1$,

$$S_n = S_{n-1} + \xi_n$$

where $S_0 = 0$ and $\{\xi_n\}_{n \geq 1}$ is a sequence of **independent** random variables taking values in $\{-1, +1\}$ with

$$\mathbb{P}(\xi_n = +1) = p, \qquad \mathbb{P}(\xi_n = -1) = 1 - p, \qquad p \in (0,1)$$

The parameter $p$ governs the drift of the process.

**Equivalent summation form.** Since $S_0 = 0$, the position at time $n$ is simply the cumulative sum of all steps:

$$S_n = \sum_{i=1}^n \xi_i$$

This is the form used most often in computations.

---

## Interpretations

At each step the process moves up or down by 1. The walk can model:

- A gambler's cumulative net winnings in a coin-flip game (fair if $p = 1/2$).
- Displacement of a particle undergoing random collisions (Einstein, 1905).
- Price changes in a discrete-time market model (Bachelier, 1900).

These interpretations apply for any $p \in (0,1)$; the parameter $p$ controls whether the drift is upward, downward, or absent.

---

## Symmetric Random Walk

A **symmetric random walk** corresponds to $p = 1/2$, so that $+1$ and $-1$ steps are equally likely:

$$\mathbb{P}(\xi_i = +1) = \mathbb{P}(\xi_i = -1) = \frac{1}{2}$$

Unless stated otherwise, the remaining pages in this section focus on the symmetric case.

![Simple Random Walk — a single path of 200 steps starting at 0, oscillating around the horizontal axis with spread growing like $\sqrt{n}$.](figures/simple_random_walk.png)

---

## Asymmetric Random Walk

For $p \neq 1/2$, the walk has a **nonzero drift** $\mu := 2p - 1$:

- $p > 1/2$: positive drift — the walk tends upward.
- $p < 1/2$: negative drift — the walk tends downward.

As shown in [Moments of Random Walk](moments_of_random_walk.md), the mean position grows linearly: $\mathbb{E}[S_n] = n(2p-1)$. The asymmetric walk is also **transient** in $d = 1$: any nonzero drift causes the walk to drift to $\pm\infty$ and visit each state only finitely many times (see [Recurrence and Transience](recurrence_and_transience.md)).

---

## Proposition Inventory

The following propositions are developed on the subpages of this section.

**Discrete walk properties**

| Label | Statement | Page |
|---|---|---|
| Prop 1.1.1 | Moments: $\mathbb{E}[S_n]$, $\text{Var}(S_n)$, $\mathbb{E}[S_n^4]$ | [Moments](moments_of_random_walk.md) |
| Prop 1.1.2 | MGF: $\mathbb{E}[e^{\lambda S_n}] = (\cosh\lambda)^n$ | [MGF](mgf_of_random_walk.md) |
| Prop 1.1.3 | Martingale property of $\{S_n\}$ | [Martingale Property](martingale_property.md) |
| Prop 1.1.4 | Quadratic martingale $\{S_n^2 - n\}$ | [Martingale Property](martingale_property.md) |
| Prop 1.1.5 | Quadratic variation $[S]_n = n$ a.s. | [Martingale Property](martingale_property.md) |
| Prop 1.1.6 | Markov property | below |
| Thm 1.1.7 | Pólya recurrence theorem | [Recurrence](recurrence_and_transience.md) |

**Scaling and limit theorems**

| Label | Statement | Page |
|---|---|---|
| Prop 1.1.8 | Asymptotic moments and covariance: $\mathbb{E}[S^{(n)}(t)]\to 0$, $\text{Var}\to t$, $\text{Cov}\to\min(s,t)$ | [Scaling Limit](scaling_limit.md) |
| Prop 1.1.9 | Independent increments of $S^{(n)}$ at dyadic times | [Scaling Limit](scaling_limit.md) |
| Thm 1.1.10 | CLT: $S_n/\sqrt{n}\xrightarrow{d}\mathcal{N}(0,1)$ | [MGF](mgf_of_random_walk.md) |
| Thm 1.1.11 | Donsker's invariance principle: $W^{(n)}\Rightarrow W$ in $C[0,T]$ | [Donsker's Theorem](donsker_theorem.md) |

---

## Markov Property

**Proposition 1.1.6** (Markov Property)

$\{S_n\}$ is a Markov chain with respect to its natural filtration $\mathcal{F}_n = \sigma(\xi_1,\ldots,\xi_n)$:

$$\mathbb{P}(S_{n+1} = j \mid S_n = i,\, S_{n-1},\ldots, S_0) = \mathbb{P}(S_{n+1} = j \mid S_n = i)$$

**Proof.** $S_{n+1} = S_n + \xi_{n+1}$ and $\xi_{n+1}$ is independent of $\mathcal{F}_n$, so the transition probability $\mathbb{P}(S_{n+1} = j \mid S_n = i) = \mathbb{P}(\xi_{n+1} = j - i)$ depends only on the current position $S_n = i$. $\square$

The scaled process $S^{(n)}(t)$ inherits this property at dyadic times, which persists in the Brownian limit.

---

## References

- Bachelier, L. (1900). *Théorie de la spéculation*. Annales scientifiques de l'École normale supérieure.
- Einstein, A. (1905). Über die von der molekularkinetischen Theorie der Wärme geforderte Bewegung. *Annalen der Physik*.
- Feller, W. (1968). *An Introduction to Probability Theory and Its Applications*, Vol. 1, 3rd ed. Wiley.
- Lawler, G. F., & Limic, V. (2010). *Random Walk: A Modern Introduction*. Cambridge University Press.
