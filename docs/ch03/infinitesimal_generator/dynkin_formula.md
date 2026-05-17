# Dynkin's Formula

**Dynkin's formula** is obtained by taking expectations in the
[fundamental decomposition](infinitesimal_generator.md#the-fundamental-decomposition),
where the martingale term $M_t$ vanishes. It is the central tool for computing
expectations of diffusion processes without solving SDEs.

$$
\boxed{
\mathbb{E}_x[f(X_\tau)] = f(x) + \mathbb{E}_x\left[\int_0^\tau (\mathcal{L}f)(X_s)\,ds\right]
}
$$

---

## Setup

Recall (see [§ Generator of a Diffusion Process](infinitesimal_generator.md#generator-of-a-diffusion-process)): for the diffusion $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$, the generator is $\mathcal{L}f = \mu f' + \tfrac{\sigma^2}{2}f''$.

We fix a stopping time $\tau$ with $\mathbb{E}_x[\tau] < \infty$.

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

??? abstract "From the Fundamental Decomposition"

    Apply the
    [fundamental decomposition](infinitesimal_generator.md#the-fundamental-decomposition)
    at time $\tau$:

    $$f(X_\tau) = f(x) + \int_0^\tau (\mathcal{L}f)(X_s)\,ds + M_\tau$$

    Taking expectations and using $\mathbb{E}[M_\tau] = 0$ (the Itô integral has zero
    mean under the integrability condition) gives Dynkin's formula. $\square$

---

## The Dynkin Martingale

Recall (see [§ The Dynkin Martingale](generator_and_martingales.md#the-dynkin-martingale)): the martingale term $M_t$ in the decomposition is precisely the Itô integral $\int_0^t f'(X_s)\sigma(X_s)\,dW_s$. Dynkin's formula then follows from optional stopping applied to $M_t$.

---

## Examples

### Brownian Motion: 𝔼[Xτ]

| Item | Value |
|------|-------|
| Process | $dX_t = dW_t$ |
| Generator | $\mathcal{L}f = \frac{1}{2}f''$ |
| Function | $f(x) = x$, so $\mathcal{L}f = \frac{1}{2} \cdot 0 = 0$ |

$$\mathbb{E}_x[X_\tau] = x + \mathbb{E}_x\left[\int_0^\tau 0\,ds\right] = x$$

---

### Brownian Motion: 𝔼[Xτ²]

| Item | Value |
|------|-------|
| Function | $f(x) = x^2$, so $\mathcal{L}f = \frac{1}{2} \cdot 2 = 1$ |

$$\mathbb{E}_x[X_\tau^2] = x^2 + \mathbb{E}_x[\tau]$$

---

### Expected Exit Time from (a, b)

**Problem**: BM starts at $x \in (a,b)$. Find $\mathbb{E}_x[\tau]$ where $\tau = \inf\{t: X_t \notin (a,b)\}$.

**Strategy**: We need $\mathcal{L}f = -1$ so that $\mathbb{E}_x[\int_0^\tau \mathcal{L}f\,ds] = -\mathbb{E}_x[\tau]$. Taking $f(x) = -x^2$:

$$\mathcal{L}f = \frac{1}{2}f'' = \frac{1}{2}(-2) = -1 \checkmark$$

**Step 1 — Exit probabilities.** Recall (see [§ Hitting b Before a (Brownian Motion)](applications_of_dynkin.md#hitting-b-before-a-brownian-motion)):

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

!!! success "Verification"

    - $x = a$: $\mathbb{E}_a[\tau] = 0$ $\checkmark$
    - $x = b$: $\mathbb{E}_b[\tau] = 0$ $\checkmark$
    - Max at midpoint: $\mathbb{E}_{(a+b)/2}[\tau] = \frac{(b-a)^2}{4}$ $\checkmark$

!!! note "Ownership"
    The PDE derivation of this same result (via the Poisson equation $\frac{1}{2}u'' = -1$) appears in [Applications of Dynkin](applications_of_dynkin.md). The two approaches are equivalent; this page derives it directly from the formula.

---

### Ornstein–Uhlenbeck: 𝔼[Xₜ]

> **Note**: This example uses a fixed time $t$ rather than a stopping time $\tau$. Dynkin's formula applies to both — simply replace $\tau$ with a deterministic $t$.

| Item | Value |
|------|-------|
| Process | $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ |
| $\mathcal{L}f$ for $f(x)=x$ | $-\kappa x \cdot 1 + \frac{\sigma^2}{2} \cdot 0 = -\kappa x$ |

$$\mathbb{E}_x[X_t] = x - \kappa \int_0^t \mathbb{E}_x[X_s]\,ds$$

Setting $m(t) = \mathbb{E}_x[X_t]$: $m'(t) = -\kappa m(t)$, giving:

$$\boxed{m(t) = x e^{-\kappa t}}$$

---

### GBM: 𝔼[Sₜ]

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

Recall (see [§ The Fundamental Decomposition](infinitesimal_generator.md#the-fundamental-decomposition)): Itô's formula gives the pathwise identity

$$f(X_t) = f(X_0) + \int_0^t (\mathcal{L}f)(X_s)\,ds + M_t$$

where $M_t$ is a martingale. Taking expectations kills $M_t$ and Dynkin's formula falls out.

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

??? success "Solution to Exercise 1"
    The BM generator is $\mathcal{L}f = \frac{1}{2}f''$. For $f(x) = x^3$:

    - $f'(x) = 3x^2$, $f''(x) = 6x$

    $$
    \mathcal{L}(x^3) = \frac{1}{2}\cdot 6x = 3x
    $$

    Applying Dynkin's formula with $\tau$ being the exit time from $(0, b)$:

    $$
    \mathbb{E}_x[X_\tau^3] = x^3 + \mathbb{E}_x\!\left[\int_0^\tau 3X_s\,ds\right] = x^3 + 3\,\mathbb{E}_x\!\left[\int_0^\tau X_s\,ds\right]
    $$

    Note that $X_\tau \in \{0, b\}$, so $\mathbb{E}_x[X_\tau^3] = b^3 \cdot \mathbb{P}_x(X_\tau = b) + 0 = b^3 \cdot \frac{x}{b} = b^2 x$, using the exit probability $\mathbb{P}_x(X_\tau = b) = x/b$ for BM on $(0,b)$. Therefore:

    $$
    b^2 x = x^3 + 3\,\mathbb{E}_x\!\left[\int_0^\tau X_s\,ds\right]
    $$

    Solving:

    $$
    \mathbb{E}_x\!\left[\int_0^\tau X_s\,ds\right] = \frac{b^2 x - x^3}{3} = \frac{x(b^2 - x^2)}{3}
    $$

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

??? success "Solution to Exercise 2"
    For $f(x) = x^4$, the BM generator gives $\mathcal{L}(x^4) = \frac{1}{2}\cdot 12x^2 = 6x^2$. By Dynkin's formula:

    $$
    \mathbb{E}_x[X_\tau^4] = x^4 + \mathbb{E}_x\!\left[\int_0^\tau 6X_s^2\,ds\right] = x^4 + 6\,\mathbb{E}_x\!\left[\int_0^\tau X_s^2\,ds\right]
    $$

    To find $\mathbb{E}_x[X_\tau^4]$, note that $X_\tau \in \{a, b\}$:

    $$
    \mathbb{E}_x[X_\tau^4] = a^4 \cdot \mathbb{P}_x(X_\tau = a) + b^4 \cdot \mathbb{P}_x(X_\tau = b) = a^4 \cdot \frac{b-x}{b-a} + b^4 \cdot \frac{x-a}{b-a} = \frac{a^4(b-x) + b^4(x-a)}{b-a}
    $$

    Substituting:

    $$
    \frac{a^4(b-x) + b^4(x-a)}{b-a} = x^4 + 6\,\mathbb{E}_x\!\left[\int_0^\tau X_s^2\,ds\right]
    $$

    Solving:

    $$
    \mathbb{E}_x\!\left[\int_0^\tau X_s^2\,ds\right] = \frac{1}{6}\left[\frac{a^4(b-x) + b^4(x-a)}{b-a} - x^4\right]
    $$

---

**Exercise 3.** Consider the Ornstein--Uhlenbeck process $dX_t = -\kappa X_t\,dt + \sigma\,dW_t$ with $X_0 = x_0$. Applying Dynkin's formula with $f(x) = x^2$ and a deterministic time $t$, derive an integral equation for $\mathbb{E}_{x_0}[X_t^2]$. Solve the resulting ODE to obtain

$$
\mathbb{E}_{x_0}[X_t^2] = x_0^2 e^{-2\kappa t} + \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})
$$

??? success "Solution to Exercise 3"
    The OU generator is $\mathcal{L}f = -\kappa x\,f' + \frac{\sigma^2}{2}f''$. For $f(x) = x^2$:

    - $f'(x) = 2x$, $f''(x) = 2$

    $$
    \mathcal{L}(x^2) = -\kappa x \cdot 2x + \frac{\sigma^2}{2}\cdot 2 = -2\kappa x^2 + \sigma^2
    $$

    Applying Dynkin's formula with deterministic time $t$:

    $$
    \mathbb{E}_{x_0}[X_t^2] = x_0^2 + \int_0^t \mathbb{E}_{x_0}[-2\kappa X_s^2 + \sigma^2]\,ds = x_0^2 - 2\kappa\int_0^t \mathbb{E}_{x_0}[X_s^2]\,ds + \sigma^2 t
    $$

    Setting $v(t) = \mathbb{E}_{x_0}[X_t^2]$ and differentiating:

    $$
    v'(t) = -2\kappa v(t) + \sigma^2, \qquad v(0) = x_0^2
    $$

    This is a first-order linear ODE. The integrating factor is $e^{2\kappa t}$:

    $$
    \frac{d}{dt}\!\left[e^{2\kappa t}v(t)\right] = \sigma^2 e^{2\kappa t}
    $$

    Integrating:

    $$
    e^{2\kappa t}v(t) = x_0^2 + \frac{\sigma^2}{2\kappa}(e^{2\kappa t} - 1)
    $$

    Therefore:

    $$
    \mathbb{E}_{x_0}[X_t^2] = x_0^2 e^{-2\kappa t} + \frac{\sigma^2}{2\kappa}(1 - e^{-2\kappa t})
    $$

    As $t \to \infty$, this converges to $\frac{\sigma^2}{2\kappa}$, the variance of the OU stationary distribution.

---

**Exercise 4.** Explain why Dynkin's formula cannot be directly applied to compute $\mathbb{E}_x[e^{-\lambda \tau}]$ for a stopping time $\tau$ and $\lambda > 0$. What goes wrong if you try to find $f$ such that $\mathcal{L}f = -\lambda f$ and apply the standard Dynkin framework? Which formula provides the correct framework instead?

??? success "Solution to Exercise 4"
    Dynkin's formula in its standard form is:

    $$
    \mathbb{E}_x[f(X_\tau)] = f(x) + \mathbb{E}_x\!\left[\int_0^\tau (\mathcal{L}f)(X_s)\,ds\right]
    $$

    To compute $\mathbb{E}_x[e^{-\lambda \tau}]$, we would need to find $f$ such that Dynkin's formula yields this quantity. The natural attempt is to look for $f$ satisfying $\mathcal{L}f = -\lambda f$. If such $f$ existed and we applied Dynkin:

    $$
    \mathbb{E}_x[f(X_\tau)] = f(x) + \mathbb{E}_x\!\left[\int_0^\tau (-\lambda f(X_s))\,ds\right] = f(x) - \lambda\,\mathbb{E}_x\!\left[\int_0^\tau f(X_s)\,ds\right]
    $$

    This gives a relationship involving $\mathbb{E}_x[\int_0^\tau f(X_s)\,ds]$, not $\mathbb{E}_x[e^{-\lambda\tau}]$. The functional $e^{-\lambda\tau}$ is multiplicative (exponential) in $\tau$, while Dynkin's formula produces additive (integral) quantities.

    The correct framework is the **Feynman--Kac formula**. One considers $v(x) = \mathbb{E}_x[e^{-\lambda\tau}]$ and shows that $e^{-\lambda t}v(X_t)$ must be a martingale (up to the stopping time). Applying the extended generator $\tilde{\mathcal{L}}$ to $g(x,t) = e^{-\lambda t}v(x)$ and setting $\tilde{\mathcal{L}}g = 0$ gives:

    $$
    -\lambda e^{-\lambda t}v(x) + e^{-\lambda t}\mathcal{L}v(x) = 0 \implies \mathcal{L}v = \lambda v
    $$

    This is the Feynman--Kac eigenvalue equation. Unlike Dynkin, which relates expectations of $f(X_\tau)$ to integrals of $\mathcal{L}f$, Feynman--Kac handles the exponential discounting $e^{-\lambda\tau}$ through the "killing" term $\lambda v$.

---

**Exercise 5.** Let $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$ (GBM) with $S_0 = s_0$. Apply Dynkin's formula with $f(s) = \ln s$ and a deterministic time $t$ to compute $\mathbb{E}_{s_0}[\ln S_t]$. Verify your answer against the known distribution of $\ln S_t$.

??? success "Solution to Exercise 5"
    For GBM $dS_t = \mu S_t\,dt + \sigma S_t\,dW_t$, the generator is $\mathcal{L}f = \mu s\,f'(s) + \frac{\sigma^2 s^2}{2}f''(s)$. For $f(s) = \ln s$:

    - $f'(s) = 1/s$, $f''(s) = -1/s^2$

    $$
    \mathcal{L}(\ln s) = \mu s \cdot \frac{1}{s} + \frac{\sigma^2 s^2}{2}\cdot\left(-\frac{1}{s^2}\right) = \mu - \frac{\sigma^2}{2}
    $$

    Applying Dynkin with deterministic time $t$:

    $$
    \mathbb{E}_{s_0}[\ln S_t] = \ln s_0 + \int_0^t \left(\mu - \frac{\sigma^2}{2}\right)ds = \ln s_0 + \left(\mu - \frac{\sigma^2}{2}\right)t
    $$

    **Verification**: We know $\ln S_t = \ln s_0 + (\mu - \sigma^2/2)t + \sigma W_t$, which is normally distributed with mean $\ln s_0 + (\mu - \sigma^2/2)t$. This confirms the result.

---

**Exercise 6.** Let $X_t$ be BM on $(a, b)$ and $\tau$ the exit time. Suppose $g$ is a $C^2$ function with $\mathcal{L}g = 0$ (i.e., $g$ is harmonic). Use Dynkin's formula to show that

$$
\mathbb{E}_x[g(X_\tau)] = g(x)
$$

What are the harmonic functions for BM, and how does this result relate to the exit probabilities $\mathbb{P}_x(X_\tau = b) = \frac{x-a}{b-a}$?

??? success "Solution to Exercise 6"
    Since $g$ is $C^2$ and $\mathcal{L}g = 0$ (i.e., $g$ is harmonic), Dynkin's formula gives:

    $$
    \mathbb{E}_x[g(X_\tau)] = g(x) + \mathbb{E}_x\!\left[\int_0^\tau (\mathcal{L}g)(X_s)\,ds\right] = g(x) + \mathbb{E}_x\!\left[\int_0^\tau 0\,ds\right] = g(x)
    $$

    For BM with $\mathcal{L} = \frac{1}{2}\partial_{xx}$, the harmonic functions satisfy $\frac{1}{2}g'' = 0$, so $g'' = 0$, meaning $g(x) = \alpha x + \beta$ (affine functions).

    For the exit probability, take $g(x) = \frac{x - a}{b - a}$, which is affine (hence harmonic) with $g(a) = 0$ and $g(b) = 1$. Since $X_\tau \in \{a, b\}$:

    $$
    g(x) = \mathbb{E}_x[g(X_\tau)] = g(b)\,\mathbb{P}_x(X_\tau = b) + g(a)\,\mathbb{P}_x(X_\tau = a) = 1 \cdot \mathbb{P}_x(X_\tau = b) + 0
    $$

    Therefore $\mathbb{P}_x(X_\tau = b) = g(x) = \frac{x - a}{b - a}$. The exit probabilities are encoded in harmonic functions with appropriate boundary values.

---

**Exercise 7.** Consider the hierarchy: Ito's formula $\to$ Dynkin's formula $\to$ semigroup/generator.

(a) Starting from Ito's lemma for $f(X_t)$ where $dX_t = \mu(X_t)\,dt + \sigma(X_t)\,dW_t$, show explicitly how taking expectations yields Dynkin's formula.

(b) Give an example of a process (e.g., a jump process or weak solution) for which Dynkin's formula applies but Ito's pathwise formula does not. Explain why the stochastic integral term is not needed at the Dynkin level.

??? success "Solution to Exercise 7"
    **(a)** Recall (see [§ The Fundamental Decomposition](infinitesimal_generator.md#the-fundamental-decomposition)): Itô's lemma applied to $f(X_t)$ yields

    $$
    f(X_t) = f(X_0) + \int_0^t (\mathcal{L}f)(X_s)\,ds + \int_0^t f'(X_s)\sigma(X_s)\,dW_s
    $$

    Taking expectations (under conditions ensuring the Ito integral has zero mean):

    $$
    \mathbb{E}_x[f(X_t)] = f(x) + \mathbb{E}_x\!\left[\int_0^t (\mathcal{L}f)(X_s)\,ds\right]
    $$

    This is Dynkin's formula. The stochastic integral vanishes because $\mathbb{E}\!\left[\int_0^t f'\sigma\,dW_s\right] = 0$.

    **(b)** Consider a compound Poisson process $X_t = \sum_{i=1}^{N_t} Y_i$ where $N_t$ is Poisson with rate $\lambda$ and $Y_i$ are i.i.d. with distribution $\nu$. This process has discontinuous paths, so Ito's formula (which requires continuity via the quadratic variation of a continuous semimartingale) does not apply in its standard form.

    However, Dynkin's formula still holds: for $f \in C^2$ with the generator $(\mathcal{L}f)(x) = \lambda\int[f(x+y) - f(x)]\,\nu(dy)$:

    $$
    \mathbb{E}_x[f(X_t)] = f(x) + \mathbb{E}_x\!\left[\int_0^t (\mathcal{L}f)(X_s)\,ds\right]
    $$

    The stochastic integral term is not needed at the Dynkin level because Dynkin's formula operates on expectations (the law of $X_t$), not on individual paths. The martingale noise — whether from continuous diffusion or from compensated jumps — has zero mean and averages out. Dynkin captures only the systematic (drift) component encoded in $\mathcal{L}$.
