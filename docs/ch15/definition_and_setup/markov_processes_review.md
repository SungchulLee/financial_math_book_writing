# Markov Processes Review

*This section covers markov processes review in the context of Markov Processes Review in Chapter 15.*

!!! abstract "Learning Objectives"
    By the end of this section, you will be able to:
    
    1. Understand the key concepts of markov processes review
    2. Apply the mathematical framework presented
    3. Connect this topic to related areas in quantitative finance

---

## Overview

This section introduces the fundamental concepts of markov processes review. We will explore its theoretical foundations and practical applications in quantitative finance.

---

## Key Concepts

*Content under development.*

---

## Mathematical Framework

*Content under development.*

---

## Summary

This section presented the fundamental concepts of markov processes review. The material connects to subsequent sections in this chapter.

---

## Exercises

**Exercise 1.** State the Markov property formally for a continuous-time process $(X_t)_{t \geq 0}$ with filtration $(\mathcal{F}_t)$. Explain in your own words why the Markov property implies that the entire history $\{X_s : 0 \leq s \leq t\}$ is irrelevant for predicting $X_T$ ($T > t$) once $X_t$ is known.

??? success "Solution to Exercise 1"
    The **Markov property** for a continuous-time process $(X_t)_{t \geq 0}$ adapted to a filtration $(\mathcal{F}_t)_{t \geq 0}$ states: for all $T > t \geq 0$ and all bounded measurable functions $f$,

    $$
    \mathbb{E}[f(X_T) \mid \mathcal{F}_t] = \mathbb{E}[f(X_T) \mid X_t]
    $$

    In words, the conditional distribution of the future state $X_T$ given the entire history up to time $t$ (encoded by $\mathcal{F}_t$, which contains all information about $\{X_s : 0 \leq s \leq t\}$ and possibly more) depends only on the current state $X_t$.

    The intuition is that $X_t$ is a **sufficient statistic** for predicting the future. The entire trajectory $\{X_s : 0 \leq s \leq t\}$---including where the process was at time $s = 0$, whether it went up or down, how volatile it was---is irrelevant once $X_t$ is known. The current state encapsulates all the information from the past that is relevant for the future evolution. This is sometimes called the "memoryless" property: the process forgets its history and only remembers where it is now.

---

**Exercise 2.** Let $(X_t)_{t \geq 0}$ be a Markov process with transition kernel $p(s, x; t, A)$. Write down the Chapman-Kolmogorov equation and explain its role in ensuring consistency of the finite-dimensional distributions.

??? success "Solution to Exercise 2"
    Let $p(s, x; t, A) = \mathbb{P}(X_t \in A \mid X_s = x)$ be the transition kernel. The **Chapman-Kolmogorov equation** states that for $s < r < t$ and all measurable sets $A$:

    $$
    p(s, x; t, A) = \int_{\mathbb{R}} p(r, y; t, A)\,p(s, x; r, dy)
    $$

    This equation asserts that to compute the probability of transitioning from $(s, x)$ to set $A$ at time $t$, one can break the transition into two steps: first transition from $(s, x)$ to some intermediate state $y$ at time $r$, and then from $(r, y)$ to $A$ at time $t$, integrating over all possible intermediate states.

    **Role in consistency**: The Chapman-Kolmogorov equation ensures that the transition probabilities for different time intervals are mutually consistent. Without it, the two-step and one-step transition probabilities could disagree, and the finite-dimensional distributions $\mathbb{P}(X_{t_1} \in A_1, \ldots, X_{t_n} \in A_n \mid X_0 = x)$ built from the kernel would not define a valid stochastic process. The Kolmogorov extension theorem then guarantees that these consistent finite-dimensional distributions extend to a probability measure on the full path space.

---

**Exercise 3.** Consider the Ornstein-Uhlenbeck process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ with $\kappa > 0$. Show that it is a Markov process by computing the conditional distribution $X_T \mid X_t = x$ and verifying that it depends only on $x$ (not on earlier values of $X$).

??? success "Solution to Exercise 3"
    The Ornstein-Uhlenbeck process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ has the explicit solution:

    $$
    X_T = X_t e^{-\kappa(T-t)} + \sigma\int_t^T e^{-\kappa(T-s)}\,dW_s
    $$

    The stochastic integral $\sigma\int_t^T e^{-\kappa(T-s)}\,dW_s$ depends only on Brownian increments $\{W_s - W_t : t \leq s \leq T\}$, which are independent of $\mathcal{F}_t$.

    Therefore, given $X_t = x$:

    $$
    X_T \mid X_t = x \sim \mathcal{N}\!\left(xe^{-\kappa(T-t)},\; \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa(T-t)})\right)
    $$

    The conditional distribution of $X_T$ given $\mathcal{F}_t$ depends on $\mathcal{F}_t$ only through $X_t$: the mean is $X_t e^{-\kappa(T-t)}$ (a function of $X_t$ alone) and the variance $\frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa(T-t)})$ depends only on the time difference $T - t$, not on the history. This confirms the Markov property: $\mathbb{E}[f(X_T) \mid \mathcal{F}_t] = \mathbb{E}[f(X_T) \mid X_t]$.

---

**Exercise 4.** Define the infinitesimal generator $\mathcal{A}$ of a Markov process and compute $\mathcal{A}f(x)$ for $f(x) = e^{ux}$ when the process is a standard Brownian motion $dX_t = dW_t$. Verify your answer using the definition

$$
\mathcal{A}f(x) = \lim_{t \downarrow 0} \frac{\mathbb{E}^x[f(X_t)] - f(x)}{t}
$$

??? success "Solution to Exercise 4"
    The infinitesimal generator $\mathcal{A}$ of a Markov process is defined by:

    $$
    \mathcal{A}f(x) = \lim_{t \downarrow 0} \frac{\mathbb{E}^x[f(X_t)] - f(x)}{t}
    $$

    for all $f$ in the domain of $\mathcal{A}$ (functions for which the limit exists).

    For standard Brownian motion $dX_t = dW_t$, we have $X_t \mid X_0 = x \sim \mathcal{N}(x, t)$. With $f(x) = e^{ux}$:

    $$
    \mathbb{E}^x[e^{uX_t}] = e^{ux + \frac{1}{2}u^2 t}
    $$

    Therefore:

    $$
    \frac{\mathbb{E}^x[e^{uX_t}] - e^{ux}}{t} = \frac{e^{ux}(e^{\frac{1}{2}u^2 t} - 1)}{t}
    $$

    Taking $t \downarrow 0$:

    $$
    \mathcal{A}f(x) = e^{ux} \cdot \lim_{t \downarrow 0} \frac{e^{\frac{1}{2}u^2 t} - 1}{t} = e^{ux} \cdot \frac{1}{2}u^2 = \frac{1}{2}u^2 e^{ux}
    $$

    Verification: for Brownian motion, the generator is $\mathcal{A} = \frac{1}{2}\frac{d^2}{dx^2}$. Computing $\frac{1}{2}f''(x) = \frac{1}{2}u^2 e^{ux}$, which matches.

---

**Exercise 5.** Explain the difference between a time-homogeneous and a time-inhomogeneous Markov process. Give one example of each from finance (e.g., interest rate models) and state whether each admits a stationary distribution.

??? success "Solution to Exercise 5"
    A Markov process is **time-homogeneous** if the transition probabilities depend only on the time difference: $p(s, x; t, A) = p(0, x; t-s, A)$ for all $s < t$. The dynamics do not change with calendar time.

    A Markov process is **time-inhomogeneous** if the transition probabilities depend explicitly on the calendar times $s$ and $t$, not just on $t - s$.

    **Time-homogeneous example**: The Vasicek model $dr_t = \kappa(\theta - r_t)\,dt + \sigma\,dW_t$ with constant parameters $\kappa, \theta, \sigma$. The conditional distribution of $r_T$ given $r_t$ depends only on $T - t$ and $r_t$. This process admits a stationary distribution $r_\infty \sim \mathcal{N}(\theta, \sigma^2/(2\kappa))$, since as $t \to \infty$ the conditional distribution converges regardless of the initial state.

    **Time-inhomogeneous example**: The Hull-White model $dr_t = (\theta(t) - \kappa r_t)\,dt + \sigma\,dW_t$ with a time-dependent mean-reversion level $\theta(t)$. The transition probabilities depend on the specific times $s$ and $t$ (through $\theta(\cdot)$), not just on $t - s$. This model does **not** admit a stationary distribution in general, because the dynamics keep changing over time---the target level $\theta(t)/\kappa$ varies, so the process never settles into a time-invariant equilibrium.

---

**Exercise 6.** A transition semigroup $(P_t)_{t \geq 0}$ satisfies $P_t f(x) = \mathbb{E}^x[f(X_t)]$. Show that the semigroup property $P_{t+s} = P_t \circ P_s$ is equivalent to the Chapman-Kolmogorov equation for the transition kernel. Under what additional condition is the semigroup a Feller semigroup?

??? success "Solution to Exercise 6"
    **Semigroup property implies Chapman-Kolmogorov**: The semigroup property states $P_{t+s}f(x) = P_t(P_s f)(x)$ for all bounded measurable $f$. Expanding:

    $$
    P_{t+s}f(x) = \mathbb{E}^x[f(X_{t+s})] = \int f(z)\,p(0, x; t+s, dz)
    $$

    $$
    P_t(P_sf)(x) = \mathbb{E}^x[(P_sf)(X_t)] = \int \left(\int f(z)\,p(0, y; s, dz)\right) p(0, x; t, dy)
    $$

    For time-homogeneous processes, $p(0, x; t+s, dz) = \int p(0, y; s, dz)\,p(0, x; t, dy)$, which is the Chapman-Kolmogorov equation (with $p(r, x; r+t, \cdot) = p(0, x; t, \cdot)$ by time-homogeneity).

    **Chapman-Kolmogorov implies semigroup property**: Conversely, if the Chapman-Kolmogorov equation holds, then for any $f$:

    $$
    \int f(z)\,p(0, x; t+s, dz) = \int\!\!\int f(z)\,p(0, y; s, dz)\,p(0, x; t, dy) = P_t(P_sf)(x)
    $$

    so $P_{t+s} = P_t \circ P_s$.

    **Feller semigroup**: The additional condition is **strong continuity** on $C_0(D)$ (continuous functions vanishing at infinity):

    $$
    \lim_{t \downarrow 0} \|P_t f - f\|_\infty = 0 \quad \text{for all } f \in C_0(D)
    $$

    combined with the requirement that $P_t$ maps $C_0(D)$ into itself. Strong continuity follows from stochastic continuity of the process. A Feller semigroup guarantees the existence of a well-defined infinitesimal generator on a dense domain in $C_0(D)$, which is the starting point for the analytic theory of Markov processes.
