# Dynkin's Formula

**Dynkin's formula** is the integral form of the infinitesimal generator — a stochastic fundamental theorem of calculus.

$$
\boxed{
\mathbb{E}_x[f(X_\tau)] = f(x) + \mathbb{E}_x\left[\int_0^\tau (\mathcal{L}f)(X_s)\,ds\right]
}
$$

---

## Setup

For the diffusion $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$ with generator:

$$\mathcal{L}f = \mu f' + \frac{\sigma^2}{2}f''$$

and stopping time $\tau$ with $\mathbb{E}_x[\tau] < \infty$.

!!! warning "Integrability Condition"
    Requires $\mathbb{E}_x\left[\int_0^\tau |(\mathcal{L}f)(X_s)|\,ds\right] < \infty$.

    A convenient sufficient condition: if $\mathcal{L}f$ is bounded on the state space and $\mathbb{E}_x[\tau] < \infty$, then

    $$\mathbb{E}_x\left[\int_0^\tau |(\mathcal{L}f)(X_s)|\,ds\right] \leq \|\mathcal{L}f\|_\infty \cdot \mathbb{E}_x[\tau] < \infty$$

    This covers all examples below: in each case $\mathcal{L}f$ is a polynomial on a bounded domain, or the process has finite expected exit time.

---

## Intuition

| Classical FTC | Dynkin's Formula |
|---------------|------------------|
| $g(b) - g(a) = \int_a^b g'(x)\,dx$ | $\mathbb{E}_x[f(X_\tau)] - f(x) = \mathbb{E}_x\left[\int_0^\tau \mathcal{L}f\,ds\right]$ |
| Derivative $g'$ | Generator $\mathcal{L}$ |
| Endpoint $b$ | Stopping time $\tau$ |

---

## Proof

??? abstract "Via Itô's Lemma"

    **Step 1**: Apply Itô's lemma

    $$df(X_t) = (\mathcal{L}f)(X_t)\,dt + \sigma(X_t)f'(X_t)\,dW_t$$

    **Step 2**: Integrate $0 \to \tau$

    $$f(X_\tau) - f(x) = \int_0^\tau (\mathcal{L}f)(X_s)\,ds + \int_0^\tau \sigma f'\,dW_s$$

    **Step 3**: Take expectation (Itô integral vanishes under the integrability condition)

    $$\mathbb{E}_x[f(X_\tau)] = f(x) + \mathbb{E}_x\left[\int_0^\tau (\mathcal{L}f)(X_s)\,ds\right] \qquad \square$$

---

## The Dynkin Martingale

$$M_t := f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,ds$$

is a local martingale. Dynkin's formula follows from optional stopping: $\mathbb{E}_x[M_\tau] = 0$.

See [Generator and Martingales](generator_and_martingales.md) for the full development.

---

## Examples

### Brownian Motion: $\mathbb{E}[X_\tau]$

| Item | Value |
|------|-------|
| Process | $dX_t = dW_t$ |
| Generator | $\mathcal{L}f = \frac{1}{2}f''$ |
| Function | $f(x) = x$, so $\mathcal{L}f = \frac{1}{2} \cdot 0 = 0$ |

$$\mathbb{E}_x[X_\tau] = x + \mathbb{E}_x\left[\int_0^\tau 0\,ds\right] = x$$

---

### Brownian Motion: $\mathbb{E}[X_\tau^2]$

| Item | Value |
|------|-------|
| Function | $f(x) = x^2$, so $\mathcal{L}f = \frac{1}{2} \cdot 2 = 1$ |

$$\mathbb{E}_x[X_\tau^2] = x^2 + \mathbb{E}_x[\tau]$$

---

### Expected Exit Time from $(a, b)$

**Problem**: BM starts at $x \in (a,b)$. Find $\mathbb{E}_x[\tau]$ where $\tau = \inf\{t: X_t \notin (a,b)\}$.

**Strategy**: We need $\mathcal{L}f = -1$ so that $\mathbb{E}_x[\int_0^\tau \mathcal{L}f\,ds] = -\mathbb{E}_x[\tau]$. Taking $f(x) = -x^2$:

$$\mathcal{L}f = \frac{1}{2}f'' = \frac{1}{2}(-2) = -1 \checkmark$$

**Step 1 — Exit probabilities.** Since BM is a martingale, $\mathbb{E}_x[X_\tau] = x$ by optional stopping. The process exits only at $a$ or $b$:

$$\mathbb{P}_x(X_\tau = b) = \frac{x-a}{b-a}, \qquad \mathbb{P}_x(X_\tau = a) = \frac{b-x}{b-a}$$

**Step 2 — Compute $\mathbb{E}_x[X_\tau^2]$.** Using the exit probabilities:

$$\mathbb{E}_x[X_\tau^2] = b^2 \cdot \frac{x-a}{b-a} + a^2 \cdot \frac{b-x}{b-a} = \frac{b^2(x-a) + a^2(b-x)}{b-a}$$

**Step 3 — Apply Dynkin with $f(x) = -x^2$**:

$$\mathbb{E}_x[-X_\tau^2] = -x^2 - \mathbb{E}_x[\tau]$$

Therefore:

$$\mathbb{E}_x[\tau] = \mathbb{E}_x[X_\tau^2] - x^2 = \frac{b^2(x-a) + a^2(b-x)}{b-a} - x^2$$

Expanding: numerator $= b^2 x - ab^2 + a^2 b - a^2 x - x^2(b-a)$, so dividing by $(b-a)$:

$$= (a+b)x - ab - x^2 = -(x^2 - (a+b)x + ab) = -(x-a)(x-b)$$

$$
\boxed{\mathbb{E}_x[\tau] = (x-a)(b-x)}
$$

!!! check "Verification"
    - $x = a$: $\mathbb{E}_a[\tau] = 0$ $\checkmark$
    - $x = b$: $\mathbb{E}_b[\tau] = 0$ $\checkmark$
    - Max at midpoint: $\mathbb{E}_{(a+b)/2}[\tau] = \frac{(b-a)^2}{4}$ $\checkmark$

!!! note "Ownership"
    The PDE derivation of this same result (via the Poisson equation $\frac{1}{2}u'' = -1$) appears in [Applications of Dynkin](applications_of_dynkin.md). The two approaches are equivalent; this page derives it directly from the formula.

---

### Ornstein–Uhlenbeck: $\mathbb{E}[X_t]$

> **Note**: This example uses a fixed time $t$ rather than a stopping time $\tau$. Dynkin's formula applies to both — simply replace $\tau$ with a deterministic $t$.

| Item | Value |
|------|-------|
| Process | $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ |
| $\mathcal{L}f$ for $f(x)=x$ | $-\kappa x \cdot 1 + \frac{\sigma^2}{2} \cdot 0 = -\kappa x$ |

$$\mathbb{E}_x[X_t] = x - \kappa \int_0^t \mathbb{E}_x[X_s]\,ds$$

Setting $m(t) = \mathbb{E}_x[X_t]$: $m'(t) = -\kappa m(t)$, giving:

$$\boxed{m(t) = x e^{-\kappa t}}$$

---

### GBM: $\mathbb{E}[S_t]$

> **Note**: As above, $t$ is a deterministic time.

| Item | Value |
|------|-------|
| Process | $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ |
| $\mathcal{L}f$ for $f(s)=s$ | $\mu s \cdot 1 + \frac{\sigma^2 s^2}{2} \cdot 0 = \mu s$ |

$$\mathbb{E}_{s_0}[S_t] = s_0 + \mu \int_0^t \mathbb{E}_{s_0}[S_u]\,du \implies \boxed{\mathbb{E}_{s_0}[S_t] = s_0 e^{\mu t}}$$

!!! note "Remark"
    This result follows more quickly from $S_t = s_0 e^{(\mu - \sigma^2/2)t + \sigma W_t}$ directly. The Dynkin derivation is instructive as a method, showing how the ODE for $\mathbb{E}[S_t]$ emerges from the generator.

---

## Applications

| Problem | Choose $f$ such that | Result |
|---------|---------------------|--------|
| Expected hitting time | $\mathcal{L}f = -1$ | $\mathbb{E}_x[\tau] = f(x) - \mathbb{E}_x[f(X_\tau)]$ |
| Exit probability | $\mathcal{L}f = 0$ | $\mathbb{E}_x[f(X_\tau)] = f(x)$ |
| $n$-th moment of BM | $f(x) = x^n$, $\mathcal{L}f = \frac{n(n-1)}{2}x^{n-2}$ (BM only) | $\mathbb{E}_x[X_\tau^n] = x^n + \frac{n(n-1)}{2}\mathbb{E}_x\!\left[\int_0^\tau X_s^{n-2}\,ds\right]$ |

The moments row gives a **recursion for BM**: $\mathbb{E}_x[X_\tau^n]$ depends on $\mathbb{E}_x[\int_0^\tau X_s^{n-2}\,ds]$, computable from lower-order results. For $n=2$: $\mathbb{E}_x[X_\tau^2] = x^2 + \mathbb{E}_x[\tau]$ (recovered above). For other processes, replace $\mathcal{L}(x^n)$ with the appropriate generator applied to $x^n$.

For a systematic treatment, see [Applications of Dynkin](applications_of_dynkin.md).

---

## Dynkin vs Itô

### The Relationship

$$\boxed{\text{Dynkin} = \mathbb{E}[\text{Itô}]}$$

**Itô's formula** (pathwise): for $f \in C^2$:

$$f(X_t) = f(X_0) + \int_0^t (\mathcal{L}f)(X_s)\,ds + \underbrace{\int_0^t f'(X_s)\sigma(X_s)\,dW_s}_{\text{martingale, zero mean}}$$

**Taking expectations** — the Itô integral vanishes:

$$\mathbb{E}_x[f(X_t)] = f(x) + \mathbb{E}_x\left[\int_0^t (\mathcal{L}f)(X_s)\,ds\right]$$

This *is* Dynkin's formula. The stochastic integral disappears because it has zero mean.

### What Each Formula Sees

| | Itô | Dynkin |
|---|-----|--------|
| Level | Paths | Laws (distributions) |
| Tracks | Fluctuations | Average evolution |
| Statement type | Strong (pathwise) | Weak (distributional) |
| Survives jumps / weak solutions | No | Yes |

The drift term survives in Dynkin because it is systematic; the martingale term disappears because it has zero-mean increments. Nothing essential for computing expectations is lost.

### The Hierarchy

| Level | Object | What it captures |
|-------|--------|-----------------|
| Strongest | Itô's formula | Full pathwise dynamics |
| Average out martingale | Dynkin's formula | Expected evolution |
| Abstract limit | Semigroup / generator | Infinitesimal operator |

Once the path structure is gone (jump processes, weak solutions), Itô disappears — Dynkin survives.

!!! abstract "The Slogan"
    **Itô explains how paths move.**

    **Dynkin explains how laws evolve.**

    **Dynkin is Itô with the noise averaged out.**

---

## See Also

- [Infinitesimal Generator](infinitesimal_generator.md)
- [Generator and Martingales](generator_and_martingales.md)
- [Applications of Dynkin](applications_of_dynkin.md)
- [Feynman–Kac Formula](../../ch05/feynman_kac/feynman_kac_formula.md)

---

## Exercises

**Exercise 1.** Let $X_t$ be standard Brownian motion starting at $x \in (0, b)$ and let $\tau = \inf\{t : X_t \notin (0, b)\}$. Use Dynkin's formula with $f(x) = x^3$ to express $\mathbb{E}_x[X_\tau^3]$ in terms of $x$ and $\mathbb{E}_x[\int_0^\tau X_s\,ds]$. (Hint: compute $\mathcal{L}(x^3)$ for the BM generator $\mathcal{L} = \frac{1}{2}\partial_{xx}$.)

---

**Exercise 2.** For Brownian motion on $(a, b)$, use the exit probabilities

$$
\mathbb{P}_x(X_\tau = b) = \frac{x - a}{b - a}, \qquad \mathbb{P}_x(X_\tau = a) = \frac{b - x}{b - a}
$$

and Dynkin's formula with $f(x) = x^4$ to show that

$$
\mathbb{E}_x\!\left[\int_0^\tau X_s^2\,ds\right] = \frac{1}{6}\left[\frac{a^4(b-x) + b^4(x-a)}{b-a} - x^4\right]
$$

(Hint: $\mathcal{L}(x^4) = 6x^2$ for BM.)

---

**Exercise 3.** Consider the Ornstein--Uhlenbeck process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ with $X_0 = x_0$. Applying Dynkin's formula with $f(x) = x^2$ and a deterministic time $t$, derive an integral equation for $\mathbb{E}_{x_0}[X_t^2]$. Solve the resulting ODE to obtain

$$
\mathbb{E}_{x_0}[X_t^2] = x_0^2 e^{-2\kappa t} + \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})
$$

---

**Exercise 4.** Explain why Dynkin's formula cannot be directly applied to compute $\mathbb{E}_x[e^{-\lambda \tau}]$ for a stopping time $\tau$ and $\lambda > 0$. What goes wrong if you try to find $f$ such that $\mathcal{L}f = -\lambda f$ and apply the standard Dynkin framework? Which formula provides the correct framework instead?

---

**Exercise 5.** Let $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ (GBM) with $S_0 = s_0$. Apply Dynkin's formula with $f(s) = \ln s$ and a deterministic time $t$ to compute $\mathbb{E}_{s_0}[\ln S_t]$. Verify your answer against the known distribution of $\ln S_t$.

---

**Exercise 6.** Let $X_t$ be BM on $(a, b)$ and $\tau$ the exit time. Suppose $g$ is a $C^2$ function with $\mathcal{L}g = 0$ (i.e., $g$ is harmonic). Use Dynkin's formula to show that

$$
\mathbb{E}_x[g(X_\tau)] = g(x)
$$

What are the harmonic functions for BM, and how does this result relate to the exit probabilities $\mathbb{P}_x(X_\tau = b) = \frac{x-a}{b-a}$?

---

**Exercise 7.** Consider the hierarchy: Ito's formula $\to$ Dynkin's formula $\to$ semigroup/generator.

(a) Starting from Ito's lemma for $f(X_t)$ where $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$, show explicitly how taking expectations yields Dynkin's formula.

(b) Give an example of a process (e.g., a jump process or weak solution) for which Dynkin's formula applies but Ito's pathwise formula does not. Explain why the stochastic integral term is not needed at the Dynkin level.
