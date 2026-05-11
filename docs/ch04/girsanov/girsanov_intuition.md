# Intuitive Introduction and Motivation


Girsanov’s theorem is one of the most important results in stochastic calculus,
yet it is often misunderstood at first encounter.

At an intuitive level, the theorem resolves a seeming paradox:

> *How can a stochastic process with drift become driftless, without changing its paths?*

The resolution lies in understanding the difference between **paths** and
**probability measures**.

---

## Paths vs Probability Measures


A probability measure does not create new paths — it assigns **weights** to paths.
All measure changes here are between **equivalent measures**: no path is removed, only reweighted.

---

## A Thought Experiment


Imagine observing many random paths over time.
Different measures assign different weights to the same paths, changing averages (drift) without changing trajectories.

From the perspective of averages:

- one observer sees a **positive drift**,
- another observer sees **no drift**.

Only the probability weights have changed.

---

## Continuous-Time Perspective


Let $W_t$ be Brownian motion under a measure $\mathbb{P}$.
The process

$$
Y_t = W_t + \theta t
$$

has drift $\theta$ under $\mathbb{P}$. More precisely:

- Under $\mathbb{P}$: $Y_t$ has drift $\theta$ (a Brownian motion plus a linear trend).
- Girsanov's theorem guarantees a measure $\mathbb{Q}$ under which $Y_t$ has drift $0$.

Girsanov’s theorem answers the following question:

> *Is there an equivalent probability measure under which $Y_t$ is a Brownian motion?*

The answer is yes (under the [Novikov condition](../martingale/novikov_kazamaki_conditions.md), automatically satisfied for constant $\theta$). The drift is absorbed into the probability measure — no sample path is added or removed, only reweighted.

---

## Why This Matters in Finance


In financial markets:

- under the **physical measure**, asset prices contain risk premia,
- under the **pricing measure**, discounted prices must have no predictable trend.

Girsanov’s theorem provides the precise mechanism for moving between these two
viewpoints.

---

## The Central Idea


> **Drift lives in the probability measure, not in the paths.**

The [theorem statement](girsanov_theorem.md) makes this precise, and the [proof](girsanov_proof.md) shows why the cancellation works.

---

## Exercises

**Exercise 1.**
Consider two observers watching the same set of stock price paths over one year. Observer A uses measure $\mathbb{P}$ and estimates a positive drift of 8%. Observer B uses measure $\mathbb{Q}$ and sees drift equal to the risk-free rate $r = 2\%$. Explain how both observers can be correct simultaneously, and describe what differs between their assessments.

??? success "Solution to Exercise 1"
    Both observers are correct because they are using different probability measures to evaluate the same set of sample paths. Observer A, using the physical measure $\mathbb{P}$, assigns probabilities to paths that reflect real-world likelihoods. Under this weighting, the average growth rate of the stock is 8%. Observer B, using the risk-neutral measure $\mathbb{Q}$, reweights the same paths via a Radon–Nikodym derivative so that upward-trending paths receive less probability and downward-trending paths receive more. Under this reweighting, the average growth rate equals the risk-free rate $r = 2\%$.

    What differs is not the paths themselves but the probability weights assigned to them. Both observers see the exact same collection of possible price trajectories. Observer A's weighting reflects beliefs about real-world returns (incorporating risk premia), while Observer B's weighting is constructed so that discounted prices are martingales, enabling arbitrage-free pricing. Neither observer is wrong — they are answering different questions about the same probability space.

---

**Exercise 2.**
Let $W_t$ be a standard Brownian motion under $\mathbb{P}$, and define $Y_t = W_t + 3t$. Under $\mathbb{P}$, compute $\mathbb{E}^{\mathbb{P}}[Y_t]$ and $\mathrm{Var}^{\mathbb{P}}(Y_t)$. Girsanov's theorem asserts there exists a measure $\mathbb{Q}$ under which $Y_t$ is a standard Brownian motion. Under $\mathbb{Q}$, what are $\mathbb{E}^{\mathbb{Q}}[Y_t]$ and $\mathrm{Var}^{\mathbb{Q}}(Y_t)$?

??? success "Solution to Exercise 2"
    Under $\mathbb{P}$, $Y_t = W_t + 3t$ where $W_t$ is standard Brownian motion. Since $\mathbb{E}^{\mathbb{P}}[W_t] = 0$ and $\mathrm{Var}^{\mathbb{P}}(W_t) = t$:

    $$
    \mathbb{E}^{\mathbb{P}}[Y_t] = \mathbb{E}^{\mathbb{P}}[W_t] + 3t = 3t
    $$

    $$
    \mathrm{Var}^{\mathbb{P}}(Y_t) = \mathrm{Var}^{\mathbb{P}}(W_t + 3t) = \mathrm{Var}^{\mathbb{P}}(W_t) = t
    $$

    Under $\mathbb{Q}$, Girsanov's theorem (with $\theta = 3$) ensures that $Y_t$ is a standard Brownian motion. Therefore:

    $$
    \mathbb{E}^{\mathbb{Q}}[Y_t] = 0
    $$

    $$
    \mathrm{Var}^{\mathbb{Q}}(Y_t) = t
    $$

    The variance is the same under both measures (since quadratic variation is a pathwise property), but the mean has changed from $3t$ to $0$. The drift has been absorbed into the probability measure.

---

**Exercise 3.**
A skeptic argues: "If changing the probability measure does not change any sample paths, then it cannot possibly change the price of a derivative." Explain the flaw in this reasoning, using the concept that expected values (and hence prices computed as discounted expectations) depend on the measure.

??? success "Solution to Exercise 3"
    The flaw in the skeptic's reasoning is that derivative prices are computed as **expected values** (specifically, discounted expected payoffs), and expected values depend on the probability measure. While the sample paths are the same under both $\mathbb{P}$ and $\mathbb{Q}$, the weights assigned to those paths differ.

    Consider a European call option with payoff $(S_T - K)^+$. Under $\mathbb{P}$, high stock price paths (where the option pays off handsomely) receive higher probability, since the stock has a positive risk premium $\mu > r$. Under $\mathbb{Q}$, those same high-return paths are downweighted.

    The pricing formula $C = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+]$ uses the risk-neutral expectation, which assigns different weights to the payoff across paths than $\mathbb{E}^{\mathbb{P}}[(S_T - K)^+]$ would. The change of measure does not change any individual path's payoff, but it changes the weighted average of those payoffs, and that weighted average is precisely the arbitrage-free price.

---

**Exercise 4.**
Suppose you flip a biased coin with $\mathbb{P}(\text{Heads}) = 0.7$. Define a new measure $\mathbb{Q}$ with $\mathbb{Q}(\text{Heads}) = 0.5$. The sample space $\{\text{H}, \text{T}\}$ is the same under both measures. Compute the Radon–Nikodym derivative $d\mathbb{Q}/d\mathbb{P}$ on each outcome and verify that $\mathbb{E}^{\mathbb{P}}[d\mathbb{Q}/d\mathbb{P}] = 1$. Use this discrete example to illustrate the intuition behind Girsanov's theorem.

??? success "Solution to Exercise 4"
    On the outcome $\text{H}$:

    $$
    \frac{d\mathbb{Q}}{d\mathbb{P}}(\text{H}) = \frac{\mathbb{Q}(\text{H})}{\mathbb{P}(\text{H})} = \frac{0.5}{0.7} = \frac{5}{7}
    $$

    On the outcome $\text{T}$:

    $$
    \frac{d\mathbb{Q}}{d\mathbb{P}}(\text{T}) = \frac{\mathbb{Q}(\text{T})}{\mathbb{P}(\text{T})} = \frac{0.5}{0.3} = \frac{5}{3}
    $$

    Verification of unit expectation:

    $$
    \mathbb{E}^{\mathbb{P}}\!\left[\frac{d\mathbb{Q}}{d\mathbb{P}}\right] = \mathbb{P}(\text{H}) \cdot \frac{5}{7} + \mathbb{P}(\text{T}) \cdot \frac{5}{3} = 0.7 \cdot \frac{5}{7} + 0.3 \cdot \frac{5}{3} = 0.5 + 0.5 = 1 \quad \checkmark
    $$

    The Radon–Nikodym derivative reweights outcomes without changing the sample space: $\text{H}$ is downweighted ($5/7 < 1$), $\text{T}$ is upweighted ($5/3 > 1$), removing the bias toward heads.

---

**Exercise 5.**
The statement "drift lives in the probability measure, not in the paths" is the central idea. Provide a concrete numerical example: take a discrete random walk with three possible paths and show that by reassigning probabilities (without adding or removing paths), you can change the expected drift from positive to zero.

??? success "Solution to Exercise 5"
    Consider a discrete random walk over one period with three possible paths:

    - Path A: the walk goes up by $+2$
    - Path B: the walk goes up by $+1$
    - Path C: the walk goes down by $-1$

    Under measure $\mathbb{P}$, assign probabilities $\mathbb{P}(A) = 0.5$, $\mathbb{P}(B) = 0.3$, $\mathbb{P}(C) = 0.2$. The expected drift under $\mathbb{P}$ is:

    $$
    \mathbb{E}^{\mathbb{P}}[X] = 0.5 \cdot 2 + 0.3 \cdot 1 + 0.2 \cdot (-1) = 1.0 + 0.3 - 0.2 = 1.1
    $$

    This is a positive drift. To achieve exactly zero drift under a new measure $\mathbb{Q}$, we need $\mathbb{Q}(A) \cdot 2 + \mathbb{Q}(B) \cdot 1 + \mathbb{Q}(C) \cdot (-1) = 0$ with $\mathbb{Q}(A) + \mathbb{Q}(B) + \mathbb{Q}(C) = 1$. Setting $\mathbb{Q}(C) = q$, $\mathbb{Q}(B) = b$, $\mathbb{Q}(A) = 1 - b - q$, the zero-drift condition gives $2 - b - 3q = 0$, or $b = 2 - 3q$. Choosing $q = 0.6$ yields $b = 0.2$ and $\mathbb{Q}(A) = 0.2$:

    $$
    \mathbb{E}^{\mathbb{Q}}[X] = 0.2 \cdot 2 + 0.2 \cdot 1 + 0.6 \cdot (-1) = 0.4 + 0.2 - 0.6 = 0
    $$

    No paths were added or removed — path A was downweighted from 0.5 to 0.2 and path C upweighted from 0.2 to 0.6.

---

**Exercise 6.**
You change measure from $\mathbb{P}$ to $\mathbb{Q}$ so that upward-trending paths are downweighted and downward-trending paths are upweighted. A colleague concludes: "Under $\mathbb{Q}$, the stock should go down in expectation." Explain precisely why this reasoning is wrong.

??? success "Solution to Exercise 6"
    The reasoning confuses "downweighting upward paths" with "making the stock decline." Under $\mathbb{Q}$, the stock's expected growth rate is $r$ (the risk-free rate), which is typically positive. The reweighting does not make the stock decline — it reduces the expected growth rate from $\mu$ (which includes a risk premium) to $r$ (which does not).

    Concretely, if $\mu = 10\%$ and $r = 3\%$, the Girsanov measure change downweights paths where the stock grew strongly (say at 15%) and upweights paths where it grew modestly or declined. The net effect is that the weighted average growth rate shifts from 10% to 3% — not to a negative number. The stock still grows in expectation under $\mathbb{Q}$, just at the risk-free rate.

    The key insight is that "downweighted" does not mean "removed" or "reversed." All paths retain positive probability under $\mathbb{Q}$ (since $\mathbb{P} \sim \mathbb{Q}$). The upward paths are still present — they simply contribute less to the weighted average, shifting the mean drift from $\mu$ to $r$.
