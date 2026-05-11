# Brownian Motion Martingales

Brownian motion is the concrete testing ground for everything developed so far — [Martingales](martingale.md), [Martingale Convergence](martingale_convergence.md), [Uniform Integrability](uniform_integrability.md), and the Doob-Meyer structure. The abstract theory becomes calculable here: $W_t$ itself is a martingale, simple polynomial corrections produce more, and a single exponential object generates them all.

Throughout, $(W_t)_{t\ge 0}$ is a standard Brownian motion on $(\Omega, \mathcal{F}, (\mathcal{F}_t), \mathbb{P})$ with the usual conditions.

---

## The Basic Martingale: W_t

Independent increments make the martingale check immediate: for $s < t$, $W_t - W_s$ is independent of $\mathcal{F}_s$ with mean zero, so

$$
\mathbb{E}[W_t \mid \mathcal{F}_s] = W_s + \mathbb{E}[W_t - W_s] = W_s.
$$

Integrability follows from $W_t \sim N(0,t)$. The martingale property is the formal statement that Brownian motion has no drift: the best prediction of the future is the present.

---

## Polynomial Martingales

Powers of $W_t$ are not themselves martingales, but the deterministic growth in their moments can be compensated.

!!! success "Compensated square and cube"
    The processes

    $$
    W_t^2 - t \quad\text{and}\quad W_t^3 - 3tW_t
    $$

    are martingales.

**Idea**. Write $W_t = W_s + \Delta$ with $\Delta = W_t - W_s \sim N(0, t-s)$ independent of $\mathcal{F}_s$. Expanding the power and taking conditional expectations replaces $\Delta^k$ by its moment — $\mathbb{E}\Delta = 0$, $\mathbb{E}\Delta^2 = t-s$, $\mathbb{E}\Delta^3 = 0$. The expansion of $W_t^2$ gives $\mathbb{E}[W_t^2 \mid \mathcal{F}_s] = W_s^2 + (t-s)$, so the compensation by $t$ yields a martingale. Similarly $\mathbb{E}[W_t^3 \mid \mathcal{F}_s] = W_s^3 + 3W_s(t-s)$, matched by the compensator $3tW_t$.

The compensator of $W_t^2$ is $[W]_t = t$ — a foreshadowing of the Doob-Meyer decomposition (see [Doob-Meyer Decomposition](doob_meyer_decomposition.md)).

---

## Hermite Structure

The polynomial martingales are not ad hoc: they are **Hermite polynomials** of $(W_t, t)$. Define the probabilist's Hermite polynomials $H_n$ by the generating function

$$
\exp\!\left(\theta x - \tfrac{\theta^2}{2}\right) = \sum_{n=0}^\infty \frac{\theta^n}{n!} H_n(x),
$$

and the "time-scaled" version $H_n(W_t, t) = t^{n/2} H_n(W_t/\sqrt t)$. The first four:

$$
H_0 = 1,\quad H_1 = W_t,\quad H_2 = W_t^2 - t,\quad H_3 = W_t^3 - 3tW_t,\quad H_4 = W_t^4 - 6tW_t^2 + 3t^2.
$$

Each $H_n(W_t, t)$ is a martingale. The next section explains why.

---

## The Exponential Martingale

The central object of the theory is

$$
Z_t^\theta = \exp\!\left(\theta W_t - \tfrac{\theta^2 t}{2}\right), \qquad \theta \in \mathbb{R}.
$$

!!! success "Exponential martingale"
    For every $\theta \in \mathbb{R}$, $Z_t^\theta$ is a strictly positive martingale with $\mathbb{E}[Z_t^\theta] = 1$.

**Proof**. Factor $Z_t^\theta = Z_s^\theta \cdot Y$ where $Y = \exp(\theta(W_t - W_s) - \tfrac{\theta^2(t-s)}{2})$. Since $W_t - W_s \sim N(0, t-s)$ is independent of $\mathcal{F}_s$, the Gaussian mgf $\mathbb{E}[e^{\theta Z}] = e^{\theta^2(t-s)/2}$ for $Z \sim N(0,t-s)$ gives $\mathbb{E}[Y] = 1$, so $\mathbb{E}[Z_t^\theta \mid \mathcal{F}_s] = Z_s^\theta$. $\square$

The quadratic term $-\theta^2 t/2$ is exactly what the exponential growth of $e^{\theta W_t}$ demands. This is the prototype of the general fact that $\exp(M_t - \tfrac{1}{2}[M]_t)$ is a local martingale for every continuous local martingale $M$.

!!! info "Generating all polynomial martingales"
    Expanding the exponential in powers of $\theta$,

    $$
    Z_t^\theta = \sum_{n=0}^\infty \frac{\theta^n}{n!} H_n(W_t, t),
    $$

    and each coefficient is a martingale. Indeed, $\mathbb{E}[Z_t^\theta \mid \mathcal{F}_s] = Z_s^\theta$ holds for all $\theta$; dominated convergence justifies interchanging sum and conditional expectation (using the Gaussian moment bound $\sum |\theta|^n |H_n(W_t,t)|/n! \le \exp(|\theta||W_t| + \theta^2 t/2) \in L^1$). Matching coefficients gives $\mathbb{E}[H_n(W_t, t) \mid \mathcal{F}_s] = H_n(W_s, s)$.

So a single exponential object encodes *all* moment-compensation martingales at once.

---

## Applications

!!! example "Girsanov"
    Defining $d\mathbb{Q}/d\mathbb{P}\big|_{\mathcal{F}_t} = Z_t^\theta$ turns $\widetilde W_t = W_t - \theta t$ into a $\mathbb{Q}$-Brownian motion. The exponential martingale *is* the density process for drift changes — the mechanism behind risk-neutral pricing.

!!! example "Moment generating functions and hitting times"
    When optional sampling applies at a stopping time $\tau$, $\mathbb{E}[\exp(\theta W_\tau - \theta^2\tau/2)] = 1$, yielding the joint Laplace transform of $(W_\tau, \tau)$ — the standard route to hitting time distributions.

!!! example "Gaussian tail bound"
    Applying Markov to $Z_t^\theta$ and optimizing in $\theta$ gives $\mathbb{P}(W_t \ge a) \le e^{-a^2/2t}$ for $a > 0$.

---

## The Stochastic Exponential

For any continuous local martingale $M$ with $M_0 = 0$,

$$
\mathcal{E}(M)_t = \exp\!\left(M_t - \tfrac{1}{2}[M]_t\right)
$$

is a local martingale (the **Doléans-Dade exponential**), the unique solution to $dZ_t = Z_t\,dM_t$, $Z_0 = 1$. For $M = \theta W$, $[M]_t = \theta^2 t$, recovering $Z_t^\theta$. This is developed fully alongside Itô calculus.

---

## Summary

| Martingale | Role |
|---|---|
| $W_t$ | The driftless process itself |
| $W_t^2 - t$ | Variance compensation; $[W]_t = t$ |
| $W_t^3 - 3tW_t$ | Third-moment compensation |
| $H_n(W_t, t)$ | $n$-th Hermite martingale |
| $\exp(\theta W_t - \theta^2 t/2)$ | Generating function; density process for Girsanov |

The exponential martingale is the organizing principle: polynomial martingales are its Taylor coefficients, Girsanov its change-of-measure content, and large deviations its Markov-inequality consequence.

---

## Exercises

**Exercise 1.** Prove $\mathbb{E}[Z_t^\theta] = 1$ and $\operatorname{Var}(Z_t^\theta) = e^{\theta^2 t} - 1$, and show $Z_t^\theta \to 0$ a.s. for $\theta \ne 0$.

??? success "Solution to Exercise 1"
    $\mathbb{E}[Z_t^\theta] = \mathbb{E}[Z_0^\theta] = 1$ by the martingale property. For the variance,

    $$
    \mathbb{E}[(Z_t^\theta)^2] = e^{-\theta^2 t}\,\mathbb{E}[e^{2\theta W_t}] = e^{-\theta^2 t}\,e^{2\theta^2 t} = e^{\theta^2 t},
    $$

    so $\operatorname{Var}(Z_t^\theta) = e^{\theta^2 t} - 1$.

    For $\theta \ne 0$: $\log Z_t^\theta / t = \theta W_t/t - \theta^2/2$. By the law of the iterated logarithm, $W_t/t \to 0$ a.s., so $\log Z_t^\theta / t \to -\theta^2/2 < 0$ and $Z_t^\theta \to 0$ a.s. (This also shows the family is not UI; see [Uniform Integrability](uniform_integrability.md).) $\square$

---

**Exercise 2.** Expand $\exp(\theta W_t - \theta^2 t/2)$ as a power series in $\theta$ through order $4$ and identify the Hermite martingales $H_0, \ldots, H_4$.

??? success "Solution to Exercise 2"
    Multiplying $\sum (\theta W_t)^k/k!$ by $\sum (-\theta^2 t/2)^j/j!$ and collecting terms:

    - $\theta^0$: $1$
    - $\theta^1$: $W_t$
    - $\theta^2$: $\tfrac{1}{2}(W_t^2 - t)$
    - $\theta^3$: $\tfrac{1}{6}(W_t^3 - 3tW_t)$
    - $\theta^4$: $\tfrac{1}{24}(W_t^4 - 6tW_t^2 + 3t^2)$

    The coefficients of $\theta^n/n!$ are $H_n(W_t, t)$; each is a martingale. $\square$

---

**Exercise 3.** Show that $\cosh(\theta W_t) e^{-\theta^2 t/2}$ and $\sinh(\theta W_t) e^{-\theta^2 t/2}$ are martingales.

??? success "Solution to Exercise 3"
    Using $\cosh x = (e^x + e^{-x})/2$ and $\sinh x = (e^x - e^{-x})/2$,

    $$
    \cosh(\theta W_t) e^{-\theta^2 t/2} = \tfrac{1}{2}(Z_t^\theta + Z_t^{-\theta}),\qquad \sinh(\theta W_t) e^{-\theta^2 t/2} = \tfrac{1}{2}(Z_t^\theta - Z_t^{-\theta}).
    $$

    Linear combinations of martingales are martingales. $\square$

---

**Exercise 4.** Prove **Lévy's characterization**: a continuous martingale $M$ with $M_0 = 0$ and $[M]_t = t$ is a standard Brownian motion.

??? success "Solution to Exercise 4"
    By the stochastic exponential principle, $\mathcal{E}(\theta M)_t = \exp(\theta M_t - \tfrac{\theta^2}{2}[M]_t) = \exp(\theta M_t - \theta^2 t/2)$ is a local martingale, and it is a true martingale because $[M]_t = t$ is deterministic (Novikov: $\mathbb{E}[\exp(\tfrac{1}{2}\theta^2 t)] < \infty$).

    The martingale identity $\mathbb{E}[\exp(\theta M_t - \theta^2 t/2)\mid \mathcal{F}_s] = \exp(\theta M_s - \theta^2 s/2)$ becomes, on setting $\theta = i\alpha$,

    $$
    \mathbb{E}[e^{i\alpha(M_t - M_s)}\mid \mathcal{F}_s] = e^{-\alpha^2(t-s)/2}.
    $$

    The right side is deterministic, so $M_t - M_s$ is independent of $\mathcal{F}_s$ with characteristic function of $N(0, t-s)$. Thus $M$ has continuous paths, $M_0 = 0$, and stationary independent Gaussian increments: it is a standard Brownian motion. $\square$

---

**Exercise 5.** State the martingale problem for Brownian motion and explain its connection to the heat equation.

??? success "Solution to Exercise 5"
    For $f \in C^2(\mathbb{R})$, Itô's formula gives

    $$
    f(W_t) - \tfrac{1}{2}\int_0^t f''(W_s)\,ds = f(W_0) + \int_0^t f'(W_s)\,dW_s,
    $$

    which is a local martingale (and a true martingale when $f'$ has suitable growth). This is the **martingale problem** for Brownian motion: the generator is $\tfrac{1}{2}\partial_{xx}$.

    If $u$ solves the heat equation $\partial_t u = \tfrac{1}{2}\partial_{xx} u$, then Itô's formula applied to $u(W_t, T-t)$ yields

    $$
    du(W_t, T-t) = \partial_x u\,dW_t + \bigl(-\partial_t u + \tfrac{1}{2}\partial_{xx} u\bigr)\,dt = \partial_x u\,dW_t,
    $$

    so $u(W_t, T-t)$ is a local martingale. This is the Feynman-Kac connection: heat-equation solutions are expectations of Brownian functionals. $\square$
