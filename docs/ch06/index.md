# Chapter 6: The Black-Scholes Model

This chapter develops the Black-Scholes option pricing framework from first principles. Starting from geometric Brownian motion and self-financing portfolios, we derive the Black-Scholes PDE through four independent approaches, analyze its structure and boundary conditions, solve it using a range of analytic techniques, and arrive at the celebrated closed-form formula for European options.

## Key Concepts

**The Black-Scholes Model** The model, introduced by Black, Scholes (1973) and Merton (1973), assumes the underlying asset follows geometric Brownian motion with constant drift and volatility:

$$dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$$

Six core assumptions -- GBM dynamics, frictionless markets, constant risk-free rate, no dividends, continuous trading, and no arbitrage -- make the mathematics tractable and enable closed-form solutions. By Ito's lemma, asset prices are log-normally distributed with explicit solution 

$$S_t = S_0 \exp\bigl((\mu - \tfrac{1}{2}\sigma^2)t + \sigma W_t\bigr)$$ 

The model emerges as the continuous-time limit of the binomial framework, inheriting the key insights of dynamic hedging and risk-neutral valuation. The self-financing portfolio condition constrains admissible trading strategies and underpins the hedging arguments that follow.

**Four Derivations of the Black-Scholes PDE** The pricing PDE

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = rV$$

is derived via four conceptually distinct routes:

- *Delta hedging*: construct a self-financing portfolio $\Pi = V - \Delta S$ that eliminates stochastic risk by setting $\Delta = \partial V / \partial S$, then apply no-arbitrage to require $d\Pi = r\Pi\, dt$
- *Risk-neutral pricing*: invoke the fundamental theorem of asset pricing and Girsanov's theorem so that the discounted price $e^{-rt}V$ is a $\mathbb{Q}$-martingale, and set its drift to zero
- *Change of numeraire*: use the stock as numeraire with its associated measure $\mathbb{Q}^S$ via the Radon-Nikodym derivative $Z_t = S_t e^{-rt}/S_0$, and derive the PDE from pricing invariance
- *Equilibrium*: derive the PDE from a representative-agent economy with CRRA preferences, where market clearing yields the equilibrium risk premium $\mu - r = \gamma \sigma^2$ and the stochastic discount factor $M_t = e^{-\rho t} S_t^{-\gamma}$

**PDE Structure and Conditions** The killing term $-rV$ encodes continuous discounting and connects to the Feynman-Kac probabilistic representation 

$$V(t,x) = \mathbb{E}[e^{-r(T-t)}\Phi(X_T) \mid X_t = x]$$ 

The discounted value process $M_s = e^{-r(s-t)}V(s, X_s)$ is a martingale precisely when $V$ solves the pricing PDE. The Greeks $\Delta$, $\Gamma$, $\Theta$, $\mathcal{V}$, and $\rho$ emerge as partial derivatives of the PDE solution, linked by the theta-gamma relation

$$\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma = rV$$

Terminal conditions $V(T,S) = \Phi(S)$ specify the contract payoff (calls, puts, digitals, straddles), while boundary conditions -- Dirichlet, Neumann, or Robin -- select the unique solution from the family of PDE solutions. The PDE smooths non-smooth and discontinuous terminal data for $t < T$.

**Analytic Solution Methods** The Black-Scholes PDE is solved through multiple techniques:

- *Heat equation reduction*: variable substitutions ($\tau = T - t$, $x = \ln S + (r - \tfrac{1}{2}\sigma^2)\tau$, and an exponential scaling) transform the PDE into the classical heat equation, whose fundamental solution is known 

$$\frac{\partial u}{\partial \tau} = \tfrac{1}{2}\sigma^2 \frac{\partial^2 u}{\partial x^2}$$

- *Separation of variables*: assume a product form $u(x,t) = X(x)T(t)$ to reduce the PDE to independent ODEs; on the semi-infinite stock-price domain this yields a continuous spectrum and Fourier transforms rather than discrete eigenvalues
- *Similarity solutions*: exploit scale invariance and the Buckingham Pi theorem to reduce to dimensionless groups $S/K$, $\sigma\sqrt{\tau}$, and $r\tau$, giving the general form 

$$V = K \cdot f(S/K, \sigma\sqrt{\tau}, r\tau)$$

- *Integral transforms*: Fourier, Mellin, and Laplace transforms convert the PDE into first-order ODEs in the transform variable, solved explicitly via characteristic exponents and inverted to recover option prices
- *Feynman-Kac formula*: bridge PDE and probability theory by representing the solution as conditional expectations under the risk-neutral measure, reducing the pricing problem to computing conditional expectations 

$$u(x,t) = \mathbb{E}[e^{-r(T-t)}\Phi(X_T) \mid X_t = x]$$
 
- *Change of numeraire*: provide alternative derivations using forward measures and stock-numeraire techniques, with the Radon-Nikodym derivative connecting different pricing measures
- *Viscosity solutions*: handle non-smooth payoffs (digital options with $\Phi(S) = \mathbf{1}_{S>K}$) and free-boundary problems (American options) where classical $C^2$ solutions fail, using test-function-based sub/supersolution definitions

**The Black-Scholes Formula** For a European call with strike $K$ and maturity $T$:

$$C = S_0\,\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$$

where

$$d_{1,2} = \frac{\ln(S_0/K) + (r \pm \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$$

The term $\mathcal{N}(d_2)$ is the risk-neutral probability of exercise, while $\mathcal{N}(d_1)$ is the exercise probability under the stock-numeraire measure $\mathbb{Q}^S$. 

$$\begin{array}{lll}
\mathcal{N}(d_1) &=& \mathbb{Q}^S(S_T > K)\\
\mathcal{N}(d_2) &=& \mathbb{Q}(S_T > K)
\end{array}$$

The formula can be derived via direct integration of the log-normal density, via Girsanov's theorem and measure change, or as the solution to the heat equation. Put-call parity

$$C - P = S - Ke^{-r(T-t)}$$

relates call and put prices as a model-independent no-arbitrage condition derived from replicating portfolios. Option prices satisfy fundamental bounds, e.g., 

$$\max(S - Ke^{-rT}, 0) \leq C \leq S$$ 

monotonicity, and convexity properties. Asymptotic analysis in the limits $S \to 0, \infty$ and $\sigma \to 0, \infty$ confirms financial intuition: deep ITM calls behave like forward contracts ($C \to S - Ke^{-rT}$) and deep OTM calls become worthless. Digital option pricing $D_0 = e^{-rT}\Phi(d_2)$ illustrates the framework applied to discontinuous payoffs.

!!! note "Role in the Book"
    This chapter unifies the stochastic calculus tools from earlier chapters into a complete pricing framework. The four PDE derivations highlight how no-arbitrage, martingale theory, numeraire invariance, and general equilibrium all converge on the same equation. The analytic solution methods -- from heat equation reduction to viscosity solutions -- form the mathematical toolkit extended in later chapters to local volatility, stochastic volatility, jump-diffusion models, and numerical PDE methods.

---
