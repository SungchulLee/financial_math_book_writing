# Chapter 2: Stochastic Processes

The central idea of this chapter is that **randomness, when combined with information,
produces structure**. We build stochastic processes in three stages:

$$
\text{discrete models}
\;\rightarrow\;
\text{continuous limit}
\;\rightarrow\;
\text{information and structure}
$$

---

## Roadmap

| Section | Role | Topics |
|---------|------|--------|
| 2.1 Simple Random Walk | Discrete engine | moments, martingales, recurrence, scaling, Donsker |
| 2.2 Brownian Motion | Continuous limit | definition, path properties, quadratic variation, hitting times |
| 2.3 Filtration and Martingales | Information + structure | filtrations, martingales, stopping times, inequalities, convergence |

---

## Key Structure

### 1. Simple Random Walk → Discrete Foundation

The simple random walk

$$
S_n = \sum_{i=1}^n X_i
$$

provides the fundamental model of accumulated randomness. This section develops:

- algebraic structure (moments, MGF)
- martingale structure
- long-run behavior (recurrence)
- scaling limits

The key result is Donsker's theorem:

$$
\frac{S_{\lfloor nt \rfloor}}{\sqrt{n}} \;\Rightarrow\; W_t
$$

which explains the emergence of Brownian motion from discrete randomness.

---

### 2. Brownian Motion → Continuous Model

Brownian motion is the continuous-time limit of random walks, characterized by:

- Gaussian independent increments
- continuous paths

Its structure is developed through:

- scaling and self-similarity
- path roughness (non-differentiability)
- quadratic variation
- symmetry and hitting behavior

This section provides the **geometric and probabilistic structure** of continuous
randomness.

---

### 3. Filtration and Martingale → Information and Dynamics

A filtration $(\mathcal{F}_t)$ describes the flow of information. Martingale is a
processe that evolve without predictable drift:

$$
\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s
$$

This section develops:

- conditional expectation (prediction)
- adapted process (information consistency)
- stopping time (random horizons)
- inequalities and convergence
- structural decomposition (Doob–Meyer)

These tools form the foundation for pricing and stochastic calculus.

---

## Conceptual Flow

```mermaid
flowchart LR
A[Random Walk]
--> B[Scaling Limit]
--> C[Brownian Motion]
--> D[Filtration]
--> E[Martingales]
```

---

!!! note "Role in the Book"
    This chapter provides the foundation for:

    - Itô calculus (Chapter 3)
    - change of measure (Chapter 4)
    - PDE connections (Chapter 5)
