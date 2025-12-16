# Diffusion Processes and Kolmogorov Equations

## 1. The Diffusion Process

A **diffusion process** is a continuous-time, continuous-state Markov process that can be characterized by a stochastic differential equation (SDE). Consider a diffusion process $\{X_t\}_{t \geq 0}$ on $\mathbb{R}^d$ satisfying:


$$dX_t = \mu(X_t, t) \, dt + \sigma(X_t, t) \, dW_t$$



where:
- $\mu: \mathbb{R}^d \times [0,\infty) \to \mathbb{R}^d$ is the **drift coefficient** (infinitesimal mean)
- $\sigma: \mathbb{R}^d \times [0,\infty) \to \mathbb{R}^{d \times m}$ is the **diffusion coefficient** (infinitesimal volatility)
- $W_t$ is an $m$-dimensional standard Brownian motion

The process evolves according to a deterministic drift perturbed by Brownian noise. The **diffusion matrix** is defined as:


$$a(x,t) = \frac{1}{2}\sigma(x,t)\sigma^T(x,t)$$



For scalar processes ($d=1$), this becomes $a(x,t) = \frac{1}{2}\sigma^2(x,t)$.

## 2. Transition Density Function

The **transition density function** (or **transition probability density**) $p(x, t \mid x_0, t_0)$ describes the conditional probability density of finding the process at state $x$ at time $t$, given that it was at state $x_0$ at time $t_0 < t$:


$$p(x, t \mid x_0, t_0) = \frac{\partial}{\partial x} \mathbb{P}(X_t \leq x \mid X_{t_0} = x_0)$$



More precisely, for any measurable set $A$:


$$\mathbb{P}(X_t \in A \mid X_{t_0} = x_0) = \int_A p(x, t \mid x_0, t_0) \, dx$$



**Key properties:**

1. **Normalization**: $\int_{-\infty}^{\infty} p(x, t \mid x_0, t_0) \, dx = 1$

2. **Initial condition**: $\lim_{t \downarrow t_0} p(x, t \mid x_0, t_0) = \delta(x - x_0)$

3. **Chapman-Kolmogorov equation**: For $t_0 < t_1 < t$,

$$p(x, t \mid x_0, t_0) = \int_{-\infty}^{\infty} p(x, t \mid y, t_1) p(y, t_1 \mid x_0, t_0) \, dy$$



**Forward vs. Backward Variables:**
- **Forward variables** $(x, t)$: the "future" state and time
- **Backward variables** $(x_0, t_0)$: the "initial" state and time

The forward equation describes evolution in $(x,t)$ with fixed $(x_0, t_0)$, while the backward equation describes evolution in $(x_0, t_0)$ with fixed $(x,t)$.

## 3. Kolmogorov Forward Equation (Fokker-Planck Equation)

The **Kolmogorov forward equation** (also called the **Fokker-Planck equation**) describes how the transition density evolves forward in time and space:


$$\frac{\partial p}{\partial t}(x, t \mid x_0, t_0) = -\frac{\partial}{\partial x}\left[\mu(x,t) p(x, t \mid x_0, t_0)\right] + \frac{\partial^2}{\partial x^2}\left[a(x,t) p(x, t \mid x_0, t_0)\right]$$



In the multi-dimensional case ($x \in \mathbb{R}^d$):


$$\frac{\partial p}{\partial t}(x, t \mid x_0, t_0) = -\sum_{i=1}^d \frac{\partial}{\partial x_i}\left[\mu_i(x,t) p\right] + \sum_{i,j=1}^d \frac{\partial^2}{\partial x_i \partial x_j}\left[a_{ij}(x,t) p\right]$$



This can be written more compactly using the **forward operator** $\mathcal{L}^*$:


$$\frac{\partial p}{\partial t} = \mathcal{L}^* p = -\nabla \cdot (\mu p) + \nabla \cdot \nabla \cdot (a p)$$



**Physical interpretation:** 
- The first term represents convective transport (drift)
- The second term represents diffusive spreading
- This is a **continuity equation** for probability density

## 4. Proof of Kolmogorov Forward Equation Using Itô's Lemma

**Goal:** Derive the forward equation for $p(x,t \mid x_0, t_0)$ using Itô's lemma.

**Setup:** Consider a test function $\phi(x) \in C_c^2(\mathbb{R})$ (twice continuously differentiable with compact support). Define:


$$u(t) = \mathbb{E}[\phi(X_t) \mid X_{t_0} = x_0] = \int_{-\infty}^{\infty} \phi(x) p(x,t \mid x_0, t_0) \, dx$$



**Step 1:** Apply Itô's lemma to $\phi(X_t)$:


$$d\phi(X_t) = \frac{\partial \phi}{\partial x}(X_t) \, dX_t + \frac{1}{2}\frac{\partial^2 \phi}{\partial x^2}(X_t) \, d\langle X \rangle_t$$



where $d\langle X \rangle_t = \sigma^2(X_t, t) \, dt$.

Substituting the SDE:


$$d\phi(X_t) = \left[\mu(X_t, t)\frac{\partial \phi}{\partial x}(X_t) + a(X_t, t)\frac{\partial^2 \phi}{\partial x^2}(X_t)\right] dt + \sigma(X_t, t)\frac{\partial \phi}{\partial x}(X_t) \, dW_t$$



**Step 2:** Take expectations:


$$\frac{d}{dt}\mathbb{E}[\phi(X_t) \mid X_{t_0} = x_0] = \mathbb{E}\left[\mu(X_t, t)\frac{\partial \phi}{\partial x}(X_t) + a(X_t, t)\frac{\partial^2 \phi}{\partial x^2}(X_t) \mid X_{t_0} = x_0\right]$$



**Step 3:** Express in terms of transition density:


$$\frac{d}{dt} \int \phi(x) p(x,t \mid x_0, t_0) \, dx = \int \left[\mu(x,t)\phi'(x) + a(x,t)\phi''(x)\right] p(x,t \mid x_0, t_0) \, dx$$



**Step 4:** Move time derivative inside and integrate by parts twice:


$$\int \phi(x) \frac{\partial p}{\partial t}(x,t \mid x_0, t_0) \, dx = \int \left[\mu(x,t)\phi'(x) + a(x,t)\phi''(x)\right] p \, dx$$



For the first term (integration by parts):

$$\int \mu(x,t)\phi'(x) p \, dx = -\int \phi(x) \frac{\partial}{\partial x}[\mu(x,t) p] \, dx$$



For the second term (integration by parts twice):

$$\int a(x,t)\phi''(x) p \, dx = \int \phi(x) \frac{\partial^2}{\partial x^2}[a(x,t) p] \, dx$$



**Step 5:** Since $\phi$ is arbitrary:


$$\boxed{\frac{\partial p}{\partial t}(x,t \mid x_0, t_0) = -\frac{\partial}{\partial x}\left[\mu(x,t) p(x,t \mid x_0, t_0)\right] + \frac{\partial^2}{\partial x^2}\left[a(x,t) p(x,t \mid x_0, t_0)\right]}$$



This is the Kolmogorov forward equation. $\square$

## 5. Proof of Kolmogorov Forward Equation Using Chapman-Kolmogorov

**Goal:** Derive the forward equation from the Chapman-Kolmogorov equation and properties of the diffusion.

**Step 1: Chapman-Kolmogorov equation**

For $t_0 < t < t + h$:


$$p(x, t+h \mid x_0, t_0) = \int_{-\infty}^{\infty} p(x, t+h \mid y, t) p(y, t \mid x_0, t_0) \, dy$$



**Step 2: Infinitesimal transition probabilities**

For small $h > 0$, the infinitesimal transition has the form:


$$p(x, t+h \mid y, t) = \delta(x-y) + h \cdot k(x, y, t) + o(h)$$



where the **infinitesimal generator** $k(x,y,t)$ satisfies:


$$\int k(x,y,t) \, dx = 0 \quad \text{(probability conservation)}$$



**Step 3: Moment conditions**

For a diffusion process, the infinitesimal moments are:


$$\int (x-y) k(x,y,t) \, dx = -\frac{\partial}{\partial y}[\mu(y,t)]$$




$$\int (x-y)^2 k(x,y,t) \, dx = -\frac{\partial^2}{\partial y^2}[a(y,t)]$$



**Step 4: Expand Chapman-Kolmogorov**


$$p(x, t+h \mid x_0, t_0) = \int \left[\delta(x-y) + h \cdot k(x,y,t)\right] p(y, t \mid x_0, t_0) \, dy + o(h)$$




$$= p(x, t \mid x_0, t_0) + h \int k(x,y,t) p(y, t \mid x_0, t_0) \, dy + o(h)$$



**Step 5: Taylor expand $p(y,t \mid x_0, t_0)$ around $y = x$**


$$p(y, t \mid x_0, t_0) = p(x,t \mid x_0, t_0) + (y-x)\frac{\partial p}{\partial x}(x,t \mid x_0, t_0) + \frac{(y-x)^2}{2}\frac{\partial^2 p}{\partial x^2}(x,t \mid x_0, t_0) + \ldots$$



**Step 6: Substitute and use moment conditions**


$$\int k(x,y,t) p(y, t \mid x_0, t_0) \, dy = -\frac{\partial}{\partial x}[\mu(x,t) p] + \frac{\partial^2}{\partial x^2}[a(x,t) p]$$



**Step 7: Take the limit**


$$\frac{p(x, t+h \mid x_0, t_0) - p(x, t \mid x_0, t_0)}{h} = -\frac{\partial}{\partial x}[\mu(x,t) p] + \frac{\partial^2}{\partial x^2}[a(x,t) p] + \frac{o(h)}{h}$$



As $h \to 0$:


$$\boxed{\frac{\partial p}{\partial t}(x,t \mid x_0, t_0) = -\frac{\partial}{\partial x}\left[\mu(x,t) p(x,t \mid x_0, t_0)\right] + \frac{\partial^2}{\partial x^2}\left[a(x,t) p(x,t \mid x_0, t_0)\right]}$$



This is the Kolmogorov forward equation. $\square$

## 6. Kolmogorov Backward Equation

The **Kolmogorov backward equation** describes how the transition density depends on the initial conditions $(x_0, t_0)$:


$$\frac{\partial p}{\partial t_0}(x, t \mid x_0, t_0) = -\mu(x_0, t_0)\frac{\partial p}{\partial x_0}(x, t \mid x_0, t_0) - a(x_0, t_0)\frac{\partial^2 p}{\partial x_0^2}(x, t \mid x_0, t_0)$$



Note the sign: $\frac{\partial}{\partial t_0}$ measures change as we move the initial time, which is "backwards" relative to forward time evolution.

Equivalently, defining $s = t - t_0$ (time to maturity) and working with $\tilde{p}(x, s \mid x_0) = p(x, t_0 + s \mid x_0, t_0)$:


$$-\frac{\partial \tilde{p}}{\partial s}(x, s \mid x_0) = -\mu(x_0, t_0)\frac{\partial \tilde{p}}{\partial x_0}(x, s \mid x_0) - a(x_0, t_0)\frac{\partial^2 \tilde{p}}{\partial x_0^2}(x, s \mid x_0)$$



This can be written using the **backward operator** $\mathcal{L}$:


$$\frac{\partial p}{\partial t_0} = -\mathcal{L}_{x_0, t_0} p = -\mu(x_0,t_0)\frac{\partial}{\partial x_0} - a(x_0,t_0)\frac{\partial^2}{\partial x_0^2}$$



**Key distinction:** The backward equation is a **parabolic PDE in the initial variables** with coefficients evaluated at $(x_0, t_0)$, while the forward equation is parabolic in the terminal variables with coefficients at $(x,t)$.

## 7. Proof of Kolmogorov Backward Equation

### Method 1: Using Itô's Lemma

**Setup:** Consider a function $v(x_0, t_0) = \mathbb{E}[f(X_t) \mid X_{t_0} = x_0]$ for some terminal condition $f$ at fixed time $t > t_0$.

Using the transition density:

$$v(x_0, t_0) = \int_{-\infty}^{\infty} f(x) p(x, t \mid x_0, t_0) \, dx$$



**Step 1:** For $t_0 < t_0 + h < t$, by the Markov property:


$$v(x_0, t_0) = \mathbb{E}[v(X_{t_0+h}, t_0+h) \mid X_{t_0} = x_0]$$



**Step 2:** Apply Itô's lemma to $v(X_s, s)$ for $s \in [t_0, t_0+h]$:


$$dv(X_s, s) = \left[\frac{\partial v}{\partial s} + \mu(X_s, s)\frac{\partial v}{\partial x} + a(X_s, s)\frac{\partial^2 v}{\partial x^2}\right]_{\!(X_s, s)} ds + \sigma(X_s, s)\frac{\partial v}{\partial x}(X_s, s) \, dW_s$$



**Step 3:** Integrate from $t_0$ to $t_0 + h$ and take expectations:


$$\mathbb{E}[v(X_{t_0+h}, t_0+h) \mid X_{t_0} = x_0] - v(x_0, t_0) = \mathbb{E}\left[\int_{t_0}^{t_0+h} \left(\frac{\partial v}{\partial s} + \mathcal{L}_s v\right) ds \mid X_{t_0} = x_0\right]$$



where $\mathcal{L}_s v = \mu(X_s,s)\frac{\partial v}{\partial x}(X_s,s) + a(X_s,s)\frac{\partial^2 v}{\partial x^2}(X_s,s)$.

**Step 4:** Since $v(x_0, t_0) = \mathbb{E}[v(X_{t_0+h}, t_0+h) \mid X_{t_0} = x_0]$:


$$0 = \mathbb{E}\left[\int_{t_0}^{t_0+h} \left(\frac{\partial v}{\partial s} + \mathcal{L}_s v\right) ds \mid X_{t_0} = x_0\right]$$



For this to hold for all $h > 0$, we need:


$$\frac{\partial v}{\partial t_0}(x_0, t_0) + \mu(x_0, t_0)\frac{\partial v}{\partial x_0}(x_0, t_0) + a(x_0, t_0)\frac{\partial^2 v}{\partial x_0^2}(x_0, t_0) = 0$$



**Step 5:** Since $v(x_0, t_0) = \int f(x) p(x, t \mid x_0, t_0) \, dx$:


$$\int f(x) \left[\frac{\partial p}{\partial t_0} + \mu(x_0, t_0)\frac{\partial p}{\partial x_0} + a(x_0, t_0)\frac{\partial^2 p}{\partial x_0^2}\right] dx = 0$$



Since $f$ is arbitrary:


$$\boxed{\frac{\partial p}{\partial t_0}(x, t \mid x_0, t_0) = -\mu(x_0, t_0)\frac{\partial p}{\partial x_0}(x, t \mid x_0, t_0) - a(x_0, t_0)\frac{\partial^2 p}{\partial x_0^2}(x, t \mid x_0, t_0)}$$



This is the Kolmogorov backward equation. $\square$

### Method 2: Using Chapman-Kolmogorov Equation

**Step 1:** Write Chapman-Kolmogorov for $t_0 < t_0 + h < t$:


$$p(x, t \mid x_0, t_0) = \int_{-\infty}^{\infty} p(x, t \mid y, t_0+h) p(y, t_0+h \mid x_0, t_0) \, dy$$



**Step 2:** For small $h$, expand $p(y, t_0+h \mid x_0, t_0)$ as a transition kernel:


$$p(y, t_0+h \mid x_0, t_0) = \delta(y - x_0) - h\mu(x_0, t_0)\frac{\partial \delta(y-x_0)}{\partial x_0} + ha(x_0, t_0)\frac{\partial^2 \delta(y-x_0)}{\partial x_0^2} + o(h)$$



**Step 3:** Substitute into Chapman-Kolmogorov:


$$p(x, t \mid x_0, t_0) = p(x, t \mid x_0, t_0+h) - h\mu(x_0, t_0)\frac{\partial p}{\partial x_0}(x, t \mid x_0, t_0+h) + ha(x_0, t_0)\frac{\partial^2 p}{\partial x_0^2}(x, t \mid x_0, t_0+h) + o(h)$$



**Step 4:** Rearranging:


$$\frac{p(x, t \mid x_0, t_0+h) - p(x, t \mid x_0, t_0)}{h} = \mu(x_0, t_0)\frac{\partial p}{\partial x_0}(x, t \mid x_0, t_0) - a(x_0, t_0)\frac{\partial^2 p}{\partial x_0^2}(x, t \mid x_0, t_0) + \frac{o(h)}{h}$$



**Step 5:** Take $h \to 0$ and note $\frac{\partial p}{\partial t_0} = -\lim_{h \to 0} \frac{p(x,t \mid x_0, t_0+h) - p(x,t \mid x_0, t_0)}{h}$:


$$\boxed{\frac{\partial p}{\partial t_0}(x, t \mid x_0, t_0) = -\mu(x_0, t_0)\frac{\partial p}{\partial x_0}(x, t \mid x_0, t_0) - a(x_0, t_0)\frac{\partial^2 p}{\partial x_0^2}(x, t \mid x_0, t_0)}$$



This is the Kolmogorov backward equation. $\square$

## 8. Applications

### 8.1 Option Pricing (Feynman-Kac Formula)

The Black-Scholes PDE for option pricing is the backward Kolmogorov equation. For an option value $V(S,t)$ where $S$ follows:


$$dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$$



The backward equation gives:


$$\frac{\partial V}{\partial t} + \mu S \frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2 \frac{\partial^2 V}{\partial S^2} = rV$$



with terminal condition $V(S,T) = \text{payoff}(S)$. This connects diffusion theory directly to derivatives pricing.

### 8.2 Heat Equation

For Brownian motion ($\mu = 0$, $a = \frac{1}{2}$), the forward equation becomes:


$$\frac{\partial p}{\partial t} = \frac{1}{2}\frac{\partial^2 p}{\partial x^2}$$



This is the **heat equation**, fundamental to thermal diffusion and Fourier analysis.

### 8.3 Fokker-Planck in Statistical Physics

The Ornstein-Uhlenbeck process models mean-reverting systems:


$$dX_t = -\theta X_t \, dt + \sigma \, dW_t$$



The forward equation becomes:


$$\frac{\partial p}{\partial t} = \theta \frac{\partial}{\partial x}(xp) + \frac{\sigma^2}{2}\frac{\partial^2 p}{\partial x^2}$$



The stationary distribution is $p_{\infty}(x) = \mathcal{N}(0, \sigma^2/(2\theta))$.

### 8.4 Population Genetics (Wright-Fisher Model)

Gene frequency dynamics with drift and mutation:


$$dx_t = \mu(x_t) \, dt + \sqrt{x_t(1-x_t)} \, dW_t$$



The forward equation describes the evolution of allele frequency distributions.

### 8.5 Neuroscience (Neuronal Firing)

The integrate-and-fire model uses the backward equation to compute first-passage time densities—the probability distribution of when a neuron will fire.

### 8.6 Filtering Theory (Kushner-Stratonovich Equation)

The forward equation generalizes to the **Kushner-Stratonovich equation** for nonlinear filtering, describing how to update probability distributions given noisy observations.

### 8.7 Machine Learning (Score-Based Generative Models)

Modern diffusion models for image generation use the forward process to gradually add noise, then train a neural network to learn the score function $\nabla_x \log p(x,t)$ to reverse the diffusion and generate samples.

---

**Summary of Key Relationships:**


$$\text{Forward Equation (Fokker-Planck)} \leftrightarrow \text{Evolution of densities in state space}$$




$$\text{Backward Equation} \leftrightarrow \text{Evolution of expectations/value functions}$$




$$\text{Feynman-Kac Formula} \leftrightarrow \text{Connects PDEs to stochastic expectations}$$
