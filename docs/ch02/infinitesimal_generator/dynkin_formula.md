# Dynkin's Formula

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
    Requires $\mathbb{E}_x\left[\int_0^\tau |(\mathcal{L}f)(X_s)|\,ds\right] < \infty$

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

### Brownian Motion: $\mathbb{E}_x[X_\tau]$

| Item | Value |
|------|-------|
| Process | $dX_t = dW_t$ |
| Generator | $\mathcal{L}f = \frac{1}{2}f''$ |
| Function | $f(x) = x$ |
| $\mathcal{L}f$ | $0$ |

$$\mathbb{E}_x[X_\tau] = x + \mathbb{E}_x\left[\int_0^\tau 0\,ds\right] = x$$

---

### Brownian Motion: $\mathbb{E}_x[X_\tau^2]$

| Item | Value |
|------|-------|
| Function | $f(x) = x^2$ |
| $\mathcal{L}f$ | $\frac{1}{2} \cdot 2 = 1$ |

$$\mathbb{E}_x[X_\tau^2] = x^2 + \mathbb{E}_x[\tau]$$

---

### Expected Hitting Time

**Problem**: BM starts at $x \in (a,b)$. Find $\mathbb{E}_x[\tau]$ where $\tau = \inf\{t: X_t \notin (a,b)\}$.

**Strategy**: Find $f$ with $\mathcal{L}f = -1$, i.e., $\frac{1}{2}f'' = -1$.

**Solution**: $f(x) = -x^2$

From $\mathbb{E}_x[X_\tau] = x$ (martingale property):

$$\mathbb{P}_x(X_\tau = b) = \frac{x-a}{b-a}, \quad \mathbb{P}_x(X_\tau = a) = \frac{b-x}{b-a}$$

Applying Dynkin with $f(x) = -x^2$:

$$\mathbb{E}_x[-X_\tau^2] = -x^2 - \mathbb{E}_x[\tau]$$

$$
\boxed{\mathbb{E}_x[\tau] = (x-a)(b-x)}
$$

!!! check "Verification"
    - $x = a$: $\mathbb{E}_a[\tau] = 0$ ✓
    - $x = b$: $\mathbb{E}_b[\tau] = 0$ ✓
    - Max at midpoint: $\mathbb{E}_{(a+b)/2}[\tau] = \frac{(b-a)^2}{4}$ ✓

---

### Ornstein–Uhlenbeck: $\mathbb{E}_x[X_t]$

| Item | Value |
|------|-------|
| Process | $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ |
| $\mathcal{L}f$ for $f(x)=x$ | $-\kappa x$ |

$$\mathbb{E}_x[X_t] = x - \kappa \int_0^t \mathbb{E}_x[X_s]\,ds$$

Setting $m(t) = \mathbb{E}_x[X_t]$: $m'(t) = -\kappa m(t)$

$$\boxed{m(t) = x e^{-\kappa t}}$$

---

### GBM: $\mathbb{E}[S_t]$

| Item | Value |
|------|-------|
| Process | $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ |
| $\mathcal{L}f$ for $f(s)=s$ | $\mu s$ |

$$\mathbb{E}_{s_0}[S_t] = s_0 + \mu \int_0^t \mathbb{E}_{s_0}[S_u]\,du$$

$$\boxed{\mathbb{E}_{s_0}[S_t] = s_0 e^{\mu t}}$$

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

often holds under **much weaker assumptions**.

So Dynkin is not just a corollary — it is **more robust**.

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
- [Feynman–Kac Formula](feynman_kac.md)
