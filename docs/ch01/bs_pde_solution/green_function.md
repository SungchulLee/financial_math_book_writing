# Green's Function Method: Complete Mathematical Treatment

The Green's function approach is profoundly elegant—it reduces option pricing to **convolution with a fundamental solution**, revealing the deep connection between PDEs and probability theory.

---

## **1. Green's Function for Parabolic PDEs**

### **Definition**

For the general parabolic PDE:
$$\frac{\partial u}{\partial t} + \mathcal{L}u = 0$$

with terminal condition $u(x,T) = \Phi(x)$, the **Green's function** $G(x,t;y,T)$ satisfies:

$$\frac{\partial G}{\partial t} + \mathcal{L}_x G = 0$$

with **initial condition** (in the Dirac sense):
$$\lim_{t \to T^-} G(x,t;y,T) = \delta(x-y)$$

where $\delta$ is the Dirac delta function.

### **Solution Representation**

The solution is then:
$$\boxed{u(x,t) = \int_{-\infty}^{\infty} G(x,t;y,T)\Phi(y)dy}$$

This is a **convolution** of the payoff with the Green's function.

### **Probabilistic Interpretation**

$G(x,t;y,T)$ is the **transition probability density**: the probability of going from state $x$ at time $t$ to state $y$ at time $T$.

---

## **2. Green's Function for Black-Scholes**

### **The Black-Scholes Operator**

$$\mathcal{L} = rS\frac{\partial}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2}{\partial S^2} - r$$

The PDE is:
$$\frac{\partial V}{\partial t} + \mathcal{L}V = 0$$

### **Terminal Value Problem**

We seek $G(S,t;S',T)$ such that:
$$\frac{\partial G}{\partial t} + rS\frac{\partial G}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 G}{\partial S^2} - rG = 0$$

with:
$$\lim_{t \to T^-}G(S,t;S',T) = \delta(S-S')$$

### **Solution Formula**

$$\boxed{V(S,t) = \int_0^{\infty} G(S,t;S',T)\Phi(S')dS'}$$

For discounting, we use:
$$\boxed{V(S,t) = e^{-r(T-t)}\int_0^{\infty} G^{\mathbb{Q}}(S,t;S',T)\Phi(S')dS'}$$

where $G^{\mathbb{Q}}$ is the transition density under the risk-neutral measure.

---

## **3. Deriving the Explicit Green's Function**

### **Method 1: From the Risk-Neutral SDE**

Under $\mathbb{Q}$:
$$dS_t = rS_t dt + \sigma S_t dW_t^{\mathbb{Q}}$$

Apply Itô's lemma to $X_t = \ln S_t$:
$$dX_t = \left(r - \frac{\sigma^2}{2}\right)dt + \sigma dW_t^{\mathbb{Q}}$$

This is **arithmetic Brownian motion** with drift $\mu = r - \frac{\sigma^2}{2}$ and volatility $\sigma$.

### **Transition Density for Arithmetic BM**

For $dX_t = \mu dt + \sigma dW_t$, the transition density is:
$$p_X(x,t;y,T) = \frac{1}{\sigma\sqrt{2\pi(T-t)}}\exp\left[-\frac{(y-x-\mu(T-t))^2}{2\sigma^2(T-t)}\right]$$

### **Change of Variables: $X \to S$**

Since $S' = e^{X'}$, we have $dS' = e^{X'}dX'$, so:
$$p_S(S,t;S',T)dS' = p_X(\ln S, t; \ln S', T)dX'$$

$$p_S(S,t;S',T) = p_X(\ln S, t; \ln S', T)\frac{dX'}{dS'} = p_X(\ln S, t; \ln S', T)\frac{1}{S'}$$

### **Explicit Formula**

$$\boxed{G^{\mathbb{Q}}(S,t;S',T) = \frac{1}{S'\sigma\sqrt{2\pi\tau}}\exp\left[-\frac{\left(\ln(S'/S) - (r-\frac{\sigma^2}{2})\tau\right)^2}{2\sigma^2\tau}\right]}$$

where $\tau = T - t$.

This is the **lognormal transition density**.

### **Alternative Form**

Define:
$$m = \ln S + \left(r - \frac{\sigma^2}{2}\right)\tau, \quad v^2 = \sigma^2\tau$$

Then:
$$G^{\mathbb{Q}}(S,t;S',T) = \frac{1}{S'v\sqrt{2\pi}}\exp\left[-\frac{(\ln S' - m)^2}{2v^2}\right]$$

This shows $\ln S' \mid S \sim N(m, v^2)$.

---

## **4. Method 2: Transform to Heat Equation**

### **From Heat Equation Green's Function**

Recall the transformations:
$$x = \ln(S/K), \quad y = \ln(S'/K), \quad \tau = \frac{\sigma^2}{2}(T-t)$$

The heat equation Green's function is:
$$G_{\text{heat}}(x,y,\tau) = \frac{1}{\sqrt{4\pi\tau}}e^{-\frac{(y-x)^2}{4\tau}}$$

### **Including the Exponential Factors**

With $u = e^{\alpha x + \beta\tau}w$, we had:
$$\alpha = -\frac{k-1}{2}, \quad \beta = -\frac{(k+1)^2}{4}, \quad k = \frac{2r}{\sigma^2}$$

The full Green's function in $(x,\tau)$ variables:
$$G_u(x,y,\tau) = e^{\alpha(y-x) + \beta\tau}G_{\text{heat}}(x,y,\tau)$$

### **Back to $(S,S',t)$ Variables**

The Jacobian gives:
$$G(S,t;S',T) = G_u(\ln(S/K), \ln(S'/K), \tau) \cdot \frac{1}{KS'} \cdot K$$

$$= \frac{1}{S'}e^{\alpha(\ln(S'/K) - \ln(S/K)) + \beta\tau}G_{\text{heat}}$$

Substituting $\alpha, \beta, \tau$:
$$G(S,t;S',T) = \frac{1}{S'\sigma\sqrt{2\pi(T-t)}}\exp\left[-\frac{(\ln(S'/S) - (r-\frac{\sigma^2}{2})(T-t))^2}{2\sigma^2(T-t)} - r(T-t)\right]$$

The $e^{-r(T-t)}$ factor is the **discounting**.

The undiscounted transition density is:
$$\tilde{G}(S,t;S',T) = e^{r(T-t)}G(S,t;S',T)$$

which matches our earlier formula.

---

## **5. Properties of the Green's Function**

### **Property 1: Normalization**

$$\int_0^{\infty} G^{\mathbb{Q}}(S,t;S',T)dS' = 1$$

This ensures probability conservation.

**Proof**: Let $X = \ln S', \mu = r - \frac{\sigma^2}{2}, v = \sigma\sqrt{\tau}$:
$$\int_0^{\infty}\frac{1}{S'v\sqrt{2\pi}}e^{-\frac{(\ln S' - m)^2}{2v^2}}dS' = \int_{-\infty}^{\infty}\frac{1}{v\sqrt{2\pi}}e^{-\frac{(X - m)^2}{2v^2}}dX = 1$$

### **Property 2: Semigroup Property (Chapman-Kolmogorov)**

$$G(S,t;S'',T) = \int_0^{\infty} G(S,t;S',s)G(S',s;S'',T)dS'$$

for $t < s < T$.

This is the **law of total probability** for Markov processes.

### **Property 3: Adjoint Symmetry**

Define the **adjoint Green's function**:
$$G^*(S,t;S',T) = e^{-r(T-t)}\frac{S}{S'}G^{\mathbb{Q}}(S',T-t;S,0)$$

For time-homogeneous processes, this relates forward and backward equations.

### **Property 4: First Moment**

$$\int_0^{\infty} S' \cdot G^{\mathbb{Q}}(S,t;S',T)dS' = Se^{r\tau}$$

This confirms the **risk-neutral drift**: $\mathbb{E}^{\mathbb{Q}}[S_T \mid S_t] = S_t e^{r(T-t)}$.

**Proof**: Using $S' = Se^X$ where $X \sim N((r-\frac{\sigma^2}{2})\tau, \sigma^2\tau)$:
$$\mathbb{E}[S'] = S\mathbb{E}[e^X] = S\exp\left[\left(r-\frac{\sigma^2}{2}\right)\tau + \frac{\sigma^2\tau}{2}\right] = Se^{r\tau}$$

### **Property 5: Second Moment**

$$\int_0^{\infty} (S')^2 \cdot G^{\mathbb{Q}}(S,t;S',T)dS' = S^2e^{(2r+\sigma^2)\tau}$$

This gives the variance: $\text{Var}(S_T) = S^2e^{2r\tau}(e^{\sigma^2\tau} - 1)$.

---

## **6. Solving for Call and Put Options**

### **European Call**

$$C(S,t) = e^{-r\tau}\int_0^{\infty}(S' - K)^+ G^{\mathbb{Q}}(S,t;S',T)dS'$$

$$= e^{-r\tau}\int_K^{\infty}(S' - K)G^{\mathbb{Q}}(S,t;S',T)dS'$$

$$= e^{-r\tau}\left[\int_K^{\infty}S' G^{\mathbb{Q}} dS' - K\int_K^{\infty}G^{\mathbb{Q}}dS'\right]$$

### **First Integral: $I_1 = \int_K^{\infty}S' G^{\mathbb{Q}} dS'$**

Let $X = \ln(S'/S)$, so $S' = Se^X$ and $dS' = Se^X dX$:

$$I_1 = \int_{\ln(K/S)}^{\infty}Se^X \cdot \frac{1}{\sigma\sqrt{2\pi\tau}}e^{-\frac{(X - (r-\frac{\sigma^2}{2})\tau)^2}{2\sigma^2\tau}}Se^X dX$$

$$= S\int_{\ln(K/S)}^{\infty}\frac{e^X}{\sigma\sqrt{2\pi\tau}}e^{-\frac{(X - (r-\frac{\sigma^2}{2})\tau)^2}{2\sigma^2\tau}}dX$$

Complete the square in the exponent:
$$X - \frac{(X - (r-\frac{\sigma^2}{2})\tau)^2}{2\sigma^2\tau} = -\frac{(X - (r+\frac{\sigma^2}{2})\tau)^2}{2\sigma^2\tau} + r\tau$$

Therefore:
$$I_1 = Se^{r\tau}\int_{\ln(K/S)}^{\infty}\frac{1}{\sigma\sqrt{2\pi\tau}}e^{-\frac{(X - (r+\frac{\sigma^2}{2})\tau)^2}{2\sigma^2\tau}}dX$$

Change of variables: $Z = \frac{X - (r+\frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}$:

$$I_1 = Se^{r\tau}\int_{\frac{\ln(K/S) - (r+\frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}}^{\infty}\frac{1}{\sqrt{2\pi}}e^{-Z^2/2}dZ$$

$$= Se^{r\tau}N\left(\frac{\ln(S/K) + (r+\frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}}\right)$$

$$= Se^{r\tau}N(d_1)$$

### **Second Integral: $I_2 = \int_K^{\infty}G^{\mathbb{Q}}dS'$**

This is just the probability:
$$I_2 = \mathbb{Q}(S_T > K \mid S_t = S) = N(d_2)$$

where:
$$d_2 = \frac{\ln(S/K) + (r-\frac{\sigma^2}{2})\tau}{\sigma\sqrt{\tau}} = d_1 - \sigma\sqrt{\tau}$$

### **Black-Scholes Call Formula**

$$C(S,t) = e^{-r\tau}[Se^{r\tau}N(d_1) - KN(d_2)]$$

$$\boxed{C(S,t) = SN(d_1) - Ke^{-r\tau}N(d_2)}$$

### **European Put**

$$P(S,t) = e^{-r\tau}\int_0^{K}(K - S')G^{\mathbb{Q}}(S,t;S',T)dS'$$

Following similar calculations:
$$\boxed{P(S,t) = Ke^{-r\tau}N(-d_2) - SN(-d_1)}$$

---

## **7. Green's Function for General Payoffs**

### **Digital (Binary) Options**

**Cash-or-nothing call**: Pays $1$ if $S_T > K$, else $0$.

$$V_{\text{digital}}(S,t) = e^{-r\tau}\int_K^{\infty}G^{\mathbb{Q}}(S,t;S',T)dS' = e^{-r\tau}N(d_2)$$

**Asset-or-nothing call**: Pays $S_T$ if $S_T > K$, else $0$.

$$V_{\text{asset}}(S,t) = e^{-r\tau}\int_K^{\infty}S' G^{\mathbb{Q}}(S,t;S',T)dS' = SN(d_1)$$

Note: $C = V_{\text{asset}} - K \cdot V_{\text{digital}}$ ✓

### **Power Options**

Payoff: $(S_T^n - K)^+$

$$V(S,t) = e^{-r\tau}\int_K^{1/n}(S'^n - K)G^{\mathbb{Q}}(S,t;S',T)dS'$$

Need to compute:
$$\mathbb{E}^{\mathbb{Q}}[S_T^n] = S^n e^{n(r + \frac{n-1}{2}\sigma^2)\tau}$$

using the moment generating function of lognormal.

### **Exotic Payoffs via Numerical Integration**

For arbitrary payoff $\Phi(S')$:
$$V(S,t) = e^{-r\tau}\int_0^{\infty}\Phi(S')G^{\mathbb{Q}}(S,t;S',T)dS'$$

Use **Gaussian quadrature** or **FFT** for numerical evaluation.

---

## **8. Method of Images for Barrier Options**

### **Down-and-Out Call**

Payoff: $(S_T - K)^+$ if $S_t > B$ for all $t \in [0,T]$, else $0$ (where $B < S < K$).

### **The Barrier Condition**

We need:
$$G_{\text{barrier}}(S,t;S',T) = 0 \quad \text{when } S = B$$

This is a **Dirichlet boundary condition**.

### **Method of Images Construction**

For the heat equation with boundary $G(0,t) = 0$, the solution is:
$$G_{\text{barrier}}(x,t;y,T) = G(x,t;y,T) - G(-x,t;y,T)$$

This is the **reflection principle**.

### **For Black-Scholes (Lognormal)**

The barrier at $S = B$ corresponds to $x = \ln(B/K)$ in log-space.

The "image" stock price is:
$$S_{\text{image}} = \frac{B^2}{S}$$

The Green's function for the down-and-out option is:
$$\boxed{G_{\text{DO}}(S,t;S',T) = G^{\mathbb{Q}}(S,t;S',T) - \left(\frac{B}{S}\right)^{2r/\sigma^2}G^{\mathbb{Q}}\left(\frac{B^2}{S},t;S',T\right)}$$

The exponent $\lambda = \frac{2r}{\sigma^2}$ comes from the **change of measure** needed to preserve the drift.

### **Down-and-Out Call Price**

$$C_{\text{DO}}(S,t) = e^{-r\tau}\int_K^{\infty}(S' - K)G_{\text{DO}}(S,t;S',T)dS'$$

$$= C_{\text{BS}}(S,K,t) - \left(\frac{B}{S}\right)^{2r/\sigma^2}C_{\text{BS}}\left(\frac{B^2}{S},K,t\right)$$

where $C_{\text{BS}}$ is the standard Black-Scholes call.

### **Geometric Interpretation**

The method of images exploits the **symmetry** of Brownian motion:
- The probability of hitting the barrier equals the probability of the reflected path
- Subtract the reflected contribution to enforce zero value at the barrier

---

## **9. Eigenfunction Expansion**

### **Spectral Decomposition**

The Green's function can be expressed as:
$$G(S,t;S',T) = \sum_{n=0}^{\infty}e^{-\lambda_n(T-t)}\psi_n(S)\psi_n(S')$$

where $\psi_n$ are eigenfunctions of the operator $\mathcal{L}$:
$$\mathcal{L}\psi_n = -\lambda_n\psi_n$$

### **For the Infinite Domain**

The Black-Scholes operator in $x = \ln S$ space:
$$\mathcal{L} = \frac{\sigma^2}{2}\frac{\partial^2}{\partial x^2} + \left(r - \frac{\sigma^2}{2}\right)\frac{\partial}{\partial x} - r$$

This has **continuous spectrum** on $\mathbb{R}$, leading to Fourier transforms rather than discrete eigenfunctions.

### **For Bounded Domains (Barriers)**

With barriers at $S = B_L$ and $S = B_U$, we get discrete eigenvalues:
$$\lambda_n = r + \frac{\sigma^2\pi^2 n^2}{2(\ln B_U - \ln B_L)^2}$$

Eigenfunctions are:
$$\psi_n(S) = \sin\left(\frac{n\pi(\ln S - \ln B_L)}{\ln B_U - \ln B_L}\right)$$

(after appropriate normalization).

### **Solution via Eigenfunction Expansion**

$$V(S,t) = \sum_{n=1}^{\infty}c_n e^{-\lambda_n(T-t)}\psi_n(S)$$

where:
$$c_n = \int_{B_L}^{B_U}\Phi(S')\psi_n(S')w(S')dS'$$

with appropriate weight function $w(S')$.

This is useful for **numerical solutions** and **barrier options**.

---

## **10. Connection to Fourier and Laplace Transforms**

### **Fourier Transform of Green's Function**

Taking the Fourier transform in $\ln S'$:
$$\hat{G}(\omega,t;S,T) = \int_{-\infty}^{\infty}G(S,t;e^y,T)e^{-i\omega y}dy$$

This gives:
$$\hat{G}(\omega,t;S,T) = \exp\left[-i\omega\left(\ln S + \left(r-\frac{\sigma^2}{2}\right)\tau\right) - \frac{\sigma^2\omega^2\tau}{2}\right]$$

This is the **characteristic function** of $\ln S_T$ under $\mathbb{Q}$.

### **Pricing via Characteristic Function**

For any payoff $\Phi(S')$:
$$V(S,t) = e^{-r\tau}\int_0^{\infty}\Phi(S')G^{\mathbb{Q}}(S,t;S',T)dS'$$

$$= \frac{e^{-r\tau}}{2\pi}\int_{-\infty}^{\infty}\hat{\Phi}(\omega)\hat{G}(\omega,t;S,T)e^{i\omega \ln S'}d\omega$$

This is the basis for **FFT pricing methods** (Carr-Madan).

### **Laplace Transform in Time**

Taking Laplace transform in $\tau = T - t$:
$$\tilde{G}(S,S';p) = \int_0^{\infty}e^{-p\tau}G(S,t;S',T)d\tau$$

The PDE becomes an ODE:
$$pV - \Phi(S) + \mathcal{L}V = 0$$

Invert numerically (Gaver-Stehfest algorithm) for time-dependent solutions.

---

## **11. Multi-Dimensional Green's Functions**

### **Basket of $n$ Assets**

Under $\mathbb{Q}$:
$$dS_i = rS_i dt + \sigma_i S_i dW_i^{\mathbb{Q}}, \quad d\langle W_i, W_j \rangle_t = \rho_{ij}dt$$

The joint transition density is:
$$G(\mathbf{S},t;\mathbf{S}',T) = \frac{1}{(2\pi)^{n/2}\sqrt{|\Sigma|\tau}\prod_{i=1}^n S_i'}\exp\left[-\frac{1}{2}(\mathbf{X}' - \mathbf{m})^T\Sigma^{-1}(\mathbf{X}' - \mathbf{m})\right]$$

where:
- $X_i = \ln S_i$
- $\mathbf{m} = \ln \mathbf{S} + (r - \frac{\sigma^2}{2})\tau \mathbf{1}$
- $\Sigma_{ij} = \rho_{ij}\sigma_i\sigma_j\tau$

This is a **multivariate lognormal** distribution.

### **Basket Option Pricing**

$$V(\mathbf{S},t) = e^{-r\tau}\int_{\mathbb{R}_+^n}\Phi(\mathbf{S}')G(\mathbf{S},t;\mathbf{S}',T)d\mathbf{S}'$$

For max-options, spread options, etc., this generally requires **Monte Carlo** or **multidimensional quadrature**.

---

## **12. Time-Dependent Parameters**

### **Stochastic Volatility Context**

If $\sigma = \sigma(t)$ is deterministic:

$$G(S,t;S',T) = \frac{1}{S'\sqrt{2\pi v^2(t,T)}}\exp\left[-\frac{(\ln(S'/S) - m(t,T))^2}{2v^2(t,T)}\right]$$

where:
$$m(t,T) = \int_t^T\left(r(s) - \frac{\sigma^2(s)}{2}\right)ds$$

$$v^2(t,T) = \int_t^T\sigma^2(s)ds$$

This is the **integrated variance**.

### **Local Volatility**

For $\sigma = \sigma(S,t)$, the Green's function is **not explicitly known** in general.

But it satisfies:
$$\frac{\partial G}{\partial t} + rS\frac{\partial G}{\partial S} + \frac{1}{2}\sigma^2(S,t)S^2\frac{\partial^2 G}{\partial S^2} = 0$$

Solve numerically (Fokker-Planck equation) or use **Dupire's formula**:
$$\sigma^2(K,T) = \frac{2\frac{\partial C}{\partial T}}{K^2\frac{\partial^2 C}{\partial K^2}}$$

---

## **13. Relationship to Kolmogorov Equations**

### **Backward Equation**

The Black-Scholes PDE is the **backward Kolmogorov equation**:
$$-\frac{\partial G}{\partial t} = \mathcal{L}_S G$$

"Backward" means we fix the terminal point $(S',T)$ and vary the initial point $(S,t)$.

### **Forward Equation (Fokker-Planck)**

The **forward Kolmogorov equation** is:
$$\frac{\partial G}{\partial T} = \mathcal{L}^*_{S'} G$$

where $\mathcal{L}^*$ is the **adjoint operator**:
$$\mathcal{L}^* = -\frac{\partial}{\partial S'}(rS' \cdot) + \frac{1}{2}\frac{\partial^2}{\partial S'^2}(\sigma^2 S'^2 \cdot)$$

This describes how the **probability distribution** evolves forward in time.

### **Duality**

For fixed $t < T$:
$$\int_0^{\infty}\phi(S)G(S,t;S',T)\psi(S')dS dS' = \int_0^{\infty}\psi(S')G(S,t;S',T)\phi(S)dS dS'$$

This symmetry relates backward and forward problems.

---

## **14. Numerical Methods Using Green's Functions**

### **Direct Quadrature**

$$V(S,t) = e^{-r\tau}\sum_{i=1}^N w_i \Phi(S_i')G(S,t;S_i',T)$$

where $\{S_i', w_i\}$ are quadrature points and weights.

**Best for**: Smooth payoffs with compact support.

### **Adaptive Integration**

For payoffs with discontinuities (e.g., $(S-K)^+$):
- Refine mesh near the strike $K$
- Use **Gauss-Legendre** or **Clenshaw-Curtis** quadrature

### **Fast Convolution (FFT)**

Since $V = e^{-r\tau}G * \Phi$:

1. Transform to log-space: $x = \ln S$
2. Discretize uniformly: $x_j = x_0 + j\Delta x$
3. Compute FFT of $\Phi(e^{x_j})$
4. Multiply by FFT of $G$
5. Inverse FFT

Complexity: $O(N \log N)$ instead of $O(N^2)$.

---

## **15. Advanced Topics**

### **Path-Dependent Options**

For **Asian options** (average payoff), need joint distribution of $(S_T, A_T)$ where:
$$A_T = \frac{1}{T}\int_0^T S_t dt$$

The Green's function becomes:
$$G(S,A,t;S',A',T)$$

Generally requires **PDE methods** or **Monte Carlo**.

### **American Options**

The free boundary problem:
$$\max\{V - \Phi(S), -\frac{\partial V}{\partial t} - \mathcal{L}V\} = 0$$

The Green's function approach gives:
$$V(S,t) = \sup_{\tau \in [t,T]}\mathbb{E}^{\mathbb{Q}}[e^{-r(\tau-t)}\Phi(S_\tau)]$$

where $\tau$ is an **optimal stopping time**.

### **Stochastic Volatility (Heston)**

$$dS_t = rS_t dt + \sqrt{v_t}S_t dW_t^{(1)}$$
$$dv_t = \kappa(\theta - v_t)dt + \xi\sqrt{v_t}dW_t^{(2)}$$

Green's function $G(S,v,t;S',v',T)$ satisfies a **2D PDE**.

Explicit formula exists using **characteristic functions** (Heston's formula).

---

## **16. Physical vs. Risk-Neutral Green's Functions**

### **Under Physical Measure $\mathbb{P}$**

$$dS_t = \mu S_t dt + \sigma S_t dW_t^{\mathbb{P}}$$

The physical Green's function:
$$G^{\mathbb{P}}(S,t;S',T) = \frac{1}{S'\sigma\sqrt{2\pi\tau}}\exp\left[-\frac{(\ln(S'/S) - (\mu-\frac{\sigma^2}{2})\tau)^2}{2\sigma^2\tau}\right]$$

### **Girsanov Connection**

The two are related by the **Radon-Nikodym derivative**:
$$\frac{d\mathbb{Q}}{d\mathbb{P}} = \exp\left[-\frac{\mu - r}{\sigma}W_T^{\mathbb{P}} - \frac{(\mu-r)^2}{2\sigma^2}T\right]$$

Therefore:
$$G^{\mathbb{Q}}(S,t;S',T) = \frac{d\mathbb{Q}/d\mathbb{P}\big|_{\mathcal{F}_T}}{d\mathbb{Q}/d\mathbb{P}\big|_{\mathcal{F}_t}}G^{\mathbb{P}}(S,t;S',T)$$

This is the **change of measure formula**.

---

## **17. Summary: Why Green's Functions are Powerful**

| **Advantage** | **Explanation** |
|---------------|-----------------|
| **Explicit solution** | Direct formula for any payoff via convolution |
| **Probabilistic meaning** | Green's function = transition density |
| **Handles discontinuities** | Payoff kinks pose no problem (unlike finite differences) |
| **Method of images** | Elegant treatment of barriers |
| **Fourier methods** | FFT for fast computation |
| **Generalizes easily** | Extend to multiple assets, time-dependent parameters |
| **Connects PDE and probability** | Bridges Kolmogorov equations and stochastic processes |

---

## **18. The Deep Connection**

The Green's function reveals the **fundamental duality**:

$$\begin{align}
&\text{PDE (Deterministic)} \quad \leftrightarrow \quad \text{SDE (Stochastic)} \\
&\text{Green's function } G \quad \leftrightarrow \quad \text{Transition density } p \\
&\text{Backward equation} \quad \leftrightarrow \quad \text{Option pricing} \\
&\text{Forward equation} \quad \leftrightarrow \quad \text{Distribution evolution} \\
&\text{Convolution} \quad \leftrightarrow \quad \text{Expectation}
\end{align}$$

### **The Master Formula**

$$\boxed{V(S,t) = \int_0^{\infty}\underbrace{e^{-r(T-t)}}_{\text{Discounting}}\underbrace{\Phi(S')}_{\text{Payoff}}\underbrace{G^{\mathbb{Q}}(S,t;S',T)}_{\text{Transition density}}dS'}$$

This single equation unifies:
- **PDE theory** (Green's function)
- **Probability theory** (expectation)
- **Finance** (risk-neutral valuation)

---

Would you like me to explore:
- Detailed derivation of barrier option formulas via method of images
- FFT implementation for option pricing
- Multi-dimensional Green's functions for basket/spread options
- Connection to characteristic functions and Fourier methods
- Stochastic volatility models (Heston) and their Green's functions?
