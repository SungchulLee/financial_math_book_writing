# Chapter 2: Stochastic Processes

This chapter develops the probabilistic machinery underlying continuous-time finance. Beginning with discrete-time probability and Markov chains, we construct Brownian motion as the scaling limit of random walks, study its path properties and moment structure, and then build the theory of filtrations, martingales, and stopping times that governs information flow and fair pricing in stochastic models.

## Key Concepts

**Discrete-Time Processes**
The measure-theoretic foundations begin with probability spaces $(\Omega, \mathcal{F}, \mathbb{P})$, random variables, and conditional expectation $\mathbb{E}[X \mid \mathcal{G}]$ defined via the Radon-Nikodym theorem. Markov chains introduce the memoryless property 

$$\mathbb{P}(X_{n+1} \mid X_0, \ldots, X_n) = \mathbb{P}(X_{n+1} \mid X_n)$$

 and are characterized by their transition matrices $P = (p_{ij})$. Stationary distributions $\pi P = \pi$ describe long-run behavior, with the Perron-Frobenius theorem guaranteeing existence and uniqueness for irreducible aperiodic chains.

**Brownian Motion**
The simple symmetric random walk 

$$S_n = \sum_{i=1}^n X_i$$

 with $\mathbb{P}(X_i = \pm 1) = 1/2$ serves as the discrete precursor. **Donsker's theorem** (the functional central limit theorem) establishes that the rescaled walk 
 
$$W^{(n)}_t = \frac{1}{\sqrt{n}} S_{\lfloor nt \rfloor}$$
 
  converges weakly in $C[0,T]$ to standard Brownian motion. This is not merely convergence of marginal distributions but convergence of entire path functionals, justifying Monte Carlo simulation via discrete approximations.

Standard Brownian motion $\{W_t\}_{t \geq 0}$ is the unique process satisfying: 

- (i) $W_0 = 0$
- (ii) independent increments
- (iii) $W_t - W_s \sim \mathcal{N}(0, t-s)$ 
- (iv) continuous paths a.s. 

Its moment structure follows from the Gaussian MGF: 

$$\mathbb{E}[W_t^{2k}] = \frac{(2k)!}{2^k k!}\, t^k$$ 

for even moments, with all odd moments vanishing.

**Path Properties**
Brownian paths exhibit a striking duality: they are continuous yet nowhere differentiable (a.s.), and Holder continuous of order $\alpha < 1/2$ but not $\alpha = 1/2$. The **quadratic variation** 

$$\langle W \rangle_t = t$$ 

is the hallmark property that distinguishes stochastic from classical calculus and gives rise to the Ito correction term. The **self-similarity** 

$$W_{ct} \overset{d}{=} \sqrt{c}\, W_t$$ 

implies Brownian motion has no intrinsic time scale; the Dambis-Dubins-Schwarz theorem extends this, showing every continuous local martingale is Brownian motion run on a random clock.

**Reflection Principle and First Passage Times**
The reflection principle exploits path symmetry to compute

$$\mathbb{P}\!\left(\max_{0 \leq s \leq t} W_s \geq a\right) = 2\,\mathbb{P}(W_t \geq a)$$

for $a > 0$. This yields the first passage time density 

$$f_{\tau_a}(t) = \frac{|a|}{\sqrt{2\pi t^3}} \exp\!\left(-\frac{a^2}{2t}\right)$$ 

an inverse Gaussian distribution. These results directly apply to barrier option pricing and credit risk modeling.

**Filtrations and Adapted Processes**
A filtration $(\mathcal{F}_t)_{t \geq 0}$ models the gradual revelation of information: $\mathcal{F}_t$ encodes precisely what can be known at time $t$. Processes are **adapted** if $X_t$ is $\mathcal{F}_t$-measurable (no looking into the future), and **progressively measurable** if the joint map $(s, \omega) \mapsto X_s(\omega)$ is measurable on $[0,t] \times \Omega$. This hierarchy of measurability conditions ensures that trading strategies and stochastic integrals are well-defined.

**Martingale Theory**
A martingale satisfies $\mathbb{E}[M_t \mid \mathcal{F}_s] = M_s$ for $s \leq t$—the best prediction of the future is the present. Brownian motion is a martingale, as are 

$$W_t^2 - t$$

and the exponential martingale 
 
$$\exp(\theta W_t - \frac{1}{2}\theta^2 t)$$
 
Submartingales ($\mathbb{E}[M_t \mid \mathcal{F}_s] \geq M_s$) and supermartingales model systematically favorable and unfavorable games respectively. Key results include:

- *Stopping times and optional sampling*: the martingale property extends to bounded stopping times $\sigma \leq \tau \leq T$ 

$$\mathbb{E}[M_\tau \mid \mathcal{F}_\sigma] = M_\sigma$$
 
- *Doob's maximal inequality*: for $p > 1$, bounding the running maximum by the terminal value 

$$\mathbb{E}[\sup_{s \leq t} |M_s|^p] \leq (p/(p-1))^p\, \mathbb{E}[|M_t|^p]$$ 



- *Martingale convergence*: bounded $L^1$ martingales converge a.s., controlled by the upcrossing inequality
- *Doob-Meyer decomposition*: every submartingale uniquely decomposes into a martingale $M_t$ and a predictable increasing process $A_t$

$$X_t = M_t + A_t$$

- *Uniform integrability*: the bridge between almost sure and $L^1$ convergence, ensuring that martingales closed by an integrable random variable converge in $L^1$

!!! note "Role in the Book"
    Brownian motion and martingale theory developed here are the essential prerequisites for stochastic calculus (Chapter 3), measure changes and Girsanov's theorem (Chapter 4), and the Feynman-Kac connection between PDEs and expectations (Chapter 5).

---
