# Brownian Motion

## Introduction

Having established the discrete random walk and its scaling limit via Donsker's theorem, we now define **Brownian motion** axiomatically. Brownian motion (also called the **Wiener process**) is the canonical continuous-time random motion that serves as the foundation for:

- Stochastic calculus and stochastic differential equations
- Mathematical finance (Black-Scholes theory)
- Statistical physics (diffusion processes)
- Filtering theory and signal processing

A standard Brownian motion is any stochastic process with continuous paths, independent increments, and stationary Gaussian increments whose variance equals the time difference, starting from zero. Any two such processes are equal in law (up to modification), making Brownian motion the fundamental building block for continuous-time stochastic modeling. The precise axiomatic definition is given below.

## Intuitive Construction

Before giving the formal definition, we develop intuition through discrete approximations that can be performed "by hand."

### Construction via Standard Normal Increments

Consider the following discrete-to-continuous procedure:

| Quantity | Notation |
|----------|----------|
| Number of ticks per year | $n$ |
| Standard normal increment at tick $k$ | $X_k$ |
| Number of ticks between $0$ and $t$ | $\lfloor nt \rfloor$ |
| Cumulative increments up to time $t$ | $\displaystyle\sum_{k=1}^{\lfloor nt \rfloor}X_k$ |
| **Normalized cumulative sum** | $\displaystyle B_t= \frac{1}{\sqrt{n}}\sum_{k=1}^{\lfloor nt \rfloor}X_k$ |

where $X_k \stackrel{\text{iid}}{\sim} \mathcal{N}(0,1)$.

**Key observation:** As $n \to \infty$, by the central limit theorem (more precisely, Donsker's theorem), $B_t$ converges to Brownian motion.

## Axiomatic Definition

**Definition 1.3.1** (Standard Brownian Motion)

A **standard Brownian motion** $\{W_t\}_{t \ge 0}$ on a probability space $(\Omega,\mathcal{F},\mathbb{P})$ is a stochastic process satisfying:

**(i) Initial condition:**

$$W_0 = 0 \quad \text{almost surely}$$

**(ii) Independent increments:** For $0 \le t_0 < t_1 < \cdots < t_n$, the increments

$$W_{t_1}-W_{t_0},\quad W_{t_2}-W_{t_1},\quad \ldots,\quad W_{t_n}-W_{t_{n-1}}$$

are independent random variables.

**(iii) Gaussian stationary increments:** For $0 \le s < t$,

$$W_t - W_s \sim \mathcal{N}(0,t-s)$$

**(iv) Continuity of paths:** The map $t \mapsto W_t(\omega)$ is continuous for almost every $\omega \in \Omega$.

## Finite-Dimensional Distributions

For any $0 \le t_1 < t_2 < \cdots < t_n$, the random vector $(W_{t_1}, \ldots, W_{t_n})$ is multivariate Gaussian with mean zero and covariance $\mathbb{E}[W_{t_i} W_{t_j}] = \min(t_i, t_j)$.

## Covariance Structure

The following formula is the most important single fact about the second-order structure of Brownian motion.

**Theorem 1.3.4** (Covariance Formula)

For all $s,t \ge 0$:

$$\boxed{\mathbb{E}[W_s W_t] = \min(s,t)}$$

**Proof:**

Without loss of generality, assume $s \le t$. Since Brownian increments are independent and centered, write $W_t = W_s + (W_t - W_s)$. Because $W_s$ and $W_t - W_s$ are independent and the increment has mean zero,

$$\mathbb{E}[W_s(W_t - W_s)] = 0$$

Hence $\mathbb{E}[W_s W_t] = \mathbb{E}[W_s^2] = s = \min(s,t)$. $\square$

Although increments are independent, the levels $W_s$ and $W_t$ remain correlated for all $s, t$.

## Scaling Property

Brownian motion is statistically self-similar: $W_{ct} \overset{d}{=} \sqrt{c}\,W_t$ for any $c > 0$, with Hurst exponent $H = 1/2$. The full development — including time changes and the Dambis–Dubins–Schwarz theorem — is in [Scaling and Time Change](scaling_and_time_change.md).

## Martingale Property

With respect to the natural filtration $\mathcal{F}_t = \sigma(W_s : s \le t)$:

$$\boxed{\mathbb{E}[W_t \mid \mathcal{F}_s] = W_s} \qquad \boxed{W_t^2 - t \text{ is a martingale}}$$

## Path Regularity

Because increments scale like $\sqrt{\Delta t}$, Brownian paths are continuous but nowhere differentiable, with infinite total variation. Classical calculus fails on these paths, motivating Itô calculus. The full treatment — including Hölder continuity for $\alpha < 1/2$ and Lévy's modulus of continuity — is in [Hölder Continuity and Non-Differentiability](holder_continuity_and_non_differentiability.md).

## Quadratic Variation

Despite infinite total variation, the squared increments of Brownian motion accumulate to the elapsed time: $[W]_T = T$, written differentially as $(dW_t)^2 = dt$. This identity is the structural replacement for derivatives and the foundation of Itô calculus. Full treatment in [Quadratic Variation of Brownian Motion](quadratic_variation_of_brownian_motion.md).

## Summary

- $W_0 = 0$, continuous paths
- independent Gaussian increments: $W_t - W_s \sim \mathcal{N}(0, t-s)$
- $\mathbb{E}[W_s W_t] = \min(s, t)$
- $[W]_t = t$
- martingale structure: $W_t$ and $W_t^2 - t$ are martingales

## References

- Billingsley, P. (1995). *Probability and Measure*, 3rd ed. Wiley.
- Karatzas, I., & Shreve, S. E. (1991). *Brownian Motion and Stochastic Calculus*, 2nd ed. Springer.
- Kallenberg, O. (2002). *Foundations of Modern Probability*, 2nd ed. Springer.
- Mörters, P., & Peres, Y. (2010). *Brownian Motion*. Cambridge University Press.
- Revuz, D., & Yor, M. (1999). *Continuous Martingales and Brownian Motion*, 3rd ed. Springer.
- Glasserman, P. (2003). *Monte Carlo Methods in Financial Engineering*. Springer.
- Kloeden, P. E., & Platen, E. (1992). *Numerical Solution of Stochastic Differential Equations*. Springer.

## Exercises

**Exercise 1.**
Show that $\mathbb{E}[W_t] = 0$ and $\text{Var}(W_t) = t$ directly from the axiomatic definition.

??? success "Solution to Exercise 1"
    From the axiomatic definition, $W_t - W_0 \sim \mathcal{N}(0, t - 0) = \mathcal{N}(0, t)$ (property (iii)), and $W_0 = 0$ a.s. (property (i)). Therefore $W_t \sim \mathcal{N}(0, t)$, which gives:

    $$
    \mathbb{E}[W_t] = 0, \quad \text{Var}(W_t) = \mathbb{E}[W_t^2] - (\mathbb{E}[W_t])^2 = t - 0 = t
    $$

---

**Exercise 2.**
Compute $\mathbb{E}[W_s W_t]$ for $0 \le s \le t$ using the independent increments property.

??? success "Solution to Exercise 2"
    Assume $0 \le s \le t$. Write $W_t = W_s + (W_t - W_s)$, where $W_t - W_s$ is independent of $W_s$ (by property (ii), since $W_s = W_s - W_0$ and $W_t - W_s$ are increments over disjoint intervals).

    $$
    \mathbb{E}[W_s W_t] = \mathbb{E}[W_s(W_s + (W_t - W_s))] = \mathbb{E}[W_s^2] + \mathbb{E}[W_s(W_t - W_s)]
    $$

    By independence and $\mathbb{E}[W_t - W_s] = 0$:

    $$
    \mathbb{E}[W_s(W_t - W_s)] = \mathbb{E}[W_s]\mathbb{E}[W_t - W_s] = 0 \cdot 0 = 0
    $$

    Therefore $\mathbb{E}[W_s W_t] = \mathbb{E}[W_s^2] = s = \min(s, t)$.

---

**Exercise 3.**
Deduce that $(W_t)_{t \ge 0}$ has stationary increments, i.e., $W_t - W_s \overset{d}{=} W_{t-s}$.

??? success "Solution to Exercise 3"
    By property (iii), $W_t - W_s \sim \mathcal{N}(0, t-s)$ and $W_{t-s} - W_0 = W_{t-s} \sim \mathcal{N}(0, t-s)$. Since both are Gaussian with the same mean (0) and variance ($t - s$), they have the same distribution:

    $$
    W_t - W_s \overset{d}{=} W_{t-s}
    $$

    This is stationarity of increments: the distribution of the increment depends only on the length $t - s$, not on the starting time $s$.

---

**Exercise 4.**
Let $0 \le s < t$. Show that $W_t - W_s \sim \mathcal{N}(0, t - s)$ from the definition.

??? success "Solution to Exercise 4"
    This follows directly from property (iii) of the definition: for $0 \le s < t$, the increment $W_t - W_s \sim \mathcal{N}(0, t - s)$.

---

**Exercise 5.**
Prove that $W_t - W_s$ is independent of $\mathcal{F}_s = \sigma(W_u : u \le s)$.

??? success "Solution to Exercise 5"
    By property (ii), for any $0 \le t_0 < t_1 < \cdots < t_n$, the increments $W_{t_1} - W_{t_0}, W_{t_2} - W_{t_1}, \ldots$ are independent. In particular, $W_t - W_s$ is independent of $W_{s} - W_{0}, W_{s/2} - W_0, \ldots$ and all events in $\sigma(W_u : u \le s)$.

    More precisely, $W_t - W_s$ is independent of $\sigma(W_{t_1} - W_{t_0}, \ldots, W_{t_k} - W_{t_{k-1}})$ for any partition $0 = t_0 < t_1 < \cdots < t_k = s$. Since the $\sigma$-algebra $\mathcal{F}_s = \sigma(W_u : u \le s)$ is generated by such increments, $W_t - W_s$ is independent of $\mathcal{F}_s$.

---

**Exercise 6.**
Compute the characteristic function $\mathbb{E}[e^{i\lambda(W_t - W_s)}]$.

??? success "Solution to Exercise 6"
    Since $W_t - W_s \sim \mathcal{N}(0, t-s)$, the characteristic function is:

    $$
    \mathbb{E}[e^{i\lambda(W_t - W_s)}] = e^{-\frac{1}{2}\lambda^2(t-s)}
    $$

    This follows from the general formula for the characteristic function of $\mathcal{N}(\mu, \sigma^2)$: $\mathbb{E}[e^{i\lambda X}] = e^{i\lambda\mu - \frac{1}{2}\lambda^2\sigma^2}$. With $\mu = 0$ and $\sigma^2 = t - s$, the result follows.

---

**Exercise 7.**
Show that $\mathbb{E}[(W_t - W_s)^2] = |t - s|$.

??? success "Solution to Exercise 7"
    Since $W_t - W_s \sim \mathcal{N}(0, t-s)$:

    $$
    \mathbb{E}[(W_t - W_s)^2] = \text{Var}(W_t - W_s) + (\mathbb{E}[W_t - W_s])^2 = (t - s) + 0 = |t - s|
    $$

---

**Exercise 8.**
Use Kolmogorov's continuity theorem to justify the existence of a continuous modification. (Hint: Show $\mathbb{E}[|W_t - W_s|^4] = 3(t-s)^2$.)

??? success "Solution to Exercise 8"
    Kolmogorov's continuity theorem requires $\mathbb{E}[|X_t - X_s|^p] \le C|t-s|^{1+\beta}$ for some $p > 0$ and $\beta > 0$.

    For Brownian motion with $p = 4$: Since $W_t - W_s \sim \mathcal{N}(0, t-s)$ and $\mathbb{E}[Z^4] = 3$ for $Z \sim \mathcal{N}(0,1)$:

    $$
    \mathbb{E}[|W_t - W_s|^4] = \mathbb{E}[(W_t - W_s)^4] = 3(t-s)^2 = 3|t-s|^{1+1}
    $$

    This gives $C = 3$, $\beta = 1$, $p = 4$. By Kolmogorov's theorem, $W$ has a continuous modification that is Hölder-$\alpha$ for any $\alpha < \beta/p = 1/4$. Taking larger $p$ (which is allowed since all Gaussian moments are finite) improves the bound to $\alpha < 1/2 - 1/p$, and letting $p \to \infty$ gives continuity with Hölder exponent up to (but not including) $1/2$.

---

**Exercise 9.**
Why does Brownian motion fail to be differentiable almost surely? (Hint: Consider what differentiability would imply for $\mathbb{E}[(W_{t+h} - W_t)^2]/h^2$ as $h \to 0$.)

??? success "Solution to Exercise 9"
    If $W$ were differentiable at some point $t$ with derivative $L$, then $W_{t+h} - W_t \approx Lh$ for small $h$, so:

    $$
    \frac{\mathbb{E}[(W_{t+h} - W_t)^2]}{h^2} = \frac{h}{h^2} = \frac{1}{h} \to \infty \quad \text{as } h \to 0
    $$

    But differentiability would require $\mathbb{E}[(W_{t+h} - W_t)^2]/h^2 \to L^2$ (finite). The divergence $1/h \to \infty$ shows this is impossible. The difference quotient $(W_{t+h} - W_t)/h$ has variance $1/h \to \infty$, meaning it fluctuates without bound rather than converging to a limit.

---

**Exercise 10.**
Show that $(W_t)_{t \ge 0}$ is a martingale with respect to its natural filtration.

??? success "Solution to Exercise 10"
    For $s \le t$, write $W_t = W_s + (W_t - W_s)$. Since $W_t - W_s$ is independent of $\mathcal{F}_s = \sigma(W_u : u \le s)$ and has mean zero:

    $$
    \mathbb{E}[W_t | \mathcal{F}_s] = \mathbb{E}[W_s + (W_t - W_s) | \mathcal{F}_s] = W_s + \mathbb{E}[W_t - W_s | \mathcal{F}_s] = W_s + \mathbb{E}[W_t - W_s] = W_s + 0 = W_s
    $$

    Also, $\mathbb{E}[|W_t|] = \sqrt{2t/\pi} < \infty$ for all $t$, and $W_t$ is adapted to $\mathcal{F}_t$. So $(W_t)$ is a martingale.

---

**Exercise 11.**
Show that $(W_t^2 - t)_{t \ge 0}$ is a martingale.

??? success "Solution to Exercise 11"
    Write $W_t^2 = (W_s + (W_t - W_s))^2 = W_s^2 + 2W_s(W_t - W_s) + (W_t - W_s)^2$. Taking conditional expectations:

    $$
    \mathbb{E}[W_t^2 | \mathcal{F}_s] = W_s^2 + 2W_s \cdot \mathbb{E}[W_t - W_s | \mathcal{F}_s] + \mathbb{E}[(W_t - W_s)^2 | \mathcal{F}_s]
    $$

    $$
    = W_s^2 + 2W_s \cdot 0 + (t - s) = W_s^2 + (t - s)
    $$

    Therefore:

    $$
    \mathbb{E}[W_t^2 - t | \mathcal{F}_s] = W_s^2 + (t - s) - t = W_s^2 - s
    $$

    This confirms $(W_t^2 - t)$ is a martingale.

---

**Exercise 12.**
Is $(W_t^3)_{t \ge 0}$ a martingale? Justify your answer by computing $\mathbb{E}[W_t^3 | \mathcal{F}_s]$. (Hint: use the Gaussian moments of $W_t - W_s$.)

??? success "Solution to Exercise 12"
    $(W_t^3)$ is **not** a martingale. Compute $\mathbb{E}[W_t^3 | \mathcal{F}_s]$ by expanding $W_t = W_s + (W_t - W_s)$. Let $\Delta = W_t - W_s$:

    $$
    W_t^3 = (W_s + \Delta)^3 = W_s^3 + 3W_s^2\Delta + 3W_s\Delta^2 + \Delta^3
    $$

    Taking conditional expectations (using $\mathbb{E}[\Delta | \mathcal{F}_s] = 0$, $\mathbb{E}[\Delta^2 | \mathcal{F}_s] = t - s$, $\mathbb{E}[\Delta^3 | \mathcal{F}_s] = 0$):

    $$
    \mathbb{E}[W_t^3 | \mathcal{F}_s] = W_s^3 + 0 + 3W_s(t-s) + 0 = W_s^3 + 3W_s(t-s)
    $$

    Since $\mathbb{E}[W_t^3 | \mathcal{F}_s] = W_s^3 + 3W_s(t-s) \neq W_s^3$ (unless $t = s$), the process $(W_t^3)$ is not a martingale. However, one can check that $W_t^3 - 3tW_t$ is a martingale.

---

**Exercise 13.**
Let $W_t$ and $\widetilde{W}_t$ be independent Brownian motions. Compute the quadratic covariation $\langle W, \widetilde{W} \rangle_t$.

??? success "Solution to Exercise 13"
    If $W_t$ and $\widetilde{W}_t$ are independent Brownian motions, the cross variation is:

    $$
    \langle W, \widetilde{W} \rangle_t = \lim_{\|\Pi\| \to 0} \sum_i (W_{t_{i+1}} - W_{t_i})(\widetilde{W}_{t_{i+1}} - \widetilde{W}_{t_i})
    $$

    The expectation of each term is $\mathbb{E}[\Delta W_i \cdot \Delta\widetilde{W}_i] = 0$ (by independence), and the variance of the sum is:

    $$
    \text{Var}\left(\sum_i \Delta W_i \cdot \Delta\widetilde{W}_i\right) = \sum_i \text{Var}(\Delta W_i \cdot \Delta\widetilde{W}_i) = \sum_i (\Delta t_i)^2 \le \|\Pi\| \cdot T \to 0
    $$

    Therefore $\langle W, \widetilde{W} \rangle_t = 0$.

---

**Exercise 14.**
What is $\langle W, \widetilde{W} \rangle_t$ if $\widetilde{W}_t = \rho W_t + \sqrt{1-\rho^2} B_t$, where $B_t$ is independent of $W_t$?

??? success "Solution to Exercise 14"
    With $\widetilde{W}_t = \rho W_t + \sqrt{1-\rho^2} B_t$ where $B_t$ is independent of $W_t$:

    $$
    \langle W, \widetilde{W} \rangle_t = \langle W, \rho W + \sqrt{1-\rho^2} B \rangle_t = \rho \langle W, W \rangle_t + \sqrt{1-\rho^2} \langle W, B \rangle_t
    $$

    Since $\langle W, W \rangle_t = t$ and $\langle W, B \rangle_t = 0$ (by independence):

    $$
    \langle W, \widetilde{W} \rangle_t = \rho t
    $$

---

**Exercise 15.**
Interpret the result of Exercise 14 in terms of correlation between the two processes.

??? success "Solution to Exercise 15"
    The result $\langle W, \widetilde{W} \rangle_t = \rho t$ shows that the quadratic covariation per unit time equals the correlation $\rho$ between the two processes. This means:

    - $\rho = 1$: The processes move in lockstep; $\langle W, \widetilde{W} \rangle_t = t = \langle W, W \rangle_t$
    - $\rho = 0$: The processes are independent; $\langle W, \widetilde{W} \rangle_t = 0$
    - $\rho = -1$: The processes move in opposite directions; $\langle W, \widetilde{W} \rangle_t = -t$

    In multi-asset finance, $\rho$ governs the diversification benefit: the portfolio variance depends on the cross variation between asset returns.

---

**Exercise 16.**
Show that Brownian motion has infinite total variation on any interval $[0, T]$ almost surely.

??? success "Solution to Exercise 16"
    For the uniform partition $\Pi_n$ of $[0, T]$ with $\Delta t = T/n$, each $|\Delta W_i| = |W_{t_{i+1}} - W_{t_i}|$ satisfies $\mathbb{E}[|\Delta W_i|] = \sqrt{2\Delta t/\pi} = \sqrt{2T/(\pi n)}$.

    The expected total variation is:

    $$
    \mathbb{E}[V_1(W, \Pi_n)] = n \cdot \sqrt{\frac{2T}{\pi n}} = \sqrt{\frac{2nT}{\pi}} \to \infty
    $$

    For a lower bound on the total variation itself: by the Cauchy-Schwarz inequality,

    $$
    V_1(W, \Pi_n) = \sum_i |\Delta W_i| \ge \frac{(\sum_i |\Delta W_i|)^2}{\sum_i |\Delta W_i|} \ge \frac{\sum_i (\Delta W_i)^2}{\max_i |\Delta W_i|}
    $$

    As $\|\Pi_n\| \to 0$: the numerator converges to $T$ in $L^2$ (quadratic variation), and the denominator converges to $0$ in probability (by Hölder continuity). Therefore $V_1(W, \Pi_n) \to \infty$ in probability, and $V_1(W) = \sup_\Pi V_1(W, \Pi) = +\infty$ a.s.

---

**Exercise 17.**
Prove that Brownian motion is Hölder continuous of any order $\alpha < 1/2$, but of no order $\alpha \ge 1/2$.

??? success "Solution to Exercise 17"
    **Hölder-$\alpha$ for $\alpha < 1/2$:** Since $W_t - W_s \sim \mathcal{N}(0, t-s)$, for any $p > 2$:

    $$
    \mathbb{E}[|W_t - W_s|^p] = C_p |t-s|^{p/2}
    $$

    Kolmogorov's continuity criterion (with $\beta = p/2 - 1 > 0$) gives Hölder-$\alpha$ for $\alpha < \beta/p = 1/2 - 1/p$. Taking $p \to \infty$ yields $\alpha < 1/2$.

    **Not Hölder-$1/2$:** By the law of the iterated logarithm:

    $$
    \limsup_{h \to 0^+} \frac{|W_{t+h} - W_t|}{\sqrt{2h\log\log(1/h)}} = 1 \quad \text{a.s.}
    $$

    If $W$ were Hölder-$1/2$, we would have $|W_{t+h} - W_t| \le C\sqrt{h}$, so the limsup would be 0. The limsup being 1 contradicts this, so $W$ is not Hölder-$1/2$.

---

**Exercise 18.**
(Time Reversal) Let $\tilde{W}_t = W_T - W_{T-t}$ for $t \in [0, T]$. Show that $\tilde{W}$ is also a Brownian motion on $[0, T]$.

??? success "Solution to Exercise 18"
    Define $\tilde{W}_t = W_T - W_{T-t}$ for $t \in [0, T]$. We verify the four properties:

    **(i)** $\tilde{W}_0 = W_T - W_T = 0$.

    **(ii) Independent increments:** For $0 \le t_0 < t_1 < \cdots < t_n \le T$:

    $$
    \tilde{W}_{t_k} - \tilde{W}_{t_{k-1}} = (W_T - W_{T-t_k}) - (W_T - W_{T-t_{k-1}}) = W_{T-t_{k-1}} - W_{T-t_k}
    $$

    Since $T - t_n < T - t_{n-1} < \cdots < T - t_0$, these are increments of $W$ over disjoint intervals (in reverse order), hence independent.

    **(iii) Gaussian stationary increments:**

    $$
    \tilde{W}_t - \tilde{W}_s = W_{T-s} - W_{T-t} \sim \mathcal{N}(0, (T-s) - (T-t)) = \mathcal{N}(0, t-s)
    $$

    **(iv) Continuous paths:** $t \mapsto \tilde{W}_t = W_T - W_{T-t}$ is continuous since $W$ has continuous paths.

---

**Exercise 19.**
(Exponential Martingale) Define $M_t := \exp\left( \lambda W_t - \frac{1}{2} \lambda^2 t \right)$ for $\lambda \in \mathbb{R}$. Show that $(M_t)_{t \ge 0}$ is a martingale and compute $\mathbb{E}[M_t]$. Explain why this is fundamental in stochastic calculus and mathematical finance (hint: Girsanov theorem, risk-neutral pricing).

??? success "Solution to Exercise 19"
    Define $M_t = \exp(\lambda W_t - \frac{1}{2}\lambda^2 t)$. We show this is a martingale.

    For $s \le t$, write $W_t = W_s + (W_t - W_s)$:

    $$
    \mathbb{E}[M_t | \mathcal{F}_s] = \mathbb{E}\left[\exp\left(\lambda W_s + \lambda(W_t - W_s) - \frac{1}{2}\lambda^2 t\right) \Big| \mathcal{F}_s\right]
    $$

    $$
    = \exp\left(\lambda W_s - \frac{1}{2}\lambda^2 t\right) \cdot \mathbb{E}\left[e^{\lambda(W_t - W_s)}\right]
    $$

    Since $W_t - W_s \sim \mathcal{N}(0, t-s)$, the MGF gives $\mathbb{E}[e^{\lambda(W_t - W_s)}] = e^{\frac{1}{2}\lambda^2(t-s)}$. Therefore:

    $$
    \mathbb{E}[M_t | \mathcal{F}_s] = \exp\left(\lambda W_s - \frac{1}{2}\lambda^2 t + \frac{1}{2}\lambda^2(t-s)\right) = \exp\left(\lambda W_s - \frac{1}{2}\lambda^2 s\right) = M_s
    $$

    Also, $\mathbb{E}[M_t] = M_0 = e^0 = 1$ for all $t$.

    **Significance:** The exponential martingale is the Radon–Nikodym derivative used in the **Girsanov theorem** to change probability measures. In finance, it transforms the real-world measure $\mathbb{P}$ to the risk-neutral measure $\mathbb{Q}$ under which discounted asset prices are martingales, enabling arbitrage-free option pricing.

---

**Exercise 20.**
(Law of the Iterated Logarithm) The law of the iterated logarithm states that $\limsup_{t \to 0^+} \frac{W_t}{\sqrt{2 t \log \log (1/t)}} = 1$ a.s. Interpret this result in terms of path oscillation and explain why it is incompatible with differentiability.

??? success "Solution to Exercise 20"
    The law of the iterated logarithm states:

    $$
    \limsup_{t \to 0^+} \frac{W_t}{\sqrt{2t\log\log(1/t)}} = 1 \quad \text{a.s.}
    $$

    **Interpretation:** Near $t = 0$, the largest fluctuations of $W_t$ are of order $\sqrt{2t\log\log(1/t)}$. This is slightly larger than $\sqrt{t}$ (by the slowly varying factor $\sqrt{\log\log(1/t)}$).

    **Incompatibility with differentiability:** If $W$ were differentiable at $t = 0$ with derivative $L$, then $W_t \approx Lt$ for small $t$, which means:

    $$
    \frac{W_t}{\sqrt{2t\log\log(1/t)}} \approx \frac{Lt}{\sqrt{2t\log\log(1/t)}} = L\sqrt{\frac{t}{2\log\log(1/t)}} \to 0
    $$

    But the limsup is 1, not 0. The LIL shows that Brownian motion oscillates at rate $\sqrt{t\log\log(1/t)}$, which is infinitely faster than the linear rate $t$ required for differentiability. The oscillations never "calm down" at any time scale.
