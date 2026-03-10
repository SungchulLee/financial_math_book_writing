# Chapter 2: Stochastic Processes


!!! warning "Incomplete page"
    This page is missing the required five-section structure (Concept Definition, Explanation, Diagram / Example). Content needs to be reorganized and expanded.

This chapter develops the probabilistic machinery underlying continuous-time finance. Beginning with the simple random walk, we construct Brownian motion as its scaling limit via Donsker's theorem, study its path properties and moment structure, and then build the theory of filtrations, conditional expectation, martingales, and stopping times that governs information flow and fair pricing in stochastic models.

## Key Concepts

### **Random Walks**
The simple symmetric random walk

$$S_n = \sum_{i=1}^n X_i$$

with $\mathbb{P}(X_i = \pm 1) = 1/2$ serves as the discrete precursor to Brownian motion. Its fundamental properties include $\mathbb{E}[S_n] = 0$, $\text{Var}(S_n) = n$, and $\mathbb{E}[S_n^4] = 3n^2 - 2n$. The general asymmetric walk with parameter $p$ has $\mathbb{E}[S_n] = n(2p-1)$ and $\text{Var}(S_n) = 4np(1-p)$. Random walks model gambler's winnings, particle displacement, and discrete-time price changes (Bachelier, 1900).

### **Donsker's Theorem and the Construction of Brownian Motion**
**Donsker's theorem** (the functional central limit theorem) establishes that the rescaled walk

$$W^{(n)}_t = \frac{1}{\sqrt{n}} S_{\lfloor nt \rfloor}$$

converges weakly in $C[0,T]$ to standard Brownian motion. This is not merely convergence of marginal distributions but convergence of entire path functionals, justifying Monte Carlo simulation via discrete approximations. The theorem explains the universality of Brownian motion: it arises as the diffusive scaling limit of any random walk with finite variance increments, regardless of the specific step distribution. Historically, Wiener (1923) first constructed Brownian motion as a measure on path space, Kolmogorov (1933) provided abstract existence via consistent finite-dimensional distributions, Donsker (1951) established universality, and Levy characterized fine path properties through the law of the iterated logarithm and local time theory.

### **Brownian Motion: Definition and Moment Structure**
Standard Brownian motion $\{W_t\}_{t \geq 0}$ is the unique process satisfying:

- (i) $W_0 = 0$
- (ii) independent increments
- (iii) $W_t - W_s \sim \mathcal{N}(0, t-s)$
- (iv) continuous paths a.s.

Its moment structure follows from the Gaussian moment generating function $\mathbb{E}[e^{\theta W_t}] = \exp(\frac{1}{2}\theta^2 t)$:

$$\mathbb{E}[W_t^{2k}] = \frac{(2k)!}{2^k k!}\, t^k$$

for even moments, with all odd moments vanishing by symmetry. The covariance structure $\mathbb{E}[W_s W_t] = \min(s,t)$ fully characterizes the Gaussian process.

### **Scaling, Time Change, and Self-Similarity**
Brownian motion exhibits **self-similarity**:

$$W_{ct} \overset{d}{=} \sqrt{c}\, W_t$$

implying no intrinsic time scale. The typical increment over time $\Delta t$ satisfies $\mathbb{E}[|W_{t+\Delta t} - W_t|^2] = \Delta t$, so the heuristic $dW_t \sim \sqrt{dt}$ governs the scaling of stochastic calculus. **Deterministic time change** via a continuous increasing function $\phi(t)$ produces new Gaussian processes $W_{\phi(t)}$. The profound **Dambis-Dubins-Schwarz theorem** extends this to random time changes, showing that every continuous local martingale $M_t$ can be represented as Brownian motion evaluated at its quadratic variation: $M_t = B_{\langle M \rangle_t}$ for some Brownian motion $B$.

### **Path Properties**
Brownian paths exhibit a striking duality: they are continuous yet nowhere differentiable (a.s.), and Holder continuous of order $\alpha < 1/2$ but not $\alpha = 1/2$. The **quadratic variation**

$$\langle W \rangle_t = t$$

is the hallmark property that distinguishes stochastic from classical calculus and gives rise to the Ito correction term. While paths have infinite first variation (total variation), the sum of squared increments $\sum (W_{t_{k+1}} - W_{t_k})^2$ converges to $t$ as the partition mesh tends to zero. This non-vanishing quadratic variation is the fundamental reason why second-order terms survive in stochastic Taylor expansions.

### **Reflection Principle and First Passage Times**
The reflection principle exploits path symmetry to compute

$$\mathbb{P}\!\left(\max_{0 \leq s \leq t} W_s \geq a\right) = 2\,\mathbb{P}(W_t \geq a)$$

for $a > 0$, via a pathwise bijection that reflects the portion of each path after the first hitting time $\tau_a = \inf\{s \geq 0 : W_s = a\}$ across level $a$. This yields the first passage time density

$$f_{\tau_a}(t) = \frac{|a|}{\sqrt{2\pi t^3}} \exp\!\left(-\frac{a^2}{2t}\right)$$

an inverse Gaussian distribution with survival probability $\mathbb{P}(\tau_a > t) = 2\Phi(-|a|/\sqrt{t})$. These results directly apply to barrier option pricing (knock-in, knock-out), credit risk modeling (default times as first passage), drawdown analysis, and optimal stopping problems.

### **Filtrations and Adapted Processes**
A filtration $(\mathcal{F}_t)_{t \geq 0}$ models the gradual revelation of information: $\mathcal{F}_t$ encodes precisely what can be known at time $t$, built from sigma-algebras $\sigma(X)$ generated by observable random variables. The filtration satisfies the **usual conditions** (right-continuity and completeness). Processes are **adapted** if $X_t$ is $\mathcal{F}_t$-measurable (no looking into the future), and **progressively measurable** if the joint map $(s, \omega) \mapsto X_s(\omega)$ is measurable on $[0,t] \times \Omega$ with respect to $\mathcal{B}([0,t]) \otimes \mathcal{F}_t$. This hierarchy---adaptedness, progressive measurability, predictability, and optional measurability---ensures that trading strategies and stochastic integrals are well-defined. A process like $X_t = W_1$ (constant equal to the time-1 value) is not adapted for $t < 1$, illustrating that adaptedness prohibits foresight.

### **Martingale Theory**
A martingale satisfies $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ for $s \leq t$---the best prediction of the future is the present. This "fair game" principle has profound consequences for pricing and convergence theory. Brownian motion $W_t$ is a martingale, as are the compensated square

$$W_t^2 - t$$

and the exponential martingale

$$\exp(\theta W_t - \tfrac{1}{2}\theta^2 t)$$

### **Submartingales** (E[M_t | F_s] ≥ M_s) and **supermartingales** (E[M_t | F_s] ≤ M_s) model systematically favorable and unfavorable games respectively. Jensen's inequality connects these: if M_t is a martingale and φ is convex, then φ(M_t) is a submartingale.

### **Stopping Times and Optional Sampling**
A **stopping time** $\tau$ satisfies $\{\tau \leq t\} \in \mathcal{F}_t$ for all $t$---the decision to stop can be made using only currently available information. The **Optional Sampling Theorem** extends the martingale property to bounded stopping times $\sigma \leq \tau \leq T$:

$$\mathbb{E}[M_\tau \mid \mathcal{F}_\sigma] = M_\sigma$$

This result is fundamental for option pricing: the fair price of a derivative at any stopping time equals the conditional expectation of its future value under the risk-neutral measure.

### **Doob's Maximal Inequality**
For $p > 1$, the running maximum of a martingale is controlled by its terminal value:

$$\mathbb{E}\!\left[\sup_{s \leq t} |M_s|^p\right] \leq \left(\frac{p}{p-1}\right)^p \mathbb{E}[|M_t|^p]$$

This $L^p$ inequality bounds the extremal behavior of martingales over entire intervals, essential for controlling stochastic integrals and proving convergence results.

### **Martingale Convergence and Uniform Integrability**
Bounded $L^1$ martingales converge almost surely, controlled by Doob's **upcrossing inequality**: for a submartingale $\{X_n\}$, the expected number of upcrossings of $[a,b]$ satisfies $(b-a)\mathbb{E}[U_N^{[a,b]}] \leq \mathbb{E}[(X_N - a)^+]$. **Uniform integrability** bridges almost sure and $L^1$ convergence: a family $\{X_\alpha\}$ is uniformly integrable if $\sup_\alpha \mathbb{E}[|X_\alpha| \mathbf{1}_{\{|X_\alpha| > K\}}] \to 0$ as $K \to \infty$. Uniformly integrable martingales converge both a.s. and in $L^1$, and are precisely the martingales that can be "closed" by an integrable terminal random variable.

### **Doob-Meyer Decomposition**
Every submartingale uniquely decomposes into a martingale $M_t$ and a predictable increasing process $A_t$:

$$X_t = M_t + A_t$$

This separation of "signal from noise" is the structural foundation for semimartingale theory: it explains why Ito processes decompose into drift (predictable, finite variation) and martingale (stochastic integral) parts. In discrete time, the decomposition is elementary: $A_n = \sum_{k=1}^n \mathbb{E}[X_k - X_{k-1} \mid \mathcal{F}_{k-1}]$. In continuous time, the deeper Doob-Meyer theorem requires right-continuous submartingales of class (DL).

!!! note "Role in the Book"
    Brownian motion and martingale theory developed here are the essential prerequisites for stochastic calculus (Chapter 3), measure changes and Girsanov's theorem (Chapter 4), and the Feynman-Kac connection between PDEs and expectations (Chapter 5).

---
