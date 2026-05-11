# Ito Integration

This section builds the Ito integral from scratch — starting from the failure of classical calculus for Brownian motion and arriving at a rigorous framework for integrating against stochastic processes.

The entire construction is driven by a single fact:

$$
(\Delta B)^2 \sim \Delta t
$$

Brownian increments have non-vanishing quadratic variation. This forces a fundamentally different notion of integration and produces the correction terms that distinguish stochastic calculus from ordinary calculus.

---

## Section Roadmap

The pages in this section follow a deliberate progression from motivation through construction to consequences. Each concept has exactly one **canonical home** — other pages reference rather than re-derive.

### Quadratic Variation — why classical calculus fails

Canonical home for $[W]_t = t$, the conceptual break that forces a new theory of integration.

### High School Integral — the baseline

The ordinary time integral reviewed as a pathwise object. Establishes the baseline: everything works because the integrator is smooth.

### Ito Integral (Intuitive) — what we are trying to define

Left-endpoint sums, non-anticipation, and the trading interpretation. No proofs — just the target object and its financial meaning.

### Construction of the Ito Integral — the rigorous definition

The proof hub: simple processes, Ito isometry proof, $L^2$ extension, first martingale proof. Canonical home for the formal definition.

### Ito Isometry — why the construction is stable

Hilbert space and orthogonality interpretation of the isometry. Conceptual meaning, not a second proof.

### Properties of Ito Integrals — what we get for free

Clean statement of consequences: martingale property, continuity, quadratic variation, linearity. References proofs to the construction page.

### Ito Processes — putting drift and diffusion together

Drift plus diffusion decomposition. The general framework for modeling asset prices, preparing the ground for Ito's formula.

### Stratonovich Integral — the alternative definition

Midpoint evaluation, classical chain rule, conversion formulas. The alternative convention with different trade-offs.

---

## Conceptual Flow

The logical dependencies between pages form a clear pipeline:

!!! tip "Transitions"

    - **After High School Integral**: Everything works because $ds$ is smooth. For Brownian motion, this fails due to quadratic variation.
    - **After Quadratic Variation**: The non-vanishing of $[W]_t$ forces a new definition of integration — one that respects the roughness of Brownian paths.
    - **After Intuitive Ito**: We know *what* the integral should be. The construction page makes this rigorous.
    - **After Construction**: The Ito isometry explains *why* the $L^2$ extension is well-defined and stable.
    - **After Properties**: The integral is now a complete tool. Combining it with a drift term gives Ito processes, the general building block for SDEs.
    - **After Ito Processes**: The Stratonovich integral provides an alternative convention with different trade-offs.

---

## Role in the Chapter

The Ito integral is the **primitive object** of stochastic calculus. Everything later in the book treats it as given and extends it in specific directions:

- **Section 3.3 (Ito's Formula)** — transforms Ito integrals via the chain rule with quadratic variation corrections
- **Section 3.4 (SDEs)** — uses Ito integrals as the solution space for stochastic differential equations
- **Section 3.5 (Infinitesimal Generator)** — extracts the local drift and diffusion of Ito processes
- **Chapter 4 (Girsanov)** — uses stochastic exponentials of Ito integrals to construct new probability measures

One concept, one identity, everything else references it: the isometry is the single fact that makes the whole theory stable, and $(\Delta B)^2 \sim \Delta t$ is the single fact that forces the theory to exist.
