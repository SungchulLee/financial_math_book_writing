# Martingale Representation Theorem: Complete Mathematical Treatment

The Martingale Representation Theorem is **profoundly fundamental**—it establishes that every martingale can be written as a stochastic integral, which translates directly into the **existence of replicating portfolios** and the **completeness of financial markets**.

---

## **1. The Fundamental Theorem**

### **Statement (Brownian Filtration)**

Let $(\Omega, \mathcal{F}, \{\mathcal{F}_t\}_{t \geq 0}, \mathbb{P})$ be a filtered probability space where $\mathcal{F}_t = \sigma(W_s : s \leq t)$ is the natural filtration of a standard Brownian motion $W_t$.

**Theorem**: If $M_t$ is a square-integrable $(\mathcal{F}_t, \mathbb{P})$-martingale, then there exists a unique **previsible process** $\phi_t$ with $\mathbb{E}\left[\int_0^T \phi_s^2 ds\right] < \infty$ such that:

$$\boxed{M_t = M_0 + \int_0^t \phi_s dW_s}$$

for all $t \in [0,T]$.

### **Interpretation**

Every martingale in a Brownian filtration can be **represented as a stochastic integral** with respect to the driving Brownian motion. This is the **previsible representation property**.

### **Uniqueness**

The process $\phi_t$ is **unique** (up to sets of measure zero in $dt \times d\mathbb{P}$).

**Proof of uniqueness**: If $M_t = M_0 + \int_0^t \phi_s dW_s = M_0 + \int_0^t \psi_s dW_s$, then:

$$\int_0^t (\phi_s - \psi_s)dW_s = 0$$

By Itô isometry:

$$\mathbb{E}\left[\int_0^t (\phi_s - \psi_s)^2 ds\right] = 0$$

Therefore $\phi_t = \psi_t$ a.e.

---

## **2. Proof Sketch**

### **Step 1: Simple Functions**

First prove for **simple processes** of the form:

$$M_t = \sum_{i=0}^{n-1} \xi_i (W_{t_{i+1} \wedge t} - W_{t_i \wedge t})$$

where $\xi_i$ is $\mathcal{F}_{t_i}$-measurable.

For these, the representation is explicit: $\phi_t = \xi_i$ for $t \in (t_i, t_{i+1}]$.

### **Step 2: Approximation**

Every $L^2$-martingale can be approximated by simple processes in the $L^2$ sense.

For a martingale $M_t$ with $\mathbb{E}[M_T^2] < \infty$, construct a sequence of simple martingales $M_t^n$ such that:

$$\mathbb{E}[(M_T - M_T^n)^2] \to 0$$

### **Step 3: Isometry**

Each $M_t^n$ has representation:

$$M_t^n = M_0 + \int_0^t \phi_s^n dW_s$$

By the **Itô isometry**:

$$\mathbb{E}[(M_T^n - M_T^m)^2] = \mathbb{E}\left[\int_0^T (\phi_s^n - \phi_s^m)^2 ds\right]$$

So $\{\phi^n\}$ is Cauchy in $L^2([0,T] \times \Omega)$.

### **Step 4: Limit**

The limit $\phi_t = \lim_{n \to \infty} \phi_t^n$ (in $L^2$) gives:

$$M_t = M_0 + \int_0^t \phi_s dW_s$$

by continuity of stochastic integration.

### **Extension to General Martingales**

For general square-integrable martingales (not necessarily continuous), use **Doob-Meyer decomposition** and **optional stopping**.

---

## **3. Application to Black-Scholes**

### **Discounted Option Value as Martingale**

Under the risk-neutral measure $\mathbb{Q}$, the discounted option value:

$$\tilde{V}_t = e^{-rt}V(S_t, t)$$

is a $\mathbb{Q}$-martingale.

**Proof**: By risk-neutral valuation:

$$\tilde{V}_t = \mathbb{E}^{\mathbb{Q}}[\tilde{V}_T \mid \mathcal{F}_t] = \mathbb{E}^{\mathbb{Q}}[e^{-rT}V(S_T,T) \mid \mathcal{F}_t]$$

Taking conditional expectations:

$$\mathbb{E}^{\mathbb{Q}}[\tilde{V}_T \mid \mathcal{F}_t] = \tilde{V}_t$$

So $\tilde{V}_t$ is a martingale.

### **Martingale Representation**

By the theorem, there exists $\phi_t$ such that:

$$\boxed{d\tilde{V}_t = \phi_t dW_t^{\mathbb{Q}}}$$

or equivalently:

$$\boxed{e^{-rt}V(S_t,t) = V(S_0,0) + \int_0^t \phi_s dW_s^{\mathbb{Q}}}$$

### **Identifying the Integrand**

Apply Itô's lemma to $\tilde{V}_t = e^{-rt}V(S_t,t)$:

$$d\tilde{V}_t = e^{-rt}\left[\frac{\partial V}{\partial t}dt + \frac{\partial V}{\partial S}dS_t + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}(dS_t)^2\right] - re^{-rt}V dt$$

With $dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}$:

$$
d\tilde{V}_t 
= 
e^{-rt}\left[\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV\right]dt + e^{-rt}\sigma S \frac{\partial V}{\partial S}dW_t^{\mathbb{Q}}
$$

For $\tilde{V}_t$ to be a martingale, the $dt$ term must vanish:

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} - rV = 0$$

This is the **Black-Scholes PDE**!

The integrand is:

$$\boxed{\phi_t = e^{-rt}\sigma S_t \frac{\partial V}{\partial S}(S_t,t)}$$

---

## **4. Hedging Interpretation**

### **The Delta Hedge**

The martingale representation tells us that the option can be replicated by holding:

- **Number of shares**: $\Delta_t = \frac{\partial V}{\partial S}(S_t, t)$

- **Cash position**: $V_t - \Delta_t S_t$

### **Self-Financing Strategy**

Define the portfolio value:

$$\Pi_t = \Delta_t S_t + B_t$$

where $B_t$ is the cash account with $dB_t = rB_t dt$.

**Self-financing condition**:

$$d\Pi_t = \Delta_t dS_t + rB_t dt$$

No external cash flows—gains/losses come only from asset price changes and interest.

### **Replication**

Substituting $B_t = V_t - \Delta_t S_t$:

$$\begin{array}{lll}
d\Pi_t 
&=&\displaystyle \Delta_t dS_t + r(V_t - \Delta_t S_t)dt\\
&=&\displaystyle \Delta_t(rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}) + rV_t dt - r\Delta_t S_t dt\\
&=&\displaystyle \Delta_t \sigma S_t dW_t^{\mathbb{Q}} + rV_t dt
\end{array}$$

But also, by Itô:

$$dV_t = \frac{\partial V}{\partial t}dt + \frac{\partial V}{\partial S}dS_t + \frac{1}{2}\frac{\partial^2 V}{\partial S^2}(dS_t)^2$$

For $d\Pi_t = dV_t$ (perfect replication), we need the **Black-Scholes PDE** to hold.

### **The Connection**

$$\boxed{\text{Martingale representation} \iff \text{Existence of replicating portfolio}}$$

The integrand $\phi_t$ **is the delta hedge**!

---

## **5. Multi-Dimensional Case**

### **Multiple Brownian Motions**

Let $W_t = (W_t^{(1)}, \ldots, W_t^{(d)})$ be a $d$-dimensional Brownian motion.

**Theorem**: If $M_t$ is a square-integrable martingale in the filtration $\mathcal{F}_t = \sigma(W_s : s \leq t)$, then:

$$\boxed{M_t = M_0 + \sum_{i=1}^d \int_0^t \phi_s^{(i)} dW_s^{(i)}}$$

for unique previsible processes $\phi_t^{(1)}, \ldots, \phi_t^{(d)}$ with:

$$\mathbb{E}\left[\int_0^T \sum_{i=1}^d (\phi_s^{(i)})^2 ds\right] < \infty$$

### **Vector Notation**

$$\boxed{M_t = M_0 + \int_0^t \boldsymbol{\phi}_s \cdot d\mathbf{W}_s}$$

where $\boldsymbol{\phi}_t \cdot d\mathbf{W}_t = \sum_{i=1}^d \phi_t^{(i)}dW_t^{(i)}$.

### **Application: Multiple Assets**

For $n$ stocks driven by $d$ Brownian motions ($d \leq n$):

$$dS_t^{(i)} = r S_t^{(i)}dt + \sum_{j=1}^d \sigma_{ij}S_t^{(i)}dW_t^{(j)}$$

An option $V(S_1, \ldots, S_n, t)$ has representation:

$$d(e^{-rt}V) = \sum_{j=1}^d \phi_t^{(j)}dW_t^{(j)}$$

### **Computing the Integrands**

Apply multi-dimensional Itô:

$$dV = \frac{\partial V}{\partial t}dt + \sum_{i=1}^n \frac{\partial V}{\partial S_i}dS_i + \frac{1}{2}\sum_{i,k=1}^n \frac{\partial^2 V}{\partial S_i \partial S_k}d\langle S_i, S_k \rangle$$

The coefficient of $dW_t^{(j)}$ gives:

$$\boxed{\phi_t^{(j)} = e^{-rt}\sum_{i=1}^n \sigma_{ij}S_t^{(i)}\frac{\partial V}{\partial S_i}}$$

---

## **6. Completeness of Markets**

### **Complete Market Definition**

A market is **complete** if every contingent claim can be **replicated** by a self-financing trading strategy.

### **Fundamental Equivalence**

For a market with $d$ independent sources of randomness and $n$ tradable assets:

$$\boxed{\text{Market is complete} \iff d \leq n \text{ and } \text{rank}(\sigma) = d}$$

where $\sigma$ is the $n \times d$ volatility matrix.

### **Black-Scholes Setting**

- **1 stock + 1 bond** (2 assets)
- **1 Brownian motion** (1 source of randomness)
- Rank condition: $\sigma \neq 0$

Therefore: **Market is complete**.

### **Martingale Representation Perspective**

Complete market ⟺ Every $\mathcal{F}_t$-martingale can be represented as a stochastic integral with respect to the **tradable assets**.

**Proof**:
 
- Every claim $H$ satisfies $e^{-rT}H$ is $\mathcal{F}_T$-measurable

- $V_t = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[H \mid \mathcal{F}_t]$ is a martingale

- By martingale representation: $V_t = V_0 + \int_0^t \phi_s dW_s^{\mathbb{Q}}$

- Construct portfolio: $\Delta_t = \phi_t/(\sigma S_t)$ shares, remainder in bonds

- This portfolio replicates $H$

---

## **7. Previsible Representation Property**

### **Previsibility**

A process $\phi_t$ is **previsible** (or **predictable**) if it is measurable with respect to the **previsible $\sigma$-algebra** $\mathcal{P}$, which is generated by left-continuous adapted processes.

### **Intuition**

$\phi_t$ is **known just before time $t$**—no "look-ahead" bias.

For continuous processes: previsible = adapted and left-continuous.

### **Why Previsibility Matters**

In finance: the hedge ratio $\Delta_t$ must be determined **before** observing $S_t$. You can't hedge based on future information!

### **Stochastic Integral Existence**

The stochastic integral $\int_0^t \phi_s dW_s$ is well-defined when $\phi_t$ is:

1. **Previsible**

2. **Square-integrable**: $\mathbb{E}\left[\int_0^T \phi_s^2 ds\right] < \infty$

These are the **admissible trading strategies**.

---

## **8. The Value Process**

### **Portfolio Dynamics**

For a self-financing portfolio with $\Delta_t$ shares and cash $B_t$:

$$V_t = \Delta_t S_t + B_t$$

$$dV_t = \Delta_t dS_t + rB_t dt$$

Substituting $B_t = V_t - \Delta_t S_t$:

$$dV_t = \Delta_t dS_t + r(V_t - \Delta_t S_t)dt$$

With $dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}$:

$$\boxed{dV_t = rV_t dt + \Delta_t \sigma S_t dW_t^{\mathbb{Q}}}$$

### **Discounted Value**

Define $\tilde{V}_t = e^{-rt}V_t$:

$$d\tilde{V}_t 
= e^{-rt}dV_t - re^{-rt}V_t dt
= e^{-rt}[rV_t dt + \Delta_t \sigma S_t dW_t^{\mathbb{Q}}] - re^{-rt}V_t dt$$

$$\boxed{d\tilde{V}_t = e^{-rt}\Delta_t \sigma S_t dW_t^{\mathbb{Q}}}$$

This is a **martingale** (no drift term)!

### **Initial Value**

Since $\tilde{V}_t$ is a martingale:

$$\tilde{V}_0 = \mathbb{E}^{\mathbb{Q}}[\tilde{V}_T]$$

$$\boxed{V_0 = e^{-rT}\mathbb{E}^{\mathbb{Q}}[V_T]}$$

This is the **risk-neutral pricing formula**.

---

## **9. Clark-Ocone Formula**

### **Malliavin Derivative**

For a smooth functional $F = f(W_{t_1}, \ldots, W_{t_n})$, the **Malliavin derivative** is:

$$D_t F = \lim_{h \to 0}\frac{F(W + h\mathbb{1}_{[0,t]}) - F(W)}{h}$$

It measures sensitivity to perturbations of the Brownian path at time $t$.

### **Clark-Ocone Formula**

For $F \in L^2(\mathcal{F}_T)$ that is Malliavin differentiable:

$$\boxed{F = \mathbb{E}[F] + \int_0^T \mathbb{E}[D_t F \mid \mathcal{F}_t]dW_t}$$

This gives an **explicit formula** for the integrand in the martingale representation!

### **Application to Options**

For $F = \Phi(S_T)$:

$$D_t F = \Phi'(S_T) \cdot D_t S_T$$

With $S_T = S_0 \exp\left[(r-\frac{\sigma^2}{2})T + \sigma W_T\right]$:

$$D_t S_T = \sigma S_T \cdot \mathbb{1}_{t \leq T}$$

Therefore:

$$\mathbb{E}[D_t F \mid \mathcal{F}_t] = \mathbb{E}[\Phi'(S_T)\sigma S_T \mid \mathcal{F}_t]$$

This relates to $\frac{\partial V}{\partial S}$ via the **Feynman-Kac formula**.

---

## **10. Incomplete Markets**

### **Stochastic Volatility**

Consider:

$$dS_t = rS_t dt + \sigma_t S_t dW_t^{(1)}$$

$$d\sigma_t = \mu(\sigma_t)dt + \xi(\sigma_t)dW_t^{(2)}$$

with $d\langle W^{(1)}, W^{(2)} \rangle = \rho dt$.

### **Two Sources of Randomness**

The filtration is generated by **two** Brownian motions, but there's only **one** tradable risky asset (the stock).

**Market is incomplete**: $d = 2 > n = 1$.

### **Martingale Representation**

For the discounted option value:

$$d(e^{-rt}V) = \phi_t^{(1)}dW_t^{(1)} + \phi_t^{(2)}dW_t^{(2)}$$

But the stock only provides exposure to $W^{(1)}$:

$$d(e^{-rt}S) = e^{-rt}\sigma S dW_t^{(1)}$$

**Cannot replicate** $\phi_t^{(2)}dW_t^{(2)}$ with stock and bond!

### **Non-Uniqueness of EMM**

There are **infinitely many** equivalent martingale measures, parametrized by the **market price of volatility risk** $\lambda_t$:

$$dW_t^{(2),\mathbb{Q}^\lambda} = dW_t^{(2)} - \lambda_t dt$$

Different $\lambda$ ⟹ different option prices.

### **Minimal Martingale Measure**

The **minimal martingale measure** $\mathbb{Q}^*$ is characterized by:

- Stock price process unchanged: $dW_t^{(1),\mathbb{Q}^*} = dW_t^{(1),\mathbb{P}}$

- Only $W^{(2)}$ changes: $dW_t^{(2),\mathbb{Q}^*} = dW_t^{(2),\mathbb{P}} - \lambda_t^* dt$

where $\lambda_t^*$ is chosen to preserve certain optimality properties.

---

## **11. Jump Processes**

### **Poisson Process Case**

Let $N_t$ be a Poisson process with intensity $\lambda$.

The martingale $M_t = N_t - \lambda t$ has representation:

$$M_t = \int_0^t dM_s$$

But this is **not** a stochastic integral with respect to a Brownian motion!

### **Martingale Representation for Jump Processes**

For a Poisson filtration $\mathcal{F}_t = \sigma(N_s : s \leq t)$, every martingale has the form:

$$M_t = M_0 + \int_0^t \phi_s dM_s = M_0 + \int_0^t \phi_s (dN_s - \lambda ds)$$

where $\phi_t$ is previsible.

### **Mixed Case: Jump-Diffusion**

For a process with both Brownian and jump components:

$$dS_t = \mu S_t dt + \sigma S_t dW_t + S_t(e^J - 1)dN_t$$

The martingale representation requires **both** types of integrals:

$$M_t = M_0 + \int_0^t \phi_s dW_s + \int_0^t \psi_s d\tilde{N}_s$$

where $\tilde{N}_t = N_t - \lambda t$ is the compensated Poisson process.

### **Market Incompleteness**

Jumps make the market **incomplete**:

- Infinitely many jump sizes ⟹ infinitely many sources of randomness

- Only finitely many tradable assets

- No perfect replication

---

## **12. Relationship to PDEs**

### **Feynman-Kac and Martingale Representation**

The Feynman-Kac formula states:

$$V(S,t) = e^{-r(T-t)}\mathbb{E}^{\mathbb{Q}}[\Phi(S_T) \mid S_t = S]$$

Applying Itô to $V(S_t,t)$ and requiring it to be a local martingale gives the PDE:

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} = rV$$

### **The Integrand**

The martingale representation:

$$d(e^{-rt}V) = \phi_t dW_t^{\mathbb{Q}}$$

gives:

$$\phi_t = e^{-rt}\sigma S_t \frac{\partial V}{\partial S}$$

So:

$$\boxed{\frac{\partial V}{\partial S} = \frac{\phi_t}{e^{-rt}\sigma S_t}}$$

The **PDE solution** and **martingale representation** are **dual perspectives** on the same object!

### **Weak vs. Strong Solutions**

- **PDE approach**: Seeks a classical solution $V(S,t)$ to the PDE
- **Martingale approach**: Constructs the value as an expectation

The martingale method often works even when classical PDE solutions don't exist (e.g., for path-dependent options).

---

## **13. Quadratic Variation and Martingales**

### **Quadratic Variation**

For the martingale:

$$M_t = \int_0^t \phi_s dW_s$$

The **quadratic variation** is:

$$\boxed{\langle M \rangle_t = \int_0^t \phi_s^2 ds}$$

This follows from the **Itô isometry**:

$$\mathbb{E}[M_t^2] = \mathbb{E}\left[\int_0^t \phi_s^2 ds\right]$$

### **Covariation**

For two martingales:

$$M_t = \int_0^t \phi_s dW_s, \quad N_t = \int_0^t \psi_s dW_s$$

The **covariation** is:

$$\boxed{\langle M, N \rangle_t = \int_0^t \phi_s \psi_s ds}$$

### **Application: Delta Hedging**

The discounted option value $\tilde{V}_t$ and discounted stock price $\tilde{S}_t$ have:

$$d\langle \tilde{V}, \tilde{S} \rangle_t = e^{-2rt}\sigma^2 S_t^2 \frac{\partial V}{\partial S}dt$$

The hedge ratio that **minimizes variance** is:

$$\displaystyle 
\Delta_t = \frac{d\langle \tilde{V}, \tilde{S} \rangle_t/dt}{d\langle \tilde{S} \rangle_t/dt} = \frac{e^{-2rt}\sigma^2 S_t^2 \frac{\partial V}{\partial S}}{e^{-2rt}\sigma^2 S_t^2} = \frac{\partial V}{\partial S}
$$

This is the **delta**!

---

## **14. Kunita-Watanabe Decomposition**

### **Orthogonal Decomposition**

For a martingale $M_t$ in a filtration generated by a process $X_t$, the **Kunita-Watanabe decomposition** states:

$$\boxed{M_t = M_0 + \int_0^t \phi_s dX_s + L_t}$$

where:

- $\int_0^t \phi_s dX_s$ is the **predictable part** (hedgeable)

- $L_t$ is a martingale **orthogonal** to $X$: $d\langle L, X \rangle = 0$ (residual risk)

### **In Complete Markets**

If the market is complete (e.g., Black-Scholes), then $L_t \equiv 0$, and:

$$M_t = M_0 + \int_0^t \phi_s dX_s$$

All risk is hedgeable!

### **In Incomplete Markets**

$L_t \neq 0$ represents **unhedgeable risk**. For example:
- In stochastic volatility models, $L_t$ captures volatility risk
- In jump models, $L_t$ captures jump risk

The variance of $L_T$ measures the **hedging error**.

---

## **15. Föllmer-Schweizer Decomposition**

### **Mean-Variance Hedging**

In incomplete markets, find the strategy that **minimizes** the expected squared hedging error:

$$\min_{\phi} \mathbb{E}\left[\left(V_T - \int_0^T \phi_s dS_s\right)^2\right]$$

### **The Decomposition**

$$\boxed{V_T = V_0 + \int_0^T \phi_s^* dS_s + L_T}$$

where:

- $\phi_t^*$ is the **optimal hedging strategy**

- $L_T$ is the **minimal hedging error**

- $\mathbb{E}[L_T \mid \mathcal{F}_t] = 0$ and $d\langle L, S \rangle = 0$

### **Computing $\phi^*$**

$$\boxed{\phi_t^* = \frac{d\langle V, S \rangle_t/dt}{d\langle S \rangle_t/dt}}$$

This generalizes the delta hedge to incomplete markets!

---

## **16. Practical Implementation**

### **Estimating the Integrand**

In practice, $\phi_t = \frac{\partial V}{\partial S}$ is computed:

1. **Analytically**: For Black-Scholes, $\Delta = N(d_1)$
2. **Numerically**: Finite difference or automatic differentiation
3. **From simulations**: 
   $$\frac{\partial V}{\partial S} \approx \frac{V(S+\epsilon) - V(S-\epsilon)}{2\epsilon}$$

### **Discrete Hedging**

In reality, hedging is done at discrete times $t_0, t_1, \ldots, t_n$:

$$V_{t_i} \approx V_0 + \sum_{j=0}^{i-1}\Delta_{t_j}(S_{t_{j+1}} - S_{t_j})$$

### **Hedging Error**

The error from discrete hedging is:

$$\epsilon_n = V_T - V_0 - \sum_{j=0}^{n-1}\Delta_{t_j}(S_{t_{j+1}} - S_{t_j})$$

As $n \to \infty$ (continuous hedging), $\epsilon_n \to 0$ in $L^2$.

### **Transaction Costs**

With transaction costs $c|dS|$, the problem becomes:

$$\min_{\phi} \mathbb{E}\left[\text{Hedging Error}^2 + c\int_0^T |d\phi_s|\right]$$

This leads to **utility-based pricing** and **optimal stopping** problems.

---

## **17. Martingale Representation in Different Measures**

### **Physical vs. Risk-Neutral**

Under the physical measure $\mathbb{P}$:

$$dS_t = \mu S_t dt + \sigma S_t dW_t^{\mathbb{P}}$$

The option value is **not** a $\mathbb{P}$-martingale.

Under $\mathbb{Q}$:

$$dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}$$

The discounted option value **is** a $\mathbb{Q}$-martingale, admitting the representation.

### **Girsanov and Representation**

The change of measure:

$$dW_t^{\mathbb{Q}} = dW_t^{\mathbb{P}} - \frac{\mu - r}{\sigma}dt$$

preserves the martingale representation property—just the driving Brownian motion changes.

### **Stock Measure**

Under $\mathbb{Q}^S$:

$$dS_t = (r+\sigma^2)S_t dt + \sigma S_t dW_t^{\mathbb{Q}^S}$$

Normalized prices (by stock) are $\mathbb{Q}^S$-martingales.

---

## **18. Abstract Formulation**

### **Previsible Representation Property**

A filtration $\{\mathcal{F}_t\}$ has the **previsible representation property** if every $\mathcal{F}_t$-martingale can be represented as a stochastic integral with respect to a fixed set of martingales.

### **Extremal Martingales**

In the Brownian case, $W_t$ is the **extremal martingale**—all others are built from it.

In multi-dimensional cases, there is a **basis** of extremal martingales $M_1, \ldots, M_d$ such that:

$$M_t = M_0 + \sum_{i=1}^d \int_0^t \phi_s^{(i)}dM_s^{(i)}$$

### **Lévy Processes**

For Lévy processes with jumps, the representation includes:

- Brownian part: $\int_0^t \phi_s dW_s$

- Small jumps: $\int_0^t \int_{|x|<1}\psi_s(x)\tilde{N}(ds,dx)$

- Large jumps: $\int_0^t \int_{|x|\geq 1}\chi_s(x)N(ds,dx)$

where $N$ is the jump measure and $\tilde{N}$ is the compensated measure.

---

## **19. The Fundamental Insights**

### **Duality Table**

| **Stochastic Calculus** | **Finance** |
|-------------------------|-------------|
| Martingale | Discounted price in EMM |
| Representation integrand $\phi_t$ | Hedging strategy $\Delta_t$ |
| Stochastic integral | Self-financing portfolio |
| Quadratic variation | Realized variance |
| Previsibility | No look-ahead |
| Completeness (PRP) | Perfect replication possible |

### **The Master Equation**

$$\boxed{e^{-rt}V(S_t,t) = V(S_0,0) + \int_0^t e^{-rs}\sigma S_s\frac{\partial V}{\partial S}(S_s,s)dW_s^{\mathbb{Q}}}$$

This **single equation** encodes:
1. Risk-neutral valuation ($V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-rT}V_T]$)
2. The Black-Scholes PDE (drift = 0)
3. Delta hedging ($\Delta = \frac{\partial V}{\partial S}$)
4. Completeness (representation exists)

### **Why It's Powerful**

1. **Existence**: Guarantees replicating portfolio exists
2. **Uniqueness**: Determines the hedge ratio uniquely
3. **Computation**: Provides formula for $\Delta_t$
4. **Optimality**: Delta hedge minimizes variance
5. **Generality**: Extends to multiple dimensions, different numeraires

---

## **20. The Philosophical Point**

The Martingale Representation Theorem reveals that **derivative pricing and hedging are two sides of the same coin**:

- **Pricing**: Computing $V_0 = \mathbb{E}^{\mathbb{Q}}[e^{-rT}V_T]$
- **Hedging**: Finding $\phi_t$ in the representation $\tilde{V}_t = V_0 + \int_0^t \phi_s dW_s$

They're **dual formulations** of the same mathematical object. The PDE, Feynman-Kac, and martingale representation are all **different windows** into this unified structure.

In complete markets, this duality is perfect. In incomplete markets, it breaks down—we have **multiple prices** (different EMMs) and **imperfect hedges** (residual $L_t$).

This is the **deep beauty** of mathematical finance!


