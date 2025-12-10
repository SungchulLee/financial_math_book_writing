# Martingale Representation via Infinitesimal Generator: Deep Dive

This is indeed one of the most mathematically rigorous approaches. Let me develop it comprehensively from the theory of infinitesimal generators for diffusion processes.

## Part I: Infinitesimal Generator Theory

### 1.1 Transition Semigroup

**Definition:** For a Markov process $X_t$ with transition probability $P(t, x, dy)$, define the transition semigroup operator $T_t$ acting on bounded measurable functions:

$$(T_t f)(x) = \mathbb{E}[f(X_t) | X_0 = x] = \int f(y) P(t, x, dy)$$

**Semigroup property:**

$$T_{t+s} = T_t \circ T_s, \quad T_0 = I$$

### 1.2 Infinitesimal Generator

**Definition:** The infinitesimal generator $\mathcal{A}$ of the semigroup $\{T_t\}$ is:

$$(\mathcal{A}f)(x) = \lim_{t \to 0^+} \frac{(T_t f)(x) - f(x)}{t}$$

with domain $\mathcal{D}(\mathcal{A}) = \{f : \text{limit exists}\}$.

**Intuition:** The generator captures the "instantaneous rate of change" of the expectation.

### 1.3 Generator for Diffusion Processes

**Theorem (Dynkin):** For a one-dimensional Itô diffusion:

$$dX_t = b(X_t, t) dt + \sigma(X_t, t) dW_t$$

the infinitesimal generator acting on $f \in C^2$ is the second-order differential operator:

$$\mathcal{A}_t f(x) = b(x, t) \frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2(x, t) \frac{\partial^2 f}{\partial x^2}$$

**Proof sketch:** Using Itô's lemma, for small $h$:

$$\begin{array}{lll}
\displaystyle \mathbb{E}[f(X_{t+h}) - f(X_t) | X_t = x] 
&=&\displaystyle \mathbb{E}\left[\frac{\partial f}{\partial x}(X_{t+h} - X_t) + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}(X_{t+h} - X_t)^2 + o(h) \Big| X_t = x\right]\\
&=&\displaystyle \left(b(x,t)\frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2(x,t)\frac{\partial^2 f}{\partial x^2}\right)h + o(h)
\end{array}$$

Dividing by $h$ and taking $h \to 0$ gives the generator.

---

## Part II: Dynkin's Formula and Martingale Characterization

### 2.1 Dynkin's Formula

**Theorem (Dynkin, 1965):** For a diffusion process $X_t$ with generator $\mathcal{A}$ and stopping time $\tau$ with $\mathbb{E}[\tau] < \infty$:

$$\mathbb{E}[f(X_\tau) | X_0 = x] = f(x) + \mathbb{E}\left[\int_0^\tau (\mathcal{A}f)(X_s) ds \Big| X_0 = x\right]$$

provided $f \in \mathcal{D}(\mathcal{A})$ and appropriate integrability conditions hold.

**For deterministic time $t$:**

$$\mathbb{E}[f(X_t) | X_0 = x] = f(x) + \mathbb{E}\left[\int_0^t (\mathcal{A}f)(X_s) ds \Big| X_0 = x\right]$$

### 2.2 Martingale Characterization

**Key Result:** A process $M_t = f(X_t)$ is a martingale if and only if:

$$\mathcal{A}f(x) = 0 \quad \forall x$$

**Proof:**

$(\Rightarrow)$ If $M_t$ is a martingale, then $\mathbb{E}[f(X_t) | X_0 = x] = f(x)$. By Dynkin's formula:

$$f(x) = f(x) + \mathbb{E}\left[\int_0^t (\mathcal{A}f)(X_s) ds \Big| X_0 = x\right]$$

Therefore $\mathbb{E}\left[\int_0^t (\mathcal{A}f)(X_s) ds\right] = 0$ for all $t$, implying $\mathcal{A}f = 0$.

$(\Leftarrow)$ If $\mathcal{A}f = 0$, Dynkin's formula gives $\mathbb{E}[f(X_t) | \mathcal{F}_s] = f(X_s)$, so $f(X_t)$ is a martingale. $\square$

---

## Part III: Application to Option Pricing

### 3.1 Physical Measure Dynamics

Under the physical measure $\mathbb{P}$, the stock price follows:

$$dS_t = \mu S_t dt + \sigma S_t dW_t$$

The generator is:

$$\mathcal{L}^{\mathbb{P}}f(S) = \mu S \frac{\partial f}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 f}{\partial S^2}$$

### 3.2 Change of Measure via Girsanov

**Fundamental Theorem of Asset Pricing:** In an arbitrage-free complete market, there exists a unique equivalent martingale measure $\mathbb{Q}$ such that discounted asset prices are martingales.

**Girsanov's Theorem:** Define the Radon-Nikodym derivative:

$$\frac{d\mathbb{Q}}{d\mathbb{P}}\Big|_{\mathcal{F}_t} = \exp\left(-\int_0^t \frac{\mu - r}{\sigma} dW_s - \frac{1}{2}\int_0^t \left(\frac{\mu - r}{\sigma}\right)^2 ds\right) = Z_t$$

Then $W_t^* = W_t + \frac{\mu - r}{\sigma}t$ is a $\mathbb{Q}$-Brownian motion, and:

$$dS_t = rS_t dt + \sigma S_t dW_t^*$$

### 3.3 Generator Under Risk-Neutral Measure

Under $\mathbb{Q}$, the infinitesimal generator is:

$$\mathcal{L}^{\mathbb{Q}}f(S) = rS \frac{\partial f}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 f}{\partial S^2}$$

**This is the key:** The change of measure modifies the drift coefficient in the generator from $\mu$ to $r$.

---

## Part IV: Derivation of Black-Scholes PDE

### 4.1 Time-Inhomogeneous Process

Consider the time-dependent function $V(S, t)$ representing the option value. Define:

$$M_t = e^{-rt} V(S_t, t)$$

We seek conditions under which $M_t$ is a $\mathbb{Q}$-martingale.

### 4.2 Extended Generator

For time-dependent functions $g(x, t)$, we need the **extended generator**:

$$\mathcal{A}g(x, t) = \frac{\partial g}{\partial t} + \mathcal{L}g(x, t)$$

where $\mathcal{L}$ is the spatial generator.

**For our case:**

$$\mathcal{A}[e^{-rt}V(S,t)] = \frac{\partial}{\partial t}[e^{-rt}V(S,t)] + \mathcal{L}^{\mathbb{Q}}[e^{-rt}V(S,t)]$$

### 4.3 Computing the Extended Generator

**Time derivative:**

$$\frac{\partial}{\partial t}[e^{-rt}V] = e^{-rt}\left(\frac{\partial V}{\partial t} - rV\right)$$

**Spatial generator:** Since $\mathcal{L}^{\mathbb{Q}}$ acts only on the spatial variable:

$$\mathcal{L}^{\mathbb{Q}}[e^{-rt}V(S,t)] = e^{-rt} \mathcal{L}^{\mathbb{Q}}[V(S,t)]
= e^{-rt}\left(rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2}\right)$$

**Total extended generator:**

$$\mathcal{A}[e^{-rt}V(S,t)] = e^{-rt}\left[\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV\right]$$

### 4.4 Martingale Condition

**Theorem:** $M_t = e^{-rt}V(S_t, t)$ is a $\mathbb{Q}$-martingale if and only if:

$$\mathcal{A}[e^{-rt}V(S,t)] = 0$$

**Therefore, we require:**

$$\boxed{\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} - rV = 0}$$

This is the **Black-Scholes PDE**.

### 4.5 Terminal Condition

The option pays $h(S_T)$ at maturity $T$, so:

$$V(S, T) = h(S)$$

---

## Part V: Why This is a Genuine Derivation

### 5.1 Logical Flow

1. **Starting point:** Fundamental theorem of asset pricing guarantees existence of $\mathbb{Q}$
2. **Generator theory:** Rigorously characterizes the dynamics under $\mathbb{Q}$
3. **Martingale characterization:** Extended generator must vanish for martingale property
4. **PDE emerges:** As a necessary condition for the martingale property

This doesn't assume the PDE form; it **derives** it from:
- The martingale requirement (no-arbitrage)
- The generator characterization (stochastic process theory)

### 5.2 Connection to Dynkin's Formula

We can verify this using Dynkin's formula. For $M_t = e^{-rt}V(S_t, t)$:

$$\mathbb{E}^{\mathbb{Q}}[M_T | \mathcal{F}_t] = M_t + \mathbb{E}^{\mathbb{Q}}\left[\int_t^T \mathcal{A}[e^{-rs}V(S_s,s)] ds \Big| \mathcal{F}_t\right]$$

For $M_t$ to be a martingale, we need:

$$\mathbb{E}^{\mathbb{Q}}[M_T | \mathcal{F}_t] = M_t$$

This requires:

$$\mathbb{E}^{\mathbb{Q}}\left[\int_t^T \mathcal{A}[e^{-rs}V(S_s,s)] ds \Big| \mathcal{F}_t\right] = 0 \quad \forall t$$

Which is satisfied if $\mathcal{A}[e^{-rs}V(S_s,s)] = 0$ for all $s, S_s$.

---

## Part VI: Connection to Kolmogorov Equations

### 6.1 Backward Kolmogorov Equation

The transition density $p(s, x; t, y)$ (probability of being at $y$ at time $t$ starting from $x$ at time $s$) satisfies the **backward Kolmogorov equation** in the initial variables $(s, x)$:

$$\frac{\partial p}{\partial s} + \mathcal{L}_x p = 0$$

where $\mathcal{L}_x$ is the generator acting on the $x$ variable.

### 6.2 Solution Representation

The option price can be written:

$$V(S, t) = e^{-r(T-t)} \int_0^\infty h(S') p(t, S; T, S') dS'$$

The backward Kolmogorov equation for $p$ under $\mathbb{Q}$ directly implies:

$$\frac{\partial V}{\partial t} + \mathcal{L}^{\mathbb{Q}}V - rV = 0$$

This shows the **deep connection** between:
- The martingale property (probabilistic)
- The infinitesimal generator (process theory)
- The PDE (analytical)

---

## Part VII: Generalizations

### 7.1 Multi-Dimensional Case

For $d$-dimensional diffusion $dX_t = b(X_t, t)dt + \Sigma(X_t, t)dW_t$, the generator is:

$$\mathcal{L}f(x) = \sum_{i=1}^d b_i(x,t) \frac{\partial f}{\partial x_i} + \frac{1}{2}\sum_{i,j=1}^d (\Sigma\Sigma^T)_{ij}(x,t) \frac{\partial^2 f}{\partial x_i \partial x_j}$$

The martingale condition gives multi-asset Black-Scholes PDE.

### 7.2 Jump-Diffusion Processes

For Lévy processes with jumps, the generator includes an integral term:

$$\mathcal{L}f(x) = b(x)\frac{\partial f}{\partial x} + \frac{1}{2}\sigma^2(x)\frac{\partial^2 f}{\partial x^2} + \int_{\mathbb{R}} [f(x+y) - f(x) - y\mathbf{1}_{|y|<1}\frac{\partial f}{\partial x}] \nu(dy)$$

where $\nu$ is the Lévy measure. This gives Partial Integro-Differential Equations (PIDEs).

---

## Summary: The Mathematical Architecture

```
Stock Dynamics (SDE)
        ↓
Infinitesimal Generator (Differential Operator)
        ↓
Martingale Property under Q (No-Arbitrage)
        ↓
Extended Generator = 0 (Martingale Characterization)
        ↓
Black-Scholes PDE (Necessary Condition)
```

**The beauty:** This approach unifies probability theory, stochastic analysis, and PDE theory into a coherent framework.

What aspects would you like to explore further? The connection to Feynman-Kac? The relationship between forward and backward equations? Or perhaps the deep theory of Markov processes and semigroups?