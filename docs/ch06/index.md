# Chapter 6: The Black-Scholes Model

This chapter develops the Black-Scholes option pricing framework from first principles. Starting from geometric Brownian motion and self-financing portfolios, we derive the Black-Scholes PDE through four independent approaches, analyze its structure and boundary conditions, solve it using a range of analytic techniques, and arrive at the celebrated closed-form formula for European options.

## Key Concepts

**The Black-Scholes Model**
The model, introduced by Black, Scholes (1973) and Merton (1973), assumes the underlying asset follows geometric Brownian motion with constant drift and volatility:

$$dS_t = \mu S_t\, dt + \sigma S_t\, dW_t$$

Six core assumptions—GBM dynamics, frictionless markets, constant risk-free rate, no dividends, continuous trading, and no arbitrage—make the mathematics tractable and enable closed-form solutions. The self-financing portfolio condition constrains admissible trading strategies and underpins the hedging arguments.

**Four Derivations of the Black-Scholes PDE**
The pricing PDE

$$\frac{\partial V}{\partial t} + rS\frac{\partial V}{\partial S} + \frac{1}{2}\sigma^2 S^2\frac{\partial^2 V}{\partial S^2} = rV$$

is derived via four conceptually distinct routes:

- *Delta hedging*: construct a self-financing portfolio that eliminates stochastic risk, then apply no-arbitrage
- *Risk-neutral pricing*: invoke the fundamental theorem of asset pricing and Girsanov's theorem so that the discounted price is a $\mathbb{Q}$-martingale
- *Change of numéraire*: use the stock as numéraire and the associated martingale measure to obtain the same PDE from pricing invariance
- *Equilibrium*: derive the PDE from a representative-agent economy with CRRA preferences and market clearing, yielding the risk premium endogenously

**PDE Structure and Conditions**
The killing term $rV$ encodes discounting and connects to Feynman-Kac probabilistic representations. The Greeks $\Delta$, $\Gamma$, $\Theta$, $\mathcal{V}$, and $\rho$, emerge as partial derivatives of the PDE solution, linked by the theta-gamma relation 

$$\Theta + rS\Delta + \frac{1}{2}\sigma^2 S^2 \Gamma = rV$$

Terminal and boundary conditions select the unique solution corresponding to a specific contract from the family of PDE solutions.

**Analytic Solution Methods**
The Black-Scholes PDE is solved through multiple techniques:

- *Heat equation reduction*: variable substitutions transform the PDE into the classical heat equation, leveraging its known fundamental solution
- *Separation of variables and similarity solutions*: exploit the PDE's symmetry structure via dimensional analysis and the Buckingham Pi theorem
- *Integral transforms*: Fourier, Mellin, and Laplace transforms convert the PDE into algebraic or ODE problems in transform space
- *Feynman-Kac formula*: bridge PDE and probability theory by representing the solution as a conditional expectation under the risk-neutral measure
- *Change of numéraire*: provide alternative derivations using forward measures and stock-numéraire techniques
- *Viscosity solutions*: handle non-smooth payoffs (digital options) and free-boundary problems (American options) where classical solutions fail

**The Black-Scholes Formula**
For a European call with strike $K$ and maturity $T$:

$$C = S_0\,\mathcal{N}(d_1) - Ke^{-rT}\mathcal{N}(d_2)$$

where 

$$d_{1,2} = \frac{\ln(S_0/K) + (r \pm \frac{1}{2}\sigma^2)T}{\sigma\sqrt{T}}$$ 

The terms $\mathcal{N}(d_1)$ and $\mathcal{N}(d_2)$ are exercise probabilities under the stock-numéraire and money-market-numéraire measures respectively. Put-call parity 

$$C - P = S - Ke^{-r(T-t)}$$ 

relates call and put prices as a no-arbitrage condition. Asymptotic analysis in the limits $S \to 0, \infty$ and $\sigma \to 0, \infty$ confirms financial intuition and serves as a validation check. Digital option pricing illustrates the framework applied to discontinuous payoffs via Girsanov's theorem.

!!! warning "Model Limitations"
    The constant-volatility and frictionless-market assumptions are violated in practice. Later chapters address local volatility, stochastic volatility, jumps, and calibration to market data.

---
