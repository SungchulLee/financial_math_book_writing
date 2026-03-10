# Dynkin's Formula


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

**Dynkin's formula** is the integral form of the infinitesimal generator — a **stochastic fundamental theorem of calculus**.

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

    A convenient sufficient condition: if $\mathcal{L}f$ is bounded on the state space and $\mathbb{E}_x[\tau] < \infty$, then the condition holds automatically, since

    $$\mathbb{E}_x\left[\int_0^\tau |(\mathcal{L}f)(X_s)|\,ds\right] \leq \|\mathcal{L}f\|_\infty \cdot \mathbb{E}_x[\tau] < \infty$$

    This covers all the examples below: in each case $\mathcal{L}f$ is a polynomial evaluated on a bounded domain, or the process has finite expected exit time.

---

## Intuition

| Classical FTC | Dynkin's Formula |
|---------------|------------------|
| $g(b) - g(a) = \int_a^b g'(x)\,dx$ | $\mathbb{E}_x[f(X_\tau)] - f(x) = \mathbb{E}_x\left[\int_0^\tau \mathcal{L}f\,ds\right]$ |
| Derivative $g'$ | Generator $\mathcal{L}$ |
| Endpoint $b$ | Stopping time $\tau$ |

---

## Proof

??? note "Via Itô's Lemma"

    **Step 1**: Apply Itô's lemma

    $$df(X_t) = (\mathcal{L}f)(X_t)\,dt + \sigma(X_t)f'(X_t)\,dW_t$$

    **Step 2**: Integrate $0 \to \tau$

    $$f(X_\tau) - f(x) = \int_0^\tau (\mathcal{L}f)(X_s)\,ds + \int_0^\tau \sigma f'\,dW_s$$

    **Step 3**: Take expectation (Itô integral vanishes)

    $$\mathbb{E}_x[f(X_\tau)] = f(x) + \mathbb{E}_x\left[\int_0^\tau (\mathcal{L}f)(X_s)\,ds\right]$$



---

## The Dynkin Martingale

$$M_t := f(X_t) - f(X_0) - \int_0^t (\mathcal{L}f)(X_s)\,ds$$

is a martingale. Dynkin's formula follows from optional stopping: $\mathbb{E}_x[M_\tau] = 0$.

---

## Examples

### Brownian Motion: E[X_τ]

| Item | Value |
|------|-------|
| Process | $dX_t = dW_t$ |
| Generator | $\mathcal{L}f = \frac{1}{2}f''$ |
| Function | $f(x) = x$ |
| $\mathcal{L}f$ | $0$ |

$$\mathbb{E}_x[X_\tau] = x + \mathbb{E}_x\left[\int_0^\tau 0\,ds\right] = x$$

---

### Brownian Motion: E[X_τ²]

| Item | Value |
|------|-------|
| Function | $f(x) = x^2$ |
| $\mathcal{L}f$ | $\frac{1}{2} \cdot 2 = 1$ |

$$\mathbb{E}_x[X_\tau^2] = x^2 + \mathbb{E}_x[\tau]$$

---

### Expected Hitting Time

**Problem**: BM starts at $x \in (a,b)$. Find $\mathbb{E}_x[\tau]$ where $\tau = \inf\{t: X_t \notin (a,b)\}$.

**Strategy**: Find $f$ with $\mathcal{L}f = -1$, i.e., $\frac{1}{2}f'' = -1$, so $f'' = -2$.

**Solution**: $f(x) = -x^2$ (linear terms may be added freely; they vanish in the final computation).

**Step 1 — Exit probabilities.** Since $X_t$ is a BM, it is a martingale, so $\mathbb{E}_x[X_\tau] = x$ by optional stopping. The process exits at $a$ or $b$ only, so:

$$\mathbb{P}_x(X_\tau = b) = \frac{x-a}{b-a}, \quad \mathbb{P}_x(X_\tau = a) = \frac{b-x}{b-a}$$

**Step 2 — Compute $\mathbb{E}_x[X_\tau^2]$.** Using the exit probabilities:

$$\mathbb{E}_x[X_\tau^2] = b^2 \cdot \frac{x-a}{b-a} + a^2 \cdot \frac{b-x}{b-a} = \frac{b^2(x-a) + a^2(b-x)}{b-a}$$

**Step 3 — Apply Dynkin with $f(x) = -x^2$**, where $\mathcal{L}f = \frac{1}{2}(-2) = -1$:

$$\mathbb{E}_x[-X_\tau^2] = -x^2 + \mathbb{E}_x\left[\int_0^\tau (-1)\,ds\right] = -x^2 - \mathbb{E}_x[\tau]$$

Therefore:

$$\mathbb{E}_x[\tau] = \mathbb{E}_x[X_\tau^2] - x^2 = \frac{b^2(x-a) + a^2(b-x)}{b-a} - x^2$$

Expanding and simplifying:

$$\mathbb{E}_x[\tau] = \frac{b^2 x - ab^2 + a^2 b - a^2 x - x^2(b-a)}{b-a} = \frac{(b^2 - a^2)(x) - ab(b-a) - x^2(b-a)}{b-a}$$

$$= (a+b)x - ab - x^2 = -(x^2 - (a+b)x + ab) = -(x-a)(x-b)$$

$$
\boxed{\mathbb{E}_x[\tau] = (x-a)(b-x)}
$$

!!! check "Verification"
    - $x = a$: $\mathbb{E}_a[\tau] = 0$ ✓
    - $x = b$: $\mathbb{E}_b[\tau] = 0$ ✓
    - Max at midpoint: $\mathbb{E}_{(a+b)/2}[\tau] = \frac{(b-a)^2}{4}$ ✓

---

### Ornstein–Uhlenbeck: E[X_t]

> **Note**: This example uses a fixed time $t$ rather than a stopping time $\tau$. Dynkin's formula applies to both — simply replace $\tau$ with a deterministic $t$.

| Item | Value |
|------|-------|
| Process | $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ |
| $\mathcal{L}f$ for $f(x)=x$ | $-\kappa x$ |

$$\mathbb{E}_x[X_t] = x - \kappa \int_0^t \mathbb{E}_x[X_s]\,ds$$

Setting $m(t) = \mathbb{E}_x[X_t]$: $m'(t) = -\kappa m(t)$

$$\boxed{m(t) = x e^{-\kappa t}}$$

---

### GBM: E[S_t]

| Item | Value |
|------|-------|
| Process | $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ |
| $\mathcal{L}f$ for $f(s)=s$ | $\mu s$ |

$$\mathbb{E}_{s_0}[S_t] = s_0 + \mu \int_0^t \mathbb{E}_{s_0}[S_u]\,du$$

$$\boxed{\mathbb{E}_{s_0}[S_t] = s_0 e^{\mu t}}$$

!!! note "Remark"
    This result can also be obtained directly from $S_t = s_0 e^{(\mu - \sigma^2/2)t + \sigma W_t}$ and taking expectations. The Dynkin derivation is more instructive as a method, showing how the ODE for $\mathbb{E}[S_t]$ emerges from the generator.

---

## Applications

| Problem | Choose $f$ such that | Result |
|---------|---------------------|--------|
| Expected hitting time | $\mathcal{L}f = -1$ | $\mathbb{E}_x[\tau] = f(x) - \mathbb{E}_x[f(X_\tau)]$ |
| Exit probability | $\mathcal{L}f = 0$ | $\mathbb{E}_x[f(X_\tau)] = f(x)$ |
| Moments | $f(x) = x^n$ | Recursion via $\mathcal{L}(x^n)$ |

---

## Dynkin vs Itô

### The Relationship

$$\boxed{\text{Dynkin} = \mathbb{E}[\text{Itô}]}$$

**Itô's formula** (pathwise): For $f \in C^2$:

$$f(X_t) = f(X_0) + \int_0^t \mathcal{L}f(X_s)\,ds + \underbrace{\int_0^t f'(X_s)\sigma(X_s)\,dW_s}_{\text{martingale}}$$

This identity holds **path by path**.

**Take expectations** (the only operation):

$$\mathbb{E}_x\left[\int_0^t f'(X_s)\sigma(X_s)\,dW_s\right] = 0$$

So:

$$\mathbb{E}_x[f(X_t)] = f(x) + \mathbb{E}_x\left[\int_0^t \mathcal{L}f(X_s)\,ds\right]$$

This *is* Dynkin's formula. No extra ideas were added. The stochastic integral simply disappeared because it is a martingale.

---

### What Disappears is Not Randomness, but Local Noise

- The **drift term** survives because it is systematic
- The **martingale term** disappears because it has **zero mean increment**

So Dynkin:

- keeps the **deterministic bias** of the dynamics
- throws away the **pathwise fluctuations**

| Itô | Dynkin |
|-----|--------|
| Sees paths | Sees laws |
| Tracks fluctuations | Tracks average evolution |
| Strong statement | Weak (distributional) statement |

---

### Stopping Times: Where Dynkin is Strictly Stronger

Itô's formula at a stopping time $\tau$ requires:

- localization
- careful justification
- pathwise control

Dynkin's formula:

$$\mathbb{E}_x[f(X_\tau)] = f(x) + \mathbb{E}_x\left[\int_0^\tau \mathcal{L}f(X_s)\,ds\right]$$

can hold under **weaker assumptions** in certain settings — for instance, for processes with jumps or weak solutions where pathwise Itô calculus breaks down. That said, Dynkin carries its own integrability requirement (see above), so neither formula is universally stronger. The key advantage of Dynkin is robustness when the path structure is unavailable or inconvenient.

So Dynkin is not just a corollary — it is **more robust in the settings that matter most**.

---

### Why Probabilists Care About Dynkin More Than Itô

- Itô lives at the **path level**
- Dynkin lives at the **law / generator level**
- Semigroups live at the **expectation operator level**

They form a strict hierarchy:

```
Itô (pathwise, strongest)
    ↓ average out martingale
Dynkin (expectations)
    ↓ abstract limit
Semigroup / generator
```

Once paths are gone (jumps, weak solutions), Itô disappears — Dynkin survives.

---

### Final Takeaway

!!! quote "The Slogan"
    **Itô explains how paths move.**
    
    **Dynkin explains how laws evolve.**
    
    **Dynkin is literally Itô with noise averaged out.**

- What is averaged out is **the martingale part**, not "information"
- Nothing essential for the law is lost

---

## See Also

- [Infinitesimal Generator](infinitesimal_generator.md)
- [Generator and Martingales](generator_and_martingales.md)
- [Applications of Dynkin](applications_of_dynkin.md)
- [Feynman–Kac Formula](../../ch05/feynman_kac/feynman_kac_formula.md)
