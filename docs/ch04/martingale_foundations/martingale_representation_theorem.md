# Martingale Representation Theorem


The **Martingale Representation Theorem (MRT)** states that, under a Brownian filtration, every square–integrable martingale can be expressed as a stochastic integral with respect to the driving Brownian motion.

Rather than repeating basic definitions already covered in earlier chapters, this section focuses on:
- the precise statement of the theorem,
- its structural meaning,
- why it is fundamental for hedging and PDE connections,
- and how it fits into change-of-measure theory.

---

## Statement of the Theorem


Let \((\Omega, \mathcal{F}, \{\mathcal{F}_t\}, \mathbb{P})\) be a filtered probability space supporting a Brownian motion \(W_t\), and assume \(\{\mathcal{F}_t\}\) is the Brownian filtration (augmented).

### 1. Martingale Representation Theorem


If \(X_t\) is a square–integrable \(\mathcal{F}_t\)-martingale, then there exists a **unique** predictable process \(\phi_t\) such that


\[
X_t = X_0 + \int_0^t \phi_s \, dW_s,
\]



with

\[
\mathbb{E}\left[ \int_0^t \phi_s^2 \, ds \right] < \infty.
\]



Uniqueness is understood up to indistinguishability.

---

## Why This Is a Strong Result


This theorem asserts that:

- Brownian motion is the *only source of randomness* in its own filtration.
- Any martingale adapted to this filtration must be built entirely from Brownian increments.
- There are no “hidden” or orthogonal martingale components.

This property is often called the **predictable representation property (PRP)**.

---

## Proof Sketch (Structure, Not Full Details)


The proof relies on Hilbert–space ideas.

### 1. Step 1: Simple Integrands

For simple predictable processes, the stochastic integral is explicitly defined.

### 2. Step 2: Density

Simple predictable processes are dense in

\[
L^2(\Omega \times [0,T]).
\]



### 3. Step 3: Itô Isometry

The map

\[
\phi \mapsto \int_0^T \phi_s \, dW_s
\]


is an isometry:

\[
\mathbb{E}\left[\left(\int_0^T \phi_s dW_s\right)^2\right]
=
\mathbb{E}\left[\int_0^T \phi_s^2 ds\right].
\]



### 4. Step 4: Completion and Uniqueness

Completeness of the Hilbert space ensures existence, and the isometry implies uniqueness.

---

## Interpretation: Geometry of Martingales


The theorem shows that the space of square–integrable martingales is isomorphic to a subspace of

\[
L^2(\Omega \times [0,T]).
\]



Each martingale corresponds to a unique “direction” \(\phi_t\) along which Brownian noise is accumulated.

---

## Connection to Hedging and Black–Scholes


In a risk–neutral setting, discounted asset prices are martingales.
By the MRT:

- Any discounted contingent claim payoff can be represented as a stochastic integral.
- The integrand \(\phi_t\) is interpreted as the **hedging strategy**.
- Identifying \(\phi_t\) leads directly to the Black–Scholes PDE.

This is the mathematical statement of **market completeness** for Brownian models.

---

## Relation to Change of Measure


The Martingale Representation Theorem works *within* a fixed probability measure.
Girsanov’s theorem explains *how the Brownian motion itself changes* under a new measure.

Together, they provide:
- existence of an equivalent martingale measure (Girsanov),
- uniqueness of hedging strategies (MRT).

---

## Beyond the Basic Setting (Optional)


### 1. Clark–Ocone Formula

In Malliavin calculus, the integrand \(\phi_t\) can sometimes be written explicitly using conditional expectations of derivatives.

### 2. Incomplete Markets

With multiple sources of randomness, martingales may admit only partial representations, leading to orthogonal decompositions (Kunita–Watanabe).

---

## Summary


- MRT characterizes all square–integrable martingales in a Brownian filtration.
- It formalizes the idea that Brownian motion generates all randomness.
- It underpins hedging, PDE connections, and modern financial mathematics.
