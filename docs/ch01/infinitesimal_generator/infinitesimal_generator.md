Excellent question! The infinitesimal generator $\mathcal{L}$ and its adjoint $\mathcal{L}^*$ are **far more than notational conveniences** - they reveal deep connections between stochastic processes, PDEs, functional analysis, and the probabilistic structure of the process. Let me explain the proper definitions and the profound insights they provide.

---

## 1. Proper Definitions

### The Infinitesimal Generator $\mathcal{L}$

**Definition (Probabilistic):**

For a Markov process $\{X_t\}$ with transition semigroup $P_t$, the **infinitesimal generator** is:

$$\mathcal{L}f(x) = \lim_{t \downarrow 0} \frac{\mathbb{E}[f(X_t) \mid X_0 = x] - f(x)}{t} = \lim_{t \downarrow 0} \frac{P_t f(x) - f(x)}{t}$$

where $(P_t f)(x) = \mathbb{E}[f(X_t) \mid X_0 = x]$.

**Interpretation:** $\mathcal{L}f(x)$ measures the **instantaneous rate of change** of the expected value of $f$ as the process evolves from initial state $x$.

**For diffusion processes:**

$$dX_t = \mu(X_t, t) dt + \sigma(X_t, t) dW_t$$

the generator is:

$$\boxed{\mathcal{L} = \mu(x,t)\frac{\partial}{\partial x} + a(x,t)\frac{\partial^2}{\partial x^2}}$$

where $a(x,t) = \frac{1}{2}\sigma^2(x,t)$.

In multidimensions:

$$\mathcal{L} = \sum_{i=1}^d \mu_i(x,t)\frac{\partial}{\partial x_i} + \sum_{i,j=1}^d a_{ij}(x,t)\frac{\partial^2}{\partial x_i \partial x_j}$$

### The Adjoint Operator $\mathcal{L}^*$

**Definition (Operator Theory):**

The **adjoint operator** $\mathcal{L}^*$ is defined via the inner product:

$$\langle \mathcal{L}^* \phi, \psi \rangle = \langle \phi, \mathcal{L}\psi \rangle$$

for suitable test functions $\phi, \psi$, where the inner product is:

$$\langle \phi, \psi \rangle = \int_{-\infty}^{\infty} \phi(x)\psi(x) \, dx$$

**Derivation by integration by parts:**

Starting with:
$$\int \phi(x) \mathcal{L}\psi(x) \, dx = \int \phi(x) \left[\mu \psi' + a\psi''\right] dx$$

Integrate by parts (assuming boundary terms vanish):

$$= \int \left[-(\mu\phi)' + (a\phi)''\right] \psi(x) \, dx$$

Therefore:

$$\boxed{\mathcal{L}^* = -\frac{\partial}{\partial x}[\mu(x,t) \cdot] + \frac{\partial^2}{\partial x^2}[a(x,t) \cdot]}$$

In multidimensions:

$$\mathcal{L}^* = -\sum_{i=1}^d \frac{\partial}{\partial x_i}[\mu_i \cdot] + \sum_{i,j=1}^d \frac{\partial^2}{\partial x_i \partial x_j}[a_{ij} \cdot]$$

---

## 2. The Semigroup Perspective

### Forward and Backward Semigroups

The infinitesimal generator is the "derivative at $t=0$" of the **transition semigroup**.

**Backward semigroup** $\{P_t\}$: Acts on functions

$$(P_t f)(x) = \mathbb{E}[f(X_t) \mid X_0 = x]$$

Properties:
- $P_0 = I$ (identity)
- $P_{t+s} = P_t P_s$ (semigroup property)
- $\frac{d}{dt}P_t f = \mathcal{L}P_t f = P_t \mathcal{L}f$

**Forward semigroup** $\{P_t^*\}$: Acts on measures/densities

$$(P_t^* \rho)(x) = \int p(x, t \mid y, 0) \rho(y) \, dy$$

Properties:
- $P_0^* = I$
- $P_{t+s}^* = P_t^* P_s^*$
- $\frac{d}{dt}P_t^* \rho = \mathcal{L}^* P_t^* \rho = P_t^* \mathcal{L}^* \rho$

**Duality:**
$$\int (P_t f)(x) \rho(x) \, dx = \int f(x) (P_t^* \rho)(x) \, dx$$

---

## 3. Deep Insights

### Insight 1: Local Behavior of the Process

The generator captures the **infinitesimal moments** of the process:

$$\mathbb{E}[X_{t+dt} - X_t \mid X_t = x] = \mu(x,t) dt + o(dt)$$

$$\mathbb{E}[(X_{t+dt} - X_t)^2 \mid X_t = x] = 2a(x,t) dt + o(dt)$$

**First-order term (drift):** $\mu(x,t) = \lim_{dt \to 0} \frac{\mathbb{E}[X_{t+dt} - x \mid X_t = x]}{dt}$

**Second-order term (diffusion):** $2a(x,t) = \lim_{dt \to 0} \frac{\mathbb{E}[(X_{t+dt} - x)^2 \mid X_t = x]}{dt}$

The operator $\mathcal{L}$ **encodes the local probabilistic structure** entirely.

### Insight 2: Martingale Characterization

**Dynkin's Formula:**

For any $f \in \text{Domain}(\mathcal{L})$, the process:

$$M_t = f(X_t) - f(X_0) - \int_0^t \mathcal{L}f(X_s) \, ds$$

is a **martingale**.

This means:
$$\mathcal{L}f(x) = 0 \quad \Longleftrightarrow \quad f(X_t) \text{ is a martingale}$$

**Example:** For Brownian motion with $\mathcal{L} = \frac{1}{2}\frac{d^2}{dx^2}$:
- $f(x) = x^2 - t$ satisfies $\mathcal{L}f + \frac{\partial f}{\partial t} = 0$, so $X_t^2 - t$ is a martingale
- $f(x) = e^{cx - \frac{c^2}{2}t}$ gives the exponential martingale

### Insight 3: Spectral Theory and Long-Time Behavior

The generator $\mathcal{L}$ is an **unbounded operator** on suitable function spaces. Its **spectrum** determines:

1. **Equilibrium distributions:** The stationary distribution $\pi$ satisfies $\mathcal{L}^* \pi = 0$

2. **Rate of convergence:** The spectral gap $\lambda_1$ (first non-zero eigenvalue) controls:
   $$\|P_t \rho - \pi\| \leq Ce^{-\lambda_1 t}$$

3. **Metastability:** Small eigenvalues indicate slow modes and timescale separation

**Example - Ornstein-Uhlenbeck:** 

$$\mathcal{L} = -\theta x \frac{d}{dx} + \frac{\sigma^2}{2}\frac{d^2}{dx^2}$$

Stationary distribution: $\mathcal{L}^* \pi = 0$ gives $\pi(x) = \mathcal{N}(0, \sigma^2/(2\theta))$

### Insight 4: Connection to Harmonic Functions

**Harmonic functions** satisfy $\mathcal{L}h = 0$.

**Probabilistic interpretation:** 
$$h(x) = \mathbb{E}[h(X_\tau) \mid X_0 = x]$$

for any stopping time $\tau$. These are **invariant under the process** in expectation.

**Example:** For Brownian motion ($\mathcal{L} = \frac{1}{2}\Delta$), harmonic functions are the classical harmonic functions from potential theory!

### Insight 5: Forward vs Backward - The Duality

The relationship between $\mathcal{L}$ and $\mathcal{L}^*$ reveals a fundamental duality:

| **Backward Generator $\mathcal{L}$** | **Forward Generator $\mathcal{L}^*$** |
|--------------------------------------|--------------------------------------|
| Acts on **functions** (observables) | Acts on **densities** (distributions) |
| "How do expectations evolve?" | "How do distributions evolve?" |
| Heisenberg picture | Schrödinger picture |
| Test functions | Measures |
| Kolmogorov backward equation | Fokker-Planck equation |

**Fundamental equation:**

$$\frac{d}{dt}\mathbb{E}[f(X_t)] = \mathbb{E}[\mathcal{L}f(X_t)]$$

This can be viewed as either:
- Evolution of $f$ forward in time (backward perspective)
- Evolution of the distribution of $X_t$ (forward perspective)

### Insight 6: Feynman-Kac and Modified Generators

Adding a potential $V(x)$ or killing rate $r(x)$ gives a **modified generator**:

$$\mathcal{L}_V = \mathcal{L} - V(x)$$

The Feynman-Kac formula:

$$v(x,t) = \mathbb{E}\left[e^{-\int_0^t V(X_s)ds} f(X_t) \mid X_0 = x\right]$$

satisfies:

$$\frac{\partial v}{\partial t} = \mathcal{L}v - Vv$$

The potential $V$ **modifies the evolution** through killing/weighting.

### Insight 7: Intertwining and Symmetry

If $\mathcal{L}$ is **symmetric** (self-adjoint): $\mathcal{L} = \mathcal{L}^*$, the process is **reversible**.

**Condition for reversibility:**

$$\mu(x,t) = a'(x,t) - \frac{\partial \log \pi(x)}{\partial x} a(x,t)$$

where $\pi$ is the stationary density.

**Example:** Overdamped Langevin dynamics in a potential $U(x)$:

$$dX_t = -\nabla U(X_t) dt + \sqrt{2} dW_t$$

has $\mathcal{L} = -\nabla U \cdot \nabla + \Delta$, which is symmetric with respect to the Gibbs measure $\pi(x) \propto e^{-U(x)}$.

---

## 4. Why This Matters: The Generator as the "DNA" of the Process

The generator $\mathcal{L}$ **completely characterizes** the Markov process:

$$\text{Generator } \mathcal{L} \quad \longleftrightarrow \quad \text{Markov Process } \{X_t\}$$

Everything about the process can be derived from $\mathcal{L}$:
- Transition probabilities: $P_t = e^{t\mathcal{L}}$
- Martingales: $\mathcal{L}f = 0$
- Stationary distributions: $\mathcal{L}^*\pi = 0$
- First passage times
- Optimal stopping problems
- etc.

---

## 5. Summary Table

| Concept | Generator $\mathcal{L}$ | Adjoint $\mathcal{L}^*$ |
|---------|------------------------|-------------------------|
| **Acts on** | Functions | Densities/measures |
| **Definition** | $\lim_{t\to 0} \frac{P_t f - f}{t}$ | $\langle \mathcal{L}^*\phi, \psi\rangle = \langle\phi, \mathcal{L}\psi\rangle$ |
| **Form** | $\mu \frac{\partial}{\partial x} + a\frac{\partial^2}{\partial x^2}$ | $-\frac{\partial}{\partial x}[\mu \cdot] + \frac{\partial^2}{\partial x^2}[a \cdot]$ |
| **Governs** | Backward equation | Forward equation |
| **Perspective** | Expectations of observables | Evolution of distributions |
| **Eigenvalue problem** | $\mathcal{L}f = \lambda f$ | $\mathcal{L}^*\rho = \lambda \rho$ |
| **Equilibrium** | Harmonic functions ($\mathcal{L}h=0$) | Stationary density ($\mathcal{L}^*\pi=0$) |

---

## Conclusion

The infinitesimal generator is **not just notation** - it is:

1. The **fundamental object** that encodes all local probabilistic information
2. The **bridge** connecting stochastic processes to PDE theory
3. The **key** to understanding long-time behavior via spectral analysis
4. The **natural language** for expressing martingales, harmonic functions, and invariant measures
5. The **basis** for the duality between forward (distributional) and backward (functional) perspectives

The operators $\mathcal{L}$ and $\mathcal{L}^*$ reveal that **stochastic processes and PDEs are two sides of the same coin**, connected by deep functional-analytic and probabilistic structures.