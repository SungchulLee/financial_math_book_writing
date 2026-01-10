# Similarity Solutions: Complete Mathematical Treatment

Similarity solutions exploit **scale invariance** and **dimensional analysis** to reduce PDEs to ODEs by identifying the "right" combination of variables. This reveals the **deep symmetry structure** underlying option pricing.

---

## **1. Dimensional Analysis Foundation**

### **Physical Dimensions**

In the Black-Scholes problem, the **dimensional quantities** are:
- $S$: stock price $[$ \$ $]$
- $K$: strike price $[$ \$ $]$
- $t, T$: time $[T]$
- $\sigma$: volatility $[T^{-1/2}]$ (since $dW_t$ scales as $\sqrt{dt}$)
- $r$: interest rate $[T^{-1}]$
- $V$: option value $[$ \$ $]$

### **Buckingham Pi Theorem**

With $n = 6$ variables and $m = 2$ fundamental dimensions ($[\$], [T]$), we get $n - m = 4$ **dimensionless groups**.

### **Dimensionless Variables**

Define:

$$\boxed{\pi_1 = \frac{S}{K} \quad \text{(moneyness)}}$$




$$\boxed{\pi_2 = \sigma\sqrt{T-t} = \sigma\sqrt{\tau} \quad \text{(scaled time)}}$$




$$\boxed{\pi_3 = r\tau \quad \text{(discount factor exponent)}}$$




$$\boxed{\pi_4 = \frac{V}{K} \quad \text{(normalized value)}}$$



### **Dimensional Reduction**

The option value must have the form:

$$\boxed{V(S,K,t,\sigma,r,T) = K \cdot f\left(\frac{S}{K}, \sigma\sqrt{\tau}, r\tau\right)}$$



This is the **most general form** consistent with dimensional analysis!

---

## **2. Scale Invariance of Black-Scholes**

### **The PDE**


$$\boxed{\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV = 0}$$



### **Scaling Transformation**

Consider the **one-parameter family** of transformations:

$$S \to \lambda S, \quad K \to \lambda K, \quad V \to \lambda V$$



with $t, \sigma, r$ unchanged.

### **Invariance**

Substituting into the PDE:

$$\frac{\partial(\lambda V)}{\partial t} + r(\lambda S)\frac{\partial(\lambda V)}{\partial(\lambda S)} + \frac{\sigma^2(\lambda S)^2}{2}\frac{\partial^2(\lambda V)}{\partial(\lambda S)^2} - r(\lambda V)$$




$$= \lambda\left[\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{\sigma^2 S^2}{2}\frac{\partial^2 V}{\partial S^2} - rV\right] = 0$$



The PDE is **homogeneous of degree 1** in $(S, K, V)$.

### **Economic Interpretation**

If all dollar amounts scale by $\lambda$ (change of currency), the **form** of the PDE doesn't change. This is the **scale invariance** or **homogeneity** of the market.

---

## **3. Similarity Variable for Black-Scholes**

### **Log-Moneyness Variable**

The most natural similarity variable combines space and time:


$$\boxed{\xi = \frac{\ln(S/K)}{\sigma\sqrt{\tau}} = \frac{x}{\sigma\sqrt{\tau}}}$$



where $x = \ln(S/K)$ and $\tau = T - t$.

### **Physical Meaning**

- Numerator: **log-moneyness** (how far from strike in log terms)
- Denominator: **volatility × time scale** (uncertainty measure)
- $\xi$: **standardized distance** from strike

For $|\xi| \approx 1$: option is at-the-money over the relevant time scale
For $|\xi| \gg 1$: option is deep in/out of the money

### **Alternative Variables**

Other common choices:

$$\eta = \frac{\ln(S/K) + (r \pm \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}} \quad \text{(drift-adjusted)}$$




$$\zeta = \frac{S}{Ke^{-r\tau}} \quad \text{(forward moneyness)}$$



Each has advantages for different problems.

---

## **4. Reduction to ODE**

### **Similarity Ansatz**

Seek a solution of the form:

$$\boxed{V(S,t) = K \cdot g(\xi) = K \cdot g\left(\frac{\ln(S/K)}{\sigma\sqrt{\tau}}\right)}$$



### **Computing Derivatives**

**Partial derivatives**:

$$\frac{\partial\xi}{\partial\tau} = -\frac{\ln(S/K)}{2\sigma\tau^{3/2}} = -\frac{\xi}{2\tau}$$




$$\frac{\partial\xi}{\partial S} = \frac{1}{S\sigma\sqrt{\tau}}$$




$$\frac{\partial^2\xi}{\partial S^2} = -\frac{1}{S^2\sigma\sqrt{\tau}}$$



**Chain rule**:

$$\frac{\partial V}{\partial t} = -\frac{\partial V}{\partial\tau} = K g'(\xi)\frac{\xi}{2\tau}$$




$$\frac{\partial V}{\partial S} = K g'(\xi) \cdot \frac{1}{S\sigma\sqrt{\tau}}$$




$$\frac{\partial^2 V}{\partial S^2} = K g''(\xi) \cdot \frac{1}{S^2\sigma^2\tau} - K g'(\xi) \cdot \frac{1}{S^2\sigma\sqrt{\tau}}$$



### **Substituting into PDE**


$$Kg'(\xi)\frac{\xi}{2\tau} + rS \cdot Kg'(\xi)\frac{1}{S\sigma\sqrt{\tau}} + \frac{\sigma^2 S^2}{2}\left[Kg''(\xi)\frac{1}{S^2\sigma^2\tau} - Kg'(\xi)\frac{1}{S^2\sigma\sqrt{\tau}}\right] - rKg(\xi) = 0$$



Simplify:

$$\frac{Kg'(\xi)\xi}{2\tau} + \frac{rKg'(\xi)}{\sigma\sqrt{\tau}} + \frac{Kg''(\xi)}{2\tau} - \frac{Kg'(\xi)}{2\sigma\sqrt{\tau}} - rKg(\xi) = 0$$



Multiply by $\frac{\tau}{K}$:

$$\frac{g'(\xi)\xi}{2} + \frac{rg'(\xi)\sqrt{\tau}}{\sigma} + \frac{g''(\xi)}{2} - \frac{g'(\xi)\sqrt{\tau}}{2\sigma} - rg(\xi)\tau = 0$$



### **Problem: Non-Similarity**

The presence of $\tau$ prevents complete reduction to ODE!

The issue: $r$ introduces a **scale** that breaks perfect similarity.

---

## **5. Modified Similarity Variables**

### **Dimensionless Time**

Include the interest rate scaling:

$$\xi = \frac{\ln(S/K) + (r - \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}$$



This is related to $d_2$ in Black-Scholes!

### **Modified Ansatz**

Try:

$$\boxed{V(S,t) = Se^{-q\tau}h(\xi_1) - Ke^{-r\tau}h(\xi_2)}$$



where:

$$\xi_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}} = d_1$$




$$\xi_2 = \frac{\ln(S/K) + (r - \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}} = d_2$$



This is the **Black-Scholes structure**!

### **The ODE for $h$**

Both $h(\xi_1)$ and $h(\xi_2)$ satisfy:

$$\boxed{\frac{d^2h}{d\xi^2} + \xi\frac{dh}{d\xi} = 0}$$



### **Solution**

Integrate once:

$$\frac{dh}{d\xi} = Ce^{-\xi^2/2}$$



Integrate again:

$$\boxed{h(\xi) = C_1\int_{-\infty}^{\xi}e^{-s^2/2}ds + C_2 = C_1\sqrt{2\pi}N(\xi) + C_2}$$



where $N(\xi) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^{\xi}e^{-s^2/2}ds$ is the standard normal CDF!

---

## **6. Heat Equation Similarity**

### **Transformed PDE**

In variables $x = \ln(S/K)$ and $\tau = T - t$, after removing drift and decay:

$$\frac{\partial w}{\partial \tau} = \frac{\partial^2 w}{\partial x^2}$$



This is the **heat equation**.

### **Self-Similar Solution**

The fundamental solution (heat kernel) has the form:

$$\boxed{w(x,\tau) = \frac{1}{\sqrt{\tau}}G\left(\frac{x}{\sqrt{\tau}}\right)}$$



where $\eta = \frac{x}{\sqrt{\tau}}$ is the **similarity variable**.

### **Reduction to ODE**

Substitute:

$$\frac{\partial w}{\partial\tau} = -\frac{1}{2\tau^{3/2}}G(\eta) - \frac{\eta}{2\tau^{3/2}}G'(\eta)$$




$$\frac{\partial^2 w}{\partial x^2} = \frac{1}{\tau^{3/2}}G''(\eta)$$



The heat equation becomes:

$$-\frac{1}{2\tau^{3/2}}G - \frac{\eta}{2\tau^{3/2}}G' = \frac{1}{\tau^{3/2}}G''$$



Multiply by $\tau^{3/2}$:

$$\boxed{G''(\eta) + \frac{\eta}{2}G'(\eta) + \frac{1}{2}G(\eta) = 0}$$



### **Solution: Gaussian**

The solution is:

$$\boxed{G(\eta) = Ce^{-\eta^2/4} = Ce^{-x^2/(4\tau)}}$$



Therefore:

$$\boxed{w(x,\tau) = \frac{C}{\sqrt{4\pi\tau}}e^{-x^2/(4\tau)}}$$



This is the **heat kernel** or **fundamental solution**!

---

## **7. Lie Group Methods**

### **Infinitesimal Generators**

The Black-Scholes PDE admits **symmetry transformations** forming a Lie group.

**Scaling symmetry**:

$$X_1 = S\frac{\partial}{\partial S} + K\frac{\partial}{\partial K} + V\frac{\partial}{\partial V}$$



**Time translation**:

$$X_2 = \frac{\partial}{\partial t}$$



**Interest rate scaling**:

$$X_3 = r\frac{\partial}{\partial r} + \frac{1}{\tau}\frac{\partial}{\partial\tau}$$



### **Invariant Solutions**

Solutions invariant under a symmetry generator satisfy:

$$X f = 0$$



For $X_1$ (scaling):

$$S\frac{\partial f}{\partial S} + K\frac{\partial f}{\partial K} + V\frac{\partial f}{\partial V} = 0$$



This gives:

$$f(S,K,V) = F\left(\frac{S}{K}, \frac{V}{K}\right)$$



The similarity structure!

### **Optimal System**

The **optimal system** of one-dimensional subalgebras gives all **inequivalent** similarity reductions.

For Black-Scholes, this recovers:
1. Scaling similarity: $\xi = S/K$
2. Heat equation similarity: $\eta = x/\sqrt{\tau}$
3. Combined: $\xi = \frac{\ln(S/K)}{\sqrt{\tau}}$

---

## **8. Traveling Wave Solutions**

### **Wave Ansatz**

For PDEs with translation symmetry, try:

$$u(x,t) = f(x - ct)$$



where $c$ is the **wave speed**.

### **Black-Scholes Context**

The drift term $\left(r - \frac{\sigma^2}{2}\right)\frac{\partial V}{\partial x}$ suggests traveling wave:

$$V(x,\tau) = F\left(x - \left(r - \frac{\sigma^2}{2}\right)\tau\right)$$



### **Moving Frame**

In the frame moving with velocity $v = r - \frac{\sigma^2}{2}$:

$$\xi = x - v\tau = \ln(S/K) - \left(r - \frac{\sigma^2}{2}\right)\tau$$



The PDE simplifies, revealing the **stationary structure**.

---

## **9. Explicit Example: European Call**

### **Terminal Condition**


$$V(S,T) = (S - K)^+ = K(e^x - 1)^+$$



In similarity variable $\xi = \frac{x}{\sigma\sqrt{\tau}}$:

$$V(x,0) = K(e^{\sigma\sqrt{\tau}\xi} - 1)^+ \quad \text{at } \tau = 0$$



As $\tau \to 0$:

$$e^{\sigma\sqrt{\tau}\xi} \approx 1 + \sigma\sqrt{\tau}\xi \to \begin{cases} 1 & \xi > 0 \\ 1 & \xi < 0 \end{cases}$$



### **Problem**

The terminal condition is **not self-similar**! It doesn't have the form $g(\xi)$ at $\tau = 0$.

### **Resolution**

The **full solution** is not purely self-similar—it's a **superposition**:

$$V(x,\tau) = \int_{-\infty}^{\infty}G(x-y,\tau)\Phi(y)dy$$



where $G$ is the self-similar fundamental solution.

### **Black-Scholes Formula**

After transformation and integration:

$$\boxed{C(S,t) = SN(d_1) - Ke^{-r\tau}N(d_2)}$$



where $d_1, d_2$ are the **similarity variables**:

$$d_1 = \frac{\ln(S/K) + (r + \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}$$




$$d_2 = \frac{\ln(S/K) + (r - \frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}} = d_1 - \sigma\sqrt{\tau}$$



The structure $N(d_1), N(d_2)$ reflects the underlying **similarity symmetry**!

---

## **10. Self-Similar Barrier Options**

### **Absorbing Barrier**

For a barrier at $S = B$, the condition $V(B,t) = 0$ in similarity variables:

$$V\left(B, t\right) = Kg\left(\frac{\ln(B/K)}{\sigma\sqrt{\tau}}\right) = 0$$



This requires:

$$g\left(\frac{\ln(B/K)}{\sigma\sqrt{\tau}}\right) = 0 \quad \forall \tau$$



This is **impossible** unless $B = K$ (barrier at strike)!

### **Power-Law Similarity**

Try modified ansatz:

$$V(S,t) = S^\alpha f(\xi)$$



where $\alpha$ is chosen to satisfy boundary conditions.

For down-and-out with barrier $B$:

$$\alpha = \frac{2r}{\sigma^2}$$



gives the correct scaling.

### **Method of Images**

The similarity structure suggests:

$$V_{DO}(S,t) = V(S,t) - \left(\frac{B}{S}\right)^{2r/\sigma^2}V\left(\frac{B^2}{S}, t\right)$$



The exponent $2r/\sigma^2$ comes from **dimensional analysis** and **scale invariance**!

---

## **11. Higher-Dimensional Similarity**

### **Two-Asset Problem**

For options on $S_1, S_2$ with **uncorrelated** dynamics:

$$\frac{\partial V}{\partial t} + \sum_{i=1,2}\left[rS_i\frac{\partial V}{\partial S_i} + \frac{\sigma_i^2 S_i^2}{2}\frac{\partial^2 V}{\partial S_i^2}\right] - rV = 0$$



### **Similarity Variables**

Define:

$$\xi_1 = \frac{\ln(S_1/K_1)}{\sigma_1\sqrt{\tau}}, \quad \xi_2 = \frac{\ln(S_2/K_2)}{\sigma_2\sqrt{\tau}}$$



### **Product Form**

Try:

$$V(S_1, S_2, t) = K_1 K_2 g(\xi_1, \xi_2)$$



The PDE separates into:

$$\frac{\partial g}{\partial\tau} = L_1 g + L_2 g$$



where $L_i$ are the one-dimensional operators.

For **basket options** $(w_1 S_1 + w_2 S_2 - K)^+$, similarity variable:

$$\xi = \frac{w_1 S_1 + w_2 S_2}{K\sqrt{\tau}}$$



approximates the solution structure.

---

## **12. Asymptotics and Similarity**

### **Short-Time Asymptotics**

As $\tau \to 0$, the similarity variable $\xi = \frac{\ln(S/K)}{\sigma\sqrt{\tau}}$ becomes:
- $\xi \to +\infty$ if $S > K$ (ITM)
- $\xi \to -\infty$ if $S < K$ (OTM)
- $\xi = O(1)$ if $S \approx K$ (ATM)

### **ATM Expansion**

For $S \approx K$ (so $\xi = O(1)$):

$$V \approx K\left[N(d_1) - N(d_2)\right] \approx \frac{K\sigma\sqrt{\tau}}{\sqrt{2\pi}}[1 + O(\tau)]$$



This is the **ATM approximation**: $V \sim \sigma\sqrt{\tau}$ (time-value decay).

### **Deep OTM/ITM**

For $|\xi| \gg 1$:

$$N(d_i) \approx \begin{cases} 1 & d_i \to +\infty \\ 0 & d_i \to -\infty \end{cases}$$



Using **Mill's ratio**:

$$1 - N(x) \approx \frac{e^{-x^2/2}}{x\sqrt{2\pi}} \quad \text{for } x \gg 1$$



This gives **exponential decay** in $\xi$.

---

## **13. Connection to Probability Theory**

### **Central Limit Theorem**

The heat kernel:

$$G(x,\tau) = \frac{1}{\sqrt{4\pi\tau}}e^{-x^2/(4\tau)}$$



is the **Gaussian density** with variance $2\tau$.

The similarity variable:

$$\xi = \frac{x}{\sqrt{2\tau}}$$



is the **standardized variable** for the CLT.

### **Large Deviations**

For $\tau \to \infty$ with $x/\tau = v$ fixed:

$$-\frac{1}{\tau}\ln G(x,\tau) \approx \frac{v^2}{4} + \frac{1}{2}\ln(4\pi\tau)$$



The **rate function** $I(v) = v^2/4$ governs large deviations.

### **Scaling Limits**

As $\tau \to 0$ with $\xi = x/\sqrt{\tau}$ fixed, the distribution **concentrates** on $\{\xi = 0\}$, i.e., $S = K$.

This is the **zero-diffusion limit** or **small-noise asymptotics**.

---

## **14. Numerical Methods via Similarity**

### **Sparse Grids**

Using similarity variable $\xi$ instead of $(S,t)$:
- Fewer grid points needed near ATM
- Natural boundary conditions at $\xi \to \pm\infty$
- Adaptive refinement based on $|\xi|$

### **Transformation of Domain**

Map $(S,t) \in (0,\infty) \times [0,T]$ to $(\xi, \tau) \in \mathbb{R} \times [0,T]$.

The "computational domain" is **unbounded** but naturally truncated:

$$\xi \in [-\xi_{\max}, \xi_{\max}]$$



where $\xi_{\max} \approx 5$ captures $99.99\%$ of the distribution.

### **Initial Condition**

Terminal payoff $\Phi(S)$ becomes:

$$\Phi(\xi, 0) = \Phi(Ke^{\sigma\sqrt{\tau}\xi})\bigg|_{\tau=0}$$



As $\tau \to 0$, this is **singular** but well-defined in distributional sense.

---

## **15. Similarity in Stochastic Volatility**

### **Heston Model**


$$dS_t = rS_t dt + \sqrt{v_t}S_t dW_t^{(1)}$$



$$dv_t = \kappa(\theta - v_t)dt + \xi\sqrt{v_t}dW_t^{(2)}$$



### **Quasi-Similarity**

Define:

$$\xi_S = \frac{\ln(S/K)}{\sqrt{v_0\tau}}, \quad \xi_v = \frac{v_t}{v_0}$$



The solution has **approximate** similarity structure:

$$V(S, v, t) \approx K f(\xi_S, \xi_v, \kappa\tau, \xi\sqrt{\tau})$$



Not purely self-similar due to mean-reversion $\kappa$.

### **Long-Time Limit**

As $\tau \to \infty$, $v_t \to \theta$ (mean-reversion), so:

$$V \approx V_{\text{BS}}(S, K, \tau, \sigma = \sqrt{\theta})$$



The similarity structure **emerges** in the long-time limit.

---

## **16. Fractional Diffusion and Anomalous Scaling**

### **Fractional Heat Equation**


$$\frac{\partial u}{\partial t} = (-\Delta)^{\alpha/2}u$$



where $(-\Delta)^{\alpha/2}$ is the **fractional Laplacian**.

### **Scaling**

The fundamental solution:

$$u(x,t) = t^{-1/\alpha}L_\alpha\left(\frac{|x|}{t^{1/\alpha}}\right)$$



where $L_\alpha$ is a **Lévy stable density**.

The similarity variable:

$$\boxed{\xi = \frac{x}{t^{1/\alpha}}}$$



reflects **anomalous diffusion** (subdiffusion $\alpha < 2$, superdiffusion $\alpha > 2$).

### **Rough Volatility**

For **fractional Brownian motion** with Hurst parameter $H$:

$$\text{Var}[B_t^H] \sim t^{2H}$$



The similarity variable scales as:

$$\xi \sim \frac{x}{t^H}$$



---

## **17. Similarity Solutions for American Options**

### **Free Boundary Problem**


$$\max\left\{-\frac{\partial V}{\partial t} - \mathcal{L}V, V - \Phi(S)\right\} = 0$$



with free boundary $S^*(t)$ (optimal exercise).

### **Similarity Variable**

The free boundary has scaling:

$$S^*(t) = K h(\tau)$$



where $h(\tau)$ satisfies an ODE derived from similarity.

### **Perpetual American Put**

For $T \to \infty$ (**perpetual**), time-independence gives:

$$V(S) = (K - S)^+ \text{ or } \mathcal{L}V = 0$$



In the continuation region $S > S^*$:

$$rS\frac{dV}{dS} + \frac{\sigma^2 S^2}{2}\frac{d^2V}{dS^2} - rV = 0$$



Try power-law: $V = AS^\alpha$:

$$\boxed{\alpha = \frac{1}{2} - \frac{r}{\sigma^2} \pm \sqrt{\left(\frac{1}{2} - \frac{r}{\sigma^2}\right)^2 + \frac{2r}{\sigma^2}}}$$



Choose $\alpha < 0$ for boundedness as $S \to \infty$.

### **Optimal Exercise Boundary**

At $S = S^*$:
- **Value matching**: $V(S^*) = K - S^*$
- **Smooth pasting**: $V'(S^*) = -1$

These determine $A$ and $S^*$:

$$\boxed{S^* = \frac{\alpha}{\alpha - 1}K}$$



The ratio $S^*/K$ is **constant** (time-independent similarity).

---

## **18. Dimensional Analysis for Exotic Options**

### **Lookback Option**

Payoff: $S_{\max} - S_T$ where $S_{\max} = \max_{0 \leq t \leq T}S_t$.

**Dimensionless variables**:

$$\pi_1 = \frac{S}{S_{\max}}, \quad \pi_2 = \frac{S_{\max}}{K}, \quad \pi_3 = \sigma\sqrt{\tau}$$



Value:

$$V = S_{\max} \cdot f\left(\frac{S}{S_{\max}}, \sigma\sqrt{\tau}, r\tau\right)$$



### **Asian Option**

Payoff depends on average $A = \frac{1}{T}\int_0^T S_t dt$.

**Dimensionless**:

$$\pi_1 = \frac{S}{K}, \quad \pi_2 = \frac{A}{K}, \quad \pi_3 = \sigma\sqrt{\tau}$$



Value:

$$V = K \cdot f\left(\frac{S}{K}, \frac{A}{K}, \sigma\sqrt{\tau}, r\tau\right)$$



The average $A$ introduces an **additional state variable**, breaking simple similarity.

---

## **19. Group Invariants and Similarity**

### **Invariant Theory**

Under the scaling group $G$:

$$g: (S, K, V, t) \to (\lambda S, \lambda K, \lambda V, t)$$



The **invariants** are:

$$I_1 = \frac{S}{K}, \quad I_2 = \frac{V}{K}, \quad I_3 = t$$



All functions of these invariants are invariant under $G$.

### **Complete Set**

The **fundamental theorem**: Any $G$-invariant function can be expressed as a function of the complete set of invariants.

For Black-Scholes:

$$V = K \cdot f\left(\frac{S}{K}, \sigma\sqrt{T-t}, r(T-t)\right)$$



is the **most general form**.

### **Differential Invariants**

Higher-order invariants:

$$J_1 = S\frac{\partial V}{\partial S}, \quad J_2 = S^2\frac{\partial^2 V}{\partial S^2}$$



The Greeks $\Delta, \Gamma$ are **differential invariants**!

---

## **20. Comparison with Other Methods**

### **Similarity vs. Fourier**

| **Aspect** | **Similarity** | **Fourier** |
|------------|----------------|-------------|
| Reduction | PDE → ODE | PDE → algebraic |
| Domain | Infinite natural | Infinite natural |
| Variables | $\xi = x/\sqrt{\tau}$ | $\omega$ (frequency) |
| Solution | Asymptotic structure | Exact formula |
| Intuition | Scaling/geometry | Spectral decomposition |

### **Similarity vs. Separation**

| **Aspect** | **Similarity** | **Separation** |
|------------|----------------|----------------|
| Ansatz | $V = f(\xi(x,t))$ | $V = X(x)T(t)$ |
| Reduction | 1 variable fewer | Independent ODEs |
| Spectrum | N/A | Discrete/continuous |
| Generality | Special solutions | Complete basis |

### **When Similarity Works**

**Best for**:
1. **Scale-invariant problems** (homogeneous PDEs)
2. **Fundamental solutions** (heat kernel, Green's functions)
3. **Asymptotic analysis** (small/large time behavior)
4. **Dimensional analysis** (parameter reduction)
5. **Conceptual understanding** (scaling laws)

**Limited for**:
1. **Inhomogeneous PDEs** (source terms)
2. **General boundary conditions** (non-self-similar)
3. **Time-dependent parameters** ($\sigma(t), r(t)$)
4. **Path-dependent options** (multiple state variables)

---

## **21. The Deep Structure**

### **Why Similarity Exists**

Similarity solutions arise when the PDE admits a **one-parameter group** of transformations:

$$\phi_\lambda: (x, t, u) \to (X(x,t,\lambda), T(x,t,\lambda), U(x,t,u,\lambda))$$



leaving the PDE invariant.

For Black-Scholes:
- **Scaling group**: $(S, K, V) \to (\lambda S, \lambda K, \lambda V)$
- **Time translation**: $t \to t + c$
- **Combined**: Similarity variables

### **Noether's Theorem Analog**

In PDE theory, **symmetries** ↔ **conservation laws** ↔ **similarity reductions**.

Each symmetry gives:
1. A **conservation law** (for hyperbolic PDEs)
2. A **similarity reduction** (reduction of variables)
3. **Invariant solutions** (special solution families)

### **The Fundamental Principle**


$$\boxed{\text{Scaling symmetry} \iff \text{Homogeneity} \iff \text{Similarity variable} \iff \text{Dimensional analysis}}$$



These are **four perspectives** on the **same mathematical structure**.

---

## **22. Summary: The Similarity Paradigm**

### **Key Insights**

1. **Black-Scholes is scale-invariant**: Multiply all dollar amounts by $\lambda$, solution scales proportionally

2. **Similarity variable**: $\xi = \frac{\ln(S/K)}{\sigma\sqrt{\tau}}$ is the "natural" coordinate

3. **Reduction to ODE**: Heat equation $\to$ ODE for Gaussian kernel

4. **Black-Scholes formula**: Structure $N(d_1), N(d_2)$ reflects similarity symmetry

5. **Greeks are invariants**: $\Delta, \Gamma$ scale correctly under transformations

### **The Master Formulas**

**Similarity variable**:

$$\boxed{\xi = \frac{\ln(S/K)}{\sigma\sqrt{\tau}}}$$



**Heat kernel**:

$$\boxed{G(\xi) = \frac{1}{\sqrt{2\pi}}e^{-\xi^2/2}}$$



**General solution**:

$$\boxed{V(S,t) = K\int_{-\infty}^{\infty}g(\xi')\frac{e^{-(\xi-\xi')^2/2}}{\sqrt{2\pi}}d\xi'}$$



**Black-Scholes structure**:

$$\boxed{C = SN(d_1) - Ke^{-r\tau}N(d_2)}$$



where $d_1, d_2$ are **similarity coordinates**.

### **The Philosophy**

Similarity solutions reveal that **option prices depend on ratios, not absolutes**:
- Not $S$ and $K$ separately, but $S/K$ (moneyness)
- Not $\tau$ and $\sigma$ separately, but $\sigma\sqrt{\tau}$ (total volatility)
- Not absolute prices, but **dimensionless combinations**

This is the **geometric essence** of option pricing!

---

Would you like me to explore:
- Detailed Lie group analysis for Black-Scholes symmetries
- Similarity methods for path-dependent options (Asian, lookback)
- Asymptotic expansions using similarity structure
- Connection to renormalization group methods in physics
- Optimal system of subalgebras for Black-Scholes
- Similarity solutions for transaction cost models
- Extensions to rough volatility and fractional processes?
