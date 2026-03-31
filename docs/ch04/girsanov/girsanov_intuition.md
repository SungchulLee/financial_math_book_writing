# Intuitive Introduction and Motivation


Girsanov’s theorem is one of the most important results in stochastic calculus,
yet it is often misunderstood at first encounter.

At an intuitive level, the theorem resolves a seeming paradox:

> *How can a stochastic process with drift become driftless, without changing its paths?*

The resolution lies in understanding the difference between **paths** and
**probability measures**.

---

## Paths vs Probability Measures


A stochastic process such as Brownian motion generates random paths

\[
\omega : [0,T] \to \mathbb{R}.
\]

A probability measure does not create new paths.
Instead, it assigns **weights** to these paths.

Changing the probability measure therefore:

- does **not** alter which paths are possible,
- but **does** change how likely each path is.

Drift is not a property of individual paths.
It is a property of how probabilities are distributed across paths.

---

## A Thought Experiment


Imagine observing many random paths over time.

Under one probability measure, paths that trend upward may be more likely.
Under another measure, those same paths may be downweighted.

From the perspective of averages:

- the first observer sees a **positive drift**,
- the second observer sees **no drift**.

The underlying paths are identical.
Only the probability weights have changed.

---

## Continuous-Time Perspective


Let \(W_t\) be Brownian motion under a measure \(\mathbb{P}\).
The process

\[
Y_t = W_t + \theta t
\]

has drift \(\theta\) under \(\mathbb{P}\).

Girsanov’s theorem answers the following question:

> *Is there another probability measure under which \(Y_t\) is a Brownian motion?*

The answer is yes.
The drift can be absorbed into the probability measure.

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

Everything that follows is a rigorous formulation of this idea.

---

## Exercises

**Exercise 1.**
Consider two observers watching the same set of stock price paths over one year. Observer A uses measure $\mathbb{P}$ and estimates a positive drift of 8%. Observer B uses measure $\mathbb{Q}$ and sees drift equal to the risk-free rate $r = 2\%$. Explain how both observers can be correct simultaneously, and describe what differs between their assessments.

---

**Exercise 2.**
Let $W_t$ be a standard Brownian motion under $\mathbb{P}$, and define $Y_t = W_t + 3t$. Under $\mathbb{P}$, compute $\mathbb{E}^{\mathbb{P}}[Y_t]$ and $\mathrm{Var}^{\mathbb{P}}(Y_t)$. Girsanov's theorem asserts there exists a measure $\mathbb{Q}$ under which $Y_t$ is a standard Brownian motion. Under $\mathbb{Q}$, what are $\mathbb{E}^{\mathbb{Q}}[Y_t]$ and $\mathrm{Var}^{\mathbb{Q}}(Y_t)$?

---

**Exercise 3.**
A skeptic argues: "If changing the probability measure does not change any sample paths, then it cannot possibly change the price of a derivative." Explain the flaw in this reasoning, using the concept that expected values (and hence prices computed as discounted expectations) depend on the measure.

---

**Exercise 4.**
Suppose you flip a biased coin with $\mathbb{P}(\text{Heads}) = 0.7$. Define a new measure $\mathbb{Q}$ with $\mathbb{Q}(\text{Heads}) = 0.5$. The sample space $\{\text{H}, \text{T}\}$ is the same under both measures. Compute the Radon-Nikodym derivative $d\mathbb{Q}/d\mathbb{P}$ on each outcome and verify that $\mathbb{E}^{\mathbb{P}}[d\mathbb{Q}/d\mathbb{P}] = 1$. Use this discrete example to illustrate the intuition behind Girsanov's theorem.

---

**Exercise 5.**
In the thought experiment of observing many random paths, suppose the first observer sees an average drift of $+5\%$ per year and the second observer sees an average drift of $0\%$. If both observe the same 10,000 simulated paths, explain how the second observer's probability weights must differ from the first's. Which paths receive higher weight under the second observer's measure?

---

**Exercise 6.**
The statement "drift lives in the probability measure, not in the paths" is the central idea. Provide a concrete numerical example: take a discrete random walk with three possible paths and show that by reassigning probabilities (without adding or removing paths), you can change the expected drift from positive to zero.

---

**Exercise 7.**
Explain why the Girsanov measure change preserves the volatility of the process. Specifically, if $Y_t = W_t + \theta t$ has the same quadratic variation as $W_t$ under both $\mathbb{P}$ and $\mathbb{Q}$, what does this imply about the "roughness" or "fluctuation" of the paths? Why is this property important for option pricing?

---

## Solutions

??? success "Solution to Exercise 1"
    Both observers are correct because they are using different probability measures to evaluate the same set of sample paths. Observer A, using the physical measure $\mathbb{P}$, assigns probabilities to paths that reflect real-world likelihoods. Under this weighting, the average growth rate of the stock is 8%. Observer B, using the risk-neutral measure $\mathbb{Q}$, reweights the same paths via a Radon-Nikodym derivative so that upward-trending paths receive less probability and downward-trending paths receive more. Under this reweighting, the average growth rate equals the risk-free rate $r = 2\%$.

    What differs is not the paths themselves but the probability weights assigned to them. Both observers see the exact same collection of possible price trajectories. Observer A's weighting reflects beliefs about real-world returns (incorporating risk premia), while Observer B's weighting is constructed so that discounted prices are martingales, enabling arbitrage-free pricing. Neither observer is wrong — they are answering different questions about the same probability space.

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

??? success "Solution to Exercise 3"
    The flaw in the skeptic's reasoning is that derivative prices are computed as **expected values** (specifically, discounted expected payoffs), and expected values depend on the probability measure. While the sample paths are the same under both $\mathbb{P}$ and $\mathbb{Q}$, the weights assigned to those paths differ.

    Consider a European call option with payoff $(S_T - K)^+$. Under $\mathbb{P}$, high stock price paths (where the option pays off handsomely) receive higher probability, since the stock has a positive risk premium $\mu > r$. Under $\mathbb{Q}$, those same high-return paths are downweighted.

    The pricing formula $C = e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T - K)^+]$ uses the risk-neutral expectation, which assigns different weights to the payoff across paths than $\mathbb{E}^{\mathbb{P}}[(S_T - K)^+]$ would. The change of measure does not change any individual path's payoff, but it changes the weighted average of those payoffs, and that weighted average is precisely the arbitrage-free price.

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

    This illustrates the key idea behind Girsanov's theorem: the Radon-Nikodym derivative reweights outcomes without changing the sample space. Under $\mathbb{P}$, heads is more likely (biased coin), so if we define "drift" as the expected value, there is a positive bias toward heads. Under $\mathbb{Q}$, the same outcomes exist but with equal probability (fair coin), removing the drift. The outcome $\text{H}$ (analogous to an upward-drifting path) is downweighted by $5/7 < 1$, while $\text{T}$ (a downward path) is upweighted by $5/3 > 1$. The continuous-time Girsanov theorem works identically: the Radon-Nikodym derivative $Z_T$ reweights paths so that a drifted process becomes driftless.

??? success "Solution to Exercise 5"
    The first observer assigns equal probability weights to all 10,000 paths (or weights consistent with the physical measure $\mathbb{P}$). Under these weights, the average drift is $+5\%$ per year, meaning paths that trend upward contribute more to the average.

    The second observer uses a different set of probability weights (corresponding to the measure $\mathbb{Q}$) so that the weighted average drift is $0\%$. To achieve this:

    - Paths that trend **downward** or stay flat must receive **higher** weight under $\mathbb{Q}$ than under $\mathbb{P}$.
    - Paths that trend **strongly upward** must receive **lower** weight under $\mathbb{Q}$.

    Specifically, the weight of each path $\omega$ is proportional to the Radon-Nikodym derivative $Z_T(\omega)$. For a process with drift $\mu > 0$ and constant volatility $\sigma$, the Girsanov kernel is $\theta = \mu/\sigma$, and the weight is $Z_T(\omega) = \exp(-\theta W_T(\omega) - \frac{1}{2}\theta^2 T)$. Paths where $W_T(\omega)$ is large and positive (those responsible for the upward drift) get exponentially downweighted by the factor $e^{-\theta W_T}$, while paths where $W_T(\omega)$ is negative get upweighted. The result is that the reweighted average drift is zero.

??? success "Solution to Exercise 6"
    Consider a discrete random walk over one period with three possible paths:

    - Path A: the walk goes up by $+2$
    - Path B: the walk goes up by $+1$
    - Path C: the walk goes down by $-1$

    Under measure $\mathbb{P}$, assign probabilities $\mathbb{P}(A) = 0.5$, $\mathbb{P}(B) = 0.3$, $\mathbb{P}(C) = 0.2$. The expected drift under $\mathbb{P}$ is:

    $$
    \mathbb{E}^{\mathbb{P}}[X] = 0.5 \cdot 2 + 0.3 \cdot 1 + 0.2 \cdot (-1) = 1.0 + 0.3 - 0.2 = 1.1
    $$

    This is a positive drift. Now define a new measure $\mathbb{Q}$ on the same three paths by choosing $\mathbb{Q}(A) = 0.1$, $\mathbb{Q}(B) = 0.2$, $\mathbb{Q}(C) = 0.7$. The expected drift under $\mathbb{Q}$ is:

    $$
    \mathbb{E}^{\mathbb{Q}}[X] = 0.1 \cdot 2 + 0.2 \cdot 1 + 0.7 \cdot (-1) = 0.2 + 0.2 - 0.7 = -0.3
    $$

    To get exactly zero drift, we need $\mathbb{Q}(A) \cdot 2 + \mathbb{Q}(B) \cdot 1 + \mathbb{Q}(C) \cdot (-1) = 0$ with $\mathbb{Q}(A) + \mathbb{Q}(B) + \mathbb{Q}(C) = 1$. One solution is $\mathbb{Q}(A) = 0.1$, $\mathbb{Q}(B) = 0.3$, $\mathbb{Q}(C) = 0.6$:

    $$
    \mathbb{E}^{\mathbb{Q}}[X] = 0.1 \cdot 2 + 0.3 \cdot 1 + 0.6 \cdot (-1) = 0.2 + 0.3 - 0.6 = -0.1
    $$

    Adjusting: choose $\mathbb{Q}(A) = 0.15$, $\mathbb{Q}(B) = 0.15$, $\mathbb{Q}(C) = 0.70$:

    $$
    \mathbb{E}^{\mathbb{Q}}[X] = 0.15 \cdot 2 + 0.15 \cdot 1 + 0.70 \cdot (-1) = 0.30 + 0.15 - 0.70 = -0.25
    $$

    Solving exactly: let $\mathbb{Q}(C) = q$, $\mathbb{Q}(B) = b$, $\mathbb{Q}(A) = 1 - b - q$. The zero-drift condition is $2(1-b-q) + b - q = 0$, giving $2 - b - 3q = 0$, or $b = 2 - 3q$. Choosing $q = 0.6$ gives $b = 0.2$ and $\mathbb{Q}(A) = 0.2$:

    $$
    \mathbb{E}^{\mathbb{Q}}[X] = 0.2 \cdot 2 + 0.2 \cdot 1 + 0.6 \cdot (-1) = 0.4 + 0.2 - 0.6 = 0
    $$

    No paths were added or removed. The upward path A was downweighted from 0.5 to 0.2, and the downward path C was upweighted from 0.2 to 0.6. This is exactly the discrete analogue of what Girsanov's theorem does in continuous time.

??? success "Solution to Exercise 7"
    The quadratic variation of $Y_t = W_t + \theta t$ is:

    $$
    \langle Y \rangle_t = \langle W + \theta \cdot \rangle_t = \langle W \rangle_t = t
    $$

    The deterministic drift term $\theta t$ has zero quadratic variation because it is a finite-variation process. Adding a finite-variation process to a semimartingale does not change its quadratic variation.

    Quadratic variation is a **pathwise** quantity — it is determined by the oscillations of the sample paths along any partition, and these oscillations are the same regardless of the probability measure. Since the paths under $\mathbb{P}$ and $\mathbb{Q}$ are identical (only their weights differ), the quadratic variation is the same: $\langle Y \rangle_t = t$ under both measures.

    This means the "roughness" or local fluctuation structure of the paths is identical under both measures. The paths have the same volatility, the same Hölder regularity, and the same local behavior.

    This is crucial for option pricing because **option prices depend primarily on volatility, not on drift**. The Black-Scholes formula, for instance, depends on $\sigma$ but not on $\mu$. The Girsanov measure change removes the drift (which encodes investor risk preferences and is difficult to estimate) while preserving the volatility (which is directly observable from market prices). This is why we can calibrate option pricing models to implied volatility without needing to estimate expected returns.
