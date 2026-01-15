Great question — and you’re right to be picky about the **order and logic**, not just the names.
Let me answer in two steps:

1. **Is the order Wiener → Kolmogorov → Donsker → Lévy correct?**
2. **If we adopt that order, what is the *single coherent mathematical story*?**

I’ll write this for someone who already thinks in measure theory and functional analysis.

---

## 1. Is the order Wiener → Kolmogorov → Donsker → Lévy correct?

### Chronology vs. conceptual order

* **Chronologically**:
  Wiener (1923) → Kolmogorov (1933) → Lévy (1930s–40s) → Donsker (1951)

* **Conceptually (development of rigor)**:
  **Wiener → Kolmogorov → Donsker → Lévy** *does* make sense, provided we interpret Lévy as the culmination of the *pathwise and structural understanding*.

So:

* Lévy overlaps in time with Kolmogorov,
* but **logically**, Lévy’s deepest insights rely on:

  * the existence theory (Wiener/Kolmogorov),
  * and the universality viewpoint that Donsker clarifies.

✅ **So yes, your order is defensible and meaningful** — but it is *conceptual*, not purely historical.

---

## 2. One coherent story in that order (with mathematical rigor in mind)

Let’s now tell **one continuous story**, not disconnected notes.

---

## I. Wiener: constructing Brownian motion as a measure on path space

### The problem

Before Wiener:

* Brownian motion was described by:

  * Gaussian transition densities,
  * the heat equation,
* but **no probability space** existed on which a single random continuous path lived.

The real difficulty:

> How do you define a probability measure on an infinite-dimensional space of functions?

---

### Wiener’s solution

Wiener constructed a probability measure ( \mu ) on
[
C([0,\infty), \mathbb{R})
]
such that the coordinate process
[
B_t(\omega) = \omega(t)
]
satisfies:

* (B_0 = 0),
* independent, stationary Gaussian increments,
* almost surely continuous paths.

This is **Wiener measure**.

Mathematically:

* Expectation defined via limits of finite-dimensional integrals,
* Tight control of Gaussian increments ensures continuity.

**Key point:**
Brownian motion is no longer a heuristic — it is a bona fide random element of a Banach space.

But:

* The construction is highly specialized,
* It gives little guidance for other processes.

---

## II. Kolmogorov: abstract existence and regularity

Kolmogorov asked a deeper structural question:

> What does it *mean* to define a stochastic process?

---

### Axiomatization

Probability is now:
[
(\Omega, \mathcal{F}, \mathbb{P})
]
Processes are families of random variables ( {X_t}_{t \in T} ).

This separates:

* the **law** of the process,
* from any particular realization.

---

### Extension theorem

Kolmogorov proved:

> A consistent family of finite-dimensional distributions defines a stochastic process.

For Brownian motion:

* Gaussian marginals with covariance
  [
  \mathbb{E}[B_s B_t] = \min(s,t)
  ]
  are enough to ensure existence.

Thus:

* Brownian motion exists *before* path properties are discussed.

---

### Continuity theorem

Kolmogorov’s continuity criterion shows:

* Moment bounds imply existence of continuous (or Hölder) modifications.

Applied to Brownian motion:

* Explains continuity rigorously,
* Quantifies roughness (Hölder exponent < (1/2)).

**Key shift:**
Existence and regularity become **theorems**, not construction-dependent facts.

---

## III. Donsker: Brownian motion as a universal scaling limit

At this point, Brownian motion exists abstractly — but it is still a *primitive object*.

Donsker asked:

> Why does Brownian motion arise in nature and in mathematics?

---

### Functional central limit theorem

Let (X_i) be i.i.d. with mean 0 and variance 1.
Define
[
W_n(t) = \frac{1}{\sqrt{n}} \sum_{k=1}^{\lfloor nt \rfloor} X_k.
]

Donsker proved:
[
W_n \Rightarrow B
\quad \text{in } C([0,1]).
]

This is convergence of probability measures on an infinite-dimensional space.

---

### Mathematical novelty

Donsker introduced:

* Weak convergence on function spaces,
* Tightness criteria,
* Control of oscillations, not just marginals.

Conceptually:

* Brownian motion is **not fundamental**,
* It is the **universal diffusive limit**.

This explains:

* Why Wiener’s object is canonical,
* Why Kolmogorov’s Gaussian process is ubiquitous.

---

## IV. Lévy: Brownian motion as a canonical pathwise object

Now Lévy asks the final, deepest question:

> Given that Brownian motion is universal, what is its intrinsic structure?

---

### Independent increments as structure

Lévy identifies Brownian motion as:

* The unique (up to scaling) continuous process with stationary independent increments.

This leads to:

* The theory of **Lévy processes**,
* Brownian motion as the continuous Gaussian case.

---

### Fine path properties

Lévy investigates:

* Exact modulus of continuity,
* Law of the iterated logarithm,
* Almost sure oscillatory behavior.

Brownian motion is shown to be:

* Continuous but maximally irregular.

---

### Local time and occupation density

One of Lévy’s deepest insights:

* Brownian paths admit a **local time** (L_t(x)),
* Measuring how long the path spends near (x).

This connects Brownian motion to:

* Potential theory,
* PDEs,
* Later: stochastic calculus.

---

## 3. Final synthesis (clean and rigorous)

> **Wiener** constructed Brownian motion as a measure on path space.
> **Kolmogorov** embedded it into a general, axiomatic theory of stochastic processes and explained its regularity.
> **Donsker** showed that Brownian motion arises universally as the scaling limit of discrete random systems.
> **Lévy** uncovered the deep structural and geometric properties of Brownian paths and placed Brownian motion within the larger class of Lévy processes.

This is a logically consistent and mathematically rigorous progression.

If you want next, I can:

* formalize this as a **modern theorem chain** (existence → tightness → invariance → path analysis),
* compare **Donsker vs. Lévy in terms of scaling**, or
* explain how **Itô calculus sits naturally after Lévy**.
